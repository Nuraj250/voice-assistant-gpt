# Voice Assistant with ChatGPT

A voice-enabled AI assistant that uses speech recognition, OpenAI's ChatGPT for responses, and text-to-speech synthesis to communicate. It can run on both a laptop and phone for seamless interaction.

## Features
- **Speech-to-Text**: Converts voice input to text using `SpeechRecognition`.
- **ChatGPT Integration**: Processes the text input and generates intelligent responses.
- **Text-to-Speech**: Converts ChatGPT's responses into spoken language using `pyttsx3`.
- **Device Compatibility**: Works on both laptops and phones with optional Flask-based communication.

---

## Project Structure
```plaintext
voice-assistant/
├── app/
│   ├── __init__.py
│   ├── audio/
│   │   ├── speech_to_text.py    # Handles audio-to-text
│   │   ├── text_to_speech.py    # Handles text-to-audio
│   ├── assistant.py             # Main assistant logic
│   ├── chatgpt_api.py           # Handles API requests to ChatGPT
│   ├── device_communication.py  # Handles communication between devices
│   └── utils/
│       ├── audio_recorder.py    # Captures audio from phone or laptop
│       └── config.py            # Configuration (e.g., API keys)
├── requirements.txt             # Dependencies
├── README.md                    # Project documentation
└── run.py                       # Entry point
```

---

## Installation

### Prerequisites
- Python 3.8 or later
- Microphone-enabled device (laptop or phone)
- OpenAI API Key ([Get it here](https://platform.openai.com/signup/))

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/voice-assistant-gpt.git
   cd voice-assistant-gpt
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API Key:
   Edit `app/chatgpt_api.py` and replace `"your_openai_api_key"` with your OpenAI API key.

4. Run the assistant:
   ```bash
   python run.py
   ```

---

## Usage
1. Speak into the microphone when prompted.
2. The assistant will transcribe your speech, process it using ChatGPT, and respond via speech.

---

## Optional: Device Communication
To interact with the assistant from a phone:
1. Start the Flask server:
   ```bash
   python app/device_communication.py
   ```
2. Use a tool like Termux or any HTTP client to send audio files to the server.

---

## Future Enhancements
- Add offline speech recognition (e.g., Vosk).
- Improve natural conversation flow with memory/context.
- Convert the project into a mobile app.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
- [OpenAI](https://openai.com) for ChatGPT API
- [SpeechRecognition Library](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
```

---