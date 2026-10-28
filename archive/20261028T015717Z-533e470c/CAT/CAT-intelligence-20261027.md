# CAT Intelligence Report

- ticker: **CAT**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/CAT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CAT/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:18:30.827272+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 6, 'ai': 15, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/CAT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'short_term_price_move_in_structural_risks': 2}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 32.0%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 713.3100 |
| Return 1D (%) | 3.0601 |
| Return 1W (%) | -1.4111 |
| Return 1M (%) | -12.9718 |
| Return YTD (%) | 25.5740 |
| Return 1Y (%) | 36.4858 |
| Annualized volatility (%) | 40.6190 |
| Beta vs SPY | 1.8564 |
| Max drawdown (%) | -35.3672 |
| Sharpe (rf=0) | 0.9702 |
| Downside deviation (rf=0, %) | 26.5358 |
| Sortino (rf=0) | 1.4851 |
| Historical VaR 95% (1D, %) | 4.0274 |
| Historical ES 95% (1D, %) | 5.1314 |
| Correlation vs SPY | 0.5805 |
| Tracking error vs SPY (%) | 34.8180 |
| P/E (trailing) | 30.71 |
| P/B | 16.91 |
| EV/EBITDA | 22.59 |
| Revenue growth (%) | 24.00 |
| Forward P/E (estimate) | 21.89 |
| Gross margin (%) | 29.71 |
| Operating margin (%) | 22.18 |
| Return on equity (%) | 56.97 |
| Free cash flow yield (%) | 1.54 |
| MA50 | 791.2660 |
| Close vs MA50 (%) | -9.8521 |
| MA200 | 806.1594 |
| Close vs MA200 (%) | -11.5175 |
| RSI (14, Wilder) | 36.8275 |
| MACD (12,26) | -30.3798 |
| MACD signal (9) | -23.5693 |
| MACD histogram | -6.8106 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CAT': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 713.3100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.0601 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.4111 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -12.9718 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 25.5740 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 36.4858 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 40.6190 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.5358 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4851 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.0274 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1314 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5805 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.8180 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8564 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -35.3672 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9702 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.8906 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 29.7130 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 22.1830 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 56.9720 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.5398 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 30.7064 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.8275 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -6.8106 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.8521 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -11.5175 -> Clearly below the moving-average trend level.

## TAILWINDS

### Caterpillar Inc (CAT) Shares Surge 3.1% -- What GF Score of 91 T
- Summary: Caterpillar Inc (CAT) Shares Surge 3.1% -- What GF Score of 91 T
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxOajNfSzNqdjBoOWRLc1dhb0ZHMGNwd0VURzI5UmJWc1dhbm9zMlQzMXo5bkZNMzdoNnpUdVUtNkt2OUNOX1lqMmt0RGlybmppdjQ0ellOUGY5UFl1MDJOalMwZy1RcWZYOXpVLWowM3dyWk1ZRjFpc0dyU2VlWDhPdTJhVkhpSTU0cGZHUEx1bWFiY0lKOTdDbVE3dllIcGljV2UwbEZ2SEVGNEN5cHNR?oc=5>

### Bears are Losing Control Over Caterpillar (CAT), Here's Why It's a 'Buy' Now
- Summary: Analysts view current dip as buying opportunity.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQS195elp0TUR6MkxjdzRZTFRjd1VwZklHNUk0UDF4NXFzY0xWZlNEZnM0Y1dCUXpXSklhdmV4Qi1MLVpSTkEzT3Q1dGJyTW5yRHFZOXg3eU03clhYZjlFN1g3SlJtZUxHT0ZkZ3ZzZlRQOFhRU2NiTTZ2TmU2LWM1OEszSTdRWXQ0S2hsc1JyRXNCRmFjd1BwWm5PTU1TZFF0VFVxVQ?oc=5>

### Caterpillar (CAT) Laps the Stock Market: Here's Why
- Summary: Positive stock performance attributed to strong fundamentals and market sentiment.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPdXd6c1dXUXJFUkdfUEtBbXdMYlkwYkdZTlRSa1R6WDZ3S2dFZDhzYThnV1FVdHZubXZKb1F0RXNuWkgxOFpiaE9NVE04cmRCaU9va3RYR1k3NlJJYVJFc1h6RkFnZmpEZGZ0c2Rrb044UGRzUXlIYXR2YXE1OHEyb1V3dHNsRGVqaHo4dWx0QnlVVm5nbExoNjVDVGItUjA?oc=5>

