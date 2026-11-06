# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:12:38.442245+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 6, 'ai': 14, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 24 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 8.0%; oldest publication 2026-11-03

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 404.4000 |
| Return 1D (%) | -17.2634 |
| Return 1W (%) | -28.6042 |
| Return 1M (%) | -35.9873 |
| Return YTD (%) | 88.8308 |
| Return 1Y (%) | 57.7654 |
| Annualized volatility (%) | 71.6157 |
| Beta vs SPY | 3.3558 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 0.9970 |
| Downside deviation (rf=0, %) | 47.7937 |
| Sortino (rf=0) | 1.4940 |
| Historical VaR 95% (1D, %) | 6.7006 |
| Historical ES 95% (1D, %) | 9.5329 |
| Correlation vs SPY | 0.6370 |
| Tracking error vs SPY (%) | 63.8231 |
| P/E (trailing) | 104.50 |
| P/B | 9.70 |
| EV/EBITDA | 58.93 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 24.71 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 21.17 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 1.11 |
| MA50 | 547.3664 |
| Close vs MA50 (%) | -26.1190 |
| MA200 | 415.0009 |
| Close vs MA200 (%) | -2.5544 |
| RSI (14, Wilder) | 29.7484 |
| MACD (12,26) | -27.8594 |
| MACD signal (9) | -14.2592 |
| MACD histogram | -13.6001 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 404.4000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -17.2634 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -28.6042 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -35.9873 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 88.8308 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 57.7654 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 71.6157 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 47.7937 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4940 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.7006 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.5329 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6370 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 63.8231 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3558 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9970 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.7096 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 21.1710 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.1093 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 104.4961 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 29.7484 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -13.6001 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -26.1190 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -2.5544 -> Slightly below the moving-average trend level.

## TAILWINDS

### AMD shares rise as AI-driven data-center strength fuels growth outlook
- Summary: AMD shares rise as AI-driven data-center strength fuels growth outlook
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOT1otSGFrSy03TGU4SkFJWHJ0SlJER0pMU0FvV3RIZm1udEtsLTlqazJwbzFEX1lNR3NGYWdNRnRBMDc1ZEk0elNtb2xHcXFFOEFqSnVsWkVRSTBpeHBPUEwtNDZtSUxuZUpKSnM1aXFlX2VUczJlNWRFSXM3MGxmRXAyYkt0dUloMlhaYVJZUVhqNmU2cGVpNkJaMXY3Sm5Qck04ZjNtbHdBSC02Q3hxd3BR?oc=5>

### AMD Stock Pops on $17B Q4 Revenue Guide. Traders Shouldn't Overlook a $3B Inventory Gamble and Collapsing Free Cash Flow.
- Summary: AMD Stock Pops on $17B Q4 Revenue Guide. Traders Shouldn't Overlook a $3B Inventory Gamble and Collapsing Free Cash Flow.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8wFBVV95cUxNRThLTzdDblZFVl9UR0FwWUxGaEJjV3IydzZ2b0JldC1fd0JiMkY2UlNBVUZ5YU01cUdGdnY5eU9TWmhZOElTVU1ocHlISERaRVplVFBvWHBQYk9tcHVOR3pFeVdkU18yX0lITHB2eGFxWXZyUS1hbkVtQmhSMHlRSm5IU3pybG1UZVJUY1FNOXg4RGFwckg1SmM1c0xNZTVwUEd6QzRBOXExMEQ5eUdFemdGVWI5T1BvNlpnS21Ba1VYUGlIcTRJRTlPbHpUV3ZOa0h2RFc5Um5GTUF0N3YzdkwxcXpwZ2ZPSmpxaFZmRmhmWms?oc=5>

### AMD Stock Jumps on Big Earnings Beat
- Summary: AMD Stock Jumps on Big Earnings Beat
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidEFVX3lxTE9mcnlEQzhqWExyWFlMNDhsWkRvc2VrVmtkR2tqUXJzQWZBWGh2UzMySGZqUjhEN3dQcFhEWGpUczZnUHJ3WFB4cEJOUDhIMHlwaGxpRGI4YmlUclBaVkVBWHFoNmhBckFUU1ctUllKaF96bTB6?oc=5>

