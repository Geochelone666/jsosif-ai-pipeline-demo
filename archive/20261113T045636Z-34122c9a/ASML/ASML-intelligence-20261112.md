# ASML Intelligence Report

- ticker: **ASML**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/ASML/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ASML/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:06:36.985670+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 4, 'ai': 14, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/ASML** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 11 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 26.09%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1497.1200 |
| Return 1D (%) | -2.4309 |
| Return 1W (%) | 10.3542 |
| Return 1M (%) | -14.3492 |
| Return YTD (%) | 40.7938 |
| Return 1Y (%) | 45.2090 |
| Annualized volatility (%) | 48.7129 |
| Beta vs SPY | 2.2565 |
| Max drawdown (%) | -31.6292 |
| Sharpe (rf=0) | 1.0119 |
| Downside deviation (rf=0, %) | 32.9073 |
| Sortino (rf=0) | 1.4979 |
| Historical VaR 95% (1D, %) | 4.7389 |
| Historical ES 95% (1D, %) | 6.4916 |
| Correlation vs SPY | 0.6362 |
| Tracking error vs SPY (%) | 41.3551 |
| P/E (trailing) | 36.84 |
| P/B | 1285.50 |
| EV/EBITDA | 1968.54 |
| Revenue growth (%) | 55.20 |
| Forward P/E (estimate) | 23.61 |
| Gross margin (%) | 54.34 |
| Operating margin (%) | 38.55 |
| Return on equity (%) | 65.64 |
| Free cash flow yield (%) | N/A |
| MA50 | 1661.8478 |
| Close vs MA50 (%) | -9.9123 |
| MA200 | 1597.8153 |
| Close vs MA200 (%) | -6.3021 |
| RSI (14, Wilder) | 42.4122 |
| MACD (12,26) | -56.7735 |
| MACD signal (9) | -55.1187 |
| MACD histogram | -1.6548 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ASML': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1497.1200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.4309 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 10.3542 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -14.3492 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 40.7938 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 45.2090 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 48.7129 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 32.9073 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4979 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.7389 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.4916 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6362 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 41.3551 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.2565 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -31.6292 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0119 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.6141 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3370 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.5520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 65.6360 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 36.8386 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.4122 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.6548 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.9123 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.3021 -> Clearly below the moving-average trend level.

## TAILWINDS

### ASML Raises 2026 Guidance as AI Demand Accelerates Capacity Expansion
- Summary: ASML Raises 2026 Guidance as AI Demand Accelerates Capacity Expansion
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNcjI2cTBhSXUwVW5rMnZpZWgxamluLV9IaGFZU1l2OVRWb1liUl9HT0Z6WE9sd1FNZHZiTTRmZ1cydTI5U19ULXFWbDVuRzRHX2lGS0V3eDM1d1A0VDc4STVCdFkxcnNrcFEtUlJxTDhtdV8xbUZhVEpSeUZBaWxpMmNhRE9yd1V1MnhaN1JzSk1XMTA?oc=5>

### ASML's Raised 2026 Guidance Is Only Half the Story — the Financing Chain Decides the Rest
- Summary: ASML's Raised 2026 Guidance Is Only Half the Story — the Financing Chain Decides the Rest
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8AFBVV95cUxOd29NTTJ4S1BBcTZXS3B2ZDg3MmNMTUhmc2tyUzU1WDNQQmhZMlJtbUJuc2dSQ2FWaHIxRllzcVJxSWZrQVMwb1JZTkpFSUxFVkhhY1R5N1lIQzY4Qk5ZQnh2aS1lbmw4LXBlY1FSUzV1dHl3REhNSlFNWVNXUGJBVjFERk1WbFJMWnk5S25aQlRBT1RVOFhtUG45VHFPUnB0UUVwZFFGa3pxZ1pLUnJEMXRpbXowckNYbWVjUk8yOHZVM3AwdXl1NW95ZHZZZjRTTDZ4cFlZX3pXSWk0ZkZPbnpWR1lIS3dmS2RRQ3pLcmI?oc=5>

### ASML Holding NV Stock (ASML) Moved Up by 3.30% on Nov 11: Facts Behind the Movement
- Summary: ASML stock rose 3.30% on Nov 11 due to positive market sentiment and favorable analyst outlook.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOTEJmcmo5NC1QbjgtbFBXakJrbW5XcGdnczg3OXdsX0RyXzl0YnQ1UGt5bTFucWh6WkVLVURyb3NLalROT2dyQy1UY1dUeVRvQkxSMmlYQTBIM3d3dXdubWVrYzRlN25PdGhOcjVsRmpiN2RnVzRmU1lIRG5YVF9kYzNaZUxoTWxsVExj?oc=5>

