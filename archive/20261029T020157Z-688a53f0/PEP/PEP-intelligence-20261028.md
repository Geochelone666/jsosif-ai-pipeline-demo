# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:26:04.468236+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 11, 'ai': 10, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 9 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 60.87%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 132.6300 |
| Return 1D (%) | -0.6517 |
| Return 1W (%) | -1.5367 |
| Return 1M (%) | 3.2140 |
| Return YTD (%) | -4.7747 |
| Return 1Y (%) | -8.0708 |
| Annualized volatility (%) | 21.1535 |
| Beta vs SPY | -0.2200 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | -0.2943 |
| Downside deviation (rf=0, %) | 14.5116 |
| Sortino (rf=0) | -0.4289 |
| Historical VaR 95% (1D, %) | 2.1996 |
| Historical ES 95% (1D, %) | 2.6716 |
| Correlation vs SPY | -0.1321 |
| Tracking error vs SPY (%) | 26.0732 |
| P/E (trailing) | 16.79 |
| P/B | 8.12 |
| EV/EBITDA | 11.56 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 15.35 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.88 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 5.00 |
| MA50 | 133.4049 |
| Close vs MA50 (%) | -0.5809 |
| MA200 | 143.7581 |
| Close vs MA200 (%) | -7.7408 |
| RSI (14, Wilder) | 51.5244 |
| MACD (12,26) | 0.9290 |
| MACD signal (9) | 0.1889 |
| MACD histogram | 0.7401 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 132.6300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.6517 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.5367 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.2140 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -4.7747 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -8.0708 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.1535 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.5116 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.4289 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1996 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6716 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1321 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.0732 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.2200 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.2943 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.3530 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.8830 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.0040 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.7886 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 51.5244 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7401 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.5809 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -7.7408 -> Clearly below the moving-average trend level.

## TAILWINDS

### PEP Stock Gains After PepsiCo Locks In 11 More Years With Taco Bell Following KFC Loss To Coke
- Summary: PEP Stock Gains After PepsiCo Locks In 11 More Years With Taco Bell Following KFC Loss To Coke
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOTXdTWFNzNmhxOU9ManFlWjVDVUI0LUlIaFdpaFJvTzkzampMcjhZbS1YNHRnNGVDemt1N3NEbFhodC1jRGhKTTN2ZWdPaGRPSXFWR2pIdF82UTNpdzF4MWFySnFBZ0RscmJibnpXSmtydUtrVElpdUNoMk9KTGgwUkNjd180VzdqVFJDcVdGVnR2ak54cXFnQ3Bn?oc=5>

### PepsiCo Inc (PEP) Stock Up 3.1% and Still Undervalued -- GF Scor
- Summary: PepsiCo Inc (PEP) Stock Up 3.1% and Still Undervalued -- GF Scor
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNSU9USEEzOTVhWVhlbm8xelBIOGVRd2tFNmxGRTQ0THdiLVE1MXZLa2xwdDBDTzVwOVVnckN2cEhmOTZESFViUmNER2xCY2h2VUtNUzJKUHhjaFFtMUphQU92UXJmTDZpd3lxbi02Nk1rUTNodmF2NUlRbi13SFhtR1lrNFN2blpkNkg2OGhwVUh5T256enpIdnNfNXQ1NnVXaDhVUHhB?oc=5>

### Is PepsiCo Stock Stronger Than It Looks?
- Summary: Questioning PepsiCo’s stock strength suggests potential undervaluation and future upside for investors.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQdGI1al9tWm5HV2dzcWcxOWtxbWg5Rm9rMlFSWldnZG9tb3Nib2VNZXAxa0RXVVlxcnp3am9DN1J6TmFYNzBVazVaUmh0cnAyZlJSVWRyNVhuVHhpaXJKVURfWGllQjVmZnhhM09OUkVVdTFHWDBfcmIxRUIwd0FKNTFiNV9fZ2VQU2NGcncyYnRCV2dsNTQyQ1E4RVI3UUxS?oc=5>

