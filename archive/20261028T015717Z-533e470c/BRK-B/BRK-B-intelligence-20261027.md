# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:18:16.569713+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 20, 'rule': 3, 'ai': 15, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'low_uncalibrated_model_confidence': 3, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 20 unique headlines; 5 named publishers; 5 exact duplicates; 20 HTTPS source links; largest publisher share 65.0%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 542.9900 |
| Return 1D (%) | -1.0154 |
| Return 1W (%) | 0.5872 |
| Return 1M (%) | 7.4207 |
| Return YTD (%) | 8.0255 |
| Return 1Y (%) | 11.2525 |
| Annualized volatility (%) | 14.7355 |
| Beta vs SPY | -0.0427 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 0.8002 |
| Downside deviation (rf=0, %) | 10.1716 |
| Sortino (rf=0) | 1.1593 |
| Historical VaR 95% (1D, %) | 1.4122 |
| Historical ES 95% (1D, %) | 2.0016 |
| Correlation vs SPY | -0.0368 |
| Tracking error vs SPY (%) | 19.8046 |
| P/E (trailing) | 13.66 |
| P/B | 0.00 |
| EV/EBITDA | -1.79 |
| Revenue growth (%) | 10.00 |
| Forward P/E (estimate) | 24.21 |
| Gross margin (%) | 30.33 |
| Operating margin (%) | 32.56 |
| Return on equity (%) | 12.12 |
| Free cash flow yield (%) | 6.19 |
| MA50 | 512.6050 |
| Close vs MA50 (%) | 5.9276 |
| MA200 | 495.0549 |
| Close vs MA200 (%) | 9.6828 |
| RSI (14, Wilder) | 68.8076 |
| MACD (12,26) | 10.1680 |
| MACD signal (9) | 7.7229 |
| MACD histogram | 2.4451 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 542.9900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.0154 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.5872 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.4207 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 8.0255 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 11.2525 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 14.7355 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.1716 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1593 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4122 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0016 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0368 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.8046 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0427 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8002 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.2066 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.3320 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.5610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 12.1200 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.1920 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.6567 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 68.8076 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.4451 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.9276 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.6828 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire shares shake the Buffett blues with new all-time highs
- Summary: Berkshire shares shake the Buffett blues with new all-time highs
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTFBDUGVaejRDVUljZ2dXVkZibE43eVJuTlpLUnRlWlpXeERSYlFtd291bEJSdWJKb2NOZ29mY0xEWWE4RHIzVGM1ZkxxempDRTl3Q09wWXpfcGRyS3p6ZkxDRVFSRndXTFBlRVRMVDJqUHJTVDdYVUhldVBJVklnRWPSAYQBQVVfeXFMUFlBMEVBeGdQbnZCdHNhSG9ldTZZai1GOUpIamhNOXBPX3hBTVc4MjZUQmpTZVYyZ1lHcWR6WWpRWS01SDg2cGF5SkNyb3lyMWNkSllkY1I3clVxdVliYWZHQ3hnV2Vka2xiSzdULXZxVWQ1RHpvTDVDSlVPUTZpaFJ4U0pC?oc=5>

### Berkshire Stock Just Hit a Record High. Don’t Back Up the Truck at the Top.
- Summary: Berkshire Stock Just Hit a Record High. Don’t Back Up the Truck at the Top.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNdmhHS1VoTmItZFplR0dLNjQ3bmE3LUNRb3RjRk5tbEE0SWVpcTA2R1duS0FRT0ppc3ZPcVp5OS1WRUhVRFJXeUZSWjBlTzgzZmh4dm5IRVpscW1CbHhPRU1SYVU1a1RMSGhGbUNEQ1gtX3gya0hxSDVpU1NkN0trSkdTZzR0RU8tODRBby1Mdk1hVzluUHh3MFFpdmU?oc=5>

