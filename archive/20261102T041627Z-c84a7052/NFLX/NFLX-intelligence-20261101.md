# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-11-01**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-11-01**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-02T04:26:34.390581+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 3, 'ai': 13, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **17** exact headline/source/date matches; prior report **20261101T014405Z-e49d1192/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'low_uncalibrated_model_confidence': 3}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 12 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 26.09%; oldest publication 2026-10-25

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 62.0800 |
| Return 1D (%) | 0.0484 |
| Return 1W (%) | -5.7251 |
| Return 1M (%) | -10.7790 |
| Return YTD (%) | -33.7884 |
| Return 1Y (%) | -42.9936 |
| Annualized volatility (%) | 35.9083 |
| Beta vs SPY | 0.1954 |
| Max drawdown (%) | -46.4449 |
| Sharpe (rf=0) | -1.3914 |
| Downside deviation (rf=0, %) | 26.4417 |
| Sortino (rf=0) | -1.8896 |
| Historical VaR 95% (1D, %) | 3.5133 |
| Historical ES 95% (1D, %) | 5.1308 |
| Correlation vs SPY | 0.0696 |
| Tracking error vs SPY (%) | 37.2698 |
| P/E (trailing) | 17.94 |
| P/B | 8.70 |
| EV/EBITDA | 16.56 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 16.46 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 34.63 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 9.86 |
| MA50 | 72.6726 |
| Close vs MA50 (%) | -14.5758 |
| MA200 | 81.5963 |
| Close vs MA200 (%) | -23.9182 |
| RSI (14, Wilder) | 30.6180 |
| MACD (12,26) | -2.7384 |
| MACD signal (9) | -2.1886 |
| MACD histogram | -0.5498 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 62.0800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.0484 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.7251 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -10.7790 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -33.7884 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -42.9936 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.9083 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.4417 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.8896 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.5133 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1308 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0696 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.2698 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.1954 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -46.4449 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.3914 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.4610 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 34.6320 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.8553 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.9422 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 30.6180 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.5498 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -14.5758 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -23.9182 -> Clearly below the moving-average trend level.

## TAILWINDS

### What Should Netflix Stock Investors Be Watching Now?
- Summary: Provides current factors investors should monitor for Netflix stock performance.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQUHJTT2tVYjBfMGpTdlVzaE1DWlF4NHdNOFZpeENYcjB0OEw4QzlPSF84Q3hGYy1EQVFmZHp6V0l1N2J3SUNHNTdMb0RMS3FTMUFYV1EzWGZxTmtTM2lUYmVHLWp6Q3lMZU9sQ0FMVEJGaHNGOTVSb2pnWDlQRnJvSXBMSl93SWxmWVlENklwbmlHcEcxdWpnNGx1VkJNdkxVSlE4bm9yd0dxYlVTVmNUSWpR?oc=5>

### Netflix Should Never Say Never To Reinventing Itself (NASDAQ:NFLX)
- Summary: Netflix emphasizes continuous reinvention, highlighting strategic product innovation and long-term growth prospects.
- Date: 2026-10-30 | Impact: medium | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQY25aRjVOYlpTOUFjenBCbW8wQ1BEMU55SFZ2dlkwaUVydjBWOFdDREFzelhBeTBpanN3ZUgzUTdLWFRtamNYZDQxOGFacFlkeTZ1ak5KX2FWMGc4NXBEeGZIYkxKTVNBOC0xU0JFR09FT0NiV2xMc2xQVGFHQmFpdzBKSTJXdkl4Yk9PQzlCVVZXaWtFUHJRUw?oc=5>

### The Battle That May Matter Most for Netflix Stock Isn't Against Disney
- Summary: Explores other competitors impacting Netflix stock beyond Disney.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNMEJjQl9vSl9kWk5nemlNQW5QangydndZUU9JRW52bjhwZ1ozX0Fnd0xhc21iUjBfNXNUV0VibVVUaHpmeFpWLVBEcHlpMXFkbXFZSzBBUzd1OV93a091XzVxdjQ0bDNyV0dYTFVaMmJuektoVmM3Z21XQW9aZUVxRVpPemFIaU5NdGZDX2tJY2pUYnRHRmY0?oc=5>

