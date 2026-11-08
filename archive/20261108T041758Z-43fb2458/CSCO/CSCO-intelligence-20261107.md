# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-11-07**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-07**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-08T04:21:43.102913+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 7, 'ai': 13, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261107T043155Z-acc5f41d/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 10 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 36.0%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 93.8500 |
| Return 1D (%) | -1.9536 |
| Return 1W (%) | -10.2000 |
| Return 1M (%) | -20.4256 |
| Return YTD (%) | 24.0912 |
| Return 1Y (%) | 34.5544 |
| Annualized volatility (%) | 36.4931 |
| Beta vs SPY | 1.2064 |
| Max drawdown (%) | -27.2567 |
| Sharpe (rf=0) | 0.9996 |
| Downside deviation (rf=0, %) | 25.4283 |
| Sortino (rf=0) | 1.4345 |
| Historical VaR 95% (1D, %) | 3.0714 |
| Historical ES 95% (1D, %) | 5.3408 |
| Correlation vs SPY | 0.4479 |
| Tracking error vs SPY (%) | 32.7470 |
| P/E (trailing) | 28.18 |
| P/B | 7.36 |
| EV/EBITDA | 20.67 |
| Revenue growth (%) | 17.60 |
| Forward P/E (estimate) | 16.69 |
| Gross margin (%) | 64.52 |
| Operating margin (%) | 27.72 |
| Return on equity (%) | 27.32 |
| Free cash flow yield (%) | 3.02 |
| MA50 | 108.6151 |
| Close vs MA50 (%) | -13.5940 |
| MA200 | 101.1786 |
| Close vs MA200 (%) | -7.2432 |
| RSI (14, Wilder) | 28.4879 |
| MACD (12,26) | -3.1892 |
| MACD signal (9) | -1.7217 |
| MACD histogram | -1.4675 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 93.8500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.9536 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -10.2000 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -20.4256 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 24.0912 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 34.5544 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.4931 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.4283 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4345 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0714 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.3408 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4479 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.7470 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2064 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.2567 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9996 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.6933 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.5240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.7190 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.3190 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.0222 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 28.1832 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 28.4879 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.4675 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -13.5940 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -7.2432 -> Clearly below the moving-average trend level.

## TAILWINDS

### What Could Lift Cisco Stock?
- Summary: Speculation on factors that could boost Cisco's stock.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNd2JhNnJ3MTU4TTV4XzZWdUZVSFdZZWJGTW8xNXlZTGdYWEY5VG9jVmx2NTV5blFTUkU0R0gyMS1SLW9Dd095djJSWXVTQ0xCYURmR2R2c2JpLVhZZEQ3S09RamFPem5PbVVBVzdzNHZULWFJazB3Y0lQeXJnMS0yVGRKY05oUUpGNnBEZi01b3plUQ?oc=5>

### Cisco Systems Stock Outlook: Is Wall Street Bullish or Bearish?
- Summary: Questioning market sentiment toward Cisco's future performance.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNNmxUZjJVSDRsTWZrakJ0REVoVTJocTBrYlRaemh4MkV4Sk1DY0hETHFKYmJsNmxrd2VrZnJ2R1JEczV1VHVHaDhoNHM0Vl9feXY1UkFhWm9Qa01ySHVGaEhlWlUzY3ZzRmprcVRCZXFTd3k4V1RtbUE0SHJxUVBULUF6OGIydDBUZHBra2xZT2hfWTd0dGlRZ29pdUZJQQ?oc=5>

### Asset One Wealth Management LLC Purchases 12,867 Shares of Cisco Systems, Inc. $CSCO
- Summary: Asset One Wealth Management LLC bought 12,867 shares of Cisco, indicating investor confidence.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxPSW94Xzd0OHctOTBxak10RzJVQV9mYWExSnhaQTkwZzdmSkRsbkVxZVdnci16MGlTZV93c3paZEh5SExjYXFxc0hOWTJIUC0wRS0yNzNqVkhkd3FNeXFKTDdsajBaOVZDY2VieC1SUmZlRGRDREhCNlNOWmZQNS1rWUNSLW9zekpEZ0ZQVTRRRDBONlRobndQbzhoRWZvZ0pvb3BOWGtFTkluV3JUbktkSlk3YTJ1bmFDZXBDY3VqaWRTYUIybUVjTkZ5VlpQZER5UGtIdEFWRXI?oc=5>

