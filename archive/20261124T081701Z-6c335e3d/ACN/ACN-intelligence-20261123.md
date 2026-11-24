# ACN Intelligence Report

- ticker: **ACN**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/ACN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ACN/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:28:10.636217+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 1, 'ai': 9, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261123T053847Z-45053549/ACN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'short_term_price_move_in_structural_risks': 2}
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 9 named publishers; 0 exact duplicates; 15 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 222.2900 |
| Return 1D (%) | 0.5064 |
| Return 1W (%) | -10.2584 |
| Return 1M (%) | -10.8594 |
| Return YTD (%) | -14.7631 |
| Return 1Y (%) | -9.1957 |
| Annualized volatility (%) | 50.3172 |
| Beta vs SPY | 0.0117 |
| Max drawdown (%) | -56.5068 |
| Sharpe (rf=0) | 0.1259 |
| Downside deviation (rf=0, %) | 35.3560 |
| Sortino (rf=0) | 0.1792 |
| Historical VaR 95% (1D, %) | 4.7187 |
| Historical ES 95% (1D, %) | 6.8166 |
| Correlation vs SPY | 0.0035 |
| Tracking error vs SPY (%) | 52.4484 |
| P/E (trailing) | 16.39 |
| P/B | 4.19 |
| EV/EBITDA | 9.95 |
| Revenue growth (%) | 6.20 |
| Forward P/E (estimate) | 13.97 |
| Gross margin (%) | 32.05 |
| Operating margin (%) | 16.42 |
| Return on equity (%) | 26.02 |
| Free cash flow yield (%) | 8.14 |
| MA50 | 221.6460 |
| Close vs MA50 (%) | 0.2906 |
| MA200 | 187.0971 |
| Close vs MA200 (%) | 18.8100 |
| RSI (14, Wilder) | 40.2032 |
| MACD (12,26) | -0.2252 |
| MACD signal (9) | 6.0459 |
| MACD histogram | -6.2711 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ACN': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 222.2900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.5064 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -10.2584 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -10.8594 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -14.7631 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -9.1957 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 50.3172 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 35.3560 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1792 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.7187 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.8166 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0035 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 52.4484 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0117 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -56.5068 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1259 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.9703 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.0500 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.4190 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.0250 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.1365 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.3931 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 40.2032 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -6.2711 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.2906 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 18.8100 -> Clearly above the moving-average trend level.

## TAILWINDS

### Accenture (NYSE:ACN): A Quality Investing Candidate With Exceptional ROIC and Cash Flow
- Summary: Accenture highlighted as a strong investment due to high ROIC and cash flow.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNWUswUHdQaC1uWlZ2NkZISUVkNDk1cWZIdmw4MVRrTnI5QWE3Z2t2d3IwQUdtQXpRNC04WUhlTm5tdW9lQzRRVFNHY3VQbE5Qby0teU5WbGQ4VHlhX3JvNDZhMGpwM2V6d3FaSlFLU0VCZ0dyWnI4cVNhTGpOczVBQmJzaDA2Tnlxd2ZOZkZOM0lHdXk2UDJ4NTdXNzJSdDF6YlFCUTZFSDZkYzROM2VvV1I0blpFajVGcVRqOGYtV0pHSzRSelNROUpsRjJWVE0?oc=5>

### Accenture (ACN) Gains as AI Disruption Fears Eased
- Summary: Shares rise as concerns over AI disruption subside, boosting investor confidence.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOUmpYUk9pS0Q0UkFUN19PdzJZZG9BS2xZX2FUdmtnQ0lOS3BIY21WMTJ3Z0M0bDdPSENGbzJXYTFJYk1sQm1WLUdrM2lnekxYVmUxNnIxNWgzUktZT0lEWE9DUlhGMkxENEppRnBmdWU1c05tTl9tbmZDNVRyOHcwZE8zSERQX3BIMk51bFFmcC05YlF0Vk91X1FickZHQQ?oc=5>

