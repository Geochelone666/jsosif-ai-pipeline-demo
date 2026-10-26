# MCO Intelligence Report

- ticker: **MCO**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/MCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCO/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:33:00.623450+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 10, 'ai': 11, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 7 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-10-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 483.4500 |
| Return 1D (%) | -1.5477 |
| Return 1W (%) | -0.3340 |
| Return 1M (%) | 2.0260 |
| Return YTD (%) | -4.7319 |
| Return 1Y (%) | 1.7407 |
| Annualized volatility (%) | 28.1425 |
| Beta vs SPY | 0.5072 |
| Max drawdown (%) | -23.6059 |
| Sharpe (rf=0) | 0.2025 |
| Downside deviation (rf=0, %) | 20.2840 |
| Sortino (rf=0) | 0.2809 |
| Historical VaR 95% (1D, %) | 2.4795 |
| Historical ES 95% (1D, %) | 3.9599 |
| Correlation vs SPY | 0.2297 |
| Tracking error vs SPY (%) | 28.1010 |
| P/E (trailing) | 28.90 |
| P/B | 25.56 |
| EV/EBITDA | 22.10 |
| Revenue growth (%) | 0.80 |
| Forward P/E (estimate) | 25.87 |
| Gross margin (%) | 74.63 |
| Operating margin (%) | 46.27 |
| Return on equity (%) | 76.74 |
| Free cash flow yield (%) | 3.04 |
| MA50 | 477.8334 |
| Close vs MA50 (%) | 1.1754 |
| MA200 | 466.6500 |
| Close vs MA200 (%) | 3.6001 |
| RSI (14, Wilder) | 56.6347 |
| MACD (12,26) | 3.6965 |
| MACD signal (9) | 0.1271 |
| MACD histogram | 3.5694 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCO': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 483.4500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.5477 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.3340 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.0260 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -4.7319 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 1.7407 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.1425 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.2840 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2809 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4795 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9599 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2297 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.1010 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5072 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.6059 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2025 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.8734 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 46.2680 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 76.7410 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.0406 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 28.8972 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.6347 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 3.5694 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.1754 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.6001 -> Slightly above the moving-average trend level.

## TAILWINDS

### MCO Q3 deep dive: AI infrastructure and analytics drive segment divergence, guidance slightly raised
- Summary: MCO Q3 deep dive: AI infrastructure and analytics drive segment divergence, guidance slightly raised
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPbzRTU3FtbjBkTVg5WkZfT3pKR2RXNG9oOG1uQ0VycGFHcWp0WnRBYXZaTHdQQldCUGNpR1p0aDZoUUN2WXNKOXFQLW4yZ3dOcmVPcXVWSTI2YUpmLWQ4S2wwTFVKNTVPYXJiZGE3XzNXdXFZVGo1cmlNbUNpR3BRbWZaaHdCWlVJdXlB?oc=5>

### Moody's: 3 Key Takeaways for Long-Term Investors
- Summary: Highlights positive long‑term investment insights for Moody’s.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNN29Sa2dyX2pMQjY4VFJlSVRfenlhd1lhVTZ0N1VyM3BNT1dNTXo2bVYwSC1JcW5lYWhYcWs5UFJJcDB6LXczWVBpQ1VrbUZzQW5VR2I5TkppZTVUWDR2bHd3b1BXZmJNbWJkdkhSM25ONmJNT0dIY2ZrWkVMYkFRMmc3YlZsUUxTa0ozNjVBcFl0M0dpOEhr?oc=5>

### Moody’s (MCO): Can Private Credit Create a Durable Subscription Business?
- Summary: Explores potential growth from private credit subscription model.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPYklUc2g0VWpBV21VTVA1N1h6Y1BOWmdwM3cxX1dFT1k3enltbnZmTVFaaTBEN04zUGlnQkZrc1BrUzl1WE9haEV5RFJwaU9xc29oYmhDNU1JSkg2S3ZrLVJTcU5KVENKekdlc2dJUHVFYXppMTEzOW51TC1tNXFXRnd6QTdKcGpNaFZfdDZ0ZHRDVVRva3RjMTk3dVE?oc=5>

