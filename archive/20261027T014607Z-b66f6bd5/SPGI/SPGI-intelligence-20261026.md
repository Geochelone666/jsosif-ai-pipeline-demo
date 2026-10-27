# SPGI Intelligence Report

- ticker: **SPGI**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/SPGI/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SPGI/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T02:09:42.946159+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 19, 'rule': 4, 'ai': 8, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261026T005504Z-6368ad31/SPGI** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 19 unique headlines; 11 named publishers; 0 exact duplicates; 19 HTTPS source links; largest publisher share 26.32%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 450.6500 |
| Return 1D (%) | 0.0755 |
| Return 1W (%) | 5.3339 |
| Return 1M (%) | 11.7406 |
| Return YTD (%) | -8.2206 |
| Return 1Y (%) | -1.8136 |
| Annualized volatility (%) | 31.1853 |
| Beta vs SPY | 0.3194 |
| Max drawdown (%) | -28.4781 |
| Sharpe (rf=0) | 0.0512 |
| Downside deviation (rf=0, %) | 23.3916 |
| Sortino (rf=0) | 0.0682 |
| Historical VaR 95% (1D, %) | 2.9322 |
| Historical ES 95% (1D, %) | 4.7334 |
| Correlation vs SPY | 0.1302 |
| Tracking error vs SPY (%) | 32.1080 |
| P/E (trailing) | 27.43 |
| P/B | 4.22 |
| EV/EBITDA | 18.37 |
| Revenue growth (%) | 10.40 |
| Forward P/E (estimate) | 22.35 |
| Gross margin (%) | 70.90 |
| Operating margin (%) | 44.79 |
| Return on equity (%) | 14.26 |
| Free cash flow yield (%) | 4.10 |
| MA50 | 418.6290 |
| Close vs MA50 (%) | 7.6490 |
| MA200 | 416.8287 |
| Close vs MA200 (%) | 8.1140 |
| RSI (14, Wilder) | 72.0447 |
| MACD (12,26) | 10.5930 |
| MACD signal (9) | 5.0831 |
| MACD histogram | 5.5098 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SPGI': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 450.6500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.0755 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.3339 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 11.7406 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -8.2206 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -1.8136 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.1853 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.3916 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.0682 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9322 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.7334 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1302 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.1080 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3194 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.4781 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0512 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.3543 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 70.9030 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.7900 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 14.2550 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.1010 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.4285 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 72.0447 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 5.5098 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.6490 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 8.1140 -> Clearly above the moving-average trend level.

## TAILWINDS

### Stay Ahead of the Game With S&P Global (SPGI) Q3 Earnings: Wall Street's Insights on Key Metrics
- Summary: Positive Q3 earnings outlook, strong metrics expected to boost investor confidence.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOWTJ1aXdZODRkZWRhUld5TUxlb0tfdGZleXczVmhLek1tXzEyV2duYnkwdjBCSDl1Q2JmRFljTnctNjZnNDBRRVQwaG91WER6aE5JZ3ZWNm1VR1RiaHg3blpFOHV0V2NaQmJMa1hPRWdhUUVOSHJSWUFkN1UzNmlxWkwtRjdsNF9WS2g2QUpVSVBRcHM?oc=5>

### S&P makes Kalshi preferred prediction market platform for Dow Jones Indices event contracts (SPGI:NYSE)
- Summary: S&P Global partners with Kalshi to use its platform for Dow Jones event contracts.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQbFNrVU9vOEJNclpDRTZJajU1NzlwbkZEZkhUUzZrbWhCRGNoaDFFVURRaEJDc013N0R5UEl0cUJCcEhaNnlfc2hJaURpZXNCMExGeWtHYy1fTVktTXJqUzd2dWh6c0c3cWVPVzlCUHRFbmtRUWxjMlpXSjA1bkZ1dVMxNUEtdXFpSXZ2YXNTY0s0VUxrem5QUjBpNkRwTnhyaEtPeGl3MS01RG41QXhRLVRhaWpFM3V5aWc2N3FmdnVtZkNSS0Z3?oc=5>

### Official S&P index values will determine how Kalshi's coming contracts settle
- Summary: S&P index values will set settlement for Kalshi contracts.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxQdDhsdlFQbjZyWURYVFF6bzk4VmJkSDlZSko0Y1FRSkdUZmd3SF9Sbm5IU3ZsQnk1aF9yRGIyVUQtdFFBaTJEbGlHbjF3TnJSaGVOT21nLXpKdTlmNnltbUpRbGRieFlrcmVvZTk2SHMxeGFTUXhibmpJek5wc1ZHS0Z3OFpNLVVCUnJ3STN6dFFsTjRSNlB3OWtuTEtFSzFLdmJuX2pSUmNMemdYM09wNUxCQXNsdkU1SjJ2M2tQZi0?oc=5>

