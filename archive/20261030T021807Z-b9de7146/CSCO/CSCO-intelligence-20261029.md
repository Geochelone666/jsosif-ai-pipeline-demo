# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:22:59.328152+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 9, 'ai': 13, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 8 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 56.0%; oldest publication 2026-10-24

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 108.5900 |
| Return 1D (%) | -1.5414 |
| Return 1W (%) | 3.5275 |
| Return 1M (%) | 1.9366 |
| Return YTD (%) | 43.5809 |
| Return 1Y (%) | 55.0545 |
| Annualized volatility (%) | 35.4878 |
| Beta vs SPY | 1.1182 |
| Max drawdown (%) | -18.6996 |
| Sharpe (rf=0) | 1.4191 |
| Downside deviation (rf=0, %) | 23.9399 |
| Sortino (rf=0) | 2.1036 |
| Historical VaR 95% (1D, %) | 2.9026 |
| Historical ES 95% (1D, %) | 4.9273 |
| Correlation vs SPY | 0.4005 |
| Tracking error vs SPY (%) | 32.5521 |
| P/E (trailing) | 32.61 |
| P/B | 8.52 |
| EV/EBITDA | 23.79 |
| Revenue growth (%) | 17.60 |
| Forward P/E (estimate) | 19.32 |
| Gross margin (%) | 64.52 |
| Operating margin (%) | 27.72 |
| Return on equity (%) | 27.32 |
| Free cash flow yield (%) | 2.61 |
| MA50 | 109.8478 |
| Close vs MA50 (%) | -1.1451 |
| MA200 | 100.3695 |
| Close vs MA200 (%) | 8.1902 |
| RSI (14, Wilder) | 46.9141 |
| MACD (12,26) | -0.5448 |
| MACD signal (9) | -0.4250 |
| MACD histogram | -0.1198 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 108.5900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.5414 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.5275 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.9366 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 43.5809 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 55.0545 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.4878 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.9399 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.1036 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9026 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.9273 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4005 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.5521 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.1182 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.6996 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4191 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 19.3151 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.5240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.7190 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.3190 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.6120 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 32.6096 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 46.9141 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1198 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -1.1451 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 8.1902 -> Clearly above the moving-average trend level.

## TAILWINDS

### Cisco Systems (NASDAQ:CSCO) Stock Jumps 1% - What's Next?
- Summary: Cisco Systems (NASDAQ:CSCO) Stock Jumps 1% - What's Next?
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQNEhvdnlwR1h1Q2hiZWdXS2xpdFdUak92TndqUnlMbk5sLTQzRzE1WXhDY0R3a20zczBQRzNIcjVKck9PSDd3QkVZSVBNQV8wRUNmLU0wUWc1aG90bDFWb0FMWjQ1dWRUWkJhZUZJT3dPdXYySWZpWnVsQWRyTlY1M3ZhOEs3eEIzb3pvcWhOSUwxOTZxWGV4QU9XdGhMYXhBN3AzZzRCdFdZRzRZLXRN?oc=5>

### Cisco Systems (NASDAQ:CSCO) Stock Price Up 3.5% - Here's Why
- Summary: Cisco Systems (NASDAQ:CSCO) Stock Price Up 3.5% - Here's Why
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOODJoejlkSmVnYnNFQVVVcm1rOHVhbWtjWmx3ZUxFcDRhVmNMSnNiUm5RY0lybGhlTkJNRmdiaGJ6d3ZiTFVQQ1BCa0FmSzgyZlhsQU1EY2ZEdU9DeTFsZ1hCQkVJbGhKbWxERWN4aFllUndPOFN0MTZRTGNjUnF1YWV0eEV0aWM5aE9JclpicHM1YmJTYks2UFk2ck9FbUNaQk52YlVwVXFzX2V5MjZiSlBYdw?oc=5>

### Cisco Systems, Inc. (CSCO) is Attracting Investor Attention: Here is What You Should Know
- Summary: Cisco draws investor interest, highlighting key factors for potential investors.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQMHVMVktpVGhyY0VnMzN0akozZWs4dTF2WHc5eXkyREtnc2dyem5zcERqYV9rSUN1Z0psQzV5V0NOMUl6X3kzSUNHTy1PS2dNYW5MaVctNENMVWVQdmZYeU93b0dodzBuWWhIa0J2R3cwOEFCZ3pQUnAtWS1UU2pBNWhLd1A0X3loel90amFLUW9qa2JjSDZWZEVNWGJocG8?oc=5>

