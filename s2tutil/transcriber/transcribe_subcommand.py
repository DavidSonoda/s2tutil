import click
import wave
from s2tutil.util import downloader
from whispercpp import Whisper
from os import walk, path, environ

DEFAULT_CSV_FILE = "transcriptions.csv"


@click.command(help="Transcribe audio files using whisper.cpp models")
@click.option(
    "--model", "-m", default="small.en", help="Model name to use for transcription"
)
@click.option("--audio-dir", help="Directory containing audio files to transcribe")
@click.option(
    "--append-to-csv", help="Path to CSV file to append transcriptions to", default=None
)
def transcribe(model: str, audio_dir: str, append_to_csv: str = None):
    downloader.download_model(model)
    w = Whisper.from_pretrained(model)
    # Walk through the audio directory and transcribe each wav file
    result = []
    for root, dirs, files in walk(audio_dir):
        for file in files:
            if file.endswith(".wav"):
                click.echo(f"...Transcribing {file}...")
                full_path = path.join(root, file)

                # If full_path is not an absolute path, make it an absolute path, the absolute path should
                # not contain any dots
                if not path.isabs(full_path):
                    full_path = path.abspath(full_path)

                text = w.transcribe_from_file(full_path)
                # Get audio length using whispercpp.utils
                audio_length = get_wav_duration(full_path)

                # Write the transcription to the CSV file
                csv_path = None
                if append_to_csv is None:
                    # Create the CSV file in the current working directory
                    csv_path = path.join(environ.get("PWD"), DEFAULT_CSV_FILE)
                else:
                    # If append_to_csv is a relative path, create the CSV file in the current working directory
                    if not path.isabs(append_to_csv):
                        csv_path = path.join(environ.get("PWD"), append_to_csv)
                    else:
                        csv_path = append_to_csv

                result.append((full_path, text, audio_length))

    # Create the CSV file if it doesn't exist
    mode = ""
    if not path.exists(csv_path):
        mode = "w"
    else:
        mode = "a"

    with open(csv_path, mode) as csv_file:
        if mode == "w":
            csv_file.write("path,text,audio_length\n")
        for full_path, text, audio_length in result:
            csv_file.write(f"{full_path},{text},{audio_length}\n")
        csv_file.close()


def get_wav_duration(filename):
    with wave.open(filename, "rb") as audio_file:
        # Get the number of frames in the WAV file
        num_frames = audio_file.getnframes()

        # Get the frame rate (number of frames per second)
        frame_rate = audio_file.getframerate()

        # Calculate the duration of the WAV file in seconds
        duration = num_frames / float(frame_rate)

    return duration


# print(whispercpp.utils.available_audio_devices())
