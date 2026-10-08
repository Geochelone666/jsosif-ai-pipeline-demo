# OTEX.TO Intelligence Demo

- ticker: **OTEX.TO**
- Report as_of: **2026-10-08**
- Market data as_of: **2026-10-07**
- Quant sources: https://finance.yahoo.com/quote/OTEX.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/OTEX.TO/key-statistics/
- AI analysis snapshot as_of: **2026-10-03** (retained; this run refreshes market data only)
- Snapshot note: the report-date daily bar may be intraday until the US market closes; its Close field is provisional. News, peers, earnings, EDGAR and macro sections reuse their existing snapshots.
- Market data fetched_at (UTC): **2026-10-08T04:17:01.296784+00:00**
- AI status: **Available**
- AI model: **gemini-3.5-flash-lite** (25 Google News RSS headlines -> AI extraction and classification; free-tier grounding unavailable, using RSS + AI)

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 33.0000 |
| Return 1D (%) | 2.1672 |
| Return 1W (%) | 3.4159 |
| Return 1M (%) | -0.3623 |
| Return YTD (%) | -23.6410 |
| Return 1Y (%) | -35.2656 |
| Annualized volatility (%) | 37.4207 |
| Beta vs SPY | 0.6999 |
| Max drawdown (%) | -47.6924 |
| Sharpe (rf=0) | -0.9798 |
| P/E (trailing) | 9.24 |
| P/B | 1.37 |
| EV/EBITDA | 7.76 |
| Revenue growth (%) | 2.90 |
| MA50 | 33.2096 |
| Close vs MA50 (%) | -0.6313 |
| MA200 | 33.1272 |
| Close vs MA200 (%) | -0.3838 |
| RSI (14, Wilder) | 55.1175 |
| MACD (12,26) | -0.1818 |
| MACD signal (9) | -0.2879 |
| MACD histogram | 0.1060 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'OTEX.TO': 255, 'SPY': 255}.

## TAILWINDS

### Open Text (NasdaqGS:OTEX) Raised Its Dividend And Buyback, Is The Stock Still 11% Undervalued?
- Summary: Open Text raised its dividend and buyback.
- Date: 2026-08-07 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQWlJudThOZjJmeV9qZFF1NEJMejQ3MnRXS3BHSVMwQ1Rad3JDMzJJZkZIaUtJZjVvRGRjalU2LTdoTExiTG1qT2Z4WERKZ3VHVEZVcnEwT0RCalluOHVyX0ZVWE1ZVGs0VUVqaGdkM2poVUtualpCU0Vrd2RqQ3JTODRGQWp3dFJrVVprU0lJUm5oN2I2Q3liZGYyaw?oc=5>

### Open Text (OTEX) Upgraded to Buy: Here's What You Should Know
- Summary: Open Text was upgraded to buy.
- Date: 2026-05-28 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOUmcxNmVRUVJtQlpnYXFRb2NjNE44ZnFKNTFacHhiRm5KUWNmLWlJU1RZck5PSGVVZ3JRRnJlM2lDalhDVlhaSDlmb0pEZ211RzZ2WTFvdHM0NERDUkY3SVhieVVFeUowdlhzU211aVlNc3dreS1MMDRTXzd2aHg0SGtSM2N1MHFiRklmcUxWb0pGYWNsVG80?oc=5>

## HEADWINDS

### Open Text Continues Transition But Growth Challenges Remain (NASDAQ:OTEX)
- Summary: Open Text continues transition while growth challenges remain.
- Date: 2025-12-04 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOeXpIR3ZKMEVlcVpBUzEzQkhaZGFTWFFhc0VqWVRnNmt4azM3ek1QV1hTM1R3RnA5bzdmN1ZRV25KSXVNWHk3Y3g5NDVTT1pLaGdmcUcwcnczQjdKdGJ0bWNlYkwwSkMyNk95SU9BekM0S284eFNMRXI3WVAwVGJ1MUh3ZkQ5Z0FuSEE5Y1lZZW1XcUFxZEJDVFpaRWRwS2xVY1E?oc=5>

