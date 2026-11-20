# GOOGL Intelligence Report

- ticker: **GOOGL**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/GOOGL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GOOGL/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:40:08.739660+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 3, 'ai': 16, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/GOOGL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **13**; {'directional_claim_without_event_type': 5, 'low_uncalibrated_model_confidence': 7, 'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 12 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 30.43%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 272.6600 |
| Return 1D (%) | -3.4627 |
| Return 1W (%) | -8.7178 |
| Return 1M (%) | -20.7798 |
| Return YTD (%) | -12.7187 |
| Return 1Y (%) | -6.6394 |
| Annualized volatility (%) | 33.6752 |
| Beta vs SPY | 1.3214 |
| Max drawdown (%) | -32.1946 |
| Sharpe (rf=0) | -0.0359 |
| Downside deviation (rf=0, %) | 24.1061 |
| Sortino (rf=0) | -0.0502 |
| Historical VaR 95% (1D, %) | 3.1807 |
| Historical ES 95% (1D, %) | 4.8274 |
| Correlation vs SPY | 0.5454 |
| Tracking error vs SPY (%) | 28.5773 |
| P/E (trailing) | 14.24 |
| P/B | 5.08 |
| EV/EBITDA | 17.55 |
| Revenue growth (%) | 24.70 |
| Forward P/E (estimate) | 17.82 |
| Gross margin (%) | 60.86 |
| Operating margin (%) | 33.32 |
| Return on equity (%) | 44.29 |
| Free cash flow yield (%) | -0.03 |
| MA50 | 323.7648 |
| Close vs MA50 (%) | -15.7845 |
| MA200 | 337.0359 |
| Close vs MA200 (%) | -19.1006 |
| RSI (14, Wilder) | 30.5811 |
| MACD (12,26) | -12.7598 |
| MACD signal (9) | -12.9229 |
| MACD histogram | 0.1631 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GOOGL': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 272.6600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.4627 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -8.7178 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -20.7798 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -12.7187 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -6.6394 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.6752 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 24.1061 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.0502 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1807 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.8274 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5454 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.5773 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3214 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -32.1946 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0359 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.8240 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 60.8570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.3210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 44.2860 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -0.0347 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.2381 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 30.5811 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1631 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -15.7845 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -19.1006 -> Clearly below the moving-average trend level.

## TAILWINDS

### Alphabet Stock Is Jumping. 2 Reasons the Comeback Starts Now.
- Summary: Alphabet Stock Is Jumping. 2 Reasons the Comeback Starts Now.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE10WDdwclZjV3ltY3NHVm9ia044N0huUnBJZGgtN1FkalNkajRpS1R4XzFjYjg3ajRXS0hwWDdvbHdPQ0k5eWxhSHBuOS1Da2x5S285MFJ1QVVwN2Nob2pLQlZmYVlwQ1ljT2VOaXBPMWMzU3dkaE5Wbg?oc=5>

### Alphabet stock climbs on upward price move as buyers show steady interest
- Summary: Alphabet stock climbs on upward price move as buyers show steady interest
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPQVNmZHh0Wm5WUnhuTFI1WU9pRlIycURsUmprUW9RYkZNSVhub3RvNUdSLVNGY2I0U01nbG9zQ0w3RGhWYzJTZ2tqLTRnVHVLOUxrYVpyUmJKMG14bmlQYjNFanFNcE14ZmlLY2NkbUVyamlQUHJ4TEFodGx5ZDZCbDZXWHN5TWJEakI0NTItNnZLc1k?oc=5>

### Alphabet Stock Down Nearly 17%: What Decides It Now?
- Summary: Alphabet shares fell 17%, prompting analysis of factors influencing the decline.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPN0s1WHI2clhqM2U3Z2NBOWVXcmFUdmR5ZzRDbGVQVWtCTkFic2YwZWFpb3hTRE1JSXRDOHd4NHhKZzFvazlGWlJXVDJpUmRydUhZc2RyUHhTSVJ3YWIyMFhKWjg5ZS1uR0hsRnFvX05hVjJRYnJEZ2ZFVTBpTkNlSUQ0QUlnVUZYbkZabUMwU2lucmUyNlkwalRZSUU4SjczM0dxaXJMUEJZRmR3VWhMNA?oc=5>

### Cramer: My favorite chartist sees two major signs of a rally brewing in Alphabet stock
- Summary: Analyst predicts a short‑term rally in Alphabet shares.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxNd1NpVlByZC1xZWxaeU1lbVc5T05GWGVqUDdkcXUxTmt5NXNyUHo5c3ZGaEM5NHExYVZ0UC0xX1RpbDU5WlBlUEY0RG5VdTNmZ0JWQkNlS04zNmJxcmtPb01FX1g2cTdPNHFJYmNSWnZRQ3dxTHFBd0E1a3N1RjlXMTFtdzFteE3SAYwBQVVfeXFMT3drcmRET3BhVThONnRna1oyWGQ0aHpabjM5cVRuUVJkM2JJSWJmcHUwWTRvWG50YlVtWXNDUFBYS3Y3VXhhR2swZ0dQdVBaeEY3TmhWaXNkUU53N2loaXdZMTFRQjlQQmFfMnRiVzlORVV5RUxCSFltajhXZnJKVnhnTW9oc25ueXB2OFo?oc=5>

### Alphabet: Why I Caught The Falling Knife (NASDAQ:GOOG)
- Summary: Author explains a recent sharp decline in Alphabet shares and reasons for buying.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxOYnNCbDJDZEN2TjM3VE9qakJEWTlNdlFMQjZkVUZDVGllanRtRWhLMHlXQUd2dTV3UHFMQTgwQVRJUjJ6RWF6b0UtbF96c21DZG1fSEpfRktjTjFvdGZnazZnRVRtbTk5UWFQeXJhZzE5Zi1NcEg0Sk5FMlB4MnUtaDJqeVpwb1U?oc=5>

### Why Alphabet Stock Popped Today
- Summary: Article discusses factors behind Alphabet's recent price increase.
- Date: 2026-11-19 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNNkJZTFlxSDA4eURKd2lBVEloR3FmMUUwU0M5U19hN3Q2Rm0xSURyeGFjSjFfNE54eGNKTzAwQ2J3TlpVUkpSV3JuN0Y0X3l2UlUxRlRzeXpNZkJfa180MFFZMHVWTTJ5M1R0RFEtckFHSnBwS1l2M05ucnZ6UEpGU0NBZG1kZEcyR0JMZlUzUWp0Z0p1TVJYVTZBblIxQW8wRGR5SVJra3hGdHRPVnRkNExKZzZlR25GQUE?oc=5>

### How To Buy Alphabet (GOOGL) Stocks & Shares
- Summary: Guide on purchasing Alphabet shares via various platforms.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNZ1Rpa1o2S3NHZU9kcEUtdUtaWENWd3JZTmZ4SkZhdF9KQ3pkVmRLZWo0c1pGc2RrWDRSTW5LRWxITi1PbFpZVlpPbnVMeUM1UEtjeUVGVGhybnU1Zy1NLUs0M2FSR3RJellkTlNfZGNJX3JGUU5tZlFqMnlTTjRPMlIzZnQtbHI0bWc?oc=5>

### Billionaire Investors Make Surprising Moves in Google Parent Alphabet Stock
- Summary: Report on notable investors buying Alphabet shares.
- Date: 2026-11-19 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxOTUpFZU5IMm8xb0NpX09XTnlsTzlPOEg4WlZSUjQxOTdBcEZHTkFFTWwyQVhoVlAxQjJlSWNPX0gwQ2xLaVJjdTVUdFFBRjFsekQ3OTQxZEpFcVYzcXBxNkYxN1UxczRkWXBWTENTc2VpSU5odWp3UE51LVp3NGV6cjJScmN4ZzNkZms1akZQMWZibmVhbW1VaGNTcm5HdEZBTkIzWU1nNHM4b2FCSVpFdUxCN1VrekZNRlhUMmpCZ3lYNi1RbkpRa0xLY0pJb0xE?oc=5>

### Is Alphabet Stock a Buy Right Now?
- Summary: Analysis of whether Alphabet shares are a good purchase currently.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxQem5kdTNnLWkxWjFsM3dqMF9xYkwxZ2dkbkR0d1V6TFo5dkJaMnIwMzhGbEhORmprZVFHZmhpRlI4VDFVd09SWWp6ZkpZSjdycTY1VjNseUwyWlpFRHRKRHI4X09kcWs3ekdPLUpfREtQM3ltWnRpS3g0dDE0SHpFZnZR?oc=5>

### Amazon and Alphabet Will Own Over 28% of Anthropic After Its IPO. Here’s What That Means for Their Stocks.
- Summary: Alphabet and Amazon acquire a 28% stake in Anthropic, potentially boosting AI-related revenue.
- Date: 2026-11-18 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOYU1Lcy0yRzhtLVRmZ003M0VQVVJTbUF3ZEFXMVItd3JjdElrZVdYalkzWjNsVXNvaDkzcHYtZHBEWnRVREw5T2YzaHZNUEQtRVJEeVVWUlE0WDUwMF9PXy1zS05FMFlaS0Myc3ZCVHFWVmVsYXd0VXBHQl9qOXhXMFFNQm9iaWUtbjl4VW9ZUFg1Y3VnSWIwZHl6c2dscnNUMWhFRklQZGc?oc=5>

## HEADWINDS

### Alphabet Stock Is Falling. Here’s Why Investors Should Be Buying the Dip.
- Summary: Alphabet Stock Is Falling. Here’s Why Investors Should Be Buying the Dip.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPd3c1Y0FKdVByU21IUFJZTzVKNkNaYWs2S1VSVExMLURtWFhxLVczRXVjaGpsUWp0NzlmZU5GVmNoN2lBMHVoSU4zWDVPcG5IUENrNEVRRngwNUpmREJRWFh6bHRnamN0MlpYaENFZ2V2dWFHOHZlUW93MmxqVEd2eFZyeGJCRmV0UW5USHdWdHBNeGF6cWRSMS1hMDhOYmtpU1dF?oc=5>

### Stock Market Today, Nov. 19: Alphabet Shares Fall as Anthropic Nasdaq Debut Puts Fresh Value on Google's Stake
- Summary: Alphabet shares dropped due to competitor debut, indicating a short‑term market move.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi-wFBVV95cUxNYUZ3Rm82c1V1TW1rd1lFUTRYM2s2LWJvSG44OWJOTHZ2UEkzNnkyT2ZPZjFES1FjclE0WWYyNkZlWm9DT25xTEIta1JzNzVXLU9ocVF4VVZ1VUVRWmhfQ3JKazNPUjY0M2lEa0lncE1PLS1uTGw4Nk9BdkRWdVk1aWQxT0RlTEVQUEhQT05GWktVYkl0Qk5RSGdWWkNmeEF1Q0JDZVhaQVM2VVk5d2ZmXzVtYXdxSWFPWHR4YWRZemo0Sk9HcFFxWWZrUGVBeS1DcjZnVkJxNzBGRnl6ODVyZ1BSSnByX2ZxM3dEX3BLaWVoZl9hb1VNMHVmOA?oc=5>

### Alphabet (GOOGL) Stock Could Be 47% Undervalued As AI Spending Fears Bite
- Summary: Analyst warns AI spending fears may undervalue Alphabet, suggesting a medium‑term headwind.
- Date: 2026-11-19 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNT1ZWV245S1M1R2I2RVIyNHprYlZwcGN1eGlRWE9ZNTJYd0Q3V2xyb0FFZWdNcFRhVHVPVUtKdEdrYmd4bDlNbkRkdTNFazJLUU1wS0g1WlVFd3U3YU1pbkl4R09QVmFkVEZYMTNjU1FJbnU0bGY5Mk9zNWxFcWV2Y0h1aDF1aGlnYjBmNk53LU5TaHVwdTBmRjd3?oc=5>

### Are You Overpaying For Alphabet Stock Versus Its Tech Rivals?
- Summary: Questioning Alphabet's valuation relative to rivals, implying a medium‑term headwind.
- Date: 2026-11-19 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxONVlvbjZ1S2xjMEFSTy1JNmpxdkV5V0hiZFVHZjZvRzFmOUxZdU91X01sWTI0eVZBZFZ5dkFuQl8tYzBzanoxdmlzcGFkbVlsd2Q1aXNzTGpjb3ZfNlYydndfX0hHblFCRVVrSzVfX1Z2bnEwQ3pVVmx2eE9xOGRmM213NklQZXlUcjFJTC1TeWkwZHFpalZTUGxoZ1NrWFc3U1lfaGd6R19qUkJRcEwtaG5YbG5sY3RZWUVRX0NBOA?oc=5>

### What Is Going on With Alphabet Stock on Thursday?
- Summary: Uncertainty about Thursday's stock movement indicates a short‑term headwind.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOMzhJZS01TjVTR1hTOUs5TTVxYzcwT1hOZ2xvV1ZMczBtTGpyRHVVaFFadG9mLUxPN1NGSW9sSl8xNHZDeWdUVFdheVZiQktxMXQ0bThsU2lpSjdUU0VUM1lHTTl0ZGFEVGp1LU1RcUtuTkZBcWR5SERfR2pIMUxCSWVScnc2cXZ6el9uQWdXaG4wdC1mUUluUmxGdmt4R0JTOTVhMlVR?oc=5>

### Why Isn’t Alphabet Stock Taking Off After Reporting Record Cloud Growth?
- Summary: Alphabet’s stock underperforms despite record cloud growth, indicating market skepticism.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNczRFYUN1ZC01a2hTT29CdmNSSFZFeVBKdW11Sm9FTEZWa0l5UC11emJGcWZSNExwSlBZcFc1ZmU4V0JUVHRJZmhsSXB2cDhncV9QckVuMF94T0F4a2UxeDBXMW9qSXkzU2QwdUhJNnBvWEtzUjFlUmlzWjUzeFBMUW1rRXdDN2lSR3N6RnA0MGtGSG8?oc=5>

### Alphabet (GOOG) Slips as 2026 Capex Outlook Rises
- Summary: Alphabet’s shares fall as higher 2026 capital expenditure outlook dampens investor sentiment.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNcHlQUHNhX0pyNGVqNUdLYXdETWRZai1UMzZPODJVWllENWFiNHE0MWYtcVlnTEZLZHJmZG9VVUZpYk9yOFNYV0RfX3pqTUlPVzBBRlZCZ0lVeGxXMXVFbzQtQWtCSmcyaUZQV0E4VC1DV2gzclNLQVdPRU1EdW9zNWhBdmNLSkVGRmdkdmwxZHdXR3NhbUhmOVVKRQ?oc=5>

## CATALYSTS

### Billionaires Walk Away From Alphabet in Q3 - Hedge Funds Google ‘How to Sell’ and Hit Enter
- Summary: Billionaires sold Alphabet shares in Q3, indicating a sell-off trend.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNRXZTZTloS1R1S25oYk4zWmlNLWZQT1Zudi1hYl9rUEVpSU0wbjFCQW5xSEpoNTQxam9nVDBxQVN5ZUpnbWQtUkRPaHBhaFdtMmZ4bzR2aHNlWVpWRmV4VGVBMGxRaEdaZmFaSXIwdllMU1hlVDRMZjBNNDZzbEN0YmNJNl93UHhZQWVWVDJ2aS0ySjVWMzczQlFrNVVlUQ?oc=5>

## RISKS

### AI Spending Could Be A Big Test For Alphabet Shares (GOOGL)
- Summary: High AI spending may pressure Alphabet's shares and affect profitability.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQWlFHbk9ZaEdmYTk4ZVFTbFFOeHdWQ2txYm96dHpWREdGVjV4ZGx1SV96anZSYlZua0xUcEhoMXpqXzYyQzViR3huam5pWWVoOGFnSWRjZy1abEhXS2czUnZaczhPZGNXWklnVkYwUm5LdUZfS2h5R3BuMjMzcE1YX0psRUZzSFBOQi1HVTJqNVUyWkdR?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GOOGL** | **14.24** | **5.08** | **17.55** | **24.70** | **3,352,081,989,632.00 USD** | **-6.64** |
| META | 20.34 | 5.59 | 13.40 | 26.10 | 1,524,082,016,256.00 USD | 3.48 |
| MSFT | 26.01 | 7.87 | 18.33 | 18.80 | 3,700,472,676,352.00 USD | 3.34 |
| AMZN | 20.81 | 4.53 | 16.19 | 12.10 | 2,782,977,327,104.00 USD | 15.57 |

Peers fetched as_of: 2026-11-19; GOOGL reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-29
- Revenue (latest available single quarter): 127,577,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 26,468,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMieEFVX3lxTE10WDdwclZjV3ltY3NHVm9ia044N0huUnBJZGgtN1FkalNkajRpS1R4XzFjYjg3ajRXS0hwWDdvbHdPQ0k5eWxhSHBuOS1Da2x5S285MFJ1QVVwN2Nob2pLQlZmYVlwQ1ljT2VOaXBPMWMzU3dkaE5Wbg?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPQVNmZHh0Wm5WUnhuTFI1WU9pRlIycURsUmprUW9RYkZNSVhub3RvNUdSLVNGY2I0U01nbG9zQ0w3RGhWYzJTZ2tqLTRnVHVLOUxrYVpyUmJKMG14bmlQYjNFanFNcE14ZmlLY2NkbUVyamlQUHJ4TEFodGx5ZDZCbDZXWHN5TWJEakI0NTItNnZLc1k?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPN0s1WHI2clhqM2U3Z2NBOWVXcmFUdmR5ZzRDbGVQVWtCTkFic2YwZWFpb3hTRE1JSXRDOHd4NHhKZzFvazlGWlJXVDJpUmRydUhZc2RyUHhTSVJ3YWIyMFhKWjg5ZS1uR0hsRnFvX05hVjJRYnJEZ2ZFVTBpTkNlSUQ0QUlnVUZYbkZabUMwU2lucmUyNlkwalRZSUU4SjczM0dxaXJMUEJZRmR3VWhMNA?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxNd1NpVlByZC1xZWxaeU1lbVc5T05GWGVqUDdkcXUxTmt5NXNyUHo5c3ZGaEM5NHExYVZ0UC0xX1RpbDU5WlBlUEY0RG5VdTNmZ0JWQkNlS04zNmJxcmtPb01FX1g2cTdPNHFJYmNSWnZRQ3dxTHFBd0E1a3N1RjlXMTFtdzFteE3SAYwBQVVfeXFMT3drcmRET3BhVThONnRna1oyWGQ0aHpabjM5cVRuUVJkM2JJSWJmcHUwWTRvWG50YlVtWXNDUFBYS3Y3VXhhR2swZ0dQdVBaeEY3TmhWaXNkUU53N2loaXdZMTFRQjlQQmFfMnRiVzlORVV5RUxCSFltajhXZnJKVnhnTW9oc25ueXB2OFo?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxOYnNCbDJDZEN2TjM3VE9qakJEWTlNdlFMQjZkVUZDVGllanRtRWhLMHlXQUd2dTV3UHFMQTgwQVRJUjJ6RWF6b0UtbF96c21DZG1fSEpfRktjTjFvdGZnazZnRVRtbTk5UWFQeXJhZzE5Zi1NcEg0Sk5FMlB4MnUtaDJqeVpwb1U?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNNkJZTFlxSDA4eURKd2lBVEloR3FmMUUwU0M5U19hN3Q2Rm0xSURyeGFjSjFfNE54eGNKTzAwQ2J3TlpVUkpSV3JuN0Y0X3l2UlUxRlRzeXpNZkJfa180MFFZMHVWTTJ5M1R0RFEtckFHSnBwS1l2M05ucnZ6UEpGU0NBZG1kZEcyR0JMZlUzUWp0Z0p1TVJYVTZBblIxQW8wRGR5SVJra3hGdHRPVnRkNExKZzZlR25GQUE?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNZ1Rpa1o2S3NHZU9kcEUtdUtaWENWd3JZTmZ4SkZhdF9KQ3pkVmRLZWo0c1pGc2RrWDRSTW5LRWxITi1PbFpZVlpPbnVMeUM1UEtjeUVGVGhybnU1Zy1NLUs0M2FSR3RJellkTlNfZGNJX3JGUU5tZlFqMnlTTjRPMlIzZnQtbHI0bWc?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxOTUpFZU5IMm8xb0NpX09XTnlsTzlPOEg4WlZSUjQxOTdBcEZHTkFFTWwyQVhoVlAxQjJlSWNPX0gwQ2xLaVJjdTVUdFFBRjFsekQ3OTQxZEpFcVYzcXBxNkYxN1UxczRkWXBWTENTc2VpSU5odWp3UE51LVp3NGV6cjJScmN4ZzNkZms1akZQMWZibmVhbW1VaGNTcm5HdEZBTkIzWU1nNHM4b2FCSVpFdUxCN1VrekZNRlhUMmpCZ3lYNi1RbkpRa0xLY0pJb0xE?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxQem5kdTNnLWkxWjFsM3dqMF9xYkwxZ2dkbkR0d1V6TFo5dkJaMnIwMzhGbEhORmprZVFHZmhpRlI4VDFVd09SWWp6ZkpZSjdycTY1VjNseUwyWlpFRHRKRHI4X09kcWs3ekdPLUpfREtQM3ltWnRpS3g0dDE0SHpFZnZR?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOYU1Lcy0yRzhtLVRmZ003M0VQVVJTbUF3ZEFXMVItd3JjdElrZVdYalkzWjNsVXNvaDkzcHYtZHBEWnRVREw5T2YzaHZNUEQtRVJEeVVWUlE0WDUwMF9PXy1zS05FMFlaS0Myc3ZCVHFWVmVsYXd0VXBHQl9qOXhXMFFNQm9iaWUtbjl4VW9ZUFg1Y3VnSWIwZHl6c2dscnNUMWhFRklQZGc?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQaV9WVUdzMk5hM0tDU1FaeFB0dkpRenRRaUFFWWdFaVZCVUdpT3hVc3cxeWZfeTlQNjVBVHJjRzdxS1dsclRZeHBIblVhQWkzMEliOU5vUzVFODgtQUI3VHJjVnVVZGd4V1lnNUVvWVdBc0hzUW5wX1JlZ2FMV0hVOXViZEFfTE1WcDFpVE1ySXRrZkVGRk5F?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPd3c1Y0FKdVByU21IUFJZTzVKNkNaYWs2S1VSVExMLURtWFhxLVczRXVjaGpsUWp0NzlmZU5GVmNoN2lBMHVoSU4zWDVPcG5IUENrNEVRRngwNUpmREJRWFh6bHRnamN0MlpYaENFZ2V2dWFHOHZlUW93MmxqVEd2eFZyeGJCRmV0UW5USHdWdHBNeGF6cWRSMS1hMDhOYmtpU1dF?oc=5
- https://news.google.com/rss/articles/CBMi-wFBVV95cUxNYUZ3Rm82c1V1TW1rd1lFUTRYM2s2LWJvSG44OWJOTHZ2UEkzNnkyT2ZPZjFES1FjclE0WWYyNkZlWm9DT25xTEIta1JzNzVXLU9ocVF4VVZ1VUVRWmhfQ3JKazNPUjY0M2lEa0lncE1PLS1uTGw4Nk9BdkRWdVk1aWQxT0RlTEVQUEhQT05GWktVYkl0Qk5RSGdWWkNmeEF1Q0JDZVhaQVM2VVk5d2ZmXzVtYXdxSWFPWHR4YWRZemo0Sk9HcFFxWWZrUGVBeS1DcjZnVkJxNzBGRnl6ODVyZ1BSSnByX2ZxM3dEX3BLaWVoZl9hb1VNMHVmOA?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNT1ZWV245S1M1R2I2RVIyNHprYlZwcGN1eGlRWE9ZNTJYd0Q3V2xyb0FFZWdNcFRhVHVPVUtKdEdrYmd4bDlNbkRkdTNFazJLUU1wS0g1WlVFd3U3YU1pbkl4R09QVmFkVEZYMTNjU1FJbnU0bGY5Mk9zNWxFcWV2Y0h1aDF1aGlnYjBmNk53LU5TaHVwdTBmRjd3?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxONVlvbjZ1S2xjMEFSTy1JNmpxdkV5V0hiZFVHZjZvRzFmOUxZdU91X01sWTI0eVZBZFZ5dkFuQl8tYzBzanoxdmlzcGFkbVlsd2Q1aXNzTGpjb3ZfNlYydndfX0hHblFCRVVrSzVfX1Z2bnEwQ3pVVmx2eE9xOGRmM213NklQZXlUcjFJTC1TeWkwZHFpalZTUGxoZ1NrWFc3U1lfaGd6R19qUkJRcEwtaG5YbG5sY3RZWUVRX0NBOA?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOMzhJZS01TjVTR1hTOUs5TTVxYzcwT1hOZ2xvV1ZMczBtTGpyRHVVaFFadG9mLUxPN1NGSW9sSl8xNHZDeWdUVFdheVZiQktxMXQ0bThsU2lpSjdUU0VUM1lHTTl0ZGFEVGp1LU1RcUtuTkZBcWR5SERfR2pIMUxCSWVScnc2cXZ6el9uQWdXaG4wdC1mUUluUmxGdmt4R0JTOTVhMlVR?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNczRFYUN1ZC01a2hTT29CdmNSSFZFeVBKdW11Sm9FTEZWa0l5UC11emJGcWZSNExwSlBZcFc1ZmU4V0JUVHRJZmhsSXB2cDhncV9QckVuMF94T0F4a2UxeDBXMW9qSXkzU2QwdUhJNnBvWEtzUjFlUmlzWjUzeFBMUW1rRXdDN2lSR3N6RnA0MGtGSG8?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQNWZrNjlHZUNBYnlqWF85WFkxSXZHRmxaOGJNZ05lTjhlREFqOC1Xd19qdTBEdGVLUzNpN0pVOHVLYnc5SkNQRGhubXpYdFNlYUpycnBhQ2h5WlhEY0tBUGxQLW9ldkNKU3FHejlkbHZXRTFUbTViTW1uNVVMdi1RTVdfRUZMZ1c4VmRMdHk2RnV6MUFRN1l1SFlHN0tjSW4zQmg0eE1NVDBTZG9oSHJSZkN3MFk?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNcHlQUHNhX0pyNGVqNUdLYXdETWRZai1UMzZPODJVWllENWFiNHE0MWYtcVlnTEZLZHJmZG9VVUZpYk9yOFNYV0RfX3pqTUlPVzBBRlZCZ0lVeGxXMXVFbzQtQWtCSmcyaUZQV0E4VC1DV2gzclNLQVdPRU1EdW9zNWhBdmNLSkVGRmdkdmwxZHdXR3NhbUhmOVVKRQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNRXZTZTloS1R1S25oYk4zWmlNLWZQT1Zudi1hYl9rUEVpSU0wbjFCQW5xSEpoNTQxam9nVDBxQVN5ZUpnbWQtUkRPaHBhaFdtMmZ4bzR2aHNlWVpWRmV4VGVBMGxRaEdaZmFaSXIwdllMU1hlVDRMZjBNNDZzbEN0YmNJNl93UHhZQWVWVDJ2aS0ySjVWMzczQlFrNVVlUQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQWlFHbk9ZaEdmYTk4ZVFTbFFOeHdWQ2txYm96dHpWREdGVjV4ZGx1SV96anZSYlZua0xUcEhoMXpqXzYyQzViR3huam5pWWVoOGFnSWRjZy1abEhXS2czUnZaczhPZGNXWklnVkYwUm5LdUZfS2h5R3BuMjMzcE1YX0psRUZzSFBOQi1HVTJqNVUyWkdR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
