# ACN Intelligence Report

- ticker: **ACN**
- Report as_of: **2026-11-06**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/ACN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ACN/key-statistics/
- AI analysis snapshot as_of: **2026-11-06**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-07T04:36:33.262018+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 14, 'rule': 3, 'ai': 7, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261106T045829Z-1db1e5a7/ACN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 14 unique headlines; 9 named publishers; 0 exact duplicates; 14 HTTPS source links; largest publisher share 21.43%; oldest publication 2026-10-30

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 260.5000 |
| Return 1D (%) | -1.7574 |
| Return 1W (%) | 0.8752 |
| Return 1M (%) | 35.7755 |
| Return YTD (%) | -0.1115 |
| Return 1Y (%) | 11.0470 |
| Annualized volatility (%) | 49.9440 |
| Beta vs SPY | -0.0117 |
| Max drawdown (%) | -56.5068 |
| Sharpe (rf=0) | 0.4614 |
| Downside deviation (rf=0, %) | 34.5916 |
| Sortino (rf=0) | 0.6661 |
| Historical VaR 95% (1D, %) | 4.5949 |
| Historical ES 95% (1D, %) | 6.8005 |
| Correlation vs SPY | -0.0032 |
| Tracking error vs SPY (%) | 51.7911 |
| P/E (trailing) | 19.21 |
| P/B | 4.91 |
| EV/EBITDA | 11.63 |
| Revenue growth (%) | 6.20 |
| Forward P/E (estimate) | 16.40 |
| Gross margin (%) | 32.05 |
| Operating margin (%) | 17.83 |
| Return on equity (%) | 26.02 |
| Free cash flow yield (%) | 6.94 |
| MA50 | 209.3828 |
| Close vs MA50 (%) | 24.4133 |
| MA200 | 187.7634 |
| Close vs MA200 (%) | 38.7384 |
| RSI (14, Wilder) | 66.2900 |
| MACD (12,26) | 16.1203 |
| MACD signal (9) | 15.7730 |
| MACD histogram | 0.3473 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ACN': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 260.5000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.7574 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.8752 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 35.7755 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -0.1115 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 11.0470 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 49.9440 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.5916 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6661 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.5949 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.8005 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0032 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 51.7911 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0117 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -56.5068 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4614 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.3962 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.0500 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8280 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.0250 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.9431 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 19.2109 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 66.2900 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3473 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 24.4133 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 38.7384 -> Clearly above the moving-average trend level.

## TAILWINDS

### Accenture PLC (ACN) Shares Surge 3.8% -- What GF Score of 94 Tel
- Summary: Accenture PLC (ACN) Shares Surge 3.8% -- What GF Score of 94 Tel
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQOEFlWW5RdW1VYWpSeEdhbHdhbldLQ1gzdi1xd3Zwcm1ackNhU3RJdWMxVHpvcWtLUkFTb25TRUZKWUwtOWp5Sm83UzdHOFhXMDBOb1pfaGhyUWRiaW1iX3lCcnhUWXRtN1RnV0JBZTFNYkpTVkl1dlZjOVc0VGhHUmRiMkpUZjRENUREck1RM1dZenIwU19MTEFZZXVPeFlYZGh0bk5STVBzQTNI?oc=5>

### Accenture PLC Stock (ACN) Closed Up by 4.46% on Oct 30: Facts Behind the Movement
- Summary: Accenture shares closed 4.46% higher on Oct 30, indicating a positive price movement.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOT1ZmaHVvYVhiUHNncFhEcTZSUGxCeERXZXlSbHNOR2FZNkFCOFJFU2o2eGE1b0FVczJfWHBTR012bndna2JOYTFQSzMxTHFQUXFjekVvWmt1QU9SNGNsa25rbUxrMjNwZGU0NTIyVmhkRFpwUW1PNC1UR1VrRlBibHdvV2tqaGFoMnc?oc=5>

