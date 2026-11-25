# CAT Intelligence Report

- ticker: **CAT**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/CAT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CAT/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:06:38.303318+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 13, 'rule': 0, 'ai': 4, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/CAT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 13 unique headlines; 6 named publishers; 0 exact duplicates; 13 HTTPS source links; largest publisher share 38.46%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 540.6300 |
| Return 1D (%) | -1.1718 |
| Return 1W (%) | -5.2839 |
| Return 1M (%) | -21.1185 |
| Return YTD (%) | -4.8253 |
| Return 1Y (%) | -2.5684 |
| Annualized volatility (%) | 42.7389 |
| Beta vs SPY | 1.8097 |
| Max drawdown (%) | -51.8628 |
| Sharpe (rf=0) | 0.1520 |
| Downside deviation (rf=0, %) | 30.2790 |
| Sortino (rf=0) | 0.2145 |
| Historical VaR 95% (1D, %) | 4.5111 |
| Historical ES 95% (1D, %) | 5.8851 |
| Correlation vs SPY | 0.6332 |
| Tracking error vs SPY (%) | 35.2257 |
| P/E (trailing) | 21.22 |
| P/B | 11.52 |
| EV/EBITDA | 16.84 |
| Revenue growth (%) | 17.30 |
| Forward P/E (estimate) | 16.80 |
| Gross margin (%) | 29.54 |
| Operating margin (%) | 18.76 |
| Return on equity (%) | 56.14 |
| Free cash flow yield (%) | 1.61 |
| MA50 | 703.5693 |
| Close vs MA50 (%) | -23.1590 |
| MA200 | 799.2468 |
| Close vs MA200 (%) | -32.3576 |
| RSI (14, Wilder) | 33.8026 |
| MACD (12,26) | -47.3484 |
| MACD signal (9) | -47.9756 |
| MACD histogram | 0.6272 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CAT': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 540.6300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.1718 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.2839 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -21.1185 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -4.8253 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -2.5684 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 42.7389 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 30.2790 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2145 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.5111 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.8851 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6332 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.2257 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8097 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -51.8628 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1520 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.8015 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 29.5420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 18.7610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 56.1350 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.6061 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.2178 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 33.8026 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6272 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -23.1590 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -32.3576 -> Clearly below the moving-average trend level.

## TAILWINDS

### Caterpillar (CAT) Stock May Be Below Fair Value Following Fresh AI Power Demand
- Summary: Potential upside as AI power demand may lift valuation.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxPWjhrRnNibVBhd2ZacnVub2lLbVkxSGxDNjU1REtEUXJNTzgwaXJrVnNSb09sUmIzaE5OUW9oS3FZNGpQX2otQnhpQ0czNC1UZ19vLXJCZTRGZUNKRlpSNkZIN1NKME03eXg4UTNRSkY1MzdjZy0yUWlmX2VHa2dTV0xIX2FndEZXejVxM21FOWhoQkRfTjBYbWRCRE1LeGZ4YjFZOFdwQlVNX29Ga1RxUWpJYVM3b3pWa0ZhakZMZ1JxQkQ2VXRTc25zRE3SAdIBQVVfeXFMTnFxVkRVVDRwVDNsalZMSWlFcVpIdXBDYWhURktwWkxPbnh4RG1mb2s3RzBud0VkUkw1TnY5aG1MMjBOUHVqaE9UUE1wTDNfU21PYzltbHJYZlZIVXg2TkUzejI1VzNlNlJtU2d0bWZTcGNfZ0NNeExHMUJNYVpOOHRldzgybFZ5S3ZzVXlQYWpjc1ZRT0wwZG5KUG1lNWtRNVkxTVFRaHd4VzlzM0QtTERJWE42M3U0cTNtSjZHTm1PUGJDVzBBdVZLSC1oWE85VElR?oc=5>

## HEADWINDS

### Caterpillar's 35% 3-Month Downturn: This Sell-Side Firm Predicts 90% Returns From Here With Another Close Behind
- Summary: Recent sharp decline signals short-term weakness.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi5wFBVV95cUxOUFRvOXhUU0hwYWpwMUNJUkRnM1ZscUpEb1FWT05fT0I1SlJNb1BIRkpDR0lqOS1jRUJvM2xNbVllZHB6NUdvbEFmT1FKYWUwUUItZUJJQm9SbTZHNGRLTmVYYzBVR2JJSjRESVoxM1R6ZzNaMlFseUJmQUJraTc0M1VBOFcyLXkxdFE2NEF1SmRHLVZQNnZZcWRQZHZUX0ZnYUZXRDRVMHFORENhZThyd3NBNE4xOVE5TDFTZlZmb1E3Vzd5Q2owWUFBU3JKOFlUYkY1c3J3SVI5YU5BNnJmWHROcGVpbDA?oc=5>