## HEADWINDS

### Cisco Stock (CSCO) Falls as Morgan Stanley Downgrades to ‘Hold’ Ahead of Q1 Earnings
- Summary: Cisco Stock (CSCO) Falls as Morgan Stanley Downgrades to ‘Hold’ Ahead of Q1 Earnings
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPLUxadF80a3hWNmZTTDBSZ1dZZmFvOEFyMERMUmRXYkhrVjBsTWJUU0RtWkRkOHE3Nm56MEdoRDN0RFctSEU1clp1RU5QS1FjSEYwZldIaGo2QkMyLUQ3b2FhZEZsV2ZoTDdxZTE2LVJPWWwzZDh1Y293cHJ2RS13bzZWQzBLNXNmRjlrLVJVUkZlblJFY3RSZ0doeDZwOFVqRGRkVXFsMXQxMWZoVkVj?oc=5>

### Cisco Systems Inc (CSCO) Shares Fall 7.6% -- GF Value Says Still Overvalued
- Summary: Cisco Systems Inc (CSCO) Shares Fall 7.6% -- GF Value Says Still Overvalued
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxQeTVWX0JOTTlWcHgyMHpFMHpMaXdmVVRmQXFJVGhzQkZBNTdvYVRPcGlpTGZfX3JKS0EwN19SZUxWekVPYklsT1o5clhOdkt3NTdXSkFLSS1JRHM3SmJJNjdGX2lTbUxGbGlvSFRHWEJ5QUU5LTBIbjZXSllhMkEyb2N6SGp5MlpGNW1DcGhFampFQzRXMnBDNmhQREg3ck5ZSklfRlhiaHg2R2M?oc=5>

### Cisco Systems (NASDAQ:CSCO) Stock Price Down 2.8% - Here's What Happened
- Summary: Cisco Systems (NASDAQ:CSCO) Stock Price Down 2.8% - Here's What Happened
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPNm1MTERFbkduR2VwaFBIdENsVFNDMkgteGVmV2xHSEd6c1djRTZyYzBTRFNQY2dJZmwxN0xIOE1GbEwxRThjMXpyV2NUeFY3Z2dRZEVYZE1aUU9jcGtha0hZYWtzbTloNE5jYTRrQXE1NUUySUxNbmswTk5aUl9VZk1rRWhubDFRNHZnb0MyT0JFeElLVjc4Vi1zRDVwb0MzT1NJQ1BmaGJSQlJGU1pBZDhzTlZGb0E5OTBvT2t5dnBfQTQ?oc=5>

### Cisco Systems (NASDAQ:CSCO) Shares Break Below 200-Day Moving Average After Analyst Downgrade
- Summary: Cisco Systems (NASDAQ:CSCO) Shares Break Below 200-Day Moving Average After Analyst Downgrade
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxNbi1GN2lCT0dDSHZESzB1OVZtVlVlVWNUWURETTJycUdQbUhrYnlKaHl1c3lQUGd3SEhmT2VvYng3UmhEYlFuV2pReFQwakFWTDlsdHBXdlFVSkdOQjVqS01VcUthZDlFWVh5TEkzcGRHZDJkdnlWYTM3bjQwdkpFZllMSGZwdnNHTVhJR3hDRHVPRWVTdXVnOEVQLUpYR20zMFlVMmRsZmg3VTAxT0xyRGROYzhmSm1pVml1UW8yWTQwZEx2dlZjX0RmMkFNM2hMQWozY0lFMXM2UGVfeGNOdFRFQ1p6Zw?oc=5>

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

