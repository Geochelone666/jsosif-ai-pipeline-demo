# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:37:37.660044+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 14, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'directional_claim_without_event_type': 2, 'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 7 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 58.33%; oldest publication 2026-11-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 149.3000 |
| Return 1D (%) | -3.9130 |
| Return 1W (%) | -1.0996 |
| Return 1M (%) | -29.2283 |
| Return YTD (%) | -19.7591 |
| Return 1Y (%) | -15.8375 |
| Annualized volatility (%) | 52.2853 |
| Beta vs SPY | 2.4270 |
| Max drawdown (%) | -47.5297 |
| Sharpe (rf=0) | -0.0844 |
| Downside deviation (rf=0, %) | 31.9966 |
| Sortino (rf=0) | -0.1379 |
| Historical VaR 95% (1D, %) | 4.3052 |
| Historical ES 95% (1D, %) | 5.9994 |
| Correlation vs SPY | 0.6930 |
| Tracking error vs SPY (%) | 43.2973 |
| P/E (trailing) | 16.04 |
| P/B | 13.50 |
| EV/EBITDA | 14.55 |
| Revenue growth (%) | 103.20 |
| Forward P/E (estimate) | 8.99 |
| Gross margin (%) | 74.92 |
| Operating margin (%) | 66.08 |
| Return on equity (%) | 117.36 |
| Free cash flow yield (%) | 2.75 |
| MA50 | 203.6544 |
| Close vs MA50 (%) | -26.6895 |
| MA200 | 202.6206 |
| Close vs MA200 (%) | -26.3155 |
| RSI (14, Wilder) | 37.4527 |
| MACD (12,26) | -16.9154 |
| MACD signal (9) | -16.2396 |
| MACD histogram | -0.6757 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 149.3000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.9130 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.0996 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -29.2283 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -19.7591 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -15.8375 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 52.2853 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 31.9966 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.1379 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.3052 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.9994 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6930 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 43.2973 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.4270 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.5297 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0844 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.9911 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.9210 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.0820 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.3640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.7528 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.0365 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 37.4527 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.6757 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -26.6895 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -26.3155 -> Clearly below the moving-average trend level.

## TAILWINDS

### Nvidia, AMD, and Micron stocks trim steep losses amid jittery AI trade
- Summary: Nvidia stock trims losses amid jittery AI trade.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOVk9mVUxsUll4NmpxRklUb1dFaHduU3ZURXZRV2ktV0pDM2ZMNElPb3RrV0NiS0JlLTVXQXJKNnpTV1JmV1k2NGMtdzNLa0F0c2tsY2xRMmJKZHhwY1dueWZXb0l4VXhWNkl4NmJ6QUlTNjBpZUItN0xkX21JUXJ5WGlUbWdON0E0V2FOT2lGYkozcm9VSjlXVjR3SDc5WWQ3VzJhWm5mb29YbjBQSU1hQURkYw?oc=5>

### NVDA Stock Alert: What to Know as Nvidia Reinstates Jensen Huang as CEO
- Summary: Information on CEO reinstatement, potential positive impact on investor sentiment.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNMk1OdWw0OUNTempyTUxOT19HRkRack4zalNNX014RVRaZXRiX0tvRzZ1ZDY5ZWdCYjlYYjUzNjVuLVJ4Sy0xcTkxMGMyemUtOVNiTDRlcEdyc1NkWHJjay16Q3dpN0ROSFllakIycEQ3U3cwOUw3X3QtTFJGWlU0RjRjSHhTVUdaaXNqc0xZZVVwbkNlQW54VQ?oc=5>

### Prediction: This Is What Nvidia Stock Will Be Worth by 2028
- Summary: Speculates Nvidia’s stock value by 2028, suggesting significant upside.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOc0Jod0ZBTDdSNzVmQ2o4Z2t2OHpkaGdBT1VBWmF2QWZfUkQ3SzRnOW16emZia3FaQTVoUDZVNGNnZ2toVmFjZXZvSno3RzlMWnFnNEYzSE9tYmFmWjlfWEYxOWJyelhBcnpVMnY0STVhc0ZUalAxeXlMTHFQc0U4bDVubUxsbk55REgzbm5aclZIbUVqMnVJdTZDRUtmYTJk?oc=5>

## HEADWINDS

