# CNQ.TO Intelligence Report

- ticker: **CNQ.TO**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-26**
- Quant sources: https://finance.yahoo.com/quote/CNQ.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CNQ.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:47:11.834969+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 2, 'ai': 5, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/CNQ.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 7 named publishers; 0 exact duplicates; 15 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 66.0800 |
| Return 1D (%) | 2.0698 |
| Return 1W (%) | 3.0889 |
| Return 1M (%) | -14.4152 |
| Return YTD (%) | 46.2611 |
| Return 1Y (%) | 47.1894 |
| Annualized volatility (%) | 32.2280 |
| Beta vs SPY | -0.4377 |
| Max drawdown (%) | -19.7526 |
| Sharpe (rf=0) | 1.3668 |
| Downside deviation (rf=0, %) | 22.9034 |
| Sortino (rf=0) | 1.9233 |
| Historical VaR 95% (1D, %) | 3.4582 |
| Historical ES 95% (1D, %) | 4.8736 |
| Correlation vs SPY | -0.2036 |
| Tracking error vs SPY (%) | 38.3057 |
| P/E (trailing) | 9.75 |
| P/B | 2.88 |
| EV/EBITDA | 6.70 |
| Revenue growth (%) | 34.40 |
| Forward P/E (estimate) | 11.14 |
| Gross margin (%) | 52.92 |
| Operating margin (%) | 30.67 |
| Return on equity (%) | 32.38 |
| Free cash flow yield (%) | 9.06 |
| MA50 | 70.3508 |
| Close vs MA50 (%) | -6.0707 |
| MA200 | 64.6145 |
| Close vs MA200 (%) | 2.2681 |
| RSI (14, Wilder) | 41.5458 |
| MACD (12,26) | -2.1154 |
| MACD signal (9) | -1.6954 |
| MACD histogram | -0.4200 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CNQ.TO': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 66.0800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.0698 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.0889 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -14.4152 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 46.2611 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 47.1894 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 32.2280 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.9034 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.9233 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.4582 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.8736 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.2036 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 38.3057 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.4377 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.7526 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.3668 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.1404 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.9160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 30.6740 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.3850 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.0553 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.7463 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.5458 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.4200 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -6.0707 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 2.2681 -> Slightly above the moving-average trend level.

## TAILWINDS

### Canadian Natural Resources: Buy The Dip In This Dividend Aristocrat (NYSE:CNQ)
- Summary: Recommendation to buy CNQ as a dividend aristocrat.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNYThJNGNiN2ZmdE5xLV85NENrRUt5VTh0TUJtRmZZQ2tMLUtrTi1YUHNjUXFzRVlhRmVVYlF6aEpLQTRjVUtua0FvV3VQUzV2VWJtSUJIZW8tWURfYTVIZE43RFR3R3NYeWtTaGVid0NUWEFVNkxGdDNncE1vZ3pZVGF5czBKc2p2T3J6cXBTRjU4Nk0tTXl6Y0cxaTgtamFZeVVqM1FRNmlmdw?oc=5>

## HEADWINDS

### Canadian Natural Resources (NYSE:CNQ) Downgraded by Wall Street Zen to "Hold"
- Summary: Canadian Natural Resources (NYSE:CNQ) Downgraded by Wall Street Zen to "Hold"
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxQblUxYWtxYjJrMUZjeUFlTUNBamprbVJXanh6VUlVVWtZaU41c25mc1VqandoM0xRcXBBbV92NmhEQXVjem8zbXVhMGZCOUpwUnhvWHNETWk1SEhFdjl1S3B3NzE3ZTZoZjR4YVpXY05Pa3FQME5wZFQ1UDZmY3lTaWZsODBPTkZlS2NRRXZhd1gzdVVfUDV4emtpUl8wWlVsZFY4VDJKelEtNzV0VWRwR1FWS1RBWnpabmtIVFViMGgzdlVnWVBQY3F4RWVUaHZH?oc=5>

### Canadian Natural Resources Stock: 6 Straight Red Days, Down 12%
- Summary: CNQ stock fell 12% over six days.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNckduZkQwNmtQOXlaS0Ryd1lwVVBaMm1hR1VkTWlfYlNaUjhhVUhsZEJ1U1M0bkF5Q09nT0swMXNZUk1nb1F5M3hJMUxScHdWbi1wQ0FBWDJURzJoNTBFYVZXOXNjMXVYZXA1UlhHWDRUZXNfMnlWMXU4dmpYU0t5bXNsZVF3TG9zLUJnZUwwcmh1aTVlbFhWeFQxRkk4NXVMYUF3Z1NPV1UyNkFyQm5DV3Z4REQzandFcU1tbQ?oc=5>

## CATALYSTS

