# ASML Intelligence Report

- ticker: **ASML**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/ASML/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ASML/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T01:55:59.312768+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 18, 'rule': 3, 'ai': 7, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261026T005504Z-6368ad31/ASML** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 18 unique headlines; 7 named publishers; 2 exact duplicates; 18 HTTPS source links; largest publisher share 27.78%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1590.9000 |
| Return 1D (%) | 1.2152 |
| Return 1W (%) | -3.4132 |
| Return 1M (%) | -8.7755 |
| Return YTD (%) | 49.4161 |
| Return 1Y (%) | 55.0071 |
| Annualized volatility (%) | 46.6348 |
| Beta vs SPY | 2.2531 |
| Max drawdown (%) | -21.9531 |
| Sharpe (rf=0) | 1.1242 |
| Downside deviation (rf=0, %) | 30.8402 |
| Sortino (rf=0) | 1.7000 |
| Historical VaR 95% (1D, %) | 4.5196 |
| Historical ES 95% (1D, %) | 5.9857 |
| Correlation vs SPY | 0.6144 |
| Tracking error vs SPY (%) | 40.0980 |
| P/E (trailing) | 39.15 |
| P/B | 1366.02 |
| EV/EBITDA | 2091.89 |
| Revenue growth (%) | 55.20 |
| Forward P/E (estimate) | 25.32 |
| Gross margin (%) | 54.34 |
| Operating margin (%) | 44.36 |
| Return on equity (%) | 65.64 |
| Free cash flow yield (%) | N/A |
| MA50 | 1717.6700 |
| Close vs MA50 (%) | -7.3803 |
| MA200 | 1587.3302 |
| Close vs MA200 (%) | 0.2249 |
| RSI (14, Wilder) | 37.9880 |
| MACD (12,26) | -40.2815 |
| MACD signal (9) | -21.1491 |
| MACD histogram | -19.1324 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ASML': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1590.9000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.2152 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.4132 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -8.7755 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 49.4161 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 55.0071 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 46.6348 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 30.8402 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7000 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.5196 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.9857 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6144 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 40.0980 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.2531 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.9531 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1242 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.3199 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3370 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.3560 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 65.6360 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.1462 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 37.9880 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -19.1324 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.3803 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 0.2249 -> Slightly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### ASML Holding NV (ASML) Shares Fall 6.9% -- What GF Score of 95 Tells Investors
- Summary: ASML Holding NV (ASML) Shares Fall 6.9% -- What GF Score of 95 Tells Investors
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQblRRYl9fUWMtdWZiTnJiU0wxOTBKYlF5d1FMVGhDS2FOV3ptNFNQWU9maWRKenNMX3RBYVRxRm9CUjBGejltcWl2ZXlFTGlFcmdFZGRUWDRVb1IweGRIcEVxVGV1U2JMTEszRFl0alJOTDl5RktiNVBHRTIyM1NEZzRzeWI0NDVLeFdkU1lCUjhTdVBOajFEYWljNUlqbnBoX1hKVVpWQ0ZTT3hsUnpF?oc=5>

### ASML Holding NV Stock (ASML) Opened Down by 3.46% on Oct 22: Key Drivers Unveiled
- Summary: ASML shares fell 3.46% on Oct 22, indicating negative market reaction to recent developments.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNamVwcWRjMlZ1aHNSa3J0QmtaN2M1ZU90ZHEyeXh2OG15TjVTbGtUMmJLSmJmTVdxWE1YVWJiQUZjcHlpVkxCTDU4dWN1VnZOQVF0clpXZnViaFdrRUttZDE2MS1FbE9hRFJlYzBsVmdTbUxaNkNLWUhBZWhKQzZhLWNMUmZVSlcxaTFB?oc=5>

### China’s Mid-Tier Emergence Threatens ASML Over the Next 3-5 Years
- Summary: China’s growing mid-tier semiconductor industry poses a competitive threat to ASML over the next 3-5 years.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNNEFEaTBMUEI0TTk2Qi1jTnlsenpuRzlGYldXVmFPTVctdUFva09UN3ZCdHFYb3QxZzFaNEpSYzlRNVVPSkFxckVlbVlzQlFpbHVFc3BGMTAtWDZKUXNudk9SQ3kwb2V3NUFZT1Bod0FlVkltQUltN1pwSVJvN3pTRmZJUmVEWXlfUmNlOTRLV1FDRFROa2tHcmNHMU1Jb3Y1cEhtdUtFd0RzdlFM?oc=5>

## CATALYSTS

### ASML (ENXTAM:ASML) Stock Fair Value Edges Higher After Mixed Analyst Revisions
- Summary: ASML (ENXTAM:ASML) Stock Fair Value Edges Higher After Mixed Analyst Revisions
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQWkVrQURlczl2Y3FFNmFtVHhLOUpreEQzc0RPZ1JqbU9LNjYzaE82Q1hQRUoxcTI5RTI1dUNTODdRTld2cVpBVzg3SWRjbjRVaVFFd3dfZkRTbEZ0ZGV6eHk5QmlwZXh4MWxIZTY5ZzRRZTg5eTFRcGhnUFFhVG9ocnljdVZiMmM0LXV5X3cyTE9VZHlSRjVJ?oc=5>

