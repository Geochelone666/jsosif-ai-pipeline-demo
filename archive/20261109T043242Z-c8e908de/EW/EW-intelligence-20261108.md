# EW Intelligence Report

- ticker: **EW**
- Report as_of: **2026-11-08**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/EW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/EW/key-statistics/
- AI analysis snapshot as_of: **2026-11-08**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-09T04:48:35.802824+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 7, 'ai': 9, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261108T041758Z-43fb2458/EW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 10 named publishers; 0 exact duplicates; 22 HTTPS source links; largest publisher share 27.27%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 102.1400 |
| Return 1D (%) | 1.3093 |
| Return 1W (%) | 11.0097 |
| Return 1M (%) | 18.1082 |
| Return YTD (%) | 19.8123 |
| Return 1Y (%) | 23.8962 |
| Annualized volatility (%) | 25.4771 |
| Beta vs SPY | 0.5193 |
| Max drawdown (%) | -13.1855 |
| Sharpe (rf=0) | 0.9714 |
| Downside deviation (rf=0, %) | 16.8688 |
| Sortino (rf=0) | 1.4671 |
| Historical VaR 95% (1D, %) | 2.5317 |
| Historical ES 95% (1D, %) | 3.1155 |
| Correlation vs SPY | 0.2762 |
| Tracking error vs SPY (%) | 25.3377 |
| P/E (trailing) | 59.38 |
| P/B | 5.41 |
| EV/EBITDA | 26.20 |
| Revenue growth (%) | 10.50 |
| Forward P/E (estimate) | 30.02 |
| Gross margin (%) | 78.02 |
| Operating margin (%) | 30.15 |
| Return on equity (%) | 9.33 |
| Free cash flow yield (%) | 1.95 |
| MA50 | 88.9206 |
| Close vs MA50 (%) | 14.8665 |
| MA200 | 85.7719 |
| Close vs MA200 (%) | 19.0833 |
| RSI (14, Wilder) | 76.8321 |
| MACD (12,26) | 3.1892 |
| MACD signal (9) | 1.8780 |
| MACD histogram | 1.3112 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'EW': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 102.1400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.3093 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 11.0097 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 18.1082 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 19.8123 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 23.8962 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.4771 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.8688 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4671 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5317 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.1155 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2762 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 25.3377 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5193 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.1855 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9714 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 30.0218 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 78.0180 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 30.1540 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.3330 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.9502 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 59.3837 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 76.8321 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.3112 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 14.8665 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 19.0833 -> Clearly above the moving-average trend level.

## TAILWINDS

### Edwards Lifesciences (EW) Q3 Earnings Beat Expectations, Raises Guidance
- Summary: Edwards Lifesciences (EW) Q3 Earnings Beat Expectations, Raises Guidance
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxORDBnalp4NXdSVVd4TGtKdkN4b0Rwb1RjUmlQUEQ4dGRmWkFaM0gzV2lhZTg0bXlfUUsyVndiX1IxcF94UzdCNXF0TUZDV1oxU0ZteUNtdzBHb2Uwd3R4T2ZpNWFOaU5yOGRkS044YkEzUm1hUThNMkM1Q3JIQThPbVA4eEZNS2g5VzlxVG5Rb2ltdE9qZEhVdU5YRGhaYVRKWDBFU00zRk95UERG?oc=5>

### EDWARDS LIFESCIENCES ($EW) Releases Q3 2026 Earnings, Stock Rises
- Summary: EDWARDS LIFESCIENCES ($EW) Releases Q3 2026 Earnings, Stock Rises
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOVXI5ODZCMTdadEFoVEVINmlYZlVQSENUUUlXY2tDTWp3UzVGTHZ3bGZYS2pUaE5ZS3djR21laXBIUmQzaV9qQXRwcnBSSVFxVzNUR08zZDJTdzA4MjJYZm9Ga3B5c0J0Q2pFMWNIWmlXZTdmejNIMTRRZE92WGNSaHlLSktFSkRzYm5sdTdLb2taclFFVk1Wako4T1YtT2RvaHlITHBCOWNoZw?oc=5>

