# MSFT Intelligence Report

- ticker: **MSFT**
- Report as_of: **2026-11-25**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/MSFT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MSFT/key-statistics/
- AI analysis snapshot as_of: **2026-11-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-26T06:51:16.890931+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 6, 'ai': 15, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/MSFT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **5**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1, 'short_term_price_move_in_structural_risks': 3}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 17 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 489.9300 |
| Return 1D (%) | -1.2497 |
| Return 1W (%) | -3.4259 |
| Return 1M (%) | -6.4124 |
| Return YTD (%) | 2.1444 |
| Return 1Y (%) | 3.5642 |
| Annualized volatility (%) | 34.0686 |
| Beta vs SPY | 0.9383 |
| Max drawdown (%) | -27.9702 |
| Sharpe (rf=0) | 0.2703 |
| Downside deviation (rf=0, %) | 21.8130 |
| Sortino (rf=0) | 0.4221 |
| Historical VaR 95% (1D, %) | 2.8530 |
| Historical ES 95% (1D, %) | 4.1000 |
| Correlation vs SPY | 0.4112 |
| Tracking error vs SPY (%) | 31.0687 |
| P/E (trailing) | 25.57 |
| P/B | 7.73 |
| EV/EBITDA | 18.03 |
| Revenue growth (%) | 18.80 |
| Forward P/E (estimate) | 20.24 |
| Gross margin (%) | 67.66 |
| Operating margin (%) | 47.10 |
| Return on equity (%) | 34.22 |
| Free cash flow yield (%) | 0.08 |
| MA50 | 518.6444 |
| Close vs MA50 (%) | -5.5364 |
| MA200 | 443.2291 |
| Close vs MA200 (%) | 10.5365 |
| RSI (14, Wilder) | 38.9941 |
| MACD (12,26) | -8.3458 |
| MACD signal (9) | -4.1453 |
| MACD histogram | -4.2005 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MSFT': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 489.9300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.2497 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.4259 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -6.4124 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 2.1444 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.5642 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.0686 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.8130 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4221 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8530 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1000 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4112 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.0687 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9383 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.9702 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2703 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.2419 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 67.6570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 47.1040 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 34.2210 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.0823 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.5705 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.9941 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.2005 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.5364 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 10.5365 -> Clearly above the moving-average trend level.

## TAILWINDS

### Microsoft Stock (MSFT) Rises 0.7% to $496.13 (Nov 24)
- Summary: Microsoft Stock (MSFT) Rises 0.7% to $496.13 (Nov 24)
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxQM0luQzAyX0lFeUV4bmJjZk9IRk94QlJyQms0OTl1SXpmeVBaSDdkcmJqVXF3YzhSZHJVY0xmeC05SlBld1RmbUg3N2ExaDhQa0thLUF6VXVjeDg2dEpQckJaSzhnV0ZDTWdTTzdrY2JyRVRJQndfQVdMdUdRRTlLa1FuLTM?oc=5>

### Microsoft (NASDAQ: MSFT) Stock Price Sits 11% Below Record Highs Despite Monday's Nvidia-Driven Tech Rally
- Summary: Microsoft (NASDAQ: MSFT) Stock Price Sits 11% Below Record Highs Despite Monday's Nvidia-Driven Tech Rally
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxQWk9fMnlSS3RJREZlVExGelNuS0JSNm50Y2EzWHNMNDlMWDNRdV80OXdqRnFNMmJUcEJ5X2VRMDk5Ml82VGs1UUVHalpuYXFDU2lTOVBsU0Y3bUNXV0RuTk5nOVRoajlManhuLVV0eUR4eW5Qai1HY3lGRFBKZnhkRGpRSkdYY2Z5UWRXZUlidWhEajU4MnVuU0ExcjlaQjdIekJkcE9vNm16R0ZkUEpPSTJERi1rXzhMaGJtM1J2d3MzVzZFSmxUY0xMVnpPZ2xOcDdpaDFFQWRwVGdRZzZZbEFoYXo?oc=5>

### Microsoft (MSFT) Is One of the Safest Ways to Own AI
- Summary: Positively frames MSFT as a secure AI investment.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOTGFBVVdNRFBFZE9EWTZDR2tLMFNwTXNEbnMycHhqOElxTnRwYzNjdUxRTlRjVGhLR25QRUxvTUdVNlFlOEhWc2JKZFI3Y3JoN3hIS1hHN25CY0s5RFhpeHE3bGN5LWg3c0VVN0ZhUVRBSk5ZbjRBaEtBS2pIVGtHUlV6a0J0Qy1KOFhJS2xCMXJ1elpScUMtcGVn?oc=5>

