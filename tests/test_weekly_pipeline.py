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
        for kind in ('md', 'pdf', 'json'):
            relative = base / f'{ticker}-intelligence-20261019.{kind}'
            path = tmp_path / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text({'md': f'# {ticker}\n', 'pdf': '%PDF-1.4 test', 'json': '{}'}[kind])
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


def test_corrupt_pdf_blocks_delivery(config, store):
    next(store.rglob('*.pdf')).write_text('%PDF changed')
    assert weekly.deliver(config, store, now=NOW, really_send=True,
                          backend=lambda _: pytest.fail('Must not send'))['deferred'] == 1


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
