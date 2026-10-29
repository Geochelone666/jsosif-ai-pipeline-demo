# V Intelligence Report

- ticker: **V**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:07:02.043396+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 12, 'ai': 9, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/V** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 400.6000 |
| Return 1D (%) | -0.3135 |
| Return 1W (%) | -1.7776 |
| Return 1M (%) | 8.9357 |
| Return YTD (%) | 14.9113 |
| Return 1Y (%) | 16.4035 |
| Annualized volatility (%) | 22.2490 |
| Beta vs SPY | 0.2747 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 0.7955 |
| Downside deviation (rf=0, %) | 13.9504 |
| Sortino (rf=0) | 1.2687 |
| Historical VaR 95% (1D, %) | 1.7961 |
| Historical ES 95% (1D, %) | 2.6824 |
| Correlation vs SPY | 0.1568 |
| Tracking error vs SPY (%) | 23.8271 |
| P/E (trailing) | 32.62 |
| P/B | 21.23 |
| EV/EBITDA | 24.09 |
| Revenue growth (%) | 14.40 |
| Forward P/E (estimate) | 23.37 |
| Gross margin (%) | 97.72 |
| Operating margin (%) | 66.13 |
| Return on equity (%) | 61.19 |
| Free cash flow yield (%) | 2.71 |
| MA50 | 379.4538 |
| Close vs MA50 (%) | 5.5728 |
| MA200 | 340.5999 |
| Close vs MA200 (%) | 17.6160 |
| RSI (14, Wilder) | 60.9527 |
| MACD (12,26) | 9.2427 |
| MACD signal (9) | 8.8886 |
| MACD histogram | 0.3542 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 400.6000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.3135 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.7776 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 8.9357 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 14.9113 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 16.4035 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.2490 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.9504 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.2687 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7961 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6824 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1568 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.8271 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2747 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.1805 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7955 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.3692 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.7250 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.1310 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 61.1900 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.7131 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 32.6221 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 60.9527 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3542 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.5728 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 17.6160 -> Clearly above the moving-average trend level.

## TAILWINDS

### Visa (V) Stock Could Be Near Fair Value Despite Its 105% Run
- Summary: Visa’s stock may be fairly valued after a 105% run, suggesting a positive valuation outlook.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOUDhOakEyejNzU1M3RXZ3bGdRcGtuckFrTTFmcGk0WGoyb0VxNFpNS1VObGVfQmVPdFVKWC0tcjc0Rk83Z1JNX3lVNnE5R0Q3bDRNdGpFdk9GNHVlbjdWLWtoU2huTGxrNnlhZnFMQ0xaa2owRU9EYlNPbXExclIwbTYxMkFhRWs1cnNNbUgwRW1NUQ?oc=5>

### Visa Q4 profit jumps: can earnings keep pace with the stock?
- Summary: Visa reports higher Q4 profit, raising earnings expectations.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQWTFYMHU5S0UteXB3c1g2UTVKSUI3d2kxQ2Z5cGtpdjZmVWpBZkI1X3NoV25HaWowUmZLMlhFX2pxUzhWT2c1R3RVeEl2cXV2LTNoS19UVHhTd21YY3h2TW5LUVBzS2FlMHJOYVBEZDZqQzVEM2J1QlZMbTgyYVBCbndqV2RJYk4tcDhHcjJJVzR2VjJmUnROeGk1X3R5Rk1UbmFGUWJsbzFwOGYtSENnaC1iT2EtZw?oc=5>

## HEADWINDS

### Visa Stock Inches Lower Despite Revenue Beat
- Summary: Visa Stock Inches Lower Despite Revenue Beat
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOQ0JtM0JOc2NMd2VBVV9JUTJLaDhRVVgwZ2h4d1JXQ3ZrYUFKMEVsamN3Wmk5WlNEamZTWkFtZ1NJQWtLTkdkeUJNVGY4aWdaT0ZWdHF3ZkU2U2VzdWtQd1Uzb1pselhZRGc3eEl5ZzN5WGtYY1hxUUlnV1FLRGdhYm4wTkt6MjhDdmhWOEJTYjhFT2NaY1NUdUQwdjA?oc=5>

