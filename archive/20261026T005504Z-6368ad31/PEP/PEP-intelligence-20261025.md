# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:39:34.985804+00:00**
- AI status: **N/A: Groq application daily budget exhausted earlier in this run**
- AI model (configured): **rules-only** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 12, 'ai': 0, 'unknown': 11})
- AI model(s) actually used: **N/A (no successful AI classification call)**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 9 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 56.52%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 135.7700 |
| Return 1D (%) | -2.2041 |
| Return 1W (%) | 3.2550 |
| Return 1M (%) | 4.2941 |
| Return YTD (%) | -2.5202 |
| Return 1Y (%) | -6.7577 |
| Annualized volatility (%) | 21.1703 |
| Beta vs SPY | -0.2088 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | -0.2266 |
| Downside deviation (rf=0, %) | 14.5163 |
| Sortino (rf=0) | -0.3305 |
| Historical VaR 95% (1D, %) | 2.1996 |
| Historical ES 95% (1D, %) | 2.6716 |
| Correlation vs SPY | -0.1257 |
| Tracking error vs SPY (%) | 26.0483 |
| P/E (trailing) | 17.08 |
| P/B | 8.31 |
| EV/EBITDA | 11.79 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 15.72 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.88 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.89 |
| MA50 | 133.6677 |
| Close vs MA50 (%) | 1.5728 |
| MA200 | 143.7912 |
| Close vs MA200 (%) | -5.5783 |
| RSI (14, Wilder) | 59.8746 |
| MACD (12,26) | 0.8956 |
| MACD signal (9) | -0.5848 |
| MACD histogram | 1.4804 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 135.7700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.2041 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.2550 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.2941 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -2.5202 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -6.7577 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.1703 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.5163 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.3305 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1996 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6716 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1257 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.0483 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.2088 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.2266 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.7165 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.8830 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.8883 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.0780 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.8746 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.4804 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.5728 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -5.5783 -> Clearly below the moving-average trend level.

## TAILWINDS

### PepsiCo Stock (PEP) Rallies on News Its Beverage Deal with Taco Bell Has Been Extended
- Summary: PepsiCo Stock (PEP) Rallies on News Its Beverage Deal with Taco Bell Has Been Extended
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQMl9VUWdORGtkaWpETWEtdnJ4SHFodUFlNnNtSl9MV2R0NEJTbEUtQ1QySjVFUUM4MVZPaXdxSElDUi1oNkVYRkFFUk9vLVcyY2lTZk85LTFrQ05IOVdPT3A4ekhVWWlJSVpoMk5pZm9mT0MtR3Vob2RfNHFrb2I1b0xLdXdEaGlLNXFhN0VXYUF5WjBKbWJiSVUxZ3NxSXcyV2h6TTI3SGQwSWxOc0NQaTlubjI?oc=5>

### PEP Stock Gains After PepsiCo Locks In 11 More Years With Taco Bell Following KFC Loss To Coke
- Summary: PEP Stock Gains After PepsiCo Locks In 11 More Years With Taco Bell Following KFC Loss To Coke
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxQUGJXQ0NGOTJJM2lNc1FGZFVWclVndEt4NXBNZ2UxZmFteEhsd1JTWVMwVld5QmE5cDBTdm1uV3BCMnVNMzQ3Q3UxdUFmS3NRT1h0a0pVQm5vRV9OOUx0d1QxLTFPVER2UkpVcV85dDJqNXdSbjkwYnUtTDBaS3RFT2d5d1RDcTZLdWNnWWNkQUh5WEdIaGN0ZEU2SlFIbnF1NlRwbC1CMU5ydzQxVDdjMW5OMmcwZHdsWlRuOHFoaHRXY0wxek8zQXc2VDN3MTBqR3c2bXJCQ0FiYkpKREtvWmJJaTQzRUpoaHc?oc=5>

### PepsiCo Inc (PEP) Stock Up 3.1% and Still Undervalued -- GF Scor
- Summary: PepsiCo Inc (PEP) Stock Up 3.1% and Still Undervalued -- GF Scor
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNSU9USEEzOTVhWVhlbm8xelBIOGVRd2tFNmxGRTQ0THdiLVE1MXZLa2xwdDBDTzVwOVVnckN2cEhmOTZESFViUmNER2xCY2h2VUtNUzJKUHhjaFFtMUphQU92UXJmTDZpd3lxbi02Nk1rUTNodmF2NUlRbi13SFhtR1lrNFN2blpkNkg2OGhwVUh5T256enpIdnNfNXQ1NnVXaDhVUHhB?oc=5>

## HEADWINDS

