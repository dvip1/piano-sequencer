import unittest

import numpy as np

from piano_sequencer.compiler import compile_sequence
from piano_sequencer.models import NoteEvent, Sequence
from piano_sequencer.notes import note_to_frequency
from piano_sequencer.parser import parse_sequence


class SequencerTests(unittest.TestCase):
    def test_note_to_frequency_uses_a4_reference(self):
        self.assertAlmostEqual(note_to_frequency("A4"), 440.0)

    def test_parse_sequence_validates_track(self):
        sequence = parse_sequence(
            {
                "tempo": 120,
                "track": [{"note": "C4", "duration": 0.5, "effect": "none"}],
            }
        )

        self.assertEqual(sequence.tempo, 120)
        self.assertEqual(sequence.track[0].note, "C4")

    def test_compile_sequence_returns_audio(self):
        sequence = Sequence(tempo=120, track=[NoteEvent(note="C4", duration=0.25)])
        audio = compile_sequence(sequence)

        self.assertIsInstance(audio, np.ndarray)
        self.assertGreater(audio.size, 0)
        self.assertLessEqual(float(np.max(np.abs(audio))), 1.0)


if __name__ == "__main__":
    unittest.main()
