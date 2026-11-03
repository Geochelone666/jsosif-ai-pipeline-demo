# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:37:14.045690+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 5, 'ai': 15, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 8 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 101.6100 |
| Return 1D (%) | -2.7749 |
| Return 1W (%) | -7.8284 |
| Return 1M (%) | -9.4385 |
| Return YTD (%) | 34.3517 |
| Return 1Y (%) | 41.5554 |
| Annualized volatility (%) | 35.8046 |
| Beta vs SPY | 1.1698 |
| Max drawdown (%) | -21.2419 |
| Sharpe (rf=0) | 1.1066 |
| Downside deviation (rf=0, %) | 24.4419 |
| Sortino (rf=0) | 1.6210 |
| Historical VaR 95% (1D, %) | 3.0039 |
| Historical ES 95% (1D, %) | 4.9898 |
| Correlation vs SPY | 0.4189 |
| Tracking error vs SPY (%) | 32.5843 |
| P/E (trailing) | 30.51 |
| P/B | 7.97 |
| EV/EBITDA | 22.31 |
| Revenue growth (%) | 17.60 |
| Forward P/E (estimate) | 18.07 |
| Gross margin (%) | 64.52 |
| Operating margin (%) | 27.72 |
| Return on equity (%) | 27.32 |
| Free cash flow yield (%) | 2.79 |
| MA50 | 109.5747 |
| Close vs MA50 (%) | -7.2687 |
| MA200 | 100.6615 |
| Close vs MA200 (%) | 0.9423 |
| RSI (14, Wilder) | 35.5404 |
| MACD (12,26) | -1.3905 |
| MACD signal (9) | -0.6933 |
| MACD histogram | -0.6973 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 101.6100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.7749 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.8284 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -9.4385 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 34.3517 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 41.5554 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.8046 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 24.4419 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6210 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0039 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.9898 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4189 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.5843 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.1698 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.2419 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1066 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.0735 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.5240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.7190 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.3190 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.7914 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 30.5135 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 35.5404 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.6973 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.2687 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 0.9423 -> Slightly above the moving-average trend level.

## TAILWINDS

### 43 ETFs Add to Cisco (CSCO) Holdings on Oct. 28
- Summary: 43 ETFs increased Cisco holdings, indicating positive investor sentiment.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOb0Y3NTh0Y29ZZmlvREUtOUdkd1pCem5lSUd0X201QWdNRHZEVFp4bzBBbDJpc1ZmYVY5eVdJTkNlNGV0aGd1c1FPVFAwVXA5RmtReXg2VHZQdkpUQThHS19XcVNMYXRiQVZLY0ZhdFpjNnVOVjYtajBlZmMxek9vXzZYdWRJWGJCSUQwWUtiMXE?oc=5>

### Can Cisco Systems (CSCO) Stay Cheap As AI Cash Flow Builds?
- Summary: Questioning Cisco’s valuation as AI-driven cash flow increases.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOcHByUFgyeGJxTllUYXBFUy1rUXY4UEItNFhYVFZXcEY3bVJBUTVOWWxBbEF2X0p6eXFqUVg3aW9FZDF1SU5lSndmcnJnV0gzZmdxUWZzZnNNdUVNR0xqczFoSUU0YW9OeUE2TnZ2YjlXalFFUDNrSmozRXpZWi1rY1NGQ056TkZTMWxDblFPNmVrQTQ1dHYzMmlR?oc=5>

### What Are Cisco Investors Betting On?
- Summary: Investors focus on Cisco’s strategic moves, suggesting optimism.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOTmJEZHBsazUwU2hHbnEwZVZfNlNSTzV5R3QwQUdUV3haV1Z5dUJKSjFGNDhoS1plTGFaWjVNRmZCWWdiZzF6VldReDBuRUNtb0o0RWFSaUlQcVFQY3hXdnRmQXNHeXRQRmVlNllIQWhOdUE3WXM3X01hb2dpUGRxeDNUNzV5Mzhwam12M1BRbDFCQQ?oc=5>

