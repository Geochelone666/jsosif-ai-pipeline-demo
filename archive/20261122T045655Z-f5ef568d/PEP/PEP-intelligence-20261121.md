# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-11-21**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-11-21**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-22T05:15:53.106087+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 20, 'rule': 7, 'ai': 7, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261121T053104Z-422ce34b/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 20 unique headlines; 9 named publishers; 0 exact duplicates; 20 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-14

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 140.5400 |
| Return 1D (%) | 1.1079 |
| Return 1W (%) | -3.3691 |
| Return 1M (%) | 4.8649 |
| Return YTD (%) | 0.9045 |
| Return 1Y (%) | 0.0921 |
| Annualized volatility (%) | 21.9597 |
| Beta vs SPY | -0.1639 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | 0.1133 |
| Downside deviation (rf=0, %) | 14.7385 |
| Sortino (rf=0) | 0.1687 |
| Historical VaR 95% (1D, %) | 2.2237 |
| Historical ES 95% (1D, %) | 2.7033 |
| Correlation vs SPY | -0.1067 |
| Tracking error vs SPY (%) | 27.4510 |
| P/E (trailing) | 17.68 |
| P/B | 8.60 |
| EV/EBITDA | 12.12 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 16.35 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.05 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.72 |
| MA50 | 134.1202 |
| Close vs MA50 (%) | 4.7866 |
| MA200 | 143.3335 |
| Close vs MA200 (%) | -1.9490 |
| RSI (14, Wilder) | 53.2382 |
| MACD (12,26) | 2.2359 |
| MACD signal (9) | 2.6974 |
| MACD histogram | -0.4615 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 140.5400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.1079 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.3691 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.8649 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 0.9045 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.0921 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.9597 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.7385 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1687 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.2237 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7033 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1067 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 27.4510 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1639 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1133 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.3535 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.0460 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.7224 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.6780 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.2382 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.4615 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.7866 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.9490 -> Slightly below the moving-average trend level.

## TAILWINDS

### PepsiCo Stock And Other Defensive Value Picks For Higher Rates
- Summary: PepsiCo Stock And Other Defensive Value Picks For Higher Rates
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQY2FmbDdLMzQtYnc2ekdOSUl3RHJaQ3BkTWkzSXV6TlE5Q2p4YXJ4OUVXQU5SSU1nVVpLOEdlOUpSOC1aN2ZYSjljSEtGZ3RtV1p5eDdDUXcwR0wzdVROZWMtY3pMaldLaFRSZ2hpVmxYdVFDTTRoOGJzTm5rRjlRU0E1bTBGTmc4YVNOYVl0aF9tZ0lETzZCZkNKSjlxc3JvRmc?oc=5>

### PepsiCo (PEP) Stock May Be 50% Undervalued Following Partnership Renewal
- Summary: Partnership renewal may signal undervaluation, boosting investor confidence.
- Date: 2026-11-21 | Impact: high | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNQ0V2bUwxb1Y4Y2NrS2ZkNm1LOWx5S19rLUJHSVhyZy1lLWJEZVVsMng0R05OWUV2NlN3S1hVVXVzUndlZnJMV3ppQUNuT3dsMFF3cjE0RlpZTXVXSE90dVJzQ05CWlJtRm1KWFdJMm1HdkNrV2ZQdkhQQ2NzOFNLRkVOWjlUZ3NFdmNSMzJNWHFURG1vOV9SZDFPV3N6SHFXOEN4eVpUU3NleUNSRlZOZWZweHB3S09QcFA1bnBPaTFIcHVCbDhOZVotS0dkVkhqUUR4UNIB2gFBVV95cUxPaU9CUFBiUnptNnFLNVE5MlFhdEEyYlI2MXEtNEhRLVlMS1pDOEdoc0NQbkRvQUc5eDhfV3ZOUW96M3FtbDBweElJdTZrZEl4ZWQ3YjNtUzFnU3BUbG9vdGZtQkVjbXVvbWhHd3lwa3AycnhacGg2MW5pSjZtY0sxZ1pMSFluUEJSRUZEOTFZbzVWTnRUb0g2cEhPWGFhTlZQaS1fQ0lkMU00MXFORjVsUTZySVMydTV6ZUZydER4SC1Rck5jM2Q4dkZWWjRydFhfMDQ1dElKMk8yZw?oc=5>