### Cisco Systems, Inc. $CSCO Stock: International Assets Investment Management LLC Trims Holdings
- Summary: International Assets trimmed its Cisco holdings, suggesting reduced confidence.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxPeDNPNXRSczdVVzlxV3V0YzBxSE94SEtROFBsSUxKT2NHd1VkQkFXcEVGcUVVNWNFTEhpNFlFbVhaeXJkd0VJWUFpcjVuMUhwUnR5dmFycTFRbXR1QTBpd0t4cXptbWxLMVAxNmM3cTE4QmFsVUd2X1JNd01sZ2R4RmlhdFQzV1F5LTRBdm4tZTdtS0lBTG1tYldoVlpOLXQxV3hvQ25aUFVNcTdYd2wwbm1fb2FkOUJRMkJYVFluLVd6emVSREpmZTVtQ1BfRVBOMTBJRUpkdmFDUmx5QWJTWHNVVzZ5QQ?oc=5>

### Should Margin Pressure Fears Require Action From Cisco Stock Investors?
- Summary: Margin pressure concerns may prompt investor action, indicating potential downside risk.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxPUGx0SkhpZ3ZCc1VJblBVZy1KZFQ4UWVfRGJCZTc1RVBmRzFkT2F3WDl6ZFJidVB3R1d4czZWVUpVRXlBUlZDTU80c1VJZ2Vpb050MjNOY0d1QnVldVh0eDJWSWlLSVU4SE8wOFNoVXBOZEw1MDhWaHVqNl9hVjBEMU9malNHN2tPSDhjWmwtQmVJVkhTeG9mOU5KQjB6NFJXUHVhSGVxRE5uZi1GaklNTG5TeFZ6ZVF0aWQ1cnNzYW8xZmdyb0F30gHMAUFVX3lxTE53Yk5oQWo0aTZWSTdNQ3FFRXkzdDJyM0UxV1RJMEpjVVdkZ2hxcGo0QjE3dHRGbnRSZ25fUGdfYXN4UWkyUHJzVEdDT2tGTndPUXFtZjNRNkJWdHJGMmQ4Nm9wN0hyYUo3QU5hMGJ0LTlpdkhQal9CQXVrM3l5MEVGa3Z0bkJDc1ZjVXJFRmhvcmMzQkx5VnpUcHFOMldUR0Y0MER0NG4zZDhUMzlpZ2V1R1JaRnBUTm5lbGFRQUZYcnhMcjRWWnQyU3RNLQ?oc=5>

## CATALYSTS

### Cisco Systems options suggest 7.9% stock move on earnings
- Summary: Cisco Systems options suggest 7.9% stock move on earnings
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxONW9UVmJFTUktME85TDJORmowbzdRR0Vaa09jMThLN1puVXdyQ3lnZjNKcTRNakhnUUtzMU43bGVxdE0xbDFRMUM5d0JMN2hoVkotWjF3Q3hIMzl0U29YNUpGcWxET09ISnNaMFpMcE9pVElOVTJjTmxoeTdkSlJnS3g1RUlMRUdnX2NLcjRiTk5CWWZfQzBtdFJ2dHBaTV9peEFldDUyYjktR1J1dXUwOGpuTWdzaURf?oc=5>

### Cisco Systems, Inc. $CSCO Stock Sold by Inscription Capital LLC
- Summary: Cisco Systems, Inc. $CSCO Stock Sold by Inscription Capital LLC
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxOZUZLeDhnR1VyTUtOR0pLREp2Zi1hY3JhamE3RER0RGpvelhNVDhyeC1SWnpNbkpCUlJZLWk0UDJWWHRRZHdXS0JZd09aZDZZRWstNTFIZUIwSERJdk1DTDY3NzcydkliWWVLbkx3ZFY2YXJvOFg0U3A1ZThmYnQ4VUo5ZXRjQWVUQTBzWF9qZnNkVVBBa0FyWUVGdk1OQm9HblBJUmFMRjdWWEtFVHlBUktXZE1NR1VFQmxGdjFB?oc=5>

### Cisco Systems, Inc. $CSCO Shares Acquired by Rakuten Investment Management Inc.
- Summary: Cisco Systems, Inc. $CSCO Shares Acquired by Rakuten Investment Management Inc.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQSXpIQjhxZmZobUVKdHU2N1VDQWlaYmxyOWFTczRPdXpheERpTjlrQXRERlkyWHlzME1kVHFIQUJodWE4NXFwdHdBTklkTzJubDNPUUFwWE4tLVNmYXBIVUxCWFdSZHdqZ2RPNkRiLVZvYWpZWFFNODVJNzMtLVp5eU1ZR3hENVdkM2hob3JHYzlVeU1NRU4tSWlqSzdydTRMaGxSWDhUdlpKSWIycHhOdGtJeE9QaV90NF82RnlGYXJYYVFmNktXaXYyQ1lrcmVRUHc?oc=5>

