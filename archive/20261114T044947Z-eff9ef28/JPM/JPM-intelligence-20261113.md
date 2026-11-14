# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T04:58:49.417742+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 2, 'ai': 11, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/JPM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 12 named publishers; 3 exact duplicates; 21 HTTPS source links; largest publisher share 38.1%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 346.1900 |
| Return 1D (%) | 0.9830 |
| Return 1W (%) | 3.4979 |
| Return 1M (%) | 4.4534 |
| Return YTD (%) | 9.5083 |
| Return 1Y (%) | 14.0163 |
| Annualized volatility (%) | 22.7136 |
| Beta vs SPY | 0.7831 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.6934 |
| Downside deviation (rf=0, %) | 16.2084 |
| Sortino (rf=0) | 0.9716 |
| Historical VaR 95% (1D, %) | 2.3879 |
| Historical ES 95% (1D, %) | 3.3202 |
| Correlation vs SPY | 0.4700 |
| Tracking error vs SPY (%) | 20.2650 |
| P/E (trailing) | 14.38 |
| P/B | 2.62 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 13.54 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 44.79 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 339.7039 |
| Close vs MA50 (%) | 1.9093 |
| MA200 | 322.4353 |
| Close vs MA200 (%) | 7.3673 |
| RSI (14, Wilder) | 56.3261 |
| MACD (12,26) | 1.5406 |
| MACD signal (9) | 0.6789 |
| MACD histogram | 0.8617 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 346.1900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.9830 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.4979 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.4534 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 9.5083 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 14.0163 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.7136 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.2084 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.9716 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.3879 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3202 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4700 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.2650 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7831 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6934 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.5373 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.7880 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.3826 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.3261 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.8617 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.9093 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 7.3673 -> Clearly above the moving-average trend level.

## TAILWINDS

### JPMorgan Chase & Co. (JPM) is Attracting Investor Attention: Here is What You Should Know
- Summary: Positive investor focus on JPM, indicating potential upside.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNZEdSeWY5RUlCZ3QxZklmQ2hsTGJXdHdxU3hXQXkxQUJCZXJaMlpMYkc4SEtubncteGpGVVIxcWFtV19RdWF2bDNSQmY5UC1aVUo5U1NmQWRpSjlnWW1OUWRhMWdyb191VS1LV2g1QTZUTTFmR0hPXzQwU3pzbndINnJhU19xN0FtQ1pQR2xCN20wbTI4YnhyWi1EazJjdw?oc=5>

### JPMorganChase Declares Preferred Stock Dividends
- Summary: JPM announces preferred stock dividends, boosting shareholder returns.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNX1hTbFd0OGF4OTF2NWktQ19MNWtFTGRuQUMteHgzRDhNV0doWXFCWTJpM3RaVFdiOFl0M2ppdFN6TmxSWjBKVmd4X3MwQnA4RXp6TlBSam9pTzVSR1NNdzNVSUE1OElySFBtWnFkanNlVTN5SXZUSVdRTGJkcmhpNTVKUHYtSGxmNk5PYV9IeTZpT0phRVNMb1Q4bXdHX09ER2lKcUU2QVE?oc=5>

### JPMorgan Partners With OpenAI: What It Means for JPM's AI Strategy
- Summary: JPM partners with OpenAI, enhancing AI capabilities and market positioning.
- Date: 2026-11-11 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPdzVzbG44emM5UVNZaktmOUVnMlU4cUlFVXBORmZjU0MyWUxWNlc2YTRZRHhpM3JkMFBsLTN3bGJXcHBWQ2Nuc1hjdjloYTNJZ3RRS19vUWM1dkN3RXp3OFd2N0wtY1JFRFpnRFN1M2JxWE45YTRDVlVheHlvRU1Idy1RZTBqV0REMVlrT2ZJZ2pfRzRtTEhoM2hiZ0pQR3Q2?oc=5>

