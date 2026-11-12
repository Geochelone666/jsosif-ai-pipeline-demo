# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:52:47.629259+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 12, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 19 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 20.83%; oldest publication 2026-11-07

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 552.9000 |
| Return 1D (%) | 7.3155 |
| Return 1W (%) | 13.1184 |
| Return 1M (%) | -9.0774 |
| Return YTD (%) | 158.1715 |
| Return 1Y (%) | 132.7804 |
| Annualized volatility (%) | 73.2912 |
| Beta vs SPY | 3.4353 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.5237 |
| Downside deviation (rf=0, %) | 47.1284 |
| Sortino (rf=0) | 2.3696 |
| Historical VaR 95% (1D, %) | 6.3184 |
| Historical ES 95% (1D, %) | 9.4746 |
| Correlation vs SPY | 0.6435 |
| Tracking error vs SPY (%) | 65.3076 |
| P/E (trailing) | 110.14 |
| P/B | 13.26 |
| EV/EBITDA | 80.79 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 31.26 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 17.82 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 0.81 |
| MA50 | 550.4294 |
| Close vs MA50 (%) | 0.4489 |
| MA200 | 420.0459 |
| Close vs MA200 (%) | 31.6285 |
| RSI (14, Wilder) | 53.6282 |
| MACD (12,26) | -17.6306 |
| MACD signal (9) | -19.6785 |
| MACD histogram | 2.0478 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 552.9000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 7.3155 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 13.1184 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -9.0774 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 158.1715 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 132.7804 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 73.2912 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 47.1284 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.3696 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.3184 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.4746 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6435 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 65.3076 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4353 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.5237 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 31.2559 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.8113 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 110.1394 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.6282 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.0478 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.4489 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 31.6285 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD Stock Surges on Expanded Partnership With Google. What Comes Next.
- Summary: AMD Stock Surges on Expanded Partnership With Google. What Comes Next.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQdHBqYVo0b05fX1ZMN245NlZzNVZsaFhjR2FpWGhnTkpVdm9rQzFBU1ZNSHQzSWF1OGJ2TkVvWmNkdnBTM2h4ZWdPUjBNbGJoMm42Z0taMHVEZm9vME5yTmNHd0ZCMzJnM0F0Ny10X2FFd1VFa2lKSWRfTTFnSUVCZ3gyT2RMMFpSX3ppUDIxSWxBTUVnTUs2R3RxWWdoNzY1RGRSSUM1MEhtdnEyQ2FlalVB?oc=5>

### Advanced Micro Devices (NASDAQ:AMD) Shares Climb 7.3% - Still a Buy?
- Summary: Advanced Micro Devices (NASDAQ:AMD) Shares Climb 7.3% - Still a Buy?
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxNQVFzUjd5UDhPRzdhdmpOV3A1Y2pibnRHUlU3XzdwY1FqMTJ2dE9NTnRaQVZlZkFnZ01Yb1VNaUFtd2pvS3JJMjNvdTJxdjZzdU5HYXNtSFZrbEtmZi1hRFlWNjZRM1lDcDVMX1Z1OXU0TnFxeExGdFhreWliTkJtYThUZmhONDZzdERlRGNPMlRnanZOZDBDUU1sbUUxY1U4LU91MVF0VG1BXzlYbWpqaFM3cXFobVFxZzJPWmFR?oc=5>

### Why is Advanced Micro Devices stock rallying today?
- Summary: Questioning the reasons behind AMD's current stock rally.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNSWpJYjh3LTd2N0JXS01nQUNBTW5mSE1DMkFXb1hGdDRnbW5IUTFaUmlGa3JBcnJFTWVXanNUUEJKbTdTbzRXSkxYcDVJVVd6RnZVeGFVaDN0UFcwc2NhLVBldUxja3lPZ2RDa0xNUWZDRHIzbG4xSVFtV05vWXlSU1FKa21VVkY4R1BQUWpiaHlpV0ZMbzlzYk1SSFhwQVhQMkhJSHc5X1BhS2VFR1J2NVZn?oc=5>

### Lisa Su Just Delivered Fantastic News for AMD Investors
- Summary: Lisa Su announced positive developments for AMD, boosting investor confidence.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPT2R4dElOVkdNdkU0X3NMQ19nbHVUM1FfNnVnYWRfSGhUY3FWaW0wVFlaQWZlVXVkYU05UWpfekozZWxZaDYzdHc5XzdFdTVmaF9KRklKRHh0UE9mLXhKbXVKQkZsMWo2OGtxai13a0RUaU1MR3hrb1RIUEd2TUc4Mlc1QTZuVmMwaXdZX1dxMUdlaG8tS0hNbUhiNV9JQQ?oc=5>