### Coca-Cola Yields Just 2.2% Compared to 4.3% for PepsiCo. Here's the Better Dividend King Stock for Generating Long-Term Passive Income.
- Summary: PepsiCo offers a higher dividend yield than Coca-Cola, positioning it as a more attractive income stock for long-term investors.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxON0NhSHRndFp3TWVQZlFmNWU2Yy13LThiTmd5OUdqRFllLTI1UXR0aEJBVVhXeVVmSDlTb0F4M19lR3prYVVvRHFpZGh0OXNGbk9Qc01FRWIybVJyTFhpMlJwa1YxUUpZQmVKSnl5ZG1lRTYwQUoyY0I0QTNMTG92Z3hndmFZbUZ3dGdiUnRCdlJ5Z1E?oc=5>

### Unusual Options Volume Report: PepsiCo Stock
- Summary: Reports of higher-than-normal options trading activity for PepsiCo, indicating increased market interest.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPOUF0bmJkQ1VJZXZkeG5WRk9YUWllcDh1NERKc1JXTEZ0VG1RVkFmR21XN01KRGh5aTNKbjRJWnNqaVc0UndnbzNSZDR1M3ZQSFJtUG5DN1NEaHJQNGNtSFNuWVJFcUVmQXJfWjZ1NHZmcVM4X2t1c2EycGhCMFRlTlFfSDhla09YbV8tM3FmeVpjVDM2SG9kVC1yOTJtS0hPY2lHUUh3?oc=5>

### Here is What to Know Beyond Why PepsiCo, Inc. (PEP) is a Trending Stock
- Summary: Overview of factors driving PepsiCo's current popularity among investors.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPcldmTTBGLW1vRFcycXJNRzZzQlZVbEs4eWYxQVVLX2ZTUmlTMlg5MG1JekdjUGpLYnFTeFo2V1BCN1gzMUlqWkdnajY3R01VZm1uNFM4TTlqRTM3aldxVjNUbUtXVW50UkhyQlA2VmF1X2NiTVZ3aTZDMkhJRGhiWTRZRHh4LWRGa291RVYxX01xM2tNS3E4?oc=5>

### PepsiCo (PEP) Stock May Be Worth More On Its Supply Chain Reset
- Summary: Analysts suggest supply chain reset could boost PepsiCo’s valuation.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNcWJTVndPbTdlcEFvZ1JyZmJPSUVpR1NKSGFOeHFiWUlzRXVGQTd6akxfbmQzUG54Q0VnR2pQVVVQRG5zODhIRHFrZEZsLXRMSGQzeF9DcUloRVBBUnJ5MlRaeEpRYnpQbmVUZl9BWjd2TkRiS1ZmVjFkd2h3NFNtUEVvQW1feGppS2JTZkUxZ2NNcTNhMVBHTi1TalpLVEVQQjZmOUFwSk1jRFoyV2pDaUhHLUpkNE5QUkIxSjNYbmwwRUNtbnNZUy1UMElTOExQX29XRtIB2gFBVV95cUxOaUR5dGVLRGxsbkJHS3dZNFV6T2tocE12Qk5LVUotTGR3WTFySWtJQm55SDV3ZXo0YUV1LThWNTY2V0ZiMm5rZGFuTms2WXFxb19kaVg2RHh6OEo5M3FtVmZqMmxGU296YnhjNmx0cEFWUV84cmpKLTY4dEVEMUFGbC1WRXZNbFg1LWlibzh2Unp3T2xLOE9sTlBQYlQtMm8xMi11UU1IRXh0bzNMb3psQ2VUMTZoQjkwN19IZkd5ZS1hZFFVa3lUbEtjWERIU21PODMtM21GVFNLZw?oc=5>

