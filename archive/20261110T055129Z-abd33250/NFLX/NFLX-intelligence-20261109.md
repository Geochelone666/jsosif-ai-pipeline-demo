# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T06:10:28.621082+00:00**
- AI status: **Partial: 3 headlines remain unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 6, 'ai': 13, 'unknown': 3, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 44.0%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 63.9500 |
| Return 1D (%) | 0.8516 |
| Return 1W (%) | 2.5826 |
| Return 1M (%) | -9.0327 |
| Return YTD (%) | -31.7939 |
| Return 1Y (%) | -42.0564 |
| Annualized volatility (%) | 36.3249 |
| Beta vs SPY | 0.2273 |
| Max drawdown (%) | -46.4449 |
| Sharpe (rf=0) | -1.3733 |
| Downside deviation (rf=0, %) | 26.6665 |
| Sortino (rf=0) | -1.8707 |
| Historical VaR 95% (1D, %) | 3.5205 |
| Historical ES 95% (1D, %) | 5.1308 |
| Correlation vs SPY | 0.0857 |
| Tracking error vs SPY (%) | 37.7058 |
| P/E (trailing) | 18.48 |
| P/B | 8.97 |
| EV/EBITDA | 17.04 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 16.96 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 34.63 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 9.70 |
| MA50 | 70.6770 |
| Close vs MA50 (%) | -9.5179 |
| MA200 | 80.9300 |
| Close vs MA200 (%) | -20.9811 |
| RSI (14, Wilder) | 41.5857 |
| MACD (12,26) | -1.9365 |
| MACD signal (9) | -2.1832 |
| MACD histogram | 0.2467 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 63.9500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.8516 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.5826 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -9.0327 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -31.7939 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -42.0564 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.3249 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.6665 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.8707 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.5205 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1308 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0857 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.7058 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2273 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -46.4449 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.3733 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.9568 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 34.6320 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.7014 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.4827 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.5857 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2467 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.5179 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -20.9811 -> Clearly below the moving-average trend level.

## TAILWINDS

### Netflix Inc (NFLX) Stock Up 4.7% and Still Undervalued -- GF Sco
- Summary: Netflix Inc (NFLX) Stock Up 4.7% and Still Undervalued -- GF Sco
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOQjB4ZnhxdjRJYnpHZkpOX3hJRV9Od1FQSFNIM2FrTjVOemI4T1ppODdhZF96WkNPc2wxcTB1M24yY1M3WmRScldnTTQ4UzJqUzN1Q0JUX1IwcGhZTUEyRjljcG1YcklMajV2bjd3cjlreV8zV1JvZUlZNmpFSjF1M0t2NXd4NDJ6VEhlU3FUYjNjR3FUMlYwUlJWckFSUlRzSjlpcXlySQ?oc=5>

### Investors Heavily Search Netflix, Inc. (NFLX): Here is What You Need to Know
- Summary: High investor search volume signals growing interest in Netflix.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxObDB2cXZhTTBKYndDM1lOMlFGM1BEbTFyR21MSVRWM2JrMWxJSUVWNWtQU1ZQLXN2a25sMW54TWxXX3p1eG91Q2ZPNlpSUHlqSzhWaVhnRk9faXdKUmNCaGppSHl4dHBvRnpYRXpIQnIxcE9oZDdFTVRhdFdoOVNQeV9ZQUxNZ2k5QjR6NHc1M29hbGNCNmhBZHJEcjVINzJ4VE9j?oc=5>

### Netflix (NFLX) Stock May Be 23% Below Fair Value As Ads Expansion Builds
- Summary: Potential undervaluation amid expanding ad strategy suggests upside.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxQNENZNGtFbTRBN1ZIM0hxVWlIdUZCcDF1NHhDXzdGN2dLbGNrM1Y1cFpqR18xcXl3cTkyRmsxbXE5VnhaNUF0NUxndHgtYmJuR3BTNWZCZXU2bVNFZklOTVBCZ1FiNWtSTXoxcDJ4akNlNlFDWXg5aGhtVTIxRVJtOFk3X3Z0b3A4SjI4TDNWNDV3QmhkY01TZ3RYekROcm51VzlVaHVIZzRXYURFTm42VmhHSkZvWkVNN1lTY1psakXSAcYBQVVfeXFMTk51VXN5Z3ZCeXZyUzlTVW0zRlJoV2U4ZV9UVml5NDFkeU5nRTkxaks3SHU4eGh3bFgxNlQwT3M5T3UyeTFaZDMwa25GYlg2M0RIWVFzZ0pmTkJhdzBWMXQzeUpuYUpEdUhGdnQ1Tkd5RWlBSURyN1N5VmdvQnJQbzlDeFRJdFJzRjl6Sk01Um44MlhpVnhGcUlGX0NkekhkeVVJVXY3UEFpQ0IxTHoxWXBDLTFnNHZVSjZLY1FJVkhsRkZSU213?oc=5>

