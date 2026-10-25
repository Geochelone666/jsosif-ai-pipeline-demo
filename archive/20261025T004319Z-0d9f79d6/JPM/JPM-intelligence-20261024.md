# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-10-24**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-10-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-25T01:08:37.638710+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 7, 'ai': 13, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 10 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 44.0%; oldest publication 2026-10-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 331.5800 |
| Return 1D (%) | -1.4738 |
| Return 1W (%) | -2.3961 |
| Return 1M (%) | -1.2727 |
| Return YTD (%) | 4.8868 |
| Return 1Y (%) | 14.7437 |
| Annualized volatility (%) | 22.1025 |
| Beta vs SPY | 0.7373 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.7353 |
| Downside deviation (rf=0, %) | 15.8824 |
| Sortino (rf=0) | 1.0233 |
| Historical VaR 95% (1D, %) | 2.3879 |
| Historical ES 95% (1D, %) | 3.2600 |
| Correlation vs SPY | 0.4252 |
| Tracking error vs SPY (%) | 20.2832 |
| P/E (trailing) | 13.91 |
| P/B | 2.51 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 12.99 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 42.58 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 344.1581 |
| Close vs MA50 (%) | -3.6548 |
| MA200 | 319.7489 |
| Close vs MA200 (%) | 3.7001 |
| RSI (14, Wilder) | 41.9724 |
| MACD (12,26) | -2.2374 |
| MACD signal (9) | -2.9915 |
| MACD histogram | 0.7541 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 331.5800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.4738 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.3961 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -1.2727 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 4.8868 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 14.7437 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.1025 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 15.8824 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.0233 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.3879 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.2600 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4252 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.2832 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7373 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7353 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.9872 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 42.5840 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.9086 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.9724 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7541 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.6548 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.7001 -> Slightly above the moving-average trend level.

## TAILWINDS

### JPMorgan Chase (NYSE:JPM) Steadies as Revenue Climbs Across Core Businesses
- Summary: JPMorgan Chase (NYSE:JPM) Steadies as Revenue Climbs Across Core Businesses
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxOTXNfelQta1pYN2doczR1ei1fZ1Z0WG5wSTZXQjZiQ3NXTVdjSW5mWVJ1NVA1TjdLSUI1cTctZTNqeEptTVdXdTFlQ3FJNU1WOFFkdHZKemF1UlhZRW9GbFJFa3JpWUhvQzVEOUtWYVFIRUlKOVF1MzBmTENZekI3WGJRS3MxSXJRRHhQSEtMOF9RUHFTa3h0Wkk2OFpLdUpwVkpJYkN6YmdDa2poVllSSXlmempGbzg3?oc=5>

### Is JPMorgan Chase Stock a Buy 8% Below Its Record High?
- Summary: Analyst suggests JPM is a good buy at 8% below record high, indicating positive valuation outlook.
- Date: 2026-10-18 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNUlcxT3A3WnVQQlBpazR1U2x5amNybTJNUzZIMmpoUmJwSEZPUHFQbE96OXFIZHdNeFhQaDZuX0tvaXJ2TlRQWTF5aXhhYUVWSkJYNEo2c1BDRGduMElYdV9GUjl1cU5OdTlRcmptMG1aeGZjcEFFbFBGYXBIMldRRXdtdmwtQkRxVHk1VFpBdzdQem5KRGc?oc=5>

### JPMorgan Chase & Co. (JPM) is Attracting Investor Attention: Here is What You Should Know
- Summary: Highlights growing investor interest in JPM, signaling favorable market perception.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQY2t2ejFWbkYzNzV5YTU3aEZiUXFwajBTdEdvYkpMd0Exa3J6X0h1RGJReUlBZTNlRllIWWlNdG02Q2NYZ0puN2xLalFEZkhWbFY3S2ZzOVhRdDNjR01zclEtVmhRQjczX0lZZ1ItZUJrYmRPWTY3Y0RGSmRVejgyUFgzUU1yOXdEVUcxOTMtR2hkTUZYczYwd0wyWjFLUQ?oc=5>

