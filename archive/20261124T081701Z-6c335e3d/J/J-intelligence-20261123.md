# J Intelligence Report

- ticker: **J**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/J/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/J/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:36:04.845889+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 7, 'ai': 13, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261123T053847Z-45053549/J** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 157.5300 |
| Return 1D (%) | 4.5877 |
| Return 1W (%) | -1.4329 |
| Return 1M (%) | 8.5964 |
| Return YTD (%) | 19.9040 |
| Return 1Y (%) | 23.6377 |
| Annualized volatility (%) | 32.3468 |
| Beta vs SPY | 0.7809 |
| Max drawdown (%) | -28.8516 |
| Sharpe (rf=0) | 0.7257 |
| Downside deviation (rf=0, %) | 22.7911 |
| Sortino (rf=0) | 1.0299 |
| Historical VaR 95% (1D, %) | 2.9570 |
| Historical ES 95% (1D, %) | 4.8028 |
| Correlation vs SPY | 0.3615 |
| Tracking error vs SPY (%) | 30.3368 |
| P/E (trailing) | 52.34 |
| P/B | 5.65 |
| EV/EBITDA | 20.16 |
| Revenue growth (%) | 34.50 |
| Forward P/E (estimate) | 16.74 |
| Gross margin (%) | 22.07 |
| Operating margin (%) | 5.93 |
| Return on equity (%) | 8.00 |
| Free cash flow yield (%) | 3.50 |
| MA50 | 146.6488 |
| Close vs MA50 (%) | 7.4199 |
| MA200 | 134.8512 |
| Close vs MA200 (%) | 16.8176 |
| RSI (14, Wilder) | 57.2083 |
| MACD (12,26) | 2.6932 |
| MACD signal (9) | 3.3351 |
| MACD histogram | -0.6419 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'J': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 157.5300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 4.5877 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.4329 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 8.5964 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 19.9040 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 23.6377 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 32.3468 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.7911 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.0299 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9570 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.8028 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3615 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.3368 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7809 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8516 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7257 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.7364 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 22.0670 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 5.9290 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 7.9980 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.5021 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 52.3355 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.2083 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.6419 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.4199 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 16.8176 -> Clearly above the moving-average trend level.

## TAILWINDS

### Jacobs Solutions (J) Tops Q4 Earnings and Revenue Estimates
- Summary: Jacobs Solutions (J) Tops Q4 Earnings and Revenue Estimates
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNTllTWXF0RXl5VHozUHJ4TlZBbkFkZFdZZFRsRHI0NU02M201ZTNvdHBZdFhWd1R0WVhTS2t4eDBmUk9GX2FPY0lkdzg2TDRKWU1WVjlmTmFHelYzUk1yREp5VUxsRm5MLURLWE4wWkcwRnZzOVlPUm1ZX19RbnZucXhlUFJCcVlCQzRVeWo0NzByTlhnY3c?oc=5>

### Jacobs Solutions (J) Releases Q4 2026 Earnings: Revenue Jumps 49.4% Y/Y
- Summary: Jacobs Solutions (J) Releases Q4 2026 Earnings: Revenue Jumps 49.4% Y/Y
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOUHV4ZkJsWTZBYnd0RzZHM1k4VGp4alVQeHJySzN1TzJGWVFQVVhuaTdqb1JFRXNwMjZGNFl1TC1BNXpnUW1PZlVBbk1nVlFYdVZtZnhjQzNHTHBLQ29QRUF2Zno4VkhOTS1ZR1ZqS3g0dW1UUDEyY3NiVGZsWDBiM0FRUEpvOXJhZk9zUTFjTTdFTE52YkEzSllDVGpnUmxBTVl6QURzRFNPd0xUaWJUQ00weXU?oc=5>

## HEADWINDS

