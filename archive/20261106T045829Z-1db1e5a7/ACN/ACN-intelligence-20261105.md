# ACN Intelligence Report

- ticker: **ACN**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/ACN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ACN/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:12:25.755543+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 18, 'rule': 4, 'ai': 6, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/ACN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 18 unique headlines; 11 named publishers; 0 exact duplicates; 18 HTTPS source links; largest publisher share 16.67%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 265.1600 |
| Return 1D (%) | 0.3368 |
| Return 1W (%) | 7.2567 |
| Return 1M (%) | 37.0352 |
| Return YTD (%) | 1.6754 |
| Return 1Y (%) | 10.0779 |
| Annualized volatility (%) | 49.9833 |
| Beta vs SPY | 0.0075 |
| Max drawdown (%) | -56.5068 |
| Sharpe (rf=0) | 0.4438 |
| Downside deviation (rf=0, %) | 34.6460 |
| Sortino (rf=0) | 0.6402 |
| Historical VaR 95% (1D, %) | 4.5949 |
| Historical ES 95% (1D, %) | 6.8005 |
| Correlation vs SPY | 0.0020 |
| Tracking error vs SPY (%) | 51.7720 |
| P/E (trailing) | 19.55 |
| P/B | 5.00 |
| EV/EBITDA | 11.84 |
| Revenue growth (%) | 6.20 |
| Forward P/E (estimate) | 16.69 |
| Gross margin (%) | 32.05 |
| Operating margin (%) | 17.83 |
| Return on equity (%) | 26.02 |
| Free cash flow yield (%) | 6.58 |
| MA50 | 207.8906 |
| Close vs MA50 (%) | 27.5479 |
| MA200 | 187.8465 |
| Close vs MA200 (%) | 41.1578 |
| RSI (14, Wilder) | 70.1700 |
| MACD (12,26) | 16.5568 |
| MACD signal (9) | 15.6862 |
| MACD histogram | 0.8705 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ACN': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 265.1600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.3368 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 7.2567 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 37.0352 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 1.6754 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 10.0779 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 49.9833 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.6460 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6402 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.5949 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.8005 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0020 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 51.7720 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0075 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -56.5068 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4438 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.6895 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.0500 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8280 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.0250 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.5847 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 19.5546 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 70.1700 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.8705 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 27.5479 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 41.1578 -> Clearly above the moving-average trend level.

## TAILWINDS

### Accenture PLC (ACN) Shares Surge 3.8% -- What GF Score of 94 Tel
- Summary: Accenture PLC (ACN) Shares Surge 3.8% -- What GF Score of 94 Tel
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQOEFlWW5RdW1VYWpSeEdhbHdhbldLQ1gzdi1xd3Zwcm1ackNhU3RJdWMxVHpvcWtLUkFTb25TRUZKWUwtOWp5Sm83UzdHOFhXMDBOb1pfaGhyUWRiaW1iX3lCcnhUWXRtN1RnV0JBZTFNYkpTVkl1dlZjOVc0VGhHUmRiMkpUZjRENUREck1RM1dZenIwU19MTEFZZXVPeFlYZGh0bk5STVBzQTNI?oc=5>

### Accenture PLC (ACN) Shares Surge 4.5% -- What GF Score of 91 Tel
- Summary: Accenture PLC (ACN) Shares Surge 4.5% -- What GF Score of 91 Tel
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNZlRfSHNlSTlBaWhBdkdGUjBGTmxSR1dxaExZclpvNEVuWDdKZDZmbmdyQ1U4VWQtVkFTSXdELWdSQmljQVItSmVLd0V0aTFnMTEyck9jVzBFUXBqV2s2eTZzWmhUOXdLNWM5OU8yME5sa2xDZDV3aEdNTmFObHA4TmMtV1JVN0luUFZQbFp2akk5LWZTVVU1UFg5S3R0dHp3czlfb19YM1VmWEps?oc=5>

