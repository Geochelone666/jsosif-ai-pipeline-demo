# MSFT Intelligence Report

- ticker: **MSFT**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/MSFT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MSFT/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:02:31.188265+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 3, 'ai': 16, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/MSFT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 535.9300 |
| Return 1D (%) | -3.5750 |
| Return 1W (%) | 1.0922 |
| Return 1M (%) | 2.0469 |
| Return YTD (%) | 11.5194 |
| Return 1Y (%) | 6.5422 |
| Annualized volatility (%) | 33.8503 |
| Beta vs SPY | 1.0369 |
| Max drawdown (%) | -30.5348 |
| Sharpe (rf=0) | 0.3539 |
| Downside deviation (rf=0, %) | 21.5880 |
| Sortino (rf=0) | 0.5550 |
| Historical VaR 95% (1D, %) | 2.8530 |
| Historical ES 95% (1D, %) | 4.1000 |
| Correlation vs SPY | 0.4164 |
| Tracking error vs SPY (%) | 30.7803 |
| P/E (trailing) | 29.00 |
| P/B | 8.46 |
| EV/EBITDA | 19.69 |
| Revenue growth (%) | 18.80 |
| Forward P/E (estimate) | 22.16 |
| Gross margin (%) | 67.66 |
| Operating margin (%) | 49.76 |
| Return on equity (%) | 34.22 |
| Free cash flow yield (%) | 0.08 |
| MA50 | 516.1348 |
| Close vs MA50 (%) | 3.8353 |
| MA200 | 438.4346 |
| Close vs MA200 (%) | 22.2372 |
| RSI (14, Wilder) | 54.4559 |
| MACD (12,26) | 4.7142 |
| MACD signal (9) | 5.1222 |
| MACD histogram | -0.4079 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MSFT': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 535.9300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.5750 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.0922 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.0469 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 11.5194 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 6.5422 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.8503 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.5880 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5550 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8530 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1000 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4164 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.7803 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.0369 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.5348 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3539 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.1648 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 67.6570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 49.7570 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 34.2210 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.0752 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 29.0005 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 54.4559 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.4079 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.8353 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 22.2372 -> Clearly above the moving-average trend level.

## TAILWINDS

### Microsoft Stock Has Gained More Than 50% in About 4 Months. Here's What It Has Usually Done Next.
- Summary: Microsoft Stock Has Gained More Than 50% in About 4 Months. Here's What It Has Usually Done Next.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxON3ZDcFFOQTFkaXM3TXZ2ZFNVaG5wLXV3d2ZCRWJqVjgwTWk0RjRKcmZJZEh6VG8wVW9wNjIxUVFZbzNtcW1GTkFyQ3ViV2hiX05qaG51UWFON0lkdC1ERHBibV9QX3dCa0NiMmpnc2w0QnowZ2d0ZVlaUk13V3JQX0M4YnU1OHVKN0VpSDB2aWs0cXJwbjRxeFVkTG4tLUoyZW5SWmRzMDBIMmlFZGZuOTd5Vk1wUXhSOWQxSkh3cDV0MmdhZFBKYzI3MUVBQ1prOXNr?oc=5>

### Microsoft Corp. (MSFT) Surges 37.8% on Record Quarterly Gains
- Summary: MSFT stock jumps 37.8% after reporting record quarterly earnings, boosting investor sentiment.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOQXo2dG9qMTRmU003ZF92OVVZQlpfU2JuS25fczJhUHpGWVFQNm1sQjYwSV9wd0IwNTBzZkZzdjVwNktPRkxNRGtlR3FGUFIya0hEenBBUHhHcy1JeFNWdUhmQjZFRExqcHZndzZzSDl0NXRBNUNwSUFhTi1DRTN5RTU1b0EtMS1YWjQ0NDM2bTd1dzlJVFV6VG5n?oc=5>

### Microsoft Corp Stock (MSFT) Opened Up by 5.61% on Nov 4: What Signal Does It Send?
- Summary: MSFT opened 5.61% higher on Nov 4, indicating bullish investor sentiment.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPZHZHSEpuclhTdFJqcEJTN2h6enV5Ry1CU2U5NTIwWXotZVllTVR0aW1oY1U1WWNOS05GUXpuNTJ5UEdCYlR3Z20wbXp5MHRPdGIwY0pWeUdNZWZLNFEyd3JFT0tsN0xlMjQ1MmJXQlRSdzBtbERwZHFvY0loU3d1d2hlYUJqRDZOM0Y0?oc=5>

