# MCO Intelligence Report

- ticker: **MCO**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/MCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCO/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:20:44.629831+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 8, 'ai': 10, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/MCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 9 named publishers; 0 exact duplicates; 21 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 477.2700 |
| Return 1D (%) | 0.6899 |
| Return 1W (%) | -0.7858 |
| Return 1M (%) | 3.7363 |
| Return YTD (%) | -5.9497 |
| Return 1Y (%) | -1.9053 |
| Annualized volatility (%) | 28.1066 |
| Beta vs SPY | 0.4897 |
| Max drawdown (%) | -23.6059 |
| Sharpe (rf=0) | 0.0720 |
| Downside deviation (rf=0, %) | 20.3801 |
| Sortino (rf=0) | 0.0993 |
| Historical VaR 95% (1D, %) | 2.4795 |
| Historical ES 95% (1D, %) | 3.9599 |
| Correlation vs SPY | 0.2213 |
| Tracking error vs SPY (%) | 28.1656 |
| P/E (trailing) | 28.53 |
| P/B | 25.24 |
| EV/EBITDA | 21.84 |
| Revenue growth (%) | 0.80 |
| Forward P/E (estimate) | 25.54 |
| Gross margin (%) | 74.63 |
| Operating margin (%) | 46.27 |
| Return on equity (%) | 76.74 |
| Free cash flow yield (%) | 3.08 |
| MA50 | 477.5894 |
| Close vs MA50 (%) | -0.0669 |
| MA200 | 465.8921 |
| Close vs MA200 (%) | 2.4422 |
| RSI (14, Wilder) | 52.2523 |
| MACD (12,26) | 3.2539 |
| MACD signal (9) | 1.7958 |
| MACD histogram | 1.4581 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCO': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 477.2700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.6899 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.7858 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.7363 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.9497 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -1.9053 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.1066 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.3801 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.0993 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4795 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9599 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2213 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.1656 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4897 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.6059 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0720 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.5426 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 46.2680 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 76.7410 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.0800 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 28.5278 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 52.2523 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.4581 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.0669 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 2.4422 -> Slightly above the moving-average trend level.

## TAILWINDS

### MCO Q3 deep dive: AI infrastructure and analytics drive segment divergence, guidance slightly raised
- Summary: MCO Q3 deep dive: AI infrastructure and analytics drive segment divergence, guidance slightly raised
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPbzRTU3FtbjBkTVg5WkZfT3pKR2RXNG9oOG1uQ0VycGFHcWp0WnRBYXZaTHdQQldCUGNpR1p0aDZoUUN2WXNKOXFQLW4yZ3dOcmVPcXVWSTI2YUpmLWQ4S2wwTFVKNTVPYXJiZGE3XzNXdXFZVGo1cmlNbUNpR3BRbWZaaHdCWlVJdXlB?oc=5>

### How Moody’s Corporation (MCO) Is Benefiting from the AI Infrastructure Boom?
- Summary: Moody's gains from AI infrastructure growth, enhancing services and revenue potential.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOYlgya3hNV1VLcWRmbEFTbmhEUG1Zb2I5bXJjc3NqUi1XVWw0ZVREaUI1ajJySk0xaUhSTE9IdXhtUUdaNzJvZkR0cU80TWMtOGZSM2pxSDFrb1lfaDBVaWRDMnhlZDFWMXJqeGxJbG54VG9nZFRCTFNEQ1F0VHo1S2xjSXMxX20xRjVJU3dfNjZzLUtzYmE1TG9fYTBEMG1NMWc?oc=5>

## HEADWINDS