### PepsiCo's North America Reset: Can Cost Cuts Restore Growth?
- Summary: Cost-cutting plan in North America may revive growth prospects.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQckpKSHpXZzJlZE9kVGUxdk1qbW5aY25LdVQzd2NFWnQySVpDRXZhQmZsRjNEd3hKby1za1lfY0FIb2dZRllIUlZHRHZBeGJJYktyZHRUV0k0SWhJWlhaei15RHNUMzBjd282cUVWMVZUTkw0NmJXT3RKM0xYZ0VjWGEySnRKUi1mbms4YXhQMXZMMW9ORFJ1eE9rR19USENtN1dLY3NNcl9hV0J6RFJ0MDlQT1o?oc=5>

### Want Income for Life? PepsiCo Yields 4.3% and Has the Kind of Competitive Moat That Makes the Income Durable.
- Summary: PepsiCo offers a 4.3% yield, indicating stable income potential.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOWU9xcFM1d2NYWVJwZXh1YnE3NDFDVWQ4YXpyazgtX1RqeWVVa1NiMVNvVWdJX21XbUkxRTF1ZEpMSXNySFBmNzFFSWdOV2o4eWE3MDd5Q1FfUm9Sdk9JUnFYY2NoUnkyaTJBUkNpSFhkLVhLRnJULU1EMFVzX1hkRzNvcThzaTlIcVdjM0hzNGx2NlpjSkRJMURBczk?oc=5>

## HEADWINDS

No items in this run

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

### PepsiCo Renews Partnership With Taco Bell for 11 More Years. Here’s What Investors Need to Know.
- Summary: PepsiCo Renews Partnership With Taco Bell for 11 More Years. Here’s What Investors Need to Know.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQbERnRTlldWdUY2NTMHVQWi1Xa0F4Yy1iVjFwTGhXZ2J6X3JYa2hWVHVVNWIySFczZmJUV1pZZ3pMWXV6eFJBaThiUlVUVGtoaHRZZGZIcFZlRVdRbFcxU2M4bThpTTRSdS1TTmVWaUNPUjVHd3FhUVNBb1BJaVZ1OE9ScVVxUUg1S1l5aUJxTzdibGlqSnc4djlkNXpLeUF0bmZN?oc=5>

### PepsiCo Renews Taco Bell Beverage Deal Through 2036 After Losing KFC to Coca-Cola
- Summary: PepsiCo Renews Taco Bell Beverage Deal Through 2036 After Losing KFC to Coca-Cola
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOWHNSYTc3bFlvN0F5OHhUYUJvUEFqbWpwWllmZmh5NHhraFpmdkphMFZrTnB5dzNVaXlLMktuc1BuLXI0R3dXMXlQcEFxRUFFQ2phNEFHREN3bHZBcS04eENNNG5lU3VCeGlNNXBLMGdINFE0bFBqY0l6RTJoYkItb0dxOXkwSFFrRXNlc3IxZVB4cHZnb0ktUThGeGxDYzA?oc=5>

### PepsiCo Yields 4%. Is Its Dividend Still Safe After Lowering Guidance?
- Summary: PepsiCo Yields 4%. Is Its Dividend Still Safe After Lowering Guidance?
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxOcUZjT1c0U1ZLcEszN2plV0FFWERYbDNWcm50Nzh1VF8tdkhWNXBmQnNLSTZmUXIxMjFZY2hHS1hyaDB0aDZWbGNpMkZPNWdEZjJMQXNyNmNMS0p3S3NSWng4a2VxVnU3MjZILW8tYThjaUpEbzJHTlpZMlo4eGFjX1pDekFwai1aQ3p1LVRkWXV4QzNrVHNxdDQyUjQ4YlFlcUV0RWhDSkx5ekJWcm00Qg?oc=5>

