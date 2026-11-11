# GOOGL Intelligence Report

- ticker: **GOOGL**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/GOOGL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GOOGL/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:39:48.983231+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 5, 'ai': 10, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261110T055129Z-abd33250/GOOGL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 14 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-11-07

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 287.3800 |
| Return 1D (%) | -0.2672 |
| Return 1W (%) | 2.6247 |
| Return 1M (%) | -18.2790 |
| Return YTD (%) | -8.0067 |
| Return 1Y (%) | -0.6800 |
| Annualized volatility (%) | 33.5345 |
| Beta vs SPY | 1.2841 |
| Max drawdown (%) | -30.6204 |
| Sharpe (rf=0) | 0.1477 |
| Downside deviation (rf=0, %) | 23.6888 |
| Sortino (rf=0) | 0.2090 |
| Historical VaR 95% (1D, %) | 2.9365 |
| Historical ES 95% (1D, %) | 4.7232 |
| Correlation vs SPY | 0.5235 |
| Tracking error vs SPY (%) | 28.8357 |
| P/E (trailing) | 15.01 |
| P/B | 5.36 |
| EV/EBITDA | 18.52 |
| Revenue growth (%) | 24.70 |
| Forward P/E (estimate) | 18.62 |
| Gross margin (%) | 60.86 |
| Operating margin (%) | 31.80 |
| Return on equity (%) | 44.29 |
| Free cash flow yield (%) | -0.03 |
| MA50 | 330.7068 |
| Close vs MA50 (%) | -13.1013 |
| MA200 | 338.7945 |
| Close vs MA200 (%) | -15.1757 |
| RSI (14, Wilder) | 32.5441 |
| MACD (12,26) | -15.6752 |
| MACD signal (9) | -13.8938 |
| MACD histogram | -1.7814 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GOOGL': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 287.3800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.2672 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.6247 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -18.2790 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -8.0067 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -0.6800 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.5345 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.6888 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2090 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9365 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.7232 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5235 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.8357 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2841 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.6204 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1477 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.6186 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 60.8570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.8050 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 44.2860 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -0.0329 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.0068 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 32.5441 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.7814 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -13.1013 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -15.1757 -> Clearly below the moving-average trend level.

## TAILWINDS

### Alphabet (GOOGL) stock is up, what you need to know
- Summary: Alphabet (GOOGL) stock is up, what you need to know
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNd1lGTmRqT1l4cXdzRi1oZHYtNmlxaTR4RmRybjR1M2FwVlVCLUM2ZWplMGl0RmxrTXZ1c2dUU3B6a0dqeTZPQU9FeS1sVWZhMGVjSmJkbW45enI2RjJrWkFWVWJFczhWb0l1S1RjZV9XcHkyOUljM1RZR1VKMHFCUE5iX05mNmJCMVBiUlVIc3poLW1sb1RYMjNtNTJMTzNucWlKN0pkX2hBRGc3dG1ubE9DbVhSeXZSbEdRcTFWR3Q1Vk1WZXNNekFNclo0M00?oc=5>

### Alphabet Stocks Rise 0.34% as Google Lines Up $10 Billion Anthropic Stake Purchase
- Summary: Alphabet Stocks Rise 0.34% as Google Lines Up $10 Billion Anthropic Stake Purchase
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPc1A1VlA1M0tHb2xJN2VYeHJhSlBnNUJ3bzlqV0R5UGZ2VkJEbW5UUjlEMUlnLVk2NnI3bWxmTkdTQWFyOHpMenZTYzg2VlJySV9TR3Nlb2R1M2dqMG1HalZaOHJFMVkxTE5HMGdxaHhmZk9tYTk2UXBwR1VrUUItcHBXYjc3VS1BeFItUG9uMHRKNEh1?oc=5>

### Alphabet Stock Rises as Google Adds Two New TPU Variants
- Summary: Alphabet Stock Rises as Google Adds Two New TPU Variants
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPZ2dldldZVUpzNW9ESXAtRnNmTWZFTGpzWnU3RFhJYmtmVDl0ZVVSWDlXdGxMZWRIZ2xBdW5kNzBSaEFscXJadjZLdFNGZG1RZGtWd0lIM3BUZG1xaWYtRmxudGVMNzgydWdoNWFibHJrNzNteVliazhmTHBRUXJHMm5YSW9qYlA2Y2piTlJRR2NFMTQ5RTBoMWlYdjRhTkQtWVJwZEJNOVYwOGdBQ0Jsb2h4YW5NX1E?oc=5>

