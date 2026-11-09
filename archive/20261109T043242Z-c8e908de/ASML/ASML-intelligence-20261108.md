# ASML Intelligence Report

- ticker: **ASML**
- Report as_of: **2026-11-08**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/ASML/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ASML/key-statistics/
- AI analysis snapshot as_of: **2026-11-08**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-09T04:45:04.142328+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 1, 'ai': 11, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **16** exact headline/source/date matches; prior report **20261108T041758Z-43fb2458/ASML** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'directional_claim_without_event_type': 2, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 13 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 17.39%; oldest publication 2026-11-01

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1424.7500 |
| Return 1D (%) | 5.0197 |
| Return 1W (%) | -9.0140 |
| Return 1M (%) | -22.2164 |
| Return YTD (%) | 33.9879 |
| Return 1Y (%) | 39.2813 |
| Annualized volatility (%) | 48.3445 |
| Beta vs SPY | 2.2379 |
| Max drawdown (%) | -31.6292 |
| Sharpe (rf=0) | 0.9294 |
| Downside deviation (rf=0, %) | 32.8747 |
| Sortino (rf=0) | 1.3667 |
| Historical VaR 95% (1D, %) | 4.7389 |
| Historical ES 95% (1D, %) | 6.4916 |
| Correlation vs SPY | 0.6272 |
| Tracking error vs SPY (%) | 41.2191 |
| P/E (trailing) | 35.06 |
| P/B | 1223.36 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 55.20 |
| Forward P/E (estimate) | 22.47 |
| Gross margin (%) | 54.34 |
| Operating margin (%) | 44.36 |
| Return on equity (%) | 65.64 |
| Free cash flow yield (%) | N/A |
| MA50 | 1675.4096 |
| Close vs MA50 (%) | -14.9611 |
| MA200 | 1595.7786 |
| Close vs MA200 (%) | -10.7176 |
| RSI (14, Wilder) | 34.7306 |
| MACD (12,26) | -69.8887 |
| MACD signal (9) | -47.4699 |
| MACD histogram | -22.4188 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ASML': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1424.7500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 5.0197 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -9.0140 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -22.2164 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 33.9879 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 39.2813 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 48.3445 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 32.8747 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3667 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.7389 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.4916 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6272 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 41.2191 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.2379 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -31.6292 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9294 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.4727 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3370 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.3560 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 65.6360 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 35.0578 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 34.7306 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -22.4188 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -14.9611 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -10.7176 -> Clearly below the moving-average trend level.

## TAILWINDS

### ASML Stock In Focus As EUV Machine Orders Stretch Into 2030
- Summary: EUV machine orders projected to extend into 2030, indicating sustained demand for ASML’s advanced lithography equipment.
- Date: 2026-11-06 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPYXZuNWI5TzU5R0hjNjZlcnQ4ejRVUU0tdnNQbWFYc0Q3cmxLbzZmLTBUTW5GTFB4WmVXbm9rdTQ3by1sUnJkcDZobmdtT0RqYV9uM3FlSVVJUWRhWG4xdFZXLUFuVnE1Z2c0TkEyUmhqR1BySHUyN0hsRjhlWlpqTExGQ2dmVmMzNldXVHctS2FKYW0wX0xyLQ?oc=5>

### ASML Holding N.V. (NASDAQ: ASML): Record Financial Performance, Accelerating EUV Demand, and Expanding AI-Driven Growth Opportunities
- Summary: Record earnings and expanding AI demand boost ASML’s growth prospects.
- Date: 2026-11-06 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi9wFBVV95cUxPWm8yeUhBMlg5RFlFQmwtLUF4ekQ4cXFXWUNOeVAtbV82QXQ0bGpkU2VLWTh2aTJ1Z0lZeE8tTmNHRURuY2gteGFYQ2xIUkN1cUJDOTJ0dnFsS3VvLW5OYmFMTXdZWDdXT2lVdk13SUhjcU9ISTJpRThkenNCYmFrc0tkX2t4dF96NHJTQzBPUExoMnVjeFZWWGszQXhoLUhFNEFzS0FWdVZxcUdlREp6OW9SV2IzUmpHVVh0LTZNYmk2VWt4STFLeHJUckFQcjg4ejkyRzVwc3JHcncxNFAweDQ2MkdzY012THZvZ2ZscnZWNVgydzhV?oc=5>

