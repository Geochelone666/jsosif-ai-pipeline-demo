# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-11-07**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-11-07**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-08T04:26:18.969775+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 7, 'ai': 13, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **14** exact headline/source/date matches; prior report **20261107T043155Z-acc5f41d/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **5**; {'directional_claim_without_event_type': 2, 'low_uncalibrated_model_confidence': 3}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 16.0%; oldest publication 2026-11-01

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 63.4100 |
| Return 1D (%) | -3.2794 |
| Return 1W (%) | 2.1424 |
| Return 1M (%) | -7.6867 |
| Return YTD (%) | -32.3699 |
| Return 1Y (%) | -42.1980 |
| Annualized volatility (%) | 36.2852 |
| Beta vs SPY | 0.2321 |
| Max drawdown (%) | -46.4449 |
| Sharpe (rf=0) | -1.3350 |
| Downside deviation (rf=0, %) | 26.6133 |
| Sortino (rf=0) | -1.8202 |
| Historical VaR 95% (1D, %) | 3.5133 |
| Historical ES 95% (1D, %) | 5.1308 |
| Correlation vs SPY | 0.0867 |
| Tracking error vs SPY (%) | 37.6165 |
| P/E (trailing) | 18.33 |
| P/B | 8.89 |
| EV/EBITDA | 16.90 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 16.81 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 34.63 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 9.78 |
| MA50 | 71.0324 |
| Close vs MA50 (%) | -10.7309 |
| MA200 | 81.0409 |
| Close vs MA200 (%) | -21.7556 |
| RSI (14, Wilder) | 39.6812 |
| MACD (12,26) | -2.0303 |
| MACD signal (9) | -2.2449 |
| MACD histogram | 0.2146 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 63.4100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.2794 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.1424 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -7.6867 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -32.3699 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -42.1980 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.2852 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.6133 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.8202 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.5133 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1308 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0867 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.6165 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2321 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -46.4449 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.3350 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.8137 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 34.6320 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.7840 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.3266 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 39.6812 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2146 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -10.7309 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -21.7556 -> Clearly below the moving-average trend level.

## TAILWINDS

### Netflix Inc (NFLX) Stock Up 4.7% and Still Undervalued -- GF Sco
- Summary: Netflix Inc (NFLX) Stock Up 4.7% and Still Undervalued -- GF Sco
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOQjB4ZnhxdjRJYnpHZkpOX3hJRV9Od1FQSFNIM2FrTjVOemI4T1ppODdhZF96WkNPc2wxcTB1M24yY1M3WmRScldnTTQ4UzJqUzN1Q0JUX1IwcGhZTUEyRjljcG1YcklMajV2bjd3cjlreV8zV1JvZUlZNmpFSjF1M0t2NXd4NDJ6VEhlU3FUYjNjR3FUMlYwUlJWckFSUlRzSjlpcXlySQ?oc=5>

### Investors Heavily Search Netflix, Inc. (NFLX): Here is What You Need to Know
- Summary: High investor search volume signals growing interest in Netflix.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxObDB2cXZhTTBKYndDM1lOMlFGM1BEbTFyR21MSVRWM2JrMWxJSUVWNWtQU1ZQLXN2a25sMW54TWxXX3p1eG91Q2ZPNlpSUHlqSzhWaVhnRk9faXdKUmNCaGppSHl4dHBvRnpYRXpIQnIxcE9oZDdFTVRhdFdoOVNQeV9ZQUxNZ2k5QjR6NHc1M29hbGNCNmhBZHJEcjVINzJ4VE9j?oc=5>

### Netflix Stock Is Trading at a Historically Low Valuation. Is This a Generational Buying Opportunity?
- Summary: Highlights low valuation, potential buying signal.
- Date: 2026-11-01 | Impact: medium | Horizon: medium | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxPQ1lRWWc3cEFBTEVxNzlnRHUyYnVvdGV6MElkWmpmUGI2M1NSclZZQ291RDd5ZEdsZE5uMVhpMWxtclJYY0dSNGZ4cExGWWpvel9kUDc4QWVPR2xuWjNyQi1fWmNRZ0NGaG9xTHlNdVhxZ3otM1ZDRGpTV1c3bE05ck9zYnpDZ2N2b2MwdDNyVUhYLXRkb25DNzFiM2lXX1dvdjh5Nm43OXBMdHM0WUNHU2h5RDcwSzdEMW9BZlo4ZnhhWHZSVWxYY21PQjJoZmt4cWlDalEyQ3U?oc=5>

