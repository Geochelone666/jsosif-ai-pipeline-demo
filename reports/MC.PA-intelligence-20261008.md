# MC.PA Intelligence Demo

- ticker: **MC.PA**
- Report as_of: **2026-10-08**
- Market data as_of: **2026-10-06**
- Quant sources: https://finance.yahoo.com/quote/MC.PA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MC.PA/key-statistics/
- AI analysis snapshot as_of: **2026-10-03** (retained; this run refreshes market data only)
- Snapshot note: the report-date daily bar may be intraday until the US market closes; its Close field is provisional. News, peers, earnings, EDGAR and macro sections reuse their existing snapshots.
- Market data fetched_at (UTC): **2026-10-08T04:18:02.150513+00:00**
- AI status: **Available**
- AI model: **gemini-3.5-flash-lite** (25 Google News RSS headlines -> AI extraction and classification; free-tier grounding unavailable, using RSS + AI)

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 385.6000 |
| Return 1D (%) | 1.2339 |
| Return 1W (%) | -2.2808 |
| Return 1M (%) | -10.1375 |
| Return YTD (%) | -39.2422 |
| Return 1Y (%) | -26.8560 |
| Annualized volatility (%) | 30.0290 |
| Beta vs SPY | 0.6319 |
| Max drawdown (%) | -41.0025 |
| Sharpe (rf=0) | -0.8804 |
| P/E (trailing) | 17.71 |
| P/B | 2.81 |
| EV/EBITDA | 10.80 |
| Revenue growth (%) | -2.90 |
| MA50 | 434.6650 |
| Close vs MA50 (%) | -11.2880 |
| MA200 | 487.9231 |
| Close vs MA200 (%) | -20.9711 |
| RSI (14, Wilder) | 31.9043 |
| MACD (12,26) | -14.9504 |
| MACD signal (9) | -14.8453 |
| MACD histogram | -0.1051 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MC.PA': 258, 'SPY': 255}.

## TAILWINDS

### Christian Dior Shares Rise 16.9% After Arnault Family Announces LVMH Ownership Restructuring
- Summary: Christian Dior shares rise 16.9% after the Arnault family announces LVMH ownership restructuring.
- Date: 2026-09-24 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxNV0Y4cmVYQTgySmk3cU9IeXdTanU0VjNHSWx2eEtmdlY5LWRLT3FCSDJaQXFfT19haXp2TlBVYk0wTVBqZGNHcjhUTlZybkp4czJ3Q0toemZiMUtBMm9qOEswazJjWWpIektwbnZkeXJYZDRiMXVzUDIyaVF3RjJsMTFveDE?oc=5>

## HEADWINDS

### LVMH (ENXTPA:MC) Stock Trades At A Discount To Cash Flow After A 37% Fall
- Summary: LVMH (ENXTPA:MC) Stock Trades At A Discount To Cash Flow After A 37% Fall
- Date: 2026-09-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOUEdDeE1PcHJhUXpySHY2ZV96WjFZbnJSdmltMVJESVBxWGNmZkNxTHZGYXhEeUZ2dFo4RHZEWHhvRzVhRExwVEpBb3M4eXFWbGZnSjYtbXNsSTVTenJtLXBpTXkyX0JKMy0tcEN3V2Z2cVppRFMtTEtpR0pjeWlQbE1GOGdOYmJxQ1h1N0Y4eXdHcjJNOXB3?oc=5>

### LVMH stock dips as fashion unit misses estimates despite return to growth
- Summary: LVMH stock dips as fashion unit misses estimates despite return to growth
- Date: 2026-07-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPZGo2T3hzczlKZVZHbTF0T183Z3duLUlMX3RFUkV0a3A5WFpQOTlYWlNLbzNHNk96MGg3bXJrejBJMWFodjJRMlhCR2RNLVVYemlacVc3WVVmSXZqb0dGX1NNNTVJSjBTWFZuQjFjYXFjS0ZVVEVZQ19VWDhWYjEweGVScDBSWWx3OGNVOGlxWjhwUlZJWUE4SUdYNURZQQ?oc=5>

