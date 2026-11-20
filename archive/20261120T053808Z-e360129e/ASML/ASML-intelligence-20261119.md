# ASML Intelligence Report

- ticker: **ASML**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/ASML/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ASML/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T06:02:29.086638+00:00**
- AI status: **Partial: 1 headline remains unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 5, 'ai': 10, 'unknown': 1, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261119T054856Z-9eb86811/ASML** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 15 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1356.2000 |
| Return 1D (%) | -2.8002 |
| Return 1W (%) | -9.4127 |
| Return 1M (%) | -17.5537 |
| Return YTD (%) | 27.5412 |
| Return 1Y (%) | 31.2877 |
| Annualized volatility (%) | 49.0121 |
| Beta vs SPY | 2.2810 |
| Max drawdown (%) | -31.6518 |
| Sharpe (rf=0) | 0.8021 |
| Downside deviation (rf=0, %) | 33.4933 |
| Sortino (rf=0) | 1.1737 |
| Historical VaR 95% (1D, %) | 5.0034 |
| Historical ES 95% (1D, %) | 6.5779 |
| Correlation vs SPY | 0.6469 |
| Tracking error vs SPY (%) | 41.4009 |
| P/E (trailing) | 33.37 |
| P/B | 1164.50 |
| EV/EBITDA | 1783.18 |
| Revenue growth (%) | 55.20 |
| Forward P/E (estimate) | 21.39 |
| Gross margin (%) | 54.34 |
| Operating margin (%) | 38.55 |
| Return on equity (%) | 65.64 |
| Free cash flow yield (%) | N/A |
| MA50 | 1631.9461 |
| Close vs MA50 (%) | -16.8968 |
| MA200 | 1597.9400 |
| Close vs MA200 (%) | -15.1282 |
| RSI (14, Wilder) | 33.7899 |
| MACD (12,26) | -71.4693 |
| MACD signal (9) | -62.0869 |
| MACD histogram | -9.3824 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ASML': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1356.2000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.8002 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -9.4127 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -17.5537 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 27.5412 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 31.2877 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 49.0121 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 33.4933 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1737 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.5779 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6469 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 41.4009 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.2810 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -31.6518 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8021 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.3914 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3370 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.5520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 65.6360 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 33.3711 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 33.7899 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -9.3824 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -16.8968 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -15.1282 -> Clearly below the moving-average trend level.

## TAILWINDS

### ASML Holding rises 2.17% in Thursday's session
- Summary: ASML Holding rises 2.17% in Thursday's session
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxQU1U0UTlvTkdwbzFYYTdkYWRFbEJUNG9haEdJWjFOamQ1RE9HTG1LZklTeHQwRzkyQUtnb2Vxc0hQRFd2S3dqNGJQMnZ1eWlqdzVUZlU4eUVHNHR3RUNmR1hzeU5IWWtiRnIzVVk0TmlmZTFwWVQ5Z3BzTm9nYVg3a0lJZDc?oc=5>

### ASML emerges as a top AI stock pick as volatility hits ahead of the Anthropic IPO
- Summary: ASML emerges as a top AI stock pick as volatility hits ahead of the Anthropic IPO
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMia0FVX3lxTFA5SzAtRE1SMDIyUEh3QjI3VEJWMmEza0xyRFYzQWdqRXRzcnFoQWpqRXltVnZKYW80aDN4WTdRNlZLZDhpTjhxaFhEQW1FMXd5RnZMeWJHTGVKZHRuSmM1NEJPWk1XVUhSaTJ3?oc=5>

### ASML Holding N.V. : Gets a Buy rating from Bernstein
- Summary: Bernstein upgrades ASML to Buy, signaling positive outlook.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPRXVRS2duSzVqMXNJdHNNNzJUVVlUdzFuQkhHQzYxdWVLTGFqYnJzSDE2YzR5cnRTYkY4VXNlVGJ3M3FUemJfanFNVGo2WG9uT19mUndubU5GV3N4OFcta21GeVBQSTVKeHFMU2Z3M2Z0Y3kwQVhYX3UxVWlpN0g4QW9OMXpBRHZqMGZBMGllSFpQQS1POFZsREg3QnBMb0I1LVZnZA?oc=5>

