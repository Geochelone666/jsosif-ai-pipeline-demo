# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:28:27.508458+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 2, 'ai': 11, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261123T053847Z-45053549/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 16 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 453.4600 |
| Return 1D (%) | 6.8498 |
| Return 1W (%) | -10.0777 |
| Return 1M (%) | -12.2545 |
| Return YTD (%) | 111.7389 |
| Return 1Y (%) | 122.5243 |
| Annualized volatility (%) | 75.0342 |
| Beta vs SPY | 3.2427 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.3782 |
| Downside deviation (rf=0, %) | 49.6068 |
| Sortino (rf=0) | 2.0847 |
| Historical VaR 95% (1D, %) | 6.9752 |
| Historical ES 95% (1D, %) | 10.1271 |
| Correlation vs SPY | 0.6472 |
| Tracking error vs SPY (%) | 66.3326 |
| P/E (trailing) | 96.89 |
| P/B | 10.87 |
| EV/EBITDA | 66.15 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 25.71 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 17.82 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 0.98 |
| MA50 | 552.2986 |
| Close vs MA50 (%) | -17.8959 |
| MA200 | 431.0112 |
| Close vs MA200 (%) | 5.2084 |
| RSI (14, Wilder) | 42.5580 |
| MACD (12,26) | -18.8510 |
| MACD signal (9) | -14.0286 |
| MACD histogram | -4.8225 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 453.4600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 6.8498 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -10.0777 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -12.2545 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 111.7389 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 122.5243 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 75.0342 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 49.6068 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.0847 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.9752 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.1271 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6472 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 66.3326 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.2427 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.3782 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.7089 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.9803 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 96.8932 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.5580 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.8225 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -17.8959 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 5.2084 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD’s Data Center Sales Jumped 97%. Is the Stock a Buy?
- Summary: AMD’s Data Center Sales Jumped 97%. Is the Stock a Buy?
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOeGVYdV9Ga0hQQzdiZ0NxZ1l4Nk1aZ2stV0N3M0RvLVY0U2FKM1M4b1BfVnMzSWk0Wm5LRkJIN3ItSkJoVV9Ia2UyM2t6QUloOFctcXJ4ajViTWpNUUl4V2V4YTZzUGdfLUkyN2NIQ1paeFVlcThHcEFveEduaDlueFdjSDd1RGcyYkpCVWMxM2N1UXZtWVlBaw?oc=5>

### Why Is AMD Stock Surging on Monday?
- Summary: AMD shares jump, boosting investor confidence and market perception.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQQnUyRHJUVmlNUWFHdUlKQko5OHl1azVBdU1OVlRqMkpqV0ltVjlHUVA4M3E1YmotSTNzeHp4NmExMkIzcUppQ0lReTdhQ1k1VUJ3Wk5zT0s3VFdOR3hOXzNING5GYlFHeU1ndEVkTFFJcVh2WVJMa0ZfVHBEbmlZMDhVR1JEMDJUTm02ckdiYVVsdlZmRlRkb2h1VWduZw?oc=5>

## HEADWINDS

### AMD stock forecast: AI growth faces China export risks and valuation pressure
- Summary: AMD stock forecast: AI growth faces China export risks and valuation pressure
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOOTV5bmxick9rcmZBZGVWaTRsR1RKWEFlRW4zZmQtbW5tN09nZ3J5T1RpMVRYSlQyMHZna0loWG5HazM2bUZRUlU5SkhCZXFmU2s2M3RhZkhQZ2tyTWdwQVZGU2RpNi02aWszejg0RC01OEhoQkhxNUdqN1hFUnJtM3VidlJtUHBWSVRKck1qekIyWEs1aHY4Y2wwRU0tSDZhWVptMldR?oc=5>

### Why Is AMD Stock Falling on Friday?
- Summary: Investors concerned about recent performance and market conditions, leading to a decline in AMD shares.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPakd6RUtYYTBuV2dfQVE4SWpBendrV1B4UmdxOUt4R2djNzVkbWo5VV9qTmZ5YjRHaUJwSXhHb0dZMG5RMTJGQVNhcWZyT1prN3JFdFBWN1JWQ0twS3RDc3ZDVjVWbDltUVZWOURuTHZ6V1MxRkhGN3NCZ1V2N1NRX0FPUnRPamJOVU1EYnVRWkRXR2N2TWZUdnJ4WQ?oc=5>

