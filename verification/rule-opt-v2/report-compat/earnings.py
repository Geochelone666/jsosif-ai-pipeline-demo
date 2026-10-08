"""Past reported earnings (actual EPS present) and next scheduled date."""
from datetime import date
import pandas as pd
import yfinance as yf
from data_utils import save, ticker_arg, ticker_file

def main():
    symbol = ticker_arg()
    today = date.today()
    data = {'ticker': symbol, 'last_earnings': None, 'next_earnings': None, 'source': 'yfinance'}
    ticker = yf.Ticker(symbol)
    try:
        dates = ticker.get_earnings_dates(limit=12)
        past, future = [], []
        if dates is not None:
            for stamp, row in dates.iterrows():
                day = stamp.date()
                if day <= today and pd.notna(row.get('Reported EPS')):
                    past.append(day)
                elif day > today:
                    future.append(day)
        data['last_earnings'] = max(past).isoformat() if past else None
        data['next_earnings'] = min(future).isoformat() if future else None
    except Exception as exc:
        print(f'earnings_dates unavailable: {type(exc).__name__}')
    if data['next_earnings'] is None:
        try:
            calendar = ticker.calendar
            upcoming = calendar.get('Earnings Date', []) if isinstance(calendar, dict) else []
            future = [pd.Timestamp(value).date() for value in upcoming if pd.Timestamp(value).date() > today]
            data['next_earnings'] = min(future).isoformat() if future else None
        except Exception as exc:
            print(f'calendar unavailable: {type(exc).__name__}')
    save(ticker_file(symbol, 'earnings.json'), data)
    print(f'earnings: {sum(data[k] is not None for k in ("last_earnings", "next_earnings"))}/2 date fields')

if __name__ == '__main__':
    main()