### Is Accenture (NYSE:ACN) Proving AI Demand With Record Large Bookings?
- Summary: Record large bookings indicate strong AI demand, boosting Accenture’s revenue outlook.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQdUFOYzNQX293cDlSdkxMTzE0S0J1SmlPdFZ3UEduNnZUNmFGdWxEVVlkUHpvajNJMVJqakVId0l0YkxQR0tvX25Ib0h6XzI4RU5QekZJX1ZHSDdCQ2pNUE80dkpxX3pJSUJvay1vMnNpT3d5ZExVTjNCVEJfUXZRcGZqM0h1RVZZcXlDalRNTWRlMVRGWlRZaS0ycFJGc3Q5TWRRRU4zdkhWVGNSLVE?oc=5>

### Is Accenture (NYSE:ACN) Poised for Another Rally After Its AI Launch?
- Summary: Accenture may see another rally post AI launch, suggesting market optimism.
- Date: 2026-11-01 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxOLUtGWUg5NGN1NEsxUmNPejhnUW8tanFONFdtZnBYOXVLWjhsYXVCQ2ZHRHQ1cTBpQUVrLXhhcDg1X2ZBOVYzQXp1WUl3UF9WTlJMVjBCdXRlMjgzb3lpbHFhNDRzOXNSME9lVlhDNUtZbEh0Rm5OZGt3bjIxZ1FXbE1NR2RsWURnR2VYUFQ2THdJQmdUOXBtSzZrNmZGblEzYzNiYkoxS3hCVWxldUJhdg?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Accenture (ACN) Stock Looks Fairly Valued After Fresh AI Launch News
- Summary: Accenture (ACN) Stock Looks Fairly Valued After Fresh AI Launch News
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOSVVTUVJRenRtUXpyRThiN3A5X0NiZnUyTHFvZjRaNFdPa3BpMFp1M0U5cVh1Q0o4bWRKSk1pWXhkWVZGN1lCWnJSeXZuWlVaQ1V3eXhNbUxubnVJMWJzNHphZVpxMGpvQ1JOQXBFSmQ0aXZDRkNua1NTRVNiZnNiamFWR2hVaVVXQ2h4VkladENSa1hncWg3X3lCekkxZw?oc=5>

### Accenture Jumped 28% in a Month and Now Trades Above Two Analysts’ $252 Targets
- Summary: Accenture Jumped 28% in a Month and Now Trades Above Two Analysts’ $252 Targets
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOWGhub0ZBcGhTN09EdUJjTVUtZFg1Ql9LNV9WZW5UR3JqZWFmcDNRY3o5M2hhM1dfZ2xYTHQxV3dWNGNqanBrNTFlZkNCbk00WXgya1picHplUlFRa29UdzBWamkzMDRPSjZrVDlsMGtCZnZpZTcxVEJHb3F5SEtlSUF1aEdhcG5Cc0ZSQUVqbFlDZWdpX0d2VV9ER2xVRGR2ZVJuOQ?oc=5>

### What Just Happened To Accenture Stock?
- Summary: Accenture stock experienced a significant price movement, prompting analysis of underlying causes.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPUGtxMTlQOFlRY3AwT1NsWXNFUl9EQkJfUThiZS1LUjcyRWhJX1FhZm9QLXdwU3UySjZhRzdQRVlnSkQ1ZjE2c1FaUC1La1VVeWF1blVnSzhvaW1lZ1ZKZ0VZMzZBcDVmeGF2VHlnc3Z3MnlvOEFmMXo1MXdQSE1PV3g2YWZDWEp4LVNwcU03b24tQjl6aXphSUNsbDRPZw?oc=5>

### Zacks Investment Ideas feature highlights: Lockheed Martin, Accenture and Nucor
- Summary: Zacks highlighted Accenture among top investment ideas, indicating analyst interest.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOenU1UkJHdEZCTUZ2cy1UMUtLQnowbWw4S19pVXhVWHQ5SkJ6QUFYa29RaEhYU0xVNGxHdUh6eTE3RFZlZnM1ZGd2ZVphT01yblhrTGJyQmdfdXBFdGhkZUJjSjZaVTRoRldLY0ZVZXVoT2h3TlFwZ0pINGZlRmNIODBVdm5waDNBVlNXWDItdXF2cjlxd1hRVkRrSzU3YnhVdXBsdkJtS25KUQ?oc=5>

