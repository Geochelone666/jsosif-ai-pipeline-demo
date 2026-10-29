# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:02:04.961212+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 6, 'ai': 14, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 8 named publishers; 0 exact duplicates; 23 HTTPS source links; largest publisher share 34.78%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 110.2900 |
| Return 1D (%) | -0.9786 |
| Return 1W (%) | 2.8249 |
| Return 1M (%) | 3.7264 |
| Return YTD (%) | 45.8287 |
| Return 1Y (%) | 54.6844 |
| Annualized volatility (%) | 35.5002 |
| Beta vs SPY | 1.1149 |
| Max drawdown (%) | -18.6996 |
| Sharpe (rf=0) | 1.4120 |
| Downside deviation (rf=0, %) | 23.9563 |
| Sortino (rf=0) | 2.0924 |
| Historical VaR 95% (1D, %) | 2.9026 |
| Historical ES 95% (1D, %) | 4.9273 |
| Correlation vs SPY | 0.3989 |
| Tracking error vs SPY (%) | 32.5858 |
| P/E (trailing) | 33.42 |
| P/B | 8.65 |
| EV/EBITDA | 24.14 |
| Revenue growth (%) | 17.60 |
| Forward P/E (estimate) | 19.62 |
| Gross margin (%) | 64.52 |
| Operating margin (%) | 27.72 |
| Return on equity (%) | 27.32 |
| Free cash flow yield (%) | 2.57 |
| MA50 | 109.8785 |
| Close vs MA50 (%) | 0.3745 |
| MA200 | 100.1990 |
| Close vs MA200 (%) | 10.0709 |
| RSI (14, Wilder) | 50.4525 |
| MACD (12,26) | -0.5053 |
| MACD signal (9) | -0.3950 |
| MACD histogram | -0.1102 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 110.2900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.9786 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.8249 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.7264 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 45.8287 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 54.6844 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.5002 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.9563 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.0924 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9026 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.9273 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3989 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.5858 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.1149 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.6996 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4120 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 19.6175 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.5240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.7190 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.3190 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.5717 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 33.4212 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.4525 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1102 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.3745 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 10.0709 -> Clearly above the moving-average trend level.

## TAILWINDS

### Cisco Systems Inc (CSCO) Stock Up 3.5% but GF Value Says Overval
- Summary: Cisco Systems Inc (CSCO) Stock Up 3.5% but GF Value Says Overval
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPVkk4QjBXZV9qdDF2SE5pQlVyaEFYVFZsZTNJd24wSUk0UU9jSWJCX2NNaUItQlAzT05oMnZ2dF9CdFp2eTNnbVFmbHp0U3k2bnkwTXo4ajBieTBBZE5pUWtZVEY3TnpudmNHeWlDTXZ5Rkd2dlBuS1A2TmZJMV8xRHRfZVFuSlVJS2tzLTdieUtVV0Q3VWNPM0FHdmtKT0ViLURSYW1KeXJRVHp0SWxCRWRnT2gzSUJE?oc=5>

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

### Is It Worth Investing in Cisco (CSCO) Based on Wall Street's Bullish Views?
- Summary: Wall Street analysts view Cisco positively, suggesting potential upside for investors.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOZ201RTRRZnMxdG5ZTFZFcHU2a0c0RzNvUGtaX3VlYnB3cHBidjdTTnEzQkZCLU5YZ3d6X2lIa2RYVElFQlkyUkdNNUFCRHFCQklUTGQweGt5bzBCNDVaSGdhellUbGJpSDJ5SGFieTB1U0gzRV9SOTJXblcyRl9hRTNVY0pNMXc4LXhuclFhTWNHNWxxSF9Ib3p2d0hEQQ?oc=5>