## HEADWINDS

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

### Is ASML Holding (NasdaqGS:ASML) Too Expensive After Its 118% Climb?
- Summary: ASML’s stock has surged 118%, raising concerns about overvaluation.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxNVExoVnVaSHhzM1cwUkw0clhzVjRtbGYxUTFuNmxXNnFIS1RBVldGUW5hZ0hINGhEdnVQMWd2TmRrUDV1Vk1mOWJHZ2FwYUVvek9LY2M1WUhJOUVBYW45aERfcHdSQ0dYMUE1QXBudHRqaFJ4d0lVelAtVnRzb19uVEcwMUs1bDJGTFpTQWtwdHZpazU3dWhnOV9URVJxdFMwd0h5MW5YOFlXTG54QXJ0TnlOZUIyUzc2ajN2UGtraVZjNW1mWS1WY2ZYLXRFaXp0cDVn0gHYAUFVX3lxTE1Xc2tXTkJHeUFJN2Z3eE8zZEVZakV3ZVJWRjhiZEZoYUNNeS00RllXUVVaV3k2MVhjNXYzN0RrM2Y3RGRDU1dJWEdwYTZKOVhwcDlxbXdkbk5XU0NoZ3BFMnpmMlN5ZTUxRWZheTNzVjFNWkc2WF9FbzRfZ2hCSy1xMEo2VVg2eWxkclduWW9aeG4weUEyazM1MTU5Slh1azQtZWNDMGIzVm9vMmcwbFY0ejVfQnU1ZnhPQlFwOEZOLXltVUxoS2pfWndHXzhycm9hUnNnc3hYMg?oc=5>

### Missed ASML's Run? What Holders Had To Believe
- Summary: Investors questioned ASML's recent performance, suggesting skepticism about future gains.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPVVhPUnN1cWxIek5NNnR1YkFnc2ZlN2p5WWx3NjZvdkxOb1h0aDJVTVF1Mm1EcGFBamZKbEpibFJ4TDBUUlBpU1BXVy1YNlNKbGxZaVBxb2V2LXZGdVNqck51STN6ZmdiQ3RhSGNUOXVOcjNDSEQtcklRTTFReWpfS1Q3QlZkYVdVVmh4QV9sSm9PNGNoQWQtSzg4YlVpUElIb3lPZXdYcVloamJDNi1HZ05GOGc4MmJDYlhmTHlGcTBqVWPSAcgBQVVfeXFMTjFVaF9mRVJSRm5OazdQUEJDYWtINllyaWJidGFSOFNLN0ZRM0xLdXNVNTlKcEUwbjlCcHVlN01oUW5YaHdTUnJfbEZPbWV0c1hVa3VieEstZDN1RUdxTDFqaHNCNnhyZ0otY0tGQ2g3RE5QVUR5d3NfSlpxdk1BUVRqV0ZFTnRORFVmVVJIdkthZUYyT1lmUm5ZRmhFZXhnWktvN3g4cVVzY1d4LU0wVGVKa0U3U0JPM3FHM01qTUZHVmtzWGwydi0?oc=5>

## CATALYSTS

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

