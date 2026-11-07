# DIS Intelligence Report

- ticker: **DIS**
- Report as_of: **2026-11-06**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/DIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/DIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-06**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-07T04:44:48.311364+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 15, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261106T045829Z-1db1e5a7/DIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 14 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 116.7500 |
| Return 1D (%) | -0.4010 |
| Return 1W (%) | 5.2371 |
| Return 1M (%) | 12.2272 |
| Return YTD (%) | 3.4056 |
| Return 1Y (%) | 7.1957 |
| Annualized volatility (%) | 27.3259 |
| Beta vs SPY | 0.6049 |
| Max drawdown (%) | -20.2451 |
| Sharpe (rf=0) | 0.3920 |
| Downside deviation (rf=0, %) | 19.2475 |
| Sortino (rf=0) | 0.5565 |
| Historical VaR 95% (1D, %) | 2.4075 |
| Historical ES 95% (1D, %) | 3.7715 |
| Correlation vs SPY | 0.3000 |
| Tracking error vs SPY (%) | 26.6115 |
| P/E (trailing) | 24.17 |
| P/B | 1.84 |
| EV/EBITDA | 11.89 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 15.58 |
| Gross margin (%) | 37.59 |
| Operating margin (%) | 19.30 |
| Return on equity (%) | 8.01 |
| Free cash flow yield (%) | 2.41 |
| MA50 | 108.0370 |
| Close vs MA50 (%) | 8.0648 |
| MA200 | 103.1286 |
| Close vs MA200 (%) | 13.2081 |
| RSI (14, Wilder) | 66.3674 |
| MACD (12,26) | 2.4980 |
| MACD signal (9) | 1.9313 |
| MACD histogram | 0.5668 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'DIS': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 116.7500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.4010 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.2371 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 12.2272 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 3.4056 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 7.1957 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 27.3259 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.2475 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5565 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4075 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.7715 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3000 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.6115 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6049 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2451 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3920 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.5754 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 37.5950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 19.3010 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.0100 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.4110 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 24.1718 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 66.3674 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.5668 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 8.0648 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 13.2081 -> Clearly above the moving-average trend level.

## TAILWINDS

### DIS Stock Ticks Higher Overnight: Disney Reportedly Weighs Thousands Of Job Cuts In Fresh Cost-Cutting Push Under Josh D’Amaro
- Summary: DIS Stock Ticks Higher Overnight: Disney Reportedly Weighs Thousands Of Job Cuts In Fresh Cost-Cutting Push Under Josh D’Amaro
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAJBVV95cUxQaWlHVGdFRHF1VGhjU0doMFhUbjlrbmEtSjhHekdzSUVsYVdJSVlRVV91bGhkbS1yRUtDX3lPanZ2V1ZUanRsUkJvRDdkYThxQ1dZakZWVTg1eXRvOFZGZ0ZCczBUd2JPQXluRlJGYlNCNEd4YlZTQi1kcVhyQlQwMnM5dFZnN2RVaUVlQ2NBZTRWblVtdEU4TjMwdmRnNkpyTm1DLTVoM3NGN2tIMjBaNnJKQ0doWkpaY1ZLbjFCZWVIY2ZqVGJIUHZ0blBuSng1Q3NES01xUTJ0YVNHRnBiSko4NmU3X05GaGtqTGdCdldDbzhGclhnV05YY2dYOXlkOHhqTUtGcjB2SGNicllYYk4wd3h3ZElo?oc=5>

### DIS Stock Analysis: Gains 1.96%, Testing Key Resistance
- Summary: DIS Stock Analysis: Gains 1.96%, Testing Key Resistance
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOYkwxSzlXVTBMLTJDUUtMSWhYRURhNXFsSXhfbkQ5bmotQmh4YjEwNTM1YXlueGQtUXFWMFRCMXN6TVhjTi1sSXMwSnZOWUh4R0I1eDBaeEtFbTFJV1MxZ1BaU2ZQRVhEMEEydTVrc1lidktrZ1VyMFQ1QVk0ZjhBRFdrb1M2QnZQdlpmdElRcDBWVHNTWmc?oc=5>