### Key facts: EW beats, lifts view; TAVR meets goals; stock hits 2022 high
- Summary: EW beat expectations, TAVR met goals, and stock reached 2022 high.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxOTmtpTGtIenh0em82Ym0yRlpjSG5JSmthcmo4WFFTYUxLSmhhRDdjUC1BdXJoWXUwZThzNzJXYXI5OGdZb3otVkJucGFKN3U3MXpmRDJYRGstTVdzODZMRGRHdzd3V09wa2s3ZFlnUHMtbVczQmo1eXBnR0NXN0NyMlkzTnZTM0lMTDlUY1Y5dmtETzBId3Y3d2k5aUhiMk9nQTZRdlNyUUloRkZqVGpnTHN3bWlaV1F0ZXFZWHIxUE1ocWlfaWtQQw?oc=5>

### CAH Shares Post New Record, EW Stock Hits Over Three-Year High – What’s Driving Today’s Rally?
- Summary: EW shares surged to a three‑year high amid CAH’s record performance, boosting investor sentiment.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxQeHY4M0VjTlJtbmZsMGYydjA0YU1EelBvMFpMdHl1VlVuTUxveGdtU29JUEVVamNQc1pwN1VKU2NzSVA3VHo1V05BdVlkR2lnVHkzZXVzWTFPVWlkZTV6UmJGcGR2OXVFajk2WkhYbXZVdDY4bEVTMkNTUm5HbHRPQWlXbVJsa0hUbnVOalExVnNvNm9YNHV2SHJXZ2wwdkxMNUR6aThXTFF0UmdZVVI3M0piMWVqTUJaRVZGLU1SY25LOTV6c1NGcm9uWVJqRV9fU1pSLXlrUDZidG0yR2dONEp6d2d6d9IB6wFBVV95cUxORndMVGJzdnJHa2Z1bllwYkFlTi1LY0lralVYZW9nMlpBRnBCdzc1VUpqaEpsUFdnazltYkhRM2Z3UVVmaERnaUhXcjZXNFg5TTVmb2V4bU5pZkJuaHh4VzVwYkZhdzE3dzI0eVZpekp1NlNFMTJyQkRJdmdQREdkSm45b1ZYTEdGMWd4SVpqeGhFeXNkQmw1VXRQRkViVFFTbGpGTEtBVUdCTXJkQUllOVQzSUgxU3IwRnRNSGRHc1M2aU9Ma1FCY2lvbTVtc2xXN1dpS19OZU1FUVNoTTgteEJNVFBLQzlTZVk4?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Edwards Lifesciences (EW) Trial Win Puts Fair Value Back In Focus
- Summary: Edwards Lifesciences (EW) Trial Win Puts Fair Value Back In Focus
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxObHM0ZTM0eE5FOUNpV1JyT05FRXRtN2JVNHRVT1Y0eVJLeWl3MEJoMGxlSHVXNm43eGVvSmdqMlpCSGZkM203UHRqSHB3YlA2TEc5TXhYaGtQamVqV1pFNWo2VG5sdmNWTXQ4LWMwelVmdTduQWl6dk45M2hSdWVsQUdIY3doRDJ6dWIxblhPeE82SGZ2WXFSN1Zn?oc=5>

### Edwards Lifesciences Q3 2026 Earnings Call Transcript
- Summary: Edwards Lifesciences Q3 2026 Earnings Call Transcript
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPX1F6OFo3WGZ5T2ZXdVVabEsyTmZHMGRudkdGZk84V1lxdVNvYl9LM2tzNHpleXc5REptVVB2MWczb19ua0xLejctT3RGUXBNLWJ4eE9ZOUVtMlU0VFZqQWk2MFVOREd4UDdWekF5YjF3OTRWQVdOc2pzNldHUl9nRlM2RzBTWEw4UWRZWHBkZkNuTTcwVEw0ZTM4WGJYLXc?oc=5>

### Edwards Lifesciences Corporation $EW Stock Sold by Boston Trust Walden Corp
- Summary: Edwards Lifesciences Corporation $EW Stock Sold by Boston Trust Walden Corp
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxPMElrSERNVnNHejFNS3o5bjhOSWJnc1lHME15LWZZQXpXTVd1bDJadHhLaTlQTHdldEhxQmV6TW04QUlNY1duQUNackdvejBRRXBlVEI2QXUzMUR4N0txZG04UUpTeXY1U182S2w2NDZXVzJMMnRzUVBIcXA5bEtGcHdpZjdoMzFGOVJWMS13X1p3MjZHNkIxSkFGWTJ3ckh6MVIwU081YjJmaFdQVlVjSHNqUVdfMVZEaDc4YmI4eVU2YWcybGJuYkFTei1UUVQ4?oc=5>

