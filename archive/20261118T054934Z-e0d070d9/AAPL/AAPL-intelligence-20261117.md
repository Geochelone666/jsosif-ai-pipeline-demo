# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:06:52.795693+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 11, 'ai': 11, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 5 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 48.0%; oldest publication 2026-11-12

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 351.9100 |
| Return 1D (%) | -0.2466 |
| Return 1W (%) | 1.0523 |
| Return 1M (%) | 2.5381 |
| Return YTD (%) | 29.8963 |
| Return 1Y (%) | 32.0332 |
| Annualized volatility (%) | 24.8820 |
| Beta vs SPY | 0.6118 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.2462 |
| Downside deviation (rf=0, %) | 16.8728 |
| Sortino (rf=0) | 1.8377 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.3389 |
| Tracking error vs SPY (%) | 24.0133 |
| P/E (trailing) | 39.28 |
| P/B | 45.63 |
| EV/EBITDA | 30.04 |
| Revenue growth (%) | 11.70 |
| Forward P/E (estimate) | 33.29 |
| Gross margin (%) | 48.79 |
| Operating margin (%) | 33.01 |
| Return on equity (%) | 142.26 |
| Free cash flow yield (%) | 2.07 |
| MA50 | 340.1695 |
| Close vs MA50 (%) | 3.4514 |
| MA200 | 301.6598 |
| Close vs MA200 (%) | 16.6579 |
| RSI (14, Wilder) | 56.3163 |
| MACD (12,26) | 4.0884 |
| MACD signal (9) | 3.5964 |
| MACD histogram | 0.4920 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 351.9100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.2466 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.0523 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.5381 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 29.8963 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 32.0332 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.8820 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.8728 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.8377 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3389 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.0133 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6118 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2462 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 33.2885 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.7860 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.0100 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 142.2570 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.0661 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.2757 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.3163 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4920 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.4514 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 16.6579 -> Clearly above the moving-average trend level.

## TAILWINDS

### Apple targets June 2027 unveiling for AI smart glasses: report (AAPL:NASDAQ)
- Summary: Apple plans to unveil AI smart glasses in June 2027.
- Date: 2026-11-16 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOZEhVR1p4SVhoeEFLSTkwSUVoLW5RRG9JRmZxX1k5NVVpbExYRU1WTGw5clM4d2FKNllFMTlROVlVT25HQmdkRHpVZUJqMWptSlhkSk9RdmF4LTlDMlhQazFDU3ZlelhMRkJPMTJkOEl0UHYxZHpOY3lYSG1lU2piV0tzM2lvZXdmaDJTU0RueExWYmNJWU1uQU4tWW83Q1lZ?oc=5>

### Apple: The Business Got Better, The Stock Got Much More Expensive (NASDAQ:AAPL)
- Summary: Business improvement and higher stock price signal positive momentum.
- Date: 2026-11-14 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOc2xKSXl6YWFyMmtDeE1OcmZpLUNDUTh4cGxTZGt0TkhTd2VMWFVsR2J1ZGdJc1hOWVZvUFBrbW9ZMzlZZ19HUVducENSWjgtQzFOdG1MU1ZBcDU4MVhyM2Izc1RJclFyblhRQV9XNDNvUmwtMHA0ZllBZTlSQ2U0VFBpU294Y3N6ZXdtMzRCc2o4SkZvcEtNaklnYjY?oc=5>

### ETFs Are Buying Apple (AAPL) on Wednesday
- Summary: ETFs purchased Apple shares on Wednesday, indicating investor confidence.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNMEp1cUF5TVRWX3FKVXJSNlNmR2F1c0hMdjR3cVpaS3JwRlVJbzBmQVp6LTY0MDVtb2h1aVBKSUZPSnI5a2lXX0dwc3ZTMjh3eDFWWjVMSUIyWHJPVHlCOHRJVzV1UzVSMzRLLTljODI3M080WWxldzNYS0kxUk40ZFQ1WkZNZGZBN1Q3RDc3WHZxWkJjNFZfOUNmZXBwQQ?oc=5>