### JPMorgan Chase (JPM) Funding Moves Put Valuation In Focus As Shares Test Record Territory
- Summary: Funding moves boost valuation focus; shares reach record highs, signaling strong market confidence.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxOVEliaW5hSkRCZUg4Y091X3R5SzdEeEZtWVhwRy01UkN2dmwyeHpNUFhpLVprTlBQcTdWMGc4ZnluY2IyaGdzRHowZWdEaXFjemFwMUl2NDBwWm8zR0p6cFlVMVNFcjNkV2J1S1I3cFB0QkR4WEREOHdjbjBaR3dacTItaUh5VGQ5LTJhbndGaElTZTdMS3p2bGRpRUFpcWJ5cHlfSmYzeTdTbUtkS25PSlR0bVFDOVdUaHBlSE4xODJXaFRoc3fSAcsBQVVfeXFMT0pvVVRXQ3RNclRZR3gtSjBaUGJEOHczeGs5UnZDekF4OVFiOE1NQzU0N1Q5UjQ2NnNyQkVNaXMwNGRUM2VUcGx1UDdxLXZjSElvY2dlZndjZEhiWkFnM3dIVGM2bDNkOExCWDQybFloTUFZMGFrQTZmTHdNVkROTGVFY0h1NnZTWjZ1ZkhyRExySkpFZXBILUwtYUM0TXloSzBKR2V0Yzhvcmc4TEJhbGozY3Z4MlUwSEVtSHh4RjF1MEFRWWhuTlNOdjg?oc=5>

## HEADWINDS

### JPMorgan (JPM) Stock May Be 31% Undervalued On Senate Probe News
- Summary: Senate probe may undervalue JPM shares, raising political risk.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQbHpMTjdWSDRrazRQMEM2dnVwV1JBdzlOWTVSaTMyY3ZwYVAxR0ttaE5wZmtTT0N6b3E2NWFDLUtUeEhzb2lxbEVOMHdZR04tUkNiTFZCbkd5UzZYaFRLeTc4TktPWXlqcUs2QWpMTHdaSFlaYWd5Y1c5UVFvdVo1TUkzS3dQekhtZWhxTm5ndUQzTE96?oc=5>

### JPMorgan Stock Slid After Reports That Senate Democrats Plan a New Investigation Into Jamie Dimon's Bank Over Its Jeffrey Epstein Relationship. Here's Why That Political Risk Could Weigh on JPM Shares.
- Summary: New investigation into Epstein ties could weigh on JPM shares.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigAJBVV95cUxOeE9uai1pckpIcnlZbTBOcERHWVR3Z1V6eUhuZkdpMWdZXzQzUTItenl2bFZHZjN0dFh5al9QbExtZWlNelRkWE1melJYZ181WUxScDc4QmNCT1BCaUtMa2J6OUUxVUhISUFITXM4OTQyQTk2Z0tVcW9PckJmWTJpUEx0Q0ZaV2FyUmtMYTJ1eFdhSEJ4OUVSMnRLaGFBU01sUXVaQTBabm1oX2l5NzExNEw4TExaUUViYmliVW5TdmtScGY5WUhRR0JJMWpqMVUyVEJUYm1GTXR4ZkJRaVBOajAxVml3RzdMQTM4QmxBQ01BNWo3aWRGZ0xaeTM1b1Mw?oc=5>

### ETFs Are Net Sellers of JPMorgan Chase (JPM) on Nov. 5
- Summary: ETFs sold JPM shares, indicating negative market sentiment.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQaGlWMXljWGtsTDNTQzZWNzBGNi12QVJQbTFMS1VyUFo5R2l5QVZZUEVGUWNtNmE1UUd6bWRqU3hNWGVidWFNbnpYYktDMjFsZUZlbXpXUTRNQmxPei1CVFdHWjk5M0tmaUFWaHEwVGhscVRUTzV2SklnSVVObE04M0xQSkFYMmVwVHpsSTFlTjFjUFY1eHB6dWdielU?oc=5>

### Bearish Signal Threatens JPMorgan Stock’s Rally
- Summary: Bearish signal threatens JPM rally, raising downside concerns.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQQ3ZJZ3dUellBTGpNWnp6U1p5QXR2S2pLcERRRF9KTTRScURXNkJsbzFJOWNwNmNzTlVOSXM4OG1mVVFJTEttRWFJWnZuWUxtMGViZ0x2bm82SHBXazJCNEVPUmVVSldkem5MYWwzNTFIbUgtTVNVS0VHNFkwZGRFdDdobGVMUWNmdWt3REdvMlY5X2Y0NW9nbkM4ZnowSHIzblhKTVMxZDU?oc=5>

## CATALYSTS

### JPMorgan Chase & Co. $JPM Stock Purchased by Pzena Investment Management LLC
- Summary: JPMorgan Chase & Co. $JPM Stock Purchased by Pzena Investment Management LLC
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxOaFl2RkI1UFFYazZjSHdRTDJpcjZFMFRSRTktWWtPQkJFSUJtZDU0aTZjZnh5MjVkRTBsREJYZHJLbVlId0VPa3pfLXNQZ3FNVEdUdjYyUWdOVExlZEFLem42dXRqbkRMQm5IdG1iN2wxdkxPeEFHR18xd0RzLUpOZkU0LV93bU9CYWJ3Q1JYLTE3UWd2SDYwVzBtNDN5SFdjNWg0X0tQTjdGemFQT2NQekpUejE5NHNsMHVtb0c5amZ3YmpjbldGSE1JVjB2Zw?oc=5>

