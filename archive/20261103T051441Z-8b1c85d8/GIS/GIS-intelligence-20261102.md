# GIS Intelligence Report

- ticker: **GIS**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/GIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:39:02.703010+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 13, 'rule': 3, 'ai': 7, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/GIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 13 unique headlines; 9 named publishers; 0 exact duplicates; 13 HTTPS source links; largest publisher share 23.08%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 34.7500 |
| Return 1D (%) | 1.3415 |
| Return 1W (%) | 3.1157 |
| Return 1M (%) | 10.6234 |
| Return YTD (%) | -20.1129 |
| Return 1Y (%) | -20.3015 |
| Annualized volatility (%) | 30.2474 |
| Beta vs SPY | -0.4114 |
| Max drawdown (%) | -33.2524 |
| Sharpe (rf=0) | -0.5929 |
| Downside deviation (rf=0, %) | 21.2929 |
| Sortino (rf=0) | -0.8423 |
| Historical VaR 95% (1D, %) | 2.9986 |
| Historical ES 95% (1D, %) | 3.8866 |
| Correlation vs SPY | -0.1744 |
| Tracking error vs SPY (%) | 34.8505 |
| P/E (trailing) | N/A |
| P/B | 2.49 |
| EV/EBITDA | 9.30 |
| Revenue growth (%) | -2.80 |
| Forward P/E (estimate) | 11.02 |
| Gross margin (%) | 33.73 |
| Operating margin (%) | 15.24 |
| Return on equity (%) | -10.49 |
| Free cash flow yield (%) | 7.01 |
| MA50 | 34.8265 |
| Close vs MA50 (%) | -0.2197 |
| MA200 | 36.2220 |
| Close vs MA200 (%) | -4.0638 |
| RSI (14, Wilder) | 56.8240 |
| MACD (12,26) | 0.0371 |
| MACD signal (9) | -0.2665 |
| MACD histogram | 0.3036 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GIS': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 34.7500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.3415 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.1157 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 10.6234 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -20.1129 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -20.3015 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.2474 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.2929 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.8423 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9986 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8866 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1744 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.8505 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.4114 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -33.2524 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.5929 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.0238 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 33.7280 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.2430 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -10.4950 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.0107 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.8240 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3036 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.2197 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -4.0638 -> Slightly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

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

### General Mills (GIS) Stock Trades Close To Its Sales Value
- Summary: GIS shares near sales value, indicating valuation alignment.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxNNEJlMmpXT3JldUc5UWNESmpwM2RzTVBTWHJ3OHE3RzRUb0E4REYwTWZtcWtZSlVSVjlyaDlhNXhienQ2OFFLdlhITGRzc0Vzek1mNERaYks1UGlNamFoSkJwQzl5QUdEOVQ4WEswQnpzN2d5QWFRRjVyMkxKdEVOeFF3ZzJRYVgtVHZWWldwbWQ0TUk1dzhTTHQtd1FBS2FBQ3NBNm1reFA4aEtNajZ1NTQ5V2tGWnliWGZfQkZDZC0xR2FkY0ZIdzByNjFoTXdRVFVj0gHYAUFVX3lxTE5WeWNqcDJJSWFOSzZ4Tk9zejU1N0hhNkFlc0MwTTJkU0ozM0hDZEhDOE5nak1FVk15bXl0WFFOUXlYd1AtanJaajU1eGdYVEVoZUEwYVVnb3hBdW02MnVtTHpZVFQyTDg3SkdmM1BqekFrU1FTSFAxblY5dUlDaGUzN0ZlZzB1NElTWUlCYmI1MzJMSFpNRUF0RlVHTHpFb2VJem53SnpmbjFJNjRTNGdyd21FMnBHV244OVgtQlRoOVNnY2xsZEdMM1hCUldfN1cwSXhudFZkNA?oc=5>

