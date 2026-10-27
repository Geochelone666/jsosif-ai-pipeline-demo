# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T01:52:19.067915+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 11, 'ai': 9, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 8 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 52.17%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 135.4600 |
| Return 1D (%) | -0.2283 |
| Return 1W (%) | 1.4150 |
| Return 1M (%) | 5.3098 |
| Return YTD (%) | -2.7428 |
| Return 1Y (%) | -6.9952 |
| Annualized volatility (%) | 21.2009 |
| Beta vs SPY | -0.2169 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | -0.2732 |
| Downside deviation (rf=0, %) | 14.5471 |
| Sortino (rf=0) | -0.3981 |
| Historical VaR 95% (1D, %) | 2.2001 |
| Historical ES 95% (1D, %) | 2.6716 |
| Correlation vs SPY | -0.1301 |
| Tracking error vs SPY (%) | 26.1021 |
| P/E (trailing) | 17.04 |
| P/B | 8.29 |
| EV/EBITDA | 11.76 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 15.68 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.88 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.90 |
| MA50 | 133.5908 |
| Close vs MA50 (%) | 1.3992 |
| MA200 | 143.7922 |
| Close vs MA200 (%) | -5.7946 |
| RSI (14, Wilder) | 59.0103 |
| MACD (12,26) | 1.0688 |
| MACD signal (9) | -0.2541 |
| MACD histogram | 1.3228 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 135.4600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.2283 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.4150 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.3098 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -2.7428 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -6.9952 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.2009 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.5471 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.3981 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.2001 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6716 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1301 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.1021 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.2169 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.2732 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.6806 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.8830 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.8995 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.0390 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.0103 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.3228 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.3992 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -5.7946 -> Clearly below the moving-average trend level.

## TAILWINDS

### PEP Stock Gains After PepsiCo Locks In 11 More Years With Taco Bell Following KFC Loss To Coke
- Summary: PEP Stock Gains After PepsiCo Locks In 11 More Years With Taco Bell Following KFC Loss To Coke
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOTXdTWFNzNmhxOU9ManFlWjVDVUI0LUlIaFdpaFJvTzkzampMcjhZbS1YNHRnNGVDemt1N3NEbFhodC1jRGhKTTN2ZWdPaGRPSXFWR2pIdF82UTNpdzF4MWFySnFBZ0RscmJibnpXSmtydUtrVElpdUNoMk9KTGgwUkNjd180VzdqVFJDcVdGVnR2ak54cXFnQ3Bn?oc=5>

### PepsiCo Inc (PEP) Stock Up 3.1% and Still Undervalued -- GF Scor
- Summary: PepsiCo Inc (PEP) Stock Up 3.1% and Still Undervalued -- GF Scor
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNSU9USEEzOTVhWVhlbm8xelBIOGVRd2tFNmxGRTQ0THdiLVE1MXZLa2xwdDBDTzVwOVVnckN2cEhmOTZESFViUmNER2xCY2h2VUtNUzJKUHhjaFFtMUphQU92UXJmTDZpd3lxbi02Nk1rUTNodmF2NUlRbi13SFhtR1lrNFN2blpkNkg2OGhwVUh5T256enpIdnNfNXQ1NnVXaDhVUHhB?oc=5>

### Unusual Options Volume Report: PepsiCo Stock
- Summary: Reports of higher-than-normal options trading activity for PepsiCo, indicating increased market interest.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPOUF0bmJkQ1VJZXZkeG5WRk9YUWllcDh1NERKc1JXTEZ0VG1RVkFmR21XN01KRGh5aTNKbjRJWnNqaVc0UndnbzNSZDR1M3ZQSFJtUG5DN1NEaHJQNGNtSFNuWVJFcUVmQXJfWjZ1NHZmcVM4X2t1c2EycGhCMFRlTlFfSDhla09YbV8tM3FmeVpjVDM2SG9kVC1yOTJtS0hPY2lHUUh3?oc=5>