### Moody's (NYSE:MCO) Stock Forecast & Analyst Predictions
- Summary: Analysts provide a forecast for MCO stock, offering insight into future performance.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxOem9wWWxzM0VxUXlSM1dsNl9sTUFwTHdKcDRTRXl1MDZId0VadW5CRUFzTWhLOXZ1LXFYVnJicnVMN1JFNFZ1czgxZ1JTVjJ6aDdpc3Rfa0MxajVOSk5jOWJtTGZBVlFnQ3Z3V3I4NDQ2R0Fyak9zU0NUdW1zaVdJTUFDZw?oc=5>

### Revenue rose 1% at Moody’s (MCO), while earnings per share grew faster.
- Summary: MCO reported a 1% revenue increase and faster EPS growth, indicating solid earnings performance.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOTUl6UTk5bmVfelktYUl4NTJ5UlpRNlhmNmNlbGJRN0JQSlRFVmU2R1ZyNVFyMUNlNmVGeDgwc2VReDNvc2tIbnpqOGVFdkhBeDB0Tjc3VXFQX2xhamhLVU9scnB3bURraXNZMTVPTktNaV8xVXp0MjBfMmJNR0I0S3hCVmRDdlRIaDdfZEktWm8zMGh2V05lUEUtMG5TeHdrN2E0bg?oc=5>

### Moody's Corporation $MCO Stock: Retail Employees Superannuation Pty Ltd as trustee for Retail Employees Superannuation Trust Grows Stake
- Summary: A trustee increased its stake in MCO, signaling confidence in the company.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwJBVV95cUxOR3VqLUxxYk9OQm5nenE1WkJVZUFXZDhMZ0ExTkRhSlliNi00d214WTF6cGItRkJTejRDUEQ5V3hBQzJWRkJRREVSbEtxS3F4dGdjc3diTWowZC1fOVJVSGpnX1E3T0M5S3QwTThNTWRJcVU4NzNmaFZyWXM1RmVobDlPWG1JbDlaTFdRNWZZVDA4dFduR1NVVUloSEZodkxvM1RFMXhqZ2JaWUZ1eWk0RVdDb1UwTzBLRVMwUkx0Z0NjRUNTeFBoMURqLUVkbVZWVWlrSl9uN1pxeHEzdUZaV29qVC1JdWZKZlExbGF1cE5wY19qdm5Oek9OOXBQTXoxalhhWXRQYnV6SWFZcEpKc3VGb1VQTzVjMTZHb1daUQ?oc=5>

## HEADWINDS

### Moody’s Shares Decline Nearly 3% as Third-Quarter Earnings and Revenue Miss Estimates
- Summary: Moody’s Shares Decline Nearly 3% as Third-Quarter Earnings and Revenue Miss Estimates
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNZ3FnQlhEYk92QUxZYWVUMm5zWXdYeFhjZHM0c2MtOXk4bzZkWFVieW9yeGFCRE10cm5DTEZUdmFrRzFieUNQNmNseEtsWnViYnlYektPWnhUWkE1cGgzbUw4MGppb0JPLTh6Wno1T1BsNVZ3djRSUDhmRTA3ZUZ1UlpZZU5pNUlZR0tmSndCUGF3UmYxZDFYRld3?oc=5>

### Moody's stock dips after Q3's double-miss, guidance disappoints (MCO:NYSE)
- Summary: Stock fell after earnings miss and weak guidance.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNaEpjZDc2NWVqazNVeEZQSGtWU1dVeTJOWmpncHVGb1k2M2xOZm5oMEg4bkc3bkdJUjZGeDYxR3d3TWxHcDFFYi0xT1BENXk3MDFzTThvVG02Ym1BR3o1bk9mMW5SRUgwUy00d3hfTTd2MWh4ZkE4T052Rkh3VmZrR2lKalZuaTFBS0hDci1Yc0VSMjBSZEJFY1JNT002cEE?oc=5>