### Visa Q4 earnings beat, revenue in line as payments volume growth ticks slightly lower (V:NYSE)
- Summary: Visa Q4 earnings beat, revenue in line as payments volume growth ticks slightly lower (V:NYSE)
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPeUZJR2FrYThtRXdfYnhJUjdwRGxSTnFvTV9WbC1VTnpZTXZzNzhNVTlFZUNrSFpSekE5QVZsdEI4c1BhVU5SQk1wbHBMQ0dDYVpRdUFYMngzY2JPdnVUSEhPeG9Jb3FNRm83cWdqeWhnLWtMMjRSQk1PTHFxNEJDYmJORldjRnBoajdEZ05aX2gxTGxLUzRGQUJ1czA2d25FSkFuYmoxLWJLNWJ0ZnVBT1FpOEV5ZHBVUHp1cWpWMA?oc=5>

### Visa Inc. (V) Stock Falls on Q4 2026 Earnings
- Summary: Visa Inc. (V) Stock Falls on Q4 2026 Earnings
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPM3pjdm8wb1FCMzlDT0VLdHpBZklsNUItVWxjbl9XU3dxbnhxNFBNeGVmUEotc01pb0J6dHpvZ05TM1VrXzlENWh2SG9qR0U0cTA3Rjk4SGxUTG0yQnU0aTJ2RGJqWC1ZWEM3a1Voa3cwcC1xNmE4eExOZEgzM1l4MWZKSXpXN3MxWnc?oc=5>

### V Stock Falls Below $400 Despite Visa Reporting Higher Fourth-Quarter Profit
- Summary: Visa shares dip below $400 despite better Q4 earnings.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPLUx5OGJFTk1CWlVSeFFqR2wtRUVKczNrZ0x1ZmxxaFFyRGN6bDB3WXhlWlZTWVlMaHZWSV9aVmZFZlBIMW1LbzN5enBxX3pYMFA5aGp6bW1ySkZMVEI5QkhQckFyMTR3cHpwcllHZ05zZXhESllJRVR3VTRacnZVU3ZhUFNFa05NSlBVLXZpdUV2SzRSZTJNQ3dNMzBtUlpOUGFKYk5TX01kcGp6cWFUQWVfQWRRYWFHQ1E?oc=5>

### V Stock Falls Below $400 on £5 Billion UK Card-Fee Claims Ahead of Visa Earnings and Stablecoin Update
- Summary: Visa shares dip below $400 amid £5B UK card‑fee lawsuit claims, affecting earnings outlook and stablecoin plans.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxOOW43VXBqZHY4SDI0OHpJckw2eW1mdEJJajBSOFdXOVJuNExoSi1kTlhVNi1kUFp5bGFLNzhob19Id1VWZEJXUHJGWDM5b2szUGdMM1hKQV9mM1pCamFlaWZUTVo3Qm5fZl9rTU1FYjlVanBrOVEtSjc4RXExaXBfNmJKVDlHd05BZjJncXRWdzRwci1TR2xucXBuODNXUGptWWZYckJKQjg5cldla0c3T3VXRUVnSmYyYmFOdkxDWEg5VHZuMDE1b1pLWkpqVUQydmRISHhMVlpOUEk?oc=5>

## CATALYSTS

