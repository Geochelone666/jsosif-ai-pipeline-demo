"""Production daily collection retains history and proceeds independently of AI quota."""
from datetime import datetime, timezone
from pathlib import Path
import shutil
import subprocess

import pytest

import refresh_reports as refresh
from check_release import check
from daily_schedule import decision
from report_store import read_json, write_json, digest


NOW = datetime(2026, 10, 18, 23, tzinfo=timezone.utc)


@pytest.mark.parametrize('instant,run,day', [
    ('2026-10-19T23:00:00+00:00', True, '2026-10-19'),
    ('2026-10-20T00:00:00+00:00', False, '2026-10-19'),
    ('2026-12-02T23:00:00+00:00', False, '2026-12-02'),
    ('2026-12-03T00:00:00+00:00', True, '2026-12-02'),
    ('2026-11-02T00:00:00+00:00', True, '2026-11-01'),
    ('2026-03-08T23:00:00+00:00', True, '2026-03-08'),
])
def test_schedule_runs_once_at_local_19_even_across_dst(instant, run, day):
    assert decision('schedule', datetime.fromisoformat(instant)) == {'run': run, 'business_date': day}


def test_delayed_scheduled_worker_keeps_the_intended_business_date():
    assert decision('schedule', datetime(2026, 10, 20, 2, tzinfo=timezone.utc), '0 23 * * *') == {
        'run': True, 'business_date': '2026-10-19'}
    assert decision('schedule', datetime(2026, 12, 3, 2, tzinfo=timezone.utc), '0 0 * * *') == {
        'run': True, 'business_date': '2026-12-02'}
    assert not decision('schedule', datetime(2026, 10, 20, 2, tzinfo=timezone.utc), '0 0 * * *')['run']


@pytest.fixture
def pipeline(tmp_path, monkeypatch):
    original = Path(refresh.__file__).resolve().parents[1]
    source = tmp_path / 'source'
    source.mkdir()
    shutil.copytree(original / 'scripts', source / 'scripts', ignore=shutil.ignore_patterns('__pycache__'))
    data = source / 'data'; data.mkdir()
    reports = source / 'reports'; reports.mkdir()
    root = tmp_path / 'store'
    monkeypatch.setattr(refresh, 'ROOT', source)
    monkeypatch.setattr(refresh, 'DATA', data)
    monkeypatch.setattr(refresh, 'REPORTS', reports)
    monkeypatch.setattr(refresh, 'SUPPORTED', ['CSCO', 'JPM'])
    for key in ('GEMINI_API_KEY', 'GOOGLE_API_KEY', 'GEMINI_CLI', 'GEMINI_RPD', 'GEMINI_RPM',
                'GROQ_API_KEY', 'Grop_ai_API', 'AI_PROVIDER'):
        monkeypatch.delenv(key, raising=False)
    monkeypatch.setenv('SEC_USER_AGENT', 'Synthetic test organization contact@example.com')
    real_run = subprocess.run
    calls = []
    failure = {'ticker': None, 'timeout': False}

    def run(command, **kwargs):
        stage = Path(command[1]).stem
        ticker = command[-1] if '--ticker' in command else None
        env = kwargs['env']; day = env['REPORT_AS_OF']
        calls.append((ticker, stage, env.get('JSOSIF_AI_ENABLED')))
        assert kwargs['timeout'] > 0
        if ticker == failure['ticker'] and stage == 'quant':
            if failure['timeout']:
                raise subprocess.TimeoutExpired(command, kwargs['timeout'])
            raise subprocess.CalledProcessError(1, command)
        if stage in ('regenerate_report', 'report_pdf'):
            return real_run(command, **dict(kwargs, capture_output=True, text=True))
        if stage == 'fred':
            write_json(data / 'fred.json', {'available': False})
            return
        if stage == 'quant':
            write_json(data / f'{ticker.lower()}-info.json', {'currency': 'USD'})
            payload = {'ticker': ticker, 'as_of': day, 'metrics': {'Close': 100},
                       'fetched_at': NOW.isoformat(), 'errors': []}
        elif stage == 'ai_extract':
            payload = dict(ticker=ticker, as_of=day, model='synthetic-test-model',
                           tailwinds=[], headwinds=[], catalysts=[], risks=[],
                           extraction_stats={'unique_headlines': 1, 'rule': 1, 'ai': 0, 'unknown': 0})
            if env['JSOSIF_AI_ENABLED'] == '0':
                payload['error'] = env['JSOSIF_AI_UNAVAILABLE_REASON']
            write_json(data / f'{ticker.lower()}-rss-items.json', [])
        elif stage == 'comparables':
            payload = {'as_of': day, 'peers': []}
        elif stage == 'earnings':
            payload = {'last_earnings': None, 'next_earnings': None}
        elif stage == 'edgar':
            payload = {'latest_filing': None, 'revenue': None, 'net_income': None}
        else:
            pytest.fail('Unexpected pipeline stage')
        name = 'ai-intel' if stage == 'ai_extract' else stage
        write_json(data / f'{ticker.lower()}-{name}.json', payload)

    monkeypatch.setattr(refresh.subprocess, 'run', run)
    return root, calls, failure


