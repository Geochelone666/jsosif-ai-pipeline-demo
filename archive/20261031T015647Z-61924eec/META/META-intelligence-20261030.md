# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T01:57:30.616611+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 6, 'ai': 15, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **11**; {'directional_claim_without_event_type': 5, 'low_uncalibrated_model_confidence': 5, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 16 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 614.9900 |
| Return 1D (%) | -1.5260 |
| Return 1W (%) | -4.2996 |
| Return 1M (%) | -15.1948 |
| Return YTD (%) | -6.5926 |
| Return 1Y (%) | -7.4113 |
| Annualized volatility (%) | 41.2798 |
| Beta vs SPY | 1.4150 |
| Max drawdown (%) | -28.7332 |
| Sharpe (rf=0) | 0.0169 |
| Downside deviation (rf=0, %) | 27.5515 |
| Sortino (rf=0) | 0.0253 |
| Historical VaR 95% (1D, %) | 3.6289 |
| Historical ES 95% (1D, %) | 5.6251 |
| Correlation vs SPY | 0.4384 |
| Tracking error vs SPY (%) | 37.4793 |
| P/E (trailing) | 20.98 |
| P/B | 5.77 |
| EV/EBITDA | 13.81 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 17.28 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 35.41 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.07 |
| MA50 | 669.7887 |
| Close vs MA50 (%) | -8.1815 |
| MA200 | 631.2753 |
| Close vs MA200 (%) | -2.5798 |
| RSI (14, Wilder) | 33.2321 |
| MACD (12,26) | -20.4821 |
| MACD signal (9) | -6.8048 |
| MACD histogram | -13.6774 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 614.9900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.5260 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.2996 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -15.1948 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -6.5926 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -7.4113 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.2798 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.5515 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.0253 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.6289 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.6251 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4384 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.4793 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.4150 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.7332 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0169 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.2809 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 35.4140 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0715 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.9823 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 33.2321 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -13.6774 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -8.1815 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -2.5798 -> Slightly below the moving-average trend level.

## TAILWINDS

### One Big Reason Meta Stock Could Be a Winner Through 2030
- Summary: Meta’s long-term growth prospects could make its stock attractive through 2030.
- Date: 2026-10-29 | Impact: high | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPRVBPRktCcEhZbWhwNHJ5LTdQWGNnbG9PNEhtUzV4ZzZPZ2V4blA0MmdZQmJ1OTdqZkdQMnVXODhDSHlpdjRXam1BT2xjQi1WZXZhUXJVanRaajgxMVFPeVJtQS1Nd2Y5ZDQzb204ZW82NkNubFZSUUhLWHZKM3JVNDVmVDEwa01rVk91WXVZa3ozaEhqeUdfODZacjIzUTFuRmc?oc=5>

### Massive News for Meta Stock Investors
- Summary: Discussion of significant news affecting Meta stock, but no specific event identified.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxOZUJjVTVVd19qajRKZEtjUEZRUEk3QW1oc2JVRVdVQmNiRVI1VTdJcmxNcXBCQm8weE1oV0lJTjZKejVYaGw5c09FQS1KVy03b3N4cmVJVGZBQXJ4dUUzM2RMdkI0Y3FMMnZPTTl1Wkd2LVlDN29JTGVMNnV6TXR0QlNlYXJabUU?oc=5>

### Should You Buy or Sell Meta Stock After Its $95 Billion Bombshell Announcement?
- Summary: Analysis of buying or selling Meta stock following a large announcement, without specifying the event.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOQWNueG1FVWtlamZtX2VsZ1pNcS11bDJ1SUdqakY0ek4zZE92UVJ2RGlPWU1pX1BMS1h0WmhaeGp3NGRNNmtQamJ4WTM3eXhtVzA3SU9ndjNkYmk0ZXk2U2R4aUZvMEVzZldnQUhwR3BiemdpaGM1SzRnc2c5YnY2dG5GMDFMZVVSd1p1dTVndjU?oc=5>

