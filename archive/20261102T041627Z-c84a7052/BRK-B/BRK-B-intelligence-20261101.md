# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-01**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-01**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-02T04:16:47.012884+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 2, 'ai': 16, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261101T014405Z-e49d1192/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 5 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 78.26%; oldest publication 2026-10-25

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 542.4900 |
| Return 1D (%) | 0.0978 |
| Return 1W (%) | 0.0553 |
| Return 1M (%) | 8.9447 |
| Return YTD (%) | 7.9260 |
| Return 1Y (%) | 13.3683 |
| Annualized volatility (%) | 14.6179 |
| Beta vs SPY | -0.0387 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 0.9349 |
| Downside deviation (rf=0, %) | 10.0225 |
| Sortino (rf=0) | 1.3636 |
| Historical VaR 95% (1D, %) | 1.4122 |
| Historical ES 95% (1D, %) | 2.0016 |
| Correlation vs SPY | -0.0338 |
| Tracking error vs SPY (%) | 19.7459 |
| P/E (trailing) | 13.64 |
| P/B | 0.00 |
| EV/EBITDA | -1.79 |
| Revenue growth (%) | 10.00 |
| Forward P/E (estimate) | 24.18 |
| Gross margin (%) | 30.33 |
| Operating margin (%) | 32.56 |
| Return on equity (%) | 12.12 |
| Free cash flow yield (%) | 6.20 |
| MA50 | 515.1120 |
| Close vs MA50 (%) | 5.3150 |
| MA200 | 495.7436 |
| Close vs MA200 (%) | 9.4295 |
| RSI (14, Wilder) | 66.8188 |
| MACD (12,26) | 9.3544 |
| MACD signal (9) | 8.6222 |
| MACD histogram | 0.7322 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 542.4900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.0978 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.0553 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 8.9447 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 7.9260 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 13.3683 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 14.6179 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.0225 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3636 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4122 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0016 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0338 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.7459 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0387 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9349 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.1843 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.3320 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.5610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 12.1200 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.1977 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.6441 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 66.8188 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7322 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.3150 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.4295 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire Hathaway Shares Just Rallied to Their Highest Level Since Warren Buffett Announced He Would Step Down as CEO, Closing Within 1.5% of Their All-Time High. Does That Rally Validate His Succession Plan?
- Summary: Berkshire Hathaway Shares Just Rallied to Their Highest Level Since Warren Buffett Announced He Would Step Down as CEO, Closing Within 1.5% of Their All-Time High. Does That Rally Validate His Succession Plan?
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQVUV2VG9CYjU2MXh1Um1SbjkyUllBVExtbzhNQkZQVFN4bjdkU0JqenZDZmRoa0VHeHd3ME1CNkxjdjhFNUp5NTdHYWNuTG5oRUkyUzdEVXItNWx4bEpRLUhoREdrbGJISW5WNTdzQWl6ZU1iQXJ5QVRlS0dOWEtNeTdtdVZ5dVV5empvMVlORUMtbF8wT2RDRm14UldBbGE0LUdUeXV3?oc=5>

### Berkshire Hathaway (BRK.B) Gains Momentum As Valuation Still Looks In Focus
- Summary: Berkshire’s valuation remains attractive, driving momentum in its stock.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNS3EtUEZPZUlYeU9nbjVBS2NfYmlVVTlnOWtCWXhEcjF1cjVOMlZyU1RmOXNHNE15cE5BVVMxNjBDNHduMHF3eEtmZEpvbjJENkUtSjk4aVJmT3RYR0ZmQllZUE5iNXpPejkxdVUzNVlCRlQyNFRlVFh3Mk9LYUR0RDRCX1lSbXhFcDk4Z3dQY3hteFdXMDVlQXo1aw?oc=5>

