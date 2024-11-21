# Gemini AI Chatbot

Welcome to the **Gemini AI Chatbot**, a multi-modal conversational assistant powered by Google's Generative AI API. This chatbot is designed to offer seamless interaction through text, voice, and even images, making it versatile and easy to use. It features advanced functionalities such as speech recognition, text-to-speech, and detailed interaction logging, all while maintaining a user-friendly design.

---

## How It Works

The Gemini AI Chatbot is built to provide an intuitive and interactive experience. Depending on your input method, it can process:
1. **Text Commands:** Type your questions or prompts directly.
2. **Voice Inputs:** Speak to the chatbot for a hands-free experience.
3. **Image Analysis:** Upload an image, and the chatbot will describe it or provide insights based on a custom prompt.

The chatbot is backed by Google's Generative AI models, ensuring high-quality responses for a variety of input types.

---

## Features

### 1. Multi-Modal Input
- **Text Input**: Communicate with the chatbot by typing.
- **Voice Input**: Use a microphone to speak directly to the chatbot.
- **Image Analysis**: Analyze images and generate descriptions or insights using AI.

### 2. Text-to-Speech Output
The chatbot can convert its responses into speech, offering a more engaging interaction experience.

### 3. Logging
Every interaction (text, voice, or image) can be logged, allowing users to review conversations later.

### 4. Custom Prompts
For image analysis, you can provide specific prompts to guide the chatbot's responses.

---

## File Structure

Here’s a breakdown of the key components in the project:

- **`gemini.py`**: The main program file containing all the chatbot logic.
- **`requirements.txt`**: A list of dependencies needed to run the chatbot.
- **`logs/`**: A directory where interaction logs are stored automatically.

---

## Installation

Follow these steps to set up and run the chatbot:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/chatbot.git
cd chatbot
```

### 2. Install Dependencies
Ensure you have Python 3.7+ installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Set Up API Key
The chatbot uses Google Generative AI. Replace the `API_KEY` placeholder in `chatbot.py` with your actual API key. To improve security, store the key in an environment variable or a configuration file in production.

---

## Usage

Run the chatbot using the command line. Here are some example commands and options:

### Basic Command
```bash
python chatbot.py
```

### Command-Line Options
| Option             | Description                                         |
|--------------------|-----------------------------------------------------|
| `--text`           | Enable text-based input.                            |
| `--voice`          | Enable voice-based input.                           |
| `--image <path>`   | Specify the path to an image for analysis.          |
| `--prompt <text>`  | Custom prompt for image analysis.                   |
| `--speak`          | Enable text-to-speech output for responses.         |
| `--log`            | Enable detailed logging of conversations.           |

### Example Scenarios

1. **Text Interaction:**
   ```bash
   python chatbot.py --text
   ```
   This enables the chatbot to interact with you via text commands.

2. **Voice Interaction with Logging:**
   ```bash
   python chatbot.py --voice --log
   ```
   Speak to the chatbot, and all interactions will be logged.

3. **Image Analysis:**
   ```bash
   python chatbot.py --image /path/to/image.jpg --prompt "Describe the emotions in this image."
   ```
   The chatbot will analyze the image and provide insights based on your custom prompt.

---

## Code Walkthrough

### Key Components

1. **Speech Recognition (`speech_recognition`):**
   - Captures and processes voice inputs.
   - Handles errors gracefully when speech cannot be understood or recognized.

2. **Text-to-Speech (`pyttsx3`):**
   - Converts the chatbot's responses into speech for an auditory experience.
   - Configurable for different voices and languages.

3. **Image Analysis (`Pillow` and `google.generativeai`):**
   - Loads and processes images.
   - Uses Google's AI to analyze and respond to image-based prompts.

4. **Logging (`logging`):**
   - Logs interactions to both the console and log files for future reference.
   - Supports separate logs for each day.

5. **Command-Line Argument Parsing (`argparse`):**
   - Provides flexibility to choose input methods and configure options.

### Core Functions

- **`parse_arguments`**: Parses command-line options and validates inputs.
- **`text_input`**: Handles text-based interaction with the user.
- **`voice_input`**: Processes voice commands using a microphone.
- **`image_analysis`**: Analyzes an uploaded image and generates a detailed response.
- **`text_to_speech`**: Speaks out the chatbot's response.
- **`log_interaction`**: Saves interactions to log files.

---

## Troubleshooting

### Common Issues

1. **Missing Dependencies**:
   Ensure all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

2. **Speech Recognition Errors**:
   - Ensure your microphone is connected and working.
   - Avoid noisy environments when speaking to the chatbot.

3. **Image Analysis Errors**:
   - Make sure the image file exists and is a valid format (e.g., JPG, PNG).
   - Provide a clear and specific custom prompt for better results.

---

## Enhancements and Future Plans

- **Expand Model Options**: Incorporate more AI models for broader functionality.
- **Web Interface**: Build a web-based UI for easier interaction.
- **Custom Training**: Train the chatbot for domain-specific applications.

---

## Security Considerations

- Avoid hardcoding sensitive data like API keys in production. Use secure methods like environment variables or secrets management systems.
- Ensure log files containing sensitive information are stored securely.

---

## License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it as per the terms of the license.

---

## Acknowledgments

Special thanks to:
- **Google Generative AI API** for providing powerful AI models.
- The developers of Python libraries like `speech_recognition`, `pyttsx3`, and `Pillow`.

Happy coding! 🚀
