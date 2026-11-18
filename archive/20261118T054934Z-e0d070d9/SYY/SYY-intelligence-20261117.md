# SYY Intelligence Report

- ticker: **SYY**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/SYY/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SYY/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:03:23.352376+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 5, 'rule': 2, 'ai': 1, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/SYY** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 5 unique headlines; 4 named publishers; 0 exact duplicates; 5 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-14

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 77.9900 |
| Return 1D (%) | -0.3195 |
| Return 1W (%) | 0.4637 |
| Return 1M (%) | -5.1447 |
| Return YTD (%) | 8.9025 |
| Return 1Y (%) | 6.8152 |
| Annualized volatility (%) | 29.2456 |
| Beta vs SPY | 0.2184 |
| Max drawdown (%) | -23.9798 |
| Sharpe (rf=0) | 0.3762 |
| Downside deviation (rf=0, %) | 22.3911 |
| Sortino (rf=0) | 0.4914 |
| Historical VaR 95% (1D, %) | 2.1606 |
| Historical ES 95% (1D, %) | 4.3236 |
| Correlation vs SPY | 0.1029 |
| Tracking error vs SPY (%) | 31.0203 |
| P/E (trailing) | 20.74 |
| P/B | 9.49 |
| EV/EBITDA | 11.20 |
| Revenue growth (%) | 2.80 |
| Forward P/E (estimate) | 14.45 |
| Gross margin (%) | 18.54 |
| Operating margin (%) | 4.13 |
| Return on equity (%) | 58.74 |
| Free cash flow yield (%) | 6.27 |
| MA50 | 79.2013 |
| Close vs MA50 (%) | -1.5294 |
| MA200 | 79.4572 |
| Close vs MA200 (%) | -1.8466 |
| RSI (14, Wilder) | 47.3861 |
| MACD (12,26) | -0.7803 |
| MACD signal (9) | -0.6378 |
| MACD histogram | -0.1426 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SYY': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 77.9900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.3195 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.4637 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -5.1447 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 8.9025 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 6.8152 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.2456 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.3911 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4914 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1606 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.3236 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1029 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.0203 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2184 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.9798 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3762 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.4499 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 18.5430 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 4.1330 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 58.7360 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.2711 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.7420 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 47.3861 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1426 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -1.5294 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.8466 -> Slightly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Sysco Corporation $SYY Stock Purchased by Teachers Retirement System of The State of Kentucky
- Summary: Sysco Corporation $SYY Stock Purchased by Teachers Retirement System of The State of Kentucky
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxNX0tCUmQ4Zm5zTXhLM3pxNW92c3o5WS1heHliWTVQM2VLSTVnSDFmWlM3QW5CSFdxcGtDclJCUVZoZ19VQUl0dkpuZV9jOHk3SGVmU0J0SXpzbkxlMVZjVkhyR0FqdUxleTYtaWRZXy01YXJ1bHdWdDJBaXNOemVqbGt2dmJHei1rSFdDQTEwd25OMXN6a3MyVHZjNE96OE0wTkI5RFp1cU5DV2NtWGp3ZUNjOFh0U2ZRNW9qaVJ1VnN1VlF5ZTdtUlB1R2ZSeUVmX0pIRzVVTy11LUdhaTRLX2RDVHZkUWZr?oc=5>

### Sysco Corporation $SYY Stock Purchased by Danske Bank A S
- Summary: Sysco Corporation $SYY Stock Purchased by Danske Bank A S
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNWURHS2NBZjQzckdTQWxuSGZORVRvUW1vQ1NfUzhFRGNOQ1dCNTBEQ3FBdUgtSVdWVmU3ZXZ1alE0UWRLN1h4MzZIMHNzUk1PZmdnSXRORC1BUHJKdUFyMG9ZNHNab0Nxa3NsN1QwV1lTQTZmLXVrOVo5WEVaR1p1dWs2TnJIblh2VWZUQ2FSZ0VoV051U1lNX2ZaY09Ia1RBRHktUFQ1SnR1ak5iazkteDJJbE5qVE41?oc=5>