### Cisco expands partner access to insights from close to 20 million devices.
- Summary: Cisco opens partner access to insights from nearly 20 million devices, enhancing collaboration and data-driven decisions.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxONmU1YzJ5ZkdkYWpKbUYzWFRzR3AxY3pCbDVkcjZrbXpSUU9saGtTc1AwdkFSVTd6R05ScVNZMWU4N1VIQm1rUlBZNmNTNXNPdnRFNzk2ckhoZm0wb1A0bklWS0RKWUMxaE43MlFYQVZFQV9BbnNCMWE2bEtsbTdaVVUxZ1ZSVTgzSVRZRndEaWNtSzVHR3pMT1NQMTh1d01LckJlbkVTdE5QWGxTNHVONjNDVUpkRmF6cmtXMjRBT20?oc=5>

### Why Cisco Systems (CSCO) Is Getting Attention Today
- Summary: Analysts spotlight Cisco, boosting investor interest.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNTXl0OEgzYVJMTGFjVXpKOFJXa0pLaGtrbG1sb3dCM3ExN0JPUklWbHBnYml5UGlRYjNkcUVvaExiSU5wQjgyMDJHRjNycTZiSno3bTJ5X1BQVlc1MzY1cDZQdTZ3OWtwbE12YnhlYW5fWm95QnduNHBORy1iM3lxMW1Ma0NyZWZ1QjVLdkpWdDhqTXNsNWp6RE81NA?oc=5>

### What Are Cisco Investors Betting On?
- Summary: Investors are evaluating Cisco’s future prospects amid evolving tech trends.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNbTlIV0hzR19DbUFCSmZrd1czTjlpSGJzbXRsY1VmLTVoODJXd3VCUTd3WVF6WTd1bFFEQU5sMW1PX3Y2TDZ3NUk0WE1mZ0tqSDc5WC1YV3IzNG1WbnFYNFBsOVdYQVRObmlqTUZIWTdDRGFFazJzd200Mkh1ZmI5R2UyVWNKN3g0cXY2OVNBdHBON3YxZ21iVVpyRXg?oc=5>

### Can Cisco Systems (CSCO) Stay Cheap As AI Cash Flow Builds?
- Summary: Questioning Cisco’s valuation as AI-driven cash flow increases.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOcHByUFgyeGJxTllUYXBFUy1rUXY4UEItNFhYVFZXcEY3bVJBUTVOWWxBbEF2X0p6eXFqUVg3aW9FZDF1SU5lSndmcnJnV0gzZmdxUWZzZnNNdUVNR0xqczFoSUU0YW9OeUE2TnZ2YjlXalFFUDNrSmozRXpZWi1rY1NGQ056TkZTMWxDblFPNmVrQTQ1dHYzMmlR?oc=5>

## HEADWINDS

### Here's Why Cisco Systems (CSCO) Fell More Than Broader Market
- Summary: Cisco's stock decline outpaced the broader market due to specific negative factors affecting investor sentiment and company performance.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOd0tuclZqb2tZSGdkdUU3eDM0czVTV2VmZ0JNcUlzOVBKUTNMZ0RIYmpGZEtHUTgxSlVTSU9PQTd6SFA4VGItcUk0RVJPNzRWZnlrNWlzTjYtZVBfZmVNNFhhbmFUMjRVNjlLbmNhclYzbnprLVpSbkhmdzBDZFhRVGFabFMyTU9IaTZGcHFYVFVqbnA3cjJWUw?oc=5>

### ETFs Are Net Sellers of Cisco (CSCO) on Monday
- Summary: ETF selling pressure may weigh on price.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOcm5DOTJTWWF4Q0lJMk5uM3laWHNLSnBta0tWVXNZS1BwSnVkVXZZRnI1Y0dhQktKRGVVSmZvWG55NXZVSXNia0dHR3RHX3pqTThONkdDS21iLTF5V0lRa0Z6MS11SmlZM01TWUNiNUxScG05SHpGMTdFOHU3ZGN5UnNDT0E3cGI1ZVR5c2thLVZKcHVZQldF?oc=5>

