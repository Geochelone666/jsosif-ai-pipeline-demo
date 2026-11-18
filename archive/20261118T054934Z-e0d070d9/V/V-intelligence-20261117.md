# V Intelligence Report

- ticker: **V**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:05:06.091232+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 2, 'ai': 6, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/V** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 6 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-10

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 416.7700 |
| Return 1D (%) | -2.2722 |
| Return 1W (%) | -1.4728 |
| Return 1M (%) | 3.7087 |
| Return YTD (%) | 19.7710 |
| Return 1Y (%) | 28.9482 |
| Annualized volatility (%) | 22.9770 |
| Beta vs SPY | 0.3305 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 1.2250 |
| Downside deviation (rf=0, %) | 14.1754 |
| Sortino (rf=0) | 1.9855 |
| Historical VaR 95% (1D, %) | 1.8058 |
| Historical ES 95% (1D, %) | 2.8262 |
| Correlation vs SPY | 0.1982 |
| Tracking error vs SPY (%) | 24.3380 |
| P/E (trailing) | 34.62 |
| P/B | 21.74 |
| EV/EBITDA | 24.27 |
| Revenue growth (%) | 13.20 |
| Forward P/E (estimate) | 24.32 |
| Gross margin (%) | 97.68 |
| Operating margin (%) | 66.31 |
| Return on equity (%) | 63.51 |
| Free cash flow yield (%) | 2.70 |
| MA50 | 391.7219 |
| Close vs MA50 (%) | 6.3944 |
| MA200 | 346.7530 |
| Close vs MA200 (%) | 20.1922 |
| RSI (14, Wilder) | 54.7624 |
| MACD (12,26) | 8.9301 |
| MACD signal (9) | 10.3028 |
| MACD histogram | -1.3726 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 416.7700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.2722 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.4728 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.7087 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 19.7710 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 28.9482 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.9770 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.1754 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.9855 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8058 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.8262 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1982 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.3380 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3305 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.1805 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2250 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.3151 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.6780 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.3070 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 63.5070 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.6984 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 34.6154 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 54.7624 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.3726 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.3944 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 20.1922 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Visa (V) Stock Gets Fair Value Bump As Analysts Lift Targets On New Growth Areas
- Summary: Visa (V) Stock Gets Fair Value Bump As Analysts Lift Targets On New Growth Areas
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNdGg3Q1R2bzk1WktDVWFnWGFQbkxGMHJocnRaVEJ4anhNXzZRYWxNdFVFVzA5dHQ3UGUxcURZMTJKWnRtT3huRzJydFliQjhIcWVranRKVl9TbWtadndhQk16ZFhicXBDank5TjR6V2hwcnRhZ2RMMjc2QTZ3dzN5Tl9JTFNiNl85MW5QMjdIbkU?oc=5>

### Visa Inc. (NYSE:V) Stock Now Rated "Buy" by Wall Street Analysts
- Summary: Visa Inc. (NYSE:V) Stock Now Rated "Buy" by Wall Street Analysts
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOZzFfQ09haUVqblBwVDh1U0pQVHJZS2VhMEpMUFZxWndwdXRoeGpnX2VVSGhPbTcyRUtseC04dVVjczJXTDVhUnNuNWJBNEs5ZE9INU9OU1MySUVpR3hITi1CTDkwQmh4ejFtSEYwb3B4aV9NNTZoM2hVWDdDT1VMQzJDdU83RDlsZ1Bma3N5V1JKS3lYYndIdFBZaEtUSHlzUEJBZFVrYkw1akVBYjhTWF9ZQ2JGc0Y2TDNfUFlzaHA?oc=5>

### Visa (V) Stock Could Be Reasonable With Excess Returns Intact
- Summary: Speculation that Visa stock may remain attractive with excess returns intact.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPamgyTVlJR1Rza3hGS3VHejlSczNrQ2J0cndUSVM4cDlsQ0xsNWNkdzdtUVo5ZkZQOTJkSVZNNHcwWUkxMUNQQ0hrTmxCZU1wdUV6OHlla1VoTTlDZmRxTUhZTFhfbF8yMTVCTTVNYjEwR2d4clpoTzFHZkZ3aUhQeDVoZlJVOGxnWEtqZEVOdFUzLTJKekdoSDNB?oc=5>

### Visa (NYSE:V) Stock Jumps 1.2% - Time to Buy?
- Summary: Visa shares rose 1.2%, reflecting short-term positive market reaction.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOYWYyZU9CcllwdkZqV3EzSXUzdmpjU3pVa2ZKMDI3bTFrZmxxaHJzX1RiUUhmVGJLZlIta2pKOExHbG8wUHFoQVZfcUhpQkttN0RNY0VhakxLVE90S1JLS0pWMkhVZ2ZUYnM1YVlHZ21Nb25PNk1TOVp4cFpRbl9Vb3dHeHg4enZUWDFYajFod242Ukx5V215bnB3VUh5czA?oc=5>

### Visa (V) Stock Price Prediction: Visa Holds Above Key Support as Earnings Beat Meets Mixed Derivatives Signals
- Summary: Visa beat earnings expectations, supporting stock above key support levels amid mixed derivatives signals.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOLWlwVmc1aXJfZDZqWndnZmJsbFZfX1lKWlFtbmpNejhFQzlnZVFWNkc5ZkE1RWFJSjhwVzNpMlBMOUkwNEc1UU9XQkowbFYzNC1xd0hweWRiN2lIdEFtWTBhVjI3bnhQQzlrSVF5V2dKVHNpbngyVTJua1BBblhLVExPZ1R4eEwta09Xc0wyLS1aUQ?oc=5>