### ASML Stock In Focus As EUV Machine Orders Stretch Into 2030
- Summary: EUV machine orders projected to extend into 2030, indicating sustained demand for ASML’s advanced lithography equipment.
- Date: 2026-11-06 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPYXZuNWI5TzU5R0hjNjZlcnQ4ejRVUU0tdnNQbWFYc0Q3cmxLbzZmLTBUTW5GTFB4WmVXbm9rdTQ3by1sUnJkcDZobmdtT0RqYV9uM3FlSVVJUWRhWG4xdFZXLUFuVnE1Z2c0TkEyUmhqR1BySHUyN0hsRjhlWlpqTExGQ2dmVmMzNldXVHctS2FKYW0wX0xyLQ?oc=5>

### Why is ASML NV ADR stock rallying today?
- Summary: ASML ADR rally driven by strong earnings guidance and market optimism.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQOWJPSWVFQlpaQXFOSnBPbFNjNHdudmN2U3dfWVpMR0hJSzlIUHhXeW5XOWp0bXdPM2ZmZXdWd3U1U204aUtWLXRmcHc1NUE4WW5Jd2pKUkVObE1Ob2twcFVCa2RVQmVLeU9wWjRrTEdrSk9fT3l0cWVGTVRqZG9ycE4ycVB3ckdGTHBSeUJNYjRhczlLb2ZlaHlwaHd0dDY0cmRn?oc=5>

### iShares PHLX SOX Semiconductor (SOXX) Adds ASML and Analog Devices on Tuesday
- Summary: Index inclusion boosts ASML visibility and may lift demand for its equipment.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNUjBycjNVVk5BTlZ4cllqcXkyZGtfSFplMEJTQ2NadEZzVE4wSDdPdmRNeUhkdmoxRktGV0d3U04teXE4ZmNPSndnUVBPQkFzdEJUNUwtSTg4dUJxSDktQ1doTGJ5MjhYc0tIakRYdGhPWWFUZXQ0My1MM1JGcG9NVklncHRnOWljcTVWNVN4TlRLaXJnRTZyN2Y4TXNrT0hTMlE?oc=5>

### ASML's Korean Order Pipeline Builds While Labour Talks Break Down
- Summary: Order pipeline in Korea grows despite labor disputes, indicating strong demand.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQeHJIWnlMcmRhdkFXb0l1TWJEOWVlMGF5ejFSSHE3QzJ0c1dQWjUwdTJIRDU3c0NwdDVYSWFnX3NfX0J3Qkhwam9xYV8tbHkySFI1RVBPOXdYdUhqMFBnWmd1ZHZDNzl3UEk1UkdHVWYtaUNfVS1qeDhSQkNxQi1fcDZKV1lJNXR4NWNaVUFqQ3Q1TGJSQUNqUjd4UlU4T0ZOUlRMVG4wdjR0MUZhbkNBRHlpMERvTXA1czJBS2lzRENJaVN5QnlOTHJVTGxHRHV4VjRF?oc=5>

## HEADWINDS

### ASML Falls 20% in the Past Month as AI Growth Meets Execution Risk
- Summary: ASML Falls 20% in the Past Month as AI Growth Meets Execution Risk
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOR1otbFFTYXl3Uml2cVNoLUdsNnVSd2Nvc08yWUdUd0lCdTdEamdZNUxjWmVEUllVSXNYUzE5cV9WRXlBZWRvdkdZeEVwTnJFdEFQSk9jYWxYb2pUQ21HX1ZndXdiLTN0UndHekRUd3FGQi1vckN6b2pfYmRfMllUejNER2JXRmNqUGVSYzN0NGdhOEU?oc=5>

### Why ASML Holdings Fell in October
- Summary: October decline reflects market volatility affecting ASML shares.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxNbmpJNTZhaWVFTXlvendJVXotM2VCSHVNNHh5YzNiTl9kcF9pb0E0UEJPdV95cHVfbWFpZEZJZk1IVWMtcERsNXdUR0lrSEczWWtSdHU4YmR5Z3NIQnpzbnB3QzRFNFdNRXRxaG84ZXZmMUEzcnJnSFl5bHdYekEzMUN3?oc=5>