### Meta Platforms (NASDAQ:META) Stock Falls 1.5% - Time to Sell?
- Summary: Report of a 1.5% decline in Meta stock, questioning whether to sell.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQMVdfQUVqN2RXcmU5T1Z5OTBoWEFYMXlKU3N4SnRIcVV3bXhocEhQM1E1QTFHUkJZMkNFaVg3SUdXQm9OcGZ1aGx5XzZEQXZ4b3M0OVA4ZDFra19qS0EyUzdIeUdnMHlJR1NFVmo1ci1HSlVrN1V4VmJRLURXZDFHNjRSMEl3UnpNWVpFLUMxVUxHeGEtbjlNck9nZnB6cUZLRGdmclI2ZnRtaklIQy1PTm0wRXc?oc=5>

### Meta Just Priced a Stock Sale at $625 a Share. I'd Consider Buying at the Same Price.
- Summary: Commentary on a recent stock sale price and personal buying consideration.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNdVlzQ3pfeDlpYVJ0TjRSX3padDdtb2NvaWNmOW9HQ0dQQzRubEdVU2E4ZTRhWE9WVGFpYjFweXdpUFd5UV9xNFZvZGdqcDE2Sm5aNGt4cXlTMllQYVBtSXRlQmJneG5JdTJXa0xDX3EtdVhRZTFMN2tFNzNEV19NbXA5REoya1I2Z3o2ZWgtVXBFQ3I3MU9ld0gwV2k1N2pTNy1ITDM4cnp3TEdpME1qbWxVQjdUc0ZKRFl4WlRxNjdzSm9PYlFZ?oc=5>

### Meta Platforms, Inc. (META) Stock Price, News, Quote & History
- Summary: General information about Meta stock price and historical data.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMiUkFVX3lxTE9NdF9xWW1RaDk2MmNFdk5acnJHSVhGM0dqcF90M081cUplRkpyVjZmakJsdS11TFhOcnVVRnM0T1RXcEo5ZzBITzA1N1BsaWVacVE?oc=5>

## HEADWINDS

### Meta Shares Are Down 12% Since Earnings. Is the Stock a Buy?
- Summary: Meta Shares Are Down 12% Since Earnings. Is the Stock a Buy?
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPeEFsRjB6d2lwTVZ1UWhyVnhEZmkwRG9rQmo1dVp5d3plSFNEVzZHQllCakFVdXJaM2dQUklnQTEwMHp6MDlud0pmOERnSFVpeEtuMFY1ZjFGMmtkcGFlN2JSUVVMLTBDNEJqazJDUXVRWTBFczdKTXJVVTlXcHk2VHZJUE1aTTVfZm1uM2YzRQ?oc=5>

### Meta Stock Falls Following Launch Of $35 Billion Stock Offering
- Summary: Meta Stock Falls Following Launch Of $35 Billion Stock Offering
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMid0FVX3lxTFA5WXQzNmRlc3JsVFdGZkFSWXhtRFlQX2ZzQkpRa0VlTmZxNFBpQmZJREZrZGR3YVI1SHBnR2FjVE1VOF9EYVBsWUctV3ZxVnc2QWw1MDB4REpGY0ExZWRoRnh4aHJlU1c5RW5Xa3lBTnVaQXlTNVZR?oc=5>

### Is Meta Stock’s Fall A Bargain Or A Warning?
- Summary: Meta’s stock decline raises concerns about valuation and future performance.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQdHR6ZEd6RloxRHdXdUk4cDVPUmJuX3ltU1NiZjh3RHFQc0R2LVdUaVZPdEYzelIxQ1JrZUpMampCVFM1ZGhOeXZoajJZdVlWb2p3SS1lbWlQMFlYVnVxYnpNdE1EeVUxeFlNZEhsVE9jQzQwQU5GdEVvcDhudnd2WXdNNEhwN3BPSDVFZGNBXzdxenhqT1hyMVdBMjM0M1lWclhxcWtB?oc=5>

