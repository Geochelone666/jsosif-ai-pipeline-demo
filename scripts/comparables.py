"""Optional configured peers; growth and return are fractions, not percentages."""
from datetime import date, timedelta
import pandas as pd
import yfinance as yf
from data_utils import number, save, ticker_arg, ticker_file, SUPPORTED, as_of_date

# Configure sector peers separately; never reuse the old technology peers.
PEERS = {
    'CNQ.TO': ['SU.TO', 'IMO.TO', 'CVE.TO'],
    'CSCO': ['ANET', 'FFIV', 'HPE'],
    'JPM': ['BAC', 'C', 'WFC'],
    'BMO.TO': ['RY.TO', 'TD.TO', 'BNS.TO'],
    'COST': ['WMT', 'TGT', 'BJ'],
    'V': ['MA', 'PYPL', 'AXP'],
    'JWEL.TO': ['HLF', 'USNA', 'NATR'],
    'VRTX': ['REGN', 'BIIB', 'AMGN'],
    'ENB': ['TRP.TO', 'KMI', 'EPD'],
    'PFE': ['MRK', 'JNJ', 'LLY'],
    'CP.TO': ['CNR.TO', 'UNP', 'NSC'],
    'ATD.TO': ['CASY', 'MUSA', 'SUN'],
    'SCHW': ['IBKR', 'HOOD', 'LPLA'],
    'ACN': ['IBM', 'CTSH', 'INFY'],
    'J': ['ACM', 'FLR', 'KBR'],
    'XYL': ['AOS', 'PH', 'DOV'],
    'PEP': ['KO', 'MNST', 'KDP'],
    'NTR.TO': ['MOS', 'CF', 'IPI'],
    'DIS': ['NFLX', 'WBD', 'PSKY'],
    'MG.TO': ['APTV', 'BWA', 'LEA'],
    'OTEX.TO': ['DSG.TO', 'CSU.TO', 'GIB'],
    'GIS': ['KHC', 'CPB', 'SJM'],
    'NVO': ['LLY', 'ROG.SW', 'SAN.PA'],
    'MC.PA': ['RMS.PA', 'CFR.SW', 'KER.PA'],
    'AMTM': ['LDOS', 'CACI', 'SAIC'],
}
PEERS.update({'SPGI': ['MCO', 'MSCI', 'FDS'],
 'MCO': ['SPGI', 'MSCI', 'FDS'],
 'TD.TO': ['RY.TO', 'BMO.TO', 'BNS.TO'],
 'GOOGL': ['META', 'MSFT', 'AMZN'],
 'AMZN': ['WMT', 'MSFT', 'GOOGL'],
 'META': ['GOOGL', 'SNAP', 'PINS'],
 'AMD': ['NVDA', 'INTC', 'AVGO'],
 'NVDA': ['AMD', 'AVGO', 'INTC'],
 'MCK': ['COR', 'CAH', 'CNC'],
 'ISRG': ['MDT', 'SYK', 'BSX'],
 'EW': ['MDT', 'BSX', 'ABT'],
 'T': ['VZ', 'TMUS', 'BCE'],
 'CAT': ['DE', 'CNH', 'CMI'],
 'MSFT': ['ORCL', 'GOOGL', 'AMZN'],
 'NFLX': ['DIS', 'WBD', 'CMCSA'],
 'SHOP.TO': ['WIX', 'CRM', 'GDDY'],
 'AAPL': ['MSFT', 'GOOGL', 'SONY'],
 'TSM': ['UMC', 'GFS', 'INTC'],
 'MU': ['WDC', 'STX', 'NXPI'],
 'CSU.TO': ['DSG.TO', 'OTEX.TO', 'TOI.V'],
 'NVAX': ['MRNA', 'BNTX', 'GSK'],
 'BRK-B': ['MKL', 'FFH.TO', 'L'],
 'TMC': ['MP', 'LAC', 'VALE'],
 'ASML': ['AMAT', 'LRCX', 'KLAC'],
 'SYY': ['USFD', 'PFGC', 'CHEF']})
FIELDS = {'pe': 'trailingPE', 'pb': 'priceToBook', 'ev_ebitda': 'enterpriseToEbitda', 'revenue_growth': 'revenueGrowth', 'mktcap': 'marketCap'}

def main():
    symbol_arg = ticker_arg()
    today = as_of_date()
    peers = []
    for symbol in PEERS[symbol_arg]:
        row = {'ticker': symbol, **dict.fromkeys(FIELDS), 'ret_1y': None, 'currency': None}
        ticker = yf.Ticker(symbol)
        try:
            info = ticker.info
            row['currency'] = info.get('currency')
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
    save(ticker_file(symbol_arg, 'comparables.json'), {'as_of': today.isoformat(), 'peers': peers})
    print(f'comparables: {len(peers)} rows, 7 fields/row')

if __name__ == '__main__':
    main()

