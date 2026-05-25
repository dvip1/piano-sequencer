from __future__ import annotations

from pathlib import Path

import numpy as np
from scipy.io import wavfile

from piano_sequencer.synth import SAMPLE_RATE


def export_wav(audio: np.ndarray, output_path: str | Path, sample_rate: int = SAMPLE_RATE) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    wavfile.write(path, sample_rate, audio)
    return path
