# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:18:34.398084+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 11, 'ai': 7, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 11 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 20.83%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 95.7200 |
| Return 1D (%) | -7.6151 |
| Return 1W (%) | -11.8519 |
| Return 1M (%) | -15.1569 |
| Return YTD (%) | 26.0750 |
| Return 1Y (%) | 34.6957 |
| Annualized volatility (%) | 36.4327 |
| Beta vs SPY | 1.2101 |
| Max drawdown (%) | -26.0938 |
| Sharpe (rf=0) | 1.0035 |
| Downside deviation (rf=0, %) | 25.3956 |
| Sortino (rf=0) | 1.4397 |
| Historical VaR 95% (1D, %) | 3.0714 |
| Historical ES 95% (1D, %) | 5.3408 |
| Correlation vs SPY | 0.4515 |
| Tracking error vs SPY (%) | 32.6333 |
| P/E (trailing) | 31.08 |
| P/B | 7.51 |
| EV/EBITDA | 21.06 |
| Revenue growth (%) | 17.60 |
| Forward P/E (estimate) | 17.03 |
| Gross margin (%) | 64.52 |
| Operating margin (%) | 27.72 |
| Return on equity (%) | 27.32 |
| Free cash flow yield (%) | 2.96 |
| MA50 | 109.1828 |
| Close vs MA50 (%) | -12.3305 |
| MA200 | 101.4150 |
| Close vs MA200 (%) | -5.6156 |
| RSI (14, Wilder) | 30.1451 |
| MACD (12,26) | -2.5627 |
| MACD signal (9) | -1.4254 |
| MACD histogram | -1.1373 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 95.7200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -7.6151 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -11.8519 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -15.1569 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 26.0750 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 34.6957 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.4327 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.3956 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4397 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0714 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.3408 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4515 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.6333 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2101 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -26.0938 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0035 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.0259 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.5240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.7190 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.3190 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.9632 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 31.0779 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 30.1451 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.1373 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -12.3305 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -5.6156 -> Clearly below the moving-average trend level.

## TAILWINDS

### What Could Lift Cisco Stock?
- Summary: Speculation on factors that could boost Cisco's stock.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNd2JhNnJ3MTU4TTV4XzZWdUZVSFdZZWJGTW8xNXlZTGdYWEY5VG9jVmx2NTV5blFTUkU0R0gyMS1SLW9Dd095djJSWXVTQ0xCYURmR2R2c2JpLVhZZEQ3S09RamFPem5PbVVBVzdzNHZULWFJazB3Y0lQeXJnMS0yVGRKY05oUUpGNnBEZi01b3plUQ?oc=5>

### Cisco Systems Stock Outlook: Is Wall Street Bullish or Bearish?
- Summary: Questioning market sentiment toward Cisco's future performance.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNNmxUZjJVSDRsTWZrakJ0REVoVTJocTBrYlRaemh4MkV4Sk1DY0hETHFKYmJsNmxrd2VrZnJ2R1JEczV1VHVHaDhoNHM0Vl9feXY1UkFhWm9Qa01ySHVGaEhlWlUzY3ZzRmprcVRCZXFTd3k4V1RtbUE0SHJxUVBULUF6OGIydDBUZHBra2xZT2hfWTd0dGlRZ29pdUZJQQ?oc=5>

## HEADWINDS

### Cisco Stock (CSCO) Falls as Morgan Stanley Downgrades to ‘Hold’ Ahead of Q1 Earnings
- Summary: Cisco Stock (CSCO) Falls as Morgan Stanley Downgrades to ‘Hold’ Ahead of Q1 Earnings
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPLUxadF80a3hWNmZTTDBSZ1dZZmFvOEFyMERMUmRXYkhrVjBsTWJUU0RtWkRkOHE3Nm56MEdoRDN0RFctSEU1clp1RU5QS1FjSEYwZldIaGo2QkMyLUQ3b2FhZEZsV2ZoTDdxZTE2LVJPWWwzZDh1Y293cHJ2RS13bzZWQzBLNXNmRjlrLVJVUkZlblJFY3RSZ0doeDZwOFVqRGRkVXFsMXQxMWZoVkVj?oc=5>