def test_missing_ai_credentials_still_refreshes_every_holding(pipeline):
    root, calls, _ = pipeline
    result = refresh.refresh(root, now=NOW)
    assert result == {'status': 'degraded', 'publish': True, 'failed': False}
    index = read_json(root / 'index.json')
    assert {r['ticker'] for r in index['reports']} == {'CSCO', 'JPM'}
    assert all(r['as_of'] == '2026-10-18' for r in index['reports'])
    assert all(flag == '0' for _, stage, flag in calls if stage == 'ai_extract')
    assert check(root)['ready']
    assert not check(root, require_ready=True)['ready']


def test_exhausted_ai_quota_does_not_skip_market_updates(pipeline, monkeypatch):
    root, calls, _ = pipeline
    monkeypatch.setenv('GEMINI_API_KEY', 'synthetic')
    monkeypatch.setenv('GEMINI_MODEL', 'test-model')
    monkeypatch.setenv('GEMINI_RPD', '10')
    monkeypatch.setenv('GEMINI_RPM', '10')
    write_json(root / 'state/api-usage.json', {'test-model:' + refresh.quota_day(NOW): 8})
    refresh.refresh(root, now=NOW)
    assert sum(stage == 'quant' for _, stage, _ in calls) == 2
    assert read_json(root / 'index.json')['refresh_plan']['remaining_requests'] == 0


def test_daily_idempotency_uses_toronto_date_across_utc_midnight(pipeline):
    root, calls, _ = pipeline
    refresh.refresh(root, now=NOW)
    count = len(calls)
    result = refresh.refresh(root, now=datetime(2026, 10, 19, 0, tzinfo=timezone.utc))
    assert result['status'] == 'skipped' and not result['publish']
    assert len(calls) == count
    assert len(read_json(root / 'index.json')['reports']) == 2


@pytest.mark.parametrize('timeout', [False, True])
def test_partial_failure_keeps_history_and_supports_explicit_recovery(pipeline, timeout):
    root, _, failure = pipeline
    failure.update(ticker='CSCO', timeout=timeout)
    result = refresh.refresh(root, now=NOW)
    assert result['failed'] and result['status'] == 'partial'
    index = read_json(root / 'index.json')
    first = index['reports'][0]
    original = digest(root / first['pdf'])
    assert index['last_attempt']['failed_tickers'] == ['CSCO']
    assert not check(root)['ready']
    failure['ticker'] = None
    refresh.refresh(root, now=NOW, force=True)
    assert len(read_json(root / 'index.json')['reports']) == 3
    assert digest(root / first['pdf']) == original
    assert check(root)['ready']


def test_full_source_evidence_passes_strict_release_check(pipeline, monkeypatch):
    root, _, _ = pipeline
    monkeypatch.setenv('GEMINI_API_KEY', 'synthetic')
    monkeypatch.setenv('GEMINI_RPD', '10')
    monkeypatch.setenv('GEMINI_RPM', '10')
    assert refresh.refresh(root, now=NOW)['status'] == 'complete'
    assert check(root, require_ready=True)['ready']


def test_release_check_cannot_pass_with_history_only(tmp_path):
    assert not check(tmp_path)['ready']


def test_failed_archive_checkpoint_prevents_new_provider_work(pipeline, monkeypatch):
    root, calls, _ = pipeline
    def fail(*args, **kwargs):
        raise subprocess.CalledProcessError(1, ['git', 'push'])
    monkeypatch.setattr(refresh, 'persist', fail)
    with pytest.raises(subprocess.CalledProcessError):
        refresh.refresh(root, now=NOW, persist_git=True)
    assert calls == []


def test_ai_reservation_is_persisted_before_the_request(tmp_path, monkeypatch):
    import gemini_provider as provider
    import report_store
    monkeypatch.setenv('GEMINI_API_KEY', 'synthetic')
    monkeypatch.setenv('GEMINI_RPD', '10')
    monkeypatch.setenv('GEMINI_RPM', '10')
    monkeypatch.setenv('JSOSIF_API_USAGE_PATH', str(tmp_path / 'state/api-usage.json'))
    monkeypatch.setenv('JSOSIF_PERSIST_API_USAGE', '1')
    def rejected(*args, **kwargs):
        raise subprocess.CalledProcessError(1, ['git', 'push'])
    monkeypatch.setattr(report_store, 'persist', rejected)
    with pytest.raises(subprocess.CalledProcessError):
        provider.generate_json('Synthetic test', opener=lambda *a, **kw: pytest.fail('Must persist before HTTP'))


def test_missing_sec_identity_never_uses_a_placeholder_contact(monkeypatch):
    import edgar
    monkeypatch.delenv('SEC_USER_AGENT', raising=False)
    monkeypatch.setattr(edgar, 'urlopen', lambda *args, **kw: pytest.fail('No placeholder SEC request'))
    with pytest.raises(ValueError, match='SEC_USER_AGENT'):
        edgar.fetch('https://www.sec.gov/files/company_tickers.json')
