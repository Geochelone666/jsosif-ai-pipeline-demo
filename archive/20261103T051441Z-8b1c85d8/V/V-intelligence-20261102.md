# V Intelligence Report

- ticker: **V**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:28:20.526318+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 11, 'ai': 9, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/V** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 425.5100 |
| Return 1D (%) | 2.8821 |
| Return 1W (%) | 5.2826 |
| Return 1M (%) | 17.9809 |
| Return YTD (%) | 22.0567 |
| Return 1Y (%) | 25.8769 |
| Annualized volatility (%) | 22.4467 |
| Beta vs SPY | 0.2583 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 1.1957 |
| Downside deviation (rf=0, %) | 13.7807 |
| Sortino (rf=0) | 1.9476 |
| Historical VaR 95% (1D, %) | 1.7967 |
| Historical ES 95% (1D, %) | 2.6824 |
| Correlation vs SPY | 0.1475 |
| Tracking error vs SPY (%) | 24.1521 |
| P/E (trailing) | 34.54 |
| P/B | 21.84 |
| EV/EBITDA | 24.32 |
| Revenue growth (%) | 13.20 |
| Forward P/E (estimate) | 24.84 |
| Gross margin (%) | 97.68 |
| Operating margin (%) | 63.73 |
| Return on equity (%) | 63.51 |
| Free cash flow yield (%) | 2.66 |
| MA50 | 382.4004 |
| Close vs MA50 (%) | 11.2734 |
| MA200 | 341.9534 |
| Close vs MA200 (%) | 24.4351 |
| RSI (14, Wilder) | 75.0998 |
| MACD (12,26) | 10.7144 |
| MACD signal (9) | 9.4444 |
| MACD histogram | 1.2700 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 425.5100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.8821 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.2826 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 17.9809 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 22.0567 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 25.8769 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.4467 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.7807 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.9476 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7967 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6824 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1475 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.1521 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2583 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.1805 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1957 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.8405 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.6780 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 63.7280 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 63.5070 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.6555 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 34.5382 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 75.0998 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.2700 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 11.2734 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 24.4351 -> Clearly above the moving-average trend level.

## TAILWINDS

### Visa (V) Upgraded to Buy: Here's What You Should Know
- Summary: Visa (V) Upgraded to Buy: Here's What You Should Know
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPSnRvc3BiVWJzdF9ZWUsxa0p6eU1maWFQck5iQVVaTW5SZ1lOcXFmZjhUZi1LM01YX25LM1M1dVREYnM4T1VjMjFQVUR0bC1JUWw3WWNEVmNaOEVFbkFPT00wR0N2dUpSLUJMekVHNTl2amdhejF4QXNsN093U2lmcGx5S3Y5dlhpakxpWEllN1d3S3cw?oc=5>

### Visa (NYSE:V) Stock Price Up 2.9% - What's Next?
- Summary: Visa (NYSE:V) Stock Price Up 2.9% - What's Next?
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQWVNBeVJfdFhEYkZDb0lHRHBYN0NqaFNZYmFnbUw4aUxMMkRXcWpSeTFidDBUbWZVeDYzWGtRU2RFRjIxamhyTVlyRG5tajBtNDZfMW00TjFHTGRrLUlwaWNjVmlyRl9PT2NkRjJkQmd3TUY1SkJNdjRKeU81NWJCWTdsWXJrNWstTFlUOWVLRllJTl9hOXBGb0ZmT2hQZnQ4MWc?oc=5>

### Visa, IBD Stock Of The Day, Shows Bullish Action After Earnings Report
- Summary: Visa, IBD Stock Of The Day, Shows Bullish Action After Earnings Report
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxOb0dyMXRNWWZvcXlhQXNPVEJsUjAzaWRzV3Y1NGhicm9mU3JGNmx2NnM1M0tnWTNreTlDU2ROYlJtcG5QYUhxbXJLbmg2VjFKamFpVG9ReGwtVDdsaW9GUHVaZ0tLY3FkeUhYZjlxZUdValVxYlpqS1Q3UWhEMFBHUFJR?oc=5>

