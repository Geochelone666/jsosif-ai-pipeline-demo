# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-08**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-08**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-09T04:40:13.572081+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 2, 'ai': 14, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261108T041758Z-43fb2458/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 8 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 27.27%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 375.4400 |
| Return 1D (%) | 6.3268 |
| Return 1W (%) | -7.5567 |
| Return 1M (%) | -22.1563 |
| Return YTD (%) | 24.5161 |
| Return 1Y (%) | 31.1760 |
| Annualized volatility (%) | 41.5764 |
| Beta vs SPY | 2.1733 |
| Max drawdown (%) | -27.3158 |
| Sharpe (rf=0) | 0.8634 |
| Downside deviation (rf=0, %) | 28.7301 |
| Sortino (rf=0) | 1.2495 |
| Historical VaR 95% (1D, %) | 4.2423 |
| Historical ES 95% (1D, %) | 5.7594 |
| Correlation vs SPY | 0.7083 |
| Tracking error vs SPY (%) | 33.3789 |
| P/E (trailing) | 24.33 |
| P/B | 71.65 |
| EV/EBITDA | 3.43 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 16.05 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 58.66 |
| Return on equity (%) | 41.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 431.3714 |
| Close vs MA50 (%) | -12.9659 |
| MA200 | 400.0292 |
| Close vs MA200 (%) | -6.1468 |
| RSI (14, Wilder) | 36.2810 |
| MACD (12,26) | -15.4204 |
| MACD signal (9) | -9.1187 |
| MACD histogram | -6.3017 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 375.4400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 6.3268 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.5567 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -22.1563 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 24.5161 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 31.1760 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.5764 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 28.7301 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.2495 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2423 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.7594 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7083 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.3789 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1733 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.3158 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8634 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.0545 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 58.6550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8550 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 24.3318 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.2810 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -6.3017 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -12.9659 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.1468 -> Clearly below the moving-average trend level.

## TAILWINDS

### TSMC Surges 7% as Taiwan Restricts Short Selling to Halt Brutal Semiconductor Crash
- Summary: TSMC shares jump 7% after Taiwan limits short selling, stabilizing the semiconductor market.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxNM2hZUDk1T3U3OEw2NkpBWHdaclZhNWlEUTZmVU9SOW8zVWctaXFJRFAwSzhlOUpDN0VOdHhLZ21FZ2kwQlliTVJxYnQ4LWJSYndSdWNsa3p3dUlSUldjRV9wZGFaQ25PaEtVSWFuUDFMUC16ZEJjZ2JlQzduZlExTGo0X0JJUnFHRWM4ZTZhVHEtb3hfRzhtREJXQVhxb0dvcjZZcEE1SmlPaFl0enU4Zi1ZaDM4ZDdra2pKdUtROVNSVXotSlB2TlFDczFwSG90?oc=5>

### This Stock Is a Nearly Guaranteed Winner From the AI Infrastructure Buildout
- Summary: Positive outlook due to AI infrastructure growth.
- Date: 2026-11-08 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQOHFaNnRxVnB4Y2hCYThnWlVsUTgwRmVWdjlya0ZuSlR3cGxfYVM3a2VEMXVMTjgxczBpQ1dXa3JwbkxKQlROQnczMHlDbVlWOU16WFZyOGUzTEMwempIRmdaVElESjdOakk0ZWRSTGZMNDREdzdwR3YyRU83UU05XzlfTDFpUUthZ25UY0l3aGpFWlhKNUU0?oc=5>

### Taiwan Semiconductor Manufacturing Company Ltd. $TSM Stock: Brighton Jones LLC Grows Position
- Summary: Brighton Jones LLC increases its stake in TSM.
- Date: 2026-11-08 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxORGxtMlZNaWhYeFV6NURFc09CQjVEbDFaa1UwSW9SaERyOGtBZWF1VHFSR1JUazI5alozN19SWi1Zbmw2X0d3SmVMQTZpUWs5RC05cVk3UHlScW9jU0RsNHl2a2VTV3VLOXBKeC01VmRlYTJOWGo3dlY3dmpUV2VyMEJBY20yTTBZYWZscUZibUh5YnF1ZXRqUUQ2bHUyNWQwalZ1NU83TS10RE85eDFCNVdEU1ZHengtaVpUa2ROV2tUNDJLdzV2c1FpLUNBV1FJUHpPN1lyYjAzSEZCWnhJaXFMNHRFQQ?oc=5>

