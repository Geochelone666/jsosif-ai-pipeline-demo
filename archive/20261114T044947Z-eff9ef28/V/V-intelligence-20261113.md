# V Intelligence Report

- ticker: **V**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T05:09:08.332354+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 19, 'rule': 6, 'ai': 8, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/V** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 19 unique headlines; 6 named publishers; 0 exact duplicates; 19 HTTPS source links; largest publisher share 36.84%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 425.7600 |
| Return 1D (%) | 1.2967 |
| Return 1W (%) | 0.9223 |
| Return 1M (%) | 7.6979 |
| Return YTD (%) | 22.3545 |
| Return 1Y (%) | 27.6808 |
| Annualized volatility (%) | 22.9759 |
| Beta vs SPY | 0.3326 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 1.1818 |
| Downside deviation (rf=0, %) | 14.1670 |
| Sortino (rf=0) | 1.9166 |
| Historical VaR 95% (1D, %) | 1.8026 |
| Historical ES 95% (1D, %) | 2.7901 |
| Correlation vs SPY | 0.1974 |
| Tracking error vs SPY (%) | 24.2921 |
| P/E (trailing) | 34.12 |
| P/B | 22.21 |
| EV/EBITDA | 24.79 |
| Revenue growth (%) | 13.20 |
| Forward P/E (estimate) | 24.84 |
| Gross margin (%) | 97.68 |
| Operating margin (%) | 66.31 |
| Return on equity (%) | 63.51 |
| Free cash flow yield (%) | 2.64 |
| MA50 | 389.7040 |
| Close vs MA50 (%) | 9.2522 |
| MA200 | 345.7896 |
| Close vs MA200 (%) | 23.1269 |
| RSI (14, Wilder) | 63.2434 |
| MACD (12,26) | 10.2183 |
| MACD signal (9) | 10.8091 |
| MACD histogram | -0.5908 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 425.7600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.2967 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.9223 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.6979 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 22.3545 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 27.6808 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.9759 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.1670 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.9166 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8026 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7901 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1974 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.2921 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3326 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.1805 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1818 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.8395 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.6780 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.3070 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 63.5070 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.6415 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 34.1154 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 63.2434 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.5908 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 9.2522 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 23.1269 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Visa (NYSE:V) Stock Price Down 1.2% - Here's What Happened
- Summary: Visa (NYSE:V) Stock Price Down 1.2% - Here's What Happened
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPZkNZLVJ6ZEs3bkxKWFNVZ1haZHFGdFZPUWtjTmZmQ3ZaNGM2RXIwMGQydmcyc081aF9zbjB3clAtRUlHM1hWNUo0Y19GMXY5RDczeWtJdEZfTmU3N3VoQUJ3ZE45Tk83dVAyUjJxQ0w5UGhIVnNSakpCemkzN0hHOTB5bklmVWZzUjRPYkNvYUFZWllyUmJaWmJpcDhYY2lSa0hmWjhveURlWFB3WEIxQw?oc=5>

## CATALYSTS

### Visa or Mastercard: I Can Only Pick One Dividend Stock for the Next 20 Years. Here’s Mine
- Summary: Visa or Mastercard: I Can Only Pick One Dividend Stock for the Next 20 Years. Here’s Mine
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE5GTkZNY2N4Q0swcmZNcnlCUnlqRWlpRWFITE1EZjRFNlVzZklocHpoWnBILTZwVjBkbDNaZS1OeExGLUZ3aHQyRXYwWlNyVTd3ekZXVDlVTm1ERnBoLWNNU0NoczM4RFdZT29OTWpQdkxMU0ZxWnMyNEV6NXR5dw?oc=5>

