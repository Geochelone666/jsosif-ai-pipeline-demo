# COST Intelligence Report

- ticker: **COST**
- Report as_of: **2026-10-24**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/COST/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/COST/key-statistics/
- AI analysis snapshot as_of: **2026-10-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-25T00:59:35.760376+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 4, 'ai': 9, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 10 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 31.82%; oldest publication 2026-10-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1003.3200 |
| Return 1D (%) | -1.4624 |
| Return 1W (%) | 1.4366 |
| Return 1M (%) | 10.9009 |
| Return YTD (%) | 16.8621 |
| Return 1Y (%) | 7.1253 |
| Annualized volatility (%) | 19.7998 |
| Beta vs SPY | -0.1841 |
| Max drawdown (%) | -18.1993 |
| Sharpe (rf=0) | 0.4477 |
| Downside deviation (rf=0, %) | 13.7252 |
| Sortino (rf=0) | 0.6459 |
| Historical VaR 95% (1D, %) | 2.0766 |
| Historical ES 95% (1D, %) | 2.7374 |
| Correlation vs SPY | -0.1185 |
| Tracking error vs SPY (%) | 24.7857 |
| P/E (trailing) | 48.33 |
| P/B | 12.42 |
| EV/EBITDA | 30.56 |
| Revenue growth (%) | 11.10 |
| Forward P/E (estimate) | 40.09 |
| Gross margin (%) | 12.77 |
| Operating margin (%) | 3.79 |
| Return on equity (%) | 28.40 |
| Free cash flow yield (%) | 1.52 |
| MA50 | 938.8648 |
| Close vs MA50 (%) | 6.8652 |
| MA200 | 967.6397 |
| Close vs MA200 (%) | 3.6874 |
| RSI (14, Wilder) | 69.1972 |
| MACD (12,26) | 22.1491 |
| MACD signal (9) | 16.0507 |
| MACD histogram | 6.0984 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'COST': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1003.3200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.4624 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.4366 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 10.9009 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 16.8621 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 7.1253 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 19.7998 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.7252 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6459 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0766 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7374 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1185 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.7857 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1841 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.1993 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4477 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 40.0906 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 12.7660 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 3.7890 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 28.4020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.5188 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 48.3295 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 69.1972 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 6.0984 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.8652 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.6874 -> Slightly above the moving-average trend level.

## TAILWINDS

### Costco (COST) Stock May Be Priced For Perfection On Earnings
- Summary: Analyst suggests Costco’s stock may be optimally priced ahead of earnings, indicating positive market sentiment.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxOT0VjaTF5LXh0cHJVY3ZxOFcwNC1LZUtpT254YVNFUkh5X2h6UXJwaWRiZkRxZW5kRWJBSDVQcFprbDRjWkhxdVg5akpJVXpoQjZaaF9tR29nY3ZocGZhdnBOUDRJdTFxVldsR1NvRjdfRVBUMHNOQm10MkhITW5tTDBZWksweExCQzhFWEFLazJpQXVoc0FQMXJKTzFvWldMVGZKNldpZExEZGZMUXZYNHltQUpISnJFRjJkN3BoYkN2cXpUQkZwQmRPNm9vbmQ1eXJPLXFIV0NTNWPSAeABQVVfeXFMTlc3RjhkSmlidGg5ZDRGb2JOV1hQeEQtM0cxTGlXTWtEd3ZKMmxOWk0yTFJ3ZVVyMHlEbjZtRkpOXy1jdzA2MEdpQ0RHdko1OGRiQTVSV3c3NmJDVE11TjVhdE1JcGg0NTZsWmxCajIwWXhkZmVvcG4xOGxkOGpxVkxPV1JHWjBLUEJuSXFCYkY5b2JLZzNCdllTcG1lRmc0c3drOVVEcU1XVXZoTmxFQXlXZHQwX25uWno5Q3k5QmJWN1ZISno0Rjk4ekRKblZKbHNvcF9WNmhpc1phRjZ1Zko?oc=5>