### The Investment Case for JPMorgan Chase & Co. (JPM)
- Summary: Outlines reasons to invest in JPM, reinforcing positive outlook.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPYUllX3Z4Qk9ieWdXVXRIQ1dwTl9wZVktTkFET1o5ZWpGRkFLa0NNQ2lISEJiN2Z4UnFPT0pDRmpxZTMyNWZ1NXpZdkVOZjhUMDNXLVN2dlU1YzRmTXBHdHNpUnRMMUVIYjMxUGVaNFg5MEpQQlFDNFo1MmhaZFRrUllxLVozQmRYc0R1U1BwME5uWjRFR2w3a0pjZm91bUU?oc=5>

## HEADWINDS

### JPMorgan Chase & Co. (NYSE:JPM) Stock Price Down 1.4% - What's Next?
- Summary: JPMorgan Chase & Co. (NYSE:JPM) Stock Price Down 1.4% - What's Next?
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQb3VYMHhoSXpoQ3BLS2RHZkE3Zks1cnBsMnEtUTJESGJfYnVBLTV1ZWJuREJCRHM2TmJVcmFtZGJzZlZZcDFIQW1NdjV0LWVIMTlMdHd3aVFTWDBxOHVZRFhybFU1RzBpcXpUcTZqMXJ5M2JkbGVHejgtOVhjSkotUEktTWtKcG1VbW1vWmF5T1ZfU3NpMnhnRFpfOTFnc0lUYnd2YWNfTEJ3Wko5a0NQNGtlQjhtWTNn?oc=5>

### JPMorgan Chase & Co. $JPM Stock Holdings Cut by Pinnacle Associates Ltd.
- Summary: Pinnacle Associates recommends cutting JPM holdings, indicating negative analyst stance.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxPTkM2bmlrQjZwX2ZHNko4eEhUZGZvTm9CUDNXaWVLdUJOVVRfa1huZVZxRUdmcGRjZzl3ZGtSc0x2Q05zczI5TUpWMGcydVJMbTJYUWR0R2ZtT1hVbHctNlExNlRPVnpFOVZ2RTZHbXhEUTVSUUlWWXI5aHlLXzNEOWpfMkNyX0hTSW9qdVo3clRIZVBBMGFhTnNnY05tQW1qOTUyS0VtSnNxSXRkVzl0WU04QVRla01idlpHLWZ2c1JUQWZNeFVv?oc=5>

## CATALYSTS

### JPMorgan Chase & Co. $JPM Stock: Focused Alpha LLC Increases Position
- Summary: JPMorgan Chase & Co. $JPM Stock: Focused Alpha LLC Increases Position
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQNDRjM3pvVV95enBYUUx3LTBLNG05S195UG91VHZRMUsyUXF4X0RFYjdjNGU3ZTBHRnlxbkl5Z1NybmpqTW5EWVliY25uUWY3aGEwUTRBYnB3eFNsOXZuaHVXTDg3N3RtdThmb2VhY09WNFgtUlFzcTc0LTY0eDMzSWtYbFdHcHhiaHFRYVI0R0JFdEZDeUxwdlVfcGVxT204RzdxLXBTZkRuRE95cTl4UnVJb1NDMWg2d01lSkNTZE81Vms?oc=5>

### JPMorgan Chase & Co. $JPM Stock: Robertson Stephens Wealth Management LLC Raises Holdings
- Summary: JPMorgan Chase & Co. $JPM Stock: Robertson Stephens Wealth Management LLC Raises Holdings
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxOUjdFdDhuSXNsS2FfQ3Z6cVlpNzcwYmVJTEVSQTJvRC1LVnEyWktFSVdheER1SGtNakEzMHhXRnR1eXhFWDhjVURJMklNUXhXM0p6OXRjY2lmbHNwcld3b2ZZQkVCUnlIWE1wQlFwZmRJMXNoMDVHTEYyNGM2Tl9vaHA2djFWZFBzdzFoZUFKQVFpamVFdjBSRUJ4QVR6b1loSDhnemRRS1ZuMGM3U3pOTFBNVElkY0NmWjZRVkhzZUFNMU5tc3hNVlJPTkFiUkwxRTF5RFVZTWRxSGQzbVE?oc=5>