### Cisco Falls 7% on Morgan Stanley Downgrade; Ciena Plunges 15%, Arista Networks Tumbles 10%
- Summary: Cisco Falls 7% on Morgan Stanley Downgrade; Ciena Plunges 15%, Arista Networks Tumbles 10%
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQS2l0el95RU5sYXRjNzI1V0c4Z09pX0xqYWN3ZWtwWGJTcG1XYzJWS29oWVZKaGNKWnJnX0tIZF9hT2pteWNLNzEtY3Baa2tFVXlVdDlmcVFoYURTRWtpbjh3bXpRdmRnd3MtcnBhMzhRcmg3NDBtUFdWdm5NU2o1ZWltVWN5SWRhVWtkMXZrZFJtUVNJOGdsVA?oc=5>

### Cisco Systems Inc (CSCO) Shares Fall 7.6% -- GF Value Says Still Overvalued
- Summary: Cisco Systems Inc (CSCO) Shares Fall 7.6% -- GF Value Says Still Overvalued
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxQeTVWX0JOTTlWcHgyMHpFMHpMaXdmVVRmQXFJVGhzQkZBNTdvYVRPcGlpTGZfX3JKS0EwN19SZUxWekVPYklsT1o5clhOdkt3NTdXSkFLSS1JRHM3SmJJNjdGX2lTbUxGbGlvSFRHWEJ5QUU5LTBIbjZXSllhMkEyb2N6SGp5MlpGNW1DcGhFampFQzRXMnBDNmhQREg3ck5ZSklfRlhiaHg2R2M?oc=5>

### Cisco downgraded at Morgan Stanley ahead of earnings (CSCO:NASDAQ)
- Summary: Cisco downgraded at Morgan Stanley ahead of earnings (CSCO:NASDAQ)
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQblVDV0FwWTctMnN1SV93b1RsZ2FoVml6QTh2X1JxMlBIRE9RRWFxcGtzYkxmYXR1VjRMT2VDNnB0blF4XzV3Q19hOE9RNkVfMjVEV2NGbnpQSHBZM3M2UkpQd1RCblVKSUREREkyRllyMGg3YTV3TVBPVXE3blNacHpSUXhzdVdmVkNUWXNsSmhXTGJY?oc=5>

### Cisco (CSCO) Downgraded by Morgan Stanley Amid Valuation Concerns
- Summary: Cisco (CSCO) Downgraded by Morgan Stanley Amid Valuation Concerns
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPdHFpSHpRV29FRFJDdUw4ZExsV2k1U21QZG4tLWJxVk96MGFIVzFnVm5GS0pMeEM4NHhQQms0ZzdLb1BkU2N4Qy1RWjBrSDNWaE1UYmQyWVhMOGxUeEVja28xWVQxYkhNb2VaSlNTa0NCa3JBTVVLSzYxcWlmNDBPMjVRX3BRazM0WEY4eWJYb0U1YTU3LUt2YjZSck5kWW1FSDZGVA?oc=5>

### Cisco Shares Slide After Morgan Stanley Cuts Rating to Hold, Trims Target to $120
- Summary: Cisco Shares Slide After Morgan Stanley Cuts Rating to Hold, Trims Target to $120
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidkFVX3lxTE9mV1RoSE0yWFNNQUc0emVCczZLSnlhY0lyd29RNHZsUWhLa3pFTE9VVWQwQTIzWFZtY0xqRnplRlU0TlpNMzBGSzBQdmFwT1RVa25CbjhSbV93SVFkSWVEY1RjdTRzMEF6ekstSmNWYy11elA2dkE?oc=5>