### Meta stock closes out Friday down as AI spending fears continue to rattle markets
- Summary: Meta’s share price fell amid AI spending fears, reflecting market volatility.
- Date: 2026-10-23 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOVBsWC1HZmNiRnJHT3RIbzlmcmZLZVpRVVlibk5sMFhyLUJfSHVtZlhxNzBLWkJ6RkgtWWprZnl2ZUVCeVBzb3NOVzlJQkYwbjBvVzQtaFZDSk9rZGxlYWVjMEJnWFY0LVFiUVM0S2J1T0ExVTJMcFY4QjJ1ZDgwNVVrVEpENFpJMHVrRkpoVXJvSTktOE9fMU94dnpLR1UxWWlSTFVHallWRG1DTDBhNXJobzJpek5UeTk3dUFRZl9QMnJhaGo1OXo3TUhSeEg0LTVQeHZiZ0NuZw?oc=5>

## CATALYSTS

### Meta Loses $400 Billion, Auctions More Stock, But Analysts Still See 1.4x Upside
- Summary: Meta Loses $400 Billion, Auctions More Stock, But Analysts Still See 1.4x Upside
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQZDZCVy1CLS1KV1plaWZjVXo4UnZuWWVXbGRQNmtQcTRlM0lIeHBnaE5tVGg2dzN0MFJ2N0tQejFjbklESHhoTS1UX2p4SlUzQWhUZXFZTzJGM2NpTDFGUHJRSXVSS0N3YVpYRG9fUEM5Z2dMQmdYbkV0TEZkYUIxMUtWT2h3eVR6MGhqRFFUeFVqdklVQzd1TzlLeUw?oc=5>

### Meta (META) Stock Sees Modest Fair Value Lift As Muse And Financing Drive Debate
- Summary: Meta (META) Stock Sees Modest Fair Value Lift As Muse And Financing Drive Debate
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNSzVnUFl0aGpRRFVlalhrS21zWkJYNmVMMmtldEpsaTR1djVpNFNqWEpfWVN1bzRELU50b0xDLUNzUGhZVjJTS3NZQURWblJCMF9vdDdmd3FzcHl2NWp5SlV5anNKWWthSG9HVk1TVVcyMGhkWWExQmlDZndUdElGSVNoamdSN0pjMlJ5ZmZvZDZYSVNPeFl3?oc=5>

### Meta’s Unusual Stock Split Comes With a $60 Billion Twist Investors Should Know About
- Summary: Meta’s Unusual Stock Split Comes With a $60 Billion Twist Investors Should Know About
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOM2xkR0Z4TFBwOUVtd2JTOFNTWmJOdENmNU9kUXViMXNlZVBHTEpwYzhaUzcxelZsNmFRQ09PdG1iTmFKOEdaOUFhVU1MNFhiWERYN0trQVc4WUtubGVWaEtwRnphTzFRX3UtU19SUUZYclpRNlB6YWV0ZnFIN3VKXzUzSG5IOEt1YWpGRXBXUnBBOUVvdE1uaGtJcw?oc=5>

### Meta Platforms Just Delivered Great News to AI Stock Investors
- Summary: Meta Platforms Just Delivered Great News to AI Stock Investors
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNY3RFaF95TzNuUUhqODJYMkJYY0lNRkN1Qm1ydUtDTW40Y0sxUlQ3bXNwMzVVM0NTSTdKZjlqZXBoUjJ4cGs4TjBPSUZjZnhJNkN5eTQwMUtVOThqYVNNY1VCSzZKLUtlWVlsZEJJcTdOVVVoakV5ZmwyVzhIYi1MRHhER3ozS09pVFZGeHdWWkw2N215SHVoYTF1R1VHZ0p3?oc=5>

### Meta’s $25 Billion Stock Sale Ended Five Times Oversubscribed
- Summary: Meta completed a $25B stock sale, oversubscribed five times, signaling strong investor demand.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNdmR1WjllZWo5S013MU1kTmgzNWdZXzd3ejl4bHZFRlR6NUpLbWt5aHdaYkpzc3g4eG55M0Q2UGVHb01oSHBIUWZyY0tzTHNzMlU2clZ6NVFoZmJ3clRtYkZLWHFsWElfRHRibEw0UkZYMUNtQzNQcFVtejBQUjM4QVh6Yk9LdVMzOENZU1U3S0syTWRxSU9zdmFkQUlLY2hVQkFtVlFrN3lseGhEcWNPdA?oc=5>

