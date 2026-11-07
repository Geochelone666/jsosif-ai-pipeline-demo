# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-11-06**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-11-06**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-07T04:49:47.311966+00:00**
- AI status: **Partial: 1 headline remains unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 7, 'ai': 9, 'unknown': 1, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261106T045829Z-1db1e5a7/JPM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 13 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-10-30

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 334.4900 |
| Return 1D (%) | -0.8448 |
| Return 1W (%) | -0.7566 |
| Return 1M (%) | 0.9690 |
| Return YTD (%) | 5.8073 |
| Return 1Y (%) | 8.7781 |
| Annualized volatility (%) | 22.9145 |
| Beta vs SPY | 0.8025 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.4832 |
| Downside deviation (rf=0, %) | 16.5689 |
| Sortino (rf=0) | 0.6682 |
| Historical VaR 95% (1D, %) | 2.4515 |
| Historical ES 95% (1D, %) | 3.3955 |
| Correlation vs SPY | 0.4746 |
| Tracking error vs SPY (%) | 20.3465 |
| P/E (trailing) | 14.03 |
| P/B | 2.53 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 13.08 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 42.58 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 340.9329 |
| Close vs MA50 (%) | -1.8898 |
| MA200 | 321.2749 |
| Close vs MA200 (%) | 4.1133 |
| RSI (14, Wilder) | 46.7380 |
| MACD (12,26) | 0.3554 |
| MACD signal (9) | -0.2542 |
| MACD histogram | 0.6096 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 334.4900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.8448 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.7566 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.9690 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 5.8073 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 8.7781 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.9145 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.5689 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6682 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4515 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3955 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4746 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.3465 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8025 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4832 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.0798 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 42.5840 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.0306 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 46.7380 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6096 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -1.8898 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 4.1133 -> Slightly above the moving-average trend level.

## TAILWINDS

### JPMorgan Chase & Co (JPM) Stock Up 4.2% but GF Value Says Overva
- Summary: JPMorgan Chase & Co (JPM) Stock Up 4.2% but GF Value Says Overva
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOMWlKWkdVQmZ1LVJjRXR2Ym15OC01UEM3ckd0TldqeXIxbE9feHRkOUh2TzhEekFCd18xbWV1bzVsMmQxOGJhc3pFWkZManJOdkQ0ZXNwdWNFMnJWYzdUY0NoQm9rTFJhR1lFMFdxRHdsaUZVbm9GRW5LV09TREpPQlJ4TXRKMVBhZjhuRFZTQ0VTWjBYc2dSWFQ3VWpGdmtyMzNfMXBrT2dzZWYxNVVVYmNrSnhGc1E?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Stock Price Up 1.1% After Analyst Upgrade
- Summary: JPMorgan Chase & Co. (NYSE:JPM) Stock Price Up 1.1% After Analyst Upgrade
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPeVBaeVl2dlVyRlhuVTlZWVVkaHJZU284ZzFTYWh5TUo3cU14MHVNYm5YUHFNZFNFd1Btejl6Tl93VEhvYlk1QWktMmdLRzdnNTBkdTF3RzdiQVRxWUxwaHpfcUthT3FhVi1zMjB1TV81OWRXbUVKSnFJUWZ5bjdUTUc5RnhzR2x1Nlc5WkROaVhFc3hLVE12MmpKRkh1Vi0wRjFkb19TQ09WTzNTV3JlQ2FMTkpSZmdEU2doZUNtNTkxZVRa?oc=5>

### JPM Stock Technicals: Gains 4.18% on Wednesday, Testing Key Resistance
- Summary: JPM Stock Technicals: Gains 4.18% on Wednesday, Testing Key Resistance
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNOTlQcmpncGV4YmlFV0I3MVhXVkdwUE9HN0RIeUVJblBpdjRqR2RaM3hseGo3enA4U2R2VU9BcXNEZ2RXN25WdTZlXzZONWFhenhCLTNyZkluTlFwY1ZkQXY1TmdUX0Y3Ui1ZMkc5RllFcUV2Vm5oXzRPOHdFV1NFemRneThkSnpkc1gxWFhWcXFZcXNBdHZCdkIzNzB1WVVKRzUxMVhZZEpEUQ?oc=5>

