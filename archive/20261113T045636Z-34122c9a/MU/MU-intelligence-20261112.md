# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:17:05.447842+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 0, 'ai': 10, 'unknown': 0, 'irrelevant': 12})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 11 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 40.91%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 798.4400 |
| Return 1D (%) | -1.5851 |
| Return 1W (%) | 21.6411 |
| Return 1M (%) | -19.2585 |
| Return YTD (%) | 179.9565 |
| Return 1Y (%) | 226.3972 |
| Annualized volatility (%) | 84.3079 |
| Beta vs SPY | 3.3981 |
| Max drawdown (%) | -45.8952 |
| Sharpe (rf=0) | 1.8281 |
| Downside deviation (rf=0, %) | 52.5515 |
| Sortino (rf=0) | 2.9328 |
| Historical VaR 95% (1D, %) | 7.0090 |
| Historical ES 95% (1D, %) | 10.3312 |
| Correlation vs SPY | 0.5536 |
| Tracking error vs SPY (%) | 77.5523 |
| P/E (trailing) | 10.74 |
| P/B | 6.53 |
| EV/EBITDA | 7.95 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 3.84 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 74.59 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 3.23 |
| MA50 | 947.2834 |
| Close vs MA50 (%) | -15.7127 |
| MA200 | 763.7025 |
| Close vs MA200 (%) | 4.5486 |
| RSI (14, Wilder) | 44.0784 |
| MACD (12,26) | -57.5168 |
| MACD signal (9) | -53.2390 |
| MACD histogram | -4.2778 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 798.4400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.5851 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 21.6411 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -19.2585 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 179.9565 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 226.3972 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 84.3079 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 52.5515 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.9328 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.0090 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.3312 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5536 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 77.5523 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3981 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -45.8952 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.8281 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 3.8431 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 74.5860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.2257 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 10.7418 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 44.0784 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.2778 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -15.7127 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 4.5486 -> Slightly above the moving-average trend level.

## TAILWINDS

### Micron Is Rebounding. Goldman Prefers These Memory Stocks.
- Summary: Micron’s stock rebounds, attracting Goldman’s preference for memory stocks, indicating positive market sentiment.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTFB2bWhjUktMQU1qZzVGbWF5ZE9XNmdGVmtUVU5EMUozbl9pNlJRZnJjOWl6N2ZLLUEwQVMyWEZpa19RT1NLMXZzbVZxTTlGd2lKMDNLa3FKSUUwQi1EQllKbndwY20zMUF3Q0tkeHFXSnUwQllJdGhiRjJKY3I2dw?oc=5>

### Micron Technology climbs 13% as one-month slide reverses (MU:NASDAQ)
- Summary: Micron’s stock climbs 13%, reversing a one-month decline, signaling strong investor confidence.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPSExVYU1oeW91UFFKa2VQNUx1ekRnOGFlVThvR3lGTmtxZnhQSXRsaHl4eG1YV2VGTkdxN0pZOWJmQnl5WTVXWDBaYy1IYjc4cTJ1MDZHVXAtbnZtRF96eXZfSnFVNWVwNl9iYlo1bXBjeV9XcHZmNGotRlJNNEt4al9wSWw0bTFGQXZUMGFfQXprVHhyeFNWM0lEdWJvUUFTRTM0?oc=5>

### I Still Think Micron Stock Is a Buy. Here's the Price at Which I'd Sell It.
- Summary: Analyst expresses bullish view and target sell price for Micron shares.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNY2stTE5ZNjFmLXlvbkxTMFNzZXduV1BwdDdRRmV6YnBPa2xlWTZqUjhaNmoxb0J0MG10THZQSXBDWEVUWkgwdVpUVE9Zd3dDYlh5aWVrUkZiS3E4LURZbV9xMS1pSlpVU1ZjVnpUbXNIelR6aldwWlVYdFBpWnNkbHplTUFLeEtpNkFmQTkzN1hMN3hwd0lnX0dYang5a3FzQ256SzNELWpwTDhzNl81Vk5oX2ZDbDA?oc=5>

### Micron Stock Is Down 40% From Its Peak After the Sell-Off. History Says This Is What Happens Next.
- Summary: Micron’s shares fell 40% post sell-off, suggesting a potential rebound per historical patterns.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOc3hPSUpZNHRWLXNkRFpvYzl2YWZ4RDVWeThpUkVLX0Z3aUdmc01GTktyNWw4MHpNWHZaU04tVTkxeG5VLTd2Um1qZGJ5QzFWNzN1MHdZaERSdGRieTdwOGI3djlfVXEyY2hYMTZRT1JFTkZXdFBXZ3dONE9oOTVuRGdYbmZfS2xGbEl2VGlHTlRsQlpm?oc=5>

