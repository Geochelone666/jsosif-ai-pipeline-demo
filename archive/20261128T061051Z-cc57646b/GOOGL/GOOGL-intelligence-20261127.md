# GOOGL Intelligence Report

- ticker: **GOOGL**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/GOOGL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GOOGL/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:21:51.642520+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 3, 'ai': 11, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/GOOGL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'negative_sentiment_in_tailwinds': 1, 'positive_sentiment_in_headwinds': 1, 'short_term_price_move_in_structural_risks': 2}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 11 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 20.83%; oldest publication 2026-11-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 274.9600 |
| Return 1D (%) | 0.6811 |
| Return 1W (%) | 3.6451 |
| Return 1M (%) | -14.2305 |
| Return YTD (%) | -11.9825 |
| Return 1Y (%) | -13.8381 |
| Annualized volatility (%) | 33.6853 |
| Beta vs SPY | 1.2565 |
| Max drawdown (%) | -34.0273 |
| Sharpe (rf=0) | -0.2788 |
| Downside deviation (rf=0, %) | 24.3732 |
| Sortino (rf=0) | -0.3853 |
| Historical VaR 95% (1D, %) | 3.1840 |
| Historical ES 95% (1D, %) | 4.8274 |
| Correlation vs SPY | 0.5603 |
| Tracking error vs SPY (%) | 28.1655 |
| P/E (trailing) | 14.36 |
| P/B | 5.13 |
| EV/EBITDA | 17.70 |
| Revenue growth (%) | 24.70 |
| Forward P/E (estimate) | 17.97 |
| Gross margin (%) | 60.86 |
| Operating margin (%) | 33.32 |
| Return on equity (%) | 44.29 |
| Free cash flow yield (%) | -0.03 |
| MA50 | 316.7934 |
| Close vs MA50 (%) | -13.2053 |
| MA200 | 335.8842 |
| Close vs MA200 (%) | -18.1385 |
| RSI (14, Wilder) | 38.3380 |
| MACD (12,26) | -11.6976 |
| MACD signal (9) | -12.4810 |
| MACD histogram | 0.7834 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GOOGL': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 274.9600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.6811 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.6451 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -14.2305 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -11.9825 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -13.8381 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.6853 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 24.3732 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.3853 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1840 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.8274 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5603 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.1655 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2565 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -34.0273 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.2788 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.9743 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 60.8570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.3210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 44.2860 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -0.0344 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.3582 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.3380 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7834 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -13.2053 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -18.1385 -> Clearly below the moving-average trend level.

## TAILWINDS

### Alphabet: You're Getting Anthropic For Free (NASDAQ:GOOG)
- Summary: Alphabet offers free Anthropic access, enhancing AI capabilities.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQbk1hLUV4QUZnNUh6QXd1LVpVY1o0d0tTemNicDNRUHlUYWdTamtSNG9nQ09uaFBZQUUwVl9UWXlmM0hhemhBQmNsWmZRd1g2c1JXN1JLRjRHTWV2ZnJPaTZsMl94OUxNM3lrYlZ3QzE2M2pZWUNjWlNKNU55NEg1ejlJVkRjN0NqZmc?oc=5>

### Alphabet (GOOGL) Expands AI Search With Wallet Data
- Summary: Alphabet launches AI search using wallet data, enhancing user experience and monetization.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOSThiNzctTzdySGZNYlM1bWNra1lQbXNMclhNZm5kR3NtaFdsOXNiOTBPN2F3LVhWb08wdXZPVkxEU015Mkk3M2FTQkg3c3ZrS2dXN1E0NlVWcjJBdjlkUEJhSHd1MzFrTUY2M0wxVDFJLXpzbHpOcUxKbkJ3UmtrUDQzdy1obi1CSHBuMzNSYWVnX2xzMGIwWUJHWFA?oc=5>

### Alphabet Could Be the Safest Way to Own Anthropic. Here’s the Math.
- Summary: Owning Anthropic via Alphabet is portrayed as a safe investment.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxNRXZsWGw1UUgybUlWQmhwcGtDMGJoaEdRTUUtNVV1Q2F0QjhiQzJ0NjdnLU9mV0tncXYzMUFreDBsNXZ4cWpxbHFiUGo3NWpkRk5pa1h4V3kzaV83ZjgxdjZVcXFUUDZmNG1ocHhCMGVSbmZNSHQxakhZaHd2NTBZbFVPcUF4VXV1T2ZiS084SUpCX1lhNHRpd3ZMdXFUOW51SGI5UGtFeEtlLW1JVW1zWE5HVmpYSDVuNkJJV0lSSWUzdUdtRjlienlqdmVHMFdMM0Z1YjhPLW1EZUNlQTdmNkVUbw?oc=5>