### LVMH, once Europe's biggest stock, exits top 10 as luxury slumps
- Summary: LVMH exits the top 10 stocks in Europe as luxury slumps.
- Date: 2026-09-14 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxNc2dHbmZTZHkxOEJtZUNVVHQ4eERJMEU1c0c2OW5BV0hheG5TTGJyaExEUWktOXN3RW5PSFBqaFBiNFZxTHlSS3h1c3hlMndEcWZHM0lHa3ZPUU9NS1Bud3JXbk1rbWlfNG9hMEtYMDFtVmc1Ui1rYVpMdkhueXJtY0NzSjBWSFk?oc=5>

### LVMH Shares Expected to Weaken After Fashion Division Misses Market Expectations
- Summary: LVMH shares are expected to weaken after its fashion division misses market expectations.
- Date: 2026-07-28 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxObmpRRk5YRU9EZzBPbHctdXp5MHZCV1gwOU4yb3ZRY1JNOWFDVnQ4UGlhT1hyLW4wMGRhajhYODhvajdrU3d2ZjlxQ0NVYloxbWhkTDVhLWYtVFZSWWFyYUQ5b0tURlJsRHNoQ1FXRWJ1QTdlMS1vZTVaTHBmSy1WcHdzeUpPOWp1cDJmZQ?oc=5>

## CATALYSTS

### Assessing LVMH (ENXTPA:MC) Valuation After Mixed Recent Returns And Contrasting Fair Value Estimates
- Summary: Assessing LVMH (ENXTPA:MC) Valuation After Mixed Recent Returns And Contrasting Fair Value Estimates
- Date: 2026-06-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPanpwR2hybkFnSy1oYmI3NmJTcUVrYXZMOHJnS0xnZnBSS29Bd2lsRkJRQi1Yak9taGZITm9peVlaTGZWRzVzcjA4TThNSldvUDhwM0ZLanpRZmw5ZGF4X1VyNEo1VjNBa0tXdU1EaXlZSGtzYU5JeDRYTkI0ZkVJeGRsR3ZQVVRxNzJDdmQ3ZnZRR0ltcGxjZC1iZENsSGdo?oc=5>

### LVMH 2025 Dividend
- Summary: LVMH 2025 Dividend
- Date: 2026-04-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOZktKOWpoYjN0UVNxRGJCbS16a1BrWFRPSnQyTnhIOGRaSkZFUU93VkdUVzF5ay05MnZiU3g5OGFRYnFER0VtNGd1cjFOUGtsTVZ0TTNyM3dmcEVqWkNabFQ0RmdseVd4UzFkeG1sNzNLZzVDT2k3dTF4M1VOMnNBbXlZWUE1SGphSlNV?oc=5>

### LVMH revenue dips 3% in H1 2026, but organic growth returns
- Summary: LVMH revenue dips 3% in H1 2026, but organic growth returns
- Date: 2026-07-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQdGk0ZlQySVdzaGVkRDVxbTJYT29GUmNmYTU4eVdIWWNZZ2NkeXpsT1lRa0ZHMXBLVWM1a1lZZlVKX0YxQ2JmNFpLUkFhZThsZU91cnZHSTB0a0hkX3lSeXdrUVRSamUwZkI4Z2dwaEhkeXN5dUpFNEZEcFVYSW5UVXY0Z3VNMUFSNzFtVXhyTjA?oc=5>