### Cisco Systems (NASDAQ:CSCO) Stock Price Down 2.8% - Here's What Happened
- Summary: Cisco Systems (NASDAQ:CSCO) Stock Price Down 2.8% - Here's What Happened
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPNm1MTERFbkduR2VwaFBIdENsVFNDMkgteGVmV2xHSEd6c1djRTZyYzBTRFNQY2dJZmwxN0xIOE1GbEwxRThjMXpyV2NUeFY3Z2dRZEVYZE1aUU9jcGtha0hZYWtzbTloNE5jYTRrQXE1NUUySUxNbmswTk5aUl9VZk1rRWhubDFRNHZnb0MyT0JFeElLVjc4Vi1zRDVwb0MzT1NJQ1BmaGJSQlJGU1pBZDhzTlZGb0E5OTBvT2t5dnBfQTQ?oc=5>

### Morgan Stanley Downgrades Cisco On AI Impacting Gross Margins
- Summary: Downgrade citing AI pressure on Cisco's margins.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxNenlRbU9KcTNickNGZy1DQ1dLTGlwb2FtaEhBZzlyRjBORUlwOWwxUEpCaG9Fbm10TGF5ZFk4RmNqQkZtQWYtbEFXR2FYUXlkNFVlaVpoOWpQVm1IempVdUVhb3ZLMjNkaE9OVEJjQlVsWnE3WnFLdEx6bDhjRlh4amY0YW5zWGs5YnJyLVhR?oc=5>

### Cisco Systems Inc Stock (CSCO) Moved Down by 5.91% on Nov 5: Drivers Behind the Movement
- Summary: Stock fell 5.91% due to identified drivers.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNdDFQV1p3VlpQeHIxMWNXc2tlZE5YUnQ3cHQ1emtpY2xmLTl2enBwaThKT0JBaE1GZTV2UC05X3d0UG9oR0FONXZqWTZnRzNwYUNORE5VT0lXcVJOOXpnUTJLeWhYUXBKeWNTVERlZlpBNUtFUC11MkdHcUhZcmtwZVJpVXI5Z1dIS1Vj?oc=5>

### Option Traders Show Moderately Bearish Sentiment on Cisco (CSCO) Amid Elevated Volatility
- Summary: Bearish option sentiment amid high volatility.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOQlpCYXRLYUtjVDRXWWRYa2dqVFRIN0Z3a3M5bHFtOTZLekYwZGpoWHdjZC03RzJNanVEcHF6eTZDLWhURmp4dWdyRVg4aHpDZ1BpamllLXZYb2NlcUVVbEllOTRFeld3SWdtRW1QRlBIdU0wZkpvb0xYaElSbV9laUd0MmtxMWhJV0l0aWVJZ1J6THFWX2tyZEUta0xyQkZmdi1nNjliMlpKdnVwVnBXNU9aUzVreEZLd0Jud0lvbnZ6dC1N?oc=5>

## CATALYSTS

### Cisco Systems options suggest 7.9% stock move on earnings
- Summary: Cisco Systems options suggest 7.9% stock move on earnings
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxONW9UVmJFTUktME85TDJORmowbzdRR0Vaa09jMThLN1puVXdyQ3lnZjNKcTRNakhnUUtzMU43bGVxdE0xbDFRMUM5d0JMN2hoVkotWjF3Q3hIMzl0U29YNUpGcWxET09ISnNaMFpMcE9pVElOVTJjTmxoeTdkSlJnS3g1RUlMRUdnX2NLcjRiTk5CWWZfQzBtdFJ2dHBaTV9peEFldDUyYjktR1J1dXUwOGpuTWdzaURf?oc=5>

### Cisco Systems, Inc. $CSCO Stock Sold by Boston Trust Walden Corp
- Summary: Cisco Systems, Inc. $CSCO Stock Sold by Boston Trust Walden Corp
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxNY052RGFzWF9wTjRocGpwak1TZzlXNGVIakpOZUd6UWpaOEx4TjZlUmc4bVhlQUxFU21oOUNMM1FDTzhxbndyM084SEFhRlRhOTl6c0JTZkFoNS0tbkhnM1NHbVpLMXpwVlJkSUdvNG5JZWNqMVlHd2JxSzZRTEx5aWNfOXdZYnFrM3pzRUgxczRKeDI4anBsNmxHMTM4REFWSkRfc2VNU25FVkt5YVZkb2xrT0pEbHRjRFYxUVpEUQ?oc=5>