### Apple (AAPL) Sees $460.3 Million in Net ETF Buying on Nov. 10
- Summary: Apple experienced $460.3M net ETF buying on Nov. 10, boosting share demand.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxOdDJER0dOZTdtdWwxU1FtekJMOFl1MVhYbDhHQ044RjB2NlVza1NDaUNRUVZMTGtLTlM4b19KTmZHazlrcXV4VTgtX0NSSldrU0hTVWl0Y05wdzlLXzRxUXFEVk01RTh0ZVBFQ0RKcVQtV2tsb2dsQ21RUEE1YVlXTjNORnd2RVJmaWU4RWRYYw?oc=5>

### Apple Inc. $AAPL Stock Holdings Raised by First Interstate Bank
- Summary: First Interstate Bank increased Apple holdings, reflecting institutional support.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPMmlGdE5NTkRwTWthS2Y0ZmZ2TXg3TTAtQmZka1cxXzkxV25LbU9xM3VjeUFtM0dhLXhkSjBBWGJuMFVYZHFWYTdfdG5XcV82dFNLN2VhNW43VWI2Q0l3aUZibFYyZU9HaXNmNVc4ZkZaMUREdkEwcFpteFdZQ29wQnU4TUVHT3dHM0ZPV3NOaXNaNVFoNWxoMGdqMkFzWlRwOUl3dHVaOF9qWXlZeE5Lb1NFenF3SWpuczFIRm9Gdw?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Apple (AAPL) Picks Core Foldable Glass Supplier For iPhone Duo
- Summary: Apple (AAPL) Picks Core Foldable Glass Supplier For iPhone Duo
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOYmt6MzR0X1VRdEVBYVF2Y1drN3B0RlpXRUtmOW9CX0ZFbE5kYUJXV0oxczZUckthVWxMTW1JeVM5bkZLaVE1QjhZSi1kazRpWUEyUHEySFFoZ21URmNfYVVtQ0Q0NEIwZTdldkpmOVc3akt0XzVxaXVvbFZ6d0ZmUzdxOFlPZkVvYUlRaUFtVU5CRTZ4S0E?oc=5>

### Apple to stand trial in France over iPhone repair restrictions: report (AAPL:NASDAQ)
- Summary: Apple to stand trial in France over iPhone repair restrictions: report (AAPL:NASDAQ)
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPZ0xRQ0RCX3RmbzdqVjRpTzAwSFZ0bTRGeTlCUzh5QXRpSlZRT0NWT3Y5YmhFU1AtdHA1ZmM1eGxDczBsdVFNUDYyd085VVJPaHFCRGZPZlZMWDZFX3hQM0p4M1UyQlZOYnlfRGY1eFNnbHFDSWdtUkN6TWE2R2VjQjlIZ09GODAxcDBmRVNUVTI1ME9xMks3WUo1U19nZ1I0ZEJQXzJ1R3VkRlU?oc=5>

### Apple adds face unlock to iPhone Duo in new software beta (AAPL:NASDAQ)
- Summary: Apple adds face unlock to iPhone Duo in new software beta (AAPL:NASDAQ)
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNekw4czk1V0dBR21SMWtoS1ozbkVuWUhPTTR5cEtWTmNTd3JrdHM3UWg5RWItekxCMnJVcUhrZXBDTkJ3aDdPdktucTRUYWtjazFCV1p4a0xyMzBsS3NrMXdvOGlmaEViOGM4MTd4MmZQOW9sN0JTbmQxY3pyRjlTUjk2eXBCa0QwWFR0N1REdHhMMmRfb0x3anhnWQ?oc=5>

### Apple Inc. $AAPL Stock Acquired by Sunesis Advisors LLC
- Summary: Apple Inc. $AAPL Stock Acquired by Sunesis Advisors LLC
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxPY1V2dU9TeHN5OV8yNllZS0RPeVNYd1cxeW5nWk5vV2loMm9oRjRoOFpJaEZPNFFfS3AyN3F3N1VvQkVHcW91Z0lwczlXdGw5RHA1MzVSanpNUTNIYlVzX21uNnRBb2lUcExIZGNWWEFKUC1ESDFPb3ZQVWtNYjgzWU40OXdHVlRSYWdvYWJqRXVxN1RRY1BneDMtaG85QnR1dGlsVTRhNi1DR3dfNzVQdzNPNVM?oc=5>