### AMD: The Bigger Earnings Opportunity Starts In 2027 (NASDAQ:AMD)
- Summary: AMD signals a significant earnings upside beginning in 2027.
- Date: 2026-11-05 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPWHUwRTBPQTlQeENmaTFPbmlhbTRDVEJnNE9FR3A5QXc2VXJaV2dONXI0dmwza3NIcWV5c2ZIdlJLNE9FQ1FoLWNTaEZ4SWlnamZqZjFuRXNMczI5ZGFsYW9ZcEZhZkhNSWd4MEFQRFhVN29CX081VWVuODhLMUxzTnNZR2NWWFpvbzJydHo5WnYxUlg0U2c?oc=5>

### AMD Posts Beat-And-Raise Report On Record AI Data-Center Sales
- Summary: AMD exceeded earnings expectations with record AI data‑center sales, boosting investor confidence.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE1XUlpyMXlqcVpLcWt5MHZGLWJZd1FXVDlUTDlMTUhrMjVuOGNtMmhDUmFsang0MVN4RmRTR0o3TFk2Zndka1ZkWWp1QzViaEhkbmcxdXpZejRKWEV2enFDb3NZNmNzb3R5STEtclNmZk1DOUxQemZWQQ?oc=5>

### New AMD Price Target as Blue Wave Dampens Strong Earnings
- Summary: Analysts adjusted AMD’s price target amid strong earnings, reflecting cautious optimism.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNLUJhYVlqMGc1MWZjUXdGVkhsczFHWXZwcjhvRzVpa3l0cGJsaHJqUTlERUZOb2tqRDBUTm1FNlFSbnVINU9PckoxeDh1M00wUWk0VkQyRTcyNm1NSjVNMlY3YTZNTUhtWWhWWVBIb2VpajJrUjlHVGV3dG5YRkZ2MGhMUGQwbjBRN3dqZlRzLXp6X213dkpwZl9STQ?oc=5>

### Here’s why AMD’s stock is rising — and sending a confident message about the AI trade
- Summary: AMD shares climb, signaling market confidence in its AI strategy.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNN1RkTUttWkc2OFZDbk9uczZTZ3FPcFNCYmg4Q0ZZbjFjZ3luNVR1Yi1Qb0F2RE5ua2RubWtXaFo1UGZkNUdCd2QwUmJkckZiZ1hmT1EycmpuNTAyajlWX2hrLWlqbXFlbkxhcW41Y3V3STdheVJvakhsN3k0RlJSRkZmYXg1blNsMzNvUngtLW5INjNVQ21LOWZrMFlDOV92dG1JVDJDQkY2QTBicmpNWFM5dmNKaTVQTF9KVUVBc080QQ?oc=5>

## HEADWINDS

### Advanced Micro Devices Inc (AMD) Stock Down 17.3% but Still Over
- Summary: Advanced Micro Devices Inc (AMD) Stock Down 17.3% but Still Over
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPTW5ETEI2UEhtLVdUOXhRcFZ3TWtyS21vMWVkY0NoWExTZTMwekxlNXA3WlFIWFk3UkppcU54NjZpYnlaWjJ3MUJjY21FUWNHX0hVSW5TOEU3cmJ0WjJPeVBGdGxUY2Q4UnR4R3pBb093MW9SenFxNk5pYjdWaGJrdjFKNnR5UnByd1RMcUV3Y0ZBTWVwMHN1U05VZEp2cTdqMFpkaVQzVDVMemJFSUpvN2tzdU5ZX3Nkam1IZg?oc=5>

### Advanced Micro Devices (NASDAQ:AMD) Stock Falls 17.3% - Here's What Happened
- Summary: Advanced Micro Devices (NASDAQ:AMD) Stock Falls 17.3% - Here's What Happened
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxPeHdRMzh4VU9UVlBHZVhxZUtVWjNiUWhta3QxTlgtNGVYQVhqdDVKX1dOR0lSRGFoLWd3c09lXzRoZDBoMGZLajJFT1J0bFBJU3RfWTJZeUEzRHdRcWgxdEZUd1RZZlRwOXE0ZnRZajlhTkpVM0NNX2UtWW0yMjZjTGphdHBCXzkxdnFxM3VtNnVQT2tlWWZfZmtfUS15b3ZYREt2NmtJWWkycV90MzIwbTloQlNIRm94NHY5aWljOXVDM0s3Q3lTNQ?oc=5>

