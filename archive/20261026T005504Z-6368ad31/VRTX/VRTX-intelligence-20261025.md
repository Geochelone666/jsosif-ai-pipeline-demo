# VRTX Intelligence Report

- ticker: **VRTX**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/VRTX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/VRTX/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T00:56:24.282048+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 17, 'rule': 1, 'ai': 11, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **5**; {'directional_claim_without_event_type': 5}
- RSS source audit (metadata only, not article fact-checking): 17 unique headlines; 8 named publishers; 0 exact duplicates; 17 HTTPS source links; largest publisher share 47.06%; oldest publication 2026-10-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 523.9300 |
| Return 1D (%) | -2.1003 |
| Return 1W (%) | 4.8405 |
| Return 1M (%) | 1.4700 |
| Return YTD (%) | 15.5660 |
| Return 1Y (%) | 23.9690 |
| Annualized volatility (%) | 29.0832 |
| Beta vs SPY | 0.4894 |
| Max drawdown (%) | -15.2113 |
| Sharpe (rf=0) | 0.8854 |
| Downside deviation (rf=0, %) | 17.8484 |
| Sortino (rf=0) | 1.4428 |
| Historical VaR 95% (1D, %) | 2.6839 |
| Historical ES 95% (1D, %) | 3.4058 |
| Correlation vs SPY | 0.2145 |
| Tracking error vs SPY (%) | 29.1424 |
| P/E (trailing) | 29.90 |
| P/B | 6.56 |
| EV/EBITDA | 24.88 |
| Revenue growth (%) | 12.50 |
| Forward P/E (estimate) | 25.66 |
| Gross margin (%) | 54.96 |
| Operating margin (%) | 38.05 |
| Return on equity (%) | 23.54 |
| Free cash flow yield (%) | 1.98 |
| MA50 | 522.7088 |
| Close vs MA50 (%) | 0.2336 |
| MA200 | 477.3702 |
| Close vs MA200 (%) | 9.7534 |
| RSI (14, Wilder) | 55.0729 |
| MACD (12,26) | 0.7421 |
| MACD signal (9) | -2.6775 |
| MACD histogram | 3.4196 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'VRTX': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 523.9300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.1003 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.8405 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.4700 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 15.5660 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 23.9690 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.0832 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 17.8484 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4428 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.6839 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4058 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2145 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.1424 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4894 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.2113 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8854 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.6598 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.9570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.0550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 23.5430 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.9789 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 29.9047 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 55.0729 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 3.4196 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.2336 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.7534 -> Clearly above the moving-average trend level.

## TAILWINDS

### Vertex Pharmaceuticals (VRTX) Outpaces Stock Market Gains: What You Should Know
- Summary: Vertex Pharmaceuticals (VRTX) Outpaces Stock Market Gains: What You Should Know
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOUFgyYVJvNnAxN1I1bmZmcnZIQXIzVC1uNlZGUzZqR3ozSEEtYnV3T1p4ZG1TRGRhRUhRY1NJZllOUzBqTjVRUmdNelBKMV9BZ1dtcUk2bng3NlJFdjlEV0ZIUEg2TVFuZUNJZHFCQXRmNFVza2FidlZOLXZhbEFlM3QyY2pMNTJKLVJ5Z3A0T2VzLUs3Y19zVWtHWURmMnVXSzd5cWVDUEt1Njg?oc=5>

### Vertex Pharmaceuticals (VRTX) Posts Positive Phase 3 Results For Povetacicept
- Summary: Positive Phase 3 results for Povetacicept indicate strong clinical progress.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNZHJ3T19LVjBFdDc3RUxicks1UUFqdjlYNEZDZ19CNmRZeWdJc0tjbkZiNjY5NlZCSlhUaUtWSzNKbEhValJ1aWtiS2h6SzlyN3hVNzgzMlNzNTVPRzNXZTFlV1BPUHB3U1dUZy1IMWM4c3dDQ2k2bk5mZkd6VDUtazd5aUZVMGpjUTMtVW9reDk4aTBIcWFvUWNxLUFmN2lBR0FDOG1R?oc=5>

