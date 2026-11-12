# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:40:21.158166+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 16, 'rule': 5, 'ai': 9, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 16 unique headlines; 8 named publishers; 0 exact duplicates; 16 HTTPS source links; largest publisher share 31.25%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 64.5400 |
| Return 1D (%) | 2.0234 |
| Return 1W (%) | -2.7866 |
| Return 1M (%) | -8.1935 |
| Return YTD (%) | -31.1647 |
| Return 1Y (%) | -43.2086 |
| Annualized volatility (%) | 36.2933 |
| Beta vs SPY | 0.2407 |
| Max drawdown (%) | -46.4449 |
| Sharpe (rf=0) | -1.3834 |
| Downside deviation (rf=0, %) | 26.6352 |
| Sortino (rf=0) | -1.8850 |
| Historical VaR 95% (1D, %) | 3.5133 |
| Historical ES 95% (1D, %) | 5.1308 |
| Correlation vs SPY | 0.0910 |
| Tracking error vs SPY (%) | 37.6160 |
| P/E (trailing) | 18.65 |
| P/B | 9.05 |
| EV/EBITDA | 17.19 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 17.11 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 31.30 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 9.61 |
| MA50 | 69.9958 |
| Close vs MA50 (%) | -7.7945 |
| MA200 | 80.7126 |
| Close vs MA200 (%) | -20.0373 |
| RSI (14, Wilder) | 44.4731 |
| MACD (12,26) | -1.7405 |
| MACD signal (9) | -2.0487 |
| MACD histogram | 0.3082 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 64.5400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.0234 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.7866 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -8.1935 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -31.1647 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -43.2086 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.2933 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.6352 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.8850 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.5133 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1308 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0910 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.6160 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2407 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -46.4449 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.3834 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.1133 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.2960 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.6127 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.6532 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 44.4731 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3082 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.7945 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -20.0373 -> Clearly below the moving-average trend level.

## TAILWINDS

### Netflix (NASDAQ:NFLX) Stock Price Up 2% - Still a Buy?
- Summary: Netflix (NASDAQ:NFLX) Stock Price Up 2% - Still a Buy?
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQbzlDR0VxOXVJdFVoencteUVUN2pRbjZjVlVXdDluRFhRSnZrWUMtOEZHR3IwZ1EtMXRvTHdzWW80MVA2Qld3YnNvQmxPTkJ6bGRNaE9GYlpkNGVGVG96SVJhV2wtNG5BRkVYcDc3cDVVcUU4SlhZWmxIZHg0XzFIQXRYQk9naHNJbzRaU0FjZnRieWxNX2FaSFJabnB2YVV0Y0JXb2Q2cWw5YmN3?oc=5>

## HEADWINDS

### NFLX Stock Slips Overnight: Co-CEO Gregory Peters Sells $1.74M Worth Of Company Shares
- Summary: NFLX Stock Slips Overnight: Co-CEO Gregory Peters Sells $1.74M Worth Of Company Shares
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOMnhNdmpIN0xleDdhQUJKekZBVWZfdWF0dzNsWXZHaEttcWZiWXQ2bml6M3VjTFVWbE9vaThlSU9nOFJzOUZtVVZ3c05WX21fb3VDWmVTSXc2UWxfRXdNV1J2NmNDWmJrNUc5N05wREMtZXY1ak8tblh3YVIyd0xfd0YtODhkelRjekdxc0dxcXNHS1JNQXU1eUlR?oc=5>

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

### Netflix (NASDAQ: NFLX) Co-CEO Offloads $1.74M In Stock Even As Company Pursues Record Buyback
- Summary: Netflix (NASDAQ: NFLX) Co-CEO Offloads $1.74M In Stock Even As Company Pursues Record Buyback
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxOeWpYbEdwMVVmNmJmd3E0ZFJvZzdoajBrZ3pXXzBXVDJaN0MwZDBDbVdfOU1MTkpOWHRpWjFrYWxIck1SazdXSHJ3Q0JQRVkxajVsNmJuV0JpdGt3WDBpRXdFeDYtaDNtNGRNbVZ5SmcyS2VLbFViTGc5b1RucE43S3pqYWlvcG5KOW1JbEZUSUc5a0xsaGNlNGhnVEUza2VuUXRoX1FfS0JzWVhqemUzZjZyUHNqa2xvQ3Q5TlZCc1AtWGg2Q0puZkdiU3VMSlBzQm9DRQ?oc=5>