### ETFs Bought $561.6 Million of Microsoft (MSFT) on Monday
- Summary: Large ETF purchases signal institutional confidence in MSFT shares.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxONWRFWERQczFobzFSekhaN0lBX3JRSk1SN3Q1VWg0azN4M3BTTmZFNVFhaG5LRUVWZGN3YV9kN1h5Y3ROTUJncTRMbUxXbHhtNlJfNl9YNlZvNUU3THdSeTZERmZpeG15YmdqU240TGx5TnFlaExjazFiaDE1RkZGZThNcTk4anYwZTBkZWhsZnhLMG9r?oc=5>

### 48 ETFs Add to Microsoft (MSFT) Holdings on Nov. 3
- Summary: 48 ETFs increased their Microsoft holdings on Nov. 3, indicating institutional confidence.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPS2RmVmRNRFNiYTg4aHlOSlUtcnJtSkwzaEIwbEJ6NW5xQmlQSm9YT3VZR0hXSXI4R2EwWV9vZUhha1ctSUFmWUN4aVl2TTZsclgtR044NXc5OTIzRVV3NlZmamlhQXNtRTVXV20yUEpoTFk5RmJpWV94VVlhdWdIRC1yT1dIMlBlaENucXROcmZJRWc1MXc?oc=5>

## HEADWINDS

### Microsoft Q3 Earnings: The Only Top AI Hyperscaler Generating Positive FCF (Rating Downgrade)
- Summary: Microsoft Q3 Earnings: The Only Top AI Hyperscaler Generating Positive FCF (Rating Downgrade)
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQV19fLURaRzFpSkg2NUk4NHBoZDVRN3dmWno3UmJ6NUtwOTJfNi1rbTFVWjhaRk1EZXhhM2lmQTJWWFFSMUhyWUhNb3huTFB4NmZhWUs4bU13cnJ3LWNHWFQ0OV9FdXczWXd0RHltSmlNUjBpYW83V2NVaXI4U3ZNOXBDY0FaYlNnQ3JnLV81RkI2bEdMQkJIR3djaXFLVU1lanZYWGNMRUwwNURlZDhScEh3bFg?oc=5>

## CATALYSTS

### Microsoft (MSFT) Stock Gets Fair Value Bump On Azure And AI Optimism
- Summary: Microsoft (MSFT) Stock Gets Fair Value Bump On Azure And AI Optimism
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOOGFuV1U3LUZsekt0ZU1FV3RlMWN4RDdGUENlVlM3SXhHUFlJSkk3S1AyU2taci1pMGN2ZTE3VDR5UmpqN19rajZQQXNsbmtQaEQyOHY0R1ZRZzZDNXVhTkk5MzBYOEk2WjAtX2JWZ3lWQWU1bmdYZHJLNk9LaW9BWEl2am5PTXo4UHlXaTNJYk5obEZwdl9RSVJfZw?oc=5>

### What's Going on With Microsoft Stock on Wednesday?
- Summary: Microsoft stock rises amid AI optimism and positive market sentiment.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQRVhBNThEMG02b1Fmc2xKZnktTDJUbGU5SkdxNFlDR0RLUjFPY1dudnZaZnRKZzdSUllHNTNnMUQwSk0zSXFmNnRBZkVhXzdfQU1tMEFsSXo3RmZZWVVySUpEV0ZKZlk1LVZrcjFoeURsWUVRd0pGQUdiNV9vWlhYYk81QWVUY0VrdEJFcGFyYU1SUldPVTJHeDYzN0VuaEl1WS1R?oc=5>

### Forget the 12-Month Squeeze: Microsoft Is Primed for an Explosive AI Payoff
- Summary: Analysts highlight AI potential to boost Microsoft’s future earnings.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOdkpnZnA5b1dlU3FEaXp5Y2NZOFVFc2h2YmduaWJpcXd1SDIzSV9mOGQzTldKMG93YkpEU2NnejRvc2MzU3BnbGdXZC05TEVuRExQdm5RVGh1T3FqR1BGQ1hvUUMzM1R2TjNIQndxUURkUWpiOEJvRmZOT3Jrb2FvWkZyX3EySE56Q3VDQkJGTzF4TUttY2VVT0VhZTdibTgzN3FISHRNdFl2Q2NYY3JTNVE1NWV3SzRKTnc?oc=5>

