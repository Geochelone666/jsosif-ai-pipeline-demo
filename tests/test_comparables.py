"""Offline coverage for the peer comparables collector."""
from pathlib import Path
import json
import sys

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import comparables
import data_utils


class FakeTicker:
    def __init__(self, symbol, info, history):
        self.symbol, self._info, self._history = symbol, info, history

    @property
    def info(self):
        if isinstance(self._info, Exception):
            raise self._info
        return self._info

    def history(self, **kwargs):
        if isinstance(self._history, Exception):
            raise self._history
        return self._history


def closes(values, end='2026-10-08', tz='America/New_York'):
    index = pd.bdate_range(end=end, periods=len(values), tz=tz)
    return pd.DataFrame({'Close': values}, index=index)


@pytest.fixture
def run(tmp_path, monkeypatch):
    monkeypatch.setattr(data_utils, 'DATA', tmp_path)
    monkeypatch.setattr(comparables, 'ticker_arg', lambda: 'CSCO')
    monkeypatch.setenv('REPORT_AS_OF', '2026-10-08')

    def execute(tickers):
        monkeypatch.setattr(comparables.yf, 'Ticker', lambda symbol: tickers[symbol])
        comparables.main()
        result = json.loads((tmp_path / 'csco-comparables.json').read_text(encoding='utf-8'))
        return result['as_of'], {row['ticker']: row for row in result['peers']}
    return execute


def test_metrics_and_one_year_return(run):
    year = closes([60.0] * 271)
    # Closes on or before the one-year boundary (2025-10-08) are the baseline.
    year.loc[year.index.tz_localize(None) <= '2025-10-08', 'Close'] = 50.0
    as_of, rows = run({
        'ANET': FakeTicker('ANET', {'currency': 'USD', 'trailingPE': 40.5, 'priceToBook': 'n/a',
                                    'enterpriseToEbitda': float('inf'), 'revenueGrowth': 0.2,
                                    'marketCap': 10**11}, year),
        'FFIV': FakeTicker('FFIV', RuntimeError('rate limited'), closes([10.0, 11.0])),
        'HPE': FakeTicker('HPE', {}, RuntimeError('no history')),
    })
    assert as_of == '2026-10-08' and list(rows) == comparables.PEERS['CSCO']
    anet = rows['ANET']
    assert anet['currency'] == 'USD' and anet['pe'] == 40.5 and anet['mktcap'] == 10**11
    assert anet['pb'] is None and anet['ev_ebitda'] is None  # nonnumeric/infinite rejected
    assert anet['ret_1y'] == pytest.approx(0.2)
    # Less than a year of history: no baseline, so the return stays unknown.
    assert rows['FFIV']['ret_1y'] is None and rows['FFIV']['pe'] is None
    assert all(rows['HPE'][key] is None for key in ('pe', 'ret_1y', 'currency'))


def test_prices_after_as_of_are_ignored(run):
    history = closes([100.0] + [100.0] * 268 + [200.0], end='2026-10-09')
    _, rows = run({symbol: FakeTicker(symbol, {}, history) for symbol in comparables.PEERS['CSCO']})
    # 2026-10-09 is after REPORT_AS_OF, so the 200 close must not be used.
    assert rows['ANET']['ret_1y'] == pytest.approx(0.0)
