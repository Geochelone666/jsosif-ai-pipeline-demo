# ACN Intelligence Demo

- ticker: **ACN**
- Report as_of: **2026-10-08**
- Market data as_of: **2026-10-07**
- Quant sources: https://finance.yahoo.com/quote/ACN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ACN/key-statistics/
- AI analysis snapshot as_of: **2026-10-03** (retained; this run refreshes market data only)
- Snapshot note: the report-date daily bar may be intraday until the US market closes; its Close field is provisional. News, peers, earnings, EDGAR and macro sections reuse their existing snapshots.
- Market data fetched_at (UTC): **2026-10-08T04:14:40.841200+00:00**
- AI status: **N/A: AI unavailable: 'list' object has no attribute 'get'**
- AI model: **gemini-3.5-flash-lite** (25 Google News RSS headlines -> AI extraction and classification; free-tier grounding unavailable, using RSS + AI)

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 196.6400 |
| Return 1D (%) | 1.6753 |
| Return 1W (%) | 7.2367 |
| Return 1M (%) | 5.3128 |
| Return YTD (%) | -25.1986 |
| Return 1Y (%) | -20.1162 |
| Annualized volatility (%) | 48.2831 |
| Beta vs SPY | 0.2445 |
| Max drawdown (%) | -56.5068 |
| Sharpe (rf=0) | -0.2241 |
| P/E (trailing) | 14.26 |
| P/B | 3.71 |
| EV/EBITDA | 8.35 |
| Revenue growth (%) | 6.20 |
| MA50 | 182.4802 |
| Close vs MA50 (%) | 7.7596 |
| MA200 | 192.3868 |
| Close vs MA200 (%) | 2.2108 |
| RSI (14, Wilder) | 57.0704 |
| MACD (12,26) | 4.0357 |
| MACD signal (9) | 2.9745 |
| MACD histogram | 1.0612 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ACN': 255, 'SPY': 255}.

## TAILWINDS

### Accenture Surges On Fiscal Q4 Beat, Outlook Amid AI Disruption Debate
- Summary: Accenture Surges On Fiscal Q4 Beat, Outlook Amid AI Disruption Debate
- Date: 2026-10-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQNV9weHdjQ2hvRDBRNDMzS3d0djdfRTVJX1RVY0JmZU1mSE1mSTduMlMzQndBT1J3MnpSMG5tQXVQc0RORTVXb0xKc3ZwY0hvQTBMWTJVUGlCbmtXS1dTaGU5MGpoNlJuMlhxMW4yT2Q4SnBpcVIxSkg0dHIxTWExeEZFQnBJMGZfYzRtM05TbGhYczNvbE1oag?oc=5>

### ACN Stock Jumps After Accenture Posts Record $84.5B Annual Bookings, Q4 Earnings Beat
- Summary: ACN Stock Jumps After Accenture Posts Record $84.5B Annual Bookings, Q4 Earnings Beat
- Date: 2026-10-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOTll6bTBtUW1BNkdHTnhZbnBEV3NfVXJoN1lfY1JRRkZabC1hQVVVTkUwY19DSlFWNm9LOXdjOS02YXZLUVZUbW5YVnE0N3pORFpyaWxMSU5iSm9wNnV5SWlQZzQyd0NZWnRZZVFldWQ0Z0NQNUZ3cG42eHpzRWRVZFBBamhTQnFrRDZlWVd5bnBqWF84dzVYOS1tUnM?oc=5>

### Accenture shares jump 21% after quarterly revenue beat, upbeat outlook (ACN:NYSE)
- Summary: Accenture shares jump 21% after quarterly revenue beat, upbeat outlook (ACN:NYSE)
- Date: 2026-10-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPcGN0YW5aWG5QSkk3RlYyTEZFYVlEUGxsTnJ0LV9tLTdaVkJCczBudHl2T0FpdmhJclNSY0h0VlU2NTBneC1PSlpqa2ZYV2kzQUdjd1NqTElfVHFYQzRhV3pORGtxN2x3TGZMWDM0UnpLZkswbmd5WWcxUUl3ZFVrbEtOVkREdDhCeXBOamlyMm9HVE5xcUQ2YjR5X2tlQm40RVh5WmUzZE9SZw?oc=5>

