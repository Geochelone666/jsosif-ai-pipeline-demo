# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:07:09.644044+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 4, 'ai': 11, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 44.0%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 217.9400 |
| Return 1D (%) | 0.8981 |
| Return 1W (%) | 0.6791 |
| Return 1M (%) | -3.1679 |
| Return YTD (%) | 17.1314 |
| Return 1Y (%) | 14.0854 |
| Annualized volatility (%) | 37.5912 |
| Beta vs SPY | 1.9337 |
| Max drawdown (%) | -20.2144 |
| Sharpe (rf=0) | 0.5385 |
| Downside deviation (rf=0, %) | 25.2659 |
| Sortino (rf=0) | 0.8013 |
| Historical VaR 95% (1D, %) | 3.7736 |
| Historical ES 95% (1D, %) | 4.5600 |
| Correlation vs SPY | 0.6533 |
| Tracking error vs SPY (%) | 30.8310 |
| P/E (trailing) | 27.55 |
| P/B | 22.98 |
| EV/EBITDA | 25.98 |
| Revenue growth (%) | 105.90 |
| Forward P/E (estimate) | 13.69 |
| Gross margin (%) | 74.67 |
| Operating margin (%) | 66.24 |
| Return on equity (%) | 117.21 |
| Free cash flow yield (%) | 0.79 |
| MA50 | 222.0794 |
| Close vs MA50 (%) | -1.8639 |
| MA200 | 203.6868 |
| Close vs MA200 (%) | 6.9976 |
| RSI (14, Wilder) | 46.3053 |
| MACD (12,26) | -2.5817 |
| MACD signal (9) | -1.2506 |
| MACD histogram | -1.3311 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 217.9400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.8981 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.6791 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.1679 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 17.1314 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 14.0854 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.5912 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.2659 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8013 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7736 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.5600 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6533 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.8310 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.9337 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2144 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5385 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.6943 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.2370 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.2110 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.7945 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.5525 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 46.3053 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.3311 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -1.8639 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.9976 -> Clearly above the moving-average trend level.

## TAILWINDS

### NVIDIA (NASDAQ:NVDA) Stock Price Up 2.4% - What's Next?
- Summary: NVIDIA (NASDAQ:NVDA) Stock Price Up 2.4% - What's Next?
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOd3QtUS1INzUwaDdYUktGRWF2NUlfa2xfQWVYT1VBZFM2c0c5TTlqWTZfWjduOWp1Wlg3NmxKdzRFYk5BSVdKRzN2OUJIcnZwZlB1S1VFelBkdG5sTFQ1dXpscjRKZVl2Z1QzNWIyS1dZdUt3a1JTVVhMYzJCLUpPdGJJVGNzd3M2SnFqTGtKaEtDcWRabzBzNXZFcEhpenlxWFF3bEtaUmlQcGc?oc=5>

### NVDA Stock Ticks Higher Overnight: a16z Data Shows GPU Rental Prices Rising Sharply, Even For Older Chips
- Summary: NVDA Stock Ticks Higher Overnight: a16z Data Shows GPU Rental Prices Rising Sharply, Even For Older Chips
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNVzhIbU14cHlhdjlKTUNmTkpxbXBMTXRHb2U5Wk1rMVg0dEhwX216VVJmUEhfT3l5SUtKZVB0ZU91QklIdERHMDRzSXhmcExnMmJxSUxNMUhJNmpYdEN4bUFMTXlwbjY4WjRENmZyR0JfQWMwTWxramtEVi0teDZWOUVMTUVFRjJSTGg2NjJ6eTVXYmFxWllIT1BQeHFGemM?oc=5>

### Nvidia (NVDA) Surpasses Market Returns: Some Facts Worth Knowing
- Summary: NVDA outperformed market returns, indicating strong performance.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQdnNyZ1g4R2pVdTJTQW1HNE53cGJLSDVBbGFTUWZlOFd0akxCQUJ6SzBwWVVlaDFYZjlLdXA3TktObUZrdnJRX1lCcEFnbDBvZTliYUVCeC1OUDMtVGxhT2pvVWxnYm05UUhEUnRER1NGbFVLZmhWVG8wYVcxQ3hKRHdjdnNkMkRGWFFuRjBFRjdUeE5oU1drR3oxV2tyUUFCcExN?oc=5>

