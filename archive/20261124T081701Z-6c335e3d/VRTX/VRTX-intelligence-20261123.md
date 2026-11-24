# VRTX Intelligence Report

- ticker: **VRTX**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/VRTX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/VRTX/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:27:10.453223+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 10, 'rule': 0, 'ai': 4, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261123T053847Z-45053549/VRTX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 10 unique headlines; 9 named publishers; 0 exact duplicates; 10 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 538.5400 |
| Return 1D (%) | 4.5668 |
| Return 1W (%) | 0.1395 |
| Return 1M (%) | 2.7885 |
| Return YTD (%) | 18.7886 |
| Return 1Y (%) | 26.1927 |
| Annualized volatility (%) | 29.9790 |
| Beta vs SPY | 0.5119 |
| Max drawdown (%) | -15.2113 |
| Sharpe (rf=0) | 0.9522 |
| Downside deviation (rf=0, %) | 18.2624 |
| Sortino (rf=0) | 1.5632 |
| Historical VaR 95% (1D, %) | 2.8874 |
| Historical ES 95% (1D, %) | 3.4662 |
| Correlation vs SPY | 0.2557 |
| Tracking error vs SPY (%) | 29.8899 |
| P/E (trailing) | 34.66 |
| P/B | 6.53 |
| EV/EBITDA | 26.80 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 27.04 |
| Gross margin (%) | 54.81 |
| Operating margin (%) | 37.79 |
| Return on equity (%) | 20.80 |
| Free cash flow yield (%) | 1.71 |
| MA50 | 523.1076 |
| Close vs MA50 (%) | 2.9501 |
| MA200 | 485.1819 |
| Close vs MA200 (%) | 10.9976 |
| RSI (14, Wilder) | 53.0775 |
| MACD (12,26) | 1.6413 |
| MACD signal (9) | 4.4323 |
| MACD histogram | -2.7910 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'VRTX': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 538.5400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 4.5668 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.1395 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.7885 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 18.7886 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 26.1927 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.9790 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.2624 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.5632 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8874 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4662 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2557 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.8899 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5119 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.2113 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9522 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 27.0390 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.8090 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7920 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 20.8020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.7122 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 34.6551 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.0775 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.7910 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.9501 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 10.9976 -> Clearly above the moving-average trend level.

## TAILWINDS

### Vertex Pharmaceuticals (VRTX) Stock May Be Undervalued After Its 187% Run
- Summary: Shares may be undervalued following a strong 187% run, suggesting potential upside.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOMzdqc19Jc2NUcjA5cHVIOWczYUxqTm1wM1JnczRZbURpcFdSNzZMalFPb2JwZlJpSzQ4QlpwUGE2dFN5b0RtWDdvczZDZ2dPRkRtY1NNVmRFVWFKR0FKa2hBVkdzX1pxZ0szMEI4Wlk0X1lDVmQtbjVnSWpJUGZsZXhRVHp4REFXVHoySkxBN1JxZ004Yk5WWHljU0dkUmdWb0l1Vg?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Vertex Pharmaceuticals: Look For Povetacicept Approval In 2 Weeks As Next Catalyst
- Summary: Povetacicept expected FDA approval within two weeks, potentially boosting Vertex’s pipeline momentum.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxNd3g5ZUlkYjdveC1zQUZ0cW5Bb3dUUXBfdlNxTFEzd2hKYm9HRWpBNGZlYXpoaFUwWFVha0VSdFdqQm1uMUp5WGw0OVg0LTBYYmtOUDg5RVpTMHkzbndsc0FCd1BzWFdIdUcweEszLXVwUGtpVTc0Y0E2RER5OWhHcWpZT29lWGZnSEJnNl9tOTlEd3M5OFR3UnNWRzZZN1ViWTBhcW1tWEwwYWNUc1EzS01TaVBqYXUxd1NPM0NDQQ?oc=5>

### Is Vertex Pharmaceuticals (VRTX) Undervalued Following The FDA Decision On Povetacicept?
- Summary: Analysts question Vertex’s valuation after FDA decision on povetacicept, suggesting potential undervaluation.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxNZ0pfVDFtYWNXbFllNUF4TGw1UXJxVnBzbzg3WWhJS3FIZTM5ZGhJVU1pWXFoZXMwLUxMNHcxQVpyWGV5NXJ6R0Y1V3lFQm1YYlZwR3ZaclBjQWFYYVpzN01OcHVFV3c1VHM4ak1EcEZQaVBVcDhfUHZKV0lGOHVfSjByNFNGd2ZJamlwSHVjUDUyTkNoMVNSajRscDNTYktOQ0dySmg3bklqcF92eGdvN19GN0tJNGZMN1lVaUIxR0JmTC1PaFVTU21pR21kOFpEeExHNlIyMzhVLXBMYnNMSzUzVnVmZ2wyQ0NTQ9IB8gFBVV95cUxOODVoS0NnWFZGVGFzd3JmSkxfOUExQl9yMElHdlRwMk1iZlRzc2ZsYWgxbVNvUGpQWkhRMHkxekVoNjdtY3g0d3M2Q19rWXVrYjVEVXh2QmI3azYzWlA3VXBadnJjdTFzdXlIdWpWMERGR045M3o3U3VYOVVGUENLUVJrQ05KcHk0UHlfMG5TaVoxX0dNcXc3YnBpVEE4S0x0VWtBWVJ1dERwVXNQdlV5NVVlb1JtTGJnTGRFTWVLZmZ2TWhKQnk3NzUtZjZuVXlGeTNNTTJGTExpUm9wWU90anRYanBxMHVPZVZFY0FWMHNmdw?oc=5>

