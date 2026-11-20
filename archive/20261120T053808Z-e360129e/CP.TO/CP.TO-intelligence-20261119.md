# CP.TO Intelligence Report

- ticker: **CP.TO**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/CP.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CP.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T06:05:53.655551+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 13, 'rule': 0, 'ai': 11, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261119T054856Z-9eb86811/CP.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 13 unique headlines; 8 named publishers; 0 exact duplicates; 13 HTTPS source links; largest publisher share 30.77%; oldest publication 2026-11-12

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 131.1100 |
| Return 1D (%) | -1.8564 |
| Return 1W (%) | -2.7013 |
| Return 1M (%) | 7.2562 |
| Return YTD (%) | 30.5842 |
| Return 1Y (%) | 35.7819 |
| Annualized volatility (%) | 22.0385 |
| Beta vs SPY | 0.3534 |
| Max drawdown (%) | -11.9692 |
| Sharpe (rf=0) | 1.5039 |
| Downside deviation (rf=0, %) | 14.4195 |
| Sortino (rf=0) | 2.2986 |
| Historical VaR 95% (1D, %) | 1.8632 |
| Historical ES 95% (1D, %) | 2.9374 |
| Correlation vs SPY | 0.2222 |
| Tracking error vs SPY (%) | 23.4688 |
| P/E (trailing) | 29.73 |
| P/B | 2.49 |
| EV/EBITDA | 16.63 |
| Revenue growth (%) | 15.20 |
| Forward P/E (estimate) | 22.20 |
| Gross margin (%) | 52.76 |
| Operating margin (%) | 39.78 |
| Return on equity (%) | 8.27 |
| Free cash flow yield (%) | 2.40 |
| MA50 | 125.6624 |
| Close vs MA50 (%) | 4.3351 |
| MA200 | 121.2326 |
| Close vs MA200 (%) | 8.1475 |
| RSI (14, Wilder) | 54.3769 |
| MACD (12,26) | 2.3975 |
| MACD signal (9) | 2.3765 |
| MACD histogram | 0.0210 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CP.TO': 285, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 131.1100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.8564 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.7013 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.2562 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 30.5842 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 35.7819 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.0385 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.4195 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.2986 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8632 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9374 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2222 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.4688 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3534 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.9692 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.5039 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.2034 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.7640 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 39.7760 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.2680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.4030 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 29.7302 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 54.3769 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0210 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.3351 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 8.1475 -> Clearly above the moving-average trend level.

## TAILWINDS

### S&P/TSX Composite Index Canadian Pacific Kansas City Limited (TSX:CP) Large Cap Growth Stock: Infrastructure and Industrial-Demand Watch
- Summary: Stock listed as watch, indicating analyst interest.
- Date: 2026-11-13 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi-gFBVV95cUxPa2hIYml0NFdSbUFFSkVnUnhlQ3htc05LTEpMR1ZTTVgtVEo4MDZZc1JIUTBHNTdpWlNyU3l3dDBrUlY2X2hoSEJJcDRobjF3VlAwV1hmN2VZYkRSYmFfclhCcVFPbTBWLWF4LUZmNnFHM2x0b3VuOWJITWZoNEVNX2ZlMlV3ME5vMnhoWHB4QlhsNlJOYjZxVTFfY0JuMGE0Z01JLURYMnQ2dnYySGFhbnNJRzB2clBtSUY5XzBDemlBWWZfTkRtdFJnUXFHbFpMWVJDZFNiTVFXc0VZRWtJd2RYUE1HdjBjR2tmREdGVWFQMHAyVTJpbGxB?oc=5>

### Canadian Pacific Kansas City (CP) Stock Forecast and Price Target 2026 $CP
- Summary: Forecasts and price target for CP for 2026.
- Date: 2026-11-13 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiYEFVX3lxTE0xbk84NjVMX1ZDWENSeDZoYzVYb0xkRHh1bHppV2l6STBLMFNkeTlHR1gwdUY3NUIwcFFsVUxhZUtZbnZkLWRiWnBSb0RkNjNycTRMTGprN0NfdnRGOW1jSA?oc=5>

