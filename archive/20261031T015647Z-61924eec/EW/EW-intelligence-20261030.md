# EW Intelligence Report

- ticker: **EW**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/EW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/EW/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:18:34.149808+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 2, 'ai': 7, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/EW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 7 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 41.67%; oldest publication 2026-10-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 92.0100 |
| Return 1D (%) | -2.5731 |
| Return 1W (%) | 3.3008 |
| Return 1M (%) | 6.5918 |
| Return YTD (%) | 7.9296 |
| Return 1Y (%) | 10.2180 |
| Annualized volatility (%) | 25.0571 |
| Beta vs SPY | 0.5672 |
| Max drawdown (%) | -13.1855 |
| Sharpe (rf=0) | 0.5145 |
| Downside deviation (rf=0, %) | 16.9927 |
| Sortino (rf=0) | 0.7587 |
| Historical VaR 95% (1D, %) | 2.5317 |
| Historical ES 95% (1D, %) | 3.1155 |
| Correlation vs SPY | 0.2895 |
| Tracking error vs SPY (%) | 24.6148 |
| P/E (trailing) | 54.77 |
| P/B | 5.00 |
| EV/EBITDA | 24.84 |
| Revenue growth (%) | 13.60 |
| Forward P/E (estimate) | 27.21 |
| Gross margin (%) | 77.84 |
| Operating margin (%) | 29.84 |
| Return on equity (%) | 9.18 |
| Free cash flow yield (%) | 2.32 |
| MA50 | 88.1428 |
| Close vs MA50 (%) | 4.3874 |
| MA200 | 85.4274 |
| Close vs MA200 (%) | 7.7055 |
| RSI (14, Wilder) | 59.8673 |
| MACD (12,26) | 1.3453 |
| MACD signal (9) | 0.6595 |
| MACD histogram | 0.6858 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'EW': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 92.0100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.5731 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.3008 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.5918 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 7.9296 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 10.2180 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.0571 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.9927 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.7587 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5317 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.1155 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2895 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.6148 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5672 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.1855 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5145 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 27.2150 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 77.8390 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 29.8390 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.1750 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.3238 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 54.7679 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.8673 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6858 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.3874 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 7.7055 -> Clearly above the moving-average trend level.

## TAILWINDS

### Curious about Edwards Lifesciences (EW) Q3 Performance? Explore Wall Street Estimates for Key Metrics
- Summary: Wall Street estimates for EW’s Q3 performance are discussed, indicating potential earnings outlook.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQcUxYRldwUFpxWERpMmstOThqQ0x4bDVJUW9kM2lpbnp3c3k3ZGpINE93Q0l4VXdVVmRPYm5ocm9mSngtM2dlNm5BQkNhSkphbHUtN0hteFhtVDlTanU3WG5DNmNpckZfTkpCU01ZWTltc3B5WjY2U0lwbDFjUjFuNWx0b25zanJGenA2cDc4SE5QX0pVU19ROThJU1pPNzJu?oc=5>

### Edwards Lifesciences (EW) Could Be 6% Undervalued As FDA Approvals Lift Growth Hopes
- Summary: EW may be undervalued due to FDA approvals, suggesting positive market sentiment.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxPOXJBRDlxNk9MbE0tVGZUNGp6dndMWDZuLTNYYjZSSTZGb0JYMmttV2NBRFBvRHBTbjFWWmJ5WjB3OW9aRnV5MzVVS2hOV1hhSDBHTkFKdlQ3bm5tUXdaYlZSLV9yZDU4NnpDY242eEZJMTV5VHFRMXFDc3hrVUlSSU90WElyMGtLRkxYVzBRaUVDVGt6ZlRJWG1sVE1PYUtmTDJEckpQNFFoamhYcGhXU1FBT05sQTlfdHN1aU4tRXlBaXhnck50amg0NWN1VHd4MjMzQlB1cHnSAdgBQVVfeXFMTzlyQUQ5cTZPTGxNLVRmVDRqenZ3TFg2bi0zWGI2Ukk2Rm9CWDJrbVdjQURQb0RwU24xVlpieVowdzlvWkZ1eTM1VUtoTldYYUgwR05BSnZUN25ubVF3WmJWUi1fcmQ1ODZ6Q2NuNnhGSTE1eVRxUTFxQ3N4a1VJUklPdFhJcjBrS0ZMWFcwUWlFQ1RremZUSVhtbFRNT2FLZkwyRHJKUDRRaGpoWHBoV1NRQU9ObEE5X3RzdWlOLUV5QWl4Z3JOdGpoNDVjdVR3eDIzM0JQdXB5?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Edwards Lifesciences Corporation $EW Stock: Generali Asset Management SPA SGR Lowers Position
- Summary: Edwards Lifesciences Corporation $EW Stock: Generali Asset Management SPA SGR Lowers Position
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5wFBVV95cUxNMzQ0THN2UUoyeGZNRjdOdm1RNjg3akkxQThTaUFPRC11ck93YzkzSWtzZmlvWXUyQUxaOUEya0pablJFRkp1YWRZRUl3VzMwWmxnM1BDQVlOV0hqc2ZqbWhuS1Ewc2U2d3N1cnQtX2ZmZjlLM01yMXp6ZG9PejkwSW1BSjhZdnZrWDJDWHQ5N01qa1FqaVJGYTRaSFlMdFpvaGt2Z0NQS1RHR2twSk9ZcUxXUmlJR044UVYtR3NMbi1zWWxWa21UVGQ1eWh6eXh0VVM5UlNhUVA2dER1VXFvaVQwVjJlZHM?oc=5>

