# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:58:11.624874+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 4, 'ai': 11, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 10 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 47.83%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 100.7600 |
| Return 1D (%) | 2.6592 |
| Return 1W (%) | -2.7507 |
| Return 1M (%) | -14.8915 |
| Return YTD (%) | 33.2278 |
| Return 1Y (%) | 43.1117 |
| Annualized volatility (%) | 36.8936 |
| Beta vs SPY | 1.2454 |
| Max drawdown (%) | -27.2567 |
| Sharpe (rf=0) | 1.1606 |
| Downside deviation (rf=0, %) | 25.4279 |
| Sortino (rf=0) | 1.6840 |
| Historical VaR 95% (1D, %) | 3.0714 |
| Historical ES 95% (1D, %) | 5.3408 |
| Correlation vs SPY | 0.4635 |
| Tracking error vs SPY (%) | 32.8654 |
| P/E (trailing) | 30.26 |
| P/B | 7.91 |
| EV/EBITDA | 22.13 |
| Revenue growth (%) | 17.60 |
| Forward P/E (estimate) | 17.92 |
| Gross margin (%) | 64.52 |
| Operating margin (%) | 25.39 |
| Return on equity (%) | 27.32 |
| Free cash flow yield (%) | 2.81 |
| MA50 | 107.9886 |
| Close vs MA50 (%) | -6.6939 |
| MA200 | 101.5299 |
| Close vs MA200 (%) | -0.7583 |
| RSI (14, Wilder) | 43.0146 |
| MACD (12,26) | -3.2217 |
| MACD signal (9) | -2.4922 |
| MACD histogram | -0.7295 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 100.7600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.6592 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.7507 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -14.8915 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 33.2278 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 43.1117 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.8936 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.4279 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6840 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0714 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.3408 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4635 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.8654 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2454 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.2567 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1606 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.9162 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.5240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 25.3910 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.3190 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.8150 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 30.2583 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.0146 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.7295 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -6.6939 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.7583 -> Slightly below the moving-average trend level.

## TAILWINDS

### Cisco Systems (CSCO) Could Be 15% Undervalued As AI Earnings Focus Builds
- Summary: Investors see Cisco undervalued amid AI earnings focus, suggesting potential upside.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNaUZoNjY4Sy13SHlPSFN1Mno0cWtaWFVDMDhDWm90TDRVcmpTSGc3dzh3M09GZ1g0bGRDdnpGVHk0WFlDUFc0WDNkaW9DYy11b2dhV2RuUEVOTTJpa3F2ZUhOdTVFaTJyUnZvWjY0Nmp1eTBWOWdldWJqOU1heXF0MlJvcUR4T1BLTDEwdXo0OEdsbXJJOGdZ?oc=5>

### Dear Cisco Stock Fans, Mark Your Calendars for November 12
- Summary: Upcoming event on November 12 for Cisco shareholders.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPNE9oNF9IX2t6RlhjMm51ZW0yTnZtaldGNDZSWHFoMjF3dTJXdHU5SGxKUGJNOUJBSjY1MEJXNmItbGhLREZoa1BxckZGcVRxcnAxanlrUUZaOHdTbEFIN2I1OV9zZWM5SzFvdzhxVmFfdGhxZVdGUExpMXJwQWtfQTN5a0tXUUNHa1Q0UHhoamV6amdhYlZUWF9iam15eUtDaGxF?oc=5>

## HEADWINDS

### ETFs Are Net Sellers of Cisco Systems (CSCO) on Nov. 5
- Summary: ETFs sold Cisco shares, indicating negative market sentiment.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQQmtjOTdBRE5SeER0WU80VFd4bDRZd2R6Z2hfSVFnR2JjTWVYWG5aQ0FBdDE1b1dFQVhaV1V1bVRadTN4TXluTkY4TTQ2NzE2ZkZhcTE1anQtcmdWc1ppTTUzOF9CWVVtT0FIOGVkcTVycFdIeC1hRDd3MmRVY3VGeWU4eFlZNUVKWHFsaElUbzFhdGs0MHhtS0djVQ?oc=5>

## CATALYSTS

### Cisco Q1 Earnings – Here’s What Analysts Expect from CSCO Stock amid AI Trade Concerns
- Summary: Cisco Q1 Earnings – Here’s What Analysts Expect from CSCO Stock amid AI Trade Concerns
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNX05KdjBPVURfSHJqN3hQb0p4LURJX1NzWDFkeEJZNEFsM3FObmxWWms1Z0FGUFp4Ti1FZzZXRXpMM21aNE50bFoyTFhtOFRseEZ2X09IQ2RlYlZOQWRFYm5CaUd0dXJGalJXUC1rUGJMTEx5Q0dlbzJNSm5PRXNqSGczOU8zbmJ2aXVfMGNtVlVBMENEZnJXOE11cVBubnlmNl9wRklGU291VW5ZUVFTcnZiSQ?oc=5>

