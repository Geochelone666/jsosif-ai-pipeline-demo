import json, io, urllib.request, os
from datetime import date, timedelta
from pathlib import Path
import pandas as pd
import numpy as np
import yfinance as yf
from data_utils import DATA, ticker_arg, ticker_file, number
TICKER=ticker_arg()
AS_OF = os.environ.get('REPORT_AS_OF', date.today().isoformat())
END = (date.fromisoformat(AS_OF) + timedelta(days=1)).isoformat()
P = DATA
errors=[]; sources=[]; series={}; info={}
def clean_prices(h, symbol):
    c=h['Close'].loc[:AS_OF].map(number)
    valid=c.notna() & (c>0)
    if not valid.all():
        errors.append(f'warning: {symbol} invalid/missing prices skipped')
    c=c.loc[valid].astype(float)
    if c.empty: raise ValueError('no valid prices')
    return c

for symbol in [TICKER,'SPY']:
    try:
        h=yf.Ticker(symbol).history(start='2025-10-02',end=END,auto_adjust=True,timeout=30)
        if h.empty: raise ValueError('empty history')
        h.index=pd.to_datetime(h.index).tz_localize(None).normalize()
        series[symbol]=clean_prices(h, symbol)
        sources.append(f'https://finance.yahoo.com/quote/{symbol}/history/')
        h.to_csv(P/f'{symbol}-yfinance.csv')
    except Exception as e:
        errors.append(f'{symbol} yfinance: {e}')
        try:
            if '.' in symbol:
                raise ValueError('US Stooq fallback unavailable for international listing')
            url=f'https://stooq.com/q/d/l/?s={symbol.lower()}.us&i=d&d1=20251002&d2={AS_OF.replace('-', '')}'
            raw=urllib.request.urlopen(url,timeout=30).read().decode()
            (P/f'{symbol}-stooq.csv').write_text(raw)
            h=pd.read_csv(io.StringIO(raw),parse_dates=['Date']).set_index('Date').sort_index()
            series[symbol]=clean_prices(h, symbol); sources.append(url)
            if series[symbol].empty: raise ValueError('empty stooq')
        except Exception as e: errors.append(f'{symbol} stooq: {e}')
try:
    info=yf.Ticker(TICKER).info
    sources.append(f'https://finance.yahoo.com/quote/{TICKER}/key-statistics/')
except Exception as e: errors.append(f'info: {e}')
(P/ticker_file(TICKER, 'info.json')).write_text(json.dumps(info,indent=2,default=str))
result={'ticker':TICKER,'errors':errors,'sources':sources,'metrics':{},'as_of':None,'verification':None,'fetched_at':__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),'requested_as_of':AS_OF}
m=result['metrics']
for label in ['Close', 'Return 1D (%)', 'Return 1W (%)', 'Return 1M (%)',
              'Return YTD (%)', 'Return 1Y (%)', 'Annualized volatility (%)',
              'Max drawdown (%)', 'Sharpe (rf=0)', 'Beta vs SPY', 'MA50',
              'Close vs MA50 (%)', 'MA200', 'Close vs MA200 (%)',
              'RSI (14, Wilder)', 'MACD (12,26)', 'MACD signal (9)', 'MACD histogram']:
    m[label]=None
if TICKER in series and len(series[TICKER]):
    m['Close']=float(series[TICKER].iloc[-1])
    result['as_of']=str(series[TICKER].index[-1].date())
if len(series.get(TICKER, []))<3:
    errors.append(f'warning: {TICKER} insufficient history; unavailable metrics are N/A')
if TICKER in series and len(series[TICKER])>1:
    c=series[TICKER]; end=c.index[-1]; result['as_of']=str(end.date()); last=float(c.iloc[-1]); m['Close']=last
    def ret(label,target):
        base=c.loc[c.index<=target]
        if len(base): m[label]=100*(last/float(base.iloc[-1])-1)
    ret('Return 1D (%)',c.index[-2]); ret('Return 1W (%)',end-pd.Timedelta(days=7)); ret('Return 1M (%)',end-pd.DateOffset(months=1)); ret('Return YTD (%)',pd.Timestamp('2025-12-31')); ret('Return 1Y (%)',end-pd.DateOffset(years=1))
    window=c.loc[c.index>=end-pd.DateOffset(years=1)]; r=window.pct_change().dropna()
    if len(r)>=2:
        std=r.std(ddof=1)
        m['Annualized volatility (%)']=float(std*np.sqrt(252)*100)
        m['Max drawdown (%)']=float((window/window.cummax()-1).min()*100)
        if std>0: m['Sharpe (rf=0)']=float(r.mean()/std*np.sqrt(252))
    if 'SPY' in series:
        joined=pd.concat([r.rename(TICKER),series['SPY'].pct_change().rename('SPY')],axis=1,sort=True).dropna()
        if len(joined)>=2 and joined.SPY.var(ddof=1)>0:
            m['Beta vs SPY']=float(joined[TICKER].cov(joined.SPY)/joined.SPY.var(ddof=1))
    for n in [50,200]:
        ma=c.rolling(n).mean().iloc[-1]; m[f'MA{n}']=float(ma); m[f'Close vs MA{n} (%)']=float((last/ma-1)*100)
    delta=c.diff(); gain=delta.clip(lower=0); loss=-delta.clip(upper=0)
    def wilder(s):
        out=pd.Series(np.nan,index=s.index)
        if len(s)<15: return out
        out.iloc[14]=s.iloc[1:15].mean()
        for i in range(15,len(s)): out.iloc[i]=(out.iloc[i-1]*13+s.iloc[i])/14
        return out
    g,l=wilder(gain).iloc[-1],wilder(loss).iloc[-1]; m['RSI (14, Wilder)']=float(100-100/(1+g/l)) if l else 100.0
    macd=c.ewm(span=12,adjust=False).mean()-c.ewm(span=26,adjust=False).mean(); signal=macd.ewm(span=9,adjust=False).mean()
    m['MACD (12,26)']=float(macd.iloc[-1]); m['MACD signal (9)']=float(signal.iloc[-1]); m['MACD histogram']=float((macd-signal).iloc[-1])
    base=c.loc[c.index<=end-pd.DateOffset(years=1)]
    if len(base):
        b=float(base.iloc[-1]); manual=(last-b)/b*100; assert abs(manual-m['Return 1Y (%)'])<1e-10
        result['verification']={'base_date':str(base.index[-1].date()),'base_close':b,'end_close':last,'manual_1Y_pct':manual,'passed':True}
for label,key in [('P/E (trailing)','trailingPE'),('P/B','priceToBook'),('EV/EBITDA','enterpriseToEbitda'),('Revenue growth (%)','revenueGrowth')]:
    v=number(info.get(key)); m[label]=v*100 if v is not None and key=='revenueGrowth' else v
for key in ['marketCap', 'trailingPE', 'priceToBook', 'enterpriseToEbitda', 'revenueGrowth']:
    if number(info.get(key)) is None:
        errors.append(f'warning: {key} unavailable (N/A)')
for label, value in m.items():
    m[label]=number(value)
    if m[label] is None:
        errors.append(f'warning: {label} unavailable (N/A)')
result['history_count']={k:len(v) for k,v in series.items()}
(P/ticker_file(TICKER, 'quant.json')).write_text(json.dumps(result,indent=2,allow_nan=False))
print(json.dumps(result,indent=2))
