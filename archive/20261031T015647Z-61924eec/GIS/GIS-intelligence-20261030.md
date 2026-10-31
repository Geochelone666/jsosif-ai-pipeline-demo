# GIS Intelligence Report

- ticker: **GIS**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/GIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GIS/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:19:07.297793+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 16, 'rule': 5, 'ai': 9, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/GIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 16 unique headlines; 7 named publishers; 2 exact duplicates; 16 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-10-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 34.2900 |
| Return 1D (%) | 2.9112 |
| Return 1W (%) | -0.2908 |
| Return 1M (%) | 8.6499 |
| Return YTD (%) | -21.1704 |
| Return 1Y (%) | -22.0919 |
| Annualized volatility (%) | 30.1672 |
| Beta vs SPY | -0.4090 |
| Max drawdown (%) | -33.2524 |
| Sharpe (rf=0) | -0.6808 |
| Downside deviation (rf=0, %) | 21.2746 |
| Sortino (rf=0) | -0.9653 |
| Historical VaR 95% (1D, %) | 2.9959 |
| Historical ES 95% (1D, %) | 3.8866 |
| Correlation vs SPY | -0.1734 |
| Tracking error vs SPY (%) | 34.7477 |
| P/E (trailing) | N/A |
| P/B | 2.46 |
| EV/EBITDA | 9.23 |
| Revenue growth (%) | -2.80 |
| Forward P/E (estimate) | 10.88 |
| Gross margin (%) | 33.73 |
| Operating margin (%) | 15.24 |
| Return on equity (%) | -10.49 |
| Free cash flow yield (%) | 7.10 |
| MA50 | 34.9160 |
| Close vs MA50 (%) | -1.7929 |
| MA200 | 36.2645 |
| Close vs MA200 (%) | -5.4448 |
| RSI (14, Wilder) | 54.4697 |
| MACD (12,26) | -0.0731 |
| MACD signal (9) | -0.3424 |
| MACD histogram | 0.2693 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GIS': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 34.2900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.9112 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.2908 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 8.6499 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -21.1704 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -22.0919 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.1672 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.2746 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.9653 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9959 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8866 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1734 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.7477 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.4090 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -33.2524 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.6808 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.8779 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 33.7280 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.2430 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -10.4950 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.1047 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 54.4697 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2693 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -1.7929 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -5.4448 -> Clearly below the moving-average trend level.

## TAILWINDS

### General Mills: The 7% Yield Is A Trap, Not A Gift (NYSE:GIS)
- Summary: Dividend yield claim criticized as misleading.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPRk1hRVFaY3FDTlRoYnRjVXc2RmxTUmQ3ZklyejFJX3BsMjYxalhPZnN4bExhYUIyTDRJc2Z0cXZURnd4SnhOaTlfNE5VWF9xMHItd3pfSTJ1UE9vcjNnRXNIZlhwQVFTOF9JS0lxeWsydXB3ZE1tU2hpeF9uTlJWR2NpcDc1aWt6cmFHLWU5LTRJR3M5ejVVY0JCQQ?oc=5>

### 90% of cereal lovers say they take extra steps to keep it fresh. Cheerios adds a resealable bag.
- Summary: Cheerios introduces resealable bag to improve freshness, enhancing product appeal.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQQmRsamNuUVNGQWt1UGF0RlFpSjdVM2tvdm5qZDNIelQ3RVAxbEtLWkRhREQtdDVGMlhjWkNrQjR6WFVObklieFJkZDhtTVhKWFdCdk9laHp6MXUxRFVMeDBWeUM3X3hRMUkzYzJycTJqMDVDUXJZRDBpeGxHOEY1MkJ4S1dtU253VzVRb0dWX1NYZGw1X2VhN3JFb1hobkRHckNPU25aSnRLODJMM0ZQUndQN0VrTms?oc=5>

## HEADWINDS

### General Mills (GIS) Stock Seems About Right On Its 38% Slide
- Summary: General Mills (GIS) Stock Seems About Right On Its 38% Slide
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOSHV0OTVXbmVEVk56cFpiTFMxQkQ5cktwREVEbC04c2hwdGRRNi1qMTJlZzdpaFVDZzJyMnZjMHFuWkZLYzdXVVY0OF9MdkZ0S0dyc1I2NVRBQ2FFSFo3dHFYcnRwNEw0R1EtM3lXVzkyQ0VsRi02MlJKQnVvdWlmdzJOT19XajgtRjVfbUw3SzRHaTNKdWNRSEtR?oc=5>