### Berkshire ekes out some new highs, but October rally stalls
- Summary: Berkshire’s stock hits new highs, though October rally stalls, indicating short-term market movement.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNMks0NDZlNFp2b3hfeWpkTXE5MlFGMlBTMjlZQTB5VEg5UXNSQWZ5UF8yTjJkaERqby05NVJWS3RjcmtMQm9rTktMcm1MaXhJdjZvYjRMY2kzYkdtYUNjQWtyZ04tQ2xhUU9zZkVkVGc3Y1E1VE1UNGVFc0lLWWlXRlVHNkQ0Z0hzZ1hBeXFWNWZpQjlQUkg4aGJpQdIBoAFBVV95cUxPTmFsNFUtR05QdmdUU1FUclBLWmlBMEN6WndVQ2ltX3F0THczZ2JKSXU2bmlreVN6bW1xTXN5aEtnT09peW9QOEJCTE1OVUxwR2xGWHVEcTVMdHhRZ0xKZlAxN0hJd3Q5ZFNSY2RWUER1YnJsMDhnUWlwcHBtd3Bmc3RRc0NCUXlacmF4ZElrbzVYeUlvbWFFbEVycjhiNzlu?oc=5>

### Berkshire Hathaway Trades Above its 50-SMA: Time to Buy the Stock?
- Summary: Stock trading above 50‑day SMA, suggesting a potential buying opportunity.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQYVgtNWNPbmtVb3NFZ2hraFRULUNXZk1tMFpOUlluREw5MHZ1RklSQU4wODFxSkFUWGNNNGpVS25xMzRkU2dnZ2tjU2hIYnZqTkhibUdHckdYcEJ4UXd5NjZ1TFUwZzkxMHl6THhIX0Z4eEhSd3ctaFNFZHNpM3JMV2VwM3FhMFo1dXlDcC1uT0pIdVgxcEdiNGF6NnE2YjhJ?oc=5>

### Berkshire Hathaway Stock Rose 10 Days in a Row in October for the First Time Since 2018. Here's What History Says Comes Next.
- Summary: 10‑day consecutive rise, indicating bullish momentum.
- Date: 2026-10-25 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOZkFuMWpmT3otRzRPaEpoM0xlaUFNU2Y0cjYyZXYxRVJtZlRKVFl0Z3ZyQXpxdDVCSXp3X3hfZmFRY3NCaHlqVFgzSUNseWdvLXhIQWdyUnFfdlNkb3hqZVFqOTFhb19DdVpPc3lBaVBWdm9LZkhOTks0QkNEcThfSnY5a2hRUTFYdVNlbVQzUHd0OFdHTldXOTFuRXpiUQ?oc=5>

## HEADWINDS

### Berkshire Hathaway: Is the Stock Still a Safe Buy Without Warren Buffett?
- Summary: Uncertainty about Berkshire’s safety post-Buffett raises concerns.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOb3d2TFVQVlNMSXVKOU5rcWplYlNOdVV5WVdDMWlIQ3pJeXRtZ1RJakpmZTdOMi00aFJKWlcxeXZ6WW8xYk9BV0lxRzJwOUdVaDgyQTZzeHRtblpfRnF5OGpndFN3ZU9pbXpGT1J2WjZDS3NLREhoWXlXcjR1Rk1GVVBxazdsWGpnSVZFZmRFb0NiM01USTZyWDJKUC1TMWlCV1E?oc=5>

## CATALYSTS

### Berkshire Hathaway Earnings Preview: What to Expect
- Summary: Berkshire Hathaway Earnings Preview: What to Expect
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNNHdVcXB4VHhLQjU3bWpGc01yZDI5RnZaOHNPMmVQTUNSbzJfMUZ0SWRUYmhEZ2dUQVFRM24wOGZXY01KMDdqMk1kelE4THZKNXZOcWZKR2N6Ty1qdlN0MWc1dkJiSVBvdGZ4NU4xU0FnS3dCcFBGUlRoZWFtcGpKYWQ0R2FjeVllTTJLajZuWUxSYldUZUEyemtITW1ZaldGTHpLdGpjajhkOTg?oc=5>