### Why Alphabet Stock Is Down Today
- Summary: Alphabet shares fell today, prompting analysis of short-term market dynamics and potential catalysts for the decline.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOaEJ6YjRoVk00LXY5R0dDcHhoN3FiNE1XWl9NZjY2RUJnYzltSTdjZFFDRTdsQ2V4a0JkRGVweFVyZ05GdnF4LTA3NXF3SU9ROUZSUHA5T1RMSTNFN1lNOVJBTjJFMFFmS3Znb182SDZOaHhodWhSR1VEeG1KdkpqcGxhd0dEdnlvUEE1c1U3aVZ1Nk5fRmRyeS1FMzhjZmhfVlF5emdGdExlSUoxVmduMF9IOEZ1NGtTR0Fn?oc=5>

## HEADWINDS

### Alphabet Stock Slips: What's Going On?
- Summary: Alphabet Stock Slips: What's Going On?
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxONzV3WFpHQl90VnFfWjdzeTQ5VVNhMkVaNVFzTHZfZWE4VGd6UFNzNHF0Y2JsbkJqMVNod05lLWZIUlVXUEtKY0ctQ2kycXRwSVVscVpvcjhlNlplXzhkYVlKbHd6ZmJ0UWFXLTNHSEpBbXkyVFFkWFdXN01TT054SUNndVNJbW9uT2lOLTZJTlQ3Vlh2d1VNbU5lRVc?oc=5>

### Why Alphabet Stock Fell Today (Hint: It's AI-Related)
- Summary: Alphabet shares fall, likely due to AI-related market reactions.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTFBkeThCOUJKVXM5alhlRV9IV08ycTRLZmdwWDlWVkJ1M1ViVnhOSG9tNkxtVkhoRW15VG1hUUthYmNwUEpCYTVwOG9nWGYzdFQyZUthaHhULXJFdDhsLUQwWU9tdjhPQzQ2eXl2QVBIUTQyRXEwYlpZVWhtdjI?oc=5>

### Jim Lebenthal Says This Is "a Correction, Not Something Worse." Why He's Buying More Alphabet
- Summary: Analyst Jim Lebenthal views the dip as a correction and signals increased buying interest in Alphabet shares.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxQeFBvTGdNOS1fcW9mZGRKcVhIZXVmeFZ4OGpIdDEyRzhaV0FlOXRtN2FUNFEtVXJvR0FNQlozZTVvZ0RDVDQ5TGMyc0hSa21HaXhTUUlJVjNKMzM1dDZsRDRsODE5ZGdqN0lwVzZPV3k5azZBQ1JFcHZOT2dSS2dBTEx2ZTQwLWVWb1FTMGtrRlV1bGZETndibTJwRWlId2o4OV9ja3dFc19lRWtlUWY5MVh4SzlLVU5PUkUxcmpyLWwxSWZRUHZnVmJKVzg?oc=5>

## CATALYSTS

### Alphabet (GOOGL) Stock Gets Fair Value Trim As Analysts Weigh AI Spending And Monetization
- Summary: Alphabet (GOOGL) Stock Gets Fair Value Trim As Analysts Weigh AI Spending And Monetization
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxON3V6WEZ5MTczaE84bktQaVNVMWY0d1ZBTDZhZW92R2pQX2RzUnZZYVJ4bzVCMTA4R0Mtbk9hUWV0cnJSdkh2MktNVjAyaFJMTVB1NEFram1EcnlqOVRHdWRMa1kwUDBJWEhRZ0ZVRkxVV0FabGtVa1NCREhWMjBkZ1N2c29mYzVodFV4T2RXdUJCMGRzQmF1MzEzTQ?oc=5>

