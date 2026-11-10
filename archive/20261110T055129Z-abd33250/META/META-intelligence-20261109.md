# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T06:07:44.445673+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 20, 'rule': 4, 'ai': 14, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 20 unique headlines; 9 named publishers; 5 exact duplicates; 20 HTTPS source links; largest publisher share 55.0%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 641.3700 |
| Return 1D (%) | 5.1168 |
| Return 1W (%) | 5.7093 |
| Return 1M (%) | -10.7560 |
| Return YTD (%) | -2.5858 |
| Return 1Y (%) | 3.5122 |
| Annualized volatility (%) | 41.6909 |
| Beta vs SPY | 1.3823 |
| Max drawdown (%) | -28.7332 |
| Sharpe (rf=0) | 0.2508 |
| Downside deviation (rf=0, %) | 27.5619 |
| Sortino (rf=0) | 0.3794 |
| Historical VaR 95% (1D, %) | 3.7819 |
| Historical ES 95% (1D, %) | 5.6434 |
| Correlation vs SPY | 0.4540 |
| Tracking error vs SPY (%) | 37.5145 |
| P/E (trailing) | 21.88 |
| P/B | 6.02 |
| EV/EBITDA | 14.39 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 18.02 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 35.41 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.03 |
| MA50 | 676.0450 |
| Close vs MA50 (%) | -5.1291 |
| MA200 | 631.0729 |
| Close vs MA200 (%) | 1.6317 |
| RSI (14, Wilder) | 46.5029 |
| MACD (12,26) | -21.0860 |
| MACD signal (9) | -18.4320 |
| MACD histogram | -2.6539 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 641.3700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 5.1168 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.7093 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -10.7560 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -2.5858 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.5122 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.6909 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.5619 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3794 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7819 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.6434 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4540 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.5145 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3823 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.7332 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2508 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.0222 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 35.4140 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0274 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.8823 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 46.5029 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.6539 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.1291 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.6317 -> Slightly above the moving-average trend level.

## TAILWINDS

### Meta (META) stock is up, what you need to know
- Summary: Meta (META) stock is up, what you need to know
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQdHo5VDQ5cV9JSHgtMHozT3p5bGprYmhyUVRpd1p5ZDBtT0xVRXI1QkIwd1pldjA1a0dlclJPSDJjLXp3YmNfaUI1RDFSRnpwSVZCVWFHVXVhZ1JmczR0WU9BX0w5UFlYcDBWRllkZ1ZZM3BKVnJqVjVMTGpJanEzdEFRMWlaV0JiclNXdWZPSFBiQkNHdmVkSTBLeWlGcElkeUhJYjItYw?oc=5>

### META, AMZN Stocks Jump As JPMorgan Picks Pair Over Alphabet — Sees Stronger AI Returns, Cloud Growth
- Summary: JPMorgan names Meta and Amazon top picks, citing stronger AI returns and cloud growth.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPUlRYcGF5YmpQQkx5NWI4RHdxbjNNNk16RldoUnduOG5hTzJYSUVxSFprTmNKXzVJZlAybzVUMzNzX3JPYTNObDE5enVrckpoOEtCWjZQNjVrOHJyMUY5OEFXa1p5OGdxLUFIWGhGM0Jxak5EeURaNHlxY0R6RUFuenFOVmI1SEVHSVBXY1dneFYwSGhlaXVtYk1Vcw?oc=5>

### JPMorgan drops Alphabet from focus list, adds Meta on AI advertising gains
- Summary: Meta added to JPMorgan focus list after dropping Alphabet, highlighting AI advertising gains.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPckw3MWpvTm1BeDN2UnlnYUc3WlBXOVVvRlU0RzItcUNhQjlhN1RVVG1OV2ZrcmNqOHN4bmJZMjRvMDhFemZRbk1mOUQ5VDhQSHRGdnY3c3hYWklpMW1NY0M5VV9BUVAyczlRaWZjVG5tRGlOb1FaVEhfMkN5NXgydmhwcGFkbGJZdFVuVlhwSHY3eG9qRGM2V1ktZ3A2aGty?oc=5>

