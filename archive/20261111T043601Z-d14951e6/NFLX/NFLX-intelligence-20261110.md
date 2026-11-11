# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:36:09.681564+00:00**
- AI status: **Partial: 1 headline remains unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 4, 'ai': 13, 'unknown': 1, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 12 named publishers; 0 exact duplicates; 23 HTTPS source links; largest publisher share 30.43%; oldest publication 2026-11-03

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 63.2600 |
| Return 1D (%) | -1.0790 |
| Return 1W (%) | -0.2523 |
| Return 1M (%) | -10.0142 |
| Return YTD (%) | -32.5299 |
| Return 1Y (%) | -43.5214 |
| Annualized volatility (%) | 36.2629 |
| Beta vs SPY | 0.2291 |
| Max drawdown (%) | -46.4449 |
| Sharpe (rf=0) | -1.4001 |
| Downside deviation (rf=0, %) | 26.6352 |
| Sortino (rf=0) | -1.9061 |
| Historical VaR 95% (1D, %) | 3.5133 |
| Historical ES 95% (1D, %) | 5.1308 |
| Correlation vs SPY | 0.0864 |
| Tracking error vs SPY (%) | 37.6332 |
| P/E (trailing) | 18.44 |
| P/B | 8.87 |
| EV/EBITDA | 16.86 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 16.77 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 34.63 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 9.81 |
| MA50 | 70.3212 |
| Close vs MA50 (%) | -10.0414 |
| MA200 | 80.8178 |
| Close vs MA200 (%) | -21.7252 |
| RSI (14, Wilder) | 39.8541 |
| MACD (12,26) | -1.8960 |
| MACD signal (9) | -2.1258 |
| MACD histogram | 0.2298 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 63.2600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.0790 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.2523 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -10.0142 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -32.5299 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -43.5214 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.2629 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.6352 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.9061 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.5133 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1308 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0864 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.6332 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2291 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -46.4449 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.4001 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.7739 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 34.6320 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.8072 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.4431 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 39.8541 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2298 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -10.0414 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -21.7252 -> Clearly below the moving-average trend level.

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

### Netflix (NFLX) director Strive Masiyiwa receives options with a $62.34 exercise price.
- Summary: Director granted options, potentially boosting morale and aligning incentives.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQR1JJT2J3ajhuUFdIQ1ktWGFuN3JBb1laWnRGUERRNmdha3pwMzE0T0xkUHNIR2xaZGtLYVNNTHVybkZmZWZPeUpXNTA2MjZxWXFBRWZDWVBYb1p1VGdaUS0zdG9KRFFIWGFaaE5XaDlPRjVyRS1pUTN6dE1PYVh4dG9VeUZpVzExQTRtOFBHQml5dGItaGVVdUdDSXR0YXRfS2JRLXpDQ2w?oc=5>

## HEADWINDS

### Netflix Stock (NASDAQ:NFLX) Slips Despite New Stranger Things Plans
- Summary: Netflix Stock (NASDAQ:NFLX) Slips Despite New Stranger Things Plans
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPd1NLeHE4Skdqd3NHRk8wSEtWSlpVazJfcEZVV0FjT0gzdElUQjEwWUs0LXdqeE9PZTAzcGNiZTJLMHNNS0h6TGVSOExwb3puOU9ybUliWHNsb2pYbnhVWjNQSXo4bjYtWFlWWHRLdWRjbFZ1ekc5c1lWWE95YXB2d1NrMXVjdDliUFJGVktOQUlBM1NBZTRlREhR?oc=5>

### Netflix Inc Stock (NFLX) Closed Down by 3.28% on Nov 6: A Full Analysis
- Summary: Recent share price drop indicates short‑term weakness.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNZ1FibVQ3b2RIcTlGWk9ITmo2cTVrMEF5WkhvMlBVYjlrcFMtcElfTkI5VEVVZXUzYWpfZUtxcVFNMC1IZzJQcVo3enVSZzVXOE9nLWxzSVdvYldZbmxJQkUtbWFCNG5mVmJSWU14Wldqd18wMjBvV3YxNzFEaTA2blJrWkdKU0U5OHhB?oc=5>

