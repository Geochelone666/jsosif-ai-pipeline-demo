# CP.TO Intelligence Report

- ticker: **CP.TO**
- Report as_of: **2026-11-20**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/CP.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CP.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-20**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-21T05:47:48.722080+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 2, 'ai': 7, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261120T053808Z-e360129e/CP.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 6 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 41.67%; oldest publication 2026-11-15

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 128.7700 |
| Return 1D (%) | -1.7848 |
| Return 1W (%) | -4.0319 |
| Return 1M (%) | 4.9299 |
| Return YTD (%) | 28.2536 |
| Return 1Y (%) | 33.7430 |
| Annualized volatility (%) | 22.1181 |
| Beta vs SPY | 0.3657 |
| Max drawdown (%) | -11.9692 |
| Sharpe (rf=0) | 1.4305 |
| Downside deviation (rf=0, %) | 14.5271 |
| Sortino (rf=0) | 2.1781 |
| Historical VaR 95% (1D, %) | 1.8632 |
| Historical ES 95% (1D, %) | 2.9374 |
| Correlation vs SPY | 0.2357 |
| Tracking error vs SPY (%) | 23.5080 |
| P/E (trailing) | 29.20 |
| P/B | 2.45 |
| EV/EBITDA | 16.39 |
| Revenue growth (%) | 15.20 |
| Forward P/E (estimate) | 21.81 |
| Gross margin (%) | 52.76 |
| Operating margin (%) | 39.78 |
| Return on equity (%) | 8.27 |
| Free cash flow yield (%) | 2.45 |
| MA50 | 125.7840 |
| Close vs MA50 (%) | 2.3739 |
| MA200 | 121.3364 |
| Close vs MA200 (%) | 6.1264 |
| RSI (14, Wilder) | 48.0290 |
| MACD (12,26) | 1.9555 |
| MACD signal (9) | 2.2923 |
| MACD histogram | -0.3368 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CP.TO': 286, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 128.7700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.7848 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.0319 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.9299 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 28.2536 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 33.7430 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.1181 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.5271 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.1781 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8632 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9374 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2357 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.5080 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3657 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.9692 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4305 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.8072 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.7640 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 39.7760 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.2680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.4467 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 29.1995 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.0290 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.3368 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.3739 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.1264 -> Clearly above the moving-average trend level.

## TAILWINDS

### Is CPKC (TSX:CP) Positioned For Stronger Growth Across Markets?
- Summary: Question about CP's growth potential across markets.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQWkZ3Q3EzWi0yaWhoZlZlZjF5eDFnQUZUNmZfUW9QYjk4ek9RbENOZVlCQzc0ZFZKQTNtMUhydTV0TFJjWng4RktDVGdZN0Q5VnRGUlNBb1FZaFRRM184UWdQTWNkeDBpTlhTMHJDX0lqd1ZkQjlOcDBkOGJrY3JsWlZEc0RSaXRCRjQ2TTJKSkdBY0RYdEZuWW5YY2NZbUdkSHJrNDRKemQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Canadian Pacific Kansas City stock: rivals defend full merger review
- Summary: Canadian Pacific Kansas City stock: rivals defend full merger review
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPRkJzNlFsR25LUWw0YkphaGZvMk9fNG4wT21tRHp0MEY5VUFJMGZ4cEtNOFRQelpvaFc1NE9XSUh3Ui1sSmVpSllyNHZucm0xbmdULVo3R1h3d3N2WTlzY0ZIakcxTU1rMGhTTnJZT21NcGxqVGZlbDk5ZFlUU2pRREItcm0tbTZJS1B0Mmx1MUx1RnhkSlktaTVlbkdXZHpNYmwyYlp1d2xkTWJJd1Q1bFdPRGphczlYMUJiX2dVWFBhSXM3OVBWYkFn?oc=5>

