# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:14:35.581570+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 2, 'ai': 16, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'low_uncalibrated_model_confidence': 2, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 7 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 72.73%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 542.1900 |
| Return 1D (%) | -0.8739 |
| Return 1W (%) | 1.9116 |
| Return 1M (%) | 6.9050 |
| Return YTD (%) | 7.8663 |
| Return 1Y (%) | 10.6149 |
| Annualized volatility (%) | 14.6831 |
| Beta vs SPY | -0.0480 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 0.7632 |
| Downside deviation (rf=0, %) | 10.1538 |
| Sortino (rf=0) | 1.1037 |
| Historical VaR 95% (1D, %) | 1.4122 |
| Historical ES 95% (1D, %) | 2.0016 |
| Correlation vs SPY | -0.0417 |
| Tracking error vs SPY (%) | 19.8415 |
| P/E (trailing) | 13.64 |
| P/B | 0.00 |
| EV/EBITDA | -1.79 |
| Revenue growth (%) | 10.00 |
| Forward P/E (estimate) | 24.17 |
| Gross margin (%) | 30.33 |
| Operating margin (%) | 32.56 |
| Return on equity (%) | 12.12 |
| Free cash flow yield (%) | 6.20 |
| MA50 | 510.8192 |
| Close vs MA50 (%) | 6.1413 |
| MA200 | 494.5915 |
| Close vs MA200 (%) | 9.6238 |
| RSI (14, Wilder) | 73.5395 |
| MACD (12,26) | 9.4436 |
| MACD signal (9) | 6.3486 |
| MACD histogram | 3.0951 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 542.1900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.8739 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.9116 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.9050 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 7.8663 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 10.6149 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 14.6831 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.1538 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1037 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4122 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0016 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0417 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.8415 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0480 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7632 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.1709 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.3320 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.5610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 12.1200 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.2012 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.6366 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 73.5395 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 3.0951 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.1413 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.6238 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire shares shake the Buffett blues with new all-time highs
- Summary: Berkshire shares shake the Buffett blues with new all-time highs
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTFBDUGVaejRDVUljZ2dXVkZibE43eVJuTlpLUnRlWlpXeERSYlFtd291bEJSdWJKb2NOZ29mY0xEWWE4RHIzVGM1ZkxxempDRTl3Q09wWXpfcGRyS3p6ZkxDRVFSRndXTFBlRVRMVDJqUHJTVDdYVUhldVBJVklnRWPSAYQBQVVfeXFMUFlBMEVBeGdQbnZCdHNhSG9ldTZZai1GOUpIamhNOXBPX3hBTVc4MjZUQmpTZVYyZ1lHcWR6WWpRWS01SDg2cGF5SkNyb3lyMWNkSllkY1I3clVxdVliYWZHQ3hnV2Vka2xiSzdULXZxVWQ1RHpvTDVDSlVPUTZpaFJ4U0pC?oc=5>

### Berkshire Stock Just Hit a Record High. Don’t Back Up the Truck at the Top.
- Summary: Berkshire Stock Just Hit a Record High. Don’t Back Up the Truck at the Top.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNdmhHS1VoTmItZFplR0dLNjQ3bmE3LUNRb3RjRk5tbEE0SWVpcTA2R1duS0FRT0ppc3ZPcVp5OS1WRUhVRFJXeUZSWjBlTzgzZmh4dm5IRVpscW1CbHhPRU1SYVU1a1RMSGhGbUNEQ1gtX3gya0hxSDVpU1NkN0trSkdTZzR0RU8tODRBby1Mdk1hVzluUHh3MFFpdmU?oc=5>

### Berkshire Hathaway B (BRK.B) Increases Despite Market Slip: Here's What You Need to Know
- Summary: Berkshire Hathaway shares rise even as broader market slips, indicating resilience.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQX01PWk9DUFBveTAzMDFDMjFyeEpMNWVHLXgzaGVtRENkRWt4WW0ySkstLWVwaEVQd0tORi00aUhEaFYtQThfYUVzbkJDQW1wNWhFc3ROcEtJU3cyRFlWbThBUnBaMElIM2JiRkhvcXJvbXVXczJvaEFad0p1U1RPMF9FZGlVd09zQmVJZklSeFUtU05UQnc?oc=5>

