# EW Intelligence Report

- ticker: **EW**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/EW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/EW/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:25:22.208533+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 13, 'rule': 2, 'ai': 7, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 13 unique headlines; 7 named publishers; 0 exact duplicates; 13 HTTPS source links; largest publisher share 38.46%; oldest publication 2026-10-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 89.0700 |
| Return 1D (%) | -1.1322 |
| Return 1W (%) | 2.8522 |
| Return 1M (%) | 2.5916 |
| Return YTD (%) | 4.4809 |
| Return 1Y (%) | 16.3857 |
| Annualized volatility (%) | 25.5201 |
| Beta vs SPY | 0.5754 |
| Max drawdown (%) | -13.1855 |
| Sharpe (rf=0) | 0.7238 |
| Downside deviation (rf=0, %) | 16.8054 |
| Sortino (rf=0) | 1.0991 |
| Historical VaR 95% (1D, %) | 2.4786 |
| Historical ES 95% (1D, %) | 3.1091 |
| Correlation vs SPY | 0.2874 |
| Tracking error vs SPY (%) | 25.0357 |
| P/E (trailing) | 53.02 |
| P/B | 4.84 |
| EV/EBITDA | 23.99 |
| Revenue growth (%) | 13.60 |
| Forward P/E (estimate) | 26.35 |
| Gross margin (%) | 77.84 |
| Operating margin (%) | 29.84 |
| Return on equity (%) | 9.18 |
| Free cash flow yield (%) | 2.40 |
| MA50 | 88.0606 |
| Close vs MA50 (%) | 1.1463 |
| MA200 | 85.2276 |
| Close vs MA200 (%) | 4.5083 |
| RSI (14, Wilder) | 55.9980 |
| MACD (12,26) | 0.3404 |
| MACD signal (9) | -0.1418 |
| MACD histogram | 0.4822 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'EW': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 89.0700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.1322 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.8522 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.5916 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 4.4809 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 16.3857 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.5201 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.8054 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.0991 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4786 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.1091 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2874 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 25.0357 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5754 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.1855 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7238 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 26.3454 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 77.8390 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 29.8390 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.1750 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.4005 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 53.0179 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 55.9980 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4822 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.1463 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 4.5083 -> Slightly above the moving-average trend level.

## TAILWINDS

### FDA approval makes Edwards the only U.S. company with therapies to repair or replace mitral and tricuspid valves.
- Summary: FDA approval positions EW as sole U.S. provider of mitral and tricuspid valve therapies, boosting market share.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOYjhBUmtfcWwyT1hDb1lyaXlKVHpCV1VBZC1MSHNMTDVJeERsTFhJcGRscnlRa3U5blpVeUg1OWQ3VHNQdlNPNHRfR05ZVkhUTjFsRlNtUUVlZWIySkQxV1JfZXZSaUlMOU5jVHk4OUVfdGlTZW5OTXZ0RE5USVdQT29RZy1LejQ3SmxhU04xZnJlR01kRXZwZ0hzQmktSlQyN2lQaWlfR0MwMkp6M3U3Z2NjcnlFc2Izc1Rn?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Edwards Lifesciences Corporation (NYSE:EW) Stock Has Consensus Price Target of $100.27
- Summary: Edwards Lifesciences Corporation (NYSE:EW) Stock Has Consensus Price Target of $100.27
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxNRHVFSkJBLXQ4MjRSdFowUlcwLUdQMS1HTy1VZnRTSjJGOXV5dlNBb0Vval9MWERRUHlxMUxsZmJGM082LXA1Vnk5bTZWM1hlc1RlM3NwSkUxRkFjcEJrUXlQYWJaZzJXd0taZVA3a190SDdLWWhPSHk4YldHV1luRlZaUm1jLUlDbFRSMDd4cUNKMHNKUE93azBuN0Y1aWNDRmFCdUFrekVWWUxhSlk3OEdVMGlCcG81OHVCWThhZ2ZCUVR3RVZ1OXRldUlzZmI3MDJwZkRBOXc5NUo4ZnZN?oc=5>

