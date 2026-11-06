# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:15:21.072638+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 4, 'ai': 10, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 12 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 572.3300 |
| Return 1D (%) | -1.1674 |
| Return 1W (%) | 5.6037 |
| Return 1M (%) | 13.4990 |
| Return YTD (%) | 13.8625 |
| Return 1Y (%) | 17.0960 |
| Annualized volatility (%) | 15.1705 |
| Beta vs SPY | 0.0399 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 1.1204 |
| Downside deviation (rf=0, %) | 10.0808 |
| Sortino (rf=0) | 1.6861 |
| Historical VaR 95% (1D, %) | 1.4122 |
| Historical ES 95% (1D, %) | 2.0016 |
| Correlation vs SPY | 0.0357 |
| Tracking error vs SPY (%) | 20.0049 |
| P/E (trailing) | 14.39 |
| P/B | 0.00 |
| EV/EBITDA | -1.79 |
| Revenue growth (%) | 10.00 |
| Forward P/E (estimate) | 25.51 |
| Gross margin (%) | 30.33 |
| Operating margin (%) | 32.56 |
| Return on equity (%) | 12.12 |
| Free cash flow yield (%) | 5.87 |
| MA50 | 520.2166 |
| Close vs MA50 (%) | 10.0176 |
| MA200 | 497.2909 |
| Close vs MA200 (%) | 15.0896 |
| RSI (14, Wilder) | 75.1451 |
| MACD (12,26) | 13.7416 |
| MACD signal (9) | 10.7358 |
| MACD histogram | 3.0058 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 572.3300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.1674 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.6037 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 13.4990 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 13.8625 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 17.0960 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 15.1705 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.0808 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6861 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4122 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0016 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0357 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.0049 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0399 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1204 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.5146 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.3320 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.5610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 12.1200 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.8746 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.3946 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 75.1451 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 3.0058 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 10.0176 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 15.0896 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire Hathaway Shares Are Up 11% This Year. Is the Stock a Buy Ahead of Earnings?
- Summary: Berkshire Hathaway Shares Are Up 11% This Year. Is the Stock a Buy Ahead of Earnings?
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPUU1NUDg0VDNtb20zc0VvbENCS09mQjd2SzFCOFdzRlJKcmZDRzUxMEdVTnkwQ0dmSFBVZWM2ZHd6eHczWmtONzJpUmFOVThwRFQzdkNtdzYxaTE3cHg2RTdwQm54dUxGZ2ZoazhPSDJ6b2tyMi1wRmlUYXRfVEVrSlZ0a0N5dzNLWHhxNDNCVS1UQkNKWGNCWUFZbjg0VlU0WnhoR0Y5RnFISHRRS3BPOFFfaUYwR2Nm?oc=5>

### Berkshire Hathaway Stock Has Surged. Can Earnings Keep the Rally Going?
- Summary: Berkshire Hathaway Stock Has Surged. Can Earnings Keep the Rally Going?
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQaFk0ektfOWtITzBVYXRoYXVjVTZub3gyclBPS05TNDR1N1lPSm80Y2lid1dJclQxY2Z6VmpSVGpRTk9NSHFUdzl5M0NHX0phWFUzOXJOV0FNWlJsdnJ0UmhEZU9PSXVLQ1h0UGdlaml5dVJnSml4NVZCRmV3dDdfQzFiWUUySHVLd1pUcQ?oc=5>

### Berkshire Hathaway Inc (BRK.B) Shares Surge 4.0% -- What GF Scor
- Summary: Berkshire Hathaway Inc (BRK.B) Shares Surge 4.0% -- What GF Scor
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOc0w4a19pY1htemludV9nRkY5RnVOcmNxRUoxQzdOakxSUnpYYzFNQU42M29VUjh5ODk3MTZueVpEMUtuZEs4Y3pySnM4TXFUeWxqTzgtQzYxMnFwRmh3S3dKYTlHblJ2em5FNkVlTkZ4TEYyOUI3SGRLenZod3hpSGM3b3d4NW9jZjZnTWctUjZrWjQ4N0dzOVlLeHBuV1pOSlhPTlNWREI3cmUxMzZaM0cta1g4d25kVHc?oc=5>

