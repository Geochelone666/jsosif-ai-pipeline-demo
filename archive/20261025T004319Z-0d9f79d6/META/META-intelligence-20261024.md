# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-10-24**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-10-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-25T01:14:27.024640+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 11, 'ai': 10, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 14 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 642.6200 |
| Return 1D (%) | -0.9602 |
| Return 1W (%) | -9.4047 |
| Return 1M (%) | -13.6379 |
| Return YTD (%) | -2.3960 |
| Return 1Y (%) | -12.1526 |
| Annualized volatility (%) | 42.6923 |
| Beta vs SPY | 1.5234 |
| Max drawdown (%) | -29.9428 |
| Sharpe (rf=0) | -0.0922 |
| Downside deviation (rf=0, %) | 29.6300 |
| Sortino (rf=0) | -0.1329 |
| Historical VaR 95% (1D, %) | 3.7761 |
| Historical ES 95% (1D, %) | 6.2110 |
| Correlation vs SPY | 0.4548 |
| Tracking error vs SPY (%) | 38.6015 |
| P/E (trailing) | 21.92 |
| P/B | 6.03 |
| EV/EBITDA | 14.42 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 18.46 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 35.41 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.03 |
| MA50 | 663.5767 |
| Close vs MA50 (%) | -3.1581 |
| MA200 | 631.6592 |
| Close vs MA200 (%) | 1.7352 |
| RSI (14, Wilder) | 35.7569 |
| MACD (12,26) | -1.9079 |
| MACD signal (9) | 12.3755 |
| MACD histogram | -14.2833 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 642.6200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.9602 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -9.4047 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -13.6379 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -2.3960 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -12.1526 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 42.6923 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.6300 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.1329 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7761 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.2110 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4548 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 38.6015 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.5234 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -29.9428 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0922 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.4551 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 35.4140 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0292 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.9249 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 35.7569 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -14.2833 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.1581 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.7352 -> Slightly above the moving-average trend level.

## TAILWINDS

### Meta Stock (META) Rises Despite Mixed Financial Results
- Summary: Meta Stock (META) Rises Despite Mixed Financial Results
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQckNFQzdOU0xDQzRpQ3NaV2NZc0oyck5QUGF3NG5UQklnSGtOUmtUWGNpZncwWjRiTGI0eDQ3N0o4VFZpLUJUM3RMeFg4S0J5SjA2aHZEMlNObi1MTUdXNFJ4Y1lSSExBM3l6WV9FZGp6NUZwQklRRC0yYXBSNlV0NExya3AzU29ROVlv?oc=5>

### Meta stock falls despite Wall Street analysts raising price targets
- Summary: Meta stock falls despite Wall Street analysts raising price targets
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxObmx1a1A0RHVlYk5INVRpT0VfUnlMNEdwZ2VUbmtYV3VCMjlYd2h4X3pMUkJEMjN5TGpPSTlHNXFoVDdVUjZOT1V0MGpieWpJbThlVi01MmxjZUxKMzVOaGw1bVNoTEpRa2h4cnNyYThZYTRfajRSUVlpcHBIMktoZzNLWWFoVHFWQzNieW00UWxRTU1xRXRoR3h3?oc=5>

### Meta Stock Is Up 9% This Year. Is It Still a Buy Ahead of Earnings?
- Summary: Meta Stock Is Up 9% This Year. Is It Still a Buy Ahead of Earnings?
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOYW53T09LUW5JZFlzME14aTZUTTJoa2w1LWJrYUpZZHhBVmhTTjBFYjBFcDNZZldOZE94cE00VVRZS0lCeW9ld21lbUwxRFc1QllETDFJdUZHamx6VVNXY3NWYjZjeUFqaGl5QTZKVF9JNF9KV1Bpd0pGa0JmWkRzTnQ5T3VETnE1WE9sVUZJYXBwUk53N09WRUdR?oc=5>

## HEADWINDS

