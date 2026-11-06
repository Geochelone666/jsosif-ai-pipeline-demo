# SPGI Intelligence Report

- ticker: **SPGI**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/SPGI/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SPGI/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:08:08.333326+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 5, 'rule': 1, 'ai': 2, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/SPGI** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 5 unique headlines; 5 named publishers; 0 exact duplicates; 5 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 472.4100 |
| Return 1D (%) | -1.9266 |
| Return 1W (%) | 2.5507 |
| Return 1M (%) | 20.8457 |
| Return YTD (%) | -3.7889 |
| Return 1Y (%) | 1.3434 |
| Annualized volatility (%) | 30.9891 |
| Beta vs SPY | 0.3562 |
| Max drawdown (%) | -28.4781 |
| Sharpe (rf=0) | 0.1997 |
| Downside deviation (rf=0, %) | 23.1023 |
| Sortino (rf=0) | 0.2679 |
| Historical VaR 95% (1D, %) | 2.8749 |
| Historical ES 95% (1D, %) | 4.6345 |
| Correlation vs SPY | 0.1562 |
| Tracking error vs SPY (%) | 31.8352 |
| P/E (trailing) | 28.77 |
| P/B | 6.95 |
| EV/EBITDA | 18.27 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 23.41 |
| Gross margin (%) | 70.99 |
| Operating margin (%) | 48.21 |
| Return on equity (%) | 17.88 |
| Free cash flow yield (%) | 4.41 |
| MA50 | 424.7066 |
| Close vs MA50 (%) | 11.2321 |
| MA200 | 415.1585 |
| Close vs MA200 (%) | 13.7903 |
| RSI (14, Wilder) | 68.0546 |
| MACD (12,26) | 16.3933 |
| MACD signal (9) | 13.1888 |
| MACD histogram | 3.2045 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SPGI': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 472.4100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.9266 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.5507 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 20.8457 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -3.7889 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 1.3434 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.9891 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.1023 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2679 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8749 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6345 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1562 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.8352 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3562 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.4781 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1997 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.4062 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 70.9940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 48.2060 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.8760 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.4095 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 28.7704 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 68.0546 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 3.2045 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 11.2321 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 13.7903 -> Clearly above the moving-average trend level.

## TAILWINDS

### S&P Global Inc (SPGI) Stock Up 3.4% and Still Undervalued -- GF Score: 94/100
- Summary: S&P Global Inc (SPGI) Stock Up 3.4% and Still Undervalued -- GF Score: 94/100
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNY0NSSEM0anBJYWg2TkduT0Q0TmE0cFJlZ0dudUpYNVZaOFdRY1VJd1lWeS1COFROVWdVeE4tMzNwTTdLcUthWFJZVEFjS3JtWXNWUEtmOUFldlhic0dfTW1ZYW5QaWdCWG5ZSGlaX2lNNklCSFdBSm14aXVTNEIzSWtVRDRXLXdGMVhISU1VVzBxX3g2bGZTR2UtcmExaS1VVS13S3pNWGpvQQ?oc=5>