### Visa posts record revenue and boosts shareholder returns
- Summary: Visa posts record revenue and boosts shareholder returns
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxNRjB4TnVIcVRCcy1FMEhWeWlMS3pUX09QTUo1dDFYNTJLRDR5U2lWc2hRdWpJbDFxdDVUNnVVN0ZOTDNtUWNNQ0NsSlRSNVBCTzJxUXlVUkYzWXM4Z3NUZEVQTFBzVmhwYXc0TzFjSWFGdWZpT2NYTWpJVHdtSE1PTHVDVUNqbjUtYUhqY2MzeVpCY3kyblVqWFFoTURZd3pydmpuek9jSjVfWjB5enlySmFER1NRNGE4SjF1akNoeXVQN3ZiN1ZNd3hMQ2RGb0xwZ0pYQ25Xaw?oc=5>

### Visa (V) Q3 earnings: what to expect
- Summary: Visa (V) Q3 earnings: what to expect
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPSXlJZkxLSEdaS2dtZXJyNkpfWDdnZHpKYzlUUGlka05SWXROTi1GMEFJYjloQTVrZ3NNc18yOEtqdndoeURRckREazhsLVlOVDNya3JtTFZVbFhPZklsZGFhMDM3cnRTam40VElqdVJuNUFRUDFhazJCMm1BWjNmNXI0R3Z3VWFYWDFrTUlwRHhjd3FG?oc=5>

### Visa Analysts Increase Their Forecasts Following Upbeat Q3 Earnings
- Summary: Visa Analysts Increase Their Forecasts Following Upbeat Q3 Earnings
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxQc0ZkNEd0YS1TNTlpbEdpQUpDUlBQbWl4d2NmWml2YjJyeURtNXFOOGZSTFBTZ2RCNFVHaUIwbl8yS3ZJMDBjUVdBM1VnSUxXdmhxS1dldi1lVFE4b290Q01CbFBMN3JJU2NJTm1oamwxTVA5a0tabk55aGVkc0tCdVZwTkhNNzNFZkNCVXd5dWtmRmN6a2FHWWhCRVR4XzBMbzFLQ0U4SHRQcUNicTJOVnQxdVp3a0NaVVFrcTdMVmIwNmZrTDYzYlk5TWk5TDNCSF9pQlRFQ1p3UQ?oc=5>

### Visa Inc. 2026 Q4 - Results - Earnings Call Presentation (NYSE:V) 2026-10-27
- Summary: Visa Inc. 2026 Q4 - Results - Earnings Call Presentation (NYSE:V) 2026-10-27
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxONDJSaWYzUGp0S3R3V083N2R0OEw5S0VOQ3NKQ0tUNUp4U2lhZ0VXOTViZmF4NXdZS1ZLOHZNSXJScVFCT0RUZy0zVURSZXp5NnFKbGR3bVo2dTBQTklYRUt3eTZMZWJmd0l3Xy0xTm1IRHlBTFhDVVRObG5mZU5ZUGlUM3J2Q2plUU54ZEJNVVVvc1JHRE53?oc=5>

### Visa’s (NYSE:V) Q3 CY2026 earnings results: revenue in line with expectations
- Summary: Visa’s (NYSE:V) Q3 CY2026 earnings results: revenue in line with expectations
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxPbHBsVkd0WjdRQ0NsUU04NDBJeFg3MkJRLXdnUWxLZDdjYjdRXzd5dnFkdTQ4NUVGU0NzSVBPSFpDMmtzTVBlQzRQalFjS1FTZGJUaHVvaUZGTmNzU1UtTVRBVDNRMUpXNW5LVmdfdlpTc2ZjVnFPZ3V5ZGIzX0VLQ3NCOHdDcVlKMVpCSU1Sal9kT1FOS1EzMFZfRy1XY2ptRkMtR2VvMVh0SWZSRkdDMWE1bjFoejF4a0s2aXBnbm1PeUt5UXJCTVNQTDhtOERy?oc=5>

