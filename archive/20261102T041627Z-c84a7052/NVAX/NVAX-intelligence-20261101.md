# NVAX Intelligence Report

- ticker: **NVAX**
- Report as_of: **2026-11-01**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/NVAX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVAX/key-statistics/
- AI analysis snapshot as_of: **2026-11-01**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-02T04:27:02.164044+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 10, 'rule': 1, 'ai': 3, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261101T014405Z-e49d1192/NVAX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 10 unique headlines; 8 named publishers; 1 exact duplicates; 10 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-10-26

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

### Novavax Stock Hits Over 1-Year High: Is Sanofi’s Flu-COVID Shot The Post-Pandemic Growth Driver?
- Summary: Novavax shares rise to a 1‑year high amid speculation that Sanofi’s new shot could drive post‑pandemic growth.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxPc0dRbnFaVW1wbHhjVTZvSHg4dm4wMjQ0RTloZEhsd1g4VllaTzgtejJNZ2M5QnlIZkpyNGlYM3ZkM2JiQzNMMnRKYk9OVWhwUkMxOWhabGlEVDFGTG9ER2FFQURqcmllRDQ4aDdyN2h2T09sSklrWmMwa0xiTDIyZVNyQ3NBLWVBd3ZZc3hNaVFvcTY2UTZia09xbHhiY0FQVUNsbVRWelhjeGpXdktmWk0yNG5mMkY1SDlYbUlNblhOX0ZOQVVvazhqak9IeXpOeGZScmFLRXRMUUdabDAtQ2lLcw?oc=5>

## HEADWINDS

### Novavax (NVAX) Stock Falls Amid Market Uptick: What Investors Need to Know
- Summary: Novavax (NVAX) Stock Falls Amid Market Uptick: What Investors Need to Know
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOX01Na1ozU085VFhKMlVzUndqOEVXdURuYTh0b2djRU9vc2VybXJfa1F6SGZjcUh1YnJMdkVHMmVXbDFtc09nN1FleTUtYWxpSHU0SERIOFpTUV91ZFlqNnBoaXNHWWg3ZUlrTHhNZjY1LVpBVVJfVExocVBLbDduY2I4aWozeDdMd2U5emxmMzRHcDZpcW1MZUpB?oc=5>

## CATALYSTS

### Novavax (NVAX) Stock May Be Above Fair Value On Current Sales
- Summary: Analysts suggest NVAX shares could be overvalued based on current sales figures, indicating potential upside for investors.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxNVWgwRkM2TVg1VGtZb1pPRVR6Z2V4V1hfQkpjbmVqZlV6OTZpeUM3SERlYkMzZWtZMDRzZkhkMmxydTVnTlgySnVBbTVxbEpGdkpIX0tvU2FNN05jdzFSNXhPNk5aanhDSkJYSDhjc1ZCRVp2MHhCbEZIbDllUDdydEMtSE5EZmNkM3JMVGcxWURndVdTcTJTaGlpSk1pd0hKQUc1Yl9fcWwxemZhZ0trY0ZNODM3MnNTRzNINmtLOUo4RFlJSlhLRlpVdFBKNWpNZ0lZd1h6QdIB3AFBVV95cUxQR3RjS1M0LWdXY0x4Qy1uN1VRWnBncVBOVVNzQTk3c3JvdVNQVlhISjNPNWRPSmY2bzZxS1JhVnNKeFJwekZDbXdLMVpVYVlpZEh1Ymc3U1lvaFZlVk9kaUpTekctLVVkeGQxdkpJVmNNa2pmMHQzU3pMQUJaWW9YRGRUSnpOMzAtLVdFYzdlTEYwTXZwSG1BYXJSN2NhUDBCYl9oUktMdHQ0dFVwakRYS29MN21FOUNRblp0UnRRY3dUOUNMQkMtXy05dEVaNDFkWVVGRDVYV1RwZE5M?oc=5>

