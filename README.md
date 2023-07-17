# Whisper-cpp python audio transcription tool

## Description
This `s2tutil` command line tool is used to transcribe audio files to text using the python bridging of Whisper.cpp. 

## Usage

```bash
s2tutil -m <model_name> --audio-dir <audio-directory> --append-to-csv <append-to-csv>
```

### Options

- `model_name`: The name of the model to use for transcription. It should be one of the following values. Please note, larger models are more accurate but will need significantly more memory take longer to transcribe audio clips.

    - tiny.en
    - tiny
    - base.en
    - base
    - small.en
    - small
    - medium.en
    - medium
    - large-v1
    - large

- `audio_dir`: The directory containing the audio files to transcribe. The audio files should be in the `.wav` format.

- `append_to_csv`: The path to a csv file to append the transcription results to. If the file does not exist, it will be created. If the file does exist, the results will be appended to the end of the file. The csv file will have the following format:

    ```csv
    <audio_file_name>,<transcription>,<audio_length>
    ```

    For example:

    ```csv
    audio1.wav,This is the transcription of audio1.wav, 10,0
    audio2.wav,This is the transcription of audio2.wav, 11.0
    ```