### Meta Will Offer Up to $95 Billion in Stock. What That Means for Its Big AI Push.
- Summary: Meta plans to sell up to $95B in shares to fund AI initiatives.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE10bm9vdXZ0RDJuVWNfMGo5bnQtLTJ6b2c3WTlMNExXaEsyOUpiNEd0cGt0YVNldlZHNEtvaThTOXV3LUpBVEFmcmNOOTBSZDNPbTBmNGlFVzgwYkFqQmY2eExVUjR6UEEtNk1hNzdkWEgtTWs2bTZNbGl2a0hOUQ?oc=5>

### Meta Platforms (META) stock price forecast: AI funding and dilution risks after Q3 earnings
- Summary: Forecast warns of AI funding and dilution risks post-Q3 earnings.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxOS0FRMjYzYmNENmdZSkQ5TEdXdXBPeUFXUkc4WDBWcG91a3dJQTlQbVNpQ3ZTLVl6UUZLM1BVUEZ1dnBlc2steXQ3clVEb2paeWV6eWlRem9pbWkwUVVueFN0TU5rWE93MnZyb2tNNkdueXJoLU0wSUFZM3EtTWJWUTRPZG42UExzUS1DXzh3?oc=5>

### S&P cuts Meta outlook to negative amid capex concerns
- Summary: S&P downgrades Meta outlook due to capex worries.
- Date: 2026-10-30 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOQmZGYUxTaGtySHU1dFlpTTZGQ3pKdlJ6dEYyOThIZGJRNVZqVkFfYmpLeHpvQUhPMmR1Y3lVLWcwclFjUEtIU2R6LVBva2VyLVNtdTRUNEYxM0NNenJNeVdoeHhyTHVYMzI0eVdOQ3l1UVZ4d2lCT0M2Wk5oZUdqTmdUMmRvS04zT1BWb01CWXd1cGF1VXBIV0tTWUkxM19ZVzR3cnlFLVRwR0lDS2djSzlaVXd6RTQ?oc=5>

### Meta’s $25 Billion Stock Sale Drew Five Times the Demand
- Summary: Meta sold $25B shares, demand five times higher.
- Date: 2026-10-28 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOckVjQjluT1BwSTlMUFpCMjVielcySEVLU0hmQjhpUVZ2YlRxTlVyZ0Rnbzg2SGd4ZzNldDRZck96SFZ2UFkyVEl2RlJOTGFxZDU4RXc4Sms3aHpITFNYZ0ZCbFJ4ZWkwWEs1c1ZTQjFMSmt1TlNQbFRFaDViLWZBU1FHUDRmcnY5NXlMY1VEUUU0cTVVT2c?oc=5>

### Will AI Equity Raise Change Meta (META) Stock Narrative
- Summary: Meta's AI equity strategy may shift its stock narrative, potentially influencing investor perception and market dynamics.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxNTnBGN0VHMkVnVU15TE1iaS1ZMDVSYklISTZVdzFidFlFcVVkN05NVG9Ldm9rYnlFc2NjNjh4NVNscE9mZ1VuSTNqcjFqVHd5eXlycGRwb196ZE8xQ2wySGx4WE5lZHNrblB5RnY1NjZmUzNEbGIweXR5cWJWa3hsQm5n?oc=5>

## RISKS

