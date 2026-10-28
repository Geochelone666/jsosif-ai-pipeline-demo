# GOOGL Intelligence Report

- ticker: **GOOGL**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/GOOGL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GOOGL/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:23:53.199654+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 6, 'ai': 13, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/GOOGL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 11 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 43.48%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 320.5800 |
| Return 1D (%) | 1.1932 |
| Return 1W (%) | -5.7894 |
| Return 1M (%) | -6.7865 |
| Return YTD (%) | 2.6210 |
| Return 1Y (%) | 19.3649 |
| Annualized volatility (%) | 31.4122 |
| Beta vs SPY | 1.3599 |
| Max drawdown (%) | -21.2178 |
| Sharpe (rf=0) | 0.7212 |
| Downside deviation (rf=0, %) | 20.0818 |
| Sortino (rf=0) | 1.1281 |
| Historical VaR 95% (1D, %) | 2.6868 |
| Historical ES 95% (1D, %) | 3.9692 |
| Correlation vs SPY | 0.5499 |
| Tracking error vs SPY (%) | 26.6325 |
| P/E (trailing) | 16.09 |
| P/B | 6.30 |
| EV/EBITDA | 22.04 |
| Revenue growth (%) | 24.20 |
| Forward P/E (estimate) | 20.87 |
| Gross margin (%) | 60.90 |
| Operating margin (%) | 34.03 |
| Return on equity (%) | 48.68 |
| Free cash flow yield (%) | 0.58 |
| MA50 | 341.8354 |
| Close vs MA50 (%) | -6.2180 |
| MA200 | 340.9083 |
| Close vs MA200 (%) | -5.9630 |
| RSI (14, Wilder) | 33.9609 |
| MACD (12,26) | -5.9088 |
| MACD signal (9) | -2.4931 |
| MACD histogram | -3.4157 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GOOGL': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 320.5800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.1932 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.7894 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -6.7865 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 2.6210 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 19.3649 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.4122 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.0818 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1281 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.6868 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9692 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5499 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.6325 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3599 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.2178 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7212 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.8729 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 60.8970 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 34.0330 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 48.6760 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.5781 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.0853 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 33.9609 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.4157 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -6.2180 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -5.9630 -> Clearly below the moving-average trend level.

## TAILWINDS

### Alphabet Stock: 3 Reasons Why GOOGL Is a Buy Ahead of Q3 Results
- Summary: Analyst recommends buying GOOGL before Q3 earnings.
- Date: 2026-10-26 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNdU9hYUVJMi1OZ215WmFqRjVyZlI0bEowaVdKZ2tfTEQ5WHBCcEVVU0JxQnVaUnBXSWxnbWpqQVpVZHE3aDZFMDZSaUxXZzZ6a1luMVNsb3JoZ3FrTXEwTmwxbGRTZC1PNVl2SWRxMGk2RVB0eFRxd3AzQkdVdGJnZGtocm53emJSNXVodmNzcUpOcHdYSUF1RTJ0bEM0VW1vb05FQy1FYk9ySkk?oc=5>

### With Alphabet Narrative Improving, Go to GOIB for Income
- Summary: Alphabet’s narrative improvement may boost investor confidence and support stock price.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNRGRtRDdzQmRKMHZ0dExBS1FrbEY4aU83dFB3ZVQ2eWtNczVTOXQtWDRuYkR3U3VmQjl5RWthNWlZVmhGeE5FVHlXM25TcEIzZk5oUXNydnNqUzJ4RWJyVHNfRGNNRUpNMzlzNFN6N0xtZ2JRV0xaNmh6Vm1Ia3lGb0NPdnRYcjA1N3I5emNuOGIzNW5yQzExZEI4dlhBM21XNzNmeWFGMA?oc=5>

