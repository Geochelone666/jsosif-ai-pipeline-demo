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
    timings = index['last_attempt']['stage_seconds']
    assert set(timings['CSCO']) == {'quant'}
    assert 'report_pdf' in timings['JPM']
    assert all(seconds >= 0 for stages in timings.values() for seconds in stages.values())
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


def test_release_coverage_requires_the_requested_business_date(pipeline, monkeypatch):
    root, _, _ = pipeline
    monkeypatch.setenv('GEMINI_API_KEY', 'synthetic')
    monkeypatch.setenv('GEMINI_RPD', '10')
    monkeypatch.setenv('GEMINI_RPM', '10')
    refresh.refresh(root, now=NOW)
    assert check(root, business_date='2026-10-18', require_ready=True)['ready']
    assert not check(root, business_date='2026-10-19', require_ready=True)['ready']


def test_full_portfolio_excel_roster_two_week_launch_rehearsal(pipeline, monkeypatch, tmp_path):
    """External research sources and mail transport are synthetic; rendering is real."""
    from datetime import timedelta
    from email import policy
    from email.parser import BytesParser
    from openpyxl import Workbook
    from subscriptions import CSV_FIELDS, import_members_excel, write_private_config
    from universe import SUPPORTED
    from deliver_weekly import deliver
    from build_site import build

    root, _, _ = pipeline
    monkeypatch.setattr(refresh, 'SUPPORTED', list(SUPPORTED))
    # The rehearsal's clock must not depend on the actual wall clock.
    start = NOW - timedelta(days=14)
    clock = {'now': start}
    real_archive = refresh.archive
    def archive(root, ticker, stamp, run_id, generated_at):
        return real_archive(root, ticker, stamp, run_id, clock['now'].isoformat())
    monkeypatch.setattr(refresh, 'archive', archive)
    monkeypatch.setenv('GEMINI_API_KEY', 'synthetic-test-only')
    monkeypatch.setenv('GEMINI_RPD', '1000')
    monkeypatch.setenv('GEMINI_RPM', '1000')
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = 'Members'
    sheet.append(list(CSV_FIELDS))
    zones = ('America/Toronto', 'Europe/London', 'Asia/Shanghai')
    for i in range(30):
        choices = ';'.join(SUPPORTED[:5]) if i == 0 else SUPPORTED[i % len(SUPPORTED)]
        sheet.append([f'fixture-{i:03}', f'Synthetic Member {i}', f'member-{i}@example.com',
                      f'group-{i % 5}', choices, i != 29, zones[i % 3], 0, '09:00'])
    excel = tmp_path / 'members.local.xlsx'
    workbook.save(excel)
    config = import_members_excel({'groups': {}, 'members': []}, excel)
    private = tmp_path / 'subscriptions.local.json'
    write_private_config(private, config)
    assert refresh.refresh(root, config=private, now=start)['status'] == 'complete'
    assert check(root, business_date=start.date().isoformat(), require_ready=True)['current'] == len(
        {t for group in config['groups'].values() for t in group['tickers']})
    first_hashes = {entry['pdf']: digest(root / entry['pdf'])
                    for entry in read_json(root / 'index.json')['reports']}
    monday = start + timedelta(hours=15)
    previews = tmp_path / 'previews'
    result = deliver(config, root, now=monday, preview_all=True, preview_dir=previews)
    assert result['prepared'] == 29 and result['skipped'] == 1
    assert not (root / 'state/deliveries.json').exists()
    messages = [BytesParser(policy=policy.default).parsebytes(path.read_bytes())
                for path in previews.glob('*.eml')]
    first = next(message for message in messages if str(message['To']) == 'member-0@example.com')
    assert len(list(first.iter_attachments())) == 5
    assert 'Hi Synthetic Member 0,' in first.get_body(preferencelist=('plain',)).get_content()
    for message in messages:
        assert len(message['To'].addresses) == 1
        assert 'member-29@example.com' not in str(message['To'])
    sent = []
    assert deliver(config, root, now=monday, really_send=True, backend=sent.append)['sent'] == 29
    assert deliver(config, root, now=monday, really_send=True, backend=sent.append)['skipped'] == 30
    assert len(sent) == 29
    # Expired reports do not reserve next week's slots.
    next_monday = monday + timedelta(days=7)
    assert deliver(config, root, now=next_monday, really_send=True, backend=sent.append)['deferred'] == 29
    assert len(read_json(root / 'state/deliveries.json')) == 29
    clock['now'] = start + timedelta(days=7)
    assert refresh.refresh(root, config=private, now=clock['now'])['status'] == 'complete'
    assert len(read_json(root / 'index.json')['reports']) == 2 * len(first_hashes)
    assert all(digest(root / path) == value for path, value in first_hashes.items())
    attempted = []
    def uncertain(message):
        attempted.append(str(message['To']))
        if str(message['To']) == 'member-0@example.com':
            raise TimeoutError('Synthetic uncertain SMTP outcome')
    result = deliver(config, root, now=next_monday, really_send=True, backend=uncertain)
    assert result['sent'] == 28 and result['unknown'] == 1
    repeated = deliver(config, root, now=next_monday, really_send=True, backend=uncertain)
    assert repeated['skipped'] == 29 and repeated['unknown'] == 1
    assert len(attempted) == 29
    site = tmp_path / 'site'
    build(root, site)
    assert len(list(site.rglob('*.pdf'))) == 2 * len(first_hashes)
    assert not (site / 'state').exists()
    import internal_email_check
    monkeypatch.setenv('GMAIL_USER', 'synthetic-self@example.com')
    ledger_before = (root / 'state/deliveries.json').read_bytes()
    preview = internal_email_check.check(root, tmp_path / 'internal-preview', now=next_monday)
    assert preview['recipient_is_sender'] and len(preview['attachments']) == 5
    assert 'Hi JSOSIF Test,' in preview['body']
    assert 'synthetic-self@example.com' not in preview['body']
    assert (root / 'state/deliveries.json').read_bytes() == ledger_before
    for path in site.rglob('*'):
        if path.is_file():
            assert b'member-0@example.com' not in path.read_bytes()
            assert b'Synthetic Member' not in path.read_bytes()


