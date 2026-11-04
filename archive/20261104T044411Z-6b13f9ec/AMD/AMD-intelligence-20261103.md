# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T04:51:10.310921+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 12, 'ai': 12, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 19 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 16.0%; oldest publication 2026-11-01

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 483.9000 |
| Return 1D (%) | 3.6544 |
| Return 1W (%) | -13.6294 |
| Return 1M (%) | -23.6642 |
| Return YTD (%) | 125.9526 |
| Return 1Y (%) | 86.3663 |
| Annualized volatility (%) | 69.5557 |
| Beta vs SPY | 3.3315 |
| Max drawdown (%) | -28.1143 |
| Sharpe (rf=0) | 1.2441 |
| Downside deviation (rf=0, %) | 44.7073 |
| Sortino (rf=0) | 1.9356 |
| Historical VaR 95% (1D, %) | 6.3184 |
| Historical ES 95% (1D, %) | 8.7057 |
| Correlation vs SPY | 0.6130 |
| Tracking error vs SPY (%) | 62.5327 |
| P/E (trailing) | 123.44 |
| P/B | 11.75 |
| EV/EBITDA | 81.69 |
| Revenue growth (%) | 50.10 |
| Forward P/E (estimate) | 30.11 |
| Gross margin (%) | 55.72 |
| Operating margin (%) | 17.25 |
| Return on equity (%) | 10.20 |
| Free cash flow yield (%) | 1.12 |
| MA50 | 548.7050 |
| Close vs MA50 (%) | -11.8105 |
| MA200 | 412.9436 |
| Close vs MA200 (%) | 17.1831 |
| RSI (14, Wilder) | 38.4098 |
| MACD (12,26) | -18.0796 |
| MACD signal (9) | -8.5950 |
| MACD histogram | -9.4846 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 274, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 483.9000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.6544 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -13.6294 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -23.6642 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 125.9526 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 86.3663 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 69.5557 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 44.7073 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.9356 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.3184 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 8.7057 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6130 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 62.5327 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3315 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.1143 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2441 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 30.1127 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 55.7240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.2500 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.1960 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.1192 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 123.4439 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.4098 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -9.4846 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -11.8105 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 17.1831 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD stock jumps 8% on earnings as data center revenue nearly doubles
- Summary: AMD stock jumps 8% on earnings as data center revenue nearly doubles
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTFBfVXVMaFFzOXpSSmhDS2xlZWZLZDk0V2w5MHpTSnZ3d2c5bkMzRDhwbzhURWpMMVcwX3ZiME8ybmU4UHR1ekdtVlUwRTYxcTI0T1dadVhheUQ0LVVpWnRqYjdmeDkxMGJKQXBkNUtpaEVKZVlXNEhYRdIBfkFVX3lxTFAwT0pLTUtFX3FhLU4tWFFuU3JjMXF4NWxpWFNVZEoxeTdqMVc2d201ZHRMdXV4cEg4VGNnd0RDRmhKbnNYZndMa1hhMzZ3Y0lUdk82SUprYVVibVZQT19vR05WaGZKZlBzcDFLZWNzczZkb0pDN180UTZ5MTRuUQ?oc=5>

### AMD forecast eases AI spending fears as data-center sales surge
- Summary: AMD forecast eases AI spending fears as data-center sales surge
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNM01ic0VHVkhaaTh2RV9KVV8zNHFCNW1TZnRlc29mMDg5T200aGRFZkdhd0JtYmtiZGt4LVJRdTdzWlV4dnhnRk9WVW5NWE1QWEFXSmhnZFVDNHpUVk94b0NFOEt4MXNLRWFmYTQzZnlZN3VvTGNtVzZFNnFHQVJ6NWlISXlsNFFBYnVVMnhXTVlOUHE0MWk2TWhYUFgtQ2Yzc1JzVHVRNmo5RmpvQ3Qwc3E3bkJVQTRnQ2JIX2x5NVg?oc=5>

### AMD Stock Jumps on Big Earnings Beat
- Summary: AMD Stock Jumps on Big Earnings Beat
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidEFVX3lxTE9mcnlEQzhqWExyWFlMNDhsWkRvc2VrVmtkR2tqUXJzQWZBWGh2UzMySGZqUjhEN3dQcFhEWGpUczZnUHJ3WFB4cEJOUDhIMHlwaGxpRGI4YmlUclBaVkVBWHFoNmhBckFUU1ctUllKaF96bTB6?oc=5>