### Buffett’s Berkshire just trounced chip stocks and flashed a rare dot-com-era signal
- Summary: Berkshire outperformed tech stocks, signaling strong market performance.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxOWnVNeFl1TkgzcElCT2x0MElyZ3NLY0lFVEJ2TjF5NlhjU3dya0QxU05GUU5UTzNrRlZTdVgzVUdWeFMtNlhKRTBTUDBoTHhxQngtdWFPSEJuZzkxUThDLVRFRk90am9QNHZIN01EeGRqQTBzN3NUTUhfQnhVRnp6YlI1WEtRUW9RTU5hOHBEWGU1RHgySUxIV2pGamlNaEZ3ZWVMQkFQZklWbDJZaUZnNU9wQzFBbktHTEhDWHM3SVVtWWtHMXJPUXZQWWF1eDcwT0NVdkln?oc=5>

### Berkshire Hathaway B (BRK.B) Increases Despite Market Slip: Here's What You Need to Know
- Summary: Berkshire Hathaway shares rise even as broader market slips, indicating resilience.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQX01PWk9DUFBveTAzMDFDMjFyeEpMNWVHLXgzaGVtRENkRWt4WW0ySkstLWVwaEVQd0tORi00aUhEaFYtQThfYUVzbkJDQW1wNWhFc3ROcEtJU3cyRFlWbThBUnBaMElIM2JiRkhvcXJvbXVXczJvaEFad0p1U1RPMF9FZGlVd09zQmVJZklSeFUtU05UQnc?oc=5>

### Berkshire Hathaway hits all-time high as RSI flashes its most overbought signal since 2024
- Summary: The stock reached a record high, with technical indicators suggesting overbought conditions, reflecting strong market demand.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNeDgteFBsR0dIVEVEbHhwRDNWQkVicmR2VWVNbGNFRDJET0dYU1dsQTA4ZzJSTk9Delk1b3E5ekh0ZXJUMzcxYXBRZFkzLXdKek4xWEJWcGxqYXNaV3JmNVNPMGJfM284UFpZSmFST0I3TVo2N3plSWxfQkJLU0FnR1k1RklNRGwxWTJrb0RvQldaR2NDNk9WeEtkSkcwcjVlNUU3ODUwb0VNTm1YbkRJVXFDNUp6RmVZck9Id1B5MGZUZw?oc=5>

### Berkshire's Financial Flexibility Underpins Long-Term Value Growth
- Summary: Highlights strong financial flexibility supporting long-term value growth.
- Date: 2026-10-27 | Impact: high | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPaEowdmYzSWJjWkt3ZDZLYkpmRFdpcVNNazg1M1VYc25KYUJNbkJCLUxNVG1sVTc4Z0xVYXFvU0JxRzMtLUVzY056R3ByRHJDOWV5Z0pGalVKRVdiUnVmaU03Z1cxNjJqN2pQeDZxWHIxU2VhYkNqZVZqbGwyX011cVZUTHJ5aDF3VDBiSHJRNzFlb2pYa0lOclZmOUZsOWdZWlgzVzVBUFVxSlo1RUZTWFpKdUVOcXpHWWpSTFo5aw?oc=5>

### Berkshire Hathaway Started Buying Back Its Own Stock Again This Year. Should You Buy It at a Record High?
- Summary: Berkshire Hathaway has resumed stock buybacks, signaling confidence and potential share value support.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOX0FmSDUxcTQ1bWV4bS1NVWM5bWdsRGhVZ1pJT0s2aUpYWXpHQnluZ18xRk03WlBVLV9WQ0t1bGY4MTJrRms5UlRzckNaNUF1YUp0YXpxQTB4bVpKdUdoZ3VIQVIwalF5WUQ5azBmQVU3VFVDajh6SWRNcTE3SGFFSUE2eC1UcE8wNENMZzdkWTlCRGg2X3NtQnNSTEhGcVp5LTQ0NnRB?oc=5>

### Berkshire Hathaway Stock Rose 10 Days in a Row in October for the First Time Since 2018. Here's What History Says Comes Next.
- Summary: The stock has achieved a 10‑day consecutive rise, indicating bullish momentum.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOZkFuMWpmT3otRzRPaEpoM0xlaUFNU2Y0cjYyZXYxRVJtZlRKVFl0Z3ZyQXpxdDVCSXp3X3hfZmFRY3NCaHlqVFgzSUNseWdvLXhIQWdyUnFfdlNkb3hqZVFqOTFhb19DdVpPc3lBaVBWdm9LZkhOTks0QkNEcThfSnY5a2hRUTFYdVNlbVQzUHd0OFdHTldXOTFuRXpiUQ?oc=5>

