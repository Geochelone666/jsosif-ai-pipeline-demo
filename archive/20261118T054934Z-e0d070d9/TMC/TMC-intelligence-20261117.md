# TMC Intelligence Report

- ticker: **TMC**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/TMC/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TMC/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T05:49:42.714891+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 5, 'rule': 0, 'ai': 2, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/TMC** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 5 unique headlines; 3 named publishers; 1 exact duplicates; 5 HTTPS source links; largest publisher share 60.0%; oldest publication 2026-11-10

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1.8600 |
| Return 1D (%) | -11.8483 |
| Return 1W (%) | -23.1405 |
| Return 1M (%) | -27.9070 |
| Return YTD (%) | -69.8541 |
| Return 1Y (%) | -61.9243 |
| Annualized volatility (%) | 94.9583 |
| Beta vs SPY | 3.5230 |
| Max drawdown (%) | -80.2966 |
| Sharpe (rf=0) | -0.5523 |
| Downside deviation (rf=0, %) | 64.0321 |
| Sortino (rf=0) | -0.8190 |
| Historical VaR 95% (1D, %) | 9.3843 |
| Historical ES 95% (1D, %) | 12.0481 |
| Correlation vs SPY | 0.5113 |
| Tracking error vs SPY (%) | 88.7064 |
| P/E (trailing) | N/A |
| P/B | -23.54 |
| EV/EBITDA | -4.46 |
| Revenue growth (%) | N/A |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 0.00 |
| Return on equity (%) | -1123.19 |
| Free cash flow yield (%) | 1.97 |
| MA50 | 3.1075 |
| Close vs MA50 (%) | -40.1448 |
| MA200 | 4.5695 |
| Close vs MA200 (%) | -59.2956 |
| RSI (14, Wilder) | 30.8169 |
| MACD (12,26) | -0.2703 |
| MACD signal (9) | -0.2722 |
| MACD histogram | 0.0018 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TMC': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1.8600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -11.8483 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -23.1405 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -27.9070 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -69.8541 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -61.9243 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 94.9583 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 64.0321 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.8190 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 9.3843 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 12.0481 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5113 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 88.7064 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.5230 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -80.2966 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.5523 -> Negative risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -1123.1911 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.9742 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 30.8169 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0018 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -40.1448 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -59.2956 -> Clearly below the moving-average trend level.

## TAILWINDS

### TMC The Metals Co (TMC) Advances Commercial Plans Amid Loss-Maki
- Summary: TMC pushes commercial plans forward despite losses, indicating resilience and growth focus.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxOeDYwVmZpWlFXbUpfdThVUHRjYnFXQlRXYWoxMWNTZnFiZTBQUFBSODk0cjRJM0U4RGtkaXBaUWtVT2lrYnpEVEZ0MXZOb2htV1ZmUGg2dnF2RTRUeFp3em9yY2wtd0d1WjVrbUpVbjc2aU9yZzRkZnNNMDF0WWE3Y2tMMXVTSk9KZ25mVFJwLS16VDNPVFYwS2VGREQ4dVF1cTUwZlhuaUtnbm5lcTNxbUpXVkQzWGpRM3hPQjFyTFpzb2Z3ZW5vSlp5SE8?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### TMC Provides Third Quarter 2026 Corporate Update
- Summary: TMC releases Q3 2026 update, offering guidance on performance and outlook.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQekZjZjdDdVFDUFdYc3BZZFp6Q2o2QXAybllVVjI3ZDhpc3J4S0FGZWg4LUtjMUsweEpOdHFrdlRRRlJrektZWEFXZDRfVmowR3ZQQ0gwOHdrb29GUUl2MUVjQlVwY3ZNTDlsWDAtWlNPTUd1Q2txNFJQZTNaUjJheDZ1UWpjQjZXREVyRWgtNENqZw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TMC** | **N/A** | **-23.54** | **-4.46** | **N/A** | **1,052,746,944.00 USD** | **-61.92** |
| MP | N/A | 3.19 | 100.66 | 190.90 | 6,214,421,504.00 USD | -38.82 |
| LAC | 4.03 | 0.34 | -22.71 | N/A | 532,041,984.00 USD | -70.44 |
| VALE | 65.12 | 1.14 | 1.90 | -3.90 | 44,345,057,280.00 USD | -7.28 |

Peers fetched as_of: 2026-11-17; TMC reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-12
- Next expected earnings: 2027-03-25 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-12
- Revenue (latest available single quarter): 410,000.00 USD; period 2024-04-01/2024-06-30; fiscal year/reporting period 2024/Q2
- Net income (latest available single quarter): -28,361,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1798562/000162828026073463/tmc-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMizAFBVV95cUxOeDYwVmZpWlFXbUpfdThVUHRjYnFXQlRXYWoxMWNTZnFiZTBQUFBSODk0cjRJM0U4RGtkaXBaUWtVT2lrYnpEVEZ0MXZOb2htV1ZmUGg2dnF2RTRUeFp3em9yY2wtd0d1WjVrbUpVbjc2aU9yZzRkZnNNMDF0WWE3Y2tMMXVTSk9KZ25mVFJwLS16VDNPVFYwS2VGREQ4dVF1cTUwZlhuaUtnbm5lcTNxbUpXVkQzWGpRM3hPQjFyTFpzb2Z3ZW5vSlp5SE8?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQekZjZjdDdVFDUFdYc3BZZFp6Q2o2QXAybllVVjI3ZDhpc3J4S0FGZWg4LUtjMUsweEpOdHFrdlRRRlJrektZWEFXZDRfVmowR3ZQQ0gwOHdrb29GUUl2MUVjQlVwY3ZNTDlsWDAtWlNPTUd1Q2txNFJQZTNaUjJheDZ1UWpjQjZXREVyRWgtNENqZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