### European Luxury Stocks Advance as LVMH’s Fashion Business Returns to Growth
- Summary: European luxury stocks advance as LVMH's fashion business returns to growth.
- Date: 2026-07-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNSS01NWJfMlNENndhbHdxMXBBU2FHVldXbENNeGpzYUFHU0VCRG54NDNLel9TZGJzUlNPeGNRYkR5NnpCOUR1c0tjZHpDT1RRTmI4ckFSRlRiY0VDY05yS253dndDUlo5MmU4N1hUTjBJQ2xCa3I3Xzc5ZmZmTDczRUpkYXc1Z2h3S0dMTw?oc=5>

## RISKS

### LVMH (ENXTPA:MC) Faces Amended Stella McCartney Lawsuit Over Pay And Retaliation
- Summary: LVMH (ENXTPA:MC) Faces Amended Stella McCartney Lawsuit Over Pay And Retaliation
- Date: 2026-06-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxONjFFRDlPM3RBbkhXNzA3VUxXV0REbGl0OVRERTYwZEtxVkx1ajEtV3lwOEM1R0g5RGR0ZlZ0Wk1NNno4OWdtcnY0SHJfaXlhYV9sUkxPNEo4WDFuNjdjVHg5MXJDQ0Y2azVwTGlfZ2NWSjdubU11Tld0bU5xTkRWSFhqZnFLSnBVUTNqWGJET0xLb3VzcVdqRA?oc=5>

### LVMH Refocuses Luxury Portfolio With Marc Jacobs Sale To WHP And G III
- Summary: LVMH refocuses its luxury portfolio with the Marc Jacobs sale to WHP and G III.
- Date: 2026-05-16 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNZnl3ZkhXMFJPeGFHaDVXQkNZZnZvcUNseHFHdi1fWnlfcnhsM2VyOFVSeHFHVEdPRVpKV1NtYWNDYUlZRVo2VE5EdWVnakNvLWdrb21Mb0V6SHRxSWtzbnhkYVhfVnVTTVlDWm9KcWhBaDFYcVlZM05lOEhMQjlDbGhvT2drM2Z3cFRKQnNudzB6NHZNR1ZqeWhBZGU2VHBnbHI0?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (USD) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MC.PA** | **17.71** | **2.81** | **10.80** | **-2.90** | **191,492,341,760.00** | **-26.86** |

