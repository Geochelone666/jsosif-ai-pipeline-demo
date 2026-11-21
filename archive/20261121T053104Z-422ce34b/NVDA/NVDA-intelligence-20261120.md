# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-20**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-20**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-21T05:36:06.175763+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 7, 'ai': 11, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261120T053808Z-e360129e/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 13 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 34.78%; oldest publication 2026-11-18

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
| P/E (trailing) | 15.67 |
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
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.6717 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 15.0466 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.6302 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -39.3576 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -38.1885 -> Clearly below the moving-average trend level.

## TAILWINDS

### Nvidia Reports Faster Growth, Says Jensen Huang Won’t Return as CEO
- Summary: Nvidia reports accelerated growth; CEO Jensen Huang will not return, signaling leadership transition.
- Date: 2026-11-18 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxQOERUMkVEZEttRVd6TG92RVVFUzc4RU10anVtbFoxeV9RN1VneDJiUkc5NXpVWWNhM09PUWhGMHNHcmJNeTU0WTltdjA1TE5BbUtvOWx1QU4ySmJJc2lPWmoydVJld09sOER4Rk4xRE9QbXpKSVMzNE9ldENzQWZWVGZGRlY?oc=5>

### NVIDIA’s (NVDA) Strategic Investment in Ohio Data Center: Securing Future Growth
- Summary: NVIDIA invests in Ohio data center to support future growth.
- Date: 2026-11-20 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPU0NpSnV3UHBFdml4OFhuY3NpVGhIcE9IVGIya3ppZXpuWmN6VlU2Q003anRHcnM1Z042V2lNX1NmVEFfOHYyV3BrVU5UQTN3TjJuTFlzd1JzSWtOakhsSk14VUhwbWIxSUV4cmxiNDVQYnhZNzR5YzlJMXdqMDdDbjZxdGRjWThGem0tYVR2akhRcFBOamlranVkWGdWZmNpaU0w?oc=5>

## HEADWINDS

### NVDA Stock Alert: What to Know as Moody's Cuts Nvidia's Outlook Rating
- Summary: NVDA Stock Alert: What to Know as Moody's Cuts Nvidia's Outlook Rating
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQQmI0cjQ4cUVpYjVTeXNuNFdNRmE4bHFJTDBsbDBNLS1LZGEzeFhsUVRvYzltRjA0YUU4RnYzS1htMkNHTDRDcHdfQXk4QjdRYloyQVRJWGtlLXhHNmJiMmVQMVhJNTduQXNZdld6ald5SmN0bUVHWUJpbmRBR2RIN2tVdEI2cG9hcXNMeExDd1JWNFBtS0JLQlkzWERheDhVSWZVZ3Z1RUNsc21zRjVQNWg4cw?oc=5>

### NVDA Stock Clocks Worst Week In 18 Years As SEC Reportedly Probes Its Accounting Practices
- Summary: NVDA Stock Clocks Worst Week In 18 Years As SEC Reportedly Probes Its Accounting Practices
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxQMUFKc01RY3ZSdUJUajBidkpqQURTcnpOM0hQNWdieklURUlzX0RDTmoxUmNYTEJNQjFJcVZrODU3WDJ3S3BaZWhPMmtOODZBNkpqM1hhVS15T3FXMnVrS1l0amIwSTZCYWxwSnd1NVFHTmxyV2MzSjByX1U1Vk8ybjJwM3R1SGV0dnVTT2dhejBJWlhjS1NkSXVmVGMzbE1JVVp1VC1NT2NHQkpLZFBYOUhaWFNHSU45X1VRR0lUb3RSN2I2Mi03SlU5dXVvS29Ncm5PUzItNDlNOXI4OTZLN09OYlNDZw?oc=5>

### NVDA Stock Down 40% From October Peak Amid China Spying Crisis: California Begins Probe Into Chip Sales
- Summary: NVDA Stock Down 40% From October Peak Amid China Spying Crisis: California Begins Probe Into Chip Sales
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQcGFEcVVtVlZRa1Ztb2lLeXpXcXJsdXF3VW80WnQ4bWQ5bW9aWFhGZXgySGV2enlZMlFCdHJXV1MwVW5QQUNlNEdKTDU4dXBsU2l0MTk3VkRwcU5mbmctRkt0NU5GS2tvSDRxTF9WUlYxNTR5TXN3ZVEzVjVQcmxJcFRoZlQ3Q2VrVnJqaUdGX3pqczYtTnc?oc=5>