### Edwards Lifesciences Corporation $EW Shares Sold by Investment House LLC
- Summary: Edwards Lifesciences Corporation $EW Shares Sold by Investment House LLC
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNd3FlWDl5c25zQnBucTFmRVpiaXpGZFZSRWdoSnREUk1hZEZ3eTk0S1pmU21udXNTckZaWFlSYnI2ZlJYQ0pWZEFVM2E2b29GQkNVT3VZNXpIWEM5X21WOVVEUWF0bU5OM3RsWlVTTGhVSXNiUEZaWnVaS2lyQnNKYjhJdWNjUExmSUh0SjljWmlMdkZ0V0VFNVFvQW1WQ3hTd3gyLXFEZ0RvV2JVa05Zc0VFc1RrQ2xiN2NObzl2SHFjeXNuYmZUSjBQS0Y?oc=5>

### Edwards Lifesciences Continually Innovating Ahead Of Q3 Results, Cardio Portfolio Thrives
- Summary: Edwards Lifesciences highlights ongoing innovation and strong cardio portfolio performance ahead of Q3 results.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNeGNQODFnODBXNHpLc1BVWWI5SndlUnkxdzZBX2dIX1V2MkJrb09OSXB6cGdNZ2k3NF9JSkJOSERwTmtaZ0M2NkhEOUVOWVJOWVdPUVZwRGNtNWs1ZVpGczdTa01leDFiTXVVWDBNUlFiNnk2Y3VuZzE0bmZ5TDRCOXFyZEZVZEtFTXBMdVIwRXkzemJEbUZqMWt4aWpWNklTMkdWYlFFSXJHSjJJQ1BadW9qSGNZdUx4NHpPRXRRVUJwak5HTlE?oc=5>

### Edwards Lifesciences (EW) Stock Forecast and Price Target 2026 $EW
- Summary: Analysts provide a 2026 price target and stock forecast for Edwards Lifesciences.
- Date: 2026-10-27 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiYEFVX3lxTE1BZWo2RkN6U005VVVUdW94UGlidnA5cVJaZTZETDF0RUtwT0ZHVl8yRGxGcGR0clk2WkdlWktiUXNGZEpMRDd4bTZDdVIzTWlEWFdUN3E1UVJ0Tnc3eF9PZQ?oc=5>

### Edwards Lifesciences Corporation Estimates – NYSE:EW
- Summary: Company releases earnings estimates for the upcoming period.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMic0FVX3lxTE1oRjI4ZzRwaG0xTzd2RGVNVUFvdm5wRnJBUk5OREpacGo4NHBLNDFObTNud1lfV2JDQ0NpZUVoWlU4ZGpOZXNoMkk3ZUdoNGlKaFZJdEJWUG92M2EyWDYtTmd1c0gtVTl2R2gyNkVodkxqZkE?oc=5>

### How Valve Device Approvals Will Impact Edwards Lifesciences Stock (EW)
- Summary: Valve device approvals could boost sales and market share.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxOX21WVk1yN0VPcnFmbXZIal9mcnh4bi1uRk5lSjFvMXN4X2s3Y0JfdjFlRUNWNGlxSmhPa0hNV0V5TmR6a3Y3eXJIaDczbXhhQzh1cGFfcUU5QXZKd0xGU1ZQYjRZTlpHTG1zWTIwUGVCQ1I3OC15U0dnQTRzOGxoWHUxZGhMczhFRy1ic0ZfYzd6M1oyc1hvMG5sVFd4QmRIYkVlODNDbk5jRXREM19ZX2Z1NFFVWkhFeGJ4VjRMYTFSYTVxXzgwOWZvSVJMRUJqaXfSAdcBQVVfeXFMTjVPYXFMNndxVUZHcUFuSG1PS0ZCdWpUVndWYWxXZXVySmE4cnYzWUpDWTZ0MEEwLXlQNkxqNEJWbnA5bDA1cEUzWjlnWHlrSGtiVUo0ZlJ3M1NPc2QyVjFZd0V4dXJwVlRSMFdzSUc0alhxUHBwaTRoLXV1OXZ0aHgxTWdYbm44VnAzem16UFFoUnMxUWNCMWVTNVVHSGR3bkdheTdTd1k5bmd3blVZdXNMWVpveGpsZVFDb3IyUW5wOVFkV0duT1YyTjlHQThpYW5fbG4xTG8?oc=5>

