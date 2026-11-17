# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:39:17.585790+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 19, 'rule': 6, 'ai': 7, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 19 unique headlines; 10 named publishers; 0 exact duplicates; 19 HTTPS source links; largest publisher share 26.32%; oldest publication 2026-11-10

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 146.4300 |
| Return 1D (%) | 0.6807 |
| Return 1W (%) | 3.2069 |
| Return 1M (%) | 11.3621 |
| Return YTD (%) | 5.1334 |
| Return 1Y (%) | 4.4657 |
| Annualized volatility (%) | 21.7174 |
| Beta vs SPY | -0.1942 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | 0.2480 |
| Downside deviation (rf=0, %) | 14.3716 |
| Sortino (rf=0) | 0.3747 |
| Historical VaR 95% (1D, %) | 2.2001 |
| Historical ES 95% (1D, %) | 2.6412 |
| Correlation vs SPY | -0.1231 |
| Tracking error vs SPY (%) | 27.1069 |
| P/E (trailing) | 18.42 |
| P/B | 8.96 |
| EV/EBITDA | 12.54 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 16.98 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.05 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.53 |
| MA50 | 133.8138 |
| Close vs MA50 (%) | 9.4282 |
| MA200 | 143.6789 |
| Close vs MA200 (%) | 1.9148 |
| RSI (14, Wilder) | 67.8098 |
| MACD (12,26) | 3.4433 |
| MACD signal (9) | 2.7979 |
| MACD histogram | 0.6454 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 146.4300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.6807 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.2069 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 11.3621 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 5.1334 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.4657 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.7174 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.3716 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3747 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.2001 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6412 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1231 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 27.1069 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1942 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2480 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.9827 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.0460 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.5324 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.4189 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 67.8098 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6454 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 9.4282 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.9148 -> Slightly above the moving-average trend level.

## TAILWINDS

### PepsiCo (NASDAQ:PEP) Stock Jumps 2.2% - Here's What Happened
- Summary: PepsiCo (NASDAQ:PEP) Stock Jumps 2.2% - Here's What Happened
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPdkNQWXlFTFF4UlZya3BZMUpMdDBhYUVPeHEzd0RGU1hpOEtIcTBMc2t2MHVqU3ZnYmRINkI4Ujh6ZjZUTDRfczZCUEVlQ3d1NGY2TUs4bGdfT2xiSEdqbS1ta0dfSEdtMHZFVHVRVC1oWVhFVmRlMUdXSGF0NHlodzdnbndQbEVqc29oaTg2NXA4T1NvTTM1ZDhrdnZYSEtDT2NzN0Jac1ZoSk05QllDd1Vkaw?oc=5>

### PepsiCo says 94% of high-risk sourcing in company-run activities is deforestation-free; cocoa sourcing is 59%.
- Summary: PepsiCo reports high deforestation-free sourcing rates, indicating stronger sustainability practices.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNbUpBVEVqNkJJNUowUXBoNVc5b29yVDJDdENMQ3NqZ0hGN3E3NWMxQWtTUHFXWFBnWEd1eEdQV0Jwd2tFX0w0eFduUUJCdk9vc2VqeHBpZlYwSGdKOEZOaEtkSjNDYzkzWXpzb3hqZV9lajlkdkFrSFR0c3QwU0E3ZHdIU2RVQ2d6X3F1MDg1MF9yLUhTaDhmTi1UY3JkajBQZmdOVzFIUWF2Yy1YdF9sdDctSTg2Z1U?oc=5>

### What's Fueling PepsiCo (NASDAQ:PEP) Growth Across Global Markets?
- Summary: PepsiCo's growth driven by global market expansion and product diversification.
- Date: 2026-11-14 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOUVFxdGl2XzVLY1NGejhRUG9nYl80bFM4RjZDUU1GMkxDOGljNzNuVnJkLXVmQVFVckJ1V0kzNFI4MnFGVloxSlh0SkxmSGdaTFkweUFmelJRbUYxU2JXa09UTzR2ZmkwY1FpLW1Ibm01MVhxc3BHMEZGUUtIYkV1T29pbEJnN2FwMmJNOXBLSVl6V0t1YlhtSmVvdk85NWJjSzhXME1nYw?oc=5>

## HEADWINDS

