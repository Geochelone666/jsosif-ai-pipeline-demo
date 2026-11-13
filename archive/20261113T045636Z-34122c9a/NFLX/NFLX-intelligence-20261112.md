# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:18:02.172103+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 4, 'ai': 7, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'low_uncalibrated_model_confidence': 1, 'short_term_price_move_in_structural_risks': 2}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 8 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 27.27%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 62.6900 |
| Return 1D (%) | -2.8664 |
| Return 1W (%) | -4.3777 |
| Return 1M (%) | -11.2165 |
| Return YTD (%) | -33.1378 |
| Return 1Y (%) | -45.8402 |
| Annualized volatility (%) | 36.3323 |
| Beta vs SPY | 0.2461 |
| Max drawdown (%) | -46.4449 |
| Sharpe (rf=0) | -1.5123 |
| Downside deviation (rf=0, %) | 26.7896 |
| Sortino (rf=0) | -2.0510 |
| Historical VaR 95% (1D, %) | 3.5133 |
| Historical ES 95% (1D, %) | 5.1308 |
| Correlation vs SPY | 0.0930 |
| Tracking error vs SPY (%) | 37.6274 |
| P/E (trailing) | 18.12 |
| P/B | 8.79 |
| EV/EBITDA | 16.72 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 16.62 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 31.30 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 9.90 |
| MA50 | 69.5950 |
| Close vs MA50 (%) | -9.9217 |
| MA200 | 80.6029 |
| Close vs MA200 (%) | -22.2236 |
| RSI (14, Wilder) | 39.7247 |
| MACD (12,26) | -1.7464 |
| MACD signal (9) | -1.9883 |
| MACD histogram | 0.2418 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 62.6900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.8664 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.3777 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.2165 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -33.1378 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -45.8402 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.3323 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.7896 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -2.0510 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.5133 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1308 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0930 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.6274 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2461 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -46.4449 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.5123 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.6227 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.2960 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.8964 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.1185 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 39.7247 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2418 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.9217 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -22.2236 -> Clearly below the moving-average trend level.

## TAILWINDS

### Netflix (NASDAQ:NFLX) Stock Price Up 2% - Still a Buy?
- Summary: Netflix (NASDAQ:NFLX) Stock Price Up 2% - Still a Buy?
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQbzlDR0VxOXVJdFVoencteUVUN2pRbjZjVlVXdDluRFhRSnZrWUMtOEZHR3IwZ1EtMXRvTHdzWW80MVA2Qld3YnNvQmxPTkJ6bGRNaE9GYlpkNGVGVG96SVJhV2wtNG5BRkVYcDc3cDVVcUU4SlhZWmxIZHg0XzFIQXRYQk9naHNJbzRaU0FjZnRieWxNX2FaSFJabnB2YVV0Y0JXb2Q2cWw5YmN3?oc=5>

## HEADWINDS

### Netflix (NASDAQ:NFLX) Stock Price Down 2.9% - What's Next?
- Summary: Netflix (NASDAQ:NFLX) Stock Price Down 2.9% - What's Next?
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQRTBpV1JIUGU2aXI3T2FBelhEaTA3dmxtZDNlNkZueDdlaHQ4YzltZWhVRHhTYXY0OTVad1NidG9kNDMwbE96cTlOVVhXbWZHa2ItUGJKSk42Tk1ESVZDOHBpTjc3dlVnckh3clpwY01XMTIwc0JFajRLYlFld0lfeTNJSkhPWFQ5VGVQVzVSQlQ2aWE3R2xxbk1wUDJkeXZMc1hVeVlGV2ROZW5CZDNN?oc=5>

### Netflix Stock (NASDAQ:NFLX) Slips Despite New Stranger Things Plans
- Summary: Netflix Stock (NASDAQ:NFLX) Slips Despite New Stranger Things Plans
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPd1NLeHE4Skdqd3NHRk8wSEtWSlpVazJfcEZVV0FjT0gzdElUQjEwWUs0LXdqeE9PZTAzcGNiZTJLMHNNS0h6TGVSOExwb3puOU9ybUliWHNsb2pYbnhVWjNQSXo4bjYtWFlWWHRLdWRjbFZ1ekc5c1lWWE95YXB2d1NrMXVjdDliUFJGVktOQUlBM1NBZTRlREhR?oc=5>

### Netflix (NFLX) Stock May Be a ‘Loser’ This Year, But You Can Still Scalp Profits From It
- Summary: Shares may underperform this year, but short-term trading opportunities remain.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQaF9lS2lHZnpDYmpGM3FsQXdWZmJGV29qb05VNGJXQkR0SVhQV2JaLUNFWjFpb3VjTDFHeXFJUHhNZkd3b0U4Rk5TcXBZOWZVRF9GZFFTd3dwSEJhMmdjbzV6MFg3dEtwQWtTS1ZXLXU3UmQ4YXB2aFAzUFBiTHdfd1VhZ1Q2ZGlyeVpjQUlPbXJkVEtkUm5uMTlacklKaWlENDdGWXJyXzdYbTJ5c0NvamlGS01SdzQzNkR0SmIycmlaUzJHN2c?oc=5>

