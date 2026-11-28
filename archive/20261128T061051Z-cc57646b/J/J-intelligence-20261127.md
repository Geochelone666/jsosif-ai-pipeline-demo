# J Intelligence Report

- ticker: **J**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/J/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/J/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:22:51.691240+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 8, 'ai': 13, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/J** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 9 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 24.0%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 146.5700 |
| Return 1D (%) | 0.7423 |
| Return 1W (%) | -2.6889 |
| Return 1M (%) | -1.1932 |
| Return YTD (%) | 11.5618 |
| Return 1Y (%) | 9.0325 |
| Annualized volatility (%) | 32.7916 |
| Beta vs SPY | 0.7909 |
| Max drawdown (%) | -28.8516 |
| Sharpe (rf=0) | 0.4539 |
| Downside deviation (rf=0, %) | 23.4463 |
| Sortino (rf=0) | 0.6348 |
| Historical VaR 95% (1D, %) | 3.0536 |
| Historical ES 95% (1D, %) | 4.9389 |
| Correlation vs SPY | 0.3623 |
| Tracking error vs SPY (%) | 30.7244 |
| P/E (trailing) | 48.69 |
| P/B | 5.26 |
| EV/EBITDA | 13.41 |
| Revenue growth (%) | 49.40 |
| Forward P/E (estimate) | 15.57 |
| Gross margin (%) | 20.84 |
| Operating margin (%) | 7.96 |
| Return on equity (%) | 8.75 |
| Free cash flow yield (%) | 4.40 |
| MA50 | 146.8784 |
| Close vs MA50 (%) | -0.2100 |
| MA200 | 134.8672 |
| Close vs MA200 (%) | 8.6773 |
| RSI (14, Wilder) | 43.3100 |
| MACD (12,26) | 0.6416 |
| MACD signal (9) | 2.3255 |
| MACD histogram | -1.6839 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'J': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 146.5700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.7423 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.6889 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -1.1932 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 11.5618 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 9.0325 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 32.7916 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.4463 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6348 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0536 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.9389 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3623 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.7244 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7909 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8516 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4539 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.5720 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 20.8420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 7.9570 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.7460 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.4006 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 48.6944 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.3100 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.6839 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.2100 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 8.6773 -> Clearly above the moving-average trend level.

## TAILWINDS

### Jacobs Solutions (J) Tops Q4 Earnings and Revenue Estimates
- Summary: Jacobs Solutions (J) Tops Q4 Earnings and Revenue Estimates
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNTllTWXF0RXl5VHozUHJ4TlZBbkFkZFdZZFRsRHI0NU02M201ZTNvdHBZdFhWd1R0WVhTS2t4eDBmUk9GX2FPY0lkdzg2TDRKWU1WVjlmTmFHelYzUk1yREp5VUxsRm5MLURLWE4wWkcwRnZzOVlPUm1ZX19RbnZucXhlUFJCcVlCQzRVeWo0NzByTlhnY3c?oc=5>

### Jacobs Solutions Q3 CY2026 deep dive: Backlog growth and segment mix support margin expansion
- Summary: Q3 backlog and mix boost margins, reflecting operational strength.
- Date: 2026-11-24 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxPQklsT1RXVGowLUZHdWdhQXBaOG5YQ1lFUXBpMHc3aHpOTUl2ak5Vc2lsSHZfTHdQTm9sWXdKdGhLaEY2a3pMQXBtbTZ1cVdzT1dHRzQ0OGtDa1VGSklrZzQwcjFrRlhtc2VKVkxId2czMG1lTHJlTWY4RHAxZnctek5FcWMwMzQ5SmhjQndGUGFDbHk4ZUloY2pFYmxiM0FWVHRkVGtNWVE0TEVBazN3NU9zQjBtaUN3c2Y2T283azZ3UDBFN21fUEZUQTZEUjVybmtLeG1nb1JFNEU1c05DSWx2NlZfOXAy?oc=5>

### Jacobs Solutions (NYSE:J) Stock Price Expected to Rise, KeyCorp Analyst Says
- Summary: Analyst forecasts a price increase, signaling positive market sentiment.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxPSENUQkRaNm5yUzY4YzZrZmZHU1ptY2xaZmJNb3VGakxKTzBLQVlPU2pQM1RwRmpVUkRCeTJJQl9MR0JkRWFlUzB4ekVQQ0dSUnBDYkNXbU5WcFN1UUcxZ05sSUhoa1JTbnZEUHlGRWRvY2V5azc4M1hnbXQyaVNnSHJXdHBPMFJxV1lvb1RoZFd6amwxMF9KbXBTZnI2QVV6emtmT1RvQnU5WVVfd09ZdEZRSXNIU1F6VjYtR3BhdEVNX1B6S09IVFlaU1h4S2JR?oc=5>

