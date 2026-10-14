"""Append-only email send audit trail; override storage with SEND_LEDGER_PATH."""
import json
import os
from pathlib import Path


DEFAULT_PATH = Path(__file__).resolve().parents[1] / 'data' / 'send_ledger.jsonl'


def _path():
    return Path(os.environ.get('SEND_LEDGER_PATH', DEFAULT_PATH))


def record(entry: dict) -> None:
    """Append one send attempt without changing earlier records."""
    line = json.dumps(entry, ensure_ascii=False) + '\n'
    path = _path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8') as stream:
        stream.write(line)


def query() -> list[dict]:
    """Return send attempts in append order."""
    path = _path()
    if not path.exists():
        return []
    with path.open(encoding='utf-8') as stream:
        return [json.loads(line) for line in stream]