### Jacobs Solutions (NYSE:J) Stock Today: Unusual Volume as Shares Move Lower
- Summary: Jacobs Solutions (NYSE:J) Stock Today: Unusual Volume as Shares Move Lower
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQOWkzQUktajZ3M0h0YWxkQ1o4cjQ5RDIwc1J3SEJGc081b0c4b3Jhbl9LUjBCRzVjS1pZQWtLSHZvbFJRRUNwUjFfNzY5SjhrWTM5Y21VZERveDZEa3YtWU9IR0g0V2dxZFM2R2FLV3VIOUJRUklMek5oSU1JM2pLOEJnbTk1dEpQV1lQSWhtVDBzLVVsbjVFN2lhaWNCZ3NtMGNDZUFjcFo?oc=5>

## CATALYSTS

### Jacobs Solutions (J) Lands Sanofi Project Following Questions Over Whether Shares Are Fully Valued
- Summary: Jacobs Solutions (J) Lands Sanofi Project Following Questions Over Whether Shares Are Fully Valued
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQdzIzTGlKLTN0UXBlZzRZaVI1LWtNOERTdjdqZ1RmRTR1Y192TFdyWDRYUWJTeF9vYW5Zb1hJX3JPUzlxR3VyTE02bHJQY3ZhVTZldUt3eGpkRUx6ZTM2YjZRM0daMF9TRmJuWDhfU3FlMXotODV1S1p5X3Vid3J4QWhwNDQ2ay0yLVVyVHVVNVBDbXZmdEFLRVhlTWQ?oc=5>

### Jacobs Solutions earnings: What to look for
- Summary: Jacobs Solutions earnings: What to look for
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPQWl6TDViZDNYVHIyeVVLOEVQX2Z4MTlFQi1sUmVUdEVfWTdBMzh1blFvOEZ3X3lGZTVISkJWSGxlTzRMQzJpYmEzbUo5M05wcHhfYTU1RHE5am5tcFpjbUFublBwYW5USnBlVGh6RWI1cmJaMW4tcW1hOGpIMUJ4T0Jlek5Wc2NoSGNfWTB0WUFOM2dkeUtxUzJpU1R4dDU2R0ZkeGJ3?oc=5>

### Jacobs Solutions Q4 2026 Earnings Date and Estimates
- Summary: Jacobs Solutions Q4 2026 Earnings Date and Estimates
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOZThXbGV2ZXFDajJKdWgxSm95UVIySXFWQlY0TnVwTDdRMkVIYU5qZGVLcWZTc2k0WU9welVEOU00b1FGYUZELWpocGd0VXhVbWtKT0ZvMFlwcHJFUW1uNVpLZm9ZZmJRZGtfLWw5OWRrSFdHMS1vVkdSN0tueUFqeWxHTDdqbk5jWWxUSlVBbjVwNlhl?oc=5>

### JACOBS SOLUTIONS Q4 2026 Earnings Preview: Recent $J Insider Trading, Hedge Fund Activity, and More
- Summary: JACOBS SOLUTIONS Q4 2026 Earnings Preview: Recent $J Insider Trading, Hedge Fund Activity, and More
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxNWUhmZ0k3ZnR1N3FRUk1GXzV6ejd4d3dlMVlqSWd3T3JTR2hhSWlUOVVkSzlJSDdGd2p3Y2NDSWZncTdiRWpmZ1d4QUN2MUliaXNlX0lVT3BsbVBKMm1NTWlWUnNSbGY4ODRCd2NzNzQzc0dXSW1yUnNjYzZpTEFCLXBDazBIS1VUX2dWb1lSSkZfQUc1NFUxVGtkMy1aNGhNeExmb2xfWHN4NncySDlKbWllSXRIelFXU1pRYnFNRlozeWF5aDZLRDVXNmZybTdLLVBJcEVVMA?oc=5>