### Why Open Text (OTEX) Is Down 14.6% After Naming IBM Veteran Ayman Antoun As Incoming CEO
- Summary: Open Text is down 14.6% after naming IBM veteran Ayman Antoun as incoming CEO.
- Date: 2026-02-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE42MTduWjhKSUprSXFHUlgyUXJUemw1cFp1eE9KMlJDdVZ5RmFOdkJKVUJyaEtmMjN6aGFreHBjZGE5TlV2czhWXzM0ZnJrWTMxOXhTZmtoZFFJY2xOQWNocmE2TjI2cHEzcDhxSG5TYURjZmZRWV9EUg?oc=5>

### Open Text: A Dividend Doesn't Compensate For Years Of Debt Paydown (NASDAQ:OTEX)
- Summary: A dividend doesn't compensate for years of debt paydown for Open Text.
- Date: 2026-02-19 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQa081eFZGLXpKSDVIeWk1dnNkdGtKb3hfVWNaQXJCQkZBTHVxMTV1T3FJUWh1ODNjOTJXTVhUVDF2c3pLVDNZaGdoV3FiUTVENFZibGx5X0xkQTZyV1J1aUhnU3FwLWp1T0hoS2dUN1JwMTk2UVg1X1d1NE02dXZ3aE5WMVViODdxaXhvdHdCUDZxbk81MWo4aUZqbk4yOG5FZDlac0ZNNA?oc=5>

## CATALYSTS

### OpenText increases share repurchase program to $500M
- Summary: OpenText increases share repurchase program to $500M
- Date: 2026-02-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNUkJPNjdPTHQ1ZHRVeW9GbVFfUktORjlrUGlhRkh3Y20tdkxPdlNPX0VzcFptaTJBeFdsRlVFeXpKQXhDTWNkaGlCaExFc0xMaGlwNEduTDJPMllzZ3JrYWFHbVd2c0tXOGQ5UFJDRUhQQ2JvRnB3a0pyRWFYRU83UkNSU1JOQUJFOFFzN2d2T3JXYTg?oc=5>

### Open Text (NasdaqGS:OTEX) Valuation Check As Preliminary Q3 Revenue And CEO Transition Take Shape
- Summary: Preliminary Q3 revenue and CEO transition take shape for Open Text.
- Date: 2026-04-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNUERkUDJsUDBpSFBDdGVXUE51WjFUQ0h5OEpqQWttdlQ1OWc3S3ZxTWw2S25hTkE2ZjdHRWNUMEdnZ01PLU5MejRUTldlN0Zsa2U3bVdkZlBqUzNMSzZ3ME5UdGNUSHRtLUowNmh6LTg1aTlfVV80Y2szR0hzTjdaZXdOdFM1M0NZazVVa1lPdm5zaVBWbmt0eG9LNVVTcm8?oc=5>

### A $1 billion bond sale will help fund OpenText's planned payoff of 2027 debt
- Summary: A $1 billion bond sale will help fund OpenText's planned payoff of 2027 debt.
- Date: 2026-10-01 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPNmJFamt5V05LUC1sU0xJZVVselBManBaUkZIM2lVcHpwRDRaQzMxMXdScElYWElCTndvSjFwM09vSTV3V20wbFpyUGFlMGphdVRQTm5rbzR1akpqaXhKQ01yS01VWWFYWjhmR3ZTNXlMM2k3b2JFOG0xM2Z2Wmt3dDdXRXBSbmJDTFh4elkyVndTX3RwU3dHbHNVeHZwQWJ5bDNMejJDZWZQZjA?oc=5>

## RISKS

