# Audio Transcription Tool

A simple Python-based audio transcription tool that supports transcribing audio from YouTube videos or local audio files. This project uses the `pytube` and `whisper` libraries to fetch and transcribe audio.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Notes](#notes)

## Requirements

- Python 3.6 or higher
- `pytube` library
- `whisper` library
- `pandas` library

## Installation

1. Clone the repository:
git clone https://github.com/JoshMatthew/Youtube-Video-Transcriber.git
2. Change directory to the cloned repository:
cd audio-transcription-tool
3. Install the required dependencies:
pip install -r requirements.txt


## Usage

1. Run the script: 
python main.py

2. Follow the on-screen instructions to choose whether to transcribe audio from a YouTube video or a local audio file.

3. If you choose to transcribe a YouTube video, enter the video URL when prompted. If you choose to transcribe a local audio file, enter the file path when prompted.

4. Wait for the transcription to complete. The transcribed text will be saved to a file named `transcribed.txt` and opened in Notepad.

## Notes

- The script has been tested on Windows and WSL. If you're using WSL, you need to mount your Windows file system to access files from the Windows environment.
