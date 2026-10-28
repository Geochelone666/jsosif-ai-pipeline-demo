# SPGI Intelligence Report

- ticker: **SPGI**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/SPGI/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SPGI/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:09:53.400137+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 11, 'ai': 8, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/SPGI** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 448.9300 |
| Return 1D (%) | -0.3817 |
| Return 1W (%) | 2.4674 |
| Return 1M (%) | 11.3142 |
| Return YTD (%) | -8.5709 |
| Return 1Y (%) | -3.6044 |
| Annualized volatility (%) | 31.1253 |
| Beta vs SPY | 0.3177 |
| Max drawdown (%) | -28.4781 |
| Sharpe (rf=0) | 0.0388 |
| Downside deviation (rf=0, %) | 23.3481 |
| Sortino (rf=0) | 0.0517 |
| Historical VaR 95% (1D, %) | 2.9286 |
| Historical ES 95% (1D, %) | 4.7334 |
| Correlation vs SPY | 0.1296 |
| Tracking error vs SPY (%) | 32.0563 |
| P/E (trailing) | 27.32 |
| P/B | 4.20 |
| EV/EBITDA | 18.37 |
| Revenue growth (%) | 10.40 |
| Forward P/E (estimate) | 22.27 |
| Gross margin (%) | 70.90 |
| Operating margin (%) | 44.79 |
| Return on equity (%) | 14.26 |
| Free cash flow yield (%) | 4.12 |
| MA50 | 419.4154 |
| Close vs MA50 (%) | 7.0371 |
| MA200 | 416.5274 |
| Close vs MA200 (%) | 7.7792 |
| RSI (14, Wilder) | 70.1900 |
| MACD (12,26) | 11.0886 |
| MACD signal (9) | 6.2842 |
| MACD histogram | 4.8044 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SPGI': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 448.9300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.3817 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.4674 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 11.3142 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -8.5709 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -3.6044 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.1253 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.3481 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.0517 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9286 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.7334 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1296 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.0563 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3177 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.4781 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0388 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.2690 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 70.9030 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.7900 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 14.2550 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.1167 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.3238 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 70.1900 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 4.8044 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.0371 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 7.7792 -> Clearly above the moving-average trend level.

## TAILWINDS

### SPGI Stock Outlook Improves as S&P Global Raises 2026 Guidance
- Summary: SPGI Stock Outlook Improves as S&P Global Raises 2026 Guidance
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxONEZJNlgxVUhTazVVR3NHVTNfV0tKelhFSDlpNHluZGtpWmthMUtSNVBpVDIzMTBnNjF3Rm50ZzJidGlpQlZqcXRXOHBjQzZsUWZmNTNpVV9URFpiek1IaldPeGJBckJlU0Z5dG9JS1JUTnBSUnNFNkNNdzB0SjRKT2RnYkdjWF9fdG0weWtlV1poZ182Y0lZTWRKdXZKN1JIYy1z0gGoAUFVX3lxTE91UlpfZFIzNERRaWNtTGpOVnVMNWNfb3BHQVBwRGZpYzNlYkFBSjV1VUVaTlE5MGlDU1VTMkdEc0ZzTGZtaTVHTl9pOEF1anpDQUhHVkNmZWxTbG85YUsyQkxGUjhPTlZpMzRHc21XUzNiMTNZaS15VGZmdjBoelMxNzQ5UFJISk4xUXpMLW1OX25yOGxmS2lhWk9BSFBvSUozUTZpaXhTdg?oc=5>

### S&P Global (SPGI) Shares Rise After Q3 Beat and Strategic Review Announcement
- Summary: S&P Global (SPGI) Shares Rise After Q3 Beat and Strategic Review Announcement
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOUWlZcTU2dkNSNE1yNU9QY3lQVDBtajVPWmVJNEM4R04tcU1kN2hzaFNkaThfWnROU2NyVmdXUXBTYUhQY0NEeU1YelB3Z1lzLUYtWk1oSnJQdmFUY1Q1WFF6OEpyaHVMX1FVYjRjd3liaFRwVVNIUk53ejFGdmZUN291Q1d2WldyQmRaNW0xTjlBMXhlOVBzeGJ4Z0RQb3hnWlZYLU5NakRhSG8ySW92cDhwTQ?oc=5>

