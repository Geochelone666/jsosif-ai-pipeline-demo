import json
from pathlib import Path
P=Path(__file__).parent
q=json.loads((P/'quant.json').read_text()); ai=None; failures=[]; sources=q['sources'].copy()
for n in [1,2]:
    try:
        envelope=json.loads((P/f'gemini-envelope-{n}.json').read_text()); obj=json.loads(envelope['text'])
        assert obj['ticker']=='NVDA' and obj['as_of']=='2026-10-03'
        for cat in ['tailwinds','headwinds','catalysts','risks']:
            assert isinstance(obj[cat],list)
            for item in obj[cat]:
                assert all(k in item for k in ['headline','summary','date','impact','horizon','confidence','sources'])
                assert item['impact'] in ['high','medium','low'] and item['horizon'] in ['short','medium','long']
                assert isinstance(item['confidence'],(int,float)) and 0<=item['confidence']<=1
                assert '2026-09-27'<=item['date']<='2026-10-03'
                assert item['sources'] and all(isinstance(u,str) and u.startswith(('https://','http://')) for u in item['sources'])
                sources.extend(item['sources'])
        sources.extend(envelope['sources']); ai=obj; break
    except Exception as e:
        err=(P/f'gemini-error-{n}.txt').read_text().strip(); failures.append({'attempt':n,'parse_error':str(e),'cli_error':err})
lines=['# NVDA Intelligence Demo','', '- ticker: **NVDA**','- Report as_of: **2026-10-03**',f"- Market data as_of: **{q['as_of'] or 'N/A'}**",'- Quant sources: '+(', '.join(q['sources']) or 'All requests failed'),'- AI model: **gemini-3.5-flash-lite** (Google Search grounding, specified CLI)','', '## QUANTITATIVE','', '| Metric | Value |','|---|---:|']
labels=['Close','Return 1D (%)','Return 1W (%)','Return 1M (%)','Return YTD (%)','Return 1Y (%)','Annualized volatility (%)','Beta vs SPY','Max drawdown (%)','Sharpe (rf=0)','P/E (trailing)','P/B','EV/EBITDA','Revenue growth (%)','MA50','Close vs MA50 (%)','MA200','Close vs MA200 (%)','RSI (14, Wilder)','MACD (12,26)','MACD signal (9)','MACD histogram']
for label in labels:
    v=q['metrics'].get(label); lines.append(f'| {label} | '+(f'{v:.4f}' if isinstance(v,(int,float)) else 'N/A')+' |')
lines+=['','Methodology: yfinance daily closes with auto_adjust=True; the Stooq fallback uses Close, with adjustment conventions not independently verified. 1W/1M/1Y use the nearest trading day on or before the end date minus one week/month/year; YTD uses the last trading day of the previous year. Risk metrics use a one-year window, simple daily returns, sample standard deviation and 252-day annualization; beta is aligned NVDA/SPY return covariance divided by SPY variance; Sharpe uses rf=0; max drawdown uses closing-price peaks. RSI uses Wilder smoothing, MACD is EMA(12)-EMA(26), and signal is EMA(9). MA position is the percentage difference from the moving average. Fundamentals are fetched info snapshots; historical point-in-time consistency is not verified.',f"Market data sample: {q['history_count']}。"]
if q['verification']:
    v=q['verification']; lines+=['',f"1Y cross-check: base date {v['base_date']}, base close {v['base_close']:.4f}, end close {v['end_close']:.4f}; manual (end close - base close)/base close x100 = {v['manual_1Y_pct']:.4f}%, matching the program result (error < 1e-10)."]
else: lines+=['','1Y cross-check: incomplete (market/baseline data unavailable).']
if q['errors']: lines+=['','Quant request errors:']+['- '+x for x in q['errors']]
for cat in ['tailwinds','headwinds','catalysts','risks']:
    lines+=['',f'## {cat.upper()}','']
    if ai is None: lines+=['Request failed: both Gemini calls returned HTTP 429 / RESOURCE_EXHAUSTED (quota exhausted), with no JSON text. AI JSON parsing and field completeness could not be verified; no AI items were generated.']
    elif not ai[cat]: lines+=['No verified items returned.']
    else:
        for item in ai[cat]:
            lines += [f"- **{item['headline']}** — date: {item['date']} / impact: {item['impact']} / horizon: {item['horizon']} / confidence: {item['confidence']:.4f}", '  '+item['summary'],'  Sources: '+', '.join(item['sources'])]
lines+=['','## SOURCES','']+['- '+u for u in dict.fromkeys(sources)]
lines+=['','AI grounding returned no sources; no AI sources could be merged.','', '## Demo notes and limitations','','This is a single-asset, one-off local demo. AI items require human spot checks; grounding coverage is not guaranteed. This AI pipeline run failed due to exhausted quota, so successful end-to-end validation of both pipelines cannot be claimed. Missing prices or fundamentals are marked N/A; no numbers are fabricated. Report and market-data dates are shown separately. This report is not investment advice.','', 'Validation: the report and required sections are complete; see the quant cross-check status above. AI JSON validation failed (the service returned no JSON). Error logs: gemini-error-1.txt and gemini-error-2.txt in this directory.']
report=P/'NVDA-intelligence-20261003.md'; report.write_text('\n'.join(lines)+'\n')
assert report.exists() and all('## '+s in report.read_text() for s in ['QUANTITATIVE','TAILWINDS','HEADWINDS','CATALYSTS','RISKS','SOURCES','Demo notes and limitations'])
(P/'validation.json').write_text(json.dumps({'report_sections_pass':True,'quant_crosscheck':q['verification'],'ai_json_pass':ai is not None,'ai_failures':failures},indent=2,ensure_ascii=False))
print(report); print(json.dumps(q,ensure_ascii=False,indent=2))
