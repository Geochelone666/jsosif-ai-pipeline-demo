# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:09:58.196213+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 3, 'ai': 8, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **7**; {'low_uncalibrated_model_confidence': 4, 'short_term_price_move_in_structural_risks': 3}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 11 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 22.73%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 516.7900 |
| Return 1D (%) | 1.7443 |
| Return 1W (%) | -2.2619 |
| Return 1M (%) | -15.9158 |
| Return YTD (%) | 141.3102 |
| Return 1Y (%) | 119.9200 |
| Annualized volatility (%) | 68.3445 |
| Beta vs SPY | 3.2410 |
| Max drawdown (%) | -27.7608 |
| Sharpe (rf=0) | 1.4970 |
| Downside deviation (rf=0, %) | 42.8038 |
| Sortino (rf=0) | 2.3903 |
| Historical VaR 95% (1D, %) | 5.8580 |
| Historical ES 95% (1D, %) | 8.2198 |
| Correlation vs SPY | 0.6045 |
| Tracking error vs SPY (%) | 61.4836 |
| P/E (trailing) | 131.83 |
| P/B | 12.55 |
| EV/EBITDA | 87.31 |
| Revenue growth (%) | 50.10 |
| Forward P/E (estimate) | 32.79 |
| Gross margin (%) | 55.72 |
| Operating margin (%) | 17.25 |
| Return on equity (%) | 10.20 |
| Free cash flow yield (%) | 1.05 |
| MA50 | 542.2794 |
| Close vs MA50 (%) | -4.7004 |
| MA200 | 402.0832 |
| Close vs MA200 (%) | 28.5281 |
| RSI (14, Wilder) | 38.9761 |
| MACD (12,26) | -9.9345 |
| MACD signal (9) | 4.0147 |
| MACD histogram | -13.9492 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 516.7900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.7443 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.2619 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -15.9158 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 141.3102 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 119.9200 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 68.3445 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 42.8038 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.3903 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.8580 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 8.2198 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6045 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 61.4836 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.2410 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.7608 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4970 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 32.7852 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 55.7240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.2500 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.1960 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0480 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 131.8342 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.9761 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -13.9492 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -4.7004 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 28.5281 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### AMD pulled lower by tech slide, falls 8% (AMD:NASDAQ)
- Summary: AMD pulled lower by tech slide, falls 8% (AMD:NASDAQ)
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxPY2lkd3hiVjE5em5HUHJFQXlMT1h6TU5mUWpNbVVmc0J5a2Jvc2pkVHkxellvSFZtb3FSdEpDWVBBV2lmLUtEODFkUWVuWmxrX291STAzWjlBc3NKNThCR1lZVGdCUzdXMS1adFhOVXgyTGlUVG5NV2xjNVRoV05wRVNn?oc=5>

### AMD Stock Drops 7% in Chip Sell-Off - Here's Why
- Summary: AMD Stock Drops 7% in Chip Sell-Off - Here's Why
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNM3VPRURJWHYtb2thbFlGa283LUhseWRJcnNOaVdnNHdFU183c24wTS1jdThnREZBNjJCRGRkbThObWRxc0V3ZHIyVlUyQWdyZ0FGLXdvSHdBT200cklRWDFKTnJtUFotYjEzemRaSlZnN2ZCeVlfSDZETURlUVNvYUdnZzdrWjgzdjFBeG5YOHZNTEF5SmxiaW5kLWVpTF9abllkZU9fRmY?oc=5>

## CATALYSTS

### Advanced Micro Devices, Inc. $AMD Stock: Sterling Capital Management LLC Lowers Stake
- Summary: Advanced Micro Devices, Inc. $AMD Stock: Sterling Capital Management LLC Lowers Stake
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxQbzZMNVM1cGEzVDhuU0RQZjNtQkVHWjQxZHNNaUd1MExVUUNweDkwLTdYY2hha1c0OTZrNzRQdWhqSk5Ud09KMkdWbDZETkF5LTZiTTNEUUU0ZzFuZGdJelNiM2NMaGFWVXA2dkVPdlEzUmNkZnZqdjdmZDE1LVJNbFpIWk9XdkVIUFoxc0QzRnMwa3BaRk01T3hZOEdrNG1hUlVTb0JhUkJ4M3JvN3JUVnpqeUxHbDBONVp5elFLNDR1MnFxSWJoWU1kWS1lb2pmTjdHWmM3Z2Fidw?oc=5>

