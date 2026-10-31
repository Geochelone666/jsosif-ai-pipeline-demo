# V Intelligence Report

- ticker: **V**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:05:44.068691+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 7, 'ai': 7, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/V** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 11 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-10-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 413.5900 |
| Return 1D (%) | 0.7429 |
| Return 1W (%) | 1.3900 |
| Return 1M (%) | 15.1003 |
| Return YTD (%) | 18.6375 |
| Return 1Y (%) | 20.8294 |
| Annualized volatility (%) | 22.3009 |
| Beta vs SPY | 0.2643 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 0.9623 |
| Downside deviation (rf=0, %) | 13.8557 |
| Sortino (rf=0) | 1.5488 |
| Historical VaR 95% (1D, %) | 1.7961 |
| Historical ES 95% (1D, %) | 2.6824 |
| Correlation vs SPY | 0.1516 |
| Tracking error vs SPY (%) | 23.9676 |
| P/E (trailing) | 33.57 |
| P/B | 21.23 |
| EV/EBITDA | 23.65 |
| Revenue growth (%) | 13.20 |
| Forward P/E (estimate) | 24.14 |
| Gross margin (%) | 97.68 |
| Operating margin (%) | 63.73 |
| Return on equity (%) | 63.51 |
| Free cash flow yield (%) | 2.73 |
| MA50 | 381.3110 |
| Close vs MA50 (%) | 8.4653 |
| MA200 | 341.4549 |
| Close vs MA200 (%) | 21.1258 |
| RSI (14, Wilder) | 69.4412 |
| MACD (12,26) | 9.6677 |
| MACD signal (9) | 9.1270 |
| MACD histogram | 0.5407 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 413.5900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.7429 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.3900 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 15.1003 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 18.6375 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 20.8294 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.3009 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.8557 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.5488 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7961 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6824 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1516 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.9676 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2643 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.1805 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9623 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.1404 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.6780 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 63.7280 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 63.5070 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.7320 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 33.5706 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 69.4412 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.5407 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 8.4653 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 21.1258 -> Clearly above the moving-average trend level.

## TAILWINDS

### Visa’s Record Year Pushes Shares Higher
- Summary: Visa’s Record Year Pushes Shares Higher
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNOVdnMkQ3UTRZTjJXN2lxcGRIM0pBaUZYNS1JQm1UNmdXc0tORnJmTXl4ZEFVR1Q2LW5QQ2M5Y0lkektFZElVSjN6OVgzblZtSllkcEpFV2NHVlMwOWNub2JJY0J2aHpNcVozeEJnY2lERjJpcmV3eS02RnBuQVdvWDhCTm5UeFF1UGJmRzIySUljeWpJaE01d2JmS3hndw?oc=5>

### Visa, IBD Stock Of The Day, Shows Bullish Action After Earnings Report
- Summary: Visa, IBD Stock Of The Day, Shows Bullish Action After Earnings Report
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxOb0dyMXRNWWZvcXlhQXNPVEJsUjAzaWRzV3Y1NGhicm9mU3JGNmx2NnM1M0tnWTNreTlDU2ROYlJtcG5QYUhxbXJLbmg2VjFKamFpVG9ReGwtVDdsaW9GUHVaZ0tLY3FkeUhYZjlxZUdValVxYlpqS1Q3UWhEMFBHUFJR?oc=5>

### Visa Stock Outlook: 3 Key Things Investors Must Watch Before Q4 Earnings
- Summary: Key factors to monitor Visa before Q4 earnings release.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPN2ZWZlF0WjN5cWFYT3RvVV9zXzFibk5JRWl4MjU3ZWN5cUpCdkEyTnlWWDh1SGpBbkxnblZlVFNSVHREVDdiZ0h1Qk8zMlFiUWJWbHJHa09CTEF0UDBrX2hSeWo5eE5zWm1Fci1TYUgyOHZiVUVReDVwdEk2NGt6aWlKdTZQMTNPN1BUUGp6OG9JakZidHROLW9vWFFITnBudGJBVXJaOXo4elNjUWF2TGVEVlljd3dabkdQcXhfOUxSUl9kaUhIRHdB?oc=5>

### Visa (V) Stock Could Be Near Fair Value Despite Its 105% Run
- Summary: Visa’s stock may be fairly valued after a 105% run, suggesting a positive valuation outlook.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOUDhOakEyejNzU1M3RXZ3bGdRcGtuckFrTTFmcGk0WGoyb0VxNFpNS1VObGVfQmVPdFVKWC0tcjc0Rk83Z1JNX3lVNnE5R0Q3bDRNdGpFdk9GNHVlbjdWLWtoU2huTGxrNnlhZnFMQ0xaa2owRU9EYlNPbXExclIwbTYxMkFhRWs1cnNNbUgwRW1NUQ?oc=5>