### Jacobs (J) Stock May Be A Bargain Despite Fresh Airport Upgrade Wins
- Summary: Jacobs stock appears undervalued amid recent airport upgrade contracts, suggesting potential upside for investors.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPZ3Vlay1FSHB2aVZSN3dOMVRzel9xVWJfV1hvZmwtMmhCQ0FaSkVRS1FydUNqeE83MzduLXgxMDg0QU9KQy16TDhabHpDNUdBc0EyTFR5TmdGS2hjSkNHVy1NbW9iR09OOW5ZMVNZMm5POVFnUjN2Ui12SzlVa3FpX3FjMUhiZTdvUS11WFFjNUhwNFhVcUE?oc=5>

### Jacobs reports strong fiscal fourth quarter and fiscal year 2026 results
- Summary: Jacobs posted robust Q4 and FY2026 earnings, exceeding expectations.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPdjZtQ0FobDlTTlVvNGhETXdsanctVVROd29QZ09vM3F0dmJWd2x2a1lsWmVfeDVnTldqT3dmTGpyaXZTNzZvLWdEaDRBN1ZhUnpISF9mOGRscGtyczR0RFpoYkZlSEdIa0JCQzVSaGtGMHBaLWFtNThKclVUSmlMcFlLN05aLXgtZHpfT2wwQm5HSUJJMWhwdW9wN2t2SUdUQlN1UWlHeExBOXM?oc=5>

### (J) Jacobs Solutions Expects Fiscal 2027 Adjusted EPS Range $8.05-$8.45, vs. FactSet Est of $8.26
- Summary: Company forecasts FY2027 EPS slightly below consensus.
- Date: 2026-11-23 | Impact: medium | Horizon: medium | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxOUzdmMi1QdW00dDZ0bFlYNnY3cU5SMHR2RHRXdFRsWEg4TGNrRDg2WTU2MjhKTXdxd2FqUmVTcHdCSEc0LU5xTXJKWlREeGhKb0xBRkowZW5jcWpzRDcyc3g0Rnd3dXoyWlJCcTZzalJya2FPaUoybTNLZ1pIR0JFbVpZenVmMHJaT1U5S3RtYWRGa1hfQ0lmOXpuQXptSXhsWER1S3BzWE1xNUVUZHdtVEpGUXJfSFpTT3dQNzkxMFNFN1FDWlY4UzJjTVBHdWZkNVRVUm90UnlvVlE?oc=5>

### Jacobs Solutions Gears Up For Q4 Print; Here Are The Recent Forecast Changes From Wall Street's Most Accu
- Summary: Company updates Q4 forecasts ahead of earnings release.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMimwJBVV95cUxObVE3bElrOFgtZ3YxM3lHcGNyQ21nbkFMWlg0WGZiMXpvOEdxSkJiWGZSQWtWVkZsV2JlbHU3ZlBjcWl2WDI4S252QkJhQ3ZONEFyMXBWTHZ2QXg4cmZsbEo1Q2JBMDhWR04tZ2NmWWwySlFFb1RVMUw5dDVZbm5sOEg4aHJidVlBdWZYQ3VXbWUxWW85X25wZlBPTGRGOEpxdVcyS1ZhRzZoRFA5UGJMbVVXU2RuN2V1STRiUkk5RXNkWEtyYmt3QVlOUGtwOE9nQnJYcXcwNmd0NXlFY19wTFhzX1pqa0xvZ3JLbF90c0lJZGxOalRFSVNrWnNpYlNUVjNHYzd3cERUb1cxX1JkZnNhLWtoc3lQeUI4?oc=5>

### Data Center Engineering Firm Jacobs Solutions In Buy Zone Ahead Of Earnings
- Summary: Jacobs Solutions stock in buy zone before earnings.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQbXhQNWRrZEdHdlhZRWlVZlhQLWFyRE5WNlRHcVBMVWZtVmpyY0RBaVlETFVoX3ctakJwRGRYa0RvZnZKNkdIUzdVRGVXMFlhVi1ZTXViek5LRmhtbEhOSEpVeTFjcDZEZkRJV1BCYUl5LUIxRWJZN0tKS1ZvVDhpZHZ3QTE2WXhMNmFNWUQ2UGt1VGVNdjNCaHo1eGhOR1p3bjh3?oc=5>

