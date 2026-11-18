# MCO Intelligence Report

- ticker: **MCO**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/MCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:18:04.758250+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 6, 'rule': 2, 'ai': 1, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/MCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 6 unique headlines; 6 named publishers; 0 exact duplicates; 6 HTTPS source links; largest publisher share 16.67%; oldest publication 2026-11-10

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 484.4100 |
| Return 1D (%) | -4.3197 |
| Return 1W (%) | -5.1497 |
| Return 1M (%) | -0.1361 |
| Return YTD (%) | -4.5427 |
| Return 1Y (%) | 3.4931 |
| Annualized volatility (%) | 28.7731 |
| Beta vs SPY | 0.5398 |
| Max drawdown (%) | -23.6059 |
| Sharpe (rf=0) | 0.2638 |
| Downside deviation (rf=0, %) | 20.5546 |
| Sortino (rf=0) | 0.3692 |
| Historical VaR 95% (1D, %) | 2.4795 |
| Historical ES 95% (1D, %) | 3.9934 |
| Correlation vs SPY | 0.2586 |
| Tracking error vs SPY (%) | 28.5090 |
| P/E (trailing) | 29.56 |
| P/B | 25.56 |
| EV/EBITDA | 22.14 |
| Revenue growth (%) | 0.80 |
| Forward P/E (estimate) | 26.05 |
| Gross margin (%) | 74.63 |
| Operating margin (%) | 46.04 |
| Return on equity (%) | 76.74 |
| Free cash flow yield (%) | 3.03 |
| MA50 | 478.6578 |
| Close vs MA50 (%) | 1.2017 |
| MA200 | 464.7819 |
| Close vs MA200 (%) | 4.2231 |
| RSI (14, Wilder) | 44.9674 |
| MACD (12,26) | 7.1596 |
| MACD signal (9) | 9.1585 |
| MACD histogram | -1.9989 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCO': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 484.4100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -4.3197 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.1497 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -0.1361 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -4.5427 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.4931 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.7731 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.5546 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3692 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4795 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9934 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2586 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.5090 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5398 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.6059 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2638 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 26.0464 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 46.0370 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 76.7410 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.0346 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 29.5552 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 44.9674 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.9989 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.2017 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 4.2231 -> Slightly above the moving-average trend level.

## TAILWINDS

### Moody’s Corporation to Present at the J.P. Morgan Ultimate Services Investor Conference on November 17, 2026
- Summary: Moody’s will speak at a major investor conference, potentially boosting visibility and investor interest.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOOVhiMEkzblJKM1RreElFYnVBanVrS0Z4bzJaMEtVSkR6UTJEME1kbUhPQVFBbnQ3SlUweGxRVjhwdG9Db09uQ3JtQ0dObEhYT1hvTDVOZG45ZEl0NXNuMnY4Y2lUNWtGVXI2S1M5cF9wWUJYSzhndXhNTXFld1VfOFdFbklQLUx4SXE5dFFIVzhidmQ2YXh0TDln?oc=5>

## HEADWINDS

### Moody’s Shares Slide 4.3% as Broader Market Weakness Meets Ongoing Ratings Revenue Concerns
- Summary: Moody’s Shares Slide 4.3% as Broader Market Weakness Meets Ongoing Ratings Revenue Concerns
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxONG1NR0RfTFBRZmJxTWNUVHlVUUVRM2JudnNNbHF4RF91SHU4ZnhqLXd0NjRvUDV4WnBoNmtfWGtkNVhScGVrODRjZFhvNVJRbXhUOHhxNVBRanVFTTFsQWI3WVFHZ1kxc25UNVU2anFFSUJfOWFTVkJ6WXJtZXFWenZKYUpWT2FFREdqT1lBcTFRcTIyWFV6NWZaVGdHTjgxcnFZenZyalNmM0ZyaWpsbjdMRk5KVzVNSngteUFua2gwMHUwTzRfTXlrY2RPWGc?oc=5>

## CATALYSTS

### Moody's Corporation (NYSE:MCO) Passed Our Checks, And It's About To Pay A US$1.03 Dividend
- Summary: Moody's Corporation (NYSE:MCO) Passed Our Checks, And It's About To Pay A US$1.03 Dividend
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxQN05SbThuc2dURTRDSTNRUF9IX0JGcE5wT3d0bkJzakZaYVhzRVYtVVRpc2thVTRZOGZpMmc2VldpQzZ1eEh4Q3U1U1dHSG1rUVdDR3F0aDhJZXZ6SE1remctNTdramUxelRGbmZGX0V5aFpjNThvQ3Q3VDZJb0p1alZWYUdHWUNJdGlMS2txckpoMkxxelhPalNLSzRKVGJEcUYwZEtkcFl2OFUzMzVLVjgydHUzNjJQdVVCenprUlQtQlhPRDY3M0NabkdBa0hzSXpNdw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCO** | **29.56** | **25.56** | **22.14** | **0.80** | **83,523,952,640.00 USD** | **3.49** |
| SPGI | 27.02 | 6.65 | 17.58 | 6.80 | 131,136,266,240.00 USD | -1.34 |
| MSCI | 33.66 | -15.13 | 25.84 | 12.40 | 45,515,472,896.00 USD | 15.74 |
| FDS | 21.70 | 5.57 | 13.80 | 6.30 | 11,144,313,856.00 USD | 17.58 |

Peers fetched as_of: 2026-11-17; MCO reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-02-17 (yfinance; expected dates may change)

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
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 1,142,100,000.00 USD; period 2019-01-01/2019-03-31; fiscal year/reporting period 2019/Q1
- Net income (latest available single quarter): 734,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1059556/000162828026066731/mco-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxOOVhiMEkzblJKM1RreElFYnVBanVrS0Z4bzJaMEtVSkR6UTJEME1kbUhPQVFBbnQ3SlUweGxRVjhwdG9Db09uQ3JtQ0dObEhYT1hvTDVOZG45ZEl0NXNuMnY4Y2lUNWtGVXI2S1M5cF9wWUJYSzhndXhNTXFld1VfOFdFbklQLUx4SXE5dFFIVzhidmQ2YXh0TDln?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxONG1NR0RfTFBRZmJxTWNUVHlVUUVRM2JudnNNbHF4RF91SHU4ZnhqLXd0NjRvUDV4WnBoNmtfWGtkNVhScGVrODRjZFhvNVJRbXhUOHhxNVBRanVFTTFsQWI3WVFHZ1kxc25UNVU2anFFSUJfOWFTVkJ6WXJtZXFWenZKYUpWT2FFREdqT1lBcTFRcTIyWFV6NWZaVGdHTjgxcnFZenZyalNmM0ZyaWpsbjdMRk5KVzVNSngteUFua2gwMHUwTzRfTXlrY2RPWGc?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQN05SbThuc2dURTRDSTNRUF9IX0JGcE5wT3d0bkJzakZaYVhzRVYtVVRpc2thVTRZOGZpMmc2VldpQzZ1eEh4Q3U1U1dHSG1rUVdDR3F0aDhJZXZ6SE1remctNTdramUxelRGbmZGX0V5aFpjNThvQ3Q3VDZJb0p1alZWYUdHWUNJdGlMS2txckpoMkxxelhPalNLSzRKVGJEcUYwZEtkcFl2OFUzMzVLVjgydHUzNjJQdVVCenprUlQtQlhPRDY3M0NabkdBa0hzSXpNdw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