### PepsiCo Stock Could Be a Contrarian Opportunity if This One Thing Improves
- Summary: Analysis suggests PepsiCo stock may rise if a specific metric improves, highlighting potential upside.
- Date: 2026-10-22 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPTnhBV0FrN01aYkVUb3FYekwyZTVDTW1tSkpqd2F1ZzJPSTRBbERlWkZmZmtyNzJKSnM5OWJjQU1mZ2tMUWVSV1FkTWtSUDktT3NYTG9qSGRyNkhTQkFDdHVBMU9vV3l5Y1EySnBrblYzU0llYVlVdUFXYWRLRHo2T2ZlVWIwcjQxd0JPOENhZTc3Z2dPdEdCbnRraUhkRWRqZ3BLb0QzanBVTXpmdUw4Q2FjZ2VaOWh2TlE?oc=5>

### Here is What to Know Beyond Why PepsiCo, Inc. (PEP) is a Trending Stock
- Summary: Overview of factors driving PepsiCo's current popularity among investors.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPcldmTTBGLW1vRFcycXJNRzZzQlZVbEs4eWYxQVVLX2ZTUmlTMlg5MG1JekdjUGpLYnFTeFo2V1BCN1gzMUlqWkdnajY3R01VZm1uNFM4TTlqRTM3aldxVjNUbUtXVW50UkhyQlA2VmF1X2NiTVZ3aTZDMkhJRGhiWTRZRHh4LWRGa291RVYxX01xM2tNS3E4?oc=5>

### Taco Bell extends PepsiCo partnership through 2036
- Summary: Taco Bell extends its partnership with PepsiCo until 2036, strengthening distribution and brand synergy.
- Date: 2026-10-22 | Impact: high | Horizon: long | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNQURfSTdiZGpkZHkxTlhJenFVN083XzBTc0xtU1J6Z1RUWnlINjlEaGFRaWRNNXRuMm5mc2JPQ2xFVU5kNjVQTzdXdkRWVVF0am9DeER4LUN0MklUbE4xWVBPbm1hcDRnUlNqd1ZnWUtsTnRjN25qZEg2cjZWNVhfYVZ0LTc1UjhUcHdWRXdvazBFMThMaVQtS2xCSXBDcUtRZ0JzcHItSFQ?oc=5>

## HEADWINDS

### PepsiCo to close bottling site in US
- Summary: PepsiCo announced the closure of a bottling facility in the United States, reducing production capacity.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOWU52WVVOTTA1RFpzMkctZUl1NXhYRHZwWVE2ZjVOeTJNcnl4cGQ5Sl9rdjA3Z3YycXk3Q01tRnVnODBuTnZ0d2MwZnlHc1B2bklJMWlmc1lBM3FScW91MG5ZS1NkUUdCNWU2em5Gam5fcm9ycjBnUU4wWmtPNVV3ZzNNdWJ1ZHQ2ZGJpbUptQ0ZkRWpw?oc=5>

## CATALYSTS

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

### PepsiCo Yields 4%. Is Its Dividend Still Safe After Lowering Guidance?
- Summary: PepsiCo Yields 4%. Is Its Dividend Still Safe After Lowering Guidance?
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxOcUZjT1c0U1ZLcEszN2plV0FFWERYbDNWcm50Nzh1VF8tdkhWNXBmQnNLSTZmUXIxMjFZY2hHS1hyaDB0aDZWbGNpMkZPNWdEZjJMQXNyNmNMS0p3S3NSWng4a2VxVnU3MjZILW8tYThjaUpEbzJHTlpZMlo4eGFjX1pDekFwai1aQ3p1LVRkWXV4QzNrVHNxdDQyUjQ4YlFlcUV0RWhDSkx5ekJWcm00Qg?oc=5>

### PepsiCo Strikes Back After KFC Loss, Locks In Taco Bell Beverage Deal Through 2036
- Summary: PepsiCo Strikes Back After KFC Loss, Locks In Taco Bell Beverage Deal Through 2036
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxPWlVxRk9VZlRJXzdQdnV2bS1pNTQwUjJIdGY2NnRtbzdETWVYclpJU1B3S1duaFlwN0ZNRWdnU2oxT2ZjcVhhQVFxU3NCNncxZ0d1R1k0WUVCZnRuNnRKa0JvVXNKQWhEMVlQakpLQUU1Mlp6RGZxWFNVN0JOU2VFQXBLR2Uzc3ltUFpjbXV4U05HOVlLb0h0dVhublRJYzFlN01BZll5TlhodDZXNnV0TnZ5MWYxeWdOUk1ra19WalY3RVdIcmZfQWhldUROTG9FWGJvag?oc=5>