### Microsoft Stock (NASDAQ:MSFT) Surges as AI Development May Pay Off
- Summary: Shares climb as AI developments promise future revenue growth.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNbUZ5VDBrWW9GUUhQTDV4eGVCTFN0ZURkVVpkcDNETWNPdl8wUnRUSW1rTXNkMkhvZ0FidlE5blUzMWxVcFg3QUF0OE9yeXlnd2h4RTlvd0dSRE9LMGRuTmM4ZVNaaVY1cjJQMTVvQnlSNE5aLTZFdmRBbkZ1OTFvcHpFUUJHSXVCbTRHZ0tZZnprQS10S2xWaw?oc=5>

### Microsoft Corporation (MSFT) Outperforms with Record Quarter Driven by Azure Demand Surge
- Summary: Microsoft reports record earnings, driven by strong Azure demand.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxORm1BVWgtcHBpSHoyRGM1T1BpODlZQWRuTkk0TFBmRU9RMGg1UkVBcTVoTGstSVhjY1ZfaDUyM0lmSTlocU50QWNxOGx6S1VwY1RyN25RSzhWaHZoMHlodGxCTmJhQjJmaVVQSThSUnJad2dCTG5VMTRZYUZmUExqTzlOTU51MGM3N0twb2V3NDBqR3JYeHg5TkpxSmZDa2tpUGlxR2U3UVFYNGFEbnlV?oc=5>

### Microsoft (MSFT) Stock Could Be Undervalued After Its 74% Five Year Run
- Summary: Microsoft’s stock may be undervalued after a strong five‑year run.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQWHQ3RXM0cG00eE1IN192dkg5cGtlMUFnUzRVUkRNQnB2TFpLRXh6VjFxZVliTF9vdjU3anZxZTZPeHJERTV4bUZQN05na1BkOWxqeVpKYXc2d3M5c25uT1ZxWFRodFNzNmliMjNhYnYzNldKbXE3Wm9uRG1pSHNmNHBBaHdlZFUxbFppN3FlY0xMd0cwVXduUHdQcjVBWHB4SktqZFdB?oc=5>

### Microsoft Corp Stock (MSFT) Moved Down by 3.11% on Nov 5: What Signal Does It Send?
- Summary: Microsoft stock fell 3.11% on Nov. 5, reflecting a short‑term market dip.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQd0FzdldoemR0Zy1sYWRvcWhYRDB2M1NwTmdTSWNjVWZ4MDhuQVJST2JIRm1IeGVQVjN3VXFBVnUzNFJkZlVKV2hyd1AydlpZcHVuczhnM1IyN21tZUVlbEVBc1R0aksyOHJGUi05Q0NFeVNpU3Y2dlMwY1BmcTBOQWljWXFoZjZ4RERZ?oc=5>

### Why Did AAPL, MSFT, AMC Stocks Surge To 52-Week Highs?
- Summary: Microsoft shares surged to a 52‑week high, showing strong investor demand.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxOUWIyeExQTUxsUEhyTHFMRkdfSXpDclVURTlBTEpXU0hfY0RQRXM4anEyNlY1Rm9wb2U2ZGhEcXpxR1M3M0pIbWd1WmVLblRYRUI3Z2x3UklTRDRJa1J0QmRibVlpb2JWTERiWUl5Z2E4bTcxNHFsZnlHZ2xSSFFZSUJvYU15MWxzWEVFSnB4SQ?oc=5>

### Microsoft Corporation (MSFT) Is Betting Big on AI: Is Its Growth Story Just Getting Started?
- Summary: Microsoft is heavily investing in AI, signaling a strategic growth push.
- Date: 2026-11-03 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQcjZDbnhpSFhJeDNidjNPUlFXM2hKZk52ZGJHRjhublBjVWd2NWVlZ0ROV3ROOXJXajVYMHlrbnd4dXBtT2xRUlY2Qk9YMklpN053d3BQVVRjUmRhSUhvbFZtUnpfTjZqeTdmZ0FRR3p5LUFhUDJrUk04d1RVaXRIaURhRVhKb082aFhLdzNsQ3JDX1k2eXdRbXRTTWdHZk4wNlEyOQ?oc=5>

### Microsoft Corp.’s (MSFT) AI Advantage: Scale, Trust, and Economic Value
- Summary: Microsoft highlights its AI strengths in scale, trust, and economic value.
- Date: 2026-11-02 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPR0hrdUNkMEMwbE5ibl80WlQxNHdWWHRxODdNYTBEbWNsOFRSVHpzWF9FdTVHbEtENWx5M2lsTDd6cER2MGlHLVhCUkV5cDhXS05uaHpSSVpHRHd0VDhDZFZWNUkyMnBXRU9JTE9iZUdpUG16dk0xN3ZGcllDUEgzcF9EanZ5X3RHVU1xWnc0OUtnZ2lTME1sUjV4RUo?oc=5>

