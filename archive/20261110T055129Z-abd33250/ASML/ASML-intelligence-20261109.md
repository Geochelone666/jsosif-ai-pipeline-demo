# ASML Intelligence Report

- ticker: **ASML**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/ASML/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ASML/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T05:58:34.099532+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 4, 'ai': 11, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/ASML** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 10 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 36.36%; oldest publication 2026-11-03

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1513.2500 |
| Return 1D (%) | 6.2116 |
| Return 1W (%) | -0.8446 |
| Return 1M (%) | -14.8901 |
| Return YTD (%) | 42.3107 |
| Return 1Y (%) | 49.7134 |
| Annualized volatility (%) | 48.7595 |
| Beta vs SPY | 2.2604 |
| Max drawdown (%) | -31.6292 |
| Sharpe (rf=0) | 1.0338 |
| Downside deviation (rf=0, %) | 32.9187 |
| Sortino (rf=0) | 1.5312 |
| Historical VaR 95% (1D, %) | 4.7437 |
| Historical ES 95% (1D, %) | 6.4916 |
| Correlation vs SPY | 0.6347 |
| Tracking error vs SPY (%) | 41.4420 |
| P/E (trailing) | 37.24 |
| P/B | 1299.35 |
| EV/EBITDA | 1989.76 |
| Revenue growth (%) | 55.20 |
| Forward P/E (estimate) | 23.87 |
| Gross margin (%) | 54.34 |
| Operating margin (%) | 44.36 |
| Return on equity (%) | 65.64 |
| Free cash flow yield (%) | N/A |
| MA50 | 1671.7961 |
| Close vs MA50 (%) | -9.4836 |
| MA200 | 1596.4419 |
| Close vs MA200 (%) | -5.2111 |
| RSI (14, Wilder) | 43.0579 |
| MACD (12,26) | -66.5656 |
| MACD signal (9) | -51.2891 |
| MACD histogram | -15.2765 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ASML': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1513.2500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 6.2116 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.8446 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -14.8901 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 42.3107 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 49.7134 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 48.7595 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 32.9187 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.5312 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.7437 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.4916 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6347 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 41.4420 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.2604 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -31.6292 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0338 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.8686 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3370 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.3560 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 65.6360 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 37.2355 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.0579 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -15.2765 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.4836 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -5.2111 -> Clearly below the moving-average trend level.

## TAILWINDS

### ASML Raises 2026 Guidance as AI Demand Accelerates Capacity Expansion
- Summary: ASML Raises 2026 Guidance as AI Demand Accelerates Capacity Expansion
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNcjI2cTBhSXUwVW5rMnZpZWgxamluLV9IaGFZU1l2OVRWb1liUl9HT0Z6WE9sd1FNZHZiTTRmZ1cydTI5U19ULXFWbDVuRzRHX2lGS0V3eDM1d1A0VDc4STVCdFkxcnNrcFEtUlJxTDhtdV8xbUZhVEpSeUZBaWxpMmNhRE9yd1V1MnhaN1JzSk1XMTA?oc=5>

### ASML Stock In Focus As EUV Machine Orders Stretch Into 2030
- Summary: EUV machine orders projected to extend into 2030, indicating sustained demand for ASML’s advanced lithography equipment.
- Date: 2026-11-06 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPYXZuNWI5TzU5R0hjNjZlcnQ4ejRVUU0tdnNQbWFYc0Q3cmxLbzZmLTBUTW5GTFB4WmVXbm9rdTQ3by1sUnJkcDZobmdtT0RqYV9uM3FlSVVJUWRhWG4xdFZXLUFuVnE1Z2c0TkEyUmhqR1BySHUyN0hsRjhlWlpqTExGQ2dmVmMzNldXVHctS2FKYW0wX0xyLQ?oc=5>

## HEADWINDS

### ASML Falls 20% in the Past Month as AI Growth Meets Execution Risk
- Summary: ASML Falls 20% in the Past Month as AI Growth Meets Execution Risk
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOR1otbFFTYXl3Uml2cVNoLUdsNnVSd2Nvc08yWUdUd0lCdTdEamdZNUxjWmVEUllVSXNYUzE5cV9WRXlBZWRvdkdZeEVwTnJFdEFQSk9jYWxYb2pUQ21HX1ZndXdiLTN0UndHekRUd3FGQi1vckN6b2pfYmRfMllUejNER2JXRmNqUGVSYzN0NGdhOEU?oc=5>

