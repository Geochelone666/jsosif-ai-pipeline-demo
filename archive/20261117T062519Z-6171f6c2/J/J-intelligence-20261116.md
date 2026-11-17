# J Intelligence Report

- ticker: **J**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/J/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/J/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:31:31.729545+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 5, 'rule': 2, 'ai': 2, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 5 unique headlines; 4 named publishers; 0 exact duplicates; 5 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 159.8200 |
| Return 1D (%) | 1.0049 |
| Return 1W (%) | 2.1932 |
| Return 1M (%) | 13.2832 |
| Return YTD (%) | 21.6470 |
| Return 1Y (%) | 4.6064 |
| Annualized volatility (%) | 34.0852 |
| Beta vs SPY | 0.8403 |
| Max drawdown (%) | -28.8516 |
| Sharpe (rf=0) | 0.3793 |
| Downside deviation (rf=0, %) | 25.3755 |
| Sortino (rf=0) | 0.5094 |
| Historical VaR 95% (1D, %) | 3.0536 |
| Historical ES 95% (1D, %) | 5.4729 |
| Correlation vs SPY | 0.3394 |
| Tracking error vs SPY (%) | 32.1371 |
| P/E (trailing) | 53.10 |
| P/B | 5.73 |
| EV/EBITDA | 20.41 |
| Revenue growth (%) | 34.50 |
| Forward P/E (estimate) | 19.40 |
| Gross margin (%) | 22.07 |
| Operating margin (%) | 5.93 |
| Return on equity (%) | 8.00 |
| Free cash flow yield (%) | 3.45 |
| MA50 | 145.3342 |
| Close vs MA50 (%) | 9.9672 |
| MA200 | 134.4598 |
| Close vs MA200 (%) | 18.8608 |
| RSI (14, Wilder) | 64.5212 |
| MACD (12,26) | 4.0915 |
| MACD signal (9) | 3.7089 |
| MACD histogram | 0.3826 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'J': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 159.8200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.0049 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.1932 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 13.2832 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 21.6470 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.6064 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.0852 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.3755 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5094 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0536 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.4729 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3394 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.1371 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8403 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8516 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3793 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 19.4029 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 22.0670 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 5.9290 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 7.9980 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.4519 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 53.0963 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 64.5212 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3826 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 9.9672 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 18.8608 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Jacobs Solutions (J) Projected to Release Earnings on Monday
- Summary: Jacobs Solutions (J) Projected to Release Earnings on Monday
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPeVp4ZW9YR293WU1UNEdzMV92RmpXemh0am9yQVZaT2Q4S1lERVRnQWFkTkpuU2FIOFdJM0hoMmRsS3p5SHNjRGZ0Ym5SZ3hoVnBxbFowN3k4TVZNMnJJeDBaZDBtcU01c2hLNDZnWkNkNE92dDRUQUU3RTA3T2NreDV0M01vcE5KMHN1XzhJRzB6a0hKb3hYTkIzS2oxNmwtTzdZQ2FqbzgtVWQtTk1OY0FrOGdXcFhaWHZaQ1lR?oc=5>

### Jacobs Solutions Inc. (NYSE:J) Shareholders to Collect $0.36 Quarterly Dividend
- Summary: Jacobs Solutions Inc. (NYSE:J) Shareholders to Collect $0.36 Quarterly Dividend
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQUGotZVRidnM3N3ZRT3dBSmp0YnE4clJ6VDF2d1plMHRaaHF6eTVoWUprZVRVUUJtb1V2Q19JQ0w1MnVWLWJfYUdaV1UyakpxVFdBUEdud0k4NTBxdHV2ck5Bb19WTGVWcUVlSGpKZFQxblROckExMEN4YWlFLW56bEFVb1JvUHVuOFdKTlJSbUxUTE10NGc1cmNmVnhKcnYyUUVudjZHeGg5U1FPQm92UTdyVmo4TXE2RGJocm9OUTBIZjZWXzN1enBUd29xZFlheEdj?oc=5>

