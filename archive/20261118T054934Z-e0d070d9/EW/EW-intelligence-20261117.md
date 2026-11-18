# EW Intelligence Report

- ticker: **EW**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/EW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/EW/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:15:53.516418+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 3, 'rule': 0, 'ai': 2, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/EW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 3 unique headlines; 2 named publishers; 0 exact duplicates; 3 HTTPS source links; largest publisher share 66.67%; oldest publication 2026-11-14

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 105.4300 |
| Return 1D (%) | -1.5685 |
| Return 1W (%) | 1.3653 |
| Return 1M (%) | 21.7437 |
| Return YTD (%) | 23.6716 |
| Return 1Y (%) | 24.4159 |
| Annualized volatility (%) | 25.5988 |
| Beta vs SPY | 0.5405 |
| Max drawdown (%) | -13.1855 |
| Sharpe (rf=0) | 0.9844 |
| Downside deviation (rf=0, %) | 16.8581 |
| Sortino (rf=0) | 1.4948 |
| Historical VaR 95% (1D, %) | 2.5317 |
| Historical ES 95% (1D, %) | 3.1155 |
| Correlation vs SPY | 0.2910 |
| Tracking error vs SPY (%) | 25.2964 |
| P/E (trailing) | 61.30 |
| P/B | 5.59 |
| EV/EBITDA | 27.11 |
| Revenue growth (%) | 10.50 |
| Forward P/E (estimate) | 31.13 |
| Gross margin (%) | 78.02 |
| Operating margin (%) | 28.82 |
| Return on equity (%) | 9.33 |
| Free cash flow yield (%) | 1.89 |
| MA50 | 91.1426 |
| Close vs MA50 (%) | 15.6759 |
| MA200 | 86.5776 |
| Close vs MA200 (%) | 21.7752 |
| RSI (14, Wilder) | 72.8941 |
| MACD (12,26) | 4.8425 |
| MACD signal (9) | 4.0571 |
| MACD histogram | 0.7855 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'EW': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 105.4300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.5685 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.3653 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 21.7437 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 23.6716 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 24.4159 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.5988 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.8581 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4948 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5317 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.1155 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2910 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 25.2964 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5405 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.1855 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9844 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 31.1333 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 78.0180 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 28.8180 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.3330 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.8893 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 61.2965 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 72.8941 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7855 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 15.6759 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 21.7752 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Are Wall Street Analysts Predicting Edwards Lifesciences Stock Will Climb or Sink?
- Summary: Presents analyst predictions on future price direction of Edwards Lifesciences stock.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPR3FnYUhYaXBJWTdmS19BQ2lsVVhYRk1TdldtVU1MaDJBeTZua2lYMmZIeFlwQmZWRzdJWHRlb3dWdWk5eEtGQXFXMWNDbWJkeFdMNUo1N1ZOVXlWN2Q4Ri1rRmlVUERsY09wQ0EtdDRGdEJEcDhYYnNRT3BhMzQ1RkNhNW9rRjF6M2kyZF82OVpfQVNMVUIyM0pHWkJyb0FYVG1XQnRWYw?oc=5>

### What Edwards Lifesciences (EW) Earnings Beat Means For Shareholders
- Summary: EW reported earnings that surpassed expectations, potentially boosting investor confidence and share value.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQLXZyOC1vRDRuLVU2M1Y5YjhEekpMQ0RUSjNjdUlRNTl6QTBLbmJqaTZuTkI1UkxxUlBsR3ZOVUEtdzVHX3RrbUJJeHY3YW9rUTBMUWtlekUxQlhxQlhOc0NYUXRKcmRfWk9CRVJ1UVNFSnpib3BHZnh2UDNGdkFGbWV4clA2c3FNMlR0V0RVXzJxUHFrS0M0OUZadkNHczdScDdRWmhISVVRWVAwM2ZKVmNhWWNaam05cnA1aE9pc002V2U4bmp0UlBzVjFLRTJJbHhN0gHYAUFVX3lxTE9JVjVLYTFHV0F2RmtzQ05UQkl1SDNLU2JTUkZtbTAyYUtiTHM5OUViSzhtQS1NVkVfb052cHFqZFBvTkdCQ3ZCMGt3cXpVV1d3czZiaTBRUXBhc3lHNWI3N1VseTNIeTJQMm9iQ1lUbDFfM3R3MVNRWTBtak5rTlNPV3RXSXJaMHZCamN2VlRqVWIzRlhJVUJacDlRckVhUy02Q1hzSE9udEZ4OWxXbzFidnFTcHFJa2V5X01vR0YweW43b0pvdi1xdFp3dklzTGJhaEZ5V1poag?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **EW** | **61.30** | **5.59** | **27.11** | **10.50** | **60,622,249,984.00 USD** | **24.42** |
| MDT | 25.14 | 2.61 | 14.51 | 13.70 | 130,881,388,544.00 USD | 9.80 |
| BSX | 18.47 | 2.43 | 13.28 | 1.40 | 62,370,832,384.00 USD | -57.71 |
| ABT | 39.07 | 3.55 | 18.25 | 14.50 | 181,351,612,416.00 USD | -17.47 |

Peers fetched as_of: 2026-11-17; EW reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

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
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,715,500,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 307,500,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1099800/000109980026000054/ew-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipwFBVV95cUxPR3FnYUhYaXBJWTdmS19BQ2lsVVhYRk1TdldtVU1MaDJBeTZua2lYMmZIeFlwQmZWRzdJWHRlb3dWdWk5eEtGQXFXMWNDbWJkeFdMNUo1N1ZOVXlWN2Q4Ri1rRmlVUERsY09wQ0EtdDRGdEJEcDhYYnNRT3BhMzQ1RkNhNW9rRjF6M2kyZF82OVpfQVNMVUIyM0pHWkJyb0FYVG1XQnRWYw?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQLXZyOC1vRDRuLVU2M1Y5YjhEekpMQ0RUSjNjdUlRNTl6QTBLbmJqaTZuTkI1UkxxUlBsR3ZOVUEtdzVHX3RrbUJJeHY3YW9rUTBMUWtlekUxQlhxQlhOc0NYUXRKcmRfWk9CRVJ1UVNFSnpib3BHZnh2UDNGdkFGbWV4clA2c3FNMlR0V0RVXzJxUHFrS0M0OUZadkNHczdScDdRWmhISVVRWVAwM2ZKVmNhWWNaam05cnA1aE9pc002V2U4bmp0UlBzVjFLRTJJbHhN0gHYAUFVX3lxTE9JVjVLYTFHV0F2RmtzQ05UQkl1SDNLU2JTUkZtbTAyYUtiTHM5OUViSzhtQS1NVkVfb052cHFqZFBvTkdCQ3ZCMGt3cXpVV1d3czZiaTBRUXBhc3lHNWI3N1VseTNIeTJQMm9iQ1lUbDFfM3R3MVNRWTBtak5rTlNPV3RXSXJaMHZCamN2VlRqVWIzRlhJVUJacDlRckVhUy02Q1hzSE9udEZ4OWxXbzFidnFTcHFJa2V5X01vR0YweW43b0pvdi1xdFp3dklzTGJhaEZ5V1poag?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