### The Zacks Analyst Blog Highlights Costco, Walt Disney, Marriott, Park Aerospace and Flanigan's
- Summary: Zacks blog spotlights Costco among top picks, implying favorable analyst coverage.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQSVNzWUlhUjI3TnlKWTJucDZ3TDRBLU5JVVdnMDh0RE1IOG9tb1lMV2FONEJjXzh1YTVMb3pzODJscnhQa3ZLUHJhMWx1S0JSdTNJN2VHcDdqaDZsS2JwRjk4MzJHRzdXdnNfUkRUMUpnZzRweTVIWmRlZXo5Q0YzcFJWN21LN0VsNXEteVk1bEZ0aUQ0Yk42dzJWMWc5b3NjTUhr?oc=5>

### Costco Wholesale Corporation $COST Stock: Adams Diversified Equity Fund Inc. Grows Position
- Summary: Adams Diversified Equity Fund increased its stake in Costco, signaling institutional confidence.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxNZ0hOcWFpdkpjcG9ROTF6ektVZC01elM0a0VPa0Z2c3EyUDdTVWc4bV9iVGpNbGFVWVZ1bkZHSnNuVnQzN0h2R2xacno4cC1mOEx3T3dkbzRvcjBYcEdFZHk5Tnc1M0o2UkdQLTNrU2ZTWTFGaXlHQ29xRld0WjR1YXItVHczZmI1LXE5MndxUFRsOENfY3djaVlWZlZLLWR6bU1aWnFwOGxqalo5UHp6Nkh0T1hvTjJSXzl0WGpUVW9lc1d0OWhqY2xyWDY5WHc4aHBhQWhueEN4SHBRUVJaTGxvZw?oc=5>

## HEADWINDS

### Truist reiterates Hold on Costco stock citing strong comps
- Summary: Truist maintains a hold rating, suggesting cautious outlook despite strong comparable companies.
- Date: 2026-10-19 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOaU5ISkZJYzJHcGpjejltNWZmWVVqdE94ci1VUUE0SkpsWnlHc0FoakRlQ0lXcTBBM3FFY25qTUktT3JEOGR1MzZCVEdpbGhQOGtKb2NmdnpTZThWRURweVJiSHd0VmZleXRIalZvbGlnZU4tR2c5Zzd5VzAxeHFLcWJ6ZmVscTdhY1JqTkh0SXBOcUFjX25WVHZxbXBSVWM5YTJRUFM3TXFadGpjUElRZXdZVzZraGxoNUE?oc=5>

### Costco Wholesale Corporation $COST Holdings Trimmed by Sepio Capital LP
- Summary: Sepio Capital LP reduced its holdings in Costco, indicating potential negative sentiment.
- Date: 2026-10-24 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxQUWZNc09aSS13THl4SVAxSTRfdmdzMHpMUVo4WHJQRkozSDkzY2ZOT0xFUVJTRHlhc19hRWI2U3dMYXVOa2RFT3RvaFFVUDR4QXEzVnpYdVZFcXY4bjFEY0xTZm1sdGk3RndGZ2o2SlVoZVBHVGIzcExZNkJDVE1Fa0JUaWRETmZnQkJFbnhUSDBOM0NFaURBdWxYY0ZvWElqN3N3dVNCdkxxYjNPcnMteDBya0hZNmRoVVFLSVFNTVk1N0FVTVV6ZWZySQ?oc=5>

## CATALYSTS

### Costco's Last Stock Split Was in 2000. Is Its Board Close to Another?
- Summary: Costco's Last Stock Split Was in 2000. Is Its Board Close to Another?
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOS0hEMnF3U29oM05mVE9xLXJsUVBLVHNjcVZFc0ZJWHdSWXlZdTJVSVlVb3Q0enZsazZTeGxSUFNMaTdfSHJjOGxEWDA3Sll0QUp5ZWd4OVdlcnltM1VHQmFUUURaRVpmMktsU1JfLTd5ckN5R3RNNW0xUGFhZm1tUmliYkZIWG14S2xTVlFmaWZzVkRsLU16M1ln?oc=5>

