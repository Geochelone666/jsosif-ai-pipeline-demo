# ENB Intelligence Demo

- ticker: **ENB**
- Report as_of: **2026-10-08**
- Market data as_of: **2026-10-07**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-10-03** (retained; this run refreshes market data only)
- Snapshot note: the report-date daily bar may be intraday until the US market closes; its Close field is provisional. News, peers, earnings, EDGAR and macro sections reuse their existing snapshots.
- Market data fetched_at (UTC): **2026-10-08T04:13:01.025654+00:00**
- AI status: **N/A: AI unavailable: Invalid category**
- AI model: **gemini-3.5-flash-lite** (25 Google News RSS headlines -> AI extraction and classification; free-tier grounding unavailable, using RSS + AI)

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 45.8900 |
| Return 1D (%) | -1.3967 |
| Return 1W (%) | -1.2906 |
| Return 1M (%) | -8.3849 |
| Return YTD (%) | -0.1784 |
| Return 1Y (%) | -3.4486 |
| Annualized volatility (%) | 17.8033 |
| Beta vs SPY | -0.1241 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | -0.1092 |
| P/E (trailing) | 24.54 |
| P/B | 2.43 |
| EV/EBITDA | 12.78 |
| Revenue growth (%) | 97.10 |
| MA50 | 49.5902 |
| Close vs MA50 (%) | -7.4615 |
| MA200 | 51.1157 |
| Close vs MA200 (%) | -10.2233 |
| RSI (14, Wilder) | 29.2335 |
| MACD (12,26) | -1.0893 |
| MACD signal (9) | -1.0644 |
| MACD histogram | -0.0249 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 255, 'SPY': 255}.

## TAILWINDS

### Enbridge (ENB) Stock Dips While Market Gains: Key Facts
- Summary: Enbridge (ENB) Stock Dips While Market Gains: Key Facts
- Date: 2026-06-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQWkNoS2x3WlkyRHJ3TVhDallrU1I1NDhubGl2TWctdmlHVlItd0o5alJydENZeWJIUHlpMjFKcUpWekNqWHdtQU4tSDk3cmtCZTU2NmFRNWp1Y3ZsRG0zeEpsejhQYUZyVUtneDd0YnpDb0h3SmgyWDdERzZwNXMzVS1iYkttbnltWnE0SjZSZEVlTlNvbVNoVWVn?oc=5>

## HEADWINDS

N/A: AI unavailable: Invalid category

## CATALYSTS

### Enbridge (ENB) Q2 Earnings and Revenues Surpass Estimates
- Summary: Enbridge (ENB) Q2 Earnings and Revenues Surpass Estimates
- Date: 2026-07-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNZFQybXpXVVRrYUVuS2dyNWVuUmxZMU1TRUhZY0tvN2xZWVlwU2ZENDV3Z1lJdm4xSmZZMW5HXzQtX0F5d2NxLWw0RTNUeGJEdUhWeXJ1blZYcURVTUdPMVJva2ZtOV9NNDNXOExGdU5zWXFkbko0M2pnQnFwYWtxY0xJSVdMczIwUExaeGJCcl9qdHhKZ3FKZ0ZROS1lekE?oc=5>

### Analysts Estimate Enbridge (ENB) to Report a Decline in Earnings: What to Look Out for
- Summary: Analysts Estimate Enbridge (ENB) to Report a Decline in Earnings: What to Look Out for
- Date: 2026-07-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPSlpmaThOdHBhaklSSzlOWWtSaTF2aTRDNDE1QzlZMzZjanpxVVJUY210dVcwdlpWbWhadW5lQi15MzdVTFVEUDA0UHdMN05veHQzTUNnV3JseUZDUXpkLVhPTmx2aXFhN0x4UGNYU2wyeUJoZDJhNTdNcVNjZHFmS1RQY0lIVlJWOU1ybXF0RGVwd3RpS1hhYzNjQWtFOV9pMm56Zg?oc=5>

## RISKS

N/A: AI unavailable: Invalid category

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (USD) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **24.54** | **2.43** | **12.78** | **97.10** | **102,281,625,600.00** | **-3.45** |

Peers fetched as_of: 2026-10-08; ENB reuses existing data (market data as_of: 2026-10-07); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-31
- Next expected earnings: 2026-11-06 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment Rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index | CPIAUCSL | 334.13 | 2026-08-01 |
| Federal Funds Effective Rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-31
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/895728/000119312526326752/enb-20260630.htm

SEC requests use the demo placeholder contact email contact@example.com. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxQWkNoS2x3WlkyRHJ3TVhDallrU1I1NDhubGl2TWctdmlHVlItd0o5alJydENZeWJIUHlpMjFKcUpWekNqWHdtQU4tSDk3cmtCZTU2NmFRNWp1Y3ZsRG0zeEpsejhQYUZyVUtneDd0YnpDb0h3SmgyWDdERzZwNXMzVS1iYkttbnltWnE0SjZSZEVlTlNvbVNoVWVn?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNZFQybXpXVVRrYUVuS2dyNWVuUmxZMU1TRUhZY0tvN2xZWVlwU2ZENDV3Z1lJdm4xSmZZMW5HXzQtX0F5d2NxLWw0RTNUeGJEdUhWeXJ1blZYcURVTUdPMVJva2ZtOV9NNDNXOExGdU5zWXFkbko0M2pnQnFwYWtxY0xJSVdMczIwUExaeGJCcl9qdHhKZ3FKZ0ZROS1lekE?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPSlpmaThOdHBhaklSSzlOWWtSaTF2aTRDNDE1QzlZMzZjanpxVVJUY210dVcwdlpWbWhadW5lQi15MzdVTFVEUDA0UHdMN05veHQzTUNnV3JseUZDUXpkLVhPTmx2aXFhN0x4UGNYU2wyeUJoZDJhNTdNcVNjZHFmS1RQY0lIVlJWOU1ybXF0RGVwd3RpS1hhYzNjQWtFOV9pMm56Zg?oc=5

## Demo notes and limitations

- Multi-ticker local demo; AI items require human spot checks; RSS coverage is not guaranteed.
- Free-tier Gemini grounding (google_search tool) returned 429; the demo uses Google News RSS + plain-text AI extraction.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