### Berkshire Hathaway (BRK.B) stock price forecast: insurance businesses hold $359 bn in cash
- Summary: Large cash reserves in insurance units could support future growth.
- Date: 2026-10-29 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNNFBxTEo5Q1doT1VNaTcyakVXSzFVaFRra3A4NXA1SUNnTjBRbFFzQUJCUU4yNmJ3ZU1iVDdEazkzMDd2eWhrQ2JDWVNCU2l5bzhmZm9BSjlyTlZ4OUlPT0FHZEhwQjVlMFVkcWJwdkJNajB5MzRDSk5vNExSVW5mQ0FCeUwwekV4RWFibG04WmhHb21ZeGxJWmlTeFBlRVZxRk5JdzlNVk42T1RhcDVkUEk3c0Y2QVQxZDdCUDdYZmdpd2s?oc=5>

### Is Berkshire Hathaway Stock a Buy Near Its All-Time High?
- Summary: Analyst question on buying Berkshire stock near all-time high.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOcHQ5LXhDTDB0czloZWlqRTdncFROSEZJc1ZTcXdTcGJ2V0Y5TlY2dlZPbmc3dlk3blZ0VWpRa1dUemtGWmR0WFRvcDVqQUUyUDd5LTM4QXhCVnhfLVpEeGFxLUxaOUdJcjhKZDcxT0dwVi1Rd2NmdktWZGFoN3FKUjgtaUxwSmw2U3pvV0duMk1pUG4wZWx5d3lvMmQ0czA?oc=5>

### Learn Why The Bull Case For Berkshire Hathaway (BRK.A) Could Change Following Tech Stake Increase
- Summary: Stake increase may alter Berkshire’s valuation outlook.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPbGJfQ2ljcFBDUl81N0lUbjlOTE1nSmhsS1dNQnBZOWt0OXlHZ2J5SGNZQW15bDVSYmU1cjQ2b2dqUTlTdk15QjJ3SWlJV2EwU19xSVZ4OW9YOWJTMzRjaldoci1CUzUtcXdoUHROUUl5bnk4VGpXRHNLNHY0TGgwTlZsenhtcEx3djJQaHpaSGR2UFBTZnhjLVl3?oc=5>

### Berkshire Hathaway Started Buying Back Its Own Stock Again This Year. Should You Buy It at a Record High?
- Summary: Berkshire has resumed share buybacks, potentially signaling confidence in its valuation.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOX0FmSDUxcTQ1bWV4bS1NVWM5bWdsRGhVZ1pJT0s2aUpYWXpHQnluZ18xRk03WlBVLV9WQ0t1bGY4MTJrRms5UlRzckNaNUF1YUp0YXpxQTB4bVpKdUdoZ3VIQVIwalF5WUQ5azBmQVU3VFVDajh6SWRNcTE3SGFFSUE2eC1UcE8wNENMZzdkWTlCRGg2X3NtQnNSTEhGcVp5LTQ0NnRB?oc=5>

### Warren Buffett's $48 Billion American Express Stake Has Been a Huge Winner. The Latest Results Say the Streak Is Far From Over.
- Summary: Berkshire’s American Express stake continues to perform well, reinforcing portfolio strength.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNY0Y1YzJaSTc3OHdpX0tuRlFUNGlPNkthbzFPUTZBNklmcmp3S3Z3TFhZd0JMbUh0SzYtSkd4RVRXU3dNUnl4eG9WOGVhcVhKZmNHWFdhQ0dBazZjMGQxU2JoU0VkTm4zZFU1bVl5UEpveFZoNDJUS3BHQ1ItOEhfbDBIMHQzVVR1c1J6UDB2VW9rSGdsUHh4aERsLTg2WHZFSXc?oc=5>

