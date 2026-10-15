from datetime import datetime
from pathlib import Path
import sys
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import scheduler


@pytest.mark.parametrize('instant,expected,seconds', [
    ('2026-10-15T08:00:00-04:00', '2026-10-15T09:00:00-04:00', 3600),
    ('2026-10-15T09:00:00-04:00', '2026-10-16T09:00:00-04:00', 86400),
    ('2026-12-31T10:00:00-05:00', '2027-01-01T09:00:00-05:00', 82800),
    ('2026-03-07T10:00:00-05:00', '2026-03-08T09:00:00-04:00', 79200),
    ('2026-10-31T10:00:00-04:00', '2026-11-01T09:00:00-05:00', 86400),
    ('2026-10-15T12:59:59+00:00', '2026-10-15T09:00:00-04:00', 1),
])
def test_schedule(instant, expected, seconds):
    now = datetime.fromisoformat(instant)
    assert scheduler.next_run(now).isoformat() == expected
    assert scheduler.seconds_until_next_run(now) == seconds


def test_naive_time_rejected():
    with pytest.raises(ValueError):
        scheduler.next_run(datetime(2026, 1, 1))


def test_lock_prevents_overlap_and_releases(tmp_path, monkeypatch):
    lock = tmp_path / 'send.lock'
    calls = []
    def child(command, **kwargs):
        calls.append(command)
        assert scheduler.run_once(lock) is False
        return SimpleNamespace(returncode=0)
    monkeypatch.setattr(scheduler.subprocess, 'run', child)
    assert scheduler.run_once(lock)
    assert scheduler.run_once(lock)
    assert len(calls) == 2
    assert calls[0][-1] == '--send'


def test_failure_releases_lock(tmp_path, monkeypatch):
    lock = tmp_path / 'send.lock'
    def fail(*args, **kwargs):
        raise OSError('sensitive detail')
    monkeypatch.setattr(scheduler.subprocess, 'run', fail)
    assert not scheduler.run_once(lock)
    monkeypatch.setattr(scheduler.subprocess, 'run', lambda *a, **k: SimpleNamespace(returncode=0))
    assert scheduler.run_once(lock)


def test_dry_run_does_not_send(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(scheduler, 'run_once', lambda *a: pytest.fail('unexpected send'))
    assert scheduler.main(['--dry-run', '--log-file', str(tmp_path / 'unused.log')]) == 0
    assert 'Next run:' in capsys.readouterr().out
    assert not list(tmp_path.iterdir())


def test_daemon_continues_after_failure(tmp_path, monkeypatch):
    attempts = []
    sleeps = []
    def sleep(seconds):
        sleeps.append(seconds)
        if len(sleeps) == 3:
            raise KeyboardInterrupt
    def run(lock):
        attempts.append(lock)
        return False
    monkeypatch.setattr(scheduler.time, 'sleep', sleep)
    monkeypatch.setattr(scheduler, 'run_once', run)
    with pytest.raises(KeyboardInterrupt):
        scheduler.daemon(tmp_path / 'lock')
    assert len(attempts) == 2
    assert all(seconds > 0 for seconds in sleeps)
