# MSFT Intelligence Report

- ticker: **MSFT**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/MSFT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MSFT/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:42:01.514635+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 17, 'rule': 3, 'ai': 11, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261123T053847Z-45053549/MSFT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 17 unique headlines; 11 named publishers; 0 exact duplicates; 17 HTTPS source links; largest publisher share 23.53%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 492.5000 |
| Return 1D (%) | 1.6470 |
| Return 1W (%) | -4.7373 |
| Return 1M (%) | -5.9215 |
| Return YTD (%) | 2.6802 |
| Return 1Y (%) | 5.1813 |
| Annualized volatility (%) | 34.1103 |
| Beta vs SPY | 0.9386 |
| Max drawdown (%) | -27.9702 |
| Sharpe (rf=0) | 0.3048 |
| Downside deviation (rf=0, %) | 21.8205 |
| Sortino (rf=0) | 0.4765 |
| Historical VaR 95% (1D, %) | 2.8549 |
| Historical ES 95% (1D, %) | 4.1000 |
| Correlation vs SPY | 0.4121 |
| Tracking error vs SPY (%) | 31.0933 |
| P/E (trailing) | 25.70 |
| P/B | 7.77 |
| EV/EBITDA | 18.12 |
| Revenue growth (%) | 18.80 |
| Forward P/E (estimate) | 20.35 |
| Gross margin (%) | 67.66 |
| Operating margin (%) | 47.10 |
| Return on equity (%) | 34.22 |
| Free cash flow yield (%) | 0.08 |
| MA50 | 518.6335 |
| Close vs MA50 (%) | -5.0389 |
| MA200 | 442.3992 |
| Close vs MA200 (%) | 11.3248 |
| RSI (14, Wilder) | 39.3439 |
| MACD (12,26) | -7.0214 |
| MACD signal (9) | -1.9852 |
| MACD histogram | -5.0361 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MSFT': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 492.5000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.6470 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.7373 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -5.9215 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 2.6802 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 5.1813 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.1103 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.8205 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4765 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8549 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1000 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4121 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.0933 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9386 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.9702 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3048 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.3505 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 67.6570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 47.1040 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 34.2210 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.0819 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.7046 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 39.3439 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -5.0361 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.0389 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 11.3248 -> Clearly above the moving-average trend level.

## TAILWINDS

### Microsoft Stock (MSFT) Forecast – Mizuho Stays Bullish on Strong Revenue Growth Prospects
- Summary: Microsoft Stock (MSFT) Forecast – Mizuho Stays Bullish on Strong Revenue Growth Prospects
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNbkpCQ3NWcTBELXRDand5VERMRC1yU1lKS0txQmlDWHEwTFljTU5SeVR6elRCZ1FzdkNCSEV2QU96TWRqTlpvcWNBamJQXzV4TV9TNFBKb1l6clVrTERjcVZPM09YRlFpcEp3cTNNSkJhV3p4OGk1X2ZiMzg2SlhuWkZNbUptcVhCa0w4bFIwN0RRNnAzbFQ4WGg1SUNlUlVFQXJV?oc=5>

### Microsoft Stock (MSFT) Rises 0.4% to $508.29 (Nov 18)
- Summary: Microsoft Stock (MSFT) Rises 0.4% to $508.29 (Nov 18)
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxNRDU5QzhENlNLSXBJMjNkRUllSFZhMHhOSkhWM1hGU3JaZmloRHJYZ3lCVWlHS21vUEVBM2N3UmJEV1FndlJScHdrZFJ6Rkloc05YdlMxV0lWQWJkUXc0QnY1QXd5UUZTeDVsdENvQjgwbXROcm1QNFR6VVpqTGMxaVlrZXo?oc=5>

### Microsoft (MSFT) Stock May Look Reasonable As AI Commitments Draw Scrutiny
- Summary: Analyst suggests MSFT stock appears reasonable amid scrutiny of AI commitments.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNalJYeUVUa3czcERnOXA2LUVJUlJaM0owQlJvZm9Gek1DeHZXV3lwREJFZVM5Nm9KVjdMbC1KRGJmeWg4Rk15M0FZV0ZMNEM0dF9wLXF3dWRpRjhZNVY4Y19fSU9ucUR0QVZKZ1hEQl91eVdnYmlZZ0E4X2RlWmxOWV9KTmpWcEZLZUxBYUJwV3plM3pUOU1MdzF3?oc=5>