### Is AMD's Stock in Trouble After a Concerning Short-Seller Report?
- Summary: Short-seller report raises doubts, potentially dampening investor sentiment.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxOdVBBOF9Jc2lOcjZFOWRETzdxTXhwQUhIazBTTjFRRnFucE1lSFFNSXBSX0JXekNYWHM5eXVlYlppZzcyZUM3ZHVOYlpreUVBdGFyZFVTU2hFQjFSTU1sb09pSXl0ZHc5cVlxZUdrcFhxTGJDQUcyWjlWaUt2OTJoUWkwVm1McHliVVVMeC1zVUtiSURGWGEzNHBUVVM3c2RXbFhsekI3Rnlidm5mSW9fZktsYTJZMkpnX3R5dlMwU3p3QXRDcnhSNHhCczBXajNzQW96Z2NFRTN5Y1FPaXVCYg?oc=5>

## CATALYSTS

### AMD registers up to 337 million shares for resale tied to OpenAI, Meta warrants
- Summary: AMD registers up to 337 million shares for resale tied to OpenAI and Meta warrants, indicating a potential stock split or share issuance.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxQTEUtd1VrdC1lbGtJZG5xcFA0NjJySjBtc3M5eHRybzJ6R0NxR0RLQmhtckVwTmNObHFoVzNVTVZxaERjVEVVMnMtaE43OHd0bEtaMTVoUy1jcnBLejIzckpIN2VDTU82WWY4YVR2Q01fU3ZqVEk1NEx4Z0RFS0FsN2dBN01vemNCUWI3b3pWTGUxSTJnQmZlNjVzZ08yMW5jS1BlYWdGRkctZmdQRnhsd2lqZnFZZG1EbWdhQV9LSmF0Q0pWaTJBVFJIckZvQnRH?oc=5>

### Advanced Micro Devices, Inc. (AMD) is Attracting Investor Attention: Here is What You Should Know
- Summary: Investor attention highlighted, no specific event disclosed.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOZkZxQzNLc04tWGhod0c2ZmRjeW9pNHdhekQyOENwZ3A5YjhocURDeFpjUFZSNHNnUzRWQktUcGhZUnlmTGZBdTJVcVBxTFM0bC1DRWJidVlKemJlUktpYTQxTGtsUk1xSUZTRmdFRVhEbDdDakFyWl9YSHZ0NkRnaEszRGpZQ3VXM0JyQUxZUlFjS0ZvUGRkbVM4bw?oc=5>

### How to Play AMD Stock as Hunterbrook Slams the Company With a New Short Report
- Summary: Short report issued, negative analyst stance.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOUGtQQXd2TllZXzYtaEJrSkM0c3V1RGRLVlhycU5BNUFKekVfSWVnamYzQ0ZYOUZxeXlyeFNqNmtyYkVxUXE4OEtWNm1VTUIyT0JPdkRSMEctMnJFb0lCUmV5ck16N1g2d2NiaU4zLXg5NGY4alpDRXBCUnpJSTBrY2QwaldESVktbjdXcVNCOE9KR2V1ZTFYMm40VHZjY0dlZGxvdWMyWmVIR1hSSF9JbDhSMzRoOXlyODU1TEc0UQ?oc=5>

### AMD (Advanced Micro Devices) : Bernstein reiterates its Buy rating
- Summary: Buy rating reaffirmed by Bernstein.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOdUEtNDd5TDhvOUhPaGRmSzI2NjhNR0o1ZHNQb1B2Ul9KM0dUZ1lJbXJ4MHJzYkpmdUctREk1OHFFZF9FTUJMajRNZThVVDhRdjZ3WXppVFhTZUlSZjB5bEpGeEZ0Z1JldmRyWHIxaGJYUVBJZTJBV09lUHRHNVBLYTVQbUltT0JwbkRSblo0YnA5NmRjOFBCQnVqTW9fWngzWHNRTUtPWFdCZzIwb3FtWnVNbHV0Zw?oc=5>

