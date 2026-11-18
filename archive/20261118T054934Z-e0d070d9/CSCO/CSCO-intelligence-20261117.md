# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:14:52.990211+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 6, 'ai': 10, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 6 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 76.0%; oldest publication 2026-11-11

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 95.1100 |
| Return 1D (%) | 0.6242 |
| Return 1W (%) | -3.0973 |
| Return 1M (%) | -11.4350 |
| Return YTD (%) | 25.7572 |
| Return 1Y (%) | 24.5446 |
| Annualized volatility (%) | 37.0882 |
| Beta vs SPY | 1.2971 |
| Max drawdown (%) | -27.2567 |
| Sharpe (rf=0) | 0.7801 |
| Downside deviation (rf=0, %) | 26.2111 |
| Sortino (rf=0) | 1.1038 |
| Historical VaR 95% (1D, %) | 3.2126 |
| Historical ES 95% (1D, %) | 5.5834 |
| Correlation vs SPY | 0.4820 |
| Tracking error vs SPY (%) | 32.7531 |
| P/E (trailing) | 25.16 |
| P/B | 7.28 |
| EV/EBITDA | 18.82 |
| Revenue growth (%) | 24.40 |
| Forward P/E (estimate) | 15.70 |
| Gross margin (%) | 64.07 |
| Operating margin (%) | 27.17 |
| Return on equity (%) | 30.38 |
| Free cash flow yield (%) | 2.89 |
| MA50 | 107.0391 |
| Close vs MA50 (%) | -11.1446 |
| MA200 | 101.9050 |
| Close vs MA200 (%) | -6.6680 |
| RSI (14, Wilder) | 37.0936 |
| MACD (12,26) | -3.5804 |
| MACD signal (9) | -3.0041 |
| MACD histogram | -0.5763 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 95.1100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.6242 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.0973 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.4350 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 25.7572 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 24.5446 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.0882 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.2111 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1038 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2126 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.5834 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4820 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.7531 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2971 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.2567 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7801 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.7029 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.0660 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.1660 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 30.3800 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.8893 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.1614 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 37.0936 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.5763 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -11.1446 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.6680 -> Clearly below the moving-average trend level.

## TAILWINDS

### Cisco upgraded to Buy at HSBC as firm sees 'attractive valuation' (CSCO:NASDAQ)
- Summary: Cisco upgraded to Buy at HSBC as firm sees 'attractive valuation' (CSCO:NASDAQ)
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPaG5CX1poZ0t3MEsyRjk0SGVNNmdEYWRjQkdYX3g2TU9RUHJ3bGs3SHp6UTZnVnQ5R2RodTlYY3lwRk82SXM1elhGaThlcEFGRTluOUkzQ1d2bDk0UzdQMGNPSGg2NERYNGZ1ZldzWjQyOWppQVFUeG9RM0xPeUQxemxybmV0NWpXcW9GdTUxd2hpaUJYc3JXTzFKM1FpWE5GZU5F?oc=5>

### Cisco Systems Delivers Record Q1 Results, Raises FY27 Outlook
- Summary: Cisco Systems Delivers Record Q1 Results, Raises FY27 Outlook
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNRVcxQXB4NnpKcjdLV2NnTHNveFFIUnllVU9ZSDdReG9iSnJMRTJKRExTSmhWNDNRLTloM1g0MjZYaXh0S2NfdjlMeWNxdnUwRnlTaTg1czdsZTF5Z2tkOVg2RkJ5U19qR0ZVRVJOWDlWTFE2cG1wSlR2Q2ZOODcwcnFvb2V0ZU9mSTFKV1NtelFhWnlEWHlPZEhzdTNRdw?oc=5>

### Cisco Systems (CSCO) Q1 Earnings and Revenues Beat Estimates
- Summary: Cisco Systems (CSCO) Q1 Earnings and Revenues Beat Estimates
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQc3NMbXh0VkFHZnEtalpOX055M2haeWpleW5zdFlYVHlpQjJzS2JLY1A1OVBhUzFfbUhQWUlqWHY2U1JEb3hZTTZDR0hqUW9TVkUxNWpFZmlMckRfZS05TUZIRjBRT3NFTjh2OXpQRUdqRFVFemNlOVdHa0pIalJ6VVRkWWs1ejM1RkdnZ25SZ2FGMU5vSVNBZzF3OA?oc=5>

