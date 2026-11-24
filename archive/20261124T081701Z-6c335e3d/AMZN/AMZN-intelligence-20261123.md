# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:17:10.777705+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 17, 'ai': 8, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 44.0%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 255.3900 |
| Return 1D (%) | 3.4722 |
| Return 1W (%) | -0.9156 |
| Return 1M (%) | 2.9798 |
| Return YTD (%) | 10.6447 |
| Return 1Y (%) | 15.7234 |
| Annualized volatility (%) | 34.4346 |
| Beta vs SPY | 1.2374 |
| Max drawdown (%) | -19.6419 |
| Sharpe (rf=0) | 0.5226 |
| Downside deviation (rf=0, %) | 21.2328 |
| Sortino (rf=0) | 0.8476 |
| Historical VaR 95% (1D, %) | 3.2323 |
| Historical ES 95% (1D, %) | 4.1300 |
| Correlation vs SPY | 0.5381 |
| Tracking error vs SPY (%) | 29.2405 |
| P/E (trailing) | 20.65 |
| P/B | 4.50 |
| EV/EBITDA | 16.07 |
| Revenue growth (%) | 12.10 |
| Forward P/E (estimate) | 23.37 |
| Gross margin (%) | 51.37 |
| Operating margin (%) | 13.09 |
| Return on equity (%) | 27.42 |
| Free cash flow yield (%) | -1.26 |
| MA50 | 255.0690 |
| Close vs MA50 (%) | 0.1258 |
| MA200 | 245.3759 |
| Close vs MA200 (%) | 4.0811 |
| RSI (14, Wilder) | 48.4407 |
| MACD (12,26) | 0.5913 |
| MACD signal (9) | 1.7068 |
| MACD histogram | -1.1156 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 255.3900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.4722 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.9156 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.9798 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 10.6447 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 15.7234 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.4346 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.2328 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8476 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2323 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1300 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5381 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.2405 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2374 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.6419 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5226 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.3743 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.3740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.0870 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.4160 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -1.2577 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.6459 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.4407 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.1156 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.1258 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 4.0811 -> Slightly above the moving-average trend level.

## TAILWINDS

### Amazon Stock Pops: What's Going On?
- Summary: Amazon Stock Pops: What's Going On?
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPZzNaYkdqazhvS254MUt3MjVTaFcxNzV6Q2NGYlZ2eHdaUm9XS3FyTkR5WkRHX3A1SjBEQ1QtY0djSC1iTUdpRkl2bUZudFRwM2ZUcDV1eHRhRVJObXNpRFBaYjMwZDdnNWhmdkVwZkpCa0xCRWtMNkZpX2xQLXg1eENFUjV6YXROaEQ2SlhJMk9KSVZhUGJKaw?oc=5>

### Amazon Stock Moves Higher: What's Going On?
- Summary: Amazon Stock Moves Higher: What's Going On?
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOd3EzOU9yRkc4NDAwWmxwN0dpeF9DdHJpNFpmN1hfV2poTUZkY21xcW1jNXAyR1BIU3NDZnpPQ0M3Z2NYMG1xeTAzRXpwTUplOTB5SHZ0R2xtNjNmajRrVWxCTVl0ZGpiUEtnS1FRRFpIMUE2dFlYZUo2WXFEVXNkM1JEYU1DdW5vS05YbXdwcW10dWJwS0ltdDVQd0xBLXVfOENXRUdn?oc=5>

### Amazon.com (NASDAQ:AMZN) Stock Jumps 3.5% After Analyst Upgrade
- Summary: Amazon.com (NASDAQ:AMZN) Stock Jumps 3.5% After Analyst Upgrade
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQdEFnQ1liWFJrVDBPTkV4Umt0SEw3V3FvWDZoeTRZczNlYTlKLXBZM2dNVThEcXRkUm9KV0ZCTUFQTVJFWnhqcVk2NWQ5V2ZsbzZBUldEbTg0b0o2VDlCRklDNUlFRHk4X2RwRGZOa1ZOcnpfZmpONEtoU3ViZWVGTTh6RGJzSENlNW9QOXptcmEwQ3NmdmxydGtEdXp2Z3RUYlRJLWI2a3BzUmg0Z01xY3I4akVmWElWbWc?oc=5>

### Amazon.com (NASDAQ:AMZN) Stock Price Target Raised at Oppenheimer
- Summary: Amazon.com (NASDAQ:AMZN) Stock Price Target Raised at Oppenheimer
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPUENIZzZ3ZEZURzJfdzgteDlHYTJZckpaZWZQeFhXeXhfdWlaSzhxZ1pURG1UckNleDFEZVU3V2l1X3dlZkFLdE5EbXJyWTh3Y2Q4VmhkbmtubXhWZVB3NEVNeUtZSVloYXpoejdlMTNERHFhUXg4WU5RM3hONlo4TlNkM0ctTFpEN0ZJZElfcGtoNGFTbEFwVkc1Z3d2c0tuM2NIQWZMcVBzbVE5WG9rN3hNSW1GazhGaVpxV2kycF9KUQ?oc=5>

