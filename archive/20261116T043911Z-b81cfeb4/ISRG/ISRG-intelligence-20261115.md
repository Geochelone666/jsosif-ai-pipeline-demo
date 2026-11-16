# ISRG Intelligence Report

- ticker: **ISRG**
- Report as_of: **2026-11-15**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/ISRG/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ISRG/key-statistics/
- AI analysis snapshot as_of: **2026-11-15**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-16T04:52:25.371947+00:00**
- AI status: **Partial: 3 headlines remain unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 17, 'rule': 3, 'ai': 8, 'unknown': 3, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261115T044154Z-6abfba73/ISRG** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 17 unique headlines; 10 named publishers; 0 exact duplicates; 17 HTTPS source links; largest publisher share 29.41%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 443.5900 |
| Return 1D (%) | 0.8411 |
| Return 1W (%) | -2.0340 |
| Return 1M (%) | 5.1012 |
| Return YTD (%) | -21.6770 |
| Return 1Y (%) | -21.5593 |
| Annualized volatility (%) | 35.5675 |
| Beta vs SPY | 0.9111 |
| Max drawdown (%) | -43.9960 |
| Sharpe (rf=0) | -0.5058 |
| Downside deviation (rf=0, %) | 26.3356 |
| Sortino (rf=0) | -0.6831 |
| Historical VaR 95% (1D, %) | 3.2143 |
| Historical ES 95% (1D, %) | 5.1297 |
| Correlation vs SPY | 0.3492 |
| Tracking error vs SPY (%) | 33.3502 |
| P/E (trailing) | 53.64 |
| P/B | 9.62 |
| EV/EBITDA | 33.52 |
| Revenue growth (%) | 21.70 |
| Forward P/E (estimate) | 35.58 |
| Gross margin (%) | 66.64 |
| Operating margin (%) | 31.70 |
| Return on equity (%) | 17.93 |
| Free cash flow yield (%) | 2.23 |
| MA50 | 417.5936 |
| Close vs MA50 (%) | 6.2253 |
| MA200 | 429.3807 |
| Close vs MA200 (%) | 3.3093 |
| RSI (14, Wilder) | 52.0777 |
| MACD (12,26) | 8.4543 |
| MACD signal (9) | 11.2069 |
| MACD histogram | -2.7526 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ISRG': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 443.5900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.8411 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.0340 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.1012 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -21.6770 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -21.5593 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.5675 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.3356 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.6831 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2143 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1297 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3492 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.3502 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9111 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.9960 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.5058 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 35.5761 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.6420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.7020 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.9320 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.2338 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 53.6384 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 52.0777 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.7526 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.2253 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.3093 -> Slightly above the moving-average trend level.

## TAILWINDS

### Intuitive Surgical price target raised to $500 from $470 at BofA
- Summary: Intuitive Surgical price target raised to $500 from $470 at BofA
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQVHU5UEh1ckhOS3VzSVVZb0czZU1WdXpKa1Nkd2I1NEpFZC1zMkRMQnpESWZ5UUdzb0VkQU9RUVlsRTJkMl9adTIzTzBCbzkwclhnc2UwczAzaTQzaHBXNk85TGZWNF92eU5mY0V3UVhLX2xES1NpckZfTHA2R0szODRiV19xWlVjVGY4NlNmOXdxUXhJMU9Obk1fTnliOFpLWmJ2RUNmVG5QVGhJTFZHSkNn?oc=5>

### Intuitive Surgical (ISRG) Adds Aaron Martin To Its Board
- Summary: Board addition signals governance strengthening and potential strategic direction.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxORWxZaFRHU3NDejZhVENYSlVyeWh0cGxUR0hUN3pFdThTVGtEUUtqRzlLMEx4UFA3Zml6U3hsZzhndnF3NGFLZll6aHNoS3ZQWk95SFRfYU1PVWpUWDhqZmxmOW5uUks1NTZMZ2pNcUJqdXo2SG1vTDNBTy1yRk1NbUFNamR0SGZHaTBEaWNRQ2FtUEJidzJGbHQ5WQ?oc=5>