## HEADWINDS

### Jacobs Solutions Slides as Investors Digest Recent Earnings and a Risk-Off Market
- Summary: Jacobs Solutions Slides as Investors Digest Recent Earnings and a Risk-Off Market
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOUGNkUkxoS1Brc1B5MlVKcVQteVBYbjBNdm9IUVE4eWI4R0V2S04tQXo5eGItYUJVcEtWRDNlRGlqU2xTM01CcW1wdVU4Xy1IYUF4ZjhJV2czajdCZ0xhREZHZVBSOEhkakRGZHcyT2l1S3ctNWlqMENQOWpXWlBwQ0gxZVI5UVhhVnM3ajZ2bkVoZkNJeTNxdHc5V0JWOUVxMVZDeVBUSE0zVjlsR2ZPbnV0OXY?oc=5>

## CATALYSTS

### Jacobs Solutions Inc. Stock 12‑Month Price Target Raised to $173.21, Implies 10% Upside
- Summary: Jacobs Solutions Inc. Stock 12‑Month Price Target Raised to $173.21, Implies 10% Upside
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxOY0ZycXJfLUxaanhoOEI2cTBqemlORGlvYi1ucEZGTlZhVUY3XzctNDVFaEdIRnRMUnM4Wmp6ZEVBZHJyYXpadlJtSWp2QVkxcXl6NmpxZDJJUnBWdzJxLXQ1bmkxT2JnWEl3ZzkxYmV4SFdfUWlzVWJOOWw1NDA1emhyeHBLQk9CSXIwdjUxU3ItMjRVUE5jeHdMNnU1QmFiTUhfbWNsNHkxMHVJemgwVTBCaXR1Y2xwOGZwdGNmQkRGVW9ZQjVDTTN3enFTNEQ1Ukxqa2dKeG5SZWh1Z0E?oc=5>

### Jacobs Solutions Analysts Boost Their Forecasts Following Upbeat Q4 Earnings
- Summary: Jacobs Solutions Analysts Boost Their Forecasts Following Upbeat Q4 Earnings
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxONFpwMlUwUV91cjl3Z1QteVZCMTZRbEpQY2RXank0N1FENFJ1RUI3cWhhN3pLdEs5cVVWZ05tTWJsQlBSa2Myc2NNRThRS1VxN1NzZ1c2dG8wNHltUnl1Q3I3T2JjazNxMkZUYnl4bUFGaVJkZ2lXU2M3ZkVQVW44OTk1NDlEZDJvbG92STIxTl9wMXUyRlFkZmpCVGJkZEFFMzE5WFZvZi1MOUNpY2tCdy1rWTh6WmhSeGpSdWsxSlNZMVNrWldZNmYyWlZrT1lSZGtQRlRGTHZyc2VGakY0Z1pXQmZEUQ?oc=5>

### Jacobs Solutions Inc. Stock 12‑Month Price Target Cut to $161.45, Implies 2% Upside
- Summary: Jacobs Solutions Inc. Stock 12‑Month Price Target Cut to $161.45, Implies 2% Upside
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxPUnFZYXRQUEtKYlJPZFNyNTNZbjdEX3NtRmJIMFljR0wybGJfc3hxMkZySG84YzQ5Tk1KeVlNck9EeVhfXzdfXzlnS2hFWnpORzZCUlA3SW04RkhBOGZfWEdlU2llQTFXNGdNMm13LXNVSVR6NUFzcGJLRG1GdnNzZ1lyS1VXUW04T3Y0YjlMZjNyZ1ZaeHFGMTFJeDZqU2lvcFppRjh3ZEhiWU1Cc0JuNnhNX2IxZDFETWRZUVVGUjJFMFFDbWhjQUp3YzhmVVZ1Qjd0UTdsSXo?oc=5>