### Fund Update: 44,390 CATERPILLAR (CAT) shares added to UniSuper Management Pty Ltd portfolio
- Summary: UniSuper added 44,390 CAT shares, indicating institutional confidence.
- Date: 2026-10-26 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxOSmZzNDUxcFNFQ2FqcWcwWG9XQ1lkczFaX0JuNG9SZnU0LTlaTjN2ZXdJSjQ2TlUyeUpEc0F5NHNnem9HVEZRMDIxU3JMRHo3V2tkaHV3OTluTHlwZUtzOVoydGIzMXcyZW9JSUxLYl8tSWVKMjVMUFJZSmJoLUZISzJNa3lhRHVJeXBVTGhleTNVb3R5enpXNXFzS1dwMEs1cjJOaGs3LXptVkJsa2hiSkd1eHRIa2lzUS1XeG5MQi1FcGYwNTVQd1VDR3hHUQ?oc=5>

### Caterpillar Inc Stock (CAT) Moved Up by 3.02% on Oct 27: Key Drivers Unveiled
- Summary: Stock rose 3.02% on Oct 27, citing key drivers that boosted investor confidence.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPbVpQbGFFa1diWWJIQmlhVGNWZ2F4d3kzUWVOakdpX3RuTUlOblVZZDNuX2RQNUNmcGpGSVlPeGhmUWxFbUprdnFOeWh5TWRTdGRlS2wwS0tYandpSnRFa0lMT3AxQUN3bWhyNEwybnJEc0NCMTV5MHQ3czdFZk44WU55ekZyYmlNOVE?oc=5>

### Caterpillar Inc. stock outperforms competitors on strong trading day
- Summary: CAT shares rise, outperforming peers amid robust trading activity.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxPYWN0MDZsWkZqUmZCQ29GWEI3MHZjbHJfR3VJX01icWNfaWdrZWUxc3dSNEdKZHNhdDdRWnVIR1R4bm5zS1dTYmNhdUtyYi1WR1VTQVI4ODdHeGNJSTRfcy1ORGtHN2dwYVF1Ny11Wk5YUTRieUFfZFNsRmJISWQ5elZvamRWN2hCUDdocDdWUDg0Q0d0MFVwYkpRc0ZyZEYydDdELThmZlpqY0VVcjdfcFBBR0syLXF1T1F4cFlmNjVGTEUzdVl5cmJFa2Z4OW94aXJfWHM5QjBJMDcxcVE?oc=5>

## HEADWINDS

### Caterpillar Inc (CAT) Stock Down 4.9% but Still Overvalued -- GF Score: 90/100
- Summary: Caterpillar Inc (CAT) Stock Down 4.9% but Still Overvalued -- GF Score: 90/100
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNMlo2YVcxejRBY1FnRU15Z1o3V1MzenRjUGRpVlpNTmFNLWxfemVtRmcyNUIxcUlndmhYUXFwb2lta0R4eVlvNzN6UVN6UFkwT0Iyel8tNm15RFpsSHFrZHZkUlR3b292YW5XV25xay1ubF80NFpycmxfcUJ2ZzlLU3ViV1NRemgtdXlsalF1dUNabGd5dmczM1EzT2hCbmtTb0JvQmpBQm5SS1FU?oc=5>

### What Has The Market Missed In Caterpillar Stock’s Drop?
- Summary: Highlights factors contributing to recent stock decline.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQeWhwRUFFUFRFc2FKa0pxNjVpbEo3YmFBSURSd0wwV2pnV2JUYllHQ1NEelhVM21MQ0o5MW5xNmNQRHlSZ1cxYTVwaWw1ejBJZUpMVTVRZURCYjBsZW9adjl0M1FDdXNJTmhpX3JFV3BBYlFZS1l6M3Y5ek1lb3ViZ3BEUkJOYzNEbGUtSWlxbWJoRHM2U1hsUVR5a1pLc1dUSHMzcTNfU3AyQThtOHRiVzBSbw?oc=5>

