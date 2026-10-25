"""Fairness and fail-fast quota behavior without live data or network."""
from datetime import date

from ticker_priority import fair_order


def test_least_recently_ready_goes_first():
    date_str = '2026-10-25'
    symbols = ['V', 'ACN', 'MSFT', 'AAPL']
    reports = [
        {'ticker': 'V', 'quality': 'ready', 'as_of': '2026-10-24'},
        {'ticker': 'MSFT', 'quality': 'ready', 'as_of': '2026-10-23'},
        {'ticker': 'AAPL', 'quality': 'degraded', 'as_of': '2026-10-24'},
        {'ticker': 'ACN', 'quality': 'ready', 'as_of': '2026-10-21'},
    ]
    result = fair_order(symbols, reports, date_str)
    assert result == ['AAPL', 'ACN', 'MSFT', 'V']
    assert sorted(result) == sorted(symbols)


def test_same_readiness_cohort_rotates_by_business_date():
    symbols = ['AAPL', 'MSFT', 'V', 'ACN', 'TSM']
    first = fair_order(symbols, [], '2026-10-25')
    second = fair_order(symbols, [], '2026-10-26')
    assert first != second
    assert set(first) == set(second) == set(symbols)
    assert fair_order(list(reversed(symbols)), [], '2026-10-25') == first


def test_future_and_degraded_reports_never_inflate_readiness():
    reports = [
        {'ticker': 'V', 'quality': 'ready', 'as_of': '2026-11-10'},
        {'ticker': 'V', 'quality': 'degraded', 'as_of': '2026-10-24'},
        {'ticker': 'AAPL', 'quality': 'ready', 'as_of': '2026-10-24'},
    ]
    assert fair_order(['V', 'AAPL'], reports, '2026-10-25')[0] == 'V'


def test_empty_and_duplicate_inputs_are_explicit():
    assert fair_order([], [], '2026-10-25') == []
    import pytest
    with pytest.raises(ValueError, match='unique'):
        fair_order(['V', 'V'], [], '2026-10-25')