### Analysts Have Conflicting Sentiments on These Financial Companies: Visa (V), PayPal Holdings (PYPL) and TransUnion (TRU)
- Summary: Analysts are divided on Visa’s prospects, reflecting uncertainty in the sector.
- Date: 2026-10-29 | Impact: medium | Horizon: medium | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMinwJBVV95cUxOYnBoZ19YTzBGZVR4YzFMOXNPbVZpc3FPUlV1MG92TlNtSWx3UFBPX0pPMVo1dWZQeWFfZEZfOGE0R3BwTGs2NTRZaUhaTjkzd2dBWXdKY0V3QTM5eFJxU2EzSmZ5Q3EwbkZJaUhsUngtV1RlNjhfdVJpTTdzeUFqSFdzRG9SYmhJTmJ2T2IxZ2p3RXVmT2JSSkZKUUlnbm15eWltQVVnd0dYZ3BRZ1NSSlY4MFZyX0NCYmtTbHQxdVJyaWZCOENCVVg4RHBDVEdMVDc5WUtvUlJHTzFWM3RmUkd0aU9IcmFzSHZnZHJwZTZWdDNKcDc1b2VLMS10M2YzWkJtOThpa2VSek84Ulo2OXZlejlJM2hsckg2ckdPcw?oc=5>

### Visa (V) Stock Could Be A Bargain On Record Revenue Growth
- Summary: Visa’s record revenue growth suggests a potential bargain for investors.
- Date: 2026-10-29 | Impact: high | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQeWc0ZUwxcXpTaVdIQ1NCenRubXBzNDBHclFqYkxqWDgzemxKemlITnh5MXNDYjVkYmVIMmpNazZPZXVVQWpUQndFd2Y5eEVBc1Y3R0xvNWdtbXBOYXVkMENxbEhBQ19sajJEZEF4T1RPTWhySjdwMjlMUnQxM1Vkc1BJZ0JPQV9zZ2lFQnFjQWYtZXhPdks2WXlkVlJWOGRUbTRGNFhRM1FtMklZdXBNN3RaejNMVlRqYVdMaGxNc01wMXQxN09F0gHMAUFVX3lxTE5tNU1qLUgtNUZMeXFxV09hLUtJaExqVmswcUN6OXIybzdzQ1RBM0ZXOEx0TkxuVGZoNVdRMzh4MWx3M3pDemVkX0dKZFB0akg2T1BwbHlNUzRuQ0tlbjljNzU1VkxHUjRYQklOVmd1Z0xiTU5WNjExWTF6VXBRbmwteWFxVlZvTXFhOWVpNUVkSm56ZzdQbW1SbG4zaHluSEttT3F2dWlPTHRRMVFuRThEcVlmMjBBUEhlWTUweVZqelh5QWR3cDZUOVU1Sw?oc=5>

## HEADWINDS

### Visa Stock Inches Lower Despite Revenue Beat
- Summary: Visa Stock Inches Lower Despite Revenue Beat
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOQ0JtM0JOc2NMd2VBVV9JUTJLaDhRVVgwZ2h4d1JXQ3ZrYUFKMEVsamN3Wmk5WlNEamZTWkFtZ1NJQWtLTkdkeUJNVGY4aWdaT0ZWdHF3ZkU2U2VzdWtQd1Uzb1pselhZRGc3eEl5ZzN5WGtYY1hxUUlnV1FLRGdhYm4wTkt6MjhDdmhWOEJTYjhFT2NaY1NUdUQwdjA?oc=5>

### Visa Q4 earnings beat, revenue in line as payments volume growth ticks slightly lower (V:NYSE)
- Summary: Visa Q4 earnings beat, revenue in line as payments volume growth ticks slightly lower (V:NYSE)
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPeUZJR2FrYThtRXdfYnhJUjdwRGxSTnFvTV9WbC1VTnpZTXZzNzhNVTlFZUNrSFpSekE5QVZsdEI4c1BhVU5SQk1wbHBMQ0dDYVpRdUFYMngzY2JPdnVUSEhPeG9Jb3FNRm83cWdqeWhnLWtMMjRSQk1PTHFxNEJDYmJORldjRnBoajdEZ05aX2gxTGxLUzRGQUJ1czA2d25FSkFuYmoxLWJLNWJ0ZnVBT1FpOEV5ZHBVUHp1cWpWMA?oc=5>

## CATALYSTS

