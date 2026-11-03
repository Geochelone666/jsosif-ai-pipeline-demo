# DIS Intelligence Report

- ticker: **DIS**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/DIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/DIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:38:08.518563+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 1, 'ai': 4, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/DIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 6 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 41.67%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 113.1100 |
| Return 1D (%) | 1.9560 |
| Return 1W (%) | 2.4547 |
| Return 1M (%) | 10.6860 |
| Return YTD (%) | 0.1817 |
| Return 1Y (%) | 1.8894 |
| Annualized volatility (%) | 27.0206 |
| Beta vs SPY | 0.6058 |
| Max drawdown (%) | -20.2451 |
| Sharpe (rf=0) | 0.2216 |
| Downside deviation (rf=0, %) | 19.2514 |
| Sortino (rf=0) | 0.3110 |
| Historical VaR 95% (1D, %) | 2.4126 |
| Historical ES 95% (1D, %) | 3.7715 |
| Correlation vs SPY | 0.2875 |
| Tracking error vs SPY (%) | 26.3689 |
| P/E (trailing) | 22.90 |
| P/B | 1.78 |
| EV/EBITDA | 11.59 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 15.08 |
| Gross margin (%) | 37.59 |
| Operating margin (%) | 19.30 |
| Return on equity (%) | 8.01 |
| Free cash flow yield (%) | 2.49 |
| MA50 | 107.4612 |
| Close vs MA50 (%) | 5.2566 |
| MA200 | 103.0158 |
| Close vs MA200 (%) | 9.7987 |
| RSI (14, Wilder) | 63.8363 |
| MACD (12,26) | 1.5111 |
| MACD signal (9) | 1.4658 |
| MACD histogram | 0.0454 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'DIS': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 113.1100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.9560 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.4547 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 10.6860 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 0.1817 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 1.8894 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 27.0206 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.2514 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3110 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4126 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.7715 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2875 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.3689 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6058 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2451 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2216 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.0849 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 37.5950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 19.3010 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.0100 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.4886 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.8968 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 63.8363 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0454 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.2566 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.7987 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Walt Disney Earnings Preview: What to Expect
- Summary: Walt Disney Earnings Preview: What to Expect
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQMldKcDFFX2poOGxTdDBWdGEwSS1tRlI0NUVGaHYtNlVIazlqMFVTempwSlBpbV9uR2sxZDhOTzlKX3cxRFhldjFFa3FNc2d5M0dpdE9YX1hpeFZCWHQ3SGg5NFNpek5fSHBkUDdtWWJLVjUzVGJJWXU5LVZGMEtISmlJbkVoczMzbXl6Yk5wZ0U5dl9RSTlkNGZHVlAyTHliSXc?oc=5>

### The Walt Disney Company (DIS) is Attracting Investor Attention: Here is What You Should Know
- Summary: Overview of factors drawing investor focus to Disney, including financials and strategic moves.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQTTM0MEdOT2hXVGFBWU9rLW5FMS1pU2NnSHdBWmlmQjBsYlRlQmx6ZkZ6U0pIWU5FTU5Ncy1xQW4waUdVWnk4cFpGY1M0eDNFcnhCU205emoyQ05zZ0xiRHhGbmtrb09TSGpiX3NWLVpKS0RlektrWGl6VnpjRzhtNF94QnhUNFhZNkJySUJYdzhpMEpPMFB0Sk42YVFyTjhv?oc=5>

### How Much Upside Is Left In Disney Stock?
- Summary: Analysis of potential upside in Disney shares, considering current valuation and future prospects.
- Date: 2026-10-27 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQRkwzeUFCNXMtMzV6T2hVRXVmYVhhWVlfbnRUbHJQY1RHcHU4M1Bvd05fQ1hOV1hWVmFhcFV4bkRWY3hDZmdKOHUzWW5mYjZ5RVBkdGtHM1hDejkzc1I5STZBb1RRNjQzd0ZFN1RUa2hEWXdhcHVRTV81azZlVlJYMzRMZ0YzQTdWOW0zV2hPaldXQVlPSnd3OGVUbThvcC1t?oc=5>