### How Much Should One Number Worry Netflix Stock Holders?
- Summary: Analytical focus on valuation metric, no event.
- Date: 2026-11-01 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQVllxOXphY0ZBQ19kR1h0aFpjU0VDenQ2SktFanRqX25FNThHc1F1d2Rob0laOHhFamZlLVFmLTEwTThLY1p0OWRld0hkWmd2OUFmc1VQeFZmMDdQNVJ1RmZ4YVRxdndnTWh6akxHZThuT2YwT0VHaTdrOExCVEs5b09Ud2piWmhuZFRVY2x1RjA2a1BSUkhrclRaeTFzS0VheHY2YzNGWUk5WHE0OTVHMTRKZ1BfUQ?oc=5>

### Netflix (NFLX) Stock May Be 23% Below Fair Value As Ads Expansion Builds
- Summary: Potential undervaluation amid expanding ad strategy suggests upside.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxQNENZNGtFbTRBN1ZIM0hxVWlIdUZCcDF1NHhDXzdGN2dLbGNrM1Y1cFpqR18xcXl3cTkyRmsxbXE5VnhaNUF0NUxndHgtYmJuR3BTNWZCZXU2bVNFZklOTVBCZ1FiNWtSTXoxcDJ4akNlNlFDWXg5aGhtVTIxRVJtOFk3X3Z0b3A4SjI4TDNWNDV3QmhkY01TZ3RYekROcm51VzlVaHVIZzRXYURFTm42VmhHSkZvWkVNN1lTY1psakXSAcYBQVVfeXFMTk51VXN5Z3ZCeXZyUzlTVW0zRlJoV2U4ZV9UVml5NDFkeU5nRTkxaks3SHU4eGh3bFgxNlQwT3M5T3UyeTFaZDMwa25GYlg2M0RIWVFzZ0pmTkJhdzBWMXQzeUpuYUpEdUhGdnQ1Tkd5RWlBSURyN1N5VmdvQnJQbzlDeFRJdFJzRjl6Sk01Um44MlhpVnhGcUlGX0NkekhkeVVJVXY3UEFpQ0IxTHoxWXBDLTFnNHZVSjZLY1FJVkhsRkZSU213?oc=5>

## HEADWINDS

### Netflix Stock (NASDAQ:NFLX) Slips Despite New Stranger Things Plans
- Summary: Netflix Stock (NASDAQ:NFLX) Slips Despite New Stranger Things Plans
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPd1NLeHE4Skdqd3NHRk8wSEtWSlpVazJfcEZVV0FjT0gzdElUQjEwWUs0LXdqeE9PZTAzcGNiZTJLMHNNS0h6TGVSOExwb3puOU9ybUliWHNsb2pYbnhVWjNQSXo4bjYtWFlWWHRLdWRjbFZ1ekc5c1lWWE95YXB2d1NrMXVjdDliUFJGVktOQUlBM1NBZTRlREhR?oc=5>

### How Investors May Respond To Netflix (NFLX) Lower Ad Revenue Guidance
- Summary: Lower ad revenue guidance may hurt investor sentiment.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNTmpuUm0tQldPM0g2UUNrdFpYUHVvZ05XM3JUVTVzYTVQV3JwSFJWRFM5aU14dlRGbDFHWUhaNDNsWXc4ZEl2RVVtcXRLN29wMU1xRXJGQWVQemU1MkZYMmRDVXFkMjgwR0txQkpza0phNXZFbWlCbzJNZ0VNek1sRmFiczNjVEF2UEFhcTV1ZW1sRDNwWHBBdG5qTE9Fc2Z5?oc=5>

