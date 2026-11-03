# XYL Intelligence Report

- ticker: **XYL**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/XYL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/XYL/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:29:32.665107+00:00**
- AI status: **Partial: 5 headlines remain unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 9, 'ai': 7, 'unknown': 5, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/XYL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 7 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 58.33%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 97.2600 |
| Return 1D (%) | 5.2597 |
| Return 1W (%) | -10.1441 |
| Return 1M (%) | -4.4503 |
| Return YTD (%) | -27.7829 |
| Return 1Y (%) | -34.6216 |
| Annualized volatility (%) | 30.1584 |
| Beta vs SPY | 0.6203 |
| Max drawdown (%) | -40.8719 |
| Sharpe (rf=0) | -1.2254 |
| Downside deviation (rf=0, %) | 25.0990 |
| Sortino (rf=0) | -1.4724 |
| Historical VaR 95% (1D, %) | 3.0033 |
| Historical ES 95% (1D, %) | 5.0991 |
| Correlation vs SPY | 0.2637 |
| Tracking error vs SPY (%) | 29.4950 |
| P/E (trailing) | 21.57 |
| P/B | 2.18 |
| EV/EBITDA | 12.65 |
| Revenue growth (%) | -3.00 |
| Forward P/E (estimate) | 16.49 |
| Gross margin (%) | 39.32 |
| Operating margin (%) | 15.95 |
| Return on equity (%) | 9.76 |
| Free cash flow yield (%) | 5.43 |
| MA50 | 104.6806 |
| Close vs MA50 (%) | -7.0888 |
| MA200 | 116.4397 |
| Close vs MA200 (%) | -16.4718 |
| RSI (14, Wilder) | 43.1557 |
| MACD (12,26) | -2.9181 |
| MACD signal (9) | -1.9018 |
| MACD histogram | -1.0163 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'XYL': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 97.2600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 5.2597 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -10.1441 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -4.4503 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -27.7829 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -34.6216 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.1584 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.0990 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.4724 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0033 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.0991 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2637 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.4950 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6203 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -40.8719 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.2254 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.4864 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 39.3200 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.9470 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.7560 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.4265 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.5654 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.1557 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.0163 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.0888 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -16.4718 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Xylem (XYL) Stock Price Sinks After Q3 Results Miss Revenue Mark
- Summary: Xylem (XYL) Stock Price Sinks After Q3 Results Miss Revenue Mark
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPS29KYkJVWWVPeFBtY1BpLVdLMU9xZ3VySUswRmExTmM2NzhKVmVWd0s3bGVlWkZ5TVFEOUQ1WktuR3poclBXSk8yQ0ZBZDlMalR2TUhham9HWkM4cmk0ZjdGZ2ZBa1JnNkFzU09Bb3lMdWJ2aktwelgzWTdYNWI0d000b2REZDlFYWtSWW5Iakp1VldNLXg0?oc=5>

### Xylem plunges to 3-yr low as earnings miss, outlook cut (XYL:NYSE)
- Summary: Xylem plunges to 3-yr low as earnings miss, outlook cut (XYL:NYSE)
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQRE91WmRwR0FvYVhOWHZkejQzVHNhLTNDV2tHVEZxT1Z2Y19Ld1dqSVlYWGlfWlF4N3VhcFB6SUtkQkpRRnNNel82Sm9KVGpZVE5rUEVJTnIxcGtOSU5QREFvZXFsVTFSZWFRRlJ6Z2hiWVNVUVhzRGJYakNYZTJCbVgzS3JLR0dHNTF2NUtVZGlVTzFhc19v?oc=5>

### Xylem Q3 Earnings Miss Estimates on Soft Metering and Projects
- Summary: Xylem Q3 Earnings Miss Estimates on Soft Metering and Projects
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNWTlNZ0Y2alE4VXhtVzI5Tm5MZENtVk1NZHR6TGZmWlhEbWdZSDNJRjJ1VlBmVlFEeUdXT2dmc09nT2ZiWGVXVHVRTTc4V2RYU3dXYy1hbGpRc3B3V3BhMnZ6aHJyNFQtbmpIUFV3TDA0cm1kU3RqV3hUeWkzNDJISFhnVjNITG9fcUo4ejN5SUpWLWJvMVNUOGNqOEJ2dw?oc=5>