### Accenture stock rallies after earnings beat expectations
- Summary: Accenture stock rallies after earnings beat expectations
- Date: 2026-10-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNWm5yS2ZOQW0xelJ4eVZxVzJST2J4eGU1SHRvd3pBNnFhbHk2QWZHM0FkeUd2S0Uzd0RabnZrWTdkcW1FYi1XUmE4dG1RYm5LSnFERXU3WGRMZVhXTEhNcVlNTHppc3diUUpjV2tZakViQ3V2N1BJVlNZWTBrVG83TEJYdmVKWXFKS0dSeEwxSDdUOHRsWDJ6d3VBWVJNZTF4RHNKTDFYeUNwbVdnMThzREpYcFJINWdBZVHSAb8BQVVfeXFMTUY4Z0RwX1RSOC1RVXVYc29laGZ4NnpXVTJiYVJYUjgxc0dGVnpkNmRMYUZKRVpKYkVsbkhDZjZlVXJlbVlnNl9MZ29UOHppZWFtRV9LeGRVYlJjdWF4NEpWbUxVV3Rxa3oxSWF0NTFoRzFmUUxnRXBCbmQxSmw0STIzWjNGSGg2SjFObmFKY2tXWkhqcjlaRjRaMUg4YkwwQTc1blBVWkkwOEJmd2F4TVQ2OThqNE1laFVxd0kydzg?oc=5>

### Accenture (ACN) Stock Trades Up, Here Is Why
- Summary: Accenture (ACN) Stock Trades Up, Here Is Why
- Date: 2026-10-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNSDRIN3ZWZDdwMVloTDlSVXhQQW9JTjV1RWd4V1F6M204RHp2N2ItbmUtUXc2WWcyVGVNU29BeTRzWFo1ZHJTeXFSTGhSN0xmUmVfUWYybHhrWHJNQlVnZEZaYWVRZ1hmZ0taN0E0Vlp4Q0NFQ2dMSk4taUFIc19NUDB5Q3I2Y2lnVHdHMTc3UUJzSG8zQ2EyaTdzQQ?oc=5>

### Accenture stock surges as record bookings dispel AI fears
- Summary: Accenture stock surges as record bookings dispel AI fears
- Date: 2026-10-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxNMDl0R0FDTnJiR05XQzg2OVVDekF2LWZ0MkhzLWMxVlpOYkZqS2I3clE4dTd1bmtGS1MxNzVGNFNfTHp0NkxSVEdvVEtfdllBNDktWGVONWNEVmlXMUtfeVlOd05jMlVVd095MTF3WW42c1l5SVFIcmxVWGlFRVN2bF9LTllRU1J6ejNzYzNaYTBpV29OVHNjaEMwQ01pSFpMSjNveEFOTGZRMU95YXpnNUsyQkRaVndiQ3lCRGJ3?oc=5>

### After Accenture Surges 17% in 1 Day, Here's What Comes Next for ACN Stock
- Summary: After Accenture Surges 17% in 1 Day, Here's What Comes Next for ACN Stock
- Date: 2026-10-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNUUlZcllmT1FXN0dkOVBnanNUdVZjMERvOEVOUkJwSHI4dk1IbDJEMW44SXVTckVkc3BkbGVXdUVXSmRUa3JUTE9mSFlPLUl2UG54bjdjMVZYdFBNWGhhZ3lfZ1N4dTZrWjdZQkVWaWxmV3Flb1E0cDY0d053SGxYNzliUWJnb2E1c2NIWHZ2dHA2dEl1?oc=5>

