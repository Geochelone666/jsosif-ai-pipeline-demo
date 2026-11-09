# MCO Intelligence Report

- ticker: **MCO**
- Report as_of: **2026-11-08**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/MCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-08**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-09T04:33:02.682133+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 13, 'rule': 1, 'ai': 8, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261108T041758Z-43fb2458/MCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 13 unique headlines; 4 named publishers; 1 exact duplicates; 13 HTTPS source links; largest publisher share 76.92%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 505.6700 |
| Return 1D (%) | -1.8764 |
| Return 1W (%) | 2.3810 |
| Return 1M (%) | 11.7947 |
| Return YTD (%) | -0.3532 |
| Return 1Y (%) | 5.7747 |
| Annualized volatility (%) | 28.5781 |
| Beta vs SPY | 0.5128 |
| Max drawdown (%) | -23.6059 |
| Sharpe (rf=0) | 0.3402 |
| Downside deviation (rf=0, %) | 20.2292 |
| Sortino (rf=0) | 0.4805 |
| Historical VaR 95% (1D, %) | 2.4637 |
| Historical ES 95% (1D, %) | 3.8509 |
| Correlation vs SPY | 0.2431 |
| Tracking error vs SPY (%) | 28.4959 |
| P/E (trailing) | 30.85 |
| P/B | 26.68 |
| EV/EBITDA | 23.05 |
| Revenue growth (%) | 0.80 |
| Forward P/E (estimate) | 27.15 |
| Gross margin (%) | 74.63 |
| Operating margin (%) | 46.27 |
| Return on equity (%) | 76.74 |
| Free cash flow yield (%) | 2.91 |
| MA50 | 477.4824 |
| Close vs MA50 (%) | 5.9034 |
| MA200 | 465.1157 |
| Close vs MA200 (%) | 8.7192 |
| RSI (14, Wilder) | 58.6170 |
| MACD (12,26) | 10.9505 |
| MACD signal (9) | 7.4709 |
| MACD histogram | 3.4796 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCO': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 505.6700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.8764 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.3810 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 11.7947 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -0.3532 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 5.7747 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.5781 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.2292 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4805 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4637 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8509 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2431 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.4959 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5128 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.6059 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3402 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 27.1540 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 46.2680 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 76.7410 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.9070 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 30.8524 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 58.6170 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 3.4796 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.9034 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 8.7192 -> Clearly above the moving-average trend level.

## TAILWINDS

### Moody's Corporation $MCO Stock: Bank Julius Baer & Co. Ltd Zurich Grows Holdings
- Summary: Bank Julius Baer increases holdings in Moody's.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxQZlpzVnNJX0Nhck9qNHpERllIalJLbzY0TndiSTJSbzBvSjAxYkFWTE5vTGk0Tm5zeTZ2V2RZNkN4OU04Z2tBeWwwUGdRdmItVkMtZXJpbHpuT09qeG11bGo4Yk05VEhKQ2pyUWQ2RTBES00zMkJtSG9RN1FjdGU3MGJmNDI0UkhDd2hMUkZuQkpaV0lFNldYQ1ZvYUtDNFVoRXB4VDdqd3VQckotZUhzbzdZS3F2anVlZEpCU2lDTWc1Uk9QS2I4dnVqZXR2OWNu?oc=5>

## HEADWINDS

### Sumitomo Mitsui Trust Group Inc. Sells 13,537 Shares of Moody's Corporation $MCO
- Summary: Sumitomo Mitsui Trust sells 13,537 shares of Moody's.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxNTnE3cFNIRm5SWVlDTU0yRmRyeVJJdGJlOGZMV3hKenVuSUc2U1Q1QmtKQjVUXzRRWkhENDkwT09HU3dhRHR1NUNjSmVvemxDRkpqNURfWEU1Q3ZlZFprYW05b2hTN2FhX0g5b3FwXzB0WTVyNGM0WXJsZEV0eldXS1h2alBnN0ZzSld2b1AxalpNeEl2YU5SLU5VdWxPODBPWkVZQjV5YlM5LTQ3QVBRV3I5WC1sZGVFMnJGYzdMQlZYeWhWaUpBSzF5RS1Rbkk3V0l3?oc=5>