### Visa Inc. $V Stock Bought by Retirement Systems of Alabama
- Summary: Visa Inc. $V Stock Bought by Retirement Systems of Alabama
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNb3lZVF9mRGZrQjl5UXcyN1E4SHZVTjh5NmhuYmxFTDVFbHJrdWdYLTdSLUNWVWZLWkxHZnZVTmloOXJ3Nm1QaG9OWXlmLW92Z3hQUmNqVmZuQjM2VjZ6Q09GZjVRXzd4NnVaN1h2SVZ4cWxqb0dEZk1nNllDdnNWX21KRGtWVE9adzZvR2lFTXZucEVxVDE1NnBvbWtrbVFGcHRVdTFqanV3a3dGOXdiXzNNNkgzdGJo?oc=5>

### Visa Inc. $V Stock Purchased by Kestra Investment Management LLC
- Summary: Visa Inc. $V Stock Purchased by Kestra Investment Management LLC
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxONGc0N2FvdDVpbnhSN3JlY19IRWlMQ1VfU0tzcUp5YThYS0dsRFNyeGY0NkRGVm5GaHdwQVFKUi1td2tvNDFRVlQ0YmFvQUFZOHh1UzE3bHNxcjNRaXpCNU42S1BpODlOaGxNckZXb1dHQlRib0hfVUhQeExXVHZBY3J5VXlMM01aalhjVUdRUHNjLUNMSUl4Z3RSenBXVzR0aGVpWE1pbHdHLTBHWGliYkRhYXIxRWNZWUt4SERFa3k?oc=5>

### Visa (V) Stock Price Stalls After Q4 Earnings Beat
- Summary: Visa (V) Stock Price Stalls After Q4 Earnings Beat
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxQRmYzcXpPN1dXRkl4M2ZBOWhmR3QxVUZwR2hTTlpLRjczMnJ1Q1BybWpGT0VvYVBvSHNlZk5IUlQzYkVYdllLVXViSGVhS2dHbXUxZE1wVmkzanV6SXNrZTVwbGtiT0hYZC01ZVN6MDBIcUV5NV85WHI0bXJ6Z1laNS1mcGRJel9TQ2U5UGlxaV9RVGEzSGV6S1F5eVg2dnptQnNqSzBnZ0JOMXcxcEhYOHhUUTRiTlhubjIyY9IBwgFBVV95cUxQakl0U1FCSGgtcG5LVFJhcE5GOVZrVDdfZG1qNFpwekFuclhDSDZHYWFFX0VkeXAwdUx0NnBfUHRZM1o4MG5odVR6c0NqbFZFTmRSeWZpTV9NVWRUd3dyTzNvR29uZHQ0X2s2TU1Eb21VcFB1TGFVTXZHaWEyZy1YaWNiLXBHUWJvLU9qUE5PM1Vnd2NxMWdwMmZZTFJxN3pwZXlnMDBvVEpuWndHNm5GSUtHekJXVnk0S09wbFlEQkNkQQ?oc=5>

### Visa Inc. $V Stock Bought by Candriam S.C.A.
- Summary: Visa Inc. $V Stock Bought by Candriam S.C.A.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNakp3ajlGaUhIRUh4S3I2ajNFRE5iX1ZXMGhCTzNfVjRnRHliSDk3emxabWcwWl9zY05tM1FqZUwwSkk0cEkzT1hidVZ2WmNhU1A2OG9tekxZSm9pbnFjYldBbGhKekZQdjVYTzNGb3V5MTR1Qk5waWZHMnQ4V0Z6WnJTMHJoeDVBR1JzVmFhWmZwX0FldTZtTlQtM083bnZNU3c?oc=5>

### Visa (V) Stock Could Be Reasonable With Excess Returns Intact
- Summary: Speculation that Visa stock may remain attractive with excess returns intact.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPamgyTVlJR1Rza3hGS3VHejlSczNrQ2J0cndUSVM4cDlsQ0xsNWNkdzdtUVo5ZkZQOTJkSVZNNHcwWUkxMUNQQ0hrTmxCZU1wdUV6OHlla1VoTTlDZmRxTUhZTFhfbF8yMTVCTTVNYjEwR2d4clpoTzFHZkZ3aUhQeDVoZlJVOGxnWEtqZEVOdFUzLTJKekdoSDNB?oc=5>

