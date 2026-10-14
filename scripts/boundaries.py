"""Explicit contracts for price metrics; no I/O or implicit input cleaning.

Prices must be positive finite numbers on unique, increasing, naive midnight
DatetimeIndex dates. Invalid series are rejected as undefined, never dropped.
Risk metrics use the trailing calendar year and require three closes (two returns).
Beta computes each series' returns first, then intersects return end dates with
at least two pairs; gaps may represent different holding periods (no resampling).
Returns require two closes and a base on/before the calendar target; 1D uses the
previous observation. YTD targets December 31 of the latest close's prior year.
RSI seeds 14 changes (15 closes). MACD retains first-close-seeded adjust=False
EMAs, but exposes its line at 26 closes and signal/histogram at 26+9-1=34 closes.
These are explicit availability policies, not claims of EMA convergence.
"""
from dataclasses import dataclass
import math
from typing import Literal

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class BoundaryResult:
    value: float | None
    status: Literal['ok', 'undefined', 'insufficient']
    reason: str

    def __post_init__(self):
        if self.status not in {'ok', 'undefined', 'insufficient'}:
            raise ValueError('Unknown boundary status')
        if not self.reason:
            raise ValueError('A readable boundary reason is required')
        if self.status == 'ok':
            if self.value is None or not math.isfinite(self.value):
                raise ValueError('An available boundary value must be finite')
        elif self.value is not None:
            raise ValueError('An unavailable boundary value must be None')


def available(value, reason='Available from valid history'):
    value = float(value)
    if not math.isfinite(value):
        return undefined('calculation produced a non-finite value')
    return BoundaryResult(value, 'ok', reason)


def undefined(reason):
    return BoundaryResult(None, 'undefined', f'undefined: {reason}')


def insufficient(count, context=''):
    suffix = f' {context}' if context else ''
    return BoundaryResult(None, 'insufficient',
                          f'insufficient history: need >={count} points{suffix}')


PRICE_METRICS = (
    'Close', 'Return 1D (%)', 'Return 1W (%)', 'Return 1M (%)',
    'Return YTD (%)', 'Return 1Y (%)', 'Annualized volatility (%)',
    'Max drawdown (%)', 'Sharpe (rf=0)', 'Beta vs SPY', 'MA50',
    'Close vs MA50 (%)', 'MA200', 'Close vs MA200 (%)',
    'RSI (14, Wilder)', 'MACD (12,26)', 'MACD signal (9)', 'MACD histogram',
)


def invalid_series(prices):
    if not isinstance(prices, pd.Series):
        return 'prices must be a pandas Series'
    if prices.empty:
        return None
    if (not isinstance(prices.index, pd.DatetimeIndex)
            or prices.index.hasnans or prices.index.tz is not None
            or not prices.index.is_unique or not prices.index.is_monotonic_increasing
            or not prices.index.equals(prices.index.normalize())):
        return 'price dates must be unique, increasing, naive midnight dates'
    for value in prices:
        if (isinstance(value, (bool, str)) or not isinstance(value, (int, float, np.number))
                or np.iscomplexobj(value)):
            return 'prices must be positive finite numbers; invalid input rejected'
        if not math.isfinite(value) or value <= 0:
            return 'prices must be positive finite numbers; invalid input rejected'
    return None


def evaluate_metrics(prices: pd.Series, spy: pd.Series | None) -> dict:
    """Return a BoundaryResult for every price metric without mutating inputs."""
    invalid = invalid_series(prices)
    if invalid:
        return {key: undefined(invalid) for key in PRICE_METRICS}
    # Overflow is converted to an explicit undefined result, never exported.
    with np.errstate(over='ignore', invalid='ignore', divide='ignore'):
        return _evaluate(prices, spy)