### AMD Stock Pops on $17B Q4 Revenue Guide. Traders Shouldn't Overlook a $3B Inventory Gamble and Collapsing Free Cash Flow.
- Summary: AMD Stock Pops on $17B Q4 Revenue Guide. Traders Shouldn't Overlook a $3B Inventory Gamble and Collapsing Free Cash Flow.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8wFBVV95cUxNRThLTzdDblZFVl9UR0FwWUxGaEJjV3IydzZ2b0JldC1fd0JiMkY2UlNBVUZ5YU01cUdGdnY5eU9TWmhZOElTVU1ocHlISERaRVplVFBvWHBQYk9tcHVOR3pFeVdkU18yX0lITHB2eGFxWXZyUS1hbkVtQmhSMHlRSm5IU3pybG1UZVJUY1FNOXg4RGFwckg1SmM1c0xNZTVwUEd6QzRBOXExMEQ5eUdFemdGVWI5T1BvNlpnS21Ba1VYUGlIcTRJRTlPbHpUV3ZOa0h2RFc5Um5GTUF0N3YzdkwxcXpwZ2ZPSmpxaFZmRmhmWms?oc=5>

### AMD Advances 5%, Intel Rises 4%, Marvell Gains 2% as Chip Stocks Bounce Ahead of AMD Earnings
- Summary: AMD Advances 5%, Intel Rises 4%, Marvell Gains 2% as Chip Stocks Bounce Ahead of AMD Earnings
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNZGt2UGdvbUNTNWlLYnZUTDM0NEI2X01iZVNTbXg4Yk5ib3NSN2VNTFEtR0JDMkVFNlgteFkzRU5Rc21VSlo4VnFkRU1FQnlYeU16Z2FIeUY4a1ZuN1o2cS1LaHlGR0ZNR3VwYnBKTUNuZjd0ZFNYLTZFN3pWajdzRDByN2MzV3pyYzRhVEdyLWlLWVJMUFNUeU91ZWxkS2ZZYzRlN0p0MXhQUjNsazR1cGdQWG1UZW1rRTZ2TEJ2MzRIT0R4SVZxeU9tTmw?oc=5>

### AMD Q3 2026 earnings results beat EPS and revenue expectations
- Summary: AMD Q3 2026 earnings results beat EPS and revenue expectations
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE9JVzhWdFlFYklTUVd0b0kwY1M0eUxmQXpXNzI2RUhRbGpEQUlwemhkRTFlQVRqUVp6T2d3U2lFM3hjTG11WFRHU3RlaWJ4c3R5RWEtWlAtZGlDVlZKVmVtUzZSMmhtTlFFQjRtR21tTF9BN0xLdmxHZw?oc=5>

### AMD Needs a Huge Outlook to Avoid Intel’s Fate as AI Fears Rise
- Summary: AMD Needs a Huge Outlook to Avoid Intel’s Fate as AI Fears Rise
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNRW9XeVZ4N0oxZjlNajFBS0ZXT2RDTE02dktLYXJad082NXU5NWctVkQ2aE1iZ01uLWt4WlZXUW51ZUk0ZzRHUWtYd0dGblRReV94empxQlVBMEJjNHBLcExfQWV4aGxIWktWaG04S0tydDdJb1NGSExIN0hGX1hVa04tYlRuQzk3V0kwQ1JSMFRUNkUzRFczU3cwZ1RObTctVUNlUVFrczVpLW9TVTA1NkxGMUI?oc=5>

### Advanced Micro Devices (AMD) Q3 Earnings and Revenues Top Estimates
- Summary: Advanced Micro Devices (AMD) Q3 Earnings and Revenues Top Estimates
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQTTR5RzFFTzBLSlo0d0M0NHZqVG1IQ3NuRDQ0Qk82MzRGTEJvNHE0WHpVMnp3dG1IbnBKMVExVWpRYm5uTVpUT1YzcEVnU2dyYXJQQVFRblRDTVFmWG1SWWFVSDlLWlJ4blZUQkc0VlZ3VnozN0RFU1I5cEROYUZtcVJYazl0aTBuTHcyU1B1ZU9kTE9LWWUxUjhHZUNaQ1FtSGxWb0lkdw?oc=5>

