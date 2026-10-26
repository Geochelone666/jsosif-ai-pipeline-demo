# ASML Intelligence Report

- ticker: **ASML**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/ASML/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ASML/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:12:29.409302+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 2, 'ai': 8, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 8 named publishers; 4 exact duplicates; 21 HTTPS source links; largest publisher share 38.1%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1571.8000 |
| Return 1D (%) | 0.7215 |
| Return 1W (%) | -4.2473 |
| Return 1M (%) | -9.9054 |
| Return YTD (%) | 47.6222 |
| Return 1Y (%) | 52.6571 |
| Annualized volatility (%) | 46.5955 |
| Beta vs SPY | 2.2434 |
| Max drawdown (%) | -21.9531 |
| Sharpe (rf=0) | 1.1437 |
| Downside deviation (rf=0, %) | 30.7803 |
| Sortino (rf=0) | 1.7313 |
| Historical VaR 95% (1D, %) | 4.5085 |
| Historical ES 95% (1D, %) | 5.9857 |
| Correlation vs SPY | 0.6137 |
| Tracking error vs SPY (%) | 40.0574 |
| P/E (trailing) | 38.68 |
| P/B | 1349.62 |
| EV/EBITDA | 2066.77 |
| Revenue growth (%) | 55.20 |
| Forward P/E (estimate) | 25.02 |
| Gross margin (%) | 54.34 |
| Operating margin (%) | 44.36 |
| Return on equity (%) | 65.64 |
| Free cash flow yield (%) | N/A |
| MA50 | 1722.7336 |
| Close vs MA50 (%) | -8.7613 |
| MA200 | 1585.3188 |
| Close vs MA200 (%) | -0.8527 |
| RSI (14, Wilder) | 35.2220 |
| MACD (12,26) | -37.5952 |
| MACD signal (9) | -16.3660 |
| MACD histogram | -21.2291 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ASML': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1571.8000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.7215 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.2473 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -9.9054 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 47.6222 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 52.6571 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 46.5955 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 30.7803 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7313 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.5085 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.9857 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6137 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 40.0574 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.2434 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.9531 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1437 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.0159 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3370 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.3560 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 65.6360 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 38.6762 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 35.2220 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -21.2291 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -8.7613 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.8527 -> Slightly below the moving-average trend level.

## TAILWINDS

### Chinese Competitors Aren’t Eroding ASML’s EUV Core Monopoly
- Summary: Chinese rivals fail to threaten ASML’s EUV dominance, supporting its market position.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNV0U0Tnk3TFZ0Y3I2UThjb2J0RTQ4MjhjR1lzbkFhdVZBUGRLR01MNGg3bUJXeWhPR1FsQXB5SV9KV0NVQU9aUmxweDBNQ0NpRUJnaEx5TWVJc2VMOGVsVHdmZUhaWk5mMkR2QUJpNzZscEpUb0s1WEl1ZmhBbjVVNFJBaXFCQUVXdXNacHpoWmRDeGkzcHNYVENSOVZQXzdW?oc=5>

### ASML Holding NV Stock (ASML) Moved Up by 3.19% on Oct 21: A Full Analysis
- Summary: ASML shares rose 3.19% on Oct 21, reflecting positive market sentiment and potential investor confidence.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQcXVNRWlVeHVnVVdiT1lweVdid0F5Zkh0TWJQdXZqY3EyT0RRcVIwT3hEWkRTdURhS0NHal9rRFd4SjRfcEZxWG1rZ2RsdjNnOHdnNzg0VkZRRzd3ZW1XYk9XdUdsY1F1ZmNTMWpPMWwxWmlIOWZhcHhqNGpGZUdOSjR3MDNKVnFlOWs0?oc=5>

## HEADWINDS