### Taiwan Semiconductor Stocks Jump 7.45% as Taiwan Slashes Short Selling After Rout
- Summary: TSM shares surge 7.45% after Taiwan reduces short selling.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxNUFIzRHlhNU1SeEliNWFWRXBkWjg0b1NwVTBqamJLQzdQcTg0T0pWcktpNHhibHVIMlBzVWdRTzU0YnNDWGtUaG5makgtLXhmaGVISXdjcmRZRDZaYnRRX0E3QTM2eTFMWjNfRUhhSlYyZ1MtWjBiczNSQzd0U1V4M0dSaWpaM3NZS3UxX0dJZmZiQ3dnR3BkX3lZZXREakE5N3BoWlFHQ2FhaGZVZ1VPNVIzNG9JYkFaUG0xcjdNMjZsd0hlR1l1Z0xNcFQ0bzZZS2h0cmVCMA?oc=5>

## HEADWINDS

### TSM Stock at 21x After a 30% Chip Sell-Off [2026]
- Summary: TSM stock priced high amid 30% chip sell‑off.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxOX1FqWGlaSkMzLUctRzBxaV92YzNySE9mQmFHVjhsS2FIVkVpQ0pkZkU1czBKLUtJQ0pMSGRkd08yT1o3N2ZXR1RWdnZPT0VackxCSlRNMXdNUTY2VVVkRmNzWUNqTEF2M0VCM0dibFFMVzdXNy01MUM1U3dLdmpFcGxaUQ?oc=5>

### TSMC Sinks 10%, UMC Down 16% as Chip Rout Deepens After Democrats’ Midterm Wins
- Summary: TSM stock falls 10% during chip rout post‑midterms.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNcmtKWTVlcVpNd3cyUm50T3VoNG5tbjB0NUI3QWhkS2tZVEY1dFZzak9lWmU5UjBJRUtleUp5dlR1R0g3bTdlOWQ4ajhKaTZzbk9BSzhTWGF6c1FPUDJUU1JES0Z0S01uZkN1XzFWRmN5Q1p5Y1NwSTR5bHFZeVhJS2hweDEtcFNmM09HSUxWT0Q?oc=5>

### TSMC Stocks Move Lower as November Sales Data Face a $53.3 Billion Quarterly Hurdle
- Summary: TSMC shares fell due to sales data challenges, indicating a short-term market decline.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNN21ieWNIWmt1ZzdET1pneEZqX0hEbTRkSE1MTUlLbDhHYUhTRlVhM1lQbEFuSVl4YVA3Mko3YjJWREduclIyT3NUV1RuSXhSbTdwV0xZbFgxLTZoTk8wSG40ejRxUlZpRGJTc2VOV1pQUHpPcjA5dmEzTlJPMUJneUNCNzBUbHFsbzByWEJwbFU2T013d1pyRXplY3M?oc=5>

## CATALYSTS

### Taiwan Semiconductor Manufacturing Company Ltd. $TSM Stock Bought by Kornitzer Capital Management Inc. KS
- Summary: Taiwan Semiconductor Manufacturing Company Ltd. $TSM Stock Bought by Kornitzer Capital Management Inc. KS
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi9gFBVV95cUxPd2hkdmczaE9hMnJZamtMbS1HbEtyRzBScmFtZnBnVWpmOE8yN0hXSkxkaDh1cEtQaVFvN0VhOXF4bENkeFBVWVJBNWtYWlA1VF9Mb21rcEVQcF9sTTdKbWM1YTdnSFFGdFp6MktRdTl1Uk5LZjZfU2pmWGhTSGdYYnBBY0k3aEVtempkb1NxbzFrNXhSTXBfZWxMRUxQeGZkNHNlX19Pa3V5OTJzZ3JoeXhRSTNGRndYY2JpejhUSWtVbHMxMkJuanFiN3FGMVVvejl2WFo4UEZCTDJfNzlGa3lYckt5UTl4Vk5GVHkyYUhuN2VfYVE?oc=5>