### Bryan Bergin Calls Fiscal 2026 a Banner Year for Visa (V). Here’s What He Expects Next
- Summary: Visa's CEO predicts strong fiscal 2026, highlighting growth expectations and strategic initiatives.
- Date: 2026-11-12 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNOHhzbFF6YndaajNISGRVc1F1ZkR5ZDFoTm1xbHhxd2VaZXphcmhmUk5JVmU4dHBMRzlndmdUTEFpY0pHYTNyd2dySHUxWnFSWUItMHliZlFDSkJkbzdLaWFCRmc5S2FWNlVNNXZid3lMT0NXWmVvWS1Ma1dYbFpqNWJlTE5UZEh2cVZrdDBXOHN4UGZybHV2aXdvaw?oc=5>

### Will Stablecoin Settlement Expansion Change Visa (V) Stock Narrative
- Summary: Speculation on stablecoin expansion's effect on Visa.
- Date: 2026-11-12 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxQRFhqRzV0UUZXNEdZRDFUZUxfTzlnM2tZV0dNMzNXamg1RVY3MlRWdS1qU1BKSDB4S1lBVlNiVmc0a21XMHlsajljdGYtN0lndFRGdWVhS0lhTGNqNmJudXpkblNnY2N2VXBReTFRU1JSajJwczMyQUFoOThGUDAtb25UMWtVUjYzdXhPUG1sUzAyQU9oLXZZRXliUFVaeG1OSy1xblR5Yi1wQ1JNc2VHVzdVUHdpS3R1c0NoRmJhVGpVUWVJUVhHUmtUSWbSAdIBQVVfeXFMTlZjV1NJNU1KVjRoTXZzdHZqalVRRHd0TzlsWDNiZVBOYS1uUC14THBmLUpwdklzLXRfUlEydDhlM2x0SDV0UzZNNVlPYlF1dm9nYTdIaHJISVYwSDg5QXVtNzdzN3BqWU1RLXJiLXlUblNaTUs1ZmlQYVM0Vi04aG5aZXhySEJPTEZqSW5VcW1TdnQxVEhMNlM1LS02enJkalRiLTJMWjRBX29IZWJsLTZrUm9hSEQ0dXBrcFpidDBKSF9nZG4zZkRadEFHME5VbmNn?oc=5>

### Citigroup Issues Positive Forecast for Visa (NYSE:V) Stock Price
- Summary: Citigroup forecasts a positive outlook for Visa stock.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQS0JsRjVsMzh1UG55eVFlaHpwaWJTam5DQjVZUFo3dG1SVUpFWU1CRHBLV1JLSkZhSm5kTEd4MGZrdmFKQ0ZzNlBSODdpcjgxa3FzNTJzOEFUQlJXUmxtVlF5ZGR1blc0c0J4bElpS1hkcDZiNXF6TC1UVnhBV3UzcHkzcVJtLTk3T2NvUF9zU29UZFQ1SE1xU0txQnNtd0piQ05YR1FEc2kxbG9LZEJfMFFFckNnTWtrY0xGdmFvZklFQQ?oc=5>

### Are Wall Street Analysts Predicting Visa Stock Will Climb or Sink?
- Summary: Analysts discuss potential price movement for Visa, offering bullish or bearish outlooks.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQUm1yUksyZ2NYWkVCUWZlbHk4ejNxaWtjN1cwbWhXU1RfVWFudnpoUDRZOHVhc1NOTDZXNlRwMEx4eXpYanBjc2h2UEw1QzhOcUlXUnZCMmZNUmpab1JLLWhXTkxBcVQ1UzhrbFpCcUJMbVdXek1EWXlsb1NPN1ZUU1REbjE2SkF5WlRRZEtCUThwdUY1OFJfbWJMdzRvUnIxaUdB?oc=5>

