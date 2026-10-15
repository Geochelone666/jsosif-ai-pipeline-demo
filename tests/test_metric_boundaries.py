"""Offline boundary contracts and pre-change numerical regression."""
import importlib
import json
from pathlib import Path
import sys
from unittest.mock import Mock

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from boundaries import BoundaryResult, PRICE_METRICS
from quant import compute_metrics


def history(count, constant=False):
    steps = np.arange(count)
    return pd.Series(np.full(count, 100.) if constant else 100+steps*.1+np.sin(steps),
                     index=pd.bdate_range(end='2026-10-07', periods=count))


def test_import_does_not_fetch(monkeypatch):
    import quant
    fetch = Mock(side_effect=AssertionError('network disabled'))
    monkeypatch.setattr(quant.yf, 'Ticker', fetch)
    monkeypatch.setattr(quant, 'fetch_symbol_prices', fetch)
    importlib.reload(quant)
    fetch.assert_not_called()


def test_constant_history():
    result = compute_metrics(history(250, True), history(250, True))
    assert result['Sharpe (rf=0)'] == BoundaryResult(None, 'undefined', 'undefined: zero volatility')
    assert result['Beta vs SPY'].reason == 'undefined: zero SPY variance'
    assert result['Annualized volatility (%)'].value == 0.0
    assert result['Max drawdown (%)'].value == 0.0
    assert result['RSI (14, Wilder)'].reason == 'undefined: no gains or losses'
    json.dumps({key: item.value for key, item in result.items()}, allow_nan=False)


@pytest.mark.parametrize('key,minimum', [
    ('MA50', 50), ('Close vs MA50 (%)', 50),
    ('MA200', 200), ('Close vs MA200 (%)', 200),
    ('RSI (14, Wilder)', 15), ('MACD (12,26)', 26),
    ('MACD signal (9)', 34), ('MACD histogram', 34),
    ('Annualized volatility (%)', 3), ('Max drawdown (%)', 3), ('Sharpe (rf=0)', 3),
    ('Close', 1), ('Return 1D (%)', 2),
])
def test_minimum_history(key, minimum):
    # Wilder seeds 14 changes; MACD policy is 26 and 26+9-1 closes.
    # The remaining counts are rolling window sizes or sample-variance requirements.
    below = compute_metrics(history(minimum-1), None)[key]
    assert below.status == 'insufficient'
    assert below.value is None
    assert f'need >={minimum} points' in below.reason
    assert compute_metrics(history(minimum), None)[key].status == 'ok'


@pytest.mark.parametrize('bad', [np.nan, np.inf, -np.inf, 0., -1., 'bad', True])
def test_invalid_prices_rejected_without_mutation(bad):
    prices = history(220).astype(object)
    prices.iloc[20] = bad
    original = prices.copy(deep=True)
    result = compute_metrics(prices, history(220))
    assert set(result) == set(PRICE_METRICS)
    assert all(item.status == 'undefined' and item.value is None for item in result.values())
    assert all('invalid input rejected' in item.reason for item in result.values())
    pd.testing.assert_series_equal(prices, original)


@pytest.mark.parametrize('kind', ['duplicate', 'unordered', 'missing', 'timezone', 'intraday'])
def test_invalid_dates(kind):
    c = history(30)
    if kind == 'duplicate':
        c.index = pd.DatetimeIndex([c.index[0]]*len(c))
    elif kind == 'unordered':
        c = c.iloc[::-1]
    elif kind == 'missing':
        c.index = pd.DatetimeIndex([pd.NaT]*len(c))
    elif kind == 'timezone':
        c.index = c.index.tz_localize('UTC')
    else:
        c.index += pd.Timedelta(hours=1)
    assert all(item.status == 'undefined' for item in compute_metrics(c, None).values())


