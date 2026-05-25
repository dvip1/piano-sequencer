from __future__ import annotations

import math
import re


NOTE_OFFSETS = {
    "C": -9,
    "C#": -8,
    "DB": -8,
    "D": -7,
    "D#": -6,
    "EB": -6,
    "E": -5,
    "F": -4,
    "F#": -3,
    "GB": -3,
    "G": -2,
    "G#": -1,
    "AB": -1,
    "A": 0,
    "A#": 1,
    "BB": 1,
    "B": 2,
}

NOTE_PATTERN = re.compile(r"^([A-Ga-g])([#bB]?)(-?\d+)$")


def note_to_frequency(note: str) -> float:
    """Convert scientific pitch notation, such as C4 or A4, to Hz."""
    match = NOTE_PATTERN.match(note.strip())
    if not match:
        raise ValueError(f"Invalid note {note!r}; expected notation like C4, F#3, or Bb5.")

    letter, accidental, octave_text = match.groups()
    pitch_name = f"{letter.upper()}{accidental.upper()}"
    octave = int(octave_text)

    if pitch_name not in NOTE_OFFSETS:
        raise ValueError(f"Invalid pitch name {note!r}.")

    semitones_from_a4 = NOTE_OFFSETS[pitch_name] + (octave - 4) * 12
    return 440.0 * math.pow(2.0, semitones_from_a4 / 12.0)


def is_valid_note(note: str) -> bool:
    try:
        note_to_frequency(note)
    except ValueError:
        return False
    return True
