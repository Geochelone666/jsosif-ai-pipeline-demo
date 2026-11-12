# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T06:02:16.224797+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 9, 'ai': 10, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/JPM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 6 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 66.67%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 343.3900 |
| Return 1D (%) | 0.3859 |
| Return 1W (%) | -2.4765 |
| Return 1M (%) | 3.1232 |
| Return YTD (%) | 8.6226 |
| Return 1Y (%) | 10.8940 |
| Annualized volatility (%) | 23.0058 |
| Beta vs SPY | 0.8056 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.5663 |
| Downside deviation (rf=0, %) | 16.5640 |
| Sortino (rf=0) | 0.7865 |
| Historical VaR 95% (1D, %) | 2.4515 |
| Historical ES 95% (1D, %) | 3.3955 |
| Correlation vs SPY | 0.4807 |
| Tracking error vs SPY (%) | 20.3488 |
| P/E (trailing) | 14.40 |
| P/B | 2.60 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 13.43 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 44.79 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 340.2180 |
| Close vs MA50 (%) | 0.9323 |
| MA200 | 321.9823 |
| Close vs MA200 (%) | 6.6487 |
| RSI (14, Wilder) | 53.9727 |
| MACD (12,26) | 1.0445 |
| MACD signal (9) | 0.2845 |
| MACD histogram | 0.7600 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 343.3900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.3859 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.4765 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.1232 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 8.6226 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 10.8940 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 23.0058 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.5640 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.7865 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4515 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3955 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4807 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.3488 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8056 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5663 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.4278 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.7880 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.4039 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.9727 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7600 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.9323 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.6487 -> Clearly above the moving-average trend level.

## TAILWINDS

### JPMorgan Chase & Co. (JPM) is Attracting Investor Attention: Here is What You Should Know
- Summary: Positive investor focus on JPM, indicating potential upside.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNZEdSeWY5RUlCZ3QxZklmQ2hsTGJXdHdxU3hXQXkxQUJCZXJaMlpMYkc4SEtubncteGpGVVIxcWFtV19RdWF2bDNSQmY5UC1aVUo5U1NmQWRpSjlnWW1OUWRhMWdyb191VS1LV2g1QTZUTTFmR0hPXzQwU3pzbndINnJhU19xN0FtQ1pQR2xCN20wbTI4YnhyWi1EazJjdw?oc=5>

### JPMorgan Chase & Co. $JPM Stock Position Raised by Bank Julius Baer & Co. Ltd Zurich
- Summary: Bank Julius Baer increased its JPM position, indicating confidence in the bank.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxPV21ST25Bejhhc3ZadlJGYkV1MlhzQ2l2b3dfRTZCbW1IZE90ejVRRWprWmNLU3ctQ1RvOW1BdHVPNFRXQTdaamZVUW8wdGl3NnZMZGJwSXFrSlY1cU9oUEFIT25RNG50Q0s1RUQzdzBLMThDVjY2dWVWNDRXeDZWZE52SFRNUEhFZ1lBTjExTUtFT01KQlA2S3k1dncycmdiblR1aDFQazdCMVdzTzhiU3c1bm9mVlFScG1yZ1hXSzJERVo5d2I2N05fWXpWVlQ2TVJ5bQ?oc=5>

## HEADWINDS

### JPMorgan Chase & Co Stock (JPM) Moved Down by 3.50% on Nov 5: What Investors Need To Know
- Summary: JPM stock fell 3.5%, reflecting short-term market pressure.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPVTNqRHRxb0VJWl9velJGajJDS1JadTFCMDQ1b0dnSS1QeEtEZUZhdnViQ2pJQUZKSkxXU0Y5dlNzZXo1bW85VnE2Mi0xaWlYZ01pNnF5dGktQnA1cVpQYVMyV0luR2NubDJSM1NyZDM3OUw4dkFPeE5xVEhlXzBwRXhUNlQ4WVNvQVE?oc=5>

## CATALYSTS

