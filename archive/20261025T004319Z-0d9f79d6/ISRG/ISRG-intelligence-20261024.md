# ISRG Intelligence Report

- ticker: **ISRG**
- Report as_of: **2026-10-24**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/ISRG/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ISRG/key-statistics/
- AI analysis snapshot as_of: **2026-10-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-25T01:07:24.993100+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 10, 'ai': 8, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 10 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 52.0%; oldest publication 2026-10-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 452.2900 |
| Return 1D (%) | 1.9015 |
| Return 1W (%) | 5.9972 |
| Return 1M (%) | 13.5551 |
| Return YTD (%) | -20.1409 |
| Return 1Y (%) | -17.9594 |
| Annualized volatility (%) | 33.9925 |
| Beta vs SPY | 0.8773 |
| Max drawdown (%) | -43.9960 |
| Sharpe (rf=0) | -0.4122 |
| Downside deviation (rf=0, %) | 25.6428 |
| Sortino (rf=0) | -0.5465 |
| Historical VaR 95% (1D, %) | 2.8853 |
| Historical ES 95% (1D, %) | 5.0452 |
| Correlation vs SPY | 0.3290 |
| Tracking error vs SPY (%) | 32.1386 |
| P/E (trailing) | 54.69 |
| P/B | 9.81 |
| EV/EBITDA | 34.19 |
| Revenue growth (%) | 21.70 |
| Forward P/E (estimate) | 36.39 |
| Gross margin (%) | 66.64 |
| Operating margin (%) | 33.29 |
| Return on equity (%) | 17.93 |
| Free cash flow yield (%) | 2.15 |
| MA50 | 396.0584 |
| Close vs MA50 (%) | 14.1978 |
| MA200 | 436.2119 |
| Close vs MA200 (%) | 3.6858 |
| RSI (14, Wilder) | 70.8426 |
| MACD (12,26) | 13.3887 |
| MACD signal (9) | 11.4329 |
| MACD histogram | 1.9559 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ISRG': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 452.2900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.9015 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.9972 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 13.5551 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -20.1409 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -17.9594 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.9925 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.6428 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.5465 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8853 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.0452 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3290 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.1386 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8773 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.9960 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.4122 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 36.3867 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.6420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.2860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.9320 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.1497 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 54.6904 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 70.8426 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.9559 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 14.1978 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.6858 -> Slightly above the moving-average trend level.

## TAILWINDS

### Intuitive Surgical, Inc. (ISRG) Q3 Earnings and Revenues Top Estimates
- Summary: Intuitive Surgical, Inc. (ISRG) Q3 Earnings and Revenues Top Estimates
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNcm41Vm1GV3RMdTR4b0RQMUV5NTk5Q0NVMkJ6d2tpbWZaelhqM1paa2ZFTUpCZ3dQRXVNU0VadjFWVU9VdXNFcGdJTmEwX21Cb3d3cF9OVG9ocEtmTjNhQlN4MUhJaU9lNUFSNm5Ia2tRdnBZZTRaRlRpbkh3QTNqbDNBY2ZIaTAwd255MXBPazNBQkJzS3N1Y3p2dw?oc=5>

### Intuitive Surgical: 3 Key Takeaways for Long-Term Investors
- Summary: Highlights long-term investment insights for ISRG.
- Date: 2026-10-21 | Impact: low | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQYnZBdDIwN3hjWU91RUNQQXAtV1hHaFI1ZlJNYXhWcHkwRlZObDlYR3lXU0ZoOFF0cXJGTXdpYllWT3dhRkRTNjJITFlkLTZ5SVlIT0J5NEJSQUZXX0F6VDM2YkpNN2U0LWhNS1lVdjdNUzg0bHd0T3ZzY3JobEd5c19CcHBlX1pTRnJ0U1U3b1FlN0Zfczd4eW05S1ZpUDdp?oc=5>

## HEADWINDS

