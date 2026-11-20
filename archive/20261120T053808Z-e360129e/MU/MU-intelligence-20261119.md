# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:45:39.767473+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 1, 'ai': 11, 'unknown': 0, 'irrelevant': 12})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 8 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 45.83%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 690.4400 |
| Return 1D (%) | -2.1027 |
| Return 1W (%) | -13.5264 |
| Return 1M (%) | -23.6999 |
| Return YTD (%) | 142.0886 |
| Return 1Y (%) | 205.9597 |
| Annualized volatility (%) | 84.3935 |
| Beta vs SPY | 3.3769 |
| Max drawdown (%) | -45.8952 |
| Sharpe (rf=0) | 1.7499 |
| Downside deviation (rf=0, %) | 52.7806 |
| Sortino (rf=0) | 2.7979 |
| Historical VaR 95% (1D, %) | 7.3172 |
| Historical ES 95% (1D, %) | 10.3774 |
| Correlation vs SPY | 0.5562 |
| Tracking error vs SPY (%) | 77.5288 |
| P/E (trailing) | 9.49 |
| P/B | 5.64 |
| EV/EBITDA | 6.83 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 3.32 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 74.59 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 3.73 |
| MA50 | 919.8045 |
| Close vs MA50 (%) | -24.9362 |
| MA200 | 771.3009 |
| Close vs MA200 (%) | -10.4837 |
| RSI (14, Wilder) | 35.8628 |
| MACD (12,26) | -61.1778 |
| MACD signal (9) | -57.1188 |
| MACD histogram | -4.0590 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 690.4400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.1027 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -13.5264 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -23.6999 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 142.0886 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 205.9597 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 84.3935 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 52.7806 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.7979 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.3172 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.3774 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5562 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 77.5288 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3769 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -45.8952 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.7499 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 3.3232 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 74.5860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.7303 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.4880 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 35.8628 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.0590 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -24.9362 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -10.4837 -> Clearly below the moving-average trend level.

## TAILWINDS

### Micron Technology Shares Jump 4.69% After Hours - Taiwan Semiconductor (NYSE:TSM), Broadcom (NASDAQ:AVGO)
- Summary: Micron Technology Shares Jump 4.69% After Hours - Taiwan Semiconductor (NYSE:TSM), Broadcom (NASDAQ:AVGO)
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPLXEzQm5DOFRRZTdNaHpMTlE5RFdad29xMkFOZ0g5Zkxodkc0MGJXZXAxQVZ4TTg1NlNucHl1dHR3V3h1UDI4RGk2Q21QamxvS3pBZ2J4cjlQUjRPOTAzNHlWbTRMTXpjWjI5U3NYMUVtc05KQTNKVjV5d2FMQW1JbHNEQXE1Z29OZXJjMG5tTUM4OC1fT0o5WS1qZ3lJVnJNMWpaV0xkZjhGemc?oc=5>

### “Ridiculously Cheap” Micron Soars 7% on Revived AI Trade
- Summary: Micron shares jump 7% after AI demand revival boosts investor confidence.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQS0Q1RjBBdW5TaWtGQWdqWklQX1JkSDVfbWpkNkppZjEza2pianhqY0NOOTBfSDdHSFBFZi1PVG1WV0UzUlJzdGp2dU9WQzd3NHRDWHlsanNUeGdmdk9pLXBGeDUyUlY3LUlkRFFSYThQUVFXVXY0a0FYZWFSZl80Ung2T3M5cC13Qk9jTmpaQlhkNVI4MnVDR3BUcTNXaEk?oc=5>

### Micron Stock Draws Big Hedge Fund Bets as AI Memory Demand Surges
- Summary: Large hedge funds buy Micron, reflecting strong AI memory demand.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQLWtUX0FnNzhKM0QxXzByMkpoZUFNdXM5ZGlyNlZReFFqLWVoQXQwQWR5ZWtzR2NrMlRNZTV1UENVSEtNOVFKTVVIV2FBQWF1WUR5SVlpdG9IOFFrREtyTW9VbThmaUtvdl9Pc3NOWTA3UjhzOWNWR0R3TFg2c1puOFQ4SE1mcm1qenh2ak9YenZaUnJxVmZCUg?oc=5>