## CATALYSTS

### Moody's Corporation $MCO Stock Bought by Candriam S.C.A.
- Summary: Moody's Corporation $MCO Stock Bought by Candriam S.C.A.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOWE1rSklBa3RmcU5aSXJZanNuODZJNE9TLVlSR3kzQXk3eXV1WDBidU1EQ2lmU2FHNGFqeVh6WDVqX2NqTFU2QjlZeDI1bk1yeG4yQ3JnUGpURlQ0QVF4aWtxNXlBRy05dThQQ285NUN2WklmZnpBYWkwSGlzcGpVMnR0dVVmYjg0bzZ1S3FpcHpvd19tenBhZUdyaDA3a25NX3Q1YlhhdUVQNmFJQjZVck93?oc=5>

### Moody's (NYSE:MCO) CEO Sells $103,199.85 in Stock
- Summary: Moody's CEO sold shares, indicating a personal liquidity move rather than a corporate decision.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPa1MzQUZFRTU5OVhQRnpWZS1EUTBQVC11bTh1eHh5enpFdTVYeFdkRjM5enRMSjgyU2ZzaFdlaUJyYUxQMW5BUHdNNEliZ3JkNk5wSXJSR0lfUEpGMUJQeU85NVFIRnBZa25HbW9tRVA4WndFN2NOQllEX1gyRnZUYmpRVUZJYW5KQ3p5N1F1Qzh6WjBPTEMtQUFtOGpJUkJxNGlDYWFzV0o?oc=5>

### Moody's (NYSE:MCO) Stock: Insider Michael West Sells 185 Shares
- Summary: Insider Michael West sold 185 shares of Moody's stock.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxNa2NSYW1VUFE3YUFRQkU1Q19sVTNIaHVZWEhuMTlqTU9IV3hEMjJvRVhXb1R2SC13X3NJVWV3X3B0TEN6NjJtN1lFSzRsTHpUeFJjQWpVY0xta1BUNEVSRFJlTzMtN1NNUDJUVXYwQnBzblRpV0hPQ0xORjFxMG1ISzF2bEJHQ2Nha1FqM2ROUUlhc0poNmh1QjlINHlKcW9ydExQUERFQlJpdFZXQU5TdWpLa3p6SmVKeHpaOTFn?oc=5>

### Insider Selling: Moody's (NYSE:MCO) Insider Sells $99,299.85 in Stock
- Summary: An insider sold shares worth $99,299.85 of Moody's stock.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQSlpDVG4xU3lvUXh3dnVPTUQyd0VHcGVYeUg5VEVickNfWFhMSFB2N0JLS3Rrc1VmeWh5eDY0X1RCcG94MmtTMXAybkZsUWh6RU45c3g4WVRyVENOV2YxajE5YXJOMnhlXzZSeHNXbklqcFNzSmlxUThGWE1OQjJQQVFmQWtaZlVBa0h1M1VWLTNsWmlJUkZFMmdlUXJ6cTVaN2VtNHF6bXE4cHp5WENCNE41TGRJVkQ2bVI5ZmZ1Qk0wUQ?oc=5>

### Moody's Corporation $MCO Stock: Kestra Advisory Services LLC Grows Stake
- Summary: Kestra Advisory Services LLC increased its stake in Moody’s Corporation.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPd1Fhd2c3VmhwaFVlTEZQQ191c3J5M04waktmWjhibGpuYmhqTkRuQU94R2wzVzVKX1ItYUxlekVPMjFJX3I2THdsRmRhQW1OcFhRSXc3d3NNa3hsMVN2YVo1SVN5NWlaS1dsLVJ5Q1hHWUZnaldzV1VDZE53azVnQ1JwT0RMcDB0M3V4ZzJIaDBfcDZiQ3FCZ0stUkxmLXA5Tld0RXR1bGQ5UTNjalNwNUFtbXJaV0RvT0dmbmJINm5Pa3FKbGJfSjRR?oc=5>

