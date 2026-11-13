# GIS Intelligence Report

- ticker: **GIS**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/GIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:11:13.320819+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 13, 'rule': 3, 'ai': 5, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/GIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 13 unique headlines; 8 named publishers; 0 exact duplicates; 13 HTTPS source links; largest publisher share 23.08%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 33.5200 |
| Return 1D (%) | -2.0170 |
| Return 1W (%) | -8.0636 |
| Return 1M (%) | 4.4562 |
| Return YTD (%) | -22.9406 |
| Return 1Y (%) | -22.9406 |
| Annualized volatility (%) | 30.8700 |
| Beta vs SPY | -0.3786 |
| Max drawdown (%) | -33.2524 |
| Sharpe (rf=0) | -0.6940 |
| Downside deviation (rf=0, %) | 21.6427 |
| Sortino (rf=0) | -0.9899 |
| Historical VaR 95% (1D, %) | 2.9959 |
| Historical ES 95% (1D, %) | 3.8866 |
| Correlation vs SPY | -0.1685 |
| Tracking error vs SPY (%) | 35.8394 |
| P/E (trailing) | N/A |
| P/B | 2.41 |
| EV/EBITDA | 9.11 |
| Revenue growth (%) | -2.80 |
| Forward P/E (estimate) | 10.65 |
| Gross margin (%) | 33.73 |
| Operating margin (%) | 15.62 |
| Return on equity (%) | -10.49 |
| Free cash flow yield (%) | 7.27 |
| MA50 | 34.0174 |
| Close vs MA50 (%) | -1.4622 |
| MA200 | 35.9305 |
| Close vs MA200 (%) | -6.7088 |
| RSI (14, Wilder) | 46.3939 |
| MACD (12,26) | 0.2488 |
| MACD signal (9) | 0.2439 |
| MACD histogram | 0.0049 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GIS': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 33.5200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.0170 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -8.0636 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.4562 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -22.9406 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -22.9406 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.8700 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.6427 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.9899 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9959 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8866 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1685 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.8394 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3786 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -33.2524 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.6940 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.6514 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 33.7280 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.6240 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -10.4950 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.2679 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 46.3939 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0049 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -1.4622 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.7088 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### General Mills downgraded by Piper Sandler with a new price target
- Summary: General Mills downgraded by Piper Sandler with a new price target
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNbDF6TU1Ka2t5WlRSUVZhd0JIX2h5QURYdWs4Wkd1WUVDUEQyQnJuaTNyekpGLUlPc3BqSGE5bDdBbDU0aHQtQm5KdXNaRER6bmFmZVVMYk1iUHZtblBzbGwyYzhURkNIX2NhZnJuRUU5MzRMSTJONnpYb0preWU1RzFJWUM1bmFuREJISjRic3RXd2FzZlk2THh5WWpyWXc5c2t3?oc=5>

### General Mills (NYSE:GIS) Downgraded by Piper Sandler to "Neutral"
- Summary: General Mills (NYSE:GIS) Downgraded by Piper Sandler to "Neutral"
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxQX0g3UWJVcFRpZGEwZzY1RU9XUDJtV3pUUmtad1pIaXEwMTVOVzZ6WnhBLVZVVWdoeENDMDA3Ujc3cE1oSUJGZ0tXQkUtNVMyV1NLOHRuVm9kb0F4ODh2dkhFb2Rvc2tUOENWTE55RTFVRVpyVDJ3eTExT1lqaUl5VjV2bmFYYnl3SFc1YXdsVFZMR0pQXzhabzVHcFdCX1EtTTVobGlZU2NqVnl4Zk9SUUdNbkZVbkNaZG8xeVJiYk8?oc=5>

### Is Piper Sandler Wrong to Give Up on General Mills? Wall Street Still Sees $37
- Summary: Piper Sandler analysts have abandoned their previous bullish view on General Mills, maintaining a $37 target price.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOTXRXekdnak5ROWxNR3VTOFA4c2tMcG8zamtRcFdVUXZzSzhXWWZoYVpONUhXbW5RVjdXNWlpelRNTExJTThqNGN5b24zaC11b3ZVRlp2ejI1NVBjZndELWlodG5VdjVtRmJKd2F4UXM1RUhGVHRIZUFMX2dSMFotWElkY3ZkNC1WUFo3djl4dnR3QmVLUHZyZF9NWXNDN0thTXB2aWNn?oc=5>