### Cisco Gains From AI Networking Boom: Can It Outpace HPE & ANET?
- Summary: Cisco benefits from AI networking surge, potentially surpassing rivals.
- Date: 2026-10-29 | Impact: high | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPR1QxblFweHdxYlBzMmFDWFQxRGNvWWQzZnpVVm9sSHlvVXFLcktyQllaT3h4UG1Tdlk5TjBEUzhQaXdiWG1JaUN4WVhIaGJIb1BkM2dlZ05DdEplaFdEUlhqdVNNTzE3Wl9BeHduZHY3bHBacXNvaFZhNDhxcWM4di10RXhjQ3hEeF9sN1ZfZERKQUZ4VkhwTjNn?oc=5>

### Cisco Raised AI Orders to $9B — So Why Is the Stock Stuck Below $124.62 Resistance?
- Summary: Cisco increased AI orders to $9B, indicating strong demand for its AI solutions.
- Date: 2026-11-01 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxPT2lKcWZzd0M3R2RBb05UTkUzNUVidXhRYTZQZmNVM2d1OGhBcFJ3ZkFvVmxFaF81NHVIQjYycVlnV0I2RGxMb1c5T3RYLXl4VVhEeGJGdDBHR2RmRmgwNnh1bnpqOVhuTTk4em1CbGFUMUg0MzRhNWdwNW9QaGFweW90ZDJDOHpqT2pKOUJPR29LWjJxMHc0R2JHSkJrNDdfZHNiakJrQ0xyejZMNnNlRzEwZEtpc1pESU1xUXlPdVZwbWNGN2E5OTZBWmUyd2xKSmRWcVJjS2VHd1M0ZHhOZEtBQQ?oc=5>

### Cisco (CSCO) Options Traders Show Cautious Sentiment Ahead of Ea
- Summary: Options traders are cautious ahead of earnings, indicating potential downside pressure.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNV3pFQzlwSDRnaVkyTWRyNFBaUzF1LUVBaG0yV21xYk1JRG85OWVjYkxzaWE1ZFpNOEROR1liaE9vbHVXdzQwSjUyLVlVQjBZakY3WXF6eS02dDU2bzdlRFBxXzZaNTh0dy1BeEpTQmdmYTExSjRwRkMxbEdFT2NQX1RBbWgwYTZyUng2cGFNT0VJTjQ0cW9lQW5tM29qTXpBUXZoNXVVaUtMOUk?oc=5>

### 22,913 Cisco Systems, Inc. $CSCO Shares Sold by Heritage Investors Management Corp
- Summary: Heritage Investors sold 22,913 shares, a modest institutional sell‑off.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQcWpwNjhHc0IwcHpoY2JqZ0tyYU05ZGNrbDVGdzY4bndGMzlNYTVNR2hKUGdjU1hmdEV2aW5CZ2szRjd3WGFwUXJ1ajdFZmY4bmFuZ192MVVZejFOazNRY20xeURrV2h4RVlBMlFibHNmRDNYaDJlSGtGa3M4MzBnQTdIdUYwOGM3dlN2Uk5kakk0OXozdTdSM0NkdEhrckNZM190NDA0VWlkS0l1aVlFRG5mZ1VMYW4tancyVnNYNEpSY3BianhFTTZWNmptcDFHUzNyR0ZR?oc=5>

### Bank Julius Baer & Co. Ltd Zurich Sells 1,048,348 Shares of Cisco Systems, Inc. $CSCO
- Summary: Julius Baer sold over a million shares, a significant institutional sell‑off.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxOZ3lKWkhhb0hsRGlab2ZlMkNLRkNqcHR1YjlIOW00Zk1qSkliT3UwTVF1RFVDTXRLX0FPVllDZXVSdl8yNEtuTVVFQWZaX0F0RGNOeE5ka1VoRE8wU0l3OUVMcm9ZWWxHY1hzYnRGbVJwcmpqb2ZMWmpBeUFhMGZSVFN3NnI3MjFMZ2h3OG52VXN2OUdlbzY2Zk1zdlY3anhaLWQ2bkZxSFFibHJyT1o2MzdHR3QtRGR6Vkx0bklGMUQ5YjFjV1RaQjh0U0lqV1U4TDJrNQ?oc=5>

## HEADWINDS