### Edwards Lifesciences Corporation $EW Stock Sold by Sumitomo Mitsui Trust Group Inc.
- Summary: Edwards Lifesciences Corporation $EW Stock Sold by Sumitomo Mitsui Trust Group Inc.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxQS1A3NGE0RHNKSUc2c05xaTVYS04wMVl2TEQtX0xIc0dqaHppYnNZU0tTT1huNFROQUhLYU5lNkRwb0lSUXFSZEVwWDZWenVCOG95QjVaaFVYbnp3R1RIMU5qeHJYMXA0TVNsMGxUaTNBcEFqUWQxd1Vkb3FXbEV4YWlKQVpXcGI5WTh4YkV2aVVQb281VU5kNFh4cHljUkIyamdBQ09YMkNSRXVjWUptZWtLbzNOWVFtMHdXYjZ0bGFHSFJscE9ZV2tuNUVhOG80WWhiTnp3RzFOQQ?oc=5>

### Edwards Lifesciences Corporation $EW Shares Sold by Factory Mutual Insurance Co.
- Summary: Edwards Lifesciences Corporation $EW Shares Sold by Factory Mutual Insurance Co.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNbXBxazF4UU53ZmtWT1hiX1Z2RUlWR0lUMnNqdG1jWE0ySURJRmkzMjUyM3hPNTNKcGQyQlc4TnVRak1DRDRDazF6ckdJdFBzZXdsYVhwMGFNSUdWQV96T2RGM0dLVG43ZWx3UGJtZ0NibXk2Qnd1QmdZZGc1Q0RYVEdRT19hVlZZWS1laDIzaEJSbEJobThrd1FGNG9FUUd0N2M3bHFmOHozbjEyQWlfa1B1ZGhWYlN1MXdTVi1OcVVLMWdrSWZCRlZtdklteF8tSXZ2SWhR?oc=5>

### Edwards Lifesciences (EW) Stock Looks Fully Priced On Cash Flow
- Summary: Analyst view that EW stock is fully priced based on cash flow projections.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxNNFE1LVpjaWwxdFc5RU9vY1VpRG1rcW5BbnktTktEZ2hnUC1RZ2xzbV9hSUdoTzJHUlNCcnFKbHZKRDNfYVZGRm5hS09wdHkxM2R6NUlja1JOTkxHMlJNOVQ2UkZaOXVubHBlelhWVXN4RWwxV20xZkV0WFZ3SXF2WmNEMUtZc0x1NW5QRUZwd1JXa1VRSFZuXzlmT0dxY0dHTzc2dXM1SWIwRlgyZEY1V3JmbmdnOTg3eUdhWUZVeTNWeUdmNFQ0ZXFjWWdpeGFYVkFF0gHYAUFVX3lxTE9TaXRUTzYwLUU3ZGlqck00NXFCMk5oU3llaWFiNE1oRVJlNGJEeDFDY0hqclNVa1hpMDN0N1pxMzktODNsbFhGQlQ5YnJnSEtfYjRUZVQzTnR3bnk3Yk5XUmI0VWZkS0ttYzBHVmhPeWl1dmI0RUE0U2ZqMzNQZVhBTWxlRllKSjhDYkJDVTk0MGRiSHgtWTZldWt2emk3bWdHcFpuRTNDOE80bUY1TnBrS2VoOVJPd196a2tPR2hpR0FHVG85N3gzd0ZjZ29Bd0J2WXdNS0haYw?oc=5>