### Intuitive Surgical (ISRG) Stock Looks In Line With Cash Flow After A 45% Run
- Summary: ISRG stock aligns with cash flow after a 45% run, indicating healthy valuation.
- Date: 2026-11-13 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxPLXU0OUM4LWFjWXZGN0hScU9GQkxULVJoT256bEZocFV0WjRpUGlwSnZlbDJDampJM256QVFKcnU4VGVJQ3hXM3lLZXFrYTJjX2o3OUlBbXBLYlV0dHdqV0ZsNFJ5OUhUZFo3SGJIY3VwU2tBbC1sYjg3WWhEVk1oQlY2aGdxVTQxUzB0dDJfVTFtM01PbTY3clZqVk1YM0t5MmZiRW42R29fY194Q2I5cFREMnFra2NTaXpLOUFxRXI0d1VKamFad0YzektQcmtXb0hlZkRn0gHbAUFVX3lxTE5VNTVxX08tUDh3SmNHdl9Ca2tpQ3RoM0g4dGtiMHZrdXkzeXZsZmFwOFE0UWtpY2Y1ZmxhMWJLU09yaWQzdnZxMG13WU9IYWNyY2FtWE9WdVpHVjMxYWxFUzZaUWM4UmRYYUdXYjRyVC1TZ3ZucmFzZEJkdDdqcmFKblJlWnRrSWNZYUdsUXIyU1BPclM5VmpnaUVES3FLZmFpR29ob0RSRHVhWWdvWjNFWDVNTXJUUGJlN1huaE9ILTMtckc3MHJrb2xqRVIxOUdvdWg4VkdpcjB6aw?oc=5>

### Intuitive Surgical (NASDAQ:ISRG): Strong Growth Meets a Constructive Technical Setup
- Summary: ISRG shows strong growth and a constructive technical setup, suggesting positive market momentum.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNLVp3elQtUjJkXzRMY1FZbGNSeXFwQXdwZDRCdmJrX2RCUEFZblJpMWE5S3dpc2tzWnYtSG5RZm95VzhKa0MwS0JITnVBWGVhUm5GN0tia2c5aExETTVzOVdBeTZmeTdRb3RDX09ZNVdtVUdiTWE2eUl6U2t6RHkybld0VFRPUHp6cFRndmU4V044UGNudGNLQkR6OEtsRGVJNmdjQ1lkSTNDcEtkSGEyY3hPb2E1S2l0YVlNaU9rTDR0ZjNURlVfajZPZVc?oc=5>

### Analysts Offer Insights on Healthcare Companies: Intuitive Surgical (ISRG) and ACADIA Pharmaceuticals (ACAD)
- Summary: Analysts discuss ISRG’s performance and outlook.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgJBVV95cUxOVjBsbEoxdUxKdkVKX00xaDNGVHFuVTdiNVU2bzNiMkN0bzNNMEdBb0x4UjF5X0FwZ1FENG9oUWoxdXhHSG1PRlZuOENqaVZ6RTZWY3pWTFlQWVdOeFU1WWl2WDFtdUxqSFJhVlJFQUVRa0JVVXFWbDQ4Z2NhSUtNZTF0UkVDWUVwUno4U1JYN2RNNnJVVjkxbUtJRjZ5cHNVSTRmbS1heTkwUXNoc29qR1doV2R2Umgxb0NCMzk4TmN5TV9QV3dFM0pvUGFxek9rRnJKa0YyaHRxOXpRMk5sQ2lKTEpEUlRRbldMUWRZSHdDdmhnX1hIUTlvcmNnU1o2QUJ2M1JGNGZGR3VIamYwOVhZUU5SV0JPUnc?oc=5>

### Intuitive Surgical (ISRG) Sees Rapid Single Port Robot Adoption
- Summary: ISRG reports fast adoption of its single-port robot technology.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNNzJod3JaMUNFVk1IY3dSM1NNN3hrSlNBaDlWM3hQd3Rfa3hOcUVxaFVDZWZIa3VsM0x5U1djZzhvd0QyM2tPcFVmMmN2YTVkT3N2d0o1X1JqUW41NDAtX25KZFRPVzFRbjZua2FWbEFtcmNWM09yMG93ZVlqbmJPcXV6NlN4UGJOd2hYOFl3RVZHVW15RGtqNUk0VlVoOVBYWnVjb19uZFdRRDRDSmVnMlQ4VFNQbU1xNTN1d29Pdno4VEdBWWxJbU9mUkU3VUpJR2RHUGtR0gHbAUFVX3lxTE45cFdMT3h0NFozVHBJOUN2ZnFDZVB3eFl5eDdqLVY1UnRsOTlkcWdLVmFrX3VnTDZ2N2w2am14dTNwVkhyVWtkeXJDQm8xQW1TUjZfTC1jNldLSk1sdHYzTXM3bHM2M2F0STVjR1F4QmNOSFRkdUNxbkU0NFpNS1FNT3ZBckNKcVdGcWhJLTJ3emZ4c2pqS2pNOTliVnpvMU9WTkxTUkNsNVk3cXdGSUlJM3hSWG0zQ1hCenBTbnV0OFNOWTR0Y1M2UHAyRVhhVnI4UF9aS25RZm9mRQ?oc=5>