### Visa Reports Strong Q4 Earnings: 'A Milestone Year' CEO Says - Visa (NYSE:V)
- Summary: Visa Reports Strong Q4 Earnings: 'A Milestone Year' CEO Says - Visa (NYSE:V)
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxPQ2dfdlYxSGQtYXVTdW01NVh1alhHbkVYcElLWG0tN2dlbkt6VmZlc2t3ZEt5VGJzY0tUQWJCa1RIckFLXzd5am94MnJzNk1teUs4VURjRjZ3c29JRGpQSTE2UG1uV05rZW5YdEZKMHZRbGtvamNxX01rZ1BmZFFDaUU4WmlaZXBnNGxpQk1sQm9oT1p0TUc5djBIbTVTYzh1YS1qSEtpTWt3aUZyaXdYTnFiZkg?oc=5>

### VISA ($V) Releases Q4 2026 Earnings
- Summary: VISA ($V) Releases Q4 2026 Earnings
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE9kRWVJZnRyc2hQM3U1LXIxaGhzcFFJQzdlcEdiYlZkQlhvQkxtM2VvYUZIM3M1T1JQbFR6X19uZFhVeXhMaVdVYjR1UUZTeDE4VTVlVUJjaGw0U2w4b3dsS2NWbndpWG1DeFdUcTdaTEtaYzlQR1pLLUdaS29NSEU?oc=5>

### Visa Inc. $V Stock: Norris Perne & French LLP MI Raises Stake
- Summary: Visa Inc. $V Stock: Norris Perne & French LLP MI Raises Stake
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNWjNjcXo3RlZwY0hXY0dscmtRVEF0cnpnYjQ3MnpWWHVfeldOc1pyWlJjOWI3NmlPdHpnbEV1bllILXFHc0lQSWNLS29IYngwd1NyQnVtSnhtOGRtMEEtYlp2WlZfaTRxcXlLMkdhdEEzalMzZ3NPWHlsVVpSc0cwaUtJRXFzdXpZaGlmcW55T2RWb0Q0cGxxN2JzeDRZYjBKUVlrZ000am1vNXZkNGhOeGdWeTFNbDRQ?oc=5>

### Ahead of Visa Earnings, Here's What Barchart Data Says Comes Next for V Stock
- Summary: Upcoming earnings release expected to influence V stock direction.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPVDRYY0luc2lVWF9UMW1NMFRNQmNHMEU5QXRrQ0RvaDVlbkJNUTFCUWpRdExncWlobndYNnUyNTBGYlVoaENBM1FtZTVkOGwzaDFCamttNVdjbXhJeWZwZjNsci1Rd2JKbEstLVE1ZzNoOExfQWlUWmxuRk1nejVseFVfcUp1c1lWTXFHZl8zcllrblh0N1JNWFZKUXZuYXdRQk1XcXM3QW5Sd1pSN3JvbGNJaGgzVE9haWJHdA?oc=5>

### Visa (V) Unveils New Commercial Payment Tools, Is The Stock Fully Valued?
- Summary: Launch of new commercial payment tools could drive growth, acting as a catalyst.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOaWNFWnd6Ny1vamNxdmVnTjNSajlwUldaQ0JyOFpFZFFmbzZabUVKbmZUWmwwSDVCdXd2YnVxRXg4SUctZzBUZmVKcVhnaWpYekdPT05QZXFYSTBBNUtBODV4a2JPTGNpMG1kdnpxZERVYWpaU0tWYWJjajBrR19GRXp2c3plRzBxb3R3aGNtTFZsWWdseG9VSDl6b1Ytak0?oc=5>

### Visa, Mastercard earnings on deck: Check for value-added services growth, guidance (V:NYSE)
- Summary: Earnings announcement may reveal growth in value-added services.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQY2hpTFJZcENkUmVxXzZ5aXJWMXVfb1ZQTlBsbU1mRFJJNklkT0M2b2cwRTVrWW9YOW9jSmVabVYzUXBnMnZ4SWhaaUUyNURNcHJMN1BPeVBtdi1TLS1GN0V0cmJhSEFDMzJyd013NGtROG5zOWZlb29JY3NxQk82OGpyWmZrWjlDOW5UNU9pV3B2c3Nhd0RaWEtESXRndk5RYlJNNEV3OXRuWnktUXRTMkgwSWoxUzcw?oc=5>