def test_beta_missing_invalid_and_unaligned():
    prices = history(60)
    for spy in (None, history(0)):
        result = compute_metrics(prices, spy)
        assert result['Beta vs SPY'].reason == 'undefined: SPY prices are missing'
        assert result['MA50'].status == 'ok'
    spy = history(60)
    spy.iloc[0] = np.nan
    assert compute_metrics(prices, spy)['Beta vs SPY'].status == 'undefined'
    spy = history(60)
    spy.index -= pd.DateOffset(years=2)
    assert compute_metrics(prices, spy)['Beta vs SPY'].status == 'insufficient'


def test_beta_intersects_return_dates_after_independent_returns():
    c = history(60)
    spy = c.iloc[::2] ** 1.1
    aligned = pd.concat([c.pct_change().rename('a'), spy.pct_change().rename('b')], axis=1).dropna()
    expected = aligned.a.cov(aligned.b)/aligned.b.var(ddof=1)
    assert compute_metrics(c, spy)['Beta vs SPY'].value == expected
    assert compute_metrics(c, spy.iloc[-2:])['Beta vs SPY'].status == 'insufficient'
    assert compute_metrics(c, spy.iloc[-3:])['Beta vs SPY'].status == 'ok'
    assert compute_metrics(c, c)['Beta vs SPY'].value == c.pct_change().dropna().cov(c.pct_change().dropna())/c.pct_change().dropna().var(ddof=1)


@pytest.mark.parametrize('period,offset', [('1W', pd.Timedelta(days=7)),
                                         ('1M', pd.DateOffset(months=1)),
                                         ('1Y', pd.DateOffset(years=1))])
def test_calendar_returns_need_starting_price(period, offset):
    end = pd.Timestamp('2026-10-07')
    target = end-offset
    c = pd.Series([100., 110.], index=[target+pd.Timedelta(days=1), end])
    label = f'Return {period} (%)'
    assert compute_metrics(c, None)[label].status == 'insufficient'
    assert 'no starting price' in compute_metrics(c, None)[label].reason
    c.index = pd.DatetimeIndex([target-pd.Timedelta(days=1), end])
    assert compute_metrics(c, None)[label].value == 100*(110/100-1)
    assert compute_metrics(c.iloc[-1:], None)[label].status == 'insufficient'


@pytest.mark.parametrize('year', [2025, 2026, 2027])
def test_ytd_uses_previous_year_end(year):
    c = pd.Series([80., 100., 110.], index=pd.to_datetime(
        [f'{year-1}-06-01', f'{year-1}-12-31', f'{year}-06-01']))
    assert compute_metrics(c, None)['Return YTD (%)'].value == 100*(110/100-1)
    c.index = pd.to_datetime([f'{year}-01-01', f'{year}-02-01', f'{year}-06-01'])
    assert compute_metrics(c, None)['Return YTD (%)'].status == 'insufficient'


@pytest.mark.parametrize('direction,rsi', [(1, 100.), (-1, 0.)])
def test_monotone_prices(direction, rsi):
    c = history(40)
    c[:] = 100+direction*np.arange(len(c))
    result = compute_metrics(c, None)
    # Pure gains/losses give the RSI endpoints algebraically; no 30/70 bands change.
    assert result['RSI (14, Wilder)'].value == rsi
    if direction == 1:
        assert result['Max drawdown (%)'].value == 0.0
        assert 'No decline' in result['Max drawdown (%)'].reason


def test_risk_window_needs_three_recent_closes():
    c = pd.Series([100., 101., 102.], index=pd.to_datetime(['2024-01-01', '2026-01-01', '2026-01-02']))
    assert compute_metrics(c, None)['Sharpe (rf=0)'].status == 'insufficient'


def test_extreme_finite_inputs_never_export_nonfinite_values():
    c = history(220)
    c.iloc[::2] = 1e-300
    c.iloc[1::2] = 1e300
    result = compute_metrics(c, c)
    assert any(item.status == 'undefined' for item in result.values())
    assert all(item.value is None or np.isfinite(item.value) for item in result.values())


