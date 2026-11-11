# EW Intelligence Report

- ticker: **EW**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/EW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/EW/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:38:49.782160+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 10, 'ai': 8, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261110T055129Z-abd33250/EW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 44.0%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 104.0100 |
| Return 1D (%) | -0.6685 |
| Return 1W (%) | 9.2657 |
| Return 1M (%) | 22.0631 |
| Return YTD (%) | 22.0059 |
| Return 1Y (%) | 23.7036 |
| Annualized volatility (%) | 25.5717 |
| Beta vs SPY | 0.5359 |
| Max drawdown (%) | -13.1855 |
| Sharpe (rf=0) | 0.9626 |
| Downside deviation (rf=0, %) | 16.8821 |
| Sortino (rf=0) | 1.4581 |
| Historical VaR 95% (1D, %) | 2.5317 |
| Historical ES 95% (1D, %) | 3.1155 |
| Correlation vs SPY | 0.2865 |
| Tracking error vs SPY (%) | 25.3081 |
| P/E (trailing) | 60.47 |
| P/B | 5.51 |
| EV/EBITDA | 26.72 |
| Revenue growth (%) | 10.50 |
| Forward P/E (estimate) | 30.73 |
| Gross margin (%) | 78.02 |
| Operating margin (%) | 30.15 |
| Return on equity (%) | 9.33 |
| Free cash flow yield (%) | 1.92 |
| MA50 | 89.4758 |
| Close vs MA50 (%) | 16.2437 |
| MA200 | 85.9759 |
| Close vs MA200 (%) | 20.9758 |
| RSI (14, Wilder) | 76.9040 |
| MACD (12,26) | 4.0300 |
| MACD signal (9) | 2.6024 |
| MACD histogram | 1.4276 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'EW': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 104.0100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.6685 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 9.2657 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 22.0631 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 22.0059 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 23.7036 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.5717 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.8821 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4581 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5317 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.1155 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2865 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 25.3081 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5359 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.1855 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9626 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 30.7327 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 78.0180 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 30.1540 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.3330 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.9151 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 60.4709 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 76.9040 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.4276 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 16.2437 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 20.9758 -> Clearly above the moving-average trend level.

## TAILWINDS

### EDWARDS LIFESCIENCES ($EW) Releases Q3 2026 Earnings, Stock Rises
- Summary: EDWARDS LIFESCIENCES ($EW) Releases Q3 2026 Earnings, Stock Rises
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOVXI5ODZCMTdadEFoVEVINmlYZlVQSENUUUlXY2tDTWp3UzVGTHZ3bGZYS2pUaE5ZS3djR21laXBIUmQzaV9qQXRwcnBSSVFxVzNUR08zZDJTdzA4MjJYZm9Ga3B5c0J0Q2pFMWNIWmlXZTdmejNIMTRRZE92WGNSaHlLSktFSkRzYm5sdTdLb2taclFFVk1Wako4T1YtT2RvaHlITHBCOWNoZw?oc=5>

### Edwards Lifesciences Corp (EW) Stock Up 4.4% but GF Value Says O
- Summary: Edwards Lifesciences Corp (EW) Stock Up 4.4% but GF Value Says O
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPSnJGeGFHdFM5TEZHNGl0NUEwWGxSaDFnX0NpeUNsMm5Eem1RZDJPTjN3a3FfZEdpbFgybWtvakc1MUJSR3Z0RURVaTRzNzhreEE2OE1tZ3hUbkpEWGZqMlpodHEwQXJSTGFUY2ExR1M5aVhxaWVSVTVmeXJwOEpSbHU0cGFURUlCWVJxNlp6ZDQ0aHEyRV9QcjlmQTFybkh6aktVRWZxbDVyc0xqSnFMNktHTDVLUEdvNUhqaFVwTFg?oc=5>

### Edwards Lifesciences (EW) Q3 Earnings Beat Expectations, Raises Guidance
- Summary: Edwards Lifesciences (EW) Q3 Earnings Beat Expectations, Raises Guidance
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxORDBnalp4NXdSVVd4TGtKdkN4b0Rwb1RjUmlQUEQ4dGRmWkFaM0gzV2lhZTg0bXlfUUsyVndiX1IxcF94UzdCNXF0TUZDV1oxU0ZteUNtdzBHb2Uwd3R4T2ZpNWFOaU5yOGRkS044YkEzUm1hUThNMkM1Q3JIQThPbVA4eEZNS2g5VzlxVG5Rb2ltdE9qZEhVdU5YRGhaYVRKWDBFU00zRk95UERG?oc=5>

