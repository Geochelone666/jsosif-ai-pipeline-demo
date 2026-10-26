# MSFT Intelligence Report

- ticker: **MSFT**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/MSFT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MSFT/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:35:35.709805+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 2, 'ai': 16, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 10 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 52.0%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 524.5100 |
| Return 1D (%) | 0.6582 |
| Return 1W (%) | -0.8581 |
| Return 1M (%) | 4.7784 |
| Return YTD (%) | 9.1430 |
| Return 1Y (%) | 1.5878 |
| Annualized volatility (%) | 32.9780 |
| Beta vs SPY | 1.0114 |
| Max drawdown (%) | -34.4984 |
| Sharpe (rf=0) | 0.2097 |
| Downside deviation (rf=0, %) | 21.3478 |
| Sortino (rf=0) | 0.3240 |
| Historical VaR 95% (1D, %) | 2.8039 |
| Historical ES 95% (1D, %) | 4.0493 |
| Correlation vs SPY | 0.3909 |
| Tracking error vs SPY (%) | 30.3540 |
| P/E (trailing) | 29.22 |
| P/B | 8.81 |
| EV/EBITDA | 20.32 |
| Revenue growth (%) | 17.70 |
| Forward P/E (estimate) | 22.13 |
| Gross margin (%) | 67.94 |
| Operating margin (%) | 45.11 |
| Return on equity (%) | 34.04 |
| Free cash flow yield (%) | 0.42 |
| MA50 | 508.3546 |
| Close vs MA50 (%) | 3.1780 |
| MA200 | 435.3676 |
| Close vs MA200 (%) | 20.4752 |
| RSI (14, Wilder) | 52.6311 |
| MACD (12,26) | 7.1766 |
| MACD signal (9) | 9.4876 |
| MACD histogram | -2.3110 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MSFT': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 524.5100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.6582 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.8581 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.7784 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 9.1430 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 1.5878 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 32.9780 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.3478 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3240 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8039 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.0493 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3909 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.3540 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.0114 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -34.4984 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2097 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.1289 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 67.9440 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 45.1110 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 34.0390 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.4248 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 29.2206 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 52.6311 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.3110 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.1780 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 20.4752 -> Clearly above the moving-average trend level.

## TAILWINDS

### Microsoft (MSFT) Stock May Be 22% Undervalued After Maia 300 Unveiling
- Summary: Microsoft’s new Maia 300 launch suggests the stock may be undervalued, potentially boosting investor confidence.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOaHdDUjJiMUkwT3NkQ05EOWxJX3lpV1AxUWlqNG9PaHRUWm1BNnJtY3pUMHljbVY4M2UwR18zelVVWkVMa0xiemN6T19MQzhvU0FMLXNQOUdCb1prc0lxb2hxWlRhRTJPZE5aa05DNk1UT2pUWFhVX0Z1QlNHTFZReUhNSU1VbGlXZU1oeXZUNlgzNVZoNS1J?oc=5>

### Microsoft May Be the Only Hyperscaler to Stay Cash-Flow Positive. What It Means for MSFT Stock
- Summary: Microsoft’s continued cash‑flow positivity signals strong financial health, likely supporting stock performance.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQWFpDcUN6TWdfQ1AxeUMtTzZyNjdTRnJONzg0YWZTNFV6V2k5WDZxdl9TQXBrU1p0bk9PMVFLRkxma3VMdGNkSW8xcXczX1U1OUJBODNUN3BjaTZqMmNFcFFWQTZDb0VRZWRRY0Jnd2R4Wlk0TWFtbWpja2x0REQwd2xLaExFSVVDYnJfQm1iUl8xYndVMkZVZmRtV3JSVE5jMVBnRTA3T3diZ2ZZM0ktZDhqdldZajNyekE4WVNSVWJkZjI4X0g0cHB4T2FMcGJOTE1F?oc=5>

### Why Is Microsoft Stock Surging Today? Azure Growth Hits 43% as MSFT Targets $560 Next
- Summary: Azure revenue grew 43%, boosting MSFT’s outlook and target price to $560.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPZ3JQMng2OHFLNFd0RTRmZUpBbDBiVVlralZYbHU1TVFPcEdWNS1ZQ0w1alJDRDY1LXFDejZveUprMkVpa3RJMS1qbHpqbUpOYk9qbEZ3bXhoUW1iTWpuNUREeTZ1akxUQUQ5ZGhJWk9hcDJwb3pVbDRZblJIOElQQVl2Tmpma1VwS19oM1pIdnlXM3B0ZUpXX2RSTTA2YVZPUVhxOFJKekV3UXZGeXJUSEpxcE9zLVJPQzZHT01Lb3N2Zw?oc=5>