### Canadian Pacific Kansas City stock: rivals oppose merger review request
- Summary: Canadian Pacific Kansas City stock: rivals oppose merger review request
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxOWjhZTGluRW1XWFhMOXJqaDlSb3BjZlZSWm44ZVpETmpvd1haYTFCUHNFbFE0dGZ6dHVtUnZKU1ZIVWRqWVd5RmRfeW9WbnR4UDItMUVDUWw5d1dCYzA0RkRNcXg1V3ZzTEg3RWZlZ3p2cmdBTXBhelg2MGlkRTQyYmhWZ2hRcnhaVlpIRThCWUhvdFFiemlyTEJUc21QbGlJX2lXRFB4Y1pBZnVJZWZoUUJQUGdjMVlpaGN3ZVZ6S3ViaGJiaUxOenc5bDdNdw?oc=5>

### Canadian Pacific Kansas City (TSX:CP) Rallies On Cross Border Network Story, Is It Still Undervalued?
- Summary: Shares rally on cross-border network news, questioning undervaluation.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxONDhjWUpnQ0kzUDM0MEpqZHBhS2QtbzhKcy0wZ2pPTmZkZExjVXdtR0ptU0VEaXg5QVh2dGFwOE40UEwzeWkwSUE2MjFxenlzU1c1Q1N0OG1nanA4RkFhOU5DY0R5X3hoeUZ5aDJjbk8zSXl0a1N2cVZiM3ZPZHltdEJ6OTM0eWRSbW5NSEZLZXBzdGR2TFF2NHNnMjhZUQ?oc=5>

### Canadian Pacific Kansas City stock: executives signal stronger growth path
- Summary: Executives indicate a stronger growth trajectory for CP.TO, suggesting improved future performance.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQLXI3ZDFZeUhxSjlxVlQwQnRkbFJ5My10MjFubW0tblh2LW5mWGhxeDJ3a0RqYnc2Y0ZobG1sMjZGTndFZjVxZWVHWHpEdXppTzNJWjdSWEs4Y2IyZTZRNFF0QmFYVkd1ZEs0UGlyWDJLVlRLMjBHTGpVdXc5VldXdnppX0JuS242bXR6VWEzSllYSkt0WV9VdUJ5ZjdSblZFNGVieE84U3QycHRxLUpXQWM5UU9uQXk4NFN1UmYyMXRZSHJ1VmF5RWkwUHJSa3hsakE?oc=5>

### Canadian Pacific Kansas City stock: executives set for Nov. 17 event
- Summary: CP executives will hold a scheduled event on Nov. 17, potentially discussing company strategy and outlook.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxQMW80REYyUDN1VnJZMXF0bkY0SG1oaXVFRzVUZUFLSkhIM1lmUG5MZ09US1BJWFBWdXZSVkNMS0VEbkc2YkEwR2t2MkJYTUpWX3BSNF94TzhTcndLUnR0eTU3MXpKbDY2M0R2aVAtSDBsdDN0UERzYmQySFNkZ1IxYU5hc2M0VktOZXlTX1hjNDJ3YTFXWlBsWHdNR011SDR1Z1B0anVmSGVvOU15a2QzWGs5S2hBQUhka3NkSHBlSnNTV1AybGRfbQ?oc=5>

### CPKC at 26th Annual Scotiabank Transportation & Industrials Conference: growth outlook By Investing.com
- Summary: CPKC presented growth outlook at the annual Scotiabank conference, outlining future revenue and operational targets.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxPSm1ZUUJWRXFGX2JISW5WVmlLT0w5NnJlZVMtQ011THEtclVzRVoycnFsOVJjaGE5Zi1oTUpsc2xXYWRCV3d0QTBCWXkyVzZZT1ZCbDV3NGhWREZNazkwNmNETDU1REltcTNIa3dlUGs5VDhsV0h0LVFMMGhKNWZ2TlcyTFpDYjFQdEFPVW9SeUplWURYWWJNT09DRzVralF4WDktMzJKdHNLTkNWSmUzTHQ1OTlKQ3BTa3lTTTU1TFBIaE5CVXhXbjVQTG9NSkpsS2dXTmhQREtPZEdDaWc?oc=5>