### PepsiCo Pays More, Coca-Cola Looks Stronger. Which Dividend Wins for Retirement?
- Summary: PepsiCo Pays More, Coca-Cola Looks Stronger. Which Dividend Wins for Retirement?
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPNHNDNXNfQjBkU0xrcWp5STBoc1l1VFJXelVOVVJqSkJtUXhKa1d3MkR6c1JqLTkwZEtDVFJ2RFVpamw4a09SXzF6VFJRM1JodFJlQl9ESzhUNV9WalJvc3FfeFctb3E1OUs1Y2FXcmNmMHVtbGFxeFN5MDVfcFozMFBrS213RF9lUkp0RUk4MVNOSGVNdlNlMUlOcVFnX3dHdUpOMldWek5ZeTZ0WVp1WW1PMm52cVAxY0lvNjNB?oc=5>

### PepsiCo renews deal to supply Taco Bell
- Summary: PepsiCo renews deal to supply Taco Bell
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxPVU9iOFVraVpfUlU2VDVOdWtSU0NHMi1UcnFIRzRVVTIxMUt3S2g4ZXFZaDlocXN6T2J6aDU5cm5zRTdnMlZJOVhVczQxNkVpOHNjUTVIdWJhWlRUbWY5cWhxTWdOaC04M2RXekdxN2h3dHRSSmM4TWVaX0hoSy01VlBUTQ?oc=5>

### PepsiCo (PEP) Renews Taco Bell Deal, Is The Stock A Bargain?
- Summary: PepsiCo renews its partnership with Taco Bell, extending the franchise agreement and potentially boosting revenue streams.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNWGNGNndxNnhNR0NTQ2Fod2UtaTFnWXFpTm01ZUtMU1UtYnBRZk9BU0FDUWR0N3cwbjY0ZTMwMDUwNGZZYndVTnFhcHN0QzBSUTdlWndZQ1VQTDEwZ0E1N1ZYWDRSMWN6QjNRdjRsd1RBZC11MEc1bmhCYTZrcFR0cjFaVDBVTnc1dmcxR2JlMFdlbXBsSlNBNA?oc=5>

### PepsiCo Stock Could Be a Contrarian Opportunity if This One Thing Improves
- Summary: Potential upside if a key metric improves, suggesting a contrarian buying opportunity.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPbkxqNzVLZ0YtNnZxQ254MDBZdkpmTmZMWEtJSVJaREhRVXZ1WW9Lek9DWXZLWWRGUVJ5eUNrR1MxdXVmZTVqVWZ5c0hQTFd4RXVGbVVFejFsbkE5Q1FhWjVWcDg0VVpJQmM0SGN3eE9MQ21hUmgwQU14VXpfOG45Zks4VDJoXzB4VDZ5Tm5BaEtLbmRUcmVSLXNNVDRzTFhVejQtZ2RBdV9pbVk?oc=5>

## RISKS

### PepsiCo: Inflation Looms, But Shares Look Attractively Valued (NASDAQ:PEP)
- Summary: Inflation concerns may weigh on PepsiCo, despite attractive valuation.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNRWQ5U1BBa215T1BpT3RrZGlyV1RrNmVsQ2k4X0JMbFFDUFNVVVFBVEFQRmkzaG1ZNVNiUFdKS0lvTzBBd2lKTGhUc1lWRU42V2J6N1lpYVhCV2M5QmR6UUlrb0pIWnBhMVJfX1ctYWsyR183SWJZU3RXQWFLazkwUDRWUzZsaGpmN3k3RHAtRDh1NFpmd0FPa0Z1OG5FS3RlS0E?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **16.79** | **8.12** | **11.56** | **5.60** | **180,740,358,144.00 USD** | **-8.07** |
| KO | 27.55 | 10.92 | 23.94 | 7.40 | 394,581,114,880.00 USD | 34.22 |
| MNST | 42.28 | 9.55 | 29.36 | 20.20 | 89,450,307,584.00 USD | 31.74 |
| KDP | 35.28 | 1.90 | 18.34 | 75.60 | 47,533,654,016.00 USD | 24.93 |

