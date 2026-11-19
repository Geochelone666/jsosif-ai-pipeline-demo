# CAT Intelligence Report

- ticker: **CAT**
- Report as_of: **2026-11-18**
- Market data as_of: **2026-11-18**
- Quant sources: https://finance.yahoo.com/quote/CAT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CAT/key-statistics/
- AI analysis snapshot as_of: **2026-11-18**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-19T05:57:04.951586+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 5, 'ai': 13, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/CAT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **5**; {'directional_claim_without_event_type': 2, 'low_uncalibrated_model_confidence': 2, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 18 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-11

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 558.7700 |
| Return 1D (%) | -2.1058 |
| Return 1W (%) | -7.1209 |
| Return 1M (%) | -23.3539 |
| Return YTD (%) | -1.6318 |
| Return 1Y (%) | 3.0430 |
| Annualized volatility (%) | 41.7051 |
| Beta vs SPY | 1.8466 |
| Max drawdown (%) | -47.7898 |
| Sharpe (rf=0) | 0.2803 |
| Downside deviation (rf=0, %) | 29.6161 |
| Sortino (rf=0) | 0.3947 |
| Historical VaR 95% (1D, %) | 4.3476 |
| Historical ES 95% (1D, %) | 5.8406 |
| Correlation vs SPY | 0.6091 |
| Tracking error vs SPY (%) | 35.0661 |
| P/E (trailing) | 21.93 |
| P/B | 11.90 |
| EV/EBITDA | 17.33 |
| Revenue growth (%) | 17.30 |
| Forward P/E (estimate) | 17.37 |
| Gross margin (%) | 29.54 |
| Operating margin (%) | 18.76 |
| Return on equity (%) | 56.14 |
| Free cash flow yield (%) | 1.55 |
| MA50 | 724.5303 |
| Close vs MA50 (%) | -22.8783 |
| MA200 | 802.6748 |
| Close vs MA200 (%) | -30.3865 |
| RSI (14, Wilder) | 29.8808 |
| MACD (12,26) | -46.4057 |
| MACD signal (9) | -47.4854 |
| MACD histogram | 1.0797 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CAT': 285, 'SPY': 285}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 558.7700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.1058 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.1209 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -23.3539 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -1.6318 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.0430 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.7051 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.6161 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3947 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.3476 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.8406 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6091 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.0661 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8466 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.7898 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2803 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.3653 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 29.5420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 18.7610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 56.1350 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.5539 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.9297 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 29.8808 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.0797 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -22.8783 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -30.3865 -> Clearly below the moving-average trend level.

## TAILWINDS

### Caterpillar Stock Offers a Backdoor Route to a Potential AI Recovery
- Summary: Speculation that Caterpillar could benefit from AI trends, suggesting future upside.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQbndQdmY0Rld2RzhjdFZEM3dac3l0NHN4OXlWTlRxRzZsT3hZM0VWb2JNMWFpRVk3MmtBS2pMdnZXM1hfS2NSYUw5YjVOcUY1TEV6NTVGVVZJYTN5ZVQxaGdxX0pkRlRrd1A0MWp2cGF0Qi1DaDFSMXhtWE5rNGFJbHlRb05kSFpLUDFWYVdQWHhEV3JYcDVfcHhzR3BBX0IyV2ZwZmFCYUFuR1lNdk9Tbnh3?oc=5>

### Caterpillar Sees a Bright 2027 as Compact Equipment and Rental Expansion Gains Ground
- Summary: Caterpillar forecasts strong 2027 growth driven by compact equipment and rental expansion.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNZTlxbXp6T2VkTWttbVdsUFYzRU5TdWVqaERTUGFySnlBSldYQ3pMSXk4ZWRXQ28xSGpBUGlIR3hIVzEyVUNsMHQwV21LYmFrYXNXTHVzY3k3Wi1wTWZnQVk3SjVkNERXWnFIZm1ocExzQmhlck5IWW1kVzBIUjhjODFtZlpSUHBaWjJ0c1RjWHhZYmIzOHNtVVVSMkFBR2dfV1lr?oc=5>

### Caterpillar (CAT) Stock Looks Like A Bargain On Its 222% Run
- Summary: Positive view on CAT stock, suggesting a bargain after a 222% run.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQZHVXQm5YSjNZLU9OdHJaU3E2blFWOEI2LUM1ajR0eTlOOVNxVlAtcERmRmp1c0hZYXJEZl8zVkhYLUlHV2wxUk5OZmVqN044UmROeklfV1NHRWwwZV81amJCdEZKNDFGcXdyODc0T2thTkR6a0tLSV9faVg3dWpVYlhKSk9CY29OLVZSRWl6RnJhbzFWeHNRZURXeWZYMWtwSmc?oc=5>

### Kevin Simpson Is Buying More Caterpillar as an AI Trade That Isn’t Just AI
- Summary: Investor buying more Caterpillar shares.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNZ01vSll2ay1obGVvUFhneVdTbDJUY1hWeFFuSU5xY0hIZFhtVXJvdnU1SGdpVlk4ZHYzSlpfSjV1Vkw3b2lwQUk2VkVxYThkX2Z3WjZMLTlQSW1uU19SN2VqODUxQ2s1d1RVS1k1anpTMXYzaU5JLUl1c2VkOXZMSHR4SUZndmdrYjB4SFZvOEpnbU9nVElBRV9IRXMtbXRjd0sxTw?oc=5>

## HEADWINDS

### Caterpillar shares technical analysis: Downward price move highlights seller pressure
- Summary: Caterpillar shares technical analysis: Downward price move highlights seller pressure
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQYTlzS0NlZFhxYVZEamdlU3B3ME5zRm53ZEpSaV9vNEdJVlZBNFJJLVFFNFFGdTlmTmRtQzI4MFpBbU9xVE1hakpHQjU2MjgwLVFxTHloX2hEQUd3S3ZJTU5sVkw2RUhSOGJWa0NLMDhwT082OWRxb3Jpb01qNVotbHRpWURtR0tubEF6NnN5bE9uWFlPY2c?oc=5>

### Caterpillar Shares Slide 10% in Worst Week Since 2025 as Burry Exits Bearish Bet
- Summary: Caterpillar Shares Slide 10% in Worst Week Since 2025 as Burry Exits Bearish Bet
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidkFVX3lxTFB6U3BIcEFrVmhLS3gxajV6U2VjM1cwVW83a0c2SXVvNVotaURhSjRkeUs5eFltWGpKZksxeUQxN2k0N1VfOFMxc3NyNTNSUC12MWZfZFNJS1l5dUU2Sm5Cc1pHWkVBVG5seW4xTWpqU09sNkZSaHc?oc=5>

### Michael Burry Cashed In Caterpillar Puts After a Nearly 4x Gain Even as CAT Stock Fell 10% in Its Worst Week in 18 Months. Is Caterpillar Still Overvalued, or Did Burry Just Lock In the Easy Money?
- Summary: Burry’s exit signals potential overvaluation concerns, adding downside pressure.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi1wJBVV95cUxQRzlMOWd6Y3BEaDZVeDkyWG9Jd2xuMlltLVFyRnJ1cVhsR2RDcjdSZ0FtRXNnZDloOEF3TlUyTWZpQVk0Q2xaXzBBUEhHN2l1VmVEZk1Ob0FPOE11MFMwc0E0LXpuR3VLYzY2dVBpcDhnRW1iMHlLUkJ2elQxQkc1YmNQTlgtMVJ0RTZnTWZGUkIxd0x2LXhfbklHVnJEZm1taE9vVlJ3SEk4Q3lPRGlZYlRiTzI4bm5KNUxoQ3NGQ0tubmRsRUE4RjF4UGNUQzQ2bk5IdU1qTTZRY1B5UkN3X21qT2k5OHJhc0pyUU1ndUsyXzlOTDJ5QVhpWDRUVWdQZVFLRlBja2lCelV6Tl85aVlPajROUFAtSWpfM1l6N09ncVVIcnhKX1dZMF9oZFh0MDZIQXN0T3VlelNCUmV4ODcyTHdzZUM4el9hdjg4X3JodExGVVdn?oc=5>

### What Has Changed In Caterpillar’s Story?
- Summary: General inquiry into changes within Caterpillar.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPOTh3QWM3QXRrNERSNmV3bG9oWnM2eGxCSHBDbXpPNWctTUw1bms3RjhVNlZhNGZTaEdQdk9hYmFtV3ZtT0Npb2lJbEZwSXhWN1U3OV9Pand0Z3k2aEpiWUFnSHhNcjNSM2dvQVFObTFkSHhXQTc5ZGhSZ2l0bzNUemxCRFA4c0lyeW95b1UxZlZNZlByX3JYcnc3U1JoWG8?oc=5>

## CATALYSTS

### Caterpillar (CAT) Stock Fair Value Falls As Analysts Cut Targets And Lift Rates
- Summary: Caterpillar (CAT) Stock Fair Value Falls As Analysts Cut Targets And Lift Rates
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxNTFZpMTVKelRubDFSaEtOVUthOG5RcDc3a3FjZFg5U1FoeGRNMTAza1J5aThiazUtaV9jcXMwU2FXMnRYQkNMNGd0MjBkWjhlcGFtUUNlNGFZQ08zS2dVdzRtWk1McVJqdDFuQi0zZnd0aTh6aDdwdVVjc2JYQ0JwSVRsNUktWWhQ?oc=5>

### Caterpillar's 'Best-In-Class' Construction Business Is Getting Overlooked, Analyst Says
- Summary: Caterpillar's 'Best-In-Class' Construction Business Is Getting Overlooked, Analyst Says
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8AFBVV95cUxPeXU3amNFLWRaME9qcldkVG14Y3VKdUs1NWE0SHNJUTAxLUlnRW9xaVc2RmY0dlVyWjhYWmtmc0NackJFZUhCUjF5ZWlUdU9Ia2M0a21ad0pJMXZQYVVMMnY4T3RTWmstZm41eVdoR1U3REVfbnhReHJ6NHZFY1VhcG0tVk1Ldk1XTEtFNW8zYjFJdS1IOVJ3d2hZemFSeHZPNVg5YVZRbi1abFk4bkFvWHhsZ3JNWFhUODQ5aHl6YTZVRkdRNXZtRlUxS1FJUnBERFZ3NXByU05HX3JGVkM0bDFNcDAwcTRVVW0zaXZodmg?oc=5>

### Caterpillar Stock: Analyst Estimates & Ratings
- Summary: Caterpillar Stock: Analyst Estimates & Ratings
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNbmZLRjRxUEVrLTIyTVpyY1FzNWZPOGtDZ2xvVjktNjdseHlyTnhfMUtBQzNJSkp5aXM3Vi1aS09TeTJBMGNxcFc3bEkxaUluaVRFdEhzMHlBeWdKOWpXNWZZcVdDWGJYX0hfTE0zYUdTQ3phU0ZwemRVRmhNcGNfVzlrZHR6NWROZ19GWkpTbTU?oc=5>

### Caterpillar’s 34% Slump Over 6 Months: Wall Street Desk Says It Sets Up 90% Gains Within a Year
- Summary: Duplicate of previous forecast, reinforcing potential upside.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOR3RwVnFOZ0M3eWlCbjUybklZQ3BqRDBxVmY0ZE5lb1RKYWY5dW40M0UtV0lMNkM3c1V6VkI3VXhMU1U0TXFRTzZMdWdjek95ZFlGRG1TNVotVDlZRjE5MGV6aVRfQWNrQXFRTHE4T3VUMlRvTi1WQTRQSmRYNDV4V2toRUhzakYxVVJBNFF5QjlGVEtqWDlZ?oc=5>

### “Trades Basically Like an AI Stock”: Caterpillar Just Dropped 22% in a Month. Sell, or Load Up?
- Summary: Caterpillar shares fell 22% in a month, prompting debate over selling or buying.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNTmViZ29WQlB0OWE0SGtrNlhJdTZNU3pNeWxGUXc3SVVXSHJ0VGk2QVM5MHgxdjZPRlh0ZEIzVkhSMFhMbmduSFVzTVB2UTdmQmZEcmI1VThockZRMmszZjBvQ2N6bnVnR3R2RmhURjhHQ3paWXE4RWlNZkdkZnMwMXBCX2N5RndBM1RNUkVYSllubzJreGxlTmRObGh5NlVWVTVzVGFZYWVpeWpPSm5TUEVRRTRtdw?oc=5>

### Caterpillar (CAT) Adds Safety Tech As Investors Ask If The Story Is Already Priced In
- Summary: Caterpillar introduces new safety technology, potentially enhancing product offerings.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxOdEVkd2UzcTRQV3U3U1hQRFVVY0FtbVY0SWZmWGxFSk83VHZNVk1HQnY4VkE5RWxzcVBpMnJhdWNzc2FqeWQtNWJmMElBU3M2ZmNwZkh4U1Q1dEp1THVkN2FleTEyUW5oQ3EwdGFrcnhyanVJZzNrSF9XdGNnUW80aWNVd3VCeEMwV1BXX19SQUQ2NXFScVBBVzZRdnlnWUFrT2lPbWtIM2tFekFLdDNlLXFubWw0ZGZCem5SMTVtNnR3Vk80bWtpak1GcWXSAdIBQVVfeXFMTnMxZGZKNW85TWVWUms3aVBuVEtaX3pnSWxYMXE2bzNrTm5JWTZhOGFoOHpRcDQ0cHVrT0t2cmZMcWE4cklvdzRCaHcxdEJjNUg3QWZaNkJEN3ZXRF9rNENod3k2UTduMjk1YUt0UEFGb0o5R09jQWpCNGkxY0hRRFVYRGxRMFY4WTB0UDdmNGhCQnI0NXp3QnVIYzV2Ui11UDIwWndEUlAyMDJISDlPc2lfUHNnOG1WYmp6N1ltaG9jM1AwZDZyWmgzZlJ4ZUY2bXBn?oc=5>

### Morgan Stanley sees Caterpillar rental gains, stays cautious
- Summary: Morgan Stanley forecasts rental revenue growth for Caterpillar but remains cautious about market conditions.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQNlliRkI0Y1l2QlJBWlF3TGFsU0VxS1NRWFhvcHNLT2NYUDdJcW1IYl9CWGxWQ2NOWTVFZWlKaFRtZHF0UlJQME1FcmFGTnJlZnAxWm9xY1NvM0ZWOWpuREZUZXB0TlFMMkl6N2lJVXctck5UaW44Ny1MNEozc3QtWF93SDRmdy1TVEM3OXFEYXEwX3NpM0VFb3JUSkFZdDE2YVBIcQ?oc=5>

## RISKS

### Caterpillar Slides as AI-Linked Industrial Trade Remains Under Pressure
- Summary: Caterpillar shares fell amid pressure on AI-linked industrial trade, impacting investor sentiment.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQVXJCOEhNZ2xRLXZ2bE83c0NkWmVDdUp3Z0gwbjRreEQ3Y0NWdm96U3NvZ1FrLUduaDhjZWw4bDNHWXlIZ2UxcGxUQmR0YU5jaE9GcFhvQ0JQZlN4QmFybHNQdVZrWFlDNDVmVU1RUlc1dk8yRk5jakZuNjljMkppdUx6Wl9YUG8yX1RnelVGWlFkMzVoYnIwa1NjTlJ2RHdqdDFpdGs0Yw?oc=5>

### DA Davidson reiterates Caterpillar stock rating after compact event By Investing.com
- Summary: Analyst maintains rating following a compact event, indicating continued support.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxPb1lpdHQ1VnRpZUhJWVdMMWJzR09YVUZHOWRfOTNtSDlQQjl2Q1RWMkUxUVBnNExFNVhDQ2xscThNU1QyQWtuMV9EX1VQREdxSjZKTFV6WTkyMFlfR1BidWs5eGt4d2U3M0h6bmF2TGFyeXk2dU9DOF82Z1VJekVCdzkxbktYMFRJcm11cVB1TDV3RElpZlA2VnVHd1hKN0tYNlZObVoyamxMM2luNUQydVh2d2Y2RFQxU3lIa2RHV2FlNkJWZWYw?oc=5>

### Caterpillar’s AI Boom Went Bust. Why Smaller Equipment Could Spark a Comeback.
- Summary: Caterpillar’s AI initiatives underperformed, prompting a shift toward smaller equipment solutions.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQQ0hEY1l3VzFNUlBaOVdPeFZ3bG1kbGNyT2xYLWNhVEl2Zi1Rbm13X2R2V2FGRVdQLVFpbkdNejZVc1djZkNZWjUwOS1IT0hEWm51MHBOY3JiSUMwTmlCRzVHM1ZCdllOVGUwVnZqbDBPdmNvU1cyOXVpSTRTXzRoOXJFVUdyV29Xa0F1YzIwVWczUUo0NWNOWQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CAT** | **21.93** | **11.90** | **17.33** | **17.30** | **255,689,900,032.00 USD** | **3.04** |
| DE | 35.84 | 6.21 | 26.92 | 4.90 | 173,840,973,824.00 USD | 37.62 |
| CNH | 53.52 | 1.78 | 35.24 | -1.00 | 18,049,714,176.00 USD | 19.33 |
| CMI | 17.82 | 4.39 | 11.85 | 13.50 | 58,520,920,064.00 USD | -6.78 |

Peers fetched as_of: 2026-11-18; CAT reuses existing data (market data as_of: 2026-11-18); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-18

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 20,682,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 1,141,000,000.00 USD; period 2011-07-01/2011-09-30; fiscal year/reporting period 2011/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/18230/000001823026000057/cat-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMisgFBVV95cUxQbndQdmY0Rld2RzhjdFZEM3dac3l0NHN4OXlWTlRxRzZsT3hZM0VWb2JNMWFpRVk3MmtBS2pMdnZXM1hfS2NSYUw5YjVOcUY1TEV6NTVGVVZJYTN5ZVQxaGdxX0pkRlRrd1A0MWp2cGF0Qi1DaDFSMXhtWE5rNGFJbHlRb05kSFpLUDFWYVdQWHhEV3JYcDVfcHhzR3BBX0IyV2ZwZmFCYUFuR1lNdk9Tbnh3?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNZTlxbXp6T2VkTWttbVdsUFYzRU5TdWVqaERTUGFySnlBSldYQ3pMSXk4ZWRXQ28xSGpBUGlIR3hIVzEyVUNsMHQwV21LYmFrYXNXTHVzY3k3Wi1wTWZnQVk3SjVkNERXWnFIZm1ocExzQmhlck5IWW1kVzBIUjhjODFtZlpSUHBaWjJ0c1RjWHhZYmIzOHNtVVVSMkFBR2dfV1lr?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQZHVXQm5YSjNZLU9OdHJaU3E2blFWOEI2LUM1ajR0eTlOOVNxVlAtcERmRmp1c0hZYXJEZl8zVkhYLUlHV2wxUk5OZmVqN044UmROeklfV1NHRWwwZV81amJCdEZKNDFGcXdyODc0T2thTkR6a0tLSV9faVg3dWpVYlhKSk9CY29OLVZSRWl6RnJhbzFWeHNRZURXeWZYMWtwSmc?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNZ01vSll2ay1obGVvUFhneVdTbDJUY1hWeFFuSU5xY0hIZFhtVXJvdnU1SGdpVlk4ZHYzSlpfSjV1Vkw3b2lwQUk2VkVxYThkX2Z3WjZMLTlQSW1uU19SN2VqODUxQ2s1d1RVS1k1anpTMXYzaU5JLUl1c2VkOXZMSHR4SUZndmdrYjB4SFZvOEpnbU9nVElBRV9IRXMtbXRjd0sxTw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQYTlzS0NlZFhxYVZEamdlU3B3ME5zRm53ZEpSaV9vNEdJVlZBNFJJLVFFNFFGdTlmTmRtQzI4MFpBbU9xVE1hakpHQjU2MjgwLVFxTHloX2hEQUd3S3ZJTU5sVkw2RUhSOGJWa0NLMDhwT082OWRxb3Jpb01qNVotbHRpWURtR0tubEF6NnN5bE9uWFlPY2c?oc=5
- https://news.google.com/rss/articles/CBMidkFVX3lxTFB6U3BIcEFrVmhLS3gxajV6U2VjM1cwVW83a0c2SXVvNVotaURhSjRkeUs5eFltWGpKZksxeUQxN2k0N1VfOFMxc3NyNTNSUC12MWZfZFNJS1l5dUU2Sm5Cc1pHWkVBVG5seW4xTWpqU09sNkZSaHc?oc=5
- https://news.google.com/rss/articles/CBMi1wJBVV95cUxQRzlMOWd6Y3BEaDZVeDkyWG9Jd2xuMlltLVFyRnJ1cVhsR2RDcjdSZ0FtRXNnZDloOEF3TlUyTWZpQVk0Q2xaXzBBUEhHN2l1VmVEZk1Ob0FPOE11MFMwc0E0LXpuR3VLYzY2dVBpcDhnRW1iMHlLUkJ2elQxQkc1YmNQTlgtMVJ0RTZnTWZGUkIxd0x2LXhfbklHVnJEZm1taE9vVlJ3SEk4Q3lPRGlZYlRiTzI4bm5KNUxoQ3NGQ0tubmRsRUE4RjF4UGNUQzQ2bk5IdU1qTTZRY1B5UkN3X21qT2k5OHJhc0pyUU1ndUsyXzlOTDJ5QVhpWDRUVWdQZVFLRlBja2lCelV6Tl85aVlPajROUFAtSWpfM1l6N09ncVVIcnhKX1dZMF9oZFh0MDZIQXN0T3VlelNCUmV4ODcyTHdzZUM4el9hdjg4X3JodExGVVdn?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPOTh3QWM3QXRrNERSNmV3bG9oWnM2eGxCSHBDbXpPNWctTUw1bms3RjhVNlZhNGZTaEdQdk9hYmFtV3ZtT0Npb2lJbEZwSXhWN1U3OV9Pand0Z3k2aEpiWUFnSHhNcjNSM2dvQVFObTFkSHhXQTc5ZGhSZ2l0bzNUemxCRFA4c0lyeW95b1UxZlZNZlByX3JYcnc3U1JoWG8?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxNTFZpMTVKelRubDFSaEtOVUthOG5RcDc3a3FjZFg5U1FoeGRNMTAza1J5aThiazUtaV9jcXMwU2FXMnRYQkNMNGd0MjBkWjhlcGFtUUNlNGFZQ08zS2dVdzRtWk1McVJqdDFuQi0zZnd0aTh6aDdwdVVjc2JYQ0JwSVRsNUktWWhQ?oc=5
- https://news.google.com/rss/articles/CBMi8AFBVV95cUxPeXU3amNFLWRaME9qcldkVG14Y3VKdUs1NWE0SHNJUTAxLUlnRW9xaVc2RmY0dlVyWjhYWmtmc0NackJFZUhCUjF5ZWlUdU9Ia2M0a21ad0pJMXZQYVVMMnY4T3RTWmstZm41eVdoR1U3REVfbnhReHJ6NHZFY1VhcG0tVk1Ldk1XTEtFNW8zYjFJdS1IOVJ3d2hZemFSeHZPNVg5YVZRbi1abFk4bkFvWHhsZ3JNWFhUODQ5aHl6YTZVRkdRNXZtRlUxS1FJUnBERFZ3NXByU05HX3JGVkM0bDFNcDAwcTRVVW0zaXZodmg?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNbmZLRjRxUEVrLTIyTVpyY1FzNWZPOGtDZ2xvVjktNjdseHlyTnhfMUtBQzNJSkp5aXM3Vi1aS09TeTJBMGNxcFc3bEkxaUluaVRFdEhzMHlBeWdKOWpXNWZZcVdDWGJYX0hfTE0zYUdTQ3phU0ZwemRVRmhNcGNfVzlrZHR6NWROZ19GWkpTbTU?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOR3RwVnFOZ0M3eWlCbjUybklZQ3BqRDBxVmY0ZE5lb1RKYWY5dW40M0UtV0lMNkM3c1V6VkI3VXhMU1U0TXFRTzZMdWdjek95ZFlGRG1TNVotVDlZRjE5MGV6aVRfQWNrQXFRTHE4T3VUMlRvTi1WQTRQSmRYNDV4V2toRUhzakYxVVJBNFF5QjlGVEtqWDlZ?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxNTmViZ29WQlB0OWE0SGtrNlhJdTZNU3pNeWxGUXc3SVVXSHJ0VGk2QVM5MHgxdjZPRlh0ZEIzVkhSMFhMbmduSFVzTVB2UTdmQmZEcmI1VThockZRMmszZjBvQ2N6bnVnR3R2RmhURjhHQ3paWXE4RWlNZkdkZnMwMXBCX2N5RndBM1RNUkVYSllubzJreGxlTmRObGh5NlVWVTVzVGFZYWVpeWpPSm5TUEVRRTRtdw?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxOdEVkd2UzcTRQV3U3U1hQRFVVY0FtbVY0SWZmWGxFSk83VHZNVk1HQnY4VkE5RWxzcVBpMnJhdWNzc2FqeWQtNWJmMElBU3M2ZmNwZkh4U1Q1dEp1THVkN2FleTEyUW5oQ3EwdGFrcnhyanVJZzNrSF9XdGNnUW80aWNVd3VCeEMwV1BXX19SQUQ2NXFScVBBVzZRdnlnWUFrT2lPbWtIM2tFekFLdDNlLXFubWw0ZGZCem5SMTVtNnR3Vk80bWtpak1GcWXSAdIBQVVfeXFMTnMxZGZKNW85TWVWUms3aVBuVEtaX3pnSWxYMXE2bzNrTm5JWTZhOGFoOHpRcDQ0cHVrT0t2cmZMcWE4cklvdzRCaHcxdEJjNUg3QWZaNkJEN3ZXRF9rNENod3k2UTduMjk1YUt0UEFGb0o5R09jQWpCNGkxY0hRRFVYRGxRMFY4WTB0UDdmNGhCQnI0NXp3QnVIYzV2Ui11UDIwWndEUlAyMDJISDlPc2lfUHNnOG1WYmp6N1ltaG9jM1AwZDZyWmgzZlJ4ZUY2bXBn?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQNlliRkI0Y1l2QlJBWlF3TGFsU0VxS1NRWFhvcHNLT2NYUDdJcW1IYl9CWGxWQ2NOWTVFZWlKaFRtZHF0UlJQME1FcmFGTnJlZnAxWm9xY1NvM0ZWOWpuREZUZXB0TlFMMkl6N2lJVXctck5UaW44Ny1MNEozc3QtWF93SDRmdy1TVEM3OXFEYXEwX3NpM0VFb3JUSkFZdDE2YVBIcQ?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQVXJCOEhNZ2xRLXZ2bE83c0NkWmVDdUp3Z0gwbjRreEQ3Y0NWdm96U3NvZ1FrLUduaDhjZWw4bDNHWXlIZ2UxcGxUQmR0YU5jaE9GcFhvQ0JQZlN4QmFybHNQdVZrWFlDNDVmVU1RUlc1dk8yRk5jakZuNjljMkppdUx6Wl9YUG8yX1RnelVGWlFkMzVoYnIwa1NjTlJ2RHdqdDFpdGs0Yw?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPb1lpdHQ1VnRpZUhJWVdMMWJzR09YVUZHOWRfOTNtSDlQQjl2Q1RWMkUxUVBnNExFNVhDQ2xscThNU1QyQWtuMV9EX1VQREdxSjZKTFV6WTkyMFlfR1BidWs5eGt4d2U3M0h6bmF2TGFyeXk2dU9DOF82Z1VJekVCdzkxbktYMFRJcm11cVB1TDV3RElpZlA2VnVHd1hKN0tYNlZObVoyamxMM2luNUQydVh2d2Y2RFQxU3lIa2RHV2FlNkJWZWYw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQQ0hEY1l3VzFNUlBaOVdPeFZ3bG1kbGNyT2xYLWNhVEl2Zi1Rbm13X2R2V2FGRVdQLVFpbkdNejZVc1djZkNZWjUwOS1IT0hEWm51MHBOY3JiSUMwTmlCRzVHM1ZCdllOVGUwVnZqbDBPdmNvU1cyOXVpSTRTXzRoOXJFVUdyV29Xa0F1YzIwVWczUUo0NWNOWQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