### Edwards Lifesciences (NYSE:EW) Upgraded at Robert W. Baird
- Summary: Edwards Lifesciences (NYSE:EW) Upgraded at Robert W. Baird
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxOanVFVDc2VVpmdHVyX1QtbVlYcFA1ZGpleHZ6X0RFYWtQZmZObVloTG1ZQWdIaTRBbVZmSG1DSDVuZTJMVnpaN2ZITmtQT3dER0xvV3JRZzVLNldfMHhyNFo5YzI1b0I3S2lQdE5XaTZfbVBxb1BQcURpLTJaQTRvN0FxU05LamhMNkMtMmJkbGo4TXhxYVFsdjE5ZXJYTmJvN2ViTTNPbW91LWdYS2pIcUZiWXpxN1gx?oc=5>

### Key facts: EW beats, lifts view; TAVR meets goals; stock hits 2022 high
- Summary: EW beat expectations, TAVR met goals, and stock reached 2022 high.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxOTmtpTGtIenh0em82Ym0yRlpjSG5JSmthcmo4WFFTYUxLSmhhRDdjUC1BdXJoWXUwZThzNzJXYXI5OGdZb3otVkJucGFKN3U3MXpmRDJYRGstTVdzODZMRGRHdzd3V09wa2s3ZFlnUHMtbVczQmo1eXBnR0NXN0NyMlkzTnZTM0lMTDlUY1Y5dmtETzBId3Y3d2k5aUhiMk9nQTZRdlNyUUloRkZqVGpnTHN3bWlaV1F0ZXFZWHIxUE1ocWlfaWtQQw?oc=5>

### Edwards Lifesciences stock hits 52-week high at 98.7 USD By Investing.com
- Summary: Stock reached 52‑week high, indicating strong market performance.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQWFhYaFRLaUlMQUU3Tm1icWJoU1RCZjNyTTZTcGxPOEQ2RHZIdkZySFpGMEZJQU5xak5Ca3FvRkdlLXdIemExemlhSVZkZDlZX0FIc0lzTE8tRmF1aXAxRUNmZDBJV09lZ2tWUFF2TkF0NVZRREMxUkxCbEFtNWlLU0RjVXJreFRvQ092TlRzVGtmYjhFODFBaGhGUzhBRGZIZnJXWGc4WnoxZ1NocjdhVkVBV05Cdw?oc=5>

### Edwards Lifesciences (EW) Trial Data Points To Earlier TAVR Use In Moderate Aortic Stenosis
- Summary: New trial data suggests earlier use of TAVR in moderate aortic stenosis, potentially expanding treatment indications.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPcW15Slp4eGM4UnFieGQwQlhVUzBuSDBiUFFsRzNxN1g5Z2hJRXVLTVQ2LUJyQnFVeDFFUGQ0YzB5LXA0c1hmUVhGM2lXSkRUUDNtTkg5Y2ItUEphS2hVRWhxcWFYa2wzN2tiWDM3cVlOb2xnZlMtZHlaQnA2clF0TUROUXhDMllSYzFlck1Mc2VmRjBWQ2Jma016Zw?oc=5>

## HEADWINDS

### Edwards Lifesciences (NYSE:EW) VP Donald Bobo Jr Sells 48,900 Shares of Stock
- Summary: Insider sale of 48,900 shares may signal negative sentiment.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxOX2pVMXZaVzZ0OUlKN1FEN1BORTkxUks2c2lBS2hmbkh3NmdYYUxNb0U5T1JsQ1dWanFqWGVBVldMV3lkQmFjWmhwMnNrVkFvZ2J5RHlJcnEzV0Q5N2xTTDJvb2d4OWdqNi1EdkM5RTNtMGtfb3R4MnYxTHB1QTh6bTgtSGgySHZqSHQyckxVbmZwTlBaWnpGZ3hFblpzb0swQUtqYVRTMTNlc0RKMjhhU1NIa0VaekM5UHktLVFOcEpnQkFJSk96eGo5YVVjMFVhRUE?oc=5>