### Cisco Systems (NASDAQ:CSCO) Stock Price Down 2.8% - Here's What Happened
- Summary: Cisco Systems (NASDAQ:CSCO) Stock Price Down 2.8% - Here's What Happened
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPNm1MTERFbkduR2VwaFBIdENsVFNDMkgteGVmV2xHSEd6c1djRTZyYzBTRFNQY2dJZmwxN0xIOE1GbEwxRThjMXpyV2NUeFY3Z2dRZEVYZE1aUU9jcGtha0hZYWtzbTloNE5jYTRrQXE1NUUySUxNbmswTk5aUl9VZk1rRWhubDFRNHZnb0MyT0JFeElLVjc4Vi1zRDVwb0MzT1NJQ1BmaGJSQlJGU1pBZDhzTlZGb0E5OTBvT2t5dnBfQTQ?oc=5>

### Cisco Systems Inc (CSCO) Shares Fall 3.8% -- What GF Score of 88 Tells Investors
- Summary: Cisco Systems Inc (CSCO) Shares Fall 3.8% -- What GF Score of 88 Tells Investors
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOeGk2UUJEUDdQZURYT1BlaVBaQ01ibkU2Ujk5d0NTNzNPZnU0TjlLWWxFWWpGcEwyWDFNX3UtY1NLT05UQ21CdGEzTTE1Z0F6QU44S3paS1BWSWdMemExMkVyQmlDbGQ4Mnc4a0pRME41QUFTYWQxMjExZUwxS1Ztb2RPM01hQ2lmYks5akF5d29RanNPMTZvOW9wbXlhY0x5RzRieXpkR0xfNFJhWVNyYUVR?oc=5>

### Why Cisco Systems (CSCO) Dipped More Than Broader Market Today
- Summary: Cisco stock fell more than the broader market today.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPTGtSaFE3OVRZdGp1MzdnWm1OWEZDYlpzZUMxUGlPaHVsRVVWZ2gyWENCTFk4dHJKMk9WdEgxdHRjeHFCVXNPbjNTOGExTlZJMDlDSXhZZmctUFpxSW1pZW9ISnFkUkUwcElKT1JfRDg2Z3UxVzR6WGw4bjJraVJ2SlhnYjZDcnJvdGpvNGY0RnhzZ1RYNFZxVDNR?oc=5>

### Cisco Systems Inc Stock (CSCO) Moved Down by 4.09% on Oct 30: Drivers Behind the Movement
- Summary: Stock fell 4.09%, reflecting short-term pressure.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNV05jeWZSZzZFU0JtbzRaZW5acXl3eHVqVUtRX0ZUamE4V1JyQ18yY0lmV2EzUEdkMWVoN2k0dkVMSk5JZ1pIeVlSRVVGalc3NDE1azMxSkR6LUZkMl9CM091NE54ZHZWbVY0VkJodm1mNGRORWNGa1NhbWhrZVpldzFqQzVOQW8zZlVv?oc=5>

### Cisco Systems, Inc. $CSCO Stock Holdings Cut by Sumitomo Mitsui Trust Group Inc.
- Summary: Sumitomo Mitsui Trust Group reduced Cisco holdings, indicating potential concerns.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxOYmx6c084bzR4WEZmS0tveDEwUHVzeENzVDhzS3JTM0IxWW1tM3VJT1NCOGpDWnYyRVdjZS1yZGZ5RGJnOWRSeXFwTzFMQ2JWZUw3UE1mZW0xN2ptNDdTU0xGVVJFeXdTZzFFWWFkVWpmWEN4cEw1S0YzUG1Fc1IxbVFMajlrWTg2VW1vN3FPNmNKeUpJSVI0RTYwdGNjWEo0Q1ZKazBWcW5jMkJmSlIwS2o1NzVXbUtESkZ1RW1LanFWaXNZbzBsb3JPYnJTWDJRM2pN?oc=5>

