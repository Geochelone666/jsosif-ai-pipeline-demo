# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T06:03:34.536670+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 1, 'ai': 14, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261119T054856Z-9eb86811/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 12 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 47.83%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 572.0400 |
| Return 1D (%) | -0.4490 |
| Return 1W (%) | -3.0161 |
| Return 1M (%) | 7.4798 |
| Return YTD (%) | 13.8048 |
| Return 1Y (%) | 14.1204 |
| Annualized volatility (%) | 15.1405 |
| Beta vs SPY | 0.0854 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 0.9516 |
| Downside deviation (rf=0, %) | 10.2361 |
| Sortino (rf=0) | 1.4075 |
| Historical VaR 95% (1D, %) | 1.4206 |
| Historical ES 95% (1D, %) | 2.0519 |
| Correlation vs SPY | 0.0784 |
| Tracking error vs SPY (%) | 19.7339 |
| P/E (trailing) | 16.01 |
| P/B | 0.00 |
| EV/EBITDA | -2.04 |
| Revenue growth (%) | 11.20 |
| Forward P/E (estimate) | 25.07 |
| Gross margin (%) | 26.60 |
| Operating margin (%) | 26.60 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | 4.32 |
| MA50 | 535.6716 |
| Close vs MA50 (%) | 6.7893 |
| MA200 | 502.2384 |
| Close vs MA200 (%) | 13.8981 |
| RSI (14, Wilder) | 58.4082 |
| MACD (12,26) | 14.3916 |
| MACD signal (9) | 15.6909 |
| MACD histogram | -1.2993 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 572.0400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.4490 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.0161 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.4798 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 13.8048 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 14.1204 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 15.1405 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.2361 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4075 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4206 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0519 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0784 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.7339 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0854 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9516 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.0712 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.3178 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.0101 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 58.4082 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.2993 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.7893 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 13.8981 -> Clearly above the moving-average trend level.

## TAILWINDS

### Warren Buffett Says Berkshire Will Never Prefer Cash Over Good Businesses. History Says Your Portfolio Shouldn't Either.
- Summary: Buffett emphasizes investing in quality businesses over cash holdings, reinforcing a long-term growth strategy.
- Date: 2026-11-19 | Impact: low | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOandVMkcyYUwwQWtUZVNvQWM3WFV3TnhOVlFqZ1ZjWF9nYlNuS1lyUDNFYjlic3B0SmdFX2U4T1oyTXdGdnV5cm5xVk45ckxDQkJmNWw3OEtKenNVVXBkUjNId29mUFplbXRLRF9nVDMtb0NvNWtORmNxUzJ4a3l4VTZBYUkta0g1VlpYc2RQNXVVbDNaQ3QtYkV4T1RFdklFVFE?oc=5>

### Berkshire Hathaway Is Up 18% in Its First Year Without Buffett as CEO. Can BRK.B Stock Hit $700 by 2027?
- Summary: Berkshire’s stock rose 18% in its first year post-Buffett, suggesting strong momentum toward a $700 target by 2027.
- Date: 2026-11-17 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPM1dENGVxMWdITEZQTWNILUFtSGRGaUVmWF9tOEhzRXVncFJvLTAtSzFFdGlGVjNobUxzSTZhZUYyYVl0VFJTOTFNa1VjdnpJeHRRX2dUamk3QzN5VXZzaE5kQmM5MmY4dWdia3NPZG93TDY2WWE2MDBzOHY5bXdfc0ZvNHV0dE5uSUY3SU5Md0k2RzlzUHpMTXdXZk5HX05OSHc?oc=5>

## HEADWINDS

### Berkshire almost doubles stake in tumbling housing stock
- Summary: Berkshire almost doubles stake in tumbling housing stock
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOMERPMWdJQlAwVjFiTXVsd294dVUxeTQzdXh1WjhIX0hnMjJxNFJyN0hJaTBNLUVPMkd3MHZJVFpuejFIMnNodmM3azd5d0tNb0hOR3E0ZnJQYUFfR05jSmUyN1hkbzlsak0wRkh3UHpVQ2VGYjNKQlFCNUVsbEswc29relZlVm40d1o1ekVwMUI5Z1hDZG42eElWN2I1MFNaNGNqVUpoUXM4RUU?oc=5>

