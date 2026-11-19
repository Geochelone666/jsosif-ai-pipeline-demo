# CP.TO Intelligence Report

- ticker: **CP.TO**
- Report as_of: **2026-11-18**
- Market data as_of: **2026-11-18**
- Quant sources: https://finance.yahoo.com/quote/CP.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CP.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-18**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-19T05:58:41.246972+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 8, 'rule': 0, 'ai': 7, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/CP.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 8 unique headlines; 7 named publishers; 0 exact duplicates; 8 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 133.5900 |
| Return 1D (%) | 0.2175 |
| Return 1W (%) | -0.0075 |
| Return 1M (%) | 8.1876 |
| Return YTD (%) | 33.0542 |
| Return 1Y (%) | 38.7063 |
| Annualized volatility (%) | 21.9479 |
| Beta vs SPY | 0.3396 |
| Max drawdown (%) | -11.9692 |
| Sharpe (rf=0) | 1.6068 |
| Downside deviation (rf=0, %) | 14.2990 |
| Sortino (rf=0) | 2.4663 |
| Historical VaR 95% (1D, %) | 1.8632 |
| Historical ES 95% (1D, %) | 2.9374 |
| Correlation vs SPY | 0.2122 |
| Tracking error vs SPY (%) | 23.4699 |
| P/E (trailing) | 30.92 |
| P/B | 2.54 |
| EV/EBITDA | 16.88 |
| Revenue growth (%) | 15.20 |
| Forward P/E (estimate) | 22.62 |
| Gross margin (%) | 52.76 |
| Operating margin (%) | 39.78 |
| Return on equity (%) | 8.27 |
| Free cash flow yield (%) | 2.36 |
| MA50 | 125.5240 |
| Close vs MA50 (%) | 6.4258 |
| MA200 | 121.0959 |
| Close vs MA200 (%) | 10.3175 |
| RSI (14, Wilder) | 62.5072 |
| MACD (12,26) | 2.6886 |
| MACD signal (9) | 2.3712 |
| MACD histogram | 0.3174 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CP.TO': 284, 'SPY': 285}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 133.5900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.2175 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.0075 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 8.1876 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 33.0542 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 38.7063 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.9479 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.2990 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.4663 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8632 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9374 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2122 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.4699 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3396 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.9692 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.6068 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.6234 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.7640 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 39.7760 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.2680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.3584 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 30.9236 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 62.5072 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3174 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.4258 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 10.3175 -> Clearly above the moving-average trend level.

## TAILWINDS

### S&P/TSX Composite Index Canadian Pacific Kansas City Limited (TSX:CP) Large Cap Growth Stock: Infrastructure and Industrial-Demand Watch
- Summary: Stock listed as watch, indicating analyst interest.
- Date: 2026-11-13 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi-gFBVV95cUxPa2hIYml0NFdSbUFFSkVnUnhlQ3htc05LTEpMR1ZTTVgtVEo4MDZZc1JIUTBHNTdpWlNyU3l3dDBrUlY2X2hoSEJJcDRobjF3VlAwV1hmN2VZYkRSYmFfclhCcVFPbTBWLWF4LUZmNnFHM2x0b3VuOWJITWZoNEVNX2ZlMlV3ME5vMnhoWHB4QlhsNlJOYjZxVTFfY0JuMGE0Z01JLURYMnQ2dnYySGFhbnNJRzB2clBtSUY5XzBDemlBWWZfTkRtdFJnUXFHbFpMWVJDZFNiTVFXc0VZRWtJd2RYUE1HdjBjR2tmREdGVWFQMHAyVTJpbGxB?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Canadian Pacific Kansas City (TSX:CP) Rallies On Cross Border Network Story, Is It Still Undervalued?
- Summary: Shares rally on cross-border network news, questioning undervaluation.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxONDhjWUpnQ0kzUDM0MEpqZHBhS2QtbzhKcy0wZ2pPTmZkZExjVXdtR0ptU0VEaXg5QVh2dGFwOE40UEwzeWkwSUE2MjFxenlzU1c1Q1N0OG1nanA4RkFhOU5DY0R5X3hoeUZ5aDJjbk8zSXl0a1N2cVZiM3ZPZHltdEJ6OTM0eWRSbW5NSEZLZXBzdGR2TFF2NHNnMjhZUQ?oc=5>

### Canadian Pacific Kansas City stock: executives set for Nov. 17 event
- Summary: CP executives will hold a scheduled event on Nov. 17, potentially discussing company strategy and outlook.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxQMW80REYyUDN1VnJZMXF0bkY0SG1oaXVFRzVUZUFLSkhIM1lmUG5MZ09US1BJWFBWdXZSVkNMS0VEbkc2YkEwR2t2MkJYTUpWX3BSNF94TzhTcndLUnR0eTU3MXpKbDY2M0R2aVAtSDBsdDN0UERzYmQySFNkZ1IxYU5hc2M0VktOZXlTX1hjNDJ3YTFXWlBsWHdNR011SDR1Z1B0anVmSGVvOU15a2QzWGs5S2hBQUhka3NkSHBlSnNTV1AybGRfbQ?oc=5>