### Alphabet stock rises as Google expands AI chip lineup to challenge Nvidia
- Summary: Alphabet stock rises as Google expands AI chip lineup to challenge Nvidia
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxOYW1VVUNLX0RxcFlsYTljOHlybnpxcXpHYldQU25qRjhIZElyTU0xT0xEVjRxQWgwb3hiQ0RFOGMwNGtHNWJpTUlIYmxQTFV1MnZob0d2cDJTZ2F4ODFBd2NZbU1Zc0RnMEM5ZGM2TmNhb1FsRGdsSG0tQWlMdFFINEhRTkVZWHA1NTRBNW44VXdJMUFwaWdETVI4b1V0SEJ6cTFRRkRLMUxXNzZlQ18yTXc0di16VGNNc1kwSWg2aURZOEhmdmJZdzB3?oc=5>

### Alphabet (GOOGL) Expands SpaceX Stake to $69 Billion and Deepens AI Ties
- Summary: Alphabet increases its stake in SpaceX to $69B, strengthening AI collaborations.
- Date: 2026-11-07 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQWFhmSzc3OTBJVU1QbnBIVFpPZURJc3Bna01BaUJLelVkV1RCcF9NQWFSZURkOHFlNlU4R0NDWUVoWXVpUkFnM2RiRElKMER0a3JBekZkVUlvem42SmtEaWg3VjFvOHZEcnI0dTg2TzRMbF92LUx4Y3ZySXFIZ0h1ZjllcWs4c1g0UEFIYW9sRWVkX2VyOUY5OTZjSFROX05p?oc=5>

### Alphabet Inc. (GOOGL) Is Part of a Massive AI Spending Race: Can the Investment Deliver Enough Returns?
- Summary: Alphabet’s AI investment may boost returns, signaling growth potential.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOY2N4MGZjMkpaLXRjN0N0RExnNmYtZjZhT0VyQU50cXRhMDF4RnpPM0RGMm1uZlBOVE1CSklDY0xqVWVfYU1UTlY4RHhlczRxMlZOWXIzQV84Ujd3dGtZUFRXV2V3S3ExeGFOZzhRaV9CLVQ1alFueWVndjFZV1ZmcDBFbzRlbV9kUDV5bndvQ1NzRkdIbkF0R3lfOA?oc=5>

### Alphabet Inc. (GOOGL) Is Seeing Its AI Investments Pay Off: Is More Upside Ahead?
- Summary: Alphabet reports AI investments are yielding returns, suggesting potential upside.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNb3o5b0Y4ZHIzSkdldmliN0VBZnpwVkJJY0VIVTVoNHBUUURpTGNvaFRmUEtmQWJmYnFpclpSdWhieFlwVHRJSVBkNVBJNmkyYnJrU2o4eWY0TWFNenVFVzZaZGRJaGVvb3JVemFxOVlETEtHZ2k0TGxWd0RWR3hzUmN0X2V6SVRFTld4dXY1OUwyRXhqZWxN?oc=5>

### Alphabet (GOOGL) Sees $100.7 Million in Net ETF Buying on Friday
- Summary: Alphabet experienced significant net ETF buying, indicating institutional confidence.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE01bUpuQVo2UXcxTXF0NXhNV2FUTjEyR1RXQ2VmQjIyTHVPOXFkMzEyUUYxWVV0dXFYdlJTYW5weFhDZzQ5M2FXTlpsV1pxbEVSdUlqVy1lOVZIZDZJSWlGcFc1OTRwVGxwQ0xuc3F0RGJhME5OemVsclNFS1lseW8?oc=5>

## HEADWINDS

### Alphabet (GOOGL) Stock Could Trade At A Discount After AI Spending Shock
- Summary: AI spending shock may depress Alphabet's stock valuation.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNY3pIQmk2dWlpcUZxdXdtcldlY3RaelpfNkdkSGdqY1FWTkJmZV9uWUdMZVBkRldwVlRoRmoyMHJnZ0szLTh0dFdxV1Q3OEdlSUZTTmJIRnpsUTZUZ19fUV80cERZYmh0d1AwRENDZlNhenEyT21zOXh1bnNwN1R5bThfNVZHd2VvQU9jR0xveEpvS2dSSWZnaFExSlBIclVoTy00S0Z4WnRlcU9OTHJEZEMyaE1DYVlsZGg5YzZBc01DeHPSAcgBQVVfeXFMT3dKOFdIakx4dGhfMEJfU1haT0h2ZE9jV0hSNXRlUlZHM0FBUThqT2EtTkc0N0FEZFJSbzV1Zmw3bUVjcnlDN1NxdUFySVpBSFdsbnpBM2ppM2UycXhIYjc2bm9jTWtIZGRQcmFXc0JwaDRqYTNUOF9YTUd2a2IzNUVaS0d4Z0FwRmZoeGNVT2JQOTZsSm9uZ25hSmRBd2c0VFIzSDM1U3hHSUFzWVZONVYtYzAxWkgxSi1Senk0Z0lzNE9CMUN6cng?oc=5>