### Meta and Amazon Rise 5% as JPMorgan Names Them Top Internet Picks; Alphabet Gains 3% Despite Losing Its Spot
- Summary: JPMorgan names Meta and Amazon top picks, boosting their shares; Alphabet gains despite losing spot.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxPOVp3bm5xUjBCSVRnZDlvZzNhOExzYWxpakkxMG9CM0JJMS1TeDh0TGM4Q202U1M3bWdSXzZnTzFhZDBtMHFYT2k4UUpDREtmUUNGdXNJR3pVZzJXLWg0ZFBZYUhDN3dsbThfYVpEVmIwSlpxY1FfM2J1YnYwejJLOE5CSmtpSmRPWUk4RDZHcFo0eXJMbXVIREE0UjI0TEhwY0tDendxVzlqMzAycVNQVHBKVjB2QkxiZmZOQjY0N21ZV0FaTlUybk1sVm1HRFkwaG5TdEUxb2l0TTFHaGxmbjR3MA?oc=5>

## HEADWINDS

### Meta Stock Dips Towards $600 But Don’t Load Up Just Yet
- Summary: Stock decline suggests short-term downside pressure.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE5IV0M4bnduUzdZYjg0UjlTLS1CWkF2QlhvdUtlSkxmbWFfeDFzVjhPWTRBdWU5Y2lfU3Eta0N6d0VoNXVIeV9fdlpMQzZlWm5RZHo4UjluLVhrRkxkRWF5VlZDMTFKcVEtRzhQLW5LWlFIYlMxWFRnUnY3WWluQQ?oc=5>

### ETFs Are Net Sellers of Meta Platforms (META) on Nov. 4
- Summary: ETF selling reflects negative market sentiment.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNSjBBYkI1NnY0UWFnaVhPZzJIaFlrQS01LTNUMk9UNEVjMU5HUmZvTjdQUFZ5V2RCbHJ4R1RmSWVTOTFUZUNfbnppczFTMDVyZktVcmF2d2taaldyZzR6a0pNLS1FN2pyNi1mR2lQeWVHYWtablBYSlNLZUw2M0FvRW00b1UzSmozSWw3VGt1N2FJa1BvSmNDcE9rS2k?oc=5>

### ETFs Are Net Sellers of Meta Platforms (META) on Nov. 5
- Summary: ETFs sold Meta shares, indicating net selling pressure.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPeU53QjM2VzdMNWQ5dGtzNlVwLWdWbU9fenBHZ3pkLWFtYXJlYkJUWjViTTN1LVo3aU1oLXNiQU9DNjNKZzhlMnN6YlhaSDFabUF1NFgzMG9tT3YzWmNvWjRLWE0tWkZjai1tSWZiSjVBSjFCUkVrWTNobHhsaFpIbU9RdElsTGN4QVUtSXVrb2x0NHpwMlVUWWRYdVI?oc=5>

## CATALYSTS

### Meta Stock Climbs on Muse Launch Reports in UK
- Summary: Meta Stock Climbs on Muse Launch Reports in UK
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxORVVHQ3NjN3pmQ1dDdFlUZUduN1poVHNVRTdwakFhSnhRU1NLQWY5NldGNWVzZTVmTlNEckdHSGFuZTduaEt5LUNlZG9IeW1KS3V6NjZGQzNyWHNnQnJSMFJFOE5BT05MNXBPYTkxWHNKdEZmX05hRGFZMGpWRkhRX19WUW9hYWZ0U056bUVhY3kxYzZBTDZNMlFvUFdtN3FLV2JDeTBKbkpYVW8?oc=5>

### Meta Platforms, Inc. $META Stock Sold by AIA Group Ltd
- Summary: Meta Platforms, Inc. $META Stock Sold by AIA Group Ltd
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOUkhhYVVFbTF2VnVXcHh1UllNaWs1djhVZmFwR19IeGIxSnB0bm1rRE5oVmxMandIY3lzUFpOX29zV1NtRExRWFJPTW5hREdwWW00WG5FUlZTX1VWYzBQUHUxU0J0WFItTUdvT09halhQRzlMLVFRdkRRbVRmOEt3WDJPbngzRGFORjM3U0RvVks2MXlMdnRnR2dlZzJ2b3N3Y09XeFo3TEhoNExScHRqNmVB?oc=5>

### Meta Platforms Stock: Is it a Steal of a Deal at $650?
- Summary: Meta Platforms Stock: Is it a Steal of a Deal at $650?
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQWl90bVRBbmtwUVN2aEJ6enF6M0o4Yml4SlA2YVRvR3hCbkFFS1pVTnEweHlGMHd3UFgzQjBsY2ZIOEhpS1ZQbHY5U19jSk0xTF9yRHYzV0RmUGNNNmNCUW43a0wzUmxxVUtIaG9EV19xVU43a1ljcDFTTW5EYmxJNzJranVJbURuNUdJUU53OHJ1VXgzdS1md04xVzM?oc=5>