### Will Alphabet Stock Surge After Oct. 28?
- Summary: Speculation about a potential post‑earnings stock rally.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxPZkw1ZWwxN28zeHVHbmpScjhET3ZmNXQ2MGRLbXBxQmh2d0hScDdKd050ckgyLVJaNVhVWS1kNjB5MktfYktkVHVadVRJTWNfMjVPd2QzbzhjaktSeFVVV2ZUNUFMcjRPamMySUR4X0pFUTl4N1prVDdRbUJMaUR1VE96MFNoNkxW?oc=5>

## HEADWINDS

### Alphabet Stock Breaks Down Ahead of Q3 Earnings: Could GOOGL Fall 30%?
- Summary: Stock falls sharply before earnings, raising 30% drop concerns.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPWktkYzZaNW94WldwdUVfMjdHNWxiSTFGZjM2NWt2MlZiQUVOMjM3a1k4ZDhJZjlMMnB5dHkzdk1qelBxQlVzT1VpbG5qSDFXQ2VoTFZLaHRjZlkyRzQ2R2ZJMHQxaTRWM09TRC1iRms1TW1aVTZmRFRmcmVWN0h6czNzblVvOF96bWVHQUowTnI5aHZuMzhYcDJzMXZGQQ?oc=5>

### Stock Market Says Alphabet Is AI Loser
- Summary: Market commentary labels Alphabet as an AI underperformer.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPRDVqeFNzN1ZZRXdEZ1VqUzFCSWg4bm83RVR2dzJDdng1b3RzcWFLSnAxRVVwNnBxNFdYNHNIeGRIbThJQnBTazhtNUpkdkEtZV9zLUgxazJHU3F3RXNKZDM0bk93a1kzUUU4bFJqLTQ4Zm5sWGlmYkQxU2tfX0hXZm9pWEhwcldGZ0E?oc=5>

### Alphabet (GOOGL) Stock Declines While Market Improves: Some Information for Investors
- Summary: Alphabet shares drop while broader market gains.
- Date: 2026-10-20 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQMHNybk5IRjdMd2pyanVGSGR4cVplVmJiOXAyV1FRYlpKcEdOcmlHemFpWms0OFRaQkFmeEJjcTBLYzlBUWF4YklzejEyV1ZzdHFyclp2NWVpZnVJR1lqVktzdkgtRUR2VXlYcm5mczVDS3dzak5MZWY1YWp1dmtfS0IzS3VDel9GbDVkb0lpcUx2Sy1YdkU0LWN3blotZFBwVnc?oc=5>

## CATALYSTS

### Alphabet Earnings Dilemma: Organic Traffic Slowdown Meets Unstoppable CapEx (NASDAQ:GOOG)
- Summary: Alphabet Earnings Dilemma: Organic Traffic Slowdown Meets Unstoppable CapEx (NASDAQ:GOOG)
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOdVdOMFZGMHJPRlFHZF9LT3lWdTB6eHBaeHY0cHVPRUZ5TU5xSGxRWlFmTmFfY3R2N3lHN0d0UTlNTnlRNnk5dTgyb3VzTHh1NEJVTmdlajJCaTFtNHhQRTZ2YWRBVjFoelVtc1U2Rk1rOG80WU9FemE5NVhmYjB3R2c5N1RJQnBiQTFzYzk1M1dFOXFwdEkzLWF6akJWcE5CenNSQmhjTTEwekFGQTNUSTh0clVEZw?oc=5>

### GOOGL Stock: 3 Things to Watch in Alphabet’s Q3 Earnings Tomorrow
- Summary: GOOGL Stock: 3 Things to Watch in Alphabet’s Q3 Earnings Tomorrow
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQOXJuUTdKai1uYVdVS3JpZC1vWVFrTjEtakNmUGVoVGlpbEU3ejMxX0VtZkhMelNWQVVOZE95Z2hlLThHT0VpTDBicEdzR3BHMFBHb1c4dG9oMFJVSExCS0lRNXhVM25wQm1oemZYTTZpdXladUVQM0NrUEt6SGVJQ25ZNFJjY2NDMm8wR3JfMjJzQlh3SzlpcQ?oc=5>

