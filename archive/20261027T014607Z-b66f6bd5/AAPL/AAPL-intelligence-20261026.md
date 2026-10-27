# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T02:12:54.981874+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 8, 'ai': 11, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261026T005504Z-6368ad31/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 36.0%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 343.9100 |
| Return 1D (%) | -1.0986 |
| Return 1W (%) | 0.2828 |
| Return 1M (%) | 0.8327 |
| Return YTD (%) | 26.8470 |
| Return 1Y (%) | 31.3372 |
| Annualized volatility (%) | 24.0180 |
| Beta vs SPY | 0.5575 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.1702 |
| Downside deviation (rf=0, %) | 16.6376 |
| Sortino (rf=0) | 1.6893 |
| Historical VaR 95% (1D, %) | 2.0102 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.2952 |
| Tracking error vs SPY (%) | 23.6274 |
| P/E (trailing) | 39.44 |
| P/B | 46.73 |
| EV/EBITDA | 30.01 |
| Revenue growth (%) | 16.40 |
| Forward P/E (estimate) | 35.97 |
| Gross margin (%) | 48.65 |
| Operating margin (%) | 32.62 |
| Return on equity (%) | 148.75 |
| Free cash flow yield (%) | 2.15 |
| MA50 | 330.2264 |
| Close vs MA50 (%) | 4.1437 |
| MA200 | 294.5359 |
| Close vs MA200 (%) | 16.7634 |
| RSI (14, Wilder) | 57.6982 |
| MACD (12,26) | 4.1596 |
| MACD signal (9) | 4.0802 |
| MACD histogram | 0.0794 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 343.9100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.0986 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.2828 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.8327 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 26.8470 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 31.3372 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.0180 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.6376 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6893 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0102 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2952 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.6274 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5575 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1702 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 35.9665 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.6530 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.6230 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 148.7510 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.1462 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.4392 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.6982 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0794 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.1437 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 16.7634 -> Clearly above the moving-average trend level.

## TAILWINDS

### Apple Stock News (Oct 23, 2026): AAPL Rises 1.2% to $348.22
- Summary: Apple Stock News (Oct 23, 2026): AAPL Rises 1.2% to $348.22
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE1US2xsMlQyUnlub2N4LU5OemNPUTlYaEo4Yjdralc4TWdXU3dsckFsekpDbnNGT3luMGozQU1pQk1hRXNMUjFSVjNmTzZzaUI5WmxDc1ZBTHJQbXAxMXdBU2w1SktSZmNDZnI4c29VMWtjdk5PWDBqOTN6cVMxQQ?oc=5>

### Apple tops Nvidia to become world's most valuable company (AAPL:NASDAQ)
- Summary: Apple surpasses Nvidia, becoming the world's most valuable company, boosting investor confidence and market perception.
- Date: 2026-10-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQXy1LUVY5N2YyajY5UkU5TFllTjZEV21qLWZXUkxiWW9VNGE3LXNFMWhuMFhDVXhHSkwyNVN4OFQxNVdLLWxFaTlrbDl4WW9NeE9yS2VvaUxrMHNyYklERGF2Q2NKLUpjaDQzYlpBMjlja3pHR01ac0hsaHYtb0I3SENoVmNPNVYtM3FvZ0NNZFhBMVlYQldBRld3?oc=5>

### Apple Inc. (AAPL) is Attracting Investor Attention: Here is What You Should Know
- Summary: Investors are focusing on Apple, indicating potential interest in future growth.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPMThESjliM3d5eVFiN2Y5X2FjWWNUZGRpWklILWJDVkQ2S056OWVjcGRHOS1nQ3ptSDNqMGlxRGNaVncxMU9QMkVRTk9kNUdoMnMyMEZPOFhUWkw0RlRDU3c3dlY2YllrOWJFTVdpSThkVmozWWlsR1NkSGlDNWNhSkFhb2JDYXJUUnFZUWNGQU41Wkt1OURVV0U2bUpGMl9z?oc=5>

### Apple (AAPL) Earnings Expected to Grow: Should You Buy?
- Summary: Analysts forecast rising earnings, suggesting a positive outlook for Apple.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPNkZWUzFDVnV6dnJSNWxJZzQwWm94bFpsa1lGaXpXR3RGQktsN0JzaVMxZUVkTk56Z0M0cG9KTHFFa2w4QVg0dVF3RjRVYjFNams2NTJreTJsTlNQd1hEMkQxMVBMZ2lxVUxzMV9FZHRnd2oyVlc1eFlUMWdtWFdyamk3Zy14ZzBneFRvSE01YmpiSXFjSXNGTTQybEFFeUE?oc=5>