### As Meta Platforms Buys Conductor, Here’s How to Play META Stock
- Summary: Meta's acquisition of Conductor could expand its AI and data capabilities.
- Date: 2026-11-08 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQVUpIUGFQYkEyTllPRTVzMEViaGc3RkZHdG53VnNnZDJVUzhTVG02TDUtanlVODNIVzQxRXpqTXJ2MTdZVnhjZERLcDNxU015ZUVaOWdPSHFONnZYeXN0aE1qS3VvdXdRc1gtZW9OSHVqWXFzYlU3NVJLYjBkemM1MWx1ZUh5VU5yODRpUmZHMWVfcDlxVDJwMXhmX05hUmx6NlM3dFRSQ3o?oc=5>

### What Is Meta Platforms (META) Facing As Legal Risks Rise And AI Deals Expand?
- Summary: Meta faces increasing legal challenges while expanding AI partnerships.
- Date: 2026-11-08 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPcmJmaDIwcnRLMjh1eGNUOGhuVjJNMGhyNFltVkNCYl9wMG43ck9jWnpNMHY0elFkWk1aYnM2WERaZ0lTWVpqV3AwVnYwZ2p2QVFWREpnRG5mV3dvRF8yMUhOb1NUcDlnSjAtUTlCanZkWWhINjhWWmcxS2g0aXZJUWEwY2Qyc0kxV25ibHJXNGVRelh5Um85N0x1TmFoZw?oc=5>

### Meta (META) Stock May Be A Bargain After Huge AI Fundraising
- Summary: Meta stock seen as attractive after large AI fundraising.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQYWo4WHVSb0lrclRUVUZ6N1VJb3dERjlDQVFRSnFDMVNJRkU5NlFkQVRDTEdNRkMtZFB3dEFuMkdEUHdZLVM3a1IxdkNJbGY4ZGUwcWxwTmZEWkpzTzQ1Z19wX204ZUdzTjZmNjhlRDRXeXJYZFZZT0hCdXRtTm1aeGZuVDdEcVFtWHZ1bUlQOUVlOUFCOHRB?oc=5>

### Why Meta Platforms Stock Rallied on Monday
- Summary: Meta’s stock price increased on Monday, indicating positive market sentiment.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQRUdMOElZOWFLR1FCQzMxbE5XN0tJeElzdUdrUksySzktUlN3U2QyTGhLbmc0LVZ0b0RadmtCNzkzamlnV2d3dGZoU1Nveks4UHgwMmk4MU93b0owRHNtMjVTWEM4NDJPTDhlM2wyZ0hnbTl2djJ5eFZ4azRrdVN2T05TNWNXaTBHSWtQaG05NnNxV1NlTDdZS0IyQlNCZw?oc=5>

### Should You Buy Meta Platforms Before Its Stock Split?
- Summary: Discussion about purchasing Meta shares ahead of an upcoming stock split.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOeGliT3JmRml6TmRJN3VpZDRFU1RmSk55aWxZWlNVenV3U2o2UndNZTNJZEQ2QTB1Y2VfVXpxcHk4WUszOTdFRWNwVXh5eXRLaVZ1aHB6U2x0UG9ES1QxWDZMeUF5VlNPRjRScFlJOVpIbVc5YkhmVVFKRzR4cll3NE95MWR2MVl4MWZueWdBUzRlbGpnZUlKeDFQdw?oc=5>

### Better Stock Split to Buy: Meta Platforms vs. Sandisk
- Summary: Comparison of Meta’s stock split to Sandisk’s, suggesting Meta as a better buy.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNcnQ5anhkMFVrUURqQmdUVlpVby01N01JNkx2UEtMNFNxQkMyTkMzZjQ5eTMtelhoRGg0VldvVW9ES3kyeHcyMFJZOVpWNHJkRjJ2eXhwYWhPOEN4aFdBSHRIWXZjcDlXaEZGWS0zRTdCSllCcm52VkRyVUViNjNpY1JaMXhobEVMWVZEalJWd2xwREhpM2l3dQ?oc=5>

