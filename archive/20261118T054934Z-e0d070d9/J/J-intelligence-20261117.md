# J Intelligence Report

- ticker: **J**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/J/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/J/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:17:04.233354+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 0, 'ai': 3, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/J** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 4 named publishers; 0 exact duplicates; 9 HTTPS source links; largest publisher share 66.67%; oldest publication 2026-11-12

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 158.2300 |
| Return 1D (%) | -0.9949 |
| Return 1W (%) | 0.7129 |
| Return 1M (%) | 12.1562 |
| Return YTD (%) | 20.4368 |
| Return 1Y (%) | 6.1928 |
| Annualized volatility (%) | 34.0331 |
| Beta vs SPY | 0.8412 |
| Max drawdown (%) | -28.8516 |
| Sharpe (rf=0) | 0.3490 |
| Downside deviation (rf=0, %) | 25.3445 |
| Sortino (rf=0) | 0.4686 |
| Historical VaR 95% (1D, %) | 3.0531 |
| Historical ES 95% (1D, %) | 5.4729 |
| Correlation vs SPY | 0.3406 |
| Tracking error vs SPY (%) | 32.0728 |
| P/E (trailing) | 53.10 |
| P/B | 5.68 |
| EV/EBITDA | 20.24 |
| Revenue growth (%) | 34.50 |
| Forward P/E (estimate) | 19.21 |
| Gross margin (%) | 22.07 |
| Operating margin (%) | 5.93 |
| Return on equity (%) | 8.00 |
| Free cash flow yield (%) | 3.49 |
| MA50 | 145.6134 |
| Close vs MA50 (%) | 8.6644 |
| MA200 | 134.5721 |
| Close vs MA200 (%) | 17.5801 |
| RSI (14, Wilder) | 61.1913 |
| MACD (12,26) | 3.9944 |
| MACD signal (9) | 3.7660 |
| MACD histogram | 0.2284 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'J': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 158.2300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.9949 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.7129 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 12.1562 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 20.4368 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 6.1928 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.0331 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.3445 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4686 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0531 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.4729 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3406 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.0728 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8412 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8516 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3490 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 19.2099 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 22.0670 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 5.9290 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 7.9980 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.4866 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 53.0973 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 61.1913 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2284 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 8.6644 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 17.5801 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Jacobs Strengthens Its Aviation Portfolio With Cochin Airport Plan
- Summary: Jacobs expands aviation portfolio via Cochin Airport project, signaling growth potential.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPanVvSXhLUWNDM3Q2Qk81bGV6TDdRTmNWb1hqa2I3Tkt6YmUyOVR5ZVY4MFc1R1JVOTc4UE5ZNG9tRHdId2ozeEVpSEtMYkZxbS0zTXNuU2h5TlNpN3h3WENJbF9abFpIdFlGMm9rQjd4RUt2enF3SkNuQlhNdTRLdnZnTzB5RlhOUi1senFIbFFCMWR2UWoxWkt6NDV2VWZubm5QUzN5bmM?oc=5>

### Stock awards vest at 140.3% and 200% of initial amounts for Jacobs Solutions (J) legal chief.
- Summary: Legal chief’s stock awards vest at 140.3% and 200% of initial amounts, boosting compensation.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNRV9MQ2RCVlBBMWhJVGtSZ1BJWkRfbFNZbjFXOTM5WTVFUFhaa1dlR0Eybk50TXN3VThEY0cxZm1ZWWdyd3U0V2RqYTZLWWtkZkZtdEZyODZ3Q2s1YVFvY0JXbXN2LVZacURnRFptQVhIOWV0am9waExiXzlFak9SUWJma2ZTa284QUUwRi1GLUs4VHBQc0xEczhnT3hhLVlqLUlSSm1XcGRrckZYN3dvQw?oc=5>

### Jacobs Solutions (J) CFO's performance awards vest at 140.3% and 200% of initial units.
- Summary: Jacobs Solutions CFO’s performance awards vest at 140.3% and 200% of initial units, indicating a significant compensation event.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQeC1ra2NuSTBkdnhUWnZCaE9OdjZZNVREQ1R6Ql9Hc3FZdFhRWGt0UEVBZkYzTTVjOFJOY3htQTY1OTduS1NrWHJrZnFBOHJMeVVzNlhCRHJWUC1aNDdCV0RSSHM2bDMwSzFVVDZQYnJsRVZSWEtISmFubUxzZTlKbmlOTW5heEZsd0hTY0FFekNKTXBmYzAwMlo0QUdPNmFvdXZoQmNwSm9nSFV3UzdUdQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **J** | **53.10** | **5.68** | **20.24** | **34.50** | **18,519,017,472.00 USD** | **6.19** |
| ACM | 25.57 | 4.73 | 12.71 | -14.20 | 10,363,922,432.00 USD | -37.94 |
| FLR | N/A | 2.43 | 10.83 | 10.50 | 6,192,581,632.00 USD | 17.49 |
| KBR | 10.28 | 2.48 | 9.65 | 5.00 | 4,367,154,176.00 USD | -13.16 |

Peers fetched as_of: 2026-11-17; J reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-23 (yfinance; expected dates may change)

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
- Filing date: 2026-08-04
- Revenue (latest available single quarter): 4,142,644,000.00 USD; period 2018-06-30/2018-09-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 136,553,000.00 USD; period 2026-03-28/2026-06-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/52988/000162828026052573/jec-20260626.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPanVvSXhLUWNDM3Q2Qk81bGV6TDdRTmNWb1hqa2I3Tkt6YmUyOVR5ZVY4MFc1R1JVOTc4UE5ZNG9tRHdId2ozeEVpSEtMYkZxbS0zTXNuU2h5TlNpN3h3WENJbF9abFpIdFlGMm9rQjd4RUt2enF3SkNuQlhNdTRLdnZnTzB5RlhOUi1senFIbFFCMWR2UWoxWkt6NDV2VWZubm5QUzN5bmM?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNRV9MQ2RCVlBBMWhJVGtSZ1BJWkRfbFNZbjFXOTM5WTVFUFhaa1dlR0Eybk50TXN3VThEY0cxZm1ZWWdyd3U0V2RqYTZLWWtkZkZtdEZyODZ3Q2s1YVFvY0JXbXN2LVZacURnRFptQVhIOWV0am9waExiXzlFak9SUWJma2ZTa284QUUwRi1GLUs4VHBQc0xEczhnT3hhLVlqLUlSSm1XcGRrckZYN3dvQw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQeC1ra2NuSTBkdnhUWnZCaE9OdjZZNVREQ1R6Ql9Hc3FZdFhRWGt0UEVBZkYzTTVjOFJOY3htQTY1OTduS1NrWHJrZnFBOHJMeVVzNlhCRHJWUC1aNDdCV0RSSHM2bDMwSzFVVDZQYnJsRVZSWEtISmFubUxzZTlKbmlOTW5heEZsd0hTY0FFekNKTXBmYzAwMlo0QUdPNmFvdXZoQmNwSm9nSFV3UzdUdQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