## HEADWINDS

### ASML Stocks Fall 2.72% as New US Rule Tightens the Chip Supply Chain It Serves
- Summary: ASML Stocks Fall 2.72% as New US Rule Tightens the Chip Supply Chain It Serves
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOUl9OTjV3ak52UDhNeENtTG9GOElJUF9fWWNtZ0dIN1Bzb0R5QUt4WG5tZHEwbHJmM0ZvQnVaWktvaGw5OW9YUFhvSGxodC1yM1B5RVRWNXFNSGJmT2lINGFHazkwSy1zWl9ya2FtVkJmbGJwSThnTmZCeWFraDAwdXE0TG45Q0lucGc?oc=5>

### ASML slides as broader chip selloff appears to pressure shares
- Summary: ASML slides as broader chip selloff appears to pressure shares
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxON3V1T0l4QmtndUVSMHM1RzJWalliN3BIaDlFTExiQnpELUI4Y2Yyc2UzVk9XbnczcGx3RzFjN3BPN3dhTWotOG42MWQybE5iQW5NTEE3Y19ZTzFBbV9weW9tcnRocmdEdWlfY0RlT0M5Q1R3SlRwbmRxWWhFZUZQcmVLS1VUbFNnUVpaV0EzamJUZjhPU3pvd0o3WQ?oc=5>

### Why is ASML stock sliding today?
- Summary: Investors question the factors behind ASML's recent share price decline.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPUjUxQVlLLUhQRlhhbDhiazlZempiRGR3ZnNRT2JmWmdsTG9sUWpHN1UyS29rRHVEVGNQUjR4eEpGZ3BpcnFBVmV6Vnp3RDNuS0Y4ZXZCWGVRVEV4Y24wRUtyYmhWemVsRXFRa1JRdVBaRTNYNktHWi1zaVVSTTdSTTFkMUpPUDRnSExpM3hnRDh0bnluZDR2UQ?oc=5>

### ASML Plunged 17% Lower Over 3 Months: This Wall Street Desk Expects 88% Gains Over the Next 12
- Summary: ASML shares fell 17% over three months, reflecting short‑term negative market pressure.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxNUmtfcVVoWkt3b3VrbzdVM1g2STlWM2lpeXp0Vm5BY2ZsOG51S3dXbVVYZ242S2lnS0ludXFjQzduenc2OHM0alFmY1Rxb3EzRDh5UHpHbU1Ea1oyc0JNVTRreTl2MWxjWDlVamdzRk9mZnZCZ1BNNnl6WTJUTUdLR3lPUGpFLU5NWEtQcFI0bmxLOWliWGd1bF9fWEZ6QWVwdHV3V29TbndCSWpqeTJCVG5qaU95QUI1R0JlM0JmaTVqVXQxZ3FhLUlBLVlxWG95?oc=5>

### ASML Holding NV Stock (ASML) Moved Down by 3.02% on Nov 17: What Investors Need To Know
- Summary: ASML shares fell 3.02% on Nov 17, prompting investors to assess reasons for the decline.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOaHFra2Y3LUFrdVY3ejF4TnptNmhHOVFXV0Z0c1RYQ0s2eXlWYmJ1YzZfTG9aeFNyN3ZoVHhZZGZmdjhwaVZ3dTNGY3dpWUNWbEJGd1RQNklnVVE3LUJ3TGVubzIwZWxfNTdhUE1CbXAxd21lZ3JIR1I2ZE1XanRxemx1anlfU0xFN2VR?oc=5>

### ASML Holding NV Stock (ASML) Opened Down by 3.69% on Nov 16: Key Drivers Unveiled
- Summary: ASML stock opened 3.69% lower on Nov 16, indicating short‑term negative market reaction.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQR2xLMTJ3cHZWbUtmUWdBdEplc3ZqeEJzR0h1TWhLRTZEUzVSQ0ZzN0hObmRtX0ZJdUgzTFJIUHJZLVJ6VFU2U2k5VkhWZllCNXN2Mm1TOXFaam1Yb3BVSHh4NUNQcmo1QUxDcW1wcnJaUHdJVmlIMWVVWHd6b3VuVm0wUENSMnoxTWZj?oc=5>

