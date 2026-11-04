# MSFT Intelligence Report

- ticker: **MSFT**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/MSFT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MSFT/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T05:03:25.937853+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 7, 'ai': 13, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/MSFT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 48.0%; oldest publication 2026-10-28

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 520.9900 |
| Return 1D (%) | 2.7351 |
| Return 1W (%) | -1.9461 |
| Return 1M (%) | 0.6686 |
| Return YTD (%) | 8.4106 |
| Return 1Y (%) | 1.5950 |
| Annualized volatility (%) | 33.0238 |
| Beta vs SPY | 1.0065 |
| Max drawdown (%) | -31.3261 |
| Sharpe (rf=0) | 0.2101 |
| Downside deviation (rf=0, %) | 21.3409 |
| Sortino (rf=0) | 0.3251 |
| Historical VaR 95% (1D, %) | 2.7847 |
| Historical ES 95% (1D, %) | 4.0430 |
| Correlation vs SPY | 0.3901 |
| Tracking error vs SPY (%) | 30.4079 |
| P/E (trailing) | 26.47 |
| P/B | 8.22 |
| EV/EBITDA | 19.15 |
| Revenue growth (%) | 18.80 |
| Forward P/E (estimate) | 21.55 |
| Gross margin (%) | 67.66 |
| Operating margin (%) | 49.76 |
| Return on equity (%) | 34.22 |
| Free cash flow yield (%) | 0.08 |
| MA50 | 514.0618 |
| Close vs MA50 (%) | 1.3477 |
| MA200 | 437.4408 |
| Close vs MA200 (%) | 19.0995 |
| RSI (14, Wilder) | 49.4057 |
| MACD (12,26) | 2.1985 |
| MACD signal (9) | 5.3985 |
| MACD histogram | -3.2000 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MSFT': 274, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 520.9900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.7351 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.9461 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.6686 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 8.4106 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 1.5950 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.0238 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.3409 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3251 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.7847 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.0430 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3901 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.4079 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.0065 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -31.3261 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2101 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.5469 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 67.6570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 49.7570 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 34.2210 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.0774 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 26.4731 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 49.4057 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.2000 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.3477 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 19.0995 -> Clearly above the moving-average trend level.

## TAILWINDS

### Microsoft Stock (MSFT) Rises After The Elder Scrolls VI: Sentinel Reveal
- Summary: Microsoft Stock (MSFT) Rises After The Elder Scrolls VI: Sentinel Reveal
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQX1Fwbnp1SUUydjF2Mm5DS2w0dlB2R05fby16VC1Lc1V4YjBGT1czWmN2Q1NQVjdfUUNUbzRvelQxWEVWS2JOazNBOVk3UEdramtVWFg3d3dFbDZfQmRUSkF3NGdZR3JxMG9Ta05ZS3YxNVBUYTR0S1B1VnFYNDh3OGVuTjlsSF9TeEljNEYxbk9mS2h5eGVBWTZvQ2pVQW9y?oc=5>

### Microsoft stock jumps 4% as cloud growth drives earnings and revenue beat
- Summary: Microsoft stock jumps 4% as cloud growth drives earnings and revenue beat
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxNclpVVGdGd3NYYWo4bGNFRTVlYjhQc0VhMzhmZnRsRnlTNkRidVNwaGlQVVdPMktwMHRMYzhUTWpYUXFYaVFfZFRkSkRmbDNGOWxVa29MSWhhUDk4RE9BVElXUTY3SWo2SHRNbGVhRU9vbjd3ZHJnZlpTdHpSbHpDNNIBhgFBVV95cUxNRXA0VC1WZEYxMWVmenJmdVRiRzhDRFVzUVNVNlJXaEJDc011NjZuT2VHdTJLYndYaGV1NDM2UU93Zm12X1J2VWtYMEJNQ3ZkU0Nhb3M0c0dQT3pzVFl3eTlqLWluNHJjRHpVRTJicTdqSXNTSHBVQjdKWlJtYjZjN2tQZkc3dw?oc=5>