### Costco Turned $1,000 Into $8,018 in Ten Years While the S&P 500 Delivered $3,564
- Summary: Costco Turned $1,000 Into $8,018 in Ten Years While the S&P 500 Delivered $3,564
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPZjNwWWRaUlV3MXFMSWJUX0hhdEtFZDZ1VkJ5MjRYcmRjS0pWZl9ZVzBQTWxhRHZPX3NKQ3hKcmswbFBmODVxaDh3UDZrc3lPa2x6NlQza2Y2TDdBOFVNMWpmNUoyZ1NFOUpRUFVUd3RXV1BYVEtzT3RKazZfd1MzZzY0bmhoZkdpMEZ5RmpQbUgwMlktMDhSVC1lRjEtemRfc2JtbEVSSWtUSVpDdVNEbkhsQzZ1Qkd1?oc=5>

### Costco Wholesale Corporation $COST Stock Acquired by Howland Capital Management LLC
- Summary: Costco Wholesale Corporation $COST Stock Acquired by Howland Capital Management LLC
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxNcEM0Ty0zTlRrcEJSR0E4OHIybnVIOE9OSE5NT09qbjNmLWhlTmUzdU16d3UydlRmM2dUMk1Ia1N5eVZEVURBUngyNlR4dVN1OVVPeUNNMEpNQjlEWjA1VGlseTBMWmJJd0RqVVNuLVBWdi1OSDQ3RTZVdDlhNUNQWUxJazBJbkp3NVdJckxRREhvT255c3JXYi0yYWFlR0dpbWZGLXVIcEVBUkdXdnByQzJkaDNqMHpoMEJUYjNoZ2tXd3FRTHVsSXFQdkFLMGZiaEV1Y2RYdnNYc0U?oc=5>

### Costco Is Paying a Dividend Next Month. Here’s the Deadline to Buy the Stock
- Summary: Costco Is Paying a Dividend Next Month. Here’s the Deadline to Buy the Stock
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxOX05TSnJzZzlKYWlwbFNzXzZxdG9naXZwTG44R1hoTWd4NHB0bERBWEp4bno5U0xqNXkzbkFCZFFadzJRR2xEdGhRYWx2MFVKeEFGcGNMLUlycEhTMjJySHhwNm9mVTNIdGo3X3NEeFBDNTlfVlBTNWo1bUpZNlo4SkNXNmhwWUZOelkyWlU5WWkwS0VMdnk3R2RtUm4zR1g5QUZITXFaTG9OU19R?oc=5>

### Costco (COST) Advances While Market Declines: Some Information for Investors
- Summary: Costco shares rise amid broader market decline, signaling investor confidence.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQdllxbjJ5MVp0RzlUZ2xwcEhHUURCbDNab3lqVHlpT0c1b0l5ODJDeHhkUUtHeGNTSGlnc1dBZHMxV0x3UEZBY0xONHBGTDJkVWRiSkNhSk15ZVgwaE9XczhEOVRFU0UybTdQSWtjUlJNcm1ablNab2tMS0k1ZzlTNElVTW5CeWhDeUtHVEN5cnpwTmdTUVhNOVNCZDk3Rnc?oc=5>

### Costco Wholesale (NASDAQ:COST) Stock Falls 1.5% - Should You Sell?
- Summary: Stock price dropped 1.5%, prompting sell‑side speculation.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPdTdCVU9sV2VLcnNlRThBeEFDZlYtQmxEZUt5X0xtM1g5M0c3V0ZCVkg5ZTh4cmZjVEZqUHBlZ2NqZlZ1bmdPdXF2TjhMbzBzaVBXcjRKc3Vjc05qSzNaR0hsekxjTEVVc0JaVk5DcE11Yl9zN2tYVXdscXFXN1d4QUEwRm5OX1JEMmVVWnRxZXBVcnk3c2tvdjVyNlQtOHNVTXJRVjdFX1FIZWZET1JUdEFVTjRfM0pUdWJ3?oc=5>