### ASML Holding NV (ASML) Stock Down 3.6% but Still Overvalued -- G
- Summary: ASML Holding NV (ASML) Stock Down 3.6% but Still Overvalued -- G
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNY01YMjFXQktxVzU3b2JOaFBvdkw2Rmx5OG8xeXllOS0wSG5qMWFrcnZXYjMzME1qNWlRZml2T0dqdWxaZ3lDdE5Qb2tPY25MUHcxNGR2NTdOMXMweTdsLV9ZYTNCREo3VDlyX2dxeDhadk9oaGZxaXZyVTA3UmF4Sng0RFlrb2J2dFlvV3Vha2FMS1l1NFl0RG1McS1QVjdyb01yOW1vcTNxalBsR2c?oc=5>

### Why is ASML stock sliding today?
- Summary: The stock slide reflects short-term market volatility, possibly due to broader tech selloff.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPN28tclFtYlBLTjNOTkJyVlV1TUdGWl9Jd3o3d0t2dVZVTWdEZjlxRGo1dkpROFptS1YzcWhoMnFjQWl1cUp4OUU4R0ZpUlc4WnFWRl80dld4cVhxZHFvdE5aUFplbkhURlhLdVV1U3JXRVJydnJZVG8tZ0dyZDRYeG9NYzJLVU40d3pEcEItMWdCdVV4S08wSQ?oc=5>

### ASML Holding NV Stock (ASML) Moved Down by 6.67% on Nov 5: Facts Behind the Movement
- Summary: A 6.67% drop on Nov 5 signals a significant short-term decline in ASML shares.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOZjNGVDd6Qk9HTmZCTERmQVBHdHNIVlVLUkc5Zy1hM0hjTE0xT2p5cG5SUXZONEo5ZlYydmlKdWNXR2FBVktKM1dEcmFKRVJLcm1hSndnTkZ4bHdERU9uS2d4c2s3RXZDZTRvR1B6ZmY4Q3Y1VGlrR0NpUTJBWi1GMGdrN1JBZ2pXUjIw?oc=5>

## CATALYSTS

### ASML reports transactions under its current share buyback program
- Summary: ASML reports transactions under its current share buyback program
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQSUlwam1lNlI4MVFZR002V0VqZG9iSVU2VDdhWXYxSzNxWUFVY3NJRzFkUzd2NGVaLXhwY0k2bGpCd0ZtaHVtMkZhbEV1d1JCWE5mVnlJQi1oSHM0MGlKWk1udkJ1MlUwNGh4SkltS2tYSTRQZ0t5alNpN2owdDM5VEdwSXpaUDZFSmhpNEktVjFLM1ZNUFFDdTUxTnlURVlmVEE1dGNjdHBVdEw2eW1WRVRB?oc=5>

### ASML Surges 48% in the Past Year: How Should You Play the Stock Now?
- Summary: ASML’s stock rose 48% last year, prompting investors to consider buying opportunities.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNcTdqYkRtLXJsLVFSMVFrbDJ0NTlsT2VHLWp2OVJFekFPN0ZEQnBVdGJMOEVfRUFYbXU0Rkp4SWM5dHJhbVN5cUhVS0hzRjItbFJGa01BNHdBajFkRnd4WmJ6ZTQxc0h5RzJOaWZ2aHktQUhSalhYUUZfNVZDQUNFblp3ZTQ0clhESy1tMnJBaUhROW8?oc=5>

### ASML Holding NV Stock (ASML) Moved Down by 3.09% on Nov 4: What Signal Does It Send?
- Summary: ASML shares fell 3.09% on Nov 4, indicating possible short-term weakness.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNRzMwdHE3emJ6TjdvNXE4UDBnWmRzbEhSLWVsZWJIakgzZFM4aWYwZ2FwNnZ2ckFaQkdBZWRHVE1YN3R0UkFiOC1uNE1pNkRXeDZtcmZwNTVYQTFDZ2lpbDBMRWRNRjNmYnVRQnRCeFV0dGFpekx1SVVyaTg4N0I0RHdpVDFDWEl4VzFv?oc=5>

