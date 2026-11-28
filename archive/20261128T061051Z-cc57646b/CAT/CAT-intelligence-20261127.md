# CAT Intelligence Report

- ticker: **CAT**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/CAT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CAT/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:18:21.560519+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 16, 'rule': 3, 'ai': 2, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/CAT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 16 unique headlines; 12 named publishers; 2 exact duplicates; 16 HTTPS source links; largest publisher share 18.75%; oldest publication 2026-11-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 561.7400 |
| Return 1D (%) | 3.3199 |
| Return 1W (%) | 10.0480 |
| Return 1M (%) | -21.2488 |
| Return YTD (%) | -1.1090 |
| Return 1Y (%) | -1.2572 |
| Annualized volatility (%) | 42.9192 |
| Beta vs SPY | 1.8139 |
| Max drawdown (%) | -51.8628 |
| Sharpe (rf=0) | 0.1759 |
| Downside deviation (rf=0, %) | 30.3395 |
| Sortino (rf=0) | 0.2489 |
| Historical VaR 95% (1D, %) | 4.5192 |
| Historical ES 95% (1D, %) | 5.8851 |
| Correlation vs SPY | 0.6349 |
| Tracking error vs SPY (%) | 35.3421 |
| P/E (trailing) | 22.05 |
| P/B | 11.97 |
| EV/EBITDA | 17.41 |
| Revenue growth (%) | 17.30 |
| Forward P/E (estimate) | 17.45 |
| Gross margin (%) | 29.54 |
| Operating margin (%) | 18.76 |
| Return on equity (%) | 56.14 |
| Free cash flow yield (%) | 1.55 |
| MA50 | 694.1271 |
| Close vs MA50 (%) | -19.0725 |
| MA200 | 797.2334 |
| Close vs MA200 (%) | -29.5388 |
| RSI (14, Wilder) | 39.6252 |
| MACD (12,26) | -42.2731 |
| MACD signal (9) | -46.4552 |
| MACD histogram | 4.1821 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CAT': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 561.7400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.3199 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 10.0480 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -21.2488 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -1.1090 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -1.2572 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 42.9192 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 30.3395 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2489 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.5192 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.8851 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6349 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.3421 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8139 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -51.8628 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1759 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.4546 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 29.5420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 18.7610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 56.1350 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.5457 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.0463 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 39.6252 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 4.1821 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -19.0725 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -29.5388 -> Clearly below the moving-average trend level.

## TAILWINDS

### Caterpillar Inc Stock (CAT) Moved Up by 3.12% on Nov 27: A Full Analysis
- Summary: Caterpillar Inc Stock (CAT) Moved Up by 3.12% on Nov 27: A Full Analysis
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPeXBtOXZOUDBHNG1oNENSZzhwRXlScHdCeko0QjU1RzNDMDg1U3VaQW9INEFqMHQ3SUYwTXkwQkdmYzU3SFVMR2l3X1d0UTlzQlVjMmE5alNxTnFkRmt3VnEyQlp2V1VOcUs2MlhlZ3YwZ21QNDBDcE9jaG9VUFRlNXZ4Tzc3aTVzNXc?oc=5>

## HEADWINDS

### Caterpillar Stock Today: CAT Drops 3% Toward 52-Week Low
- Summary: Caterpillar Stock Today: CAT Drops 3% Toward 52-Week Low
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOeHVmQzNoRWwySzR1UTUxTHdPMDY1M1J4UVBta3JqVWpjbmNqRGZKUF85UHA1dXhmNTFKcV9fTjZRY3JuVlhieE10QVRULTdqRDJkOVdFREsyelZ4OTduYWtOTDZUM2RHNDl5RER6SGZWZWljQ1V4MDNmMEh3ZWZ4WmNLQVlYYkRXQ05RSVloU09UNnVKdllBU3pB0gGfAUFVX3lxTFBpcEV5UGZpZjVzeldZbDAzcXlKb1dkLTBpT1lYOEJPemxtX3RhdUt0a2M1RWs1LXJxMzljbDVSSE5rME9YWWlDc3N4THB0Y0RfV1J2a1FrVThBTGpJZUgwemZoYU9YajF4U0ZXWXZaZzV0eU16UktMdDVNQWFnbDUxVmpzcWlZdWIzMG5KOTNlZjRjVkIzQ29YMVNYUDVIcw?oc=5>

### Caterpillar Inc Stock (CAT) Moved Down by 3.17% on Nov 24: Key Drivers Unveiled
- Summary: Caterpillar Inc Stock (CAT) Moved Down by 3.17% on Nov 24: Key Drivers Unveiled
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNUFQxeVVzdEp2V0w2MVZZQUt2MzBTWEJNYllYSk51S0VRVWdjdEtpb2tzQ2tPWWpuRmtPeUVpTDVIaWVpYTUzUW43cy1wY0QyMjFOSFgtelE3V2poblVIRDloaEtHM2t6d3ZYNW9wYU90ZEZFVHk3bGRDQkdoZDR4RFYxR3VFNjVROXc?oc=5>

## CATALYSTS