## CATALYSTS

### Berkshire Hathaway 13F: Sales Outweighed Purchases; Swapping Bank of America Stock for Lennar
- Summary: Portfolio shift: selling BofA, buying Lennar, net sales exceed purchases.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQdmdiajF3SkI1V2Z0enpmcllyeGwxaE9iUTJMRXI3dEF1czZlekxONWppN1I1MkV6dUNmWVB6TVMtSVdYbThjTDNVZVUtZV9rYmE3bm00cEJ3VzBLa0Frbm1CZjJYSEtyUFB4dnl1NDBkTzBKZjdLNDZScVBaQjAxRHFZd05PUFJTRldnVWJJZWVOaUR3STlTaHVuZWltYUx2NVhWV2pNZ1lqQVZYdVhtWXVRZTd2dWJGMzd3?oc=5>

### Berkshire Hathaway Slashes This Top 5 Stock; Nvidia Boosts SpaceX
- Summary: Berkshire sells a top 5 holding, indicating portfolio rebalancing.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQWmtSdzA4SVl6UlZEclpaQVd2b2NSaXRLQWZDTzVIQ3dRYnU2elJoVEtmbFhWb0tMbVZiSVVnMHVSWHdRS3V2VW5uYmY3cnFWU1FHbmo1aF85QzFVY0VCVnRRcXZLSHFGNGlfWExtRlJpRU5idDgxMGlKWWlQdVhwZmkyZFVtVnNsTHc2SzVoXzR1R2xLXzVfMFJ1RnJCU2RJZDJj?oc=5>

### Berkshire Executives Buy $2 Million in Stock With Shares Near a Record
- Summary: Berkshire Hathaway executives purchased $2 million of the company's stock as share prices approached a record high.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxObTQzbWFHcU5FR0Y5YmVZYnR3d2otWjNGRHVPYm9DbVdQM1dHTlpOcEFJOGJLT2NkX2J6cm44WUJkQzl1YnBXYTFHRHBNcVZWWUNyT2lxZHowT25tRkd2Tml2dnRReWdIZVB5WTNUVlZNVVZFQ0M1SzJnWjQ5VjFSU3BCRWktSHZZ?oc=5>

### Here's What Berkshire Hathaway Bought and Sold in Q3
- Summary: Summary of Berkshire's Q3 acquisitions and divestitures.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNODdJLV9XbG85V0RTTi1lT2lZTm1KaWFVa2h6MnhXT21UWUlVenZWZFFnVW51Nk9LYWx4V2VPeW1TYlBzbUF6OGpTbWxSNGYtMVBGQklwMFUtenA0VFBRendROW9GRXNudnJGUlhubUhOZ2tPVDBTZ1dDeHFDOXg0ZXNaazlnajNGbnpwY3AzLWF0dw?oc=5>

### Berkshire Hathaway (BRK.B) Reduced Its Stake in Bank of America During the Third Quarter
- Summary: Berkshire cuts Bank of America stake in Q3.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNMUpQNVBxajZZcHBrc1gxZWwwQ3VTZmMxV3lVam5TUU1YSFNYLW9ENTIyNUtoNGRWcVdXcGg5VEFZWFFWQ0RhNzBHbUZLNFRZNFRSMjVfSUN2eHFiOXNKV3A4ZHdOYTB5ck5TUTU4VWM0V3dFV1huQTAzd0xDREx0bEFqMjBuUGNlUEs3amJvbjJhd3ViczlxOUxTWUtzdTQ4RkF1YURLYWVTckJ1MmlJVmMyYXBOblk?oc=5>

### Berkshire Hathaway (BRK.B) Reveals New Stake And Nearly Doubles One Holding
- Summary: Berkshire doubles a holding, adding a significant stake to its holdings.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPdVhDY2h0djVhZ3dwUXNPSHg3TFFhT1NFUnVvNWpHanZ5M1kzS3JrSENsdlQzNmhHZUJJUjdNc2NXam1LSTdjV0VEZXNneS1Vc2RrZTR2Q1dvREUwUHUxUmJheDJjY1lQTV9zOFlfQ0Z1ZXJiTDJueGdXRnRobzNWQ3pVRmpWcW9tYnY4d0dwZjhuU1dGYUpFQ0VBbDVWQQ?oc=5>

