"""Additional historical price-risk dimensions, calculated without extra provider calls.

These describe observed adjusted-close returns, not forecasts, portfolio FX-adjusted
returns, or investment recommendations. All statistics use the trailing calendar year.
"""
import math

import numpy as np
import pandas as pd

from boundaries import available, undefined, insufficient, invalid_series


RISK_KEYS = (
    'Downside deviation (rf=0, %)',
    'Sortino (rf=0)',
    'Historical VaR 95% (1D, %)',
    'Historical ES 95% (1D, %)',
    'Correlation vs SPY',
    'Tracking error vs SPY (%)',
)


def compute_extended_risk(prices: pd.Series, spy: pd.Series | None) -> dict:
    """Return bounded, explicitly unavailable risk metrics on valid price histories."""
    invalid = invalid_series(prices)
    if invalid:
        return {key: undefined(invalid) for key in RISK_KEYS}
    result = {key: insufficient(21, 'daily closes in the trailing year')
              for key in RISK_KEYS[:2]}
    result.update({key: insufficient(101, 'daily closes in the trailing year')
                   for key in RISK_KEYS[2:4]})
    for key in RISK_KEYS[4:]:
        result[key] = undefined('SPY prices are missing')
    if prices.empty:
        return result
    end = prices.index[-1]
    window = prices.loc[prices.index >= end - pd.DateOffset(years=1)]
    with np.errstate(over='ignore', invalid='ignore', divide='ignore'):
        returns = window.pct_change().dropna()
        if len(returns) >= 20:
            negative = np.minimum(returns.to_numpy(dtype=float), 0)
            downside = float(np.sqrt(np.mean(negative ** 2)))
            result[RISK_KEYS[0]] = available(downside * math.sqrt(252) * 100)
            result[RISK_KEYS[1]] = (undefined('zero downside deviation') if downside == 0
                                    else available(float(returns.mean()) / downside * math.sqrt(252)))
        if len(returns) >= 100:
            lower = float(np.quantile(returns.to_numpy(dtype=float), 0.05))
            tail = returns[returns <= lower]
            result[RISK_KEYS[2]] = available(max(0., -lower * 100))
            result[RISK_KEYS[3]] = available(max(0., -float(tail.mean()) * 100))
        if spy is None or spy.empty:
            return result
        invalid_benchmark = invalid_series(spy)
        if invalid_benchmark:
            for key in RISK_KEYS[4:]:
                result[key] = undefined('SPY ' + invalid_benchmark)
            return result
        joined = pd.concat([returns.rename('asset'), spy.pct_change().rename('benchmark')],
                           axis=1, sort=True).dropna()
        for key in RISK_KEYS[4:]:
            result[key] = insufficient(20, 'of date-aligned daily return pairs')
        if len(joined) >= 20:
            asset_std = float(joined.asset.std(ddof=1))
            spy_std = float(joined.benchmark.std(ddof=1))
            result[RISK_KEYS[4]] = (undefined('zero asset or SPY variance')
                                    if asset_std == 0 or spy_std == 0
                                    else available(float(joined.asset.corr(joined.benchmark))))
            result[RISK_KEYS[5]] = available(float(
                (joined.asset - joined.benchmark).std(ddof=1)) * math.sqrt(252) * 100)
    return result