### CPKC's President and CEO Keith Creel to address the 2026 UBS Global Industrials and Transportation Conference
- Summary: CEO will speak at 2026 conference, discussing company outlook.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNZWdjRm1Qakg2VzlXMnZJR3p1VHQzVE1nLUxJcTJvQW9fUHZjWURPSnhPSGU3eVphcU1rRllwc01lcWpnelZYV0VsZVBsYjQ3U1RhSi1IZHM2bVROV3JybXF6c0dlUUFKSGRuZGdad1FYQ3Uzb1RKbjdMaW9VbTdhVEZUZlRPNzVHZnRMSW5QcDdQaXluYktxRm9qM08?oc=5>

### CPKC at 26th Annual Scotiabank Transportation & Industrials Conference: growth outlook
- Summary: Company presents growth outlook at annual conference.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxNcWtZemtaLVNBQTBwRWRPLWIwaGpPN0djQU5NZ095WmtpV3ppdV9GSUVhWnkwYjBLTEFOZ0E1cVhwelpHVmtOWDZpT0g2V19XeHBtUlNzMWYwR0lRbXdMaGNlSjRuandEbXhZVndBX3VQN0oyaG1lMTZ4V0JmR3NjdFhMTTdFR1I3dm50ZTREcHM2VWdWenR6NWI2NXpsemdYQTliRlRmYWZjbkRQV2taVF8tT3Bab3lSS2p1aEZ3ZlUwSHdpOTcyTnlfWDdyRFFJUi03Qm5KbUxOcmZNOVE?oc=5>

### Canadian Pacific Kansas City (TSX:CP) Stock Could Be Above Fair Value As Merger Debate Heats Up
- Summary: Market views stock potentially overvalued amid merger debate.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxNbzR0UWF3ZkNlOTFiVWROVFRPQzdab1pyR0wzM09pZG5IWG94Q3hvWVo4dXZnb0E5OEV3aklFLTA3T3otd2M0YWZaVGg0X3pINzAtTjVnQ1p1MmJPbEdHUXFBT3dMNGN1c3lDY0JhTzg5bDExTm5xT1hJcUxMR1RhWkNGZmUtX2J4ZlRybDA5LTMtVFprQ0NYNFRCS1ZIN250cDcwRmFTV2lZRjh3ZDgydUJidC0wbTdTY2J6RGptY3NncFZtcUFFanByMEQzQVlRbWx5ckpvelBmYU5qN21NU3l1UndTa2pveFpR0gHwAUFVX3lxTE1pcjktaHRUYS0xSTRIcUE5eUVsejI2ZEpaODBQUF9fSEdmTkVxSHlWOThyMklJRE5aLVdHT3VydllESUpQdE5EUkFON0F2UFRROGxPWEpNSGFDdVprcURMdEtHR3RpTTN4R0hnbVZNMkZ6c3pUYUdtWm5oLVdfR3ZyRWhXbUNndU9zMXdld1lkcnlUYUstUUZFdEFIdmp6ZkUzRnVZeko3WFM1emlTWmhOTFJhU0lLWFpPU2l3cmtSS3dMbkI1dGV1Q1VzYXE3NHZDZUN3NlBJZmtFZ0luXzZSQk50MGNtOU1EUFVwNElScw?oc=5>

## RISKS

### Does CPKC (TSX:CP) Have The Order Quality To Weather Volatility?
- Summary: Questioning order quality raises uncertainty about resilience.
- Date: 2026-11-18 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPSjJJOEJ2LTRLWnJjRmJ4a1dzOVFqRFRmbk5mdnFUQlFzTUVSNFk4cnhvdktQN21EeXptYlM0eWhuWlpiSmZDc3FfQ041azlrc202MDd5NERkNHd6aWtVZGltOHJFaXN0dzhXREx5NnhqN0prRk9iWndsSDlQSVkyODA3VWxfcjFmRzlxWk5qWG1DMnR6R0Myd3FtOEV0cnpHVHlHS0ZONTRnZw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CP.TO** | **30.92** | **2.54** | **16.88** | **15.20** | **116,163,813,376.00 CAD** | **38.71** |
| CNR.TO | 22.39 | 4.91 | 13.91 | 14.60 | 107,562,188,800.00 CAD | 39.81 |
| UNP | 23.47 | 8.12 | 15.57 | 15.30 | 178,809,946,112.00 USD | 39.14 |
| NSC | 27.12 | 4.34 | 15.23 | 13.60 | 72,663,498,752.00 USD | 17.18 |