### Moody's Corporation $MCO Position Cut by Allen Investment Management LLC
- Summary: Allen Investment Management LLC reduced its position in Moody’s Corporation.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxNazJoeGhBXzVXSU5sWC1fOEVYRGFFZmMzYm4tdWRIZlA2RkpjNHBvYWdxeVk0ZmlmaFdjWlhDSlVxQ05mR3MzS0F6b3NuWkNkckx6cGw3aHNRQzZwMlp1NUpEdWoza2JVeW53WlBsSkladE9ua3VIN3dUVlVHOFV2bEVqWGFKdUJCcXA0WTBQcnN6ckt0RkhNTEtKakZMQVkwcE56Z1lXYzkwTkQ5UEhIYjdTV3p3WmQ3VVZnWm5MdkZSLUEtcHc4a1lNdw?oc=5>

### Moody's Corporation $MCO Stock: Hikari Power Ltd Trims Stake
- Summary: Hikari Power Ltd trimmed its stake in Moody’s Corporation.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNazJMa0h3bUdHYUk3MmJTOGJ0WmZRV01RM3lRVjVTZTVWVWNJQWdsQS1mWE14aUIxbS01ajQ4d0twN2phdWQxOTdrLXZUVnVBSlYtd2lLRGw1cF9XSWFZZXJtaExmLXVBOXNxeFoxZWN4SGJxSk5WeXlLbERrSnVoUGF2TzBVODVTNlZrWkU4eFZNY1VqblMzdnNSN2dOS3dNdEh0cFVzR0ZuekhLUjdiT2pJV2tTTm45UEE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCO** | **30.85** | **26.68** | **23.05** | **0.80** | **87,189,684,224.00 USD** | **5.77** |
| SPGI | 27.95 | 6.88 | 18.12 | 6.80 | 135,615,217,664.00 USD | 1.81 |
| MSCI | 33.90 | -15.24 | 25.99 | 12.40 | 46,601,428,992.00 USD | 12.03 |
| FDS | 22.50 | 5.77 | 14.26 | 6.30 | 11,564,639,232.00 USD | 31.60 |