### Meta's nearly $100 billion stock sale is a turning point for how Big Tech pays for AI
- Summary: Meta's $100B stock sale could alter funding models for AI, raising concerns about capital allocation and shareholder value.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxNN3hiMUxqR2tHRWdQY2xwX05JVVU4My1BWnpLdzJadkZ4bWJYT0N4T015RTdjcEQySF8xR2lBWElsM1JadEU2V2pVSkRHYXhORUhEZkdjSk5HQVBCOC02S0gxODNwLTZTa0lrTXg4VXBCQWJzV3FfSThBZnRnemZ6c0I2YkRHZVVmenNDY3hrcW0wbVE1UzBCRm5fcHcwRUZHQnlOXy1xVkFNTVVJemlqa1JleHl6Y0ZqUUc0VlBldUdaZFFoaHVIRnhycjJwd0E0N19sUWJPQQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **20.98** | **5.77** | **13.81** | **26.10** | **1,572,426,743,808.00 USD** | **-7.41** |
| GOOGL | 14.61 | 5.22 | 18.03 | 24.70 | 3,440,352,690,176.00 USD | -0.32 |
| SNAP | N/A | 4.66 | -72.44 | 18.90 | 9,030,995,968.00 USD | -29.74 |
| PINS | 56.94 | 2.71 | 35.39 | 18.20 | 10,963,820,544.00 USD | -40.45 |

Peers fetched as_of: 2026-10-30; META reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

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