### Nvidia’s Stock Slide Deepens After Report of SEC Accounting Probe
- Summary: Nvidia’s Stock Slide Deepens After Report of SEC Accounting Probe
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMid0FVX3lxTE5INVNuU2E4Z3Bsa0FYa0RqbHNYM3ZlS1lZV3BlODA2Q2F2ejlxMllHQnl2YzhmMm5IeW5RdU9tUzhGUUdlVTJtMUozbkJYZGZOMFpnMmRaWWxpRDY0OVF3a1JiTVBrZmNWMkJsTVotRERzWUZvQVNV?oc=5>

### Nvidia Shares Sink to 52-Week Low After Report SEC Is Probing Accounting
- Summary: Nvidia Shares Sink to 52-Week Low After Report SEC Is Probing Accounting
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQbEx6c1BUSEpEMUF5OHd4d3prVHYwYnJxdzNWbTdvNl80QWVOaWZHX2F1UVFxTy1UQU9pMmhLdzVfTk9zSS1mWElBR0lWdDExWkNINEtNemJSZmQxcUhxWXlwN01RaHBBZGVmcHNnek1jSEZVQUVuaEx3VXFBS1VkV3hIcWpxRC1IcnNOLURVa1RsdVQxLUE?oc=5>

### Nvidia (NVDA) Stock Drops Despite Q3 Results Showing Huge AI Earnings
- Summary: Nvidia (NVDA) Stock Drops Despite Q3 Results Showing Huge AI Earnings
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPWHNRcEVuR1ViVWpUY0p5RnIyekVpWDRTVUFLXzhLYnFDZ2tfeGctTGFkcENyRFliRXVRSktrc3hiTU01ZW9oY1dzaVJ2dzBNcTBxLWZienhFM0I0dVFDYXp3NTVjM3lZNGhxMXpuZUhuLXdUd1o0RTN2VVR0bzRDNnE0LXByUDJvWFl3VUFra1JDQXZmbV9FejNKdEI?oc=5>

### Nvidia Stock Drops Below $150 Support After Jensen Huang Scandal: Key Levels to Watch
- Summary: Nvidia Stock Drops Below $150 Support After Jensen Huang Scandal: Key Levels to Watch
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQNldhalBiZklRZ3ExMXViMU1CTWExTFh5SHhRSEVaSWJ0UmVlQS1lQnNsRVIwTDNtVHFuYVFXcGpnbkJ4V0ZDNmg4Y2dMSzBFV1BMNEJRSkRwTVd1bFRIZTlnOFhDdFhsakh0dlpkNml5aVU4TVJzSXFQNjUzNmY1ZXRZQjlpNnEtQVE?oc=5>

### Why Is Nvidia (NVDA) Stock Falling After Record Earnings?
- Summary: Stock decline following record earnings.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTFBFOVFHRlJnRTd1eTF3aG9HVUJzLVpJZVJIand2T2dFMzk3QU5mRkhwNXU5aXdzYmREWFk1dEdvR0ZOS1pQYWNJTk5CWGM1akFQTjQxbV82U0pEQVRTZUEzbXNFUkpObTJvU2NQb28zeVBPRFZLeDg5NW1JOTVfdw?oc=5>

### Nvidia stock extends $2.7 trillion rout as SEC probe reportedly investigates its accounting
- Summary: SEC probe into Nvidia’s accounting amid a $2.7 trillion market rout.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxQS25iVW9uNHFsc3lYdkNPRTJyTUhYcWRVbjhOZlR4QUpLZGs4RkE0d1lSLTEtN2x6N0ZxZnlZdE9KaTQxeS1TbWRFaGFpd0hGc0ZKWmF5OEVRdnFDX1NNWFlBTl9rdVRUVFlxSVRIelpPNmluWVdUVElhQzh1NWtjemJaUnlhRnJ2N3Q2dDNVYlhVYWtXbkswbXhYLWdiOHE0V1dkQ2xjNjFsTlpEQ0hzRDBja0RqV0VFX0FZaXdKRVZ2RHdGVUUtS2VzanJrTkhiSVcxeGVCRXNlUUhSVWJ3?oc=5>

