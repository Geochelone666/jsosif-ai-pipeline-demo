# V Intelligence Demo

- ticker: **V**
- Report as_of: **2026-10-08**
- Market data as_of: **2026-10-07**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-10-03** (retained; this run refreshes market data only)
- Snapshot note: the report-date daily bar may be intraday until the US market closes; its Close field is provisional. News, peers, earnings, EDGAR and macro sections reuse their existing snapshots.
- Market data fetched_at (UTC): **2026-10-08T04:12:01.257790+00:00**
- AI status: **N/A: AI unavailable: Invalid category**
- AI model: **gemini-3.5-flash-lite** (25 Google News RSS headlines -> AI extraction and classification; free-tier grounding unavailable, using RSS + AI)

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 372.1000 |
| Return 1D (%) | 0.3939 |
| Return 1W (%) | 3.5538 |
| Return 1M (%) | -0.7919 |
| Return YTD (%) | 6.7362 |
| Return 1Y (%) | 6.4287 |
| Annualized volatility (%) | 22.1321 |
| Beta vs SPY | 0.2999 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 0.3920 |
| P/E (trailing) | 31.53 |
| P/B | 19.72 |
| EV/EBITDA | 22.34 |
| Revenue growth (%) | 14.40 |
| MA50 | 369.0966 |
| Close vs MA50 (%) | 0.8137 |
| MA200 | 336.9263 |
| Close vs MA200 (%) | 10.4396 |
| RSI (14, Wilder) | 55.6707 |
| MACD (12,26) | -0.5278 |
| MACD signal (9) | -0.9249 |
| MACD histogram | 0.3972 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 255, 'SPY': 255}.

## TAILWINDS

### Why Visa (V) Stock Is Up Today
- Summary: Why Visa (V) Stock Is Up Today
- Date: 2026-07-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxPcVZrZ2RCS3d1V3RZbXRjNEhfUWxBVEJTa2RsSjR2RUpzc3Y1bVVrSDVBRHF4WTQ4VTBxX2xpdTZ5Wk9taTF6a2JObXJYN3ZhVlA0VVctZUxZSGZzSVA5aXlBdU1VczBNNURoUzNOR1h1WXBRMXNfaksxalRPRnpiTzdodU5jQ05OQTNGQXR3Mng?oc=5>

### Blue-Chip Visa Stock Just Hit a New All-Time High
- Summary: Blue-Chip Visa Stock Just Hit a New All-Time High
- Date: 2026-08-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOeWIyaHJxZVV5WXY1WWhuMFlBV1hPNFRBcUM5Z3BENV91MmNLTUpnOEFiUlQ5c0JYT1g4NWVJN0pWMmFheDhNYVdWa1A3TXhxcjZUUjloOXJaOG8zcGZuaGZRRkVmZTNGQUwyRmxNaUNSc0s3MjhXN2FXZEZfcFA0Ylp4VGt4QkxUcDZkU0VWOEY1MVdf?oc=5>

## HEADWINDS

N/A: AI unavailable: Invalid category

## CATALYSTS

### Visa Stock Heads Into October 27 Earnings With Stablecoins and AI Payments in Focus
- Summary: Visa Stock Heads Into October 27 Earnings With Stablecoins and AI Payments in Focus
- Date: 2026-09-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQWjBlb29ZcktZbTdiZ2wxbDlabEdPOUtWZGRWdHkzNlVCMmtxNUhZTUl2UVlpU19sd292bHdQdTk3enYyTW9SN1FoSi1aN0pySnBrZEtWdmg5cnF3OWo0a1pPdUVrRm1wUWNwQUVQSTI0ZWZCeUxyZ1ZMTTRuSlNoNENjQXFmenh1NllYczBQMGlHREtFc2NzVFA2ak5nRWtxTWh6Szh2UXlNMmdFSlE?oc=5>

## RISKS

N/A: AI unavailable: Invalid category

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (USD) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **V** | **31.53** | **19.72** | **22.34** | **14.40** | **698,563,887,104.00** | **6.43** |

Peers fetched as_of: 2026-10-08; V reuses existing data (market data as_of: 2026-10-07); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-28
- Next expected earnings: 2026-10-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment Rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index | CPIAUCSL | 334.13 | 2026-08-01 |
| Federal Funds Effective Rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-29
- Revenue (latest available single quarter): 5,840,000,000.00 USD; period 2019-04-01/2019-06-30; fiscal year/reporting period 2019/Q3
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/1403161/000140316126000104/v-20260630.htm

SEC requests use the demo placeholder contact email contact@example.com. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikAFBVV95cUxPcVZrZ2RCS3d1V3RZbXRjNEhfUWxBVEJTa2RsSjR2RUpzc3Y1bVVrSDVBRHF4WTQ4VTBxX2xpdTZ5Wk9taTF6a2JObXJYN3ZhVlA0VVctZUxZSGZzSVA5aXlBdU1VczBNNURoUzNOR1h1WXBRMXNfaksxalRPRnpiTzdodU5jQ05OQTNGQXR3Mng?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOeWIyaHJxZVV5WXY1WWhuMFlBV1hPNFRBcUM5Z3BENV91MmNLTUpnOEFiUlQ5c0JYT1g4NWVJN0pWMmFheDhNYVdWa1A3TXhxcjZUUjloOXJaOG8zcGZuaGZRRkVmZTNGQUwyRmxNaUNSc0s3MjhXN2FXZEZfcFA0Ylp4VGt4QkxUcDZkU0VWOEY1MVdf?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQWjBlb29ZcktZbTdiZ2wxbDlabEdPOUtWZGRWdHkzNlVCMmtxNUhZTUl2UVlpU19sd292bHdQdTk3enYyTW9SN1FoSi1aN0pySnBrZEtWdmg5cnF3OWo0a1pPdUVrRm1wUWNwQUVQSTI0ZWZCeUxyZ1ZMTTRuSlNoNENjQXFmenh1NllYczBQMGlHREtFc2NzVFA2ak5nRWtxTWh6Szh2UXlNMmdFSlE?oc=5

## Demo notes and limitations

- Multi-ticker local demo; AI items require human spot checks; RSS coverage is not guaranteed.
- Free-tier Gemini grounding (google_search tool) returned 429; the demo uses Google News RSS + plain-text AI extraction.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