## HEADWINDS

### Netflix Shares Are Down 9% Since Earnings. Is the Stock a Buy?
- Summary: Netflix Shares Are Down 9% Since Earnings. Is the Stock a Buy?
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPZ1pZb216M0NKaGhqWmdoXzkwOC1TQjFzRExLVEpXYVpSU19HTWN5QUVKbTg3cGNYem9nQmw5Mmsxd0V1M2IyMmJQWDJrdUszTllwRmFsRG5UNTZpTjRrVWRCYzBsdGlGazhkeGFwNW5ENUhXRzFEOUJ1U0J4aHJtaDhYdW5hNWdPM1FCajlZZk1pUQ?oc=5>

### Netflix Is Down 51% From Its High. History Suggests This Is What Happens Next.
- Summary: Shares dropped 51% from peak, hinting at potential further decline.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPZTg4c2VtT2d1SV9meTFhZFpzN2ItRk85YXlQWnAwQUxDRm5VMmhBU0RrVXAyRWROcWk4RUpFdk4yWlhkc3dlUjFyU3hkVDVkaklFNC0zTmRPRmJZNHQxN2xvYmQtMVlDVm9Bd2VJdkZIOEI1Mnh0blZMNEJ4d0FGOXBvY25ic1UwV2NYa2ZPcw?oc=5>

## CATALYSTS

### Netflix's U.S. Audience Engagement Problem Is Hurting The Stock (Rating Downgrade)
- Summary: Netflix's U.S. Audience Engagement Problem Is Hurting The Stock (Rating Downgrade)
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOY3JYbDhETktQMDhGRklxQl8wM3d0YkFPdGpia3dkaFlXdUxlczVzVlFBTlVVTkRUSWw4MF9PbHZyazd5bE9EejVzR2ZBVmowNTZ2dWZuMDZ5aGhZQ3IxS3VkMmg0TFBDSFAyQ0R3OGxIMklaLV9xUEdLZGY4Q0VxTWFsal80OUZuQjRXSUZ0QUNxR2x1aTgwcVhGUnlKY1RoblJkZGZuNjlIVHZtWkpsd3ZzYWFiSUZ1RlE?oc=5>

### Netflix's Problem Isn't Profits. It's Viewing Time.
- Summary: Netflix's Problem Isn't Profits. It's Viewing Time.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNUkI4X0RpN3VILXY2MExJTlctZGZ5dWk5MDhqRTZDc2JJdzdiclBEcVNLNFI4YktGVWRzbGx0aUQyeGMxamNwNU8tOEF6aFJZR1l3SUtiZ0JqMDAxSEdqTFFhaGFGdmVGNm5YWkN2QVNub0ZXa3RFVEJ4bldTSnRTMFROSVdFZEZWaUpFdGw5SEl5MEktWWJYbnpiX1VfNXE5QVEtUw?oc=5>

### Netflix Stock: A $275bn Company Priced At No Growth (NASDAQ:NFLX)
- Summary: Despite a $275B market cap, Netflix shows limited growth, raising concerns about future earnings and valuation.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNaUJrZk9aRDR5YV9IeFVvQ2cwMzlQLXJmRkxiZkVVOXVfbXhJa0p1aXE1VUJ2aE94TEFYbGlTQTBhbDJlSkpyWW84c3RmTFlrS2RtV0VGa0haTHBjbTZHUnNJbENnSUgxc1k1ZXlubElZMTd1Yld2VFpYQUZ1N2NrTnpma29rNEtyQ2FvMA?oc=5>