### Cisco Systems, Inc. $CSCO Shares Sold by Integrity Alliance LLC.
- Summary: Cisco Systems, Inc. $CSCO Shares Sold by Integrity Alliance LLC.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxNWEFWc0dSd2pweHRpYU5oNFZSbEQ3QUVVeng4VzhOMmFlVUI2eHpxN0hfVHh4cWNwY2xPdlIwVFhzQWhwdklvZXdaY0pmeFQ5UkNfbWJzTk9IenMyb0Q0VW1tejRLZEFEZEc1RW9aZ0VraVdZTXB2RktpbVNFVHFTUWlaSEtVVURnTkJ5eWk0Tklpa2pRNnQ4a2d1eVdrc2ctY1I2UngzaXlfd3MxSkozd0xtenhPTGNTTDZQVFlB?oc=5>

### Cisco Systems, Inc. $CSCO Shares Sold by GRIMES & Co WEALTH MANAGEMENT LLC
- Summary: Cisco Systems, Inc. $CSCO Shares Sold by GRIMES & Co WEALTH MANAGEMENT LLC
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxNQV84T3ktclhDV180c1dZZXFWUGhRbmgxZXBudUVZeFpuNWR0TDZybXlub2lXODY3SDBwbWZiZ0Y2X2drRkVFRU02cWxIVWRNeXJ2all0dlV5MVgtcm5HQXg0MkRqczVSNnczUXBmd1VIVnpRMmt0N1RLai1kNUMxR2dYTS0wMk1lWF9lN09xNGw0N0RxczdPSmZEcVFXR093RTRZQlZyOVVxMDRFeVNVRi1ZNHBCRFNVMnRpaEVlRElMOVZyUk93QTBR?oc=5>

### Cisco (CSCO) Stock Looks Undervalued On Future Cash Flow Estimates
- Summary: Analyst suggests Cisco stock undervalued based on future cash flow estimates.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNRkVmNHFuMzZObmVHRkpVOEZZNFJmT3ZKQ0NGYjBtdTBQVFIwbko0Mk53UnFfNU05dTRPdE9MWXRKZWhjbVJ2dXJOdzJFaXBHWkNuZWxvNGRha0lKQ0o5OG82WXVpN0o2azdRV2dCQ3R1WE80QjB0dDUteTZjTG5NRU9YQWE1MFI5clJQaWIyUTNsXzBvVVpaM29FdjJZSlZ5QTlqSDdJc05zMmU2LVJzazVtMWlXcENGU0dGTzBCSEtxQXljNTdj0gHMAUFVX3lxTE1oM0RXNVdySG1lbmpDZ2gyYWpSNmFGRGdjR21kd3NHOURpZXFSTUdjMDVMaDJFc0c2emtWXzRfTnE2ckdoYjFjMjVMMWdQTTFmRUFQQy0zOFZwallqX1lhelQ0MHNmaGR0Mk5BTXRDM1lfSFNvX216UXlwVk1YaTktampMQXRseDdYdXhFcTEybzdFZmNNQzJEdmVOTVNQM0tMZllMZ05nVDBEUkhNUEpGS3JtSkp1bllURDE1SnZfOXZ5THRRbGRIdlNQZg?oc=5>

## RISKS

