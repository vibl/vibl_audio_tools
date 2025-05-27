
# USAGE

`uv run python src/vibl_audio_tools/cli.py remove-silences-cli <input_file> <output_dir> <output_file>`

# EXAMPLES

```
uv run python src/vibl_audio_tools/cli.py remove-silences-cli data/input.mp3 data/output/ output.mp3
```

```
uv run python src/vibl_audio_tools/cli.py remove-silences-cli data/input.mp3 data/output/ output.mp3 --min-silence-len 1000 --silence-threshold -40 --padding 100 --output-bitrate 128k
```