### AMD Q3 Preview: Expert Says ‘Growth Story Remains Impressive,’ Can Earnings Send Stock Back to Highs?
- Summary: Positive analyst outlook on Q3 earnings, suggesting potential upside for AMD stock.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxPYmpQbzdwSUE4a2NJZmpKQ0lGaE1PUHRvbk9MZmlGT2w2WHg3M1NtSGcyMlpJdjZ0OFE5NDJyQUpsSGdnLWlVaC1TRDlDdThtZmZZaTVVcnQ1MlNiS09BM1NuTWViM1NqN0ZFX2c0bGRsNkdjaV9Tb18tbzBYX3JjN3lkQm9IR3EwWXRZblNlcl8wZ2hqd3dTejJ3ZXZGN2R5emZ3ZFRaSGdlR3RCcWpYMEFtTDVmcUh0NUV2bWdCamhEb01fSjRIQUh5aG5NdkhLTW15ZkgxbnBpdFNaeFQ1R1BLaw?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### AMD Forecasts 66% Q4 Growth on AI Chip Demand: Rapid Earnings Reaction
- Summary: AMD Forecasts 66% Q4 Growth on AI Chip Demand: Rapid Earnings Reaction
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQTHNVVjZCWm5ncUFkZUJ0ai1GNVdQREdBTlpBSzRFMDAyUUVzNGFtR09PdDFRUnJlX2RuZmxlcU80NFdvVVpsZHVCeExzTjNrc3NOeTMxenBwMHVqWUw2XzdYa1VrWDR1SUFnQkt6UXYwOEFsdnZyaDRuTmVIQ0RtR2Q3YVprS3hOWWNNSlRJU081SWF5d0E?oc=5>

### Advanced Micro Devices, Inc. 2026 Q3 - Results - Earnings Call Presentation (NASDAQ:AMD) 2026-11-03
- Summary: Advanced Micro Devices, Inc. 2026 Q3 - Results - Earnings Call Presentation (NASDAQ:AMD) 2026-11-03
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxOQVFodFk5ZTYxa3RWRmtsTDJYbHVYWGlBZVNGMXN0VVlyXzBzMkRiZS1jSUE0SFM2RGZVN0FNVWRJTHNJb09PLWlKOERJbWNXWURlT2xqVXpfdlFHU2VIUkppQWh3U1pRcGhnTXBLck9jemZOWFZ3Q2djXy1QV0NJUU16WDNIa1hIS1cwaDhUWW1ZbkpIRW5uRXRvOU1xaExUQXAxakRkUWliUnE4MkUw?oc=5>

### Advanced Micro Devices (AMD) Set to Report Q3 Earnings Amid Elevated Market Expectations
- Summary: Advanced Micro Devices (AMD) Set to Report Q3 Earnings Amid Elevated Market Expectations
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxOamd6dmlkYzJDbHY4cDVQNWkxZVQya3FoR295Q0Q2WmdoWHRpajFSYzkyejhWVWtnWnVGXzhSZ2tnN3FnMEdSRzB6aE9Pa1RxS0VQN3NBUDlJdE1EeDFLNFk2cHVkbUo3ZDBmYjNnQWJBRGkxMGVtcVlnQ3ZKRkNqaXFTSDA1YUF2STJIdkpYOXdPbnIxeWdEM1VsU3lnMmJzQ3lvY25CMVVyaHB2d1dlelhFWWhCN3ZMWVY1TnNST0Nsc28?oc=5>

### AMD has been crushed into earnings. Here’s one way to trade it
- Summary: AMD has been crushed into earnings. Here’s one way to trade it
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNUTkwNkpvdTJyX05fdUJGY0ZvZUtuTnhtTXJzM1FIQ3U5T2JxVG1pVVRiWTlVVFg4X3J1aURPWEI5X1pMZGFjQktfUjJoUnF3bTMyMFI0WGVIbmVINXktSmJEQ0duV2R1cEtoRzNNR2ZYcllPbjNGU3VJNWtVeGdXV2NCSHZnTmlPSms1ZF9HWVdfVWdhY1R1UWFVejNoQdIBowFBVV95cUxQb0MtZXNHNHRfaGVjU1RuNlRJTUxnZnFER0N1czM5NTM2NS11TmpLVFRPTV96R05iSFZqZmE1ZVZMU1NKRWlQeXVRSHlqY2N2RWlmdEM0UkJ1MU11OTF6LUZMQWVzMmhBc2o2SzRqU3lwQnBDLWJyUnotbVRTVERTMHV3SjFlSS13SUxKeU03ZVBtNmJuTWtiWi1hVlN2VU44NHo4?oc=5>