### AMD vs. Palantir: One AI Stock Is a Buy Now, One Can Wait, Says Top Investor
- Summary: Top investor compares AMD favorably to Palantir.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNM2FVdVVQQldqX2lYdnBvbzVsSm03ZlI0TW1rRF9Xd1pDNVZ5bjNmV0dFR2IyWlMxVzlxemVLQjFJblR4REdKUG9mVWM2WEpQM1MtSkRxWVpvSDhSZVhoa0lwOGdYcDFRM3R0eUlTUWUzWnJuLTJEVS1fbU10cHdFOURtVm9IYjJoYkRmY1NFQzFBN0d6aEludkt4eFJaVzExZEw2NXlaMFF1TERuc2tn?oc=5>

### Stock Market Today, Nov. 23: Advanced Micro Devices Climbs on AI-Chip Rebound After Nvidia Reinstates Jensen Huang as CEO
- Summary: AMD shares rose on AI-chip rebound, linked to Nvidia CEO change.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwJBVV95cUxQeWlXazZSREdHVFpCWDBzdG1YTHQwU2JmZXc5Y0dqamhsaTV0YWo5UzFqbUk2aVM0Q0p6TWtxb3kzdUQtdVVySWg0V3lNRm1SSlNuMmx3V09SVGhvZUh6bS1hNmFHR05ENGdHSjRDR1o1SmxnTXJMYmQ0ZWdTRmhBbk0xTjBENHdoRUQ3RG1waTZNYkNodEFMdHZrQjRkRmJUUkxPWkxLR3dkUXdyaTNGcmwxdlp5SlFtRmxpMENLRTBoWDV3aE45cktrVU94Rnk2cXdlXzg1d3hQZ2g3NWgxbmxjc2trcEtvN1o1S3VHNThuS2dnTmZSVU15aUF2ZWFaaTdwU0ZKOWsyTnc?oc=5>

## RISKS

### Advanced Micro Devices (AMD) Faces Firmware Allegations And Class Action Scrutiny
- Summary: AMD faces firmware allegations and class‑action scrutiny, potentially impacting operations and reputation.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNX0RaMHU5SVFZX1JpOHYzRVBPOGxQYTF6UFlwbUU3aG9YWWNKdENRZ3VSVXdUaW14TElpcldNTzY5SXhQdm5OTnNQdG40TFpXLTFYeFo0dzV5Qy0tLXpqYmJTc2xXMTdUMlVXLWpnbUdSZjh6WUFiMXFFVllpWWdtcHhWR2RxMENBVnNfOXhpLTVoTTlxMGJESUxOWjFGUQ?oc=5>

### AMD Gained From Nvidia’s China Scandal. Now a Short Seller Says AMD Has a China Problem Too.
- Summary: Short seller alleges AMD faces China issues after Nvidia scandal.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNM2UyYnM1anhCMjQ0bTNQYXVwLWRhMHVoOFRWZU5kUXRvbksxQUM2UW5vYTBkX0U4RXZZVUlySTZ6UEV3SEp0OTM4UmVudnk0dUFtZm1aTTR2b001MnJmdnJZVFBzaTFmOU1hcTljTDktZm5OampyVklMUmJkYzliWVJHSXhoM3MxYmFtN3l0RzU4X1kydWNCQkhhc2g?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **96.89** | **10.87** | **66.15** | **44.70** | **750,506,016,768.00 USD** | **122.52** |
| NVDA | 17.73 | 14.92 | 16.11 | 103.20 | 3,985,462,263,808.00 USD | -7.51 |
| INTC | N/A | 2.76 | 17.24 | 20.90 | 317,092,888,576.00 USD | 72.93 |
| AVGO | 40.04 | 15.02 | 29.32 | 85.50 | 1,496,771,592,192.00 USD | -7.15 |