### Dell, Lenovo, Cisco, HPE, Supermicro: Why AMD’s New AI Blueprint Has Everyone Signing On
- Summary: AMD unveils AI blueprint attracting major OEMs, signaling product launch and partnership potential.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOd2diNGt0TW1ZUUlXdjNzdnk0SkF3MTd3cm1taWR6dkUwNlZ6OTBFN2YweTVDbFFDcDBjNExrRFRRVVBMVEdxd080YTlrRUhxVVN3OUFsUzFwM0JkRkNaVkstcDlFdS1Mc0VWVHlJM09xSjAxeDIxU1E5RGVCNkVZWF9ES0JycVdSQURTSHBodWJVVXNLYXZJTGJKS0lEZThSVGNuNnFoTUhoZmZ3dFFxTnRRRmFETnZtaDVrSGZTeERRRW1j?oc=5>

## RISKS

### Why Are Nvidia, AMD and Micron Stocks Crashing Today? AI Spending Fears Hit Chips
- Summary: AI spending fears trigger sharp decline in AMD shares, indicating market risk.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE0zc25iZ1RZenM5U3N2QkJMQ2Q1UVBscjFreDQ5cDZ1LW1EUGdiNVFHU2JIeEJmajJfaThMN3RqNExGNWRnVFlqblEtb0o2OFMwaF9FZmJicloxemtoZzJRNFhtOXhmMXI4YWxtd2ZEcklyRDZOVWNyZ1RMTXhxWTg?oc=5>

### Why Are Nvidia, Intel, and AMD Stocks Rebounding in Premarket Today, October 23?
- Summary: Positive premarket rebound lifts AMD stock, reducing short-term risk.
- Date: 2026-10-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQV3FIOXNDVE5WUW4wNDR6MFZ6RTA4ay1vOXppWUJrWG1HZERnYU5XdXVRRjdmN0dTU2RKVTVrb3BUenlkMGxDblhyV1AydWNnRm5QVEU4NmgzWGRucnl2QUw2bkhSLTRtRUMzNUkzQzVRbGlmeWVOTWl3R3dyUDYtX3VOTXA1M0kwT01keTZTR2w2R0VWNGVQZms3NEJiYzV6bUpxYzNWbFNrY21nQzNHOA?oc=5>

### AMD, Lam Research among market cap stock movers on Thursday
- Summary: AMD shares move within market cap changes, reflecting moderate market activity.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPSjliN2QzU052bHEyZ2NFVTNGbk92XzRhN1dDRS01ekxkcDZVMWFDM1JsUVlNczF4OENndmlsdXEySHVRc3NXT3J5NTVBS2xhTG9Xak96YXVxOHdnTEtvcnoydlI2SXlaa0hhaHI0OVR6eGg5UzA3MER3X2NnblgzX0ZYMUpZcnZ5c1BCaTZ3UTZPWm9aME5BT1NYWlF4blJQQ2ZReFo4VnpTYlh4dWg5Q2tVOElPbGtOQjFIaw?oc=5>

### Advanced Micro Devices (AMD) Stock Plummeted 13% Last Week. Should You Buy the Dip Before Nov. 3?
- Summary: Shares fell 13% last week; article questions buying before Nov. 3.
- Date: 2026-10-21 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiigJBVV95cUxNRHRFeW9ZZy0tS0JFSG1xajRwdnZDeDB2eFFoQmp2Q3J6MmpnTHV4SE10MnlORy0tbmJPeDZrVllKaXh6OHJ3SndDZVp0cFJtY3pqMGxLemhheUM4eEtWb2VldHhSVGxKVUtEdjZCOTFaamxLV0ozNm1BMGZ5cnNqbTZSaThXSmFpaUNWX0xFcEdfR2xwRDVwUUcxU2hnMFhPbHJZQVB1YVZZTzhxcWJsekN1M2RCNTRrb0ZqTXhQcVN6NTh3ZWVOREtyY21sUjVlMWFYTVd3YWFqSDl0VFNMaHR5RERRbXRibk5PVWdNdWQwNk1KTG5PRXlHbENZTU9peDQtNmVKbjRqZw?oc=5>

### Why Is Advanced Micro Devices Stock Trending Wednesday?
- Summary: Explores reasons behind AMD stock movement on Wednesday.
- Date: 2026-10-21 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQeVRzcl9TV1BVc1ljRENYWmZGRzdTSG00NTNEc0pjWElhUDJqeGQ3dDFhZVA4Vk12cV92cFpEX2JuRllrWjZyeDdwV3FLOFpSblFJVnBDTlMtME41QUY2MndpWWpwUGh4dVBva2RnZ2pyZkE5TnlteENYQ3poUm5WRUZUbEtpOWhDbDVXNGt2VkMtM3lJZEx6WVkxZ0FjLUZVRVhaTVBLQXQ4a1BmNk0zNmJzM0tWdw?oc=5>

