A lightweight Python application that reads a JSON file of piano notes and renders a single WAV file.

## Usage

Install dependencies:

```sh
uv sync
```

Render the sample sequence:

```sh
uv run piano-sequencer --config sequence.json --out output.wav
```

The JSON format uses beats for `duration`, with `tempo` in beats per minute:

```json
{
  "tempo": 120,
  "track": [
    {"note": "C4", "duration": 0.5, "effect": "none"},
    {"note": "E4", "duration": 0.5, "effect": "none"},
    {"note": "G4", "duration": 1.0, "effect": "reverb"}
  ]
}
```

Supported effects are `none` and `reverb`.