### Ahead of Advanced Micro Devices Earnings, Here’s What Barchart Data Says Comes Next for AMD Stock
- Summary: Barchart data predicts next moves for AMD ahead of earnings.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQbXJodzQtaWtBSi1tRFpVZ1VyQ0tObE5BOU5uY2htQU4ya0Fncm1ITE5xYXhoNlp5NUlwTGIxQ0ZfejExYzZvMXJYSUg0bUo4bE1fU3lOSTgyeS11U0YzRTZEODZncjVvTmtjeTdwWHJSMVVNY2E1QTlSbTdJMnpfZV92NUhSSEM4eGNjN0JyenFCWEo2OURpNmt6Z1AwaXhqMFVEVWgxa2NTbUJkSU92V3ZRVEVUeGgxaXhma2N6aXFXWjRyaGNTbkVWT1hkT3VuZzBYWlV3?oc=5>

### Here’s How Much Traders Expect AMD Stock to Move After Earnings
- Summary: Traders forecast AMD stock movement post-earnings.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOUzk2TFExUnNScHk1cVdXaHlHMGUxWGhoQVlIWDY3MnE3NnctbVhnYUtERlZFTEw1bjFuVmo5TkRVZC11WWhncHFWb3IybUF3ZjYyWU1kRmlYWTVoOENVaVNHVmY3aVhNZU00VFJfX0VHem1ZRU1mYURPMUxBQVVzZkxKQnVZdW5PR2FoMm1PZnZCeDlTUDQwTTJR?oc=5>

### AMD Beats Wall Street Expectations as it Pivots to Data-Center First Status
- Summary: AMD exceeded earnings expectations, shifting focus to data centers.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQTS1ackJyUFczU0ZLRnVmUkF2M2M2MUtueVFjd3ZpOEVkSlJQRWY3eUFNa2g2MVlHOTJDZTROanJCRkMzN0k0S0s2WWh6c2VMVW84VklCRmNBdW5CcmlMYzFXX2RpNmp2UDNPbjNWOFZRMVJUYWtyQkcxX0NPTE1FZU1TXzQ4d2VmaXZkNEVRNTRsQUVPTlUtcXIxRUg5endOZVZyT29sYmtEbmhCQ2pxUA?oc=5>

### AMD Forecast Exceeds Estimates After AI Chip Demand Soars
- Summary: AMD's forecast surpassed estimates amid rising AI chip demand.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQYURlOUxxRUMybEdmbkJoTHZiZEVTTUtCN0gyZ1RsV0s3YlEteXR1NFZIWDNwXzJKTUdCRUpJY0RWNlRqVC02M0VaMFgtY0piUFNGSkhKQmZ3bTVwMHFERHN6ZExPSnVFbWdBWDYxQnNnX0RJRnF6QVlld0FBeDhySGlrUEZ4bEtmWkkybFFVRU9EcnhRd2F5c1M1eGc2OFk5VG95X0dUa1dWUGhPZzJJ?oc=5>

### AMD Posts Beat-And-Raise Report On Record AI Data-Center Sales
- Summary: AMD beat earnings and raised guidance on record AI sales.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE1XUlpyMXlqcVpLcWt5MHZGLWJZd1FXVDlUTDlMTUhrMjVuOGNtMmhDUmFsang0MVN4RmRTR0o3TFk2Zndka1ZkWWp1QzViaEhkbmcxdXpZejRKWEV2enFDb3NZNmNzb3R5STEtclNmZk1DOUxQemZWQQ?oc=5>

### Advanced Micro: Q3 Earnings Snapshot
- Summary: AMD reports Q3 earnings, providing financial performance snapshot.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxQOU9NRDc2TDFnalJoMGRGU2lHaWljdGl6ZkR5RGpsT0pGT2xjcElWVWRoNHdneXM3TEc2YWMwcDZKVHcyTlg1MVQ1Z0tSd1FPQnk0Z2s5ZjVuR1pJVXI2OU5tcjRVZ1JOVElTRzBQNkQ1SlJkQ2x4Ny1DWGpGZW1KbENyRDU0SExNZ2hLOHlsOTQyNW82RU5XNWpudEIwRDVJbU5kZlZzTW9zWkZ0dEpJUHkxZkdTbGNxaDFzek01ODJ0T0tRa2hvOUMxWWEtQQ?oc=5>