### ETFs Are Buying NVIDIA (NVDA) on Thursday
- Summary: ETFs are purchasing NVDA shares, indicating increased institutional demand.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQRDhlSHItazZid1JpaGpGOVJSb0tMUENleERVZEVyX3pMaklPcXJwRDBqQlFVcTRBTzZ5ZXM4ZEMzRWdHS2oyaV8yNUFBeFFqU0l2UDZCd0s2THhnMUJkMGRfeWpNb2tJVjZaLXNmblNDdWlaczJPTjQwYkVsTzRaeVN0MlgzcG5ob3U5V05raGowQ2hGRVEzMjJQNTVnUQ?oc=5>

## HEADWINDS

### Elon Musk Just Delivered a Sweeping Blow to Nvidia Investors
- Summary: Negative impact on NVDA investors due to Musk's actions.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQdFlrYjBrclR0Z1h0LTZJejNtYXRkbWRQb3NkSENTdVlicWxDTWFzRXp4V0pfYWhLX0xQVzc1NVZkUThPOFkzLXBQOXdVV193ZkpPVk9LNXAwQnV3N0VPNE81Zk5wM3YxLVYwRGNQbjFLRzF4N21GdzhTSVFPTUktMDM1cG5RdDBxUEJSOGtOall0UkRNMnBKTg?oc=5>

## CATALYSTS

### Nvidia Stock $216: SpaceX $40B GPU Deal, Bull $243
- Summary: Nvidia Stock $216: SpaceX $40B GPU Deal, Bull $243
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxOT2ZzTjNmanRRMnAxOW5GZTR0Y2hPU1NtZ29TOElBa3BfTHVlR2pCUzQ5UTBkRGtyeHhNWkhpZUlKZDN2UnRVdG1wNzdHeUhoakNhbmFaSkhBeF9vY1ZLajNLWk9mQmVSYXJjbldsYUIwYS1ycnplSnQtZ1lvVlZYV0RMcjdueXgtOUd5aEQzVER3bHh0c21MUWl6RGJzRkxfNjlmOWZsRjJpMWY0Mnp4b2NPWGJ1UjlNbm1vbQ?oc=5>

### Nvidia (NASDAQ:NVDA) to Invest $3 Billion in Meta (NASDAQ:META) Share Offering as AI Partnership Expands
- Summary: Nvidia (NASDAQ:NVDA) to Invest $3 Billion in Meta (NASDAQ:META) Share Offering as AI Partnership Expands
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPa3p2ZDNFSE9sdnIwSWVWN1hTX2JaUzV0am9lNlNzS3VKbEpBbDRaWjRORlVOUjNSam9jdjF1anE1eVkzZlFUWTc5X0Y4VHJqaVd2anVKS09CQWNVSHliMUFkNERSbU1sOTZ2OUxOSW8tVmZlVEhrNjYwLUhUZVFVLVpxUmFkaXdyMVhlYU5jVk45NEY1VXc?oc=5>

### NVDA Stock Alert: What to Know as Nvidia Invests $3 Billion in Meta
- Summary: Nvidia invests $3B in Meta stock, expanding AI collaboration.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPWnl5Qi1MY0NrMUF0ODAzM3hvbUxLMkpLRnBrMlp2RExVQkx5eEhtZW0zdVdac1pPNGowX1JBUkYzX3BHYWtVRnZtOGFZbzdoYV9oY3hpenJXcnltOE5IUEtKc21zRktPb0Q3cTRGX2VXc2FaUzFGZVRjWkZrc29veEdoX1pIazh6Wm5Rdy1CYkRFUUhQS0NNb01DSVE4SThlRkFiNWZmdkdQUF9qcVE?oc=5>

### Nvidia to invest $3B in Meta stock, expand AI collaboration on Muse models (NVDA:NASDAQ)
- Summary: Nvidia invests $3B in Meta stock, expanding AI collaboration.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNc0hJUV8wbklYTWx4NVlpcnNNSlV3WExEaGhDV3hNckpkaHhMUUUtcFdVV3YyWmRnTF9wWnhBVkY4eGhLLTlsT0d3SXJORk12NVhSWVo1RVpKS0xjNFRrWGpFYU4wN0ZUak9pbFpjdnYtQWZUaVRma09wcGJLU253VjVoSlZYdzE1eTNPUXBsbVh2VnduNlMyWEJsWFNvR3VadW9mdmhRQW9NTFVSdkZB?oc=5>

