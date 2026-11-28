# MCK Intelligence Report

- ticker: **MCK**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/MCK/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCK/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:23:31.851921+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 8, 'rule': 2, 'ai': 4, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/MCK** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 2}
- RSS source audit (metadata only, not article fact-checking): 8 unique headlines; 5 named publishers; 0 exact duplicates; 8 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1075.6600 |
| Return 1D (%) | -0.1541 |
| Return 1W (%) | 0.5826 |
| Return 1M (%) | 11.2345 |
| Return YTD (%) | 31.5254 |
| Return 1Y (%) | 22.2001 |
| Annualized volatility (%) | 31.8997 |
| Beta vs SPY | -0.1951 |
| Max drawdown (%) | -27.1691 |
| Sharpe (rf=0) | 0.7976 |
| Downside deviation (rf=0, %) | 18.5376 |
| Sortino (rf=0) | 1.3725 |
| Historical VaR 95% (1D, %) | 2.5993 |
| Historical ES 95% (1D, %) | 3.6083 |
| Correlation vs SPY | -0.0919 |
| Tracking error vs SPY (%) | 36.4870 |
| P/E (trailing) | 27.74 |
| P/B | -31.28 |
| EV/EBITDA | 18.05 |
| Revenue growth (%) | 7.60 |
| Forward P/E (estimate) | 20.51 |
| Gross margin (%) | 3.65 |
| Operating margin (%) | 1.59 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 5.96 |
| MA50 | 988.3656 |
| Close vs MA50 (%) | 8.8322 |
| MA200 | 881.1653 |
| Close vs MA200 (%) | 22.0724 |
| RSI (14, Wilder) | 59.5271 |
| MACD (12,26) | 23.8510 |
| MACD signal (9) | 29.1058 |
| MACD histogram | -5.2548 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCK': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1075.6600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.1541 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.5826 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 11.2345 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 31.5254 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 22.2001 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.8997 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.5376 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3725 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5993 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.6083 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0919 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 36.4870 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1951 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.1691 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7976 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.5053 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 3.6530 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 1.5900 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.9606 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.7446 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.5271 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -5.2548 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 8.8322 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 22.0724 -> Clearly above the moving-average trend level.

## TAILWINDS

### McKesson Keeps Gaining on Earnings Growth, Expanding Treatments
- Summary: McKesson Keeps Gaining on Earnings Growth, Expanding Treatments
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNR2VkeUVmU01KRXhFVVA5Q3hRRE16cGlZMEpoOUgyODZWTWdGYXJBVWFtZ2VULTRabWlkMThwWHFSeTRNLWsxR0p1WnZCQUNESFUzLVJveW9HV29yejN0cEc4ZmtoUk1naDJVQTc5RVpHdHczSm9pR0Y3MU9EUFZCRVJqOVdOSTd6TjFMbFVDb000ODc2blR6YjZsT2hWcVhDT3dRNk9uTjNINWVkblZXbnkyWQ?oc=5>

### Do Wall Street Analysts Like McKesson Stock?
- Summary: Wall Street analysts discuss McKesson’s stock performance and potential upside.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOc1h0YnprSHlCSXBvX3ZJYV8xTUhNMDlPRTFVSElBQ01pY01Jb3ozWFhkUll0MDlsNndoa05nWTBjYzBpV1pWSHBzZ2VLYU83N040WmFYZDhRZTU3akFoRVFLQWwxTnpEeExpLU5VTTlFenJxRU84dF9rYnZuS2VYMzA2eUdDMHN0QlV1Uko3b0VkUS1SdS16LVlqLXNIZkVWNHc?oc=5>

### Here's Why You Should Add McKesson Stock to Your Portfolio Now
- Summary: Positive outlook encouraging investment in McKesson.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxPV0xZUDFtbjMxVEFzaVpVTEFyM3dnLTZIZFNvS09QQzNnclB1MUZLbVBVOEY5VUN5empnLXBsUWpsRlR3ZmcwYTNXa1R2ckVEanUxcDFhZEFXN3BmRWdteTZEZXdBOHRoamJpNUxMNUlTMEhIcExPaU9nQTdPMXA1NlJ0RFBkRm1pekc2T2VFRHpVakpfdFd4OVZaSEZ5V0xTQk5jenl4dXA0VjZ3MFV3VkRGcF9KY19idk9LdWUxb0pxaWJfazdiRm5IQjhGZ285b3VLdm5FWEhNNnFQSlE?oc=5>