### Apple Inc. $AAPL Stock: Patton Albertson Miller Group LLC Reduces Stake
- Summary: Apple Inc. $AAPL Stock: Patton Albertson Miller Group LLC Reduces Stake
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxPWG1xRGdvdk1TNWc1UDdHWG5ScnZBSTQ4LVRFX085Z1E4bVpUcG94YXNUbHM3QTR5UUZnT3RSRnk2aWhkWWRBdmdjWkhtNE1RWnh1VTB4VkF3VGFyQ2JfSWw2MGN4SWNFeTdfRXV0eHg2emZieTBEWHFweHVOZTZFcE81eVQ5dDljcVVoNTZCM3ZxYWF4MUQyU1RpenFpVllpUHlpcEx3MGlEWWFNVjFfM0pQX281WG16dkNKY2trc3hiZFZuaktjbA?oc=5>

### Apple Inc. $AAPL Stock Sold by Loring Wolcott & Coolidge Fiduciary Advisors LLP MA
- Summary: Apple Inc. $AAPL Stock Sold by Loring Wolcott & Coolidge Fiduciary Advisors LLP MA
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNSVpRTXc5WDRsakZNVk9xLTRpYlptUXZJblQzcDhWS1JpdTFoSnB5eVJUZm1HRFdKQWdtOC0zTFVwdDVtam5vQU54N2tYUFlwSzZHRmhZODBXZ1psREZlbTVBbGlKVGVIdXFfblcyOFVQWDEwMFl4aWZaMkNsNTJ3bnJ3MWJmQ1NJc2FpSV9LUEdYVk5IUmhMOVJSLUpVQ0VuaVpHOW1jU3o1Nm9HNGZIM3FQWks0N2pRUzRKMG11UHhUeE5uTjFvUS11dUNLZUl3LWU1Yll3?oc=5>

### Apple Inc. $AAPL Stock: VUB Generali dochodkova spravcovska spolocnost a.s. Lowers Position
- Summary: Apple Inc. $AAPL Stock: VUB Generali dochodkova spravcovska spolocnost a.s. Lowers Position
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxOTVFJM0JrLU1tcUZLaDU4NkN1NlBucUlIaW5KZ1htblFsMVM4alRENmYtSmV0MHhnZFFDNW5mLWx3R0MxQ191YkJPZjFaV0FCLUg2V1puZEJDRlVwVWhKX3ZJRmRObE54Z3dHVVAwcVBnakNsWUUwY2VwVl9WaXp0M0JJdGZwVlE4NFlhcUcwZXlQWUhvR29oalZ0TG1PcmNFTVBEUVYtRFNLYmdmZXZVampPM1EtRmlZYzNyM29DY05aWE5pLWMwTmxpNHZZX2lSR0ZsbjdBYXdjVnhvcFNhUQ?oc=5>

### Apple Inc. $AAPL Stock Sold by B.O.S.S. Retirement Advisors LLC
- Summary: Apple Inc. $AAPL Stock Sold by B.O.S.S. Retirement Advisors LLC
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOdU5mOHNySXJMdGZnbDFJY2llUzBXS2J5OWVBS0licnFRYVBiaFhwTVEyX3Z3bzZTMUxFUWhjMXMyQkRTVjFFc3pheE9pMS1DNmxRNWYySDVzS3hyTjVFRVpKaGt3X2lBek9RQlN2ZUlyVm9kQWg1Y3IzMmc2LUVrN1FHSmZWMXFFNG9yVTV0TzExblBQTDFwWE1IODhzN3lGU3F1bWhRUXUySHNBcGhlemVUY21ELURTdEE?oc=5>

### Apple Inc. $AAPL Stock Sold by Slow Capital Inc.
- Summary: Apple Inc. $AAPL Stock Sold by Slow Capital Inc.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPZTcwQkk1LS1MS2o4TUl5MlpKU1Q5TktoSmRRcmJqZ0VzZFpDSXNfc0szSFlmanVXYllOQU0yaTZoVXp0ZjFRTGg2WTdCcy1NeVhYVDZBZTJkQ0dfTkdWTnZ3a01IdXplTURXSWppbzU0b0M1SllHM0VxUk1Nd2loTGJGRzRvOTBUUi12SklYMFBsWmRJWlpsSHdFMG9WTURpUFBxLUxhSGJNUQ?oc=5>

