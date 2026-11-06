# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:04:31.596255+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 7, 'ai': 11, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'directional_claim_without_event_type': 2, 'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 13 named publishers; 0 exact duplicates; 24 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-30

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 65.5600 |
| Return 1D (%) | -1.2502 |
| Return 1W (%) | 5.6567 |
| Return 1M (%) | -2.8741 |
| Return YTD (%) | -30.0768 |
| Return 1Y (%) | -40.3164 |
| Annualized volatility (%) | 36.1521 |
| Beta vs SPY | 0.2348 |
| Max drawdown (%) | -46.4449 |
| Sharpe (rf=0) | -1.2525 |
| Downside deviation (rf=0, %) | 26.4100 |
| Sortino (rf=0) | -1.7145 |
| Historical VaR 95% (1D, %) | 3.5133 |
| Historical ES 95% (1D, %) | 5.1308 |
| Correlation vs SPY | 0.0883 |
| Tracking error vs SPY (%) | 37.4830 |
| P/E (trailing) | 18.95 |
| P/B | 9.19 |
| EV/EBITDA | 17.45 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 17.38 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 34.63 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 9.33 |
| MA50 | 71.3610 |
| Close vs MA50 (%) | -8.1291 |
| MA200 | 81.1415 |
| Close vs MA200 (%) | -19.2029 |
| RSI (14, Wilder) | 45.1198 |
| MACD (12,26) | -2.0656 |
| MACD signal (9) | -2.2986 |
| MACD histogram | 0.2330 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 65.5600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.2502 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.6567 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -2.8741 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -30.0768 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -40.3164 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.1521 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.4100 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.7145 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.5133 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1308 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0883 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.4830 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2348 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -46.4449 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.2525 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.3837 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 34.6320 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.3322 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.9480 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 45.1198 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2330 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -8.1291 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -19.2029 -> Clearly below the moving-average trend level.

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

## HEADWINDS

### Netflix (NASDAQ:NFLX) Stock Price Down 1.3% on Insider Selling
- Summary: Netflix (NASDAQ:NFLX) Stock Price Down 1.3% on Insider Selling
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQTWtraVFWUVZGUEsxSWoxRFZacFBxUXJzV2pwQklqU0t4NmI2bDhLQm1NMjB4VWJfWVZwYmNTODh1T1VFSHlWd05EOXVkMmg0X1NFT0VnXzVpUjAxRVlMYXY2MFN6WGRWMXhoWWs5S0hxMGRDa1AyajcyNWVWTTNHeldmNVg0dkhfRGZQcldPVXpYWVhRZm1faFlrb29XSU5kQm9WQi11NjdZY1pyUl9haG1iM191YnFITEE?oc=5>

### How Investors May Respond To Netflix (NFLX) Lower Ad Revenue Guidance
- Summary: Lower ad revenue guidance may hurt investor sentiment.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNTmpuUm0tQldPM0g2UUNrdFpYUHVvZ05XM3JUVTVzYTVQV3JwSFJWRFM5aU14dlRGbDFHWUhaNDNsWXc4ZEl2RVVtcXRLN29wMU1xRXJGQWVQemU1MkZYMmRDVXFkMjgwR0txQkpza0phNXZFbWlCbzJNZ0VNek1sRmFiczNjVEF2UEFhcTV1ZW1sRDNwWHBBdG5qTE9Fc2Z5?oc=5>

## CATALYSTS

### Netflix's U.S. Audience Engagement Problem Is Hurting The Stock (Rating Downgrade)
- Summary: Netflix's U.S. Audience Engagement Problem Is Hurting The Stock (Rating Downgrade)
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOY3JYbDhETktQMDhGRklxQl8wM3d0YkFPdGpia3dkaFlXdUxlczVzVlFBTlVVTkRUSWw4MF9PbHZyazd5bE9EejVzR2ZBVmowNTZ2dWZuMDZ5aGhZQ3IxS3VkMmg0TFBDSFAyQ0R3OGxIMklaLV9xUEdLZGY4Q0VxTWFsal80OUZuQjRXSUZ0QUNxR2x1aTgwcVhGUnlKY1RoblJkZGZuNjlIVHZtWkpsd3ZzYWFiSUZ1RlE?oc=5>