### Will Vertex Pharmaceuticals (NASDAQ:VRTX) Turn Its Pipeline Into Momentum?
- Summary: Speculation on Vertex converting its pipeline into sustained growth momentum.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNMU1Na2x4LTJYbmw0VzEtZV82UldOUWkzYjVtdDFQVzRnVXlhaXh4OWNQRGt5QnY1c09DVWE2aVZYcE9zaE5XZjM4M3pBQWhBRzN3WVY3cUZrM1ZxcHVWMDdUeFgtWGx5RWp1dWFnSHdhYV9MdXZUNzkwTG1TZTFOYXZKZGt0cjlfOHNRblhWM1BaelIyV1NlYTZ4czMyZV9OcThpNVFJVE1lbVE4VmczN01jUU4wckU?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **VRTX** | **34.66** | **6.53** | **26.80** | **11.80** | **136,540,176,384.00 USD** | **26.19** |
| REGN | 20.83 | 2.82 | 15.58 | 36.30 | 97,472,708,608.00 USD | 25.26 |
| BIIB | 111.13 | 2.01 | 13.46 | 10.60 | 37,946,929,152.00 USD | 46.44 |
| AMGN | 26.03 | 16.92 | 16.09 | 8.50 | 242,890,899,456.00 USD | 36.54 |

Peers fetched as_of: 2026-11-23; VRTX reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-02-11 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

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

- https://news.google.com/rss/articles/CBMipAFBVV95cUxOMzdqc19Jc2NUcjA5cHVIOWczYUxqTm1wM1JnczRZbURpcFdSNzZMalFPb2JwZlJpSzQ4QlpwUGE2dFN5b0RtWDdvczZDZ2dPRkRtY1NNVmRFVWFKR0FKa2hBVkdzX1pxZ0szMEI4Wlk0X1lDVmQtbjVnSWpJUGZsZXhRVHp4REFXVHoySkxBN1JxZ004Yk5WWHljU0dkUmdWb0l1Vg?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxNd3g5ZUlkYjdveC1zQUZ0cW5Bb3dUUXBfdlNxTFEzd2hKYm9HRWpBNGZlYXpoaFUwWFVha0VSdFdqQm1uMUp5WGw0OVg0LTBYYmtOUDg5RVpTMHkzbndsc0FCd1BzWFdIdUcweEszLXVwUGtpVTc0Y0E2RER5OWhHcWpZT29lWGZnSEJnNl9tOTlEd3M5OFR3UnNWRzZZN1ViWTBhcW1tWEwwYWNUc1EzS01TaVBqYXUxd1NPM0NDQQ?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxNZ0pfVDFtYWNXbFllNUF4TGw1UXJxVnBzbzg3WWhJS3FIZTM5ZGhJVU1pWXFoZXMwLUxMNHcxQVpyWGV5NXJ6R0Y1V3lFQm1YYlZwR3ZaclBjQWFYYVpzN01OcHVFV3c1VHM4ak1EcEZQaVBVcDhfUHZKV0lGOHVfSjByNFNGd2ZJamlwSHVjUDUyTkNoMVNSajRscDNTYktOQ0dySmg3bklqcF92eGdvN19GN0tJNGZMN1lVaUIxR0JmTC1PaFVTU21pR21kOFpEeExHNlIyMzhVLXBMYnNMSzUzVnVmZ2wyQ0NTQ9IB8gFBVV95cUxOODVoS0NnWFZGVGFzd3JmSkxfOUExQl9yMElHdlRwMk1iZlRzc2ZsYWgxbVNvUGpQWkhRMHkxekVoNjdtY3g0d3M2Q19rWXVrYjVEVXh2QmI3azYzWlA3VXBadnJjdTFzdXlIdWpWMERGR045M3o3U3VYOVVGUENLUVJrQ05KcHk0UHlfMG5TaVoxX0dNcXc3YnBpVEE4S0x0VWtBWVJ1dERwVXNQdlV5NVVlb1JtTGJnTGRFTWVLZmZ2TWhKQnk3NzUtZjZuVXlGeTNNTTJGTExpUm9wWU90anRYanBxMHVPZVZFY0FWMHNmdw?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNMU1Na2x4LTJYbmw0VzEtZV82UldOUWkzYjVtdDFQVzRnVXlhaXh4OWNQRGt5QnY1c09DVWE2aVZYcE9zaE5XZjM4M3pBQWhBRzN3WVY3cUZrM1ZxcHVWMDdUeFgtWGx5RWp1dWFnSHdhYV9MdXZUNzkwTG1TZTFOYXZKZGt0cjlfOHNRblhWM1BaelIyV1NlYTZ4czMyZV9OcThpNVFJVE1lbVE4VmczN01jUU4wckU?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