### Berkshire Hathaway (BRK.B) Stock Could Be Cheap Even After An 89% Run
- Summary: Shares may be undervalued after a steep rally, presenting a buying opportunity.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxOcDc3SE96MnNGdEFhUU9yMF82MThGeUJFMk9nelVIMnBDdnJNUWVxejIzZGh0bG8xeFJxek5ZVkg1Vy1ZYzRPSFliZ0VyRnRLWU1GV1Fvc0xfYXk5OU12eHhEMkJjTEVFS0FQM2VPTXRMZnk4Tkl6Q0ZLS2JyTjg0NVFGakxvT0RUM3pyNXhUYmVqZjNscjQwMlhGaDZ4TzhORlJ0cHYwQ2hseG1iVUJTT0xtdzM2el81bjh0eHBpWmRJSU5jSWhhV1BTSDZDZk1IVklWMlp5S05Ub19wNXZqaUt3a1LSAeoBQVVfeXFMTXhUZGNQM0diWUppZjVGeWZHMDJJSGJRZm5nTVl4LWpYVHdrX0Z3dGFrdjcyM1hMZmhTMDljeUsxcUhVT183ak0yZkVUTV9HZEgtOGtUV3ZQclBReGpyR0VsTFEwV0pOWDN3VWFvRllUeVN5TEI0eUVzdG81bFZHTVNFeWo3bFBJTHRZSWl5ZG1HY0RjeHdYWGwxVnpubXItd0J1czRwZnV6ZG50ZDBPc0p4cnFDSktLSTZ6RkZHTmN6c2NGMUlmVkpuaXdQYjJ0azA1SFNqaktpUXl5bjF4U2RzZmZiWUV1cHdn?oc=5>

### Buffett’s Berkshire just trounced chip stocks and flashed a rare dot-com-era signal
- Summary: Berkshire outperformed tech stocks, signaling strong market performance.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxOWnVNeFl1TkgzcElCT2x0MElyZ3NLY0lFVEJ2TjF5NlhjU3dya0QxU05GUU5UTzNrRlZTdVgzVUdWeFMtNlhKRTBTUDBoTHhxQngtdWFPSEJuZzkxUThDLVRFRk90am9QNHZIN01EeGRqQTBzN3NUTUhfQnhVRnp6YlI1WEtRUW9RTU5hOHBEWGU1RHgySUxIV2pGamlNaEZ3ZWVMQkFQZklWbDJZaUZnNU9wQzFBbktHTEhDWHM3SVVtWWtHMXJPUXZQWWF1eDcwT0NVdkln?oc=5>

### Berkshire Hathaway Stock Rose 10 Days in a Row in October for the First Time Since 2018. Here's What History Says Comes Next.
- Summary: Extended rally suggests potential continuation of positive trend.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOZkFuMWpmT3otRzRPaEpoM0xlaUFNU2Y0cjYyZXYxRVJtZlRKVFl0Z3ZyQXpxdDVCSXp3X3hfZmFRY3NCaHlqVFgzSUNseWdvLXhIQWdyUnFfdlNkb3hqZVFqOTFhb19DdVpPc3lBaVBWdm9LZkhOTks0QkNEcThfSnY5a2hRUTFYdVNlbVQzUHd0OFdHTldXOTFuRXpiUQ?oc=5>

### Berkshire Hathaway stock hits new high, giving Abel a vote of confidence (BRK.B:NYSE)
- Summary: Berkshire stock reaches new peak, boosting investor confidence in Abel.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQN1p1YUs2X0FtTFg1ZVowOXFfNFpkTlBhbnVUSjdBclY5TjVJVnd5eW1Cb3JDYTJKUXg1amJVQUZhZTRVWUF6TTNpX0pxYkpRemxDeW4zS3FETW1zcWRES0FBbFV3WWNGdm1CXzdyckJXd2Nzd3doV0VjNmpzV21fbWUwSnREdWZBcXBCd3hHNVZaZDBBbjBmZEJvbFJhd1k2NldweGVLcy16TmdWR2c?oc=5>

### Berkshire Finally Topped Its Pre-Buffett-Exit Peak
- Summary: Berkshire surpasses its pre-Buffett peak valuation, signaling strong market performance.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNZV96cW9STksxZ0hjWFNDbDZTWXVicUhzeFdQaVo0eXZSUmx2clZ4MGxmd3hiOUtkcUoyZzFQVW5jc2VPUlpMeDNWdENpS0FtRXA3bEc3cWdLbm0tVDl1WGdMQWNLNnNvS0dVRGY2ejRvUUpiTHZhalRSLTN4ZElsRGFNNi1lX0R4aXhTLTMzWEZuVU1jLXNkR29SbDRuYmJjakU0?oc=5>