### Is Microsoft Stock Stronger Than It Looks?
- Summary: Analysis questioning stock strength.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPSTN0N1hHMGNON3J1ZFRlaGhhZXA4WnZWWlBRRXU2cG9Sd2J5TmVYMGlWSnJ4TWExU0JJaWN3d3RhM0Rja0RkbmhmQkhLMkhkTlFka3p1TFNUUUhQdTRBNWhJMmhYTmY2QU9PZDJybmtoZWEwVDYzY3BDMWMwRUM3Uy1YQ3Rjck10M1dzaWxzRVNQZ05VQ014V2JiTkJqTWZMSURocA?oc=5>

### What Microsoft (MSFT)'s Enterprise AI Partnerships Mean For Shareholders
- Summary: New AI partnerships expand enterprise offerings, potentially increasing revenue streams.
- Date: 2026-11-24 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQSVY1c1libERfeFdXazhSbjdCblNEWHZfWGRiVlFPVFdDUWFMLUtjaEFudTU1LTZLOFRTM2Q2TVAyczdOcVZzbUJYTHE4UVBRdUkwOURqbTZtYlE3eVIxRVNPbU9JcWVVNER5UHdlVURGWWFsQnM3eF9vZ2c4VnhpUWlBWm5xZkYwY1UtMFZUdF83OXFGMVQzbmV5cTJkYUlkRDF5SGZ3WkE?oc=5>

### Microsoft (MSFT) Stock May Look Reasonable As AI Commitments Draw Scrutiny
- Summary: Analyst suggests MSFT stock appears reasonable amid scrutiny of AI commitments.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNalJYeUVUa3czcERnOXA2LUVJUlJaM0owQlJvZm9Gek1DeHZXV3lwREJFZVM5Nm9KVjdMbC1KRGJmeWg4Rk15M0FZV0ZMNEM0dF9wLXF3dWRpRjhZNVY4Y19fSU9ucUR0QVZKZ1hEQl91eVdnYmlZZ0E4X2RlWmxOWV9KTmpWcEZLZUxBYUJwV3plM3pUOU1MdzF3?oc=5>

### Microsoft Corp Stock (MSFT) Opened Up by 3.39% on Nov 23: A Full Analysis
- Summary: Stock opened higher by 3.39%.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPWUd0X3I1bVJ2SDRzRDBLajlQcXRUTWFMbjg1RS1YR1BhWlR1UVM0dEgtS2VWc2lySFpXYkppSC1XMnFaZkdXa0cxMjBqbjZBRkxYLUd3Y3RhTmdUUVlLTzREdmJEWEhJVWhXTjZucWZoOFYtNXJmdU0tWVJVWXM1S1Y1QkFlY0RVQ0Nz?oc=5>

## HEADWINDS

### Microsoft Stocks Fall 2.53% as Hyperscalers Join AI Selloff
- Summary: Microsoft Stocks Fall 2.53% as Hyperscalers Join AI Selloff
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPUlNuenNyci02QTQtcEFiaTFad2ZGUTFiWXdqaE90d183SVRCVF9iWFBHRFRsd2lvejgtb3JiYTRTdFpuZ0M5NzFUeEJ6ZEpkNUlmcTE1ZlhkU3hVYURhSFR0SkxfSFJpSHFuQmxudjQwdUdvR0RiTVJOYmNVVkcyZmxnZ1U0dWNYUGM1cjBmcnhITkxVRWVldEthT2JxS3Jxd1FRNkI3eEh4NkZrQ19iV0J3U1NRMHdXVmc?oc=5>

### Microsoft Stock Falls 7% in a Month as 24-Hour Outage Triggers "Code Red"
- Summary: Microsoft Stock Falls 7% in a Month as 24-Hour Outage Triggers "Code Red"
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNMmswXzV3QXUxa3JXUFpWUEtGWHZyZzdjdUpsN0pmZzgxM2pqaFMzeXVidDV1ZEY1ZmNJbDIxMHJ5WkVaUF9ValMwdTZzSVQ2Qjdid0RvX3NISXNlLTNiYmx5dTlWdVNvcUVEX2RNNElFeDU5WjlaRTF3a3UzaHBTeXIzZFUxdDFTeDJ1Q1ozdGlJX2FXVmNKSXhaMHV6QVk?oc=5>

