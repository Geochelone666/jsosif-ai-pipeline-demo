"""Same-day scheduled earnings remain visible until actual results are reported."""
from datetime import date

import pandas as pd
import pytest

import earnings


@pytest.mark.parametrize('actual,expected_last,expected_next', [
    (None, '2026-07-20', '2026-10-20'),
    (1.25, '2026-10-20', None),
])
def test_same_day_earnings_distinguish_scheduled_and_reported(monkeypatch, actual, expected_last, expected_next):
    class Ticker:
        calendar = {'Earnings Date': [date(2026, 10, 20)]}

        def get_earnings_dates(self, limit):
            return pd.DataFrame({'Reported EPS': [1.0, actual]},
                                index=pd.to_datetime(['2026-07-20', '2026-10-20']))

    saved = {}
    monkeypatch.setattr(earnings, 'ticker_arg', lambda: 'CSCO')
    monkeypatch.setattr(earnings, 'as_of_date', lambda: date(2026, 10, 20))
    monkeypatch.setattr(earnings.yf, 'Ticker', lambda symbol: Ticker())
    monkeypatch.setattr(earnings, 'save', lambda name, data: saved.update(data))
    earnings.main()
    assert saved['last_earnings'] == expected_last
    assert saved['next_earnings'] == expected_next


def test_calendar_fallback_retains_today_without_reported_results(monkeypatch):
    class Ticker:
        calendar = {'Earnings Date': [date(2026, 10, 19), date(2026, 10, 20)]}

        def get_earnings_dates(self, limit):
            raise TimeoutError

    saved = {}
    monkeypatch.setattr(earnings, 'ticker_arg', lambda: 'CSCO')
    monkeypatch.setattr(earnings, 'as_of_date', lambda: date(2026, 10, 20))
    monkeypatch.setattr(earnings.yf, 'Ticker', lambda symbol: Ticker())
    monkeypatch.setattr(earnings, 'save', lambda name, data: saved.update(data))
    earnings.main()
    assert saved['last_earnings'] is None
    assert saved['next_earnings'] == '2026-10-20'
