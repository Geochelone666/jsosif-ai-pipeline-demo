# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T05:03:05.545783+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 14, 'rule': 4, 'ai': 8, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'short_term_price_move_in_structural_risks': 2}
- RSS source audit (metadata only, not article fact-checking): 14 unique headlines; 8 named publishers; 1 exact duplicates; 14 HTTPS source links; largest publisher share 42.86%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 62.1500 |
| Return 1D (%) | -0.8614 |
| Return 1W (%) | -1.9871 |
| Return 1M (%) | -11.7939 |
| Return YTD (%) | -33.7137 |
| Return 1Y (%) | -46.1546 |
| Annualized volatility (%) | 36.3380 |
| Beta vs SPY | 0.2507 |
| Max drawdown (%) | -46.2932 |
| Sharpe (rf=0) | -1.5280 |
| Downside deviation (rf=0, %) | 26.8021 |
| Sortino (rf=0) | -2.0717 |
| Historical VaR 95% (1D, %) | 3.5133 |
| Historical ES 95% (1D, %) | 5.1308 |
| Correlation vs SPY | 0.0940 |
| Tracking error vs SPY (%) | 37.5918 |
| P/E (trailing) | 18.12 |
| P/B | 8.71 |
| EV/EBITDA | 16.58 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 16.48 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 31.30 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 9.98 |
| MA50 | 69.1846 |
| Close vs MA50 (%) | -10.1679 |
| MA200 | 80.4978 |
| Close vs MA200 (%) | -22.7930 |
| RSI (14, Wilder) | 38.4347 |
| MACD (12,26) | -1.7743 |
| MACD signal (9) | -1.9455 |
| MACD histogram | 0.1712 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 62.1500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.8614 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.9871 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.7939 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -33.7137 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -46.1546 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.3380 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.8021 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -2.0717 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.5133 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1308 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0940 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.5918 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2507 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -46.2932 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.5280 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.4796 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.2960 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.9824 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.1195 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.4347 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1712 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -10.1679 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -22.7930 -> Clearly below the moving-average trend level.

## TAILWINDS

### Netflix (NASDAQ:NFLX) Stock Price Up 2% - Still a Buy?
- Summary: Netflix (NASDAQ:NFLX) Stock Price Up 2% - Still a Buy?
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQbzlDR0VxOXVJdFVoencteUVUN2pRbjZjVlVXdDluRFhRSnZrWUMtOEZHR3IwZ1EtMXRvTHdzWW80MVA2Qld3YnNvQmxPTkJ6bGRNaE9GYlpkNGVGVG96SVJhV2wtNG5BRkVYcDc3cDVVcUU4SlhZWmxIZHg0XzFIQXRYQk9naHNJbzRaU0FjZnRieWxNX2FaSFJabnB2YVV0Y0JXb2Q2cWw5YmN3?oc=5>

### Should Netflix (NFLX) Investors Rethink Its Outlook After Bill Ackman’s Fresh Backing?
- Summary: Bill Ackman’s fresh backing signals renewed confidence in Netflix, potentially boosting investor sentiment.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQUDBZc0M0UWw0WE5Wb2R0UXpESl9BRDJjZnZqWEh4R2lTVmdtM0ZaTGxKRmd4dHR6Nk9hMmdkNWhaaGtCWjJMQktaU3hySWU4TUpLYmV4eDZvTW5Id0hrNlNhTTM1OHpTWG5GLWpFajRuT1VQZkxIVVZpWGdncW9xb25nVWdJVzdjZDNaZUZhWC1SdnJMcnc2NjhMMEZET25zZW5xZlJn?oc=5>