### What Is Going on With Nvidia Stock on Tuesday?
- Summary: Inquiry about Nvidia stock movement on Tuesday.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQQVRRXzl6ZXlFNmFmRk1pZWxSOVE3VlM3Y3gzbEt5SkQwRV9fTTllblRQRWNhR05nVzNXeWdZVmNSR21LMWE1R1JBOEo2VldNODBpczQ1WlFMWG9wU085WDNZUGVUS3dYc3ZEcUltZzB1VkRCZ09IWkRmSzlyWGE5d01rVjJnRHh2SlVvSExuYkd6ZXRlM2tNM28zWmJKNC16VlE?oc=5>

### ETFs Are Net Sellers of NVIDIA (NVDA) on Oct. 23
- Summary: ETFs sold Nvidia shares on Oct. 23.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOdEJPRFZtT2h5TFdxZFBQVzBsOXlxX1prcWJHLTliS29yWjZOblQ1ZlVYWkJvZzVibm1xRFNiTlJQNVBuZmgyTWRBTkFiRG9VeThpQlRaQ3NqUUdDMlFUb0h2NHM3ZWxqR1VsLXNKUU5wcDh2QkZHRGd5R09UQ3UyOHhDQkdwWUVKYWtScy1qQmVsSC11LTh2Vg?oc=5>

### Nvidia: Berlin Keynote Signals A More Vertically Integrated Future
- Summary: Nvidia outlines future strategy at Berlin keynote.
- Date: 2026-10-27 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPQjRJd3NWTEZka0RiaWFCM3VRLVJaSTM0Vm9LemRIZkIzRHhVa0lTb0VQcm5icFFaSU05ODBvT2JibkpTZnBTQ3FpWGVUS0tsSHhMT3E1TlFiOWdNUm9fTG9MWFc1NUdjcG5wWkZCUEVHSHZmM2luNlRZUzBDUS1ycVZlcXNHWVdmV2d6WVhIdE1ILV9EYmlPd2ZqNDlVVU9OamsxZGhwblVDZw?oc=5>

### Nvidia Just Announced Plans to Pour Billions Into Meta's Muse
- Summary: Nvidia announced a multi‑billion dollar investment in Meta’s Muse AI platform, signaling a strategic partnership to enhance AI capabilities.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQQklZdXZGd3E4dUlIenhZRDQzRXNXQmlBcW03ZU9qcmlBdmRSakY5THJCVUtxTGpSUlVTSld1WjRiOVEwQ3ZTUFRYeUJNQkt0RlhoN3hCY3BrNHRSY3VXRGhsYVoyRThBTlM1OTlEbEU1NDY5NDZ3WXM5dUpTVkdPSUlVWFFkYjF5ODRNS0RRbVJZajJYX1JPRDN6M1dHSEhMR2ZJT0h3?oc=5>

### Nvidia Picks Up $3B Stock In Meta's Equity Offering, Will Help Improve Muse AI Platform
- Summary: Nvidia purchased $3 billion of Meta stock to support the Muse AI platform, strengthening collaboration between the companies.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQbGpWWWxhdjZ6bFFVbnA2blZ6V3AxNzY3S0daQ3h0ZFEzVkhpQmJOVWFiRlFLZXZXMl9CT1RRcWM2X19LWm1zR1AxWk4zQUUyWXRiVU55cFdiR1g1Q3EwXzRvSzJqWW9QQ2JvTllfT0FGSGRTMGdjdllQTEE4bUtRTjZZdlNHQnBkd3NuOEVTejUyYi01Y1E?oc=5>

## RISKS