### Moody’s Shares Decline Nearly 3% as Third-Quarter Earnings and Revenue Miss Estimates
- Summary: Moody’s Shares Decline Nearly 3% as Third-Quarter Earnings and Revenue Miss Estimates
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNZ3FnQlhEYk92QUxZYWVUMm5zWXdYeFhjZHM0c2MtOXk4bzZkWFVieW9yeGFCRE10cm5DTEZUdmFrRzFieUNQNmNseEtsWnViYnlYektPWnhUWkE1cGgzbUw4MGppb0JPLTh6Wno1T1BsNVZ3djRSUDhmRTA3ZUZ1UlpZZU5pNUlZR0tmSndCUGF3UmYxZDFYRld3?oc=5>

### Moody's stock dips after Q3's double-miss, guidance disappoints (MCO:NYSE)
- Summary: Stock fell after earnings miss and weak guidance.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNaEpjZDc2NWVqazNVeEZQSGtWU1dVeTJOWmpncHVGb1k2M2xOZm5oMEg4bkc3bkdJUjZGeDYxR3d3TWxHcDFFYi0xT1BENXk3MDFzTThvVG02Ym1BR3o1bk9mMW5SRUgwUy00d3hfTTd2MWh4ZkE4T052Rkh3VmZrR2lKalZuaTFBS0hDci1Yc0VSMjBSZEJFY1JNT002cEE?oc=5>

### Moody's: Q3 Earnings Emphasize Detached Valuation (NYSE:MCO)
- Summary: Earnings highlighted valuation concerns, signaling potential downside.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPU3FIdVhRM1BuN3psR3R0eVRHMXJhT2g0dk9oTV94NWhTMW5xREcybzhDa3pVT1JOZFZibEJWX1pGeF9HMk01bV9rQ1I1dVA0RG8zTHRpNXBuZGR6WjlUb0lDM2hSTEdONHJzQjhJTGgzUWxIeVM1aVdUZmpjUVBjZ0ZmVmdZVHBhMGd4QlR6d2tBdw?oc=5>

### Moody's (MCO) Shares Dip After Q3 Miss, Despite Maintaining 2026 EPS Guidance
- Summary: Share price fell after Q3 earnings miss.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNT2NpQkJXMERYQnh0YWI3djVHeEUxSy1EMk5EVDdldWFvLWk2Vm9JNU14dk9CdExwMXgxaFh4bzdDYjNVX1NNRnJUeWVuai1pN2hUYjhydXVjWWZ0QnNybmp5SXdlQ0FWakZFQjZ6UGVxNDNWN1RFYUUyX2NoeGJEMDhIXzlfWUZvWEprTVMyT3lqRU9zdUY0cVVSZzl5UVd2ZzlBekJmWVlPOG5EdEZqbWpn?oc=5>

### Stifel Nicolaus Issues Pessimistic Forecast for Moody's (NYSE:MCO) Stock Price
- Summary: Stifel Nicolaus issued a negative forecast for MCO stock, potentially dampening investor sentiment.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxPWm9YbGdPV19ITUkxcjQ2NDQ0ZGNRZ3RGemxmMnloNVJlenh4YjgxMHpwTWY3WXUwaG1yNGE2TjItZXhlTVBCQ2Z3b1QtMlBBdnRVM25mMm1ZZzItT2lrSDAzVmdrZWxaNF9wUDVGQUNoaFZERnhYQVVJZXdhbzBQellkQzkzWmJUbHVaZFNrcDFJWG5OSHNLRUFQYnNneU9ZbzJ0M3pwUXlFTFRfbDlDNlZ6X2tQVmxiREF4SnlmRFF5T0FsclJob0V3eUJOVnp4YWs0?oc=5>

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

### Moody's Corporation $MCO Shares Sold by Robeco Institutional Asset Management B.V.
- Summary: Moody's Corporation $MCO Shares Sold by Robeco Institutional Asset Management B.V.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNcEFhQzgwYW9NdkZWZnZkMjFvUVdkUHVBU2JFVWdzZG01SjN2RkRrTkVPQ1Q4bUlVZWEtb1ZuYXp5NlN2V21OenpoQjZ4NDJMRXdKRnIxZjl5SWZzMnRNbTJ5RnVuMEF0UkFMbUV4bGs1UjN5N3pVNkU4TlNtZlFqenlTN1pjeHpQT2djR2RaVjRIbkQxYjEycDQyQTNueGNyWEs0ZjNVT28zamxEcm9qSGcyZkVnQTNvUjRpdmhRcXhOZTZrV2ZRMnluc0h2UTdyU2cyaUN3?oc=5>

