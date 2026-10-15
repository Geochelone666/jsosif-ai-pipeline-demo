"""Phase-one environment isolation; all credentials below are synthetic."""
import os
from pathlib import Path
import subprocess
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import run_phase1


CONFIG = dict(report_as_of='2026-01-01', rss_count=7, rss_max_attempts=2, rss_timeout=9)


@pytest.mark.parametrize('script', run_phase1.SCRIPT_ENV)
def test_environment_is_exact_allowlist(script, monkeypatch):
    parent = {key: 'synthetic' for key in run_phase1.RUNTIME_ENV}
    parent.update({key: 'synthetic' for key in (
        'GEMINI_CLI', 'GEMINI_API_KEY', 'GOOGLE_API_KEY', 'AWS_SECRET_ACCESS_KEY',
        'GITHUB_TOKEN', 'OPENAI_API_KEY', 'SMTP_PASSWORD', 'FRED_API_KEY',
        'HOME', 'USERPROFILE', 'PYTHONPATH', 'PYTHONSTARTUP', 'HTTP_PROXY',
        'JSOSIF_CONFIG', 'JSOSIF_APPROVED_SEND', 'UNRECOGNIZED_SECRET')})
    parent.update(REPORT_AS_OF='stale', JSOSIF_RSS_COUNT='stale')
    monkeypatch.setattr(os, 'environ', parent)
    expected = {key: parent[key] for key in run_phase1.RUNTIME_ENV}
    expected.update(REPORT_AS_OF='2026-01-01', JSOSIF_REPORT_AS_OF='2026-01-01')
    if script == 'ai_extract':
        expected.update({key: parent[key] for key in run_phase1.SCRIPT_ENV[script]})
        expected.update(JSOSIF_RSS_COUNT='7', JSOSIF_RSS_MAX_ATTEMPTS='2', JSOSIF_RSS_TIMEOUT='9')
    assert run_phase1.child_env(script, CONFIG) == expected
    assert parent['REPORT_AS_OF'] == 'stale'


def test_empty_parent_and_fresh_environments(monkeypatch):
    monkeypatch.setattr(os, 'environ', {})
    first = run_phase1.child_env('quant', CONFIG)
    first['UNRECOGNIZED_SECRET'] = 'synthetic'
    assert run_phase1.child_env('quant', CONFIG) == {
        'REPORT_AS_OF': '2026-01-01', 'JSOSIF_REPORT_AS_OF': '2026-01-01'}


def test_every_child_uses_its_own_environment(monkeypatch):
    monkeypatch.setattr(run_phase1, 'startup_config', lambda: CONFIG)
    monkeypatch.setattr(run_phase1, 'SUPPORTED', ['ACN', 'MSFT'])
    monkeypatch.setattr(os, 'environ', {'GEMINI_API_KEY': 'synthetic', 'PRIVATE_TOKEN': 'synthetic'})
    calls = []

    def run(command, **kwargs):
        script = Path(command[1]).stem
        assert command[0] == sys.executable
        assert kwargs == dict(check=True, cwd=run_phase1.ROOT,
                              env=run_phase1.child_env(script, CONFIG))
        calls.append((command[-1], script))
        # Simulate caller mutation: subsequent children must still be isolated.
        kwargs['env']['PRIVATE_TOKEN'] = 'synthetic'

    monkeypatch.setattr(run_phase1.subprocess, 'run', run)
    run_phase1.main()
    assert calls == [(ticker, script) for ticker in ['ACN', 'MSFT']
                     for script in run_phase1.SCRIPT_ENV]


def test_child_failure_stops_pipeline(monkeypatch):
    monkeypatch.setattr(run_phase1, 'startup_config', lambda: CONFIG)
    calls = []

    def fail(command, **kwargs):
        calls.append(command)
        raise subprocess.CalledProcessError(1, command)

    monkeypatch.setattr(run_phase1.subprocess, 'run', fail)
    with pytest.raises(subprocess.CalledProcessError):
        run_phase1.main()
    assert len(calls) == 1