### Will EUV Orders Through 2030 Change ASML's (ENXTAM:ASML) Narrative
- Summary: EUV orders projected through 2030 could reshape ASML’s growth narrative, indicating sustained demand for advanced lithography technology.
- Date: 2026-11-07 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxNS3dWeDZ2Uk5HcEoxdUh1MXdDTl9Lb0FaMkFFSXAwUnB3RjJYZUwwT2ZHaThYbVZsTjZzb2VJRXUtbEgxd08tTnI5dVlvT0tpbjBETEFYVXpta09YQzk2MG9iUXFUalN1NHN2OFN6MG8tbEo4R2MtNkNrbUhtSXY4M2NiMGZVZHF0a1ZOS1JnRlRkR1praHl2aFoyTnlTUVBVbHRVdEdkaHJqUkg5SHM0ZXRxOWRkR0lhR2JpVHBCUkxISllCaWFMNDd5NVN3RjZKd2lqTlUyamLSAd4BQVVfeXFMTm5MOVJOWUZGUHY3VGtEYUNfd0xKNjdhclJjdjJFNTVqY0lRVnFJWnM5TDk0YWoyenprdi1ab0k3MDV4UzBGaXFoZGpQcXlhQ3B0WmVGdEV3eUJPSkNIQi1rWVdnYmIwQkJlcHRDeEVZT08tV3VmdTFRdkUyNXlxdDdZdHpfcTUwVjhmNkd5Rnc4UnVpbkRZeVY2MkJlSVUzcWNsakljanVDYWNjb1N6M0pCSHNnVHU1MG0tZUU5bHI4ODhJb3FoUG9sNWtQNDNPX1ZjNzhRQ3BFZFlsc0tn?oc=5>

### Why ASML Holdings Fell in October
- Summary: ASML shares dropped in October, likely due to market concerns.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPZXlUOGlTU0NidTJteW95YnhwS1dwODlaR3VSVkNUVm5hU3NHcFJhWDFIN3ZtWGpMNWIta3V3OU9zQmNkcjY0dmtnamNFeUIzWlhOSHdEeldRV0U0dHdfdHdCYW9zN0JuYzJjT1BvaTRoYmY2enJoLWdHMXR1YXB6bkJySmlrZU9QZGUzMFB5T19hUTZEUnQwSk9SWQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ASML** | **35.06** | **1,223.36** | **N/A** | **55.20** | **549,123,915,776.00 USD** | **39.28** |
| AMAT | 28.71 | 10.30 | 25.82 | 24.80 | 264,041,775,104.00 USD | 43.26 |
| LRCX | 29.87 | 18.00 | 24.38 | 54.40 | 250,383,826,944.00 USD | 24.15 |
| KLAC | 34.71 | 27.67 | N/A | 28.90 | 180,447,281,152.00 USD | 15.42 |

Peers fetched as_of: 2026-11-08; ASML reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-14
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-08

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