### ASML Holding NV Stock (ASML) Opened Up by 3.10% on Nov 3: A Full Analysis
- Summary: ASML shares opened 3.10% higher; analysis covers recent performance.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOWGpidnZXdlJpWV9qbmFtOE50Z055cGEwYUR0b1AxcGd4U2pCTlVocU5mS3ZFUmFWaTd2anRFVVJFS2p2ZV9FX1Vna0RNUWEtN2VsT3Iya1h2cGhJMzRKXzNTeXk5OXRhUnlRbzd2U2hMc3ZqTzk0aFdSOUlXbmVDVU8yV2l1cElPb1hF?oc=5>

### Why ASML Holdings Fell in October
- Summary: ASML shares dropped in October due to market volatility and sector rotation.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPZXlUOGlTU0NidTJteW95YnhwS1dwODlaR3VSVkNUVm5hU3NHcFJhWDFIN3ZtWGpMNWIta3V3OU9zQmNkcjY0dmtnamNFeUIzWlhOSHdEeldRV0U0dHdfdHdCYW9zN0JuYzJjT1BvaTRoYmY2enJoLWdHMXR1YXB6bkJySmlrZU9QZGUzMFB5T19hUTZEUnQwSk9SWQ?oc=5>

### Why ASML Bounced Back Today
- Summary: ASML shares recovered today after a dip, driven by positive analyst coverage.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPODlhWk1sTmpvU3g5VlVXMXRoSWRGRnJNWWhPZ0U5UnFxVXVxNUV4eGt5Yk9hUmJnNGd3MzdyM2h6Sk9NUlBBbXo0Z1dxa3ozUVNnZ2d5M0o0QVZGRjFXMllUYWpQM2dmdUxlOUZOUlpZSHRWb1dZNElJcy1HMHY3dDJ6dzlUdjVLNDlBcWxYRW9vUHRWZ0Nn?oc=5>

### Why is ASML NV ADR stock surging today?
- Summary: ASML ADRs surged today following favorable earnings guidance and product launch news.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNQUtCYWN1cC0zenNRSEdqaXNpZ01mTGNFTG0yZlJpTHExMmNJUHVBenM2VUNJcnMtUlZMN3UtLTdVdW83dzNCdjBKX0ZGMjhjcnlMTFRaRmk0eEhxM3VYdS1SWW5aS2lHYUVTRm16MUg1bW5xOHpFcnZwaXE0cnE4dHVTSjBjSFdYUHBPTDQwQVo2OHNZUElsZS1NNm1vLVRET1E?oc=5>

### ASML Holding NV Stock (ASML) Moved Up by 6.12% on Nov 9: Key Drivers Unveiled
- Summary: ASML stock rose 6.12% on Nov 9, driven by strong earnings and product demand.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.92
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxObndWMC03WmxrTkpGUTdVZ1phdWxvelRCVzBqVVNhc3AxWGljdnd5SVF4QTdpTzBIaTFmeHgzemRqek5LcHY0REs4SDFURUFFS2ZzajFCdUFSWTkySWE3SjhGZVM1NTZuQmpDQk45eDVWVE1zcEdscUoxX2h0U3htUkZLc2RtS0ZsNDFZ?oc=5>

### Applied Materials Jumps 11% Ahead of Earnings; Lam Research Surges 9%, ASML Rises 6%
- Summary: ASML shares rise 6% in market reaction to sector moves.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcjFldU84UWg4b21Nd1pyd2VsaXlDaWhDRUk3THdxQ0xtTGZpWkUyYnpwRnYyNDFZbk1FSDQwcTZhaXlmQmNJY0x6cDF3QkhWdnNLUkc3dnc1eGZYUXotUFpGN2QxSC1sVVlQWXZ5YVJDZzUtcVlzZWdYWWR2NDlIOFFiRWwzMTNqclJLSDJQOFNjajJ5NVJVQjZLX3preUgwNHN2R2FOMlNITGwybGJZckFhQmxVQUJmSVJxc0Y5dmk?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ASML** | **37.24** | **1,299.35** | **1,989.76** | **55.20** | **583,233,372,160.00 USD** | **49.71** |
| AMAT | 31.97 | 11.48 | 28.77 | 24.80 | 294,067,535,872.00 USD | 61.95 |
| LRCX | 32.98 | 19.88 | 26.96 | 54.40 | 276,454,014,976.00 USD | 39.52 |
| KLAC | 37.94 | 30.25 | 30.17 | 28.90 | 197,242,454,016.00 USD | 27.54 |