### What Are Cisco Investors Betting On?
- Summary: Investors are evaluating Cisco’s future prospects amid evolving tech trends.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNbTlIV0hzR19DbUFCSmZrd1czTjlpSGJzbXRsY1VmLTVoODJXd3VCUTd3WVF6WTd1bFFEQU5sMW1PX3Y2TDZ3NUk0WE1mZ0tqSDc5WC1YV3IzNG1WbnFYNFBsOVdYQVRObmlqTUZIWTdDRGFFazJzd200Mkh1ZmI5R2UyVWNKN3g0cXY2OVNBdHBON3YxZ21iVVpyRXg?oc=5>

### Can Cisco Systems (CSCO) Stay Cheap As AI Cash Flow Builds?
- Summary: Questioning Cisco’s valuation as AI-driven cash flow increases.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOcHByUFgyeGJxTllUYXBFUy1rUXY4UEItNFhYVFZXcEY3bVJBUTVOWWxBbEF2X0p6eXFqUVg3aW9FZDF1SU5lSndmcnJnV0gzZmdxUWZzZnNNdUVNR0xqczFoSUU0YW9OeUE2TnZ2YjlXalFFUDNrSmozRXpZWi1rY1NGQ056TkZTMWxDblFPNmVrQTQ1dHYzMmlR?oc=5>

### Is It Worth Investing in Cisco (CSCO) Based on Wall Street's Bullish Views?
- Summary: Wall Street analysts view Cisco positively, suggesting potential upside for investors.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOZ201RTRRZnMxdG5ZTFZFcHU2a0c0RzNvUGtaX3VlYnB3cHBidjdTTnEzQkZCLU5YZ3d6X2lIa2RYVElFQlkyUkdNNUFCRHFCQklUTGQweGt5bzBCNDVaSGdhellUbGJpSDJ5SGFieTB1U0gzRV9SOTJXblcyRl9hRTNVY0pNMXc4LXhuclFhTWNHNWxxSF9Ib3p2d0hEQQ?oc=5>

### Cisco expands partner access to insights from close to 20 million devices.
- Summary: Cisco opens partner access to insights from nearly 20 million devices, enhancing collaboration and data-driven decisions.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxONmU1YzJ5ZkdkYWpKbUYzWFRzR3AxY3pCbDVkcjZrbXpSUU9saGtTc1AwdkFSVTd6R05ScVNZMWU4N1VIQm1rUlBZNmNTNXNPdnRFNzk2ckhoZm0wb1A0bklWS0RKWUMxaE43MlFYQVZFQV9BbnNCMWE2bEtsbTdaVVUxZ1ZSVTgzSVRZRndEaWNtSzVHR3pMT1NQMTh1d01LckJlbkVTdE5QWGxTNHVONjNDVUpkRmF6cmtXMjRBT20?oc=5>

### Cisco Systems, Inc. (NASDAQ:CSCO) Stock Has Consensus Target Price of $128.52 According to Brokerages
- Summary: Brokerages set a consensus target price of $128.52 for Cisco stock.
- Date: 2026-10-29 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi8AFBVV95cUxPRFFtSWJza3ZMMUFhWGJMLXFXNm5jVDBJcElFZjVETEVoQS1BZ19nYkhfQ0FzaUp2Y2FXRU40REVpVGVFRmtHeDlNV3Zkbm1oZ0J6QTR0ck5Tdk01UGh5OFdMTFpPQndUdlNzZVFEY2tUUTVPcXRyYVcwbGtRRW13cEpjbVcxTEVVQkpDd3hfc2R1UWZZci16bkkwelRPRzIxdEdOMTB5Z2dReURSeXZUUTBHTEVlckcyQU5qa2czQ0tYOGtaeEw0Wk9Ib2FLREpMeFRZYUtMaVdfM2xsdWRxYkpoeWhjN1Z4YU1nOWNCeEs?oc=5>

## HEADWINDS