### Berkshire Hathaway Stock (BRK.B) Hits All-Time High as Market Tanks
- Summary: Berkshire Hathaway Stock (BRK.B) Hits All-Time High as Market Tanks
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQY0FyNElEb0JXNUptbU1IRnJjWHEtekVkVHFZbTA2RmxBcG9ncmxpSWQxeEtmeHltc3hjZFluTGd4eUh4MEZWRUp6VWRmZ0FhcjJXRV9HTGN5Mm5hMlF0a1VFOGxjS3E0dkFUQWN4OGlEdmRBWTR6aFZlVlZBaFZmUEtNZVotYnVhSjBLN1ppUy1vZGNxQ2JkRXEybw?oc=5>

### Berkshire Hathaway's Stock Portfolio Is Worth About 3 Times What It Paid. The Gains Alone Equal About 19% of the Company.
- Summary: Portfolio value tripled, gains 19% of company, indicating strong asset performance.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPWmxkMW4tQXR5X09YUWJIXy1QMFE2VTA1NjkyTEx0MTBmZHRhQUJiTzAxMnBBR0Q0dUhpNVB5VHBrWTJ3N0g2b3RvYkZybnlmM0IyYmpXMHlhNHZQLVM4b0VhOXhxYmNSaEZCRF83WVFiQXVjZDN6bWJQSE9MSFR3TE04akxPWWhzOWtGMC03bVlOei1qeFVWLTBVeVh4QjZFWmtNajNKWGpxZw?oc=5>

## HEADWINDS

### 1 of Greg Abel's Favorite Stocks and a Top 5 Berkshire Hathaway Holding Just Suffered a Devastating Decline
- Summary: A Berkshire holding dropped sharply, impacting portfolio performance.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPTGI0X1ZyaHhPM3BJeFBlRmtFZzBuTm9sbXRLdy1aU1BvQXFUOFZCVG1KWTRoNy1pR1N3dV8waExaeEdNRFVWZ3ZPZHRGdUdrQ1FxbWFGNnF1VzlJVlQtVjRidncwYjB3emk2c3FkR2VYM2tSLW5kWXNlcURwMHViZF93MV9GRDNJOGhMTV9OU0lxT3IwcUZueg?oc=5>

### Berkshire After Buffett: Steady Hands, Big Bets In The Greg Abel Era
- Summary: Berkshire shifts strategy under Greg Abel, continuing steady leadership and significant bets.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOc1FqWWVkbUpRTGV3cVpaa1VnN3N0dk5zYnF6LVhBd1NjczU0UEJmV014ZUdBYno2akE5NTB6cC1XY2VMVnlUeVRoNnJqQ01Qbk5KRll2SlRQZVg2V1JGZDdOaVdmSEFxNWRZeVBCM2QtOUlnRnktM0pyU2FaWGh1dXoyN2Y0U1J6QWpSZmlSWEZSdDV2ODFodjA4QUx2V1p1MkE?oc=5>

## CATALYSTS

### Warren Buffett's 3 Longest-Held Stocks Average a 3,757% Gain and Collectively Deliver $1.53 Billion in Annual Dividend Income for Berkshire Hathaway
- Summary: Three long-held stocks generate $1.53B in dividends for Berkshire.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxOTjVjOWhwZDZXRVRtTjVrcms1YWdnX0IwQnJIbFRFMkRrMWhZR1h3Z1BlQU1HQUZVNmZYelBqZkFYVWFRdEpVNUEyN2Q0OVFoLUVNLTZVb3d3a0lZcUg2YWJFRkNEN21HdjRIdnpvMWduWXhpa0QtN2QtYnZ2bFBrR01qN0FBNWZxdmNKaE1MNHRMQU01M1ZrOTlaOHFNTFZYSDBWWHJVQ2tZamZRNFpoYmRxTG9pVktfTzBvTHNmUmRwZW9adEtGa2pWa0V2MS1vRGJVaEZRQ3dyN0xWblk1LTNEbU9MZw?oc=5>

### Berkshire Hathaway Is Buying More Sirius XM. Here’s What It May See
- Summary: Berkshire Hathaway is increasing its stake in Sirius XM, potentially expanding its media portfolio.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNNmFRR3dWNThYNkVNZUl0SnhGS3JaQ3J3Q2hsN2pseHlNRDJVWTV1dEs1MHRBQUtVNDNJZjg1aHNJTDNfcFhQX2dUcTc1VF9kTFJwbzBWdm1Sd0p0WnRTbTFpZDBEV2dseEhxdVJsZjJyTFBnNHZFN3JGc2U3dVJDTkdkMVBtamNKWENuQmhUdm9UUVB0cDFkQkNnQ0JmMzdmUVRjaA?oc=5>