### Moody's Corporation $MCO Stock Sold by Canoe Financial LP
- Summary: Moody's Corporation $MCO Stock Sold by Canoe Financial LP
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNREV4Zk56cWV2ekpaWTk1TzNlTW9SaTJLZV83dkt3Q19NV0NMLXdZdGZzMURqT1haU0xrNzlyZVRLSmhUVWJZYXlrZ2pjR3dzWEhJRF8wM3BxRjhabS1qT3hHZmxZYW15TXV2Yk5tWEd5TE12Y2hISlp6alc0VjhWWGFjVzd3ODN5ZWM4YmpVTDBlaUlNTkY1elpRRTdOSXVzMHBqMHNPNkloZjJrcGpyZUFnb0Y3dnM?oc=5>

### Moody's Corporation (NYSE:MCO) Shareholders Set to Receive $1.03 Quarterly Dividend
- Summary: Moody's Corporation (NYSE:MCO) Shareholders Set to Receive $1.03 Quarterly Dividend
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxQc2YzTFRIMnZpMUQwdUZKOUtEQm1MTE15OE1HR2VvYmpxMnlzTl85R0ViQTNSQlJtTTUwOWpwbjRMZUFKUDdrWWliX1JJWVpjZ0c1ODlmR012WGZyaU9hc0djYXZ1aEtqRlpiZ2NhV2dkV2NZTE95bUdPUGUxTmk2RGUyVi1rM2NJR0Y2bzdHcVVGVXo4eHRRVGhlOHBYWjhCWnVvcUg4M0ZDM3hvcU5DaXg1ZkxVR2dFZkhkZXAxOHhsUDRTbWZ0b203MXdCdUl3VURTdFV4RFQ?oc=5>

### Moody's: Q3 Earnings Snapshot
- Summary: Moody’s releases Q3 earnings data, showing performance metrics and guidance for the next quarter.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPY0RNdnU1aWd5VzJiR0kxMnQxZmU2UGlFd3JqRnVpSVBZTVotVS0tNDZnaDlkNjgxZ3RWTTM5WHYxeng5RXA2WVVkM1NmOUVuZW5GYXpramZRYS11Z2NUSXBYVndsbU5tdjc3NjJxQ0lyVTZpOWVoUk9MV1JiY3JTYVhEYTROLTdwXy1pOUgwbDFkVlF4bXR3?oc=5>

### MCO Q3 Earnings Miss Estimates as Costs Rise & MIS Revenues Fall
- Summary: Moody’s Q3 earnings fell short of estimates due to higher costs and lower MIS revenue.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNWUZKdDZYa0ZBWlpmNC0wY3E2d1R2TC1ub2JRRWVHcEhuVmhVTnN6ekpvX2s1NDJRZzVTXzBHS0hQc1RlODRPNzNyYWVudGVNOUdoMUkyX08xWVB0SWxldTVmTGlTTWtmdjJMNjFNNXVIWnVLQ1lrN3RKUk1NQVk4MnR6ZWY0M3JFY01GOXFhbnljVjV2QzlIc2Z4OS1EMHRLMGphZTJIY3dZS2ZUTlM3Q21XckROTnd2YXc?oc=5>

### Moody's Corporation Reports Results For Third Quarter 2026
- Summary: Moody’s reports its third-quarter 2026 financial results, detailing revenue, earnings, and outlook.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOR0xWTWh6WVJObG1jd19ZdGVMLTI0ZE52dVR4R2FtcGNOZVBLdDNKZW9CSUd1dUE0MHNZZUpGeERJU1hyYVBjMmNFeFIyd0F5dkpvTnlVbkh6bElkQnJJUDdCR21jSzZ1Tmg4OEtoTGRvZ1loMjZpNGYzVUNHTXlBem02MGFkV3ZhMDYtam4xcGV0UQ?oc=5>