- https://news.google.com/rss/articles/CBMiogFBVV95cUxPRVBPRktCcEhZbWhwNHJ5LTdQWGNnbG9PNEhtUzV4ZzZPZ2V4blA0MmdZQmJ1OTdqZkdQMnVXODhDSHlpdjRXam1BT2xjQi1WZXZhUXJVanRaajgxMVFPeVJtQS1Nd2Y5ZDQzb204ZW82NkNubFZSUUhLWHZKM3JVNDVmVDEwa01rVk91WXVZa3ozaEhqeUdfODZacjIzUTFuRmc?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxOZUJjVTVVd19qajRKZEtjUEZRUEk3QW1oc2JVRVdVQmNiRVI1VTdJcmxNcXBCQm8weE1oV0lJTjZKejVYaGw5c09FQS1KVy03b3N4cmVJVGZBQXJ4dUUzM2RMdkI0Y3FMMnZPTTl1Wkd2LVlDN29JTGVMNnV6TXR0QlNlYXJabUU?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOQWNueG1FVWtlamZtX2VsZ1pNcS11bDJ1SUdqakY0ek4zZE92UVJ2RGlPWU1pX1BMS1h0WmhaeGp3NGRNNmtQamJ4WTM3eXhtVzA3SU9ndjNkYmk0ZXk2U2R4aUZvMEVzZldnQUhwR3BiemdpaGM1SzRnc2c5YnY2dG5GMDFMZVVSd1p1dTVndjU?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQV2NoTk5hV1FvZ3FFN0tVT2Rxd05GV1IwUTNMaGN1Sk5weWh5NUdWY0JKdTNrYUMzRGpXeFl3X0ItQmpkUkplNThhT3h4UUVMV05hTUJSUHBNZXhyS0doOHR2X2FwakxtdkVxdkVGamJiaUV4X2FsUkMxb0VSZkxYLU9yaWRFaUVQN0oya1JmQzZYNENRTGNvVA?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQMVdfQUVqN2RXcmU5T1Z5OTBoWEFYMXlKU3N4SnRIcVV3bXhocEhQM1E1QTFHUkJZMkNFaVg3SUdXQm9OcGZ1aGx5XzZEQXZ4b3M0OVA4ZDFra19qS0EyUzdIeUdnMHlJR1NFVmo1ci1HSlVrN1V4VmJRLURXZDFHNjRSMEl3UnpNWVpFLUMxVUxHeGEtbjlNck9nZnB6cUZLRGdmclI2ZnRtaklIQy1PTm0wRXc?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNdVlzQ3pfeDlpYVJ0TjRSX3padDdtb2NvaWNmOW9HQ0dQQzRubEdVU2E4ZTRhWE9WVGFpYjFweXdpUFd5UV9xNFZvZGdqcDE2Sm5aNGt4cXlTMllQYVBtSXRlQmJneG5JdTJXa0xDX3EtdVhRZTFMN2tFNzNEV19NbXA5REoya1I2Z3o2ZWgtVXBFQ3I3MU9ld0gwV2k1N2pTNy1ITDM4cnp3TEdpME1qbWxVQjdUc0ZKRFl4WlRxNjdzSm9PYlFZ?oc=5
- https://news.google.com/rss/articles/CBMiUkFVX3lxTE9NdF9xWW1RaDk2MmNFdk5acnJHSVhGM0dqcF90M081cUplRkpyVjZmakJsdS11TFhOcnVVRnM0T1RXcEo5ZzBITzA1N1BsaWVacVE?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPeEFsRjB6d2lwTVZ1UWhyVnhEZmkwRG9rQmo1dVp5d3plSFNEVzZHQllCakFVdXJaM2dQUklnQTEwMHp6MDlud0pmOERnSFVpeEtuMFY1ZjFGMmtkcGFlN2JSUVVMLTBDNEJqazJDUXVRWTBFczdKTXJVVTlXcHk2VHZJUE1aTTVfZm1uM2YzRQ?oc=5
- https://news.google.com/rss/articles/CBMid0FVX3lxTFA5WXQzNmRlc3JsVFdGZkFSWXhtRFlQX2ZzQkpRa0VlTmZxNFBpQmZJREZrZGR3YVI1SHBnR2FjVE1VOF9EYVBsWUctV3ZxVnc2QWw1MDB4REpGY0ExZWRoRnh4aHJlU1c5RW5Xa3lBTnVaQXlTNVZR?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQdHR6ZEd6RloxRHdXdUk4cDVPUmJuX3ltU1NiZjh3RHFQc0R2LVdUaVZPdEYzelIxQ1JrZUpMampCVFM1ZGhOeXZoajJZdVlWb2p3SS1lbWlQMFlYVnVxYnpNdE1EeVUxeFlNZEhsVE9jQzQwQU5GdEVvcDhudnd2WXdNNEhwN3BPSDVFZGNBXzdxenhqT1hyMVdBMjM0M1lWclhxcWtB?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOVBsWC1HZmNiRnJHT3RIbzlmcmZLZVpRVVlibk5sMFhyLUJfSHVtZlhxNzBLWkJ6RkgtWWprZnl2ZUVCeVBzb3NOVzlJQkYwbjBvVzQtaFZDSk9rZGxlYWVjMEJnWFY0LVFiUVM0S2J1T0ExVTJMcFY4QjJ1ZDgwNVVrVEpENFpJMHVrRkpoVXJvSTktOE9fMU94dnpLR1UxWWlSTFVHallWRG1DTDBhNXJobzJpek5UeTk3dUFRZl9QMnJhaGo1OXo3TUhSeEg0LTVQeHZiZ0NuZw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQZDZCVy1CLS1KV1plaWZjVXo4UnZuWWVXbGRQNmtQcTRlM0lIeHBnaE5tVGg2dzN0MFJ2N0tQejFjbklESHhoTS1UX2p4SlUzQWhUZXFZTzJGM2NpTDFGUHJRSXVSS0N3YVpYRG9fUEM5Z2dMQmdYbkV0TEZkYUIxMUtWT2h3eVR6MGhqRFFUeFVqdklVQzd1TzlLeUw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNSzVnUFl0aGpRRFVlalhrS21zWkJYNmVMMmtldEpsaTR1djVpNFNqWEpfWVN1bzRELU50b0xDLUNzUGhZVjJTS3NZQURWblJCMF9vdDdmd3FzcHl2NWp5SlV5anNKWWthSG9HVk1TVVcyMGhkWWExQmlDZndUdElGSVNoamdSN0pjMlJ5ZmZvZDZYSVNPeFl3?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOM2xkR0Z4TFBwOUVtd2JTOFNTWmJOdENmNU9kUXViMXNlZVBHTEpwYzhaUzcxelZsNmFRQ09PdG1iTmFKOEdaOUFhVU1MNFhiWERYN0trQVc4WUtubGVWaEtwRnphTzFRX3UtU19SUUZYclpRNlB6YWV0ZnFIN3VKXzUzSG5IOEt1YWpGRXBXUnBBOUVvdE1uaGtJcw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNY3RFaF95TzNuUUhqODJYMkJYY0lNRkN1Qm1ydUtDTW40Y0sxUlQ3bXNwMzVVM0NTSTdKZjlqZXBoUjJ4cGs4TjBPSUZjZnhJNkN5eTQwMUtVOThqYVNNY1VCSzZKLUtlWVlsZEJJcTdOVVVoakV5ZmwyVzhIYi1MRHhER3ozS09pVFZGeHdWWkw2N215SHVoYTF1R1VHZ0p3?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNdmR1WjllZWo5S013MU1kTmgzNWdZXzd3ejl4bHZFRlR6NUpLbWt5aHdaYkpzc3g4eG55M0Q2UGVHb01oSHBIUWZyY0tzTHNzMlU2clZ6NVFoZmJ3clRtYkZLWHFsWElfRHRibEw0UkZYMUNtQzNQcFVtejBQUjM4QVh6Yk9LdVMzOENZU1U3S0syTWRxSU9zdmFkQUlLY2hVQkFtVlFrN3lseGhEcWNPdA?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE10bm9vdXZ0RDJuVWNfMGo5bnQtLTJ6b2c3WTlMNExXaEsyOUpiNEd0cGt0YVNldlZHNEtvaThTOXV3LUpBVEFmcmNOOTBSZDNPbTBmNGlFVzgwYkFqQmY2eExVUjR6UEEtNk1hNzdkWEgtTWs2bTZNbGl2a0hOUQ?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxOS0FRMjYzYmNENmdZSkQ5TEdXdXBPeUFXUkc4WDBWcG91a3dJQTlQbVNpQ3ZTLVl6UUZLM1BVUEZ1dnBlc2steXQ3clVEb2paeWV6eWlRem9pbWkwUVVueFN0TU5rWE93MnZyb2tNNkdueXJoLU0wSUFZM3EtTWJWUTRPZG42UExzUS1DXzh3?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOQmZGYUxTaGtySHU1dFlpTTZGQ3pKdlJ6dEYyOThIZGJRNVZqVkFfYmpLeHpvQUhPMmR1Y3lVLWcwclFjUEtIU2R6LVBva2VyLVNtdTRUNEYxM0NNenJNeVdoeHhyTHVYMzI0eVdOQ3l1UVZ4d2lCT0M2Wk5oZUdqTmdUMmRvS04zT1BWb01CWXd1cGF1VXBIV0tTWUkxM19ZVzR3cnlFLVRwR0lDS2djSzlaVXd6RTQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOckVjQjluT1BwSTlMUFpCMjVielcySEVLU0hmQjhpUVZ2YlRxTlVyZ0Rnbzg2SGd4ZzNldDRZck96SFZ2UFkyVEl2RlJOTGFxZDU4RXc4Sms3aHpITFNYZ0ZCbFJ4ZWkwWEs1c1ZTQjFMSmt1TlNQbFRFaDViLWZBU1FHUDRmcnY5NXlMY1VEUUU0cTVVT2c?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxNTnBGN0VHMkVnVU15TE1iaS1ZMDVSYklISTZVdzFidFlFcVVkN05NVG9Ldm9rYnlFc2NjNjh4NVNscE9mZ1VuSTNqcjFqVHd5eXlycGRwb196ZE8xQ2wySGx4WE5lZHNrblB5RnY1NjZmUzNEbGIweXR5cWJWa3hsQm5n?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxNN3hiMUxqR2tHRWdQY2xwX05JVVU4My1BWnpLdzJadkZ4bWJYT0N4T015RTdjcEQySF8xR2lBWElsM1JadEU2V2pVSkRHYXhORUhEZkdjSk5HQVBCOC02S0gxODNwLTZTa0lrTXg4VXBCQWJzV3FfSThBZnRnemZ6c0I2YkRHZVVmenNDY3hrcW0wbVE1UzBCRm5fcHcwRUZHQnlOXy1xVkFNTVVJemlqa1JleHl6Y0ZqUUc0VlBldUdaZFFoaHVIRnhycjJwd0E0N19sUWJPQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
