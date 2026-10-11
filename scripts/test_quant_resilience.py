"""Run the real Quant script against offline, deliberately incomplete inputs."""
import io
import json
import runpy
from pathlib import Path
from unittest.mock import Mock

import numpy as np
import pandas as pd
import pytest
import yfinance as yf

import data_utils


SCRIPT = Path(__file__).with_name('quant.py')
INFO = {'marketCap': 1000000, 'trailingPE': 20, 'priceToBook': 3,
        'enterpriseToEbitda': 10, 'revenueGrowth': 0.1}
RISK_METRICS = ['Annualized volatility (%)', 'Sharpe (rf=0)', 'Max drawdown (%)']


def history(count=280):
    dates = pd.bdate_range(end='2026-10-07', periods=count)
    return pd.DataFrame({'Close': 100 + np.arange(count) * 0.1
                         + np.sin(np.arange(count))}, index=dates)


@pytest.fixture
def run_pipeline(monkeypatch, tmp_path, capsys):
    def run(prices=None, info=None, benchmark=None, stooq=False):
        prices = history() if prices is None else prices
        benchmark = history() if benchmark is None else benchmark
        monkeypatch.setattr(data_utils, 'DATA', tmp_path)
        monkeypatch.setattr(data_utils, 'ticker_arg', lambda: 'CSCO')
        monkeypatch.setenv('REPORT_AS_OF', '2026-10-07')
        tickers = {}
        for symbol, frame in [('CSCO', prices), ('SPY', benchmark)]:
            ticker = Mock()
            ticker.history.return_value = frame.copy()
            ticker.info = dict(INFO if info is None else info)
            tickers[symbol] = ticker
        if stooq:
            tickers['CSCO'].history.side_effect = RuntimeError('mock Yahoo unavailable')
        monkeypatch.setattr(yf, 'Ticker', lambda symbol: tickers[symbol])
        # Block every real fallback request; allow only a supplied Stooq fixture.
        def urlopen(url, timeout):
            if stooq and 'csco.us' in url:
                return io.BytesIO(prices.rename_axis('Date').to_csv().encode())
            raise AssertionError('network disabled in resilience tests')
        monkeypatch.setattr('urllib.request.urlopen', urlopen)
        runpy.run_path(str(SCRIPT), run_name='__main__')
        def reject_nonfinite(value):
            pytest.fail(f'nonstandard JSON number: {value}')
        output = json.loads(capsys.readouterr().out, parse_constant=reject_nonfinite)
        saved = json.loads((tmp_path / 'csco-quant.json').read_text(),
                           parse_constant=reject_nonfinite)
        assert output == saved
        assert (tmp_path / 'csco-info.json').exists()
        return saved
    return run


@pytest.mark.parametrize('position', ['middle', 'tail', 'all'])
@pytest.mark.parametrize('stooq', [False, True], ids=['yfinance', 'stooq'])
def test_nan_prices_finish_with_warning(run_pipeline, position, stooq):
    prices = history()
    indices = {'middle': prices.index[100:103], 'tail': prices.index[-3:],
               'all': prices.index}[position]
    prices.loc[indices, 'Close'] = np.nan
    result = run_pipeline(prices=prices, stooq=stooq)
    assert any('invalid/missing prices skipped' in error for error in result['errors'])
    if position == 'all':
        assert result['metrics']['Close'] is None
        assert any('N/A' in error for error in result['errors'])
    else:
        valid = prices['Close'].dropna()
        assert result['history_count']['CSCO'] == len(valid)
        assert result['metrics']['Close'] == pytest.approx(valid.iloc[-1])
        assert result['metrics']['Annualized volatility (%)'] is not None


@pytest.mark.parametrize('info', [{}, {'marketCap': 1000000},
                                {'trailingPE': 20, 'revenueGrowth': 0.1}])
def test_missing_fundamentals_finish_with_na(run_pipeline, info):
    result = run_pipeline(info=info)
    for label, key in [('P/E (trailing)', 'trailingPE'), ('P/B', 'priceToBook'),
                       ('EV/EBITDA', 'enterpriseToEbitda'),
                       ('Revenue growth (%)', 'revenueGrowth')]:
        if key not in info:
            assert result['metrics'][label] is None
            assert any(key in error and 'N/A' in error for error in result['errors'])
    if 'marketCap' not in info:
        assert any('marketCap' in error and 'N/A' in error for error in result['errors'])
    assert result['metrics']['Close'] is not None


@pytest.mark.parametrize('count', [1, 2])
def test_short_history_finishes_with_na(run_pipeline, count):
    result = run_pipeline(prices=history(count))
    assert result['history_count']['CSCO'] == count
    assert result['metrics']['Close'] is not None
    for metric in RISK_METRICS + ['RSI (14, Wilder)', 'MA50', 'MA200', 'Beta vs SPY']:
        assert result['metrics'][metric] is None
        assert any(metric in error and 'N/A' in error for error in result['errors'])
    assert any('insufficient history' in error for error in result['errors'])


@pytest.mark.parametrize('count', [1, 2])
def test_short_benchmark_finishes_with_na_beta(run_pipeline, count):
    result = run_pipeline(benchmark=history(count))
    assert result['metrics']['Beta vs SPY'] is None
    assert any('Beta vs SPY' in error and 'N/A' in error for error in result['errors'])
    assert result['metrics']['Annualized volatility (%)'] is not None


def test_complete_history_preserves_available_metrics(run_pipeline):
    result = run_pipeline()
    assert all(value is not None for value in result['metrics'].values())
    assert result['errors'] == []