### What Edwards Lifesciences Stock Beat And Raised Outlook Means For Shareholders
- Summary: Earnings beat and new guidance boost investor confidence.
- Date: 2026-11-08 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxOTjVBZzdtOFJCSFFmdHAyWjFZSWFJcWlFQzI0X0d5QjZLb0w2Vzk3aWdnWkdabXJuUF9YSDYxcDg2cUJpZFV0Q25JTkZtMUlpRjJCWEtZcmdCM2VrUXBJalp5aFhCSW5wSHVPaTM2U2pJd3VSa1N3TTRYX3RVLTE2YUw0TUdkU09fSUd3MmVjR0IwZ0ZmUjh6bmhFMUNrSXN3OFNrN0FrUU5yWnV3R1NEblc2N0pDd0xnb3JNSGh0TElweHowU3ZzYlRWWEFiM0N4Wnhv0gHYAUFVX3lxTE03ODlmY25icldSdlMzbHNpWF90M0xvdW9DOV96RGtDV1RwZVpYV3h2U2lNb0lsNEY1Y2ZCbC01eG5MT2dZQm1VeVBOTVRDYnZtNjdCeld2QXVLMHM1WVctaTJTejA5dGlLdUFfcVdoY1ptbDRoTTF2TmMxQjl0TTB0WHFaTURVUDE3bU15dnV6UnNvQ1pyRVBiQ2s2TnJnYzJZOEM1N241UF9lUGxmQmZ3X0dpcXhnOHRFNGRlTGpWSkhveUNrMlJCQkJBNG9IdU5HY1NvRlBVTw?oc=5>

### Edwards Lifesciences (EW) Could Be 21% Undervalued After Earnings Guidance And Trial Data
- Summary: Guidance and trial data suggest undervaluation.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxPNnZOMFFuSHlpbkRqa3BBejUtcHBjcUhFdTJ3XzY1Mm54WUNNWmNWUnRkMGlnbVJFRXAxdEFxemN2QS1qcTYwNDBISzFuRms0RWs3ZXI5MkRZZzc4dXN2eGtaWVVxMHRlaUswUFpncXQ3eE4zZWtHOURxcVhJR0ZkS2hZMmdLYmZNYmJBUDFUUDc0R2hmajBWZjhPWjBkMGY5VTNtZTkwUnN0ZmtYbWZNY0h2ell1YTFVMmJENy1xOEpSMXZ2d2s3V2ZCbWxXRWczZ2FN0gHYAUFVX3lxTE5XYzVjQkZlLUJ1MDRiZFBCUVlWREY3Ny0zalQ2TU91Z0xicHJPb2F3cW0xdWpiNkdmS1Q2LVZvRlpnWXdMR0JTQUlvSk5YVjBrUHNYakhCUV92WGdRaTBDWkRqUDRoTTVNWHlpWFJ3eF9LMkNlWkEwUkR0aXRGS2dpMXpJYklVTWxmWHYzbVlWVXExd3g0NUo5Nk5HYWZjYldMcWVfLTg1blZqUDlYX054OEJBdW90bHdDZ1ZhVE9vaDJtNlRoMXNEblQ0Q1ZZRzc5bGo1dWl5RA?oc=5>

### Edwards Lifesciences' PASCAL System Trial Success Boosts Prospec
- Summary: Trial success supports product prospects.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPLTNNVF91VC1xTndlSFVLRzhuazZJM1d4MnZXVlUyRVZfeGRtUVJ5bml0THNBYnV6ZzRYcm5BcmRCRFVjYnUwSEN5OEVPRUVDWWUwR3dIV0JJU0pUQjdmOHJjNVZRbDR0aFhjcUpRMmwtcEpzOUpNOWx2TTJUbXhYd3FReG83aUtIUWRmR2pjWThZNjJ2UWtEMHJJdklhdXVSaWR6NkNyZzNvS256UTRXX3dKZm44OUoz?oc=5>

### Edwards Lifesciences (EW) Reports Positive CLASP II TR Trial Res
- Summary: Positive CLASP II TR trial results for Edwards Lifesciences, indicating improved outcomes for transcatheter aortic valve replacement.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOb0pDekI2dTZDeXNHOXZMM1lRX0VVQUtLTjEzSEtQMjN1aTdiR3BqcUJCWk4wSFJ2bnB2QUNnNG1CMWRiN1c4QXplRlVrV3dXTjhuTFZjNUhUb00yQWN0TG9GdmdXM2RVaXJYZVFEd1Y3UWZ0eTZVdV9DNTRnQVRlM2NhN0V4QXFOZmhKY2lEWTQzVV8yQjBxOUtoVFhhX0gzcUtSYTdkVUJDSy1OMm81cWNZQmRqa0ZYdGZMLVBrUHQ?oc=5>