Peers fetched as_of: 2026-11-18; CP.TO reuses existing data (market data as_of: 2026-11-18); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-18

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
- https://news.google.com/rss/articles/CBMingFBVV95cUxONDhjWUpnQ0kzUDM0MEpqZHBhS2QtbzhKcy0wZ2pPTmZkZExjVXdtR0ptU0VEaXg5QVh2dGFwOE40UEwzeWkwSUE2MjFxenlzU1c1Q1N0OG1nanA4RkFhOU5DY0R5X3hoeUZ5aDJjbk8zSXl0a1N2cVZiM3ZPZHltdEJ6OTM0eWRSbW5NSEZLZXBzdGR2TFF2NHNnMjhZUQ?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxQMW80REYyUDN1VnJZMXF0bkY0SG1oaXVFRzVUZUFLSkhIM1lmUG5MZ09US1BJWFBWdXZSVkNMS0VEbkc2YkEwR2t2MkJYTUpWX3BSNF94TzhTcndLUnR0eTU3MXpKbDY2M0R2aVAtSDBsdDN0UERzYmQySFNkZ1IxYU5hc2M0VktOZXlTX1hjNDJ3YTFXWlBsWHdNR011SDR1Z1B0anVmSGVvOU15a2QzWGs5S2hBQUhka3NkSHBlSnNTV1AybGRfbQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNZWdjRm1Qakg2VzlXMnZJR3p1VHQzVE1nLUxJcTJvQW9fUHZjWURPSnhPSGU3eVphcU1rRllwc01lcWpnelZYV0VsZVBsYjQ3U1RhSi1IZHM2bVROV3JybXF6c0dlUUFKSGRuZGdad1FYQ3Uzb1RKbjdMaW9VbTdhVEZUZlRPNzVHZnRMSW5QcDdQaXluYktxRm9qM08?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxNcWtZemtaLVNBQTBwRWRPLWIwaGpPN0djQU5NZ095WmtpV3ppdV9GSUVhWnkwYjBLTEFOZ0E1cVhwelpHVmtOWDZpT0g2V19XeHBtUlNzMWYwR0lRbXdMaGNlSjRuandEbXhZVndBX3VQN0oyaG1lMTZ4V0JmR3NjdFhMTTdFR1I3dm50ZTREcHM2VWdWenR6NWI2NXpsemdYQTliRlRmYWZjbkRQV2taVF8tT3Bab3lSS2p1aEZ3ZlUwSHdpOTcyTnlfWDdyRFFJUi03Qm5KbUxOcmZNOVE?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxNbzR0UWF3ZkNlOTFiVWROVFRPQzdab1pyR0wzM09pZG5IWG94Q3hvWVo4dXZnb0E5OEV3aklFLTA3T3otd2M0YWZaVGg0X3pINzAtTjVnQ1p1MmJPbEdHUXFBT3dMNGN1c3lDY0JhTzg5bDExTm5xT1hJcUxMR1RhWkNGZmUtX2J4ZlRybDA5LTMtVFprQ0NYNFRCS1ZIN250cDcwRmFTV2lZRjh3ZDgydUJidC0wbTdTY2J6RGptY3NncFZtcUFFanByMEQzQVlRbWx5ckpvelBmYU5qN21NU3l1UndTa2pveFpR0gHwAUFVX3lxTE1pcjktaHRUYS0xSTRIcUE5eUVsejI2ZEpaODBQUF9fSEdmTkVxSHlWOThyMklJRE5aLVdHT3VydllESUpQdE5EUkFON0F2UFRROGxPWEpNSGFDdVprcURMdEtHR3RpTTN4R0hnbVZNMkZ6c3pUYUdtWm5oLVdfR3ZyRWhXbUNndU9zMXdld1lkcnlUYUstUUZFdEFIdmp6ZkUzRnVZeko3WFM1emlTWmhOTFJhU0lLWFpPU2l3cmtSS3dMbkI1dGV1Q1VzYXE3NHZDZUN3NlBJZmtFZ0luXzZSQk50MGNtOU1EUFVwNElScw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPSjJJOEJ2LTRLWnJjRmJ4a1dzOVFqRFRmbk5mdnFUQlFzTUVSNFk4cnhvdktQN21EeXptYlM0eWhuWlpiSmZDc3FfQ041azlrc202MDd5NERkNHd6aWtVZGltOHJFaXN0dzhXREx5NnhqN0prRk9iWndsSDlQSVkyODA3VWxfcjFmRzlxWk5qWG1DMnR6R0Myd3FtOEV0cnpHVHlHS0ZONTRnZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