### Durable Growth Reinforces Microsoft Corporation’s (MSFT) Investment Thesis
- Summary: Microsoft’s sustained growth strengthens its investment case.
- Date: 2026-10-23 | Impact: high | Horizon: medium | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOSmE3ZUloOVJQaU1BWnNsdXRHWTBZUWRyZy1BUHdDWF9QQ0xGU0hwUlNQVzljQkdONXI3dnNORVRSV2JIQlVlcTg0X3lzSFZySzNKZnlfbGsyMUp4dWRJX0hJYVdFeGV4VjRqSnFfZlA0WHpsRjJnVUFaUzg3OGRnLVYySWJkMHB5aVYwYmVWVXkwQXBDbTZmQWxGUGxZd3NyeXg3MmZiZUI2MVVDTXRjLXZn?oc=5>

### Strong Azure Growth and Cash Flow Discipline Strengthen Microsoft Corporation (MSFT)
- Summary: Azure’s robust growth and disciplined cash flow boost Microsoft’s outlook.
- Date: 2026-10-23 | Impact: high | Horizon: medium | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOM2g5ODlTNnI5Z0ZKOVlSSUswLWdIa3E4eDZqN05NbWpnU0RjTDRyWEFMUzJDaGdjTVZtMnN0RVFPeGRhVHNnN3M3WXpMM2I2YU1aN0RaTVYzZ1JvcFJ5aVFHZXNvb3JiQkJfSU9oMnh3em5CLW5GamxRUGRRSVl6dGJlRlZVRjF0Q2lrU2tZNjVWSXphRnI3Q0pB?oc=5>

### Jim Cramer and Ken Fisher’s AI Pick: Microsoft (MSFT)
- Summary: Positive analyst endorsement highlights Microsoft’s AI prospects.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOb1pmemlxTW5xT1NRanZxNjRjNG04bF9iSnEwQzV1enVSSWNoR1ZZQVB4QjA3MWFrSnJXTllUTU5fbmUzUDhHZXdSQ3d6LWo3c0Z2Ukp4UFhHUldSUXVsVjdqcWUxczg3X1dfUVFUU2VHR1ViNzd5dHFFODMycEdtdXBDbTUxUHFMU2FfaTlvaEJuYms?oc=5>

### Market Re-Rating Aligns Microsoft Corporation’s (MSFT) Valuation with Core AI Fundamentals
- Summary: Valuation aligns with AI fundamentals, boosting investor confidence.
- Date: 2026-10-21 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPdWVNMTM3dzBuUmZvU3VuMzhPQkM3WlNnZ2JOc2lFU203eDAybkRkSldaLU5XRTZMbFJCQTJocC1hVTV3cHViWVVEWHFMdnZ6SGZjNVljcXZ2S2NZanpDRG5xZldLM3NCeVNjQS1yWGNoMzVkUFJXbzVNMlhXRWNybEg5RV9fWkdJT1pINXhsaVJ3cS1zM1RWUENva0Zkc1BIOFZzeUZXQUZ1anc?oc=5>

## HEADWINDS

### Microsoft (MSFT) Falls More Steeply Than Broader Market: What Investors Need to Know
- Summary: Microsoft’s share price dropped more sharply than the broader market, indicating short‑term downside risk.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOYWNjS2pNU3JnRHk1ejRIQkRnTlFGWXQ4OFpscFlZVTBfa0RqRTRxNGpZLVNUSTJfRWRoc1pZVkFkcEVhbEZWZEZLT3ItZnFDNlJhZ1FxYkZ5S29GZ0p6b19GQVdjcHYycFBrWFcwUm92bUVoUE5IcE5zVGU3QTNPTUhlcEFweTh6Q3NnRUNFSVZJSXVaU2d6em9maFlXVnM?oc=5>