## HEADWINDS

### S&P Global (SPGI) Could Be 19% Overvalued Following Its Shelf Registration
- Summary: Market concerns over potential overvaluation may dampen investor enthusiasm.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxPYnRZODNnZ0F4NjA3b3RoYi1mRS1yTXdNM2VWVGFJM200QzB3bUZuRXl2V1V0TlNzb2xBUnBWUDlqX1JZQnZjUUJoTTNycnZBTFhKeG5WWTBlYlFRQ29JYkZFYjZ4blYyTUNiOFZBMjlZRThrZVlBRWJOSjlyMmgyR0UxeE0weWdRUU9lRnZSNEo?oc=5>

## CATALYSTS

### S&P Global Earnings Ahead: What Past Reactions Say About The Stock
- Summary: S&P Global Earnings Ahead: What Past Reactions Say About The Stock
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQNi1yS3VXakYtLWJLMm1FcUFYV0ZHM3NNZV9wbjJnN2xqLS1rRmhYVUtMTElicmpGSHh1cUpDN2RxRnVtdVpaTFhmdXhod0tmMUwzODFLOHlVWWxWbmtQb1duNnB1WndVbFlDaWFFSEJOTlNRUkNvSS1EQ0N0RmhzdXJuZ3FRWVpZa2p4dUt1dEV1SC0wanJPTHE1U0NXOWFyRFJDNGM2NlQ5RF9Pd25md2NKRXVXdll3VlA4Y2ZfcnJtN3M?oc=5>

### S&P Global (SPGI) to report earnings tomorrow: here is what to expect
- Summary: S&P Global (SPGI) to report earnings tomorrow: here is what to expect
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNTUl6RjVKU296MUxyQld2b0pfZW9SMHk0RGZKSnJRVGRmTVpqU1FwZEpLaGhkckhmY3FaVlhxcWpTVlVBZnhrcksxOTdZTHc5QXA5dHlib1ZLRlU4bmg4MXpYV0NGR2Q0QlNUcm9mY0FpRHVjT1l6ZVlsQUZ1WFNiMHZBc1MyWUpCNUZrMnJHTjRXNjVwY29SVTZwR0NPWWR6SkxWM0N1VnpNcTlVY2ZzMEdCMHBQWDNVU2J0WnF5S19BWi1zQmc?oc=5>

### SPGI Gears Up to Report Q3 Earnings: Here's What Investors Should Know
- Summary: SPGI Gears Up to Report Q3 Earnings: Here's What Investors Should Know
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNRmpRRkl5bmJMeEtraXItMlVLOFNlcHVHODRLRURLOE5lbUxnSk9QQUEtMW9kYXVlQmdiUjJFOU1jeTcydTdNNEhUdVMwZ2lJeElWQ2UtM3ZqMzlWUTlTWHRKSFFhVWRoM0FCYmhYNEpweGM0XzJPMVAzSU9tUGhJam1tUzRkcExqVzFVRUFiS2pVcUNUNmQ2OGl6Zkc5NE1VZGlYTjVJZVZBQXpWVGZ0TnpaQjJvdnJreGtIb3I3MXByZjA?oc=5>

### S&P Global (SPGI) Declares Quarterly Dividend of $0.45 per Share
- Summary: S&P Global (SPGI) Declares Quarterly Dividend of $0.45 per Share
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOWG5YVHUyOWR3U0lBSURTS2drNXJRb0JFd0d5ZDdUOENENWdsREV4TkFMeUVqb3RpalM2bkVwNW9aVUtucU1SazhzeDUzTFBxdW1sVkFyaldjU1gwdm5rSUtWYjBBdGtfcTVlaEZkX2d6X1Z2RjFuSVViUHVUMFdWOXAzQjJGbXd2VHNPQXlHWlNlU1JhT0gyejFiNWZwN3M?oc=5>

### Analysts Estimate S&P Global (SPGI) to Report a Decline in Earnings: What to Look Out for
- Summary: Analysts forecast a decline in SPGI earnings, signaling potential financial pressure.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNa0lRZDh0WTdtSWcxTUNlYXdKM1BZVEJBUTNJNEQxUkJUYThNTjlSeC1UR3ZXTjZ5UnI0WV9ZeUpRTnEzTWFaZVgzVDVsUWg1UERKSVFyRUNWT1BTQ2pyZ0NMV0lCU2I4UHllVEwyUHhZOVVpZG1ubENOUnE2RXI1MlFsN2VjWlFtbE9LRTRlb3VyUkFsN0hfeFhBVFU?oc=5>

