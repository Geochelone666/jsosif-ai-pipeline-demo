"""Behavioral regressions for date filtering, private subscriptions and durable delivery."""
from copy import deepcopy
from datetime import datetime, timezone
import io
import json
from pathlib import Path

import pytest

import ai_extract
import deliver_weekly as weekly
from build_site import build
from report_store import digest, write_json, read_json
from subscriptions import validate, tickers_for
from gemini_provider import generate_json, GeminiError
from refresh_reports import quota_plan
from snapshot_emit import emit_frozen_snapshot


NOW = datetime(2026, 10, 19, 14, tzinfo=timezone.utc)


@pytest.fixture
def config():
    return {'groups': {'tech': {'tickers': ['CSCO']}, 'other': {'tickers': ['CSCO', 'JPM']}},
            'members': [{'id': 'one', 'name': 'Alice Example', 'email': 'alice@example.com',
                         'groups': ['tech', 'other'], 'enabled': True,
                         'timezone': 'America/Toronto', 'send_weekday': 0, 'send_time': '09:00'}]}


@pytest.fixture
def store(tmp_path):
    reports = []
    for ticker in ('CSCO', 'JPM'):
        base = Path('archive/run-1') / ticker
        entry = {'ticker': ticker, 'report_id': f'run-1/{ticker}', 'quality': 'ready',
                 'generated_at': '2026-10-19T12:00:00+00:00', 'as_of': '2026-10-19'}
        snapshot = emit_frozen_snapshot(
            ticker=ticker, as_of=entry['as_of'], quant_metrics={'Close': 100},
            ai={'status': 'Available'}, freshness={}, disclaimer='Not investment advice.')
        snapshot['quality'] = 'ready'
        for kind in ('md', 'pdf', 'json'):
            relative = base / f'{ticker}-intelligence-20261019.{kind}'
            path = tmp_path / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text({'md': f'# {ticker}\n', 'pdf': '%PDF-1.4 test',
                             'json': json.dumps(snapshot)}[kind])
            entry[kind] = relative.as_posix()
        entry['sha256'] = {kind: digest(tmp_path / entry[kind]) for kind in ('md', 'pdf', 'json')}
        reports.append(entry)
    write_json(tmp_path / 'index.json', {'reports': reports})
    return tmp_path


def test_recent_news_is_not_discarded(monkeypatch):
    xml = b'''<rss><channel><item><title>Cisco stock gains</title><pubDate>Fri, 16 Oct 2026 12:00:00 GMT</pubDate></item><item><title>Old</title><pubDate>Fri, 02 Oct 2026 12:00:00 GMT</pubDate></item><item><title>Future</title><pubDate>Mon, 19 Oct 2026 12:00:00 GMT</pubDate></item></channel></rss>'''
    monkeypatch.setattr(ai_extract.urllib.request, 'urlopen', lambda *a, **k: io.BytesIO(xml))
    items, status = ai_extract.fetch_rss('Cisco', as_of='2026-10-17', window_days=7)
    assert [x['headline'] for x in items] == ['Cisco stock gains']
    assert status['status'] == 'ok'
    assert ai_extract.extract([], 'CSCO', as_of='2026-10-17')['as_of'] == '2026-10-17'


def test_groups_overlap_and_multiple_members(config):
    second = dict(config['members'][0], id='two', email='bob@example.com')
    config['members'].append(second)
    validate(config)
    assert tickers_for(config, second) == ['CSCO', 'JPM']
    second['enabled'] = False
    assert tickers_for(config) == ['CSCO', 'JPM']
    config['members'][0]['enabled'] = False
    assert tickers_for(config) == []


@pytest.mark.parametrize('field,value', [('enabled', 'false'), ('timezone', 'invalid'),
    ('send_time', '25:00'), ('send_weekday', True), ('groups', ['unknown']), ('name', 'A\nB')])
def test_invalid_members(config, field, value):
    config['members'][0][field] = value
    with pytest.raises(ValueError):
        validate(config)