### The post earnings slide in Nvidia stock is getting uglier by the day
- Summary: Nvidia’s post‑earnings performance deteriorates, worsening investor sentiment.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxQYVo0b1dObGhWclp0S0JnV095MjVJVEx3QW1hQ3FIdk9VZ3NNZWt2cHp3YnVqbm9EVFJ1UXFlOG1YRmpNdV9CSEFTQ2Z1b0FfdGpaMFJjNVRxZEl5bDJzQ21oLTM1NnNkdHV2LXRvd3p5UjRnQktpanhIcHFPM3FONTlUZTZOU3lqME9rbEdXNVBlcER0WDZNSUxGOWkxaDhDRXI1YUFfcmFvWjliZDQ4UnhVeTNNVUpyN2Z6RUVMRkM4Q2lTdkJsYjBKajM?oc=5>

### Nvidia stock plunges 14%, wraps up longest weekly losing streak since 2008 financial crisis
- Summary: Nvidia shares fall 14%, ending a historic weekly losing streak.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOSXJZbEJSVExtUGxySHJ5eFBaLTRFV0dTRWFjY244NWdhVTZ5cENMNXBqcVhBS08xLS1oSG5jbVJTME9QdWZKcXlzOXpTN3ZmMFZrREtNVzhHUVFMZXBmTndDUklLWFFrOGlpNTc5Y3dQR25mMjhXdGlSbl9SNVBfbFVOVXhCZTg3a3gtVUwyN1FWOVZ6NWIwRXUxZTdReG56V1MxeGdIONIBrAFBVV95cUxNN3pqQmZoNHdVc1M2SHpMWERNaDNHOUVyRGNDM3dlVzdGR19IaVdyRG5mQ0p6SzBZYlpWemdoZDN1M3NzZVpVVWpNVkFGa2ZpT3g0YVR1aFBLb0RoWm5mM0EwMkRkdmEtNndicG9iTHNLTGU4VUg4XzdPNWpDd0tYMWItNFM1NDNuMTN5OHEwbWFBNUloZEh6ekdsYW5WY2FXSHZjcmgxS3M5Tmx0?oc=5>

### EXCLUSIVE: Nvidia's accounting is a focus of US SEC investigation, sources say
- Summary: SEC probes Nvidia's accounting practices.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPMzlPdFVTT2cyVkhmMFVKNWZ1MnpNT0NLcURnblg4THMwUWNuYTRBLWUxU0ZSSUR5bk1zNnBmVlhIUjByNkN6TzVBNC1uaXQxM0dwY2FkMzZQdm00a0xyMXo3NFNpSUNPdERZWU82aGZLa0lNZHpMOXVnVDBVQW9lMmNrWEVRczVYS1Racm1NNlNERDBJeTFJRG1pZVRfTC1LTy1pNjhpVzRaeGRrY25kSzQ1aDNUUQ?oc=5>

### Closing Bell panel assesses sharp selloff as Nvidia, AI stocks tumble
- Summary: Market selloff hits Nvidia and AI stocks.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQQ1g0UXZ5OXJuVHpnN1lqWUk1OURVWVRkdDZRemFXcS1hNk1GdTNQcHE1dDdyb0NxbDc4R0hTTDlFMG1IdnJWbThPSGNqTzVVWXJxR09Lamh6WGZaSWZvVm12X05zdGpaek1zZVRWcWhEYk1sM0lEblZjNURGOTVWdXVmaXdnMW5RWkdZY1dwTV9hdTcwTGVWWlY4UmNocWhGaUk5UHE0SWJxUTFiZUtSNQ?oc=5>

### Nvidia Stock Plunge Wipes Out Nearly $500 Billion in One Day as SEC Reportedly Probes Its Accounting
- Summary: SEC probe triggers massive Nvidia stock plunge.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxOZXVvWWpMRlREaWkzWTdnWGVvMzZsX2JVekNROC1CNXkwMDJyN3J2R2djNmdnTHZVN0xzVXFjdFdEM0laV1kzWFo2MlQ2ajVfYU9TZ0xTZHFpYXhHdllpX3ZNWUh1bk55N1BwSjRsa1FKUmloTU5RelRHM1VVOGRLZUF0RFVKejdPakJmQVh0RGhjcTk4TGs3czY4RkVPLWZKOUZ1bnk0REFQOXZja3RrSnYybWd0b2ZTTEVkdjBCZDZhRkwtTkFWdFNKc0FDVGcydHBlTVFTU0xRbXdLLUE?oc=5>

