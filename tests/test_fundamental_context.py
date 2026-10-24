"""Additional fundamentals are derived only from supplied vendor snapshots."""
import math

import pytest

from fundamental_context import compute_fundamental_context, FUNDAMENTAL_KEYS


def test_financial_factors_and_currency_matched_fcf_yield():
    inputs = {'forwardPE': 21.5, 'grossMargins': .45, 'operatingMargins': .22,
              'returnOnEquity': .19, 'freeCashflow': 500., 'marketCap': 10_000.,
              'currency': 'CAD', 'financialCurrency': 'CAD'}
    result = compute_fundamental_context(inputs)
    assert set(result) == set(FUNDAMENTAL_KEYS)
    assert {key: item.value for key, item in result.items()} == pytest.approx({
        'Forward P/E (estimate)': 21.5,
        'Gross margin (%)': 45.,
        'Operating margin (%)': 22.,
        'Return on equity (%)': 19.,
        'Free cash flow yield (%)': 5.,
    })


@pytest.mark.parametrize('currency,financial', [
    ('USD', 'CAD'), ('USD', None), (None, 'USD'), ('', ''),
])
def test_unverified_currency_never_exposes_misleading_cash_yield(currency, financial):
    result = compute_fundamental_context({
        'currency': currency, 'financialCurrency': financial,
        'freeCashflow': 500, 'marketCap': 10_000,
    })
    assert result['Free cash flow yield (%)'].value is None
    assert result['Free cash flow yield (%)'].status == 'undefined'


@pytest.mark.parametrize('cap,fcf', [(0, 12), (-1, 12), (None, 12), (10, math.inf),
                                     (10, True), (math.nan, 1)])
def test_cash_yield_rejects_invalid_numeric_inputs(cap, fcf):
    result = compute_fundamental_context({
        'currency': 'USD', 'financialCurrency': 'USD',
        'freeCashflow': fcf, 'marketCap': cap,
    })
    assert result['Free cash flow yield (%)'].value is None


def test_missing_values_and_nonpositive_estimated_pe_remain_unavailable():
    result = compute_fundamental_context({
        'forwardPE': -3, 'grossMargins': float('nan'), 'operatingMargins': True,
    })
    assert all(value.value is None for value in result.values())
    assert result['Forward P/E (estimate)'].status == 'undefined'
    assert all(value.reason for value in result.values())


def test_negative_cash_flow_yield_is_retained_not_turned_into_positive():
    result = compute_fundamental_context({
        'currency': 'USD', 'financialCurrency': 'USD',
        'freeCashflow': -120, 'marketCap': 1_000,
    })
    assert result['Free cash flow yield (%)'].value == pytest.approx(-12.)