### Microsoft Corporation (MSFT) Is Facing AI Spending Fears: Could Its Cloud Growth Change the Narrative?
- Summary: Highlights concerns over AI spending impacting cloud growth.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPSHhZLXZ3QWQ5eFRidGdBVDBfeXYteFljWGQ4Uk9PRUxaOHlNWWVXSzdmOVRyX0pmSm91dWV2SmRZa3pGMHpvQjcxTldsd3hSS1pwVWxtclYxUTNOc1hHZkZYa3ZteFlaakJKNGRwUkJaYVQxdUs0c2V1RjEzOU1yUnA5aWN3a0pFUzhBbHZQVWNvd1FUWXNKV1BNZ3dPMm8zWlZn?oc=5>

### Microsoft engineers faced 'fog of war' during 24-hour outage: report (MSFT:NASDAQ)
- Summary: Reports a 24‑hour outage affecting Microsoft services.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOZXdjMEJSdlpsWVNMV3hya0k1NDRJYXJhZGJoYnZ2VElkUDNxeUh4dF96YVZUak8xaGxfaEVPVm1oOWh6VVFoRzNBLU9ESkxkeDJwQlI1YzhXS3p1dWE3eml2UzdyMTFvbmM4bERmcC1kLWIydm1yS0hRVUZHeTFXNEdETmRuMkwzNjZiRjJBMzBkVm1NSFVLN18xdnNmS203SHRobFRB?oc=5>

## CATALYSTS

### Microsoft Remains Attractively Valued as Azure and Cloud Drive Growth
- Summary: Microsoft Remains Attractively Valued as Azure and Cloud Drive Growth
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxOR0xIZGJOcndyX3Y2WFlBRzlvZDZaSUJKSDMzLTFSS0lPMmlnTVZEa0VRZTkzTVI4SXJ4QkotRVUxRzFqTVh2OThjZ2ZFTlV6VWFMRVU3QVpPaGt4cUxDMGtzYUg3QWxCNUpad3dhd3hJWnhWTG54MW15LUF1ODE4YnFoY0hpVkJkM0RWN0RlTkxoNmRaMmMtajJIMmszQ3ZfTWc3czRFN0xGbjNa?oc=5>

### Microsoft Is Down 7% in a Month, but Not One Analyst Says Sell. Wall Street Sees $630+
- Summary: Microsoft Is Down 7% in a Month, but Not One Analyst Says Sell. Wall Street Sees $630+
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQUlRxa19vYXRzZEJudlNDRHl6ZE1fa095dG5YZjc1a3h4NHN6NFBuZm9KSkFnZGFyV0VGU2NCMy1TMUd0ekIyY1d1bVc2dkdHNUhRYVlYUTRRZ1hrR3J4WGxLYmlaYmNzMldKZ085amhzU0tJX3JYVTl4eWplemJDNjFUeHVfQ1Z4Qmhvc3d4cHJjNGs4N254TkUyRk5qVS1oOXpDYXFoUmFSZlhoZEJza21Bb3A0NkdjcXRtUlpTM0pKWnc?oc=5>

### Microsoft beats earnings estimates and lifts dividend: Can MSFT sustain gains?
- Summary: Microsoft reported earnings above estimates and increased its dividend, potentially supporting future growth.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxONWdLNmU3ckxKNHE2MUk5ZFdyZ0p1cmlRcjhsUHI4YktvcWN3S2wtb09nT0pZdElRMnVUa3Ewc3FoMU1FTGkzd2FuSlNIVEN0UVVyREFpejFmdTBBSEg1eDdLY2ZjZDljdGNzeVRqVkc3VmtCUkNLRnd0azlXc1hOaGlKNU1ON0lLOUNJTTdGU01tQjNrOWc?oc=5>

### A new data center proposal is up for a vote at Microsoft (MSFT) after its predecessor drew 27.48% of votes cast.
- Summary: Microsoft seeks approval for a new data center, following a prior proposal that received 27.48% votes.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNTWRKR0Z3dmF5SFpoaVRnMTFJdVFoZTFEV2RRMU54bEJtRy0zTUVmMjczQlZnc2hEeDFhUjg0T3dpakZfMUFKQk9lVWU4TWVXRjNvczZIZFlwQnN0bzk0WnpaajhjZHluMm1YbmNNaTBtT1ZzS3pUVXU0bzlHTTc4MW9vaERCbUlEckpiQzZBbFBENG1UTmFGakllVQ?oc=5>