### Netflix, Inc. $NFLX Stock Position Reduced by Boston Trust Walden Corp
- Summary: Institutional sell‑off may weigh on stock momentum.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxObWp6WS1RSURnTG43Sy02dXI5TXpWeFpKdmdIVzFsbGItNG54M1pwUWVqZDBjSDdkV3lFZGwzSDJtUVJQcURrWlgwb2lQWDVNcTJnbEFQdjJ6ZzdMQlIxS3JjRW12bjZFQXlESU9xN1R4bGYtN1N5WlhTZ3J2eHYyQVFrbEVrWkFVcHFjc1BvTUdBc000dy12Q05DX1VSS09oSkd5QWFzNzRlZU5feU5sUzFqb3E2T09ZSWRkNVVBSVFaUnRJaHRv?oc=5>

### Netflix (NASDAQ:NFLX) CEO Theodore Sarandos Sells 27,312 Shares of Stock
- Summary: CEO sold shares, indicating possible lack of confidence.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxPd2lXbXpMOGQzWUpmQ0ZTWDJ5VnpQMHRESHFFajRxMHdNTkJmMlpfZkVzZ1NzUWxLWDNrR24xcnhkWV9PTUFWdmp6Y2h6Rk1naFR1b1ZJdmVPZHJrNllXNU55ZUFQcUZ6SV9FWDZoZUx5WGRGTjFJZXRzUE9nR0lvejBwLXpuR054OGpIYUZjZXlIXzRsMVhndE1KeWFMWUR6VEpBMFVjVzNIZlM0U3dJZGZFOFhzb3pNeDBCc2VVOG1hbldhdmJaTHFnRQ?oc=5>

### Netflix (NASDAQ:NFLX) CFO Sells $612,085.95 in Stock
- Summary: CFO sold shares, raising concerns about internal sentiment.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPZnhfcDByNFVWUlVJbTdIR3JVZ1UtZmdYeGNsSVF5S0JQckZtWFhJU0pPVFdieGNPSnR5QXZ1WDZjRldpai1Wa2hJdTVSVDZmUXpVeEx2SzA4TmJEdnlKS2ZkOEhoLVhiN19pVjd4YTJ3ZEtrVnJWY2VUeGI0VURSSWpaOFJINUNTUVFwMWJNaTJDNkRkcEd2bTFuWXF1QUwxTkpnam5YSTRkY1phLWc?oc=5>

### Commonwealth Equity Services LLC Sells 143,113 Shares of Netflix, Inc. $NFLX
- Summary: Large share sale by a firm, potentially signaling negative outlook.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxQa0VEaThTdl9JVVh1d3d4a25FVUxXZW9YbG5VMlVrcFR1Vmp4UEUya0RLZUxwYWR1ak5oZmNXV1czQXduSFdTU0dwdTFkOTR2a2s1SjdYeVVWNDI1dWNZUWgtYWtSY2FnanJneW1Gc2dqMlZQUmZuZzdCMjd5WmVsQ2xpdnNpQ2szaFp4RFlrbG9XdG82WEZuWWZyVnZjWmt2SzlKRGJ6OE1WNjEtZTlpUUY3Nl9Vc0RyMUtRQ1JFSWhsRTA4RkZtM0NRQWFXUQ?oc=5>

## CATALYSTS

### Netflix (NFLX) Stock Looks Cheap With 23% Upside To Fair Value
- Summary: Netflix (NFLX) Stock Looks Cheap With 23% Upside To Fair Value
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNU3JaOWhSd2RhT3RScnpyQWRnWGRTZ0w4UjcteEJfY0phVVQ2UWlfLVctbEtFZnptSkU2Y2RiRDJfNFYwYWtHR21CaV8xdUxWYW8xNzNmOGR5U1hzQzhhX2hWam1iUHFHSnRCb2E2RG9CUU9kZHhMZGh5cldLcllMTjFXdTVfWGdDaGJUTWYtNzNBOFVLOGZFZ2x0NA?oc=5>