### How Investors May Respond To General Mills (GIS) EPIC Sticks Launch
- Summary: General Mills is launching EPIC Sticks, a new product line, potentially boosting sales and brand visibility.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxPRUhQT1h1UzlBMWtiMGV0TXFpSU9KVTZtRkVxRDdHVmlpREVsU1RDMEswUV9tQ2FaVmREQnU5NjJ6Ujh4andUejVxbzExSUxEcVZPMkhDWl9BMWp4ZzJHYWlvQ1gxaDRqWjRaVG1NcmNyU2ZIVDdfTVpPQnFBNS1Ma3FURUxwUXBKUVc3TEcwc0kxSkRCRlpQWlpOOGhCMmczbHRweHZuZEsyTkxfZXdNcm91TGdTRFJ4TjlTVDIwaUhvS2JQZS02WTVRaXNJQUxoNHJMdUVIRzdGd9IB3wFBVV95cUxQUUVpMlQ1MVg4bmEtN2JzSHJyS0M3RWxqQ2hLc0duVnU4WDJ2VmhDb1hRWHJZUU9ndEtmMHI1T0FwQWw4ZVBHRGcwVDRhejYyd0J3dDZtWEZqcDB0dzhmOFZuYV80UjJPb2UycXlTcDktSzd2T211VGYzYmJTZk8xYWlVNERGMDdSeWVlY3gtTUlDYnh6dnNKV0hpeDdNSzlTNzk3dHh4bFZuRXpxU0JxMHMzZlVKdG9HVGQwX3lxOE1FQ2UyNEN5aWpHVkF5dF9KYmZoVVZMVmdBcVZ4VTFB?oc=5>

### General Mills: A 7.3% Yield Value Opportunity With Major Cost Savings Ahead (NYSE:GIS)
- Summary: General Mills highlights a 7.3% yield and upcoming cost savings, signaling potential upside for investors.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPMnpOTnZhNmlRZFp5WkpkWklQZ0hRY3JDTFlFYlg2bzl1Q19FUktoandKOFpLd0dMaDEtN19nT2pmYmhJRUV5c2xVYnI5QjI4c2lRSWUwT1BrRG9FNEpxY1dIUDVVQ0FpVlgzeGthZF9RbWVxc2hMVE4wbXpiYlZhTUczbUhqQk10R1pWd2thS2xqaGdrbm1iS0VFS3ZCU3MtM19FT2VGbmJiSk1xTElFTjVUb1VvZkh4ZkVQaWdkek9mZw?oc=5>

### Dunkin’ and General Mills will bring latte-inspired cereal flavors with no coffee or caffeine.
- Summary: General Mills partners with Dunkin' to launch latte-inspired cereal flavors, expanding product line and appealing to coffee lovers.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOeF9jNkJqZkdNaWxBSGxRNlhvU085TGozaG85WDhkUjIwVW42Ynp6enMybnJsb0hPQ1dNSU1iR3FnamE4TGJMbDBXRW8xUkdPTzdKQzhOUEp5bS16ZmFxZjlxWk0xVUZBWTNkTEQwbTlsOTczcWpGem1aVUlqcDNtS3hzWWRHNGtsMHpJRTlrTFE3WThSaUdNeVpIVnlGQkdibjZ1Ykk1ZkdsZkdDN2xaYk1FVVBKMjlRYlE?oc=5>

### Despite Structural Challenges, General Mills' Valuation And 7.1% Yield Stand Out (Upgrade)
- Summary: Analysts upgrade General Mills, noting strong valuation and 7.1% yield despite structural challenges.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNdW1xa3dCaEVrVzBscUpYZWRPR3U4QmFmZWtqT3M4ODVLdU43Q3lFWS1NcC0xdWF4ZnE5OU9SbFIway1wd0R0MmNtQ0NURnlraE1sQWRQbUFaVDRtbkhvbFI0OWRxQVRoYUZ3Uk9URnRwMzlQdm10dTVkTHdGSWpEZ0l0Rk9aTy1uTWFVYUVkYWxSTVNNeHEyMkR5T3A4djdCRElGSkFScVNMZWdmbDdMSWZibzZLallzUHRmcmdpY2ZXTVNFUTNN?oc=5>

### General Mills: The 7% Yield Is A Trap, Not A Gift (NYSE:GIS)
- Summary: General Mills warns that a 7% dividend yield may be unsustainable, suggesting potential future dividend adjustments.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPRk1hRVFaY3FDTlRoYnRjVXc2RmxTUmQ3ZklyejFJX3BsMjYxalhPZnN4bExhYUIyTDRJc2Z0cXZURnd4SnhOaTlfNE5VWF9xMHItd3pfSTJ1UE9vcjNnRXNIZlhwQVFTOF9JS0lxeWsydXB3ZE1tU2hpeF9uTlJWR2NpcDc1aWt6cmFHLWU5LTRJR3M5ejVVY0JCQQ?oc=5>