### Meta stock closes out Friday down as AI spending fears continue to rattle markets
- Summary: Meta stock closes out Friday down as AI spending fears continue to rattle markets
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOVBsWC1HZmNiRnJHT3RIbzlmcmZLZVpRVVlibk5sMFhyLUJfSHVtZlhxNzBLWkJ6RkgtWWprZnl2ZUVCeVBzb3NOVzlJQkYwbjBvVzQtaFZDSk9rZGxlYWVjMEJnWFY0LVFiUVM0S2J1T0ExVTJMcFY4QjJ1ZDgwNVVrVEpENFpJMHVrRkpoVXJvSTktOE9fMU94dnpLR1UxWWlSTFVHallWRG1DTDBhNXJobzJpek5UeTk3dUFRZl9QMnJhaGo1OXo3TUhSeEg0LTVQeHZiZ0NuZw?oc=5>

### Meta shares slide, default insurance hits record as AI spending alarms investors
- Summary: Meta shares slide, default insurance hits record as AI spending alarms investors
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQdnFibXQ2bEZfUWFpTEoxYTNPQ3dHTlMwMjZRaFcxZlphTlplUlNFWkgta2xwdVBvU0l5OWNkMEctQmNrM2s1UDRpSW5jNFhpLW9TQUlzYlpmZFZudjhvM0RtcC1hQ24xSmVOMDYwbUIzNDQ3NlAwTEpILTc4akh1czlRcThIUnU3Y2VkbWJJWE9jdXJzbWtzclVfeUh5RzN6UzdaTlZjRWlMQQ?oc=5>

### META Stock Slips As Legal And AI Spending Risks Mount
- Summary: META Stock Slips As Legal And AI Spending Risks Mount
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMie0FVX3lxTE5rX3l2N3JWRW15VUNrLVZJdmxtYWxodHBMNE5ZWUl2QXl3aUxlNElON0FQYXdWNEF1ZG1acnZHOW82VnlzZDZjeDBXOHRxMEt4T2laeGpaYWZLT3A0N3EwbXp5TVRQeFZncUJiSnpXNFpidnFFUV95NzROTQ?oc=5>

### META Stock Set To Record Worst Day In Nearly Three Months As Investors Fret Over Negative Cash Flows Amid Raised Capex Floor
- Summary: META Stock Set To Record Worst Day In Nearly Three Months As Investors Fret Over Negative Cash Flows Amid Raised Capex Floor
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPOWVFcXJuaU5SQ1M2ZmRqWUQxU3k0QlZkQ01zUTBtNmxub0pGeE80UzFmVW1CQ3FvRHFXY0dxaXd6Rmp1b1lFNl80ZjQ5ay1Va0t2bGNDQ2ktLVgxTGxHc0hBSExGbnIzRjZxSnRIUGtuaVR1WFhJekNHbmt4UlctcDY5WVJNS2xzeDNpODA3UGNINkpxN0N3?oc=5>

### Meta Stock Falls Despite Strong Q3 Results As AI Spending Takes Focus
- Summary: Meta Stock Falls Despite Strong Q3 Results As AI Spending Takes Focus
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiekFVX3lxTE13Wjk2WUxJQlotZzhWT0kycHlpRU5wQVpBVVpuZDJQQ1hKWG9zeVJLQUZnbTZrTzRKNFJLdV9Sa3NWZ0RPN1VhaEp0ODBsRnYxV3BJQy14b0VKN2lheXA5WHZteVZnSEhtc1dOS3dVbDF0UzdYUHQ2QzFn?oc=5>

### Meta Stock Falls. Earnings Show Just How Much Future Growth Will Cost.
- Summary: Meta Stock Falls. Earnings Show Just How Much Future Growth Will Cost.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE4tdTM5U2kwQ295eEpWaTdjamk4SDdmT09TWjFBNHBhZkRxcmR6SmpNT1lEbTZGZTl0LVZpYUxXUERlOEtsaWdFLXF2QTFSUG9LM0RjbkZyR21YR1dlNmN2NnhvTWFqanY4Q09IYjBqT29SOHBGeWxrZg?oc=5>

