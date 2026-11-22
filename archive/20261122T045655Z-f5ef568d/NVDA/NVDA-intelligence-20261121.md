# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-21**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-21**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-22T05:14:18.401676+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 7, 'ai': 7, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261121T053104Z-422ce34b/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 7 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 54.17%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 125.5300 |
| Return 1D (%) | -14.0088 |
| Return 1W (%) | -22.9168 |
| Return 1M (%) | -42.0104 |
| Return YTD (%) | -32.5342 |
| Return 1Y (%) | -30.3417 |
| Annualized volatility (%) | 41.1536 |
| Beta vs SPY | 1.8981 |
| Max drawdown (%) | -47.5297 |
| Sharpe (rf=0) | -0.6738 |
| Downside deviation (rf=0, %) | 31.3311 |
| Sortino (rf=0) | -0.8850 |
| Historical VaR 95% (1D, %) | 4.2460 |
| Historical ES 95% (1D, %) | 5.8772 |
| Correlation vs SPY | 0.6593 |
| Tracking error vs SPY (%) | 33.4994 |
| P/E (trailing) | 13.48 |
| P/B | 11.35 |
| EV/EBITDA | 12.19 |
| Revenue growth (%) | 103.20 |
| Forward P/E (estimate) | 7.56 |
| Gross margin (%) | 74.92 |
| Operating margin (%) | 66.08 |
| Return on equity (%) | 117.36 |
| Free cash flow yield (%) | 3.27 |
| MA50 | 207.0004 |
| Close vs MA50 (%) | -39.3576 |
| MA200 | 203.0853 |
| Close vs MA200 (%) | -38.1885 |
| RSI (14, Wilder) | 15.0466 |
| MACD (12,26) | -19.8282 |
| MACD signal (9) | -15.1980 |
| MACD histogram | -4.6302 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 125.5300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -14.0088 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -22.9168 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -42.0104 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -32.5342 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -30.3417 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.1536 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 31.3311 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.8850 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2460 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.8772 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6593 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.4994 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8981 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.5297 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.6738 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 7.5596 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.9210 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.0820 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.3640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.2740 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.4834 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 15.0466 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.6302 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -39.3576 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -38.1885 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Nvidia Stock Is Down 35% From Its High. History Suggests a $5,000 Investment Now Will Be Worth This Much by 2028.
- Summary: Nvidia Stock Is Down 35% From Its High. History Suggests a $5,000 Investment Now Will Be Worth This Much by 2028.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxOWjNFQ3VvT3Foa1Z3aHRaUFFWZmMydmxQa1piMVpXaC1ycHBRMHFzWTRWeFlvUUVJSEUydzV4U29TZGhxMXAwQ3Z0elE1MWR6TXVTcHlDenljRlRJZ2c5aE1pTm1NYVk3TlNPUldEaXdLcmdsNlZWZjhmT19yWHE3akFWWF85MWM5a3RLZ3g0d05HNmwtVjc4bV8zY18tenVPb2VwdWVvZXI3TW1VTG15N3JjTFRnSERQN0xNVU1HdEJLaWw1MHpIMWhROFJfUWlBYWdfbTdueFdDLW5GY2JIYW1ETmRJMVNoTmZr?oc=5>

### NVDA Stock Alert: What to Know as Moody's Cuts Nvidia's Outlook Rating
- Summary: NVDA Stock Alert: What to Know as Moody's Cuts Nvidia's Outlook Rating
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQQmI0cjQ4cUVpYjVTeXNuNFdNRmE4bHFJTDBsbDBNLS1LZGEzeFhsUVRvYzltRjA0YUU4RnYzS1htMkNHTDRDcHdfQXk4QjdRYloyQVRJWGtlLXhHNmJiMmVQMVhJNTduQXNZdld6ald5SmN0bUVHWUJpbmRBR2RIN2tVdEI2cG9hcXNMeExDd1JWNFBtS0JLQlkzWERheDhVSWZVZ3Z1RUNsc21zRjVQNWg4cw?oc=5>