### ISRG Gains 7.8% in 6 Months: Will the Share Price Recovery Continue?
- Summary: ISRG’s stock rose 7.8% over six months, prompting a recovery question.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxOS0p0TFpDX1JNWG8xV2pYbUhidC1PTHoySVVCMkV3Wm9hdFhJZV92VGxlZnVYZURkQmpTMDI4SEpITEI1SldVOWpnZ1F4aUgtMUYtMGgzVURVOF9KNGlFdkUtcVJlemRoSVVweFNVWGUyM0RBRFVhOUpaR0xyT1ZfQTRxdmpabGk1NWdwQVJmdWN0MjFxSXB5OVhTSUJfdUhzOUcyN1o5MUMtQlJuOU8zc3k2VlgtSEl4UGlrVXBn?oc=5>

## HEADWINDS

### Intuitive Surgical (ISRG) Dropped, So What Is Driving Attention Now?
- Summary: Recent share price decline indicates market concern over valuation or earnings expectations.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOY0xpOFlBYVhVVWlXR3F0eC16UU9SYUdfLTFDM2JPVDAySjlPb0FycHNQTE84MEI2Y3ZucFFiSjU3S3RHa2p4d1doTk5VVWxuN25hNFlRYmp4VWV6U3l6WjVjSE5CNG9EM2daSlhCS2FGTTd3dmNmaVpiWnRhdUg0RVZ6cUF2akw4WlpCa01LanF4dw?oc=5>

### What Has The Market Missed In Intuitive Surgical Stock’s Drop?
- Summary: Analysis of share price drop highlights potential overlooked risks or valuation issues.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPcnNNYlRENUEzZlozRzA1dVNKUXFzZTJHNFU5UV84YmhDWGdDY0NTSjluaHMtMURpWldGVTFEcUJrcW80QWs0dzVDa0FlN2IxM3FUMHRfeWNSRm9WWnUyelBUbkZNTkFaMmJ2OFlORTJ3dnZucG1mTW1Pc2JIRDRuMWJYSHFsRms0QWRkY2RodEF4eEFLZnlyMzRCZTNEazZpVHFIMVV0WDdpQWpWV0J2LUJNYnEzS0x1X3loNzl3?oc=5>

## CATALYSTS

### Intuitive Surgical (ISRG) Stock Fair Value Edges Higher After Mixed Q3 Analyst Revisions
- Summary: Intuitive Surgical (ISRG) Stock Fair Value Edges Higher After Mixed Q3 Analyst Revisions
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPQW1hV1lMNFBYRmJWdW9OTDVTTDV6QktCT3hhMGFteTFYdGJ5dGxSci1TNk1pdkVBUUhuRlJJamNodjcya3o1NXh5aVZTUWU3b1NNekM5YWdyd2IxU00xZ3hRRXdWdG96YmRRZXhIWUF0aGZfR2FfNC0zR21JZ05KSzNhckdBQlBFcFctbDVRV0o5cUplWXpuMjhSaTNSVFlR?oc=5>

### Intuitive Surgical (ISRG) Just Grew Revenue 22%. Why Is the Stock Still Down This Year?
- Summary: Intuitive Surgical (ISRG) Just Grew Revenue 22%. Why Is the Stock Still Down This Year?
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOV1JDa3pWOXNYTDdmclZzOG0yMVlIUElneWlQU05HbzZKQWdTdHZrVlZaaVhtMFcwT1RoUjMzaVdQY2tYeThqXzEtNWxNZGxZNUFDbEhCOU5WeFptd3ltY2lmTTVBR3NnLXlnS2RwUFNpUkJPVXBTQ1d2Zk5jWFJfLVYxelNTcFV1ajA0RDh6cjhLbm5ISkRsLWxQN29xb3M?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ISRG** | **53.64** | **9.62** | **33.52** | **21.70** | **153,767,690,240.00 USD** | **-21.56** |
| MDT | 25.27 | 2.62 | 14.58 | 13.70 | 131,572,129,792.00 USD | 10.54 |
| SYK | 32.98 | 5.03 | 17.32 | 7.60 | 117,877,170,176.00 USD | -16.16 |
| BSX | 18.71 | 2.51 | 13.62 | 1.40 | 64,269,643,776.00 USD | -57.76 |