## HEADWINDS

### PepsiCo (PEP) Stock: Drops as Company Secures 10-Year Beverage Deal With Hyatt Across 700+ Hotels in America
- Summary: PepsiCo (PEP) Stock: Drops as Company Secures 10-Year Beverage Deal With Hyatt Across 700+ Hotels in America
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxOd3BCalBHdHFNYWxZdnU1Mi1FSmlTZ1ExeVhNV1VHaGZINVNydFd1SlZaaGhFVWtCS1BSUGdXd1dTSTNaY0RVVGlxWVUzdGdSZC1mOHJ6TVlNRFFxLU9WNW5fbGtzUUJMSV9hWWpNR0FtN1FmZFZ5RkdzTDFYd1czWFc1SklDbjlhNEtxc0ZMeVpabjdyR3k2ejBLZDZkeVd3VEYtSUVTNVJ0aGRqSnp5WmVqTzVxRmZfVUxRZW5semlqMHFmVDI0?oc=5>

### Bernstein Sees Trouble Ahead for PepsiCo (PEP). Here’s Where.
- Summary: Bernstein research warns of future challenges for PepsiCo.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxOT3ctYUZMSGdjY2o2WFJvcElIdkZWcHlUd2NweGxJRFpHLVhvVzJQaENEMVpXTGlNamhPU28wd1JEMWhSRzRIU0dSdHNGa3JwcFpBTUxlSUw0alVSVEtEc00xYXBTVEl5NkZfOHM2R3ZIeWZxRTVHUi02THNMRk91eTFZR2p6YzRIY2lLWTktUFlMdHNwXzRxZjlac1oyODVFX2NJ?oc=5>

### Could PepsiCo Be The Value Stock For Your Portfolio?
- Summary: Opinion piece on PepsiCo as a value investment.
- Date: 2026-11-17 | Impact: low | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNWlJCOW9wd2tPRXh5dHpPLV95R0pCQkdFR1o1cFNYSnFzMlVXWG1kRGxHeGJ0NV9QR2gzM0dqTmJJaUdCQUprTWRNVmxMUmFfNzZvcW1MUVRGU1pZemVVWmxhd0syYTNaU2hjbWVHMDdmaW1mUnhPZWhJQXl6S3dmZ0lDOFlsQXpCMG1NOEpFSmVZaHBfeUlMRzZTS2JIWWd3R0E?oc=5>

### How KFC Partnership Loss Will Impact PepsiCo (PEP) Investors
- Summary: Loss of KFC partnership could negatively affect PepsiCo’s revenue.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNSXhiSVlnWlVTSFZFeV9HUndTWnJpSHkwQ1VCb2kxSkZvbkJ0WmRsTG5nT3hwa0JRdjR4eW1EOGJVUzRqMUlqb2N0bll1QU9CQmRrM0F5RUdwZmo1eGZldjNIMkloYWoxaXpoaXRyeXIxMG5yZ192T1FzN25lVk5QTUdTam9BUTVtc3JkaHU0TUlSdGRMcEdPZFdqM01RLTdCd0E?oc=5>