### Visa Stock Outlook: 3 Key Things Investors Must Watch Before Q4 Earnings
- Summary: Key factors to monitor before Q4 earnings release.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiWEFVX3lxTFBjTzBDZWpzV3lkZHp5Umk0cG5ZVFFaclZ5RFdMb2g2ZEpmTlZjelVXU25mVlJpdm1qVzJrYjktajMzU0dSRHpJXzEyZFpaVkt4QnlTVjJjTW0?oc=5>

## RISKS

### Visa (V) Faces £5 Billion UK Lawsuit Over Card Fees
- Summary: Visa (V) Faces £5 Billion UK Lawsuit Over Card Fees
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNYzY1dlNmOUp5UVBwUno0aV9nUmNzYzFNSl9aX3V3VmJrU0FYa1hmOXZud0Z2MEVod3VSZC1xWmhKT0lFcFhlekF5VTFmb1VtR1VxM0sxdW1USVpVMWxIWjJndW1zY0ZGb3dHdEpWLWtsX0R4MENOdFVUV3J4cWk4c3J4NS1CRDdBbjVWMFpaZmVNLVBiYUhBMUgwRi1Yckg1WE84M3plNUFveXhaM0VXdDJ1NktqTHJVbnVYZtIBwgFBVV95cUxNOVI0Mk5qakgzU29HcldXcXhwa21qcXVubFlxZzFtZ3RvRmVNSGxQWFV3TDRYdExWLU1ha2o1YS1QZ25zMG8tUFNNUkRxRXY5c1lWRFpDWTdLZG1Ya0VmSmpCN28tWmZkQURoa25scExoa1BxY2NSXzVzd1EtNk1MaldBM0hHczkzbDZrS05vd1p2YXVCUEJSZXBsaXQyd0hpM1l1dmkwdWFwb0k4bzdfckpoOE9QckdDeVNjYXlfZDZUUQ?oc=5>

### What Drives Visa’s (V) Long-Term Compounding Potential?
- Summary: Factors affecting Visa's long-term growth prospects.
- Date: 2026-10-26 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNaFQ4YmdZOVBMM09WS1pCQ0NybnNPSlM1QXFKVUJaWHJxbmFHVDRVYjNDQ2g1Ty13OXhPUTFLYUhCa0dZRmpybkwtRXJpbndZSkswLThha2tVRDJOc3FLYWQ2ZHlpbFVLS1FjMkpiXzFOM1BLYzh3T08xN01sRTJWUEdhZk9QN3I2bGM1LUVKN2RRQQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **V** | **32.62** | **21.23** | **24.09** | **14.40** | **752,068,526,080.00 USD** | **16.40** |
| MA | 33.57 | 95.42 | 24.67 | 14.10 | 534,637,608,960.00 USD | 8.54 |
| PYPL | 10.79 | 2.57 | 7.87 | 2.00 | 47,332,347,904.00 USD | -21.69 |
| AXP | 17.62 | 5.96 | N/A | 11.30 | 213,195,309,056.00 USD | -10.94 |