### Taiwan Semiconductor Manufacturing Company Ltd. $TSM Stock Acquired by Ethic Inc.
- Summary: Taiwan Semiconductor Manufacturing Company Ltd. $TSM Stock Acquired by Ethic Inc.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQTm5kZUdNQUhEN0RDQ2FrSUNaclBrbTl3OTg2eGhpMkxVRURoZThENWlXZkRTXzRIVzl2ZW0yaVl0dEs1ajhMcFVNZmVCOHh0a3lxUklwdklwWmlZUnljUC1nNm1oZmlUdW1jOHlyWWF0MTJxQWhHM3AwMnZPY3NKN01waUszdDB1aVRpR1RxYVdZUi0xREdHbTd2d1IxemJrRVVBR1otaHN5QXc0VGFDWFQ2ZTg2d1piT1dnZ1czdVlnMDNrRzhfMHVwTjdjdGdybUJOQVlR?oc=5>

### TSMC’s AI Opportunity Is Expanding. Here’s the Question That Matters for Its Stock Price
- Summary: Explores TSMC's growing AI prospects and their impact on stock valuation.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxQTE91N3lqQmhwTnRpMEdqcC1WTFk1blNhSzZHVHRZOUd3dGhUNEU5TGFWZUxVb3FmNWJKazVvY095RS1nV0tGWWdJR0ZPYWxFT2MycURzeXN6aEpkeENCcFYwYXVUSjRqbS1sMl9GQWtSdGZySXdjQ0tXb1dOTmxoZXo5RGlTX016bGhxSTFoYk9VS3pnaEdDc2FMa3J5THNmNDNrVkpLSGdKOEs2ZjJ4ODVqeEUydFdtQUpZdmN1aVlXdWI2THZDZw?oc=5>

### Nvidia vs. Taiwan Semiconductor: The AI Revolution Is Big Enough for Both. Here's the Better Buy.
- Summary: Recommends TSM as a better investment over Nvidia.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPTDNYN2cxV2pHRDRoZm0tUEFobGpnYzBKMUtlbUgwMFF1TklfMU9ZbkpFQnZCamZYVXY4dWFpTVRWUFhmczRvSi1TRnpNOUlpMlZGNnRQaWNpYzBzY1VqaVhUeVBpR0tYOXpuTGlZejhkVlZ5d18takN1ZGdTSkV5MHFTZm1FYVdNYUl0NW9RS3JMMWVJc3MwWA?oc=5>

### TSMC rises on report of potential push into advanced memory for Nvidia
- Summary: TSM shares rise due to potential advanced memory push for Nvidia.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNRGNTQTdxUFhhMmJMcEpnNUcwdldseWVRTmIyREZtblRncFM3cld4Y2VISnRhWW9rVDdPVHMwaDNVVFNsRjZTZmxaRXZhcm1idmk0NGZPTjlwMHJCdWwxSTBidVh5Vy1ZTjlfeDNBUjQzSDQwV1kweUlJMDdVeV9IVnRteEVsRTBhNmVfUVBUT1FqamRSN1F4RGswdXU?oc=5>

### Taiwan Semiconductor (TSM) Sees $146.2 Million in Net ETF Buying on Nov. 3
- Summary: Net ETF buying of $146.2M indicates institutional confidence in TSM.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOTHZJQ3FxWHdoRHdCWW50TmE3bzNNVGpiVDFKenBjZEdfWHpWaU16QlFCWmZaejVIcDFlNnFFY0tCQ19vZXczbURkd0p0M3h5YktDRWxhbk94R0Qwd3lldGdlazcwbzdwY1NibnRtdFJRdFhidmJnY1BUMG42VnBYZmFLclZYY0hDbDcyYUlNRGMxWUxPVnNHME9uMVFzNEk?oc=5>

