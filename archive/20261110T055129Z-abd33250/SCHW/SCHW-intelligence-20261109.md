# SCHW Intelligence Report

- ticker: **SCHW**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/SCHW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SCHW/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T06:14:47.347543+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 2, 'ai': 3, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/SCHW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 5 named publishers; 0 exact duplicates; 9 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 92.7300 |
| Return 1D (%) | 1.3553 |
| Return 1W (%) | 4.5316 |
| Return 1M (%) | -4.1055 |
| Return YTD (%) | -6.2663 |
| Return 1Y (%) | -1.3910 |
| Annualized volatility (%) | 25.9743 |
| Beta vs SPY | 0.4564 |
| Max drawdown (%) | -22.5253 |
| Sharpe (rf=0) | 0.0625 |
| Downside deviation (rf=0, %) | 19.7544 |
| Sortino (rf=0) | 0.0822 |
| Historical VaR 95% (1D, %) | 2.5536 |
| Historical ES 95% (1D, %) | 3.9505 |
| Correlation vs SPY | 0.2406 |
| Tracking error vs SPY (%) | 26.2870 |
| P/E (trailing) | 15.85 |
| P/B | 3.54 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 16.90 |
| Forward P/E (estimate) | 11.88 |
| Gross margin (%) | 97.51 |
| Operating margin (%) | 52.80 |
| Return on equity (%) | 21.11 |
| Free cash flow yield (%) | N/A |
| MA50 | 98.1406 |
| Close vs MA50 (%) | -5.5131 |
| MA200 | 96.8845 |
| Close vs MA200 (%) | -4.2880 |
| RSI (14, Wilder) | 48.2447 |
| MACD (12,26) | -1.7551 |
| MACD signal (9) | -2.5136 |
| MACD histogram | 0.7584 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SCHW': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 92.7300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.3553 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.5316 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -4.1055 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -6.2663 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -1.3910 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.9743 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.7544 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.0822 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5536 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9505 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2406 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.2870 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4564 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -22.5253 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0625 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.8837 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.5060 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 52.7960 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 21.1130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.8513 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.2447 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7584 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.5131 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -4.2880 -> Slightly below the moving-average trend level.

## TAILWINDS

### Eligible Charles Schwab clients can now trade five cryptocurrencies
- Summary: Schwab expands crypto trading to clients.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOOUxpUDlrMFpvVk5xR1daQ0NpWW1ybHZISEhBdHBEQXQ2b3BRc0FMWlFsbDBTWTZVYzhUaU1sdC1WUDkxTjhkdWFfc1dZYS14ZUtMd1hCNFdFNW9FLUFCT3IxaFZLU2FjM3VSWDU3U2UtZkZNZjNpY2Zna09rYzBfT3A5cG16cjVsVDBlY05PNXhpR2dHY2tfYjJma1RzQ2ZpeS1aR2pUTlQxaEJma0pEb3BpcmU2TFUwZFJj?oc=5>

## HEADWINDS

### Charles Schwab (SCHW) co-chairman sells 11,675 shares; his trust retains 53.3M.
- Summary: Insider sale of shares by co-chairman.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNWnZLUG1QS3A2UTJDVG9DeGJBS0RicHBlbUtlOFIxVTdzVHh5Z21vQzNoeWZPb3lnOHQtZ2VsRnRRdV9zdXlCZWFRbHpRTFV1REFfNEZQT1dPdmVvWjU0S3p2VGpVRWN1RXpPUU5TTklBNkNhRWFfZ1Nqd01LWThwMmc0ODk2NzBrcEo3VG9SRXhXNmhIbFhnWHRVRWd4N05kb2hjS0tmNTZkaHhUQ1FpdWxvQQ?oc=5>

## CATALYSTS

### Charles Schwab Stock: Analyst Estimates & Ratings
- Summary: Charles Schwab Stock: Analyst Estimates & Ratings
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPRm4td3hlLWZLcmNzT3ctaXJMbjhiX3BQX003dm1mQ0F6dXdySGJmZUhZUjVNR3U5VE9MZDFoQUFyYlUzN2cwZmR0NUdIaGh6RDBMeWlTdVFPQllDY19pZERlR0tHQUQ0UzZUTUp2MENqUWZnWGNNLV91TUlodDQzSURaamZtVFZoSGkxZUlGTUJvSWdwNm1aYjJoQTg3bUVIN3JubjZB?oc=5>