### CPKC at 26th Annual Scotiabank Transportation & Industrials Conference: growth outlook
- Summary: Conference presentation on growth outlook for CP.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxPcVktM0hxcUl5SXNKdFRjRnFUWDgwSmRxU2s5Ui10R3FBQ2JYcC16WGFRUExmTlBiWmw3cC1wVHF2U2pCYXQxZjRUQ3ZDcXN5YXhmLUVZbi0wWXA0SFlxUXhLQ0VrUi1FWWVpcV85Rjh1aS1fUWRvTEhsVmJENW1qYlU2Vi1lMm9ZM3g3SEl4Q3hpbHBTOURfdVItU0lWcHVUeEJQTXFrMkZlWENDNlJKY3RBRndsYjZ4dWJIT1RQTnVkYktyQWdMWFU2RXlxS3YxT1ZOUjVOcENqcUZrTEE?oc=5>

### Is CPKC (TSX:CP) Positioned For Stronger Growth Across Markets?
- Summary: Question about CP's growth potential across markets.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQWkZ3Q3EzWi0yaWhoZlZlZjF5eDFnQUZUNmZfUW9QYjk4ek9RbENOZVlCQzc0ZFZKQTNtMUhydTV0TFJjWng4RktDVGdZN0Q5VnRGUlNBb1FZaFRRM184UWdQTWNkeDBpTlhTMHJDX0lqd1ZkQjlOcDBkOGJrY3JsWlZEc0RSaXRCRjQ2TTJKSkdBY0RYdEZuWW5YY2NZbUdkSHJrNDRKemQ?oc=5>

### Canadian Pacific Kansas City Li (CP) Stock Forecasts
- Summary: Stock forecasts for CP.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxPdkxFTnlhcU5nMmxISnU2SE9abU1QNHRUWkJ3YTR1dkUxM1Z3SnJiUHNZTXhxMnEtZm9fbXl3Sjl3YzhMU2JoSVV3akxkLWlJZEFYTXpPU1VKa1ExeXVBbFpWLTc2bkU2LVo5QVc4N3FESEdoblJqY3NYc1RXUEl4N1QzVXczMllD?oc=5>

### Canadian Pacific Kansas City stock highlights record October grain volumes
- Summary: Highlights record grain volumes for CP in October.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQQ0ZoTzdVOVNhQk9MRng2cGtaQU96RHBTWFBPeWxXVUdHWFpoY1dCT0RrZTZHbVNtaWdZX3VXSzhOal9xY1hoRmdYX0kwOHptMHFwWmI4TFNQLVh0VlJkSGFOcFUzS3ZvM251VlMxeGxfMVpoUzV2dWx5UldzTVJSVmVIZ2laYV9FTi10NHNxSkltZXRvdXJJNS1Tc3RLQ2tkY21iaUtWcVJ6TTFodWF0c2FYeWMydjVTcFRobllNQzZrMHR4aXNKcVBuSFU2Nlc5Mlc4?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Canadian Pacific Kansas City (TSX:CP) Rallies On Cross Border Network Story, Is It Still Undervalued?
- Summary: Shares rally on cross-border network news, questioning undervaluation.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxONDhjWUpnQ0kzUDM0MEpqZHBhS2QtbzhKcy0wZ2pPTmZkZExjVXdtR0ptU0VEaXg5QVh2dGFwOE40UEwzeWkwSUE2MjFxenlzU1c1Q1N0OG1nanA4RkFhOU5DY0R5X3hoeUZ5aDJjbk8zSXl0a1N2cVZiM3ZPZHltdEJ6OTM0eWRSbW5NSEZLZXBzdGR2TFF2NHNnMjhZUQ?oc=5>

