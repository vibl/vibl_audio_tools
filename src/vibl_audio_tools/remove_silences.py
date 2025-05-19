from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import argparse
import os  # Required for directory operations

# Default configuration
DEFAULT_MIN_SILENCE_LEN = 1000
DEFAULT_SILENCE_THRESHOLD = -50
DEFAULT_PADDING = 300
DEFAULT_OUTPUT_BITRATE = "32k"

def get_extension(file_name):
    return file_name.split(".")[-1]

def get_base_name(file_path):
    base_name = os.path.basename(file_path)  # get the base name of the file
    file_name = os.path.splitext(base_name)[0]  # remove the extension
    return file_name

def generate_output_file_path(output_dir, input_file):
    output_dir_path = output_dir if os.path.isabs(output_dir) else os.path.abspath(os.path.join(os.path.dirname(input_file), output_dir))
    os.makedirs(output_dir_path, exist_ok=True)  # Create the directory if it doesn't exist
    base_name = get_base_name(input_file)
    extension = get_extension(input_file)
    output_ext = "mp3" if (extension == "m4a") or not extension else extension
    output_file_path = os.path.join(output_dir_path, base_name + '.' + output_ext)
    return output_file_path

def remove_silences(input_file, output_dir, output_file, min_silence_len=DEFAULT_MIN_SILENCE_LEN, silence_threshold=DEFAULT_SILENCE_THRESHOLD, padding=DEFAULT_PADDING, output_bitrate=DEFAULT_OUTPUT_BITRATE):
    """
    Remove silences from an audio file and preserve specified padding around non-silent ranges.

    :param input_file: Path to the input audio file.
    :param output_file: Path to the output audio file.
    :param min_silence_len: Minimum duration of silence in ms. Default is 1000 ms.
    :param silence_thresh: Silence threshold in dB. Default is -30 dB.
    :param padding: Amount of silence to preserve before and after non-silent ranges in ms. Default is 100 ms.
    :param output_bitrate: Bitrate of the output audio file. Default is "192k".

    """

    input_format = get_extension(input_file)

    if not output_file:
        output_file = generate_output_file_path(output_dir, input_file)

    input_audio = AudioSegment.from_file(input_file, format=input_format)

    # Detect non-silent ranges in the audio
    nonsilent_ranges = detect_nonsilent(input_audio, min_silence_len, silence_threshold, seek_step=100)

    # Concatenate non-silent ranges and preserve silence padding
    output_audio = AudioSegment.empty()

    for start, end in nonsilent_ranges:
        start = max(0, start - padding)
        end = min(len(input_audio), end + padding)
        output_audio += input_audio[start:end]

    # Export the output audio file
    output_audio.export(output_file, format=get_extension(output_file), bitrate=output_bitrate)

    print(output_file)