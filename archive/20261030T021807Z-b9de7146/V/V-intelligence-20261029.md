# V Intelligence Report

- ticker: **V**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:37:14.202903+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 6, 'ai': 13, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/V** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 41.67%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 410.5400 |
| Return 1D (%) | 2.4813 |
| Return 1W (%) | -0.9171 |
| Return 1M (%) | 12.2062 |
| Return YTD (%) | 17.7626 |
| Return 1Y (%) | 21.2562 |
| Annualized volatility (%) | 22.3143 |
| Beta vs SPY | 0.2678 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 0.9777 |
| Downside deviation (rf=0, %) | 13.8557 |
| Sortino (rf=0) | 1.5746 |
| Historical VaR 95% (1D, %) | 1.7961 |
| Historical ES 95% (1D, %) | 2.6824 |
| Correlation vs SPY | 0.1525 |
| Tracking error vs SPY (%) | 23.9366 |
| P/E (trailing) | 33.32 |
| P/B | 21.07 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 13.20 |
| Forward P/E (estimate) | 23.95 |
| Gross margin (%) | 97.68 |
| Operating margin (%) | 0.00 |
| Return on equity (%) | 63.51 |
| Free cash flow yield (%) | N/A |
| MA50 | 380.3538 |
| Close vs MA50 (%) | 7.9363 |
| MA200 | 341.0229 |
| Close vs MA200 (%) | 20.3849 |
| RSI (14, Wilder) | 67.6971 |
| MACD (12,26) | 9.4047 |
| MACD signal (9) | 8.9918 |
| MACD histogram | 0.4129 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 410.5400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.4813 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.9171 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 12.2062 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 17.7626 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 21.2562 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.3143 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.8557 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.5746 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7961 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6824 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1525 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.9366 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2678 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.1805 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9777 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.9527 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.6780 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 63.5070 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 33.3231 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 67.6971 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4129 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.9363 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 20.3849 -> Clearly above the moving-average trend level.

## TAILWINDS

### Visa, IBD Stock Of The Day, Shows Bullish Action After Earnings Report
- Summary: Visa, IBD Stock Of The Day, Shows Bullish Action After Earnings Report
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxOb0dyMXRNWWZvcXlhQXNPVEJsUjAzaWRzV3Y1NGhicm9mU3JGNmx2NnM1M0tnWTNreTlDU2ROYlJtcG5QYUhxbXJLbmg2VjFKamFpVG9ReGwtVDdsaW9GUHVaZ0tLY3FkeUhYZjlxZUdValVxYlpqS1Q3UWhEMFBHUFJR?oc=5>

### Visa (NYSE:V) Stock Jumps 2.4% Following Analyst Upgrade
- Summary: Visa (NYSE:V) Stock Jumps 2.4% Following Analyst Upgrade
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQWWcwUmVJT0JLazdPdUNSYXBCSjBEV3ZqNVlKdHFYbnhyWDVIbk52NGlqVFhEck1Ba1E3NlN5dG56WGtQaDlMQkRydkFTZUM2YUw1bTIwdUswc2ZYX1Vma2xQcjJ5VGdzeVNKYm5UckMtLUp0STRSZ0JhTHR6ajM0VVlkb0xNaW5QbVE1X1NWWWtydDZLSFJJU1JBUGE1TldZTm9tcnY0VkN4RVRDS1ZmNTJn?oc=5>

### Visa (V) Stock Could Be Near Fair Value Despite Its 105% Run
- Summary: Visa’s stock may be fairly valued after a 105% run, suggesting a positive valuation outlook.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOUDhOakEyejNzU1M3RXZ3bGdRcGtuckFrTTFmcGk0WGoyb0VxNFpNS1VObGVfQmVPdFVKWC0tcjc0Rk83Z1JNX3lVNnE5R0Q3bDRNdGpFdk9GNHVlbjdWLWtoU2huTGxrNnlhZnFMQ0xaa2owRU9EYlNPbXExclIwbTYxMkFhRWs1cnNNbUgwRW1NUQ?oc=5>