### Jacobs Solutions Inc. 2026 Q4 - Results - Earnings Call Presentation (NYSE:J) 2026-11-24
- Summary: Jacobs Solutions Inc. 2026 Q4 - Results - Earnings Call Presentation (NYSE:J) 2026-11-24
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQeU9vbEtzWC0xUjBRSHM4cW45ems5TC1sUEcwWU5yQzRVbXpCWlo5UXZYeUNEMTQ2ZUNfdlFaZkdrNTZDNDRLTEEwaDQtaEV5Q1hhM085X2dVb1JKLUExdVNncXhLMVp5ZXJNeDRmOFlwT3drdWlyU2t5RnBmUzFPSWprQjdaWGpGaFNMUTk4ckhGUThkUlp2NVVYR004WDZuaGFGeEpNUQ?oc=5>

### Jacobs Solutions earnings: What to look for
- Summary: Jacobs Solutions earnings: What to look for
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPQWl6TDViZDNYVHIyeVVLOEVQX2Z4MTlFQi1sUmVUdEVfWTdBMzh1blFvOEZ3X3lGZTVISkJWSGxlTzRMQzJpYmEzbUo5M05wcHhfYTU1RHE5am5tcFpjbUFublBwYW5USnBlVGh6RWI1cmJaMW4tcW1hOGpIMUJ4T0Jlek5Wc2NoSGNfWTB0WUFOM2dkeUtxUzJpU1R4dDU2R0ZkeGJ3?oc=5>

### JACOBS SOLUTIONS Q4 2026 Earnings Preview: Recent $J Insider Trading, Hedge Fund Activity, and More
- Summary: JACOBS SOLUTIONS Q4 2026 Earnings Preview: Recent $J Insider Trading, Hedge Fund Activity, and More
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxNWUhmZ0k3ZnR1N3FRUk1GXzV6ejd4d3dlMVlqSWd3T3JTR2hhSWlUOVVkSzlJSDdGd2p3Y2NDSWZncTdiRWpmZ1d4QUN2MUliaXNlX0lVT3BsbVBKMm1NTWlWUnNSbGY4ODRCd2NzNzQzc0dXSW1yUnNjYzZpTEFCLXBDazBIS1VUX2dWb1lSSkZfQUc1NFUxVGtkMy1aNGhNeExmb2xfWHN4NncySDlKbWllSXRIelFXU1pRYnFNRlozeWF5aDZLRDVXNmZybTdLLVBJcEVVMA?oc=5>

### Do Wall Street Analysts Like Jacobs Solutions Stock?
- Summary: Analysts discuss potential impact on Jacobs Solutions stock performance.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNNGsxc1R2ZTcwSGRidEJpODVnOGNLTGt5d2FmOU9sZWFTN01VbDFraFpwOW83VUY2ZkY2eWNTaU94V3M2TUtMRHo5SGNJMVBPbWlsREphRFBraXBUWFlVdEdmNzgzY1dtemVRUTBBQmZKY0psNE1lcWd5bDNlSjFBSmtfeGFUWnNFYTJmNmVhbmdaUl9jbHZKazlzSmhrVTRHdE5tYw?oc=5>

### Jacobs Solutions Gears Up For Q4 Print; Here Are The Recent Forecast Changes From Wall Street's Most Accu
- Summary: Company updates Q4 forecasts ahead of earnings release.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMimwJBVV95cUxObVE3bElrOFgtZ3YxM3lHcGNyQ21nbkFMWlg0WGZiMXpvOEdxSkJiWGZSQWtWVkZsV2JlbHU3ZlBjcWl2WDI4S252QkJhQ3ZONEFyMXBWTHZ2QXg4cmZsbEo1Q2JBMDhWR04tZ2NmWWwySlFFb1RVMUw5dDVZbm5sOEg4aHJidVlBdWZYQ3VXbWUxWW85X25wZlBPTGRGOEpxdVcyS1ZhRzZoRFA5UGJMbVVXU2RuN2V1STRiUkk5RXNkWEtyYmt3QVlOUGtwOE9nQnJYcXcwNmd0NXlFY19wTFhzX1pqa0xvZ3JLbF90c0lJZGxOalRFSVNrWnNpYlNUVjNHYzd3cERUb1cxX1JkZnNhLWtoc3lQeUI4?oc=5>

### Jacobs (J) Stock May Be A Bargain Despite Fresh Airport Upgrade Wins
- Summary: Jacobs stock appears undervalued amid recent airport upgrade contracts, suggesting potential upside for investors.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPZ3Vlay1FSHB2aVZSN3dOMVRzel9xVWJfV1hvZmwtMmhCQ0FaSkVRS1FydUNqeE83MzduLXgxMDg0QU9KQy16TDhabHpDNUdBc0EyTFR5TmdGS2hjSkNHVy1NbW9iR09OOW5ZMVNZMm5POVFnUjN2Ui12SzlVa3FpX3FjMUhiZTdvUS11WFFjNUhwNFhVcUE?oc=5>