### CPKC's President and CEO Keith Creel to address the 2026 UBS Global Industrials and Transportation Conference
- Summary: CEO Keith Creel will speak at the UBS conference, discussing company strategy and market positioning.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNZWdjRm1Qakg2VzlXMnZJR3p1VHQzVE1nLUxJcTJvQW9fUHZjWURPSnhPSGU3eVphcU1rRllwc01lcWpnelZYV0VsZVBsYjQ3U1RhSi1IZHM2bVROV3JybXF6c0dlUUFKSGRuZGdad1FYQ3Uzb1RKbjdMaW9VbTdhVEZUZlRPNzVHZnRMSW5QcDdQaXluYktxRm9qM08?oc=5>

## RISKS

### Does CPKC (TSX:CP) Have The Order Quality To Weather Volatility?
- Summary: Questioning order quality raises uncertainty about resilience.
- Date: 2026-11-18 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPSjJJOEJ2LTRLWnJjRmJ4a1dzOVFqRFRmbk5mdnFUQlFzTUVSNFk4cnhvdktQN21EeXptYlM0eWhuWlpiSmZDc3FfQ041azlrc202MDd5NERkNHd6aWtVZGltOHJFaXN0dzhXREx5NnhqN0prRk9iWndsSDlQSVkyODA3VWxfcjFmRzlxWk5qWG1DMnR6R0Myd3FtOEV0cnpHVHlHS0ZONTRnZw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CP.TO** | **29.20** | **2.45** | **16.39** | **15.20** | **111,972,573,184.00 CAD** | **33.74** |
| CNR.TO | 22.03 | 4.80 | 13.66 | 14.60 | 105,175,384,064.00 CAD | 38.29 |
| UNP | 22.67 | 7.75 | 14.96 | 15.30 | 170,722,213,888.00 USD | 32.61 |
| NSC | 26.07 | 4.18 | 14.75 | 13.60 | 69,858,041,856.00 USD | 12.87 |