### NVDA Stock Down 40% From October Peak Amid China Spying Crisis: California Begins Probe Into Chip Sales
- Summary: NVDA Stock Down 40% From October Peak Amid China Spying Crisis: California Begins Probe Into Chip Sales
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQcGFEcVVtVlZRa1Ztb2lLeXpXcXJsdXF3VW80WnQ4bWQ5bW9aWFhGZXgySGV2enlZMlFCdHJXV1MwVW5QQUNlNEdKTDU4dXBsU2l0MTk3VkRwcU5mbmctRkt0NU5GS2tvSDRxTF9WUlYxNTR5TXN3ZVEzVjVQcmxJcFRoZlQ3Q2VrVnJqaUdGX3pqczYtTnc?oc=5>

### Nvidia Just Issued a Major Warning to AMD and Intel Stock Investors
- Summary: Nvidia Just Issued a Major Warning to AMD and Intel Stock Investors
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxOT2FGV192VllUQ19HUkJtU296SWE3UFFvNjRkS2NIWXpBNzRtaF9uMVVvZ2ZjVFBHVVY0UG1nZ0pBc1NjeURyOTBxNy1Rc3JJelRsY1BCbDBPNmtsSlQ2clRkcDJUQ2N4RFRSRXJHR1BlNmhZY3hZaDVLaU1hZVF4WFpCMmdDRVdSOFlheUlxNWVvbW9GTTk4RGkzc012cjAtNG02Y2IxWEJvekFNbFI0?oc=5>

### Nvidia (NVDA) Stock Drops Despite Q3 Results Showing Huge AI Earnings
- Summary: Nvidia (NVDA) Stock Drops Despite Q3 Results Showing Huge AI Earnings
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPWHNRcEVuR1ViVWpUY0p5RnIyekVpWDRTVUFLXzhLYnFDZ2tfeGctTGFkcENyRFliRXVRSktrc3hiTU01ZW9oY1dzaVJ2dzBNcTBxLWZienhFM0I0dVFDYXp3NTVjM3lZNGhxMXpuZUhuLXdUd1o0RTN2VVR0bzRDNnE0LXByUDJvWFl3VUFra1JDQXZmbV9FejNKdEI?oc=5>

### Nvidia Stock Falls to $150 Per Share. Is It a Buy Now?
- Summary: Nvidia Stock Falls to $150 Per Share. Is It a Buy Now?
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNZnBlVDFLTGxBQnRDYXJ5YTNuS1drVnhWVDh4N2o0aWlta1RyeXE1OGdmbVgzNU93OGcxWXNqR2k5X1VUOXN2SVdSc19FeExkcFNtU0hiZ0FOREhQVF9vdGp4Sm1PaURXWlBjdEJlU2s4LVFuWnJzS1A5ZjlNOEZsWTJvNGNWOTRJR2Z3T2sxQ25nV0VzTWhrQWFudFhrdw?oc=5>

### Nvidia stock plunges 14%, wraps up longest weekly losing streak since 2008 financial crisis
- Summary: Nvidia shares fall 14%, ending a historic weekly losing streak.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOSXJZbEJSVExtUGxySHJ5eFBaLTRFV0dTRWFjY244NWdhVTZ5cENMNXBqcVhBS08xLS1oSG5jbVJTME9QdWZKcXlzOXpTN3ZmMFZrREtNVzhHUVFMZXBmTndDUklLWFFrOGlpNTc5Y3dQR25mMjhXdGlSbl9SNVBfbFVOVXhCZTg3a3gtVUwyN1FWOVZ6NWIwRXUxZTdReG56V1MxeGdIONIBrAFBVV95cUxNN3pqQmZoNHdVc1M2SHpMWERNaDNHOUVyRGNDM3dlVzdGR19IaVdyRG5mQ0p6SzBZYlpWemdoZDN1M3NzZVpVVWpNVkFGa2ZpT3g0YVR1aFBLb0RoWm5mM0EwMkRkdmEtNndicG9iTHNLTGU4VUg4XzdPNWpDd0tYMWItNFM1NDNuMTN5OHEwbWFBNUloZEh6ekdsYW5WY2FXSHZjcmgxS3M5Tmx0?oc=5>

