# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T06:06:26.702800+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 6, 'ai': 16, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/JPM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 7 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 70.83%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 342.0800 |
| Return 1D (%) | 2.2691 |
| Return 1W (%) | 0.4404 |
| Return 1M (%) | 2.7298 |
| Return YTD (%) | 8.2082 |
| Return 1Y (%) | 10.9667 |
| Annualized volatility (%) | 23.0539 |
| Beta vs SPY | 0.8103 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.5331 |
| Downside deviation (rf=0, %) | 16.6020 |
| Sortino (rf=0) | 0.7402 |
| Historical VaR 95% (1D, %) | 2.4535 |
| Historical ES 95% (1D, %) | 3.3955 |
| Correlation vs SPY | 0.4813 |
| Tracking error vs SPY (%) | 20.3746 |
| P/E (trailing) | 14.35 |
| P/B | 2.59 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 13.38 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 42.58 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 340.6576 |
| Close vs MA50 (%) | 0.4175 |
| MA200 | 321.5182 |
| Close vs MA200 (%) | 6.3952 |
| RSI (14, Wilder) | 52.9064 |
| MACD (12,26) | 0.6085 |
| MACD signal (9) | -0.0816 |
| MACD histogram | 0.6901 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 342.0800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.2691 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.4404 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.7298 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 8.2082 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 10.9667 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 23.0539 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.6020 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.7402 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4535 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3955 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4813 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.3746 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8103 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5331 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.3766 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 42.5840 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.3490 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 52.9064 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6901 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.4175 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.3952 -> Clearly above the moving-average trend level.

## TAILWINDS

### JPMorgan Chase & Co. $JPM Stock Position Raised by Bank Julius Baer & Co. Ltd Zurich
- Summary: Bank Julius Baer increased its JPM position, indicating confidence in the bank.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxPV21ST25Bejhhc3ZadlJGYkV1MlhzQ2l2b3dfRTZCbW1IZE90ejVRRWprWmNLU3ctQ1RvOW1BdHVPNFRXQTdaamZVUW8wdGl3NnZMZGJwSXFrSlY1cU9oUEFIT25RNG50Q0s1RUQzdzBLMThDVjY2dWVWNDRXeDZWZE52SFRNUEhFZ1lBTjExTUtFT01KQlA2S3k1dncycmdiblR1aDFQazdCMVdzTzhiU3c1bm9mVlFScG1yZ1hXSzJERVo5d2I2N05fWXpWVlQ2TVJ5bQ?oc=5>

### JPMorgan Chase & Co. $JPM Stock Holdings Boosted by Summit Global Investments
- Summary: Summit Global Investments increased its stake in JPM, signaling confidence in the bank.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNSlh5b2xBZU1OSHJqVjkzN2lrM2ZyOVpkbklGcHpvaVVGQjFhOFNkWUdYbmxlYTVtTGhKSjZZSVVyOEotVzE0NFp3VUk2XzE1bm5qNXFlbTlMWGg5ZFMyU0RmUFlDVjl1Vk1pc2VHMTI4d29MQVZfa0poa1dUd0UxQVpaZGZTVjJybUdSRlV0WTNhdDEtTXR1d2ZCQUY4NDh5ODRfX2p1OW9OalhqeHZod3NWRnRObFVJRmV0OEhfMjJLZXE5SU1YSENYc3FvLVE?oc=5>

## HEADWINDS

### JPMorgan stock (JPM) slides as Democrats plan probe into Jeffrey Epstein ties: Could bank executives face
- Summary: Stock slid amid planned probe, suggesting potential regulatory risk.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwJBVV95cUxQRDNicXhjOHZJalM5UnNmZDFDdTdkc0lvLXduVE1pTGVhNkhDMGZxM2RpM2Q5Z3hpOTdGQkhyQTVSZkJ1UzRXTGVlNF9hRFJ0UTBsVmRnaUw4QlZHTHJBcC1mckNNOWRGUW5Qd21DY2xxVmMzZWQwUzJLdlBuNFRsaVBJT29mVGxzbExRM3VjbTNfSEdqcF85S2M4U2dJcnowblJXS2N4b05JZmQwU0ZCdF9nQmhsV2ZyZHVtVEJsVnRHRlV3enUwLXFhTVFSNTFMVXNfcUJLNXlhNDBNelVjUXZWZ0J5cjRkc21RRHlUc0RQcm9OcGlaNi14Z1RBM0dWVVNveGxQT3pHQkdzUGs0YmNyeFU2MWs5bWNOV2NFQdIBpAJBVV95cUxOS3BsWloxMFpFOWtyaHdrTThNZ0c4VkRFNGZxT0FLMVFSZDVQblBUZ3hPTUlILUJRRFozcHRwdEdJT3lWaFNEN0hJQWRpMk0tMVZZNVJTRU1fZzhSWnlSRkQ5SzViZTdLRVZWVWRMX2ZnVm05Mk1CVHZzdS0yUks2eWxKZWJfRk5zS2VmSmJxeTNndjJRQU1WZWoxV3Y2V0cwdFNLSGxRRFphU0NzSUJiTkxXeW1BTU1UajNnblJmVG5uTkgtTVZBMGFDNW85VUsyRlpYLXJQRlFkaEJOX0lONFJUOUpoTUtXRkxLemc0Y3JMUnhWVEJNa3NmMW5FSjNDUDFycWVNQnYxLUhBTWFucl9tRmpkOEQxUnFRTjBRczNfQnpC?oc=5>