### Cisco Q1 earnings on deck: What to expect (CSCO:NASDAQ)
- Summary: Cisco Q1 earnings on deck: What to expect (CSCO:NASDAQ)
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxPQ3ZYckxoMEdmcTdkc2FtVGNxTjhSLTJtMFlacGVLR21kdFBUNVg2S1Bqd2x5SWIwbTkyVW0yWDB2V0RGekNqaElFQ2k0TUFPdzFuZWsyU1U0QWRVS3NkZTFobi1xN20tY3JrNktGSER5cUI0N2QzOExGNFpaOThnd2VLcFI?oc=5>

### Cisco schedules Q1 earnings and expands AI lineup: CSCO tests $102.04 resistance
- Summary: Cisco schedules Q1 earnings and expands AI lineup: CSCO tests $102.04 resistance
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQX2JYdF9HVkpQYmdocllyeG94dXZIQ2Z6bFVNUWRiVWZiRjBwM1lSUnpuTEl3eHNBZGtUczljVzQyMGhYR2k1bmJieTVKVkloVndaQ0pTNVliMEZ2M3lhcGJGbnQyb3lVR1R0TlBMX0s2SjF1OEJ0WV9ZeG5hR2FLWGdVMXd6WGpkNHdR?oc=5>

### Cisco Systems Has Suffered $145 Billion Wipeout. Will Earnings Change This?
- Summary: Cisco Systems Has Suffered $145 Billion Wipeout. Will Earnings Change This?
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxOYW1LNThidjEtdnVGeXpMdVRUMUhaT1I0aUl6cElGM3B5SFFuNHZfV3BtRDJwVk9wY1lPZkpEVWJqTE5CMlJwa3l5TEVkd2dLNUM0NURCajRHMzB2V1E5WTFHaDlOak40YWx5ODhxZkh6ci1EM0dyUGl1VlctdTJoREFXQUxjdTB4eXJwYXVOU2E1TXZKSi16N2l0WlByX2RlMXVTUms5UkE2ZUNGU29acTM3cHRCdjJzaENkSWN0R3E5blZ3N1ROMzlybXNROEc2?oc=5>

### 1 Options Trade to Bet on Cisco Stock Ahead of Earnings on November 12 — and Get a Shot at a 128.57% Maximum Payout
- Summary: Options trade signals investor interest ahead of earnings, potentially influencing volatility.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxNS0hqbXdISTAwWng4ZjEtWW52V1RiZnRiYnVxWXB1X1JpZ19kMktObE4wU3dYOXpRamFQcXNRVTh1VkU0MG5uNnRCS0c1a2hSNE1rUHg0eTdxNnJOcHVmTzB1X0Q2ZkdLa19BSDMwTlp3dkhuZFFXdFd4MWRDYU1pcHI0LURWWERpNUNDaGpWbEt4STZMd3BQOE9CWWo4NXM3N00wVHdiTnptWWFubE5DMnpFMmxSbk9ZMzF5aDdFZ1huQmNHZzdzNjlVWnp1cU1hMlpCQWxEQWJMVm4yQmZTZkJHUmpUd1FNSnRtbA?oc=5>

### How Investors Are Reacting To Cisco Stock After Analyst Downgrade
- Summary: Investors react negatively to Cisco downgrade, impacting short-term sentiment.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNc3plRmFVemkybDMwNkhvQ3BDSVphWjdfb1VGbng1cTg0akFrVzh1akR4R1FUdVFRZ3RyY2ZPTE9pN2VEMDF5VXB1UDVfNFROZjNPakYxa2F5cWtHeWg5SGNMUll0S042WUpwR2Fra0tRNTl5Qnd5OGZYeXdvNmx3NjNJd3dUS2dDdjVTNkN2QUZkMThFTXJmSDBLeWpFMHlkby1qTWpB?oc=5>