### Netflix, Inc. $NFLX Stock Sold by International Assets Investment Management LLC
- Summary: Netflix, Inc. $NFLX Stock Sold by International Assets Investment Management LLC
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxOVFc2eFFtOHhZaU5FZ2xCX2xYUTlLRzI1aUVOc2dLZ0JfUWZKN2ZuNHV5TUd1bC1OZUZ5OEFnUHdyeGNXR3J3Rzc0TVNZTmtrVVgyMFAzOVluNVkyZmJXdlNKc21JMUxPQkR1dzF4TjVzVXNrdHVFa1VIaDdqWDZGcjFpYXlUQnlKTnVFQkdzUjlBLWlQUTdWY0syTmJZMzB4eGFiS19EWThsTXRsekNDakYyN09TVXlyRWZ6d3FNb3lFd1czWm13dmZLSUItMzdrbHA4RA?oc=5>

### Insider trades: Netflix, Intel, Visa among notable names (V:NYSE)
- Summary: Insider trading activity involving Netflix shares noted among several companies.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPU1FaN0dLTS0xR2F6NmtmajJrblZBaHV2MGFEbURkU0x5Si1Jd2RadThjZWxIYjVwM0sxcHBsWGdtN2UwWHJvbGNvTkJzUkFLNkU5SXVESGNBWHZDUlZVSFR1QlF4R21yU3JUT25MUWNBLXBkSHVsdnBoTjVaMWpZVTBmV01JclZ6RWk4WlFIbFR1QlJNV1E?oc=5>

### Netflix (NFLX) CFO sells 9,253 shares after 18,428 stock units vest.
- Summary: NFLX CFO sold 9,253 shares following vesting of 18,428 stock units.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNOHl0YUJfcS1vbWtyNTBCRUtnME5wZVRuRlcwVWpsNzc4Mkx1NU5fTEwwM0sxajdNaXBjelp4eS0zOUVXUTQ4Z01mbDNNUXJsRlRKSXpzYkxEX1hwMEQzRzhGLWFMTjJEd0dRUElXbkdYcUEwUTlQN2tRVzcyLVBZY1g5QVVXWVh5cmpHNml0TjVtSFZIUERTQmdUbzYwU1NUNnFQNldyalU?oc=5>

### Netflix, Inc. $NFLX Stock: CenterBook Partners LP Decreases Holdings
- Summary: CenterBook Partners LP reduced its holdings in Netflix stock.
- Date: 2026-11-08 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxOWFVMQVpvNnNRVVNUTzRfZmY5YkFhX05hWnFsQ3EwTHRWRlRpWUcwSGx4eWVoMkFwWXhnbHAzWURtS0xPb2dHZThNZm5WNTVNb3BOUDYtWkNFM2JDd2FiWU83eU9Vak9FanlFUk5QS1I2YWRVOFNWRHYyOE9SRnVUQjJ6NXFiUHY3cUk2WGhiSlV5a2dLR1JDY3Q4c2ZsMVNIX2ktZW9KR0tjTzlEbXROUW9TZXlFOTNXdTNmQnpiZVVySlE?oc=5>

### Why Netflix Stock Plunged 11% in October
- Summary: Shares fell 11% in October, reflecting market concerns.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPVEFpUE1pTmNGWWlJcl8zOTdBeXJKeEpiejc2cUtJLXJfYnlsanktbGxyMjBMM1c4Y0I1NDVkcEdNenRxV0VZTzJjc3Jia1dHMERFUEpVQmNvMnNTbTEtMkJCZF9iV09vbk9TNzNOOEN6UVBacUU2S0pERzk5Y01TWnBJS2N3U09LdjFHTl9Gb0g5QVNGb0ZqNQ?oc=5>

## RISKS

### Netflix's Loyal Subscribers Are Not Priced Correctly (NASDAQ:NFLX)
- Summary: Netflix may face subscriber churn due to pricing misalignment, potentially impacting revenue.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPcnRVQjVzNlRVdG1lSXIzSHZMMHhIZ0NycFp6V1lVUjVBdjRyVFV4c1V1LVQ3SE5qRVlRV21XbU1IcUEtLWNPNHo3bHlPc2FUcTExTU9pS2FMMERuZ181TUI5Y3ZJcTltQndNWWZqdFhKQTFMbTNiQ19odDN2YlVnMXpBVVE0cU1tWF81WjFPM1Y3ZG10aXpB?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **18.44** | **8.87** | **16.86** | **11.80** | **259,766,173,696.00 USD** | **-43.52** |
| DIS | 24.58 | 1.87 | 12.09 | 6.80 | 205,838,336,000.00 USD | 7.75 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 7.76 | 0.95 | 5.00 | -6.10 | 87,887,405,056.00 USD | 2.59 |

