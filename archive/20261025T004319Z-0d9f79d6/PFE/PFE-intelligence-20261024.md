# PFE Intelligence Report

- ticker: **PFE**
- Report as_of: **2026-10-24**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/PFE/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PFE/key-statistics/
- AI analysis snapshot as_of: **2026-10-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-25T01:25:57.811754+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 2, 'ai': 6, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 7 named publishers; 0 exact duplicates; 9 HTTPS source links; largest publisher share 22.22%; oldest publication 2026-10-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 30.0300 |
| Return 1D (%) | -1.2820 |
| Return 1W (%) | 1.5213 |
| Return 1M (%) | 6.5649 |
| Return YTD (%) | 26.8273 |
| Return 1Y (%) | 30.2638 |
| Annualized volatility (%) | 21.1939 |
| Beta vs SPY | 0.2450 |
| Max drawdown (%) | -15.7243 |
| Sharpe (rf=0) | 1.3584 |
| Downside deviation (rf=0, %) | 13.6502 |
| Sortino (rf=0) | 2.1092 |
| Historical VaR 95% (1D, %) | 1.9258 |
| Historical ES 95% (1D, %) | 2.5887 |
| Correlation vs SPY | 0.1474 |
| Tracking error vs SPY (%) | 23.0660 |
| P/E (trailing) | 39.51 |
| P/B | 2.01 |
| EV/EBITDA | 8.79 |
| Revenue growth (%) | 2.60 |
| Forward P/E (estimate) | 10.41 |
| Gross margin (%) | 74.72 |
| Operating margin (%) | 27.88 |
| Return on equity (%) | 5.01 |
| Free cash flow yield (%) | 7.29 |
| MA50 | 28.2952 |
| Close vs MA50 (%) | 6.1311 |
| MA200 | 26.1819 |
| Close vs MA200 (%) | 14.6976 |
| RSI (14, Wilder) | 65.6086 |
| MACD (12,26) | 0.5937 |
| MACD signal (9) | 0.4324 |
| MACD histogram | 0.1614 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PFE': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 30.0300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.2820 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.5213 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.5649 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 26.8273 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 30.2638 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.1939 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.6502 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.1092 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.9258 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.5887 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1474 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.0660 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2450 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.7243 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.3584 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.4123 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.8770 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 5.0140 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.2947 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.5132 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 65.6086 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1614 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.1311 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 14.6976 -> Clearly above the moving-average trend level.

## TAILWINDS

### Pfizer’s infant shot could target strains behind about 84% of serious pneumococcal disease in U.S. children under 5
- Summary: Pfizer develops infant vaccine covering 84% of serious pneumococcal strains in U.S. children under 5.
- Date: 2026-10-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPd1NFeEFmbUJBWnExdFRmQ3dSYXdmRktzbURBZmozTmhKQXBsUGp5TUhrTklSeDRJWTc3cUZQYkdfdE5FanptSDhFTWF5blhZWVZXMERFclQ2NUhEMElueld5YVJfUF80eTNjTUFDcFFDbV9OakpRWTJyZGJCaFowWWVyemZrRzRvZlVfRU83WHNDV2JFdFpEaVB3SmtKTHFzek0zMlVHX2dqTEkwWVB6bkllZw?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Pfizer's Stock Is Finally Showing Signs of Life. Could This Be the Start of a Much Bigger Rally?
- Summary: Pfizer's Stock Is Finally Showing Signs of Life. Could This Be the Start of a Much Bigger Rally?
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPcEJfdzlMUl9wcnFZbUpPTWJ6UWRwcG1QWExtV21vS2FuZ1YtUlUtLUQ0VUxqWDZKSlpKYi1FSUVPV1o4RVBramZSaGI0RDZScDd4RnRZWVREX1p5OUJxR0hNbXdnN3JSdXl1a1czZl9vMkc4cUdGUy1xck9RSk1OREZlNGxCQzBPTFB1QzR4MWY4elRsRVI2WTlVbi00TVdtWlE?oc=5>

