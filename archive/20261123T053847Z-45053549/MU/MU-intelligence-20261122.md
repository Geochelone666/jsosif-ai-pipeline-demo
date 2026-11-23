# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-11-22**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-11-22**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-23T05:45:44.777003+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 1, 'ai': 11, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261122T045655Z-f5ef568d/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 7 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 34.78%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 594.5100 |
| Return 1D (%) | -13.8940 |
| Return 1W (%) | -23.6153 |
| Return 1M (%) | -33.6536 |
| Return YTD (%) | 108.4527 |
| Return 1Y (%) | 195.5680 |
| Annualized volatility (%) | 84.8609 |
| Beta vs SPY | 3.3667 |
| Max drawdown (%) | -50.9958 |
| Sharpe (rf=0) | 1.7044 |
| Downside deviation (rf=0, %) | 53.4888 |
| Sortino (rf=0) | 2.7041 |
| Historical VaR 95% (1D, %) | 7.3172 |
| Historical ES 95% (1D, %) | 10.6103 |
| Correlation vs SPY | 0.5671 |
| Tracking error vs SPY (%) | 77.6512 |
| P/E (trailing) | 8.00 |
| P/B | 4.86 |
| EV/EBITDA | 5.83 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 2.85 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 74.59 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 4.33 |
| MA50 | 912.1925 |
| Close vs MA50 (%) | -34.8263 |
| MA200 | 772.3604 |
| Close vs MA200 (%) | -23.0269 |
| RSI (14, Wilder) | 29.5189 |
| MACD (12,26) | -69.2101 |
| MACD signal (9) | -59.5370 |
| MACD histogram | -9.6731 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 594.5100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -13.8940 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -23.6153 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -33.6536 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 108.4527 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 195.5680 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 84.8609 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 53.4888 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.7041 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.3172 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.6103 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5671 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 77.6512 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3667 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -50.9958 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.7044 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 2.8469 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 74.5860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.3322 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 7.9983 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 29.5189 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -9.6731 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -34.8263 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -23.0269 -> Clearly below the moving-average trend level.

## TAILWINDS

### Why Is Micron Technology Stock Rising Today?
- Summary: Analysts highlight positive market sentiment and potential upside for Micron, driving current stock gains.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNZG1XWC12Nm54SXpHQXlpcDhPNmJQRGxtNmdXcEo4TjZzYnNCeWhKOEwzQUktd08wNUg3Z2pDMm9FX0FXUVFpaVNreTdxeFM5WlBuX2ZNZTVtdHJJYncwaU0zRTBwalJ1NndRQ2dqZDFnbHA3cjFRSjc2VU9GWVh3OVloRkFlaENDRHRNakl0SG5NN0Q1ZXdLRXVWN3Zfc2It?oc=5>

### How Much Upside Is Left In Micron Stock?
- Summary: Investors assess remaining growth potential for Micron, suggesting continued upward momentum.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOYy1naDRFbTJCbzZmMU5TTE9FYmxnY3JYdWI2X2RzT3Y1WmZqb3NyNDFIcGZRTDNKQkNnejUtaXMycENGUnp4TW5PaWhNNmdUeHNobFZRZXVXSG1oMDZOTHItTlVRQm5SZGhoZ3o5V0RPeFhCUmhtZ1RPOWxWbEFpWndKQVVETENUYmJWRUlCR3AzdEZFV0tIN3B3?oc=5>

## HEADWINDS

### Micron and Sandisk stocks might look like bargains, but analysts say that’s actually a red flag
- Summary: Analysts warn that low prices may signal underlying issues, suggesting caution for investors.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxONFBQTHoyOUt3Zi1vMFh5ZFN3ejlKb0tXSjlQQnkzQkZweXJZdEtRTFVKcll5LTVIQWQxbWQtSFRJanVXbThPbU16NUNQTUVFYVdvSTIySi1NMk9YTmkyYmtlcV9hQzV2SXJ1RzZfd0xqQ3NJY1otQ2ZrZ2VWMEU2azNkdXVDcG55SFJfRy1GQmpwQzM0eGw3dUNFbVZVQUZ4QVQyYVpHWnhWY3BLSDVPcnA1ZkFRcnlGdVB6b2ZDcUNVRVNQdTM5OWMzdkRyTXBGa3c?oc=5>

### 7 Red Days In A Row: Micron Technology Stock Is Down 27%
- Summary: Stock has fallen 27% over seven consecutive days, indicating a sharp decline.
- Date: 2026-11-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPWi1laGRDdmxIMDBFMk8zaTEzNXRUUWV3VlNQRTYwM0VpMVlBcTFBcUVZUlhZd1FIUXJRM0xrcC1OM1VrYUljd0RmQ2R6WVBwbzh5U2hoR09KUG9maGc3ZERoQkpzNlVWb0dsdmg0MHBTMVFjUk1qcFNkV3pZcEN2TVJ6OUVBOFE0dF8xNjVBOWhTRS16eUR1ampBNURWN25ibm1vY25ydWVOZ2k4X0RxMVVCVQ?oc=5>