### Microsoft (MSFT) and Its Rivals Are Making a Huge AI Bet – Here’s What Investors Should Know
- Summary: Microsoft is investing heavily in AI, positioning itself for future growth.
- Date: 2026-11-20 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQZkJwODVzRnptNlFrc3UtMlA0NUN2bkVNYnNDcGQ3MDBNRzdVbnJPT0Q1c21xNndPMUY5eVA4NzVCUW1fdkx3bGJUMnFUdTV6cjNPUkY4RWpCMXpsNHZjQVp0bHd6RVFmMEpxcGkyNEtNSWJZTklOdVd1Z1RwaWlJX3N1emMxQ0FYUjRaeHlzcXozeFV5bXgzbzZMUERoQQ?oc=5>

### Is Microsoft Stock Stronger Than It Looks?
- Summary: Analysis questioning stock strength.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPSTN0N1hHMGNON3J1ZFRlaGhhZXA4WnZWWlBRRXU2cG9Sd2J5TmVYMGlWSnJ4TWExU0JJaWN3d3RhM0Rja0RkbmhmQkhLMkhkTlFka3p1TFNUUUhQdTRBNWhJMmhYTmY2QU9PZDJybmtoZWEwVDYzY3BDMWMwRUM3Uy1YQ3Rjck10M1dzaWxzRVNQZ05VQ014V2JiTkJqTWZMSURocA?oc=5>

### Microsoft(MSFT) Stock Price Today | Quotes & News
- Summary: Daily stock price update.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi5wJBVV95cUxQRWdGQ2dZeGs1RnZYbmRPaG9STmFIUFZGUGY1ZWoxWjQtLVlvZGdmR2VIRnpvSHJiOG4wOWVDWklLdUFxNmpiekxaRWtiZzA4Y0NVNFpLMzJjZGtCV1JkX3ptYlkzeE1nQ1FHZ3dnVHVzbXpreU5BcmQweTBZSEcwYm1pTnV1VXhkWW8wWHhHMkE1NXBsdXBMeE0wUW9HTDVwa2dxaHlPdnZpbkhQLWhSbURkUmFLX2FmU0UycUwzazhrZEMwS2tSV05Kek1kNEtQbGFzODJCTmJ6UDJ2dlZvZ2dsYkFhZlJoYlNQZXE5SUdlUzE4anBEYVBsa2UyeGV5Z0R0X0dWNDh0a3dick1NcmhxVDJ5S1V0YmYwbi1CTXQyWFYxc1lDelgwcVdFN3M2NVM4QnBzaFV5cXA3d2U3am9fM1N3TDNUeG5vSWFhT3A4OVVwaENKMFFGb2lieGhoYXNMNHJFQQ?oc=5>

### Microsoft Corp Stock (MSFT) Opened Up by 3.39% on Nov 23: A Full Analysis
- Summary: Stock opened higher by 3.39%.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPWUd0X3I1bVJ2SDRzRDBLajlQcXRUTWFMbjg1RS1YR1BhWlR1UVM0dEgtS2VWc2lySFpXYkppSC1XMnFaZkdXa0cxMjBqbjZBRkxYLUd3Y3RhTmdUUVlLTzREdmJEWEhJVWhXTjZucWZoOFYtNXJmdU0tWVJVWXM1S1Y1QkFlY0RVQ0Nz?oc=5>

### New Buy Rating for Microsoft (MSFT), the Technology Giant
- Summary: Analyst upgraded rating to buy.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNcllITFdRQy1wY0NxVWxIXzQxdUczaDdXeDdyU1NwcWQzdzB4LTlUajhjUS1HQVhZM29Dek1mVGlpczUwZXZYY1F2dVB4aFZMN0lHV2FoWERYRVdmakRWMlI1Q1VvV1BvTWJTODFzc3F2aHNzY0Y1U1Z1MjZfeE1LZlU2d3R6YVcxRXhoeFlLcEwtdzlQOTZUdzNjbHBKT1BiYy1mSzZBc2NtOUN0dzctQTkwYXoxTFk3UklOT1lKRkdWMTVIVDN5OVE4ZnlxN2ZvdmZXemV3?oc=5>