### S&P Global (SPGI) Shares Rise on Capital IQ Separation and Stron
- Summary: S&P Global (SPGI) Shares Rise on Capital IQ Separation and Stron
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPMFRqeG52eFN6elQyVlRSYll3SDFlTmhyWEtZSGhRREEteGFVR1hyQ3ZENTNSdXB1d193QlQzUlQ5ZGJEM1FmeUJRQ2Y2Ni1ITkdTVnBJb3FnWXAzaklEMUc3RHc0dzBiS1lzc0Q2THFramtDblN6WmZwWFdUU2xUYWZIR2tpNWljcVJvN1o1cFJ3d2toMm1GSlBsZ1J4azVuaGxDOWdYZVgzNE44UFNUWW5mRQ?oc=5>

### S&P Global (SPGI) Q3 Earnings Beat Estimates, Shares Trade Below GF Value™
- Summary: S&P Global (SPGI) Q3 Earnings Beat Estimates, Shares Trade Below GF Value™
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPVXZSSFpacl9EUlIzbUtISlN1WEJFbVZqOGhJNGtZOUNqYkJ4Z3ltRThXOXp6cU1vMXUzWDJ0XzQ0d0FVQkJqN2p6RmFWUzB1THdYdVNsQW5ZemNrNVctUUpnbFh3ajFOeDRxeFFwbFpyS2tUZFoyT0IweW8xQVRmVTgtcWp5X0kyR2N5Z3pPN1lxcGhCVWVrWmsxb2c5cE1GdjFyY1JuUmRINjBv?oc=5>

### Stay Ahead of the Game With S&P Global (SPGI) Q3 Earnings: Wall Street's Insights on Key Metrics
- Summary: Positive Q3 earnings outlook, strong metrics expected to boost investor confidence.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOWTJ1aXdZODRkZWRhUld5TUxlb0tfdGZleXczVmhLek1tXzEyV2duYnkwdjBCSDl1Q2JmRFljTnctNjZnNDBRRVQwaG91WER6aE5JZ3ZWNm1VR1RiaHg3blpFOHV0V2NaQmJMa1hPRWdhUUVOSHJSWUFkN1UzNmlxWkwtRjdsNF9WS2g2QUpVSVBRcHM?oc=5>

### S&P Global (SPGI) Stock Looks Fully Priced Despite Strong Excess Returns
- Summary: Stock appears fully priced, indicating market confidence.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNZkJOcnNoTVNDRElhOU9KUkcxOTYtbVFYY0JDTXNXbGpIaW9kRmt3SVo0OS1kdHpCdUNydGdUMUpQYTlMaFZpUkZVTE11WW96c2Z1UVZGOGgwT1FxTldCUmxFQW44UE93czlNTnY3dmhMSkprVlEyR3RCdDBwWk96QnBuVFBuaE91QXljODVDUWdhcEdW?oc=5>

### S&P Global (SPGI) Opens Its Indices To Regulated Prediction Markets
- Summary: Launch of regulated prediction markets for indices expands product offerings.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPUzloaXoyQjd1UHNwVnhrWlF5ZnNaTlhXQ0dUNTFxSjRmZWZGVHh6cG94VXNkWmx3Q0lUVzU2MTZvZGR0N1FqZUZjZVV4UFFZS1JvNk1MU0VYUjNMTk9JSzR3MzVYMVFQQVZNMnFTM2prMTZRa2xGdXlSWVh0b1ZHVDhzNGtFTTc3TklRVzZFQzVoMUQ0M09F?oc=5>

## HEADWINDS

### S&P Global (SPGI) Could Be 19% Overvalued Following Its Shelf Registration
- Summary: Market concerns over potential overvaluation may dampen investor enthusiasm.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxPYnRZODNnZ0F4NjA3b3RoYi1mRS1yTXdNM2VWVGFJM200QzB3bUZuRXl2V1V0TlNzb2xBUnBWUDlqX1JZQnZjUUJoTTNycnZBTFhKeG5WWTBlYlFRQ29JYkZFYjZ4blYyTUNiOFZBMjlZRThrZVlBRWJOSjlyMmgyR0UxeE0weWdRUU9lRnZSNEo?oc=5>