### ETFs Bought $107.9 Million of Visa (V) on Nov. 11
- Summary: Institutional ETFs increased holdings in Visa, indicating confidence in the stock.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOYUZLbEtDc0J1emtpazl0dUpaWFhQczdBb2ZEbG9pcFpxUnBKVExvNk12ZXJRWGhMcDM3dk1SdFY5cjE2TGxZWWtyMUZYY2U1dGF4WlBlREpDSDE5Q1hrWHI1QjZSV0NKWEN6VElwT0JqLUNJQXZPdjJqZW1SRVA5OU9wYjczbFVZS3BaZUN3bnpnUk1Y?oc=5>

### Visa (NYSE:V) Stock Jumps 1.2% - Time to Buy?
- Summary: Visa shares rose 1.2%, reflecting short-term positive market reaction.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOYWYyZU9CcllwdkZqV3EzSXUzdmpjU3pVa2ZKMDI3bTFrZmxxaHJzX1RiUUhmVGJLZlIta2pKOExHbG8wUHFoQVZfcUhpQkttN0RNY0VhakxLVE90S1JLS0pWMkhVZ2ZUYnM1YVlHZ21Nb25PNk1TOVp4cFpRbl9Vb3dHeHg4enZUWDFYajFod242Ukx5V215bnB3VUh5czA?oc=5>

### Visa Inc. $V Stock: Ethic Inc. Boosts Stake
- Summary: Ethic Inc. increased its stake in Visa, signaling stronger ownership interest.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNMnZ5SkpVSERZVWFFa1pfUXVFVkRydDNFVTYzVkNTeVpsVDR2QkRRakh4WXlUZmthaEwtcGM4VHpMNlVwSkUtcTVaZy1oeGE1aUwxMTlpdzFKUTc4ZXBWa3BvRWlULVRwaDliZ2Jqc0t2Zmo0Zk5keklpNzVWeklCUmI1Smp2YVluREtVUmg4TDJZRGsya1hMTUxkS3ZHWVBYVWc?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **V** | **34.12** | **22.21** | **24.79** | **13.20** | **794,383,024,128.00 USD** | **27.68** |
| MA | 34.15 | 85.39 | 25.60 | 14.00 | 576,012,943,360.00 USD | 19.78 |
| PYPL | 11.12 | 2.55 | 8.16 | 2.00 | 49,241,423,872.00 USD | -8.25 |
| AXP | 17.92 | 6.01 | N/A | 11.30 | 214,978,969,600.00 USD | -11.11 |