### Microsoft Just Revealed a $677 Billion Reason to Buy Its Stock
- Summary: Microsoft announces a $677B rationale for buying its shares, signaling strong confidence in future growth.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPRUJBeDZkZHk3ZlR5WXA2U2JGdS1nYnBfc0UwazNMaTlvWnRhLVY1dG9sVl9tZVBCZjFxbk1maTdaWk1GOG5OdnJBWWxDS3hMdVRzdTdJYUxyeXlWMmYyeGRjQlBVS25XZERVMC1MT3ZQVURXTkpzSmUtc3V1MVdnbWd4MGdDTnN0YXVZY0JoM0F2S2VIS3E1QmFyN1VBaXU5Tmc?oc=5>

### Microsoft Corp. (MSFT) Surges 37.8% on Record Quarterly Gains
- Summary: MSFT stock jumps 37.8% after reporting record quarterly earnings, boosting investor sentiment.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOQXo2dG9qMTRmU003ZF92OVVZQlpfU2JuS25fczJhUHpGWVFQNm1sQjYwSV9wd0IwNTBzZkZzdjVwNktPRkxNRGtlR3FGUFIya0hEenBBUHhHcy1JeFNWdUhmQjZFRExqcHZndzZzSDl0NXRBNUNwSUFhTi1DRTN5RTU1b0EtMS1YWjQ0NDM2bTd1dzlJVFV6VG5n?oc=5>

### Microsoft Corporation (MSFT) Delivers Strong Azure Growth as AI Demand Exceeds Supply
- Summary: Azure revenue surges due to high AI demand.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWVhoYmtlZjVaYkFjNy1oNkJqMDA1d1E0MGRCbjF4Sk5weHRGVDhHTFhubDJkMmpmOEFYTnJLZGp2Nmg0TXpiTDZtVk1hZXdiSEpaVUZUYnpvOFZPUUxLU28ydGpRMzlIeTJKNWFaVlVsbjk2N1YzTWl6bEdCMVNFUWR5U0l1RjgwTXgtenowT0o1dmlVcU8xTDlGS2tPeXpBSVFOdER0S1pfQQ?oc=5>

### Microsoft Corp.’s (MSFT) AI Advantage: Scale, Trust, and Economic Value
- Summary: Microsoft highlights AI strengths in scale and trust.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPR0hrdUNkMEMwbE5ibl80WlQxNHdWWHRxODdNYTBEbWNsOFRSVHpzWF9FdTVHbEtENWx5M2lsTDd6cER2MGlHLVhCUkV5cDhXS05uaHpSSVpHRHd0VDhDZFZWNUkyMnBXRU9JTE9iZUdpUG16dk0xN3ZGcllDUEgzcF9EanZ5X3RHVU1xWnc0OUtnZ2lTME1sUjV4RUo?oc=5>

### MSFT Stock Rebounds Above $520 as Microsoft's Anthropic Commitment Reaches $44.9 Billion
- Summary: Microsoft’s partnership with Anthropic boosts AI capabilities, driving stock rally above $520.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNUDBXaVRLeFd2U0FOYzd0OWRKNFQ3OUhkdU9sZTNqb1VvdU9PSmswVVVpN1pLcXEtSDNVSUt0NGIybG1hdkZ1UGI1QUJVT0kzaW8wQmlBcmJ6MTFrYi1UUHRTNzVDd2RXRFBHRHRhUndFcncyMkJaZG9laDNTTUVoWkRZcldfQjBxNlpfYmFiRXZEUVNhMUZLTHotbmh1eHlFVUMxYUQwY3ltYUJRZzkzdWhmSFBTUUpvMXZNMHRieDZ1VURNV2pZ?oc=5>

### Microsoft Corporation (MSFT) Is Betting Big on AI: Is Its Growth Story Just Getting Started?
- Summary: Microsoft is investing heavily in AI, signaling a potential acceleration of its growth trajectory.
- Date: 2026-11-03 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQcjZDbnhpSFhJeDNidjNPUlFXM2hKZk52ZGJHRjhublBjVWd2NWVlZ0ROV3ROOXJXajVYMHlrbnd4dXBtT2xRUlY2Qk9YMklpN053d3BQVVRjUmRhSUhvbFZtUnpfTjZqeTdmZ0FRR3p5LUFhUDJrUk04d1RVaXRIaURhRVhKb082aFhLdzNsQ3JDX1k2eXdRbXRTTWdHZk4wNlEyOQ?oc=5>

