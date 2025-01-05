import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    mic_index = int(input("Enter the microphone index to use: "))  # Specify index manually
    with sr.Microphone(device_index=mic_index) as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Calibrate to noise
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand the speech."
    except sr.RequestError:
        return "Speech recognition service is unavailable."