### Visa (V) Stock Could Be A Bargain On Record Revenue Growth
- Summary: Visa’s record revenue growth suggests a potential bargain for investors.
- Date: 2026-10-29 | Impact: high | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQeWc0ZUwxcXpTaVdIQ1NCenRubXBzNDBHclFqYkxqWDgzemxKemlITnh5MXNDYjVkYmVIMmpNazZPZXVVQWpUQndFd2Y5eEVBc1Y3R0xvNWdtbXBOYXVkMENxbEhBQ19sajJEZEF4T1RPTWhySjdwMjlMUnQxM1Vkc1BJZ0JPQV9zZ2lFQnFjQWYtZXhPdks2WXlkVlJWOGRUbTRGNFhRM1FtMklZdXBNN3RaejNMVlRqYVdMaGxNc01wMXQxN09F0gHMAUFVX3lxTE5tNU1qLUgtNUZMeXFxV09hLUtJaExqVmswcUN6OXIybzdzQ1RBM0ZXOEx0TkxuVGZoNVdRMzh4MWx3M3pDemVkX0dKZFB0akg2T1BwbHlNUzRuQ0tlbjljNzU1VkxHUjRYQklOVmd1Z0xiTU5WNjExWTF6VXBRbmwteWFxVlZvTXFhOWVpNUVkSm56ZzdQbW1SbG4zaHluSEttT3F2dWlPTHRRMVFuRThEcVlmMjBBUEhlWTUweVZqelh5QWR3cDZUOVU1Sw?oc=5>

### Analysts Have Conflicting Sentiments on These Financial Companies: Visa (V), PayPal Holdings (PYPL) and TransUnion (TRU)
- Summary: Analysts are divided on Visa’s prospects, reflecting uncertainty in the sector.
- Date: 2026-10-29 | Impact: medium | Horizon: medium | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMinwJBVV95cUxOYnBoZ19YTzBGZVR4YzFMOXNPbVZpc3FPUlV1MG92TlNtSWx3UFBPX0pPMVo1dWZQeWFfZEZfOGE0R3BwTGs2NTRZaUhaTjkzd2dBWXdKY0V3QTM5eFJxU2EzSmZ5Q3EwbkZJaUhsUngtV1RlNjhfdVJpTTdzeUFqSFdzRG9SYmhJTmJ2T2IxZ2p3RXVmT2JSSkZKUUlnbm15eWltQVVnd0dYZ3BRZ1NSSlY4MFZyX0NCYmtTbHQxdVJyaWZCOENCVVg4RHBDVEdMVDc5WUtvUlJHTzFWM3RmUkd0aU9IcmFzSHZnZHJwZTZWdDNKcDc1b2VLMS10M2YzWkJtOThpa2VSek84Ulo2OXZlejlJM2hsckg2ckdPcw?oc=5>

### Visa vs. Block: Which Digital Payments Stock Has More Upside?
- Summary: Comparison highlights Visa’s potential upside over Block in digital payments.
- Date: 2026-10-29 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQMTRULXNka2pJcC05Z3BNOXpWZ1g4V1N2MHVBMzZMZXR4aHBYeHl4dXVzeGd0YVpHTmtaLTA2ZktPTXZ1cnNOMWRUZzE5SjRETklJR183ekVER2VLTHQwNENiSXBGaGJfTlFKWDdmVzVkaU1yOXkwOUpiSlpsZ2ZNSEdKeUxDT1FWWVhCMUtSa2Z1SU81aTVLRVhOU1lIVXhXU1UwNnVvVElHWmpfWXNFZHBfOEM?oc=5>

### Are You Looking for a Top Momentum Pick? Why Visa (V) is a Great Choice
- Summary: Visa is promoted as a strong momentum stock for investors.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNTE9QUWJSeXZfNnM1ZktLbEEtN2VMVHo3OWJTaVVPb2lYOERCckV0VHIwbnVFSWFSZnd6ZHB4MVhvdkcxb0RScVNRbnp3RHl1ZG9EbU0xNmFrX3hyZDVEdWxYX2hXNmRtQVVpWGFyUnhtRjNZUWRKeUJTRGtoc05GVXI4eGd3ekN0MWVhYWoyUmNpRnZ1UGFGbWd3?oc=5>