### Visa’s Record Year Pushes Shares Higher
- Summary: Visa’s Record Year Pushes Shares Higher
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOay1tSlFVd3FsMlVIV0prNl9Bemo3MTRaUnBOR0cwdDhnOWp6N3VnOUJkUmFQMVFoc1pDUjlpdmc5LWJpazdSUXFzajNtLVRGMUJMTnFqTmgwZ040cHVSd3pvcGJTcmQ5Mjh2Y2wxMTZDbjNKWktmZzRqYmlkOWNUYjNBYlhQRlZVVTdHLTJOWFJ2U0k?oc=5>

### Visa (NYSE:V) Stock Jumps 2.4% Following Analyst Upgrade
- Summary: Visa (NYSE:V) Stock Jumps 2.4% Following Analyst Upgrade
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQWWcwUmVJT0JLazdPdUNSYXBCSjBEV3ZqNVlKdHFYbnhyWDVIbk52NGlqVFhEck1Ba1E3NlN5dG56WGtQaDlMQkRydkFTZUM2YUw1bTIwdUswc2ZYX1Vma2xQcjJ5VGdzeVNKYm5UckMtLUp0STRSZ0JhTHR6ajM0VVlkb0xNaW5QbVE1X1NWWWtydDZLSFJJU1JBUGE1TldZTm9tcnY0VkN4RVRDS1ZmNTJn?oc=5>

### Mastercard Rises 4% on Revenue and EPS Beat Led by Value-Added Services; Visa and American Express Gain 2%, PayPal Ticks Up
- Summary: Visa shares rose 2% following market movement.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi9gFBVV95cUxORkVDSGtsVU44bXRQUUVQV2I3WElJak5uWFJELXhITmIzS2VUTE80UjBXdDNLMUlkV0hRa0QyNUswamh4YWZOb3VtdU1kSEFaQ0RlNUlEcWtiRW1PaDhJNzllMW9xYkRZSlQxaUxzS01yazFPOVdMZWpjYnFKMk03UndiOG1MdWdtMmdSZmxFUTJTOEtveDZWd0R4MDczRjNIZXh4eU1TVlJxSU1BamxQd1ptTjJ6bzQ1VDJ4SjRIWkZrT3lOclpBdTlVTkFhSUU1S29wejZ1VEgxeFRodXRyd2dKVGpNUGJkMkFlN212N2hSUWgtdmc?oc=5>

### Visa (V) Stock Could Be A Bargain On Record Revenue Growth
- Summary: Visa’s record revenue growth suggests a potential bargain for investors.
- Date: 2026-10-29 | Impact: high | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQeWc0ZUwxcXpTaVdIQ1NCenRubXBzNDBHclFqYkxqWDgzemxKemlITnh5MXNDYjVkYmVIMmpNazZPZXVVQWpUQndFd2Y5eEVBc1Y3R0xvNWdtbXBOYXVkMENxbEhBQ19sajJEZEF4T1RPTWhySjdwMjlMUnQxM1Vkc1BJZ0JPQV9zZ2lFQnFjQWYtZXhPdks2WXlkVlJWOGRUbTRGNFhRM1FtMklZdXBNN3RaejNMVlRqYVdMaGxNc01wMXQxN09F0gHMAUFVX3lxTE5tNU1qLUgtNUZMeXFxV09hLUtJaExqVmswcUN6OXIybzdzQ1RBM0ZXOEx0TkxuVGZoNVdRMzh4MWx3M3pDemVkX0dKZFB0akg2T1BwbHlNUzRuQ0tlbjljNzU1VkxHUjRYQklOVmd1Z0xiTU5WNjExWTF6VXBRbmwteWFxVlZvTXFhOWVpNUVkSm56ZzdQbW1SbG4zaHluSEttT3F2dWlPTHRRMVFuRThEcVlmMjBBUEhlWTUweVZqelh5QWR3cDZUOVU1Sw?oc=5>

### Visa Inc Stock (V) Moved Up by 3.14% on Nov 2: What Investors Need To Know
- Summary: Shares rose 3.14% on Nov 2, indicating positive market sentiment.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxQbHJiazdqS3VVeVJpS2Rob2dNRUV2c3Y3WS0tSExLZzFkSVBmbWw3ZERwT05GLVRCcjctMnh6WWxlV2pWNzJldlJjUUVoa1dtMHJoS0RFTkhrNUJSVmR3M1diVkhkR2pTNEg0eTdtakRwSC1pOUw3bzRYRkw5MVQ5RElxQ2JKZjQ?oc=5>

