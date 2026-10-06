"""Shared strict JSON output and finite-number handling for added sources."""
import json
import math
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

SUPPORTED = ('NVDA', 'MSFT', 'AAPL', 'GOOGL', 'AMZN', 'TSLA')

def ticker_arg():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--ticker', type=str.upper, choices=SUPPORTED, default='NVDA')
    return parser.parse_args().ticker

def ticker_file(ticker, name):
    return f'{ticker.lower()}-{name}'
