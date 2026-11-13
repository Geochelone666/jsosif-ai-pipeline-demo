# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:14:04.318276+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 4, 'ai': 13, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/JPM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'low_uncalibrated_model_confidence': 3}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 7 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 47.83%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 342.8200 |
| Return 1D (%) | -0.1660 |
| Return 1W (%) | 1.6245 |
| Return 1M (%) | 2.5486 |
| Return YTD (%) | 8.4422 |
| Return 1Y (%) | 9.0549 |
| Annualized volatility (%) | 22.9595 |
| Beta vs SPY | 0.8053 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.4938 |
| Downside deviation (rf=0, %) | 16.5649 |
| Sortino (rf=0) | 0.6844 |
| Historical VaR 95% (1D, %) | 2.4515 |
| Historical ES 95% (1D, %) | 3.3955 |
| Correlation vs SPY | 0.4817 |
| Tracking error vs SPY (%) | 20.2966 |
| P/E (trailing) | 14.38 |
| P/B | 2.59 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 13.41 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 44.79 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 339.9854 |
| Close vs MA50 (%) | 0.8338 |
| MA200 | 322.2143 |
| Close vs MA200 (%) | 6.3950 |
| RSI (14, Wilder) | 53.4059 |
| MACD (12,26) | 1.1795 |
| MACD signal (9) | 0.4635 |
| MACD histogram | 0.7160 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 342.8200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.1660 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.6245 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.5486 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 8.4422 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 9.0549 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.9595 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.5649 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6844 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4515 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3955 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4817 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.2966 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8053 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4938 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.4055 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.7880 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.3800 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.4059 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7160 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.8338 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.3950 -> Clearly above the moving-average trend level.

## TAILWINDS

### JPMorgan Chase & Co. (JPM) is Attracting Investor Attention: Here is What You Should Know
- Summary: Positive investor focus on JPM, indicating potential upside.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNZEdSeWY5RUlCZ3QxZklmQ2hsTGJXdHdxU3hXQXkxQUJCZXJaMlpMYkc4SEtubncteGpGVVIxcWFtV19RdWF2bDNSQmY5UC1aVUo5U1NmQWRpSjlnWW1OUWRhMWdyb191VS1LV2g1QTZUTTFmR0hPXzQwU3pzbndINnJhU19xN0FtQ1pQR2xCN20wbTI4YnhyWi1EazJjdw?oc=5>

### JP Morgan Chase & (JPM): JPMorgan reports $1.84 trillion in 13F holdings for Q3 2026
- Summary: Reported $1.84 trillion in 13F holdings, indicating significant investment activity.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPXzhOYl9CdlM4NDVTYkl2bGo3bUxnZktqN2tkcUthRnVibDN6aWF1QVc4WlQtYzd3d09rSW5JbWFWakdBUmp1QmtpdHdCVGVkVE1Hdk5sakE3ajFCMmoyYklOUGtRbkZ4dWNtSkhIaVZqbHVSR1U0ZTdLblA3bEVmekMyY1N0WUVHRWxhbEtsTQ?oc=5>

### JP Morgan Chase & (JPM): Fact sheet sets 2036 EURO STOXX 50 note with 75% threshold
- Summary: JPM issued a 2036 Euro Stoxx 50 structured note with a 75% threshold, offering a long-term investment product.
- Date: 2026-11-12 | Impact: low | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNVE5OdzZCcVc2WTBaZEo3akpRQU11eXF4d0ZGTk9tVU1Za180VnUwcm5NbG0xN2ZvZVRKc1h4N0wycmRObjJPVDd3dFEtLU5iZ0ZUU3MtTURlMFhCOW9CUThHWlBLWk5GVW5IdXRSbk90RXZfOE9Tcm1TRUxfLTdySFZDS0g3dHgtRDE0?oc=5>

## HEADWINDS