### Is Lower 2026 Guidance Altering The Investment Case For PepsiCo (PEP)?
- Summary: Lower 2026 guidance may weaken PepsiCo’s outlook.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxQRHAwZTFpZ29MVEhlNDA3bTJqaC1FeTIwSEozaFJPNDA0TE8wY0FwalI4MmFlV2ZJSUF4cmhHdHl3S29rSzNnRDk4cEdBcTNxVWl5NHdTS056WVR6ZlVVZTVpNjFKWDFlQkdydk96dTRNdFFEd1dUcE1QV2FaX3Q2LTVJVl9oRGhEQmVSQTc3RzFscTREczJOMF8yUDV6eUpvWnVnQkV2ZEFoN2NFT2J3ZXh2a3E1S3ZteTY4T1o5UXdiWDBPcjQtOG9Ka2ZZa0phUVJYTtIB2gFBVV95cUxNY2xnN0k5QWRYbnp6Rzc4YW9wbE14TElOMDhCQ3o0YWV0Mm9CQ2VfWjVYNTRYeHB6NVF0OGRuOXQ3b2hYT3lqUGtSckU1bkJJWWFDbS1CdklaZkd1Vk8xTUp5TGVOamd6eUpwd1pEWjMwTXJIWUw0blg3eU1SaGF2a3NCdEFralFjMzZCWVZBSXVtbTFrQlByVUl1d3E3eWNJRVQ3Y0tWV21BWUhkbDRxZ3l1UUdCYzAtdVA3ekprUjZZcXI1b0RybUM2THZvVTVjUlNjUllsRnVfUQ?oc=5>

## CATALYSTS

### PepsiCo (PEP) Lands Hyatt Deal On A Fair Value Debate
- Summary: PepsiCo (PEP) Lands Hyatt Deal On A Fair Value Debate
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNTVFiVXNnMmNNTlZ4UzA0QlFEZV94WVluckhCT1hsVjJnTXc5NkhiRnVyR0tTQ3phaWNDci0xZWpjQmpoWjA0X2JTU3dzalcyc1djU3gxY0hDV0ZKM0lBZDhINS1LM3VvMHRLUHpTbVhqTVdQb2I1ZU1nbS1BazlCS1pUSWp0TjUtX1NaZDRYVmZzR0VNUDZUeA?oc=5>

### PepsiCo Declares Quarterly Dividend
- Summary: PepsiCo Declares Quarterly Dividend
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPZlJSVjZEQWNRbmlCdE9hd2c2VzcyY0R6dFBIeTV0TGpVa1paVm9obUdCRXFTZzFTN0k0LTAtbk0xMEdJcFRDQjBDQ1hMN09GTGNGLWVXTzRTWHhEOFZzcHRLZ3NvQzlhUWhrZkdKQkNwTm1ORTBXYjFCTl9Xc1gxWVRoTWNTWjRiWUVEOGVvcWw5RnJFOFFyNFBLM2FVbjRVclE?oc=5>

### PepsiCo Has Raised Its Dividend 54 Straight Years. Here's What $10,000 Invested Pays Annually.
- Summary: PepsiCo Has Raised Its Dividend 54 Straight Years. Here's What $10,000 Invested Pays Annually.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxORU9WSnJGbDh4cXZJNVNOX2IyV2FGa0hSU0pQblJvY1E4YjVqRWxmdzF2R1JuY3B2dHM2UFBodEppUWVBLTZtNW9NNmNKdXpYNTM0dlBVOVgtam1kU01LZW1CVjFsZkszZjI4U0R6RUt4REczenhHVXFmMDB0anFzZDRpWUdxSXZPTDdRd0kxNUxUYWJoNUd4Q2tOeVNmVl9EbkJqSkt3aWZlbFlOallkLUkyWVpHTWFwRmJnbkg4Yml3RWI0RHhLU2thRDg?oc=5>

### PepsiCo, Inc. $PEP Stock: Voya Investment Management LLC Reduces Position
- Summary: PepsiCo, Inc. $PEP Stock: Voya Investment Management LLC Reduces Position
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxNbzlnUzE4SHVuWElNaVRwTWpUV29fUFZxVHhER2ZYd1FrTDdDZ2RlV3drU3ZYdGwyUnZjWnZsNHl0RDRWNlo2a0xMaG1EdF9tRG9EMlVFX0VORnFEeGRYWHB4VTg0bDlEQUtYSFBVYkdac0VQbFV4dlNvU0dWMGk1WDkyODFuekxaRzYwS3ZsRjh4X3E3ZFZwaHVFcmRiWFB0bVRfTjRwa082NGcxcktxd1RBbnh4ejNOSEhTYmlBM1RuZG1FODBZaDV3?oc=5>