### Warren Buffett's Successor, Greg Abel, Has 32% of Berkshire Hathaway's $364 Billion Portfolio Invested in 3 Unstoppable AI Stocks
- Summary: Abel’s AI-focused portfolio allocation highlights strategic growth focus.
- Date: 2026-10-23 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxPb2szY1FfR0FCYlV0N29iSWg5bndSdFdfTWNBazJoSC00Mi16RDFTa3pPaFNSTDU3elBINGRwZEprOHY4VWx0cE82a1BkeEIyZWdFbmFNYnRwWDVkVDN5WnZVcFhpbUJzSlVhYWIzb19mUjBzNkNFbTUxQWtFVjB2U2tNNXNrRVFlSlhGeEpZN29nODRTSmtpR0xub0kwX09QUXlIVXZrQ1NIcjhVWTUtenFBbzNxVFI0TS0ySDlpcVdOVkhJd2I2ZnlENEdrdGZrb1VKX19oTVh3Y3pYYm5sS2diTW12Z09SeEE?oc=5>

### If You Invested $1000 in Berkshire Hathaway B a Decade Ago, This is How Much It'd Be Worth Now
- Summary: Shows past performance, indicating strong long-term growth.
- Date: 2026-10-20 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQTDQyeHYwMFFFQjB5OE82enFpc3NMNTdPdF9Wdno1SEdfSGg5eU04V0lfOVZUUHNpZTFNMks4cDBrb190Q2VMZFZ2cGdFbDc0SC1NUGtkMDA5ak1sNG1PX0pNSGFpV0VnclRLZUUzT0d4S3V0TmxTWjI1b2NEVENVd0hCZUNSaUhXbEpndmF5Tk5HTTRqS080bTBiOEpVOElH?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Berkshire Hathaway Started Buying Back Its Own Stock Again This Year. Should You Buy It at a Record High?
- Summary: Company repurchases shares, indicating confidence in valuation.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOX0FmSDUxcTQ1bWV4bS1NVWM5bWdsRGhVZ1pJT0s2aUpYWXpHQnluZ18xRk03WlBVLV9WQ0t1bGY4MTJrRms5UlRzckNaNUF1YUp0YXpxQTB4bVpKdUdoZ3VIQVIwalF5WUQ5azBmQVU3VFVDajh6SWRNcTE3SGFFSUE2eC1UcE8wNENMZzdkWTlCRGg2X3NtQnNSTEhGcVp5LTQ0NnRB?oc=5>

### Berkshire Hathaway (BRK-B) Starts Spending Its Cash, but Is 24 Times Earnings Fair?
- Summary: Berkshire begins cash outlays, raising questions on valuation and spending strategy.
- Date: 2026-10-21 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQcjBSTEFUWUxMNFBQUmFMME5sWHUzbkdUY0RVNURhSUdLamhVYjVxX3pEd0d6Q0NHOUlJOTZvSEoxYjAxcVdSRnhidDNfa0VzMU5DaVdia0c4ZTMzUWdBc1NWS0hrTVFqdDZfTlBlYTlPeExrdW5ibVdvWGdwUVoxN2NEOENKQjFyMjV3NG9PYUVYR09wOTZGQWJrV3o?oc=5>

### What Could Berkshire Hathaway (BRK.B) Gain From An Early AI Funding Round?
- Summary: Speculation on potential benefits from early AI funding for Berkshire Hathaway.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNZEw2bVhaMGVVc0FlS1RMOEtGWUNjVUMzZEZjeVhNNExOQUxqZThIOGZHNi1QTDVCaFc0OWpvQkF1OFprRWFKVUJTRnFyeS14MVZaZDVMdy1PYU00N01zd1diM3FVRXdaeElHamRwR09BM0NQVWFCVHBtdHk5d2l1aVFzVTlRWHZ1TG1YeEU2cFU0cXFNVzg2NHVB?oc=5>