### JPMorgan Chase & Co. $JPM Stock: Birch Hill Investment Advisors LLC Lowers Holdings
- Summary: JPMorgan Chase & Co. $JPM Stock: Birch Hill Investment Advisors LLC Lowers Holdings
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQY1ZJeFRzMlBPdmxlSVZiV3ZxS19sallCZEtBOW1zLTdibGpFU09raENBdlJ6UW1kX2xZZmxreE5LLU1yT21RVUVpSnlUaHJTT0ZvOHZ0bmxJeWdQUTk1VXhaRXNGY3c0b1N4c1N2TEl3UHl1U3hIeVFQZnFBWU1IWGJKTXZwd0lhbVJ6cVF4OExKSEtPU2t4QXFJTGs3dlVBUldPTTd3c3dqVDVaX3RnREtpbVpQTnBUMW1NUlBTVmVtSUlYTk1yc3J0WmdDVHFvWm9yeldB?oc=5>

### JPMorgan Chase & Co. $JPM Stock: BDF Gestion Reduces Holdings
- Summary: JPMorgan Chase & Co. $JPM Stock: BDF Gestion Reduces Holdings
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNWFprSXlPazRSblVDaTI3LWZTNGdoNllMUGhyTGlBVXJmbkt4M2F2UmZIa0FGLTdLVWJaMl80bzZVbExSZEFmVlNUZTVJRm5RVzdwWElBYmJzSXRnVDk1bnAxaDM3Q2p1ODc5N2ZpbEYtQ3hsRmxPRzBZOGJWUmVqTXc0U1dIc2RVVG5YckdwcWNYMUJZMDJUQkJEdnBQdGx4MmdiUklDZkVtVjZ1UkYzSXR0d2syT3Nf?oc=5>

### JPMorgan Chase & Co. $JPM Shares Sold by Courant Investment Management LLC
- Summary: JPMorgan Chase & Co. $JPM Shares Sold by Courant Investment Management LLC
- Date: 2026-10-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxNZnlJLS1ZbTBTWUdBSG5MajZIQlJ6VV85bE00VzE5VkFtcW1faWNSWHVTbUR3M0tMTU5SOWMzeGVRbmdnazR5Uzc2aXNURVFXSDRMck9VbEFoeE5BeXpGbzQwcXdUSzVaQUtSbzJ3cW5TRTJpajZfdHdLM3pfN2l5NW02OF85SG84ejFWc0oxMElUVkIwV1BWckp1MXU5cVdROGFUVktOS2t2OHBBVnlrYVRNODZxeEFRa0ZFQjlObzRNZTBoY3JUbVEtTQ?oc=5>

### JPMorgan Chase & Co. $JPM Stock: Carnegie Investment Counsel Trims Holdings
- Summary: Carnegie Investment Counsel reduced JPM holdings, indicating a change in ownership stakes.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxOeWRoUlFSZEtLTnhOSVNTM214TDlNSVV1ZXdQdFdYb3BJU0lJSnlhMGdtNHdSS3Q1UXpwRmdPREhvWExQZ1Y5QkQweDM0VF81TVduS29IbXZvNnlrekZueWV6UTc0YTlYX0Vtdk9Yam83VmdBc2dwVFdjdTgzR0N5MkM1WHRNdFFjcTdSQ0pCMklhQUV2ZWkyNGNibjhCeTkyVFJ1eldTS2Y3TUhLc1V5bWRVTl9pVm9pYnZTNzA2UjcwSGU0c1R6aDhIaw?oc=5>

### JPMorgan Chase Invests $5 Billion In US National Security Tech
- Summary: JPM invests $5B in U.S. national security technology, expanding its tech portfolio and strengthening defense-related services.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPSWF3eFpEd0RMVXdmMEwzYmJlUnpSMnpsTG1TMm9JbGcyay1qTElldnpVclF3RURab3p2U2pGME9NQ3Z0RFhSSm5ZaTFaVGNfTGJMQnlhN1ZndUR5OEs5ODQ0S3h2aUJDRHhVOXI0djlCZUttMFZKNlNlWDBSS05VMXZiYmM2YkYta3NB?oc=5>

