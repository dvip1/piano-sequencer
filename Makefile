.PHONY: install run clean test

install:
	uv sync

run:
	uv run piano-sequencer --config sequence.json --out output.wav

clean:
	uv run python -c "from pathlib import Path; [p.unlink() for p in Path('.').glob('*.wav')]; [p.unlink() for p in Path('.').rglob('*.pyc')]; [d.rmdir() for d in sorted(Path('.').rglob('__pycache__'), reverse=True)]"

test:
	uv run python -m unittest discover -s tests