### Disney Stock Forecast: DIS Guidance, Valuation and Risks
- Summary: Analysts discuss Disney’s future guidance, valuation metrics, and potential risks affecting the stock.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMidkFVX3lxTE41dUpLLXdRYk5Sel80Nll3NDdzZS1YZElydlhZbHd5ZUlSQVFxZVZtdE9RUGtMajg5X2pBUWNaZzFQZ3VFQlhja2lJR2l5bUJQT1pBbnB4WWx3aXJaU0tURVo0VzY1SjdJZzFHNjhJUEhwSnJIWEE?oc=5>

## RISKS

### Walt Disney (DIS) Stock Drops Despite Market Gains: Important Facts to Note
- Summary: Disney shares fell amid broader market gains, indicating investor concern over recent performance.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOYlBMWmx5TjRucnVzN1dpOVN4dG9wRFJFdEF0NHRkX1FhMnpLVmpiai1oTXI4VUtTSXdrdmF1N2gzQjZDX3l6UjJKb2U5M3V4NDcxNEJFdVVYTF8ySkJxZkY1ZEtrNmdoQXBhVXlLTDFIY2dMcmdoN19XVE5UVHBsbUN3N3NKLTJOdGF5ZWxJOGVoYWVldVI4?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **DIS** | **22.90** | **1.78** | **11.59** | **6.80** | **195,305,553,920.00 USD** | **1.89** |
| NFLX | 18.02 | 8.74 | 16.63 | 11.80 | 259,580,002,304.00 USD | -44.28 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| PSKY | N/A | 0.93 | 7.95 | 0.90 | 10,992,190,464.00 USD | N/A |

Peers fetched as_of: 2026-11-02; DIS reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-05
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 25,248,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,638,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1744489/000174448926000057/dis-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiogFBVV95cUxQMldKcDFFX2poOGxTdDBWdGEwSS1tRlI0NUVGaHYtNlVIazlqMFVTempwSlBpbV9uR2sxZDhOTzlKX3cxRFhldjFFa3FNc2d5M0dpdE9YX1hpeFZCWHQ3SGg5NFNpek5fSHBkUDdtWWJLVjUzVGJJWXU5LVZGMEtISmlJbkVoczMzbXl6Yk5wZ0U5dl9RSTlkNGZHVlAyTHliSXc?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQTTM0MEdOT2hXVGFBWU9rLW5FMS1pU2NnSHdBWmlmQjBsYlRlQmx6ZkZ6U0pIWU5FTU5Ncy1xQW4waUdVWnk4cFpGY1M0eDNFcnhCU205emoyQ05zZ0xiRHhGbmtrb09TSGpiX3NWLVpKS0RlektrWGl6VnpjRzhtNF94QnhUNFhZNkJySUJYdzhpMEpPMFB0Sk42YVFyTjhv?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQRkwzeUFCNXMtMzV6T2hVRXVmYVhhWVlfbnRUbHJQY1RHcHU4M1Bvd05fQ1hOV1hWVmFhcFV4bkRWY3hDZmdKOHUzWW5mYjZ5RVBkdGtHM1hDejkzc1I5STZBb1RRNjQzd0ZFN1RUa2hEWXdhcHVRTV81azZlVlJYMzRMZ0YzQTdWOW0zV2hPaldXQVlPSnd3OGVUbThvcC1t?oc=5
- https://news.google.com/rss/articles/CBMidkFVX3lxTE41dUpLLXdRYk5Sel80Nll3NDdzZS1YZElydlhZbHd5ZUlSQVFxZVZtdE9RUGtMajg5X2pBUWNaZzFQZ3VFQlhja2lJR2l5bUJQT1pBbnB4WWx3aXJaU0tURVo0VzY1SjdJZzFHNjhJUEhwSnJIWEE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOYlBMWmx5TjRucnVzN1dpOVN4dG9wRFJFdEF0NHRkX1FhMnpLVmpiai1oTXI4VUtTSXdrdmF1N2gzQjZDX3l6UjJKb2U5M3V4NDcxNEJFdVVYTF8ySkJxZkY1ZEtrNmdoQXBhVXlLTDFIY2dMcmdoN19XVE5UVHBsbUN3N3NKLTJOdGF5ZWxJOGVoYWVldVI4?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
