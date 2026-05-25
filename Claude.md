# Claude.md

## Project Context

This workspace contains a small Python project for turning a JSON music sequence into a WAV file. The original project plan is in `Todo.md`, and the implemented application lives in `piano_sequencer/`.

The app reads `sequence.json`, validates the note data, synthesizes simple piano-like tones with NumPy, applies a basic ADSR envelope and optional reverb, then writes a `.wav` file with SciPy.

## Current Layout

```text
.
├── Claude.md
├── Todo.md
└── piano_sequencer/
    ├── Makefile
    ├── README.md
    ├── docs/
    │   └── sequence-json-guide.md
    ├── main.py
    ├── piano_sequencer/
    │   ├── __init__.py
    │   ├── compiler.py
    │   ├── export.py
    │   ├── main.py
    │   ├── models.py
    │   ├── notes.py
    │   ├── parser.py
    │   └── synth.py
    ├── pyproject.toml
    ├── sequence.json
    ├── tests/
    │   └── test_sequencer.py
    └── uv.lock
```

## Important Files

- `Todo.md`: Original checklist. Items have been marked complete for the current implemented slice.
- `piano_sequencer/sequence.json`: Sample song file. Currently contains a basic "Twinkle Twinkle Little Star" melody.
- `piano_sequencer/docs/sequence-json-guide.md`: Simple user-facing guide for editing `sequence.json`.
- `piano_sequencer/piano_sequencer/parser.py`: Loads and validates JSON config.
- `piano_sequencer/piano_sequencer/notes.py`: Converts notes like `C4`, `F#4`, and `Bb4` into frequencies.
- `piano_sequencer/piano_sequencer/synth.py`: Generates note waveforms, ADSR envelope, and basic reverb.
- `piano_sequencer/piano_sequencer/compiler.py`: Renders each note and concatenates the final audio array.
- `piano_sequencer/piano_sequencer/export.py`: Writes WAV files.
- `piano_sequencer/piano_sequencer/main.py`: CLI entry point.

## Commands

Run commands from:

```sh
cd piano_sequencer
```

Install dependencies:

```sh
uv sync
```

Render the sample song:

```sh
uv run piano-sequencer --config sequence.json --out output.wav
```

Run tests:

```sh
uv run python -m unittest discover -s tests
```

Makefile shortcuts:

```sh
make install
make run
make test
make clean
```

On Windows, `make` may not be installed. The direct `uv` commands above are the reliable path.

## sequence.json Format

Basic shape:

```json
{
  "tempo": 100,
  "track": [
    {"note": "C4", "duration": 1.0, "effect": "none"},
    {"note": "G4", "duration": 2.0, "effect": "reverb"}
  ]
}
```

Fields:

- `tempo`: Positive integer, beats per minute.
- `track`: Non-empty list of note events.
- `note`: Scientific pitch notation such as `C4`, `A4`, `F#4`, or `Bb4`.
- `duration`: Positive number measured in beats.
- `effect`: Either `none` or `reverb`.

## Implementation Notes

- The project uses `uv` and is packaged with `[tool.uv] package = true` so the `piano-sequencer` console script works.
- Python requirement is currently `>=3.11`.
- Dependencies are `numpy` and `scipy`.
- Generated WAV files are ignored by `.gitignore`.
- Audio is monophonic: notes play one after another, not as chords.
- The synth uses a simple harmonic blend, not a sampled piano.
- Reverb is currently a short delayed copy mixed into the note.
- Tests use Python `unittest`.

## Good Next Steps

- Add rest support, for example `{"note": "REST", "duration": 1.0}`.
- Add chord support by allowing `note` to be a list of notes.
- Add more effects such as delay, tremolo, or low-pass filtering.
- Add stricter schema documentation or JSON Schema validation.
- Improve the piano tone with richer harmonics or velocity support.
