# sequence.json Guide

`sequence.json` is the song file. It tells the sequencer which notes to play, how fast to play them, and whether to add a simple effect.

## Basic Shape

```json
{
  "tempo": 100,
  "track": [
    {"note": "C4", "duration": 1.0, "effect": "none"},
    {"note": "G4", "duration": 1.0, "effect": "reverb"}
  ]
}
```

## What You Can Change

### tempo

`tempo` controls the speed of the song in beats per minute.

Lower numbers are slower:

```json
"tempo": 80
```

Higher numbers are faster:

```json
"tempo": 140
```

### track

`track` is the list of notes. The sequencer plays them from top to bottom.

Each item has three fields:

```json
{"note": "C4", "duration": 1.0, "effect": "none"}
```

### note

`note` is the pitch to play.

Use standard note names like:

```text
C4, D4, E4, F4, G4, A4, B4, C5
```

You can also use sharps and flats:

```text
F#4, Bb4
```

Middle C is `C4`. Higher octave numbers sound higher. Lower octave numbers sound lower.

### duration

`duration` is how long the note lasts, measured in beats.

Common values:

```text
0.5 = short note
1.0 = normal note
2.0 = long note
4.0 = very long note
```

At `"tempo": 120`, a `duration` of `1.0` lasts half a second.

### effect

`effect` controls simple audio processing.

Supported values:

```text
none
reverb
```

Use `"none"` for a plain note:

```json
{"note": "C4", "duration": 1.0, "effect": "none"}
```

Use `"reverb"` for a little echo:

```json
{"note": "C4", "duration": 1.0, "effect": "reverb"}
```

## Tiny Example

```json
{
  "tempo": 100,
  "track": [
    {"note": "C4", "duration": 1.0, "effect": "none"},
    {"note": "D4", "duration": 1.0, "effect": "none"},
    {"note": "E4", "duration": 2.0, "effect": "reverb"}
  ]
}
```

Run it with:

```sh
uv run piano-sequencer --config sequence.json --out output.wav
```