### PepsiCo Stock Is Down 27% From Its High. Here’s What Q3 Earnings Need to Show
- Summary: PepsiCo Stock Is Down 27% From Its High. Here’s What Q3 Earnings Need to Show
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNbTNWZU83dXc4bjFKbllicUQyUi1EUURRcHZjR3I3bDlYa1VsSXJXR0lzaERRRVl0ekdYajlsRnEwa0h0b0RtLVVUdURUOVAwN0RQV0dISnZYMWU1Tm1LWVZYemprVjFpeG5ILXEyVElma1hmTkEtRkYzeGpocUhTZTg5RGdJV3g2WmNXN05McWozWWl4R1E?oc=5>

## CATALYSTS

### PepsiCo Pays More, Coca-Cola Looks Stronger. Which Dividend Wins for Retirement?
- Summary: PepsiCo Pays More, Coca-Cola Looks Stronger. Which Dividend Wins for Retirement?
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPNHNDNXNfQjBkU0xrcWp5STBoc1l1VFJXelVOVVJqSkJtUXhKa1d3MkR6c1JqLTkwZEtDVFJ2RFVpamw4a09SXzF6VFJRM1JodFJlQl9ESzhUNV9WalJvc3FfeFctb3E1OUs1Y2FXcmNmMHVtbGFxeFN5MDVfcFozMFBrS213RF9lUkp0RUk4MVNOSGVNdlNlMUlOcVFnX3dHdUpOMldWek5ZeTZ0WVp1WW1PMm52cVAxY0lvNjNB?oc=5>

### PepsiCo Renews US Partnership With Taco Bell Through 2036
- Summary: PepsiCo Renews US Partnership With Taco Bell Through 2036
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQdFhncENHdFJ1WG9OV2xTLW5ocGFWT2JNakRSM1gtbXp6UTFxNl95R2ZsZDZETEJoOGQ4NUVXQzlvZDl0bGd3UUFCRkNTc1dwUjIxSEp6SUN0RXdvN0R4cjFoVG5XMlN4TWQwVWw4MmIxTjV1WGM4aTVtWGdmNFQ5SEI0MTBVejBlUndrLWJrZlJ3NnktUzk0VFVXbGhxM3gw?oc=5>

### PepsiCo (PEP) Extends Its Global Beverage Partnership Through 2036
- Summary: PepsiCo (PEP) Extends Its Global Beverage Partnership Through 2036
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQQmxndWR4OVE5OElNMWZlanNGOWxEYWMtaTB2QVlGMmZGaXE3enBqakhlZ1pjX21yd2l1RGNKMHM4WVF2YWtaNjVkYU1wdW0wYnMxbFk5NS1TenRhZjJ4cmVFNTk2bzJGY1VXcXNwc1lmZDFUZHFEZ2dScUZ2REhLTjl4RlpPRW9GV3Bza0VzQlU5SDI5NFNyNWRHcl9YVzl5THc?oc=5>

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

### PepsiCo Yields 4%. Is Its Dividend Still Safe After Lowering Guidance?
- Summary: PepsiCo Yields 4%. Is Its Dividend Still Safe After Lowering Guidance?
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxOcUZjT1c0U1ZLcEszN2plV0FFWERYbDNWcm50Nzh1VF8tdkhWNXBmQnNLSTZmUXIxMjFZY2hHS1hyaDB0aDZWbGNpMkZPNWdEZjJMQXNyNmNMS0p3S3NSWng4a2VxVnU3MjZILW8tYThjaUpEbzJHTlpZMlo4eGFjX1pDekFwai1aQ3p1LVRkWXV4QzNrVHNxdDQyUjQ4YlFlcUV0RWhDSkx5ekJWcm00Qg?oc=5>

### PepsiCo Stock And Other Defensive Dividend Plays For Uncertain Markets
- Summary: PepsiCo Stock And Other Defensive Dividend Plays For Uncertain Markets
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxPTHFxRE5uZEVPMWZfNHF5cmZEdkpna01fZmFPYXpuZGFWc1BTVUNmZk5VWUg0WXN1aWNJQjkzUjZxbkdQZThzSzdkUDhpdFZnVlozUjRmR0FzMUh0enlWT1dpVl9mTDFjczkwUUl4bW9mMUNBb3VZMU1HcEJmY1cwLUlMUHlIQk9XeGVMVTh3SFRaa1I1STFSVmQxNk1sWXFodW9vbzRnZWNaRzFlcVNXR2pNUFFJakZWQ0dGSDJHMU5GT1llS21sUDZPRWdLeVpoOFRkemh30gHbAUFVX3lxTFAtc3Nvd3pkM3lOZWZqeDZDNjRWazF2ZW9GNm1rMkZIUWk2VEpGamFFSUhlTENxYzdxWTNmNVVXeEVyUzdxTGJLQ09tNGxzcEJ5TDJYd0VRS3FXWUpMaGpMRlFtZlRZSnRIM2FWZnNCelRiS0FYSzlXR2tEMGhxc1FZZGxjc2FZRl9JdU1nZER1aUxfU2hkSkJhVDVJeUJWaHFQbnc4Ymh4MVItOGZ0b1VGS1R5YVU1R0dObDF2ODM2UjdGUmM1VzFqSTRqcUFUX0taOXowaW82VTRvbw?oc=5>