### Conagra and Campbell's Have Already Cut Their Dividends in 2026. Could General Mills Be Next?
- Summary: Speculation that General Mills might follow competitors Conagra and Campbell's in cutting dividends in 2026.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNS1hZeHlCTVNpYkVnWk5XUU1GS2R3RDM1X2ZzSTJqSk5ZbWdLVDdZVlE1Y0tLWnl3Yy1MUmJLbVdUWWtKdk9NaDJTcUwzMFIya0hONy1lZnlHa3BQcEdGYnhyaElwLUJBYmJRaUdQZkZrejY0M3B2Z05BQ3RCQi1XMnJvczRmdUY4amY5NWNJbWVXUmhJcnEzMHp5U1Bzal9WazFERUdBVE1hbVh5TUJ3UWVUUk1fRkxhTi1vcEtHeXBTRmJnclQ2TUl3al9McDQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GIS** | **N/A** | **2.49** | **9.30** | **-2.80** | **18,580,377,600.00 USD** | **-20.30** |
| KHC | N/A | 0.82 | 8.38 | -1.40 | 29,562,587,136.00 USD | 7.71 |
| CPB | 16.90 | 1.71 | 8.62 | -7.90 | 6,602,915,840.00 USD | -21.82 |
| SJM | 60.81 | 2.44 | 9.24 | 5.00 | 14,031,225,856.00 USD | 32.07 |