### Accenture (ACN) Stock Is Up, What You Need To Know
- Summary: Accenture (ACN) Stock Is Up, What You Need To Know
- Date: 2026-09-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOUEMwSzR4SUpZbHAwRnRGb3hMYVJsdzF5NXltVkphaHdIYTZkQ1lTdEI5a2Uydlo5SnNUSU5feFY4NHIzM2lQUXN5SWhTMWxNTVotSm5xZ2R2SGZUeXViRkVNdXJ6LVp0MDdRdWZXUFVaMTJQSWRobHlkMXBuQUNkT00xMUQ5cVowREZSN1E3OHRGR1U?oc=5>

### Accenture Stock Climbs as AI Demand Boosts Results
- Summary: Accenture Stock Climbs as AI Demand Boosts Results
- Date: 2026-10-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPd2JfRk9YNzBpRTFlNEVHWHB1OWZrSlNuV0t4NVNzY0xaS2hzTEJ4Y1Nabl9pYS1PRWxOT25YVVJ5bE9WMzdRZTkwcGIxMTd0WlJkVXpNY3Z4R0stZWJRQWRsX3dGMUtrSEZ3clZYcnpONzN4a3NEWExKMUozYXg3enZVQmxhUVhLckZBOTVmVThlTXBqTVowUkxkNGlPQnVCTjVIaEpaaW14UlZYOWdv?oc=5>

### Accenture (ACN) Stock Rallies On Margin Gains As Valuation Questions Linger
- Summary: Accenture (ACN) Stock Rallies On Margin Gains As Valuation Questions Linger
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNc01UT0FVeVNWVDZ4bXJsU1dZSmw2aUM2X05kYWh5aXh3R2Ffc3RvbDVBTVpjUHVFelh5eFdvMjAzT3lXb3pNQklQRWJsSkFHYXB0X245ZlpsS1R6UUhvVjVkTDJUWEVfdjN3bExSc0w1NFdpaVdpQVU4ZXF0RXdkbVJtclc0ZUlQZ1NjZFBWVklzY0VKc0l3b01GdDJyODJlZVhCbkQ1RjB3Y2J3WE85TU1hd0JCOUU4R0l2RXpQYTE4QTDSAcgBQVVfeXFMUDNiUGpKM082aXQ4QmhJeU5RY3ctMU5BVTZsZlgxWXY5aDhZVVVHR3RVMVFIb3RkMDhKMGRCUENfNngySTZvQ2ltX0lPbnRhV0haWXpUWFJtMDVsYzRRYVY3MFNYcUFITHE4ZlM0aE5mWUktNy10a1pzSmtRQ2pfTTJPUTFjV2tERlBrOHdONGJ1REUxd2ZrUHJ1QWkyZWNYbmpORTEtNmpXc1hyNXR5TVprUlRqbjhkNC1iWFUzM2YtLVB1OGlyS0k?oc=5>

### ACN Stock Rises 37.6% in Three Months: Here's What You Should Know
- Summary: ACN Stock Rises 37.6% in Three Months: Here's What You Should Know
- Date: 2026-09-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPeDcxYXVCUzI5ZVE3NXNfNVU1dmJEM05Rc1pmS3pYN3Jvdmt0ZnlZcVJqSXZSM1AxeDVIcndMMnZhbzRBSDFSVEVGWlFWNW5yY3ZMQ2JmZGRHcjBKVzNnbVo2NXlvLWk4RVZUdldaNndFWU5CYmM3U3NHMHVucXVxZ0VsbkZCemxndnJucjh3?oc=5>

### Why Accenture (ACN) Stock Is Up Today
- Summary: Why Accenture (ACN) Stock Is Up Today
- Date: 2026-09-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQSWtlUVNLQkdBTFVOdW9UdjJYNDFhZE5nbXhzRmQ4QTBZQ3RIZ1NMOGV4TWpYVVhmU1FRR0RBZks2U2l6WmhSUmlDMk1iX3c1aGZJcFEtXzBiRnRDQkJIdV8tMmFaSC1MZzVBSVM5ak1pSkFKYjhqQjRpZ0xPeTNac0ZrNGFEY1JsTGhaZjhYN3lNNXo1OW1wcV9n?oc=5>

## HEADWINDS