### JPMorgan Chase (JPM) Draws A Senate Probe Over Epstein Ties
- Summary: JPM faces a Senate probe related to Epstein connections, raising regulatory concerns.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOZXhoQjJxaGViV0VDeGlvUURGODN6T25jcXhzT2h3V0RBdGxPS1VkRnNkTm15bFVfTDZuLUV2SWlGUjhPdnQycmY5a3dyUWVwZ3hHdWtoNDVIRWVRMlhlT1RVdVlUOXpPTEc0LW8xZW5kUjdaVkpEb2swLXZyQjZLQjhvdDlZcmxVdVFYZHBqZnlfLUFGUmVpQTZYVEpXZlJIQzNyd0VhQmtoTmY1elhBaGlWSU8wNWQyMkFpNXpZQTVBZ9IBxwFBVV95cUxNcU1HZFdGSEF3QmdnOE5aakFpYTBCcVRJaVM4QXpjZVQ5ZkhmMVN3MjFidllOUHRPX3hlcnNnUEJXdmtUbjU3alh5WGpfMTdUam1GamppM085VGVTTG8tVm9vMEQwWThfUEs2ZkhfejFvV2ZLQlNpc1d1UUxHcGdQVjgxWjJOUXJyMnZsaXEyVC1LcjE5ZFVyUWlnUDdEbDgtOWpiTmo1d3FZbHhPMjVQSzRINjhVR2tlZkJyaklKM19XbGs3a3k0?oc=5>

### ETFs Are Net Sellers of JPMorgan Chase (JPM) on Nov. 5
- Summary: ETFs sold JPM shares, indicating negative sentiment among institutional investors.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQaGlWMXljWGtsTDNTQzZWNzBGNi12QVJQbTFMS1VyUFo5R2l5QVZZUEVGUWNtNmE1UUd6bWRqU3hNWGVidWFNbnpYYktDMjFsZUZlbXpXUTRNQmxPei1CVFdHWjk5M0tmaUFWaHEwVGhscVRUTzV2SklnSVVObE04M0xQSkFYMmVwVHpsSTFlTjFjUFY1eHB6dWdielU?oc=5>

### JPMorgan Chase & Co Stock (JPM) Moved Down by 3.50% on Nov 5: What Investors Need To Know
- Summary: JPM stock fell 3.5%, reflecting short-term market pressure.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPVTNqRHRxb0VJWl9velJGajJDS1JadTFCMDQ1b0dnSS1QeEtEZUZhdnViQ2pJQUZKSkxXU0Y5dlNzZXo1bW85VnE2Mi0xaWlYZ01pNnF5dGktQnA1cVpQYVMyV0luR2NubDJSM1NyZDM3OUw4dkFPeE5xVEhlXzBwRXhUNlQ4WVNvQVE?oc=5>

### JPMorgan Drops 6.2% in a Single Session: What It Means
- Summary: JPM shares dropped 6.2% in one session, signaling significant downside risk.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQSnBNeVhaelpNUWNLUzZ4TU91blhhWHVjX1lNRjc0cHY0UU5fcU44RlZLY3ZJVGZzM1R2dVZoakRGcGNsRUM4eWRKVjlsQy1oT1JwYkt3dk9uOW5CSXduakhDYmlkM1pCLVBKTzdfZ3U3dERERDF6eXZLTGFLb3RES1ZVaUs5cHRiZVYtYWxISQ?oc=5>

## CATALYSTS

### JPMorgan Chase & Co. $JPM Stock: Provenance Wealth Advisors LLC Raises Holdings
- Summary: JPMorgan Chase & Co. $JPM Stock: Provenance Wealth Advisors LLC Raises Holdings
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxQOEhkdEhBTFZVSDFWUEtLcmhkc1FlMlpESWlJeVFJZ1E0VzBIVnBVR213c2dNUllmeFB4UWNyVUtULWs0OGFlTW5MRFVvUVhQSUdPT2N3VlhMRXR6R1Zmb0g5SUdxUkxiS3k2cmkzaGl3OURMMkpXWjlIbVdMR2lSZzJFRk5GNm5HWDdKYldaLTlPNmZhekJuTnMtWGZjWWNvS3VVdGxzdXNDQmZLM25QWE9QcTdtdktxaWtaRDh1b1VtRHFXS1FnWG1jaXNkSnRf?oc=5>