### Cathie Wood Just Sold AMD Stock and Bought This AI Chip Stock Instead
- Summary: Cathie Wood sold AMD shares, indicating negative sentiment.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQV0xtQkJITndvRUR4ZjBEYVBib0E0dTFGUzV0OXVHU2FLaThRVHpXX0pVSGlETUlNd1lDNzNLSFUxekdEeHFrRHNIUC1VR0syMEh4SWRBWGpLdm1pVG5CazdiYzViemVFMEs0WUlhZUxmSllNbDJvOURxSGQ2azFOZmFEajRCRnpFdXpxWFV4dF9taFd2LXZaTg?oc=5>

### From Micron to AMD, AI Stocks Crater — And Citi Just Flagged an 'Exponential' New Threat to Data Centers
- Summary: AI stocks, including AMD, are falling amid new data center threat.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi5wFBVV95cUxQRkV2Q0JEVWZCanEzeGZEVUlScFB2eVl5Qjk3anBUSWRGZ0RCYjNfdC1iU0t3OVNsbk84WXByVWRPcmx0ZXFFdE1udGNEVGZXS1RfUlBZU0xDX2dOU2VDVUVsaHRsWTd2aHRXTWtHYzRTckVxSUFzM2V1b3VHUEItRld4aFpldUQ4ZDN0bnhjTjVzeHFIOXhQRTM0NUFpRmJiYmd2QVRsVFBKNVQ1c1Z5Q2tQcGxIQUkwU1M0SGlnV1ZYVXVRVWswb2ZLMktNa25BU0EtYnFGNk92TXRDRnhLQnhpeVFUeFU?oc=5>

### AMD Tumbles 13%, NVIDIA Slides 7% as AI Regulation Fears Hit Chip Stocks; Intel Sinks 8%
- Summary: AMD shares fell 13% due to AI regulation fears.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQZXpOcVdYWWIyd0ZyaldnY3QxMFJUUk14d3E0UmpWVzRwakhSOF9lOUE1azgtTmxRMm55V1JWZ24wZmhsNlVjWHBtZW1DNTJLMmFRNjd1YS0yaFJ1cUxQQVhkdU14V0Mzb1VjbFBreGpFS3FjYUdnXzd1NkVYUUlEY05uYWVJVEgxaGMzbDhzMU5rZWpmNkxqcjdBT0lLMy1kWVlhN1lhbjB2TDFEOGQ4SEJ3YXAxUnpuMi1kMy1RdkZzZVFicVE?oc=5>

### AMD Sinks 13%, Bloom Energy Down 18% as Midterm “Seismic Shift” Deepens Chip Sell-Off
- Summary: AMD shares fell 13% amid a broader chip sell‑off driven by a midterm seismic shift.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPcGhqckJxRHZncHRjelVMN0tkNUptaDQ2T3FHYnF2c3l4RGtJbmhoWGFwMFVpWldWYVMtSERhbU1aSGpQMDRUR1hUZGdER2hXX3VmTmZzekRqMENRRWp0ZEMzZEVTX19qbHFOQ29SV1BSd3MxTGwtWTFzT3QwUGR4U1ZYZE1oZWRuM1c2aWVzTkIyYVdlc1RkQ0FOSFVjaVlwdGJOWEFMejNXOE0?oc=5>

## CATALYSTS

### AMD's data center revenue nearly doubles in Q3 and CEO Su expects growth to accelerate
- Summary: AMD's data center revenue nearly doubles in Q3 and CEO Su expects growth to accelerate
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTFBfVXVMaFFzOXpSSmhDS2xlZWZLZDk0V2w5MHpTSnZ3d2c5bkMzRDhwbzhURWpMMVcwX3ZiME8ybmU4UHR1ekdtVlUwRTYxcTI0T1dadVhheUQ0LVVpWnRqYjdmeDkxMGJKQXBkNUtpaEVKZVlXNEhYRdIBfkFVX3lxTFAwT0pLTUtFX3FhLU4tWFFuU3JjMXF4NWxpWFNVZEoxeTdqMVc2d201ZHRMdXV4cEg4VGNnd0RDRmhKbnNYZndMa1hhMzZ3Y0lUdk82SUprYVVibVZQT19vR05WaGZKZlBzcDFLZWNzczZkb0pDN180UTZ5MTRuUQ?oc=5>