### Microsoft Stock Price Forecast: Shares Surge 7% in Single Day to Record High as Azure Growth Could Drive MSFT to $600
- Summary: Analysts forecast MSFT shares to hit $600 driven by Azure growth.
- Date: 2026-11-05 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxPYnlteU1qSlZHc1BIb2tVcDRzR0ZhNkJCWlgzX0hHd20tbTU4ZTZycXNmd2h4M0JyQ1NHRzA5QzEwOUhVZHVJZlpwSTliMWZVLVMxQi12eGxTZDNRTWExbHhBUTBycjA1UUFjc3AwbDMweUtJRzkybmwxSDRtTHZ1N1JhSUtWRDRaT2dEcDZCclh2MTNBcmdxRTVWd3JCTGlJQTZkTDIydGcxZ2dySGR6NHg3Z1h5VzR6TFl6RzMyVnNRcDI5LXhON0NoTDF6T1E?oc=5>

### Voters Just Made Microsoft’s Data Centers More Valuable, a Wall Street Veteran Says
- Summary: Voting increased perceived value of MSFT data centers.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQSmVLMGo2RFZNb0N3M2tlY0dWVzNrYUNoQlRRYS15aHJ3eEVzX0dqcnJIUDRLV2dKZ0hJV0d3M1JkYmxPTEdzTG10cUc4dUFrQkVGSDA4VzFlcW8teVd6TWtvcEFxdU1POWNQRmN1enpBbUxtSzNvcFhuVjFvei1VQl93ZmhmVmpwa3NkaDV0NUhRUEV4enpKNkdLRWFQX2Q4Uk9rWFJSTXNZalZ2bmg0M3lhQjBTQlVxcmdEWGpfRDJaVVU?oc=5>

### ETFs Are Net Sellers of Microsoft (MSFT) on Friday
- Summary: ETFs sold shares of MSFT, indicating selling pressure.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNYm8zY3YyUVpsVDRVWFkycURXMUNXSFNoRzdkam5KNWtDWHVtbDM1V09SdThvOHJ2cTY0ZHZXUURKU280d3dkMUJPcWpIQlJ5Q1V1eEk2MTRZaWZpbmNkQ0ktcEljOWtQZktVajhqbHVSZWkyOE4xQ3R1Y0RjSkRtWkRxUWFUOFpTbTdUTXlxaEpGUEJFZGZ0SHpscGk?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MSFT** | **29.00** | **8.46** | **19.69** | **18.80** | **3,979,920,277,504.00 USD** | **6.54** |
| ORCL | 18.05 | 5.63 | 14.10 | 29.60 | 359,035,273,216.00 USD | -53.38 |
| GOOGL | 15.09 | 5.27 | 18.20 | 24.70 | 3,473,915,510,784.00 USD | -0.35 |
| AMZN | 21.50 | 4.58 | 16.35 | 12.10 | 2,813,686,448,128.00 USD | 4.00 |