### Moody's (NYSE:MCO) Stock Forecast & Analyst Predictions
- Summary: Analysts provide forecasts and price targets for Moody’s stock, reflecting market expectations.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxOem9wWWxzM0VxUXlSM1dsNl9sTUFwTHdKcDRTRXl1MDZId0VadW5CRUFzTWhLOXZ1LXFYVnJicnVMN1JFNFZ1czgxZ1JTVjJ6aDdpc3Rfa0MxajVOSk5jOWJtTGZBVlFnQ3Z3V3I4NDQ2R0Fyak9zU0NUdW1zaVdJTUFDZw?oc=5>

### Revenue rose 1% at Moody’s (MCO), while earnings per share grew faster.
- Summary: MCO reported a 1% revenue increase and higher EPS growth, indicating solid earnings performance.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOTUl6UTk5bmVfelktYUl4NTJ5UlpRNlhmNmNlbGJRN0JQSlRFVmU2R1ZyNVFyMUNlNmVGeDgwc2VReDNvc2tIbnpqOGVFdkhBeDB0Tjc3VXFQX2xhamhLVU9scnB3bURraXNZMTVPTktNaV8xVXp0MjBfMmJNR0I0S3hCVmRDdlRIaDdfZEktWm8zMGh2V05lUEUtMG5TeHdrN2E0bg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCO** | **28.53** | **25.24** | **21.84** | **0.80** | **82,292,842,496.00 USD** | **-1.91** |
| SPGI | 26.84 | 6.60 | 17.37 | -5.40 | 130,260,762,624.00 USD | -2.94 |
| MSCI | 31.18 | -14.46 | 24.71 | 12.40 | 43,979,137,024.00 USD | 3.35 |
| FDS | 21.24 | 5.51 | 13.66 | 6.30 | 11,028,183,040.00 USD | 10.36 |

