from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NoteEvent:
    note: str
    duration: float
    effect: str = "none"


@dataclass(frozen=True)
class Sequence:
    tempo: int
    track: list[NoteEvent]