### JPMorgan Chase (JPM) Draws Fresh ETF Buying, Is The Stock Still Undervalued?
- Summary: ETF buying indicates increased demand for JPM shares.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNdUVKQkh1T29HY3dqdnllRFIxTS1xRXhiaE1fa1c4cnVMWVNhaG5kSWNRajBjWU9JdGxPdnRrLS1nZmt4RUVLLUw4X3NjNWp4SllRR2VINXkyTG9qb3lNNG4wd2tPY3k4SGdpa3Z0eVhUR0UwRjhpSF84VjhDeEFVTHdlV3otLUtuYmprVHo0dGZYaVlnM1lES0FhV2tEeDh5T0ZoNkRZQ2dUeE5YdnV1VXJJY3JhWjJ6MUtqZzcwSDZIWE9ZaEHSAcsBQVVfeXFMTzd6YTVqeGJWUjFaLW5FYlhPcmNqQ2hLMkhtM1d5c25SSDBiLVJQeGpIYXprS1BlT0VOTUpibGlpZVl2aXpybkdyeWYtcmVmMXRLdU83ODdMTVpZRWtVak5xbGlZcE9lRHBkaXdVV2hyLVlhMkl5TW9zOHZSMjZwQWJvYnBGM3BuTHR4RklMbVRkbkNuQUUwREo5TWRoSkJyYk1jdUVJQWpsSVJUdk9PQzRfMG9sWjI4WFlCbnNzVnlxemdVSVVkU2k1Zzg?oc=5>

### JPMorgan Chase & Co. $JPM Stock Holdings Boosted by Summit Global Investments
- Summary: Summit Global Investments increased JPM holdings, signaling confidence in the bank.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNSlh5b2xBZU1OSHJqVjkzN2lrM2ZyOVpkbklGcHpvaVVGQjFhOFNkWUdYbmxlYTVtTGhKSjZZSVVyOEotVzE0NFp3VUk2XzE1bm5qNXFlbTlMWGg5ZFMyU0RmUFlDVjl1Vk1pc2VHMTI4d29MQVZfa0poa1dUd0UxQVpaZGZTVjJybUdSRlV0WTNhdDEtTXR1d2ZCQUY4NDh5ODRfX2p1OW9OalhqeHZod3NWRnRObFVJRmV0OEhfMjJLZXE5SU1YSENYc3FvLVE?oc=5>

## HEADWINDS

### JPMorgan Chase Stock (JPM) Falls on Reports Democrats Plan to Probe Its Ties to Jeffrey Epstein
- Summary: JPMorgan Chase Stock (JPM) Falls on Reports Democrats Plan to Probe Its Ties to Jeffrey Epstein
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxQclNOVk53TE1lZnpjVEVhVFl2Z3d5TGtDVXpHSEl1bGpKeEVnVVlJVkVPbGxvdE9NVFBqbHpqWGd6Umo5LVFaTzN1NDhfWHR0QjVkQ2dLN3FqME1YTlNsTlhLU2lYaXRuV0JnMnpQUk9zUHc5elF4SGJLYUV2NFJ4a2x0alR6N0dyRC1fWFdTNWROa0prTlUtZy1Idnl4SFZBREtKWVpIWEVrQWJKWVpXcW5RSW5FaUZha2dpR3podzg?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Shares Down 4.2% - Here's Why
- Summary: JPMorgan Chase & Co. (NYSE:JPM) Shares Down 4.2% - Here's Why
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNRWhUbDBSNFhqOUE3SldKYklBU1UzR1lNYnViX04yLXNVN3AwNnB2Z0ZaS2RoWkpscVJOaE0zSjBYbFJoWUhZdWhyNmpQV3h5b3JScVRtNXotM2UxSDRraHVxOTVtd0Q4N1pjLUlJNmd3WENYX0gwbEpXUF96N2FtWndSSHpGWHc4UDkyV1BDMzBFaF9MazRzcVB6cjEtWDQwNWd2RHJpUmdzV1JIMXFRdQ?oc=5>