Peers fetched as_of: 2026-10-28; MCO reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-02-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

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
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOYlgya3hNV1VLcWRmbEFTbmhEUG1Zb2I5bXJjc3NqUi1XVWw0ZVREaUI1ajJySk0xaUhSTE9IdXhtUUdaNzJvZkR0cU80TWMtOGZSM2pxSDFrb1lfaDBVaWRDMnhlZDFWMXJqeGxJbG54VG9nZFRCTFNEQ1F0VHo1S2xjSXMxX20xRjVJU3dfNjZzLUtzYmE1TG9fYTBEMG1NMWc?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNZ3FnQlhEYk92QUxZYWVUMm5zWXdYeFhjZHM0c2MtOXk4bzZkWFVieW9yeGFCRE10cm5DTEZUdmFrRzFieUNQNmNseEtsWnViYnlYektPWnhUWkE1cGgzbUw4MGppb0JPLTh6Wno1T1BsNVZ3djRSUDhmRTA3ZUZ1UlpZZU5pNUlZR0tmSndCUGF3UmYxZDFYRld3?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNaEpjZDc2NWVqazNVeEZQSGtWU1dVeTJOWmpncHVGb1k2M2xOZm5oMEg4bkc3bkdJUjZGeDYxR3d3TWxHcDFFYi0xT1BENXk3MDFzTThvVG02Ym1BR3o1bk9mMW5SRUgwUy00d3hfTTd2MWh4ZkE4T052Rkh3VmZrR2lKalZuaTFBS0hDci1Yc0VSMjBSZEJFY1JNT002cEE?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPU3FIdVhRM1BuN3psR3R0eVRHMXJhT2g0dk9oTV94NWhTMW5xREcybzhDa3pVT1JOZFZibEJWX1pGeF9HMk01bV9rQ1I1dVA0RG8zTHRpNXBuZGR6WjlUb0lDM2hSTEdONHJzQjhJTGgzUWxIeVM1aVdUZmpjUVBjZ0ZmVmdZVHBhMGd4QlR6d2tBdw?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNT2NpQkJXMERYQnh0YWI3djVHeEUxSy1EMk5EVDdldWFvLWk2Vm9JNU14dk9CdExwMXgxaFh4bzdDYjNVX1NNRnJUeWVuai1pN2hUYjhydXVjWWZ0QnNybmp5SXdlQ0FWakZFQjZ6UGVxNDNWN1RFYUUyX2NoeGJEMDhIXzlfWUZvWEprTVMyT3lqRU9zdUY0cVVSZzl5UVd2ZzlBekJmWVlPOG5EdEZqbWpn?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxPWm9YbGdPV19ITUkxcjQ2NDQ0ZGNRZ3RGemxmMnloNVJlenh4YjgxMHpwTWY3WXUwaG1yNGE2TjItZXhlTVBCQ2Z3b1QtMlBBdnRVM25mMm1ZZzItT2lrSDAzVmdrZWxaNF9wUDVGQUNoaFZERnhYQVVJZXdhbzBQellkQzkzWmJUbHVaZFNrcDFJWG5OSHNLRUFQYnNneU9ZbzJ0M3pwUXlFTFRfbDlDNlZ6X2tQVmxiREF4SnlmRFF5T0FsclJob0V3eUJOVnp4YWs0?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOQk9UUnltYnFpRnlQQ1UtbWY2LWlIc2lCNHFGTGF0eHQ1SjZtWlQyMnhfWnpNMGtOQzNaRzdyWHNMT2FqTkhPVWNBYXRUMjFXQjc3LWRwS0lpaHZVNTdoV1pLZTNkcHBELUNJN1hXeVdBZnp1WDNVUlctM01uQ3dMNUo4OGNuWVY1TFZFbng4cWxoWHlxRWNvRENGYm9uSWlPZ3pBS2t1LVJRYlRaVVN4cjFZRWU2WDJ1WV85OExicUlGTVBr?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxPcmFSWEJnUDZ4aHRjeUNIazhGNWlQYUQxMEU2Sjc4VGNrY3NBenVEWUdUWXc2NTVYeVVrNWNSN0dlZWg2eFM5cWo2eXhYd1FtOEF4LW1RSWluSGpIWXlyemVPQ3k4eFNPYVFGb2JKa3RMQTJpLXBTMHpFN3gzTG8zb0RjamN1YXFwN1NCOVBWdENMS2ROZ1BpYXhLbFpmc2hrVVFqRmpCcEZDMkEwcnZlVkIzRjNibUJEZWNzXy0wLUdCbVY4TWZ3anktdUp1enpDek9SaVZaUW9wZw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOM0cxVlhITUo1MmZ0VWdTSEIxM0dSOXJfX1N2Q20tYkdfcHVNaFZ3U21Ca2xnN2hZOFFjdXR5NWVCdTRGZk42a2J2ak96OEp3MjRnUlBES3d4T014dUdTZmxQRWIyc0xOZWpYWGdxUUl0SExuNDZLMkhZc1JXRHozdHZlMGZ1U0p3TFZicnVaelVrdGFFWVdfbDhkQ2JoQmZfLVMwZQ?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNcEFhQzgwYW9NdkZWZnZkMjFvUVdkUHVBU2JFVWdzZG01SjN2RkRrTkVPQ1Q4bUlVZWEtb1ZuYXp5NlN2V21OenpoQjZ4NDJMRXdKRnIxZjl5SWZzMnRNbTJ5RnVuMEF0UkFMbUV4bGs1UjN5N3pVNkU4TlNtZlFqenlTN1pjeHpQT2djR2RaVjRIbkQxYjEycDQyQTNueGNyWEs0ZjNVT28zamxEcm9qSGcyZkVnQTNvUjRpdmhRcXhOZTZrV2ZRMnluc0h2UTdyU2cyaUN3?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNREV4Zk56cWV2ekpaWTk1TzNlTW9SaTJLZV83dkt3Q19NV0NMLXdZdGZzMURqT1haU0xrNzlyZVRLSmhUVWJZYXlrZ2pjR3dzWEhJRF8wM3BxRjhabS1qT3hHZmxZYW15TXV2Yk5tWEd5TE12Y2hISlp6alc0VjhWWGFjVzd3ODN5ZWM4YmpVTDBlaUlNTkY1elpRRTdOSXVzMHBqMHNPNkloZjJrcGpyZUFnb0Y3dnM?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxQc2YzTFRIMnZpMUQwdUZKOUtEQm1MTE15OE1HR2VvYmpxMnlzTl85R0ViQTNSQlJtTTUwOWpwbjRMZUFKUDdrWWliX1JJWVpjZ0c1ODlmR012WGZyaU9hc0djYXZ1aEtqRlpiZ2NhV2dkV2NZTE95bUdPUGUxTmk2RGUyVi1rM2NJR0Y2bzdHcVVGVXo4eHRRVGhlOHBYWjhCWnVvcUg4M0ZDM3hvcU5DaXg1ZkxVR2dFZkhkZXAxOHhsUDRTbWZ0b203MXdCdUl3VURTdFV4RFQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPY0RNdnU1aWd5VzJiR0kxMnQxZmU2UGlFd3JqRnVpSVBZTVotVS0tNDZnaDlkNjgxZ3RWTTM5WHYxeng5RXA2WVVkM1NmOUVuZW5GYXpramZRYS11Z2NUSXBYVndsbU5tdjc3NjJxQ0lyVTZpOWVoUk9MV1JiY3JTYVhEYTROLTdwXy1pOUgwbDFkVlF4bXR3?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNWUZKdDZYa0ZBWlpmNC0wY3E2d1R2TC1ub2JRRWVHcEhuVmhVTnN6ekpvX2s1NDJRZzVTXzBHS0hQc1RlODRPNzNyYWVudGVNOUdoMUkyX08xWVB0SWxldTVmTGlTTWtmdjJMNjFNNXVIWnVLQ1lrN3RKUk1NQVk4MnR6ZWY0M3JFY01GOXFhbnljVjV2QzlIc2Z4OS1EMHRLMGphZTJIY3dZS2ZUTlM3Q21XckROTnd2YXc?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOR0xWTWh6WVJObG1jd19ZdGVMLTI0ZE52dVR4R2FtcGNOZVBLdDNKZW9CSUd1dUE0MHNZZUpGeERJU1hyYVBjMmNFeFIyd0F5dkpvTnlVbkh6bElkQnJJUDdCR21jSzZ1Tmg4OEtoTGRvZ1loMjZpNGYzVUNHTXlBem02MGFkV3ZhMDYtam4xcGV0UQ?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxOem9wWWxzM0VxUXlSM1dsNl9sTUFwTHdKcDRTRXl1MDZId0VadW5CRUFzTWhLOXZ1LXFYVnJicnVMN1JFNFZ1czgxZ1JTVjJ6aDdpc3Rfa0MxajVOSk5jOWJtTGZBVlFnQ3Z3V3I4NDQ2R0Fyak9zU0NUdW1zaVdJTUFDZw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOTUl6UTk5bmVfelktYUl4NTJ5UlpRNlhmNmNlbGJRN0JQSlRFVmU2R1ZyNVFyMUNlNmVGeDgwc2VReDNvc2tIbnpqOGVFdkhBeDB0Tjc3VXFQX2xhamhLVU9scnB3bURraXNZMTVPTktNaV8xVXp0MjBfMmJNR0I0S3hCVmRDdlRIaDdfZEktWm8zMGh2V05lUEUtMG5TeHdrN2E0bg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