### Xylem (NYSE:XYL) misses Q3 2026 revenue estimates, stock drops
- Summary: Xylem (NYSE:XYL) misses Q3 2026 revenue estimates, stock drops
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxORjUyLTdIXzc4b2VWRjVZRGk4VVFmU041V2hfQ0ZMdFc0TkJXLW1sX05HRXFGZ0VnZWU5Vm9uWmYwR2NzaGhpS2pGTmZMR24wLU9IVnBHSXRkMzBScnRTd0tGa2NjU3IyWWdDaDZIb2JSNERiYWpxcXo4YXdyYTVUSHRsSTlFSnNwUUF0LUpHeGtwbzQ?oc=5>

### Xylem tumbles 14% to new 52-week low after earnings miss (XYL:NYSE)
- Summary: Xylem tumbles 14% to new 52-week low after earnings miss (XYL:NYSE)
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQOWVBOEdiajVsWW1wc1RNRjNmVDhZdU1Kb3JWMjBQQ2V1V3lhclJ3eTYxTllRcm1UZ2hhdkR2V3BtSzZoNlhYZDNBYTFRamhleF9zYnI5NEp1bEY1MnBfeTRDdEVFWEY5WnJMQXRHZmFsX2phNWktTm02RFVaRFZCMW83Szh2ck5ObDlsYmFmWV9Gb25RTVd1Sg?oc=5>

### Xylem (XYL) Misses Q3 Earnings and Revenue Estimates
- Summary: Xylem (XYL) Misses Q3 Earnings and Revenue Estimates
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQOW9ZdEdTLUg1bWpxZnlpRkVjVWhFQS1lR2EzUW5vQXE3OXRJZ05QMjFTR3VTM0k5RVFJckhpUVJna1ZrQU9OOER6eDh1cVN5QnpOUVBwdEQxeTJKUVVhcW1IeHlZVFlEYnh6YldqREszRndfRF9YYmZIelV5M0tiU0wwM01CaDVLREJwSWJnVFJqaVNBZ0J5cA?oc=5>

### Xylem: Near Term Headwinds Are Real, But So Is The Overreaction
- Summary: Near-term headwinds confirmed, overreaction noted.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQeHgyb0lGX2ZCUmlmSFRqX2VFNEw3ZXkySDZqakludEMydGhkd0dKWm1adndOVUFlSGdQNDF6OHhvWnMtQ0NGeGNocWxhVFZ5S1RnOU42blBaN3U2cFhSY0hRRm9pU284OVFTczBCenNPd3Y2OHRKeVdMeERSTG9kTWR6WUFvOWI3VWtsUENyLVV3TjU3YjhvNm1ybUxNTUZGNWt2bF9sV0c?oc=5>

### Why Is Xylem Stock Sinking Tuesday? - Xylem (NYSE:XYL)
- Summary: Stock price falling on Tuesday, reflecting investor anxiety.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPRGthMzdjTDlxNWJqemZ5bDU3OUoxOG42VG9mZmQ3ZmVUaThWMkprZXpDeURCSXd6VEZ3cW5NLW4wXzh4U1hmZm12dnJ0R1VYR05ES2ZSekVyZnZLYjQxRWJWa1BlYzhwN0w3clpBd0pENWg4VEg2ZW9fR1NQWVpuTEV3SmJsVEJrNFpOanZCczJUOWNDYW5fOHdjaEx5ZHdfcS15TmFfMmlxWTRYZ0JPbmFiSGNEc1I5SXBZcUpUOVoyOE9k?oc=5>

## CATALYSTS

### Xylem’s Q3 earnings call: our top 5 analyst questions
- Summary: Xylem’s Q3 earnings call: our top 5 analyst questions
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOckZDbHN1YjJORW9SVU4ySVZJdGtNTF9iTEFsRVF0aC1FU2llbWdrdndGTjNXdVQzaC0xUGh2TWp6OWt5TldsT1A5S2hQNHowMDc2ZkJrY2RJeFhiODhib21zdllqcWl4dlRXSC1LZmpVZE5NS2l0Zm9lVGRzQ1ZYNmNzRnQ5V0dyX3J2bG9sQ1Z4b1AzQkE?oc=5>

