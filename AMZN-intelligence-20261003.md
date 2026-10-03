# AMZN Intelligence Demo

- ticker: **AMZN**
- Report as_of: **2026-10-03**
- Market data as_of: **2026-10-02**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI status: **Available**
- AI model: **gemini-3.5-flash-lite** (25 Google News RSS headlines -> AI extraction and classification; free-tier grounding unavailable, using RSS + AI)

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 251.5200 |
| Return 1D (%) | 1.3254 |
| Return 1W (%) | 0.7410 |
| Return 1M (%) | -1.3570 |
| Return YTD (%) | 8.9680 |
| Return 1Y (%) | 13.0884 |
| Annualized volatility (%) | 34.4165 |
| Beta vs SPY | 1.4400 |
| Max drawdown (%) | -21.7362 |
| Sharpe (rf=0) | 0.5267 |
| P/E (trailing) | 19.96 |
| P/B | 4.92 |
| EV/EBITDA | 16.82 |
| Revenue growth (%) | 19.60 |
| MA50 | 256.5438 |
| Close vs MA50 (%) | -1.9583 |
| MA200 | 241.3629 |
| Close vs MA200 (%) | 4.2082 |
| RSI (14, Wilder) | 48.5637 |
| MACD (12,26) | -2.1953 |
| MACD signal (9) | -2.1316 |
| MACD histogram | -0.0637 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 252, 'SPY': 252}.

## TAILWINDS

### Amazon, Top Warship Builder Added To Goldman's Conviction List
- Summary: Goldman Sachs has added Amazon to its high-conviction list, highlighting strong institutional confidence in the company's growth vectors.
- Date: 2026-10-01 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPdHdmU2RRYmhlU0pha05lM2p1TkZvS19OT1RjVWdEanVlck53dmpKaEoyeDU5UDAwWU9vLXVMM3hKdWNSVWs0c1NuVEo1aEFvejdhMWJrWWp5S3VNNEVJMU9lQnVuWDhlSGNsSzlpYV9XNENEYjRSbUlvTGNsNXplN2RxVHJvX3FOcXVCUW8xd0thQTJuOUhJSDVoVDVRVlVyaURNUE05S2R2UQ?oc=5>

### Amazon Stock Has 46% Upside. Muse and Dots Threats Are ‘Overstated.’
- Summary: The headline presents an opinion that Amazon has 46% upside and that Muse and Dots threats are overstated.
- Date: 2026-09-30 | Impact: high | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxQOUU3aFNpc3Q5aGlia0h3eDg3U1JjSHN1Qy1wWEZaZVpnY28tMnhNN3pEc0o3eFVSVFdON1ZtZ05DMC1YaWQtVy1zRjFJcldKZ2Z1clR4Vy1xeXA3RDUxUllXMkZfM1VZT1B5am5KOFNJM3R6MzJzQzBCZTBRcndyQUZB?oc=5>

## HEADWINDS

### AMZN Stock Drops Nearly 2% After-Hours — Senate Panel Reportedly Probes Amazon Over Alleged Chinese Influence
- Summary: A Senate panel is investigating Amazon regarding alleged Chinese influence, creating regulatory headwinds and pressuring the stock.
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxQRVNXWXAtNWVsUWRhdDVTMWxDTjJtUWwxNFpzN2hIcUk4M3RMeThoMVo4NkwzQ0JuRVl2ZlE0TjZYVVY3ZDYzZU9jTmNpQjFIWlJUa2YyWkpvaktuWHphMXdyUW9WczVvNU5YU1psOTBRakpsV2lNamZXcVVBODdrRTlmRGgwN3ZheW9GZUEyY2Q4dGhJU3RJTVE2R3Bpd09fanAxaWZEbXFCaTUtS0taMlE4QW1PWWQwcWJ2d0lKaFd3WGZPaVNZeHd1dWY?oc=5>

