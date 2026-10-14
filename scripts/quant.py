import json, sys
from datetime import date, timedelta
import pandas as pd
import yfinance as yf
from data_utils import DATA, ticker_arg, ticker_file, number, as_of_date
from price_fetch import fetch_symbol_prices, stooq_url
from assumptions import VERSION, PRICE_START, AssumptionViolation, check_all, checked_mapping
from boundaries import evaluate_metrics, available, undefined


def compute_metrics(prices: pd.Series, spy: pd.Series | None) -> dict:
    """Pure price calculation returning metric names mapped to BoundaryResult."""
    return evaluate_metrics(prices, spy)


def main():
    TICKER=ticker_arg()
    AS_OF = as_of_date().isoformat()
    END = (date.fromisoformat(AS_OF) + timedelta(days=1)).isoformat()
    P = DATA
    errors=[]; sources=[]; series={}; info={}
    stooq_symbols=[]
    price_status=[]
    price_failure_warnings=[]
    for symbol in [TICKER,'SPY']:
        prices, statuses = fetch_symbol_prices(symbol, PRICE_START, AS_OF, END, P)
        price_status.extend(statuses)
        for status in statuses:
            if status['status'] == 'failed':
                warning = (f"{symbol} {status['source']}: {status['detail']} "
                           f"after {status['attempts']} attempts ({status['category']})")
                errors.append(warning)
                price_failure_warnings.append(warning)
            elif 'warning:' in status['detail']:
                errors.append(status['detail'].split('; ', 1)[1])
        if prices is not None:
            series[symbol] = prices
            if statuses[-1]['source'] == 'yfinance':
                sources.append(f'https://finance.yahoo.com/quote/{symbol}/history/')
            else:
                sources.append(stooq_url(symbol, PRICE_START, AS_OF))
                stooq_symbols.append(symbol)

    try:
        info=yf.Ticker(TICKER).info
        sources.append(f'https://finance.yahoo.com/quote/{TICKER}/key-statistics/')
    except Exception as e: errors.append(f'info: {e}')
    (P/ticker_file(TICKER, 'info.json')).write_text(json.dumps(info,indent=2,default=str))
    result={'ticker':TICKER,'errors':errors,'sources':sources,'metrics':{},'as_of':None,'verification':None,'fetched_at':__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),'requested_as_of':AS_OF}
    result['price_status'] = price_status
    c = series.get(TICKER, pd.Series(dtype=float))
    boundaries = compute_metrics(c, series.get('SPY'))
    m = result['metrics'] = {label: item.value for label, item in boundaries.items()}
    result['metric_notes'] = {label: {'status': item.status, 'reason': item.reason}
                              for label, item in boundaries.items()
                              if item.status != 'ok' or item.reason != 'Available from valid history'}
    if len(c):
        result['as_of'] = str(c.index[-1].date())
    if len(c) < 3:
        errors.append(f'warning: {TICKER} insufficient history; unavailable metrics are N/A')
    if m['Return 1Y (%)'] is not None:
        base = c.loc[c.index <= c.index[-1]-pd.DateOffset(years=1)]
        b = float(base.iloc[-1]); last = float(c.iloc[-1]); manual = (last-b)/b*100
        assert abs(manual-m['Return 1Y (%)']) < 1e-10
        result['verification'] = {'base_date': str(base.index[-1].date()), 'base_close': b,
                                  'end_close': last, 'manual_1Y_pct': manual, 'passed': True}
    for label,key in [('P/E (trailing)','trailingPE'),('P/B','priceToBook'),('EV/EBITDA','enterpriseToEbitda'),('Revenue growth (%)','revenueGrowth')]:
        v = number(info.get(key))
        item = (undefined('fundamental value is missing or non-finite') if v is None else
                available(v*100 if key == 'revenueGrowth' else v))
        m[label] = item.value
        if item.status != 'ok':
            result['metric_notes'][label] = {'status': item.status, 'reason': item.reason}
    for key in ['marketCap', 'trailingPE', 'priceToBook', 'enterpriseToEbitda', 'revenueGrowth']:
        if number(info.get(key)) is None:
            errors.append(f'warning: {key} unavailable (N/A)')
    for label, value in m.items():
        m[label]=number(value)
        if m[label] is None:
            errors.append(f'warning: {label} unavailable (N/A)')
    result['history_count']={k:len(v) for k,v in series.items()}
    context = {'ticker': TICKER, 'as_of': AS_OF, 'price_start': PRICE_START,
               'price_count': len(series.get(TICKER, [])), 'stooq_symbols': stooq_symbols}
    if TICKER in series:
        context['price_index'] = series[TICKER].index
    violation = None
    try:
        checks = check_all(context)
    except AssumptionViolation as exc:
        checks, violation = exc.results, exc
    result['assumptions_version'] = VERSION
    result['assumptions_checked'] = checked_mapping(checks)
    (P/ticker_file(TICKER, 'quant.json')).write_text(json.dumps(result,indent=2,allow_nan=False))
    print(json.dumps(result,indent=2))
    for warning in price_failure_warnings:
        print(warning, file=sys.stderr)

    if violation is not None:
        print(str(violation), file=sys.stderr)
        raise SystemExit(2)


if __name__ == '__main__':
    main()