### Netflix Inc Stock (NFLX) Closed Down by 3.28% on Nov 6: A Full Analysis
- Summary: Recent share price drop indicates short‑term weakness.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNZ1FibVQ3b2RIcTlGWk9ITmo2cTVrMEF5WkhvMlBVYjlrcFMtcElfTkI5VEVVZXUzYWpfZUtxcVFNMC1IZzJQcVo3enVSZzVXOE9nLWxzSVdvYldZbmxJQkUtbWFCNG5mVmJSWU14Wldqd18wMjBvV3YxNzFEaTA2blJrWkdKU0U5OHhB?oc=5>

### Netflix, Inc. $NFLX Stock Position Reduced by Boston Trust Walden Corp
- Summary: Institutional sell‑off may weigh on stock momentum.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxObWp6WS1RSURnTG43Sy02dXI5TXpWeFpKdmdIVzFsbGItNG54M1pwUWVqZDBjSDdkV3lFZGwzSDJtUVJQcURrWlgwb2lQWDVNcTJnbEFQdjJ6ZzdMQlIxS3JjRW12bjZFQXlESU9xN1R4bGYtN1N5WlhTZ3J2eHYyQVFrbEVrWkFVcHFjc1BvTUdBc000dy12Q05DX1VSS09oSkd5QWFzNzRlZU5feU5sUzFqb3E2T09ZSWRkNVVBSVFaUnRJaHRv?oc=5>

## CATALYSTS

### Netflix (NFLX) Stock Looks Cheap With 23% Upside To Fair Value
- Summary: Netflix (NFLX) Stock Looks Cheap With 23% Upside To Fair Value
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxPMGF6OTJWMWtVa3V2TU9MWFB6a0JYWHFUdUI1MUlCTGxqQm9ESUNUNnlndHB2cXQyWnBnZ2NYSHoySG43aWlkNm9GVXR0LWJRWTIwNmtabGo1T2cyQTB0YTBfU1EtMEtQU0otczhjR1o1QUVDd0hwcV9kX1BTaDZjUXhYSm44dw?oc=5>

### Netflix's U.S. Audience Engagement Problem Is Hurting The Stock (Rating Downgrade)
- Summary: Netflix's U.S. Audience Engagement Problem Is Hurting The Stock (Rating Downgrade)
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOY3JYbDhETktQMDhGRklxQl8wM3d0YkFPdGpia3dkaFlXdUxlczVzVlFBTlVVTkRUSWw4MF9PbHZyazd5bE9EejVzR2ZBVmowNTZ2dWZuMDZ5aGhZQ3IxS3VkMmg0TFBDSFAyQ0R3OGxIMklaLV9xUEdLZGY4Q0VxTWFsal80OUZuQjRXSUZ0QUNxR2x1aTgwcVhGUnlKY1RoblJkZGZuNjlIVHZtWkpsd3ZzYWFiSUZ1RlE?oc=5>

### Netflix, Inc. $NFLX Stock Bought by Markel Group Inc.
- Summary: Netflix, Inc. $NFLX Stock Bought by Markel Group Inc.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQRzh4YkdwZG9XakQ2bmxidTJicUg3TmhzbFkxRHNkUzhVaFd4SHdOblEtWUtjaWtINmxMUWFKXzNnOTk3V29CVjJybFBuaG9VMExFRWtJOXRETlZHd1RRTjRYckE5OEd6SGhVNTV2SFo3VTJtTkpHME1kcEhWb2pWWll0dnB6SFpranVqSk5vQ1FoWE55alJRUDVyal9CVG01S1VqZjVVRmdfSHJxME9Z?oc=5>

### Netflix, Inc. $NFLX Stock Acquired by Provenance Wealth Advisors LLC
- Summary: Netflix, Inc. $NFLX Stock Acquired by Provenance Wealth Advisors LLC
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPTHJ2Z29EV3htXzNqRjFCTUM0THRBeDlPSmtqUzRtMUFURFJCTU04RzU2ODVIcHNLbXFHWTdYVkNUaDJUVzlVaHhWM3NCMXFmbmhMaTZqZVgzcXJFel9ubmtfSHVfdVY3VHB5ejkteVItNGoxSXhSYldZZ0RHRnNSdUdSTlRtUlBvd2lQZk8xZE1xVHJlRkw4NjRtR2E3eUtJdUZtRDR5T2JVTXJnYlR3UW9jc2F5SHZVaXBYcnNfMkExNmJt?oc=5>