### 23 Big Funds Bought Advanced Micro Devices Last Quarter. Is It a Buy Before Earnings?
- Summary: Institutional buying noted before earnings, indicating potential support.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTE1nX3FtNWcyRXozTmx1Qzk5ZGhPU2tudFJpZDhFSzBzRnZ1bzNTMVlsNnFjbXdKeDExRWtzQTRLZEdXblZrZE1vV0k4NlByeFcwYm92WnRmRU5rS1BjSmozUG0zb1NULUtoZ1RVM2tMbHNrR3hTSTJJOTRYSVk?oc=5>

### ‘Wait for the Big Drop,’ Says Investor About AMD Stock
- Summary: Investor cautions on potential price decline, reflecting negative sentiment.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQd0FNLUhKUzQyRThDUEFVbFRuMTFTbS15Zjd0VHRRV2J3alQ4c194UUpCZDlnTXEtRWtNMlFpVVJJaG8xSEVaRC1EbFZ6Q3NlQ0lvbnlEb0h2Q0pvbTRtZjkxMDlqM1ltUjdLcUVlU2ZySkZFYUgxUC1YcE1KUGRibUM2UTNFaXFWWEJzbTZTQWJoVzQ?oc=5>

### AMD Stock $466 on Results Day: Bull $510, Bear $425
- Summary: Stock price at $466 on results day, with bullish and bearish targets.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNQkdaemd0bjhYUDFfOUppbkVOMTNZclhORHVIWWx5czZTRjAtM2hXMHBzMmJTeG1JSWJJSVlLOWVrandaa1hFbWYyNmhzVFA2VmRkR1ZOQldJR0NGZ2lfbnlERE5KOWNQdkY3cXI0RUxTNHg5T2tVVE5VM2lVMHZNX1I4ZEZibW44enp2NWREa1lreXVZYTg3Mg?oc=5>

### AMD Issues Upbeat Fourth-Quarter Revenue Guidance Following Third-Quarter Beat
- Summary: AMD provides optimistic Q4 revenue guidance after Q3 beat.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQakI0aDZPeGllNllmNFZOa19YWU05NXZzeEJ4MHVSeFROVWZMWjNrM2hqNnBWbnR1RUxLUWNLYkRKTFZBMHg4SlBmd00wR1Myd1NpU2lBYURVRUlaUGZfUWxxZ1l3XzBNdnNVek8wc0dVWlZialZURXhraEFrRUUwdS1FQmVHMVB2azhyZmg0RzJCeVQzZC1qRVhER1E4dw?oc=5>

### AMD data center revenue nearly doubles as Q4 outlook beats expectations
- Summary: AMD's data center revenue nearly doubled, and its Q4 outlook surpassed expectations, signaling strong performance.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxORXdhTXZuLVo0elFUcHM2WWpSWWdOM1BHTTZUZktFSHViVnl2eS0xbkVSSTF4N19tZ1p5MW1hUkVTTUswdjk5dllMbWVyT0xaU1BHWjlsLVNnLWdWRzlFeTZWQVJVSUt6S3hRWlQ0UWZ4YzFySzFhZDkwcnY3Wk1mSE5idFVVVnV4LURCRDlTeFdLaVpadVBKSkRpUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **123.44** | **11.75** | **81.69** | **50.10** | **789,954,625,536.00 USD** | **86.37** |
| NVDA | 25.55 | 21.80 | 24.63 | 105.90 | 4,990,943,363,072.00 USD | 0.15 |
| INTC | N/A | 2.80 | 17.49 | 20.90 | 321,823,244,288.00 USD | 53.29 |
| AVGO | 41.16 | 15.91 | 31.02 | 85.50 | 1,585,465,786,368.00 USD | -7.71 |

