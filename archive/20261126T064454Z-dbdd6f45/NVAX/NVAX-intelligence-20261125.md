# NVAX Intelligence Report

- ticker: **NVAX**
- Report as_of: **2026-11-25**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/NVAX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVAX/key-statistics/
- AI analysis snapshot as_of: **2026-11-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-26T06:53:00.893835+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 8, 'rule': 0, 'ai': 2, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/NVAX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 8 unique headlines; 7 named publishers; 0 exact duplicates; 8 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 7.8100 |
| Return 1D (%) | -1.8844 |
| Return 1W (%) | -1.8844 |
| Return 1M (%) | -19.4845 |
| Return YTD (%) | 16.2202 |
| Return 1Y (%) | 16.7414 |
| Annualized volatility (%) | 73.7895 |
| Beta vs SPY | 1.9291 |
| Max drawdown (%) | -41.7317 |
| Sharpe (rf=0) | 0.5672 |
| Downside deviation (rf=0, %) | 44.3259 |
| Sortino (rf=0) | 0.9442 |
| Historical VaR 95% (1D, %) | 6.0826 |
| Historical ES 95% (1D, %) | 8.3779 |
| Correlation vs SPY | 0.3903 |
| Tracking error vs SPY (%) | 69.3380 |
| P/E (trailing) | N/A |
| P/B | -5.94 |
| EV/EBITDA | -17.30 |
| Revenue growth (%) | -3.00 |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | 5.30 |
| Operating margin (%) | -16.98 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 0.91 |
| MA50 | 10.2492 |
| Close vs MA50 (%) | -23.7989 |
| MA200 | 9.3089 |
| Close vs MA200 (%) | -16.1022 |
| RSI (14, Wilder) | 36.5634 |
| MACD (12,26) | -0.7622 |
| MACD signal (9) | -0.6380 |
| MACD histogram | -0.1242 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVAX': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 7.8100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.8844 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.8844 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -19.4845 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 16.2202 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 16.7414 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 73.7895 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 44.3259 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.9442 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.0826 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 8.3779 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3903 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 69.3380 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.9291 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -41.7317 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5672 -> Modest risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 5.2970 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: -16.9770 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.9122 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.5634 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1242 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -23.7989 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -16.1022 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

No items in this run

## RISKS

### Novavax (NVAX) Stock Could Be Pricey Given Its Unsteady Sales Base
- Summary: Unsteady sales base may limit future growth, potentially keeping stock price high but unsustainable. Investors should monitor sales trends closely.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOR0ktQVlzcFNFTGd1dUlYQ0dOQ2pFeVpzdFBtR2gzVE9pNzRnYWM3VzJBaElHOS1MSUs5WE5qNV9fV2Y4aXhCcG5qek5yWGlkOEE2UjJqTjMyNEY0bWJhR0t2Q2tSZ1ZVSWJiekk5TDZva2pLdU9VTUVqZE9kS3F3bUxZZUgwRHA2aEV2bW1GS09LME5HUVVN?oc=5>

### Novavax (NVAX) Institutional Ownership 2026
- Summary: Projected institutional ownership levels for 2026.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiekFVX3lxTE4tNWx3M21heDNrdmtWWFVfdExFWTRHSXlOV0RFeTNELVFRcDJveG1rV0RHYW5TQV9vREIzZFBFS0JrbFB3M3R3OWtLRXl0amlEdnZwemNNLV9DbVNnQUExNDFrRkhHSFN0Rl85Vm8zQWNqUV80MmhuR1JR?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVAX** | **N/A** | **-5.94** | **-17.30** | **-3.00** | **1,288,720,384.00 USD** | **16.74** |
| MRNA | N/A | 13.05 | -49.59 | 29.20 | 89,356,492,800.00 USD | 792.28 |
| BNTX | N/A | 1.13 | -8.94 | -15.10 | 22,417,666,048.00 USD | -9.32 |
| GSK | 17.69 | 4.05 | 10.63 | 4.00 | 102,305,538,048.00 USD | 10.56 |

Peers fetched as_of: 2026-11-25; NVAX reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-05
- Next expected earnings: 2027-02-25 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-25

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

- https://news.google.com/rss/articles/CBMilwFBVV95cUxOR0ktQVlzcFNFTGd1dUlYQ0dOQ2pFeVpzdFBtR2gzVE9pNzRnYWM3VzJBaElHOS1MSUs5WE5qNV9fV2Y4aXhCcG5qek5yWGlkOEE2UjJqTjMyNEY0bWJhR0t2Q2tSZ1ZVSWJiekk5TDZva2pLdU9VTUVqZE9kS3F3bUxZZUgwRHA2aEV2bW1GS09LME5HUVVN?oc=5
- https://news.google.com/rss/articles/CBMiekFVX3lxTE4tNWx3M21heDNrdmtWWFVfdExFWTRHSXlOV0RFeTNELVFRcDJveG1rV0RHYW5TQV9vREIzZFBFS0JrbFB3M3R3OWtLRXl0amlEdnZwemNNLV9DbVNnQUExNDFrRkhHSFN0Rl85Vm8zQWNqUV80MmhuR1JR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