### Does Earnings Beat Change The Bull Case For Sysco (SYY)?
- Summary: Analysis of whether Sysco's earnings surpass expectations and its effect on the bullish outlook.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOdThMRVNhT2tpU0ZJdkdDVHZyTGtjN2VXXzQ0Z0RXbjFzOFdmdGZFX2tHZE91c3NWY1Ryd3k1bmJDUTRzRVZ1ZG5qSW4yQ2VFUTVVbXoySDVVcWNPVkxhcWJUZTZMdmcyLVFxelNNVFpidFJrVG5JeWhTLWlvOUJxRXVvYnoxQVV2c0trNTBCR09CMU9uOTc4VjVod1pMdmZrY0VaQTFvN3hiXy1UUTY3LTQ2R1lSc3VwXzlFMEkxMFloZ9IBxwFBVV95cUxQTXl1ejlxSGZJWkxDdmUzQVNBLVBXNDRVUjh0blFBOGJweDk0OU1TZC1sSFlEUXRZQ3RmTGZ0Um5YUDN0V3kxRTVhX1dLaGJLSEZ6OHBJcHVTTldWUTRpUzNMbU1JTjAyTlYtMVNjQTdJMGZiakFnWllhRzR0UDk5bHlnQ3NVWnRGUVRlcTNKd3N5VVM5am9FeDBOV3JwaEVjVFBFR1pXdXYzczF6cDk1d09kUi1iaG5RS3RwVEQ0cS1WX2RhN3VJ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SYY** | **20.74** | **9.49** | **11.20** | **2.80** | **38,392,193,024.00 USD** | **6.82** |
| USFD | 30.24 | 5.30 | 14.86 | 2.10 | 22,982,754,304.00 USD | 50.27 |
| PFGC | 44.69 | 3.41 | 14.34 | 5.50 | 17,416,255,488.00 USD | 17.34 |
| CHEF | 44.70 | 6.21 | 19.41 | 11.20 | 4,546,219,008.00 USD | 81.25 |

Peers fetched as_of: 2026-11-17; SYY reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 21,744,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2027/Q1
- Net income (latest available single quarter): 526,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/96021/000009602126000050/syy-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi6AFBVV95cUxNX0tCUmQ4Zm5zTXhLM3pxNW92c3o5WS1heHliWTVQM2VLSTVnSDFmWlM3QW5CSFdxcGtDclJCUVZoZ19VQUl0dkpuZV9jOHk3SGVmU0J0SXpzbkxlMVZjVkhyR0FqdUxleTYtaWRZXy01YXJ1bHdWdDJBaXNOemVqbGt2dmJHei1rSFdDQTEwd25OMXN6a3MyVHZjNE96OE0wTkI5RFp1cU5DV2NtWGp3ZUNjOFh0U2ZRNW9qaVJ1VnN1VlF5ZTdtUlB1R2ZSeUVmX0pIRzVVTy11LUdhaTRLX2RDVHZkUWZr?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNWURHS2NBZjQzckdTQWxuSGZORVRvUW1vQ1NfUzhFRGNOQ1dCNTBEQ3FBdUgtSVdWVmU3ZXZ1alE0UWRLN1h4MzZIMHNzUk1PZmdnSXRORC1BUHJKdUFyMG9ZNHNab0Nxa3NsN1QwV1lTQTZmLXVrOVo5WEVaR1p1dWs2TnJIblh2VWZUQ2FSZ0VoV051U1lNX2ZaY09Ia1RBRHktUFQ1SnR1ak5iazkteDJJbE5qVE41?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOdThMRVNhT2tpU0ZJdkdDVHZyTGtjN2VXXzQ0Z0RXbjFzOFdmdGZFX2tHZE91c3NWY1Ryd3k1bmJDUTRzRVZ1ZG5qSW4yQ2VFUTVVbXoySDVVcWNPVkxhcWJUZTZMdmcyLVFxelNNVFpidFJrVG5JeWhTLWlvOUJxRXVvYnoxQVV2c0trNTBCR09CMU9uOTc4VjVod1pMdmZrY0VaQTFvN3hiXy1UUTY3LTQ2R1lSc3VwXzlFMEkxMFloZ9IBxwFBVV95cUxQTXl1ejlxSGZJWkxDdmUzQVNBLVBXNDRVUjh0blFBOGJweDk0OU1TZC1sSFlEUXRZQ3RmTGZ0Um5YUDN0V3kxRTVhX1dLaGJLSEZ6OHBJcHVTTldWUTRpUzNMbU1JTjAyTlYtMVNjQTdJMGZiakFnWllhRzR0UDk5bHlnQ3NVWnRGUVRlcTNKd3N5VVM5am9FeDBOV3JwaEVjVFBFR1pXdXYzczF6cDk1d09kUi1iaG5RS3RwVEQ0cS1WX2RhN3VJ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