## CATALYSTS

### General Mills' Quarterly Earnings Preview: What You Need to Know
- Summary: General Mills' Quarterly Earnings Preview: What You Need to Know
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOVG1vdS1QbUJDZXV3TDFSd1FtVG9zbW5vOFZ6U2ZyTmVxaGxHNjZ0OFZRNEZrTDlLM0JRMFczZHJvWGk3TXZvMXRiNndqLWNuU2xqZmhtQzN4SUNBRGlDX3N3djBZX0UwR3M4VTNCc0xzV1hMTXJxdnBFWnUzWjkzeDBhaW9LaHVVR3ozUVM0MTk0VlczT2JNTmxPRUJHOGdsNW9lSkRYTi0?oc=5>

### General Mills Yields Nearly 7%. Is Its Dividend Safer Than Kraft Heinz or Smucker?
- Summary: General Mills Yields Nearly 7%. Is Its Dividend Safer Than Kraft Heinz or Smucker?
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOLUVNeWVMdXFwU1BoOU5ENnc3SnRPZXZPSXVzQmFsVU9VSi1acTVqYVRxaTgwQjlQMVlQUkFTTkh0ZTlJaFhYMUJVcHAwUzVWYjlfTE5uN1Q5WTBqQWE5NXhTTW1URmxHTklCdXMxMzM0NDJHdG1yTWQ0R1lEM2V4U2ZGX1pWQzlDdGgtMWdBejEzNXNSQWdlaTNUX1d2Tzl1VHRDUDJnLXVkckxjWFZzdy1VNkNhVUZPcG4yVDJoQ3E?oc=5>

### General Mills, Inc. $GIS Stock Purchased by Sigma Planning Corp
- Summary: General Mills, Inc. $GIS Stock Purchased by Sigma Planning Corp
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxOTktwa3dzVFBTdUtWN29IWklMZVM3NGtaWUNnQVRRSVBmVzRVb0FzSnp6V016Ynh4bzZZNXA3dUc1TWZpRjlfSFJhWU9QUktmV1Z3SmctNWt3cEhHaTJfWVQ3SUZSR09uam1xempnbWtXeExLX2ZMRUhmMkVfRUZwNU5xUjJ5TTllcVctb1VOemJQY2w4cEpfb0FSeXJ3NTVFUzFiNGRybVc1cEF3ZkNEMjIwZkJxZE15NkFIRHVR?oc=5>

### General Mills, Inc. $GIS Stock Sold by Quadrant Capital Group LLC
- Summary: General Mills, Inc. $GIS Stock Sold by Quadrant Capital Group LLC
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNREFTTFpiYjV2N3AzSFNBVEJ4aVhNSGJDbmx0ckEyUF80eUN5RzlVejE2TU5zZnMxekpHeFQ4bEtlbVNkZzJMNzg3ZVJVSHQ0a2dCSkM5Qkp2UUx4WmpXVHQzNVg2XzZWMFBfWHR5b05SMjg5dF85aS1QZWZUNHA5dWhBVGZlSmkwMkM1dW1XQWFFZFc2TlZjUUFUdVZpUmV2dVJhMm1mVmpON2l5STZYekRPdHJYQXJvRW5SbHhrS08?oc=5>

### General Mills: A 7.3% Yield Value Opportunity With Major Cost Savings Ahead (NYSE:GIS)
- Summary: General Mills highlights a 7.3% yield opportunity and significant cost savings, signaling potential upside for investors.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPMnpOTnZhNmlRZFp5WkpkWklQZ0hRY3JDTFlFYlg2bzl1Q19FUktoandKOFpLd0dMaDEtN19nT2pmYmhJRUV5c2xVYnI5QjI4c2lRSWUwT1BrRG9FNEpxY1dIUDVVQ0FpVlgzeGthZF9RbWVxc2hMVE4wbXpiYlZhTUczbUhqQk10R1pWd2thS2xqaGdrbm1iS0VFS3ZCU3MtM19FT2VGbmJiSk1xTElFTjVUb1VvZkh4ZkVQaWdkek9mZw?oc=5>