### Alphabet Earnings To Accelerate The AI Bubble Burst (NASDAQ:GOOG)
- Summary: Alphabet Earnings To Accelerate The AI Bubble Burst (NASDAQ:GOOG)
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPTUZhTTJ5OXZzZjJtNmFDNTF5THFzSTRKeXJQemFEbUZoMndDSVd2UFp6V3N1QnFYRWhNejN5NW9GbkdhbTBpckRRMXc1eDZVenZWWV9tZUtYNnVoVExMWlBOTUFCcXVfeFBuMlNyV2NaaUdWOXZpUDJzNV93dGZMNlBaYlBRNHNWc3RqMUxBUVNkU19tV2tJ?oc=5>

### Alphabet (GOOGL) Stock Looks Below Fair Value After AI Spending Plans
- Summary: Alphabet (GOOGL) Stock Looks Below Fair Value After AI Spending Plans
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNTXJqRWlqNkRWekQ3dkJteHJzSjRZZlZvTkJjU3FDQ0kwRzlaQWNqWXRqaVFPQzZJemVXajRrYVBaWUtrSUpVNHZuQjZFdjdNOWIwVUVpSzVpSnUwdF9SUXJXWnVwUjZMMTVrWWJ1WEg2STNjTDRkdTJuLWZ3SWYyQ2lrRDBObHphRUQxSU16M0c5WW9SVTlsWkVCYWNBUQ?oc=5>

### Alphabet earnings: what to look for from GOOGL
- Summary: Alphabet earnings: what to look for from GOOGL
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOUEZWaG9TQUdXRGViU3Q1Xy1BTllUa2w4RWtLcVl2bk1sREw1Y0xzMHNuTzZ6ZUdTT21zUlU2VkFSZUJKM0hDZFV4OVZkN3pOX0V4R3NCY0RlOXF4X1NlS2FZc2dmU0ZKeUJJakpJNktYOGpiSUU2VnJ0N2diUDQ4Z2d0YnZheUVSb3BnOGJUVWxZY0VWdk90RA?oc=5>

### Alphabet (GOOGL) Q3 earnings preview: US$200 billion AI capex test puts major uptrend at risk
- Summary: Alphabet (GOOGL) Q3 earnings preview: US$200 billion AI capex test puts major uptrend at risk
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOTjBfSnRtNzBqeHZxYUZ3SzZBcFhHMUhSMVFHbmdnX3ZuRHgtOHQwUlJZSTQtNEJESVNVcG54YmhydUZnY1h0dndiUXhud0c1OTNxM212emgxdTlhNy02THFMX1hNblVaT3hzTGZZUi1idjRXSlRFaHQxOXB6M3NmcUEtQnV1YlliekxHSFRPRWdJYzNSYlNmS0JraFY0YmkzZjJ2MUR0dTNsNGhFemtoOGRidHRVZ3lOM3hYM2lQLXkwRktj?oc=5>

### Here’s How Much Traders See Google Parent Alphabet’s Stock Moving After Earnings
- Summary: Expected post-earnings movement of GOOGL stock.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxQbGtJWXRlTkUxems2ckVtd1RmSTZGVW8zN0RBUGlSWGtLekdWVk9wWGlFcWt3MUNrcjJocEpUUkNxbE5RNy1TMDRKazhFbHpmWjR2WEVHNmRsZ3RJeXA4eFpubm9IUnRzZGRPd3FCbENoTTNpcXNidFpQSGZJY2VGUDlramhXalA3bWM5S1VhMDRfNENpUEkwWUZ6ekRUbVoxWGwxQ2lxT1dvcG5PZ1VOZ2tXNUFfSTdoMUZDYUY0bTJuWUFzRFdJT2NBNWU0QQ?oc=5>