### Why Walt Disney (DIS) Outpaced the Stock Market Today
- Summary: Disney's stock outperformed the market, indicating strong investor confidence.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNeVFCRE1aZ21KUEViRGJxdkd6Ni1pY3pOTGV1RnBTRks0dEVGMVN4bWlSWUFLdHZJdzBJZ1ZucFdvTWVvUWgtSGJET2hhUFd1LXhRallxT1NaRlFXS2tCcVFveWNsNXAtU3kyOXVFd1k5Q3hRSG03WEt5ay1JLU5YUUlEanE0dlZjOWh4N25rZS12Wkc0NkUzZw?oc=5>

### Disney (DIS) Stock Looks Fairly Valued As Cash Flow Holds Up
- Summary: Disney’s valuation appears fair with stable cash flow, suggesting a positive outlook.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNUTNPQVVubVlnZVVCd0JScnZIWDFNdTZjRjV0dW1kbnZmYmFNUTFJM3laVWxFNEN4Xy1FT0YtOTFPRGY3X09Ea05JRTVDYk5ScF92anN3cl9zbG1sRWpwcV9nWjhGYl92bU50NDB6R3o4Vkx3TWlrejZDeWtLWU5oZWpkd2NBdGFHWjRnc2pWd1p6bV9TbnJsN2lR?oc=5>

### Disney Just Gained 9% in a Month: Take Profits, or Buy More?
- Summary: Disney's share price rose 9% over the month, reflecting positive market sentiment.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxOUWJyWmNramVOTllpM1RzVWduX0RWLUZ1dHRSQWViLUtPdzVoMzg4RXg3QTNGbnhpTXZfS0c0ZTNDUVVBWnQ0T3JPMXJhZ0VBZlRkZm1jQWs3U3NyQ1JtWXc5V0FZWmYwb3lUeDhZMWpkMGs2NUVCMjhlQWNMTExoaVFIWQ?oc=5>

### RSI Overbought, DIS Stock Gains 4.18% on Wednesday
- Summary: Technical indicator shows overbought condition, yet stock rose 4.18% today.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOQkk3dzlhbllDQXR0dzZ4LXoxb3hBakpfS2xIR3dCSXdZT0lEQnptUkU4SE5aMXlNZ05CVGhJcDlabDJWS1dpWGhCS3g5ODJwZTdsZzhLVmRwZmQzZ2ZrcUIyTDlLZjVKSXVVbDBuOTA0WjVVODB5VHBudmpKZExma0I2b3RaUk9oMHpPTkQtaTg?oc=5>

### Disney (DIS) Stock Looks Fairly Valued After Its 34% Rise
- Summary: Stock surged 34%, suggesting favorable valuation and investor sentiment.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNMTJCZWR1TUdoN3pVTEJ1MW1XZ1FDR0FtV3hxb2t6U3BQcFI3OGRlWkVSNXF3d1F0WFdoZy1xMUJKY29fQ09OUlh0VW9pOFdHcEdfN240R2F3VVV4ckdhSDlBV0hfcUw5T084TW1Bei1uS0NfV1RiNzYtR0NQdGVrSG9LOVpWdUNSbVhNM05JYlJRbVNjcW05QkFhZ2hLa0hIeEpWTUxJWFpmZVdZMkkxWjFmbHI1Nll6UnfSAb8BQVVfeXFMUF9yRGdYNTNpaElTbEo0NExoX3lwN3M4NFF4ZFNQN2ttbEF5V3NtMFZGQ0toOTBETkwtbS1UYXdCT2hTajRlRkVnN0hiMkF2YkZiZWNXNUt3MVEySkJzRzFIcDRESll5QTJONVNtNk9SV0g2T0tzWW9NQjF1eElxRWk1dVVkS0RNZWVGN1Z3bzI4bXp5R2tRMTBKU2x0OS1UOE5hY2tpb3dBcnoxWVNiSERDQWd2MzB1WmpTeTFja0E?oc=5>

## HEADWINDS