### Netflix Spent $4.8 Billion Buying Back Stock in 1 Quarter. Here's What That Tells You.
- Summary: Netflix repurchased $4.8B of shares this quarter, signaling confidence and potentially boosting EPS per share.
- Date: 2026-10-30 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQUjViaXJMRjdUcktWc0Y0bWRGX2ViaHA4UXhJcTREbks0LUZjcGNYSzNqZl9CTHZEd3kwLUFhZFNhcDNwaVYtVnJ3cUltT1p4NkZNcTdrSE1oZVpZQzVLZHpySjdCYTV4QXVJdXhFcW9LWU1MUC0zcDl2RVp2QUwxb3liRDVWRVd4WHFFZWZwLV9RVzlx?oc=5>

### Netflix, Inc. (NFLX) Stock Forecasts
- Summary: Predictions for future performance of Netflix shares.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxOeFN4ZjN0Q0RPX3AxYTVZemJxVHhNemRHWDBhdWhRSXdzRklENkdic24yUloyQjNONFhobWgxb0F6R1N5ZGp3RW52SWRHWjE2RW5tRE5qOTBCYlVXZ3VoY2pQQ1lpaFp0V1c0bXpXcXlicEhVdjBWeGNBaTkweDBWWG1Tb1k1WDBXU29kLWtn?oc=5>

### Netflix: Price Increases Are No Longer Providing Unchecked Upside (Downgrade) (NFLX)
- Summary: Downgrade signals Netflix's price hikes no longer yield upside.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxONkdVeC1kd29pUUlKbjZfd3lYckhoSFNnbktmU1VIbVFBR08yV3pYcWo3TDkzbE43SnBJQ2RlTE84OUhnTnRnYWNsTVo4N2hBMlVKdVotVWdDVV9IdGhxbWJKLUd3Yk1fZDBKTzc0Uk1SUzc1RUdBLXpqVkdfWkV4ay1FOXpwTTNvMGZGUmxiUEJUdlVnZW1pZ2RXWW1GNC1JaVczaWczU01NRWJ6UTV2Rm9VNUZMZw?oc=5>

### Options Volatility Rises for Netflix (NFLX) Ahead of Market Move
- Summary: Increase in options volatility for Netflix before a market event.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMizAJBVV95cUxPOXRvVWhSa2Fxam1fVHRJYWdjWUlydjZlOUlvekxuVUhTSm1obXIyYlBzSUpqdXByUkUxZnRERW5FU2xJWmk1Qk03c3N5azA5UE5ta2VVZUU0UmlqaUVBSDZ5cERZZEhFT1RzX1hXODA3UEl4dXBNRlpnb19ZZ19TNVFhVzB1UlJ2NU5yNDZVcThhRkNmRjEzWnZ6UnRFNkd0ZFZzM09DZHdtajEzRVZKei02MnIwcXNvM1Q3VkpiaWFDMUgtbzRzSk90Q1B5TUFybEpjUUxfVDVqX19vMDdmXzZ0bkFka3Jlek5XUVZwakU5RHNLMXIyaTlqaWdxYWtNN1ZLZWs1V20xUXVxMy1VR1M1d2FjNkZGVE51ZkFYbjllUHN3MkhVOU1IOUgzekN4TFptcnRRMXk2c1Q1TEE1OEpWTW1qbS1kQnM5cg?oc=5>

### Wall Street Is Treating Netflix Like It's Broken, But I'm Still Bullish (NASDAQ:NFLX)
- Summary: Analyst remains bullish despite market skepticism.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPRnlVQVVLX05hNGdyek9rTjNybEw5b2lJcEFnN3BlMElCNEpDZmpRcnJfSDNWbHRxS2NXS3NyQ1FkbDZLZzAzdjl0RklFMk55aTZ4REF2SDlnVWpGZmk4T2NHTGNoSVVUZWM3WTVWMkl0UEFDSFJiRllqX3RRLXBXZkpIY21HTzhWZ0ZIemdvVnoxT0VqZC1UamZPTENnWDloNmZ6VDBZVWN0QQ?oc=5>