### Accenture (ACN) Stock Trades Down, Here Is Why
- Summary: Accenture (ACN) Stock Trades Down, Here Is Why
- Date: 2026-09-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNcGhqTFJJWUJHdTJ4eUJjemFXbUpHS1dvWVdJWmZuTnlPd0NjWFo0cHl4RURyOHNUT01MMG1jTkM3aFJzRnNJOFdLRG5QcmxIODBpOHlBLVk2WVl6LTM4RE40WVRSdG1HOUpKVzNPTWgtWi1xa29QLThzVnpDSWxBWWh5cHdQRElZY0xmVWwwSDkxNzBwSkpBcGlXZVE?oc=5>

### Accenture PLC Stock (ACN) Moved Down by 4.67% on Oct 2: Key Drivers Unveiled
- Summary: Accenture PLC Stock (ACN) Moved Down by 4.67% on Oct 2: Key Drivers Unveiled
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNcVpmSHRvengwZ2o5QzBUcHNvV2pwMG1CR1RqTTUwRkR4S0p5WmZTNkthOTcxWHI5VnJCQ3IzeWdJRnhlNmFwdVU3dnF1SEEwcF9yMEQ1MUdtU1VSZV9aNVk0MkhFMzBoX0x2UG9uWWJXa0hNR0kxS2NmNjFTM1VhZlRPc0VCenJQREE?oc=5>

### Accenture (ACN) Stock Still Looks Overvalued On Its 40% Five Year Fall
- Summary: Accenture (ACN) Stock Still Looks Overvalued On Its 40% Five Year Fall
- Date: 2026-08-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQbWxFZW9BWFo1VnhlUFNDM3IyWXMxMzhEU1Zqcm5xUElxR1VVTzFQaEowMXVxSGs2MnJOSUI2OGhMOC1FaFpTaTFuTXZJWmVfQ21qeExHMmwtZl9QR2dKTlhtVlRvbGdDTXcxeTY4bXlwNnFYSkNGUWZKc0k4MHBJNkc5eV9ER3I4X2dBUFFodGVKZWVBQzAzT21jNTA?oc=5>

## CATALYSTS

### Accenture Stock Soars After Stronger-Than-Expected Earnings
- Summary: Accenture Stock Soars After Stronger-Than-Expected Earnings
- Date: 2026-10-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNdFdnVGktX0tBWkN0Zjd4WGt5LUpiM1IxN29ZQmdKZG1CSWMwV2ZaSjFRSXRJcVZtcG5KNVJSa2FTRm5xczdOeUZQUDBQeHg5d0pXMEFjdmgyb1FNOUZWR1phMW5EU0UzRmlteVBnVXV6NnFJTU40MXJvSnF1eXB2ak1tczJTWmQtVlZrb2FOWlk3dkVtX05Qck55aEROU1JDSzM0cG1CX3NnckZ2N21CSjl1OHRUdw?oc=5>

### Accenture (ACN) Soars 15.8% as Q4 Earnings, AI Bookings Crush Disruption Fears
- Summary: Accenture (ACN) Soars 15.8% as Q4 Earnings, AI Bookings Crush Disruption Fears
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNbml3UVFvME5TTnFKMnJkYURzSTBCYjBiZ3lCV2pKdTFfR1o5Sll2X2FISmduZTNhRGViRGpYR1VXU0JnSlpiUlBPZjRibWQ1UFhRTjcwXzlJN19CaUtBczdmSDFNRmw3cGdkLS1fbnJZQ19mSjRHbldBb3k4UzdEa1ZPR2haVGlCWWlCa01fVlN1SGc?oc=5>

### Accenture (ACN) Launches Construct Following A New Question About Whether The Stock Is Fully Valued
- Summary: Accenture (ACN) Launches Construct Following A New Question About Whether The Stock Is Fully Valued
- Date: 2026-09-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNU184LW1KSmNBT0ZtVlBDTlU4QjFjUHBwSUVvRjIwSzVUTVVEWFQ2QnQ1OUNMQzNEUUJVa3RKc0FlRklFQ09SaXprU0RIUmI2Q0pMS3d1UVR6WHp6MjVROFJGTnltS2dDLThCU2ZrTVpodU9WR3RiQWdVSW5WVERNTTdaQTg1LUljbUFraFJwTTRXdmFQb1RnbVNKUDVVSUZZXzBwdGR5dGJUVU0?oc=5>