## HEADWINDS

### ETFs Are Net Sellers of Microsoft (MSFT) on Friday
- Summary: ETF net selling pressure may weigh on Microsoft’s share price.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNYm8zY3YyUVpsVDRVWFkycURXMUNXSFNoRzdkam5KNWtDWHVtbDM1V09SdThvOHJ2cTY0ZHZXUURKU280d3dkMUJPcWpIQlJ5Q1V1eEk2MTRZaWZpbmNkQ0ktcEljOWtQZktVajhqbHVSZWkyOE4xQ3R1Y0RjSkRtWkRxUWFUOFpTbTdUTXlxaEpGUEJFZGZ0SHpscGk?oc=5>

## CATALYSTS

### Microsoft Corporation (MSFT) Delivered Strong Fiscal Fourth-Quarter Results: Mott Capital’s Take
- Summary: Microsoft Corporation (MSFT) Delivered Strong Fiscal Fourth-Quarter Results: Mott Capital’s Take
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNQk9QazJNaHFhVHFmSzhPcUFMbHJzQk05dXV3ZXNwZ0xEM3JoazhBbktLS0I1RVpIckc1VnhQOEt4VzNOU3I3N1N2YVU2cW50S0RheWhNU3ZUNjJja0RXbkVuU2N1VThHM0tNX0hWemd3LXpGNjluODk2NzFnVV9jclAwNnhtTWxKeFhYcVRBcm11cWhVaUVWZWJnbXJVclAzQ1UtLU9KZzV4MUd5?oc=5>

### Microsoft Delivered a Beat on Both Earnings and Revenue. Here’s How to Think About MSFT Stock Now.
- Summary: Microsoft Delivered a Beat on Both Earnings and Revenue. Here’s How to Think About MSFT Stock Now.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQT1lkOTk4d0ZMa1ZYOTRrOHhNV0ZmNVJhZ0lOTGVnVTk5S2tYYkw0Y0wyX1lkRWtnVjREZ1pGVmM4bGRjZ292dGNjdzlYNEtEcVBzUGU5X2l2WFF3N2JEZFItZzdxVW9Bc0sycDcyY2swcHVkZ1M1cTBac2R6Nm5LdFpMUXFQYW5KQTduM1NMYkkyLW8yaUwwWWpKT3JUM21DZjYyZUh4X28xWjJCak1EdmJqMFFEQ0dzN2ZDN3hWZTZ3aXF0YmVBRjc2dmZTUVNEa3hiWlN3?oc=5>

### Microsoft (MSFT) Stock Gets Fair Value Bump On Azure And AI Optimism
- Summary: Microsoft (MSFT) Stock Gets Fair Value Bump On Azure And AI Optimism
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxNMVNHUmdfVEtaUVd0cG00UmVMSlFtSXJ6cTVVdEpPR0NYcmtvSzFLVEtEd28yREhYeTh0QXN3NGlJc0tlN0NwdUFBZEwzTE9vbnRVV2tpVmwza01XLVhwQU5uTzEtWGZPSVpNbTlTT01LS2tmRUQ1YllVNFQxcVB1bnhlMXUwQQ?oc=5>

### Microsoft (MSFT) Stock Shrugs Off Q1 Earnings As AI Spending Looms
- Summary: Microsoft (MSFT) Stock Shrugs Off Q1 Earnings As AI Spending Looms
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNcVl0VWhEWUhhTi1wb2pFS2EwdEhvem12dWtCNENMNGRhNjVCbkJ4OHJsLWgtaVRSa2xXcFFoQ1I0RzNLRVdUTmhjYVVkZDJQTmM3SUdZUk5jcWFxZjZfcnJrQnF4Qm5ickpyOU01QmJqMUNsQ2l4UjNmWU9BcDN3Nzk1NUVsTklzTmtUQnM4dTlFLVZEQzRpVkgtUWo?oc=5>