### Cisco beats on earnings, says AI infrastructure revenue will double this fiscal year
- Summary: Cisco exceeded earnings expectations, projecting AI infrastructure revenue to double this fiscal year.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMickFVX3lxTFBXZ1VHS3FlM0xwR1ctNVZGd255am4zdHdQUUhBVjdyRmVoRy05RkZPcGQ2RUgzUFVsSlk1YTQ5aUZTM1lhZmFPT2lXUXY4NzcwanBweWVNN3RMSklUdzBfdDg5MUtfMzY0Qi1FMmpHT19sZ9IBd0FVX3lxTFB0dFNlWHZZSG04enVwQmRHZ3J3LUtIT3ZUdF9ESkVzZExBaWJFSTVjcGZxbkFxUVl2VFZ3dkFBTVFVc0dWTG5INTRlMDBqT1VudEJYZ0xOX0NiUzVPSEtoUzhfRlh5bmlMMWZjaHExV0dPTVBra2hv?oc=5>

## HEADWINDS

### Cisco Stocks Fall 5.29% as AI Networking Mix Squeezes Gross Margins
- Summary: Cisco Stocks Fall 5.29% as AI Networking Mix Squeezes Gross Margins
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOTHpSRFcxQ044ZXdXUDR6TkJYWDU4Z2hoMjJLSk9XTm9NN3hVYTBqY3hiUW5OTjNUVWlLcWZPU0lMYTBlSlowbHhSVFQ3SExOY0dQcUF6X2ppWkI1U09YTzdqeW8zS1o4VEZaQzdZTXoyOFd4OGdOWnpTNTRFa2tEOGlmU1J0MFVRQ2F0Zld0aVU?oc=5>

## CATALYSTS

### Cisco (CSCO) Stock Gets Fair Value Trim As Analysts Cut Targets After Strong Q1
- Summary: Cisco (CSCO) Stock Gets Fair Value Trim As Analysts Cut Targets After Strong Q1
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOd0psSW1iRElNXzlmeTI0QTZrM1J1UU5QaUJnS1J4NXFMYzhMM2dvb3dxeG5zSHRFTG5IRkhPTklXMy1vM01GaDBRSlRYNjQxM3E2aEZtYXlyTEdRR0x3STNMMUlyQ1A4aWNERVNQTW1RazVaZUc2WFJ2UjY1eVVUanA2U3ZGMXZITlRJOVRNeF9QTzhJaHc?oc=5>

### Cisco (CSCO) Reports Q1 Earnings: What Key Metrics Have to Say
- Summary: Cisco (CSCO) Reports Q1 Earnings: What Key Metrics Have to Say
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOTFIyN2F2c28zSndhdFk0UUtQcHlpZTNEbkpYdFdsSmpsYzZLZDFOVk0wZzdMWmU5MUhoQnBlUllpbnA2R044dlVhSVd6QXhzQWhZN0FYLVVHRVp5ZloxQ2VrcXUyam1DbF9nMkFwQlJMYXNQQjNacEhJV3NRTk0yRU5qanlQd1pHRjdmd2NmeXh3SXp2T3lNZFRlVQ?oc=5>

### Cisco: Better Earnings, Cheaper Stock (NASDAQ:CSCO)
- Summary: Cisco reports improved earnings and a lower stock price, indicating stronger financial performance and potential upside for investors.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxOQW1JNjZlRklwSUJiX3pwLW13UG5WZF9NbTc3Mlk4dmhTeUNReWlfLWloUFNrbG5GY3ZfczdIZ0tHbUI0VGZ4dGFub252Z3dfMTdGX0ZDQi1LRVVxYW1wdkhlLXRhbzAyMXhsMHVUcXExRWlHbW52N2EyRlQ0OThlOWhB?oc=5>

### Cisco (CSCO) vs. ANET and HPE: Can AI Networking Turn Strong Orders Into Lasting Earnings Growth?
- Summary: Questioning whether AI networking can convert strong orders into sustained earnings growth.
- Date: 2026-11-12 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQSGozWEcxNGh2Nk0zaHFIbnFXSTg1UGNpWEdSUDdMUHFWdzRreV9meUprdGpHZWpMZTRHdmd2QzVTMXhfWjl6VlhBX3Z4RW5oRGFlT3VqZkV5WUlLbmYyVHppSnlxR0pUbVdfZEFqdlRORHRrcUlaeW1OWlZoMHN5VjNpN0hMdnhQaG5qQXpBTGM?oc=5>