### How Big Could Caterpillar Stock’s Next Fall Be?
- Summary: Speculates on potential magnitude of future decline.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQellmZ1ZFejhCWHFzUmEtUjlUZTRjZWRxaklWblhWYldqbGlYLTlJV0ROd2w2Nm1YaXU2clp6WjNob25iRmE4dG5PX2U4WlhtTm9vN2lDQkpuOV92R1NuUERlY0U5Y2pBeUFVbHdyTzh6bEJwbEdGeEFiY1RYVldPS09NTVppSjcwek9Ja1QwVmRWWmZRSnpsR2FCUTFaVU9lUjJCS25nNFk?oc=5>

## CATALYSTS

### Caterpillar (CAT) Q3 Earnings Preview: What You Should Know Beyond the Headline Estimates
- Summary: Caterpillar (CAT) Q3 Earnings Preview: What You Should Know Beyond the Headline Estimates
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNUnN0U2NDdGs2MjQwVGduaVZLcWxsT0RJbUpxRHppV2pZVHA0a3FxTmxET1ZQUEpVRkxNY2lfMC1oWVBGYUU5XzJwSGsxZDFBdFJqclFlWjlsdzNXZlg1WjlhLTc4Z05nQ21vRFhkRC1Cek1oSzJ6T1B3a0gwODdqeVpCYzdVcXphX0JOLVRFYVNHX3VXVFBLS25rNVEwcWR3WXc?oc=5>

### Caterpillar (CAT) Reports Next Week: Wall Street Expects Earnings Growth
- Summary: Caterpillar (CAT) Reports Next Week: Wall Street Expects Earnings Growth
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNTWROdHc0S3hGTEFFUmswNDVGMUxadkZ2ZU4yT0tCSXhQU0Z6anc5dkpySWlnbkJPeVVLUlpUUkVlTzVUS2REdFZiTWNTZ0lLSVd3MGFMVGlmZXlManduVzdOUm9BTHZEQmlKaVlma0FLTnNWZUNRU1FjVjJhWTVNZklPVjJTRXZMUlVReFVSNkJGZXAzd1V5M054ZnNxclk?oc=5>

### Caterpillar (CAT) CFO acquires 13 and 8 stock-linked units, payable in cash at retirement or separation.
- Summary: Caterpillar (CAT) CFO acquires 13 and 8 stock-linked units, payable in cash at retirement or separation.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxObm5WV1hRek1BajVPMzVHUFJCRURJQXpQVE9XVTMwZFpUUFNHWkJONllQVkM4WjlIMXdfLVhFNTlfZWV2WHBfYTdCOFB1dnpDZmNyNFBNZzFTNy1VU21TSkU2NW5UUlhuamN1TENxSVd6UXV0UXhCOGNKbUY3SDk4TzgxQkJlbkRsWkJCQ2tWQ1ZxczJ1RXIyM0pmU212Vnp5dVF3bm9YcmN1R3NO?oc=5>

### Caterpillar (CAT) executive acquires 13 stock-linked units, settled fully in cash at retirement or separation.
- Summary: Caterpillar (CAT) executive acquires 13 stock-linked units, settled fully in cash at retirement or separation.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQY3hSR2FOMlBBVUhDd205d2lXa3ZiMmZTX1FoZ2g2RklGRDRjY2Z3c1lsSlRpdldDMDY0WjRPYXQ1T3hmYTlhcThWV1lBWXIxeEc0ckVRTzNXZ1VOTy1pVkV6NXhuSk1UaHA0SW9EV1BCVUx0YXpqMlVpdmpkREdwSkoyYXJ1cGl5LWQ3NmZsTWZXeUZMT0xiSzhwaEJYd0pPNHZEQmxDU1pZU0tF?oc=5>

### Caterpillar Set to Report Q3 Earnings: Buy, Sell or Hold the Stock?
- Summary: Caterpillar will announce Q3 earnings, potentially influencing stock valuation.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQMUFqOFpQTDhPdlFBajh6SDRjQkdiSERCTnhyeEc1LXo4a3BMV3hjaXFtcGtZS01iQVR5YkM3UkZkS2stcjU4ZGh3T1dpdk1wZVFValBuWU44cThnLVFQclQ4VWFrb0d1UGZzbUlBclVRc3djd1A2NjlJaXNlRXhJNzRjaG51aTBrVXNXajdMeDFkWkhjUzdLQmF0cU44QzNF?oc=5>