## CATALYSTS

### Alphabet Stocks Rise 3.16% as Google Unveils Two New TPU Systems
- Summary: Alphabet Stocks Rise 3.16% as Google Unveils Two New TPU Systems
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQSlg2SHVJcUZ3cDFCZ1JrVjRjdzktb2tQSXF3MDJYcUhTbzlxWnNSLTNMYVdHRFhqMGw4S0xJNVYwbUctMkVueDViZnBreEVCR1J5VDk0dHhJMURVOE9rdmhveU52b2c3ZVI5akJtclVNUUl4ekhRQ1pZcGxCVEU1RUtSUEplSjJMdjZPWWM1SGNwWUFyWG9QcG5UQ0JvbE4zZnBF?oc=5>

### Mapping the Market: Alphabet shares may be ready for a corrective rally
- Summary: Potential short‑term rally for Alphabet shares based on market analysis.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTE9vZGlZeXZzRUlyeHhERkg4UzlnbEFhMHBoZDlLaGN1aS05cWZ5MENHV2xGREkzWjdaMDhyR3JWQTYycjhqVVI3TFkxNldsakNGYUJLNjFobWVSUWpXdzItZ2w4TDFYMVZRMzJTQlNyUF90YkJKQ2FmVzVLdkc?oc=5>

### Alphabet Inc Class A Stock (GOOGL) Opened Up by 3.44% on Nov 9: Facts Behind the Movement
- Summary: Stock opened up 3.44% on Nov 9.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPcHVHZjNZeF9QZm1oYkNOTkhpb0hFdU5JWGpZX2ZCRndXSlNZZE1LNFNkSTc4Umlyb0NTLXdQNF95ZUxSZDRWV0tQZ1ZLZllZejFhTk10RW96dnYzNWdaM0xkNXhDTnJVVDFBR25RWm9ZYmNIdjJncGhQV1E4aGVtOGNkNGNqaGF5dHZrMA?oc=5>

### Alphabet Inc. (GOOGL) Stock Forecasts
- Summary: Alphabet releases stock price forecasts, indicating expected performance trends.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOVml5UUUzQThVeGF6ZVBVcEtuTzNyZlRySnFySkxyR2h0V1oxWGViU0p2M2xVZFJBVThhWDFNOHRMZ0Rsb0lTendHZDl5bndYWGR2WGxmcDBfVDJRMTdMSm5qRUtjWmFVWjBFd1dVUEtSZU5lQnpVcUh3Rkdkc0hldVdUSi12Ql9lRURKRjF3RnZPblNESkc5cTl4NA?oc=5>

### Alphabet, Meta, and Oracle Are All Teaming Up to Disrupt Nvidia's Biggest Competitive Advantage
- Summary: Alphabet partners with Meta and Oracle to challenge Nvidia’s market edge.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPMXRRR1NYUWpvODRFLUpfdkxYNndaVHBZaWlqczUzVGxwcUZzbHMxcjFnNDBkVUtPS28wTmtfU2UzZ21lekZXbmxDNnNUdWtxb19KOTVHeTBweGdvSGFZVVB2bGhPYWtpeTRydWlTd0U5dFMxRE11a3NtcDBvd2pwbWV2Nl9zWW9WRlRpb3BzMXBJc1NzbkpSeA?oc=5>

## RISKS