### Argus Forecasts Strong Price Appreciation for Jacobs Solutions (NYSE:J) Stock
- Summary: Argus predicts significant price appreciation for Jacobs Solutions stock.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQcXZmTXktUkt0VlpyU3VtZGdDOHpFWmZSbXFYSWo0dERkRVVIZ2hXY0YxbHhHRWR2Tk9hVWpkVGhzT0E0YzI1VTBFdE54SFlEUmdvRHJrWElmT3Y0ZjBNNGpnam5ScENfa0t0LVQyVlhkeXIxRDFWYnBJb0hwR2p6VWhYd2ZvclhsNUhKU012VTZyR050dEY2TUlUMC1iODFidjFZUWZ2dlByVW1vOUVVMUVaSGhrT0ZNbFlEcHdPM2laR3UzN1NyUVZOZW1BLUxLOEU4?oc=5>

### UBS Group Issues Positive Forecast for Jacobs Solutions (NYSE:J) Stock Price
- Summary: UBS forecasts a positive outlook for Jacobs Solutions, suggesting potential upside for the stock.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQOE1GSnEzTy1NYlZmdDl6aG1MVUh4SEpUT2RnM293Vy1JV2FabGZjTlQ1VkZNamJlYU40emY0bmUzSFJaLTd1TldWT3o5WG0wQi0xUUpKU1JtcXJ2cjRadHNnUi00ZS1nV0FlRTdwRGQ0NW9GdVU0eVNQbjJ2YUFEX3B1R2p4RnJ2WkE1UDhIQzdpVUJUTXNVZUVNWlNFbVh6ZEtJRy02NUJCTzE1QzMzZGNQTW9JWHJ4Qlpsekg5SUZpUDRsNFppcXRpSnYteTl3X0E?oc=5>

### Truist Financial Forecasts Strong Price Appreciation for Jacobs Solutions (NYSE:J) Stock
- Summary: Truist Financial forecasts strong price appreciation for Jacobs Solutions stock.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxNT3hMZFBBSGUwOE1PN09kbTdvTW1YUFJ0VUtCRlE4MVVxQ242QTBxaFFVUk1waFhQR2RFcXZZOGtxQk11eGIzREVfc2VLRTNsNlQwellhcENBdUJJcjBuZ1dGdUVmR3BhVE9XOFF3M1huanVoclBHUGRXQVRnNFRJT0hGTkRCb19YTEVLOURnWGR5eElHNV9QM29vMGtaWHRQMkVRQ0twVmxBQ1B6WW43VDdPU3owa0U2SU1WSEdXRTJkajU0a2xXNUFtNE45bjJ6OU1wamhKeVFIVnBhZFZWZlBB?oc=5>

### Jacobs Solutions (NYSE:J) Gains as Fiscal Fourth Quarter Shows a Swelling Backlog
- Summary: Jacobs reported a larger backlog in Q4, boosting its share price and outlook.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNMTdYVy04VFBBVk5BRUZPczZKVFpINVBiSDVJekNfTU9ENGQ1TXowVjJDYmhZUGt5cXhiV3YxWkdzVlhCWFJ0VUYxQ0syX0NjaVRxd0FfVWxxZmE1aV9yLVdJSEhzcXM3bl80NDNzVkktSnZTOTNSdlR4cjZqbHZiWjdIOXJrS2stc0xoOFg4TnNqbk15RElGd0o3N1MwUXpqLWdTWUk2X1g1RFQtRVJRME9KX0hMQQ?oc=5>

### Robert W. Baird Issues Positive Forecast for Jacobs Solutions (NYSE:J) Stock Price
- Summary: Baird analysts issue a positive forecast for Jacobs Solutions, suggesting potential upside for the stock.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxOSUN2MHNKTDAwODM2bDZmd3NLYktMclloTkM2X0hWS09zT2ttWDlBNDZPbjNUMGlMR0d4M3FOTWdJa1RwaXNZcE1rb2tIVWRfN2F2UHhlT2xpRG9UWm1ybHhvVmRnOFhkWDA3OWh3NU9iZXVyTTNyc1FqUWxCMXhIRTVvUEZhWWJFdEtJS0lTODFFYTNqeTFwLW5TOVVJaVpKMXF1RG5Ubl9jSzZPQUZmdnJwOWJyV1ljcm10VkhRTEhIYldBV2U2Y19TdWs1RkZkWHRncklFNFA?oc=5>