## HEADWINDS

### Visa Stock Inches Lower Despite Revenue Beat
- Summary: Visa Stock Inches Lower Despite Revenue Beat
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOQ0JtM0JOc2NMd2VBVV9JUTJLaDhRVVgwZ2h4d1JXQ3ZrYUFKMEVsamN3Wmk5WlNEamZTWkFtZ1NJQWtLTkdkeUJNVGY4aWdaT0ZWdHF3ZkU2U2VzdWtQd1Uzb1pselhZRGc3eEl5ZzN5WGtYY1hxUUlnV1FLRGdhYm4wTkt6MjhDdmhWOEJTYjhFT2NaY1NUdUQwdjA?oc=5>

### Visa Inc. (V) Stock Falls on Q4 2026 Earnings
- Summary: Visa Inc. (V) Stock Falls on Q4 2026 Earnings
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPM3pjdm8wb1FCMzlDT0VLdHpBZklsNUItVWxjbl9XU3dxbnhxNFBNeGVmUEotc01pb0J6dHpvZ05TM1VrXzlENWh2SG9qR0U0cTA3Rjk4SGxUTG0yQnU0aTJ2RGJqWC1ZWEM3a1Voa3cwcC1xNmE4eExOZEgzM1l4MWZKSXpXN3MxWnc?oc=5>

### Analysts Have Conflicting Sentiments on These Financial Companies: Visa (V), PayPal Holdings (PYPL) and TransUnion (TRU)
- Summary: Analysts hold mixed sentiments on Visa, PayPal, and TransUnion, signaling market uncertainty.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwJBVV95cUxOYnBoZ19YTzBGZVR4YzFMOXNPbVZpc3FPUlV1MG92TlNtSWx3UFBPX0pPMVo1dWZQeWFfZEZfOGE0R3BwTGs2NTRZaUhaTjkzd2dBWXdKY0V3QTM5eFJxU2EzSmZ5Q3EwbkZJaUhsUngtV1RlNjhfdVJpTTdzeUFqSFdzRG9SYmhJTmJ2T2IxZ2p3RXVmT2JSSkZKUUlnbm15eWltQVVnd0dYZ3BRZ1NSSlY4MFZyX0NCYmtTbHQxdVJyaWZCOENCVVg4RHBDVEdMVDc5WUtvUlJHTzFWM3RmUkd0aU9IcmFzSHZnZHJwZTZWdDNKcDc1b2VLMS10M2YzWkJtOThpa2VSek84Ulo2OXZlejlJM2hsckg2ckdPcw?oc=5>

## CATALYSTS

### Visa (V) Stock Fair Value Edges Higher After Analysts Lift Targets On Q4 Results
- Summary: Visa (V) Stock Fair Value Edges Higher After Analysts Lift Targets On Q4 Results
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPSUM0T3phd1lPUkhkRlpMdUdNVWZRYnlHNk5sLXhwSjBxd3J0OXVMb1lMaGxsMGRWMmptQVNjT3dYcUVNazZiRzBNX3dpOE0yYS1Nd2tHeXJENlQwcFV5MFlqZ3ZZNFJjWFI4RlhwN3FKbmhTcVJhWkV3dW1oTkgybExxeDBtc1plbVFXdG82V0RBQQ?oc=5>

### Visa Inc. $V Stock Purchased by Vise Technologies Inc.
- Summary: Visa Inc. $V Stock Purchased by Vise Technologies Inc.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOSzBMWnlUbm5zX0c1U3pNZ2FXc3pVWFdqNGRWeUZIc3dzRE9hUHZTbjF5WUtyakNia3YwWjExNWFaR1lSdHdrN3NERkZKa092XzYwN2UtUFFrbVRJRHE2a0lJM3FyQWFNdTdJc1J4V0p0S2hJOGpxQndFeWNZOVhndlBKNFM0a3Z3X3FnbzhMQ1dMZFRPS0xsbE1QVjhBY3dCSE1DMlBrSy1qaDVid1NQZkd3?oc=5>