### Berkshire Hathaway-B (BRK.B) Stock Forecast & Analyst Ratings
- Summary: Analyst forecasts and ratings for Berkshire Hathaway stock.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAJBVV95cUxQVEU2eWlZYW8zdlpZMlBrWlJSOWNIV1h1aEtFYnk5LWJVS1YtRjBYYlNuUEl2WGtxUzg1T0dKZURScldEZEVhdUVjWThEcFhBTGg2Mlh0Z2l6dVc3Q1hBQWF2d3RfUDZ1UXN2dWF1REZJWXVncDA3WGcxUERXNzRsMEdocXVyRTl4b3NLMlIwRy0tUjNCV0lUUV82MFlFTzBVY0tpaXJWVnRhYzBZUGhLeTlFVWpDWUVMOUxKcmUxNGM5Tm5MUmE2V0hhbW00MlQtQlFtb0FvaHVzbjk0M3dBMnI5eXFkaDBUTVBSZHJZZmxyOHpxcm9GYkpBeEF4NE9FbkZlZUpmYzl2YXhQWWRCeWpzbk1QU2hkem1iaTh1YzUzQXpXNmRfOXczNEpxSURiS2dUSWlZS2I?oc=5>

### Warren Buffett's Successor, Greg Abel, Has 22% of Berkshire Hathaway Invested in This Stock That Just Crossed the $5 Trillion Mark
- Summary: Portfolio shift: 22% invested in a $5T+ stock.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQWmFaalFEVEVoODVHbG9EVkFMS0lzQ3MzM2VoQ3dKRVBmaXJKRWhndGx5RGtneThUQ0ZRamVENE16ejdpZHRhTi1RdFpQd0NEV09waF9kZDJrbWJTd3RGc1NHSU1FRDZJay1tUkFTWHY5YXRMSHhMX3l4M2N5MGJKOHNnTzB1UUhIZk5sejNIWjNJUTl3dXlvOXRnZmtWQWNlcWc?oc=5>

### 2 Stocks to Buy From the 5 That Make Up Roughly 61.5% of Berkshire Hathaway's Portfolio
- Summary: Recommendation to buy two of Berkshire's top holdings.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQOGw2U0RrUGV4QXNGTldWOUFiOHE4clBTRVlfOFBsVEViNUxpTDU0enVQcHpWeHlqZzhZM3VSNlcyQm5VeVl4OXdNS0kyN2lLU2RBV0JyaVJLSFh3MEl2MjdIQlpfbkpuMVJRVjRlelRhWjhvSXlNRi1pU2hLMjk4Z0dHSkR2dl9hT0VhWDRjcnQ?oc=5>

### Berkshire Hathaway's New Top Holding Owns Its Market
- Summary: Berkshire’s new top holding dominates its market segment, indicating strategic ownership expansion.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxObERTV2U0UFZZSGYwQWtpZFRKSVZUcWJ6cEhnQXBMM1VzTXB1OE9TaFBXamRpQ04xQkM0Y2VOZWJETlJUNExlQ1BEY1pFakM4NGFyYUdNeWswdTI0QlpNWUl1b2EzWFNNNEJkRkt6VHVldTlESF9NWDRwaWlxajRyd0ZZUEJZRGdfT3pDQmZSTnJVakplREJCSGsxM0JpOW1oVnBj?oc=5>

## RISKS

### Can Berkshire Hathaway (BRK.A) Stay Below Fair Value After Its 87% Run?
- Summary: Questioning Berkshire's ability to remain undervalued after a significant share run.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPdGZGVW1tb2VRWENsb0ZQWkJ0a3lWbWc3UzJSa2YtLTRHNTR3bG9STC1KY1RKSFIzRE84Wm5FSFJvdldCN2lkR0w3RXBSXzJuWWhiMmkwZHV4VW5fVkN5M21pRC1qRUxpekdZMmJWeUVQcTFyZW05NHBmZTlmaFZmN2dMMWNLSHhoVXZ5WmxsSFRLWUREaTBhb2c2amd5Snc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **13.64** | **0.00** | **-1.79** | **10.00** | **1,160,671,395,840.00 USD** | **10.61** |
| MKL | 10.31 | 1.22 | 6.49 | 12.70 | 23,170,336,768.00 USD | -1.38 |
| FFH.TO | 8.76 | 1.35 | 7.89 | -0.50 | 55,217,143,808.00 CAD | 7.01 |
| L | 13.73 | 1.20 | 8.14 | 3.90 | 22,897,948,672.00 USD | 12.34 |

