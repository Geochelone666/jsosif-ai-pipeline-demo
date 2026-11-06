# GIS Intelligence Report

- ticker: **GIS**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/GIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:20:34.763852+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 8, 'rule': 1, 'ai': 5, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/GIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 8 unique headlines; 5 named publishers; 0 exact duplicates; 8 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-10-30

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 36.4600 |
| Return 1D (%) | 1.7015 |
| Return 1W (%) | 9.4238 |
| Return 1M (%) | 17.2761 |
| Return YTD (%) | -16.1818 |
| Return 1Y (%) | -15.9831 |
| Annualized volatility (%) | 30.7524 |
| Beta vs SPY | -0.3643 |
| Max drawdown (%) | -33.2524 |
| Sharpe (rf=0) | -0.4159 |
| Downside deviation (rf=0, %) | 21.3378 |
| Sortino (rf=0) | -0.5994 |
| Historical VaR 95% (1D, %) | 2.9959 |
| Historical ES 95% (1D, %) | 3.8866 |
| Correlation vs SPY | -0.1610 |
| Tracking error vs SPY (%) | 35.5684 |
| P/E (trailing) | N/A |
| P/B | 2.62 |
| EV/EBITDA | 9.57 |
| Revenue growth (%) | -2.80 |
| Forward P/E (estimate) | 11.57 |
| Gross margin (%) | 33.73 |
| Operating margin (%) | 15.24 |
| Return on equity (%) | -10.49 |
| Free cash flow yield (%) | 6.68 |
| MA50 | 34.5838 |
| Close vs MA50 (%) | 5.4251 |
| MA200 | 36.1234 |
| Close vs MA200 (%) | 0.9318 |
| RSI (14, Wilder) | 63.3011 |
| MACD (12,26) | 0.4114 |
| MACD signal (9) | -0.0076 |
| MACD histogram | 0.4190 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GIS': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 36.4600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.7015 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 9.4238 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 17.2761 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -16.1818 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -15.9831 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.7524 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.3378 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.5994 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9959 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8866 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1610 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.5684 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3643 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -33.2524 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.4159 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.5663 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 33.7280 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.2430 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -10.4950 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.6819 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 63.3011 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4190 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.4251 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 0.9318 -> Slightly above the moving-average trend level.

## TAILWINDS

### General Mills Inc (GIS) Stock Up 5.2% and Still Undervalued -- G
- Summary: General Mills Inc (GIS) Stock Up 5.2% and Still Undervalued -- G
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQaGdBbDE1UVhacG5mMi1wZlVYVTNaMVVwNEV1S1NEbzQ5N2hVeEVPakhYRVRtSnBjOVVjUWNEZldIcTBuR21TWG5venBodTA5WmhabTJjdnpwcV9SeTFMOHJ4SWdfTmI3VkRxQ3oxcnFDeEJkLXdTa3c5dUlPLTNyUW9ZcmNnaVZEemJXbGxkcm4wQmhYX1kzTWJmRHRWaHR5SElCRlVzMFFFaE9RTUE?oc=5>

### General Mills (GIS) Teams Up With Dunkin, Is It Fairly Valued?
- Summary: General Mills partners with Dunkin to expand product offerings and reach new customers.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxPZ2dtWFpaR01sdV9FYUc2LUl2NWFDem5ldzY2WVU3ZkRUSmJoME1wOWdqOVhIdzBzblFHaXFtTjFzUFZNOGNJMnBiU1FXVmtrV2J2RWc2dXJQZHlpcGRhZWNFSVJlTGlrSnhFV1pSR0JSVFF3X3VjRUdJa19lY3RqUWlaMlhTVHVfYmdvWnB2eU4wMEc0bWVnSlRFSFd4VWNpeGFvY01aM1UwUHlKQlNMZ0FCcFVDNlhsZnU2LU0zUGdvVHJKZ2lmM2wzT3pCTWxFZnZESTl2QdIB3AFBVV95cUxOV2o2alcxV3Nsendzc0VnMjhrYUV0Q2VHV3A2cmE4akxLS1ptbGdHYVRjQ0pDaExkbE11WHZYdDVXNTdINUYxLUp4ZW5idVNyUGd2S0RORGFlYmQyNW9uNDh1ZzNyWkN3am5COVpuVkpRN3hMVlhaSElyMG9NT3h6UmdJVkNlX3ktZW1oWEwwVG1kaDEtU2dqYzVOczVnaGhOTGFwem9hazhRZEZhYjN5Z0xKRWpqMWRHcGszRnUxdFVOMk4zYzUydlRwSDhVUW5ZdFZ2R25MOGN2a0lm?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### General Mills (GIS) Stock Trades Close To Its Sales Value
- Summary: GIS shares near sales value, indicating valuation alignment.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxNNEJlMmpXT3JldUc5UWNESmpwM2RzTVBTWHJ3OHE3RzRUb0E4REYwTWZtcWtZSlVSVjlyaDlhNXhienQ2OFFLdlhITGRzc0Vzek1mNERaYks1UGlNamFoSkJwQzl5QUdEOVQ4WEswQnpzN2d5QWFRRjVyMkxKdEVOeFF3ZzJRYVgtVHZWWldwbWQ0TUk1dzhTTHQtd1FBS2FBQ3NBNm1reFA4aEtNajZ1NTQ5V2tGWnliWGZfQkZDZC0xR2FkY0ZIdzByNjFoTXdRVFVj0gHYAUFVX3lxTE5WeWNqcDJJSWFOSzZ4Tk9zejU1N0hhNkFlc0MwTTJkU0ozM0hDZEhDOE5nak1FVk15bXl0WFFOUXlYd1AtanJaajU1eGdYVEVoZUEwYVVnb3hBdW02MnVtTHpZVFQyTDg3SkdmM1BqekFrU1FTSFAxblY5dUlDaGUzN0ZlZzB1NElTWUlCYmI1MzJMSFpNRUF0RlVHTHpFb2VJem53SnpmbjFJNjRTNGdyd21FMnBHV244OVgtQlRoOVNnY2xsZEdMM1hCUldfN1cwSXhudFZkNA?oc=5>

