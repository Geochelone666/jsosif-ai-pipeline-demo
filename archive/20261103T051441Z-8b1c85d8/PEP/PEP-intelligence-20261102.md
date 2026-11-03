# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:23:00.736973+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 20, 'rule': 5, 'ai': 6, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 20 unique headlines; 10 named publishers; 2 exact duplicates; 20 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 140.4200 |
| Return 1D (%) | 2.2426 |
| Return 1W (%) | 3.6616 |
| Return 1M (%) | 11.5418 |
| Return YTD (%) | 0.8184 |
| Return 1Y (%) | 0.0135 |
| Annualized volatility (%) | 21.2241 |
| Beta vs SPY | -0.2464 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | 0.1877 |
| Downside deviation (rf=0, %) | 14.1598 |
| Sortino (rf=0) | 0.2813 |
| Historical VaR 95% (1D, %) | 2.0913 |
| Historical ES 95% (1D, %) | 2.6375 |
| Correlation vs SPY | -0.1489 |
| Tracking error vs SPY (%) | 26.3795 |
| P/E (trailing) | 17.66 |
| P/B | 8.59 |
| EV/EBITDA | 12.12 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 16.25 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.88 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.73 |
| MA50 | 133.1636 |
| Close vs MA50 (%) | 5.4492 |
| MA200 | 143.7003 |
| Close vs MA200 (%) | -2.2828 |
| RSI (14, Wilder) | 66.2069 |
| MACD (12,26) | 1.6429 |
| MACD signal (9) | 0.7357 |
| MACD histogram | 0.9072 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 140.4200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.2426 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.6616 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 11.5418 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 0.8184 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.0135 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.2241 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.1598 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2813 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0913 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6375 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1489 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.3795 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.2464 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1877 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.2546 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.8830 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.7264 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.6629 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 66.2069 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.9072 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.4492 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -2.2828 -> Slightly below the moving-average trend level.

## TAILWINDS

### PepsiCo (NASDAQ:PEP) Stock Price Up 2.2% - What's Next?
- Summary: PepsiCo (NASDAQ:PEP) Stock Price Up 2.2% - What's Next?
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOX0V0QmNORTZKUmdFaW93WUdXYURCLVhQSkxjNlIxOEQ1SEdOQnRoZjRsOXRZeWtWMmVja3AwaF9yUmpPc2Z2dGxCWFFUMS1mTUo0SHdsVkxNQkl5WUtCVHF2WEU1QmkwVDMzODZxWmhvU0JudUp0LXl1Z0FCYW9jY01QejhyZzN1QkJzS1ZvN0duTm41UkljMi12ajhfbUpoRW1XbXMyLVVXZ1U?oc=5>

### Is PepsiCo Stock Stronger Than It Looks?
- Summary: Questioning PepsiCo’s stock strength suggests potential undervaluation and future upside for investors.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQdGI1al9tWm5HV2dzcWcxOWtxbWg5Rm9rMlFSWldnZG9tb3Nib2VNZXAxa0RXVVlxcnp3am9DN1J6TmFYNzBVazVaUmh0cnAyZlJSVWRyNVhuVHhpaXJKVURfWGllQjVmZnhhM09OUkVVdTFHWDBfcmIxRUIwd0FKNTFiNV9fZ2VQU2NGcncyYnRCV2dsNTQyQ1E4RVI3UUxS?oc=5>

### Coca-Cola Yields Just 2.2% Compared to 4.3% for PepsiCo. Here's the Better Dividend King Stock for Generating Long-Term Passive Income.
- Summary: PepsiCo offers a higher dividend yield than Coca-Cola, positioning it as a more attractive income stock for long-term investors.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxON0NhSHRndFp3TWVQZlFmNWU2Yy13LThiTmd5OUdqRFllLTI1UXR0aEJBVVhXeVVmSDlTb0F4M19lR3prYVVvRHFpZGh0OXNGbk9Qc01FRWIybVJyTFhpMlJwa1YxUUpZQmVKSnl5ZG1lRTYwQUoyY0I0QTNMTG92Z3hndmFZbUZ3dGdiUnRCdlJ5Z1E?oc=5>