### Edwards Lifesciences Corporation $EW Shares Sold by Investment House LLC
- Summary: Edwards Lifesciences Corporation $EW Shares Sold by Investment House LLC
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNd3FlWDl5c25zQnBucTFmRVpiaXpGZFZSRWdoSnREUk1hZEZ3eTk0S1pmU21udXNTckZaWFlSYnI2ZlJYQ0pWZEFVM2E2b29GQkNVT3VZNXpIWEM5X21WOVVEUWF0bU5OM3RsWlVTTGhVSXNiUEZaWnVaS2lyQnNKYjhJdWNjUExmSUh0SjljWmlMdkZ0V0VFNVFvQW1WQ3hTd3gyLXFEZ0RvV2JVa05Zc0VFc1RrQ2xiN2NObzl2SHFjeXNuYmZUSjBQS0Y?oc=5>

### Does Valve Repair Approval Change The Bull Case For Edwards Lifesciences (EW)?
- Summary: Valve repair approval could boost Edwards Lifesciences’ market position and investor sentiment.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPV0NiNzlISzVfYmI0NkJKMGEzTVVxTmVQOWc0dWlxcjdlTm5lYmJDcW96RkUwRHNHM0ZJeGcxSTNaZHZpSU1fSW4xSm9UcFBWSi1vT1VvaVhzT0N0SFlJeDZVTnEzTS14aXd5X2V0eV9ReEZwTHlzaUJpcHV2d2JqLWhLWjVTZ000QldZdlE3eTloeHV5MkFaTzNn?oc=5>

### How Valve Device Approvals Will Impact Edwards Lifesciences Stock (EW)
- Summary: New valve device approvals are expected to positively influence the company’s stock performance.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxOX21WVk1yN0VPcnFmbXZIal9mcnh4bi1uRk5lSjFvMXN4X2s3Y0JfdjFlRUNWNGlxSmhPa0hNV0V5TmR6a3Y3eXJIaDczbXhhQzh1cGFfcUU5QXZKd0xGU1ZQYjRZTlpHTG1zWTIwUGVCQ1I3OC15U0dnQTRzOGxoWHUxZGhMczhFRy1ic0ZfYzd6M1oyc1hvMG5sVFd4QmRIYkVlODNDbk5jRXREM19ZX2Z1NFFVWkhFeGJ4VjRMYTFSYTVxXzgwOWZvSVJMRUJqaXfSAdcBQVVfeXFMTjVPYXFMNndxVUZHcUFuSG1PS0ZCdWpUVndWYWxXZXVySmE4cnYzWUpDWTZ0MEEwLXlQNkxqNEJWbnA5bDA1cEUzWjlnWHlrSGtiVUo0ZlJ3M1NPc2QyVjFZd0V4dXJwVlRSMFdzSUc0alhxUHBwaTRoLXV1OXZ0aHgxTWdYbm44VnAzem16UFFoUnMxUWNCMWVTNVVHSGR3bkdheTdTd1k5bmd3blVZdXNMWVpveGpsZVFDb3IyUW5wOVFkV0duT1YyTjlHQThpYW5fbG4xTG8?oc=5>

### Edwards Lifesciences Corporation Estimates – NYSE:EW
- Summary: Company releases earnings estimates, providing insight into future financial performance.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMic0FVX3lxTE1oRjI4ZzRwaG0xTzd2RGVNVUFvdm5wRnJBUk5OREpacGo4NHBLNDFObTNud1lfV2JDQ0NpZUVoWlU4ZGpOZXNoMkk3ZUdoNGlKaFZJdEJWUG92M2EyWDYtTmd1c0gtVTl2R2gyNkVodkxqZkE?oc=5>

