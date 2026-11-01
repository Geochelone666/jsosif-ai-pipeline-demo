"""Production health must distinguish quota failures from data/integrity failures."""
import json

from production_health import build_health, failure_reason, markdown
from report_store import write_json


def fake_report(root, ticker, quality, ai, *, run='r1', date='2026-10-24'):
    folder = root / 'archive' / run / ticker
    sources = folder / 'sources'
    sources.mkdir(parents=True, exist_ok=True)
    (sources / (ticker.lower() + '-ai-intel.json')).write_text(json.dumps(ai))
    report = folder / 'report.json'
    report.write_text(json.dumps({
        'source_status': {
            'market': 'ok',
            'news': 'ok' if quality == 'ready' else 'degraded',
        }
    }))
    return {'ticker': ticker, 'quality': quality, 'as_of': date,
            'report_id': run + '/' + ticker,
            'generated_at': date + 'T22:00:00Z',
            'json': f'archive/{run}/{ticker}/report.json'}


def test_health_categories_are_specific_and_never_overstate_readiness(tmp_path, monkeypatch):
    root = tmp_path
    first = fake_report(root, 'AAPL', 'ready', {
        'extraction_stats': {'rule': 3, 'ai': 2, 'unknown': 0, 'irrelevant': 1},
        'rss_audit': {'unique_publishers': 3},
        'ai_reuse': {'reused_headlines': 2},
        'decision_audit': {'flag_count': 1},
    })
    second = fake_report(root, 'V', 'degraded', {
        'error': 'AI unavailable: Groq application daily budget exhausted (tokens)',
        'fetch_status': {'status': 'ok'},
        'extraction_stats': {'rule': 1, 'ai': 0, 'unknown': 9},
    })
    write_json(root / 'index.json', {
        'last_attempt': {
            'run_id': 'r1', 'business_date': '2026-10-24', 'status': 'degraded',
            'expected_tickers': ['AAPL', 'V', 'XYL'],
        },
        'refresh_plan': {'priority_policy': 'least_recently_ready_then_date_rotation'},
        'reports': [first, second],
    })
    monkeypatch.setattr('production_health.verified_report_files',
                        lambda root, entry: {'json': root / entry['json']})
    h = build_health(root)
    assert (h['expected'], h['ready'], h['degraded_or_unverified']) == (3, 1, 2)
    assert not h['strict_release_eligible']
    assert h['failure_reasons']['groq_daily_tokens'] == 1
    assert h['integrity_errors']['missing_report'] == 1
    assert h['classification_totals']['ai'] == 2
    assert h['classification_totals']['unknown'] == 9
    assert h['verified_ai_decisions_reused'] == 2
    assert h['nonblocking_decision_review_flags'] == 1
    text = markdown(h)
    assert 'V: degraded / groq_daily_tokens' in text
    assert 'XYL: missing / missing_report' in text
    assert 'evidence completeness' in text


def test_corrupt_report_is_ineligible(tmp_path, monkeypatch):
    report = fake_report(tmp_path, 'AAPL', 'ready', {'extraction_stats': {}})
    write_json(tmp_path / 'index.json', {
        'last_attempt': {'run_id': 'r1', 'business_date': '2026-10-24',
                         'status': 'complete', 'expected_tickers': ['AAPL']},
        'reports': [report],
    })
    def reject(*args):
        raise ValueError('bad source digest')
    monkeypatch.setattr('production_health.verified_report_files', reject)
    h = build_health(tmp_path)
    assert h['ready'] == 0
    assert not h['strict_release_eligible']
    assert h['integrity_errors']['archive_integrity'] == 1


def test_reason_priority_does_not_misdiagnose_market_failure_as_token_limit():
    ai = {'error': 'AI unavailable: Groq application daily budget exhausted (tokens)'}
    assert failure_reason({'source_status': {'market': 'failed'}}, ai) == 'market_source_invalid'
    assert failure_reason({'source_status': {'market': 'ok'}},
                          {'fetch_status': {'status': 'failed'}}) == 'rss_fetch_failed'
    assert failure_reason({'source_status': {'market': 'ok', 'news': 'degraded'}},
                          {'extraction_stats': {'unknown': 2}}) == 'unresolved_news_classification'


def _allow_all_archives(monkeypatch):
    stub = lambda root, entry: {'json': root / entry['json']}
    monkeypatch.setattr('production_health.verified_report_files', stub)
    monkeypatch.setattr('check_release.verified_report_files', stub)


def _single_ticker_index(reports, status='complete'):
    return {'last_attempt': {'run_id': 'r1', 'business_date': '2026-10-24',
                             'status': status, 'expected_tickers': ['AAPL']},
            'reports': reports}


def test_clean_complete_run_is_strict_eligible(tmp_path, monkeypatch):
    report = fake_report(tmp_path, 'AAPL', 'ready', {'extraction_stats': {}})
    write_json(tmp_path / 'index.json', _single_ticker_index([report]))
    _allow_all_archives(monkeypatch)
    h = build_health(tmp_path)
    assert h['ready'] == 1
    assert h['strict_release_eligible'] is True


def test_advisory_report_is_not_strict_eligible(tmp_path, monkeypatch):
    # The row itself is ready, but check_release rejects advisories under
    # --require-ready; health eligibility must not overstate the gate.
    report = fake_report(tmp_path, 'AAPL', 'ready', {'extraction_stats': {}})
    report['advisory'] = 'SEC identity unverified in this archived version'
    write_json(tmp_path / 'index.json', _single_ticker_index([report]))
    _allow_all_archives(monkeypatch)
    h = build_health(tmp_path)
    assert h['ready'] == 1
    assert h['strict_release_eligible'] is False


def test_newer_prior_run_degradation_is_not_strict_eligible(tmp_path, monkeypatch):
    # Health rows prefer the current run's ready report; the strict gate looks
    # at the newest archived version per ticker and must win.
    current = fake_report(tmp_path, 'AAPL', 'ready', {'extraction_stats': {}}, run='r1')
    regenerated = fake_report(tmp_path, 'AAPL', 'degraded', {'extraction_stats': {}}, run='r0')
    regenerated['generated_at'] = '2026-10-24T23:59:00Z'
    write_json(tmp_path / 'index.json', _single_ticker_index([current, regenerated]))
    _allow_all_archives(monkeypatch)
    h = build_health(tmp_path)
    assert h['ready'] == 1
    assert h['strict_release_eligible'] is False


def test_incomplete_run_is_not_strict_eligible_even_when_rows_ready(tmp_path, monkeypatch):
    report = fake_report(tmp_path, 'AAPL', 'ready', {'extraction_stats': {}})
    write_json(tmp_path / 'index.json', _single_ticker_index([report], status='partial'))
    _allow_all_archives(monkeypatch)
    h = build_health(tmp_path)
    assert h['strict_release_eligible'] is False
