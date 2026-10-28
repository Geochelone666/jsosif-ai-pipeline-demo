# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:08:11.753464+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 12, 'ai': 9, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 8 named publishers; 4 exact duplicates; 21 HTTPS source links; largest publisher share 52.38%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 133.5000 |
| Return 1D (%) | -1.4469 |
| Return 1W (%) | -0.3880 |
| Return 1M (%) | 3.7860 |
| Return YTD (%) | -4.1500 |
| Return 1Y (%) | -8.9895 |
| Annualized volatility (%) | 21.2065 |
| Beta vs SPY | -0.2210 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | -0.3405 |
| Downside deviation (rf=0, %) | 14.5903 |
| Sortino (rf=0) | -0.4949 |
| Historical VaR 95% (1D, %) | 2.1996 |
| Historical ES 95% (1D, %) | 2.6716 |
| Correlation vs SPY | -0.1324 |
| Tracking error vs SPY (%) | 26.1217 |
| P/E (trailing) | 16.79 |
| P/B | 8.17 |
| EV/EBITDA | 11.62 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 15.45 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.88 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.97 |
| MA50 | 133.5253 |
| Close vs MA50 (%) | -0.0189 |
| MA200 | 143.7808 |
| Close vs MA200 (%) | -7.1503 |
| RSI (14, Wilder) | 53.7288 |
| MACD (12,26) | 1.0359 |
| MACD signal (9) | 0.0039 |
| MACD histogram | 1.0320 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 133.5000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.4469 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.3880 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.7860 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -4.1500 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -8.9895 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.2065 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.5903 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.4949 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1996 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6716 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1324 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.1217 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.2210 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.3405 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.4537 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.8830 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.9714 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.7925 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.7288 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.0320 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.0189 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -7.1503 -> Clearly below the moving-average trend level.

## TAILWINDS

### PEP Stock Gains After PepsiCo Locks In 11 More Years With Taco Bell Following KFC Loss To Coke
- Summary: PEP Stock Gains After PepsiCo Locks In 11 More Years With Taco Bell Following KFC Loss To Coke
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8AFBVV95cUxNa0lEZnJIcmhtS2Fkb0JmZFJrLWcxMG9vM1FncVBPX3QtNUJoMWdmb2VGN3ptcm0yQkZYbTc0cGJBQW1SUEg5VDd0RkZzZDVqRmVhMU5hdzM5djN2Vko3ZGo5anlqWGxsTHhzbC1mZm54eVhRWDUwY3Uwdnc1cVllMUJsZDk5Z3F4dm1NcUYwc040MkhOOG1NYW1RdGF4d1VhblBWekR2Ukdnd19jbWM2WVIxNEstQ25qMUU0bmRlbDJRdnBxTlcybWFBWEhDdE1WbDFVbk93YTlTN3k3aWgzRGwxaWxJcnVsOE1xM1lGdzQ?oc=5>

### PepsiCo Inc (PEP) Stock Up 3.1% and Still Undervalued -- GF Scor
- Summary: PepsiCo Inc (PEP) Stock Up 3.1% and Still Undervalued -- GF Scor
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNSU9USEEzOTVhWVhlbm8xelBIOGVRd2tFNmxGRTQ0THdiLVE1MXZLa2xwdDBDTzVwOVVnckN2cEhmOTZESFViUmNER2xCY2h2VUtNUzJKUHhjaFFtMUphQU92UXJmTDZpd3lxbi02Nk1rUTNodmF2NUlRbi13SFhtR1lrNFN2blpkNkg2OGhwVUh5T256enpIdnNfNXQ1NnVXaDhVUHhB?oc=5>

