#!/usr/bin/env python3
"""Run extraction, report packaging, and an offline email preview in order."""
import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)
    stage = '1 (Quant + AI extract)'
    try:
        print(f'STAGE {stage} START', flush=True)
        subprocess.run(['python3', 'scripts/run_phase1.py'], check=True, cwd=ROOT)
        print(f'STAGE {stage} DONE', flush=True)
    except Exception as exc:
        print(f'STAGE {stage} FAILED: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