### Nvidia Stock (NVDA) Drops 4% as S&P Flags ‘Compromised’ Board and Warns of Downgrade
- Summary: Nvidia Stock (NVDA) Drops 4% as S&P Flags ‘Compromised’ Board and Warns of Downgrade
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPWGhSeERSZWtuR0ZpQkVET25uSHpHcENTNXp2VXZrdFFNbHctRmtSQjBBOXRkMzAzTTktNHlhSGstNzhHbE1mTWRvWDBjNXRCMHlKczJyMjNwandRUzhHRmoyV1hmZjFoOWZMT194RFZkWUlPcnpzSS01bXV6b3VJVmhxYkNBNTZtcFp3NmlWVGhHSWszU2pRSkpCVUxXX2k5Q3hTTy1zZ3pWeHJn?oc=5>

### NVIDIA Just Dropped 31% in a Month. Will NVDA Stock Hit $125 or $200 First?
- Summary: NVIDIA Just Dropped 31% in a Month. Will NVDA Stock Hit $125 or $200 First?
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQVXFSdnRPQk1JV3F3SzQ5VHVza3dwb1RNVlk5WGt2QnA1OHlZaWRhdTRlRUdqSUlfS196STEwWXVNWWxOUE1BeW1PeWh3WmI1M1MzSUZvenZOVlplWnROYnl3NGswVTBmd3R3bU5peGpOWkF6MEIyQUZOOWlTMW1CMGZDOVd4XzJ6cS1yNEJuRFZlTzZjTDdTVg?oc=5>

### Nvidia Is the Worst-Performing "Magnificent Seven" Stock This Year. Is It a Buy Before 2027?
- Summary: Nvidia Is the Worst-Performing "Magnificent Seven" Stock This Year. Is It a Buy Before 2027?
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxPb1JfZkFPMnBSbjY3ekF0ZUpIUHpVVUgzTDdSbEgzeGIweHFfTFRuVWc1T3hZQ1R0Ynh5UkFJRFEwRmJNMjJ2OEJIS1pRcnZkcWczcEoyMk5QYTh2MzdaTkFSekx5cUNHZHdmRXZ6NUdXbGRZSUx4VmZob3ZMeGhYblpVcW44NHVMbnUzX09XYmVWYUp1SE1NaTl3WWpsZWQzX3l6MEtjZnlXTFdkRDVuaXJ4TDFwMjNUcXUzYkFvNHh6c0NXUzNKYUh0NA?oc=5>

### Nvidia stock continues to fall after massive rally, Jensen Huang apologizes to employees
- Summary: Nvidia stock falls after rally; CEO apologizes to staff.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxNYnBZTkhUUGlCUVBvdW9Mam9JbGJueElLNmRUenk3eTZ2YmhXSEJhb3VCTTlrQ0xDZzF1N3pURFZFNDROVkZhOW1Mc0JxQUhGQ25rSjdWZXdxMnZNLWFaNzJfdXdFeEpUMzFQMUl3alZfWVotcFRHRGxSRzNiWHJuSlpyaXVHTld1MDFLSy1rdDJCU1F6ME9vZDB1bzB2bS1PeHpZbTg5czJrQ1lzdFRHbUlmS3JzYlFvQnRjZ2xRT3hoR1FVMUQ2a0hNMXZwNEtYckw1Q0ZYOThJMTlobXZTY3JzdDFESjBN?oc=5>

### NVDA Stock Alert: Nvidia CEO Jensen Huang Rejects Calls for Succession Plan
- Summary: CEO Huang rejects succession plan calls, raising governance concerns.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQanBEQ2g0YVdlS0owSUNzQXQxV0pnMjVfZ3M0di1YaFIxejgxT2lVeGIyQThMT3dOMUlkQ3IxLVNlYlhFVFMySHE4UWhQQWFtNDZycDhUSXNyZTJCZXo3ZjFoM0JMZXNqcjF0NXVORXF0Uml3cjdaWmhjMEZSRUZ4UDFLbmFCSUJqQTBZZkdMTVoxVjVJR1Zn?oc=5>

### Nvidia stock falls after epic rally on Jensen Huang's return as CEO
- Summary: Stock decline following rally, indicating market skepticism.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPQ2VuMWM0TmxDX1JHckNONUktS3M3eFVSbDVJeWQ0bWZsUFlhWTZ6dkZWSi1lUTlZUjVnamk5OTQ4bTBBc2ViWHJzekF0cTlWSlo0blR1ZkU2RDNYVU5QbnJOaDcwZVlmWlljTHEwRV9wQ2pfdG9nNG1icTZvcnBwalZFZGRCa3Q0dTNvQ2dWcVdzTnlGcHZEajN4ME5URDNTTV9RODhxSWQzdlBTZUZDZTF1ZkExektQMVhibk5PdFoyMEJfMmtIYnZR?oc=5>

