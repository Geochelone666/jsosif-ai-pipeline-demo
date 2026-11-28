# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:32:25.141880+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 1, 'ai': 5, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/T** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 7 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 36.36%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 23.2100 |
| Return 1D (%) | 1.0448 |
| Return 1W (%) | 4.0341 |
| Return 1M (%) | 10.8405 |
| Return YTD (%) | -2.1038 |
| Return 1Y (%) | -5.8195 |
| Annualized volatility (%) | 28.8253 |
| Beta vs SPY | -0.3166 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.0911 |
| Downside deviation (rf=0, %) | 22.0019 |
| Sortino (rf=0) | -0.1194 |
| Historical VaR 95% (1D, %) | 2.8611 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1650 |
| Tracking error vs SPY (%) | 34.6329 |
| P/E (trailing) | 12.41 |
| P/B | 1.47 |
| EV/EBITDA | 7.49 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.94 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 22.59 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 7.65 |
| MA50 | 22.8685 |
| Close vs MA50 (%) | 1.4932 |
| MA200 | 24.2259 |
| Close vs MA200 (%) | -4.1935 |
| RSI (14, Wilder) | 61.7302 |
| MACD (12,26) | 0.0636 |
| MACD signal (9) | -0.1449 |
| MACD histogram | 0.2085 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 23.2100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.0448 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.0341 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 10.8405 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -2.1038 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -5.8195 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.8253 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.0019 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.1194 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8611 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1650 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.6329 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3166 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0911 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.9414 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 22.5930 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.6504 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 12.4118 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 61.7302 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2085 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.4932 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -4.1935 -> Slightly below the moving-average trend level.

## TAILWINDS

### AT&T (NYSE:T) Stock Jumps 2.6% - Here's Why
- Summary: AT&T (NYSE:T) Stock Jumps 2.6% - Here's Why
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQX2dsLUV0TnpEdGFaTTUtb1d1RGVSdWV3ZzEyVzFURG1SWGlINmtCOWRYMVZnOV9od1JybXBjbkp1M3hkd0ZybVJxSWx1Q0ZPX0ZXR1pTQjZ2UGEwNkJwczhuNzFja2REM0RGVnhvUkl3UUlqaHNEay1EZlJVdHpBa1ZkWFRMM0piWUpNa3FvZFlwX1hSNldZOEFOOA?oc=5>

### AT&T(T) Stock Price Today | Quotes & News
- Summary: AT&T shares rise today, reflecting positive market sentiment.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi9gJBVV95cUxPb0Nic3c4OFVpZmRzWGJWUW1KY2pCZE5wekhZSENjVDdDczhRekVaRFYtemV5aFlNekRkMndpMlk1bzZLQ092N1FuLUdJdHR4S0hSVzNiaDB5QlBHdC1ZbHNtT2Nidy1HcUR4TjdTeld3SzZYaW5JYVh2bjhqT0lkd1o4d2ZIbkt2bllvY2JHWmo0dGNkOFVDemR3TTJWS1NXM25qdU9KT0ZZdlhzTDQtRlpyOENqY09mS1RsdjJNQ3FadUdpbXFGRXY2aEtBMEM1S1F2OFdMcGZ2U3dweVBTUmk5VHZxSVZNYVJyc2pVRHhlRlc5NHo0eWFxR21vNTI5dnc2ZllOdTdtcDJMbXVEMkFHM3Buek93MG02ZEdRUHhQTklMSGtjVU0xNVZ6VG5SdmdCMm9feGxKYzB5aTFoSTlraGtwaExnOUM4dXZfUTM5cmp3T3REU1VGcFg0T0tnQk1QYXNhemxBekZ2dmlJbDVzR29fQQ?oc=5>

### AT&T Is Up 10% in a Month. Steve Eisman Calls the Big Three Carriers “Uninvestable.” Who’s Right?
- Summary: AT&T stock gains 10% monthly, despite analyst skepticism.
- Date: 2026-11-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxPdC1POUZpQnM4WWVoTmctMk1Ray1jZ0ZlYnVNcWdPYi12aXVVM3UwZlFDQXVXYVBDNDVtXzJHVUpYLTBfN205MkIzM1ZDczNSUnN1ckVrMjNjSGI0emlDZHNuZlZkYUtGZ1hKTWdCbW9sLU9na3RDY094U0NkcHBsREVTWnRiUU9zZldLSk1Vek03cUE5M1Z2V2pWZXVZaFVkOEVuM1hjS2pNSVd0aG1BNzVyQmowbjlmODJvMmxheE1Rc25helR5UVNuRnYzUFh5V201Sm5FdEFNcXhDclVVamVMZ1hCamx6UkJyMg?oc=5>

## HEADWINDS

### AT&T (T) Stock Could Trade Below Fair Value Even Now
- Summary: AT&T stock may be undervalued, suggesting potential downside risk for investors.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQdUxaQ2tPUG0zNGxhVUpYbHdIbEEyZ25RdXNvOTBMZzN5aVhjbER6SWdueVNHa3NOQXRkNFhkc2RwU0tzMVBORG9QamFOeEVYNEZTTjE3OVhtUmUzWTVBcUt5MjZOUFB6OVVNc2tZazNrY0JPUC1CTmtlUTdpTDNGb0xDeFpwNjA3RF9PYk04cw?oc=5>

## CATALYSTS