## CATALYSTS

### S&P Global confirms strategic review of Capital IQ, data businesses; Q3 earnings beat (SPGI:NYSE)
- Summary: S&P Global confirms strategic review of Capital IQ, data businesses; Q3 earnings beat (SPGI:NYSE)
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNZ2NVLUdkWW8yY0g0VmQzNlY5T0NDVjdGa2pqRnBWNllLUDBFVVNRUGxpd3c0X09ncThWVUF0Wk9ORUgyUTJzUjNHdnRCb0dvVE94VzJjd2NYYzBWX3kxWlRneVZoRUt2aUo0RkVoX2duNWlZdkRKd2tUOFVERU1EUHdWVnBPcDBraHB5aGRkRTd5TlRKTUYtdGVfWnRNZDdhcExPYk1VVHBiYmE4dHVZZWpNZGdaUWlPb2RtUA?oc=5>

### S&P Global (SPGI) Q3 Earnings and Revenues Surpass Estimates
- Summary: S&P Global (SPGI) Q3 Earnings and Revenues Surpass Estimates
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNYWZJa0ZHSEZ1RnJIWjFCa2ZLSXVEbUVlWVZkZGdMRHRUOEh4c193UXNWZ1l4WDBvQllhQXgzbmV0MnJ6QVpEWUFVT0ZCRUxZNkFhbG8wcHFoT1g1U0JhMEoyQVNBT0M3SzBSbS1rbTFodWpzZ3lzVU1udFRjdXY4WTlkbFE1ZmNmQ3hVb21MbC1iMlNp?oc=5>

### S&P Global (SPGI) Reports Q3 Earnings: What Key Metrics Have to Say
- Summary: S&P Global (SPGI) Reports Q3 Earnings: What Key Metrics Have to Say
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQRWRhQVJacHhlWjNRUUZIR2pUVTQwQTZDREI2MTJxWF8yUVhRR3hGZzJ2V0EwVFNnUHlFanZBeGdMYU50WHBubTJ3SVJIWS1zX0JEX2Z5SERFMzVnVWdWalVLa2h1TGZ6SHRjUHVCWWxrSW1jLTJHb1BZUmlpRnc5VHRDdEtsNS1rT29KeTIzaXRrbTQ?oc=5>

### S&P Global Inc. 2026 Q3 - Results - Earnings Call Presentation (NYSE:SPGI) 2026-10-27
- Summary: S&P Global Inc. 2026 Q3 - Results - Earnings Call Presentation (NYSE:SPGI) 2026-10-27
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNN1ozWGFyVmJMTlcxOGl3dk5yaHNFbUVxaVhrYUlsTEhreTBtT1ZhSm9ZOS1oOXNZcHhEUUJ5ZmM1a003UkNNaHBLTFhHdmtaYlVOZ04yZ0t3MUNrcVFPRGpoQTJrSGtBQ2NmSVFic3UwUWJvMTRmWkV4ZWsxLV9UUmF6am1QM1V6Q1lzUGJGUGVaazNNbFh4bllIMktWTkFlOVJpQQ?oc=5>

### S&P Global Beats Q3 Earnings on Indices & Market Intelligence
- Summary: S&P Global Beats Q3 Earnings on Indices & Market Intelligence
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOdkROeDIyNk43UWFISDF0WkxIbTJ4WTg1N2J1U0EwMC1uUzFldkFQWDJ6Qi1tMWlJaTgtNm5udWk3dElKempXeTNXR2dxbEM5WTdlRVRBaWxYeU9KOTlmOWNwVmxYZGtFMDdEbll3Yk9PRUdQNmFyZC1RUlhrMGRxTWxIZl9VYzliTU1NMXRiYnE1VVBrRWR0d1IydHZtYzVfcF9yWkRSTTNWTGxpZU43d1oxWFBtUQ?oc=5>

