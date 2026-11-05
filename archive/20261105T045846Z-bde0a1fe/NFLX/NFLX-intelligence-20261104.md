# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:16:41.712929+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 6, 'ai': 11, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'directional_claim_without_event_type': 2, 'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-10-30

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 66.3900 |
| Return 1D (%) | 4.6831 |
| Return 1W (%) | 7.0979 |
| Return 1M (%) | -0.9991 |
| Return YTD (%) | -29.1916 |
| Return 1Y (%) | -39.2567 |
| Annualized volatility (%) | 36.1424 |
| Beta vs SPY | 0.2352 |
| Max drawdown (%) | -46.4449 |
| Sharpe (rf=0) | -1.2041 |
| Downside deviation (rf=0, %) | 26.3803 |
| Sortino (rf=0) | -1.6497 |
| Historical VaR 95% (1D, %) | 3.5133 |
| Historical ES 95% (1D, %) | 5.1308 |
| Correlation vs SPY | 0.0835 |
| Tracking error vs SPY (%) | 37.3306 |
| P/E (trailing) | 19.19 |
| P/B | 9.31 |
| EV/EBITDA | 17.67 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 17.60 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 34.63 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 9.22 |
| MA50 | 71.6790 |
| Close vs MA50 (%) | -7.3787 |
| MA200 | 81.2405 |
| Close vs MA200 (%) | -18.2797 |
| RSI (14, Wilder) | 47.4511 |
| MACD (12,26) | -2.2994 |
| MACD signal (9) | -2.3568 |
| MACD histogram | 0.0574 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 66.3900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 4.6831 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 7.0979 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -0.9991 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -29.1916 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -39.2567 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.1424 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.3803 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.6497 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.5133 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1308 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0835 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.3306 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2352 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -46.4449 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.2041 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.6038 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 34.6320 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.2155 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 19.1879 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 47.4511 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0574 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.3787 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -18.2797 -> Clearly below the moving-average trend level.

## TAILWINDS

### Netflix Inc (NFLX) Stock Up 4.7% and Still Undervalued -- GF Sco
- Summary: Netflix Inc (NFLX) Stock Up 4.7% and Still Undervalued -- GF Sco
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOQjB4ZnhxdjRJYnpHZkpOX3hJRV9Od1FQSFNIM2FrTjVOemI4T1ppODdhZF96WkNPc2wxcTB1M24yY1M3WmRScldnTTQ4UzJqUzN1Q0JUX1IwcGhZTUEyRjljcG1YcklMajV2bjd3cjlreV8zV1JvZUlZNmpFSjF1M0t2NXd4NDJ6VEhlU3FUYjNjR3FUMlYwUlJWckFSUlRzSjlpcXlySQ?oc=5>

### How Much Should One Number Worry Netflix Stock Holders?
- Summary: Analytical focus on valuation metric, no event.
- Date: 2026-11-01 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQVllxOXphY0ZBQ19kR1h0aFpjU0VDenQ2SktFanRqX25FNThHc1F1d2Rob0laOHhFamZlLVFmLTEwTThLY1p0OWRld0hkWmd2OUFmc1VQeFZmMDdQNVJ1RmZ4YVRxdndnTWh6akxHZThuT2YwT0VHaTdrOExCVEs5b09Ud2piWmhuZFRVY2x1RjA2a1BSUkhrclRaeTFzS0VheHY2YzNGWUk5WHE0OTVHMTRKZ1BfUQ?oc=5>

### Netflix Stock Is Trading at a Historically Low Valuation. Is This a Generational Buying Opportunity?
- Summary: Highlights low valuation, potential buying signal.
- Date: 2026-11-01 | Impact: medium | Horizon: medium | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxPQ1lRWWc3cEFBTEVxNzlnRHUyYnVvdGV6MElkWmpmUGI2M1NSclZZQ291RDd5ZEdsZE5uMVhpMWxtclJYY0dSNGZ4cExGWWpvel9kUDc4QWVPR2xuWjNyQi1fWmNRZ0NGaG9xTHlNdVhxZ3otM1ZDRGpTV1c3bE05ck9zYnpDZ2N2b2MwdDNyVUhYLXRkb25DNzFiM2lXX1dvdjh5Nm43OXBMdHM0WUNHU2h5RDcwSzdEMW9BZlo4ZnhhWHZSVWxYY21PQjJoZmt4cWlDalEyQ3U?oc=5>