### MCO Q3 Earnings Miss Estimates as Costs Rise & MIS Revenues Fall
- Summary: Earnings fell short of estimates amid rising costs and lower MIS revenue.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNWUZKdDZYa0ZBWlpmNC0wY3E2d1R2TC1ub2JRRWVHcEhuVmhVTnN6ekpvX2s1NDJRZzVTXzBHS0hQc1RlODRPNzNyYWVudGVNOUdoMUkyX08xWVB0SWxldTVmTGlTTWtmdjJMNjFNNXVIWnVLQ1lrN3RKUk1NQVk4MnR6ZWY0M3JFY01GOXFhbnljVjV2QzlIc2Z4OS1EMHRLMGphZTJIY3dZS2ZUTlM3Q21XckROTnd2YXc?oc=5>

### Moody's: Q3 Earnings Emphasize Detached Valuation (NYSE:MCO)
- Summary: Earnings highlighted valuation concerns, signaling potential downside.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPU3FIdVhRM1BuN3psR3R0eVRHMXJhT2g0dk9oTV94NWhTMW5xREcybzhDa3pVT1JOZFZibEJWX1pGeF9HMk01bV9rQ1I1dVA0RG8zTHRpNXBuZGR6WjlUb0lDM2hSTEdONHJzQjhJTGgzUWxIeVM1aVdUZmpjUVBjZ0ZmVmdZVHBhMGd4QlR6d2tBdw?oc=5>

### Moody's (MCO) Shares Dip After Q3 Miss, Despite Maintaining 2026 EPS Guidance
- Summary: Share price fell after Q3 earnings miss.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNT2NpQkJXMERYQnh0YWI3djVHeEUxSy1EMk5EVDdldWFvLWk2Vm9JNU14dk9CdExwMXgxaFh4bzdDYjNVX1NNRnJUeWVuai1pN2hUYjhydXVjWWZ0QnNybmp5SXdlQ0FWakZFQjZ6UGVxNDNWN1RFYUUyX2NoeGJEMDhIXzlfWUZvWEprTVMyT3lqRU9zdUY0cVVSZzl5UVd2ZzlBekJmWVlPOG5EdEZqbWpn?oc=5>

### Stifel Nicolaus Issues Pessimistic Forecast for Moody's (NYSE:MCO) Stock Price
- Summary: Stifel Nicolaus released a pessimistic forecast, potentially dampening investor sentiment.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxPWm9YbGdPV19ITUkxcjQ2NDQ0ZGNRZ3RGemxmMnloNVJlenh4YjgxMHpwTWY3WXUwaG1yNGE2TjItZXhlTVBCQ2Z3b1QtMlBBdnRVM25mMm1ZZzItT2lrSDAzVmdrZWxaNF9wUDVGQUNoaFZERnhYQVVJZXdhbzBQellkQzkzWmJUbHVaZFNrcDFJWG5OSHNLRUFQYnNneU9ZbzJ0M3pwUXlFTFRfbDlDNlZ6X2tQVmxiREF4SnlmRFF5T0FsclJob0V3eUJOVnp4YWs0?oc=5>

### 2,155 Moody's Corporation $MCO Shares Sold by Bank Pictet & Cie Europe AG
- Summary: Bank Pictet sold 2,155 MCO shares, possibly indicating a short-term sell pressure.
- Date: 2026-10-20 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxQcXpUWmlQaVl4aE1qQXlRLXBsMXloSUdFazFUOEVWNWdFRVM5ZWtObFM5NDljQWRyaVYyVVV5WnpPYnJDM2tWZV9DNmtqWUVzbWxoS2pMUGhTWUpkRHpZRHFibjNqQm40dTRTak9tNUd1dlNwc2VHN3I1ekNMNmFMQWV4eW9HclRMemxnZjY5ME5zUkxOaWV4NFA4c3Viczc0X3lwWEhNLUFTVFZDSEI2bm9CdExSaWFPWDlXenFrNndHT29qT3lXeg?oc=5>

## CATALYSTS

