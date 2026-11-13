# VRTX Intelligence Report

- ticker: **VRTX**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/VRTX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/VRTX/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:01:13.553485+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 3, 'rule': 1, 'ai': 1, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 3 unique headlines; 3 named publishers; 0 exact duplicates; 3 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-10

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 542.6200 |
| Return 1D (%) | -0.8062 |
| Return 1W (%) | 0.0221 |
| Return 1M (%) | 7.0256 |
| Return YTD (%) | 19.6886 |
| Return 1Y (%) | 24.9729 |
| Annualized volatility (%) | 29.6174 |
| Beta vs SPY | 0.4248 |
| Max drawdown (%) | -15.2113 |
| Sharpe (rf=0) | 0.9021 |
| Downside deviation (rf=0, %) | 18.2575 |
| Sortino (rf=0) | 1.4634 |
| Historical VaR 95% (1D, %) | 2.8866 |
| Historical ES 95% (1D, %) | 3.4957 |
| Correlation vs SPY | 0.1970 |
| Tracking error vs SPY (%) | 30.0926 |
| P/E (trailing) | 34.92 |
| P/B | 6.58 |
| EV/EBITDA | 27.01 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 27.20 |
| Gross margin (%) | 54.81 |
| Operating margin (%) | 37.79 |
| Return on equity (%) | 20.80 |
| Free cash flow yield (%) | 1.70 |
| MA50 | 522.7546 |
| Close vs MA50 (%) | 3.8001 |
| MA200 | 483.0278 |
| Close vs MA200 (%) | 12.3372 |
| RSI (14, Wilder) | 54.9669 |
| MACD (12,26) | 8.5174 |
| MACD signal (9) | 7.8173 |
| MACD histogram | 0.7001 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'VRTX': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 542.6200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.8062 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.0221 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.0256 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 19.6886 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 24.9729 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.6174 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.2575 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4634 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8866 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4957 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1970 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.0926 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4248 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.2113 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9021 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 27.2001 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.8090 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7920 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 20.8020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.6993 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 34.9176 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 54.9669 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7001 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.8001 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 12.3372 -> Clearly above the moving-average trend level.

## TAILWINDS

### Vertex Pharmaceuticals (VRTX) Stock Rises 0.69% (November 9, 2026): Golden Cross Formed
- Summary: Vertex Pharmaceuticals (VRTX) Stock Rises 0.69% (November 9, 2026): Golden Cross Formed
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNV0FPaTlSVF81V2pCYUd4cTJGajR2YmJtUy1WaERGR2dscjMyN09zQUg1NHd1T2w5TnNmamdsX3dXN3lGUDBJdU5xVlE1djFidHhzYy1fXzdyX292MlAwV3owYUhHWG5HOUxhVTlGcV8xWHRWci1Icl9kYnFTdFduSmJVdjJaRXNtWWxLTTJXa1k5VHlOSjRfV2FERVlyRXE5djIyN2VWTWtVVFhac1k1RnhuZU9kdlcwYTY0?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### An officer's proposed sale covers 15,286 Vertex Pharmaceuticals (VRTX) shares.
- Summary: An officer proposes to sell 15,286 VRTX shares, indicating a potential ownership change by an insider.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOX0ZDX1pFSXhhRUp6QUNHYk9GWmpxczQyZ0U2MWVsTE1JLVhOZlhoY0QtUXp1UE8wbm9NcXhUWFJsa3k2VjNSaGMwaU9zZFYzRnpIOWI4bzUxUHFfOXNRQk9CSXdBUk9zUF9XRFBDWFRXMkVkUDNlMzJsYmZsNXhSeTJETlJYVDZsQ2NnVGEwMDR2cFJudm1wOUl0SnpGZUIwRGR5NGJGMFQ5UQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **VRTX** | **34.92** | **6.58** | **27.01** | **11.80** | **137,574,612,992.00 USD** | **24.97** |
| REGN | 21.03 | 2.85 | 15.74 | 36.30 | 98,398,568,448.00 USD | 40.24 |
| BIIB | 109.86 | 1.96 | 13.18 | 10.60 | 37,026,009,088.00 USD | 55.12 |
| AMGN | 27.08 | 17.60 | 16.64 | 8.50 | 252,638,117,888.00 USD | 42.74 |

Peers fetched as_of: 2026-11-12; VRTX reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-02-11 (yfinance; expected dates may change)

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
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 640,799,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 653,600,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/875320/000087532026000291/vrtx-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNV0FPaTlSVF81V2pCYUd4cTJGajR2YmJtUy1WaERGR2dscjMyN09zQUg1NHd1T2w5TnNmamdsX3dXN3lGUDBJdU5xVlE1djFidHhzYy1fXzdyX292MlAwV3owYUhHWG5HOUxhVTlGcV8xWHRWci1Icl9kYnFTdFduSmJVdjJaRXNtWWxLTTJXa1k5VHlOSjRfV2FERVlyRXE5djIyN2VWTWtVVFhac1k1RnhuZU9kdlcwYTY0?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOX0ZDX1pFSXhhRUp6QUNHYk9GWmpxczQyZ0U2MWVsTE1JLVhOZlhoY0QtUXp1UE8wbm9NcXhUWFJsa3k2VjNSaGMwaU9zZFYzRnpIOWI4bzUxUHFfOXNRQk9CSXdBUk9zUF9XRFBDWFRXMkVkUDNlMzJsYmZsNXhSeTJETlJYVDZsQ2NnVGEwMDR2cFJudm1wOUl0SnpGZUIwRGR5NGJGMFQ5UQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