### JPMorgan Chase & Co. $JPM Stock Purchased by Pzena Investment Management LLC
- Summary: JPMorgan Chase & Co. $JPM Stock Purchased by Pzena Investment Management LLC
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxOaFl2RkI1UFFYazZjSHdRTDJpcjZFMFRSRTktWWtPQkJFSUJtZDU0aTZjZnh5MjVkRTBsREJYZHJLbVlId0VPa3pfLXNQZ3FNVEdUdjYyUWdOVExlZEFLem42dXRqbkRMQm5IdG1iN2wxdkxPeEFHR18xd0RzLUpOZkU0LV93bU9CYWJ3Q1JYLTE3UWd2SDYwVzBtNDN5SFdjNWg0X0tQTjdGemFQT2NQekpUejE5NHNsMHVtb0c5amZ3YmpjbldGSE1JVjB2Zw?oc=5>

### JPMorgan Chase & Co. $JPM Stock Bought by Greenleaf Trust
- Summary: JPMorgan Chase & Co. $JPM Stock Bought by Greenleaf Trust
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQZjNsYmtiazRCZTluMmhBYlMxSUkyaEhObzdMWFpYcUNyTWVrLTVOUUZ0MWUxQldpemEzX1BNcEN2RVVjSlpkRXFTRXZQZkRpcVQ0TkFRQUVDMW9PaWdFRHVIdXlMMHBWQk5yV2xBemlFVHgtdlF3aU83RnBaTGlfV0sxcW9YaHQydzk3ZFJvRGQ5MUZuc3VyWkhmZmRKQTJpTEcyanFlTWNkOFZrQ0dhalEwaC0?oc=5>

### JPMorgan Chase & Co. $JPM Stock Sold by Inscription Capital LLC
- Summary: JPMorgan Chase & Co. $JPM Stock Sold by Inscription Capital LLC
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNbExVV3pHMzk2ZEFxMjAtbldSOEphR2xCMDJWWEdlYkl4MTRHdGE4LVNTeDk0MFBESUVMMEhVUEx4SHhLVkFtTEMwbzB2eThRRjNDZWt5ZERzek9xQlRLUjZSRXlXLWp5ZEEtMlVVY0ducnQ3VWxiR0VGTTBTZVZiUzA1OWRPcldHNU5xT2VnaXkzX1M4NFE2Sjh0dXFPWVU4MVlmZ09nZnJ4OE1vMTZ2NWF1RklXQzNEdWVCZg?oc=5>

### JPMorgan Chase & Co. $JPM Stock: Provenance Wealth Advisors LLC Raises Holdings
- Summary: JPMorgan Chase & Co. $JPM Stock: Provenance Wealth Advisors LLC Raises Holdings
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxQOEhkdEhBTFZVSDFWUEtLcmhkc1FlMlpESWlJeVFJZ1E0VzBIVnBVR213c2dNUllmeFB4UWNyVUtULWs0OGFlTW5MRFVvUVhQSUdPT2N3VlhMRXR6R1Zmb0g5SUdxUkxiS3k2cmkzaGl3OURMMkpXWjlIbVdMR2lSZzJFRk5GNm5HWDdKYldaLTlPNmZhekJuTnMtWGZjWWNvS3VVdGxzdXNDQmZLM25QWE9QcTdtdktxaWtaRDh1b1VtRHFXS1FnWG1jaXNkSnRf?oc=5>

### JPMorgan Chase & Co. $JPM Shares Sold by Commonwealth Equity Services LLC
- Summary: JPMorgan Chase & Co. $JPM Shares Sold by Commonwealth Equity Services LLC
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPUWhVX2dlNUtJaHlFMFdWakwyVVZZSXM4S1J2QUl2ZWVNeTBVUlE4VHVXMHRoRWNvcW1LNDB2UGhZNEZvRmVlcHhBMDJJV1Fwcl9SX2dHUExUQVpUNmgxSU1rdGNOdFFQZHdqYmlqMGxXekc3elRJV3JkTmxnSWFmZUV6aVYwTXNBeFJxUjBJb1NjXzFGX3FzQjdGYkdHQk5iMWNYMWNhby1QVHRPU1FvRXl1NXJRS2pyXzVDdkJ6Y3hJQVdzLVVIR213?oc=5>

