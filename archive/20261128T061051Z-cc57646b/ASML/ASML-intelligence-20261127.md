# ASML Intelligence Report

- ticker: **ASML**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/ASML/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ASML/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:14:19.237787+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 6, 'ai': 10, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/ASML** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 16.0%; oldest publication 2026-11-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1325.8199 |
| Return 1D (%) | 1.7451 |
| Return 1W (%) | 4.7069 |
| Return 1M (%) | -18.9384 |
| Return YTD (%) | 24.6842 |
| Return 1Y (%) | 28.1446 |
| Annualized volatility (%) | 50.0692 |
| Beta vs SPY | 2.2209 |
| Max drawdown (%) | -36.1866 |
| Sharpe (rf=0) | 0.7120 |
| Downside deviation (rf=0, %) | 33.9836 |
| Sortino (rf=0) | 1.0491 |
| Historical VaR 95% (1D, %) | 5.0250 |
| Historical ES 95% (1D, %) | 6.6569 |
| Correlation vs SPY | 0.6663 |
| Tracking error vs SPY (%) | 41.5963 |
| P/E (trailing) | 32.62 |
| P/B | 1138.41 |
| EV/EBITDA | 1743.22 |
| Revenue growth (%) | 55.20 |
| Forward P/E (estimate) | 20.91 |
| Gross margin (%) | 54.34 |
| Operating margin (%) | 38.55 |
| Return on equity (%) | 65.64 |
| Free cash flow yield (%) | N/A |
| MA50 | 1602.5222 |
| Close vs MA50 (%) | -17.2667 |
| MA200 | 1596.0011 |
| Close vs MA200 (%) | -16.9286 |
| RSI (14, Wilder) | 38.4804 |
| MACD (12,26) | -80.4348 |
| MACD signal (9) | -74.2297 |
| MACD histogram | -6.2051 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ASML': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1325.8199 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.7451 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.7069 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -18.9384 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 24.6842 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 28.1446 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 50.0692 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 33.9836 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.0491 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.0250 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.6569 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6663 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 41.5963 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.2209 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -36.1866 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7120 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.9122 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3370 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.5520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 65.6360 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 32.6235 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.4804 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -6.2051 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -17.2667 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -16.9286 -> Clearly below the moving-average trend level.

## TAILWINDS

### ASML Stock 12‑Month Price Target Raised to $2,436.94, Implies 92% Upside
- Summary: ASML Stock 12‑Month Price Target Raised to $2,436.94, Implies 92% Upside
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxPRjFTdFR5c19TSXh2SERzMUZoSU9BVW5lTmwxaXMtSVVkdGh6SWN6V2QzSGFMa2tLbnJSZERBTkp3UDVEU0lnMWR0Zmx2NWV1Q1RpckRmWFpUMWsyaVhmZGttZF80aVZuck1Way0yamFPWGhlT1FTZ2lwQnBrTkExSm5pQ3JRYnd2bjhjZHQ3LS1WdGFmWmxIazZ6WnR0YjU2QkV0MDVjVzlrTGtidkd3N3hPd3pVSlZfNUJRSjdzWldSeWhjRFVOR0hyMA?oc=5>

### ASML Holding NV Stock (ASML) Moved Up by 10.09% on Nov 23: Facts Behind the Movement
- Summary: ASML Holding NV Stock (ASML) Moved Up by 10.09% on Nov 23: Facts Behind the Movement
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNUUw1aUVCMGN4bUpXamVoaUdhOGtvSGxZcFR4c2g5SGJwRWpsNzEzUFI5cmFoNDl2VkF3RWhIa2xBRGh3SEwwUV9wRzNkaGplU1hmZGxtdmpaWV9OTkFjcXRRdVM0Wi02MzdPbFFxcUV0OUEtcGstcUM0eTJRUlNtOUhEZnAyRGdNa2ZR?oc=5>

### ASML Holding NV (0QB8): New Buy Recommendation for This Technology Giant
- Summary: Analyst upgrade signals positive outlook for ASML.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxOekgzM1JFQ3hqZTVVeVE2czdqa3hwTjJjUUs3cmFkeUpTQ1N0Ykw0Xzh2R3BacWg2U2FpUFlqTHFqSTVCR1RNbWlCNlhTNEZaT2lWYUxwSlQ3Smp0ZnBHalRiZVVkUEh5dVI2NlJKcG9uNHlNVnFsUGQzSm82UWoyRkZ3azJNOFVmS2RjckdPZmxGTkRqZVRxdHoxQnluWGpEVjRKdWNxVmdBYlZMMzJobm1wUTZ1TXdWdkVYdWc0Q2JUanB5dmR4VnJ2RDB1NWtIZjF1VDlhUVQydmlNUk82bDlVb3pPY3IwOU5PNw?oc=5>

