"""Offline coverage for the SEC EDGAR collector: retries, period selection, fallbacks."""
import io
import json
from urllib.error import HTTPError, URLError

import pytest

import data_utils
import edgar


@pytest.fixture(autouse=True)
def env(tmp_path, monkeypatch):
    monkeypatch.setattr(data_utils, 'DATA', tmp_path)
    monkeypatch.setattr(edgar.time, 'sleep', lambda *_: None)
    monkeypatch.setenv('SEC_USER_AGENT', 'Test Org contact@example.com')
    monkeypatch.setenv('REPORT_AS_OF', '2026-10-08')
    monkeypatch.delenv('JSOSIF_SEC_CACHE', raising=False)
    monkeypatch.delenv('GMAIL_USER', raising=False)


class Resp(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def http_error(code):
    return HTTPError('https://x', code, 'err', {}, io.BytesIO(b''))


def test_fetch_requires_contact_identity(monkeypatch):
    monkeypatch.delenv('SEC_USER_AGENT')
    with pytest.raises(ValueError):
        edgar.fetch('https://data.sec.gov/x')


def test_fetch_sends_identity_and_retries_transient_errors(monkeypatch):
    seen, calls = [], iter([http_error(503), URLError('down'), Resp(b'{"ok": 1}')])

    def fake(request, timeout):
        seen.append(request.get_header('User-agent'))
        item = next(calls)
        if isinstance(item, Exception):
            raise item
        return item
    monkeypatch.setattr(edgar, 'urlopen', fake)
    assert edgar.fetch('https://data.sec.gov/x') == {'ok': 1}
    assert seen == ['Test Org contact@example.com'] * 3


def test_fetch_does_not_retry_client_errors_and_gives_up_after_three(monkeypatch):
    count = []

    def not_found(request, timeout):
        count.append(1)
        raise http_error(404)
    monkeypatch.setattr(edgar, 'urlopen', not_found)
    with pytest.raises(HTTPError):
        edgar.fetch('https://data.sec.gov/x')
    assert len(count) == 1
    count.clear()

    def busy(request, timeout):
        count.append(1)
        raise http_error(429)
    monkeypatch.setattr(edgar, 'urlopen', busy)
    with pytest.raises(HTTPError):
        edgar.fetch('https://data.sec.gov/x')
    assert len(count) == 3


def obs(start, end, val, filed, form='10-Q', **extra):
    return {'start': start, 'end': end, 'val': val, 'filed': filed, 'form': form, 'fy': 2026, 'fp': 'Q2', **extra}


def test_quarter_value_uses_latest_quarter_filed_by_as_of_and_ignores_bad_rows(monkeypatch):
    rows = [
        obs('2026-04-01', '2026-06-30', 100, '2026-08-01'),
        obs('2026-07-01', '2026-09-30', 999, '2026-10-20'),        # filed after the as-of date
        obs('2026-01-01', '2026-06-30', 555, '2026-08-01'),        # half-year, not a quarter
        obs('2026-04-01', '2026-06-30', 777, '2026-08-01', form='8-K'),
        {'val': 1, 'form': '10-Q', 'filed': '2026-08-01'},         # missing period
        obs('2026-04-01', '2026-06-30', 'n/a', '2026-08-02'),      # non-numeric
    ]
    monkeypatch.setattr(edgar, 'fetch', lambda url: {'units': {'USD': rows}})
    result = edgar.quarter_value('Revenues', '320193')
    assert result['value'] == 100
    assert result['period'] == '2026-04-01/2026-06-30'
    assert result['unit'] == 'USD'


def test_quarter_value_none_without_usable_rows(monkeypatch):
    monkeypatch.setattr(edgar, 'fetch', lambda url: {'units': {}})
    assert edgar.quarter_value('Revenues', '1') is None


def test_quarter_value_zero_pads_cik(monkeypatch):
    urls = []
    monkeypatch.setattr(edgar, 'fetch', lambda url: urls.append(url) or {})
    edgar.quarter_value('Revenues', '858877')
    assert 'CIK0000858877' in urls[0]


def run_main(monkeypatch, tmp_path, fetch, symbol='CSCO', cik='858877'):
    monkeypatch.setattr(edgar, 'ticker_arg', lambda: symbol)
    monkeypatch.setattr(edgar, 'resolve_cik', lambda s: cik)
    monkeypatch.setattr(edgar, 'fetch', fetch)
    edgar.main()
    return json.loads((tmp_path / f'{symbol.lower()}-edgar.json').read_text())


def submissions():
    return {'filings': {'recent': {
        'form': ['8-K', '10-K', '10-Q', '10-Q'],
        'filingDate': ['2026-10-01', '2026-09-01', '2026-08-01', '2026-10-20'],
        'accessionNumber': ['a-1', '0001-26-000001', '0001-26-000002', '0001-26-000003'],
        'primaryDocument': ['x.htm', 'k.htm', 'q.htm', 'future.htm']}}}


def test_main_picks_latest_eligible_filing_and_falls_back_to_contract_revenue(monkeypatch, tmp_path):
    def fetch(url):
        if 'submissions' in url:
            return submissions()
        if url.endswith('/Revenues.json'):
            return {'units': {'USD': []}}
        return {'units': {'USD': [obs('2026-04-01', '2026-06-30', 42, '2026-08-01')]}}
    data = run_main(monkeypatch, tmp_path, fetch)
    assert data['latest_filing']['accession'] == '0001-26-000001'
    assert data['latest_filing']['url'].endswith('/858877/000126000001/k.htm')
    assert data['revenue']['value'] == 42
    assert data['net_income']['value'] == 42


def test_main_survives_every_sec_failure(monkeypatch, tmp_path):
    def fetch(url):
        raise URLError('offline')
    data = run_main(monkeypatch, tmp_path, fetch)
    assert data['cik'] == '858877'
    assert data['latest_filing'] is None and data['revenue'] is None and data['net_income'] is None


def test_main_without_issuer_mapping_writes_explicit_na(monkeypatch, tmp_path):
    data = run_main(monkeypatch, tmp_path, lambda url: pytest.fail('no SEC request expected'),
                    symbol='AIR.PA', cik=None)
    assert data['cik'] is None
    assert data['error'].startswith('N/A')