### JPMorgan Chase & Co. $JPM Shares Acquired by Rakuten Investment Management Inc.
- Summary: JPMorgan Chase & Co. $JPM Shares Acquired by Rakuten Investment Management Inc.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxNZnNYeUVUZEhzcU42bzVZYklGd2NkQWJjRG5kYmxFOEFvcWtNdXE0ZXZVV2RyWHdfbUhHUkNlNVg3YzZId0tlMFh2TUtXTGgzSjFoUHBlRU1GazVzZlNFbV9wcVEwV3JSakNwamQ4RkF6RTA1TVp2R0xLb05RNGlDdTVqb0JXbF9zRkVrYzhmSDdpZkcxb3F5LXVIcy1DTl93SkZCRVBnQzJ0VVc3eFZXT2x0am5Fc2FVZWR6UFZ1NVZEZlFfRkw2cVg3Z2hKaVF4?oc=5>

### JPMorgan Chase & Co. $JPM Stock Bought by Greenleaf Trust
- Summary: JPMorgan Chase & Co. $JPM Stock Bought by Greenleaf Trust
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQZjNsYmtiazRCZTluMmhBYlMxSUkyaEhObzdMWFpYcUNyTWVrLTVOUUZ0MWUxQldpemEzX1BNcEN2RVVjSlpkRXFTRXZQZkRpcVQ0TkFRQUVDMW9PaWdFRHVIdXlMMHBWQk5yV2xBemlFVHgtdlF3aU83RnBaTGlfV0sxcW9YaHQydzk3ZFJvRGQ5MUZuc3VyWkhmZmRKQTJpTEcyanFlTWNkOFZrQ0dhalEwaC0?oc=5>

### JPMorgan Chase & Co. $JPM Shares Sold by AIA Group Ltd
- Summary: JPMorgan Chase & Co. $JPM Shares Sold by AIA Group Ltd
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPMXNySVJDRkZWNVEzc2pYWXE5MUdpNUptYzVkRXBTLVRNMkJtSXZGR2lRNmlVQXNQSmNkb2dZWkNZODhlSll2V004Q0ZhejZqR3dZM0hFWEp5QndOSDUtb0M2NHRJemc1WjVLSVN3OVdHc2p0alFZWWVyYzBiTGR2N1V0QzNnVlh6eHZ0M2ZHZE5SczdUZHN3Y1hLOXpFMmc3c0JpOVZkX2FpRTFrQl9EVw?oc=5>

### JPMorgan Chase & Co. $JPM Stock: ProShare Advisors LLC Cuts Stake
- Summary: JPMorgan Chase & Co. $JPM Stock: ProShare Advisors LLC Cuts Stake
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQTW1LNDZzRXRoVFQwdVlsaVFqRGN2Rk9oZDlsM0UxREgzcVdXeVBYZEpZbEJHRGxhZl9wX1RRZDhVRUlpM0pnRU5GNTFxUXRseXBkMHJHaVZRdWNLcHBTZWxmQ2NjekxnVzFObEZ3aTFzQ3BhVExGSkxJVW1CVEw2T1ZuS3Rkakp6NWxmVTZDYTRObHNJZlIyV0pXdjdsdXhfSUMtRzVZQkxYV2JNN1M4dUNJY1NMaXZYMzZscDZ3?oc=5>

### JPMorgan Chase & Co. $JPM Shares Purchased by One Way Holdings LLC
- Summary: JPMorgan Chase & Co. $JPM Shares Purchased by One Way Holdings LLC
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNU2ZMaTZDY3FVcms0QmZ4SGg5a1I2WThhNnFranpEUGxldDZHSHh5UHU2ZFNraHhuT0dBLTlBeFQ0TkVDYk0yazkyZDJoTk1XWmJRRWd0YTdIWm9yOXkwZ1piVGZXNEtKOGRiZlhTQTd2UjdHUjBmelBVRFkzbjdRd3l1WTltZGlqS2EtSEZNX2M2d1BEWE9rdjE2andiZEQ0a09WUUgybkxyeGtjdlZDSHNoUHgwVlhiR2tZcW9uZnM?oc=5>