### S&P Global Earnings Ahead: What Past Reactions Say About The Stock
- Summary: S&P Global Earnings Ahead: What Past Reactions Say About The Stock
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQNi1yS3VXakYtLWJLMm1FcUFYV0ZHM3NNZV9wbjJnN2xqLS1rRmhYVUtMTElicmpGSHh1cUpDN2RxRnVtdVpaTFhmdXhod0tmMUwzODFLOHlVWWxWbmtQb1duNnB1WndVbFlDaWFFSEJOTlNRUkNvSS1EQ0N0RmhzdXJuZ3FRWVpZa2p4dUt1dEV1SC0wanJPTHE1U0NXOWFyRFJDNGM2NlQ5RF9Pd25md2NKRXVXdll3VlA4Y2ZfcnJtN3M?oc=5>

### S&P Global (SPGI) to report earnings tomorrow: here is what to expect
- Summary: S&P Global (SPGI) to report earnings tomorrow: here is what to expect
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNTUl6RjVKU296MUxyQld2b0pfZW9SMHk0RGZKSnJRVGRmTVpqU1FwZEpLaGhkckhmY3FaVlhxcWpTVlVBZnhrcksxOTdZTHc5QXA5dHlib1ZLRlU4bmg4MXpYV0NGR2Q0QlNUcm9mY0FpRHVjT1l6ZVlsQUZ1WFNiMHZBc1MyWUpCNUZrMnJHTjRXNjVwY29SVTZwR0NPWWR6SkxWM0N1VnpNcTlVY2ZzMEdCMHBQWDNVU2J0WnF5S19BWi1zQmc?oc=5>

### S&P Global starts review for Capital IQ and related data business
- Summary: Internal review of Capital IQ and related data business.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNUTlPSHg5RWh2UEZuY2lDSmF1Z0Z3UkVscm42OHFKRjRlZ21MemFjNVF1ZmNwaVVHVDgwTW9hd29kRHhLMGpKQU9sV0xubG5JdGs5SEdqTkJiWkJwN1QwWmlCZnFNTHJtc2dNNjVyN2k5LTVrX0c1NDdpUlVxZXNJQ1VzREt1SUsxTGd5MVhfV3o2TWlHbkFQVVBQT0NQcVQ4UEI5Y0pyaThEYTZDOWU4SUxkU2w1Wjl2R1l2aTdBTExNLWN5azhz?oc=5>

### S&P Global (NYSE:SPGI) Q3 2026 Results In Line With Consensus as Capital IQ Strategic Review Announced
- Summary: Results matched consensus; Capital IQ strategic review announced, signaling potential future changes.
- Date: 2026-10-27 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxQdGN1QXNDQ1JBeVpiUHVkQjNIczU4TTRkeFUyTVZRWkNSa1RzbDk0azB5WU9uSjE4QXNaVWwxWVlYZHA5RF8xQUZaYUxRTzNFNi1aSkxEd0p1cVpGUkVuU2tXTmQzLUp6QWIzWGlTY2xBa01PUXA2R3FoNFpwOW1leF93NktLeXoxSU9UWjYwUVF4eHBldkdWLXRVRldxR0RYVmFldG9UTGQzS1dkOU01bnozeUpVb0hnSERIcWJLRnpNdTFfa1FKQ3JEN0tYRS1lUTRMT09jLVAwT0hoQld6Q25kcmY?oc=5>

### S&P Global Evaluates Strategic Options for Capital IQ and Kensho Data (SPGI)
- Summary: Company is assessing strategic options for Capital IQ and Kensho Data, indicating possible restructuring.
- Date: 2026-10-27 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNRWNNdEpFWUo4Z0cwT3c0Qm8zNGVlMGpMRmpvSm1UdEFpS042R1UwZjBvSjIzNEh1cXhFQk5CTzEtYV9SUHFJelNNTHljTzREOVhRY3lsNnZ0T05qV282NXJSNGgzVWVtMUt6OFJVQi1NR21aVUl4Y28zQ1AyTzllWkFVRF9UR2hsUkpERDJqdjFYanFrRDdiQ2lrVFZYTkMwVEVzZlFrZUhNRXRUSzc3enR3?oc=5>