### Cisco Systems (NASDAQ:CSCO) Shares Down 1.5% - Here's What Happened
- Summary: Cisco Systems (NASDAQ:CSCO) Shares Down 1.5% - Here's What Happened
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxQVG5fQXRDMUJGenBZSVVPOWk0SUp0Q281M0p6OGhYZWJPUFlCSnZHNWprYkRzT3ppQTIwVWpON3NWZUhmSDg4Vk1nYWZsTk5SZFU3VzdEZ3VnWnNkdXA5eHM0dGR0Z1pPTjY0dG1wY3dvTVRjNHdiMGxGbHlyRzBnWXA0Z1lqUVNkWHhocGNLRXRqSUdvLVZEeXV5LW1zcGpZR1lTUGpXYXB6aWZIeDFPVER6d3g0MEdGZHUzcg?oc=5>

### Why Cisco Systems (CSCO) Dipped More Than Broader Market Today
- Summary: Cisco stock fell more than the broader market today.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPTGtSaFE3OVRZdGp1MzdnWm1OWEZDYlpzZUMxUGlPaHVsRVVWZ2gyWENCTFk4dHJKMk9WdEgxdHRjeHFCVXNPbjNTOGExTlZJMDlDSXhZZmctUFpxSW1pZW9ISnFkUkUwcElKT1JfRDg2Z3UxVzR6WGw4bjJraVJ2SlhnYjZDcnJvdGpvNGY0RnhzZ1RYNFZxVDNR?oc=5>

### Cisco Systems, Inc. $CSCO Stock Position Reduced by Bokf Na
- Summary: Investor Bokf Na reduced their Cisco stock position.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxOQ1drMkFrZFBwVkpBQmZmbWloMVlORGp3QjB0YUNHX1pVOUdkNlFMRXNNNVJEZHFIZVZQNnJ5NEFGaGswSkdwVlNtVjhWa3dBVlVNZnZTLTdqZ1ZHY0tJOTVwVlowX2FYamJlUDF4TzE5emhCc0ctbFd4NklKQ0RkMmJuak9Fa04xWFp5cF94RDM0aVdNVWd0M254X29IdldFOV9HdGF1UkpSb05zX0Y0Y0ZvSkFxejhZ?oc=5>

## CATALYSTS

### Cisco Is Up 47%, IBM Is Down 13%. Which Dividend Stock Is Better for Retirement?
- Summary: Cisco Is Up 47%, IBM Is Down 13%. Which Dividend Stock Is Better for Retirement?
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPWkRMNUdXeDZuWDNGOFlDYkNVMzU3ZmFyY3E0NnhMN1Z0eHAyaHk5XzdubkN6X2FnYm05Ym1GQWc2Tm1OaTFzRkVESUNyRTA5V01IWjA2SlJJLS05R1FFNzVjZWZHeVBfSGJqWC1NT2JsQ2Z3TktXMGw0ZjVmZkpaenNXYzNmMm93Z3dSQUdNZHU3aFFJbzZnc3hkUUxmUGtFVnVRQ1JBOTRvSThQalFneUVaX19nbGdPZng4?oc=5>

### Cisco Systems, Inc. $CSCO Stock Sold by VestGen Advisors LLC
- Summary: Cisco Systems, Inc. $CSCO Stock Sold by VestGen Advisors LLC
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPMGJnYnhjOGx1RGZraDV3SEZzbWhFT1ZSLW1QQ3BMZnlxYlV6X2RmZlF3VmVLRjJ1d0YxU2Q5N3pwaTFSaUpOX1kzYlBGQ3RzOVdpbzFtQlVHajc5Q2VFblFuTzhYN3pKOUFmNS1JNzFwOFo5YmREMHpBYkNMbXl1ZnZVSlNRbThfRG1TOXUyeklfYXJQdXNTTHY2cFZQQkpHd3QtODl0UUxWSFJHZUNfNjl3VGs4Q1d4MGc?oc=5>

### Cisco Systems, Inc. $CSCO Stock Sold by Sowell Financial Services LLC
- Summary: Cisco Systems, Inc. $CSCO Stock Sold by Sowell Financial Services LLC
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQbTZoN1k4cDZlMEJPMUN0MGZSb0VkbGJGWDUxcy1wREpzMVotUk15R3BPRWVmU01XVGxpdGhkNmgtTVhjYWZrSVRJcVpZamx0aVJPZVR1a29TMmdxS3FRdFBUZlhNUGJmQm9RejNwRU91UjBRbUNkb1I0MkV1NWQ1eUl3S0pLSTRFS09tVTkxTWxGOERZSVYwZm13Yzcweko4eVJ1MFFreUpENEdqaXg1YThvQ3piRXpEQVA0dVhWc3YyMGJiZEE?oc=5>