### PepsiCo Stock Could Be a Contrarian Opportunity if This One Thing Improves
- Summary: Analysis suggests PepsiCo stock may rise if a specific metric improves, highlighting potential upside.
- Date: 2026-10-22 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPTnhBV0FrN01aYkVUb3FYekwyZTVDTW1tSkpqd2F1ZzJPSTRBbERlWkZmZmtyNzJKSnM5OWJjQU1mZ2tMUWVSV1FkTWtSUDktT3NYTG9qSGRyNkhTQkFDdHVBMU9vV3l5Y1EySnBrblYzU0llYVlVdUFXYWRLRHo2T2ZlVWIwcjQxd0JPOENhZTc3Z2dPdEdCbnRraUhkRWRqZ3BLb0QzanBVTXpmdUw4Q2FjZ2VaOWh2TlE?oc=5>

### Unusual Options Volume Report: PepsiCo Stock
- Summary: Reports of higher-than-normal options trading activity for PepsiCo, indicating increased market interest.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPOUF0bmJkQ1VJZXZkeG5WRk9YUWllcDh1NERKc1JXTEZ0VG1RVkFmR21XN01KRGh5aTNKbjRJWnNqaVc0UndnbzNSZDR1M3ZQSFJtUG5DN1NEaHJQNGNtSFNuWVJFcUVmQXJfWjZ1NHZmcVM4X2t1c2EycGhCMFRlTlFfSDhla09YbV8tM3FmeVpjVDM2SG9kVC1yOTJtS0hPY2lHUUh3?oc=5>

### Here is What to Know Beyond Why PepsiCo, Inc. (PEP) is a Trending Stock
- Summary: Overview of factors driving PepsiCo's current popularity among investors.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPcldmTTBGLW1vRFcycXJNRzZzQlZVbEs4eWYxQVVLX2ZTUmlTMlg5MG1JekdjUGpLYnFTeFo2V1BCN1gzMUlqWkdnajY3R01VZm1uNFM4TTlqRTM3aldxVjNUbUtXVW50UkhyQlA2VmF1X2NiTVZ3aTZDMkhJRGhiWTRZRHh4LWRGa291RVYxX01xM2tNS3E4?oc=5>

### Coca-Cola Yields Just 2.2% Compared to 4.3% for PepsiCo. Here's the Better Dividend King Stock for Generating Long-Term Passive Income.
- Summary: PepsiCo offers a higher dividend yield than Coca-Cola, positioning it as a more attractive income stock for long-term investors.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxON0NhSHRndFp3TWVQZlFmNWU2Yy13LThiTmd5OUdqRFllLTI1UXR0aEJBVVhXeVVmSDlTb0F4M19lR3prYVVvRHFpZGh0OXNGbk9Qc01FRWIybVJyTFhpMlJwa1YxUUpZQmVKSnl5ZG1lRTYwQUoyY0I0QTNMTG92Z3hndmFZbUZ3dGdiUnRCdlJ5Z1E?oc=5>

### Is PepsiCo Stock Stronger Than It Looks?
- Summary: Questioning PepsiCo’s stock strength suggests potential undervaluation and future upside for investors.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQdGI1al9tWm5HV2dzcWcxOWtxbWg5Rm9rMlFSWldnZG9tb3Nib2VNZXAxa0RXVVlxcnp3am9DN1J6TmFYNzBVazVaUmh0cnAyZlJSVWRyNVhuVHhpaXJKVURfWGllQjVmZnhhM09OUkVVdTFHWDBfcmIxRUIwd0FKNTFiNV9fZ2VQU2NGcncyYnRCV2dsNTQyQ1E4RVI3UUxS?oc=5>

### PepsiCo Stock Rebounds From 52-Week Lows; Can Q2 Earnings Fuel a Bigger Rally?
- Summary: PepsiCo’s recent rebound from 52‑week lows may be supported by upcoming Q2 earnings, indicating possible further upside.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxQSWtjeVctTnZoWm9PWVFQc3Zrc3NwRmJXbml5WTV4aVR4eFlFNWF3MTZFQTBQaEpEZm0zSE9DNk1FR2M5a3BmUXZQREZTT1hBMm5lNlVqWTdfZklLNHVXZ0ZGVktobTU1NXJ2WEpmdmliNk1scks2b3Zid0MzMlBadnJ6TE9BWm5DTnFVU2swMUg4SWNRcE9DUmhvX0dDcnREaHhHZlRPLUwyREZDTzdNUnVJLVJiNk9tWUNSTGRGdFcyNEI1WkZoNUl3WGVrZURHN1lldw?oc=5>

