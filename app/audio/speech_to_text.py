import speech_recognition as sr

def detect_microphones():
    """List all available microphones and prompt user to select one."""
    mic_list = sr.Microphone.list_microphone_names()
    print("Available microphones:")
    for index, name in enumerate(mic_list):
        print(f"{index}: {name}")
    mic_index = int(input("Enter the microphone index to use: "))
    return mic_index

def speech_to_text():
    """Perform speech recognition using the selected microphone."""
    recognizer = sr.Recognizer()
    print("Detecting microphones...")
    mic_index = detect_microphones()  # Detect and select a microphone
    print(f"Using microphone {mic_index}: {sr.Microphone.list_microphone_names()[mic_index]}")
    try:
        with sr.Microphone(device_index=mic_index) as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Calibrate to background noise
            audio = recognizer.listen(source)  # Capture audio
        # Recognize speech using Google's API
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand the speech."
    except sr.RequestError:
        return "Speech recognition service is unavailable."