### Visa Stock Outlook: 3 Key Things Investors Must Watch Before Q4 Earnings
- Summary: Key factors to monitor Visa before Q4 earnings release.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPN2ZWZlF0WjN5cWFYT3RvVV9zXzFibk5JRWl4MjU3ZWN5cUpCdkEyTnlWWDh1SGpBbkxnblZlVFNSVHREVDdiZ0h1Qk8zMlFiUWJWbHJHa09CTEF0UDBrX2hSeWo5eE5zWm1Fci1TYUgyOHZiVUVReDVwdEk2NGt6aWlKdTZQMTNPN1BUUGp6OG9JakZidHROLW9vWFFITnBudGJBVXJaOXo4elNjUWF2TGVEVlljd3dabkdQcXhfOUxSUl9kaUhIRHdB?oc=5>

### Wells Fargo & Company Issues Positive Forecast for Visa (NYSE:V) Stock Price
- Summary: Wells Fargo forecasts a positive outlook for Visa’s stock price.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxQMkhmSjlNOWhfeFE0RGFWTWRmRUc2ZzZJMmp1akNHZmxCaDZ5R19meFBJdHI4SjBjT3Etdk5NZUF5NXlhblAwZm1oQ2kwdklCZ0Z0dlJQeE03YjJGaWxIcjR0ems3MVRmTEVFVnR0U1V3S05iMWhGbnllVi1MQmRQcnhaSUptVjJvTk1kS1Z3NmNtZlZLckZjRDhTN2VfVXhGV2g2MjNnUW15MDRVOVhlOVpJRkg4TXlfenFpWkpqRnAtbmdwSzZJZ1JXU2RCVWc?oc=5>

## HEADWINDS

### Visa Stock Inches Lower Despite Revenue Beat
- Summary: Visa Stock Inches Lower Despite Revenue Beat
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOQ0JtM0JOc2NMd2VBVV9JUTJLaDhRVVgwZ2h4d1JXQ3ZrYUFKMEVsamN3Wmk5WlNEamZTWkFtZ1NJQWtLTkdkeUJNVGY4aWdaT0ZWdHF3ZkU2U2VzdWtQd1Uzb1pselhZRGc3eEl5ZzN5WGtYY1hxUUlnV1FLRGdhYm4wTkt6MjhDdmhWOEJTYjhFT2NaY1NUdUQwdjA?oc=5>

### Visa Q4 earnings beat, revenue in line as payments volume growth ticks slightly lower (V:NYSE)
- Summary: Visa Q4 earnings beat, revenue in line as payments volume growth ticks slightly lower (V:NYSE)
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPeUZJR2FrYThtRXdfYnhJUjdwRGxSTnFvTV9WbC1VTnpZTXZzNzhNVTlFZUNrSFpSekE5QVZsdEI4c1BhVU5SQk1wbHBMQ0dDYVpRdUFYMngzY2JPdnVUSEhPeG9Jb3FNRm83cWdqeWhnLWtMMjRSQk1PTHFxNEJDYmJORldjRnBoajdEZ05aX2gxTGxLUzRGQUJ1czA2d25FSkFuYmoxLWJLNWJ0ZnVBT1FpOEV5ZHBVUHp1cWpWMA?oc=5>

## CATALYSTS

### Visa Just Hiked Its Dividend 16.4%. The Small Yield Is Hiding a Compounding Machine
- Summary: Visa Just Hiked Its Dividend 16.4%. The Small Yield Is Hiding a Compounding Machine
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOam82YTZSWlVDQmdiM3dYbzhNWVctVmpCTGlXZENFMnpUS0xoN3pBR2I5NlpjLUVaMWdGbWJpb3Bvbk54dkJ1dHpKM2JkOUxkQUtBLXJfUU8wbGtNZEJoTWFUM0lweGZoX0NBWkswem44ZFk1WlhaMmhqeTJPM0hxMGJCMzRiVGFzc0ZGQmw1QlpfanJtdnNN?oc=5>

