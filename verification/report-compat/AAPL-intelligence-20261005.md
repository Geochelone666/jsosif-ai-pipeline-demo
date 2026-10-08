# AAPL Intelligence Demo

- ticker: **AAPL**
- Report as_of: **2026-10-05**
- Market data as_of: **2026-10-05**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-10-03** (retained; this run refreshes market data only)
- Snapshot note: the report-date daily bar may be intraday until the US market closes; its Close field is provisional. News, peers, earnings, EDGAR and macro sections reuse their existing snapshots.
- Market data fetched_at (UTC): **2026-10-05T16:09:07.410271+00:00**
- AI status: **Available**
- AI model: **gemini-3.5-flash-lite** (25 Google News RSS headlines -> AI extraction and classification; free-tier grounding unavailable, using RSS + AI)

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 333.4238 |
| Return 1D (%) | -0.0798 |
| Return 1W (%) | -1.4705 |
| Return 1M (%) | 4.2047 |
| Return YTD (%) | 22.9792 |
| Return 1Y (%) | 29.7014 |
| Annualized volatility (%) | 24.7290 |
| Beta vs SPY | 0.6875 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.2054 |
| P/E (trailing) | 38.24 |
| P/B | 45.30 |
| EV/EBITDA | 29.12 |
| Revenue growth (%) | 16.40 |
| MA50 | 322.3690 |
| Close vs MA50 (%) | 3.4292 |
| MA200 | 289.0968 |
| Close vs MA200 (%) | 15.3329 |
| RSI (14, Wilder) | 54.4249 |
| MACD (12,26) | 3.5387 |
| MACD signal (9) | 4.5788 |
| MACD histogram | -1.0401 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 253, 'SPY': 253}.

## TAILWINDS

No items in this run

## HEADWINDS

### Apple Stock Falls After Bank of America Flags a New AI Threat
- Summary: Apple Stock Falls After Bank of America Flags a New AI Threat
- Date: 2026-09-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNUGNCTUI0eXd0cFdSSFYydG1BeVJqOFZUX2tpNDJUai1OSEQtYklRMURfZWo5a2lzeklSbFBwY3l5ellreERyWnk3TE9EMjk3RGtVcWp1NlhLQ3dMNGxEZ29TR3k3dURkQndrOWFoZDZETVhvbjlueXQxM2lPWF9XMnprdkgyZUl2cFlPdVRMbWdTcURVcUlWYzlQNA?oc=5>

### Morgan Stanley lowers Apple stock price target on limited upside
- Summary: Morgan Stanley lowers Apple stock price target on limited upside
- Date: 2026-10-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOQ2xXaF9wblpEb1VEYWlJUFNvZmEwNXJ1cl9qeVkzbzdpZmd5QzZmczlmMWhicjNlSzZ5Vjk0MUgyWUp4dFhzNkRrWTBRX0lpSVVUTWJtNW5KMzN0RmhRQTB0ekFGZVZCSVFLYXZlN1Z0VFpmbDdySHZaaVNSYXFqMmdPWDB5VVl1dUtKVHZncFlYVWlUa3FRdkRCcjlGMFkyak1ybVptdnlkeHBpMjZxX2tOZjZtMVZ0LVlGQTNkY2JxQQ?oc=5>

## CATALYSTS

### Apple Predicted To Sell 6 Million iPhone Duo Handsets This Year
- Summary: Apple Predicted To Sell 6 Million iPhone Duo Handsets This Year
- Date: 2026-09-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOU0VaNmd2U0tkNXlzazM5Y2dxSXBfajRBT2JwYnNacklBN1ZnRU1EbXp3ZDNsUm1WcVM2MlBkTm02WDhoNW80MWFLVDV2WGtWOWZIcTRaRW5uQmJHM0VhbkNiUFJ2dU1rdjdVc054dzlYYnQzQ0xzc1k2dlY3LWVJVHpic2tsVGhScUVabGotdlUyell1?oc=5>

### Jim Cramer urges buying Apple stock before foldable iPhone launch
- Summary: Jim Cramer urges buying Apple stock before foldable iPhone launch
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMickFVX3lxTE9LTThYTXNidkVveHltcS1DTTlueDhva2pPWHdmVUFKal9OWmtzYzlZbWNOeWtYUjRZM1oxaVJacGlPSTJvY0Z1elBZSlhTZzl1S1l6bUlibnFXNFNCZWY3NkdHcURWZTRKUGM2NC1ad1Z4dw?oc=5>