### Moody's Corporation $MCO Stock Bought by Norris Perne & French LLP MI
- Summary: Moody's Corporation $MCO Stock Bought by Norris Perne & French LLP MI
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOQk9UUnltYnFpRnlQQ1UtbWY2LWlIc2lCNHFGTGF0eHQ1SjZtWlQyMnhfWnpNMGtOQzNaRzdyWHNMT2FqTkhPVWNBYXRUMjFXQjc3LWRwS0lpaHZVNTdoV1pLZTNkcHBELUNJN1hXeVdBZnp1WDNVUlctM01uQ3dMNUo4OGNuWVY1TFZFbng4cWxoWHlxRWNvRENGYm9uSWlPZ3pBS2t1LVJRYlRaVVN4cjFZRWU2WDJ1WV85OExicUlGTVBr?oc=5>

### Moody's Corporation (NYSE:MCO) Stock Now Rated "Moderate Buy" by Sell-Side Analysts
- Summary: Moody's Corporation (NYSE:MCO) Stock Now Rated "Moderate Buy" by Sell-Side Analysts
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxPcmFSWEJnUDZ4aHRjeUNIazhGNWlQYUQxMEU2Sjc4VGNrY3NBenVEWUdUWXc2NTVYeVVrNWNSN0dlZWg2eFM5cWo2eXhYd1FtOEF4LW1RSWluSGpIWXlyemVPQ3k4eFNPYVFGb2JKa3RMQTJpLXBTMHpFN3gzTG8zb0RjamN1YXFwN1NCOVBWdENMS2ROZ1BpYXhLbFpmc2hrVVFqRmpCcEZDMkEwcnZlVkIzRjNibUJEZWNzXy0wLUdCbVY4TWZ3anktdUp1enpDek9SaVZaUW9wZw?oc=5>

### Moody's Corporation 2026 Q3 - Results - Earnings Call Presentation (NYSE:MCO) 2026-10-21
- Summary: Moody's Corporation 2026 Q3 - Results - Earnings Call Presentation (NYSE:MCO) 2026-10-21
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOM0cxVlhITUo1MmZ0VWdTSEIxM0dSOXJfX1N2Q20tYkdfcHVNaFZ3U21Ca2xnN2hZOFFjdXR5NWVCdTRGZk42a2J2ak96OEp3MjRnUlBES3d4T014dUdTZmxQRWIyc0xOZWpYWGdxUUl0SExuNDZLMkhZc1JXRHozdHZlMGZ1U0p3TFZicnVaelVrdGFFWVdfbDhkQ2JoQmZfLVMwZQ?oc=5>

### Moody's Corporation $MCO Stock Sold by Canoe Financial LP
- Summary: Moody's Corporation $MCO Stock Sold by Canoe Financial LP
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNREV4Zk56cWV2ekpaWTk1TzNlTW9SaTJLZV83dkt3Q19NV0NMLXdZdGZzMURqT1haU0xrNzlyZVRLSmhUVWJZYXlrZ2pjR3dzWEhJRF8wM3BxRjhabS1qT3hHZmxZYW15TXV2Yk5tWEd5TE12Y2hISlp6alc0VjhWWGFjVzd3ODN5ZWM4YmpVTDBlaUlNTkY1elpRRTdOSXVzMHBqMHNPNkloZjJrcGpyZUFnb0Y3dnM?oc=5>

### Moody's Corporation $MCO Shares Sold by Robeco Institutional Asset Management B.V.
- Summary: Moody's Corporation $MCO Shares Sold by Robeco Institutional Asset Management B.V.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNcEFhQzgwYW9NdkZWZnZkMjFvUVdkUHVBU2JFVWdzZG01SjN2RkRrTkVPQ1Q4bUlVZWEtb1ZuYXp5NlN2V21OenpoQjZ4NDJMRXdKRnIxZjl5SWZzMnRNbTJ5RnVuMEF0UkFMbUV4bGs1UjN5N3pVNkU4TlNtZlFqenlTN1pjeHpQT2djR2RaVjRIbkQxYjEycDQyQTNueGNyWEs0ZjNVT28zamxEcm9qSGcyZkVnQTNvUjRpdmhRcXhOZTZrV2ZRMnluc0h2UTdyU2cyaUN3?oc=5>