### JPMorgan Chase & Co. $JPM Stock: SteelPeak Wealth LLC Boosts Holdings
- Summary: SteelPeak Wealth LLC increases its JPM holdings, indicating confidence in the bank’s prospects.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQQzY3X29lNl95NmF4Nkw1TjBFWU9HaU5KcWlJQ0RZUlpqNnF3clFCQ3VBWWVkb0Nfa1FSS0ZkeklycmhtQlNQalJBV0I5X0dfYWN1bXhaZEVDN2dyRHdWWm95Y0REOVJsWnREWXhwMUtjZlZZWU0xdGZJOVR0d2lja19QUEk3eGdHRlBjSERNSkQ0S2VHN3VPUVRRdkdmMHFrb1dEOUlLRklYcUpIbXJzVzJ6U1lYdzF5aXFkTG5vT1V4aWc?oc=5>

### JPMorgan Chase (JPM) Stock Looks Cheap Following Its 153% Run
- Summary: JPM stock has surged 153%, prompting analysts to label it undervalued.
- Date: 2026-10-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPVGQ5ejFvb1V4MW5PNU1VdW1IS0lzeUIycmNHRWZrTnFLYl9RSEJYejhrX05lWkNWYk0zVU9NUFlISEVfRHduckdfRHFBMG41REVuUXF2dHZ5a25WSm1JQlduVFhjeVE3QUV0WVp0NlNZMFJOQUV3ZjRZTDY4YVBOSlYtcElMWjk4RXRaR3M5ck1xT1NDQURLOTFoOWt5X2J6UVUwYk9aQlV0Rl9VY195c28ycnl5X0UwMnE1c3FPcjEwZzDSAcgBQVVfeXFMT0tueE85S2ZUTW15VE1UM2V6aTM2N3I1NHdCNjQxckwxSjIxSWhrX3Qyak4zbmp2MVBIUHZSSGdFeHBsQi1YVS10V2RGMDRLeGUxcWFSR3pVWnpPYnlxRFk4YnFpN3JCQnB2eUhtT3BnUmZPREJ0SXJpVnh5SUVpOGViYkdRUFhqa3ZSN0l2azhpWmVBVnlVMF9hWVk4dkxEY3JKOFlFdlBqVHMxWXpCVy1taXpoQ2tNZnY0RjRiTnV5N0xILUVFNmc?oc=5>

### JPMorgan Chase (JPM) Puts JPM Coin on Ethereum for Institutional Payments
- Summary: JPM launches JPM Coin on Ethereum to facilitate institutional payments.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNNzVNbW9MWnd2YV9qRU9pR2NTYzRxMTdzSVJ5Y0Nsc0VmNzVFSXVRYnNIYUVrT3NWa1hDSjZKXzh0TkxtMnlsTFV2VVY4UlZhYnk1aGx1NTE0SWJBRXRCTnNIMXJXUGVGWXRyOG9ZY2R5VTNlUTczVEtVZWFHY0JHUHlHSWRwM2E1SzN1dGtFdkVoRGN5Y2RJU1Q4OTJQS096cVg1T0VYMjR2OVpyV0J1U1kxcUJ0OXRRZEpObWlYMDdIcU5PVEHSAcsBQVVfeXFMUE9WdEFHRlVvQU9qX1VkYndfLUNmM0ViRnh2VzdpU0pCeGhGbmZacFpMT29mUk1sazBOeUc3dHdfc1NQNFlLLVdUX1V1MVVlb1pLY1BwM2FQUEF2OGx1UDgxWmJrenVCTGVrT2NBVXpaelBFbjVJVnk3MVpJT1FfMWJGZzluVFpoVnlxOU5sU3ZRSDktaXZpbVdfNEZfRlJvNTJSb1drTjNqSGVIQ2VkdnhTN2xDdFlLZXdvOUkxZmRXLV9PMkJ2Xy12cDg?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Stock Falls 1.8% - Time to Sell?
- Summary: JPM shares drop 1.8%, raising sell‑side questions.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNenBhTHZxazRybnFQWXZ2dDV3cU1wVHZIblpYcXlRTWFpaGltb3NvSkU3bERuTXl5Qkxyck0ydEZtcmloSjRONXhXMjN2UGlqd05sTHY3cnJWQW9tSklrc0xmS19Nbm9MSUNIZndRam5HN1Fuejhvc1JsY0w2UmJZd19FN3N5TklSaDRFOTViTEtOX19mRzdhVVRGU2lvakx1bWFFQ1lnb0dGTWpFZ3lhQjZZWkY?oc=5>