### What to Expect From Caterpillar's Next Quarterly Earnings Report
- Summary: Upcoming earnings report may reveal financial performance.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPWTEtdUxJUVJINzRwV05aLXduNWxRdjF3ejl2SXdSQkVsM3RqSWZCeEgwZjdkaGpBb3pRX0x5MzF2eU15Y2laTjdwb093bGhINjZHOG9vdTlVMV9pdUtIQkpTS0hNRHZIdXZZVzRfSDRQTlFaTjE1ejVkVFZCUUhKU0NaWW9OUUFMS09VU0xOTXVMUFRyRHM1TUhkaURwZDJqWjNFbk1tdWZtVjd2?oc=5>

### Will Caterpillar (CAT) Beat Estimates Again in Its Next Earnings Report?
- Summary: Upcoming earnings report may confirm earnings beat expectations.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNdFZSODYwSGZHTTZTaUprVElfRTRzZDJ0dFpfUzluYkl0U1c0WG9HTnk4dWRuSm1OR1FyaXNPd3RvRVJPVGRNNjA0bHlvT3R5MXdpaXhjY2xjemRkOGp3VTNmeng3NXVURG9ldVBTbHN1ZEZQbmI1LWNnV2lQVlc0aFJFZnZvWGk3elZFV1k5TUJZU2VNYVo5NlM3UURQam5kZXFB?oc=5>

### Caterpillar (CAT) CEO gets 23 stock-linked units, payable in cash on retirement or separation from service.
- Summary: CEO receives 23 stock-linked units, payable in cash upon retirement or separation.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPRVlzaXdobjFYVzdyS2ZlQnpnN0hmOEZEU2syc0dXVlRncG9rVUFrLUJtbDhyUlpROW9Tbk4tdUl6dk5uNmJxV3JLWTVRcGc1QVgwMWEzNkR5Qlc4M3oyZUl5cXRKQnJoS19fa05MWl9xRkljNkRpZTdPTU56bHVncWZWajZfQnlDMXNxMmx0dmpaeXhrWlBfLW5sSGg2Y2UyVG1GcWYwMWVZaUtD?oc=5>

### Form 4 Caterpillar: Kyle Joseph Epley (CFO) For: 26 October By Investing.com
- Summary: CFO Kyle Epley files Form 4, reporting insider transaction.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPTDQ5RWstMkxmX0NZMmRScmpWU2Y3VHgyS3B0VmpqZkNGcW90dVpLZGQ2QnNuTWpkZUVhbFVySzFMclZ5RnozTEx3aFVMNUx6ang2N09oQVhFVGIwa0hkMDE4ek9YWUJnSUZtUU9lSHNhaVllX1ZxZUFzNTIydzFFYmcyVmtPMjZTTV9ZQ3M4aXJnMmljeHBxYzlCS3JQcTlpekxQSGxCaVh6Ti1ULTlCOVpvbnlNck0?oc=5>

## RISKS

### Caterpillar Inc Stock (CAT) Moved Down by 3.96% on Oct 22: What Investors Need To Know
- Summary: CAT shares fell 3.96% on Oct 22, reflecting a short‑term market decline.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNUUNnamh6SDVQY0xFTG95UHpNYUw5YlMyRFltQk5kazJ5emRJLUpELUhCdDFWdTQ2VU1DaUV2UzRzMjc0SVUzd2RrVzktdXo1MXNfSUtCSXhKNzZXMl8wR1pGMmVBOHNGRXR0S3hZRmV0RHZvakRWbkxCaWNhNFVhR0hCcWVJNmxpQ3c?oc=5>

### Caterpillar Stocks Move Higher Before Data-Center Backlog Test
- Summary: Stock rises ahead of backlog test, potential volatility.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQdUtqNHNZRXAxNkNDZDlpOFZESXFJbUdnbmQ2bTRvQzEzZXR0Ui1qQXJGMUFpYzJpQ2pxV21FeGJDRV9SemlxOFhidUlTby1xVERqLWJGSndzejRZMFhIa3dvWkVWSXFoeE1SRzBKdmtHSUZ5TWJFeXJXQTVqZFRXUzFJbmhtV3hYV3lObkVfTi1SX3NaOTRqUm9fa0Fpbmo3NkE?oc=5>