### Cisco (CSCO) Options Traders Show Cautious Sentiment Ahead of Ea
- Summary: Options traders wary before earnings release.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNV3pFQzlwSDRnaVkyTWRyNFBaUzF1LUVBaG0yV21xYk1JRG85OWVjYkxzaWE1ZFpNOEROR1liaE9vbHVXdzQwSjUyLVlVQjBZakY3WXF6eS02dDU2bzdlRFBxXzZaNTh0dy1BeEpTQmdmYTExSjRwRkMxbEdFT2NQX1RBbWgwYTZyUng2cGFNT0VJTjQ0cW9lQW5tM29qTXpBUXZoNXVVaUtMOUk?oc=5>

## CATALYSTS

### Cisco Systems, Inc. $CSCO Stock Sold by Arnhold LLC
- Summary: Cisco Systems, Inc. $CSCO Stock Sold by Arnhold LLC
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPT2NOWW1sVFZlMUdTcm90NHFUTEUzNUVsMTBUdFg2NEdtbnBnZ2pTZFZVVzBhYmlLZXFCdzlUYlpzWE5aVVpFUlB6V0s5Y2VDS3ctUTVNYjNVaElDT2J5d0wwaEJVaEtybUt1c1VaX0FkTG5ybFVTTnd6N1FNN2hXZFJfWFRwa1ZNTnNMTDVTYzRMZ1JZZnQwSTZiRlN1VVFoNlVScFJtb0ttOHNmOFE?oc=5>

### Cisco Is Up 47%, IBM Is Down 13%. Which Dividend Stock Is Better for Retirement?
- Summary: Cisco Is Up 47%, IBM Is Down 13%. Which Dividend Stock Is Better for Retirement?
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPWkRMNUdXeDZuWDNGOFlDYkNVMzU3ZmFyY3E0NnhMN1Z0eHAyaHk5XzdubkN6X2FnYm05Ym1GQWc2Tm1OaTFzRkVESUNyRTA5V01IWjA2SlJJLS05R1FFNzVjZWZHeVBfSGJqWC1NT2JsQ2Z3TktXMGw0ZjVmZkpaenNXYzNmMm93Z3dSQUdNZHU3aFFJbzZnc3hkUUxmUGtFVnVRQ1JBOTRvSThQalFneUVaX19nbGdPZng4?oc=5>

### Cisco Systems, Inc. $CSCO Shares Purchased by Apollon Wealth Management LLC
- Summary: Cisco Systems, Inc. $CSCO Shares Purchased by Apollon Wealth Management LLC
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxPOGlNdXVSN25pRVdiV0pkdEdwZGItc213T0g4eXdfeWNvOXFIMGZkRHg2M3VyaV9oR2RpZWtmVU5Fb0I1enV5eUlsMTd2LUJEbDVEQjFWRDFobWI5dEswTDZXOElNQl9rN2FldW91NzJFYWtzY0lfejVWTHBKWUkycks3VFd2V1p3Tl8tREZCQWdYNGFQUDdZanRPOVltNVBjZVQyNWtQV0lqSTFnbm11SEZyd2hfQ0lBbDhNQ0lGUjU3dXF4YXpqdE9MQmkzQQ?oc=5>

### Did AI Networking Expansion Just Shift Cisco's (CSCO) Investment Narrative?
- Summary: Cisco's AI networking expansion may alter investor perception, potentially boosting demand for its networking solutions.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOQW5kYV9YR1ptZTJpOEV4VDhCdXBERFI0TWtCd2oxSGhXTFlnZm5FZktyOFNFUmRuQ0VJYzQ2RTBEX29uRUVzellhV2ZmWld2dEhVS3BxWmd5NnhVZndSUER5ODVXbTJrQnJ5RUpCRUNYQXZScHNTOHB0WFdZaGtpakdSTDZLcTFVd1I3aVZES2RjZ0RsQ3d5Qm1lN1M?oc=5>