### Alphabet (GOOGL) Pushes Google Play Into Cars With Native In Vehicle Integration
- Summary: Alphabet expands Google Play to in-vehicle systems, enhancing its automotive ecosystem.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQQXZEeUdLVkFRYTNCeDNjQlQ4Wmc1bWdJSDdjYzV3RTZsY3o1S21jRVYxdkZKaVVlM19TMHhGaTVsSnVEVFVTaFNHcU9xbEhWaUxFNENjcm5TMjRMdkt0cXRFczJqcjdVRklTanRVVGp0dEYtWHpSZlQ3QXh1Q3BYQmpXYUdueVlRczNjR0pSSDVGa2VzRm95OGViV05OZw?oc=5>

### Ahead of Alphabet Earnings, Here's What Barchart Data Says Comes Next for GOOGL Stock
- Summary: Barchart data provides insights into potential post-earnings movement.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPTmxSV0pmUGUxb3J2OGsxVkJYRzd6a3BSZk9sYmQzQ3c0cXNYUXBSLTZSQWIxY0k1al8wX0hGOGY5VWVOdVpseTkzX0tLb0VPUnBYQjc0ZHNDY1B0NWREWHRfLUxnVHZPVjVSamRRNmVIZF9ETkNTUlkyOU13OE91dXJSc3FyTk44SVZldUh1NFhKTzgzZGlXX3FGQm9xNDRKOXRvS0t3?oc=5>

### Alphabet Must Show This on Oct. 28 or the Stock Could Stall
- Summary: Upcoming Q3 earnings release on Oct 28 may influence stock movement.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQa3BsVTlXaUtORjNLS1lEbENwQUdUdEQyVWRhcXVWcnRqOUJOMmg4dHRENXFhOWZUUEFWUTlka2YzLTFNaV9lQnJlZVhWeEwwdi13OUtMR2dHVWlQRTZPaWUzOGRfSWpnZGtQTGxWRFJRcXhLMlpKVDFnSW8yaVFCSmdreFNFb1Y3OHBZR1VzODZjNElRSDBHWA?oc=5>

### Alphabet’s Q3 results to put AI spending back in the spotlight (GOOG:NASDAQ)
- Summary: Q3 earnings will highlight AI spending trends.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPelQ4bXZ4M3hOSWJyM3F1QnJzVmprUTVjQXc1cEEwTDN2R2lXcE05VzBQUlRIVXczSE1CclE5dW93MHZ2dEtsMXVUdHg2bmJTVVhQZWlkd2xxS0sweGc3S2dLQ1FXUlZqVVJ4NlFTbzdTMTJMYlZMSlRMcVhTYTNHenB1bFE0LTBRaWdrbkh0RTlFeDdpZnliSTZsbVptZ0NE?oc=5>

### Dear Google Stock Fans, Mark Your Calendars for October 28
- Summary: Reminder of Q3 earnings release on Oct 28.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOeGdPZEtqTVoyV1hTUEhTSVhNOFBvd24tcFNjTldvVkR2THZvTlZtWjcyMlVTakRqYnhoSVk2SEZURDFaMUxnWXNNVnRxYTRIZTNNd2N4TTVENEJCdkEzS3BCUEpEZklYY3JTZVNZM3drQTJ6czR5OGdNUlJPUDdKeTBZOGo0RHpNQ09MSnlKX2JySTBKZnJn?oc=5>

