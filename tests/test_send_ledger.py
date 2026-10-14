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


@pytest.mark.parametrize('filters, expected', [
    ({'since': '2026-10-02'}, [1, 2]),
    ({'until': '2026-10-02'}, [0, 1]),
    ({'ticker': 'CNQ.TO'}, [0, 1]),
    ({'dry_run': False}, [0, 2]),
    ({'dry_run': True}, [1]),
    ({'since': '2026-10-02', 'until': '2026-10-02', 'ticker': 'CNQ.TO', 'dry_run': True}, [1]),
    ({'since': '2026-10-02T23:59:59Z', 'until': '2026-10-02T23:59:59+00:00'}, [1]),
    ({'ticker': 'CNQ'}, []),
])
def test_filters(ledger, filters, expected):
    rows = [entry(), entry('CNQ.TO-2026-10-02', '2026-10-02T23:59:59Z', True),
            entry('ACN-2026-10-03', '2026-10-03T00:00:00Z')]
    for row in rows:
        ledger.record(row)
    assert ledger.query(**filters) == [rows[i] for i in expected]


def test_malformed_lines(ledger, caplog):
    ledger.record(entry())
    with ledger._path().open('a') as stream:
        stream.write('broken json\n[]\n{"timestamp": "bad"}\n')
    ledger.record(entry(dry_run=True))
    assert ledger.query() == [entry(), entry(dry_run=True)]
    assert len(caplog.records) == 3
    assert all('line' in r.message for r in caplog.records)


def test_defaults_and_failure(ledger):
    row = entry()
    del row['timestamp']
    del row['error']
    ledger.record(row)
    saved = ledger.query()[0]
    from datetime import datetime, timezone
    assert abs((datetime.now(timezone.utc) - datetime.fromisoformat(saved['timestamp'])).total_seconds()) < 5
    assert saved['error'] is None
    failed = dict(entry(), status='failed', error='SMTP unavailable')
    ledger.record(failed)
    assert ledger.query()[-1] == failed


def test_cli(ledger):
    import subprocess
    ledger.record(entry(dry_run=True))
    ledger.record(entry('ACN-2026-10-01'))
    result = subprocess.run([sys.executable, ledger.__file__, '--list', '--since',
                             '2026-10-01', '--ticker', 'CNQ.TO', '--dry-run'],
                            capture_output=True, text=True, check=True)
    assert 'CNQ.TO-2026-10-01' in result.stdout
    assert 'dry-run' in result.stdout
    assert 'analyst@example.com' in result.stdout
    assert 'ACN' not in result.stdout


def test_normalizes_offset_to_utc(ledger):
    ledger.record(entry(timestamp='2026-10-02T01:00:00+02:00'))
    assert ledger.query(until='2026-10-01')[0]['timestamp'] == '2026-10-01T23:00:00+00:00'


@pytest.mark.parametrize('changes', [
    {'timestamp': '2026-10-01T12:00:00'}, {'recipients': 'a@example.com'},
    {'dry_run': 'false'}, {'status': 'unknown'}, {'snapshot_id': ''},
])
def test_invalid_record_does_not_append(ledger, changes):
    ledger.record(entry())
    before = ledger._path().read_bytes()
    with pytest.raises(ValueError):
        ledger.record(dict(entry(), **changes))
    assert ledger._path().read_bytes() == before