Peers fetched as_of: 2026-11-05; MSFT reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

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
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 19,953,000,000.00 USD; period 2010-10-01/2010-12-31; fiscal year/reporting period 2011/Q2
- Net income (latest available single quarter): 36,629,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi0wFBVV95cUxON3ZDcFFOQTFkaXM3TXZ2ZFNVaG5wLXV3d2ZCRWJqVjgwTWk0RjRKcmZJZEh6VG8wVW9wNjIxUVFZbzNtcW1GTkFyQ3ViV2hiX05qaG51UWFON0lkdC1ERHBibV9QX3dCa0NiMmpnc2w0QnowZ2d0ZVlaUk13V3JQX0M4YnU1OHVKN0VpSDB2aWs0cXJwbjRxeFVkTG4tLUoyZW5SWmRzMDBIMmlFZGZuOTd5Vk1wUXhSOWQxSkh3cDV0MmdhZFBKYzI3MUVBQ1prOXNr?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOQXo2dG9qMTRmU003ZF92OVVZQlpfU2JuS25fczJhUHpGWVFQNm1sQjYwSV9wd0IwNTBzZkZzdjVwNktPRkxNRGtlR3FGUFIya0hEenBBUHhHcy1JeFNWdUhmQjZFRExqcHZndzZzSDl0NXRBNUNwSUFhTi1DRTN5RTU1b0EtMS1YWjQ0NDM2bTd1dzlJVFV6VG5n?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPZHZHSEpuclhTdFJqcEJTN2h6enV5Ry1CU2U5NTIwWXotZVllTVR0aW1oY1U1WWNOS05GUXpuNTJ5UEdCYlR3Z20wbXp5MHRPdGIwY0pWeUdNZWZLNFEyd3JFT0tsN0xlMjQ1MmJXQlRSdzBtbERwZHFvY0loU3d1d2hlYUJqRDZOM0Y0?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxONWRFWERQczFobzFSekhaN0lBX3JRSk1SN3Q1VWg0azN4M3BTTmZFNVFhaG5LRUVWZGN3YV9kN1h5Y3ROTUJncTRMbUxXbHhtNlJfNl9YNlZvNUU3THdSeTZERmZpeG15YmdqU240TGx5TnFlaExjazFiaDE1RkZGZThNcTk4anYwZTBkZWhsZnhLMG9r?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPS2RmVmRNRFNiYTg4aHlOSlUtcnJtSkwzaEIwbEJ6NW5xQmlQSm9YT3VZR0hXSXI4R2EwWV9vZUhha1ctSUFmWUN4aVl2TTZsclgtR044NXc5OTIzRVV3NlZmamlhQXNtRTVXV20yUEpoTFk5RmJpWV94VVlhdWdIRC1yT1dIMlBlaENucXROcmZJRWc1MXc?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQV19fLURaRzFpSkg2NUk4NHBoZDVRN3dmWno3UmJ6NUtwOTJfNi1rbTFVWjhaRk1EZXhhM2lmQTJWWFFSMUhyWUhNb3huTFB4NmZhWUs4bU13cnJ3LWNHWFQ0OV9FdXczWXd0RHltSmlNUjBpYW83V2NVaXI4U3ZNOXBDY0FaYlNnQ3JnLV81RkI2bEdMQkJIR3djaXFLVU1lanZYWGNMRUwwNURlZDhScEh3bFg?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOOGFuV1U3LUZsekt0ZU1FV3RlMWN4RDdGUENlVlM3SXhHUFlJSkk3S1AyU2taci1pMGN2ZTE3VDR5UmpqN19rajZQQXNsbmtQaEQyOHY0R1ZRZzZDNXVhTkk5MzBYOEk2WjAtX2JWZ3lWQWU1bmdYZHJLNk9LaW9BWEl2am5PTXo4UHlXaTNJYk5obEZwdl9RSVJfZw?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQRVhBNThEMG02b1Fmc2xKZnktTDJUbGU5SkdxNFlDR0RLUjFPY1dudnZaZnRKZzdSUllHNTNnMUQwSk0zSXFmNnRBZkVhXzdfQU1tMEFsSXo3RmZZWVVySUpEV0ZKZlk1LVZrcjFoeURsWUVRd0pGQUdiNV9vWlhYYk81QWVUY0VrdEJFcGFyYU1SUldPVTJHeDYzN0VuaEl1WS1R?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOdkpnZnA5b1dlU3FEaXp5Y2NZOFVFc2h2YmduaWJpcXd1SDIzSV9mOGQzTldKMG93YkpEU2NnejRvc2MzU3BnbGdXZC05TEVuRExQdm5RVGh1T3FqR1BGQ1hvUUMzM1R2TjNIQndxUURkUWpiOEJvRmZOT3Jrb2FvWkZyX3EySE56Q3VDQkJGTzF4TUttY2VVT0VhZTdibTgzN3FISHRNdFl2Q2NYY3JTNVE1NWV3SzRKTnc?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNbUZ5VDBrWW9GUUhQTDV4eGVCTFN0ZURkVVpkcDNETWNPdl8wUnRUSW1rTXNkMkhvZ0FidlE5blUzMWxVcFg3QUF0OE9yeXlnd2h4RTlvd0dSRE9LMGRuTmM4ZVNaaVY1cjJQMTVvQnlSNE5aLTZFdmRBbkZ1OTFvcHpFUUJHSXVCbTRHZ0tZZnprQS10S2xWaw?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxORm1BVWgtcHBpSHoyRGM1T1BpODlZQWRuTkk0TFBmRU9RMGg1UkVBcTVoTGstSVhjY1ZfaDUyM0lmSTlocU50QWNxOGx6S1VwY1RyN25RSzhWaHZoMHlodGxCTmJhQjJmaVVQSThSUnJad2dCTG5VMTRZYUZmUExqTzlOTU51MGM3N0twb2V3NDBqR3JYeHg5TkpxSmZDa2tpUGlxR2U3UVFYNGFEbnlV?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQWHQ3RXM0cG00eE1IN192dkg5cGtlMUFnUzRVUkRNQnB2TFpLRXh6VjFxZVliTF9vdjU3anZxZTZPeHJERTV4bUZQN05na1BkOWxqeVpKYXc2d3M5c25uT1ZxWFRodFNzNmliMjNhYnYzNldKbXE3Wm9uRG1pSHNmNHBBaHdlZFUxbFppN3FlY0xMd0cwVXduUHdQcjVBWHB4SktqZFdB?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQd0FzdldoemR0Zy1sYWRvcWhYRDB2M1NwTmdTSWNjVWZ4MDhuQVJST2JIRm1IeGVQVjN3VXFBVnUzNFJkZlVKV2hyd1AydlpZcHVuczhnM1IyN21tZUVlbEVBc1R0aksyOHJGUi05Q0NFeVNpU3Y2dlMwY1BmcTBOQWljWXFoZjZ4RERZ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxOUWIyeExQTUxsUEhyTHFMRkdfSXpDclVURTlBTEpXU0hfY0RQRXM4anEyNlY1Rm9wb2U2ZGhEcXpxR1M3M0pIbWd1WmVLblRYRUI3Z2x3UklTRDRJa1J0QmRibVlpb2JWTERiWUl5Z2E4bTcxNHFsZnlHZ2xSSFFZSUJvYU15MWxzWEVFSnB4SQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQcjZDbnhpSFhJeDNidjNPUlFXM2hKZk52ZGJHRjhublBjVWd2NWVlZ0ROV3ROOXJXajVYMHlrbnd4dXBtT2xRUlY2Qk9YMklpN053d3BQVVRjUmRhSUhvbFZtUnpfTjZqeTdmZ0FRR3p5LUFhUDJrUk04d1RVaXRIaURhRVhKb082aFhLdzNsQ3JDX1k2eXdRbXRTTWdHZk4wNlEyOQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPR0hrdUNkMEMwbE5ibl80WlQxNHdWWHRxODdNYTBEbWNsOFRSVHpzWF9FdTVHbEtENWx5M2lsTDd6cER2MGlHLVhCUkV5cDhXS05uaHpSSVpHRHd0VDhDZFZWNUkyMnBXRU9JTE9iZUdpUG16dk0xN3ZGcllDUEgzcF9EanZ5X3RHVU1xWnc0OUtnZ2lTME1sUjV4RUo?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxPYnlteU1qSlZHc1BIb2tVcDRzR0ZhNkJCWlgzX0hHd20tbTU4ZTZycXNmd2h4M0JyQ1NHRzA5QzEwOUhVZHVJZlpwSTliMWZVLVMxQi12eGxTZDNRTWExbHhBUTBycjA1UUFjc3AwbDMweUtJRzkybmwxSDRtTHZ1N1JhSUtWRDRaT2dEcDZCclh2MTNBcmdxRTVWd3JCTGlJQTZkTDIydGcxZ2dySGR6NHg3Z1h5VzR6TFl6RzMyVnNRcDI5LXhON0NoTDF6T1E?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQSmVLMGo2RFZNb0N3M2tlY0dWVzNrYUNoQlRRYS15aHJ3eEVzX0dqcnJIUDRLV2dKZ0hJV0d3M1JkYmxPTEdzTG10cUc4dUFrQkVGSDA4VzFlcW8teVd6TWtvcEFxdU1POWNQRmN1enpBbUxtSzNvcFhuVjFvei1VQl93ZmhmVmpwa3NkaDV0NUhRUEV4enpKNkdLRWFQX2Q4Uk9rWFJSTXNZalZ2bmg0M3lhQjBTQlVxcmdEWGpfRDJaVVU?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNYm8zY3YyUVpsVDRVWFkycURXMUNXSFNoRzdkam5KNWtDWHVtbDM1V09SdThvOHJ2cTY0ZHZXUURKU280d3dkMUJPcWpIQlJ5Q1V1eEk2MTRZaWZpbmNkQ0ktcEljOWtQZktVajhqbHVSZWkyOE4xQ3R1Y0RjSkRtWkRxUWFUOFpTbTdUTXlxaEpGUEJFZGZ0SHpscGk?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