### Why Meta Platforms Stock Took a Hit Today
- Summary: Meta shares fell sharply today, reflecting market concerns over recent performance.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNSHVCSkdkWmRnY0NkYjVuLWlNbEdZY2VodlBNWlFUd1ZKd255a2lLemlEMjR0MjdCVi1lYjl2NlF4c2dqUTFVeWNPRzVuX2U3cnp5UGFnelFUVURTT0M0Umk2UzJsQjZYSXlzV3BxZ2Y1YUhtdjdGVmUxcklWbUNXNFAxaEFDOXFBSkVaTA?oc=5>

### Meta Platforms, Inc. $META Stock Holdings Trimmed by Baskin Financial Services Inc.
- Summary: Baskin Financial trimmed its Meta holdings, indicating a negative outlook for the stock.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxNcTVfaFhsUk5HeW51Qk9wYzNxdE5qLXkxNW4yZHZ1SHM2S25OWFFBeEVwNHNBNTk4RFBmalFnVVNfeVA2c3JfbTR5UWV5TmlqWXpvOFJMNDNZeENVTnN2Z3ZockJjdkREV1hhdEM3TTlKZjY2dEZVa3QzWHdNZk9EZzZpd3JZZGR6RDJoS2xMZmxjd3VoLVp2YzExYVFQdy16Wm5vUzlqeUhMRG9OdWRJLW10cWN4ektQVFhueURPNmZOTkNQb1ZoQjkxVGMwR29YLUVHNVFHbw?oc=5>

### Why Meta (META) shares are getting obliterated today
- Summary: Meta shares experienced a significant decline, suggesting strong negative market sentiment.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNR0E3WDFFeXVId3dtV3I1N3BGVEdoSlJ4TUxVZzhVd3ctRjMyX1ZwU2VhaklwOVA4eldpdmVpb1d5amdOMGR2d1IwYkFiMF9jVzZaa0RQendlYldjRldVckdlWVRveWl1WTFUcXQ4TW11NllKQlMyR0FQTXVEQ3RxdHhqMlpYaEJTQnR4V3I2NG5JOFB5RWpNMg?oc=5>

## CATALYSTS

### META Stock Alert: What to Know as Meta Platforms Announces Stock Split
- Summary: META Stock Alert: What to Know as Meta Platforms Announces Stock Split
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQTGlmNFp2OWRxcWh1dFVIUTZPdk1iZlpxbXhELXlNR0VJTG5IejRpRFhuaWg4dDRIMk5wQkVlQi1LcE1lNWlUWGdNeXR0dVR6NlFmX0cxUk51d3BqNE1MN0JkMXF0UTIzLXd4aEh3VTVfVWJCaDRXcWhoeUMwdXI1bFUzejRFNkc1dER5NV9kUjlHejBXZW5JVEVJb0h1S2xDcC1aNTJNUUZFdko4aFc2cjd2QQ?oc=5>

### Meta’s Stock Split Paves Way for Huge AI Financing Deal
- Summary: Meta’s Stock Split Paves Way for Huge AI Financing Deal
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxQclVZYi1ZSWIzcjFXUVdfWTUzVVh0eUtRRkxmVllWNm1yYzA1Q2s3dVZmVTdPZDlsNjlSR2pfdnpBMkRoZ0Q2UTU4M1ZPajNuekxVZV9tX3dyXzFLNWZ1THFHQmNPZUxiSHNFVkNrRkVMdXhla0hHSVpabEloYndobUp5bFlmN2M?oc=5>

### Meta Will Split Stock, Create New Class to Fund AI Spending
- Summary: Meta announces a stock split to create a new class aimed at funding AI initiatives.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxOY20xcVZmaDh6bkhCTVVoQVJIOFhWZU1McXpENHNVTEdvMVY0YUQyUVdqOFBldFhJU1VXZ3lIY3FOSDN0ZFdBbXJDOXluVlA2WU9mcUJfM3FrVkQ1YXJBcDNSbXM0RlVib19UMFlsTFBBeFIyVGlEdUxVZS0wRDhWWl81ZjVXU0ZlQjJPeFRTaw?oc=5>