### Intuitive Surgical stock drops after Q3 beat (ISRG:NASDAQ)
- Summary: Intuitive Surgical stock drops after Q3 beat (ISRG:NASDAQ)
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxOaHNmbUs4MTcwdVdmcVQ5cTFraThfY0xXTFdpbzkwMVU2R050cTdVRndfR05uSTMwYXltanJHOFhRcXFsLTBweGpGY0txS2l6MDQ3STc4U2xTMzFDN2NXTVlZRExDbldkRnVaa1pUZUp5dlZ2d2UtdkdNMU9Oc3d5dlJ3?oc=5>

### Intuitive Surgical Stock Slides Despite Earnings Beat as Company Discloses Settlement
- Summary: Intuitive Surgical Stock Slides Despite Earnings Beat as Company Discloses Settlement
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxPc3RHTVVTcl9rNTlEb2t2R3Z0czF3YVJQdXZPYTZoSnFTUEszSzhXODFHQUV0bjN5LV9EbEpQSHlxZHJhTGhtOHYyTndsZkpLM1RvNWVTdXRTM25Gd1JOUXJvWFdrVzJaLUx5RXlDYzd1VkJDRjdYVjRsUVZ0ZXRueHFWUVJ2WnZL?oc=5>

### Intuitive Surgical slides 13% as earnings hit by pre-tax charge
- Summary: Intuitive Surgical slides 13% as earnings hit by pre-tax charge
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQcUlHMmEzU1U1eGkwZnk3OXk4b002MkkyTVRwYmI5UU91Zjhkd1VzX3BtNHJLeXNLYlJ0RkJRMW5MMmFWYTZEZ1JudnBwMlptYjcxdXpSdkdRMU9Za1hibDJ2OEtWVGxhbjU5N2pxdlZzNlFFNDRQaUswTUNUODNKTk1oR3BRZndIUW1zR1FhM21kZXZYZW9WNHFmbDloLWlUTkVJTlUta1NiZEFFQ1V1U09zbTg?oc=5>

### Intuitive Surgical (NASDAQ:ISRG) Reports Upbeat Q3 2026 But Stock Drops 12.7%
- Summary: Intuitive Surgical (NASDAQ:ISRG) Reports Upbeat Q3 2026 But Stock Drops 12.7%
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPWTRFbm43RUZrNnpvUXBvWW5mZnh1bTBqVHlrMFRQbWdmM1dvYkZGUHR1aHJhUG0xbW05TExUZC1odXVIWUZNMmlNakRsb0J4WkJIN2FQcGVydGdxN3owVGJMNmJwLThiZEVxQ2prYTJvUnRlS1p2QzF4aENVMl9JWGc2d2NNWmY0ekJEYUQxcGhFVWpDUUI5MjFHSE1LWnN6Qm12bWtn?oc=5>

### Intuitive Surgical (ISRG) Stock Is Down 25% Year to Date. History Says Patient Investors Get Rewarded.
- Summary: Intuitive Surgical (ISRG) Stock Is Down 25% Year to Date. History Says Patient Investors Get Rewarded.
- Date: 2026-10-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOM2E0TktaZnZmbE1vNXZGWTRhMUNlbkkya3Y5TDdVdXMtajdQaDE4Zm5VVVlTbUdPcURmQThMdm5PTDZfdHNwWmRTbkwyd3VTMWYzcGJOMThneGJrUXNkVjJ0dFktSDFrcjBuWkxLdENLRVpocFU5YXZfTFlRTHk1eEhMQnpvVWU3enNCaFgzOUlSYWFUOXc?oc=5>