### Caterpillar Inc Stock (CAT) Moved Down by 3.98% on Nov 20: Facts Behind the Movement
- Summary: Recent price drop reflects market concerns.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQQW41UkRQQ1VSNnl0bk9DTy0taE15dHhFM091YUtCaVpOVFFYTlZrVnVtUUpvOGt6VTB6STRySXRxZkZhNFN5SFFUQ3BzVVp3RXp0c2RkdV9PYXBhWHVZLU0wX01NQm8xWjdmMUl0RjFvVjFzc1gzSjJpZC13MzJ0N21ydzJhYWtteXc?oc=5>

### Caterpillar Inc Stock (CAT) Moved Down by 3.78% on Nov 19: Key Drivers Unveiled
- Summary: Stock fell 3.78% on Nov 19, indicating short‑term market pressure.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPc2xYTFJOZTF3OEgwMnE4aDRua0FBRjN6R2JKTC1YMk1VMUp4R013WjBMX0dNdXNqN3o2NkpYekliMkpwbm42S3hQNlBaY0oxZGxaLVRHZjFPRlN4N2lBVlpoeWlkSFZ4cEgyTHVxZVMtTFE4aG9CNDRwbkNJQjZ5MnAxeUl0b19YNnc?oc=5>

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CAT** | **21.22** | **11.52** | **16.84** | **17.30** | **247,389,143,040.00 USD** | **-2.57** |
| DE | 34.12 | 5.91 | 25.95 | 4.90 | 165,485,297,664.00 USD | 27.41 |
| CNH | 52.38 | 1.75 | 34.97 | -1.00 | 17,664,311,296.00 USD | 16.30 |
| CMI | 17.31 | 4.27 | 11.53 | 13.50 | 56,831,709,184.00 USD | -13.25 |

Peers fetched as_of: 2026-11-24; CAT reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

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

- https://news.google.com/rss/articles/CBMizAFBVV95cUxPWjhrRnNibVBhd2ZacnVub2lLbVkxSGxDNjU1REtEUXJNTzgwaXJrVnNSb09sUmIzaE5OUW9oS3FZNGpQX2otQnhpQ0czNC1UZ19vLXJCZTRGZUNKRlpSNkZIN1NKME03eXg4UTNRSkY1MzdjZy0yUWlmX2VHa2dTV0xIX2FndEZXejVxM21FOWhoQkRfTjBYbWRCRE1LeGZ4YjFZOFdwQlVNX29Ga1RxUWpJYVM3b3pWa0ZhakZMZ1JxQkQ2VXRTc25zRE3SAdIBQVVfeXFMTnFxVkRVVDRwVDNsalZMSWlFcVpIdXBDYWhURktwWkxPbnh4RG1mb2s3RzBud0VkUkw1TnY5aG1MMjBOUHVqaE9UUE1wTDNfU21PYzltbHJYZlZIVXg2TkUzejI1VzNlNlJtU2d0bWZTcGNfZ0NNeExHMUJNYVpOOHRldzgybFZ5S3ZzVXlQYWpjc1ZRT0wwZG5KUG1lNWtRNVkxTVFRaHd4VzlzM0QtTERJWE42M3U0cTNtSjZHTm1PUGJDVzBBdVZLSC1oWE85VElR?oc=5
- https://news.google.com/rss/articles/CBMi5wFBVV95cUxOUFRvOXhUU0hwYWpwMUNJUkRnM1ZscUpEb1FWT05fT0I1SlJNb1BIRkpDR0lqOS1jRUJvM2xNbVllZHB6NUdvbEFmT1FKYWUwUUItZUJJQm9SbTZHNGRLTmVYYzBVR2JJSjRESVoxM1R6ZzNaMlFseUJmQUJraTc0M1VBOFcyLXkxdFE2NEF1SmRHLVZQNnZZcWRQZHZUX0ZnYUZXRDRVMHFORENhZThyd3NBNE4xOVE5TDFTZlZmb1E3Vzd5Q2owWUFBU3JKOFlUYkY1c3J3SVI5YU5BNnJmWHROcGVpbDA?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQQW41UkRQQ1VSNnl0bk9DTy0taE15dHhFM091YUtCaVpOVFFYTlZrVnVtUUpvOGt6VTB6STRySXRxZkZhNFN5SFFUQ3BzVVp3RXp0c2RkdV9PYXBhWHVZLU0wX01NQm8xWjdmMUl0RjFvVjFzc1gzSjJpZC13MzJ0N21ydzJhYWtteXc?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPc2xYTFJOZTF3OEgwMnE4aDRua0FBRjN6R2JKTC1YMk1VMUp4R013WjBMX0dNdXNqN3o2NkpYekliMkpwbm42S3hQNlBaY0oxZGxaLVRHZjFPRlN4N2lBVlpoeWlkSFZ4cEgyTHVxZVMtTFE4aG9CNDRwbkNJQjZ5MnAxeUl0b19YNnc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