### PepsiCo Stock Drops 2.4% in 6 Months: Is More Downside Ahead?
- Summary: PepsiCo Stock Drops 2.4% in 6 Months: Is More Downside Ahead?
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNdmZKNDhmOV9UTnEyMDd6Z2hKVTZUaXpSeGExT2VuMGNvbElETFJERDFnY3paRFREY2l1dF9iZGpzMTBnakowVS1kS0FmYkc2RUdIanhoYXEyZUktd19MeFRSUmNKZV91bk80VG1BakkyRExyWEdrMUwyd3ZsdENsdC0ybmcwNTEtVjdoM3ZET1g2bC10ZWtjWG02bWlIb0I2QW5tdWVOUjc4RGtRRl8xeE50cU4?oc=5>

### PepsiCo layoffs: 1,000 jobs slashed as North America CEO pushes for soda giant to ‘be faster’ and ‘more capable’
- Summary: PepsiCo layoffs: 1,000 jobs slashed as North America CEO pushes for soda giant to ‘be faster’ and ‘more capable’
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOWjFORHFEemN1NXVYVklpUE03dndCNEVLdzBXbjVmV3NaN1Z1QVFCaURUV0tWRjhuTFA5OXpLdllkRmdBZnIzTWNyNTV3eHZJbUZxa3FhaFF0SWlrTlVaOU50MzFsempTTG52cURsUWNwMkphYU9Ya3hOM3VaOFNESW5wdGltWXV6VF81RS1nQXRjcy0wdEE?oc=5>

### PepsiCo (NASDAQ:PEP) Stock Price Down 1.2% - Here's Why
- Summary: PepsiCo (NASDAQ:PEP) Stock Price Down 1.2% - Here's Why
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQekl6NkVNTlBJZkNyLTNrOXEtV1dCOEo3OVhoc3JfcGYxRjNJTEYzaFlMa0RtLUZ5eXVlOGIwQkZydlpUbERha29QS09pZnpDNU1YZVBkX2c0OTZNMUs4MFgwY0U4T0xZOW1Xa1Vxclh3U1RrcExfckNZWUpJR2ZvUXViLWRjMnZQU3NTbEdFZVQwbDlBMWg2T3dRbk9Kamg3N3lERzNqcGZVOTlR?oc=5>

### PepsiCo slashes 1,000 more North American jobs after a string of plant closures — despite netting billions last quarter
- Summary: PepsiCo announced cutting 1,000 North American jobs amid plant closures, signaling cost-cutting amid profitability.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOekRKTzFid2lkem1QXzVxUi0yOEtrdGh0YXNDUEVnOEJqLWRUYmRRbXdmNUZOT1JFcGF2TnhCQVpWeGJ4dVh6UVlnNU9LQmp5bFJtTlpVWnZGMm1zX1dXcUtGTE41Rlg1eGRfSC12YnRyUzNoQVNBaWVwaS1UTV93TF82YjNjbVlyWGRCWUY4V3lfaFBNQ3c?oc=5>

### PepsiCo ‘to cut 1,000 jobs in North America’
- Summary: PepsiCo confirmed a 1,000 job reduction in North America, reflecting operational restructuring.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOTnc5eHpOUkNtNmZUblU2c3BudDZaY3o5WV9CS0RTYll6dm9WWDRhM0xWY0ZkMVhZSDZfRkR4aTNMSDVHYTFnSVZ0NlBCcFpWLTN0dFpqcmFxeHYzLXdnU0hSMWQwemdzN0ZvNlM2UXRsY3J2RDNBaGw3LXlJWUV0Y2VpeVhVOWpzN3ZDNE5BMUU?oc=5>

## CATALYSTS

### PepsiCo, Inc. $PEP Stock Sold by Danske Bank A S
- Summary: PepsiCo, Inc. $PEP Stock Sold by Danske Bank A S
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPWjFhWkg5UWkwVlNIWlp0QXJhRGp3dk9UdV82V01YSTJpZWdVdU1nZDN3RnZfOXJ3NE5JLTY4VTlfWHlOc21RLXdHMDN5LUdlZXJ2MFltRzZIV3lId2dmVERlM0FpMFpwNEVHc1haOTdIcWFFQ2RnNTNrSktMR2R6d19NR2N6LVRhWUJGeW44QVZWSS1PNHVqUFpRV2RfMjJ3bjd6TlRhTnRTQQ?oc=5>