### Edwards Lifesciences (NYSE:EW) VP Daniel Lippis Sells 619 Shares of Stock
- Summary: VP Daniel Lippis sold 619 shares, possibly indicating insider concerns.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxQeVRxVFNUWF9zNldhNmFwRUUwQ3hLNk0zd0hfRlFEY3dHb2oxcXNpSWE4MS1IcjROZkpicm4tNnBsTzU4cnJmVVRZa2R4MW9VekNRMWt6UmphdGE2eEtvRWttZ2VGMEVwekRjeU5jOE5DZm9NSnpCanNhTkxMaGlrNlJVY1pKQ2lKYnJnWkREMFpDREJUNHNOMmlIS0NpUEtkeXhQdkhJSUo3aUJCYTdiN21QRnprX0dhZzhMd1RBbFRENDVPU0l2aGNsZlFFdw?oc=5>

## CATALYSTS

### Edwards Lifesciences Corporation $EW Stock Sold by Lockheed Martin Investment Management Co.
- Summary: Edwards Lifesciences Corporation $EW Stock Sold by Lockheed Martin Investment Management Co.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxPODJwRzl1eERGT1daZzJlS0I5WmJ4bHl1NllYNXBRYkd4Z3prNnV3Q1hDWXBlMkltWVlsY19tVFZ1ZmQzT3czWW14TENyWkhJbEFZTWtobTY5eUs5RFNCMk85T0VrSlJlTlRITnhvV0FNZUQ5aW5GZ1JCdG1mbXI3cUphNGNKamNIUmNuV0dKYk5QbWE4ZDl2bmItbjJacGQ1ZnhLQlR0WHp3cWQ0d2ZoM1FHM1Y5WllEWk1MenF4T0tOdFNWUVJJUmpvZkx1NzQydVNWcXU1ZTBWSS1pVkhXN09zUVVjZw?oc=5>

### Edwards Lifesciences (NYSE:EW) Stock Gets Price Target Increase from Citigroup
- Summary: Edwards Lifesciences (NYSE:EW) Stock Gets Price Target Increase from Citigroup
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxQYTBJZzhrQlZ5RkF6UnV0ekVvTjVKMkdBRS1OdmoteU8zc1QwQjVXU1ZFTEZfQ2FkS0JUdjF3em9Qd2NPRzRwYTc1bUhLNzVkcUFDNGxoNl9XYmxjOVh0MXJyRndxYVZkTV9LbDdTRS1EdDkzRnRvNHVBOEw5SlFXbTlGbmNJMUtYZHNXTXJlZUhqejltMFgydEZlUkVNdDMxTE00bktVdS00bjY1eFRINHE5cGQ5RDdMTmRhZU82UXdhWXpfVDNOalJScWljWFpDUlNidg?oc=5>

### Edwards Lifesciences Corporation $EW Stock Sold by Boston Trust Walden Corp
- Summary: Edwards Lifesciences Corporation $EW Stock Sold by Boston Trust Walden Corp
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxPMElrSERNVnNHejFNS3o5bjhOSWJnc1lHME15LWZZQXpXTVd1bDJadHhLaTlQTHdldEhxQmV6TW04QUlNY1duQUNackdvejBRRXBlVEI2QXUzMUR4N0txZG04UUpTeXY1U182S2w2NDZXVzJMMnRzUVBIcXA5bEtGcHdpZjdoMzFGOVJWMS13X1p3MjZHNkIxSkFGWTJ3ckh6MVIwU081YjJmaFdQVlVjSHNqUVdfMVZEaDc4YmI4eVU2YWcybGJuYkFTei1UUVQ4?oc=5>