### Amazon.com (NASDAQ:AMZN) Stock Jumps 3.8% - Here's Why
- Summary: Amazon.com (NASDAQ:AMZN) Stock Jumps 3.8% - Here's Why
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNY3FYSHN1WVd5R2I5T0lTUXhrMmhMRVhwZ0FiTEZGTHRmaF92aHF2LUFpLVpWSXpUM2ZKYXdmbWRZUkp1MkV4aDluQzZSNncxTURrcmF2bU8xTWRFNzE2NU15WU1jVkRFY2NWeDFDekVQRjBHdi1tODg4SUtwR1pkajcwVmNjYmVEUFVteUVqOEk5elBpUkt4TjBVVEdFc0dTVm9qQ1lHN0MtQQ?oc=5>

### Amazon.com Inc Stock (AMZN) Moved Up by 3.71% on Nov 23: A Full Analysis
- Summary: Amazon shares rose 3.71% on Nov 23, indicating a positive market reaction.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOYUI4dW4yVFZLUmNocWJ3SmJ4MFhaTGRrcFVqd2ZUak1sdDYwSlR6YkJjUHkya1FaQzlmQkduYVRDYkhKa0w1ZHBvYkFSZXlLOGNlVmxLcjdMclgxaUlZTi11VmJwYUpuUXVuWU13WVE3UFhPRjgyek1MTkNUckhHMkd6cVVfNGoxc3Vn?oc=5>

### Amazon (AMZN) and Big Tech Are Spending Heavily on AI – Here’s Why Investors Aren’t Panicking
- Summary: Amazon’s significant AI investment is viewed positively, with investors remaining calm.
- Date: 2026-11-20 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOMXdBQUpoQ2EwOFVBdW5HQWtaTXdVVTJqbjJZczdqRFZJdDJ3bHMzQmVQU2RVTF9ISmNxcFRXV2VJeWdDNURIZ0duc2pTX0lVZmE4WTREb3NaQmIyM1JfMzBqNFpENlBjTEhoVlZPc3I1bHdkVFowWEkyWXFib1hDbWF6bUJKS2pobVg1OW5pZFZqUElibGNJVQ?oc=5>

### AMZN Stock Rebounds Despite the UBS Downgrade, as Amazon Anthropic Investment Could Be Worth $150B
- Summary: Amazon stock rebounded after a downgrade, buoyed by a potentially $150B Anthropic investment.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxOZFNiUFJsMmw0dEhwOTdjNWtNRU54Z3hrSmV4LXNOMnMtTnZLcUNod1VNcUNjOVNCY0pvWWZKLXdHRTNVOVI2RzR0bDJEdlhuRzRvTUhLYUJ4a1hCcEdRRXRDakNPak02RnRUOGZ5cHRuRjZWSUsxV003ZVFveUFVTFlVc2M4VTZPWWs5aEJSQzZ6bGlmLWt0V2E2S2ZZR0VlSW5wdko1c2REM3pvUnl4X1hscjVBN29hZmJJZUZsR1FyUTd5RlgyTHNCQU41OExSLWIwaGRn?oc=5>

## HEADWINDS

### Amazon Stock (AMZN) Falls 3.9% After Anthropic IPO Debut (Nov 19)
- Summary: Amazon Stock (AMZN) Falls 3.9% After Anthropic IPO Debut (Nov 19)
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxOejFaODVKV0NVTXhtWFRJTjNhVmh5SFhiRl85T3VIYm1hUWZJeUF4RENfNFlQc2NLN2NBUFROSk9aRE8wN3dsdUNrTFJHR0h2NDZGTTczNld3NVRsRlBYY1lldHYxckZnODF5TTZHRm12Qk5RNThEVWxhZWVFYlpNbQ?oc=5>

### Amazon Stock Falls 4% as Nasdaq Crashes 5%: Is AMZN a Buy?
- Summary: Amazon Stock Falls 4% as Nasdaq Crashes 5%: Is AMZN a Buy?
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOSGR2Y01NTm9pWUx4Q2g1cllsVUUwdTd5Nk5MN3k1RzM2bWhBcDFtN0FFN09UTHgyMU5mQ3lfc1I0cXlVTnhBWjBiTDlKTmJ6WDg1d0YwV2lTVjY2VTlWQ3R5WFE3U3dsaUJoUVMyUFNUMVJ5VzBVTnVlV3lJa2dsVE1Oc0VUTThZbGc?oc=5>