### ASML Holding N.V. : Buy rating from Bernstein
- Summary: Bernstein’s buy rating indicates favorable analyst sentiment for ASML.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPSndXRFRWbGgtU29kVUZjVG41WGNQUm9NUUFvaWQxdmxJUjR4VjJvelBrUUh3eVZaalR6X2V1R3dJakhvRGRDd1h0QnJSclZnSk14Ym1NdHI5bWNHaWR6ZUpBaGIxdWpjUGlLeVBJR1BrUzlQZjNYaGFrWC1lYzA2MTdZU1lDM1FrMjhNVkU4Y2xleWVEVTJwNGN1Yw?oc=5>

## HEADWINDS

### ASML Stock Fell 25% In The AI Selloff, But Its Outlook Hasn’t Budged (NASDAQ:ASML)
- Summary: ASML Stock Fell 25% In The AI Selloff, But Its Outlook Hasn’t Budged (NASDAQ:ASML)
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNS0xMdThabnAwMURidkl0a3A3alJKVzN2bnJTdThoMUZFQWdaZEEyNGh6OXJmQWQzSXlKM0Y4ZTN0bmNUdmVxRDY2MUlXWmVnNVNuU1VYZEhUMHdKcXlQbHZzMDBER2hlTHhfd0NWVmRkQnA5cHhBb25FTHUwTkpnU3JhQzF5dlNKZ3ZPd1RSR09lZXZkZERYc1FORkhCSlZERlBQM2xPQkg5ai1YMHF1MGFGeV8?oc=5>

### ASML stock falls 6% as Dutch lawmakers oppose US chip export curbs
- Summary: ASML stock falls 6% as Dutch lawmakers oppose US chip export curbs
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPLVFLdGZycW5fUm1fcjI1U0JvcGZxV2g4NXNWQ3l5ZUV5cjgwLUtJWXpoLXNVUXVEZWRSYjBqc1B1S2J6Tk9nc2N5WV9VMDN0bVgxQzNWTldOR0NIdS1wcE1kZ0puU2p0U1F6Z0lmTWNpQzVXYWhmSW5DZ19PcXVCNUJCZGU4bHZ0OUJSS2J6MFlONmlPSlBhRTQ1V3lfRW0zbW93ZFoxR0RIblg5dUl6OHM3V2tHdjRJOTJoQUhCSQ?oc=5>

### ASML Holding NV Stock (ASML) Moved Down by 7.01% on Nov 25: Drivers Behind the Movement
- Summary: ASML Holding NV Stock (ASML) Moved Down by 7.01% on Nov 25: Drivers Behind the Movement
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOU0g5ZEFIeE9tY2hvbW02TjZ2akZKQXllWlUzTFVsclJfUi1nQU5XT3lrQWhOUV9iWHBZTk5IVkxqaElLYUpZTUQweE1CeTFhQlR2R01FMzVRTGFGYnc3Q183bUM2T2V1aW41MVJhYk96S1F0ZUg3VElOVUFuZ3hIamptNjA0UF9QLXdz?oc=5>

### Netherlands Tells Washington It Won't Take Orders on ASML's China Sales
- Summary: Policy limits orders for ASML’s China sales, restricting revenue.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPTWNSb29ZQlBNclFMV3dUQ1hVUGVEQ0Nxa2JZV2paemtnVDFzWXZXbENnT0JRUWJGZjZFckd5STBNakpkZk5NMnh2U29mNHA4amlUdEFDRmJjNUpmWU9pTUgxbUUyUnFOMFNGN2wzWHZ5ZWxlTmVhZnNuVUJPVHdjTklqUE9zYlVwc2l1SkZndXF3UkFsaTBMRm5qVDlzdw?oc=5>