### Why Should You Think About Vertex Differently Now?
- Summary: Article suggests new perspective on Vertex’s strategy and potential growth.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNaUgtVU90SlhKRFFUM0hIbkh2dGNva1ZpM2I5S3pqQm9HZzRlcThJbWRXZm1Dc0ExSEMzZ0QyZDVISi1hbzdlSnJqUGxqMFdUSF96WGpkMmpWX3BCdmYtZEJiSEhGX2s0OG1NMnhuc0VSRFpnUWFBdmVjTlNPcUo4WThuUEJvN0VIMmxRM25Zd2RrMmhKV0U0RVllYVFhZw?oc=5>

### Vertex Pharmaceuticals Incorpor (VRTX) Stock Forecasts
- Summary: Forecasts predict future stock performance for Vertex.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQc0VzMGtueUtMc3NJN09ZTVpOUTJSaHY1WmdrV3VCTzQ1V0lnVVhFX2ZId2VSV1ZtcTN2aG4zN1pRVVVuSGx6STFzRExxY1lQaGxSN0F0Sm42QTNvMERLRFhZN2ZjdmJrdWlETFpZYThPbVpvYldjYTFZMDdwNDFpS0VsX0lqblM4RUFsYg?oc=5>

### Vertex Pharmaceuticals’ New Drugs Are Gaining Ground. Is That Enough for Investors?
- Summary: Discusses market acceptance of Vertex’s new drugs and investor implications.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOQmV1bzlLNFA2T2R0aTY0WEdKYTdWVmZycTFZcXkycjFQS3JVTDBfaEFLTzhlV0ZyZUpQdnV0cW1ubG5TdGx3WXJMZ2FZX0N5VmFhSmVwUTdNbEo2dExlNTliNXBnOFB1MkphcDBTTC1KNVpUd0RBejFtSXM1ME5SQkV6cDV0QVg0b1VfSTh3N2N1WHRYSWEyQlNkb240QThqOTBnVW5fWQ?oc=5>

### Vertex Pharmaceuticals Incorpor (VRTX) Stock forecasts
- Summary: Reiterates predictions on Vertex stock trajectory.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxPMnU5eTNjRFl4RkJHUERsVEN0U1BtdVhQeDQwb2lMUVM2SkViYkJEX05HbkVtMDV0YzJNQUx2ejRqQXF0WVhtZjIxeVUxUEdjU3BhQmNLMGtxa2VLNmswamZKRGxQOFNoeDA4Vy1aeWZGamhfUEFxMDI0UzhIQ1pDTFY4YVhLckFYeVhKVEZ4VVQ?oc=5>

### Vertex Pharmaceuticals (VRTX) Sees $11.6 Million in Net ETF Buying on Thursday
- Summary: Reports significant ETF buying activity in Vertex shares.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPd2EwdVRkTThwN1h6WjVxYkxtc205MzBOUUFONkZiWlpMMUJ1UV8xSW9kQjBJQ2tBZHIzYUZMX3lNTlktcWZ2UTFGc0tuTHVycExfa0VkM254SUxSZElkR2F6NkQtNzJHWjlwblhzMllmOEZWOWJEMWp5bURRNG9YOWxSRXhUdnRFTVVVdDBaTTh5ZklRMzI3MFRORGwwSWVhVmc?oc=5>

### What Vertex Pharmaceuticals (VRTX)'s Pancreas Recovery Data Means For Shareholders
- Summary: Positive pancreas recovery data could boost investor confidence and support share price.
- Date: 2026-10-18 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTVlMOE1RZ2FxZmVsV1VVZmVBWlNveVZpaEJTTmpyNHdvaGpjdEpQZHRvZkwzVXloX2QwcGhhV2JZMWpOUTAyVkNfZ0RtMDRidHBHUTRNTTNYemlYZnBXYnc1cHFxXzRKRDZsZGgtSExUY3ZXTUpqRFoyTFUtTEpWV1g2cFh3TFRsZjlRd1N2VFdMWGZyZXlrLWZUNVhxUnJobWtVandSdWJUZw?oc=5>