### Want Income for Life? PepsiCo Yields 4.3% and Has the Kind of Competitive Moat That Makes the Income Durable.
- Summary: PepsiCo’s 4.3% yield and strong moat make it a durable income source for long‑term investors.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOWU9xcFM1d2NYWVJwZXh1YnE3NDFDVWQ4YXpyazgtX1RqeWVVa1NiMVNvVWdJX21XbUkxRTF1ZEpMSXNySFBmNzFFSWdOV2o4eWE3MDd5Q1FfUm9Sdk9JUnFYY2NoUnkyaTJBUkNpSFhkLVhLRnJULU1EMFVzX1hkRzNvcThzaTlIcVdjM0hzNGx2NlpjSkRJMURBczk?oc=5>

### PepsiCo vs. Starbucks: Which Consumer Goods Stock Is a Better Buy in 2026?
- Summary: Comparing PepsiCo to Starbucks highlights PepsiCo’s stronger fundamentals for a 2026 investment case.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNckxQRzVSUGlzX3NHQXR3SmdWOVdtMGltZHotTzdEWG9ldlJILWw4Q0NDdUY5djFJMllvQzBJZEZWOGJSRlMtVHlVOTlhRXAwMVNGaE0wWHdhakMxYlJHRThzWXltSS03djRWTFVMMmZwcllsalpob3JJTUdxdDNMa29xT2t0UzdzeVBZdXU0Ujl0amVfMEU2TlE3VU04RDcyM0dGZm0zTFB1cC0yYVhuSjFQVlNGNUsyS0hfZVlOY3I3QQ?oc=5>

## HEADWINDS

### PepsiCo (NASDAQ:PEP) Stock Falls 1.4% - Here's What Happened
- Summary: PepsiCo (NASDAQ:PEP) Stock Falls 1.4% - Here's What Happened
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQMmpRUVY4eTl2WGstalBRMGRycnFfZW1kQW5abjh6cDhBUlZfbE5PYVNid28xNjBnUWl0NmJaZms0U1hrNWpGeTkyZkg2eDdpSUh2MFRZYkVKQ3BWTnZCTjY0eVNJTG5hNzh3dDFCNUNNWmt0QnlvZWpJdXdpY0VQYWI2cWhiVmVfRUdJR2I5Vmdma2k2eThocUdTTEVERE45X3dDTHhMd0lIaE1hd2FvYzE0VQ?oc=5>

## CATALYSTS

### PepsiCo (PEP) Stock Looks Below Fair Value After A Choppy Year
- Summary: PepsiCo (PEP) Stock Looks Below Fair Value After A Choppy Year
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNZzY1UzBpLS14VFl2UVBpU1FJYXJJRU9BaTNibm9OQkFQQ3g5NTZBWVNOUk9xRHV5dVptYmJYYnlwa0RpYUpuVGZvTmNqV09YcUpWSXk4YjNVNDFub0hQcXJRMGwweHJRSTR5eHBRam9uQmNXdHdLLVp6X0M2R2Zlb3k1UjlzRzl2YUt0VVJaeGtLUmhrYUJUaENB?oc=5>

### PepsiCo (PEP) Extends Its Global Beverage Partnership Through 2036
- Summary: PepsiCo (PEP) Extends Its Global Beverage Partnership Through 2036
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQQmxndWR4OVE5OElNMWZlanNGOWxEYWMtaTB2QVlGMmZGaXE3enBqakhlZ1pjX21yd2l1RGNKMHM4WVF2YWtaNjVkYU1wdW0wYnMxbFk5NS1TenRhZjJ4cmVFNTk2bzJGY1VXcXNwc1lmZDFUZHFEZ2dScUZ2REhLTjl4RlpPRW9GV3Bza0VzQlU5SDI5NFNyNWRHcl9YVzl5THc?oc=5>