### Morgan Stanley resets Cisco stock price target before earnings
- Summary: Morgan Stanley adjusts Cisco price target ahead of earnings, neutral impact.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPSDdLTmFtNnZ6YWJfQkxDNzNEQndNQTR0NVVlSlU5a1NNQWZaWjB3cl9FVUw4Q3hZeExiUEV4YmZMYjF6YTJTeEN0SDJTNnZHN1huV04tZUprUnF0eXA2MXNzQ0lXVGRuY2lKcGxXM2doRkpqcG1Zb2lxWUFzbExUSHEzbFZmWTM1bFdteDJPbk5qWnhZTUF5NXVVUnB2WkdzblRKNVYyUjdlSVZyak9rcUFucw?oc=5>

### How Investors Are Reacting To Cisco Stock After Analyst Downgrade
- Summary: Investors react negatively to Cisco downgrade, impacting short-term sentiment.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNc3plRmFVemkybDMwNkhvQ3BDSVphWjdfb1VGbng1cTg0akFrVzh1akR4R1FUdVFRZ3RyY2ZPTE9pN2VEMDF5VXB1UDVfNFROZjNPakYxa2F5cWtHeWg5SGNMUll0S042WUpwR2Fra0tRNTl5Qnd5OGZYeXdvNmx3NjNJd3dUS2dDdjVTNkN2QUZkMThFTXJmSDBLeWpFMHlkby1qTWpB?oc=5>

### Cisco Systems, Inc. $CSCO Stock: Alta Advisers Ltd Boosts Position
- Summary: Alta Advisers Ltd raised its holdings in Cisco, reflecting a bullish stance on the firm.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxQTy15RWZEelJOczBlV3FWMUJ4M082d0ZZSE5iblJ1ZGFSbC1oNHQxcHhKa3R3VFJKRlhMN2tTdFZCZy1SamhTLUtYWXZWZVZEOEtsNUw3TGNpM3V3NzRSZ0tCd2o1OWNlN19lUHZWSE9qeTlUYnJnM00xWHhSdG9aWVpXeFhlX3o1U3JTUFhTYzBrNTJhTFNNNmdWVExpTTV2UGFmTEVGQk5rRnRsZk9fMDJnRnBLYWZVeUlyUnROQUw?oc=5>

### Cisco Systems, Inc. $CSCO Stock Position Boosted by Kestra Advisory Services LLC
- Summary: Kestra Advisory Services LLC increased its stake in Cisco, indicating confidence in the company’s prospects.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNLU9NTE9yR1JLdm85WS13U1ZvNjZHTmN0UkxEckZ1YTBUWHJfUmtUOEZpMWtTUjZvTDd1NWtobFlTSnhvWk9pcnRhLWQ4YVc3eWg1VlZHV24tczc4VFdWVnpGN1gySGZNRXJVYjhUaW5SNVdsU081MURUZWxvTENEU19pRGpCaE1LSnJoNUpFSnh2WHRlZ3FKQXJrdmpHSkd5TlhtZGU4VC1RbW4zWkx3UGtzRE9tbDRtWjdhVjR5MkVkTUd0S1VxT1dydkpnOVdsdnBiQQ?oc=5>