### Netflix Unveils ‘AI Discover’ To Take The Guesswork Out Of Streaming TV
- Summary: Netflix Unveils ‘AI Discover’ To Take The Guesswork Out Of Streaming TV
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPVmFCMjkxWERhcDluVjRRWGIyOTkzR3RSNXNHSGsxRGhZa1FoY1BDcEdkQXBOVER6WXIxcjJjYnBDOTBNemJOak9kNDBzV29CaDBLX2hPN19BUzJSQTJMU0taNzdzZE1QUUJQVkpGWHBPUE5QWm05NTl6eld4Zm5qaVVCVEs4Q2UxR0pSdUVZWDdGZGFwV2ZPc1djNWRNRVRfUnc0cEF6MXhaSHJjRnA2SzVSNUZXTlBsWlJsWkRBTEp4enZ3aW9Ed3NB?oc=5>

### Netflix, Inc. $NFLX Stock Sold by International Assets Investment Management LLC
- Summary: Netflix, Inc. $NFLX Stock Sold by International Assets Investment Management LLC
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxOVFc2eFFtOHhZaU5FZ2xCX2xYUTlLRzI1aUVOc2dLZ0JfUWZKN2ZuNHV5TUd1bC1OZUZ5OEFnUHdyeGNXR3J3Rzc0TVNZTmtrVVgyMFAzOVluNVkyZmJXdlNKc21JMUxPQkR1dzF4TjVzVXNrdHVFa1VIaDdqWDZGcjFpYXlUQnlKTnVFQkdzUjlBLWlQUTdWY0syTmJZMzB4eGFiS19EWThsTXRsekNDakYyN09TVXlyRWZ6d3FNb3lFd1czWm13dmZLSUItMzdrbHA4RA?oc=5>

### Netflix, Inc. $NFLX Stock Acquired by Provenance Wealth Advisors LLC
- Summary: Netflix, Inc. $NFLX Stock Acquired by Provenance Wealth Advisors LLC
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPTHJ2Z29EV3htXzNqRjFCTUM0THRBeDlPSmtqUzRtMUFURFJCTU04RzU2ODVIcHNLbXFHWTdYVkNUaDJUVzlVaHhWM3NCMXFmbmhMaTZqZVgzcXJFel9ubmtfSHVfdVY3VHB5ejkteVItNGoxSXhSYldZZ0RHRnNSdUdSTlRtUlBvd2lQZk8xZE1xVHJlRkw4NjRtR2E3eUtJdUZtRDR5T2JVTXJnYlR3UW9jc2F5SHZVaXBYcnNfMkExNmJt?oc=5>

### Netflix, Inc. $NFLX Stock: D.A. Davidson & CO. Raises Position
- Summary: Netflix, Inc. $NFLX Stock: D.A. Davidson & CO. Raises Position
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNUTN2QnF4dlZWVnJyVkJlanNZLVFfN1JpWWZoWF9EM1dvSXA3STY5OVhCdGtiaVA5bmpSYXVFN3UxaENtbjdlYzZMYmRGeUNPTGJuVWxuSEFlQ0c0VW9JWExVbW1pbndEdi12YUZFak5jWlBRRkhuYjVUMDNGYTI0M0lMeDcxWTlObUUtZ0VHTDM1TkZsNTZkMnZadEU2M2lNOWdvaE9taUpTVnZCYkFmWHh2WTY?oc=5>

### Netflix Inc Stock (NFLX) Moved Up by 4.85% on Nov 4: What Investors Need To Know
- Summary: Shares rose 4.85% on Nov 4, indicating positive market reception.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNREFiOGpzM3NvWHVsQWF0SFEzTW9UQWx5Zzc4MjVjRmhsVDdnTG41SWIwWGpxZXNySkZ4ZGd6TTJwUC1DZWJkMHhjRUZwbXBLYS1jUm5Od2tTb3RtSGlSSmRVaDFhbG5jWWdWMDRsOEJfNlhyY1RXRENrM2tCZUx2bFI5bllCdEg2cGVN?oc=5>