### Amazon.com (NASDAQ:AMZN) Stock Falls 3.9% - Here's What Happened
- Summary: Amazon.com (NASDAQ:AMZN) Stock Falls 3.9% - Here's What Happened
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOSzU4aVNRUDd2aEJiRHFaRUZ4NHoycXBPUkVmQUtudmFMSkhWT3R3MDhpMHowRUhENmhJSnVJeU4xdTdSNFp3SkJWcGpZVHVTMHFERmNmNWFsVi1UWEdEc2pUTVFxbHA0VnlOSzhqLVJZYy1XdVZDNHZNeWRpYUluN0pRZUpGRVZhYUhxRUtrRWxSZ0ZCUW9Bdzg3ZlBOSFRGRjg3dzVxTTdqRldaQjN0dVFuQll5WFU?oc=5>

### Stock Market Today, Nov. 20: Amazon Shares Slide on AI and Mega-Cap Tech Sell-Off
- Summary: Amazon shares fell amid AI concerns and a broader tech sell-off.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxOZ3Q4VjNVRWVxOW90cDAtdDVDc1V0eXZGZ3gxbHhCQlhGUC1aTFNqTmtrU055TklQUjZreGR5NkRHU1FvblFOajBsWnVncTVhVnA3NTEzaWlQUFh0UjZMR0FDa2pINmlZSnItYmtHMDJ4TnhRclBFbnJzVXFvalg2UEJhQlZkTmJMQnc1dkJ2MVF5dTBFM3RYY3VBanF1blJOYzUxbGF2cHhvY2FBV3hXcURYb0VWamxSZVRxN3BWSGZoQWtqMEtaaWJ6SFFXNjBjbmtvOVFB?oc=5>

### New York City legislation could upend Amazon's delivery model (AMZN:NASDAQ)
- Summary: NYC law may force Amazon to alter its delivery operations, potentially increasing costs and reducing efficiency.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQMm14N0pvX2NlNEJxQW5UZWJqX3pyQVVoNzJZdGpFTG9WeWZUTVNtTnZRZWZ5SkxPUVNMQ2EwM3I5SFllM042QVhXd0c3a3JuM2ozeTVlX2JnTk9mT1VDNkdBVExxZnF2UFRqYjJTUmx5bDRfLWFfM1FEZEQ2UkM5V2R6N19Ibm1TS294Z3M4cFhIVEMwckwxN05qSG9QSkE?oc=5>

## CATALYSTS

### Amazon Stock Rises 4% After Announcing Acquisition of AI Startup Decart AI
- Summary: Amazon Stock Rises 4% After Announcing Acquisition of AI Startup Decart AI
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOeGZMRDlrbE1hb21mc28zX0JxOFNacFNmWVNYZzJ3cnVOeWd0TTdMNlJ0RGNxT1FRSkdvNEdqSi1fN2NueW9yeEdGaUxmNVNyd052SWZoSTl6QTA4WmNIWDQ5eWVDUWl4TW1sYU1PRHV0MU1iNFBJY05DSWNzdTNwbmRaZ0xiR2xpUE8zNnd5R2VNaWpTTFlucWVfR1dYcm1zZUU3WnhKTFI5V2M?oc=5>

### Amazon (AMZN) Stock Trades Below Fair Value As Its 82% Run Continues
- Summary: Amazon (AMZN) Stock Trades Below Fair Value As Its 82% Run Continues
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQUUtfMDhmNWV5dFk3RkdyTDhlTi1NZ2U1QmVMXzBhWmZwWHlGWktLSk1kbUFJUTVEUjYybDFxT2NJMjFRa2lySmw2bkVSdXFtcnpxaEFsbWF1MEhPX3FVLUxFSXAyTmM4LXJwVUVSS29KTWtxejlYYjZVejNGTW9FbXpmUFBzRE53Yi11TnBUVnAyYTBLNllfQ2E2OA?oc=5>

### Amazon nearing $7.5B deal to buy AI start-up Decart: FT
- Summary: Amazon nearing $7.5B deal to buy AI start-up Decart: FT
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPeWc2UVNPUkd5Zkphdnk2U0VVcnpReDhobWoyNEtSemI4cUhlMDBpZGhiTm51TWpORk1YQ3dBS1g3YzN1TlN6aFQ1azRPZ19wYWhEQnpkSy1rSGhocjk2V3MwYXN6cjVTQm0za2NiTGNxWUJXUDhJNUtfTHNyZkVRRGVwbGE1dDBQc1E?oc=5>