### Netflix, Inc. (NFLX) Stock forecasts
- Summary: Forecasts for Netflix stock performance.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNT1JCQVk2LWJnZUtua1ptNXZzNFgyYzBVSUNEMUxSZjRweHdvZklPNlNyeHZYaVRYWklrRzl0QXhLeVBIX25NdjJocUYwZUllcDlycjhsZDFUcENHeENCejlXZlJFM1htMU53VHUxUWthdlpGZW5xd0hMMGtyREdTY3Q0U2ZjQXVnTjFpaUc1SDY?oc=5>

### Why Netflix Stock Could Double From This Dip
- Summary: Analysis suggests Netflix stock may rise significantly after a recent dip.
- Date: 2026-11-01 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOZ2xkUHpTZ1FLVE9NNFlqQU4yRVg4d2xMcWk0ZDNGNUwzLWtKVldUbF9SVXNLSFJMZkRNUnhLYTZ6NWc3ZEc2dDNVcjNTTDk3c0pZblc2OVdtZkY1ZFhhZWc5MGE0NkRUSmpicTNXcDJTdDdJVFBmRXZFck1hUGRUYUtjSUU5eWZiOTNibXhHRzIwcGVaX3RESGtScw?oc=5>

## RISKS

### Is Netflix (NFLX) A Bargain After Its 2026 Guidance Reset?
- Summary: Investors question if Netflix remains a bargain following its 2026 guidance reset, suggesting possible long-term downside risk.
- Date: 2026-10-30 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQYXFIRXR2UFNyNHdHZFVwM0FwMVQtdVhKRU1VTWljeTQ2Rm1qYVVWeERlaklHVklBU0pyNjRaUWZGYXVhOGJMZ0h5TmRpVERTTDVoZkJ3eW5OenNfcVhnUEhLLVBNY0VqSGdVRlZMS2FwWlgweUcwckJ3ZmYwc2dJb3lScWI2VFdKNmc3aGdpUGJFdTVVZFpIaW9qR3ZGSmN0?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **17.94** | **8.70** | **16.56** | **11.80** | **258,497,380,352.00 USD** | **-42.99** |
| DIS | 22.87 | 1.74 | 11.41 | 6.80 | 191,558,647,808.00 USD | 0.63 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 7.35 | 0.89 | 4.84 | -6.10 | 82,454,364,160.00 USD | -4.46 |