### Alphabet stock plunges as Google walks away from a big Australian news deal
- Summary: Alphabet stock plunges as Google walks away from a big Australian news deal
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxNRHppYVF4UlRjVERuWnA5WUNMVTNTUVJNNWY5Q2RzZmZUNGJXNFZ3SW5XdkJ4cXZORFdxbEZ2R1dSN3BrVGhtcENqUC12bm9fNGlueE50S3BiNDNDdHZId1FmQjZ1Rkx0MnFiMVpZYndnQmsybEQ4Rnk2RlZiay0tdmdJd3JKVi1aVmpkQ2V4M2VrcW4xbGpHUDNPWkhEcmxlVW04OGRwUTRRaUNxclNMUjFiVEhnQ1lnZ1JhNnZ6clVIbWV0clZ3U1hzNDJDWFVC?oc=5>

### 2 Ways Anthropic's IPO Pays Off for Alphabet Investors
- Summary: Anthropic's IPO benefits Alphabet investors, boosting confidence in AI investments.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQRFRkTWhBMG5wR3h0N2huX2tqYVVydUoxVWIxWFZFYzZEdVV3MDRCYjh0dnQ5cWlEejhFRlpBRjNvWnN2NEpfam1iRXYwQ3NhaUlqczhITXM5T3lVZV9BaXk4bWl0bzlVYWxVc1ludTF2UjlySE14T0c4YS1ROE1yNjlGTHhsdURrNnVWWW00UGVGMmxISE1vczFUM3dtZw?oc=5>

## RISKS

### What Does Alphabet (GOOGL) Need To Prove After The Air Force Cloud Breach?
- Summary: Alphabet faces scrutiny over a recent Air Force cloud breach, raising concerns about data security and compliance.
- Date: 2026-11-27 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPbDAxWkxlMzZsOW5RVmxldklXYkJvUldtSUFxS2UzQ2xoQXhpa0FpTzg3Yjc0NldfV3RUMDkzVzBMVXFIdnduWG5hVTI5ZXo0Q3lDT1ZqM0gwQWhVTEkzbnd3by1yN0lBOTdNTDh6dE8tSjJnRFUwWE10OVNMZlAzUERMNnMxMkl0NXZDNWVSZVJVVzlraEFmcWVR?oc=5>

### Is Google Services Still the Prime Earnings Engine for Alphabet Stock?
- Summary: Analysis questions whether Google Services remains the main driver of Alphabet's earnings.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxQNGhyZXZKamVLM3RIUjU0dXgyWU1MVzhEMXJzRUpxMXpwRFpCczNQRkMzM3RUSEFsa2J2YlE2cWRMS3lQQWs2blpVZkVnaF82Yml4RElFTFY3Q3g5QjNPVFZEWFlhWjlaSFViS2JtcTdpSTYxaFBfN2FQSHNIVUNHbFY4MUZkLWFGRmtfN1hqbkI5STFDRGgzLXNfME9uXzdyTm83bFY4NU9rY01pcXRmTXVROXRNUFo3YjYwN200dVR2ZFBuTVhWNmVDMm5uYU1pZ0stM2NyalRvMzdKTmU1SnVWZUNtRXZkUlE?oc=5>

### Alphabet (GOOGL) Dropped, So What Is Behind The Latest Attention?
- Summary: Alphabet shares fell, prompting speculation about underlying factors affecting investor sentiment.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPTTRkV2JVajZXY2tLRGZwanVWWXBweVhseHFZS2k1Rmlic3dvNVViQ0xPSDVYVFdOTC1GSy1aYUg1cXdpazRkZHJrYjJPR3dVRi1Sd0RuVDZ3WUthVDRnUGVPUjFRSFN1OWJXMFdQQkdEUzVoNmlVTVY2Q0Frejh2Ql9HaTJxSTlQMHFNeEhIOHhqR09OdEJqRmRTRUZoSVl0Vkc4?oc=5>

### Alphabet Stocks Move Lower as Record Credit Spreads Shadow AI Spending
- Summary: Alphabet shares declined amid widening credit spreads that dampen AI investment enthusiasm.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxQd3U1STJHb2dZMXNJelNIS21xV2dwWFF0Zm1OMnFfcG40Y1JiQnE3Qmo2WWhWQ3QycExHUER4ZDF3RGFaVldqMTRFTzNIbHZvYVZ3bkZlQjJoM1RZQmZyM1dlNzZxVEdwNWExbW9wanhkRVNZNDRkV3dJZlpIUXpuTy1mM1pldndLWnpXc2w2SWI2b0EwVkNrYnVQZGJuR1dOa0NUOWFxdEZFYWxvWDhwRmkxd3hQQkJqc1NGaGhYTzczZWdDcU1wcVpn?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GOOGL** | **14.36** | **5.13** | **17.70** | **24.70** | **3,380,358,152,192.00 USD** | **-13.84** |
| META | 20.75 | 5.90 | 14.12 | 26.10 | 1,607,773,454,336.00 USD | -0.40 |
| MSFT | 25.72 | 7.78 | 18.13 | 18.80 | 3,660,000,002,048.00 USD | 2.36 |
| AMZN | 20.54 | 4.48 | 15.99 | 12.10 | 2,747,834,564,608.00 USD | 10.89 |

