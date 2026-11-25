# CNQ.TO Intelligence Report

- ticker: **CNQ.TO**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/CNQ.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CNQ.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:06:54.034954+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 2, 'ai': 4, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/CNQ.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 6 named publishers; 0 exact duplicates; 9 HTTPS source links; largest publisher share 44.44%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 63.8200 |
| Return 1D (%) | 1.4143 |
| Return 1W (%) | -6.5456 |
| Return 1M (%) | -17.2459 |
| Return YTD (%) | 41.2588 |
| Return 1Y (%) | 43.1341 |
| Annualized volatility (%) | 32.1529 |
| Beta vs SPY | -0.4318 |
| Max drawdown (%) | -19.7526 |
| Sharpe (rf=0) | 1.2819 |
| Downside deviation (rf=0, %) | 22.9035 |
| Sortino (rf=0) | 1.7996 |
| Historical VaR 95% (1D, %) | 3.4582 |
| Historical ES 95% (1D, %) | 4.8736 |
| Correlation vs SPY | -0.2015 |
| Tracking error vs SPY (%) | 38.2062 |
| P/E (trailing) | 9.41 |
| P/B | 2.78 |
| EV/EBITDA | 6.49 |
| Revenue growth (%) | 34.40 |
| Forward P/E (estimate) | 10.76 |
| Gross margin (%) | 52.92 |
| Operating margin (%) | 30.67 |
| Return on equity (%) | 32.38 |
| Free cash flow yield (%) | 9.38 |
| MA50 | 70.5700 |
| Close vs MA50 (%) | -9.5650 |
| MA200 | 64.4762 |
| Close vs MA200 (%) | -1.0177 |
| RSI (14, Wilder) | 31.9827 |
| MACD (12,26) | -2.2733 |
| MACD signal (9) | -1.4232 |
| MACD histogram | -0.8502 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CNQ.TO': 288, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 63.8200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.4143 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -6.5456 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -17.2459 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 41.2588 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 43.1341 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 32.1529 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.9035 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7996 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.4582 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.8736 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.2015 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 38.2062 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.4318 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.7526 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2819 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.7594 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.9160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 30.6740 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.3850 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.3760 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.4130 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 31.9827 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.8502 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.5650 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.0177 -> Slightly below the moving-average trend level.

## TAILWINDS

### Canadian Natural Resources: Buy The Dip In This Dividend Aristocrat (NYSE:CNQ)
- Summary: Recommendation to buy CNQ as a dividend aristocrat.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNYThJNGNiN2ZmdE5xLV85NENrRUt5VTh0TUJtRmZZQ2tMLUtrTi1YUHNjUXFzRVlhRmVVYlF6aEpLQTRjVUtua0FvV3VQUzV2VWJtSUJIZW8tWURfYTVIZE43RFR3R3NYeWtTaGVid0NUWEFVNkxGdDNncE1vZ3pZVGF5czBKc2p2T3J6cXBTRjU4Nk0tTXl6Y0cxaTgtamFZeVVqM1FRNmlmdw?oc=5>

### My Top Canadian Dividend Stock to Own Going Into 2027
- Summary: Recommendation to hold CNQ for long-term dividends.
- Date: 2026-11-19 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxNQnBDNVMyaUc5a01acjBsMVRjSjRLN1JlQXNkaE55TTdhakh0LVNwVWI3Y2wxdHFpaThhcUY1MU5tNjJaTzYyRk15R2hRNmRvZGRlLVBzenlrNGM2ZmdJOFh4TnlmZzFBRTVnZDZ1YjFkRG12T0oycmVVSC1KMENPckcxblVtSk0?oc=5>

## HEADWINDS

### Canadian Natural Resources Stock: 6 Straight Red Days, Down 12%
- Summary: CNQ stock fell 12% over six days.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNckduZkQwNmtQOXlaS0Ryd1lwVVBaMm1hR1VkTWlfYlNaUjhhVUhsZEJ1U1M0bkF5Q09nT0swMXNZUk1nb1F5M3hJMUxScHdWbi1wQ0FBWDJURzJoNTBFYVZXOXNjMXVYZXA1UlhHWDRUZXNfMnlWMXU4dmpYU0t5bXNsZVF3TG9zLUJnZUwwcmh1aTVlbFhWeFQxRkk4NXVMYUF3Z1NPV1UyNkFyQm5DV3Z4REQzandFcU1tbQ?oc=5>

### Canadian Natural Resources down 4.06% on Wednesday
- Summary: CNQ shares dropped 4.06% on Wednesday.
- Date: 2026-11-18 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPeDVKOTJKbXVVaFVHVHF3MGd2em1GcmJXZDhiSS10MnhTTnh6Z013M3h3aUswbEVTX1VzNVhZaXkxZlJXTEYyeWViMk1EWkhLZktXX0p4VDUyWEVOSmRaQmUzdUJ5cmFzemlGS3V6WHlyd21VVlpHSlY3aXRIc0k2Z1Uyalp5WXZNVGp3cGVNM3lDeVkxUnc?oc=5>

