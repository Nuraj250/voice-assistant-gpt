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