### Dunkin’ and General Mills will bring latte-inspired cereal flavors with no coffee or caffeine.
- Summary: General Mills partners with Dunkin' to launch latte-inspired cereal flavors, expanding product line and appealing to coffee lovers.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOeF9jNkJqZkdNaWxBSGxRNlhvU085TGozaG85WDhkUjIwVW42Ynp6enMybnJsb0hPQ1dNSU1iR3FnamE4TGJMbDBXRW8xUkdPTzdKQzhOUEp5bS16ZmFxZjlxWk0xVUZBWTNkTEQwbTlsOTczcWpGem1aVUlqcDNtS3hzWWRHNGtsMHpJRTlrTFE3WThSaUdNeVpIVnlGQkdibjZ1Ykk1ZkdsZkdDN2xaYk1FVVBKMjlRYlE?oc=5>

### General Mills evaluating selling Häagen-Dazs business outside of North America - WSJ (GIS:NYSE)
- Summary: General Mills is considering divesting its Häagen-Dazs brand outside North America.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOTUlWUkVIaXp1dDd6TEEwR1lkZWd2NkMxTGxzcWRVMkNVUUxmNS0xaEZzd1R6azNQR3VYYW0tRHJ4aGVOXzRxZTRCVHZoZ3RZaFUtWEZsbDY5WmhMQ29SWFpqVTZuMjZRWXVXa2MzUEM2V29tSDlhQVlXM3dkWmR4LTBBZHhzQWx6aGdrMk5aRTVVYUFENm9DLVV2TTdMTjNWYVAwdW5qcFJXLUpyVnNfeGVRaWczeXVKb015ZzRlQQ?oc=5>

### General Mills (GIS) Considers Divesting Häagen-Dazs Outside Nort
- Summary: General Mills is evaluating divestiture of Häagen-Dazs outside North America.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxPRWxaLXJiNFBweC11aXJGM2c5blVxb1paeVNBVUdLdzZoNmhBTWJleDlXTWZ4c3YtT21sX29FUUJUZm5iVnMzaTk4Q0dRR3paVDdKUmwyV1hVR0lQcnlXWllnamcxdDF6V0xrS0lNU2poRUZwM29DdGlJTVMyUnJkazlsMjZRcE4wMnJiMTBSWlQ0MDgycWpVZjVwV201ME9pSkQ1TVZTNTR6VC1pcVhCZ2lCdzR0Z2VqSWhnN24tSmtHbFd2eVhyQXV5YkJLdVU?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GIS** | **N/A** | **2.62** | **9.57** | **-2.80** | **19,494,692,864.00 USD** | **-15.98** |
| KHC | N/A | 0.83 | 8.80 | -2.00 | 30,025,056,256.00 USD | 12.07 |
| CPB | 17.89 | 1.81 | 8.86 | -7.90 | 6,987,638,784.00 USD | -18.23 |
| SJM | 61.98 | 2.48 | 9.33 | 5.00 | 14,234,188,800.00 USD | 31.80 |