### ASML Holding stock faces execution test as AI demand stays strong
- Summary: Stock faces execution test amid sustained AI demand, potentially affecting short-term performance.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxPNFJDYWUtVU15R2hFVVRXVFVtTXJUS0F2Mk54VU9UQlFVckVYLVBIdHFveWpzdm1ic0VaUDZ0dFBrVUQ1WVF3YjlSWmxUMHVTZ0x6WTNBNThQRmp2YXJUUkpkMWoyUi1vS1RBc2RuajlJQjBkcjRiLXFVRHN1N1RpRFczZEE3Nll4VkN4MWxNT2NtYklnU2ZHcmpYMmxCa1FvNVVSS2NRRjBaNXpOTWt5R1RMa28yU3h2ZEN2N0JHdUNJczBYODNv?oc=5>

### ASML Holding stock faces capacity test as AI orders reach 2030
- Summary: Capacity constraints may challenge meeting AI orders projected to 2030, posing operational risk.
- Date: 2026-11-09 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNT2VvS1NkSk1JLXo4bHNuNU9mZmg2MWg4NFdjZlZkVk5oeEdwdl9aZnVwR3ZuaWtMR2NXbDBvWmNPQWNMdHJzZ3hjTThhWmp5OXliV25DalZLaDNfTHRyTEJuVDYwUWRWT25UWXZDNk9WWTJfM291YjhJYUVOODhONDJJX2JRTUpGQXdoNkhJUGU5bEpRdjFCZXJ3REZ3UGR1R3prZ1hPWHVJSkFqak5CYWVNbFNDdGZXRExIbzRjS1dqZ2s?oc=5>

### ASML Stock Price Prediction: Holding above short-term trend support while sellers still control momentum
- Summary: Predicted price above short-term support, but sellers may limit upward momentum.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNMzJMWjdYVU5YclVORFZvcFZmRFBiM3FMVDZSbTBDUmJhSmtVODlvV0RTSzRudTBReDNNLVpYcnhaUXoxMG9rOHh3T1NhQ2R6QzFtbFBjZVpUdEl4bmlxWDQ3LWR3VUJLWFpZSVV4OW9vNVE0SzJOdDI4dVhXMFBaTzZqX0k5d2xDSjR1Skt0eEx6WnRrOXh4TF82akd5TVk?oc=5>

## CATALYSTS

### ASML Capitalizes on AI Boom with Record Earnings
- Summary: ASML Capitalizes on AI Boom with Record Earnings
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQNWJ6VG5ub0JyUFI4ck5Qb3A2M2NCNVh5VkdjZmhub0VZb25zQndfcFVYV0ZDbDhMSVFMNFpzaG43V2FjRHBBNnRGOWk0WG0wajZ2Y3lsVmQxR1ZIT19xZUdNMDNYc2N6SlBJcGhETDZ2RkJra09KOThmRWhqdk9IVlZ1RlBLN2p2SFE?oc=5>

### Why ASML Bounced Back Today
- Summary: ASML shares recovered today after a dip, driven by positive analyst coverage.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPODlhWk1sTmpvU3g5VlVXMXRoSWRGRnJNWWhPZ0U5UnFxVXVxNUV4eGt5Yk9hUmJnNGd3MzdyM2h6Sk9NUlBBbXo0Z1dxa3ozUVNnZ2d5M0o0QVZGRjFXMllUYWpQM2dmdUxlOUZOUlpZSHRWb1dZNElJcy1HMHY3dDJ6dzlUdjVLNDlBcWxYRW9vUHRWZ0Nn?oc=5>

### ASML Holding NV Stock (ASML) Moved Up by 6.12% on Nov 9: Key Drivers Unveiled
- Summary: ASML stock rose 6.12% on Nov 9, driven by strong earnings and product demand.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.92
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxObndWMC03WmxrTkpGUTdVZ1phdWxvelRCVzBqVVNhc3AxWGljdnd5SVF4QTdpTzBIaTFmeHgzemRqek5LcHY0REs4SDFURUFFS2ZzajFCdUFSWTkySWE3SjhGZVM1NTZuQmpDQk45eDVWVE1zcEdscUoxX2h0U3htUkZLc2RtS0ZsNDFZ?oc=5>

### Why is ASML NV ADR stock surging today?
- Summary: ASML ADRs surged today following favorable earnings guidance and product launch news.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNQUtCYWN1cC0zenNRSEdqaXNpZ01mTGNFTG0yZlJpTHExMmNJUHVBenM2VUNJcnMtUlZMN3UtLTdVdW83dzNCdjBKX0ZGMjhjcnlMTFRaRmk0eEhxM3VYdS1SWW5aS2lHYUVTRm16MUg1bW5xOHpFcnZwaXE0cnE4dHVTSjBjSFdYUHBPTDQwQVo2OHNZUElsZS1NNm1vLVRET1E?oc=5>

