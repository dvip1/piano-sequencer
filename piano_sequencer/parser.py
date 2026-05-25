from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from piano_sequencer.models import NoteEvent, Sequence
from piano_sequencer.notes import is_valid_note


SUPPORTED_EFFECTS = {"none", "reverb"}


def load_sequence(path: str | Path) -> Sequence:
    config_path = Path(path)
    try:
        raw = json.loads(config_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Config file does not exist: {config_path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {config_path}: {exc.msg}") from exc

    return parse_sequence(raw)


def parse_sequence(raw: Any) -> Sequence:
    if not isinstance(raw, dict):
        raise ValueError("Sequence config must be a JSON object.")

    tempo = raw.get("tempo", 120)
    if not isinstance(tempo, int) or tempo <= 0:
        raise ValueError("tempo must be a positive integer.")

    track = raw.get("track")
    if not isinstance(track, list) or not track:
        raise ValueError("track must be a non-empty array of note events.")

    events = [_parse_event(item, index) for index, item in enumerate(track)]
    return Sequence(tempo=tempo, track=events)


def _parse_event(raw: Any, index: int) -> NoteEvent:
    if not isinstance(raw, dict):
        raise ValueError(f"track[{index}] must be an object.")

    note = raw.get("note")
    if not isinstance(note, str) or not is_valid_note(note):
        raise ValueError(f"track[{index}].note must be valid pitch notation, such as C4.")

    duration = raw.get("duration")
    if not isinstance(duration, int | float) or isinstance(duration, bool) or duration <= 0:
        raise ValueError(f"track[{index}].duration must be a positive number of beats.")

    effect = raw.get("effect", "none")
    if not isinstance(effect, str):
        raise ValueError(f"track[{index}].effect must be a string.")

    normalized_effect = effect.lower()
    if normalized_effect not in SUPPORTED_EFFECTS:
        supported = ", ".join(sorted(SUPPORTED_EFFECTS))
        raise ValueError(f"track[{index}].effect must be one of: {supported}.")

    return NoteEvent(note=note.strip(), duration=float(duration), effect=normalized_effect)