### Evercore ISI Raises Price Target for Edwards Lifesciences (EW) t
- Summary: Analyst Evercore ISI increases price target, indicating stronger growth expectations.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxNWjFuS1hJX1AxQXVjVXpyalNiTExPS2RkZ0NadTBIZ0JxZjBKVTdhb0ozN1VwVkpzLWFuejAxODVJQUlWU29nSVZVbnE3aHpScXFVRVNzcC1jQndpWWZ4NGVJWFZRdFZVNW41eHNYYnQ3c2N5YWd2TGNja3lkNUNiNGFhZV9RY2xGc0VqYV9TVm1xSUxCZHczWWdIR3RfZGt4eVhKQ1pHWVkyTVBEdTVvYVZPV0tXajZjMjNqR0dyaWJUc1BKZWczZnN0MVJISEZ5OHRB?oc=5>

### Edwards Lifesciences (EW) Stock Forecast and Price Target 2026 $EW
- Summary: Analysts project 2026 price target for EW, indicating future upside potential.
- Date: 2026-10-23 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiYEFVX3lxTE1BZWo2RkN6U005VVVUdW94UGlidnA5cVJaZTZETDF0RUtwT0ZHVl8yRGxGcGR0clk2WkdlWktiUXNGZEpMRDd4bTZDdVIzTWlEWFdUN3E1UVJ0Tnc3eF9PZQ?oc=5>

### Edwards Lifesciences (NYSE:EW) Stock Forecast & Analyst Predictions
- Summary: Analyst predictions suggest EW's future valuation trends.
- Date: 2026-10-21 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxNVURZUTZibGZKdmdBdVlyWVkxWVh5TkdvcnNFQkZTSTl1T2wxX0N5bENtQU5XZTN0YzZmSFBXcWJCekdncGJja0dKT2hXZHlJQk1yOXp3a2hQdDVMd3hrU29CaFBiT2NjMmtmRnRKRFdrQTlPR2k0TEdlb1ZiM1hBbnZBbE8?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **EW** | **53.02** | **4.84** | **23.99** | **13.60** | **51,339,948,032.00 USD** | **16.39** |
| MDT | 23.44 | 2.43 | 13.64 | 13.70 | 122,042,556,416.00 USD | 4.63 |
| BSX | 18.50 | 2.65 | 13.75 | 7.50 | 66,215,297,024.00 USD | -55.38 |
| ABT | 38.55 | 3.51 | 17.33 | 14.50 | 179,440,746,496.00 USD | -15.88 |

