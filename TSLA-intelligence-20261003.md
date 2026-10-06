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
| P/E (trailing) | 343.14 |
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
- Summary: Tesla reported Q3 vehicle deliveries of 486,532, exceeding production and market expectations, driving a strong 5% stock rally.
- Date: 2026-10-02 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPLTV2TThXeklJVmVnSl9pMDYzQnNoaWVielg0ekwyYTJVemhmRDdKdlpaekRVYXdTcndZNGRyelluczN1MUIxQ3J6M2FDWTQ4dnQwd3c1OEVURkdBUGdQLTBXaE1iUWxXOGFUVlZOLWdscVp0UkFTSEpsWkM3QTRDT3pMdkFlME41OHRn0gGQAUFVX3lxTFBoR1hCMDN2NU1mQ1ZJdFg3XzBQYWJSMzZmQk5aVnlBTTg5YnBfUi1KMm9seGMydVVOU2p1WnloTVVUV25QRXdYT1hwQ1Y4ODlvc0RBcUhwOG9VWUh3OG9CSnJ6N2ZuQUlBUjdWT0xPTnFaN3JHOTdjMk8tZnpWamkwOF9FaHNSUnZHQ1ZpQWkwZQ?oc=5>

### Tesla Wins Denmark Green Light For FSD Expansion — But TSLA Stock Slips
- Summary: Regulatory approval was granted in Denmark for the expansion of Tesla's Full Self-Driving technology, marking a positive step for international software monetization.
- Date: 2026-10-02 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNalFQVWYtc0ZkVzRtaDNIV1ZqWmpfYlNBcnFqS0xNNHd5NkxLMUFsTUEtbGh0ZnNtTlB1NGFxN2E5eHFzVE0zT3RBQldSOHVLNXZNVzlyd21CNVBwZUhrdkNtMU9ENGU5ZGYtbWlzM192am0tZmdtUlJscm8yanhFbS1rMnJpRHdlT3lqY2dpZUVxb1UzaUU2clc2SzNidmhkREpiNTFqRG4tRWduODJERU1B?oc=5>

## HEADWINDS

### TSLA Stock On Track For Worst Week In A Year On Fresh Roadster Delay As Musk’s April Promise Fades
- Summary: Delays regarding the next-generation Roadster continue to mount, frustrating retail investors and contributing to weekly downward pressure.
- Date: 2026-10-02 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxOTXpzV2drdVRITXRXaFBEdGsxdFdTR2FSazBFMDJKWUJ4MF8tWWNZQnEwT2tpYXh5cmFEOUZGemN2dUV0ZTFjbjZHNDdXZ005bXV6UlVkVzNJc05Yc0t0Ri0ySzBCOXItVTI5eGZUTFRMTm10RXlLMkhFZWpnbjNvSkVoSnN0V09XaV9ucVNfeWdLWkIzQXNHWDJBZXRsNktwcl80bE40a3g2aS1ibEZwMEJodmlqYTd4UmFGdldSNTdOeElValkwWjU4YWpWNnY0YnQ4VzE1aHRzaTJIMUZqX29CaktiQUxYU2NyZFdoWQ?oc=5>

### TSLA Stock: Tesla Doubles EU Registrations In May But BYD Still Leads With Over 26K Units
- Summary: Despite doubling EU registrations, Tesla faces stiff competition in Europe where competitor BYD maintains the leading position in unit sales.
- Date: 2026-10-03 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNVldVMFpzQThpWHpaaTh1MHJVVlVoa1RKdW9hd1FqRUVqMXFld1Z6MFFraWRkX0plX0M0MDBqTmpjUUhwQTZMal9FV1h6ckNITTBVQWlUcjZhQjgzVDB5RW05LXlSaXFSRktBbG1XQ3BCdXpPUzhjUTU3VjlxUmU5czlZRklkLXJiMmZmcU9qV1RKaHp5STFYSWt2dk1XWFR5ejZVSWtZVG8xYWNmTGtqQlJqaklmVXltYjVOR0hwRVEwSjVReFBpOHJwRDM?oc=5>

## CATALYSTS