### The post earnings slide in Nvidia stock is getting uglier by the day
- Summary: Nvidia’s post‑earnings performance deteriorates, worsening investor sentiment.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxQYVo0b1dObGhWclp0S0JnV095MjVJVEx3QW1hQ3FIdk9VZ3NNZWt2cHp3YnVqbm9EVFJ1UXFlOG1YRmpNdV9CSEFTQ2Z1b0FfdGpaMFJjNVRxZEl5bDJzQ21oLTM1NnNkdHV2LXRvd3p5UjRnQktpanhIcHFPM3FONTlUZTZOU3lqME9rbEdXNVBlcER0WDZNSUxGOWkxaDhDRXI1YUFfcmFvWjliZDQ4UnhVeTNNVUpyN2Z6RUVMRkM4Q2lTdkJsYjBKajM?oc=5>

### Nvidia stock extends $2.5 trillion rout as SEC probe reportedly investigates its accounting
- Summary: SEC probe into Nvidia’s accounting fuels a sharp decline in its stock, extending a massive market rout.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxQS25iVW9uNHFsc3lYdkNPRTJyTUhYcWRVbjhOZlR4QUpLZGs4RkE0d1lSLTEtN2x6N0ZxZnlZdE9KaTQxeS1TbWRFaGFpd0hGc0ZKWmF5OEVRdnFDX1NNWFlBTl9rdVRUVFlxSVRIelpPNmluWVdUVElhQzh1NWtjemJaUnlhRnJ2N3Q2dDNVYlhVYWtXbkswbXhYLWdiOHE0V1dkQ2xjNjFsTlpEQ0hzRDBja0RqV0VFX0FZaXdKRVZ2RHdGVUUtS2VzanJrTkhiSVcxeGVCRXNlUUhSVWJ3?oc=5>

### Nvidia Stock Price Forecast: Technical Signals Say Sell, but Analysts See 70%+ Upside
- Summary: Technical sell signals clash with analyst upside projections, creating uncertainty for Nvidia’s stock price.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNNnhJbmItN2ItMlRsSjJXMTNva0laLXROMVJIck1sczVBMUNtQmNOVlZFcVpaaVp1QS1ZWUtQNU5kLXItbTEtTXlXdzMzOXhMYXhCNnhOWWI1YWM5c05jSXo2cHhHb2lEU3h4V2JnSEY4bnpBOWltT2hGSHlvRUZLRWo5WlFGX0VMUTJDMEtTdW1qT21WanFrYUtvMG1mR0psdEdIYWp5Q1J3VFdhVnJtMw?oc=5>

## CATALYSTS

### NVIDIA Doubled Its Revenue in Its First Quarter Without Huang. Here’s Our Price Target.
- Summary: NVIDIA Doubled Its Revenue in Its First Quarter Without Huang. Here’s Our Price Target.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNMnc5TjJWdmVlZ255ZjJOaUpXa3FzWVJYdXVrQjRoRWVxTmtpRXptS21fX3h3a3ZXMXZIQjVNYnd6N25XSURjYzlKV3JOMkE0Yk9LanRZcGZLelgxSzc3YkVOZk9UYnJCSmxuVUVqSDNpNXBIdUdvODl2VmJKdUNRR0FyM0pVbFpGYmVLbm5IUWNkbkVIb0s5MFRRdmhKWWhoQ013?oc=5>