### Earnings Flash (J) Jacobs Solutions Inc. Posts Q4 Adjusted EPS $2.20 per Share, vs. FactSet Est of $2.12
- Summary: Jacobs reported Q4 adjusted EPS of $2.20, beating estimates.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxNWFk0aXFCTEwxSDhXcUdKcnljZ3JIWV80MVQ2RHpVeXZ4bzJ4UkNsRDJaSk9UT3Z5eWtmZFpXcXpQRG1Jb1hoZVZoTWVydTBzNk45YXlMalc3aFgwR3RhYy10LTlRQl9MS2VLbTRYWVctQm5fcVctbENZVG9aRm9Xd1FOdHk2RlFTa2NtcFo4LVNXdzNKQWtDNUpONE5hVkVpMWh1WmhLaTdCMVN5cUoweVZwX2ZDNHlzdWYwd09KMG9zVC0yb1ZpR1RSa2VfZnp6aFhPN3NIcUpaUnY3THhB?oc=5>

### When a stock grant vested, William B. Allen Jr. tendered 81 Jacobs Solutions (J) shares for taxes.
- Summary: Employee William B. Allen Jr. had 81 J shares vested and tendered for tax withholding.
- Date: 2026-11-19 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPWEZEVXlJemRvUnBVeDVwVjlsTXRHMlhTSVNvLTdORTN6ZGkyY2pJUUpxQnJRNENzTExpc0gzb0NhU3FpWjdlYzlMbGFqbVlnY3pZRGRxeFBSd3VGNUFaS282YlVWSUFzTkNpUl9kTzRENGNLejRsOS11cnc3d0tMSTBmb01WMEU4YmxnV2Z2RUE5WV9fTDhfUmxqdHNEVTZkR3dkbE5RUGllOV9ldjl1VA?oc=5>

### When her stock grant vested, Joanne Caruso Zaccaro of Jacobs Solutions (J) had 692 shares withheld for taxes.
- Summary: Employee Joanne Caruso Zaccaro had 692 J shares vested and withheld for taxes.
- Date: 2026-11-19 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNSE1hUWlpOGxiMWltQzZiYXFJSXgwVHJqRDdIWmloMVdjRzhNdWVrWGNId0tvOFFFSzlVbHVyaWVoS1lvR1hINFh0M0dUWkQyZnU4b2NYWmxrZElUMU1WeVJiWXNualNHeW1SOHY5cjU1Y2FSOC1hNEthcVFkWnRTWWJKN3EtU1pRY254YnI1LV9OOVhpQVRzNWo0NjdpTG16ZU9aeHU5NTFKaWlaM0Q2NA?oc=5>

### When a stock grant vested, the Jacobs Solutions (J) CFO tendered 741 shares for tax withholding.
- Summary: CFO of J had 741 shares vested and tendered for tax withholding.
- Date: 2026-11-19 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNQ29TZ1NEN09GR0NiOTNGWXJoUXAyVXJmaEY5ZkZ6eTI4SGVqaVJYTWlneHhBcWZGbEtQbFFjV1VsMy1wLVVOd2hwS3YwZ1pTSlpTaUFvbmlUdjV4aVdGN0k2MWhmU1B4UVF4MjNaak9WcmVkNkVPd2Rod0RPTk9rY1czWmZESGVqYU40OF9zSUg2WFN1ay01M1ZnVjhGQzU5VGRXZzhOYm5kd3QyRmdvbQ?oc=5>

### When his stock grant vested, Jacobs Solutions (J) CEO Robert V. Pragada had 2,706 shares withheld for taxes.
- Summary: CEO Robert V. Pragada had 2,706 J shares vested and withheld for taxes.
- Date: 2026-11-19 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNaHdMRUhkc0xiUFY4NUkwRmFSZFJPLVJnZ3ZKTEhLRmtoTklLVFhoRmIxZlJldzU2Wnh5cHJWMlJZYlNLN0pndTNiVGN1VDRmUTl1dHBTWTdITXR4N3k3OWdlQmZTY2REU0xyczdGbE1vN3hVTzFsYjB1dkFWWFJwQWJyTTZXRHNKSjk1RkFtSFhnVG1LOEJCTmMtMHBJNVk5OC1KaTZRNjVXdFdYZ2xBYw?oc=5>