### JPMorgan Chase & Co. $JPM Shares Sold by AIA Group Ltd
- Summary: JPMorgan Chase & Co. $JPM Shares Sold by AIA Group Ltd
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPMXNySVJDRkZWNVEzc2pYWXE5MUdpNUptYzVkRXBTLVRNMkJtSXZGR2lRNmlVQXNQSmNkb2dZWkNZODhlSll2V004Q0ZhejZqR3dZM0hFWEp5QndOSDUtb0M2NHRJemc1WjVLSVN3OVdHc2p0alFZWWVyYzBiTGR2N1V0QzNnVlh6eHZ0M2ZHZE5SczdUZHN3Y1hLOXpFMmc3c0JpOVZkX2FpRTFrQl9EVw?oc=5>

### JPMorgan Chase & Co. $JPM Shares Acquired by Rakuten Investment Management Inc.
- Summary: JPMorgan Chase & Co. $JPM Shares Acquired by Rakuten Investment Management Inc.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxNZnNYeUVUZEhzcU42bzVZYklGd2NkQWJjRG5kYmxFOEFvcWtNdXE0ZXZVV2RyWHdfbUhHUkNlNVg3YzZId0tlMFh2TUtXTGgzSjFoUHBlRU1GazVzZlNFbV9wcVEwV3JSakNwamQ4RkF6RTA1TVp2R0xLb05RNGlDdTVqb0JXbF9zRkVrYzhmSDdpZkcxb3F5LXVIcy1DTl93SkZCRVBnQzJ0VVc3eFZXT2x0am5Fc2FVZWR6UFZ1NVZEZlFfRkw2cVg3Z2hKaVF4?oc=5>

### JPMorgan Chase & Co. $JPM Stock: ProShare Advisors LLC Cuts Stake
- Summary: JPMorgan Chase & Co. $JPM Stock: ProShare Advisors LLC Cuts Stake
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQTW1LNDZzRXRoVFQwdVlsaVFqRGN2Rk9oZDlsM0UxREgzcVdXeVBYZEpZbEJHRGxhZl9wX1RRZDhVRUlpM0pnRU5GNTFxUXRseXBkMHJHaVZRdWNLcHBTZWxmQ2NjekxnVzFObEZ3aTFzQ3BhVExGSkxJVW1CVEw2T1ZuS3Rkakp6NWxmVTZDYTRObHNJZlIyV0pXdjdsdXhfSUMtRzVZQkxYV2JNN1M4dUNJY1NMaXZYMzZscDZ3?oc=5>

### JPMorgan Chase & Co. $JPM Shares Purchased by One Way Holdings LLC
- Summary: JPMorgan Chase & Co. $JPM Shares Purchased by One Way Holdings LLC
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNU2ZMaTZDY3FVcms0QmZ4SGg5a1I2WThhNnFranpEUGxldDZHSHh5UHU2ZFNraHhuT0dBLTlBeFQ0TkVDYk0yazkyZDJoTk1XWmJRRWd0YTdIWm9yOXkwZ1piVGZXNEtKOGRiZlhTQTd2UjdHUjBmelBVRFkzbjdRd3l1WTltZGlqS2EtSEZNX2M2d1BEWE9rdjE2andiZEQ0a09WUUgybkxyeGtjdlZDSHNoUHgwVlhiR2tZcW9uZnM?oc=5>

### JPMorgan Chase & Co. $JPM Stock Holdings Raised by GRIMES & Co WEALTH MANAGEMENT LLC
- Summary: GRIMES & Co WEALTH MANAGEMENT LLC increased its JPM holdings, indicating confidence in the bank's prospects.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxPVEVfTDVFVjBSZ1JLTVRoaUlOT0NIMFdxNmdlSXBFWmxLMnpBcXcta2NyTXJ5VEVsc3U0bEQ0eExrWkpkSkhKM1FxUGNOWWc0a29uRzhUZzIteUM3OWZBdllTZWd4NmIzYTNjbUgwWlhDVjI5LWJxWEs0S0N4czdKSHhhYlVDTGxiZzRzMjVVLVI2SU5ObUV3cnY0cTU5MjYzemlqREFZei1iV0tsQTJCanZscnoydUh0ZVYzTkFCWE5Taml5ZWpNN2QxQ1JvbGxRMUUxall3?oc=5>