### 2 Berkshire Hathaway Holdings to Buy After Record Third Quarters
- Summary: Berkshire Hathaway plans to acquire two holdings following record third-quarter performance.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQUzc5U0lRWFB3UWhTdEEzazg2SU5tekdwVTNXWTY1M3MyM0lWbXhiUFpBVUF2MUtBcEFVblN6a3pENzcybFJyNGhWcnZXTU91aHhtZS04QklkelJjZ09qS01RQjFhNUQxQmZNWVI2UUUwei13VzVkM3RGX0ZRUVhEelZBTDg0QkNyamJMVkd2WEM2TUU0dkZfeE1Fd05xeGc?oc=5>

### Berkshire Hathaway Reports Nov. 7 With Its Stock at a Record. Its Cash Pile Is the Number to Watch.
- Summary: Berkshire Hathaway's stock hits record on Nov. 7; cash reserves highlighted.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPZ2V4Z3p0enpkOUJEajZ1N1N0VGxNS3pEZFhXZk1KU2praFo0OUVETFBmVjlfYWgxeWVWVW5STzdQZ2huUFRwdnJMaGN3Y2ttQ1VNZmVxa09vRGFnZzZNTTdMZnpXeHh2aGtLZWJSdXlSU1VBdi1YSFB2SWh4TWtQUi1qSUdic2czb2hqVE9XQWctWlVyVnoyQlVKTFhpdw?oc=5>

### Berkshire Has Gained 16% in About 5 Weeks
- Summary: Berkshire Hathaway shares rose 16% over roughly five weeks, indicating strong investor confidence and positive market performance.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQWDVzSlBjckRRN2JXTjRubUVLb1BCOENjMV9PZzNPQzREZVBNUzd0emhtOHRhQ21MTlkzY21qVXktNEticzJRVFpZdEVrUWZ0MEM5R3gzTlFDbjdLLV9IZ2VzWDZERklMcjJ5UFllMFQyVGJtYmdSS2l4Sm9tVy1HUE82c1pLUzlUeWFrXw?oc=5>

### Greg Abel’s Next 13F Lands November 16, and 1 Question About Berkshire Hathaway’s $299 Billion Portfolio Looms Larger Than Any Other
- Summary: Upcoming 13F filing may reveal portfolio changes, potential impact on holdings.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNNEVVcjVzM2U2T1lJaThYTlZWZUJJdDFGYlVYTWtPNzhUZ2ROcHFsN3JnMXhWWTNMaTlibUVjMldLTGh0RElpdTd6TExzSDFJSEtxR1RmNmQyXzBYSEQ4Uzl1bmdOYW5lQkw2MzB6Z3ExY2kzSGFQYVU3UnF3YV9BcWNhbkFWVW1EQ2t5dEQzY3pHdk0?oc=5>

## RISKS

### Berkshire Hathaway: The Easy Re-Rating Is Gone (NYSE:BRK.A)
- Summary: Berkshire's easy re-rating has disappeared, indicating potential credit risk changes.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPSGUzZzN3eG1yME1RSXRweXlLR3NxLTlqcVYzSDFDd19fN2tJQUdIaWlYNXYyTXVxc1dkSnlvVlFyaVBpcW01a1piYl83SkJuMVVKTWM1RGZ2STVQck9LRVZFNlA5Ykd4XzY1RmVkWGx4dW5FZ3lPeWE1Q1NuY01lZGplUEwtS0RLLXdPbE1Xbw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **14.39** | **0.00** | **-1.79** | **10.00** | **1,225,192,505,344.00 USD** | **17.10** |
| MKL | 13.88 | 1.29 | 7.97 | -11.20 | 23,846,283,264.00 USD | -2.36 |
| FFH.TO | 10.01 | 1.43 | 8.77 | 1.90 | 58,257,702,912.00 CAD | 22.68 |
| L | 15.37 | 1.23 | 8.71 | 1.90 | 22,473,289,728.00 USD | 10.44 |

