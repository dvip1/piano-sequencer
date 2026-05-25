# Nursery Rhymes

This folder contains simple JSON melodies that work with the piano sequencer.

Render any song from the `piano_sequencer/` directory:

```sh
uv run piano-sequencer --config nursery_rhymes/twinkle_twinkle_little_star.json --out twinkle.wav
```

Each file uses the same structure as `sequence.json`:

```json
{
  "tempo": 100,
  "track": [
    {"note": "C4", "duration": 1.0, "effect": "none"}
  ]
}
```