### Is Costco Wholesale (NASDAQ:COST) Standing Strong Amid Market Rotation?
- Summary: Analysis of Costco’s resilience during sector rotation.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQUVR0bGZySG9LYVRtNXJsVzEyVFY0Q0RuYUxFN2g4bHdNZDNzbmVOY2xuSEVSOTROd0FYQlh6V0FOM1Y3VjZPeG9MSlNJNXpPeTZSM0V2VG1Ob1NfSkl4YUJydUpJaWRQNW82dmtHdWhUQ21xMmRMR29CdnZnWldfODdsVm84UlRDNk1IT0E5YUxHdTFlRldOWU5lTWpfenhIVVVvOF9zQ185UDRtT0E?oc=5>

### Costco Wholesale Corporation $COST Stock Holdings Reduced by Hosking Partners LLP
- Summary: Hosking Partners LLP decreased its Costco holdings.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxPTG8wS0NRM0NVVjUyYzlxQ2NpMHQtREdVOHFnUjNHdDItM0o5cUF2Zjl2eWFNdWxMdkdzVnRYakJ3VWVaYlhLWXgzX0dudUh0OXE2TU0wTG03TE4zRkh3aERFXzRVVU9wbFphaW5fTm5GTXQ4Vi14dG1kSmtsTmd5UVJRNV9RODEyRkVyRUZvOUJYa0UzWDg2RzV6ZEVRMHNNNTI2eTM4al9aUVRrMFduLWRITmtpN182eGJEUDdGSXZmbUNSVnhjd2l6QjJGOFZoLXRfU0I2djg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **COST** | **48.33** | **12.42** | **30.56** | **11.10** | **444,600,549,376.00 USD** | **7.13** |
| WMT | 43.44 | 9.69 | 23.17 | 5.90 | 954,094,059,520.00 USD | 13.14 |
| TGT | 15.86 | 3.89 | 9.68 | 5.30 | 69,398,364,160.00 USD | 68.64 |
| BJ | 22.24 | 6.09 | 13.88 | 15.70 | 13,369,146,368.00 USD | 13.23 |