### Warren Buffett's Successor, Greg Abel, Has 32% of Berkshire Hathaway's $364 Billion Portfolio Invested in 3 Unstoppable AI Stocks
- Summary: A significant portion of the portfolio is allocated to AI stocks, reflecting a strategic focus.
- Date: 2026-10-23 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxPb2szY1FfR0FCYlV0N29iSWg5bndSdFdfTWNBazJoSC00Mi16RDFTa3pPaFNSTDU3elBINGRwZEprOHY4VWx0cE82a1BkeEIyZWdFbmFNYnRwWDVkVDN5WnZVcFhpbUJzSlVhYWIzb19mUjBzNkNFbTUxQWtFVjB2U2tNNXNrRVFlSlhGeEpZN29nODRTSmtpR0xub0kwX09QUXlIVXZrQ1NIcjhVWTUtenFBbzNxVFI0TS0ySDlpcVdOVkhJd2I2ZnlENEdrdGZrb1VKX19oTVh3Y3pYYm5sS2diTW12Z09SeEE?oc=5>

## HEADWINDS

### Warren Buffett's Berkshire Stock Flashes Strong Warning
- Summary: Stock issued a strong warning, signaling potential downside risk.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPa1BxSVZNc1FGSHVGeFNsazl3dnBCY2RvbkFmdTdPaF9tUzV1R0xvRGE2WFJPTkVtZ0xuLTR4T3F6cW9TYzRqbWFjcnV3X3ZHbHIyVlVySWZaWENrOFdYZUN6MEJXUmtOdENETFV4OWlNMXoxUjQzOXhuYk1lVTFNbE1kaFV4LWM4Ql9HZGhlVW1LejN4ZTUyT05QM0pCUHk3REVvWlNCbw?oc=5>

### Berkshire Hathaway: Is the Stock Still a Safe Buy Without Warren Buffett?
- Summary: Questions the stock's safety in Buffett's absence.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOLUQ4NkFrUFJ4ZUJKMXd4ZktjTXc5WFUyVUl0UGFnS0x0QUNLM0VhQ08zZnFMT05oa2RNVnk3MDhrMUdoemJCaUJsS0RrMVZRTWRYd3RybUVMNV9yRmc2SklYaGhON2t2d05XQUp6UDBlWlFaenU4MWJ2TE1Cc0FVNDhqaF9KbndLU3JFS3dQNUN1QUozRjJxQWNEREN3NEd2Rm1WcXVZLVVQcktfemlWc21jcmk?oc=5>

### ETFs Are Net Sellers of Berkshire Hathaway (BRK.B) on Oct. 23
- Summary: ETFs sold Berkshire shares, indicating short‑term selling pressure.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNSFlBamNJYld5NmUwa2VCa09WSnVYRG9HVWtxWGpWcEdhNmw4eVF6UkFybnNiaUpFT1p2RGtodmZlZGxleHVESnNlckNGUnJCbnh1dm5GWFFsUWJ5OTRxVkhoSGRpb1dYVFFfT3RMY0NjSjVQOGpYTnlDYVg0QTROVDl1T0tTRDlWUEwwNkJ1czA2V0w3dFMtOVBNZUFwTjVTWmc?oc=5>

### Jim Cramer warns investors against going all-in on Warren Buffett
- Summary: Cramer cautions against overexposure to Berkshire, suggesting potential risk.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNaGlrTFRVeXlYTl9mUFlRVnpELUZKY0dDdDFtMGY1Z2JRRUFWNzAxQU1DTk9HSFVtV0ZtTzlzbmphQl9vX3AwUVl3V2tOaFhHWU1vN1IwRUs2d3ZvTXBsSnV1c081Uzl1TTFILW1MRC1nc19KVVR0bUw0bGhrTk10anJHYzlHUWZvUTYtRWs4aFdic3hxRjE0V2xCLXpuMGVk?oc=5>

## CATALYSTS