### Why Is Accenture (NYSE:ACN) Stock Up 3% in US Trading After Two Sharp Drops on AI Disruption Fears?
- Summary: Accenture shares rose 3% after a brief dip amid AI disruption concerns, reflecting investor optimism.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxPSUZqRUFtMTB5VmRUZG5OREpIT0JvOWtNc05uTHcxLU5vekc2NWlXU0Nubk84aVBVeTZpdUpWdmFxNS1hT01faDVSTktITE1mWm1jd2pwTFZrNDNkcDZmeWFiZjZhTjlTanVZUGdxQnBIM0JZQWRDa1FtWDl2emYzQnJfdG5MaG1VczZTZ2VhUTk0ZGZoMGZuV2tlbHI1RkU1Y3hsb3FaZ1F0aENDNkFsbGl5UWUzY1VubmRrWWFpMFpXeVNzXzM4ZDdVREowQQ?oc=5>

## HEADWINDS

### Accenture PLC (ACN) Shares Fall 3.4% -- What GF Score of 95 Tells Investors
- Summary: Accenture PLC (ACN) Shares Fall 3.4% -- What GF Score of 95 Tells Investors
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNRFZXNlBUZG1IRXg3b3VLQUd5dm5IT3dDTkYxUDVBX0VoUGRLNUVkSUY4US03WWlybGNNYTY2ZGN3LWNyR0g5ak41QkR0bldQS0dIcmJYRDRSVzVoRUlWaUFXaDNpVUF6UjlrN0haZWQtNE5DQ1FPWVFpQ3VXaGk5QUFJQUFVbkdLR1drOXZUVWtzcG1qcW1zZ293eWlKZ0tqLVVwenBBR3RPX1U?oc=5>

### Accenture (ACN) Stock May Trade At A Discount On Fresh AI Outsourcing News
- Summary: Potential discount on ACN shares due to new AI outsourcing news.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQQUNjcFJ4bU91ZlFkTDQ4cmI4dEs2X0lvaGY0cDFOcmFSMzFleWlwRThZU2pfZVVfd2VQa21CdDIyOS1XQkVNZ2VjOFBNNjJoaG5WM2lPZGFOaVlkdGR5LWYtMkNoY1ZJMVNDbUUzQWpHczEtQ2loQnhDWl9xU0kwNm92Y0pSa3RNaUNnZm40VW15VkdiS2FhVkln?oc=5>

### Accenture PLC Stock (ACN) Moved Down by 3.64% on Nov 18: What Signal Does It Send?
- Summary: Shares dropped 3.64% on Nov 18, raising questions about future performance.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQenVUZi02eS1Dc2s0RzdvMGNEeW5vT0tWcVhaRDNOc205bFVENXo4MmFSZk9jQXhZWXc5X3U0bFQ3LXliS1hORXhPLVZuZ1loWGlNcTZDWWpkWVhUQzFvWWptM2FkVzdLVWRQbGpPV3E4b0JNZC15N2JOdmlLQzJBWjBLZFExY1hWOFE?oc=5>

### Accenture PLC Stock (ACN) Moved Down by 4.35% on Nov 19: A Full Analysis
- Summary: Shares fell 4.35% on Nov 19, reflecting market concerns.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQUzhTOWMwWEF5cTRCZTJJVWloTWJhWEU2QzZpUFdtWEJTTkFnTy1LUnlWcV9iY3kzdXRlRUlnbU1rNjZ2Z1FfSVNRaGlacVB6VW1kVFpKY1lnQ1B1VDlEdktzX1BGWmtWaXJWWnNQeDBuU2lJVGxFZUFYWHRqWkF6S0owRndXdF9HZlE?oc=5>