### Could Amazon Stock Survive AI Spending Outrunning Its Cash?
- Summary: Concerns are mounting regarding whether massive capital expenditures on artificial intelligence initiatives will outpace operating cash flows.
- Date: 2026-09-30 | Impact: medium | Horizon: medium | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQR0NzUGZhY05seEZXRWdESXNCTktRMThkTXQtYXhxZkZTanRQT2ZKVjY0VHlJcUtrWFJLYWktVFVJS3VyNDZ0QzVkR3Y3X2JsMEdkZVY5YkhvXzQ4R2ZnUWU3eVRST0xndUdvQVpXczJoOWxhU056WllLM2lzMjlWQ29DSUloMnNxM0NDRGViS2p0T0VGNWVFZ0FxTFZSOEdWOG1mNVg2WUdiLXRxcEZuM2x1ZHRUdzVISEow?oc=5>

## CATALYSTS

### Amazon Stock (AMZN) Pops Up 1.8% as AWS Chief Pledges $1 Billion Fund to Ease AI Data Center Pushback from Locals
- Summary: The headline reports that the AWS chief pledged a $1 billion fund to address local opposition to AI data centers.
- Date: 2026-10-02 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNYUYtdVVWOXFPc1BGdExseWs0VUpWbGtwT2l0SXZ1TWlmUVc0MkF6VmZYUjdQSWJMd0QydU5lY1RBZWRaLTJaU0NENWdzVzdzdE5OTnhhUVZBVEZhRzJVUE5CekNGTmlQSGMwZ3I0eVZnenRPQktVRUlvekg1Y2lyclVzRno5aXdNZGt3TU8yUkVqSVhWNXZvMVBSei1fNDY2cy1pbG92ZUJ4ZW9saFhSdFY4d0NPUG5uTzlyRlhBLXBUR3k1OEtUenV6VWRQUEYtLTdmRUhn?oc=5>

### AMZN Inches Higher Premarket: Amazon Reportedly Seeks To Offload $8B Of Nvidia Chips To Investors
- Summary: Reports indicate Amazon is seeking to offload $8 billion of Nvidia chips to third-party investors, impacting how AI infrastructure is financed.
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNVF9xYld4bkxmSlhqcjBpWHdBQjFhdXNwRG9rM0h0U1g3N1lUN05mdk1Yc1JvOC1pU2NLUGZ4SzdEWnY1aVo4dHZzR0tEOG05dzJEOE1Wa0JlZE5QcWhZaW9oOWhKdHp1Z0JmUTZWVmlZNy1mMnI3azhOTEFXRXlFbjM3R2Q0QWgyX0c1TmdzZWRFMjN5eXpDdFNheTF2WEk1ckE?oc=5>

## RISKS

### AMZN Stock Dips Overnight After Breaching $3 Trillion Market Cap: Retail Gets Buzzing About Bezos’ Share Sale
- Summary: Profit-taking and retail discussion surrounding founder Jeff Bezos's share sales following the $3 trillion milestone could introduce volatility.
- Date: 2026-10-02 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNVHZ1T2JiXzhsbzJVTkxnQ1A5VDBvYkJPVWxhbkp5Yi1jQkVGNmRMSnFzdl9Bc2YzcTh1SFJhN2paYmdVRVJwcENRVl9uV0ZIWkdRRHR2ekxDWUFEOUpZY2xYbDBmRlJjcmZodVJXS01DQ3FvZnFYMnVTd1F3a3lPTEFsb3g0X255dmtyMFNqdkxSSzNSWmpVdG1yWGxRMHZibjM0Ym1UWXNnV2V4UmRnOGdvWnY?oc=5>