### Microsoft (MSFT) Lands $25 Billion Bond Deal As AI Push Deepens
- Summary: Microsoft (MSFT) Lands $25 Billion Bond Deal As AI Push Deepens
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPbHJpVVFoMThPSnp3Yi1DZFFZMi12UmtEUDR0Q2ZFVFhITFIxRm84UWpSallCak90Z0ZkczVrTzBhRlduclJMbm5GR3VUdTNNN1ZLWGpLUE5EN19oQl9EOGlaYjV0ckYtWC1hUHJKempYak1yaGR5ODF3TU5ELUdjNXlva05OWFl2LWplV1M4bWdDQnVrT251T3lkSQ?oc=5>

### What Could Surprise Microsoft Stock Investors On The Upside?
- Summary: Speculation about potential upside factors for MSFT investors, suggesting upcoming positive developments.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNY3E2YmVpd2JPblRCUFhZeWFLcDJsUTRDWXJtNnNCVFVoQnNsNEpfT2xLQi1rWnp3WUxVYV9mVC1BZS1fc2VzN1ExRnRGT0xTMHFiVkpYekZhZi11eEJUQjVlWkRGZmdkM0pBQW1MTWQwaDB5LUFUNE5SOXRCaWpWNU1RTkpzek95VllIXy1HVGdxM0pBRzJJdHQ4UXRndWdrWFlHbFRaQml6aTdyZnF1MjQ4M1VCS3dEUkw3RA?oc=5>

### Microsoft Beat Again. Its Stock Is Still Lower Than a Year Ago
- Summary: Microsoft reported earnings that beat expectations, though its stock remains below last year's level.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNb3RPR1ZNU25VcS1ad09XX1FlZnJrWENqMXcyNThFc3JkZVVfQmRGOWZ5QVNxMTNjdU9QOS0yQ0QtT2ZHMEloR0NUQmpuUGtCTENYTi1JaURIWjBjVWNhdGFtbUJRb0stRW5obEJ5aXpYN3ZadTlzM1hORGpta1hKeTJSRk9wcXo0X2IxeUlrMzRJMEUtWER2cTZsUGVvcE1TZE90aE9xb0U?oc=5>

### Microsoft’s AI Engine Is Becoming Even More Powerful (NASDAQ:MSFT)
- Summary: Microsoft announces enhancements to its AI engine, signaling stronger future offerings.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQcW8yclFmcV9EUWZFTGFtQTJJdzNFcE9wb1dIZndGTngzUjNwUGpEcnRaWENyR0JlQmRDa2xPY0JES2pXM1BocVl1T05oTWxCcjJKd3NrVWpUOTBHWnpwZF94UjRDOGE3QWJHc1E5OHNraFJ3eWFDY1o2ZGJGajhWSHY0endSYklFTEhURE5EWVI1ZW9YR1E?oc=5>

### Why Microsoft Was Rewarded for Spending Less on AI
- Summary: Microsoft's lower AI spend boosts investor confidence, leading to a 2% share price rise.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOWDlqbUhfUFZYakJrTWpkN1pxQlZ1eXN3N09keE1tVzdwNEg1RHRoakhsdmRmYVhiQmt1LXBVcy13V3JEYlY4XzBhOGlPM1JzTV9CVjU1NmdXQUp2aVNVRG9SVkJSd2lfZXg4b2RFTFI3d1hRSVZIUEtwSEJ1SHRZLVY1ZWxBeGkwWTBIN1pZU0VaZ1dwc3ZjakVB?oc=5>

## RISKS

### AI Bond Funding Might Change The Case For Investing In Microsoft (MSFT)
- Summary: AI bond funding could alter MSFT investment outlook.
- Date: 2026-11-02 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxORnhOQUtrTXZjTkcyUElCQ2VNeTQ3VzZ0SHhaRzRKOUdTTThnLUlwVGhxckVBUm5zdDBkTUdKNlFnaGZ1WXpqdUhQM2dxYjRWQUFqZEh0NEp2UEp4b19OZ1pJNXE1ay1GZTJ4NWc5N0o3RzRheFJKd016RXhxY1J0azdxUkxMZHdpLWFmUVBxblMyWlRoUUFXRA?oc=5>