### Billionaire investor Bill Ackman on why he's staying bullish on Netflix
- Summary: Ackman remains bullish, indicating strong support for Netflix’s future prospects.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxPN2FXdVM4Rlh5TzBFZjVTOHRLS05zTmJhd1FvRm5kMXRGZUY3RV9Sd3hRUHZKMUV3eGlURzFwclBueGRlRlhhVmRUTWhJNGFObVByaGpMcWwzZHJydU9Hc3VmVDFYOVNUT2dKdDNjc0h4ZXZkT3lWZTlVRUlrSkZjX3pPUmdWckNUeEt2dVY3TmphMHI4YUFTelgxa2xZcWJBZ3dBME9DcVZOM3pRTGlFcmpyZWZIVE5KY3ROcXNGbWlPclFUTjJHMjYwWDloN0U?oc=5>

### Netflix (NASDAQ: NFLX) Stock Trades At A Decade-Low Valuation As Its Advertising Business Holds The Key To A Potential Rebound
- Summary: Low valuation and a growing advertising business suggest a potential rebound for Netflix.
- Date: 2026-11-13 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiggJBVV95cUxNZV9WTjdQZmFwMWNGZWNtd29sOElEaHVLTDB0MlJuamJVdVQzT0l6TmVhbnVkc2gxUE9xMFBnOG1FZEFBNG85d0RDY0lOVWdjaC1MN3RVdXJRdWd4enRvUGFRYmJ4TE9vWV9wTldScFV6OEE0ZzJyWnJFRXZZZkpxU1NsQjRrQ2xBU0RYcEJWbUpjM1pjd0FmYmxKZXlvbmZGVENjYzQ0Q0R3OWJWQzhlYTdWbmhrVTFlZTdJX2pmQzFLaHJyVmVheXd4alRsQzBINF9uTlNPNVVzZVNOWjdWWVRXZEV4c2I5bC15UTZIenhzYjN6N3M1aHlTVGtFWFZqUEE?oc=5>

### Netflix (NASDAQ:NFLX): An Affordable Growth Case at a Reasonable Valuation
- Summary: Analyst highlights Netflix’s growth potential and attractive valuation, suggesting a positive outlook for investors.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxNYmRwTkx0blZpOFRhclpZb0JOQjlhQ3d0amhqOGhBWnppUHE3SUNwQnFBMUJmX1Z2RkM2dndBWHM4ZC1Vdkk4OWYwSjNVSXVJSkl3MEh1VmdiLTJObTBORG9jQmhNWFFFek90Y250TGlNaWNfOThDWWRneTdXNXZRX1BsWnJhMERqUXZicnUzX2VjcEVRcGhtR1RRREJzRnA5Qnp0eUF0NkJjamNkOFpaeXZvYjFobUhXYkpRODNUNA?oc=5>

## HEADWINDS

### Netflix (NASDAQ:NFLX) Stock Price Down 2.9% - What's Next?
- Summary: Netflix (NASDAQ:NFLX) Stock Price Down 2.9% - What's Next?
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQRTBpV1JIUGU2aXI3T2FBelhEaTA3dmxtZDNlNkZueDdlaHQ4YzltZWhVRHhTYXY0OTVad1NidG9kNDMwbE96cTlOVVhXbWZHa2ItUGJKSk42Tk1ESVZDOHBpTjc3dlVnckh3clpwY01XMTIwc0JFajRLYlFld0lfeTNJSkhPWFQ5VGVQVzVSQlQ2aWE3R2xxbk1wUDJkeXZMc1hVeVlGV2ROZW5CZDNN?oc=5>

### Netflix (NFLX) Stock May Be a ‘Loser’ This Year, But You Can Still Scalp Profits From It
- Summary: Shares may underperform this year, but short-term trading opportunities remain.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQaF9lS2lHZnpDYmpGM3FsQXdWZmJGV29qb05VNGJXQkR0SVhQV2JaLUNFWjFpb3VjTDFHeXFJUHhNZkd3b0U4Rk5TcXBZOWZVRF9GZFFTd3dwSEJhMmdjbzV6MFg3dEtwQWtTS1ZXLXU3UmQ4YXB2aFAzUFBiTHdfd1VhZ1Q2ZGlyeVpjQUlPbXJkVEtkUm5uMTlacklKaWlENDdGWXJyXzdYbTJ5c0NvamlGS01SdzQzNkR0SmIycmlaUzJHN2c?oc=5>