### Microsoft Q1: A $744 Billion AI Reckoning Is Coming (NASDAQ:MSFT)
- Summary: Anticipated AI challenges could weigh on performance.
- Date: 2026-10-24 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQUTN5LS1OVkkwY2UzWFh0SkJlM21VRkpmRXpEYXNwZEIydFRPZGdnRTl4OWlfWkEzUXNkdlljRllvVlhpTzQtdkptbzlPcDJ4MUEwVWVzUTVVVERsZ2QwNW1OR3loNm44Wk5ObGhrbmtuYWt1aHFQRmU1bTNQV2MwRXZxb1IwTl9jVHoyX0QyNUNiTW1I?oc=5>

## CATALYSTS

### Microsoft Earnings Report To Focus On AI Momentum, Capex
- Summary: Microsoft Earnings Report To Focus On AI Momentum, Capex
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPVkhrYl9acjF5aWRCRnliWEZWQUNJbU5ST2V5M3hJZlQ2TzBMUU1mRmdiQWpzeDdXVVA0THRVYUhXMl9QLWZPbzc3ZnVNRFVqRU5BNkY3N0ZwbmlYOURTajh5b05PdDc0OGxISm50UW5kbEo5TGM4aE9NLUNuUWlEYzA0MFg5ZF9rcGw2VkJhUElJZjgy?oc=5>

### Microsoft (MSFT) Stock Gets Fair Value Bump As AI Revenue Views Lift
- Summary: Microsoft (MSFT) Stock Gets Fair Value Bump As AI Revenue Views Lift
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPaFJ2SkhKWnczQjZFSEhxNmZlNG4zYkFlMEVVbVRBSWcxbmZjbWd3RVBXTGpmeE9hQ0FBV2MxMjFhU0xLVTNWa21HSVZyanF0aWUwZ3BLdWlFS2Jmby0yeXpKbHoyblJRXy1ibGlsVUU1U1VkR191QkVQZ0IzVFVfQWg3VFJGSE5NQ2RLMjJkakxWQ0s5WFBFeVY0TQ?oc=5>

### Microsoft (MSFT) Earnings Expected to Grow: What to Know Ahead of Next Week's Release
- Summary: MSFT’s upcoming earnings are projected to rise, signaling stronger financial performance.
- Date: 2026-10-21 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNbjlpQWhTY0NBUTRLWDJSb2VnRWxHYWo3QzZzVTFzd0xuTzJ6MktWOHB0X25ROU1lWE9IWUdINE9nSEtQa2Q5WmNfMHBrRzRzNkNFY0IwRWlSUzBXM1RnNHdQNi1BU29pNTVIRXBNbDY5Vlk5aDhfY1htWHEyWExYWWxPUnhmdV9LWnBzQmZwQW54Uk84SllLMVdFd185ZS1KWTk5Uw?oc=5>

### Seeking Clues to Microsoft (MSFT) Q1 Earnings? A Peek Into Wall Street Projections for Key Metrics
- Summary: Market expectations for Q1 earnings are analyzed.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQYkxldmNtU2E3NVlJM0QzOFV5enVyOThvWnN6bllld0VwYkpBeG8xZUlNTEloeDBQb0pFVnJjQmNXakdIWTRVcUJGeFRwelVWcjZGNEVZejJwZWMzem5MdXRkUG1lM1JreUhXZDlKYmRLTG4yaU1JQ1pZRVJMaHltaDQ5aHU0aUFyNW5DNHZoYmJJTld0enBnUFFVeVY?oc=5>

### Earnings Preview: What to Expect From Microsoft’s Report
- Summary: Preliminary outlook for Microsoft’s upcoming earnings report.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQMGZ2YWp2d0RyYU1ycUpfUnl0WWM4V0RIaWZOem9rUldkbkVUdmNZWVhmYmdjb3FLSVRiVmhDQ1Fsblk1UElVWG5nLW5YZWx2aF94Z0tKU01fLXQzWTJ4ZHZqeXR4WlI3Y2pEU3dqbjRvaDRwZjlIMmVHU29menpzNFdIc2tkTWFsVWJkX1ZxVVFWaGFYSmszNmphU0t5Zi10RFM5TjRlYWs?oc=5>