### Taiwan Semiconductor Manufactur (TSM) Stock Forecasts
- Summary: Provides stock forecast for TSM.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQU241b0xoOWFLMWx3UzJKT0FhNjR5RXJGbFY5LWxjVzFoM2Ezdm03U3hfRVh3LThvRzJyVWJjVW5nWG16RkN0a2p3LVJLR0JFTEtLVUpBWTVuWThuNUV2R3RtWnV2aHU1cUFrT25uZXllb1dzc3VVdkxEZF9FTzlGRUw2XzVjX2c5N0JRSw?oc=5>

### TSMC Makes the Chips for Both Nvidia and AMD. Here's What a $5,000 Investment Could Be Worth by 2030.
- Summary: TSMC manufactures chips for Nvidia and AMD, indicating a partnership with major clients.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQMXFsYkRzLWZITVoyRGlFX0szVFlyNzVCVWNBTnJtX2c0YW1PU28yMVNlcm1FVDlZajFRRGhBVTJnWkVOWXl5Yk9OZXNLS29DT3J5ZllaR0JOdTZBV3BqbzYxcUE2LVIxeThFNjlka0NfaGxmMjdtOGtZVHRIMDZfbXRvWm9kekxDXzlLb3pDVmFIZmp6NkJpag?oc=5>

### TSMC Jumped 6% on a Report It Could Make Memory Chips for Nvidia
- Summary: TSMC may produce memory chips for Nvidia, boosting its product portfolio.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNLThISkFpaFQ2b3BIQVVMTXFDcWdTX3d4ZnFzQVFEc2U3WGRNZUp1dlkwZmc5V29vQUVGcXZCZ3Y5X2RTRGltWC0wdkNia1VnM2pCZFlLdXFRV1UyM3lWZ2tDWUZ2Y21Bc1hrcktOUGNmRFlNSFlWNmRNVGdXekxNNkJueHdkOWtkU29yeHBERkV4RGc0azJONTJzTERxT0JOaXJValBKb1RQSzg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **24.33** | **71.65** | **3.43** | **50.90** | **1,947,209,826,304.00 USD** | **31.18** |
| UMC | 13.07 | 2.39 | -0.31 | 25.60 | 34,732,945,408.00 USD | 92.80 |
| GFS | 110.34 | 1.80 | 10.35 | 12.50 | 21,528,670,208.00 USD | 12.65 |
| INTC | N/A | 2.60 | 16.30 | 20.90 | 299,128,193,024.00 USD | 51.13 |

