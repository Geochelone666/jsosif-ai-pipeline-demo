# EW Intelligence Report

- ticker: **EW**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/EW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/EW/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:39:40.311784+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 7, 'rule': 1, 'ai': 2, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/EW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 7 unique headlines; 6 named publishers; 0 exact duplicates; 7 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-11-15

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 103.8800 |
| Return 1D (%) | -1.2829 |
| Return 1W (%) | -1.8148 |
| Return 1M (%) | 19.1011 |
| Return YTD (%) | 21.8534 |
| Return 1Y (%) | 20.7626 |
| Annualized volatility (%) | 25.5202 |
| Beta vs SPY | 0.5380 |
| Max drawdown (%) | -13.1855 |
| Sharpe (rf=0) | 0.8693 |
| Downside deviation (rf=0, %) | 16.8878 |
| Sortino (rf=0) | 1.3136 |
| Historical VaR 95% (1D, %) | 2.5317 |
| Historical ES 95% (1D, %) | 3.1155 |
| Correlation vs SPY | 0.2930 |
| Tracking error vs SPY (%) | 25.2309 |
| P/E (trailing) | 60.40 |
| P/B | 5.51 |
| EV/EBITDA | 26.68 |
| Revenue growth (%) | 10.50 |
| Forward P/E (estimate) | 30.68 |
| Gross margin (%) | 78.02 |
| Operating margin (%) | 28.82 |
| Return on equity (%) | 9.33 |
| Free cash flow yield (%) | 1.92 |
| MA50 | 91.8658 |
| Close vs MA50 (%) | 13.0780 |
| MA200 | 86.8138 |
| Close vs MA200 (%) | 19.6585 |
| RSI (14, Wilder) | 66.5467 |
| MACD (12,26) | 4.4194 |
| MACD signal (9) | 4.2317 |
| MACD histogram | 0.1877 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'EW': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 103.8800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.2829 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.8148 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 19.1011 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 21.8534 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 20.7626 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.5202 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.8878 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3136 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5317 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.1155 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2930 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 25.2309 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5380 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.1855 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8693 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 30.6756 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 78.0180 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 28.8180 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.3330 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.9175 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 60.3953 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 66.5467 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1877 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 13.0780 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 19.6585 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Edwards Lifesciences Enters New $750 Million Revolving Credit Agreement
- Summary: Edwards Lifesciences Enters New $750 Million Revolving Credit Agreement
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxNa2FrS0JZX1B6MjlwUzdlNVZSeEdhQnpBSk80eXQzcEV2R29PajJ2ZnRyWC1yM19TM0Q4N2JINGdVT21MWEVmOWlPWG9DNG9vb25Gam9aMnFTanFOTWVuOWJNcHl5b1k1NlR2dGVQTk12b1M3UGh2Nmk5TDRaRnNpc2cyaEFIODd1WFo4OGlkNEtTY05qNVlFMEJaM3V0N2lDbDAyeUJnUG9XRkdKUUN6UVUzNDhvQ1pyOVAwN2MtUQ?oc=5>

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
| **EW** | **60.40** | **5.51** | **26.68** | **10.50** | **59,730,997,248.00 USD** | **20.76** |
| MDT | 24.72 | 2.56 | 14.30 | 13.70 | 128,694,067,200.00 USD | 3.59 |
| BSX | 18.45 | 2.43 | 13.27 | 1.40 | 62,312,857,600.00 USD | -55.68 |
| ABT | 38.76 | 3.53 | 18.12 | 14.50 | 179,896,778,752.00 USD | -15.62 |

Peers fetched as_of: 2026-11-19; EW reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

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

- https://news.google.com/rss/articles/CBMivwFBVV95cUxNa2FrS0JZX1B6MjlwUzdlNVZSeEdhQnpBSk80eXQzcEV2R29PajJ2ZnRyWC1yM19TM0Q4N2JINGdVT21MWEVmOWlPWG9DNG9vb25Gam9aMnFTanFOTWVuOWJNcHl5b1k1NlR2dGVQTk12b1M3UGh2Nmk5TDRaRnNpc2cyaEFIODd1WFo4OGlkNEtTY05qNVlFMEJaM3V0N2lDbDAyeUJnUG9XRkdKUUN6UVUzNDhvQ1pyOVAwN2MtUQ?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPR3FnYUhYaXBJWTdmS19BQ2lsVVhYRk1TdldtVU1MaDJBeTZua2lYMmZIeFlwQmZWRzdJWHRlb3dWdWk5eEtGQXFXMWNDbWJkeFdMNUo1N1ZOVXlWN2Q4Ri1rRmlVUERsY09wQ0EtdDRGdEJEcDhYYnNRT3BhMzQ1RkNhNW9rRjF6M2kyZF82OVpfQVNMVUIyM0pHWkJyb0FYVG1XQnRWYw?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQLXZyOC1vRDRuLVU2M1Y5YjhEekpMQ0RUSjNjdUlRNTl6QTBLbmJqaTZuTkI1UkxxUlBsR3ZOVUEtdzVHX3RrbUJJeHY3YW9rUTBMUWtlekUxQlhxQlhOc0NYUXRKcmRfWk9CRVJ1UVNFSnpib3BHZnh2UDNGdkFGbWV4clA2c3FNMlR0V0RVXzJxUHFrS0M0OUZadkNHczdScDdRWmhISVVRWVAwM2ZKVmNhWWNaam05cnA1aE9pc002V2U4bmp0UlBzVjFLRTJJbHhN0gHYAUFVX3lxTE9JVjVLYTFHV0F2RmtzQ05UQkl1SDNLU2JTUkZtbTAyYUtiTHM5OUViSzhtQS1NVkVfb052cHFqZFBvTkdCQ3ZCMGt3cXpVV1d3czZiaTBRUXBhc3lHNWI3N1VseTNIeTJQMm9iQ1lUbDFfM3R3MVNRWTBtak5rTlNPV3RXSXJaMHZCamN2VlRqVWIzRlhJVUJacDlRckVhUy02Q1hzSE9udEZ4OWxXbzFidnFTcHFJa2V5X01vR0YweW43b0pvdi1xdFp3dklzTGJhaEZ5V1poag?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