Peers fetched as_of: 2026-10-25; EW reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-23
- Next expected earnings: 2026-11-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-04
- Revenue (latest available single quarter): 1,741,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 241,900,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1099800/000109980026000043/ew-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOYjhBUmtfcWwyT1hDb1lyaXlKVHpCV1VBZC1MSHNMTDVJeERsTFhJcGRscnlRa3U5blpVeUg1OWQ3VHNQdlNPNHRfR05ZVkhUTjFsRlNtUUVlZWIySkQxV1JfZXZSaUlMOU5jVHk4OUVfdGlTZW5OTXZ0RE5USVdQT29RZy1LejQ3SmxhU04xZnJlR01kRXZwZ0hzQmktSlQyN2lQaWlfR0MwMkp6M3U3Z2NjcnlFc2Izc1Rn?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxNRHVFSkJBLXQ4MjRSdFowUlcwLUdQMS1HTy1VZnRTSjJGOXV5dlNBb0Vval9MWERRUHlxMUxsZmJGM082LXA1Vnk5bTZWM1hlc1RlM3NwSkUxRkFjcEJrUXlQYWJaZzJXd0taZVA3a190SDdLWWhPSHk4YldHV1luRlZaUm1jLUlDbFRSMDd4cUNKMHNKUE93azBuN0Y1aWNDRmFCdUFrekVWWUxhSlk3OEdVMGlCcG81OHVCWThhZ2ZCUVR3RVZ1OXRldUlzZmI3MDJwZkRBOXc5NUo4ZnZN?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNd3FlWDl5c25zQnBucTFmRVpiaXpGZFZSRWdoSnREUk1hZEZ3eTk0S1pmU21udXNTckZaWFlSYnI2ZlJYQ0pWZEFVM2E2b29GQkNVT3VZNXpIWEM5X21WOVVEUWF0bU5OM3RsWlVTTGhVSXNiUEZaWnVaS2lyQnNKYjhJdWNjUExmSUh0SjljWmlMdkZ0V0VFNVFvQW1WQ3hTd3gyLXFEZ0RvV2JVa05Zc0VFc1RrQ2xiN2NObzl2SHFjeXNuYmZUSjBQS0Y?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPV0NiNzlISzVfYmI0NkJKMGEzTVVxTmVQOWc0dWlxcjdlTm5lYmJDcW96RkUwRHNHM0ZJeGcxSTNaZHZpSU1fSW4xSm9UcFBWSi1vT1VvaVhzT0N0SFlJeDZVTnEzTS14aXd5X2V0eV9ReEZwTHlzaUJpcHV2d2JqLWhLWjVTZ000QldZdlE3eTloeHV5MkFaTzNn?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxOX21WVk1yN0VPcnFmbXZIal9mcnh4bi1uRk5lSjFvMXN4X2s3Y0JfdjFlRUNWNGlxSmhPa0hNV0V5TmR6a3Y3eXJIaDczbXhhQzh1cGFfcUU5QXZKd0xGU1ZQYjRZTlpHTG1zWTIwUGVCQ1I3OC15U0dnQTRzOGxoWHUxZGhMczhFRy1ic0ZfYzd6M1oyc1hvMG5sVFd4QmRIYkVlODNDbk5jRXREM19ZX2Z1NFFVWkhFeGJ4VjRMYTFSYTVxXzgwOWZvSVJMRUJqaXfSAdcBQVVfeXFMTjVPYXFMNndxVUZHcUFuSG1PS0ZCdWpUVndWYWxXZXVySmE4cnYzWUpDWTZ0MEEwLXlQNkxqNEJWbnA5bDA1cEUzWjlnWHlrSGtiVUo0ZlJ3M1NPc2QyVjFZd0V4dXJwVlRSMFdzSUc0alhxUHBwaTRoLXV1OXZ0aHgxTWdYbm44VnAzem16UFFoUnMxUWNCMWVTNVVHSGR3bkdheTdTd1k5bmd3blVZdXNMWVpveGpsZVFDb3IyUW5wOVFkV0duT1YyTjlHQThpYW5fbG4xTG8?oc=5
- https://news.google.com/rss/articles/CBMic0FVX3lxTE1oRjI4ZzRwaG0xTzd2RGVNVUFvdm5wRnJBUk5OREpacGo4NHBLNDFObTNud1lfV2JDQ0NpZUVoWlU4ZGpOZXNoMkk3ZUdoNGlKaFZJdEJWUG92M2EyWDYtTmd1c0gtVTl2R2gyNkVodkxqZkE?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxNWjFuS1hJX1AxQXVjVXpyalNiTExPS2RkZ0NadTBIZ0JxZjBKVTdhb0ozN1VwVkpzLWFuejAxODVJQUlWU29nSVZVbnE3aHpScXFVRVNzcC1jQndpWWZ4NGVJWFZRdFZVNW41eHNYYnQ3c2N5YWd2TGNja3lkNUNiNGFhZV9RY2xGc0VqYV9TVm1xSUxCZHczWWdIR3RfZGt4eVhKQ1pHWVkyTVBEdTVvYVZPV0tXajZjMjNqR0dyaWJUc1BKZWczZnN0MVJISEZ5OHRB?oc=5
- https://news.google.com/rss/articles/CBMiYEFVX3lxTE1BZWo2RkN6U005VVVUdW94UGlidnA5cVJaZTZETDF0RUtwT0ZHVl8yRGxGcGR0clk2WkdlWktiUXNGZEpMRDd4bTZDdVIzTWlEWFdUN3E1UVJ0Tnc3eF9PZQ?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxNVURZUTZibGZKdmdBdVlyWVkxWVh5TkdvcnNFQkZTSTl1T2wxX0N5bENtQU5XZTN0YzZmSFBXcWJCekdncGJja0dKT2hXZHlJQk1yOXp3a2hQdDVMd3hrU29CaFBiT2NjMmtmRnRKRFdrQTlPR2k0TEdlb1ZiM1hBbnZBbE8?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