### Amazon (AMZN) Stock Trades Below Fair Value With AI Cash Flow In Focus
- Summary: Amazon (AMZN) Stock Trades Below Fair Value With AI Cash Flow In Focus
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNcWlDUlo1X0dLWE1CbGY1dUg4cXRPaDgtRFRHN1JWRGxOTktkbzFRV1VTWnQ1VmMzUDUwTWloa2l5RVdtU0FuZC1kbHR1X2N4bEdHMHg4TEZ2bGV6LTM0d2FvVFg4emU5RjlJbHRXOXhReFBUbEZQREZfeHNFclBlcFNnQzlaLW13czBwbUVSakJrUG14eG9OUS1lY2lFMFBXOGZTZzdNZHFVXy1xQWVidEM5Rm5oYndMVnB3YTFIZkJxdlXSAcgBQVVfeXFMTkQzTnB5bEJNOHNlbjJVOFpVbFVzQXdQb0lxV19wQWp4OE5SU3hSQnFmMWM0dmZvU1hHeWh4cWZ6a1N6WU1EbXFHNW9LOVlXZmFEaDB3M2F3Y3ZrN0dKcklScDBWSEZxUWlmR2xfekdGbEQyN1pVNEdtMkhPOFd2UkZHVHBnalVhZkJublJoQkdueWd0LVMxWFhmWm9NUDJIRjVVUHRZYjJIRlJpUWFUU2NmeGE1bnE3VWJxWHl2cGtOa1JVQ2tQbkY?oc=5>

### Amazon.com, Inc. $AMZN Stock Acquired by Pathway Financial Advisers LLC
- Summary: Amazon.com, Inc. $AMZN Stock Acquired by Pathway Financial Advisers LLC
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNcFpfM2FRQkJObWxDajQ4OURuNEp0MFVaOFdXbG9hb0I3dUNpaG5DR1hmWW5TbVBFdW4xZ0JnblF2MEVCOWZEUUFkcWgybkxPRlNxaEtWNmxWc0RtcnpDcnpqanJwTTRTNllEVE9DeFFTblJXam91Rl9uSHdINWlMOXQxRGYxU19lMUpnQWxOdHJ6SXdSdEJrUG5ZYzdrRFhIdUhIaXBiNkdiV09aUDFmZ2pHUUlOMG5DUkZLbkdlNVJXNmFjN2xB?oc=5>

### Amazon.com, Inc. $AMZN Stock Purchased by Third View Private Wealth LLC
- Summary: Amazon.com, Inc. $AMZN Stock Purchased by Third View Private Wealth LLC
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQdTQxTEpPbldhX0NMaEE4WUpnUkdJWExSWWRwdm5RSnNiSkJuVXNRYnBhQVhjMDNWSWRSdTh2aGhMM0tzbTFpY01qak5TUHJzc0ZydEVNYV9UWTJ1c20wMk5Pd2FwY3AyZVdpX2tMWlB2QnQ5cGg0NTNLRG4teHM1Mk9BN2lGUWMyXy1tX1FNZ0lNUk5DbXN3X2JsWkM4X0dWSzQwX2VBSHRzSTRZV0kwTy1ha21wemFWLXNkaHYwRng1Ml8yVGN3?oc=5>

### Amazon.com, Inc. $AMZN Stock Acquired by 3Chopt Investment Partners LLC
- Summary: Amazon.com, Inc. $AMZN Stock Acquired by 3Chopt Investment Partners LLC
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQNHRKVHZFZTB6U0wtT1pUX3NEQjlQMHZjdFV2OU5RTUdRdmI4RHBfZ2lZanVHSGhzTWlUazV6alN2U21McFdGNXBsVl94cmkwbVo4RUZnT04tQ2FNVl9RMVdiR1ZKMXMtODk5eThYUEtqaWVvWDBDVFR2VXZURkdfVEZUZjh3OGRoUHhhTDJtUjRoOG5RZkFnN2ozTE03NUd3eTBBZkVHVGZLelpoX3pVWkRjRHA1OFNDSll2cjJkbXRsWG1PZENR?oc=5>

### Amazon.com, Inc. $AMZN Stock Purchased by Attestor Capital Ltd
- Summary: Amazon.com, Inc. $AMZN Stock Purchased by Attestor Capital Ltd
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNM0lrRnJCc0ZCS0tPZGQyOFZvR2VNdWVEeVVySjMybXQzRjA1czFrRXhQTnhWamE0SklwVm5NZE5NTmdBb0RnZTlGU3V6UjRKbnVMaVdzRlJnaWtnZnBodTFiUVRDeUNkdGlhTFdQSWZOTDJ1dHNKYzFpMjIydWQ3V21reWFkZkJRY29uSnp4UWtWX2tkT0Nvc1FDX3pqUUxfdXlJQ2pRQnAxcmNFaTlUdVBPYWhiT0FETXNr?oc=5>