### Does The Move In AMD Stock Change Anything?
- Summary: Assesses impact of recent AMD stock movement.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPcjJRMDVEMzlYTzhBRFRBbEZEbkJSLWtvLXkzY3FzVXVfVTNkc3hmNkEzYXI2YzNrdkVwS1BadnFYWmNfcW5MWTNILUduVWZYTkw4OU5feS1JcEZndkxyUkRsR0U5a1ZidjlFUVliV0xuTzgtb1lNR0UtLUIwSmxad0FTNkIwd2p2RF9oMnRsT3FHczNkblFtelN3UFBnUGhrZF93Sw?oc=5>

### 1 Red Flag That Keeps Me From Buying AMD Stock
- Summary: Highlights a concern deterring purchase of AMD shares.
- Date: 2026-10-25 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPNENhNjZRRVpLRDJfRzg4Xy03WmtTNE4xWmVxNXZQejEwbno1Zkh6SldtTzg3bHd3ZEQ0NFJ6MlFyWUV4MUV2T2c5c1BiQ2lrS3JGSnI1ektxSGRHcGNmU1I1SWFLVnFPbFY0dmpUYjZJdVpQT3BHMUhTS1ZfVnZBTGVzSEhiaHJpdURQWTB6d2ktU3M?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **131.83** | **12.55** | **87.31** | **50.10** | **843,646,697,472.00 USD** | **119.92** |
| NVDA | 26.67 | 22.25 | 25.14 | 105.90 | 5,094,050,889,728.00 USD | 16.09 |
| INTC | N/A | 5.01 | 28.21 | 25.40 | 459,679,694,848.00 USD | 127.88 |
| AVGO | 41.08 | 15.40 | 30.06 | 85.50 | 1,535,581,224,960.00 USD | -5.87 |