### Analysts Lifted Accenture’s Price Targets After a 31% Rally. Did Their Earnings Estimates Move Too?
- Summary: Analysts raised price targets following a 31% rally, signaling optimism about future earnings.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPenhac3lSUElXMnFEMHQ5REY4SlhET095YmlKeFBYbDkwTDlBd2lFc0tGREZHcEpiYW40U1NuSzZqYVJMcHlKYzhObjF0aXVuRldZNHYyNEswcUkwbjFrdEQ5MFoxQnM0alBmZTBmQi1JWGZuZ1BFdkphaUpfQnhlRUhadkJ3SjNKbEtVNHVTMA?oc=5>

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

### Accenture (ACN) Sees $560 Million in Net ETF Selling on Oct. 30
- Summary: Accenture ETF shares sold $560M, indicating investor pullback.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNRnllLVVSX2k1WXdXX1dmcjI0eERpbHZLejJsM2pKS0Q5cGUxLTY2aTFDTUloV3cydXlsYkxhWEI4M0psRS1EYzRMN3hjWGZHbElEQkZrbGdTLWltcnEtX0N4WTdNb2R0Y2JYV1FOUUcxbm1CbGNGN0xLYVJBNVJ0MW9ZUk05SHNFaTk5Y2tyQWtRTGwzUGp0WVF1RQ?oc=5>

## CATALYSTS

### Accenture (ACN) Stock Looks Fairly Valued After Fresh AI Launch News
- Summary: Accenture (ACN) Stock Looks Fairly Valued After Fresh AI Launch News
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOSVVTUVJRenRtUXpyRThiN3A5X0NiZnUyTHFvZjRaNFdPa3BpMFp1M0U5cVh1Q0o4bWRKSk1pWXhkWVZGN1lCWnJSeXZuWlVaQ1V3eXhNbUxubnVJMWJzNHphZVpxMGpvQ1JOQXBFSmQ0aXZDRkNua1NTRVNiZnNiamFWR2hVaVVXQ2h4VkladENSa1hncWg3X3lCekkxZw?oc=5>

### Accenture Jumped 28% in a Month and Now Trades Above Two Analysts’ $252 Targets
- Summary: Accenture Jumped 28% in a Month and Now Trades Above Two Analysts’ $252 Targets
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOWGhub0ZBcGhTN09EdUJjTVUtZFg1Ql9LNV9WZW5UR3JqZWFmcDNRY3o5M2hhM1dfZ2xYTHQxV3dWNGNqanBrNTFlZkNCbk00WXgya1picHplUlFRa29UdzBWamkzMDRPSjZrVDlsMGtCZnZpZTcxVEJHb3F5SEtlSUF1aEdhcG5Cc0ZSQUVqbFlDZWdpX0d2VV9ER2xVRGR2ZVJuOQ?oc=5>

### At $270 a share, Accenture (ACN) Asia Pacific co-CEO sells 10,000 shares.
- Summary: Co‑CEO of Accenture’s Asia Pacific unit sold 10,000 shares at $270 each, an insider transaction indicating personal portfolio activity.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOajBTT2t2eTN2X2drQ2RsRWtUWnBVaW5xcmxrSjdoNkJnejJSQ3FfekJpMlRkVjNBOTFwRG1NTnAxa1ZyWnFfUFNkRFMyUE4zZENQOUQ1ZDlBcDBaNXhDbWh2N21RVDgyU05IQzJZTDQ1UnlYV3JTV01iTXNxNnJYVWpneVhWREVONFBOTHF6T3QwRjRLY2ZjRVhaS2F3TXR0TTNJam45ZGhmQQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ACN** | **19.55** | **5.00** | **11.84** | **6.20** | **162,262,564,864.00 USD** | **10.08** |
| IBM | 21.08 | 6.57 | 17.45 | 4.70 | 233,548,808,192.00 USD | -17.35 |
| CTSH | 12.01 | 2.02 | 7.38 | 4.60 | 29,745,405,952.00 USD | -8.86 |
| INFY | 15.06 | 10.04 | 20.55 | 1.40 | 51,844,820,992.00 USD | -20.36 |