### JPMorgan Drops 6.2% in a Single Session: What It Means
- Summary: Shares dropped 6.2% in one session, signaling significant short‑term volatility.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQSnBNeVhaelpNUWNLUzZ4TU91blhhWHVjX1lNRjc0cHY0UU5fcU44RlZLY3ZJVGZzM1R2dVZoakRGcGNsRUM4eWRKVjlsQy1oT1JwYkt3dk9uOW5CSXduakhDYmlkM1pCLVBKTzdfZ3U3dERERDF6eXZLTGFLb3RES1ZVaUs5cHRiZVYtYWxISQ?oc=5>

### JPMorgan Chase & Co Stock (JPM) Moved Down by 3.50% on Nov 5: What Investors Need To Know
- Summary: Stock fell 3.5% on Nov 5, indicating short‑term downside pressure.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPVTNqRHRxb0VJWl9velJGajJDS1JadTFCMDQ1b0dnSS1QeEtEZUZhdnViQ2pJQUZKSkxXU0Y5dlNzZXo1bW85VnE2Mi0xaWlYZ01pNnF5dGktQnA1cVpQYVMyV0luR2NubDJSM1NyZDM3OUw4dkFPeE5xVEhlXzBwRXhUNlQ4WVNvQVE?oc=5>

### Learn Why The Bull Case For JPMorgan Chase Stock Could Change Following Earnings Miss
- Summary: JPM missed earnings expectations, potentially weakening its bull case.
- Date: 2026-11-01 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQN3lvaEZRZy1SYlZ2cVlxSlRjTHJERVNPbE00T0JUS3JhdHUzQmlnMGtEX1R0WTF5eS1UcTEyYlBWcmM0RlB4eWJMaWQ5aW42b0dja0dxMTFfaVB4QXA3aENadDczdTA2WDRndkRlbGNhQlhreGxhakxLcGVlUk1nMVNoTjVDNVNGS0RtLV9PcGZpTUZ0MWtPVA?oc=5>

### JPMorgan stock (JPM) slides as Democrats plan probe into Jeffrey Epstein ties: Could bank executives face
- Summary: Stock slid amid planned probe, suggesting potential regulatory risk.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwJBVV95cUxQRDNicXhjOHZJalM5UnNmZDFDdTdkc0lvLXduVE1pTGVhNkhDMGZxM2RpM2Q5Z3hpOTdGQkhyQTVSZkJ1UzRXTGVlNF9hRFJ0UTBsVmRnaUw4QlZHTHJBcC1mckNNOWRGUW5Qd21DY2xxVmMzZWQwUzJLdlBuNFRsaVBJT29mVGxzbExRM3VjbTNfSEdqcF85S2M4U2dJcnowblJXS2N4b05JZmQwU0ZCdF9nQmhsV2ZyZHVtVEJsVnRHRlV3enUwLXFhTVFSNTFMVXNfcUJLNXlhNDBNelVjUXZWZ0J5cjRkc21RRHlUc0RQcm9OcGlaNi14Z1RBM0dWVVNveGxQT3pHQkdzUGs0YmNyeFU2MWs5bWNOV2NFQdIBpAJBVV95cUxOS3BsWloxMFpFOWtyaHdrTThNZ0c4VkRFNGZxT0FLMVFSZDVQblBUZ3hPTUlILUJRRFozcHRwdEdJT3lWaFNEN0hJQWRpMk0tMVZZNVJTRU1fZzhSWnlSRkQ5SzViZTdLRVZWVWRMX2ZnVm05Mk1CVHZzdS0yUks2eWxKZWJfRk5zS2VmSmJxeTNndjJRQU1WZWoxV3Y2V0cwdFNLSGxRRFphU0NzSUJiTkxXeW1BTU1UajNnblJmVG5uTkgtTVZBMGFDNW85VUsyRlpYLXJQRlFkaEJOX0lONFJUOUpoTUtXRkxLemc0Y3JMUnhWVEJNa3NmMW5FSjNDUDFycWVNQnYxLUhBTWFucl9tRmpkOEQxUnFRTjBRczNfQnpC?oc=5>