Peers fetched as_of: 2026-11-08; TSM reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-08

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMi0AFBVV95cUxNM2hZUDk1T3U3OEw2NkpBWHdaclZhNWlEUTZmVU9SOW8zVWctaXFJRFAwSzhlOUpDN0VOdHhLZ21FZ2kwQlliTVJxYnQ4LWJSYndSdWNsa3p3dUlSUldjRV9wZGFaQ25PaEtVSWFuUDFMUC16ZEJjZ2JlQzduZlExTGo0X0JJUnFHRWM4ZTZhVHEtb3hfRzhtREJXQVhxb0dvcjZZcEE1SmlPaFl0enU4Zi1ZaDM4ZDdra2pKdUtROVNSVXotSlB2TlFDczFwSG90?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQOHFaNnRxVnB4Y2hCYThnWlVsUTgwRmVWdjlya0ZuSlR3cGxfYVM3a2VEMXVMTjgxczBpQ1dXa3JwbkxKQlROQnczMHlDbVlWOU16WFZyOGUzTEMwempIRmdaVElESjdOakk0ZWRSTGZMNDREdzdwR3YyRU83UU05XzlfTDFpUUthZ25UY0l3aGpFWlhKNUU0?oc=5
- https://news.google.com/rss/articles/CBMi9AFBVV95cUxNb2pWZXZBUTAyaUhhVy1VLWhzRkE3NkhNYi1vcmpJdTNMZHhuNl9HR1JpbnEyV2p0dWNnbWpKQ2JxTFR1b3p4U1JqOXpGcV8zc1JaY0R6SVBhTkR4dE5LWC1uZExHNUdKa1lySVE0NGx6N3JOVjZaUnlsSVVUNF9jOU5XbTUyWFNzRUZaczBOclVNcTROUnExemd1cXdYQTlGY3BTeVNLMjh2T1FpczZVRURNUTB4eW9DVldwUkZraUpZdEM5TGZLYUZIT3RXbDdvTFVyVmtaNmN0bmphSDdKeUxJdVotckNTUDgxLTA2eW9zWnJY?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxORGxtMlZNaWhYeFV6NURFc09CQjVEbDFaa1UwSW9SaERyOGtBZWF1VHFSR1JUazI5alozN19SWi1Zbmw2X0d3SmVMQTZpUWs5RC05cVk3UHlScW9jU0RsNHl2a2VTV3VLOXBKeC01VmRlYTJOWGo3dlY3dmpUV2VyMEJBY20yTTBZYWZscUZibUh5YnF1ZXRqUUQ2bHUyNWQwalZ1NU83TS10RE85eDFCNVdEU1ZHengtaVpUa2ROV2tUNDJLdzV2c1FpLUNBV1FJUHpPN1lyYjAzSEZCWnhJaXFMNHRFQQ?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxNUFIzRHlhNU1SeEliNWFWRXBkWjg0b1NwVTBqamJLQzdQcTg0T0pWcktpNHhibHVIMlBzVWdRTzU0YnNDWGtUaG5makgtLXhmaGVISXdjcmRZRDZaYnRRX0E3QTM2eTFMWjNfRUhhSlYyZ1MtWjBiczNSQzd0U1V4M0dSaWpaM3NZS3UxX0dJZmZiQ3dnR3BkX3lZZXREakE5N3BoWlFHQ2FhaGZVZ1VPNVIzNG9JYkFaUG0xcjdNMjZsd0hlR1l1Z0xNcFQ0bzZZS2h0cmVCMA?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxOX1FqWGlaSkMzLUctRzBxaV92YzNySE9mQmFHVjhsS2FIVkVpQ0pkZkU1czBKLUtJQ0pMSGRkd08yT1o3N2ZXR1RWdnZPT0VackxCSlRNMXdNUTY2VVVkRmNzWUNqTEF2M0VCM0dibFFMVzdXNy01MUM1U3dLdmpFcGxaUQ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNcmtKWTVlcVpNd3cyUm50T3VoNG5tbjB0NUI3QWhkS2tZVEY1dFZzak9lWmU5UjBJRUtleUp5dlR1R0g3bTdlOWQ4ajhKaTZzbk9BSzhTWGF6c1FPUDJUU1JES0Z0S01uZkN1XzFWRmN5Q1p5Y1NwSTR5bHFZeVhJS2hweDEtcFNmM09HSUxWT0Q?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNN21ieWNIWmt1ZzdET1pneEZqX0hEbTRkSE1MTUlLbDhHYUhTRlVhM1lQbEFuSVl4YVA3Mko3YjJWREduclIyT3NUV1RuSXhSbTdwV0xZbFgxLTZoTk8wSG40ejRxUlZpRGJTc2VOV1pQUHpPcjA5dmEzTlJPMUJneUNCNzBUbHFsbzByWEJwbFU2T013d1pyRXplY3M?oc=5
- https://news.google.com/rss/articles/CBMi9gFBVV95cUxPd2hkdmczaE9hMnJZamtMbS1HbEtyRzBScmFtZnBnVWpmOE8yN0hXSkxkaDh1cEtQaVFvN0VhOXF4bENkeFBVWVJBNWtYWlA1VF9Mb21rcEVQcF9sTTdKbWM1YTdnSFFGdFp6MktRdTl1Uk5LZjZfU2pmWGhTSGdYYnBBY0k3aEVtempkb1NxbzFrNXhSTXBfZWxMRUxQeGZkNHNlX19Pa3V5OTJzZ3JoeXhRSTNGRndYY2JpejhUSWtVbHMxMkJuanFiN3FGMVVvejl2WFo4UEZCTDJfNzlGa3lYckt5UTl4Vk5GVHkyYUhuN2VfYVE?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQTm5kZUdNQUhEN0RDQ2FrSUNaclBrbTl3OTg2eGhpMkxVRURoZThENWlXZkRTXzRIVzl2ZW0yaVl0dEs1ajhMcFVNZmVCOHh0a3lxUklwdklwWmlZUnljUC1nNm1oZmlUdW1jOHlyWWF0MTJxQWhHM3AwMnZPY3NKN01waUszdDB1aVRpR1RxYVdZUi0xREdHbTd2d1IxemJrRVVBR1otaHN5QXc0VGFDWFQ2ZTg2d1piT1dnZ1czdVlnMDNrRzhfMHVwTjdjdGdybUJOQVlR?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxQTE91N3lqQmhwTnRpMEdqcC1WTFk1blNhSzZHVHRZOUd3dGhUNEU5TGFWZUxVb3FmNWJKazVvY095RS1nV0tGWWdJR0ZPYWxFT2MycURzeXN6aEpkeENCcFYwYXVUSjRqbS1sMl9GQWtSdGZySXdjQ0tXb1dOTmxoZXo5RGlTX016bGhxSTFoYk9VS3pnaEdDc2FMa3J5THNmNDNrVkpLSGdKOEs2ZjJ4ODVqeEUydFdtQUpZdmN1aVlXdWI2THZDZw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPTDNYN2cxV2pHRDRoZm0tUEFobGpnYzBKMUtlbUgwMFF1TklfMU9ZbkpFQnZCamZYVXY4dWFpTVRWUFhmczRvSi1TRnpNOUlpMlZGNnRQaWNpYzBzY1VqaVhUeVBpR0tYOXpuTGlZejhkVlZ5d18takN1ZGdTSkV5MHFTZm1FYVdNYUl0NW9RS3JMMWVJc3MwWA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNRGNTQTdxUFhhMmJMcEpnNUcwdldseWVRTmIyREZtblRncFM3cld4Y2VISnRhWW9rVDdPVHMwaDNVVFNsRjZTZmxaRXZhcm1idmk0NGZPTjlwMHJCdWwxSTBidVh5Vy1ZTjlfeDNBUjQzSDQwV1kweUlJMDdVeV9IVnRteEVsRTBhNmVfUVBUT1FqamRSN1F4RGswdXU?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOTHZJQ3FxWHdoRHdCWW50TmE3bzNNVGpiVDFKenBjZEdfWHpWaU16QlFCWmZaejVIcDFlNnFFY0tCQ19vZXczbURkd0p0M3h5YktDRWxhbk94R0Qwd3lldGdlazcwbzdwY1NibnRtdFJRdFhidmJnY1BUMG42VnBYZmFLclZYY0hDbDcyYUlNRGMxWUxPVnNHME9uMVFzNEk?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQU241b0xoOWFLMWx3UzJKT0FhNjR5RXJGbFY5LWxjVzFoM2Ezdm03U3hfRVh3LThvRzJyVWJjVW5nWG16RkN0a2p3LVJLR0JFTEtLVUpBWTVuWThuNUV2R3RtWnV2aHU1cUFrT25uZXllb1dzc3VVdkxEZF9FTzlGRUw2XzVjX2c5N0JRSw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQMXFsYkRzLWZITVoyRGlFX0szVFlyNzVCVWNBTnJtX2c0YW1PU28yMVNlcm1FVDlZajFRRGhBVTJnWkVOWXl5Yk9OZXNLS29DT3J5ZllaR0JOdTZBV3BqbzYxcUE2LVIxeThFNjlka0NfaGxmMjdtOGtZVHRIMDZfbXRvWm9kekxDXzlLb3pDVmFIZmp6NkJpag?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNLThISkFpaFQ2b3BIQVVMTXFDcWdTX3d4ZnFzQVFEc2U3WGRNZUp1dlkwZmc5V29vQUVGcXZCZ3Y5X2RTRGltWC0wdkNia1VnM2pCZFlLdXFRV1UyM3lWZ2tDWUZ2Y21Bc1hrcktOUGNmRFlNSFlWNmRNVGdXekxNNkJueHdkOWtkU29yeHBERkV4RGc0azJONTJzTERxT0JOaXJValBKb1RQSzg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