### PepsiCo Renews US Partnership With Taco Bell Through 2036
- Summary: PepsiCo Renews US Partnership With Taco Bell Through 2036
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQdFhncENHdFJ1WG9OV2xTLW5ocGFWT2JNakRSM1gtbXp6UTFxNl95R2ZsZDZETEJoOGQ4NUVXQzlvZDl0bGd3UUFCRkNTc1dwUjIxSEp6SUN0RXdvN0R4cjFoVG5XMlN4TWQwVWw4MmIxTjV1WGM4aTVtWGdmNFQ5SEI0MTBVejBlUndrLWJrZlJ3NnktUzk0VFVXbGhxM3gw?oc=5>

### PepsiCo locks in Taco Bell partnership through 2036 following KFC loss
- Summary: PepsiCo locks in Taco Bell partnership through 2036 following KFC loss
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOMTFrLUlBM0tCbFd2R1B3MFVTNl9seUlwYlRTMGh1azBOZEpodG1MT1dzYUo1UkttZ2FYeWU4eUJReGg5TlU5bVVCbVJjNTJRYndpUm5YTWdXOGpBMHdqNHJwRjk4QzJZQzBOdTVCa3ViWHdTVmR4ZDlyRjc5MU01UTRLS2I4SnV4VFM4aEctX1NLTFhaMHFDMXNFaGpra2RIbGc?oc=5>

### PepsiCo Renews Taco Bell Beverage Deal Through 2036 After Losing KFC to Coca-Cola
- Summary: PepsiCo Renews Taco Bell Beverage Deal Through 2036 After Losing KFC to Coca-Cola
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOWHNSYTc3bFlvN0F5OHhUYUJvUEFqbWpwWllmZmh5NHhraFpmdkphMFZrTnB5dzNVaXlLMktuc1BuLXI0R3dXMXlQcEFxRUFFQ2phNEFHREN3bHZBcS04eENNNG5lU3VCeGlNNXBLMGdINFE0bFBqY0l6RTJoYkItb0dxOXkwSFFrRXNlc3IxZVB4cHZnb0ktUThGeGxDYzA?oc=5>

### PepsiCo Renews Partnership With Taco Bell for 11 More Years. Here’s What Investors Need to Know.
- Summary: PepsiCo Renews Partnership With Taco Bell for 11 More Years. Here’s What Investors Need to Know.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQbERnRTlldWdUY2NTMHVQWi1Xa0F4Yy1iVjFwTGhXZ2J6X3JYa2hWVHVVNWIySFczZmJUV1pZZ3pMWXV6eFJBaThiUlVUVGtoaHRZZGZIcFZlRVdRbFcxU2M4bThpTTRSdS1TTmVWaUNPUjVHd3FhUVNBb1BJaVZ1OE9ScVVxUUg1S1l5aUJxTzdibGlqSnc4djlkNXpLeUF0bmZN?oc=5>

### PepsiCo Pays More, Coca-Cola Looks Stronger. Which Dividend Wins for Retirement?
- Summary: PepsiCo Pays More, Coca-Cola Looks Stronger. Which Dividend Wins for Retirement?
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPNHNDNXNfQjBkU0xrcWp5STBoc1l1VFJXelVOVVJqSkJtUXhKa1d3MkR6c1JqLTkwZEtDVFJ2RFVpamw4a09SXzF6VFJRM1JodFJlQl9ESzhUNV9WalJvc3FfeFctb3E1OUs1Y2FXcmNmMHVtbGFxeFN5MDVfcFozMFBrS213RF9lUkp0RUk4MVNOSGVNdlNlMUlOcVFnX3dHdUpOMldWek5ZeTZ0WVp1WW1PMm52cVAxY0lvNjNB?oc=5>

### PepsiCo renews deal to supply Taco Bell
- Summary: PepsiCo renews deal to supply Taco Bell
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxPVU9iOFVraVpfUlU2VDVOdWtSU0NHMi1UcnFIRzRVVTIxMUt3S2g4ZXFZaDlocXN6T2J6aDU5cm5zRTdnMlZJOVhVczQxNkVpOHNjUTVIdWJhWlRUbWY5cWhxTWdOaC04M2RXekdxN2h3dHRSSmM4TWVaX0hoSy01VlBUTQ?oc=5>