### Canadian Natural Resources Limited (NYSE:CNQ) Stock Now Rated "Moderate Buy" by Wall Street Analysts
- Summary: Canadian Natural Resources Limited (NYSE:CNQ) Stock Now Rated "Moderate Buy" by Wall Street Analysts
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8gFBVV95cUxQWGlIaWhjRFJXNjZiaEFLTnpQek1BQzBMS2hoaVZQWTc5eWJOek16a1lCZEFEdkpjNDhJQUZnVVliejZTNTMzSGV6em82VnMwRzZuM0ZxdjRmeGZsWi00N0hzVDNTSnU4cU9kVzBUREdKdV9Zc3Zrd3ZvSV9RdWlPb0ktcHdiUzJScjdOVTZTajlkS2llMjlzVlVnMnVXZXN0NWRrRFBLeTJPME80Umd5M0ZnVXRFcHZQRlc3SjM3TC0zZUt1NHM5ajBta2hIMUdJRHhtNEc2VUl4STBOUVFheWtGRmxfUF8wOW9PR1RJLUZ3UQ?oc=5>

### Energy Focus: Canadian Natural Resources Ltd. (TSX:CNQ) — S&P/TSX Composite Large Cap Value Stock in Focus After Fresh Corporate News
- Summary: CNQ highlighted for strong corporate updates, boosting investor interest.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxPSVpkeGJvcEVEcmFZOUNCQWlpSnNuWTVpdU5mR2NhZmZ2am1kVVB4T1hWWHpjUk1qdkZyVVBubnBZY0RxZ2tfTVdPa0tlaDVQSVdITVBvOUVOQmxvYUVQd2h4U21ieGd1NnMyU19JWEQzdFppb2xxZThBcW1oZVJRVmU0eFozUzZNRVRmSHB2OHBXdzdsSVR6N3E3dlFlYnNBWVlVMU50Z3NYVVFYa1d6TEczTkFYMUZBU0k0TGRSRVVlcTZ0dDVlTkxFQkI0RFhDOERJeDlsMVlyakxyanE5dGNaOTZubGNkeXdz?oc=5>

### Why Canadian Natural Resources Limited Is Drawing Fresh Attention Today as Investors Track strong production and accelerating shareholder returns (TSX:CNQ)
- Summary: CNQ gains attention due to robust production and rising shareholder returns.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikAJBVV95cUxQRm1aWnRyczhJZHlnbEVneFVoZTJtczhuNkVHYlQybXFoOHBxSjh3ZkRtRkluOVE3N3FGcm5fQnlSWS1jYXQtU2JhWGZpRTFWb201bjg5ZnZiR2d5ajZ1WUVOTHlCS09sWW5tckZuWEdNTzE1NVdGcXJVdy10cWhpdTM5N1pBVi1IVUJQNHJybm1GbUd4cVJzUzd4ZnhfNzRnM25RSDRvNVBBNWJWLUlVVDROQXJCa0kyNG9uMjA0d1E4UmJhVkJiTkFUZnU2NlA4d1ZuVnEybVBySmdFdUtBLUVhalhtcmlxSmdnUUNmV2duRklmWjJ0SDloLXQ2WkQ3UkhuV0dYcnBldmZCcVdYcw?oc=5>

### Canadian Natural Resources stock: Zacks sees rebound case after sell-off
- Summary: Zacks predicts a rebound for CNQ following recent sell-off.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxObXVfVEMxYmVaMVFRWURLT2cwNFI0cmp5MHJ1SlI0OHpwVGpGc0dHREhpczk0NmVJOWdYZ3NuWFU0clRTcGE4aUlWOTl3eWJWd3lkc0dqY0swTlYxcTFhM05wSGZ2eWd5c0paS1UtaGkzOGRNdTFjSzQ1UmkxSEZzSFhjWC1JdW1QV0p1REQ0U2pzd3JOZUpiQmkzRnJJaS1QbkN4WlNkb2xFbzFKUlBNdWlwNjAtTEZzOThONVVHblRxZmJqNmJkN3ZtZUxqNlk?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CNQ.TO** | **9.75** | **2.88** | **6.70** | **34.40** | **134,481,395,712.00 CAD** | **47.19** |
| SU.TO | 10.19 | 2.19 | 4.92 | 50.40 | 107,892,736,000.00 CAD | 54.80 |
| IMO.TO | 13.72 | 3.27 | 7.92 | 34.90 | 79,911,600,128.00 CAD | 24.69 |
| CVE.TO | 8.32 | 2.00 | 4.44 | 21.10 | 70,485,565,440.00 CAD | 62.04 |