### Why Netflix Stock Plunged 11% in October
- Summary: October decline attributed to earnings miss and subscriber slowdown.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPVEFpUE1pTmNGWWlJcl8zOTdBeXJKeEpiejc2cUtJLXJfYnlsanktbGxyMjBMM1c4Y0I1NDVkcEdNenRxV0VZTzJjc3Jia1dHMERFUEpVQmNvMnNTbTEtMkJCZF9iV09vbk9TNzNOOEN6UVBacUU2S0pERzk5Y01TWnBJS2N3U09LdjFHTl9Gb0g5QVNGb0ZqNQ?oc=5>

## CATALYSTS

### Netflix (NFLX) Stock Looks Cheap With 23% Upside To Fair Value
- Summary: Netflix (NFLX) Stock Looks Cheap With 23% Upside To Fair Value
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNU3JaOWhSd2RhT3RScnpyQWRnWGRTZ0w4UjcteEJfY0phVVQ2UWlfLVctbEtFZnptSkU2Y2RiRDJfNFYwYWtHR21CaV8xdUxWYW8xNzNmOGR5U1hzQzhhX2hWam1iUHFHSnRCb2E2RG9CUU9kZHhMZGh5cldLcllMTjFXdTVfWGdDaGJUTWYtNzNBOFVLOGZFZ2x0NA?oc=5>

### Netflix Split Its Stock 10-for-1 One Year Ago, and $1,000 Invested Right After Is Now Worth $568
- Summary: Netflix Split Its Stock 10-for-1 One Year Ago, and $1,000 Invested Right After Is Now Worth $568
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxPYi16Q2dXbTZYM3lhVUVIdENPbXZxS1d1ZXRYOXM4R1NaX3ZQSWIzQXBBN2VTV29qRmhrYmQzZG0wZTJrWXlHS0t4Mjg1SUJYQUxwQlRna0swMWw3TUJmeUtBNHpxNjVIcW1ZcXR4SDdvWjNVZmxaU0pvSDZjZElpQ1hnUGstb3Rnb3JtbG1HYU84Y0w0eWNhb1otTkxjelp1T2Y3ZGRyTWJnSzloVm9DWWlQSFduU1RSSUNrM0JKQW5kYlRuQWhuMGtVa2xsbWZNWmc?oc=5>

## RISKS

### Options Traders Show Cautious Sentiment as Netflix (NFLX) Stock Dips Near Two-Year Low
- Summary: Options traders exhibit caution as Netflix stock falls close to a two‑year low, signaling potential downside pressure.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxNR1hfR2dPTlhsdURFRlJDMEtYZEVlclRRNktic2dBMkd4cU1IMzVGLW1IdEQ3OXBXTEx2SkJXVkRjZ1R6LVlCZFZkeTRoSjEyZUdRVTBTelJ6anBLZmMzYUd4d194RG8xa0hiWnQ5UjNmR1V0ZUJ5SDhWSnE4UU1SdHlMRXZpSTBuTnBYYXNRQ2NHZVJGT2dHbHpWbEdVQjN3V0t3NXFVSGYxRlloZzI5SERVbnBjMFFySk1OeDBuQQ?oc=5>

### Netflix (NFLX) Price Prediction: Rally stalls under resistance as momentum stays mixed
- Summary: Analysts predict a stalled rally for Netflix, with resistance levels holding and momentum remaining mixed.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQYmVaOGVVZFdrVGZtcWxBRlNrZHJRcEhEeVlveW9QNF9PS2hlbnhwLW9JNXV3ZXl2M3djX0ZJWnUyNUVUbDlWX1ZTZmVOM1dIUkU3WTlTeEV1MUprbjZFbG1OVkI3VFYtU1ZCemJ1azA2VFFNUXZKTHBYTzBnd21saW0wdTdXSUoyVm1pUlBFVllHbHQ5Y1FjMzdMdVE2ZDU4X0VZ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **18.12** | **8.71** | **16.58** | **11.80** | **255,208,161,280.00 USD** | **-46.15** |
| DIS | 24.38 | 1.87 | 12.07 | 6.80 | 205,423,935,488.00 USD | 12.16 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 7.86 | 0.97 | 5.05 | -6.10 | 89,343,311,872.00 USD | 1.12 |