Peers fetched as_of: 2026-11-27; GOOGL reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

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

- https://news.google.com/rss/articles/CBMiigFBVV95cUxQbk1hLUV4QUZnNUh6QXd1LVpVY1o0d0tTemNicDNRUHlUYWdTamtSNG9nQ09uaFBZQUUwVl9UWXlmM0hhemhBQmNsWmZRd1g2c1JXN1JLRjRHTWV2ZnJPaTZsMl94OUxNM3lrYlZ3QzE2M2pZWUNjWlNKNU55NEg1ejlJVkRjN0NqZmc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOSThiNzctTzdySGZNYlM1bWNra1lQbXNMclhNZm5kR3NtaFdsOXNiOTBPN2F3LVhWb08wdXZPVkxEU015Mkk3M2FTQkg3c3ZrS2dXN1E0NlVWcjJBdjlkUEJhSHd1MzFrTUY2M0wxVDFJLXpzbHpOcUxKbkJ3UmtrUDQzdy1obi1CSHBuMzNSYWVnX2xzMGIwWUJHWFA?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxNRXZsWGw1UUgybUlWQmhwcGtDMGJoaEdRTUUtNVV1Q2F0QjhiQzJ0NjdnLU9mV0tncXYzMUFreDBsNXZ4cWpxbHFiUGo3NWpkRk5pa1h4V3kzaV83ZjgxdjZVcXFUUDZmNG1ocHhCMGVSbmZNSHQxakhZaHd2NTBZbFVPcUF4VXV1T2ZiS084SUpCX1lhNHRpd3ZMdXFUOW51SGI5UGtFeEtlLW1JVW1zWE5HVmpYSDVuNkJJV0lSSWUzdUdtRjlienlqdmVHMFdMM0Z1YjhPLW1EZUNlQTdmNkVUbw?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOaEJ6YjRoVk00LXY5R0dDcHhoN3FiNE1XWl9NZjY2RUJnYzltSTdjZFFDRTdsQ2V4a0JkRGVweFVyZ05GdnF4LTA3NXF3SU9ROUZSUHA5T1RMSTNFN1lNOVJBTjJFMFFmS3Znb182SDZOaHhodWhSR1VEeG1KdkpqcGxhd0dEdnlvUEE1c1U3aVZ1Nk5fRmRyeS1FMzhjZmhfVlF5emdGdExlSUoxVmduMF9IOEZ1NGtTR0Fn?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxONzV3WFpHQl90VnFfWjdzeTQ5VVNhMkVaNVFzTHZfZWE4VGd6UFNzNHF0Y2JsbkJqMVNod05lLWZIUlVXUEtKY0ctQ2kycXRwSVVscVpvcjhlNlplXzhkYVlKbHd6ZmJ0UWFXLTNHSEpBbXkyVFFkWFdXN01TT054SUNndVNJbW9uT2lOLTZJTlQ3Vlh2d1VNbU5lRVc?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTFBkeThCOUJKVXM5alhlRV9IV08ycTRLZmdwWDlWVkJ1M1ViVnhOSG9tNkxtVkhoRW15VG1hUUthYmNwUEpCYTVwOG9nWGYzdFQyZUthaHhULXJFdDhsLUQwWU9tdjhPQzQ2eXl2QVBIUTQyRXEwYlpZVWhtdjI?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxQeFBvTGdNOS1fcW9mZGRKcVhIZXVmeFZ4OGpIdDEyRzhaV0FlOXRtN2FUNFEtVXJvR0FNQlozZTVvZ0RDVDQ5TGMyc0hSa21HaXhTUUlJVjNKMzM1dDZsRDRsODE5ZGdqN0lwVzZPV3k5azZBQ1JFcHZOT2dSS2dBTEx2ZTQwLWVWb1FTMGtrRlV1bGZETndibTJwRWlId2o4OV9ja3dFc19lRWtlUWY5MVh4SzlLVU5PUkUxcmpyLWwxSWZRUHZnVmJKVzg?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxON3V6WEZ5MTczaE84bktQaVNVMWY0d1ZBTDZhZW92R2pQX2RzUnZZYVJ4bzVCMTA4R0Mtbk9hUWV0cnJSdkh2MktNVjAyaFJMTVB1NEFram1EcnlqOVRHdWRMa1kwUDBJWEhRZ0ZVRkxVV0FabGtVa1NCREhWMjBkZ1N2c29mYzVodFV4T2RXdUJCMGRzQmF1MzEzTQ?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxNRHppYVF4UlRjVERuWnA5WUNMVTNTUVJNNWY5Q2RzZmZUNGJXNFZ3SW5XdkJ4cXZORFdxbEZ2R1dSN3BrVGhtcENqUC12bm9fNGlueE50S3BiNDNDdHZId1FmQjZ1Rkx0MnFiMVpZYndnQmsybEQ4Rnk2RlZiay0tdmdJd3JKVi1aVmpkQ2V4M2VrcW4xbGpHUDNPWkhEcmxlVW04OGRwUTRRaUNxclNMUjFiVEhnQ1lnZ1JhNnZ6clVIbWV0clZ3U1hzNDJDWFVC?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQRFRkTWhBMG5wR3h0N2huX2tqYVVydUoxVWIxWFZFYzZEdVV3MDRCYjh0dnQ5cWlEejhFRlpBRjNvWnN2NEpfam1iRXYwQ3NhaUlqczhITXM5T3lVZV9BaXk4bWl0bzlVYWxVc1ludTF2UjlySE14T0c4YS1ROE1yNjlGTHhsdURrNnVWWW00UGVGMmxISE1vczFUM3dtZw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPbDAxWkxlMzZsOW5RVmxldklXYkJvUldtSUFxS2UzQ2xoQXhpa0FpTzg3Yjc0NldfV3RUMDkzVzBMVXFIdnduWG5hVTI5ZXo0Q3lDT1ZqM0gwQWhVTEkzbnd3by1yN0lBOTdNTDh6dE8tSjJnRFUwWE10OVNMZlAzUERMNnMxMkl0NXZDNWVSZVJVVzlraEFmcWVR?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxQNGhyZXZKamVLM3RIUjU0dXgyWU1MVzhEMXJzRUpxMXpwRFpCczNQRkMzM3RUSEFsa2J2YlE2cWRMS3lQQWs2blpVZkVnaF82Yml4RElFTFY3Q3g5QjNPVFZEWFlhWjlaSFViS2JtcTdpSTYxaFBfN2FQSHNIVUNHbFY4MUZkLWFGRmtfN1hqbkI5STFDRGgzLXNfME9uXzdyTm83bFY4NU9rY01pcXRmTXVROXRNUFo3YjYwN200dVR2ZFBuTVhWNmVDMm5uYU1pZ0stM2NyalRvMzdKTmU1SnVWZUNtRXZkUlE?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPTTRkV2JVajZXY2tLRGZwanVWWXBweVhseHFZS2k1Rmlic3dvNVViQ0xPSDVYVFdOTC1GSy1aYUg1cXdpazRkZHJrYjJPR3dVRi1Sd0RuVDZ3WUthVDRnUGVPUjFRSFN1OWJXMFdQQkdEUzVoNmlVTVY2Q0Frejh2Ql9HaTJxSTlQMHFNeEhIOHhqR09OdEJqRmRTRUZoSVl0Vkc4?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxQd3U1STJHb2dZMXNJelNIS21xV2dwWFF0Zm1OMnFfcG40Y1JiQnE3Qmo2WWhWQ3QycExHUER4ZDF3RGFaVldqMTRFTzNIbHZvYVZ3bkZlQjJoM1RZQmZyM1dlNzZxVEdwNWExbW9wanhkRVNZNDRkV3dJZlpIUXpuTy1mM1pldndLWnpXc2w2SWI2b0EwVkNrYnVQZGJuR1dOa0NUOWFxdEZFYWxvWDhwRmkxd3hQQkJqc1NGaGhYTzczZWdDcU1wcVpn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
