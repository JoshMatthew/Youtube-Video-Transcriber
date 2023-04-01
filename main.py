import os
from pytube import YouTube
import whisper
import pandas as pd
import subprocess
import curses


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu(stdscr):
    curses.curs_set(0)
    current_row = 0

    choices = ["YouTube URL", "File path"]

    while True:
        stdscr.clear()
        for idx, choice in enumerate(choices):
            if idx == current_row:
                stdscr.addstr(idx, 0, choice, curses.A_REVERSE)
            else:
                stdscr.addstr(idx, 0, choice)
        key = stdscr.getch()

        if key == curses.KEY_UP:
            current_row = max(0, current_row - 1)
        elif key == curses.KEY_DOWN:
            current_row = min(len(choices) - 1, current_row + 1)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return current_row

        stdscr.refresh()


clear_console()

choice = curses.wrapper(menu)

if choice == 0:
    yt_url = input("Enter the YouTube video URL: ")
    audio_file = YouTube(yt_url).streams.filter(
        only_audio=True).first().download(filename="audio.mp4")
elif choice == 1:
    audio_file = input("Enter the file path: ")

print("Transcribing audio file...")
whisper_model = whisper.load_model("tiny")

transcription = whisper_model.transcribe(audio_file)

df = pd.DataFrame(transcription['segments'], columns=['start', 'end', 'text'])

df.to_csv('transcribed.txt', sep='\t', index=False)

print("DONE")
subprocess.run(['notepad.exe', 'transcribed.txt'])