### Why Is Micron Technology Stock Rising Today?
- Summary: Analysts highlight positive market sentiment and potential upside for Micron, driving current stock gains.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNZG1XWC12Nm54SXpHQXlpcDhPNmJQRGxtNmdXcEo4TjZzYnNCeWhKOEwzQUktd08wNUg3Z2pDMm9FX0FXUVFpaVNreTdxeFM5WlBuX2ZNZTVtdHJJYncwaU0zRTBwalJ1NndRQ2dqZDFnbHA3cjFRSjc2VU9GWVh3OVloRkFlaENDRHRNakl0SG5NN0Q1ZXdLRXVWN3Zfc2It?oc=5>

### How Much Upside Is Left In Micron Stock?
- Summary: Investors assess remaining growth potential for Micron, suggesting continued upward momentum.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOYy1naDRFbTJCbzZmMU5TTE9FYmxnY3JYdWI2X2RzT3Y1WmZqb3NyNDFIcGZRTDNKQkNnejUtaXMycENGUnp4TW5PaWhNNmdUeHNobFZRZXVXSG1oMDZOTHItTlVRQm5SZGhoZ3o5V0RPeFhCUmhtZ1RPOWxWbEFpWndKQVVETENUYmJWRUlCR3AzdEZFV0tIN3B3?oc=5>

### The Dates That Matter Most For Micron Stock
- Summary: Key upcoming dates, such as earnings releases, are expected to influence Micron’s stock performance.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNZmQwTWJxOWg2eWZlT3FQcjlYbUtRSmhKcW92T2ZWa3BnaEVONnJUX05jOFVISDJ1ZUxMODlQOW0yVXQ3QVRHY0h1WWh0MGNhS2t1R2kwbzdLRWdLNTZKclhHRnVKNXBiak5RRXVBaUNWZnEtUzhYT2FjM0VrLUVJSG9ySTVKMUxfTmQ3TmJpemVPWnN0ODhSMG4tNHB1c0hyWnFQcw?oc=5>

### Not Micron, Not Sandisk. This Is My Top Memory Stock for 2027.
- Summary: A bullish outlook positions Micron as a leading memory stock for 2027, boosting investor confidence.
- Date: 2026-11-18 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOLU9SVFFVUDlDN1BiLTFSQmFsSElIMXZDOUN1WjV5REFlaGduVzk3VEJhZk9pWDVBRGpRc19WNXJwckpoZ01fS0lTTjZmU2lZODZvS3RLYnktTHgtRXhmTTNWWlNBdnJyTERTX2hkZUlmOHprVXN1YTJhUzNYSEtQcXBjM1lVU2tNVGRMS1YwYWtkdHJiRGlmWFA5cEYwZ3BSU2NKNA?oc=5>

## HEADWINDS

### Why Micron Stock Keeps On Going Down
- Summary: Micron shares decline, indicating market concerns.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQZThEaDlUMnZDUVE3Tk84REhENGlzOF9aSHVLU0F2VVdzSk42MU5KR1ZRdTlfMExmTFF4RWFfV3F3VHpzdXQ0NGpzRkhLelZkUXJQd21SdUY3c3V2TGdpWHZCWWp4UjIzYUUxSmxBTURQZFF6aVFzOEtfazlDM0Iycm93eHJTb1E5S0k2cEtTQ0thblFHMFZSVA?oc=5>

## CATALYSTS

### Micron Stock Is Down 41%, but the $35 Billion Buyback Could Change the Game. Here's How.
- Summary: Micron announces a $35 billion share buyback, potentially boosting stock value.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNS1huaXhkbmEtaUlvU2dCZl9iWTA2WDVJWEZvdS0yMERkWDhrbEpqSUhCbzFEOFZWa211ZkRPYjd0TkV1YktoSzJJeGFjZ0tHNDFIYkk2dEE1UV9hQlI4c2J2THQtU19KZ1pOb2JOSHVLa2d6bl9YVHRDS3llekpiSy1HTndLYjVQdEEtYmZ3SzI0amdGSS05Z1ptN2FtUVFrekc4ZTJjRlY4dkw4QUR0Qno5eWlPbVA1WTV4WXJWTW9NTnJkdXc?oc=5>

### Micron Stock: 3 Catalysts Set to Boost the Memory Chip Maker Beyond Nvidia Earnings
- Summary: Three new product developments are expected to lift Micron’s performance beyond Nvidia’s earnings.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTE1EUkd4T0FNR1lpSjgxY2pQMm5jR1dJYU1WLU9PT0tybjhIcGpFTTBqemF5djRKUFd2T0gzaENGQU9QUXhuQXhpQmdUNmlZcG50Q1RJMjhFSlRIUlhQWmpGZFZKWWVjRm8wcGk0WmFJaUxVeEkwdnQxQXVaX3g?oc=5>

