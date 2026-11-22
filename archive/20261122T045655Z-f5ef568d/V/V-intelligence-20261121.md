# V Intelligence Report

- ticker: **V**
- Report as_of: **2026-11-21**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-11-21**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-22T04:59:20.150701+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 17, 'rule': 5, 'ai': 8, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261121T053104Z-422ce34b/V** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 17 unique headlines; 8 named publishers; 0 exact duplicates; 17 HTTPS source links; largest publisher share 29.41%; oldest publication 2026-11-14

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 401.8700 |
| Return 1D (%) | -0.0945 |
| Return 1W (%) | -5.6111 |
| Return 1M (%) | -0.9731 |
| Return YTD (%) | 15.4890 |
| Return 1Y (%) | 25.0985 |
| Annualized volatility (%) | 23.1457 |
| Beta vs SPY | 0.3339 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 1.0861 |
| Downside deviation (rf=0, %) | 14.4533 |
| Sortino (rf=0) | 1.7394 |
| Historical VaR 95% (1D, %) | 1.8407 |
| Historical ES 95% (1D, %) | 2.9273 |
| Correlation vs SPY | 0.2062 |
| Tracking error vs SPY (%) | 24.5688 |
| P/E (trailing) | 32.62 |
| P/B | 20.97 |
| EV/EBITDA | 23.41 |
| Revenue growth (%) | 13.20 |
| Forward P/E (estimate) | 23.45 |
| Gross margin (%) | 97.68 |
| Operating margin (%) | 66.31 |
| Return on equity (%) | 63.51 |
| Free cash flow yield (%) | 2.80 |
| MA50 | 394.0485 |
| Close vs MA50 (%) | 1.9849 |
| MA200 | 347.9482 |
| Close vs MA200 (%) | 15.4971 |
| RSI (14, Wilder) | 43.8983 |
| MACD (12,26) | 4.2899 |
| MACD signal (9) | 8.0875 |
| MACD histogram | -3.7976 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 401.8700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.0945 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.6111 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -0.9731 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 15.4890 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 25.0985 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 23.1457 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.4533 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7394 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8407 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9273 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2062 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.5688 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3339 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.1805 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0861 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.4458 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.6780 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.3070 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 63.5070 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.7985 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 32.6193 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.8983 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.7976 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.9849 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 15.4971 -> Clearly above the moving-average trend level.

## TAILWINDS

### PayPal and Stripe join Visa to help merchants prepare for AI agents that buy things
- Summary: Visa partners with PayPal and Stripe to support merchants using AI agents for purchases.
- Date: 2026-11-18 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQeDFpdWZMaDVnZ0R5OVNtX256UDVPZnhBNkFmd0xYSEotMTgzckF3ZVg5YUVNV25fMzNzQ0xwRDk5RzNxVjN1T2gzV3RidWhkVFFQQmhTYzllT19qeXVNZC1BU1ZzN3RUbjlaWDZzYTc1eUNtV0FvemotMmZ0ZldrbjJhdDRZNTdZU1REbGRVY3NvVllOZVNtQUdFaUFTbE5qTUVrR09oTXZwclBIemEyci1R?oc=5>

## HEADWINDS

### Visa stock extends downward price move as seller pressure outweighs oversold signals
- Summary: Visa stock extends downward price move as seller pressure outweighs oversold signals
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNVy1wQkk0NXV5MHJ5S2tIOWdrVFNZLS1RYllGU1FCM2lNMW1ySG5fNXo3RTVwVmVqY3FaLURZUGtvM1FBVUZuZFhyRFN1ZVBvdEZZT010Snpfd1FGbUdLRlExT1FuaWNtMjlqdmVtWjVNM0RId01kTy1XQUEzX2J1UWh0WGplSWE2SGRYTXVyUQ?oc=5>

## CATALYSTS

### Visa (V) Stock Gets Fair Value Bump As Analysts Lift Targets On New Growth Areas
- Summary: Visa (V) Stock Gets Fair Value Bump As Analysts Lift Targets On New Growth Areas
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNdGg3Q1R2bzk1WktDVWFnWGFQbkxGMHJocnRaVEJ4anhNXzZRYWxNdFVFVzA5dHQ3UGUxcURZMTJKWnRtT3huRzJydFliQjhIcWVranRKVl9TbWtadndhQk16ZFhicXBDank5TjR6V2hwcnRhZ2RMMjc2QTZ3dzN5Tl9JTFNiNl85MW5QMjdIbkU?oc=5>