### Pfizer (PFE) Stock Looks Richly Priced On Current Earnings
- Summary: Pfizer (PFE) Stock Looks Richly Priced On Current Earnings
- Date: 2026-10-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxQNEZmWkFQM0lWTXBLamxnVzRnSWlpcFJqVldvNGRadUlBWll6RlljdlFGcnlOU05JampweElfWFprd1NqaGd0ZmlYV0Y4Nzc3YTR2cVBYRWV4elFoRXRJaFlmR2dDRUt5c2t0M1pCbm9lZC1HMnZ3aFJmWjNXSXZPRjBFNDZZMTBrUXFPeXg3a3NFNGc0ZThKOE9MNjhDN3FqdllVdGFEeU5xSk5ndlV2b2xKdG1NZWpDQWJtSGlXZ0xoUDFDbDJ3Qks2NVljUdIB0wFBVV95cUxNc255NEFUU3h1R0ZTT0t1NzNHQU50WXgyT1lsQldYWnJ0WHdiODlackpqaW5sQ1RjbVR5X25LWUQyVUlha3RDb1hGaWtEVlZPWUFmX3VsY25FbkJVcHNrX0tZYUpjeWZXdzhrNmpBQU95U3BGUWtJNE02VnpVSEtfYlhzclRySHVjUTJRZkxQc0lJaU8xcnJwRzlDRllYdjBUWVpPd0d2d0ZvR3dRZWstMV9fWDJMSGlRRHZ0X2NiY2NRZEpZNVZ0QVhPb1lDUWRpbjZJ?oc=5>

### Pfizer Inc. (PFE) Is a Trending Stock: Facts to Know Before Betting on It
- Summary: Provides general information about Pfizer’s stock performance and key facts for investors.
- Date: 2026-10-20 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPbHdlNnFXOWZIVndoeEt3WTAyU0hTdDB1MnFuWV9JSURsTEJmc0lpQzBGWXY5a3h4dDVDZ2JBb3ZYV2R1c1ZYRThsdGlWTlUydHl4MEktX3J3cXlFOFc2OGluZzFBc0dkWVZsUmFMcWtlTEw0R1RVR3hyN1lfTUgyQXVvWVJ4WE14QV92MzB2TDVzR2FnVkFrckdR?oc=5>

### How To Boost The Dividend Yield On This Drugmaking Behemoth
- Summary: Offers strategies to increase dividend yield for Pfizer shareholders.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNQ0NpWENzSnJwcUxsVVBFMlJBa2wwb0FxOXFXZWtXazZFOEdYajVLTEdCdG0xaV9IMG1aVkp0V19fRVVWMFBLY3dLRDFKdTZqZmlhQ0VSNzBVY3RGZFc3bDdkanlHd3JqbnpDR1FPdWtMZHBISkFvVWFqU3VMZkg4cFozZ0hMVTZHQmxtUEV6ZGlwUEs2dm9lUmVocHg?oc=5>

### What Have Pfizer Stock Holders Really Earned?
- Summary: Analyzes historical returns and earnings for Pfizer stock holders.
- Date: 2026-10-21 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPTHVLY2tkQjdlbnJZV0Rod0wzNjJPbVhtRTNvV0NXTU5pT1JFYkN4Yi1ZTXFlWHQwcl9NTjRqUjlySEs4cDUyNjloeG1kX0hhcFlHQlVHLXhvYTlscWMwMm5nSEZWS3pRYWQwdHU3OVQ3aHA1NXFtLXN3ZTU2UV9hckUzZUZqTHdPOGpoS09wOE1HSjRPOHNwdlM3Xy1Qak5yVEh4WVcyZw?oc=5>

### Pfizer, Inc. (PFE) Stock Forecasts
- Summary: Presents future stock price predictions and analyst forecasts for Pfizer.
- Date: 2026-10-21 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQd1l5Rkg0MmV5UVBUXzFJLU1rLVlYaVFqdkx4U2JoX09OWFdnSmpWMWhnWS1tUGhxcElMdE5iQnZ0VWgzNXNIUzV0R05BX1RTaUY3SUwzZkd0VHRLWGE4R0xqc0FrQjhnM3ZRQXQ1cE0yMXJnRU5Ea2p1VXdPTVdRSGwtMHlBN0NnZ3dJRmRjWGc?oc=5>