### Cisco Systems, Inc. $CSCO Stock Position Boosted by Provenance Wealth Advisors LLC
- Summary: Provenance Wealth Advisors LLC increased its holdings in Cisco, indicating confidence in the company’s prospects.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxNNmdKUExrYVZYSTNzX2dFY3kxQjd3UzlFSEg3aHIzeEtpeWRmTVlzSm1wckhlcVdlX0h5OGdkM2J4dkR4cHh2RENCZ0daUnEwaFdnRGstdUtDTlVyT0ZYUGI1VmNpREtnSnF6dWxaSGlKOU9aNS1OUWZaRG1BMnhVRlhSYnc3QzlodnRIZ1dhUF9lTW5iUXloaFRvMWFuRnZzSnVpN1QzZXQ5ZjU0akIwQXZYblZLNEtHMjJTdnN5YTVkV3B3OUN2QU9jeGVPcGEwcks2SWZQTQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **28.18** | **7.36** | **20.67** | **17.60** | **370,011,766,784.00 USD** | **34.55** |
| ANET | 45.79 | 13.12 | 37.98 | 58.50 | 215,789,125,632.00 USD | 27.44 |
| FFIV | 24.83 | 4.41 | 17.59 | 13.30 | 17,659,131,904.00 USD | 25.29 |
| HPE | 23.08 | 2.24 | 10.68 | 33.70 | 59,430,600,704.00 USD | 94.77 |

