"""Shared strict JSON output and finite-number handling for added sources."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def number(value):
    if isinstance(value, bool):
        return None
    try:
        result = float(value)
        return result if math.isfinite(result) else None
    except (TypeError, ValueError):
        return None

def save(name, data):
    path = ROOT / name
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    with path.open(encoding='utf-8') as stream:
        json.load(stream)
    print(f'{name}: JSON OK, {len(data)} top-level fields', flush=True)