## RISKS

### Jacobs Solutions’s Q3 CY2026: Beats on revenue but full-year sales guidance misses expectations significantly
- Summary: Q3 revenue beat, but full-year sales guidance below expectations.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi_gFBVV95cUxQbXZWR1I4TnJYZEFfTGRERkFxcUd3eFJQN3BRalo1Um41WUNfaWphQmQwczM2XzNBWWZtXzB1anVGazJ6Z1lHQ0dURUxYeEUtMEtvZ2dQTzY1bXY2YXF4U2hwMTJSU0JuczRBTk1mVTZUT1Y0eF8yQ0xKVDcxanhmNGxzV0s2N0dlU2ZYc3FXUHNjWVdEMEhwbl9lNEphRml4Z1UwLXVZZndFVmNBQ1dNVUtTZnBJRGc0X0NETWtHVExLM2tkR1pocEZfakdFcUxzVGV1ZDBCVDNHa3N5VkV6Ry0wWXVwS2dXV0RrWW9FNFJuR25XQkZrTkN5bkt5dw?oc=5>

### Jacobs Solutions (NYSE:J) Stock Price Crosses Below 50 Day Moving Average - Here's Why
- Summary: Stock falls below 50‑day moving average, indicating potential downside pressure.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxOQ29UR1FUYUZSX19CZlNRcDhRS3VXWEdVMjZlU3RoMDIzZHRmbHRJeXBvUW8xaExlQ3NibDFvaEpvQTc3bEZSMm84bXRlaXkzcG5Sdzh4bFpRTlBveWxrTVJldVhuQXVyX0g1RzZJSVJWX1JLWThBYWRKWkhkaW1NRzh5SXEzNTdXOFZRbzFJRVRxR0wzU1FqdXV4ZmFBN19hNkJfTDZCNmpTMHRxYlpIU1BLQ3ppYTZWaks5bHdUVXQ3TG9oY0pJeEV0eHhqcjZBU2hMbHZUcFo?oc=5>

### Jacobs Solutions: A Burgeoning Backlog Could Lead To Slowing Growth (Rating Downgrade)
- Summary: Credit rating downgrade signals potential slowdown in growth due to backlog concerns.
- Date: 2026-11-25 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQc2dYNkFmUkl0TTYzLVlXLVBpNlB3b3A0eEI1bHhzQ1ZvdWZSc0VnNkkxM0xQbWl4eWdPbmVkaWVMYkZuLXFzN3drcEFnZkc5WjVuNDlCeG13M2ZnM21GVlppUHZpTWJJcHBxbGt3ZjBqM0ZrLVlCOXVHVjN1WWtDRUhQUW01Q3YtZU9ZM3BTcEE3dGoyVlM3RHVYRGkzZUJmeE0tTU5hdjFmZTZrV1ZKVw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **J** | **48.69** | **5.26** | **13.41** | **49.40** | **17,024,361,472.00 USD** | **9.03** |
| ACM | 29.64 | 4.94 | 13.72 | -7.10 | 10,844,519,424.00 USD | -18.84 |
| FLR | N/A | 2.39 | 10.53 | 10.50 | 6,073,370,112.00 USD | 11.72 |
| KBR | 10.06 | 2.47 | 9.64 | 5.00 | 4,362,109,952.00 USD | -13.67 |