### Netflix, Inc. $NFLX Stock: MGO One Seven LLC Decreases Holdings
- Summary: MGO One Seven LLC reduced its Netflix holdings, indicating a potential shift in investor confidence.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPcVlBT24zN19VWDFOejJxSWQyemhmc2lvUVlfRVVkQlFURDlPTHFJajViVmlCcjFpQW9EeXBCeHZYLUFZT3hxbGZ0M1FDS255QzRab0NZcC05dzBKWjRQNUZsV0ltV0sxMUdDWFNSTERMNlRuVHVDc01NLVppV0ZBNW1lbDBKZkZmSzdQWTh1ZG55dzhpZnliNEFYQjZnRk9JSUhLRU5ZeXk2RVFqNlZaemJKUDlxV2xiaHJoRQ?oc=5>

### Netflix, Inc. $NFLX Stock: Heritage Investors Management Corp Boosts Holdings
- Summary: Heritage Investors Management Corp increased its Netflix stake, suggesting bullish outlook.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxPYXFnS1VqcmgtQnJRLUUtaVNPSmFpeXdUQjVLY1phUHJIOXJqLWNyLUZUQ0FiZlBNNlBkMnNQSW1FOXczUWNVOEt3ZVo1RTNtY3R3M3ZsN21MVmhBanktVU9JUjNrZGtIN3czbW5YcVVXeG1BQ1RVdlAwQWFNR2tnUG1WRTFUR2V6MWF1Sndub2hyMUZxWThySTdjeUFkN2dHbTlxUUYzdGZFOFNfNm1nZTZnQTRFekV0bDdVQmpLaUZPbHRYdlRLZ3ZrNTduRzg?oc=5>

### Netflix, Inc. $NFLX Stock Position Lifted by Gerber Kawasaki Wealth & Investment Management
- Summary: Gerber Kawasaki Wealth & Investment Management raised its Netflix position, reflecting positive sentiment.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxQQWpwcW9xTG42TncwVVdxd1ZrODZkcjhzMHNmUGh5a3g5VWdXbHNIak1FT1BycDBRZm5IcnZuS2NKeW9LQW1kR1lWSHlUT1Z0THlCSGVtRmcwbUtueDIxYS1ER0VVQVFDalFkamZoaUM5dG1EN0xVelV2clVHYU9BTVluV0dySGhrWXBLeWVlRW85X01ONWQ2X2ZYVDNDMi1pZzhPdV93bXhWT2R0QWVkSVd5bWtiU2tKSzdsak9BbzZ0SVdhOWRIbXllQUJwQnhXc3d5RWtiN0V0ZzVXbW5Ucw?oc=5>

### Netflix, Inc. $NFLX Stock Position Lifted by ProShare Advisors LLC
- Summary: ProShare Advisors LLC increased its Netflix holdings, indicating confidence in the company.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOajJ3YmpQMnlyZ01vZmRmMkZnMWFyZkNIQS02VERhQlMxUnlDaG9XQnlQdnNrMGJLV2lpeUlPTkdtaGxDbkd6anUybUlzdjhvT3dhVnN5enFQTTZGTmJ6ZVU0VUdvTHU3TWRRc3FJUGRkdUd0TTN4SUNCRnB0Q2J3Zzg3Vm9WOGxNakdzZkxpbDVVVmxsUjBwRTlQMXpUX3oxc1daaExsS0JkN1JBUHlvNEstRTVGUEkxZGhoWjg1eVBkdw?oc=5>

