# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-11-15**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-11-15**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-16T04:58:47.376163+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 2, 'ai': 1, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261115T044154Z-6abfba73/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 5 named publishers; 2 exact duplicates; 9 HTTPS source links; largest publisher share 44.44%; oldest publication 2026-11-10

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 145.4400 |
| Return 1D (%) | 2.2353 |
| Return 1W (%) | 2.9008 |
| Return 1M (%) | 14.2498 |
| Return YTD (%) | 4.4226 |
| Return 1Y (%) | 4.3533 |
| Annualized volatility (%) | 21.7122 |
| Beta vs SPY | -0.1975 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | 0.3048 |
| Downside deviation (rf=0, %) | 14.3430 |
| Sortino (rf=0) | 0.4614 |
| Historical VaR 95% (1D, %) | 2.1996 |
| Historical ES 95% (1D, %) | 2.6412 |
| Correlation vs SPY | -0.1240 |
| Tracking error vs SPY (%) | 27.0318 |
| P/E (trailing) | 18.29 |
| P/B | 8.90 |
| EV/EBITDA | 12.47 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 16.87 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.05 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.56 |
| MA50 | 133.6378 |
| Close vs MA50 (%) | 8.8315 |
| MA200 | 143.6922 |
| Close vs MA200 (%) | 1.2164 |
| RSI (14, Wilder) | 66.4506 |
| MACD (12,26) | 3.2624 |
| MACD signal (9) | 2.6366 |
| MACD histogram | 0.6258 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 145.4400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.2353 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.9008 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 14.2498 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 4.4226 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.3533 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.7122 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.3430 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4614 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1996 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6412 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1240 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 27.0318 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1975 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3048 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.8679 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.0460 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.5633 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.2943 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 66.4506 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6258 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 8.8315 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.2164 -> Slightly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### PepsiCo layoffs: 1,000 jobs slashed as North America CEO pushes for soda giant to 'be faster' and 'more capable'
- Summary: PepsiCo layoffs: 1,000 jobs slashed as North America CEO pushes for soda giant to 'be faster' and 'more capable'
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNLVlXZHZ5alpyRzNKbXpRUDVVOE10bVBBZkI2NWdUYWdTTC1WNlppSVR1dzdKWS1NYnljMVpyX1dJLXZ3clZFTmUtWUZYNFdpTnJxT3hXOWxhMXVxU0VmZ2lQcDlFRElFam9iYl9HS3RucEZQZUxFQnh0SlhOSnlxdE5iTEZyNW50aXg4ZTJFV1VYeDVhZXA5MlNrd0k?oc=5>

### PepsiCo ‘to cut 1,000 jobs in North America’
- Summary: PepsiCo announced a reduction of 1,000 jobs in North America, signaling cost-cutting measures amid market pressures.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNdzJ0TGxVVmsxbHhlbE9ORXRvZGVhTF9zZ082aUlBRXluSWwxaHdkSEF1bDRjVjJTa3U0YmxPcDJxeDl0bXNRNVJYbjBuWE5pM1VNc3FzWEsyejUwaWtHMjJQbHJVUG8wME93c0FZRDQ4dTgzd3oxMjZqcTFGU2V5Z0h2bkV6UGI1VlJvLS15LVA?oc=5>

## CATALYSTS