### Cisco Systems (NASDAQ:CSCO) Shares Break Above Fifty Day Moving Average - Here's What Happened
- Summary: Shares surpassed the 50‑day moving average, indicating a short‑term bullish trend.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxNd2ZhYzVVLWZPN3JZbVBlVHpCdXdmNnNKWXJMa1dsNkVnRmVRellxQnZTenZ1aEp0N0JOUGhwMkFPTFlpQjVHNk9aTFM4VTYzd2JwUmJMQ0dSWDJoMFFGaWYtMF9nemM0RGlMcGFkQkppTWh3bVhnNDBkTEZtT3o2MFlTME4yYWtTSkFHNHJ0ZFRvSDFPNnZFSEZrWGVNdC13R0lHYldOYUdrTjF2NHBrZUctN3d4UllDTEEtT0hRRXBIVFhKVEtCRllIZnB4ZVZ3YWFjY1Jfd2VQUzB6Vy1UQUNJNA?oc=5>

### 31,948 Cisco Systems, Inc. $CSCO Shares Sold by Sterling Capital Management LLC
- Summary: Sterling Capital sold 31,948 shares, reflecting a short‑term market move.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQM3BuVHRsckRsR3NkV2lUOWxjUjNDMEprcUx1T0hQTWtQQ0F3OGV3S3htYzFOZ0dwNmVJaWRzOU4zR0dJWWd6eUIyZFZ2MDRFVTFERVo5ZlJ2NHpHVm9Sc1dMVDRQWWdvakx3LVd2QWM2Yjh1clpzSjVpZDRJY3A4Q1FjRXQwYjQ5dm1Gd24tYlU3Sl9mMnBrcmdteTduUGRfcXo0N1ljaHJTaWVKcTd3ZjMteWEyRVowLWU4SERPbmJZQnVZRUVELTZOR0VmYmx2bWc?oc=5>

### 16,889 Cisco Systems, Inc. $CSCO Shares Sold by Hourglass Capital LLC
- Summary: Hourglass Capital sold 16,889 shares, indicating a short‑term market move.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPYlMtUXEweEVsQXR1Y094R1FlZzFqTGtFdjI5Z0UzNjBTVHJWVXR3Y1FqdEtObFJGVjJ5b1J2N0U0RVZhZ1NDRHJabmNfU09rc2p6bzRkQjhOOVgydUM4MFlJOGZqb09SYlNRNUFyUm14M2NCM2pDYTJ4Y1RkcDdsTE4tbFJWNk4xbFk1TUJCTjh2akFialUyUzMxaFQxU0FSUUp5c0JlYkFjYTZ2a3JabWw5UV9peFdUeHFzVkRraGVkMjZG?oc=5>

## RISKS

### Wells Fargo (WF), Cisco (CSCO), Marvell (MRVL) join objections to OKX-ICE tokenized stock plans
- Summary: Cisco joined a lawsuit against tokenized stock plans, potentially facing regulatory scrutiny.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNekc1MnU3Uktka3JVcEpxem1xS0UxaGZVQzcwQTVBWHNQd01PUHNJMzdBa3Y4UFB6SkVlRTljOHJzYnZIS045eklhNlFtTDJFd3llSXJBS0x5VFNialdLMm5CVDhSTTBVa1lkcmxab1ZoQVZ0ZUhTZXl5ZWs0T0FFZUxIT0pvcmh1TjRLVUxGdG9Dd1JjQjVYdmRmaEdSdnl0Nk55aWxmMU5uX0NaN1hyU1g5NjJEOXoycGJWRzV1VXE1VGppS3lHOWd1TDc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **33.42** | **8.65** | **24.14** | **17.60** | **434,827,919,360.00 USD** | **54.68** |
| ANET | 58.90 | 15.91 | 47.88 | 37.70 | 235,495,882,752.00 USD | 19.10 |
| FFIV | 29.20 | 5.39 | 26.71 | 10.90 | 20,698,935,296.00 USD | 36.61 |
| HPE | 31.10 | 3.02 | 13.68 | 33.70 | 80,085,958,656.00 USD | 153.27 |

