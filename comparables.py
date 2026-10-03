"""Four fixed peers; growth and return are fractions, not percentages."""
from datetime import date, timedelta
import pandas as pd
import yfinance as yf
from data_utils import number, save

PEERS = ('AMD', 'AVGO', 'MSFT', 'TSM')
FIELDS = {'pe': 'trailingPE', 'pb': 'priceToBook', 'ev_ebitda': 'enterpriseToEbitda', 'revenue_growth': 'revenueGrowth', 'mktcap': 'marketCap'}

def main():
    today = date.today()
    peers = []
    for symbol in PEERS:
        row = {'ticker': symbol, **dict.fromkeys(FIELDS), 'ret_1y': None}
        ticker = yf.Ticker(symbol)
        try:
            info = ticker.info
            row.update({key: number(info.get(field)) for key, field in FIELDS.items()})
        except Exception as exc:
            print(f'{symbol} info unavailable: {type(exc).__name__}')
        try:
            # Extra days include the preceding trading day at the 1Y boundary.
            history = ticker.history(start=today - timedelta(days=380), end=today + timedelta(days=1), auto_adjust=True, timeout=30)
            close = history['Close'].dropna().sort_index()
            close.index = pd.to_datetime(close.index).tz_localize(None).normalize()
            close = close.loc[:str(today)]
            if len(close) > 1:
                baseline = close.loc[close.index <= close.index[-1] - pd.DateOffset(years=1)]
                if len(baseline) and baseline.iloc[-1] > 0:
                    row['ret_1y'] = number(close.iloc[-1] / baseline.iloc[-1] - 1)
        except Exception as exc:
            print(f'{symbol} history unavailable: {type(exc).__name__}')
        peers.append(row)
        print(f'{symbol}: {sum(row[k] is not None for k in (*FIELDS, "ret_1y"))}/6 numeric fields', flush=True)
    save('comparables.json', {'as_of': today.isoformat(), 'peers': peers})
    print(f'comparables: {len(peers)} rows, 7 fields/row')

if __name__ == '__main__':
    main()