### Amazon (AMZN) Stock Could Be 43% Undervalued After AI Tax Break Scrutiny
- Summary: Increased scrutiny regarding tax breaks utilized for AI infrastructure investments poses potential financial and compliance risks.
- Date: 2026-09-30 | Impact: medium | Horizon: medium | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOclJHanp6RXBLM2k2R0xTelJxdWdEOTM1NTI5aS1iOThrTXhpc2VUQXNqOU1vUUFyQ3NXMlBpeklzRmp1U0ZHWGpOSS1JR3EtcU9mOUVHWUcwZ1hZR2VPY3BZVkpIQ3Q3QnhheE9UYzZRc0tIVWVZZ19tVU0yM0RQaWx3eGJuVWhUUTB1SGtPbzBNWS14cHVobkh3bnFQN2VfRDBrX205M1NGSnBla2ZITk42UXlZQkVNVGdrOS1XZ2tzZmxy0gHKAUFVX3lxTE1ubU13akRIaDQ2eWlVQ3VKNzBvNWxwQURvNlQ2Zi1Fc1VjVUVCYWphTUw1RldUQWNjbThFWmdiTkN2VEZTdnhtQ0c5WEpyaENYeFVCVFQ1YUd2dTdRSllSaGw0dnBJUnpPSzJkdGlIeVZrQ3BGUDRCVWp2WTVYQ1VaemlsMGdwS2NKc0dWUVM4MnZUclpKd2JPbDVqTHg5WlRXZ3lCYVZHbEllQnFBSDd0OG5PdURNeDFpZ3NqNWc4WjhZMFJ4X0FSZ1E?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (USD) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **19.96** | **4.92** | **16.82** | **19.60** | **2,712,973,606,912.00** | **13.09** |
| GOOGL | 16.98 | 6.75 | 23.66 | 24.20 | 4,200,982,642,688.00 | 40.17 |
| META | 27.32 | 7.10 | 17.12 | 28.00 | 1,854,788,337,664.00 | 0.48 |
| MSFT | 28.58 | 8.69 | 20.05 | 17.70 | 3,842,942,959,616.00 | 1.17 |
| AAPL | 37.88 | 45.34 | 29.12 | 16.40 | 4,869,931,925,504.00 | 30.25 |