### Netflix (NFLX) Dismisses Film Chief Dan Lin
- Summary: Netflix fired film chief Dan Lin, a significant personnel change impacting leadership.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNcGJPRnBWTkdYOUZhTU9rQldlMjNNUzlFeHJvSFZZVmZqZmo0dDFLR1hZQVhUcFNyWUlxcUNoZ0pyQzhLcmtUNGVkQTZyNGdBMUduQ3dtRjNvN0tnVkdCUk5Fd0pvZW9RZ1NJTkpvdE5SRFUwc0JRVVhDc2dCdVlLcUJUWGpSSWdTN1NNR2VkUWU3UmZzYmkyeml3Y1hzcGozUm53QnZtZ9IBrAFBVV95cUxNLWlRUVBPcS1RTDFDMTlIUUlFMkYxLUljSmFkNkJuRDhjeks5anRnOERzbVFfTDVFYlVQbUNfYm1ZRk84a3gzMzJydVVRT1ZfX0N6cDhXYzJpUzFZRmE4cGhJV3Z1a3BodWphWXNUeDdhMDlaMzdHTzl5NldmV3dsYXkyY0pXeklwdW4xYl9DMTFvNEtuXzQ1SGJWRnBSaWM0RmUyRVpWMF9PUGlI?oc=5>

### Netflix (NFLX) Tests AI-Powered Content Discovery in Race to Keep Viewers Engaged
- Summary: Netflix is experimenting with AI-driven content discovery to boost viewer engagement and retention.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQeDBhWG5IVTNTbWZhdGZOMGV2OUMxOWhiQk80M2lCeUlOcVk4aTNJVll6azhmcTBvTGtveEl4NlFjRGtFM2dieW04Yjh4ZzJPMlUtZWM4aVlkbVJDdU9jWHRjdVI1Q3hza1dTbVJYS3E1TnA3SGx6ckljbWxTTnY4Qjg0SThMWHN6dHZhZ0xDRklnT0xUNGZxbEc2d2ZJMDJuQjcw?oc=5>

## RISKS

### Netflix (NFLX) legal chief sells 5,727 shares at $64.55 after stock awards vest.
- Summary: Legal chief sold shares, potentially signaling insider concerns.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNUGduLTYzT1RDRHR5WFROb1JiZ2swX0tOaDNKeTRUd1o1VndVeEt4dWg5cm52S0hFRFRvbEJ5UzN2S3ZEMVN6dGZpTWFPMWZ5cWpjNmpidjRjWGRSNXpta3lKMThQT1BPZl93MEFjYXVKQTZuSmdkYU9KQUs2M1lzdTBwSGdDclljWVhmdUU0WXU3a2o3bnB1Rk5sbHdHVi16dERPMWstUHI?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **18.95** | **9.19** | **17.45** | **11.80** | **272,987,865,088.00 USD** | **-40.32** |
| DIS | 24.52 | 1.84 | 11.93 | 6.80 | 202,402,234,368.00 USD | 6.79 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 7.90 | 0.96 | 5.02 | -6.10 | 88,597,610,496.00 USD | 0.38 |