### Cisco Systems, Inc. $CSCO Stock: Stockman Wealth Management Inc. Cuts Position
- Summary: Cisco Systems, Inc. $CSCO Stock: Stockman Wealth Management Inc. Cuts Position
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxPYTU5cE1wN3k2cGtEa1dRU0VhdU1pNWlYcnFzUDd2ZWZDdkJ6cHdpYmZrX29ZNEFsR3h5Mk5raWdyRkg3ejYwaWtrOXpKY1hqRmRwdkxsQVdBb1QzZjRsSkdGOWVvLXJiUF9YNVF3OG04QmJhREVQclFDcC1KLUxqWElFdzdTY0IwRm1jYVZDMDBDSmhHcllBYzhmdnRrVUtMbXBfMGJqOTNtX1lsdzQ4eEZDNmNMQTBxVnBPYnBoeVRPWnRQd3ExbEFwNmhzV2c?oc=5>

### Cisco Systems, Inc. $CSCO Stock: Simplify Asset Management Inc. Lowers Holdings
- Summary: Cisco Systems, Inc. $CSCO Stock: Simplify Asset Management Inc. Lowers Holdings
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxNQUJ0V2NNeWZxaGFhbThqcVM3TllvcjRMSkRJR2w5OGpZODRkcTUzcEpsMEllbDg2UkRJOXJpYm5LMG55N0NWdy04TzJKQ3hxQnd4bDFGRWlEWGp0VVRnUWhDRkE3ZFRFenRqLVZiWHRGX2lhNVYzZUwxT0wtR3dQcVA1TUFESzcxeVgyQ3JiSkhsT0xMSGoxdkhsRHlITGh5dUlmYVQtVmVaOXo0dHlQa2FjZ3JMSG80QU1FM3FYZXE2VUhxX1pfZVNLNkN2M2ZX?oc=5>

### Cisco Systems, Inc. $CSCO Stock Sold by Arnhold LLC
- Summary: Cisco Systems, Inc. $CSCO Stock Sold by Arnhold LLC
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPT2NOWW1sVFZlMUdTcm90NHFUTEUzNUVsMTBUdFg2NEdtbnBnZ2pTZFZVVzBhYmlLZXFCdzlUYlpzWE5aVVpFUlB6V0s5Y2VDS3ctUTVNYjNVaElDT2J5d0wwaEJVaEtybUt1c1VaX0FkTG5ybFVTTnd6N1FNN2hXZFJfWFRwa1ZNTnNMTDVTYzRMZ1JZZnQwSTZiRlN1VVFoNlVScFJtb0ttOHNmOFE?oc=5>

### Cisco Systems (NASDAQ:CSCO) Shares Break Above Fifty Day Moving Average - Here's What Happened
- Summary: Shares surpassed the 50‑day moving average, indicating a short‑term bullish trend.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxNd2ZhYzVVLWZPN3JZbVBlVHpCdXdmNnNKWXJMa1dsNkVnRmVRellxQnZTenZ1aEp0N0JOUGhwMkFPTFlpQjVHNk9aTFM4VTYzd2JwUmJMQ0dSWDJoMFFGaWYtMF9nemM0RGlMcGFkQkppTWh3bVhnNDBkTEZtT3o2MFlTME4yYWtTSkFHNHJ0ZFRvSDFPNnZFSEZrWGVNdC13R0lHYldOYUdrTjF2NHBrZUctN3d4UllDTEEtT0hRRXBIVFhKVEtCRllIZnB4ZVZ3YWFjY1Jfd2VQUzB6Vy1UQUNJNA?oc=5>

### 31,948 Cisco Systems, Inc. $CSCO Shares Sold by Sterling Capital Management LLC
- Summary: Sterling Capital sold 31,948 shares, reflecting a short‑term market move.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQM3BuVHRsckRsR3NkV2lUOWxjUjNDMEprcUx1T0hQTWtQQ0F3OGV3S3htYzFOZ0dwNmVJaWRzOU4zR0dJWWd6eUIyZFZ2MDRFVTFERVo5ZlJ2NHpHVm9Sc1dMVDRQWWdvakx3LVd2QWM2Yjh1clpzSjVpZDRJY3A4Q1FjRXQwYjQ5dm1Gd24tYlU3Sl9mMnBrcmdteTduUGRfcXo0N1ljaHJTaWVKcTd3ZjMteWEyRVowLWU4SERPbmJZQnVZRUVELTZOR0VmYmx2bWc?oc=5>