### Visa (V) Stock Price Prediction: Visa holds near short-term support as analysts lift targets and traders lean slightly bullish
- Summary: Analysts raise targets, bullish sentiment; stock near short-term support.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNUkgwdTBBclV0Uk5EV2F4M1VHc2l4LW9feWRSR1NWUVF5c1M3djk2Sy11bk5wS1RZaFJlYXFjVkRaMDNRVzM2eUxBazZwUkZsMENUb1JFQ0lxc3dySUIwQUJwLXhraUxzb0RFUV9wZVpoTHc1WjBobUtHbkV2dUNvdzZKM0RMTk5mSWlXSG5FQVAzVlZ0R2c?oc=5>

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
| **V** | **34.62** | **21.74** | **24.27** | **13.20** | **777,609,478,144.00 USD** | **28.95** |
| MA | 34.62 | 83.40 | 25.01 | 14.00 | 562,544,574,464.00 USD | 21.05 |
| PYPL | 11.22 | 2.50 | 8.01 | 2.00 | 48,269,553,664.00 USD | -5.06 |
| AXP | 17.97 | 5.92 | N/A | 11.30 | 211,746,914,304.00 USD | -6.42 |

Peers fetched as_of: 2026-11-17; V reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

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

- https://news.google.com/rss/articles/CBMikAFBVV95cUxNdGg3Q1R2bzk1WktDVWFnWGFQbkxGMHJocnRaVEJ4anhNXzZRYWxNdFVFVzA5dHQ3UGUxcURZMTJKWnRtT3huRzJydFliQjhIcWVranRKVl9TbWtadndhQk16ZFhicXBDank5TjR6V2hwcnRhZ2RMMjc2QTZ3dzN5Tl9JTFNiNl85MW5QMjdIbkU?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOZzFfQ09haUVqblBwVDh1U0pQVHJZS2VhMEpMUFZxWndwdXRoeGpnX2VVSGhPbTcyRUtseC04dVVjczJXTDVhUnNuNWJBNEs5ZE9INU9OU1MySUVpR3hITi1CTDkwQmh4ejFtSEYwb3B4aV9NNTZoM2hVWDdDT1VMQzJDdU83RDlsZ1Bma3N5V1JKS3lYYndIdFBZaEtUSHlzUEJBZFVrYkw1akVBYjhTWF9ZQ2JGc0Y2TDNfUFlzaHA?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPamgyTVlJR1Rza3hGS3VHejlSczNrQ2J0cndUSVM4cDlsQ0xsNWNkdzdtUVo5ZkZQOTJkSVZNNHcwWUkxMUNQQ0hrTmxCZU1wdUV6OHlla1VoTTlDZmRxTUhZTFhfbF8yMTVCTTVNYjEwR2d4clpoTzFHZkZ3aUhQeDVoZlJVOGxnWEtqZEVOdFUzLTJKekdoSDNB?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOYWYyZU9CcllwdkZqV3EzSXUzdmpjU3pVa2ZKMDI3bTFrZmxxaHJzX1RiUUhmVGJLZlIta2pKOExHbG8wUHFoQVZfcUhpQkttN0RNY0VhakxLVE90S1JLS0pWMkhVZ2ZUYnM1YVlHZ21Nb25PNk1TOVp4cFpRbl9Vb3dHeHg4enZUWDFYajFod242Ukx5V215bnB3VUh5czA?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOLWlwVmc1aXJfZDZqWndnZmJsbFZfX1lKWlFtbmpNejhFQzlnZVFWNkc5ZkE1RWFJSjhwVzNpMlBMOUkwNEc1UU9XQkowbFYzNC1xd0hweWRiN2lIdEFtWTBhVjI3bnhQQzlrSVF5V2dKVHNpbngyVTJua1BBblhLVExPZ1R4eEwta09Xc0wyLS1aUQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNUkgwdTBBclV0Uk5EV2F4M1VHc2l4LW9feWRSR1NWUVF5c1M3djk2Sy11bk5wS1RZaFJlYXFjVkRaMDNRVzM2eUxBazZwUkZsMENUb1JFQ0lxc3dySUIwQUJwLXhraUxzb0RFUV9wZVpoTHc1WjBobUtHbkV2dUNvdzZKM0RMTk5mSWlXSG5FQVAzVlZ0R2c?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNRl9NR0ZERmhCcm5aUnJwTWZzWnJPWWxYanBzenZEdWRwd3pHS2NyMmpBTEdiMXNrSjNvUnFBYlJYV19XdUphSHo5R0NER1NQdlc0eGctbWY1UWVSMnlIUmpOSjhoUzZuTlhGQzdsSmFLeFViUHYySzJKcEZqWllBSG5JVWs2ODBLaVdKLUNlc1pVWDlra2tGQUszRnExbHJBb3Nja2VLR3lfNmpWLUZSY1R6OGIzUlU?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQOHlhU2tOTUl5WTVLVnBqeDhXbjlNV05XSTVfeHVzamkyOHRVS2d2SUdnUkR2S1dyXzF5b0RCWGFvT0p5aW4xalVReFk2Z2k5SWp4WHhrcXh4WXlnNXVnTEE2SW8tTmNDY3hJckxSWk9kVXpsVVAxQmNBUjZXQUJ2Qi1xdVlCMm1EcGZ5VGVlVHUzQ1k?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