### DIS Stock Layoffs: What to Know as Disney Plans More Layoffs
- Summary: DIS Stock Layoffs: What to Know as Disney Plans More Layoffs
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNQnBnQ2dJT3M2X213aFBVSnpOQ3dWUlN2NWFXdTlCdjZiNERvM2lCSmFyRjJCSHFidkNRRHAtaFlvdjFxeTZTbkhXMl9NNDh3aUFiaUcyejlSby1oV18tZkdmVlU3dURTWGFrZ3N4N3hxSjloaWpyM2c0MWFvV0NYNTRfendCZ3FWYkcyQmJjanhzUE5VdG5FU19xRm4zTzlTSWhGZjdB?oc=5>

### Walt Disney (DIS) Starts Major Layoffs Across Multiple Departments
- Summary: Walt Disney (DIS) Starts Major Layoffs Across Multiple Departments
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOYWRzVjJKandmQnVqemdHUUdZdDFuR2JIbVJlUEt4Y1lydGlMNzYxNTl0WWZpd0ZRQXJOdGt1bFJ1Z0NydXZTVVB3Q09rQU0tSUFfSFI1eTJpMndnSkdibGlxbUdQSVhsTXBjbWRpeG5JeWpqZ3NtLWtaN2VTbklhRlNLQjF0bUhxdldxTVRvMVU5dGloRXpFVA?oc=5>

### How to Play DIS Stock as Disney Eyes 20% Cost Cuts and Thousands of Layoffs
- Summary: Disney plans significant cost cuts and layoffs, indicating potential operational challenges.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNUVhqVHpqTlVYeFlSalNiY2t2cTE1R2FNWU5IRFotWjhDVms3dGk0R0o3ZDFWOVFYQ3RhcHpTc0FyTXRXM19ITUM0SjVEemUxSC1fTDdvaG13QmQzeXdOZDdKem5IeTJHU19NalVKRUhmRWZHNzJqNnZ2bWYzSWw0WjFyaktUNTJrUUk2aE1IOTV3U0YzUDFsTFQxTm5BamVVRWxJNG02Q0ticzdUSFBKemFqTHpsS3RmeXc?oc=5>

### Disney targets up to 20% in cost savings, including job cuts – report (DIS:NYSE)
- Summary: Disney plans cost cuts up to 20%, involving job reductions.
- Date: 2026-11-03 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOM1NkdXQ0aVp1RnYtSlQ4cmswbi11MzJqazIzaDdkeDFIWEM2cGVreTFMRDQ4TkxRZGFpSXBlcjRNbmYzS3NCcW85R0pDS3NMZW9jVzltLTl5NlU2cmFTQmJoMFpsREUzd2JOVk9ONnhyWkh6YTNtTWJ3SGh5MjdvbVM2UVlWbFIxRHNDWFFuZmhOQnh6NXpyNXVmRnJpSjBNeTZZSHh3?oc=5>

### Disney (DIS) Prepares Major Staff Cuts Amid Cost-Cutting Drive
- Summary: Disney plans significant staff reductions to cut costs, impacting operations and employee morale.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOWXpzdlFjOEN1QU9vaDYwNWVmWkJTMWJBVjJCTVlXM0lIMzE0ZGZ2NzFrV3dzTGNDbU5vNkZKRndHWjdtNE5IU0NfYXcxYl9TM0YwMjRkaG1aMzBzNnZBWkFDU3hJY0hUcEdjcUpnLWFrMmp3bF9wX1FfMTJFTDc1aXdIVG9iaHBBMFBJN1ZQT0tmMWY5MWdzZmw3YThBdVU?oc=5>

### Walt Disney (DIS) executive sells 20,552 shares at $120 under a written trading plan.
- Summary: Executive sale may signal insider concern, potentially dampening investor confidence.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPcHZRLWROd1A3NE02SUR0TXd2Wl9kT3pENjI2S255Nm5MRjNnSXVqNzI2ekhkZER4VTJOUktaS05qLW1uUFJrczAxTlMyR0tXWl90NnlONFNwR3o5cjBGcXdTVXkyRzhXeExKczJudjVRZVFIOVJ3dENySU45NXpnbFVjX1hqMW9GbHd3OGdySHNVakpiMmtRU3I2YmRiLTQtYy1TYzdYa05VLUk?oc=5>