### Cisco Systems (CSCO) Stock Dropped, So What Is Driving Attention Now?
- Summary: Cisco stock fell, raising concerns among investors.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxOejhROHprSi11clBoVVFhX0Y5TXB0UkFIbGZOS0tfa1NTNU1IbndrRE5IRU1LTXBTV1BtN2FJSHZVcTREYXhFODVoYnpEU2lQUElJaTF1d0VhUzEzd0JiaWRMdzFiR3c5T3RYTlhpQzBoQl93ZHpaZks1QUpFNXdkaWZVUnNEdkRxZlVrWWZaWmdCSlNqSFpYRzBPMWFYem9HRWFPVEJaTzRNMk1jSlIwcE1kOGhBMzZmeHJqUjItVmZmOG5uNXZIQnc5Yi3SAcwBQVVfeXFMTno4UTh6a0otdXJQaFVRYV9GOU1wdFJBSGxmTktLX2tTUzVNSG53a0ROSEVNS01wU1dQbTdhSUh2VXE0RGF4RTg1aGJ6RFNpUFBJSWkxdXdFYVMxM3dCYmlkTHcxYkd3OU90WE5YaUMwaEJfd2R6WmZLNUFKRTV3ZGlmVVJzRHZEcWZVa1lmWlpnQkpTakhaWEcwTzFhWHpvR0VhT1RCWk80TTJNY0pSMHBNZDhoQTM2ZnhyalIyLVZmZjhubjV2SEJ3OWIt?oc=5>

### ETFs Are Net Sellers of Cisco (CSCO) on Oct. 29
- Summary: ETFs sold Cisco shares, adding selling pressure.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNSXRNZGJ1RmNMZUQ3M0p5dzlrSnNjUDAzYUhXNGh0ZGRJODduX3hHSWlDS1hrb3BVRGVpWXNnOHpRZmN4S1BUU1IwMWFfQlBvQ0ZraV9aQml5Zk5XRlR1TUlGdm9fSGFWbHIxWF83V0ZYNFQzWUE1WHRTQ2piMnkxSHF5LWdqakxnVGJEY09ZUHpld1RtdnFR?oc=5>

## CATALYSTS

### Cisco Systems, Inc. $CSCO Shares Sold by Welch Group LLC
- Summary: Cisco Systems, Inc. $CSCO Shares Sold by Welch Group LLC
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOR1o3WjZHSmU2MmNuRDFOUDhFX0hIaTNDRHdXSTRVVDJaZHZwUzRONXd6eXh2VW9scjFmNm5QRDB1b2RLSUhBc2JDUmE0MkFnbDY5T1RHaFVyMTlKajRRR2FPU0tzUkhLaG1NT0FJNjEzR3VxZmoxeDZxV0ctVmhlQ0hVTm9oVlc5NFdfbVNua2VBQjFuVGgtNUhQY0h6bjg5OGRWYmRHTW0yQWptbV9XQmFRUHY?oc=5>

### Cisco Is Up 47%, IBM Is Down 13%. Which Dividend Stock Is Better for Retirement?
- Summary: Cisco Is Up 47%, IBM Is Down 13%. Which Dividend Stock Is Better for Retirement?
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPWkRMNUdXeDZuWDNGOFlDYkNVMzU3ZmFyY3E0NnhMN1Z0eHAyaHk5XzdubkN6X2FnYm05Ym1GQWc2Tm1OaTFzRkVESUNyRTA5V01IWjA2SlJJLS05R1FFNzVjZWZHeVBfSGJqWC1NT2JsQ2Z3TktXMGw0ZjVmZkpaenNXYzNmMm93Z3dSQUdNZHU3aFFJbzZnc3hkUUxmUGtFVnVRQ1JBOTRvSThQalFneUVaX19nbGdPZng4?oc=5>

### Cisco Systems, Inc. $CSCO Stock: Modera Wealth Management LLC Lowers Stake
- Summary: Cisco Systems, Inc. $CSCO Stock: Modera Wealth Management LLC Lowers Stake
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxQaW12a0pmQmYtZUlPOUZmX09GaXM4MTBoRV9jRHNsbEVhaU4yOUo5S1RpN2RHc0FIU1l3UHRtMktrSnowc3NrUFByNXhkRXlYY3c1bkJKbVFHWTVFclVEdlZzZmJ5ZkdhVEhEWF80VzdHVWdUWHBLZnFwUXhWV3NhdFJkVFd0amc3NE5ha3NvOVBlaUJpZkJ4QTFFRlRFLURoY3hPY0I4czc2YmdtSHhGLWh3OGtxSFVxRlVZdTBQTjR2RVcza0wwTFNSZw?oc=5>