### 5,740 JPMorgan Chase & Co. $JPM Shares Sold by Coerente Capital Management
- Summary: Coerente Capital sold 5,740 shares of JPM, indicating a modest divestment.
- Date: 2026-11-08 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPN0V2RjVUZkREdk1jQ1VubHNUUGtLY2xhcG1ER2hFcmwzVEhWQ3F5c1JYT2x1VFNHNDdLaUZiSGxsOUtrSFZKR1RPU0tfczc2ZEhmaVR2LTlJWl91VU9LRGptdEltZlNqQV9nOFFaRktmLW9yMlFGN3ZKWU9PSzM1UlVFT3V0NmQxb294b01GajlZczZ1R3hsc0thQ2xjby1HNm9iREp1N3RIV1V0R3UtQ0o2VFZ2aGxGaHRYVjJPTVRqQUZuVU4zRGpn?oc=5>

### JPMorgan Chase & Co. $JPM Stake Lowered by Parr Mcknight Wealth Management Group LLC
- Summary: Parr Mcknight reduced its JPM stake, reflecting a slight portfolio shift.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxNSzRraGFGYXF6VUozYzZEeng2YlFKQjV5ZmtpckpCazR3QXZ5aDhmdFlfc3phc2xQWTFPbkROQWdJVV9mRmZ3cy1CclduWXZPUjNvdmNibUEtQ05vT0Fld1hEZzRBeXFnR0kxT1k5dVVpdWFLZVh3RGRzdnFXSm1RQnpYWk5UcU1iblJjVjAzdml6dHRpYUxQUGQySkdmR1NENHB3ZHZYVFF5bEc0dzI5VnUycEQwSzB4amN6cnB2amItN1gzYnQwTFpTelBFSi1yV2l5NHJXeVc?oc=5>

### Heritage Investors Management Corp Sells 11,293 Shares of JPMorgan Chase & Co. $JPM
- Summary: Heritage Investors sold 11,293 shares, a small divestiture.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNWEY2U0M2SXI2NkdyY3NvUFZJUF8tQllXTWNvM2N2OWpmbV9QSFZLZVZHeXQwcy1KYVBlcU1aLVIwVTJYWENoWnJ6Ni1FWHkxeEU3cjhFWnV6VW1vOFhxYnZfNzdBTVE4TEdSSlh1NU5KQ0JqTi11TU5zV3ZrN2ZNTzJhY2ZSaHo1MlA4eVhTZXdJQU9NdW5vWmowNk83Nklia0REQlZ4TjBCZVJGQm54VUlqRmNnelRwZ2IySVZPYWFOeVI3WDVYNmNySDRORERTMlE2Q0FR?oc=5>

## CATALYSTS

### JPMorgan Chase & Co. $JPM Stock Sold by JCIC Asset Management Inc.
- Summary: JPMorgan Chase & Co. $JPM Stock Sold by JCIC Asset Management Inc.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQaGp5RFo4ZmstX3BhbVpNRWh5cHRIdnRYUzM0dVl2eF9YcVhWaVZPRWJ6ZlNUN1k2ZkhwT3RiTGVia2RReFFaRWZaSlFsWmhiV0NyUFVwS0VoajM1ZkM0UE9EZllhcUVYOFdOcFpaYkVWYjZlU0otMzEwSmh1YzFiQ1NiY2VRaVdJcGtNUzhDVGVEMm9fY1ptclBDSTN1OUY4TFhLSElHTUFIdlR6ZEpMb3lBZmJwUi1MamdqRDlwUQ?oc=5>

### JPMorgan Chase & Co. $JPM Stock Sold by Inscription Capital LLC
- Summary: JPMorgan Chase & Co. $JPM Stock Sold by Inscription Capital LLC
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNbExVV3pHMzk2ZEFxMjAtbldSOEphR2xCMDJWWEdlYkl4MTRHdGE4LVNTeDk0MFBESUVMMEhVUEx4SHhLVkFtTEMwbzB2eThRRjNDZWt5ZERzek9xQlRLUjZSRXlXLWp5ZEEtMlVVY0ducnQ3VWxiR0VGTTBTZVZiUzA1OWRPcldHNU5xT2VnaXkzX1M4NFE2Sjh0dXFPWVU4MVlmZ09nZnJ4OE1vMTZ2NWF1RklXQzNEdWVCZg?oc=5>