### PepsiCo Stock And Other Defensive Dividend Plays For Uncertain Markets
- Summary: PepsiCo Stock And Other Defensive Dividend Plays For Uncertain Markets
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxPTHFxRE5uZEVPMWZfNHF5cmZEdkpna01fZmFPYXpuZGFWc1BTVUNmZk5VWUg0WXN1aWNJQjkzUjZxbkdQZThzSzdkUDhpdFZnVlozUjRmR0FzMUh0enlWT1dpVl9mTDFjczkwUUl4bW9mMUNBb3VZMU1HcEJmY1cwLUlMUHlIQk9XeGVMVTh3SFRaa1I1STFSVmQxNk1sWXFodW9vbzRnZWNaRzFlcVNXR2pNUFFJakZWQ0dGSDJHMU5GT1llS21sUDZPRWdLeVpoOFRkemh30gHbAUFVX3lxTFAtc3Nvd3pkM3lOZWZqeDZDNjRWazF2ZW9GNm1rMkZIUWk2VEpGamFFSUhlTENxYzdxWTNmNVVXeEVyUzdxTGJLQ09tNGxzcEJ5TDJYd0VRS3FXWUpMaGpMRlFtZlRZSnRIM2FWZnNCelRiS0FYSzlXR2tEMGhxc1FZZGxjc2FZRl9JdU1nZER1aUxfU2hkSkJhVDVJeUJWaHFQbnc4Ymh4MVItOGZ0b1VGS1R5YVU1R0dObDF2ODM2UjdGUmM1VzFqSTRqcUFUX0taOXowaW82VTRvbw?oc=5>

### PepsiCo (PEP) Renews Taco Bell Deal, Is The Stock A Bargain?
- Summary: PepsiCo renews its partnership with Taco Bell, extending the franchise agreement and potentially boosting revenue streams.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNWGNGNndxNnhNR0NTQ2Fod2UtaTFnWXFpTm01ZUtMU1UtYnBRZk9BU0FDUWR0N3cwbjY0ZTMwMDUwNGZZYndVTnFhcHN0QzBSUTdlWndZQ1VQTDEwZ0E1N1ZYWDRSMWN6QjNRdjRsd1RBZC11MEc1bmhCYTZrcFR0cjFaVDBVTnc1dmcxR2JlMFdlbXBsSlNBNA?oc=5>

### Baja Blast has grown into a billion-dollar brand. Taco Bell and PepsiCo renewed their deal for 11 years.
- Summary: PepsiCo and Taco Bell extended their partnership, securing an 11‑year renewal for the popular Baja Blast brand, boosting long‑term revenue prospects.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxNSmpPV2xyd2M3emNERjlMUjBnQ1BWNUhEeDlFZC1vSlQ1MXVINVNiRFAxdFdKWmRGa2tCM2xHcmFkeVA1M2pQbDdXcG4zRzUySVFra0lqbk5wZDh3NC1aUHRIdnhzVVJaWVJzM3E5QklvMXUzX0xlN3dnMmtVLTFzQXhpTkFlWFlpbXFQb3lDSTdTSjhRczNFSE1pRlF4Z0NubWJhZGR6Z2drV2xiTWZBS0prUFFlaVBXSDNNZ053?oc=5>

### What is moving PepsiCo (NASDAQ:PEP) stock today?
- Summary: Investors are analyzing factors influencing PepsiCo's stock price today.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOengyWEMwYWdwMkNSSi1JRGhMNjluazJ2QkFCS080UExPUjFsSkdqc0M1WWhVdmFaSHBvZnhkaHdfUi1fakJDaTdIUWE5NjNqNTByczRiMk1nZVQ3MTJwdjBXWWI0YWl3VHF6YlhNUGtGc1Z6TXdFd1pHNXZJS1U2LVpubWxKcnluaWx4ODJ6aExUUQ?oc=5>