### Why Netflix Stock Plunged 11% in October
- Summary: October decline attributed to earnings miss and subscriber slowdown.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPVEFpUE1pTmNGWWlJcl8zOTdBeXJKeEpiejc2cUtJLXJfYnlsanktbGxyMjBMM1c4Y0I1NDVkcEdNenRxV0VZTzJjc3Jia1dHMERFUEpVQmNvMnNTbTEtMkJCZF9iV09vbk9TNzNOOEN6UVBacUU2S0pERzk5Y01TWnBJS2N3U09LdjFHTl9Gb0g5QVNGb0ZqNQ?oc=5>

### What Could Lift Netflix Stock From Here?
- Summary: Potential upside from new content releases and subscriber growth.
- Date: 2026-11-10 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOR3V0UlpQTXZmZWVHUFVqdlk1NFAtUnlnc0xEREt4OE5oVkZQQ3VpbHhLZ0V6OEl5OTJBUzlrS2NURVcyVzdBeE5MYk5LMGVPZUQxOE1RMzE0VUdSZDVTeEREX2dBNGdPNFVXNnVSb3FQR0JTVE9VaU9XOWgwdV9qNVotaW1rU2JpNUw3b09kZlVtbDJIN2NkUFpRQnp4OTJCNlE?oc=5>

### Investors Heavily Search Netflix, Inc. (NFLX): Here is What You Need to Know
- Summary: High search volume indicates growing investor interest.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxObDB2cXZhTTBKYndDM1lOMlFGM1BEbTFyR21MSVRWM2JrMWxJSUVWNWtQU1ZQLXN2a25sMW54TWxXX3p1eG91Q2ZPNlpSUHlqSzhWaVhnRk9faXdKUmNCaGppSHl4dHBvRnpYRXpIQnIxcE9oZDdFTVRhdFdoOVNQeV9ZQUxNZ2k5QjR6NHc1M29hbGNCNmhBZHJEcjVINzJ4VE9j?oc=5>

## CATALYSTS

### Netflix (NFLX) Stock Looks Cheap With 23% Upside To Fair Value
- Summary: Netflix (NFLX) Stock Looks Cheap With 23% Upside To Fair Value
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNU3JaOWhSd2RhT3RScnpyQWRnWGRTZ0w4UjcteEJfY0phVVQ2UWlfLVctbEtFZnptSkU2Y2RiRDJfNFYwYWtHR21CaV8xdUxWYW8xNzNmOGR5U1hzQzhhX2hWam1iUHFHSnRCb2E2RG9CUU9kZHhMZGh5cldLcllMTjFXdTVfWGdDaGJUTWYtNzNBOFVLOGZFZ2x0NA?oc=5>

### Insider trades: Netflix, Intel, Visa among notable names (V:NYSE)
- Summary: Insider trading activity involving Netflix shares noted, indicating potential insider confidence or strategic moves.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPU1FaN0dLTS0xR2F6NmtmajJrblZBaHV2MGFEbURkU0x5Si1Jd2RadThjZWxIYjVwM0sxcHBsWGdtN2UwWHJvbGNvTkJzUkFLNkU5SXVESGNBWHZDUlZVSFR1QlF4R21yU3JUT25MUWNBLXBkSHVsdnBoTjVaMWpZVTBmV01JclZ6RWk4WlFIbFR1QlJNV1E?oc=5>

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
| **NFLX** | **18.12** | **8.79** | **16.72** | **11.80** | **257,425,571,840.00 USD** | **-45.84** |
| DIS | 24.38 | 1.86 | 12.01 | 6.80 | 204,146,196,480.00 USD | 2.82 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 7.85 | 0.95 | 5.01 | -6.10 | 88,064,950,272.00 USD | -0.04 |