### ETFs Are Net Sellers of Microsoft (MSFT) on Thursday
- Summary: Exchange-traded funds sold Microsoft shares, indicating a short-term sell pressure.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPVXlBRDVRWWpFT1JuRUkzSnlzSVZmUWpZUU9GWEVURGRZR3RxSnJsb196TlQzUkFFNEwxRFZlZThxNzRRR0VYejlqMzFyQmFfTGF5QWhNMkgtdUg2b0RxUTQ3amlMaDY0WEk3NXA1MFZiQzVrejAyREpjXzVvSkUzbjY4LUs0TGg1TkxfbWhvWVFOUUJrWEc0MEdaNDE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MSFT** | **26.47** | **8.22** | **19.15** | **18.80** | **3,868,973,072,384.00 USD** | **1.59** |
| ORCL | 18.69 | 6.17 | 15.07 | 29.60 | 382,545,133,568.00 USD | -50.41 |
| GOOGL | 14.57 | 5.22 | 18.04 | 24.70 | 3,442,688,655,360.00 USD | -1.04 |
| AMZN | 20.27 | 4.42 | 15.79 | 12.10 | 2,710,745,645,056.00 USD | -1.30 |

Peers fetched as_of: 2026-11-03; MSFT reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

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
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 19,953,000,000.00 USD; period 2010-10-01/2010-12-31; fiscal year/reporting period 2011/Q2
- Net income (latest available single quarter): 36,629,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMioAFBVV95cUxQX1Fwbnp1SUUydjF2Mm5DS2w0dlB2R05fby16VC1Lc1V4YjBGT1czWmN2Q1NQVjdfUUNUbzRvelQxWEVWS2JOazNBOVk3UEdramtVWFg3d3dFbDZfQmRUSkF3NGdZR3JxMG9Ta05ZS3YxNVBUYTR0S1B1VnFYNDh3OGVuTjlsSF9TeEljNEYxbk9mS2h5eGVBWTZvQ2pVQW9y?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxNclpVVGdGd3NYYWo4bGNFRTVlYjhQc0VhMzhmZnRsRnlTNkRidVNwaGlQVVdPMktwMHRMYzhUTWpYUXFYaVFfZFRkSkRmbDNGOWxVa29MSWhhUDk4RE9BVElXUTY3SWo2SHRNbGVhRU9vbjd3ZHJnZlpTdHpSbHpDNNIBhgFBVV95cUxNRXA0VC1WZEYxMWVmenJmdVRiRzhDRFVzUVNVNlJXaEJDc011NjZuT2VHdTJLYndYaGV1NDM2UU93Zm12X1J2VWtYMEJNQ3ZkU0Nhb3M0c0dQT3pzVFl3eTlqLWluNHJjRHpVRTJicTdqSXNTSHBVQjdKWlJtYjZjN2tQZkc3dw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPRUJBeDZkZHk3ZlR5WXA2U2JGdS1nYnBfc0UwazNMaTlvWnRhLVY1dG9sVl9tZVBCZjFxbk1maTdaWk1GOG5OdnJBWWxDS3hMdVRzdTdJYUxyeXlWMmYyeGRjQlBVS25XZERVMC1MT3ZQVURXTkpzSmUtc3V1MVdnbWd4MGdDTnN0YXVZY0JoM0F2S2VIS3E1QmFyN1VBaXU5Tmc?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOQXo2dG9qMTRmU003ZF92OVVZQlpfU2JuS25fczJhUHpGWVFQNm1sQjYwSV9wd0IwNTBzZkZzdjVwNktPRkxNRGtlR3FGUFIya0hEenBBUHhHcy1JeFNWdUhmQjZFRExqcHZndzZzSDl0NXRBNUNwSUFhTi1DRTN5RTU1b0EtMS1YWjQ0NDM2bTd1dzlJVFV6VG5n?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWVhoYmtlZjVaYkFjNy1oNkJqMDA1d1E0MGRCbjF4Sk5weHRGVDhHTFhubDJkMmpmOEFYTnJLZGp2Nmg0TXpiTDZtVk1hZXdiSEpaVUZUYnpvOFZPUUxLU28ydGpRMzlIeTJKNWFaVlVsbjk2N1YzTWl6bEdCMVNFUWR5U0l1RjgwTXgtenowT0o1dmlVcU8xTDlGS2tPeXpBSVFOdER0S1pfQQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPR0hrdUNkMEMwbE5ibl80WlQxNHdWWHRxODdNYTBEbWNsOFRSVHpzWF9FdTVHbEtENWx5M2lsTDd6cER2MGlHLVhCUkV5cDhXS05uaHpSSVpHRHd0VDhDZFZWNUkyMnBXRU9JTE9iZUdpUG16dk0xN3ZGcllDUEgzcF9EanZ5X3RHVU1xWnc0OUtnZ2lTME1sUjV4RUo?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNUDBXaVRLeFd2U0FOYzd0OWRKNFQ3OUhkdU9sZTNqb1VvdU9PSmswVVVpN1pLcXEtSDNVSUt0NGIybG1hdkZ1UGI1QUJVT0kzaW8wQmlBcmJ6MTFrYi1UUHRTNzVDd2RXRFBHRHRhUndFcncyMkJaZG9laDNTTUVoWkRZcldfQjBxNlpfYmFiRXZEUVNhMUZLTHotbmh1eHlFVUMxYUQwY3ltYUJRZzkzdWhmSFBTUUpvMXZNMHRieDZ1VURNV2pZ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQcjZDbnhpSFhJeDNidjNPUlFXM2hKZk52ZGJHRjhublBjVWd2NWVlZ0ROV3ROOXJXajVYMHlrbnd4dXBtT2xRUlY2Qk9YMklpN053d3BQVVRjUmRhSUhvbFZtUnpfTjZqeTdmZ0FRR3p5LUFhUDJrUk04d1RVaXRIaURhRVhKb082aFhLdzNsQ3JDX1k2eXdRbXRTTWdHZk4wNlEyOQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNYm8zY3YyUVpsVDRVWFkycURXMUNXSFNoRzdkam5KNWtDWHVtbDM1V09SdThvOHJ2cTY0ZHZXUURKU280d3dkMUJPcWpIQlJ5Q1V1eEk2MTRZaWZpbmNkQ0ktcEljOWtQZktVajhqbHVSZWkyOE4xQ3R1Y0RjSkRtWkRxUWFUOFpTbTdUTXlxaEpGUEJFZGZ0SHpscGk?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNQk9QazJNaHFhVHFmSzhPcUFMbHJzQk05dXV3ZXNwZ0xEM3JoazhBbktLS0I1RVpIckc1VnhQOEt4VzNOU3I3N1N2YVU2cW50S0RheWhNU3ZUNjJja0RXbkVuU2N1VThHM0tNX0hWemd3LXpGNjluODk2NzFnVV9jclAwNnhtTWxKeFhYcVRBcm11cWhVaUVWZWJnbXJVclAzQ1UtLU9KZzV4MUd5?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQT1lkOTk4d0ZMa1ZYOTRrOHhNV0ZmNVJhZ0lOTGVnVTk5S2tYYkw0Y0wyX1lkRWtnVjREZ1pGVmM4bGRjZ292dGNjdzlYNEtEcVBzUGU5X2l2WFF3N2JEZFItZzdxVW9Bc0sycDcyY2swcHVkZ1M1cTBac2R6Nm5LdFpMUXFQYW5KQTduM1NMYkkyLW8yaUwwWWpKT3JUM21DZjYyZUh4X28xWjJCak1EdmJqMFFEQ0dzN2ZDN3hWZTZ3aXF0YmVBRjc2dmZTUVNEa3hiWlN3?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxNMVNHUmdfVEtaUVd0cG00UmVMSlFtSXJ6cTVVdEpPR0NYcmtvSzFLVEtEd28yREhYeTh0QXN3NGlJc0tlN0NwdUFBZEwzTE9vbnRVV2tpVmwza01XLVhwQU5uTzEtWGZPSVpNbTlTT01LS2tmRUQ1YllVNFQxcVB1bnhlMXUwQQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNcVl0VWhEWUhhTi1wb2pFS2EwdEhvem12dWtCNENMNGRhNjVCbkJ4OHJsLWgtaVRSa2xXcFFoQ1I0RzNLRVdUTmhjYVVkZDJQTmM3SUdZUk5jcWFxZjZfcnJrQnF4Qm5ickpyOU01QmJqMUNsQ2l4UjNmWU9BcDN3Nzk1NUVsTklzTmtUQnM4dTlFLVZEQzRpVkgtUWo?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPbHJpVVFoMThPSnp3Yi1DZFFZMi12UmtEUDR0Q2ZFVFhITFIxRm84UWpSallCak90Z0ZkczVrTzBhRlduclJMbm5GR3VUdTNNN1ZLWGpLUE5EN19oQl9EOGlaYjV0ckYtWC1hUHJKempYak1yaGR5ODF3TU5ELUdjNXlva05OWFl2LWplV1M4bWdDQnVrT251T3lkSQ?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNY3E2YmVpd2JPblRCUFhZeWFLcDJsUTRDWXJtNnNCVFVoQnNsNEpfT2xLQi1rWnp3WUxVYV9mVC1BZS1fc2VzN1ExRnRGT0xTMHFiVkpYekZhZi11eEJUQjVlWkRGZmdkM0pBQW1MTWQwaDB5LUFUNE5SOXRCaWpWNU1RTkpzek95VllIXy1HVGdxM0pBRzJJdHQ4UXRndWdrWFlHbFRaQml6aTdyZnF1MjQ4M1VCS3dEUkw3RA?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNb3RPR1ZNU25VcS1ad09XX1FlZnJrWENqMXcyNThFc3JkZVVfQmRGOWZ5QVNxMTNjdU9QOS0yQ0QtT2ZHMEloR0NUQmpuUGtCTENYTi1JaURIWjBjVWNhdGFtbUJRb0stRW5obEJ5aXpYN3ZadTlzM1hORGpta1hKeTJSRk9wcXo0X2IxeUlrMzRJMEUtWER2cTZsUGVvcE1TZE90aE9xb0U?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQcW8yclFmcV9EUWZFTGFtQTJJdzNFcE9wb1dIZndGTngzUjNwUGpEcnRaWENyR0JlQmRDa2xPY0JES2pXM1BocVl1T05oTWxCcjJKd3NrVWpUOTBHWnpwZF94UjRDOGE3QWJHc1E5OHNraFJ3eWFDY1o2ZGJGajhWSHY0endSYklFTEhURE5EWVI1ZW9YR1E?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOWDlqbUhfUFZYakJrTWpkN1pxQlZ1eXN3N09keE1tVzdwNEg1RHRoakhsdmRmYVhiQmt1LXBVcy13V3JEYlY4XzBhOGlPM1JzTV9CVjU1NmdXQUp2aVNVRG9SVkJSd2lfZXg4b2RFTFI3d1hRSVZIUEtwSEJ1SHRZLVY1ZWxBeGkwWTBIN1pZU0VaZ1dwc3ZjakVB?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxORnhOQUtrTXZjTkcyUElCQ2VNeTQ3VzZ0SHhaRzRKOUdTTThnLUlwVGhxckVBUm5zdDBkTUdKNlFnaGZ1WXpqdUhQM2dxYjRWQUFqZEh0NEp2UEp4b19OZ1pJNXE1ay1GZTJ4NWc5N0o3RzRheFJKd016RXhxY1J0azdxUkxMZHdpLWFmUVBxblMyWlRoUUFXRA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPVXlBRDVRWWpFT1JuRUkzSnlzSVZmUWpZUU9GWEVURGRZR3RxSnJsb196TlQzUkFFNEwxRFZlZThxNzRRR0VYejlqMzFyQmFfTGF5QWhNMkgtdUg2b0RxUTQ3amlMaDY0WEk3NXA1MFZiQzVrejAyREpjXzVvSkUzbjY4LUs0TGg1TkxfbWhvWVFOUUJrWEc0MEdaNDE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