### Open Text Corporation (NASDAQ:OTEX) Stock's 27% Dive Might Signal An Opportunity But It Requires Some Scrutiny
- Summary: Open Text stock experienced a 27% dive.
- Date: 2026-02-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNRDVCVElaU3R1bnAwSFE0c2tIaWd5MFB3X1p1OHZjd3c4ZDh4ckZtOHVnUWp6eG1ybmRkSi1CeDFId0dyM0JoSTJSbm5BQWVTNmtuUVNYRWFnaXEteHVHRV9udlI0TzRQZ3BqS3p4YkpPbkNhdGxCV2l6dEk2dTBEQjJqOW03ZElZR1ktcWNCVEhfRU55dzl4bkJzdUxqZTViVDBzeERSamNIMWEtdnllTjFQQUdEczZxVE95UmdUVThHZDVqcXI00gHMAUFVX3lxTE5qdjZCeFR6UVJQc1hKVXdmMHU3WTZSYkxETWpCd01Ral9kLTdnNkRRbGMxUExJalNPVFpyYUhOZ2EzTVZkLXBjYVh0YlZCRnk2MnNBX0xUcnk5bURMellOTGJDNzdoNDF2aEJzMDY0eEpkd2tXYV9vVmZuNjhweWJmZF9PZFNqUkRZQkdoTHgwYW9ZbzE1VHp5OHNvM2paX191MF8xMlRHWmIyX3hKMGpaT2wtVU5OZXU0VVI4YUREbGI0STRRSFRoR3dkQg?oc=5>

### Open Text (OTEX) Stock Trades Below Fair Value As Shares Fell 44%
- Summary: Open Text shares fell 44%, trading below fair value.
- Date: 2026-08-07 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNbWdzcHN3a2V2ZUc2Y1NqellaUHNKSkJkWEtyVmVGekdfb0RGOEtZX2NKNDhURW53eEE0RjM1VUFNdS1rUGxGbTJyRkRWQURGNDVHSVhocXFvT21IdTV0V2xTRHBLZ0ROUDZtYjNCX0x1UGVhYmJhRHlwOXJZeHVjbjJfOHZLMWJ5MmdxQnZtZ3VVckNlREpz?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (USD) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **OTEX.TO** | **9.24** | **1.37** | **7.76** | **2.90** | **7,990,182,400.00** | **-35.27** |

Peers fetched as_of: 2026-10-08; OTEX.TO reuses existing data (market data as_of: 2026-10-07); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-06
- Next expected earnings: 2026-11-05 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment Rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index | CPIAUCSL | 334.13 | 2026-08-01 |
| Federal Funds Effective Rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-08-06
- Revenue (latest available single quarter): 685,879,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 172,652,000.00 USD; period 2026-01-01/2026-03-31; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1002638/000100263826000068/otex-20260630.htm

