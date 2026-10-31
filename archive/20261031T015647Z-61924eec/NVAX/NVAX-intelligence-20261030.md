# NVAX Intelligence Report

- ticker: **NVAX**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/NVAX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVAX/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:00:40.830713+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 8, 'rule': 2, 'ai': 3, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/NVAX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 8 unique headlines; 5 named publishers; 0 exact duplicates; 8 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-10-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 10.0800 |
| Return 1D (%) | -3.7249 |
| Return 1W (%) | 3.9175 |
| Return 1M (%) | -6.7530 |
| Return YTD (%) | 50.0000 |
| Return 1Y (%) | 19.5729 |
| Annualized volatility (%) | 70.9906 |
| Beta vs SPY | 2.0200 |
| Max drawdown (%) | -34.5844 |
| Sharpe (rf=0) | 0.5946 |
| Downside deviation (rf=0, %) | 41.7767 |
| Sortino (rf=0) | 1.0105 |
| Historical VaR 95% (1D, %) | 5.9349 |
| Historical ES 95% (1D, %) | 7.7057 |
| Correlation vs SPY | 0.3639 |
| Tracking error vs SPY (%) | 67.3976 |
| P/E (trailing) | N/A |
| P/B | -8.71 |
| EV/EBITDA | -12.22 |
| Revenue growth (%) | -76.30 |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | -2.56 |
| Operating margin (%) | -89.61 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 9.23 |
| MA50 | 10.4596 |
| Close vs MA50 (%) | -3.6292 |
| MA200 | 9.2946 |
| Close vs MA200 (%) | 8.4495 |
| RSI (14, Wilder) | 44.8788 |
| MACD (12,26) | -0.1607 |
| MACD signal (9) | 0.0553 |
| MACD histogram | -0.2160 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVAX': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 10.0800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.7249 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.9175 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -6.7530 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 50.0000 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 19.5729 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 70.9906 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 41.7767 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.0105 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.9349 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.7057 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3639 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 67.3976 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.0200 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -34.5844 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5946 -> Modest risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: -2.5580 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: -89.6080 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.2259 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 44.8788 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2160 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.6292 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 8.4495 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Novavax (NVAX) Stock Falls Amid Market Uptick: What Investors Need to Know
- Summary: Novavax (NVAX) Stock Falls Amid Market Uptick: What Investors Need to Know
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOX01Na1ozU085VFhKMlVzUndqOEVXdURuYTh0b2djRU9vc2VybXJfa1F6SGZjcUh1YnJMdkVHMmVXbDFtc09nN1FleTUtYWxpSHU0SERIOFpTUV91ZFlqNnBoaXNHWWg3ZUlrTHhNZjY1LVpBVVJfVExocVBLbDduY2I4aWozeDdMd2U5emxmMzRHcDZpcW1MZUpB?oc=5>

### Novavax (NVAX) Slips 3.14% to $9.39 as Shares Drift Toward Mid-Range Support - Fast Moving Stocks
- Summary: Novavax (NVAX) Slips 3.14% to $9.39 as Shares Drift Toward Mid-Range Support - Fast Moving Stocks
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxORmVaV2UzRHNFdFAwYzMzckI3ZThuU0wwNDBkejQ3Z0lIcGh5MktWVDhET1dLUFNKUGVqd1liaGxON0cwYUdkNDVEbnFZNWJfSV9tOUQwWmFUc3VNSjIydl82czJ3S2dlR19ib0czdF8tT2h3RFN1ajNrYWdKWngwTm9tQmFJYWY0OUh1LWpLVmxwY2tOLVhlWkI5SVFnd1BPTWEzajBENVJEXzNBRVVuVGxxU1Q?oc=5>

## CATALYSTS

### A flu-COVID vaccine trial in people 60 and older brings Novavax $125 million
- Summary: Novavax reports $125 million from a flu-COVID vaccine trial targeting seniors, indicating progress in product development and potential revenue boost.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPemwxNE1GcXZ2cDRpVHFXbXNvb0hTd2lZUlZLc0dpZlBDUmNEeXFHZVdUNjJyU2J1MVlMXzY3THZhei11azhCY0dvS3ZZNVU4ZHEzSFRNc2lCdmhiSDFod1JsTzZjckpueVp6ZVRKWU5WcFNKaGRyMUx2NnpVMEZRUGdWOURGdF95OGtIZmQ3d2lTVVM0SWNPY2ZZVWp3Y2FOWkVLTW5QZ0N4bFMwSWY0ZHcza1RtbTFy?oc=5>

### How Phase 3 Trial Progress At Novavax (NVAX) Has Changed Its Investment Story
- Summary: Phase 3 trial progress may enhance product prospects.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxQblNIU0JTbHFGRGVvTDhHZHdDeWNoUDAza1oxWXZSUk93ODhKeElxWl9iakZ0NmxWV05VSHlOZXI0NlFCWER0ZU5ZWmNxcXRwWFBheWpJRTl2WkRGNk40TVlaYlMzWC1hVWlSY2tSRWFzenhlUkFfaE1NMWFMQUoyTDVDVEdJbUFQWEoxRWlVOXlxblFwWUFZNG5kUzFMdzEyNl9zRk8tLUxXYmZ4a29tNlBENnQ2NldYNnRiSEtCQ09iZ2JudzBBbGxhZmk0aXliTGJmaEtnWEbSAd4BQVVfeXFMTl9sbGoyQi10S0FwN08ycjNvVG12VFZFdVpGMkkyeFBpUlQzVmh6VUZGd29ENEhhOFVWYkhNU2VNUG42c3BBMGt6c3VHeFlCQmNVV1FIaF94eTFPM01fbTJWWnl3eVBpT0pDOHNUQjV3RU55U3pjSjJkVUV4eE85cHZ6ZXlnVmdRQmphRl9qZEp3MDVMQTl0ZTZQc2JyZHpQUXhGV3NacmlXcjRvQ3plMmFTNHVscXNRWWt4ck4wcWdHZGQ3N0QxNVRXWGdiTFBpSi1mNjU5Q2hVWXFHeC1B?oc=5>