### PepsiCo, Inc. $PEP Stock Sold by Oppenheimer & Co. Inc.
- Summary: PepsiCo, Inc. $PEP Stock Sold by Oppenheimer & Co. Inc.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQYzJFSXJHc1hPbTNOa2t2Z0E3V3VXRGpZWXRsaDlqQWFyY0hPdlRmWDhOZzZvR1BNSUVlaG9xZjhOSkFlS1d5bHhoWkNaZFp3Qjc2Sl9EVjdqZ2syOHVPM1BsTDdpM196bmluMGxJQUxsRHp6NXQzMkpfZFJRb2JkNTBkWmNrZTRHd3VpSXhUMW9Gam1lbTE2Qnk1Sk13eFZsaWxGbTFmNGtPWkJfb1E?oc=5>

### PepsiCo (PEP) Renews Taco Bell Deal, Is The Stock A Bargain?
- Summary: PepsiCo renews its partnership with Taco Bell, extending the franchise agreement and potentially boosting revenue streams.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNWGNGNndxNnhNR0NTQ2Fod2UtaTFnWXFpTm01ZUtMU1UtYnBRZk9BU0FDUWR0N3cwbjY0ZTMwMDUwNGZZYndVTnFhcHN0QzBSUTdlWndZQ1VQTDEwZ0E1N1ZYWDRSMWN6QjNRdjRsd1RBZC11MEc1bmhCYTZrcFR0cjFaVDBVTnc1dmcxR2JlMFdlbXBsSlNBNA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **16.79** | **8.17** | **11.62** | **5.60** | **181,925,937,152.00 USD** | **-8.99** |
| KO | 27.38 | 10.85 | 25.23 | 6.70 | 392,306,425,856.00 USD | 33.61 |
| MNST | 42.07 | 9.51 | 29.21 | 20.20 | 89,019,310,080.00 USD | 30.42 |
| KDP | 35.21 | 1.90 | 18.32 | 75.60 | 47,438,393,344.00 USD | 23.06 |