### ASML Caught in US-China Chip Battle as Netherlands Vows to Resist Trump’s Proposed Export Curbs: ‘We Will
- Summary: Export curbs threaten ASML’s supply chain, creating a headwind for the company.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwJBVV95cUxNbnY5aGU0UGIzS0U0LS1HSnlsRGFxZ2thb1JBN3BSa0tMM1VuMVhIcWtwMUZZSG8wVk5DOVlmOFA4UHRBbU1pbFNCTXlJU21Ua3hpbjM1by1jTEFfdEljZVNjb2hRRzRIZG5ZUjZMNnZDRVh4SHF5YXJnODRmTFNsdXh4cEpNamkzTWw5STdrQWE4MjlmckhVZzJzRmc1SUpPeFgyaFJHR3ljQ0RCQ0tVVVJZd1liUEpsajUyNEJhOElPRjNJa0NXa3B5ZXFELVBLVHFtV3RnT1FPbG9iZDRlSjk4QWx3SzAza0U3U0lwTGwxd3drNmNFZ3o0c1RkWlR4X0dBSUgxc1Utd2pLbmdQemZSUQ?oc=5>

### ASML Sinks 7% in a Week: Dutch Lawmaker Warns the MATCH Act Is “Disastrous for ASML.” Time to Buy?
- Summary: Dutch lawmaker warns MATCH Act could harm ASML, causing a 7% share drop. Regulatory risk may impact short‑term performance.
- Date: 2026-11-26 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPaXRjLW9YY2ZrbW1JWFpDLUpJYUR2MHVWUl9jOFVZVzh0Y2xLSEhVR2hEeXlYVzFNZHhyVUF4Q3V6LUl0NzRMOFRJSlJ1aHZ1VEN4RXh3RDJLWXZnbUJYazJmY1ZaZzlINkpTTXZCYUhESzFEXzNsSW9kX1BPd2p0dm0weGRlV1VVbzVibWsxU2hDRkd4SzdUS0JfZWVtWW1DMjRuZm5KTUpGVmp5a2lLNnI1V1hyMnlTZEE?oc=5>

## CATALYSTS

### ASML (ASML) Q2 2026 Earnings Preview: $7.94 EPS Expected, 8% Options Swing; Triangle at $1,800
- Summary: ASML (ASML) Q2 2026 Earnings Preview: $7.94 EPS Expected, 8% Options Swing; Triangle at $1,800
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxNUk5WVnlaMVZ4c04zTVNBV2ZTSDdGOGlsM2xvZUFVZ042UTI3U1p6N0tiaVFJNS1qZmNOTEF1NTBQaWxCWUpLVWF2eXRVSG80R0tTenZGeW5XRGVfMU1RbEEzeXhQS212QVhweVA5ZFdmbFJUamR6UTgwOXpTN1lDZDFtSVRMZWpSSndZclJ6RmxvNFo5VS11RnBtU2xRdFhDT2JkMWEtY2RvdW8zdTkyaE00dlB2WDdVb082OHVROFBoWVRwaEt1NUJn?oc=5>

### ASML surges 9% as chip stocks rally (ASML:NASDAQ)
- Summary: ASML shares jumped 9% amid broader chip market rally.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTFBDTHVWdFhBU1B6Y0RWNmxFZG13akZXdjZGUXkxb1F5cGY3cVExejRnNmQ1bi0tUGl1akRvNDR5Y0o3UmlPaFp4c1hfbEV5eWdyOVhrN3FXTzl0SThHeU9KeFVpNkJBRG54Rnp2THdTRk0za3hsUlI4eWtoWDk?oc=5>

## RISKS

### ASML (ASML) Can’t Meet Demand. Is That a Strength or Risk?
- Summary: Demand shortfall may signal capacity risk.
- Date: 2026-11-26 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQVzlaZGR2OUNRV1AtMXNtNWw2Rm0zN21ldGM4WTV4dmlqQ05iODV6X2x1OVlPdlhyOHlvZG9EcHFtckpiUzlhbl9qbXNPRFBJdWRVbW1ZM2NCaHNnX0t2YW9hOXVrWEl1NHIyOHhmT3IxdktYSGlSelNkcHVGMF9DNnlPTHY3TjdxT0JXVmFEc2RPUQ?oc=5>

### ‘Disastrous' for ASML: Dutch Lawmakers Revolt Against US Push to Tighten China Chip Curbs
- Summary: Dutch lawmakers oppose US chip export restrictions, creating regulatory uncertainty for ASML’s China business.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQdi1yQ1BMQ0FZeTFWcTN3RWtjaG1fWTJScHZidExKTWxqeVFxNGthTHNXa0NxMXNuRlAzU0F4Z2NlUzA2bEdPOTE2NXlRWmtEbEpZQV9aSW9pMklxN1FrSWpOODF1czN5QU5LbVE5RWZiYjY2b1otSHlmbE1OOVZqMmp1X1VfV3B4WnVV?oc=5>