## CATALYSTS

### Nvidia Is Financing Its Own Demand, And The Fed Noticed (NASDAQ:NVDA)
- Summary: NVDA’s self-financing of demand attracts Fed attention, indicating significant liquidity use and market impact.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPSWY1d2ItZkhENElDOVhFeHBYYXpQcU0zdjZTbG4yV0Z2RHM1eGF5ZG5FTFo4YklUTUItMnNJZVd4b1gzMGZoeE9PRzhnZ3pwREQxYVBMVDNFRVo4bWNhcktfZUlBZkRacldEQUZRSG84eEJGM3Y0YWc0eEU2VUV3MVREMHJBWE1UaUk2d0tpaEY0SDFxZXN5bkZTVQ?oc=5>

### Trump Bought Up to $265,000 of NVIDIA Stock. Here’s Where the Price Target Stands
- Summary: Former President Trump purchased $265,000 worth of NVIDIA shares, indicating personal investment interest.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOWFdocXQzR1ZkeXlGTzBsZ3ZybUMwVEhveUlxX0RvekZxWDVYUjJiTnhwaVJ6U3hJZ2E2dUplQ0lndGJJXzVSdGFUWkZXa1RHY205T1JEMUNjcE1kVVhMVExUV3hFNndsMFFzSTJEam9EdUZfcm9DeVRlTEhRazhTSkExMEJObnlCR2gwM011WGxucTR0X3d3?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **15.67** | **11.35** | **12.19** | **103.20** | **3,031,172,907,008.00 USD** | **-30.34** |
| AMD | 90.68 | 10.18 | 61.88 | 44.70 | 702,393,286,656.00 USD | 105.99 |
| AVGO | 38.88 | 14.58 | 28.48 | 85.50 | 1,453,140,738,048.00 USD | -11.58 |
| INTC | N/A | 2.37 | 14.91 | 20.90 | 272,553,181,184.00 USD | 52.53 |

Peers fetched as_of: 2026-11-20; NVDA reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-17
- Next expected earnings: 2027-02-24 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-20

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