### Warren Buffett Gives $5.4 Billion in Berkshire Shares to 4 Family Foundations— See Which One Gets the Mos
- Summary: Buffett transferred $5.4B of Berkshire shares to family foundations, a significant ownership shift.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAJBVV95cUxObHNrZldQUkx2YVRTWlA4WjFDS3VRR016Qm9VcmN3R2I4VkVfWi1pR0tCNEN4ajRxeEJLNm5OcUIzcG04cUozdU9BS3djOWM3dmwzVnhBQW9icmx6SjJjc21JZVZBQ3FpUTd2VTVjQm5iSFdTS1FVUHB5TFlMX3hoN1c1NUNySVE3N0VPTGVPSTZLQjhzTXl6aFJac003THN0bW5BemdKcnlWbVRiWEFDUFRSSGVjS2VtbHJRemtSbVVNVzI2ZmdVUDdqeW5zY3dzdkV1bXU4NWJkN1h6NWRzVE1jMU5wTU51V215cmtMUndreDBOc3NaTnRfeGxtcG0wZUhtQ2NnSk0zdjVvTHBhdmxVd0ozZlBac0VQdUpPMWI?oc=5>

### Warren Buffett Just Gave Away $5.5 Billion of Berkshire Stock. He Says His Confidence in Berkshire Is "As Strong as Ever."
- Summary: Buffett distributes $5.5B of Berkshire shares, signaling strong confidence.
- Date: 2026-11-18 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPZWE3aFRHaTlWWkdRRUxteUdMX1pOSVRBc1NlNmZTMFZlMEdMeHVQRDdSY1JfNlZHMVRZaHJNdkthM3ByYm1udHVFMVROVHhuVk82eGJtcFVXS3pDOTdrQmRfa0dEQ0lTUlNGcW1GenlDQ2QyWGt5dGVuaFNMRmNIQzBaMkt4c1JoenBsQlhEeTBXMmxNR3l0cFlR?oc=5>

### Forget Apple. Warren Buffett’s Berkshire Is Pouring Nearly $1 Billion Into This Little-Known Tech Stock.
- Summary: Berkshire invests ~$1B in a small tech company, signaling confidence in its growth potential.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxONmpGNnEtZDhjWF9xZnZSMVF6Y1hUeWdSM09IQ0dla0JWand2Z1lSMzR5REVqZmRyZC1ubVlaeUxMZmtwRVF6dGtuQ3dtVHRoMWs2QTJfX1UzWExPWlFXMWdJOFZPNUpQNVd1MURvODVMSEw5MkMyVWxWdVJRX1Q0TGtNOEZYWGN5bmtKMXpibGRNcTU5LS1qcUVSX29NWFdzaF9aTQ?oc=5>

### Warren Buffett Expects Berkshire Hathaway (BRKA, BRKB) Stock to Drop About 50% Again Someday. Here's What He Says to Do Then.
- Summary: Buffett predicts a future 50% drop in Berkshire stock and outlines potential actions.
- Date: 2026-11-19 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQV1FWcTNHWTNfd3pnSmZ2MUJYWXpaWm0taXI3TFE5bmRyV041UjVRSUFiYmF6SENLYVV3ZWZiM2pZZ3FISlNUeS13MDhSaWdOVW10M09XVWVJVDllSkFaby1YYm9hZElMM1huZlU1OEJINmc4Z29QZC12Ri1hUThsWmc3TmdueXNoN3dYWlc0TTRHcDMyX1FjVVA1a21jelVzVmJmZU9LTTZwUQ?oc=5>