### Intuitive Surgical (ISRG) Shares Fall Nearly 7% After Q3 Earnings Beat
- Summary: Intuitive Surgical (ISRG) Shares Fall Nearly 7% After Q3 Earnings Beat
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPejhyNTZVazBOYWlmd0YwNlgxWXVXWFU1MFkzUFVXaGU1TWREd0dtTUFPUGlXeVZYQTVXeHlkT2xVM19IUzh3aGRnWVJGeE1QYUIyMm9oaGNsT2drWjFsVXpFTDVzQXBXV2tXWDZOcDFxVFRfOHpiTkFDeTdxdV9ialhJRUJlY1FLSTQ2dUVEaEdaUWlpbVBIc0hBeWFGOEMzRk83VVVGckJiZw?oc=5>

### Update: Intuitive Surgical Drops as 2026 Global da Vinci Growth Outlook Tweak, $450 Million Charge Chip Away at Q3 Adjusted Earnings, Revenue Beats
- Summary: Stock fell after outlook tweak and large charge, despite earnings beat.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQZXVVcU1TV3VIM2pjVlZiWFZwUWw5MmprMHhZbjdIcDNaX1MyMTZQV3ZOamtiMGdzNFNHN1h1OVE3TFcxelVVa0s1a3gtODE3Q3RNZzRlVndfZG5xN0s2T3plelZraXZLUkd4RWZ6bGdLV3hUdGctYXdDRUJFcXlGV25JV3h6X2ctODVfc2xMYTZOZ21XZlIwUkZvdlNzdw?oc=5>

### Intuitive Surgical (ISRG) Shares Dip Despite Strong Q3 Results o
- Summary: Shares declined despite strong Q3 performance.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPVElCY21walNRbE1pRW15Wkx4ZnlZelNFamRpbC04cEdlTVBzejFYdGVqU2V5THhCOUFfSjBmTUk1NGR3RWVQQm80ZGxHb3F2TzYza2swN1RrSDdybllxbE9CSHF2aWtYbnl5czZDTnhmRllQeTllMWo0MVZ3cmVEelJ5ZjJ6dWFiQi1teFJ3aVlFZHJmclpOSEJuSE12cjdLakdWeVphZXV0cWZZZHFQRnowVy1zeDdQ?oc=5>

## CATALYSTS

### Intuitive Surgical (ISRG) Stock Faces A Q3 Earnings Valuation Reality Check
- Summary: Intuitive Surgical (ISRG) Stock Faces A Q3 Earnings Valuation Reality Check
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQU0JGbU5VQ1dmVmRnVi1URXY3VWpxT3otdU9LUzRhRm9xZUlzbGlzR3VGSFB6VDI1WHk3SlNsa2x2MjFrbVduQ2R3SVY3bVIwdUg1Z2VyQ3ZxaUVkN0dEMVlTUzhQUlV2TjVfNjVnLXE5WjNvY0FPbnA1MHNqRHNMR2UxSDhnYUM5SXZTdHZwdmhlY3lGSUgwYjZXU0dZdlI4Zmc?oc=5>

### Intuitive Surgical Earnings: What To Look For From ISRG
- Summary: Intuitive Surgical Earnings: What To Look For From ISRG
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNRHVISDg2OExqYWNHS25oYzdENGgtcDQzd0ltZkRJZ3B1SDZKVG51czc3dnkyb0gzSUhxTF9DSVp4blR1STl0S3ZIRG9JNjJ5ZWRUUzBkOGNCRWxJMTA0TFh0ZTltZ2paQ3VxZWIxY19jUWVWQWZTRmI1QnlPTXZzQ215YzlBckVFSF9oVzFXdzlfcmpwZVQ3azVSZFBWMTREQ0t2UQ?oc=5>

### Intuitive Surgical, Inc. 2026 Q3 - Results - Earnings Call Presentation (NASDAQ:ISRG) 2026-10-23
- Summary: Intuitive Surgical, Inc. 2026 Q3 - Results - Earnings Call Presentation (NASDAQ:ISRG) 2026-10-23
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTmpjcE5OT1pBOXJ4aGFzZkhja3VhUi1TcV9tNEI0cUd1TVVUeHF1ZzlNczhHWUplMkZqQXhHNDBELVdXTVZXU24yaHRVRTVPa0JTQW9tZnRadXN1MGNVTWhrQU5zUFcwZ2JaRVZNbFNQcHhNdkpJX0tNRTRhRzNUNUJON2pzY01DQ2ZUMVRlZkVGMmNTdmFMZFRuM1hpelpWVDRzUHdGQjBRZw?oc=5>