### Accenture Falls as Investors Weigh Consulting Demand and a Weak Tech Backdrop
- Summary: Stock drops amid doubts about consulting demand and a weak tech environment.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNQldsS1lMdEYzVFVrOGVGVmNfOXh3cmF4WmdTeFlsVThYcHNaVDdkSzJsaUxJTnZLSGxrMFpCZmFpT0I1Zm1lYlhIbUJobWdaQmp4YUxEMEM2TFRST01IMU5IYkFsM0kyWUlFU1htUUpaOGdoQnYxMzAtQ3BZeTZ4SVJ5bWFTcFhJcUpMTEtpb19jWTlwa1ZNOS1QRzhzS2dkNlpKQ1ltNzhISy10Nlk0?oc=5>

## CATALYSTS

No items in this run

## RISKS

### Accenture (ACN) Registers a Bigger Fall Than the Market: Important Facts to Note
- Summary: Accenture shares fell more than the market, indicating potential valuation concerns.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQVndURE9QTl9jVmJGLVNtNTY4OHdHM1hQTGwxelBQN1V6QVJjOUszeVlGcnBKZEZaMk9Id1pkYldhUW5lcWs5bm01VDJiTEVCdXhEdmpJWUNETDBMS3Z4VXBuSlM3eExFZ3M0WnowY2JuY0gwXzd5Z0pmTkRHOXYxNENJd1Z1bFBfcXFNZnhjS2NwcXVZSEtDQnE0TzBTSS0ybHc?oc=5>

### Accenture PLC Stock (ACN) Closed Down by 3.40% on Nov 17: A Full Analysis
- Summary: Shares closed 3.40% lower on Nov 17, reflecting recent market pressure.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQMUI3RDNCY2tnZHkwSFhaU3J4M2o0b3VDVzhtaGJqMS1wWEN5Umt2ekpVZDQ2NlVrVDlLaWQ1X05EcVd2d3FTVmh1aE5Qd29xdThpeVJ6aW9BM3ZGNkQ1dkxZbkZvZGFmM1hUaFM1X0RPZ18tUm43ZjByMWp3cmpWcWRZbE4tTmlVcVE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ACN** | **16.39** | **4.19** | **9.95** | **6.20** | **131,315,032,064.00 USD** | **-9.20** |
| IBM | 19.88 | 6.20 | 16.65 | 4.70 | 220,213,149,696.00 USD | -19.52 |
| CTSH | 10.69 | 1.78 | 6.52 | 4.60 | 26,182,572,032.00 USD | -21.11 |
| INFY | 14.94 | 9.49 | 19.39 | 1.40 | 49,009,557,504.00 USD | -30.16 |