Peers fetched as_of: 2026-11-08; MCO reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-02-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-08

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 1,142,100,000.00 USD; period 2019-01-01/2019-03-31; fiscal year/reporting period 2019/Q1
- Net income (latest available single quarter): 734,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1059556/000162828026066731/mco-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi0AFBVV95cUxQZlpzVnNJX0Nhck9qNHpERllIalJLbzY0TndiSTJSbzBvSjAxYkFWTE5vTGk0Tm5zeTZ2V2RZNkN4OU04Z2tBeWwwUGdRdmItVkMtZXJpbHpuT09qeG11bGo4Yk05VEhKQ2pyUWQ2RTBES00zMkJtSG9RN1FjdGU3MGJmNDI0UkhDd2hMUkZuQkpaV0lFNldYQ1ZvYUtDNFVoRXB4VDdqd3VQckotZUhzbzdZS3F2anVlZEpCU2lDTWc1Uk9QS2I4dnVqZXR2OWNu?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxNTnE3cFNIRm5SWVlDTU0yRmRyeVJJdGJlOGZMV3hKenVuSUc2U1Q1QmtKQjVUXzRRWkhENDkwT09HU3dhRHR1NUNjSmVvemxDRkpqNURfWEU1Q3ZlZFprYW05b2hTN2FhX0g5b3FwXzB0WTVyNGM0WXJsZEV0eldXS1h2alBnN0ZzSld2b1AxalpNeEl2YU5SLU5VdWxPODBPWkVZQjV5YlM5LTQ3QVBRV3I5WC1sZGVFMnJGYzdMQlZYeWhWaUpBSzF5RS1Rbkk3V0l3?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxOWE1rSklBa3RmcU5aSXJZanNuODZJNE9TLVlSR3kzQXk3eXV1WDBidU1EQ2lmU2FHNGFqeVh6WDVqX2NqTFU2QjlZeDI1bk1yeG4yQ3JnUGpURlQ0QVF4aWtxNXlBRy05dThQQ285NUN2WklmZnpBYWkwSGlzcGpVMnR0dVVmYjg0bzZ1S3FpcHpvd19tenBhZUdyaDA3a25NX3Q1YlhhdUVQNmFJQjZVck93?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPa1MzQUZFRTU5OVhQRnpWZS1EUTBQVC11bTh1eHh5enpFdTVYeFdkRjM5enRMSjgyU2ZzaFdlaUJyYUxQMW5BUHdNNEliZ3JkNk5wSXJSR0lfUEpGMUJQeU85NVFIRnBZa25HbW9tRVA4WndFN2NOQllEX1gyRnZUYmpRVUZJYW5KQ3p5N1F1Qzh6WjBPTEMtQUFtOGpJUkJxNGlDYWFzV0o?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxNa2NSYW1VUFE3YUFRQkU1Q19sVTNIaHVZWEhuMTlqTU9IV3hEMjJvRVhXb1R2SC13X3NJVWV3X3B0TEN6NjJtN1lFSzRsTHpUeFJjQWpVY0xta1BUNEVSRFJlTzMtN1NNUDJUVXYwQnBzblRpV0hPQ0xORjFxMG1ISzF2bEJHQ2Nha1FqM2ROUUlhc0poNmh1QjlINHlKcW9ydExQUERFQlJpdFZXQU5TdWpLa3p6SmVKeHpaOTFn?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQSlpDVG4xU3lvUXh3dnVPTUQyd0VHcGVYeUg5VEVickNfWFhMSFB2N0JLS3Rrc1VmeWh5eDY0X1RCcG94MmtTMXAybkZsUWh6RU45c3g4WVRyVENOV2YxajE5YXJOMnhlXzZSeHNXbklqcFNzSmlxUThGWE1OQjJQQVFmQWtaZlVBa0h1M1VWLTNsWmlJUkZFMmdlUXJ6cTVaN2VtNHF6bXE4cHp5WENCNE41TGRJVkQ2bVI5ZmZ1Qk0wUQ?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPd1Fhd2c3VmhwaFVlTEZQQ191c3J5M04waktmWjhibGpuYmhqTkRuQU94R2wzVzVKX1ItYUxlekVPMjFJX3I2THdsRmRhQW1OcFhRSXc3d3NNa3hsMVN2YVo1SVN5NWlaS1dsLVJ5Q1hHWUZnaldzV1VDZE53azVnQ1JwT0RMcDB0M3V4ZzJIaDBfcDZiQ3FCZ0stUkxmLXA5Tld0RXR1bGQ5UTNjalNwNUFtbXJaV0RvT0dmbmJINm5Pa3FKbGJfSjRR?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxNazJoeGhBXzVXSU5sWC1fOEVYRGFFZmMzYm4tdWRIZlA2RkpjNHBvYWdxeVk0ZmlmaFdjWlhDSlVxQ05mR3MzS0F6b3NuWkNkckx6cGw3aHNRQzZwMlp1NUpEdWoza2JVeW53WlBsSkladE9ua3VIN3dUVlVHOFV2bEVqWGFKdUJCcXA0WTBQcnN6ckt0RkhNTEtKakZMQVkwcE56Z1lXYzkwTkQ5UEhIYjdTV3p3WmQ3VVZnWm5MdkZSLUEtcHc4a1lNdw?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNazJMa0h3bUdHYUk3MmJTOGJ0WmZRV01RM3lRVjVTZTVWVWNJQWdsQS1mWE14aUIxbS01ajQ4d0twN2phdWQxOTdrLXZUVnVBSlYtd2lLRGw1cF9XSWFZZXJtaExmLXVBOXNxeFoxZWN4SGJxSk5WeXlLbERrSnVoUGF2TzBVODVTNlZrWkU4eFZNY1VqblMzdnNSN2dOS3dNdEh0cFVzR0ZuekhLUjdiT2pJV2tTTm45UEE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