### Weekly Recap: Azure revenue growth and Maia 300 AI chip unveiling
- Summary: Azure revenue growth and new AI chip unveiled.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPdTJLNGZUM2ZLZEV3d3JWZEM2Z1pqYzRkM0E1bWdpNjJHcVhraEQyTU9vNTZ2T1RzNlF4UWs5aUVCNU9jN3R2NmhQN1ptM2JiQXJtRFl2SmExekh0bG5JZzV0eTVFODJZancxRUxUcF82RDhRRE9mTk5YS3dNZWhsS0F4aWc0MlN3YnFYZDBoNnlLMDg2NktSZ2pPU3gxYXVkajM3bmNqRmY0dTB4ZHJpbDh4dlF1ZVBNRlNpd1p6cV94Z29H?oc=5>

## HEADWINDS

### Microsoft MSFT Stock Drops but $500 Holds as New Cybersecurity Concerns Hit Tech
- Summary: Microsoft MSFT Stock Drops but $500 Holds as New Cybersecurity Concerns Hit Tech
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQMzdIamo3aFJCeDlxRWVEZWJmdTNtNElVM3pER2ozc2tkNGlBa01XdmNfdDBURDVVVFgySXN0eXk3NEtHNGQ3dmJXMHRFTDZHOFRPSnlJZGpUY2ZzcTZqUjhXaHBaemc2dmV1VXloZnZqb3FZRzVVd0Vmd2JReUJHSmNUTURzbWQ0ajA4S1RhT096cFZUTThKVVR2MkVLRzVtc1VsVHlFd2NMMXZYaE15d2JyR3hDaVhYTWZCeDFVQQ?oc=5>

### What Could Stall Microsoft Stock’s Run?
- Summary: Article discusses potential factors that could hinder Microsoft’s stock performance.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPd1NYMThWX2pISm1GWnk1MGZFU0lxUi1lV2FIMVFJV3BJa3lvSmVlOXRJTEhHVm90cTFjOEhjVDc3OVRvbWVpc2FEMUVwRlQzOWJPQTVYYWREVEF0V0RQUWpZVjgwdWs1eDhsY21sMjdFZXFEaFNMaDVibW9ibjYyQ1gxYWxfRXd1cXJZN09zWGVEN2lZRHIwY3BYZ190aHM?oc=5>

## CATALYSTS

### Microsoft Corporation (MSFT) Stock Forecasts
- Summary: Analysts provided stock forecasts for Microsoft.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPQTVtR182YU9iMFIxRHBBTHlWeFRJTWJmMDI4WWwyWUFmem1IWFBPeTYyY3pKQ3o1bkJBZnVwY0xwZ0ZsRHA2UHNzVGFMTjhiRnRMWEtNY2pJLWxnNm1uLTFpZ1cxdUxpZlVaaWl5d2ZtWlJPY2Q5SERuYWNncEQ3UnFlQkxxVTl3MDhOWA?oc=5>

### Microsoft emphasizes 'pay-for-performance' in its Azure cloud division: report
- Summary: Microsoft introduces pay-for-performance model for Azure cloud services.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPSjlwdzByRXV3R0NCMnZ3NU1VQktxYmNIdDVyaTZRNTRCSmtoU0k5NkpXcmdDTmFDNmZlUEw1dFRhRlp1anJJdmNqdzVERFpQX2xIajZ0c0FuZ2tiN0tTckhkSDB1dVFvb3U3eTIyUE1JX0hmSFN1N0RYaDZsNTVXLS1mWl9TSXF4Ums3UWJ4MlNjVHhfM3M4b0RZdWNuM0lNSkVER29CMFY4SDVuUUtsb29LQQ?oc=5>

## RISKS

### Microsoft rises as warning on Chinese optical hardware ban fuels AI investment concern
- Summary: Chinese ban warning may dampen AI investment, potentially affecting Microsoft’s growth prospects.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxPRERJcHRpV3FoSUtqN2I0SXk5TGFGYWNjNHZtTGdHaDFuNk9nYklsUlU1WENjMm12OGZzRGZaZ2JoOVQ4cXRiTTA0REdIeWwza0JVSVZ3ZnpKYW5SMFR5X1FuZmNNSnVmUlpSUUM0WHl4c0VKSGVnZ09OeG9KSE5LMFZzSEZQQQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MSFT** | **25.70** | **7.77** | **18.12** | **18.80** | **3,657,400,844,288.00 USD** | **5.18** |
| ORCL | 17.82 | 5.56 | 13.97 | 29.60 | 354,421,047,296.00 USD | -42.04 |
| GOOGL | 14.73 | 5.26 | 18.17 | 24.70 | 3,468,137,332,736.00 USD | -5.62 |
| AMZN | 20.65 | 4.50 | 16.07 | 12.10 | 2,761,567,240,192.00 USD | 15.72 |