### Xylem Inc (XYL) Earnings, Actual EPS, EPS Estimates & Results
- Summary: Xylem Inc (XYL) Earnings, Actual EPS, EPS Estimates & Results
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiVEFVX3lxTE1UaTdmQnoyTnJfS2tzUEhVMVlDR21YS05NZmhZcS1RSXZPaU9Nd21KMGxQRW1HaDh0TFo4VVNXc19iZEpFc3phTm1NR055OWQ2LXRoYQ?oc=5>

### Xylem Gears Up to Post Q3 Earnings: What's in the Cards?
- Summary: Xylem Gears Up to Post Q3 Earnings: What's in the Cards?
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNZzAwYzZtZVh1Vk5Ba0k0UEpqN2FhcTN0UV9MdzNIeVg2cVdCWElPb0pFbW9ZbjF6VTFlTmJya1RGYWlaRmhZNExiUGJpcTFZNl9NUm1yVEhfaVBIOTRGeUpwSVh4VlF1R3RENzg4VWs2Zkx2UkdtNjhZTW5jS0xOREI5M05mTGNnWVBNY3kxbkNGdERhOEluUQ?oc=5>

### XYL Q3 deep dive: portfolio reshaping and delayed utility spending drive guidance revision
- Summary: Xylem revises Q3 guidance due to portfolio changes and delayed utility spending.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOLVJvSFpnYWxVNWtPS2xCdHVFVDhfa19WUVVTaVRYMVluckVqOGhlZFVKOE9hcXhmTDRHdFpRZFp5YmFXZjFLc1N6TFlIUnF1X05TS29fS2pEN3dsX212Uk56UnE0NVk3NGdPRzMwVkJXY0J6azlFVVU3SEJCWGItNWxSMFpOMDhOdnBfTlFDLUNteUdnSmc?oc=5>

### Here's What Key Metrics Tell Us About Xylem (XYL) Q3 Earnings
- Summary: Key metrics suggest potential earnings strength.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPaWI0R1VZRGJxWjBsVGp3YWFOTG5nMHo0ZWFTcHhHZnF2MWtObzVCT3M5U2xQV3hUbzFyYkpBMXhmS3ItNENtN1dfZXlfb2pvWnNRbk1yU2RqbDNFVXB4QUpJd204VEJsM3Frb2xXTXJfLU1tby1LNU11UFZ4bHhxM19aanhZWjRoMzNodGF3a2RnVFR4?oc=5>

### What to expect from Xylem’s (XYL) Q3 earnings
- Summary: Xylem’s Q3 earnings are anticipated, providing insight into financial performance and future outlook.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQaGJHVi1MQ0hXVDBNYXprR2R0dm5yZDJYSDR4M0gzME5iT2lkbU9DWWhMUENrRVQwNFRtdF84Z2pqQXhzdU5kTE1TLW1QeG9UWklwN1hKZVZLUXEyMS1IanpDZ3FXTHlDUDdYSUx0ejU4Y2lCUTVvZGJzUm1YTENSajFZQVhlY3JYSHBRRzIxTlV2NDRvMlAzSw?oc=5>

### Is Xylem Inc (XYL) a Bargain After 5.0% Drop? GF Value Says Unde
- Summary: GF Value comments on Xylem's valuation after a price drop.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPbllUZURlUEFXc0JXTkZfUVZSU1RCV084SHlYQjUzd0FJSzVJdnJLam16Tl9LQmdSTnhISWpvb1dFemtmZ0Fob05Ca1pTLWRTTXpJOG45VDBYYUYwRkdCdTJOc2Q4ZDFaT0tiVFZ0WmJYbmJ2aVhXVjhXSVlXd1Z0Uk5GTjVDVEN3dEhRSzhDWVNhYVB3TE9HRXVNdDREcG9wMTRiVVN2Si0?oc=5>