### Prediction: A Bear Market Is Coming. Here's Warren Buffett's Best Advice to Prepare for Volatility
- Summary: Buffett warns of impending bear market, offering volatility preparation advice.
- Date: 2026-10-31 | Impact: medium | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOWlBmbkNJZFlVamUtSG8xcVd5VkFYRnVscUJOME1HaUVSam5rVlJBZjlNVU5FV0wzbUNYQkpRd3FNQlZVU0dSM05fbmpuSTdIbzZIUWdIMFRUWHllaDBkdzJhaUxjekNVeFNfcTNHYnktRXVCYnl0WXUyeFNKc2ZybVdKN3o2X3h5aW94NXZNRnItWjV3NFlhaQ?oc=5>

### Warren Buffett’s Berkshire adds $330 million to a familiar bet
- Summary: Berkshire increases stake in a known investment by $330M, strengthening position.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE1iZnhTbWFMdkd0SmdyOGU0bXZlakVvUXRpR3ZfT1JCTFJLUUE4RTkySDlCYXNyQWpxZy1fVUplWVRBcHh2UVhzTVhJcVhXQ1NLdXhDbEgxczFPZDBLbVBtalhQMGhSWFVEQXNWM01CYVRSOGV6UEtkZGVPNU11QQ?oc=5>

### Warren Buffett's Successor, Greg Abel, Has 54% of Berkshire Hathaway's $365 Billion Portfolio Invested in 4 Proven Winners
- Summary: Abel’s portfolio heavily weighted in four winners, reflecting strategic focus.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPUnA1LW4zRFM5Tzh1NVdCekFhcnkwYkdMVlNHUTE0OHFfRS1MaklIRVp5VHdXeVNsa1FKWUM5anNzMDhNM2FLMjIxcnlxc0tJcFQyWXg4MDMtaG83RjV6LS1wMVQ2VzZDU2ttckcwQjFwWHFvQ2g1bl9ydW1fVkpRdm80Tm43c0VSSkVKSUxiYmxuY0JzTHZjRXpKNldPS3Bhcnc?oc=5>

### Warren Buffett's Apple Bet Is Still Berkshire Hathaway's Biggest Stock Holding at 22% of the Portfolio
- Summary: Apple remains Berkshire’s largest holding at 22% of portfolio.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOMkt5SlVKQkJXX3JyV1J3Qk5fY3lZZWtsZDFKenh6WTZ6b0VIdG9WMVlGenNFcGd3MFhPRmZnR1JsZzNCS013Mk80S1VYYndxTi0yYk1mWWR5QnBoTngtbEl0OUE2X0xEcVNSbWc0c3d6OVFmcmxFcEZzSVJ6WTFJNXl6XzRaZmlybU1BNFE3ekRScWdQS0N6dWVMeGc?oc=5>

### Greg Abel Just Spent $330 Million on This Tech Stock. Here's What It Means for Investors.
- Summary: Berkshire’s chief investment officer purchased a large stake in a technology company, indicating a bullish stance on the sector.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNVmdWTEg0ZlNycGY3eHppMXF5Vl8weWttanpMY3RudW9YU3dLRDQwNXNib0kwMTVaMjh1WFZUVHNJLV9taDk5OVZ5bk90NGFKRWEtdzdDS0E5UEYxX3B6WVhqMUJVQjJ6VklZdllLV3JqOU5rNjRXN0kwY3pFakpCMDNxZ1gtRjN4UXpYWGhqTVVMelU?oc=5>

## RISKS