Peers fetched as_of: 2026-10-25; BRK-B reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-08
- Next expected earnings: 2026-11-07 (yfinance; expected dates may change)

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
- Filing date: 2026-08-10
- Revenue (latest available single quarter): 101,808,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 25,667,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1067983/000119312526341032/brka-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMif0FVX3lxTFBDUGVaejRDVUljZ2dXVkZibE43eVJuTlpLUnRlWlpXeERSYlFtd291bEJSdWJKb2NOZ29mY0xEWWE4RHIzVGM1ZkxxempDRTl3Q09wWXpfcGRyS3p6ZkxDRVFSRndXTFBlRVRMVDJqUHJTVDdYVUhldVBJVklnRWPSAYQBQVVfeXFMUFlBMEVBeGdQbnZCdHNhSG9ldTZZai1GOUpIamhNOXBPX3hBTVc4MjZUQmpTZVYyZ1lHcWR6WWpRWS01SDg2cGF5SkNyb3lyMWNkSllkY1I3clVxdVliYWZHQ3hnV2Vka2xiSzdULXZxVWQ1RHpvTDVDSlVPUTZpaFJ4U0pC?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNdmhHS1VoTmItZFplR0dLNjQ3bmE3LUNRb3RjRk5tbEE0SWVpcTA2R1duS0FRT0ppc3ZPcVp5OS1WRUhVRFJXeUZSWjBlTzgzZmh4dm5IRVpscW1CbHhPRU1SYVU1a1RMSGhGbUNEQ1gtX3gya0hxSDVpU1NkN0trSkdTZzR0RU8tODRBby1Mdk1hVzluUHh3MFFpdmU?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQX01PWk9DUFBveTAzMDFDMjFyeEpMNWVHLXgzaGVtRENkRWt4WW0ySkstLWVwaEVQd0tORi00aUhEaFYtQThfYUVzbkJDQW1wNWhFc3ROcEtJU3cyRFlWbThBUnBaMElIM2JiRkhvcXJvbXVXczJvaEFad0p1U1RPMF9FZGlVd09zQmVJZklSeFUtU05UQnc?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxOcDc3SE96MnNGdEFhUU9yMF82MThGeUJFMk9nelVIMnBDdnJNUWVxejIzZGh0bG8xeFJxek5ZVkg1Vy1ZYzRPSFliZ0VyRnRLWU1GV1Fvc0xfYXk5OU12eHhEMkJjTEVFS0FQM2VPTXRMZnk4Tkl6Q0ZLS2JyTjg0NVFGakxvT0RUM3pyNXhUYmVqZjNscjQwMlhGaDZ4TzhORlJ0cHYwQ2hseG1iVUJTT0xtdzM2el81bjh0eHBpWmRJSU5jSWhhV1BTSDZDZk1IVklWMlp5S05Ub19wNXZqaUt3a1LSAeoBQVVfeXFMTXhUZGNQM0diWUppZjVGeWZHMDJJSGJRZm5nTVl4LWpYVHdrX0Z3dGFrdjcyM1hMZmhTMDljeUsxcUhVT183ak0yZkVUTV9HZEgtOGtUV3ZQclBReGpyR0VsTFEwV0pOWDN3VWFvRllUeVN5TEI0eUVzdG81bFZHTVNFeWo3bFBJTHRZSWl5ZG1HY0RjeHdYWGwxVnpubXItd0J1czRwZnV6ZG50ZDBPc0p4cnFDSktLSTZ6RkZHTmN6c2NGMUlmVkpuaXdQYjJ0azA1SFNqaktpUXl5bjF4U2RzZmZiWUV1cHdn?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxOWnVNeFl1TkgzcElCT2x0MElyZ3NLY0lFVEJ2TjF5NlhjU3dya0QxU05GUU5UTzNrRlZTdVgzVUdWeFMtNlhKRTBTUDBoTHhxQngtdWFPSEJuZzkxUThDLVRFRk90am9QNHZIN01EeGRqQTBzN3NUTUhfQnhVRnp6YlI1WEtRUW9RTU5hOHBEWGU1RHgySUxIV2pGamlNaEZ3ZWVMQkFQZklWbDJZaUZnNU9wQzFBbktHTEhDWHM3SVVtWWtHMXJPUXZQWWF1eDcwT0NVdkln?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOZkFuMWpmT3otRzRPaEpoM0xlaUFNU2Y0cjYyZXYxRVJtZlRKVFl0Z3ZyQXpxdDVCSXp3X3hfZmFRY3NCaHlqVFgzSUNseWdvLXhIQWdyUnFfdlNkb3hqZVFqOTFhb19DdVpPc3lBaVBWdm9LZkhOTks0QkNEcThfSnY5a2hRUTFYdVNlbVQzUHd0OFdHTldXOTFuRXpiUQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQMW9rUmp4RnlObFJ3NWlmVk40d0ZPZ0gzbHlwNG5la1RLZ2xFNENxbXBsamw5dXZnTjd4NjBDanM1WTQtS3pueGNicXhMd3pNN2syRHBUYnJVR0JJc25SVmdHU2kwTWVxbm1WX2c1RDk3RkJWNmVqSFhsQWNsa1QwcGxDNV9lNGpEMUJjQTZnQzZxb28ya2cw?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQN1p1YUs2X0FtTFg1ZVowOXFfNFpkTlBhbnVUSjdBclY5TjVJVnd5eW1Cb3JDYTJKUXg1amJVQUZhZTRVWUF6TTNpX0pxYkpRemxDeW4zS3FETW1zcWRES0FBbFV3WWNGdm1CXzdyckJXd2Nzd3doV0VjNmpzV21fbWUwSnREdWZBcXBCd3hHNVZaZDBBbjBmZEJvbFJhd1k2NldweGVLcy16TmdWR2c?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNZV96cW9STksxZ0hjWFNDbDZTWXVicUhzeFdQaVo0eXZSUmx2clZ4MGxmd3hiOUtkcUoyZzFQVW5jc2VPUlpMeDNWdENpS0FtRXA3bEc3cWdLbm0tVDl1WGdMQWNLNnNvS0dVRGY2ejRvUUpiTHZhalRSLTN4ZElsRGFNNi1lX0R4aXhTLTMzWEZuVU1jLXNkR29SbDRuYmJjakU0?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxPb2szY1FfR0FCYlV0N29iSWg5bndSdFdfTWNBazJoSC00Mi16RDFTa3pPaFNSTDU3elBINGRwZEprOHY4VWx0cE82a1BkeEIyZWdFbmFNYnRwWDVkVDN5WnZVcFhpbUJzSlVhYWIzb19mUjBzNkNFbTUxQWtFVjB2U2tNNXNrRVFlSlhGeEpZN29nODRTSmtpR0xub0kwX09QUXlIVXZrQ1NIcjhVWTUtenFBbzNxVFI0TS0ySDlpcVdOVkhJd2I2ZnlENEdrdGZrb1VKX19oTVh3Y3pYYm5sS2diTW12Z09SeEE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQQ2FVRFAtN1pJYVVKTGNYYTYxajZ0Y3BXT1cyb3VRRkV3TEZtV21WS0VOWDFOMjhabFlMZVA5QVh3MVhzZTNROFM3SlRFQWFibTU1TnBWU3YxLVNSdFZ0UU5jSExwVDh0MHpzNTdDTGNpWHl3Z1Q2azdidnNfZlhJZkpuRGpHS2tBbDczWU5hZjdsSUZITWp5NGNrUTQyZDlo?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQTDQyeHYwMFFFQjB5OE82enFpc3NMNTdPdF9Wdno1SEdfSGg5eU04V0lfOVZUUHNpZTFNMks4cDBrb190Q2VMZFZ2cGdFbDc0SC1NUGtkMDA5ak1sNG1PX0pNSGFpV0VnclRLZUUzT0d4S3V0TmxTWjI1b2NEVENVd0hCZUNSaUhXbEpndmF5Tk5HTTRqS080bTBiOEpVOElH?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOX0FmSDUxcTQ1bWV4bS1NVWM5bWdsRGhVZ1pJT0s2aUpYWXpHQnluZ18xRk03WlBVLV9WQ0t1bGY4MTJrRms5UlRzckNaNUF1YUp0YXpxQTB4bVpKdUdoZ3VIQVIwalF5WUQ5azBmQVU3VFVDajh6SWRNcTE3SGFFSUE2eC1UcE8wNENMZzdkWTlCRGg2X3NtQnNSTEhGcVp5LTQ0NnRB?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxOa0dobzY5aWRZMU5ZSnB1OVlCazNWYWdtWXJ1ZWRhNFZKV01zVUtPa3ZqNTBBSjNHSmpqWnpKb2UzdnNCTlB3SklYNnlzYUJKRTRQcEVoelFHQmhaQ2hNR2pnbnlhaUpZWWVLdGVPeGJCcWF5aHN3ckQtSlc5LTJjVlFWYnoySG92Q1U3dW9kMC10TnZHWkFXbGI3U3VkMXVwbXB1UGdjWHRRakdvc09idG1vdHp3bjhJQVdPQjJRaW1WT0lLcTJMREViWnZoR3VuQTE3bzNWQU92QkdlMTRN?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQcjBSTEFUWUxMNFBQUmFMME5sWHUzbkdUY0RVNURhSUdLamhVYjVxX3pEd0d6Q0NHOUlJOTZvSEoxYjAxcVdSRnhidDNfa0VzMU5DaVdia0c4ZTMzUWdBc1NWS0hrTVFqdDZfTlBlYTlPeExrdW5ibVdvWGdwUVoxN2NEOENKQjFyMjV3NG9PYUVYR09wOTZGQWJrV3o?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNZEw2bVhaMGVVc0FlS1RMOEtGWUNjVUMzZEZjeVhNNExOQUxqZThIOGZHNi1QTDVCaFc0OWpvQkF1OFprRWFKVUJTRnFyeS14MVZaZDVMdy1PYU00N01zd1diM3FVRXdaeElHamRwR09BM0NQVWFCVHBtdHk5d2l1aVFzVTlRWHZ1TG1YeEU2cFU0cXFNVzg2NHVB?oc=5
- https://news.google.com/rss/articles/CBMiuAJBVV95cUxQVEU2eWlZYW8zdlpZMlBrWlJSOWNIV1h1aEtFYnk5LWJVS1YtRjBYYlNuUEl2WGtxUzg1T0dKZURScldEZEVhdUVjWThEcFhBTGg2Mlh0Z2l6dVc3Q1hBQWF2d3RfUDZ1UXN2dWF1REZJWXVncDA3WGcxUERXNzRsMEdocXVyRTl4b3NLMlIwRy0tUjNCV0lUUV82MFlFTzBVY0tpaXJWVnRhYzBZUGhLeTlFVWpDWUVMOUxKcmUxNGM5Tm5MUmE2V0hhbW00MlQtQlFtb0FvaHVzbjk0M3dBMnI5eXFkaDBUTVBSZHJZZmxyOHpxcm9GYkpBeEF4NE9FbkZlZUpmYzl2YXhQWWRCeWpzbk1QU2hkem1iaTh1YzUzQXpXNmRfOXczNEpxSURiS2dUSWlZS2I?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQWmFaalFEVEVoODVHbG9EVkFMS0lzQ3MzM2VoQ3dKRVBmaXJKRWhndGx5RGtneThUQ0ZRamVENE16ejdpZHRhTi1RdFpQd0NEV09waF9kZDJrbWJTd3RGc1NHSU1FRDZJay1tUkFTWHY5YXRMSHhMX3l4M2N5MGJKOHNnTzB1UUhIZk5sejNIWjNJUTl3dXlvOXRnZmtWQWNlcWc?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQOGw2U0RrUGV4QXNGTldWOUFiOHE4clBTRVlfOFBsVEViNUxpTDU0enVQcHpWeHlqZzhZM3VSNlcyQm5VeVl4OXdNS0kyN2lLU2RBV0JyaVJLSFh3MEl2MjdIQlpfbkpuMVJRVjRlelRhWjhvSXlNRi1pU2hLMjk4Z0dHSkR2dl9hT0VhWDRjcnQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxObERTV2U0UFZZSGYwQWtpZFRKSVZUcWJ6cEhnQXBMM1VzTXB1OE9TaFBXamRpQ04xQkM0Y2VOZWJETlJUNExlQ1BEY1pFakM4NGFyYUdNeWswdTI0QlpNWUl1b2EzWFNNNEJkRkt6VHVldTlESF9NWDRwaWlxajRyd0ZZUEJZRGdfT3pDQmZSTnJVakplREJCSGsxM0JpOW1oVnBj?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPdGZGVW1tb2VRWENsb0ZQWkJ0a3lWbWc3UzJSa2YtLTRHNTR3bG9STC1KY1RKSFIzRE84Wm5FSFJvdldCN2lkR0w3RXBSXzJuWWhiMmkwZHV4VW5fVkN5M21pRC1qRUxpekdZMmJWeUVQcTFyZW05NHBmZTlmaFZmN2dMMWNLSHhoVXZ5WmxsSFRLWUREaTBhb2c2amd5Snc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