## RISKS

### 79,593 Edwards Lifesciences Corporation $EW Shares Sold by Robeco Institutional Asset Management B.V.
- Summary: Large share sale may signal confidence decline.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxNa1VUbHoyS3hYNzNHdlpKb2xxVFY1OXdacGgyVnJMNGRtVVJfd0Z0bU5KeUFyaFE3Z2dxdlBZVi1hQ2Z2bTMwRUNpYmQyVE1qRzJQcVg1ZHFLbVRnVWlVVE9oTzFUNFFIUGdOUGpsUUEwVWhicm9oOTF2cmpKTEM3LUU4WHZfYnZsdkdjSnByY3BJejRrVlZRZDRNYW1JX1d3eGZCV3lJMFFQdEREOHFweVl2XzljQnltcXVMT0xyTUpMYnZrQ3Zxdkc3ZzNPdGo5blhTLXpfRXpGMVhNTzBLcFlJdHB4a0lTQkFwQ1pwTQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **EW** | **54.77** | **5.00** | **24.84** | **13.60** | **53,034,565,632.00 USD** | **10.22** |
| MDT | 23.72 | 2.46 | 13.78 | 13.70 | 123,487,977,472.00 USD | 9.64 |
| BSX | 17.71 | 2.44 | 12.85 | 1.40 | 60,838,658,048.00 USD | -58.26 |
| ABT | 39.48 | 3.60 | 17.70 | 14.50 | 183,766,712,320.00 USD | -12.70 |