### Is McKesson (NYSE:MCK) Positioned For The Next Upswing?
- Summary: Suggests potential upside for McKesson stock.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPVXRURUVpNXNBRUx5a0NoRkhrZHVHb3hfV3ZrdS1LVW1GQlpIUkRsQ2F4b0IzN1o3R0xzNEJTdDk4bzBXU2p0TVdVTEhibmh3UUI3Mk5nb1QyLWxCZERFWC1ZQzRrWHNsYWxyamNFTVYwYjNSVHVVY0xMZWp0NUs2cVFFT3Z0XzdpVV82T3ZZNlVqX3hyME16dDJUbjl4dw?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### McKesson (MCK) Earnings Beat Keeps Fair Value In Focus
- Summary: McKesson (MCK) Earnings Beat Keeps Fair Value In Focus
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNYzU1bnRib3liX2lHXy1jc01jQ0czZ2w1RWJ4cmN0MWNwM1RtOFhrMlBoUDhfOHFOS0ZKVUF0Y2VFaGF4aWphdEt0YlF4OGJLcDJUQ1dDMTNZZlVrdkIwdGdYMHFuc3lBYUVZNTBuYTNfeG1sa2hTZ0kxUF94WjhOV2lGbWk1aDEzR0s4MGRLbUN0Yk1rVnpKNUZVRzdJa3ZQUk9QNWczUWpVamxtdDFsenZ4bTlpWk93MGfSAb8BQVVfeXFMUGVicUxJOXBzaWVjY2E1WS1GN3FSSFlyOVg1VDBFeFVTOVpIdElwZThMSXlublRvLW9iZjQzbkdZOXFzRC02UFFOalk4eXk5S0FGWTZ2aDhuTW11b3ZNRDNFb3J4WFBRSFY3eEFHRDRFT2NZM3pDMWpSUkVLLVNhU2k1MGFsUlVjRFBrSnZtRmR4SnRHeS01eWpBOWZUWmN0dXZKdDhURVZvMWtOZTVTbDVaZkQ1cE9VQU5hYU0tUzg?oc=5>

### Should Stronger Oncology Earnings Require Action From McKesson (MCK) Investors?
- Summary: Investors debate whether improved oncology earnings warrant strategic action.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOUlFDTE9CeW1vRGdkSTYtT29CUUdETjRxMkRtTHJuYTVQMlRzeE9zd3BJQWFnWkJ3X0JKbmVJUjBuNHZxYS1UNzk3Z3JUeDBDU3ZXd3BTLTA5Z2d1MUtjRGNITkp0QVpJU08xNEVRazAyTEVTaFFlcG95VDVVZWtYblkwTTdSdjNxZlhOZjB6cU5LVnlhYWUzZlR6WUlmMlpNM28xdXZyMG9naUJGVkRhcnZoZ2hpVFNiZjVjblZLTnlnTDFh0gHKAUFVX3lxTE1iQ3pfRGxFc05ZNGRuaGFIdGxlaHplMW02MjFiQldzRmlELTRnV0I4eTRNblVBZzl6cS1ESUlmcy1pNHpXaXR4emtnX3pHSmhtbjNmS1pUUVYyYkRKTWczYWthZFUxazFETVF6Y0RMTmhqeV9iNXRqWjA2YkNKYkdJSFFjb2NPNDg3NWwxLU1fR25nX1J6bURaZklDc0xyN3Y5c19YcVhYcTIzR1VLUGxTZTNnSExfbllSdkNTREpaSDNqYXl6TXI2RGc?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCK** | **27.74** | **-31.28** | **18.05** | **7.60** | **124,192,120,832.00 USD** | **22.20** |
| COR | 19.74 | 19.39 | 13.29 | 5.50 | 67,459,170,304.00 USD | -3.09 |
| CAH | 36.59 | -21.69 | 15.74 | 5.50 | 65,379,311,616.00 USD | 33.97 |
| CNC | 22.60 | 1.47 | 5.25 | 0.20 | 32,565,571,584.00 USD | 66.70 |

