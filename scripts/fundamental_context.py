"""Optional valuation and profitability context from the existing yfinance info snapshot.

No additional requests; never infer currency equivalence or substitute stale data.
"""
from boundaries import available, undefined
from data_utils import number


FUNDAMENTAL_KEYS = (
    'Forward P/E (estimate)',
    'Gross margin (%)',
    'Operating margin (%)',
    'Return on equity (%)',
    'Free cash flow yield (%)',
)


def compute_fundamental_context(info: dict) -> dict:
    if not isinstance(info, dict):
        info = {}
    keys = (
        ('Forward P/E (estimate)', 'forwardPE', 1),
        ('Gross margin (%)', 'grossMargins', 100),
        ('Operating margin (%)', 'operatingMargins', 100),
        ('Return on equity (%)', 'returnOnEquity', 100),
    )
    result = {}
    for label, key, multiplier in keys:
        value = number(info.get(key))
        result[label] = (undefined('provider did not supply a finite ' + key)
                         if value is None else available(value * multiplier))
    if result['Forward P/E (estimate)'].value is not None and result['Forward P/E (estimate)'].value <= 0:
        result['Forward P/E (estimate)'] = undefined('non-positive projected earnings multiple')
    fcf = number(info.get('freeCashflow'))
    cap = number(info.get('marketCap'))
    listing = info.get('currency')
    financial = info.get('financialCurrency')
    if not (isinstance(listing, str) and listing.strip() and
            isinstance(financial, str) and financial.strip() and listing == financial):
        result[FUNDAMENTAL_KEYS[-1]] = undefined('free cash flow and market capitalization currency match is unverified')
    elif fcf is None or cap is None or cap <= 0:
        result[FUNDAMENTAL_KEYS[-1]] = undefined('finite free cash flow and positive market capitalization are required')
    else:
        result[FUNDAMENTAL_KEYS[-1]] = available(fcf / cap * 100)
    return result