### Director D Koch Buys 11,000 Shares of Xylem Inc (XYL)
- Summary: Xylem director D Koch purchased 11,000 shares, indicating confidence in the company.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxObVdQLWFwNk0yYjJQUDVmWXotakkxT0JiMUVSUXUyalNLRU9ENkFyMmI0Z3BNdzZURkhXanVYZ2xJM3lRRXVRWVRNZGlQNVVjSmRqUlBUY1NvX3luUTBieWU3OTBGVUp1VEd0cDQtQkNyQVkxTmtlNEhWNWlNQ0JnVVVZS2RiV0c4TjBQdUVFbkVVQjg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **XYL** | **21.57** | **2.18** | **12.65** | **-3.00** | **22,305,083,392.00 USD** | **-34.62** |
| AOS | 17.63 | 4.82 | 11.80 | -0.20 | 8,787,800,064.00 USD | 1.41 |
| PH | 32.59 | 7.60 | 22.11 | 9.80 | 117,068,890,112.00 USD | 21.12 |
| DOV | 24.23 | 3.76 | 15.46 | 7.50 | 28,716,173,312.00 USD | 20.20 |

Peers fetched as_of: 2026-11-02; XYL reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-27
- Revenue (latest available single quarter): 2,201,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 291,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1524472/000152447226000148/xyl-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilwFBVV95cUxPS29KYkJVWWVPeFBtY1BpLVdLMU9xZ3VySUswRmExTmM2NzhKVmVWd0s3bGVlWkZ5TVFEOUQ1WktuR3poclBXSk8yQ0ZBZDlMalR2TUhham9HWkM4cmk0ZjdGZ2ZBa1JnNkFzU09Bb3lMdWJ2aktwelgzWTdYNWI0d000b2REZDlFYWtSWW5Iakp1VldNLXg0?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQRE91WmRwR0FvYVhOWHZkejQzVHNhLTNDV2tHVEZxT1Z2Y19Ld1dqSVlYWGlfWlF4N3VhcFB6SUtkQkpRRnNNel82Sm9KVGpZVE5rUEVJTnIxcGtOSU5QREFvZXFsVTFSZWFRRlJ6Z2hiWVNVUVhzRGJYakNYZTJCbVgzS3JLR0dHNTF2NUtVZGlVTzFhc19v?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNWTlNZ0Y2alE4VXhtVzI5Tm5MZENtVk1NZHR6TGZmWlhEbWdZSDNJRjJ1VlBmVlFEeUdXT2dmc09nT2ZiWGVXVHVRTTc4V2RYU3dXYy1hbGpRc3B3V3BhMnZ6aHJyNFQtbmpIUFV3TDA0cm1kU3RqV3hUeWkzNDJISFhnVjNITG9fcUo4ejN5SUpWLWJvMVNUOGNqOEJ2dw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxORjUyLTdIXzc4b2VWRjVZRGk4VVFmU041V2hfQ0ZMdFc0TkJXLW1sX05HRXFGZ0VnZWU5Vm9uWmYwR2NzaGhpS2pGTmZMR24wLU9IVnBHSXRkMzBScnRTd0tGa2NjU3IyWWdDaDZIb2JSNERiYWpxcXo4YXdyYTVUSHRsSTlFSnNwUUF0LUpHeGtwbzQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQOWVBOEdiajVsWW1wc1RNRjNmVDhZdU1Kb3JWMjBQQ2V1V3lhclJ3eTYxTllRcm1UZ2hhdkR2V3BtSzZoNlhYZDNBYTFRamhleF9zYnI5NEp1bEY1MnBfeTRDdEVFWEY5WnJMQXRHZmFsX2phNWktTm02RFVaRFZCMW83Szh2ck5ObDlsYmFmWV9Gb25RTVd1Sg?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQOW9ZdEdTLUg1bWpxZnlpRkVjVWhFQS1lR2EzUW5vQXE3OXRJZ05QMjFTR3VTM0k5RVFJckhpUVJna1ZrQU9OOER6eDh1cVN5QnpOUVBwdEQxeTJKUVVhcW1IeHlZVFlEYnh6YldqREszRndfRF9YYmZIelV5M0tiU0wwM01CaDVLREJwSWJnVFJqaVNBZ0J5cA?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQeHgyb0lGX2ZCUmlmSFRqX2VFNEw3ZXkySDZqakludEMydGhkd0dKWm1adndOVUFlSGdQNDF6OHhvWnMtQ0NGeGNocWxhVFZ5S1RnOU42blBaN3U2cFhSY0hRRm9pU284OVFTczBCenNPd3Y2OHRKeVdMeERSTG9kTWR6WUFvOWI3VWtsUENyLVV3TjU3YjhvNm1ybUxNTUZGNWt2bF9sV0c?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPRGthMzdjTDlxNWJqemZ5bDU3OUoxOG42VG9mZmQ3ZmVUaThWMkprZXpDeURCSXd6VEZ3cW5NLW4wXzh4U1hmZm12dnJ0R1VYR05ES2ZSekVyZnZLYjQxRWJWa1BlYzhwN0w3clpBd0pENWg4VEg2ZW9fR1NQWVpuTEV3SmJsVEJrNFpOanZCczJUOWNDYW5fOHdjaEx5ZHdfcS15TmFfMmlxWTRYZ0JPbmFiSGNEc1I5SXBZcUpUOVoyOE9k?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOckZDbHN1YjJORW9SVU4ySVZJdGtNTF9iTEFsRVF0aC1FU2llbWdrdndGTjNXdVQzaC0xUGh2TWp6OWt5TldsT1A5S2hQNHowMDc2ZkJrY2RJeFhiODhib21zdllqcWl4dlRXSC1LZmpVZE5NS2l0Zm9lVGRzQ1ZYNmNzRnQ5V0dyX3J2bG9sQ1Z4b1AzQkE?oc=5
- https://news.google.com/rss/articles/CBMiVEFVX3lxTE1UaTdmQnoyTnJfS2tzUEhVMVlDR21YS05NZmhZcS1RSXZPaU9Nd21KMGxQRW1HaDh0TFo4VVNXc19iZEpFc3phTm1NR055OWQ2LXRoYQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNZzAwYzZtZVh1Vk5Ba0k0UEpqN2FhcTN0UV9MdzNIeVg2cVdCWElPb0pFbW9ZbjF6VTFlTmJya1RGYWlaRmhZNExiUGJpcTFZNl9NUm1yVEhfaVBIOTRGeUpwSVh4VlF1R3RENzg4VWs2Zkx2UkdtNjhZTW5jS0xOREI5M05mTGNnWVBNY3kxbkNGdERhOEluUQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOLVJvSFpnYWxVNWtPS2xCdHVFVDhfa19WUVVTaVRYMVluckVqOGhlZFVKOE9hcXhmTDRHdFpRZFp5YmFXZjFLc1N6TFlIUnF1X05TS29fS2pEN3dsX212Uk56UnE0NVk3NGdPRzMwVkJXY0J6azlFVVU3SEJCWGItNWxSMFpOMDhOdnBfTlFDLUNteUdnSmc?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPaWI0R1VZRGJxWjBsVGp3YWFOTG5nMHo0ZWFTcHhHZnF2MWtObzVCT3M5U2xQV3hUbzFyYkpBMXhmS3ItNENtN1dfZXlfb2pvWnNRbk1yU2RqbDNFVXB4QUpJd204VEJsM3Frb2xXTXJfLU1tby1LNU11UFZ4bHhxM19aanhZWjRoMzNodGF3a2RnVFR4?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQaGJHVi1MQ0hXVDBNYXprR2R0dm5yZDJYSDR4M0gzME5iT2lkbU9DWWhMUENrRVQwNFRtdF84Z2pqQXhzdU5kTE1TLW1QeG9UWklwN1hKZVZLUXEyMS1IanpDZ3FXTHlDUDdYSUx0ejU4Y2lCUTVvZGJzUm1YTENSajFZQVhlY3JYSHBRRzIxTlV2NDRvMlAzSw?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPbllUZURlUEFXc0JXTkZfUVZSU1RCV084SHlYQjUzd0FJSzVJdnJLam16Tl9LQmdSTnhISWpvb1dFemtmZ0Fob05Ca1pTLWRTTXpJOG45VDBYYUYwRkdCdTJOc2Q4ZDFaT0tiVFZ0WmJYbmJ2aVhXVjhXSVlXd1Z0Uk5GTjVDVEN3dEhRSzhDWVNhYVB3TE9HRXVNdDREcG9wMTRiVVN2Si0?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxObVdQLWFwNk0yYjJQUDVmWXotakkxT0JiMUVSUXUyalNLRU9ENkFyMmI0Z3BNdzZURkhXanVYZ2xJM3lRRXVRWVRNZGlQNVVjSmRqUlBUY1NvX3luUTBieWU3OTBGVUp1VEd0cDQtQkNyQVkxTmtlNEhWNWlNQ0JnVVVZS2RiV0c4TjBQdUVFbkVVQjg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