### AMD Beats Wall Street Expectations as It Pivots to Data-Center First Status
- Summary: AMD exceeded earnings expectations by shifting focus to data‑center products.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQTS1ackJyUFczU0ZLRnVmUkF2M2M2MUtueVFjd3ZpOEVkSlJQRWY3eUFNa2g2MVlHOTJDZTROanJCRkMzN0k0S0s2WWh6c2VMVW84VklCRmNBdW5CcmlMYzFXX2RpNmp2UDNPbjNWOFZRMVJUYWtyQkcxX0NPTE1FZU1TXzQ4d2VmaXZkNEVRNTRsQUVPTlUtcXIxRUg5endOZVZyT29sYmtEbmhCQ2pxUA?oc=5>

### AMD Forecast Exceeds Estimates After AI Chip Demand Soars
- Summary: AMD's forecast surpassed estimates amid rising AI chip demand.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQYURlOUxxRUMybEdmbkJoTHZiZEVTTUtCN0gyZ1RsV0s3YlEteXR1NFZIWDNwXzJKTUdCRUpJY0RWNlRqVC02M0VaMFgtY0piUFNGSkhKQmZ3bTVwMHFERHN6ZExPSnVFbWdBWDYxQnNnX0RJRnF6QVlld0FBeDhySGlrUEZ4bEtmWkkybFFVRU9EcnhRd2F5c1M1eGc2OFk5VG95X0dUa1dWUGhPZzJJ?oc=5>

### Here’s How Much Traders Expect AMD Stock to Move After Earnings
- Summary: Traders forecast AMD stock movement post-earnings.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOUzk2TFExUnNScHk1cVdXaHlHMGUxWGhoQVlIWDY3MnE3NnctbVhnYUtERlZFTEw1bjFuVmo5TkRVZC11WWhncHFWb3IybUF3ZjYyWU1kRmlYWTVoOENVaVNHVmY3aVhNZU00VFJfX0VHem1ZRU1mYURPMUxBQVVzZkxKQnVZdW5PR2FoMm1PZnZCeDlTUDQwTTJR?oc=5>

### Advanced Micro Devices (NASDAQ:AMD) Q3 2026 Earnings: Data Center Nearly Doubles and Guidance Tops Consensus
- Summary: Q3 earnings show data center revenue nearly doubled; guidance exceeds consensus expectations.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.97
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxNV0swN190MXdjV0QxZWoxR3I2ZTJMVXJCNVFNWk56UDBRVlFRaDZ6YnV6blEyd2RXb2NJRTNpSWd2Q2tqX3VSSU8yT0tlX3kyZ3NQYlVIVjBITEVmQ3NfbThNdlg2cHdqVnFTbDc1WDBjclZvNDc1MXZvd2dqdXVsNHhrYjc3MGtpaURFa3Q0QldlTHBvcWZqSC1ER29jRnd5RzFpeGoxZ1ZXRmplbl9mSl9xbDZkQ1hWWWI1NUNVeHBneDBqVFQxUmNUVzZYeUZ1N3kySWNVdlBoZFJHTThrZW5xSmhGd1ZZelNv?oc=5>

### AMD Earnings: Strong Data Center Outlook Points to Upside for Stock
- Summary: AMD reports strong Q3 earnings with positive data center outlook, suggesting upside potential.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOaEkyb2htSzVuS3VET3VLa1NHd0dYOThyQ19XdU5yQm43VzZOS1VnMHctbjhLZWlPZTQ1dFktWk1zX0NYWnJzenJXVGpDcGFUanR4ZUR5Rnd1VENMMGRnRTd0SVBKTDVTQ0g4SE5ubDVpWmFPOHhDZEZ5RFV1aFdkQmtFUGF0SGdTX2YyYnlsMHlHZWNLMXY1YVJB?oc=5>