### JPMorgan Just Added Meta Platforms to Its Analyst Focus List
- Summary: JPMorgan has added Meta to its analyst focus list, signaling increased coverage.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOd2hEeUlDMndhMlBSeWhjS3FXa01sdTBLRTM1UnVIZFhJX1lWMmY1eWhjNnNjQl85Z3otN2Jaa0FfVWFzRW42ZU1OQmtQbEZKNThveWZJVDRGb2t4VDJrNjdPeTN2YXNaWTJyWnF4WnNJaE1LUEJDanpoWVVTbkJCYUlXRE9qMXk5Ql9aRF9QYXR1dC1DdEd1STZSR2ljUGpuTGZfMWhZVQ?oc=5>

### Why is Meta Platforms stock surging today?
- Summary: Meta’s stock is experiencing a surge today, reflecting strong investor interest.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPYl9SM01uVnc1VU51ZUxhV3IyenZOODZSN3dRbFJOYWpRY05Va3Y2ODc4RlYxTkhUWXNvUlItbGxzc3pzTUV0dXpLUG1BVXhpcWs2S3dsTW8waGZVMDhmLTlNWkpzWjhUS0J5UWpoczBOblVIT2oxUVZxVmVxVG9Cbnd5NTlTREhFTnNmeWlsU2NCQ3REei1nUnBTd3RpTi1oQ0ZHMmxB?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **21.88** | **6.02** | **14.39** | **26.10** | **1,639,876,001,792.00 USD** | **3.51** |
| GOOGL | 15.05 | 5.37 | 18.57 | 24.70 | 3,542,515,974,144.00 USD | 3.61 |
| SNAP | N/A | 3.89 | 164.68 | 14.30 | 8,719,212,544.00 USD | -38.49 |
| PINS | 79.42 | 3.52 | 35.99 | 11.90 | 10,931,058,688.00 USD | -29.64 |