## CATALYSTS

### Canadian Natural Resources Has Raised Its Dividend for 26 Straight Years: Here’s Why It Stands Out
- Summary: Canadian Natural Resources Has Raised Its Dividend for 26 Straight Years: Here’s Why It Stands Out
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQOVdQN01mT0JXNFJJVDdlYXFFMjdUemhDRmhIRG5qb2xzU2wyOU43VTRFLUhyZVBqN2NhUTdsUTl6OTU2M0dSRnZIZ1YzNXFSaTRYRkEwdnh0QllRc3RySlpyc0ZOMGprU2NFRVJPc3hhNEFFOTB5UndHR05reDNoREstS1cxNlJOYnVkZmZXenUydV9LUFE?oc=5>

### Canadian Natural Resources (TSX:CNQ) Plans To Acquire Advantage Energy
- Summary: Canadian Natural Resources (TSX:CNQ) Plans To Acquire Advantage Energy
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNTUx0b0dyamljMVYwb3VDZ2pKT2VLd0NKbi1yNFJBSnZrYXMteXFfTWN5b2d3eWFoS1VaM2RfSk1JRWxLNVhmamY0TlVFR1JmZHFWR3NZeGpSZXJjTEFRYURueEVXbDFqTGxEa2ZRNDRRQm12YlZaTWg2U18tQl91d01LVUtkcXZpWnFfd0JLVEM1SGxvWkE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CNQ.TO** | **9.41** | **2.78** | **6.49** | **34.40** | **129,881,997,312.00 CAD** | **43.13** |
| SU.TO | 9.72 | 2.12 | 4.79 | 50.40 | 104,749,883,392.00 CAD | 50.22 |
| IMO.TO | 13.21 | 3.19 | 7.75 | 34.90 | 78,113,234,944.00 CAD | 22.78 |
| CVE.TO | 8.16 | 1.97 | 4.38 | 21.10 | 69,310,808,064.00 CAD | 55.98 |

Peers fetched as_of: 2026-11-24; CNQ.TO reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-05
- Next expected earnings: 2027-03-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

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
- https://news.google.com/rss/articles/CBMihwFBVV95cUxNQnBDNVMyaUc5a01acjBsMVRjSjRLN1JlQXNkaE55TTdhakh0LVNwVWI3Y2wxdHFpaThhcUY1MU5tNjJaTzYyRk15R2hRNmRvZGRlLVBzenlrNGM2ZmdJOFh4TnlmZzFBRTVnZDZ1YjFkRG12T0oycmVVSC1KMENPckcxblVtSk0?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNckduZkQwNmtQOXlaS0Ryd1lwVVBaMm1hR1VkTWlfYlNaUjhhVUhsZEJ1U1M0bkF5Q09nT0swMXNZUk1nb1F5M3hJMUxScHdWbi1wQ0FBWDJURzJoNTBFYVZXOXNjMXVYZXA1UlhHWDRUZXNfMnlWMXU4dmpYU0t5bXNsZVF3TG9zLUJnZUwwcmh1aTVlbFhWeFQxRkk4NXVMYUF3Z1NPV1UyNkFyQm5DV3Z4REQzandFcU1tbQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPeDVKOTJKbXVVaFVHVHF3MGd2em1GcmJXZDhiSS10MnhTTnh6Z013M3h3aUswbEVTX1VzNVhZaXkxZlJXTEYyeWViMk1EWkhLZktXX0p4VDUyWEVOSmRaQmUzdUJ5cmFzemlGS3V6WHlyd21VVlpHSlY3aXRIc0k2Z1Uyalp5WXZNVGp3cGVNM3lDeVkxUnc?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQOVdQN01mT0JXNFJJVDdlYXFFMjdUemhDRmhIRG5qb2xzU2wyOU43VTRFLUhyZVBqN2NhUTdsUTl6OTU2M0dSRnZIZ1YzNXFSaTRYRkEwdnh0QllRc3RySlpyc0ZOMGprU2NFRVJPc3hhNEFFOTB5UndHR05reDNoREstS1cxNlJOYnVkZmZXenUydV9LUFE?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNTUx0b0dyamljMVYwb3VDZ2pKT2VLd0NKbi1yNFJBSnZrYXMteXFfTWN5b2d3eWFoS1VaM2RfSk1JRWxLNVhmamY0TlVFR1JmZHFWR3NZeGpSZXJjTEFRYURueEVXbDFqTGxEa2ZRNDRRQm12YlZaTWg2U18tQl91d01LVUtkcXZpWnFfd0JLVEM1SGxvWkE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