### Trump Bought Up to $265,000 of NVIDIA Stock. Here’s Where the Price Target Stands
- Summary: Former President Trump purchased $265,000 worth of NVIDIA shares, indicating personal investment interest.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOWFdocXQzR1ZkeXlGTzBsZ3ZybUMwVEhveUlxX0RvekZxWDVYUjJiTnhwaVJ6U3hJZ2E2dUplQ0lndGJJXzVSdGFUWkZXa1RHY205T1JEMUNjcE1kVVhMVExUV3hFNndsMFFzSTJEam9EdUZfcm9DeVRlTEhRazhTSkExMEJObnlCR2gwM011WGxucTR0X3d3?oc=5>

### ‘Dean Of Valuation’ Says Nvidia Is 30% Below Fair Value, Waits For $140 — Calls Jensen Huang ‘Great CEO, But Human’
- Summary: Analyst deems Nvidia 30% undervalued, targeting $140, praising CEO but noting human limits.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNRTUwbU9xUUJFY3ZMYUtwdVRuLW1ad0NIR3ZpdHR6cFZiZzh0Rzludkt2X3FlTGZEcXhmd0V6a1pxZFljVUZOSmd1RG44VDJxbE1QeGljTmlVcXo4MHNFMHM2WmROelNoN19Hakg4U2Ewa3NfX2FiRkhGTmE1eG9SRkZ4V2VGVlJFODNGbjFzOGU3azB3S2hGYkhR?oc=5>

## RISKS

### Nvidia Stock Plunges 12% After Reuters Reports an SEC Probe of Its Accounting. It’s Nvidia’s Worst Day Since DeepSeek and It Has Lost $2.7 Trillion Since October
- Summary: SEC probe of Nvidia’s accounting triggers a 12% stock drop, marking the worst day since DeepSeek and a $2.7 trillion loss since October.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNek83Um5vdUVIV3dWb2FVZlZSemZJUmh3Zkt6cUxiYUgxVjJzS3k4Z3lRWEhFRzZ4THRWVTlvSzR6TFVPaDVLYVlIV2Q1alRwODNZNndjQnctNFNmcTJGamk1LWR2bl9oMktRWThaeURldFFJRnowaXE4Nzd1T2hUaFpDSVQ2dlZ1TEVVU3EzOXg1STRmWmRQbDZRNU8?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **13.48** | **11.35** | **12.19** | **103.20** | **3,031,172,907,008.00 USD** | **-30.34** |
| AMD | 90.68 | 10.18 | 61.88 | 44.70 | 702,393,286,656.00 USD | 105.99 |
| AVGO | 38.88 | 14.58 | 28.48 | 85.50 | 1,453,140,738,048.00 USD | -11.58 |
| INTC | N/A | 2.37 | 14.91 | 20.90 | 272,553,181,184.00 USD | 52.53 |