def test_normal_history_exact_pre_change_regression():
    # Captured offline from 121c37b before editing, using these same 400 closes.
    # Keep the original hex fixtures; allow rounding differences across NumPy/pandas builds.
    expected = {
        'Close': '0x1.17c3b89f709c6p+7', 'Return 1D (%)': '-0x1.10de2e5bca1d8p-1',
        'Return 1W (%)': '0x1.0b6956143ad10p+0', 'Return 1M (%)': '0x1.9408012a9211cp+0',
        'Return YTD (%)': '0x1.187b7c6f302c0p+4', 'Return 1Y (%)': '0x1.72a8cfc4c7574p+4',
        'Annualized volatility (%)': '0x1.11e73f8ba64a2p+3',
        'Max drawdown (%)': '-0x1.75bb59dc139dap+0', 'Sharpe (rf=0)': '0x1.326b9bd0bc16cp+1',
        'Beta vs SPY': '-0x1.564beb5f1c30dp-10', 'MA50': '0x1.12e81ca2e788fp+7',
        'Close vs MA50 (%)': '0x1.c46004b260b80p+0', 'MA200': '0x1.03e8be5e97be8p+7',
        'Close vs MA200 (%)': '0x1.e8eb2e15f38d1p+2', 'RSI (14, Wilder)': '0x1.cd65c6f24e784p+5',
        'MACD (12,26)': '0x1.8950ec9c2c000p-1', 'MACD signal (9)': '0x1.710a637479049p-1',
        'MACD histogram': '0x1.8468927b2fb70p-5',
    }
    c = history(400)
    spy = pd.Series(100+np.arange(400)*.2+np.cos(np.arange(400)), index=c.index)
    before_c, before_spy = c.copy(), spy.copy()
    result = compute_metrics(c, spy)
    assert {key: item.value for key, item in result.items()} == pytest.approx(
        {key: float.fromhex(value) for key, value in expected.items()},
        rel=1e-12, abs=1e-12,
    )
    assert all(item.status == 'ok' for item in result.values())
    pd.testing.assert_series_equal(c, before_c)
    pd.testing.assert_series_equal(spy, before_spy)


@pytest.mark.parametrize('count', [0, 5, 40])
def test_json_notes_and_existing_failure_contract(monkeypatch, tmp_path, capsys, count):
    import quant
    from metric_interpretation import build_interpretation_section
    c = history(count, constant=True)
    monkeypatch.setattr(quant, 'DATA', tmp_path)
    monkeypatch.setattr(quant, 'ticker_arg', lambda: 'CSCO')
    monkeypatch.setenv('REPORT_AS_OF', '2026-10-07')
    monkeypatch.setattr(quant, 'fetch_symbol_prices', lambda *args: (
        c if count else None,
        [{'source': 'yfinance', 'status': 'ok', 'detail': 'Valid prices'}] if count else []))
    monkeypatch.setattr(quant.yf, 'Ticker', lambda *args: Mock(info={}))
    if count:
        quant.main()
    else:
        with pytest.raises(SystemExit) as caught:
            quant.main()
        assert caught.value.code == 2
    saved = json.loads((tmp_path / 'csco-quant.json').read_text())
    assert json.loads(capsys.readouterr().out) == saved
    assert 'price_status' in saved and 'assumptions_version' in saved
    assert 'assumptions_checked' in saved
    for label, value in saved['metrics'].items():
        if value is None:
            note = saved['metric_notes'][label]
            assert note['status'] in {'undefined', 'insufficient'}
            assert note['reason'] and note['reason'].isascii()
            assert 'Traceback' not in note['reason'] and '://' not in note['reason']
    if count:
        assert saved['metric_notes']['MA200']['status'] == 'insufficient'
        assert saved['metric_notes']['Max drawdown (%)']['status'] == 'ok'
        assert '0.0' in saved['metric_notes']['Max drawdown (%)']['reason']
        assert saved['metric_notes']['Sharpe (rf=0)']['status'] == 'undefined'
    section = build_interpretation_section(saved['metrics'])
    assert '**Sharpe (rf=0)**' not in section
    assert '**RSI (14, Wilder)**' not in section