### S&P Global (NYSE:SPGI) exceeds Q3 2026 expectations
- Summary: S&P Global surpassed Q3 2026 earnings forecasts, indicating stronger-than-expected performance.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQZ3RobWhvN2ptWVAydEkxU0M2TS1YTUxrYXdHdXlsOVhBTlRvWURTYjVwbEJ6TFdCa3Y4S1dvRUFOOG55b214QXBaZDNabG1RcGZwcDBMV21ORkV3VXRLWmtBbFNOa010OEJXdmUwd3ZjaV9MMUVpNjdUSWhBSFlVeVU2NGc5clFLU1Btck9wa20tZzM0aG9tUDB0bFBlNHFfRE1JLW85UGVCRlRJOXhj?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SPGI** | **27.32** | **4.20** | **18.37** | **10.40** | **132,344,561,664.00 USD** | **-3.60** |
| MCO | 28.33 | 25.06 | 21.70 | 0.80 | 81,729,011,712.00 USD | -3.43 |
| MSCI | 31.02 | -14.38 | 24.60 | 12.40 | 43,747,225,600.00 USD | 11.62 |
| FDS | 21.25 | 5.45 | 13.54 | 6.30 | 10,917,436,416.00 USD | 8.53 |

Peers fetched as_of: 2026-10-27; SPGI reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: N/A (yfinance; expected dates may change)

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
- Filing date: 2026-07-28
- Revenue (latest available single quarter): 1,567,000,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/64040/000006404026000045/spgi-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiowFBVV95cUxONEZJNlgxVUhTazVVR3NHVTNfV0tKelhFSDlpNHluZGtpWmthMUtSNVBpVDIzMTBnNjF3Rm50ZzJidGlpQlZqcXRXOHBjQzZsUWZmNTNpVV9URFpiek1IaldPeGJBckJlU0Z5dG9JS1JUTnBSUnNFNkNNdzB0SjRKT2RnYkdjWF9fdG0weWtlV1poZ182Y0lZTWRKdXZKN1JIYy1z0gGoAUFVX3lxTE91UlpfZFIzNERRaWNtTGpOVnVMNWNfb3BHQVBwRGZpYzNlYkFBSjV1VUVaTlE5MGlDU1VTMkdEc0ZzTGZtaTVHTl9pOEF1anpDQUhHVkNmZWxTbG85YUsyQkxGUjhPTlZpMzRHc21XUzNiMTNZaS15VGZmdjBoelMxNzQ5UFJISk4xUXpMLW1OX25yOGxmS2lhWk9BSFBvSUozUTZpaXhTdg?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOUWlZcTU2dkNSNE1yNU9QY3lQVDBtajVPWmVJNEM4R04tcU1kN2hzaFNkaThfWnROU2NyVmdXUXBTYUhQY0NEeU1YelB3Z1lzLUYtWk1oSnJQdmFUY1Q1WFF6OEpyaHVMX1FVYjRjd3liaFRwVVNIUk53ejFGdmZUN291Q1d2WldyQmRaNW0xTjlBMXhlOVBzeGJ4Z0RQb3hnWlZYLU5NakRhSG8ySW92cDhwTQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPMFRqeG52eFN6elQyVlRSYll3SDFlTmhyWEtZSGhRREEteGFVR1hyQ3ZENTNSdXB1d193QlQzUlQ5ZGJEM1FmeUJRQ2Y2Ni1ITkdTVnBJb3FnWXAzaklEMUc3RHc0dzBiS1lzc0Q2THFramtDblN6WmZwWFdUU2xUYWZIR2tpNWljcVJvN1o1cFJ3d2toMm1GSlBsZ1J4azVuaGxDOWdYZVgzNE44UFNUWW5mRQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPVXZSSFpacl9EUlIzbUtISlN1WEJFbVZqOGhJNGtZOUNqYkJ4Z3ltRThXOXp6cU1vMXUzWDJ0XzQ0d0FVQkJqN2p6RmFWUzB1THdYdVNsQW5ZemNrNVctUUpnbFh3ajFOeDRxeFFwbFpyS2tUZFoyT0IweW8xQVRmVTgtcWp5X0kyR2N5Z3pPN1lxcGhCVWVrWmsxb2c5cE1GdjFyY1JuUmRINjBv?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOWTJ1aXdZODRkZWRhUld5TUxlb0tfdGZleXczVmhLek1tXzEyV2duYnkwdjBCSDl1Q2JmRFljTnctNjZnNDBRRVQwaG91WER6aE5JZ3ZWNm1VR1RiaHg3blpFOHV0V2NaQmJMa1hPRWdhUUVOSHJSWUFkN1UzNmlxWkwtRjdsNF9WS2g2QUpVSVBRcHM?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNZkJOcnNoTVNDRElhOU9KUkcxOTYtbVFYY0JDTXNXbGpIaW9kRmt3SVo0OS1kdHpCdUNydGdUMUpQYTlMaFZpUkZVTE11WW96c2Z1UVZGOGgwT1FxTldCUmxFQW44UE93czlNTnY3dmhMSkprVlEyR3RCdDBwWk96QnBuVFBuaE91QXljODVDUWdhcEdW?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPUzloaXoyQjd1UHNwVnhrWlF5ZnNaTlhXQ0dUNTFxSjRmZWZGVHh6cG94VXNkWmx3Q0lUVzU2MTZvZGR0N1FqZUZjZVV4UFFZS1JvNk1MU0VYUjNMTk9JSzR3MzVYMVFQQVZNMnFTM2prMTZRa2xGdXlSWVh0b1ZHVDhzNGtFTTc3TklRVzZFQzVoMUQ0M09F?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPYnRZODNnZ0F4NjA3b3RoYi1mRS1yTXdNM2VWVGFJM200QzB3bUZuRXl2V1V0TlNzb2xBUnBWUDlqX1JZQnZjUUJoTTNycnZBTFhKeG5WWTBlYlFRQ29JYkZFYjZ4blYyTUNiOFZBMjlZRThrZVlBRWJOSjlyMmgyR0UxeE0weWdRUU9lRnZSNEo?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNZ2NVLUdkWW8yY0g0VmQzNlY5T0NDVjdGa2pqRnBWNllLUDBFVVNRUGxpd3c0X09ncThWVUF0Wk9ORUgyUTJzUjNHdnRCb0dvVE94VzJjd2NYYzBWX3kxWlRneVZoRUt2aUo0RkVoX2duNWlZdkRKd2tUOFVERU1EUHdWVnBPcDBraHB5aGRkRTd5TlRKTUYtdGVfWnRNZDdhcExPYk1VVHBiYmE4dHVZZWpNZGdaUWlPb2RtUA?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNYWZJa0ZHSEZ1RnJIWjFCa2ZLSXVEbUVlWVZkZGdMRHRUOEh4c193UXNWZ1l4WDBvQllhQXgzbmV0MnJ6QVpEWUFVT0ZCRUxZNkFhbG8wcHFoT1g1U0JhMEoyQVNBT0M3SzBSbS1rbTFodWpzZ3lzVU1udFRjdXY4WTlkbFE1ZmNmQ3hVb21MbC1iMlNp?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQRWRhQVJacHhlWjNRUUZIR2pUVTQwQTZDREI2MTJxWF8yUVhRR3hGZzJ2V0EwVFNnUHlFanZBeGdMYU50WHBubTJ3SVJIWS1zX0JEX2Z5SERFMzVnVWdWalVLa2h1TGZ6SHRjUHVCWWxrSW1jLTJHb1BZUmlpRnc5VHRDdEtsNS1rT29KeTIzaXRrbTQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNN1ozWGFyVmJMTlcxOGl3dk5yaHNFbUVxaVhrYUlsTEhreTBtT1ZhSm9ZOS1oOXNZcHhEUUJ5ZmM1a003UkNNaHBLTFhHdmtaYlVOZ04yZ0t3MUNrcVFPRGpoQTJrSGtBQ2NmSVFic3UwUWJvMTRmWkV4ZWsxLV9UUmF6am1QM1V6Q1lzUGJGUGVaazNNbFh4bllIMktWTkFlOVJpQQ?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOdkROeDIyNk43UWFISDF0WkxIbTJ4WTg1N2J1U0EwMC1uUzFldkFQWDJ6Qi1tMWlJaTgtNm5udWk3dElKempXeTNXR2dxbEM5WTdlRVRBaWxYeU9KOTlmOWNwVmxYZGtFMDdEbll3Yk9PRUdQNmFyZC1RUlhrMGRxTWxIZl9VYzliTU1NMXRiYnE1VVBrRWR0d1IydHZtYzVfcF9yWkRSTTNWTGxpZU43d1oxWFBtUQ?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQNi1yS3VXakYtLWJLMm1FcUFYV0ZHM3NNZV9wbjJnN2xqLS1rRmhYVUtMTElicmpGSHh1cUpDN2RxRnVtdVpaTFhmdXhod0tmMUwzODFLOHlVWWxWbmtQb1duNnB1WndVbFlDaWFFSEJOTlNRUkNvSS1EQ0N0RmhzdXJuZ3FRWVpZa2p4dUt1dEV1SC0wanJPTHE1U0NXOWFyRFJDNGM2NlQ5RF9Pd25md2NKRXVXdll3VlA4Y2ZfcnJtN3M?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNTUl6RjVKU296MUxyQld2b0pfZW9SMHk0RGZKSnJRVGRmTVpqU1FwZEpLaGhkckhmY3FaVlhxcWpTVlVBZnhrcksxOTdZTHc5QXA5dHlib1ZLRlU4bmg4MXpYV0NGR2Q0QlNUcm9mY0FpRHVjT1l6ZVlsQUZ1WFNiMHZBc1MyWUpCNUZrMnJHTjRXNjVwY29SVTZwR0NPWWR6SkxWM0N1VnpNcTlVY2ZzMEdCMHBQWDNVU2J0WnF5S19BWi1zQmc?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNUTlPSHg5RWh2UEZuY2lDSmF1Z0Z3UkVscm42OHFKRjRlZ21MemFjNVF1ZmNwaVVHVDgwTW9hd29kRHhLMGpKQU9sV0xubG5JdGs5SEdqTkJiWkJwN1QwWmlCZnFNTHJtc2dNNjVyN2k5LTVrX0c1NDdpUlVxZXNJQ1VzREt1SUsxTGd5MVhfV3o2TWlHbkFQVVBQT0NQcVQ4UEI5Y0pyaThEYTZDOWU4SUxkU2w1Wjl2R1l2aTdBTExNLWN5azhz?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxQdGN1QXNDQ1JBeVpiUHVkQjNIczU4TTRkeFUyTVZRWkNSa1RzbDk0azB5WU9uSjE4QXNaVWwxWVlYZHA5RF8xQUZaYUxRTzNFNi1aSkxEd0p1cVpGUkVuU2tXTmQzLUp6QWIzWGlTY2xBa01PUXA2R3FoNFpwOW1leF93NktLeXoxSU9UWjYwUVF4eHBldkdWLXRVRldxR0RYVmFldG9UTGQzS1dkOU01bnozeUpVb0hnSERIcWJLRnpNdTFfa1FKQ3JEN0tYRS1lUTRMT09jLVAwT0hoQld6Q25kcmY?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNRWNNdEpFWUo4Z0cwT3c0Qm8zNGVlMGpMRmpvSm1UdEFpS042R1UwZjBvSjIzNEh1cXhFQk5CTzEtYV9SUHFJelNNTHljTzREOVhRY3lsNnZ0T05qV282NXJSNGgzVWVtMUt6OFJVQi1NR21aVUl4Y28zQ1AyTzllWkFVRF9UR2hsUkpERDJqdjFYanFrRDdiQ2lrVFZYTkMwVEVzZlFrZUhNRXRUSzc3enR3?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQZ3RobWhvN2ptWVAydEkxU0M2TS1YTUxrYXdHdXlsOVhBTlRvWURTYjVwbEJ6TFdCa3Y4S1dvRUFOOG55b214QXBaZDNabG1RcGZwcDBMV21ORkV3VXRLWmtBbFNOa010OEJXdmUwd3ZjaV9MMUVpNjdUSWhBSFlVeVU2NGc5clFLU1Btck9wa20tZzM0aG9tUDB0bFBlNHFfRE1JLW85UGVCRlRJOXhj?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
