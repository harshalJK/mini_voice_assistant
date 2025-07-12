# tts.py
import pyttsx3

def speak(text):
    print("🔊 Speaking...")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()