### Google Stock Investors Biggest Risk
- Summary: Investors face significant risk with Google stock.
- Date: 2026-11-08 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxOYkFqanltQlJvenA3UkE0ejM2d0sxckRqV1EtbDZEUWVqblZUSlZ0TEZTT2JLWHJSci0ySmR5UGFLRUJPN3NhNDFneEtBcFNLSWJPZHhEU2hYUVRTMXRPS1JpZTVDdXNaOXY1STMzQWRVOS1RdE41OGVzbGRjT3JKQlc5SDk?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GOOGL** | **15.01** | **5.36** | **18.52** | **24.70** | **3,533,049,692,160.00 USD** | **-0.68** |
| META | 21.88 | 6.02 | 14.39 | 26.10 | 1,639,927,119,872.00 USD | 1.87 |
| MSFT | 27.83 | 8.42 | 19.59 | 18.80 | 3,959,349,575,680.00 USD | 6.23 |
| AMZN | 21.90 | 4.77 | 16.98 | 12.10 | 2,928,954,572,800.00 USD | 9.05 |

Peers fetched as_of: 2026-11-10; GOOGL reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-10

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

- https://news.google.com/rss/articles/CBMizwFBVV95cUxNd1lGTmRqT1l4cXdzRi1oZHYtNmlxaTR4RmRybjR1M2FwVlVCLUM2ZWplMGl0RmxrTXZ1c2dUU3B6a0dqeTZPQU9FeS1sVWZhMGVjSmJkbW45enI2RjJrWkFWVWJFczhWb0l1S1RjZV9XcHkyOUljM1RZR1VKMHFCUE5iX05mNmJCMVBiUlVIc3poLW1sb1RYMjNtNTJMTzNucWlKN0pkX2hBRGc3dG1ubE9DbVhSeXZSbEdRcTFWR3Q1Vk1WZXNNekFNclo0M00?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPc1A1VlA1M0tHb2xJN2VYeHJhSlBnNUJ3bzlqV0R5UGZ2VkJEbW5UUjlEMUlnLVk2NnI3bWxmTkdTQWFyOHpMenZTYzg2VlJySV9TR3Nlb2R1M2dqMG1HalZaOHJFMVkxTE5HMGdxaHhmZk9tYTk2UXBwR1VrUUItcHBXYjc3VS1BeFItUG9uMHRKNEh1?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPZ2dldldZVUpzNW9ESXAtRnNmTWZFTGpzWnU3RFhJYmtmVDl0ZVVSWDlXdGxMZWRIZ2xBdW5kNzBSaEFscXJadjZLdFNGZG1RZGtWd0lIM3BUZG1xaWYtRmxudGVMNzgydWdoNWFibHJrNzNteVliazhmTHBRUXJHMm5YSW9qYlA2Y2piTlJRR2NFMTQ5RTBoMWlYdjRhTkQtWVJwZEJNOVYwOGdBQ0Jsb2h4YW5NX1E?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxOYW1VVUNLX0RxcFlsYTljOHlybnpxcXpHYldQU25qRjhIZElyTU0xT0xEVjRxQWgwb3hiQ0RFOGMwNGtHNWJpTUlIYmxQTFV1MnZob0d2cDJTZ2F4ODFBd2NZbU1Zc0RnMEM5ZGM2TmNhb1FsRGdsSG0tQWlMdFFINEhRTkVZWHA1NTRBNW44VXdJMUFwaWdETVI4b1V0SEJ6cTFRRkRLMUxXNzZlQ18yTXc0di16VGNNc1kwSWg2aURZOEhmdmJZdzB3?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQWFhmSzc3OTBJVU1QbnBIVFpPZURJc3Bna01BaUJLelVkV1RCcF9NQWFSZURkOHFlNlU4R0NDWUVoWXVpUkFnM2RiRElKMER0a3JBekZkVUlvem42SmtEaWg3VjFvOHZEcnI0dTg2TzRMbF92LUx4Y3ZySXFIZ0h1ZjllcWs4c1g0UEFIYW9sRWVkX2VyOUY5OTZjSFROX05p?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOY2N4MGZjMkpaLXRjN0N0RExnNmYtZjZhT0VyQU50cXRhMDF4RnpPM0RGMm1uZlBOVE1CSklDY0xqVWVfYU1UTlY4RHhlczRxMlZOWXIzQV84Ujd3dGtZUFRXV2V3S3ExeGFOZzhRaV9CLVQ1alFueWVndjFZV1ZmcDBFbzRlbV9kUDV5bndvQ1NzRkdIbkF0R3lfOA?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNb3o5b0Y4ZHIzSkdldmliN0VBZnpwVkJJY0VIVTVoNHBUUURpTGNvaFRmUEtmQWJmYnFpclpSdWhieFlwVHRJSVBkNVBJNmkyYnJrU2o4eWY0TWFNenVFVzZaZGRJaGVvb3JVemFxOVlETEtHZ2k0TGxWd0RWR3hzUmN0X2V6SVRFTld4dXY1OUwyRXhqZWxN?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE01bUpuQVo2UXcxTXF0NXhNV2FUTjEyR1RXQ2VmQjIyTHVPOXFkMzEyUUYxWVV0dXFYdlJTYW5weFhDZzQ5M2FXTlpsV1pxbEVSdUlqVy1lOVZIZDZJSWlGcFc1OTRwVGxwQ0xuc3F0RGJhME5OemVsclNFS1lseW8?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNY3pIQmk2dWlpcUZxdXdtcldlY3RaelpfNkdkSGdqY1FWTkJmZV9uWUdMZVBkRldwVlRoRmoyMHJnZ0szLTh0dFdxV1Q3OEdlSUZTTmJIRnpsUTZUZ19fUV80cERZYmh0d1AwRENDZlNhenEyT21zOXh1bnNwN1R5bThfNVZHd2VvQU9jR0xveEpvS2dSSWZnaFExSlBIclVoTy00S0Z4WnRlcU9OTHJEZEMyaE1DYVlsZGg5YzZBc01DeHPSAcgBQVVfeXFMT3dKOFdIakx4dGhfMEJfU1haT0h2ZE9jV0hSNXRlUlZHM0FBUThqT2EtTkc0N0FEZFJSbzV1Zmw3bUVjcnlDN1NxdUFySVpBSFdsbnpBM2ppM2UycXhIYjc2bm9jTWtIZGRQcmFXc0JwaDRqYTNUOF9YTUd2a2IzNUVaS0d4Z0FwRmZoeGNVT2JQOTZsSm9uZ25hSmRBd2c0VFIzSDM1U3hHSUFzWVZONVYtYzAxWkgxSi1Senk0Z0lzNE9CMUN6cng?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQSlg2SHVJcUZ3cDFCZ1JrVjRjdzktb2tQSXF3MDJYcUhTbzlxWnNSLTNMYVdHRFhqMGw4S0xJNVYwbUctMkVueDViZnBreEVCR1J5VDk0dHhJMURVOE9rdmhveU52b2c3ZVI5akJtclVNUUl4ekhRQ1pZcGxCVEU1RUtSUEplSjJMdjZPWWM1SGNwWUFyWG9QcG5UQ0JvbE4zZnBF?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTE9vZGlZeXZzRUlyeHhERkg4UzlnbEFhMHBoZDlLaGN1aS05cWZ5MENHV2xGREkzWjdaMDhyR3JWQTYycjhqVVI3TFkxNldsakNGYUJLNjFobWVSUWpXdzItZ2w4TDFYMVZRMzJTQlNyUF90YkJKQ2FmVzVLdkc?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPcHVHZjNZeF9QZm1oYkNOTkhpb0hFdU5JWGpZX2ZCRndXSlNZZE1LNFNkSTc4Umlyb0NTLXdQNF95ZUxSZDRWV0tQZ1ZLZllZejFhTk10RW96dnYzNWdaM0xkNXhDTnJVVDFBR25RWm9ZYmNIdjJncGhQV1E4aGVtOGNkNGNqaGF5dHZrMA?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVml5UUUzQThVeGF6ZVBVcEtuTzNyZlRySnFySkxyR2h0V1oxWGViU0p2M2xVZFJBVThhWDFNOHRMZ0Rsb0lTendHZDl5bndYWGR2WGxmcDBfVDJRMTdMSm5qRUtjWmFVWjBFd1dVUEtSZU5lQnpVcUh3Rkdkc0hldVdUSi12Ql9lRURKRjF3RnZPblNESkc5cTl4NA?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPMXRRR1NYUWpvODRFLUpfdkxYNndaVHBZaWlqczUzVGxwcUZzbHMxcjFnNDBkVUtPS28wTmtfU2UzZ21lekZXbmxDNnNUdWtxb19KOTVHeTBweGdvSGFZVVB2bGhPYWtpeTRydWlTd0U5dFMxRE11a3NtcDBvd2pwbWV2Nl9zWW9WRlRpb3BzMXBJc1NzbkpSeA?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxOYkFqanltQlJvenA3UkE0ejM2d0sxckRqV1EtbDZEUWVqblZUSlZ0TEZTT2JLWHJSci0ySmR5UGFLRUJPN3NhNDFneEtBcFNLSWJPZHhEU2hYUVRTMXRPS1JpZTVDdXNaOXY1STMzQWRVOS1RdE41OGVzbGRjT3JKQlc5SDk?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