### Canadian Pacific Kansas City (TSX:CP) Stock Could Be Above Fair Value As Merger Debate Heats Up
- Summary: Market views stock potentially overvalued amid merger debate.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxNbzR0UWF3ZkNlOTFiVWROVFRPQzdab1pyR0wzM09pZG5IWG94Q3hvWVo4dXZnb0E5OEV3aklFLTA3T3otd2M0YWZaVGg0X3pINzAtTjVnQ1p1MmJPbEdHUXFBT3dMNGN1c3lDY0JhTzg5bDExTm5xT1hJcUxMR1RhWkNGZmUtX2J4ZlRybDA5LTMtVFprQ0NYNFRCS1ZIN250cDcwRmFTV2lZRjh3ZDgydUJidC0wbTdTY2J6RGptY3NncFZtcUFFanByMEQzQVlRbWx5ckpvelBmYU5qN21NU3l1UndTa2pveFpR0gHwAUFVX3lxTE1pcjktaHRUYS0xSTRIcUE5eUVsejI2ZEpaODBQUF9fSEdmTkVxSHlWOThyMklJRE5aLVdHT3VydllESUpQdE5EUkFON0F2UFRROGxPWEpNSGFDdVprcURMdEtHR3RpTTN4R0hnbVZNMkZ6c3pUYUdtWm5oLVdfR3ZyRWhXbUNndU9zMXdld1lkcnlUYUstUUZFdEFIdmp6ZkUzRnVZeko3WFM1emlTWmhOTFJhU0lLWFpPU2l3cmtSS3dMbkI1dGV1Q1VzYXE3NHZDZUN3NlBJZmtFZ0luXzZSQk50MGNtOU1EUFVwNElScw?oc=5>

### Canadian Pacific Kansas City stock: executives set for Nov. 17 event
- Summary: CP executives will hold a scheduled event on Nov. 17, potentially discussing company strategy and outlook.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxQMW80REYyUDN1VnJZMXF0bkY0SG1oaXVFRzVUZUFLSkhIM1lmUG5MZ09US1BJWFBWdXZSVkNMS0VEbkc2YkEwR2t2MkJYTUpWX3BSNF94TzhTcndLUnR0eTU3MXpKbDY2M0R2aVAtSDBsdDN0UERzYmQySFNkZ1IxYU5hc2M0VktOZXlTX1hjNDJ3YTFXWlBsWHdNR011SDR1Z1B0anVmSGVvOU15a2QzWGs5S2hBQUhka3NkSHBlSnNTV1AybGRfbQ?oc=5>

### Canadian Pacific Kansas City stock: executives signal stronger growth path
- Summary: Executives indicate a stronger growth trajectory for CP.TO, suggesting improved future performance.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQLXI3ZDFZeUhxSjlxVlQwQnRkbFJ5My10MjFubW0tblh2LW5mWGhxeDJ3a0RqYnc2Y0ZobG1sMjZGTndFZjVxZWVHWHpEdXppTzNJWjdSWEs4Y2IyZTZRNFF0QmFYVkd1ZEs0UGlyWDJLVlRLMjBHTGpVdXc5VldXdnppX0JuS242bXR6VWEzSllYSkt0WV9VdUJ5ZjdSblZFNGVieE84U3QycHRxLUpXQWM5UU9uQXk4NFN1UmYyMXRZSHJ1VmF5RWkwUHJSa3hsakE?oc=5>

## RISKS

### Does CPKC (TSX:CP) Have The Order Quality To Weather Volatility?
- Summary: Questioning order quality raises uncertainty about resilience.
- Date: 2026-11-18 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPSjJJOEJ2LTRLWnJjRmJ4a1dzOVFqRFRmbk5mdnFUQlFzTUVSNFk4cnhvdktQN21EeXptYlM0eWhuWlpiSmZDc3FfQ041azlrc202MDd5NERkNHd6aWtVZGltOHJFaXN0dzhXREx5NnhqN0prRk9iWndsSDlQSVkyODA3VWxfcjFmRzlxWk5qWG1DMnR6R0Myd3FtOEV0cnpHVHlHS0ZONTRnZw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CP.TO** | **29.73** | **2.49** | **16.63** | **15.20** | **114,007,326,720.00 CAD** | **35.78** |
| CNR.TO | 22.30 | 4.89 | 13.87 | 14.60 | 107,142,397,952.00 CAD | 39.06 |
| UNP | 23.48 | 7.84 | 15.11 | 15.30 | 172,707,004,416.00 USD | 34.18 |
| NSC | 26.56 | 4.25 | 14.97 | 13.60 | 71,163,060,224.00 USD | 14.34 |