Peers fetched as_of: 2026-11-13; NFLX reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 12,874,176,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,663,927,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMirAFBVV95cUxQbzlDR0VxOXVJdFVoencteUVUN2pRbjZjVlVXdDluRFhRSnZrWUMtOEZHR3IwZ1EtMXRvTHdzWW80MVA2Qld3YnNvQmxPTkJ6bGRNaE9GYlpkNGVGVG96SVJhV2wtNG5BRkVYcDc3cDVVcUU4SlhZWmxIZHg0XzFIQXRYQk9naHNJbzRaU0FjZnRieWxNX2FaSFJabnB2YVV0Y0JXb2Q2cWw5YmN3?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQUDBZc0M0UWw0WE5Wb2R0UXpESl9BRDJjZnZqWEh4R2lTVmdtM0ZaTGxKRmd4dHR6Nk9hMmdkNWhaaGtCWjJMQktaU3hySWU4TUpLYmV4eDZvTW5Id0hrNlNhTTM1OHpTWG5GLWpFajRuT1VQZkxIVVZpWGdncW9xb25nVWdJVzdjZDNaZUZhWC1SdnJMcnc2NjhMMEZET25zZW5xZlJn?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxPN2FXdVM4Rlh5TzBFZjVTOHRLS05zTmJhd1FvRm5kMXRGZUY3RV9Sd3hRUHZKMUV3eGlURzFwclBueGRlRlhhVmRUTWhJNGFObVByaGpMcWwzZHJydU9Hc3VmVDFYOVNUT2dKdDNjc0h4ZXZkT3lWZTlVRUlrSkZjX3pPUmdWckNUeEt2dVY3TmphMHI4YUFTelgxa2xZcWJBZ3dBME9DcVZOM3pRTGlFcmpyZWZIVE5KY3ROcXNGbWlPclFUTjJHMjYwWDloN0U?oc=5
- https://news.google.com/rss/articles/CBMiggJBVV95cUxNZV9WTjdQZmFwMWNGZWNtd29sOElEaHVLTDB0MlJuamJVdVQzT0l6TmVhbnVkc2gxUE9xMFBnOG1FZEFBNG85d0RDY0lOVWdjaC1MN3RVdXJRdWd4enRvUGFRYmJ4TE9vWV9wTldScFV6OEE0ZzJyWnJFRXZZZkpxU1NsQjRrQ2xBU0RYcEJWbUpjM1pjd0FmYmxKZXlvbmZGVENjYzQ0Q0R3OWJWQzhlYTdWbmhrVTFlZTdJX2pmQzFLaHJyVmVheXd4alRsQzBINF9uTlNPNVVzZVNOWjdWWVRXZEV4c2I5bC15UTZIenhzYjN6N3M1aHlTVGtFWFZqUEE?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxNYmRwTkx0blZpOFRhclpZb0JOQjlhQ3d0amhqOGhBWnppUHE3SUNwQnFBMUJmX1Z2RkM2dndBWHM4ZC1Vdkk4OWYwSjNVSXVJSkl3MEh1VmdiLTJObTBORG9jQmhNWFFFek90Y250TGlNaWNfOThDWWRneTdXNXZRX1BsWnJhMERqUXZicnUzX2VjcEVRcGhtR1RRREJzRnA5Qnp0eUF0NkJjamNkOFpaeXZvYjFobUhXYkpRODNUNA?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQRTBpV1JIUGU2aXI3T2FBelhEaTA3dmxtZDNlNkZueDdlaHQ4YzltZWhVRHhTYXY0OTVad1NidG9kNDMwbE96cTlOVVhXbWZHa2ItUGJKSk42Tk1ESVZDOHBpTjc3dlVnckh3clpwY01XMTIwc0JFajRLYlFld0lfeTNJSkhPWFQ5VGVQVzVSQlQ2aWE3R2xxbk1wUDJkeXZMc1hVeVlGV2ROZW5CZDNN?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQaF9lS2lHZnpDYmpGM3FsQXdWZmJGV29qb05VNGJXQkR0SVhQV2JaLUNFWjFpb3VjTDFHeXFJUHhNZkd3b0U4Rk5TcXBZOWZVRF9GZFFTd3dwSEJhMmdjbzV6MFg3dEtwQWtTS1ZXLXU3UmQ4YXB2aFAzUFBiTHdfd1VhZ1Q2ZGlyeVpjQUlPbXJkVEtkUm5uMTlacklKaWlENDdGWXJyXzdYbTJ5c0NvamlGS01SdzQzNkR0SmIycmlaUzJHN2c?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPVEFpUE1pTmNGWWlJcl8zOTdBeXJKeEpiejc2cUtJLXJfYnlsanktbGxyMjBMM1c4Y0I1NDVkcEdNenRxV0VZTzJjc3Jia1dHMERFUEpVQmNvMnNTbTEtMkJCZF9iV09vbk9TNzNOOEN6UVBacUU2S0pERzk5Y01TWnBJS2N3U09LdjFHTl9Gb0g5QVNGb0ZqNQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNU3JaOWhSd2RhT3RScnpyQWRnWGRTZ0w4UjcteEJfY0phVVQ2UWlfLVctbEtFZnptSkU2Y2RiRDJfNFYwYWtHR21CaV8xdUxWYW8xNzNmOGR5U1hzQzhhX2hWam1iUHFHSnRCb2E2RG9CUU9kZHhMZGh5cldLcllMTjFXdTVfWGdDaGJUTWYtNzNBOFVLOGZFZ2x0NA?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxPYi16Q2dXbTZYM3lhVUVIdENPbXZxS1d1ZXRYOXM4R1NaX3ZQSWIzQXBBN2VTV29qRmhrYmQzZG0wZTJrWXlHS0t4Mjg1SUJYQUxwQlRna0swMWw3TUJmeUtBNHpxNjVIcW1ZcXR4SDdvWjNVZmxaU0pvSDZjZElpQ1hnUGstb3Rnb3JtbG1HYU84Y0w0eWNhb1otTkxjelp1T2Y3ZGRyTWJnSzloVm9DWWlQSFduU1RSSUNrM0JKQW5kYlRuQWhuMGtVa2xsbWZNWmc?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxNR1hfR2dPTlhsdURFRlJDMEtYZEVlclRRNktic2dBMkd4cU1IMzVGLW1IdEQ3OXBXTEx2SkJXVkRjZ1R6LVlCZFZkeTRoSjEyZUdRVTBTelJ6anBLZmMzYUd4d194RG8xa0hiWnQ5UjNmR1V0ZUJ5SDhWSnE4UU1SdHlMRXZpSTBuTnBYYXNRQ2NHZVJGT2dHbHpWbEdVQjN3V0t3NXFVSGYxRlloZzI5SERVbnBjMFFySk1OeDBuQQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQYmVaOGVVZFdrVGZtcWxBRlNrZHJRcEhEeVlveW9QNF9PS2hlbnhwLW9JNXV3ZXl2M3djX0ZJWnUyNUVUbDlWX1ZTZmVOM1dIUkU3WTlTeEV1MUprbjZFbG1OVkI3VFYtU1ZCemJ1azA2VFFNUXZKTHBYTzBnd21saW0wdTdXSUoyVm1pUlBFVllHbHQ5Y1FjMzdMdVE2ZDU4X0VZ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