Peers fetched as_of: 2026-11-01; NFLX reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-01

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 12,874,176,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,663,927,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMisgFBVV95cUxQUHJTT2tVYjBfMGpTdlVzaE1DWlF4NHdNOFZpeENYcjB0OEw4QzlPSF84Q3hGYy1EQVFmZHp6V0l1N2J3SUNHNTdMb0RMS3FTMUFYV1EzWGZxTmtTM2lUYmVHLWp6Q3lMZU9sQ0FMVEJGaHNGOTVSb2pnWDlQRnJvSXBMSl93SWxmWVlENklwbmlHcEcxdWpnNGx1VkJNdkxVSlE4bm9yd0dxYlVTVmNUSWpR?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQY25aRjVOYlpTOUFjenBCbW8wQ1BEMU55SFZ2dlkwaUVydjBWOFdDREFzelhBeTBpanN3ZUgzUTdLWFRtamNYZDQxOGFacFlkeTZ1ak5KX2FWMGc4NXBEeGZIYkxKTVNBOC0xU0JFR09FT0NiV2xMc2xQVGFHQmFpdzBKSTJXdkl4Yk9PQzlCVVZXaWtFUHJRUw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNMEJjQl9vSl9kWk5nemlNQW5QangydndZUU9JRW52bjhwZ1ozX0Fnd0xhc21iUjBfNXNUV0VibVVUaHpmeFpWLVBEcHlpMXFkbXFZSzBBUzd1OV93a091XzVxdjQ0bDNyV0dYTFVaMmJuektoVmM3Z21XQW9aZUVxRVpPemFIaU5NdGZDX2tJY2pUYnRHRmY0?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPZ1pZb216M0NKaGhqWmdoXzkwOC1TQjFzRExLVEpXYVpSU19HTWN5QUVKbTg3cGNYem9nQmw5Mmsxd0V1M2IyMmJQWDJrdUszTllwRmFsRG5UNTZpTjRrVWRCYzBsdGlGazhkeGFwNW5ENUhXRzFEOUJ1U0J4aHJtaDhYdW5hNWdPM1FCajlZZk1pUQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPZTg4c2VtT2d1SV9meTFhZFpzN2ItRk85YXlQWnAwQUxDRm5VMmhBU0RrVXAyRWROcWk4RUpFdk4yWlhkc3dlUjFyU3hkVDVkaklFNC0zTmRPRmJZNHQxN2xvYmQtMVlDVm9Bd2VJdkZIOEI1Mnh0blZMNEJ4d0FGOXBvY25ic1UwV2NYa2ZPcw?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOY3JYbDhETktQMDhGRklxQl8wM3d0YkFPdGpia3dkaFlXdUxlczVzVlFBTlVVTkRUSWw4MF9PbHZyazd5bE9EejVzR2ZBVmowNTZ2dWZuMDZ5aGhZQ3IxS3VkMmg0TFBDSFAyQ0R3OGxIMklaLV9xUEdLZGY4Q0VxTWFsal80OUZuQjRXSUZ0QUNxR2x1aTgwcVhGUnlKY1RoblJkZGZuNjlIVHZtWkpsd3ZzYWFiSUZ1RlE?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNUkI4X0RpN3VILXY2MExJTlctZGZ5dWk5MDhqRTZDc2JJdzdiclBEcVNLNFI4YktGVWRzbGx0aUQyeGMxamNwNU8tOEF6aFJZR1l3SUtiZ0JqMDAxSEdqTFFhaGFGdmVGNm5YWkN2QVNub0ZXa3RFVEJ4bldTSnRTMFROSVdFZEZWaUpFdGw5SEl5MEktWWJYbnpiX1VfNXE5QVEtUw?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNaUJrZk9aRDR5YV9IeFVvQ2cwMzlQLXJmRkxiZkVVOXVfbXhJa0p1aXE1VUJ2aE94TEFYbGlTQTBhbDJlSkpyWW84c3RmTFlrS2RtV0VGa0haTHBjbTZHUnNJbENnSUgxc1k1ZXlubElZMTd1Yld2VFpYQUZ1N2NrTnpma29rNEtyQ2FvMA?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQUjViaXJMRjdUcktWc0Y0bWRGX2ViaHA4UXhJcTREbks0LUZjcGNYSzNqZl9CTHZEd3kwLUFhZFNhcDNwaVYtVnJ3cUltT1p4NkZNcTdrSE1oZVpZQzVLZHpySjdCYTV4QXVJdXhFcW9LWU1MUC0zcDl2RVp2QUwxb3liRDVWRVd4WHFFZWZwLV9RVzlx?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxOeFN4ZjN0Q0RPX3AxYTVZemJxVHhNemRHWDBhdWhRSXdzRklENkdic24yUloyQjNONFhobWgxb0F6R1N5ZGp3RW52SWRHWjE2RW5tRE5qOTBCYlVXZ3VoY2pQQ1lpaFp0V1c0bXpXcXlicEhVdjBWeGNBaTkweDBWWG1Tb1k1WDBXU29kLWtn?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxONkdVeC1kd29pUUlKbjZfd3lYckhoSFNnbktmU1VIbVFBR08yV3pYcWo3TDkzbE43SnBJQ2RlTE84OUhnTnRnYWNsTVo4N2hBMlVKdVotVWdDVV9IdGhxbWJKLUd3Yk1fZDBKTzc0Uk1SUzc1RUdBLXpqVkdfWkV4ay1FOXpwTTNvMGZGUmxiUEJUdlVnZW1pZ2RXWW1GNC1JaVczaWczU01NRWJ6UTV2Rm9VNUZMZw?oc=5
- https://news.google.com/rss/articles/CBMizAJBVV95cUxPOXRvVWhSa2Fxam1fVHRJYWdjWUlydjZlOUlvekxuVUhTSm1obXIyYlBzSUpqdXByUkUxZnRERW5FU2xJWmk1Qk03c3N5azA5UE5ta2VVZUU0UmlqaUVBSDZ5cERZZEhFT1RzX1hXODA3UEl4dXBNRlpnb19ZZ19TNVFhVzB1UlJ2NU5yNDZVcThhRkNmRjEzWnZ6UnRFNkd0ZFZzM09DZHdtajEzRVZKei02MnIwcXNvM1Q3VkpiaWFDMUgtbzRzSk90Q1B5TUFybEpjUUxfVDVqX19vMDdmXzZ0bkFka3Jlek5XUVZwakU5RHNLMXIyaTlqaWdxYWtNN1ZLZWs1V20xUXVxMy1VR1M1d2FjNkZGVE51ZkFYbjllUHN3MkhVOU1IOUgzekN4TFptcnRRMXk2c1Q1TEE1OEpWTW1qbS1kQnM5cg?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPRnlVQVVLX05hNGdyek9rTjNybEw5b2lJcEFnN3BlMElCNEpDZmpRcnJfSDNWbHRxS2NXS3NyQ1FkbDZLZzAzdjl0RklFMk55aTZ4REF2SDlnVWpGZmk4T2NHTGNoSVVUZWM3WTVWMkl0UEFDSFJiRllqX3RRLXBXZkpIY21HTzhWZ0ZIemdvVnoxT0VqZC1UamZPTENnWDloNmZ6VDBZVWN0QQ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNT1JCQVk2LWJnZUtua1ptNXZzNFgyYzBVSUNEMUxSZjRweHdvZklPNlNyeHZYaVRYWklrRzl0QXhLeVBIX25NdjJocUYwZUllcDlycjhsZDFUcENHeENCejlXZlJFM1htMU53VHUxUWthdlpGZW5xd0hMMGtyREdTY3Q0U2ZjQXVnTjFpaUc1SDY?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOZ2xkUHpTZ1FLVE9NNFlqQU4yRVg4d2xMcWk0ZDNGNUwzLWtKVldUbF9SVXNLSFJMZkRNUnhLYTZ6NWc3ZEc2dDNVcjNTTDk3c0pZblc2OVdtZkY1ZFhhZWc5MGE0NkRUSmpicTNXcDJTdDdJVFBmRXZFck1hUGRUYUtjSUU5eWZiOTNibXhHRzIwcGVaX3RESGtScw?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOTHdVQzdqQ2pIcV9WT2tPUDdyTkQ1VzR5UXNPdk5xLXVIT3ducXc5ZTRiLWJWRjR5NWRkOTlOd3BUNUFJeE9lWTh5Z0RCdUtkcG93cVcwRmZiVV9ETHFFdkw2NGg4TDZjdWwySlYwdGp5NVZDalQzUG5HV1o1R24yRUhqZU1vdlNiUnJQMWh2UjE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQYXFIRXR2UFNyNHdHZFVwM0FwMVQtdVhKRU1VTWljeTQ2Rm1qYVVWeERlaklHVklBU0pyNjRaUWZGYXVhOGJMZ0h5TmRpVERTTDVoZkJ3eW5OenNfcVhnUEhLLVBNY0VqSGdVRlZMS2FwWlgweUcwckJ3ZmYwc2dJb3lScWI2VFdKNmc3aGdpUGJFdTVVZFpIaW9qR3ZGSmN0?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