### Can ASML Holding (ENXTAM:ASML) Stay Cheap Enough on Cash Flow?
- Summary: Questioning ASML's ability to maintain low cash flow costs amid rising expenses.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNN3J5SkhiTk5hdmRyUTVuREItYmxSMEszWWFCS29RTHVWZ001WTlaa2tUZ1V2c0hoVDBQNTROYTBMU2dRQWpSRzVnTXVzVnlLclZ6VnNEbDJuUUtjYlNtWWM2SkhfYVo3ZXpBSk0tS1VjTjRfUU5iZldJUl9rQ3lMMTBGbzVUZUJEUG9CV2xlSExYQ3FFRkhkOGNwLWZLdjBWN1VFSHN0NkdkYzV3cFo0NkNEbVdtWTYxQ2F2Ry1EOUpqcVVwekJBeWJJZGdpQ0tmcmdGZm9n0gHbAUFVX3lxTE1yM2NwbDYySThYQzJzTHNvYVJWbkY4dnFoZUNaVmZ1bTRlY2JCRzkyeEU0TS12RngzejdzR0I1S1FvY3JMYnBIU3E0UjlGUUhwY0ZmWVJxbXd6QWI0bTdvOVI4cjJGVFdqX043MzdhTThBX1E1NDlnVmtBQmIzdGU2bGxSRWRSRnBZME1nVlNCZFZ4cjB2M085d1VhYWljYmhoU3RXb2xsdWhmb2JLSjJVN0JOX0NzbXBSMlo4QXlNMzIzRWpmTTdBZkNqRlczTjdFNzNJRVFzMWdnVQ?oc=5>

## CATALYSTS

### ASML reports transactions under its current share buyback program
- Summary: ASML reports transactions under its current share buyback program
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNYlFVSlRnVHh5eFFNUllxdmVOUWQ4T0NaTFZUYnMzQjRiWmFWdi04N0JDSFNXOGJRaGhhd0JvT2UwblZGcndaS04xY3BqNFBWc2twZnNKQlVKMnJLSjNNbEF6MGFsQWhmcDAzcEF3RTNLbGNoRU5XRkdRc215Zm9xVzJsMTBlOXRDY2tXeUJhbGw5ck4weXludWo5NWE1bFZiMENFbmdVUQ?oc=5>

### ASML Stock Price Prediction: ASML lifts guidance again as the stock tests lower support
- Summary: ASML raises guidance, indicating positive outlook.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQOWY1cDlwVWExLTUwUHFTUXpTa0ZUVDMtRkxVaExqdHNWY0FZMDByWXdVaXpUTV9pTmdqN3d1S2VMTUtmR0VvRWxnWENxRnE2TUhfQktYNm5LNlFaUUZzSGlvZHVYb1FYSDRveE5YTE04S3ZmSy1KMjZHR1ZhZzF2cTdLd05aN1ZQd1dKamh5Y2FnaXk4QUpR?oc=5>

### Why Ken Fisher Keeps Adding to ASML Holding (ASML) While Its Order Book Is Sold Out
- Summary: Analyst Ken Fisher increases ASML holdings amid sold-out order book, signaling confidence in future demand.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOVHExZXNEaXpjenZKdzNmak4wTXloVTNSNFdvODVXZ2h1ZWNnSHJTYXFLOGRON1ZhcUZkQ3RUU3JQVU1IR2M5WllvU1paYTh4NjR6bWQycEQ5M1J5Wmh5bTkwNFdneFc4dEtGa3hJVVR4bjFIQzB0b1h1TXlaN2puUjlzakI1YkNrM0p3TnYzODhuby15YUQw?oc=5>