### Pfizer (PFE) Showcases IDWeek Data, Is The Stock Fully Priced?
- Summary: Discusses Pfizer’s IDWeek data release and its impact on stock valuation.
- Date: 2026-10-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxOMWhIcHg4bE9FakVhQm9pQkJSYUZyaXJIQWtzN1F6cnpWS3JfcHVrTXpmR2MzcU04OTdGZDRmUUZMdGZmd3RqMFMzSndWLVcxR2dCVU5DREcyeFB2TDBRSkVEeE1SOURacnVGeVVvcXMwMldDU2xDVFllcUZxQW1LUGxTSUJuUnNDN2ZMbUxjQ3IzSFhubEtNX2E3Y1NjektSZW1iREZIUnVhcEtWdkl2ZGQ3NWQ1YXhNOVNQc21sbW4xdHp2U0FFVVl6Mno1MGl40gHWAUFVX3lxTE5GYlVqTE0zbXNTNXZuZWRTX0JuMjNVVy15M1dMcTFpWWp5MnVJaVhkc2FjeXdRYjJ2R2lOMDBxRURyZ2hoUnNIMW91ckdpRDBnbzlDLVlXNmc0RVRlcEFUci12aEh1WUhKZ3R2UC1fd191b3Q3aGtxNldvOUtnb3JfZmpiVXk5akhMdEpJNkZtOXNYMl9Wd2thVDZmMnlmaXBHdHBjMjFOM0hZSW1LX2hJbXR6a0tOdTRCcU9zNFdTMTZJd0Y1clJId1VJUHlzODBQSEJhV3c?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PFE** | **39.51** | **2.01** | **8.79** | **2.60** | **171,161,206,784.00 USD** | **30.26** |
| MRK | 117.15 | 8.55 | 14.04 | 5.10 | 358,406,029,312.00 USD | 71.53 |
| JNJ | 40.03 | 7.79 | 19.20 | 5.90 | 635,072,544,768.00 USD | 40.15 |
| LLY | 42.75 | 33.51 | 28.32 | 47.70 | 1,135,596,929,024.00 USD | 56.08 |