### Netflix (NASDAQ:NFLX) Shares Climb 4.7% - Should You Buy?
- Summary: Shares rose 4.7%, indicating short‑term bullish sentiment.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQRzJJbWpkUXR3Q0RFRHRiekNDbWw5S2I4RGltb3N0dVFTUU1kMkxINlJMUFBuMlljamtxQ1NKVW1KNjdPZzljMktPZmRLOFpuLXRuS1pDRHJZTUx0QWU3UDRuZ2c3MTk0MldKb0ZES3lNS3J5bVF3N2NqODc5djM1ZjE5UUZBTDFYZkNSNUlPZXcyZHg5TjRzUk9RTzRtQnI4OXhINmlPNllWYmRjdnZz?oc=5>

## HEADWINDS

### Netflix (NASDAQ:NFLX) Stock Price Down 1.3% on Insider Selling
- Summary: Netflix (NASDAQ:NFLX) Stock Price Down 1.3% on Insider Selling
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQTWtraVFWUVZGUEsxSWoxRFZacFBxUXJzV2pwQklqU0t4NmI2bDhLQm1NMjB4VWJfWVZwYmNTODh1T1VFSHlWd05EOXVkMmg0X1NFT0VnXzVpUjAxRVlMYXY2MFN6WGRWMXhoWWs5S0hxMGRDa1AyajcyNWVWTTNHeldmNVg0dkhfRGZQcldPVXpYWVhRZm1faFlrb29XSU5kQm9WQi11NjdZY1pyUl9haG1iM191YnFITEE?oc=5>

### Netflix (NASDAQ:NFLX) Stock Price Down 3.3% on Insider Selling
- Summary: Netflix (NASDAQ:NFLX) Stock Price Down 3.3% on Insider Selling
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxORFdFYkJHQm1kMWtHTmJVRzRyUG9zUURnRTFXZjVzYlI1UndQS0lxQVR5WDBhTGM0YlF2YVJJQXhhUjVnOXhRWngtOGRIZzRJUWY4NEhvazgxZ1QzNjNmWVlUWUV3bTNZOXkwNWpQN0U0anlSSVNDOHFuZE5pUDVJZmlzaU1xWHNyeUFVSGtkWG5zd3pkd0JNTm1qTnlsSFBEUzRUTmFlekVZeFIxN3dXVk9DOTYzaEJTVVE?oc=5>

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

### Netflix Unveils ‘AI Discover’ To Take The Guesswork Out Of Streaming TV
- Summary: Netflix Unveils ‘AI Discover’ To Take The Guesswork Out Of Streaming TV
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPVmFCMjkxWERhcDluVjRRWGIyOTkzR3RSNXNHSGsxRGhZa1FoY1BDcEdkQXBOVER6WXIxcjJjYnBDOTBNemJOak9kNDBzV29CaDBLX2hPN19BUzJSQTJMU0taNzdzZE1QUUJQVkpGWHBPUE5QWm05NTl6eld4Zm5qaVVCVEs4Q2UxR0pSdUVZWDdGZGFwV2ZPc1djNWRNRVRfUnc0cEF6MXhaSHJjRnA2SzVSNUZXTlBsWlJsWkRBTEp4enZ3aW9Ed3NB?oc=5>

### Netflix, Inc. $NFLX Stock Sold by International Assets Investment Management LLC
- Summary: Netflix, Inc. $NFLX Stock Sold by International Assets Investment Management LLC
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxOVFc2eFFtOHhZaU5FZ2xCX2xYUTlLRzI1aUVOc2dLZ0JfUWZKN2ZuNHV5TUd1bC1OZUZ5OEFnUHdyeGNXR3J3Rzc0TVNZTmtrVVgyMFAzOVluNVkyZmJXdlNKc21JMUxPQkR1dzF4TjVzVXNrdHVFa1VIaDdqWDZGcjFpYXlUQnlKTnVFQkdzUjlBLWlQUTdWY0syTmJZMzB4eGFiS19EWThsTXRsekNDakYyN09TVXlyRWZ6d3FNb3lFd1czWm13dmZLSUItMzdrbHA4RA?oc=5>