### Edwards Lifesciences (EW) Trial Results Put Earlier TAVR Use In Focus
- Summary: Trial results suggest earlier use of Edwards Lifesciences TAVR devices may benefit patients, highlighting potential shift in treatment timing.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQbTJEOW5FTER5Qy1EZjFkUjdaTnpPMEphY0I3SFY0Z3A5R1lfSTZfQVNUQmxhTVVjbExZQTNKX3l0RVhsR2Y5UHpzQXh5SWR4aVhFWm1wVENiVTdEWllkc2VPend3X0dmYlhBUmczSnViWVN1TndzeDJ0ZEsyOF9SRkNVWHYwVEQ0eW9tWnkyOFIyaUF0TzRrQ0RRLVZOMzdUZDY4UlNabW9kbEtmMlp0bDBvRkhYWkdHb3dKLTZpYlVGTmN5b2xhTnQwUU9mSExIMlUw0gHYAUFVX3lxTFBxNnB1N0tqSW4taTFsRW1uSnZHTWREUkMteDM3LThyUm45NVd4bTVKVzdEWGxFRy00YXpaUWwwWHdMTFB3aTVCUk5vMWtrQzdzdkZGeGtyZU5rZmpWdEJvVHJlTW1Fd29RX0VDd05DbGhwbTVEMGpGbE53amxFdUVVOVpKWkluX1R5RnhkZzJVYUh1Q3dNaUFmTFl0Tm5fT2NDUk1UVzB3U2hHMENnNEFhaUh2QVhyNjgzVzBoZ2MxYkJQX1JCV29hYW1iSWhwNElxbDBIZ1BDcA?oc=5>

### 79,661 Edwards Lifesciences Corporation $EW Shares Acquired by TrinityBridge Ltd
- Summary: TrinityBridge Ltd acquired 79,661 shares of Edwards Lifesciences, reflecting investor activity in the company’s equity.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNZ0tIU0xlRGFlbVplSDVKSXNOTFdrTTBGWXRFa2VkOEtmTTEyQkNha2hQa0dqdWdLdE9mQS1IZnIyaldlcUVTcHF5V1R0bTZveVFtZFMxdXRtaWV2RXMweHVDNmpxSDJ0RGQyNVlUbHBpNTJMM0FZQk9nMXFIUHlteXBXcHU2QzB2S1Q3MjFrbmU1UW93RmJBOUVuNEk1OXZ2WFVSTkVtczlGaE5MSjQ2TUNpd285aVFfNXhVTlpSY2FBMFZ3c0w4X2JQRWFmVG5OREhvTVR3?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **EW** | **59.38** | **5.41** | **26.20** | **10.50** | **58,730,500,096.00 USD** | **23.90** |
| MDT | 25.01 | 2.59 | 14.43 | 13.70 | 130,216,247,296.00 USD | 16.78 |
| BSX | 18.04 | 2.42 | N/A | 1.40 | 61,964,984,320.00 USD | -56.84 |
| ABT | 41.02 | 3.73 | 19.04 | 14.50 | 190,392,336,384.00 USD | -9.83 |