### Bill Ackman: Netflix “an Incredibly Cheap Stock” After a 55% Drop. But Is He Right?
- Summary: Bill Ackman comments on Netflix’s low valuation after a steep decline.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxOUjIwXzNqX0p6UTJSTzlwYUkzNUZEdUVqWVo3cjBWdjJhcld6VFNiN3RQcnZLazA0ZWdVUHd5X3d1ZDVjeU1WaEFIOHUzVnRmN1dERU5WeEtYaTBXclZIS1A1ZDBwX1A4aGh3YVV1LVJDOGV0QW1JdG94NnlUMGh6enFtellRajlXWWkwTmZBbzkxQ2xsNHRIQ3d0OXhyc0RBRUtoOEJaOVFzY09hb2JmS2N5djVfZUxEMEVmV1NhSXZ3b3EzdldZSlcwQlVSX096NlFQeFJPMGNEYWprRmkyWm4zb1QwZjlNVFE?oc=5>

### Netflix (NFLX) director Strive Masiyiwa receives options with a $62.34 exercise price.
- Summary: Director Strive Masiyiwa granted options at $62.34 per share.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQR1JJT2J3ajhuUFdIQ1ktWGFuN3JBb1laWnRGUERRNmdha3pwMzE0T0xkUHNIR2xaZGtLYVNNTHVybkZmZWZPeUpXNTA2MjZxWXFBRWZDWVBYb1p1VGdaUS0zdG9KRFFIWGFaaE5XaDlPRjVyRS1pUTN6dE1PYVh4dG9VeUZpVzExQTRtOFBHQml5dGItaGVVdUdDSXR0YXRfS2JRLXpDQ2w?oc=5>

### Netflix (NFLX) grants director Bradford L. Smith 1,003 options exercisable at $62.34 per share.
- Summary: Director Bradford Smith granted 1,003 options at $62.34 exercise price.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNMnpxWWhrMWc4STYzX3Q3THJaMDdBZTJLalc2eS1Eb05QLW5kQ21mbkl1Mk1CcXNqTm5GYlJfMmI2RERvSnNPTGFoMmhDbU4tREZPX2NhdDAzeXl3VmIwbjd2UXpxRHFrSDhabGtjQ3NuSUdRVW8xUnlvU1c4VXhCZEViNURLNG9CTThXUzd1dDdDUGdCOVNjTDlvc2dIWlNJS2x4ZF96ei0?oc=5>

### Netflix (NFLX) grants its accounting chief 1,170 options with a $62.34 exercise price.
- Summary: Accounting chief awarded 1,170 options at $62.34 exercise price.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQT0tuMkE4RVh5NjNmY0ROX0otLW9SR3c1djVSb0c2b1lpa3NrbDBENmNtTjE1VnRfRVRNQ0ZUc0hURWV2SXRaOFBsY1ZyNWFLdHFQU19XT1FHbDdJTFFkRnFjc21TNjR3bEFSbmFhdHZ6T3EyZmRJaTRxLUdwc0hDRG1oT01kLU54ZzBuUVZjWWpLbGxaMEJrSXVwcWNEUDZILThrY2dJR00?oc=5>

### Netflix (NFLX) grants Ann Mather 1,003 options with a $62.34 exercise price.
- Summary: Ann Mather granted 1,003 options at $62.34 exercise price.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOTDBjLVFwZllzX09NVFNSc1NnS2xCSjlJenVuS0xpcUZlNkl4bGlWNTNxNFF3d1lDVW03UGhJeGU0cVBhZ05VTDZRc0J4ekhxbllEUWZhaC1ucFdkR1Blc21tYWozZmxtU0k3RTlIcDZ0RW1hSzNqYlJlRnBidGNrWVhROFBJaVhKVjg1QVFrMjI4WThYeFFEOFFTZDJoUUFxaFRLYTlEQVI?oc=5>

## HEADWINDS