### OpenZeppelin officially becomes part of S&P Global
- Summary: S&P Global acquires OpenZeppelin, enhancing security offerings.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMibkFVX3lxTFBTUzY5a25pVHJmOEo2UHpkbS1VYmg0TEZmWEI2V0JMaXdxaHdic25ZWkFMZnk4ekdtaW5KQVR5cERaeWhKRWdFM0otQ3lqSzkxRWZrREhoa29XcWZ5eHpzYzJYWURDdUZkWmV4S053?oc=5>

### Over $38 trillion in transferred value rests on OpenZeppelin's code. S&P Global has acquired the company.
- Summary: S&P Global acquisition of OpenZeppelin secures $38T transferred value.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOUk5JVmwzMllqVkdGTzhNaDdQOWs0bGFlTmFnY0xJdEVDUVA4MjdCVlRmY2tIckNPWDFyaUFid3g2Mk1zYUVFY0taNG5GYzEwNWQydnBHVHBaeGQ0TlJmUkstdWtndFgtZnozWXdKR1N5RER3ZlozczNkb0RvNk5QQVBkWTEyTEE0N19KSDdzMEQyaUowMXhwQV8tYw?oc=5>

## RISKS

### S&P Global’s AI Transition Faces Q3 Moment of Truth Oct. 27: Kensho APIs and $11T Refinancing Wall Need to Outrun Sales Bottlenecks
- Summary: Refinancing and sales bottlenecks threaten AI transition.
- Date: 2026-10-24 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQTk1NSGNnNGNKOWdpblFnTHB0SXVjeHdCS1YxS0FwRHV1ZTd6RDZlNExrc0w1em0xRmFxTnlmN0NaUjczT0p1SHozaFZxOW1NNkQwVG5YR0NGSWIxUTBEcmxRQlk0VTUxVU1TSTNzb2dkOThFUFdxZXBnbWlONFBheWZDWHdPWmhiNFVMVVpfcWIydkpvSU1r?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SPGI** | **27.43** | **4.22** | **18.37** | **10.40** | **132,851,621,888.00 USD** | **-1.81** |
| MCO | 28.96 | 25.62 | 22.15 | 0.80 | 83,530,850,304.00 USD | -0.44 |
| MSCI | 31.84 | -14.76 | 25.16 | 12.40 | 44,904,607,744.00 USD | 15.54 |
| FDS | 22.20 | 5.70 | 14.08 | 6.30 | 11,501,541,376.00 USD | 15.38 |