def test_due_time_and_dst(config):
    m = config['members'][0]
    assert weekly.due_period(m, datetime(2026, 10, 19, 12, 59, tzinfo=timezone.utc)) is None
    assert weekly.due_period(m, NOW) == '2026-10-19'
    assert weekly.due_period(m, datetime(2026, 11, 2, 13, 59, tzinfo=timezone.utc)) is None
    assert weekly.due_period(m, datetime(2026, 11, 2, 14, tzinfo=timezone.utc)) == '2026-11-02'


def test_personalized_pdfs_and_once_per_week(config, store):
    sent = []
    first = weekly.deliver(config, store, now=NOW, really_send=True, backend=sent.append)
    again = weekly.deliver(config, store, now=NOW, really_send=True, backend=sent.append)
    assert first['sent'] == 1 and again['skipped'] == 1 and len(sent) == 1
    assert len(list(sent[0].iter_attachments())) == 2
    assert 'Hi Alice Example,' in sent[0].get_body(preferencelist=('plain',)).get_content()
    ledger = (store / 'state/deliveries.json').read_text()
    assert 'alice@example.com' not in ledger and 'Alice' not in ledger


def test_uncertain_send_is_not_retried(config, store):
    calls = []
    def fail(message):
        calls.append(message)
        raise TimeoutError('SMTP may have accepted the email')
    assert weekly.deliver(config, store, now=NOW, really_send=True, backend=fail)['unknown'] == 1
    weekly.deliver(config, store, now=NOW, really_send=True, backend=fail)
    assert len(calls) == 1


def test_persist_before_transport(config, store, monkeypatch):
    sent = []
    def fail(*args):
        raise OSError('Storage unavailable')
    monkeypatch.setattr(weekly, 'persist', fail)
    with pytest.raises(OSError):
        weekly.deliver(config, store, now=NOW, really_send=True, backend=sent.append)
    assert not sent


def test_preview_does_not_consume_week(config, store):
    assert weekly.deliver(config, store, now=NOW)['prepared'] == 1
    assert not (store / 'state/deliveries.json').exists()
    assert weekly.deliver(config, store, now=NOW, really_send=True, backend=lambda _: None)['sent'] == 1


def test_table_personal_choices_and_opt_out_drive_the_digest(config, store):
    from email import policy
    from email.parser import BytesParser
    config['members'][0]['tickers'] = ['CSCO']
    config['members'].append(dict(config['members'][0], id='two', name='Bob Example',
                                  email='bob@example.com', tickers=['JPM'], enabled=False))
    output = store.with_name(store.name + '-mail-previews')
    result = weekly.deliver(config, store, now=NOW, preview_dir=output)
    assert result['prepared'] == 1 and result['skipped'] == 1
    files = list(output.glob('*.eml'))
    assert len(files) == 1 and files[0].stat().st_mode & 0o777 == 0o600
    message = BytesParser(policy=policy.default).parsebytes(files[0].read_bytes())
    body = message.get_body(preferencelist=('plain',)).get_content().replace('\r\n', '\n')
    assert body.strip() == ('Hi Alice Example,\n\nHere are the latest JSOSIF intelligence reports:'
                            '\n\n- CSCO — 2026-10-19\n\nBest,\nTech Team')
    assert str(message['To']) == 'alice@example.com'
    assert [part.get_filename() for part in message.iter_attachments()] == ['CSCO-intelligence-20261019.pdf']
    assert not (store / 'state/deliveries.json').exists()


def test_pre_presentation_preview_does_not_wait_for_the_weekly_slot(config, store):
    config['members'][0]['send_weekday'] = 2
    assert weekly.deliver(config, store, now=NOW)['skipped'] == 1
    output = store.with_name(store.name + '-advance-preview')
    result = weekly.deliver(config, store, now=NOW, preview_all=True, preview_dir=output,
                            backend=lambda _: pytest.fail('Preview must not contact SMTP'))
    assert result['prepared'] == 1
    assert len(list(output.glob('*.eml'))) == 1
    assert not (store / 'state/deliveries.json').exists()
    with pytest.raises(ValueError, match='Preview'):
        weekly.deliver(config, store, really_send=True, preview_all=True)