## HEADWINDS

### AMD's Stock Fades as Investors Weigh Whether Nvidia's Turmoil Will Mean Lasting Wins
- Summary: Investors concerned that Nvidia's issues may hurt AMD's market position, leading to a decline in AMD shares.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPaUZDQ3VHNU1YV2Q5MU5NLXFUYTloblM5bEV0UjVGQWluMVZNVXRMamJ0N0NEby1zQnkwOFJPTkVvODlEZUVtNGdrU3F4UF9lY3BVRDdOdktaT3BKdm80eTZ5ZUtKSDQ2TG9tYlpIRWszZFNVaEZvYzBwcjN4UW55dkJHQW5LTEhnRk5SZ284RkhOY3lrc2k2N202Wmc?oc=5>

### Advanced Micro Devices (AMD) Recently Crashed Out of the $1 Trillion Club. Should You Buy the Dip?
- Summary: AMD loses $1 trillion market cap, indicating a negative market move.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOeEpRMjVrSzZYZENMSFgxdHVucTIxajJzb0xQVXptZGVjRUh3eEMxUEU4MDVpUFJEMnBSYnU5UFhOYXI2SHFjdHQ0NW9QdDczV2MtVlczVzZCbEE0RDN5R0l3NnhkbE40bkJUR3FZSXpZMmVTQ0VPRHNFR3lWcW9mQ2FxTlJpQl9pZ01YTGV2RzlXNVdoVHFV?oc=5>

## CATALYSTS

### AMD Stock Rises on the Launch of its EPYC Venice 9006 CPUs
- Summary: AMD Stock Rises on the Launch of its EPYC Venice 9006 CPUs
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQZ0ExN05CQV9IQ0xMTmh1cmQtTVNaSFU5amFaMGo0SEtPOGpQVm5WQVhXTFBFc1pieTExcHAwamFfLVV0ajlyVGR3cEFsWmI0Rm5SNlJlQ1lobUw4TGFZZEFkbzZPTmhYZ25ydEVKTmtvVFJkN1lmSE90c2lsNVZnQVRwNU82UjhwVm13?oc=5>

### AMD stock jumps 13% after 5-star analyst resets price target
- Summary: AMD stock jumps 13% after 5-star analyst resets price target
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPYlRIejllVjJBT1VWTzZjVFRYYUtIOUJUS0kyVm02aS02YkhQWVhmM2JmcVJwaVVQbW96aUpZMEpiVnZoclhlS3lqZnF3YnA2NnRWRTQ5TEZiU1Q3eC02dVU4bXZlMXhPTWU1LUE3YWlCNUNuN01Vak5KX05hUVEyMWgyemJLdllOOGNhMTljNDlSTW4zb1Rr?oc=5>

### AMD shares are primed for a comeback, says Oppenheimer
- Summary: Analyst predicts short‑term rebound for AMD shares.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMie0FVX3lxTE1CYmI5cjRwNEFyb0VzcTdZb3Fic0Jkck9Cd1RLNURuYVdTWEpDSzktSER6TjBCNlplV3VyRkc1NmZnOThHYnBoZTRibUYwWkNkbktuUGE5d2JLM2pQNW9VdnJ5Rl92WjZ5Z0dobmdTLWdySUFSUDl1REVKdw?oc=5>

### Stock Market Today, Nov. 11: Advanced Micro Devices Jumps -- and Not Only Because of CoreWeave's Results
- Summary: AMD shares surged on market day, driven by CoreWeave results.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8AFBVV95cUxNTGgxdktvSEI0M2hDSUdFUktvLTFDVldrV1FDcXJyX1RQMDFPWDdoWUZyTXJyaFgzQmpmUkZaMUl5SEdjWTVqc2ZsQ3lXd0ZteXM1eTUwZ0YyUGptbDh3eVJUVk9GNWdFemkzX3VvZUI3eHpSRkxXS1RzMW52MDlWTzhDMzNCbFU2M3BnNzZfTXZucHdhclFDYWJHclN0eUFHZzdPS2o2dzBoU0FnSGhJNkFhdU1mSjhNNWRWRktSdmpnd2FGRW5SR0ZPVDF5Qi00aE5XX1BXdVNFLTVrRGo1ZFBvQ3RIVmlad1hxaUhac3c?oc=5>

