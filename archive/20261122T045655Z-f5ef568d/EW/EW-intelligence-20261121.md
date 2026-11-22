# EW Intelligence Report

- ticker: **EW**
- Report as_of: **2026-11-21**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/EW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/EW/key-statistics/
- AI analysis snapshot as_of: **2026-11-21**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-22T05:09:07.027691+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 10, 'rule': 1, 'ai': 2, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261121T053104Z-422ce34b/EW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 10 unique headlines; 7 named publishers; 0 exact duplicates; 10 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-14

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 101.8500 |
| Return 1D (%) | -1.9542 |
| Return 1W (%) | -4.9463 |
| Return 1M (%) | 15.3585 |
| Return YTD (%) | 19.4721 |
| Return 1Y (%) | 21.1202 |
| Annualized volatility (%) | 25.4952 |
| Beta vs SPY | 0.5277 |
| Max drawdown (%) | -13.1855 |
| Sharpe (rf=0) | 0.8815 |
| Downside deviation (rf=0, %) | 16.8516 |
| Sortino (rf=0) | 1.3337 |
| Historical VaR 95% (1D, %) | 2.5317 |
| Historical ES 95% (1D, %) | 3.1155 |
| Correlation vs SPY | 0.2959 |
| Tracking error vs SPY (%) | 25.2721 |
| P/E (trailing) | 59.22 |
| P/B | 5.40 |
| EV/EBITDA | 26.12 |
| Revenue growth (%) | 10.50 |
| Forward P/E (estimate) | 30.08 |
| Gross margin (%) | 78.02 |
| Operating margin (%) | 28.82 |
| Return on equity (%) | 9.33 |
| Free cash flow yield (%) | 1.96 |
| MA50 | 92.2154 |
| Close vs MA50 (%) | 10.4479 |
| MA200 | 86.9325 |
| Close vs MA200 (%) | 17.1599 |
| RSI (14, Wilder) | 59.2075 |
| MACD (12,26) | 3.9907 |
| MACD signal (9) | 4.1835 |
| MACD histogram | -0.1928 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'EW': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 101.8500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.9542 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.9463 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 15.3585 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 19.4721 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 21.1202 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.4952 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.8516 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3337 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5317 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.1155 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2959 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 25.2721 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5277 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.1855 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8815 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 30.0761 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 78.0180 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 28.8180 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.3330 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.9557 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 59.2151 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.2075 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1928 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 10.4479 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 17.1599 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Edwards Lifesciences Corporation (EW) - What Are Analysts Saying About This Stock?
- Summary: Edwards Lifesciences Corporation (EW) - What Are Analysts Saying About This Stock?
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxPQ0t1VTRWMnhYM2ZvVURaVHJTTnE3M2N2Y0U5aE5PbHJmaXFuNjVGeDZ3WEpZaTNKSjhhdElnWHFTT1RwRks4Vl8tb0tkWGs5aF9GZzBYWEFVZTBqWnkyS2tZWjhjYXluX3NDcmxHbnFyWmZON1hXYTNNbXNoSXRaamowQ3pCQndkZVFBZUczaFUtb2l6WDZWUG9SOF9TR0dJSUpObGpzS1o5QmdCZDJzbHg1b0kwRzVBeG1pX0VMX0E1LXl3SHduejliekJVZkI4Q0pxSkhMZ2E?oc=5>

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
| **EW** | **59.22** | **5.40** | **26.12** | **10.50** | **58,563,747,840.00 USD** | **21.12** |
| MDT | 24.56 | 2.55 | 14.22 | 13.70 | 127,837,044,736.00 USD | 3.93 |
| BSX | 17.71 | 2.37 | 13.01 | 1.40 | 60,848,885,760.00 USD | -56.54 |
| ABT | 38.43 | 3.50 | 17.99 | 14.50 | 178,389,991,424.00 USD | -14.85 |

Peers fetched as_of: 2026-11-21; EW reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-21

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

- https://news.google.com/rss/articles/CBMi2AFBVV95cUxPQ0t1VTRWMnhYM2ZvVURaVHJTTnE3M2N2Y0U5aE5PbHJmaXFuNjVGeDZ3WEpZaTNKSjhhdElnWHFTT1RwRks4Vl8tb0tkWGs5aF9GZzBYWEFVZTBqWnkyS2tZWjhjYXluX3NDcmxHbnFyWmZON1hXYTNNbXNoSXRaamowQ3pCQndkZVFBZUczaFUtb2l6WDZWUG9SOF9TR0dJSUpObGpzS1o5QmdCZDJzbHg1b0kwRzVBeG1pX0VMX0E1LXl3SHduejliekJVZkI4Q0pxSkhMZ2E?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPR3FnYUhYaXBJWTdmS19BQ2lsVVhYRk1TdldtVU1MaDJBeTZua2lYMmZIeFlwQmZWRzdJWHRlb3dWdWk5eEtGQXFXMWNDbWJkeFdMNUo1N1ZOVXlWN2Q4Ri1rRmlVUERsY09wQ0EtdDRGdEJEcDhYYnNRT3BhMzQ1RkNhNW9rRjF6M2kyZF82OVpfQVNMVUIyM0pHWkJyb0FYVG1XQnRWYw?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQLXZyOC1vRDRuLVU2M1Y5YjhEekpMQ0RUSjNjdUlRNTl6QTBLbmJqaTZuTkI1UkxxUlBsR3ZOVUEtdzVHX3RrbUJJeHY3YW9rUTBMUWtlekUxQlhxQlhOc0NYUXRKcmRfWk9CRVJ1UVNFSnpib3BHZnh2UDNGdkFGbWV4clA2c3FNMlR0V0RVXzJxUHFrS0M0OUZadkNHczdScDdRWmhISVVRWVAwM2ZKVmNhWWNaam05cnA1aE9pc002V2U4bmp0UlBzVjFLRTJJbHhN0gHYAUFVX3lxTE9JVjVLYTFHV0F2RmtzQ05UQkl1SDNLU2JTUkZtbTAyYUtiTHM5OUViSzhtQS1NVkVfb052cHFqZFBvTkdCQ3ZCMGt3cXpVV1d3czZiaTBRUXBhc3lHNWI3N1VseTNIeTJQMm9iQ1lUbDFfM3R3MVNRWTBtak5rTlNPV3RXSXJaMHZCamN2VlRqVWIzRlhJVUJacDlRckVhUy02Q1hzSE9udEZ4OWxXbzFidnFTcHFJa2V5X01vR0YweW43b0pvdi1xdFp3dklzTGJhaEZ5V1poag?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