SEC requests use the demo placeholder contact email contact@example.com. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxQWlJudThOZjJmeV9qZFF1NEJMejQ3MnRXS3BHSVMwQ1Rad3JDMzJJZkZIaUtJZjVvRGRjalU2LTdoTExiTG1qT2Z4WERKZ3VHVEZVcnEwT0RCalluOHVyX0ZVWE1ZVGs0VUVqaGdkM2poVUtualpCU0Vrd2RqQ3JTODRGQWp3dFJrVVprU0lJUm5oN2I2Q3liZGYyaw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOUmcxNmVRUVJtQlpnYXFRb2NjNE44ZnFKNTFacHhiRm5KUWNmLWlJU1RZck5PSGVVZ3JRRnJlM2lDalhDVlhaSDlmb0pEZ211RzZ2WTFvdHM0NERDUkY3SVhieVVFeUowdlhzU211aVlNc3dreS1MMDRTXzd2aHg0SGtSM2N1MHFiRklmcUxWb0pGYWNsVG80?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOeXpIR3ZKMEVlcVpBUzEzQkhaZGFTWFFhc0VqWVRnNmt4azM3ek1QV1hTM1R3RnA5bzdmN1ZRV25KSXVNWHk3Y3g5NDVTT1pLaGdmcUcwcnczQjdKdGJ0bWNlYkwwSkMyNk95SU9BekM0S284eFNMRXI3WVAwVGJ1MUh3ZkQ5Z0FuSEE5Y1lZZW1XcUFxZEJDVFpaRWRwS2xVY1E?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTE42MTduWjhKSUprSXFHUlgyUXJUemw1cFp1eE9KMlJDdVZ5RmFOdkJKVUJyaEtmMjN6aGFreHBjZGE5TlV2czhWXzM0ZnJrWTMxOXhTZmtoZFFJY2xOQWNocmE2TjI2cHEzcDhxSG5TYURjZmZRWV9EUg?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQa081eFZGLXpKSDVIeWk1dnNkdGtKb3hfVWNaQXJCQkZBTHVxMTV1T3FJUWh1ODNjOTJXTVhUVDF2c3pLVDNZaGdoV3FiUTVENFZibGx5X0xkQTZyV1J1aUhnU3FwLWp1T0hoS2dUN1JwMTk2UVg1X1d1NE02dXZ3aE5WMVViODdxaXhvdHdCUDZxbk81MWo4aUZqbk4yOG5FZDlac0ZNNA?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNUkJPNjdPTHQ1ZHRVeW9GbVFfUktORjlrUGlhRkh3Y20tdkxPdlNPX0VzcFptaTJBeFdsRlVFeXpKQXhDTWNkaGlCaExFc0xMaGlwNEduTDJPMllzZ3JrYWFHbVd2c0tXOGQ5UFJDRUhQQ2JvRnB3a0pyRWFYRU83UkNSU1JOQUJFOFFzN2d2T3JXYTg?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNUERkUDJsUDBpSFBDdGVXUE51WjFUQ0h5OEpqQWttdlQ1OWc3S3ZxTWw2S25hTkE2ZjdHRWNUMEdnZ01PLU5MejRUTldlN0Zsa2U3bVdkZlBqUzNMSzZ3ME5UdGNUSHRtLUowNmh6LTg1aTlfVV80Y2szR0hzTjdaZXdOdFM1M0NZazVVa1lPdm5zaVBWbmt0eG9LNVVTcm8?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPNmJFamt5V05LUC1sU0xJZVVselBManBaUkZIM2lVcHpwRDRaQzMxMXdScElYWElCTndvSjFwM09vSTV3V20wbFpyUGFlMGphdVRQTm5rbzR1akpqaXhKQ01yS01VWWFYWjhmR3ZTNXlMM2k3b2JFOG0xM2Z2Wmt3dDdXRXBSbmJDTFh4elkyVndTX3RwU3dHbHNVeHZwQWJ5bDNMejJDZWZQZjA?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNRDVCVElaU3R1bnAwSFE0c2tIaWd5MFB3X1p1OHZjd3c4ZDh4ckZtOHVnUWp6eG1ybmRkSi1CeDFId0dyM0JoSTJSbm5BQWVTNmtuUVNYRWFnaXEteHVHRV9udlI0TzRQZ3BqS3p4YkpPbkNhdGxCV2l6dEk2dTBEQjJqOW03ZElZR1ktcWNCVEhfRU55dzl4bkJzdUxqZTViVDBzeERSamNIMWEtdnllTjFQQUdEczZxVE95UmdUVThHZDVqcXI00gHMAUFVX3lxTE5qdjZCeFR6UVJQc1hKVXdmMHU3WTZSYkxETWpCd01Ral9kLTdnNkRRbGMxUExJalNPVFpyYUhOZ2EzTVZkLXBjYVh0YlZCRnk2MnNBX0xUcnk5bURMellOTGJDNzdoNDF2aEJzMDY0eEpkd2tXYV9vVmZuNjhweWJmZF9PZFNqUkRZQkdoTHgwYW9ZbzE1VHp5OHNvM2paX191MF8xMlRHWmIyX3hKMGpaT2wtVU5OZXU0VVI4YUREbGI0STRRSFRoR3dkQg?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNbWdzcHN3a2V2ZUc2Y1NqellaUHNKSkJkWEtyVmVGekdfb0RGOEtZX2NKNDhURW53eEE0RjM1VUFNdS1rUGxGbTJyRkRWQURGNDVHSVhocXFvT21IdTV0V2xTRHBLZ0ROUDZtYjNCX0x1UGVhYmJhRHlwOXJZeHVjbjJfOHZLMWJ5MmdxQnZtZ3VVckNlREpz?oc=5

## Demo notes and limitations

- Multi-ticker local demo; AI items require human spot checks; RSS coverage is not guaranteed.
- Free-tier Gemini grounding (google_search tool) returned 429; the demo uses Google News RSS + plain-text AI extraction.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
