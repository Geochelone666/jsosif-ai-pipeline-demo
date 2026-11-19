# V Intelligence Report

- ticker: **V**
- Report as_of: **2026-11-18**
- Market data as_of: **2026-11-18**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-11-18**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-19T05:51:17.927707+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 1, 'ai': 8, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/V** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 7 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 415.2200 |
| Return 1D (%) | -0.3719 |
| Return 1W (%) | -2.4274 |
| Return 1M (%) | 3.3230 |
| Return YTD (%) | 19.3255 |
| Return 1Y (%) | 30.2966 |
| Annualized volatility (%) | 22.9317 |
| Beta vs SPY | 0.3254 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 1.2725 |
| Downside deviation (rf=0, %) | 14.1105 |
| Sortino (rf=0) | 2.0680 |
| Historical VaR 95% (1D, %) | 1.8058 |
| Historical ES 95% (1D, %) | 2.8262 |
| Correlation vs SPY | 0.1952 |
| Tracking error vs SPY (%) | 24.3302 |
| P/E (trailing) | 33.70 |
| P/B | 21.66 |
| EV/EBITDA | 24.18 |
| Revenue growth (%) | 13.20 |
| Forward P/E (estimate) | 24.22 |
| Gross margin (%) | 97.68 |
| Operating margin (%) | 66.31 |
| Return on equity (%) | 63.51 |
| Free cash flow yield (%) | 2.71 |
| MA50 | 392.6920 |
| Close vs MA50 (%) | 5.7368 |
| MA200 | 347.1973 |
| Close vs MA200 (%) | 19.5919 |
| RSI (14, Wilder) | 53.4770 |
| MACD (12,26) | 7.8718 |
| MACD signal (9) | 9.8166 |
| MACD histogram | -1.9448 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 285, 'SPY': 285}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 415.2200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.3719 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.4274 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.3230 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 19.3255 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 30.2966 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.9317 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.1105 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.0680 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8058 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.8262 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1952 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.3302 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3254 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.1805 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2725 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.2246 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.6780 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.3070 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 63.5070 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.7085 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 33.7029 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.4770 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.9448 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.7368 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 19.5919 -> Clearly above the moving-average trend level.

## TAILWINDS

### PayPal and Stripe join Visa to help merchants prepare for AI agents that buy things
- Summary: Visa partners with PayPal and Stripe to support merchants using AI agents for purchases.
- Date: 2026-11-18 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQeDFpdWZMaDVnZ0R5OVNtX256UDVPZnhBNkFmd0xYSEotMTgzckF3ZVg5YUVNV25fMzNzQ0xwRDk5RzNxVjN1T2gzV3RidWhkVFFQQmhTYzllT19qeXVNZC1BU1ZzN3RUbjlaWDZzYTc1eUNtV0FvemotMmZ0ZldrbjJhdDRZNTdZU1REbGRVY3NvVllOZVNtQUdFaUFTbE5qTUVrR09oTXZwclBIemEyci1R?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Visa (V) Stock Gets Fair Value Bump As Analysts Lift Targets On New Growth Areas
- Summary: Visa (V) Stock Gets Fair Value Bump As Analysts Lift Targets On New Growth Areas
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNdGg3Q1R2bzk1WktDVWFnWGFQbkxGMHJocnRaVEJ4anhNXzZRYWxNdFVFVzA5dHQ3UGUxcURZMTJKWnRtT3huRzJydFliQjhIcWVranRKVl9TbWtadndhQk16ZFhicXBDank5TjR6V2hwcnRhZ2RMMjc2QTZ3dzN5Tl9JTFNiNl85MW5QMjdIbkU?oc=5>

### Visa (NYSE:V) Stock Jumps 1.2% - Time to Buy?
- Summary: Visa shares rose 1.2%, reflecting short-term positive market reaction.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOYWYyZU9CcllwdkZqV3EzSXUzdmpjU3pVa2ZKMDI3bTFrZmxxaHJzX1RiUUhmVGJLZlIta2pKOExHbG8wUHFoQVZfcUhpQkttN0RNY0VhakxLVE90S1JLS0pWMkhVZ2ZUYnM1YVlHZ21Nb25PNk1TOVp4cFpRbl9Vb3dHeHg4enZUWDFYajFod242Ukx5V215bnB3VUh5czA?oc=5>

### Visa (V) Stock Price Prediction: Visa holds near short-term support as analysts lift targets and traders lean slightly bullish
- Summary: Analysts raise targets, bullish sentiment; stock near short-term support.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNUkgwdTBBclV0Uk5EV2F4M1VHc2l4LW9feWRSR1NWUVF5c1M3djk2Sy11bk5wS1RZaFJlYXFjVkRaMDNRVzM2eUxBazZwUkZsMENUb1JFQ0lxc3dySUIwQUJwLXhraUxzb0RFUV9wZVpoTHc1WjBobUtHbkV2dUNvdzZKM0RMTk5mSWlXSG5FQVAzVlZ0R2c?oc=5>