### Is Micron Next to Announce a Stock Split?
- Summary: Speculation about a potential stock split could boost shares.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOUVpxd3RmaHk1MzdaTTdLMG9yb3ZzNGFOLUZkM0V1cXp6VlMxa0t6N25NbzRSeENDN0lSTVY3Zl90dWdwZHhmc1VnMm9QWEYzY2wxeGRKSGVySXZrWnNzRXBOaVRzQWlacTFYY1FIUFl4LXh2bWRRVG92a3BiQ2V0Z3BsazZmMVNFejhxcnROejg1VnZfbkRlejJXRW9FZw?oc=5>

## RISKS

### Micron Has Plunged 36% From Its Peak. Here’s the Price at Which I’d Buy.
- Summary: Micron’s share price fell 36% from its peak, raising concerns about valuation.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQTVZVemk2Q01NdFZ4QXVYRzBSNzBBX0g2UUxpN2FCZGhkY3REMWZRWUtuSW41VnVTTUlqUHlMVVNBWTdkN09aTWx1ZzVFWlRjVkJaN0owMGF2M1dRVS1QV01qcWFDalBERm50bXhsdHEtSlBXUXhodVZPVU9rbGRWd25GTFFDQ1N1SHlObFI4Zl9YMzdBcGd1NW0xMVgxUEdlcU5xckx3NXJYOUh3QmFVRlBB?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **9.49** | **5.64** | **6.83** | **379.30** | **781,179,879,424.00 USD** | **205.96** |
| WDC | 10.14 | 11.87 | 17.54 | 55.50 | 111,091,654,656.00 USD | 93.11 |
| STX | 27.34 | 34.69 | 20.64 | 61.00 | 119,690,870,784.00 USD | 102.39 |
| NXPI | 19.87 | 5.25 | 13.16 | 19.30 | 63,456,858,112.00 USD | 34.80 |