Peers fetched as_of: 2026-10-26; SPGI reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-28
- Next expected earnings: 2026-10-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-28
- Revenue (latest available single quarter): 1,567,000,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/64040/000006404026000045/spgi-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikwFBVV95cUxOWTJ1aXdZODRkZWRhUld5TUxlb0tfdGZleXczVmhLek1tXzEyV2duYnkwdjBCSDl1Q2JmRFljTnctNjZnNDBRRVQwaG91WER6aE5JZ3ZWNm1VR1RiaHg3blpFOHV0V2NaQmJMa1hPRWdhUUVOSHJSWUFkN1UzNmlxWkwtRjdsNF9WS2g2QUpVSVBRcHM?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQbFNrVU9vOEJNclpDRTZJajU1NzlwbkZEZkhUUzZrbWhCRGNoaDFFVURRaEJDc013N0R5UEl0cUJCcEhaNnlfc2hJaURpZXNCMExGeWtHYy1fTVktTXJqUzd2dWh6c0c3cWVPVzlCUHRFbmtRUWxjMlpXSjA1bkZ1dVMxNUEtdXFpSXZ2YXNTY0s0VUxrem5QUjBpNkRwTnhyaEtPeGl3MS01RG41QXhRLVRhaWpFM3V5aWc2N3FmdnVtZkNSS0Z3?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxQdDhsdlFQbjZyWURYVFF6bzk4VmJkSDlZSko0Y1FRSkdUZmd3SF9Sbm5IU3ZsQnk1aF9yRGIyVUQtdFFBaTJEbGlHbjF3TnJSaGVOT21nLXpKdTlmNnltbUpRbGRieFlrcmVvZTk2SHMxeGFTUXhibmpJek5wc1ZHS0Z3OFpNLVVCUnJ3STN6dFFsTjRSNlB3OWtuTEtFSzFLdmJuX2pSUmNMemdYM09wNUxCQXNsdkU1SjJ2M2tQZi0?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPYnRZODNnZ0F4NjA3b3RoYi1mRS1yTXdNM2VWVGFJM200QzB3bUZuRXl2V1V0TlNzb2xBUnBWUDlqX1JZQnZjUUJoTTNycnZBTFhKeG5WWTBlYlFRQ29JYkZFYjZ4blYyTUNiOFZBMjlZRThrZVlBRWJOSjlyMmgyR0UxeE0weWdRUU9lRnZSNEo?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQNi1yS3VXakYtLWJLMm1FcUFYV0ZHM3NNZV9wbjJnN2xqLS1rRmhYVUtMTElicmpGSHh1cUpDN2RxRnVtdVpaTFhmdXhod0tmMUwzODFLOHlVWWxWbmtQb1duNnB1WndVbFlDaWFFSEJOTlNRUkNvSS1EQ0N0RmhzdXJuZ3FRWVpZa2p4dUt1dEV1SC0wanJPTHE1U0NXOWFyRFJDNGM2NlQ5RF9Pd25md2NKRXVXdll3VlA4Y2ZfcnJtN3M?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNTUl6RjVKU296MUxyQld2b0pfZW9SMHk0RGZKSnJRVGRmTVpqU1FwZEpLaGhkckhmY3FaVlhxcWpTVlVBZnhrcksxOTdZTHc5QXA5dHlib1ZLRlU4bmg4MXpYV0NGR2Q0QlNUcm9mY0FpRHVjT1l6ZVlsQUZ1WFNiMHZBc1MyWUpCNUZrMnJHTjRXNjVwY29SVTZwR0NPWWR6SkxWM0N1VnpNcTlVY2ZzMEdCMHBQWDNVU2J0WnF5S19BWi1zQmc?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNRmpRRkl5bmJMeEtraXItMlVLOFNlcHVHODRLRURLOE5lbUxnSk9QQUEtMW9kYXVlQmdiUjJFOU1jeTcydTdNNEhUdVMwZ2lJeElWQ2UtM3ZqMzlWUTlTWHRKSFFhVWRoM0FCYmhYNEpweGM0XzJPMVAzSU9tUGhJam1tUzRkcExqVzFVRUFiS2pVcUNUNmQ2OGl6Zkc5NE1VZGlYTjVJZVZBQXpWVGZ0TnpaQjJvdnJreGtIb3I3MXByZjA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOWG5YVHUyOWR3U0lBSURTS2drNXJRb0JFd0d5ZDdUOENENWdsREV4TkFMeUVqb3RpalM2bkVwNW9aVUtucU1SazhzeDUzTFBxdW1sVkFyaldjU1gwdm5rSUtWYjBBdGtfcTVlaEZkX2d6X1Z2RjFuSVViUHVUMFdWOXAzQjJGbXd2VHNPQXlHWlNlU1JhT0gyejFiNWZwN3M?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNa0lRZDh0WTdtSWcxTUNlYXdKM1BZVEJBUTNJNEQxUkJUYThNTjlSeC1UR3ZXTjZ5UnI0WV9ZeUpRTnEzTWFaZVgzVDVsUWg1UERKSVFyRUNWT1BTQ2pyZ0NMV0lCU2I4UHllVEwyUHhZOVVpZG1ubENOUnE2RXI1MlFsN2VjWlFtbE9LRTRlb3VyUkFsN0hfeFhBVFU?oc=5
- https://news.google.com/rss/articles/CBMibkFVX3lxTFBTUzY5a25pVHJmOEo2UHpkbS1VYmg0TEZmWEI2V0JMaXdxaHdic25ZWkFMZnk4ekdtaW5KQVR5cERaeWhKRWdFM0otQ3lqSzkxRWZrREhoa29XcWZ5eHpzYzJYWURDdUZkWmV4S053?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOUk5JVmwzMllqVkdGTzhNaDdQOWs0bGFlTmFnY0xJdEVDUVA4MjdCVlRmY2tIckNPWDFyaUFid3g2Mk1zYUVFY0taNG5GYzEwNWQydnBHVHBaeGQ0TlJmUkstdWtndFgtZnozWXdKR1N5RER3ZlozczNkb0RvNk5QQVBkWTEyTEE0N19KSDdzMEQyaUowMXhwQV8tYw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQTk1NSGNnNGNKOWdpblFnTHB0SXVjeHdCS1YxS0FwRHV1ZTd6RDZlNExrc0w1em0xRmFxTnlmN0NaUjczT0p1SHozaFZxOW1NNkQwVG5YR0NGSWIxUTBEcmxRQlk0VTUxVU1TSTNzb2dkOThFUFdxZXBnbWlONFBheWZDWHdPWmhiNFVMVVpfcWIydkpvSU1r?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