### Is Vertex Pharmaceuticals (VRTX) A Bargain After Its Phase 3 Kidney Trial Win?
- Summary: Phase 3 kidney trial success suggests undervaluation and potential upside.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxQZG5hRkFwbDdac3BTellXczFoU3QxVG5vbGlua09JYzlDTVZlV1l1aENQNjV3blp6WWRQazdwSV9GLWVJRUJnVnNEdTNqTl9zLU1wc3NIS3RfeXJ0OUgyNHhILWFBdTVVVzFMOU1qeGJicDRTa1pNMmtrVTZxcnJreDhKa0RiS0Q0WDRwbDBXN2thT1o3NlpzZW5xQVh0bnJaRWVmb3dCam9PdjRlanpyUnNVV3FkU2MxZU0zd3hyRlRHQ0Rlckk2UzFpNm5MWjlaUUVOTHlpMkhnb1hYN2otYU5KVnBWaGxNVjlqa9IB8gFBVV95cUxNSlRkeFoxU2Q0T0hhTGZLVEVrdlIzWW9fZW9JcnJ3SnlTREE5ejIyVW9mb0tmWVZ0NG1xZUxiaTZMUlVrck90RUlXbHByWE9uWlVZVTFiV1JoWjZXc0JvWVFkQXp4bWRTdjFyQWtRSHF0NWNaa2c4dWlOVkhGSm9POGxFTDdhTDZZenc3c3pDeURBaU5YZjBPOVpHOGhpN3BPWDVJUFZ0M1FTaWxXYlAydW9aLVV0UFk4T3BTZ1h2bllEY2ZLNHlqMzhlb0ZZRmtXamN5Qmg0ZnRxWUliSVY5NGVCS1lMWFIxX0FRQ3dlUXVSZw?oc=5>

### Vertex (VRTX) Stock Could Be 32% Undervalued Despite New ALYFTREK Data
- Summary: New ALYFTREK data indicates possible undervaluation, supporting a bullish outlook.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxPRVBqa2FOdFJKbHM2Q0JBSzRqckRRbW0zTm85SHdMRGJpNk9wdEQ1YVhFUDhpSW94bmhpVGM2a1dUOVlYRE96OWlwWW1hU3ZzeG5jc0pVZzVHekhwQ2UzbEpHaUdobGk5ZkIweDVjOTVZRDZ5d1lKV2Y5RUFyQlBZQjVtcEZSdWUtNnk3bWY2ODR6Z1VFd0VWaWh1dkpVQTdmSVV3NTFDRDdXRDRtNVdnR2Q4T1k1a1hBbFBTdFliWkU2MXJZSENiSG9xazN1YU5CNjVSQ09DOXRWTVZDU1RzU1cybVd1U1hXZUFaYtIB8gFBVV95cUxQWWlGancyZGYyODEwZ1VjdzRDc3UxWXBHb1lEQ2Q4TXB4UGRvNlgyZWJ6STUwRnl2blp5ZkcxcDd5Q3ZFemhuRTM0c0FlX0RvMUdyS0MxS2ZNMXRSbGxuR2pVaDFiSlNBVF8tTl9vQUx6bXZmaEpPTkdEMk55cnNEVl9TVFdOQVprWE1NS0RGMHdUMGJPUGk2WTVVcWxpNmtGZEN1NUt2cjRzX25MR2E1TUlMRm85U21MYXMwQjNfSjduMGtCdzdyd0hkOG13RmpQRk1GYmxsTGo0R3dIOVRZdEVPSnlHVXFKTXo5MmR6a1RSQQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Vertex Pharmaceuticals Incorporated Estimates – NASDAQ:VRTX
- Summary: Company releases earnings estimates for upcoming period.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE5GOHRJNC1Yems2S1BMVXZEWWhWU0hpMHVPTm1YenpFbmZyVERKNmZZbHB2dHNCUDBDZFZRZ0lWV0gzQ2VzZjdiM05uNFdwUURxTG15N1YxRl9yNU9xUUFSMmdSN1I1aksxNkcxWXZiNmUyN2VqMkZ0dw?oc=5>

### A finance executive with more than 35 years in health care joins Vertex's board.
- Summary: Vertex adds a seasoned finance executive to its board, enhancing governance and strategic oversight.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQTmhlNW11ZzVTN0I4OWstQ1hLaTcxcDIxZVFUbU5qMnRHTk8xYW9FMHF6dWtpdWt2NTNIMkdEOWowNzVZLThNZkNsZGdVSldBSlZfblc3cDZYVGdzZm5ZbGxnS2xSUkpDcFotcnlpZm8wb3ZxNnJWdy1yMHhaYmx5d3NMTm5BY3djQ2tzRTBZRmxhbjBGbDRkOE5aUDZLM2V4MHp3?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **VRTX** | **29.90** | **6.56** | **24.88** | **12.50** | **132,795,785,216.00 USD** | **23.97** |
| REGN | 19.91 | 2.55 | 15.97 | 16.70 | 82,880,831,488.00 USD | 40.55 |
| BIIB | 44.53 | 1.96 | 13.13 | 3.40 | 37,040,451,584.00 USD | 67.04 |
| AMGN | 27.28 | 20.32 | 16.26 | 9.50 | 237,478,019,072.00 USD | 54.13 |