## RISKS

### What's Going On With Microsoft Stock Today?
- Summary: Analyzes current market sentiment and price movements for MSFT.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOcDJiZnI4X3BtV1V1R0lBcmo5U240UVJXVm53UHRuOHpFN1hMWmxBeXVFLVVDVVliZGI0VTlsMmY4V1B2ZTVKX2NXb2ZiaDlTLVEyUVFnc3hUUXZpejl3aUtNODBLLTNFeWctaDRWMXlqZXZqekdadl9GYzNrU3NBMFVQOVlPUGNxcVUwbDBxRmlSWnhaVV9DMmJsWFo?oc=5>

### Is Microsoft Stock Worth Owning as AI Capex Weighs on Free Cash Flow?
- Summary: Examines AI spending impact on MSFT's free cash flow and valuation.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPYTFrRzFPS2FrbHk2TjJGR1NvdDd5eGFyd1o3bjY1blFYU045bElKUGQwUHpNWHh5SEszU0p2SkwtS1VDUE8zdWY5aFhvaWQ3ZHV4T0tWOXR0U3FjTndpM1RMQTRNZjk1My04OGFMTW9HejRVcWdkR2RoOC0wZGFkQzNOZ3FrSml5OVNzZ2JnajBGRlZzOWRPWmF5dlRONm9MTDQyb2ZHUGdSenB4T3psNlZUb0cxeTVvSFFjaEVZOERadw?oc=5>

### Can Microsoft security overhaul pressure MSFT further?
- Summary: Considers potential security challenges affecting MSFT's operations.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPSE9HM1NZQmg0V2lmLTRCcnFVS1RMcDdiV3AwVmVlbi1KSVo4dmYxbUtvMGdsamxvVkd3OXdkV1VlN3RrUUw0eWczRlZ2SnhkbGpkWFFKU3ZzVkIyaXp1bmVscUR3THBXOENZS3M2QXlGeXktb0JKZWQyTDlzZlVsLU53OFNwV2kzQzF2Tjk0NmpCMG9UeUE?oc=5>

### Microsoft(MSFT) Stock Price Today | Quotes & News
- Summary: Reports current MSFT stock price and market activity.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5wJBVV95cUxQRWdGQ2dZeGs1RnZYbmRPaG9STmFIUFZGUGY1ZWoxWjQtLVlvZGdmR2VIRnpvSHJiOG4wOWVDWklLdUFxNmpiekxaRWtiZzA4Y0NVNFpLMzJjZGtCV1JkX3ptYlkzeE1nQ1FHZ3dnVHVzbXpreU5BcmQweTBZSEcwYm1pTnV1VXhkWW8wWHhHMkE1NXBsdXBMeE0wUW9HTDVwa2dxaHlPdnZpbkhQLWhSbURkUmFLX2FmU0UycUwzazhrZEMwS2tSV05Kek1kNEtQbGFzODJCTmJ6UDJ2dlZvZ2dsYkFhZlJoYlNQZXE5SUdlUzE4anBEYVBsa2UyeGV5Z0R0X0dWNDh0a3dick1NcmhxVDJ5S1V0YmYwbi1CTXQyWFYxc1lDelgwcVdFN3M2NVM4QnBzaFV5cXA3d2U3am9fM1N3TDNUeG5vSWFhT3A4OVVwaENKMFFGb2lieGhoYXNMNHJFQQ?oc=5>

### Microsoft Corp Stock (MSFT) Opened Down by 3.53% on Nov 25: Key Drivers Unveiled
- Summary: Details factors behind MSFT's 3.53% decline on Nov 25.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNZmhhQmotWUtRbTF5ajZ2R0ZUbFplWlZETHRpSTVkRmpqTTFiR1lRRWxDbmh5RXgzLUN1Nm9mWEc5TlZObVJEQlIxNTVmMGs1SDF5dkJfTmpHOFZGN1BSWnJhV3ZuYmx4VVhTQl9VRlBtUF90MDNVbVNhWlFLMWt2V0pCTWVYWFQxTFJj?oc=5>