### Visa Inc. $V Stock Sold by Voya Investment Management LLC
- Summary: Visa Inc. $V Stock Sold by Voya Investment Management LLC
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQOGk1UjZhXzlGZnpjeU1Uc3RHbjJkWXE5TFZiUXRhSDk0TmJ2SEt6U1EwZkJpa0tWZXNFTlFKOWdkMXRvOHlHMjBndFQwYUlpUzczWk1wQ0JqY1V1OTByNHpxd05oOVl6SFhmSGp4VkItMHFaQ0xoMk5UY2xqTUlMbTJrZVpwT1ZiamJTaGdWcUdrTmZPc2I2ZHF2TmpCVnowcEVTWkNrMC1PZnk5b2hfdnpFOWhSdWs?oc=5>

### Visa Inc. $V Stock: Public Sector Pension Investment Board Increases Stake
- Summary: Visa Inc. $V Stock: Public Sector Pension Investment Board Increases Stake
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxOMkhDcUM1UUNvaGlBNlI4TGo5VFpadDRDdlhiNndTZFowS2tlTllOeHZqOVYzUWdEbi11VEJNMnhGQ3hSWVFsVkdjMjYzRkpNMVFMNE55V3lxSUV0YkstUG9Za1NPVVFxcVZjOUNCT09hUDQ2NVBoM0JzX1RqS2N4a0ZIRUNJeXkzSXpOYXhDTlVfSENlQ2daeTZVWm1jSkpjVmJJN29wUFg4VDhDSTJaOElubVlDMnUxOHZzYS1ucWQ1WHJ5ZElpNDQwalQ?oc=5>

### Visa Inc. $V Stock Sold by Danske Bank A S
- Summary: Visa Inc. $V Stock Sold by Danske Bank A S
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPcnU2QmVMeGhob2E3WDhtRW1VMmsxMlNEVjV2MXhnX083bmpFRDlaSG5NeFcyaVJkbW5zbnBXSTZfdVkwa01DZWNLQTZqaHJZbFBHaUZxaXdKT2EweVd1VTFlZGpaekRuU1RVSXV6ZEcyVGdxdmdSanFnWHdkOGRGVzAwNDc1dGtuSGI3UVJWbjJEMW1YT3dlcl9xZmRTLU1NVGo0?oc=5>

### Visa Inc Stock (V) Moved Down by 3.45% on Nov 19: What Signal Does It Send?
- Summary: Visa stock fell 3.45% on Nov 19, indicating potential short‑term weakness.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxOY1FrekJiSXVObHpDVjY1ZzVxMzZ1ME5hN2hPMFN5X3N6MXBXOWlWSFAwalNDbzhYbEE1WjliZFI2aEN6VDBkbzJobUFPQ0gwSmUwdFJSNXBlX2VYQkNhWHF6NllLXzdjaXJYak1DdFBoT2l6Q0hlMEpLYXJqc3lzaG9KeGY0Qk0?oc=5>

### Visa (V) Stock Price Prediction: Visa holds a constructive pullback as analysts stay broadly positive
- Summary: Analysts predict a constructive pullback in Visa stock price.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOczhnSEFuZExsb0JGb0tyakZPT2RGTmh4eUs3VnlVam1fRnFUeHF2LWQzRlJBNTFSMUhha1dDbzRDUFk1OEdETUZzVGtQRU9IcTB4TGthZHVIb0h0SDN4TmppdGtibkhKVnRWWEZNWHZfYnJvZXYzV0pDQTMzWURZcXZEc1Z1T29VYXh5VGpwVGhxaklnbFA2TzFR?oc=5>

### Visa (V) Stock Price Prediction: Visa Holds Near Key Support After a Choppy Pullback
- Summary: Visa stock near key support after pullback, predicted to hold.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNS1p1WWdSazdtWklLX21EbFRDaG0yREVBYzE3ZVhPdDlzSi1oM21GTk5NNTROLXZuRDA2emxyalpsQnhfWXRnTzFKNFpTSUNiblQ0M2RPbFlKNDU5TDh6Tkh0RTFsZm12d3hFMUtCLXlYOEZxY0RiRWl2Um1vREtUQ1ZJUWE2SWZFMTg0S1ZjamV0YjdR?oc=5>