### What Could Surprise AT&T Stock Investors On The Upside?
- Summary: Potential upside factors could positively influence AT&T stock, though specifics remain unclear.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQME9kTmY2N0haSHE2RXhlWFN0bjk0OVp6RWhvbjAtSVFBd21lVVBGTGNIaVJwLTFkQ2FhemVQWU9mbWl2dm1TTmN4UmlfOGFZN1VXWU9yb2ZURUNVbmRjc1FtejNrRXVNb191ck9VYWotRW5tNXNNUV96SENQeHpIRVYtZlVra29yTzRYQ3VjZEkzcWl4a1JqclRLVjlFNjg2OFp0anhOVG1ZeEc1dHpUXw?oc=5>

### Will Subscriber Growth Change AT&T Stock Narrative
- Summary: Subscriber growth trends may shift investor perception of AT&T’s future performance.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQU0JZZF9uZlhLcUVkRlN6WWh2RW8yemdjV1hFWk1Dem1zVjZ3TVRYU3g3RGhENkhjU2dyb2h6SFN2TV9vSHhaa1FuMVd5RlJsN095Q3JjdE1oekFna21Ka0JPTUZJWURQTGFXbDd2eklmMHJtV2NSVEtacWRwSzVmYmlhVGx2TFNHYlNpS3oxQkN0RHYxMEQtbGxVT3I5QQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **12.41** | **1.47** | **7.49** | **5.30** | **156,353,544,192.00 USD** | **-5.82** |
| VZ | 12.13 | 1.86 | 7.47 | 1.50 | 197,034,213,376.00 USD | 24.03 |
| TMUS | 16.41 | 3.21 | 8.30 | 7.40 | 180,277,608,448.00 USD | -15.76 |
| BCE | 11.85 | 1.37 | 7.41 | 2.20 | 20,440,965,120.00 USD | -0.45 |

Peers fetched as_of: 2026-11-27; T reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 32,322,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 891,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/732717/000073271726000372/t-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxQX2dsLUV0TnpEdGFaTTUtb1d1RGVSdWV3ZzEyVzFURG1SWGlINmtCOWRYMVZnOV9od1JybXBjbkp1M3hkd0ZybVJxSWx1Q0ZPX0ZXR1pTQjZ2UGEwNkJwczhuNzFja2REM0RGVnhvUkl3UUlqaHNEay1EZlJVdHpBa1ZkWFRMM0piWUpNa3FvZFlwX1hSNldZOEFOOA?oc=5
- https://news.google.com/rss/articles/CBMi9gJBVV95cUxPb0Nic3c4OFVpZmRzWGJWUW1KY2pCZE5wekhZSENjVDdDczhRekVaRFYtemV5aFlNekRkMndpMlk1bzZLQ092N1FuLUdJdHR4S0hSVzNiaDB5QlBHdC1ZbHNtT2Nidy1HcUR4TjdTeld3SzZYaW5JYVh2bjhqT0lkd1o4d2ZIbkt2bllvY2JHWmo0dGNkOFVDemR3TTJWS1NXM25qdU9KT0ZZdlhzTDQtRlpyOENqY09mS1RsdjJNQ3FadUdpbXFGRXY2aEtBMEM1S1F2OFdMcGZ2U3dweVBTUmk5VHZxSVZNYVJyc2pVRHhlRlc5NHo0eWFxR21vNTI5dnc2ZllOdTdtcDJMbXVEMkFHM3Buek93MG02ZEdRUHhQTklMSGtjVU0xNVZ6VG5SdmdCMm9feGxKYzB5aTFoSTlraGtwaExnOUM4dXZfUTM5cmp3T3REU1VGcFg0T0tnQk1QYXNhemxBekZ2dmlJbDVzR29fQQ?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxPdC1POUZpQnM4WWVoTmctMk1Ray1jZ0ZlYnVNcWdPYi12aXVVM3UwZlFDQXVXYVBDNDVtXzJHVUpYLTBfN205MkIzM1ZDczNSUnN1ckVrMjNjSGI0emlDZHNuZlZkYUtGZ1hKTWdCbW9sLU9na3RDY094U0NkcHBsREVTWnRiUU9zZldLSk1Vek03cUE5M1Z2V2pWZXVZaFVkOEVuM1hjS2pNSVd0aG1BNzVyQmowbjlmODJvMmxheE1Rc25helR5UVNuRnYzUFh5V201Sm5FdEFNcXhDclVVamVMZ1hCamx6UkJyMg?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQdUxaQ2tPUG0zNGxhVUpYbHdIbEEyZ25RdXNvOTBMZzN5aVhjbER6SWdueVNHa3NOQXRkNFhkc2RwU0tzMVBORG9QamFOeEVYNEZTTjE3OVhtUmUzWTVBcUt5MjZOUFB6OVVNc2tZazNrY0JPUC1CTmtlUTdpTDNGb0xDeFpwNjA3RF9PYk04cw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQME9kTmY2N0haSHE2RXhlWFN0bjk0OVp6RWhvbjAtSVFBd21lVVBGTGNIaVJwLTFkQ2FhemVQWU9mbWl2dm1TTmN4UmlfOGFZN1VXWU9yb2ZURUNVbmRjc1FtejNrRXVNb191ck9VYWotRW5tNXNNUV96SENQeHpIRVYtZlVra29yTzRYQ3VjZEkzcWl4a1JqclRLVjlFNjg2OFp0anhOVG1ZeEc1dHpUXw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQU0JZZF9uZlhLcUVkRlN6WWh2RW8yemdjV1hFWk1Dem1zVjZ3TVRYU3g3RGhENkhjU2dyb2h6SFN2TV9vSHhaa1FuMVd5RlJsN095Q3JjdE1oekFna21Ka0JPTUZJWURQTGFXbDd2eklmMHJtV2NSVEtacWRwSzVmYmlhVGx2TFNHYlNpS3oxQkN0RHYxMEQtbGxVT3I5QQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