### AMD and Coherent: What the Biggest Gainers Since the Midterm Selloff Say About the AI Trade
- Summary: AMD and Coherent among top gainers, reflecting AI sector momentum.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMie0FVX3lxTE5la2wydkhvVGI4X2w3OGpMXzdsenFEYjFBOHJ6NEp6QXh2U19URDVsVFpIX2I4aU9iNTNjMmlvcnFENkNfZ3ZUc1dqMUtlZGN5TzZMRndnMElTU3FFRjVKc2pMMkpkUXZtc0RTMmo1ZkJwaWlDTXM4NGNYbw?oc=5>

### AMD Price Prediction: AI Boom and Record Revenue Set the Stage for Another Monster Rally
- Summary: Analysts forecast strong AI-driven revenue growth, suggesting a potential rally for AMD shares.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxOV2JwTlVmYURNakZDS1ZlNGw4U0VUYWlDY2xPNXpnVGV6YlZXMVZVcndaNTJFUGk0Smxmc01neTUyTUY2YkJMWGdHQml2TnVyZ1VxcENaZTBkaUhGQnhLbWxHNWdra0F2MFA3RG9UNjhUWWhiUktLcVRsdHdpS0x0eFAyaHdLTlRxU0VseWpIeVJ2QXg2a2kySWZ0QVN0WUlhWHZMY04za3ZVZXpFSlk1TG43bVdoQ2lVRnQ5bUVIZk5aUkFMXzNMbllXMA?oc=5>

### BofA Raised Its Earnings Estimates but Cut Its Target on AMD (AMD), Here’s Why
- Summary: Bank of America increased earnings forecasts for AMD but lowered its price target, reflecting mixed outlook on the company's performance.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNSXJleUlRZEFkakZDN3phZjBfVTRMNWRrZ2JnQWduQXh1aVdFbm5vVzNRblN2dlQ4VkxvdVlSQ1VNRFZpcXlOd0RCYWxfSnZDa3BLNE5kZHBCYUdUbHEzcEdPVTdvandlX3VmeWdWSmgzYkVWWEo4SlRMbC1LaGRFSDJ4ZnBnZHZoREZVTkhxeXVJMTFRZDN5RnI0b0pvSjVi?oc=5>

### AMD Stocks Rise as $2.5 Billion Anthropic Stake Meets Goldman To
- Summary: AMD shares climb after a $2.5B stake deal with Goldman, signaling investor confidence.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxOVVByb0sxYWc4YTJfa3hTRWUtdFQyRkVmV2ZucmJKR2ZXNEFfcmJsUzdGQVdCNTBIc0t3OGl0WjhDZGN3b2JWTGJYdEZVNVluanFqTHhVOThtTWh1U04tQ1lYQ1lMUGJ3WlNLV2ZRbWxhcGNhSnNNVnFZNE16SkstOWlUbnEtX0RJOEFmaFVESnpPRFZaTWNRRzJROXlGSzQ2NGdOMjV3WDdraGtfdHM1OA?oc=5>

### Why Advanced Micro Devices Stock Popped Today
- Summary: AMD stock surged today, reflecting positive market sentiment and recent corporate developments.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOMWRENGltcGVObDltYWVFeE1hN3NRdXZTNG5LQ29zTHlhQV9WRGsyTWI2SE92VjlFcl9pZkdjQzhSVjl4dFBfNVRWakIycmgxU0hqSGlyNVhtZzlyS2FNa2EyVDljamk1Nk9GbjhZWGI3TjROamJ1WWJSVFNFWjI1MWZqazBFd3NvM0VJU2k4ZTUxaV9XYXNRcVlNYVJ3Zw?oc=5>

### 2 Reasons AMD Can Still Outperform by 2030
- Summary: Analysts highlight two factors supporting AMD's long-term growth prospects through 2030.
- Date: 2026-11-10 | Impact: medium | Horizon: long | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPeDBRMW5CZ1I2RDExWWZVUTJRWGViRWdrNmFUeDlzcWtZYTlMenp2anpBdzEzYTE1aXdiVHJ1aXFWZGNGS3FjbmRtaHVPUW9DcF9CaEhBSG9fTU9USWI4Qk5acGtGcEk4LWctTFpsTWdsdXF0OTZHMDRLQUZLZGpjdk5LX3hlU0ZrVW5fdk5kOEo1LVJPcTIxVWZLMA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **110.14** | **13.26** | **80.79** | **44.70** | **906,804,330,496.00 USD** | **132.78** |
| NVDA | 21.96 | 18.32 | 20.68 | 105.90 | 4,195,058,188,288.00 USD | -9.84 |
| INTC | N/A | 2.89 | 18.03 | 20.90 | 332,187,500,544.00 USD | 64.99 |
| AVGO | 44.09 | 16.53 | 32.21 | 85.50 | 1,647,952,527,360.00 USD | -1.19 |