### ASML Holding NV (ASML) Shares Fall 6.9% -- What GF Score of 95 Tells Investors
- Summary: ASML Holding NV (ASML) Shares Fall 6.9% -- What GF Score of 95 Tells Investors
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQblRRYl9fUWMtdWZiTnJiU0wxOTBKYlF5d1FMVGhDS2FOV3ptNFNQWU9maWRKenNMX3RBYVRxRm9CUjBGejltcWl2ZXlFTGlFcmdFZGRUWDRVb1IweGRIcEVxVGV1U2JMTEszRFl0alJOTDl5RktiNVBHRTIyM1NEZzRzeWI0NDVLeFdkU1lCUjhTdVBOajFEYWljNUlqbnBoX1hKVVpWQ0ZTT3hsUnpF?oc=5>

### China’s Mid-Tier Emergence Threatens ASML Over the Next 3-5 Years
- Summary: China’s growing tech sector may challenge ASML’s market share in the next 3-5 years.
- Date: 2026-10-23 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQY3Y0TEdWUV9DamFXUXRNal92dmxldC1wUnAtYkxZM0FjRDV2bVhuYVZvRmo1SnhqdmRFOVQ4U2wzNjU4OUxpSFlvNjk2VXpxUWdOWnBzQ09ITEV5T1d6T1gwbmtEdU9IQlA2RzBHV1lLcE45MUw3cWtWSk04SzdzRWZuRkREYkZDV2p3bmF2dW8ySWdnRFV1VENJdWtQUnNS?oc=5>

### ASML Holding NV Stock (ASML) Opened Down by 3.46% on Oct 22: Key Drivers Unveiled
- Summary: ASML shares fell 3.46% on Oct 22, indicating negative market reaction to recent developments.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNamVwcWRjMlZ1aHNSa3J0QmtaN2M1ZU90ZHEyeXh2OG15TjVTbGtUMmJLSmJmTVdxWE1YVWJiQUZjcHlpVkxCTDU4dWN1VnZOQVF0clpXZnViaFdrRUttZDE2MS1FbE9hRFJlYzBsVmdTbUxaNkNLWUhBZWhKQzZhLWNMUmZVSlcxaTFB?oc=5>

## CATALYSTS

### ASML (ENXTAM:ASML) Stock Fair Value Edges Higher After Mixed Analyst Revisions
- Summary: ASML (ENXTAM:ASML) Stock Fair Value Edges Higher After Mixed Analyst Revisions
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQWkVrQURlczl2Y3FFNmFtVHhLOUpreEQzc0RPZ1JqbU9LNjYzaE82Q1hQRUoxcTI5RTI1dUNTODdRTld2cVpBVzg3SWRjbjRVaVFFd3dfZkRTbEZ0ZGV6eHk5QmlwZXh4MWxIZTY5ZzRRZTg5eTFRcGhnUFFhVG9ocnljdVZiMmM0LXV5X3cyTE9VZHlSRjVJ?oc=5>

### Stock-Split Watch: Is ASML Next?
- Summary: Speculation about a potential stock split for ASML.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNS2RwWDRwSVZnRXZQeXowYTFUNmhnLTM0ODNNVlR6djlPcjNXTHRiRkJ1X3IxVkhMc2V0WkRoVlBYMVFIV1NOY0RDZEtNcXVDUVBkbTVIYXJBQWhvSWlwV0NHczJTX280a0lQNHNrS3RUUVNJaHRjT1pyTjdYMlQ5d3RWQ05lZTk1c0xvRVZfX1ZsbGtiWFBj?oc=5>

### ASML Holding N.V. (ASML) Benefits From Demand for Advanced Semiconductor Manufacturing
- Summary: Demand for advanced semiconductor manufacturing boosts ASML.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQZVZmT1FQYXVjbUZudEJDNDZuOGt5SmF6bkhNS2owVmg1WEsxVlJtcWF6ZlhCN1hENWpuVnR3TUEwUXhOYWhyaHFsQzc1WTBLenZKZS1yT3pKeXhtZldoajNJTWo4Ukd6MW9ZZEVidVJKaXZhc2RNUTZNbGFOVjB1N1ZiTXdsTUpXUTJsblVFOA?oc=5>