### Netflix (NFLX) Stock Looks Cheap With 23% Upside To Fair Value
- Summary: Netflix (NFLX) Stock Looks Cheap With 23% Upside To Fair Value
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNU3JaOWhSd2RhT3RScnpyQWRnWGRTZ0w4UjcteEJfY0phVVQ2UWlfLVctbEtFZnptSkU2Y2RiRDJfNFYwYWtHR21CaV8xdUxWYW8xNzNmOGR5U1hzQzhhX2hWam1iUHFHSnRCb2E2RG9CUU9kZHhMZGh5cldLcllMTjFXdTVfWGdDaGJUTWYtNzNBOFVLOGZFZ2x0NA?oc=5>

### Netflix (NFLX) co-CEO Peters sells 27,312 shares and retains 119,412 directly.
- Summary: Insider sale of 27,312 shares by co-CEO Peters.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNVzV6eXh1N3VobEFTLWVJdE1vX0ZGR0Y1eEc3VDlySUZzV3hRWGhnSjl1NG0xZ2Jaakg4bm13WGtsNS1MbmJZazY4MjhGN0RkdTlCYWdkVXdOMVhfYkNpaThWVXlZTUNNVERMVk53YXh3U2pJWHZoOEp5d25CVXFMbFE3Wk1BdjNnMFFNS05kbUJqVDA2ZFpvb2RtTVg4aUROMVFpUEtLVW8?oc=5>

### Netflix, Inc. $NFLX Stock: Allspring Global Investments Holdings LLC Trims Stake
- Summary: Allspring Global Investments reduces its stake in Netflix, indicating a change in ownership structure.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxOMC1CUjhveTVLWTgyTDdwM3ExSDhsNUN2Z3QwODlEbVBfREp3aUsyVnVNckpkU2NTSDNHbmx5SHFyeEx0bFZZRFNRZDAwY25YUzY4eGlCY2ZFb01VeXVibEdiaTA2VTBqZFEtNzdvMnRZeWg0UFFVLVhQNzJKd1J6aXgyeVhLWVhvRkN6aG1fQWZ3Y3BVZFQwZU5pWU9PRWlkTlFlZGJ4ZV9aQVlNT3NqMVZXRnhGSGhORlNWZEFMVWR2MjJNdHgzMS1lMU1nWi03RUpN?oc=5>

### Netflix, Inc. $NFLX Stock Position Reduced by Boston Trust Walden Corp
- Summary: Boston Trust Walden Corp decreases its holdings in Netflix, reflecting a shift in ownership.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxObWp6WS1RSURnTG43Sy02dXI5TXpWeFpKdmdIVzFsbGItNG54M1pwUWVqZDBjSDdkV3lFZGwzSDJtUVJQcURrWlgwb2lQWDVNcTJnbEFQdjJ6ZzdMQlIxS3JjRW12bjZFQXlESU9xN1R4bGYtN1N5WlhTZ3J2eHYyQVFrbEVrWkFVcHFjc1BvTUdBc000dy12Q05DX1VSS09oSkd5QWFzNzRlZU5feU5sUzFqb3E2T09ZSWRkNVVBSVFaUnRJaHRv?oc=5>

### Netflix (NFLX) CFO sells 9,253 shares after 18,428 stock units vest.
- Summary: Netflix CFO sells shares post-vesting, altering ownership distribution.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNOHl0YUJfcS1vbWtyNTBCRUtnME5wZVRuRlcwVWpsNzc4Mkx1NU5fTEwwM0sxajdNaXBjelp4eS0zOUVXUTQ4Z01mbDNNUXJsRlRKSXpzYkxEX1hwMEQzRzhGLWFMTjJEd0dRUElXbkdYcUEwUTlQN2tRVzcyLVBZY1g5QVVXWVh5cmpHNml0TjVtSFZIUERTQmdUbzYwU1NUNnFQNldyalU?oc=5>

