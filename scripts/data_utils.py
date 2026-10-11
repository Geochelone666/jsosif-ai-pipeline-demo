"""Shared strict JSON output and finite-number handling for added sources."""
import json
import math
import os
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # repo root (this file lives in scripts/)
DATA = ROOT / 'data'
REPORTS = ROOT / 'reports'
SCRIPTS = ROOT / 'scripts'

def number(value):
    if isinstance(value, bool):
        return None
    try:
        result = float(value)
        return result if math.isfinite(result) else None
    except (TypeError, ValueError):
        return None

def save(name, data):
    path = DATA / name
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    with path.open(encoding='utf-8') as stream:
        json.load(stream)
    print(f'{name}: JSON OK, {len(data)} top-level fields', flush=True)

from universe import SUPPORTED

def ticker_arg():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--ticker', type=lambda value: value.strip().upper(), choices=SUPPORTED, default=SUPPORTED[0])
    return parser.parse_args().ticker

def ticker_file(ticker, name):
    return f'{ticker.lower()}-{name}'


def as_of_date():
    """Return the snapshot date, rejecting malformed or future input."""
    today = date.today()
    value = os.environ.get('REPORT_AS_OF', today.isoformat())
    error = (f"Invalid REPORT_AS_OF: expected a real calendar date in YYYY-MM-DD "
             f"format, no later than today ({today.isoformat()}); got {value!r}.")
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
        print(error, file=sys.stderr)
        raise SystemExit(2)
    try:
        result = date.fromisoformat(value)
    except ValueError:
        print(error, file=sys.stderr)
        raise SystemExit(2) from None
    if result > today:
        print(error + " Snapshot date cannot be in the future.", file=sys.stderr)
        raise SystemExit(2)
    return result