### PepsiCo Stock And Other Dividend Names Worth Watching As Rate Hike Risks Return
- Summary: PepsiCo Stock And Other Dividend Names Worth Watching As Rate Hike Risks Return
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxPRmhNV2g2eE44SW5VOGc3Zi00NHIxdE4yYW81LVJoM3lzcDY1Rk5zTTJYRXZFVUgzZEtfZXJzYnppeGhnbndNd2RYUmhRSldHNkl1NDdEeFo5Y3A1cTlzN3AtZU9neG12dHNIdEtiZU9hZUx2TkxYRVpxQzRieUJuWXRsRmRsQ015akwxUzZSSTI1ckJfbkxncjM3U1UxUWJTd3kyeTluODFlY1F5aTdSWHlYVGdXendzbHpILWdjNFFxbzFWQXlGeTlQMUUtRzg4NWRtc9IB2gFBVV95cUxPMFpnblNGQzlEa25xWU0xNTNFLWVLVDlOYjVVZ2c3dkNyY1B5QjNaNm1CalpBSXJFU1FMVDFvaEUyNkFDckxfYjh2bHFuT3pYMjkycmx5N0ZXWVNEWC1vWmZRZ1FwMlk1Q0hlRms4MGZvOVpzdk5pTGdEQ0txc0xYVjBuQVQ3d19MWnozcHBKTHBLLUxtYVAza3pqUWdET05PTnlxRUNzTUhrcWt3M29yU2o0bk9CVm9lY1ZpU1QxY1F0Tm05czhkZHo3MUZ1c0g3bjJhd1ZHUlFvZw?oc=5>

### Is Lower 2026 Guidance Altering The Investment Case For PepsiCo (PEP)?
- Summary: PepsiCo's 2026 guidance may affect investment outlook.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxQRHAwZTFpZ29MVEhlNDA3bTJqaC1FeTIwSEozaFJPNDA0TE8wY0FwalI4MmFlV2ZJSUF4cmhHdHl3S29rSzNnRDk4cEdBcTNxVWl5NHdTS056WVR6ZlVVZTVpNjFKWDFlQkdydk96dTRNdFFEd1dUcE1QV2FaX3Q2LTVJVl9oRGhEQmVSQTc3RzFscTREczJOMF8yUDV6eUpvWnVnQkV2ZEFoN2NFT2J3ZXh2a3E1S3ZteTY4T1o5UXdiWDBPcjQtOG9Ka2ZZa0phUVJYTtIB2gFBVV95cUxNY2xnN0k5QWRYbnp6Rzc4YW9wbE14TElOMDhCQ3o0YWV0Mm9CQ2VfWjVYNTRYeHB6NVF0OGRuOXQ3b2hYT3lqUGtSckU1bkJJWWFDbS1CdklaZkd1Vk8xTUp5TGVOamd6eUpwd1pEWjMwTXJIWUw0blg3eU1SaGF2a3NCdEFralFjMzZCWVZBSXVtbTFrQlByVUl1d3E3eWNJRVQ3Y0tWV21BWUhkbDRxZ3l1UUdCYzAtdVA3ekprUjZZcXI1b0RybUM2THZvVTVjUlNjUllsRnVfUQ?oc=5>

### PepsiCo (PEP) Cuts 1,000 Jobs, Is The Stock A Bargain?
- Summary: Job cuts could signal cost-cutting but may impact morale.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxOd1NlejQ3S3lTcnUyN2JrUm5YcUJxNldEZjQ4RHZFb0tZa1dPY1JwSU8wZzc1Zi0wRVFuSjNlS2NxTWE2b0hQUXVlcy1fNTdENWZPaDJYTTR2QWVFQnQ2eEpTRzJtbm9SV21SSUE1N0VCeFY5QzRmX1o5Mm0yQ1l5RjR4ZWh1d250R1RCMUhPdFp6TGFHcUhNbUIzMTV3MkRWcW1fUnlGME9GUmFTY2xfVzcyaHBuTUswSGdhX3J1Nk8tMGI2ZHfSAcsBQVVfeXFMT01IRERycWtBX1FPYW5mLXIzZVd5aHpPWjQyR2t0Zko5czBfbjFXVVNvMFdYS2hWTERtSWN0NVJyM2NDTDhIRnRLYWRxTzFWMXhwODlTNUUya1k2NGVtVXVlQU1paXo4Tzd4VTl4SVh0UE5mb0VNSjdiVDlBa3htM2xJbTBxX0FBUll6ZkJ2ZklmZHppTXMxSEZOTUpRMHZrSFRqeTVZa3QyMlFzcm51Y3BIQlBwWGJOeEVCQ1FFM0NSdVJLSmhSQ0ptRFk?oc=5>