### Is Novavax (NVAX) Fully Priced Relative To Its Sales Base?
- Summary: Valuation analysis relative to sales base.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPVTJVWmlDQ3dOZVFseEU4M3lBZDFzR0hCVzd6SHZRVUs5UFNDTDJkemJfSzdHX29nWC1CTE5KNzRTTjNVODI3bjVrMXpkc1RDUjdEWVV0eVFVYUlDb0JKN1Vld2RIRjdheFZZM3lSMG1FdG9oenJDV2tfQXFxWE85RmQ5WWttdnlFaFRKU2VaXzZwNm1HOUt0djd3X3piVF9a?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVAX** | **N/A** | **-8.71** | **-12.22** | **-76.30** | **1,662,652,928.00 USD** | **19.57** |
| MRNA | N/A | 13.08 | -38.57 | 2.10 | 88,518,582,272.00 USD | 687.92 |
| BNTX | N/A | 1.11 | -6.52 | -59.50 | 22,148,687,872.00 USD | -15.76 |
| GSK | 17.25 | 3.95 | 10.80 | 4.00 | 99,194,036,224.00 USD | 9.21 |

Peers fetched as_of: 2026-10-30; NVAX reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-06
- Next expected earnings: 2026-11-05 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-06
- Revenue (latest available single quarter): 56,698,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): -53,387,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1000694/000100069426000018/nvax-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxOX01Na1ozU085VFhKMlVzUndqOEVXdURuYTh0b2djRU9vc2VybXJfa1F6SGZjcUh1YnJMdkVHMmVXbDFtc09nN1FleTUtYWxpSHU0SERIOFpTUV91ZFlqNnBoaXNHWWg3ZUlrTHhNZjY1LVpBVVJfVExocVBLbDduY2I4aWozeDdMd2U5emxmMzRHcDZpcW1MZUpB?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxORmVaV2UzRHNFdFAwYzMzckI3ZThuU0wwNDBkejQ3Z0lIcGh5MktWVDhET1dLUFNKUGVqd1liaGxON0cwYUdkNDVEbnFZNWJfSV9tOUQwWmFUc3VNSjIydl82czJ3S2dlR19ib0czdF8tT2h3RFN1ajNrYWdKWngwTm9tQmFJYWY0OUh1LWpLVmxwY2tOLVhlWkI5SVFnd1BPTWEzajBENVJEXzNBRVVuVGxxU1Q?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPemwxNE1GcXZ2cDRpVHFXbXNvb0hTd2lZUlZLc0dpZlBDUmNEeXFHZVdUNjJyU2J1MVlMXzY3THZhei11azhCY0dvS3ZZNVU4ZHEzSFRNc2lCdmhiSDFod1JsTzZjckpueVp6ZVRKWU5WcFNKaGRyMUx2NnpVMEZRUGdWOURGdF95OGtIZmQ3d2lTVVM0SWNPY2ZZVWp3Y2FOWkVLTW5QZ0N4bFMwSWY0ZHcza1RtbTFy?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxQblNIU0JTbHFGRGVvTDhHZHdDeWNoUDAza1oxWXZSUk93ODhKeElxWl9iakZ0NmxWV05VSHlOZXI0NlFCWER0ZU5ZWmNxcXRwWFBheWpJRTl2WkRGNk40TVlaYlMzWC1hVWlSY2tSRWFzenhlUkFfaE1NMWFMQUoyTDVDVEdJbUFQWEoxRWlVOXlxblFwWUFZNG5kUzFMdzEyNl9zRk8tLUxXYmZ4a29tNlBENnQ2NldYNnRiSEtCQ09iZ2JudzBBbGxhZmk0aXliTGJmaEtnWEbSAd4BQVVfeXFMTl9sbGoyQi10S0FwN08ycjNvVG12VFZFdVpGMkkyeFBpUlQzVmh6VUZGd29ENEhhOFVWYkhNU2VNUG42c3BBMGt6c3VHeFlCQmNVV1FIaF94eTFPM01fbTJWWnl3eVBpT0pDOHNUQjV3RU55U3pjSjJkVUV4eE85cHZ6ZXlnVmdRQmphRl9qZEp3MDVMQTl0ZTZQc2JyZHpQUXhGV3NacmlXcjRvQ3plMmFTNHVscXNRWWt4ck4wcWdHZGQ3N0QxNVRXWGdiTFBpSi1mNjU5Q2hVWXFHeC1B?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPVTJVWmlDQ3dOZVFseEU4M3lBZDFzR0hCVzd6SHZRVUs5UFNDTDJkemJfSzdHX29nWC1CTE5KNzRTTjNVODI3bjVrMXpkc1RDUjdEWVV0eVFVYUlDb0JKN1Vld2RIRjdheFZZM3lSMG1FdG9oenJDV2tfQXFxWE85RmQ5WWttdnlFaFRKU2VaXzZwNm1HOUt0djd3X3piVF9a?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