### Can JPMorgan Chase (NYSE:JPM) Steady Itself as Revenue Climbs Across Businesses?
- Summary: JPM reports rising revenue across its business units, indicating strong performance.
- Date: 2026-10-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxOanp4SE9nLUoweVpsTlRmWWQ5NVFKU2hTWllhOHhxQ1I4TkNESVYyNml2c3JrT0pEMlhzZDZXMmZMRWFXRnphSTBSSDA3NUFwYkEtaHlmUEVMRGc5b2t2NmZYWnBLdG0tWEZTQTE1YS1QdXR2by14SXhQbHZNN3JERTRIUjNMRHlJT3J2Zm9va2x0enhtYjFySWdIblBmRWd2QzE4QUFibGk4VzFLajBLMFpLT21MOVVMYzBmQkR3?oc=5>

## RISKS

### Big U.S. banks are detecting unauthorized AI agents - report (JPM:NYSE)
- Summary: Unauthorized AI agents detected in U.S. banks, posing security risks.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNMldobHZ6WkZYTFI0SFYwLW53WVdDTGE2UVc2UFdLWGtZbkE1blF3Y0hHWXVubkxGeWRTQUF5aGlpVG9JczZKSEc0U0tIVW1tTkZKWjNPTE1DaTU2Rm96djV5NnJkSG1WYTlfaXBnMWQ3TUxlaGZRNVptZ1NpR1ZONnd5Y1dfUi1vZ1BnX0VHd0ZhT1dpNTJndVNZNA?oc=5>

### JPMorgan (NYSE:JPM) Chase Earnings Miss: What the NYSE Composite Reveals
- Summary: JPM's earnings fell short of expectations, raising concerns about profitability.
- Date: 2026-10-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPSVFvd0xnUUtIRzd2NUQ1b0xWbUtMc2szbmdjNnJLUWhtcDlLaEhfOEkyNVlyYjE1NFp0d2V5TWhwR2VCUng4VktLLU9uSm92WGRaWXU2dGs1YXBUVkUyai16SlFRbkl1a1NyZ056cWlXQUdmSmtseXI5eVpza3NmX0gxOFNIQ3d2YUZnUDdWTjFudlJkYndrQjVnU1RRbzZzOGtqNGlzMElENDFCbTdCT25NVGRJdw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **13.91** | **2.51** | **N/A** | **10.20** | **880,543,858,688.00 USD** | **14.74** |
| BAC | 12.07 | 1.29 | N/A | 7.10 | 350,011,490,304.00 USD | -0.24 |
| C | 11.76 | 1.04 | N/A | 8.00 | 199,650,230,272.00 USD | 27.39 |
| WFC | 11.62 | 1.56 | N/A | 0.40 | 247,305,027,584.00 USD | -0.32 |

