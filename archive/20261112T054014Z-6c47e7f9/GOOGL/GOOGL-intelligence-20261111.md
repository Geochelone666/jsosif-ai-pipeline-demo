# GOOGL Intelligence Report

- ticker: **GOOGL**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/GOOGL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GOOGL/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T06:00:50.547897+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 4, 'ai': 10, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/GOOGL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 293.4500 |
| Return 1D (%) | 2.1122 |
| Return 1W (%) | 1.5644 |
| Return 1M (%) | -16.5529 |
| Return YTD (%) | -6.0636 |
| Return 1Y (%) | 0.9966 |
| Annualized volatility (%) | 33.5977 |
| Beta vs SPY | 1.2870 |
| Max drawdown (%) | -30.6204 |
| Sharpe (rf=0) | 0.1980 |
| Downside deviation (rf=0, %) | 23.6888 |
| Sortino (rf=0) | 0.2809 |
| Historical VaR 95% (1D, %) | 2.9365 |
| Historical ES 95% (1D, %) | 4.7232 |
| Correlation vs SPY | 0.5259 |
| Tracking error vs SPY (%) | 28.8466 |
| P/E (trailing) | 15.32 |
| P/B | 5.47 |
| EV/EBITDA | 18.93 |
| Revenue growth (%) | 24.70 |
| Forward P/E (estimate) | 19.01 |
| Gross margin (%) | 60.86 |
| Operating margin (%) | 33.32 |
| Return on equity (%) | 44.29 |
| Free cash flow yield (%) | -0.03 |
| MA50 | 329.8797 |
| Close vs MA50 (%) | -11.0433 |
| MA200 | 338.5923 |
| Close vs MA200 (%) | -13.3323 |
| RSI (14, Wilder) | 37.9631 |
| MACD (12,26) | -14.6504 |
| MACD signal (9) | -14.0451 |
| MACD histogram | -0.6053 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GOOGL': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 293.4500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.1122 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.5644 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.5529 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -6.0636 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.9966 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.5977 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.6888 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2809 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9365 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.7232 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5259 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.8466 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2870 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.6204 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1980 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 19.0118 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 60.8570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.3210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 44.2860 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -0.0322 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.3238 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 37.9631 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.6053 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -11.0433 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -13.3323 -> Clearly below the moving-average trend level.

## TAILWINDS

### Alphabet (GOOGL) stock is up, what you need to know
- Summary: Alphabet (GOOGL) stock is up, what you need to know
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxObjU0eTV0SzhZTnhLa20zOUtGeUFnZnh2TDc1T09MMXJFcUoya1BPLXVsUm5abjUxdHB5eTY3Z0Z5OVA2NWVuQndzaVRXOTI1X2sxME4ySHJOcXFLSFJtTWZUbWo1YlVGNmlsU3A0Uk05aDdscEk5SjhfTWRsQ2o3dUYyaGtUMFFXNHBrMU1FUnUtc2JicXJFWjBGaWhGR1dGdTBDVG5DcVpoa2c0Nmc?oc=5>

### Alphabet Edged Higher After Revealing a Pair of New TPUs for Agentic AI. A Bigger Challenge for GOOGL Stock Is Its Cash Flow.
- Summary: Alphabet Edged Higher After Revealing a Pair of New TPUs for Agentic AI. A Bigger Challenge for GOOGL Stock Is Its Cash Flow.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPUVJ1OEd0UmpmV0d1djJvUl9VU1lLbHhPTTNvTWZuOXRzYllqcE5WZGtiZE5PNlpzOGRPLVF5TXpBUVM3QWxSWnVTRHBJVk54TjRvTnhsSHU4WHdLeWNmSlNKemFBaDNybGpRajV5dm9vdjlfbllsVFNtMnpYV2czUUlSVkoxblZrWEQ4Z1dEOEJ1REZiR3pnczNMQ0NkSzdfY1E?oc=5>

### Alphabet Stocks Rise 0.34% as Google Lines Up $10 Billion Anthropic Stake Purchase
- Summary: Alphabet Stocks Rise 0.34% as Google Lines Up $10 Billion Anthropic Stake Purchase
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPc1A1VlA1M0tHb2xJN2VYeHJhSlBnNUJ3bzlqV0R5UGZ2VkJEbW5UUjlEMUlnLVk2NnI3bWxmTkdTQWFyOHpMenZTYzg2VlJySV9TR3Nlb2R1M2dqMG1HalZaOHJFMVkxTE5HMGdxaHhmZk9tYTk2UXBwR1VrUUItcHBXYjc3VS1BeFItUG9uMHRKNEh1?oc=5>