### The AI Stock Slump Is Crushing Caterpillar. Here’s Why I Like the Stock More Than Ever.
- Summary: Commentary on AI slump affecting CAT stock, expressing increased interest.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxPazU3MkhkenE2OV8yOGFLb1pEN04wMmRWMFMzLVZoTnN2N2w4V0IzMmlZdXVFejZZT2tqOVNOLW5XMU5iWFZ1WEFwM3dzSnNDbE1wQWlkaGk4NTFfZy10UEJ0MzhrbWVRRl9pcnRHUGZjQU1XVlAzUkMtMGRXajVjVUsxMzNWSmlnd09nR2lya1JabU14Q0E2N0gtcjNzd0N1UGNTUEVMOFZUSEUzUHNiSWNJOTE0blNFc3MyVlB6bXdYSUhnd0VZ?oc=5>

### 2027 Industrial Divide: Caterpillar Monetizes AI Power While Deere Chases an Ag Bottom
- Summary: CAT monetizes AI power, indicating product advancement.
- Date: 2026-11-25 | Impact: medium | Horizon: medium | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxOdWhrbzhuU25abzhCRGpxQ0ZNYkRxaUI2dkFhUWNKX2JpRXRLcGc4dDItU3FFRGdWQ1pzSGZrdjVNMGtsT0VkZjVoZHZ6cmg4cWdEbWRlM0FPSEdmY1R6QjZCZVNjM2lPN3dBTG5NUkN4Ym9KaEl2UGRQM21FZW85Vnl5Q01GRkhCS3R1RFVFODU4eTV1TnkzZHBPSkgyeGJPd1hOSFpNTHJrVnlBTXJRZGRzUTZWaG1LMThHaFE4ZlRWVjlhSGNOOQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CAT** | **22.05** | **11.97** | **17.41** | **17.30** | **257,048,952,832.00 USD** | **-1.26** |
| DE | 36.37 | 6.30 | 25.93 | -1.80 | 176,399,728,640.00 USD | 40.83 |
| CNH | 58.95 | 1.96 | 36.53 | -1.00 | 19,880,380,416.00 USD | 32.97 |
| CMI | 17.99 | 4.43 | 11.95 | 13.50 | 59,068,919,808.00 USD | -11.92 |

Peers fetched as_of: 2026-11-27; CAT reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
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

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 20,682,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 1,141,000,000.00 USD; period 2011-07-01/2011-09-30; fiscal year/reporting period 2011/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/18230/000001823026000057/cat-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiigFBVV95cUxPeXBtOXZOUDBHNG1oNENSZzhwRXlScHdCeko0QjU1RzNDMDg1U3VaQW9INEFqMHQ3SUYwTXkwQkdmYzU3SFVMR2l3X1d0UTlzQlVjMmE5alNxTnFkRmt3VnEyQlp2V1VOcUs2MlhlZ3YwZ21QNDBDcE9jaG9VUFRlNXZ4Tzc3aTVzNXc?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOeHVmQzNoRWwySzR1UTUxTHdPMDY1M1J4UVBta3JqVWpjbmNqRGZKUF85UHA1dXhmNTFKcV9fTjZRY3JuVlhieE10QVRULTdqRDJkOVdFREsyelZ4OTduYWtOTDZUM2RHNDl5RER6SGZWZWljQ1V4MDNmMEh3ZWZ4WmNLQVlYYkRXQ05RSVloU09UNnVKdllBU3pB0gGfAUFVX3lxTFBpcEV5UGZpZjVzeldZbDAzcXlKb1dkLTBpT1lYOEJPemxtX3RhdUt0a2M1RWs1LXJxMzljbDVSSE5rME9YWWlDc3N4THB0Y0RfV1J2a1FrVThBTGpJZUgwemZoYU9YajF4U0ZXWXZaZzV0eU16UktMdDVNQWFnbDUxVmpzcWlZdWIzMG5KOTNlZjRjVkIzQ29YMVNYUDVIcw?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNUFQxeVVzdEp2V0w2MVZZQUt2MzBTWEJNYllYSk51S0VRVWdjdEtpb2tzQ2tPWWpuRmtPeUVpTDVIaWVpYTUzUW43cy1wY0QyMjFOSFgtelE3V2poblVIRDloaEtHM2t6d3ZYNW9wYU90ZEZFVHk3bGRDQkdoZDR4RFYxR3VFNjVROXc?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPazU3MkhkenE2OV8yOGFLb1pEN04wMmRWMFMzLVZoTnN2N2w4V0IzMmlZdXVFejZZT2tqOVNOLW5XMU5iWFZ1WEFwM3dzSnNDbE1wQWlkaGk4NTFfZy10UEJ0MzhrbWVRRl9pcnRHUGZjQU1XVlAzUkMtMGRXajVjVUsxMzNWSmlnd09nR2lya1JabU14Q0E2N0gtcjNzd0N1UGNTUEVMOFZUSEUzUHNiSWNJOTE0blNFc3MyVlB6bXdYSUhnd0VZ?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxOdWhrbzhuU25abzhCRGpxQ0ZNYkRxaUI2dkFhUWNKX2JpRXRLcGc4dDItU3FFRGdWQ1pzSGZrdjVNMGtsT0VkZjVoZHZ6cmg4cWdEbWRlM0FPSEdmY1R6QjZCZVNjM2lPN3dBTG5NUkN4Ym9KaEl2UGRQM21FZW85Vnl5Q01GRkhCS3R1RFVFODU4eTV1TnkzZHBPSkgyeGJPd1hOSFpNTHJrVnlBTXJRZGRzUTZWaG1LMThHaFE4ZlRWVjlhSGNOOQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