### Can Caterpillar’s $72B Backlog Save Its Stock From a 10% Slump?
- Summary: Backlog of $72B may prevent a 10% stock decline, but uncertainty remains.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOLUh6NG9OMTl3Tkl1UFRBTy1SN2k0NFZPcGcyb2FSMGlCVXBVQVhwaGRMZk9vMlR1YTBFSzZXN3hSWmlYel92UDg4ODNCS0JPQzMwdzJrSTB4VmUtQ1B0ODFFU0MxbkFZTG1CeGsyTE5XM3VXY1BRSkhVRlBtRTdmN1ZnbDZFb3FvRFJvaGR2ZnZaU2VWOGthaVFxaWV0YUlJLWVUWXl3?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CAT** | **30.71** | **16.91** | **22.59** | **24.00** | **327,890,698,240.00 USD** | **36.49** |
| DE | 35.55 | 6.16 | 26.76 | 4.90 | 172,447,023,104.00 USD | 35.30 |
| CNH | 44.56 | 1.78 | 36.80 | 2.00 | 17,914,888,192.00 USD | 3.86 |
| CMI | 27.11 | 5.69 | 15.63 | 9.40 | 73,046,147,072.00 USD | 27.86 |

Peers fetched as_of: 2026-10-27; CAT reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-10-29 (yfinance; expected dates may change)

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
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 20,543,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 1,141,000,000.00 USD; period 2011-07-01/2011-09-30; fiscal year/reporting period 2011/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/18230/000001823026000046/cat-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMirwFBVV95cUxOajNfSzNqdjBoOWRLc1dhb0ZHMGNwd0VURzI5UmJWc1dhbm9zMlQzMXo5bkZNMzdoNnpUdVUtNkt2OUNOX1lqMmt0RGlybmppdjQ0ellOUGY5UFl1MDJOalMwZy1RcWZYOXpVLWowM3dyWk1ZRjFpc0dyU2VlWDhPdTJhVkhpSTU0cGZHUEx1bWFiY0lKOTdDbVE3dllIcGljV2UwbEZ2SEVGNEN5cHNR?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQS195elp0TUR6MkxjdzRZTFRjd1VwZklHNUk0UDF4NXFzY0xWZlNEZnM0Y1dCUXpXSklhdmV4Qi1MLVpSTkEzT3Q1dGJyTW5yRHFZOXg3eU03clhYZjlFN1g3SlJtZUxHT0ZkZ3ZzZlRQOFhRU2NiTTZ2TmU2LWM1OEszSTdRWXQ0S2hsc1JyRXNCRmFjd1BwWm5PTU1TZFF0VFVxVQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPdXd6c1dXUXJFUkdfUEtBbXdMYlkwYkdZTlRSa1R6WDZ3S2dFZDhzYThnV1FVdHZubXZKb1F0RXNuWkgxOFpiaE9NVE04cmRCaU9va3RYR1k3NlJJYVJFc1h6RkFnZmpEZGZ0c2Rrb044UGRzUXlIYXR2YXE1OHEyb1V3dHNsRGVqaHo4dWx0QnlVVm5nbExoNjVDVGItUjA?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxOSmZzNDUxcFNFQ2FqcWcwWG9XQ1lkczFaX0JuNG9SZnU0LTlaTjN2ZXdJSjQ2TlUyeUpEc0F5NHNnem9HVEZRMDIxU3JMRHo3V2tkaHV3OTluTHlwZUtzOVoydGIzMXcyZW9JSUxLYl8tSWVKMjVMUFJZSmJoLUZISzJNa3lhRHVJeXBVTGhleTNVb3R5enpXNXFzS1dwMEs1cjJOaGs3LXptVkJsa2hiSkd1eHRIa2lzUS1XeG5MQi1FcGYwNTVQd1VDR3hHUQ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPbVpQbGFFa1diWWJIQmlhVGNWZ2F4d3kzUWVOakdpX3RuTUlOblVZZDNuX2RQNUNmcGpGSVlPeGhmUWxFbUprdnFOeWh5TWRTdGRlS2wwS0tYandpSnRFa0lMT3AxQUN3bWhyNEwybnJEc0NCMTV5MHQ3czdFZk44WU55ekZyYmlNOVE?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxPYWN0MDZsWkZqUmZCQ29GWEI3MHZjbHJfR3VJX01icWNfaWdrZWUxc3dSNEdKZHNhdDdRWnVIR1R4bm5zS1dTYmNhdUtyYi1WR1VTQVI4ODdHeGNJSTRfcy1ORGtHN2dwYVF1Ny11Wk5YUTRieUFfZFNsRmJISWQ5elZvamRWN2hCUDdocDdWUDg0Q0d0MFVwYkpRc0ZyZEYydDdELThmZlpqY0VVcjdfcFBBR0syLXF1T1F4cFlmNjVGTEUzdVl5cmJFa2Z4OW94aXJfWHM5QjBJMDcxcVE?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNMlo2YVcxejRBY1FnRU15Z1o3V1MzenRjUGRpVlpNTmFNLWxfemVtRmcyNUIxcUlndmhYUXFwb2lta0R4eVlvNzN6UVN6UFkwT0Iyel8tNm15RFpsSHFrZHZkUlR3b292YW5XV25xay1ubF80NFpycmxfcUJ2ZzlLU3ViV1NRemgtdXlsalF1dUNabGd5dmczM1EzT2hCbmtTb0JvQmpBQm5SS1FU?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQeWhwRUFFUFRFc2FKa0pxNjVpbEo3YmFBSURSd0wwV2pnV2JUYllHQ1NEelhVM21MQ0o5MW5xNmNQRHlSZ1cxYTVwaWw1ejBJZUpMVTVRZURCYjBsZW9adjl0M1FDdXNJTmhpX3JFV3BBYlFZS1l6M3Y5ek1lb3ViZ3BEUkJOYzNEbGUtSWlxbWJoRHM2U1hsUVR5a1pLc1dUSHMzcTNfU3AyQThtOHRiVzBSbw?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQellmZ1ZFejhCWHFzUmEtUjlUZTRjZWRxaklWblhWYldqbGlYLTlJV0ROd2w2Nm1YaXU2clp6WjNob25iRmE4dG5PX2U4WlhtTm9vN2lDQkpuOV92R1NuUERlY0U5Y2pBeUFVbHdyTzh6bEJwbEdGeEFiY1RYVldPS09NTVppSjcwek9Ja1QwVmRWWmZRSnpsR2FCUTFaVU9lUjJCS25nNFk?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNUnN0U2NDdGs2MjQwVGduaVZLcWxsT0RJbUpxRHppV2pZVHA0a3FxTmxET1ZQUEpVRkxNY2lfMC1oWVBGYUU5XzJwSGsxZDFBdFJqclFlWjlsdzNXZlg1WjlhLTc4Z05nQ21vRFhkRC1Cek1oSzJ6T1B3a0gwODdqeVpCYzdVcXphX0JOLVRFYVNHX3VXVFBLS25rNVEwcWR3WXc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNTWROdHc0S3hGTEFFUmswNDVGMUxadkZ2ZU4yT0tCSXhQU0Z6anc5dkpySWlnbkJPeVVLUlpUUkVlTzVUS2REdFZiTWNTZ0lLSVd3MGFMVGlmZXlManduVzdOUm9BTHZEQmlKaVlma0FLTnNWZUNRU1FjVjJhWTVNZklPVjJTRXZMUlVReFVSNkJGZXAzd1V5M054ZnNxclk?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxObm5WV1hRek1BajVPMzVHUFJCRURJQXpQVE9XVTMwZFpUUFNHWkJONllQVkM4WjlIMXdfLVhFNTlfZWV2WHBfYTdCOFB1dnpDZmNyNFBNZzFTNy1VU21TSkU2NW5UUlhuamN1TENxSVd6UXV0UXhCOGNKbUY3SDk4TzgxQkJlbkRsWkJCQ2tWQ1ZxczJ1RXIyM0pmU212Vnp5dVF3bm9YcmN1R3NO?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQY3hSR2FOMlBBVUhDd205d2lXa3ZiMmZTX1FoZ2g2RklGRDRjY2Z3c1lsSlRpdldDMDY0WjRPYXQ1T3hmYTlhcThWV1lBWXIxeEc0ckVRTzNXZ1VOTy1pVkV6NXhuSk1UaHA0SW9EV1BCVUx0YXpqMlVpdmpkREdwSkoyYXJ1cGl5LWQ3NmZsTWZXeUZMT0xiSzhwaEJYd0pPNHZEQmxDU1pZU0tF?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQMUFqOFpQTDhPdlFBajh6SDRjQkdiSERCTnhyeEc1LXo4a3BMV3hjaXFtcGtZS01iQVR5YkM3UkZkS2stcjU4ZGh3T1dpdk1wZVFValBuWU44cThnLVFQclQ4VWFrb0d1UGZzbUlBclVRc3djd1A2NjlJaXNlRXhJNzRjaG51aTBrVXNXajdMeDFkWkhjUzdLQmF0cU44QzNF?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPWTEtdUxJUVJINzRwV05aLXduNWxRdjF3ejl2SXdSQkVsM3RqSWZCeEgwZjdkaGpBb3pRX0x5MzF2eU15Y2laTjdwb093bGhINjZHOG9vdTlVMV9pdUtIQkpTS0hNRHZIdXZZVzRfSDRQTlFaTjE1ejVkVFZCUUhKU0NaWW9OUUFMS09VU0xOTXVMUFRyRHM1TUhkaURwZDJqWjNFbk1tdWZtVjd2?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNdFZSODYwSGZHTTZTaUprVElfRTRzZDJ0dFpfUzluYkl0U1c0WG9HTnk4dWRuSm1OR1FyaXNPd3RvRVJPVGRNNjA0bHlvT3R5MXdpaXhjY2xjemRkOGp3VTNmeng3NXVURG9ldVBTbHN1ZEZQbmI1LWNnV2lQVlc0aFJFZnZvWGk3elZFV1k5TUJZU2VNYVo5NlM3UURQam5kZXFB?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPRVlzaXdobjFYVzdyS2ZlQnpnN0hmOEZEU2syc0dXVlRncG9rVUFrLUJtbDhyUlpROW9Tbk4tdUl6dk5uNmJxV3JLWTVRcGc1QVgwMWEzNkR5Qlc4M3oyZUl5cXRKQnJoS19fa05MWl9xRkljNkRpZTdPTU56bHVncWZWajZfQnlDMXNxMmx0dmpaeXhrWlBfLW5sSGg2Y2UyVG1GcWYwMWVZaUtD?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPTDQ5RWstMkxmX0NZMmRScmpWU2Y3VHgyS3B0VmpqZkNGcW90dVpLZGQ2QnNuTWpkZUVhbFVySzFMclZ5RnozTEx3aFVMNUx6ang2N09oQVhFVGIwa0hkMDE4ek9YWUJnSUZtUU9lSHNhaVllX1ZxZUFzNTIydzFFYmcyVmtPMjZTTV9ZQ3M4aXJnMmljeHBxYzlCS3JQcTlpekxQSGxCaVh6Ti1ULTlCOVpvbnlNck0?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNUUNnamh6SDVQY0xFTG95UHpNYUw5YlMyRFltQk5kazJ5emRJLUpELUhCdDFWdTQ2VU1DaUV2UzRzMjc0SVUzd2RrVzktdXo1MXNfSUtCSXhKNzZXMl8wR1pGMmVBOHNGRXR0S3hZRmV0RHZvakRWbkxCaWNhNFVhR0hCcWVJNmxpQ3c?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQdUtqNHNZRXAxNkNDZDlpOFZESXFJbUdnbmQ2bTRvQzEzZXR0Ui1qQXJGMUFpYzJpQ2pxV21FeGJDRV9SemlxOFhidUlTby1xVERqLWJGSndzejRZMFhIa3dvWkVWSXFoeE1SRzBKdmtHSUZ5TWJFeXJXQTVqZFRXUzFJbmhtV3hYV3lObkVfTi1SX3NaOTRqUm9fa0Fpbmo3NkE?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOLUh6NG9OMTl3Tkl1UFRBTy1SN2k0NFZPcGcyb2FSMGlCVXBVQVhwaGRMZk9vMlR1YTBFSzZXN3hSWmlYel92UDg4ODNCS0JPQzMwdzJrSTB4VmUtQ1B0ODFFU0MxbkFZTG1CeGsyTE5XM3VXY1BRSkhVRlBtRTdmN1ZnbDZFb3FvRFJvaGR2ZnZaU2VWOGthaVFxaWV0YUlJLWVUWXl3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