### PepsiCo (PEP) Stock May Be Worth More On Its Supply Chain Reset
- Summary: Analysts suggest supply chain reset could boost PepsiCo’s valuation.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNcWJTVndPbTdlcEFvZ1JyZmJPSUVpR1NKSGFOeHFiWUlzRXVGQTd6akxfbmQzUG54Q0VnR2pQVVVQRG5zODhIRHFrZEZsLXRMSGQzeF9DcUloRVBBUnJ5MlRaeEpRYnpQbmVUZl9BWjd2TkRiS1ZmVjFkd2h3NFNtUEVvQW1feGppS2JTZkUxZ2NNcTNhMVBHTi1TalpLVEVQQjZmOUFwSk1jRFoyV2pDaUhHLUpkNE5QUkIxSjNYbmwwRUNtbnNZUy1UMElTOExQX29XRtIB2gFBVV95cUxOaUR5dGVLRGxsbkJHS3dZNFV6T2tocE12Qk5LVUotTGR3WTFySWtJQm55SDV3ZXo0YUV1LThWNTY2V0ZiMm5rZGFuTms2WXFxb19kaVg2RHh6OEo5M3FtVmZqMmxGU296YnhjNmx0cEFWUV84cmpKLTY4dEVEMUFGbC1WRXZNbFg1LWlibzh2Unp3T2xLOE9sTlBQYlQtMm8xMi11UU1IRXh0bzNMb3psQ2VUMTZoQjkwN19IZkd5ZS1hZFFVa3lUbEtjWERIU21PODMtM21GVFNLZw?oc=5>

### PepsiCo Generated Strong FCF - Huge, Unusual Put Options Volume Trade Today is a Bullish Signal
- Summary: PepsiCo reported strong free cash flow, with unusual put option volume indicating bullish sentiment.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPUmlrdHkzbGZWX3o4ekk3ZGNHaWZlalJvN2g2bUxFY3dod040ZVFoTzBsWW5rU1ZHTVlla1NjYVNCUk45bmxuSWJPam5wQWs4MUtObFJSdVFVM2lUb01XNVRjYTBDdDByc1pNd083dnpaOTFaaXVjSGNobVhudTdRZk5yLS1kQU5wdDNFalJ2UHcxR3RydTl0OXRMV1A4Y3Fi?oc=5>

### What PepsiCo (PEP)'s Taco Bell Renewal Means For Shareholders
- Summary: PepsiCo renewed its partnership with Taco Bell, potentially boosting revenue and shareholder value.
- Date: 2026-11-02 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQUHJLQXc1b2xhR28yWV8zb1NwM0FpVFJKbEpJY083T2w2OXU2WENIX0R4UG1PUTdtMFkzWnkxMldNb04wOWNIWXJNR1I3UnRoSmZaeWIxQ0I0NGwzcHV1U0R2S0pEZFFDX3pGbHZKb0lCM1VrcGcwMmloUmxJNUJVcUJvOGQ4ckZaLUtYdV96SmpfbXdWcWxxNG9UTFU1c2NjLUVCSXVReXRObXRlLWJfOWM1STB5dG80XzROYnlMcy1uaE42SEtaLTNhX1NHYnV5dEHSAdcBQVVfeXFMT1U0LTFBdUZIelU2SU5xTzZJdGt2Yy12bDZfNVZBREROekx4dnd2Y0p2MmkyVUFRSjVHMUpzLWZrQXVoZEJtaEpOMFlfNWxta3dqMk5JcF9yTlFTQnNIUE5FRDYtWXdYS3ZfcnNsU21veEVKNzJxbTNQY1ZLaDZ3cjJzRU5yUW1VMlNDT195TmJOX25yUVp0VHJsazNGcXpXdmc5T1NDd1lrVDRoUkZJU3FmUzVWWXlUdHFzT0xSa2tWbmFKODhUYmVCN2FRTjdWdW5ucmhnZDQ?oc=5>

## HEADWINDS