### Apple expands Siri AI languages from Portuguese to Japanese (AAPL:NASDAQ)
- Summary: Apple adds Japanese to Siri’s language support, expanding its AI capabilities.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQSzJxNGstbU5Fck55X2FMSmViZF9DdTRDSnJINVVVNXhxcnNkc2I5VEcwSEJnWWVqZ2JoZ0pFNVpyci01NkJYOFVjZkZZLVNrTlRZVk1kQzhQRUxXcWFnOFVqN1NVNnhLMC0xcl81dGZWeDRTLW40RHNteVBYbVpkU0tydWhuV0UzS0ZwNWd6S0d0QVFfV1Q2cVRodG5HZw?oc=5>

### ETFs Are Buying Apple (AAPL) on Oct. 22
- Summary: Institutional ETFs increased Apple holdings, indicating bullish sentiment.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPcGhBbXFDNENiSHRTT2pUOVBuemMxMDZDYzFuR0NQMkJEM0NpYnNDc2tyRjFNMm1LZGp0cTk5aTdMUl91ajd6bTMyMGlKaFRxSk5lNzV6R0NNREhpaEZjeG5yTDNva1NmZGxRemh1ZmFMeHllc2xtb244aFpCTlNMTkczM1JRRURlZDhGS05zTFBTSEgydGc?oc=5>

### Apple Joins Nvidia in the $5 Trillion Club. Here's Which Stock I Think Can Get to $10 Trillion First.
- Summary: Apple’s market cap reaches $5T, boosting its valuation narrative.
- Date: 2026-10-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNQnZzVWVvN1ZJT19fTTlZQ1o3M1ZuNmZDcHZ0NGpRR3ZGUjBvNXJESjdFMXQ0OFNkZzdTd0Y4UGlocTdjNmU5VHZUbTBNa0JJa3VZVUZsOXVhMUt4LU1XWjlZUGE3bVM2MVpYMDJyTktvVHcyQmxVRE9KSWR4UGJaTGhBbUt4TEcwc2JzY2JJSQ?oc=5>

## HEADWINDS

### Apple (AAPL) Stock Falls Amid Market Uptick: What Investors Need to Know
- Summary: Apple (AAPL) Stock Falls Amid Market Uptick: What Investors Need to Know
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPRm40OVVmVmxpU3Z1alRpUDV2U2wtYmk2enZKQmlkdTNWd0NWbXVvenNremt5RmRodVgtak5JdHdlVUZXQUkxdDRna1dNSDJROEhqWlJvQ0phMTUxcVVJUGxnNFNrSXFvMzBmTGhQWjdfVnAzOGNnYlJGTFFNSk5FTFhpcVQyRy1VdHlPMVB6SDI3QnBUYUFN?oc=5>

### AAPL Stock Heads For Worst Single-Day Fall In Over A Year — Wall Street Warns Apple’s AI Supply Chain Headwinds Are Far From Over
- Summary: AAPL Stock Heads For Worst Single-Day Fall In Over A Year — Wall Street Warns Apple’s AI Supply Chain Headwinds Are Far From Over
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxQM0NVeHRMVUhYQzcxTHE1RWR4c1BlOXZLa3VxYjZSNmhYci1ZamtvNGRDalktNlhmM1kwOE5IMmZUR05hWXMtb2lEUnN3S1BZNFE4c2s5emM4NGVnMlRXaFpQWm52S3haY191RW1KSEVwUGNJVTJEVmk1cnZhQmV1eE9VM1MwLXQ2c2pqeC1wZ1YyYnFMUmg2MFZ3Ri1aU21jN3F2aTI1S0ZhYTIzOGJXVDdxNzdBZ2FBc2JTOG9zMFZUMWJRbjdlWTYyWVRDMDlnUDVsN3hIOXNyM3lKaEQ4?oc=5>