### Analysts Estimate Berkshire Hathaway B (BRK.B) to Report a Decline in Earnings: What to Look Out for
- Summary: Forecasts predict a drop in Berkshire’s earnings, potentially affecting investor sentiment.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNYXlWNjd6V2dkUmdRRHBUMjRSR09JclBRdm9fZGVLcE1iSnZET293bFBLVnJJdm9YNkxtZnJDSnVRVWxZRzhGazJvdnhHbFFtUk95dVJPNDN5YWs3RkRSN1R5MnRXb2lWa2JsNVFjbzJ4QlJ2N1BxelBXM1JSYTRYcjBma19pTktRZmlzR213alhsNXh2b3h4MDh2bXVRUjRMTGU4TTZn?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **13.64** | **0.00** | **-1.79** | **10.00** | **1,161,313,648,640.00 USD** | **13.37** |
| MKL | 13.31 | 1.24 | 7.63 | -11.20 | 22,866,710,528.00 USD | -3.54 |
| FFH.TO | 8.88 | 1.37 | 7.98 | -0.50 | 55,963,697,152.00 CAD | 10.71 |
| L | 13.64 | 1.19 | 8.10 | 3.90 | 22,756,892,672.00 USD | 12.10 |

Peers fetched as_of: 2026-11-01; BRK-B reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-08
- Next expected earnings: 2026-11-07 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-01

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