### JPMorgan Chase & Co. $JPM Stock Holdings Raised by Nippon Life Global Investors Americas Inc.
- Summary: Nippon Life increased its JPM holdings, indicating confidence in the bank's prospects.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxNMFFqa3FHNU1CWlFPX0pzZUZacGViM0VJV0V4a0JVcnpLRFREa2FGeklJMU5MQkFSOWIwWFFOYVZrR2dSQi1BSVB4Q01IZXJOcGtEUkJDc0hLanRGZ0h2VUxRbWR4STAxNVVvU242VUNIVWJkUUVubV9kWVNsV1hTblBobFZPM2ZfWTFSbmVzYk1ab1hMVVRlWHV2eVBtRzh5Z3YybmhiSjFtQ216WnVwOEJUSTdJdDBzaGdaR2s0M1l3dmJUMEF1OXZFR3lUaE9GQzdhczN6ZFd1UW9OVWNfRUhPQQ?oc=5>

### JPMorgan Stock Loses Over 100% of Its Post-Election Rally. But Why?
- Summary: JPM stock fell, erasing post-election gains, prompting questions about causes.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQMXJFekNOaWVaVFd6WW5BdldQU05QUk5ldURDV196SXZGTUQ5NG9aMUtvWmhLeGRoaHYtTnk0ajBYOS1mcU9DeVFXTEtOM3BlR1ZCZGZ3NEhKSHhGbVF1QVh1VWRKTTdaM2p0RHZqanBWekpRTG1heGFVdXJ1Q29qcWdRWG51MS1pc05YV3pMZnpGb3RUaVU2ZjdB?oc=5>

### JPMorganChase backs training to help veteran-owned businesses compete for federal contracts
- Summary: JPM Chase supports training for veteran-owned firms to win federal contracts.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNYk5WT3NFSVRIRElaYVFlYXdrcHAteGxRUzRYYWxDaDFoVDl2VFVLVzZpUGYxSVVRX2hWZ3JyZS1sbWU2cHVTVFdaS0xuQzh4OWZHRWFua0xKSmdfOFEyMlNCTWtVN21QQzVfdTdzZEJTOXFEQVRKa19oR3RYeUd2cVpvSjNWekdrQmxnWmpxazFBLWlrbVl6TlZVRnlOYzBvRzdfVTZhZzdPblNHOENDbFFxbndETU1QN0tmTA?oc=5>

### Legacy CG LLC Sells 4,507 Shares of JPMorgan Chase & Co. $JPM
- Summary: Legacy CG LLC sold 4,507 JPM shares.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNbFc1MFFIOWJNODdEVnEzWG5KZF9YUWdOLXZUeGNsbWVDMGxxNnJ6V1ltajhwejgycmhNa0lUUG1iRUpGM2NCN1B0Q0VsYl9aaS1tUEd4d0NWSndIOTlGYUQyQmVqVHlpMl9wekhCTDg1WmJRckxJMzlHZW91YUZad0liZXpUamV1b0RiZmtkRTBxSnRKNkI0dUl1bUM2X3lBcTJHbF8tT1pWY21MdVRnTE1xOEtMYXpp?oc=5>

## RISKS

### JPMorgan Chase & Co. $JPM Stock: Summit Wealth Group LLC Co. Boosts Stake
- Summary: Summit Wealth increased its JPM stake, potentially signaling confidence but also raising concentration risk.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQbGJiMWhTQTVnVjBFRHlkcU9pWTBxWVMyTGtHMkZJOU5KaW5sWEJQeDNSVElObmhTZzNlbVhiS0Y5SlBFRHlIWnE0WVRZVmNQLXk1S1Jsc29EMHBLMUJMOW0yNkY2YXJWaGhKaUNmVkhZLXlRYjUwamZ6aXBpXzVNOHVneUQ3Z3BwWHdFcVlDa0h0NHJXRUxZYk5RNDlsMFljRXNVTG1IVVowSVlrYmFXNDVvcVZUNmZJOWs1WkJlbmM2Y1ZaeFlv?oc=5>