### Conning Inc. Acquires 65,355 Shares of Cisco Systems, Inc. $CSCO
- Summary: Conning Inc. purchased 65,355 shares of Cisco, indicating a modest ownership increase.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxQWXFJMnk0MExoM09Wbml6YnZtSE1qamZkU3B1Rm13WlI5NlNiTnpPOV94eWVDdnBoUFBkbXg5cXRyUzd2a29xN2pxTDhmaE1sblNQTTY3VFY4bFVwaEpGNjNZMEZMMER3M3hMQzlydWY0WGZnMjdUdUhySFQyNUFxWWRIclJKMDJ0SmN5OHliNGUyeVlMMjRsT3M3dDFpNzlBUzhZY3JmaWtpbnVHOTJ0X3A5ODdmOVRZVlhfbA?oc=5>

### Motley Fool Asset Management LLC Buys 273,992 Shares of Cisco Systems, Inc. $CSCO
- Summary: Motley Fool Asset Management acquired 273,992 Cisco shares, reflecting a significant ownership stake.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxQdXBzeGNwdExtdDNsNk9uc2tfSFFWenNoRkVwVVJBUGVoZW1zbjc1UkUzekYydGtNU3Jhb1pHWlVfU1lYckFHT0szWGlQb2dMdWhZdTdPSGhSdDF1Q3hhd3Y3cVRFeXNJUEh4b2JnNUxQQWdEVGxza3o2ek81cDNFUF8tX2MxYzV6NkNVZjNlMlhROTVwTmJ4NE9GR216Q3FXZUpxdXVRNm5aQjE2ekpGWnVENUxSMXhpdll0MjFLTHJ0V2k5SGdfMWpvbjZ2Q1ZobmNNZA?oc=5>

## RISKS

### Wells Fargo (WF), Cisco (CSCO), Marvell (MRVL) join objections to OKX-ICE tokenized stock plans
- Summary: Cisco joined a lawsuit against tokenized stock plans, potentially facing regulatory scrutiny.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNekc1MnU3Uktka3JVcEpxem1xS0UxaGZVQzcwQTVBWHNQd01PUHNJMzdBa3Y4UFB6SkVlRTljOHJzYnZIS045eklhNlFtTDJFd3llSXJBS0x5VFNialdLMm5CVDhSTTBVa1lkcmxab1ZoQVZ0ZUhTZXl5ZWs0T0FFZUxIT0pvcmh1TjRLVUxGdG9Dd1JjQjVYdmRmaEdSdnl0Nk55aWxmMU5uX0NaN1hyU1g5NjJEOXoycGJWRzV1VXE1VGppS3lHOWd1TDc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **32.61** | **8.52** | **23.79** | **17.60** | **428,125,487,104.00 USD** | **55.05** |
| ANET | 58.11 | 15.70 | 47.20 | 37.70 | 232,342,814,720.00 USD | 13.69 |
| FFIV | 29.03 | 5.16 | N/A | 13.30 | 20,648,525,824.00 USD | 40.46 |
| HPE | 30.35 | 2.95 | 13.40 | 33.70 | 78,147,854,336.00 USD | 146.94 |