Peers fetched as_of: 2026-11-26; CNQ.TO reuses existing data (market data as_of: 2026-11-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-05
- Next expected earnings: 2027-03-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNYThJNGNiN2ZmdE5xLV85NENrRUt5VTh0TUJtRmZZQ2tMLUtrTi1YUHNjUXFzRVlhRmVVYlF6aEpLQTRjVUtua0FvV3VQUzV2VWJtSUJIZW8tWURfYTVIZE43RFR3R3NYeWtTaGVid0NUWEFVNkxGdDNncE1vZ3pZVGF5czBKc2p2T3J6cXBTRjU4Nk0tTXl6Y0cxaTgtamFZeVVqM1FRNmlmdw?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxQblUxYWtxYjJrMUZjeUFlTUNBamprbVJXanh6VUlVVWtZaU41c25mc1VqandoM0xRcXBBbV92NmhEQXVjem8zbXVhMGZCOUpwUnhvWHNETWk1SEhFdjl1S3B3NzE3ZTZoZjR4YVpXY05Pa3FQME5wZFQ1UDZmY3lTaWZsODBPTkZlS2NRRXZhd1gzdVVfUDV4emtpUl8wWlVsZFY4VDJKelEtNzV0VWRwR1FWS1RBWnpabmtIVFViMGgzdlVnWVBQY3F4RWVUaHZH?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNckduZkQwNmtQOXlaS0Ryd1lwVVBaMm1hR1VkTWlfYlNaUjhhVUhsZEJ1U1M0bkF5Q09nT0swMXNZUk1nb1F5M3hJMUxScHdWbi1wQ0FBWDJURzJoNTBFYVZXOXNjMXVYZXA1UlhHWDRUZXNfMnlWMXU4dmpYU0t5bXNsZVF3TG9zLUJnZUwwcmh1aTVlbFhWeFQxRkk4NXVMYUF3Z1NPV1UyNkFyQm5DV3Z4REQzandFcU1tbQ?oc=5
- https://news.google.com/rss/articles/CBMi8gFBVV95cUxQWGlIaWhjRFJXNjZiaEFLTnpQek1BQzBMS2hoaVZQWTc5eWJOek16a1lCZEFEdkpjNDhJQUZnVVliejZTNTMzSGV6em82VnMwRzZuM0ZxdjRmeGZsWi00N0hzVDNTSnU4cU9kVzBUREdKdV9Zc3Zrd3ZvSV9RdWlPb0ktcHdiUzJScjdOVTZTajlkS2llMjlzVlVnMnVXZXN0NWRrRFBLeTJPME80Umd5M0ZnVXRFcHZQRlc3SjM3TC0zZUt1NHM5ajBta2hIMUdJRHhtNEc2VUl4STBOUVFheWtGRmxfUF8wOW9PR1RJLUZ3UQ?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxPSVpkeGJvcEVEcmFZOUNCQWlpSnNuWTVpdU5mR2NhZmZ2am1kVVB4T1hWWHpjUk1qdkZyVVBubnBZY0RxZ2tfTVdPa0tlaDVQSVdITVBvOUVOQmxvYUVQd2h4U21ieGd1NnMyU19JWEQzdFppb2xxZThBcW1oZVJRVmU0eFozUzZNRVRmSHB2OHBXdzdsSVR6N3E3dlFlYnNBWVlVMU50Z3NYVVFYa1d6TEczTkFYMUZBU0k0TGRSRVVlcTZ0dDVlTkxFQkI0RFhDOERJeDlsMVlyakxyanE5dGNaOTZubGNkeXdz?oc=5
- https://news.google.com/rss/articles/CBMikAJBVV95cUxQRm1aWnRyczhJZHlnbEVneFVoZTJtczhuNkVHYlQybXFoOHBxSjh3ZkRtRkluOVE3N3FGcm5fQnlSWS1jYXQtU2JhWGZpRTFWb201bjg5ZnZiR2d5ajZ1WUVOTHlCS09sWW5tckZuWEdNTzE1NVdGcXJVdy10cWhpdTM5N1pBVi1IVUJQNHJybm1GbUd4cVJzUzd4ZnhfNzRnM25RSDRvNVBBNWJWLUlVVDROQXJCa0kyNG9uMjA0d1E4UmJhVkJiTkFUZnU2NlA4d1ZuVnEybVBySmdFdUtBLUVhalhtcmlxSmdnUUNmV2duRklmWjJ0SDloLXQ2WkQ3UkhuV0dYcnBldmZCcVdYcw?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxObXVfVEMxYmVaMVFRWURLT2cwNFI0cmp5MHJ1SlI0OHpwVGpGc0dHREhpczk0NmVJOWdYZ3NuWFU0clRTcGE4aUlWOTl3eWJWd3lkc0dqY0swTlYxcTFhM05wSGZ2eWd5c0paS1UtaGkzOGRNdTFjSzQ1UmkxSEZzSFhjWC1JdW1QV0p1REQ0U2pzd3JOZUpiQmkzRnJJaS1QbkN4WlNkb2xFbzFKUlBNdWlwNjAtTEZzOThONVVHblRxZmJqNmJkN3ZtZUxqNlk?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