- https://news.google.com/rss/articles/CBMipgFBVV95cUxQVUV2VG9CYjU2MXh1Um1SbjkyUllBVExtbzhNQkZQVFN4bjdkU0JqenZDZmRoa0VHeHd3ME1CNkxjdjhFNUp5NTdHYWNuTG5oRUkyUzdEVXItNWx4bEpRLUhoREdrbGJISW5WNTdzQWl6ZU1iQXJ5QVRlS0dOWEtNeTdtdVZ5dVV5empvMVlORUMtbF8wT2RDRm14UldBbGE0LUdUeXV3?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNRnhobGVyclJON2dZSktPb2Q5ei1zV1pxY2ItWTlyMWRkanY1X1Y1UmxRODZwNEtwSlpNZFU0WldKdTNuNFM2a0NPamJVRWNvYWxMU3QyaGxrZ2o1TjYzR1pUU2JyRFRQUDFiSUItYXBkWENVSXY0aUEtUWFyd05sR21qek8xWF9ncHN1YTNSNmQ3ZnFQZXBlYw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNS3EtUEZPZUlYeU9nbjVBS2NfYmlVVTlnOWtCWXhEcjF1cjVOMlZyU1RmOXNHNE15cE5BVVMxNjBDNHduMHF3eEtmZEpvbjJENkUtSjk4aVJmT3RYR0ZmQllZUE5iNXpPejkxdVUzNVlCRlQyNFRlVFh3Mk9LYUR0RDRCX1lSbXhFcDk4Z3dQY3hteFdXMDVlQXo1aw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNMks0NDZlNFp2b3hfeWpkTXE5MlFGMlBTMjlZQTB5VEg5UXNSQWZ5UF8yTjJkaERqby05NVJWS3RjcmtMQm9rTktMcm1MaXhJdjZvYjRMY2kzYkdtYUNjQWtyZ04tQ2xhUU9zZkVkVGc3Y1E1VE1UNGVFc0lLWWlXRlVHNkQ0Z0hzZ1hBeXFWNWZpQjlQUkg4aGJpQdIBoAFBVV95cUxPTmFsNFUtR05QdmdUU1FUclBLWmlBMEN6WndVQ2ltX3F0THczZ2JKSXU2bmlreVN6bW1xTXN5aEtnT09peW9QOEJCTE1OVUxwR2xGWHVEcTVMdHhRZ0xKZlAxN0hJd3Q5ZFNSY2RWUER1YnJsMDhnUWlwcHBtd3Bmc3RRc0NCUXlacmF4ZElrbzVYeUlvbWFFbEVycjhiNzlu?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQYVgtNWNPbmtVb3NFZ2hraFRULUNXZk1tMFpOUlluREw5MHZ1RklSQU4wODFxSkFUWGNNNGpVS25xMzRkU2dnZ2tjU2hIYnZqTkhibUdHckdYcEJ4UXd5NjZ1TFUwZzkxMHl6THhIX0Z4eEhSd3ctaFNFZHNpM3JMV2VwM3FhMFo1dXlDcC1uT0pIdVgxcEdiNGF6NnE2YjhJ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOZkFuMWpmT3otRzRPaEpoM0xlaUFNU2Y0cjYyZXYxRVJtZlRKVFl0Z3ZyQXpxdDVCSXp3X3hfZmFRY3NCaHlqVFgzSUNseWdvLXhIQWdyUnFfdlNkb3hqZVFqOTFhb19DdVpPc3lBaVBWdm9LZkhOTks0QkNEcThfSnY5a2hRUTFYdVNlbVQzUHd0OFdHTldXOTFuRXpiUQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOb3d2TFVQVlNMSXVKOU5rcWplYlNOdVV5WVdDMWlIQ3pJeXRtZ1RJakpmZTdOMi00aFJKWlcxeXZ6WW8xYk9BV0lxRzJwOUdVaDgyQTZzeHRtblpfRnF5OGpndFN3ZU9pbXpGT1J2WjZDS3NLREhoWXlXcjR1Rk1GVVBxazdsWGpnSVZFZmRFb0NiM01USTZyWDJKUC1TMWlCV1E?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNNHdVcXB4VHhLQjU3bWpGc01yZDI5RnZaOHNPMmVQTUNSbzJfMUZ0SWRUYmhEZ2dUQVFRM24wOGZXY01KMDdqMk1kelE4THZKNXZOcWZKR2N6Ty1qdlN0MWc1dkJiSVBvdGZ4NU4xU0FnS3dCcFBGUlRoZWFtcGpKYWQ0R2FjeVllTTJLajZuWUxSYldUZUEyemtITW1ZaldGTHpLdGpjajhkOTg?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNNFBxTEo5Q1doT1VNaTcyakVXSzFVaFRra3A4NXA1SUNnTjBRbFFzQUJCUU4yNmJ3ZU1iVDdEazkzMDd2eWhrQ2JDWVNCU2l5bzhmZm9BSjlyTlZ4OUlPT0FHZEhwQjVlMFVkcWJwdkJNajB5MzRDSk5vNExSVW5mQ0FCeUwwekV4RWFibG04WmhHb21ZeGxJWmlTeFBlRVZxRk5JdzlNVk42T1RhcDVkUEk3c0Y2QVQxZDdCUDdYZmdpd2s?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOcHQ5LXhDTDB0czloZWlqRTdncFROSEZJc1ZTcXdTcGJ2V0Y5TlY2dlZPbmc3dlk3blZ0VWpRa1dUemtGWmR0WFRvcDVqQUUyUDd5LTM4QXhCVnhfLVpEeGFxLUxaOUdJcjhKZDcxT0dwVi1Rd2NmdktWZGFoN3FKUjgtaUxwSmw2U3pvV0duMk1pUG4wZWx5d3lvMmQ0czA?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPbGJfQ2ljcFBDUl81N0lUbjlOTE1nSmhsS1dNQnBZOWt0OXlHZ2J5SGNZQW15bDVSYmU1cjQ2b2dqUTlTdk15QjJ3SWlJV2EwU19xSVZ4OW9YOWJTMzRjaldoci1CUzUtcXdoUHROUUl5bnk4VGpXRHNLNHY0TGgwTlZsenhtcEx3djJQaHpaSGR2UFBTZnhjLVl3?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOX0FmSDUxcTQ1bWV4bS1NVWM5bWdsRGhVZ1pJT0s2aUpYWXpHQnluZ18xRk03WlBVLV9WQ0t1bGY4MTJrRms5UlRzckNaNUF1YUp0YXpxQTB4bVpKdUdoZ3VIQVIwalF5WUQ5azBmQVU3VFVDajh6SWRNcTE3SGFFSUE2eC1UcE8wNENMZzdkWTlCRGg2X3NtQnNSTEhGcVp5LTQ0NnRB?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNY0Y1YzJaSTc3OHdpX0tuRlFUNGlPNkthbzFPUTZBNklmcmp3S3Z3TFhZd0JMbUh0SzYtSkd4RVRXU3dNUnl4eG9WOGVhcVhKZmNHWFdhQ0dBazZjMGQxU2JoU0VkTm4zZFU1bVl5UEpveFZoNDJUS3BHQ1ItOEhfbDBIMHQzVVR1c1J6UDB2VW9rSGdsUHh4aERsLTg2WHZFSXc?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOWlBmbkNJZFlVamUtSG8xcVd5VkFYRnVscUJOME1HaUVSam5rVlJBZjlNVU5FV0wzbUNYQkpRd3FNQlZVU0dSM05fbmpuSTdIbzZIUWdIMFRUWHllaDBkdzJhaUxjekNVeFNfcTNHYnktRXVCYnl0WXUyeFNKc2ZybVdKN3o2X3h5aW94NXZNRnItWjV3NFlhaQ?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE1iZnhTbWFMdkd0SmdyOGU0bXZlakVvUXRpR3ZfT1JCTFJLUUE4RTkySDlCYXNyQWpxZy1fVUplWVRBcHh2UVhzTVhJcVhXQ1NLdXhDbEgxczFPZDBLbVBtalhQMGhSWFVEQXNWM01CYVRSOGV6UEtkZGVPNU11QQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPUnA1LW4zRFM5Tzh1NVdCekFhcnkwYkdMVlNHUTE0OHFfRS1MaklIRVp5VHdXeVNsa1FKWUM5anNzMDhNM2FLMjIxcnlxc0tJcFQyWXg4MDMtaG83RjV6LS1wMVQ2VzZDU2ttckcwQjFwWHFvQ2g1bl9ydW1fVkpRdm80Tm43c0VSSkVKSUxiYmxuY0JzTHZjRXpKNldPS3Bhcnc?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxQLVAwVlpaYTFxbXV4RmV5RzF2bzExVTdmVFRhdS1YQWVNYjZrSHNma3ZmcTJpY3VlQ0gwYkhQLUc2ZlRYRkhnMm0weDhpX2MwTEZXQU95ZnVqVEh0X3ZQMVJIOUJyWHJfU0t2V1B1SDBqY1V5Wm85a3R1OVQ0QnNySDNiLWh1ZVpNX3I3VlREVzZZa09QWXM0UDlweHVrYmozbzNqekxBc0Q4aXZlVW5Qdk1XaDdSMUlubTlDU2piUUJuTGpFYjBQUWRIbDZadFQ2R3hoTGUxWE1PQ2FKZXdXUw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOMkt5SlVKQkJXX3JyV1J3Qk5fY3lZZWtsZDFKenh6WTZ6b0VIdG9WMVlGenNFcGd3MFhPRmZnR1JsZzNCS013Mk80S1VYYndxTi0yYk1mWWR5QnBoTngtbEl0OUE2X0xEcVNSbWc0c3d6OVFmcmxFcEZzSVJ6WTFJNXl6XzRaZmlybU1BNFE3ekRScWdQS0N6dWVMeGc?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNVmdWTEg0ZlNycGY3eHppMXF5Vl8weWttanpMY3RudW9YU3dLRDQwNXNib0kwMTVaMjh1WFZUVHNJLV9taDk5OVZ5bk90NGFKRWEtdzdDS0E5UEYxX3B6WVhqMUJVQjJ6VklZdllLV3JqOU5rNjRXN0kwY3pFakpCMDNxZ1gtRjN4UXpYWGhqTVVMelU?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNYXlWNjd6V2dkUmdRRHBUMjRSR09JclBRdm9fZGVLcE1iSnZET293bFBLVnJJdm9YNkxtZnJDSnVRVWxZRzhGazJvdnhHbFFtUk95dVJPNDN5YWs3RkRSN1R5MnRXb2lWa2JsNVFjbzJ4QlJ2N1BxelBXM1JSYTRYcjBma19pTktRZmlzR213alhsNXh2b3h4MDh2bXVRUjRMTGU4TTZn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