### Why Micron Technology Stock Gained On Monday
- Summary: MU stock rose Monday.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNb1hrRzc0OGpMSFBjQ0lmcVpCY3YwMGZ2dFhHSXRaWHU4b0xubTNHaE8yUzBxT3BBQk5xcnZrSHY0QWpKVUdzb1lUMFRldWpSLVpEbFg2QXZRM0ZtN0tKczJnaFJDanlKZmROQWN5SzdnNUU4VEVpamI3WWFLdkpTQmVrQUk4QUpGWXQzUXM4eWtSVG5zU2prOER0TVNXeThH?oc=5>

## HEADWINDS

### Micron Technology Stocks Slip 1.27% as Hot CPI Overshadows $1 Billion Anthropic Bet
- Summary: Micron shares fall 1.27% due to inflation concerns outweighing AI investment.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPb3ltSGpYNHg5X1N1VW5PMEJtTk5Ba0hkakhXWjdXOFRvVnp3aGxROFgyWHRheFZxMG1MY1YtT3RXN25hcTgwT2xaUEphbjJrVWI1UHgzZ1VxN1FLNXdjYm1yZTJtT2hjdjJRVDVtR01BT0c3R0RqanFYd1BQdnlRdm1KdktwZ0tOMmNxRndoRWVLSFhlci1MQWNCYU8?oc=5>

### Micron Stock Pulls Back After 184% Rally. Who Still Owns MU Stock?
- Summary: MU stock retraces after huge rally.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOakxpTG5idlpTaGhxMEdLM050TTVhZ2VzXy1NMkgtWm9uOVI2SDhLSVJZckhDdUhTUnVMZVZxOEVabDBYcGhKdTZsTTd4LUp3WjVQNGt0enU0dFZpVEh2NG1FYTQwOVNvc1BKRXhIRXV0ZGF0NVV4SEYyR0pqZVcxcGhPc21YeFQxeVJhQ0N0QnA0NzNLbFk1eg?oc=5>

### Micron Technology Inc Stock (MU) Opened Down by 3.17% on Nov 12: What Investors Need To Know
- Summary: MU opened down 3.17% Nov 12.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxPVW1nV3ZQWl9BZ1drYWMzZEMyc0hsNXE4N2k3RjdHcE13YXJ2cFdlMnhseFhreTNidjgwcjRGU3htOU5nLVdDVE1BWVlhckFzbXZveDJjUlB0aVRPZHhYWWxLZXdPbWdIaVFGMDZfTTdrWm9pU0hTRV84MVlKS3NOWHdvMFFzczhE?oc=5>

## CATALYSTS

### Prediction: This Will Be Micron's Stock Price by the End of 2027
- Summary: Predicted MU stock price by end 2027.
- Date: 2026-11-12 | Impact: medium | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQdExhLTYyT2s0OGJycElyRmxOTE1sWjRVRUhRajhPMld4VGNzZlpvSHJzWi1GYTdSZDROdEJZUmJHNU9CaXl6aFY0dTdtZHgtd243Z0M3WnNEemdwWHZUX3d2YjVHZXpaSG95aExpaEV0Ri1henl5akpqRzVRUi1QWG9sVVJ0UFl1OTZndlhPWEczTUhYbEp1Q3MwWjNtWmVp?oc=5>

### Why You Should Think About Micron Differently Now
- Summary: Opinion urges new perspective on MU.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPcFNnQTlwa05zX0NIRktFcVBSaF9RMTFkVXJUbERZNFlVTzdqM2FGdDkwQVFtdGpnQUhtU2hqSklFb1VLOWkwT1RsWEE2Mzg4cmsycFE1VndieDBjZzJDU0dVeWpwU3VXdlhMNXBtWlRoYVd1YnNIQmEtY2JBVFBpdldSVlFiT2RLeVVYT3dHTGp6bTM5LXFfRVhVYnJPMVNUaC1GaVh2VlZVQTBx?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **10.74** | **6.53** | **7.95** | **379.30** | **903,373,586,432.00 USD** | **226.40** |
| WDC | 10.95 | 12.45 | 18.39 | 55.50 | 116,493,139,968.00 USD | 87.70 |
| STX | 28.59 | 36.27 | 21.57 | 61.00 | 125,142,941,696.00 USD | 93.59 |
| NXPI | 21.03 | 5.57 | 13.88 | 19.30 | 67,371,245,568.00 USD | 33.29 |