Peers fetched as_of: 2026-11-03; AMD reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: N/A (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMieEFVX3lxTFBfVXVMaFFzOXpSSmhDS2xlZWZLZDk0V2w5MHpTSnZ3d2c5bkMzRDhwbzhURWpMMVcwX3ZiME8ybmU4UHR1ekdtVlUwRTYxcTI0T1dadVhheUQ0LVVpWnRqYjdmeDkxMGJKQXBkNUtpaEVKZVlXNEhYRdIBfkFVX3lxTFAwT0pLTUtFX3FhLU4tWFFuU3JjMXF4NWxpWFNVZEoxeTdqMVc2d201ZHRMdXV4cEg4VGNnd0RDRmhKbnNYZndMa1hhMzZ3Y0lUdk82SUprYVVibVZQT19vR05WaGZKZlBzcDFLZWNzczZkb0pDN180UTZ5MTRuUQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNM01ic0VHVkhaaTh2RV9KVV8zNHFCNW1TZnRlc29mMDg5T200aGRFZkdhd0JtYmtiZGt4LVJRdTdzWlV4dnhnRk9WVW5NWE1QWEFXSmhnZFVDNHpUVk94b0NFOEt4MXNLRWFmYTQzZnlZN3VvTGNtVzZFNnFHQVJ6NWlISXlsNFFBYnVVMnhXTVlOUHE0MWk2TWhYUFgtQ2Yzc1JzVHVRNmo5RmpvQ3Qwc3E3bkJVQTRnQ2JIX2x5NVg?oc=5
- https://news.google.com/rss/articles/CBMidEFVX3lxTE9mcnlEQzhqWExyWFlMNDhsWkRvc2VrVmtkR2tqUXJzQWZBWGh2UzMySGZqUjhEN3dQcFhEWGpUczZnUHJ3WFB4cEJOUDhIMHlwaGxpRGI4YmlUclBaVkVBWHFoNmhBckFUU1ctUllKaF96bTB6?oc=5
- https://news.google.com/rss/articles/CBMi8wFBVV95cUxNRThLTzdDblZFVl9UR0FwWUxGaEJjV3IydzZ2b0JldC1fd0JiMkY2UlNBVUZ5YU01cUdGdnY5eU9TWmhZOElTVU1ocHlISERaRVplVFBvWHBQYk9tcHVOR3pFeVdkU18yX0lITHB2eGFxWXZyUS1hbkVtQmhSMHlRSm5IU3pybG1UZVJUY1FNOXg4RGFwckg1SmM1c0xNZTVwUEd6QzRBOXExMEQ5eUdFemdGVWI5T1BvNlpnS21Ba1VYUGlIcTRJRTlPbHpUV3ZOa0h2RFc5Um5GTUF0N3YzdkwxcXpwZ2ZPSmpxaFZmRmhmWms?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNZGt2UGdvbUNTNWlLYnZUTDM0NEI2X01iZVNTbXg4Yk5ib3NSN2VNTFEtR0JDMkVFNlgteFkzRU5Rc21VSlo4VnFkRU1FQnlYeU16Z2FIeUY4a1ZuN1o2cS1LaHlGR0ZNR3VwYnBKTUNuZjd0ZFNYLTZFN3pWajdzRDByN2MzV3pyYzRhVEdyLWlLWVJMUFNUeU91ZWxkS2ZZYzRlN0p0MXhQUjNsazR1cGdQWG1UZW1rRTZ2TEJ2MzRIT0R4SVZxeU9tTmw?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTE9JVzhWdFlFYklTUVd0b0kwY1M0eUxmQXpXNzI2RUhRbGpEQUlwemhkRTFlQVRqUVp6T2d3U2lFM3hjTG11WFRHU3RlaWJ4c3R5RWEtWlAtZGlDVlZKVmVtUzZSMmhtTlFFQjRtR21tTF9BN0xLdmxHZw?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNRW9XeVZ4N0oxZjlNajFBS0ZXT2RDTE02dktLYXJad082NXU5NWctVkQ2aE1iZ01uLWt4WlZXUW51ZUk0ZzRHUWtYd0dGblRReV94empxQlVBMEJjNHBLcExfQWV4aGxIWktWaG04S0tydDdJb1NGSExIN0hGX1hVa04tYlRuQzk3V0kwQ1JSMFRUNkUzRFczU3cwZ1RObTctVUNlUVFrczVpLW9TVTA1NkxGMUI?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQTTR5RzFFTzBLSlo0d0M0NHZqVG1IQ3NuRDQ0Qk82MzRGTEJvNHE0WHpVMnp3dG1IbnBKMVExVWpRYm5uTVpUT1YzcEVnU2dyYXJQQVFRblRDTVFmWG1SWWFVSDlLWlJ4blZUQkc0VlZ3VnozN0RFU1I5cEROYUZtcVJYazl0aTBuTHcyU1B1ZU9kTE9LWWUxUjhHZUNaQ1FtSGxWb0lkdw?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxPYmpQbzdwSUE4a2NJZmpKQ0lGaE1PUHRvbk9MZmlGT2w2WHg3M1NtSGcyMlpJdjZ0OFE5NDJyQUpsSGdnLWlVaC1TRDlDdThtZmZZaTVVcnQ1MlNiS09BM1NuTWViM1NqN0ZFX2c0bGRsNkdjaV9Tb18tbzBYX3JjN3lkQm9IR3EwWXRZblNlcl8wZ2hqd3dTejJ3ZXZGN2R5emZ3ZFRaSGdlR3RCcWpYMEFtTDVmcUh0NUV2bWdCamhEb01fSjRIQUh5aG5NdkhLTW15ZkgxbnBpdFNaeFQ1R1BLaw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQTHNVVjZCWm5ncUFkZUJ0ai1GNVdQREdBTlpBSzRFMDAyUUVzNGFtR09PdDFRUnJlX2RuZmxlcU80NFdvVVpsZHVCeExzTjNrc3NOeTMxenBwMHVqWUw2XzdYa1VrWDR1SUFnQkt6UXYwOEFsdnZyaDRuTmVIQ0RtR2Q3YVprS3hOWWNNSlRJU081SWF5d0E?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxOQVFodFk5ZTYxa3RWRmtsTDJYbHVYWGlBZVNGMXN0VVlyXzBzMkRiZS1jSUE0SFM2RGZVN0FNVWRJTHNJb09PLWlKOERJbWNXWURlT2xqVXpfdlFHU2VIUkppQWh3U1pRcGhnTXBLck9jemZOWFZ3Q2djXy1QV0NJUU16WDNIa1hIS1cwaDhUWW1ZbkpIRW5uRXRvOU1xaExUQXAxakRkUWliUnE4MkUw?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxOamd6dmlkYzJDbHY4cDVQNWkxZVQya3FoR295Q0Q2WmdoWHRpajFSYzkyejhWVWtnWnVGXzhSZ2tnN3FnMEdSRzB6aE9Pa1RxS0VQN3NBUDlJdE1EeDFLNFk2cHVkbUo3ZDBmYjNnQWJBRGkxMGVtcVlnQ3ZKRkNqaXFTSDA1YUF2STJIdkpYOXdPbnIxeWdEM1VsU3lnMmJzQ3lvY25CMVVyaHB2d1dlelhFWWhCN3ZMWVY1TnNST0Nsc28?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNUTkwNkpvdTJyX05fdUJGY0ZvZUtuTnhtTXJzM1FIQ3U5T2JxVG1pVVRiWTlVVFg4X3J1aURPWEI5X1pMZGFjQktfUjJoUnF3bTMyMFI0WGVIbmVINXktSmJEQ0duV2R1cEtoRzNNR2ZYcllPbjNGU3VJNWtVeGdXV2NCSHZnTmlPSms1ZF9HWVdfVWdhY1R1UWFVejNoQdIBowFBVV95cUxQb0MtZXNHNHRfaGVjU1RuNlRJTUxnZnFER0N1czM5NTM2NS11TmpLVFRPTV96R05iSFZqZmE1ZVZMU1NKRWlQeXVRSHlqY2N2RWlmdEM0UkJ1MU11OTF6LUZMQWVzMmhBc2o2SzRqU3lwQnBDLWJyUnotbVRTVERTMHV3SjFlSS13SUxKeU03ZVBtNmJuTWtiWi1hVlN2VU44NHo4?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQbXJodzQtaWtBSi1tRFpVZ1VyQ0tObE5BOU5uY2htQU4ya0Fncm1ITE5xYXhoNlp5NUlwTGIxQ0ZfejExYzZvMXJYSUg0bUo4bE1fU3lOSTgyeS11U0YzRTZEODZncjVvTmtjeTdwWHJSMVVNY2E1QTlSbTdJMnpfZV92NUhSSEM4eGNjN0JyenFCWEo2OURpNmt6Z1AwaXhqMFVEVWgxa2NTbUJkSU92V3ZRVEVUeGgxaXhma2N6aXFXWjRyaGNTbkVWT1hkT3VuZzBYWlV3?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOUzk2TFExUnNScHk1cVdXaHlHMGUxWGhoQVlIWDY3MnE3NnctbVhnYUtERlZFTEw1bjFuVmo5TkRVZC11WWhncHFWb3IybUF3ZjYyWU1kRmlYWTVoOENVaVNHVmY3aVhNZU00VFJfX0VHem1ZRU1mYURPMUxBQVVzZkxKQnVZdW5PR2FoMm1PZnZCeDlTUDQwTTJR?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQTS1ackJyUFczU0ZLRnVmUkF2M2M2MUtueVFjd3ZpOEVkSlJQRWY3eUFNa2g2MVlHOTJDZTROanJCRkMzN0k0S0s2WWh6c2VMVW84VklCRmNBdW5CcmlMYzFXX2RpNmp2UDNPbjNWOFZRMVJUYWtyQkcxX0NPTE1FZU1TXzQ4d2VmaXZkNEVRNTRsQUVPTlUtcXIxRUg5endOZVZyT29sYmtEbmhCQ2pxUA?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQYURlOUxxRUMybEdmbkJoTHZiZEVTTUtCN0gyZ1RsV0s3YlEteXR1NFZIWDNwXzJKTUdCRUpJY0RWNlRqVC02M0VaMFgtY0piUFNGSkhKQmZ3bTVwMHFERHN6ZExPSnVFbWdBWDYxQnNnX0RJRnF6QVlld0FBeDhySGlrUEZ4bEtmWkkybFFVRU9EcnhRd2F5c1M1eGc2OFk5VG95X0dUa1dWUGhPZzJJ?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTE1XUlpyMXlqcVpLcWt5MHZGLWJZd1FXVDlUTDlMTUhrMjVuOGNtMmhDUmFsang0MVN4RmRTR0o3TFk2Zndka1ZkWWp1QzViaEhkbmcxdXpZejRKWEV2enFDb3NZNmNzb3R5STEtclNmZk1DOUxQemZWQQ?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxQOU9NRDc2TDFnalJoMGRGU2lHaWljdGl6ZkR5RGpsT0pGT2xjcElWVWRoNHdneXM3TEc2YWMwcDZKVHcyTlg1MVQ1Z0tSd1FPQnk0Z2s5ZjVuR1pJVXI2OU5tcjRVZ1JOVElTRzBQNkQ1SlJkQ2x4Ny1DWGpGZW1KbENyRDU0SExNZ2hLOHlsOTQyNW82RU5XNWpudEIwRDVJbU5kZlZzTW9zWkZ0dEpJUHkxZkdTbGNxaDFzek01ODJ0T0tRa2hvOUMxWWEtQQ?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTE1nX3FtNWcyRXozTmx1Qzk5ZGhPU2tudFJpZDhFSzBzRnZ1bzNTMVlsNnFjbXdKeDExRWtzQTRLZEdXblZrZE1vV0k4NlByeFcwYm92WnRmRU5rS1BjSmozUG0zb1NULUtoZ1RVM2tMbHNrR3hTSTJJOTRYSVk?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQd0FNLUhKUzQyRThDUEFVbFRuMTFTbS15Zjd0VHRRV2J3alQ4c194UUpCZDlnTXEtRWtNMlFpVVJJaG8xSEVaRC1EbFZ6Q3NlQ0lvbnlEb0h2Q0pvbTRtZjkxMDlqM1ltUjdLcUVlU2ZySkZFYUgxUC1YcE1KUGRibUM2UTNFaXFWWEJzbTZTQWJoVzQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNQkdaemd0bjhYUDFfOUppbkVOMTNZclhORHVIWWx5czZTRjAtM2hXMHBzMmJTeG1JSWJJSVlLOWVrandaa1hFbWYyNmhzVFA2VmRkR1ZOQldJR0NGZ2lfbnlERE5KOWNQdkY3cXI0RUxTNHg5T2tVVE5VM2lVMHZNX1I4ZEZibW44enp2NWREa1lreXVZYTg3Mg?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQakI0aDZPeGllNllmNFZOa19YWU05NXZzeEJ4MHVSeFROVWZMWjNrM2hqNnBWbnR1RUxLUWNLYkRKTFZBMHg4SlBmd00wR1Myd1NpU2lBYURVRUlaUGZfUWxxZ1l3XzBNdnNVek8wc0dVWlZialZURXhraEFrRUUwdS1FQmVHMVB2azhyZmg0RzJCeVQzZC1qRVhER1E4dw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxORXdhTXZuLVo0elFUcHM2WWpSWWdOM1BHTTZUZktFSHViVnl2eS0xbkVSSTF4N19tZ1p5MW1hUkVTTUswdjk5dllMbWVyT0xaU1BHWjlsLVNnLWdWRzlFeTZWQVJVSUt6S3hRWlQ0UWZ4YzFySzFhZDkwcnY3Wk1mSE5idFVVVnV4LURCRDlTeFdLaVpadVBKSkRpUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