### How Investors May Respond To Netflix (NFLX) Lower Ad Revenue Guidance
- Summary: Lower ad revenue guidance may hurt investor sentiment.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNTmpuUm0tQldPM0g2UUNrdFpYUHVvZ05XM3JUVTVzYTVQV3JwSFJWRFM5aU14dlRGbDFHWUhaNDNsWXc4ZEl2RVVtcXRLN29wMU1xRXJGQWVQemU1MkZYMmRDVXFkMjgwR0txQkpza0phNXZFbWlCbzJNZ0VNek1sRmFiczNjVEF2UEFhcTV1ZW1sRDNwWHBBdG5qTE9Fc2Z5?oc=5>

## CATALYSTS

### Netflix's U.S. Audience Engagement Problem Is Hurting The Stock (Rating Downgrade)
- Summary: Netflix's U.S. Audience Engagement Problem Is Hurting The Stock (Rating Downgrade)
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOY3JYbDhETktQMDhGRklxQl8wM3d0YkFPdGpia3dkaFlXdUxlczVzVlFBTlVVTkRUSWw4MF9PbHZyazd5bE9EejVzR2ZBVmowNTZ2dWZuMDZ5aGhZQ3IxS3VkMmg0TFBDSFAyQ0R3OGxIMklaLV9xUEdLZGY4Q0VxTWFsal80OUZuQjRXSUZ0QUNxR2x1aTgwcVhGUnlKY1RoblJkZGZuNjlIVHZtWkpsd3ZzYWFiSUZ1RlE?oc=5>

### Netflix's Problem Isn't Profits. It's Viewing Time.
- Summary: Netflix's Problem Isn't Profits. It's Viewing Time.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOVGhjVDQ3VGtkNk1paC1uSjIwOUYweC1FRmI3YTlHU1JpaXBsTzN5UkhsYkQ2eXVKRUdTX0JnSHNPWk1PeGVfYVJRQjZTLXB3ejR1TEhiS19BX0NzV1VNSk95OTRkV3hXZHpTdFM4V2pQQTl1aXFYUlJyeldDQWYxTk5NMndJaGROdGRVeks4WVJTeDQ?oc=5>

### Netflix, Inc. $NFLX Stock Acquired by Provenance Wealth Advisors LLC
- Summary: Netflix, Inc. $NFLX Stock Acquired by Provenance Wealth Advisors LLC
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPTHJ2Z29EV3htXzNqRjFCTUM0THRBeDlPSmtqUzRtMUFURFJCTU04RzU2ODVIcHNLbXFHWTdYVkNUaDJUVzlVaHhWM3NCMXFmbmhMaTZqZVgzcXJFel9ubmtfSHVfdVY3VHB5ejkteVItNGoxSXhSYldZZ0RHRnNSdUdSTlRtUlBvd2lQZk8xZE1xVHJlRkw4NjRtR2E3eUtJdUZtRDR5T2JVTXJnYlR3UW9jc2F5SHZVaXBYcnNfMkExNmJt?oc=5>

### Netflix, Inc. $NFLX Stock Bought by Markel Group Inc.
- Summary: Netflix, Inc. $NFLX Stock Bought by Markel Group Inc.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQRzh4YkdwZG9XakQ2bmxidTJicUg3TmhzbFkxRHNkUzhVaFd4SHdOblEtWUtjaWtINmxMUWFKXzNnOTk3V29CVjJybFBuaG9VMExFRWtJOXRETlZHd1RRTjRYckE5OEd6SGhVNTV2SFo3VTJtTkpHME1kcEhWb2pWWll0dnB6SFpranVqSk5vQ1FoWE55alJRUDVyal9CVG01S1VqZjVVRmdfSHJxME9Z?oc=5>

### Netflix Unveils ‘AI Discover’ To Take The Guesswork Out Of Streaming TV
- Summary: Netflix Unveils ‘AI Discover’ To Take The Guesswork Out Of Streaming TV
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPVmFCMjkxWERhcDluVjRRWGIyOTkzR3RSNXNHSGsxRGhZa1FoY1BDcEdkQXBOVER6WXIxcjJjYnBDOTBNemJOak9kNDBzV29CaDBLX2hPN19BUzJSQTJMU0taNzdzZE1QUUJQVkpGWHBPUE5QWm05NTl6eld4Zm5qaVVCVEs4Q2UxR0pSdUVZWDdGZGFwV2ZPc1djNWRNRVRfUnc0cEF6MXhaSHJjRnA2SzVSNUZXTlBsWlJsWkRBTEp4enZ3aW9Ed3NB?oc=5>