Peers fetched as_of: 2026-11-15; ISRG reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-15

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMisgFBVV95cUxQVHU5UEh1ckhOS3VzSVVZb0czZU1WdXpKa1Nkd2I1NEpFZC1zMkRMQnpESWZ5UUdzb0VkQU9RUVlsRTJkMl9adTIzTzBCbzkwclhnc2UwczAzaTQzaHBXNk85TGZWNF92eU5mY0V3UVhLX2xES1NpckZfTHA2R0szODRiV19xWlVjVGY4NlNmOXdxUXhJMU9Obk1fTnliOFpLWmJ2RUNmVG5QVGhJTFZHSkNn?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxORWxZaFRHU3NDejZhVENYSlVyeWh0cGxUR0hUN3pFdThTVGtEUUtqRzlLMEx4UFA3Zml6U3hsZzhndnF3NGFLZll6aHNoS3ZQWk95SFRfYU1PVWpUWDhqZmxmOW5uUks1NTZMZ2pNcUJqdXo2SG1vTDNBTy1yRk1NbUFNamR0SGZHaTBEaWNRQ2FtUEJidzJGbHQ5WQ?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxPLXU0OUM4LWFjWXZGN0hScU9GQkxULVJoT256bEZocFV0WjRpUGlwSnZlbDJDampJM256QVFKcnU4VGVJQ3hXM3lLZXFrYTJjX2o3OUlBbXBLYlV0dHdqV0ZsNFJ5OUhUZFo3SGJIY3VwU2tBbC1sYjg3WWhEVk1oQlY2aGdxVTQxUzB0dDJfVTFtM01PbTY3clZqVk1YM0t5MmZiRW42R29fY194Q2I5cFREMnFra2NTaXpLOUFxRXI0d1VKamFad0YzektQcmtXb0hlZkRn0gHbAUFVX3lxTE5VNTVxX08tUDh3SmNHdl9Ca2tpQ3RoM0g4dGtiMHZrdXkzeXZsZmFwOFE0UWtpY2Y1ZmxhMWJLU09yaWQzdnZxMG13WU9IYWNyY2FtWE9WdVpHVjMxYWxFUzZaUWM4UmRYYUdXYjRyVC1TZ3ZucmFzZEJkdDdqcmFKblJlWnRrSWNZYUdsUXIyU1BPclM5VmpnaUVES3FLZmFpR29ob0RSRHVhWWdvWjNFWDVNTXJUUGJlN1huaE9ILTMtckc3MHJrb2xqRVIxOUdvdWg4VkdpcjB6aw?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNLVp3elQtUjJkXzRMY1FZbGNSeXFwQXdwZDRCdmJrX2RCUEFZblJpMWE5S3dpc2tzWnYtSG5RZm95VzhKa0MwS0JITnVBWGVhUm5GN0tia2c5aExETTVzOVdBeTZmeTdRb3RDX09ZNVdtVUdiTWE2eUl6U2t6RHkybld0VFRPUHp6cFRndmU4V044UGNudGNLQkR6OEtsRGVJNmdjQ1lkSTNDcEtkSGEyY3hPb2E1S2l0YVlNaU9rTDR0ZjNURlVfajZPZVc?oc=5
- https://news.google.com/rss/articles/CBMimgJBVV95cUxOVjBsbEoxdUxKdkVKX00xaDNGVHFuVTdiNVU2bzNiMkN0bzNNMEdBb0x4UjF5X0FwZ1FENG9oUWoxdXhHSG1PRlZuOENqaVZ6RTZWY3pWTFlQWVdOeFU1WWl2WDFtdUxqSFJhVlJFQUVRa0JVVXFWbDQ4Z2NhSUtNZTF0UkVDWUVwUno4U1JYN2RNNnJVVjkxbUtJRjZ5cHNVSTRmbS1heTkwUXNoc29qR1doV2R2Umgxb0NCMzk4TmN5TV9QV3dFM0pvUGFxek9rRnJKa0YyaHRxOXpRMk5sQ2lKTEpEUlRRbldMUWRZSHdDdmhnX1hIUTlvcmNnU1o2QUJ2M1JGNGZGR3VIamYwOVhZUU5SV0JPUnc?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNNzJod3JaMUNFVk1IY3dSM1NNN3hrSlNBaDlWM3hQd3Rfa3hOcUVxaFVDZWZIa3VsM0x5U1djZzhvd0QyM2tPcFVmMmN2YTVkT3N2d0o1X1JqUW41NDAtX25KZFRPVzFRbjZua2FWbEFtcmNWM09yMG93ZVlqbmJPcXV6NlN4UGJOd2hYOFl3RVZHVW15RGtqNUk0VlVoOVBYWnVjb19uZFdRRDRDSmVnMlQ4VFNQbU1xNTN1d29Pdno4VEdBWWxJbU9mUkU3VUpJR2RHUGtR0gHbAUFVX3lxTE45cFdMT3h0NFozVHBJOUN2ZnFDZVB3eFl5eDdqLVY1UnRsOTlkcWdLVmFrX3VnTDZ2N2w2am14dTNwVkhyVWtkeXJDQm8xQW1TUjZfTC1jNldLSk1sdHYzTXM3bHM2M2F0STVjR1F4QmNOSFRkdUNxbkU0NFpNS1FNT3ZBckNKcVdGcWhJLTJ3emZ4c2pqS2pNOTliVnpvMU9WTkxTUkNsNVk3cXdGSUlJM3hSWG0zQ1hCenBTbnV0OFNOWTR0Y1M2UHAyRVhhVnI4UF9aS25RZm9mRQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxOS0p0TFpDX1JNWG8xV2pYbUhidC1PTHoySVVCMkV3Wm9hdFhJZV92VGxlZnVYZURkQmpTMDI4SEpITEI1SldVOWpnZ1F4aUgtMUYtMGgzVURVOF9KNGlFdkUtcVJlemRoSVVweFNVWGUyM0RBRFVhOUpaR0xyT1ZfQTRxdmpabGk1NWdwQVJmdWN0MjFxSXB5OVhTSUJfdUhzOUcyN1o5MUMtQlJuOU8zc3k2VlgtSEl4UGlrVXBn?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOY0xpOFlBYVhVVWlXR3F0eC16UU9SYUdfLTFDM2JPVDAySjlPb0FycHNQTE84MEI2Y3ZucFFiSjU3S3RHa2p4d1doTk5VVWxuN25hNFlRYmp4VWV6U3l6WjVjSE5CNG9EM2daSlhCS2FGTTd3dmNmaVpiWnRhdUg0RVZ6cUF2akw4WlpCa01LanF4dw?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPcnNNYlRENUEzZlozRzA1dVNKUXFzZTJHNFU5UV84YmhDWGdDY0NTSjluaHMtMURpWldGVTFEcUJrcW80QWs0dzVDa0FlN2IxM3FUMHRfeWNSRm9WWnUyelBUbkZNTkFaMmJ2OFlORTJ3dnZucG1mTW1Pc2JIRDRuMWJYSHFsRms0QWRkY2RodEF4eEFLZnlyMzRCZTNEazZpVHFIMVV0WDdpQWpWV0J2LUJNYnEzS0x1X3loNzl3?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPQW1hV1lMNFBYRmJWdW9OTDVTTDV6QktCT3hhMGFteTFYdGJ5dGxSci1TNk1pdkVBUUhuRlJJamNodjcya3o1NXh5aVZTUWU3b1NNekM5YWdyd2IxU00xZ3hRRXdWdG96YmRRZXhIWUF0aGZfR2FfNC0zR21JZ05KSzNhckdBQlBFcFctbDVRV0o5cUplWXpuMjhSaTNSVFlR?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOV1JDa3pWOXNYTDdmclZzOG0yMVlIUElneWlQU05HbzZKQWdTdHZrVlZaaVhtMFcwT1RoUjMzaVdQY2tYeThqXzEtNWxNZGxZNUFDbEhCOU5WeFptd3ltY2lmTTVBR3NnLXlnS2RwUFNpUkJPVXBTQ1d2Zk5jWFJfLVYxelNTcFV1ajA0RDh6cjhLbm5ISkRsLWxQN29xb3M?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