### Microsoft Declares ‘Code Red’ After Recent Outage
- Summary: Microsoft issues a Code Red alert following a recent outage affecting services.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNN3ZJV01hcVVRTmpKMU1Va3pZUFFaMG1wdE9USXlRYnEzNjZ5SGViVjZGejdwVUVGWVIwOWpTdTdqVFp4X01zNDc2YURWanB2RHFQcGFLc0xmcHJ4YWVPYzBmQmZhWENSWjBFOWI4QUdoRjY0QmdhenpzYWU1S0p2amgwZHpEVDZGeWF5Q2VXWU5TTWNXQjg5WnNhY2J3b3ZwVVVvcDlOc05tM2tibUxNVjRsZTlSODRod3liTTFRcDViSkZWb0lpT0VEdmI?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MSFT** | **25.57** | **7.73** | **18.03** | **18.80** | **3,638,315,450,368.00 USD** | **3.56** |
| ORCL | 16.28 | 5.08 | 13.11 | 29.60 | 323,867,508,736.00 USD | -46.57 |
| GOOGL | 14.26 | 5.09 | 17.58 | 24.70 | 3,357,491,331,072.00 USD | -15.34 |
| AMZN | 19.76 | 4.31 | 15.42 | 12.10 | 2,643,055,345,664.00 USD | 6.43 |