### PepsiCo, Inc. $PEP Stock Sold by Danske Bank A S
- Summary: PepsiCo, Inc. $PEP Stock Sold by Danske Bank A S
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPWjFhWkg5UWkwVlNIWlp0QXJhRGp3dk9UdV82V01YSTJpZWdVdU1nZDN3RnZfOXJ3NE5JLTY4VTlfWHlOc21RLXdHMDN5LUdlZXJ2MFltRzZIV3lId2dmVERlM0FpMFpwNEVHc1haOTdIcWFFQ2RnNTNrSktMR2R6d19NR2N6LVRhWUJGeW44QVZWSS1PNHVqUFpRV2RfMjJ3bjd6TlRhTnRTQQ?oc=5>

### $400,000 in PepsiCo and Kimberly-Clark Pays $17,845 a Year in Dividends
- Summary: PepsiCo dividend payout of $17,845 per year on $400,000 investment.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNc1VTV3Z4T0ZpZkdWbHI4Q3IxYlMwY3FlMDNrVlZrSFVtYzA4RGJZOHo2Z3AycEVvVnl1QUhmLXQxZDViRjVUM1czRGF5TVFCUkJDWmU4VHJBNEI4Mms2b3FaX1dyRERlcVA3VlhXMDlWZHF6YjFaazlZX1J3cG9CdlhiVkJhWk5RU1F1WXRRb2MxeDhkWFVLLWRUV2ktdzBQSFRuZHpRSGw2c0NMZDRHSg?oc=5>

### 4 Dividend Stocks Yielding 4%+: Realty Income, PepsiCo, More
- Summary: PepsiCo is highlighted among dividend-paying stocks yielding over 4%, indicating its stable dividend policy and attractiveness to income-focused investors.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPZjRtVkdxeldFdGhKcHNFU29WRERBdHNKNU5PN0l5WnluUVBmTEdzY1AydWFmd2JueHZnV09ZaVVPdmlUZWlTQ2lQek8td0RiUG83Z2NMcHJXRUhLVWJUY2UyYzI2eXZhbWlHQVVjdEJ2U2FfNHZaYzV1WXJBX0RpNXhrelJaRGFxX251Skw0LTczU20xZVJHZTJZY0lqQQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **17.68** | **8.60** | **12.12** | **5.60** | **191,519,621,120.00 USD** | **0.09** |
| KO | 28.61 | 11.16 | 25.53 | 7.40 | 417,241,497,600.00 USD | 39.82 |
| MNST | 39.72 | 8.69 | 27.50 | 16.70 | 85,523,693,568.00 USD | 20.99 |
| KDP | 31.39 | 1.86 | 16.25 | 70.60 | 49,738,104,832.00 USD | 32.12 |