### Intuitive Surgical (ISRG) Stock Looks Reasonable After Mixed Q3 Results
- Summary: Mixed Q3 results prompt a reasonable stock valuation assessment.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxOdDRpdU9FbjgxbEJxbHVOSy1wTE9UazRNSG1Nc3AwaXRSTUJQR2lISUhyNzltWUZ6MWpFRXlRVWZkMk5uc2xZYnNkSXEzWUFoZUh0MEdiZTVwVVoxU190cmk5WGNUMlRyUTZxLXBIaTNDSUhybG9JRzFmcU5ibDNNenZRc1N0UUJCNmhwMXIwZFV3alpRalFpSmtjTkVfdFYtMUl5YWNFbXZUek5WMWlvZmFkb3ZyenhLMDlxSVkxck1JeDNMXzY3dE9nRWpMd2tGTEN4V0pB0gHbAUFVX3lxTFBEcm1NRjkyem5SRk52RVN6dUdBNHhDRXBXWnZNUzJJU0NadVNZWFFVR3ZMdGwyWVcwVENFd3N3RHB1bVlDV3FNMGRtT28yeUdHSjNzcC1mT0NfV3VEWFowbTE2WVpOUlFValduNnRBT0F4UFgydWNfQXpwVUVLVTZGc2Zvckh6ZDJJc1Yxeng4eUFiVkNiaHZDNlZDUzlKNWhzNmdydlpsc2JUc2lXRDM4bEFMLTNZSkJ6MWdHNHRHZllTN29rLU40T3c4bGNrekNaWG5TLUR2UEMwdw?oc=5>

### Intuitive Surgical Drops as $450 Million Charge Overshadows Beat
- Summary: Earnings beat offset by a $450M charge, impacting profitability.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQZEpVWk9BRU92NkhRQTRDcUpGMldvbVEyOVQxal9NT0t5WGE4dE5ESkNUejRVbDY0QTBtZDlFMDYzSUZtX00wSDg0azYySkJ0TTFuaHp2Y2pINmxWX0x6Qjdibm1ZRUttNml1VExLR0NUeFNMaFA1blhaekpmT1VyRkI3bjY5OHk2WEI3dnp1cmRrX3BGWnd0WjRhUi1aNm0xdmJF?oc=5>

## RISKS

### Robotics Titan Hammered On Elevated Buy-Side Views
- Summary: Elevated buy-side views lead to a sharp decline in the stock.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPbFQ1cWh6R3FnQ3BUZWJlMHNqazZUeExEN1RkQUMzeDBPcHgyOGxfZHI2eV82RkxQcWVXV2h2MDVOcWZaeGNEOEZDN29GcmdLTDR2S1lMaHpoTDFGQ1VjYTBxS010bkZGbmV1aGxmSW5tcFEyUTFzb3FrQno2aE5WV1JDMHlaU2FndDVRNHZYYkZ1alV3eWQ4RHEyb0ZCWnEtZlJmaDl3?oc=5>

### Stocks making the biggest moves after hours: Super Micro Computer, Intuitive Surgical, Netflix, SpaceX & more
- Summary: Intuitive Surgical experiences significant after-hours movement.
- Date: 2026-10-20 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxORXdWekxkMVpyM3RJa2dwOU81c2h2Qy1iQUd2QzkyVUNGMnEtZW9JNFVNZGZFMDRIOEdiNWVTZFdPbDBIdjhLMHNlVE1LbmtCNDZtODF2SEd4dTYtUGdQX05uSWhoS2NoZnVjUmQyajZfMFlBZ1BPMjhVUFlubVE5ajRVZGdqSGlkaWNucVdvd2JqV3ZUY012T0xJWQ?oc=5>