### Apple Stock Downgraded As Analysts Turn Cautious On iPhone Maker
- Summary: Apple Stock Downgraded As Analysts Turn Cautious On iPhone Maker
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOSzNXYWVVQlFPQUdlNE03Q3FDenFiVUNQTlB4M1RmX05pRzJwQXVrX0ZwUmRMZncxY1hqOWpHUHVmUzFva1cyb3A3bGN6OWZQMW01N2JvLTR6SzN3UTFBdFlES1dIMnpBOWNuZnZ1Y2NMSEFhVW9VQ29VOXc1TzBWRnJhZjBXT0xoWGcxb1hhbGxfSHhyUW1VbmVHZkRSdmVVMWI0Yi1XM0R3SDQ?oc=5>

### Apple Gives iPad Mini ‘Its Biggest Update Ever’ at a Higher Price; AAPL Stock Falls
- Summary: New iPad Mini update raises price, causing a short-term stock decline.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNR2E5OWRWNVlUc0xjZWtzTmJrLWYxc3FUWjJTQnhvRFJMazJ1aTRmeGpaWUpYZmJnY1ZDbjl2NURRenZLTUE4SThJbVBkbG9hbmdOdGdCd0JZaUdvX3lhaGVqcTVlZ3dKUGc1R214X0ZhVlZOUklvOVYzeDVfNHE2MjRBM3BHeThUMGYyU05fNzBsYTQ2WTlZNl9XNjVMa1UwMlR4X1UzNEpoN0VMT0VJ?oc=5>

## CATALYSTS

### Apple (NASDAQ:AAPL) Stock Hits Record US$351.73 as iPhone Duo Production Target Reportedly Jumps 44%
- Summary: Apple (NASDAQ:AAPL) Stock Hits Record US$351.73 as iPhone Duo Production Target Reportedly Jumps 44%
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiekFVX3lxTE42YWZvT3p4TXJERy1HVHRZTTROeWlHWURrY3VnV25CTFpFcTJ4dndMSXR3b3owTW9rTy14eXFTLXNFOGtaV2h3MzFKaFYwMkpJWWV4WnpLaG1iTjI0U0ZMYmtnNTRvUEZIZnhfbnZ3Y01aeHBaUmNlSGJn?oc=5>

### Apple Stock Hits Record High On iPhone Duo Launch
- Summary: Apple Stock Hits Record High On iPhone Duo Launch
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNdUltNURaQjNjcmctdzRVNGdxX3ZWbmE0ejVOc0c3aXFjQVUzVC14VURDMGRKQzViUzFQdlV1Z3hOQy1sZTJNdkVrWDFxOC0zSXlTalJyQW1TbVdhYVRQRFU3UmxCREFPdWlHbzRxOEg3T1BRMTh5cGxPRk00d3VualFvbnhhOEFaYkIwVTRsRUtNRlZobjdz?oc=5>

### Apple's iPhone Duo: Management Listened To The Innovation Critics (NASDAQ:AAPL)
- Summary: Apple's iPhone Duo: Management Listened To The Innovation Critics (NASDAQ:AAPL)
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPUG5NM01uN3RIWHlIZkwyTTUzbF9rYjhvOXpMeF9LLU5vSENwYWdta2dfZ2pVdTJCQ0ZSc2RYaEtrLTJuOTFNbFozbjF4NEJ1THpGUEJ0YXVMcE1mZW54bHVfNi1SUDB1VnpEakNZODNRcWl0WkM2bmZpei1GRTg2Z2hDamJtMDhPTEFFdUxTS0Fwa09FMTVRcVFIQy1FZGpqNmZqXzVyOA?oc=5>

### Apple launches new iPad mini with OLED display, A20 pro chip (AAPL:NASDAQ)
- Summary: Apple launches new iPad mini with OLED display, A20 pro chip (AAPL:NASDAQ)
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNQzMxZlhCTDN5dGFKOWJDQzN3dEdQNk15UjRQLUFmUEVYVG9sYm1UbDlQMUc3bnVXWHJocDlneHlWdzUwUEVHcUZsNDNkeEZld0ZCSEtwbVdZbE5IOEZNTjNpWjFPbXJoRTNXR3JXSk81OGpFNXdmd3oxNU9GbFJ3WWxGcS1vbVRkVGgyMXYtYUU3ZUl1a0lxLU1rN2xxZw?oc=5>