### Moody's Corporation $MCO Stock Sold by Baskin Financial Services Inc.
- Summary: Moody's Corporation $MCO Stock Sold by Baskin Financial Services Inc.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxOWWtBSnNFbEg3VThaT2JXTm9zMkoxbXRHNy1IQXBSQnE4UFlwRXhoM2ZuVXgtNXRrZXBJVmpQdUdSRGhIRF81RGpkY2d3ZC1PQTB3bmUxWV9ia1NvS1VJMEx6c2o1SU9lTEI0OUh6Nk55bzBiZzg4MGZSZFllU3BhYm9kUTZ2QzAtOGhEVkQ4aVo5dWM2WnZmN1dhVGFhSFhwY1c1Qko5dWdHRXU1dWtaS1ZVYzlkNXUyeFpfOU1EeVJ6Si0yNnc?oc=5>

### Moody's Corporation (NYSE:MCO) Shareholders Set to Receive $1.03 Quarterly Dividend
- Summary: Moody's Corporation (NYSE:MCO) Shareholders Set to Receive $1.03 Quarterly Dividend
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxQc2YzTFRIMnZpMUQwdUZKOUtEQm1MTE15OE1HR2VvYmpxMnlzTl85R0ViQTNSQlJtTTUwOWpwbjRMZUFKUDdrWWliX1JJWVpjZ0c1ODlmR012WGZyaU9hc0djYXZ1aEtqRlpiZ2NhV2dkV2NZTE95bUdPUGUxTmk2RGUyVi1rM2NJR0Y2bzdHcVVGVXo4eHRRVGhlOHBYWjhCWnVvcUg4M0ZDM3hvcU5DaXg1ZkxVR2dFZkhkZXAxOHhsUDRTbWZ0b203MXdCdUl3VURTdFV4RFQ?oc=5>

### Moody's Corporation $MCO Stock: Assenagon Asset Management S.A. Lowers Holdings
- Summary: Moody's Corporation $MCO Stock: Assenagon Asset Management S.A. Lowers Holdings
- Date: 2026-10-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxQOXBWVVVQSVQ4dUZxTnVBMWxBalRVR01NbkdrekhaejEwSFNwcGZaNVcxb05Kejc0YndhQVByU3pZbm8wVFpkYkVHTlVfZjF5Y3RqSXp2WVpyWUJCcjg0MDdwZWJSeVJjQTRhVlNNUDRyWGZ5c1RSemZqbFpLRU9tS29oZnMwXzlSeXc2UWF1anJma19NOEdIUEc0ZmczVDhkSEsxTWRIV05CbTBfSFFiRkl1bzNuOF8zQWlnRHZxcmNMMUhUQlVRajBwbFFxY3dV?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCO** | **28.90** | **25.56** | **22.10** | **0.80** | **83,358,425,088.00 USD** | **1.74** |
| SPGI | 27.41 | 4.21 | 18.36 | 10.40 | 132,751,384,576.00 USD | -0.52 |
| MSCI | 31.73 | -14.72 | 25.09 | 12.40 | 44,755,574,784.00 USD | 15.91 |
| FDS | 22.74 | 5.84 | 14.39 | 6.30 | 11,783,576,576.00 USD | 17.58 |

