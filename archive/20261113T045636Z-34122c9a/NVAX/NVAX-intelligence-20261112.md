# NVAX Intelligence Report

- ticker: **NVAX**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/NVAX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVAX/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:18:28.590001+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 4, 'rule': 0, 'ai': 2, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/NVAX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 4 unique headlines; 2 named publishers; 0 exact duplicates; 4 HTTPS source links; largest publisher share 75.0%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 8.7600 |
| Return 1D (%) | -12.2244 |
| Return 1W (%) | -10.4294 |
| Return 1M (%) | -30.8057 |
| Return YTD (%) | 30.3572 |
| Return 1Y (%) | 21.6667 |
| Annualized volatility (%) | 73.6066 |
| Beta vs SPY | 2.0942 |
| Max drawdown (%) | -34.5844 |
| Sharpe (rf=0) | 0.6232 |
| Downside deviation (rf=0, %) | 44.0614 |
| Sortino (rf=0) | 1.0411 |
| Historical VaR 95% (1D, %) | 6.0826 |
| Historical ES 95% (1D, %) | 8.3779 |
| Correlation vs SPY | 0.3908 |
| Tracking error vs SPY (%) | 69.4006 |
| P/E (trailing) | N/A |
| P/B | -6.67 |
| EV/EBITDA | -20.12 |
| Revenue growth (%) | -3.00 |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | 5.30 |
| Operating margin (%) | -16.98 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 0.81 |
| MA50 | 10.5732 |
| Close vs MA50 (%) | -17.1490 |
| MA200 | 9.3384 |
| Close vs MA200 (%) | -6.1943 |
| RSI (14, Wilder) | 38.8806 |
| MACD (12,26) | -0.2663 |
| MACD signal (9) | -0.1610 |
| MACD histogram | -0.1054 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVAX': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 8.7600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -12.2244 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -10.4294 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -30.8057 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 30.3572 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 21.6667 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 73.6066 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 44.0614 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.0411 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.0826 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 8.3779 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3908 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 69.4006 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.0942 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -34.5844 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6232 -> Modest risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 5.2970 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: -16.9770 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.8133 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.8806 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1054 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -17.1490 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.1943 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Novavax (NVAX) stock trades up, here is why
- Summary: Shares of Novavax rose, driven by positive market sentiment and recent corporate developments.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQY1BYNFRsZjVRcEZNd3JxSFZ6MVpYSk5jRGRzNmJNR1EwdDVoMWtSN0lvUU1WaHhXZFpybTBLLXJOOFRFMDNNaTNNaHg4SzRDVGx6bC02Sm1fZUwwRmJqeHhFcm1FdWlrZDV1R18tSkFEVDdEaHQ2UFhnVkVxSUNmS1JOMVRBdnZNR2tyNklxaGMtd29UYVNVeHVR?oc=5>

### Novavax Inc (NVAX) (Q3 2026) Earnings Call Highlights: Sanofi Milestone Lifts Revenue Outlook ...
- Summary: Novavax reports Q3 2026 earnings, noting a Sanofi milestone that boosts revenue outlook.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxONnZJTDMzSkdIeW9sUnNnN1E0Tk9UaHJpV1VJMHZSbktpUFJuR2JSczhpVXlWTmd5aUktWGg5TEZwdXRiMjFkdGtydHZFbmpSSEh3U3pBbnR6dXlqVmZCYzJGMnZPUjNBTVVqSk83c2dBU1ZKbTJNd3lZR1EtZ0k2OUNZOHAxdVJJX2NXMWh3?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVAX** | **N/A** | **-6.67** | **-20.12** | **-3.00** | **1,445,478,912.00 USD** | **21.67** |
| MRNA | N/A | 13.67 | -51.97 | 29.20 | 93,609,058,304.00 USD | 766.16 |
| BNTX | N/A | 1.06 | -7.62 | -15.10 | 21,083,811,840.00 USD | -23.87 |
| GSK | 17.64 | 4.04 | 10.61 | 4.00 | 101,506,342,912.00 USD | 9.08 |

Peers fetched as_of: 2026-11-12; NVAX reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-05
- Next expected earnings: 2027-02-25 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-05
- Revenue (latest available single quarter): 68,298,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): -31,376,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1000694/000100069426000022/nvax-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxQY1BYNFRsZjVRcEZNd3JxSFZ6MVpYSk5jRGRzNmJNR1EwdDVoMWtSN0lvUU1WaHhXZFpybTBLLXJOOFRFMDNNaTNNaHg4SzRDVGx6bC02Sm1fZUwwRmJqeHhFcm1FdWlrZDV1R18tSkFEVDdEaHQ2UFhnVkVxSUNmS1JOMVRBdnZNR2tyNklxaGMtd29UYVNVeHVR?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxONnZJTDMzSkdIeW9sUnNnN1E0Tk9UaHJpV1VJMHZSbktpUFJuR2JSczhpVXlWTmd5aUktWGg5TEZwdXRiMjFkdGtydHZFbmpSSEh3U3pBbnR6dXlqVmZCYzJGMnZPUjNBTVVqSk83c2dBU1ZKbTJNd3lZR1EtZ0k2OUNZOHAxdVJJX2NXMWh3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