### JPMorgan Chase & Co. $JPM Shares Sold by Commonwealth Equity Services LLC
- Summary: JPMorgan Chase & Co. $JPM Shares Sold by Commonwealth Equity Services LLC
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPUWhVX2dlNUtJaHlFMFdWakwyVVZZSXM4S1J2QUl2ZWVNeTBVUlE4VHVXMHRoRWNvcW1LNDB2UGhZNEZvRmVlcHhBMDJJV1Fwcl9SX2dHUExUQVpUNmgxSU1rdGNOdFFQZHdqYmlqMGxXekc3elRJV3JkTmxnSWFmZUV6aVYwTXNBeFJxUjBJb1NjXzFGX3FzQjdGYkdHQk5iMWNYMWNhby1QVHRPU1FvRXl1NXJRS2pyXzVDdkJ6Y3hJQVdzLVVIR213?oc=5>

### JPMorgan Chase & Co. $JPM Shares Sold by AIA Group Ltd
- Summary: JPMorgan Chase & Co. $JPM Shares Sold by AIA Group Ltd
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPMXNySVJDRkZWNVEzc2pYWXE5MUdpNUptYzVkRXBTLVRNMkJtSXZGR2lRNmlVQXNQSmNkb2dZWkNZODhlSll2V004Q0ZhejZqR3dZM0hFWEp5QndOSDUtb0M2NHRJemc1WjVLSVN3OVdHc2p0alFZWWVyYzBiTGR2N1V0QzNnVlh6eHZ0M2ZHZE5SczdUZHN3Y1hLOXpFMmc3c0JpOVZkX2FpRTFrQl9EVw?oc=5>

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

### JPMorgan Chase & Co. (JPM) Up 2.4% Since Last Earnings Report: Can It Continue?
- Summary: Shares of JPM rose 2.4% after the latest earnings release, raising questions about sustaining the upward trend.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPeTd2Z2g4LXpqenNnYkozQUZBV1JUODhBeHdkcERHZENfOWpYWm5wU1pTXzRpcFBDX2d1dDdDcmk3cHFDTGtFVGdzYlpPYV9HWnVTeTc5SV90ekEtR29KVTFyb1JPb29FUGZNbXM5bzFuY3NxWWkyR3Q4SmVRZkhfUWN5WW5WbGJ4MGRqeGR3TVpqdw?oc=5>

### JPMorgan Chase (JPM) Private Wealth Alternative Assets In Asia Pacific Rose 40%
- Summary: Private wealth alternative assets in APAC grew 40% for JPM, indicating strong asset performance.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQV2stREw1dHJYQVpJWTdMS3RocVg0dkpwRUVvbmVJOTRWYm5SME16LVlEanJKbWl6SUxSeVJSVkRINy1TZzlxV2VxdWM2Zk1sN0RSSXBtSDhVTDRHMUZ2TG5SR0o1VGRSYTBpcFIxd1E4ZW5hMzhLR0tVS2tLUE02aTBfbHg3TUMzZGctVzZRMXNXSzNWb0lJMjVsNGRZeHNLb053cHQ0T1ZqbnJIcUhEY1pxVDlhU0tOckZIUy1MR2h5OGRuaWfSAcsBQVVfeXFMTUFWRjdnR05fNlNDVFVEbTJrNkF1ZVdJY1JxM295SmVndm14VVQ4Slg2NFRubXpyVnVUaEFGYUlvWjRUazVLOTZzakdMYXR6VzRLMmhmLVNHc0dfamtrWUxoUGVzZktFUzIyYmNIT3UwVDdieGNiYkROMk1pRVNLZzdramtDdThzRG5IWU0zUHY5R1ZOWlg2aUoxNGg2UDdoWkhwSzRBZWJHUHQwU1Mxb01uQ1FfTGI1c1FnLXRBZ2lfYU9aRG5HNWtkbkE?oc=5>

## RISKS

### JPMorgan Chase & Co. $JPM Stock: International Assets Investment Management LLC Decreases Stake
- Summary: Large investor reduces stake in JPM, potentially signaling negative sentiment.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxOOTV1d0hOSlBSTEdtR0NUTFo1aE5QMkYxeDZSdWhtdVQ4dVpmbGNiMTdZakpQZ0JMeXIzVS1kQWxBMGlEeFM5OUpmVEo1dTJJdWZzMFpOVWVxSDY2aV9UWXo0bnNZV2ttZzhXLUdpNXpqUFJUelBwY2t4ZHBQWnhJVEVnMkdpOFdWWlQwaFppdENEdFBSajdGSWdMTjZQbUtySnV2bDZzM2dIcW9tZFJhRndaa3NSNmktbWc0TGVUOTNsWWVhS0dtbjZiaXFsTENYanNabWFVdHA3UVdEVDUyQ0xBcVJSZw?oc=5>