Peers fetched as_of: 2026-11-25; MSFT reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMihAFBVV95cUxQM0luQzAyX0lFeUV4bmJjZk9IRk94QlJyQms0OTl1SXpmeVBaSDdkcmJqVXF3YzhSZHJVY0xmeC05SlBld1RmbUg3N2ExaDhQa0thLUF6VXVjeDg2dEpQckJaSzhnV0ZDTWdTTzdrY2JyRVRJQndfQVdMdUdRRTlLa1FuLTM?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxQWk9fMnlSS3RJREZlVExGelNuS0JSNm50Y2EzWHNMNDlMWDNRdV80OXdqRnFNMmJUcEJ5X2VRMDk5Ml82VGs1UUVHalpuYXFDU2lTOVBsU0Y3bUNXV0RuTk5nOVRoajlManhuLVV0eUR4eW5Qai1HY3lGRFBKZnhkRGpRSkdYY2Z5UWRXZUlidWhEajU4MnVuU0ExcjlaQjdIekJkcE9vNm16R0ZkUEpPSTJERi1rXzhMaGJtM1J2d3MzVzZFSmxUY0xMVnpPZ2xOcDdpaDFFQWRwVGdRZzZZbEFoYXo?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOTGFBVVdNRFBFZE9EWTZDR2tLMFNwTXNEbnMycHhqOElxTnRwYzNjdUxRTlRjVGhLR25QRUxvTUdVNlFlOEhWc2JKZFI3Y3JoN3hIS1hHN25CY0s5RFhpeHE3bGN5LWg3c0VVN0ZhUVRBSk5ZbjRBaEtBS2pIVGtHUlV6a0J0Qy1KOFhJS2xCMXJ1elpScUMtcGVn?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPSTN0N1hHMGNON3J1ZFRlaGhhZXA4WnZWWlBRRXU2cG9Sd2J5TmVYMGlWSnJ4TWExU0JJaWN3d3RhM0Rja0RkbmhmQkhLMkhkTlFka3p1TFNUUUhQdTRBNWhJMmhYTmY2QU9PZDJybmtoZWEwVDYzY3BDMWMwRUM3Uy1YQ3Rjck10M1dzaWxzRVNQZ05VQ014V2JiTkJqTWZMSURocA?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQSVY1c1libERfeFdXazhSbjdCblNEWHZfWGRiVlFPVFdDUWFMLUtjaEFudTU1LTZLOFRTM2Q2TVAyczdOcVZzbUJYTHE4UVBRdUkwOURqbTZtYlE3eVIxRVNPbU9JcWVVNER5UHdlVURGWWFsQnM3eF9vZ2c4VnhpUWlBWm5xZkYwY1UtMFZUdF83OXFGMVQzbmV5cTJkYUlkRDF5SGZ3WkE?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNalJYeUVUa3czcERnOXA2LUVJUlJaM0owQlJvZm9Gek1DeHZXV3lwREJFZVM5Nm9KVjdMbC1KRGJmeWg4Rk15M0FZV0ZMNEM0dF9wLXF3dWRpRjhZNVY4Y19fSU9ucUR0QVZKZ1hEQl91eVdnYmlZZ0E4X2RlWmxOWV9KTmpWcEZLZUxBYUJwV3plM3pUOU1MdzF3?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPWUd0X3I1bVJ2SDRzRDBLajlQcXRUTWFMbjg1RS1YR1BhWlR1UVM0dEgtS2VWc2lySFpXYkppSC1XMnFaZkdXa0cxMjBqbjZBRkxYLUd3Y3RhTmdUUVlLTzREdmJEWEhJVWhXTjZucWZoOFYtNXJmdU0tWVJVWXM1S1Y1QkFlY0RVQ0Nz?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPUlNuenNyci02QTQtcEFiaTFad2ZGUTFiWXdqaE90d183SVRCVF9iWFBHRFRsd2lvejgtb3JiYTRTdFpuZ0M5NzFUeEJ6ZEpkNUlmcTE1ZlhkU3hVYURhSFR0SkxfSFJpSHFuQmxudjQwdUdvR0RiTVJOYmNVVkcyZmxnZ1U0dWNYUGM1cjBmcnhITkxVRWVldEthT2JxS3Jxd1FRNkI3eEh4NkZrQ19iV0J3U1NRMHdXVmc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNMmswXzV3QXUxa3JXUFpWUEtGWHZyZzdjdUpsN0pmZzgxM2pqaFMzeXVidDV1ZEY1ZmNJbDIxMHJ5WkVaUF9ValMwdTZzSVQ2Qjdid0RvX3NISXNlLTNiYmx5dTlWdVNvcUVEX2RNNElFeDU5WjlaRTF3a3UzaHBTeXIzZFUxdDFTeDJ1Q1ozdGlJX2FXVmNKSXhaMHV6QVk?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPSHhZLXZ3QWQ5eFRidGdBVDBfeXYteFljWGQ4Uk9PRUxaOHlNWWVXSzdmOVRyX0pmSm91dWV2SmRZa3pGMHpvQjcxTldsd3hSS1pwVWxtclYxUTNOc1hHZkZYa3ZteFlaakJKNGRwUkJaYVQxdUs0c2V1RjEzOU1yUnA5aWN3a0pFUzhBbHZQVWNvd1FUWXNKV1BNZ3dPMm8zWlZn?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOZXdjMEJSdlpsWVNMV3hya0k1NDRJYXJhZGJoYnZ2VElkUDNxeUh4dF96YVZUak8xaGxfaEVPVm1oOWh6VVFoRzNBLU9ESkxkeDJwQlI1YzhXS3p1dWE3eml2UzdyMTFvbmM4bERmcC1kLWIydm1yS0hRVUZHeTFXNEdETmRuMkwzNjZiRjJBMzBkVm1NSFVLN18xdnNmS203SHRobFRB?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxOR0xIZGJOcndyX3Y2WFlBRzlvZDZaSUJKSDMzLTFSS0lPMmlnTVZEa0VRZTkzTVI4SXJ4QkotRVUxRzFqTVh2OThjZ2ZFTlV6VWFMRVU3QVpPaGt4cUxDMGtzYUg3QWxCNUpad3dhd3hJWnhWTG54MW15LUF1ODE4YnFoY0hpVkJkM0RWN0RlTkxoNmRaMmMtajJIMmszQ3ZfTWc3czRFN0xGbjNa?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQUlRxa19vYXRzZEJudlNDRHl6ZE1fa095dG5YZjc1a3h4NHN6NFBuZm9KSkFnZGFyV0VGU2NCMy1TMUd0ekIyY1d1bVc2dkdHNUhRYVlYUTRRZ1hrR3J4WGxLYmlaYmNzMldKZ085amhzU0tJX3JYVTl4eWplemJDNjFUeHVfQ1Z4Qmhvc3d4cHJjNGs4N254TkUyRk5qVS1oOXpDYXFoUmFSZlhoZEJza21Bb3A0NkdjcXRtUlpTM0pKWnc?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxONWdLNmU3ckxKNHE2MUk5ZFdyZ0p1cmlRcjhsUHI4YktvcWN3S2wtb09nT0pZdElRMnVUa3Ewc3FoMU1FTGkzd2FuSlNIVEN0UVVyREFpejFmdTBBSEg1eDdLY2ZjZDljdGNzeVRqVkc3VmtCUkNLRnd0azlXc1hOaGlKNU1ON0lLOUNJTTdGU01tQjNrOWc?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNTWRKR0Z3dmF5SFpoaVRnMTFJdVFoZTFEV2RRMU54bEJtRy0zTUVmMjczQlZnc2hEeDFhUjg0T3dpakZfMUFKQk9lVWU4TWVXRjNvczZIZFlwQnN0bzk0WnpaajhjZHluMm1YbmNNaTBtT1ZzS3pUVXU0bzlHTTc4MW9vaERCbUlEckpiQzZBbFBENG1UTmFGakllVQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOcDJiZnI4X3BtV1V1R0lBcmo5U240UVJXVm53UHRuOHpFN1hMWmxBeXVFLVVDVVliZGI0VTlsMmY4V1B2ZTVKX2NXb2ZiaDlTLVEyUVFnc3hUUXZpejl3aUtNODBLLTNFeWctaDRWMXlqZXZqekdadl9GYzNrU3NBMFVQOVlPUGNxcVUwbDBxRmlSWnhaVV9DMmJsWFo?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPYTFrRzFPS2FrbHk2TjJGR1NvdDd5eGFyd1o3bjY1blFYU045bElKUGQwUHpNWHh5SEszU0p2SkwtS1VDUE8zdWY5aFhvaWQ3ZHV4T0tWOXR0U3FjTndpM1RMQTRNZjk1My04OGFMTW9HejRVcWdkR2RoOC0wZGFkQzNOZ3FrSml5OVNzZ2JnajBGRlZzOWRPWmF5dlRONm9MTDQyb2ZHUGdSenB4T3psNlZUb0cxeTVvSFFjaEVZOERadw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPSE9HM1NZQmg0V2lmLTRCcnFVS1RMcDdiV3AwVmVlbi1KSVo4dmYxbUtvMGdsamxvVkd3OXdkV1VlN3RrUUw0eWczRlZ2SnhkbGpkWFFKU3ZzVkIyaXp1bmVscUR3THBXOENZS3M2QXlGeXktb0JKZWQyTDlzZlVsLU53OFNwV2kzQzF2Tjk0NmpCMG9UeUE?oc=5
- https://news.google.com/rss/articles/CBMi5wJBVV95cUxQRWdGQ2dZeGs1RnZYbmRPaG9STmFIUFZGUGY1ZWoxWjQtLVlvZGdmR2VIRnpvSHJiOG4wOWVDWklLdUFxNmpiekxaRWtiZzA4Y0NVNFpLMzJjZGtCV1JkX3ptYlkzeE1nQ1FHZ3dnVHVzbXpreU5BcmQweTBZSEcwYm1pTnV1VXhkWW8wWHhHMkE1NXBsdXBMeE0wUW9HTDVwa2dxaHlPdnZpbkhQLWhSbURkUmFLX2FmU0UycUwzazhrZEMwS2tSV05Kek1kNEtQbGFzODJCTmJ6UDJ2dlZvZ2dsYkFhZlJoYlNQZXE5SUdlUzE4anBEYVBsa2UyeGV5Z0R0X0dWNDh0a3dick1NcmhxVDJ5S1V0YmYwbi1CTXQyWFYxc1lDelgwcVdFN3M2NVM4QnBzaFV5cXA3d2U3am9fM1N3TDNUeG5vSWFhT3A4OVVwaENKMFFGb2lieGhoYXNMNHJFQQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNZmhhQmotWUtRbTF5ajZ2R0ZUbFplWlZETHRpSTVkRmpqTTFiR1lRRWxDbmh5RXgzLUN1Nm9mWEc5TlZObVJEQlIxNTVmMGs1SDF5dkJfTmpHOFZGN1BSWnJhV3ZuYmx4VVhTQl9VRlBtUF90MDNVbVNhWlFLMWt2V0pCTWVYWFQxTFJj?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNN3ZJV01hcVVRTmpKMU1Va3pZUFFaMG1wdE9USXlRYnEzNjZ5SGViVjZGejdwVUVGWVIwOWpTdTdqVFp4X01zNDc2YURWanB2RHFQcGFLc0xmcHJ4YWVPYzBmQmZhWENSWjBFOWI4QUdoRjY0QmdhenpzYWU1S0p2amgwZHpEVDZGeWF5Q2VXWU5TTWNXQjg5WnNhY2J3b3ZwVVVvcDlOc05tM2tibUxNVjRsZTlSODRod3liTTFRcDViSkZWb0lpT0VEdmI?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