### ASML reports transactions under its current share buyback program
- Summary: ASML reports transactions under its current share buyback program
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPUHlqVVFKclROVk1Ic3ZsMmw3b3JobEFwbkNTU2tiR1pqTDBHZGx3UWFjcUExVDZoTFNlQ2lyMTRPUkVjQzVtVnAza00wWEFNeWNfSWVwOWhqS3ZabXUxQXpkWGw2SlRYZk4xSnVabnRjdndYdXIzTWpQTEdocHRJVllEcmQxUkxQXzBEQWVkZWZSQlRIVVBESXlxRDB5bHZMRE9idXdraw?oc=5>

### ASML: No AI Slowdown In Sight As Orders And Margins Surge (NASDAQ:ASML)
- Summary: ASML reports strong orders and margin growth, indicating positive outlook.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPMzZNVXRGU0pHQnVjOEdNTkFVSHluNkNsa0l0bG02TnZBVFZydE16RDVGdC1DZ09jLXdCRTV3YS10cTFMUWJRR0ZlU0hVbW5IU3hpM2hYSmJSY0FDRllkSzdsZlhyQ0I2TGR1cWNiYTRRTnNwVTloLXRMakdyVm8wTEExT3RCQWxUd1NGTUJGdEdnWlZ1RUJLcm9ING8xZUpR?oc=5>

### Why ASML's Q3 2026 Results Dropped The Stock Price (NASDAQ:ASML)
- Summary: ASML reported Q3 2026 earnings below expectations, causing a sharp decline in its share price.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNT1ZhVkhrUE8wclNRcVVQeHc3Z1lMRjh1RTNmWUZUcWFqWVB4TEI0bTV4blVuY1pEaVJkVEpnVXZBckprajZPM0tmZ012SUlTRlB6VS1ZS0YyQkdNQTM5ZVY1QU5XcDdEYnZYZVNRMkEzLWFWbkJqVnhSWWdZaGkyZUU4VW1SRFlUYmQ4VWFCMjBaaEk?oc=5>

### Stock-Split Watch: Is ASML Next?
- Summary: Speculation that ASML may execute a stock split, potentially increasing liquidity and investor interest.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTFB2Sk9Yd3RacW40T3pyOEdqNXQxcUdnLTV3Zk8tYWNMU2pQVGFKX21wSU9hZDhvbmNFOXdhV3l1QU12aDltdWlxNUljSkRuOGN5SWRDWEhNT2hGNDRicmIxbUZ4NThXZi1OWm96VlVpZHlIOW9OamxyWnc5emFXQQ?oc=5>

### ASML: Creating Its Own Bottleneck (NASDAQ:ASML)
- Summary: ASML faces internal production bottlenecks, potentially affecting output and delivery schedules.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE5UTDZiNmR4ZndtYW4tQW8wSDU2dXk4UVJLcDJ1a3RuYy1zYkNOYTVvMENMVVBpUlh6THdfM1N1UEVmWWZQYjFKRHhPYmk2S3Ayd2VJRE1MdEZvNGs4VXVjdFZ0dk1xS0swUlRhZ2g4dVdsdWtrdlFlX2dBYWJYUQ?oc=5>

### Why ASML is a buy After Terafab Deal?
- Summary: Analyst recommends buying ASML shares following the Terafab acquisition, citing strategic benefits.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNcHMyUmZQRDZQSUR1VWhLdkZDOG9pY0NwRXNZdG9WXzhEVTBWN1B0UXZCSldFbVU3bHdhQU40NWpNQXJBYVRaWnBpdWRVM0lyOHFSUy16VEw3VGNmNVA2S1lSUjNTeUNOTDNZaU1zZm5RMWkxbnJaQWJCLTYxYVhvcDFRZE9nS2xOY0hzTlRLanV0cWlJR2pLbHg5VVp6aTNQeG5qa29xUS1OeFl4czlCNw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ASML** | **39.15** | **1,366.02** | **2,091.89** | **55.20** | **613,161,041,920.00 USD** | **55.01** |
| AMAT | 33.44 | 12.00 | 30.10 | 24.80 | 307,590,430,720.00 USD | 70.38 |
| LRCX | 35.39 | 21.33 | 28.96 | 54.40 | 297,213,296,640.00 USD | 57.30 |
| KLAC | 40.77 | 30.71 | 32.40 | 15.20 | 194,720,022,528.00 USD | 26.83 |