### Amazon.com, Inc. $AMZN Stock Bought by Oregon Public Employees Retirement Fund
- Summary: Amazon.com, Inc. $AMZN Stock Bought by Oregon Public Employees Retirement Fund
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxNc2hhNUhvTWluN1JCQ08wYzdIYjNxXzc4MDMyUFBnRTVXMlAtSUxucFE3NENhRGRHeDJfZGVYYmwwa1g0RmZCb24tbWpETjlUc0dBZWtBckJtLVlKYV9HY0FSZEY0Sm9Zdnh4TFRFcUhjd1FLNTlfNVJtVkNUd0hndUxUV2RLVXBvMGdpZ0tMNzd4YXdiMFMtb0tpcU1pMldYUEJvU1lYSHpWNS1PeXZDV0xRUnI4ZXFCMFBxUXhlVmpidUhvQW54TTdsRjNTc1JY?oc=5>

### Amazon.com, Inc. $AMZN Stock: StrongBox Wealth LLC Grows Position
- Summary: StrongBox Wealth LLC increased its stake in Amazon, indicating confidence in the company.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxNaVBIUTY5M3V2TmktVXcyT2NhYmhxbHRYRlFFV3dkcjBhWGRNZ1lES2pIaEJfSU9nY3RGS2NQaDFIejRyV0VjcC1NOHBad1Q3VjZ4eE5hd0JmRHI4cnJPLVpZcTFFVDYwSVpmbW1zVTgxSFpTUV9KSWFBeFg1UkZGZWgxUlZkZzhzVTVmYnJmUjBnTnVkUWxIaGU4VERZdXRfY2x3WXg4ZklkcGlCT1pwM1VMbzluMWx5ekwxTmln?oc=5>

### Amazon.com, Inc. $AMZN Stock: GRIMES & Co WEALTH MANAGEMENT LLC Grows Stake
- Summary: Grimes & Co Wealth Management increased its Amazon holdings, signaling confidence in the retailer’s prospects.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxNWGNoUTJZS3A0VTlPXzN1U3R3X1hkSG5qV0xVbm5YaEUzOTFCSDVwM09KY0F3OXhELTFERFFMM0tYNDk3VTVYZGp5UjJTSERSei05TmhBdmltTkRkZHM5Sm9lMElSa182cFAwR2N6UzB0ak5EYU5zdW1IWng0VVNiT3FVSGg3eDZ5X0RGN21JbGpxRjVwOG1EZkl2RTF2WWxGZG0wMi1EaElnU0RNN1BHbUdUdWZJa0FzZ016aHp2NzJ4eF9LbG5lQg?oc=5>

## RISKS

### Jeff Bezos predicts Amazon will eventually 'go bankrupt' and shares 30-year rule behind it
- Summary: Bezos warned Amazon could go bankrupt, citing a 30-year rule.
- Date: 2026-11-22 | Impact: high | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOeWdMeV82cExKX1NFdklKcjc5eUNDOGJGdmJjNXZRVXFIRTJWSktvNHlDREY4THJtMmNwN1YtSXNRNFM0MDIzdno3VDcyZmN4YlI5SWNJZW9ZREpPeC0wMURzOVJSYlNwWmw0cHpfa25hb1ZBWDlCWWJKTkZsYUdUWGtDc0dvOEhERjBHYTN5TTNEa29SYmdSQk4xUExKRkt2b001MQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **20.65** | **4.50** | **16.07** | **12.10** | **2,761,567,240,192.00 USD** | **15.72** |
| WMT | 46.95 | 10.48 | 22.64 | 5.20 | 1,031,207,911,424.00 USD | 24.07 |
| MSFT | 25.70 | 7.77 | 18.12 | 18.80 | 3,657,400,844,288.00 USD | 5.18 |
| GOOGL | 14.73 | 5.26 | 18.17 | 24.70 | 3,468,137,332,736.00 USD | -5.62 |