### Visa Just Hiked Its Dividend 16.4%. The Small Yield Is Hiding a Compounding Machine
- Summary: Visa Just Hiked Its Dividend 16.4%. The Small Yield Is Hiding a Compounding Machine
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOam82YTZSWlVDQmdiM3dYbzhNWVctVmpCTGlXZENFMnpUS0xoN3pBR2I5NlpjLUVaMWdGbWJpb3Bvbk54dkJ1dHpKM2JkOUxkQUtBLXJfUU8wbGtNZEJoTWFUM0lweGZoX0NBWkswem44ZFk1WlhaMmhqeTJPM0hxMGJCMzRiVGFzc0ZGQmw1QlpfanJtdnNN?oc=5>

### Visa (V) Q3 earnings: what to expect
- Summary: Visa (V) Q3 earnings: what to expect
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPSXlJZkxLSEdaS2dtZXJyNkpfWDdnZHpKYzlUUGlka05SWXROTi1GMEFJYjloQTVrZ3NNc18yOEtqdndoeURRckREazhsLVlOVDNya3JtTFZVbFhPZklsZGFhMDM3cnRTam40VElqdVJuNUFRUDFhazJCMm1BWjNmNXI0R3Z3VWFYWDFrTUlwRHhjd3FG?oc=5>

### Visa posts record revenue and boosts shareholder returns
- Summary: Visa posts record revenue and boosts shareholder returns
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxNRjB4TnVIcVRCcy1FMEhWeWlMS3pUX09QTUo1dDFYNTJLRDR5U2lWc2hRdWpJbDFxdDVUNnVVN0ZOTDNtUWNNQ0NsSlRSNVBCTzJxUXlVUkYzWXM4Z3NUZEVQTFBzVmhwYXc0TzFjSWFGdWZpT2NYTWpJVHdtSE1PTHVDVUNqbjUtYUhqY2MzeVpCY3kyblVqWFFoTURZd3pydmpuek9jSjVfWjB5enlySmFER1NRNGE4SjF1akNoeXVQN3ZiN1ZNd3hMQ2RGb0xwZ0pYQ25Xaw?oc=5>

### Ahead of Visa Earnings, Here's What Barchart Data Says Comes Next for V Stock
- Summary: Upcoming earnings release expected to influence V stock direction.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPVDRYY0luc2lVWF9UMW1NMFRNQmNHMEU5QXRrQ0RvaDVlbkJNUTFCUWpRdExncWlobndYNnUyNTBGYlVoaENBM1FtZTVkOGwzaDFCamttNVdjbXhJeWZwZjNsci1Rd2JKbEstLVE1ZzNoOExfQWlUWmxuRk1nejVseFVfcUp1c1lWTXFHZl8zcllrblh0N1JNWFZKUXZuYXdRQk1XcXM3QW5Sd1pSN3JvbGNJaGgzVE9haWJHdA?oc=5>

### V Stock Falls Below $400 Despite Visa Reporting Higher Fourth-Quarter Profit
- Summary: Visa reports higher Q4 profit, yet stock drops below $400, indicating market overreaction or other concerns.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPLUx5OGJFTk1CWlVSeFFqR2wtRUVKczNrZ0x1ZmxxaFFyRGN6bDB3WXhlWlZTWVlMaHZWSV9aVmZFZlBIMW1LbzN5enBxX3pYMFA5aGp6bW1ySkZMVEI5QkhQckFyMTR3cHpwcllHZ05zZXhESllJRVR3VTRacnZVU3ZhUFNFa05NSlBVLXZpdUV2SzRSZTJNQ3dNMzBtUlpOUGFKYk5TX01kcGp6cWFUQWVfQWRRYWFHQ1E?oc=5>

### Visa Q4 profit jumps: can earnings keep pace with the stock?
- Summary: Visa reports a Q4 profit increase, raising questions about sustaining earnings growth.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQWTFYMHU5S0UteXB3c1g2UTVKSUI3d2kxQ2Z5cGtpdjZmVWpBZkI1X3NoV25HaWowUmZLMlhFX2pxUzhWT2c1R3RVeEl2cXV2LTNoS19UVHhTd21YY3h2TW5LUVBzS2FlMHJOYVBEZDZqQzVEM2J1QlZMbTgyYVBCbndqV2RJYk4tcDhHcjJJVzR2VjJmUnROeGk1X3R5Rk1UbmFGUWJsbzFwOGYtSENnaC1iT2EtZw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **V** | **33.57** | **21.23** | **23.65** | **13.20** | **773,002,166,272.00 USD** | **20.83** |
| MA | 35.09 | 82.48 | 24.94 | 14.00 | 555,819,073,536.00 USD | 15.97 |
| PYPL | 10.88 | 2.45 | 7.87 | 2.00 | 47,355,830,272.00 USD | -15.14 |
| AXP | 17.98 | 5.98 | N/A | 11.30 | 213,979,840,512.00 USD | -10.08 |