Peers fetched as_of: 2026-11-11; AMD reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,428,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMisgFBVV95cUxQdHBqYVo0b05fX1ZMN245NlZzNVZsaFhjR2FpWGhnTkpVdm9rQzFBU1ZNSHQzSWF1OGJ2TkVvWmNkdnBTM2h4ZWdPUjBNbGJoMm42Z0taMHVEZm9vME5yTmNHd0ZCMzJnM0F0Ny10X2FFd1VFa2lKSWRfTTFnSUVCZ3gyT2RMMFpSX3ppUDIxSWxBTUVnTUs2R3RxWWdoNzY1RGRSSUM1MEhtdnEyQ2FlalVB?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxNQVFzUjd5UDhPRzdhdmpOV3A1Y2pibnRHUlU3XzdwY1FqMTJ2dE9NTnRaQVZlZkFnZ01Yb1VNaUFtd2pvS3JJMjNvdTJxdjZzdU5HYXNtSFZrbEtmZi1hRFlWNjZRM1lDcDVMX1Z1OXU0TnFxeExGdFhreWliTkJtYThUZmhONDZzdERlRGNPMlRnanZOZDBDUU1sbUUxY1U4LU91MVF0VG1BXzlYbWpqaFM3cXFobVFxZzJPWmFR?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNSWpJYjh3LTd2N0JXS01nQUNBTW5mSE1DMkFXb1hGdDRnbW5IUTFaUmlGa3JBcnJFTWVXanNUUEJKbTdTbzRXSkxYcDVJVVd6RnZVeGFVaDN0UFcwc2NhLVBldUxja3lPZ2RDa0xNUWZDRHIzbG4xSVFtV05vWXlSU1FKa21VVkY4R1BQUWpiaHlpV0ZMbzlzYk1SSFhwQVhQMkhJSHc5X1BhS2VFR1J2NVZn?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPT2R4dElOVkdNdkU0X3NMQ19nbHVUM1FfNnVnYWRfSGhUY3FWaW0wVFlaQWZlVXVkYU05UWpfekozZWxZaDYzdHc5XzdFdTVmaF9KRklKRHh0UE9mLXhKbXVKQkZsMWo2OGtxai13a0RUaU1MR3hrb1RIUEd2TUc4Mlc1QTZuVmMwaXdZX1dxMUdlaG8tS0hNbUhiNV9JQQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPaUZDQ3VHNU1YV2Q5MU5NLXFUYTloblM5bEV0UjVGQWluMVZNVXRMamJ0N0NEby1zQnkwOFJPTkVvODlEZUVtNGdrU3F4UF9lY3BVRDdOdktaT3BKdm80eTZ5ZUtKSDQ2TG9tYlpIRWszZFNVaEZvYzBwcjN4UW55dkJHQW5LTEhnRk5SZ284RkhOY3lrc2k2N202Wmc?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOeEpRMjVrSzZYZENMSFgxdHVucTIxajJzb0xQVXptZGVjRUh3eEMxUEU4MDVpUFJEMnBSYnU5UFhOYXI2SHFjdHQ0NW9QdDczV2MtVlczVzZCbEE0RDN5R0l3NnhkbE40bkJUR3FZSXpZMmVTQ0VPRHNFR3lWcW9mQ2FxTlJpQl9pZ01YTGV2RzlXNVdoVHFV?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQZ0ExN05CQV9IQ0xMTmh1cmQtTVNaSFU5amFaMGo0SEtPOGpQVm5WQVhXTFBFc1pieTExcHAwamFfLVV0ajlyVGR3cEFsWmI0Rm5SNlJlQ1lobUw4TGFZZEFkbzZPTmhYZ25ydEVKTmtvVFJkN1lmSE90c2lsNVZnQVRwNU82UjhwVm13?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPYlRIejllVjJBT1VWTzZjVFRYYUtIOUJUS0kyVm02aS02YkhQWVhmM2JmcVJwaVVQbW96aUpZMEpiVnZoclhlS3lqZnF3YnA2NnRWRTQ5TEZiU1Q3eC02dVU4bXZlMXhPTWU1LUE3YWlCNUNuN01Vak5KX05hUVEyMWgyemJLdllOOGNhMTljNDlSTW4zb1Rr?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTE1CYmI5cjRwNEFyb0VzcTdZb3Fic0Jkck9Cd1RLNURuYVdTWEpDSzktSER6TjBCNlplV3VyRkc1NmZnOThHYnBoZTRibUYwWkNkbktuUGE5d2JLM2pQNW9VdnJ5Rl92WjZ5Z0dobmdTLWdySUFSUDl1REVKdw?oc=5
- https://news.google.com/rss/articles/CBMi8AFBVV95cUxNTGgxdktvSEI0M2hDSUdFUktvLTFDVldrV1FDcXJyX1RQMDFPWDdoWUZyTXJyaFgzQmpmUkZaMUl5SEdjWTVqc2ZsQ3lXd0ZteXM1eTUwZ0YyUGptbDh3eVJUVk9GNWdFemkzX3VvZUI3eHpSRkxXS1RzMW52MDlWTzhDMzNCbFU2M3BnNzZfTXZucHdhclFDYWJHclN0eUFHZzdPS2o2dzBoU0FnSGhJNkFhdU1mSjhNNWRWRktSdmpnd2FGRW5SR0ZPVDF5Qi00aE5XX1BXdVNFLTVrRGo1ZFBvQ3RIVmlad1hxaUhac3c?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTE5la2wydkhvVGI4X2w3OGpMXzdsenFEYjFBOHJ6NEp6QXh2U19URDVsVFpIX2I4aU9iNTNjMmlvcnFENkNfZ3ZUc1dqMUtlZGN5TzZMRndnMElTU3FFRjVKc2pMMkpkUXZtc0RTMmo1ZkJwaWlDTXM4NGNYbw?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxOV2JwTlVmYURNakZDS1ZlNGw4U0VUYWlDY2xPNXpnVGV6YlZXMVZVcndaNTJFUGk0Smxmc01neTUyTUY2YkJMWGdHQml2TnVyZ1VxcENaZTBkaUhGQnhLbWxHNWdra0F2MFA3RG9UNjhUWWhiUktLcVRsdHdpS0x0eFAyaHdLTlRxU0VseWpIeVJ2QXg2a2kySWZ0QVN0WUlhWHZMY04za3ZVZXpFSlk1TG43bVdoQ2lVRnQ5bUVIZk5aUkFMXzNMbllXMA?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNSXJleUlRZEFkakZDN3phZjBfVTRMNWRrZ2JnQWduQXh1aVdFbm5vVzNRblN2dlQ4VkxvdVlSQ1VNRFZpcXlOd0RCYWxfSnZDa3BLNE5kZHBCYUdUbHEzcEdPVTdvandlX3VmeWdWSmgzYkVWWEo4SlRMbC1LaGRFSDJ4ZnBnZHZoREZVTkhxeXVJMTFRZDN5RnI0b0pvSjVi?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxOVVByb0sxYWc4YTJfa3hTRWUtdFQyRkVmV2ZucmJKR2ZXNEFfcmJsUzdGQVdCNTBIc0t3OGl0WjhDZGN3b2JWTGJYdEZVNVluanFqTHhVOThtTWh1U04tQ1lYQ1lMUGJ3WlNLV2ZRbWxhcGNhSnNNVnFZNE16SkstOWlUbnEtX0RJOEFmaFVESnpPRFZaTWNRRzJROXlGSzQ2NGdOMjV3WDdraGtfdHM1OA?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOMWRENGltcGVObDltYWVFeE1hN3NRdXZTNG5LQ29zTHlhQV9WRGsyTWI2SE92VjlFcl9pZkdjQzhSVjl4dFBfNVRWakIycmgxU0hqSGlyNVhtZzlyS2FNa2EyVDljamk1Nk9GbjhZWGI3TjROamJ1WWJSVFNFWjI1MWZqazBFd3NvM0VJU2k4ZTUxaV9XYXNRcVlNYVJ3Zw?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxOZmo4dVdhejJqa19WZEhvNjBSQTNTWV9mdHhHVHhFS1p1ZWJnOHg4eUJMUmRCZ2ZVU3NPc2E3bnhjdTlnaEtOei0wS180a0dqNzFHU2RWZlpoeUtYM09zNTBUQ1N2R09odnNsVktsRl93R1NUMGQ0YXptSlY3R1dLTk5OdGdwSzdBM1AtQUlxMG1tOXdTeFZycFJZSkV5TkY5Tk11UFB2Y01DcG5HbzNkNUVHeTNqaUhqeFR5WWFzNHZvLW5PVkNLdFhPUXY?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPeDBRMW5CZ1I2RDExWWZVUTJRWGViRWdrNmFUeDlzcWtZYTlMenp2anpBdzEzYTE1aXdiVHJ1aXFWZGNGS3FjbmRtaHVPUW9DcF9CaEhBSG9fTU9USWI4Qk5acGtGcEk4LWctTFpsTWdsdXF0OTZHMDRLQUZLZGpjdk5LX3hlU0ZrVW5fdk5kOEo1LVJPcTIxVWZLMA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
