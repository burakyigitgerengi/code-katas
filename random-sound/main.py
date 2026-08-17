import time
import os
from pathlib import Path

# Hides pygame support prompt
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

from pygame import error as pygame_error
from pygame import mixer
import random

# Get current working directory
CWD = os.getcwd()


# Custom Exceptions
class FolderInitError(Exception):
    def __init__(self) -> None:

        super().__init__()

    def __str__(self) -> str:
        return "Error initializing the audio folder."


# Functions
def init_mixer():

    try:
        mixer.init()

    except pygame_error as e:
        print("Audio initialization has failed!", e)


def create_audio_folder(name="audio"):

    target = Path(CWD) / name
    if not Path.exists(target):
        target.mkdir(parents=True, exist_ok=True)
        print('"Audio folder created"')
        return target

    if Path.exists(target):
        return target

    else:
        raise FolderInitError()


def play_music(folder: str, file: str):

    try:
        mixer.music.load(f"{folder}/{file}")
        mixer.music.play()

    except pygame_error as e:
        print("Audio playing failed: ", e)


def extract_files_from_folder(folder: str):

    extracted_files_from_folder = [
        file for file in os.listdir(folder) if file.endswith((".mp3"))
    ]

    if extracted_files_from_folder:
        print(f"{len(extracted_files_from_folder)} audio files have been loaded.")
        return extracted_files_from_folder
    else:
        raise FileNotFoundError(
            "No files found matching the format, read the manual if needed."
        )


def random_selection(lst: list):
    return random.choice(lst)


def main():

    try:

        init_mixer()
        audio_folder = create_audio_folder()
        extracted_files = extract_files_from_folder(str(audio_folder))
        random_selection_from_folder = random_selection(list(extracted_files))
        play_music(str(audio_folder), random_selection_from_folder)

        # don't remove this code, otherwise script exits (start)
        while mixer.music.get_busy():
            time.sleep(0.1)
        # don't remove this code, otherwise script exits (end)

    except FileNotFoundError as e:
        # Catch the empty folder error and print just the message
        print(f"\n[Notice] {e}")
        print("Please add some .mp3 files to the 'audio' folder and try again.\n")

    except KeyboardInterrupt:
        print("\nPlayback stopped by user. Exiting safely...")
        mixer.music.stop()


if __name__ == "__main__":
    main()
