"""Offline coverage for graceful price provider failures."""
import io
import json
from pathlib import Path
import runpy
import socket
import sys
from unittest.mock import Mock
from urllib.error import HTTPError, URLError

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import data_utils
import price_fetch as pf


def http(code):
    return HTTPError('https://example.invalid', code, 'untrusted server text', {}, None)


@pytest.mark.parametrize('exc,category,retryable', [
    (URLError('DNS failure'), 'dns_or_connection', True),
    (TimeoutError(), 'timeout', True),
    (socket.timeout(), 'timeout', True),
    (URLError(TimeoutError()), 'timeout', True),
    (URLError('timed out'), 'timeout', True),
    (ConnectionError(), 'dns_or_connection', True),
    (OSError('connection refused'), 'dns_or_connection', True),
    (http(429), 'http_error', True),
    (http(503), 'http_error', True),
    (http(404), 'http_error', False),
    (ValueError('empty history'), 'empty_response', False),
    (ValueError('no valid prices'), 'no_valid_prices', False),
    (RuntimeError('Traceback: untrusted server text'), 'dns_or_connection', False),
])
def test_classification(exc, category, retryable):
    actual, transient, detail = pf.classify_price_error(exc, 'yfinance')
    assert (actual, transient) == (category, retryable)
    assert detail and 'Traceback' not in detail
    assert 'untrusted server text' not in detail
    assert 'https://' not in detail


def test_retry_recovers():
    fetch = Mock(side_effect=[URLError('offline'), URLError('offline'), 'prices'])
    sleep = Mock()
    value, attempts = pf.fetch_with_retry(fetch, 'yfinance', sleep=sleep)
    assert (value, attempts) == ('prices', 3)
    assert [call.args for call in sleep.call_args_list] == [(0.5,), (1,)]


@pytest.mark.parametrize('exc,attempts', [(URLError('offline'), 3), (http(404), 1)])
def test_retry_final_failure(exc, attempts):
    fetch, sleep = Mock(side_effect=exc), Mock()
    with pytest.raises(pf.PriceFetchError) as caught:
        pf.fetch_with_retry(fetch, 'stooq', sleep=sleep)
    assert caught.value.attempts == attempts
    assert caught.value.source == 'stooq'
    assert fetch.call_count == attempts
    assert sleep.call_count == attempts - 1


def fail_providers(monkeypatch):
    ticker = Mock()
    ticker.history.side_effect = URLError('Traceback: untrusted server text')
    ticker.info = {}
    monkeypatch.setattr(pf.yf, 'Ticker', Mock(return_value=ticker))
    urlopen = Mock(side_effect=URLError('offline'))
    monkeypatch.setattr(pf.urllib.request, 'urlopen', urlopen)
    return ticker, urlopen


def fetch_symbol(tmp_path, symbol='CSCO'):
    return pf.fetch_symbol_prices(symbol, '2025-01-01', '2026-10-07',
                                 '2026-10-08', tmp_path, sleep=Mock())


def test_both_providers_fail(monkeypatch, tmp_path):
    fail_providers(monkeypatch)
    prices, statuses = fetch_symbol(tmp_path)
    assert prices is None
    assert [s['source'] for s in statuses] == ['yfinance', 'stooq']
    for status in statuses:
        assert status['status'] == 'failed'
        assert status['category'] == 'dns_or_connection'
        assert status['retryable'] is True
        assert status['attempts'] == 3


def test_international_skips_stooq(monkeypatch, tmp_path):
    _, urlopen = fail_providers(monkeypatch)
    prices, statuses = fetch_symbol(tmp_path, 'BABA.HK')
    assert prices is None
    assert statuses[-1]['category'] == 'unsupported_listing'
    assert statuses[-1]['attempts'] == 1
    assert statuses[-1]['retryable'] is False
    urlopen.assert_not_called()


@pytest.mark.parametrize('payload', [b'', b'No data', b'Date,Close\n'])
def test_empty_stooq(monkeypatch, tmp_path, payload):
    fail_providers(monkeypatch)
    monkeypatch.setattr(pf.urllib.request, 'urlopen', lambda *a, **kw: io.BytesIO(payload))
    prices, statuses = fetch_symbol(tmp_path)
    assert prices is None
    assert statuses[-1]['category'] == 'empty_response'
    assert statuses[-1]['attempts'] == 1


def test_stooq_recovers_and_writes_raw_csv(monkeypatch, tmp_path):
    fail_providers(monkeypatch)
    raw = b'Date,Close\n2026-10-06,100\n2026-10-07,101\n'
    monkeypatch.setattr(pf.urllib.request, 'urlopen', lambda *a, **kw: io.BytesIO(raw))
    prices, statuses = fetch_symbol(tmp_path)
    assert prices.iloc[-1] == 101
    assert statuses[-1]['status'] == 'ok'
    assert (tmp_path / 'CSCO-stooq.csv').read_bytes() == raw


def test_cleaning_preserves_cutoff_and_warnings():
    h = pd.DataFrame({'Close': [100, 0, -1, None, 102, 999]},
                     index=pd.date_range('2026-10-03', periods=6))
    prices, warnings = pf.clean_prices_series(h, 'CSCO', '2026-10-07')
    assert prices.tolist() == [100, 102]
    assert warnings == ['warning: CSCO invalid/missing prices skipped']


@pytest.mark.parametrize('success', [False, True])
def test_quant_pipeline(monkeypatch, tmp_path, capsys, success):
    ticker, urlopen = fail_providers(monkeypatch)
    if success:
        ticker.history.side_effect = None
        ticker.history.return_value = pd.DataFrame(
            {'Close': [100., 101.]}, index=pd.to_datetime(['2026-10-06', '2026-10-07']))
    original = pf.fetch_symbol_prices
    monkeypatch.setattr(pf, 'fetch_symbol_prices',
                        lambda *a, **kw: original(*a, **kw, sleep=Mock()))
    monkeypatch.setattr(data_utils, 'DATA', tmp_path)
    monkeypatch.setattr(data_utils, 'ticker_arg', lambda: 'CSCO')
    monkeypatch.setenv('REPORT_AS_OF', '2026-10-07')
    script = Path(__file__).resolve().parents[1] / 'scripts' / 'quant.py'
    if success:
        runpy.run_path(str(script), run_name='__main__')
    else:
        with pytest.raises(SystemExit) as caught:
            runpy.run_path(str(script), run_name='__main__')
        assert caught.value.code == 2
    result = json.loads((tmp_path / 'csco-quant.json').read_text())
    captured = capsys.readouterr()
    assert json.loads(captured.out) == result
    assert 'Traceback' not in '\n'.join(result['errors']) + captured.err
    if success:
        assert result['metrics']['Close'] == 101
        assert (tmp_path / 'CSCO-yfinance.csv').exists()
        assert len(result['price_status']) == 2
        urlopen.assert_not_called()
    else:
        assert all(value is None for value in result['metrics'].values())
        assert [(s['symbol'], s['source']) for s in result['price_status']] == [
            ('CSCO', 'yfinance'), ('CSCO', 'stooq'), ('SPY', 'yfinance'), ('SPY', 'stooq')]
        for status in result['price_status']:
            assert status['stage'] == 'price_fetch'
            assert status['status'] == 'failed'
            assert status['category'] == 'dns_or_connection'
            assert status['retryable'] is True
            assert status['attempts'] == 3
        assert 'prices-minimum-history' in captured.err
        assert 'dns_or_connection' in captured.err