## RISKS

N/A: Groq application daily budget exhausted earlier in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **17.08** | **8.31** | **11.79** | **5.60** | **185,019,367,424.00 USD** | **-6.76** |
| KO | 27.84 | 11.04 | 25.23 | 6.70 | 398,889,320,448.00 USD | 36.08 |
| MNST | 42.77 | 9.66 | 29.71 | 20.20 | 90,488,602,624.00 USD | 32.18 |
| KDP | 35.03 | 1.89 | 18.27 | 75.60 | 47,193,444,352.00 USD | 29.89 |

Peers fetched as_of: 2026-10-25; PEP reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

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

- https://news.google.com/rss/articles/CBMitAFBVV95cUxQMl9VUWdORGtkaWpETWEtdnJ4SHFodUFlNnNtSl9MV2R0NEJTbEUtQ1QySjVFUUM4MVZPaXdxSElDUi1oNkVYRkFFUk9vLVcyY2lTZk85LTFrQ05IOVdPT3A4ekhVWWlJSVpoMk5pZm9mT0MtR3Vob2RfNHFrb2I1b0xLdXdEaGlLNXFhN0VXYUF5WjBKbWJiSVUxZ3NxSXcyV2h6TTI3SGQwSWxOc0NQaTlubjI?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxQUGJXQ0NGOTJJM2lNc1FGZFVWclVndEt4NXBNZ2UxZmFteEhsd1JTWVMwVld5QmE5cDBTdm1uV3BCMnVNMzQ3Q3UxdUFmS3NRT1h0a0pVQm5vRV9OOUx0d1QxLTFPVER2UkpVcV85dDJqNXdSbjkwYnUtTDBaS3RFT2d5d1RDcTZLdWNnWWNkQUh5WEdIaGN0ZEU2SlFIbnF1NlRwbC1CMU5ydzQxVDdjMW5OMmcwZHdsWlRuOHFoaHRXY0wxek8zQXc2VDN3MTBqR3c2bXJCQ0FiYkpKREtvWmJJaTQzRUpoaHc?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNSU9USEEzOTVhWVhlbm8xelBIOGVRd2tFNmxGRTQ0THdiLVE1MXZLa2xwdDBDTzVwOVVnckN2cEhmOTZESFViUmNER2xCY2h2VUtNUzJKUHhjaFFtMUphQU92UXJmTDZpd3lxbi02Nk1rUTNodmF2NUlRbi13SFhtR1lrNFN2blpkNkg2OGhwVUh5T256enpIdnNfNXQ1NnVXaDhVUHhB?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNbTNWZU83dXc4bjFKbllicUQyUi1EUURRcHZjR3I3bDlYa1VsSXJXR0lzaERRRVl0ekdYajlsRnEwa0h0b0RtLVVUdURUOVAwN0RQV0dISnZYMWU1Tm1LWVZYemprVjFpeG5ILXEyVElma1hmTkEtRkYzeGpocUhTZTg5RGdJV3g2WmNXN05McWozWWl4R1E?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPNHNDNXNfQjBkU0xrcWp5STBoc1l1VFJXelVOVVJqSkJtUXhKa1d3MkR6c1JqLTkwZEtDVFJ2RFVpamw4a09SXzF6VFJRM1JodFJlQl9ESzhUNV9WalJvc3FfeFctb3E1OUs1Y2FXcmNmMHVtbGFxeFN5MDVfcFozMFBrS213RF9lUkp0RUk4MVNOSGVNdlNlMUlOcVFnX3dHdUpOMldWek5ZeTZ0WVp1WW1PMm52cVAxY0lvNjNB?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQdFhncENHdFJ1WG9OV2xTLW5ocGFWT2JNakRSM1gtbXp6UTFxNl95R2ZsZDZETEJoOGQ4NUVXQzlvZDl0bGd3UUFCRkNTc1dwUjIxSEp6SUN0RXdvN0R4cjFoVG5XMlN4TWQwVWw4MmIxTjV1WGM4aTVtWGdmNFQ5SEI0MTBVejBlUndrLWJrZlJ3NnktUzk0VFVXbGhxM3gw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQQmxndWR4OVE5OElNMWZlanNGOWxEYWMtaTB2QVlGMmZGaXE3enBqakhlZ1pjX21yd2l1RGNKMHM4WVF2YWtaNjVkYU1wdW0wYnMxbFk5NS1TenRhZjJ4cmVFNTk2bzJGY1VXcXNwc1lmZDFUZHFEZ2dScUZ2REhLTjl4RlpPRW9GV3Bza0VzQlU5SDI5NFNyNWRHcl9YVzl5THc?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOMTFrLUlBM0tCbFd2R1B3MFVTNl9seUlwYlRTMGh1azBOZEpodG1MT1dzYUo1UkttZ2FYeWU4eUJReGg5TlU5bVVCbVJjNTJRYndpUm5YTWdXOGpBMHdqNHJwRjk4QzJZQzBOdTVCa3ViWHdTVmR4ZDlyRjc5MU01UTRLS2I4SnV4VFM4aEctX1NLTFhaMHFDMXNFaGpra2RIbGc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOWHNSYTc3bFlvN0F5OHhUYUJvUEFqbWpwWllmZmh5NHhraFpmdkphMFZrTnB5dzNVaXlLMktuc1BuLXI0R3dXMXlQcEFxRUFFQ2phNEFHREN3bHZBcS04eENNNG5lU3VCeGlNNXBLMGdINFE0bFBqY0l6RTJoYkItb0dxOXkwSFFrRXNlc3IxZVB4cHZnb0ktUThGeGxDYzA?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQbERnRTlldWdUY2NTMHVQWi1Xa0F4Yy1iVjFwTGhXZ2J6X3JYa2hWVHVVNWIySFczZmJUV1pZZ3pMWXV6eFJBaThiUlVUVGtoaHRZZGZIcFZlRVdRbFcxU2M4bThpTTRSdS1TTmVWaUNPUjVHd3FhUVNBb1BJaVZ1OE9ScVVxUUg1S1l5aUJxTzdibGlqSnc4djlkNXpLeUF0bmZN?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxOTlZNMVVha1lxcTRCMlV6UGR2SlltekgzQWt1UGlBX19WLVl1T0tOeHJ3SnZkVE5SVVJnRGh0bEZXUkxwVkFzYmtRem1VT0JmN19UeTRuOVl3WDdMaDZBTVBwa0hESmk2ckV3X0kyNUFHLW5TT2RQNmFVWThBVkdvRGttRG1TRVllY2kxRVd2cVJnM2VtcEFld3RGUjBoZ3dFZTc1T1NaeGpWNXltZ3VxdThZd1AxejlTQ05oLW5qUWlpNHR6WUpzanhpMm5qNVE?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxOcUZjT1c0U1ZLcEszN2plV0FFWERYbDNWcm50Nzh1VF8tdkhWNXBmQnNLSTZmUXIxMjFZY2hHS1hyaDB0aDZWbGNpMkZPNWdEZjJMQXNyNmNMS0p3S3NSWng4a2VxVnU3MjZILW8tYThjaUpEbzJHTlpZMlo4eGFjX1pDekFwai1aQ3p1LVRkWXV4QzNrVHNxdDQyUjQ4YlFlcUV0RWhDSkx5ekJWcm00Qg?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxPTHFxRE5uZEVPMWZfNHF5cmZEdkpna01fZmFPYXpuZGFWc1BTVUNmZk5VWUg0WXN1aWNJQjkzUjZxbkdQZThzSzdkUDhpdFZnVlozUjRmR0FzMUh0enlWT1dpVl9mTDFjczkwUUl4bW9mMUNBb3VZMU1HcEJmY1cwLUlMUHlIQk9XeGVMVTh3SFRaa1I1STFSVmQxNk1sWXFodW9vbzRnZWNaRzFlcVNXR2pNUFFJakZWQ0dGSDJHMU5GT1llS21sUDZPRWdLeVpoOFRkemh30gHbAUFVX3lxTFAtc3Nvd3pkM3lOZWZqeDZDNjRWazF2ZW9GNm1rMkZIUWk2VEpGamFFSUhlTENxYzdxWTNmNVVXeEVyUzdxTGJLQ09tNGxzcEJ5TDJYd0VRS3FXWUpMaGpMRlFtZlRZSnRIM2FWZnNCelRiS0FYSzlXR2tEMGhxc1FZZGxjc2FZRl9JdU1nZER1aUxfU2hkSkJhVDVJeUJWaHFQbnc4Ymh4MVItOGZ0b1VGS1R5YVU1R0dObDF2ODM2UjdGUmM1VzFqSTRqcUFUX0taOXowaW82VTRvbw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