Peers fetched as_of: 2026-10-03; AMZN reuses existing data (market data as_of: 2026-10-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

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
- Revenue (latest available single quarter): 200,606,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 62,647,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm

SEC requests use the demo placeholder contact email contact@example.com. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPdHdmU2RRYmhlU0pha05lM2p1TkZvS19OT1RjVWdEanVlck53dmpKaEoyeDU5UDAwWU9vLXVMM3hKdWNSVWs0c1NuVEo1aEFvejdhMWJrWWp5S3VNNEVJMU9lQnVuWDhlSGNsSzlpYV9XNENEYjRSbUlvTGNsNXplN2RxVHJvX3FOcXVCUW8xd0thQTJuOUhJSDVoVDVRVlVyaURNUE05S2R2UQ?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxQOUU3aFNpc3Q5aGlia0h3eDg3U1JjSHN1Qy1wWEZaZVpnY28tMnhNN3pEc0o3eFVSVFdON1ZtZ05DMC1YaWQtVy1zRjFJcldKZ2Z1clR4Vy1xeXA3RDUxUllXMkZfM1VZT1B5am5KOFNJM3R6MzJzQzBCZTBRcndyQUZB?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxQRVNXWXAtNWVsUWRhdDVTMWxDTjJtUWwxNFpzN2hIcUk4M3RMeThoMVo4NkwzQ0JuRVl2ZlE0TjZYVVY3ZDYzZU9jTmNpQjFIWlJUa2YyWkpvaktuWHphMXdyUW9WczVvNU5YU1psOTBRakpsV2lNamZXcVVBODdrRTlmRGgwN3ZheW9GZUEyY2Q4dGhJU3RJTVE2R3Bpd09fanAxaWZEbXFCaTUtS0taMlE4QW1PWWQwcWJ2d0lKaFd3WGZPaVNZeHd1dWY?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQR0NzUGZhY05seEZXRWdESXNCTktRMThkTXQtYXhxZkZTanRQT2ZKVjY0VHlJcUtrWFJLYWktVFVJS3VyNDZ0QzVkR3Y3X2JsMEdkZVY5YkhvXzQ4R2ZnUWU3eVRST0xndUdvQVpXczJoOWxhU056WllLM2lzMjlWQ29DSUloMnNxM0NDRGViS2p0T0VGNWVFZ0FxTFZSOEdWOG1mNVg2WUdiLXRxcEZuM2x1ZHRUdzVISEow?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNYUYtdVVWOXFPc1BGdExseWs0VUpWbGtwT2l0SXZ1TWlmUVc0MkF6VmZYUjdQSWJMd0QydU5lY1RBZWRaLTJaU0NENWdzVzdzdE5OTnhhUVZBVEZhRzJVUE5CekNGTmlQSGMwZ3I0eVZnenRPQktVRUlvekg1Y2lyclVzRno5aXdNZGt3TU8yUkVqSVhWNXZvMVBSei1fNDY2cy1pbG92ZUJ4ZW9saFhSdFY4d0NPUG5uTzlyRlhBLXBUR3k1OEtUenV6VWRQUEYtLTdmRUhn?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNVF9xYld4bkxmSlhqcjBpWHdBQjFhdXNwRG9rM0h0U1g3N1lUN05mdk1Yc1JvOC1pU2NLUGZ4SzdEWnY1aVo4dHZzR0tEOG05dzJEOE1Wa0JlZE5QcWhZaW9oOWhKdHp1Z0JmUTZWVmlZNy1mMnI3azhOTEFXRXlFbjM3R2Q0QWgyX0c1TmdzZWRFMjN5eXpDdFNheTF2WEk1ckE?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNVHZ1T2JiXzhsbzJVTkxnQ1A5VDBvYkJPVWxhbkp5Yi1jQkVGNmRMSnFzdl9Bc2YzcTh1SFJhN2paYmdVRVJwcENRVl9uV0ZIWkdRRHR2ekxDWUFEOUpZY2xYbDBmRlJjcmZodVJXS01DQ3FvZnFYMnVTd1F3a3lPTEFsb3g0X255dmtyMFNqdkxSSzNSWmpVdG1yWGxRMHZibjM0Ym1UWXNnV2V4UmRnOGdvWnY?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOclJHanp6RXBLM2k2R0xTelJxdWdEOTM1NTI5aS1iOThrTXhpc2VUQXNqOU1vUUFyQ3NXMlBpeklzRmp1U0ZHWGpOSS1JR3EtcU9mOUVHWUcwZ1hZR2VPY3BZVkpIQ3Q3QnhheE9UYzZRc0tIVWVZZ19tVU0yM0RQaWx3eGJuVWhUUTB1SGtPbzBNWS14cHVobkh3bnFQN2VfRDBrX205M1NGSnBla2ZITk42UXlZQkVNVGdrOS1XZ2tzZmxy0gHKAUFVX3lxTE1ubU13akRIaDQ2eWlVQ3VKNzBvNWxwQURvNlQ2Zi1Fc1VjVUVCYWphTUw1RldUQWNjbThFWmdiTkN2VEZTdnhtQ0c5WEpyaENYeFVCVFQ1YUd2dTdRSllSaGw0dnBJUnpPSzJkdGlIeVZrQ3BGUDRCVWp2WTVYQ1VaemlsMGdwS2NKc0dWUVM4MnZUclpKd2JPbDVqTHg5WlRXZ3lCYVZHbEllQnFBSDd0OG5PdURNeDFpZ3NqNWc4WjhZMFJ4X0FSZ1E?oc=5

## Demo notes and limitations

- Multi-ticker local demo; AI items require human spot checks; RSS coverage is not guaranteed.
- Free-tier Gemini grounding (google_search tool) returned 429; the demo uses Google News RSS + plain-text AI extraction.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