### Meta, AI Stocks Tumble As AI Spending Fears Reignite
- Summary: Meta shares fall amid renewed concerns over AI spending, affecting broader AI sector stocks.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQajBLQkZtRlFleDRoUmFKTDllbzhqMEpfd1hIOHdKeXdlVVFiU0VtS1JvUUxDR1hILWV1VnF5NzdLMkhZOVAyUy00VW92aVhpcHFtWWNRU1FwZ0wxNGp4LTNFazBkY3dPZmVJejNNT2FfaE05TWZOaWlCZW1Ja2dHMXVTUERvVEhhaVZ4Vg?oc=5>

### How Meta Stock Can Be Both the ‘Cleanest’ AI Winner and a Risky Play
- Summary: Analysts weigh Meta’s AI potential against associated risks, offering a balanced view.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE5DajFQVmM2bGkwbGwwRVdiS1JIZEcwdE52SkRyMTZLWnVOWUdjMWdaaVViZC14WXpqQTVXSmlPSFJkWHk5eDBLTk9YQlNuSHI3NC1uaTRGaDFPX3dEVDJwNUV2NXdvMnBCQngxZnZ3NHFYQ3ptdWxMSE5CeFZyUQ?oc=5>

### Bank of America revamps Meta stock price target once again
- Summary: Bank of America updates its price target for Meta, reflecting new outlooks.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPZ3Y4UTVnSVh3bGc5c1FkNUwwc1ZibllGZklVLXFrVDd6Q1RUVVRqNk9pb1RKTVFQaDNMeXpPMTYzek56MFpwbi1sVWlEMkR0akVWcFAxcWVKSk5oeVlaVzlXNlNqZGZiNzdteHhQOHRxOURDMkNjWmJ4UzlEUEpyeTR6NWhxdkZENmxVeHVjYVlaejhIdGhKR2hiRjdNNTIyOTk4?oc=5>

### Meta is splitting its stock: Here’s why, when, and what it means for investors
- Summary: Meta details the rationale, timing, and implications of its upcoming stock split.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQTUJJdlJ1REVnTV9ZVHFOaVhHQVplRG9jLVRpY2hfUDRuVFRFd0xpQWxHbDdaam5nNi1NTTBEckpOb3l0MjFuUE1EbEFWN0Fxam0xenFLV2VkQkZxUnNCZ3hqUHd2RE9mVVB5cXduNTBNTFZ4Sk5nQ25aRnlTV3Npb1dwSXpXMThnUG1JeU5lU2tWWGZ4?oc=5>

### Here’s How Much Meta Stock Is Expected to Move After Earnings
- Summary: Analysts predict moderate movement in Meta shares following earnings release.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNNDlGN05oelNLdkV4ZXJWRFVsZl80RDlnVFBhY044cjFTNEc5a3ZoU2NVeFdmejZYQTlZMXFQdm9POU5mcFlEcmhCLVhFZ2NDN3dFM1hrU2Zmdm42NlVGNTZWTE95YnF0ZlBjSzMyM2FqelpxR0ljMXZHYjF4THRCcEMwaTNDRUpvdlR2UndBanpMa0dVSGtTaWZWUFJVNEpCQ1NhLWdNaTR3SGpLNlBpZVdzb0UxVWdy?oc=5>