### JPMorgan Chase & Co. $JPM Stock: International Assets Investment Management LLC Decreases Stake
- Summary: Large investor reduces stake in JPM, potentially signaling negative sentiment.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxOOTV1d0hOSlBSTEdtR0NUTFo1aE5QMkYxeDZSdWhtdVQ4dVpmbGNiMTdZakpQZ0JMeXIzVS1kQWxBMGlEeFM5OUpmVEo1dTJJdWZzMFpOVWVxSDY2aV9UWXo0bnNZV2ttZzhXLUdpNXpqUFJUelBwY2t4ZHBQWnhJVEVnMkdpOFdWWlQwaFppdENEdFBSajdGSWdMTjZQbUtySnV2bDZzM2dIcW9tZFJhRndaa3NSNmktbWc0TGVUOTNsWWVhS0dtbjZiaXFsTENYanNabWFVdHA3UVdEVDUyQ0xBcVJSZw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **14.40** | **2.60** | **N/A** | **10.20** | **911,909,847,040.00 USD** | **10.89** |
| BAC | 12.09 | 1.29 | N/A | 3.40 | 349,633,576,960.00 USD | -3.51 |
| C | 12.11 | 1.07 | N/A | 8.00 | 205,592,952,832.00 USD | 25.82 |
| WFC | 12.10 | 1.62 | N/A | 0.40 | 257,558,773,760.00 USD | 1.79 |