### A former strategy adviser who led three companies joins Jacobs’ board Dec. 1.
- Summary: Jacobs appoints a former strategy adviser to its board, potentially enhancing strategic guidance.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQQ2x6WHNRZjV1NzB4emdFUEtURDR0a2xkOUwzVE1sVHVObGRUOTB0UXg1YVYtOFJMTkpRYjZHWng2U1pfeHZJbHVFNTBERGdiOWd2TmpXOF9YSi1HaVN4VXB6c21RR3JVMS1HWElUOXZfRkVpRzExWkFCM0xUdWFlUlRsU1E1S0tNOHRQaU81NFZ2WmpBVmRFZzlyYjd3YXQ3emc?oc=5>

### Jacobs Solutions Appoints Richard Phillips to Board of Directors
- Summary: Jacobs adds Richard Phillips to its board, strengthening governance and expertise.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNTUFicUItZU9rSHBIX3Z2TGtndUhsSklvd2V4T3NBQVd5T09MeWhsOUxFYnVpU0tXZ2ZhV2QwTE1aalB5NXpSM1Mwa1VjTGlETjRzUVg3T3ViTTV6clNxRGE5SHZHb3ZkUV91VnBQQ3pPTkU3Y2JHbHVWbUFORnZlTkE4aHMxR1kwTmZRaVVnbmVodkZDUXRGMGNwUHA3dDNGZl95YmJxMUR5THZtaTFjWHAzVll1SEU?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **J** | **53.10** | **5.73** | **20.41** | **34.50** | **18,705,111,040.00 USD** | **4.61** |
| ACM | 25.53 | 4.25 | 12.71 | -14.20 | 9,330,490,368.00 USD | -44.80 |
| FLR | N/A | 2.44 | 10.86 | 10.50 | 6,202,835,968.00 USD | 14.15 |
| KBR | 10.28 | 2.53 | 9.78 | 5.00 | 4,457,952,256.00 USD | -14.50 |

Peers fetched as_of: 2026-11-16; J reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

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

- https://news.google.com/rss/articles/CBMivgFBVV95cUxPeVp4ZW9YR293WU1UNEdzMV92RmpXemh0am9yQVZaT2Q4S1lERVRnQWFkTkpuU2FIOFdJM0hoMmRsS3p5SHNjRGZ0Ym5SZ3hoVnBxbFowN3k4TVZNMnJJeDBaZDBtcU01c2hLNDZnWkNkNE92dDRUQUU3RTA3T2NreDV0M01vcE5KMHN1XzhJRzB6a0hKb3hYTkIzS2oxNmwtTzdZQ2FqbzgtVWQtTk1OY0FrOGdXcFhaWHZaQ1lR?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQUGotZVRidnM3N3ZRT3dBSmp0YnE4clJ6VDF2d1plMHRaaHF6eTVoWUprZVRVUUJtb1V2Q19JQ0w1MnVWLWJfYUdaV1UyakpxVFdBUEdud0k4NTBxdHV2ck5Bb19WTGVWcUVlSGpKZFQxblROckExMEN4YWlFLW56bEFVb1JvUHVuOFdKTlJSbUxUTE10NGc1cmNmVnhKcnYyUUVudjZHeGg5U1FPQm92UTdyVmo4TXE2RGJocm9OUTBIZjZWXzN1enBUd29xZFlheEdj?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQQ2x6WHNRZjV1NzB4emdFUEtURDR0a2xkOUwzVE1sVHVObGRUOTB0UXg1YVYtOFJMTkpRYjZHWng2U1pfeHZJbHVFNTBERGdiOWd2TmpXOF9YSi1HaVN4VXB6c21RR3JVMS1HWElUOXZfRkVpRzExWkFCM0xUdWFlUlRsU1E1S0tNOHRQaU81NFZ2WmpBVmRFZzlyYjd3YXQ3emc?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNTUFicUItZU9rSHBIX3Z2TGtndUhsSklvd2V4T3NBQVd5T09MeWhsOUxFYnVpU0tXZ2ZhV2QwTE1aalB5NXpSM1Mwa1VjTGlETjRzUVg3T3ViTTV6clNxRGE5SHZHb3ZkUV91VnBQQ3pPTkU3Y2JHbHVWbUFORnZlTkE4aHMxR1kwTmZRaVVnbmVodkZDUXRGMGNwUHA3dDNGZl95YmJxMUR5THZtaTFjWHAzVll1SEU?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