### JPMorgan Stock Loses Over 100% of Its Post-Election Rally. But Why?
- Summary: JPM stock fell, erasing post‑election gains, indicating market volatility and investor uncertainty.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQMXJFekNOaWVaVFd6WW5BdldQU05QUk5ldURDV196SXZGTUQ5NG9aMUtvWmhLeGRoaHYtTnk0ajBYOS1mcU9DeVFXTEtOM3BlR1ZCZGZ3NEhKSHhGbVF1QVh1VWRKTTdaM2p0RHZqanBWekpRTG1heGFVdXJ1Q29qcWdRWG51MS1pc05YV3pMZnpGb3RUaVU2ZjdB?oc=5>

### JPMorgan Chase & Co. $JPM Stock Holdings Raised by GRIMES & Co WEALTH MANAGEMENT LLC
- Summary: GRIMES & Co WEALTH MANAGEMENT LLC increased its JPM holdings, indicating confidence in the bank's prospects.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxPVEVfTDVFVjBSZ1JLTVRoaUlOT0NIMFdxNmdlSXBFWmxLMnpBcXcta2NyTXJ5VEVsc3U0bEQ0eExrWkpkSkhKM1FxUGNOWWc0a29uRzhUZzIteUM3OWZBdllTZWd4NmIzYTNjbUgwWlhDVjI5LWJxWEs0S0N4czdKSHhhYlVDTGxiZzRzMjVVLVI2SU5ObUV3cnY0cTU5MjYzemlqREFZei1iV0tsQTJCanZscnoydUh0ZVYzTkFCWE5Taml5ZWpNN2QxQ1JvbGxRMUUxall3?oc=5>

### JPMorgan Chase & Co. $JPM Stock Holdings Raised by Nippon Life Global Investors Americas Inc.
- Summary: Nippon Life increased its JPM holdings, indicating confidence in the bank's prospects.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxNMFFqa3FHNU1CWlFPX0pzZUZacGViM0VJV0V4a0JVcnpLRFREa2FGeklJMU5MQkFSOWIwWFFOYVZrR2dSQi1BSVB4Q01IZXJOcGtEUkJDc0hLanRGZ0h2VUxRbWR4STAxNVVvU242VUNIVWJkUUVubV9kWVNsV1hTblBobFZPM2ZfWTFSbmVzYk1ab1hMVVRlWHV2eVBtRzh5Z3YybmhiSjFtQ216WnVwOEJUSTdJdDBzaGdaR2s0M1l3dmJUMEF1OXZFR3lUaE9GQzdhczN6ZFd1UW9OVWNfRUhPQQ?oc=5>

### 5,740 JPMorgan Chase & Co. $JPM Shares Sold by Coerente Capital Management
- Summary: Coerente Capital Management sold 5,740 JPM shares, a modest divestiture with limited market impact.
- Date: 2026-11-08 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPN0V2RjVUZkREdk1jQ1VubHNUUGtLY2xhcG1ER2hFcmwzVEhWQ3F5c1JYT2x1VFNHNDdLaUZiSGxsOUtrSFZKR1RPU0tfczc2ZEhmaVR2LTlJWl91VU9LRGptdEltZlNqQV9nOFFaRktmLW9yMlFGN3ZKWU9PSzM1UlVFT3V0NmQxb294b01GajlZczZ1R3hsc0thQ2xjby1HNm9iREp1N3RIV1V0R3UtQ0o2VFZ2aGxGaHRYVjJPTVRqQUZuVU4zRGpn?oc=5>

### JPMorgan Chase & Co. $JPM Stake Lowered by Parr Mcknight Wealth Management Group LLC
- Summary: Parr Mcknight Wealth Management Group LLC reduced its stake in JPMorgan Chase, indicating a potential shift in investment strategy.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxNSzRraGFGYXF6VUozYzZEeng2YlFKQjV5ZmtpckpCazR3QXZ5aDhmdFlfc3phc2xQWTFPbkROQWdJVV9mRmZ3cy1CclduWXZPUjNvdmNibUEtQ05vT0Fld1hEZzRBeXFnR0kxT1k5dVVpdWFLZVh3RGRzdnFXSm1RQnpYWk5UcU1iblJjVjAzdml6dHRpYUxQUGQySkdmR1NENHB3ZHZYVFF5bEc0dzI5VnUycEQwSzB4amN6cnB2amItN1gzYnQwTFpTelBFSi1yV2l5NHJXeVc?oc=5>

### First Nebraska Trust Co Makes New $12.96 Million Investment in JPMorgan Chase & Co. $JPM
- Summary: First Nebraska Trust Co. invested $12.96 million in JPMorgan Chase, expanding its holdings in the bank.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxQMzF2TE02UmlpR2wzMmRsaGl4MW1GT2VsYTdyTFBvQThIOTlaZDJlVUNUWUdCajM0RmhrTng1LUU3RTZNUi1DR041aVVuUXVraFlrZVRVdW8zRUt4RUExOWJ6Y1JmTGt4d1dlRktFNnFNeUc1MEFrbXNKOXJtUlF4VGFMc0RaZ01oZ3hoSlFaXzB3Vld5TDczNXBfa2FjbUNGNWdGWVhzY0tha3JPVnZDTExVbk5XZmV4OXQwNFF2ZkUtZ19RYU8yY3daUjZJdENLS3dRb09XWjJFNWs?oc=5>