Peers fetched as_of: 2026-10-30; V reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMingFBVV95cUxNOVdnMkQ3UTRZTjJXN2lxcGRIM0pBaUZYNS1JQm1UNmdXc0tORnJmTXl4ZEFVR1Q2LW5QQ2M5Y0lkektFZElVSjN6OVgzblZtSllkcEpFV2NHVlMwOWNub2JJY0J2aHpNcVozeEJnY2lERjJpcmV3eS02RnBuQVdvWDhCTm5UeFF1UGJmRzIySUljeWpJaE01d2JmS3hndw?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxOb0dyMXRNWWZvcXlhQXNPVEJsUjAzaWRzV3Y1NGhicm9mU3JGNmx2NnM1M0tnWTNreTlDU2ROYlJtcG5QYUhxbXJLbmg2VjFKamFpVG9ReGwtVDdsaW9GUHVaZ0tLY3FkeUhYZjlxZUdValVxYlpqS1Q3UWhEMFBHUFJR?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPN2ZWZlF0WjN5cWFYT3RvVV9zXzFibk5JRWl4MjU3ZWN5cUpCdkEyTnlWWDh1SGpBbkxnblZlVFNSVHREVDdiZ0h1Qk8zMlFiUWJWbHJHa09CTEF0UDBrX2hSeWo5eE5zWm1Fci1TYUgyOHZiVUVReDVwdEk2NGt6aWlKdTZQMTNPN1BUUGp6OG9JakZidHROLW9vWFFITnBudGJBVXJaOXo4elNjUWF2TGVEVlljd3dabkdQcXhfOUxSUl9kaUhIRHdB?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOUDhOakEyejNzU1M3RXZ3bGdRcGtuckFrTTFmcGk0WGoyb0VxNFpNS1VObGVfQmVPdFVKWC0tcjc0Rk83Z1JNX3lVNnE5R0Q3bDRNdGpFdk9GNHVlbjdWLWtoU2huTGxrNnlhZnFMQ0xaa2owRU9EYlNPbXExclIwbTYxMkFhRWs1cnNNbUgwRW1NUQ?oc=5
- https://news.google.com/rss/articles/CBMinwJBVV95cUxOYnBoZ19YTzBGZVR4YzFMOXNPbVZpc3FPUlV1MG92TlNtSWx3UFBPX0pPMVo1dWZQeWFfZEZfOGE0R3BwTGs2NTRZaUhaTjkzd2dBWXdKY0V3QTM5eFJxU2EzSmZ5Q3EwbkZJaUhsUngtV1RlNjhfdVJpTTdzeUFqSFdzRG9SYmhJTmJ2T2IxZ2p3RXVmT2JSSkZKUUlnbm15eWltQVVnd0dYZ3BRZ1NSSlY4MFZyX0NCYmtTbHQxdVJyaWZCOENCVVg4RHBDVEdMVDc5WUtvUlJHTzFWM3RmUkd0aU9IcmFzSHZnZHJwZTZWdDNKcDc1b2VLMS10M2YzWkJtOThpa2VSek84Ulo2OXZlejlJM2hsckg2ckdPcw?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQeWc0ZUwxcXpTaVdIQ1NCenRubXBzNDBHclFqYkxqWDgzemxKemlITnh5MXNDYjVkYmVIMmpNazZPZXVVQWpUQndFd2Y5eEVBc1Y3R0xvNWdtbXBOYXVkMENxbEhBQ19sajJEZEF4T1RPTWhySjdwMjlMUnQxM1Vkc1BJZ0JPQV9zZ2lFQnFjQWYtZXhPdks2WXlkVlJWOGRUbTRGNFhRM1FtMklZdXBNN3RaejNMVlRqYVdMaGxNc01wMXQxN09F0gHMAUFVX3lxTE5tNU1qLUgtNUZMeXFxV09hLUtJaExqVmswcUN6OXIybzdzQ1RBM0ZXOEx0TkxuVGZoNVdRMzh4MWx3M3pDemVkX0dKZFB0akg2T1BwbHlNUzRuQ0tlbjljNzU1VkxHUjRYQklOVmd1Z0xiTU5WNjExWTF6VXBRbmwteWFxVlZvTXFhOWVpNUVkSm56ZzdQbW1SbG4zaHluSEttT3F2dWlPTHRRMVFuRThEcVlmMjBBUEhlWTUweVZqelh5QWR3cDZUOVU1Sw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOQ0JtM0JOc2NMd2VBVV9JUTJLaDhRVVgwZ2h4d1JXQ3ZrYUFKMEVsamN3Wmk5WlNEamZTWkFtZ1NJQWtLTkdkeUJNVGY4aWdaT0ZWdHF3ZkU2U2VzdWtQd1Uzb1pselhZRGc3eEl5ZzN5WGtYY1hxUUlnV1FLRGdhYm4wTkt6MjhDdmhWOEJTYjhFT2NaY1NUdUQwdjA?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPeUZJR2FrYThtRXdfYnhJUjdwRGxSTnFvTV9WbC1VTnpZTXZzNzhNVTlFZUNrSFpSekE5QVZsdEI4c1BhVU5SQk1wbHBMQ0dDYVpRdUFYMngzY2JPdnVUSEhPeG9Jb3FNRm83cWdqeWhnLWtMMjRSQk1PTHFxNEJDYmJORldjRnBoajdEZ05aX2gxTGxLUzRGQUJ1czA2d25FSkFuYmoxLWJLNWJ0ZnVBT1FpOEV5ZHBVUHp1cWpWMA?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOam82YTZSWlVDQmdiM3dYbzhNWVctVmpCTGlXZENFMnpUS0xoN3pBR2I5NlpjLUVaMWdGbWJpb3Bvbk54dkJ1dHpKM2JkOUxkQUtBLXJfUU8wbGtNZEJoTWFUM0lweGZoX0NBWkswem44ZFk1WlhaMmhqeTJPM0hxMGJCMzRiVGFzc0ZGQmw1QlpfanJtdnNN?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPSXlJZkxLSEdaS2dtZXJyNkpfWDdnZHpKYzlUUGlka05SWXROTi1GMEFJYjloQTVrZ3NNc18yOEtqdndoeURRckREazhsLVlOVDNya3JtTFZVbFhPZklsZGFhMDM3cnRTam40VElqdVJuNUFRUDFhazJCMm1BWjNmNXI0R3Z3VWFYWDFrTUlwRHhjd3FG?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxNRjB4TnVIcVRCcy1FMEhWeWlMS3pUX09QTUo1dDFYNTJLRDR5U2lWc2hRdWpJbDFxdDVUNnVVN0ZOTDNtUWNNQ0NsSlRSNVBCTzJxUXlVUkYzWXM4Z3NUZEVQTFBzVmhwYXc0TzFjSWFGdWZpT2NYTWpJVHdtSE1PTHVDVUNqbjUtYUhqY2MzeVpCY3kyblVqWFFoTURZd3pydmpuek9jSjVfWjB5enlySmFER1NRNGE4SjF1akNoeXVQN3ZiN1ZNd3hMQ2RGb0xwZ0pYQ25Xaw?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPVDRYY0luc2lVWF9UMW1NMFRNQmNHMEU5QXRrQ0RvaDVlbkJNUTFCUWpRdExncWlobndYNnUyNTBGYlVoaENBM1FtZTVkOGwzaDFCamttNVdjbXhJeWZwZjNsci1Rd2JKbEstLVE1ZzNoOExfQWlUWmxuRk1nejVseFVfcUp1c1lWTXFHZl8zcllrblh0N1JNWFZKUXZuYXdRQk1XcXM3QW5Sd1pSN3JvbGNJaGgzVE9haWJHdA?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPLUx5OGJFTk1CWlVSeFFqR2wtRUVKczNrZ0x1ZmxxaFFyRGN6bDB3WXhlWlZTWVlMaHZWSV9aVmZFZlBIMW1LbzN5enBxX3pYMFA5aGp6bW1ySkZMVEI5QkhQckFyMTR3cHpwcllHZ05zZXhESllJRVR3VTRacnZVU3ZhUFNFa05NSlBVLXZpdUV2SzRSZTJNQ3dNMzBtUlpOUGFKYk5TX01kcGp6cWFUQWVfQWRRYWFHQ1E?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQWTFYMHU5S0UteXB3c1g2UTVKSUI3d2kxQ2Z5cGtpdjZmVWpBZkI1X3NoV25HaWowUmZLMlhFX2pxUzhWT2c1R3RVeEl2cXV2LTNoS19UVHhTd21YY3h2TW5LUVBzS2FlMHJOYVBEZDZqQzVEM2J1QlZMbTgyYVBCbndqV2RJYk4tcDhHcjJJVzR2VjJmUnROeGk1X3R5Rk1UbmFGUWJsbzFwOGYtSENnaC1iT2EtZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