### Jensen Huang’s Return Doesn’t Make Nvidia Stock (NVDA) a Buy
- Summary: Analyst opinion deems stock unattractive despite CEO return.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPSndtT1dTZXdiYWpqTXRoMktMU3pTZ3U0d1lMTURLenJTa1BpdkE5c0IwNnVPTFJYX2NidVRlb2FuT3BNZFptMDBvQ3ZPdTVEbGowUlRvbVlpNXpZRFlTQUkyd0VMTmtmUUZfWjlnWWJYbVJYY0VGa3BDVEU2clpGR18zbmlaV0xOTWRDb2xWYnBhWE5iZUdJ?oc=5>

### Why Nvidia Stock Is Falling Again
- Summary: Explains factors causing Nvidia stock decline.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOVnZYQmNDcUVPbkdnb3J6b2xpMU9DVFFqbTNBdDFnTUk2cDBHbTNXQnBuVk9vRWVVdmYwN3dCWjF5RTZRSXV3dENOVGRnLU9BYjkxelMxNi1jRVpneUVmOEdoVjVSUGszREFxNE0xVjM2b2FlOXF5UDJQV0VEVEJra2lCeC1iZUpIQmF1SnZpWklreDQ2MVpjZG90NA?oc=5>

## CATALYSTS

### Nvidia (NVDA) Stock Looks Below Fair Value After Recent Turmoil
- Summary: Nvidia (NVDA) Stock Looks Below Fair Value After Recent Turmoil
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQbUpxbnpVNGpTNThJa3dsbWR4R3cyQ3hWbVFydFJ6bW10dldabWVTU3hPMGRoZlFhczNXZWgzbHppOVBIZzNKb1VTNWZ0dFd3S3lHdTJFRkdJOUo2N0FIQ1I3VnVPLVdwSWdmS1NsbWVmVW9WVXdrOFI5TnV2a1JFb0dfVWRjUWxMMUhwT0FQdUdRMEFvVFBjTjZR?oc=5>

### Nvidia Sell-Off: You Won’t Believe How Cheap the Stock Is
- Summary: Nvidia stock falls sharply, seen as cheap.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOcU1sN2NqMk9iRHNZTTNZTldZRVc4UWhvZXhTZ0NOd3M3TEphU2JXbmxyaTZoTnJXOHg3SjlTamhxb0FvZlFTQVo2OERzeldyQXNQanJzZmhYUFNYWXI0MmE5UThjVXN4OUEzUHVWQ3FQSkFBTFV1VlROQjN6ZmZYVVQtV2VzWnRod1R4TXVIMFJPVFBGTGVteFgwTlU4RUx4?oc=5>

### Why Nvidia (NVDA) Stock Is Falling Today: Tech and Chip Selloff
- Summary: Nvidia shares drop amid broader tech selloff.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPbUtXWTRwbjJyUHJSeW96c01xRU5wT0hINTlCU0hhRXpIc2dQa2hhSkpSRkwyeW9YSFhHOGpPVVRTb0Z4Tzd1Z3cyaWV0NWM2emR1Qk5lTktDdnhwYVBsTWdnOXFsbDVnV2hMVDNQbVNvNFJGeUVrTno2eDZSZExtWjZfZVRKMGNjT3czM2xHSm1OUEtnSG1SN0F3?oc=5>

### 5-Star Analyst Revamps Nvidia Stock Price Target for 2027
- Summary: Analyst updates Nvidia 2027 price target.
- Date: 2026-11-25 | Impact: medium | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNS2hzS1B6LVBLQ0RHeU1Za29PUWxpRWdMeVc2cXhPZm1lWF8zYkFIenR6VFR0d0Naa2F2cEN1M0tvbDV1Y3dzdTYzTXZ0cVVRakVLMzRfTU91eDJWb1VZWHFieG1QSF9adzlfeGpBUEpRTkxTQzVyTzJUU1JkU1lORHlFa2xyWDJjYnhmOWFhY2F1RE82anh1SGhR?oc=5>