### Cisco (CSCO) Stock Looks Undervalued On Future Cash Flow Estimates
- Summary: Analyst suggests Cisco stock undervalued based on future cash flow estimates.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNRkVmNHFuMzZObmVHRkpVOEZZNFJmT3ZKQ0NGYjBtdTBQVFIwbko0Mk53UnFfNU05dTRPdE9MWXRKZWhjbVJ2dXJOdzJFaXBHWkNuZWxvNGRha0lKQ0o5OG82WXVpN0o2azdRV2dCQ3R1WE80QjB0dDUteTZjTG5NRU9YQWE1MFI5clJQaWIyUTNsXzBvVVpaM29FdjJZSlZ5QTlqSDdJc05zMmU2LVJzazVtMWlXcENGU0dGTzBCSEtxQXljNTdj0gHMAUFVX3lxTE1oM0RXNVdySG1lbmpDZ2gyYWpSNmFGRGdjR21kd3NHOURpZXFSTUdjMDVMaDJFc0c2emtWXzRfTnE2ckdoYjFjMjVMMWdQTTFmRUFQQy0zOFZwallqX1lhelQ0MHNmaGR0Mk5BTXRDM1lfSFNvX216UXlwVk1YaTktampMQXRseDdYdXhFcTEybzdFZmNNQzJEdmVOTVNQM0tMZllMZ05nVDBEUkhNUEpGS3JtSkp1bllURDE1SnZfOXZ5THRRbGRIdlNQZg?oc=5>

### Cisco Systems, Inc. $CSCO Stock: Parcion Private Wealth LLC Boosts Position
- Summary: Parcion Private Wealth LLC increased its Cisco holdings.
- Date: 2026-10-31 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxORl9NbF9KQVNuaGlrRFR1UG1KUFZTYlg2SnFPbWl5aHhMZDZFQnBueURSY3ZobFJxZlVVS0ZEb1lLNkFpY2xvWjk4bVoyNzZzcnFhd0tZMHplTDRWYXRUNXgxSURxdTJuWVFoemU5S2w0QzFQeEhndW9VT1ZiLV9pT3lQMDcyc25xYnZSaE85QzN5V0VBRUlNYVllSFJ6WXBTajFwZFlsZEY0Rmc0UkVsbVJvRm0zYmFzMV9jdEVBS2JkU2tRRGJGdTZIajM?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **30.51** | **7.97** | **22.31** | **17.60** | **400,606,265,344.00 USD** | **41.56** |
| ANET | 53.29 | 13.99 | 41.74 | 37.70 | 207,017,426,944.00 USD | 4.09 |
| FFIV | 27.00 | 4.60 | 18.43 | 13.30 | 18,438,008,832.00 USD | 28.26 |
| HPE | 28.44 | 2.56 | 11.92 | 33.70 | 67,952,922,624.00 USD | 113.40 |

