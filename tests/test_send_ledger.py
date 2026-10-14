"""Contracts for the append-only send audit trail."""
import importlib
import json
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))


@pytest.fixture
def ledger(tmp_path, monkeypatch):
    monkeypatch.setenv('SEND_LEDGER_PATH', str(tmp_path / 'data' / 'ledger.jsonl'))
    return importlib.import_module('send_ledger')


def entry(snapshot='CNQ.TO-2026-10-01', timestamp='2026-10-01T12:00:00Z', dry_run=False):
    return dict(snapshot_id=snapshot, recipients=['analyst@example.com'],
                timestamp=timestamp, dry_run=dry_run,
                status='dry-run' if dry_run else 'sent', error=None)


def test_append_and_query(ledger):
    assert ledger.query() == []
    first = entry()
    ledger.record(first)
    path = ledger._path()
    original = path.read_bytes()
    second = entry(dry_run=True)
    ledger.record(second)
    assert path.read_bytes().startswith(original)
    assert ledger.query() == [first, second]
    assert [json.loads(line) for line in path.read_text().splitlines()] == [first, second]
