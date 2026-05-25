from __future__ import annotations

import argparse
import sys
from pathlib import Path

from piano_sequencer.compiler import compile_sequence
from piano_sequencer.export import export_wav
from piano_sequencer.parser import load_sequence


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Render a JSON note sequence to a WAV file.")
    parser.add_argument(
        "--config",
        default="sequence.json",
        help="Path to a JSON sequence file. Defaults to sequence.json.",
    )
    parser.add_argument(
        "--out",
        default="output.wav",
        help="Destination WAV path. Defaults to output.wav.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        sequence = load_sequence(args.config)
        audio = compile_sequence(sequence)
        output_path = export_wav(audio, args.out)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote {Path(output_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