Peers fetched as_of: 2026-10-24; JPM reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-06
- Revenue (latest available single quarter): 24,246,000,000.00 USD; period 2014-07-01/2014-09-30; fiscal year/reporting period 2014/Q3
- Net income (latest available single quarter): 21,155,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/19617/000162828026054343/jpm-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiuAFBVV95cUxOTXNfelQta1pYN2doczR1ei1fZ1Z0WG5wSTZXQjZiQ3NXTVdjSW5mWVJ1NVA1TjdLSUI1cTctZTNqeEptTVdXdTFlQ3FJNU1WOFFkdHZKemF1UlhZRW9GbFJFa3JpWUhvQzVEOUtWYVFIRUlKOVF1MzBmTENZekI3WGJRS3MxSXJRRHhQSEtMOF9RUHFTa3h0Wkk2OFpLdUpwVkpJYkN6YmdDa2poVllSSXlmempGbzg3?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNUlcxT3A3WnVQQlBpazR1U2x5amNybTJNUzZIMmpoUmJwSEZPUHFQbE96OXFIZHdNeFhQaDZuX0tvaXJ2TlRQWTF5aXhhYUVWSkJYNEo2c1BDRGduMElYdV9GUjl1cU5OdTlRcmptMG1aeGZjcEFFbFBGYXBIMldRRXdtdmwtQkRxVHk1VFpBdzdQem5KRGc?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQY2t2ejFWbkYzNzV5YTU3aEZiUXFwajBTdEdvYkpMd0Exa3J6X0h1RGJReUlBZTNlRllIWWlNdG02Q2NYZ0puN2xLalFEZkhWbFY3S2ZzOVhRdDNjR01zclEtVmhRQjczX0lZZ1ItZUJrYmRPWTY3Y0RGSmRVejgyUFgzUU1yOXdEVUcxOTMtR2hkTUZYczYwd0wyWjFLUQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPYUllX3Z4Qk9ieWdXVXRIQ1dwTl9wZVktTkFET1o5ZWpGRkFLa0NNQ2lISEJiN2Z4UnFPT0pDRmpxZTMyNWZ1NXpZdkVOZjhUMDNXLVN2dlU1YzRmTXBHdHNpUnRMMUVIYjMxUGVaNFg5MEpQQlFDNFo1MmhaZFRrUllxLVozQmRYc0R1U1BwME5uWjRFR2w3a0pjZm91bUU?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQb3VYMHhoSXpoQ3BLS2RHZkE3Zks1cnBsMnEtUTJESGJfYnVBLTV1ZWJuREJCRHM2TmJVcmFtZGJzZlZZcDFIQW1NdjV0LWVIMTlMdHd3aVFTWDBxOHVZRFhybFU1RzBpcXpUcTZqMXJ5M2JkbGVHejgtOVhjSkotUEktTWtKcG1VbW1vWmF5T1ZfU3NpMnhnRFpfOTFnc0lUYnd2YWNfTEJ3Wko5a0NQNGtlQjhtWTNn?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPTkM2bmlrQjZwX2ZHNko4eEhUZGZvTm9CUDNXaWVLdUJOVVRfa1huZVZxRUdmcGRjZzl3ZGtSc0x2Q05zczI5TUpWMGcydVJMbTJYUWR0R2ZtT1hVbHctNlExNlRPVnpFOVZ2RTZHbXhEUTVSUUlWWXI5aHlLXzNEOWpfMkNyX0hTSW9qdVo3clRIZVBBMGFhTnNnY05tQW1qOTUyS0VtSnNxSXRkVzl0WU04QVRla01idlpHLWZ2c1JUQWZNeFVv?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQNDRjM3pvVV95enBYUUx3LTBLNG05S195UG91VHZRMUsyUXF4X0RFYjdjNGU3ZTBHRnlxbkl5Z1NybmpqTW5EWVliY25uUWY3aGEwUTRBYnB3eFNsOXZuaHVXTDg3N3RtdThmb2VhY09WNFgtUlFzcTc0LTY0eDMzSWtYbFdHcHhiaHFRYVI0R0JFdEZDeUxwdlVfcGVxT204RzdxLXBTZkRuRE95cTl4UnVJb1NDMWg2d01lSkNTZE81Vms?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxOUjdFdDhuSXNsS2FfQ3Z6cVlpNzcwYmVJTEVSQTJvRC1LVnEyWktFSVdheER1SGtNakEzMHhXRnR1eXhFWDhjVURJMklNUXhXM0p6OXRjY2lmbHNwcld3b2ZZQkVCUnlIWE1wQlFwZmRJMXNoMDVHTEYyNGM2Tl9vaHA2djFWZFBzdzFoZUFKQVFpamVFdjBSRUJ4QVR6b1loSDhnemRRS1ZuMGM3U3pOTFBNVElkY0NmWjZRVkhzZUFNMU5tc3hNVlJPTkFiUkwxRTF5RFVZTWRxSGQzbVE?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQY1ZJeFRzMlBPdmxlSVZiV3ZxS19sallCZEtBOW1zLTdibGpFU09raENBdlJ6UW1kX2xZZmxreE5LLU1yT21RVUVpSnlUaHJTT0ZvOHZ0bmxJeWdQUTk1VXhaRXNGY3c0b1N4c1N2TEl3UHl1U3hIeVFQZnFBWU1IWGJKTXZwd0lhbVJ6cVF4OExKSEtPU2t4QXFJTGs3dlVBUldPTTd3c3dqVDVaX3RnREtpbVpQTnBUMW1NUlBTVmVtSUlYTk1yc3J0WmdDVHFvWm9yeldB?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNWFprSXlPazRSblVDaTI3LWZTNGdoNllMUGhyTGlBVXJmbkt4M2F2UmZIa0FGLTdLVWJaMl80bzZVbExSZEFmVlNUZTVJRm5RVzdwWElBYmJzSXRnVDk1bnAxaDM3Q2p1ODc5N2ZpbEYtQ3hsRmxPRzBZOGJWUmVqTXc0U1dIc2RVVG5YckdwcWNYMUJZMDJUQkJEdnBQdGx4MmdiUklDZkVtVjZ1UkYzSXR0d2syT3Nf?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxNZnlJLS1ZbTBTWUdBSG5MajZIQlJ6VV85bE00VzE5VkFtcW1faWNSWHVTbUR3M0tMTU5SOWMzeGVRbmdnazR5Uzc2aXNURVFXSDRMck9VbEFoeE5BeXpGbzQwcXdUSzVaQUtSbzJ3cW5TRTJpajZfdHdLM3pfN2l5NW02OF85SG84ejFWc0oxMElUVkIwV1BWckp1MXU5cVdROGFUVktOS2t2OHBBVnlrYVRNODZxeEFRa0ZFQjlObzRNZTBoY3JUbVEtTQ?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxOeWRoUlFSZEtLTnhOSVNTM214TDlNSVV1ZXdQdFdYb3BJU0lJSnlhMGdtNHdSS3Q1UXpwRmdPREhvWExQZ1Y5QkQweDM0VF81TVduS29IbXZvNnlrekZueWV6UTc0YTlYX0Vtdk9Yam83VmdBc2dwVFdjdTgzR0N5MkM1WHRNdFFjcTdSQ0pCMklhQUV2ZWkyNGNibjhCeTkyVFJ1eldTS2Y3TUhLc1V5bWRVTl9pVm9pYnZTNzA2UjcwSGU0c1R6aDhIaw?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPSWF3eFpEd0RMVXdmMEwzYmJlUnpSMnpsTG1TMm9JbGcyay1qTElldnpVclF3RURab3p2U2pGME9NQ3Z0RFhSSm5ZaTFaVGNfTGJMQnlhN1ZndUR5OEs5ODQ0S3h2aUJDRHhVOXI0djlCZUttMFZKNlNlWDBSS05VMXZiYmM2YkYta3NB?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQQzY3X29lNl95NmF4Nkw1TjBFWU9HaU5KcWlJQ0RZUlpqNnF3clFCQ3VBWWVkb0Nfa1FSS0ZkeklycmhtQlNQalJBV0I5X0dfYWN1bXhaZEVDN2dyRHdWWm95Y0REOVJsWnREWXhwMUtjZlZZWU0xdGZJOVR0d2lja19QUEk3eGdHRlBjSERNSkQ0S2VHN3VPUVRRdkdmMHFrb1dEOUlLRklYcUpIbXJzVzJ6U1lYdzF5aXFkTG5vT1V4aWc?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPVGQ5ejFvb1V4MW5PNU1VdW1IS0lzeUIycmNHRWZrTnFLYl9RSEJYejhrX05lWkNWYk0zVU9NUFlISEVfRHduckdfRHFBMG41REVuUXF2dHZ5a25WSm1JQlduVFhjeVE3QUV0WVp0NlNZMFJOQUV3ZjRZTDY4YVBOSlYtcElMWjk4RXRaR3M5ck1xT1NDQURLOTFoOWt5X2J6UVUwYk9aQlV0Rl9VY195c28ycnl5X0UwMnE1c3FPcjEwZzDSAcgBQVVfeXFMT0tueE85S2ZUTW15VE1UM2V6aTM2N3I1NHdCNjQxckwxSjIxSWhrX3Qyak4zbmp2MVBIUHZSSGdFeHBsQi1YVS10V2RGMDRLeGUxcWFSR3pVWnpPYnlxRFk4YnFpN3JCQnB2eUhtT3BnUmZPREJ0SXJpVnh5SUVpOGViYkdRUFhqa3ZSN0l2azhpWmVBVnlVMF9hWVk4dkxEY3JKOFlFdlBqVHMxWXpCVy1taXpoQ2tNZnY0RjRiTnV5N0xILUVFNmc?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNNzVNbW9MWnd2YV9qRU9pR2NTYzRxMTdzSVJ5Y0Nsc0VmNzVFSXVRYnNIYUVrT3NWa1hDSjZKXzh0TkxtMnlsTFV2VVY4UlZhYnk1aGx1NTE0SWJBRXRCTnNIMXJXUGVGWXRyOG9ZY2R5VTNlUTczVEtVZWFHY0JHUHlHSWRwM2E1SzN1dGtFdkVoRGN5Y2RJU1Q4OTJQS096cVg1T0VYMjR2OVpyV0J1U1kxcUJ0OXRRZEpObWlYMDdIcU5PVEHSAcsBQVVfeXFMUE9WdEFHRlVvQU9qX1VkYndfLUNmM0ViRnh2VzdpU0pCeGhGbmZacFpMT29mUk1sazBOeUc3dHdfc1NQNFlLLVdUX1V1MVVlb1pLY1BwM2FQUEF2OGx1UDgxWmJrenVCTGVrT2NBVXpaelBFbjVJVnk3MVpJT1FfMWJGZzluVFpoVnlxOU5sU3ZRSDktaXZpbVdfNEZfRlJvNTJSb1drTjNqSGVIQ2VkdnhTN2xDdFlLZXdvOUkxZmRXLV9PMkJ2Xy12cDg?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNenBhTHZxazRybnFQWXZ2dDV3cU1wVHZIblpYcXlRTWFpaGltb3NvSkU3bERuTXl5Qkxyck0ydEZtcmloSjRONXhXMjN2UGlqd05sTHY3cnJWQW9tSklrc0xmS19Nbm9MSUNIZndRam5HN1Fuejhvc1JsY0w2UmJZd19FN3N5TklSaDRFOTViTEtOX19mRzdhVVRGU2lvakx1bWFFQ1lnb0dGTWpFZ3lhQjZZWkY?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxOanp4SE9nLUoweVpsTlRmWWQ5NVFKU2hTWllhOHhxQ1I4TkNESVYyNml2c3JrT0pEMlhzZDZXMmZMRWFXRnphSTBSSDA3NUFwYkEtaHlmUEVMRGc5b2t2NmZYWnBLdG0tWEZTQTE1YS1QdXR2by14SXhQbHZNN3JERTRIUjNMRHlJT3J2Zm9va2x0enhtYjFySWdIblBmRWd2QzE4QUFibGk4VzFLajBLMFpLT21MOVVMYzBmQkR3?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNMldobHZ6WkZYTFI0SFYwLW53WVdDTGE2UVc2UFdLWGtZbkE1blF3Y0hHWXVubkxGeWRTQUF5aGlpVG9JczZKSEc0U0tIVW1tTkZKWjNPTE1DaTU2Rm96djV5NnJkSG1WYTlfaXBnMWQ3TUxlaGZRNVptZ1NpR1ZONnd5Y1dfUi1vZ1BnX0VHd0ZhT1dpNTJndVNZNA?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPSVFvd0xnUUtIRzd2NUQ1b0xWbUtMc2szbmdjNnJLUWhtcDlLaEhfOEkyNVlyYjE1NFp0d2V5TWhwR2VCUng4VktLLU9uSm92WGRaWXU2dGs1YXBUVkUyai16SlFRbkl1a1NyZ056cWlXQUdmSmtseXI5eVpza3NmX0gxOFNIQ3d2YUZnUDdWTjFudlJkYndrQjVnU1RRbzZzOGtqNGlzMElENDFCbTdCT25NVGRJdw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