### Edwards Lifesciences Corporation $EW Shares Sold by Allspring Global Investments Holdings LLC
- Summary: Edwards Lifesciences Corporation $EW Shares Sold by Allspring Global Investments Holdings LLC
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxQeWVVX1NsbGswSlFhcFRidl9ZYTVMNkRNZTN0SWlkM1k4Ml80MUJzdVVHcUpBMzh1Tkg1c1BnSXhJUlJuU1FNeHc0SGlybjIwWmpCQmlvc0RmeWlGU0hvazc5RmwzaGl0TTVWLTlQZ1ZadUNUcFJ1V3Zud2l4Rkh0Wk94dGdfTVl4Q3pVQ0o0RW44d3ZncmpMbTVjS0JfZHZmaHJ0QkctbXp6R0s1X3pRSEUyRnB0cG5QOXF0QjZnY2tmX25ZTkd3ZmdZYWYzU193dXhOZUNzUlRFOUEyQk9fSGg5Nlg4OVVk?oc=5>

### Edwards Lifesciences Q3 2026 Earnings Call Transcript
- Summary: Edwards Lifesciences Q3 2026 Earnings Call Transcript
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPX1F6OFo3WGZ5T2ZXdVVabEsyTmZHMGRudkdGZk84V1lxdVNvYl9LM2tzNHpleXc5REptVVB2MWczb19ua0xLejctT3RGUXBNLWJ4eE9ZOUVtMlU0VFZqQWk2MFVOREd4UDdWekF5YjF3OTRWQVdOc2pzNldHUl9nRlM2RzBTWEw4UWRZWHBkZkNuTTcwVEw0ZTM4WGJYLXc?oc=5>

### Edwards Lifesciences Corporation $EW Shares Sold by Factory Mutual Insurance Co.
- Summary: Edwards Lifesciences Corporation $EW Shares Sold by Factory Mutual Insurance Co.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNbXBxazF4UU53ZmtWT1hiX1Z2RUlWR0lUMnNqdG1jWE0ySURJRmkzMjUyM3hPNTNKcGQyQlc4TnVRak1DRDRDazF6ckdJdFBzZXdsYVhwMGFNSUdWQV96T2RGM0dLVG43ZWx3UGJtZ0NibXk2Qnd1QmdZZGc1Q0RYVEdRT19hVlZZWS1laDIzaEJSbEJobThrd1FGNG9FUUd0N2M3bHFmOHozbjEyQWlfa1B1ZGhWYlN1MXdTVi1OcVVLMWdrSWZCRlZtdklteF8tSXZ2SWhR?oc=5>

### What Edwards Lifesciences Stock Beat And Raised Outlook Means For Shareholders
- Summary: Earnings beat and new guidance boost investor confidence.
- Date: 2026-11-08 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxOTjVBZzdtOFJCSFFmdHAyWjFZSWFJcWlFQzI0X0d5QjZLb0w2Vzk3aWdnWkdabXJuUF9YSDYxcDg2cUJpZFV0Q25JTkZtMUlpRjJCWEtZcmdCM2VrUXBJalp5aFhCSW5wSHVPaTM2U2pJd3VSa1N3TTRYX3RVLTE2YUw0TUdkU09fSUd3MmVjR0IwZ0ZmUjh6bmhFMUNrSXN3OFNrN0FrUU5yWnV3R1NEblc2N0pDd0xnb3JNSGh0TElweHowU3ZzYlRWWEFiM0N4Wnhv0gHYAUFVX3lxTE03ODlmY25icldSdlMzbHNpWF90M0xvdW9DOV96RGtDV1RwZVpYV3h2U2lNb0lsNEY1Y2ZCbC01eG5MT2dZQm1VeVBOTVRDYnZtNjdCeld2QXVLMHM1WVctaTJTejA5dGlLdUFfcVdoY1ptbDRoTTF2TmMxQjl0TTB0WHFaTURVUDE3bU15dnV6UnNvQ1pyRVBiQ2s2TnJnYzJZOEM1N241UF9lUGxmQmZ3X0dpcXhnOHRFNGRlTGpWSkhveUNrMlJCQkJBNG9IdU5HY1NvRlBVTw?oc=5>