### JPMorgan (JPM) Stock May Be 31% Undervalued On Senate Probe News
- Summary: Senate probe may reveal undervaluation, posing potential risk.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQbHpMTjdWSDRrazRQMEM2dnVwV1JBdzlOWTVSaTMyY3ZwYVAxR0ttaE5wZmtTT0N6b3E2NWFDLUtUeEhzb2lxbEVOMHdZR04tUkNiTFZCbkd5UzZYaFRLeTc4TktPWXlqcUs2QWpMTHdaSFlaYWd5Y1c5UVFvdVo1TUkzS3dQekhtZWhxTm5ndUQzTE96?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **14.38** | **2.59** | **N/A** | **10.20** | **910,396,096,512.00 USD** | **9.05** |
| BAC | 12.05 | 1.29 | N/A | 3.40 | 348,529,557,504.00 USD | -4.66 |
| C | 12.09 | 1.07 | N/A | 8.00 | 205,344,669,696.00 USD | 23.09 |
| WFC | 12.10 | 1.62 | N/A | 0.40 | 257,438,695,424.00 USD | 1.66 |

Peers fetched as_of: 2026-11-12; JPM reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

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
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPXzhOYl9CdlM4NDVTYkl2bGo3bUxnZktqN2tkcUthRnVibDN6aWF1QVc4WlQtYzd3d09rSW5JbWFWakdBUmp1QmtpdHdCVGVkVE1Hdk5sakE3ajFCMmoyYklOUGtRbkZ4dWNtSkhIaVZqbHVSR1U0ZTdLblA3bEVmekMyY1N0WUVHRWxhbEtsTQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNVE5OdzZCcVc2WTBaZEo3akpRQU11eXF4d0ZGTk9tVU1Za180VnUwcm5NbG0xN2ZvZVRKc1h4N0wycmRObjJPVDd3dFEtLU5iZ0ZUU3MtTURlMFhCOW9CUThHWlBLWk5GVW5IdXRSbk90RXZfOE9Tcm1TRUxfLTdySFZDS0g3dHgtRDE0?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPN0V2RjVUZkREdk1jQ1VubHNUUGtLY2xhcG1ER2hFcmwzVEhWQ3F5c1JYT2x1VFNHNDdLaUZiSGxsOUtrSFZKR1RPU0tfczc2ZEhmaVR2LTlJWl91VU9LRGptdEltZlNqQV9nOFFaRktmLW9yMlFGN3ZKWU9PSzM1UlVFT3V0NmQxb294b01GajlZczZ1R3hsc0thQ2xjby1HNm9iREp1N3RIV1V0R3UtQ0o2VFZ2aGxGaHRYVjJPTVRqQUZuVU4zRGpn?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxNSzRraGFGYXF6VUozYzZEeng2YlFKQjV5ZmtpckpCazR3QXZ5aDhmdFlfc3phc2xQWTFPbkROQWdJVV9mRmZ3cy1CclduWXZPUjNvdmNibUEtQ05vT0Fld1hEZzRBeXFnR0kxT1k5dVVpdWFLZVh3RGRzdnFXSm1RQnpYWk5UcU1iblJjVjAzdml6dHRpYUxQUGQySkdmR1NENHB3ZHZYVFF5bEc0dzI5VnUycEQwSzB4amN6cnB2amItN1gzYnQwTFpTelBFSi1yV2l5NHJXeVc?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNWEY2U0M2SXI2NkdyY3NvUFZJUF8tQllXTWNvM2N2OWpmbV9QSFZLZVZHeXQwcy1KYVBlcU1aLVIwVTJYWENoWnJ6Ni1FWHkxeEU3cjhFWnV6VW1vOFhxYnZfNzdBTVE4TEdSSlh1NU5KQ0JqTi11TU5zV3ZrN2ZNTzJhY2ZSaHo1MlA4eVhTZXdJQU9NdW5vWmowNk83Nklia0REQlZ4TjBCZVJGQm54VUlqRmNnelRwZ2IySVZPYWFOeVI3WDVYNmNySDRORERTMlE2Q0FR?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQaGp5RFo4ZmstX3BhbVpNRWh5cHRIdnRYUzM0dVl2eF9YcVhWaVZPRWJ6ZlNUN1k2ZkhwT3RiTGVia2RReFFaRWZaSlFsWmhiV0NyUFVwS0VoajM1ZkM0UE9EZllhcUVYOFdOcFpaYkVWYjZlU0otMzEwSmh1YzFiQ1NiY2VRaVdJcGtNUzhDVGVEMm9fY1ptclBDSTN1OUY4TFhLSElHTUFIdlR6ZEpMb3lBZmJwUi1MamdqRDlwUQ?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNbExVV3pHMzk2ZEFxMjAtbldSOEphR2xCMDJWWEdlYkl4MTRHdGE4LVNTeDk0MFBESUVMMEhVUEx4SHhLVkFtTEMwbzB2eThRRjNDZWt5ZERzek9xQlRLUjZSRXlXLWp5ZEEtMlVVY0ducnQ3VWxiR0VGTTBTZVZiUzA1OWRPcldHNU5xT2VnaXkzX1M4NFE2Sjh0dXFPWVU4MVlmZ09nZnJ4OE1vMTZ2NWF1RklXQzNEdWVCZg?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPUWhVX2dlNUtJaHlFMFdWakwyVVZZSXM4S1J2QUl2ZWVNeTBVUlE4VHVXMHRoRWNvcW1LNDB2UGhZNEZvRmVlcHhBMDJJV1Fwcl9SX2dHUExUQVpUNmgxSU1rdGNOdFFQZHdqYmlqMGxXekc3elRJV3JkTmxnSWFmZUV6aVYwTXNBeFJxUjBJb1NjXzFGX3FzQjdGYkdHQk5iMWNYMWNhby1QVHRPU1FvRXl1NXJRS2pyXzVDdkJ6Y3hJQVdzLVVIR213?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPMXNySVJDRkZWNVEzc2pYWXE5MUdpNUptYzVkRXBTLVRNMkJtSXZGR2lRNmlVQXNQSmNkb2dZWkNZODhlSll2V004Q0ZhejZqR3dZM0hFWEp5QndOSDUtb0M2NHRJemc1WjVLSVN3OVdHc2p0alFZWWVyYzBiTGR2N1V0QzNnVlh6eHZ0M2ZHZE5SczdUZHN3Y1hLOXpFMmc3c0JpOVZkX2FpRTFrQl9EVw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQMXJFekNOaWVaVFd6WW5BdldQU05QUk5ldURDV196SXZGTUQ5NG9aMUtvWmhLeGRoaHYtTnk0ajBYOS1mcU9DeVFXTEtOM3BlR1ZCZGZ3NEhKSHhGbVF1QVh1VWRKTTdaM2p0RHZqanBWekpRTG1heGFVdXJ1Q29qcWdRWG51MS1pc05YV3pMZnpGb3RUaVU2ZjdB?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNYk5WT3NFSVRIRElaYVFlYXdrcHAteGxRUzRYYWxDaDFoVDl2VFVLVzZpUGYxSVVRX2hWZ3JyZS1sbWU2cHVTVFdaS0xuQzh4OWZHRWFua0xKSmdfOFEyMlNCTWtVN21QQzVfdTdzZEJTOXFEQVRKa19oR3RYeUd2cVpvSjNWekdrQmxnWmpxazFBLWlrbVl6TlZVRnlOYzBvRzdfVTZhZzdPblNHOENDbFFxbndETU1QN0tmTA?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNbFc1MFFIOWJNODdEVnEzWG5KZF9YUWdOLXZUeGNsbWVDMGxxNnJ6V1ltajhwejgycmhNa0lUUG1iRUpGM2NCN1B0Q0VsYl9aaS1tUEd4d0NWSndIOTlGYUQyQmVqVHlpMl9wekhCTDg1WmJRckxJMzlHZW91YUZad0liZXpUamV1b0RiZmtkRTBxSnRKNkI0dUl1bUM2X3lBcTJHbF8tT1pWY21MdVRnTE1xOEtMYXpp?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPeTd2Z2g4LXpqenNnYkozQUZBV1JUODhBeHdkcERHZENfOWpYWm5wU1pTXzRpcFBDX2d1dDdDcmk3cHFDTGtFVGdzYlpPYV9HWnVTeTc5SV90ekEtR29KVTFyb1JPb29FUGZNbXM5bzFuY3NxWWkyR3Q4SmVRZkhfUWN5WW5WbGJ4MGRqeGR3TVpqdw?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQV2stREw1dHJYQVpJWTdMS3RocVg0dkpwRUVvbmVJOTRWYm5SME16LVlEanJKbWl6SUxSeVJSVkRINy1TZzlxV2VxdWM2Zk1sN0RSSXBtSDhVTDRHMUZ2TG5SR0o1VGRSYTBpcFIxd1E4ZW5hMzhLR0tVS2tLUE02aTBfbHg3TUMzZGctVzZRMXNXSzNWb0lJMjVsNGRZeHNLb053cHQ0T1ZqbnJIcUhEY1pxVDlhU0tOckZIUy1MR2h5OGRuaWfSAcsBQVVfeXFMTUFWRjdnR05fNlNDVFVEbTJrNkF1ZVdJY1JxM295SmVndm14VVQ4Slg2NFRubXpyVnVUaEFGYUlvWjRUazVLOTZzakdMYXR6VzRLMmhmLVNHc0dfamtrWUxoUGVzZktFUzIyYmNIT3UwVDdieGNiYkROMk1pRVNLZzdramtDdThzRG5IWU0zUHY5R1ZOWlg2aUoxNGg2UDdoWkhwSzRBZWJHUHQwU1Mxb01uQ1FfTGI1c1FnLXRBZ2lfYU9aRG5HNWtkbkE?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxOOTV1d0hOSlBSTEdtR0NUTFo1aE5QMkYxeDZSdWhtdVQ4dVpmbGNiMTdZakpQZ0JMeXIzVS1kQWxBMGlEeFM5OUpmVEo1dTJJdWZzMFpOVWVxSDY2aV9UWXo0bnNZV2ttZzhXLUdpNXpqUFJUelBwY2t4ZHBQWnhJVEVnMkdpOFdWWlQwaFppdENEdFBSajdGSWdMTjZQbUtySnV2bDZzM2dIcW9tZFJhRndaa3NSNmktbWc0TGVUOTNsWWVhS0dtbjZiaXFsTENYanNabWFVdHA3UVdEVDUyQ0xBcVJSZw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQbHpMTjdWSDRrazRQMEM2dnVwV1JBdzlOWTVSaTMyY3ZwYVAxR0ttaE5wZmtTT0N6b3E2NWFDLUtUeEhzb2lxbEVOMHdZR04tUkNiTFZCbkd5UzZYaFRLeTc4TktPWXlqcUs2QWpMTHdaSFlaYWd5Y1c5UVFvdVo1TUkzS3dQekhtZWhxTm5ndUQzTE96?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNd0NtU25YWWN4Y2Mzc1ZoYS13dW5LS2R1QzNWOGU0SWhId0tHWFJTNVRJWDZ5T0htZ1ZOak5GOGsyRzl3anI5Ukc5Nm5CWGN4alB0QnRxcTJTNHpETDZoLThfVGJNcV9CY3pnLU44UTc2dkloaS1BNXRFTWw3ZC1iWXk1alBVZ1V6c2J3QUxkR0d6Q3B5M21XWEV3T0pJQ29lcVU4RlpHN1NBcHJrYlZJQWMzSW1mZWF2b0VwalEzT1YwMDVfTkHSAcsBQVVfeXFMT09SQm1XMUxYZklmM3F5Ty1oTWFNMVhyX2Fnb0J1VE5TbTVObGttMU1QWWpnWjR5LUF1dXBjSDczTVViWlBxcFlmeDZISzZRakxuaW1XSEJmT25Uamx3UzZxczUyWjg3Ul8zMXI2OUdiUjdJbjJyX2EzLXZNckVRMkZXYTNoZlMtakRZYzBDdW9pM0Y5c0ZLNkk2ZFRRQ1REbFZ3aGZXWXJVM01LNW5Wc2pGTERaUlROYTZ4bkd6eWpXY2FXWWtsQ1FGWEE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