### Applied Materials Jumps 11% Ahead of Earnings; Lam Research Surges 9%, ASML Rises 6%
- Summary: ASML shares rise 6% in market reaction to sector moves.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcjFldU84UWg4b21Nd1pyd2VsaXlDaWhDRUk3THdxQ0xtTGZpWkUyYnpwRnYyNDFZbk1FSDQwcTZhaXlmQmNJY0x6cDF3QkhWdnNLUkc3dnc1eGZYUXotUFpGN2QxSC1sVVlQWXZ5YVJDZzUtcVlzZWdYWWR2NDlIOFFiRWwzMTNqclJLSDJQOFNjajJ5NVJVQjZLX3preUgwNHN2R2FOMlNITGwybGJZckFhQmxVQUJmSVJxc0Y5dmk?oc=5>

### Wall Street's Next Blockbuster Stock Split Could Come From This Chip Equipment Giant
- Summary: Potential stock split could increase liquidity and attract investors.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNbC1ITm02aU16TDlXT2Z4Z2lHa2lBdTc0ZmhHNl9iUWZCVDItc0tTOTYwS1JnQjV1emdfc0VpU01EdlZzWWhtUkxBaV81NS1rS3JqdUhIaGl4Z183a19qOHRzaEpZQmJfZFRuZkJzSzUzTk5uQVVzQzRlckVJUGhQQlJPc29yX0huWWxSMTIycGNGdTUydVc5aTROVm1aTmJNbGc?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ASML** | **36.84** | **1,285.50** | **1,968.54** | **55.20** | **577,016,561,664.00 USD** | **45.21** |
| AMAT | 30.19 | 11.80 | 29.59 | 24.80 | 302,320,943,104.00 USD | 66.02 |
| LRCX | 35.15 | 21.00 | 28.50 | 54.40 | 292,031,168,512.00 USD | 45.50 |
| KLAC | 39.42 | 31.43 | 31.34 | 28.90 | 204,955,992,064.00 USD | 31.90 |

