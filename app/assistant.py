from app.audio.speech_to_text import speech_to_text
from app.audio.text_to_speech import text_to_speech
from app.chatgpt_api import get_chatgpt_response

def run_assistant():
    text = speech_to_text()
    if text:
        print(f"You said: {text}")
        response = get_chatgpt_response(text)
        print(f"ChatGPT: {response}")
        text_to_speech(response)