Peers fetched as_of: 2026-11-19; CP.TO reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

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

- https://news.google.com/rss/articles/CBMi-gFBVV95cUxPa2hIYml0NFdSbUFFSkVnUnhlQ3htc05LTEpMR1ZTTVgtVEo4MDZZc1JIUTBHNTdpWlNyU3l3dDBrUlY2X2hoSEJJcDRobjF3VlAwV1hmN2VZYkRSYmFfclhCcVFPbTBWLWF4LUZmNnFHM2x0b3VuOWJITWZoNEVNX2ZlMlV3ME5vMnhoWHB4QlhsNlJOYjZxVTFfY0JuMGE0Z01JLURYMnQ2dnYySGFhbnNJRzB2clBtSUY5XzBDemlBWWZfTkRtdFJnUXFHbFpMWVJDZFNiTVFXc0VZRWtJd2RYUE1HdjBjR2tmREdGVWFQMHAyVTJpbGxB?oc=5
- https://news.google.com/rss/articles/CBMiYEFVX3lxTE0xbk84NjVMX1ZDWENSeDZoYzVYb0xkRHh1bHppV2l6STBLMFNkeTlHR1gwdUY3NUIwcFFsVUxhZUtZbnZkLWRiWnBSb0RkNjNycTRMTGprN0NfdnRGOW1jSA?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxPcVktM0hxcUl5SXNKdFRjRnFUWDgwSmRxU2s5Ui10R3FBQ2JYcC16WGFRUExmTlBiWmw3cC1wVHF2U2pCYXQxZjRUQ3ZDcXN5YXhmLUVZbi0wWXA0SFlxUXhLQ0VrUi1FWWVpcV85Rjh1aS1fUWRvTEhsVmJENW1qYlU2Vi1lMm9ZM3g3SEl4Q3hpbHBTOURfdVItU0lWcHVUeEJQTXFrMkZlWENDNlJKY3RBRndsYjZ4dWJIT1RQTnVkYktyQWdMWFU2RXlxS3YxT1ZOUjVOcENqcUZrTEE?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQWkZ3Q3EzWi0yaWhoZlZlZjF5eDFnQUZUNmZfUW9QYjk4ek9RbENOZVlCQzc0ZFZKQTNtMUhydTV0TFJjWng4RktDVGdZN0Q5VnRGUlNBb1FZaFRRM184UWdQTWNkeDBpTlhTMHJDX0lqd1ZkQjlOcDBkOGJrY3JsWlZEc0RSaXRCRjQ2TTJKSkdBY0RYdEZuWW5YY2NZbUdkSHJrNDRKemQ?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxPdkxFTnlhcU5nMmxISnU2SE9abU1QNHRUWkJ3YTR1dkUxM1Z3SnJiUHNZTXhxMnEtZm9fbXl3Sjl3YzhMU2JoSVV3akxkLWlJZEFYTXpPU1VKa1ExeXVBbFpWLTc2bkU2LVo5QVc4N3FESEdoblJqY3NYc1RXUEl4N1QzVXczMllD?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQQ0ZoTzdVOVNhQk9MRng2cGtaQU96RHBTWFBPeWxXVUdHWFpoY1dCT0RrZTZHbVNtaWdZX3VXSzhOal9xY1hoRmdYX0kwOHptMHFwWmI4TFNQLVh0VlJkSGFOcFUzS3ZvM251VlMxeGxfMVpoUzV2dWx5UldzTVJSVmVIZ2laYV9FTi10NHNxSkltZXRvdXJJNS1Tc3RLQ2tkY21iaUtWcVJ6TTFodWF0c2FYeWMydjVTcFRobllNQzZrMHR4aXNKcVBuSFU2Nlc5Mlc4?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxONDhjWUpnQ0kzUDM0MEpqZHBhS2QtbzhKcy0wZ2pPTmZkZExjVXdtR0ptU0VEaXg5QVh2dGFwOE40UEwzeWkwSUE2MjFxenlzU1c1Q1N0OG1nanA4RkFhOU5DY0R5X3hoeUZ5aDJjbk8zSXl0a1N2cVZiM3ZPZHltdEJ6OTM0eWRSbW5NSEZLZXBzdGR2TFF2NHNnMjhZUQ?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxNbzR0UWF3ZkNlOTFiVWROVFRPQzdab1pyR0wzM09pZG5IWG94Q3hvWVo4dXZnb0E5OEV3aklFLTA3T3otd2M0YWZaVGg0X3pINzAtTjVnQ1p1MmJPbEdHUXFBT3dMNGN1c3lDY0JhTzg5bDExTm5xT1hJcUxMR1RhWkNGZmUtX2J4ZlRybDA5LTMtVFprQ0NYNFRCS1ZIN250cDcwRmFTV2lZRjh3ZDgydUJidC0wbTdTY2J6RGptY3NncFZtcUFFanByMEQzQVlRbWx5ckpvelBmYU5qN21NU3l1UndTa2pveFpR0gHwAUFVX3lxTE1pcjktaHRUYS0xSTRIcUE5eUVsejI2ZEpaODBQUF9fSEdmTkVxSHlWOThyMklJRE5aLVdHT3VydllESUpQdE5EUkFON0F2UFRROGxPWEpNSGFDdVprcURMdEtHR3RpTTN4R0hnbVZNMkZ6c3pUYUdtWm5oLVdfR3ZyRWhXbUNndU9zMXdld1lkcnlUYUstUUZFdEFIdmp6ZkUzRnVZeko3WFM1emlTWmhOTFJhU0lLWFpPU2l3cmtSS3dMbkI1dGV1Q1VzYXE3NHZDZUN3NlBJZmtFZ0luXzZSQk50MGNtOU1EUFVwNElScw?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxQMW80REYyUDN1VnJZMXF0bkY0SG1oaXVFRzVUZUFLSkhIM1lmUG5MZ09US1BJWFBWdXZSVkNMS0VEbkc2YkEwR2t2MkJYTUpWX3BSNF94TzhTcndLUnR0eTU3MXpKbDY2M0R2aVAtSDBsdDN0UERzYmQySFNkZ1IxYU5hc2M0VktOZXlTX1hjNDJ3YTFXWlBsWHdNR011SDR1Z1B0anVmSGVvOU15a2QzWGs5S2hBQUhka3NkSHBlSnNTV1AybGRfbQ?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQLXI3ZDFZeUhxSjlxVlQwQnRkbFJ5My10MjFubW0tblh2LW5mWGhxeDJ3a0RqYnc2Y0ZobG1sMjZGTndFZjVxZWVHWHpEdXppTzNJWjdSWEs4Y2IyZTZRNFF0QmFYVkd1ZEs0UGlyWDJLVlRLMjBHTGpVdXc5VldXdnppX0JuS242bXR6VWEzSllYSkt0WV9VdUJ5ZjdSblZFNGVieE84U3QycHRxLUpXQWM5UU9uQXk4NFN1UmYyMXRZSHJ1VmF5RWkwUHJSa3hsakE?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPSjJJOEJ2LTRLWnJjRmJ4a1dzOVFqRFRmbk5mdnFUQlFzTUVSNFk4cnhvdktQN21EeXptYlM0eWhuWlpiSmZDc3FfQ041azlrc202MDd5NERkNHd6aWtVZGltOHJFaXN0dzhXREx5NnhqN0prRk9iWndsSDlQSVkyODA3VWxfcjFmRzlxWk5qWG1DMnR6R0Myd3FtOEV0cnpHVHlHS0ZONTRnZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
