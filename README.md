# 🗣️ Mini Voice Assistant

A simple voice assistant that:
- Listens to your speech via microphone 🎙️
- Transcribes it using OpenAI Whisper 🧠
- Sends the text to a language model 🤖
- Speaks the response out loud 🔊

---

## 🔧 Features

- 🎛️ Input device selection
- 🎙️ Audio recording with `sounddevice`
- 🧠 Transcription using Whisper
- 💬 Text-to-text response from LLM (e.g., OpenAI GPT-3.5)
- 🔊 Speech playback via `pyttsx3`

---

## 📦 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## FFmpeg (Required for Whisper)
- Whisper requires FFmpeg to process audio.

### 👉 Install FFmpeg:
- Download from: https://ffmpeg.org/download.html

- Extract the ZIP archive

- Add the bin/ folder path (e.g., C:\ffmpeg\bin) to your System PATH


## LLM API Key
- This project is compatible with any LLM provider that supports chat-style completions.

- You must provide your own API key in llm.py.

### Example using OpenAI:

```bash
from openai import OpenAI
client = OpenAI(api_key="sk-...")  # Replace with your key
```

## How to Use
1. Clone this repo
```bash
git clone https://github.com/YOUR_USERNAME/mini_voice_assistant.git
cd mini_voice_assistant
```
2. Set up virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # (Windows)
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the app
```bash
python main.py
```
### The assistant will:

1. List available input devices

2. Let you select your microphone

3. Record your voice

4. Transcribe it using Whisper

5. Get a response from the LLM

6. Speak it aloud using TTS

## Project Structure

mini_voice_assistant\
├── main.py        # Entry point\
├── stt.py         # Speech-to-text logic\
├── llm.py         # Language model communication\
├── tts.py         # Text-to-speech\
├── requirements.txt\
├── README.md\
└── .gitignore