Peers fetched as_of: 2026-11-19; MU reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-09
- Revenue (latest available single quarter): 8,440,000,000.00 USD; period 2018-06-01/2018-08-30; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 28,243,000,000.00 USD; period 2026-02-27/2026-05-28; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPLXEzQm5DOFRRZTdNaHpMTlE5RFdad29xMkFOZ0g5Zkxodkc0MGJXZXAxQVZ4TTg1NlNucHl1dHR3V3h1UDI4RGk2Q21QamxvS3pBZ2J4cjlQUjRPOTAzNHlWbTRMTXpjWjI5U3NYMUVtc05KQTNKVjV5d2FMQW1JbHNEQXE1Z29OZXJjMG5tTUM4OC1fT0o5WS1qZ3lJVnJNMWpaV0xkZjhGemc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQS0Q1RjBBdW5TaWtGQWdqWklQX1JkSDVfbWpkNkppZjEza2pianhqY0NOOTBfSDdHSFBFZi1PVG1WV0UzUlJzdGp2dU9WQzd3NHRDWHlsanNUeGdmdk9pLXBGeDUyUlY3LUlkRFFSYThQUVFXVXY0a0FYZWFSZl80Ung2T3M5cC13Qk9jTmpaQlhkNVI4MnVDR3BUcTNXaEk?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQLWtUX0FnNzhKM0QxXzByMkpoZUFNdXM5ZGlyNlZReFFqLWVoQXQwQWR5ZWtzR2NrMlRNZTV1UENVSEtNOVFKTVVIV2FBQWF1WUR5SVlpdG9IOFFrREtyTW9VbThmaUtvdl9Pc3NOWTA3UjhzOWNWR0R3TFg2c1puOFQ4SE1mcm1qenh2ak9YenZaUnJxVmZCUg?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNZG1XWC12Nm54SXpHQXlpcDhPNmJQRGxtNmdXcEo4TjZzYnNCeWhKOEwzQUktd08wNUg3Z2pDMm9FX0FXUVFpaVNreTdxeFM5WlBuX2ZNZTVtdHJJYncwaU0zRTBwalJ1NndRQ2dqZDFnbHA3cjFRSjc2VU9GWVh3OVloRkFlaENDRHRNakl0SG5NN0Q1ZXdLRXVWN3Zfc2It?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOYy1naDRFbTJCbzZmMU5TTE9FYmxnY3JYdWI2X2RzT3Y1WmZqb3NyNDFIcGZRTDNKQkNnejUtaXMycENGUnp4TW5PaWhNNmdUeHNobFZRZXVXSG1oMDZOTHItTlVRQm5SZGhoZ3o5V0RPeFhCUmhtZ1RPOWxWbEFpWndKQVVETENUYmJWRUlCR3AzdEZFV0tIN3B3?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNZmQwTWJxOWg2eWZlT3FQcjlYbUtRSmhKcW92T2ZWa3BnaEVONnJUX05jOFVISDJ1ZUxMODlQOW0yVXQ3QVRHY0h1WWh0MGNhS2t1R2kwbzdLRWdLNTZKclhHRnVKNXBiak5RRXVBaUNWZnEtUzhYT2FjM0VrLUVJSG9ySTVKMUxfTmQ3TmJpemVPWnN0ODhSMG4tNHB1c0hyWnFQcw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOLU9SVFFVUDlDN1BiLTFSQmFsSElIMXZDOUN1WjV5REFlaGduVzk3VEJhZk9pWDVBRGpRc19WNXJwckpoZ01fS0lTTjZmU2lZODZvS3RLYnktTHgtRXhmTTNWWlNBdnJyTERTX2hkZUlmOHprVXN1YTJhUzNYSEtQcXBjM1lVU2tNVGRMS1YwYWtkdHJiRGlmWFA5cEYwZ3BSU2NKNA?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQNUtEWE45Si14U3NjVmpheXdPT3dpaXNvMDlDU09pTXJRd2NFZGg3T0hRblVyMnFoR2Y2WjVCM3JDSFh2OGVjTG1lYjFkblNJVk91SGZaNVBHdnN3TVhmekJsSnBDbXY0WkRtM1JHUW1YRnVYMVJENEEwcXdwOUFrSHJWbEpHLXk0MmhENGg1NzVmdzJJX0E?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQZThEaDlUMnZDUVE3Tk84REhENGlzOF9aSHVLU0F2VVdzSk42MU5KR1ZRdTlfMExmTFF4RWFfV3F3VHpzdXQ0NGpzRkhLelZkUXJQd21SdUY3c3V2TGdpWHZCWWp4UjIzYUUxSmxBTURQZFF6aVFzOEtfazlDM0Iycm93eHJTb1E5S0k2cEtTQ0thblFHMFZSVA?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNS1huaXhkbmEtaUlvU2dCZl9iWTA2WDVJWEZvdS0yMERkWDhrbEpqSUhCbzFEOFZWa211ZkRPYjd0TkV1YktoSzJJeGFjZ0tHNDFIYkk2dEE1UV9hQlI4c2J2THQtU19KZ1pOb2JOSHVLa2d6bl9YVHRDS3llekpiSy1HTndLYjVQdEEtYmZ3SzI0amdGSS05Z1ptN2FtUVFrekc4ZTJjRlY4dkw4QUR0Qno5eWlPbVA1WTV4WXJWTW9NTnJkdXc?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTE1EUkd4T0FNR1lpSjgxY2pQMm5jR1dJYU1WLU9PT0tybjhIcGpFTTBqemF5djRKUFd2T0gzaENGQU9QUXhuQXhpQmdUNmlZcG50Q1RJMjhFSlRIUlhQWmpGZFZKWWVjRm8wcGk0WmFJaUxVeEkwdnQxQXVaX3g?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOUVpxd3RmaHk1MzdaTTdLMG9yb3ZzNGFOLUZkM0V1cXp6VlMxa0t6N25NbzRSeENDN0lSTVY3Zl90dWdwZHhmc1VnMm9QWEYzY2wxeGRKSGVySXZrWnNzRXBOaVRzQWlacTFYY1FIUFl4LXh2bWRRVG92a3BiQ2V0Z3BsazZmMVNFejhxcnROejg1VnZfbkRlejJXRW9FZw?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQTVZVemk2Q01NdFZ4QXVYRzBSNzBBX0g2UUxpN2FCZGhkY3REMWZRWUtuSW41VnVTTUlqUHlMVVNBWTdkN09aTWx1ZzVFWlRjVkJaN0owMGF2M1dRVS1QV01qcWFDalBERm50bXhsdHEtSlBXUXhodVZPVU9rbGRWd25GTFFDQ1N1SHlObFI4Zl9YMzdBcGd1NW0xMVgxUEdlcU5xckx3NXJYOUh3QmFVRlBB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