### Visa (V) Stock Price Prediction: Visa holds near short-term support as analysts lift targets and traders lean slightly bullish
- Summary: Analysts raise targets, bullish sentiment; stock near short-term support.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNUkgwdTBBclV0Uk5EV2F4M1VHc2l4LW9feWRSR1NWUVF5c1M3djk2Sy11bk5wS1RZaFJlYXFjVkRaMDNRVzM2eUxBazZwUkZsMENUb1JFQ0lxc3dySUIwQUJwLXhraUxzb0RFUV9wZVpoTHc1WjBobUtHbkV2dUNvdzZKM0RMTk5mSWlXSG5FQVAzVlZ0R2c?oc=5>

### Visa Inc. $V Stock: Edgewood Management LLC Trims Holdings
- Summary: Edgewood Management LLC reduced its Visa holdings, indicating a shift in investment strategy.
- Date: 2026-11-21 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPdWNSSWQwZk0zbUZXb3NsVzFYU0gxOWtQSE9XTUZtWEtyd2p3TzNSbWNuU0ZQQjUwMzRqVHhrZTNZZk15WmEyUjZ5d2VIYzk3UDVRTGJvbDdDTTRvTXE0S1JscHNOWGw3XzQtZGUwbTJtaEU1NEkwV3RuaWpNMndhWG1qbzltcWJJaG1rbDFvX0pyZDN5SG95VWw1UHFORUlocnE2VTlucU53YmxkeFZZT2ZSbnJRVlE?oc=5>

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
| **V** | **32.62** | **20.97** | **23.41** | **13.20** | **749,809,041,408.00 USD** | **25.10** |
| MA | 32.74 | 80.79 | 24.25 | 14.00 | 544,999,112,704.00 USD | 19.27 |
| PYPL | 10.17 | 2.29 | 7.40 | 2.00 | 44,265,783,296.00 USD | -7.48 |
| AXP | 17.00 | 5.66 | N/A | 11.30 | 202,305,552,384.00 USD | -11.26 |