Peers fetched as_of: 2026-10-28; V reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-29
- Revenue (latest available single quarter): 5,840,000,000.00 USD; period 2019-04-01/2019-06-30; fiscal year/reporting period 2019/Q3
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/1403161/000140316126000104/v-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikgFBVV95cUxOUDhOakEyejNzU1M3RXZ3bGdRcGtuckFrTTFmcGk0WGoyb0VxNFpNS1VObGVfQmVPdFVKWC0tcjc0Rk83Z1JNX3lVNnE5R0Q3bDRNdGpFdk9GNHVlbjdWLWtoU2huTGxrNnlhZnFMQ0xaa2owRU9EYlNPbXExclIwbTYxMkFhRWs1cnNNbUgwRW1NUQ?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQWTFYMHU5S0UteXB3c1g2UTVKSUI3d2kxQ2Z5cGtpdjZmVWpBZkI1X3NoV25HaWowUmZLMlhFX2pxUzhWT2c1R3RVeEl2cXV2LTNoS19UVHhTd21YY3h2TW5LUVBzS2FlMHJOYVBEZDZqQzVEM2J1QlZMbTgyYVBCbndqV2RJYk4tcDhHcjJJVzR2VjJmUnROeGk1X3R5Rk1UbmFGUWJsbzFwOGYtSENnaC1iT2EtZw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOQ0JtM0JOc2NMd2VBVV9JUTJLaDhRVVgwZ2h4d1JXQ3ZrYUFKMEVsamN3Wmk5WlNEamZTWkFtZ1NJQWtLTkdkeUJNVGY4aWdaT0ZWdHF3ZkU2U2VzdWtQd1Uzb1pselhZRGc3eEl5ZzN5WGtYY1hxUUlnV1FLRGdhYm4wTkt6MjhDdmhWOEJTYjhFT2NaY1NUdUQwdjA?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPeUZJR2FrYThtRXdfYnhJUjdwRGxSTnFvTV9WbC1VTnpZTXZzNzhNVTlFZUNrSFpSekE5QVZsdEI4c1BhVU5SQk1wbHBMQ0dDYVpRdUFYMngzY2JPdnVUSEhPeG9Jb3FNRm83cWdqeWhnLWtMMjRSQk1PTHFxNEJDYmJORldjRnBoajdEZ05aX2gxTGxLUzRGQUJ1czA2d25FSkFuYmoxLWJLNWJ0ZnVBT1FpOEV5ZHBVUHp1cWpWMA?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPM3pjdm8wb1FCMzlDT0VLdHpBZklsNUItVWxjbl9XU3dxbnhxNFBNeGVmUEotc01pb0J6dHpvZ05TM1VrXzlENWh2SG9qR0U0cTA3Rjk4SGxUTG0yQnU0aTJ2RGJqWC1ZWEM3a1Voa3cwcC1xNmE4eExOZEgzM1l4MWZKSXpXN3MxWnc?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPLUx5OGJFTk1CWlVSeFFqR2wtRUVKczNrZ0x1ZmxxaFFyRGN6bDB3WXhlWlZTWVlMaHZWSV9aVmZFZlBIMW1LbzN5enBxX3pYMFA5aGp6bW1ySkZMVEI5QkhQckFyMTR3cHpwcllHZ05zZXhESllJRVR3VTRacnZVU3ZhUFNFa05NSlBVLXZpdUV2SzRSZTJNQ3dNMzBtUlpOUGFKYk5TX01kcGp6cWFUQWVfQWRRYWFHQ1E?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxOOW43VXBqZHY4SDI0OHpJckw2eW1mdEJJajBSOFdXOVJuNExoSi1kTlhVNi1kUFp5bGFLNzhob19Id1VWZEJXUHJGWDM5b2szUGdMM1hKQV9mM1pCamFlaWZUTVo3Qm5fZl9rTU1FYjlVanBrOVEtSjc4RXExaXBfNmJKVDlHd05BZjJncXRWdzRwci1TR2xucXBuODNXUGptWWZYckJKQjg5cldla0c3T3VXRUVnSmYyYmFOdkxDWEg5VHZuMDE1b1pLWkpqVUQydmRISHhMVlpOUEk?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxNRjB4TnVIcVRCcy1FMEhWeWlMS3pUX09QTUo1dDFYNTJLRDR5U2lWc2hRdWpJbDFxdDVUNnVVN0ZOTDNtUWNNQ0NsSlRSNVBCTzJxUXlVUkYzWXM4Z3NUZEVQTFBzVmhwYXc0TzFjSWFGdWZpT2NYTWpJVHdtSE1PTHVDVUNqbjUtYUhqY2MzeVpCY3kyblVqWFFoTURZd3pydmpuek9jSjVfWjB5enlySmFER1NRNGE4SjF1akNoeXVQN3ZiN1ZNd3hMQ2RGb0xwZ0pYQ25Xaw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPSXlJZkxLSEdaS2dtZXJyNkpfWDdnZHpKYzlUUGlka05SWXROTi1GMEFJYjloQTVrZ3NNc18yOEtqdndoeURRckREazhsLVlOVDNya3JtTFZVbFhPZklsZGFhMDM3cnRTam40VElqdVJuNUFRUDFhazJCMm1BWjNmNXI0R3Z3VWFYWDFrTUlwRHhjd3FG?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxQc0ZkNEd0YS1TNTlpbEdpQUpDUlBQbWl4d2NmWml2YjJyeURtNXFOOGZSTFBTZ2RCNFVHaUIwbl8yS3ZJMDBjUVdBM1VnSUxXdmhxS1dldi1lVFE4b290Q01CbFBMN3JJU2NJTm1oamwxTVA5a0tabk55aGVkc0tCdVZwTkhNNzNFZkNCVXd5dWtmRmN6a2FHWWhCRVR4XzBMbzFLQ0U4SHRQcUNicTJOVnQxdVp3a0NaVVFrcTdMVmIwNmZrTDYzYlk5TWk5TDNCSF9pQlRFQ1p3UQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxONDJSaWYzUGp0S3R3V083N2R0OEw5S0VOQ3NKQ0tUNUp4U2lhZ0VXOTViZmF4NXdZS1ZLOHZNSXJScVFCT0RUZy0zVURSZXp5NnFKbGR3bVo2dTBQTklYRUt3eTZMZWJmd0l3Xy0xTm1IRHlBTFhDVVRObG5mZU5ZUGlUM3J2Q2plUU54ZEJNVVVvc1JHRE53?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxPbHBsVkd0WjdRQ0NsUU04NDBJeFg3MkJRLXdnUWxLZDdjYjdRXzd5dnFkdTQ4NUVGU0NzSVBPSFpDMmtzTVBlQzRQalFjS1FTZGJUaHVvaUZGTmNzU1UtTVRBVDNRMUpXNW5LVmdfdlpTc2ZjVnFPZ3V5ZGIzX0VLQ3NCOHdDcVlKMVpCSU1Sal9kT1FOS1EzMFZfRy1XY2ptRkMtR2VvMVh0SWZSRkdDMWE1bjFoejF4a0s2aXBnbm1PeUt5UXJCTVNQTDhtOERy?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxPQ2dfdlYxSGQtYXVTdW01NVh1alhHbkVYcElLWG0tN2dlbkt6VmZlc2t3ZEt5VGJzY0tUQWJCa1RIckFLXzd5am94MnJzNk1teUs4VURjRjZ3c29JRGpQSTE2UG1uV05rZW5YdEZKMHZRbGtvamNxX01rZ1BmZFFDaUU4WmlaZXBnNGxpQk1sQm9oT1p0TUc5djBIbTVTYzh1YS1qSEtpTWt3aUZyaXdYTnFiZkg?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE9kRWVJZnRyc2hQM3U1LXIxaGhzcFFJQzdlcEdiYlZkQlhvQkxtM2VvYUZIM3M1T1JQbFR6X19uZFhVeXhMaVdVYjR1UUZTeDE4VTVlVUJjaGw0U2w4b3dsS2NWbndpWG1DeFdUcTdaTEtaYzlQR1pLLUdaS29NSEU?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNWjNjcXo3RlZwY0hXY0dscmtRVEF0cnpnYjQ3MnpWWHVfeldOc1pyWlJjOWI3NmlPdHpnbEV1bllILXFHc0lQSWNLS29IYngwd1NyQnVtSnhtOGRtMEEtYlp2WlZfaTRxcXlLMkdhdEEzalMzZ3NPWHlsVVpSc0cwaUtJRXFzdXpZaGlmcW55T2RWb0Q0cGxxN2JzeDRZYjBKUVlrZ000am1vNXZkNGhOeGdWeTFNbDRQ?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPVDRYY0luc2lVWF9UMW1NMFRNQmNHMEU5QXRrQ0RvaDVlbkJNUTFCUWpRdExncWlobndYNnUyNTBGYlVoaENBM1FtZTVkOGwzaDFCamttNVdjbXhJeWZwZjNsci1Rd2JKbEstLVE1ZzNoOExfQWlUWmxuRk1nejVseFVfcUp1c1lWTXFHZl8zcllrblh0N1JNWFZKUXZuYXdRQk1XcXM3QW5Sd1pSN3JvbGNJaGgzVE9haWJHdA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOaWNFWnd6Ny1vamNxdmVnTjNSajlwUldaQ0JyOFpFZFFmbzZabUVKbmZUWmwwSDVCdXd2YnVxRXg4SUctZzBUZmVKcVhnaWpYekdPT05QZXFYSTBBNUtBODV4a2JPTGNpMG1kdnpxZERVYWpaU0tWYWJjajBrR19GRXp2c3plRzBxb3R3aGNtTFZsWWdseG9VSDl6b1Ytak0?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQY2hpTFJZcENkUmVxXzZ5aXJWMXVfb1ZQTlBsbU1mRFJJNklkT0M2b2cwRTVrWW9YOW9jSmVabVYzUXBnMnZ4SWhaaUUyNURNcHJMN1BPeVBtdi1TLS1GN0V0cmJhSEFDMzJyd013NGtROG5zOWZlb29JY3NxQk82OGpyWmZrWjlDOW5UNU9pV3B2c3Nhd0RaWEtESXRndk5RYlJNNEV3OXRuWnktUXRTMkgwSWoxUzcw?oc=5
- https://news.google.com/rss/articles/CBMiWEFVX3lxTFBjTzBDZWpzV3lkZHp5Umk0cG5ZVFFaclZ5RFdMb2g2ZEpmTlZjelVXU25mVlJpdm1qVzJrYjktajMzU0dSRHpJXzEyZFpaVkt4QnlTVjJjTW0?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNYzY1dlNmOUp5UVBwUno0aV9nUmNzYzFNSl9aX3V3VmJrU0FYa1hmOXZud0Z2MEVod3VSZC1xWmhKT0lFcFhlekF5VTFmb1VtR1VxM0sxdW1USVpVMWxIWjJndW1zY0ZGb3dHdEpWLWtsX0R4MENOdFVUV3J4cWk4c3J4NS1CRDdBbjVWMFpaZmVNLVBiYUhBMUgwRi1Yckg1WE84M3plNUFveXhaM0VXdDJ1NktqTHJVbnVYZtIBwgFBVV95cUxNOVI0Mk5qakgzU29HcldXcXhwa21qcXVubFlxZzFtZ3RvRmVNSGxQWFV3TDRYdExWLU1ha2o1YS1QZ25zMG8tUFNNUkRxRXY5c1lWRFpDWTdLZG1Ya0VmSmpCN28tWmZkQURoa25scExoa1BxY2NSXzVzd1EtNk1MaldBM0hHczkzbDZrS05vd1p2YXVCUEJSZXBsaXQyd0hpM1l1dmkwdWFwb0k4bzdfckpoOE9QckdDeVNjYXlfZDZUUQ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNaFQ4YmdZOVBMM09WS1pCQ0NybnNPSlM1QXFKVUJaWHJxbmFHVDRVYjNDQ2g1Ty13OXhPUTFLYUhCa0dZRmpybkwtRXJpbndZSkswLThha2tVRDJOc3FLYWQ2ZHlpbFVLS1FjMkpiXzFOM1BLYzh3T08xN01sRTJWUEdhZk9QN3I2bGM1LUVKN2RRQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