### Ahead of Cisco Earnings, Here's What Barchart Data Says Comes Next for CSCO Stock
- Summary: Market data predicts post-earnings movement.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQOTA3ZmRSaHdoS2dnM1JoMnRtSHVoU01iR25wLWVTN3JXZ1psVWRld2wxeGJDMy1lQnhpTXdEUnBCWjRRbzhHOFlVekx4VmNUUFB6eTdCQnNpcWNFa3BQMzJodU1XRlltM1B4M3BaWW9FWHBDV0hfc05ndnhPXzZ1MnQtMVRsWVliNnp1UUZWem5tTi0yaEJhTm5CSnd5WnljNEE?oc=5>

### US AI Data Centers ‘Are Going to Get Built’ Despite Political Pushback, Says Cisco CEO: ‘Too Important to Our Country’
- Summary: Cisco CEO announces plans to build AI data centers despite political pushback, emphasizing their national importance.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNckJ4NmZvWFF5RVVvbHZJYTRnR2p0aGdEWElXeDR1VEJia2lNcDkyR0luMEoyU0dMd2JKdTZLOFRZVE4xakhwaURfYldpSm1qRmpzbEREbHQ1NmcteDNjR1JyWFdJbnhhTy0zanhGaDRpQTBqeHc0SjFCODJGQ09tWTlPVDlQVi1CRmpmc2lOdXVQUQ?oc=5>

### HSBC Upgrades Cisco Stock (CSCO) to Buy, Cites Attractive Valuation and Business Momentum
- Summary: HSBC upgraded Cisco to Buy, citing attractive valuation and business momentum, signaling positive analyst sentiment.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNM1RaSU1yTklPck5rSF95dkhZUVBDSWUyTzcyOVlXQjdkeWlVUkl1TUtMV01LQ1hLeDdZZ25rUnhFcGxrVW02OGZPdHE3ZDRsQTRSQU8ycTFfYlNQSEFnRi1GS0RXTGMwV3FVRDdadFY3WFRJbXljRUpHbzNBRDdrNGczdnI1VmFJNEhWVjdTMFVESkcyS2U4MnFRRHgxRmNwWUZycUp4b0RXREVlMGlTR3BsZHUyWnc?oc=5>

### Cisco Systems, Inc. (CSCO) Stock Forecasts
- Summary: Analysts predict future stock performance for Cisco.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNd2dxNjJnclhCR195N3JKQnlXd3hFdmZ2bExObjRLSGRlRWEtRkNJVHpLNTFxQXBDMzJGU2J3amVRN2NVWWl5VUtiZnlDd1Q3eEpGbTF2NlczZXlvMTJ0ZllmU0VpNEU1em82a3NmOENJREFpd1c3UlVwYS1pSHhONkFBNVFOWDFZUm4tVA?oc=5>

### Cisco’s Growth May Have Peaked Despite Raised AI Revenue Outlook, Says Citi — Barclays Sees Margins Holding Up
- Summary: Citi raises AI revenue outlook, noting margins remain stable, suggesting potential growth plateau.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQU296WWh2dWhYa0dscGY4S1J1NXctalp4YmhOQWFpOS1id1dORzEyM3B2czB2SjVGWjlQTzIxN2hOMHJTYzFZUFNOR29ZRjY0OVRLalZTdDVQUjhkOTJ3c0JGaVFoc2E1aFFLN3JfTEtzc2JBQUFhZkw3b3l2WEdGQXpEdk0xOWdESEx6aXdrNFkxM2o1OGZmUGZuWDk?oc=5>

### ‘Still Early In Networking Super Cycle’: Cisco Delivers Beat And Raise Quarter But Shares Drop Amid Nvidia-Linked Volatility
- Summary: Cisco beats earnings estimates and raises quarterly guidance, but shares fell due to broader market volatility.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOY19wcldBYlMxclFIWE8zTzY3OEVzWHZKXzRTQjNnNnhIS2Q5M2JySEd2RldMbVJQY2U5bHJKb192Nnp4ZU1jMmlNMkthblBNSWJyUG14NGNDY1FHNW1BMEp1eU5OOC1TYVk4TVMyZTZhVENfUVRfM1djWXBzM0o2S3JvTjU4MFU0dDctVnhNR1RYWlpYajJnMWlxMlU5VTdJ?oc=5>