### Despite Structural Challenges, General Mills' Valuation And 7.1% Yield Stand Out (Upgrade)
- Summary: Analyst upgrade highlights strong valuation and yield.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNdW1xa3dCaEVrVzBscUpYZWRPR3U4QmFmZWtqT3M4ODVLdU43Q3lFWS1NcC0xdWF4ZnE5OU9SbFIway1wd0R0MmNtQ0NURnlraE1sQWRQbUFaVDRtbkhvbFI0OWRxQVRoYUZ3Uk9URnRwMzlQdm10dTVkTHdGSWpEZ0l0Rk9aTy1uTWFVYUVkYWxSTVNNeHEyMkR5T3A4djdCRElGSkFScVNMZWdmbDdMSWZibzZLallzUHRmcmdpY2ZXTVNFUTNN?oc=5>

### How EPIC Sticks Launch At General Mills (GIS) Has Changed Its Investment Story
- Summary: Launch of EPIC Sticks product line, influencing investment perception.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPanpYVHhXaXhLRHRUX3lEOEZkcVNFX3JmeW4tQklHOXpORjFqYmxXRHpDQTZnZUdkTFRLV3A3bFFUTkxnaGVLenRORFdkSXdNRlNzejlYa2JMcDZFVkJ1UXN6VEJVRm5ucG5XaWxkbDJ5dmd1UDBiR3gwWkNiX1BLWlZ6V1dJd0wzbzlGak5BSzFaUGdtV2Q4TUEyU3BvUQ?oc=5>

### General Mills (GIS) Stock Looks Reasonably Priced For Now
- Summary: Analyst suggests current price is fair, no immediate upside.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxOaVExbjV1YWNRalAyS2NtY2NTV3NPTzVCUGYwUmFsNWMwRUFMUUxLRkxBRzNQdXk4eFpaWjZPUk1xbzlxWTJ6THhlWlJULTk0Z2VmcHpqcjR0Q3ZJczFYbXZRTXU0UzVPWG9HMm5kUE5VNDc4Q0tFRjNrajV2Y1F4bVJRWHdQc1RUb1A0SU9PcHVsSnFxVDQzUFU2Tl9wRWJPSUFRRkF2MzNkRHZNd251a2JicjN0THQxRTd5VjFKQ24tenpwdDc4Z2dOenpfRVhoNFY40gHYAUFVX3lxTE44clVSWVp3eVlJYlNJcGlwR0I0ZWlqVFV2dGVVUThPb1ltV3JUNGFwaDNqNzRzVldPMHZQYkEzSGl4MDJtQUwybmNyT0p5SWZSUjFpaDkweGFuUUl3MldHTXI1ZVBMa0Y3QWI1bDlid2EtOENuOXl5WUhTdlhHaTBwdUtuLVBkZ0s0b0ZnVU1iWlpNVFVJSEM5TkQtUXBmZ1g3MmhJeElEa3VKU1pyN0V4WWh1SU1iTXJfODRTbV8yeFRUZ3dncVBRUDlyLXhzeWxteENZRThOVQ?oc=5>

### General Mills, Inc. Estimates – NYSE:GIS
- Summary: GIS releases earnings estimates for the upcoming period.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidEFVX3lxTE5tS0ZTdDlQd2FtSlJSYnMwVDNtZ2NPVGZvc3VHUFBQbS1pRUpPWDBXYzZIM2xZTXZ1dGFjM3ZsZnA4YjAxeWpJcF9JeTlPNnRTOFBweElCQklnd1VoTEpnendUVkdpMUdza1J3dmJjc3FsWTlI?oc=5>