Peers fetched as_of: 2026-11-08; EW reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-08

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMirAFBVV95cUxORDBnalp4NXdSVVd4TGtKdkN4b0Rwb1RjUmlQUEQ4dGRmWkFaM0gzV2lhZTg0bXlfUUsyVndiX1IxcF94UzdCNXF0TUZDV1oxU0ZteUNtdzBHb2Uwd3R4T2ZpNWFOaU5yOGRkS044YkEzUm1hUThNMkM1Q3JIQThPbVA4eEZNS2g5VzlxVG5Rb2ltdE9qZEhVdU5YRGhaYVRKWDBFU00zRk95UERG?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOVXI5ODZCMTdadEFoVEVINmlYZlVQSENUUUlXY2tDTWp3UzVGTHZ3bGZYS2pUaE5ZS3djR21laXBIUmQzaV9qQXRwcnBSSVFxVzNUR08zZDJTdzA4MjJYZm9Ga3B5c0J0Q2pFMWNIWmlXZTdmejNIMTRRZE92WGNSaHlLSktFSkRzYm5sdTdLb2taclFFVk1Wako4T1YtT2RvaHlITHBCOWNoZw?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxOTmtpTGtIenh0em82Ym0yRlpjSG5JSmthcmo4WFFTYUxLSmhhRDdjUC1BdXJoWXUwZThzNzJXYXI5OGdZb3otVkJucGFKN3U3MXpmRDJYRGstTVdzODZMRGRHdzd3V09wa2s3ZFlnUHMtbVczQmo1eXBnR0NXN0NyMlkzTnZTM0lMTDlUY1Y5dmtETzBId3Y3d2k5aUhiMk9nQTZRdlNyUUloRkZqVGpnTHN3bWlaV1F0ZXFZWHIxUE1ocWlfaWtQQw?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxQeHY4M0VjTlJtbmZsMGYydjA0YU1EelBvMFpMdHl1VlVuTUxveGdtU29JUEVVamNQc1pwN1VKU2NzSVA3VHo1V05BdVlkR2lnVHkzZXVzWTFPVWlkZTV6UmJGcGR2OXVFajk2WkhYbXZVdDY4bEVTMkNTUm5HbHRPQWlXbVJsa0hUbnVOalExVnNvNm9YNHV2SHJXZ2wwdkxMNUR6aThXTFF0UmdZVVI3M0piMWVqTUJaRVZGLU1SY25LOTV6c1NGcm9uWVJqRV9fU1pSLXlrUDZidG0yR2dONEp6d2d6d9IB6wFBVV95cUxORndMVGJzdnJHa2Z1bllwYkFlTi1LY0lralVYZW9nMlpBRnBCdzc1VUpqaEpsUFdnazltYkhRM2Z3UVVmaERnaUhXcjZXNFg5TTVmb2V4bU5pZkJuaHh4VzVwYkZhdzE3dzI0eVZpekp1NlNFMTJyQkRJdmdQREdkSm45b1ZYTEdGMWd4SVpqeGhFeXNkQmw1VXRQRkViVFFTbGpGTEtBVUdCTXJkQUllOVQzSUgxU3IwRnRNSGRHc1M2aU9Ma1FCY2lvbTVtc2xXN1dpS19OZU1FUVNoTTgteEJNVFBLQzlTZVk4?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxObHM0ZTM0eE5FOUNpV1JyT05FRXRtN2JVNHRVT1Y0eVJLeWl3MEJoMGxlSHVXNm43eGVvSmdqMlpCSGZkM203UHRqSHB3YlA2TEc5TXhYaGtQamVqV1pFNWo2VG5sdmNWTXQ4LWMwelVmdTduQWl6dk45M2hSdWVsQUdIY3doRDJ6dWIxblhPeE82SGZ2WXFSN1Zn?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPX1F6OFo3WGZ5T2ZXdVVabEsyTmZHMGRudkdGZk84V1lxdVNvYl9LM2tzNHpleXc5REptVVB2MWczb19ua0xLejctT3RGUXBNLWJ4eE9ZOUVtMlU0VFZqQWk2MFVOREd4UDdWekF5YjF3OTRWQVdOc2pzNldHUl9nRlM2RzBTWEw4UWRZWHBkZkNuTTcwVEw0ZTM4WGJYLXc?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxPMElrSERNVnNHejFNS3o5bjhOSWJnc1lHME15LWZZQXpXTVd1bDJadHhLaTlQTHdldEhxQmV6TW04QUlNY1duQUNackdvejBRRXBlVEI2QXUzMUR4N0txZG04UUpTeXY1U182S2w2NDZXVzJMMnRzUVBIcXA5bEtGcHdpZjdoMzFGOVJWMS13X1p3MjZHNkIxSkFGWTJ3ckh6MVIwU081YjJmaFdQVlVjSHNqUVdfMVZEaDc4YmI4eVU2YWcybGJuYkFTei1UUVQ4?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxQS1A3NGE0RHNKSUc2c05xaTVYS04wMVl2TEQtX0xIc0dqaHppYnNZU0tTT1huNFROQUhLYU5lNkRwb0lSUXFSZEVwWDZWenVCOG95QjVaaFVYbnp3R1RIMU5qeHJYMXA0TVNsMGxUaTNBcEFqUWQxd1Vkb3FXbEV4YWlKQVpXcGI5WTh4YkV2aVVQb281VU5kNFh4cHljUkIyamdBQ09YMkNSRXVjWUptZWtLbzNOWVFtMHdXYjZ0bGFHSFJscE9ZV2tuNUVhOG80WWhiTnp3RzFOQQ?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNbXBxazF4UU53ZmtWT1hiX1Z2RUlWR0lUMnNqdG1jWE0ySURJRmkzMjUyM3hPNTNKcGQyQlc4TnVRak1DRDRDazF6ckdJdFBzZXdsYVhwMGFNSUdWQV96T2RGM0dLVG43ZWx3UGJtZ0NibXk2Qnd1QmdZZGc1Q0RYVEdRT19hVlZZWS1laDIzaEJSbEJobThrd1FGNG9FUUd0N2M3bHFmOHozbjEyQWlfa1B1ZGhWYlN1MXdTVi1OcVVLMWdrSWZCRlZtdklteF8tSXZ2SWhR?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxNNFE1LVpjaWwxdFc5RU9vY1VpRG1rcW5BbnktTktEZ2hnUC1RZ2xzbV9hSUdoTzJHUlNCcnFKbHZKRDNfYVZGRm5hS09wdHkxM2R6NUlja1JOTkxHMlJNOVQ2UkZaOXVubHBlelhWVXN4RWwxV20xZkV0WFZ3SXF2WmNEMUtZc0x1NW5QRUZwd1JXa1VRSFZuXzlmT0dxY0dHTzc2dXM1SWIwRlgyZEY1V3JmbmdnOTg3eUdhWUZVeTNWeUdmNFQ0ZXFjWWdpeGFYVkFF0gHYAUFVX3lxTE9TaXRUTzYwLUU3ZGlqck00NXFCMk5oU3llaWFiNE1oRVJlNGJEeDFDY0hqclNVa1hpMDN0N1pxMzktODNsbFhGQlQ5YnJnSEtfYjRUZVQzTnR3bnk3Yk5XUmI0VWZkS0ttYzBHVmhPeWl1dmI0RUE0U2ZqMzNQZVhBTWxlRllKSjhDYkJDVTk0MGRiSHgtWTZldWt2emk3bWdHcFpuRTNDOE80bUY1TnBrS2VoOVJPd196a2tPR2hpR0FHVG85N3gzd0ZjZ29Bd0J2WXdNS0haYw?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOTjVBZzdtOFJCSFFmdHAyWjFZSWFJcWlFQzI0X0d5QjZLb0w2Vzk3aWdnWkdabXJuUF9YSDYxcDg2cUJpZFV0Q25JTkZtMUlpRjJCWEtZcmdCM2VrUXBJalp5aFhCSW5wSHVPaTM2U2pJd3VSa1N3TTRYX3RVLTE2YUw0TUdkU09fSUd3MmVjR0IwZ0ZmUjh6bmhFMUNrSXN3OFNrN0FrUU5yWnV3R1NEblc2N0pDd0xnb3JNSGh0TElweHowU3ZzYlRWWEFiM0N4Wnhv0gHYAUFVX3lxTE03ODlmY25icldSdlMzbHNpWF90M0xvdW9DOV96RGtDV1RwZVpYV3h2U2lNb0lsNEY1Y2ZCbC01eG5MT2dZQm1VeVBOTVRDYnZtNjdCeld2QXVLMHM1WVctaTJTejA5dGlLdUFfcVdoY1ptbDRoTTF2TmMxQjl0TTB0WHFaTURVUDE3bU15dnV6UnNvQ1pyRVBiQ2s2TnJnYzJZOEM1N241UF9lUGxmQmZ3X0dpcXhnOHRFNGRlTGpWSkhveUNrMlJCQkJBNG9IdU5HY1NvRlBVTw?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxPNnZOMFFuSHlpbkRqa3BBejUtcHBjcUhFdTJ3XzY1Mm54WUNNWmNWUnRkMGlnbVJFRXAxdEFxemN2QS1qcTYwNDBISzFuRms0RWs3ZXI5MkRZZzc4dXN2eGtaWVVxMHRlaUswUFpncXQ3eE4zZWtHOURxcVhJR0ZkS2hZMmdLYmZNYmJBUDFUUDc0R2hmajBWZjhPWjBkMGY5VTNtZTkwUnN0ZmtYbWZNY0h2ell1YTFVMmJENy1xOEpSMXZ2d2s3V2ZCbWxXRWczZ2FN0gHYAUFVX3lxTE5XYzVjQkZlLUJ1MDRiZFBCUVlWREY3Ny0zalQ2TU91Z0xicHJPb2F3cW0xdWpiNkdmS1Q2LVZvRlpnWXdMR0JTQUlvSk5YVjBrUHNYakhCUV92WGdRaTBDWkRqUDRoTTVNWHlpWFJ3eF9LMkNlWkEwUkR0aXRGS2dpMXpJYklVTWxmWHYzbVlWVXExd3g0NUo5Nk5HYWZjYldMcWVfLTg1blZqUDlYX054OEJBdW90bHdDZ1ZhVE9vaDJtNlRoMXNEblQ0Q1ZZRzc5bGo1dWl5RA?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPLTNNVF91VC1xTndlSFVLRzhuazZJM1d4MnZXVlUyRVZfeGRtUVJ5bml0THNBYnV6ZzRYcm5BcmRCRFVjYnUwSEN5OEVPRUVDWWUwR3dIV0JJU0pUQjdmOHJjNVZRbDR0aFhjcUpRMmwtcEpzOUpNOWx2TTJUbXhYd3FReG83aUtIUWRmR2pjWThZNjJ2UWtEMHJJdklhdXVSaWR6NkNyZzNvS256UTRXX3dKZm44OUoz?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOb0pDekI2dTZDeXNHOXZMM1lRX0VVQUtLTjEzSEtQMjN1aTdiR3BqcUJCWk4wSFJ2bnB2QUNnNG1CMWRiN1c4QXplRlVrV3dXTjhuTFZjNUhUb00yQWN0TG9GdmdXM2RVaXJYZVFEd1Y3UWZ0eTZVdV9DNTRnQVRlM2NhN0V4QXFOZmhKY2lEWTQzVV8yQjBxOUtoVFhhX0gzcUtSYTdkVUJDSy1OMm81cWNZQmRqa0ZYdGZMLVBrUHQ?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQbTJEOW5FTER5Qy1EZjFkUjdaTnpPMEphY0I3SFY0Z3A5R1lfSTZfQVNUQmxhTVVjbExZQTNKX3l0RVhsR2Y5UHpzQXh5SWR4aVhFWm1wVENiVTdEWllkc2VPend3X0dmYlhBUmczSnViWVN1TndzeDJ0ZEsyOF9SRkNVWHYwVEQ0eW9tWnkyOFIyaUF0TzRrQ0RRLVZOMzdUZDY4UlNabW9kbEtmMlp0bDBvRkhYWkdHb3dKLTZpYlVGTmN5b2xhTnQwUU9mSExIMlUw0gHYAUFVX3lxTFBxNnB1N0tqSW4taTFsRW1uSnZHTWREUkMteDM3LThyUm45NVd4bTVKVzdEWGxFRy00YXpaUWwwWHdMTFB3aTVCUk5vMWtrQzdzdkZGeGtyZU5rZmpWdEJvVHJlTW1Fd29RX0VDd05DbGhwbTVEMGpGbE53amxFdUVVOVpKWkluX1R5RnhkZzJVYUh1Q3dNaUFmTFl0Tm5fT2NDUk1UVzB3U2hHMENnNEFhaUh2QVhyNjgzVzBoZ2MxYkJQX1JCV29hYW1iSWhwNElxbDBIZ1BDcA?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNZ0tIU0xlRGFlbVplSDVKSXNOTFdrTTBGWXRFa2VkOEtmTTEyQkNha2hQa0dqdWdLdE9mQS1IZnIyaldlcUVTcHF5V1R0bTZveVFtZFMxdXRtaWV2RXMweHVDNmpxSDJ0RGQyNVlUbHBpNTJMM0FZQk9nMXFIUHlteXBXcHU2QzB2S1Q3MjFrbmU1UW93RmJBOUVuNEk1OXZ2WFVSTkVtczlGaE5MSjQ2TUNpd285aVFfNXhVTlpSY2FBMFZ3c0w4X2JQRWFmVG5OREhvTVR3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