Peers fetched as_of: 2026-11-02; CSCO reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-12
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMikAFBVV95cUxOb0Y3NTh0Y29ZZmlvREUtOUdkd1pCem5lSUd0X201QWdNRHZEVFp4bzBBbDJpc1ZmYVY5eVdJTkNlNGV0aGd1c1FPVFAwVXA5RmtReXg2VHZQdkpUQThHS19XcVNMYXRiQVZLY0ZhdFpjNnVOVjYtajBlZmMxek9vXzZYdWRJWGJCSUQwWUtiMXE?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPUUFMR3k0ejVyRnJ1OGNubTMzMkR3S2xvYXpzNEdhVlNVTm0zcURDQzRoMksyWGNxRXZGUUVrdEg3TXlsSk9qZXFqNFZzTHVDdGc2TWdvSHBvdlVXcWt1NzBhVW1mV0MybjJJMFZCMnNpU3JCOEF1TndXcFozM1JmSFFsVGdVajIwX2NvUkR0a2JOcEhNdmUyc3BMQU1YZ0UtMGFsZXFMTQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOcHByUFgyeGJxTllUYXBFUy1rUXY4UEItNFhYVFZXcEY3bVJBUTVOWWxBbEF2X0p6eXFqUVg3aW9FZDF1SU5lSndmcnJnV0gzZmdxUWZzZnNNdUVNR0xqczFoSUU0YW9OeUE2TnZ2YjlXalFFUDNrSmozRXpZWi1rY1NGQ056TkZTMWxDblFPNmVrQTQ1dHYzMmlR?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOTmJEZHBsazUwU2hHbnEwZVZfNlNSTzV5R3QwQUdUV3haV1Z5dUJKSjFGNDhoS1plTGFaWjVNRmZCWWdiZzF6VldReDBuRUNtb0o0RWFSaUlQcVFQY3hXdnRmQXNHeXRQRmVlNllIQWhOdUE3WXM3X01hb2dpUGRxeDNUNzV5Mzhwam12M1BRbDFCQQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPR1QxblFweHdxYlBzMmFDWFQxRGNvWWQzZnpVVm9sSHlvVXFLcktyQllaT3h4UG1Tdlk5TjBEUzhQaXdiWG1JaUN4WVhIaGJIb1BkM2dlZ05DdEplaFdEUlhqdVNNTzE3Wl9BeHduZHY3bHBacXNvaFZhNDhxcWM4di10RXhjQ3hEeF9sN1ZfZERKQUZ4VkhwTjNn?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxPT2lKcWZzd0M3R2RBb05UTkUzNUVidXhRYTZQZmNVM2d1OGhBcFJ3ZkFvVmxFaF81NHVIQjYycVlnV0I2RGxMb1c5T3RYLXl4VVhEeGJGdDBHR2RmRmgwNnh1bnpqOVhuTTk4em1CbGFUMUg0MzRhNWdwNW9QaGFweW90ZDJDOHpqT2pKOUJPR29LWjJxMHc0R2JHSkJrNDdfZHNiakJrQ0xyejZMNnNlRzEwZEtpc1pESU1xUXlPdVZwbWNGN2E5OTZBWmUyd2xKSmRWcVJjS2VHd1M0ZHhOZEtBQQ?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNV3pFQzlwSDRnaVkyTWRyNFBaUzF1LUVBaG0yV21xYk1JRG85OWVjYkxzaWE1ZFpNOEROR1liaE9vbHVXdzQwSjUyLVlVQjBZakY3WXF6eS02dDU2bzdlRFBxXzZaNTh0dy1BeEpTQmdmYTExSjRwRkMxbEdFT2NQX1RBbWgwYTZyUng2cGFNT0VJTjQ0cW9lQW5tM29qTXpBUXZoNXVVaUtMOUk?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQcWpwNjhHc0IwcHpoY2JqZ0tyYU05ZGNrbDVGdzY4bndGMzlNYTVNR2hKUGdjU1hmdEV2aW5CZ2szRjd3WGFwUXJ1ajdFZmY4bmFuZ192MVVZejFOazNRY20xeURrV2h4RVlBMlFibHNmRDNYaDJlSGtGa3M4MzBnQTdIdUYwOGM3dlN2Uk5kakk0OXozdTdSM0NkdEhrckNZM190NDA0VWlkS0l1aVlFRG5mZ1VMYW4tancyVnNYNEpSY3BianhFTTZWNmptcDFHUzNyR0ZR?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxOZ3lKWkhhb0hsRGlab2ZlMkNLRkNqcHR1YjlIOW00Zk1qSkliT3UwTVF1RFVDTXRLX0FPVllDZXVSdl8yNEtuTVVFQWZaX0F0RGNOeE5ka1VoRE8wU0l3OUVMcm9ZWWxHY1hzYnRGbVJwcmpqb2ZMWmpBeUFhMGZSVFN3NnI3MjFMZ2h3OG52VXN2OUdlbzY2Zk1zdlY3anhaLWQ2bkZxSFFibHJyT1o2MzdHR3QtRGR6Vkx0bklGMUQ5YjFjV1RaQjh0U0lqV1U4TDJrNQ?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPNm1MTERFbkduR2VwaFBIdENsVFNDMkgteGVmV2xHSEd6c1djRTZyYzBTRFNQY2dJZmwxN0xIOE1GbEwxRThjMXpyV2NUeFY3Z2dRZEVYZE1aUU9jcGtha0hZYWtzbTloNE5jYTRrQXE1NUUySUxNbmswTk5aUl9VZk1rRWhubDFRNHZnb0MyT0JFeElLVjc4Vi1zRDVwb0MzT1NJQ1BmaGJSQlJGU1pBZDhzTlZGb0E5OTBvT2t5dnBfQTQ?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxOeGk2UUJEUDdQZURYT1BlaVBaQ01ibkU2Ujk5d0NTNzNPZnU0TjlLWWxFWWpGcEwyWDFNX3UtY1NLT05UQ21CdGEzTTE1Z0F6QU44S3paS1BWSWdMemExMkVyQmlDbGQ4Mnc4a0pRME41QUFTYWQxMjExZUwxS1Ztb2RPM01hQ2lmYks5akF5d29RanNPMTZvOW9wbXlhY0x5RzRieXpkR0xfNFJhWVNyYUVR?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPTGtSaFE3OVRZdGp1MzdnWm1OWEZDYlpzZUMxUGlPaHVsRVVWZ2gyWENCTFk4dHJKMk9WdEgxdHRjeHFCVXNPbjNTOGExTlZJMDlDSXhZZmctUFpxSW1pZW9ISnFkUkUwcElKT1JfRDg2Z3UxVzR6WGw4bjJraVJ2SlhnYjZDcnJvdGpvNGY0RnhzZ1RYNFZxVDNR?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNV05jeWZSZzZFU0JtbzRaZW5acXl3eHVqVUtRX0ZUamE4V1JyQ18yY0lmV2EzUEdkMWVoN2k0dkVMSk5JZ1pIeVlSRVVGalc3NDE1azMxSkR6LUZkMl9CM091NE54ZHZWbVY0VkJodm1mNGRORWNGa1NhbWhrZVpldzFqQzVOQW8zZlVv?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOYmx6c084bzR4WEZmS0tveDEwUHVzeENzVDhzS3JTM0IxWW1tM3VJT1NCOGpDWnYyRVdjZS1yZGZ5RGJnOWRSeXFwTzFMQ2JWZUw3UE1mZW0xN2ptNDdTU0xGVVJFeXdTZzFFWWFkVWpmWEN4cEw1S0YzUG1Fc1IxbVFMajlrWTg2VW1vN3FPNmNKeUpJSVI0RTYwdGNjWEo0Q1ZKazBWcW5jMkJmSlIwS2o1NzVXbUtESkZ1RW1LanFWaXNZbzBsb3JPYnJTWDJRM2pN?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxOejhROHprSi11clBoVVFhX0Y5TXB0UkFIbGZOS0tfa1NTNU1IbndrRE5IRU1LTXBTV1BtN2FJSHZVcTREYXhFODVoYnpEU2lQUElJaTF1d0VhUzEzd0JiaWRMdzFiR3c5T3RYTlhpQzBoQl93ZHpaZks1QUpFNXdkaWZVUnNEdkRxZlVrWWZaWmdCSlNqSFpYRzBPMWFYem9HRWFPVEJaTzRNMk1jSlIwcE1kOGhBMzZmeHJqUjItVmZmOG5uNXZIQnc5Yi3SAcwBQVVfeXFMTno4UTh6a0otdXJQaFVRYV9GOU1wdFJBSGxmTktLX2tTUzVNSG53a0ROSEVNS01wU1dQbTdhSUh2VXE0RGF4RTg1aGJ6RFNpUFBJSWkxdXdFYVMxM3dCYmlkTHcxYkd3OU90WE5YaUMwaEJfd2R6WmZLNUFKRTV3ZGlmVVJzRHZEcWZVa1lmWlpnQkpTakhaWEcwTzFhWHpvR0VhT1RCWk80TTJNY0pSMHBNZDhoQTM2ZnhyalIyLVZmZjhubjV2SEJ3OWIt?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNSXRNZGJ1RmNMZUQ3M0p5dzlrSnNjUDAzYUhXNGh0ZGRJODduX3hHSWlDS1hrb3BVRGVpWXNnOHpRZmN4S1BUU1IwMWFfQlBvQ0ZraV9aQml5Zk5XRlR1TUlGdm9fSGFWbHIxWF83V0ZYNFQzWUE1WHRTQ2piMnkxSHF5LWdqakxnVGJEY09ZUHpld1RtdnFR?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOR1o3WjZHSmU2MmNuRDFOUDhFX0hIaTNDRHdXSTRVVDJaZHZwUzRONXd6eXh2VW9scjFmNm5QRDB1b2RLSUhBc2JDUmE0MkFnbDY5T1RHaFVyMTlKajRRR2FPU0tzUkhLaG1NT0FJNjEzR3VxZmoxeDZxV0ctVmhlQ0hVTm9oVlc5NFdfbVNua2VBQjFuVGgtNUhQY0h6bjg5OGRWYmRHTW0yQWptbV9XQmFRUHY?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPWkRMNUdXeDZuWDNGOFlDYkNVMzU3ZmFyY3E0NnhMN1Z0eHAyaHk5XzdubkN6X2FnYm05Ym1GQWc2Tm1OaTFzRkVESUNyRTA5V01IWjA2SlJJLS05R1FFNzVjZWZHeVBfSGJqWC1NT2JsQ2Z3TktXMGw0ZjVmZkpaenNXYzNmMm93Z3dSQUdNZHU3aFFJbzZnc3hkUUxmUGtFVnVRQ1JBOTRvSThQalFneUVaX19nbGdPZng4?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxQaW12a0pmQmYtZUlPOUZmX09GaXM4MTBoRV9jRHNsbEVhaU4yOUo5S1RpN2RHc0FIU1l3UHRtMktrSnowc3NrUFByNXhkRXlYY3c1bkJKbVFHWTVFclVEdlZzZmJ5ZkdhVEhEWF80VzdHVWdUWHBLZnFwUXhWV3NhdFJkVFd0amc3NE5ha3NvOVBlaUJpZkJ4QTFFRlRFLURoY3hPY0I4czc2YmdtSHhGLWh3OGtxSFVxRlVZdTBQTjR2RVcza0wwTFNSZw?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNRkVmNHFuMzZObmVHRkpVOEZZNFJmT3ZKQ0NGYjBtdTBQVFIwbko0Mk53UnFfNU05dTRPdE9MWXRKZWhjbVJ2dXJOdzJFaXBHWkNuZWxvNGRha0lKQ0o5OG82WXVpN0o2azdRV2dCQ3R1WE80QjB0dDUteTZjTG5NRU9YQWE1MFI5clJQaWIyUTNsXzBvVVpaM29FdjJZSlZ5QTlqSDdJc05zMmU2LVJzazVtMWlXcENGU0dGTzBCSEtxQXljNTdj0gHMAUFVX3lxTE1oM0RXNVdySG1lbmpDZ2gyYWpSNmFGRGdjR21kd3NHOURpZXFSTUdjMDVMaDJFc0c2emtWXzRfTnE2ckdoYjFjMjVMMWdQTTFmRUFQQy0zOFZwallqX1lhelQ0MHNmaGR0Mk5BTXRDM1lfSFNvX216UXlwVk1YaTktampMQXRseDdYdXhFcTEybzdFZmNNQzJEdmVOTVNQM0tMZllMZ05nVDBEUkhNUEpGS3JtSkp1bllURDE1SnZfOXZ5THRRbGRIdlNQZg?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxORl9NbF9KQVNuaGlrRFR1UG1KUFZTYlg2SnFPbWl5aHhMZDZFQnBueURSY3ZobFJxZlVVS0ZEb1lLNkFpY2xvWjk4bVoyNzZzcnFhd0tZMHplTDRWYXRUNXgxSURxdTJuWVFoemU5S2w0QzFQeEhndW9VT1ZiLV9pT3lQMDcyc25xYnZSaE85QzN5V0VBRUlNYVllSFJ6WXBTajFwZFlsZEY0Rmc0UkVsbVJvRm0zYmFzMV9jdEVBS2JkU2tRRGJGdTZIajM?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