Peers fetched as_of: 2026-11-05; GIS reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-23
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

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
- Filing date: 2026-09-23
- Revenue (latest available single quarter): 4,389,500,000.00 USD; period 2026-06-01/2026-08-30; fiscal year/reporting period 2027/Q1
- Net income (latest available single quarter): 397,000,000.00 USD; period 2026-06-01/2026-08-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/40704/000162828026063201/gis-20260830.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMirgFBVV95cUxQaGdBbDE1UVhacG5mMi1wZlVYVTNaMVVwNEV1S1NEbzQ5N2hVeEVPakhYRVRtSnBjOVVjUWNEZldIcTBuR21TWG5venBodTA5WmhabTJjdnpwcV9SeTFMOHJ4SWdfTmI3VkRxQ3oxcnFDeEJkLXdTa3c5dUlPLTNyUW9ZcmNnaVZEemJXbGxkcm4wQmhYX1kzTWJmRHRWaHR5SElCRlVzMFFFaE9RTUE?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxPZ2dtWFpaR01sdV9FYUc2LUl2NWFDem5ldzY2WVU3ZkRUSmJoME1wOWdqOVhIdzBzblFHaXFtTjFzUFZNOGNJMnBiU1FXVmtrV2J2RWc2dXJQZHlpcGRhZWNFSVJlTGlrSnhFV1pSR0JSVFF3X3VjRUdJa19lY3RqUWlaMlhTVHVfYmdvWnB2eU4wMEc0bWVnSlRFSFd4VWNpeGFvY01aM1UwUHlKQlNMZ0FCcFVDNlhsZnU2LU0zUGdvVHJKZ2lmM2wzT3pCTWxFZnZESTl2QdIB3AFBVV95cUxOV2o2alcxV3Nsendzc0VnMjhrYUV0Q2VHV3A2cmE4akxLS1ptbGdHYVRjQ0pDaExkbE11WHZYdDVXNTdINUYxLUp4ZW5idVNyUGd2S0RORGFlYmQyNW9uNDh1ZzNyWkN3am5COVpuVkpRN3hMVlhaSElyMG9NT3h6UmdJVkNlX3ktZW1oWEwwVG1kaDEtU2dqYzVOczVnaGhOTGFwem9hazhRZEZhYjN5Z0xKRWpqMWRHcGszRnUxdFVOMk4zYzUydlRwSDhVUW5ZdFZ2R25MOGN2a0lm?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxNNEJlMmpXT3JldUc5UWNESmpwM2RzTVBTWHJ3OHE3RzRUb0E4REYwTWZtcWtZSlVSVjlyaDlhNXhienQ2OFFLdlhITGRzc0Vzek1mNERaYks1UGlNamFoSkJwQzl5QUdEOVQ4WEswQnpzN2d5QWFRRjVyMkxKdEVOeFF3ZzJRYVgtVHZWWldwbWQ0TUk1dzhTTHQtd1FBS2FBQ3NBNm1reFA4aEtNajZ1NTQ5V2tGWnliWGZfQkZDZC0xR2FkY0ZIdzByNjFoTXdRVFVj0gHYAUFVX3lxTE5WeWNqcDJJSWFOSzZ4Tk9zejU1N0hhNkFlc0MwTTJkU0ozM0hDZEhDOE5nak1FVk15bXl0WFFOUXlYd1AtanJaajU1eGdYVEVoZUEwYVVnb3hBdW02MnVtTHpZVFQyTDg3SkdmM1BqekFrU1FTSFAxblY5dUlDaGUzN0ZlZzB1NElTWUlCYmI1MzJMSFpNRUF0RlVHTHpFb2VJem53SnpmbjFJNjRTNGdyd21FMnBHV244OVgtQlRoOVNnY2xsZEdMM1hCUldfN1cwSXhudFZkNA?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOeF9jNkJqZkdNaWxBSGxRNlhvU085TGozaG85WDhkUjIwVW42Ynp6enMybnJsb0hPQ1dNSU1iR3FnamE4TGJMbDBXRW8xUkdPTzdKQzhOUEp5bS16ZmFxZjlxWk0xVUZBWTNkTEQwbTlsOTczcWpGem1aVUlqcDNtS3hzWWRHNGtsMHpJRTlrTFE3WThSaUdNeVpIVnlGQkdibjZ1Ykk1ZkdsZkdDN2xaYk1FVVBKMjlRYlE?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOTUlWUkVIaXp1dDd6TEEwR1lkZWd2NkMxTGxzcWRVMkNVUUxmNS0xaEZzd1R6azNQR3VYYW0tRHJ4aGVOXzRxZTRCVHZoZ3RZaFUtWEZsbDY5WmhMQ29SWFpqVTZuMjZRWXVXa2MzUEM2V29tSDlhQVlXM3dkWmR4LTBBZHhzQWx6aGdrMk5aRTVVYUFENm9DLVV2TTdMTjNWYVAwdW5qcFJXLUpyVnNfeGVRaWczeXVKb015ZzRlQQ?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxPRWxaLXJiNFBweC11aXJGM2c5blVxb1paeVNBVUdLdzZoNmhBTWJleDlXTWZ4c3YtT21sX29FUUJUZm5iVnMzaTk4Q0dRR3paVDdKUmwyV1hVR0lQcnlXWllnamcxdDF6V0xrS0lNU2poRUZwM29DdGlJTVMyUnJkazlsMjZRcE4wMnJiMTBSWlQ0MDgycWpVZjVwV201ME9pSkQ1TVZTNTR6VC1pcVhCZ2lCdzR0Z2VqSWhnN24tSmtHbFd2eVhyQXV5YkJLdVU?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