### What Analyst Projections for Key Metrics Reveal About Cisco (CSCO) Q1 Earnings
- Summary: Analyst forecasts for Cisco’s Q1 earnings indicate potential upside, suggesting stronger revenue and earnings than expected.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNVkQtSVE2N2xBbTB6MGJZY1FMMURxeW55NW03eHR0YXNkSnBWUVg5Z08zWmppNHFlOW5pdExRajd4YnQ4YXpYSjhBVlo0QjhNQnZhNjdNd1BFVHhSYVFHeU1FNWQ0Rnh1QVZOWXlxb1RPVmhGSjZVcXY5cC1XaDdrYVNNN2xJUFZPMElnWWM2R1dXWjE0SUttNXZHcm4yRUV6SVQ5WHR3?oc=5>

### Will Cisco Systems (CSCO) Deliver the Strong Results the Market Needs to See?
- Summary: Speculation on Cisco's upcoming earnings performance.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQSjRuWWVZQzNFa3hnMzB4U0VKc21CcHZPeXE0OTc4dVgzdHRycVpOYXJrbWpPanRiTTVUOXBDRTZFMk9WZlNIVFY3UW5hOXpzMFhqOFlxRUVPV0dFN2FrdVFWZU1XdFJyVXFCU0tuM0huMUU1VG8tdmhQOEh0OGx0dDlDVUJCS1I2NHpsSGFmWlIzQnZpZFpsR0ZGcERmNmc?oc=5>

### Cisco: Why I'm Upgrading After Underestimating The AI Opportunity (NASDAQ:CSCO)
- Summary: Analyst upgrades Cisco citing AI opportunities.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxObi0zcnBPMGZtRWFxYWtPS3YyQkFUVzFsX3RlSEZyM2xiZ2ZUTExnQzFWUVQ4QkowQkVhUUpCTUtvWUF0dFNNeFlkNklYRS1yekxfcmYycTdXaWNWWnVDX2Z5dHJ6dWhCYTNwcjV0ZGdtWS1XYTE1SHltYnFETURQYTBjLTktTlVqbWZZSWN2NW9sTjdPamhTcDdyeFFjVW5aS3VQTzJPQQ?oc=5>

### Cisco (CSCO) Is Considered a Good Investment by Brokers: Is That True?
- Summary: Broker opinions on Cisco's investment quality.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQeGV5MUl4VUl0cHBmb290cmcwNzRROTAzT0VsSkR2Mktkc2VuODVKTFoyTWdYWjY4MGdrM1FzOWdHR1l6WVF5Uk8yR0ZIQ0hqV2dScHVlZHRaWENMVWs5aUFXaG4zcWhXTnVOejFDZ2tyU3d2Mmd2RnpfR09XR3RieHA0TFJ4cU1xdWFiSWpIMVd0X0o1SzRTYjJIU1lfLXppbHUwSQ?oc=5>

### Ahead of Cisco Earnings, Here's What Barchart Data Says Comes Next for CSCO Stock
- Summary: Market data predicts post-earnings movement.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQOTA3ZmRSaHdoS2dnM1JoMnRtSHVoU01iR25wLWVTN3JXZ1psVWRld2wxeGJDMy1lQnhpTXdEUnBCWjRRbzhHOFlVekx4VmNUUFB6eTdCQnNpcWNFa3BQMzJodU1XRlltM1B4M3BaWW9FWHBDV0hfc05ndnhPXzZ1MnQtMVRsWVliNnp1UUZWem5tTi0yaEJhTm5CSnd5WnljNEE?oc=5>

### Will Cisco (CSCO) Beat Estimates Again in Its Next Earnings Report?
- Summary: Questioning Cisco's ability to exceed earnings estimates.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNRGJRSG9SOERDYW9PNnVvRXdCY0haNHB3MDVwM0hXMmhERnVrOHBRTElLRTkxQUNtRF9RSk5DOXZhS09FMTE3c0pNLXFnV04xWmZMUXVjYXRCMXNvM00zX2k3c1pxcExOQ3U0QzhDcm5YbDN4TGd2c3NrdVE3d3V4dTg0RGo1MmlGQTgwZEV4YkZDdm81S1FIMzJ3ZEc?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **30.26** | **7.91** | **22.13** | **17.60** | **397,255,049,216.00 USD** | **43.11** |
| ANET | 49.54 | 15.11 | 44.14 | 58.50 | 248,485,969,920.00 USD | 45.76 |
| FFIV | 25.34 | 4.54 | 18.16 | 13.30 | 18,180,087,808.00 USD | 34.17 |
| HPE | 24.75 | 2.52 | 11.74 | 33.70 | 66,705,108,992.00 USD | 123.49 |