### ASML Just Announced Fantastic News for Investors in AI Stocks
- Summary: ASML announced positive news related to AI investments.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPc2VEa1FuRXUtQUlpY0s2ZFZzZF9fMzNPbWN5VmNoMHhUQzNRSmxtc1ZwdzJ2T1k3SVljNDRxSmFoUGNDM21VOUZfU0s1UlZfTm8xYkYtZVUtMVZ3RnRCb1ZadmtHVlhJTlJLLWlwa3k5X2xSUFBkNFdFY1FQRUhSWE9TLVlJZFFkeS1JUHJpY1dTYS0tSGVEWm11ME9aMUFpN3hNUFctNA?oc=5>

### ASML: No AI Slowdown In Sight As Orders And Margins Surge (NASDAQ:ASML)
- Summary: ASML reports strong orders and margin growth, indicating positive outlook.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPMzZNVXRGU0pHQnVjOEdNTkFVSHluNkNsa0l0bG02TnZBVFZydE16RDVGdC1DZ09jLXdCRTV3YS10cTFMUWJRR0ZlU0hVbW5IU3hpM2hYSmJSY0FDRllkSzdsZlhyQ0I2TGR1cWNiYTRRTnNwVTloLXRMakdyVm8wTEExT3RCQWxUd1NGTUJGdEdnWlZ1RUJLcm9ING8xZUpR?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ASML** | **38.68** | **1,349.62** | **2,066.77** | **55.20** | **605,799,579,648.00 USD** | **52.66** |
| AMAT | 32.55 | 11.68 | 29.30 | 24.80 | 299,376,705,536.00 USD | 66.03 |
| LRCX | 34.29 | 20.67 | 28.05 | 54.40 | 287,952,764,928.00 USD | 56.68 |
| KLAC | 39.78 | 29.97 | 31.63 | 15.20 | 190,021,992,448.00 USD | 26.31 |

Peers fetched as_of: 2026-10-25; ASML reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-14
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

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