### A flu-COVID vaccine trial in people 60 and older brings Novavax $125 million
- Summary: Novavax reports $125 million from a flu-COVID vaccine trial targeting seniors, indicating progress in product development and potential revenue boost.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPemwxNE1GcXZ2cDRpVHFXbXNvb0hTd2lZUlZLc0dpZlBDUmNEeXFHZVdUNjJyU2J1MVlMXzY3THZhei11azhCY0dvS3ZZNVU4ZHEzSFRNc2lCdmhiSDFod1JsTzZjckpueVp6ZVRKWU5WcFNKaGRyMUx2NnpVMEZRUGdWOURGdF95OGtIZmQ3d2lTVVM0SWNPY2ZZVWp3Y2FOWkVLTW5QZ0N4bFMwSWY0ZHcza1RtbTFy?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVAX** | **N/A** | **-8.71** | **-12.22** | **-76.30** | **1,662,652,928.00 USD** | **19.57** |
| MRNA | N/A | 13.08 | -38.57 | 2.10 | 88,518,582,272.00 USD | 687.92 |
| BNTX | N/A | 1.11 | -6.52 | -59.50 | 22,148,687,872.00 USD | -15.76 |
| GSK | 17.25 | 3.95 | 10.80 | 4.00 | 99,194,036,224.00 USD | 9.21 |

Peers fetched as_of: 2026-11-01; NVAX reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-06
- Next expected earnings: 2026-11-05 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-01

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

- https://news.google.com/rss/articles/CBMi4wFBVV95cUxPc0dRbnFaVW1wbHhjVTZvSHg4dm4wMjQ0RTloZEhsd1g4VllaTzgtejJNZ2M5QnlIZkpyNGlYM3ZkM2JiQzNMMnRKYk9OVWhwUkMxOWhabGlEVDFGTG9ER2FFQURqcmllRDQ4aDdyN2h2T09sSklrWmMwa0xiTDIyZVNyQ3NBLWVBd3ZZc3hNaVFvcTY2UTZia09xbHhiY0FQVUNsbVRWelhjeGpXdktmWk0yNG5mMkY1SDlYbUlNblhOX0ZOQVVvazhqak9IeXpOeGZScmFLRXRMUUdabDAtQ2lLcw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOX01Na1ozU085VFhKMlVzUndqOEVXdURuYTh0b2djRU9vc2VybXJfa1F6SGZjcUh1YnJMdkVHMmVXbDFtc09nN1FleTUtYWxpSHU0SERIOFpTUV91ZFlqNnBoaXNHWWg3ZUlrTHhNZjY1LVpBVVJfVExocVBLbDduY2I4aWozeDdMd2U5emxmMzRHcDZpcW1MZUpB?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxNVWgwRkM2TVg1VGtZb1pPRVR6Z2V4V1hfQkpjbmVqZlV6OTZpeUM3SERlYkMzZWtZMDRzZkhkMmxydTVnTlgySnVBbTVxbEpGdkpIX0tvU2FNN05jdzFSNXhPNk5aanhDSkJYSDhjc1ZCRVp2MHhCbEZIbDllUDdydEMtSE5EZmNkM3JMVGcxWURndVdTcTJTaGlpSk1pd0hKQUc1Yl9fcWwxemZhZ0trY0ZNODM3MnNTRzNINmtLOUo4RFlJSlhLRlpVdFBKNWpNZ0lZd1h6QdIB3AFBVV95cUxQR3RjS1M0LWdXY0x4Qy1uN1VRWnBncVBOVVNzQTk3c3JvdVNQVlhISjNPNWRPSmY2bzZxS1JhVnNKeFJwekZDbXdLMVpVYVlpZEh1Ymc3U1lvaFZlVk9kaUpTekctLVVkeGQxdkpJVmNNa2pmMHQzU3pMQUJaWW9YRGRUSnpOMzAtLVdFYzdlTEYwTXZwSG1BYXJSN2NhUDBCYl9oUktMdHQ0dFVwakRYS29MN21FOUNRblp0UnRRY3dUOUNMQkMtXy05dEVaNDFkWVVGRDVYV1RwZE5M?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPemwxNE1GcXZ2cDRpVHFXbXNvb0hTd2lZUlZLc0dpZlBDUmNEeXFHZVdUNjJyU2J1MVlMXzY3THZhei11azhCY0dvS3ZZNVU4ZHEzSFRNc2lCdmhiSDFod1JsTzZjckpueVp6ZVRKWU5WcFNKaGRyMUx2NnpVMEZRUGdWOURGdF95OGtIZmQ3d2lTVVM0SWNPY2ZZVWp3Y2FOWkVLTW5QZ0N4bFMwSWY0ZHcza1RtbTFy?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
