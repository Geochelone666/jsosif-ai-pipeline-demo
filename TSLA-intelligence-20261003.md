# TSLA Intelligence Demo

- ticker: **TSLA**
- Report as_of: **2026-10-03**
- Market data as_of: **2026-10-02**
- Quant sources: https://finance.yahoo.com/quote/TSLA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSLA/key-statistics/
- AI status: **Available**
- AI model: **gemini-3.5-flash-lite** (25 Google News RSS headlines -> AI extraction and classification; free-tier grounding unavailable, using RSS + AI)

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 370.5900 |
| Return 1D (%) | 4.6539 |
| Return 1W (%) | -0.4085 |
| Return 1M (%) | 3.8038 |
| Return YTD (%) | -17.5954 |
| Return 1Y (%) | -15.0023 |
| Annualized volatility (%) | 45.8767 |
| Beta vs SPY | 2.2231 |
| Max drawdown (%) | -39.1035 |
| Sharpe (rf=0) | -0.1251 |
| P/E (trailing) | 333.86 |
| P/B | 16.85 |
| EV/EBITDA | 133.60 |
| Revenue growth (%) | 25.50 |
| MA50 | 347.5838 |
| Close vs MA50 (%) | 6.6189 |
| MA200 | 393.1821 |
| Close vs MA200 (%) | -5.7460 |
| RSI (14, Wilder) | 54.9916 |
| MACD (12,26) | 1.8335 |
| MACD signal (9) | 3.3320 |
| MACD histogram | -1.4985 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSLA': 252, 'SPY': 252}.

## TAILWINDS

### Tesla stock jumps 5% on better-than-expected vehicle deliveries report
- Summary: The headline reports a 5% stock gain following better-than-expected vehicle deliveries.
- Date: 2026-10-02 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPLTV2TThXeklJVmVnSl9pMDYzQnNoaWVielg0ekwyYTJVemhmRDdKdlpaekRVYXdTcndZNGRyelluczN1MUIxQ3J6M2FDWTQ4dnQwd3c1OEVURkdBUGdQLTBXaE1iUWxXOGFUVlZOLWdscVp0UkFTSEpsWkM3QTRDT3pMdkFlME41OHRn0gGQAUFVX3lxTFBoR1hCMDN2NU1mQ1ZJdFg3XzBQYWJSMzZmQk5aVnlBTTg5YnBfUi1KMm9seGMydVVOU2p1WnloTVVUV25QRXdYT1hwQ1Y4ODlvc0RBcUhwOG9VWUh3OG9CSnJ6N2ZuQUlBUjdWT0xPTnFaN3JHOTdjMk8tZnpWamkwOF9FaHNSUnZHQ1ZpQWkwZQ?oc=5>

### TSLA Stock Cools Overnight After Miami Robotaxi Rally — But Morgan Stanley Sees 30,000-Vehicle Fleet By 2030
- Summary: Long-term bullish sentiment is supported by firm projections from analysts like Morgan Stanley forecasting significant robotaxi fleet expansion over the decade.
- Date: 2026-10-02 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPRXBDR09mbWJCLWdwUUhpQkhKaTB6aHNBdXpueXQxNkdqMmUyc05NLU5BcDFaei12dms2QXdjTW9lamc2T29saHFSRDZ3ZVFSZEw0ZUpLNmhETkNZY0k5d0dmcUVPaURENkRleG9YbVh4V3RXOVpLOGE5TVRBTGs0X2tOOFVxcjZXRjFHdUthei1qdHRNX200ZHFhLWtXeVp4WXFHZmxMQ3E2ODkxYmJmOTlB?oc=5>

## HEADWINDS

### TSLA Stock Sinks Toward Worst Week This Year After Weak Q2 — But CEO Elon Musk Is A 'Big Fan' Of His Insightful Retail Investor Army
- Summary: The headline links a difficult week for Tesla shares to weak Q2 results.
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNVV9KRmdKX0xCWE81Vk03OC1sZnJoaFE3dW1yNW56T3NvU1BKTi1yQ1h1b0NTZWgzazV4Q3ZNTHJCZGlfRnBDZ1FnYXRHaXFtOUxNd1RQVDIxSlJlSmhNMGlTM21Wc0pvWWd5d0R5ZlptbUw3OWVjOGwxR01JZExNRkhOY21SdXFPbmpDeUZHLTVLdThDX0VxQlRrVFhBb2pXc1N2Wll3aFJVblFMNE5WX0txekgyUXZLeXc?oc=5>