### What Happens To Micron Stock If Prices Stop Rising?
- Summary: Explores potential decline if Micron’s share price stalls, indicating possible downside risk.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxOaEc0VF9fdFRCeTVJU0lHMkxCYzVHLTd2NXZMc0toOWhlbUd5bEl3eTY4aVJoV0huWU1jR1FuVHExOWJLM1k4bmt5bXkzMl80cnliZEhURHhzMHhWZWdXWUg1d09LS1VaLU1ubXpCVWFqcEQ1VXpFX2h4a1hMMGgxdFoyUWZFdHRRWFZzaWY1RS1ndHppaV9xcUdUWHRNWktEeTh6NmRxMzkyc2dJQkE?oc=5>

### Micron Stock Fell More Than 40% From Its June Record. History Says What It Did After Its 5 Other Drops This Deep.
- Summary: Highlights a steep 40% drop, suggesting a significant market correction and potential long-term weakness.
- Date: 2026-11-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOZG8yeWFVVTRUTndGRmVPNnRWS3Frc2R1UFBRcFh2eE9acmwxWTI1aHU2YUxwdWdzTlY4cU1yOXNTa0V5RVZ4eDhZSGRYQmdxS1lYblo2Vk1qNW9wem9VWFhxT0JJU1pKc1pTdlNpeWlHVzFabkFMTlFRZFM3Q2ZsYzZ1V3JmbWNjSnlTRUlObER6WEU0?oc=5>

### Why Micron Stock Crashed Today
- Summary: Analyzes the reasons behind today’s sharp decline, pointing to immediate negative catalysts.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTFBJOEpiNHBCaGxkQXVWRElZVThVMFRnbzhUQXhnOFNwTTVXWW05Y2hjWlZEVTh4eExrWXpiYkZmZTE4T0tKcXdxMjdxQlB2dHFJYTc3czczWHhxRmdkVUJ3YVduOXpSWDIyWTJUQVpCcDl0YXZ5dnFZNFpCS0V3dw?oc=5>

### Micron Stock (MU) Crashes Over 11% to Historic Bargain Levels. Wall Street Still Sees 169% Upside.
- Summary: Reports a 11% drop to low levels, yet analysts maintain upside potential, indicating mixed outlook.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxNdy0zVEhXR1E5NzUxQV9YQUxBSjZycXBWc0Y3YlRvZ05lUm9rSk9lQmxlX0Nhd2UtQ25pdkZLS3RDU2RGSmhHcGZKMGRSN1N2NTQxSjVVcG9ESXRiTm9hNE5Lc3RKRlk2c1BENFBscWZzd1ZWcHZieVduQW5HLW5KT0ZfYXNSRDhzV09OS0VEYm4xQW1yZjVxUy00MzU0NWw1V3NjeXZNX0plU2NIMXZRUXlRWklBTDJLOHdpQUZONA?oc=5>

### What's Going On With Micron Technology Stock Monday? (UPDATED)
- Summary: Provides updates on Monday’s stock performance, noting recent volatility and investor concerns.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.82
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOOENST1M1UlNIcFJqOHhNUzdFWV9lT2dXNU5Xc2E2WEpRdHA3YWxQZHFxNHRGaU51c3prVFhzeHhOVEpjN2lJdjZXeVE1eGVBbG82ZkdWbGxRWkQteDZUcUF5aHliSzkzVW5lVW1rZEJIcXo4Zi1jR0hnd2Rid3l2MXRBcTJsOEdNdVRLQUNLSU5TWjRKdWhtRU1FcnpUWHZkdXVPcW1FOHI?oc=5>

## CATALYSTS

### Micron Is Down 32% in a Month. Can MU Stock Get Back to $1,000?
- Summary: Micron shares dropped 32% within a month, questioning future recovery prospects.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNQ3J3M1QxV2ZsMXItUkt2THBabi1fY0tra0tvZEpTSFl6RzItTjhxcndNSDFOZ3F2M1g0RzA5TFM3eTlvLUw5dXViaGlNU1Q5YnZ2RTR1elc3elNoMzZnWjNsY0FPWjZUakcwN0tQVzQ1Z1N2MUlvRDFZNVJhbGV0UVBsMDdISUpnZmJscG5zWHVzQQ?oc=5>