## CATALYSTS

### JPMorgan Chase & Co. $JPM Shares Purchased by Investment Partners LTD.
- Summary: JPMorgan Chase & Co. $JPM Shares Purchased by Investment Partners LTD.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPSWV5Y0tZUng3M1JxQ2RXMy1Hb0JkOG1zVk41dTlwLTJGYy1qVkZ0OFBMbm55a0dlT3lrdEN5UXl1bWFjSXFYZ3RzT2JlMDN0S1JlTkdRRFlwU0RZckNYYW8wYVdIVUU3MWNEbW1KYUIxMXd6SThPNHFvcXVCY2tXanp3LWJpX0ppdXJTOHJoN2JuekFlQ2p3clMzclpjNGNxMndqaGpYUlI1RmdIOTJraUJJaERjOWRGMkhnNDBVUktJUXE1?oc=5>

### JPMorgan Chase & Co. $JPM Stock Acquired by CHICAGO TRUST Co NA
- Summary: JPMorgan Chase & Co. $JPM Stock Acquired by CHICAGO TRUST Co NA
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNS1B6RFV2SmZxRmNTTTA5LXphMU5ZQnJGVE9HNHU1UnVWaW1qME1XNWtEa19LM3VpcmxGVjhoUk4zQXZISVg0UW9mTUwwOG1fblRjcVkwaFpWallpOVh6WnhTQVA0OGNqTlE4bW1wejVPZXlQRXdleGVQWE11c2FQamdUOV9PbGR0OUZlbnJ2cW1zNjNPa21lS0hpRDB2UFdpSEt4T1JTb0ZuUFNvV3RwN2lteHEyc3V1a01nTQ?oc=5>

### JPMorgan Chase (JPM) Stock May Be 32% Undervalued Following Blockchain Expansion
- Summary: Analysts suggest JPM's stock is undervalued due to its blockchain initiatives, indicating potential upside.
- Date: 2026-11-02 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNQUtmOUNqSlFCMFFPVTBHYTlUN1BPVVhLVEh5LTNWNi1ka2lWeHBOMnNENVR3NWV2dGZIaURWR3Z5SkdfM3BxZ1dxOVZYUU55Wmp3NnlGSmFsb2djUmwyMWZlVnBmcnctMXlaX2Z5MlE1RWZoNFhvZU9kXzVqZXlBM2R3aTZPUXM4by1mbzJHNGJweDJrMVcxZjdnakJDXzN6NDF5QV9BSW1LRThHZTJDVHNvTkZZT0YzM0c0aFQ1M2JjdGw0Q3fSAcsBQVVfeXFMTmZFeXpBTGVaTW0tazZNUFJoVXRnaFBDZFBaNTA0TjFoWUN0RjZjaE95SmUxRmpMQXhsVXZHWmtfMlk4eFNDNS1lREp6OW5ma1BBeUlHYXFsTE5RVS16dUpoZm1Tal95c0hKQjNQMWxUc3JKR1dCT1ZqZjdvNTZGdDl2QUZJVUtTQjYtamdudGFHRkpRa1lZM0k5RVdnemRtaW5Ya3c0OWZUOFJjenp6WmtnMlJOclJBdFBya3M3ajIwUXl3OU0tQ1dpX1k?oc=5>