### Visa (NYSE:V) Stock Sold by Rep. Pete Sessions
- Summary: Visa (NYSE:V) Stock Sold by Rep. Pete Sessions
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxObWlNa2NOOFNwWnpZeWE0dzZYS1BfZEdsVm5veExyUXBYREFtWDJDdGlFWWdfSldnV0llekpjT1cyd3Z1Z1hnSjJiVTNLdGwzdkRBMnh4QTNwTnNQRUFyYWlJcFdhdmhJeDlXTG4zazFMSzlMWGhySktPVTF5djBHWUIxZl94SURVMmpBeFB2Q1NjUjZtemZjT1hodXNjLTRXRXpVWUVDVU5pUQ?oc=5>

### VISA ($V) Releases Q4 2026 Earnings
- Summary: VISA ($V) Releases Q4 2026 Earnings
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE9kRWVJZnRyc2hQM3U1LXIxaGhzcFFJQzdlcEdiYlZkQlhvQkxtM2VvYUZIM3M1T1JQbFR6X19uZFhVeXhMaVdVYjR1UUZTeDE4VTVlVUJjaGw0U2w4b3dsS2NWbndpWG1DeFdUcTdaTEtaYzlQR1pLLUdaS29NSEU?oc=5>

### Wells Fargo & Company Issues Positive Forecast for Visa (NYSE:V) Stock Price
- Summary: Wells Fargo forecasts a positive outlook for Visa stock, suggesting potential upside.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxQMkhmSjlNOWhfeFE0RGFWTWRmRUc2ZzZJMmp1akNHZmxCaDZ5R19meFBJdHI4SjBjT3Etdk5NZUF5NXlhblAwZm1oQ2kwdklCZ0Z0dlJQeE03YjJGaWxIcjR0ems3MVRmTEVFVnR0U1V3S05iMWhGbnllVi1MQmRQcnhaSUptVjJvTk1kS1Z3NmNtZlZLckZjRDhTN2VfVXhGV2g2MjNnUW15MDRVOVhlOVpJRkg4TXlfenFpWkpqRnAtbmdwSzZJZ1JXU2RCVWc?oc=5>

### Visa raises dividend by 16%: Can V stock continue its gains?
- Summary: Visa announced a 16% dividend increase, potentially boosting investor confidence and supporting stock performance.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxNdUZJWVpmVWxsQ2g3enhpYUk1eGs3a2hkaXVTX21PQWtCZF9LcjB5LUJSZkNzblp5VnBWNE5FMzY4NGRzSld3UVAyUXYwM1BnMFBFcUxEX0VUMDQ0bXlDZlhyRFNXOVBoLWZrNGhBUUF6X0laakt5ME0xelhmUXlWSDNRUUd1bDdQeU9KenFR?oc=5>

### Why Are Credit Card Stocks Mastercard (MA), Visa (V), and American Express (AXP) Up Today?
- Summary: Market rally lifts credit card stocks, reflecting positive sentiment toward the sector.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQVVcydnJkbElzVTlxcmVTeGJ6R3dWOXdPVVpmcTRCNWQycmN0NTFnMm5LajVBQ05CQjhISkZ4RzlUS3BqOHV3SXhna3RqZ1A3Y0U3S0NqZ3g1UlpkaUpIdzJreDU5eWtYbFFHaEltbUZ6dWdGZ29tV3lKWE15OWNaNDhPRDdWY285ZXlUeVBycE1LRC1WcF9pOXFEQUZUd3B3WlZ3WU5TRTlMeGpVV1llWA?oc=5>

### Visa (V) director Lloyd Carney sells 605 shares at an average $415.28 each.
- Summary: Director Lloyd Carney sold 605 Visa shares at $415.28 each, indicating a personal divestment.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOWVY5SGp2MHF3U0tQT2xIR1YwcTlWaTFmX2tNUkpFYUVlZTJHdEhraE5hLTB0TjhOaV9nT21mVy1BSFFHdnJObVBpNnJ3UkxwVy1LZ3RtakhuS05uOTlScUN0VFliUVNBOVZYbTNxUjNrTDVLTUlvbFhhUkdCQm5oNWNwYVlaVFZ1b2pNMGIzUXNCTGFoanpHdjRsXzlkU3Ry?oc=5>