Peers fetched as_of: 2026-10-27; PEP reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

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
- Filing date: 2026-10-08
- Revenue (latest available single quarter): 25,274,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,048,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/77476/000007747626000048/pep-20260905.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi8AFBVV95cUxNa0lEZnJIcmhtS2Fkb0JmZFJrLWcxMG9vM1FncVBPX3QtNUJoMWdmb2VGN3ptcm0yQkZYbTc0cGJBQW1SUEg5VDd0RkZzZDVqRmVhMU5hdzM5djN2Vko3ZGo5anlqWGxsTHhzbC1mZm54eVhRWDUwY3Uwdnc1cVllMUJsZDk5Z3F4dm1NcUYwc040MkhOOG1NYW1RdGF4d1VhblBWekR2Ukdnd19jbWM2WVIxNEstQ25qMUU0bmRlbDJRdnBxTlcybWFBWEhDdE1WbDFVbk93YTlTN3k3aWgzRGwxaWxJcnVsOE1xM1lGdzQ?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxQUGJXQ0NGOTJJM2lNc1FGZFVWclVndEt4NXBNZ2UxZmFteEhsd1JTWVMwVld5QmE5cDBTdm1uV3BCMnVNMzQ3Q3UxdUFmS3NRT1h0a0pVQm5vRV9OOUx0d1QxLTFPVER2UkpVcV85dDJqNXdSbjkwYnUtTDBaS3RFT2d5d1RDcTZLdWNnWWNkQUh5WEdIaGN0ZEU2SlFIbnF1NlRwbC1CMU5ydzQxVDdjMW5OMmcwZHdsWlRuOHFoaHRXY0wxek8zQXc2VDN3MTBqR3c2bXJCQ0FiYkpKREtvWmJJaTQzRUpoaHc?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNSU9USEEzOTVhWVhlbm8xelBIOGVRd2tFNmxGRTQ0THdiLVE1MXZLa2xwdDBDTzVwOVVnckN2cEhmOTZESFViUmNER2xCY2h2VUtNUzJKUHhjaFFtMUphQU92UXJmTDZpd3lxbi02Nk1rUTNodmF2NUlRbi13SFhtR1lrNFN2blpkNkg2OGhwVUh5T256enpIdnNfNXQ1NnVXaDhVUHhB?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPTnhBV0FrN01aYkVUb3FYekwyZTVDTW1tSkpqd2F1ZzJPSTRBbERlWkZmZmtyNzJKSnM5OWJjQU1mZ2tMUWVSV1FkTWtSUDktT3NYTG9qSGRyNkhTQkFDdHVBMU9vV3l5Y1EySnBrblYzU0llYVlVdUFXYWRLRHo2T2ZlVWIwcjQxd0JPOENhZTc3Z2dPdEdCbnRraUhkRWRqZ3BLb0QzanBVTXpmdUw4Q2FjZ2VaOWh2TlE?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNWUJtTlc4bUphUHZOazVMdklwMmdibC0wMy1QUHc0ZGRmOVNkcllOYzExRWRiZXU2VmwzTGIyVVJGemtoZVg5aVRBZHBZcnFTOFM5V1l1czZ5UlZ0Qkh4S2lqZW1oWGZ6Mk92WF9ZRE5CS0Z0LTRhaG5wZnB6TG5WRDZHbWlwQThFV3VrUXo4SQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPOUF0bmJkQ1VJZXZkeG5WRk9YUWllcDh1NERKc1JXTEZ0VG1RVkFmR21XN01KRGh5aTNKbjRJWnNqaVc0UndnbzNSZDR1M3ZQSFJtUG5DN1NEaHJQNGNtSFNuWVJFcUVmQXJfWjZ1NHZmcVM4X2t1c2EycGhCMFRlTlFfSDhla09YbV8tM3FmeVpjVDM2SG9kVC1yOTJtS0hPY2lHUUh3?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPcldmTTBGLW1vRFcycXJNRzZzQlZVbEs4eWYxQVVLX2ZTUmlTMlg5MG1JekdjUGpLYnFTeFo2V1BCN1gzMUlqWkdnajY3R01VZm1uNFM4TTlqRTM3aldxVjNUbUtXVW50UkhyQlA2VmF1X2NiTVZ3aTZDMkhJRGhiWTRZRHh4LWRGa291RVYxX01xM2tNS3E4?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxON0NhSHRndFp3TWVQZlFmNWU2Yy13LThiTmd5OUdqRFllLTI1UXR0aEJBVVhXeVVmSDlTb0F4M19lR3prYVVvRHFpZGh0OXNGbk9Qc01FRWIybVJyTFhpMlJwa1YxUUpZQmVKSnl5ZG1lRTYwQUoyY0I0QTNMTG92Z3hndmFZbUZ3dGdiUnRCdlJ5Z1E?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQdGI1al9tWm5HV2dzcWcxOWtxbWg5Rm9rMlFSWldnZG9tb3Nib2VNZXAxa0RXVVlxcnp3am9DN1J6TmFYNzBVazVaUmh0cnAyZlJSVWRyNVhuVHhpaXJKVURfWGllQjVmZnhhM09OUkVVdTFHWDBfcmIxRUIwd0FKNTFiNV9fZ2VQU2NGcncyYnRCV2dsNTQyQ1E4RVI3UUxS?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQSWtjeVctTnZoWm9PWVFQc3Zrc3NwRmJXbml5WTV4aVR4eFlFNWF3MTZFQTBQaEpEZm0zSE9DNk1FR2M5a3BmUXZQREZTT1hBMm5lNlVqWTdfZklLNHVXZ0ZGVktobTU1NXJ2WEpmdmliNk1scks2b3Zid0MzMlBadnJ6TE9BWm5DTnFVU2swMUg4SWNRcE9DUmhvX0dDcnREaHhHZlRPLUwyREZDTzdNUnVJLVJiNk9tWUNSTGRGdFcyNEI1WkZoNUl3WGVrZURHN1lldw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOWU9xcFM1d2NYWVJwZXh1YnE3NDFDVWQ4YXpyazgtX1RqeWVVa1NiMVNvVWdJX21XbUkxRTF1ZEpMSXNySFBmNzFFSWdOV2o4eWE3MDd5Q1FfUm9Sdk9JUnFYY2NoUnkyaTJBUkNpSFhkLVhLRnJULU1EMFVzX1hkRzNvcThzaTlIcVdjM0hzNGx2NlpjSkRJMURBczk?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQc1g1TkNWMjVsY2lJOUo4WFZPbkgyZFZOV1lLWUlnT3ItRm5ZczZDSk5rRkpkNXAxNE9YYnVtOTZ0dXdCOU1yUjVyWEJqUExCMDlRUDc2TXE2R2lEVEVqM1ROVGU5RG5QVXFjRlFJempFSDhLcngwbmFYd2U3QlhNb0pEbEhyd0ZtNS1hX3hMNVdPT1hHTTZkYw?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNckxQRzVSUGlzX3NHQXR3SmdWOVdtMGltZHotTzdEWG9ldlJILWw4Q0NDdUY5djFJMllvQzBJZEZWOGJSRlMtVHlVOTlhRXAwMVNGaE0wWHdhakMxYlJHRThzWXltSS03djRWTFVMMmZwcllsalpob3JJTUdxdDNMa29xT2t0UzdzeVBZdXU0Ujl0amVfMEU2TlE3VU04RDcyM0dGZm0zTFB1cC0yYVhuSjFQVlNGNUsyS0hfZVlOY3I3QQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQMmpRUVY4eTl2WGstalBRMGRycnFfZW1kQW5abjh6cDhBUlZfbE5PYVNid28xNjBnUWl0NmJaZms0U1hrNWpGeTkyZkg2eDdpSUh2MFRZYkVKQ3BWTnZCTjY0eVNJTG5hNzh3dDFCNUNNWmt0QnlvZWpJdXdpY0VQYWI2cWhiVmVfRUdJR2I5Vmdma2k2eThocUdTTEVERE45X3dDTHhMd0lIaE1hd2FvYzE0VQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNZzY1UzBpLS14VFl2UVBpU1FJYXJJRU9BaTNibm9OQkFQQ3g5NTZBWVNOUk9xRHV5dVptYmJYYnlwa0RpYUpuVGZvTmNqV09YcUpWSXk4YjNVNDFub0hQcXJRMGwweHJRSTR5eHBRam9uQmNXdHdLLVp6X0M2R2Zlb3k1UjlzRzl2YUt0VVJaeGtLUmhrYUJUaENB?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQQmxndWR4OVE5OElNMWZlanNGOWxEYWMtaTB2QVlGMmZGaXE3enBqakhlZ1pjX21yd2l1RGNKMHM4WVF2YWtaNjVkYU1wdW0wYnMxbFk5NS1TenRhZjJ4cmVFNTk2bzJGY1VXcXNwc1lmZDFUZHFEZ2dScUZ2REhLTjl4RlpPRW9GV3Bza0VzQlU5SDI5NFNyNWRHcl9YVzl5THc?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQdFhncENHdFJ1WG9OV2xTLW5ocGFWT2JNakRSM1gtbXp6UTFxNl95R2ZsZDZETEJoOGQ4NUVXQzlvZDl0bGd3UUFCRkNTc1dwUjIxSEp6SUN0RXdvN0R4cjFoVG5XMlN4TWQwVWw4MmIxTjV1WGM4aTVtWGdmNFQ5SEI0MTBVejBlUndrLWJrZlJ3NnktUzk0VFVXbGhxM3gw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOMTFrLUlBM0tCbFd2R1B3MFVTNl9seUlwYlRTMGh1azBOZEpodG1MT1dzYUo1UkttZ2FYeWU4eUJReGg5TlU5bVVCbVJjNTJRYndpUm5YTWdXOGpBMHdqNHJwRjk4QzJZQzBOdTVCa3ViWHdTVmR4ZDlyRjc5MU01UTRLS2I4SnV4VFM4aEctX1NLTFhaMHFDMXNFaGpra2RIbGc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOWHNSYTc3bFlvN0F5OHhUYUJvUEFqbWpwWllmZmh5NHhraFpmdkphMFZrTnB5dzNVaXlLMktuc1BuLXI0R3dXMXlQcEFxRUFFQ2phNEFHREN3bHZBcS04eENNNG5lU3VCeGlNNXBLMGdINFE0bFBqY0l6RTJoYkItb0dxOXkwSFFrRXNlc3IxZVB4cHZnb0ktUThGeGxDYzA?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQbERnRTlldWdUY2NTMHVQWi1Xa0F4Yy1iVjFwTGhXZ2J6X3JYa2hWVHVVNWIySFczZmJUV1pZZ3pMWXV6eFJBaThiUlVUVGtoaHRZZGZIcFZlRVdRbFcxU2M4bThpTTRSdS1TTmVWaUNPUjVHd3FhUVNBb1BJaVZ1OE9ScVVxUUg1S1l5aUJxTzdibGlqSnc4djlkNXpLeUF0bmZN?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxOTlZNMVVha1lxcTRCMlV6UGR2SlltekgzQWt1UGlBX19WLVl1T0tOeHJ3SnZkVE5SVVJnRGh0bEZXUkxwVkFzYmtRem1VT0JmN19UeTRuOVl3WDdMaDZBTVBwa0hESmk2ckV3X0kyNUFHLW5TT2RQNmFVWThBVkdvRGttRG1TRVllY2kxRVd2cVJnM2VtcEFld3RGUjBoZ3dFZTc1T1NaeGpWNXltZ3VxdThZd1AxejlTQ05oLW5qUWlpNHR6WUpzanhpMm5qNVE?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPNHNDNXNfQjBkU0xrcWp5STBoc1l1VFJXelVOVVJqSkJtUXhKa1d3MkR6c1JqLTkwZEtDVFJ2RFVpamw4a09SXzF6VFJRM1JodFJlQl9ESzhUNV9WalJvc3FfeFctb3E1OUs1Y2FXcmNmMHVtbGFxeFN5MDVfcFozMFBrS213RF9lUkp0RUk4MVNOSGVNdlNlMUlOcVFnX3dHdUpOMldWek5ZeTZ0WVp1WW1PMm52cVAxY0lvNjNB?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxPVU9iOFVraVpfUlU2VDVOdWtSU0NHMi1UcnFIRzRVVTIxMUt3S2g4ZXFZaDlocXN6T2J6aDU5cm5zRTdnMlZJOVhVczQxNkVpOHNjUTVIdWJhWlRUbWY5cWhxTWdOaC04M2RXekdxN2h3dHRSSmM4TWVaX0hoSy01VlBUTQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQYzJFSXJHc1hPbTNOa2t2Z0E3V3VXRGpZWXRsaDlqQWFyY0hPdlRmWDhOZzZvR1BNSUVlaG9xZjhOSkFlS1d5bHhoWkNaZFp3Qjc2Sl9EVjdqZ2syOHVPM1BsTDdpM196bmluMGxJQUxsRHp6NXQzMkpfZFJRb2JkNTBkWmNrZTRHd3VpSXhUMW9Gam1lbTE2Qnk1Sk13eFZsaWxGbTFmNGtPWkJfb1E?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNWGNGNndxNnhNR0NTQ2Fod2UtaTFnWXFpTm01ZUtMU1UtYnBRZk9BU0FDUWR0N3cwbjY0ZTMwMDUwNGZZYndVTnFhcHN0QzBSUTdlWndZQ1VQTDEwZ0E1N1ZYWDRSMWN6QjNRdjRsd1RBZC11MEc1bmhCYTZrcFR0cjFaVDBVTnc1dmcxR2JlMFdlbXBsSlNBNA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