Peers fetched as_of: 2026-10-26; ASML reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-14
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMirwFBVV95cUxQblRRYl9fUWMtdWZiTnJiU0wxOTBKYlF5d1FMVGhDS2FOV3ptNFNQWU9maWRKenNMX3RBYVRxRm9CUjBGejltcWl2ZXlFTGlFcmdFZGRUWDRVb1IweGRIcEVxVGV1U2JMTEszRFl0alJOTDl5RktiNVBHRTIyM1NEZzRzeWI0NDVLeFdkU1lCUjhTdVBOajFEYWljNUlqbnBoX1hKVVpWQ0ZTT3hsUnpF?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNamVwcWRjMlZ1aHNSa3J0QmtaN2M1ZU90ZHEyeXh2OG15TjVTbGtUMmJLSmJmTVdxWE1YVWJiQUZjcHlpVkxCTDU4dWN1VnZOQVF0clpXZnViaFdrRUttZDE2MS1FbE9hRFJlYzBsVmdTbUxaNkNLWUhBZWhKQzZhLWNMUmZVSlcxaTFB?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNNEFEaTBMUEI0TTk2Qi1jTnlsenpuRzlGYldXVmFPTVctdUFva09UN3ZCdHFYb3QxZzFaNEpSYzlRNVVPSkFxckVlbVlzQlFpbHVFc3BGMTAtWDZKUXNudk9SQ3kwb2V3NUFZT1Bod0FlVkltQUltN1pwSVJvN3pTRmZJUmVEWXlfUmNlOTRLV1FDRFROa2tHcmNHMU1Jb3Y1cEhtdUtFd0RzdlFM?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQWkVrQURlczl2Y3FFNmFtVHhLOUpreEQzc0RPZ1JqbU9LNjYzaE82Q1hQRUoxcTI5RTI1dUNTODdRTld2cVpBVzg3SWRjbjRVaVFFd3dfZkRTbEZ0ZGV6eHk5QmlwZXh4MWxIZTY5ZzRRZTg5eTFRcGhnUFFhVG9ocnljdVZiMmM0LXV5X3cyTE9VZHlSRjVJ?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPUHlqVVFKclROVk1Ic3ZsMmw3b3JobEFwbkNTU2tiR1pqTDBHZGx3UWFjcUExVDZoTFNlQ2lyMTRPUkVjQzVtVnAza00wWEFNeWNfSWVwOWhqS3ZabXUxQXpkWGw2SlRYZk4xSnVabnRjdndYdXIzTWpQTEdocHRJVllEcmQxUkxQXzBEQWVkZWZSQlRIVVBESXlxRDB5bHZMRE9idXdraw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPMzZNVXRGU0pHQnVjOEdNTkFVSHluNkNsa0l0bG02TnZBVFZydE16RDVGdC1DZ09jLXdCRTV3YS10cTFMUWJRR0ZlU0hVbW5IU3hpM2hYSmJSY0FDRllkSzdsZlhyQ0I2TGR1cWNiYTRRTnNwVTloLXRMakdyVm8wTEExT3RCQWxUd1NGTUJGdEdnWlZ1RUJLcm9ING8xZUpR?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNT1ZhVkhrUE8wclNRcVVQeHc3Z1lMRjh1RTNmWUZUcWFqWVB4TEI0bTV4blVuY1pEaVJkVEpnVXZBckprajZPM0tmZ012SUlTRlB6VS1ZS0YyQkdNQTM5ZVY1QU5XcDdEYnZYZVNRMkEzLWFWbkJqVnhSWWdZaGkyZUU4VW1SRFlUYmQ4VWFCMjBaaEk?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTFB2Sk9Yd3RacW40T3pyOEdqNXQxcUdnLTV3Zk8tYWNMU2pQVGFKX21wSU9hZDhvbmNFOXdhV3l1QU12aDltdWlxNUljSkRuOGN5SWRDWEhNT2hGNDRicmIxbUZ4NThXZi1OWm96VlVpZHlIOW9OamxyWnc5emFXQQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNS2RwWDRwSVZnRXZQeXowYTFUNmhnLTM0ODNNVlR6djlPcjNXTHRiRkJ1X3IxVkhMc2V0WkRoVlBYMVFIV1NOY0RDZEtNcXVDUVBkbTVIYXJBQWhvSWlwV0NHczJTX280a0lQNHNrS3RUUVNJaHRjT1pyTjdYMlQ5d3RWQ05lZTk1c0xvRVZfX1ZsbGtiWFBj?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE5UTDZiNmR4ZndtYW4tQW8wSDU2dXk4UVJLcDJ1a3RuYy1zYkNOYTVvMENMVVBpUlh6THdfM1N1UEVmWWZQYjFKRHhPYmk2S3Ayd2VJRE1MdEZvNGs4VXVjdFZ0dk1xS0swUlRhZ2g4dVdsdWtrdlFlX2dBYWJYUQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNcHMyUmZQRDZQSUR1VWhLdkZDOG9pY0NwRXNZdG9WXzhEVTBWN1B0UXZCSldFbVU3bHdhQU40NWpNQXJBYVRaWnBpdWRVM0lyOHFSUy16VEw3VGNmNVA2S1lSUjNTeUNOTDNZaU1zZm5RMWkxbnJaQWJCLTYxYVhvcDFRZE9nS2xOY0hzTlRLanV0cWlJR2pLbHg5VVp6aTNQeG5qa29xUS1OeFl4czlCNw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
