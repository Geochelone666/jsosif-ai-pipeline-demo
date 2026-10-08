# TSLA Intelligence Demo

- ticker: **TSLA**
- Report as_of: **2026-10-05**
- Market data as_of: **2026-10-05**
- Quant sources: https://finance.yahoo.com/quote/TSLA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSLA/key-statistics/
- AI analysis snapshot as_of: **2026-10-03** (retained; this run refreshes market data only)
- Snapshot note: the report-date daily bar may be intraday until the US market closes; its Close field is provisional. News, peers, earnings, EDGAR and macro sections reuse their existing snapshots.
- Market data fetched_at (UTC): **2026-10-05T16:09:15.516459+00:00**
- AI status: **Available**
- AI model: **gemini-3.5-flash-lite** (25 Google News RSS headlines -> AI extraction and classification; free-tier grounding unavailable, using RSS + AI)

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 377.0400 |
| Return 1D (%) | 1.7405 |
| Return 1W (%) | 5.4805 |
| Return 1M (%) | 6.4844 |
| Return YTD (%) | -16.1612 |
| Return 1Y (%) | -12.2816 |
| Annualized volatility (%) | 45.6508 |
| Beta vs SPY | 2.2163 |
| Max drawdown (%) | -39.1035 |
| Sharpe (rf=0) | -0.1768 |
| P/E (trailing) | 349.11 |
| P/B | 17.14 |
| EV/EBITDA | 133.60 |
| Revenue growth (%) | 25.50 |
| MA50 | 348.8640 |
| Close vs MA50 (%) | 8.0765 |
| MA200 | 392.6179 |
| Close vs MA200 (%) | -3.9677 |
| RSI (14, Wilder) | 58.0399 |
| MACD (12,26) | 2.7625 |
| MACD signal (9) | 3.2181 |
| MACD histogram | -0.4556 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSLA': 253, 'SPY': 253}.

## TAILWINDS

### Tesla stock jumps 5% on better-than-expected vehicle deliveries report
- Summary: Tesla stock jumps 5% on better-than-expected vehicle deliveries report
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPLTV2TThXeklJVmVnSl9pMDYzQnNoaWVielg0ekwyYTJVemhmRDdKdlpaekRVYXdTcndZNGRyelluczN1MUIxQ3J6M2FDWTQ4dnQwd3c1OEVURkdBUGdQLTBXaE1iUWxXOGFUVlZOLWdscVp0UkFTSEpsWkM3QTRDT3pMdkFlME41OHRn0gGQAUFVX3lxTFBoR1hCMDN2NU1mQ1ZJdFg3XzBQYWJSMzZmQk5aVnlBTTg5YnBfUi1KMm9seGMydVVOU2p1WnloTVVUV25QRXdYT1hwQ1Y4ODlvc0RBcUhwOG9VWUh3OG9CSnJ6N2ZuQUlBUjdWT0xPTnFaN3JHOTdjMk8tZnpWamkwOF9FaHNSUnZHQ1ZpQWkwZQ?oc=5>

### TSLA Stock Pops as Tesla Surprises on Q3 Deliveries
- Summary: TSLA Stock Pops as Tesla Surprises on Q3 Deliveries
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNQTFacFR2ZjJmTHZPbG8wemFhdWZBd3FNWXZGRDAtemtHanBNS0h0RFc3TVlVOVJJeUhELV9hRVFiUGxNNk1MWktHVGtWOGVCbE1pRUZHSjJLaG96cldNWV9nYzJ0TGhHRkxoM2JuQzZwaGQyLUxZVkhxWmIzRHZJZ1lRLUljZXpTYWJjYXp6dW41M1lpTW1IUXpqSQ?oc=5>

### TSLA Stock Hits Nearly 3-Week High: Nvidia Win Adds Muscle To ‘Physical AI’ Pivot Despite Optimus Delays
- Summary: TSLA Stock Hits Nearly 3-Week High: Nvidia Win Adds Muscle To ‘Physical AI’ Pivot Despite Optimus Delays
- Date: 2026-10-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNcDFPQm5pcFd4aDEybHBvUkVjUEYwUk9TRWw4Rl9ITF81SzNpc04wdmZRN3ZxM2FESnlaWUNtWFpIbzZKdFhma1ZfdkhCN0VjZGt5ZGlTcTR5Z1pBRk5hZzk1aXl2LUJTZE9MeFpaQktLMVI2ZGtTMHg4emZLYU52VHd0SFJ4RU02Rmkzeld2MGdyVTJad1RrcUJ5ZnBRVk5Nc2x6RWtfSlRrSEYzTXpLbWJ5Qjg?oc=5>