- https://news.google.com/rss/articles/CBMihAFBVV95cUxQOERUMkVEZEttRVd6TG92RVVFUzc4RU10anVtbFoxeV9RN1VneDJiUkc5NXpVWWNhM09PUWhGMHNHcmJNeTU0WTltdjA1TE5BbUtvOWx1QU4ySmJJc2lPWmoydVJld09sOER4Rk4xRE9QbXpKSVMzNE9ldENzQWZWVGZGRlY?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPU0NpSnV3UHBFdml4OFhuY3NpVGhIcE9IVGIya3ppZXpuWmN6VlU2Q003anRHcnM1Z042V2lNX1NmVEFfOHYyV3BrVU5UQTN3TjJuTFlzd1JzSWtOakhsSk14VUhwbWIxSUV4cmxiNDVQYnhZNzR5YzlJMXdqMDdDbjZxdGRjWThGem0tYVR2akhRcFBOamlranVkWGdWZmNpaU0w?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQQmI0cjQ4cUVpYjVTeXNuNFdNRmE4bHFJTDBsbDBNLS1LZGEzeFhsUVRvYzltRjA0YUU4RnYzS1htMkNHTDRDcHdfQXk4QjdRYloyQVRJWGtlLXhHNmJiMmVQMVhJNTduQXNZdld6ald5SmN0bUVHWUJpbmRBR2RIN2tVdEI2cG9hcXNMeExDd1JWNFBtS0JLQlkzWERheDhVSWZVZ3Z1RUNsc21zRjVQNWg4cw?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxQMUFKc01RY3ZSdUJUajBidkpqQURTcnpOM0hQNWdieklURUlzX0RDTmoxUmNYTEJNQjFJcVZrODU3WDJ3S3BaZWhPMmtOODZBNkpqM1hhVS15T3FXMnVrS1l0amIwSTZCYWxwSnd1NVFHTmxyV2MzSjByX1U1Vk8ybjJwM3R1SGV0dnVTT2dhejBJWlhjS1NkSXVmVGMzbE1JVVp1VC1NT2NHQkpLZFBYOUhaWFNHSU45X1VRR0lUb3RSN2I2Mi03SlU5dXVvS29Ncm5PUzItNDlNOXI4OTZLN09OYlNDZw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQcGFEcVVtVlZRa1Ztb2lLeXpXcXJsdXF3VW80WnQ4bWQ5bW9aWFhGZXgySGV2enlZMlFCdHJXV1MwVW5QQUNlNEdKTDU4dXBsU2l0MTk3VkRwcU5mbmctRkt0NU5GS2tvSDRxTF9WUlYxNTR5TXN3ZVEzVjVQcmxJcFRoZlQ3Q2VrVnJqaUdGX3pqczYtTnc?oc=5
- https://news.google.com/rss/articles/CBMid0FVX3lxTE5INVNuU2E4Z3Bsa0FYa0RqbHNYM3ZlS1lZV3BlODA2Q2F2ejlxMllHQnl2YzhmMm5IeW5RdU9tUzhGUUdlVTJtMUozbkJYZGZOMFpnMmRaWWxpRDY0OVF3a1JiTVBrZmNWMkJsTVotRERzWUZvQVNV?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQbEx6c1BUSEpEMUF5OHd4d3prVHYwYnJxdzNWbTdvNl80QWVOaWZHX2F1UVFxTy1UQU9pMmhLdzVfTk9zSS1mWElBR0lWdDExWkNINEtNemJSZmQxcUhxWXlwN01RaHBBZGVmcHNnek1jSEZVQUVuaEx3VXFBS1VkV3hIcWpxRC1IcnNOLURVa1RsdVQxLUE?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPWHNRcEVuR1ViVWpUY0p5RnIyekVpWDRTVUFLXzhLYnFDZ2tfeGctTGFkcENyRFliRXVRSktrc3hiTU01ZW9oY1dzaVJ2dzBNcTBxLWZienhFM0I0dVFDYXp3NTVjM3lZNGhxMXpuZUhuLXdUd1o0RTN2VVR0bzRDNnE0LXByUDJvWFl3VUFra1JDQXZmbV9FejNKdEI?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQNldhalBiZklRZ3ExMXViMU1CTWExTFh5SHhRSEVaSWJ0UmVlQS1lQnNsRVIwTDNtVHFuYVFXcGpnbkJ4V0ZDNmg4Y2dMSzBFV1BMNEJRSkRwTVd1bFRIZTlnOFhDdFhsakh0dlpkNml5aVU4TVJzSXFQNjUzNmY1ZXRZQjlpNnEtQVE?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTFBFOVFHRlJnRTd1eTF3aG9HVUJzLVpJZVJIand2T2dFMzk3QU5mRkhwNXU5aXdzYmREWFk1dEdvR0ZOS1pQYWNJTk5CWGM1akFQTjQxbV82U0pEQVRTZUEzbXNFUkpObTJvU2NQb28zeVBPRFZLeDg5NW1JOTVfdw?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxQS25iVW9uNHFsc3lYdkNPRTJyTUhYcWRVbjhOZlR4QUpLZGs4RkE0d1lSLTEtN2x6N0ZxZnlZdE9KaTQxeS1TbWRFaGFpd0hGc0ZKWmF5OEVRdnFDX1NNWFlBTl9rdVRUVFlxSVRIelpPNmluWVdUVElhQzh1NWtjemJaUnlhRnJ2N3Q2dDNVYlhVYWtXbkswbXhYLWdiOHE0V1dkQ2xjNjFsTlpEQ0hzRDBja0RqV0VFX0FZaXdKRVZ2RHdGVUUtS2VzanJrTkhiSVcxeGVCRXNlUUhSVWJ3?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxQYVo0b1dObGhWclp0S0JnV095MjVJVEx3QW1hQ3FIdk9VZ3NNZWt2cHp3YnVqbm9EVFJ1UXFlOG1YRmpNdV9CSEFTQ2Z1b0FfdGpaMFJjNVRxZEl5bDJzQ21oLTM1NnNkdHV2LXRvd3p5UjRnQktpanhIcHFPM3FONTlUZTZOU3lqME9rbEdXNVBlcER0WDZNSUxGOWkxaDhDRXI1YUFfcmFvWjliZDQ4UnhVeTNNVUpyN2Z6RUVMRkM4Q2lTdkJsYjBKajM?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOSXJZbEJSVExtUGxySHJ5eFBaLTRFV0dTRWFjY244NWdhVTZ5cENMNXBqcVhBS08xLS1oSG5jbVJTME9QdWZKcXlzOXpTN3ZmMFZrREtNVzhHUVFMZXBmTndDUklLWFFrOGlpNTc5Y3dQR25mMjhXdGlSbl9SNVBfbFVOVXhCZTg3a3gtVUwyN1FWOVZ6NWIwRXUxZTdReG56V1MxeGdIONIBrAFBVV95cUxNN3pqQmZoNHdVc1M2SHpMWERNaDNHOUVyRGNDM3dlVzdGR19IaVdyRG5mQ0p6SzBZYlpWemdoZDN1M3NzZVpVVWpNVkFGa2ZpT3g0YVR1aFBLb0RoWm5mM0EwMkRkdmEtNndicG9iTHNLTGU4VUg4XzdPNWpDd0tYMWItNFM1NDNuMTN5OHEwbWFBNUloZEh6ekdsYW5WY2FXSHZjcmgxS3M5Tmx0?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPMzlPdFVTT2cyVkhmMFVKNWZ1MnpNT0NLcURnblg4THMwUWNuYTRBLWUxU0ZSSUR5bk1zNnBmVlhIUjByNkN6TzVBNC1uaXQxM0dwY2FkMzZQdm00a0xyMXo3NFNpSUNPdERZWU82aGZLa0lNZHpMOXVnVDBVQW9lMmNrWEVRczVYS1Racm1NNlNERDBJeTFJRG1pZVRfTC1LTy1pNjhpVzRaeGRrY25kSzQ1aDNUUQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQQ1g0UXZ5OXJuVHpnN1lqWUk1OURVWVRkdDZRemFXcS1hNk1GdTNQcHE1dDdyb0NxbDc4R0hTTDlFMG1IdnJWbThPSGNqTzVVWXJxR09Lamh6WGZaSWZvVm12X05zdGpaek1zZVRWcWhEYk1sM0lEblZjNURGOTVWdXVmaXdnMW5RWkdZY1dwTV9hdTcwTGVWWlY4UmNocWhGaUk5UHE0SWJxUTFiZUtSNQ?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxOZXVvWWpMRlREaWkzWTdnWGVvMzZsX2JVekNROC1CNXkwMDJyN3J2R2djNmdnTHZVN0xzVXFjdFdEM0laV1kzWFo2MlQ2ajVfYU9TZ0xTZHFpYXhHdllpX3ZNWUh1bk55N1BwSjRsa1FKUmloTU5RelRHM1VVOGRLZUF0RFVKejdPakJmQVh0RGhjcTk4TGs3czY4RkVPLWZKOUZ1bnk0REFQOXZja3RrSnYybWd0b2ZTTEVkdjBCZDZhRkwtTkFWdFNKc0FDVGcydHBlTVFTU0xRbXdLLUE?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPVWFQUldJZnVhd3djV1YwODFlN1FHamxJNVZENFJfRUZ1X29GRUdFTnZNRkVRTFF4T0R5azFKVVpBSEloRko5clVoeEQtSlBiTkt1OHJOVEJNWjZJZXozR1d1UGg1MUFNeHMtU21kSWZxYzdEdm80VEhfaVEwMjdXMFY1Mk85d0xUNUFfZ1dRWTY5aG5Zb3NjaUlVaXZsQQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPSWY1d2ItZkhENElDOVhFeHBYYXpQcU0zdjZTbG4yV0Z2RHM1eGF5ZG5FTFo4YklUTUItMnNJZVd4b1gzMGZoeE9PRzhnZ3pwREQxYVBMVDNFRVo4bWNhcktfZUlBZkRacldEQUZRSG84eEJGM3Y0YWc0eEU2VUV3MVREMHJBWE1UaUk2d0tpaEY0SDFxZXN5bkZTVQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOWFdocXQzR1ZkeXlGTzBsZ3ZybUMwVEhveUlxX0RvekZxWDVYUjJiTnhwaVJ6U3hJZ2E2dUplQ0lndGJJXzVSdGFUWkZXa1RHY205T1JEMUNjcE1kVVhMVExUV3hFNndsMFFzSTJEam9EdUZfcm9DeVRlTEhRazhTSkExMEJObnlCR2gwM011WGxucTR0X3d3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