Peers fetched as_of: 2026-11-10; NFLX reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-10

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQR1JJT2J3ajhuUFdIQ1ktWGFuN3JBb1laWnRGUERRNmdha3pwMzE0T0xkUHNIR2xaZGtLYVNNTHVybkZmZWZPeUpXNTA2MjZxWXFBRWZDWVBYb1p1VGdaUS0zdG9KRFFIWGFaaE5XaDlPRjVyRS1pUTN6dE1PYVh4dG9VeUZpVzExQTRtOFBHQml5dGItaGVVdUdDSXR0YXRfS2JRLXpDQ2w?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPd1NLeHE4Skdqd3NHRk8wSEtWSlpVazJfcEZVV0FjT0gzdElUQjEwWUs0LXdqeE9PZTAzcGNiZTJLMHNNS0h6TGVSOExwb3puOU9ybUliWHNsb2pYbnhVWjNQSXo4bjYtWFlWWHRLdWRjbFZ1ekc5c1lWWE95YXB2d1NrMXVjdDliUFJGVktOQUlBM1NBZTRlREhR?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNZ1FibVQ3b2RIcTlGWk9ITmo2cTVrMEF5WkhvMlBVYjlrcFMtcElfTkI5VEVVZXUzYWpfZUtxcVFNMC1IZzJQcVo3enVSZzVXOE9nLWxzSVdvYldZbmxJQkUtbWFCNG5mVmJSWU14Wldqd18wMjBvV3YxNzFEaTA2blJrWkdKU0U5OHhB?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxObWp6WS1RSURnTG43Sy02dXI5TXpWeFpKdmdIVzFsbGItNG54M1pwUWVqZDBjSDdkV3lFZGwzSDJtUVJQcURrWlgwb2lQWDVNcTJnbEFQdjJ6ZzdMQlIxS3JjRW12bjZFQXlESU9xN1R4bGYtN1N5WlhTZ3J2eHYyQVFrbEVrWkFVcHFjc1BvTUdBc000dy12Q05DX1VSS09oSkd5QWFzNzRlZU5feU5sUzFqb3E2T09ZSWRkNVVBSVFaUnRJaHRv?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxPd2lXbXpMOGQzWUpmQ0ZTWDJ5VnpQMHRESHFFajRxMHdNTkJmMlpfZkVzZ1NzUWxLWDNrR24xcnhkWV9PTUFWdmp6Y2h6Rk1naFR1b1ZJdmVPZHJrNllXNU55ZUFQcUZ6SV9FWDZoZUx5WGRGTjFJZXRzUE9nR0lvejBwLXpuR054OGpIYUZjZXlIXzRsMVhndE1KeWFMWUR6VEpBMFVjVzNIZlM0U3dJZGZFOFhzb3pNeDBCc2VVOG1hbldhdmJaTHFnRQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPZnhfcDByNFVWUlVJbTdIR3JVZ1UtZmdYeGNsSVF5S0JQckZtWFhJU0pPVFdieGNPSnR5QXZ1WDZjRldpai1Wa2hJdTVSVDZmUXpVeEx2SzA4TmJEdnlKS2ZkOEhoLVhiN19pVjd4YTJ3ZEtrVnJWY2VUeGI0VURSSWpaOFJINUNTUVFwMWJNaTJDNkRkcEd2bTFuWXF1QUwxTkpnam5YSTRkY1phLWc?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxQa0VEaThTdl9JVVh1d3d4a25FVUxXZW9YbG5VMlVrcFR1Vmp4UEUya0RLZUxwYWR1ak5oZmNXV1czQXduSFdTU0dwdTFkOTR2a2s1SjdYeVVWNDI1dWNZUWgtYWtSY2FnanJneW1Gc2dqMlZQUmZuZzdCMjd5WmVsQ2xpdnNpQ2szaFp4RFlrbG9XdG82WEZuWWZyVnZjWmt2SzlKRGJ6OE1WNjEtZTlpUUY3Nl9Vc0RyMUtRQ1JFSWhsRTA4RkZtM0NRQWFXUQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNU3JaOWhSd2RhT3RScnpyQWRnWGRTZ0w4UjcteEJfY0phVVQ2UWlfLVctbEtFZnptSkU2Y2RiRDJfNFYwYWtHR21CaV8xdUxWYW8xNzNmOGR5U1hzQzhhX2hWam1iUHFHSnRCb2E2RG9CUU9kZHhMZGh5cldLcllMTjFXdTVfWGdDaGJUTWYtNzNBOFVLOGZFZ2x0NA?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxOVFc2eFFtOHhZaU5FZ2xCX2xYUTlLRzI1aUVOc2dLZ0JfUWZKN2ZuNHV5TUd1bC1OZUZ5OEFnUHdyeGNXR3J3Rzc0TVNZTmtrVVgyMFAzOVluNVkyZmJXdlNKc21JMUxPQkR1dzF4TjVzVXNrdHVFa1VIaDdqWDZGcjFpYXlUQnlKTnVFQkdzUjlBLWlQUTdWY0syTmJZMzB4eGFiS19EWThsTXRsekNDakYyN09TVXlyRWZ6d3FNb3lFd1czWm13dmZLSUItMzdrbHA4RA?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPU1FaN0dLTS0xR2F6NmtmajJrblZBaHV2MGFEbURkU0x5Si1Jd2RadThjZWxIYjVwM0sxcHBsWGdtN2UwWHJvbGNvTkJzUkFLNkU5SXVESGNBWHZDUlZVSFR1QlF4R21yU3JUT25MUWNBLXBkSHVsdnBoTjVaMWpZVTBmV01JclZ6RWk4WlFIbFR1QlJNV1E?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNOHl0YUJfcS1vbWtyNTBCRUtnME5wZVRuRlcwVWpsNzc4Mkx1NU5fTEwwM0sxajdNaXBjelp4eS0zOUVXUTQ4Z01mbDNNUXJsRlRKSXpzYkxEX1hwMEQzRzhGLWFMTjJEd0dRUElXbkdYcUEwUTlQN2tRVzcyLVBZY1g5QVVXWVh5cmpHNml0TjVtSFZIUERTQmdUbzYwU1NUNnFQNldyalU?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxOWFVMQVpvNnNRVVNUTzRfZmY5YkFhX05hWnFsQ3EwTHRWRlRpWUcwSGx4eWVoMkFwWXhnbHAzWURtS0xPb2dHZThNZm5WNTVNb3BOUDYtWkNFM2JDd2FiWU83eU9Vak9FanlFUk5QS1I2YWRVOFNWRHYyOE9SRnVUQjJ6NXFiUHY3cUk2WGhiSlV5a2dLR1JDY3Q4c2ZsMVNIX2ktZW9KR0tjTzlEbXROUW9TZXlFOTNXdTNmQnpiZVVySlE?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPVEFpUE1pTmNGWWlJcl8zOTdBeXJKeEpiejc2cUtJLXJfYnlsanktbGxyMjBMM1c4Y0I1NDVkcEdNenRxV0VZTzJjc3Jia1dHMERFUEpVQmNvMnNTbTEtMkJCZF9iV09vbk9TNzNOOEN6UVBacUU2S0pERzk5Y01TWnBJS2N3U09LdjFHTl9Gb0g5QVNGb0ZqNQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPcnRVQjVzNlRVdG1lSXIzSHZMMHhIZ0NycFp6V1lVUjVBdjRyVFV4c1V1LVQ3SE5qRVlRV21XbU1IcUEtLWNPNHo3bHlPc2FUcTExTU9pS2FMMERuZ181TUI5Y3ZJcTltQndNWWZqdFhKQTFMbTNiQ19odDN2YlVnMXpBVVE0cU1tWF81WjFPM1Y3ZG10aXpB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