Peers fetched as_of: 2026-11-21; PEP reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-21

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMiogFBVV95cUxQY2FmbDdLMzQtYnc2ekdOSUl3RHJaQ3BkTWkzSXV6TlE5Q2p4YXJ4OUVXQU5SSU1nVVpLOEdlOUpSOC1aN2ZYSjljSEtGZ3RtV1p5eDdDUXcwR0wzdVROZWMtY3pMaldLaFRSZ2hpVmxYdVFDTTRoOGJzTm5rRjlRU0E1bTBGTmc4YVNOYVl0aF9tZ0lETzZCZkNKSjlxc3JvRmc?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNQ0V2bUwxb1Y4Y2NrS2ZkNm1LOWx5S19rLUJHSVhyZy1lLWJEZVVsMng0R05OWUV2NlN3S1hVVXVzUndlZnJMV3ppQUNuT3dsMFF3cjE0RlpZTXVXSE90dVJzQ05CWlJtRm1KWFdJMm1HdkNrV2ZQdkhQQ2NzOFNLRkVOWjlUZ3NFdmNSMzJNWHFURG1vOV9SZDFPV3N6SHFXOEN4eVpUU3NleUNSRlZOZWZweHB3S09QcFA1bnBPaTFIcHVCbDhOZVotS0dkVkhqUUR4UNIB2gFBVV95cUxPaU9CUFBiUnptNnFLNVE5MlFhdEEyYlI2MXEtNEhRLVlMS1pDOEdoc0NQbkRvQUc5eDhfV3ZOUW96M3FtbDBweElJdTZrZEl4ZWQ3YjNtUzFnU3BUbG9vdGZtQkVjbXVvbWhHd3lwa3AycnhacGg2MW5pSjZtY0sxZ1pMSFluUEJSRUZEOTFZbzVWTnRUb0g2cEhPWGFhTlZQaS1fQ0lkMU00MXFORjVsUTZySVMydTV6ZUZydER4SC1Rck5jM2Q4dkZWWjRydFhfMDQ1dElKMk8yZw?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxOd3BCalBHdHFNYWxZdnU1Mi1FSmlTZ1ExeVhNV1VHaGZINVNydFd1SlZaaGhFVWtCS1BSUGdXd1dTSTNaY0RVVGlxWVUzdGdSZC1mOHJ6TVlNRFFxLU9WNW5fbGtzUUJMSV9hWWpNR0FtN1FmZFZ5RkdzTDFYd1czWFc1SklDbjlhNEtxc0ZMeVpabjdyR3k2ejBLZDZkeVd3VEYtSUVTNVJ0aGRqSnp5WmVqTzVxRmZfVUxRZW5semlqMHFmVDI0?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxOT3ctYUZMSGdjY2o2WFJvcElIdkZWcHlUd2NweGxJRFpHLVhvVzJQaENEMVpXTGlNamhPU28wd1JEMWhSRzRIU0dSdHNGa3JwcFpBTUxlSUw0alVSVEtEc00xYXBTVEl5NkZfOHM2R3ZIeWZxRTVHUi02THNMRk91eTFZR2p6YzRIY2lLWTktUFlMdHNwXzRxZjlac1oyODVFX2NJ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNWlJCOW9wd2tPRXh5dHpPLV95R0pCQkdFR1o1cFNYSnFzMlVXWG1kRGxHeGJ0NV9QR2gzM0dqTmJJaUdCQUprTWRNVmxMUmFfNzZvcW1MUVRGU1pZemVVWmxhd0syYTNaU2hjbWVHMDdmaW1mUnhPZWhJQXl6S3dmZ0lDOFlsQXpCMG1NOEpFSmVZaHBfeUlMRzZTS2JIWWd3R0E?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNSXhiSVlnWlVTSFZFeV9HUndTWnJpSHkwQ1VCb2kxSkZvbkJ0WmRsTG5nT3hwa0JRdjR4eW1EOGJVUzRqMUlqb2N0bll1QU9CQmRrM0F5RUdwZmo1eGZldjNIMkloYWoxaXpoaXRyeXIxMG5yZ192T1FzN25lVk5QTUdTam9BUTVtc3JkaHU0TUlSdGRMcEdPZFdqM01RLTdCd0E?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQRHAwZTFpZ29MVEhlNDA3bTJqaC1FeTIwSEozaFJPNDA0TE8wY0FwalI4MmFlV2ZJSUF4cmhHdHl3S29rSzNnRDk4cEdBcTNxVWl5NHdTS056WVR6ZlVVZTVpNjFKWDFlQkdydk96dTRNdFFEd1dUcE1QV2FaX3Q2LTVJVl9oRGhEQmVSQTc3RzFscTREczJOMF8yUDV6eUpvWnVnQkV2ZEFoN2NFT2J3ZXh2a3E1S3ZteTY4T1o5UXdiWDBPcjQtOG9Ka2ZZa0phUVJYTtIB2gFBVV95cUxNY2xnN0k5QWRYbnp6Rzc4YW9wbE14TElOMDhCQ3o0YWV0Mm9CQ2VfWjVYNTRYeHB6NVF0OGRuOXQ3b2hYT3lqUGtSckU1bkJJWWFDbS1CdklaZkd1Vk8xTUp5TGVOamd6eUpwd1pEWjMwTXJIWUw0blg3eU1SaGF2a3NCdEFralFjMzZCWVZBSXVtbTFrQlByVUl1d3E3eWNJRVQ3Y0tWV21BWUhkbDRxZ3l1UUdCYzAtdVA3ekprUjZZcXI1b0RybUM2THZvVTVjUlNjUllsRnVfUQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNTVFiVXNnMmNNTlZ4UzA0QlFEZV94WVluckhCT1hsVjJnTXc5NkhiRnVyR0tTQ3phaWNDci0xZWpjQmpoWjA0X2JTU3dzalcyc1djU3gxY0hDV0ZKM0lBZDhINS1LM3VvMHRLUHpTbVhqTVdQb2I1ZU1nbS1BazlCS1pUSWp0TjUtX1NaZDRYVmZzR0VNUDZUeA?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPZlJSVjZEQWNRbmlCdE9hd2c2VzcyY0R6dFBIeTV0TGpVa1paVm9obUdCRXFTZzFTN0k0LTAtbk0xMEdJcFRDQjBDQ1hMN09GTGNGLWVXTzRTWHhEOFZzcHRLZ3NvQzlhUWhrZkdKQkNwTm1ORTBXYjFCTl9Xc1gxWVRoTWNTWjRiWUVEOGVvcWw5RnJFOFFyNFBLM2FVbjRVclE?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxORU9WSnJGbDh4cXZJNVNOX2IyV2FGa0hSU0pQblJvY1E4YjVqRWxmdzF2R1JuY3B2dHM2UFBodEppUWVBLTZtNW9NNmNKdXpYNTM0dlBVOVgtam1kU01LZW1CVjFsZkszZjI4U0R6RUt4REczenhHVXFmMDB0anFzZDRpWUdxSXZPTDdRd0kxNUxUYWJoNUd4Q2tOeVNmVl9EbkJqSkt3aWZlbFlOallkLUkyWVpHTWFwRmJnbkg4Yml3RWI0RHhLU2thRDg?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxNbzlnUzE4SHVuWElNaVRwTWpUV29fUFZxVHhER2ZYd1FrTDdDZ2RlV3drU3ZYdGwyUnZjWnZsNHl0RDRWNlo2a0xMaG1EdF9tRG9EMlVFX0VORnFEeGRYWHB4VTg0bDlEQUtYSFBVYkdac0VQbFV4dlNvU0dWMGk1WDkyODFuekxaRzYwS3ZsRjh4X3E3ZFZwaHVFcmRiWFB0bVRfTjRwa082NGcxcktxd1RBbnh4ejNOSEhTYmlBM1RuZG1FODBZaDV3?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPWjFhWkg5UWkwVlNIWlp0QXJhRGp3dk9UdV82V01YSTJpZWdVdU1nZDN3RnZfOXJ3NE5JLTY4VTlfWHlOc21RLXdHMDN5LUdlZXJ2MFltRzZIV3lId2dmVERlM0FpMFpwNEVHc1haOTdIcWFFQ2RnNTNrSktMR2R6d19NR2N6LVRhWUJGeW44QVZWSS1PNHVqUFpRV2RfMjJ3bjd6TlRhTnRTQQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNc1VTV3Z4T0ZpZkdWbHI4Q3IxYlMwY3FlMDNrVlZrSFVtYzA4RGJZOHo2Z3AycEVvVnl1QUhmLXQxZDViRjVUM1czRGF5TVFCUkJDWmU4VHJBNEI4Mms2b3FaX1dyRERlcVA3VlhXMDlWZHF6YjFaazlZX1J3cG9CdlhiVkJhWk5RU1F1WXRRb2MxeDhkWFVLLWRUV2ktdzBQSFRuZHpRSGw2c0NMZDRHSg?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPZjRtVkdxeldFdGhKcHNFU29WRERBdHNKNU5PN0l5WnluUVBmTEdzY1AydWFmd2JueHZnV09ZaVVPdmlUZWlTQ2lQek8td0RiUG83Z2NMcHJXRUhLVWJUY2UyYzI2eXZhbWlHQVVjdEJ2U2FfNHZaYzV1WXJBX0RpNXhrelJaRGFxX251Skw0LTczU20xZVJHZTJZY0lqQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