### Apple Inc. $AAPL Stock Sold by Nadler Financial Group Inc.
- Summary: Apple Inc. $AAPL Stock Sold by Nadler Financial Group Inc.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxON3BPQndiREdNOFVXNzdjeWhndTVfSHpsTDJBSExkSncwUy1JNm1ja183bmVyMXU1ZjJQdVJOWFBYZjB6VzEzY1lqVUpZcnFiYUpDcDhla3BnOV9sNzY2TWlkUDBYdjFqRHNTZDFUdVlFQXJyMk5BOUpRYnNxOUNETXZESGV4a0ItdWctRGtYM0wwSEV1Y2N3bHh0LUZYRUNVejlvM015QUlGQk55dlVvbjI0UVc0X3c?oc=5>

### Apple Inc. $AAPL Stock Acquired by One Wealth Capital Management LLC
- Summary: Apple Inc. $AAPL Stock Acquired by One Wealth Capital Management LLC
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNMmszLVZpbk1hTFowUEJDOURpTDBNVzV0V0dDaVI3SzUyU1dIU2pUUzU1NDJrSXhMd2V2TXlnTThqdmVOMWg1enlPajJYNkhsVENFOHBDUDU1MzROYWtFdHdMNDEyUEl2dFJqXzh1d21wTlZGSTBpZ1hVUS1TVEg1bjJTSnA2b1c0dnhmSXpneTQwRDBpcDRnbk5uUVdqeTdCdm9CT21zUFJfdWd3TUpBcFNGNkZyeXVwRTlwcWVJSjBiWmV0TVE?oc=5>

### AAPL Stock Posted Best Week In 4 Months Amid Nvidia Disruption: Apple Reportedly Plans Smart Glasses To Rival Meta Next Year
- Summary: Apple’s stock surged after announcing plans to launch smart glasses competing with Meta, marking its best week in four months amid Nvidia’s market disruption.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPaTZ2ZWQ2QTBxMk1iWTJ4ZXBGc3hpUDRHMDVVdFdMaGtkWVVkcEtzM2djWFpZQ1ZxTnYtUHFhMHFIbjFSSjhPSXVDWWsxdXlvQzQ1RDliaVNNUzR5QzZLWEl0UW9ROGx5RnZVdko4LWYzbWNqWEJORkJDTEVmY3ZObDgyaHNmZzRHaWpQN2ZCaDFQM05ja21J?oc=5>

### A $1,999 Sellout. What China Renaissance Sees in Apple (AAPL)
- Summary: China Renaissance's $1,999 sellout view on Apple.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPUVhYalN0S3o2VVRpNWZPTU9oWEZJZnlRNi1VU1pTY3VzUXFueTh3Um9IUWIzdjY4OW9EU3kwVG5QblI5MzcxUVg2Y3J3QW5KM3RuZGh3UmRJYTRBWVR0Ql9iZVAzb2JucTM5Qi1IQkl1bHNLQXpDeFltVzhqQm9mTXFneG5GSi1vQ25oSGY0VnBrSEI5a1hWb1d3VDU?oc=5>

### Apple (AAPL) Puts Tim Cook At The Center Of A Surprise CEO Search
- Summary: Apple announces a surprise CEO search, placing Tim Cook at the center of the process, signaling potential leadership changes.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxQZ2pUMi1tNld3R2xsYWtXRlNIck5ST3gyZVNBUE5tcE04d1Q5SWdJeUJaSjVVNm9kWHpVX3huOWQtTHFGbWxLNUY4TGsxMkFNX1BtUXdndVUxTnpDajhkdm5FMXROeXRIdDhCN05aQ3NiQXBqeEYtT21KRThBemZKSnhwVk1kZmxGVVhTZ053?oc=5>

