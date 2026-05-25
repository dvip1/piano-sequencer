from __future__ import annotations

import numpy as np

from piano_sequencer.models import Sequence
from piano_sequencer.synth import SAMPLE_RATE, apply_reverb, synthesize_note


def compile_sequence(sequence: Sequence, sample_rate: int = SAMPLE_RATE) -> np.ndarray:
    rendered_notes: list[np.ndarray] = []

    for event in sequence.track:
        audio = synthesize_note(event.note, event.duration, sequence.tempo, sample_rate)
        if event.effect == "reverb":
            audio = apply_reverb(audio, sample_rate)
        rendered_notes.append(audio)

    if not rendered_notes:
        return np.array([], dtype=np.float64)

    master = np.concatenate(rendered_notes)
    peak = np.max(np.abs(master))
    if peak > 0:
        master = master / peak * 0.9
    return master.astype(np.float32)