## CATALYSTS

### General Mills is on watch after Piper Sandler warns of a potential dividend cut (GIS:NYSE)
- Summary: General Mills is on watch after Piper Sandler warns of a potential dividend cut (GIS:NYSE)
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxOY1FUYmJWalRhdWtFN0RnNDlKbGJnYW5NQVpDY1A3QWJLcnZCSGtpd0tZZlg2TzNfX2pPU0ZsSVQ3UWtRaHRlT2w2SVNtTEFDdnNRMlhxN1Bnb1liZkZ1b0huVlBoMVhwX1BlUXJWWnRuYVhYdG0zX0JIeDNURUNkUXJiQzl3UzVlNXZvZWw4NkZocExlMjBESHNYb3dxZThzNFpzaF85NTR4RHF3SEpoR1AwclhCeVR0?oc=5>

### Can General Mills' New Operating Model Drive Profitable Growth?
- Summary: Assessing new operating model's impact on growth.
- Date: 2026-11-11 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPdFZhZXNqMlMwTjFuX25mb2NTV1hJejMwMFpFZllEMG4ycEdqenVCSG5QbXNQYjdBRVc1TkNJOGJNVURteFMwRzM1SWRNaVlQT1lkU3BGbGFWSWN3cURCSGo1MzdEZ2hHUEhVcnJ6c0ZvbW5wUUd6aXBYT0lqdkhzRjJTR0pJM1JjVTNMcUxFbk1JcExMMzNfRnJidHdOT1h4NGt5Wkl0cWVKY0wzS0E0R3JxRWRtYVlX?oc=5>

### General Mills separates businesses to sharpen focus and resource allocation (GIS:NYSE)
- Summary: General Mills is restructuring its business units to improve focus and resource allocation.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOZGVCV3U4T0lTSlM4RGgzYW1FT0pySFNJb3NsbVBESHBmajg1Z0xvTTRsTjA0Rm44ZFMyVFZ5NWltZTBLSlF2bW5ZNlBybTNoTG4tRVFQSTZJaElBTHFSY3d5SFRWOUNXZnNpOXhEWkFER3E3eHFsdTlnTGdGWGNabmlQb2h4MU1OaFpNM0dFZmhzSHZEYWV2bXFFd2lhdUxEMTdmOWZaa3RWTFFjVFpSaU9vWQ?oc=5>

### Better High-Yield Dividend Stock: General Mills vs. Comcast
- Summary: General Mills offers higher dividend yield than Comcast.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOVkxJMlVxMllYdXE2VGYxRnNXbWxiVVpaSGlERUdRaEN1SXNONGxYMkZITUpGRTRhZjlqZEpmb2twUG42akhsSXhvWklfUTJ1MUxmLThCMzRrYnpiMkFDRkZjcXcyd2Q5anlreXVWSXYtejdFRm13VnBYUkE3dS1lSFFKU0FTalZvd1Vj?oc=5>

### General Mills evaluating selling Häagen-Dazs business outside of North America - WSJ (GIS:NYSE)
- Summary: General Mills is considering divesting its Häagen-Dazs brand outside North America, potentially reshaping its portfolio and focus.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOTUlWUkVIaXp1dDd6TEEwR1lkZWd2NkMxTGxzcWRVMkNVUUxmNS0xaEZzd1R6azNQR3VYYW0tRHJ4aGVOXzRxZTRCVHZoZ3RZaFUtWEZsbDY5WmhMQ29SWFpqVTZuMjZRWXVXa2MzUEM2V29tSDlhQVlXM3dkWmR4LTBBZHhzQWx6aGdrMk5aRTVVYUFENm9DLVV2TTdMTjNWYVAwdW5qcFJXLUpyVnNfeGVRaWczeXVKb015ZzRlQQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GIS** | **N/A** | **2.41** | **9.11** | **-2.80** | **17,922,713,600.00 USD** | **-22.94** |
| KHC | N/A | 0.81 | 8.37 | -2.00 | 28,980,133,888.00 USD | 5.68 |
| CPB | 16.85 | 1.71 | 8.61 | -7.90 | 6,582,039,552.00 USD | -24.67 |
| SJM | 62.13 | 2.45 | 9.26 | 5.00 | 14,069,682,176.00 USD | 24.86 |