### S&P Global Inc. (SPGI) Remains a Key Player in Financial Markets: Is Its Competitive Edge Underestimated?
- Summary: Highlights SPGI’s strong market position and potential undervaluation.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQd3dFNUo5YTJMdzdlV0pENWgtYTdxNElxU00xdUxfMGZ0WTBMdjJlekR0TEd1VEZXQ1ZFbXJURmlsRGFzS0dsNm1oVzFLM2Z0clpjYmdoRFh6YWVrQjhMNHh3ODdoTHc5ZFBvcHNON254RUtjbHZMTTdFampXU0x5Zm8zVWpyMkZ0ME5yTlZiT0FKc2Va?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### S&P Global (SPGI) Could Be 23% Above Fair Value After Q3 Beat
- Summary: SPGI’s valuation may be 23% above fair value following a Q3 earnings beat, indicating potential upside.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxON1ljWFZSZmFkOW00UjVnNnp5b3pxNXR4VHVmTXpkaDdIQ0VwSmtuY0JqRXBfMVRoWTN0TksxT0pHcHRpak5MVDRJVmRoN3FCeElXS2diNjlkNmpESk5MT2w4N0RKZWpJWHQteV9XSFRWcDR1M0RCUFdKa1pCekg3Z3RfN0c4SkF4MFBEQllGZjl2amt4Y2I5WUN3a3FhSXcxd0xQLUloTEJzbzRXTU13RDZXbzhHcElfeUMwSGxnTmRoSnA2SVN4a1M0V3NJdDh6a2o00gHYAUFVX3lxTE5TaHkxTTk4SzBtdXFaRDZpTVNqMEJEZ0ZhLUpMZU45NHZKV05DMGJUYnV0REdISDE3Uk5NX3Iza3lpZVMxajg0QVVYUDZrbXdaZXhxXzBRYVJSSEFRUGlBdnE4cmZYNmstSE1KaldlYmtpR3phczlVYlhMdEl3NDdyQ2h6Wm5sbUtCRWRLeWE1QUxlWHAyenZWSTVoY0JPdThJR3FnM1JZV01oWEtlUGNNU3IwZmVLLThtS25HbVJab0lNYmMxZmtVWmlpS0tyRGJJN3RyM0ZvUw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SPGI** | **28.77** | **6.95** | **18.27** | **6.80** | **136,951,660,544.00 USD** | **1.34** |
| MCO | 32.23 | 27.19 | 23.46 | 0.80 | 88,857,026,560.00 USD | 6.86 |
| MSCI | 35.67 | -15.59 | 26.52 | 12.40 | 47,684,653,056.00 USD | 16.33 |
| FDS | 23.48 | 6.00 | 14.75 | 6.30 | 12,008,333,312.00 USD | 32.71 |

Peers fetched as_of: 2026-11-05; SPGI reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 1,567,000,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 1,240,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/64040/000006404026000058/spgi-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNY0NSSEM0anBJYWg2TkduT0Q0TmE0cFJlZ0dudUpYNVZaOFdRY1VJd1lWeS1COFROVWdVeE4tMzNwTTdLcUthWFJZVEFjS3JtWXNWUEtmOUFldlhic0dfTW1ZYW5QaWdCWG5ZSGlaX2lNNklCSFdBSm14aXVTNEIzSWtVRDRXLXdGMVhISU1VVzBxX3g2bGZTR2UtcmExaS1VVS13S3pNWGpvQQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQd3dFNUo5YTJMdzdlV0pENWgtYTdxNElxU00xdUxfMGZ0WTBMdjJlekR0TEd1VEZXQ1ZFbXJURmlsRGFzS0dsNm1oVzFLM2Z0clpjYmdoRFh6YWVrQjhMNHh3ODdoTHc5ZFBvcHNON254RUtjbHZMTTdFampXU0x5Zm8zVWpyMkZ0ME5yTlZiT0FKc2Va?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxON1ljWFZSZmFkOW00UjVnNnp5b3pxNXR4VHVmTXpkaDdIQ0VwSmtuY0JqRXBfMVRoWTN0TksxT0pHcHRpak5MVDRJVmRoN3FCeElXS2diNjlkNmpESk5MT2w4N0RKZWpJWHQteV9XSFRWcDR1M0RCUFdKa1pCekg3Z3RfN0c4SkF4MFBEQllGZjl2amt4Y2I5WUN3a3FhSXcxd0xQLUloTEJzbzRXTU13RDZXbzhHcElfeUMwSGxnTmRoSnA2SVN4a1M0V3NJdDh6a2o00gHYAUFVX3lxTE5TaHkxTTk4SzBtdXFaRDZpTVNqMEJEZ0ZhLUpMZU45NHZKV05DMGJUYnV0REdISDE3Uk5NX3Iza3lpZVMxajg0QVVYUDZrbXdaZXhxXzBRYVJSSEFRUGlBdnE4cmZYNmstSE1KaldlYmtpR3phczlVYlhMdEl3NDdyQ2h6Wm5sbUtCRWRLeWE1QUxlWHAyenZWSTVoY0JPdThJR3FnM1JZV01oWEtlUGNNU3IwZmVLLThtS25HbVJab0lNYmMxZmtVWmlpS0tyRGJJN3RyM0ZvUw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