### Associated Banc Corp Buys New Position in JPMorgan Chase & Co. $JPM
- Summary: Associated Banc Corp acquired a new position in JPMorgan Chase, increasing its exposure to the bank.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPd2VzMDJPLUlsSEkwdF9Yc1BLNE9Na1UzVDZTME4wYjhKNldjNlprWGZwZ1BVR1pEWmU5SU1tQnNIQzlnWUozcnFTczBSbGd4NjA0UEZUb1BQT0Jld1YxMzRza2FnZ2c0TG9mc19ycFRkU3lfajNjNDliUzQxNWhidktZR1hhcVJOOVlVVmxhYlUwM01CblVrTktaSFM1amk3M0hjWk1vemJPYy1GQXNyOE83MS1WbW1TTllMWWdnOUhoQQ?oc=5>

## RISKS

### JPMorgan Chase & Co. $JPM Stock: Summit Wealth Group LLC Co. Boosts Stake
- Summary: Summit Wealth increased its JPM stake, potentially signaling confidence but also raising concentration risk.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQbGJiMWhTQTVnVjBFRHlkcU9pWTBxWVMyTGtHMkZJOU5KaW5sWEJQeDNSVElObmhTZzNlbVhiS0Y5SlBFRHlIWnE0WVRZVmNQLXk1S1Jsc29EMHBLMUJMOW0yNkY2YXJWaGhKaUNmVkhZLXlRYjUwamZ6aXBpXzVNOHVneUQ3Z3BwWHdFcVlDa0h0NHJXRUxZYk5RNDlsMFljRXNVTG1IVVowSVlrYmFXNDVvcVZUNmZJOWs1WkJlbmM2Y1ZaeFlv?oc=5>

### JPM: SEC Form FWP filed by JP Morgan Chase & Co.
- Summary: SEC filing may raise regulatory scrutiny, potentially impacting operations.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNZzZ5dXdieDk2aF93S1FRZEJ2MEdqaENuVXZXeVBXRjVGVm5XeVQ2U3VEcksyS211WFJyNUtZVkRCOWxvS0QtTlFTbEwxZDhoTm50SDFVcU9ZdHAxYlFteE5tVDFEX21mZS1TN3Q4em4yVHl5amd2WE1OLUNuRS1IdDBKa2htd0Vfc1RV?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **14.35** | **2.59** | **N/A** | **10.20** | **908,430,868,480.00 USD** | **10.97** |
| BAC | 12.06 | 1.29 | N/A | 3.40 | 348,805,562,368.00 USD | -2.96 |
| C | 11.89 | 1.06 | N/A | 8.00 | 201,885,286,400.00 USD | 23.52 |
| WFC | 12.06 | 1.62 | N/A | 0.40 | 256,628,178,944.00 USD | 1.60 |

Peers fetched as_of: 2026-11-09; JPM reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

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