def _evaluate(c, spy):
    m = {key: insufficient(1) for key in PRICE_METRICS}
    if len(c):
        last = float(c.iloc[-1])
        end = c.index[-1]
        m['Close'] = available(last)
    for period in ('1D', '1W', '1M', 'YTD', '1Y'):
        label = f'Return {period} (%)'
        m[label] = insufficient(2)
        if len(c) < 2:
            continue
        target = {'1D': c.index[-2], '1W': end-pd.Timedelta(days=7),
                  '1M': end-pd.DateOffset(months=1),
                  'YTD': pd.Timestamp(year=end.year-1, month=12, day=31),
                  '1Y': end-pd.DateOffset(years=1)}[period]
        base = c.loc[c.index <= target]
        m[label] = (available(100*(last/float(base.iloc[-1])-1)) if len(base)
                    else BoundaryResult(None, 'insufficient',
                                        f'insufficient history: no starting price on or before {target.date()}'))
    window = c.loc[c.index >= end-pd.DateOffset(years=1)] if len(c) else c
    r = window.pct_change().dropna()
    risk = ('Annualized volatility (%)', 'Max drawdown (%)', 'Sharpe (rf=0)')
    for key in risk:
        m[key] = insufficient(3, 'in the trailing calendar year')
    if len(r) >= 2:
        std = r.std(ddof=1)
        m[risk[0]] = available(std*np.sqrt(252)*100,
                               'Zero means constant returns' if std == 0 else 'Available from valid history')
        drawdown = float((window/window.cummax()-1).min()*100)
        m[risk[1]] = available(drawdown, 'No decline from a running peak; drawdown is 0.0'
                               if drawdown == 0 else 'Available from valid history')
        m[risk[2]] = (undefined('zero volatility') if std == 0
                      else available(r.mean()/std*np.sqrt(252)))
    m['Beta vs SPY'] = undefined('SPY prices are missing')
    if spy is not None:
        invalid = invalid_series(spy)
        if invalid:
            m['Beta vs SPY'] = undefined(f'SPY {invalid}')
        elif spy.empty:
            m['Beta vs SPY'] = undefined('SPY prices are missing')
        else:
            joined = pd.concat([r.rename('asset'), spy.pct_change().rename('benchmark')],
                               axis=1, sort=True).dropna()
            m['Beta vs SPY'] = insufficient(2, 'of date-aligned returns')
            if len(joined) >= 2:
                variance = joined.benchmark.var(ddof=1)
                m['Beta vs SPY'] = (undefined('zero SPY variance') if variance == 0 else
                                    available(joined.asset.cov(joined.benchmark)/variance))
    for n in (50, 200):
        m[f'MA{n}'] = m[f'Close vs MA{n} (%)'] = insufficient(n)
        if len(c) >= n:
            ma = c.rolling(n).mean().iloc[-1]
            m[f'MA{n}'] = available(ma)
            m[f'Close vs MA{n} (%)'] = available((last/ma-1)*100)
    m['RSI (14, Wilder)'] = insufficient(15, 'for 14 changes of Wilder warmup')
    if len(c) >= 15:
        delta = c.diff()
        def wilder(s):
            out = pd.Series(np.nan, index=s.index)
            out.iloc[14] = s.iloc[1:15].mean()
            for i in range(15, len(s)):
                out.iloc[i] = (out.iloc[i-1]*13+s.iloc[i])/14
            return out.iloc[-1]
        g, loss = wilder(delta.clip(lower=0)), wilder(-delta.clip(upper=0))
        if loss == 0:
            m['RSI (14, Wilder)'] = (undefined('no gains or losses') if g == 0 else
                                    available(100.0, 'No losses with positive gains; RSI is 100'))
        else:
            m['RSI (14, Wilder)'] = available(100-100/(1+g/loss),
                                                     'No gains with positive losses; RSI is 0'
                                                     if g == 0 else 'Available from valid history')
    macd_keys = ('MACD (12,26)', 'MACD signal (9)', 'MACD histogram')
    for key, count in zip(macd_keys, (26, 34, 34)):
        m[key] = insufficient(count, 'for MACD warmup')
    if len(c) >= 26:
        macd = c.ewm(span=12, adjust=False).mean()-c.ewm(span=26, adjust=False).mean()
        signal = macd.ewm(span=9, adjust=False).mean()
        m[macd_keys[0]] = available(macd.iloc[-1])
        if len(c) >= 34:
            m[macd_keys[1]] = available(signal.iloc[-1])
            m[macd_keys[2]] = available((macd-signal).iloc[-1])
    return m