### Edwards Lifesciences (EW) Stock Looks Fully Priced On Cash Flow
- Summary: Analyst view that EW stock is fully priced based on cash flow projections.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxNNFE1LVpjaWwxdFc5RU9vY1VpRG1rcW5BbnktTktEZ2hnUC1RZ2xzbV9hSUdoTzJHUlNCcnFKbHZKRDNfYVZGRm5hS09wdHkxM2R6NUlja1JOTkxHMlJNOVQ2UkZaOXVubHBlelhWVXN4RWwxV20xZkV0WFZ3SXF2WmNEMUtZc0x1NW5QRUZwd1JXa1VRSFZuXzlmT0dxY0dHTzc2dXM1SWIwRlgyZEY1V3JmbmdnOTg3eUdhWUZVeTNWeUdmNFQ0ZXFjWWdpeGFYVkFF0gHYAUFVX3lxTE9TaXRUTzYwLUU3ZGlqck00NXFCMk5oU3llaWFiNE1oRVJlNGJEeDFDY0hqclNVa1hpMDN0N1pxMzktODNsbFhGQlQ5YnJnSEtfYjRUZVQzTnR3bnk3Yk5XUmI0VWZkS0ttYzBHVmhPeWl1dmI0RUE0U2ZqMzNQZVhBTWxlRllKSjhDYkJDVTk0MGRiSHgtWTZldWt2emk3bWdHcFpuRTNDOE80bUY1TnBrS2VoOVJPd196a2tPR2hpR0FHVG85N3gzd0ZjZ29Bd0J2WXdNS0haYw?oc=5>

### Edwards Lifesciences (EW) Could Be 21% Undervalued After Earnings Guidance And Trial Data
- Summary: Guidance and trial data suggest undervaluation.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxPNnZOMFFuSHlpbkRqa3BBejUtcHBjcUhFdTJ3XzY1Mm54WUNNWmNWUnRkMGlnbVJFRXAxdEFxemN2QS1qcTYwNDBISzFuRms0RWs3ZXI5MkRZZzc4dXN2eGtaWVVxMHRlaUswUFpncXQ3eE4zZWtHOURxcVhJR0ZkS2hZMmdLYmZNYmJBUDFUUDc0R2hmajBWZjhPWjBkMGY5VTNtZTkwUnN0ZmtYbWZNY0h2ell1YTFVMmJENy1xOEpSMXZ2d2s3V2ZCbWxXRWczZ2FN0gHYAUFVX3lxTE5XYzVjQkZlLUJ1MDRiZFBCUVlWREY3Ny0zalQ2TU91Z0xicHJPb2F3cW0xdWpiNkdmS1Q2LVZvRlpnWXdMR0JTQUlvSk5YVjBrUHNYakhCUV92WGdRaTBDWkRqUDRoTTVNWHlpWFJ3eF9LMkNlWkEwUkR0aXRGS2dpMXpJYklVTWxmWHYzbVlWVXExd3g0NUo5Nk5HYWZjYldMcWVfLTg1blZqUDlYX054OEJBdW90bHdDZ1ZhVE9vaDJtNlRoMXNEblQ0Q1ZZRzc5bGo1dWl5RA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **EW** | **60.47** | **5.51** | **26.72** | **10.50** | **59,805,749,248.00 USD** | **23.70** |
| MDT | 24.96 | 2.59 | 14.40 | 13.70 | 129,947,615,232.00 USD | 13.27 |
| BSX | 18.86 | 2.53 | 13.71 | 1.40 | 64,791,457,792.00 USD | -55.70 |
| ABT | 41.22 | 3.75 | 19.12 | 14.50 | 191,310,266,368.00 USD | -10.08 |