### Cisco CEO Shrugs Off Concerns On Revenue Guidance Dip, Says ‘Profitability Of The Business Is Incredible’
- Summary: CEO dismisses revenue guidance dip, emphasizing strong profitability.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPeGh0X3ROdDZvMDdHc1dXMVhLblE1Y09rSEkxcmppR2plLVYxa2xnRHRGaENtUThLT3o4R290SklBWlRSSW1VT1NIMkVDRi1EQlFfWDlpSUtzdHk5ZDJCcUxoOFgta1k0bFRwOTVBdHpnd1kyWU94TDdJNkNVR3JyU3hDQzJKeDEzbk1nVHZYZGdiRFhET3REQWxB?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **25.16** | **7.28** | **18.82** | **24.40** | **374,446,194,688.00 USD** | **24.54** |
| ANET | 50.11 | 14.32 | 41.70 | 58.50 | 235,523,473,408.00 USD | 46.49 |
| FFIV | 24.37 | 4.33 | 17.24 | 13.30 | 17,335,875,584.00 USD | 33.46 |
| HPE | 24.01 | 2.31 | 10.94 | 33.70 | 61,182,853,120.00 USD | 121.01 |

Peers fetched as_of: 2026-11-17; CSCO reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-12
- Next expected earnings: 2027-02-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-17
- Revenue (latest available single quarter): 12,844,000,000.00 USD; period 2018-04-29/2018-07-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 4,552,000,000.00 USD; period 2026-07-26/2026-10-24; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/858877/000085887726000185/csco-20261024.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiowFBVV95cUxPaG5CX1poZ0t3MEsyRjk0SGVNNmdEYWRjQkdYX3g2TU9RUHJ3bGs3SHp6UTZnVnQ5R2RodTlYY3lwRk82SXM1elhGaThlcEFGRTluOUkzQ1d2bDk0UzdQMGNPSGg2NERYNGZ1ZldzWjQyOWppQVFUeG9RM0xPeUQxemxybmV0NWpXcW9GdTUxd2hpaUJYc3JXTzFKM1FpWE5GZU5F?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNRVcxQXB4NnpKcjdLV2NnTHNveFFIUnllVU9ZSDdReG9iSnJMRTJKRExTSmhWNDNRLTloM1g0MjZYaXh0S2NfdjlMeWNxdnUwRnlTaTg1czdsZTF5Z2tkOVg2RkJ5U19qR0ZVRVJOWDlWTFE2cG1wSlR2Q2ZOODcwcnFvb2V0ZU9mSTFKV1NtelFhWnlEWHlPZEhzdTNRdw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQc3NMbXh0VkFHZnEtalpOX055M2haeWpleW5zdFlYVHlpQjJzS2JLY1A1OVBhUzFfbUhQWUlqWHY2U1JEb3hZTTZDR0hqUW9TVkUxNWpFZmlMckRfZS05TUZIRjBRT3NFTjh2OXpQRUdqRFVFemNlOVdHa0pIalJ6VVRkWWs1ejM1RkdnZ25SZ2FGMU5vSVNBZzF3OA?oc=5
- https://news.google.com/rss/articles/CBMickFVX3lxTFBXZ1VHS3FlM0xwR1ctNVZGd255am4zdHdQUUhBVjdyRmVoRy05RkZPcGQ2RUgzUFVsSlk1YTQ5aUZTM1lhZmFPT2lXUXY4NzcwanBweWVNN3RMSklUdzBfdDg5MUtfMzY0Qi1FMmpHT19sZ9IBd0FVX3lxTFB0dFNlWHZZSG04enVwQmRHZ3J3LUtIT3ZUdF9ESkVzZExBaWJFSTVjcGZxbkFxUVl2VFZ3dkFBTVFVc0dWTG5INTRlMDBqT1VudEJYZ0xOX0NiUzVPSEtoUzhfRlh5bmlMMWZjaHExV0dPTVBra2hv?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOTHpSRFcxQ044ZXdXUDR6TkJYWDU4Z2hoMjJLSk9XTm9NN3hVYTBqY3hiUW5OTjNUVWlLcWZPU0lMYTBlSlowbHhSVFQ3SExOY0dQcUF6X2ppWkI1U09YTzdqeW8zS1o4VEZaQzdZTXoyOFd4OGdOWnpTNTRFa2tEOGlmU1J0MFVRQ2F0Zld0aVU?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOd0psSW1iRElNXzlmeTI0QTZrM1J1UU5QaUJnS1J4NXFMYzhMM2dvb3dxeG5zSHRFTG5IRkhPTklXMy1vM01GaDBRSlRYNjQxM3E2aEZtYXlyTEdRR0x3STNMMUlyQ1A4aWNERVNQTW1RazVaZUc2WFJ2UjY1eVVUanA2U3ZGMXZITlRJOVRNeF9QTzhJaHc?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOTFIyN2F2c28zSndhdFk0UUtQcHlpZTNEbkpYdFdsSmpsYzZLZDFOVk0wZzdMWmU5MUhoQnBlUllpbnA2R044dlVhSVd6QXhzQWhZN0FYLVVHRVp5ZloxQ2VrcXUyam1DbF9nMkFwQlJMYXNQQjNacEhJV3NRTk0yRU5qanlQd1pHRjdmd2NmeXh3SXp2T3lNZFRlVQ?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxOQW1JNjZlRklwSUJiX3pwLW13UG5WZF9NbTc3Mlk4dmhTeUNReWlfLWloUFNrbG5GY3ZfczdIZ0tHbUI0VGZ4dGFub252Z3dfMTdGX0ZDQi1LRVVxYW1wdkhlLXRhbzAyMXhsMHVUcXExRWlHbW52N2EyRlQ0OThlOWhB?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQSGozWEcxNGh2Nk0zaHFIbnFXSTg1UGNpWEdSUDdMUHFWdzRreV9meUprdGpHZWpMZTRHdmd2QzVTMXhfWjl6VlhBX3Z4RW5oRGFlT3VqZkV5WUlLbmYyVHppSnlxR0pUbVdfZEFqdlRORHRrcUlaeW1OWlZoMHN5VjNpN0hMdnhQaG5qQXpBTGM?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQOTA3ZmRSaHdoS2dnM1JoMnRtSHVoU01iR25wLWVTN3JXZ1psVWRld2wxeGJDMy1lQnhpTXdEUnBCWjRRbzhHOFlVekx4VmNUUFB6eTdCQnNpcWNFa3BQMzJodU1XRlltM1B4M3BaWW9FWHBDV0hfc05ndnhPXzZ1MnQtMVRsWVliNnp1UUZWem5tTi0yaEJhTm5CSnd5WnljNEE?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNckJ4NmZvWFF5RVVvbHZJYTRnR2p0aGdEWElXeDR1VEJia2lNcDkyR0luMEoyU0dMd2JKdTZLOFRZVE4xakhwaURfYldpSm1qRmpzbEREbHQ1NmcteDNjR1JyWFdJbnhhTy0zanhGaDRpQTBqeHc0SjFCODJGQ09tWTlPVDlQVi1CRmpmc2lOdXVQUQ?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNM1RaSU1yTklPck5rSF95dkhZUVBDSWUyTzcyOVlXQjdkeWlVUkl1TUtMV01LQ1hLeDdZZ25rUnhFcGxrVW02OGZPdHE3ZDRsQTRSQU8ycTFfYlNQSEFnRi1GS0RXTGMwV3FVRDdadFY3WFRJbXljRUpHbzNBRDdrNGczdnI1VmFJNEhWVjdTMFVESkcyS2U4MnFRRHgxRmNwWUZycUp4b0RXREVlMGlTR3BsZHUyWnc?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNd2dxNjJnclhCR195N3JKQnlXd3hFdmZ2bExObjRLSGRlRWEtRkNJVHpLNTFxQXBDMzJGU2J3amVRN2NVWWl5VUtiZnlDd1Q3eEpGbTF2NlczZXlvMTJ0ZllmU0VpNEU1em82a3NmOENJREFpd1c3UlVwYS1pSHhONkFBNVFOWDFZUm4tVA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQU296WWh2dWhYa0dscGY4S1J1NXctalp4YmhOQWFpOS1id1dORzEyM3B2czB2SjVGWjlQTzIxN2hOMHJTYzFZUFNOR29ZRjY0OVRLalZTdDVQUjhkOTJ3c0JGaVFoc2E1aFFLN3JfTEtzc2JBQUFhZkw3b3l2WEdGQXpEdk0xOWdESEx6aXdrNFkxM2o1OGZmUGZuWDk?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOY19wcldBYlMxclFIWE8zTzY3OEVzWHZKXzRTQjNnNnhIS2Q5M2JySEd2RldMbVJQY2U5bHJKb192Nnp4ZU1jMmlNMkthblBNSWJyUG14NGNDY1FHNW1BMEp1eU5OOC1TYVk4TVMyZTZhVENfUVRfM1djWXBzM0o2S3JvTjU4MFU0dDctVnhNR1RYWlpYajJnMWlxMlU5VTdJ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPeGh0X3ROdDZvMDdHc1dXMVhLblE1Y09rSEkxcmppR2plLVYxa2xnRHRGaENtUThLT3o4R290SklBWlRSSW1VT1NIMkVDRi1EQlFfWDlpSUtzdHk5ZDJCcUxoOFgta1k0bFRwOTVBdHpnd1kyWU94TDdJNkNVR3JyU3hDQzJKeDEzbk1nVHZYZGdiRFhET3REQWxB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