Peers fetched as_of: 2026-11-09; META reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

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
- Filing date: 2026-10-22
- Revenue (latest available single quarter): 13,727,000,000.00 USD; period 2018-07-01/2018-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 9,860,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipwFBVV95cUxQdHo5VDQ5cV9JSHgtMHozT3p5bGprYmhyUVRpd1p5ZDBtT0xVRXI1QkIwd1pldjA1a0dlclJPSDJjLXp3YmNfaUI1RDFSRnpwSVZCVWFHVXVhZ1JmczR0WU9BX0w5UFlYcDBWRllkZ1ZZM3BKVnJqVjVMTGpJanEzdEFRMWlaV0JiclNXdWZPSFBiQkNHdmVkSTBLeWlGcElkeUhJYjItYw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPUlRYcGF5YmpQQkx5NWI4RHdxbjNNNk16RldoUnduOG5hTzJYSUVxSFprTmNKXzVJZlAybzVUMzNzX3JPYTNObDE5enVrckpoOEtCWjZQNjVrOHJyMUY5OEFXa1p5OGdxLUFIWGhGM0Jxak5EeURaNHlxY0R6RUFuenFOVmI1SEVHSVBXY1dneFYwSGhlaXVtYk1Vcw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPckw3MWpvTm1BeDN2UnlnYUc3WlBXOVVvRlU0RzItcUNhQjlhN1RVVG1OV2ZrcmNqOHN4bmJZMjRvMDhFemZRbk1mOUQ5VDhQSHRGdnY3c3hYWklpMW1NY0M5VV9BUVAyczlRaWZjVG5tRGlOb1FaVEhfMkN5NXgydmhwcGFkbGJZdFVuVlhwSHY3eG9qRGM2V1ktZ3A2aGty?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxPOVp3bm5xUjBCSVRnZDlvZzNhOExzYWxpakkxMG9CM0JJMS1TeDh0TGM4Q202U1M3bWdSXzZnTzFhZDBtMHFYT2k4UUpDREtmUUNGdXNJR3pVZzJXLWg0ZFBZYUhDN3dsbThfYVpEVmIwSlpxY1FfM2J1YnYwejJLOE5CSmtpSmRPWUk4RDZHcFo0eXJMbXVIREE0UjI0TEhwY0tDendxVzlqMzAycVNQVHBKVjB2QkxiZmZOQjY0N21ZV0FaTlUybk1sVm1HRFkwaG5TdEUxb2l0TTFHaGxmbjR3MA?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE5IV0M4bnduUzdZYjg0UjlTLS1CWkF2QlhvdUtlSkxmbWFfeDFzVjhPWTRBdWU5Y2lfU3Eta0N6d0VoNXVIeV9fdlpMQzZlWm5RZHo4UjluLVhrRkxkRWF5VlZDMTFKcVEtRzhQLW5LWlFIYlMxWFRnUnY3WWluQQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNSjBBYkI1NnY0UWFnaVhPZzJIaFlrQS01LTNUMk9UNEVjMU5HUmZvTjdQUFZ5V2RCbHJ4R1RmSWVTOTFUZUNfbnppczFTMDVyZktVcmF2d2taaldyZzR6a0pNLS1FN2pyNi1mR2lQeWVHYWtablBYSlNLZUw2M0FvRW00b1UzSmozSWw3VGt1N2FJa1BvSmNDcE9rS2k?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPeU53QjM2VzdMNWQ5dGtzNlVwLWdWbU9fenBHZ3pkLWFtYXJlYkJUWjViTTN1LVo3aU1oLXNiQU9DNjNKZzhlMnN6YlhaSDFabUF1NFgzMG9tT3YzWmNvWjRLWE0tWkZjai1tSWZiSjVBSjFCUkVrWTNobHhsaFpIbU9RdElsTGN4QVUtSXVrb2x0NHpwMlVUWWRYdVI?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxORVVHQ3NjN3pmQ1dDdFlUZUduN1poVHNVRTdwakFhSnhRU1NLQWY5NldGNWVzZTVmTlNEckdHSGFuZTduaEt5LUNlZG9IeW1KS3V6NjZGQzNyWHNnQnJSMFJFOE5BT05MNXBPYTkxWHNKdEZmX05hRGFZMGpWRkhRX19WUW9hYWZ0U056bUVhY3kxYzZBTDZNMlFvUFdtN3FLV2JDeTBKbkpYVW8?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxOUkhhYVVFbTF2VnVXcHh1UllNaWs1djhVZmFwR19IeGIxSnB0bm1rRE5oVmxMandIY3lzUFpOX29zV1NtRExRWFJPTW5hREdwWW00WG5FUlZTX1VWYzBQUHUxU0J0WFItTUdvT09halhQRzlMLVFRdkRRbVRmOEt3WDJPbngzRGFORjM3U0RvVks2MXlMdnRnR2dlZzJ2b3N3Y09XeFo3TEhoNExScHRqNmVB?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQWl90bVRBbmtwUVN2aEJ6enF6M0o4Yml4SlA2YVRvR3hCbkFFS1pVTnEweHlGMHd3UFgzQjBsY2ZIOEhpS1ZQbHY5U19jSk0xTF9yRHYzV0RmUGNNNmNCUW43a0wzUmxxVUtIaG9EV19xVU43a1ljcDFTTW5EYmxJNzJranVJbURuNUdJUU53OHJ1VXgzdS1md04xVzM?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNakxvaEdiTzR5M0tqcm5KeE1mVDFYUTVuZlhCdzl6MHdXV0tiek90QU1qZHBxdktxWjNIaHNoRDhPNTVrN0F5OGx1VUtiTWhObkJRcl9pVXFDbzFsT2cxcTRwaHBKZF93cEgzM0JHd3VkVVpIZ0theFMxdEJIY2FvQ0xtSlQyNTMwNmlMRzVKYS0yRjZVMkR6cGln?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQVUpIUGFQYkEyTllPRTVzMEViaGc3RkZHdG53VnNnZDJVUzhTVG02TDUtanlVODNIVzQxRXpqTXJ2MTdZVnhjZERLcDNxU015ZUVaOWdPSHFONnZYeXN0aE1qS3VvdXdRc1gtZW9OSHVqWXFzYlU3NVJLYjBkemM1MWx1ZUh5VU5yODRpUmZHMWVfcDlxVDJwMXhmX05hUmx6NlM3dFRSQ3o?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPcmJmaDIwcnRLMjh1eGNUOGhuVjJNMGhyNFltVkNCYl9wMG43ck9jWnpNMHY0elFkWk1aYnM2WERaZ0lTWVpqV3AwVnYwZ2p2QVFWREpnRG5mV3dvRF8yMUhOb1NUcDlnSjAtUTlCanZkWWhINjhWWmcxS2g0aXZJUWEwY2Qyc0kxV25ibHJXNGVRelh5Um85N0x1TmFoZw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQYWo4WHVSb0lrclRUVUZ6N1VJb3dERjlDQVFRSnFDMVNJRkU5NlFkQVRDTEdNRkMtZFB3dEFuMkdEUHdZLVM3a1IxdkNJbGY4ZGUwcWxwTmZEWkpzTzQ1Z19wX204ZUdzTjZmNjhlRDRXeXJYZFZZT0hCdXRtTm1aeGZuVDdEcVFtWHZ1bUlQOUVlOUFCOHRB?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQRUdMOElZOWFLR1FCQzMxbE5XN0tJeElzdUdrUksySzktUlN3U2QyTGhLbmc0LVZ0b0RadmtCNzkzamlnV2d3dGZoU1Nveks4UHgwMmk4MU93b0owRHNtMjVTWEM4NDJPTDhlM2wyZ0hnbTl2djJ5eFZ4azRrdVN2T05TNWNXaTBHSWtQaG05NnNxV1NlTDdZS0IyQlNCZw?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPVDgwQzNoRXFMc0I4c2JPS3NtUEM0TEYxckxXM2RqQnZIUWF2T1Z0enZzM243RjBjUEwxZlo5NS1yQlNKN3h6UHE4UnpvQXgxSVdqYkx2OU53bHF3NGhWRFpGZkFDeGdTc3dweHNiOHpNdFV4YzBuZ1pMY2NWYjhqaHhRaVFycjFMYk83ZjNZUTVnb0dsRF8ta19HWmk2YWdDN2c2dTJxVHQtVk9EbEtvYW53ODhPV21QSjRYVjd5ZXNGUQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOeGliT3JmRml6TmRJN3VpZDRFU1RmSk55aWxZWlNVenV3U2o2UndNZTNJZEQ2QTB1Y2VfVXpxcHk4WUszOTdFRWNwVXh5eXRLaVZ1aHB6U2x0UG9ES1QxWDZMeUF5VlNPRjRScFlJOVpIbVc5YkhmVVFKRzR4cll3NE95MWR2MVl4MWZueWdBUzRlbGpnZUlKeDFQdw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNcnQ5anhkMFVrUURqQmdUVlpVby01N01JNkx2UEtMNFNxQkMyTkMzZjQ5eTMtelhoRGg0VldvVW9ES3kyeHcyMFJZOVpWNHJkRjJ2eXhwYWhPOEN4aFdBSHRIWXZjcDlXaEZGWS0zRTdCSllCcm52VkRyVUViNjNpY1JaMXhobEVMWVZEalJWd2xwREhpM2l3dQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPVHRJZU8xNzNENHV4eU4zOWgyMG00aWU5cnV1NVhpUVdQT1JpbmsyTmVpLXo5ckNTNVMtNkZRNFlRQ2FzeWlzampma0E3REVXSjJ6a21Ma1g3Y3dab21Nd3BNa1dFOEd5d2tpTGZxOEI5dFhZcWJzZ1VMUk9nc25QdlVmNS13LXVFQU5tam9NSEZKUnNQRGJB?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOd2hEeUlDMndhMlBSeWhjS3FXa01sdTBLRTM1UnVIZFhJX1lWMmY1eWhjNnNjQl85Z3otN2Jaa0FfVWFzRW42ZU1OQmtQbEZKNThveWZJVDRGb2t4VDJrNjdPeTN2YXNaWTJyWnF4WnNJaE1LUEJDanpoWVVTbkJCYUlXRE9qMXk5Ql9aRF9QYXR1dC1DdEd1STZSR2ljUGpuTGZfMWhZVQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQMmFWV1dTcEphNzdJU1psZHZReUJiV25PNnVMNnRzZzFKTzZycGRjeG5fM1FZV0RSM2xSZTRHUi1FdHBsTWVxa3lyWXhvZ0phY2EzWnN6T1JNRS1kdHRkUmFjMEI4YkxwX3RvcXUwMUlNaWlSak8tb19QZm84Z3ROQ0pvYWRmbGN0Uk5uYTVnbGtrUFZ2SERtaTc0UXNfZHF0?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPYl9SM01uVnc1VU51ZUxhV3IyenZOODZSN3dRbFJOYWpRY05Va3Y2ODc4RlYxTkhUWXNvUlItbGxzc3pzTUV0dXpLUG1BVXhpcWs2S3dsTW8waGZVMDhmLTlNWkpzWjhUS0J5UWpoczBOblVIT2oxUVZxVmVxVG9Cbnd5NTlTREhFTnNmeWlsU2NCQ3REei1nUnBTd3RpTi1oQ0ZHMmxB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