### Visa (V) officer plans to sell 5,875 shares through an employee stock option exercise.
- Summary: An officer intends to sell 5,875 shares via an option exercise, reflecting a planned divestiture.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOR1ZuRmJ6dkRnU25GeVJWdzluZ3doUGpXY0xFRFBncmd3ZDVmODh4cDNjZnZkZGk4eFk4MDZ0eEdLUXZ1QnBsMzEwTWNQWXBwNDNYSjh3V3NRQkhsMkl6OHpEbjNaU1l4T3VOOHI4ZXBNVk5LYW9LWk1pTTFneHRwbXB1Yy1wdjc2R0E?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **V** | **34.54** | **21.84** | **24.32** | **13.20** | **795,280,736,256.00 USD** | **25.88** |
| MA | 33.39 | 84.99 | 25.48 | 14.00 | 573,320,986,624.00 USD | 19.99 |
| PYPL | 10.89 | 2.53 | 8.10 | 2.00 | 48,826,093,568.00 USD | -14.20 |
| AXP | 18.48 | 6.15 | N/A | 11.30 | 219,927,658,496.00 USD | -8.06 |

Peers fetched as_of: 2026-11-02; V reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-29
- Revenue (latest available single quarter): 5,840,000,000.00 USD; period 2019-04-01/2019-06-30; fiscal year/reporting period 2019/Q3
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/1403161/000140316126000104/v-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilAFBVV95cUxPSnRvc3BiVWJzdF9ZWUsxa0p6eU1maWFQck5iQVVaTW5SZ1lOcXFmZjhUZi1LM01YX25LM1M1dVREYnM4T1VjMjFQVUR0bC1JUWw3WWNEVmNaOEVFbkFPT00wR0N2dUpSLUJMekVHNTl2amdhejF4QXNsN093U2lmcGx5S3Y5dlhpakxpWEllN1d3S3cw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQWVNBeVJfdFhEYkZDb0lHRHBYN0NqaFNZYmFnbUw4aUxMMkRXcWpSeTFidDBUbWZVeDYzWGtRU2RFRjIxamhyTVlyRG5tajBtNDZfMW00TjFHTGRrLUlwaWNjVmlyRl9PT2NkRjJkQmd3TUY1SkJNdjRKeU81NWJCWTdsWXJrNWstTFlUOWVLRllJTl9hOXBGb0ZmT2hQZnQ4MWc?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxOb0dyMXRNWWZvcXlhQXNPVEJsUjAzaWRzV3Y1NGhicm9mU3JGNmx2NnM1M0tnWTNreTlDU2ROYlJtcG5QYUhxbXJLbmg2VjFKamFpVG9ReGwtVDdsaW9GUHVaZ0tLY3FkeUhYZjlxZUdValVxYlpqS1Q3UWhEMFBHUFJR?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOay1tSlFVd3FsMlVIV0prNl9Bemo3MTRaUnBOR0cwdDhnOWp6N3VnOUJkUmFQMVFoc1pDUjlpdmc5LWJpazdSUXFzajNtLVRGMUJMTnFqTmgwZ040cHVSd3pvcGJTcmQ5Mjh2Y2wxMTZDbjNKWktmZzRqYmlkOWNUYjNBYlhQRlZVVTdHLTJOWFJ2U0k?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQWWcwUmVJT0JLazdPdUNSYXBCSjBEV3ZqNVlKdHFYbnhyWDVIbk52NGlqVFhEck1Ba1E3NlN5dG56WGtQaDlMQkRydkFTZUM2YUw1bTIwdUswc2ZYX1Vma2xQcjJ5VGdzeVNKYm5UckMtLUp0STRSZ0JhTHR6ajM0VVlkb0xNaW5QbVE1X1NWWWtydDZLSFJJU1JBUGE1TldZTm9tcnY0VkN4RVRDS1ZmNTJn?oc=5
- https://news.google.com/rss/articles/CBMi9gFBVV95cUxORkVDSGtsVU44bXRQUUVQV2I3WElJak5uWFJELXhITmIzS2VUTE80UjBXdDNLMUlkV0hRa0QyNUswamh4YWZOb3VtdU1kSEFaQ0RlNUlEcWtiRW1PaDhJNzllMW9xYkRZSlQxaUxzS01yazFPOVdMZWpjYnFKMk03UndiOG1MdWdtMmdSZmxFUTJTOEtveDZWd0R4MDczRjNIZXh4eU1TVlJxSU1BamxQd1ptTjJ6bzQ1VDJ4SjRIWkZrT3lOclpBdTlVTkFhSUU1S29wejZ1VEgxeFRodXRyd2dKVGpNUGJkMkFlN212N2hSUWgtdmc?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQeWc0ZUwxcXpTaVdIQ1NCenRubXBzNDBHclFqYkxqWDgzemxKemlITnh5MXNDYjVkYmVIMmpNazZPZXVVQWpUQndFd2Y5eEVBc1Y3R0xvNWdtbXBOYXVkMENxbEhBQ19sajJEZEF4T1RPTWhySjdwMjlMUnQxM1Vkc1BJZ0JPQV9zZ2lFQnFjQWYtZXhPdks2WXlkVlJWOGRUbTRGNFhRM1FtMklZdXBNN3RaejNMVlRqYVdMaGxNc01wMXQxN09F0gHMAUFVX3lxTE5tNU1qLUgtNUZMeXFxV09hLUtJaExqVmswcUN6OXIybzdzQ1RBM0ZXOEx0TkxuVGZoNVdRMzh4MWx3M3pDemVkX0dKZFB0akg2T1BwbHlNUzRuQ0tlbjljNzU1VkxHUjRYQklOVmd1Z0xiTU5WNjExWTF6VXBRbmwteWFxVlZvTXFhOWVpNUVkSm56ZzdQbW1SbG4zaHluSEttT3F2dWlPTHRRMVFuRThEcVlmMjBBUEhlWTUweVZqelh5QWR3cDZUOVU1Sw?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxQbHJiazdqS3VVeVJpS2Rob2dNRUV2c3Y3WS0tSExLZzFkSVBmbWw3ZERwT05GLVRCcjctMnh6WWxlV2pWNzJldlJjUUVoa1dtMHJoS0RFTkhrNUJSVmR3M1diVkhkR2pTNEg0eTdtakRwSC1pOUw3bzRYRkw5MVQ5RElxQ2JKZjQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOQ0JtM0JOc2NMd2VBVV9JUTJLaDhRVVgwZ2h4d1JXQ3ZrYUFKMEVsamN3Wmk5WlNEamZTWkFtZ1NJQWtLTkdkeUJNVGY4aWdaT0ZWdHF3ZkU2U2VzdWtQd1Uzb1pselhZRGc3eEl5ZzN5WGtYY1hxUUlnV1FLRGdhYm4wTkt6MjhDdmhWOEJTYjhFT2NaY1NUdUQwdjA?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPM3pjdm8wb1FCMzlDT0VLdHpBZklsNUItVWxjbl9XU3dxbnhxNFBNeGVmUEotc01pb0J6dHpvZ05TM1VrXzlENWh2SG9qR0U0cTA3Rjk4SGxUTG0yQnU0aTJ2RGJqWC1ZWEM3a1Voa3cwcC1xNmE4eExOZEgzM1l4MWZKSXpXN3MxWnc?oc=5
- https://news.google.com/rss/articles/CBMinwJBVV95cUxOYnBoZ19YTzBGZVR4YzFMOXNPbVZpc3FPUlV1MG92TlNtSWx3UFBPX0pPMVo1dWZQeWFfZEZfOGE0R3BwTGs2NTRZaUhaTjkzd2dBWXdKY0V3QTM5eFJxU2EzSmZ5Q3EwbkZJaUhsUngtV1RlNjhfdVJpTTdzeUFqSFdzRG9SYmhJTmJ2T2IxZ2p3RXVmT2JSSkZKUUlnbm15eWltQVVnd0dYZ3BRZ1NSSlY4MFZyX0NCYmtTbHQxdVJyaWZCOENCVVg4RHBDVEdMVDc5WUtvUlJHTzFWM3RmUkd0aU9IcmFzSHZnZHJwZTZWdDNKcDc1b2VLMS10M2YzWkJtOThpa2VSek84Ulo2OXZlejlJM2hsckg2ckdPcw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPSUM0T3phd1lPUkhkRlpMdUdNVWZRYnlHNk5sLXhwSjBxd3J0OXVMb1lMaGxsMGRWMmptQVNjT3dYcUVNazZiRzBNX3dpOE0yYS1Nd2tHeXJENlQwcFV5MFlqZ3ZZNFJjWFI4RlhwN3FKbmhTcVJhWkV3dW1oTkgybExxeDBtc1plbVFXdG82V0RBQQ?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxOSzBMWnlUbm5zX0c1U3pNZ2FXc3pVWFdqNGRWeUZIc3dzRE9hUHZTbjF5WUtyakNia3YwWjExNWFaR1lSdHdrN3NERkZKa092XzYwN2UtUFFrbVRJRHE2a0lJM3FyQWFNdTdJc1J4V0p0S2hJOGpxQndFeWNZOVhndlBKNFM0a3Z3X3FnbzhMQ1dMZFRPS0xsbE1QVjhBY3dCSE1DMlBrSy1qaDVid1NQZkd3?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxObWlNa2NOOFNwWnpZeWE0dzZYS1BfZEdsVm5veExyUXBYREFtWDJDdGlFWWdfSldnV0llekpjT1cyd3Z1Z1hnSjJiVTNLdGwzdkRBMnh4QTNwTnNQRUFyYWlJcFdhdmhJeDlXTG4zazFMSzlMWGhySktPVTF5djBHWUIxZl94SURVMmpBeFB2Q1NjUjZtemZjT1hodXNjLTRXRXpVWUVDVU5pUQ?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE9kRWVJZnRyc2hQM3U1LXIxaGhzcFFJQzdlcEdiYlZkQlhvQkxtM2VvYUZIM3M1T1JQbFR6X19uZFhVeXhMaVdVYjR1UUZTeDE4VTVlVUJjaGw0U2w4b3dsS2NWbndpWG1DeFdUcTdaTEtaYzlQR1pLLUdaS29NSEU?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxQMkhmSjlNOWhfeFE0RGFWTWRmRUc2ZzZJMmp1akNHZmxCaDZ5R19meFBJdHI4SjBjT3Etdk5NZUF5NXlhblAwZm1oQ2kwdklCZ0Z0dlJQeE03YjJGaWxIcjR0ems3MVRmTEVFVnR0U1V3S05iMWhGbnllVi1MQmRQcnhaSUptVjJvTk1kS1Z3NmNtZlZLckZjRDhTN2VfVXhGV2g2MjNnUW15MDRVOVhlOVpJRkg4TXlfenFpWkpqRnAtbmdwSzZJZ1JXU2RCVWc?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxNdUZJWVpmVWxsQ2g3enhpYUk1eGs3a2hkaXVTX21PQWtCZF9LcjB5LUJSZkNzblp5VnBWNE5FMzY4NGRzSld3UVAyUXYwM1BnMFBFcUxEX0VUMDQ0bXlDZlhyRFNXOVBoLWZrNGhBUUF6X0laakt5ME0xelhmUXlWSDNRUUd1bDdQeU9KenFR?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQVVcydnJkbElzVTlxcmVTeGJ6R3dWOXdPVVpmcTRCNWQycmN0NTFnMm5LajVBQ05CQjhISkZ4RzlUS3BqOHV3SXhna3RqZ1A3Y0U3S0NqZ3g1UlpkaUpIdzJreDU5eWtYbFFHaEltbUZ6dWdGZ29tV3lKWE15OWNaNDhPRDdWY285ZXlUeVBycE1LRC1WcF9pOXFEQUZUd3B3WlZ3WU5TRTlMeGpVV1llWA?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOWVY5SGp2MHF3U0tQT2xIR1YwcTlWaTFmX2tNUkpFYUVlZTJHdEhraE5hLTB0TjhOaV9nT21mVy1BSFFHdnJObVBpNnJ3UkxwVy1LZ3RtakhuS05uOTlScUN0VFliUVNBOVZYbTNxUjNrTDVLTUlvbFhhUkdCQm5oNWNwYVlaVFZ1b2pNMGIzUXNCTGFoanpHdjRsXzlkU3Ry?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOR1ZuRmJ6dkRnU25GeVJWdzluZ3doUGpXY0xFRFBncmd3ZDVmODh4cDNjZnZkZGk4eFk4MDZ0eEdLUXZ1QnBsMzEwTWNQWXBwNDNYSjh3V3NRQkhsMkl6OHpEbjNaU1l4T3VOOHI4ZXBNVk5LYW9LWk1pTTFneHRwbXB1Yy1wdjc2R0E?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