### PepsiCo (NASDAQ:PEP) In Focus As Consumer Demand Shifts
- Summary: PepsiCo faces changing consumer demand, impacting its product strategy.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQNUpjV1hwai03UGFieG1QUDZCUkI5My1hOU5Vb1JycGpKUzhaUVpQSmlBV0s3SlNjZ01WM25BQ3p4bHZ5RjUzVnJId1NuUnlkbklLYmhWQ1VHY3hXS2loMnp4bjFwamJydUJyNnNmeEFDZ01LY1MzdWxGUzhOMzZhX0k5Q3p0RG5RNkFuS1lCamlmQVUxU0FobnN4YXQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **17.04** | **8.29** | **11.76** | **5.60** | **184,596,922,368.00 USD** | **-7.00** |
| KO | 27.84 | 11.03 | 25.23 | 6.70 | 398,846,263,296.00 USD | 36.51 |
| MNST | 43.00 | 9.72 | 29.88 | 20.20 | 90,978,361,344.00 USD | 33.28 |
| KDP | 35.34 | 1.90 | 18.36 | 75.60 | 47,615,303,680.00 USD | 32.93 |

Peers fetched as_of: 2026-10-26; PEP reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

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

- https://news.google.com/rss/articles/CBMimgFBVV95cUxOTXdTWFNzNmhxOU9ManFlWjVDVUI0LUlIaFdpaFJvTzkzampMcjhZbS1YNHRnNGVDemt1N3NEbFhodC1jRGhKTTN2ZWdPaGRPSXFWR2pIdF82UTNpdzF4MWFySnFBZ0RscmJibnpXSmtydUtrVElpdUNoMk9KTGgwUkNjd180VzdqVFJDcVdGVnR2ak54cXFnQ3Bn?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNSU9USEEzOTVhWVhlbm8xelBIOGVRd2tFNmxGRTQ0THdiLVE1MXZLa2xwdDBDTzVwOVVnckN2cEhmOTZESFViUmNER2xCY2h2VUtNUzJKUHhjaFFtMUphQU92UXJmTDZpd3lxbi02Nk1rUTNodmF2NUlRbi13SFhtR1lrNFN2blpkNkg2OGhwVUh5T256enpIdnNfNXQ1NnVXaDhVUHhB?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPOUF0bmJkQ1VJZXZkeG5WRk9YUWllcDh1NERKc1JXTEZ0VG1RVkFmR21XN01KRGh5aTNKbjRJWnNqaVc0UndnbzNSZDR1M3ZQSFJtUG5DN1NEaHJQNGNtSFNuWVJFcUVmQXJfWjZ1NHZmcVM4X2t1c2EycGhCMFRlTlFfSDhla09YbV8tM3FmeVpjVDM2SG9kVC1yOTJtS0hPY2lHUUh3?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPTnhBV0FrN01aYkVUb3FYekwyZTVDTW1tSkpqd2F1ZzJPSTRBbERlWkZmZmtyNzJKSnM5OWJjQU1mZ2tMUWVSV1FkTWtSUDktT3NYTG9qSGRyNkhTQkFDdHVBMU9vV3l5Y1EySnBrblYzU0llYVlVdUFXYWRLRHo2T2ZlVWIwcjQxd0JPOENhZTc3Z2dPdEdCbnRraUhkRWRqZ3BLb0QzanBVTXpmdUw4Q2FjZ2VaOWh2TlE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPcldmTTBGLW1vRFcycXJNRzZzQlZVbEs4eWYxQVVLX2ZTUmlTMlg5MG1JekdjUGpLYnFTeFo2V1BCN1gzMUlqWkdnajY3R01VZm1uNFM4TTlqRTM3aldxVjNUbUtXVW50UkhyQlA2VmF1X2NiTVZ3aTZDMkhJRGhiWTRZRHh4LWRGa291RVYxX01xM2tNS3E4?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNQURfSTdiZGpkZHkxTlhJenFVN083XzBTc0xtU1J6Z1RUWnlINjlEaGFRaWRNNXRuMm5mc2JPQ2xFVU5kNjVQTzdXdkRWVVF0am9DeER4LUN0MklUbE4xWVBPbm1hcDRnUlNqd1ZnWUtsTnRjN25qZEg2cjZWNVhfYVZ0LTc1UjhUcHdWRXdvazBFMThMaVQtS2xCSXBDcUtRZ0JzcHItSFQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOWU52WVVOTTA1RFpzMkctZUl1NXhYRHZwWVE2ZjVOeTJNcnl4cGQ5Sl9rdjA3Z3YycXk3Q01tRnVnODBuTnZ0d2MwZnlHc1B2bklJMWlmc1lBM3FScW91MG5ZS1NkUUdCNWU2em5Gam5fcm9ycjBnUU4wWmtPNVV3ZzNNdWJ1ZHQ2ZGJpbUptQ0ZkRWpw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQQmxndWR4OVE5OElNMWZlanNGOWxEYWMtaTB2QVlGMmZGaXE3enBqakhlZ1pjX21yd2l1RGNKMHM4WVF2YWtaNjVkYU1wdW0wYnMxbFk5NS1TenRhZjJ4cmVFNTk2bzJGY1VXcXNwc1lmZDFUZHFEZ2dScUZ2REhLTjl4RlpPRW9GV3Bza0VzQlU5SDI5NFNyNWRHcl9YVzl5THc?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQdFhncENHdFJ1WG9OV2xTLW5ocGFWT2JNakRSM1gtbXp6UTFxNl95R2ZsZDZETEJoOGQ4NUVXQzlvZDl0bGd3UUFCRkNTc1dwUjIxSEp6SUN0RXdvN0R4cjFoVG5XMlN4TWQwVWw4MmIxTjV1WGM4aTVtWGdmNFQ5SEI0MTBVejBlUndrLWJrZlJ3NnktUzk0VFVXbGhxM3gw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOMTFrLUlBM0tCbFd2R1B3MFVTNl9seUlwYlRTMGh1azBOZEpodG1MT1dzYUo1UkttZ2FYeWU4eUJReGg5TlU5bVVCbVJjNTJRYndpUm5YTWdXOGpBMHdqNHJwRjk4QzJZQzBOdTVCa3ViWHdTVmR4ZDlyRjc5MU01UTRLS2I4SnV4VFM4aEctX1NLTFhaMHFDMXNFaGpra2RIbGc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOWHNSYTc3bFlvN0F5OHhUYUJvUEFqbWpwWllmZmh5NHhraFpmdkphMFZrTnB5dzNVaXlLMktuc1BuLXI0R3dXMXlQcEFxRUFFQ2phNEFHREN3bHZBcS04eENNNG5lU3VCeGlNNXBLMGdINFE0bFBqY0l6RTJoYkItb0dxOXkwSFFrRXNlc3IxZVB4cHZnb0ktUThGeGxDYzA?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQbERnRTlldWdUY2NTMHVQWi1Xa0F4Yy1iVjFwTGhXZ2J6X3JYa2hWVHVVNWIySFczZmJUV1pZZ3pMWXV6eFJBaThiUlVUVGtoaHRZZGZIcFZlRVdRbFcxU2M4bThpTTRSdS1TTmVWaUNPUjVHd3FhUVNBb1BJaVZ1OE9ScVVxUUg1S1l5aUJxTzdibGlqSnc4djlkNXpLeUF0bmZN?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxOTlZNMVVha1lxcTRCMlV6UGR2SlltekgzQWt1UGlBX19WLVl1T0tOeHJ3SnZkVE5SVVJnRGh0bEZXUkxwVkFzYmtRem1VT0JmN19UeTRuOVl3WDdMaDZBTVBwa0hESmk2ckV3X0kyNUFHLW5TT2RQNmFVWThBVkdvRGttRG1TRVllY2kxRVd2cVJnM2VtcEFld3RGUjBoZ3dFZTc1T1NaeGpWNXltZ3VxdThZd1AxejlTQ05oLW5qUWlpNHR6WUpzanhpMm5qNVE?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPNHNDNXNfQjBkU0xrcWp5STBoc1l1VFJXelVOVVJqSkJtUXhKa1d3MkR6c1JqLTkwZEtDVFJ2RFVpamw4a09SXzF6VFJRM1JodFJlQl9ESzhUNV9WalJvc3FfeFctb3E1OUs1Y2FXcmNmMHVtbGFxeFN5MDVfcFozMFBrS213RF9lUkp0RUk4MVNOSGVNdlNlMUlOcVFnX3dHdUpOMldWek5ZeTZ0WVp1WW1PMm52cVAxY0lvNjNB?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxOcUZjT1c0U1ZLcEszN2plV0FFWERYbDNWcm50Nzh1VF8tdkhWNXBmQnNLSTZmUXIxMjFZY2hHS1hyaDB0aDZWbGNpMkZPNWdEZjJMQXNyNmNMS0p3S3NSWng4a2VxVnU3MjZILW8tYThjaUpEbzJHTlpZMlo4eGFjX1pDekFwai1aQ3p1LVRkWXV4QzNrVHNxdDQyUjQ4YlFlcUV0RWhDSkx5ekJWcm00Qg?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxPWlVxRk9VZlRJXzdQdnV2bS1pNTQwUjJIdGY2NnRtbzdETWVYclpJU1B3S1duaFlwN0ZNRWdnU2oxT2ZjcVhhQVFxU3NCNncxZ0d1R1k0WUVCZnRuNnRKa0JvVXNKQWhEMVlQakpLQUU1Mlp6RGZxWFNVN0JOU2VFQXBLR2Uzc3ltUFpjbXV4U05HOVlLb0h0dVhublRJYzFlN01BZll5TlhodDZXNnV0TnZ5MWYxeWdOUk1ra19WalY3RVdIcmZfQWhldUROTG9FWGJvag?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxPTHFxRE5uZEVPMWZfNHF5cmZEdkpna01fZmFPYXpuZGFWc1BTVUNmZk5VWUg0WXN1aWNJQjkzUjZxbkdQZThzSzdkUDhpdFZnVlozUjRmR0FzMUh0enlWT1dpVl9mTDFjczkwUUl4bW9mMUNBb3VZMU1HcEJmY1cwLUlMUHlIQk9XeGVMVTh3SFRaa1I1STFSVmQxNk1sWXFodW9vbzRnZWNaRzFlcVNXR2pNUFFJakZWQ0dGSDJHMU5GT1llS21sUDZPRWdLeVpoOFRkemh30gHbAUFVX3lxTFAtc3Nvd3pkM3lOZWZqeDZDNjRWazF2ZW9GNm1rMkZIUWk2VEpGamFFSUhlTENxYzdxWTNmNVVXeEVyUzdxTGJLQ09tNGxzcEJ5TDJYd0VRS3FXWUpMaGpMRlFtZlRZSnRIM2FWZnNCelRiS0FYSzlXR2tEMGhxc1FZZGxjc2FZRl9JdU1nZER1aUxfU2hkSkJhVDVJeUJWaHFQbnc4Ymh4MVItOGZ0b1VGS1R5YVU1R0dObDF2ODM2UjdGUmM1VzFqSTRqcUFUX0taOXowaW82VTRvbw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNWGNGNndxNnhNR0NTQ2Fod2UtaTFnWXFpTm01ZUtMU1UtYnBRZk9BU0FDUWR0N3cwbjY0ZTMwMDUwNGZZYndVTnFhcHN0QzBSUTdlWndZQ1VQTDEwZ0E1N1ZYWDRSMWN6QjNRdjRsd1RBZC11MEc1bmhCYTZrcFR0cjFaVDBVTnc1dmcxR2JlMFdlbXBsSlNBNA?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxNSmpPV2xyd2M3emNERjlMUjBnQ1BWNUhEeDlFZC1vSlQ1MXVINVNiRFAxdFdKWmRGa2tCM2xHcmFkeVA1M2pQbDdXcG4zRzUySVFra0lqbk5wZDh3NC1aUHRIdnhzVVJaWVJzM3E5QklvMXUzX0xlN3dnMmtVLTFzQXhpTkFlWFlpbXFQb3lDSTdTSjhRczNFSE1pRlF4Z0NubWJhZGR6Z2drV2xiTWZBS0prUFFlaVBXSDNNZ053?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOengyWEMwYWdwMkNSSi1JRGhMNjluazJ2QkFCS080UExPUjFsSkdqc0M1WWhVdmFaSHBvZnhkaHdfUi1fakJDaTdIUWE5NjNqNTByczRiMk1nZVQ3MTJwdjBXWWI0YWl3VHF6YlhNUGtGc1Z6TXdFd1pHNXZJS1U2LVpubWxKcnluaWx4ODJ6aExUUQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQNUpjV1hwai03UGFieG1QUDZCUkI5My1hOU5Vb1JycGpKUzhaUVpQSmlBV0s3SlNjZ01WM25BQ3p4bHZ5RjUzVnJId1NuUnlkbklLYmhWQ1VHY3hXS2loMnp4bjFwamJydUJyNnNmeEFDZ01LY1MzdWxGUzhOMzZhX0k5Q3p0RG5RNkFuS1lCamlmQVUxU0FobnN4YXQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