### TSLA Stock On Track For Worst Week In A Year On Fresh Roadster Delay As Musk’s April Promise Fades
- Summary: Delays regarding the new Roadster model weighed on investor sentiment, offsetting some near-term enthusiasm.
- Date: 2026-10-02 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxOTXpzV2drdVRITXRXaFBEdGsxdFdTR2FSazBFMDJKWUJ4MF8tWWNZQnEwT2tpYXh5cmFEOUZGemN2dUV0ZTFjbjZHNDdXZ005bXV6UlVkVzNJc05Yc0t0Ri0ySzBCOXItVTI5eGZUTFRMTm10RXlLMkhFZWpnbjNvSkVoSnN0V09XaV9ucVNfeWdLWkIzQXNHWDJBZXRsNktwcl80bE40a3g2aS1ibEZwMEJodmlqYTd4UmFGdldSNTdOeElValkwWjU4YWpWNnY0YnQ4VzE1aHRzaTJIMUZqX29CaktiQUxYU2NyZFdoWQ?oc=5>

## CATALYSTS

### Tesla stock rises as company reports Q3 deliveries that top analyst estimates
- Summary: The headline reports that Q3 deliveries exceeded analyst estimates and shares rose.
- Date: 2026-10-02 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxNaFYteC1YV2FWTDNpU1g1cDZxR1RtNkZPNFY5Vi1oMUFrZWZnZ0wxZ0k2alRJbEV6bVI2amZqcmlnc2VUVDktdXBqYTJjV2JfWEJXSVlGT3NzWmpfd3JrdTA1X3RWbXNoRDFuc2stanZsdC0tQVprSnA2dVVsLTdFc1Q3c2RnWUdQZXNmQmk2eEJYVDcwQVpIcWZzVl9zVGIzX1Q4SWd3elpCbTBKc0FxZGo5Y3I4ZDFyb25XdDEzcjRVSHlrclRKNnBWRE52UDJTNjJSbmQ1QXQ?oc=5>

## RISKS

### TSLA Stock Extends Tumble Overnight: Munster Sees Capex Blowing Past Street Estimates Next Year Too
- Summary: Rising capital expenditures anticipated for future quarters could pressure free cash flows and increase funding execution risks.
- Date: 2026-10-01 | Impact: medium | Horizon: medium | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPRkx0eEM2aTdZcWZEeFdZRDJJVTFWWHgyWndzMTRTTlBsZ3kydXlUbDRaX3VCamRkUndoNV9YNWRvbjZSTzR5VzAxQS1uekNOX1B0RUl1TkJ4eU9UMkxrdDZVaGNKZ2k4cDdERTNMeXZzWVlESzhSZklVZWh6LVhIaWU4a1pmT3ppcHc3MHJDU2o2TWhNU3hOeUtWQ0t4dmlMS0gwc1M0V012Q2FWQkNKQVVVRQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (USD) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSLA** | **333.86** | **16.85** | **133.60** | **25.50** | **1,463,662,804,992.00** | **-15.00** |
| F | N/A | 1.35 | 24.79 | -3.80 | 48,249,909,248.00 | 3.63 |
| GM | 35.42 | 1.11 | 10.59 | 1.90 | 70,791,413,760.00 | 32.99 |
| RIVN | N/A | 3.81 | -7.65 | 27.20 | 20,704,407,552.00 | 5.69 |
| LCID | N/A | -1.54 | -2.07 | 56.20 | 1,627,509,888.00 | -82.86 |