### Jacobs to Report Q4 Earnings: What to Expect From the Stock?
- Summary: Jacobs will release Q4 earnings, providing insight into financial performance and guidance.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOR0hmTWdYV1lWM3FWSDN5enJ0XzFfMUZuWUs3eFpVdXNtQ0RFOC0zZkRIYVY4Q2llVTdtQVZhbFE1akxtV1FoU2VQRnBzREtmbnpxc2g3U0U0Q3ViREdvcmwtVTVqU2FpMmRMMmk4QW5uNTVrVTlCbUViRk9vN0E4UThMMnhYb1B1YkVHQUtmQ082RTBfMjZOSUJpT1NZY2JqUUNrWTRTeGVFcnhoZVVXTG9kQ3Y?oc=5>

### In the final quarter of FY2026 alone, Jacobs Solutions (J) bought back 758,609 shares.
- Summary: Jacobs executed a share buyback of 758,609 shares in FY2026 Q4.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQa3dJR2J2aWlDdFBTR0RfWUlZQktfbWR1N3VnNTVxMHpqd2ZDN0ZGVzlxVDRfcVR2R0ZMVW1xZnFWUi0tUGw0QzNLVlpDMW83dnBkOHJ0VGpUSG9oNXJKdEZKRXNHT2JIVTNMWFVIV2NIczQ3cHluM2JHODhybEJKRm1EeWl3MVRKZThsc0Q0SVM5SmdOX0haSjExeHdQR2NLVGE0ZlIxVQ?oc=5>

## RISKS

### Jacobs Solutions’s Q3 CY2026: Beats on revenue but full-year sales guidance misses expectations significantly
- Summary: Q3 revenue beat, but full-year sales guidance below expectations.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi_gFBVV95cUxQbXZWR1I4TnJYZEFfTGRERkFxcUd3eFJQN3BRalo1Um41WUNfaWphQmQwczM2XzNBWWZtXzB1anVGazJ6Z1lHQ0dURUxYeEUtMEtvZ2dQTzY1bXY2YXF4U2hwMTJSU0JuczRBTk1mVTZUT1Y0eF8yQ0xKVDcxanhmNGxzV0s2N0dlU2ZYc3FXUHNjWVdEMEhwbl9lNEphRml4Z1UwLXVZZndFVmNBQ1dNVUtTZnBJRGc0X0NETWtHVExLM2tkR1pocEZfakdFcUxzVGV1ZDBCVDNHa3N5VkV6Ry0wWXVwS2dXV0RrWW9FNFJuR25XQkZrTkN5bkt5dw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **J** | **52.34** | **5.65** | **20.16** | **34.50** | **18,437,091,328.00 USD** | **23.64** |
| ACM | 27.65 | 4.74 | 13.49 | -7.10 | 10,401,412,096.00 USD | -20.70 |
| FLR | N/A | 2.36 | 10.37 | 10.50 | 6,011,842,048.00 USD | 17.10 |
| KBR | 9.49 | 2.33 | 9.29 | 5.00 | 4,114,936,320.00 USD | -17.65 |

