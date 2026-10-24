"""Offline numerical contracts for additional, opt-in-free risk report dimensions."""
import math

import numpy as np
import pandas as pd
import pytest

from risk_extensions import compute_extended_risk, RISK_KEYS


def prices(count=260):
    t = np.arange(count, dtype=float)
    returns = .001 + .012 * np.sin(t * .37) - .008 * np.cos(t * .11)
    values = 100 * np.cumprod(1 + returns)
    return pd.Series(values, index=pd.bdate_range(end='2026-10-23', periods=count))


def test_reproducible_tail_and_downside_calculation():
    asset = prices()
    out = compute_extended_risk(asset, asset)
    r = asset.loc[asset.index >= asset.index[-1]-pd.DateOffset(years=1)].pct_change().dropna()
    downside = np.sqrt(np.mean(np.minimum(r.to_numpy(), 0) ** 2))
    threshold = np.quantile(r.to_numpy(), .05)
    assert out['Downside deviation (rf=0, %)'].value == pytest.approx(
        downside * math.sqrt(252) * 100)
    assert out['Sortino (rf=0)'].value == pytest.approx(r.mean() / downside * math.sqrt(252))
    assert out['Historical VaR 95% (1D, %)'].value == pytest.approx(max(0., -threshold * 100))
    assert out['Historical ES 95% (1D, %)'].value == pytest.approx(
        max(0., -r[r <= threshold].mean() * 100))
    assert out['Historical ES 95% (1D, %)'].value >= out['Historical VaR 95% (1D, %)'].value
    assert out['Correlation vs SPY'].value == pytest.approx(1.)
    assert out['Tracking error vs SPY (%)'].value == pytest.approx(0., abs=1e-12)
    assert set(out) == set(RISK_KEYS)


@pytest.mark.parametrize('length', [0, 1, 20, 100])
def test_explicit_sample_thresholds(length):
    out = compute_extended_risk(prices(length), None)
    assert out['Historical VaR 95% (1D, %)'].status == 'insufficient'
    assert out['Historical ES 95% (1D, %)'].status == 'insufficient'
    if length <= 20:
        assert out['Sortino (rf=0)'].status == 'insufficient'
    assert out['Correlation vs SPY'].status == 'undefined'


def test_missing_benchmark_and_invalid_prices_never_fabricate_values():
    asset = prices()
    corrupt = asset.copy()
    corrupt.iloc[2] = -10
    out = compute_extended_risk(corrupt, asset)
    assert all(v.status == 'undefined' and v.value is None for v in out.values())
    out = compute_extended_risk(asset, None)
    assert out['Tracking error vs SPY (%)'].value is None
    shifted = asset.copy()
    shifted.index = shifted.index - pd.DateOffset(years=2)
    out = compute_extended_risk(asset, shifted)
    assert out['Correlation vs SPY'].status == 'insufficient'
    assert out['Tracking error vs SPY (%)'].status == 'insufficient'


def test_zero_volatility_and_zero_downside_are_not_divided_by_zero():
    asset = pd.Series(100., index=pd.bdate_range(end='2026-10-23', periods=260))
    out = compute_extended_risk(asset, asset)
    assert out['Downside deviation (rf=0, %)'].value == 0.
    assert out['Sortino (rf=0)'].status == 'undefined'
    assert out['Historical VaR 95% (1D, %)'].value == 0.
    assert out['Historical ES 95% (1D, %)'].value == 0.
    assert out['Correlation vs SPY'].status == 'undefined'
    assert out['Tracking error vs SPY (%)'].value == 0.


def test_returns_are_calculated_before_alignment():
    asset = prices(260)
    benchmark = asset.iloc[::3] * 1.01
    out = compute_extended_risk(asset, benchmark)
    a = asset.loc[asset.index >= asset.index[-1]-pd.DateOffset(years=1)].pct_change()
    b = benchmark.pct_change()
    aligned = pd.concat([a.rename('asset'), b.rename('benchmark')], axis=1).dropna()
    assert out['Correlation vs SPY'].value == pytest.approx(aligned.asset.corr(aligned.benchmark))
    assert out['Tracking error vs SPY (%)'].value == pytest.approx(
        (aligned.asset - aligned.benchmark).std(ddof=1) * math.sqrt(252) * 100)


def test_no_network_or_external_state_and_no_input_mutation():
    asset, benchmark = prices(), prices()
    original = asset.copy(deep=True)
    out = compute_extended_risk(asset, benchmark)
    assert all(v.value is None or math.isfinite(v.value) for v in out.values())
    pd.testing.assert_series_equal(asset, original)