Peers fetched as_of: 2026-10-25; VRTX reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-03
- Next expected earnings: 2026-11-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-04
- Revenue (latest available single quarter): 640,799,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 1,099,800,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/875320/000087532026000259/vrtx-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOUFgyYVJvNnAxN1I1bmZmcnZIQXIzVC1uNlZGUzZqR3ozSEEtYnV3T1p4ZG1TRGRhRUhRY1NJZllOUzBqTjVRUmdNelBKMV9BZ1dtcUk2bng3NlJFdjlEV0ZIUEg2TVFuZUNJZHFCQXRmNFVza2FidlZOLXZhbEFlM3QyY2pMNTJKLVJ5Z3A0T2VzLUs3Y19zVWtHWURmMnVXSzd5cWVDUEt1Njg?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNZHJ3T19LVjBFdDc3RUxicks1UUFqdjlYNEZDZ19CNmRZeWdJc0tjbkZiNjY5NlZCSlhUaUtWSzNKbEhValJ1aWtiS2h6SzlyN3hVNzgzMlNzNTVPRzNXZTFlV1BPUHB3U1dUZy1IMWM4c3dDQ2k2bk5mZkd6VDUtazd5aUZVMGpjUTMtVW9reDk4aTBIcWFvUWNxLUFmN2lBR0FDOG1R?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNaUgtVU90SlhKRFFUM0hIbkh2dGNva1ZpM2I5S3pqQm9HZzRlcThJbWRXZm1Dc0ExSEMzZ0QyZDVISi1hbzdlSnJqUGxqMFdUSF96WGpkMmpWX3BCdmYtZEJiSEhGX2s0OG1NMnhuc0VSRFpnUWFBdmVjTlNPcUo4WThuUEJvN0VIMmxRM25Zd2RrMmhKV0U0RVllYVFhZw?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQc0VzMGtueUtMc3NJN09ZTVpOUTJSaHY1WmdrV3VCTzQ1V0lnVVhFX2ZId2VSV1ZtcTN2aG4zN1pRVVVuSGx6STFzRExxY1lQaGxSN0F0Sm42QTNvMERLRFhZN2ZjdmJrdWlETFpZYThPbVpvYldjYTFZMDdwNDFpS0VsX0lqblM4RUFsYg?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOQmV1bzlLNFA2T2R0aTY0WEdKYTdWVmZycTFZcXkycjFQS3JVTDBfaEFLTzhlV0ZyZUpQdnV0cW1ubG5TdGx3WXJMZ2FZX0N5VmFhSmVwUTdNbEo2dExlNTliNXBnOFB1MkphcDBTTC1KNVpUd0RBejFtSXM1ME5SQkV6cDV0QVg0b1VfSTh3N2N1WHRYSWEyQlNkb240QThqOTBnVW5fWQ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPMnU5eTNjRFl4RkJHUERsVEN0U1BtdVhQeDQwb2lMUVM2SkViYkJEX05HbkVtMDV0YzJNQUx2ejRqQXF0WVhtZjIxeVUxUEdjU3BhQmNLMGtxa2VLNmswamZKRGxQOFNoeDA4Vy1aeWZGamhfUEFxMDI0UzhIQ1pDTFY4YVhLckFYeVhKVEZ4VVQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPd2EwdVRkTThwN1h6WjVxYkxtc205MzBOUUFONkZiWlpMMUJ1UV8xSW9kQjBJQ2tBZHIzYUZMX3lNTlktcWZ2UTFGc0tuTHVycExfa0VkM254SUxSZElkR2F6NkQtNzJHWjlwblhzMllmOEZWOWJEMWp5bURRNG9YOWxSRXhUdnRFTVVVdDBaTTh5ZklRMzI3MFRORGwwSWVhVmc?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTVlMOE1RZ2FxZmVsV1VVZmVBWlNveVZpaEJTTmpyNHdvaGpjdEpQZHRvZkwzVXloX2QwcGhhV2JZMWpOUTAyVkNfZ0RtMDRidHBHUTRNTTNYemlYZnBXYnc1cHFxXzRKRDZsZGgtSExUY3ZXTUpqRFoyTFUtTEpWV1g2cFh3TFRsZjlRd1N2VFdMWGZyZXlrLWZUNVhxUnJobWtVandSdWJUZw?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxQZG5hRkFwbDdac3BTellXczFoU3QxVG5vbGlua09JYzlDTVZlV1l1aENQNjV3blp6WWRQazdwSV9GLWVJRUJnVnNEdTNqTl9zLU1wc3NIS3RfeXJ0OUgyNHhILWFBdTVVVzFMOU1qeGJicDRTa1pNMmtrVTZxcnJreDhKa0RiS0Q0WDRwbDBXN2thT1o3NlpzZW5xQVh0bnJaRWVmb3dCam9PdjRlanpyUnNVV3FkU2MxZU0zd3hyRlRHQ0Rlckk2UzFpNm5MWjlaUUVOTHlpMkhnb1hYN2otYU5KVnBWaGxNVjlqa9IB8gFBVV95cUxNSlRkeFoxU2Q0T0hhTGZLVEVrdlIzWW9fZW9JcnJ3SnlTREE5ejIyVW9mb0tmWVZ0NG1xZUxiaTZMUlVrck90RUlXbHByWE9uWlVZVTFiV1JoWjZXc0JvWVFkQXp4bWRTdjFyQWtRSHF0NWNaa2c4dWlOVkhGSm9POGxFTDdhTDZZenc3c3pDeURBaU5YZjBPOVpHOGhpN3BPWDVJUFZ0M1FTaWxXYlAydW9aLVV0UFk4T3BTZ1h2bllEY2ZLNHlqMzhlb0ZZRmtXamN5Qmg0ZnRxWUliSVY5NGVCS1lMWFIxX0FRQ3dlUXVSZw?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxPRVBqa2FOdFJKbHM2Q0JBSzRqckRRbW0zTm85SHdMRGJpNk9wdEQ1YVhFUDhpSW94bmhpVGM2a1dUOVlYRE96OWlwWW1hU3ZzeG5jc0pVZzVHekhwQ2UzbEpHaUdobGk5ZkIweDVjOTVZRDZ5d1lKV2Y5RUFyQlBZQjVtcEZSdWUtNnk3bWY2ODR6Z1VFd0VWaWh1dkpVQTdmSVV3NTFDRDdXRDRtNVdnR2Q4T1k1a1hBbFBTdFliWkU2MXJZSENiSG9xazN1YU5CNjVSQ09DOXRWTVZDU1RzU1cybVd1U1hXZUFaYtIB8gFBVV95cUxQWWlGancyZGYyODEwZ1VjdzRDc3UxWXBHb1lEQ2Q4TXB4UGRvNlgyZWJ6STUwRnl2blp5ZkcxcDd5Q3ZFemhuRTM0c0FlX0RvMUdyS0MxS2ZNMXRSbGxuR2pVaDFiSlNBVF8tTl9vQUx6bXZmaEpPTkdEMk55cnNEVl9TVFdOQVprWE1NS0RGMHdUMGJPUGk2WTVVcWxpNmtGZEN1NUt2cjRzX25MR2E1TUlMRm85U21MYXMwQjNfSjduMGtCdzdyd0hkOG13RmpQRk1GYmxsTGo0R3dIOVRZdEVPSnlHVXFKTXo5MmR6a1RSQQ?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTE5GOHRJNC1Yems2S1BMVXZEWWhWU0hpMHVPTm1YenpFbmZyVERKNmZZbHB2dHNCUDBDZFZRZ0lWV0gzQ2VzZjdiM05uNFdwUURxTG15N1YxRl9yNU9xUUFSMmdSN1I1aksxNkcxWXZiNmUyN2VqMkZ0dw?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQTmhlNW11ZzVTN0I4OWstQ1hLaTcxcDIxZVFUbU5qMnRHTk8xYW9FMHF6dWtpdWt2NTNIMkdEOWowNzVZLThNZkNsZGdVSldBSlZfblc3cDZYVGdzZm5ZbGxnS2xSUkpDcFotcnlpZm8wb3ZxNnJWdy1yMHhaYmx5d3NMTm5BY3djQ2tzRTBZRmxhbjBGbDRkOE5aUDZLM2V4MHp3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