Peers fetched as_of: 2026-11-20; CP.TO reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-20

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-29
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/16875/000001687526000033/cp-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQWkZ3Q3EzWi0yaWhoZlZlZjF5eDFnQUZUNmZfUW9QYjk4ek9RbENOZVlCQzc0ZFZKQTNtMUhydTV0TFJjWng4RktDVGdZN0Q5VnRGUlNBb1FZaFRRM184UWdQTWNkeDBpTlhTMHJDX0lqd1ZkQjlOcDBkOGJrY3JsWlZEc0RSaXRCRjQ2TTJKSkdBY0RYdEZuWW5YY2NZbUdkSHJrNDRKemQ?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPRkJzNlFsR25LUWw0YkphaGZvMk9fNG4wT21tRHp0MEY5VUFJMGZ4cEtNOFRQelpvaFc1NE9XSUh3Ui1sSmVpSllyNHZucm0xbmdULVo3R1h3d3N2WTlzY0ZIakcxTU1rMGhTTnJZT21NcGxqVGZlbDk5ZFlUU2pRREItcm0tbTZJS1B0Mmx1MUx1RnhkSlktaTVlbkdXZHpNYmwyYlp1d2xkTWJJd1Q1bFdPRGphczlYMUJiX2dVWFBhSXM3OVBWYkFn?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxOWjhZTGluRW1XWFhMOXJqaDlSb3BjZlZSWm44ZVpETmpvd1haYTFCUHNFbFE0dGZ6dHVtUnZKU1ZIVWRqWVd5RmRfeW9WbnR4UDItMUVDUWw5d1dCYzA0RkRNcXg1V3ZzTEg3RWZlZ3p2cmdBTXBhelg2MGlkRTQyYmhWZ2hRcnhaVlpIRThCWUhvdFFiemlyTEJUc21QbGlJX2lXRFB4Y1pBZnVJZWZoUUJQUGdjMVlpaGN3ZVZ6S3ViaGJiaUxOenc5bDdNdw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxONDhjWUpnQ0kzUDM0MEpqZHBhS2QtbzhKcy0wZ2pPTmZkZExjVXdtR0ptU0VEaXg5QVh2dGFwOE40UEwzeWkwSUE2MjFxenlzU1c1Q1N0OG1nanA4RkFhOU5DY0R5X3hoeUZ5aDJjbk8zSXl0a1N2cVZiM3ZPZHltdEJ6OTM0eWRSbW5NSEZLZXBzdGR2TFF2NHNnMjhZUQ?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQLXI3ZDFZeUhxSjlxVlQwQnRkbFJ5My10MjFubW0tblh2LW5mWGhxeDJ3a0RqYnc2Y0ZobG1sMjZGTndFZjVxZWVHWHpEdXppTzNJWjdSWEs4Y2IyZTZRNFF0QmFYVkd1ZEs0UGlyWDJLVlRLMjBHTGpVdXc5VldXdnppX0JuS242bXR6VWEzSllYSkt0WV9VdUJ5ZjdSblZFNGVieE84U3QycHRxLUpXQWM5UU9uQXk4NFN1UmYyMXRZSHJ1VmF5RWkwUHJSa3hsakE?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxQMW80REYyUDN1VnJZMXF0bkY0SG1oaXVFRzVUZUFLSkhIM1lmUG5MZ09US1BJWFBWdXZSVkNMS0VEbkc2YkEwR2t2MkJYTUpWX3BSNF94TzhTcndLUnR0eTU3MXpKbDY2M0R2aVAtSDBsdDN0UERzYmQySFNkZ1IxYU5hc2M0VktOZXlTX1hjNDJ3YTFXWlBsWHdNR011SDR1Z1B0anVmSGVvOU15a2QzWGs5S2hBQUhka3NkSHBlSnNTV1AybGRfbQ?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxPSm1ZUUJWRXFGX2JISW5WVmlLT0w5NnJlZVMtQ011THEtclVzRVoycnFsOVJjaGE5Zi1oTUpsc2xXYWRCV3d0QTBCWXkyVzZZT1ZCbDV3NGhWREZNazkwNmNETDU1REltcTNIa3dlUGs5VDhsV0h0LVFMMGhKNWZ2TlcyTFpDYjFQdEFPVW9SeUplWURYWWJNT09DRzVralF4WDktMzJKdHNLTkNWSmUzTHQ1OTlKQ3BTa3lTTTU1TFBIaE5CVXhXbjVQTG9NSkpsS2dXTmhQREtPZEdDaWc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNZWdjRm1Qakg2VzlXMnZJR3p1VHQzVE1nLUxJcTJvQW9fUHZjWURPSnhPSGU3eVphcU1rRllwc01lcWpnelZYV0VsZVBsYjQ3U1RhSi1IZHM2bVROV3JybXF6c0dlUUFKSGRuZGdad1FYQ3Uzb1RKbjdMaW9VbTdhVEZUZlRPNzVHZnRMSW5QcDdQaXluYktxRm9qM08?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPSjJJOEJ2LTRLWnJjRmJ4a1dzOVFqRFRmbk5mdnFUQlFzTUVSNFk4cnhvdktQN21EeXptYlM0eWhuWlpiSmZDc3FfQ041azlrc202MDd5NERkNHd6aWtVZGltOHJFaXN0dzhXREx5NnhqN0prRk9iWndsSDlQSVkyODA3VWxfcjFmRzlxWk5qWG1DMnR6R0Myd3FtOEV0cnpHVHlHS0ZONTRnZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