### JPMorgan Chase & Co. (NYSE: JPM) Stock Analysis: Low-Teens P/E and a 1.75% Dividend Yield
- Summary: JPMorgan Chase & Co. (NYSE: JPM) Stock Analysis: Low-Teens P/E and a 1.75% Dividend Yield
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPMFp2TGFUOUZmdE9TR09iRGdBSEtSR3FjRlp5YVliaGlBTUxXZDR1b2w4alBkT09HWnZhMF84bzF6T0ZNQTJqbzRTUjlwZ1VzR2lWU3l0OUtlRFJNMlQ4cEpPUUVpWkdvRkNERjRVU1M0Nmx4WXFXRWNMdzlmREVHTUtjMndjeWFaVmtqZU9BN2hVNWxNRHZTcmF1QzQxUVliZHpOUElKNUoxY21hVGFDY1FaYmQwNUo4XzNwNEFzMUFUYzRp?oc=5>

### JPMorgan Chase & Co. (JPM) Up 2.4% Since Last Earnings Report: Can It Continue?
- Summary: Shares of JPM rose 2.4% after the latest earnings release, raising questions about sustaining the upward trend.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPeTd2Z2g4LXpqenNnYkozQUZBV1JUODhBeHdkcERHZENfOWpYWm5wU1pTXzRpcFBDX2d1dDdDcmk3cHFDTGtFVGdzYlpPYV9HWnVTeTc5SV90ekEtR29KVTFyb1JPb29FUGZNbXM5bzFuY3NxWWkyR3Q4SmVRZkhfUWN5WW5WbGJ4MGRqeGR3TVpqdw?oc=5>

### JPMorgan Chase Increases Crypto Exposure
- Summary: JPM expands crypto services, signaling new product offering.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQTmFqNmhWdGc2ZXhyZDhQcHdWMjhUWGxLeWFFdHFVekg2bjdJbDUtYlBhSFVoVGwxUXM3T1R0bkZyVDNjMDVaMUFrbUFqWHptZTVta01lbmp2Z1ZYQVYyY1BIYkg2VlY0NnNkTEVXMTg5NEY1dnhvS3pSRDhXZHhEUm1WSEFLVFA4TWdVQS1qeXItWTA4RzdranBmR1VZbmdQU0owR3gweEc?oc=5>

### JPMorgan Chase (JPM) Ramps Up Crypto Investments
- Summary: JPM expands crypto investments, diversifying portfolio and positioning for digital asset growth.
- Date: 2026-11-13 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxPUWJucHdkQ2xiUVY3TDBwTkFBRlU5ZFZSM1NyblJManRvaWZYNzBWbTI0UDlSYlgxTGFNYzNvemR6NDJ2WDFRZ0oyUVN6WF8wS0lVYVpNNDBzeWt2MzFBS1JQcjBBMENmRWVtV1dYYjgxRDNKT0NtWG9jYXg5TDhJRGtR?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **14.38** | **2.62** | **N/A** | **10.20** | **919,345,496,064.00 USD** | **14.02** |
| BAC | 12.06 | 1.30 | N/A | 3.40 | 352,048,676,864.00 USD | -1.44 |
| C | 12.09 | 1.07 | N/A | 8.00 | 205,261,914,112.00 USD | 25.73 |
| WFC | 12.10 | 1.63 | N/A | 0.40 | 258,309,226,496.00 USD | 3.88 |