### Apple Inc. $AAPL Stock: Kingswood Wealth Advisors LLC Grows Stake
- Summary: Kingswood Wealth Advisors increased its stake in Apple, indicating confidence in the company’s prospects.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPQlpNd1VpODBLbkxRZVY5MDFTWmRSZlpRVEE3cGlUSXhLT3FZRG55UmswMnhqR3lKYWhMRG5GRWtvV2tfNFh3eTRwUjRqT1I1MTFpVjdGSjMyY2NORWxzTHR6VWxBbDBsV1FVbXBZX1RtYVhscHByVFRpTnVSMjZRdm55cUJsdUg2UkJQREw2cjR2ZmpWUTFEVVFNb0JkUm4tQ296OUZQa1J4VTktTUVJd0VPM01IMFRwaUg2c0lwMWw?oc=5>

### Apple (AAPL) Executive Chairman Tim Cook Is Being Floated For A Top AI CEO Role
- Summary: Tim Cook is being considered for a top AI CEO position, reflecting leadership interest but no direct company action.
- Date: 2026-11-14 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQaklkY2pvYk9qNVZSMFVTdmwxdnlSU2NyeUo4QmRBUGlZbEdvb3JNdGo5NGppM0stTG81Y21wNHhFZExGcUlVTUVobkZqdGNPNVJBYVJxTjVCTlZfVDNZc2IxdjVBa1dQbFFXaTNwbm1sbkNfWjdoV0J3WDhGVW1faWdrNVVTcmc2anpteENuNFA5Nkg2M2FyNVFrWmQyUE9WQlYzaUoxYVFvS0FObG1NVXJQVnVDczNxaFdN0gHAAUFVX3lxTE5DLUppNThsaGw2R3dWRlFrVWtFRVNxaXpzRGVya1pEeU50ZlVBT0NzMXVCXzVxcWNfbHpBZU5YZ1FMQ2NYckZ4TWVzdlB6ZFUwSmhrV21zNTFVQldFZ25LLW1LNzBucDVhcF8tWTRfNFp2QUtuYU8xbWMzYWV1VG9mdTlTam14dnQ4U1ZTbFRqZGxILUY5WUduRmdmUHA0UGJuUlBZWXVMY1VMOWQtZzJqTmZJRHhRWVBCUFVxQUtQZg?oc=5>

### Apple Inc. $AAPL Stock Position Boosted by BG Investment Services LLC
- Summary: BG Investment Services increased its Apple holdings, signaling positive outlook for the company.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxOZTVsX3VDRnJuQ2tZVHpQTkRwTDFySUlGazBxX3lVX3lDOXU3LUJGcjNYR0ZjbnVfckN1SUJDVFFfdnU5eWwxMUlzZG5SVHZ5TmFLa2tWdmtnSFFEeHFiOEVLaEg2UVBwTzJEWDlGRjd0eDdmSC1BTWZMYk96TFZLaXdvTHhNU0ZDcTZTbFczXzBGQlpKX3F5WXhzT2xyYjZqdkJyMDZBelhlNm9VZGg5U0Y4Y2J0Y0F1NUIxX2R3LTFVNmxLV19J?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **39.28** | **45.63** | **30.04** | **11.70** | **5,114,019,971,072.00 USD** | **32.03** |
| MSFT | 26.42 | 7.99 | 18.61 | 18.80 | 3,759,436,726,272.00 USD | 0.57 |
| GOOGL | 14.82 | 5.22 | 18.05 | 24.70 | 3,444,778,729,472.00 USD | -1.44 |
| SONY | 19.91 | 2.88 | 0.30 | 10.30 | 155,497,807,872.00 USD | -8.28 |