Peers fetched as_of: 2026-11-23; AMD reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

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
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,428,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxOeGVYdV9Ga0hQQzdiZ0NxZ1l4Nk1aZ2stV0N3M0RvLVY0U2FKM1M4b1BfVnMzSWk0Wm5LRkJIN3ItSkJoVV9Ia2UyM2t6QUloOFctcXJ4ajViTWpNUUl4V2V4YTZzUGdfLUkyN2NIQ1paeFVlcThHcEFveEduaDlueFdjSDd1RGcyYkpCVWMxM2N1UXZtWVlBaw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQQnUyRHJUVmlNUWFHdUlKQko5OHl1azVBdU1OVlRqMkpqV0ltVjlHUVA4M3E1YmotSTNzeHp4NmExMkIzcUppQ0lReTdhQ1k1VUJ3Wk5zT0s3VFdOR3hOXzNING5GYlFHeU1ndEVkTFFJcVh2WVJMa0ZfVHBEbmlZMDhVR1JEMDJUTm02ckdiYVVsdlZmRlRkb2h1VWduZw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOOTV5bmxick9rcmZBZGVWaTRsR1RKWEFlRW4zZmQtbW5tN09nZ3J5T1RpMVRYSlQyMHZna0loWG5HazM2bUZRUlU5SkhCZXFmU2s2M3RhZkhQZ2tyTWdwQVZGU2RpNi02aWszejg0RC01OEhoQkhxNUdqN1hFUnJtM3VidlJtUHBWSVRKck1qekIyWEs1aHY4Y2wwRU0tSDZhWVptMldR?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPakd6RUtYYTBuV2dfQVE4SWpBendrV1B4UmdxOUt4R2djNzVkbWo5VV9qTmZ5YjRHaUJwSXhHb0dZMG5RMTJGQVNhcWZyT1prN3JFdFBWN1JWQ0twS3RDc3ZDVjVWbDltUVZWOURuTHZ6V1MxRkhGN3NCZ1V2N1NRX0FPUnRPamJOVU1EYnVRWkRXR2N2TWZUdnJ4WQ?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxOdVBBOF9Jc2lOcjZFOWRETzdxTXhwQUhIazBTTjFRRnFucE1lSFFNSXBSX0JXekNYWHM5eXVlYlppZzcyZUM3ZHVOYlpreUVBdGFyZFVTU2hFQjFSTU1sb09pSXl0ZHc5cVlxZUdrcFhxTGJDQUcyWjlWaUt2OTJoUWkwVm1McHliVVVMeC1zVUtiSURGWGEzNHBUVVM3c2RXbFhsekI3Rnlidm5mSW9fZktsYTJZMkpnX3R5dlMwU3p3QXRDcnhSNHhCczBXajNzQW96Z2NFRTN5Y1FPaXVCYg?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPclhvdTVuOXdjb2dEZmc4YTNGUk5DZllnVzkzWTQwbl9NM1VxVGtsNjBLRnZUX1lXT196clVESUFZVXhUMzB3YzhZSUFSY0VWV2ZuckhkMW54dzV2aU9MVFJoLUpGVVZMNEFFaWszOENUR1Z4WUlxNDc1R2lmenhJRHQ1a0Y0ZXdPaXFwUW1CS2EtYU1UY3BQWlliVWlaX3lmaWRQUmhVNkZJdkE?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxQTEUtd1VrdC1lbGtJZG5xcFA0NjJySjBtc3M5eHRybzJ6R0NxR0RLQmhtckVwTmNObHFoVzNVTVZxaERjVEVVMnMtaE43OHd0bEtaMTVoUy1jcnBLejIzckpIN2VDTU82WWY4YVR2Q01fU3ZqVEk1NEx4Z0RFS0FsN2dBN01vemNCUWI3b3pWTGUxSTJnQmZlNjVzZ08yMW5jS1BlYWdGRkctZmdQRnhsd2lqZnFZZG1EbWdhQV9LSmF0Q0pWaTJBVFJIckZvQnRH?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOZkZxQzNLc04tWGhod0c2ZmRjeW9pNHdhekQyOENwZ3A5YjhocURDeFpjUFZSNHNnUzRWQktUcGhZUnlmTGZBdTJVcVBxTFM0bC1DRWJidVlKemJlUktpYTQxTGtsUk1xSUZTRmdFRVhEbDdDakFyWl9YSHZ0NkRnaEszRGpZQ3VXM0JyQUxZUlFjS0ZvUGRkbVM4bw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOUGtQQXd2TllZXzYtaEJrSkM0c3V1RGRLVlhycU5BNUFKekVfSWVnamYzQ0ZYOUZxeXlyeFNqNmtyYkVxUXE4OEtWNm1VTUIyT0JPdkRSMEctMnJFb0lCUmV5ck16N1g2d2NiaU4zLXg5NGY4alpDRXBCUnpJSTBrY2QwaldESVktbjdXcVNCOE9KR2V1ZTFYMm40VHZjY0dlZGxvdWMyWmVIR1hSSF9JbDhSMzRoOXlyODU1TEc0UQ?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOdUEtNDd5TDhvOUhPaGRmSzI2NjhNR0o1ZHNQb1B2Ul9KM0dUZ1lJbXJ4MHJzYkpmdUctREk1OHFFZF9FTUJMajRNZThVVDhRdjZ3WXppVFhTZUlSZjB5bEpGeEZ0Z1JldmRyWHIxaGJYUVBJZTJBV09lUHRHNVBLYTVQbUltT0JwbkRSblo0YnA5NmRjOFBCQnVqTW9fWngzWHNRTUtPWFdCZzIwb3FtWnVNbHV0Zw?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNM2FVdVVQQldqX2lYdnBvbzVsSm03ZlI0TW1rRF9Xd1pDNVZ5bjNmV0dFR2IyWlMxVzlxemVLQjFJblR4REdKUG9mVWM2WEpQM1MtSkRxWVpvSDhSZVhoa0lwOGdYcDFRM3R0eUlTUWUzWnJuLTJEVS1fbU10cHdFOURtVm9IYjJoYkRmY1NFQzFBN0d6aEludkt4eFJaVzExZEw2NXlaMFF1TERuc2tn?oc=5
- https://news.google.com/rss/articles/CBMiiwJBVV95cUxQeWlXazZSREdHVFpCWDBzdG1YTHQwU2JmZXc5Y0dqamhsaTV0YWo5UzFqbUk2aVM0Q0p6TWtxb3kzdUQtdVVySWg0V3lNRm1SSlNuMmx3V09SVGhvZUh6bS1hNmFHR05ENGdHSjRDR1o1SmxnTXJMYmQ0ZWdTRmhBbk0xTjBENHdoRUQ3RG1waTZNYkNodEFMdHZrQjRkRmJUUkxPWkxLR3dkUXdyaTNGcmwxdlp5SlFtRmxpMENLRTBoWDV3aE45cktrVU94Rnk2cXdlXzg1d3hQZ2g3NWgxbmxjc2trcEtvN1o1S3VHNThuS2dnTmZSVU15aUF2ZWFaaTdwU0ZKOWsyTnc?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNX0RaMHU5SVFZX1JpOHYzRVBPOGxQYTF6UFlwbUU3aG9YWWNKdENRZ3VSVXdUaW14TElpcldNTzY5SXhQdm5OTnNQdG40TFpXLTFYeFo0dzV5Qy0tLXpqYmJTc2xXMTdUMlVXLWpnbUdSZjh6WUFiMXFFVllpWWdtcHhWR2RxMENBVnNfOXhpLTVoTTlxMGJESUxOWjFGUQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNM2UyYnM1anhCMjQ0bTNQYXVwLWRhMHVoOFRWZU5kUXRvbksxQUM2UW5vYTBkX0U4RXZZVUlySTZ6UEV3SEp0OTM4UmVudnk0dUFtZm1aTTR2b001MnJmdnJZVFBzaTFmOU1hcTljTDktZm5OampyVklMUmJkYzliWVJHSXhoM3MxYmFtN3l0RzU4X1kydWNCQkhhc2g?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