Peers fetched as_of: 2026-11-23; J reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-23
- Next expected earnings: N/A (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-23
- Revenue (latest available single quarter): 4,142,644,000.00 USD; period 2018-06-30/2018-09-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 136,553,000.00 USD; period 2026-03-28/2026-06-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/52988/000162828026075495/jec-20261002.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilgFBVV95cUxNTllTWXF0RXl5VHozUHJ4TlZBbkFkZFdZZFRsRHI0NU02M201ZTNvdHBZdFhWd1R0WVhTS2t4eDBmUk9GX2FPY0lkdzg2TDRKWU1WVjlmTmFHelYzUk1yREp5VUxsRm5MLURLWE4wWkcwRnZzOVlPUm1ZX19RbnZucXhlUFJCcVlCQzRVeWo0NzByTlhnY3c?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOUHV4ZkJsWTZBYnd0RzZHM1k4VGp4alVQeHJySzN1TzJGWVFQVVhuaTdqb1JFRXNwMjZGNFl1TC1BNXpnUW1PZlVBbk1nVlFYdVZtZnhjQzNHTHBLQ29QRUF2Zno4VkhOTS1ZR1ZqS3g0dW1UUDEyY3NiVGZsWDBiM0FRUEpvOXJhZk9zUTFjTTdFTE52YkEzSllDVGpnUmxBTVl6QURzRFNPd0xUaWJUQ00weXU?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQOWkzQUktajZ3M0h0YWxkQ1o4cjQ5RDIwc1J3SEJGc081b0c4b3Jhbl9LUjBCRzVjS1pZQWtLSHZvbFJRRUNwUjFfNzY5SjhrWTM5Y21VZERveDZEa3YtWU9IR0g0V2dxZFM2R2FLV3VIOUJRUklMek5oSU1JM2pLOEJnbTk1dEpQV1lQSWhtVDBzLVVsbjVFN2lhaWNCZ3NtMGNDZUFjcFo?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQdzIzTGlKLTN0UXBlZzRZaVI1LWtNOERTdjdqZ1RmRTR1Y192TFdyWDRYUWJTeF9vYW5Zb1hJX3JPUzlxR3VyTE02bHJQY3ZhVTZldUt3eGpkRUx6ZTM2YjZRM0daMF9TRmJuWDhfU3FlMXotODV1S1p5X3Vid3J4QWhwNDQ2ay0yLVVyVHVVNVBDbXZmdEFLRVhlTWQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPQWl6TDViZDNYVHIyeVVLOEVQX2Z4MTlFQi1sUmVUdEVfWTdBMzh1blFvOEZ3X3lGZTVISkJWSGxlTzRMQzJpYmEzbUo5M05wcHhfYTU1RHE5am5tcFpjbUFublBwYW5USnBlVGh6RWI1cmJaMW4tcW1hOGpIMUJ4T0Jlek5Wc2NoSGNfWTB0WUFOM2dkeUtxUzJpU1R4dDU2R0ZkeGJ3?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOZThXbGV2ZXFDajJKdWgxSm95UVIySXFWQlY0TnVwTDdRMkVIYU5qZGVLcWZTc2k0WU9welVEOU00b1FGYUZELWpocGd0VXhVbWtKT0ZvMFlwcHJFUW1uNVpLZm9ZZmJRZGtfLWw5OWRrSFdHMS1vVkdSN0tueUFqeWxHTDdqbk5jWWxUSlVBbjVwNlhl?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxNWUhmZ0k3ZnR1N3FRUk1GXzV6ejd4d3dlMVlqSWd3T3JTR2hhSWlUOVVkSzlJSDdGd2p3Y2NDSWZncTdiRWpmZ1d4QUN2MUliaXNlX0lVT3BsbVBKMm1NTWlWUnNSbGY4ODRCd2NzNzQzc0dXSW1yUnNjYzZpTEFCLXBDazBIS1VUX2dWb1lSSkZfQUc1NFUxVGtkMy1aNGhNeExmb2xfWHN4NncySDlKbWllSXRIelFXU1pRYnFNRlozeWF5aDZLRDVXNmZybTdLLVBJcEVVMA?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPZ3Vlay1FSHB2aVZSN3dOMVRzel9xVWJfV1hvZmwtMmhCQ0FaSkVRS1FydUNqeE83MzduLXgxMDg0QU9KQy16TDhabHpDNUdBc0EyTFR5TmdGS2hjSkNHVy1NbW9iR09OOW5ZMVNZMm5POVFnUjN2Ui12SzlVa3FpX3FjMUhiZTdvUS11WFFjNUhwNFhVcUE?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPdjZtQ0FobDlTTlVvNGhETXdsanctVVROd29QZ09vM3F0dmJWd2x2a1lsWmVfeDVnTldqT3dmTGpyaXZTNzZvLWdEaDRBN1ZhUnpISF9mOGRscGtyczR0RFpoYkZlSEdIa0JCQzVSaGtGMHBaLWFtNThKclVUSmlMcFlLN05aLXgtZHpfT2wwQm5HSUJJMWhwdW9wN2t2SUdUQlN1UWlHeExBOXM?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxOUzdmMi1QdW00dDZ0bFlYNnY3cU5SMHR2RHRXdFRsWEg4TGNrRDg2WTU2MjhKTXdxd2FqUmVTcHdCSEc0LU5xTXJKWlREeGhKb0xBRkowZW5jcWpzRDcyc3g0Rnd3dXoyWlJCcTZzalJya2FPaUoybTNLZ1pIR0JFbVpZenVmMHJaT1U5S3RtYWRGa1hfQ0lmOXpuQXptSXhsWER1S3BzWE1xNUVUZHdtVEpGUXJfSFpTT3dQNzkxMFNFN1FDWlY4UzJjTVBHdWZkNVRVUm90UnlvVlE?oc=5
- https://news.google.com/rss/articles/CBMimwJBVV95cUxObVE3bElrOFgtZ3YxM3lHcGNyQ21nbkFMWlg0WGZiMXpvOEdxSkJiWGZSQWtWVkZsV2JlbHU3ZlBjcWl2WDI4S252QkJhQ3ZONEFyMXBWTHZ2QXg4cmZsbEo1Q2JBMDhWR04tZ2NmWWwySlFFb1RVMUw5dDVZbm5sOEg4aHJidVlBdWZYQ3VXbWUxWW85X25wZlBPTGRGOEpxdVcyS1ZhRzZoRFA5UGJMbVVXU2RuN2V1STRiUkk5RXNkWEtyYmt3QVlOUGtwOE9nQnJYcXcwNmd0NXlFY19wTFhzX1pqa0xvZ3JLbF90c0lJZGxOalRFSVNrWnNpYlNUVjNHYzd3cERUb1cxX1JkZnNhLWtoc3lQeUI4?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQbXhQNWRrZEdHdlhZRWlVZlhQLWFyRE5WNlRHcVBMVWZtVmpyY0RBaVlETFVoX3ctakJwRGRYa0RvZnZKNkdIUzdVRGVXMFlhVi1ZTXViek5LRmhtbEhOSEpVeTFjcDZEZkRJV1BCYUl5LUIxRWJZN0tKS1ZvVDhpZHZ3QTE2WXhMNmFNWUQ2UGt1VGVNdjNCaHo1eGhOR1p3bjh3?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxNWFk0aXFCTEwxSDhXcUdKcnljZ3JIWV80MVQ2RHpVeXZ4bzJ4UkNsRDJaSk9UT3Z5eWtmZFpXcXpQRG1Jb1hoZVZoTWVydTBzNk45YXlMalc3aFgwR3RhYy10LTlRQl9MS2VLbTRYWVctQm5fcVctbENZVG9aRm9Xd1FOdHk2RlFTa2NtcFo4LVNXdzNKQWtDNUpONE5hVkVpMWh1WmhLaTdCMVN5cUoweVZwX2ZDNHlzdWYwd09KMG9zVC0yb1ZpR1RSa2VfZnp6aFhPN3NIcUpaUnY3THhB?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPWEZEVXlJemRvUnBVeDVwVjlsTXRHMlhTSVNvLTdORTN6ZGkyY2pJUUpxQnJRNENzTExpc0gzb0NhU3FpWjdlYzlMbGFqbVlnY3pZRGRxeFBSd3VGNUFaS282YlVWSUFzTkNpUl9kTzRENGNLejRsOS11cnc3d0tMSTBmb01WMEU4YmxnV2Z2RUE5WV9fTDhfUmxqdHNEVTZkR3dkbE5RUGllOV9ldjl1VA?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNSE1hUWlpOGxiMWltQzZiYXFJSXgwVHJqRDdIWmloMVdjRzhNdWVrWGNId0tvOFFFSzlVbHVyaWVoS1lvR1hINFh0M0dUWkQyZnU4b2NYWmxrZElUMU1WeVJiWXNualNHeW1SOHY5cjU1Y2FSOC1hNEthcVFkWnRTWWJKN3EtU1pRY254YnI1LV9OOVhpQVRzNWo0NjdpTG16ZU9aeHU5NTFKaWlaM0Q2NA?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNQ29TZ1NEN09GR0NiOTNGWXJoUXAyVXJmaEY5ZkZ6eTI4SGVqaVJYTWlneHhBcWZGbEtQbFFjV1VsMy1wLVVOd2hwS3YwZ1pTSlpTaUFvbmlUdjV4aVdGN0k2MWhmU1B4UVF4MjNaak9WcmVkNkVPd2Rod0RPTk9rY1czWmZESGVqYU40OF9zSUg2WFN1ay01M1ZnVjhGQzU5VGRXZzhOYm5kd3QyRmdvbQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNaHdMRUhkc0xiUFY4NUkwRmFSZFJPLVJnZ3ZKTEhLRmtoTklLVFhoRmIxZlJldzU2Wnh5cHJWMlJZYlNLN0pndTNiVGN1VDRmUTl1dHBTWTdITXR4N3k3OWdlQmZTY2REU0xyczdGbE1vN3hVTzFsYjB1dkFWWFJwQWJyTTZXRHNKSjk1RkFtSFhnVG1LOEJCTmMtMHBJNVk5OC1KaTZRNjVXdFdYZ2xBYw?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOR0hmTWdYV1lWM3FWSDN5enJ0XzFfMUZuWUs3eFpVdXNtQ0RFOC0zZkRIYVY4Q2llVTdtQVZhbFE1akxtV1FoU2VQRnBzREtmbnpxc2g3U0U0Q3ViREdvcmwtVTVqU2FpMmRMMmk4QW5uNTVrVTlCbUViRk9vN0E4UThMMnhYb1B1YkVHQUtmQ082RTBfMjZOSUJpT1NZY2JqUUNrWTRTeGVFcnhoZVVXTG9kQ3Y?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQa3dJR2J2aWlDdFBTR0RfWUlZQktfbWR1N3VnNTVxMHpqd2ZDN0ZGVzlxVDRfcVR2R0ZMVW1xZnFWUi0tUGw0QzNLVlpDMW83dnBkOHJ0VGpUSG9oNXJKdEZKRXNHT2JIVTNMWFVIV2NIczQ3cHluM2JHODhybEJKRm1EeWl3MVRKZThsc0Q0SVM5SmdOX0haSjExeHdQR2NLVGE0ZlIxVQ?oc=5
- https://news.google.com/rss/articles/CBMi_gFBVV95cUxQbXZWR1I4TnJYZEFfTGRERkFxcUd3eFJQN3BRalo1Um41WUNfaWphQmQwczM2XzNBWWZtXzB1anVGazJ6Z1lHQ0dURUxYeEUtMEtvZ2dQTzY1bXY2YXF4U2hwMTJSU0JuczRBTk1mVTZUT1Y0eF8yQ0xKVDcxanhmNGxzV0s2N0dlU2ZYc3FXUHNjWVdEMEhwbl9lNEphRml4Z1UwLXVZZndFVmNBQ1dNVUtTZnBJRGc0X0NETWtHVExLM2tkR1pocEZfakdFcUxzVGV1ZDBCVDNHa3N5VkV6Ry0wWXVwS2dXV0RrWW9FNFJuR25XQkZrTkN5bkt5dw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