def test_intraday_manual_acceptance_does_not_consume_the_evening_schedule(pipeline):
    from datetime import timedelta
    root, calls, _ = pipeline
    refresh.refresh(root, now=NOW - timedelta(hours=4))
    first = read_json(root / 'index.json')['reports']
    hashes = {entry['pdf']: digest(root / entry['pdf']) for entry in first}
    assert refresh.refresh(root, now=NOW, scheduled=True)['status'] == 'degraded'
    assert len(read_json(root / 'index.json')['reports']) == 4
    assert all(digest(root / file) == value for file, value in hashes.items())
    before = len(calls)
    assert refresh.refresh(root, now=NOW + timedelta(hours=1), scheduled=True)['status'] == 'skipped'
    assert len(calls) == before


def test_quiet_news_report_renders_real_pdf_without_claiming_ai_classification(pipeline, monkeypatch):
    root, _, _ = pipeline
    monkeypatch.setenv('GEMINI_API_KEY', 'synthetic')
    monkeypatch.setenv('GEMINI_RPD', '10')
    monkeypatch.setenv('GEMINI_RPM', '10')
    run = refresh.subprocess.run
    def quiet(command, **kwargs):
        result = run(command, **kwargs)
        if Path(command[1]).stem == 'ai_extract':
            target = refresh.DATA / (command[-1].lower() + '-ai-intel.json')
            data = read_json(target)
            data.update(fetch_status={'status': 'ok'}, extraction_stats={
                'unique_headlines': 0, 'rule': 0, 'ai': 0, 'unknown': 0})
            write_json(target, data)
        return result
    monkeypatch.setattr(refresh.subprocess, 'run', quiet)
    assert refresh.refresh(root, now=NOW)['status'] == 'complete'
    entry = read_json(root / 'index.json')['reports'][0]
    assert 'No recent headlines returned by RSS; no AI classification performed' in (root / entry['md']).read_text()
    assert (root / entry['pdf']).read_bytes().startswith(b'%PDF-')