def test_private_email_preview_cannot_be_published_in_the_archive(config, store):
    with pytest.raises(ValueError, match='outside'):
        weekly.deliver(config, store, now=NOW, preview_dir=store / 'archive/previews')
    assert not list(store.rglob('*.eml'))


def test_site_overview_metrics_come_from_the_saved_snapshot(store, tmp_path):
    index = read_json(store / 'index.json')
    entry = index['reports'][0]
    payload = read_json(store / entry['json'])
    payload['quant'][0]['value'] = '0'
    write_json(store / entry['json'], payload)
    entry['sha256']['json'] = digest(store / entry['json'])
    write_json(store / 'index.json', index)
    output = store.with_name(store.name + '-summary-site')
    build(store, output)
    public = read_json(output / 'index.json')
    assert public['reports'][0]['summary']['close'] == '0'
    assert public['publication']['refresh_seconds'] == 60
    assert public['publication']['published_at']
    assert 'summary' not in read_json(store / 'index.json')['reports'][0]


def test_corrupt_pdf_blocks_delivery(config, store):
    next(store.rglob('*.pdf')).write_text('%PDF changed')
    assert weekly.deliver(config, store, now=NOW, really_send=True,
                          backend=lambda _: pytest.fail('Must not send'))['deferred'] == 1


@pytest.mark.parametrize('corruption', ['identity', 'quality', 'contract', 'pdf', 'paths'])
def test_rehashed_invalid_archive_is_not_delivered(config, store, corruption):
    output = store.with_name(store.name + '-verified-site')
    build(store, output)
    previous_index = (output / 'index.json').read_bytes()
    index = read_json(store / 'index.json')
    entry = index['reports'][0]
    path = store / entry['json']
    payload = read_json(path)
    if corruption == 'identity':
        payload['identity']['ticker'] = 'JPM'
    elif corruption == 'quality':
        payload['quality'] = 'historical'
    elif corruption == 'contract':
        payload = {}
    elif corruption == 'pdf':
        (store / entry['pdf']).write_bytes(b'Not a PDF')
    elif corruption == 'paths':
        entry['json'] = index['reports'][1]['json']
    if corruption != 'paths':
        write_json(path, payload)
    entry['sha256'] = {kind: digest(store / entry[kind]) for kind in ('md', 'json', 'pdf')}
    write_json(store / 'index.json', index)
    result = weekly.deliver(config, store, now=NOW, really_send=True,
                            backend=lambda _: pytest.fail('Invalid archive must not be sent'))
    assert result['deferred'] == 1
    assert not (store / 'state/deliveries.json').exists()
    with pytest.raises(ValueError):
        build(store, output)
    assert (output / 'index.json').read_bytes() == previous_index


def test_stale_or_disabled_members_are_not_sent(config, store):
    config['members'][0]['enabled'] = False
    assert weekly.deliver(config, store, now=NOW)['skipped'] == 1
    config['members'][0]['enabled'] = True
    later = datetime(2026, 10, 26, 14, tzinfo=timezone.utc)
    assert weekly.deliver(config, store, now=later)['deferred'] == 1


def test_site_has_all_versions_but_no_private_state(store, tmp_path):
    write_json(store / 'state/deliveries.json', {'private': 'sensitive'})
    output = tmp_path.parent / (tmp_path.name + '-site')
    build(store, output)
    assert len(read_json(output / 'index.json')['reports']) == 2
    assert len(list(output.rglob('*.pdf'))) == 2
    assert not (output / 'state').exists()