### Netflix, Inc. $NFLX Stock Acquired by Asset One Wealth Management LLC
- Summary: Netflix, Inc. $NFLX Stock Acquired by Asset One Wealth Management LLC
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNYjJOLUdNcGJXV0stckNiMkNsaHFJU2U1akRDLWdIX1kzRXJxM0RXMDlRbGlGUHktdW9JOXZzWWZ0MWMxMUczOVQ2bnFNbnJqVXo4YWREMDZRYW9fUEVENnE3dHpNSXVQS2ZrNDNnRUVMdjBxUExkUEpmUHYyWVB5STR1VVhYS3EtUWQ0eUJma0pPNFJfSlpfeXA0WEl4S0NlTnpUTnk0VmtwalI3S09oLVJIVFlFdmxhS1V3aDlQaDN6MVRfVEE?oc=5>

### Netflix Inc Stock (NFLX) Moved Up by 4.85% on Nov 4: What Investors Need To Know
- Summary: Shares rose 4.85% on Nov 4, indicating positive market reception.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNREFiOGpzM3NvWHVsQWF0SFEzTW9UQWx5Zzc4MjVjRmhsVDdnTG41SWIwWGpxZXNySkZ4ZGd6TTJwUC1DZWJkMHhjRUZwbXBLYS1jUm5Od2tTb3RtSGlSSmRVaDFhbG5jWWdWMDRsOEJfNlhyY1RXRENrM2tCZUx2bFI5bllCdEg2cGVN?oc=5>

### Netflix (NFLX) CFO sells 9,253 shares after 18,428 stock units vest.
- Summary: NFLX CFO sold 9,253 shares following vesting of 18,428 stock units.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNOHl0YUJfcS1vbWtyNTBCRUtnME5wZVRuRlcwVWpsNzc4Mkx1NU5fTEwwM0sxajdNaXBjelp4eS0zOUVXUTQ4Z01mbDNNUXJsRlRKSXpzYkxEX1hwMEQzRzhGLWFMTjJEd0dRUElXbkdYcUEwUTlQN2tRVzcyLVBZY1g5QVVXWVh5cmpHNml0TjVtSFZIUERTQmdUbzYwU1NUNnFQNldyalU?oc=5>

### Netflix: Growth Slows, But Potential Remains Intact
- Summary: Netflix reports slowed growth but maintains long‑term potential.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNNXJUbGZFUmFBTzFZWElwS3J1ZVdiWEc0OEdsVHFsWjd2bm96TGcwTlczX2pMMFNXTXFmeDFYQ25Cc2JVa3RpYXpIT1JWWkZIUDFEQTRqLS0yMkJwT0JGdmNRaGlSTi1SYUVaNUIxQmJHVHYyaDlpTWluNmV5RWNFZHpUNXIzRG5McUljVk8xSnItVUlk?oc=5>

### Netflix Is Playing a Bigger Game. Investors Should Take Notice
- Summary: Netflix outlines an expanded strategy for investors.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQT0JEa2c4OG9JemZzZDJHYjViWGFiaHlzd2UyblkwUjQ1OHRnZC1qNGk5ZzlUQWVILUsxeWQ3NXVPQzBVNEJQNDZseGRNd3BucEYxaDN5bHZYb1BPTHU3bzBZS2IxUzZzdUx5b1Z4MlcwUVgybVhvc20ydlhpMzVlZXJ5Y3lCVlQteUs0TlIwZVQ3RXg4UEJqbmxEU1JwYWRWSDJDM0I4eGI?oc=5>

### Prediction: Netflix Will Begin Paying a Dividend in 2027 and Beat the S&P 500 During the Next Decade
- Summary: Forecasts Netflix will start dividends in 2027 and outperform the S&P 500.
- Date: 2026-11-02 | Impact: medium | Horizon: long | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxObTRWTjFVSXgyTTliSmFpWnpCVkVsalBDemZtQjBZc0J3eEFKcGZLXzFtZlhtaU52c0tmeTVuWnVoODhlbElya0NCSDRSZGFDUHVIS2R2cHdETG01RW1TZmFOWjdKS2wxSFpsU3Z2M2VscmctOV9FQXJMcWV2X0VOYldfMGd1X1NmTHFlTzNSSTh5M1hhQnQ0Sg?oc=5>