Peers fetched as_of: 2026-11-27; MCK reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 29,980,000,000.00 USD; period 2011-04-01/2011-06-30; fiscal year/reporting period 2011/Q1
- Net income (latest available single quarter): 1,218,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/927653/000092765326000281/mck-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiswFBVV95cUxNR2VkeUVmU01KRXhFVVA5Q3hRRE16cGlZMEpoOUgyODZWTWdGYXJBVWFtZ2VULTRabWlkMThwWHFSeTRNLWsxR0p1WnZCQUNESFUzLVJveW9HV29yejN0cEc4ZmtoUk1naDJVQTc5RVpHdHczSm9pR0Y3MU9EUFZCRVJqOVdOSTd6TjFMbFVDb000ODc2blR6YjZsT2hWcVhDT3dRNk9uTjNINWVkblZXbnkyWQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOc1h0YnprSHlCSXBvX3ZJYV8xTUhNMDlPRTFVSElBQ01pY01Jb3ozWFhkUll0MDlsNndoa05nWTBjYzBpV1pWSHBzZ2VLYU83N040WmFYZDhRZTU3akFoRVFLQWwxTnpEeExpLU5VTTlFenJxRU84dF9rYnZuS2VYMzA2eUdDMHN0QlV1Uko3b0VkUS1SdS16LVlqLXNIZkVWNHc?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxPV0xZUDFtbjMxVEFzaVpVTEFyM3dnLTZIZFNvS09QQzNnclB1MUZLbVBVOEY5VUN5empnLXBsUWpsRlR3ZmcwYTNXa1R2ckVEanUxcDFhZEFXN3BmRWdteTZEZXdBOHRoamJpNUxMNUlTMEhIcExPaU9nQTdPMXA1NlJ0RFBkRm1pekc2T2VFRHpVakpfdFd4OVZaSEZ5V0xTQk5jenl4dXA0VjZ3MFV3VkRGcF9KY19idk9LdWUxb0pxaWJfazdiRm5IQjhGZ285b3VLdm5FWEhNNnFQSlE?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPVXRURUVpNXNBRUx5a0NoRkhrZHVHb3hfV3ZrdS1LVW1GQlpIUkRsQ2F4b0IzN1o3R0xzNEJTdDk4bzBXU2p0TVdVTEhibmh3UUI3Mk5nb1QyLWxCZERFWC1ZQzRrWHNsYWxyamNFTVYwYjNSVHVVY0xMZWp0NUs2cVFFT3Z0XzdpVV82T3ZZNlVqX3hyME16dDJUbjl4dw?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNYzU1bnRib3liX2lHXy1jc01jQ0czZ2w1RWJ4cmN0MWNwM1RtOFhrMlBoUDhfOHFOS0ZKVUF0Y2VFaGF4aWphdEt0YlF4OGJLcDJUQ1dDMTNZZlVrdkIwdGdYMHFuc3lBYUVZNTBuYTNfeG1sa2hTZ0kxUF94WjhOV2lGbWk1aDEzR0s4MGRLbUN0Yk1rVnpKNUZVRzdJa3ZQUk9QNWczUWpVamxtdDFsenZ4bTlpWk93MGfSAb8BQVVfeXFMUGVicUxJOXBzaWVjY2E1WS1GN3FSSFlyOVg1VDBFeFVTOVpIdElwZThMSXlublRvLW9iZjQzbkdZOXFzRC02UFFOalk4eXk5S0FGWTZ2aDhuTW11b3ZNRDNFb3J4WFBRSFY3eEFHRDRFT2NZM3pDMWpSUkVLLVNhU2k1MGFsUlVjRFBrSnZtRmR4SnRHeS01eWpBOWZUWmN0dXZKdDhURVZvMWtOZTVTbDVaZkQ1cE9VQU5hYU0tUzg?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOUlFDTE9CeW1vRGdkSTYtT29CUUdETjRxMkRtTHJuYTVQMlRzeE9zd3BJQWFnWkJ3X0JKbmVJUjBuNHZxYS1UNzk3Z3JUeDBDU3ZXd3BTLTA5Z2d1MUtjRGNITkp0QVpJU08xNEVRazAyTEVTaFFlcG95VDVVZWtYblkwTTdSdjNxZlhOZjB6cU5LVnlhYWUzZlR6WUlmMlpNM28xdXZyMG9naUJGVkRhcnZoZ2hpVFNiZjVjblZLTnlnTDFh0gHKAUFVX3lxTE1iQ3pfRGxFc05ZNGRuaGFIdGxlaHplMW02MjFiQldzRmlELTRnV0I4eTRNblVBZzl6cS1ESUlmcy1pNHpXaXR4emtnX3pHSmhtbjNmS1pUUVYyYkRKTWczYWthZFUxazFETVF6Y0RMTmhqeV9iNXRqWjA2YkNKYkdJSFFjb2NPNDg3NWwxLU1fR25nX1J6bURaZklDc0xyN3Y5c19YcVhYcTIzR1VLUGxTZTNnSExfbllSdkNTREpaSDNqYXl6TXI2RGc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