### Netflix Is Playing a Bigger Game. Investors Should Take Notice
- Summary: Netflix outlines an expanded strategy for investors.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQT0JEa2c4OG9JemZzZDJHYjViWGFiaHlzd2UyblkwUjQ1OHRnZC1qNGk5ZzlUQWVILUsxeWQ3NXVPQzBVNEJQNDZseGRNd3BucEYxaDN5bHZYb1BPTHU3bzBZS2IxUzZzdUx5b1Z4MlcwUVgybVhvc20ydlhpMzVlZXJ5Y3lCVlQteUs0TlIwZVQ3RXg4UEJqbmxEU1JwYWRWSDJDM0I4eGI?oc=5>

### Insider trades: Netflix, Intel, Visa among notable names (V:NYSE)
- Summary: Insider trading activity involving Netflix shares noted among several companies.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPU1FaN0dLTS0xR2F6NmtmajJrblZBaHV2MGFEbURkU0x5Si1Jd2RadThjZWxIYjVwM0sxcHBsWGdtN2UwWHJvbGNvTkJzUkFLNkU5SXVESGNBWHZDUlZVSFR1QlF4R21yU3JUT25MUWNBLXBkSHVsdnBoTjVaMWpZVTBmV01JclZ6RWk4WlFIbFR1QlJNV1E?oc=5>

### Netflix Inc Stock (NFLX) Moved Up by 4.85% on Nov 4: What Investors Need To Know
- Summary: Shares rose 4.85% on Nov 4, indicating positive market reception.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNREFiOGpzM3NvWHVsQWF0SFEzTW9UQWx5Zzc4MjVjRmhsVDdnTG41SWIwWGpxZXNySkZ4ZGd6TTJwUC1DZWJkMHhjRUZwbXBLYS1jUm5Od2tTb3RtSGlSSmRVaDFhbG5jWWdWMDRsOEJfNlhyY1RXRENrM2tCZUx2bFI5bllCdEg2cGVN?oc=5>

### Netflix (NFLX) CFO sells 9,253 shares after 18,428 stock units vest.
- Summary: NFLX CFO sold 9,253 shares following vesting of 18,428 stock units.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNOHl0YUJfcS1vbWtyNTBCRUtnME5wZVRuRlcwVWpsNzc4Mkx1NU5fTEwwM0sxajdNaXBjelp4eS0zOUVXUTQ4Z01mbDNNUXJsRlRKSXpzYkxEX1hwMEQzRzhGLWFMTjJEd0dRUElXbkdYcUEwUTlQN2tRVzcyLVBZY1g5QVVXWVh5cmpHNml0TjVtSFZIUERTQmdUbzYwU1NUNnFQNldyalU?oc=5>

### Netflix, Inc. $NFLX Stock: CenterBook Partners LP Decreases Holdings
- Summary: CenterBook Partners LP reduced its holdings in Netflix stock.
- Date: 2026-11-08 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxOWFVMQVpvNnNRVVNUTzRfZmY5YkFhX05hWnFsQ3EwTHRWRlRpWUcwSGx4eWVoMkFwWXhnbHAzWURtS0xPb2dHZThNZm5WNTVNb3BOUDYtWkNFM2JDd2FiWU83eU9Vak9FanlFUk5QS1I2YWRVOFNWRHYyOE9SRnVUQjJ6NXFiUHY3cUk2WGhiSlV5a2dLR1JDY3Q4c2ZsMVNIX2ktZW9KR0tjTzlEbXROUW9TZXlFOTNXdTNmQnpiZVVySlE?oc=5>