- https://news.google.com/rss/articles/CBMi1AFBVV95cUxPV21ST25Bejhhc3ZadlJGYkV1MlhzQ2l2b3dfRTZCbW1IZE90ejVRRWprWmNLU3ctQ1RvOW1BdHVPNFRXQTdaamZVUW8wdGl3NnZMZGJwSXFrSlY1cU9oUEFIT25RNG50Q0s1RUQzdzBLMThDVjY2dWVWNDRXeDZWZE52SFRNUEhFZ1lBTjExTUtFT01KQlA2S3k1dncycmdiblR1aDFQazdCMVdzTzhiU3c1bm9mVlFScG1yZ1hXSzJERVo5d2I2N05fWXpWVlQ2TVJ5bQ?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxNSlh5b2xBZU1OSHJqVjkzN2lrM2ZyOVpkbklGcHpvaVVGQjFhOFNkWUdYbmxlYTVtTGhKSjZZSVVyOEotVzE0NFp3VUk2XzE1bm5qNXFlbTlMWGg5ZFMyU0RmUFlDVjl1Vk1pc2VHMTI4d29MQVZfa0poa1dUd0UxQVpaZGZTVjJybUdSRlV0WTNhdDEtTXR1d2ZCQUY4NDh5ODRfX2p1OW9OalhqeHZod3NWRnRObFVJRmV0OEhfMjJLZXE5SU1YSENYc3FvLVE?oc=5
- https://news.google.com/rss/articles/CBMinwJBVV95cUxQRDNicXhjOHZJalM5UnNmZDFDdTdkc0lvLXduVE1pTGVhNkhDMGZxM2RpM2Q5Z3hpOTdGQkhyQTVSZkJ1UzRXTGVlNF9hRFJ0UTBsVmRnaUw4QlZHTHJBcC1mckNNOWRGUW5Qd21DY2xxVmMzZWQwUzJLdlBuNFRsaVBJT29mVGxzbExRM3VjbTNfSEdqcF85S2M4U2dJcnowblJXS2N4b05JZmQwU0ZCdF9nQmhsV2ZyZHVtVEJsVnRHRlV3enUwLXFhTVFSNTFMVXNfcUJLNXlhNDBNelVjUXZWZ0J5cjRkc21RRHlUc0RQcm9OcGlaNi14Z1RBM0dWVVNveGxQT3pHQkdzUGs0YmNyeFU2MWs5bWNOV2NFQdIBpAJBVV95cUxOS3BsWloxMFpFOWtyaHdrTThNZ0c4VkRFNGZxT0FLMVFSZDVQblBUZ3hPTUlILUJRRFozcHRwdEdJT3lWaFNEN0hJQWRpMk0tMVZZNVJTRU1fZzhSWnlSRkQ5SzViZTdLRVZWVWRMX2ZnVm05Mk1CVHZzdS0yUks2eWxKZWJfRk5zS2VmSmJxeTNndjJRQU1WZWoxV3Y2V0cwdFNLSGxRRFphU0NzSUJiTkxXeW1BTU1UajNnblJmVG5uTkgtTVZBMGFDNW85VUsyRlpYLXJQRlFkaEJOX0lONFJUOUpoTUtXRkxLemc0Y3JMUnhWVEJNa3NmMW5FSjNDUDFycWVNQnYxLUhBTWFucl9tRmpkOEQxUnFRTjBRczNfQnpC?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOZXhoQjJxaGViV0VDeGlvUURGODN6T25jcXhzT2h3V0RBdGxPS1VkRnNkTm15bFVfTDZuLUV2SWlGUjhPdnQycmY5a3dyUWVwZ3hHdWtoNDVIRWVRMlhlT1RVdVlUOXpPTEc0LW8xZW5kUjdaVkpEb2swLXZyQjZLQjhvdDlZcmxVdVFYZHBqZnlfLUFGUmVpQTZYVEpXZlJIQzNyd0VhQmtoTmY1elhBaGlWSU8wNWQyMkFpNXpZQTVBZ9IBxwFBVV95cUxNcU1HZFdGSEF3QmdnOE5aakFpYTBCcVRJaVM4QXpjZVQ5ZkhmMVN3MjFidllOUHRPX3hlcnNnUEJXdmtUbjU3alh5WGpfMTdUam1GamppM085VGVTTG8tVm9vMEQwWThfUEs2ZkhfejFvV2ZLQlNpc1d1UUxHcGdQVjgxWjJOUXJyMnZsaXEyVC1LcjE5ZFVyUWlnUDdEbDgtOWpiTmo1d3FZbHhPMjVQSzRINjhVR2tlZkJyaklKM19XbGs3a3k0?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQaGlWMXljWGtsTDNTQzZWNzBGNi12QVJQbTFMS1VyUFo5R2l5QVZZUEVGUWNtNmE1UUd6bWRqU3hNWGVidWFNbnpYYktDMjFsZUZlbXpXUTRNQmxPei1CVFdHWjk5M0tmaUFWaHEwVGhscVRUTzV2SklnSVVObE04M0xQSkFYMmVwVHpsSTFlTjFjUFY1eHB6dWdielU?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPVTNqRHRxb0VJWl9velJGajJDS1JadTFCMDQ1b0dnSS1QeEtEZUZhdnViQ2pJQUZKSkxXU0Y5dlNzZXo1bW85VnE2Mi0xaWlYZ01pNnF5dGktQnA1cVpQYVMyV0luR2NubDJSM1NyZDM3OUw4dkFPeE5xVEhlXzBwRXhUNlQ4WVNvQVE?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQSnBNeVhaelpNUWNLUzZ4TU91blhhWHVjX1lNRjc0cHY0UU5fcU44RlZLY3ZJVGZzM1R2dVZoakRGcGNsRUM4eWRKVjlsQy1oT1JwYkt3dk9uOW5CSXduakhDYmlkM1pCLVBKTzdfZ3U3dERERDF6eXZLTGFLb3RES1ZVaUs5cHRiZVYtYWxISQ?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxQOEhkdEhBTFZVSDFWUEtLcmhkc1FlMlpESWlJeVFJZ1E0VzBIVnBVR213c2dNUllmeFB4UWNyVUtULWs0OGFlTW5MRFVvUVhQSUdPT2N3VlhMRXR6R1Zmb0g5SUdxUkxiS3k2cmkzaGl3OURMMkpXWjlIbVdMR2lSZzJFRk5GNm5HWDdKYldaLTlPNmZhekJuTnMtWGZjWWNvS3VVdGxzdXNDQmZLM25QWE9QcTdtdktxaWtaRDh1b1VtRHFXS1FnWG1jaXNkSnRf?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxNZnNYeUVUZEhzcU42bzVZYklGd2NkQWJjRG5kYmxFOEFvcWtNdXE0ZXZVV2RyWHdfbUhHUkNlNVg3YzZId0tlMFh2TUtXTGgzSjFoUHBlRU1GazVzZlNFbV9wcVEwV3JSakNwamQ4RkF6RTA1TVp2R0xLb05RNGlDdTVqb0JXbF9zRkVrYzhmSDdpZkcxb3F5LXVIcy1DTl93SkZCRVBnQzJ0VVc3eFZXT2x0am5Fc2FVZWR6UFZ1NVZEZlFfRkw2cVg3Z2hKaVF4?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQZjNsYmtiazRCZTluMmhBYlMxSUkyaEhObzdMWFpYcUNyTWVrLTVOUUZ0MWUxQldpemEzX1BNcEN2RVVjSlpkRXFTRXZQZkRpcVQ0TkFRQUVDMW9PaWdFRHVIdXlMMHBWQk5yV2xBemlFVHgtdlF3aU83RnBaTGlfV0sxcW9YaHQydzk3ZFJvRGQ5MUZuc3VyWkhmZmRKQTJpTEcyanFlTWNkOFZrQ0dhalEwaC0?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPMXNySVJDRkZWNVEzc2pYWXE5MUdpNUptYzVkRXBTLVRNMkJtSXZGR2lRNmlVQXNQSmNkb2dZWkNZODhlSll2V004Q0ZhejZqR3dZM0hFWEp5QndOSDUtb0M2NHRJemc1WjVLSVN3OVdHc2p0alFZWWVyYzBiTGR2N1V0QzNnVlh6eHZ0M2ZHZE5SczdUZHN3Y1hLOXpFMmc3c0JpOVZkX2FpRTFrQl9EVw?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQTW1LNDZzRXRoVFQwdVlsaVFqRGN2Rk9oZDlsM0UxREgzcVdXeVBYZEpZbEJHRGxhZl9wX1RRZDhVRUlpM0pnRU5GNTFxUXRseXBkMHJHaVZRdWNLcHBTZWxmQ2NjekxnVzFObEZ3aTFzQ3BhVExGSkxJVW1CVEw2T1ZuS3Rkakp6NWxmVTZDYTRObHNJZlIyV0pXdjdsdXhfSUMtRzVZQkxYV2JNN1M4dUNJY1NMaXZYMzZscDZ3?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNU2ZMaTZDY3FVcms0QmZ4SGg5a1I2WThhNnFranpEUGxldDZHSHh5UHU2ZFNraHhuT0dBLTlBeFQ0TkVDYk0yazkyZDJoTk1XWmJRRWd0YTdIWm9yOXkwZ1piVGZXNEtKOGRiZlhTQTd2UjdHUjBmelBVRFkzbjdRd3l1WTltZGlqS2EtSEZNX2M2d1BEWE9rdjE2andiZEQ0a09WUUgybkxyeGtjdlZDSHNoUHgwVlhiR2tZcW9uZnM?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQMXJFekNOaWVaVFd6WW5BdldQU05QUk5ldURDV196SXZGTUQ5NG9aMUtvWmhLeGRoaHYtTnk0ajBYOS1mcU9DeVFXTEtOM3BlR1ZCZGZ3NEhKSHhGbVF1QVh1VWRKTTdaM2p0RHZqanBWekpRTG1heGFVdXJ1Q29qcWdRWG51MS1pc05YV3pMZnpGb3RUaVU2ZjdB?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxPVEVfTDVFVjBSZ1JLTVRoaUlOT0NIMFdxNmdlSXBFWmxLMnpBcXcta2NyTXJ5VEVsc3U0bEQ0eExrWkpkSkhKM1FxUGNOWWc0a29uRzhUZzIteUM3OWZBdllTZWd4NmIzYTNjbUgwWlhDVjI5LWJxWEs0S0N4czdKSHhhYlVDTGxiZzRzMjVVLVI2SU5ObUV3cnY0cTU5MjYzemlqREFZei1iV0tsQTJCanZscnoydUh0ZVYzTkFCWE5Taml5ZWpNN2QxQ1JvbGxRMUUxall3?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxNMFFqa3FHNU1CWlFPX0pzZUZacGViM0VJV0V4a0JVcnpLRFREa2FGeklJMU5MQkFSOWIwWFFOYVZrR2dSQi1BSVB4Q01IZXJOcGtEUkJDc0hLanRGZ0h2VUxRbWR4STAxNVVvU242VUNIVWJkUUVubV9kWVNsV1hTblBobFZPM2ZfWTFSbmVzYk1ab1hMVVRlWHV2eVBtRzh5Z3YybmhiSjFtQ216WnVwOEJUSTdJdDBzaGdaR2s0M1l3dmJUMEF1OXZFR3lUaE9GQzdhczN6ZFd1UW9OVWNfRUhPQQ?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPN0V2RjVUZkREdk1jQ1VubHNUUGtLY2xhcG1ER2hFcmwzVEhWQ3F5c1JYT2x1VFNHNDdLaUZiSGxsOUtrSFZKR1RPU0tfczc2ZEhmaVR2LTlJWl91VU9LRGptdEltZlNqQV9nOFFaRktmLW9yMlFGN3ZKWU9PSzM1UlVFT3V0NmQxb294b01GajlZczZ1R3hsc0thQ2xjby1HNm9iREp1N3RIV1V0R3UtQ0o2VFZ2aGxGaHRYVjJPTVRqQUZuVU4zRGpn?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxNSzRraGFGYXF6VUozYzZEeng2YlFKQjV5ZmtpckpCazR3QXZ5aDhmdFlfc3phc2xQWTFPbkROQWdJVV9mRmZ3cy1CclduWXZPUjNvdmNibUEtQ05vT0Fld1hEZzRBeXFnR0kxT1k5dVVpdWFLZVh3RGRzdnFXSm1RQnpYWk5UcU1iblJjVjAzdml6dHRpYUxQUGQySkdmR1NENHB3ZHZYVFF5bEc0dzI5VnUycEQwSzB4amN6cnB2amItN1gzYnQwTFpTelBFSi1yV2l5NHJXeVc?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxQMzF2TE02UmlpR2wzMmRsaGl4MW1GT2VsYTdyTFBvQThIOTlaZDJlVUNUWUdCajM0RmhrTng1LUU3RTZNUi1DR041aVVuUXVraFlrZVRVdW8zRUt4RUExOWJ6Y1JmTGt4d1dlRktFNnFNeUc1MEFrbXNKOXJtUlF4VGFMc0RaZ01oZ3hoSlFaXzB3Vld5TDczNXBfa2FjbUNGNWdGWVhzY0tha3JPVnZDTExVbk5XZmV4OXQwNFF2ZkUtZ19RYU8yY3daUjZJdENLS3dRb09XWjJFNWs?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPd2VzMDJPLUlsSEkwdF9Yc1BLNE9Na1UzVDZTME4wYjhKNldjNlprWGZwZ1BVR1pEWmU5SU1tQnNIQzlnWUozcnFTczBSbGd4NjA0UEZUb1BQT0Jld1YxMzRza2FnZ2c0TG9mc19ycFRkU3lfajNjNDliUzQxNWhidktZR1hhcVJOOVlVVmxhYlUwM01CblVrTktaSFM1amk3M0hjWk1vemJPYy1GQXNyOE83MS1WbW1TTllMWWdnOUhoQQ?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQbGJiMWhTQTVnVjBFRHlkcU9pWTBxWVMyTGtHMkZJOU5KaW5sWEJQeDNSVElObmhTZzNlbVhiS0Y5SlBFRHlIWnE0WVRZVmNQLXk1S1Jsc29EMHBLMUJMOW0yNkY2YXJWaGhKaUNmVkhZLXlRYjUwamZ6aXBpXzVNOHVneUQ3Z3BwWHdFcVlDa0h0NHJXRUxZYk5RNDlsMFljRXNVTG1IVVowSVlrYmFXNDVvcVZUNmZJOWs1WkJlbmM2Y1ZaeFlv?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNZzZ5dXdieDk2aF93S1FRZEJ2MEdqaENuVXZXeVBXRjVGVm5XeVQ2U3VEcksyS211WFJyNUtZVkRCOWxvS0QtTlFTbEwxZDhoTm50SDFVcU9ZdHAxYlFteE5tVDFEX21mZS1TN3Q4em4yVHl5amd2WE1OLUNuRS1IdDBKa2htd0Vfc1RV?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPaTMtNEFMY3ZsSVZfSkxaWkdiSGZpcVRPWkNnRmVwMEY0RDJSenRkbTdMbW05RkpQWUZJNUd2ZXVBMDdXTnNpNDBjVmQxLTZuTE9nYkJBS1Y1X00tTy1GQ1FpMXQ5dGU0UjFKaUVYWTB4R3Y1X0dvMlpwSkhQSVdaUVZRQ2E1aHpFR1Jn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