### Berkshire reveals new $689 million stake in major tech stock
- Summary: Berkshire announced a $689M stake in a major tech company, expanding its portfolio.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQcHNSX3ZyWGhORWM3UjJpeG9sblZJR3dFVXRCYzhRLXZlMnd3M2RyVGVDdW0xLVdBb0lXTmt0RG1ZMUVQS1NNb1VVWXZjTWtRcWdwdWxsSXRtdG1sTHN3MGJuYkJ5V3laY0F4Z2xjeHRLeHBJSmdnekw5cUc5OUk5bFdRUlFHU2RNdTlydHA0ZThyTUJiSGpVOWFvaG1pRFh1NGc?oc=5>

### Warren Buffett's Berkshire Just Revealed a New Stock and Sold More Bank of America. Here's What a 68-Year-Old With 400 Shares Owns
- Summary: Berkshire disclosed a new stock purchase and a sale of Bank of America shares.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigAJBVV95cUxOeWtpeEZnSHpka2xZUlc5dEFJaG9Md3A5SXk5MXpVckhEb3dmWXZyODJxT1FScC1OZmF5dEgtNTB5ZFpRTjBFV0Vhbl8yU2w4VkNrOWI1MmlkZHRWZ0RTYmtUOTI0dnRjSGFjQUh0UG8xS2lyZ1NjMFdqb2hXWm80TlJTRGxtYXVfYUYwUnU1ZGhKc2xEZjFKWUlMY0Y4QllIUkpIRVZfeS00VWM1S3lPcXBWQThIbWh5SlVuamF0TTA3REVBdTR2Mkl2TzdJdVY2WjU2YndwalJlY3JjM2ZfY3FUWV92bXpWUDBXUTlmb1dzOFR4SElEVGg0YnZsT0ZQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **16.01** | **0.00** | **-2.04** | **11.20** | **1,215,309,938,688.00 USD** | **14.12** |
| MKL | 13.97 | 1.29 | 7.98 | -11.20 | 23,867,441,152.00 USD | -4.37 |
| FFH.TO | 9.77 | 1.41 | 8.67 | 1.90 | 55,557,185,536.00 CAD | 14.74 |
| L | 15.17 | 1.22 | 8.61 | 1.90 | 22,184,108,032.00 USD | 4.42 |

