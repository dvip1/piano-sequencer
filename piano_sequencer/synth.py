from __future__ import annotations

import numpy as np

from piano_sequencer.notes import note_to_frequency


SAMPLE_RATE = 44_100


def beats_to_seconds(beats: float, tempo: int) -> float:
    return beats * 60.0 / tempo


def synthesize_note(
    note: str,
    beats: float,
    tempo: int,
    sample_rate: int = SAMPLE_RATE,
) -> np.ndarray:
    seconds = beats_to_seconds(beats, tempo)
    sample_count = max(1, int(round(seconds * sample_rate)))
    t = np.linspace(0.0, seconds, sample_count, endpoint=False)
    frequency = note_to_frequency(note)

    fundamental = np.sin(2.0 * np.pi * frequency * t)
    second_harmonic = 0.35 * np.sin(2.0 * np.pi * frequency * 2.0 * t)
    third_harmonic = 0.15 * np.sin(2.0 * np.pi * frequency * 3.0 * t)
    waveform = fundamental + second_harmonic + third_harmonic

    return waveform * adsr_envelope(sample_count, sample_rate)


def adsr_envelope(
    sample_count: int,
    sample_rate: int = SAMPLE_RATE,
    attack: float = 0.01,
    decay: float = 0.08,
    sustain_level: float = 0.55,
    release: float = 0.12,
) -> np.ndarray:
    attack_samples = min(int(attack * sample_rate), sample_count)
    decay_samples = min(int(decay * sample_rate), max(0, sample_count - attack_samples))
    release_samples = min(int(release * sample_rate), max(0, sample_count - attack_samples - decay_samples))
    sustain_samples = max(0, sample_count - attack_samples - decay_samples - release_samples)

    parts: list[np.ndarray] = []
    if attack_samples:
        parts.append(np.linspace(0.0, 1.0, attack_samples, endpoint=False))
    if decay_samples:
        parts.append(np.linspace(1.0, sustain_level, decay_samples, endpoint=False))
    if sustain_samples:
        parts.append(np.full(sustain_samples, sustain_level))
    if release_samples:
        start = sustain_level if sustain_samples else 1.0
        parts.append(np.linspace(start, 0.0, release_samples, endpoint=True))

    if not parts:
        return np.ones(sample_count)

    envelope = np.concatenate(parts)
    if envelope.size < sample_count:
        envelope = np.pad(envelope, (0, sample_count - envelope.size))
    return envelope[:sample_count]


def apply_reverb(audio: np.ndarray, sample_rate: int = SAMPLE_RATE) -> np.ndarray:
    delay_samples = int(0.12 * sample_rate)
    decay = 0.35
    wet = np.zeros(audio.size + delay_samples, dtype=np.float64)
    wet[: audio.size] += audio
    wet[delay_samples:] += audio * decay
    return wet