### Nvidia AI Boost Could Matter For ASML Stock (ENXTAM:ASML)
- Summary: Nvidia's AI advancements may influence ASML's stock performance, potentially boosting demand for its lithography equipment.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxPY0Jab3lRS0l2TXV6Ym1ZcWFEekZiZGd3Ulg1aXZ2Unhhb1ctbHljbkdjRlhCc2FrQ19fdDBWUTNkelZ1RDIwQVQ5N2VGeWIwcnhYWnlEU0UwTFgwV2h6Z24tdUVyRURnOFFSLXhoS3hoczNXcUtpbDB3MGVZcllJalZxMmYxSnZKM2VWenBnNWVzZjVCb3lVUGZ2VkNuNjVzWE0tNEtjSHNFLVI2UVdtSjMtNkZtbnl5UUx6SkxDWm5Nc29MMXYtTXdva2dOTGFw0gHWAUFVX3lxTFBFVWk5UzNBaGxDd3VMaVpvMnhaLVhYQjRncWtaTjdYZFIzTXhRN1JBYktQcHB5aFE1WnE2U2EzMFRYSU12NmlRQXp2cFJqV0JZSkVkR2x1TUxNcXY2SDRiUHZFTWVMbGtKQ1Y0WWtIT1BxRGVfTWhDcUpzS2Q2MHlVM2pqWW5LRGxOQ0RfMU1OaDMyOV9pVXJld3h6eEpmSjMxbFpPVTBPcTlIa1BJYlhNMVlqSEJhMnNrYnFheUN0SEtfeklPZWVURElOSFV5Y2o4d2w5Nmc?oc=5>

## RISKS

### ASML Rides on Improving Profitability: Will It Sustain?
- Summary: ASML's profitability gains raise questions about sustainability, potentially affecting future earnings.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxOU3EtQUQ0SjkyVkRISTVBS1gwdmdqUER2SGJsSEFXRDNTZUZzOGFKTThvVFNIWEdvSXpsdlVYekRJM0cxd3ppRTZhTkE1QkRtSnF1TlM2THNGbGN2UXhMdU9Sdm5QNnZBREljOFBkLUhrMXVYaGtucFhkWFo1VTc0LWo2QVM3RzJQbk5XODNLa19FMnNFTGphQmVZOHhqeEZ3MkxNNk5ybGxxU3VFdkE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ASML** | **33.37** | **1,164.50** | **1,783.18** | **55.20** | **522,703,503,360.00 USD** | **31.29** |
| AMAT | 27.92 | 10.30 | 22.31 | 53.10 | 268,973,981,696.00 USD | 45.16 |
| LRCX | 30.35 | 18.29 | 24.78 | 54.40 | 254,431,133,696.00 USD | 37.51 |
| KLAC | 35.46 | 28.27 | 28.21 | 28.90 | 184,343,117,824.00 USD | 21.82 |