### Google to report Q3 results as investors focus on AI growth, weigh Meta Muse AI risk
- Summary: Q3 earnings will address AI growth and Meta Muse AI risk.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxPeFNCNzhFanV1OTduaTk2dkZ3VzcxSF9zcWl3NzJVdTIwUGNDLXZZMTNnVjA2S3A0eUpOQ1R1Qk1VS3dkbHpzaVBEQ1lMUUdhTExFUDFuRTEySGh1aGdzVXlWeGVrdy0ta1FDelc0NWVHal9GODJfdjJ0Qy1PMWJzQ3psLTNvZWJBWWJMdXVxdk9hZkFfVi1pLXpwdVFtU0pMZVRLalM0NlZnZlE4WUl2OXhXbGp5OWhtYUNiRjRuWVprQlNycjhlbTZQa21yZTV2bFVSY0hqWnVYU1k?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GOOGL** | **16.09** | **6.30** | **22.04** | **24.20** | **3,920,672,325,632.00 USD** | **19.36** |
| META | 21.16 | 5.82 | 13.92 | 26.10 | 1,585,722,294,272.00 USD | -17.12 |
| MSFT | 29.60 | 8.92 | 20.58 | 17.70 | 3,945,415,311,360.00 USD | 0.79 |
| AMZN | 20.36 | 4.95 | 16.92 | 19.60 | 2,730,015,850,496.00 USD | 11.51 |