### Mirae Asset Global Investments Co. Ltd. Makes New $320.21 Million Investment in JPMorgan Chase & Co. $JPM
- Summary: Mirae Asset invests $320.21M in JPM shares, indicating confidence in the bank's prospects.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxPdndEZ2pvNDZMc2lJNEZPb3ZEampkSFJjbnczSlg4bzB1Q1VIYWUzM3NYbkVIZExKYjNkd1FYdjNOTE9sV1o1WG44c3pXbnlJbzdqZzdtZHUyVnc0OWNsN0RFbUFPdXdueklJaUs2OFBOckxUZ012Vy05T0JxMWtLTFZiUVZQbWx2bGIzQjFGcWdsc29aTnl5S3FIQUp0ek1IRzFWTm5SRGp0ZWhURFJnRnRXTlZqVnNDLUhRTlE3bUNNNUNOcmZUaDhjZ2dfS1hUSDBPeXR5QzVEeXI4bWlGNUx4aTdPRHJYck9lU3FTVQ?oc=5>

## RISKS

### JPMorgan Chase (JPM) Draws A Senate Probe Over Epstein Ties
- Summary: Senate investigation into JPM's ties to Epstein raises regulatory concerns.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOZXhoQjJxaGViV0VDeGlvUURGODN6T25jcXhzT2h3V0RBdGxPS1VkRnNkTm15bFVfTDZuLUV2SWlGUjhPdnQycmY5a3dyUWVwZ3hHdWtoNDVIRWVRMlhlT1RVdVlUOXpPTEc0LW8xZW5kUjdaVkpEb2swLXZyQjZLQjhvdDlZcmxVdVFYZHBqZnlfLUFGUmVpQTZYVEpXZlJIQzNyd0VhQmtoTmY1elhBaGlWSU8wNWQyMkFpNXpZQTVBZ9IBxwFBVV95cUxNcU1HZFdGSEF3QmdnOE5aakFpYTBCcVRJaVM4QXpjZVQ5ZkhmMVN3MjFidllOUHRPX3hlcnNnUEJXdmtUbjU3alh5WGpfMTdUam1GamppM085VGVTTG8tVm9vMEQwWThfUEs2ZkhfejFvV2ZLQlNpc1d1UUxHcGdQVjgxWjJOUXJyMnZsaXEyVC1LcjE5ZFVyUWlnUDdEbDgtOWpiTmo1d3FZbHhPMjVQSzRINjhVR2tlZkJyaklKM19XbGs3a3k0?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **14.03** | **2.53** | **N/A** | **10.20** | **888,274,812,928.00 USD** | **8.78** |
| BAC | 11.88 | 1.26 | N/A | 3.40 | 341,008,318,464.00 USD | -5.29 |
| C | 11.55 | 1.03 | N/A | 8.00 | 197,051,564,032.00 USD | 20.49 |
| WFC | 11.96 | 1.59 | N/A | 0.40 | 251,975,319,552.00 USD | 0.28 |