def test_provider_header_usage_and_safe_errors(monkeypatch):
    monkeypatch.setenv('GEMINI_API_KEY', 'synthetic-secret')
    monkeypatch.delenv('JSOSIF_API_USAGE_PATH', raising=False)
    calls = []
    def opener(request, **kwargs):
        calls.append(request)
        return io.BytesIO(json.dumps({'candidates': [{'content': {'parts': [{'text': '{}'}]}}],
                                     'usageMetadata': {'promptTokenCount': 10}}).encode())
    result = generate_json('test', opener=opener)
    assert result['usage']['promptTokenCount'] == 10
    assert 'synthetic-secret' not in calls[0].full_url
    assert calls[0].get_header('X-goog-api-key') == 'synthetic-secret'
    monkeypatch.delenv('GEMINI_API_KEY')
    monkeypatch.delenv('GOOGLE_API_KEY', raising=False)
    with pytest.raises(GeminiError, match='not configured'):
        generate_json('test', opener=opener)


def test_quota_rotation_prioritizes_missing_and_older_reports():
    index = {'reports': [{'ticker': 'CSCO', 'generated_at': '2026-10-19T12:00:00+00:00'}]}
    tickers, plan = quota_plan(['CSCO', 'JPM', 'COST'], index, 10)
    assert tickers == ['COST', 'JPM']
    assert plan['full_rotation_days'] == 2
    assert plan['tickers_per_day'] * 3 <= plan['local_daily_budget']
    with pytest.raises(ValueError):
        quota_plan(['CSCO'], index, 0)


def test_provider_counts_attempts_and_blocks_exhausted_budget(tmp_path, monkeypatch):
    from gemini_provider import reserve_request
    path = tmp_path / 'usage.json'
    monkeypatch.setenv('JSOSIF_API_USAGE_PATH', str(path))
    monkeypatch.setenv('GEMINI_RPD', '2')
    monkeypatch.setenv('GEMINI_RPM', '1000')
    reserve_request('test-model')
    with pytest.raises(GeminiError, match='exhausted'):
        reserve_request('test-model')


def test_archive_versions_are_immutable(tmp_path, monkeypatch):
    import refresh_reports as refresh
    from snapshot_emit import emit_frozen_snapshot, NO_REFRESH_NOTE
    reports = tmp_path / 'reports'; data = tmp_path / 'data'; root = tmp_path / 'store'
    reports.mkdir(); data.mkdir()
    monkeypatch.setattr(refresh, 'REPORTS', reports); monkeypatch.setattr(refresh, 'DATA', data)
    payload = emit_frozen_snapshot(ticker='CSCO', as_of='2026-10-19', quant_metrics={'Close': 100},
                                  ai={}, freshness={}, disclaimer='Not investment advice')
    payload['quality'] = 'ready'
    base = reports / 'CSCO-intelligence-20261019'
    base.with_suffix('.md').write_text('# CSCO')
    base.with_suffix('.json').write_text(json.dumps(payload))
    base.with_suffix('.pdf').write_bytes(b'%PDF-1.4 original')
    for name in ('quant', 'info', 'ai-intel', 'rss-items', 'comparables', 'earnings', 'edgar'):
        (data / f'csco-{name}.json').write_text('{}')
    (data / 'fred.json').write_text('{}')
    first = refresh.archive(root, 'CSCO', '20261019', 'run-1', NOW.isoformat())
    base.with_suffix('.pdf').write_bytes(b'%PDF-1.4 updated')
    second = refresh.archive(root, 'CSCO', '20261019', 'run-2', NOW.isoformat())
    assert (root / first['pdf']).read_bytes() == b'%PDF-1.4 original'
    assert (root / second['pdf']).read_bytes() == b'%PDF-1.4 updated'
    with pytest.raises(ValueError, match='already exists'):
        refresh.archive(root, 'CSCO', '20261019', 'run-1', NOW.isoformat())


def test_quota_plan_subtracts_same_day_attempts():
    index = {'reports': []}
    selected, plan = quota_plan(['CSCO', 'JPM', 'COST'], index, 10, used_requests=5)
    assert selected == ['COST']
    assert plan['remaining_requests'] == 3 and plan['used_requests_today'] == 5
    selected, plan = quota_plan(['CSCO'], index, 10, used_requests=8)
    assert selected == [] and plan['remaining_requests'] == 0