### PepsiCo (PEP) Stock Could Be Below Fair Value On Cash Flow
- Summary: Stock may be undervalued based on cash flow analysis.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxQa1FBd3lLTDU1OE1vQzByRlphSWJZY05HS1ptZGpfZEgyMVJMQlVTMUt3LUVvWjRTYXpIbWUzMEdSN3BqUjJVdjBOb0J4X1ByMHpaZWxrX041NVFRalVPMnNvUXFoOG1qV1k2NXVPc1BubFRLcElDUGROTUdreldNSm5OOHd4anhIaGZKSmU3ZWZGUkc5TmZtWkpad3psdmZLMWRua3pFYTBnUzV0Uy0wUGo4Y2pEcGk0TzBmaWI5am53NENacFJHaGYtdFd3ZE3SAdQBQVVfeXFMT1BUY2dJbXFWeXBrbWIxV3Rlb0o2SWFtRkhYRGx2Y21rc2tGU3l2S1ZmVEpfaW0tb0QyLXdpSFdfdkpKWnU3UjlEMTZ3TkFiT2NRM19CVHlCa2dMRmlrQ2JMQ0tGbVVvYkRiaUpLZDh0UWxpWVlnblhhdTBfeEV4NXdPc1FHQUxZV2dtXzVURWpOcjJIY01jQkxHRUpmZmw0QzlWdk8xb2Z0bkFma3lNOWZySnFzZ2sxMEhhWkxRUlRZV2ZnZHVFeVh4UWx2VnE5el9qOEY?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **18.42** | **8.96** | **12.54** | **5.60** | **199,546,175,488.00 USD** | **4.47** |
| KO | 29.35 | 11.45 | 26.14 | 7.40 | 427,953,258,496.00 USD | 43.51 |
| MNST | 41.64 | 9.11 | 28.88 | 16.70 | 89,654,042,624.00 USD | 28.45 |
| KDP | 32.05 | 1.90 | 16.44 | 70.60 | 48,422,543,360.00 USD | 35.32 |

Peers fetched as_of: 2026-11-16; PEP reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

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