### How Job Cuts At Disney Stock Has Changed Its Investment Story
- Summary: Job cuts indicate cost-cutting, raising concerns about operational health and future earnings.
- Date: 2026-11-03 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOUVpGNE5qck9jMmNNNUZEcXJ4Rmg3NDIzQWNvQ2lvbnZRb0JIbFRaY3pEZU9VdDYyYVhyakxWbEpoR2Nqdk1lN2NhRGlRZWx4ZzM0WTJfVkJHVmZQRDdKRmRtOHRUTHNyVjJHTDl6WlVuNDJ2czltX1NxUE94TFZ1dlkwUWRtRVVqYU9GUTJPSGVrVTEtMjBnclpn?oc=5>

## CATALYSTS

### Is Wall Street Bullish or Bearish on Walt Disney Stock?
- Summary: Market sentiment toward Disney stock is questioned.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPOGY5TVhmTGFlbzZYUXZpXzdpSTNmSXVhdFpid2dUbnMyV3JSQjh4cmtFbV9SdFBlOTAtVzZtWS1sdlV4dWNtUXZsUFNrMkNhdmFJU2dpakRua0xBZEN4emt0Yy0zN3FObnRTVW9xUlhOV3lDaW1ENWduc3dOMWpfajd6Q28tSUE3M0dLVTI5blhrazlZeDVGVVNhWnp3dw?oc=5>

### Disney Eyes Thousands of Layoffs, With Managers Asked to Cut 20%
- Summary: Disney seeks to reduce workforce by thousands, asking managers to cut 20% of staff.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxONy1ueVhiMS1RaHJGNUlaZGpPaFlxR3lhd0xBN0o5SFctdk1sVFpQZmN6dnVoa3ZlamhnM0RHbzBaQi0xZ0dIZTdidTZQS0Z5ZFpHN0xlRGJMdlJEQllFV2ZoSmFSVzg4a1NQNjE4ZVN2STF2UzZacWJxeTluN3ZDaUJpZHVBaE15MFhyWTE1SWxvakZvSXNuLVJyVU80ejR4anRsUXpyZnNLdw?oc=5>

### Disney Targets Thousands of Jobs in Fresh Cost-Cutting Blitz: Report
- Summary: Disney plans massive layoffs to cut costs, targeting thousands of jobs across the company.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQalFuV2FLS0xzQ3pQdjVtNE1qWXo4UUh6QUx5MkdqaDZXTjNaajN5ZC14WDRyOFFwVHZjSC1uSUhoODNiajRYeFItTGVzc2Q4UkliVTJHSkU2dEFMeENhZzNyMnRkdlNfWlVFVU00dzdJWjRvY0xJdDVSZl85ZHRIaGI5aVVhU0FocGIyb1gxMWtkclYtdG1LUjEwRVBUcmFSdXVXRl94RFl0QmJtdTl0TkZkWVRCQ1FnU1h3RWRXUVh0S0U?oc=5>

### Disney (DIS) and WWE Launch John Cena Classic Event at ESPN Comp
- Summary: Disney partners with WWE for a new event featuring John Cena.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQZkNOWmdYM0xPeFNhQ1FaVURLcGwzUFhOcmN1alFHdDFTNVNNWU1kV21wazYzTFk3SEVrZ3p0cnVwajVOZzJJZl8tRk5wcnN0OFY0VWZtTzRzSng0ZTFmczhneGFFbHE3TlJxUVpja0F5Z3N6VmM3TzFSZzFtbXNSTHk5Y0tsd09QRy1SaUZYZmE1SXd3RmRZdFNkOFd5NWhOU1MtSEZJSQ?oc=5>

### A new Disney-WWE mashup has John Cena and the new Avengers movie working in tandem (DIS:NYSE)
- Summary: Disney collaborates with WWE and Avengers for a joint promotion featuring John Cena.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNQzhET2J5Qm5WbjlETllEMzBudlFiYVNoUnF2SUl6YzlLbW9YQlBwNndLLTMxalE2bmxQeENPNkVEUUNncjB1WGtaM3NiQ082UnJoSXRpM2Ntc1ZpUWZPb3JhTEVHeW1NTms4amE0ZWtuSElPN1RPaTFUeWQwWlVUWG1oMEtLeEJib2VSN0d6d1Vjakw0NWNJQ1FmQWZmcThKOXNXMGxidVhSNlFRTHM1M1JuMDNwLV9MMnJFQQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **DIS** | **24.17** | **1.84** | **11.89** | **6.80** | **201,590,685,696.00 USD** | **7.20** |
| NFLX | 18.33 | 8.89 | 16.90 | 11.80 | 260,382,130,176.00 USD | -42.20 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| PSKY | N/A | 0.93 | 7.95 | 0.90 | 10,992,190,464.00 USD | N/A |