Peers fetched as_of: 2026-11-10; EW reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-10

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,715,500,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 307,500,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1099800/000109980026000054/ew-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOVXI5ODZCMTdadEFoVEVINmlYZlVQSENUUUlXY2tDTWp3UzVGTHZ3bGZYS2pUaE5ZS3djR21laXBIUmQzaV9qQXRwcnBSSVFxVzNUR08zZDJTdzA4MjJYZm9Ga3B5c0J0Q2pFMWNIWmlXZTdmejNIMTRRZE92WGNSaHlLSktFSkRzYm5sdTdLb2taclFFVk1Wako4T1YtT2RvaHlITHBCOWNoZw?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPSnJGeGFHdFM5TEZHNGl0NUEwWGxSaDFnX0NpeUNsMm5Eem1RZDJPTjN3a3FfZEdpbFgybWtvakc1MUJSR3Z0RURVaTRzNzhreEE2OE1tZ3hUbkpEWGZqMlpodHEwQXJSTGFUY2ExR1M5aVhxaWVSVTVmeXJwOEpSbHU0cGFURUlCWVJxNlp6ZDQ0aHEyRV9QcjlmQTFybkh6aktVRWZxbDVyc0xqSnFMNktHTDVLUEdvNUhqaFVwTFg?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxORDBnalp4NXdSVVd4TGtKdkN4b0Rwb1RjUmlQUEQ4dGRmWkFaM0gzV2lhZTg0bXlfUUsyVndiX1IxcF94UzdCNXF0TUZDV1oxU0ZteUNtdzBHb2Uwd3R4T2ZpNWFOaU5yOGRkS044YkEzUm1hUThNMkM1Q3JIQThPbVA4eEZNS2g5VzlxVG5Rb2ltdE9qZEhVdU5YRGhaYVRKWDBFU00zRk95UERG?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxOanVFVDc2VVpmdHVyX1QtbVlYcFA1ZGpleHZ6X0RFYWtQZmZObVloTG1ZQWdIaTRBbVZmSG1DSDVuZTJMVnpaN2ZITmtQT3dER0xvV3JRZzVLNldfMHhyNFo5YzI1b0I3S2lQdE5XaTZfbVBxb1BQcURpLTJaQTRvN0FxU05LamhMNkMtMmJkbGo4TXhxYVFsdjE5ZXJYTmJvN2ViTTNPbW91LWdYS2pIcUZiWXpxN1gx?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxOTmtpTGtIenh0em82Ym0yRlpjSG5JSmthcmo4WFFTYUxLSmhhRDdjUC1BdXJoWXUwZThzNzJXYXI5OGdZb3otVkJucGFKN3U3MXpmRDJYRGstTVdzODZMRGRHdzd3V09wa2s3ZFlnUHMtbVczQmo1eXBnR0NXN0NyMlkzTnZTM0lMTDlUY1Y5dmtETzBId3Y3d2k5aUhiMk9nQTZRdlNyUUloRkZqVGpnTHN3bWlaV1F0ZXFZWHIxUE1ocWlfaWtQQw?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQWFhYaFRLaUlMQUU3Tm1icWJoU1RCZjNyTTZTcGxPOEQ2RHZIdkZySFpGMEZJQU5xak5Ca3FvRkdlLXdIemExemlhSVZkZDlZX0FIc0lzTE8tRmF1aXAxRUNmZDBJV09lZ2tWUFF2TkF0NVZRREMxUkxCbEFtNWlLU0RjVXJreFRvQ092TlRzVGtmYjhFODFBaGhGUzhBRGZIZnJXWGc4WnoxZ1NocjdhVkVBV05Cdw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPcW15Slp4eGM4UnFieGQwQlhVUzBuSDBiUFFsRzNxN1g5Z2hJRXVLTVQ2LUJyQnFVeDFFUGQ0YzB5LXA0c1hmUVhGM2lXSkRUUDNtTkg5Y2ItUEphS2hVRWhxcWFYa2wzN2tiWDM3cVlOb2xnZlMtZHlaQnA2clF0TUROUXhDMllSYzFlck1Mc2VmRjBWQ2Jma016Zw?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxOX2pVMXZaVzZ0OUlKN1FEN1BORTkxUks2c2lBS2hmbkh3NmdYYUxNb0U5T1JsQ1dWanFqWGVBVldMV3lkQmFjWmhwMnNrVkFvZ2J5RHlJcnEzV0Q5N2xTTDJvb2d4OWdqNi1EdkM5RTNtMGtfb3R4MnYxTHB1QTh6bTgtSGgySHZqSHQyckxVbmZwTlBaWnpGZ3hFblpzb0swQUtqYVRTMTNlc0RKMjhhU1NIa0VaekM5UHktLVFOcEpnQkFJSk96eGo5YVVjMFVhRUE?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxQeVRxVFNUWF9zNldhNmFwRUUwQ3hLNk0zd0hfRlFEY3dHb2oxcXNpSWE4MS1IcjROZkpicm4tNnBsTzU4cnJmVVRZa2R4MW9VekNRMWt6UmphdGE2eEtvRWttZ2VGMEVwekRjeU5jOE5DZm9NSnpCanNhTkxMaGlrNlJVY1pKQ2lKYnJnWkREMFpDREJUNHNOMmlIS0NpUEtkeXhQdkhJSUo3aUJCYTdiN21QRnprX0dhZzhMd1RBbFRENDVPU0l2aGNsZlFFdw?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxPODJwRzl1eERGT1daZzJlS0I5WmJ4bHl1NllYNXBRYkd4Z3prNnV3Q1hDWXBlMkltWVlsY19tVFZ1ZmQzT3czWW14TENyWkhJbEFZTWtobTY5eUs5RFNCMk85T0VrSlJlTlRITnhvV0FNZUQ5aW5GZ1JCdG1mbXI3cUphNGNKamNIUmNuV0dKYk5QbWE4ZDl2bmItbjJacGQ1ZnhLQlR0WHp3cWQ0d2ZoM1FHM1Y5WllEWk1MenF4T0tOdFNWUVJJUmpvZkx1NzQydVNWcXU1ZTBWSS1pVkhXN09zUVVjZw?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQYTBJZzhrQlZ5RkF6UnV0ekVvTjVKMkdBRS1OdmoteU8zc1QwQjVXU1ZFTEZfQ2FkS0JUdjF3em9Qd2NPRzRwYTc1bUhLNzVkcUFDNGxoNl9XYmxjOVh0MXJyRndxYVZkTV9LbDdTRS1EdDkzRnRvNHVBOEw5SlFXbTlGbmNJMUtYZHNXTXJlZUhqejltMFgydEZlUkVNdDMxTE00bktVdS00bjY1eFRINHE5cGQ5RDdMTmRhZU82UXdhWXpfVDNOalJScWljWFpDUlNidg?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxPMElrSERNVnNHejFNS3o5bjhOSWJnc1lHME15LWZZQXpXTVd1bDJadHhLaTlQTHdldEhxQmV6TW04QUlNY1duQUNackdvejBRRXBlVEI2QXUzMUR4N0txZG04UUpTeXY1U182S2w2NDZXVzJMMnRzUVBIcXA5bEtGcHdpZjdoMzFGOVJWMS13X1p3MjZHNkIxSkFGWTJ3ckh6MVIwU081YjJmaFdQVlVjSHNqUVdfMVZEaDc4YmI4eVU2YWcybGJuYkFTei1UUVQ4?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxQeWVVX1NsbGswSlFhcFRidl9ZYTVMNkRNZTN0SWlkM1k4Ml80MUJzdVVHcUpBMzh1Tkg1c1BnSXhJUlJuU1FNeHc0SGlybjIwWmpCQmlvc0RmeWlGU0hvazc5RmwzaGl0TTVWLTlQZ1ZadUNUcFJ1V3Zud2l4Rkh0Wk94dGdfTVl4Q3pVQ0o0RW44d3ZncmpMbTVjS0JfZHZmaHJ0QkctbXp6R0s1X3pRSEUyRnB0cG5QOXF0QjZnY2tmX25ZTkd3ZmdZYWYzU193dXhOZUNzUlRFOUEyQk9fSGg5Nlg4OVVk?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPX1F6OFo3WGZ5T2ZXdVVabEsyTmZHMGRudkdGZk84V1lxdVNvYl9LM2tzNHpleXc5REptVVB2MWczb19ua0xLejctT3RGUXBNLWJ4eE9ZOUVtMlU0VFZqQWk2MFVOREd4UDdWekF5YjF3OTRWQVdOc2pzNldHUl9nRlM2RzBTWEw4UWRZWHBkZkNuTTcwVEw0ZTM4WGJYLXc?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNbXBxazF4UU53ZmtWT1hiX1Z2RUlWR0lUMnNqdG1jWE0ySURJRmkzMjUyM3hPNTNKcGQyQlc4TnVRak1DRDRDazF6ckdJdFBzZXdsYVhwMGFNSUdWQV96T2RGM0dLVG43ZWx3UGJtZ0NibXk2Qnd1QmdZZGc1Q0RYVEdRT19hVlZZWS1laDIzaEJSbEJobThrd1FGNG9FUUd0N2M3bHFmOHozbjEyQWlfa1B1ZGhWYlN1MXdTVi1OcVVLMWdrSWZCRlZtdklteF8tSXZ2SWhR?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOTjVBZzdtOFJCSFFmdHAyWjFZSWFJcWlFQzI0X0d5QjZLb0w2Vzk3aWdnWkdabXJuUF9YSDYxcDg2cUJpZFV0Q25JTkZtMUlpRjJCWEtZcmdCM2VrUXBJalp5aFhCSW5wSHVPaTM2U2pJd3VSa1N3TTRYX3RVLTE2YUw0TUdkU09fSUd3MmVjR0IwZ0ZmUjh6bmhFMUNrSXN3OFNrN0FrUU5yWnV3R1NEblc2N0pDd0xnb3JNSGh0TElweHowU3ZzYlRWWEFiM0N4Wnhv0gHYAUFVX3lxTE03ODlmY25icldSdlMzbHNpWF90M0xvdW9DOV96RGtDV1RwZVpYV3h2U2lNb0lsNEY1Y2ZCbC01eG5MT2dZQm1VeVBOTVRDYnZtNjdCeld2QXVLMHM1WVctaTJTejA5dGlLdUFfcVdoY1ptbDRoTTF2TmMxQjl0TTB0WHFaTURVUDE3bU15dnV6UnNvQ1pyRVBiQ2s2TnJnYzJZOEM1N241UF9lUGxmQmZ3X0dpcXhnOHRFNGRlTGpWSkhveUNrMlJCQkJBNG9IdU5HY1NvRlBVTw?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxNNFE1LVpjaWwxdFc5RU9vY1VpRG1rcW5BbnktTktEZ2hnUC1RZ2xzbV9hSUdoTzJHUlNCcnFKbHZKRDNfYVZGRm5hS09wdHkxM2R6NUlja1JOTkxHMlJNOVQ2UkZaOXVubHBlelhWVXN4RWwxV20xZkV0WFZ3SXF2WmNEMUtZc0x1NW5QRUZwd1JXa1VRSFZuXzlmT0dxY0dHTzc2dXM1SWIwRlgyZEY1V3JmbmdnOTg3eUdhWUZVeTNWeUdmNFQ0ZXFjWWdpeGFYVkFF0gHYAUFVX3lxTE9TaXRUTzYwLUU3ZGlqck00NXFCMk5oU3llaWFiNE1oRVJlNGJEeDFDY0hqclNVa1hpMDN0N1pxMzktODNsbFhGQlQ5YnJnSEtfYjRUZVQzTnR3bnk3Yk5XUmI0VWZkS0ttYzBHVmhPeWl1dmI0RUE0U2ZqMzNQZVhBTWxlRllKSjhDYkJDVTk0MGRiSHgtWTZldWt2emk3bWdHcFpuRTNDOE80bUY1TnBrS2VoOVJPd196a2tPR2hpR0FHVG85N3gzd0ZjZ29Bd0J2WXdNS0haYw?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxPNnZOMFFuSHlpbkRqa3BBejUtcHBjcUhFdTJ3XzY1Mm54WUNNWmNWUnRkMGlnbVJFRXAxdEFxemN2QS1qcTYwNDBISzFuRms0RWs3ZXI5MkRZZzc4dXN2eGtaWVVxMHRlaUswUFpncXQ3eE4zZWtHOURxcVhJR0ZkS2hZMmdLYmZNYmJBUDFUUDc0R2hmajBWZjhPWjBkMGY5VTNtZTkwUnN0ZmtYbWZNY0h2ell1YTFVMmJENy1xOEpSMXZ2d2s3V2ZCbWxXRWczZ2FN0gHYAUFVX3lxTE5XYzVjQkZlLUJ1MDRiZFBCUVlWREY3Ny0zalQ2TU91Z0xicHJPb2F3cW0xdWpiNkdmS1Q2LVZvRlpnWXdMR0JTQUlvSk5YVjBrUHNYakhCUV92WGdRaTBDWkRqUDRoTTVNWHlpWFJ3eF9LMkNlWkEwUkR0aXRGS2dpMXpJYklVTWxmWHYzbVlWVXExd3g0NUo5Nk5HYWZjYldMcWVfLTg1blZqUDlYX054OEJBdW90bHdDZ1ZhVE9vaDJtNlRoMXNEblQ0Q1ZZRzc5bGo1dWl5RA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