Peers fetched as_of: 2026-10-08; MC.PA reuses existing data (market data as_of: 2026-10-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: N/A
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment Rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index | CPIAUCSL | 334.13 | 2026-08-01 |
| Federal Funds Effective Rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the demo placeholder contact email contact@example.com. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMihAFBVV95cUxNV0Y4cmVYQTgySmk3cU9IeXdTanU0VjNHSWx2eEtmdlY5LWRLT3FCSDJaQXFfT19haXp2TlBVYk0wTVBqZGNHcjhUTlZybkp4czJ3Q0toemZiMUtBMm9qOEswazJjWWpIektwbnZkeXJYZDRiMXVzUDIyaVF3RjJsMTFveDE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOUEdDeE1PcHJhUXpySHY2ZV96WjFZbnJSdmltMVJESVBxWGNmZkNxTHZGYXhEeUZ2dFo4RHZEWHhvRzVhRExwVEpBb3M4eXFWbGZnSjYtbXNsSTVTenJtLXBpTXkyX0JKMy0tcEN3V2Z2cVppRFMtTEtpR0pjeWlQbE1GOGdOYmJxQ1h1N0Y4eXdHcjJNOXB3?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPZGo2T3hzczlKZVZHbTF0T183Z3duLUlMX3RFUkV0a3A5WFpQOTlYWlNLbzNHNk96MGg3bXJrejBJMWFodjJRMlhCR2RNLVVYemlacVc3WVVmSXZqb0dGX1NNNTVJSjBTWFZuQjFjYXFjS0ZVVEVZQ19VWDhWYjEweGVScDBSWWx3OGNVOGlxWjhwUlZJWUE4SUdYNURZQQ?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxNc2dHbmZTZHkxOEJtZUNVVHQ4eERJMEU1c0c2OW5BV0hheG5TTGJyaExEUWktOXN3RW5PSFBqaFBiNFZxTHlSS3h1c3hlMndEcWZHM0lHa3ZPUU9NS1Bud3JXbk1rbWlfNG9hMEtYMDFtVmc1Ui1rYVpMdkhueXJtY0NzSjBWSFk?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxObmpRRk5YRU9EZzBPbHctdXp5MHZCV1gwOU4yb3ZRY1JNOWFDVnQ4UGlhT1hyLW4wMGRhajhYODhvajdrU3d2ZjlxQ0NVYloxbWhkTDVhLWYtVFZSWWFyYUQ5b0tURlJsRHNoQ1FXRWJ1QTdlMS1vZTVaTHBmSy1WcHdzeUpPOWp1cDJmZQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPanpwR2hybkFnSy1oYmI3NmJTcUVrYXZMOHJnS0xnZnBSS29Bd2lsRkJRQi1Yak9taGZITm9peVlaTGZWRzVzcjA4TThNSldvUDhwM0ZLanpRZmw5ZGF4X1VyNEo1VjNBa0tXdU1EaXlZSGtzYU5JeDRYTkI0ZkVJeGRsR3ZQVVRxNzJDdmQ3ZnZRR0ltcGxjZC1iZENsSGdo?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOZktKOWpoYjN0UVNxRGJCbS16a1BrWFRPSnQyTnhIOGRaSkZFUU93VkdUVzF5ay05MnZiU3g5OGFRYnFER0VtNGd1cjFOUGtsTVZ0TTNyM3dmcEVqWkNabFQ0RmdseVd4UzFkeG1sNzNLZzVDT2k3dTF4M1VOMnNBbXlZWUE1SGphSlNV?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQdGk0ZlQySVdzaGVkRDVxbTJYT29GUmNmYTU4eVdIWWNZZ2NkeXpsT1lRa0ZHMXBLVWM1a1lZZlVKX0YxQ2JmNFpLUkFhZThsZU91cnZHSTB0a0hkX3lSeXdrUVRSamUwZkI4Z2dwaEhkeXN5dUpFNEZEcFVYSW5UVXY0Z3VNMUFSNzFtVXhyTjA?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNSS01NWJfMlNENndhbHdxMXBBU2FHVldXbENNeGpzYUFHU0VCRG54NDNLel9TZGJzUlNPeGNRYkR5NnpCOUR1c0tjZHpDT1RRTmI4ckFSRlRiY0VDY05yS253dndDUlo5MmU4N1hUTjBJQ2xCa3I3Xzc5ZmZmTDczRUpkYXc1Z2h3S0dMTw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxONjFFRDlPM3RBbkhXNzA3VUxXV0REbGl0OVRERTYwZEtxVkx1ajEtV3lwOEM1R0g5RGR0ZlZ0Wk1NNno4OWdtcnY0SHJfaXlhYV9sUkxPNEo4WDFuNjdjVHg5MXJDQ0Y2azVwTGlfZ2NWSjdubU11Tld0bU5xTkRWSFhqZnFLSnBVUTNqWGJET0xLb3VzcVdqRA?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNZnl3ZkhXMFJPeGFHaDVXQkNZZnZvcUNseHFHdi1fWnlfcnhsM2VyOFVSeHFHVEdPRVpKV1NtYWNDYUlZRVo2VE5EdWVnakNvLWdrb21Mb0V6SHRxSWtzbnhkYVhfVnVTTVlDWm9KcWhBaDFYcVlZM05lOEhMQjlDbGhvT2drM2Z3cFRKQnNudzB6NHZNR1ZqeWhBZGU2VHBnbHI0?oc=5

## Demo notes and limitations

- Multi-ticker local demo; AI items require human spot checks; RSS coverage is not guaranteed.
- Free-tier Gemini grounding (google_search tool) returned 429; the demo uses Google News RSS + plain-text AI extraction.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