Peers fetched as_of: 2026-11-12; ASML reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-14
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikwFBVV95cUxNcjI2cTBhSXUwVW5rMnZpZWgxamluLV9IaGFZU1l2OVRWb1liUl9HT0Z6WE9sd1FNZHZiTTRmZ1cydTI5U19ULXFWbDVuRzRHX2lGS0V3eDM1d1A0VDc4STVCdFkxcnNrcFEtUlJxTDhtdV8xbUZhVEpSeUZBaWxpMmNhRE9yd1V1MnhaN1JzSk1XMTA?oc=5
- https://news.google.com/rss/articles/CBMi8AFBVV95cUxOd29NTTJ4S1BBcTZXS3B2ZDg3MmNMTUhmc2tyUzU1WDNQQmhZMlJtbUJuc2dSQ2FWaHIxRllzcVJxSWZrQVMwb1JZTkpFSUxFVkhhY1R5N1lIQzY4Qk5ZQnh2aS1lbmw4LXBlY1FSUzV1dHl3REhNSlFNWVNXUGJBVjFERk1WbFJMWnk5S25aQlRBT1RVOFhtUG45VHFPUnB0UUVwZFFGa3pxZ1pLUnJEMXRpbXowckNYbWVjUk8yOHZVM3AwdXl1NW95ZHZZZjRTTDZ4cFlZX3pXSWk0ZkZPbnpWR1lIS3dmS2RRQ3pLcmI?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOTEJmcmo5NC1QbjgtbFBXakJrbW5XcGdnczg3OXdsX0RyXzl0YnQ1UGt5bTFucWh6WkVLVURyb3NLalROT2dyQy1UY1dUeVRvQkxSMmlYQTBIM3d3dXdubWVrYzRlN25PdGhOcjVsRmpiN2RnVzRmU1lIRG5YVF9kYzNaZUxoTWxsVExj?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPYXZuNWI5TzU5R0hjNjZlcnQ4ejRVUU0tdnNQbWFYc0Q3cmxLbzZmLTBUTW5GTFB4WmVXbm9rdTQ3by1sUnJkcDZobmdtT0RqYV9uM3FlSVVJUWRhWG4xdFZXLUFuVnE1Z2c0TkEyUmhqR1BySHUyN0hsRjhlWlpqTExGQ2dmVmMzNldXVHctS2FKYW0wX0xyLQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQOWJPSWVFQlpaQXFOSnBPbFNjNHdudmN2U3dfWVpMR0hJSzlIUHhXeW5XOWp0bXdPM2ZmZXdWd3U1U204aUtWLXRmcHc1NUE4WW5Jd2pKUkVObE1Ob2twcFVCa2RVQmVLeU9wWjRrTEdrSk9fT3l0cWVGTVRqZG9ycE4ycVB3ckdGTHBSeUJNYjRhczlLb2ZlaHlwaHd0dDY0cmRn?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNUjBycjNVVk5BTlZ4cllqcXkyZGtfSFplMEJTQ2NadEZzVE4wSDdPdmRNeUhkdmoxRktGV0d3U04teXE4ZmNPSndnUVBPQkFzdEJUNUwtSTg4dUJxSDktQ1doTGJ5MjhYc0tIakRYdGhPWWFUZXQ0My1MM1JGcG9NVklncHRnOWljcTVWNVN4TlRLaXJnRTZyN2Y4TXNrT0hTMlE?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQeHJIWnlMcmRhdkFXb0l1TWJEOWVlMGF5ejFSSHE3QzJ0c1dQWjUwdTJIRDU3c0NwdDVYSWFnX3NfX0J3Qkhwam9xYV8tbHkySFI1RVBPOXdYdUhqMFBnWmd1ZHZDNzl3UEk1UkdHVWYtaUNfVS1qeDhSQkNxQi1fcDZKV1lJNXR4NWNaVUFqQ3Q1TGJSQUNqUjd4UlU4T0ZOUlRMVG4wdjR0MUZhbkNBRHlpMERvTXA1czJBS2lzRENJaVN5QnlOTHJVTGxHRHV4VjRF?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOR1otbFFTYXl3Uml2cVNoLUdsNnVSd2Nvc08yWUdUd0lCdTdEamdZNUxjWmVEUllVSXNYUzE5cV9WRXlBZWRvdkdZeEVwTnJFdEFQSk9jYWxYb2pUQ21HX1ZndXdiLTN0UndHekRUd3FGQi1vckN6b2pfYmRfMllUejNER2JXRmNqUGVSYzN0NGdhOEU?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxNbmpJNTZhaWVFTXlvendJVXotM2VCSHVNNHh5YzNiTl9kcF9pb0E0UEJPdV95cHVfbWFpZEZJZk1IVWMtcERsNXdUR0lrSEczWWtSdHU4YmR5Z3NIQnpzbnB3QzRFNFdNRXRxaG84ZXZmMUEzcnJnSFl5bHdYekEzMUN3?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPZXlUOGlTU0NidTJteW95YnhwS1dwODlaR3VSVkNUVm5hU3NHcFJhWDFIN3ZtWGpMNWIta3V3OU9zQmNkcjY0dmtnamNFeUIzWlhOSHdEeldRV0U0dHdfdHdCYW9zN0JuYzJjT1BvaTRoYmY2enJoLWdHMXR1YXB6bkJySmlrZU9QZGUzMFB5T19hUTZEUnQwSk9SWQ?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPNFJDYWUtVU15R2hFVVRXVFVtTXJUS0F2Mk54VU9UQlFVckVYLVBIdHFveWpzdm1ic0VaUDZ0dFBrVUQ1WVF3YjlSWmxUMHVTZ0x6WTNBNThQRmp2YXJUUkpkMWoyUi1vS1RBc2RuajlJQjBkcjRiLXFVRHN1N1RpRFczZEE3Nll4VkN4MWxNT2NtYklnU2ZHcmpYMmxCa1FvNVVSS2NRRjBaNXpOTWt5R1RMa28yU3h2ZEN2N0JHdUNJczBYODNv?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNT2VvS1NkSk1JLXo4bHNuNU9mZmg2MWg4NFdjZlZkVk5oeEdwdl9aZnVwR3ZuaWtMR2NXbDBvWmNPQWNMdHJzZ3hjTThhWmp5OXliV25DalZLaDNfTHRyTEJuVDYwUWRWT25UWXZDNk9WWTJfM291YjhJYUVOODhONDJJX2JRTUpGQXdoNkhJUGU5bEpRdjFCZXJ3REZ3UGR1R3prZ1hPWHVJSkFqak5CYWVNbFNDdGZXRExIbzRjS1dqZ2s?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNMzJMWjdYVU5YclVORFZvcFZmRFBiM3FMVDZSbTBDUmJhSmtVODlvV0RTSzRudTBReDNNLVpYcnhaUXoxMG9rOHh3T1NhQ2R6QzFtbFBjZVpUdEl4bmlxWDQ3LWR3VUJLWFpZSVV4OW9vNVE0SzJOdDI4dVhXMFBaTzZqX0k5d2xDSjR1Skt0eEx6WnRrOXh4TF82akd5TVk?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQNWJ6VG5ub0JyUFI4ck5Qb3A2M2NCNVh5VkdjZmhub0VZb25zQndfcFVYV0ZDbDhMSVFMNFpzaG43V2FjRHBBNnRGOWk0WG0wajZ2Y3lsVmQxR1ZIT19xZUdNMDNYc2N6SlBJcGhETDZ2RkJra09KOThmRWhqdk9IVlZ1RlBLN2p2SFE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPODlhWk1sTmpvU3g5VlVXMXRoSWRGRnJNWWhPZ0U5UnFxVXVxNUV4eGt5Yk9hUmJnNGd3MzdyM2h6Sk9NUlBBbXo0Z1dxa3ozUVNnZ2d5M0o0QVZGRjFXMllUYWpQM2dmdUxlOUZOUlpZSHRWb1dZNElJcy1HMHY3dDJ6dzlUdjVLNDlBcWxYRW9vUHRWZ0Nn?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxObndWMC03WmxrTkpGUTdVZ1phdWxvelRCVzBqVVNhc3AxWGljdnd5SVF4QTdpTzBIaTFmeHgzemRqek5LcHY0REs4SDFURUFFS2ZzajFCdUFSWTkySWE3SjhGZVM1NTZuQmpDQk45eDVWVE1zcEdscUoxX2h0U3htUkZLc2RtS0ZsNDFZ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNQUtCYWN1cC0zenNRSEdqaXNpZ01mTGNFTG0yZlJpTHExMmNJUHVBenM2VUNJcnMtUlZMN3UtLTdVdW83dzNCdjBKX0ZGMjhjcnlMTFRaRmk0eEhxM3VYdS1SWW5aS2lHYUVTRm16MUg1bW5xOHpFcnZwaXE0cnE4dHVTSjBjSFdYUHBPTDQwQVo2OHNZUElsZS1NNm1vLVRET1E?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcjFldU84UWg4b21Nd1pyd2VsaXlDaWhDRUk3THdxQ0xtTGZpWkUyYnpwRnYyNDFZbk1FSDQwcTZhaXlmQmNJY0x6cDF3QkhWdnNLUkc3dnc1eGZYUXotUFpGN2QxSC1sVVlQWXZ5YVJDZzUtcVlzZWdYWWR2NDlIOFFiRWwzMTNqclJLSDJQOFNjajJ5NVJVQjZLX3preUgwNHN2R2FOMlNITGwybGJZckFhQmxVQUJmSVJxc0Y5dmk?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNbC1ITm02aU16TDlXT2Z4Z2lHa2lBdTc0ZmhHNl9iUWZCVDItc0tTOTYwS1JnQjV1emdfc0VpU01EdlZzWWhtUkxBaV81NS1rS3JqdUhIaGl4Z183a19qOHRzaEpZQmJfZFRuZkJzSzUzTk5uQVVzQzRlckVJUGhQQlJPc29yX0huWWxSMTIycGNGdTUydVc5aTROVm1aTmJNbGc?oc=5
- https://news.google.com/rss/articles/CBMigAJBVV95cUxQSG5ZT3VlMTlyQS1TZTlXU3UwemJwRnhSM2tpV0pXaEpHZjRwT3VVeWVITUpRZDZEX2VTWFIyek45U1FjUFRIZ1BTZFJfY3AwMkc0dkQzcEczYXdOWEJMUGdla0N4Q0NFS2tHakF0SDF4QnRvODgyV3hBZHlhX1lhU3J2MDBxaE5RUHlwV2Q4bGd0ODdyRDg3blM5MEhTMXMyeGZkcTNia0hXTjBoRGNmY2R0eG40eDZBZkZfUEh3RmJ3ak1lYkd5TjY3aFFVMnF4ZlgtTTZNMjcwdEk5Y0cyUlltdVRIbTJTYWx3dmlEbkpRNUUwbTZ4cGpKN0FBNGg1?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