Peers fetched as_of: 2026-11-05; ACN reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-01
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
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
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNZlRfSHNlSTlBaWhBdkdGUjBGTmxSR1dxaExZclpvNEVuWDdKZDZmbmdyQ1U4VWQtVkFTSXdELWdSQmljQVItSmVLd0V0aTFnMTEyck9jVzBFUXBqV2s2eTZzWmhUOXdLNWM5OU8yME5sa2xDZDV3aEdNTmFObHA4TmMtV1JVN0luUFZQbFp2akk5LWZTVVU1UFg5S3R0dHp3czlfb19YM1VmWEps?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPenhac3lSUElXMnFEMHQ5REY4SlhET095YmlKeFBYbDkwTDlBd2lFc0tGREZHcEpiYW40U1NuSzZqYVJMcHlKYzhObjF0aXVuRldZNHYyNEswcUkwbjFrdEQ5MFoxQnM0alBmZTBmQi1JWGZuZ1BFdkphaUpfQnhlRUhadkJ3SjNKbEtVNHVTMA?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOT1ZmaHVvYVhiUHNncFhEcTZSUGxCeERXZXlSbHNOR2FZNkFCOFJFU2o2eGE1b0FVczJfWHBTR012bndna2JOYTFQSzMxTHFQUXFjekVvWmt1QU9SNGNsa25rbUxrMjNwZGU0NTIyVmhkRFpwUW1PNC1UR1VrRlBibHdvV2tqaGFoMnc?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQdUFOYzNQX293cDlSdkxMTzE0S0J1SmlPdFZ3UEduNnZUNmFGdWxEVVlkUHpvajNJMVJqakVId0l0YkxQR0tvX25Ib0h6XzI4RU5QekZJX1ZHSDdCQ2pNUE80dkpxX3pJSUJvay1vMnNpT3d5ZExVTjNCVEJfUXZRcGZqM0h1RVZZcXlDalRNTWRlMVRGWlRZaS0ycFJGc3Q5TWRRRU4zdkhWVGNSLVE?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxOLUtGWUg5NGN1NEsxUmNPejhnUW8tanFONFdtZnBYOXVLWjhsYXVCQ2ZHRHQ1cTBpQUVrLXhhcDg1X2ZBOVYzQXp1WUl3UF9WTlJMVjBCdXRlMjgzb3lpbHFhNDRzOXNSME9lVlhDNUtZbEh0Rm5OZGt3bjIxZ1FXbE1NR2RsWURnR2VYUFQ2THdJQmdUOXBtSzZrNmZGblEzYzNiYkoxS3hCVWxldUJhdg?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNRnllLVVSX2k1WXdXX1dmcjI0eERpbHZLejJsM2pKS0Q5cGUxLTY2aTFDTUloV3cydXlsYkxhWEI4M0psRS1EYzRMN3hjWGZHbElEQkZrbGdTLWltcnEtX0N4WTdNb2R0Y2JYV1FOUUcxbm1CbGNGN0xLYVJBNVJ0MW9ZUk05SHNFaTk5Y2tyQWtRTGwzUGp0WVF1RQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOSVVTUVJRenRtUXpyRThiN3A5X0NiZnUyTHFvZjRaNFdPa3BpMFp1M0U5cVh1Q0o4bWRKSk1pWXhkWVZGN1lCWnJSeXZuWlVaQ1V3eXhNbUxubnVJMWJzNHphZVpxMGpvQ1JOQXBFSmQ0aXZDRkNua1NTRVNiZnNiamFWR2hVaVVXQ2h4VkladENSa1hncWg3X3lCekkxZw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOWGhub0ZBcGhTN09EdUJjTVUtZFg1Ql9LNV9WZW5UR3JqZWFmcDNRY3o5M2hhM1dfZ2xYTHQxV3dWNGNqanBrNTFlZkNCbk00WXgya1picHplUlFRa29UdzBWamkzMDRPSjZrVDlsMGtCZnZpZTcxVEJHb3F5SEtlSUF1aEdhcG5Cc0ZSQUVqbFlDZWdpX0d2VV9ER2xVRGR2ZVJuOQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOajBTT2t2eTN2X2drQ2RsRWtUWnBVaW5xcmxrSjdoNkJnejJSQ3FfekJpMlRkVjNBOTFwRG1NTnAxa1ZyWnFfUFNkRFMyUE4zZENQOUQ1ZDlBcDBaNXhDbWh2N21RVDgyU05IQzJZTDQ1UnlYV3JTV01iTXNxNnJYVWpneVhWREVONFBOTHF6T3QwRjRLY2ZjRVhaS2F3TXR0TTNJam45ZGhmQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