### Dear Microsoft Stock Fans, Mark Your Calendar for October 28
- Summary: Upcoming event likely earnings, potential upside.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQWV9DZnczUmFIazNYWFZzamRDdnhDWm1hMEhpWEpSWXc4N0h0VTNpcXBIdzBTR2F6ejF6U0FFMVFVaVJMR2ttbjE4RkFPQlBPWFRPcHloZ0NuYlkxTjBrVmU1YldkczBzbTRlb01fa3FDUjBEVWEyM2tJaWl6MHluZi1BSXZiVkI3WkpUeFZsaGpOTzJ2VzBPS0tsNA?oc=5>

### Will Microsoft (MSFT) Beat Estimates Again in Its Next Earnings Report?
- Summary: Possible earnings beat could lift stock.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNcW10MmRRSDR3QVY2dG9ITTRZb3J6aFhMaGZ5anVteGZQd3h2YzFjS2ZTS0ZCdnJxZ0xvUDA1bDYyX3BaYnBjbnRkN2ZfMG5wbi1FWGFweUFkaDZleTV6T212aGF6TTNtR19xTnRNTU12dzZLNUZTNm5oSi1qbC1kUm5oREtTR1dHbmdBQ21ENGJZZmlPdVJ2NVpDR29mVzJZcUE?oc=5>

### Microsoft (MSFT), Alphabet (GOOGL) and Amazon (AMZN) Earnings: Can They Save the AI Stock Rally?
- Summary: Microsoft’s earnings could influence AI‑related stock rally, potentially boosting investor confidence.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxPOG5TZHpqYkVsSTVEUDhRZGdualhHTnFTSTBtaHBrWE1tUVp1clNEbHFxWEVfNDZlV01NNjYzdjczM3lrSkFiN2E3el9NOHZKV1hqZEFkblVTdnZDN0lrd0tUUXp3Zkk1U3JmX0ZxbktGay0xMWlxdHV4SFY3cW0tcQ?oc=5>

## RISKS

### Microsoft (MSFT), Alphabet (GOOG), Goldman Sachs (GS) join objections to OKX-ICE tokenized stock trading
- Summary: Regulatory objections may pose compliance risks for Microsoft’s trading operations.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxQT1JQcGkxc2tGRTIyUG42RldTRkh1TDY3Y2tXblZDNXZScVRFZ25iRXBtTVdoeDVURFVPaE1ETzlyRjNGX0FyMm5aLWRCOTlUOXNLMVFyai1YY1NOTmJHOWJ4dUtneVJQV2h5LWRnWWxjajNNd3dmQ3NrTGZ4U09wZUVWUHVIQ2ZlMlhMU0hjc2lTMjgwQ0g3TmRVa2E4aDBjMVdKWmtkTzJ0dy1GamRiV255ZTM2eVA1ZlBIamFxdV9IWmlUOXVPVnlZTDI?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MSFT** | **29.22** | **8.81** | **20.32** | **17.70** | **3,894,773,022,720.00 USD** | **1.59** |
| ORCL | 19.77 | 6.17 | 15.07 | 29.60 | 382,454,169,600.00 USD | -54.35 |
| GOOGL | 16.07 | 6.29 | 22.02 | 24.20 | 3,916,147,458,048.00 USD | 26.85 |
| AMZN | 19.95 | 4.85 | 16.60 | 19.60 | 2,675,005,718,528.00 USD | 12.17 |

