"""Deterministic fairness for limited-budget daily research.

Priority is based only on *verified ready* history and a transparent daily
rotation, not on financial performance, news sentiment or member identity.
"""
from datetime import date


def fair_order(tickers, reports, business_date):
    """Give long-unserved symbols first access to finite AI budget.

    Preserve the same ticker set. The rotating tie-break prevents alphabetical
    starvation for tickers with the same last-ready date.
    """
    if len(set(tickers)) != len(tickers):
        raise ValueError('Ticker ordering requires unique symbols')
    day = date.fromisoformat(business_date)
    alphabetic = sorted(tickers)
    if not alphabetic:
        return []
    shift = (day.toordinal() * 17) % len(alphabetic)
    rotated = alphabetic[shift:] + alphabetic[:shift]
    tie = {symbol: i for i, symbol in enumerate(rotated)}
    last_ready = {symbol: '' for symbol in alphabetic}
    for report in reports:
        symbol = report.get('ticker')
        if (symbol in last_ready and report.get('quality') == 'ready'
                and isinstance(report.get('as_of'), str)
                and report['as_of'] < business_date
                and report['as_of'] > last_ready[symbol]):
            last_ready[symbol] = report['as_of']
    return sorted(alphabetic, key=lambda symbol: (last_ready[symbol], tie[symbol]))