Peers fetched as_of: 2026-11-19; ASML reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-14
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

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMihAFBVV95cUxQU1U0UTlvTkdwbzFYYTdkYWRFbEJUNG9haEdJWjFOamQ1RE9HTG1LZklTeHQwRzkyQUtnb2Vxc0hQRFd2S3dqNGJQMnZ1eWlqdzVUZlU4eUVHNHR3RUNmR1hzeU5IWWtiRnIzVVk0TmlmZTFwWVQ5Z3BzTm9nYVg3a0lJZDc?oc=5
- https://news.google.com/rss/articles/CBMia0FVX3lxTFA5SzAtRE1SMDIyUEh3QjI3VEJWMmEza0xyRFYzQWdqRXRzcnFoQWpqRXltVnZKYW80aDN4WTdRNlZLZDhpTjhxaFhEQW1FMXd5RnZMeWJHTGVKZHRuSmM1NEJPWk1XVUhSaTJ3?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPRXVRS2duSzVqMXNJdHNNNzJUVVlUdzFuQkhHQzYxdWVLTGFqYnJzSDE2YzR5cnRTYkY4VXNlVGJ3M3FUemJfanFNVGo2WG9uT19mUndubU5GV3N4OFcta21GeVBQSTVKeHFMU2Z3M2Z0Y3kwQVhYX3UxVWlpN0g4QW9OMXpBRHZqMGZBMGllSFpQQS1POFZsREg3QnBMb0I1LVZnZA?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOUl9OTjV3ak52UDhNeENtTG9GOElJUF9fWWNtZ0dIN1Bzb0R5QUt4WG5tZHEwbHJmM0ZvQnVaWktvaGw5OW9YUFhvSGxodC1yM1B5RVRWNXFNSGJmT2lINGFHazkwSy1zWl9ya2FtVkJmbGJwSThnTmZCeWFraDAwdXE0TG45Q0lucGc?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxON3V1T0l4QmtndUVSMHM1RzJWalliN3BIaDlFTExiQnpELUI4Y2Yyc2UzVk9XbnczcGx3RzFjN3BPN3dhTWotOG42MWQybE5iQW5NTEE3Y19ZTzFBbV9weW9tcnRocmdEdWlfY0RlT0M5Q1R3SlRwbmRxWWhFZUZQcmVLS1VUbFNnUVpaV0EzamJUZjhPU3pvd0o3WQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPUjUxQVlLLUhQRlhhbDhiazlZempiRGR3ZnNRT2JmWmdsTG9sUWpHN1UyS29rRHVEVGNQUjR4eEpGZ3BpcnFBVmV6Vnp3RDNuS0Y4ZXZCWGVRVEV4Y24wRUtyYmhWemVsRXFRa1JRdVBaRTNYNktHWi1zaVVSTTdSTTFkMUpPUDRnSExpM3hnRDh0bnluZDR2UQ?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxNUmtfcVVoWkt3b3VrbzdVM1g2STlWM2lpeXp0Vm5BY2ZsOG51S3dXbVVYZ242S2lnS0ludXFjQzduenc2OHM0alFmY1Rxb3EzRDh5UHpHbU1Ea1oyc0JNVTRreTl2MWxjWDlVamdzRk9mZnZCZ1BNNnl6WTJUTUdLR3lPUGpFLU5NWEtQcFI0bmxLOWliWGd1bF9fWEZ6QWVwdHV3V29TbndCSWpqeTJCVG5qaU95QUI1R0JlM0JmaTVqVXQxZ3FhLUlBLVlxWG95?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOaHFra2Y3LUFrdVY3ejF4TnptNmhHOVFXV0Z0c1RYQ0s2eXlWYmJ1YzZfTG9aeFNyN3ZoVHhZZGZmdjhwaVZ3dTNGY3dpWUNWbEJGd1RQNklnVVE3LUJ3TGVubzIwZWxfNTdhUE1CbXAxd21lZ3JIR1I2ZE1XanRxemx1anlfU0xFN2VR?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQR2xLMTJ3cHZWbUtmUWdBdEplc3ZqeEJzR0h1TWhLRTZEUzVSQ0ZzN0hObmRtX0ZJdUgzTFJIUHJZLVJ6VFU2U2k5VkhWZllCNXN2Mm1TOXFaam1Yb3BVSHh4NUNQcmo1QUxDcW1wcnJaUHdJVmlIMWVVWHd6b3VuVm0wUENSMnoxTWZj?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNN3J5SkhiTk5hdmRyUTVuREItYmxSMEszWWFCS29RTHVWZ001WTlaa2tUZ1V2c0hoVDBQNTROYTBMU2dRQWpSRzVnTXVzVnlLclZ6VnNEbDJuUUtjYlNtWWM2SkhfYVo3ZXpBSk0tS1VjTjRfUU5iZldJUl9rQ3lMMTBGbzVUZUJEUG9CV2xlSExYQ3FFRkhkOGNwLWZLdjBWN1VFSHN0NkdkYzV3cFo0NkNEbVdtWTYxQ2F2Ry1EOUpqcVVwekJBeWJJZGdpQ0tmcmdGZm9n0gHbAUFVX3lxTE1yM2NwbDYySThYQzJzTHNvYVJWbkY4dnFoZUNaVmZ1bTRlY2JCRzkyeEU0TS12RngzejdzR0I1S1FvY3JMYnBIU3E0UjlGUUhwY0ZmWVJxbXd6QWI0bTdvOVI4cjJGVFdqX043MzdhTThBX1E1NDlnVmtBQmIzdGU2bGxSRWRSRnBZME1nVlNCZFZ4cjB2M085d1VhYWljYmhoU3RXb2xsdWhmb2JLSjJVN0JOX0NzbXBSMlo4QXlNMzIzRWpmTTdBZkNqRlczTjdFNzNJRVFzMWdnVQ?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNYlFVSlRnVHh5eFFNUllxdmVOUWQ4T0NaTFZUYnMzQjRiWmFWdi04N0JDSFNXOGJRaGhhd0JvT2UwblZGcndaS04xY3BqNFBWc2twZnNKQlVKMnJLSjNNbEF6MGFsQWhmcDAzcEF3RTNLbGNoRU5XRkdRc215Zm9xVzJsMTBlOXRDY2tXeUJhbGw5ck4weXludWo5NWE1bFZiMENFbmdVUQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQOWY1cDlwVWExLTUwUHFTUXpTa0ZUVDMtRkxVaExqdHNWY0FZMDByWXdVaXpUTV9pTmdqN3d1S2VMTUtmR0VvRWxnWENxRnE2TUhfQktYNm5LNlFaUUZzSGlvZHVYb1FYSDRveE5YTE04S3ZmSy1KMjZHR1ZhZzF2cTdLd05aN1ZQd1dKamh5Y2FnaXk4QUpR?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOVHExZXNEaXpjenZKdzNmak4wTXloVTNSNFdvODVXZ2h1ZWNnSHJTYXFLOGRON1ZhcUZkQ3RUU3JQVU1IR2M5WllvU1paYTh4NjR6bWQycEQ5M1J5Wmh5bTkwNFdneFc4dEtGa3hJVVR4bjFIQzB0b1h1TXlaN2puUjlzakI1YkNrM0p3TnYzODhuby15YUQw?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxPY0Jab3lRS0l2TXV6Ym1ZcWFEekZiZGd3Ulg1aXZ2Unhhb1ctbHljbkdjRlhCc2FrQ19fdDBWUTNkelZ1RDIwQVQ5N2VGeWIwcnhYWnlEU0UwTFgwV2h6Z24tdUVyRURnOFFSLXhoS3hoczNXcUtpbDB3MGVZcllJalZxMmYxSnZKM2VWenBnNWVzZjVCb3lVUGZ2VkNuNjVzWE0tNEtjSHNFLVI2UVdtSjMtNkZtbnl5UUx6SkxDWm5Nc29MMXYtTXdva2dOTGFw0gHWAUFVX3lxTFBFVWk5UzNBaGxDd3VMaVpvMnhaLVhYQjRncWtaTjdYZFIzTXhRN1JBYktQcHB5aFE1WnE2U2EzMFRYSU12NmlRQXp2cFJqV0JZSkVkR2x1TUxNcXY2SDRiUHZFTWVMbGtKQ1Y0WWtIT1BxRGVfTWhDcUpzS2Q2MHlVM2pqWW5LRGxOQ0RfMU1OaDMyOV9pVXJld3h6eEpmSjMxbFpPVTBPcTlIa1BJYlhNMVlqSEJhMnNrYnFheUN0SEtfeklPZWVURElOSFV5Y2o4d2w5Nmc?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxOU3EtQUQ0SjkyVkRISTVBS1gwdmdqUER2SGJsSEFXRDNTZUZzOGFKTThvVFNIWEdvSXpsdlVYekRJM0cxd3ppRTZhTkE1QkRtSnF1TlM2THNGbGN2UXhMdU9Sdm5QNnZBREljOFBkLUhrMXVYaGtucFhkWFo1VTc0LWo2QVM3RzJQbk5XODNLa19FMnNFTGphQmVZOHhqeEZ3MkxNNk5ybGxxU3VFdkE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