- https://news.google.com/rss/articles/CBMioAFBVV95cUxNV0U0Tnk3TFZ0Y3I2UThjb2J0RTQ4MjhjR1lzbkFhdVZBUGRLR01MNGg3bUJXeWhPR1FsQXB5SV9KV0NVQU9aUmxweDBNQ0NpRUJnaEx5TWVJc2VMOGVsVHdmZUhaWk5mMkR2QUJpNzZscEpUb0s1WEl1ZmhBbjVVNFJBaXFCQUVXdXNacHpoWmRDeGkzcHNYVENSOVZQXzdW?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPYVdaNUJTNkY4VUhNdXlINlhROEtmdUp0eTVUN0NGQWVQaVZzOHlkU1FoOHItZ0JoZWxURnd0Tmk4Ry1XNWozdTFpTmpuUHpHcFF5X242VF9xYVlGRVhMd05veDR2djF4bE1kSW1EMUNzVC1POWx2cTZvV2IyQnFUY2M3NHJIbHdhU190NWg1WUVqMUY2c1kzLS1UeU53ejRJUEVV?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQcXVNRWlVeHVnVVdiT1lweVdid0F5Zkh0TWJQdXZqY3EyT0RRcVIwT3hEWkRTdURhS0NHal9rRFd4SjRfcEZxWG1rZ2RsdjNnOHdnNzg0VkZRRzd3ZW1XYk9XdUdsY1F1ZmNTMWpPMWwxWmlIOWZhcHhqNGpGZUdOSjR3MDNKVnFlOWs0?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQblRRYl9fUWMtdWZiTnJiU0wxOTBKYlF5d1FMVGhDS2FOV3ptNFNQWU9maWRKenNMX3RBYVRxRm9CUjBGejltcWl2ZXlFTGlFcmdFZGRUWDRVb1IweGRIcEVxVGV1U2JMTEszRFl0alJOTDl5RktiNVBHRTIyM1NEZzRzeWI0NDVLeFdkU1lCUjhTdVBOajFEYWljNUlqbnBoX1hKVVpWQ0ZTT3hsUnpF?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQY3Y0TEdWUV9DamFXUXRNal92dmxldC1wUnAtYkxZM0FjRDV2bVhuYVZvRmo1SnhqdmRFOVQ4U2wzNjU4OUxpSFlvNjk2VXpxUWdOWnBzQ09ITEV5T1d6T1gwbmtEdU9IQlA2RzBHV1lLcE45MUw3cWtWSk04SzdzRWZuRkREYkZDV2p3bmF2dW8ySWdnRFV1VENJdWtQUnNS?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNamVwcWRjMlZ1aHNSa3J0QmtaN2M1ZU90ZHEyeXh2OG15TjVTbGtUMmJLSmJmTVdxWE1YVWJiQUZjcHlpVkxCTDU4dWN1VnZOQVF0clpXZnViaFdrRUttZDE2MS1FbE9hRFJlYzBsVmdTbUxaNkNLWUhBZWhKQzZhLWNMUmZVSlcxaTFB?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQWkVrQURlczl2Y3FFNmFtVHhLOUpreEQzc0RPZ1JqbU9LNjYzaE82Q1hQRUoxcTI5RTI1dUNTODdRTld2cVpBVzg3SWRjbjRVaVFFd3dfZkRTbEZ0ZGV6eHk5QmlwZXh4MWxIZTY5ZzRRZTg5eTFRcGhnUFFhVG9ocnljdVZiMmM0LXV5X3cyTE9VZHlSRjVJ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNS2RwWDRwSVZnRXZQeXowYTFUNmhnLTM0ODNNVlR6djlPcjNXTHRiRkJ1X3IxVkhMc2V0WkRoVlBYMVFIV1NOY0RDZEtNcXVDUVBkbTVIYXJBQWhvSWlwV0NHczJTX280a0lQNHNrS3RUUVNJaHRjT1pyTjdYMlQ5d3RWQ05lZTk1c0xvRVZfX1ZsbGtiWFBj?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTFB2Sk9Yd3RacW40T3pyOEdqNXQxcUdnLTV3Zk8tYWNMU2pQVGFKX21wSU9hZDhvbmNFOXdhV3l1QU12aDltdWlxNUljSkRuOGN5SWRDWEhNT2hGNDRicmIxbUZ4NThXZi1OWm96VlVpZHlIOW9OamxyWnc5emFXQQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQZVZmT1FQYXVjbUZudEJDNDZuOGt5SmF6bkhNS2owVmg1WEsxVlJtcWF6ZlhCN1hENWpuVnR3TUEwUXhOYWhyaHFsQzc1WTBLenZKZS1yT3pKeXhtZldoajNJTWo4Ukd6MW9ZZEVidVJKaXZhc2RNUTZNbGFOVjB1N1ZiTXdsTUpXUTJsblVFOA?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPc2VEa1FuRXUtQUlpY0s2ZFZzZF9fMzNPbWN5VmNoMHhUQzNRSmxtc1ZwdzJ2T1k3SVljNDRxSmFoUGNDM21VOUZfU0s1UlZfTm8xYkYtZVUtMVZ3RnRCb1ZadmtHVlhJTlJLLWlwa3k5X2xSUFBkNFdFY1FQRUhSWE9TLVlJZFFkeS1JUHJpY1dTYS0tSGVEWm11ME9aMUFpN3hNUFctNA?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPMzZNVXRGU0pHQnVjOEdNTkFVSHluNkNsa0l0bG02TnZBVFZydE16RDVGdC1DZ09jLXdCRTV3YS10cTFMUWJRR0ZlU0hVbW5IU3hpM2hYSmJSY0FDRllkSzdsZlhyQ0I2TGR1cWNiYTRRTnNwVTloLXRMakdyVm8wTEExT3RCQWxUd1NGTUJGdEdnWlZ1RUJLcm9ING8xZUpR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