### Netflix, Inc. $NFLX Stock: Heritage Investors Management Corp Boosts Holdings
- Summary: Heritage Investors Management Corp increased its Netflix holdings, indicating confidence in the company.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxPYXFnS1VqcmgtQnJRLUUtaVNPSmFpeXdUQjVLY1phUHJIOXJqLWNyLUZUQ0FiZlBNNlBkMnNQSW1FOXczUWNVOEt3ZVo1RTNtY3R3M3ZsN21MVmhBanktVU9JUjNrZGtIN3czbW5YcVVXeG1BQ1RVdlAwQWFNR2tnUG1WRTFUR2V6MWF1Sndub2hyMUZxWThySTdjeUFkN2dHbTlxUUYzdGZFOFNfNm1nZTZnQTRFekV0bDdVQmpLaUZPbHRYdlRLZ3ZrNTduRzg?oc=5>

### Netflix, Inc. $NFLX Stock Position Lifted by Gerber Kawasaki Wealth & Investment Management
- Summary: Gerber Kawasaki Wealth & Investment Management raised its Netflix position, signaling positive outlook.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxQQWpwcW9xTG42TncwVVdxd1ZrODZkcjhzMHNmUGh5a3g5VWdXbHNIak1FT1BycDBRZm5IcnZuS2NKeW9LQW1kR1lWSHlUT1Z0THlCSGVtRmcwbUtueDIxYS1ER0VVQVFDalFkamZoaUM5dG1EN0xVelV2clVHYU9BTVluV0dySGhrWXBLeWVlRW85X01ONWQ2X2ZYVDNDMi1pZzhPdV93bXhWT2R0QWVkSVd5bWtiU2tKSzdsak9BbzZ0SVdhOWRIbXllQUJwQnhXc3d5RWtiN0V0ZzVXbW5Ucw?oc=5>

## RISKS

### Netflix's Loyal Subscribers Are Not Priced Correctly (NASDAQ:NFLX)
- Summary: Netflix may face subscriber churn due to pricing misalignment, potentially impacting revenue.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPcnRVQjVzNlRVdG1lSXIzSHZMMHhIZ0NycFp6V1lVUjVBdjRyVFV4c1V1LVQ3SE5qRVlRV21XbU1IcUEtLWNPNHo3bHlPc2FUcTExTU9pS2FMMERuZ181TUI5Y3ZJcTltQndNWWZqdFhKQTFMbTNiQ19odDN2YlVnMXpBVVE0cU1tWF81WjFPM1Y3ZG10aXpB?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **18.48** | **8.97** | **17.04** | **11.80** | **262,599,557,120.00 USD** | **-42.06** |
| DIS | 24.56 | 1.87 | 12.09 | 6.80 | 205,682,950,144.00 USD | 9.12 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 7.76 | 0.94 | 4.98 | -6.10 | 87,035,166,720.00 USD | 0.74 |