### TSLA Stock Hits Nearly 3-Week High: Nvidia Win Adds Muscle To ‘Physical AI’ Pivot Despite Optimus Delays
- Summary: Tesla's pivot toward physical AI and autonomous systems gains technical support following hardware achievements, driving shares to a three-week high.
- Date: 2026-10-03 | Impact: high | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNcDFPQm5pcFd4aDEybHBvUkVjUEYwUk9TRWw4Rl9ITF81SzNpc04wdmZRN3ZxM2FESnlaWUNtWFpIbzZKdFhma1ZfdkhCN0VjZGt5ZGlTcTR5Z1pBRk5hZzk1aXl2LUJTZE9MeFpaQktLMVI2ZGtTMHg4emZLYU52VHd0SFJ4RU02Rmkzeld2MGdyVTJad1RrcUJ5ZnBRVk5Nc2x6RWtfSlRrSEYzTXpLbWJ5Qjg?oc=5>

### TSLA Stock Cools Overnight After Miami Robotaxi Rally — But Morgan Stanley Sees 30,000-Vehicle Fleet By 2030
- Summary: Analyst projections point to a massive scaling of the Robotaxi fleet by 2030, reinforcing the long-term autonomous service narrative.
- Date: 2026-10-02 | Impact: high | Horizon: long | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPRXBDR09mbWJCLWdwUUhpQkhKaTB6aHNBdXpueXQxNkdqMmUyc05NLU5BcDFaei12dms2QXdjTW9lamc2T29saHFSRDZ3ZVFSZEw0ZUpLNmhETkNZY0k5d0dmcUVPaURENkRleG9YbVh4V3RXOVpLOGE5TVRBTGs0X2tOOFVxcjZXRjFHdUthei1qdHRNX200ZHFhLWtXeVp4WXFHZmxMQ3E2ODkxYmJmOTlB?oc=5>

## RISKS

### TSLA Stock Slips Overnight: Gary Black Says SpaceX Can’t Afford Tesla – ‘The Math Won’t Pass Muster’
- Summary: Market commentary highlights the financial impracticability of a potential merger between SpaceX and Tesla, raising corporate governance concerns.
- Date: 2026-10-03 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNVGNwWnNoeTNhNmdTUDhDZUgtMVB0WjNhM3loUy1uUjhoT1hzb2llYndjZ3BNRnNpazdRektjNHZTUHJfZnpwUU9hRDRZVGpPQ1lIY01hNGswV2M3VWZaYUU1enNrVXpqbDdpamNoUUNncHJhWjFSeGFzSld3dTBMQmY3bUkwakcyWjBGV09VZXc2Sm1ISTBoR0RtRWl0ek5vbGVBSFd0elFxX0V4MUZVcFh4WGM?oc=5>

### TSLA Stock Rises Overnight: JPMorgan Says Tesla-SpaceX Merger Looks ‘Coherent On Paper’ — But China Approval Risks Loom
- Summary: While a Tesla-SpaceX combination is viewed theoretically as coherent, any such move introduces severe regulatory and approval hurdles in critical markets like China.
- Date: 2026-10-02 | Impact: high | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQSGdaUkJ2bHB1cWluVWdERFBaVVdxc3NyQVVSYWM2R2l5b05qR2diWElYeUtLV3Q1X3NTLVpnQU8yZElmSTBZbVVNNTZJOFRST0Q0akYycTk1Ti1sMmYtUVMwcUcyQURKZW1sRWJWWERxdjNoYlcxc21idmVIeHBQTmZ2aDZRbkg5amdLV2JHb1hydW82eU82MW5ITl9qd28zdWFzaXdn?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (USD) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSLA** | **343.14** | **16.85** | **133.60** | **25.50** | **1,463,662,804,992.00** | **-15.00** |
| F | N/A | 1.35 | 24.79 | -3.80 | 48,249,909,248.00 | 3.63 |
| GM | 35.10 | 1.11 | 10.59 | 1.90 | 68,678,127,616.00 | 32.99 |
| RIVN | N/A | 3.81 | -7.65 | 27.20 | 20,704,407,552.00 | 5.69 |
| LCID | N/A | -1.54 | -2.07 | 56.20 | 1,627,509,888.00 | -82.86 |