Peers fetched as_of: 2026-10-28; PEP reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

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
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQdGI1al9tWm5HV2dzcWcxOWtxbWg5Rm9rMlFSWldnZG9tb3Nib2VNZXAxa0RXVVlxcnp3am9DN1J6TmFYNzBVazVaUmh0cnAyZlJSVWRyNVhuVHhpaXJKVURfWGllQjVmZnhhM09OUkVVdTFHWDBfcmIxRUIwd0FKNTFiNV9fZ2VQU2NGcncyYnRCV2dsNTQyQ1E4RVI3UUxS?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxON0NhSHRndFp3TWVQZlFmNWU2Yy13LThiTmd5OUdqRFllLTI1UXR0aEJBVVhXeVVmSDlTb0F4M19lR3prYVVvRHFpZGh0OXNGbk9Qc01FRWIybVJyTFhpMlJwa1YxUUpZQmVKSnl5ZG1lRTYwQUoyY0I0QTNMTG92Z3hndmFZbUZ3dGdiUnRCdlJ5Z1E?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPOUF0bmJkQ1VJZXZkeG5WRk9YUWllcDh1NERKc1JXTEZ0VG1RVkFmR21XN01KRGh5aTNKbjRJWnNqaVc0UndnbzNSZDR1M3ZQSFJtUG5DN1NEaHJQNGNtSFNuWVJFcUVmQXJfWjZ1NHZmcVM4X2t1c2EycGhCMFRlTlFfSDhla09YbV8tM3FmeVpjVDM2SG9kVC1yOTJtS0hPY2lHUUh3?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPcldmTTBGLW1vRFcycXJNRzZzQlZVbEs4eWYxQVVLX2ZTUmlTMlg5MG1JekdjUGpLYnFTeFo2V1BCN1gzMUlqWkdnajY3R01VZm1uNFM4TTlqRTM3aldxVjNUbUtXVW50UkhyQlA2VmF1X2NiTVZ3aTZDMkhJRGhiWTRZRHh4LWRGa291RVYxX01xM2tNS3E4?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNcWJTVndPbTdlcEFvZ1JyZmJPSUVpR1NKSGFOeHFiWUlzRXVGQTd6akxfbmQzUG54Q0VnR2pQVVVQRG5zODhIRHFrZEZsLXRMSGQzeF9DcUloRVBBUnJ5MlRaeEpRYnpQbmVUZl9BWjd2TkRiS1ZmVjFkd2h3NFNtUEVvQW1feGppS2JTZkUxZ2NNcTNhMVBHTi1TalpLVEVQQjZmOUFwSk1jRFoyV2pDaUhHLUpkNE5QUkIxSjNYbmwwRUNtbnNZUy1UMElTOExQX29XRtIB2gFBVV95cUxOaUR5dGVLRGxsbkJHS3dZNFV6T2tocE12Qk5LVUotTGR3WTFySWtJQm55SDV3ZXo0YUV1LThWNTY2V0ZiMm5rZGFuTms2WXFxb19kaVg2RHh6OEo5M3FtVmZqMmxGU296YnhjNmx0cEFWUV84cmpKLTY4dEVEMUFGbC1WRXZNbFg1LWlibzh2Unp3T2xLOE9sTlBQYlQtMm8xMi11UU1IRXh0bzNMb3psQ2VUMTZoQjkwN19IZkd5ZS1hZFFVa3lUbEtjWERIU21PODMtM21GVFNLZw?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQckpKSHpXZzJlZE9kVGUxdk1qbW5aY25LdVQzd2NFWnQySVpDRXZhQmZsRjNEd3hKby1za1lfY0FIb2dZRllIUlZHRHZBeGJJYktyZHRUV0k0SWhJWlhaei15RHNUMzBjd282cUVWMVZUTkw0NmJXT3RKM0xYZ0VjWGEySnRKUi1mbms4YXhQMXZMMW9ORFJ1eE9rR19USENtN1dLY3NNcl9hV0J6RFJ0MDlQT1o?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOWU9xcFM1d2NYWVJwZXh1YnE3NDFDVWQ4YXpyazgtX1RqeWVVa1NiMVNvVWdJX21XbUkxRTF1ZEpMSXNySFBmNzFFSWdOV2o4eWE3MDd5Q1FfUm9Sdk9JUnFYY2NoUnkyaTJBUkNpSFhkLVhLRnJULU1EMFVzX1hkRzNvcThzaTlIcVdjM0hzNGx2NlpjSkRJMURBczk?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQc1g1TkNWMjVsY2lJOUo4WFZPbkgyZFZOV1lLWUlnT3ItRm5ZczZDSk5rRkpkNXAxNE9YYnVtOTZ0dXdCOU1yUjVyWEJqUExCMDlRUDc2TXE2R2lEVEVqM1ROVGU5RG5QVXFjRlFJempFSDhLcngwbmFYd2U3QlhNb0pEbEhyd0ZtNS1hX3hMNVdPT1hHTTZkYw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNZzY1UzBpLS14VFl2UVBpU1FJYXJJRU9BaTNibm9OQkFQQ3g5NTZBWVNOUk9xRHV5dVptYmJYYnlwa0RpYUpuVGZvTmNqV09YcUpWSXk4YjNVNDFub0hQcXJRMGwweHJRSTR5eHBRam9uQmNXdHdLLVp6X0M2R2Zlb3k1UjlzRzl2YUt0VVJaeGtLUmhrYUJUaENB?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQQmxndWR4OVE5OElNMWZlanNGOWxEYWMtaTB2QVlGMmZGaXE3enBqakhlZ1pjX21yd2l1RGNKMHM4WVF2YWtaNjVkYU1wdW0wYnMxbFk5NS1TenRhZjJ4cmVFNTk2bzJGY1VXcXNwc1lmZDFUZHFEZ2dScUZ2REhLTjl4RlpPRW9GV3Bza0VzQlU5SDI5NFNyNWRHcl9YVzl5THc?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQdFhncENHdFJ1WG9OV2xTLW5ocGFWT2JNakRSM1gtbXp6UTFxNl95R2ZsZDZETEJoOGQ4NUVXQzlvZDl0bGd3UUFCRkNTc1dwUjIxSEp6SUN0RXdvN0R4cjFoVG5XMlN4TWQwVWw4MmIxTjV1WGM4aTVtWGdmNFQ5SEI0MTBVejBlUndrLWJrZlJ3NnktUzk0VFVXbGhxM3gw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOMTFrLUlBM0tCbFd2R1B3MFVTNl9seUlwYlRTMGh1azBOZEpodG1MT1dzYUo1UkttZ2FYeWU4eUJReGg5TlU5bVVCbVJjNTJRYndpUm5YTWdXOGpBMHdqNHJwRjk4QzJZQzBOdTVCa3ViWHdTVmR4ZDlyRjc5MU01UTRLS2I4SnV4VFM4aEctX1NLTFhaMHFDMXNFaGpra2RIbGc?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQbERnRTlldWdUY2NTMHVQWi1Xa0F4Yy1iVjFwTGhXZ2J6X3JYa2hWVHVVNWIySFczZmJUV1pZZ3pMWXV6eFJBaThiUlVUVGtoaHRZZGZIcFZlRVdRbFcxU2M4bThpTTRSdS1TTmVWaUNPUjVHd3FhUVNBb1BJaVZ1OE9ScVVxUUg1S1l5aUJxTzdibGlqSnc4djlkNXpLeUF0bmZN?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxOTlZNMVVha1lxcTRCMlV6UGR2SlltekgzQWt1UGlBX19WLVl1T0tOeHJ3SnZkVE5SVVJnRGh0bEZXUkxwVkFzYmtRem1VT0JmN19UeTRuOVl3WDdMaDZBTVBwa0hESmk2ckV3X0kyNUFHLW5TT2RQNmFVWThBVkdvRGttRG1TRVllY2kxRVd2cVJnM2VtcEFld3RGUjBoZ3dFZTc1T1NaeGpWNXltZ3VxdThZd1AxejlTQ05oLW5qUWlpNHR6WUpzanhpMm5qNVE?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOWHNSYTc3bFlvN0F5OHhUYUJvUEFqbWpwWllmZmh5NHhraFpmdkphMFZrTnB5dzNVaXlLMktuc1BuLXI0R3dXMXlQcEFxRUFFQ2phNEFHREN3bHZBcS04eENNNG5lU3VCeGlNNXBLMGdINFE0bFBqY0l6RTJoYkItb0dxOXkwSFFrRXNlc3IxZVB4cHZnb0ktUThGeGxDYzA?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxOcUZjT1c0U1ZLcEszN2plV0FFWERYbDNWcm50Nzh1VF8tdkhWNXBmQnNLSTZmUXIxMjFZY2hHS1hyaDB0aDZWbGNpMkZPNWdEZjJMQXNyNmNMS0p3S3NSWng4a2VxVnU3MjZILW8tYThjaUpEbzJHTlpZMlo4eGFjX1pDekFwai1aQ3p1LVRkWXV4QzNrVHNxdDQyUjQ4YlFlcUV0RWhDSkx5ekJWcm00Qg?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPNHNDNXNfQjBkU0xrcWp5STBoc1l1VFJXelVOVVJqSkJtUXhKa1d3MkR6c1JqLTkwZEtDVFJ2RFVpamw4a09SXzF6VFJRM1JodFJlQl9ESzhUNV9WalJvc3FfeFctb3E1OUs1Y2FXcmNmMHVtbGFxeFN5MDVfcFozMFBrS213RF9lUkp0RUk4MVNOSGVNdlNlMUlOcVFnX3dHdUpOMldWek5ZeTZ0WVp1WW1PMm52cVAxY0lvNjNB?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxPVU9iOFVraVpfUlU2VDVOdWtSU0NHMi1UcnFIRzRVVTIxMUt3S2g4ZXFZaDlocXN6T2J6aDU5cm5zRTdnMlZJOVhVczQxNkVpOHNjUTVIdWJhWlRUbWY5cWhxTWdOaC04M2RXekdxN2h3dHRSSmM4TWVaX0hoSy01VlBUTQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNWGNGNndxNnhNR0NTQ2Fod2UtaTFnWXFpTm01ZUtMU1UtYnBRZk9BU0FDUWR0N3cwbjY0ZTMwMDUwNGZZYndVTnFhcHN0QzBSUTdlWndZQ1VQTDEwZ0E1N1ZYWDRSMWN6QjNRdjRsd1RBZC11MEc1bmhCYTZrcFR0cjFaVDBVTnc1dmcxR2JlMFdlbXBsSlNBNA?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPbkxqNzVLZ0YtNnZxQ254MDBZdkpmTmZMWEtJSVJaREhRVXZ1WW9Lek9DWXZLWWRGUVJ5eUNrR1MxdXVmZTVqVWZ5c0hQTFd4RXVGbVVFejFsbkE5Q1FhWjVWcDg0VVpJQmM0SGN3eE9MQ21hUmgwQU14VXpfOG45Zks4VDJoXzB4VDZ5Tm5BaEtLbmRUcmVSLXNNVDRzTFhVejQtZ2RBdV9pbVk?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNRWQ5U1BBa215T1BpT3RrZGlyV1RrNmVsQ2k4X0JMbFFDUFNVVVFBVEFQRmkzaG1ZNVNiUFdKS0lvTzBBd2lKTGhUc1lWRU42V2J6N1lpYVhCV2M5QmR6UUlrb0pIWnBhMVJfX1ctYWsyR183SWJZU3RXQWFLazkwUDRWUzZsaGpmN3k3RHAtRDh1NFpmd0FPa0Z1OG5FS3RlS0E?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