Peers fetched as_of: 2026-11-12; NFLX reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

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
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQRTBpV1JIUGU2aXI3T2FBelhEaTA3dmxtZDNlNkZueDdlaHQ4YzltZWhVRHhTYXY0OTVad1NidG9kNDMwbE96cTlOVVhXbWZHa2ItUGJKSk42Tk1ESVZDOHBpTjc3dlVnckh3clpwY01XMTIwc0JFajRLYlFld0lfeTNJSkhPWFQ5VGVQVzVSQlQ2aWE3R2xxbk1wUDJkeXZMc1hVeVlGV2ROZW5CZDNN?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPd1NLeHE4Skdqd3NHRk8wSEtWSlpVazJfcEZVV0FjT0gzdElUQjEwWUs0LXdqeE9PZTAzcGNiZTJLMHNNS0h6TGVSOExwb3puOU9ybUliWHNsb2pYbnhVWjNQSXo4bjYtWFlWWHRLdWRjbFZ1ekc5c1lWWE95YXB2d1NrMXVjdDliUFJGVktOQUlBM1NBZTRlREhR?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQaF9lS2lHZnpDYmpGM3FsQXdWZmJGV29qb05VNGJXQkR0SVhQV2JaLUNFWjFpb3VjTDFHeXFJUHhNZkd3b0U4Rk5TcXBZOWZVRF9GZFFTd3dwSEJhMmdjbzV6MFg3dEtwQWtTS1ZXLXU3UmQ4YXB2aFAzUFBiTHdfd1VhZ1Q2ZGlyeVpjQUlPbXJkVEtkUm5uMTlacklKaWlENDdGWXJyXzdYbTJ5c0NvamlGS01SdzQzNkR0SmIycmlaUzJHN2c?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPVEFpUE1pTmNGWWlJcl8zOTdBeXJKeEpiejc2cUtJLXJfYnlsanktbGxyMjBMM1c4Y0I1NDVkcEdNenRxV0VZTzJjc3Jia1dHMERFUEpVQmNvMnNTbTEtMkJCZF9iV09vbk9TNzNOOEN6UVBacUU2S0pERzk5Y01TWnBJS2N3U09LdjFHTl9Gb0g5QVNGb0ZqNQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOR3V0UlpQTXZmZWVHUFVqdlk1NFAtUnlnc0xEREt4OE5oVkZQQ3VpbHhLZ0V6OEl5OTJBUzlrS2NURVcyVzdBeE5MYk5LMGVPZUQxOE1RMzE0VUdSZDVTeEREX2dBNGdPNFVXNnVSb3FQR0JTVE9VaU9XOWgwdV9qNVotaW1rU2JpNUw3b09kZlVtbDJIN2NkUFpRQnp4OTJCNlE?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxObDB2cXZhTTBKYndDM1lOMlFGM1BEbTFyR21MSVRWM2JrMWxJSUVWNWtQU1ZQLXN2a25sMW54TWxXX3p1eG91Q2ZPNlpSUHlqSzhWaVhnRk9faXdKUmNCaGppSHl4dHBvRnpYRXpIQnIxcE9oZDdFTVRhdFdoOVNQeV9ZQUxNZ2k5QjR6NHc1M29hbGNCNmhBZHJEcjVINzJ4VE9j?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNU3JaOWhSd2RhT3RScnpyQWRnWGRTZ0w4UjcteEJfY0phVVQ2UWlfLVctbEtFZnptSkU2Y2RiRDJfNFYwYWtHR21CaV8xdUxWYW8xNzNmOGR5U1hzQzhhX2hWam1iUHFHSnRCb2E2RG9CUU9kZHhMZGh5cldLcllMTjFXdTVfWGdDaGJUTWYtNzNBOFVLOGZFZ2x0NA?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPU1FaN0dLTS0xR2F6NmtmajJrblZBaHV2MGFEbURkU0x5Si1Jd2RadThjZWxIYjVwM0sxcHBsWGdtN2UwWHJvbGNvTkJzUkFLNkU5SXVESGNBWHZDUlZVSFR1QlF4R21yU3JUT25MUWNBLXBkSHVsdnBoTjVaMWpZVTBmV01JclZ6RWk4WlFIbFR1QlJNV1E?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxNR1hfR2dPTlhsdURFRlJDMEtYZEVlclRRNktic2dBMkd4cU1IMzVGLW1IdEQ3OXBXTEx2SkJXVkRjZ1R6LVlCZFZkeTRoSjEyZUdRVTBTelJ6anBLZmMzYUd4d194RG8xa0hiWnQ5UjNmR1V0ZUJ5SDhWSnE4UU1SdHlMRXZpSTBuTnBYYXNRQ2NHZVJGT2dHbHpWbEdVQjN3V0t3NXFVSGYxRlloZzI5SERVbnBjMFFySk1OeDBuQQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQYmVaOGVVZFdrVGZtcWxBRlNrZHJRcEhEeVlveW9QNF9PS2hlbnhwLW9JNXV3ZXl2M3djX0ZJWnUyNUVUbDlWX1ZTZmVOM1dIUkU3WTlTeEV1MUprbjZFbG1OVkI3VFYtU1ZCemJ1azA2VFFNUXZKTHBYTzBnd21saW0wdTdXSUoyVm1pUlBFVllHbHQ5Y1FjMzdMdVE2ZDU4X0VZ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