Peers fetched as_of: 2026-11-05; BRK-B reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-08
- Next expected earnings: 2026-11-07 (yfinance; expected dates may change)

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
- Filing date: 2026-08-10
- Revenue (latest available single quarter): 101,808,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 25,667,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1067983/000119312526341032/brka-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPUU1NUDg0VDNtb20zc0VvbENCS09mQjd2SzFCOFdzRlJKcmZDRzUxMEdVTnkwQ0dmSFBVZWM2ZHd6eHczWmtONzJpUmFOVThwRFQzdkNtdzYxaTE3cHg2RTdwQm54dUxGZ2ZoazhPSDJ6b2tyMi1wRmlUYXRfVEVrSlZ0a0N5dzNLWHhxNDNCVS1UQkNKWGNCWUFZbjg0VlU0WnhoR0Y5RnFISHRRS3BPOFFfaUYwR2Nm?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQRm5DaTN3NmRadmh5LVczYXBueVBlUnhtaDZrQ2FGRGtmS0J1WnRkOWcwQ1FmT1pLN0dwQUV2ajRWZENUTGRFRmRBMEpJdjBMbUVmcnB0ZGxRWTNDRWV6RlItbjBfWndhNWVhVVZuWkxWdUY5RnZmU3h5dVlfaXItdEs4NDN5RVdnTFF6RnNBWXZMTExSRUoyS3B6UTNiSE9qbWx2X3VHNVZYRENl?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQaFk0ektfOWtITzBVYXRoYXVjVTZub3gyclBPS05TNDR1N1lPSm80Y2lid1dJclQxY2Z6VmpSVGpRTk9NSHFUdzl5M0NHX0phWFUzOXJOV0FNWlJsdnJ0UmhEZU9PSXVLQ1h0UGdlaml5dVJnSml4NVZCRmV3dDdfQzFiWUUySHVLd1pUcQ?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOc0w4a19pY1htemludV9nRkY5RnVOcmNxRUoxQzdOakxSUnpYYzFNQU42M29VUjh5ODk3MTZueVpEMUtuZEs4Y3pySnM4TXFUeWxqTzgtQzYxMnFwRmh3S3dKYTlHblJ2em5FNkVlTkZ4TEYyOUI3SGRLenZod3hpSGM3b3d4NW9jZjZnTWctUjZrWjQ4N0dzOVlLeHBuV1pOSlhPTlNWREI3cmUxMzZaM0cta1g4d25kVHc?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQY0FyNElEb0JXNUptbU1IRnJjWHEtekVkVHFZbTA2RmxBcG9ncmxpSWQxeEtmeHltc3hjZFluTGd4eUh4MEZWRUp6VWRmZ0FhcjJXRV9HTGN5Mm5hMlF0a1VFOGxjS3E0dkFUQWN4OGlEdmRBWTR6aFZlVlZBaFZmUEtNZVotYnVhSjBLN1ppUy1vZGNxQ2JkRXEybw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPWmxkMW4tQXR5X09YUWJIXy1QMFE2VTA1NjkyTEx0MTBmZHRhQUJiTzAxMnBBR0Q0dUhpNVB5VHBrWTJ3N0g2b3RvYkZybnlmM0IyYmpXMHlhNHZQLVM4b0VhOXhxYmNSaEZCRF83WVFiQXVjZDN6bWJQSE9MSFR3TE04akxPWWhzOWtGMC03bVlOei1qeFVWLTBVeVh4QjZFWmtNajNKWGpxZw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPTGI0X1ZyaHhPM3BJeFBlRmtFZzBuTm9sbXRLdy1aU1BvQXFUOFZCVG1KWTRoNy1pR1N3dV8waExaeEdNRFVWZ3ZPZHRGdUdrQ1FxbWFGNnF1VzlJVlQtVjRidncwYjB3emk2c3FkR2VYM2tSLW5kWXNlcURwMHViZF93MV9GRDNJOGhMTV9OU0lxT3IwcUZueg?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOc1FqWWVkbUpRTGV3cVpaa1VnN3N0dk5zYnF6LVhBd1NjczU0UEJmV014ZUdBYno2akE5NTB6cC1XY2VMVnlUeVRoNnJqQ01Qbk5KRll2SlRQZVg2V1JGZDdOaVdmSEFxNWRZeVBCM2QtOUlnRnktM0pyU2FaWGh1dXoyN2Y0U1J6QWpSZmlSWEZSdDV2ODFodjA4QUx2V1p1MkE?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxOTjVjOWhwZDZXRVRtTjVrcms1YWdnX0IwQnJIbFRFMkRrMWhZR1h3Z1BlQU1HQUZVNmZYelBqZkFYVWFRdEpVNUEyN2Q0OVFoLUVNLTZVb3d3a0lZcUg2YWJFRkNEN21HdjRIdnpvMWduWXhpa0QtN2QtYnZ2bFBrR01qN0FBNWZxdmNKaE1MNHRMQU01M1ZrOTlaOHFNTFZYSDBWWHJVQ2tZamZRNFpoYmRxTG9pVktfTzBvTHNmUmRwZW9adEtGa2pWa0V2MS1vRGJVaEZRQ3dyN0xWblk1LTNEbU9MZw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNNmFRR3dWNThYNkVNZUl0SnhGS3JaQ3J3Q2hsN2pseHlNRDJVWTV1dEs1MHRBQUtVNDNJZjg1aHNJTDNfcFhQX2dUcTc1VF9kTFJwbzBWdm1Sd0p0WnRTbTFpZDBEV2dseEhxdVJsZjJyTFBnNHZFN3JGc2U3dVJDTkdkMVBtamNKWENuQmhUdm9UUVB0cDFkQkNnQ0JmMzdmUVRjaA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQUzc5U0lRWFB3UWhTdEEzazg2SU5tekdwVTNXWTY1M3MyM0lWbXhiUFpBVUF2MUtBcEFVblN6a3pENzcybFJyNGhWcnZXTU91aHhtZS04QklkelJjZ09qS01RQjFhNUQxQmZNWVI2UUUwei13VzVkM3RGX0ZRUVhEelZBTDg0QkNyamJMVkd2WEM2TUU0dkZfeE1Fd05xeGc?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPZ2V4Z3p0enpkOUJEajZ1N1N0VGxNS3pEZFhXZk1KU2praFo0OUVETFBmVjlfYWgxeWVWVW5STzdQZ2huUFRwdnJMaGN3Y2ttQ1VNZmVxa09vRGFnZzZNTTdMZnpXeHh2aGtLZWJSdXlSU1VBdi1YSFB2SWh4TWtQUi1qSUdic2czb2hqVE9XQWctWlVyVnoyQlVKTFhpdw?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQRTFYN1AwWVpyUUxvMWF3R004djZQc0ljZFpSUmtzckhuU1hTX0dhZnBzNkk2UUw4d0VjTHBBbXUwTlUwUFhReGt2TmdIUVhnZzVpbjY5cy1XeTRnWi10MTlubVhxdDIxS2s0bExjWmQ0U3VhYmpfOFYzUWdTXzU4dElmUUJVcl85VUJiS2w3c0c3TTg5Q1plYzVPcnJjTGQ3OEFHTDJyNHVoZDNXTkNuZk1xRko5eXFMQXdjclR0OWp5ZUtNR0FwUFJoRmxpR2xIYkxOVVF3?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQWDVzSlBjckRRN2JXTjRubUVLb1BCOENjMV9PZzNPQzREZVBNUzd0emhtOHRhQ21MTlkzY21qVXktNEticzJRVFpZdEVrUWZ0MEM5R3gzTlFDbjdLLV9IZ2VzWDZERklMcjJ5UFllMFQyVGJtYmdSS2l4Sm9tVy1HUE82c1pLUzlUeWFrXw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQUFpYMmxkRm1HSmhmakE3UFV6MExlakxTRVJrVUxGLWdHTF9rMV9iS2c1ZE9mMkJZSFByVjR2VV9sWnBoNnlNaEZSYkNOcjhXRVlFNWRWVWhUYXVXdHpwMGtuUkRITG1jWi1rTnFkd2JTR3NnZzN4VWVXSHMtWmVDeUtEZnNzMmxUWjg5OFNfdkhZeUczNGRr?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNNEVVcjVzM2U2T1lJaThYTlZWZUJJdDFGYlVYTWtPNzhUZ2ROcHFsN3JnMXhWWTNMaTlibUVjMldLTGh0RElpdTd6TExzSDFJSEtxR1RmNmQyXzBYSEQ4Uzl1bmdOYW5lQkw2MzB6Z3ExY2kzSGFQYVU3UnF3YV9BcWNhbkFWVW1EQ2t5dEQzY3pHdk0?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPSGUzZzN3eG1yME1RSXRweXlLR3NxLTlqcVYzSDFDd19fN2tJQUdIaWlYNXYyTXVxc1dkSnlvVlFyaVBpcW01a1piYl83SkJuMVVKTWM1RGZ2STVQck9LRVZFNlA5Ykd4XzY1RmVkWGx4dW5FZ3lPeWE1Q1NuY01lZGplUEwtS0RLLXdPbE1Xbw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