Peers fetched as_of: 2026-11-12; GIS reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-23
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMiowFBVV95cUxNbDF6TU1Ka2t5WlRSUVZhd0JIX2h5QURYdWs4Wkd1WUVDUEQyQnJuaTNyekpGLUlPc3BqSGE5bDdBbDU0aHQtQm5KdXNaRER6bmFmZVVMYk1iUHZtblBzbGwyYzhURkNIX2NhZnJuRUU5MzRMSTJONnpYb0preWU1RzFJWUM1bmFuREJISjRic3RXd2FzZlk2THh5WWpyWXc5c2t3?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxQX0g3UWJVcFRpZGEwZzY1RU9XUDJtV3pUUmtad1pIaXEwMTVOVzZ6WnhBLVZVVWdoeENDMDA3Ujc3cE1oSUJGZ0tXQkUtNVMyV1NLOHRuVm9kb0F4ODh2dkhFb2Rvc2tUOENWTE55RTFVRVpyVDJ3eTExT1lqaUl5VjV2bmFYYnl3SFc1YXdsVFZMR0pQXzhabzVHcFdCX1EtTTVobGlZU2NqVnl4Zk9SUUdNbkZVbkNaZG8xeVJiYk8?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOTXRXekdnak5ROWxNR3VTOFA4c2tMcG8zamtRcFdVUXZzSzhXWWZoYVpONUhXbW5RVjdXNWlpelRNTExJTThqNGN5b24zaC11b3ZVRlp2ejI1NVBjZndELWlodG5VdjVtRmJKd2F4UXM1RUhGVHRIZUFMX2dSMFotWElkY3ZkNC1WUFo3djl4dnR3QmVLUHZyZF9NWXNDN0thTXB2aWNn?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxOY1FUYmJWalRhdWtFN0RnNDlKbGJnYW5NQVpDY1A3QWJLcnZCSGtpd0tZZlg2TzNfX2pPU0ZsSVQ3UWtRaHRlT2w2SVNtTEFDdnNRMlhxN1Bnb1liZkZ1b0huVlBoMVhwX1BlUXJWWnRuYVhYdG0zX0JIeDNURUNkUXJiQzl3UzVlNXZvZWw4NkZocExlMjBESHNYb3dxZThzNFpzaF85NTR4RHF3SEpoR1AwclhCeVR0?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPdFZhZXNqMlMwTjFuX25mb2NTV1hJejMwMFpFZllEMG4ycEdqenVCSG5QbXNQYjdBRVc1TkNJOGJNVURteFMwRzM1SWRNaVlQT1lkU3BGbGFWSWN3cURCSGo1MzdEZ2hHUEhVcnJ6c0ZvbW5wUUd6aXBYT0lqdkhzRjJTR0pJM1JjVTNMcUxFbk1JcExMMzNfRnJidHdOT1h4NGt5Wkl0cWVKY0wzS0E0R3JxRWRtYVlX?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOZGVCV3U4T0lTSlM4RGgzYW1FT0pySFNJb3NsbVBESHBmajg1Z0xvTTRsTjA0Rm44ZFMyVFZ5NWltZTBLSlF2bW5ZNlBybTNoTG4tRVFQSTZJaElBTHFSY3d5SFRWOUNXZnNpOXhEWkFER3E3eHFsdTlnTGdGWGNabmlQb2h4MU1OaFpNM0dFZmhzSHZEYWV2bXFFd2lhdUxEMTdmOWZaa3RWTFFjVFpSaU9vWQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOVkxJMlVxMllYdXE2VGYxRnNXbWxiVVpaSGlERUdRaEN1SXNONGxYMkZITUpGRTRhZjlqZEpmb2twUG42akhsSXhvWklfUTJ1MUxmLThCMzRrYnpiMkFDRkZjcXcyd2Q5anlreXVWSXYtejdFRm13VnBYUkE3dS1lSFFKU0FTalZvd1Vj?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOTUlWUkVIaXp1dDd6TEEwR1lkZWd2NkMxTGxzcWRVMkNVUUxmNS0xaEZzd1R6azNQR3VYYW0tRHJ4aGVOXzRxZTRCVHZoZ3RZaFUtWEZsbDY5WmhMQ29SWFpqVTZuMjZRWXVXa2MzUEM2V29tSDlhQVlXM3dkWmR4LTBBZHhzQWx6aGdrMk5aRTVVYUFENm9DLVV2TTdMTjNWYVAwdW5qcFJXLUpyVnNfeGVRaWczeXVKb015ZzRlQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