Peers fetched as_of: 2026-11-23; ACN reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-01
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-16
- Revenue (latest available single quarter): 18,679,110,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- Net income (latest available single quarter): 1,991,267,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- SEC link: https://www.sec.gov/Archives/edgar/data/1467373/000146737326000049/acn-20260831.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMizwFBVV95cUxNWUswUHdQaC1uWlZ2NkZISUVkNDk1cWZIdmw4MVRrTnI5QWE3Z2t2d3IwQUdtQXpRNC04WUhlTm5tdW9lQzRRVFNHY3VQbE5Qby0teU5WbGQ4VHlhX3JvNDZhMGpwM2V6d3FaSlFLU0VCZ0dyWnI4cVNhTGpOczVBQmJzaDA2Tnlxd2ZOZkZOM0lHdXk2UDJ4NTdXNzJSdDF6YlFCUTZFSDZkYzROM2VvV1I0blpFajVGcVRqOGYtV0pHSzRSelNROUpsRjJWVE0?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOUmpYUk9pS0Q0UkFUN19PdzJZZG9BS2xZX2FUdmtnQ0lOS3BIY21WMTJ3Z0M0bDdPSENGbzJXYTFJYk1sQm1WLUdrM2lnekxYVmUxNnIxNWgzUktZT0lEWE9DUlhGMkxENEppRnBmdWU1c05tTl9tbmZDNVRyOHcwZE8zSERQX3BIMk51bFFmcC05YlF0Vk91X1FickZHQQ?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxPSUZqRUFtMTB5VmRUZG5OREpIT0JvOWtNc05uTHcxLU5vekc2NWlXU0Nubk84aVBVeTZpdUpWdmFxNS1hT01faDVSTktITE1mWm1jd2pwTFZrNDNkcDZmeWFiZjZhTjlTanVZUGdxQnBIM0JZQWRDa1FtWDl2emYzQnJfdG5MaG1VczZTZ2VhUTk0ZGZoMGZuV2tlbHI1RkU1Y3hsb3FaZ1F0aENDNkFsbGl5UWUzY1VubmRrWWFpMFpXeVNzXzM4ZDdVREowQQ?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNRFZXNlBUZG1IRXg3b3VLQUd5dm5IT3dDTkYxUDVBX0VoUGRLNUVkSUY4US03WWlybGNNYTY2ZGN3LWNyR0g5ak41QkR0bldQS0dIcmJYRDRSVzVoRUlWaUFXaDNpVUF6UjlrN0haZWQtNE5DQ1FPWVFpQ3VXaGk5QUFJQUFVbkdLR1drOXZUVWtzcG1qcW1zZ293eWlKZ0tqLVVwenBBR3RPX1U?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQQUNjcFJ4bU91ZlFkTDQ4cmI4dEs2X0lvaGY0cDFOcmFSMzFleWlwRThZU2pfZVVfd2VQa21CdDIyOS1XQkVNZ2VjOFBNNjJoaG5WM2lPZGFOaVlkdGR5LWYtMkNoY1ZJMVNDbUUzQWpHczEtQ2loQnhDWl9xU0kwNm92Y0pSa3RNaUNnZm40VW15VkdiS2FhVkln?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQenVUZi02eS1Dc2s0RzdvMGNEeW5vT0tWcVhaRDNOc205bFVENXo4MmFSZk9jQXhZWXc5X3U0bFQ3LXliS1hORXhPLVZuZ1loWGlNcTZDWWpkWVhUQzFvWWptM2FkVzdLVWRQbGpPV3E4b0JNZC15N2JOdmlLQzJBWjBLZFExY1hWOFE?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQUzhTOWMwWEF5cTRCZTJJVWloTWJhWEU2QzZpUFdtWEJTTkFnTy1LUnlWcV9iY3kzdXRlRUlnbU1rNjZ2Z1FfSVNRaGlacVB6VW1kVFpKY1lnQ1B1VDlEdktzX1BGWmtWaXJWWnNQeDBuU2lJVGxFZUFYWHRqWkF6S0owRndXdF9HZlE?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNQldsS1lMdEYzVFVrOGVGVmNfOXh3cmF4WmdTeFlsVThYcHNaVDdkSzJsaUxJTnZLSGxrMFpCZmFpT0I1Zm1lYlhIbUJobWdaQmp4YUxEMEM2TFRST01IMU5IYkFsM0kyWUlFU1htUUpaOGdoQnYxMzAtQ3BZeTZ4SVJ5bWFTcFhJcUpMTEtpb19jWTlwa1ZNOS1QRzhzS2dkNlpKQ1ltNzhISy10Nlk0?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQVndURE9QTl9jVmJGLVNtNTY4OHdHM1hQTGwxelBQN1V6QVJjOUszeVlGcnBKZEZaMk9Id1pkYldhUW5lcWs5bm01VDJiTEVCdXhEdmpJWUNETDBMS3Z4VXBuSlM3eExFZ3M0WnowY2JuY0gwXzd5Z0pmTkRHOXYxNENJd1Z1bFBfcXFNZnhjS2NwcXVZSEtDQnE0TzBTSS0ybHc?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQMUI3RDNCY2tnZHkwSFhaU3J4M2o0b3VDVzhtaGJqMS1wWEN5Umt2ekpVZDQ2NlVrVDlLaWQ1X05EcVd2d3FTVmh1aE5Qd29xdThpeVJ6aW9BM3ZGNkQ1dkxZbkZvZGFmM1hUaFM1X0RPZ18tUm43ZjByMWp3cmpWcWRZbE4tTmlVcVE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