- https://news.google.com/rss/articles/CBMiswFBVV95cUxPdkNQWXlFTFF4UlZya3BZMUpMdDBhYUVPeHEzd0RGU1hpOEtIcTBMc2t2MHVqU3ZnYmRINkI4Ujh6ZjZUTDRfczZCUEVlQ3d1NGY2TUs4bGdfT2xiSEdqbS1ta0dfSEdtMHZFVHVRVC1oWVhFVmRlMUdXSGF0NHlodzdnbndQbEVqc29oaTg2NXA4T1NvTTM1ZDhrdnZYSEtDT2NzN0Jac1ZoSk05QllDd1Vkaw?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNbUpBVEVqNkJJNUowUXBoNVc5b29yVDJDdENMQ3NqZ0hGN3E3NWMxQWtTUHFXWFBnWEd1eEdQV0Jwd2tFX0w0eFduUUJCdk9vc2VqeHBpZlYwSGdKOEZOaEtkSjNDYzkzWXpzb3hqZV9lajlkdkFrSFR0c3QwU0E3ZHdIU2RVQ2d6X3F1MDg1MF9yLUhTaDhmTi1UY3JkajBQZmdOVzFIUWF2Yy1YdF9sdDctSTg2Z1U?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOUVFxdGl2XzVLY1NGejhRUG9nYl80bFM4RjZDUU1GMkxDOGljNzNuVnJkLXVmQVFVckJ1V0kzNFI4MnFGVloxSlh0SkxmSGdaTFkweUFmelJRbUYxU2JXa09UTzR2ZmkwY1FpLW1Ibm01MVhxc3BHMEZGUUtIYkV1T29pbEJnN2FwMmJNOXBLSVl6V0t1YlhtSmVvdk85NWJjSzhXME1nYw?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNdmZKNDhmOV9UTnEyMDd6Z2hKVTZUaXpSeGExT2VuMGNvbElETFJERDFnY3paRFREY2l1dF9iZGpzMTBnakowVS1kS0FmYkc2RUdIanhoYXEyZUktd19MeFRSUmNKZV91bk80VG1BakkyRExyWEdrMUwyd3ZsdENsdC0ybmcwNTEtVjdoM3ZET1g2bC10ZWtjWG02bWlIb0I2QW5tdWVOUjc4RGtRRl8xeE50cU4?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOWjFORHFEemN1NXVYVklpUE03dndCNEVLdzBXbjVmV3NaN1Z1QVFCaURUV0tWRjhuTFA5OXpLdllkRmdBZnIzTWNyNTV3eHZJbUZxa3FhaFF0SWlrTlVaOU50MzFsempTTG52cURsUWNwMkphYU9Ya3hOM3VaOFNESW5wdGltWXV6VF81RS1nQXRjcy0wdEE?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQekl6NkVNTlBJZkNyLTNrOXEtV1dCOEo3OVhoc3JfcGYxRjNJTEYzaFlMa0RtLUZ5eXVlOGIwQkZydlpUbERha29QS09pZnpDNU1YZVBkX2c0OTZNMUs4MFgwY0U4T0xZOW1Xa1Vxclh3U1RrcExfckNZWUpJR2ZvUXViLWRjMnZQU3NTbEdFZVQwbDlBMWg2T3dRbk9Kamg3N3lERzNqcGZVOTlR?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOekRKTzFid2lkem1QXzVxUi0yOEtrdGh0YXNDUEVnOEJqLWRUYmRRbXdmNUZOT1JFcGF2TnhCQVpWeGJ4dVh6UVlnNU9LQmp5bFJtTlpVWnZGMm1zX1dXcUtGTE41Rlg1eGRfSC12YnRyUzNoQVNBaWVwaS1UTV93TF82YjNjbVlyWGRCWUY4V3lfaFBNQ3c?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOTnc5eHpOUkNtNmZUblU2c3BudDZaY3o5WV9CS0RTYll6dm9WWDRhM0xWY0ZkMVhZSDZfRkR4aTNMSDVHYTFnSVZ0NlBCcFpWLTN0dFpqcmFxeHYzLXdnU0hSMWQwemdzN0ZvNlM2UXRsY3J2RDNBaGw3LXlJWUV0Y2VpeVhVOWpzN3ZDNE5BMUU?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPWjFhWkg5UWkwVlNIWlp0QXJhRGp3dk9UdV82V01YSTJpZWdVdU1nZDN3RnZfOXJ3NE5JLTY4VTlfWHlOc21RLXdHMDN5LUdlZXJ2MFltRzZIV3lId2dmVERlM0FpMFpwNEVHc1haOTdIcWFFQ2RnNTNrSktMR2R6d19NR2N6LVRhWUJGeW44QVZWSS1PNHVqUFpRV2RfMjJ3bjd6TlRhTnRTQQ?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxPRmhNV2g2eE44SW5VOGc3Zi00NHIxdE4yYW81LVJoM3lzcDY1Rk5zTTJYRXZFVUgzZEtfZXJzYnppeGhnbndNd2RYUmhRSldHNkl1NDdEeFo5Y3A1cTlzN3AtZU9neG12dHNIdEtiZU9hZUx2TkxYRVpxQzRieUJuWXRsRmRsQ015akwxUzZSSTI1ckJfbkxncjM3U1UxUWJTd3kyeTluODFlY1F5aTdSWHlYVGdXendzbHpILWdjNFFxbzFWQXlGeTlQMUUtRzg4NWRtc9IB2gFBVV95cUxPMFpnblNGQzlEa25xWU0xNTNFLWVLVDlOYjVVZ2c3dkNyY1B5QjNaNm1CalpBSXJFU1FMVDFvaEUyNkFDckxfYjh2bHFuT3pYMjkycmx5N0ZXWVNEWC1vWmZRZ1FwMlk1Q0hlRms4MGZvOVpzdk5pTGdEQ0txc0xYVjBuQVQ3d19MWnozcHBKTHBLLUxtYVAza3pqUWdET05PTnlxRUNzTUhrcWt3M29yU2o0bk9CVm9lY1ZpU1QxY1F0Tm05czhkZHo3MUZ1c0g3bjJhd1ZHUlFvZw?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQRHAwZTFpZ29MVEhlNDA3bTJqaC1FeTIwSEozaFJPNDA0TE8wY0FwalI4MmFlV2ZJSUF4cmhHdHl3S29rSzNnRDk4cEdBcTNxVWl5NHdTS056WVR6ZlVVZTVpNjFKWDFlQkdydk96dTRNdFFEd1dUcE1QV2FaX3Q2LTVJVl9oRGhEQmVSQTc3RzFscTREczJOMF8yUDV6eUpvWnVnQkV2ZEFoN2NFT2J3ZXh2a3E1S3ZteTY4T1o5UXdiWDBPcjQtOG9Ka2ZZa0phUVJYTtIB2gFBVV95cUxNY2xnN0k5QWRYbnp6Rzc4YW9wbE14TElOMDhCQ3o0YWV0Mm9CQ2VfWjVYNTRYeHB6NVF0OGRuOXQ3b2hYT3lqUGtSckU1bkJJWWFDbS1CdklaZkd1Vk8xTUp5TGVOamd6eUpwd1pEWjMwTXJIWUw0blg3eU1SaGF2a3NCdEFralFjMzZCWVZBSXVtbTFrQlByVUl1d3E3eWNJRVQ3Y0tWV21BWUhkbDRxZ3l1UUdCYzAtdVA3ekprUjZZcXI1b0RybUM2THZvVTVjUlNjUllsRnVfUQ?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOd1NlejQ3S3lTcnUyN2JrUm5YcUJxNldEZjQ4RHZFb0tZa1dPY1JwSU8wZzc1Zi0wRVFuSjNlS2NxTWE2b0hQUXVlcy1fNTdENWZPaDJYTTR2QWVFQnQ2eEpTRzJtbm9SV21SSUE1N0VCeFY5QzRmX1o5Mm0yQ1l5RjR4ZWh1d250R1RCMUhPdFp6TGFHcUhNbUIzMTV3MkRWcW1fUnlGME9GUmFTY2xfVzcyaHBuTUswSGdhX3J1Nk8tMGI2ZHfSAcsBQVVfeXFMT01IRERycWtBX1FPYW5mLXIzZVd5aHpPWjQyR2t0Zko5czBfbjFXVVNvMFdYS2hWTERtSWN0NVJyM2NDTDhIRnRLYWRxTzFWMXhwODlTNUUya1k2NGVtVXVlQU1paXo4Tzd4VTl4SVh0UE5mb0VNSjdiVDlBa3htM2xJbTBxX0FBUll6ZkJ2ZklmZHppTXMxSEZOTUpRMHZrSFRqeTVZa3QyMlFzcm51Y3BIQlBwWGJOeEVCQ1FFM0NSdVJLSmhSQ0ptRFk?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxQa1FBd3lLTDU1OE1vQzByRlphSWJZY05HS1ptZGpfZEgyMVJMQlVTMUt3LUVvWjRTYXpIbWUzMEdSN3BqUjJVdjBOb0J4X1ByMHpaZWxrX041NVFRalVPMnNvUXFoOG1qV1k2NXVPc1BubFRLcElDUGROTUdreldNSm5OOHd4anhIaGZKSmU3ZWZGUkc5TmZtWkpad3psdmZLMWRua3pFYTBnUzV0Uy0wUGo4Y2pEcGk0TzBmaWI5am53NENacFJHaGYtdFd3ZE3SAdQBQVVfeXFMT1BUY2dJbXFWeXBrbWIxV3Rlb0o2SWFtRkhYRGx2Y21rc2tGU3l2S1ZmVEpfaW0tb0QyLXdpSFdfdkpKWnU3UjlEMTZ3TkFiT2NRM19CVHlCa2dMRmlrQ2JMQ0tGbVVvYkRiaUpLZDh0UWxpWVlnblhhdTBfeEV4NXdPc1FHQUxZV2dtXzVURWpOcjJIY01jQkxHRUpmZmw0QzlWdk8xb2Z0bkFma3lNOWZySnFzZ2sxMEhhWkxRUlRZV2ZnZHVFeVh4UWx2VnE5el9qOEY?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