### TSLA Stock Cools Overnight After Miami Robotaxi Rally — But Morgan Stanley Sees 30,000-Vehicle Fleet By 2030
- Summary: TSLA Stock Cools Overnight After Miami Robotaxi Rally — But Morgan Stanley Sees 30,000-Vehicle Fleet By 2030
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPRXBDR09mbWJCLWdwUUhpQkhKaTB6aHNBdXpueXQxNkdqMmUyc05NLU5BcDFaei12dms2QXdjTW9lamc2T29saHFSRDZ3ZVFSZEw0ZUpLNmhETkNZY0k5d0dmcUVPaURENkRleG9YbVh4V3RXOVpLOGE5TVRBTGs0X2tOOFVxcjZXRjFHdUthei1qdHRNX200ZHFhLWtXeVp4WXFHZmxMQ3E2ODkxYmJmOTlB?oc=5>

## HEADWINDS

### TSLA Eyes Worst Week In 2 Months As Q3 Delivery Numbers Loom — But Munster Bets On A Beat As 'EV Winter' Thaws
- Summary: TSLA Eyes Worst Week In 2 Months As Q3 Delivery Numbers Loom — But Munster Bets On A Beat As 'EV Winter' Thaws
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQamlzeFFIVkVOcktJNmNzVlhTOE9MSEFhWTlUTWJjRmRuYmI2dXFEbTlmMVdXR1BvU2piWGdWMDJQZlVhb0taVkxvbEQ4bkpkNUFvd08wS2NpN1Z3VDQtdWFKb1FUbkdpcUZYVjJZa2haS0JYTDNvNWhrUVVtTTZRWTJLTXllcVROVGVENlBsQ0U?oc=5>

### TSLA Stock On Track For Worst Week In A Year On Fresh Roadster Delay As Musk’s April Promise Fades
- Summary: TSLA Stock On Track For Worst Week In A Year On Fresh Roadster Delay As Musk’s April Promise Fades
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxOTXpzV2drdVRITXRXaFBEdGsxdFdTR2FSazBFMDJKWUJ4MF8tWWNZQnEwT2tpYXh5cmFEOUZGemN2dUV0ZTFjbjZHNDdXZ005bXV6UlVkVzNJc05Yc0t0Ri0ySzBCOXItVTI5eGZUTFRMTm10RXlLMkhFZWpnbjNvSkVoSnN0V09XaV9ucVNfeWdLWkIzQXNHWDJBZXRsNktwcl80bE40a3g2aS1ibEZwMEJodmlqYTd4UmFGdldSNTdOeElValkwWjU4YWpWNnY0YnQ4VzE1aHRzaTJIMUZqX29CaktiQUxYU2NyZFdoWQ?oc=5>

### TSLA Stock Slips Overnight: Gary Black Says SpaceX Can’t Afford Tesla – ‘The Math Won’t Pass Muster’
- Summary: TSLA Stock Slips Overnight: Gary Black Says SpaceX Can’t Afford Tesla – ‘The Math Won’t Pass Muster’
- Date: 2026-10-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNVGNwWnNoeTNhNmdTUDhDZUgtMVB0WjNhM3loUy1uUjhoT1hzb2llYndjZ3BNRnNpazdRektjNHZTUHJfZnpwUU9hRDRZVGpPQ1lIY01hNGswV2M3VWZaYUU1enNrVXpqbDdpamNoUUNncHJhWjFSeGFzSld3dTBMQmY3bUkwakcyWjBGV09VZXc2Sm1ISTBoR0RtRWl0ek5vbGVBSFd0elFxX0V4MUZVcFh4WGM?oc=5>