Peers fetched as_of: 2026-11-23; AMZN reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-30
- Revenue (latest available single quarter): 201,944,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 20,685,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxPZzNaYkdqazhvS254MUt3MjVTaFcxNzV6Q2NGYlZ2eHdaUm9XS3FyTkR5WkRHX3A1SjBEQ1QtY0djSC1iTUdpRkl2bUZudFRwM2ZUcDV1eHRhRVJObXNpRFBaYjMwZDdnNWhmdkVwZkpCa0xCRWtMNkZpX2xQLXg1eENFUjV6YXROaEQ2SlhJMk9KSVZhUGJKaw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOd3EzOU9yRkc4NDAwWmxwN0dpeF9DdHJpNFpmN1hfV2poTUZkY21xcW1jNXAyR1BIU3NDZnpPQ0M3Z2NYMG1xeTAzRXpwTUplOTB5SHZ0R2xtNjNmajRrVWxCTVl0ZGpiUEtnS1FRRFpIMUE2dFlYZUo2WXFEVXNkM1JEYU1DdW5vS05YbXdwcW10dWJwS0ltdDVQd0xBLXVfOENXRUdn?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQdEFnQ1liWFJrVDBPTkV4Umt0SEw3V3FvWDZoeTRZczNlYTlKLXBZM2dNVThEcXRkUm9KV0ZCTUFQTVJFWnhqcVk2NWQ5V2ZsbzZBUldEbTg0b0o2VDlCRklDNUlFRHk4X2RwRGZOa1ZOcnpfZmpONEtoU3ViZWVGTTh6RGJzSENlNW9QOXptcmEwQ3NmdmxydGtEdXp2Z3RUYlRJLWI2a3BzUmg0Z01xY3I4akVmWElWbWc?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPUENIZzZ3ZEZURzJfdzgteDlHYTJZckpaZWZQeFhXeXhfdWlaSzhxZ1pURG1UckNleDFEZVU3V2l1X3dlZkFLdE5EbXJyWTh3Y2Q4VmhkbmtubXhWZVB3NEVNeUtZSVloYXpoejdlMTNERHFhUXg4WU5RM3hONlo4TlNkM0ctTFpEN0ZJZElfcGtoNGFTbEFwVkc1Z3d2c0tuM2NIQWZMcVBzbVE5WG9rN3hNSW1GazhGaVpxV2kycF9KUQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNY3FYSHN1WVd5R2I5T0lTUXhrMmhMRVhwZ0FiTEZGTHRmaF92aHF2LUFpLVpWSXpUM2ZKYXdmbWRZUkp1MkV4aDluQzZSNncxTURrcmF2bU8xTWRFNzE2NU15WU1jVkRFY2NWeDFDekVQRjBHdi1tODg4SUtwR1pkajcwVmNjYmVEUFVteUVqOEk5elBpUkt4TjBVVEdFc0dTVm9qQ1lHN0MtQQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOYUI4dW4yVFZLUmNocWJ3SmJ4MFhaTGRrcFVqd2ZUak1sdDYwSlR6YkJjUHkya1FaQzlmQkduYVRDYkhKa0w1ZHBvYkFSZXlLOGNlVmxLcjdMclgxaUlZTi11VmJwYUpuUXVuWU13WVE3UFhPRjgyek1MTkNUckhHMkd6cVVfNGoxc3Vn?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOMXdBQUpoQ2EwOFVBdW5HQWtaTXdVVTJqbjJZczdqRFZJdDJ3bHMzQmVQU2RVTF9ISmNxcFRXV2VJeWdDNURIZ0duc2pTX0lVZmE4WTREb3NaQmIyM1JfMzBqNFpENlBjTEhoVlZPc3I1bHdkVFowWEkyWXFib1hDbWF6bUJKS2pobVg1OW5pZFZqUElibGNJVQ?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxOZFNiUFJsMmw0dEhwOTdjNWtNRU54Z3hrSmV4LXNOMnMtTnZLcUNod1VNcUNjOVNCY0pvWWZKLXdHRTNVOVI2RzR0bDJEdlhuRzRvTUhLYUJ4a1hCcEdRRXRDakNPak02RnRUOGZ5cHRuRjZWSUsxV003ZVFveUFVTFlVc2M4VTZPWWs5aEJSQzZ6bGlmLWt0V2E2S2ZZR0VlSW5wdko1c2REM3pvUnl4X1hscjVBN29hZmJJZUZsR1FyUTd5RlgyTHNCQU41OExSLWIwaGRn?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxOejFaODVKV0NVTXhtWFRJTjNhVmh5SFhiRl85T3VIYm1hUWZJeUF4RENfNFlQc2NLN2NBUFROSk9aRE8wN3dsdUNrTFJHR0h2NDZGTTczNld3NVRsRlBYY1lldHYxckZnODF5TTZHRm12Qk5RNThEVWxhZWVFYlpNbQ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOSGR2Y01NTm9pWUx4Q2g1cllsVUUwdTd5Nk5MN3k1RzM2bWhBcDFtN0FFN09UTHgyMU5mQ3lfc1I0cXlVTnhBWjBiTDlKTmJ6WDg1d0YwV2lTVjY2VTlWQ3R5WFE3U3dsaUJoUVMyUFNUMVJ5VzBVTnVlV3lJa2dsVE1Oc0VUTThZbGc?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOSzU4aVNRUDd2aEJiRHFaRUZ4NHoycXBPUkVmQUtudmFMSkhWT3R3MDhpMHowRUhENmhJSnVJeU4xdTdSNFp3SkJWcGpZVHVTMHFERmNmNWFsVi1UWEdEc2pUTVFxbHA0VnlOSzhqLVJZYy1XdVZDNHZNeWRpYUluN0pRZUpGRVZhYUhxRUtrRWxSZ0ZCUW9Bdzg3ZlBOSFRGRjg3dzVxTTdqRldaQjN0dVFuQll5WFU?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxOZ3Q4VjNVRWVxOW90cDAtdDVDc1V0eXZGZ3gxbHhCQlhGUC1aTFNqTmtrU055TklQUjZreGR5NkRHU1FvblFOajBsWnVncTVhVnA3NTEzaWlQUFh0UjZMR0FDa2pINmlZSnItYmtHMDJ4TnhRclBFbnJzVXFvalg2UEJhQlZkTmJMQnc1dkJ2MVF5dTBFM3RYY3VBanF1blJOYzUxbGF2cHhvY2FBV3hXcURYb0VWamxSZVRxN3BWSGZoQWtqMEtaaWJ6SFFXNjBjbmtvOVFB?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQMm14N0pvX2NlNEJxQW5UZWJqX3pyQVVoNzJZdGpFTG9WeWZUTVNtTnZRZWZ5SkxPUVNMQ2EwM3I5SFllM042QVhXd0c3a3JuM2ozeTVlX2JnTk9mT1VDNkdBVExxZnF2UFRqYjJTUmx5bDRfLWFfM1FEZEQ2UkM5V2R6N19Ibm1TS294Z3M4cFhIVEMwckwxN05qSG9QSkE?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOeGZMRDlrbE1hb21mc28zX0JxOFNacFNmWVNYZzJ3cnVOeWd0TTdMNlJ0RGNxT1FRSkdvNEdqSi1fN2NueW9yeEdGaUxmNVNyd052SWZoSTl6QTA4WmNIWDQ5eWVDUWl4TW1sYU1PRHV0MU1iNFBJY05DSWNzdTNwbmRaZ0xiR2xpUE8zNnd5R2VNaWpTTFlucWVfR1dYcm1zZUU3WnhKTFI5V2M?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQUUtfMDhmNWV5dFk3RkdyTDhlTi1NZ2U1QmVMXzBhWmZwWHlGWktLSk1kbUFJUTVEUjYybDFxT2NJMjFRa2lySmw2bkVSdXFtcnpxaEFsbWF1MEhPX3FVLUxFSXAyTmM4LXJwVUVSS29KTWtxejlYYjZVejNGTW9FbXpmUFBzRE53Yi11TnBUVnAyYTBLNllfQ2E2OA?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPeWc2UVNPUkd5Zkphdnk2U0VVcnpReDhobWoyNEtSemI4cUhlMDBpZGhiTm51TWpORk1YQ3dBS1g3YzN1TlN6aFQ1azRPZ19wYWhEQnpkSy1rSGhocjk2V3MwYXN6cjVTQm0za2NiTGNxWUJXUDhJNUtfTHNyZkVRRGVwbGE1dDBQc1E?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNcWlDUlo1X0dLWE1CbGY1dUg4cXRPaDgtRFRHN1JWRGxOTktkbzFRV1VTWnQ1VmMzUDUwTWloa2l5RVdtU0FuZC1kbHR1X2N4bEdHMHg4TEZ2bGV6LTM0d2FvVFg4emU5RjlJbHRXOXhReFBUbEZQREZfeHNFclBlcFNnQzlaLW13czBwbUVSakJrUG14eG9OUS1lY2lFMFBXOGZTZzdNZHFVXy1xQWVidEM5Rm5oYndMVnB3YTFIZkJxdlXSAcgBQVVfeXFMTkQzTnB5bEJNOHNlbjJVOFpVbFVzQXdQb0lxV19wQWp4OE5SU3hSQnFmMWM0dmZvU1hHeWh4cWZ6a1N6WU1EbXFHNW9LOVlXZmFEaDB3M2F3Y3ZrN0dKcklScDBWSEZxUWlmR2xfekdGbEQyN1pVNEdtMkhPOFd2UkZHVHBnalVhZkJublJoQkdueWd0LVMxWFhmWm9NUDJIRjVVUHRZYjJIRlJpUWFUU2NmeGE1bnE3VWJxWHl2cGtOa1JVQ2tQbkY?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNcFpfM2FRQkJObWxDajQ4OURuNEp0MFVaOFdXbG9hb0I3dUNpaG5DR1hmWW5TbVBFdW4xZ0JnblF2MEVCOWZEUUFkcWgybkxPRlNxaEtWNmxWc0RtcnpDcnpqanJwTTRTNllEVE9DeFFTblJXam91Rl9uSHdINWlMOXQxRGYxU19lMUpnQWxOdHJ6SXdSdEJrUG5ZYzdrRFhIdUhIaXBiNkdiV09aUDFmZ2pHUUlOMG5DUkZLbkdlNVJXNmFjN2xB?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQdTQxTEpPbldhX0NMaEE4WUpnUkdJWExSWWRwdm5RSnNiSkJuVXNRYnBhQVhjMDNWSWRSdTh2aGhMM0tzbTFpY01qak5TUHJzc0ZydEVNYV9UWTJ1c20wMk5Pd2FwY3AyZVdpX2tMWlB2QnQ5cGg0NTNLRG4teHM1Mk9BN2lGUWMyXy1tX1FNZ0lNUk5DbXN3X2JsWkM4X0dWSzQwX2VBSHRzSTRZV0kwTy1ha21wemFWLXNkaHYwRng1Ml8yVGN3?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQNHRKVHZFZTB6U0wtT1pUX3NEQjlQMHZjdFV2OU5RTUdRdmI4RHBfZ2lZanVHSGhzTWlUazV6alN2U21McFdGNXBsVl94cmkwbVo4RUZnT04tQ2FNVl9RMVdiR1ZKMXMtODk5eThYUEtqaWVvWDBDVFR2VXZURkdfVEZUZjh3OGRoUHhhTDJtUjRoOG5RZkFnN2ozTE03NUd3eTBBZkVHVGZLelpoX3pVWkRjRHA1OFNDSll2cjJkbXRsWG1PZENR?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNM0lrRnJCc0ZCS0tPZGQyOFZvR2VNdWVEeVVySjMybXQzRjA1czFrRXhQTnhWamE0SklwVm5NZE5NTmdBb0RnZTlGU3V6UjRKbnVMaVdzRlJnaWtnZnBodTFiUVRDeUNkdGlhTFdQSWZOTDJ1dHNKYzFpMjIydWQ3V21reWFkZkJRY29uSnp4UWtWX2tkT0Nvc1FDX3pqUUxfdXlJQ2pRQnAxcmNFaTlUdVBPYWhiT0FETXNr?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxNc2hhNUhvTWluN1JCQ08wYzdIYjNxXzc4MDMyUFBnRTVXMlAtSUxucFE3NENhRGRHeDJfZGVYYmwwa1g0RmZCb24tbWpETjlUc0dBZWtBckJtLVlKYV9HY0FSZEY0Sm9Zdnh4TFRFcUhjd1FLNTlfNVJtVkNUd0hndUxUV2RLVXBvMGdpZ0tMNzd4YXdiMFMtb0tpcU1pMldYUEJvU1lYSHpWNS1PeXZDV0xRUnI4ZXFCMFBxUXhlVmpidUhvQW54TTdsRjNTc1JY?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxNaVBIUTY5M3V2TmktVXcyT2NhYmhxbHRYRlFFV3dkcjBhWGRNZ1lES2pIaEJfSU9nY3RGS2NQaDFIejRyV0VjcC1NOHBad1Q3VjZ4eE5hd0JmRHI4cnJPLVpZcTFFVDYwSVpmbW1zVTgxSFpTUV9KSWFBeFg1UkZGZWgxUlZkZzhzVTVmYnJmUjBnTnVkUWxIaGU4VERZdXRfY2x3WXg4ZklkcGlCT1pwM1VMbzluMWx5ekwxTmln?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxNWGNoUTJZS3A0VTlPXzN1U3R3X1hkSG5qV0xVbm5YaEUzOTFCSDVwM09KY0F3OXhELTFERFFMM0tYNDk3VTVYZGp5UjJTSERSei05TmhBdmltTkRkZHM5Sm9lMElSa182cFAwR2N6UzB0ak5EYU5zdW1IWng0VVNiT3FVSGg3eDZ5X0RGN21JbGpxRjVwOG1EZkl2RTF2WWxGZG0wMi1EaElnU0RNN1BHbUdUdWZJa0FzZ016aHp2NzJ4eF9LbG5lQg?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOeWdMeV82cExKX1NFdklKcjc5eUNDOGJGdmJjNXZRVXFIRTJWSktvNHlDREY4THJtMmNwN1YtSXNRNFM0MDIzdno3VDcyZmN4YlI5SWNJZW9ZREpPeC0wMURzOVJSYlNwWmw0cHpfa25hb1ZBWDlCWWJKTkZsYUdUWGtDc0dvOEhERjBHYTN5TTNEa29SYmdSQk4xUExKRkt2b001MQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