### Visa (V) Q3 earnings: what to expect
- Summary: Visa (V) Q3 earnings: what to expect
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPSXlJZkxLSEdaS2dtZXJyNkpfWDdnZHpKYzlUUGlka05SWXROTi1GMEFJYjloQTVrZ3NNc18yOEtqdndoeURRckREazhsLVlOVDNya3JtTFZVbFhPZklsZGFhMDM3cnRTam40VElqdVJuNUFRUDFhazJCMm1BWjNmNXI0R3Z3VWFYWDFrTUlwRHhjd3FG?oc=5>

### Ahead of Visa Earnings, Here's What Barchart Data Says Comes Next for V Stock
- Summary: Upcoming earnings release expected to influence V stock direction.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPVDRYY0luc2lVWF9UMW1NMFRNQmNHMEU5QXRrQ0RvaDVlbkJNUTFCUWpRdExncWlobndYNnUyNTBGYlVoaENBM1FtZTVkOGwzaDFCamttNVdjbXhJeWZwZjNsci1Rd2JKbEstLVE1ZzNoOExfQWlUWmxuRk1nejVseFVfcUp1c1lWTXFHZl8zcllrblh0N1JNWFZKUXZuYXdRQk1XcXM3QW5Sd1pSN3JvbGNJaGgzVE9haWJHdA?oc=5>

### Visa (V) Unveils New Commercial Payment Tools, Is The Stock Fully Valued?
- Summary: Launch of new commercial payment tools could drive growth, acting as a catalyst.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOaWNFWnd6Ny1vamNxdmVnTjNSajlwUldaQ0JyOFpFZFFmbzZabUVKbmZUWmwwSDVCdXd2YnVxRXg4SUctZzBUZmVKcVhnaWpYekdPT05QZXFYSTBBNUtBODV4a2JPTGNpMG1kdnpxZERVYWpaU0tWYWJjajBrR19GRXp2c3plRzBxb3R3aGNtTFZsWWdseG9VSDl6b1Ytak0?oc=5>

### Why the Market Dipped But Visa (V) Gained Today
- Summary: Visa’s stock rose while the broader market fell.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNVlQ3cWRrV1U4ZmJheVBwUlNLdzVPWm5uTzBCWURZZm9wWkl5SlM2MVhkb25yTlcyOGlndFJJLWVVRnEyVTA5OFZTM2pEcGhaeExoRndoR1lPUWRhb3p2SWcxLTVPRzhTLV9JanAzWExmRldwek5VbmRVNUxHLXRoLUdFYTdxRV82Ukw1S2ZuNDRoU28?oc=5>

### Etsy, Visa , Everpure Among 8 Hot Prospects New To Big Cap 20 And Stock Spotlight Lists
- Summary: Visa listed among hot prospects in analyst spotlight.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPbGZzNl9idkVQQzV4STJEZ05nVmh2d2k2UnlDWXhXM3UwMnNYVEZ3c0JCMnhQZXBGZW15WWc2LTZ1RHozalEyZld5MDFUdlhMVEJsOG9YWU55aXI5aDJZeDBDbUdCWWl5SFVXM1l3TzdxclJlbmtzdTAwUG56akw1OERTLXY3V00xLU01U3kwc0xVRGdZNlN4MU96cENRdzFDZlpHbFhSTW9zSkJTZGdWYUtlS3V6SWNFMnA0Mw?oc=5>

### Wall Street Analysts Think Visa (V) Is a Good Investment: Is It?
- Summary: Analysts view Visa as a good investment.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPT3FoQVBSSkF0WDFmdEFCdGpOR0tHVmtMUE1Hek5WX0ViZ2V2QVU2VGVCNndSSFpOQm8wYVJUNXBHY3lyMW9SdVdYeHh0dzdTV3JfUEZES2VGcWk3OGVhY2NudFZDZUUyMHpDaVgybVg2eTJMTm1CN09NczMxVHVSRm1WWlBoY0h2Mms4OHlwUkZ4OUg0MVJxMF9UYmU?oc=5>

## RISKS