### Netflix, Inc. $NFLX Stock: CenterBook Partners LP Decreases Holdings
- Summary: CenterBook Partners LP reduces its Netflix holdings, impacting ownership structure.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxOWFVMQVpvNnNRVVNUTzRfZmY5YkFhX05hWnFsQ3EwTHRWRlRpWUcwSGx4eWVoMkFwWXhnbHAzWURtS0xPb2dHZThNZm5WNTVNb3BOUDYtWkNFM2JDd2FiWU83eU9Vak9FanlFUk5QS1I2YWRVOFNWRHYyOE9SRnVUQjJ6NXFiUHY3cUk2WGhiSlV5a2dLR1JDY3Q4c2ZsMVNIX2ktZW9KR0tjTzlEbXROUW9TZXlFOTNXdTNmQnpiZVVySlE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **18.65** | **9.05** | **17.19** | **11.80** | **265,022,291,968.00 USD** | **-43.21** |
| DIS | 24.57 | 1.88 | 12.13 | 6.80 | 206,598,078,464.00 USD | 5.69 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 7.92 | 0.96 | 5.03 | -6.10 | 88,846,180,352.00 USD | 2.46 |

Peers fetched as_of: 2026-11-11; NFLX reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

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
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOMnhNdmpIN0xleDdhQUJKekZBVWZfdWF0dzNsWXZHaEttcWZiWXQ2bml6M3VjTFVWbE9vaThlSU9nOFJzOUZtVVZ3c05WX21fb3VDWmVTSXc2UWxfRXdNV1J2NmNDWmJrNUc5N05wREMtZXY1ak8tblh3YVIyd0xfd0YtODhkelRjekdxc0dxcXNHS1JNQXU1eUlR?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPd1NLeHE4Skdqd3NHRk8wSEtWSlpVazJfcEZVV0FjT0gzdElUQjEwWUs0LXdqeE9PZTAzcGNiZTJLMHNNS0h6TGVSOExwb3puOU9ybUliWHNsb2pYbnhVWjNQSXo4bjYtWFlWWHRLdWRjbFZ1ekc5c1lWWE95YXB2d1NrMXVjdDliUFJGVktOQUlBM1NBZTRlREhR?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQaF9lS2lHZnpDYmpGM3FsQXdWZmJGV29qb05VNGJXQkR0SVhQV2JaLUNFWjFpb3VjTDFHeXFJUHhNZkd3b0U4Rk5TcXBZOWZVRF9GZFFTd3dwSEJhMmdjbzV6MFg3dEtwQWtTS1ZXLXU3UmQ4YXB2aFAzUFBiTHdfd1VhZ1Q2ZGlyeVpjQUlPbXJkVEtkUm5uMTlacklKaWlENDdGWXJyXzdYbTJ5c0NvamlGS01SdzQzNkR0SmIycmlaUzJHN2c?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPVEFpUE1pTmNGWWlJcl8zOTdBeXJKeEpiejc2cUtJLXJfYnlsanktbGxyMjBMM1c4Y0I1NDVkcEdNenRxV0VZTzJjc3Jia1dHMERFUEpVQmNvMnNTbTEtMkJCZF9iV09vbk9TNzNOOEN6UVBacUU2S0pERzk5Y01TWnBJS2N3U09LdjFHTl9Gb0g5QVNGb0ZqNQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOR3V0UlpQTXZmZWVHUFVqdlk1NFAtUnlnc0xEREt4OE5oVkZQQ3VpbHhLZ0V6OEl5OTJBUzlrS2NURVcyVzdBeE5MYk5LMGVPZUQxOE1RMzE0VUdSZDVTeEREX2dBNGdPNFVXNnVSb3FQR0JTVE9VaU9XOWgwdV9qNVotaW1rU2JpNUw3b09kZlVtbDJIN2NkUFpRQnp4OTJCNlE?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxObDB2cXZhTTBKYndDM1lOMlFGM1BEbTFyR21MSVRWM2JrMWxJSUVWNWtQU1ZQLXN2a25sMW54TWxXX3p1eG91Q2ZPNlpSUHlqSzhWaVhnRk9faXdKUmNCaGppSHl4dHBvRnpYRXpIQnIxcE9oZDdFTVRhdFdoOVNQeV9ZQUxNZ2k5QjR6NHc1M29hbGNCNmhBZHJEcjVINzJ4VE9j?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxOeWpYbEdwMVVmNmJmd3E0ZFJvZzdoajBrZ3pXXzBXVDJaN0MwZDBDbVdfOU1MTkpOWHRpWjFrYWxIck1SazdXSHJ3Q0JQRVkxajVsNmJuV0JpdGt3WDBpRXdFeDYtaDNtNGRNbVZ5SmcyS2VLbFViTGc5b1RucE43S3pqYWlvcG5KOW1JbEZUSUc5a0xsaGNlNGhnVEUza2VuUXRoX1FfS0JzWVhqemUzZjZyUHNqa2xvQ3Q5TlZCc1AtWGg2Q0puZkdiU3VMSlBzQm9DRQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNU3JaOWhSd2RhT3RScnpyQWRnWGRTZ0w4UjcteEJfY0phVVQ2UWlfLVctbEtFZnptSkU2Y2RiRDJfNFYwYWtHR21CaV8xdUxWYW8xNzNmOGR5U1hzQzhhX2hWam1iUHFHSnRCb2E2RG9CUU9kZHhMZGh5cldLcllMTjFXdTVfWGdDaGJUTWYtNzNBOFVLOGZFZ2x0NA?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNVzV6eXh1N3VobEFTLWVJdE1vX0ZGR0Y1eEc3VDlySUZzV3hRWGhnSjl1NG0xZ2Jaakg4bm13WGtsNS1MbmJZazY4MjhGN0RkdTlCYWdkVXdOMVhfYkNpaThWVXlZTUNNVERMVk53YXh3U2pJWHZoOEp5d25CVXFMbFE3Wk1BdjNnMFFNS05kbUJqVDA2ZFpvb2RtTVg4aUROMVFpUEtLVW8?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOMC1CUjhveTVLWTgyTDdwM3ExSDhsNUN2Z3QwODlEbVBfREp3aUsyVnVNckpkU2NTSDNHbmx5SHFyeEx0bFZZRFNRZDAwY25YUzY4eGlCY2ZFb01VeXVibEdiaTA2VTBqZFEtNzdvMnRZeWg0UFFVLVhQNzJKd1J6aXgyeVhLWVhvRkN6aG1fQWZ3Y3BVZFQwZU5pWU9PRWlkTlFlZGJ4ZV9aQVlNT3NqMVZXRnhGSGhORlNWZEFMVWR2MjJNdHgzMS1lMU1nWi03RUpN?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxObWp6WS1RSURnTG43Sy02dXI5TXpWeFpKdmdIVzFsbGItNG54M1pwUWVqZDBjSDdkV3lFZGwzSDJtUVJQcURrWlgwb2lQWDVNcTJnbEFQdjJ6ZzdMQlIxS3JjRW12bjZFQXlESU9xN1R4bGYtN1N5WlhTZ3J2eHYyQVFrbEVrWkFVcHFjc1BvTUdBc000dy12Q05DX1VSS09oSkd5QWFzNzRlZU5feU5sUzFqb3E2T09ZSWRkNVVBSVFaUnRJaHRv?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNOHl0YUJfcS1vbWtyNTBCRUtnME5wZVRuRlcwVWpsNzc4Mkx1NU5fTEwwM0sxajdNaXBjelp4eS0zOUVXUTQ4Z01mbDNNUXJsRlRKSXpzYkxEX1hwMEQzRzhGLWFMTjJEd0dRUElXbkdYcUEwUTlQN2tRVzcyLVBZY1g5QVVXWVh5cmpHNml0TjVtSFZIUERTQmdUbzYwU1NUNnFQNldyalU?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxOWFVMQVpvNnNRVVNUTzRfZmY5YkFhX05hWnFsQ3EwTHRWRlRpWUcwSGx4eWVoMkFwWXhnbHAzWURtS0xPb2dHZThNZm5WNTVNb3BOUDYtWkNFM2JDd2FiWU83eU9Vak9FanlFUk5QS1I2YWRVOFNWRHYyOE9SRnVUQjJ6NXFiUHY3cUk2WGhiSlV5a2dLR1JDY3Q4c2ZsMVNIX2ktZW9KR0tjTzlEbXROUW9TZXlFOTNXdTNmQnpiZVVySlE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