### Morgan Stanley Downgrades Cisco (CSCO) Ahead of Earnings, Shares Fall Premarket
- Summary: Morgan Stanley downgraded Cisco ahead of earnings, causing premarket share decline.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOUy1UQU9TNGtKODZ2eFdnZkJpZlNhMGV2OHp5ODN2RmZrTnRPZ0ZWZTRVaXZFblpGOFpDYWRJalVnUXRLNkctSjRRRUF3YUhZMHNmbUJQQV9uN3psaFdicVE3Rk5ORlRVcFl1WGR3bm1yZTVEYnJydTFiVkdOOTJTVExQS2dhMm5OX2RqWk1uS243ZzR6ZnhlQXE1aVlQY3pCUXd4dU9FRVhTSzUyWmhLdkxaMGRJQQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **31.08** | **7.51** | **21.06** | **17.60** | **377,384,435,712.00 USD** | **34.70** |
| ANET | 47.80 | 12.21 | 35.17 | 58.50 | 201,083,125,760.00 USD | 13.35 |
| FFIV | 26.33 | 4.42 | 17.65 | 13.30 | 17,710,260,224.00 USD | 26.47 |
| HPE | 25.82 | 2.21 | 10.56 | 33.70 | 58,620,846,080.00 USD | 89.61 |