### Apple Chief Executive John Ternus Weighs Major Corporate Overhaul and Product Release Shift
- Summary: Apple Chief Executive John Ternus Weighs Major Corporate Overhaul and Product Release Shift
- Date: 2026-10-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOUHVNS19lOVZENVVHOGFJRUJteFJRRnBzUktaNnlNTjJjWG5pT2hvVnFPTXhLN3JxY1daaWZmWWtfb21uZFJSLWFGLUJ4ZG41ZHBwRWppUDJYeU11ei1uZmRkbWJENHFRLVNPRnZXVXM5V2w1cjhJRjNxX2dldmN1LTlBNFRhRDEzNGFzdFdPRjZDS0U?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (USD) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **38.24** | **45.30** | **29.12** | **16.40** | **4,865,918,500,864.00** | **29.70** |
| MSFT | 28.83 | 8.69 | 20.05 | 17.70 | 3,842,942,959,616.00 | 1.17 |
| GOOGL | 17.24 | 6.75 | 23.66 | 24.20 | 4,200,982,642,688.00 | 40.17 |
| AMZN | 20.23 | 4.92 | 16.82 | 19.60 | 2,712,973,606,912.00 | 13.09 |
| NVDA | 29.58 | 24.67 | 27.90 | 105.90 | 5,649,190,617,088.00 | 24.15 |

Peers fetched as_of: 2026-10-05; AAPL reuses existing data (market data as_of: 2026-10-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-30
- Next expected earnings: 2026-10-29 (yfinance; expected dates may change)

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
- Revenue (latest available single quarter): 62,900,000,000.00 USD; period 2018-07-01/2018-09-29; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 29,789,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/320193/000032019326000020/aapl-20260627.htm

SEC requests use the demo placeholder contact email contact@example.com. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxNUGNCTUI0eXd0cFdSSFYydG1BeVJqOFZUX2tpNDJUai1OSEQtYklRMURfZWo5a2lzeklSbFBwY3l5ellreERyWnk3TE9EMjk3RGtVcWp1NlhLQ3dMNGxEZ29TR3k3dURkQndrOWFoZDZETVhvbjlueXQxM2lPWF9XMnprdkgyZUl2cFlPdVRMbWdTcURVcUlWYzlQNA?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOQ2xXaF9wblpEb1VEYWlJUFNvZmEwNXJ1cl9qeVkzbzdpZmd5QzZmczlmMWhicjNlSzZ5Vjk0MUgyWUp4dFhzNkRrWTBRX0lpSVVUTWJtNW5KMzN0RmhRQTB0ekFGZVZCSVFLYXZlN1Z0VFpmbDdySHZaaVNSYXFqMmdPWDB5VVl1dUtKVHZncFlYVWlUa3FRdkRCcjlGMFkyak1ybVptdnlkeHBpMjZxX2tOZjZtMVZ0LVlGQTNkY2JxQQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOU0VaNmd2U0tkNXlzazM5Y2dxSXBfajRBT2JwYnNacklBN1ZnRU1EbXp3ZDNsUm1WcVM2MlBkTm02WDhoNW80MWFLVDV2WGtWOWZIcTRaRW5uQmJHM0VhbkNiUFJ2dU1rdjdVc054dzlYYnQzQ0xzc1k2dlY3LWVJVHpic2tsVGhScUVabGotdlUyell1?oc=5
- https://news.google.com/rss/articles/CBMickFVX3lxTE9LTThYTXNidkVveHltcS1DTTlueDhva2pPWHdmVUFKal9OWmtzYzlZbWNOeWtYUjRZM1oxaVJacGlPSTJvY0Z1elBZSlhTZzl1S1l6bUlibnFXNFNCZWY3NkdHcURWZTRKUGM2NC1ad1Z4dw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOUHVNS19lOVZENVVHOGFJRUJteFJRRnBzUktaNnlNTjJjWG5pT2hvVnFPTXhLN3JxY1daaWZmWWtfb21uZFJSLWFGLUJ4ZG41ZHBwRWppUDJYeU11ei1uZmRkbWJENHFRLVNPRnZXVXM5V2w1cjhJRjNxX2dldmN1LTlBNFRhRDEzNGFzdFdPRjZDS0U?oc=5

## Demo notes and limitations

- Multi-ticker local demo; AI items require human spot checks; RSS coverage is not guaranteed.
- Free-tier Gemini grounding (google_search tool) returned 429; the demo uses Google News RSS + plain-text AI extraction.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
