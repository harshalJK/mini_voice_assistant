from stt import record_audio, transcribe_audio
from llm import ask_llm
from tts import speak
import sounddevice as sd

def list_input_devices():
    print("🎤 Available input devices:")
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        if device['max_input_channels'] > 0:
            print(f"{i:>3}: {device['name']} ({device['hostapi']})")
    print()

def get_user_device():
    try:
        index = int(input("🎛️ Enter the device index you want to use for recording: "))
        return index
    except ValueError:
        print("❌ Invalid input. Defaulting to device 0.")
        return 0

def main():
    try:
        list_input_devices()
        device_index = get_user_device()
        audio_file = record_audio(device=device_index)
        text = transcribe_audio(audio_file)
        response = ask_llm(text)
        speak(response)
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