Peers fetched as_of: 2026-10-05; TSLA reuses existing data (market data as_of: 2026-10-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

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
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNalFQVWYtc0ZkVzRtaDNIV1ZqWmpfYlNBcnFqS0xNNHd5NkxLMUFsTUEtbGh0ZnNtTlB1NGFxN2E5eHFzVE0zT3RBQldSOHVLNXZNVzlyd21CNVBwZUhrdkNtMU9ENGU5ZGYtbWlzM192am0tZmdtUlJscm8yanhFbS1rMnJpRHdlT3lqY2dpZUVxb1UzaUU2clc2SzNidmhkREpiNTFqRG4tRWduODJERU1B?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxOTXpzV2drdVRITXRXaFBEdGsxdFdTR2FSazBFMDJKWUJ4MF8tWWNZQnEwT2tpYXh5cmFEOUZGemN2dUV0ZTFjbjZHNDdXZ005bXV6UlVkVzNJc05Yc0t0Ri0ySzBCOXItVTI5eGZUTFRMTm10RXlLMkhFZWpnbjNvSkVoSnN0V09XaV9ucVNfeWdLWkIzQXNHWDJBZXRsNktwcl80bE40a3g2aS1ibEZwMEJodmlqYTd4UmFGdldSNTdOeElValkwWjU4YWpWNnY0YnQ4VzE1aHRzaTJIMUZqX29CaktiQUxYU2NyZFdoWQ?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNVldVMFpzQThpWHpaaTh1MHJVVlVoa1RKdW9hd1FqRUVqMXFld1Z6MFFraWRkX0plX0M0MDBqTmpjUUhwQTZMal9FV1h6ckNITTBVQWlUcjZhQjgzVDB5RW05LXlSaXFSRktBbG1XQ3BCdXpPUzhjUTU3VjlxUmU5czlZRklkLXJiMmZmcU9qV1RKaHp5STFYSWt2dk1XWFR5ejZVSWtZVG8xYWNmTGtqQlJqaklmVXltYjVOR0hwRVEwSjVReFBpOHJwRDM?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNcDFPQm5pcFd4aDEybHBvUkVjUEYwUk9TRWw4Rl9ITF81SzNpc04wdmZRN3ZxM2FESnlaWUNtWFpIbzZKdFhma1ZfdkhCN0VjZGt5ZGlTcTR5Z1pBRk5hZzk1aXl2LUJTZE9MeFpaQktLMVI2ZGtTMHg4emZLYU52VHd0SFJ4RU02Rmkzeld2MGdyVTJad1RrcUJ5ZnBRVk5Nc2x6RWtfSlRrSEYzTXpLbWJ5Qjg?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPRXBDR09mbWJCLWdwUUhpQkhKaTB6aHNBdXpueXQxNkdqMmUyc05NLU5BcDFaei12dms2QXdjTW9lamc2T29saHFSRDZ3ZVFSZEw0ZUpLNmhETkNZY0k5d0dmcUVPaURENkRleG9YbVh4V3RXOVpLOGE5TVRBTGs0X2tOOFVxcjZXRjFHdUthei1qdHRNX200ZHFhLWtXeVp4WXFHZmxMQ3E2ODkxYmJmOTlB?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNVGNwWnNoeTNhNmdTUDhDZUgtMVB0WjNhM3loUy1uUjhoT1hzb2llYndjZ3BNRnNpazdRektjNHZTUHJfZnpwUU9hRDRZVGpPQ1lIY01hNGswV2M3VWZaYUU1enNrVXpqbDdpamNoUUNncHJhWjFSeGFzSld3dTBMQmY3bUkwakcyWjBGV09VZXc2Sm1ISTBoR0RtRWl0ek5vbGVBSFd0elFxX0V4MUZVcFh4WGM?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQSGdaUkJ2bHB1cWluVWdERFBaVVdxc3NyQVVSYWM2R2l5b05qR2diWElYeUtLV3Q1X3NTLVpnQU8yZElmSTBZbVVNNTZJOFRST0Q0akYycTk1Ti1sMmYtUVMwcUcyQURKZW1sRWJWWERxdjNoYlcxc21idmVIeHBQTmZ2aDZRbkg5amdLV2JHb1hydW82eU82MW5ITl9qd28zdWFzaXdn?oc=5

## Demo notes and limitations

- Multi-ticker local demo; AI items require human spot checks; RSS coverage is not guaranteed.
- Free-tier Gemini grounding (google_search tool) returned 429; the demo uses Google News RSS + plain-text AI extraction.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