### Visa vs. American Express: Which Stock Has More Growth Potential?
- Summary: Analyst comparison of Visa and AmEx growth prospects.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPcDF5UTRKUEViTTMtbVBiUWVTaEVZRFFiTjJJOE9NdEdMSnNnblNFZ2tEQ05JQmFoZzE1QTRBV3pmUEdyOGdPM0dtWC1SUmRxYVdNRGZ1Z3V2WkpJUWFoSGRCMXVIa1AtRmZUaVMwQ1hoWVd4VnVOS3FvNFFUWHRtSGQ0enlqaVpscmFaSGNMdjdfY3k2WFRFRUFoTmdub29ITmJCRDJCbmtpSVM0emF4SWJCNFNnVk1kMUE?oc=5>

### Visa Inc. $V Stock Position Cut by Bessemer Group Inc.
- Summary: Bessemer Group reduces its Visa holdings, signaling negative outlook.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPc1hKcDdMX1BmanJkcTE5cGMyLW1uZVVFOUlxRUdkNzVUTG9FQW1PbFduMUFsZmdtRWZUNUNZOUhNSkdUMHNCeHB5R1dFNDJ0TktseUVHWlNjWGF6dTdtSl9oUlFzRXNvUGNsVE1WbkZFdC1oMV9DSlhpdHNUeUtZcjJJY3VTQ3g0OUJ4UXl6UU82bTZpTTB4N0JFWXZCLXZlUnZEaTd4ZV9Lc3MzOHBFRVpR?oc=5>

### Visa (V) Stock Price Prediction: Visa holds a constructive pullback as analysts stay broadly positive
- Summary: Analysts predict a constructive pullback in Visa stock price.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOczhnSEFuZExsb0JGb0tyakZPT2RGTmh4eUs3VnlVam1fRnFUeHF2LWQzRlJBNTFSMUhha1dDbzRDUFk1OEdETUZzVGtQRU9IcTB4TGthZHVIb0h0SDN4TmppdGtibkhKVnRWWEZNWHZfYnJvZXYzV0pDQTMzWURZcXZEc1Z1T29VYXh5VGpwVGhxaklnbFA2TzFR?oc=5>

## RISKS

### Visa identified more than $1.4 billion in potential fraud. Scam activity rose 40% in six months.
- Summary: Visa uncovered over $1.4B in potential fraud, with scam activity up 40% in six months, highlighting significant security concerns.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNRl9NR0ZERmhCcm5aUnJwTWZzWnJPWWxYanBzenZEdWRwd3pHS2NyMmpBTEdiMXNrSjNvUnFBYlJYV19XdUphSHo5R0NER1NQdlc0eGctbWY1UWVSMnlIUmpOSjhoUzZuTlhGQzdsSmFLeFViUHYySzJKcEZqWllBSG5JVWs2ODBLaVdKLUNlc1pVWDlra2tGQUszRnExbHJBb3Nja2VLR3lfNmpWLUZSY1R6OGIzUlU?oc=5>

### Visa (V) Stock: Slides as New Report Reveals 62% Rise in Cyberattacks
- Summary: Cyberattack surge causes stock slide.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQOHlhU2tOTUl5WTVLVnBqeDhXbjlNV05XSTVfeHVzamkyOHRVS2d2SUdnUkR2S1dyXzF5b0RCWGFvT0p5aW4xalVReFk2Z2k5SWp4WHhrcXh4WXlnNXVnTEE2SW8tTmNDY3hJckxSWk9kVXpsVVAxQmNBUjZXQUJ2Qi1xdVlCMm1EcGZ5VGVlVHUzQ1k?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **V** | **33.70** | **21.66** | **24.18** | **13.20** | **774,717,505,536.00 USD** | **30.30** |
| MA | 33.79 | 83.09 | 24.92 | 14.00 | 560,488,579,072.00 USD | 22.73 |
| PYPL | 11.09 | 2.49 | 7.98 | 2.00 | 48,086,810,624.00 USD | -3.57 |
| AXP | 17.77 | 5.91 | N/A | 11.30 | 211,492,093,952.00 USD | -6.37 |