Peers fetched as_of: 2026-11-05; NFLX reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

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
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQTWtraVFWUVZGUEsxSWoxRFZacFBxUXJzV2pwQklqU0t4NmI2bDhLQm1NMjB4VWJfWVZwYmNTODh1T1VFSHlWd05EOXVkMmg0X1NFT0VnXzVpUjAxRVlMYXY2MFN6WGRWMXhoWWs5S0hxMGRDa1AyajcyNWVWTTNHeldmNVg0dkhfRGZQcldPVXpYWVhRZm1faFlrb29XSU5kQm9WQi11NjdZY1pyUl9haG1iM191YnFITEE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNTmpuUm0tQldPM0g2UUNrdFpYUHVvZ05XM3JUVTVzYTVQV3JwSFJWRFM5aU14dlRGbDFHWUhaNDNsWXc4ZEl2RVVtcXRLN29wMU1xRXJGQWVQemU1MkZYMmRDVXFkMjgwR0txQkpza0phNXZFbWlCbzJNZ0VNek1sRmFiczNjVEF2UEFhcTV1ZW1sRDNwWHBBdG5qTE9Fc2Z5?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOY3JYbDhETktQMDhGRklxQl8wM3d0YkFPdGpia3dkaFlXdUxlczVzVlFBTlVVTkRUSWw4MF9PbHZyazd5bE9EejVzR2ZBVmowNTZ2dWZuMDZ5aGhZQ3IxS3VkMmg0TFBDSFAyQ0R3OGxIMklaLV9xUEdLZGY4Q0VxTWFsal80OUZuQjRXSUZ0QUNxR2x1aTgwcVhGUnlKY1RoblJkZGZuNjlIVHZtWkpsd3ZzYWFiSUZ1RlE?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPVmFCMjkxWERhcDluVjRRWGIyOTkzR3RSNXNHSGsxRGhZa1FoY1BDcEdkQXBOVER6WXIxcjJjYnBDOTBNemJOak9kNDBzV29CaDBLX2hPN19BUzJSQTJMU0taNzdzZE1QUUJQVkpGWHBPUE5QWm05NTl6eld4Zm5qaVVCVEs4Q2UxR0pSdUVZWDdGZGFwV2ZPc1djNWRNRVRfUnc0cEF6MXhaSHJjRnA2SzVSNUZXTlBsWlJsWkRBTEp4enZ3aW9Ed3NB?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxOVFc2eFFtOHhZaU5FZ2xCX2xYUTlLRzI1aUVOc2dLZ0JfUWZKN2ZuNHV5TUd1bC1OZUZ5OEFnUHdyeGNXR3J3Rzc0TVNZTmtrVVgyMFAzOVluNVkyZmJXdlNKc21JMUxPQkR1dzF4TjVzVXNrdHVFa1VIaDdqWDZGcjFpYXlUQnlKTnVFQkdzUjlBLWlQUTdWY0syTmJZMzB4eGFiS19EWThsTXRsekNDakYyN09TVXlyRWZ6d3FNb3lFd1czWm13dmZLSUItMzdrbHA4RA?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPTHJ2Z29EV3htXzNqRjFCTUM0THRBeDlPSmtqUzRtMUFURFJCTU04RzU2ODVIcHNLbXFHWTdYVkNUaDJUVzlVaHhWM3NCMXFmbmhMaTZqZVgzcXJFel9ubmtfSHVfdVY3VHB5ejkteVItNGoxSXhSYldZZ0RHRnNSdUdSTlRtUlBvd2lQZk8xZE1xVHJlRkw4NjRtR2E3eUtJdUZtRDR5T2JVTXJnYlR3UW9jc2F5SHZVaXBYcnNfMkExNmJt?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNUTN2QnF4dlZWVnJyVkJlanNZLVFfN1JpWWZoWF9EM1dvSXA3STY5OVhCdGtiaVA5bmpSYXVFN3UxaENtbjdlYzZMYmRGeUNPTGJuVWxuSEFlQ0c0VW9JWExVbW1pbndEdi12YUZFak5jWlBRRkhuYjVUMDNGYTI0M0lMeDcxWTlObUUtZ0VHTDM1TkZsNTZkMnZadEU2M2lNOWdvaE9taUpTVnZCYkFmWHh2WTY?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNREFiOGpzM3NvWHVsQWF0SFEzTW9UQWx5Zzc4MjVjRmhsVDdnTG41SWIwWGpxZXNySkZ4ZGd6TTJwUC1DZWJkMHhjRUZwbXBLYS1jUm5Od2tTb3RtSGlSSmRVaDFhbG5jWWdWMDRsOEJfNlhyY1RXRENrM2tCZUx2bFI5bllCdEg2cGVN?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPcVlBT24zN19VWDFOejJxSWQyemhmc2lvUVlfRVVkQlFURDlPTHFJajViVmlCcjFpQW9EeXBCeHZYLUFZT3hxbGZ0M1FDS255QzRab0NZcC05dzBKWjRQNUZsV0ltV0sxMUdDWFNSTERMNlRuVHVDc01NLVppV0ZBNW1lbDBKZkZmSzdQWTh1ZG55dzhpZnliNEFYQjZnRk9JSUhLRU5ZeXk2RVFqNlZaemJKUDlxV2xiaHJoRQ?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxPYXFnS1VqcmgtQnJRLUUtaVNPSmFpeXdUQjVLY1phUHJIOXJqLWNyLUZUQ0FiZlBNNlBkMnNQSW1FOXczUWNVOEt3ZVo1RTNtY3R3M3ZsN21MVmhBanktVU9JUjNrZGtIN3czbW5YcVVXeG1BQ1RVdlAwQWFNR2tnUG1WRTFUR2V6MWF1Sndub2hyMUZxWThySTdjeUFkN2dHbTlxUUYzdGZFOFNfNm1nZTZnQTRFekV0bDdVQmpLaUZPbHRYdlRLZ3ZrNTduRzg?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxQQWpwcW9xTG42TncwVVdxd1ZrODZkcjhzMHNmUGh5a3g5VWdXbHNIak1FT1BycDBRZm5IcnZuS2NKeW9LQW1kR1lWSHlUT1Z0THlCSGVtRmcwbUtueDIxYS1ER0VVQVFDalFkamZoaUM5dG1EN0xVelV2clVHYU9BTVluV0dySGhrWXBLeWVlRW85X01ONWQ2X2ZYVDNDMi1pZzhPdV93bXhWT2R0QWVkSVd5bWtiU2tKSzdsak9BbzZ0SVdhOWRIbXllQUJwQnhXc3d5RWtiN0V0ZzVXbW5Ucw?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOajJ3YmpQMnlyZ01vZmRmMkZnMWFyZkNIQS02VERhQlMxUnlDaG9XQnlQdnNrMGJLV2lpeUlPTkdtaGxDbkd6anUybUlzdjhvT3dhVnN5enFQTTZGTmJ6ZVU0VUdvTHU3TWRRc3FJUGRkdUd0TTN4SUNCRnB0Q2J3Zzg3Vm9WOGxNakdzZkxpbDVVVmxsUjBwRTlQMXpUX3oxc1daaExsS0JkN1JBUHlvNEstRTVGUEkxZGhoWjg1eVBkdw?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNcGJPRnBWTkdYOUZhTU9rQldlMjNNUzlFeHJvSFZZVmZqZmo0dDFLR1hZQVhUcFNyWUlxcUNoZ0pyQzhLcmtUNGVkQTZyNGdBMUduQ3dtRjNvN0tnVkdCUk5Fd0pvZW9RZ1NJTkpvdE5SRFUwc0JRVVhDc2dCdVlLcUJUWGpSSWdTN1NNR2VkUWU3UmZzYmkyeml3Y1hzcGozUm53QnZtZ9IBrAFBVV95cUxNLWlRUVBPcS1RTDFDMTlIUUlFMkYxLUljSmFkNkJuRDhjeks5anRnOERzbVFfTDVFYlVQbUNfYm1ZRk84a3gzMzJydVVRT1ZfX0N6cDhXYzJpUzFZRmE4cGhJV3Z1a3BodWphWXNUeDdhMDlaMzdHTzl5NldmV3dsYXkyY0pXeklwdW4xYl9DMTFvNEtuXzQ1SGJWRnBSaWM0RmUyRVpWMF9PUGlI?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQeDBhWG5IVTNTbWZhdGZOMGV2OUMxOWhiQk80M2lCeUlOcVk4aTNJVll6azhmcTBvTGtveEl4NlFjRGtFM2dieW04Yjh4ZzJPMlUtZWM4aVlkbVJDdU9jWHRjdVI1Q3hza1dTbVJYS3E1TnA3SGx6ckljbWxTTnY4Qjg0SThMWHN6dHZhZ0xDRklnT0xUNGZxbEc2d2ZJMDJuQjcw?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNUGduLTYzT1RDRHR5WFROb1JiZ2swX0tOaDNKeTRUd1o1VndVeEt4dWg5cm52S0hFRFRvbEJ5UzN2S3ZEMVN6dGZpTWFPMWZ5cWpjNmpidjRjWGRSNXpta3lKMThQT1BPZl93MEFjYXVKQTZuSmdkYU9KQUs2M1lzdTBwSGdDclljWVhmdUU0WXU3a2o3bnB1Rk5sbHdHVi16dERPMWstUHI?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
