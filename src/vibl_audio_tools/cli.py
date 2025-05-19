"""Console script for vibl_audio_tools."""
import vibl_audio_tools

import typer
from rich.console import Console
from vibl_audio_tools.remove_silences import remove_silences, generate_output_file_path, DEFAULT_MIN_SILENCE_LEN, DEFAULT_SILENCE_THRESHOLD, DEFAULT_PADDING, DEFAULT_OUTPUT_BITRATE

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for vibl_audio_tools."""
    console.print("Replace this message by putting your code into "
               "vibl_audio_tools.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")



@app.command()
def remove_silences_cli(
    input_file: str = typer.Argument(..., help="Path to the input audio file."),
    output_dir: str = typer.Option("./silenced_removed", help="Absolute or relative path to the output directory."),
    output_file: str = typer.Option(None, help="Path to the output audio file."),
    min_silence_len: int = typer.Option(DEFAULT_MIN_SILENCE_LEN, help=f"Minimum length of a silence to be considered in ms. Default is {DEFAULT_MIN_SILENCE_LEN} ms."),
    silence_threshold: int = typer.Option(DEFAULT_SILENCE_THRESHOLD, help=f"Silence threshold in dB. Default is {DEFAULT_SILENCE_THRESHOLD} dB."),
    padding: int = typer.Option(DEFAULT_PADDING, help=f"Amount of padding to leave around non-silent sections in ms. Default is {DEFAULT_PADDING} ms."),
    output_bitrate: str = typer.Option(DEFAULT_OUTPUT_BITRATE, help=f"Bitrate of the output audio file. Default is '{DEFAULT_OUTPUT_BITRATE}'."),
    print_parameters: bool = typer.Option(False, help="Print all parameters.")
):
    """Remove silences from an audio file."""
    final_output_file = output_file if output_file else generate_output_file_path(output_dir, input_file)
    if print_parameters:
        console.print("Running with the following parameters:")
        console.print(f"Input File: {input_file}")
        console.print(f"Output File: {final_output_file}")
        console.print(f"Min Silence Length: {min_silence_len} ms")
        console.print(f"Silence Threshold: {silence_threshold} dB")
        console.print(f"Padding: {padding} ms")
        console.print(f"Output Bitrate: {output_bitrate}")
    remove_silences(
        input_file=input_file,
        output_dir=output_dir,
        output_file=final_output_file,
        min_silence_len=min_silence_len,
        silence_threshold=silence_threshold,
        padding=padding,
        output_bitrate=output_bitrate
    )
    console.print(final_output_file)


if __name__ == "__main__":
    app()