Peers fetched as_of: 2026-11-19; BRK-B reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-07
- Next expected earnings: 2027-03-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-09
- Revenue (latest available single quarter): 105,647,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 22,112,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1067983/000119312526452412/brka-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiogFBVV95cUxOandVMkcyYUwwQWtUZVNvQWM3WFV3TnhOVlFqZ1ZjWF9nYlNuS1lyUDNFYjlic3B0SmdFX2U4T1oyTXdGdnV5cm5xVk45ckxDQkJmNWw3OEtKenNVVXBkUjNId29mUFplbXRLRF9nVDMtb0NvNWtORmNxUzJ4a3l4VTZBYUkta0g1VlpYc2RQNXVVbDNaQ3QtYkV4T1RFdklFVFE?oc=5
- https://news.google.com/rss/articles/CBMi8gFBVV95cUxPT0JWNldCZlB1TDdUNnpNU2ktNHdfZ3hZWkRDRkpENXdzaDUzUkc0bm9JRkFlSnVMbDdqbi1acWloY0JFM0Y0NDJoVFpBWmFsVEViUG9VZFhzLWI5VVpqMFQzQjJsSElhMTJfSHBsSlFNcmhneGVGWnVYYWJ5SUVORUFXbU9WMF8zdjFoYUxZLVlaZDVuWjFPU0hSN2xvVlJjT045VVZPbDhXeUJELXMxZkJqUldvSUxJcEJ5VVNVc216Q0wxRnJkNkNCa3ppVjBaWDd0TlBRakc3QnRWbHVPbjg2ZXdGZGQ3S1FDR3hMQjdHUQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPM1dENGVxMWdITEZQTWNILUFtSGRGaUVmWF9tOEhzRXVncFJvLTAtSzFFdGlGVjNobUxzSTZhZUYyYVl0VFJTOTFNa1VjdnpJeHRRX2dUamk3QzN5VXZzaE5kQmM5MmY4dWdia3NPZG93TDY2WWE2MDBzOHY5bXdfc0ZvNHV0dE5uSUY3SU5Md0k2RzlzUHpMTXdXZk5HX05OSHc?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOMERPMWdJQlAwVjFiTXVsd294dVUxeTQzdXh1WjhIX0hnMjJxNFJyN0hJaTBNLUVPMkd3MHZJVFpuejFIMnNodmM3azd5d0tNb0hOR3E0ZnJQYUFfR05jSmUyN1hkbzlsak0wRkh3UHpVQ2VGYjNKQlFCNUVsbEswc29relZlVm40d1o1ekVwMUI5Z1hDZG42eElWN2I1MFNaNGNqVUpoUXM4RUU?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQdmdiajF3SkI1V2Z0enpmcllyeGwxaE9iUTJMRXI3dEF1czZlekxONWppN1I1MkV6dUNmWVB6TVMtSVdYbThjTDNVZVUtZV9rYmE3bm00cEJ3VzBLa0Frbm1CZjJYSEtyUFB4dnl1NDBkTzBKZjdLNDZScVBaQjAxRHFZd05PUFJTRldnVWJJZWVOaUR3STlTaHVuZWltYUx2NVhWV2pNZ1lqQVZYdVhtWXVRZTd2dWJGMzd3?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQWmtSdzA4SVl6UlZEclpaQVd2b2NSaXRLQWZDTzVIQ3dRYnU2elJoVEtmbFhWb0tMbVZiSVVnMHVSWHdRS3V2VW5uYmY3cnFWU1FHbmo1aF85QzFVY0VCVnRRcXZLSHFGNGlfWExtRlJpRU5idDgxMGlKWWlQdVhwZmkyZFVtVnNsTHc2SzVoXzR1R2xLXzVfMFJ1RnJCU2RJZDJj?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxObTQzbWFHcU5FR0Y5YmVZYnR3d2otWjNGRHVPYm9DbVdQM1dHTlpOcEFJOGJLT2NkX2J6cm44WUJkQzl1YnBXYTFHRHBNcVZWWUNyT2lxZHowT25tRkd2Tml2dnRReWdIZVB5WTNUVlZNVVZFQ0M1SzJnWjQ5VjFSU3BCRWktSHZZ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNODdJLV9XbG85V0RTTi1lT2lZTm1KaWFVa2h6MnhXT21UWUlVenZWZFFnVW51Nk9LYWx4V2VPeW1TYlBzbUF6OGpTbWxSNGYtMVBGQklwMFUtenA0VFBRendROW9GRXNudnJGUlhubUhOZ2tPVDBTZ1dDeHFDOXg0ZXNaazlnajNGbnpwY3AzLWF0dw?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNMUpQNVBxajZZcHBrc1gxZWwwQ3VTZmMxV3lVam5TUU1YSFNYLW9ENTIyNUtoNGRWcVdXcGg5VEFZWFFWQ0RhNzBHbUZLNFRZNFRSMjVfSUN2eHFiOXNKV3A4ZHdOYTB5ck5TUTU4VWM0V3dFV1huQTAzd0xDREx0bEFqMjBuUGNlUEs3amJvbjJhd3ViczlxOUxTWUtzdTQ4RkF1YURLYWVTckJ1MmlJVmMyYXBOblk?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPdVhDY2h0djVhZ3dwUXNPSHg3TFFhT1NFUnVvNWpHanZ5M1kzS3JrSENsdlQzNmhHZUJJUjdNc2NXam1LSTdjV0VEZXNneS1Vc2RrZTR2Q1dvREUwUHUxUmJheDJjY1lQTV9zOFlfQ0Z1ZXJiTDJueGdXRnRobzNWQ3pVRmpWcW9tYnY4d0dwZjhuU1dGYUpFQ0VBbDVWQQ?oc=5
- https://news.google.com/rss/articles/CBMioAJBVV95cUxObHNrZldQUkx2YVRTWlA4WjFDS3VRR016Qm9VcmN3R2I4VkVfWi1pR0tCNEN4ajRxeEJLNm5OcUIzcG04cUozdU9BS3djOWM3dmwzVnhBQW9icmx6SjJjc21JZVZBQ3FpUTd2VTVjQm5iSFdTS1FVUHB5TFlMX3hoN1c1NUNySVE3N0VPTGVPSTZLQjhzTXl6aFJac003THN0bW5BemdKcnlWbVRiWEFDUFRSSGVjS2VtbHJRemtSbVVNVzI2ZmdVUDdqeW5zY3dzdkV1bXU4NWJkN1h6NWRzVE1jMU5wTU51V215cmtMUndreDBOc3NaTnRfeGxtcG0wZUhtQ2NnSk0zdjVvTHBhdmxVd0ozZlBac0VQdUpPMWI?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPZWE3aFRHaTlWWkdRRUxteUdMX1pOSVRBc1NlNmZTMFZlMEdMeHVQRDdSY1JfNlZHMVRZaHJNdkthM3ByYm1udHVFMVROVHhuVk82eGJtcFVXS3pDOTdrQmRfa0dEQ0lTUlNGcW1GenlDQ2QyWGt5dGVuaFNMRmNIQzBaMkt4c1JoenBsQlhEeTBXMmxNR3l0cFlR?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxONmpGNnEtZDhjWF9xZnZSMVF6Y1hUeWdSM09IQ0dla0JWand2Z1lSMzR5REVqZmRyZC1ubVlaeUxMZmtwRVF6dGtuQ3dtVHRoMWs2QTJfX1UzWExPWlFXMWdJOFZPNUpQNVd1MURvODVMSEw5MkMyVWxWdVJRX1Q0TGtNOEZYWGN5bmtKMXpibGRNcTU5LS1qcUVSX29NWFdzaF9aTQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQV1FWcTNHWTNfd3pnSmZ2MUJYWXpaWm0taXI3TFE5bmRyV041UjVRSUFiYmF6SENLYVV3ZWZiM2pZZ3FISlNUeS13MDhSaWdOVW10M09XVWVJVDllSkFaby1YYm9hZElMM1huZlU1OEJINmc4Z29QZC12Ri1hUThsWmc3TmdueXNoN3dYWlc0TTRHcDMyX1FjVVA1a21jelVzVmJmZU9LTTZwUQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPa1lzNGRJZmZXMG9yOG1XaWVBRXRycW1pTXU5SXE2Z0JBbDVLUXpDQTdoREJSbENSOGFlZGwtck9xMkNzbWpwbXBCZXlXWU5MSDFET1gxM3NxWG5xalA1NUM5T0RhcjFwTWZiSEJyVjN1akZXZzVhem92blQ1X3BFeUo2cUp2N24yNmY0STBNeEVrT2RqcFRidQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQcHNSX3ZyWGhORWM3UjJpeG9sblZJR3dFVXRCYzhRLXZlMnd3M2RyVGVDdW0xLVdBb0lXTmt0RG1ZMUVQS1NNb1VVWXZjTWtRcWdwdWxsSXRtdG1sTHN3MGJuYkJ5V3laY0F4Z2xjeHRLeHBJSmdnekw5cUc5OUk5bFdRUlFHU2RNdTlydHA0ZThyTUJiSGpVOWFvaG1pRFh1NGc?oc=5
- https://news.google.com/rss/articles/CBMigAJBVV95cUxOeWtpeEZnSHpka2xZUlc5dEFJaG9Md3A5SXk5MXpVckhEb3dmWXZyODJxT1FScC1OZmF5dEgtNTB5ZFpRTjBFV0Vhbl8yU2w4VkNrOWI1MmlkZHRWZ0RTYmtUOTI0dnRjSGFjQUh0UG8xS2lyZ1NjMFdqb2hXWm80TlJTRGxtYXVfYUYwUnU1ZGhKc2xEZjFKWUlMY0Y4QllIUkpIRVZfeS00VWM1S3lPcXBWQThIbWh5SlVuamF0TTA3REVBdTR2Mkl2TzdJdVY2WjU2YndwalJlY3JjM2ZfY3FUWV92bXpWUDBXUTlmb1dzOFR4SElEVGg0YnZsT0ZQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