### Charles Schwab Corporation (NYSE:SCHW) Stock Analysis — Earnings Recovery and Technical Divergence
- Summary: Charles Schwab Corporation (NYSE:SCHW) Stock Analysis — Earnings Recovery and Technical Divergence
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxNQ2FDcEdQZy1tQS1ubHA2U1JIcHFleEh1X0dJcC1FWkZLaGRia2l2U2FZcE0xNHVlc19NdmJETmliaGZBemRUTzRuc3dNWHM4UVVhTWdFUlZhRDYxTV80S21Fc2N0UDRFRF9wOEYzT0lYUVBsWEQwbThpSzNuNVJGU1pzdk9zZFJRZVh4RjlyWjBCbHVNeXVKZHBLY1ZPeGZSTUFueDdhOVBZM2l6eU1wVDd5aWRSclZCbzBzX2cybUpTXzBXUmlXQXU4VkllaDVTX3c?oc=5>

### Schwab Q4 Retail Client Sentiment Report: Investors Turn More Bearish on the U.S. Stock Market but Confidence in Reaching Financial Goals Remains High
- Summary: Schwab releases Q4 client sentiment report showing increased bearishness but stable confidence in financial goals.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNYjhaYWtzaXZtSThOdXoxSDUxNklBU1dCWTJ3Smo5d0RXYmFNem16S1lUUm1VSWt3b1ZVYjFVZ2tBYjlQUUxSNHVWeXdoNUZVZkxTNTJJdUpHMDhOeXp3TWx6OElDcnA1MGJSd1lvVGk0X3ViUGlmclNHSlBFWlB3RWZObGNJOTVaNWlDbnVtOHlEdm5SOVpyYTBXcEhaU2s?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SCHW** | **15.85** | **3.54** | **N/A** | **16.90** | **160,052,690,944.00 USD** | **-1.39** |
| IBKR | 29.61 | 5.66 | N/A | 13.50 | 132,166,959,104.00 USD | 10.43 |
| HOOD | 38.40 | 7.51 | N/A | 11.80 | 75,028,930,560.00 USD | -36.08 |
| LPLA | 17.51 | 4.12 | N/A | 17.80 | 23,788,021,760.00 USD | -17.91 |

Peers fetched as_of: 2026-11-09; SCHW reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-06
- Revenue (latest available single quarter): 7,171,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,906,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/316709/000031670926000038/schw-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOOUxpUDlrMFpvVk5xR1daQ0NpWW1ybHZISEhBdHBEQXQ2b3BRc0FMWlFsbDBTWTZVYzhUaU1sdC1WUDkxTjhkdWFfc1dZYS14ZUtMd1hCNFdFNW9FLUFCT3IxaFZLU2FjM3VSWDU3U2UtZkZNZjNpY2Zna09rYzBfT3A5cG16cjVsVDBlY05PNXhpR2dHY2tfYjJma1RzQ2ZpeS1aR2pUTlQxaEJma0pEb3BpcmU2TFUwZFJj?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxNWnZLUG1QS3A2UTJDVG9DeGJBS0RicHBlbUtlOFIxVTdzVHh5Z21vQzNoeWZPb3lnOHQtZ2VsRnRRdV9zdXlCZWFRbHpRTFV1REFfNEZQT1dPdmVvWjU0S3p2VGpVRWN1RXpPUU5TTklBNkNhRWFfZ1Nqd01LWThwMmc0ODk2NzBrcEo3VG9SRXhXNmhIbFhnWHRVRWd4N05kb2hjS0tmNTZkaHhUQ1FpdWxvQQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPRm4td3hlLWZLcmNzT3ctaXJMbjhiX3BQX003dm1mQ0F6dXdySGJmZUhZUjVNR3U5VE9MZDFoQUFyYlUzN2cwZmR0NUdIaGh6RDBMeWlTdVFPQllDY19pZERlR0tHQUQ0UzZUTUp2MENqUWZnWGNNLV91TUlodDQzSURaamZtVFZoSGkxZUlGTUJvSWdwNm1aYjJoQTg3bUVIN3JubjZB?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxNQ2FDcEdQZy1tQS1ubHA2U1JIcHFleEh1X0dJcC1FWkZLaGRia2l2U2FZcE0xNHVlc19NdmJETmliaGZBemRUTzRuc3dNWHM4UVVhTWdFUlZhRDYxTV80S21Fc2N0UDRFRF9wOEYzT0lYUVBsWEQwbThpSzNuNVJGU1pzdk9zZFJRZVh4RjlyWjBCbHVNeXVKZHBLY1ZPeGZSTUFueDdhOVBZM2l6eU1wVDd5aWRSclZCbzBzX2cybUpTXzBXUmlXQXU4VkllaDVTX3c?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNYjhaYWtzaXZtSThOdXoxSDUxNklBU1dCWTJ3Smo5d0RXYmFNem16S1lUUm1VSWt3b1ZVYjFVZ2tBYjlQUUxSNHVWeXdoNUZVZkxTNTJJdUpHMDhOeXp3TWx6OElDcnA1MGJSd1lvVGk0X3ViUGlmclNHSlBFWlB3RWZObGNJOTVaNWlDbnVtOHlEdm5SOVpyYTBXcEhaU2s?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