Peers fetched as_of: 2026-11-13; JPM reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 24,246,000,000.00 USD; period 2014-07-01/2014-09-30; fiscal year/reporting period 2014/Q3
- Net income (latest available single quarter): 15,305,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/19617/000162828026069523/jpm-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMingFBVV95cUxNZEdSeWY5RUlCZ3QxZklmQ2hsTGJXdHdxU3hXQXkxQUJCZXJaMlpMYkc4SEtubncteGpGVVIxcWFtV19RdWF2bDNSQmY5UC1aVUo5U1NmQWRpSjlnWW1OUWRhMWdyb191VS1LV2g1QTZUTTFmR0hPXzQwU3pzbndINnJhU19xN0FtQ1pQR2xCN20wbTI4YnhyWi1EazJjdw?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNX1hTbFd0OGF4OTF2NWktQ19MNWtFTGRuQUMteHgzRDhNV0doWXFCWTJpM3RaVFdiOFl0M2ppdFN6TmxSWjBKVmd4X3MwQnA4RXp6TlBSam9pTzVSR1NNdzNVSUE1OElySFBtWnFkanNlVTN5SXZUSVdRTGJkcmhpNTVKUHYtSGxmNk5PYV9IeTZpT0phRVNMb1Q4bXdHX09ER2lKcUU2QVE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPdzVzbG44emM5UVNZaktmOUVnMlU4cUlFVXBORmZjU0MyWUxWNlc2YTRZRHhpM3JkMFBsLTN3bGJXcHBWQ2Nuc1hjdjloYTNJZ3RRS19vUWM1dkN3RXp3OFd2N0wtY1JFRFpnRFN1M2JxWE45YTRDVlVheHlvRU1Idy1RZTBqV0REMVlrT2ZJZ2pfRzRtTEhoM2hiZ0pQR3Q2?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOVEliaW5hSkRCZUg4Y091X3R5SzdEeEZtWVhwRy01UkN2dmwyeHpNUFhpLVprTlBQcTdWMGc4ZnluY2IyaGdzRHowZWdEaXFjemFwMUl2NDBwWm8zR0p6cFlVMVNFcjNkV2J1S1I3cFB0QkR4WEREOHdjbjBaR3dacTItaUh5VGQ5LTJhbndGaElTZTdMS3p2bGRpRUFpcWJ5cHlfSmYzeTdTbUtkS25PSlR0bVFDOVdUaHBlSE4xODJXaFRoc3fSAcsBQVVfeXFMT0pvVVRXQ3RNclRZR3gtSjBaUGJEOHczeGs5UnZDekF4OVFiOE1NQzU0N1Q5UjQ2NnNyQkVNaXMwNGRUM2VUcGx1UDdxLXZjSElvY2dlZndjZEhiWkFnM3dIVGM2bDNkOExCWDQybFloTUFZMGFrQTZmTHdNVkROTGVFY0h1NnZTWjZ1ZkhyRExySkpFZXBILUwtYUM0TXloSzBKR2V0Yzhvcmc4TEJhbGozY3Z4MlUwSEVtSHh4RjF1MEFRWWhuTlNOdjg?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQbHpMTjdWSDRrazRQMEM2dnVwV1JBdzlOWTVSaTMyY3ZwYVAxR0ttaE5wZmtTT0N6b3E2NWFDLUtUeEhzb2lxbEVOMHdZR04tUkNiTFZCbkd5UzZYaFRLeTc4TktPWXlqcUs2QWpMTHdaSFlaYWd5Y1c5UVFvdVo1TUkzS3dQekhtZWhxTm5ndUQzTE96?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNd0NtU25YWWN4Y2Mzc1ZoYS13dW5LS2R1QzNWOGU0SWhId0tHWFJTNVRJWDZ5T0htZ1ZOak5GOGsyRzl3anI5Ukc5Nm5CWGN4alB0QnRxcTJTNHpETDZoLThfVGJNcV9CY3pnLU44UTc2dkloaS1BNXRFTWw3ZC1iWXk1alBVZ1V6c2J3QUxkR0d6Q3B5M21XWEV3T0pJQ29lcVU4RlpHN1NBcHJrYlZJQWMzSW1mZWF2b0VwalEzT1YwMDVfTkHSAcsBQVVfeXFMT09SQm1XMUxYZklmM3F5Ty1oTWFNMVhyX2Fnb0J1VE5TbTVObGttMU1QWWpnWjR5LUF1dXBjSDczTVViWlBxcFlmeDZISzZRakxuaW1XSEJmT25Uamx3UzZxczUyWjg3Ul8zMXI2OUdiUjdJbjJyX2EzLXZNckVRMkZXYTNoZlMtakRZYzBDdW9pM0Y5c0ZLNkk2ZFRRQ1REbFZ3aGZXWXJVM01LNW5Wc2pGTERaUlROYTZ4bkd6eWpXY2FXWWtsQ1FGWEE?oc=5
- https://news.google.com/rss/articles/CBMigAJBVV95cUxOeE9uai1pckpIcnlZbTBOcERHWVR3Z1V6eUhuZkdpMWdZXzQzUTItenl2bFZHZjN0dFh5al9QbExtZWlNelRkWE1melJYZ181WUxScDc4QmNCT1BCaUtMa2J6OUUxVUhISUFITXM4OTQyQTk2Z0tVcW9PckJmWTJpUEx0Q0ZaV2FyUmtMYTJ1eFdhSEJ4OUVSMnRLaGFBU01sUXVaQTBabm1oX2l5NzExNEw4TExaUUViYmliVW5TdmtScGY5WUhRR0JJMWpqMVUyVEJUYm1GTXR4ZkJRaVBOajAxVml3RzdMQTM4QmxBQ01BNWo3aWRGZ0xaeTM1b1Mw?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxOeWhJZFVHamhINHpfeXBzN1pLcTU2MlZRY05PMlI4TGlLcVRFUkpIajRwdUNBOTYyWGpHTWhCWTlFLXdyekdkU185V3NYSDRVa1VBN1NMWDUxM2Mxd2FZZ0tBa282VGp1cnlZTkJvQVRSM05jSkF4ZmEzenJkRlZ0Tm5VNno?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQaGlWMXljWGtsTDNTQzZWNzBGNi12QVJQbTFMS1VyUFo5R2l5QVZZUEVGUWNtNmE1UUd6bWRqU3hNWGVidWFNbnpYYktDMjFsZUZlbXpXUTRNQmxPei1CVFdHWjk5M0tmaUFWaHEwVGhscVRUTzV2SklnSVVObE04M0xQSkFYMmVwVHpsSTFlTjFjUFY1eHB6dWdielU?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQQ3ZJZ3dUellBTGpNWnp6U1p5QXR2S2pLcERRRF9KTTRScURXNkJsbzFJOWNwNmNzTlVOSXM4OG1mVVFJTEttRWFJWnZuWUxtMGViZ0x2bm82SHBXazJCNEVPUmVVSldkem5MYWwzNTFIbUgtTVNVS0VHNFkwZGRFdDdobGVMUWNmdWt3REdvMlY5X2Y0NW9nbkM4ZnowSHIzblhKTVMxZDU?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxOaFl2RkI1UFFYazZjSHdRTDJpcjZFMFRSRTktWWtPQkJFSUJtZDU0aTZjZnh5MjVkRTBsREJYZHJLbVlId0VPa3pfLXNQZ3FNVEdUdjYyUWdOVExlZEFLem42dXRqbkRMQm5IdG1iN2wxdkxPeEFHR18xd0RzLUpOZkU0LV93bU9CYWJ3Q1JYLTE3UWd2SDYwVzBtNDN5SFdjNWg0X0tQTjdGemFQT2NQekpUejE5NHNsMHVtb0c5amZ3YmpjbldGSE1JVjB2Zw?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPMFp2TGFUOUZmdE9TR09iRGdBSEtSR3FjRlp5YVliaGlBTUxXZDR1b2w4alBkT09HWnZhMF84bzF6T0ZNQTJqbzRTUjlwZ1VzR2lWU3l0OUtlRFJNMlQ4cEpPUUVpWkdvRkNERjRVU1M0Nmx4WXFXRWNMdzlmREVHTUtjMndjeWFaVmtqZU9BN2hVNWxNRHZTcmF1QzQxUVliZHpOUElKNUoxY21hVGFDY1FaYmQwNUo4XzNwNEFzMUFUYzRp?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPeTd2Z2g4LXpqenNnYkozQUZBV1JUODhBeHdkcERHZENfOWpYWm5wU1pTXzRpcFBDX2d1dDdDcmk3cHFDTGtFVGdzYlpPYV9HWnVTeTc5SV90ekEtR29KVTFyb1JPb29FUGZNbXM5bzFuY3NxWWkyR3Q4SmVRZkhfUWN5WW5WbGJ4MGRqeGR3TVpqdw?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQTmFqNmhWdGc2ZXhyZDhQcHdWMjhUWGxLeWFFdHFVekg2bjdJbDUtYlBhSFVoVGwxUXM3T1R0bkZyVDNjMDVaMUFrbUFqWHptZTVta01lbmp2Z1ZYQVYyY1BIYkg2VlY0NnNkTEVXMTg5NEY1dnhvS3pSRDhXZHhEUm1WSEFLVFA4TWdVQS1qeXItWTA4RzdranBmR1VZbmdQU0owR3gweEc?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxPUWJucHdkQ2xiUVY3TDBwTkFBRlU5ZFZSM1NyblJManRvaWZYNzBWbTI0UDlSYlgxTGFNYzNvemR6NDJ2WDFRZ0oyUVN6WF8wS0lVYVpNNDBzeWt2MzFBS1JQcjBBMENmRWVtV1dYYjgxRDNKT0NtWG9jYXg5TDhJRGtR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