Peers fetched as_of: 2026-10-27; GOOGL reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-22
- Next expected earnings: 2026-10-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-23
- Revenue (latest available single quarter): 119,796,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 112,193,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNdU9hYUVJMi1OZ215WmFqRjVyZlI0bEowaVdKZ2tfTEQ5WHBCcEVVU0JxQnVaUnBXSWxnbWpqQVpVZHE3aDZFMDZSaUxXZzZ6a1luMVNsb3JoZ3FrTXEwTmwxbGRTZC1PNVl2SWRxMGk2RVB0eFRxd3AzQkdVdGJnZGtocm53emJSNXVodmNzcUpOcHdYSUF1RTJ0bEM0VW1vb05FQy1FYk9ySkk?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNRGRtRDdzQmRKMHZ0dExBS1FrbEY4aU83dFB3ZVQ2eWtNczVTOXQtWDRuYkR3U3VmQjl5RWthNWlZVmhGeE5FVHlXM25TcEIzZk5oUXNydnNqUzJ4RWJyVHNfRGNNRUpNMzlzNFN6N0xtZ2JRV0xaNmh6Vm1Ia3lGb0NPdnRYcjA1N3I5emNuOGIzNW5yQzExZEI4dlhBM21XNzNmeWFGMA?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxPZkw1ZWwxN28zeHVHbmpScjhET3ZmNXQ2MGRLbXBxQmh2d0hScDdKd050ckgyLVJaNVhVWS1kNjB5MktfYktkVHVadVRJTWNfMjVPd2QzbzhjaktSeFVVV2ZUNUFMcjRPamMySUR4X0pFUTl4N1prVDdRbUJMaUR1VE96MFNoNkxW?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPb0JQMTd0VVJ1SXFnZEIyakxDLU9VT3p2bTdOYWk1ZU9ONWV0aVc1MERVM3lhWk0yS0d6UFV5R05lSEk1SmtxM3N6QWlWYzF2eTVMWk1zWlhOM2ZobU9kVkcxaXFiU2NNMjFuaDY1NTQ1aWd1TXZyd3FnTzAycno5Qzl4MEd2NTV6QklzZnFubmwxTXZnVU5B?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPWktkYzZaNW94WldwdUVfMjdHNWxiSTFGZjM2NWt2MlZiQUVOMjM3a1k4ZDhJZjlMMnB5dHkzdk1qelBxQlVzT1VpbG5qSDFXQ2VoTFZLaHRjZlkyRzQ2R2ZJMHQxaTRWM09TRC1iRms1TW1aVTZmRFRmcmVWN0h6czNzblVvOF96bWVHQUowTnI5aHZuMzhYcDJzMXZGQQ?oc=5
- https://news.google.com/rss/articles/CBMidEFVX3lxTFA5em5wVEFCX1hDblFxYXI1WVdpVzFYNHFHUTlsQWpmb0NCbmpEWVN4OEQ5UDNYTjJDTmJXN3NQRzMxLVpwUmczWWUyQVROTmhsaVFfWHJmWG5SQWxOTDBEbmtsYkduTzR2T29sd3VwUHZhajBo?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPRDVqeFNzN1ZZRXdEZ1VqUzFCSWg4bm83RVR2dzJDdng1b3RzcWFLSnAxRVVwNnBxNFdYNHNIeGRIbThJQnBTazhtNUpkdkEtZV9zLUgxazJHU3F3RXNKZDM0bk93a1kzUUU4bFJqLTQ4Zm5sWGlmYkQxU2tfX0hXZm9pWEhwcldGZ0E?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQMHNybk5IRjdMd2pyanVGSGR4cVplVmJiOXAyV1FRYlpKcEdOcmlHemFpWms0OFRaQkFmeEJjcTBLYzlBUWF4YklzejEyV1ZzdHFyclp2NWVpZnVJR1lqVktzdkgtRUR2VXlYcm5mczVDS3dzak5MZWY1YWp1dmtfS0IzS3VDel9GbDVkb0lpcUx2Sy1YdkU0LWN3blotZFBwVnc?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOdVdOMFZGMHJPRlFHZF9LT3lWdTB6eHBaeHY0cHVPRUZ5TU5xSGxRWlFmTmFfY3R2N3lHN0d0UTlNTnlRNnk5dTgyb3VzTHh1NEJVTmdlajJCaTFtNHhQRTZ2YWRBVjFoelVtc1U2Rk1rOG80WU9FemE5NVhmYjB3R2c5N1RJQnBiQTFzYzk1M1dFOXFwdEkzLWF6akJWcE5CenNSQmhjTTEwekFGQTNUSTh0clVEZw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQOXJuUTdKai1uYVdVS3JpZC1vWVFrTjEtakNmUGVoVGlpbEU3ejMxX0VtZkhMelNWQVVOZE95Z2hlLThHT0VpTDBicEdzR3BHMFBHb1c4dG9oMFJVSExCS0lRNXhVM25wQm1oemZYTTZpdXladUVQM0NrUEt6SGVJQ25ZNFJjY2NDMm8wR3JfMjJzQlh3SzlpcQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPTUZhTTJ5OXZzZjJtNmFDNTF5THFzSTRKeXJQemFEbUZoMndDSVd2UFp6V3N1QnFYRWhNejN5NW9GbkdhbTBpckRRMXc1eDZVenZWWV9tZUtYNnVoVExMWlBOTUFCcXVfeFBuMlNyV2NaaUdWOXZpUDJzNV93dGZMNlBaYlBRNHNWc3RqMUxBUVNkU19tV2tJ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNTXJqRWlqNkRWekQ3dkJteHJzSjRZZlZvTkJjU3FDQ0kwRzlaQWNqWXRqaVFPQzZJemVXajRrYVBaWUtrSUpVNHZuQjZFdjdNOWIwVUVpSzVpSnUwdF9SUXJXWnVwUjZMMTVrWWJ1WEg2STNjTDRkdTJuLWZ3SWYyQ2lrRDBObHphRUQxSU16M0c5WW9SVTlsWkVCYWNBUQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOUEZWaG9TQUdXRGViU3Q1Xy1BTllUa2w4RWtLcVl2bk1sREw1Y0xzMHNuTzZ6ZUdTT21zUlU2VkFSZUJKM0hDZFV4OVZkN3pOX0V4R3NCY0RlOXF4X1NlS2FZc2dmU0ZKeUJJakpJNktYOGpiSUU2VnJ0N2diUDQ4Z2d0YnZheUVSb3BnOGJUVWxZY0VWdk90RA?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOTjBfSnRtNzBqeHZxYUZ3SzZBcFhHMUhSMVFHbmdnX3ZuRHgtOHQwUlJZSTQtNEJESVNVcG54YmhydUZnY1h0dndiUXhud0c1OTNxM212emgxdTlhNy02THFMX1hNblVaT3hzTGZZUi1idjRXSlRFaHQxOXB6M3NmcUEtQnV1YlliekxHSFRPRWdJYzNSYlNmS0JraFY0YmkzZjJ2MUR0dTNsNGhFemtoOGRidHRVZ3lOM3hYM2lQLXkwRktj?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxQbGtJWXRlTkUxems2ckVtd1RmSTZGVW8zN0RBUGlSWGtLekdWVk9wWGlFcWt3MUNrcjJocEpUUkNxbE5RNy1TMDRKazhFbHpmWjR2WEVHNmRsZ3RJeXA4eFpubm9IUnRzZGRPd3FCbENoTTNpcXNidFpQSGZJY2VGUDlramhXalA3bWM5S1VhMDRfNENpUEkwWUZ6ekRUbVoxWGwxQ2lxT1dvcG5PZ1VOZ2tXNUFfSTdoMUZDYUY0bTJuWUFzRFdJT2NBNWU0QQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQQXZEeUdLVkFRYTNCeDNjQlQ4Wmc1bWdJSDdjYzV3RTZsY3o1S21jRVYxdkZKaVVlM19TMHhGaTVsSnVEVFVTaFNHcU9xbEhWaUxFNENjcm5TMjRMdkt0cXRFczJqcjdVRklTanRVVGp0dEYtWHpSZlQ3QXh1Q3BYQmpXYUdueVlRczNjR0pSSDVGa2VzRm95OGViV05OZw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPTmxSV0pmUGUxb3J2OGsxVkJYRzd6a3BSZk9sYmQzQ3c0cXNYUXBSLTZSQWIxY0k1al8wX0hGOGY5VWVOdVpseTkzX0tLb0VPUnBYQjc0ZHNDY1B0NWREWHRfLUxnVHZPVjVSamRRNmVIZF9ETkNTUlkyOU13OE91dXJSc3FyTk44SVZldUh1NFhKTzgzZGlXX3FGQm9xNDRKOXRvS0t3?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQa3BsVTlXaUtORjNLS1lEbENwQUdUdEQyVWRhcXVWcnRqOUJOMmg4dHRENXFhOWZUUEFWUTlka2YzLTFNaV9lQnJlZVhWeEwwdi13OUtMR2dHVWlQRTZPaWUzOGRfSWpnZGtQTGxWRFJRcXhLMlpKVDFnSW8yaVFCSmdreFNFb1Y3OHBZR1VzODZjNElRSDBHWA?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPelQ4bXZ4M3hOSWJyM3F1QnJzVmprUTVjQXc1cEEwTDN2R2lXcE05VzBQUlRIVXczSE1CclE5dW93MHZ2dEtsMXVUdHg2bmJTVVhQZWlkd2xxS0sweGc3S2dLQ1FXUlZqVVJ4NlFTbzdTMTJMYlZMSlRMcVhTYTNHenB1bFE0LTBRaWdrbkh0RTlFeDdpZnliSTZsbVptZ0NE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOeGdPZEtqTVoyV1hTUEhTSVhNOFBvd24tcFNjTldvVkR2THZvTlZtWjcyMlVTakRqYnhoSVk2SEZURDFaMUxnWXNNVnRxYTRIZTNNd2N4TTVENEJCdkEzS3BCUEpEZklYY3JTZVNZM3drQTJ6czR5OGdNUlJPUDdKeTBZOGo0RHpNQ09MSnlKX2JySTBKZnJn?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxPeFNCNzhFanV1OTduaTk2dkZ3VzcxSF9zcWl3NzJVdTIwUGNDLXZZMTNnVjA2S3A0eUpOQ1R1Qk1VS3dkbHpzaVBEQ1lMUUdhTExFUDFuRTEySGh1aGdzVXlWeGVrdy0ta1FDelc0NWVHal9GODJfdjJ0Qy1PMWJzQ3psLTNvZWJBWWJMdXVxdk9hZkFfVi1pLXpwdVFtU0pMZVRLalM0NlZnZlE4WUl2OXhXbGp5OWhtYUNiRjRuWVprQlNycjhlbTZQa21yZTV2bFVSY0hqWnVYU1k?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