Peers fetched as_of: 2026-11-06; DIS reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-05
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

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
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 25,248,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,638,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1744489/000174448926000057/dis-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAJBVV95cUxQaWlHVGdFRHF1VGhjU0doMFhUbjlrbmEtSjhHekdzSUVsYVdJSVlRVV91bGhkbS1yRUtDX3lPanZ2V1ZUanRsUkJvRDdkYThxQ1dZakZWVTg1eXRvOFZGZ0ZCczBUd2JPQXluRlJGYlNCNEd4YlZTQi1kcVhyQlQwMnM5dFZnN2RVaUVlQ2NBZTRWblVtdEU4TjMwdmRnNkpyTm1DLTVoM3NGN2tIMjBaNnJKQ0doWkpaY1ZLbjFCZWVIY2ZqVGJIUHZ0blBuSng1Q3NES01xUTJ0YVNHRnBiSko4NmU3X05GaGtqTGdCdldDbzhGclhnV05YY2dYOXlkOHhqTUtGcjB2SGNicllYYk4wd3h3ZElo?oc=5
- https://news.google.com/rss/articles/CBMilAJBVV95cUxPaWY3UnlMcVRlWlRhQWxtdDhBTkg1RExvSkE4R0Z1T2xWVFVCWGlYamxKVnhWa0FVVUdua2RLWVdLbkRadjBWa3pOcXozNzdMUWhsTFprVHdDODBFaGY0OVlFNHVkdGtMT0xFQXlucENTeEw0LUQ0S3dVRTVsdzliV21aeTY2OXVoOGlIYWtLLVFzdy1JcHl1OG9VVDZReE9QZm00WjJ0MC1menJpaDNDVGM4djBYRlc5MnZMdDBBbENqNDctZ2xRT2lrOTNpd0ZYNFZNR2ZXbDRxY1BScm10X0RUb05FaF81VnhqTENGTjBxR1JTM3Vrc0RSRnBZeEVtdVlnRjZJZ05jMUthcGI1U3c4YTA?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOYkwxSzlXVTBMLTJDUUtMSWhYRURhNXFsSXhfbkQ5bmotQmh4YjEwNTM1YXlueGQtUXFWMFRCMXN6TVhjTi1sSXMwSnZOWUh4R0I1eDBaeEtFbTFJV1MxZ1BaU2ZQRVhEMEEydTVrc1lidktrZ1VyMFQ1QVk0ZjhBRFdrb1M2QnZQdlpmdElRcDBWVHNTWmc?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNeVFCRE1aZ21KUEViRGJxdkd6Ni1pY3pOTGV1RnBTRks0dEVGMVN4bWlSWUFLdHZJdzBJZ1ZucFdvTWVvUWgtSGJET2hhUFd1LXhRallxT1NaRlFXS2tCcVFveWNsNXAtU3kyOXVFd1k5Q3hRSG03WEt5ay1JLU5YUUlEanE0dlZjOWh4N25rZS12Wkc0NkUzZw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNUTNPQVVubVlnZVVCd0JScnZIWDFNdTZjRjV0dW1kbnZmYmFNUTFJM3laVWxFNEN4Xy1FT0YtOTFPRGY3X09Ea05JRTVDYk5ScF92anN3cl9zbG1sRWpwcV9nWjhGYl92bU50NDB6R3o4Vkx3TWlrejZDeWtLWU5oZWpkd2NBdGFHWjRnc2pWd1p6bV9TbnJsN2lR?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxOUWJyWmNramVOTllpM1RzVWduX0RWLUZ1dHRSQWViLUtPdzVoMzg4RXg3QTNGbnhpTXZfS0c0ZTNDUVVBWnQ0T3JPMXJhZ0VBZlRkZm1jQWs3U3NyQ1JtWXc5V0FZWmYwb3lUeDhZMWpkMGs2NUVCMjhlQWNMTExoaVFIWQ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOQkk3dzlhbllDQXR0dzZ4LXoxb3hBakpfS2xIR3dCSXdZT0lEQnptUkU4SE5aMXlNZ05CVGhJcDlabDJWS1dpWGhCS3g5ODJwZTdsZzhLVmRwZmQzZ2ZrcUIyTDlLZjVKSXVVbDBuOTA0WjVVODB5VHBudmpKZExma0I2b3RaUk9oMHpPTkQtaTg?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNMTJCZWR1TUdoN3pVTEJ1MW1XZ1FDR0FtV3hxb2t6U3BQcFI3OGRlWkVSNXF3d1F0WFdoZy1xMUJKY29fQ09OUlh0VW9pOFdHcEdfN240R2F3VVV4ckdhSDlBV0hfcUw5T084TW1Bei1uS0NfV1RiNzYtR0NQdGVrSG9LOVpWdUNSbVhNM05JYlJRbVNjcW05QkFhZ2hLa0hIeEpWTUxJWFpmZVdZMkkxWjFmbHI1Nll6UnfSAb8BQVVfeXFMUF9yRGdYNTNpaElTbEo0NExoX3lwN3M4NFF4ZFNQN2ttbEF5V3NtMFZGQ0toOTBETkwtbS1UYXdCT2hTajRlRkVnN0hiMkF2YkZiZWNXNUt3MVEySkJzRzFIcDRESll5QTJONVNtNk9SV0g2T0tzWW9NQjF1eElxRWk1dVVkS0RNZWVGN1Z3bzI4bXp5R2tRMTBKU2x0OS1UOE5hY2tpb3dBcnoxWVNiSERDQWd2MzB1WmpTeTFja0E?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNQnBnQ2dJT3M2X213aFBVSnpOQ3dWUlN2NWFXdTlCdjZiNERvM2lCSmFyRjJCSHFidkNRRHAtaFlvdjFxeTZTbkhXMl9NNDh3aUFiaUcyejlSby1oV18tZkdmVlU3dURTWGFrZ3N4N3hxSjloaWpyM2c0MWFvV0NYNTRfendCZ3FWYkcyQmJjanhzUE5VdG5FU19xRm4zTzlTSWhGZjdB?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOYWRzVjJKandmQnVqemdHUUdZdDFuR2JIbVJlUEt4Y1lydGlMNzYxNTl0WWZpd0ZRQXJOdGt1bFJ1Z0NydXZTVVB3Q09rQU0tSUFfSFI1eTJpMndnSkdibGlxbUdQSVhsTXBjbWRpeG5JeWpqZ3NtLWtaN2VTbklhRlNLQjF0bUhxdldxTVRvMVU5dGloRXpFVA?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNUVhqVHpqTlVYeFlSalNiY2t2cTE1R2FNWU5IRFotWjhDVms3dGk0R0o3ZDFWOVFYQ3RhcHpTc0FyTXRXM19ITUM0SjVEemUxSC1fTDdvaG13QmQzeXdOZDdKem5IeTJHU19NalVKRUhmRWZHNzJqNnZ2bWYzSWw0WjFyaktUNTJrUUk2aE1IOTV3U0YzUDFsTFQxTm5BamVVRWxJNG02Q0ticzdUSFBKemFqTHpsS3RmeXc?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOM1NkdXQ0aVp1RnYtSlQ4cmswbi11MzJqazIzaDdkeDFIWEM2cGVreTFMRDQ4TkxRZGFpSXBlcjRNbmYzS3NCcW85R0pDS3NMZW9jVzltLTl5NlU2cmFTQmJoMFpsREUzd2JOVk9ONnhyWkh6YTNtTWJ3SGh5MjdvbVM2UVlWbFIxRHNDWFFuZmhOQnh6NXpyNXVmRnJpSjBNeTZZSHh3?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOWXpzdlFjOEN1QU9vaDYwNWVmWkJTMWJBVjJCTVlXM0lIMzE0ZGZ2NzFrV3dzTGNDbU5vNkZKRndHWjdtNE5IU0NfYXcxYl9TM0YwMjRkaG1aMzBzNnZBWkFDU3hJY0hUcEdjcUpnLWFrMmp3bF9wX1FfMTJFTDc1aXdIVG9iaHBBMFBJN1ZQT0tmMWY5MWdzZmw3YThBdVU?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPcHZRLWROd1A3NE02SUR0TXd2Wl9kT3pENjI2S255Nm5MRjNnSXVqNzI2ekhkZER4VTJOUktaS05qLW1uUFJrczAxTlMyR0tXWl90NnlONFNwR3o5cjBGcXdTVXkyRzhXeExKczJudjVRZVFIOVJ3dENySU45NXpnbFVjX1hqMW9GbHd3OGdySHNVakpiMmtRU3I2YmRiLTQtYy1TYzdYa05VLUk?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOUVpGNE5qck9jMmNNNUZEcXJ4Rmg3NDIzQWNvQ2lvbnZRb0JIbFRaY3pEZU9VdDYyYVhyakxWbEpoR2Nqdk1lN2NhRGlRZWx4ZzM0WTJfVkJHVmZQRDdKRmRtOHRUTHNyVjJHTDl6WlVuNDJ2czltX1NxUE94TFZ1dlkwUWRtRVVqYU9GUTJPSGVrVTEtMjBnclpn?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPOGY5TVhmTGFlbzZYUXZpXzdpSTNmSXVhdFpid2dUbnMyV3JSQjh4cmtFbV9SdFBlOTAtVzZtWS1sdlV4dWNtUXZsUFNrMkNhdmFJU2dpakRua0xBZEN4emt0Yy0zN3FObnRTVW9xUlhOV3lDaW1ENWduc3dOMWpfajd6Q28tSUE3M0dLVTI5blhrazlZeDVGVVNhWnp3dw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxONy1ueVhiMS1RaHJGNUlaZGpPaFlxR3lhd0xBN0o5SFctdk1sVFpQZmN6dnVoa3ZlamhnM0RHbzBaQi0xZ0dIZTdidTZQS0Z5ZFpHN0xlRGJMdlJEQllFV2ZoSmFSVzg4a1NQNjE4ZVN2STF2UzZacWJxeTluN3ZDaUJpZHVBaE15MFhyWTE1SWxvakZvSXNuLVJyVU80ejR4anRsUXpyZnNLdw?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQalFuV2FLS0xzQ3pQdjVtNE1qWXo4UUh6QUx5MkdqaDZXTjNaajN5ZC14WDRyOFFwVHZjSC1uSUhoODNiajRYeFItTGVzc2Q4UkliVTJHSkU2dEFMeENhZzNyMnRkdlNfWlVFVU00dzdJWjRvY0xJdDVSZl85ZHRIaGI5aVVhU0FocGIyb1gxMWtkclYtdG1LUjEwRVBUcmFSdXVXRl94RFl0QmJtdTl0TkZkWVRCQ1FnU1h3RWRXUVh0S0U?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQZkNOWmdYM0xPeFNhQ1FaVURLcGwzUFhOcmN1alFHdDFTNVNNWU1kV21wazYzTFk3SEVrZ3p0cnVwajVOZzJJZl8tRk5wcnN0OFY0VWZtTzRzSng0ZTFmczhneGFFbHE3TlJxUVpja0F5Z3N6VmM3TzFSZzFtbXNSTHk5Y0tsd09QRy1SaUZYZmE1SXd3RmRZdFNkOFd5NWhOU1MtSEZJSQ?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNQzhET2J5Qm5WbjlETllEMzBudlFiYVNoUnF2SUl6YzlLbW9YQlBwNndLLTMxalE2bmxQeENPNkVEUUNncjB1WGtaM3NiQ082UnJoSXRpM2Ntc1ZpUWZPb3JhTEVHeW1NTms4amE0ZWtuSElPN1RPaTFUeWQwWlVUWG1oMEtLeEJib2VSN0d6d1Vjakw0NWNJQ1FmQWZmcThKOXNXMGxidVhSNlFRTHM1M1JuMDNwLV9MMnJFQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