### Netflix Inc Stock (NFLX) Moved Up by 4.85% on Nov 4: What Investors Need To Know
- Summary: Shares rose 4.85% on Nov 4, indicating positive market reception.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNREFiOGpzM3NvWHVsQWF0SFEzTW9UQWx5Zzc4MjVjRmhsVDdnTG41SWIwWGpxZXNySkZ4ZGd6TTJwUC1DZWJkMHhjRUZwbXBLYS1jUm5Od2tTb3RtSGlSSmRVaDFhbG5jWWdWMDRsOEJfNlhyY1RXRENrM2tCZUx2bFI5bllCdEg2cGVN?oc=5>

## RISKS

### Is Netflix (NFLX) A Bargain After Its 2026 Guidance Reset?
- Summary: Investors question if Netflix remains a bargain following its 2026 guidance reset, suggesting possible long-term downside risk.
- Date: 2026-10-30 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQYXFIRXR2UFNyNHdHZFVwM0FwMVQtdVhKRU1VTWljeTQ2Rm1qYVVWeERlaklHVklBU0pyNjRaUWZGYXVhOGJMZ0h5TmRpVERTTDVoZkJ3eW5OenNfcVhnUEhLLVBNY0VqSGdVRlZMS2FwWlgweUcwckJ3ZmYwc2dJb3lScWI2VFdKNmc3aGdpUGJFdTVVZFpIaW9qR3ZGSmN0?oc=5>

### Netflix (NFLX) legal chief sells 5,727 shares at $64.55 after stock awards vest.
- Summary: Legal chief sold shares, potentially signaling insider concerns.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNUGduLTYzT1RDRHR5WFROb1JiZ2swX0tOaDNKeTRUd1o1VndVeEt4dWg5cm52S0hFRFRvbEJ5UzN2S3ZEMVN6dGZpTWFPMWZ5cWpjNmpidjRjWGRSNXpta3lKMThQT1BPZl93MEFjYXVKQTZuSmdkYU9KQUs2M1lzdTBwSGdDclljWVhmdUU0WXU3a2o3bnB1Rk5sbHdHVi16dERPMWstUHI?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **19.19** | **9.31** | **17.67** | **11.80** | **276,443,955,200.00 USD** | **-39.26** |
| DIS | 23.55 | 1.87 | 12.07 | 6.80 | 205,389,398,016.00 USD | 8.26 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 7.86 | 0.95 | 5.01 | -6.10 | 88,242,503,680.00 USD | 1.80 |