### TSLA Stock Eyes Red September: Cathie Wood Buys Ahead Of Q3 Update As Tesla Bear Flags Funding Pressure
- Summary: TSLA Stock Eyes Red September: Cathie Wood Buys Ahead Of Q3 Update As Tesla Bear Flags Funding Pressure
- Date: 2026-09-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi9AFBVV95cUxQVmVTZlVqR25SZ2xQaDhwaE1nQWdwWXNjYUtaNXlHS0d1S0FxUTZ1bVJqdEZEdTdkazNTSVhMbDhaYVhhOHlfWWpHNTE2RTZaVWlsNnA4ZERheWwtcE0tZ1I1ODlkYnkzS2FZQ24xY0lycUh1WGhmZUlrNzlyT05WWHhoTi1kZkJYYkFsY0piODRfYXdCT2RkS1NSX1RWN0FHUlFMQVZwNDZOYmwxM0VvbGpjVUMwN1lRcGtST1Y3YldRUVpsazh4N3dOTWJFVFFhR2tubHMwXzhTRmpKc3VjNWtsWGhEcDJsMHR1UDlXNWZxdDRt?oc=5>

### Tesla (TSLA) Stock Falls Amid Market Uptick: What Investors Need to Know
- Summary: Tesla (TSLA) Stock Falls Amid Market Uptick: What Investors Need to Know
- Date: 2026-09-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNYWNLWkZTbUZYbHRZNWlpWDg2LTJCTXh4UnBZN21uNHo2OVhDdE9qNDJfMDRINU4xZGxaUW01UXk3bXRlSmdZdG02dTk2ZzVUTjBSUURrblUwT01Ha05RVWpaVXRyNjR2amNoYTB1V0pZNDVFdGJUekFxdTVnSjhBSldzUWlwMWE1Szd3ZHdJQUVkbE90ek8w?oc=5>

## CATALYSTS

### TSLA Stock Rises Overnight: JPMorgan Says Tesla-SpaceX Merger Looks ‘Coherent On Paper’ — But China Approval Risks Loom
- Summary: TSLA Stock Rises Overnight: JPMorgan Says Tesla-SpaceX Merger Looks ‘Coherent On Paper’ — But China Approval Risks Loom
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQSGdaUkJ2bHB1cWluVWdERFBaVVdxc3NyQVVSYWM2R2l5b05qR2diWElYeUtLV3Q1X3NTLVpnQU8yZElmSTBZbVVNNTZJOFRST0Q0akYycTk1Ti1sMmYtUVMwcUcyQURKZW1sRWJWWERxdjNoYlcxc21idmVIeHBQTmZ2aDZRbkg5amdLV2JHb1hydW82eU82MW5ITl9qd28zdWFzaXdn?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (USD) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSLA** | **349.11** | **17.14** | **133.60** | **25.50** | **1,489,137,434,624.00** | **-12.28** |
| F | N/A | 1.35 | 24.79 | -3.80 | 48,249,909,248.00 | 3.63 |
| GM | 35.10 | 1.11 | 10.59 | 1.90 | 68,678,127,616.00 | 32.99 |
| RIVN | N/A | 3.81 | -7.65 | 27.20 | 20,704,407,552.00 | 5.69 |
| LCID | N/A | -1.54 | -2.07 | 56.20 | 1,627,509,888.00 | -82.86 |