def test_provider_day_resets_in_pacific_time():
    from gemini_provider import quota_day
    assert quota_day(datetime(2026, 10, 18, 6, 59, tzinfo=timezone.utc)) == '2026-10-17'
    assert quota_day(datetime(2026, 10, 18, 7, 0, tzinfo=timezone.utc)) == '2026-10-18'


def test_fall_back_second_hour_does_not_undo_due_time(config):
    member = dict(config['members'][0], send_weekday=6, send_time='01:30')
    assert weekly.due_period(member, datetime(2026, 11, 1, 5, 29, tzinfo=timezone.utc)) is None
    assert weekly.due_period(member, datetime(2026, 11, 1, 6, 15, tzinfo=timezone.utc)) == '2026-10-26'


def test_spring_gap_moves_forward_by_gap(config):
    member = dict(config['members'][0], send_weekday=6, send_time='02:30')
    assert weekly.due_period(member, datetime(2026, 3, 8, 7, 10, tzinfo=timezone.utc)) is None
    assert weekly.due_period(member, datetime(2026, 3, 8, 7, 30, tzinfo=timezone.utc)) == '2026-03-02'


def test_failed_site_build_preserves_last_good_output(store, tmp_path):
    output = tmp_path.parent / (tmp_path.name + '-atomic-site')
    build(store, output)
    previous = {p.relative_to(output): p.read_bytes() for p in output.rglob('*') if p.is_file()}
    next(store.rglob('*.pdf')).write_bytes(b'%PDF-1.4 corrupt')
    with pytest.raises(ValueError, match='integrity'):
        build(store, output)
    assert {p.relative_to(output): p.read_bytes() for p in output.rglob('*') if p.is_file()} == previous


def test_missing_store_cannot_erase_site(store, tmp_path):
    output = tmp_path.parent / (tmp_path.name + '-missing-store-site')
    build(store, output)
    index = (output / 'index.json').read_bytes()
    (store / 'index.json').unlink()
    with pytest.raises(ValueError, match='persisted archive index'):
        build(store, output)
    assert (output / 'index.json').read_bytes() == index


@pytest.mark.parametrize('path', ['/tmp/report.pdf', '../report.pdf', 'archive/../../report.pdf', 'archive\\report.pdf'])
def test_report_manifest_paths_cannot_escape_store(tmp_path, path):
    from report_store import resolve_file
    with pytest.raises(ValueError):
        resolve_file(tmp_path, path)