## RISKS

N/A: AI unavailable: 'list' object has no attribute 'get'

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (USD) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ACN** | **14.26** | **3.71** | **8.35** | **6.20** | **120,332,288,000.00** | **-20.12** |

Peers fetched as_of: 2026-10-08; ACN reuses existing data (market data as_of: 2026-10-07); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-01
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment Rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index | CPIAUCSL | 334.13 | 2026-08-01 |
| Federal Funds Effective Rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-06-18
- Revenue (latest available single quarter): 18,718,144,000.00 USD; period 2026-03-01/2026-05-31; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,338,989,000.00 USD; period 2026-03-01/2026-05-31; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1467373/000146737326000032/acn-20260531.htm

SEC requests use the demo placeholder contact email contact@example.com. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxQNV9weHdjQ2hvRDBRNDMzS3d0djdfRTVJX1RVY0JmZU1mSE1mSTduMlMzQndBT1J3MnpSMG5tQXVQc0RORTVXb0xKc3ZwY0hvQTBMWTJVUGlCbmtXS1dTaGU5MGpoNlJuMlhxMW4yT2Q4SnBpcVIxSkg0dHIxTWExeEZFQnBJMGZfYzRtM05TbGhYczNvbE1oag?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOTll6bTBtUW1BNkdHTnhZbnBEV3NfVXJoN1lfY1JRRkZabC1hQVVVTkUwY19DSlFWNm9LOXdjOS02YXZLUVZUbW5YVnE0N3pORFpyaWxMSU5iSm9wNnV5SWlQZzQyd0NZWnRZZVFldWQ0Z0NQNUZ3cG42eHpzRWRVZFBBamhTQnFrRDZlWVd5bnBqWF84dzVYOS1tUnM?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPcGN0YW5aWG5QSkk3RlYyTEZFYVlEUGxsTnJ0LV9tLTdaVkJCczBudHl2T0FpdmhJclNSY0h0VlU2NTBneC1PSlpqa2ZYV2kzQUdjd1NqTElfVHFYQzRhV3pORGtxN2x3TGZMWDM0UnpLZkswbmd5WWcxUUl3ZFVrbEtOVkREdDhCeXBOamlyMm9HVE5xcUQ2YjR5X2tlQm40RVh5WmUzZE9SZw?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNWm5yS2ZOQW0xelJ4eVZxVzJST2J4eGU1SHRvd3pBNnFhbHk2QWZHM0FkeUd2S0Uzd0RabnZrWTdkcW1FYi1XUmE4dG1RYm5LSnFERXU3WGRMZVhXTEhNcVlNTHppc3diUUpjV2tZakViQ3V2N1BJVlNZWTBrVG83TEJYdmVKWXFKS0dSeEwxSDdUOHRsWDJ6d3VBWVJNZTF4RHNKTDFYeUNwbVdnMThzREpYcFJINWdBZVHSAb8BQVVfeXFMTUY4Z0RwX1RSOC1RVXVYc29laGZ4NnpXVTJiYVJYUjgxc0dGVnpkNmRMYUZKRVpKYkVsbkhDZjZlVXJlbVlnNl9MZ29UOHppZWFtRV9LeGRVYlJjdWF4NEpWbUxVV3Rxa3oxSWF0NTFoRzFmUUxnRXBCbmQxSmw0STIzWjNGSGg2SjFObmFKY2tXWkhqcjlaRjRaMUg4YkwwQTc1blBVWkkwOEJmd2F4TVQ2OThqNE1laFVxd0kydzg?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNSDRIN3ZWZDdwMVloTDlSVXhQQW9JTjV1RWd4V1F6M204RHp2N2ItbmUtUXc2WWcyVGVNU29BeTRzWFo1ZHJTeXFSTGhSN0xmUmVfUWYybHhrWHJNQlVnZEZaYWVRZ1hmZ0taN0E0Vlp4Q0NFQ2dMSk4taUFIc19NUDB5Q3I2Y2lnVHdHMTc3UUJzSG8zQ2EyaTdzQQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxNMDl0R0FDTnJiR05XQzg2OVVDekF2LWZ0MkhzLWMxVlpOYkZqS2I3clE4dTd1bmtGS1MxNzVGNFNfTHp0NkxSVEdvVEtfdllBNDktWGVONWNEVmlXMUtfeVlOd05jMlVVd095MTF3WW42c1l5SVFIcmxVWGlFRVN2bF9LTllRU1J6ejNzYzNaYTBpV29OVHNjaEMwQ01pSFpMSjNveEFOTGZRMU95YXpnNUsyQkRaVndiQ3lCRGJ3?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNUUlZcllmT1FXN0dkOVBnanNUdVZjMERvOEVOUkJwSHI4dk1IbDJEMW44SXVTckVkc3BkbGVXdUVXSmRUa3JUTE9mSFlPLUl2UG54bjdjMVZYdFBNWGhhZ3lfZ1N4dTZrWjdZQkVWaWxmV3Flb1E0cDY0d053SGxYNzliUWJnb2E1c2NIWHZ2dHA2dEl1?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOUEMwSzR4SUpZbHAwRnRGb3hMYVJsdzF5NXltVkphaHdIYTZkQ1lTdEI5a2Uydlo5SnNUSU5feFY4NHIzM2lQUXN5SWhTMWxNTVotSm5xZ2R2SGZUeXViRkVNdXJ6LVp0MDdRdWZXUFVaMTJQSWRobHlkMXBuQUNkT00xMUQ5cVowREZSN1E3OHRGR1U?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPd2JfRk9YNzBpRTFlNEVHWHB1OWZrSlNuV0t4NVNzY0xaS2hzTEJ4Y1Nabl9pYS1PRWxOT25YVVJ5bE9WMzdRZTkwcGIxMTd0WlJkVXpNY3Z4R0stZWJRQWRsX3dGMUtrSEZ3clZYcnpONzN4a3NEWExKMUozYXg3enZVQmxhUVhLckZBOTVmVThlTXBqTVowUkxkNGlPQnVCTjVIaEpaaW14UlZYOWdv?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNc01UT0FVeVNWVDZ4bXJsU1dZSmw2aUM2X05kYWh5aXh3R2Ffc3RvbDVBTVpjUHVFelh5eFdvMjAzT3lXb3pNQklQRWJsSkFHYXB0X245ZlpsS1R6UUhvVjVkTDJUWEVfdjN3bExSc0w1NFdpaVdpQVU4ZXF0RXdkbVJtclc0ZUlQZ1NjZFBWVklzY0VKc0l3b01GdDJyODJlZVhCbkQ1RjB3Y2J3WE85TU1hd0JCOUU4R0l2RXpQYTE4QTDSAcgBQVVfeXFMUDNiUGpKM082aXQ4QmhJeU5RY3ctMU5BVTZsZlgxWXY5aDhZVVVHR3RVMVFIb3RkMDhKMGRCUENfNngySTZvQ2ltX0lPbnRhV0haWXpUWFJtMDVsYzRRYVY3MFNYcUFITHE4ZlM0aE5mWUktNy10a1pzSmtRQ2pfTTJPUTFjV2tERlBrOHdONGJ1REUxd2ZrUHJ1QWkyZWNYbmpORTEtNmpXc1hyNXR5TVprUlRqbjhkNC1iWFUzM2YtLVB1OGlyS0k?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPeDcxYXVCUzI5ZVE3NXNfNVU1dmJEM05Rc1pmS3pYN3Jvdmt0ZnlZcVJqSXZSM1AxeDVIcndMMnZhbzRBSDFSVEVGWlFWNW5yY3ZMQ2JmZGRHcjBKVzNnbVo2NXlvLWk4RVZUdldaNndFWU5CYmM3U3NHMHVucXVxZ0VsbkZCemxndnJucjh3?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQSWtlUVNLQkdBTFVOdW9UdjJYNDFhZE5nbXhzRmQ4QTBZQ3RIZ1NMOGV4TWpYVVhmU1FRR0RBZks2U2l6WmhSUmlDMk1iX3c1aGZJcFEtXzBiRnRDQkJIdV8tMmFaSC1MZzVBSVM5ak1pSkFKYjhqQjRpZ0xPeTNac0ZrNGFEY1JsTGhaZjhYN3lNNXo1OW1wcV9n?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNcGhqTFJJWUJHdTJ4eUJjemFXbUpHS1dvWVdJWmZuTnlPd0NjWFo0cHl4RURyOHNUT01MMG1jTkM3aFJzRnNJOFdLRG5QcmxIODBpOHlBLVk2WVl6LTM4RE40WVRSdG1HOUpKVzNPTWgtWi1xa29QLThzVnpDSWxBWWh5cHdQRElZY0xmVWwwSDkxNzBwSkpBcGlXZVE?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNcVpmSHRvengwZ2o5QzBUcHNvV2pwMG1CR1RqTTUwRkR4S0p5WmZTNkthOTcxWHI5VnJCQ3IzeWdJRnhlNmFwdVU3dnF1SEEwcF9yMEQ1MUdtU1VSZV9aNVk0MkhFMzBoX0x2UG9uWWJXa0hNR0kxS2NmNjFTM1VhZlRPc0VCenJQREE?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQbWxFZW9BWFo1VnhlUFNDM3IyWXMxMzhEU1Zqcm5xUElxR1VVTzFQaEowMXVxSGs2MnJOSUI2OGhMOC1FaFpTaTFuTXZJWmVfQ21qeExHMmwtZl9QR2dKTlhtVlRvbGdDTXcxeTY4bXlwNnFYSkNGUWZKc0k4MHBJNkc5eV9ER3I4X2dBUFFodGVKZWVBQzAzT21jNTA?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxNdFdnVGktX0tBWkN0Zjd4WGt5LUpiM1IxN29ZQmdKZG1CSWMwV2ZaSjFRSXRJcVZtcG5KNVJSa2FTRm5xczdOeUZQUDBQeHg5d0pXMEFjdmgyb1FNOUZWR1phMW5EU0UzRmlteVBnVXV6NnFJTU40MXJvSnF1eXB2ak1tczJTWmQtVlZrb2FOWlk3dkVtX05Qck55aEROU1JDSzM0cG1CX3NnckZ2N21CSjl1OHRUdw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNbml3UVFvME5TTnFKMnJkYURzSTBCYjBiZ3lCV2pKdTFfR1o5Sll2X2FISmduZTNhRGViRGpYR1VXU0JnSlpiUlBPZjRibWQ1UFhRTjcwXzlJN19CaUtBczdmSDFNRmw3cGdkLS1fbnJZQ19mSjRHbldBb3k4UzdEa1ZPR2haVGlCWWlCa01fVlN1SGc?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNU184LW1KSmNBT0ZtVlBDTlU4QjFjUHBwSUVvRjIwSzVUTVVEWFQ2QnQ1OUNMQzNEUUJVa3RKc0FlRklFQ09SaXprU0RIUmI2Q0pMS3d1UVR6WHp6MjVROFJGTnltS2dDLThCU2ZrTVpodU9WR3RiQWdVSW5WVERNTTdaQTg1LUljbUFraFJwTTRXdmFQb1RnbVNKUDVVSUZZXzBwdGR5dGJUVU0?oc=5

## Demo notes and limitations

- Multi-ticker local demo; AI items require human spot checks; RSS coverage is not guaranteed.
- Free-tier Gemini grounding (google_search tool) returned 429; the demo uses Google News RSS + plain-text AI extraction.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