- https://news.google.com/rss/articles/CBMimAFBVV95cUxPYXZuNWI5TzU5R0hjNjZlcnQ4ejRVUU0tdnNQbWFYc0Q3cmxLbzZmLTBUTW5GTFB4WmVXbm9rdTQ3by1sUnJkcDZobmdtT0RqYV9uM3FlSVVJUWRhWG4xdFZXLUFuVnE1Z2c0TkEyUmhqR1BySHUyN0hsRjhlWlpqTExGQ2dmVmMzNldXVHctS2FKYW0wX0xyLQ?oc=5
- https://news.google.com/rss/articles/CBMi9wFBVV95cUxPWm8yeUhBMlg5RFlFQmwtLUF4ekQ4cXFXWUNOeVAtbV82QXQ0bGpkU2VLWTh2aTJ1Z0lZeE8tTmNHRURuY2gteGFYQ2xIUkN1cUJDOTJ0dnFsS3VvLW5OYmFMTXdZWDdXT2lVdk13SUhjcU9ISTJpRThkenNCYmFrc0tkX2t4dF96NHJTQzBPUExoMnVjeFZWWGszQXhoLUhFNEFzS0FWdVZxcUdlREp6OW9SV2IzUmpHVVh0LTZNYmk2VWt4STFLeHJUckFQcjg4ejkyRzVwc3JHcncxNFAweDQ2MkdzY012THZvZ2ZscnZWNVgydzhV?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNY01YMjFXQktxVzU3b2JOaFBvdkw2Rmx5OG8xeXllOS0wSG5qMWFrcnZXYjMzME1qNWlRZml2T0dqdWxaZ3lDdE5Qb2tPY25MUHcxNGR2NTdOMXMweTdsLV9ZYTNCREo3VDlyX2dxeDhadk9oaGZxaXZyVTA3UmF4Sng0RFlrb2J2dFlvV3Vha2FMS1l1NFl0RG1McS1QVjdyb01yOW1vcTNxalBsR2c?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPN28tclFtYlBLTjNOTkJyVlV1TUdGWl9Jd3o3d0t2dVZVTWdEZjlxRGo1dkpROFptS1YzcWhoMnFjQWl1cUp4OUU4R0ZpUlc4WnFWRl80dld4cVhxZHFvdE5aUFplbkhURlhLdVV1U3JXRVJydnJZVG8tZ0dyZDRYeG9NYzJLVU40d3pEcEItMWdCdVV4S08wSQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOZjNGVDd6Qk9HTmZCTERmQVBHdHNIVlVLUkc5Zy1hM0hjTE0xT2p5cG5SUXZONEo5ZlYydmlKdWNXR2FBVktKM1dEcmFKRVJLcm1hSndnTkZ4bHdERU9uS2d4c2s3RXZDZTRvR1B6ZmY4Q3Y1VGlrR0NpUTJBWi1GMGdrN1JBZ2pXUjIw?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxNVExoVnVaSHhzM1cwUkw0clhzVjRtbGYxUTFuNmxXNnFIS1RBVldGUW5hZ0hINGhEdnVQMWd2TmRrUDV1Vk1mOWJHZ2FwYUVvek9LY2M1WUhJOUVBYW45aERfcHdSQ0dYMUE1QXBudHRqaFJ4d0lVelAtVnRzb19uVEcwMUs1bDJGTFpTQWtwdHZpazU3dWhnOV9URVJxdFMwd0h5MW5YOFlXTG54QXJ0TnlOZUIyUzc2ajN2UGtraVZjNW1mWS1WY2ZYLXRFaXp0cDVn0gHYAUFVX3lxTE1Xc2tXTkJHeUFJN2Z3eE8zZEVZakV3ZVJWRjhiZEZoYUNNeS00RllXUVVaV3k2MVhjNXYzN0RrM2Y3RGRDU1dJWEdwYTZKOVhwcDlxbXdkbk5XU0NoZ3BFMnpmMlN5ZTUxRWZheTNzVjFNWkc2WF9FbzRfZ2hCSy1xMEo2VVg2eWxkclduWW9aeG4weUEyazM1MTU5Slh1azQtZWNDMGIzVm9vMmcwbFY0ejVfQnU1ZnhPQlFwOEZOLXltVUxoS2pfWndHXzhycm9hUnNnc3hYMg?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPVVhPUnN1cWxIek5NNnR1YkFnc2ZlN2p5WWx3NjZvdkxOb1h0aDJVTVF1Mm1EcGFBamZKbEpibFJ4TDBUUlBpU1BXVy1YNlNKbGxZaVBxb2V2LXZGdVNqck51STN6ZmdiQ3RhSGNUOXVOcjNDSEQtcklRTTFReWpfS1Q3QlZkYVdVVmh4QV9sSm9PNGNoQWQtSzg4YlVpUElIb3lPZXdYcVloamJDNi1HZ05GOGc4MmJDYlhmTHlGcTBqVWPSAcgBQVVfeXFMTjFVaF9mRVJSRm5OazdQUEJDYWtINllyaWJidGFSOFNLN0ZRM0xLdXNVNTlKcEUwbjlCcHVlN01oUW5YaHdTUnJfbEZPbWV0c1hVa3VieEstZDN1RUdxTDFqaHNCNnhyZ0otY0tGQ2g3RE5QVUR5d3NfSlpxdk1BUVRqV0ZFTnRORFVmVVJIdkthZUYyT1lmUm5ZRmhFZXhnWktvN3g4cVVzY1d4LU0wVGVKa0U3U0JPM3FHM01qTUZHVmtzWGwydi0?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNcTdqYkRtLXJsLVFSMVFrbDJ0NTlsT2VHLWp2OVJFekFPN0ZEQnBVdGJMOEVfRUFYbXU0Rkp4SWM5dHJhbVN5cUhVS0hzRjItbFJGa01BNHdBajFkRnd4WmJ6ZTQxc0h5RzJOaWZ2aHktQUhSalhYUUZfNVZDQUNFblp3ZTQ0clhESy1tMnJBaUhROW8?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNRzMwdHE3emJ6TjdvNXE4UDBnWmRzbEhSLWVsZWJIakgzZFM4aWYwZ2FwNnZ2ckFaQkdBZWRHVE1YN3R0UkFiOC1uNE1pNkRXeDZtcmZwNTVYQTFDZ2lpbDBMRWRNRjNmYnVRQnRCeFV0dGFpekx1SVVyaTg4N0I0RHdpVDFDWEl4VzFv?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOWGpidnZXdlJpWV9qbmFtOE50Z055cGEwYUR0b1AxcGd4U2pCTlVocU5mS3ZFUmFWaTd2anRFVVJFS2p2ZV9FX1Vna0RNUWEtN2VsT3Iya1h2cGhJMzRKXzNTeXk5OXRhUnlRbzd2U2hMc3ZqTzk0aFdSOUlXbmVDVU8yV2l1cElPb1hF?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxNS3dWeDZ2Uk5HcEoxdUh1MXdDTl9Lb0FaMkFFSXAwUnB3RjJYZUwwT2ZHaThYbVZsTjZzb2VJRXUtbEgxd08tTnI5dVlvT0tpbjBETEFYVXpta09YQzk2MG9iUXFUalN1NHN2OFN6MG8tbEo4R2MtNkNrbUhtSXY4M2NiMGZVZHF0a1ZOS1JnRlRkR1praHl2aFoyTnlTUVBVbHRVdEdkaHJqUkg5SHM0ZXRxOWRkR0lhR2JpVHBCUkxISllCaWFMNDd5NVN3RjZKd2lqTlUyamLSAd4BQVVfeXFMTm5MOVJOWUZGUHY3VGtEYUNfd0xKNjdhclJjdjJFNTVqY0lRVnFJWnM5TDk0YWoyenprdi1ab0k3MDV4UzBGaXFoZGpQcXlhQ3B0WmVGdEV3eUJPSkNIQi1rWVdnYmIwQkJlcHRDeEVZT08tV3VmdTFRdkUyNXlxdDdZdHpfcTUwVjhmNkd5Rnc4UnVpbkRZeVY2MkJlSVUzcWNsakljanVDYWNjb1N6M0pCSHNnVHU1MG0tZUU5bHI4ODhJb3FoUG9sNWtQNDNPX1ZjNzhRQ3BFZFlsc0tn?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPZXlUOGlTU0NidTJteW95YnhwS1dwODlaR3VSVkNUVm5hU3NHcFJhWDFIN3ZtWGpMNWIta3V3OU9zQmNkcjY0dmtnamNFeUIzWlhOSHdEeldRV0U0dHdfdHdCYW9zN0JuYzJjT1BvaTRoYmY2enJoLWdHMXR1YXB6bkJySmlrZU9QZGUzMFB5T19hUTZEUnQwSk9SWQ?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxNbmpJNTZhaWVFTXlvendJVXotM2VCSHVNNHh5YzNiTl9kcF9pb0E0UEJPdV95cHVfbWFpZEZJZk1IVWMtcERsNXdUR0lrSEczWWtSdHU4YmR5Z3NIQnpzbnB3QzRFNFdNRXRxaG84ZXZmMUEzcnJnSFl5bHdYekEzMUN3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