def test_reconciliation_respects_active_delivery_lock(store, monkeypatch):
    import fcntl
    import sys
    import delivery_state
    monkeypatch.setattr(sys, 'argv', ['delivery_state.py', '--store', str(store),
                                     '--member-id', 'example', '--period', '2026-10-19',
                                     '--resolution', 'retry'])
    with (store / '.delivery.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        with pytest.raises(BlockingIOError):
            delivery_state.main()


def test_exhausted_quota_only_disables_ai_budget(tmp_path, monkeypatch):
    import sys
    import refresh_reports as refresh
    monkeypatch.setenv('GEMINI_API_KEY', 'synthetic')
    monkeypatch.setenv('GEMINI_MODEL', 'test-model')
    monkeypatch.setenv('GEMINI_RPD', '10')
    monkeypatch.setenv('GEMINI_RPM', '3')
    monkeypatch.setenv('SEC_USER_AGENT', 'Synthetic fixture contact@example.com')
    monkeypatch.delenv('GEMINI_CLI', raising=False)
    monkeypatch.setattr(refresh, 'quota_day', lambda *args: '2026-10-17')
    write_json(tmp_path / 'state/api-usage.json', {'test-model:2026-10-17': 8})
    selected, plan = refresh.ai_budget(['CSCO'], {'reports': []}, tmp_path, NOW)
    assert selected == []
    assert plan['remaining_requests'] == 0
    assert 'insufficient' in plan['reason']


def test_recently_packaged_old_report_is_not_fresh(config, store):
    index = read_json(store / 'index.json')
    for entry in index['reports']:
        entry['as_of'] = '2026-10-08'
    write_json(store / 'index.json', index)
    config['allow_degraded'] = True
    assert weekly.deliver(config, store, now=NOW, really_send=True,
                          backend=lambda _: pytest.fail('Old report must be deferred'))['deferred'] == 1


def test_history_import_does_not_postpone_real_collection():
    index = {'reports': [{'ticker': 'CSCO', 'generated_at': NOW.isoformat(), 'quality': 'historical'},
                         {'ticker': 'JPM', 'generated_at': '2026-10-18T12:00:00+00:00', 'quality': 'ready'}]}
    selected, _ = quota_plan(['CSCO', 'JPM'], index, 5)
    assert selected == ['CSCO']


def test_zero_age_allows_today_but_not_yesterday(config, store):
    config['max_report_age_days'] = 0
    validate(config)
    assert weekly.deliver(config, store, now=NOW)['prepared'] == 1
    index = read_json(store / 'index.json')
    index['reports'][0]['as_of'] = '2026-10-18'
    write_json(store / 'index.json', index)
    assert weekly.deliver(config, store, now=NOW)['deferred'] == 1


@pytest.mark.parametrize('changes', [
    {'generated_at': 'bad-date'}, {'generated_at': '2026-10-19T12:00:00'},
    {'generated_at': None}, {'as_of': 'bad-date'}, {'as_of': None},
    {'report_id': None}, {'sha256': None}, {'pdf': None},
])
def test_bad_metadata_does_not_block_other_members(config, store, changes):
    config['members'][0]['groups'] = ['tech']
    config['groups']['bank'] = {'tickers': ['JPM']}
    config['members'].append(dict(config['members'][0], id='two',
                                  email='bob@example.com', groups=['bank']))
    index = read_json(store / 'index.json')
    index['reports'][0].update(changes)
    write_json(store / 'index.json', index)
    sent = []
    result = weekly.deliver(config, store, now=NOW, really_send=True, backend=sent.append)
    assert result['deferred'] == 1 and result['sent'] == 1
    assert str(sent[0]['To']) == 'bob@example.com'


def test_bad_old_metadata_does_not_hide_valid_report(config, store):
    index = read_json(store / 'index.json')
    index['reports'].insert(0, dict(index['reports'][0], generated_at='bad-date'))
    index['reports'].append(None)
    write_json(store / 'index.json', index)
    assert weekly.deliver(config, store, now=NOW)['prepared'] == 1


@pytest.mark.parametrize('headline,ticker', [
    ('Visa rival Mastercard wins major contract', 'V'),
    ("Visa's competitor Mastercard raises its dividend", 'V'),
    ('Visa (V) rival Mastercard wins major contract', 'V'),
    ('Visa and Mastercard win major contracts', 'V'),
    ('Visa rival Mastercard stock rises', 'V'),
    ('J&J wins major contract', 'J'),
])
def test_competitor_and_ambiguous_ticker_news_requires_review(headline, ticker):
    item = {'headline': headline, 'pubDate': 'Fri, 16 Oct 2026 12:00:00 GMT'}
    data = ai_extract.extract([item], ticker, as_of='2026-10-17')
    assert data['extraction_stats']['rule'] == 0
    assert len(data['unclassified']) == 1


@pytest.mark.parametrize('headline,ticker', [
    ('Visa wins major contract', 'V'), ('Jacobs wins major contract', 'J'),
    ('$J wins major contract', 'J'), ('(V) wins major contract', 'V'),
])
def test_unambiguous_company_and_cashtag_rules_still_work(headline, ticker):
    item = {'headline': headline, 'pubDate': 'Fri, 16 Oct 2026 12:00:00 GMT'}
    assert ai_extract.classify_rule(item, ticker)[1]['extraction_method'] == 'rule'


@pytest.mark.parametrize('instant,as_of,expected', [
    ('2026-12-03T00:15:00+00:00', '2026-12-02', True),
    ('2026-12-03T00:15:00+00:00', '2026-12-03', False),
    ('2026-12-03T05:15:00+00:00', '2026-12-02', False),
])
def test_zero_age_uses_toronto_report_date(store, instant, as_of, expected):
    entry = read_json(store / 'index.json')['reports'][0]
    entry.update(as_of=as_of, generated_at='2026-12-02T23:30:00+00:00')
    assert weekly.eligible_report(entry, 'CSCO', {'max_report_age_days': 0},
                                  datetime.fromisoformat(instant)) is expected


@pytest.fixture
def published(store):
    from functools import partial
    from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
    from threading import Thread
    index = read_json(store / 'index.json')
    index['last_attempt'] = {'business_date': '2026-10-19', 'status': 'complete',
                             'expected_tickers': ['CSCO', 'JPM'], 'successful_tickers': ['CSCO', 'JPM'],
                             'degraded_tickers': [], 'failed_tickers': []}
    write_json(store / 'index.json', index)
    output = store.with_name(store.name + '-http-site')
    build(store, output)
    class Quiet(SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(Quiet, directory=str(output)))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield 'http://127.0.0.1:' + str(server.server_port), output
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


def test_deployed_publication_verifies_every_current_file(published):
    from check_site import check
    base, _ = published
    result = check(base, business_date='2026-10-19', require_ready=True)
    assert result['holdings'] == 2 and result['files_verified'] == 6


def test_healthy_local_archive_cannot_mask_a_broken_deployed_pdf(published):
    from check_site import check, SiteError
    base, output = published
    next(output.rglob('*.pdf')).write_bytes(b'<html>Unavailable</html>')
    with pytest.raises(SiteError, match='integrity'):
        check(base, business_date='2026-10-19', require_ready=True)


def test_deployment_check_rejects_stale_day_and_mixed_publications(published):
    from check_site import check, SiteError
    base, output = published
    with pytest.raises(SiteError, match='expected business date'):
        check(base, business_date='2026-10-20')
    health = read_json(output / 'health.json')
    health['published_at'] = '2026-10-18T00:00:00+00:00'
    write_json(output / 'health.json', health)
    with pytest.raises(SiteError, match='different publications'):
        check(base, business_date='2026-10-19')


def test_deployment_check_rejects_missing_holding(published):
    from check_site import check, SiteError
    base, output = published
    index = read_json(output / 'index.json')
    index['reports'] = index['reports'][:1]
    write_json(output / 'index.json', index)
    with pytest.raises(SiteError, match='missing'):
        check(base, business_date='2026-10-19')


def test_due_delivery_deferral_fails_the_sending_job_without_contacting_smtp(config, store, monkeypatch):
    import sys
    monkeypatch.setattr(sys, 'argv', ['deliver_weekly.py', '--config', 'synthetic.json',
                                     '--store', str(store), '--send'])
    monkeypatch.setenv('JSOSIF_APPROVED_SEND', '1')
    monkeypatch.setattr(weekly, 'load', lambda _: config)
    monkeypatch.setattr(weekly.GmailSmtpBackend, 'credentials', lambda _: ('synthetic@example.com', 'synthetic'))
    monkeypatch.setattr(weekly, 'deliver', lambda *a, **kw: {'unknown': 0, 'deferred': 1})
    with pytest.raises(SystemExit, match='deferred'):
        weekly.main()


def test_schedule_aware_site_check_accepts_a_newer_manual_publication_but_not_stale_data(published):
    from check_site import check, SiteError
    base, _ = published
    result = check(base, business_date='2026-10-18', allow_newer=True, latest_date='2026-10-20', require_ready=True)
    assert result['business_date'] == '2026-10-19'
    with pytest.raises(SiteError, match='stale or future'):
        check(base, business_date='2026-10-20', allow_newer=True, latest_date='2026-10-20')
    with pytest.raises(SiteError, match='stale or future'):
        check(base, business_date='2026-10-18', allow_newer=True, latest_date='2026-10-18')