def test_resume_only_collects_outstanding_reports_and_reuses_intact_ready_versions(pipeline, monkeypatch):
    root, calls, failure = pipeline
    monkeypatch.setenv('GEMINI_API_KEY', 'synthetic')
    monkeypatch.setenv('GEMINI_RPD', '100')
    monkeypatch.setenv('GEMINI_RPM', '100')
    failure['ticker'] = 'CSCO'
    refresh.refresh(root, now=NOW)
    original = read_json(root / 'index.json')['reports'][0]
    old_digest = digest(root / original['pdf'])
    calls.clear(); failure['ticker'] = None
    result = refresh.refresh(root, now=NOW, resume=True)
    assert result == {'status': 'complete', 'publish': True, 'failed': False}
    assert {ticker for ticker, stage, _ in calls if stage == 'quant'} == {'CSCO'}
    index = read_json(root / 'index.json')
    assert index['last_attempt']['reused_tickers'] == ['JPM']
    assert len(index['reports']) == 2
    assert digest(root / original['pdf']) == old_digest
    assert check(root, require_ready=True)['ready']
    calls.clear()
    refresh.refresh(root, now=NOW, resume=True)
    assert calls == []  # A fully recovered date performs no provider calls.


def test_resume_retries_degraded_reports(pipeline):
    root, calls, _ = pipeline
    refresh.refresh(root, now=NOW)  # Missing AI credentials makes both reports degraded.
    calls.clear()
    refresh.refresh(root, now=NOW, resume=True)
    assert {ticker for ticker, stage, _ in calls if stage == 'quant'} == {'CSCO', 'JPM'}
    assert read_json(root / 'index.json')['last_attempt']['reused_tickers'] == []


def test_resume_does_not_trust_a_modified_pdf(pipeline, monkeypatch):
    root, calls, _ = pipeline
    monkeypatch.setenv('GEMINI_API_KEY', 'synthetic')
    monkeypatch.setenv('GEMINI_RPD', '100'); monkeypatch.setenv('GEMINI_RPM', '100')
    refresh.refresh(root, now=NOW)
    entry = next(r for r in read_json(root / 'index.json')['reports'] if r['ticker'] == 'CSCO')
    (root / entry['pdf']).write_bytes(b'%PDF-corrupted')
    calls.clear()
    refresh.refresh(root, now=NOW, resume=True)
    assert {ticker for ticker, stage, _ in calls if stage == 'quant'} == {'CSCO'}
    assert read_json(root / 'index.json')['last_attempt']['reused_tickers'] == ['JPM']
    assert not check(root, require_ready=True)['ready']  # Corrupt history still requires restoration.


def test_time_budget_stops_provider_work_and_preserves_publishable_checkpoint(pipeline, monkeypatch):
    root, calls, _ = pipeline
    clock = {'seconds': 0.}
    monkeypatch.setattr(refresh, 'monotonic', lambda: clock['seconds'])
    original_run = refresh.subprocess.run
    def elapsed(command, **kwargs):
        result = original_run(command, **kwargs)
        if Path(command[1]).stem == 'quant':
            clock['seconds'] += 6
        return result
    monkeypatch.setattr(refresh.subprocess, 'run', elapsed)
    result = refresh.refresh(root, now=NOW, time_budget_seconds=5)
    assert result == {'status': 'interrupted', 'publish': True, 'failed': True}
    assert [ticker for ticker, stage, _ in calls if stage == 'quant'] == ['CSCO']
    attempt = read_json(root / 'index.json')['last_attempt']
    assert attempt['interruption_reason'] == 'time_budget_exhausted'
    assert attempt['pending_tickers'] == ['CSCO', 'JPM']
    assert 'current_ticker' not in attempt
    assert not check(root)['ready']


def test_resume_and_force_are_mutually_exclusive(pipeline):
    with pytest.raises(ValueError, match='Choose resume or force'):
        refresh.refresh(pipeline[0], now=NOW, resume=True, force=True)


@pytest.mark.parametrize('budget', [0, -1, float('nan'), float('inf'), True])
def test_invalid_collection_budget_rejected_before_provider_calls(pipeline, budget):
    root, calls, _ = pipeline
    with pytest.raises(ValueError, match='Time budget'):
        refresh.refresh(root, now=NOW, time_budget_seconds=budget)
    assert calls == []