### Will Apple (AAPL) Change Macs With Its First Touchscreen MacBook Pro?
- Summary: Speculation that Apple may introduce a touchscreen MacBook Pro, potentially expanding its product line.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxObUJBZXJ6TTZfbDg4S0IxTnhqOHRsSlc0QjczUGlrMkZxYWFMWExrTHBrN1hxQXI1STNNX0lyZmwwN3FqaUI1Zm5iQUNsbGJnYlFQN1NGSEkxdFk0ZS1BOHN6akZVVXNEMEk3R2ZrT2VLR3RHODhVQjVqR3ZCVGpBT0FqeVVrTWFoMThkQkp6R3FmVnFpRVk3Ng?oc=5>

### How much Apple stock does former CEO Tim Cook actually own?
- Summary: Details on Tim Cook’s current Apple share ownership, indicating personal investment level.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxQd1Q5cm02a01vTUpTUGtWY1NhZG5KZ05jZm82US1FUmlLOE5qT2s5SEYwbU9ORF9FOVQxUGJFejJXZ2NvSUo2VkxTSENXR0xUYVlDd1NZWWVmOVEwTjQtd1RZRmxnZ08wWWZ5Y19vSVBoY0V6c202Yk9xRVF1MElzRVQ4UWFmaXplZ0wwZDFR?oc=5>

## RISKS

### Apple Stock Price Forecast: AAPL Continues Pullback After Record High, Will It Test $300 Again This Year?
- Summary: Forecast predicts continued pullback from record high, questioning $300 target, indicating potential downside pressure.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQYy16c1hoRlNmSWUyZ2FGNV92azg2ckFMLVp4RXdsRG9OSGE0WGVMdHJXZGlLZjNQcWNWQm9mZm9uRE84b0RpM0I4X2o1X0pTQzR0WnpwcTlSR1JHVmhrRng3d21vX0V0ZkJsYTl3dWtnLXhqaTBlS1hVTnp4TFV2dW1EYWg3OGpwQUROMm5Md3BqOEFhbnBpa0owNDF5QkpmVV9TdDdDa1NpdW5rdWlPNzI5eFJMakVWU0RLV3pqQndpQ1k?oc=5>

### Why Buying Apple Stock Before Q4 Earnings Could Be Risky
- Summary: Investors warned that buying Apple stock before Q4 earnings may expose them to volatility and potential downside, suggesting caution.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOSmRTRXU1S3VTbjVrSVhnMktzbEJDWF9CejhyMktuWXRESEY4b2I4TzlSc0s1V1ZxUWJPVndlNnd5TXR6RlR1Q2xtOFc3aGltSmF4S05LRUVBdWNJWEhzTXIxZkNzUHRSLXFPUWpPMUJrQWc2Szk3YUota2IzWERpYjU0dVVvNk85S3h4RGQwM2RRMDVB?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **39.44** | **46.73** | **30.01** | **16.40** | **5,019,084,521,472.00 USD** | **31.34** |
| MSFT | 29.67 | 8.94 | 20.63 | 17.70 | 3,954,845,417,472.00 USD | 2.55 |
| GOOGL | 15.90 | 6.22 | 21.78 | 24.20 | 3,874,443,231,232.00 USD | 22.20 |
| SONY | 21.51 | 2.89 | 0.12 | 8.20 | 152,011,194,368.00 USD | -9.14 |