Peers fetched as_of: 2026-10-24; PFE reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-04
- Revenue (latest available single quarter): 15,034,000,000.00 USD; period 2026-03-30/2026-06-28; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): -248,000,000.00 USD; period 2026-03-30/2026-06-28; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/78003/000007800326000095/pfe-20260628.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiswFBVV95cUxPd1NFeEFmbUJBWnExdFRmQ3dSYXdmRktzbURBZmozTmhKQXBsUGp5TUhrTklSeDRJWTc3cUZQYkdfdE5FanptSDhFTWF5blhZWVZXMERFclQ2NUhEMElueld5YVJfUF80eTNjTUFDcFFDbV9OakpRWTJyZGJCaFowWWVyemZrRzRvZlVfRU83WHNDV2JFdFpEaVB3SmtKTHFzek0zMlVHX2dqTEkwWVB6bkllZw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPcEJfdzlMUl9wcnFZbUpPTWJ6UWRwcG1QWExtV21vS2FuZ1YtUlUtLUQ0VUxqWDZKSlpKYi1FSUVPV1o4RVBramZSaGI0RDZScDd4RnRZWVREX1p5OUJxR0hNbXdnN3JSdXl1a1czZl9vMkc4cUdGUy1xck9RSk1OREZlNGxCQzBPTFB1QzR4MWY4elRsRVI2WTlVbi00TVdtWlE?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxQNEZmWkFQM0lWTXBLamxnVzRnSWlpcFJqVldvNGRadUlBWll6RlljdlFGcnlOU05JampweElfWFprd1NqaGd0ZmlYV0Y4Nzc3YTR2cVBYRWV4elFoRXRJaFlmR2dDRUt5c2t0M1pCbm9lZC1HMnZ3aFJmWjNXSXZPRjBFNDZZMTBrUXFPeXg3a3NFNGc0ZThKOE9MNjhDN3FqdllVdGFEeU5xSk5ndlV2b2xKdG1NZWpDQWJtSGlXZ0xoUDFDbDJ3Qks2NVljUdIB0wFBVV95cUxNc255NEFUU3h1R0ZTT0t1NzNHQU50WXgyT1lsQldYWnJ0WHdiODlackpqaW5sQ1RjbVR5X25LWUQyVUlha3RDb1hGaWtEVlZPWUFmX3VsY25FbkJVcHNrX0tZYUpjeWZXdzhrNmpBQU95U3BGUWtJNE02VnpVSEtfYlhzclRySHVjUTJRZkxQc0lJaU8xcnJwRzlDRllYdjBUWVpPd0d2d0ZvR3dRZWstMV9fWDJMSGlRRHZ0X2NiY2NRZEpZNVZ0QVhPb1lDUWRpbjZJ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPbHdlNnFXOWZIVndoeEt3WTAyU0hTdDB1MnFuWV9JSURsTEJmc0lpQzBGWXY5a3h4dDVDZ2JBb3ZYV2R1c1ZYRThsdGlWTlUydHl4MEktX3J3cXlFOFc2OGluZzFBc0dkWVZsUmFMcWtlTEw0R1RVR3hyN1lfTUgyQXVvWVJ4WE14QV92MzB2TDVzR2FnVkFrckdR?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNQ0NpWENzSnJwcUxsVVBFMlJBa2wwb0FxOXFXZWtXazZFOEdYajVLTEdCdG0xaV9IMG1aVkp0V19fRVVWMFBLY3dLRDFKdTZqZmlhQ0VSNzBVY3RGZFc3bDdkanlHd3JqbnpDR1FPdWtMZHBISkFvVWFqU3VMZkg4cFozZ0hMVTZHQmxtUEV6ZGlwUEs2dm9lUmVocHg?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPTHVLY2tkQjdlbnJZV0Rod0wzNjJPbVhtRTNvV0NXTU5pT1JFYkN4Yi1ZTXFlWHQwcl9NTjRqUjlySEs4cDUyNjloeG1kX0hhcFlHQlVHLXhvYTlscWMwMm5nSEZWS3pRYWQwdHU3OVQ3aHA1NXFtLXN3ZTU2UV9hckUzZUZqTHdPOGpoS09wOE1HSjRPOHNwdlM3Xy1Qak5yVEh4WVcyZw?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQd1l5Rkg0MmV5UVBUXzFJLU1rLVlYaVFqdkx4U2JoX09OWFdnSmpWMWhnWS1tUGhxcElMdE5iQnZ0VWgzNXNIUzV0R05BX1RTaUY3SUwzZkd0VHRLWGE4R0xqc0FrQjhnM3ZRQXQ1cE0yMXJnRU5Ea2p1VXdPTVdRSGwtMHlBN0NnZ3dJRmRjWGc?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxOMWhIcHg4bE9FakVhQm9pQkJSYUZyaXJIQWtzN1F6cnpWS3JfcHVrTXpmR2MzcU04OTdGZDRmUUZMdGZmd3RqMFMzSndWLVcxR2dCVU5DREcyeFB2TDBRSkVEeE1SOURacnVGeVVvcXMwMldDU2xDVFllcUZxQW1LUGxTSUJuUnNDN2ZMbUxjQ3IzSFhubEtNX2E3Y1NjektSZW1iREZIUnVhcEtWdkl2ZGQ3NWQ1YXhNOVNQc21sbW4xdHp2U0FFVVl6Mno1MGl40gHWAUFVX3lxTE5GYlVqTE0zbXNTNXZuZWRTX0JuMjNVVy15M1dMcTFpWWp5MnVJaVhkc2FjeXdRYjJ2R2lOMDBxRURyZ2hoUnNIMW91ckdpRDBnbzlDLVlXNmc0RVRlcEFUci12aEh1WUhKZ3R2UC1fd191b3Q3aGtxNldvOUtnb3JfZmpiVXk5akhMdEpJNkZtOXNYMl9Wd2thVDZmMnlmaXBHdHBjMjFOM0hZSW1LX2hJbXR6a0tOdTRCcU9zNFdTMTZJd0Y1clJId1VJUHlzODBQSEJhV3c?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