Peers fetched as_of: 2026-10-28; CSCO reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-12
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

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

- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPVkk4QjBXZV9qdDF2SE5pQlVyaEFYVFZsZTNJd24wSUk0UU9jSWJCX2NNaUItQlAzT05oMnZ2dF9CdFp2eTNnbVFmbHp0U3k2bnkwTXo4ajBieTBBZE5pUWtZVEY3TnpudmNHeWlDTXZ5Rkd2dlBuS1A2TmZJMV8xRHRfZVFuSlVJS2tzLTdieUtVV0Q3VWNPM0FHdmtKT0ViLURSYW1KeXJRVHp0SWxCRWRnT2gzSUJE?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQNEhvdnlwR1h1Q2hiZWdXS2xpdFdUak92TndqUnlMbk5sLTQzRzE1WXhDY0R3a20zczBQRzNIcjVKck9PSDd3QkVZSVBNQV8wRUNmLU0wUWc1aG90bDFWb0FMWjQ1dWRUWkJhZUZJT3dPdXYySWZpWnVsQWRyTlY1M3ZhOEs3eEIzb3pvcWhOSUwxOTZxWGV4QU9XdGhMYXhBN3AzZzRCdFdZRzRZLXRN?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOODJoejlkSmVnYnNFQVVVcm1rOHVhbWtjWmx3ZUxFcDRhVmNMSnNiUm5RY0lybGhlTkJNRmdiaGJ6d3ZiTFVQQ1BCa0FmSzgyZlhsQU1EY2ZEdU9DeTFsZ1hCQkVJbGhKbWxERWN4aFllUndPOFN0MTZRTGNjUnF1YWV0eEV0aWM5aE9JclpicHM1YmJTYks2UFk2ck9FbUNaQk52YlVwVXFzX2V5MjZiSlBYdw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQMHVMVktpVGhyY0VnMzN0akozZWs4dTF2WHc5eXkyREtnc2dyem5zcERqYV9rSUN1Z0psQzV5V0NOMUl6X3kzSUNHTy1PS2dNYW5MaVctNENMVWVQdmZYeU93b0dodzBuWWhIa0J2R3cwOEFCZ3pQUnAtWS1UU2pBNWhLd1A0X3loel90amFLUW9qa2JjSDZWZEVNWGJocG8?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOZ201RTRRZnMxdG5ZTFZFcHU2a0c0RzNvUGtaX3VlYnB3cHBidjdTTnEzQkZCLU5YZ3d6X2lIa2RYVElFQlkyUkdNNUFCRHFCQklUTGQweGt5bzBCNDVaSGdhellUbGJpSDJ5SGFieTB1U0gzRV9SOTJXblcyRl9hRTNVY0pNMXc4LXhuclFhTWNHNWxxSF9Ib3p2d0hEQQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxONmU1YzJ5ZkdkYWpKbUYzWFRzR3AxY3pCbDVkcjZrbXpSUU9saGtTc1AwdkFSVTd6R05ScVNZMWU4N1VIQm1rUlBZNmNTNXNPdnRFNzk2ckhoZm0wb1A0bklWS0RKWUMxaE43MlFYQVZFQV9BbnNCMWE2bEtsbTdaVVUxZ1ZSVTgzSVRZRndEaWNtSzVHR3pMT1NQMTh1d01LckJlbkVTdE5QWGxTNHVONjNDVUpkRmF6cmtXMjRBT20?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNTXl0OEgzYVJMTGFjVXpKOFJXa0pLaGtrbG1sb3dCM3ExN0JPUklWbHBnYml5UGlRYjNkcUVvaExiSU5wQjgyMDJHRjNycTZiSno3bTJ5X1BQVlc1MzY1cDZQdTZ3OWtwbE12YnhlYW5fWm95QnduNHBORy1iM3lxMW1Ma0NyZWZ1QjVLdkpWdDhqTXNsNWp6RE81NA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNbTlIV0hzR19DbUFCSmZrd1czTjlpSGJzbXRsY1VmLTVoODJXd3VCUTd3WVF6WTd1bFFEQU5sMW1PX3Y2TDZ3NUk0WE1mZ0tqSDc5WC1YV3IzNG1WbnFYNFBsOVdYQVRObmlqTUZIWTdDRGFFazJzd200Mkh1ZmI5R2UyVWNKN3g0cXY2OVNBdHBON3YxZ21iVVpyRXg?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOcHByUFgyeGJxTllUYXBFUy1rUXY4UEItNFhYVFZXcEY3bVJBUTVOWWxBbEF2X0p6eXFqUVg3aW9FZDF1SU5lSndmcnJnV0gzZmdxUWZzZnNNdUVNR0xqczFoSUU0YW9OeUE2TnZ2YjlXalFFUDNrSmozRXpZWi1rY1NGQ056TkZTMWxDblFPNmVrQTQ1dHYzMmlR?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOd0tuclZqb2tZSGdkdUU3eDM0czVTV2VmZ0JNcUlzOVBKUTNMZ0RIYmpGZEtHUTgxSlVTSU9PQTd6SFA4VGItcUk0RVJPNzRWZnlrNWlzTjYtZVBfZmVNNFhhbmFUMjRVNjlLbmNhclYzbnprLVpSbkhmdzBDZFhRVGFabFMyTU9IaTZGcHFYVFVqbnA3cjJWUw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOcm5DOTJTWWF4Q0lJMk5uM3laWHNLSnBta0tWVXNZS1BwSnVkVXZZRnI1Y0dhQktKRGVVSmZvWG55NXZVSXNia0dHR3RHX3pqTThONkdDS21iLTF5V0lRa0Z6MS11SmlZM01TWUNiNUxScG05SHpGMTdFOHU3ZGN5UnNDT0E3cGI1ZVR5c2thLVZKcHVZQldF?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNV3pFQzlwSDRnaVkyTWRyNFBaUzF1LUVBaG0yV21xYk1JRG85OWVjYkxzaWE1ZFpNOEROR1liaE9vbHVXdzQwSjUyLVlVQjBZakY3WXF6eS02dDU2bzdlRFBxXzZaNTh0dy1BeEpTQmdmYTExSjRwRkMxbEdFT2NQX1RBbWgwYTZyUng2cGFNT0VJTjQ0cW9lQW5tM29qTXpBUXZoNXVVaUtMOUk?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPT2NOWW1sVFZlMUdTcm90NHFUTEUzNUVsMTBUdFg2NEdtbnBnZ2pTZFZVVzBhYmlLZXFCdzlUYlpzWE5aVVpFUlB6V0s5Y2VDS3ctUTVNYjNVaElDT2J5d0wwaEJVaEtybUt1c1VaX0FkTG5ybFVTTnd6N1FNN2hXZFJfWFRwa1ZNTnNMTDVTYzRMZ1JZZnQwSTZiRlN1VVFoNlVScFJtb0ttOHNmOFE?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPWkRMNUdXeDZuWDNGOFlDYkNVMzU3ZmFyY3E0NnhMN1Z0eHAyaHk5XzdubkN6X2FnYm05Ym1GQWc2Tm1OaTFzRkVESUNyRTA5V01IWjA2SlJJLS05R1FFNzVjZWZHeVBfSGJqWC1NT2JsQ2Z3TktXMGw0ZjVmZkpaenNXYzNmMm93Z3dSQUdNZHU3aFFJbzZnc3hkUUxmUGtFVnVRQ1JBOTRvSThQalFneUVaX19nbGdPZng4?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxPOGlNdXVSN25pRVdiV0pkdEdwZGItc213T0g4eXdfeWNvOXFIMGZkRHg2M3VyaV9oR2RpZWtmVU5Fb0I1enV5eUlsMTd2LUJEbDVEQjFWRDFobWI5dEswTDZXOElNQl9rN2FldW91NzJFYWtzY0lfejVWTHBKWUkycks3VFd2V1p3Tl8tREZCQWdYNGFQUDdZanRPOVltNVBjZVQyNWtQV0lqSTFnbm11SEZyd2hfQ0lBbDhNQ0lGUjU3dXF4YXpqdE9MQmkzQQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOQW5kYV9YR1ptZTJpOEV4VDhCdXBERFI0TWtCd2oxSGhXTFlnZm5FZktyOFNFUmRuQ0VJYzQ2RTBEX29uRUVzellhV2ZmWld2dEhVS3BxWmd5NnhVZndSUER5ODVXbTJrQnJ5RUpCRUNYQXZScHNTOHB0WFdZaGtpakdSTDZLcTFVd1I3aVZES2RjZ0RsQ3d5Qm1lN1M?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxNd2ZhYzVVLWZPN3JZbVBlVHpCdXdmNnNKWXJMa1dsNkVnRmVRellxQnZTenZ1aEp0N0JOUGhwMkFPTFlpQjVHNk9aTFM4VTYzd2JwUmJMQ0dSWDJoMFFGaWYtMF9nemM0RGlMcGFkQkppTWh3bVhnNDBkTEZtT3o2MFlTME4yYWtTSkFHNHJ0ZFRvSDFPNnZFSEZrWGVNdC13R0lHYldOYUdrTjF2NHBrZUctN3d4UllDTEEtT0hRRXBIVFhKVEtCRllIZnB4ZVZ3YWFjY1Jfd2VQUzB6Vy1UQUNJNA?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQM3BuVHRsckRsR3NkV2lUOWxjUjNDMEprcUx1T0hQTWtQQ0F3OGV3S3htYzFOZ0dwNmVJaWRzOU4zR0dJWWd6eUIyZFZ2MDRFVTFERVo5ZlJ2NHpHVm9Sc1dMVDRQWWdvakx3LVd2QWM2Yjh1clpzSjVpZDRJY3A4Q1FjRXQwYjQ5dm1Gd24tYlU3Sl9mMnBrcmdteTduUGRfcXo0N1ljaHJTaWVKcTd3ZjMteWEyRVowLWU4SERPbmJZQnVZRUVELTZOR0VmYmx2bWc?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPYlMtUXEweEVsQXR1Y094R1FlZzFqTGtFdjI5Z0UzNjBTVHJWVXR3Y1FqdEtObFJGVjJ5b1J2N0U0RVZhZ1NDRHJabmNfU09rc2p6bzRkQjhOOVgydUM4MFlJOGZqb09SYlNRNUFyUm14M2NCM2pDYTJ4Y1RkcDdsTE4tbFJWNk4xbFk1TUJCTjh2akFialUyUzMxaFQxU0FSUUp5c0JlYkFjYTZ2a3JabWw5UV9peFdUeHFzVkRraGVkMjZG?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNekc1MnU3Uktka3JVcEpxem1xS0UxaGZVQzcwQTVBWHNQd01PUHNJMzdBa3Y4UFB6SkVlRTljOHJzYnZIS045eklhNlFtTDJFd3llSXJBS0x5VFNialdLMm5CVDhSTTBVa1lkcmxab1ZoQVZ0ZUhTZXl5ZWs0T0FFZUxIT0pvcmh1TjRLVUxGdG9Dd1JjQjVYdmRmaEdSdnl0Nk55aWxmMU5uX0NaN1hyU1g5NjJEOXoycGJWRzV1VXE1VGppS3lHOWd1TDc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