Peers fetched as_of: 2026-11-12; MU reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-09
- Revenue (latest available single quarter): 8,440,000,000.00 USD; period 2018-06-01/2018-08-30; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 28,243,000,000.00 USD; period 2026-02-27/2026-05-28; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMifkFVX3lxTFB2bWhjUktMQU1qZzVGbWF5ZE9XNmdGVmtUVU5EMUozbl9pNlJRZnJjOWl6N2ZLLUEwQVMyWEZpa19RT1NLMXZzbVZxTTlGd2lKMDNLa3FKSUUwQi1EQllKbndwY20zMUF3Q0tkeHFXSnUwQllJdGhiRjJKY3I2dw?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPSExVYU1oeW91UFFKa2VQNUx1ekRnOGFlVThvR3lGTmtxZnhQSXRsaHl4eG1YV2VGTkdxN0pZOWJmQnl5WTVXWDBaYy1IYjc4cTJ1MDZHVXAtbnZtRF96eXZfSnFVNWVwNl9iYlo1bXBjeV9XcHZmNGotRlJNNEt4al9wSWw0bTFGQXZUMGFfQXprVHhyeFNWM0lEdWJvUUFTRTM0?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNY2stTE5ZNjFmLXlvbkxTMFNzZXduV1BwdDdRRmV6YnBPa2xlWTZqUjhaNmoxb0J0MG10THZQSXBDWEVUWkgwdVpUVE9Zd3dDYlh5aWVrUkZiS3E4LURZbV9xMS1pSlpVU1ZjVnpUbXNIelR6aldwWlVYdFBpWnNkbHplTUFLeEtpNkFmQTkzN1hMN3hwd0lnX0dYang5a3FzQ256SzNELWpwTDhzNl81Vk5oX2ZDbDA?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOc3hPSUpZNHRWLXNkRFpvYzl2YWZ4RDVWeThpUkVLX0Z3aUdmc01GTktyNWw4MHpNWHZaU04tVTkxeG5VLTd2Um1qZGJ5QzFWNzN1MHdZaERSdGRieTdwOGI3djlfVXEyY2hYMTZRT1JFTkZXdFBXZ3dONE9oOTVuRGdYbmZfS2xGbEl2VGlHTlRsQlpm?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNb1hrRzc0OGpMSFBjQ0lmcVpCY3YwMGZ2dFhHSXRaWHU4b0xubTNHaE8yUzBxT3BBQk5xcnZrSHY0QWpKVUdzb1lUMFRldWpSLVpEbFg2QXZRM0ZtN0tKczJnaFJDanlKZmROQWN5SzdnNUU4VEVpamI3WWFLdkpTQmVrQUk4QUpGWXQzUXM4eWtSVG5zU2prOER0TVNXeThH?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPVE1LVjVKalFkQlVCVFVaU0Z6OWtfYW1ES0lMZmI5c1NPN213eFo3cXhqdWNiX2txVFpBc1FyUTk1ZV8wZ0pGWlV3NHB6X213a1BCODJYWUV4SExXMU1yOFQ1YV9VZF9qZGF2NDlQMkpnSDV4OFV2aFczUWF5QWdUR1pZVU9RTlJUc0Z6VEUyNFc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPb3ltSGpYNHg5X1N1VW5PMEJtTk5Ba0hkakhXWjdXOFRvVnp3aGxROFgyWHRheFZxMG1MY1YtT3RXN25hcTgwT2xaUEphbjJrVWI1UHgzZ1VxN1FLNXdjYm1yZTJtT2hjdjJRVDVtR01BT0c3R0RqanFYd1BQdnlRdm1KdktwZ0tOMmNxRndoRWVLSFhlci1MQWNCYU8?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOakxpTG5idlpTaGhxMEdLM050TTVhZ2VzXy1NMkgtWm9uOVI2SDhLSVJZckhDdUhTUnVMZVZxOEVabDBYcGhKdTZsTTd4LUp3WjVQNGt0enU0dFZpVEh2NG1FYTQwOVNvc1BKRXhIRXV0ZGF0NVV4SEYyR0pqZVcxcGhPc21YeFQxeVJhQ0N0QnA0NzNLbFk1eg?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxPVW1nV3ZQWl9BZ1drYWMzZEMyc0hsNXE4N2k3RjdHcE13YXJ2cFdlMnhseFhreTNidjgwcjRGU3htOU5nLVdDVE1BWVlhckFzbXZveDJjUlB0aVRPZHhYWWxLZXdPbWdIaVFGMDZfTTdrWm9pU0hTRV84MVlKS3NOWHdvMFFzczhE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQdExhLTYyT2s0OGJycElyRmxOTE1sWjRVRUhRajhPMld4VGNzZlpvSHJzWi1GYTdSZDROdEJZUmJHNU9CaXl6aFY0dTdtZHgtd243Z0M3WnNEemdwWHZUX3d2YjVHZXpaSG95aExpaEV0Ri1henl5akpqRzVRUi1QWG9sVVJ0UFl1OTZndlhPWEczTUhYbEp1Q3MwWjNtWmVp?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPcFNnQTlwa05zX0NIRktFcVBSaF9RMTFkVXJUbERZNFlVTzdqM2FGdDkwQVFtdGpnQUhtU2hqSklFb1VLOWkwT1RsWEE2Mzg4cmsycFE1VndieDBjZzJDU0dVeWpwU3VXdlhMNXBtWlRoYVd1YnNIQmEtY2JBVFBpdldSVlFiT2RLeVVYT3dHTGp6bTM5LXFfRVhVYnJPMVNUaC1GaVh2VlZVQTBx?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