### Nvidia Stock Has Found Its Next Big Catalyst, Making the Stock a Once-in-a-Decade Buying Opportunity.
- Summary: Identifies a new catalyst driving Nvidia stock upward.
- Date: 2026-11-26 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxPNlYtanViOVZ0ZUxOeUxTeXpWaXE5Slc5R2tLNjU4UDI3YzVEUnV0ckNfQ1QtOGxySUI1REtKd3JSQ3RqOF9ab0VCVDlrMk9maFFTbEtNRHdtbHJPTzM3MHlENl81WjFYdUJueGdtQ3F5Q05lMTJIWnRtaFR1OG41a0VoVGtTN0JwaUI5WTN4SnJhV1VfRFZ5S200TUxISFZKYmZJNjh0bWxMLTktaERMX0FWN1JxLWl0dFNNeXY4a3BabHVIMlQ2QkNXSVhYZldJZUJzVEtuc2NxZw?oc=5>

## RISKS

### Top Analyst Flags 5 Major Risks for NVDA Stock, Says Nvidia Could Stay in ‘Penalty Box’ for 1-2 Quarters
- Summary: Five key risks identified, potential short-term performance impact.
- Date: 2026-11-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNM0h2OGVIVXpRNWtNWDd6bk5iWnJmZTAtNG5sOW80UnpZbUJKOXVlUHB5WUk0TGVoYkJ6aHhuZUV0YkFrdWVSaEJjV1ZGaTczRnYzUXBydG92VUc1WGR5SjN3SndmczZIYUpNdkFpM3RQMHlCdUtLcmotZHEybXhKVUlpaUFqUkZzNjBLRVM3b252WmZXRjlPUnZuRVJXM3lRTWViMmc4bzJKT3UwZTJoc1V6OWJ1YTVxdDVXVV9ndUduTkMzb0E?oc=5>

### Here’s How Quickly NVIDIA Could Reach $200 Following Jensen Huang’s Reinstatement as CEO
- Summary: Assesses rapid price rise risk after CEO reinstatement.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOQ3VDQU5Oajd1RGlFYjZRM28yQVBtNmV6MnZJSVVJbFhhcjhxOFVXTW90UDJQOTZzSGtTRlZRcVdEZzFEVDhob01NZy1xRDZPYzY1WmhzQkZBSXpsS01wWmpWRmpQcjJLM1BERm1HVGpJSnVmWlU2clVsNmd3dDU1RngwazN0Qk83NWRYSmVmSUM0alZHNjFXcEZwRQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **16.04** | **13.50** | **14.55** | **103.20** | **3,605,147,156,480.00 USD** | **-15.84** |
| AMD | 86.76 | 9.74 | 59.17 | 44.70 | 672,006,275,072.00 USD | 96.98 |
| AVGO | 38.42 | 14.41 | 28.16 | 85.50 | 1,436,194,177,024.00 USD | -21.28 |
| INTC | N/A | 2.52 | 15.80 | 20.90 | 289,508,032,512.00 USD | 52.02 |

Peers fetched as_of: 2026-11-26; NVDA reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-17
- Next expected earnings: 2027-02-24 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-26

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