Peers fetched as_of: 2026-10-25; MCO reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-02-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 1,142,100,000.00 USD; period 2019-01-01/2019-03-31; fiscal year/reporting period 2019/Q1
- Net income (latest available single quarter): 734,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1059556/000162828026066731/mco-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPbzRTU3FtbjBkTVg5WkZfT3pKR2RXNG9oOG1uQ0VycGFHcWp0WnRBYXZaTHdQQldCUGNpR1p0aDZoUUN2WXNKOXFQLW4yZ3dOcmVPcXVWSTI2YUpmLWQ4S2wwTFVKNTVPYXJiZGE3XzNXdXFZVGo1cmlNbUNpR3BRbWZaaHdCWlVJdXlB?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNN29Sa2dyX2pMQjY4VFJlSVRfenlhd1lhVTZ0N1VyM3BNT1dNTXo2bVYwSC1JcW5lYWhYcWs5UFJJcDB6LXczWVBpQ1VrbUZzQW5VR2I5TkppZTVUWDR2bHd3b1BXZmJNbWJkdkhSM25ONmJNT0dIY2ZrWkVMYkFRMmc3YlZsUUxTa0ozNjVBcFl0M0dpOEhr?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPYklUc2g0VWpBV21VTVA1N1h6Y1BOWmdwM3cxX1dFT1k3enltbnZmTVFaaTBEN04zUGlnQkZrc1BrUzl1WE9haEV5RFJwaU9xc29oYmhDNU1JSkg2S3ZrLVJTcU5KVENKekdlc2dJUHVFYXppMTEzOW51TC1tNXFXRnd6QTdKcGpNaFZfdDZ0ZHRDVVRva3RjMTk3dVE?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxOem9wWWxzM0VxUXlSM1dsNl9sTUFwTHdKcDRTRXl1MDZId0VadW5CRUFzTWhLOXZ1LXFYVnJicnVMN1JFNFZ1czgxZ1JTVjJ6aDdpc3Rfa0MxajVOSk5jOWJtTGZBVlFnQ3Z3V3I4NDQ2R0Fyak9zU0NUdW1zaVdJTUFDZw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOTUl6UTk5bmVfelktYUl4NTJ5UlpRNlhmNmNlbGJRN0JQSlRFVmU2R1ZyNVFyMUNlNmVGeDgwc2VReDNvc2tIbnpqOGVFdkhBeDB0Tjc3VXFQX2xhamhLVU9scnB3bURraXNZMTVPTktNaV8xVXp0MjBfMmJNR0I0S3hCVmRDdlRIaDdfZEktWm8zMGh2V05lUEUtMG5TeHdrN2E0bg?oc=5
- https://news.google.com/rss/articles/CBMinwJBVV95cUxOR3VqLUxxYk9OQm5nenE1WkJVZUFXZDhMZ0ExTkRhSlliNi00d214WTF6cGItRkJTejRDUEQ5V3hBQzJWRkJRREVSbEtxS3F4dGdjc3diTWowZC1fOVJVSGpnX1E3T0M5S3QwTThNTWRJcVU4NzNmaFZyWXM1RmVobDlPWG1JbDlaTFdRNWZZVDA4dFduR1NVVUloSEZodkxvM1RFMXhqZ2JaWUZ1eWk0RVdDb1UwTzBLRVMwUkx0Z0NjRUNTeFBoMURqLUVkbVZWVWlrSl9uN1pxeHEzdUZaV29qVC1JdWZKZlExbGF1cE5wY19qdm5Oek9OOXBQTXoxalhhWXRQYnV6SWFZcEpKc3VGb1VQTzVjMTZHb1daUQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNZ3FnQlhEYk92QUxZYWVUMm5zWXdYeFhjZHM0c2MtOXk4bzZkWFVieW9yeGFCRE10cm5DTEZUdmFrRzFieUNQNmNseEtsWnViYnlYektPWnhUWkE1cGgzbUw4MGppb0JPLTh6Wno1T1BsNVZ3djRSUDhmRTA3ZUZ1UlpZZU5pNUlZR0tmSndCUGF3UmYxZDFYRld3?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNaEpjZDc2NWVqazNVeEZQSGtWU1dVeTJOWmpncHVGb1k2M2xOZm5oMEg4bkc3bkdJUjZGeDYxR3d3TWxHcDFFYi0xT1BENXk3MDFzTThvVG02Ym1BR3o1bk9mMW5SRUgwUy00d3hfTTd2MWh4ZkE4T052Rkh3VmZrR2lKalZuaTFBS0hDci1Yc0VSMjBSZEJFY1JNT002cEE?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNWUZKdDZYa0ZBWlpmNC0wY3E2d1R2TC1ub2JRRWVHcEhuVmhVTnN6ekpvX2s1NDJRZzVTXzBHS0hQc1RlODRPNzNyYWVudGVNOUdoMUkyX08xWVB0SWxldTVmTGlTTWtmdjJMNjFNNXVIWnVLQ1lrN3RKUk1NQVk4MnR6ZWY0M3JFY01GOXFhbnljVjV2QzlIc2Z4OS1EMHRLMGphZTJIY3dZS2ZUTlM3Q21XckROTnd2YXc?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPU3FIdVhRM1BuN3psR3R0eVRHMXJhT2g0dk9oTV94NWhTMW5xREcybzhDa3pVT1JOZFZibEJWX1pGeF9HMk01bV9rQ1I1dVA0RG8zTHRpNXBuZGR6WjlUb0lDM2hSTEdONHJzQjhJTGgzUWxIeVM1aVdUZmpjUVBjZ0ZmVmdZVHBhMGd4QlR6d2tBdw?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNT2NpQkJXMERYQnh0YWI3djVHeEUxSy1EMk5EVDdldWFvLWk2Vm9JNU14dk9CdExwMXgxaFh4bzdDYjNVX1NNRnJUeWVuai1pN2hUYjhydXVjWWZ0QnNybmp5SXdlQ0FWakZFQjZ6UGVxNDNWN1RFYUUyX2NoeGJEMDhIXzlfWUZvWEprTVMyT3lqRU9zdUY0cVVSZzl5UVd2ZzlBekJmWVlPOG5EdEZqbWpn?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxPWm9YbGdPV19ITUkxcjQ2NDQ0ZGNRZ3RGemxmMnloNVJlenh4YjgxMHpwTWY3WXUwaG1yNGE2TjItZXhlTVBCQ2Z3b1QtMlBBdnRVM25mMm1ZZzItT2lrSDAzVmdrZWxaNF9wUDVGQUNoaFZERnhYQVVJZXdhbzBQellkQzkzWmJUbHVaZFNrcDFJWG5OSHNLRUFQYnNneU9ZbzJ0M3pwUXlFTFRfbDlDNlZ6X2tQVmxiREF4SnlmRFF5T0FsclJob0V3eUJOVnp4YWs0?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxQcXpUWmlQaVl4aE1qQXlRLXBsMXloSUdFazFUOEVWNWdFRVM5ZWtObFM5NDljQWRyaVYyVVV5WnpPYnJDM2tWZV9DNmtqWUVzbWxoS2pMUGhTWUpkRHpZRHFibjNqQm40dTRTak9tNUd1dlNwc2VHN3I1ekNMNmFMQWV4eW9HclRMemxnZjY5ME5zUkxOaWV4NFA4c3Viczc0X3lwWEhNLUFTVFZDSEI2bm9CdExSaWFPWDlXenFrNndHT29qT3lXeg?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOQk9UUnltYnFpRnlQQ1UtbWY2LWlIc2lCNHFGTGF0eHQ1SjZtWlQyMnhfWnpNMGtOQzNaRzdyWHNMT2FqTkhPVWNBYXRUMjFXQjc3LWRwS0lpaHZVNTdoV1pLZTNkcHBELUNJN1hXeVdBZnp1WDNVUlctM01uQ3dMNUo4OGNuWVY1TFZFbng4cWxoWHlxRWNvRENGYm9uSWlPZ3pBS2t1LVJRYlRaVVN4cjFZRWU2WDJ1WV85OExicUlGTVBr?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxPcmFSWEJnUDZ4aHRjeUNIazhGNWlQYUQxMEU2Sjc4VGNrY3NBenVEWUdUWXc2NTVYeVVrNWNSN0dlZWg2eFM5cWo2eXhYd1FtOEF4LW1RSWluSGpIWXlyemVPQ3k4eFNPYVFGb2JKa3RMQTJpLXBTMHpFN3gzTG8zb0RjamN1YXFwN1NCOVBWdENMS2ROZ1BpYXhLbFpmc2hrVVFqRmpCcEZDMkEwcnZlVkIzRjNibUJEZWNzXy0wLUdCbVY4TWZ3anktdUp1enpDek9SaVZaUW9wZw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOM0cxVlhITUo1MmZ0VWdTSEIxM0dSOXJfX1N2Q20tYkdfcHVNaFZ3U21Ca2xnN2hZOFFjdXR5NWVCdTRGZk42a2J2ak96OEp3MjRnUlBES3d4T014dUdTZmxQRWIyc0xOZWpYWGdxUUl0SExuNDZLMkhZc1JXRHozdHZlMGZ1U0p3TFZicnVaelVrdGFFWVdfbDhkQ2JoQmZfLVMwZQ?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNREV4Zk56cWV2ekpaWTk1TzNlTW9SaTJLZV83dkt3Q19NV0NMLXdZdGZzMURqT1haU0xrNzlyZVRLSmhUVWJZYXlrZ2pjR3dzWEhJRF8wM3BxRjhabS1qT3hHZmxZYW15TXV2Yk5tWEd5TE12Y2hISlp6alc0VjhWWGFjVzd3ODN5ZWM4YmpVTDBlaUlNTkY1elpRRTdOSXVzMHBqMHNPNkloZjJrcGpyZUFnb0Y3dnM?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNcEFhQzgwYW9NdkZWZnZkMjFvUVdkUHVBU2JFVWdzZG01SjN2RkRrTkVPQ1Q4bUlVZWEtb1ZuYXp5NlN2V21OenpoQjZ4NDJMRXdKRnIxZjl5SWZzMnRNbTJ5RnVuMEF0UkFMbUV4bGs1UjN5N3pVNkU4TlNtZlFqenlTN1pjeHpQT2djR2RaVjRIbkQxYjEycDQyQTNueGNyWEs0ZjNVT28zamxEcm9qSGcyZkVnQTNvUjRpdmhRcXhOZTZrV2ZRMnluc0h2UTdyU2cyaUN3?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOWWtBSnNFbEg3VThaT2JXTm9zMkoxbXRHNy1IQXBSQnE4UFlwRXhoM2ZuVXgtNXRrZXBJVmpQdUdSRGhIRF81RGpkY2d3ZC1PQTB3bmUxWV9ia1NvS1VJMEx6c2o1SU9lTEI0OUh6Nk55bzBiZzg4MGZSZFllU3BhYm9kUTZ2QzAtOGhEVkQ4aVo5dWM2WnZmN1dhVGFhSFhwY1c1Qko5dWdHRXU1dWtaS1ZVYzlkNXUyeFpfOU1EeVJ6Si0yNnc?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxQc2YzTFRIMnZpMUQwdUZKOUtEQm1MTE15OE1HR2VvYmpxMnlzTl85R0ViQTNSQlJtTTUwOWpwbjRMZUFKUDdrWWliX1JJWVpjZ0c1ODlmR012WGZyaU9hc0djYXZ1aEtqRlpiZ2NhV2dkV2NZTE95bUdPUGUxTmk2RGUyVi1rM2NJR0Y2bzdHcVVGVXo4eHRRVGhlOHBYWjhCWnVvcUg4M0ZDM3hvcU5DaXg1ZkxVR2dFZkhkZXAxOHhsUDRTbWZ0b203MXdCdUl3VURTdFV4RFQ?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxQOXBWVVVQSVQ4dUZxTnVBMWxBalRVR01NbkdrekhaejEwSFNwcGZaNVcxb05Kejc0YndhQVByU3pZbm8wVFpkYkVHTlVfZjF5Y3RqSXp2WVpyWUJCcjg0MDdwZWJSeVJjQTRhVlNNUDRyWGZ5c1RSemZqbFpLRU9tS29oZnMwXzlSeXc2UWF1anJma19NOEdIUEc0ZmczVDhkSEsxTWRIV05CbTBfSFFiRkl1bzNuOF8zQWlnRHZxcmNMMUhUQlVRajBwbFFxY3dV?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