### PepsiCo Stock And Other Dividend Names Worth Watching As Rate Hike Risks Return
- Summary: PepsiCo Stock And Other Dividend Names Worth Watching As Rate Hike Risks Return
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxPRmhNV2g2eE44SW5VOGc3Zi00NHIxdE4yYW81LVJoM3lzcDY1Rk5zTTJYRXZFVUgzZEtfZXJzYnppeGhnbndNd2RYUmhRSldHNkl1NDdEeFo5Y3A1cTlzN3AtZU9neG12dHNIdEtiZU9hZUx2TkxYRVpxQzRieUJuWXRsRmRsQ015akwxUzZSSTI1ckJfbkxncjM3U1UxUWJTd3kyeTluODFlY1F5aTdSWHlYVGdXendzbHpILWdjNFFxbzFWQXlGeTlQMUUtRzg4NWRtc9IB2gFBVV95cUxPMFpnblNGQzlEa25xWU0xNTNFLWVLVDlOYjVVZ2c3dkNyY1B5QjNaNm1CalpBSXJFU1FMVDFvaEUyNkFDckxfYjh2bHFuT3pYMjkycmx5N0ZXWVNEWC1vWmZRZ1FwMlk1Q0hlRms4MGZvOVpzdk5pTGdEQ0txc0xYVjBuQVQ3d19MWnozcHBKTHBLLUxtYVAza3pqUWdET05PTnlxRUNzTUhrcWt3M29yU2o0bk9CVm9lY1ZpU1QxY1F0Tm05czhkZHo3MUZ1c0g3bjJhd1ZHUlFvZw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **18.29** | **8.90** | **12.47** | **5.60** | **198,197,067,776.00 USD** | **4.35** |
| KO | 29.28 | 11.43 | 26.08 | 7.40 | 426,963,795,968.00 USD | 43.36 |
| MNST | 42.24 | 9.24 | 29.32 | 16.70 | 90,946,002,944.00 USD | 30.73 |
| KDP | 32.74 | 1.95 | 16.63 | 70.60 | 49,456,865,280.00 USD | 38.88 |

Peers fetched as_of: 2026-11-15; PEP reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-15

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-08
- Revenue (latest available single quarter): 25,274,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,048,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/77476/000007747626000048/pep-20260905.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinAFBVV95cUxNLVlXZHZ5alpyRzNKbXpRUDVVOE10bVBBZkI2NWdUYWdTTC1WNlppSVR1dzdKWS1NYnljMVpyX1dJLXZ3clZFTmUtWUZYNFdpTnJxT3hXOWxhMXVxU0VmZ2lQcDlFRElFam9iYl9HS3RucEZQZUxFQnh0SlhOSnlxdE5iTEZyNW50aXg4ZTJFV1VYeDVhZXA5MlNrd0k?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNdzJ0TGxVVmsxbHhlbE9ORXRvZGVhTF9zZ082aUlBRXluSWwxaHdkSEF1bDRjVjJTa3U0YmxPcDJxeDl0bXNRNVJYbjBuWE5pM1VNc3FzWEsyejUwaWtHMjJQbHJVUG8wME93c0FZRDQ4dTgzd3oxMjZqcTFGU2V5Z0h2bkV6UGI1VlJvLS15LVA?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxPRmhNV2g2eE44SW5VOGc3Zi00NHIxdE4yYW81LVJoM3lzcDY1Rk5zTTJYRXZFVUgzZEtfZXJzYnppeGhnbndNd2RYUmhRSldHNkl1NDdEeFo5Y3A1cTlzN3AtZU9neG12dHNIdEtiZU9hZUx2TkxYRVpxQzRieUJuWXRsRmRsQ015akwxUzZSSTI1ckJfbkxncjM3U1UxUWJTd3kyeTluODFlY1F5aTdSWHlYVGdXendzbHpILWdjNFFxbzFWQXlGeTlQMUUtRzg4NWRtc9IB2gFBVV95cUxPMFpnblNGQzlEa25xWU0xNTNFLWVLVDlOYjVVZ2c3dkNyY1B5QjNaNm1CalpBSXJFU1FMVDFvaEUyNkFDckxfYjh2bHFuT3pYMjkycmx5N0ZXWVNEWC1vWmZRZ1FwMlk1Q0hlRms4MGZvOVpzdk5pTGdEQ0txc0xYVjBuQVQ3d19MWnozcHBKTHBLLUxtYVAza3pqUWdET05PTnlxRUNzTUhrcWt3M29yU2o0bk9CVm9lY1ZpU1QxY1F0Tm05czhkZHo3MUZ1c0g3bjJhd1ZHUlFvZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