Peers fetched as_of: 2026-11-21; V reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-21

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
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNVy1wQkk0NXV5MHJ5S2tIOWdrVFNZLS1RYllGU1FCM2lNMW1ySG5fNXo3RTVwVmVqY3FaLURZUGtvM1FBVUZuZFhyRFN1ZVBvdEZZT010Snpfd1FGbUdLRlExT1FuaWNtMjlqdmVtWjVNM0RId01kTy1XQUEzX2J1UWh0WGplSWE2SGRYTXVyUQ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNdGg3Q1R2bzk1WktDVWFnWGFQbkxGMHJocnRaVEJ4anhNXzZRYWxNdFVFVzA5dHQ3UGUxcURZMTJKWnRtT3huRzJydFliQjhIcWVranRKVl9TbWtadndhQk16ZFhicXBDank5TjR6V2hwcnRhZ2RMMjc2QTZ3dzN5Tl9JTFNiNl85MW5QMjdIbkU?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxQOGk1UjZhXzlGZnpjeU1Uc3RHbjJkWXE5TFZiUXRhSDk0TmJ2SEt6U1EwZkJpa0tWZXNFTlFKOWdkMXRvOHlHMjBndFQwYUlpUzczWk1wQ0JqY1V1OTByNHpxd05oOVl6SFhmSGp4VkItMHFaQ0xoMk5UY2xqTUlMbTJrZVpwT1ZiamJTaGdWcUdrTmZPc2I2ZHF2TmpCVnowcEVTWkNrMC1PZnk5b2hfdnpFOWhSdWs?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxOMkhDcUM1UUNvaGlBNlI4TGo5VFpadDRDdlhiNndTZFowS2tlTllOeHZqOVYzUWdEbi11VEJNMnhGQ3hSWVFsVkdjMjYzRkpNMVFMNE55V3lxSUV0YkstUG9Za1NPVVFxcVZjOUNCT09hUDQ2NVBoM0JzX1RqS2N4a0ZIRUNJeXkzSXpOYXhDTlVfSENlQ2daeTZVWm1jSkpjVmJJN29wUFg4VDhDSTJaOElubVlDMnUxOHZzYS1ucWQ1WHJ5ZElpNDQwalQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPcnU2QmVMeGhob2E3WDhtRW1VMmsxMlNEVjV2MXhnX083bmpFRDlaSG5NeFcyaVJkbW5zbnBXSTZfdVkwa01DZWNLQTZqaHJZbFBHaUZxaXdKT2EweVd1VTFlZGpaekRuU1RVSXV6ZEcyVGdxdmdSanFnWHdkOGRGVzAwNDc1dGtuSGI3UVJWbjJEMW1YT3dlcl9xZmRTLU1NVGo0?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxOY1FrekJiSXVObHpDVjY1ZzVxMzZ1ME5hN2hPMFN5X3N6MXBXOWlWSFAwalNDbzhYbEE1WjliZFI2aEN6VDBkbzJobUFPQ0gwSmUwdFJSNXBlX2VYQkNhWHF6NllLXzdjaXJYak1DdFBoT2l6Q0hlMEpLYXJqc3lzaG9KeGY0Qk0?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOczhnSEFuZExsb0JGb0tyakZPT2RGTmh4eUs3VnlVam1fRnFUeHF2LWQzRlJBNTFSMUhha1dDbzRDUFk1OEdETUZzVGtQRU9IcTB4TGthZHVIb0h0SDN4TmppdGtibkhKVnRWWEZNWHZfYnJvZXYzV0pDQTMzWURZcXZEc1Z1T29VYXh5VGpwVGhxaklnbFA2TzFR?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNS1p1WWdSazdtWklLX21EbFRDaG0yREVBYzE3ZVhPdDlzSi1oM21GTk5NNTROLXZuRDA2emxyalpsQnhfWXRnTzFKNFpTSUNiblQ0M2RPbFlKNDU5TDh6Tkh0RTFsZm12d3hFMUtCLXlYOEZxY0RiRWl2Um1vREtUQ1ZJUWE2SWZFMTg0S1ZjamV0YjdR?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNUkgwdTBBclV0Uk5EV2F4M1VHc2l4LW9feWRSR1NWUVF5c1M3djk2Sy11bk5wS1RZaFJlYXFjVkRaMDNRVzM2eUxBazZwUkZsMENUb1JFQ0lxc3dySUIwQUJwLXhraUxzb0RFUV9wZVpoTHc1WjBobUtHbkV2dUNvdzZKM0RMTk5mSWlXSG5FQVAzVlZ0R2c?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPdWNSSWQwZk0zbUZXb3NsVzFYU0gxOWtQSE9XTUZtWEtyd2p3TzNSbWNuU0ZQQjUwMzRqVHhrZTNZZk15WmEyUjZ5d2VIYzk3UDVRTGJvbDdDTTRvTXE0S1JscHNOWGw3XzQtZGUwbTJtaEU1NEkwV3RuaWpNMndhWG1qbzltcWJJaG1rbDFvX0pyZDN5SG95VWw1UHFORUlocnE2VTlucU53YmxkeFZZT2ZSbnJRVlE?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNRl9NR0ZERmhCcm5aUnJwTWZzWnJPWWxYanBzenZEdWRwd3pHS2NyMmpBTEdiMXNrSjNvUnFBYlJYV19XdUphSHo5R0NER1NQdlc0eGctbWY1UWVSMnlIUmpOSjhoUzZuTlhGQzdsSmFLeFViUHYySzJKcEZqWllBSG5JVWs2ODBLaVdKLUNlc1pVWDlra2tGQUszRnExbHJBb3Nja2VLR3lfNmpWLUZSY1R6OGIzUlU?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQOHlhU2tOTUl5WTVLVnBqeDhXbjlNV05XSTVfeHVzamkyOHRVS2d2SUdnUkR2S1dyXzF5b0RCWGFvT0p5aW4xalVReFk2Z2k5SWp4WHhrcXh4WXlnNXVnTEE2SW8tTmNDY3hJckxSWk9kVXpsVVAxQmNBUjZXQUJ2Qi1xdVlCMm1EcGZ5VGVlVHUzQ1k?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