Peers fetched as_of: 2026-11-23; MSFT reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 19,953,000,000.00 USD; period 2010-10-01/2010-12-31; fiscal year/reporting period 2011/Q2
- Net income (latest available single quarter): 36,629,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiowFBVV95cUxNbkpCQ3NWcTBELXRDand5VERMRC1yU1lKS0txQmlDWHEwTFljTU5SeVR6elRCZ1FzdkNCSEV2QU96TWRqTlpvcWNBamJQXzV4TV9TNFBKb1l6clVrTERjcVZPM09YRlFpcEp3cTNNSkJhV3p4OGk1X2ZiMzg2SlhuWkZNbUptcVhCa0w4bFIwN0RRNnAzbFQ4WGg1SUNlUlVFQXJV?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxNRDU5QzhENlNLSXBJMjNkRUllSFZhMHhOSkhWM1hGU3JaZmloRHJYZ3lCVWlHS21vUEVBM2N3UmJEV1FndlJScHdrZFJ6Rkloc05YdlMxV0lWQWJkUXc0QnY1QXd5UUZTeDVsdENvQjgwbXROcm1QNFR6VVpqTGMxaVlrZXo?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNalJYeUVUa3czcERnOXA2LUVJUlJaM0owQlJvZm9Gek1DeHZXV3lwREJFZVM5Nm9KVjdMbC1KRGJmeWg4Rk15M0FZV0ZMNEM0dF9wLXF3dWRpRjhZNVY4Y19fSU9ucUR0QVZKZ1hEQl91eVdnYmlZZ0E4X2RlWmxOWV9KTmpWcEZLZUxBYUJwV3plM3pUOU1MdzF3?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQZkJwODVzRnptNlFrc3UtMlA0NUN2bkVNYnNDcGQ3MDBNRzdVbnJPT0Q1c21xNndPMUY5eVA4NzVCUW1fdkx3bGJUMnFUdTV6cjNPUkY4RWpCMXpsNHZjQVp0bHd6RVFmMEpxcGkyNEtNSWJZTklOdVd1Z1RwaWlJX3N1emMxQ0FYUjRaeHlzcXozeFV5bXgzbzZMUERoQQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPSTN0N1hHMGNON3J1ZFRlaGhhZXA4WnZWWlBRRXU2cG9Sd2J5TmVYMGlWSnJ4TWExU0JJaWN3d3RhM0Rja0RkbmhmQkhLMkhkTlFka3p1TFNUUUhQdTRBNWhJMmhYTmY2QU9PZDJybmtoZWEwVDYzY3BDMWMwRUM3Uy1YQ3Rjck10M1dzaWxzRVNQZ05VQ014V2JiTkJqTWZMSURocA?oc=5
- https://news.google.com/rss/articles/CBMi5wJBVV95cUxQRWdGQ2dZeGs1RnZYbmRPaG9STmFIUFZGUGY1ZWoxWjQtLVlvZGdmR2VIRnpvSHJiOG4wOWVDWklLdUFxNmpiekxaRWtiZzA4Y0NVNFpLMzJjZGtCV1JkX3ptYlkzeE1nQ1FHZ3dnVHVzbXpreU5BcmQweTBZSEcwYm1pTnV1VXhkWW8wWHhHMkE1NXBsdXBMeE0wUW9HTDVwa2dxaHlPdnZpbkhQLWhSbURkUmFLX2FmU0UycUwzazhrZEMwS2tSV05Kek1kNEtQbGFzODJCTmJ6UDJ2dlZvZ2dsYkFhZlJoYlNQZXE5SUdlUzE4anBEYVBsa2UyeGV5Z0R0X0dWNDh0a3dick1NcmhxVDJ5S1V0YmYwbi1CTXQyWFYxc1lDelgwcVdFN3M2NVM4QnBzaFV5cXA3d2U3am9fM1N3TDNUeG5vSWFhT3A4OVVwaENKMFFGb2lieGhoYXNMNHJFQQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPWUd0X3I1bVJ2SDRzRDBLajlQcXRUTWFMbjg1RS1YR1BhWlR1UVM0dEgtS2VWc2lySFpXYkppSC1XMnFaZkdXa0cxMjBqbjZBRkxYLUd3Y3RhTmdUUVlLTzREdmJEWEhJVWhXTjZucWZoOFYtNXJmdU0tWVJVWXM1S1Y1QkFlY0RVQ0Nz?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNcllITFdRQy1wY0NxVWxIXzQxdUczaDdXeDdyU1NwcWQzdzB4LTlUajhjUS1HQVhZM29Dek1mVGlpczUwZXZYY1F2dVB4aFZMN0lHV2FoWERYRVdmakRWMlI1Q1VvV1BvTWJTODFzc3F2aHNzY0Y1U1Z1MjZfeE1LZlU2d3R6YVcxRXhoeFlLcEwtdzlQOTZUdzNjbHBKT1BiYy1mSzZBc2NtOUN0dzctQTkwYXoxTFk3UklOT1lKRkdWMTVIVDN5OVE4ZnlxN2ZvdmZXemV3?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPdTJLNGZUM2ZLZEV3d3JWZEM2Z1pqYzRkM0E1bWdpNjJHcVhraEQyTU9vNTZ2T1RzNlF4UWs5aUVCNU9jN3R2NmhQN1ptM2JiQXJtRFl2SmExekh0bG5JZzV0eTVFODJZancxRUxUcF82RDhRRE9mTk5YS3dNZWhsS0F4aWc0MlN3YnFYZDBoNnlLMDg2NktSZ2pPU3gxYXVkajM3bmNqRmY0dTB4ZHJpbDh4dlF1ZVBNRlNpd1p6cV94Z29H?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQMzdIamo3aFJCeDlxRWVEZWJmdTNtNElVM3pER2ozc2tkNGlBa01XdmNfdDBURDVVVFgySXN0eXk3NEtHNGQ3dmJXMHRFTDZHOFRPSnlJZGpUY2ZzcTZqUjhXaHBaemc2dmV1VXloZnZqb3FZRzVVd0Vmd2JReUJHSmNUTURzbWQ0ajA4S1RhT096cFZUTThKVVR2MkVLRzVtc1VsVHlFd2NMMXZYaE15d2JyR3hDaVhYTWZCeDFVQQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPd1NYMThWX2pISm1GWnk1MGZFU0lxUi1lV2FIMVFJV3BJa3lvSmVlOXRJTEhHVm90cTFjOEhjVDc3OVRvbWVpc2FEMUVwRlQzOWJPQTVYYWREVEF0V0RQUWpZVjgwdWs1eDhsY21sMjdFZXFEaFNMaDVibW9ibjYyQ1gxYWxfRXd1cXJZN09zWGVEN2lZRHIwY3BYZ190aHM?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPQTVtR182YU9iMFIxRHBBTHlWeFRJTWJmMDI4WWwyWUFmem1IWFBPeTYyY3pKQ3o1bkJBZnVwY0xwZ0ZsRHA2UHNzVGFMTjhiRnRMWEtNY2pJLWxnNm1uLTFpZ1cxdUxpZlVaaWl5d2ZtWlJPY2Q5SERuYWNncEQ3UnFlQkxxVTl3MDhOWA?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPSjlwdzByRXV3R0NCMnZ3NU1VQktxYmNIdDVyaTZRNTRCSmtoU0k5NkpXcmdDTmFDNmZlUEw1dFRhRlp1anJJdmNqdzVERFpQX2xIajZ0c0FuZ2tiN0tTckhkSDB1dVFvb3U3eTIyUE1JX0hmSFN1N0RYaDZsNTVXLS1mWl9TSXF4Ums3UWJ4MlNjVHhfM3M4b0RZdWNuM0lNSkVER29CMFY4SDVuUUtsb29LQQ?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxPRERJcHRpV3FoSUtqN2I0SXk5TGFGYWNjNHZtTGdHaDFuNk9nYklsUlU1WENjMm12OGZzRGZaZ2JoOVQ4cXRiTTA0REdIeWwza0JVSVZ3ZnpKYW5SMFR5X1FuZmNNSnVmUlpSUUM0WHl4c0VKSGVnZ09OeG9KSE5LMFZzSEZQQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