### General Mills (GIS) Stock Trades Close To Its Sales Value
- Summary: GIS shares near sales value, indicating valuation alignment.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxNNEJlMmpXT3JldUc5UWNESmpwM2RzTVBTWHJ3OHE3RzRUb0E4REYwTWZtcWtZSlVSVjlyaDlhNXhienQ2OFFLdlhITGRzc0Vzek1mNERaYks1UGlNamFoSkJwQzl5QUdEOVQ4WEswQnpzN2d5QWFRRjVyMkxKdEVOeFF3ZzJRYVgtVHZWWldwbWQ0TUk1dzhTTHQtd1FBS2FBQ3NBNm1reFA4aEtNajZ1NTQ5V2tGWnliWGZfQkZDZC0xR2FkY0ZIdzByNjFoTXdRVFVj0gHYAUFVX3lxTE5WeWNqcDJJSWFOSzZ4Tk9zejU1N0hhNkFlc0MwTTJkU0ozM0hDZEhDOE5nak1FVk15bXl0WFFOUXlYd1AtanJaajU1eGdYVEVoZUEwYVVnb3hBdW02MnVtTHpZVFQyTDg3SkdmM1BqekFrU1FTSFAxblY5dUlDaGUzN0ZlZzB1NElTWUlCYmI1MzJMSFpNRUF0RlVHTHpFb2VJem53SnpmbjFJNjRTNGdyd21FMnBHV244OVgtQlRoOVNnY2xsZEdMM1hCUldfN1cwSXhudFZkNA?oc=5>

## RISKS

### Conagra and Campbell's Have Already Cut Their Dividends in 2026. Could General Mills Be Next?
- Summary: Potential dividend cut could reduce shareholder returns.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPeVdJcURjSDhyTDc4V0dfcTEwNWNBUHpPaWFnZHNDZmhXdG9SOERtQVZmdTdocDBId05fZGs0OVhfcVAwS2lPMzhXT2dZWVBScmRuMVg0WVdtSnJ5eU1aOGNJMXN2cXUtSmNTNjdnSWw5akVwcWRpZkNwUXZqVnBlR2t1cnN0S1YtWnNGQ1FTb1doa2sxalN5dzNDaVk2ZHdhY3lETGdrbw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GIS** | **N/A** | **2.46** | **9.23** | **-2.80** | **18,334,423,040.00 USD** | **-22.09** |
| KHC | N/A | 0.80 | 8.25 | -1.40 | 28,862,949,376.00 USD | 5.80 |
| CPB | 16.35 | 1.66 | 8.49 | -7.90 | 6,388,187,136.00 USD | -24.76 |
| SJM | 60.70 | 2.41 | 9.18 | 5.00 | 13,876,330,496.00 USD | 32.14 |