Peers fetched as_of: 2026-10-25; MSFT reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-29
- Next expected earnings: 2026-10-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-07-29
- Revenue (latest available single quarter): 19,953,000,000.00 USD; period 2010-10-01/2010-12-31; fiscal year/reporting period 2011/Q2
- Net income (latest available single quarter): 31,778,000,000.00 USD; period 2026-01-01/2026-03-31; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilwFBVV95cUxOaHdDUjJiMUkwT3NkQ05EOWxJX3lpV1AxUWlqNG9PaHRUWm1BNnJtY3pUMHljbVY4M2UwR18zelVVWkVMa0xiemN6T19MQzhvU0FMLXNQOUdCb1prc0lxb2hxWlRhRTJPZE5aa05DNk1UT2pUWFhVX0Z1QlNHTFZReUhNSU1VbGlXZU1oeXZUNlgzNVZoNS1J?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQWFpDcUN6TWdfQ1AxeUMtTzZyNjdTRnJONzg0YWZTNFV6V2k5WDZxdl9TQXBrU1p0bk9PMVFLRkxma3VMdGNkSW8xcXczX1U1OUJBODNUN3BjaTZqMmNFcFFWQTZDb0VRZWRRY0Jnd2R4Wlk0TWFtbWpja2x0REQwd2xLaExFSVVDYnJfQm1iUl8xYndVMkZVZmRtV3JSVE5jMVBnRTA3T3diZ2ZZM0ktZDhqdldZajNyekE4WVNSVWJkZjI4X0g0cHB4T2FMcGJOTE1F?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPZ3JQMng2OHFLNFd0RTRmZUpBbDBiVVlralZYbHU1TVFPcEdWNS1ZQ0w1alJDRDY1LXFDejZveUprMkVpa3RJMS1qbHpqbUpOYk9qbEZ3bXhoUW1iTWpuNUREeTZ1akxUQUQ5ZGhJWk9hcDJwb3pVbDRZblJIOElQQVl2Tmpma1VwS19oM1pIdnlXM3B0ZUpXX2RSTTA2YVZPUVhxOFJKekV3UXZGeXJUSEpxcE9zLVJPQzZHT01Lb3N2Zw?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxOSmE3ZUloOVJQaU1BWnNsdXRHWTBZUWRyZy1BUHdDWF9QQ0xGU0hwUlNQVzljQkdONXI3dnNORVRSV2JIQlVlcTg0X3lzSFZySzNKZnlfbGsyMUp4dWRJX0hJYVdFeGV4VjRqSnFfZlA0WHpsRjJnVUFaUzg3OGRnLVYySWJkMHB5aVYwYmVWVXkwQXBDbTZmQWxGUGxZd3NyeXg3MmZiZUI2MVVDTXRjLXZn?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOM2g5ODlTNnI5Z0ZKOVlSSUswLWdIa3E4eDZqN05NbWpnU0RjTDRyWEFMUzJDaGdjTVZtMnN0RVFPeGRhVHNnN3M3WXpMM2I2YU1aN0RaTVYzZ1JvcFJ5aVFHZXNvb3JiQkJfSU9oMnh3em5CLW5GamxRUGRRSVl6dGJlRlZVRjF0Q2lrU2tZNjVWSXphRnI3Q0pB?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOb1pmemlxTW5xT1NRanZxNjRjNG04bF9iSnEwQzV1enVSSWNoR1ZZQVB4QjA3MWFrSnJXTllUTU5fbmUzUDhHZXdSQ3d6LWo3c0Z2Ukp4UFhHUldSUXVsVjdqcWUxczg3X1dfUVFUU2VHR1ViNzd5dHFFODMycEdtdXBDbTUxUHFMU2FfaTlvaEJuYms?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPdWVNMTM3dzBuUmZvU3VuMzhPQkM3WlNnZ2JOc2lFU203eDAybkRkSldaLU5XRTZMbFJCQTJocC1hVTV3cHViWVVEWHFMdnZ6SGZjNVljcXZ2S2NZanpDRG5xZldLM3NCeVNjQS1yWGNoMzVkUFJXbzVNMlhXRWNybEg5RV9fWkdJT1pINXhsaVJ3cS1zM1RWUENva0Zkc1BIOFZzeUZXQUZ1anc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOYWNjS2pNU3JnRHk1ejRIQkRnTlFGWXQ4OFpscFlZVTBfa0RqRTRxNGpZLVNUSTJfRWRoc1pZVkFkcEVhbEZWZEZLT3ItZnFDNlJhZ1FxYkZ5S29GZ0p6b19GQVdjcHYycFBrWFcwUm92bUVoUE5IcE5zVGU3QTNPTUhlcEFweTh6Q3NnRUNFSVZJSXVaU2d6em9maFlXVnM?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQUTN5LS1OVkkwY2UzWFh0SkJlM21VRkpmRXpEYXNwZEIydFRPZGdnRTl4OWlfWkEzUXNkdlljRllvVlhpTzQtdkptbzlPcDJ4MUEwVWVzUTVVVERsZ2QwNW1OR3loNm44Wk5ObGhrbmtuYWt1aHFQRmU1bTNQV2MwRXZxb1IwTl9jVHoyX0QyNUNiTW1I?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPVkhrYl9acjF5aWRCRnliWEZWQUNJbU5ST2V5M3hJZlQ2TzBMUU1mRmdiQWpzeDdXVVA0THRVYUhXMl9QLWZPbzc3ZnVNRFVqRU5BNkY3N0ZwbmlYOURTajh5b05PdDc0OGxISm50UW5kbEo5TGM4aE9NLUNuUWlEYzA0MFg5ZF9rcGw2VkJhUElJZjgy?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPaFJ2SkhKWnczQjZFSEhxNmZlNG4zYkFlMEVVbVRBSWcxbmZjbWd3RVBXTGpmeE9hQ0FBV2MxMjFhU0xLVTNWa21HSVZyanF0aWUwZ3BLdWlFS2Jmby0yeXpKbHoyblJRXy1ibGlsVUU1U1VkR191QkVQZ0IzVFVfQWg3VFJGSE5NQ2RLMjJkakxWQ0s5WFBFeVY0TQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNbjlpQWhTY0NBUTRLWDJSb2VnRWxHYWo3QzZzVTFzd0xuTzJ6MktWOHB0X25ROU1lWE9IWUdINE9nSEtQa2Q5WmNfMHBrRzRzNkNFY0IwRWlSUzBXM1RnNHdQNi1BU29pNTVIRXBNbDY5Vlk5aDhfY1htWHEyWExYWWxPUnhmdV9LWnBzQmZwQW54Uk84SllLMVdFd185ZS1KWTk5Uw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQYkxldmNtU2E3NVlJM0QzOFV5enVyOThvWnN6bllld0VwYkpBeG8xZUlNTEloeDBQb0pFVnJjQmNXakdIWTRVcUJGeFRwelVWcjZGNEVZejJwZWMzem5MdXRkUG1lM1JreUhXZDlKYmRLTG4yaU1JQ1pZRVJMaHltaDQ5aHU0aUFyNW5DNHZoYmJJTld0enBnUFFVeVY?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQMGZ2YWp2d0RyYU1ycUpfUnl0WWM4V0RIaWZOem9rUldkbkVUdmNZWVhmYmdjb3FLSVRiVmhDQ1Fsblk1UElVWG5nLW5YZWx2aF94Z0tKU01fLXQzWTJ4ZHZqeXR4WlI3Y2pEU3dqbjRvaDRwZjlIMmVHU29menpzNFdIc2tkTWFsVWJkX1ZxVVFWaGFYSmszNmphU0t5Zi10RFM5TjRlYWs?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQWV9DZnczUmFIazNYWFZzamRDdnhDWm1hMEhpWEpSWXc4N0h0VTNpcXBIdzBTR2F6ejF6U0FFMVFVaVJMR2ttbjE4RkFPQlBPWFRPcHloZ0NuYlkxTjBrVmU1YldkczBzbTRlb01fa3FDUjBEVWEyM2tJaWl6MHluZi1BSXZiVkI3WkpUeFZsaGpOTzJ2VzBPS0tsNA?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNcW10MmRRSDR3QVY2dG9ITTRZb3J6aFhMaGZ5anVteGZQd3h2YzFjS2ZTS0ZCdnJxZ0xvUDA1bDYyX3BaYnBjbnRkN2ZfMG5wbi1FWGFweUFkaDZleTV6T212aGF6TTNtR19xTnRNTU12dzZLNUZTNm5oSi1qbC1kUm5oREtTR1dHbmdBQ21ENGJZZmlPdVJ2NVpDR29mVzJZcUE?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxPOG5TZHpqYkVsSTVEUDhRZGdualhHTnFTSTBtaHBrWE1tUVp1clNEbHFxWEVfNDZlV01NNjYzdjczM3lrSkFiN2E3el9NOHZKV1hqZEFkblVTdnZDN0lrd0tUUXp3Zkk1U3JmX0ZxbktGay0xMWlxdHV4SFY3cW0tcQ?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxQT1JQcGkxc2tGRTIyUG42RldTRkh1TDY3Y2tXblZDNXZScVRFZ25iRXBtTVdoeDVURFVPaE1ETzlyRjNGX0FyMm5aLWRCOTlUOXNLMVFyai1YY1NOTmJHOWJ4dUtneVJQV2h5LWRnWWxjajNNd3dmQ3NrTGZ4U09wZUVWUHVIQ2ZlMlhMU0hjc2lTMjgwQ0g3TmRVa2E4aDBjMVdKWmtkTzJ0dy1GamRiV255ZTM2eVA1ZlBIamFxdV9IWmlUOXVPVnlZTDI?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
