# 🎙️ Example Project: Audio Transcription App (OpenAI Whisper)

## 📦 Step 1: Install requirements

You need Python 3.9+
```
pip install openai-whisper
pip install torch
```
On some systems, torch installs automatically.

## Step 2: Download ffmpeg (most likely required)

### 1️⃣ What is FFmpeg? (quickly)

FFmpeg is a powerful tool for:
- Converting video/audio formats
- Extracting audio
- Cutting, merging media

### 2️⃣ Download FFmpeg (Windows)

Open your browser

Go to:
https://www.gyan.dev/ffmpeg/builds/

Download:
👉 ffmpeg-release-essentials.zip

(“Essentials” is enough for most users)

### 3️⃣ Extract FFmpeg

Right-click the downloaded .zip

Click Extract All

Move the extracted folder to a simple location, for example:
```
C:\ffmpeg
```

Inside it you should see:
```
C:\ffmpeg\bin\ffmpeg.exe
```

✅ This file is the FFmpeg program

### 4️⃣ Add ffmpeg folder to Path environment variable

<img src="ffmpeg_path.gif" alt="FFmpeg path" width="1000">


-> Then Sign Out from Windows or Restart computer

### 5️⃣ Verify installation

Run in terminal:
```
ffmpeg -version
```

✅ Correct output looks like:
ffmpeg version 6.x ...

If you see this → FFmpeg is installed correctly


## 📁 Step 2: Prepare an audio file

Put an audio file in your project folder, for example:
```
speech.mp3
```
(You can record a short voice note on your phone and transfer it.)

## 🧑‍💻 Step 3: Simple Whisper Transcription Code
```
import whisper

# Load Whisper model (small = fast)
model = whisper.load_model("small")

# Transcribe audio
result = model.transcribe("speech.mp3")

# Print text
print("Transcription:")
print(result["text"])
```
▶️ Run the project
```
python transcribe.py
```