Peers fetched as_of: 2026-10-03; TSLA reuses existing data (market data as_of: 2026-10-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-22
- Next expected earnings: 2026-10-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment Rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index | CPIAUCSL | 334.13 | 2026-08-01 |
| Federal Funds Effective Rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-23
- Revenue (latest available single quarter): 28,236,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 1,114,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1318605/000162828026049270/tsla-20260630.htm

SEC requests use the demo placeholder contact email contact@example.com. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPLTV2TThXeklJVmVnSl9pMDYzQnNoaWVielg0ekwyYTJVemhmRDdKdlpaekRVYXdTcndZNGRyelluczN1MUIxQ3J6M2FDWTQ4dnQwd3c1OEVURkdBUGdQLTBXaE1iUWxXOGFUVlZOLWdscVp0UkFTSEpsWkM3QTRDT3pMdkFlME41OHRn0gGQAUFVX3lxTFBoR1hCMDN2NU1mQ1ZJdFg3XzBQYWJSMzZmQk5aVnlBTTg5YnBfUi1KMm9seGMydVVOU2p1WnloTVVUV25QRXdYT1hwQ1Y4ODlvc0RBcUhwOG9VWUh3OG9CSnJ6N2ZuQUlBUjdWT0xPTnFaN3JHOTdjMk8tZnpWamkwOF9FaHNSUnZHQ1ZpQWkwZQ?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPRXBDR09mbWJCLWdwUUhpQkhKaTB6aHNBdXpueXQxNkdqMmUyc05NLU5BcDFaei12dms2QXdjTW9lamc2T29saHFSRDZ3ZVFSZEw0ZUpLNmhETkNZY0k5d0dmcUVPaURENkRleG9YbVh4V3RXOVpLOGE5TVRBTGs0X2tOOFVxcjZXRjFHdUthei1qdHRNX200ZHFhLWtXeVp4WXFHZmxMQ3E2ODkxYmJmOTlB?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNVV9KRmdKX0xCWE81Vk03OC1sZnJoaFE3dW1yNW56T3NvU1BKTi1yQ1h1b0NTZWgzazV4Q3ZNTHJCZGlfRnBDZ1FnYXRHaXFtOUxNd1RQVDIxSlJlSmhNMGlTM21Wc0pvWWd5d0R5ZlptbUw3OWVjOGwxR01JZExNRkhOY21SdXFPbmpDeUZHLTVLdThDX0VxQlRrVFhBb2pXc1N2Wll3aFJVblFMNE5WX0txekgyUXZLeXc?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxOTXpzV2drdVRITXRXaFBEdGsxdFdTR2FSazBFMDJKWUJ4MF8tWWNZQnEwT2tpYXh5cmFEOUZGemN2dUV0ZTFjbjZHNDdXZ005bXV6UlVkVzNJc05Yc0t0Ri0ySzBCOXItVTI5eGZUTFRMTm10RXlLMkhFZWpnbjNvSkVoSnN0V09XaV9ucVNfeWdLWkIzQXNHWDJBZXRsNktwcl80bE40a3g2aS1ibEZwMEJodmlqYTd4UmFGdldSNTdOeElValkwWjU4YWpWNnY0YnQ4VzE1aHRzaTJIMUZqX29CaktiQUxYU2NyZFdoWQ?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxNaFYteC1YV2FWTDNpU1g1cDZxR1RtNkZPNFY5Vi1oMUFrZWZnZ0wxZ0k2alRJbEV6bVI2amZqcmlnc2VUVDktdXBqYTJjV2JfWEJXSVlGT3NzWmpfd3JrdTA1X3RWbXNoRDFuc2stanZsdC0tQVprSnA2dVVsLTdFc1Q3c2RnWUdQZXNmQmk2eEJYVDcwQVpIcWZzVl9zVGIzX1Q4SWd3elpCbTBKc0FxZGo5Y3I4ZDFyb25XdDEzcjRVSHlrclRKNnBWRE52UDJTNjJSbmQ1QXQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPRkx0eEM2aTdZcWZEeFdZRDJJVTFWWHgyWndzMTRTTlBsZ3kydXlUbDRaX3VCamRkUndoNV9YNWRvbjZSTzR5VzAxQS1uekNOX1B0RUl1TkJ4eU9UMkxrdDZVaGNKZ2k4cDdERTNMeXZzWVlESzhSZklVZWh6LVhIaWU4a1pmT3ppcHc3MHJDU2o2TWhNU3hOeUtWQ0t4dmlMS0gwc1M0V012Q2FWQkNKQVVVRQ?oc=5

## Demo notes and limitations

- Multi-ticker local demo; AI items require human spot checks; RSS coverage is not guaranteed.
- Free-tier Gemini grounding (google_search tool) returned 429; the demo uses Google News RSS + plain-text AI extraction.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