Peers fetched as_of: 2026-11-27; J reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-23
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-23
- Revenue (latest available single quarter): 4,142,644,000.00 USD; period 2018-06-30/2018-09-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 136,553,000.00 USD; period 2026-03-28/2026-06-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/52988/000162828026075495/jec-20261002.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilgFBVV95cUxNTllTWXF0RXl5VHozUHJ4TlZBbkFkZFdZZFRsRHI0NU02M201ZTNvdHBZdFhWd1R0WVhTS2t4eDBmUk9GX2FPY0lkdzg2TDRKWU1WVjlmTmFHelYzUk1yREp5VUxsRm5MLURLWE4wWkcwRnZzOVlPUm1ZX19RbnZucXhlUFJCcVlCQzRVeWo0NzByTlhnY3c?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxPQklsT1RXVGowLUZHdWdhQXBaOG5YQ1lFUXBpMHc3aHpOTUl2ak5Vc2lsSHZfTHdQTm9sWXdKdGhLaEY2a3pMQXBtbTZ1cVdzT1dHRzQ0OGtDa1VGSklrZzQwcjFrRlhtc2VKVkxId2czMG1lTHJlTWY4RHAxZnctek5FcWMwMzQ5SmhjQndGUGFDbHk4ZUloY2pFYmxiM0FWVHRkVGtNWVE0TEVBazN3NU9zQjBtaUN3c2Y2T283azZ3UDBFN21fUEZUQTZEUjVybmtLeG1nb1JFNEU1c05DSWx2NlZfOXAy?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxPSENUQkRaNm5yUzY4YzZrZmZHU1ptY2xaZmJNb3VGakxKTzBLQVlPU2pQM1RwRmpVUkRCeTJJQl9MR0JkRWFlUzB4ekVQQ0dSUnBDYkNXbU5WcFN1UUcxZ05sSUhoa1JTbnZEUHlGRWRvY2V5azc4M1hnbXQyaVNnSHJXdHBPMFJxV1lvb1RoZFd6amwxMF9KbXBTZnI2QVV6emtmT1RvQnU5WVVfd09ZdEZRSXNIU1F6VjYtR3BhdEVNX1B6S09IVFlaU1h4S2JR?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOUGNkUkxoS1Brc1B5MlVKcVQteVBYbjBNdm9IUVE4eWI4R0V2S04tQXo5eGItYUJVcEtWRDNlRGlqU2xTM01CcW1wdVU4Xy1IYUF4ZjhJV2czajdCZ0xhREZHZVBSOEhkakRGZHcyT2l1S3ctNWlqMENQOWpXWlBwQ0gxZVI5UVhhVnM3ajZ2bkVoZkNJeTNxdHc5V0JWOUVxMVZDeVBUSE0zVjlsR2ZPbnV0OXY?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxOY0ZycXJfLUxaanhoOEI2cTBqemlORGlvYi1ucEZGTlZhVUY3XzctNDVFaEdIRnRMUnM4Wmp6ZEVBZHJyYXpadlJtSWp2QVkxcXl6NmpxZDJJUnBWdzJxLXQ1bmkxT2JnWEl3ZzkxYmV4SFdfUWlzVWJOOWw1NDA1emhyeHBLQk9CSXIwdjUxU3ItMjRVUE5jeHdMNnU1QmFiTUhfbWNsNHkxMHVJemgwVTBCaXR1Y2xwOGZwdGNmQkRGVW9ZQjVDTTN3enFTNEQ1Ukxqa2dKeG5SZWh1Z0E?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxONFpwMlUwUV91cjl3Z1QteVZCMTZRbEpQY2RXank0N1FENFJ1RUI3cWhhN3pLdEs5cVVWZ05tTWJsQlBSa2Myc2NNRThRS1VxN1NzZ1c2dG8wNHltUnl1Q3I3T2JjazNxMkZUYnl4bUFGaVJkZ2lXU2M3ZkVQVW44OTk1NDlEZDJvbG92STIxTl9wMXUyRlFkZmpCVGJkZEFFMzE5WFZvZi1MOUNpY2tCdy1rWTh6WmhSeGpSdWsxSlNZMVNrWldZNmYyWlZrT1lSZGtQRlRGTHZyc2VGakY0Z1pXQmZEUQ?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxPUnFZYXRQUEtKYlJPZFNyNTNZbjdEX3NtRmJIMFljR0wybGJfc3hxMkZySG84YzQ5Tk1KeVlNck9EeVhfXzdfXzlnS2hFWnpORzZCUlA3SW04RkhBOGZfWEdlU2llQTFXNGdNMm13LXNVSVR6NUFzcGJLRG1GdnNzZ1lyS1VXUW04T3Y0YjlMZjNyZ1ZaeHFGMTFJeDZqU2lvcFppRjh3ZEhiWU1Cc0JuNnhNX2IxZDFETWRZUVVGUjJFMFFDbWhjQUp3YzhmVVZ1Qjd0UTdsSXo?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQeU9vbEtzWC0xUjBRSHM4cW45ems5TC1sUEcwWU5yQzRVbXpCWlo5UXZYeUNEMTQ2ZUNfdlFaZkdrNTZDNDRLTEEwaDQtaEV5Q1hhM085X2dVb1JKLUExdVNncXhLMVp5ZXJNeDRmOFlwT3drdWlyU2t5RnBmUzFPSWprQjdaWGpGaFNMUTk4ckhGUThkUlp2NVVYR004WDZuaGFGeEpNUQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPQWl6TDViZDNYVHIyeVVLOEVQX2Z4MTlFQi1sUmVUdEVfWTdBMzh1blFvOEZ3X3lGZTVISkJWSGxlTzRMQzJpYmEzbUo5M05wcHhfYTU1RHE5am5tcFpjbUFublBwYW5USnBlVGh6RWI1cmJaMW4tcW1hOGpIMUJ4T0Jlek5Wc2NoSGNfWTB0WUFOM2dkeUtxUzJpU1R4dDU2R0ZkeGJ3?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxNWUhmZ0k3ZnR1N3FRUk1GXzV6ejd4d3dlMVlqSWd3T3JTR2hhSWlUOVVkSzlJSDdGd2p3Y2NDSWZncTdiRWpmZ1d4QUN2MUliaXNlX0lVT3BsbVBKMm1NTWlWUnNSbGY4ODRCd2NzNzQzc0dXSW1yUnNjYzZpTEFCLXBDazBIS1VUX2dWb1lSSkZfQUc1NFUxVGtkMy1aNGhNeExmb2xfWHN4NncySDlKbWllSXRIelFXU1pRYnFNRlozeWF5aDZLRDVXNmZybTdLLVBJcEVVMA?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNNGsxc1R2ZTcwSGRidEJpODVnOGNLTGt5d2FmOU9sZWFTN01VbDFraFpwOW83VUY2ZkY2eWNTaU94V3M2TUtMRHo5SGNJMVBPbWlsREphRFBraXBUWFlVdEdmNzgzY1dtemVRUTBBQmZKY0psNE1lcWd5bDNlSjFBSmtfeGFUWnNFYTJmNmVhbmdaUl9jbHZKazlzSmhrVTRHdE5tYw?oc=5
- https://news.google.com/rss/articles/CBMimwJBVV95cUxObVE3bElrOFgtZ3YxM3lHcGNyQ21nbkFMWlg0WGZiMXpvOEdxSkJiWGZSQWtWVkZsV2JlbHU3ZlBjcWl2WDI4S252QkJhQ3ZONEFyMXBWTHZ2QXg4cmZsbEo1Q2JBMDhWR04tZ2NmWWwySlFFb1RVMUw5dDVZbm5sOEg4aHJidVlBdWZYQ3VXbWUxWW85X25wZlBPTGRGOEpxdVcyS1ZhRzZoRFA5UGJMbVVXU2RuN2V1STRiUkk5RXNkWEtyYmt3QVlOUGtwOE9nQnJYcXcwNmd0NXlFY19wTFhzX1pqa0xvZ3JLbF90c0lJZGxOalRFSVNrWnNpYlNUVjNHYzd3cERUb1cxX1JkZnNhLWtoc3lQeUI4?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPZ3Vlay1FSHB2aVZSN3dOMVRzel9xVWJfV1hvZmwtMmhCQ0FaSkVRS1FydUNqeE83MzduLXgxMDg0QU9KQy16TDhabHpDNUdBc0EyTFR5TmdGS2hjSkNHVy1NbW9iR09OOW5ZMVNZMm5POVFnUjN2Ui12SzlVa3FpX3FjMUhiZTdvUS11WFFjNUhwNFhVcUE?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQcXZmTXktUkt0VlpyU3VtZGdDOHpFWmZSbXFYSWo0dERkRVVIZ2hXY0YxbHhHRWR2Tk9hVWpkVGhzT0E0YzI1VTBFdE54SFlEUmdvRHJrWElmT3Y0ZjBNNGpnam5ScENfa0t0LVQyVlhkeXIxRDFWYnBJb0hwR2p6VWhYd2ZvclhsNUhKU012VTZyR050dEY2TUlUMC1iODFidjFZUWZ2dlByVW1vOUVVMUVaSGhrT0ZNbFlEcHdPM2laR3UzN1NyUVZOZW1BLUxLOEU4?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQOE1GSnEzTy1NYlZmdDl6aG1MVUh4SEpUT2RnM293Vy1JV2FabGZjTlQ1VkZNamJlYU40emY0bmUzSFJaLTd1TldWT3o5WG0wQi0xUUpKU1JtcXJ2cjRadHNnUi00ZS1nV0FlRTdwRGQ0NW9GdVU0eVNQbjJ2YUFEX3B1R2p4RnJ2WkE1UDhIQzdpVUJUTXNVZUVNWlNFbVh6ZEtJRy02NUJCTzE1QzMzZGNQTW9JWHJ4Qlpsekg5SUZpUDRsNFppcXRpSnYteTl3X0E?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxNT3hMZFBBSGUwOE1PN09kbTdvTW1YUFJ0VUtCRlE4MVVxQ242QTBxaFFVUk1waFhQR2RFcXZZOGtxQk11eGIzREVfc2VLRTNsNlQwellhcENBdUJJcjBuZ1dGdUVmR3BhVE9XOFF3M1huanVoclBHUGRXQVRnNFRJT0hGTkRCb19YTEVLOURnWGR5eElHNV9QM29vMGtaWHRQMkVRQ0twVmxBQ1B6WW43VDdPU3owa0U2SU1WSEdXRTJkajU0a2xXNUFtNE45bjJ6OU1wamhKeVFIVnBhZFZWZlBB?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxNMTdYVy04VFBBVk5BRUZPczZKVFpINVBiSDVJekNfTU9ENGQ1TXowVjJDYmhZUGt5cXhiV3YxWkdzVlhCWFJ0VUYxQ0syX0NjaVRxd0FfVWxxZmE1aV9yLVdJSEhzcXM3bl80NDNzVkktSnZTOTNSdlR4cjZqbHZiWjdIOXJrS2stc0xoOFg4TnNqbk15RElGd0o3N1MwUXpqLWdTWUk2X1g1RFQtRVJRME9KX0hMQQ?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxOSUN2MHNKTDAwODM2bDZmd3NLYktMclloTkM2X0hWS09zT2ttWDlBNDZPbjNUMGlMR0d4M3FOTWdJa1RwaXNZcE1rb2tIVWRfN2F2UHhlT2xpRG9UWm1ybHhvVmRnOFhkWDA3OWh3NU9iZXVyTTNyc1FqUWxCMXhIRTVvUEZhWWJFdEtJS0lTODFFYTNqeTFwLW5TOVVJaVpKMXF1RG5Ubl9jSzZPQUZmdnJwOWJyV1ljcm10VkhRTEhIYldBV2U2Y19TdWs1RkZkWHRncklFNFA?oc=5
- https://news.google.com/rss/articles/CBMi_gFBVV95cUxQbXZWR1I4TnJYZEFfTGRERkFxcUd3eFJQN3BRalo1Um41WUNfaWphQmQwczM2XzNBWWZtXzB1anVGazJ6Z1lHQ0dURUxYeEUtMEtvZ2dQTzY1bXY2YXF4U2hwMTJSU0JuczRBTk1mVTZUT1Y0eF8yQ0xKVDcxanhmNGxzV0s2N0dlU2ZYc3FXUHNjWVdEMEhwbl9lNEphRml4Z1UwLXVZZndFVmNBQ1dNVUtTZnBJRGc0X0NETWtHVExLM2tkR1pocEZfakdFcUxzVGV1ZDBCVDNHa3N5VkV6Ry0wWXVwS2dXV0RrWW9FNFJuR25XQkZrTkN5bkt5dw?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxOQ29UR1FUYUZSX19CZlNRcDhRS3VXWEdVMjZlU3RoMDIzZHRmbHRJeXBvUW8xaExlQ3NibDFvaEpvQTc3bEZSMm84bXRlaXkzcG5Sdzh4bFpRTlBveWxrTVJldVhuQXVyX0g1RzZJSVJWX1JLWThBYWRKWkhkaW1NRzh5SXEzNTdXOFZRbzFJRVRxR0wzU1FqdXV4ZmFBN19hNkJfTDZCNmpTMHRxYlpIU1BLQ3ppYTZWaks5bHdUVXQ3TG9oY0pJeEV0eHhqcjZBU2hMbHZUcFo?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQc2dYNkFmUkl0TTYzLVlXLVBpNlB3b3A0eEI1bHhzQ1ZvdWZSc0VnNkkxM0xQbWl4eWdPbmVkaWVMYkZuLXFzN3drcEFnZkc5WjVuNDlCeG13M2ZnM21GVlppUHZpTWJJcHBxbGt3ZjBqM0ZrLVlCOXVHVjN1WWtDRUhQUW01Q3YtZU9ZM3BTcEE3dGoyVlM3RHVYRGkzZUJmeE0tTU5hdjFmZTZrV1ZKVw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