Peers fetched as_of: 2026-11-21; NVDA reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-17
- Next expected earnings: 2027-02-24 (yfinance; expected dates may change)

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
- Filing date: 2026-08-26
- Revenue (latest available single quarter): 96,221,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- Net income (latest available single quarter): 59,688,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi6wFBVV95cUxOWjNFQ3VvT3Foa1Z3aHRaUFFWZmMydmxQa1piMVpXaC1ycHBRMHFzWTRWeFlvUUVJSEUydzV4U29TZGhxMXAwQ3Z0elE1MWR6TXVTcHlDenljRlRJZ2c5aE1pTm1NYVk3TlNPUldEaXdLcmdsNlZWZjhmT19yWHE3akFWWF85MWM5a3RLZ3g0d05HNmwtVjc4bV8zY18tenVPb2VwdWVvZXI3TW1VTG15N3JjTFRnSERQN0xNVU1HdEJLaWw1MHpIMWhROFJfUWlBYWdfbTdueFdDLW5GY2JIYW1ETmRJMVNoTmZr?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNN19tUHBlVnVTVVNpdl84VUpCWUxxVGxNVTk0ZzlZeURoandQMVVnbHRQLUJjTi0ybEJFZndIdnBnSnhYd0Z4dlppZFZUWFoxclpEbUI0Zmk4aklsV3FEQ3lzNXJ6SjlWRlU4dXYyazBwWGVhVlBxMVpJaXU5M1loZ25UZlVOR3NzcFdYTk9Fb0Rzdmk0?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQQmI0cjQ4cUVpYjVTeXNuNFdNRmE4bHFJTDBsbDBNLS1LZGEzeFhsUVRvYzltRjA0YUU4RnYzS1htMkNHTDRDcHdfQXk4QjdRYloyQVRJWGtlLXhHNmJiMmVQMVhJNTduQXNZdld6ald5SmN0bUVHWUJpbmRBR2RIN2tVdEI2cG9hcXNMeExDd1JWNFBtS0JLQlkzWERheDhVSWZVZ3Z1RUNsc21zRjVQNWg4cw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQcGFEcVVtVlZRa1Ztb2lLeXpXcXJsdXF3VW80WnQ4bWQ5bW9aWFhGZXgySGV2enlZMlFCdHJXV1MwVW5QQUNlNEdKTDU4dXBsU2l0MTk3VkRwcU5mbmctRkt0NU5GS2tvSDRxTF9WUlYxNTR5TXN3ZVEzVjVQcmxJcFRoZlQ3Q2VrVnJqaUdGX3pqczYtTnc?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxOT2FGV192VllUQ19HUkJtU296SWE3UFFvNjRkS2NIWXpBNzRtaF9uMVVvZ2ZjVFBHVVY0UG1nZ0pBc1NjeURyOTBxNy1Rc3JJelRsY1BCbDBPNmtsSlQ2clRkcDJUQ2N4RFRSRXJHR1BlNmhZY3hZaDVLaU1hZVF4WFpCMmdDRVdSOFlheUlxNWVvbW9GTTk4RGkzc012cjAtNG02Y2IxWEJvekFNbFI0?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPWHNRcEVuR1ViVWpUY0p5RnIyekVpWDRTVUFLXzhLYnFDZ2tfeGctTGFkcENyRFliRXVRSktrc3hiTU01ZW9oY1dzaVJ2dzBNcTBxLWZienhFM0I0dVFDYXp3NTVjM3lZNGhxMXpuZUhuLXdUd1o0RTN2VVR0bzRDNnE0LXByUDJvWFl3VUFra1JDQXZmbV9FejNKdEI?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNZnBlVDFLTGxBQnRDYXJ5YTNuS1drVnhWVDh4N2o0aWlta1RyeXE1OGdmbVgzNU93OGcxWXNqR2k5X1VUOXN2SVdSc19FeExkcFNtU0hiZ0FOREhQVF9vdGp4Sm1PaURXWlBjdEJlU2s4LVFuWnJzS1A5ZjlNOEZsWTJvNGNWOTRJR2Z3T2sxQ25nV0VzTWhrQWFudFhrdw?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOSXJZbEJSVExtUGxySHJ5eFBaLTRFV0dTRWFjY244NWdhVTZ5cENMNXBqcVhBS08xLS1oSG5jbVJTME9QdWZKcXlzOXpTN3ZmMFZrREtNVzhHUVFMZXBmTndDUklLWFFrOGlpNTc5Y3dQR25mMjhXdGlSbl9SNVBfbFVOVXhCZTg3a3gtVUwyN1FWOVZ6NWIwRXUxZTdReG56V1MxeGdIONIBrAFBVV95cUxNN3pqQmZoNHdVc1M2SHpMWERNaDNHOUVyRGNDM3dlVzdGR19IaVdyRG5mQ0p6SzBZYlpWemdoZDN1M3NzZVpVVWpNVkFGa2ZpT3g0YVR1aFBLb0RoWm5mM0EwMkRkdmEtNndicG9iTHNLTGU4VUg4XzdPNWpDd0tYMWItNFM1NDNuMTN5OHEwbWFBNUloZEh6ekdsYW5WY2FXSHZjcmgxS3M5Tmx0?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxQYVo0b1dObGhWclp0S0JnV095MjVJVEx3QW1hQ3FIdk9VZ3NNZWt2cHp3YnVqbm9EVFJ1UXFlOG1YRmpNdV9CSEFTQ2Z1b0FfdGpaMFJjNVRxZEl5bDJzQ21oLTM1NnNkdHV2LXRvd3p5UjRnQktpanhIcHFPM3FONTlUZTZOU3lqME9rbEdXNVBlcER0WDZNSUxGOWkxaDhDRXI1YUFfcmFvWjliZDQ4UnhVeTNNVUpyN2Z6RUVMRkM4Q2lTdkJsYjBKajM?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxQS25iVW9uNHFsc3lYdkNPRTJyTUhYcWRVbjhOZlR4QUpLZGs4RkE0d1lSLTEtN2x6N0ZxZnlZdE9KaTQxeS1TbWRFaGFpd0hGc0ZKWmF5OEVRdnFDX1NNWFlBTl9rdVRUVFlxSVRIelpPNmluWVdUVElhQzh1NWtjemJaUnlhRnJ2N3Q2dDNVYlhVYWtXbkswbXhYLWdiOHE0V1dkQ2xjNjFsTlpEQ0hzRDBja0RqV0VFX0FZaXdKRVZ2RHdGVUUtS2VzanJrTkhiSVcxeGVCRXNlUUhSVWJ3?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNNnhJbmItN2ItMlRsSjJXMTNva0laLXROMVJIck1sczVBMUNtQmNOVlZFcVpaaVp1QS1ZWUtQNU5kLXItbTEtTXlXdzMzOXhMYXhCNnhOWWI1YWM5c05jSXo2cHhHb2lEU3h4V2JnSEY4bnpBOWltT2hGSHlvRUZLRWo5WlFGX0VMUTJDMEtTdW1qT21WanFrYUtvMG1mR0psdEdIYWp5Q1J3VFdhVnJtMw?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNMnc5TjJWdmVlZ255ZjJOaUpXa3FzWVJYdXVrQjRoRWVxTmtpRXptS21fX3h3a3ZXMXZIQjVNYnd6N25XSURjYzlKV3JOMkE0Yk9LanRZcGZLelgxSzc3YkVOZk9UYnJCSmxuVUVqSDNpNXBIdUdvODl2VmJKdUNRR0FyM0pVbFpGYmVLbm5IUWNkbkVIb0s5MFRRdmhKWWhoQ013?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOWFdocXQzR1ZkeXlGTzBsZ3ZybUMwVEhveUlxX0RvekZxWDVYUjJiTnhwaVJ6U3hJZ2E2dUplQ0lndGJJXzVSdGFUWkZXa1RHY205T1JEMUNjcE1kVVhMVExUV3hFNndsMFFzSTJEam9EdUZfcm9DeVRlTEhRazhTSkExMEJObnlCR2gwM011WGxucTR0X3d3?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNRTUwbU9xUUJFY3ZMYUtwdVRuLW1ad0NIR3ZpdHR6cFZiZzh0Rzludkt2X3FlTGZEcXhmd0V6a1pxZFljVUZOSmd1RG44VDJxbE1QeGljTmlVcXo4MHNFMHM2WmROelNoN19Hakg4U2Ewa3NfX2FiRkhGTmE1eG9SRkZ4V2VGVlJFODNGbjFzOGU3azB3S2hGYkhR?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNek83Um5vdUVIV3dWb2FVZlZSemZJUmh3Zkt6cUxiYUgxVjJzS3k4Z3lRWEhFRzZ4THRWVTlvSzR6TFVPaDVLYVlIV2Q1alRwODNZNndjQnctNFNmcTJGamk1LWR2bl9oMktRWThaeURldFFJRnowaXE4Nzd1T2hUaFpDSVQ2dlZ1TEVVU3EzOXg1STRmWmRQbDZRNU8?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