Peers fetched as_of: 2026-10-29; CSCO reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-12
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-09-02
- Revenue (latest available single quarter): 12,844,000,000.00 USD; period 2018-04-29/2018-07-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 3,373,000,000.00 USD; period 2026-01-25/2026-04-25; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/858877/000085887726000132/csco-20260725.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMirwFBVV95cUxQNEhvdnlwR1h1Q2hiZWdXS2xpdFdUak92TndqUnlMbk5sLTQzRzE1WXhDY0R3a20zczBQRzNIcjVKck9PSDd3QkVZSVBNQV8wRUNmLU0wUWc1aG90bDFWb0FMWjQ1dWRUWkJhZUZJT3dPdXYySWZpWnVsQWRyTlY1M3ZhOEs3eEIzb3pvcWhOSUwxOTZxWGV4QU9XdGhMYXhBN3AzZzRCdFdZRzRZLXRN?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOODJoejlkSmVnYnNFQVVVcm1rOHVhbWtjWmx3ZUxFcDRhVmNMSnNiUm5RY0lybGhlTkJNRmdiaGJ6d3ZiTFVQQ1BCa0FmSzgyZlhsQU1EY2ZEdU9DeTFsZ1hCQkVJbGhKbWxERWN4aFllUndPOFN0MTZRTGNjUnF1YWV0eEV0aWM5aE9JclpicHM1YmJTYks2UFk2ck9FbUNaQk52YlVwVXFzX2V5MjZiSlBYdw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQMHVMVktpVGhyY0VnMzN0akozZWs4dTF2WHc5eXkyREtnc2dyem5zcERqYV9rSUN1Z0psQzV5V0NOMUl6X3kzSUNHTy1PS2dNYW5MaVctNENMVWVQdmZYeU93b0dodzBuWWhIa0J2R3cwOEFCZ3pQUnAtWS1UU2pBNWhLd1A0X3loel90amFLUW9qa2JjSDZWZEVNWGJocG8?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNbTlIV0hzR19DbUFCSmZrd1czTjlpSGJzbXRsY1VmLTVoODJXd3VCUTd3WVF6WTd1bFFEQU5sMW1PX3Y2TDZ3NUk0WE1mZ0tqSDc5WC1YV3IzNG1WbnFYNFBsOVdYQVRObmlqTUZIWTdDRGFFazJzd200Mkh1ZmI5R2UyVWNKN3g0cXY2OVNBdHBON3YxZ21iVVpyRXg?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOcHByUFgyeGJxTllUYXBFUy1rUXY4UEItNFhYVFZXcEY3bVJBUTVOWWxBbEF2X0p6eXFqUVg3aW9FZDF1SU5lSndmcnJnV0gzZmdxUWZzZnNNdUVNR0xqczFoSUU0YW9OeUE2TnZ2YjlXalFFUDNrSmozRXpZWi1rY1NGQ056TkZTMWxDblFPNmVrQTQ1dHYzMmlR?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOZ201RTRRZnMxdG5ZTFZFcHU2a0c0RzNvUGtaX3VlYnB3cHBidjdTTnEzQkZCLU5YZ3d6X2lIa2RYVElFQlkyUkdNNUFCRHFCQklUTGQweGt5bzBCNDVaSGdhellUbGJpSDJ5SGFieTB1U0gzRV9SOTJXblcyRl9hRTNVY0pNMXc4LXhuclFhTWNHNWxxSF9Ib3p2d0hEQQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxONmU1YzJ5ZkdkYWpKbUYzWFRzR3AxY3pCbDVkcjZrbXpSUU9saGtTc1AwdkFSVTd6R05ScVNZMWU4N1VIQm1rUlBZNmNTNXNPdnRFNzk2ckhoZm0wb1A0bklWS0RKWUMxaE43MlFYQVZFQV9BbnNCMWE2bEtsbTdaVVUxZ1ZSVTgzSVRZRndEaWNtSzVHR3pMT1NQMTh1d01LckJlbkVTdE5QWGxTNHVONjNDVUpkRmF6cmtXMjRBT20?oc=5
- https://news.google.com/rss/articles/CBMi8AFBVV95cUxPRFFtSWJza3ZMMUFhWGJMLXFXNm5jVDBJcElFZjVETEVoQS1BZ19nYkhfQ0FzaUp2Y2FXRU40REVpVGVFRmtHeDlNV3Zkbm1oZ0J6QTR0ck5Tdk01UGh5OFdMTFpPQndUdlNzZVFEY2tUUTVPcXRyYVcwbGtRRW13cEpjbVcxTEVVQkpDd3hfc2R1UWZZci16bkkwelRPRzIxdEdOMTB5Z2dReURSeXZUUTBHTEVlckcyQU5qa2czQ0tYOGtaeEw0Wk9Ib2FLREpMeFRZYUtMaVdfM2xsdWRxYkpoeWhjN1Z4YU1nOWNCeEs?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxQVG5fQXRDMUJGenBZSVVPOWk0SUp0Q281M0p6OGhYZWJPUFlCSnZHNWprYkRzT3ppQTIwVWpON3NWZUhmSDg4Vk1nYWZsTk5SZFU3VzdEZ3VnWnNkdXA5eHM0dGR0Z1pPTjY0dG1wY3dvTVRjNHdiMGxGbHlyRzBnWXA0Z1lqUVNkWHhocGNLRXRqSUdvLVZEeXV5LW1zcGpZR1lTUGpXYXB6aWZIeDFPVER6d3g0MEdGZHUzcg?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPTGtSaFE3OVRZdGp1MzdnWm1OWEZDYlpzZUMxUGlPaHVsRVVWZ2gyWENCTFk4dHJKMk9WdEgxdHRjeHFCVXNPbjNTOGExTlZJMDlDSXhZZmctUFpxSW1pZW9ISnFkUkUwcElKT1JfRDg2Z3UxVzR6WGw4bjJraVJ2SlhnYjZDcnJvdGpvNGY0RnhzZ1RYNFZxVDNR?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxOQ1drMkFrZFBwVkpBQmZmbWloMVlORGp3QjB0YUNHX1pVOUdkNlFMRXNNNVJEZHFIZVZQNnJ5NEFGaGswSkdwVlNtVjhWa3dBVlVNZnZTLTdqZ1ZHY0tJOTVwVlowX2FYamJlUDF4TzE5emhCc0ctbFd4NklKQ0RkMmJuak9Fa04xWFp5cF94RDM0aVdNVWd0M254X29IdldFOV9HdGF1UkpSb05zX0Y0Y0ZvSkFxejhZ?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPWkRMNUdXeDZuWDNGOFlDYkNVMzU3ZmFyY3E0NnhMN1Z0eHAyaHk5XzdubkN6X2FnYm05Ym1GQWc2Tm1OaTFzRkVESUNyRTA5V01IWjA2SlJJLS05R1FFNzVjZWZHeVBfSGJqWC1NT2JsQ2Z3TktXMGw0ZjVmZkpaenNXYzNmMm93Z3dSQUdNZHU3aFFJbzZnc3hkUUxmUGtFVnVRQ1JBOTRvSThQalFneUVaX19nbGdPZng4?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPMGJnYnhjOGx1RGZraDV3SEZzbWhFT1ZSLW1QQ3BMZnlxYlV6X2RmZlF3VmVLRjJ1d0YxU2Q5N3pwaTFSaUpOX1kzYlBGQ3RzOVdpbzFtQlVHajc5Q2VFblFuTzhYN3pKOUFmNS1JNzFwOFo5YmREMHpBYkNMbXl1ZnZVSlNRbThfRG1TOXUyeklfYXJQdXNTTHY2cFZQQkpHd3QtODl0UUxWSFJHZUNfNjl3VGs4Q1d4MGc?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQbTZoN1k4cDZlMEJPMUN0MGZSb0VkbGJGWDUxcy1wREpzMVotUk15R3BPRWVmU01XVGxpdGhkNmgtTVhjYWZrSVRJcVpZamx0aVJPZVR1a29TMmdxS3FRdFBUZlhNUGJmQm9RejNwRU91UjBRbUNkb1I0MkV1NWQ1eUl3S0pLSTRFS09tVTkxTWxGOERZSVYwZm13Yzcweko4eVJ1MFFreUpENEdqaXg1YThvQ3piRXpEQVA0dVhWc3YyMGJiZEE?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxPYTU5cE1wN3k2cGtEa1dRU0VhdU1pNWlYcnFzUDd2ZWZDdkJ6cHdpYmZrX29ZNEFsR3h5Mk5raWdyRkg3ejYwaWtrOXpKY1hqRmRwdkxsQVdBb1QzZjRsSkdGOWVvLXJiUF9YNVF3OG04QmJhREVQclFDcC1KLUxqWElFdzdTY0IwRm1jYVZDMDBDSmhHcllBYzhmdnRrVUtMbXBfMGJqOTNtX1lsdzQ4eEZDNmNMQTBxVnBPYnBoeVRPWnRQd3ExbEFwNmhzV2c?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxNQUJ0V2NNeWZxaGFhbThqcVM3TllvcjRMSkRJR2w5OGpZODRkcTUzcEpsMEllbDg2UkRJOXJpYm5LMG55N0NWdy04TzJKQ3hxQnd4bDFGRWlEWGp0VVRnUWhDRkE3ZFRFenRqLVZiWHRGX2lhNVYzZUwxT0wtR3dQcVA1TUFESzcxeVgyQ3JiSkhsT0xMSGoxdkhsRHlITGh5dUlmYVQtVmVaOXo0dHlQa2FjZ3JMSG80QU1FM3FYZXE2VUhxX1pfZVNLNkN2M2ZX?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPT2NOWW1sVFZlMUdTcm90NHFUTEUzNUVsMTBUdFg2NEdtbnBnZ2pTZFZVVzBhYmlLZXFCdzlUYlpzWE5aVVpFUlB6V0s5Y2VDS3ctUTVNYjNVaElDT2J5d0wwaEJVaEtybUt1c1VaX0FkTG5ybFVTTnd6N1FNN2hXZFJfWFRwa1ZNTnNMTDVTYzRMZ1JZZnQwSTZiRlN1VVFoNlVScFJtb0ttOHNmOFE?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxNd2ZhYzVVLWZPN3JZbVBlVHpCdXdmNnNKWXJMa1dsNkVnRmVRellxQnZTenZ1aEp0N0JOUGhwMkFPTFlpQjVHNk9aTFM4VTYzd2JwUmJMQ0dSWDJoMFFGaWYtMF9nemM0RGlMcGFkQkppTWh3bVhnNDBkTEZtT3o2MFlTME4yYWtTSkFHNHJ0ZFRvSDFPNnZFSEZrWGVNdC13R0lHYldOYUdrTjF2NHBrZUctN3d4UllDTEEtT0hRRXBIVFhKVEtCRllIZnB4ZVZ3YWFjY1Jfd2VQUzB6Vy1UQUNJNA?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQM3BuVHRsckRsR3NkV2lUOWxjUjNDMEprcUx1T0hQTWtQQ0F3OGV3S3htYzFOZ0dwNmVJaWRzOU4zR0dJWWd6eUIyZFZ2MDRFVTFERVo5ZlJ2NHpHVm9Sc1dMVDRQWWdvakx3LVd2QWM2Yjh1clpzSjVpZDRJY3A4Q1FjRXQwYjQ5dm1Gd24tYlU3Sl9mMnBrcmdteTduUGRfcXo0N1ljaHJTaWVKcTd3ZjMteWEyRVowLWU4SERPbmJZQnVZRUVELTZOR0VmYmx2bWc?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxQWXFJMnk0MExoM09Wbml6YnZtSE1qamZkU3B1Rm13WlI5NlNiTnpPOV94eWVDdnBoUFBkbXg5cXRyUzd2a29xN2pxTDhmaE1sblNQTTY3VFY4bFVwaEpGNjNZMEZMMER3M3hMQzlydWY0WGZnMjdUdUhySFQyNUFxWWRIclJKMDJ0SmN5OHliNGUyeVlMMjRsT3M3dDFpNzlBUzhZY3JmaWtpbnVHOTJ0X3A5ODdmOVRZVlhfbA?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQdXBzeGNwdExtdDNsNk9uc2tfSFFWenNoRkVwVVJBUGVoZW1zbjc1UkUzekYydGtNU3Jhb1pHWlVfU1lYckFHT0szWGlQb2dMdWhZdTdPSGhSdDF1Q3hhd3Y3cVRFeXNJUEh4b2JnNUxQQWdEVGxza3o2ek81cDNFUF8tX2MxYzV6NkNVZjNlMlhROTVwTmJ4NE9GR216Q3FXZUpxdXVRNm5aQjE2ekpGWnVENUxSMXhpdll0MjFLTHJ0V2k5SGdfMWpvbjZ2Q1ZobmNNZA?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNekc1MnU3Uktka3JVcEpxem1xS0UxaGZVQzcwQTVBWHNQd01PUHNJMzdBa3Y4UFB6SkVlRTljOHJzYnZIS045eklhNlFtTDJFd3llSXJBS0x5VFNialdLMm5CVDhSTTBVa1lkcmxab1ZoQVZ0ZUhTZXl5ZWs0T0FFZUxIT0pvcmh1TjRLVUxGdG9Dd1JjQjVYdmRmaEdSdnl0Nk55aWxmMU5uX0NaN1hyU1g5NjJEOXoycGJWRzV1VXE1VGppS3lHOWd1TDc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