Peers fetched as_of: 2026-10-30; GIS reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-23
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-09-23
- Revenue (latest available single quarter): 4,389,500,000.00 USD; period 2026-06-01/2026-08-30; fiscal year/reporting period 2027/Q1
- Net income (latest available single quarter): 397,000,000.00 USD; period 2026-06-01/2026-08-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/40704/000162828026063201/gis-20260830.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxPRk1hRVFaY3FDTlRoYnRjVXc2RmxTUmQ3ZklyejFJX3BsMjYxalhPZnN4bExhYUIyTDRJc2Z0cXZURnd4SnhOaTlfNE5VWF9xMHItd3pfSTJ1UE9vcjNnRXNIZlhwQVFTOF9JS0lxeWsydXB3ZE1tU2hpeF9uTlJWR2NpcDc1aWt6cmFHLWU5LTRJR3M5ejVVY0JCQQ?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxQQmRsamNuUVNGQWt1UGF0RlFpSjdVM2tvdm5qZDNIelQ3RVAxbEtLWkRhREQtdDVGMlhjWkNrQjR6WFVObklieFJkZDhtTVhKWFdCdk9laHp6MXUxRFVMeDBWeUM3X3hRMUkzYzJycTJqMDVDUXJZRDBpeGxHOEY1MkJ4S1dtU253VzVRb0dWX1NYZGw1X2VhN3JFb1hobkRHckNPU25aSnRLODJMM0ZQUndQN0VrTms?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOSHV0OTVXbmVEVk56cFpiTFMxQkQ5cktwREVEbC04c2hwdGRRNi1qMTJlZzdpaFVDZzJyMnZjMHFuWkZLYzdXVVY0OF9MdkZ0S0dyc1I2NVRBQ2FFSFo3dHFYcnRwNEw0R1EtM3lXVzkyQ0VsRi02MlJKQnVvdWlmdzJOT19XajgtRjVfbUw3SzRHaTNKdWNRSEtR?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOVG1vdS1QbUJDZXV3TDFSd1FtVG9zbW5vOFZ6U2ZyTmVxaGxHNjZ0OFZRNEZrTDlLM0JRMFczZHJvWGk3TXZvMXRiNndqLWNuU2xqZmhtQzN4SUNBRGlDX3N3djBZX0UwR3M4VTNCc0xzV1hMTXJxdnBFWnUzWjkzeDBhaW9LaHVVR3ozUVM0MTk0VlczT2JNTmxPRUJHOGdsNW9lSkRYTi0?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOLUVNeWVMdXFwU1BoOU5ENnc3SnRPZXZPSXVzQmFsVU9VSi1acTVqYVRxaTgwQjlQMVlQUkFTTkh0ZTlJaFhYMUJVcHAwUzVWYjlfTE5uN1Q5WTBqQWE5NXhTTW1URmxHTklCdXMxMzM0NDJHdG1yTWQ0R1lEM2V4U2ZGX1pWQzlDdGgtMWdBejEzNXNSQWdlaTNUX1d2Tzl1VHRDUDJnLXVkckxjWFZzdy1VNkNhVUZPcG4yVDJoQ3E?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxOTktwa3dzVFBTdUtWN29IWklMZVM3NGtaWUNnQVRRSVBmVzRVb0FzSnp6V016Ynh4bzZZNXA3dUc1TWZpRjlfSFJhWU9QUktmV1Z3SmctNWt3cEhHaTJfWVQ3SUZSR09uam1xempnbWtXeExLX2ZMRUhmMkVfRUZwNU5xUjJ5TTllcVctb1VOemJQY2w4cEpfb0FSeXJ3NTVFUzFiNGRybVc1cEF3ZkNEMjIwZkJxZE15NkFIRHVR?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNREFTTFpiYjV2N3AzSFNBVEJ4aVhNSGJDbmx0ckEyUF80eUN5RzlVejE2TU5zZnMxekpHeFQ4bEtlbVNkZzJMNzg3ZVJVSHQ0a2dCSkM5Qkp2UUx4WmpXVHQzNVg2XzZWMFBfWHR5b05SMjg5dF85aS1QZWZUNHA5dWhBVGZlSmkwMkM1dW1XQWFFZFc2TlZjUUFUdVZpUmV2dVJhMm1mVmpON2l5STZYekRPdHJYQXJvRW5SbHhrS08?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPMnpOTnZhNmlRZFp5WkpkWklQZ0hRY3JDTFlFYlg2bzl1Q19FUktoandKOFpLd0dMaDEtN19nT2pmYmhJRUV5c2xVYnI5QjI4c2lRSWUwT1BrRG9FNEpxY1dIUDVVQ0FpVlgzeGthZF9RbWVxc2hMVE4wbXpiYlZhTUczbUhqQk10R1pWd2thS2xqaGdrbm1iS0VFS3ZCU3MtM19FT2VGbmJiSk1xTElFTjVUb1VvZkh4ZkVQaWdkek9mZw?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNdW1xa3dCaEVrVzBscUpYZWRPR3U4QmFmZWtqT3M4ODVLdU43Q3lFWS1NcC0xdWF4ZnE5OU9SbFIway1wd0R0MmNtQ0NURnlraE1sQWRQbUFaVDRtbkhvbFI0OWRxQVRoYUZ3Uk9URnRwMzlQdm10dTVkTHdGSWpEZ0l0Rk9aTy1uTWFVYUVkYWxSTVNNeHEyMkR5T3A4djdCRElGSkFScVNMZWdmbDdMSWZibzZLallzUHRmcmdpY2ZXTVNFUTNN?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPanpYVHhXaXhLRHRUX3lEOEZkcVNFX3JmeW4tQklHOXpORjFqYmxXRHpDQTZnZUdkTFRLV3A3bFFUTkxnaGVLenRORFdkSXdNRlNzejlYa2JMcDZFVkJ1UXN6VEJVRm5ucG5XaWxkbDJ5dmd1UDBiR3gwWkNiX1BLWlZ6V1dJd0wzbzlGak5BSzFaUGdtV2Q4TUEyU3BvUQ?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOaVExbjV1YWNRalAyS2NtY2NTV3NPTzVCUGYwUmFsNWMwRUFMUUxLRkxBRzNQdXk4eFpaWjZPUk1xbzlxWTJ6THhlWlJULTk0Z2VmcHpqcjR0Q3ZJczFYbXZRTXU0UzVPWG9HMm5kUE5VNDc4Q0tFRjNrajV2Y1F4bVJRWHdQc1RUb1A0SU9PcHVsSnFxVDQzUFU2Tl9wRWJPSUFRRkF2MzNkRHZNd251a2JicjN0THQxRTd5VjFKQ24tenpwdDc4Z2dOenpfRVhoNFY40gHYAUFVX3lxTE44clVSWVp3eVlJYlNJcGlwR0I0ZWlqVFV2dGVVUThPb1ltV3JUNGFwaDNqNzRzVldPMHZQYkEzSGl4MDJtQUwybmNyT0p5SWZSUjFpaDkweGFuUUl3MldHTXI1ZVBMa0Y3QWI1bDlid2EtOENuOXl5WUhTdlhHaTBwdUtuLVBkZ0s0b0ZnVU1iWlpNVFVJSEM5TkQtUXBmZ1g3MmhJeElEa3VKU1pyN0V4WWh1SU1iTXJfODRTbV8yeFRUZ3dncVBRUDlyLXhzeWxteENZRThOVQ?oc=5
- https://news.google.com/rss/articles/CBMidEFVX3lxTE5tS0ZTdDlQd2FtSlJSYnMwVDNtZ2NPVGZvc3VHUFBQbS1pRUpPWDBXYzZIM2xZTXZ1dGFjM3ZsZnA4YjAxeWpJcF9JeTlPNnRTOFBweElCQklnd1VoTEpnendUVkdpMUdza1J3dmJjc3FsWTlI?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxNNEJlMmpXT3JldUc5UWNESmpwM2RzTVBTWHJ3OHE3RzRUb0E4REYwTWZtcWtZSlVSVjlyaDlhNXhienQ2OFFLdlhITGRzc0Vzek1mNERaYks1UGlNamFoSkJwQzl5QUdEOVQ4WEswQnpzN2d5QWFRRjVyMkxKdEVOeFF3ZzJRYVgtVHZWWldwbWQ0TUk1dzhTTHQtd1FBS2FBQ3NBNm1reFA4aEtNajZ1NTQ5V2tGWnliWGZfQkZDZC0xR2FkY0ZIdzByNjFoTXdRVFVj0gHYAUFVX3lxTE5WeWNqcDJJSWFOSzZ4Tk9zejU1N0hhNkFlc0MwTTJkU0ozM0hDZEhDOE5nak1FVk15bXl0WFFOUXlYd1AtanJaajU1eGdYVEVoZUEwYVVnb3hBdW02MnVtTHpZVFQyTDg3SkdmM1BqekFrU1FTSFAxblY5dUlDaGUzN0ZlZzB1NElTWUlCYmI1MzJMSFpNRUF0RlVHTHpFb2VJem53SnpmbjFJNjRTNGdyd21FMnBHV244OVgtQlRoOVNnY2xsZEdMM1hCUldfN1cwSXhudFZkNA?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPeVdJcURjSDhyTDc4V0dfcTEwNWNBUHpPaWFnZHNDZmhXdG9SOERtQVZmdTdocDBId05fZGs0OVhfcVAwS2lPMzhXT2dZWVBScmRuMVg0WVdtSnJ5eU1aOGNJMXN2cXUtSmNTNjdnSWw5akVwcWRpZkNwUXZqVnBlR2t1cnN0S1YtWnNGQ1FTb1doa2sxalN5dzNDaVk2ZHdhY3lETGdrbw?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxNS1hZeHlCTVNpYkVnWk5XUU1GS2R3RDM1X2ZzSTJqSk5ZbWdLVDdZVlE1Y0tLWnl3Yy1MUmJLbVdUWWtKdk9NaDJTcUwzMFIya0hONy1lZnlHa3BQcEdGYnhyaElwLUJBYmJRaUdQZkZrejY0M3B2Z05BQ3RCQi1XMnJvczRmdUY4amY5NWNJbWVXUmhJcnEzMHp5U1Bzal9WazFERUdBVE1hbVh5TUJ3UWVUUk1fRkxhTi1vcEtHeXBTRmJnclQ2TUl3al9McDQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