### Accenture vs. Microsoft: Which Technology Stock Is a Better Buy for 2027?
- Summary: Analyst comparison of Accenture and Microsoft for 2027 investment prospects.
- Date: 2026-11-02 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOLVZIWG9OSXhzRHl0UzBfbmVyY2lpSkhyUDMybkM5WVIzc2o5Qk9GM0dLSDc4dFhjTF91WU5nRGdHaWE5TWdRV1R1YUoxcTBBR01QQnBhT1hCbmQ4N3dkaGdmMmxhLThyWnlLTzZVMHpwSE0xNWVJcWUwdzlnRjdGMmw0VV9EV1BTbWpNQlNVcUNyNFpjZ3p0ejlIei05OXMzTFJueTBPaHB2ODBudTcwMTNyV3dsLWJ3dDNXNlZhdGs?oc=5>

### Analysts Lifted Accenture’s Price Targets After a 31% Rally. Did Their Earnings Estimates Move Too?
- Summary: Analysts raised price targets for Accenture following a rally, questioning earnings estimates.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPX0JMRkJCSF9BY0J6NmhKRjdPSGxORzZDR1BhN25pd2dONm4tV2tETHpjQ25hcUtqVU9wMUxITHlRam5OVEszc3JHemlIcWU3U2ZDYTNab21fT3FqcklGaGRFMEZoT3g0MGdPRGlablo4TWJCaW9aQXhnYkV0YkdTLVJLZ243NXpmVU5QRzd3?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ACN** | **19.21** | **4.91** | **11.63** | **6.20** | **153,887,113,216.00 USD** | **11.05** |
| IBM | 20.90 | 6.52 | 17.33 | 4.70 | 231,554,596,864.00 USD | -19.54 |
| CTSH | 12.14 | 1.97 | 7.19 | 4.60 | 28,931,809,280.00 USD | -9.13 |
| INFY | 15.43 | 9.80 | 20.05 | 1.40 | 50,629,705,728.00 USD | -21.07 |