Peers fetched as_of: 2026-11-17; AAPL reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-01-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 62,900,000,000.00 USD; period 2018-07-01/2018-09-29; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 29,789,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMioAFBVV95cUxOZEhVR1p4SVhoeEFLSTkwSUVoLW5RRG9JRmZxX1k5NVVpbExYRU1WTGw5clM4d2FKNllFMTlROVlVT25HQmdkRHpVZUJqMWptSlhkSk9RdmF4LTlDMlhQazFDU3ZlelhMRkJPMTJkOEl0UHYxZHpOY3lYSG1lU2piV0tzM2lvZXdmaDJTU0RueExWYmNJWU1uQU4tWW83Q1lZ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOc2xKSXl6YWFyMmtDeE1OcmZpLUNDUTh4cGxTZGt0TkhTd2VMWFVsR2J1ZGdJc1hOWVZvUFBrbW9ZMzlZZ19HUVducENSWjgtQzFOdG1MU1ZBcDU4MVhyM2Izc1RJclFyblhRQV9XNDNvUmwtMHA0ZllBZTlSQ2U0VFBpU294Y3N6ZXdtMzRCc2o4SkZvcEtNaklnYjY?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNMEp1cUF5TVRWX3FKVXJSNlNmR2F1c0hMdjR3cVpaS3JwRlVJbzBmQVp6LTY0MDVtb2h1aVBKSUZPSnI5a2lXX0dwc3ZTMjh3eDFWWjVMSUIyWHJPVHlCOHRJVzV1UzVSMzRLLTljODI3M080WWxldzNYS0kxUk40ZFQ1WkZNZGZBN1Q3RDc3WHZxWkJjNFZfOUNmZXBwQQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxOdDJER0dOZTdtdWwxU1FtekJMOFl1MVhYbDhHQ044RjB2NlVza1NDaUNRUVZMTGtLTlM4b19KTmZHazlrcXV4VTgtX0NSSldrU0hTVWl0Y05wdzlLXzRxUXFEVk01RTh0ZVBFQ0RKcVQtV2tsb2dsQ21RUEE1YVlXTjNORnd2RVJmaWU4RWRYYw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPMmlGdE5NTkRwTWthS2Y0ZmZ2TXg3TTAtQmZka1cxXzkxV25LbU9xM3VjeUFtM0dhLXhkSjBBWGJuMFVYZHFWYTdfdG5XcV82dFNLN2VhNW43VWI2Q0l3aUZibFYyZU9HaXNmNVc4ZkZaMUREdkEwcFpteFdZQ29wQnU4TUVHT3dHM0ZPV3NOaXNaNVFoNWxoMGdqMkFzWlRwOUl3dHVaOF9qWXlZeE5Lb1NFenF3SWpuczFIRm9Gdw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOYmt6MzR0X1VRdEVBYVF2Y1drN3B0RlpXRUtmOW9CX0ZFbE5kYUJXV0oxczZUckthVWxMTW1JeVM5bkZLaVE1QjhZSi1kazRpWUEyUHEySFFoZ21URmNfYVVtQ0Q0NEIwZTdldkpmOVc3akt0XzVxaXVvbFZ6d0ZmUzdxOFlPZkVvYUlRaUFtVU5CRTZ4S0E?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPZ0xRQ0RCX3RmbzdqVjRpTzAwSFZ0bTRGeTlCUzh5QXRpSlZRT0NWT3Y5YmhFU1AtdHA1ZmM1eGxDczBsdVFNUDYyd085VVJPaHFCRGZPZlZMWDZFX3hQM0p4M1UyQlZOYnlfRGY1eFNnbHFDSWdtUkN6TWE2R2VjQjlIZ09GODAxcDBmRVNUVTI1ME9xMks3WUo1U19nZ1I0ZEJQXzJ1R3VkRlU?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNekw4czk1V0dBR21SMWtoS1ozbkVuWUhPTTR5cEtWTmNTd3JrdHM3UWg5RWItekxCMnJVcUhrZXBDTkJ3aDdPdktucTRUYWtjazFCV1p4a0xyMzBsS3NrMXdvOGlmaEViOGM4MTd4MmZQOW9sN0JTbmQxY3pyRjlTUjk2eXBCa0QwWFR0N1REdHhMMmRfb0x3anhnWQ?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxPY1V2dU9TeHN5OV8yNllZS0RPeVNYd1cxeW5nWk5vV2loMm9oRjRoOFpJaEZPNFFfS3AyN3F3N1VvQkVHcW91Z0lwczlXdGw5RHA1MzVSanpNUTNIYlVzX21uNnRBb2lUcExIZGNWWEFKUC1ESDFPb3ZQVWtNYjgzWU40OXdHVlRSYWdvYWJqRXVxN1RRY1BneDMtaG85QnR1dGlsVTRhNi1DR3dfNzVQdzNPNVM?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxPWG1xRGdvdk1TNWc1UDdHWG5ScnZBSTQ4LVRFX085Z1E4bVpUcG94YXNUbHM3QTR5UUZnT3RSRnk2aWhkWWRBdmdjWkhtNE1RWnh1VTB4VkF3VGFyQ2JfSWw2MGN4SWNFeTdfRXV0eHg2emZieTBEWHFweHVOZTZFcE81eVQ5dDljcVVoNTZCM3ZxYWF4MUQyU1RpenFpVllpUHlpcEx3MGlEWWFNVjFfM0pQX281WG16dkNKY2trc3hiZFZuaktjbA?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNSVpRTXc5WDRsakZNVk9xLTRpYlptUXZJblQzcDhWS1JpdTFoSnB5eVJUZm1HRFdKQWdtOC0zTFVwdDVtam5vQU54N2tYUFlwSzZHRmhZODBXZ1psREZlbTVBbGlKVGVIdXFfblcyOFVQWDEwMFl4aWZaMkNsNTJ3bnJ3MWJmQ1NJc2FpSV9LUEdYVk5IUmhMOVJSLUpVQ0VuaVpHOW1jU3o1Nm9HNGZIM3FQWks0N2pRUzRKMG11UHhUeE5uTjFvUS11dUNLZUl3LWU1Yll3?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxOTVFJM0JrLU1tcUZLaDU4NkN1NlBucUlIaW5KZ1htblFsMVM4alRENmYtSmV0MHhnZFFDNW5mLWx3R0MxQ191YkJPZjFaV0FCLUg2V1puZEJDRlVwVWhKX3ZJRmRObE54Z3dHVVAwcVBnakNsWUUwY2VwVl9WaXp0M0JJdGZwVlE4NFlhcUcwZXlQWUhvR29oalZ0TG1PcmNFTVBEUVYtRFNLYmdmZXZVampPM1EtRmlZYzNyM29DY05aWE5pLWMwTmxpNHZZX2lSR0ZsbjdBYXdjVnhvcFNhUQ?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOdU5mOHNySXJMdGZnbDFJY2llUzBXS2J5OWVBS0licnFRYVBiaFhwTVEyX3Z3bzZTMUxFUWhjMXMyQkRTVjFFc3pheE9pMS1DNmxRNWYySDVzS3hyTjVFRVpKaGt3X2lBek9RQlN2ZUlyVm9kQWg1Y3IzMmc2LUVrN1FHSmZWMXFFNG9yVTV0TzExblBQTDFwWE1IODhzN3lGU3F1bWhRUXUySHNBcGhlemVUY21ELURTdEE?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPZTcwQkk1LS1MS2o4TUl5MlpKU1Q5TktoSmRRcmJqZ0VzZFpDSXNfc0szSFlmanVXYllOQU0yaTZoVXp0ZjFRTGg2WTdCcy1NeVhYVDZBZTJkQ0dfTkdWTnZ3a01IdXplTURXSWppbzU0b0M1SllHM0VxUk1Nd2loTGJGRzRvOTBUUi12SklYMFBsWmRJWlpsSHdFMG9WTURpUFBxLUxhSGJNUQ?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxON3BPQndiREdNOFVXNzdjeWhndTVfSHpsTDJBSExkSncwUy1JNm1ja183bmVyMXU1ZjJQdVJOWFBYZjB6VzEzY1lqVUpZcnFiYUpDcDhla3BnOV9sNzY2TWlkUDBYdjFqRHNTZDFUdVlFQXJyMk5BOUpRYnNxOUNETXZESGV4a0ItdWctRGtYM0wwSEV1Y2N3bHh0LUZYRUNVejlvM015QUlGQk55dlVvbjI0UVc0X3c?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNMmszLVZpbk1hTFowUEJDOURpTDBNVzV0V0dDaVI3SzUyU1dIU2pUUzU1NDJrSXhMd2V2TXlnTThqdmVOMWg1enlPajJYNkhsVENFOHBDUDU1MzROYWtFdHdMNDEyUEl2dFJqXzh1d21wTlZGSTBpZ1hVUS1TVEg1bjJTSnA2b1c0dnhmSXpneTQwRDBpcDRnbk5uUVdqeTdCdm9CT21zUFJfdWd3TUpBcFNGNkZyeXVwRTlwcWVJSjBiWmV0TVE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPaTZ2ZWQ2QTBxMk1iWTJ4ZXBGc3hpUDRHMDVVdFdMaGtkWVVkcEtzM2djWFpZQ1ZxTnYtUHFhMHFIbjFSSjhPSXVDWWsxdXlvQzQ1RDliaVNNUzR5QzZLWEl0UW9ROGx5RnZVdko4LWYzbWNqWEJORkJDTEVmY3ZObDgyaHNmZzRHaWpQN2ZCaDFQM05ja21J?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPUVhYalN0S3o2VVRpNWZPTU9oWEZJZnlRNi1VU1pTY3VzUXFueTh3Um9IUWIzdjY4OW9EU3kwVG5QblI5MzcxUVg2Y3J3QW5KM3RuZGh3UmRJYTRBWVR0Ql9iZVAzb2JucTM5Qi1IQkl1bHNLQXpDeFltVzhqQm9mTXFneG5GSi1vQ25oSGY0VnBrSEI5a1hWb1d3VDU?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxQZ2pUMi1tNld3R2xsYWtXRlNIck5ST3gyZVNBUE5tcE04d1Q5SWdJeUJaSjVVNm9kWHpVX3huOWQtTHFGbWxLNUY4TGsxMkFNX1BtUXdndVUxTnpDajhkdm5FMXROeXRIdDhCN05aQ3NiQXBqeEYtT21KRThBemZKSnhwVk1kZmxGVVhTZ053?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPQlpNd1VpODBLbkxRZVY5MDFTWmRSZlpRVEE3cGlUSXhLT3FZRG55UmswMnhqR3lKYWhMRG5GRWtvV2tfNFh3eTRwUjRqT1I1MTFpVjdGSjMyY2NORWxzTHR6VWxBbDBsV1FVbXBZX1RtYVhscHByVFRpTnVSMjZRdm55cUJsdUg2UkJQREw2cjR2ZmpWUTFEVVFNb0JkUm4tQ296OUZQa1J4VTktTUVJd0VPM01IMFRwaUg2c0lwMWw?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQaklkY2pvYk9qNVZSMFVTdmwxdnlSU2NyeUo4QmRBUGlZbEdvb3JNdGo5NGppM0stTG81Y21wNHhFZExGcUlVTUVobkZqdGNPNVJBYVJxTjVCTlZfVDNZc2IxdjVBa1dQbFFXaTNwbm1sbkNfWjdoV0J3WDhGVW1faWdrNVVTcmc2anpteENuNFA5Nkg2M2FyNVFrWmQyUE9WQlYzaUoxYVFvS0FObG1NVXJQVnVDczNxaFdN0gHAAUFVX3lxTE5DLUppNThsaGw2R3dWRlFrVWtFRVNxaXpzRGVya1pEeU50ZlVBT0NzMXVCXzVxcWNfbHpBZU5YZ1FMQ2NYckZ4TWVzdlB6ZFUwSmhrV21zNTFVQldFZ25LLW1LNzBucDVhcF8tWTRfNFp2QUtuYU8xbWMzYWV1VG9mdTlTam14dnQ4U1ZTbFRqZGxILUY5WUduRmdmUHA0UGJuUlBZWXVMY1VMOWQtZzJqTmZJRHhRWVBCUFVxQUtQZg?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxOZTVsX3VDRnJuQ2tZVHpQTkRwTDFySUlGazBxX3lVX3lDOXU3LUJGcjNYR0ZjbnVfckN1SUJDVFFfdnU5eWwxMUlzZG5SVHZ5TmFLa2tWdmtnSFFEeHFiOEVLaEg2UVBwTzJEWDlGRjd0eDdmSC1BTWZMYk96TFZLaXdvTHhNU0ZDcTZTbFczXzBGQlpKX3F5WXhzT2xyYjZqdkJyMDZBelhlNm9VZGg5U0Y4Y2J0Y0F1NUIxX2R3LTFVNmxLV19J?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