## RISKS

### Netflix's Loyal Subscribers Are Not Priced Correctly (NASDAQ:NFLX)
- Summary: Netflix may face subscriber churn due to pricing misalignment, potentially impacting revenue.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPcnRVQjVzNlRVdG1lSXIzSHZMMHhIZ0NycFp6V1lVUjVBdjRyVFV4c1V1LVQ3SE5qRVlRV21XbU1IcUEtLWNPNHo3bHlPc2FUcTExTU9pS2FMMERuZ181TUI5Y3ZJcTltQndNWWZqdFhKQTFMbTNiQ19odDN2YlVnMXpBVVE0cU1tWF81WjFPM1Y3ZG10aXpB?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **18.33** | **8.89** | **16.90** | **11.80** | **260,382,130,176.00 USD** | **-42.20** |
| DIS | 24.07 | 1.84 | 11.89 | 6.80 | 201,590,685,696.00 USD | 7.20 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 7.72 | 0.94 | 4.96 | -6.10 | 86,609,035,264.00 USD | 0.40 |

Peers fetched as_of: 2026-11-07; NFLX reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-07

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
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
- https://news.google.com/rss/articles/CBMiowFBVV95cUxObDB2cXZhTTBKYndDM1lOMlFGM1BEbTFyR21MSVRWM2JrMWxJSUVWNWtQU1ZQLXN2a25sMW54TWxXX3p1eG91Q2ZPNlpSUHlqSzhWaVhnRk9faXdKUmNCaGppSHl4dHBvRnpYRXpIQnIxcE9oZDdFTVRhdFdoOVNQeV9ZQUxNZ2k5QjR6NHc1M29hbGNCNmhBZHJEcjVINzJ4VE9j?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxPQ1lRWWc3cEFBTEVxNzlnRHUyYnVvdGV6MElkWmpmUGI2M1NSclZZQ291RDd5ZEdsZE5uMVhpMWxtclJYY0dSNGZ4cExGWWpvel9kUDc4QWVPR2xuWjNyQi1fWmNRZ0NGaG9xTHlNdVhxZ3otM1ZDRGpTV1c3bE05ck9zYnpDZ2N2b2MwdDNyVUhYLXRkb25DNzFiM2lXX1dvdjh5Nm43OXBMdHM0WUNHU2h5RDcwSzdEMW9BZlo4ZnhhWHZSVWxYY21PQjJoZmt4cWlDalEyQ3U?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQVllxOXphY0ZBQ19kR1h0aFpjU0VDenQ2SktFanRqX25FNThHc1F1d2Rob0laOHhFamZlLVFmLTEwTThLY1p0OWRld0hkWmd2OUFmc1VQeFZmMDdQNVJ1RmZ4YVRxdndnTWh6akxHZThuT2YwT0VHaTdrOExCVEs5b09Ud2piWmhuZFRVY2x1RjA2a1BSUkhrclRaeTFzS0VheHY2YzNGWUk5WHE0OTVHMTRKZ1BfUQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxQNENZNGtFbTRBN1ZIM0hxVWlIdUZCcDF1NHhDXzdGN2dLbGNrM1Y1cFpqR18xcXl3cTkyRmsxbXE5VnhaNUF0NUxndHgtYmJuR3BTNWZCZXU2bVNFZklOTVBCZ1FiNWtSTXoxcDJ4akNlNlFDWXg5aGhtVTIxRVJtOFk3X3Z0b3A4SjI4TDNWNDV3QmhkY01TZ3RYekROcm51VzlVaHVIZzRXYURFTm42VmhHSkZvWkVNN1lTY1psakXSAcYBQVVfeXFMTk51VXN5Z3ZCeXZyUzlTVW0zRlJoV2U4ZV9UVml5NDFkeU5nRTkxaks3SHU4eGh3bFgxNlQwT3M5T3UyeTFaZDMwa25GYlg2M0RIWVFzZ0pmTkJhdzBWMXQzeUpuYUpEdUhGdnQ1Tkd5RWlBSURyN1N5VmdvQnJQbzlDeFRJdFJzRjl6Sk01Um44MlhpVnhGcUlGX0NkekhkeVVJVXY3UEFpQ0IxTHoxWXBDLTFnNHZVSjZLY1FJVkhsRkZSU213?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPd1NLeHE4Skdqd3NHRk8wSEtWSlpVazJfcEZVV0FjT0gzdElUQjEwWUs0LXdqeE9PZTAzcGNiZTJLMHNNS0h6TGVSOExwb3puOU9ybUliWHNsb2pYbnhVWjNQSXo4bjYtWFlWWHRLdWRjbFZ1ekc5c1lWWE95YXB2d1NrMXVjdDliUFJGVktOQUlBM1NBZTRlREhR?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNTmpuUm0tQldPM0g2UUNrdFpYUHVvZ05XM3JUVTVzYTVQV3JwSFJWRFM5aU14dlRGbDFHWUhaNDNsWXc4ZEl2RVVtcXRLN29wMU1xRXJGQWVQemU1MkZYMmRDVXFkMjgwR0txQkpza0phNXZFbWlCbzJNZ0VNek1sRmFiczNjVEF2UEFhcTV1ZW1sRDNwWHBBdG5qTE9Fc2Z5?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNZ1FibVQ3b2RIcTlGWk9ITmo2cTVrMEF5WkhvMlBVYjlrcFMtcElfTkI5VEVVZXUzYWpfZUtxcVFNMC1IZzJQcVo3enVSZzVXOE9nLWxzSVdvYldZbmxJQkUtbWFCNG5mVmJSWU14Wldqd18wMjBvV3YxNzFEaTA2blJrWkdKU0U5OHhB?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxObWp6WS1RSURnTG43Sy02dXI5TXpWeFpKdmdIVzFsbGItNG54M1pwUWVqZDBjSDdkV3lFZGwzSDJtUVJQcURrWlgwb2lQWDVNcTJnbEFQdjJ6ZzdMQlIxS3JjRW12bjZFQXlESU9xN1R4bGYtN1N5WlhTZ3J2eHYyQVFrbEVrWkFVcHFjc1BvTUdBc000dy12Q05DX1VSS09oSkd5QWFzNzRlZU5feU5sUzFqb3E2T09ZSWRkNVVBSVFaUnRJaHRv?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxPMGF6OTJWMWtVa3V2TU9MWFB6a0JYWHFUdUI1MUlCTGxqQm9ESUNUNnlndHB2cXQyWnBnZ2NYSHoySG43aWlkNm9GVXR0LWJRWTIwNmtabGo1T2cyQTB0YTBfU1EtMEtQU0otczhjR1o1QUVDd0hwcV9kX1BTaDZjUXhYSm44dw?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOY3JYbDhETktQMDhGRklxQl8wM3d0YkFPdGpia3dkaFlXdUxlczVzVlFBTlVVTkRUSWw4MF9PbHZyazd5bE9EejVzR2ZBVmowNTZ2dWZuMDZ5aGhZQ3IxS3VkMmg0TFBDSFAyQ0R3OGxIMklaLV9xUEdLZGY4Q0VxTWFsal80OUZuQjRXSUZ0QUNxR2x1aTgwcVhGUnlKY1RoblJkZGZuNjlIVHZtWkpsd3ZzYWFiSUZ1RlE?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQRzh4YkdwZG9XakQ2bmxidTJicUg3TmhzbFkxRHNkUzhVaFd4SHdOblEtWUtjaWtINmxMUWFKXzNnOTk3V29CVjJybFBuaG9VMExFRWtJOXRETlZHd1RRTjRYckE5OEd6SGhVNTV2SFo3VTJtTkpHME1kcEhWb2pWWll0dnB6SFpranVqSk5vQ1FoWE55alJRUDVyal9CVG01S1VqZjVVRmdfSHJxME9Z?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPTHJ2Z29EV3htXzNqRjFCTUM0THRBeDlPSmtqUzRtMUFURFJCTU04RzU2ODVIcHNLbXFHWTdYVkNUaDJUVzlVaHhWM3NCMXFmbmhMaTZqZVgzcXJFel9ubmtfSHVfdVY3VHB5ejkteVItNGoxSXhSYldZZ0RHRnNSdUdSTlRtUlBvd2lQZk8xZE1xVHJlRkw4NjRtR2E3eUtJdUZtRDR5T2JVTXJnYlR3UW9jc2F5SHZVaXBYcnNfMkExNmJt?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNYjJOLUdNcGJXV0stckNiMkNsaHFJU2U1akRDLWdIX1kzRXJxM0RXMDlRbGlGUHktdW9JOXZzWWZ0MWMxMUczOVQ2bnFNbnJqVXo4YWREMDZRYW9fUEVENnE3dHpNSXVQS2ZrNDNnRUVMdjBxUExkUEpmUHYyWVB5STR1VVhYS3EtUWQ0eUJma0pPNFJfSlpfeXA0WEl4S0NlTnpUTnk0VmtwalI3S09oLVJIVFlFdmxhS1V3aDlQaDN6MVRfVEE?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNREFiOGpzM3NvWHVsQWF0SFEzTW9UQWx5Zzc4MjVjRmhsVDdnTG41SWIwWGpxZXNySkZ4ZGd6TTJwUC1DZWJkMHhjRUZwbXBLYS1jUm5Od2tTb3RtSGlSSmRVaDFhbG5jWWdWMDRsOEJfNlhyY1RXRENrM2tCZUx2bFI5bllCdEg2cGVN?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNOHl0YUJfcS1vbWtyNTBCRUtnME5wZVRuRlcwVWpsNzc4Mkx1NU5fTEwwM0sxajdNaXBjelp4eS0zOUVXUTQ4Z01mbDNNUXJsRlRKSXpzYkxEX1hwMEQzRzhGLWFMTjJEd0dRUElXbkdYcUEwUTlQN2tRVzcyLVBZY1g5QVVXWVh5cmpHNml0TjVtSFZIUERTQmdUbzYwU1NUNnFQNldyalU?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNNXJUbGZFUmFBTzFZWElwS3J1ZVdiWEc0OEdsVHFsWjd2bm96TGcwTlczX2pMMFNXTXFmeDFYQ25Cc2JVa3RpYXpIT1JWWkZIUDFEQTRqLS0yMkJwT0JGdmNRaGlSTi1SYUVaNUIxQmJHVHYyaDlpTWluNmV5RWNFZHpUNXIzRG5McUljVk8xSnItVUlk?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQT0JEa2c4OG9JemZzZDJHYjViWGFiaHlzd2UyblkwUjQ1OHRnZC1qNGk5ZzlUQWVILUsxeWQ3NXVPQzBVNEJQNDZseGRNd3BucEYxaDN5bHZYb1BPTHU3bzBZS2IxUzZzdUx5b1Z4MlcwUVgybVhvc20ydlhpMzVlZXJ5Y3lCVlQteUs0TlIwZVQ3RXg4UEJqbmxEU1JwYWRWSDJDM0I4eGI?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxObTRWTjFVSXgyTTliSmFpWnpCVkVsalBDemZtQjBZc0J3eEFKcGZLXzFtZlhtaU52c0tmeTVuWnVoODhlbElya0NCSDRSZGFDUHVIS2R2cHdETG01RW1TZmFOWjdKS2wxSFpsU3Z2M2VscmctOV9FQXJMcWV2X0VOYldfMGd1X1NmTHFlTzNSSTh5M1hhQnQ0Sg?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPcnRVQjVzNlRVdG1lSXIzSHZMMHhIZ0NycFp6V1lVUjVBdjRyVFV4c1V1LVQ3SE5qRVlRV21XbU1IcUEtLWNPNHo3bHlPc2FUcTExTU9pS2FMMERuZ181TUI5Y3ZJcTltQndNWWZqdFhKQTFMbTNiQ19odDN2YlVnMXpBVVE0cU1tWF81WjFPM1Y3ZG10aXpB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