Peers fetched as_of: 2026-11-11; JPM reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMingFBVV95cUxNZEdSeWY5RUlCZ3QxZklmQ2hsTGJXdHdxU3hXQXkxQUJCZXJaMlpMYkc4SEtubncteGpGVVIxcWFtV19RdWF2bDNSQmY5UC1aVUo5U1NmQWRpSjlnWW1OUWRhMWdyb191VS1LV2g1QTZUTTFmR0hPXzQwU3pzbndINnJhU19xN0FtQ1pQR2xCN20wbTI4YnhyWi1EazJjdw?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxPV21ST25Bejhhc3ZadlJGYkV1MlhzQ2l2b3dfRTZCbW1IZE90ejVRRWprWmNLU3ctQ1RvOW1BdHVPNFRXQTdaamZVUW8wdGl3NnZMZGJwSXFrSlY1cU9oUEFIT25RNG50Q0s1RUQzdzBLMThDVjY2dWVWNDRXeDZWZE52SFRNUEhFZ1lBTjExTUtFT01KQlA2S3k1dncycmdiblR1aDFQazdCMVdzTzhiU3c1bm9mVlFScG1yZ1hXSzJERVo5d2I2N05fWXpWVlQ2TVJ5bQ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPVTNqRHRxb0VJWl9velJGajJDS1JadTFCMDQ1b0dnSS1QeEtEZUZhdnViQ2pJQUZKSkxXU0Y5dlNzZXo1bW85VnE2Mi0xaWlYZ01pNnF5dGktQnA1cVpQYVMyV0luR2NubDJSM1NyZDM3OUw4dkFPeE5xVEhlXzBwRXhUNlQ4WVNvQVE?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxOaFl2RkI1UFFYazZjSHdRTDJpcjZFMFRSRTktWWtPQkJFSUJtZDU0aTZjZnh5MjVkRTBsREJYZHJLbVlId0VPa3pfLXNQZ3FNVEdUdjYyUWdOVExlZEFLem42dXRqbkRMQm5IdG1iN2wxdkxPeEFHR18xd0RzLUpOZkU0LV93bU9CYWJ3Q1JYLTE3UWd2SDYwVzBtNDN5SFdjNWg0X0tQTjdGemFQT2NQekpUejE5NHNsMHVtb0c5amZ3YmpjbldGSE1JVjB2Zw?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQZjNsYmtiazRCZTluMmhBYlMxSUkyaEhObzdMWFpYcUNyTWVrLTVOUUZ0MWUxQldpemEzX1BNcEN2RVVjSlpkRXFTRXZQZkRpcVQ0TkFRQUVDMW9PaWdFRHVIdXlMMHBWQk5yV2xBemlFVHgtdlF3aU83RnBaTGlfV0sxcW9YaHQydzk3ZFJvRGQ5MUZuc3VyWkhmZmRKQTJpTEcyanFlTWNkOFZrQ0dhalEwaC0?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNbExVV3pHMzk2ZEFxMjAtbldSOEphR2xCMDJWWEdlYkl4MTRHdGE4LVNTeDk0MFBESUVMMEhVUEx4SHhLVkFtTEMwbzB2eThRRjNDZWt5ZERzek9xQlRLUjZSRXlXLWp5ZEEtMlVVY0ducnQ3VWxiR0VGTTBTZVZiUzA1OWRPcldHNU5xT2VnaXkzX1M4NFE2Sjh0dXFPWVU4MVlmZ09nZnJ4OE1vMTZ2NWF1RklXQzNEdWVCZg?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxQOEhkdEhBTFZVSDFWUEtLcmhkc1FlMlpESWlJeVFJZ1E0VzBIVnBVR213c2dNUllmeFB4UWNyVUtULWs0OGFlTW5MRFVvUVhQSUdPT2N3VlhMRXR6R1Zmb0g5SUdxUkxiS3k2cmkzaGl3OURMMkpXWjlIbVdMR2lSZzJFRk5GNm5HWDdKYldaLTlPNmZhekJuTnMtWGZjWWNvS3VVdGxzdXNDQmZLM25QWE9QcTdtdktxaWtaRDh1b1VtRHFXS1FnWG1jaXNkSnRf?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPUWhVX2dlNUtJaHlFMFdWakwyVVZZSXM4S1J2QUl2ZWVNeTBVUlE4VHVXMHRoRWNvcW1LNDB2UGhZNEZvRmVlcHhBMDJJV1Fwcl9SX2dHUExUQVpUNmgxSU1rdGNOdFFQZHdqYmlqMGxXekc3elRJV3JkTmxnSWFmZUV6aVYwTXNBeFJxUjBJb1NjXzFGX3FzQjdGYkdHQk5iMWNYMWNhby1QVHRPU1FvRXl1NXJRS2pyXzVDdkJ6Y3hJQVdzLVVIR213?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPMXNySVJDRkZWNVEzc2pYWXE5MUdpNUptYzVkRXBTLVRNMkJtSXZGR2lRNmlVQXNQSmNkb2dZWkNZODhlSll2V004Q0ZhejZqR3dZM0hFWEp5QndOSDUtb0M2NHRJemc1WjVLSVN3OVdHc2p0alFZWWVyYzBiTGR2N1V0QzNnVlh6eHZ0M2ZHZE5SczdUZHN3Y1hLOXpFMmc3c0JpOVZkX2FpRTFrQl9EVw?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxNZnNYeUVUZEhzcU42bzVZYklGd2NkQWJjRG5kYmxFOEFvcWtNdXE0ZXZVV2RyWHdfbUhHUkNlNVg3YzZId0tlMFh2TUtXTGgzSjFoUHBlRU1GazVzZlNFbV9wcVEwV3JSakNwamQ4RkF6RTA1TVp2R0xLb05RNGlDdTVqb0JXbF9zRkVrYzhmSDdpZkcxb3F5LXVIcy1DTl93SkZCRVBnQzJ0VVc3eFZXT2x0am5Fc2FVZWR6UFZ1NVZEZlFfRkw2cVg3Z2hKaVF4?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQTW1LNDZzRXRoVFQwdVlsaVFqRGN2Rk9oZDlsM0UxREgzcVdXeVBYZEpZbEJHRGxhZl9wX1RRZDhVRUlpM0pnRU5GNTFxUXRseXBkMHJHaVZRdWNLcHBTZWxmQ2NjekxnVzFObEZ3aTFzQ3BhVExGSkxJVW1CVEw2T1ZuS3Rkakp6NWxmVTZDYTRObHNJZlIyV0pXdjdsdXhfSUMtRzVZQkxYV2JNN1M4dUNJY1NMaXZYMzZscDZ3?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNU2ZMaTZDY3FVcms0QmZ4SGg5a1I2WThhNnFranpEUGxldDZHSHh5UHU2ZFNraHhuT0dBLTlBeFQ0TkVDYk0yazkyZDJoTk1XWmJRRWd0YTdIWm9yOXkwZ1piVGZXNEtKOGRiZlhTQTd2UjdHUjBmelBVRFkzbjdRd3l1WTltZGlqS2EtSEZNX2M2d1BEWE9rdjE2andiZEQ0a09WUUgybkxyeGtjdlZDSHNoUHgwVlhiR2tZcW9uZnM?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxPVEVfTDVFVjBSZ1JLTVRoaUlOT0NIMFdxNmdlSXBFWmxLMnpBcXcta2NyTXJ5VEVsc3U0bEQ0eExrWkpkSkhKM1FxUGNOWWc0a29uRzhUZzIteUM3OWZBdllTZWd4NmIzYTNjbUgwWlhDVjI5LWJxWEs0S0N4czdKSHhhYlVDTGxiZzRzMjVVLVI2SU5ObUV3cnY0cTU5MjYzemlqREFZei1iV0tsQTJCanZscnoydUh0ZVYzTkFCWE5Taml5ZWpNN2QxQ1JvbGxRMUUxall3?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxNMFFqa3FHNU1CWlFPX0pzZUZacGViM0VJV0V4a0JVcnpLRFREa2FGeklJMU5MQkFSOWIwWFFOYVZrR2dSQi1BSVB4Q01IZXJOcGtEUkJDc0hLanRGZ0h2VUxRbWR4STAxNVVvU242VUNIVWJkUUVubV9kWVNsV1hTblBobFZPM2ZfWTFSbmVzYk1ab1hMVVRlWHV2eVBtRzh5Z3YybmhiSjFtQ216WnVwOEJUSTdJdDBzaGdaR2s0M1l3dmJUMEF1OXZFR3lUaE9GQzdhczN6ZFd1UW9OVWNfRUhPQQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQMXJFekNOaWVaVFd6WW5BdldQU05QUk5ldURDV196SXZGTUQ5NG9aMUtvWmhLeGRoaHYtTnk0ajBYOS1mcU9DeVFXTEtOM3BlR1ZCZGZ3NEhKSHhGbVF1QVh1VWRKTTdaM2p0RHZqanBWekpRTG1heGFVdXJ1Q29qcWdRWG51MS1pc05YV3pMZnpGb3RUaVU2ZjdB?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNYk5WT3NFSVRIRElaYVFlYXdrcHAteGxRUzRYYWxDaDFoVDl2VFVLVzZpUGYxSVVRX2hWZ3JyZS1sbWU2cHVTVFdaS0xuQzh4OWZHRWFua0xKSmdfOFEyMlNCTWtVN21QQzVfdTdzZEJTOXFEQVRKa19oR3RYeUd2cVpvSjNWekdrQmxnWmpxazFBLWlrbVl6TlZVRnlOYzBvRzdfVTZhZzdPblNHOENDbFFxbndETU1QN0tmTA?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNbFc1MFFIOWJNODdEVnEzWG5KZF9YUWdOLXZUeGNsbWVDMGxxNnJ6V1ltajhwejgycmhNa0lUUG1iRUpGM2NCN1B0Q0VsYl9aaS1tUEd4d0NWSndIOTlGYUQyQmVqVHlpMl9wekhCTDg1WmJRckxJMzlHZW91YUZad0liZXpUamV1b0RiZmtkRTBxSnRKNkI0dUl1bUM2X3lBcTJHbF8tT1pWY21MdVRnTE1xOEtMYXpp?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQbGJiMWhTQTVnVjBFRHlkcU9pWTBxWVMyTGtHMkZJOU5KaW5sWEJQeDNSVElObmhTZzNlbVhiS0Y5SlBFRHlIWnE0WVRZVmNQLXk1S1Jsc29EMHBLMUJMOW0yNkY2YXJWaGhKaUNmVkhZLXlRYjUwamZ6aXBpXzVNOHVneUQ3Z3BwWHdFcVlDa0h0NHJXRUxZYk5RNDlsMFljRXNVTG1IVVowSVlrYmFXNDVvcVZUNmZJOWs1WkJlbmM2Y1ZaeFlv?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxOOTV1d0hOSlBSTEdtR0NUTFo1aE5QMkYxeDZSdWhtdVQ4dVpmbGNiMTdZakpQZ0JMeXIzVS1kQWxBMGlEeFM5OUpmVEo1dTJJdWZzMFpOVWVxSDY2aV9UWXo0bnNZV2ttZzhXLUdpNXpqUFJUelBwY2t4ZHBQWnhJVEVnMkdpOFdWWlQwaFppdENEdFBSajdGSWdMTjZQbUtySnV2bDZzM2dIcW9tZFJhRndaa3NSNmktbWc0TGVUOTNsWWVhS0dtbjZiaXFsTENYanNabWFVdHA3UVdEVDUyQ0xBcVJSZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