Peers fetched as_of: 2026-11-09; ASML reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-14
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikwFBVV95cUxNcjI2cTBhSXUwVW5rMnZpZWgxamluLV9IaGFZU1l2OVRWb1liUl9HT0Z6WE9sd1FNZHZiTTRmZ1cydTI5U19ULXFWbDVuRzRHX2lGS0V3eDM1d1A0VDc4STVCdFkxcnNrcFEtUlJxTDhtdV8xbUZhVEpSeUZBaWxpMmNhRE9yd1V1MnhaN1JzSk1XMTA?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPYXZuNWI5TzU5R0hjNjZlcnQ4ejRVUU0tdnNQbWFYc0Q3cmxLbzZmLTBUTW5GTFB4WmVXbm9rdTQ3by1sUnJkcDZobmdtT0RqYV9uM3FlSVVJUWRhWG4xdFZXLUFuVnE1Z2c0TkEyUmhqR1BySHUyN0hsRjhlWlpqTExGQ2dmVmMzNldXVHctS2FKYW0wX0xyLQ?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOR1otbFFTYXl3Uml2cVNoLUdsNnVSd2Nvc08yWUdUd0lCdTdEamdZNUxjWmVEUllVSXNYUzE5cV9WRXlBZWRvdkdZeEVwTnJFdEFQSk9jYWxYb2pUQ21HX1ZndXdiLTN0UndHekRUd3FGQi1vckN6b2pfYmRfMllUejNER2JXRmNqUGVSYzN0NGdhOEU?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNY01YMjFXQktxVzU3b2JOaFBvdkw2Rmx5OG8xeXllOS0wSG5qMWFrcnZXYjMzME1qNWlRZml2T0dqdWxaZ3lDdE5Qb2tPY25MUHcxNGR2NTdOMXMweTdsLV9ZYTNCREo3VDlyX2dxeDhadk9oaGZxaXZyVTA3UmF4Sng0RFlrb2J2dFlvV3Vha2FMS1l1NFl0RG1McS1QVjdyb01yOW1vcTNxalBsR2c?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPN28tclFtYlBLTjNOTkJyVlV1TUdGWl9Jd3o3d0t2dVZVTWdEZjlxRGo1dkpROFptS1YzcWhoMnFjQWl1cUp4OUU4R0ZpUlc4WnFWRl80dld4cVhxZHFvdE5aUFplbkhURlhLdVV1U3JXRVJydnJZVG8tZ0dyZDRYeG9NYzJLVU40d3pEcEItMWdCdVV4S08wSQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOZjNGVDd6Qk9HTmZCTERmQVBHdHNIVlVLUkc5Zy1hM0hjTE0xT2p5cG5SUXZONEo5ZlYydmlKdWNXR2FBVktKM1dEcmFKRVJLcm1hSndnTkZ4bHdERU9uS2d4c2s3RXZDZTRvR1B6ZmY4Q3Y1VGlrR0NpUTJBWi1GMGdrN1JBZ2pXUjIw?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQSUlwam1lNlI4MVFZR002V0VqZG9iSVU2VDdhWXYxSzNxWUFVY3NJRzFkUzd2NGVaLXhwY0k2bGpCd0ZtaHVtMkZhbEV1d1JCWE5mVnlJQi1oSHM0MGlKWk1udkJ1MlUwNGh4SkltS2tYSTRQZ0t5alNpN2owdDM5VEdwSXpaUDZFSmhpNEktVjFLM1ZNUFFDdTUxTnlURVlmVEE1dGNjdHBVdEw2eW1WRVRB?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPd3FYZ3dxbnh0dmlBdy1XY0o4ZXRPNVJDcWQ4Si1zS095VW1HQXpQY2I1eGtyY1RNSWoyVjRKd19HZlFQeTBUMHJTRHBUYkxuNkFUVHZqM2c5Z0E4VG03SFo5WWI4ZDFUM0tYeGRLRThGMmtEVjI3b1JqZEd0aGw1WldfYWhxYkRFQUNCWGRtMWktb2JTT050SXNjQkh1WnRiM0RHYjlCaw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNcTdqYkRtLXJsLVFSMVFrbDJ0NTlsT2VHLWp2OVJFekFPN0ZEQnBVdGJMOEVfRUFYbXU0Rkp4SWM5dHJhbVN5cUhVS0hzRjItbFJGa01BNHdBajFkRnd4WmJ6ZTQxc0h5RzJOaWZ2aHktQUhSalhYUUZfNVZDQUNFblp3ZTQ0clhESy1tMnJBaUhROW8?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNRzMwdHE3emJ6TjdvNXE4UDBnWmRzbEhSLWVsZWJIakgzZFM4aWYwZ2FwNnZ2ckFaQkdBZWRHVE1YN3R0UkFiOC1uNE1pNkRXeDZtcmZwNTVYQTFDZ2lpbDBMRWRNRjNmYnVRQnRCeFV0dGFpekx1SVVyaTg4N0I0RHdpVDFDWEl4VzFv?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOWGpidnZXdlJpWV9qbmFtOE50Z055cGEwYUR0b1AxcGd4U2pCTlVocU5mS3ZFUmFWaTd2anRFVVJFS2p2ZV9FX1Vna0RNUWEtN2VsT3Iya1h2cGhJMzRKXzNTeXk5OXRhUnlRbzd2U2hMc3ZqTzk0aFdSOUlXbmVDVU8yV2l1cElPb1hF?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPZXlUOGlTU0NidTJteW95YnhwS1dwODlaR3VSVkNUVm5hU3NHcFJhWDFIN3ZtWGpMNWIta3V3OU9zQmNkcjY0dmtnamNFeUIzWlhOSHdEeldRV0U0dHdfdHdCYW9zN0JuYzJjT1BvaTRoYmY2enJoLWdHMXR1YXB6bkJySmlrZU9QZGUzMFB5T19hUTZEUnQwSk9SWQ?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxNbmpJNTZhaWVFTXlvendJVXotM2VCSHVNNHh5YzNiTl9kcF9pb0E0UEJPdV95cHVfbWFpZEZJZk1IVWMtcERsNXdUR0lrSEczWWtSdHU4YmR5Z3NIQnpzbnB3QzRFNFdNRXRxaG84ZXZmMUEzcnJnSFl5bHdYekEzMUN3?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPODlhWk1sTmpvU3g5VlVXMXRoSWRGRnJNWWhPZ0U5UnFxVXVxNUV4eGt5Yk9hUmJnNGd3MzdyM2h6Sk9NUlBBbXo0Z1dxa3ozUVNnZ2d5M0o0QVZGRjFXMllUYWpQM2dmdUxlOUZOUlpZSHRWb1dZNElJcy1HMHY3dDJ6dzlUdjVLNDlBcWxYRW9vUHRWZ0Nn?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNQUtCYWN1cC0zenNRSEdqaXNpZ01mTGNFTG0yZlJpTHExMmNJUHVBenM2VUNJcnMtUlZMN3UtLTdVdW83dzNCdjBKX0ZGMjhjcnlMTFRaRmk0eEhxM3VYdS1SWW5aS2lHYUVTRm16MUg1bW5xOHpFcnZwaXE0cnE4dHVTSjBjSFdYUHBPTDQwQVo2OHNZUElsZS1NNm1vLVRET1E?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxObndWMC03WmxrTkpGUTdVZ1phdWxvelRCVzBqVVNhc3AxWGljdnd5SVF4QTdpTzBIaTFmeHgzemRqek5LcHY0REs4SDFURUFFS2ZzajFCdUFSWTkySWE3SjhGZVM1NTZuQmpDQk45eDVWVE1zcEdscUoxX2h0U3htUkZLc2RtS0ZsNDFZ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcjFldU84UWg4b21Nd1pyd2VsaXlDaWhDRUk3THdxQ0xtTGZpWkUyYnpwRnYyNDFZbk1FSDQwcTZhaXlmQmNJY0x6cDF3QkhWdnNLUkc3dnc1eGZYUXotUFpGN2QxSC1sVVlQWXZ5YVJDZzUtcVlzZWdYWWR2NDlIOFFiRWwzMTNqclJLSDJQOFNjajJ5NVJVQjZLX3preUgwNHN2R2FOMlNITGwybGJZckFhQmxVQUJmSVJxc0Y5dmk?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