### Google Stock News: Cloud Revenue Doubles To $30.7 Billion As Alphabet Gains Favour
- Summary: Google Stock News: Cloud Revenue Doubles To $30.7 Billion As Alphabet Gains Favour
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPa2VlZjQ4bkFSb3JUakZBcm5MM0M3ZVh1TjdwbnBObEVKR0ZCcFJqZ3VKd3pocnJURDVXOFpwWlp4eVdDQkdrTWhPSWdEcDhGNUdpQ2l1cXdxZGRPY2FfaU1WV3E0NVBsYV92cEZvQ2hPVzh0U0ctZ2ZhVTVUODREZzlwWkwzV1l5MFliZWJHby1McnoyeWFqNHRtNHdHcDRTZlhmbGZWdl9mTjhUSVZKN0hkSGFfMEhNMkwyRdIBwgFBVV95cUxPTkFJLVJOOVg5LW5LMGRmd0ROYWJDM19rcHFROXRHWW5XN1Zad25UYUxxYWRYZ0VLLVVvREliVDR3bXlDZDBKWjFDcmtzQk5SdUk0aDdJSXpJUFAwRzJVT19NNEYyLXV2VGtBZEVJTjhreFo2SzBSLXNCM25KU1lydUFFS3l4MlpVdjg0dFVOY2N3NUQ2Uk8yZlAwUUNsSzlVUXdmWURvclBYU2JsNUZZR01mMWJxQ2wyNHZEczZaMmE1QQ?oc=5>

### Alphabet Inc. (GOOGL) Is Part of a Massive AI Spending Race: Can the Investment Deliver Enough Returns?
- Summary: Alphabet’s AI investment may boost returns, signaling growth potential.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOY2N4MGZjMkpaLXRjN0N0RExnNmYtZjZhT0VyQU50cXRhMDF4RnpPM0RGMm1uZlBOVE1CSklDY0xqVWVfYU1UTlY4RHhlczRxMlZOWXIzQV84Ujd3dGtZUFRXV2V3S3ExeGFOZzhRaV9CLVQ1alFueWVndjFZV1ZmcDBFbzRlbV9kUDV5bndvQ1NzRkdIbkF0R3lfOA?oc=5>

### Alphabet Inc. (GOOGL) Is Seeing Its AI Investments Pay Off: Is More Upside Ahead?
- Summary: Alphabet reports AI investments are yielding returns, suggesting potential upside.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNb3o5b0Y4ZHIzSkdldmliN0VBZnpwVkJJY0VIVTVoNHBUUURpTGNvaFRmUEtmQWJmYnFpclpSdWhieFlwVHRJSVBkNVBJNmkyYnJrU2o4eWY0TWFNenVFVzZaZGRJaGVvb3JVemFxOVlETEtHZ2k0TGxWd0RWR3hzUmN0X2V6SVRFTld4dXY1OUwyRXhqZWxN?oc=5>

### Alphabet shares appear to have bottomed. How to play it for a quick rebound
- Summary: Alphabet shares bottomed, suggesting a potential quick rebound. Investors may consider buying.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNVEdUUHd6WEdOZFlVRm5COXRVN0hLSXVyLXdzVTVhMjlibmdqMXJPRlp3WWJHc3NaWDlmcWRrUmJwNmJuNzFJLUt3Vm5PUXYxczM3bE9Calh5SXJRVk5JcGZTQVJZMXNsM1hOeVBHclFwQnM3U3JRS1NlaHZKWUNEaTd0Xzg2eVlYbW9NR3VwRnA0cElsNkJ6SS1PUUVZcnZINEdmbFZaZjJzLUN3R2ZrTw?oc=5>

## HEADWINDS