### What Drives Visa’s (V) Long-Term Compounding Potential?
- Summary: Factors affecting Visa's long-term growth prospects.
- Date: 2026-10-26 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNaFQ4YmdZOVBMM09WS1pCQ0NybnNPSlM1QXFKVUJaWHJxbmFHVDRVYjNDQ2g1Ty13OXhPUTFLYUhCa0dZRmpybkwtRXJpbndZSkswLThha2tVRDJOc3FLYWQ2ZHlpbFVLS1FjMkpiXzFOM1BLYzh3T08xN01sRTJWUEdhZk9QN3I2bGM1LUVKN2RRQQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **V** | **33.32** | **21.07** | **N/A** | **13.20** | **767,301,713,920.00 USD** | **21.26** |
| MA | 34.97 | 99.39 | 25.67 | 14.10 | 556,879,511,552.00 USD | 15.36 |
| PYPL | 10.87 | 2.45 | 7.99 | 2.00 | 47,305,990,144.00 USD | -17.36 |
| AXP | 18.24 | 6.07 | N/A | 11.30 | 217,064,374,272.00 USD | -8.62 |

Peers fetched as_of: 2026-10-29; V reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-29
- Revenue (latest available single quarter): 5,840,000,000.00 USD; period 2019-04-01/2019-06-30; fiscal year/reporting period 2019/Q3
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/1403161/000140316126000104/v-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiggFBVV95cUxOb0dyMXRNWWZvcXlhQXNPVEJsUjAzaWRzV3Y1NGhicm9mU3JGNmx2NnM1M0tnWTNreTlDU2ROYlJtcG5QYUhxbXJLbmg2VjFKamFpVG9ReGwtVDdsaW9GUHVaZ0tLY3FkeUhYZjlxZUdValVxYlpqS1Q3UWhEMFBHUFJR?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQWWcwUmVJT0JLazdPdUNSYXBCSjBEV3ZqNVlKdHFYbnhyWDVIbk52NGlqVFhEck1Ba1E3NlN5dG56WGtQaDlMQkRydkFTZUM2YUw1bTIwdUswc2ZYX1Vma2xQcjJ5VGdzeVNKYm5UckMtLUp0STRSZ0JhTHR6ajM0VVlkb0xNaW5QbVE1X1NWWWtydDZLSFJJU1JBUGE1TldZTm9tcnY0VkN4RVRDS1ZmNTJn?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOUDhOakEyejNzU1M3RXZ3bGdRcGtuckFrTTFmcGk0WGoyb0VxNFpNS1VObGVfQmVPdFVKWC0tcjc0Rk83Z1JNX3lVNnE5R0Q3bDRNdGpFdk9GNHVlbjdWLWtoU2huTGxrNnlhZnFMQ0xaa2owRU9EYlNPbXExclIwbTYxMkFhRWs1cnNNbUgwRW1NUQ?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQeWc0ZUwxcXpTaVdIQ1NCenRubXBzNDBHclFqYkxqWDgzemxKemlITnh5MXNDYjVkYmVIMmpNazZPZXVVQWpUQndFd2Y5eEVBc1Y3R0xvNWdtbXBOYXVkMENxbEhBQ19sajJEZEF4T1RPTWhySjdwMjlMUnQxM1Vkc1BJZ0JPQV9zZ2lFQnFjQWYtZXhPdks2WXlkVlJWOGRUbTRGNFhRM1FtMklZdXBNN3RaejNMVlRqYVdMaGxNc01wMXQxN09F0gHMAUFVX3lxTE5tNU1qLUgtNUZMeXFxV09hLUtJaExqVmswcUN6OXIybzdzQ1RBM0ZXOEx0TkxuVGZoNVdRMzh4MWx3M3pDemVkX0dKZFB0akg2T1BwbHlNUzRuQ0tlbjljNzU1VkxHUjRYQklOVmd1Z0xiTU5WNjExWTF6VXBRbmwteWFxVlZvTXFhOWVpNUVkSm56ZzdQbW1SbG4zaHluSEttT3F2dWlPTHRRMVFuRThEcVlmMjBBUEhlWTUweVZqelh5QWR3cDZUOVU1Sw?oc=5
- https://news.google.com/rss/articles/CBMinwJBVV95cUxOYnBoZ19YTzBGZVR4YzFMOXNPbVZpc3FPUlV1MG92TlNtSWx3UFBPX0pPMVo1dWZQeWFfZEZfOGE0R3BwTGs2NTRZaUhaTjkzd2dBWXdKY0V3QTM5eFJxU2EzSmZ5Q3EwbkZJaUhsUngtV1RlNjhfdVJpTTdzeUFqSFdzRG9SYmhJTmJ2T2IxZ2p3RXVmT2JSSkZKUUlnbm15eWltQVVnd0dYZ3BRZ1NSSlY4MFZyX0NCYmtTbHQxdVJyaWZCOENCVVg4RHBDVEdMVDc5WUtvUlJHTzFWM3RmUkd0aU9IcmFzSHZnZHJwZTZWdDNKcDc1b2VLMS10M2YzWkJtOThpa2VSek84Ulo2OXZlejlJM2hsckg2ckdPcw?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQMTRULXNka2pJcC05Z3BNOXpWZ1g4V1N2MHVBMzZMZXR4aHBYeHl4dXVzeGd0YVpHTmtaLTA2ZktPTXZ1cnNOMWRUZzE5SjRETklJR183ekVER2VLTHQwNENiSXBGaGJfTlFKWDdmVzVkaU1yOXkwOUpiSlpsZ2ZNSEdKeUxDT1FWWVhCMUtSa2Z1SU81aTVLRVhOU1lIVXhXU1UwNnVvVElHWmpfWXNFZHBfOEM?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNTE9QUWJSeXZfNnM1ZktLbEEtN2VMVHo3OWJTaVVPb2lYOERCckV0VHIwbnVFSWFSZnd6ZHB4MVhvdkcxb0RScVNRbnp3RHl1ZG9EbU0xNmFrX3hyZDVEdWxYX2hXNmRtQVVpWGFyUnhtRjNZUWRKeUJTRGtoc05GVXI4eGd3ekN0MWVhYWoyUmNpRnZ1UGFGbWd3?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPN2ZWZlF0WjN5cWFYT3RvVV9zXzFibk5JRWl4MjU3ZWN5cUpCdkEyTnlWWDh1SGpBbkxnblZlVFNSVHREVDdiZ0h1Qk8zMlFiUWJWbHJHa09CTEF0UDBrX2hSeWo5eE5zWm1Fci1TYUgyOHZiVUVReDVwdEk2NGt6aWlKdTZQMTNPN1BUUGp6OG9JakZidHROLW9vWFFITnBudGJBVXJaOXo4elNjUWF2TGVEVlljd3dabkdQcXhfOUxSUl9kaUhIRHdB?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxQMkhmSjlNOWhfeFE0RGFWTWRmRUc2ZzZJMmp1akNHZmxCaDZ5R19meFBJdHI4SjBjT3Etdk5NZUF5NXlhblAwZm1oQ2kwdklCZ0Z0dlJQeE03YjJGaWxIcjR0ems3MVRmTEVFVnR0U1V3S05iMWhGbnllVi1MQmRQcnhaSUptVjJvTk1kS1Z3NmNtZlZLckZjRDhTN2VfVXhGV2g2MjNnUW15MDRVOVhlOVpJRkg4TXlfenFpWkpqRnAtbmdwSzZJZ1JXU2RCVWc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOQ0JtM0JOc2NMd2VBVV9JUTJLaDhRVVgwZ2h4d1JXQ3ZrYUFKMEVsamN3Wmk5WlNEamZTWkFtZ1NJQWtLTkdkeUJNVGY4aWdaT0ZWdHF3ZkU2U2VzdWtQd1Uzb1pselhZRGc3eEl5ZzN5WGtYY1hxUUlnV1FLRGdhYm4wTkt6MjhDdmhWOEJTYjhFT2NaY1NUdUQwdjA?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPeUZJR2FrYThtRXdfYnhJUjdwRGxSTnFvTV9WbC1VTnpZTXZzNzhNVTlFZUNrSFpSekE5QVZsdEI4c1BhVU5SQk1wbHBMQ0dDYVpRdUFYMngzY2JPdnVUSEhPeG9Jb3FNRm83cWdqeWhnLWtMMjRSQk1PTHFxNEJDYmJORldjRnBoajdEZ05aX2gxTGxLUzRGQUJ1czA2d25FSkFuYmoxLWJLNWJ0ZnVBT1FpOEV5ZHBVUHp1cWpWMA?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOam82YTZSWlVDQmdiM3dYbzhNWVctVmpCTGlXZENFMnpUS0xoN3pBR2I5NlpjLUVaMWdGbWJpb3Bvbk54dkJ1dHpKM2JkOUxkQUtBLXJfUU8wbGtNZEJoTWFUM0lweGZoX0NBWkswem44ZFk1WlhaMmhqeTJPM0hxMGJCMzRiVGFzc0ZGQmw1QlpfanJtdnNN?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPSXlJZkxLSEdaS2dtZXJyNkpfWDdnZHpKYzlUUGlka05SWXROTi1GMEFJYjloQTVrZ3NNc18yOEtqdndoeURRckREazhsLVlOVDNya3JtTFZVbFhPZklsZGFhMDM3cnRTam40VElqdVJuNUFRUDFhazJCMm1BWjNmNXI0R3Z3VWFYWDFrTUlwRHhjd3FG?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPVDRYY0luc2lVWF9UMW1NMFRNQmNHMEU5QXRrQ0RvaDVlbkJNUTFCUWpRdExncWlobndYNnUyNTBGYlVoaENBM1FtZTVkOGwzaDFCamttNVdjbXhJeWZwZjNsci1Rd2JKbEstLVE1ZzNoOExfQWlUWmxuRk1nejVseFVfcUp1c1lWTXFHZl8zcllrblh0N1JNWFZKUXZuYXdRQk1XcXM3QW5Sd1pSN3JvbGNJaGgzVE9haWJHdA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOaWNFWnd6Ny1vamNxdmVnTjNSajlwUldaQ0JyOFpFZFFmbzZabUVKbmZUWmwwSDVCdXd2YnVxRXg4SUctZzBUZmVKcVhnaWpYekdPT05QZXFYSTBBNUtBODV4a2JPTGNpMG1kdnpxZERVYWpaU0tWYWJjajBrR19GRXp2c3plRzBxb3R3aGNtTFZsWWdseG9VSDl6b1Ytak0?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNVlQ3cWRrV1U4ZmJheVBwUlNLdzVPWm5uTzBCWURZZm9wWkl5SlM2MVhkb25yTlcyOGlndFJJLWVVRnEyVTA5OFZTM2pEcGhaeExoRndoR1lPUWRhb3p2SWcxLTVPRzhTLV9JanAzWExmRldwek5VbmRVNUxHLXRoLUdFYTdxRV82Ukw1S2ZuNDRoU28?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPbGZzNl9idkVQQzV4STJEZ05nVmh2d2k2UnlDWXhXM3UwMnNYVEZ3c0JCMnhQZXBGZW15WWc2LTZ1RHozalEyZld5MDFUdlhMVEJsOG9YWU55aXI5aDJZeDBDbUdCWWl5SFVXM1l3TzdxclJlbmtzdTAwUG56akw1OERTLXY3V00xLU01U3kwc0xVRGdZNlN4MU96cENRdzFDZlpHbFhSTW9zSkJTZGdWYUtlS3V6SWNFMnA0Mw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPT3FoQVBSSkF0WDFmdEFCdGpOR0tHVmtMUE1Hek5WX0ViZ2V2QVU2VGVCNndSSFpOQm8wYVJUNXBHY3lyMW9SdVdYeHh0dzdTV3JfUEZES2VGcWk3OGVhY2NudFZDZUUyMHpDaVgybVg2eTJMTm1CN09NczMxVHVSRm1WWlBoY0h2Mms4OHlwUkZ4OUg0MVJxMF9UYmU?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNaFQ4YmdZOVBMM09WS1pCQ0NybnNPSlM1QXFKVUJaWHJxbmFHVDRVYjNDQ2g1Ty13OXhPUTFLYUhCa0dZRmpybkwtRXJpbndZSkswLThha2tVRDJOc3FLYWQ2ZHlpbFVLS1FjMkpiXzFOM1BLYzh3T08xN01sRTJWUEdhZk9QN3I2bGM1LUVKN2RRQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