### Berkshire Hathaway (BRK.A) After Buffett’s Warning Looks Undervalued On Fair Value Narrative
- Summary: Berkshire Hathaway (BRK.A) After Buffett’s Warning Looks Undervalued On Fair Value Narrative
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQcXdMQ28xZUpSZlVVU2pqalJVcFRoSWtNVXlRSU1DV2EzaUhvYXNURzlMZFRqZnU2X3lJbzFDRWJXR1cya0tpQUlJallDcHc4eUxHT3RZU1BwdVF5NTMxbUNfd0N2ZUY1SkdSV0JTTWtWMWNFTEtzcW80Sm5ra2dXRURYUmdJRXVwT3VicG5VXzI0U2VlSjAxeDV1cVpSQjhjQTBWcWJ3?oc=5>

### Berkshire Hathaway (BRK-B) Starts Spending Its Cash, but Is 24 Times Earnings Fair?
- Summary: Berkshire begins cash outlays, raising questions on valuation and spending strategy.
- Date: 2026-10-21 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQcjBSTEFUWUxMNFBQUmFMME5sWHUzbkdUY0RVNURhSUdLamhVYjVxX3pEd0d6Q0NHOUlJOTZvSEoxYjAxcVdSRnhidDNfa0VzMU5DaVdia0c4ZTMzUWdBc1NWS0hrTVFqdDZfTlBlYTlPeExrdW5ibVdvWGdwUVoxN2NEOENKQjFyMjV3NG9PYUVYR09wOTZGQWJrV3o?oc=5>

### What Could Berkshire Hathaway (BRK.B) Gain From An Early AI Funding Round?
- Summary: Speculation on potential benefits from early AI funding for Berkshire Hathaway.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNZEw2bVhaMGVVc0FlS1RMOEtGWUNjVUMzZEZjeVhNNExOQUxqZThIOGZHNi1QTDVCaFc0OWpvQkF1OFprRWFKVUJTRnFyeS14MVZaZDVMdy1PYU00N01zd1diM3FVRXdaeElHamRwR09BM0NQVWFCVHBtdHk5d2l1aVFzVTlRWHZ1TG1YeEU2cFU0cXFNVzg2NHVB?oc=5>

### Berkshire to Report Q3 Earnings: Time to Buy, Hold or Sell the Stock?
- Summary: Upcoming Q3 earnings report may influence investment decisions.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxNeDcxaXpSVGd2WnktZ0UxaGdOR1c4aHhhZk84Nko1N29JcGNSalo2MVpNSjhycnh2U291azNHMTRucE5seUpBMkkwTXVvaF9PcXI1MjNfWjVUS2w0R2F6M0pzMXRQUzF4RVRsZkt2aGFhRjFpNjZEQXhVazdqUzY0OVJBdU85TXNWbTFRbGg5eFk0Q2pjMUJkOW53ZkxLN3liVTRGODFDbE5Fb0c0NW1lRW43c21pN3JwYmlRUXVUcw?oc=5>

## RISKS

### Can Berkshire Hathaway (BRK.A) Stay Below Fair Value After Its 87% Run?
- Summary: Questioning Berkshire's ability to remain undervalued after a significant share run.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPdGZGVW1tb2VRWENsb0ZQWkJ0a3lWbWc3UzJSa2YtLTRHNTR3bG9STC1KY1RKSFIzRE84Wm5FSFJvdldCN2lkR0w3RXBSXzJuWWhiMmkwZHV4VW5fVkN5M21pRC1qRUxpekdZMmJWeUVQcTFyZW05NHBmZTlmaFZmN2dMMWNLSHhoVXZ5WmxsSFRLWUREaTBhb2c2amd5Snc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **13.66** | **0.00** | **-1.79** | **10.00** | **1,162,383,982,592.00 USD** | **11.25** |
| MKL | 10.24 | 1.21 | 6.45 | 12.70 | 23,028,224,000.00 USD | -1.31 |
| FFH.TO | 8.77 | 1.35 | 7.89 | -0.50 | 55,253,614,592.00 CAD | 7.04 |
| L | 13.61 | 1.19 | 8.08 | 3.90 | 22,695,563,264.00 USD | 11.21 |