### Prediction: This Will Be Micron’s Stock Price by the End of 2028
- Summary: Forecasts project Micron's stock price trajectory through 2028, indicating potential long-term trends.
- Date: 2026-11-21 | Impact: medium | Horizon: long | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOODQ0aGxEM1BzSF9NdGdnY3FsbXZvR09xN2JKLUw4NjAxQ3ZQdVlIMFlTOUxQSlJsQ3hjQVE5UGI2d1lRVUgyWVNUZVJCUTBMZldINElOMExQY3c5YWdiZVMzOGNnNmx2TzhmQjEyVmVIZWJjaTRhenpNUkxGUmlYSzdmZ29iUVYtc1J3Szl0Rm0yNGtUSGZzM2piUnRZUVZaMUVLcmJQc0g?oc=5>

## RISKS

### Micron Technology (MU) Keeps DRAM Price Fixing Lawsuit Alive After Judge Rejection
- Summary: Micron Technology (MU) Keeps DRAM Price Fixing Lawsuit Alive After Judge Rejection
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNZUpwaEUwOWZyeDh2VjJJaVlPVEtGSTBRNFJ0MVhHNzdGY2xmRHdzUkQtRy1SQmpMeHY5TUM2NFBEU2V6cDFBZV9JTGhyRDBhdFlUSHNYZFNMUThrU0diMUpJRzA5Q1QzLXU2SkRXRzZtZUJUdEdfV294dEoyRWdpMlhNX0RPWVdUTjcxT1lDX2tUWEd5TTJJdDFobzg?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **8.00** | **4.86** | **5.83** | **379.30** | **672,642,433,024.00 USD** | **195.57** |
| WDC | 9.18 | 10.45 | 15.42 | 55.50 | 97,739,538,432.00 USD | 86.55 |
| STX | 23.96 | 30.40 | 18.12 | 61.00 | 104,911,724,544.00 USD | 91.15 |
| NXPI | 18.50 | 4.90 | 12.38 | 19.30 | 59,270,258,688.00 USD | 29.92 |