Peers fetched as_of: 2026-10-24; COST reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-24
- Next expected earnings: 2026-12-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-07
- Revenue (latest available single quarter): 69,597,000,000.00 USD; period 2025-11-24/2026-02-15; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 2,192,000,000.00 USD; period 2026-02-16/2026-05-10; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi2wFBVV95cUxOT0VjaTF5LXh0cHJVY3ZxOFcwNC1LZUtpT254YVNFUkh5X2h6UXJwaWRiZkRxZW5kRWJBSDVQcFprbDRjWkhxdVg5akpJVXpoQjZaaF9tR29nY3ZocGZhdnBOUDRJdTFxVldsR1NvRjdfRVBUMHNOQm10MkhITW5tTDBZWksweExCQzhFWEFLazJpQXVoc0FQMXJKTzFvWldMVGZKNldpZExEZGZMUXZYNHltQUpISnJFRjJkN3BoYkN2cXpUQkZwQmRPNm9vbmQ1eXJPLXFIV0NTNWPSAeABQVVfeXFMTlc3RjhkSmlidGg5ZDRGb2JOV1hQeEQtM0cxTGlXTWtEd3ZKMmxOWk0yTFJ3ZVVyMHlEbjZtRkpOXy1jdzA2MEdpQ0RHdko1OGRiQTVSV3c3NmJDVE11TjVhdE1JcGg0NTZsWmxCajIwWXhkZmVvcG4xOGxkOGpxVkxPV1JHWjBLUEJuSXFCYkY5b2JLZzNCdllTcG1lRmc0c3drOVVEcU1XVXZoTmxFQXlXZHQwX25uWno5Q3k5QmJWN1ZISno0Rjk4ekRKblZKbHNvcF9WNmhpc1phRjZ1Zko?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQSVNzWUlhUjI3TnlKWTJucDZ3TDRBLU5JVVdnMDh0RE1IOG9tb1lMV2FONEJjXzh1YTVMb3pzODJscnhQa3ZLUHJhMWx1S0JSdTNJN2VHcDdqaDZsS2JwRjk4MzJHRzdXdnNfUkRUMUpnZzRweTVIWmRlZXo5Q0YzcFJWN21LN0VsNXEteVk1bEZ0aUQ0Yk42dzJWMWc5b3NjTUhr?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxNZ0hOcWFpdkpjcG9ROTF6ektVZC01elM0a0VPa0Z2c3EyUDdTVWc4bV9iVGpNbGFVWVZ1bkZHSnNuVnQzN0h2R2xacno4cC1mOEx3T3dkbzRvcjBYcEdFZHk5Tnc1M0o2UkdQLTNrU2ZTWTFGaXlHQ29xRld0WjR1YXItVHczZmI1LXE5MndxUFRsOENfY3djaVlWZlZLLWR6bU1aWnFwOGxqalo5UHp6Nkh0T1hvTjJSXzl0WGpUVW9lc1d0OWhqY2xyWDY5WHc4aHBhQWhueEN4SHBRUVJaTGxvZw?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOaU5ISkZJYzJHcGpjejltNWZmWVVqdE94ci1VUUE0SkpsWnlHc0FoakRlQ0lXcTBBM3FFY25qTUktT3JEOGR1MzZCVEdpbGhQOGtKb2NmdnpTZThWRURweVJiSHd0VmZleXRIalZvbGlnZU4tR2c5Zzd5VzAxeHFLcWJ6ZmVscTdhY1JqTkh0SXBOcUFjX25WVHZxbXBSVWM5YTJRUFM3TXFadGpjUElRZXdZVzZraGxoNUE?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxQUWZNc09aSS13THl4SVAxSTRfdmdzMHpMUVo4WHJQRkozSDkzY2ZOT0xFUVJTRHlhc19hRWI2U3dMYXVOa2RFT3RvaFFVUDR4QXEzVnpYdVZFcXY4bjFEY0xTZm1sdGk3RndGZ2o2SlVoZVBHVGIzcExZNkJDVE1Fa0JUaWRETmZnQkJFbnhUSDBOM0NFaURBdWxYY0ZvWElqN3N3dVNCdkxxYjNPcnMteDBya0hZNmRoVVFLSVFNTVk1N0FVTVV6ZWZySQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOS0hEMnF3U29oM05mVE9xLXJsUVBLVHNjcVZFc0ZJWHdSWXlZdTJVSVlVb3Q0enZsazZTeGxSUFNMaTdfSHJjOGxEWDA3Sll0QUp5ZWd4OVdlcnltM1VHQmFUUURaRVpmMktsU1JfLTd5ckN5R3RNNW0xUGFhZm1tUmliYkZIWG14S2xTVlFmaWZzVkRsLU16M1ln?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTFB5MlluZF9FTXpyS2dFNjVRb2lMUVQtV1IxWUdXQ2dLX3dwOXVFZUVwblJ2dklobXR3S1ZGUDd0YmxJaWlnV0RneGtsem0yYzlwX0xmTUlWRFNCYlVrdk80MjNPWTVTb2hPeFVHdmxoNUZnNjBKVVZWdmkyeU0wQQ?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPZjNwWWRaUlV3MXFMSWJUX0hhdEtFZDZ1VkJ5MjRYcmRjS0pWZl9ZVzBQTWxhRHZPX3NKQ3hKcmswbFBmODVxaDh3UDZrc3lPa2x6NlQza2Y2TDdBOFVNMWpmNUoyZ1NFOUpRUFVUd3RXV1BYVEtzT3RKazZfd1MzZzY0bmhoZkdpMEZ5RmpQbUgwMlktMDhSVC1lRjEtemRfc2JtbEVSSWtUSVpDdVNEbkhsQzZ1Qkd1?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxNcEM0Ty0zTlRrcEJSR0E4OHIybnVIOE9OSE5NT09qbjNmLWhlTmUzdU16d3UydlRmM2dUMk1Ia1N5eVZEVURBUngyNlR4dVN1OVVPeUNNMEpNQjlEWjA1VGlseTBMWmJJd0RqVVNuLVBWdi1OSDQ3RTZVdDlhNUNQWUxJazBJbkp3NVdJckxRREhvT255c3JXYi0yYWFlR0dpbWZGLXVIcEVBUkdXdnByQzJkaDNqMHpoMEJUYjNoZ2tXd3FRTHVsSXFQdkFLMGZiaEV1Y2RYdnNYc0U?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxOX05TSnJzZzlKYWlwbFNzXzZxdG9naXZwTG44R1hoTWd4NHB0bERBWEp4bno5U0xqNXkzbkFCZFFadzJRR2xEdGhRYWx2MFVKeEFGcGNMLUlycEhTMjJySHhwNm9mVTNIdGo3X3NEeFBDNTlfVlBTNWo1bUpZNlo4SkNXNmhwWUZOelkyWlU5WWkwS0VMdnk3R2RtUm4zR1g5QUZITXFaTG9OU19R?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQdllxbjJ5MVp0RzlUZ2xwcEhHUURCbDNab3lqVHlpT0c1b0l5ODJDeHhkUUtHeGNTSGlnc1dBZHMxV0x3UEZBY0xONHBGTDJkVWRiSkNhSk15ZVgwaE9XczhEOVRFU0UybTdQSWtjUlJNcm1ablNab2tMS0k1ZzlTNElVTW5CeWhDeUtHVEN5cnpwTmdTUVhNOVNCZDk3Rnc?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPdTdCVU9sV2VLcnNlRThBeEFDZlYtQmxEZUt5X0xtM1g5M0c3V0ZCVkg5ZTh4cmZjVEZqUHBlZ2NqZlZ1bmdPdXF2TjhMbzBzaVBXcjRKc3Vjc05qSzNaR0hsekxjTEVVc0JaVk5DcE11Yl9zN2tYVXdscXFXN1d4QUEwRm5OX1JEMmVVWnRxZXBVcnk3c2tvdjVyNlQtOHNVTXJRVjdFX1FIZWZET1JUdEFVTjRfM0pUdWJ3?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQUVR0bGZySG9LYVRtNXJsVzEyVFY0Q0RuYUxFN2g4bHdNZDNzbmVOY2xuSEVSOTROd0FYQlh6V0FOM1Y3VjZPeG9MSlNJNXpPeTZSM0V2VG1Ob1NfSkl4YUJydUpJaWRQNW82dmtHdWhUQ21xMmRMR29CdnZnWldfODdsVm84UlRDNk1IT0E5YUxHdTFlRldOWU5lTWpfenhIVVVvOF9zQ185UDRtT0E?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxPTG8wS0NRM0NVVjUyYzlxQ2NpMHQtREdVOHFnUjNHdDItM0o5cUF2Zjl2eWFNdWxMdkdzVnRYakJ3VWVaYlhLWXgzX0dudUh0OXE2TU0wTG03TE4zRkh3aERFXzRVVU9wbFphaW5fTm5GTXQ4Vi14dG1kSmtsTmd5UVJRNV9RODEyRkVyRUZvOUJYa0UzWDg2RzV6ZEVRMHNNNTI2eTM4al9aUVRrMFduLWRITmtpN182eGJEUDdGSXZmbUNSVnhjd2l6QjJGOFZoLXRfU0I2djg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