### Why Is PepsiCo Stock Falling, and Is It a Buying Opportunity?
- Summary: PepsiCo shares are declining, raising concerns about short-term performance.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQZnptbTE5THpPQURPOTIwZEhMbTdLdjg2RTl6Skd5LUo4MjBfU04xNi13dDdCSEViOU1xV2laWmpzdGNrU3d0aVg2UV9MYmxINm1XVUs4NmFLNEhMdTczX185N3RCU0I3dDhTREtxVGlnNHpSVjRMajhmamw5ZHhVTmpHUm51VFU2LVdWRk1aZV8?oc=5>

## CATALYSTS

### PepsiCo (PEP) Stock Looks Below Fair Value After A Choppy Year
- Summary: PepsiCo (PEP) Stock Looks Below Fair Value After A Choppy Year
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNZzY1UzBpLS14VFl2UVBpU1FJYXJJRU9BaTNibm9OQkFQQ3g5NTZBWVNOUk9xRHV5dVptYmJYYnlwa0RpYUpuVGZvTmNqV09YcUpWSXk4YjNVNDFub0hQcXJRMGwweHJRSTR5eHBRam9uQmNXdHdLLVp6X0M2R2Zlb3k1UjlzRzl2YUt0VVJaeGtLUmhrYUJUaENB?oc=5>

### PepsiCo Hasn't Been This Cheap Relative to Earnings in 6 Years. Here's Why That's the Signal to Buy.
- Summary: PepsiCo Hasn't Been This Cheap Relative to Earnings in 6 Years. Here's Why That's the Signal to Buy.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPMklRamY4NTlwSXBhcnNLbjVrWjU0VnVPYTc3WG9NY1NianJJZVN4b2JRWmpHcktGYm5rVHJiU3h6dk9DTVhqLTVleEd3LTZqWmozQlQ2WWxsYkc3d2piTVVfel9VMF9qdjA3YmNveTdKRVlyOFc0TDk3cDMxSnZudEU3SzRKdG92UE16ZVNHYlUxTFB4N3Uw?oc=5>

### PepsiCo, Inc. $PEP Stock Sold by Heritage Investors Management Corp
- Summary: PepsiCo, Inc. $PEP Stock Sold by Heritage Investors Management Corp
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQdzQzOGNNVGNELW5xaXFyLWw5Q1gydHdJcG5mRFFGemIxV2hzSk9tekZlMmlHNEM1REhsbkM0ZG5jczZBbDktaEsxMERhbDR5Ym15cjNhTFNmLV90QVo4all0OEFJMjdiUDBWMllNajFFQzJqNUpCbTA5M0pZOUhKYlRUVTNRcjRLSVZEMWRoS3pYSl9faHhmLTlrYVJhUEFlcGt1TXJZUDVGOHBmSGd5bng5YTl0dmlkamIzX3NOZkZ1Z3c?oc=5>

### PepsiCo, Inc. $PEP Stock Sold by Summit Global Investments
- Summary: PepsiCo, Inc. $PEP Stock Sold by Summit Global Investments
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOUlVzM3l5ejBhRmxQcXhNaGp0UGQ5T0Y1VWJKVk5VZE9sa3lvNno4V1BNZFBIS1pYdkhEb1dydEY4cUhnR2VXOS00QlZ3eHFubVZ1eHhJSGJWdmswU2FQT0xQZmxaWXdZT3p3eXY0THVER0djWU9LSWJZZlJkdC1OV3RPYVI5X1RoY1A5SF9YN0cxcnhvdlp0RDNrSHlXTXdCR2pYd2h6SkZvUXRpNWFybDU4OXZMU28?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **17.66** | **8.59** | **12.12** | **5.60** | **191,356,108,800.00 USD** | **0.01** |
| KO | 28.27 | 11.03 | 25.24 | 7.40 | 412,251,324,416.00 USD | 42.78 |
| MNST | 43.65 | 10.05 | 30.94 | 20.20 | 94,073,667,584.00 USD | 43.71 |
| KDP | 36.10 | 2.00 | 18.87 | 75.60 | 50,105,614,336.00 USD | 39.89 |

