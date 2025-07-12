import sounddevice as sd
from scipy.io.wavfile import write
import whisper

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

def record_audio(filename="input.wav", duration=5, samplerate=44100, device=0):
    print(f"🎙️ Recording from device {device} ...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, device=device)
    sd.wait()
    write(filename, samplerate, audio)
    print("✅ Recording saved as", filename)
    return filename

def transcribe_audio(filename="input.wav"):
    print("🚀 Loading model...")
    model = whisper.load_model("base")
    print("🧠 Transcribing...")
    result = model.transcribe(filename)
    print("📝 You said:", result["text"])
    return result["text"]

if __name__ == "__main__":
    list_input_devices()
    selected_device = get_user_device()
    filename = record_audio(device=selected_device)
    transcribe_audio(filename)