- https://news.google.com/rss/articles/CBMiswFBVV95cUxOVk9mVUxsUll4NmpxRklUb1dFaHduU3ZURXZRV2ktV0pDM2ZMNElPb3RrV0NiS0JlLTVXQXJKNnpTV1JmV1k2NGMtdzNLa0F0c2tsY2xRMmJKZHhwY1dueWZXb0l4VXhWNkl4NmJ6QUlTNjBpZUItN0xkX21JUXJ5WGlUbWdON0E0V2FOT2lGYkozcm9VSjlXVjR3SDc5WWQ3VzJhWm5mb29YbjBQSU1hQURkYw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNMk1OdWw0OUNTempyTUxOT19HRkRack4zalNNX014RVRaZXRiX0tvRzZ1ZDY5ZWdCYjlYYjUzNjVuLVJ4Sy0xcTkxMGMyemUtOVNiTDRlcEdyc1NkWHJjay16Q3dpN0ROSFllakIycEQ3U3cwOUw3X3QtTFJGWlU0RjRjSHhTVUdaaXNqc0xZZVVwbkNlQW54VQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOc0Jod0ZBTDdSNzVmQ2o4Z2t2OHpkaGdBT1VBWmF2QWZfUkQ3SzRnOW16emZia3FaQTVoUDZVNGNnZ2toVmFjZXZvSno3RzlMWnFnNEYzSE9tYmFmWjlfWEYxOWJyelhBcnpVMnY0STVhc0ZUalAxeXlMTHFQc0U4bDVubUxsbk55REgzbm5aclZIbUVqMnVJdTZDRUtmYTJk?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPWGhSeERSZWtuR0ZpQkVET25uSHpHcENTNXp2VXZrdFFNbHctRmtSQjBBOXRkMzAzTTktNHlhSGstNzhHbE1mTWRvWDBjNXRCMHlKczJyMjNwandRUzhHRmoyV1hmZjFoOWZMT194RFZkWUlPcnpzSS01bXV6b3VJVmhxYkNBNTZtcFp3NmlWVGhHSWszU2pRSkpCVUxXX2k5Q3hTTy1zZ3pWeHJn?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQVXFSdnRPQk1JV3F3SzQ5VHVza3dwb1RNVlk5WGt2QnA1OHlZaWRhdTRlRUdqSUlfS196STEwWXVNWWxOUE1BeW1PeWh3WmI1M1MzSUZvenZOVlplWnROYnl3NGswVTBmd3R3bU5peGpOWkF6MEIyQUZOOWlTMW1CMGZDOVd4XzJ6cS1yNEJuRFZlTzZjTDdTVg?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNM1Bja1BxWDc0aEdqbmV4Q01STV9qcTFZd1JpN2N1Rlp3N0dCclpxOEtKUEN2ODlrRVgtaHljYXlweHgtbjdfUDZ0dlZjdkw0anFSSF9ZajhUV1RjZGNnZzFnVVl3TUtOVXVXdi02a3psbW9Gb3Y3ZTdPdmN6MUlaV1E3ZDV3OUlPVWlGNGZRMm12NWI2WUhzU21MTDhsZUVzcW1mNzhVMUo1RGllMlJ6bUlyc0M?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxPb1JfZkFPMnBSbjY3ekF0ZUpIUHpVVUgzTDdSbEgzeGIweHFfTFRuVWc1T3hZQ1R0Ynh5UkFJRFEwRmJNMjJ2OEJIS1pRcnZkcWczcEoyMk5QYTh2MzdaTkFSekx5cUNHZHdmRXZ6NUdXbGRZSUx4VmZob3ZMeGhYblpVcW44NHVMbnUzX09XYmVWYUp1SE1NaTl3WWpsZWQzX3l6MEtjZnlXTFdkRDVuaXJ4TDFwMjNUcXUzYkFvNHh6c0NXUzNKYUh0NA?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxNYnBZTkhUUGlCUVBvdW9Mam9JbGJueElLNmRUenk3eTZ2YmhXSEJhb3VCTTlrQ0xDZzF1N3pURFZFNDROVkZhOW1Mc0JxQUhGQ25rSjdWZXdxMnZNLWFaNzJfdXdFeEpUMzFQMUl3alZfWVotcFRHRGxSRzNiWHJuSlpyaXVHTld1MDFLSy1rdDJCU1F6ME9vZDB1bzB2bS1PeHpZbTg5czJrQ1lzdFRHbUlmS3JzYlFvQnRjZ2xRT3hoR1FVMUQ2a0hNMXZwNEtYckw1Q0ZYOThJMTlobXZTY3JzdDFESjBN?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQanBEQ2g0YVdlS0owSUNzQXQxV0pnMjVfZ3M0di1YaFIxejgxT2lVeGIyQThMT3dOMUlkQ3IxLVNlYlhFVFMySHE4UWhQQWFtNDZycDhUSXNyZTJCZXo3ZjFoM0JMZXNqcjF0NXVORXF0Uml3cjdaWmhjMEZSRUZ4UDFLbmFCSUJqQTBZZkdMTVoxVjVJR1Zn?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPQ2VuMWM0TmxDX1JHckNONUktS3M3eFVSbDVJeWQ0bWZsUFlhWTZ6dkZWSi1lUTlZUjVnamk5OTQ4bTBBc2ViWHJzekF0cTlWSlo0blR1ZkU2RDNYVU5QbnJOaDcwZVlmWlljTHEwRV9wQ2pfdG9nNG1icTZvcnBwalZFZGRCa3Q0dTNvQ2dWcVdzTnlGcHZEajN4ME5URDNTTV9RODhxSWQzdlBTZUZDZTF1ZkExektQMVhibk5PdFoyMEJfMmtIYnZR?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPSndtT1dTZXdiYWpqTXRoMktMU3pTZ3U0d1lMTURLenJTa1BpdkE5c0IwNnVPTFJYX2NidVRlb2FuT3BNZFptMDBvQ3ZPdTVEbGowUlRvbVlpNXpZRFlTQUkyd0VMTmtmUUZfWjlnWWJYbVJYY0VGa3BDVEU2clpGR18zbmlaV0xOTWRDb2xWYnBhWE5iZUdJ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVnZYQmNDcUVPbkdnb3J6b2xpMU9DVFFqbTNBdDFnTUk2cDBHbTNXQnBuVk9vRWVVdmYwN3dCWjF5RTZRSXV3dENOVGRnLU9BYjkxelMxNi1jRVpneUVmOEdoVjVSUGszREFxNE0xVjM2b2FlOXF5UDJQV0VEVEJra2lCeC1iZUpIQmF1SnZpWklreDQ2MVpjZG90NA?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQbUpxbnpVNGpTNThJa3dsbWR4R3cyQ3hWbVFydFJ6bW10dldabWVTU3hPMGRoZlFhczNXZWgzbHppOVBIZzNKb1VTNWZ0dFd3S3lHdTJFRkdJOUo2N0FIQ1I3VnVPLVdwSWdmS1NsbWVmVW9WVXdrOFI5TnV2a1JFb0dfVWRjUWxMMUhwT0FQdUdRMEFvVFBjTjZR?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOcU1sN2NqMk9iRHNZTTNZTldZRVc4UWhvZXhTZ0NOd3M3TEphU2JXbmxyaTZoTnJXOHg3SjlTamhxb0FvZlFTQVo2OERzeldyQXNQanJzZmhYUFNYWXI0MmE5UThjVXN4OUEzUHVWQ3FQSkFBTFV1VlROQjN6ZmZYVVQtV2VzWnRod1R4TXVIMFJPVFBGTGVteFgwTlU4RUx4?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPbUtXWTRwbjJyUHJSeW96c01xRU5wT0hINTlCU0hhRXpIc2dQa2hhSkpSRkwyeW9YSFhHOGpPVVRTb0Z4Tzd1Z3cyaWV0NWM2emR1Qk5lTktDdnhwYVBsTWdnOXFsbDVnV2hMVDNQbVNvNFJGeUVrTno2eDZSZExtWjZfZVRKMGNjT3czM2xHSm1OUEtnSG1SN0F3?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNS2hzS1B6LVBLQ0RHeU1Za29PUWxpRWdMeVc2cXhPZm1lWF8zYkFIenR6VFR0d0Naa2F2cEN1M0tvbDV1Y3dzdTYzTXZ0cVVRakVLMzRfTU91eDJWb1VZWHFieG1QSF9adzlfeGpBUEpRTkxTQzVyTzJUU1JkU1lORHlFa2xyWDJjYnhmOWFhY2F1RE82anh1SGhR?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxPNlYtanViOVZ0ZUxOeUxTeXpWaXE5Slc5R2tLNjU4UDI3YzVEUnV0ckNfQ1QtOGxySUI1REtKd3JSQ3RqOF9ab0VCVDlrMk9maFFTbEtNRHdtbHJPTzM3MHlENl81WjFYdUJueGdtQ3F5Q05lMTJIWnRtaFR1OG41a0VoVGtTN0JwaUI5WTN4SnJhV1VfRFZ5S200TUxISFZKYmZJNjh0bWxMLTktaERMX0FWN1JxLWl0dFNNeXY4a3BabHVIMlQ2QkNXSVhYZldJZUJzVEtuc2NxZw?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNM0h2OGVIVXpRNWtNWDd6bk5iWnJmZTAtNG5sOW80UnpZbUJKOXVlUHB5WUk0TGVoYkJ6aHhuZUV0YkFrdWVSaEJjV1ZGaTczRnYzUXBydG92VUc1WGR5SjN3SndmczZIYUpNdkFpM3RQMHlCdUtLcmotZHEybXhKVUlpaUFqUkZzNjBLRVM3b252WmZXRjlPUnZuRVJXM3lRTWViMmc4bzJKT3UwZTJoc1V6OWJ1YTVxdDVXVV9ndUduTkMzb0E?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOQ3VDQU5Oajd1RGlFYjZRM28yQVBtNmV6MnZJSVVJbFhhcjhxOFVXTW90UDJQOTZzSGtTRlZRcVdEZzFEVDhob01NZy1xRDZPYzY1WmhzQkZBSXpsS01wWmpWRmpQcjJLM1BERm1HVGpJSnVmWlU2clVsNmd3dDU1RngwazN0Qk83NWRYSmVmSUM0alZHNjFXcEZwRQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