### What's Going on With Alphabet Stock on Tuesday? - Alphabet (NASDAQ:GOOGL), Alphabet (NASDAQ:GOOG)
- Summary: Alphabet stock activity on Tuesday is uncertain, with mixed market signals.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNeWNyYXFOZlF0WkN3dFhPUkxBMU9FQnZudVBlVUNkQWFFZER6OUNMVzFIUlBTVFF3b3RtbHRZMlppWEROVlhwMHVrck1vNGN6NHV2cXYzU3NHT2o0M0U5Sk5pNHUxTEVjTkFWQVFKSVFhRGZrUllEMGd3NVFneWVNN3ZlV09WaHRUZ05TQmlTTFB3bHkwOGtLNlBfNWcwQXM?oc=5>

## CATALYSTS

### Mapping the Market: Alphabet shares may be ready for a corrective rally
- Summary: Potential short‑term rally for Alphabet shares based on market analysis.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTE9vZGlZeXZzRUlyeHhERkg4UzlnbEFhMHBoZDlLaGN1aS05cWZ5MENHV2xGREkzWjdaMDhyR3JWQTYycjhqVVI3TFkxNldsakNGYUJLNjFobWVSUWpXdzItZ2w4TDFYMVZRMzJTQlNyUF90YkJKQ2FmVzVLdkc?oc=5>

### Alphabet Inc. (GOOGL) Stock Forecasts
- Summary: Alphabet releases stock price forecasts, indicating expected performance trends.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOVml5UUUzQThVeGF6ZVBVcEtuTzNyZlRySnFySkxyR2h0V1oxWGViU0p2M2xVZFJBVThhWDFNOHRMZ0Rsb0lTendHZDl5bndYWGR2WGxmcDBfVDJRMTdMSm5qRUtjWmFVWjBFd1dVUEtSZU5lQnpVcUh3Rkdkc0hldVdUSi12Ql9lRURKRjF3RnZPblNESkc5cTl4NA?oc=5>

### Nvidia and Alphabet Just Agreed to Buy $10 Billion Each of Anthropic Stock at Its IPO Price
- Summary: Alphabet and Nvidia jointly purchase $10B Anthropic stock at IPO price, expanding AI partnership.
- Date: 2026-11-11 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxNZ1NPRnN4V1I4SmpvVG5PU1FQYnUwMDA2Y3pOc1FRclg1cm1hR1hmR042TUFGYzNETTdPVlFJR2hWUVBCeXZMQ3g4bVhYYjB1R3FLdzVQZjNUUW85ZHNKZDBHTlBEc0VEUC1ud0pXR3U2VUZJZ1BfdnMyeVNJWDRTMWY0Yktwd0pWWGh5Qm1qX2hqT0lCMlo1ckI0MnNad0ZmWTdQS2c4ZldwcnE3VGZiczB5QmZPY3NyZWQzZkZ1YzNnLTk1M2Q4SmQwM21ub0NfeWc?oc=5>

### Alphabet Stocks Rise as Google Commits $10 Billion to Anthropic IPO
- Summary: Alphabet shares climb after Google pledges $10B to Anthropic IPO.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxOaDhxbUFQYl9aLWJtTFdOZGhVdy1aU1R1N2tsa0p5RDh6eE9rNnJGWWlPX3EwWEpVRUEtUUdTb21ULUJWcTFFMFIwMnpxbnItdUwtU18wWXJfMjV6bzRRaEJUbzBIdXZnZ1hEbTZsSjBpSm1LZWJXWmhnZXBJamZvWFpyaWxzdG5mcjVVbA?oc=5>

### Will Alphabet stock sustain gains amid aggressive AI investment and expansion?
- Summary: Question on Alphabet stock performance amid AI investment.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPRGMzNFZqYWg0OWxhbi1RaHRXMnBsN0RqQTFIYk1TbGJPVm1uV1JaT3FsdDR1N05KQkw3UmlEcDRBOWRLMWdQc0FVUjQ4aDN3U0k3N3dlNkhqcFl1SDkwREJDMU55b3k3MmxMenB3V28ycVo0Y1ZWcURIdUlvRmNXNzVqQUhOUTREd2FCVVBFUTMyMzl0?oc=5>

## RISKS