Peers fetched as_of: 2026-11-11; CSCO reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-12
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-09-02
- Revenue (latest available single quarter): 12,844,000,000.00 USD; period 2018-04-29/2018-07-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 3,373,000,000.00 USD; period 2026-01-25/2026-04-25; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/858877/000085887726000132/csco-20260725.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilwFBVV95cUxNaUZoNjY4Sy13SHlPSFN1Mno0cWtaWFVDMDhDWm90TDRVcmpTSGc3dzh3M09GZ1g0bGRDdnpGVHk0WFlDUFc0WDNkaW9DYy11b2dhV2RuUEVOTTJpa3F2ZUhOdTVFaTJyUnZvWjY0Nmp1eTBWOWdldWJqOU1heXF0MlJvcUR4T1BLTDEwdXo0OEdsbXJJOGdZ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPNE9oNF9IX2t6RlhjMm51ZW0yTnZtaldGNDZSWHFoMjF3dTJXdHU5SGxKUGJNOUJBSjY1MEJXNmItbGhLREZoa1BxckZGcVRxcnAxanlrUUZaOHdTbEFIN2I1OV9zZWM5SzFvdzhxVmFfdGhxZVdGUExpMXJwQWtfQTN5a0tXUUNHa1Q0UHhoamV6amdhYlZUWF9iam15eUtDaGxF?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQQmtjOTdBRE5SeER0WU80VFd4bDRZd2R6Z2hfSVFnR2JjTWVYWG5aQ0FBdDE1b1dFQVhaV1V1bVRadTN4TXluTkY4TTQ2NzE2ZkZhcTE1anQtcmdWc1ppTTUzOF9CWVVtT0FIOGVkcTVycFdIeC1hRDd3MmRVY3VGeWU4eFlZNUVKWHFsaElUbzFhdGs0MHhtS0djVQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxNX05KdjBPVURfSHJqN3hQb0p4LURJX1NzWDFkeEJZNEFsM3FObmxWWms1Z0FGUFp4Ti1FZzZXRXpMM21aNE50bFoyTFhtOFRseEZ2X09IQ2RlYlZOQWRFYm5CaUd0dXJGalJXUC1rUGJMTEx5Q0dlbzJNSm5PRXNqSGczOU8zbmJ2aXVfMGNtVlVBMENEZnJXOE11cVBubnlmNl9wRklGU291VW5ZUVFTcnZiSQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOajdxTFFHUlRraWFsc0pSekZYRktYRFZVRnVEZDZWc0p0clZaRUNYMjFaMjVHVU9UQzZ0X1cwcE9hWFBLWjBuSGdiSFZ4dmMtcklIUG1YVzgyU19mVm13UnA2OXdZTVNlY2JDVGZMREVfUlVfTGtscTRLVlFhN1hBR2YyejZTLWhsakJSWktCZ09wQ0ZrbV9RVmZseGNZdG8?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxPQ3ZYckxoMEdmcTdkc2FtVGNxTjhSLTJtMFlacGVLR21kdFBUNVg2S1Bqd2x5SWIwbTkyVW0yWDB2V0RGekNqaElFQ2k0TUFPdzFuZWsyU1U0QWRVS3NkZTFobi1xN20tY3JrNktGSER5cUI0N2QzOExGNFpaOThnd2VLcFI?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQX2JYdF9HVkpQYmdocllyeG94dXZIQ2Z6bFVNUWRiVWZiRjBwM1lSUnpuTEl3eHNBZGtUczljVzQyMGhYR2k1bmJieTVKVkloVndaQ0pTNVliMEZ2M3lhcGJGbnQyb3lVR1R0TlBMX0s2SjF1OEJ0WV9ZeG5hR2FLWGdVMXd6WGpkNHdR?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxOYW1LNThidjEtdnVGeXpMdVRUMUhaT1I0aUl6cElGM3B5SFFuNHZfV3BtRDJwVk9wY1lPZkpEVWJqTE5CMlJwa3l5TEVkd2dLNUM0NURCajRHMzB2V1E5WTFHaDlOak40YWx5ODhxZkh6ci1EM0dyUGl1VlctdTJoREFXQUxjdTB4eXJwYXVOU2E1TXZKSi16N2l0WlByX2RlMXVTUms5UkE2ZUNGU29acTM3cHRCdjJzaENkSWN0R3E5blZ3N1ROMzlybXNROEc2?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxNS0hqbXdISTAwWng4ZjEtWW52V1RiZnRiYnVxWXB1X1JpZ19kMktObE4wU3dYOXpRamFQcXNRVTh1VkU0MG5uNnRCS0c1a2hSNE1rUHg0eTdxNnJOcHVmTzB1X0Q2ZkdLa19BSDMwTlp3dkhuZFFXdFd4MWRDYU1pcHI0LURWWERpNUNDaGpWbEt4STZMd3BQOE9CWWo4NXM3N00wVHdiTnptWWFubE5DMnpFMmxSbk9ZMzF5aDdFZ1huQmNHZzdzNjlVWnp1cU1hMlpCQWxEQWJMVm4yQmZTZkJHUmpUd1FNSnRtbA?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNc3plRmFVemkybDMwNkhvQ3BDSVphWjdfb1VGbng1cTg0akFrVzh1akR4R1FUdVFRZ3RyY2ZPTE9pN2VEMDF5VXB1UDVfNFROZjNPakYxa2F5cWtHeWg5SGNMUll0S042WUpwR2Fra0tRNTl5Qnd5OGZYeXdvNmx3NjNJd3dUS2dDdjVTNkN2QUZkMThFTXJmSDBLeWpFMHlkby1qTWpB?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNVkQtSVE2N2xBbTB6MGJZY1FMMURxeW55NW03eHR0YXNkSnBWUVg5Z08zWmppNHFlOW5pdExRajd4YnQ4YXpYSjhBVlo0QjhNQnZhNjdNd1BFVHhSYVFHeU1FNWQ0Rnh1QVZOWXlxb1RPVmhGSjZVcXY5cC1XaDdrYVNNN2xJUFZPMElnWWM2R1dXWjE0SUttNXZHcm4yRUV6SVQ5WHR3?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQSjRuWWVZQzNFa3hnMzB4U0VKc21CcHZPeXE0OTc4dVgzdHRycVpOYXJrbWpPanRiTTVUOXBDRTZFMk9WZlNIVFY3UW5hOXpzMFhqOFlxRUVPV0dFN2FrdVFWZU1XdFJyVXFCU0tuM0huMUU1VG8tdmhQOEh0OGx0dDlDVUJCS1I2NHpsSGFmWlIzQnZpZFpsR0ZGcERmNmc?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxNb0RTcWZnNWFNSDFZSWRKdUFEVkcyNXdoV2tVX3V4VjdSSW5Na0J6bkdsYmgtclZ5WkJSb0NSUG95alVRRHpINXNyckFhTFF3Q2NmV2dDWGNrNnBRZmhDai04ZmxKRE5YZnZiN0NvSDdwYVpiLUZiX0txajZwbk1oTER2eVZaUy00ZERuOEVzT2pEUFUzMXFkeEFNWm82TW11UDZHbHV0N05hQXZXYVU1b0h4aWRtQQ?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxObi0zcnBPMGZtRWFxYWtPS3YyQkFUVzFsX3RlSEZyM2xiZ2ZUTExnQzFWUVQ4QkowQkVhUUpCTUtvWUF0dFNNeFlkNklYRS1yekxfcmYycTdXaWNWWnVDX2Z5dHJ6dWhCYTNwcjV0ZGdtWS1XYTE1SHltYnFETURQYTBjLTktTlVqbWZZSWN2NW9sTjdPamhTcDdyeFFjVW5aS3VQTzJPQQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQeGV5MUl4VUl0cHBmb290cmcwNzRROTAzT0VsSkR2Mktkc2VuODVKTFoyTWdYWjY4MGdrM1FzOWdHR1l6WVF5Uk8yR0ZIQ0hqV2dScHVlZHRaWENMVWs5aUFXaG4zcWhXTnVOejFDZ2tyU3d2Mmd2RnpfR09XR3RieHA0TFJ4cU1xdWFiSWpIMVd0X0o1SzRTYjJIU1lfLXppbHUwSQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQOTA3ZmRSaHdoS2dnM1JoMnRtSHVoU01iR25wLWVTN3JXZ1psVWRld2wxeGJDMy1lQnhpTXdEUnBCWjRRbzhHOFlVekx4VmNUUFB6eTdCQnNpcWNFa3BQMzJodU1XRlltM1B4M3BaWW9FWHBDV0hfc05ndnhPXzZ1MnQtMVRsWVliNnp1UUZWem5tTi0yaEJhTm5CSnd5WnljNEE?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNRGJRSG9SOERDYW9PNnVvRXdCY0haNHB3MDVwM0hXMmhERnVrOHBRTElLRTkxQUNtRF9RSk5DOXZhS09FMTE3c0pNLXFnV04xWmZMUXVjYXRCMXNvM00zX2k3c1pxcExOQ3U0QzhDcm5YbDN4TGd2c3NrdVE3d3V4dTg0RGo1MmlGQTgwZEV4YkZDdm81S1FIMzJ3ZEc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
