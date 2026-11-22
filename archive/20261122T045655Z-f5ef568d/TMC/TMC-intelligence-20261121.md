# TMC Intelligence Report

- ticker: **TMC**
- Report as_of: **2026-11-21**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/TMC/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TMC/key-statistics/
- AI analysis snapshot as_of: **2026-11-21**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-22T05:18:16.412369+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 3, 'rule': 3, 'ai': 0, 'unknown': 0})
- AI model(s) actually used: **N/A (no successful AI classification call)**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 3 unique headlines; 2 named publishers; 0 exact duplicates; 3 HTTPS source links; largest publisher share 66.67%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1.5200 |
| Return 1D (%) | -8.4337 |
| Return 1W (%) | -34.1991 |
| Return 1M (%) | -41.9847 |
| Return YTD (%) | -75.3647 |
| Return 1Y (%) | -70.8253 |
| Annualized volatility (%) | 94.9267 |
| Beta vs SPY | 3.5034 |
| Max drawdown (%) | -83.8983 |
| Sharpe (rf=0) | -0.8329 |
| Downside deviation (rf=0, %) | 65.0266 |
| Sortino (rf=0) | -1.2158 |
| Historical VaR 95% (1D, %) | 9.3843 |
| Historical ES 95% (1D, %) | 12.0481 |
| Correlation vs SPY | 0.5276 |
| Tracking error vs SPY (%) | 88.2246 |
| P/E (trailing) | N/A |
| P/B | -15.35 |
| EV/EBITDA | -3.23 |
| Revenue growth (%) | N/A |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 0.00 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 0.58 |
| MA50 | 2.9612 |
| Close vs MA50 (%) | -48.6695 |
| MA200 | 4.4976 |
| Close vs MA200 (%) | -66.2040 |
| RSI (14, Wilder) | 25.8016 |
| MACD (12,26) | -0.3421 |
| MACD signal (9) | -0.2964 |
| MACD histogram | -0.0457 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TMC': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1.5200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -8.4337 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -34.1991 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -41.9847 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -75.3647 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -70.8253 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 94.9267 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 65.0266 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.2158 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 9.3843 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 12.0481 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5276 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 88.2246 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.5034 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -83.8983 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.8329 -> Negative risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.5836 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 25.8016 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0457 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -48.6695 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -66.2040 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### The Metals Company Falls 7% As Rate Fears Hit Markets
- Summary: The Metals Company Falls 7% As Rate Fears Hit Markets
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxPVDY4NElpZmZDandQYmsyb1phSFJLOHZHYVpXMlVaOHRoMktDN0pYMG12REY1dEVSRlhQbGtYal96V2JrNU8xMDE0Mzk3dXRRY2RkMGdTX0hNV3BEbl95Zl9fbjd0Nk82SWd3S2FoTXNIek1NSWRyd3lXT0xWVWZvR1A4SnE?oc=5>

### The Metals Company Falls 7% Near Annual Low
- Summary: The Metals Company Falls 7% Near Annual Low
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxONXYyRUw4a3RZTzBjQUFjMHhabERrUVJKRzNHelVlak1adjZobFl5QVN5ZDZYVEJpTkRJVVRTb0JUcEhPSjlHaDRKTWhFQi1SNmM5WFN2ampMaE1Sckx2aG9zSWk0d1Ryc0gtRExMNTBTbVlaVG04SzVrazM1cVo1V2VzN3c?oc=5>

## CATALYSTS

### TMC The Metals (TMC) Stock Sees Fair Value Falls After Q3 Sparks Analyst Target Cuts
- Summary: TMC The Metals (TMC) Stock Sees Fair Value Falls After Q3 Sparks Analyst Target Cuts
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOMS1ydzc4azJSWFh1ZHZrMTlTel9td2NBdWl5SFl5b0Z3M0tZNGoxcUxQYnBsdmJ6clRQR0RTU3NRSE1nUlFhQktrbkE0dWFvZW1SU3dUeFNhSHE5eDJabVY2d1ZpcVNrVmVYWlRIeEJoZ0YtaHBiZGVrRnZEVGEzcEpNMklYX1ZfS3cycUlzdUNQQ0Nv?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TMC** | **N/A** | **-15.35** | **-3.23** | **N/A** | **860,309,312.00 USD** | **-70.83** |
| MP | N/A | 3.10 | 98.06 | 190.90 | 6,052,197,888.00 USD | -40.10 |
| LAC | 3.63 | 0.31 | -21.89 | N/A | 479,215,136.00 USD | -73.49 |
| VALE | 59.31 | 1.04 | 1.84 | -3.90 | 40,387,194,880.00 USD | -13.78 |

Peers fetched as_of: 2026-11-21; TMC reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-12
- Next expected earnings: 2027-03-25 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-21

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

- https://news.google.com/rss/articles/CBMihAFBVV95cUxPVDY4NElpZmZDandQYmsyb1phSFJLOHZHYVpXMlVaOHRoMktDN0pYMG12REY1dEVSRlhQbGtYal96V2JrNU8xMDE0Mzk3dXRRY2RkMGdTX0hNV3BEbl95Zl9fbjd0Nk82SWd3S2FoTXNIek1NSWRyd3lXT0xWVWZvR1A4SnE?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxONXYyRUw4a3RZTzBjQUFjMHhabERrUVJKRzNHelVlak1adjZobFl5QVN5ZDZYVEJpTkRJVVRTb0JUcEhPSjlHaDRKTWhFQi1SNmM5WFN2ampMaE1Sckx2aG9zSWk0d1Ryc0gtRExMNTBTbVlaVG04SzVrazM1cVo1V2VzN3c?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOMS1ydzc4azJSWFh1ZHZrMTlTel9td2NBdWl5SFl5b0Z3M0tZNGoxcUxQYnBsdmJ6clRQR0RTU3NRSE1nUlFhQktrbkE0dWFvZW1SU3dUeFNhSHE5eDJabVY2d1ZpcVNrVmVYWlRIeEJoZ0YtaHBiZGVrRnZEVGEzcEpNMklYX1ZfS3cycUlzdUNQQ0Nv?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