Peers fetched as_of: 2026-10-26; AAPL reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-30
- Next expected earnings: 2026-11-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-31
- Revenue (latest available single quarter): 62,900,000,000.00 USD; period 2018-07-01/2018-09-29; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 29,789,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/320193/000032019326000020/aapl-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMifkFVX3lxTE1US2xsMlQyUnlub2N4LU5OemNPUTlYaEo4Yjdralc4TWdXU3dsckFsekpDbnNGT3luMGozQU1pQk1hRXNMUjFSVjNmTzZzaUI5WmxDc1ZBTHJQbXAxMXdBU2w1SktSZmNDZnI4c29VMWtjdk5PWDBqOTN6cVMxQQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQXy1LUVY5N2YyajY5UkU5TFllTjZEV21qLWZXUkxiWW9VNGE3LXNFMWhuMFhDVXhHSkwyNVN4OFQxNVdLLWxFaTlrbDl4WW9NeE9yS2VvaUxrMHNyYklERGF2Q2NKLUpjaDQzYlpBMjlja3pHR01ac0hsaHYtb0I3SENoVmNPNVYtM3FvZ0NNZFhBMVlYQldBRld3?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPMThESjliM3d5eVFiN2Y5X2FjWWNUZGRpWklILWJDVkQ2S056OWVjcGRHOS1nQ3ptSDNqMGlxRGNaVncxMU9QMkVRTk9kNUdoMnMyMEZPOFhUWkw0RlRDU3c3dlY2YllrOWJFTVdpSThkVmozWWlsR1NkSGlDNWNhSkFhb2JDYXJUUnFZUWNGQU41Wkt1OURVV0U2bUpGMl9z?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPNkZWUzFDVnV6dnJSNWxJZzQwWm94bFpsa1lGaXpXR3RGQktsN0JzaVMxZUVkTk56Z0M0cG9KTHFFa2w4QVg0dVF3RjRVYjFNams2NTJreTJsTlNQd1hEMkQxMVBMZ2lxVUxzMV9FZHRnd2oyVlc1eFlUMWdtWFdyamk3Zy14ZzBneFRvSE01YmpiSXFjSXNGTTQybEFFeUE?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQSzJxNGstbU5Fck55X2FMSmViZF9DdTRDSnJINVVVNXhxcnNkc2I5VEcwSEJnWWVqZ2JoZ0pFNVpyci01NkJYOFVjZkZZLVNrTlRZVk1kQzhQRUxXcWFnOFVqN1NVNnhLMC0xcl81dGZWeDRTLW40RHNteVBYbVpkU0tydWhuV0UzS0ZwNWd6S0d0QVFfV1Q2cVRodG5HZw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPcGhBbXFDNENiSHRTT2pUOVBuemMxMDZDYzFuR0NQMkJEM0NpYnNDc2tyRjFNMm1LZGp0cTk5aTdMUl91ajd6bTMyMGlKaFRxSk5lNzV6R0NNREhpaEZjeG5yTDNva1NmZGxRemh1ZmFMeHllc2xtb244aFpCTlNMTkczM1JRRURlZDhGS05zTFBTSEgydGc?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNQnZzVWVvN1ZJT19fTTlZQ1o3M1ZuNmZDcHZ0NGpRR3ZGUjBvNXJESjdFMXQ0OFNkZzdTd0Y4UGlocTdjNmU5VHZUbTBNa0JJa3VZVUZsOXVhMUt4LU1XWjlZUGE3bVM2MVpYMDJyTktvVHcyQmxVRE9KSWR4UGJaTGhBbUt4TEcwc2JzY2JJSQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPRm40OVVmVmxpU3Z1alRpUDV2U2wtYmk2enZKQmlkdTNWd0NWbXVvenNremt5RmRodVgtak5JdHdlVUZXQUkxdDRna1dNSDJROEhqWlJvQ0phMTUxcVVJUGxnNFNrSXFvMzBmTGhQWjdfVnAzOGNnYlJGTFFNSk5FTFhpcVQyRy1VdHlPMVB6SDI3QnBUYUFN?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxQM0NVeHRMVUhYQzcxTHE1RWR4c1BlOXZLa3VxYjZSNmhYci1ZamtvNGRDalktNlhmM1kwOE5IMmZUR05hWXMtb2lEUnN3S1BZNFE4c2s5emM4NGVnMlRXaFpQWm52S3haY191RW1KSEVwUGNJVTJEVmk1cnZhQmV1eE9VM1MwLXQ2c2pqeC1wZ1YyYnFMUmg2MFZ3Ri1aU21jN3F2aTI1S0ZhYTIzOGJXVDdxNzdBZ2FBc2JTOG9zMFZUMWJRbjdlWTYyWVRDMDlnUDVsN3hIOXNyM3lKaEQ4?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOSzNXYWVVQlFPQUdlNE03Q3FDenFiVUNQTlB4M1RmX05pRzJwQXVrX0ZwUmRMZncxY1hqOWpHUHVmUzFva1cyb3A3bGN6OWZQMW01N2JvLTR6SzN3UTFBdFlES1dIMnpBOWNuZnZ1Y2NMSEFhVW9VQ29VOXc1TzBWRnJhZjBXT0xoWGcxb1hhbGxfSHhyUW1VbmVHZkRSdmVVMWI0Yi1XM0R3SDQ?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNR2E5OWRWNVlUc0xjZWtzTmJrLWYxc3FUWjJTQnhvRFJMazJ1aTRmeGpaWUpYZmJnY1ZDbjl2NURRenZLTUE4SThJbVBkbG9hbmdOdGdCd0JZaUdvX3lhaGVqcTVlZ3dKUGc1R214X0ZhVlZOUklvOVYzeDVfNHE2MjRBM3BHeThUMGYyU05fNzBsYTQ2WTlZNl9XNjVMa1UwMlR4X1UzNEpoN0VMT0VJ?oc=5
- https://news.google.com/rss/articles/CBMiekFVX3lxTE42YWZvT3p4TXJERy1HVHRZTTROeWlHWURrY3VnV25CTFpFcTJ4dndMSXR3b3owTW9rTy14eXFTLXNFOGtaV2h3MzFKaFYwMkpJWWV4WnpLaG1iTjI0U0ZMYmtnNTRvUEZIZnhfbnZ3Y01aeHBaUmNlSGJn?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNdUltNURaQjNjcmctdzRVNGdxX3ZWbmE0ejVOc0c3aXFjQVUzVC14VURDMGRKQzViUzFQdlV1Z3hOQy1sZTJNdkVrWDFxOC0zSXlTalJyQW1TbVdhYVRQRFU3UmxCREFPdWlHbzRxOEg3T1BRMTh5cGxPRk00d3VualFvbnhhOEFaYkIwVTRsRUtNRlZobjdz?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPUG5NM01uN3RIWHlIZkwyTTUzbF9rYjhvOXpMeF9LLU5vSENwYWdta2dfZ2pVdTJCQ0ZSc2RYaEtrLTJuOTFNbFozbjF4NEJ1THpGUEJ0YXVMcE1mZW54bHVfNi1SUDB1VnpEakNZODNRcWl0WkM2bmZpei1GRTg2Z2hDamJtMDhPTEFFdUxTS0Fwa09FMTVRcVFIQy1FZGpqNmZqXzVyOA?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNQzMxZlhCTDN5dGFKOWJDQzN3dEdQNk15UjRQLUFmUEVYVG9sYm1UbDlQMUc3bnVXWHJocDlneHlWdzUwUEVHcUZsNDNkeEZld0ZCSEtwbVdZbE5IOEZNTjNpWjFPbXJoRTNXR3JXSk81OGpFNXdmd3oxNU9GbFJ3WWxGcS1vbVRkVGgyMXYtYUU3ZUl1a0lxLU1rN2xxZw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxObUJBZXJ6TTZfbDg4S0IxTnhqOHRsSlc0QjczUGlrMkZxYWFMWExrTHBrN1hxQXI1STNNX0lyZmwwN3FqaUI1Zm5iQUNsbGJnYlFQN1NGSEkxdFk0ZS1BOHN6akZVVXNEMEk3R2ZrT2VLR3RHODhVQjVqR3ZCVGpBT0FqeVVrTWFoMThkQkp6R3FmVnFpRVk3Ng?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxQd1Q5cm02a01vTUpTUGtWY1NhZG5KZ05jZm82US1FUmlLOE5qT2s5SEYwbU9ORF9FOVQxUGJFejJXZ2NvSUo2VkxTSENXR0xUYVlDd1NZWWVmOVEwTjQtd1RZRmxnZ08wWWZ5Y19vSVBoY0V6c202Yk9xRVF1MElzRVQ4UWFmaXplZ0wwZDFR?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQYy16c1hoRlNmSWUyZ2FGNV92azg2ckFMLVp4RXdsRG9OSGE0WGVMdHJXZGlLZjNQcWNWQm9mZm9uRE84b0RpM0I4X2o1X0pTQzR0WnpwcTlSR1JHVmhrRng3d21vX0V0ZkJsYTl3dWtnLXhqaTBlS1hVTnp4TFV2dW1EYWg3OGpwQUROMm5Md3BqOEFhbnBpa0owNDF5QkpmVV9TdDdDa1NpdW5rdWlPNzI5eFJMakVWU0RLV3pqQndpQ1k?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOSmRTRXU1S3VTbjVrSVhnMktzbEJDWF9CejhyMktuWXRESEY4b2I4TzlSc0s1V1ZxUWJPVndlNnd5TXR6RlR1Q2xtOFc3aGltSmF4S05LRUVBdWNJWEhzTXIxZkNzUHRSLXFPUWpPMUJrQWc2Szk3YUota2IzWERpYjU0dVVvNk85S3h4RGQwM2RRMDVB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