Peers fetched as_of: 2026-11-06; ACN reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-01
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-06

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-16
- Revenue (latest available single quarter): 18,679,110,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- Net income (latest available single quarter): 1,991,267,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- SEC link: https://www.sec.gov/Archives/edgar/data/1467373/000146737326000049/acn-20260831.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMirAFBVV95cUxQOEFlWW5RdW1VYWpSeEdhbHdhbldLQ1gzdi1xd3Zwcm1ackNhU3RJdWMxVHpvcWtLUkFTb25TRUZKWUwtOWp5Sm83UzdHOFhXMDBOb1pfaGhyUWRiaW1iX3lCcnhUWXRtN1RnV0JBZTFNYkpTVkl1dlZjOVc0VGhHUmRiMkpUZjRENUREck1RM1dZenIwU19MTEFZZXVPeFlYZGh0bk5STVBzQTNI?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOT1ZmaHVvYVhiUHNncFhEcTZSUGxCeERXZXlSbHNOR2FZNkFCOFJFU2o2eGE1b0FVczJfWHBTR012bndna2JOYTFQSzMxTHFQUXFjekVvWmt1QU9SNGNsa25rbUxrMjNwZGU0NTIyVmhkRFpwUW1PNC1UR1VrRlBibHdvV2tqaGFoMnc?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQdUFOYzNQX293cDlSdkxMTzE0S0J1SmlPdFZ3UEduNnZUNmFGdWxEVVlkUHpvajNJMVJqakVId0l0YkxQR0tvX25Ib0h6XzI4RU5QekZJX1ZHSDdCQ2pNUE80dkpxX3pJSUJvay1vMnNpT3d5ZExVTjNCVEJfUXZRcGZqM0h1RVZZcXlDalRNTWRlMVRGWlRZaS0ycFJGc3Q5TWRRRU4zdkhWVGNSLVE?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxOLUtGWUg5NGN1NEsxUmNPejhnUW8tanFONFdtZnBYOXVLWjhsYXVCQ2ZHRHQ1cTBpQUVrLXhhcDg1X2ZBOVYzQXp1WUl3UF9WTlJMVjBCdXRlMjgzb3lpbHFhNDRzOXNSME9lVlhDNUtZbEh0Rm5OZGt3bjIxZ1FXbE1NR2RsWURnR2VYUFQ2THdJQmdUOXBtSzZrNmZGblEzYzNiYkoxS3hCVWxldUJhdg?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOSVVTUVJRenRtUXpyRThiN3A5X0NiZnUyTHFvZjRaNFdPa3BpMFp1M0U5cVh1Q0o4bWRKSk1pWXhkWVZGN1lCWnJSeXZuWlVaQ1V3eXhNbUxubnVJMWJzNHphZVpxMGpvQ1JOQXBFSmQ0aXZDRkNua1NTRVNiZnNiamFWR2hVaVVXQ2h4VkladENSa1hncWg3X3lCekkxZw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOWGhub0ZBcGhTN09EdUJjTVUtZFg1Ql9LNV9WZW5UR3JqZWFmcDNRY3o5M2hhM1dfZ2xYTHQxV3dWNGNqanBrNTFlZkNCbk00WXgya1picHplUlFRa29UdzBWamkzMDRPSjZrVDlsMGtCZnZpZTcxVEJHb3F5SEtlSUF1aEdhcG5Cc0ZSQUVqbFlDZWdpX0d2VV9ER2xVRGR2ZVJuOQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPUGtxMTlQOFlRY3AwT1NsWXNFUl9EQkJfUThiZS1LUjcyRWhJX1FhZm9QLXdwU3UySjZhRzdQRVlnSkQ1ZjE2c1FaUC1La1VVeWF1blVnSzhvaW1lZ1ZKZ0VZMzZBcDVmeGF2VHlnc3Z3MnlvOEFmMXo1MXdQSE1PV3g2YWZDWEp4LVNwcU03b24tQjl6aXphSUNsbDRPZw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOenU1UkJHdEZCTUZ2cy1UMUtLQnowbWw4S19pVXhVWHQ5SkJ6QUFYa29RaEhYU0xVNGxHdUh6eTE3RFZlZnM1ZGd2ZVphT01yblhrTGJyQmdfdXBFdGhkZUJjSjZaVTRoRldLY0ZVZXVoT2h3TlFwZ0pINGZlRmNIODBVdm5waDNBVlNXWDItdXF2cjlxd1hRVkRrSzU3YnhVdXBsdkJtS25KUQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOLVZIWG9OSXhzRHl0UzBfbmVyY2lpSkhyUDMybkM5WVIzc2o5Qk9GM0dLSDc4dFhjTF91WU5nRGdHaWE5TWdRV1R1YUoxcTBBR01QQnBhT1hCbmQ4N3dkaGdmMmxhLThyWnlLTzZVMHpwSE0xNWVJcWUwdzlnRjdGMmw0VV9EV1BTbWpNQlNVcUNyNFpjZ3p0ejlIei05OXMzTFJueTBPaHB2ODBudTcwMTNyV3dsLWJ3dDNXNlZhdGs?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPX0JMRkJCSF9BY0J6NmhKRjdPSGxORzZDR1BhN25pd2dONm4tV2tETHpjQ25hcUtqVU9wMUxITHlRam5OVEszc3JHemlIcWU3U2ZDYTNab21fT3FqcklGaGRFMEZoT3g0MGdPRGlablo4TWJCaW9aQXhnYkV0YkdTLVJLZ243NXpmVU5QRzd3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