Peers fetched as_of: 2026-11-07; CSCO reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-12
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-07

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
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
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxPSW94Xzd0OHctOTBxak10RzJVQV9mYWExSnhaQTkwZzdmSkRsbkVxZVdnci16MGlTZV93c3paZEh5SExjYXFxc0hOWTJIUC0wRS0yNzNqVkhkd3FNeXFKTDdsajBaOVZDY2VieC1SUmZlRGRDREhCNlNOWmZQNS1rWUNSLW9zekpEZ0ZQVTRRRDBONlRobndQbzhoRWZvZ0pvb3BOWGtFTkluV3JUbktkSlk3YTJ1bmFDZXBDY3VqaWRTYUIybUVjTkZ5VlpQZER5UGtIdEFWRXI?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPLUxadF80a3hWNmZTTDBSZ1dZZmFvOEFyMERMUmRXYkhrVjBsTWJUU0RtWkRkOHE3Nm56MEdoRDN0RFctSEU1clp1RU5QS1FjSEYwZldIaGo2QkMyLUQ3b2FhZEZsV2ZoTDdxZTE2LVJPWWwzZDh1Y293cHJ2RS13bzZWQzBLNXNmRjlrLVJVUkZlblJFY3RSZ0doeDZwOFVqRGRkVXFsMXQxMWZoVkVj?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxQeTVWX0JOTTlWcHgyMHpFMHpMaXdmVVRmQXFJVGhzQkZBNTdvYVRPcGlpTGZfX3JKS0EwN19SZUxWekVPYklsT1o5clhOdkt3NTdXSkFLSS1JRHM3SmJJNjdGX2lTbUxGbGlvSFRHWEJ5QUU5LTBIbjZXSllhMkEyb2N6SGp5MlpGNW1DcGhFampFQzRXMnBDNmhQREg3ck5ZSklfRlhiaHg2R2M?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPNm1MTERFbkduR2VwaFBIdENsVFNDMkgteGVmV2xHSEd6c1djRTZyYzBTRFNQY2dJZmwxN0xIOE1GbEwxRThjMXpyV2NUeFY3Z2dRZEVYZE1aUU9jcGtha0hZYWtzbTloNE5jYTRrQXE1NUUySUxNbmswTk5aUl9VZk1rRWhubDFRNHZnb0MyT0JFeElLVjc4Vi1zRDVwb0MzT1NJQ1BmaGJSQlJGU1pBZDhzTlZGb0E5OTBvT2t5dnBfQTQ?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxNbi1GN2lCT0dDSHZESzB1OVZtVlVlVWNUWURETTJycUdQbUhrYnlKaHl1c3lQUGd3SEhmT2VvYng3UmhEYlFuV2pReFQwakFWTDlsdHBXdlFVSkdOQjVqS01VcUthZDlFWVh5TEkzcGRHZDJkdnlWYTM3bjQwdkpFZllMSGZwdnNHTVhJR3hDRHVPRWVTdXVnOEVQLUpYR20zMFlVMmRsZmg3VTAxT0xyRGROYzhmSm1pVml1UW8yWTQwZEx2dlZjX0RmMkFNM2hMQWozY0lFMXM2UGVfeGNOdFRFQ1p6Zw?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxNenlRbU9KcTNickNGZy1DQ1dLTGlwb2FtaEhBZzlyRjBORUlwOWwxUEpCaG9Fbm10TGF5ZFk4RmNqQkZtQWYtbEFXR2FYUXlkNFVlaVpoOWpQVm1IempVdUVhb3ZLMjNkaE9OVEJjQlVsWnE3WnFLdEx6bDhjRlh4amY0YW5zWGs5YnJyLVhR?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNdDFQV1p3VlpQeHIxMWNXc2tlZE5YUnQ3cHQ1emtpY2xmLTl2enBwaThKT0JBaE1GZTV2UC05X3d0UG9oR0FONXZqWTZnRzNwYUNORE5VT0lXcVJOOXpnUTJLeWhYUXBKeWNTVERlZlpBNUtFUC11MkdHcUhZcmtwZVJpVXI5Z1dIS1Vj?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOQlpCYXRLYUtjVDRXWWRYa2dqVFRIN0Z3a3M5bHFtOTZLekYwZGpoWHdjZC03RzJNanVEcHF6eTZDLWhURmp4dWdyRVg4aHpDZ1BpamllLXZYb2NlcUVVbEllOTRFeld3SWdtRW1QRlBIdU0wZkpvb0xYaElSbV9laUd0MmtxMWhJV0l0aWVJZ1J6THFWX2tyZEUta0xyQkZmdi1nNjliMlpKdnVwVnBXNU9aUzVreEZLd0Jud0lvbnZ6dC1N?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxPeDNPNXRSczdVVzlxV3V0YzBxSE94SEtROFBsSUxKT2NHd1VkQkFXcEVGcUVVNWNFTEhpNFlFbVhaeXJkd0VJWUFpcjVuMUhwUnR5dmFycTFRbXR1QTBpd0t4cXptbWxLMVAxNmM3cTE4QmFsVUd2X1JNd01sZ2R4RmlhdFQzV1F5LTRBdm4tZTdtS0lBTG1tYldoVlpOLXQxV3hvQ25aUFVNcTdYd2wwbm1fb2FkOUJRMkJYVFluLVd6emVSREpmZTVtQ1BfRVBOMTBJRUpkdmFDUmx5QWJTWHNVVzZ5QQ?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPUGx0SkhpZ3ZCc1VJblBVZy1KZFQ4UWVfRGJCZTc1RVBmRzFkT2F3WDl6ZFJidVB3R1d4czZWVUpVRXlBUlZDTU80c1VJZ2Vpb050MjNOY0d1QnVldVh0eDJWSWlLSVU4SE8wOFNoVXBOZEw1MDhWaHVqNl9hVjBEMU9malNHN2tPSDhjWmwtQmVJVkhTeG9mOU5KQjB6NFJXUHVhSGVxRE5uZi1GaklNTG5TeFZ6ZVF0aWQ1cnNzYW8xZmdyb0F30gHMAUFVX3lxTE53Yk5oQWo0aTZWSTdNQ3FFRXkzdDJyM0UxV1RJMEpjVVdkZ2hxcGo0QjE3dHRGbnRSZ25fUGdfYXN4UWkyUHJzVEdDT2tGTndPUXFtZjNRNkJWdHJGMmQ4Nm9wN0hyYUo3QU5hMGJ0LTlpdkhQal9CQXVrM3l5MEVGa3Z0bkJDc1ZjVXJFRmhvcmMzQkx5VnpUcHFOMldUR0Y0MER0NG4zZDhUMzlpZ2V1R1JaRnBUTm5lbGFRQUZYcnhMcjRWWnQyU3RNLQ?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxONW9UVmJFTUktME85TDJORmowbzdRR0Vaa09jMThLN1puVXdyQ3lnZjNKcTRNakhnUUtzMU43bGVxdE0xbDFRMUM5d0JMN2hoVkotWjF3Q3hIMzl0U29YNUpGcWxET09ISnNaMFpMcE9pVElOVTJjTmxoeTdkSlJnS3g1RUlMRUdnX2NLcjRiTk5CWWZfQzBtdFJ2dHBaTV9peEFldDUyYjktR1J1dXUwOGpuTWdzaURf?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxOZUZLeDhnR1VyTUtOR0pLREp2Zi1hY3JhamE3RER0RGpvelhNVDhyeC1SWnpNbkpCUlJZLWk0UDJWWHRRZHdXS0JZd09aZDZZRWstNTFIZUIwSERJdk1DTDY3NzcydkliWWVLbkx3ZFY2YXJvOFg0U3A1ZThmYnQ4VUo5ZXRjQWVUQTBzWF9qZnNkVVBBa0FyWUVGdk1OQm9HblBJUmFMRjdWWEtFVHlBUktXZE1NR1VFQmxGdjFB?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQSXpIQjhxZmZobUVKdHU2N1VDQWlaYmxyOWFTczRPdXpheERpTjlrQXRERlkyWHlzME1kVHFIQUJodWE4NXFwdHdBTklkTzJubDNPUUFwWE4tLVNmYXBIVUxCWFdSZHdqZ2RPNkRiLVZvYWpZWFFNODVJNzMtLVp5eU1ZR3hENVdkM2hob3JHYzlVeU1NRU4tSWlqSzdydTRMaGxSWDhUdlpKSWIycHhOdGtJeE9QaV90NF82RnlGYXJYYVFmNktXaXYyQ1lrcmVRUHc?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPSDdLTmFtNnZ6YWJfQkxDNzNEQndNQTR0NVVlSlU5a1NNQWZaWjB3cl9FVUw4Q3hZeExiUEV4YmZMYjF6YTJTeEN0SDJTNnZHN1huV04tZUprUnF0eXA2MXNzQ0lXVGRuY2lKcGxXM2doRkpqcG1Zb2lxWUFzbExUSHEzbFZmWTM1bFdteDJPbk5qWnhZTUF5NXVVUnB2WkdzblRKNVYyUjdlSVZyak9rcUFucw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNc3plRmFVemkybDMwNkhvQ3BDSVphWjdfb1VGbng1cTg0akFrVzh1akR4R1FUdVFRZ3RyY2ZPTE9pN2VEMDF5VXB1UDVfNFROZjNPakYxa2F5cWtHeWg5SGNMUll0S042WUpwR2Fra0tRNTl5Qnd5OGZYeXdvNmx3NjNJd3dUS2dDdjVTNkN2QUZkMThFTXJmSDBLeWpFMHlkby1qTWpB?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxQTy15RWZEelJOczBlV3FWMUJ4M082d0ZZSE5iblJ1ZGFSbC1oNHQxcHhKa3R3VFJKRlhMN2tTdFZCZy1SamhTLUtYWXZWZVZEOEtsNUw3TGNpM3V3NzRSZ0tCd2o1OWNlN19lUHZWSE9qeTlUYnJnM00xWHhSdG9aWVpXeFhlX3o1U3JTUFhTYzBrNTJhTFNNNmdWVExpTTV2UGFmTEVGQk5rRnRsZk9fMDJnRnBLYWZVeUlyUnROQUw?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNLU9NTE9yR1JLdm85WS13U1ZvNjZHTmN0UkxEckZ1YTBUWHJfUmtUOEZpMWtTUjZvTDd1NWtobFlTSnhvWk9pcnRhLWQ4YVc3eWg1VlZHV24tczc4VFdWVnpGN1gySGZNRXJVYjhUaW5SNVdsU081MURUZWxvTENEU19pRGpCaE1LSnJoNUpFSnh2WHRlZ3FKQXJrdmpHSkd5TlhtZGU4VC1RbW4zWkx3UGtzRE9tbDRtWjdhVjR5MkVkTUd0S1VxT1dydkpnOVdsdnBiQQ?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxNNmdKUExrYVZYSTNzX2dFY3kxQjd3UzlFSEg3aHIzeEtpeWRmTVlzSm1wckhlcVdlX0h5OGdkM2J4dkR4cHh2RENCZ0daUnEwaFdnRGstdUtDTlVyT0ZYUGI1VmNpREtnSnF6dWxaSGlKOU9aNS1OUWZaRG1BMnhVRlhSYnc3QzlodnRIZ1dhUF9lTW5iUXloaFRvMWFuRnZzSnVpN1QzZXQ5ZjU0akIwQXZYblZLNEtHMjJTdnN5YTVkV3B3OUN2QU9jeGVPcGEwcks2SWZQTQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