### Nvidia (NVDA) Has Lost Its China AI Accelerator Market
- Summary: Nvidia lost its China AI accelerator market, indicating a decline in regional market share.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNZXBrdnEtYnZLWk95RmJjZlRTeFR2ZjZDaGM5dDR4VW9KNWdDZjRjTmJidlY0eWExNVJVYUZ2NGJlNlo3NXZYMzFTZkhYeUU4ZC1RSGUzMXhLYkdkRUZXMEt5bVJRY1E0LW52Z0QzaWFYRTE3bDh1SVBMWnRNZUs0dndHVXBXdmZkYjBoRWFsX0p6RG8?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **27.55** | **22.98** | **25.98** | **105.90** | **5,262,596,898,816.00 USD** | **14.09** |
| AMD | 142.92 | 13.60 | 94.73 | 50.10 | 914,610,454,528.00 USD | 115.76 |
| AVGO | 43.72 | 16.39 | 31.95 | 85.50 | 1,634,156,675,072.00 USD | -4.74 |
| INTC | N/A | 5.40 | 30.24 | 25.40 | 495,519,465,472.00 USD | 137.08 |

Peers fetched as_of: 2026-10-27; NVDA reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-26
- Revenue (latest available single quarter): 96,221,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- Net income (latest available single quarter): 59,688,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOd3QtUS1INzUwaDdYUktGRWF2NUlfa2xfQWVYT1VBZFM2c0c5TTlqWTZfWjduOWp1Wlg3NmxKdzRFYk5BSVdKRzN2OUJIcnZwZlB1S1VFelBkdG5sTFQ1dXpscjRKZVl2Z1QzNWIyS1dZdUt3a1JTVVhMYzJCLUpPdGJJVGNzd3M2SnFqTGtKaEtDcWRabzBzNXZFcEhpenlxWFF3bEtaUmlQcGc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNVzhIbU14cHlhdjlKTUNmTkpxbXBMTXRHb2U5Wk1rMVg0dEhwX216VVJmUEhfT3l5SUtKZVB0ZU91QklIdERHMDRzSXhmcExnMmJxSUxNMUhJNmpYdEN4bUFMTXlwbjY4WjRENmZyR0JfQWMwTWxramtEVi0teDZWOUVMTUVFRjJSTGg2NjJ6eTVXYmFxWllIT1BQeHFGemM?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQdnNyZ1g4R2pVdTJTQW1HNE53cGJLSDVBbGFTUWZlOFd0akxCQUJ6SzBwWVVlaDFYZjlLdXA3TktObUZrdnJRX1lCcEFnbDBvZTliYUVCeC1OUDMtVGxhT2pvVWxnYm05UUhEUnRER1NGbFVLZmhWVG8wYVcxQ3hKRHdjdnNkMkRGWFFuRjBFRjdUeE5oU1drR3oxV2tyUUFCcExN?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQRDhlSHItazZid1JpaGpGOVJSb0tMUENleERVZEVyX3pMaklPcXJwRDBqQlFVcTRBTzZ5ZXM4ZEMzRWdHS2oyaV8yNUFBeFFqU0l2UDZCd0s2THhnMUJkMGRfeWpNb2tJVjZaLXNmblNDdWlaczJPTjQwYkVsTzRaeVN0MlgzcG5ob3U5V05raGowQ2hGRVEzMjJQNTVnUQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQdFlrYjBrclR0Z1h0LTZJejNtYXRkbWRQb3NkSENTdVlicWxDTWFzRXp4V0pfYWhLX0xQVzc1NVZkUThPOFkzLXBQOXdVV193ZkpPVk9LNXAwQnV3N0VPNE81Zk5wM3YxLVYwRGNQbjFLRzF4N21GdzhTSVFPTUktMDM1cG5RdDBxUEJSOGtOall0UkRNMnBKTg?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxOT2ZzTjNmanRRMnAxOW5GZTR0Y2hPU1NtZ29TOElBa3BfTHVlR2pCUzQ5UTBkRGtyeHhNWkhpZUlKZDN2UnRVdG1wNzdHeUhoakNhbmFaSkhBeF9vY1ZLajNLWk9mQmVSYXJjbldsYUIwYS1ycnplSnQtZ1lvVlZYV0RMcjdueXgtOUd5aEQzVER3bHh0c21MUWl6RGJzRkxfNjlmOWZsRjJpMWY0Mnp4b2NPWGJ1UjlNbm1vbQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPa3p2ZDNFSE9sdnIwSWVWN1hTX2JaUzV0am9lNlNzS3VKbEpBbDRaWjRORlVOUjNSam9jdjF1anE1eVkzZlFUWTc5X0Y4VHJqaVd2anVKS09CQWNVSHliMUFkNERSbU1sOTZ2OUxOSW8tVmZlVEhrNjYwLUhUZVFVLVpxUmFkaXdyMVhlYU5jVk45NEY1VXc?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPWnl5Qi1MY0NrMUF0ODAzM3hvbUxLMkpLRnBrMlp2RExVQkx5eEhtZW0zdVdac1pPNGowX1JBUkYzX3BHYWtVRnZtOGFZbzdoYV9oY3hpenJXcnltOE5IUEtKc21zRktPb0Q3cTRGX2VXc2FaUzFGZVRjWkZrc29veEdoX1pIazh6Wm5Rdy1CYkRFUUhQS0NNb01DSVE4SThlRkFiNWZmdkdQUF9qcVE?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNc0hJUV8wbklYTWx4NVlpcnNNSlV3WExEaGhDV3hNckpkaHhMUUUtcFdVV3YyWmRnTF9wWnhBVkY4eGhLLTlsT0d3SXJORk12NVhSWVo1RVpKS0xjNFRrWGpFYU4wN0ZUak9pbFpjdnYtQWZUaVRma09wcGJLU253VjVoSlZYdzE1eTNPUXBsbVh2VnduNlMyWEJsWFNvR3VadW9mdmhRQW9NTFVSdkZB?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQQVRRXzl6ZXlFNmFmRk1pZWxSOVE3VlM3Y3gzbEt5SkQwRV9fTTllblRQRWNhR05nVzNXeWdZVmNSR21LMWE1R1JBOEo2VldNODBpczQ1WlFMWG9wU085WDNZUGVUS3dYc3ZEcUltZzB1VkRCZ09IWkRmSzlyWGE5d01rVjJnRHh2SlVvSExuYkd6ZXRlM2tNM28zWmJKNC16VlE?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOdEJPRFZtT2h5TFdxZFBQVzBsOXlxX1prcWJHLTliS29yWjZOblQ1ZlVYWkJvZzVibm1xRFNiTlJQNVBuZmgyTWRBTkFiRG9VeThpQlRaQ3NqUUdDMlFUb0h2NHM3ZWxqR1VsLXNKUU5wcDh2QkZHRGd5R09UQ3UyOHhDQkdwWUVKYWtScy1qQmVsSC11LTh2Vg?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPQjRJd3NWTEZka0RiaWFCM3VRLVJaSTM0Vm9LemRIZkIzRHhVa0lTb0VQcm5icFFaSU05ODBvT2JibkpTZnBTQ3FpWGVUS0tsSHhMT3E1TlFiOWdNUm9fTG9MWFc1NUdjcG5wWkZCUEVHSHZmM2luNlRZUzBDUS1ycVZlcXNHWVdmV2d6WVhIdE1ILV9EYmlPd2ZqNDlVVU9OamsxZGhwblVDZw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQQklZdXZGd3E4dUlIenhZRDQzRXNXQmlBcW03ZU9qcmlBdmRSakY5THJCVUtxTGpSUlVTSld1WjRiOVEwQ3ZTUFRYeUJNQkt0RlhoN3hCY3BrNHRSY3VXRGhsYVoyRThBTlM1OTlEbEU1NDY5NDZ3WXM5dUpTVkdPSUlVWFFkYjF5ODRNS0RRbVJZajJYX1JPRDN6M1dHSEhMR2ZJT0h3?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQbGpWWWxhdjZ6bFFVbnA2blZ6V3AxNzY3S0daQ3h0ZFEzVkhpQmJOVWFiRlFLZXZXMl9CT1RRcWM2X19LWm1zR1AxWk4zQUUyWXRiVU55cFdiR1g1Q3EwXzRvSzJqWW9QQ2JvTllfT0FGSGRTMGdjdllQTEE4bUtRTjZZdlNHQnBkd3NuOEVTejUyYi01Y1E?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNZXBrdnEtYnZLWk95RmJjZlRTeFR2ZjZDaGM5dDR4VW9KNWdDZjRjTmJidlY0eWExNVJVYUZ2NGJlNlo3NXZYMzFTZkhYeUU4ZC1RSGUzMXhLYkdkRUZXMEt5bVJRY1E0LW52Z0QzaWFYRTE3bDh1SVBMWnRNZUs0dndHVXBXdmZkYjBoRWFsX0p6RG8?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