Peers fetched as_of: 2026-10-27; BRK-B reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-08
- Next expected earnings: 2026-11-07 (yfinance; expected dates may change)

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
- Filing date: 2026-08-10
- Revenue (latest available single quarter): 101,808,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 25,667,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1067983/000119312526341032/brka-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMif0FVX3lxTFBDUGVaejRDVUljZ2dXVkZibE43eVJuTlpLUnRlWlpXeERSYlFtd291bEJSdWJKb2NOZ29mY0xEWWE4RHIzVGM1ZkxxempDRTl3Q09wWXpfcGRyS3p6ZkxDRVFSRndXTFBlRVRMVDJqUHJTVDdYVUhldVBJVklnRWPSAYQBQVVfeXFMUFlBMEVBeGdQbnZCdHNhSG9ldTZZai1GOUpIamhNOXBPX3hBTVc4MjZUQmpTZVYyZ1lHcWR6WWpRWS01SDg2cGF5SkNyb3lyMWNkSllkY1I3clVxdVliYWZHQ3hnV2Vka2xiSzdULXZxVWQ1RHpvTDVDSlVPUTZpaFJ4U0pC?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNdmhHS1VoTmItZFplR0dLNjQ3bmE3LUNRb3RjRk5tbEE0SWVpcTA2R1duS0FRT0ppc3ZPcVp5OS1WRUhVRFJXeUZSWjBlTzgzZmh4dm5IRVpscW1CbHhPRU1SYVU1a1RMSGhGbUNEQ1gtX3gya0hxSDVpU1NkN0trSkdTZzR0RU8tODRBby1Mdk1hVzluUHh3MFFpdmU?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxOWnVNeFl1TkgzcElCT2x0MElyZ3NLY0lFVEJ2TjF5NlhjU3dya0QxU05GUU5UTzNrRlZTdVgzVUdWeFMtNlhKRTBTUDBoTHhxQngtdWFPSEJuZzkxUThDLVRFRk90am9QNHZIN01EeGRqQTBzN3NUTUhfQnhVRnp6YlI1WEtRUW9RTU5hOHBEWGU1RHgySUxIV2pGamlNaEZ3ZWVMQkFQZklWbDJZaUZnNU9wQzFBbktHTEhDWHM3SVVtWWtHMXJPUXZQWWF1eDcwT0NVdkln?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQX01PWk9DUFBveTAzMDFDMjFyeEpMNWVHLXgzaGVtRENkRWt4WW0ySkstLWVwaEVQd0tORi00aUhEaFYtQThfYUVzbkJDQW1wNWhFc3ROcEtJU3cyRFlWbThBUnBaMElIM2JiRkhvcXJvbXVXczJvaEFad0p1U1RPMF9FZGlVd09zQmVJZklSeFUtU05UQnc?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNeDgteFBsR0dIVEVEbHhwRDNWQkVicmR2VWVNbGNFRDJET0dYU1dsQTA4ZzJSTk9Delk1b3E5ekh0ZXJUMzcxYXBRZFkzLXdKek4xWEJWcGxqYXNaV3JmNVNPMGJfM284UFpZSmFST0I3TVo2N3plSWxfQkJLU0FnR1k1RklNRGwxWTJrb0RvQldaR2NDNk9WeEtkSkcwcjVlNUU3ODUwb0VNTm1YbkRJVXFDNUp6RmVZck9Id1B5MGZUZw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPaEowdmYzSWJjWkt3ZDZLYkpmRFdpcVNNazg1M1VYc25KYUJNbkJCLUxNVG1sVTc4Z0xVYXFvU0JxRzMtLUVzY056R3ByRHJDOWV5Z0pGalVKRVdiUnVmaU03Z1cxNjJqN2pQeDZxWHIxU2VhYkNqZVZqbGwyX011cVZUTHJ5aDF3VDBiSHJRNzFlb2pYa0lOclZmOUZsOWdZWlgzVzVBUFVxSlo1RUZTWFpKdUVOcXpHWWpSTFo5aw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOX0FmSDUxcTQ1bWV4bS1NVWM5bWdsRGhVZ1pJT0s2aUpYWXpHQnluZ18xRk03WlBVLV9WQ0t1bGY4MTJrRms5UlRzckNaNUF1YUp0YXpxQTB4bVpKdUdoZ3VIQVIwalF5WUQ5azBmQVU3VFVDajh6SWRNcTE3SGFFSUE2eC1UcE8wNENMZzdkWTlCRGg2X3NtQnNSTEhGcVp5LTQ0NnRB?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxOa0dobzY5aWRZMU5ZSnB1OVlCazNWYWdtWXJ1ZWRhNFZKV01zVUtPa3ZqNTBBSjNHSmpqWnpKb2UzdnNCTlB3SklYNnlzYUJKRTRQcEVoelFHQmhaQ2hNR2pnbnlhaUpZWWVLdGVPeGJCcWF5aHN3ckQtSlc5LTJjVlFWYnoySG92Q1U3dW9kMC10TnZHWkFXbGI3U3VkMXVwbXB1UGdjWHRRakdvc09idG1vdHp3bjhJQVdPQjJRaW1WT0lLcTJMREViWnZoR3VuQTE3bzNWQU92QkdlMTRN?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOZkFuMWpmT3otRzRPaEpoM0xlaUFNU2Y0cjYyZXYxRVJtZlRKVFl0Z3ZyQXpxdDVCSXp3X3hfZmFRY3NCaHlqVFgzSUNseWdvLXhIQWdyUnFfdlNkb3hqZVFqOTFhb19DdVpPc3lBaVBWdm9LZkhOTks0QkNEcThfSnY5a2hRUTFYdVNlbVQzUHd0OFdHTldXOTFuRXpiUQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQMW9rUmp4RnlObFJ3NWlmVk40d0ZPZ0gzbHlwNG5la1RLZ2xFNENxbXBsamw5dXZnTjd4NjBDanM1WTQtS3pueGNicXhMd3pNN2syRHBUYnJVR0JJc25SVmdHU2kwTWVxbm1WX2c1RDk3RkJWNmVqSFhsQWNsa1QwcGxDNV9lNGpEMUJjQTZnQzZxb28ya2cw?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxPb2szY1FfR0FCYlV0N29iSWg5bndSdFdfTWNBazJoSC00Mi16RDFTa3pPaFNSTDU3elBINGRwZEprOHY4VWx0cE82a1BkeEIyZWdFbmFNYnRwWDVkVDN5WnZVcFhpbUJzSlVhYWIzb19mUjBzNkNFbTUxQWtFVjB2U2tNNXNrRVFlSlhGeEpZN29nODRTSmtpR0xub0kwX09QUXlIVXZrQ1NIcjhVWTUtenFBbzNxVFI0TS0ySDlpcVdOVkhJd2I2ZnlENEdrdGZrb1VKX19oTVh3Y3pYYm5sS2diTW12Z09SeEE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQQ2FVRFAtN1pJYVVKTGNYYTYxajZ0Y3BXT1cyb3VRRkV3TEZtV21WS0VOWDFOMjhabFlMZVA5QVh3MVhzZTNROFM3SlRFQWFibTU1TnBWU3YxLVNSdFZ0UU5jSExwVDh0MHpzNTdDTGNpWHl3Z1Q2azdidnNfZlhJZkpuRGpHS2tBbDczWU5hZjdsSUZITWp5NGNrUTQyZDlo?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPa1BxSVZNc1FGSHVGeFNsazl3dnBCY2RvbkFmdTdPaF9tUzV1R0xvRGE2WFJPTkVtZ0xuLTR4T3F6cW9TYzRqbWFjcnV3X3ZHbHIyVlVySWZaWENrOFdYZUN6MEJXUmtOdENETFV4OWlNMXoxUjQzOXhuYk1lVTFNbE1kaFV4LWM4Ql9HZGhlVW1LejN4ZTUyT05QM0pCUHk3REVvWlNCbw?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOLUQ4NkFrUFJ4ZUJKMXd4ZktjTXc5WFUyVUl0UGFnS0x0QUNLM0VhQ08zZnFMT05oa2RNVnk3MDhrMUdoemJCaUJsS0RrMVZRTWRYd3RybUVMNV9yRmc2SklYaGhON2t2d05XQUp6UDBlWlFaenU4MWJ2TE1Cc0FVNDhqaF9KbndLU3JFS3dQNUN1QUozRjJxQWNEREN3NEd2Rm1WcXVZLVVQcktfemlWc21jcmk?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOb3d2TFVQVlNMSXVKOU5rcWplYlNOdVV5WVdDMWlIQ3pJeXRtZ1RJakpmZTdOMi00aFJKWlcxeXZ6WW8xYk9BV0lxRzJwOUdVaDgyQTZzeHRtblpfRnF5OGpndFN3ZU9pbXpGT1J2WjZDS3NLREhoWXlXcjR1Rk1GVVBxazdsWGpnSVZFZmRFb0NiM01USTZyWDJKUC1TMWlCV1E?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNSFlBamNJYld5NmUwa2VCa09WSnVYRG9HVWtxWGpWcEdhNmw4eVF6UkFybnNiaUpFT1p2RGtodmZlZGxleHVESnNlckNGUnJCbnh1dm5GWFFsUWJ5OTRxVkhoSGRpb1dYVFFfT3RMY0NjSjVQOGpYTnlDYVg0QTROVDl1T0tTRDlWUEwwNkJ1czA2V0w3dFMtOVBNZUFwTjVTWmc?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNaGlrTFRVeXlYTl9mUFlRVnpELUZKY0dDdDFtMGY1Z2JRRUFWNzAxQU1DTk9HSFVtV0ZtTzlzbmphQl9vX3AwUVl3V2tOaFhHWU1vN1IwRUs2d3ZvTXBsSnV1c081Uzl1TTFILW1MRC1nc19KVVR0bUw0bGhrTk10anJHYzlHUWZvUTYtRWs4aFdic3hxRjE0V2xCLXpuMGVk?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQcXdMQ28xZUpSZlVVU2pqalJVcFRoSWtNVXlRSU1DV2EzaUhvYXNURzlMZFRqZnU2X3lJbzFDRWJXR1cya0tpQUlJallDcHc4eUxHT3RZU1BwdVF5NTMxbUNfd0N2ZUY1SkdSV0JTTWtWMWNFTEtzcW80Sm5ra2dXRURYUmdJRXVwT3VicG5VXzI0U2VlSjAxeDV1cVpSQjhjQTBWcWJ3?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQcjBSTEFUWUxMNFBQUmFMME5sWHUzbkdUY0RVNURhSUdLamhVYjVxX3pEd0d6Q0NHOUlJOTZvSEoxYjAxcVdSRnhidDNfa0VzMU5DaVdia0c4ZTMzUWdBc1NWS0hrTVFqdDZfTlBlYTlPeExrdW5ibVdvWGdwUVoxN2NEOENKQjFyMjV3NG9PYUVYR09wOTZGQWJrV3o?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNZEw2bVhaMGVVc0FlS1RMOEtGWUNjVUMzZEZjeVhNNExOQUxqZThIOGZHNi1QTDVCaFc0OWpvQkF1OFprRWFKVUJTRnFyeS14MVZaZDVMdy1PYU00N01zd1diM3FVRXdaeElHamRwR09BM0NQVWFCVHBtdHk5d2l1aVFzVTlRWHZ1TG1YeEU2cFU0cXFNVzg2NHVB?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxNeDcxaXpSVGd2WnktZ0UxaGdOR1c4aHhhZk84Nko1N29JcGNSalo2MVpNSjhycnh2U291azNHMTRucE5seUpBMkkwTXVvaF9PcXI1MjNfWjVUS2w0R2F6M0pzMXRQUzF4RVRsZkt2aGFhRjFpNjZEQXhVazdqUzY0OVJBdU85TXNWbTFRbGg5eFk0Q2pjMUJkOW53ZkxLN3liVTRGODFDbE5Fb0c0NW1lRW43c21pN3JwYmlRUXVUcw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPdGZGVW1tb2VRWENsb0ZQWkJ0a3lWbWc3UzJSa2YtLTRHNTR3bG9STC1KY1RKSFIzRE84Wm5FSFJvdldCN2lkR0w3RXBSXzJuWWhiMmkwZHV4VW5fVkN5M21pRC1qRUxpekdZMmJWeUVQcTFyZW05NHBmZTlmaFZmN2dMMWNLSHhoVXZ5WmxsSFRLWUREaTBhb2c2amd5Snc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