### AMD: Great Q3 Earnings, But 70% Downside Is Not Unrealistic (NASDAQ:AMD)
- Summary: AMD posts solid Q3 earnings but warns of significant downside risk, tempering upside expectations.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQNWl1ZUdmNk5CdDA0RWxldDBCbE1mTFY1NUQ0YklGWE1zY3h2SE4td2piY2lSTjJJZm4yMkxQMXVCX1BMRlFMdW9XdHRNSk43ZmtJdnFlX2hxVDhteXdoNVZNS0lkeEV0ZHo0cVlGMVRZejNXUkNtcHFla1RtaHNTbHNtX291eGJ0Q0EzaG1oZXJScWNsUnFUcTFGRXptbVpfd0pzLUVYVHY?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **104.50** | **9.70** | **58.93** | **44.70** | **663,251,320,832.00 USD** | **57.77** |
| NVDA | 22.96 | 19.15 | 21.63 | 105.90 | 4,385,095,286,784.00 USD | -6.75 |
| INTC | N/A | 2.41 | 15.18 | 20.90 | 277,708,734,464.00 USD | 36.14 |
| AVGO | 41.59 | 13.96 | 27.31 | 85.50 | 1,391,656,304,640.00 USD | -18.19 |

Peers fetched as_of: 2026-11-05; AMD reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,428,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMisgFBVV95cUxOT1otSGFrSy03TGU4SkFJWHJ0SlJER0pMU0FvV3RIZm1udEtsLTlqazJwbzFEX1lNR3NGYWdNRnRBMDc1ZEk0elNtb2xHcXFFOEFqSnVsWkVRSTBpeHBPUEwtNDZtSUxuZUpKSnM1aXFlX2VUczJlNWRFSXM3MGxmRXAyYkt0dUloMlhaYVJZUVhqNmU2cGVpNkJaMXY3Sm5Qck04ZjNtbHdBSC02Q3hxd3BR?oc=5
- https://news.google.com/rss/articles/CBMi8wFBVV95cUxNRThLTzdDblZFVl9UR0FwWUxGaEJjV3IydzZ2b0JldC1fd0JiMkY2UlNBVUZ5YU01cUdGdnY5eU9TWmhZOElTVU1ocHlISERaRVplVFBvWHBQYk9tcHVOR3pFeVdkU18yX0lITHB2eGFxWXZyUS1hbkVtQmhSMHlRSm5IU3pybG1UZVJUY1FNOXg4RGFwckg1SmM1c0xNZTVwUEd6QzRBOXExMEQ5eUdFemdGVWI5T1BvNlpnS21Ba1VYUGlIcTRJRTlPbHpUV3ZOa0h2RFc5Um5GTUF0N3YzdkwxcXpwZ2ZPSmpxaFZmRmhmWms?oc=5
- https://news.google.com/rss/articles/CBMidEFVX3lxTE9mcnlEQzhqWExyWFlMNDhsWkRvc2VrVmtkR2tqUXJzQWZBWGh2UzMySGZqUjhEN3dQcFhEWGpUczZnUHJ3WFB4cEJOUDhIMHlwaGxpRGI4YmlUclBaVkVBWHFoNmhBckFUU1ctUllKaF96bTB6?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPWHUwRTBPQTlQeENmaTFPbmlhbTRDVEJnNE9FR3A5QXc2VXJaV2dONXI0dmwza3NIcWV5c2ZIdlJLNE9FQ1FoLWNTaEZ4SWlnamZqZjFuRXNMczI5ZGFsYW9ZcEZhZkhNSWd4MEFQRFhVN29CX081VWVuODhLMUxzTnNZR2NWWFpvbzJydHo5WnYxUlg0U2c?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTE1XUlpyMXlqcVpLcWt5MHZGLWJZd1FXVDlUTDlMTUhrMjVuOGNtMmhDUmFsang0MVN4RmRTR0o3TFk2Zndka1ZkWWp1QzViaEhkbmcxdXpZejRKWEV2enFDb3NZNmNzb3R5STEtclNmZk1DOUxQemZWQQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNLUJhYVlqMGc1MWZjUXdGVkhsczFHWXZwcjhvRzVpa3l0cGJsaHJqUTlERUZOb2tqRDBUTm1FNlFSbnVINU9PckoxeDh1M00wUWk0VkQyRTcyNm1NSjVNMlY3YTZNTUhtWWhWWVBIb2VpajJrUjlHVGV3dG5YRkZ2MGhMUGQwbjBRN3dqZlRzLXp6X213dkpwZl9STQ?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNN1RkTUttWkc2OFZDbk9uczZTZ3FPcFNCYmg4Q0ZZbjFjZ3luNVR1Yi1Qb0F2RE5ua2RubWtXaFo1UGZkNUdCd2QwUmJkckZiZ1hmT1EycmpuNTAyajlWX2hrLWlqbXFlbkxhcW41Y3V3STdheVJvakhsN3k0RlJSRkZmYXg1blNsMzNvUngtLW5INjNVQ21LOWZrMFlDOV92dG1JVDJDQkY2QTBicmpNWFM5dmNKaTVQTF9KVUVBc080QQ?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPTW5ETEI2UEhtLVdUOXhRcFZ3TWtyS21vMWVkY0NoWExTZTMwekxlNXA3WlFIWFk3UkppcU54NjZpYnlaWjJ3MUJjY21FUWNHX0hVSW5TOEU3cmJ0WjJPeVBGdGxUY2Q4UnR4R3pBb093MW9SenFxNk5pYjdWaGJrdjFKNnR5UnByd1RMcUV3Y0ZBTWVwMHN1U05VZEp2cTdqMFpkaVQzVDVMemJFSUpvN2tzdU5ZX3Nkam1IZg?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxPeHdRMzh4VU9UVlBHZVhxZUtVWjNiUWhta3QxTlgtNGVYQVhqdDVKX1dOR0lSRGFoLWd3c09lXzRoZDBoMGZLajJFT1J0bFBJU3RfWTJZeUEzRHdRcWgxdEZUd1RZZlRwOXE0ZnRZajlhTkpVM0NNX2UtWW0yMjZjTGphdHBCXzkxdnFxM3VtNnVQT2tlWWZfZmtfUS15b3ZYREt2NmtJWWkycV90MzIwbTloQlNIRm94NHY5aWljOXVDM0s3Q3lTNQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQV0xtQkJITndvRUR4ZjBEYVBib0E0dTFGUzV0OXVHU2FLaThRVHpXX0pVSGlETUlNd1lDNzNLSFUxekdEeHFrRHNIUC1VR0syMEh4SWRBWGpLdm1pVG5CazdiYzViemVFMEs0WUlhZUxmSllNbDJvOURxSGQ2azFOZmFEajRCRnpFdXpxWFV4dF9taFd2LXZaTg?oc=5
- https://news.google.com/rss/articles/CBMi5wFBVV95cUxQRkV2Q0JEVWZCanEzeGZEVUlScFB2eVl5Qjk3anBUSWRGZ0RCYjNfdC1iU0t3OVNsbk84WXByVWRPcmx0ZXFFdE1udGNEVGZXS1RfUlBZU0xDX2dOU2VDVUVsaHRsWTd2aHRXTWtHYzRTckVxSUFzM2V1b3VHUEItRld4aFpldUQ4ZDN0bnhjTjVzeHFIOXhQRTM0NUFpRmJiYmd2QVRsVFBKNVQ1c1Z5Q2tQcGxIQUkwU1M0SGlnV1ZYVXVRVWswb2ZLMktNa25BU0EtYnFGNk92TXRDRnhLQnhpeVFUeFU?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQZXpOcVdYWWIyd0ZyaldnY3QxMFJUUk14d3E0UmpWVzRwakhSOF9lOUE1azgtTmxRMm55V1JWZ24wZmhsNlVjWHBtZW1DNTJLMmFRNjd1YS0yaFJ1cUxQQVhkdU14V0Mzb1VjbFBreGpFS3FjYUdnXzd1NkVYUUlEY05uYWVJVEgxaGMzbDhzMU5rZWpmNkxqcjdBT0lLMy1kWVlhN1lhbjB2TDFEOGQ4SEJ3YXAxUnpuMi1kMy1RdkZzZVFicVE?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPcGhqckJxRHZncHRjelVMN0tkNUptaDQ2T3FHYnF2c3l4RGtJbmhoWGFwMFVpWldWYVMtSERhbU1aSGpQMDRUR1hUZGdER2hXX3VmTmZzekRqMENRRWp0ZEMzZEVTX19qbHFOQ29SV1BSd3MxTGwtWTFzT3QwUGR4U1ZYZE1oZWRuM1c2aWVzTkIyYVdlc1RkQ0FOSFVjaVlwdGJOWEFMejNXOE0?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTFBfVXVMaFFzOXpSSmhDS2xlZWZLZDk0V2w5MHpTSnZ3d2c5bkMzRDhwbzhURWpMMVcwX3ZiME8ybmU4UHR1ekdtVlUwRTYxcTI0T1dadVhheUQ0LVVpWnRqYjdmeDkxMGJKQXBkNUtpaEVKZVlXNEhYRdIBfkFVX3lxTFAwT0pLTUtFX3FhLU4tWFFuU3JjMXF4NWxpWFNVZEoxeTdqMVc2d201ZHRMdXV4cEg4VGNnd0RDRmhKbnNYZndMa1hhMzZ3Y0lUdk82SUprYVVibVZQT19vR05WaGZKZlBzcDFLZWNzczZkb0pDN180UTZ5MTRuUQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQTS1ackJyUFczU0ZLRnVmUkF2M2M2MUtueVFjd3ZpOEVkSlJQRWY3eUFNa2g2MVlHOTJDZTROanJCRkMzN0k0S0s2WWh6c2VMVW84VklCRmNBdW5CcmlMYzFXX2RpNmp2UDNPbjNWOFZRMVJUYWtyQkcxX0NPTE1FZU1TXzQ4d2VmaXZkNEVRNTRsQUVPTlUtcXIxRUg5endOZVZyT29sYmtEbmhCQ2pxUA?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQYURlOUxxRUMybEdmbkJoTHZiZEVTTUtCN0gyZ1RsV0s3YlEteXR1NFZIWDNwXzJKTUdCRUpJY0RWNlRqVC02M0VaMFgtY0piUFNGSkhKQmZ3bTVwMHFERHN6ZExPSnVFbWdBWDYxQnNnX0RJRnF6QVlld0FBeDhySGlrUEZ4bEtmWkkybFFVRU9EcnhRd2F5c1M1eGc2OFk5VG95X0dUa1dWUGhPZzJJ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOUzk2TFExUnNScHk1cVdXaHlHMGUxWGhoQVlIWDY3MnE3NnctbVhnYUtERlZFTEw1bjFuVmo5TkRVZC11WWhncHFWb3IybUF3ZjYyWU1kRmlYWTVoOENVaVNHVmY3aVhNZU00VFJfX0VHem1ZRU1mYURPMUxBQVVzZkxKQnVZdW5PR2FoMm1PZnZCeDlTUDQwTTJR?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxNV0swN190MXdjV0QxZWoxR3I2ZTJMVXJCNVFNWk56UDBRVlFRaDZ6YnV6blEyd2RXb2NJRTNpSWd2Q2tqX3VSSU8yT0tlX3kyZ3NQYlVIVjBITEVmQ3NfbThNdlg2cHdqVnFTbDc1WDBjclZvNDc1MXZvd2dqdXVsNHhrYjc3MGtpaURFa3Q0QldlTHBvcWZqSC1ER29jRnd5RzFpeGoxZ1ZXRmplbl9mSl9xbDZkQ1hWWWI1NUNVeHBneDBqVFQxUmNUVzZYeUZ1N3kySWNVdlBoZFJHTThrZW5xSmhGd1ZZelNv?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOaEkyb2htSzVuS3VET3VLa1NHd0dYOThyQ19XdU5yQm43VzZOS1VnMHctbjhLZWlPZTQ1dFktWk1zX0NYWnJzenJXVGpDcGFUanR4ZUR5Rnd1VENMMGRnRTd0SVBKTDVTQ0g4SE5ubDVpWmFPOHhDZEZ5RFV1aFdkQmtFUGF0SGdTX2YyYnlsMHlHZWNLMXY1YVJB?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQNWl1ZUdmNk5CdDA0RWxldDBCbE1mTFY1NUQ0YklGWE1zY3h2SE4td2piY2lSTjJJZm4yMkxQMXVCX1BMRlFMdW9XdHRNSk43ZmtJdnFlX2hxVDhteXdoNVZNS0lkeEV0ZHo0cVlGMVRZejNXUkNtcHFla1RtaHNTbHNtX291eGJ0Q0EzaG1oZXJScWNsUnFUcTFGRXptbVpfd0pzLUVYVHY?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