### ASML Can’t Build Enough Machines for 2028. Is a 20% China Risk a Reason to Sell, or Buy More?
- Summary: ASML faces production capacity limits, raising concerns about meeting 2028 demand and potential China exposure, impacting future growth prospects.
- Date: 2026-11-26 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNb2Y4aU5RWGRYZlNjeEY4WlJFOHN2Zno3M3hEUmo2WXlORjA4eEh6cUFUc0xRaHMxczBjaWZyMnRfdi0xX2tMME12ZHBtYmV3eHZjNFUxSkJYNVo2TkZldEsya1VsUkVaM21BZzR6dlU1b2ZDV2FmanZfUndvOFB0S2xfdHdDeDYwbmN4MTZENUNITDYxUlVuYzlNeTM4U3RuQ0pEVFRxSk50NmlpWlRuUFhUZkY?oc=5>

### What ASML Holding (ENXTAM:ASML)'s China Export Curbs Means For Shareholders
- Summary: China export curbs could limit ASML's ability to sell certain high‑performance lithography equipment, potentially affecting revenue and shareholder value.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxOXzJUQ3dOUWNGMVgtZDlBX0hyUnRuSndVakVEeVA1X0Rzc1FQaGF3SGVXZ0huUjRlamYwVHhQSTlHXzE0U1I4QU5NZWsybjB0VmxMUTJ0a1VjVzVSZFdsU1FlRXcybDRCRzdZM3lZTm1zWTdsUXh3UWpSV1l4Z201azhjRTFmSGszaTJJZ2NRUWFHSHRjVlI5V19pR01UQzU4VVdHa2dXbHphdGZIYUZXTW9zbVd2MzdvUmtabnJjaXlSaTNVeEhXWlZnLUNydV9FeXdqN05xUmjSAd4BQVVfeXFMT0g4WU9lVWJPc09JZ0o0Z1g1ZUJSUHJ3S3MwN1RXMUNpYkFYU2F0bGZwOVRRZF9lb2UtbUlrdkZ6Zzl1clBYSDlYbno4Ry1WbUlNcExpUG9pNWlGSzhwMGZ1VWNhajlJX2luU095S0hxcEtMNlVGdnNhZU5PbkpNeDd4ZHBBd1RZQ3dHRU5lRG82U2tXZXVUTkdfbFdJVWdPMDM1X2ZobENPb1lxcnhUM3FXNEpVYWJVU2dpYnZ1NHJObW50TU9CQ2U5bmU0VWdZUzdleFRha055RXZSNHpn?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ASML** | **32.62** | **1,138.41** | **1,743.22** | **55.20** | **510,994,513,920.00 USD** | **28.14** |
| AMAT | 25.52 | 9.78 | 21.19 | 53.10 | 255,570,132,992.00 USD | 29.49 |
| LRCX | 28.72 | 17.31 | 23.43 | 54.40 | 240,702,750,720.00 USD | 24.78 |
| KLAC | 30.69 | 28.14 | 28.09 | 28.90 | 183,535,288,320.00 USD | 22.16 |

Peers fetched as_of: 2026-11-27; ASML reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-14
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

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