Peers fetched as_of: 2026-11-05; CSCO reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-12
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-09-02
- Revenue (latest available single quarter): 12,844,000,000.00 USD; period 2018-04-29/2018-07-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 3,373,000,000.00 USD; period 2026-01-25/2026-04-25; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/858877/000085887726000132/csco-20260725.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikgFBVV95cUxNd2JhNnJ3MTU4TTV4XzZWdUZVSFdZZWJGTW8xNXlZTGdYWEY5VG9jVmx2NTV5blFTUkU0R0gyMS1SLW9Dd095djJSWXVTQ0xCYURmR2R2c2JpLVhZZEQ3S09RamFPem5PbVVBVzdzNHZULWFJazB3Y0lQeXJnMS0yVGRKY05oUUpGNnBEZi01b3plUQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNNmxUZjJVSDRsTWZrakJ0REVoVTJocTBrYlRaemh4MkV4Sk1DY0hETHFKYmJsNmxrd2VrZnJ2R1JEczV1VHVHaDhoNHM0Vl9feXY1UkFhWm9Qa01ySHVGaEhlWlUzY3ZzRmprcVRCZXFTd3k4V1RtbUE0SHJxUVBULUF6OGIydDBUZHBra2xZT2hfWTd0dGlRZ29pdUZJQQ?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPLUxadF80a3hWNmZTTDBSZ1dZZmFvOEFyMERMUmRXYkhrVjBsTWJUU0RtWkRkOHE3Nm56MEdoRDN0RFctSEU1clp1RU5QS1FjSEYwZldIaGo2QkMyLUQ3b2FhZEZsV2ZoTDdxZTE2LVJPWWwzZDh1Y293cHJ2RS13bzZWQzBLNXNmRjlrLVJVUkZlblJFY3RSZ0doeDZwOFVqRGRkVXFsMXQxMWZoVkVj?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQS2l0el95RU5sYXRjNzI1V0c4Z09pX0xqYWN3ZWtwWGJTcG1XYzJWS29oWVZKaGNKWnJnX0tIZF9hT2pteWNLNzEtY3Baa2tFVXlVdDlmcVFoYURTRWtpbjh3bXpRdmRnd3MtcnBhMzhRcmg3NDBtUFdWdm5NU2o1ZWltVWN5SWRhVWtkMXZrZFJtUVNJOGdsVA?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxNTkRiZEVMc2tZVEdlRUtnTTlGTTRiSDcwdmVGSVFkREI3eXdabUlXdTNGek1yeFY3eDBCNHpza2RISlprSlZKa2gzWEJjNmpTZ01IZmI2NmxNdDJyeS1mRVZBbGR1bnhFZ3dtbGQzWngwOU0yZjNCRy1XY3lBUHU1RHpkTUx0Nll5SG9sUTFXUzlxX3hYX1ZPMlV0ZWhfS3E3bWJlTkdyQ2QzUDBmajZsVUlQdW4wSDVYRlRvWmM3RUtRUksxZlVHXw?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxQeTVWX0JOTTlWcHgyMHpFMHpMaXdmVVRmQXFJVGhzQkZBNTdvYVRPcGlpTGZfX3JKS0EwN19SZUxWekVPYklsT1o5clhOdkt3NTdXSkFLSS1JRHM3SmJJNjdGX2lTbUxGbGlvSFRHWEJ5QUU5LTBIbjZXSllhMkEyb2N6SGp5MlpGNW1DcGhFampFQzRXMnBDNmhQREg3ck5ZSklfRlhiaHg2R2M?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQblVDV0FwWTctMnN1SV93b1RsZ2FoVml6QTh2X1JxMlBIRE9RRWFxcGtzYkxmYXR1VjRMT2VDNnB0blF4XzV3Q19hOE9RNkVfMjVEV2NGbnpQSHBZM3M2UkpQd1RCblVKSUREREkyRllyMGg3YTV3TVBPVXE3blNacHpSUXhzdVdmVkNUWXNsSmhXTGJY?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPdHFpSHpRV29FRFJDdUw4ZExsV2k1U21QZG4tLWJxVk96MGFIVzFnVm5GS0pMeEM4NHhQQms0ZzdLb1BkU2N4Qy1RWjBrSDNWaE1UYmQyWVhMOGxUeEVja28xWVQxYkhNb2VaSlNTa0NCa3JBTVVLSzYxcWlmNDBPMjVRX3BRazM0WEY4eWJYb0U1YTU3LUt2YjZSck5kWW1FSDZGVA?oc=5
- https://news.google.com/rss/articles/CBMidkFVX3lxTE9mV1RoSE0yWFNNQUc0emVCczZLSnlhY0lyd29RNHZsUWhLa3pFTE9VVWQwQTIzWFZtY0xqRnplRlU0TlpNMzBGSzBQdmFwT1RVa25CbjhSbV93SVFkSWVEY1RjdTRzMEF6ekstSmNWYy11elA2dkE?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPNm1MTERFbkduR2VwaFBIdENsVFNDMkgteGVmV2xHSEd6c1djRTZyYzBTRFNQY2dJZmwxN0xIOE1GbEwxRThjMXpyV2NUeFY3Z2dRZEVYZE1aUU9jcGtha0hZYWtzbTloNE5jYTRrQXE1NUUySUxNbmswTk5aUl9VZk1rRWhubDFRNHZnb0MyT0JFeElLVjc4Vi1zRDVwb0MzT1NJQ1BmaGJSQlJGU1pBZDhzTlZGb0E5OTBvT2t5dnBfQTQ?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxNenlRbU9KcTNickNGZy1DQ1dLTGlwb2FtaEhBZzlyRjBORUlwOWwxUEpCaG9Fbm10TGF5ZFk4RmNqQkZtQWYtbEFXR2FYUXlkNFVlaVpoOWpQVm1IempVdUVhb3ZLMjNkaE9OVEJjQlVsWnE3WnFLdEx6bDhjRlh4amY0YW5zWGs5YnJyLVhR?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNdDFQV1p3VlpQeHIxMWNXc2tlZE5YUnQ3cHQ1emtpY2xmLTl2enBwaThKT0JBaE1GZTV2UC05X3d0UG9oR0FONXZqWTZnRzNwYUNORE5VT0lXcVJOOXpnUTJLeWhYUXBKeWNTVERlZlpBNUtFUC11MkdHcUhZcmtwZVJpVXI5Z1dIS1Vj?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOQlpCYXRLYUtjVDRXWWRYa2dqVFRIN0Z3a3M5bHFtOTZLekYwZGpoWHdjZC03RzJNanVEcHF6eTZDLWhURmp4dWdyRVg4aHpDZ1BpamllLXZYb2NlcUVVbEllOTRFeld3SWdtRW1QRlBIdU0wZkpvb0xYaElSbV9laUd0MmtxMWhJV0l0aWVJZ1J6THFWX2tyZEUta0xyQkZmdi1nNjliMlpKdnVwVnBXNU9aUzVreEZLd0Jud0lvbnZ6dC1N?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxONW9UVmJFTUktME85TDJORmowbzdRR0Vaa09jMThLN1puVXdyQ3lnZjNKcTRNakhnUUtzMU43bGVxdE0xbDFRMUM5d0JMN2hoVkotWjF3Q3hIMzl0U29YNUpGcWxET09ISnNaMFpMcE9pVElOVTJjTmxoeTdkSlJnS3g1RUlMRUdnX2NLcjRiTk5CWWZfQzBtdFJ2dHBaTV9peEFldDUyYjktR1J1dXUwOGpuTWdzaURf?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxNY052RGFzWF9wTjRocGpwak1TZzlXNGVIakpOZUd6UWpaOEx4TjZlUmc4bVhlQUxFU21oOUNMM1FDTzhxbndyM084SEFhRlRhOTl6c0JTZkFoNS0tbkhnM1NHbVpLMXpwVlJkSUdvNG5JZWNqMVlHd2JxSzZRTEx5aWNfOXdZYnFrM3pzRUgxczRKeDI4anBsNmxHMTM4REFWSkRfc2VNU25FVkt5YVZkb2xrT0pEbHRjRFYxUVpEUQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxNWEFWc0dSd2pweHRpYU5oNFZSbEQ3QUVVeng4VzhOMmFlVUI2eHpxN0hfVHh4cWNwY2xPdlIwVFhzQWhwdklvZXdaY0pmeFQ5UkNfbWJzTk9IenMyb0Q0VW1tejRLZEFEZEc1RW9aZ0VraVdZTXB2RktpbVNFVHFTUWlaSEtVVURnTkJ5eWk0Tklpa2pRNnQ4a2d1eVdrc2ctY1I2UngzaXlfd3MxSkozd0xtenhPTGNTTDZQVFlB?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxNQV84T3ktclhDV180c1dZZXFWUGhRbmgxZXBudUVZeFpuNWR0TDZybXlub2lXODY3SDBwbWZiZ0Y2X2drRkVFRU02cWxIVWRNeXJ2all0dlV5MVgtcm5HQXg0MkRqczVSNnczUXBmd1VIVnpRMmt0N1RLai1kNUMxR2dYTS0wMk1lWF9lN09xNGw0N0RxczdPSmZEcVFXR093RTRZQlZyOVVxMDRFeVNVRi1ZNHBCRFNVMnRpaEVlRElMOVZyUk93QTBR?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNRkVmNHFuMzZObmVHRkpVOEZZNFJmT3ZKQ0NGYjBtdTBQVFIwbko0Mk53UnFfNU05dTRPdE9MWXRKZWhjbVJ2dXJOdzJFaXBHWkNuZWxvNGRha0lKQ0o5OG82WXVpN0o2azdRV2dCQ3R1WE80QjB0dDUteTZjTG5NRU9YQWE1MFI5clJQaWIyUTNsXzBvVVpaM29FdjJZSlZ5QTlqSDdJc05zMmU2LVJzazVtMWlXcENGU0dGTzBCSEtxQXljNTdj0gHMAUFVX3lxTE1oM0RXNVdySG1lbmpDZ2gyYWpSNmFGRGdjR21kd3NHOURpZXFSTUdjMDVMaDJFc0c2emtWXzRfTnE2ckdoYjFjMjVMMWdQTTFmRUFQQy0zOFZwallqX1lhelQ0MHNmaGR0Mk5BTXRDM1lfSFNvX216UXlwVk1YaTktampMQXRseDdYdXhFcTEybzdFZmNNQzJEdmVOTVNQM0tMZllMZ05nVDBEUkhNUEpGS3JtSkp1bllURDE1SnZfOXZ5THRRbGRIdlNQZg?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOUy1UQU9TNGtKODZ2eFdnZkJpZlNhMGV2OHp5ODN2RmZrTnRPZ0ZWZTRVaXZFblpGOFpDYWRJalVnUXRLNkctSjRRRUF3YUhZMHNmbUJQQV9uN3psaFdicVE3Rk5ORlRVcFl1WGR3bm1yZTVEYnJydTFiVkdOOTJTVExQS2dhMm5OX2RqWk1uS243ZzR6ZnhlQXE1aVlQY3pCUXd4dU9FRVhTSzUyWmhLdkxaMGRJQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