Peers fetched as_of: 2026-10-30; EW reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-23
- Next expected earnings: 2026-11-04 (yfinance; expected dates may change)

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
- Filing date: 2026-08-04
- Revenue (latest available single quarter): 1,741,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 241,900,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1099800/000109980026000043/ew-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMioAFBVV95cUxQcUxYRldwUFpxWERpMmstOThqQ0x4bDVJUW9kM2lpbnp3c3k3ZGpINE93Q0l4VXdVVmRPYm5ocm9mSngtM2dlNm5BQkNhSkphbHUtN0hteFhtVDlTanU3WG5DNmNpckZfTkpCU01ZWTltc3B5WjY2U0lwbDFjUjFuNWx0b25zanJGenA2cDc4SE5QX0pVU19ROThJU1pPNzJu?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxPOXJBRDlxNk9MbE0tVGZUNGp6dndMWDZuLTNYYjZSSTZGb0JYMmttV2NBRFBvRHBTbjFWWmJ5WjB3OW9aRnV5MzVVS2hOV1hhSDBHTkFKdlQ3bm5tUXdaYlZSLV9yZDU4NnpDY242eEZJMTV5VHFRMXFDc3hrVUlSSU90WElyMGtLRkxYVzBRaUVDVGt6ZlRJWG1sVE1PYUtmTDJEckpQNFFoamhYcGhXU1FBT05sQTlfdHN1aU4tRXlBaXhnck50amg0NWN1VHd4MjMzQlB1cHnSAdgBQVVfeXFMTzlyQUQ5cTZPTGxNLVRmVDRqenZ3TFg2bi0zWGI2Ukk2Rm9CWDJrbVdjQURQb0RwU24xVlpieVowdzlvWkZ1eTM1VUtoTldYYUgwR05BSnZUN25ubVF3WmJWUi1fcmQ1ODZ6Q2NuNnhGSTE1eVRxUTFxQ3N4a1VJUklPdFhJcjBrS0ZMWFcwUWlFQ1RremZUSVhtbFRNT2FLZkwyRHJKUDRRaGpoWHBoV1NRQU9ObEE5X3RzdWlOLUV5QWl4Z3JOdGpoNDVjdVR3eDIzM0JQdXB5?oc=5
- https://news.google.com/rss/articles/CBMi5wFBVV95cUxNMzQ0THN2UUoyeGZNRjdOdm1RNjg3akkxQThTaUFPRC11ck93YzkzSWtzZmlvWXUyQUxaOUEya0pablJFRkp1YWRZRUl3VzMwWmxnM1BDQVlOV0hqc2ZqbWhuS1Ewc2U2d3N1cnQtX2ZmZjlLM01yMXp6ZG9PejkwSW1BSjhZdnZrWDJDWHQ5N01qa1FqaVJGYTRaSFlMdFpvaGt2Z0NQS1RHR2twSk9ZcUxXUmlJR044UVYtR3NMbi1zWWxWa21UVGQ1eWh6eXh0VVM5UlNhUVA2dER1VXFvaVQwVjJlZHM?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNd3FlWDl5c25zQnBucTFmRVpiaXpGZFZSRWdoSnREUk1hZEZ3eTk0S1pmU21udXNTckZaWFlSYnI2ZlJYQ0pWZEFVM2E2b29GQkNVT3VZNXpIWEM5X21WOVVEUWF0bU5OM3RsWlVTTGhVSXNiUEZaWnVaS2lyQnNKYjhJdWNjUExmSUh0SjljWmlMdkZ0V0VFNVFvQW1WQ3hTd3gyLXFEZ0RvV2JVa05Zc0VFc1RrQ2xiN2NObzl2SHFjeXNuYmZUSjBQS0Y?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNeGNQODFnODBXNHpLc1BVWWI5SndlUnkxdzZBX2dIX1V2MkJrb09OSXB6cGdNZ2k3NF9JSkJOSERwTmtaZ0M2NkhEOUVOWVJOWVdPUVZwRGNtNWs1ZVpGczdTa01leDFiTXVVWDBNUlFiNnk2Y3VuZzE0bmZ5TDRCOXFyZEZVZEtFTXBMdVIwRXkzemJEbUZqMWt4aWpWNklTMkdWYlFFSXJHSjJJQ1BadW9qSGNZdUx4NHpPRXRRVUJwak5HTlE?oc=5
- https://news.google.com/rss/articles/CBMiYEFVX3lxTE1BZWo2RkN6U005VVVUdW94UGlidnA5cVJaZTZETDF0RUtwT0ZHVl8yRGxGcGR0clk2WkdlWktiUXNGZEpMRDd4bTZDdVIzTWlEWFdUN3E1UVJ0Tnc3eF9PZQ?oc=5
- https://news.google.com/rss/articles/CBMic0FVX3lxTE1oRjI4ZzRwaG0xTzd2RGVNVUFvdm5wRnJBUk5OREpacGo4NHBLNDFObTNud1lfV2JDQ0NpZUVoWlU4ZGpOZXNoMkk3ZUdoNGlKaFZJdEJWUG92M2EyWDYtTmd1c0gtVTl2R2gyNkVodkxqZkE?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxOX21WVk1yN0VPcnFmbXZIal9mcnh4bi1uRk5lSjFvMXN4X2s3Y0JfdjFlRUNWNGlxSmhPa0hNV0V5TmR6a3Y3eXJIaDczbXhhQzh1cGFfcUU5QXZKd0xGU1ZQYjRZTlpHTG1zWTIwUGVCQ1I3OC15U0dnQTRzOGxoWHUxZGhMczhFRy1ic0ZfYzd6M1oyc1hvMG5sVFd4QmRIYkVlODNDbk5jRXREM19ZX2Z1NFFVWkhFeGJ4VjRMYTFSYTVxXzgwOWZvSVJMRUJqaXfSAdcBQVVfeXFMTjVPYXFMNndxVUZHcUFuSG1PS0ZCdWpUVndWYWxXZXVySmE4cnYzWUpDWTZ0MEEwLXlQNkxqNEJWbnA5bDA1cEUzWjlnWHlrSGtiVUo0ZlJ3M1NPc2QyVjFZd0V4dXJwVlRSMFdzSUc0alhxUHBwaTRoLXV1OXZ0aHgxTWdYbm44VnAzem16UFFoUnMxUWNCMWVTNVVHSGR3bkdheTdTd1k5bmd3blVZdXNMWVpveGpsZVFDb3IyUW5wOVFkV0duT1YyTjlHQThpYW5fbG4xTG8?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxNa1VUbHoyS3hYNzNHdlpKb2xxVFY1OXdacGgyVnJMNGRtVVJfd0Z0bU5KeUFyaFE3Z2dxdlBZVi1hQ2Z2bTMwRUNpYmQyVE1qRzJQcVg1ZHFLbVRnVWlVVE9oTzFUNFFIUGdOUGpsUUEwVWhicm9oOTF2cmpKTEM3LUU4WHZfYnZsdkdjSnByY3BJejRrVlZRZDRNYW1JX1d3eGZCV3lJMFFQdEREOHFweVl2XzljQnltcXVMT0xyTUpMYnZrQ3Zxdkc3ZzNPdGo5blhTLXpfRXpGMVhNTzBLcFlJdHB4a0lTQkFwQ1pwTQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