Peers fetched as_of: 2026-11-04; NFLX reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 12,874,176,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,663,927,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipwFBVV95cUxOQjB4ZnhxdjRJYnpHZkpOX3hJRV9Od1FQSFNIM2FrTjVOemI4T1ppODdhZF96WkNPc2wxcTB1M24yY1M3WmRScldnTTQ4UzJqUzN1Q0JUX1IwcGhZTUEyRjljcG1YcklMajV2bjd3cjlreV8zV1JvZUlZNmpFSjF1M0t2NXd4NDJ6VEhlU3FUYjNjR3FUMlYwUlJWckFSUlRzSjlpcXlySQ?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQVllxOXphY0ZBQ19kR1h0aFpjU0VDenQ2SktFanRqX25FNThHc1F1d2Rob0laOHhFamZlLVFmLTEwTThLY1p0OWRld0hkWmd2OUFmc1VQeFZmMDdQNVJ1RmZ4YVRxdndnTWh6akxHZThuT2YwT0VHaTdrOExCVEs5b09Ud2piWmhuZFRVY2x1RjA2a1BSUkhrclRaeTFzS0VheHY2YzNGWUk5WHE0OTVHMTRKZ1BfUQ?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxPQ1lRWWc3cEFBTEVxNzlnRHUyYnVvdGV6MElkWmpmUGI2M1NSclZZQ291RDd5ZEdsZE5uMVhpMWxtclJYY0dSNGZ4cExGWWpvel9kUDc4QWVPR2xuWjNyQi1fWmNRZ0NGaG9xTHlNdVhxZ3otM1ZDRGpTV1c3bE05ck9zYnpDZ2N2b2MwdDNyVUhYLXRkb25DNzFiM2lXX1dvdjh5Nm43OXBMdHM0WUNHU2h5RDcwSzdEMW9BZlo4ZnhhWHZSVWxYY21PQjJoZmt4cWlDalEyQ3U?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxOUjIwXzNqX0p6UTJSTzlwYUkzNUZEdUVqWVo3cjBWdjJhcld6VFNiN3RQcnZLazA0ZWdVUHd5X3d1ZDVjeU1WaEFIOHUzVnRmN1dERU5WeEtYaTBXclZIS1A1ZDBwX1A4aGh3YVV1LVJDOGV0QW1JdG94NnlUMGh6enFtellRajlXWWkwTmZBbzkxQ2xsNHRIQ3d0OXhyc0RBRUtoOEJaOVFzY09hb2JmS2N5djVfZUxEMEVmV1NhSXZ3b3EzdldZSlcwQlVSX096NlFQeFJPMGNEYWprRmkyWm4zb1QwZjlNVFE?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQR1JJT2J3ajhuUFdIQ1ktWGFuN3JBb1laWnRGUERRNmdha3pwMzE0T0xkUHNIR2xaZGtLYVNNTHVybkZmZWZPeUpXNTA2MjZxWXFBRWZDWVBYb1p1VGdaUS0zdG9KRFFIWGFaaE5XaDlPRjVyRS1pUTN6dE1PYVh4dG9VeUZpVzExQTRtOFBHQml5dGItaGVVdUdDSXR0YXRfS2JRLXpDQ2w?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNMnpxWWhrMWc4STYzX3Q3THJaMDdBZTJLalc2eS1Eb05QLW5kQ21mbkl1Mk1CcXNqTm5GYlJfMmI2RERvSnNPTGFoMmhDbU4tREZPX2NhdDAzeXl3VmIwbjd2UXpxRHFrSDhabGtjQ3NuSUdRVW8xUnlvU1c4VXhCZEViNURLNG9CTThXUzd1dDdDUGdCOVNjTDlvc2dIWlNJS2x4ZF96ei0?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQT0tuMkE4RVh5NjNmY0ROX0otLW9SR3c1djVSb0c2b1lpa3NrbDBENmNtTjE1VnRfRVRNQ0ZUc0hURWV2SXRaOFBsY1ZyNWFLdHFQU19XT1FHbDdJTFFkRnFjc21TNjR3bEFSbmFhdHZ6T3EyZmRJaTRxLUdwc0hDRG1oT01kLU54ZzBuUVZjWWpLbGxaMEJrSXVwcWNEUDZILThrY2dJR00?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOTDBjLVFwZllzX09NVFNSc1NnS2xCSjlJenVuS0xpcUZlNkl4bGlWNTNxNFF3d1lDVW03UGhJeGU0cVBhZ05VTDZRc0J4ekhxbllEUWZhaC1ucFdkR1Blc21tYWozZmxtU0k3RTlIcDZ0RW1hSzNqYlJlRnBidGNrWVhROFBJaVhKVjg1QVFrMjI4WThYeFFEOFFTZDJoUUFxaFRLYTlEQVI?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNTmpuUm0tQldPM0g2UUNrdFpYUHVvZ05XM3JUVTVzYTVQV3JwSFJWRFM5aU14dlRGbDFHWUhaNDNsWXc4ZEl2RVVtcXRLN29wMU1xRXJGQWVQemU1MkZYMmRDVXFkMjgwR0txQkpza0phNXZFbWlCbzJNZ0VNek1sRmFiczNjVEF2UEFhcTV1ZW1sRDNwWHBBdG5qTE9Fc2Z5?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOY3JYbDhETktQMDhGRklxQl8wM3d0YkFPdGpia3dkaFlXdUxlczVzVlFBTlVVTkRUSWw4MF9PbHZyazd5bE9EejVzR2ZBVmowNTZ2dWZuMDZ5aGhZQ3IxS3VkMmg0TFBDSFAyQ0R3OGxIMklaLV9xUEdLZGY4Q0VxTWFsal80OUZuQjRXSUZ0QUNxR2x1aTgwcVhGUnlKY1RoblJkZGZuNjlIVHZtWkpsd3ZzYWFiSUZ1RlE?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOVGhjVDQ3VGtkNk1paC1uSjIwOUYweC1FRmI3YTlHU1JpaXBsTzN5UkhsYkQ2eXVKRUdTX0JnSHNPWk1PeGVfYVJRQjZTLXB3ejR1TEhiS19BX0NzV1VNSk95OTRkV3hXZHpTdFM4V2pQQTl1aXFYUlJyeldDQWYxTk5NMndJaGROdGRVeks4WVJTeDQ?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPTHJ2Z29EV3htXzNqRjFCTUM0THRBeDlPSmtqUzRtMUFURFJCTU04RzU2ODVIcHNLbXFHWTdYVkNUaDJUVzlVaHhWM3NCMXFmbmhMaTZqZVgzcXJFel9ubmtfSHVfdVY3VHB5ejkteVItNGoxSXhSYldZZ0RHRnNSdUdSTlRtUlBvd2lQZk8xZE1xVHJlRkw4NjRtR2E3eUtJdUZtRDR5T2JVTXJnYlR3UW9jc2F5SHZVaXBYcnNfMkExNmJt?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQRzh4YkdwZG9XakQ2bmxidTJicUg3TmhzbFkxRHNkUzhVaFd4SHdOblEtWUtjaWtINmxMUWFKXzNnOTk3V29CVjJybFBuaG9VMExFRWtJOXRETlZHd1RRTjRYckE5OEd6SGhVNTV2SFo3VTJtTkpHME1kcEhWb2pWWll0dnB6SFpranVqSk5vQ1FoWE55alJRUDVyal9CVG01S1VqZjVVRmdfSHJxME9Z?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPVmFCMjkxWERhcDluVjRRWGIyOTkzR3RSNXNHSGsxRGhZa1FoY1BDcEdkQXBOVER6WXIxcjJjYnBDOTBNemJOak9kNDBzV29CaDBLX2hPN19BUzJSQTJMU0taNzdzZE1QUUJQVkpGWHBPUE5QWm05NTl6eld4Zm5qaVVCVEs4Q2UxR0pSdUVZWDdGZGFwV2ZPc1djNWRNRVRfUnc0cEF6MXhaSHJjRnA2SzVSNUZXTlBsWlJsWkRBTEp4enZ3aW9Ed3NB?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNREFiOGpzM3NvWHVsQWF0SFEzTW9UQWx5Zzc4MjVjRmhsVDdnTG41SWIwWGpxZXNySkZ4ZGd6TTJwUC1DZWJkMHhjRUZwbXBLYS1jUm5Od2tTb3RtSGlSSmRVaDFhbG5jWWdWMDRsOEJfNlhyY1RXRENrM2tCZUx2bFI5bllCdEg2cGVN?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQYXFIRXR2UFNyNHdHZFVwM0FwMVQtdVhKRU1VTWljeTQ2Rm1qYVVWeERlaklHVklBU0pyNjRaUWZGYXVhOGJMZ0h5TmRpVERTTDVoZkJ3eW5OenNfcVhnUEhLLVBNY0VqSGdVRlZMS2FwWlgweUcwckJ3ZmYwc2dJb3lScWI2VFdKNmc3aGdpUGJFdTVVZFpIaW9qR3ZGSmN0?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNUGduLTYzT1RDRHR5WFROb1JiZ2swX0tOaDNKeTRUd1o1VndVeEt4dWg5cm52S0hFRFRvbEJ5UzN2S3ZEMVN6dGZpTWFPMWZ5cWpjNmpidjRjWGRSNXpta3lKMThQT1BPZl93MEFjYXVKQTZuSmdkYU9KQUs2M1lzdTBwSGdDclljWVhmdUU0WXU3a2o3bnB1Rk5sbHdHVi16dERPMWstUHI?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