Peers fetched as_of: 2026-11-22; MU reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-22

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-09
- Revenue (latest available single quarter): 8,440,000,000.00 USD; period 2018-06-01/2018-08-30; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 28,243,000,000.00 USD; period 2026-02-27/2026-05-28; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMioAFBVV95cUxNZG1XWC12Nm54SXpHQXlpcDhPNmJQRGxtNmdXcEo4TjZzYnNCeWhKOEwzQUktd08wNUg3Z2pDMm9FX0FXUVFpaVNreTdxeFM5WlBuX2ZNZTVtdHJJYncwaU0zRTBwalJ1NndRQ2dqZDFnbHA3cjFRSjc2VU9GWVh3OVloRkFlaENDRHRNakl0SG5NN0Q1ZXdLRXVWN3Zfc2It?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOYy1naDRFbTJCbzZmMU5TTE9FYmxnY3JYdWI2X2RzT3Y1WmZqb3NyNDFIcGZRTDNKQkNnejUtaXMycENGUnp4TW5PaWhNNmdUeHNobFZRZXVXSG1oMDZOTHItTlVRQm5SZGhoZ3o5V0RPeFhCUmhtZ1RPOWxWbEFpWndKQVVETENUYmJWRUlCR3AzdEZFV0tIN3B3?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxONFBQTHoyOUt3Zi1vMFh5ZFN3ejlKb0tXSjlQQnkzQkZweXJZdEtRTFVKcll5LTVIQWQxbWQtSFRJanVXbThPbU16NUNQTUVFYVdvSTIySi1NMk9YTmkyYmtlcV9hQzV2SXJ1RzZfd0xqQ3NJY1otQ2ZrZ2VWMEU2azNkdXVDcG55SFJfRy1GQmpwQzM0eGw3dUNFbVZVQUZ4QVQyYVpHWnhWY3BLSDVPcnA1ZkFRcnlGdVB6b2ZDcUNVRVNQdTM5OWMzdkRyTXBGa3c?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPWi1laGRDdmxIMDBFMk8zaTEzNXRUUWV3VlNQRTYwM0VpMVlBcTFBcUVZUlhZd1FIUXJRM0xrcC1OM1VrYUljd0RmQ2R6WVBwbzh5U2hoR09KUG9maGc3ZERoQkpzNlVWb0dsdmg0MHBTMVFjUk1qcFNkV3pZcEN2TVJ6OUVBOFE0dF8xNjVBOWhTRS16eUR1ampBNURWN25ibm1vY25ydWVOZ2k4X0RxMVVCVQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxOaEc0VF9fdFRCeTVJU0lHMkxCYzVHLTd2NXZMc0toOWhlbUd5bEl3eTY4aVJoV0huWU1jR1FuVHExOWJLM1k4bmt5bXkzMl80cnliZEhURHhzMHhWZWdXWUg1d09LS1VaLU1ubXpCVWFqcEQ1VXpFX2h4a1hMMGgxdFoyUWZFdHRRWFZzaWY1RS1ndHppaV9xcUdUWHRNWktEeTh6NmRxMzkyc2dJQkE?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOZG8yeWFVVTRUTndGRmVPNnRWS3Frc2R1UFBRcFh2eE9acmwxWTI1aHU2YUxwdWdzTlY4cU1yOXNTa0V5RVZ4eDhZSGRYQmdxS1lYblo2Vk1qNW9wem9VWFhxT0JJU1pKc1pTdlNpeWlHVzFabkFMTlFRZFM3Q2ZsYzZ1V3JmbWNjSnlTRUlObER6WEU0?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxQd1BPVy1BX2VIMkUtLTFCUjJSWmhpYmFJSHF4RUVxUkpiSVhpM0otckxPMVJ4bEY5b2szdVAyXzBSRV9XejFjZGtOaEtJZmZPMkg5VnR4bWdHWVRyUHhYNm9RS1V5aFY3YUxlaFBZeTZXaTIxYkthOHcyTEdudTY1dkZELS02Mmw4SVIxM1FHX3N5aFpDMnFjRWVGeTdhOXJQRVJqaEV1dEJQWHdxQmlCNnFTWjVVNEVEeHRpLWdqWGhSQ29aTDE0azh6R1hVdnlhVFBwYi1Ud2NzdHV4SXM2Wi13cWQtNWUy?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTFBJOEpiNHBCaGxkQXVWRElZVThVMFRnbzhUQXhnOFNwTTVXWW05Y2hjWlZEVTh4eExrWXpiYkZmZTE4T0tKcXdxMjdxQlB2dHFJYTc3czczWHhxRmdkVUJ3YVduOXpSWDIyWTJUQVpCcDl0YXZ5dnFZNFpCS0V3dw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNOU1hQmNSRmQ0aGJ5bzRfakxHSzlZWVJLYzFBOFFnbVNrSTBVWUJoTHhob3FQbGNwMkp2WXRsWm1yRnRaUHo5SWtaX0FtdkdkNm5Ib3BvM09ja3B3QnNTdlJfRDN3WW00dkZobjgyWndUNm9YR0Z0dGZJbkkwNVE5bG5nQTRFVFFOSE1jTUxhdU9yRGxNOTN6WEVWVQ?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxNdy0zVEhXR1E5NzUxQV9YQUxBSjZycXBWc0Y3YlRvZ05lUm9rSk9lQmxlX0Nhd2UtQ25pdkZLS3RDU2RGSmhHcGZKMGRSN1N2NTQxSjVVcG9ESXRiTm9hNE5Lc3RKRlk2c1BENFBscWZzd1ZWcHZieVduQW5HLW5KT0ZfYXNSRDhzV09OS0VEYm4xQW1yZjVxUy00MzU0NWw1V3NjeXZNX0plU2NIMXZRUXlRWklBTDJLOHdpQUZONA?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOOENST1M1UlNIcFJqOHhNUzdFWV9lT2dXNU5Xc2E2WEpRdHA3YWxQZHFxNHRGaU51c3prVFhzeHhOVEpjN2lJdjZXeVE1eGVBbG82ZkdWbGxRWkQteDZUcUF5aHliSzkzVW5lVW1rZEJIcXo4Zi1jR0hnd2Rid3l2MXRBcTJsOEdNdVRLQUNLSU5TWjRKdWhtRU1FcnpUWHZkdXVPcW1FOHI?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNQ3J3M1QxV2ZsMXItUkt2THBabi1fY0tra0tvZEpTSFl6RzItTjhxcndNSDFOZ3F2M1g0RzA5TFM3eTlvLUw5dXViaGlNU1Q5YnZ2RTR1elc3elNoMzZnWjNsY0FPWjZUakcwN0tQVzQ1Z1N2MUlvRDFZNVJhbGV0UVBsMDdISUpnZmJscG5zWHVzQQ?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOODQ0aGxEM1BzSF9NdGdnY3FsbXZvR09xN2JKLUw4NjAxQ3ZQdVlIMFlTOUxQSlJsQ3hjQVE5UGI2d1lRVUgyWVNUZVJCUTBMZldINElOMExQY3c5YWdiZVMzOGNnNmx2TzhmQjEyVmVIZWJjaTRhenpNUkxGUmlYSzdmZ29iUVYtc1J3Szl0Rm0yNGtUSGZzM2piUnRZUVZaMUVLcmJQc0g?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNZUpwaEUwOWZyeDh2VjJJaVlPVEtGSTBRNFJ0MVhHNzdGY2xmRHdzUkQtRy1SQmpMeHY5TUM2NFBEU2V6cDFBZV9JTGhyRDBhdFlUSHNYZFNMUThrU0diMUpJRzA5Q1QzLXU2SkRXRzZtZUJUdEdfV294dEoyRWdpMlhNX0RPWVdUTjcxT1lDX2tUWEd5TTJJdDFobzg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