Peers fetched as_of: 2026-11-18; V reuses existing data (market data as_of: 2026-11-18); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-18

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-05
- Revenue (latest available single quarter): 5,840,000,000.00 USD; period 2019-04-01/2019-06-30; fiscal year/reporting period 2019/Q3
- Net income (latest available single quarter): 5,628,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1403161/000140316126000134/v-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMisgFBVV95cUxQeDFpdWZMaDVnZ0R5OVNtX256UDVPZnhBNkFmd0xYSEotMTgzckF3ZVg5YUVNV25fMzNzQ0xwRDk5RzNxVjN1T2gzV3RidWhkVFFQQmhTYzllT19qeXVNZC1BU1ZzN3RUbjlaWDZzYTc1eUNtV0FvemotMmZ0ZldrbjJhdDRZNTdZU1REbGRVY3NvVllOZVNtQUdFaUFTbE5qTUVrR09oTXZwclBIemEyci1R?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNdGg3Q1R2bzk1WktDVWFnWGFQbkxGMHJocnRaVEJ4anhNXzZRYWxNdFVFVzA5dHQ3UGUxcURZMTJKWnRtT3huRzJydFliQjhIcWVranRKVl9TbWtadndhQk16ZFhicXBDank5TjR6V2hwcnRhZ2RMMjc2QTZ3dzN5Tl9JTFNiNl85MW5QMjdIbkU?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOYWYyZU9CcllwdkZqV3EzSXUzdmpjU3pVa2ZKMDI3bTFrZmxxaHJzX1RiUUhmVGJLZlIta2pKOExHbG8wUHFoQVZfcUhpQkttN0RNY0VhakxLVE90S1JLS0pWMkhVZ2ZUYnM1YVlHZ21Nb25PNk1TOVp4cFpRbl9Vb3dHeHg4enZUWDFYajFod242Ukx5V215bnB3VUh5czA?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNUkgwdTBBclV0Uk5EV2F4M1VHc2l4LW9feWRSR1NWUVF5c1M3djk2Sy11bk5wS1RZaFJlYXFjVkRaMDNRVzM2eUxBazZwUkZsMENUb1JFQ0lxc3dySUIwQUJwLXhraUxzb0RFUV9wZVpoTHc1WjBobUtHbkV2dUNvdzZKM0RMTk5mSWlXSG5FQVAzVlZ0R2c?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPcDF5UTRKUEViTTMtbVBiUWVTaEVZRFFiTjJJOE9NdEdMSnNnblNFZ2tEQ05JQmFoZzE1QTRBV3pmUEdyOGdPM0dtWC1SUmRxYVdNRGZ1Z3V2WkpJUWFoSGRCMXVIa1AtRmZUaVMwQ1hoWVd4VnVOS3FvNFFUWHRtSGQ0enlqaVpscmFaSGNMdjdfY3k2WFRFRUFoTmdub29ITmJCRDJCbmtpSVM0emF4SWJCNFNnVk1kMUE?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPc1hKcDdMX1BmanJkcTE5cGMyLW1uZVVFOUlxRUdkNzVUTG9FQW1PbFduMUFsZmdtRWZUNUNZOUhNSkdUMHNCeHB5R1dFNDJ0TktseUVHWlNjWGF6dTdtSl9oUlFzRXNvUGNsVE1WbkZFdC1oMV9DSlhpdHNUeUtZcjJJY3VTQ3g0OUJ4UXl6UU82bTZpTTB4N0JFWXZCLXZlUnZEaTd4ZV9Lc3MzOHBFRVpR?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOczhnSEFuZExsb0JGb0tyakZPT2RGTmh4eUs3VnlVam1fRnFUeHF2LWQzRlJBNTFSMUhha1dDbzRDUFk1OEdETUZzVGtQRU9IcTB4TGthZHVIb0h0SDN4TmppdGtibkhKVnRWWEZNWHZfYnJvZXYzV0pDQTMzWURZcXZEc1Z1T29VYXh5VGpwVGhxaklnbFA2TzFR?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNRl9NR0ZERmhCcm5aUnJwTWZzWnJPWWxYanBzenZEdWRwd3pHS2NyMmpBTEdiMXNrSjNvUnFBYlJYV19XdUphSHo5R0NER1NQdlc0eGctbWY1UWVSMnlIUmpOSjhoUzZuTlhGQzdsSmFLeFViUHYySzJKcEZqWllBSG5JVWs2ODBLaVdKLUNlc1pVWDlra2tGQUszRnExbHJBb3Nja2VLR3lfNmpWLUZSY1R6OGIzUlU?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQOHlhU2tOTUl5WTVLVnBqeDhXbjlNV05XSTVfeHVzamkyOHRVS2d2SUdnUkR2S1dyXzF5b0RCWGFvT0p5aW4xalVReFk2Z2k5SWp4WHhrcXh4WXlnNXVnTEE2SW8tTmNDY3hJckxSWk9kVXpsVVAxQmNBUjZXQUJ2Qi1xdVlCMm1EcGZ5VGVlVHUzQ1k?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