Peers fetched as_of: 2026-10-25; AMD reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,297,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiggFBVV95cUxPY2lkd3hiVjE5em5HUHJFQXlMT1h6TU5mUWpNbVVmc0J5a2Jvc2pkVHkxellvSFZtb3FSdEpDWVBBV2lmLUtEODFkUWVuWmxrX291STAzWjlBc3NKNThCR1lZVGdCUzdXMS1adFhOVXgyTGlUVG5NV2xjNVRoV05wRVNn?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNM3VPRURJWHYtb2thbFlGa283LUhseWRJcnNOaVdnNHdFU183c24wTS1jdThnREZBNjJCRGRkbThObWRxc0V3ZHIyVlUyQWdyZ0FGLXdvSHdBT200cklRWDFKTnJtUFotYjEzemRaSlZnN2ZCeVlfSDZETURlUVNvYUdnZzdrWjgzdjFBeG5YOHZNTEF5SmxiaW5kLWVpTF9abllkZU9fRmY?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxQbzZMNVM1cGEzVDhuU0RQZjNtQkVHWjQxZHNNaUd1MExVUUNweDkwLTdYY2hha1c0OTZrNzRQdWhqSk5Ud09KMkdWbDZETkF5LTZiTTNEUUU0ZzFuZGdJelNiM2NMaGFWVXA2dkVPdlEzUmNkZnZqdjdmZDE1LVJNbFpIWk9XdkVIUFoxc0QzRnMwa3BaRk01T3hZOEdrNG1hUlVTb0JhUkJ4M3JvN3JUVnpqeUxHbDBONVp5elFLNDR1MnFxSWJoWU1kWS1lb2pmTjdHWmM3Z2Fidw?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOd2diNGt0TW1ZUUlXdjNzdnk0SkF3MTd3cm1taWR6dkUwNlZ6OTBFN2YweTVDbFFDcDBjNExrRFRRVVBMVEdxd080YTlrRUhxVVN3OUFsUzFwM0JkRkNaVkstcDlFdS1Mc0VWVHlJM09xSjAxeDIxU1E5RGVCNkVZWF9ES0JycVdSQURTSHBodWJVVXNLYXZJTGJKS0lEZThSVGNuNnFoTUhoZmZ3dFFxTnRRRmFETnZtaDVrSGZTeERRRW1j?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNWXB6a3d0Yml4a2t1bHNKNTZkZ3B4SEpqYjgyN0JHcTJBTVQ1NUJKMjg0V3pnWERNSjJHVS1QUHdZZ2xOVUl1MVNraGJrd1ZULTlyaW5ObnB4Vko3R013Tkx3bUZzRzFBVThNLVcweGx4dTA2SC1MSzFtd0xXUUc1QnVtX0RyZjl1MTd5bDJTcFBXcGZidFl6d3dQdDI?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE0zc25iZ1RZenM5U3N2QkJMQ2Q1UVBscjFreDQ5cDZ1LW1EUGdiNVFHU2JIeEJmajJfaThMN3RqNExGNWRnVFlqblEtb0o2OFMwaF9FZmJicloxemtoZzJRNFhtOXhmMXI4YWxtd2ZEcklyRDZOVWNyZ1RMTXhxWTg?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQV3FIOXNDVE5WUW4wNDR6MFZ6RTA4ay1vOXppWUJrWG1HZERnYU5XdXVRRjdmN0dTU2RKVTVrb3BUenlkMGxDblhyV1AydWNnRm5QVEU4NmgzWGRucnl2QUw2bkhSLTRtRUMzNUkzQzVRbGlmeWVOTWl3R3dyUDYtX3VOTXA1M0kwT01keTZTR2w2R0VWNGVQZms3NEJiYzV6bUpxYzNWbFNrY21nQzNHOA?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPSjliN2QzU052bHEyZ2NFVTNGbk92XzRhN1dDRS01ekxkcDZVMWFDM1JsUVlNczF4OENndmlsdXEySHVRc3NXT3J5NTVBS2xhTG9Xak96YXVxOHdnTEtvcnoydlI2SXlaa0hhaHI0OVR6eGg5UzA3MER3X2NnblgzX0ZYMUpZcnZ5c1BCaTZ3UTZPWm9aME5BT1NYWlF4blJQQ2ZReFo4VnpTYlh4dWg5Q2tVOElPbGtOQjFIaw?oc=5
- https://news.google.com/rss/articles/CBMiigJBVV95cUxNRHRFeW9ZZy0tS0JFSG1xajRwdnZDeDB2eFFoQmp2Q3J6MmpnTHV4SE10MnlORy0tbmJPeDZrVllKaXh6OHJ3SndDZVp0cFJtY3pqMGxLemhheUM4eEtWb2VldHhSVGxKVUtEdjZCOTFaamxLV0ozNm1BMGZ5cnNqbTZSaThXSmFpaUNWX0xFcEdfR2xwRDVwUUcxU2hnMFhPbHJZQVB1YVZZTzhxcWJsekN1M2RCNTRrb0ZqTXhQcVN6NTh3ZWVOREtyY21sUjVlMWFYTVd3YWFqSDl0VFNMaHR5RERRbXRibk5PVWdNdWQwNk1KTG5PRXlHbENZTU9peDQtNmVKbjRqZw?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQeVRzcl9TV1BVc1ljRENYWmZGRzdTSG00NTNEc0pjWElhUDJqeGQ3dDFhZVA4Vk12cV92cFpEX2JuRllrWjZyeDdwV3FLOFpSblFJVnBDTlMtME41QUY2MndpWWpwUGh4dVBva2RnZ2pyZkE5TnlteENYQ3poUm5WRUZUbEtpOWhDbDVXNGt2VkMtM3lJZEx6WVkxZ0FjLUZVRVhaTVBLQXQ4a1BmNk0zNmJzM0tWdw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPcjJRMDVEMzlYTzhBRFRBbEZEbkJSLWtvLXkzY3FzVXVfVTNkc3hmNkEzYXI2YzNrdkVwS1BadnFYWmNfcW5MWTNILUduVWZYTkw4OU5feS1JcEZndkxyUkRsR0U5a1ZidjlFUVliV0xuTzgtb1lNR0UtLUIwSmxad0FTNkIwd2p2RF9oMnRsT3FHczNkblFtelN3UFBnUGhrZF93Sw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPNENhNjZRRVpLRDJfRzg4Xy03WmtTNE4xWmVxNXZQejEwbno1Zkh6SldtTzg3bHd3ZEQ0NFJ6MlFyWUV4MUV2T2c5c1BiQ2lrS3JGSnI1ektxSGRHcGNmU1I1SWFLVnFPbFY0dmpUYjZJdVpQT3BHMUhTS1ZfVnZBTGVzSEhiaHJpdURQWTB6d2ktU3M?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
