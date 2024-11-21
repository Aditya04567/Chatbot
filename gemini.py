import google.generativeai as genai
import sys
import argparse
import shlex
import datetime
import speech_recognition as sr
import pyttsx3
import os
from PIL import Image
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler('chatbot.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

# API Configuration (IMPORTANT: Replace with secure method in production)
API_KEY = "AIzaSyB6bPpOTHgHD1tu5Jdg85Rh9vqMgBy6BJk"

class GeminiChatbot:
    def __init__(self):
        # Initialize recognizer and text-to-speech engine
        self.recognizer = sr.Recognizer()
        self.speech_engine = pyttsx3.init()
        
        # Configure Gemini API
        genai.configure(api_key=API_KEY)

    def parse_arguments(self):
        """
        Parse command-line arguments with robust handling
        """
        parser = argparse.ArgumentParser(
            description="Gemini AI Chatbot with Multi-Modal Input",
            epilog="Support for text, voice, and image-based interactions"
        )
        
        # Input method arguments
        parser.add_argument(
            "--text", 
            action='store_true', 
            help="Enable text-based input"
        )
        parser.add_argument(
            "--voice", 
            action='store_true', 
            help="Enable voice-based input"
        )
        parser.add_argument(
            "--image", 
            type=self.validate_image_path, 
            help="Path to image file for analysis"
        )
        
        # Additional configuration arguments
        parser.add_argument(
            "--prompt", 
            nargs='*', 
            default=["Describe this image in detail"],
            help="Custom prompt for image analysis"
        )
        parser.add_argument(
            "--speak", 
            action='store_true', 
            help="Enable text-to-speech output"
        )
        parser.add_argument(
            "--log", 
            action='store_true', 
            help="Enable detailed logging"
        )

        # Use shlex for more robust parsing
        try:
            args = parser.parse_args(shlex.split(' '.join(sys.argv[1:])))
            
            # Convert prompt list to string
            if isinstance(args.prompt, list):
                args.prompt = ' '.join(args.prompt)
            
            return args
        except Exception as e:
            logging.error(f"Argument parsing error: {e}")
            sys.exit(1)

    def validate_image_path(self, path):
        """
        Validate and normalize image file path
        """
        try:
            # Normalize path
            normalized_path = os.path.normpath(path)
            
            # Check file exists and is an image
            if not os.path.exists(normalized_path):
                raise argparse.ArgumentTypeError(f"Image file not found: {normalized_path}")
            
            # Check file is an image
            Image.open(normalized_path)
            
            return normalized_path
        except Exception as e:
            raise argparse.ArgumentTypeError(f"Invalid image file: {e}")

    def text_input(self):
        """
        Handle text-based input
        """
        try:
            user_input = input("You: ").strip()
            return user_input
        except Exception as e:
            logging.error(f"Text input error: {e}")
            return None

    def voice_input(self):
        """
        Handle voice-based input using speech recognition
        """
        try:
            print("Speak now... (listening)")
            
            with sr.Microphone() as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                # Listen to audio
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                
                # Recognize speech
                user_input = self.recognizer.recognize_google(audio).lower()
                print(f"Recognized: {user_input}")
                
                return user_input
        except sr.UnknownValueError:
            logging.warning("Could not understand audio")
        except sr.RequestError as e:
            logging.error(f"Speech recognition error: {e}")
        except Exception as e:
            logging.error(f"Unexpected voice input error: {e}")
        
        return None

    def image_analysis(self, image_path, prompt):
        """
        Analyze image using Gemini API
        """
        try:
            # Load image
            img = Image.open(image_path)
            
            # Use Pro model for multimodal input
            model = genai.GenerativeModel("gemini-1.5-pro")
            
            # Generate response
            response = model.generate_content([img, prompt])
            
            return response.text
        except Exception as e:
            logging.error(f"Image analysis error: {e}")
            return None

    def text_to_speech(self, text):
        """
        Convert text to speech
        """
        try:
            self.speech_engine.say(text)
            self.speech_engine.runAndWait()
        except Exception as e:
            logging.error(f"Text-to-speech error: {e}")

    def log_interaction(self, input_type, user_input, response):
        """
        Log interactions to file
        """
        try:
            log_dir = os.path.join(os.getcwd(), 'logs')
            os.makedirs(log_dir, exist_ok=True)
            
            log_file = os.path.join(log_dir, f"chat_{datetime.date.today()}.log")
            
            with open(log_file, 'a', encoding='utf-8') as f:
                log_entry = (
                    f"[{datetime.datetime.now()}]\n"
                    f"Input Type: {input_type}\n"
                    f"User Input: {user_input}\n"
                    f"Response: {response}\n\n"
                )
                f.write(log_entry)
        except Exception as e:
            logging.error(f"Logging error: {e}")

    def chat(self, args):
        """
        Main chat logic
        """
        try:
            # Image analysis takes precedence
            if args.image:
                response = self.image_analysis(args.image, args.prompt)
                
                if response:
                    print("Image Analysis: ", response)
                    
                    if args.speak:
                        self.text_to_speech(response)
                    
                    if args.log:
                        self.log_interaction('image', args.image, response)
                
                return

            # Determine input method
            while True:
                if args.text:
                    user_input = self.text_input()
                elif args.voice:
                    user_input = self.voice_input()
                else:
                    logging.error("No input method specified")
                    break

                # Exit conditions
                if not user_input or user_input.lower() in ['quit', 'exit', 'bye']:
                    break

                # Generate response
                try:
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    response = model.generate_content(user_input).text
                    
                    print("Chatbot: ", response)
                    
                    # Text-to-speech if enabled
                    if args.speak:
                        self.text_to_speech(response)
                    
                    # Logging if enabled
                    if args.log:
                        self.log_interaction('text', user_input, response)
                
                except Exception as e:
                    logging.error(f"Chat generation error: {e}")
                    break

        except Exception as e:
            logging.error(f"Unexpected chat error: {e}")

def main():
    """
    Main application entry point
    """
    try:
        # Initialize chatbot
        chatbot = GeminiChatbot()
        
        # Parse arguments
        args = chatbot.parse_arguments()
        
        # Start chat
        chatbot.chat(args)
    
    except KeyboardInterrupt:
        print("\nChat terminated by user.")
    except Exception as e:
        logging.error(f"Application error: {e}")

if __name__ == "__main__":
    main()