Peers fetched as_of: 2026-11-06; JPM reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-06

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 24,246,000,000.00 USD; period 2014-07-01/2014-09-30; fiscal year/reporting period 2014/Q3
- Net income (latest available single quarter): 15,305,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/19617/000162828026069523/jpm-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMitwFBVV95cUxOMWlKWkdVQmZ1LVJjRXR2Ym15OC01UEM3ckd0TldqeXIxbE9feHRkOUh2TzhEekFCd18xbWV1bzVsMmQxOGJhc3pFWkZManJOdkQ0ZXNwdWNFMnJWYzdUY0NoQm9rTFJhR1lFMFdxRHdsaUZVbm9GRW5LV09TREpPQlJ4TXRKMVBhZjhuRFZTQ0VTWjBYc2dSWFQ3VWpGdmtyMzNfMXBrT2dzZWYxNVVVYmNrSnhGc1E?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPeVBaeVl2dlVyRlhuVTlZWVVkaHJZU284ZzFTYWh5TUo3cU14MHVNYm5YUHFNZFNFd1Btejl6Tl93VEhvYlk1QWktMmdLRzdnNTBkdTF3RzdiQVRxWUxwaHpfcUthT3FhVi1zMjB1TV81OWRXbUVKSnFJUWZ5bjdUTUc5RnhzR2x1Nlc5WkROaVhFc3hLVE12MmpKRkh1Vi0wRjFkb19TQ09WTzNTV3JlQ2FMTkpSZmdEU2doZUNtNTkxZVRa?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNOTlQcmpncGV4YmlFV0I3MVhXVkdwUE9HN0RIeUVJblBpdjRqR2RaM3hseGo3enA4U2R2VU9BcXNEZ2RXN25WdTZlXzZONWFhenhCLTNyZkluTlFwY1ZkQXY1TmdUX0Y3Ui1ZMkc5RllFcUV2Vm5oXzRPOHdFV1NFemRneThkSnpkc1gxWFhWcXFZcXNBdHZCdkIzNzB1WVVKRzUxMVhZZEpEUQ?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNdUVKQkh1T29HY3dqdnllRFIxTS1xRXhiaE1fa1c4cnVMWVNhaG5kSWNRajBjWU9JdGxPdnRrLS1nZmt4RUVLLUw4X3NjNWp4SllRR2VINXkyTG9qb3lNNG4wd2tPY3k4SGdpa3Z0eVhUR0UwRjhpSF84VjhDeEFVTHdlV3otLUtuYmprVHo0dGZYaVlnM1lES0FhV2tEeDh5T0ZoNkRZQ2dUeE5YdnV1VXJJY3JhWjJ6MUtqZzcwSDZIWE9ZaEHSAcsBQVVfeXFMTzd6YTVqeGJWUjFaLW5FYlhPcmNqQ2hLMkhtM1d5c25SSDBiLVJQeGpIYXprS1BlT0VOTUpibGlpZVl2aXpybkdyeWYtcmVmMXRLdU83ODdMTVpZRWtVak5xbGlZcE9lRHBkaXdVV2hyLVlhMkl5TW9zOHZSMjZwQWJvYnBGM3BuTHR4RklMbVRkbkNuQUUwREo5TWRoSkJyYk1jdUVJQWpsSVJUdk9PQzRfMG9sWjI4WFlCbnNzVnlxemdVSVVkU2k1Zzg?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxNSlh5b2xBZU1OSHJqVjkzN2lrM2ZyOVpkbklGcHpvaVVGQjFhOFNkWUdYbmxlYTVtTGhKSjZZSVVyOEotVzE0NFp3VUk2XzE1bm5qNXFlbTlMWGg5ZFMyU0RmUFlDVjl1Vk1pc2VHMTI4d29MQVZfa0poa1dUd0UxQVpaZGZTVjJybUdSRlV0WTNhdDEtTXR1d2ZCQUY4NDh5ODRfX2p1OW9OalhqeHZod3NWRnRObFVJRmV0OEhfMjJLZXE5SU1YSENYc3FvLVE?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxQclNOVk53TE1lZnpjVEVhVFl2Z3d5TGtDVXpHSEl1bGpKeEVnVVlJVkVPbGxvdE9NVFBqbHpqWGd6Umo5LVFaTzN1NDhfWHR0QjVkQ2dLN3FqME1YTlNsTlhLU2lYaXRuV0JnMnpQUk9zUHc5elF4SGJLYUV2NFJ4a2x0alR6N0dyRC1fWFdTNWROa0prTlUtZy1Idnl4SFZBREtKWVpIWEVrQWJKWVpXcW5RSW5FaUZha2dpR3podzg?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNRWhUbDBSNFhqOUE3SldKYklBU1UzR1lNYnViX04yLXNVN3AwNnB2Z0ZaS2RoWkpscVJOaE0zSjBYbFJoWUhZdWhyNmpQV3h5b3JScVRtNXotM2UxSDRraHVxOTVtd0Q4N1pjLUlJNmd3WENYX0gwbEpXUF96N2FtWndSSHpGWHc4UDkyV1BDMzBFaF9MazRzcVB6cjEtWDQwNWd2RHJpUmdzV1JIMXFRdQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQSnBNeVhaelpNUWNLUzZ4TU91blhhWHVjX1lNRjc0cHY0UU5fcU44RlZLY3ZJVGZzM1R2dVZoakRGcGNsRUM4eWRKVjlsQy1oT1JwYkt3dk9uOW5CSXduakhDYmlkM1pCLVBKTzdfZ3U3dERERDF6eXZLTGFLb3RES1ZVaUs5cHRiZVYtYWxISQ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPVTNqRHRxb0VJWl9velJGajJDS1JadTFCMDQ1b0dnSS1QeEtEZUZhdnViQ2pJQUZKSkxXU0Y5dlNzZXo1bW85VnE2Mi0xaWlYZ01pNnF5dGktQnA1cVpQYVMyV0luR2NubDJSM1NyZDM3OUw4dkFPeE5xVEhlXzBwRXhUNlQ4WVNvQVE?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQN3lvaEZRZy1SYlZ2cVlxSlRjTHJERVNPbE00T0JUS3JhdHUzQmlnMGtEX1R0WTF5eS1UcTEyYlBWcmM0RlB4eWJMaWQ5aW42b0dja0dxMTFfaVB4QXA3aENadDczdTA2WDRndkRlbGNhQlhreGxhakxLcGVlUk1nMVNoTjVDNVNGS0RtLV9PcGZpTUZ0MWtPVA?oc=5
- https://news.google.com/rss/articles/CBMinwJBVV95cUxQRDNicXhjOHZJalM5UnNmZDFDdTdkc0lvLXduVE1pTGVhNkhDMGZxM2RpM2Q5Z3hpOTdGQkhyQTVSZkJ1UzRXTGVlNF9hRFJ0UTBsVmRnaUw4QlZHTHJBcC1mckNNOWRGUW5Qd21DY2xxVmMzZWQwUzJLdlBuNFRsaVBJT29mVGxzbExRM3VjbTNfSEdqcF85S2M4U2dJcnowblJXS2N4b05JZmQwU0ZCdF9nQmhsV2ZyZHVtVEJsVnRHRlV3enUwLXFhTVFSNTFMVXNfcUJLNXlhNDBNelVjUXZWZ0J5cjRkc21RRHlUc0RQcm9OcGlaNi14Z1RBM0dWVVNveGxQT3pHQkdzUGs0YmNyeFU2MWs5bWNOV2NFQdIBpAJBVV95cUxOS3BsWloxMFpFOWtyaHdrTThNZ0c4VkRFNGZxT0FLMVFSZDVQblBUZ3hPTUlILUJRRFozcHRwdEdJT3lWaFNEN0hJQWRpMk0tMVZZNVJTRU1fZzhSWnlSRkQ5SzViZTdLRVZWVWRMX2ZnVm05Mk1CVHZzdS0yUks2eWxKZWJfRk5zS2VmSmJxeTNndjJRQU1WZWoxV3Y2V0cwdFNLSGxRRFphU0NzSUJiTkxXeW1BTU1UajNnblJmVG5uTkgtTVZBMGFDNW85VUsyRlpYLXJQRlFkaEJOX0lONFJUOUpoTUtXRkxLemc0Y3JMUnhWVEJNa3NmMW5FSjNDUDFycWVNQnYxLUhBTWFucl9tRmpkOEQxUnFRTjBRczNfQnpC?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPSWV5Y0tZUng3M1JxQ2RXMy1Hb0JkOG1zVk41dTlwLTJGYy1qVkZ0OFBMbm55a0dlT3lrdEN5UXl1bWFjSXFYZ3RzT2JlMDN0S1JlTkdRRFlwU0RZckNYYW8wYVdIVUU3MWNEbW1KYUIxMXd6SThPNHFvcXVCY2tXanp3LWJpX0ppdXJTOHJoN2JuekFlQ2p3clMzclpjNGNxMndqaGpYUlI1RmdIOTJraUJJaERjOWRGMkhnNDBVUktJUXE1?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNS1B6RFV2SmZxRmNTTTA5LXphMU5ZQnJGVE9HNHU1UnVWaW1qME1XNWtEa19LM3VpcmxGVjhoUk4zQXZISVg0UW9mTUwwOG1fblRjcVkwaFpWallpOVh6WnhTQVA0OGNqTlE4bW1wejVPZXlQRXdleGVQWE11c2FQamdUOV9PbGR0OUZlbnJ2cW1zNjNPa21lS0hpRDB2UFdpSEt4T1JTb0ZuUFNvV3RwN2lteHEyc3V1a01nTQ?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNQUtmOUNqSlFCMFFPVTBHYTlUN1BPVVhLVEh5LTNWNi1ka2lWeHBOMnNENVR3NWV2dGZIaURWR3Z5SkdfM3BxZ1dxOVZYUU55Wmp3NnlGSmFsb2djUmwyMWZlVnBmcnctMXlaX2Z5MlE1RWZoNFhvZU9kXzVqZXlBM2R3aTZPUXM4by1mbzJHNGJweDJrMVcxZjdnakJDXzN6NDF5QV9BSW1LRThHZTJDVHNvTkZZT0YzM0c0aFQ1M2JjdGw0Q3fSAcsBQVVfeXFMTmZFeXpBTGVaTW0tazZNUFJoVXRnaFBDZFBaNTA0TjFoWUN0RjZjaE95SmUxRmpMQXhsVXZHWmtfMlk4eFNDNS1lREp6OW5ma1BBeUlHYXFsTE5RVS16dUpoZm1Tal95c0hKQjNQMWxUc3JKR1dCT1ZqZjdvNTZGdDl2QUZJVUtTQjYtamdudGFHRkpRa1lZM0k5RVdnemRtaW5Ya3c0OWZUOFJjenp6WmtnMlJOclJBdFBya3M3ajIwUXl3OU0tQ1dpX1k?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxPdndEZ2pvNDZMc2lJNEZPb3ZEampkSFJjbnczSlg4bzB1Q1VIYWUzM3NYbkVIZExKYjNkd1FYdjNOTE9sV1o1WG44c3pXbnlJbzdqZzdtZHUyVnc0OWNsN0RFbUFPdXdueklJaUs2OFBOckxUZ012Vy05T0JxMWtLTFZiUVZQbWx2bGIzQjFGcWdsc29aTnl5S3FIQUp0ek1IRzFWTm5SRGp0ZWhURFJnRnRXTlZqVnNDLUhRTlE3bUNNNUNOcmZUaDhjZ2dfS1hUSDBPeXR5QzVEeXI4bWlGNUx4aTdPRHJYck9lU3FTVQ?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOZXhoQjJxaGViV0VDeGlvUURGODN6T25jcXhzT2h3V0RBdGxPS1VkRnNkTm15bFVfTDZuLUV2SWlGUjhPdnQycmY5a3dyUWVwZ3hHdWtoNDVIRWVRMlhlT1RVdVlUOXpPTEc0LW8xZW5kUjdaVkpEb2swLXZyQjZLQjhvdDlZcmxVdVFYZHBqZnlfLUFGUmVpQTZYVEpXZlJIQzNyd0VhQmtoTmY1elhBaGlWSU8wNWQyMkFpNXpZQTVBZ9IBxwFBVV95cUxNcU1HZFdGSEF3QmdnOE5aakFpYTBCcVRJaVM4QXpjZVQ5ZkhmMVN3MjFidllOUHRPX3hlcnNnUEJXdmtUbjU3alh5WGpfMTdUam1GamppM085VGVTTG8tVm9vMEQwWThfUEs2ZkhfejFvV2ZLQlNpc1d1UUxHcGdQVjgxWjJOUXJyMnZsaXEyVC1LcjE5ZFVyUWlnUDdEbDgtOWpiTmo1d3FZbHhPMjVQSzRINjhVR2tlZkJyaklKM19XbGs3a3k0?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