### Will AI Replace Google Search? The Risk for Alphabet Stock
- Summary: AI may replace Google Search, posing a long‑term risk to Alphabet.
- Date: 2026-11-11 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPZUlFejdBYzAxSHhOamxWdUdVc0RsWm9rb0Z3TjJ6SkM2OVRuTGhUR3BiazJ6U214cFhUclZ2NjJ2NmZVWkJqcG1SaDNPeW1FbUY4QjFaOUIxVUp3Tk1jZHFnVWh6QTBDbDFveTFET3BYQUhoOG1VT2FfYm02WDdRQTVPbEZNdTV0MGFKSEh3?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GOOGL** | **15.32** | **5.47** | **18.93** | **24.70** | **3,607,674,224,640.00 USD** | **1.00** |
| META | 21.89 | 5.90 | 14.11 | 26.10 | 1,607,659,945,984.00 USD | 0.61 |
| MSFT | 27.82 | 8.23 | 19.15 | 18.80 | 3,869,975,511,040.00 USD | 3.29 |
| AMZN | 21.52 | 4.69 | 16.70 | 12.10 | 2,878,132,977,664.00 USD | 6.85 |

Peers fetched as_of: 2026-11-11; GOOGL reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

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
- Filing date: 2026-10-29
- Revenue (latest available single quarter): 127,577,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 26,468,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMirgFBVV95cUxObjU0eTV0SzhZTnhLa20zOUtGeUFnZnh2TDc1T09MMXJFcUoya1BPLXVsUm5abjUxdHB5eTY3Z0Z5OVA2NWVuQndzaVRXOTI1X2sxME4ySHJOcXFLSFJtTWZUbWo1YlVGNmlsU3A0Uk05aDdscEk5SjhfTWRsQ2o3dUYyaGtUMFFXNHBrMU1FUnUtc2JicXJFWjBGaWhGR1dGdTBDVG5DcVpoa2c0Nmc?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPUVJ1OEd0UmpmV0d1djJvUl9VU1lLbHhPTTNvTWZuOXRzYllqcE5WZGtiZE5PNlpzOGRPLVF5TXpBUVM3QWxSWnVTRHBJVk54TjRvTnhsSHU4WHdLeWNmSlNKemFBaDNybGpRajV5dm9vdjlfbllsVFNtMnpYV2czUUlSVkoxblZrWEQ4Z1dEOEJ1REZiR3pnczNMQ0NkSzdfY1E?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPc1A1VlA1M0tHb2xJN2VYeHJhSlBnNUJ3bzlqV0R5UGZ2VkJEbW5UUjlEMUlnLVk2NnI3bWxmTkdTQWFyOHpMenZTYzg2VlJySV9TR3Nlb2R1M2dqMG1HalZaOHJFMVkxTE5HMGdxaHhmZk9tYTk2UXBwR1VrUUItcHBXYjc3VS1BeFItUG9uMHRKNEh1?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPa2VlZjQ4bkFSb3JUakZBcm5MM0M3ZVh1TjdwbnBObEVKR0ZCcFJqZ3VKd3pocnJURDVXOFpwWlp4eVdDQkdrTWhPSWdEcDhGNUdpQ2l1cXdxZGRPY2FfaU1WV3E0NVBsYV92cEZvQ2hPVzh0U0ctZ2ZhVTVUODREZzlwWkwzV1l5MFliZWJHby1McnoyeWFqNHRtNHdHcDRTZlhmbGZWdl9mTjhUSVZKN0hkSGFfMEhNMkwyRdIBwgFBVV95cUxPTkFJLVJOOVg5LW5LMGRmd0ROYWJDM19rcHFROXRHWW5XN1Zad25UYUxxYWRYZ0VLLVVvREliVDR3bXlDZDBKWjFDcmtzQk5SdUk0aDdJSXpJUFAwRzJVT19NNEYyLXV2VGtBZEVJTjhreFo2SzBSLXNCM25KU1lydUFFS3l4MlpVdjg0dFVOY2N3NUQ2Uk8yZlAwUUNsSzlVUXdmWURvclBYU2JsNUZZR01mMWJxQ2wyNHZEczZaMmE1QQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOY2N4MGZjMkpaLXRjN0N0RExnNmYtZjZhT0VyQU50cXRhMDF4RnpPM0RGMm1uZlBOVE1CSklDY0xqVWVfYU1UTlY4RHhlczRxMlZOWXIzQV84Ujd3dGtZUFRXV2V3S3ExeGFOZzhRaV9CLVQ1alFueWVndjFZV1ZmcDBFbzRlbV9kUDV5bndvQ1NzRkdIbkF0R3lfOA?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNb3o5b0Y4ZHIzSkdldmliN0VBZnpwVkJJY0VIVTVoNHBUUURpTGNvaFRmUEtmQWJmYnFpclpSdWhieFlwVHRJSVBkNVBJNmkyYnJrU2o4eWY0TWFNenVFVzZaZGRJaGVvb3JVemFxOVlETEtHZ2k0TGxWd0RWR3hzUmN0X2V6SVRFTld4dXY1OUwyRXhqZWxN?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNVEdUUHd6WEdOZFlVRm5COXRVN0hLSXVyLXdzVTVhMjlibmdqMXJPRlp3WWJHc3NaWDlmcWRrUmJwNmJuNzFJLUt3Vm5PUXYxczM3bE9Calh5SXJRVk5JcGZTQVJZMXNsM1hOeVBHclFwQnM3U3JRS1NlaHZKWUNEaTd0Xzg2eVlYbW9NR3VwRnA0cElsNkJ6SS1PUUVZcnZINEdmbFZaZjJzLUN3R2ZrTw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNeWNyYXFOZlF0WkN3dFhPUkxBMU9FQnZudVBlVUNkQWFFZER6OUNMVzFIUlBTVFF3b3RtbHRZMlppWEROVlhwMHVrck1vNGN6NHV2cXYzU3NHT2o0M0U5Sk5pNHUxTEVjTkFWQVFKSVFhRGZrUllEMGd3NVFneWVNN3ZlV09WaHRUZ05TQmlTTFB3bHkwOGtLNlBfNWcwQXM?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTE9vZGlZeXZzRUlyeHhERkg4UzlnbEFhMHBoZDlLaGN1aS05cWZ5MENHV2xGREkzWjdaMDhyR3JWQTYycjhqVVI3TFkxNldsakNGYUJLNjFobWVSUWpXdzItZ2w4TDFYMVZRMzJTQlNyUF90YkJKQ2FmVzVLdkc?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVml5UUUzQThVeGF6ZVBVcEtuTzNyZlRySnFySkxyR2h0V1oxWGViU0p2M2xVZFJBVThhWDFNOHRMZ0Rsb0lTendHZDl5bndYWGR2WGxmcDBfVDJRMTdMSm5qRUtjWmFVWjBFd1dVUEtSZU5lQnpVcUh3Rkdkc0hldVdUSi12Ql9lRURKRjF3RnZPblNESkc5cTl4NA?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxNZ1NPRnN4V1I4SmpvVG5PU1FQYnUwMDA2Y3pOc1FRclg1cm1hR1hmR042TUFGYzNETTdPVlFJR2hWUVBCeXZMQ3g4bVhYYjB1R3FLdzVQZjNUUW85ZHNKZDBHTlBEc0VEUC1ud0pXR3U2VUZJZ1BfdnMyeVNJWDRTMWY0Yktwd0pWWGh5Qm1qX2hqT0lCMlo1ckI0MnNad0ZmWTdQS2c4ZldwcnE3VGZiczB5QmZPY3NyZWQzZkZ1YzNnLTk1M2Q4SmQwM21ub0NfeWc?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxOaDhxbUFQYl9aLWJtTFdOZGhVdy1aU1R1N2tsa0p5RDh6eE9rNnJGWWlPX3EwWEpVRUEtUUdTb21ULUJWcTFFMFIwMnpxbnItdUwtU18wWXJfMjV6bzRRaEJUbzBIdXZnZ1hEbTZsSjBpSm1LZWJXWmhnZXBJamZvWFpyaWxzdG5mcjVVbA?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPRGMzNFZqYWg0OWxhbi1RaHRXMnBsN0RqQTFIYk1TbGJPVm1uV1JaT3FsdDR1N05KQkw3UmlEcDRBOWRLMWdQc0FVUjQ4aDN3U0k3N3dlNkhqcFl1SDkwREJDMU55b3k3MmxMenB3V28ycVo0Y1ZWcURIdUlvRmNXNzVqQUhOUTREd2FCVVBFUTMyMzl0?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPZUlFejdBYzAxSHhOamxWdUdVc0RsWm9rb0Z3TjJ6SkM2OVRuTGhUR3BiazJ6U214cFhUclZ2NjJ2NmZVWkJqcG1SaDNPeW1FbUY4QjFaOUIxVUp3Tk1jZHFnVWh6QTBDbDFveTFET3BYQUhoOG1VT2FfYm02WDdRQTVPbEZNdTV0MGFKSEh3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