Peers fetched as_of: 2026-11-09; NFLX reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

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
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxQNENZNGtFbTRBN1ZIM0hxVWlIdUZCcDF1NHhDXzdGN2dLbGNrM1Y1cFpqR18xcXl3cTkyRmsxbXE5VnhaNUF0NUxndHgtYmJuR3BTNWZCZXU2bVNFZklOTVBCZ1FiNWtSTXoxcDJ4akNlNlFDWXg5aGhtVTIxRVJtOFk3X3Z0b3A4SjI4TDNWNDV3QmhkY01TZ3RYekROcm51VzlVaHVIZzRXYURFTm42VmhHSkZvWkVNN1lTY1psakXSAcYBQVVfeXFMTk51VXN5Z3ZCeXZyUzlTVW0zRlJoV2U4ZV9UVml5NDFkeU5nRTkxaks3SHU4eGh3bFgxNlQwT3M5T3UyeTFaZDMwa25GYlg2M0RIWVFzZ0pmTkJhdzBWMXQzeUpuYUpEdUhGdnQ1Tkd5RWlBSURyN1N5VmdvQnJQbzlDeFRJdFJzRjl6Sk01Um44MlhpVnhGcUlGX0NkekhkeVVJVXY3UEFpQ0IxTHoxWXBDLTFnNHZVSjZLY1FJVkhsRkZSU213?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQRzJJbWpkUXR3Q0RFRHRiekNDbWw5S2I4RGltb3N0dVFTUU1kMkxINlJMUFBuMlljamtxQ1NKVW1KNjdPZzljMktPZmRLOFpuLXRuS1pDRHJZTUx0QWU3UDRuZ2c3MTk0MldKb0ZES3lNS3J5bVF3N2NqODc5djM1ZjE5UUZBTDFYZkNSNUlPZXcyZHg5TjRzUk9RTzRtQnI4OXhINmlPNllWYmRjdnZz?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQTWtraVFWUVZGUEsxSWoxRFZacFBxUXJzV2pwQklqU0t4NmI2bDhLQm1NMjB4VWJfWVZwYmNTODh1T1VFSHlWd05EOXVkMmg0X1NFT0VnXzVpUjAxRVlMYXY2MFN6WGRWMXhoWWs5S0hxMGRDa1AyajcyNWVWTTNHeldmNVg0dkhfRGZQcldPVXpYWVhRZm1faFlrb29XSU5kQm9WQi11NjdZY1pyUl9haG1iM191YnFITEE?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxORFdFYkJHQm1kMWtHTmJVRzRyUG9zUURnRTFXZjVzYlI1UndQS0lxQVR5WDBhTGM0YlF2YVJJQXhhUjVnOXhRWngtOGRIZzRJUWY4NEhvazgxZ1QzNjNmWVlUWUV3bTNZOXkwNWpQN0U0anlSSVNDOHFuZE5pUDVJZmlzaU1xWHNyeUFVSGtkWG5zd3pkd0JNTm1qTnlsSFBEUzRUTmFlekVZeFIxN3dXVk9DOTYzaEJTVVE?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNZ1FibVQ3b2RIcTlGWk9ITmo2cTVrMEF5WkhvMlBVYjlrcFMtcElfTkI5VEVVZXUzYWpfZUtxcVFNMC1IZzJQcVo3enVSZzVXOE9nLWxzSVdvYldZbmxJQkUtbWFCNG5mVmJSWU14Wldqd18wMjBvV3YxNzFEaTA2blJrWkdKU0U5OHhB?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxObWp6WS1RSURnTG43Sy02dXI5TXpWeFpKdmdIVzFsbGItNG54M1pwUWVqZDBjSDdkV3lFZGwzSDJtUVJQcURrWlgwb2lQWDVNcTJnbEFQdjJ6ZzdMQlIxS3JjRW12bjZFQXlESU9xN1R4bGYtN1N5WlhTZ3J2eHYyQVFrbEVrWkFVcHFjc1BvTUdBc000dy12Q05DX1VSS09oSkd5QWFzNzRlZU5feU5sUzFqb3E2T09ZSWRkNVVBSVFaUnRJaHRv?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxPMGF6OTJWMWtVa3V2TU9MWFB6a0JYWHFUdUI1MUlCTGxqQm9ESUNUNnlndHB2cXQyWnBnZ2NYSHoySG43aWlkNm9GVXR0LWJRWTIwNmtabGo1T2cyQTB0YTBfU1EtMEtQU0otczhjR1o1QUVDd0hwcV9kX1BTaDZjUXhYSm44dw?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPVmFCMjkxWERhcDluVjRRWGIyOTkzR3RSNXNHSGsxRGhZa1FoY1BDcEdkQXBOVER6WXIxcjJjYnBDOTBNemJOak9kNDBzV29CaDBLX2hPN19BUzJSQTJMU0taNzdzZE1QUUJQVkpGWHBPUE5QWm05NTl6eld4Zm5qaVVCVEs4Q2UxR0pSdUVZWDdGZGFwV2ZPc1djNWRNRVRfUnc0cEF6MXhaSHJjRnA2SzVSNUZXTlBsWlJsWkRBTEp4enZ3aW9Ed3NB?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxOVFc2eFFtOHhZaU5FZ2xCX2xYUTlLRzI1aUVOc2dLZ0JfUWZKN2ZuNHV5TUd1bC1OZUZ5OEFnUHdyeGNXR3J3Rzc0TVNZTmtrVVgyMFAzOVluNVkyZmJXdlNKc21JMUxPQkR1dzF4TjVzVXNrdHVFa1VIaDdqWDZGcjFpYXlUQnlKTnVFQkdzUjlBLWlQUTdWY0syTmJZMzB4eGFiS19EWThsTXRsekNDakYyN09TVXlyRWZ6d3FNb3lFd1czWm13dmZLSUItMzdrbHA4RA?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQT0JEa2c4OG9JemZzZDJHYjViWGFiaHlzd2UyblkwUjQ1OHRnZC1qNGk5ZzlUQWVILUsxeWQ3NXVPQzBVNEJQNDZseGRNd3BucEYxaDN5bHZYb1BPTHU3bzBZS2IxUzZzdUx5b1Z4MlcwUVgybVhvc20ydlhpMzVlZXJ5Y3lCVlQteUs0TlIwZVQ3RXg4UEJqbmxEU1JwYWRWSDJDM0I4eGI?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPU1FaN0dLTS0xR2F6NmtmajJrblZBaHV2MGFEbURkU0x5Si1Jd2RadThjZWxIYjVwM0sxcHBsWGdtN2UwWHJvbGNvTkJzUkFLNkU5SXVESGNBWHZDUlZVSFR1QlF4R21yU3JUT25MUWNBLXBkSHVsdnBoTjVaMWpZVTBmV01JclZ6RWk4WlFIbFR1QlJNV1E?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNREFiOGpzM3NvWHVsQWF0SFEzTW9UQWx5Zzc4MjVjRmhsVDdnTG41SWIwWGpxZXNySkZ4ZGd6TTJwUC1DZWJkMHhjRUZwbXBLYS1jUm5Od2tTb3RtSGlSSmRVaDFhbG5jWWdWMDRsOEJfNlhyY1RXRENrM2tCZUx2bFI5bllCdEg2cGVN?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNOHl0YUJfcS1vbWtyNTBCRUtnME5wZVRuRlcwVWpsNzc4Mkx1NU5fTEwwM0sxajdNaXBjelp4eS0zOUVXUTQ4Z01mbDNNUXJsRlRKSXpzYkxEX1hwMEQzRzhGLWFMTjJEd0dRUElXbkdYcUEwUTlQN2tRVzcyLVBZY1g5QVVXWVh5cmpHNml0TjVtSFZIUERTQmdUbzYwU1NUNnFQNldyalU?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxOWFVMQVpvNnNRVVNUTzRfZmY5YkFhX05hWnFsQ3EwTHRWRlRpWUcwSGx4eWVoMkFwWXhnbHAzWURtS0xPb2dHZThNZm5WNTVNb3BOUDYtWkNFM2JDd2FiWU83eU9Vak9FanlFUk5QS1I2YWRVOFNWRHYyOE9SRnVUQjJ6NXFiUHY3cUk2WGhiSlV5a2dLR1JDY3Q4c2ZsMVNIX2ktZW9KR0tjTzlEbXROUW9TZXlFOTNXdTNmQnpiZVVySlE?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxPYXFnS1VqcmgtQnJRLUUtaVNPSmFpeXdUQjVLY1phUHJIOXJqLWNyLUZUQ0FiZlBNNlBkMnNQSW1FOXczUWNVOEt3ZVo1RTNtY3R3M3ZsN21MVmhBanktVU9JUjNrZGtIN3czbW5YcVVXeG1BQ1RVdlAwQWFNR2tnUG1WRTFUR2V6MWF1Sndub2hyMUZxWThySTdjeUFkN2dHbTlxUUYzdGZFOFNfNm1nZTZnQTRFekV0bDdVQmpLaUZPbHRYdlRLZ3ZrNTduRzg?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxQQWpwcW9xTG42TncwVVdxd1ZrODZkcjhzMHNmUGh5a3g5VWdXbHNIak1FT1BycDBRZm5IcnZuS2NKeW9LQW1kR1lWSHlUT1Z0THlCSGVtRmcwbUtueDIxYS1ER0VVQVFDalFkamZoaUM5dG1EN0xVelV2clVHYU9BTVluV0dySGhrWXBLeWVlRW85X01ONWQ2X2ZYVDNDMi1pZzhPdV93bXhWT2R0QWVkSVd5bWtiU2tKSzdsak9BbzZ0SVdhOWRIbXllQUJwQnhXc3d5RWtiN0V0ZzVXbW5Ucw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPcnRVQjVzNlRVdG1lSXIzSHZMMHhIZ0NycFp6V1lVUjVBdjRyVFV4c1V1LVQ3SE5qRVlRV21XbU1IcUEtLWNPNHo3bHlPc2FUcTExTU9pS2FMMERuZ181TUI5Y3ZJcTltQndNWWZqdFhKQTFMbTNiQ19odDN2YlVnMXpBVVE0cU1tWF81WjFPM1Y3ZG10aXpB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