### Intuitive Surgical, Inc. (ISRG) Crossed Above the 200-Day Moving Average: What That Means for Investors
- Summary: Stock crosses 200-day MA, indicating potential bullish trend.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPZXloQXFGcFY4ckZHSTF3Wk5EaFh3d04yeDRSNXVVZTRlblF2WExJclFZRTNjUFJNVTc2TXpCaDdjRk1WdnJwQW9VMGJDbTV6cEJtazFKQzJ2VGYxX1BoeGFoZ1lZVVFsaHZBWExhQXRDblBBenA4RXVUTlp2NnF0cllrdnk0Y0VfUUpiOUVOZDhHYkJxZGxSaWYyRU5zZ3VCSVE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ISRG** | **54.69** | **9.81** | **34.19** | **21.70** | **159,784,124,416.00 USD** | **-17.96** |
| MDT | 23.44 | 2.43 | 13.64 | 13.70 | 122,042,556,416.00 USD | 4.63 |
| SYK | 31.83 | 4.91 | 17.60 | 9.40 | 117,814,460,416.00 USD | -18.93 |
| BSX | 18.50 | 2.65 | 13.75 | 7.50 | 66,215,297,024.00 USD | -55.38 |

Peers fetched as_of: 2026-10-24; ISRG reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 3,048,700,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 522,800,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1035267/000103526726000071/isrg-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxNcm41Vm1GV3RMdTR4b0RQMUV5NTk5Q0NVMkJ6d2tpbWZaelhqM1paa2ZFTUpCZ3dQRXVNU0VadjFWVU9VdXNFcGdJTmEwX21Cb3d3cF9OVG9ocEtmTjNhQlN4MUhJaU9lNUFSNm5Ia2tRdnBZZTRaRlRpbkh3QTNqbDNBY2ZIaTAwd255MXBPazNBQkJzS3N1Y3p2dw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQYnZBdDIwN3hjWU91RUNQQXAtV1hHaFI1ZlJNYXhWcHkwRlZObDlYR3lXU0ZoOFF0cXJGTXdpYllWT3dhRkRTNjJITFlkLTZ5SVlIT0J5NEJSQUZXX0F6VDM2YkpNN2U0LWhNS1lVdjdNUzg0bHd0T3ZzY3JobEd5c19CcHBlX1pTRnJ0U1U3b1FlN0Zfczd4eW05S1ZpUDdp?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxOaHNmbUs4MTcwdVdmcVQ5cTFraThfY0xXTFdpbzkwMVU2R050cTdVRndfR05uSTMwYXltanJHOFhRcXFsLTBweGpGY0txS2l6MDQ3STc4U2xTMzFDN2NXTVlZRExDbldkRnVaa1pUZUp5dlZ2d2UtdkdNMU9Oc3d5dlJ3?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxPc3RHTVVTcl9rNTlEb2t2R3Z0czF3YVJQdXZPYTZoSnFTUEszSzhXODFHQUV0bjN5LV9EbEpQSHlxZHJhTGhtOHYyTndsZkpLM1RvNWVTdXRTM25Gd1JOUXJvWFdrVzJaLUx5RXlDYzd1VkJDRjdYVjRsUVZ0ZXRueHFWUVJ2WnZL?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQcUlHMmEzU1U1eGkwZnk3OXk4b002MkkyTVRwYmI5UU91Zjhkd1VzX3BtNHJLeXNLYlJ0RkJRMW5MMmFWYTZEZ1JudnBwMlptYjcxdXpSdkdRMU9Za1hibDJ2OEtWVGxhbjU5N2pxdlZzNlFFNDRQaUswTUNUODNKTk1oR3BRZndIUW1zR1FhM21kZXZYZW9WNHFmbDloLWlUTkVJTlUta1NiZEFFQ1V1U09zbTg?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPWTRFbm43RUZrNnpvUXBvWW5mZnh1bTBqVHlrMFRQbWdmM1dvYkZGUHR1aHJhUG0xbW05TExUZC1odXVIWUZNMmlNakRsb0J4WkJIN2FQcGVydGdxN3owVGJMNmJwLThiZEVxQ2prYTJvUnRlS1p2QzF4aENVMl9JWGc2d2NNWmY0ekJEYUQxcGhFVWpDUUI5MjFHSE1LWnN6Qm12bWtn?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOM2E0TktaZnZmbE1vNXZGWTRhMUNlbkkya3Y5TDdVdXMtajdQaDE4Zm5VVVlTbUdPcURmQThMdm5PTDZfdHNwWmRTbkwyd3VTMWYzcGJOMThneGJrUXNkVjJ0dFktSDFrcjBuWkxLdENLRVpocFU5YXZfTFlRTHk1eEhMQnpvVWU3enNCaFgzOUlSYWFUOXc?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPejhyNTZVazBOYWlmd0YwNlgxWXVXWFU1MFkzUFVXaGU1TWREd0dtTUFPUGlXeVZYQTVXeHlkT2xVM19IUzh3aGRnWVJGeE1QYUIyMm9oaGNsT2drWjFsVXpFTDVzQXBXV2tXWDZOcDFxVFRfOHpiTkFDeTdxdV9ialhJRUJlY1FLSTQ2dUVEaEdaUWlpbVBIc0hBeWFGOEMzRk83VVVGckJiZw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQZXVVcU1TV3VIM2pjVlZiWFZwUWw5MmprMHhZbjdIcDNaX1MyMTZQV3ZOamtiMGdzNFNHN1h1OVE3TFcxelVVa0s1a3gtODE3Q3RNZzRlVndfZG5xN0s2T3plelZraXZLUkd4RWZ6bGdLV3hUdGctYXdDRUJFcXlGV25JV3h6X2ctODVfc2xMYTZOZ21XZlIwUkZvdlNzdw?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPVElCY21walNRbE1pRW15Wkx4ZnlZelNFamRpbC04cEdlTVBzejFYdGVqU2V5THhCOUFfSjBmTUk1NGR3RWVQQm80ZGxHb3F2TzYza2swN1RrSDdybllxbE9CSHF2aWtYbnl5czZDTnhmRllQeTllMWo0MVZ3cmVEelJ5ZjJ6dWFiQi1teFJ3aVlFZHJmclpOSEJuSE12cjdLakdWeVphZXV0cWZZZHFQRnowVy1zeDdQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQU0JGbU5VQ1dmVmRnVi1URXY3VWpxT3otdU9LUzRhRm9xZUlzbGlzR3VGSFB6VDI1WHk3SlNsa2x2MjFrbVduQ2R3SVY3bVIwdUg1Z2VyQ3ZxaUVkN0dEMVlTUzhQUlV2TjVfNjVnLXE5WjNvY0FPbnA1MHNqRHNMR2UxSDhnYUM5SXZTdHZwdmhlY3lGSUgwYjZXU0dZdlI4Zmc?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNRHVISDg2OExqYWNHS25oYzdENGgtcDQzd0ltZkRJZ3B1SDZKVG51czc3dnkyb0gzSUhxTF9DSVp4blR1STl0S3ZIRG9JNjJ5ZWRUUzBkOGNCRWxJMTA0TFh0ZTltZ2paQ3VxZWIxY19jUWVWQWZTRmI1QnlPTXZzQ215YzlBckVFSF9oVzFXdzlfcmpwZVQ3azVSZFBWMTREQ0t2UQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTmpjcE5OT1pBOXJ4aGFzZkhja3VhUi1TcV9tNEI0cUd1TVVUeHF1ZzlNczhHWUplMkZqQXhHNDBELVdXTVZXU24yaHRVRTVPa0JTQW9tZnRadXN1MGNVTWhrQU5zUFcwZ2JaRVZNbFNQcHhNdkpJX0tNRTRhRzNUNUJON2pzY01DQ2ZUMVRlZkVGMmNTdmFMZFRuM1hpelpWVDRzUHdGQjBRZw?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxOdDRpdU9FbjgxbEJxbHVOSy1wTE9UazRNSG1Nc3AwaXRSTUJQR2lISUhyNzltWUZ6MWpFRXlRVWZkMk5uc2xZYnNkSXEzWUFoZUh0MEdiZTVwVVoxU190cmk5WGNUMlRyUTZxLXBIaTNDSUhybG9JRzFmcU5ibDNNenZRc1N0UUJCNmhwMXIwZFV3alpRalFpSmtjTkVfdFYtMUl5YWNFbXZUek5WMWlvZmFkb3ZyenhLMDlxSVkxck1JeDNMXzY3dE9nRWpMd2tGTEN4V0pB0gHbAUFVX3lxTFBEcm1NRjkyem5SRk52RVN6dUdBNHhDRXBXWnZNUzJJU0NadVNZWFFVR3ZMdGwyWVcwVENFd3N3RHB1bVlDV3FNMGRtT28yeUdHSjNzcC1mT0NfV3VEWFowbTE2WVpOUlFValduNnRBT0F4UFgydWNfQXpwVUVLVTZGc2Zvckh6ZDJJc1Yxeng4eUFiVkNiaHZDNlZDUzlKNWhzNmdydlpsc2JUc2lXRDM4bEFMLTNZSkJ6MWdHNHRHZllTN29rLU40T3c4bGNrekNaWG5TLUR2UEMwdw?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQZEpVWk9BRU92NkhRQTRDcUpGMldvbVEyOVQxal9NT0t5WGE4dE5ESkNUejRVbDY0QTBtZDlFMDYzSUZtX00wSDg0azYySkJ0TTFuaHp2Y2pINmxWX0x6Qjdibm1ZRUttNml1VExLR0NUeFNMaFA1blhaekpmT1VyRkI3bjY5OHk2WEI3dnp1cmRrX3BGWnd0WjRhUi1aNm0xdmJF?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPbFQ1cWh6R3FnQ3BUZWJlMHNqazZUeExEN1RkQUMzeDBPcHgyOGxfZHI2eV82RkxQcWVXV2h2MDVOcWZaeGNEOEZDN29GcmdLTDR2S1lMaHpoTDFGQ1VjYTBxS010bkZGbmV1aGxmSW5tcFEyUTFzb3FrQno2aE5WV1JDMHlaU2FndDVRNHZYYkZ1alV3eWQ4RHEyb0ZCWnEtZlJmaDl3?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxORXdWekxkMVpyM3RJa2dwOU81c2h2Qy1iQUd2QzkyVUNGMnEtZW9JNFVNZGZFMDRIOEdiNWVTZFdPbDBIdjhLMHNlVE1LbmtCNDZtODF2SEd4dTYtUGdQX05uSWhoS2NoZnVjUmQyajZfMFlBZ1BPMjhVUFlubVE5ajRVZGdqSGlkaWNucVdvd2JqV3ZUY012T0xJWQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPZXloQXFGcFY4ckZHSTF3Wk5EaFh3d04yeDRSNXVVZTRlblF2WExJclFZRTNjUFJNVTc2TXpCaDdjRk1WdnJwQW9VMGJDbTV6cEJtazFKQzJ2VGYxX1BoeGFoZ1lZVVFsaHZBWExhQXRDblBBenA4RXVUTlp2NnF0cllrdnk0Y0VfUUpiOUVOZDhHYkJxZGxSaWYyRU5zZ3VCSVE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