### Meta puts Muse agent at heart of AI strategy, plans new stock to power investments
- Summary: Meta focuses on Muse agent for AI, launching new stock to fund investments.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPRFFieGdGQjNVTEpWeTlmUG5ZOW5rRjgwSmpnV1RWdTUzRG5fZW1BQmxBdElRdEtfOVYzcWlaMjR1SGJqZWdPR200RzJuV2JZajJMYmhiSmh4VFdYVjdLQXNxRWo1ZEprRWpKQW1vQkhoMm5jT1RKNzJVczV4aUxHdDNWQ0JoSXVOYzN0WDhFMmh4cjg5RWNmZFhtaHlQTlJ0NmVnRlNpQjg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **21.92** | **6.03** | **14.42** | **26.10** | **1,637,078,401,024.00 USD** | **-12.15** |
| GOOGL | 16.07 | 6.29 | 22.02 | 24.20 | 3,916,147,458,048.00 USD | 26.85 |
| SNAP | N/A | 5.53 | -84.00 | 18.90 | 10,722,193,408.00 USD | -19.44 |
| PINS | 65.65 | 4.36 | 39.68 | 18.20 | 12,640,106,496.00 USD | -33.27 |

Peers fetched as_of: 2026-10-24; META reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-22
- Revenue (latest available single quarter): 13,727,000,000.00 USD; period 2018-07-01/2018-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 9,860,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQckNFQzdOU0xDQzRpQ3NaV2NZc0oyck5QUGF3NG5UQklnSGtOUmtUWGNpZncwWjRiTGI0eDQ3N0o4VFZpLUJUM3RMeFg4S0J5SjA2aHZEMlNObi1MTUdXNFJ4Y1lSSExBM3l6WV9FZGp6NUZwQklRRC0yYXBSNlV0NExya3AzU29ROVlv?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxObmx1a1A0RHVlYk5INVRpT0VfUnlMNEdwZ2VUbmtYV3VCMjlYd2h4X3pMUkJEMjN5TGpPSTlHNXFoVDdVUjZOT1V0MGpieWpJbThlVi01MmxjZUxKMzVOaGw1bVNoTEpRa2h4cnNyYThZYTRfajRSUVlpcHBIMktoZzNLWWFoVHFWQzNieW00UWxRTU1xRXRoR3h3?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOYW53T09LUW5JZFlzME14aTZUTTJoa2w1LWJrYUpZZHhBVmhTTjBFYjBFcDNZZldOZE94cE00VVRZS0lCeW9ld21lbUwxRFc1QllETDFJdUZHamx6VVNXY3NWYjZjeUFqaGl5QTZKVF9JNF9KV1Bpd0pGa0JmWkRzTnQ5T3VETnE1WE9sVUZJYXBwUk53N09WRUdR?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOVBsWC1HZmNiRnJHT3RIbzlmcmZLZVpRVVlibk5sMFhyLUJfSHVtZlhxNzBLWkJ6RkgtWWprZnl2ZUVCeVBzb3NOVzlJQkYwbjBvVzQtaFZDSk9rZGxlYWVjMEJnWFY0LVFiUVM0S2J1T0ExVTJMcFY4QjJ1ZDgwNVVrVEpENFpJMHVrRkpoVXJvSTktOE9fMU94dnpLR1UxWWlSTFVHallWRG1DTDBhNXJobzJpek5UeTk3dUFRZl9QMnJhaGo1OXo3TUhSeEg0LTVQeHZiZ0NuZw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQdnFibXQ2bEZfUWFpTEoxYTNPQ3dHTlMwMjZRaFcxZlphTlplUlNFWkgta2xwdVBvU0l5OWNkMEctQmNrM2s1UDRpSW5jNFhpLW9TQUlzYlpmZFZudjhvM0RtcC1hQ24xSmVOMDYwbUIzNDQ3NlAwTEpILTc4akh1czlRcThIUnU3Y2VkbWJJWE9jdXJzbWtzclVfeUh5RzN6UzdaTlZjRWlMQQ?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTE5rX3l2N3JWRW15VUNrLVZJdmxtYWxodHBMNE5ZWUl2QXl3aUxlNElON0FQYXdWNEF1ZG1acnZHOW82VnlzZDZjeDBXOHRxMEt4T2laeGpaYWZLT3A0N3EwbXp5TVRQeFZncUJiSnpXNFpidnFFUV95NzROTQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPOWVFcXJuaU5SQ1M2ZmRqWUQxU3k0QlZkQ01zUTBtNmxub0pGeE80UzFmVW1CQ3FvRHFXY0dxaXd6Rmp1b1lFNl80ZjQ5ay1Va0t2bGNDQ2ktLVgxTGxHc0hBSExGbnIzRjZxSnRIUGtuaVR1WFhJekNHbmt4UlctcDY5WVJNS2xzeDNpODA3UGNINkpxN0N3?oc=5
- https://news.google.com/rss/articles/CBMiekFVX3lxTE13Wjk2WUxJQlotZzhWT0kycHlpRU5wQVpBVVpuZDJQQ1hKWG9zeVJLQUZnbTZrTzRKNFJLdV9Sa3NWZ0RPN1VhaEp0ODBsRnYxV3BJQy14b0VKN2lheXA5WHZteVZnSEhtc1dOS3dVbDF0UzdYUHQ2QzFn?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTE4tdTM5U2kwQ295eEpWaTdjamk4SDdmT09TWjFBNHBhZkRxcmR6SmpNT1lEbTZGZTl0LVZpYUxXUERlOEtsaWdFLXF2QTFSUG9LM0RjbkZyR21YR1dlNmN2NnhvTWFqanY4Q09IYjBqT29SOHBGeWxrZg?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNSHVCSkdkWmRnY0NkYjVuLWlNbEdZY2VodlBNWlFUd1ZKd255a2lLemlEMjR0MjdCVi1lYjl2NlF4c2dqUTFVeWNPRzVuX2U3cnp5UGFnelFUVURTT0M0Umk2UzJsQjZYSXlzV3BxZ2Y1YUhtdjdGVmUxcklWbUNXNFAxaEFDOXFBSkVaTA?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNNVBQMTBnV2UxVENmTm5GN2wtTFVRYmE0NHFLRGhMcGYxRWlnSHdMQ2hOT3BFdTlpaklWem9oMHFTTkEyVVhhSzBMU1pzc2xKS3ZGRjR3c0hCeTZwSUF4eHR6Z25hR0FiVUd4Q3VMVTlUZnhhcE1sUGVqYUJTX0p2cFNQbGRnMkFGZUpKRlItNjJhRENzQU4xaEln?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxNcTVfaFhsUk5HeW51Qk9wYzNxdE5qLXkxNW4yZHZ1SHM2S25OWFFBeEVwNHNBNTk4RFBmalFnVVNfeVA2c3JfbTR5UWV5TmlqWXpvOFJMNDNZeENVTnN2Z3ZockJjdkREV1hhdEM3TTlKZjY2dEZVa3QzWHdNZk9EZzZpd3JZZGR6RDJoS2xMZmxjd3VoLVp2YzExYVFQdy16Wm5vUzlqeUhMRG9OdWRJLW10cWN4ektQVFhueURPNmZOTkNQb1ZoQjkxVGMwR29YLUVHNVFHbw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNR0E3WDFFeXVId3dtV3I1N3BGVEdoSlJ4TUxVZzhVd3ctRjMyX1ZwU2VhaklwOVA4eldpdmVpb1d5amdOMGR2d1IwYkFiMF9jVzZaa0RQendlYldjRldVckdlWVRveWl1WTFUcXQ4TW11NllKQlMyR0FQTXVEQ3RxdHhqMlpYaEJTQnR4V3I2NG5JOFB5RWpNMg?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQTGlmNFp2OWRxcWh1dFVIUTZPdk1iZlpxbXhELXlNR0VJTG5IejRpRFhuaWg4dDRIMk5wQkVlQi1LcE1lNWlUWGdNeXR0dVR6NlFmX0cxUk51d3BqNE1MN0JkMXF0UTIzLXd4aEh3VTVfVWJCaDRXcWhoeUMwdXI1bFUzejRFNkc1dER5NV9kUjlHejBXZW5JVEVJb0h1S2xDcC1aNTJNUUZFdko4aFc2cjd2QQ?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxQclVZYi1ZSWIzcjFXUVdfWTUzVVh0eUtRRkxmVllWNm1yYzA1Q2s3dVZmVTdPZDlsNjlSR2pfdnpBMkRoZ0Q2UTU4M1ZPajNuekxVZV9tX3dyXzFLNWZ1THFHQmNPZUxiSHNFVkNrRkVMdXhla0hHSVpabEloYndobUp5bFlmN2M?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxOY20xcVZmaDh6bkhCTVVoQVJIOFhWZU1McXpENHNVTEdvMVY0YUQyUVdqOFBldFhJU1VXZ3lIY3FOSDN0ZFdBbXJDOXluVlA2WU9mcUJfM3FrVkQ1YXJBcDNSbXM0RlVib19UMFlsTFBBeFIyVGlEdUxVZS0wRDhWWl81ZjVXU0ZlQjJPeFRTaw?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQajBLQkZtRlFleDRoUmFKTDllbzhqMEpfd1hIOHdKeXdlVVFiU0VtS1JvUUxDR1hILWV1VnF5NzdLMkhZOVAyUy00VW92aVhpcHFtWWNRU1FwZ0wxNGp4LTNFazBkY3dPZmVJejNNT2FfaE05TWZOaWlCZW1Ja2dHMXVTUERvVEhhaVZ4Vg?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE5DajFQVmM2bGkwbGwwRVdiS1JIZEcwdE52SkRyMTZLWnVOWUdjMWdaaVViZC14WXpqQTVXSmlPSFJkWHk5eDBLTk9YQlNuSHI3NC1uaTRGaDFPX3dEVDJwNUV2NXdvMnBCQngxZnZ3NHFYQ3ptdWxMSE5CeFZyUQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPZ3Y4UTVnSVh3bGc5c1FkNUwwc1ZibllGZklVLXFrVDd6Q1RUVVRqNk9pb1RKTVFQaDNMeXpPMTYzek56MFpwbi1sVWlEMkR0akVWcFAxcWVKSk5oeVlaVzlXNlNqZGZiNzdteHhQOHRxOURDMkNjWmJ4UzlEUEpyeTR6NWhxdkZENmxVeHVjYVlaejhIdGhKR2hiRjdNNTIyOTk4?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQTUJJdlJ1REVnTV9ZVHFOaVhHQVplRG9jLVRpY2hfUDRuVFRFd0xpQWxHbDdaam5nNi1NTTBEckpOb3l0MjFuUE1EbEFWN0Fxam0xenFLV2VkQkZxUnNCZ3hqUHd2RE9mVVB5cXduNTBNTFZ4Sk5nQ25aRnlTV3Npb1dwSXpXMThnUG1JeU5lU2tWWGZ4?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNNDlGN05oelNLdkV4ZXJWRFVsZl80RDlnVFBhY044cjFTNEc5a3ZoU2NVeFdmejZYQTlZMXFQdm9POU5mcFlEcmhCLVhFZ2NDN3dFM1hrU2Zmdm42NlVGNTZWTE95YnF0ZlBjSzMyM2FqelpxR0ljMXZHYjF4THRCcEMwaTNDRUpvdlR2UndBanpMa0dVSGtTaWZWUFJVNEpCQ1NhLWdNaTR3SGpLNlBpZVdzb0UxVWdy?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPRFFieGdGQjNVTEpWeTlmUG5ZOW5rRjgwSmpnV1RWdTUzRG5fZW1BQmxBdElRdEtfOVYzcWlaMjR1SGJqZWdPR200RzJuV2JZajJMYmhiSmh4VFdYVjdLQXNxRWo1ZEprRWpKQW1vQkhoMm5jT1RKNzJVczV4aUxHdDNWQ0JoSXVOYzN0WDhFMmh4cjg5RWNmZFhtaHlQTlJ0NmVnRlNpQjg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