- https://news.google.com/rss/articles/CBMiywFBVV95cUxPRjFTdFR5c19TSXh2SERzMUZoSU9BVW5lTmwxaXMtSVVkdGh6SWN6V2QzSGFMa2tLbnJSZERBTkp3UDVEU0lnMWR0Zmx2NWV1Q1RpckRmWFpUMWsyaVhmZGttZF80aVZuck1Way0yamFPWGhlT1FTZ2lwQnBrTkExSm5pQ3JRYnd2bjhjZHQ3LS1WdGFmWmxIazZ6WnR0YjU2QkV0MDVjVzlrTGtidkd3N3hPd3pVSlZfNUJRSjdzWldSeWhjRFVOR0hyMA?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNUUw1aUVCMGN4bUpXamVoaUdhOGtvSGxZcFR4c2g5SGJwRWpsNzEzUFI5cmFoNDl2VkF3RWhIa2xBRGh3SEwwUV9wRzNkaGplU1hmZGxtdmpaWV9OTkFjcXRRdVM0Wi02MzdPbFFxcUV0OUEtcGstcUM0eTJRUlNtOUhEZnAyRGdNa2ZR?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxOekgzM1JFQ3hqZTVVeVE2czdqa3hwTjJjUUs3cmFkeUpTQ1N0Ykw0Xzh2R3BacWg2U2FpUFlqTHFqSTVCR1RNbWlCNlhTNEZaT2lWYUxwSlQ3Smp0ZnBHalRiZVVkUEh5dVI2NlJKcG9uNHlNVnFsUGQzSm82UWoyRkZ3azJNOFVmS2RjckdPZmxGTkRqZVRxdHoxQnluWGpEVjRKdWNxVmdBYlZMMzJobm1wUTZ1TXdWdkVYdWc0Q2JUanB5dmR4VnJ2RDB1NWtIZjF1VDlhUVQydmlNUk82bDlVb3pPY3IwOU5PNw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPSndXRFRWbGgtU29kVUZjVG41WGNQUm9NUUFvaWQxdmxJUjR4VjJvelBrUUh3eVZaalR6X2V1R3dJakhvRGRDd1h0QnJSclZnSk14Ym1NdHI5bWNHaWR6ZUpBaGIxdWpjUGlLeVBJR1BrUzlQZjNYaGFrWC1lYzA2MTdZU1lDM1FrMjhNVkU4Y2xleWVEVTJwNGN1Yw?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNS0xMdThabnAwMURidkl0a3A3alJKVzN2bnJTdThoMUZFQWdaZEEyNGh6OXJmQWQzSXlKM0Y4ZTN0bmNUdmVxRDY2MUlXWmVnNVNuU1VYZEhUMHdKcXlQbHZzMDBER2hlTHhfd0NWVmRkQnA5cHhBb25FTHUwTkpnU3JhQzF5dlNKZ3ZPd1RSR09lZXZkZERYc1FORkhCSlZERlBQM2xPQkg5ai1YMHF1MGFGeV8?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPLVFLdGZycW5fUm1fcjI1U0JvcGZxV2g4NXNWQ3l5ZUV5cjgwLUtJWXpoLXNVUXVEZWRSYjBqc1B1S2J6Tk9nc2N5WV9VMDN0bVgxQzNWTldOR0NIdS1wcE1kZ0puU2p0U1F6Z0lmTWNpQzVXYWhmSW5DZ19PcXVCNUJCZGU4bHZ0OUJSS2J6MFlONmlPSlBhRTQ1V3lfRW0zbW93ZFoxR0RIblg5dUl6OHM3V2tHdjRJOTJoQUhCSQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOU0g5ZEFIeE9tY2hvbW02TjZ2akZKQXllWlUzTFVsclJfUi1nQU5XT3lrQWhOUV9iWHBZTk5IVkxqaElLYUpZTUQweE1CeTFhQlR2R01FMzVRTGFGYnc3Q183bUM2T2V1aW41MVJhYk96S1F0ZUg3VElOVUFuZ3hIamptNjA0UF9QLXdz?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPTWNSb29ZQlBNclFMV3dUQ1hVUGVEQ0Nxa2JZV2paemtnVDFzWXZXbENnT0JRUWJGZjZFckd5STBNakpkZk5NMnh2U29mNHA4amlUdEFDRmJjNUpmWU9pTUgxbUUyUnFOMFNGN2wzWHZ5ZWxlTmVhZnNuVUJPVHdjTklqUE9zYlVwc2l1SkZndXF3UkFsaTBMRm5qVDlzdw?oc=5
- https://news.google.com/rss/articles/CBMikwJBVV95cUxNbnY5aGU0UGIzS0U0LS1HSnlsRGFxZ2thb1JBN3BSa0tMM1VuMVhIcWtwMUZZSG8wVk5DOVlmOFA4UHRBbU1pbFNCTXlJU21Ua3hpbjM1by1jTEFfdEljZVNjb2hRRzRIZG5ZUjZMNnZDRVh4SHF5YXJnODRmTFNsdXh4cEpNamkzTWw5STdrQWE4MjlmckhVZzJzRmc1SUpPeFgyaFJHR3ljQ0RCQ0tVVVJZd1liUEpsajUyNEJhOElPRjNJa0NXa3B5ZXFELVBLVHFtV3RnT1FPbG9iZDRlSjk4QWx3SzAza0U3U0lwTGwxd3drNmNFZ3o0c1RkWlR4X0dBSUgxc1Utd2pLbmdQemZSUQ?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPaXRjLW9YY2ZrbW1JWFpDLUpJYUR2MHVWUl9jOFVZVzh0Y2xLSEhVR2hEeXlYVzFNZHhyVUF4Q3V6LUl0NzRMOFRJSlJ1aHZ1VEN4RXh3RDJLWXZnbUJYazJmY1ZaZzlINkpTTXZCYUhESzFEXzNsSW9kX1BPd2p0dm0weGRlV1VVbzVibWsxU2hDRkd4SzdUS0JfZWVtWW1DMjRuZm5KTUpGVmp5a2lLNnI1V1hyMnlTZEE?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxNUk5WVnlaMVZ4c04zTVNBV2ZTSDdGOGlsM2xvZUFVZ042UTI3U1p6N0tiaVFJNS1qZmNOTEF1NTBQaWxCWUpLVWF2eXRVSG80R0tTenZGeW5XRGVfMU1RbEEzeXhQS212QVhweVA5ZFdmbFJUamR6UTgwOXpTN1lDZDFtSVRMZWpSSndZclJ6RmxvNFo5VS11RnBtU2xRdFhDT2JkMWEtY2RvdW8zdTkyaE00dlB2WDdVb082OHVROFBoWVRwaEt1NUJn?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTFBDTHVWdFhBU1B6Y0RWNmxFZG13akZXdjZGUXkxb1F5cGY3cVExejRnNmQ1bi0tUGl1akRvNDR5Y0o3UmlPaFp4c1hfbEV5eWdyOVhrN3FXTzl0SThHeU9KeFVpNkJBRG54Rnp2THdTRk0za3hsUlI4eWtoWDk?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQVzlaZGR2OUNRV1AtMXNtNWw2Rm0zN21ldGM4WTV4dmlqQ05iODV6X2x1OVlPdlhyOHlvZG9EcHFtckpiUzlhbl9qbXNPRFBJdWRVbW1ZM2NCaHNnX0t2YW9hOXVrWEl1NHIyOHhmT3IxdktYSGlSelNkcHVGMF9DNnlPTHY3TjdxT0JXVmFEc2RPUQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQdi1yQ1BMQ0FZeTFWcTN3RWtjaG1fWTJScHZidExKTWxqeVFxNGthTHNXa0NxMXNuRlAzU0F4Z2NlUzA2bEdPOTE2NXlRWmtEbEpZQV9aSW9pMklxN1FrSWpOODF1czN5QU5LbVE5RWZiYjY2b1otSHlmbE1OOVZqMmp1X1VfV3B4WnVV?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNb2Y4aU5RWGRYZlNjeEY4WlJFOHN2Zno3M3hEUmo2WXlORjA4eEh6cUFUc0xRaHMxczBjaWZyMnRfdi0xX2tMME12ZHBtYmV3eHZjNFUxSkJYNVo2TkZldEsya1VsUkVaM21BZzR6dlU1b2ZDV2FmanZfUndvOFB0S2xfdHdDeDYwbmN4MTZENUNITDYxUlVuYzlNeTM4U3RuQ0pEVFRxSk50NmlpWlRuUFhUZkY?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxOXzJUQ3dOUWNGMVgtZDlBX0hyUnRuSndVakVEeVA1X0Rzc1FQaGF3SGVXZ0huUjRlamYwVHhQSTlHXzE0U1I4QU5NZWsybjB0VmxMUTJ0a1VjVzVSZFdsU1FlRXcybDRCRzdZM3lZTm1zWTdsUXh3UWpSV1l4Z201azhjRTFmSGszaTJJZ2NRUWFHSHRjVlI5V19pR01UQzU4VVdHa2dXbHphdGZIYUZXTW9zbVd2MzdvUmtabnJjaXlSaTNVeEhXWlZnLUNydV9FeXdqN05xUmjSAd4BQVVfeXFMT0g4WU9lVWJPc09JZ0o0Z1g1ZUJSUHJ3S3MwN1RXMUNpYkFYU2F0bGZwOVRRZF9lb2UtbUlrdkZ6Zzl1clBYSDlYbno4Ry1WbUlNcExpUG9pNWlGSzhwMGZ1VWNhajlJX2luU095S0hxcEtMNlVGdnNhZU5PbkpNeDd4ZHBBd1RZQ3dHRU5lRG82U2tXZXVUTkdfbFdJVWdPMDM1X2ZobENPb1lxcnhUM3FXNEpVYWJVU2dpYnZ1NHJObW50TU9CQ2U5bmU0VWdZUzdleFRha055RXZSNHpn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