Peers fetched as_of: 2026-11-02; PEP reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-08
- Revenue (latest available single quarter): 25,274,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,048,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/77476/000007747626000048/pep-20260905.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOX0V0QmNORTZKUmdFaW93WUdXYURCLVhQSkxjNlIxOEQ1SEdOQnRoZjRsOXRZeWtWMmVja3AwaF9yUmpPc2Z2dGxCWFFUMS1mTUo0SHdsVkxNQkl5WUtCVHF2WEU1QmkwVDMzODZxWmhvU0JudUp0LXl1Z0FCYW9jY01QejhyZzN1QkJzS1ZvN0duTm41UkljMi12ajhfbUpoRW1XbXMyLVVXZ1U?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQdGI1al9tWm5HV2dzcWcxOWtxbWg5Rm9rMlFSWldnZG9tb3Nib2VNZXAxa0RXVVlxcnp3am9DN1J6TmFYNzBVazVaUmh0cnAyZlJSVWRyNVhuVHhpaXJKVURfWGllQjVmZnhhM09OUkVVdTFHWDBfcmIxRUIwd0FKNTFiNV9fZ2VQU2NGcncyYnRCV2dsNTQyQ1E4RVI3UUxS?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxON0NhSHRndFp3TWVQZlFmNWU2Yy13LThiTmd5OUdqRFllLTI1UXR0aEJBVVhXeVVmSDlTb0F4M19lR3prYVVvRHFpZGh0OXNGbk9Qc01FRWIybVJyTFhpMlJwa1YxUUpZQmVKSnl5ZG1lRTYwQUoyY0I0QTNMTG92Z3hndmFZbUZ3dGdiUnRCdlJ5Z1E?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNcWJTVndPbTdlcEFvZ1JyZmJPSUVpR1NKSGFOeHFiWUlzRXVGQTd6akxfbmQzUG54Q0VnR2pQVVVQRG5zODhIRHFrZEZsLXRMSGQzeF9DcUloRVBBUnJ5MlRaeEpRYnpQbmVUZl9BWjd2TkRiS1ZmVjFkd2h3NFNtUEVvQW1feGppS2JTZkUxZ2NNcTNhMVBHTi1TalpLVEVQQjZmOUFwSk1jRFoyV2pDaUhHLUpkNE5QUkIxSjNYbmwwRUNtbnNZUy1UMElTOExQX29XRtIB2gFBVV95cUxOaUR5dGVLRGxsbkJHS3dZNFV6T2tocE12Qk5LVUotTGR3WTFySWtJQm55SDV3ZXo0YUV1LThWNTY2V0ZiMm5rZGFuTms2WXFxb19kaVg2RHh6OEo5M3FtVmZqMmxGU296YnhjNmx0cEFWUV84cmpKLTY4dEVEMUFGbC1WRXZNbFg1LWlibzh2Unp3T2xLOE9sTlBQYlQtMm8xMi11UU1IRXh0bzNMb3psQ2VUMTZoQjkwN19IZkd5ZS1hZFFVa3lUbEtjWERIU21PODMtM21GVFNLZw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPUmlrdHkzbGZWX3o4ekk3ZGNHaWZlalJvN2g2bUxFY3dod040ZVFoTzBsWW5rU1ZHTVlla1NjYVNCUk45bmxuSWJPam5wQWs4MUtObFJSdVFVM2lUb01XNVRjYTBDdDByc1pNd083dnpaOTFaaXVjSGNobVhudTdRZk5yLS1kQU5wdDNFalJ2UHcxR3RydTl0OXRMV1A4Y3Fi?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQUHJLQXc1b2xhR28yWV8zb1NwM0FpVFJKbEpJY083T2w2OXU2WENIX0R4UG1PUTdtMFkzWnkxMldNb04wOWNIWXJNR1I3UnRoSmZaeWIxQ0I0NGwzcHV1U0R2S0pEZFFDX3pGbHZKb0lCM1VrcGcwMmloUmxJNUJVcUJvOGQ4ckZaLUtYdV96SmpfbXdWcWxxNG9UTFU1c2NjLUVCSXVReXRObXRlLWJfOWM1STB5dG80XzROYnlMcy1uaE42SEtaLTNhX1NHYnV5dEHSAdcBQVVfeXFMT1U0LTFBdUZIelU2SU5xTzZJdGt2Yy12bDZfNVZBREROekx4dnd2Y0p2MmkyVUFRSjVHMUpzLWZrQXVoZEJtaEpOMFlfNWxta3dqMk5JcF9yTlFTQnNIUE5FRDYtWXdYS3ZfcnNsU21veEVKNzJxbTNQY1ZLaDZ3cjJzRU5yUW1VMlNDT195TmJOX25yUVp0VHJsazNGcXpXdmc5T1NDd1lrVDRoUkZJU3FmUzVWWXlUdHFzT0xSa2tWbmFKODhUYmVCN2FRTjdWdW5ucmhnZDQ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQZnptbTE5THpPQURPOTIwZEhMbTdLdjg2RTl6Skd5LUo4MjBfU04xNi13dDdCSEViOU1xV2laWmpzdGNrU3d0aVg2UV9MYmxINm1XVUs4NmFLNEhMdTczX185N3RCU0I3dDhTREtxVGlnNHpSVjRMajhmamw5ZHhVTmpHUm51VFU2LVdWRk1aZV8?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQZ3pMSk05S3QyZ2QyMkpGOUZ4VjlaMmtxV3BZVVBHTE13Z2xLcUI2WTYzS2xOeHk3WW5pcV9SQVoyLVQ2Zm5CaXdqQmJhaWdMRWFFUGhNR0hQOEdzbHZtMFRIX1Q5VFhYdDJiRS05SWdLLU5jVjlzbk9rWFpIaTYwQzlMdzFkTlBYdFpMR08tSXotTjFJd2xkeWVRTTVkdw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNZzY1UzBpLS14VFl2UVBpU1FJYXJJRU9BaTNibm9OQkFQQ3g5NTZBWVNOUk9xRHV5dVptYmJYYnlwa0RpYUpuVGZvTmNqV09YcUpWSXk4YjNVNDFub0hQcXJRMGwweHJRSTR5eHBRam9uQmNXdHdLLVp6X0M2R2Zlb3k1UjlzRzl2YUt0VVJaeGtLUmhrYUJUaENB?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPMklRamY4NTlwSXBhcnNLbjVrWjU0VnVPYTc3WG9NY1NianJJZVN4b2JRWmpHcktGYm5rVHJiU3h6dk9DTVhqLTVleEd3LTZqWmozQlQ2WWxsYkc3d2piTVVfel9VMF9qdjA3YmNveTdKRVlyOFc0TDk3cDMxSnZudEU3SzRKdG92UE16ZVNHYlUxTFB4N3Uw?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQdzQzOGNNVGNELW5xaXFyLWw5Q1gydHdJcG5mRFFGemIxV2hzSk9tekZlMmlHNEM1REhsbkM0ZG5jczZBbDktaEsxMERhbDR5Ym15cjNhTFNmLV90QVo4all0OEFJMjdiUDBWMllNajFFQzJqNUpCbTA5M0pZOUhKYlRUVTNRcjRLSVZEMWRoS3pYSl9faHhmLTlrYVJhUEFlcGt1TXJZUDVGOHBmSGd5bng5YTl0dmlkamIzX3NOZkZ1Z3c?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOUlVzM3l5ejBhRmxQcXhNaGp0UGQ5T0Y1VWJKVk5VZE9sa3lvNno4V1BNZFBIS1pYdkhEb1dydEY4cUhnR2VXOS00QlZ3eHFubVZ1eHhJSGJWdmswU2FQT0xQZmxaWXdZT3p3eXY0THVER0djWU9LSWJZZlJkdC1OV3RPYVI5X1RoY1A5SF9YN0cxcnhvdlp0RDNrSHlXTXdCR2pYd2h6SkZvUXRpNWFybDU4OXZMU28?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