Peers fetched as_of: 2026-10-05; TSLA reuses existing data (market data as_of: 2026-10-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

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
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNQTFacFR2ZjJmTHZPbG8wemFhdWZBd3FNWXZGRDAtemtHanBNS0h0RFc3TVlVOVJJeUhELV9hRVFiUGxNNk1MWktHVGtWOGVCbE1pRUZHSjJLaG96cldNWV9nYzJ0TGhHRkxoM2JuQzZwaGQyLUxZVkhxWmIzRHZJZ1lRLUljZXpTYWJjYXp6dW41M1lpTW1IUXpqSQ?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNcDFPQm5pcFd4aDEybHBvUkVjUEYwUk9TRWw4Rl9ITF81SzNpc04wdmZRN3ZxM2FESnlaWUNtWFpIbzZKdFhma1ZfdkhCN0VjZGt5ZGlTcTR5Z1pBRk5hZzk1aXl2LUJTZE9MeFpaQktLMVI2ZGtTMHg4emZLYU52VHd0SFJ4RU02Rmkzeld2MGdyVTJad1RrcUJ5ZnBRVk5Nc2x6RWtfSlRrSEYzTXpLbWJ5Qjg?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPRXBDR09mbWJCLWdwUUhpQkhKaTB6aHNBdXpueXQxNkdqMmUyc05NLU5BcDFaei12dms2QXdjTW9lamc2T29saHFSRDZ3ZVFSZEw0ZUpLNmhETkNZY0k5d0dmcUVPaURENkRleG9YbVh4V3RXOVpLOGE5TVRBTGs0X2tOOFVxcjZXRjFHdUthei1qdHRNX200ZHFhLWtXeVp4WXFHZmxMQ3E2ODkxYmJmOTlB?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQamlzeFFIVkVOcktJNmNzVlhTOE9MSEFhWTlUTWJjRmRuYmI2dXFEbTlmMVdXR1BvU2piWGdWMDJQZlVhb0taVkxvbEQ4bkpkNUFvd08wS2NpN1Z3VDQtdWFKb1FUbkdpcUZYVjJZa2haS0JYTDNvNWhrUVVtTTZRWTJLTXllcVROVGVENlBsQ0U?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxOTXpzV2drdVRITXRXaFBEdGsxdFdTR2FSazBFMDJKWUJ4MF8tWWNZQnEwT2tpYXh5cmFEOUZGemN2dUV0ZTFjbjZHNDdXZ005bXV6UlVkVzNJc05Yc0t0Ri0ySzBCOXItVTI5eGZUTFRMTm10RXlLMkhFZWpnbjNvSkVoSnN0V09XaV9ucVNfeWdLWkIzQXNHWDJBZXRsNktwcl80bE40a3g2aS1ibEZwMEJodmlqYTd4UmFGdldSNTdOeElValkwWjU4YWpWNnY0YnQ4VzE1aHRzaTJIMUZqX29CaktiQUxYU2NyZFdoWQ?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNVGNwWnNoeTNhNmdTUDhDZUgtMVB0WjNhM3loUy1uUjhoT1hzb2llYndjZ3BNRnNpazdRektjNHZTUHJfZnpwUU9hRDRZVGpPQ1lIY01hNGswV2M3VWZaYUU1enNrVXpqbDdpamNoUUNncHJhWjFSeGFzSld3dTBMQmY3bUkwakcyWjBGV09VZXc2Sm1ISTBoR0RtRWl0ek5vbGVBSFd0elFxX0V4MUZVcFh4WGM?oc=5
- https://news.google.com/rss/articles/CBMi9AFBVV95cUxQVmVTZlVqR25SZ2xQaDhwaE1nQWdwWXNjYUtaNXlHS0d1S0FxUTZ1bVJqdEZEdTdkazNTSVhMbDhaYVhhOHlfWWpHNTE2RTZaVWlsNnA4ZERheWwtcE0tZ1I1ODlkYnkzS2FZQ24xY0lycUh1WGhmZUlrNzlyT05WWHhoTi1kZkJYYkFsY0piODRfYXdCT2RkS1NSX1RWN0FHUlFMQVZwNDZOYmwxM0VvbGpjVUMwN1lRcGtST1Y3YldRUVpsazh4N3dOTWJFVFFhR2tubHMwXzhTRmpKc3VjNWtsWGhEcDJsMHR1UDlXNWZxdDRt?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNYWNLWkZTbUZYbHRZNWlpWDg2LTJCTXh4UnBZN21uNHo2OVhDdE9qNDJfMDRINU4xZGxaUW01UXk3bXRlSmdZdG02dTk2ZzVUTjBSUURrblUwT01Ha05RVWpaVXRyNjR2amNoYTB1V0pZNDVFdGJUekFxdTVnSjhBSldzUWlwMWE1Szd3ZHdJQUVkbE90ek8w?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQSGdaUkJ2bHB1cWluVWdERFBaVVdxc3NyQVVSYWM2R2l5b05qR2diWElYeUtLV3Q1X3NTLVpnQU8yZElmSTBZbVVNNTZJOFRST0Q0akYycTk1Ti1sMmYtUVMwcUcyQURKZW1sRWJWWERxdjNoYlcxc21idmVIeHBQTmZ2aDZRbkg5amdLV2JHb1hydW82eU82MW5ITl9qd28zdWFzaXdn?oc=5

## Demo notes and limitations

- Multi-ticker local demo; AI items require human spot checks; RSS coverage is not guaranteed.
- Free-tier Gemini grounding (google_search tool) returned 429; the demo uses Google News RSS + plain-text AI extraction.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