Peers fetched as_of: 2026-11-13; V reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-05
- Revenue (latest available single quarter): 5,840,000,000.00 USD; period 2019-04-01/2019-06-30; fiscal year/reporting period 2019/Q3
- Net income (latest available single quarter): 5,628,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1403161/000140316126000134/v-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMisAFBVV95cUxPZkNZLVJ6ZEs3bkxKWFNVZ1haZHFGdFZPUWtjTmZmQ3ZaNGM2RXIwMGQydmcyc081aF9zbjB3clAtRUlHM1hWNUo0Y19GMXY5RDczeWtJdEZfTmU3N3VoQUJ3ZE45Tk83dVAyUjJxQ0w5UGhIVnNSakpCemkzN0hHOTB5bklmVWZzUjRPYkNvYUFZWllyUmJaWmJpcDhYY2lSa0hmWjhveURlWFB3WEIxQw?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE5GTkZNY2N4Q0swcmZNcnlCUnlqRWlpRWFITE1EZjRFNlVzZklocHpoWnBILTZwVjBkbDNaZS1OeExGLUZ3aHQyRXYwWlNyVTd3ekZXVDlVTm1ERnBoLWNNU0NoczM4RFdZT29OTWpQdkxMU0ZxWnMyNEV6NXR5dw?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNb3lZVF9mRGZrQjl5UXcyN1E4SHZVTjh5NmhuYmxFTDVFbHJrdWdYLTdSLUNWVWZLWkxHZnZVTmloOXJ3Nm1QaG9OWXlmLW92Z3hQUmNqVmZuQjM2VjZ6Q09GZjVRXzd4NnVaN1h2SVZ4cWxqb0dEZk1nNllDdnNWX21KRGtWVE9adzZvR2lFTXZucEVxVDE1NnBvbWtrbVFGcHRVdTFqanV3a3dGOXdiXzNNNkgzdGJo?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxONGc0N2FvdDVpbnhSN3JlY19IRWlMQ1VfU0tzcUp5YThYS0dsRFNyeGY0NkRGVm5GaHdwQVFKUi1td2tvNDFRVlQ0YmFvQUFZOHh1UzE3bHNxcjNRaXpCNU42S1BpODlOaGxNckZXb1dHQlRib0hfVUhQeExXVHZBY3J5VXlMM01aalhjVUdRUHNjLUNMSUl4Z3RSenBXVzR0aGVpWE1pbHdHLTBHWGliYkRhYXIxRWNZWUt4SERFa3k?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxQRmYzcXpPN1dXRkl4M2ZBOWhmR3QxVUZwR2hTTlpLRjczMnJ1Q1BybWpGT0VvYVBvSHNlZk5IUlQzYkVYdllLVXViSGVhS2dHbXUxZE1wVmkzanV6SXNrZTVwbGtiT0hYZC01ZVN6MDBIcUV5NV85WHI0bXJ6Z1laNS1mcGRJel9TQ2U5UGlxaV9RVGEzSGV6S1F5eVg2dnptQnNqSzBnZ0JOMXcxcEhYOHhUUTRiTlhubjIyY9IBwgFBVV95cUxQakl0U1FCSGgtcG5LVFJhcE5GOVZrVDdfZG1qNFpwekFuclhDSDZHYWFFX0VkeXAwdUx0NnBfUHRZM1o4MG5odVR6c0NqbFZFTmRSeWZpTV9NVWRUd3dyTzNvR29uZHQ0X2s2TU1Eb21VcFB1TGFVTXZHaWEyZy1YaWNiLXBHUWJvLU9qUE5PM1Vnd2NxMWdwMmZZTFJxN3pwZXlnMDBvVEpuWndHNm5GSUtHekJXVnk0S09wbFlEQkNkQQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNakp3ajlGaUhIRUh4S3I2ajNFRE5iX1ZXMGhCTzNfVjRnRHliSDk3emxabWcwWl9zY05tM1FqZUwwSkk0cEkzT1hidVZ2WmNhU1A2OG9tekxZSm9pbnFjYldBbGhKekZQdjVYTzNGb3V5MTR1Qk5waWZHMnQ4V0Z6WnJTMHJoeDVBR1JzVmFhWmZwX0FldTZtTlQtM083bnZNU3c?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPamgyTVlJR1Rza3hGS3VHejlSczNrQ2J0cndUSVM4cDlsQ0xsNWNkdzdtUVo5ZkZQOTJkSVZNNHcwWUkxMUNQQ0hrTmxCZU1wdUV6OHlla1VoTTlDZmRxTUhZTFhfbF8yMTVCTTVNYjEwR2d4clpoTzFHZkZ3aUhQeDVoZlJVOGxnWEtqZEVOdFUzLTJKekdoSDNB?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNOHhzbFF6YndaajNISGRVc1F1ZkR5ZDFoTm1xbHhxd2VaZXphcmhmUk5JVmU4dHBMRzlndmdUTEFpY0pHYTNyd2dySHUxWnFSWUItMHliZlFDSkJkbzdLaWFCRmc5S2FWNlVNNXZid3lMT0NXWmVvWS1Ma1dYbFpqNWJlTE5UZEh2cVZrdDBXOHN4UGZybHV2aXdvaw?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxQRFhqRzV0UUZXNEdZRDFUZUxfTzlnM2tZV0dNMzNXamg1RVY3MlRWdS1qU1BKSDB4S1lBVlNiVmc0a21XMHlsajljdGYtN0lndFRGdWVhS0lhTGNqNmJudXpkblNnY2N2VXBReTFRU1JSajJwczMyQUFoOThGUDAtb25UMWtVUjYzdXhPUG1sUzAyQU9oLXZZRXliUFVaeG1OSy1xblR5Yi1wQ1JNc2VHVzdVUHdpS3R1c0NoRmJhVGpVUWVJUVhHUmtUSWbSAdIBQVVfeXFMTlZjV1NJNU1KVjRoTXZzdHZqalVRRHd0TzlsWDNiZVBOYS1uUC14THBmLUpwdklzLXRfUlEydDhlM2x0SDV0UzZNNVlPYlF1dm9nYTdIaHJISVYwSDg5QXVtNzdzN3BqWU1RLXJiLXlUblNaTUs1ZmlQYVM0Vi04aG5aZXhySEJPTEZqSW5VcW1TdnQxVEhMNlM1LS02enJkalRiLTJMWjRBX29IZWJsLTZrUm9hSEQ0dXBrcFpidDBKSF9nZG4zZkRadEFHME5VbmNn?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQS0JsRjVsMzh1UG55eVFlaHpwaWJTam5DQjVZUFo3dG1SVUpFWU1CRHBLV1JLSkZhSm5kTEd4MGZrdmFKQ0ZzNlBSODdpcjgxa3FzNTJzOEFUQlJXUmxtVlF5ZGR1blc0c0J4bElpS1hkcDZiNXF6TC1UVnhBV3UzcHkzcVJtLTk3T2NvUF9zU29UZFQ1SE1xU0txQnNtd0piQ05YR1FEc2kxbG9LZEJfMFFFckNnTWtrY0xGdmFvZklFQQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQUm1yUksyZ2NYWkVCUWZlbHk4ejNxaWtjN1cwbWhXU1RfVWFudnpoUDRZOHVhc1NOTDZXNlRwMEx4eXpYanBjc2h2UEw1QzhOcUlXUnZCMmZNUmpab1JLLWhXTkxBcVQ1UzhrbFpCcUJMbVdXek1EWXlsb1NPN1ZUU1REbjE2SkF5WlRRZEtCUThwdUY1OFJfbWJMdzRvUnIxaUdB?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOYUZLbEtDc0J1emtpazl0dUpaWFhQczdBb2ZEbG9pcFpxUnBKVExvNk12ZXJRWGhMcDM3dk1SdFY5cjE2TGxZWWtyMUZYY2U1dGF4WlBlREpDSDE5Q1hrWHI1QjZSV0NKWEN6VElwT0JqLUNJQXZPdjJqZW1SRVA5OU9wYjczbFVZS3BaZUN3bnpnUk1Y?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOYWYyZU9CcllwdkZqV3EzSXUzdmpjU3pVa2ZKMDI3bTFrZmxxaHJzX1RiUUhmVGJLZlIta2pKOExHbG8wUHFoQVZfcUhpQkttN0RNY0VhakxLVE90S1JLS0pWMkhVZ2ZUYnM1YVlHZ21Nb25PNk1TOVp4cFpRbl9Vb3dHeHg4enZUWDFYajFod242Ukx5V215bnB3VUh5czA?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNMnZ5SkpVSERZVWFFa1pfUXVFVkRydDNFVTYzVkNTeVpsVDR2QkRRakh4WXlUZmthaEwtcGM4VHpMNlVwSkUtcTVaZy1oeGE1aUwxMTlpdzFKUTc4ZXBWa3BvRWlULVRwaDliZ2Jqc0t2Zmo0Zk5keklpNzVWeklCUmI1Smp2YVluREtVUmg4TDJZRGsya1hMTUxkS3ZHWVBYVWc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