Peers fetched as_of: 2026-11-02; GIS reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-23
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOVG1vdS1QbUJDZXV3TDFSd1FtVG9zbW5vOFZ6U2ZyTmVxaGxHNjZ0OFZRNEZrTDlLM0JRMFczZHJvWGk3TXZvMXRiNndqLWNuU2xqZmhtQzN4SUNBRGlDX3N3djBZX0UwR3M4VTNCc0xzV1hMTXJxdnBFWnUzWjkzeDBhaW9LaHVVR3ozUVM0MTk0VlczT2JNTmxPRUJHOGdsNW9lSkRYTi0?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOLUVNeWVMdXFwU1BoOU5ENnc3SnRPZXZPSXVzQmFsVU9VSi1acTVqYVRxaTgwQjlQMVlQUkFTTkh0ZTlJaFhYMUJVcHAwUzVWYjlfTE5uN1Q5WTBqQWE5NXhTTW1URmxHTklCdXMxMzM0NDJHdG1yTWQ0R1lEM2V4U2ZGX1pWQzlDdGgtMWdBejEzNXNSQWdlaTNUX1d2Tzl1VHRDUDJnLXVkckxjWFZzdy1VNkNhVUZPcG4yVDJoQ3E?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxOTktwa3dzVFBTdUtWN29IWklMZVM3NGtaWUNnQVRRSVBmVzRVb0FzSnp6V016Ynh4bzZZNXA3dUc1TWZpRjlfSFJhWU9QUktmV1Z3SmctNWt3cEhHaTJfWVQ3SUZSR09uam1xempnbWtXeExLX2ZMRUhmMkVfRUZwNU5xUjJ5TTllcVctb1VOemJQY2w4cEpfb0FSeXJ3NTVFUzFiNGRybVc1cEF3ZkNEMjIwZkJxZE15NkFIRHVR?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxNNEJlMmpXT3JldUc5UWNESmpwM2RzTVBTWHJ3OHE3RzRUb0E4REYwTWZtcWtZSlVSVjlyaDlhNXhienQ2OFFLdlhITGRzc0Vzek1mNERaYks1UGlNamFoSkJwQzl5QUdEOVQ4WEswQnpzN2d5QWFRRjVyMkxKdEVOeFF3ZzJRYVgtVHZWWldwbWQ0TUk1dzhTTHQtd1FBS2FBQ3NBNm1reFA4aEtNajZ1NTQ5V2tGWnliWGZfQkZDZC0xR2FkY0ZIdzByNjFoTXdRVFVj0gHYAUFVX3lxTE5WeWNqcDJJSWFOSzZ4Tk9zejU1N0hhNkFlc0MwTTJkU0ozM0hDZEhDOE5nak1FVk15bXl0WFFOUXlYd1AtanJaajU1eGdYVEVoZUEwYVVnb3hBdW02MnVtTHpZVFQyTDg3SkdmM1BqekFrU1FTSFAxblY5dUlDaGUzN0ZlZzB1NElTWUlCYmI1MzJMSFpNRUF0RlVHTHpFb2VJem53SnpmbjFJNjRTNGdyd21FMnBHV244OVgtQlRoOVNnY2xsZEdMM1hCUldfN1cwSXhudFZkNA?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxPRUhQT1h1UzlBMWtiMGV0TXFpSU9KVTZtRkVxRDdHVmlpREVsU1RDMEswUV9tQ2FaVmREQnU5NjJ6Ujh4andUejVxbzExSUxEcVZPMkhDWl9BMWp4ZzJHYWlvQ1gxaDRqWjRaVG1NcmNyU2ZIVDdfTVpPQnFBNS1Ma3FURUxwUXBKUVc3TEcwc0kxSkRCRlpQWlpOOGhCMmczbHRweHZuZEsyTkxfZXdNcm91TGdTRFJ4TjlTVDIwaUhvS2JQZS02WTVRaXNJQUxoNHJMdUVIRzdGd9IB3wFBVV95cUxQUUVpMlQ1MVg4bmEtN2JzSHJyS0M3RWxqQ2hLc0duVnU4WDJ2VmhDb1hRWHJZUU9ndEtmMHI1T0FwQWw4ZVBHRGcwVDRhejYyd0J3dDZtWEZqcDB0dzhmOFZuYV80UjJPb2UycXlTcDktSzd2T211VGYzYmJTZk8xYWlVNERGMDdSeWVlY3gtTUlDYnh6dnNKV0hpeDdNSzlTNzk3dHh4bFZuRXpxU0JxMHMzZlVKdG9HVGQwX3lxOE1FQ2UyNEN5aWpHVkF5dF9KYmZoVVZMVmdBcVZ4VTFB?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPMnpOTnZhNmlRZFp5WkpkWklQZ0hRY3JDTFlFYlg2bzl1Q19FUktoandKOFpLd0dMaDEtN19nT2pmYmhJRUV5c2xVYnI5QjI4c2lRSWUwT1BrRG9FNEpxY1dIUDVVQ0FpVlgzeGthZF9RbWVxc2hMVE4wbXpiYlZhTUczbUhqQk10R1pWd2thS2xqaGdrbm1iS0VFS3ZCU3MtM19FT2VGbmJiSk1xTElFTjVUb1VvZkh4ZkVQaWdkek9mZw?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOeF9jNkJqZkdNaWxBSGxRNlhvU085TGozaG85WDhkUjIwVW42Ynp6enMybnJsb0hPQ1dNSU1iR3FnamE4TGJMbDBXRW8xUkdPTzdKQzhOUEp5bS16ZmFxZjlxWk0xVUZBWTNkTEQwbTlsOTczcWpGem1aVUlqcDNtS3hzWWRHNGtsMHpJRTlrTFE3WThSaUdNeVpIVnlGQkdibjZ1Ykk1ZkdsZkdDN2xaYk1FVVBKMjlRYlE?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNdW1xa3dCaEVrVzBscUpYZWRPR3U4QmFmZWtqT3M4ODVLdU43Q3lFWS1NcC0xdWF4ZnE5OU9SbFIway1wd0R0MmNtQ0NURnlraE1sQWRQbUFaVDRtbkhvbFI0OWRxQVRoYUZ3Uk9URnRwMzlQdm10dTVkTHdGSWpEZ0l0Rk9aTy1uTWFVYUVkYWxSTVNNeHEyMkR5T3A4djdCRElGSkFScVNMZWdmbDdMSWZibzZLallzUHRmcmdpY2ZXTVNFUTNN?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPRk1hRVFaY3FDTlRoYnRjVXc2RmxTUmQ3ZklyejFJX3BsMjYxalhPZnN4bExhYUIyTDRJc2Z0cXZURnd4SnhOaTlfNE5VWF9xMHItd3pfSTJ1UE9vcjNnRXNIZlhwQVFTOF9JS0lxeWsydXB3ZE1tU2hpeF9uTlJWR2NpcDc1aWt6cmFHLWU5LTRJR3M5ejVVY0JCQQ?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxNS1hZeHlCTVNpYkVnWk5XUU1GS2R3RDM1X2ZzSTJqSk5ZbWdLVDdZVlE1Y0tLWnl3Yy1MUmJLbVdUWWtKdk9NaDJTcUwzMFIya0hONy1lZnlHa3BQcEdGYnhyaElwLUJBYmJRaUdQZkZrejY0M3B2Z05BQ3RCQi1XMnJvczRmdUY4amY5NWNJbWVXUmhJcnEzMHp5U1Bzal9WazFERUdBVE1hbVh5TUJ3UWVUUk1fRkxhTi1vcEtHeXBTRmJnclQ2TUl3al9McDQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
