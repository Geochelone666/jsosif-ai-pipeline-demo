# CAT Intelligence Report

- ticker: **CAT**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/CAT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CAT/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T06:04:23.046170+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 19, 'rule': 1, 'ai': 10, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261119T054856Z-9eb86811/CAT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 19 unique headlines; 12 named publishers; 0 exact duplicates; 19 HTTPS source links; largest publisher share 21.05%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 537.3700 |
| Return 1D (%) | -3.8298 |
| Return 1W (%) | -11.2196 |
| Return 1M (%) | -25.7846 |
| Return YTD (%) | -5.3992 |
| Return 1Y (%) | -2.0196 |
| Annualized volatility (%) | 41.8707 |
| Beta vs SPY | 1.8475 |
| Max drawdown (%) | -49.3241 |
| Sharpe (rf=0) | 0.1600 |
| Downside deviation (rf=0, %) | 29.8637 |
| Sortino (rf=0) | 0.2243 |
| Historical VaR 95% (1D, %) | 4.3476 |
| Historical ES 95% (1D, %) | 5.8406 |
| Correlation vs SPY | 0.6133 |
| Tracking error vs SPY (%) | 35.1075 |
| P/E (trailing) | 21.93 |
| P/B | 11.45 |
| EV/EBITDA | 16.75 |
| Revenue growth (%) | 17.30 |
| Forward P/E (estimate) | 16.70 |
| Gross margin (%) | 29.54 |
| Operating margin (%) | 18.76 |
| Return on equity (%) | 56.14 |
| Free cash flow yield (%) | 1.62 |
| MA50 | 719.2159 |
| Close vs MA50 (%) | -25.2839 |
| MA200 | 801.9237 |
| Close vs MA200 (%) | -32.9899 |
| RSI (14, Wilder) | 27.1522 |
| MACD (12,26) | -47.5732 |
| MACD signal (9) | -47.5030 |
| MACD histogram | -0.0702 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CAT': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 537.3700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.8298 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -11.2196 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -25.7846 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.3992 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -2.0196 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.8707 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.8637 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2243 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.3476 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.8406 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6133 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.1075 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8475 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -49.3241 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1600 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.7002 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 29.5420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 18.7610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 56.1350 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.6158 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.9335 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 27.1522 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0702 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -25.2839 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -32.9899 -> Clearly below the moving-average trend level.

## TAILWINDS

### Caterpillar Stock Offers a Backdoor Route to a Potential AI Recovery
- Summary: Speculation that Caterpillar could benefit from AI trends, suggesting future upside.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQbndQdmY0Rld2RzhjdFZEM3dac3l0NHN4OXlWTlRxRzZsT3hZM0VWb2JNMWFpRVk3MmtBS2pMdnZXM1hfS2NSYUw5YjVOcUY1TEV6NTVGVVZJYTN5ZVQxaGdxX0pkRlRrd1A0MWp2cGF0Qi1DaDFSMXhtWE5rNGFJbHlRb05kSFpLUDFWYVdQWHhEV3JYcDVfcHhzR3BBX0IyV2ZwZmFCYUFuR1lNdk9Tbnh3?oc=5>

### Caterpillar (CAT) Stock Price Prediction: Bears have the tape, but analyst targets still span a wide range
- Summary: Analyst targets vary widely, reflecting market uncertainty.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxORlhMOXFpWk5hSUNEME9JNE52Y1BONEdMdFVzZ1dtWVR3TkFuSGhDa0NjSGxQalVWWlZVSk1uLVk1TFNhZy1GcTJHSl9VSHVGSUpoeG0xZi1ELUVzR3d6ZURwd2pIZ21SQW9HdFlualc5aHZTUnRzSmlzNFpoSy1pNmhwb2pxODlSR3BrWnMyek9VTUNM?oc=5>

### Caterpillar (CAT) Isn’t Just a Bulldozer Stock Anymore, and Ken Fisher Knows Why
- Summary: Ken Fisher explains why Caterpillar’s stock is more than a bulldozer, highlighting diversification and growth prospects.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOaVVvWTg4QlFEZzRGb2gxYjJITE5keFgtblZlWVB5ZGVIUm56Y1FoTTMtVTFwU2Juekl0ODVqZE5xMlk4U2d2bXhpemZfQ1hkcGFvb2lTQ0R4QnlvaEhDNUs5Z05fUWZoMmdqYXhpbFNsMENySDNyREZjdmdpc19vYXFYbnM1ci1OSkxwczVxeFVadFVldFE?oc=5>

### Caterpillar (CAT) Stock Price Prediction: Bulls lean on upgrades, but price action says the market is still proving it
- Summary: Analysts upgrade Caterpillar, boosting bullish sentiment, yet market remains cautious, reflecting uncertainty in short-term performance.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOVXdNRkl0eTd5RkE4STVDVVR5SnJoWDQxa09tQWhVckQtRTN2TDNNZW5iSlBRd2xkRno0SnZFWUtRRFZjMWV1UENEMTYwdUkya3NKZzFNNTFiRFdjUnctX3hKa2ZpSXpvdjB5TEZLX3BaOHJSMnkybzROM3V1T0hqNDlMT2xtVm9IWnN2N1FONWRtX0NwWmg1X1ptMGNoaEE?oc=5>

## HEADWINDS

### Michael Burry Cashed In Caterpillar Puts After a Nearly 4x Gain Even as CAT Stock Fell 10% in Its Worst Week in 18 Months. Is Caterpillar Still Overvalued, or Did Burry Just Lock In the Easy Money?
- Summary: Burry’s exit signals potential overvaluation concerns, adding downside pressure.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi1wJBVV95cUxQRzlMOWd6Y3BEaDZVeDkyWG9Jd2xuMlltLVFyRnJ1cVhsR2RDcjdSZ0FtRXNnZDloOEF3TlUyTWZpQVk0Q2xaXzBBUEhHN2l1VmVEZk1Ob0FPOE11MFMwc0E0LXpuR3VLYzY2dVBpcDhnRW1iMHlLUkJ2elQxQkc1YmNQTlgtMVJ0RTZnTWZGUkIxd0x2LXhfbklHVnJEZm1taE9vVlJ3SEk4Q3lPRGlZYlRiTzI4bm5KNUxoQ3NGQ0tubmRsRUE4RjF4UGNUQzQ2bk5IdU1qTTZRY1B5UkN3X21qT2k5OHJhc0pyUU1ndUsyXzlOTDJ5QVhpWDRUVWdQZVFLRlBja2lCelV6Tl85aVlPajROUFAtSWpfM1l6N09ncVVIcnhKX1dZMF9oZFh0MDZIQXN0T3VlelNCUmV4ODcyTHdzZUM4el9hdjg4X3JodExGVVdn?oc=5>

### Caterpillar Inc Stock (CAT) Moved Down by 3.78% on Nov 19: Key Drivers Unveiled
- Summary: Stock fell 3.78% on Nov 19, indicating short‑term market pressure.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPc2xYTFJOZTF3OEgwMnE4aDRua0FBRjN6R2JKTC1YMk1VMUp4R013WjBMX0dNdXNqN3o2NkpYekliMkpwbm42S3hQNlBaY0oxZGxaLVRHZjFPRlN4N2lBVlpoeWlkSFZ4cEgyTHVxZVMtTFE4aG9CNDRwbkNJQjZ5MnAxeUl0b19YNnc?oc=5>

## CATALYSTS

### Caterpillar (CAT) Stock Fair Value Falls As Analysts Cut Targets And Lift Rates
- Summary: Caterpillar (CAT) Stock Fair Value Falls As Analysts Cut Targets And Lift Rates
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQQmd5a2U2TE5CNTVaZmVfTTZ0Y1ZmU3R2WlRMQm44dWJFU2FJN3RMRkZBeTkxS2hqNnBrLUwydHpPdUdoNzFMMDNQY3pZYUlJTmRZd1VlT3piSkluSjVkMXp2a1dXbnVXd29fbzUwaHRDYVdEbDlFV3E1SWIzT3RoM3NpLTNCbG1sMEpZVm9Pa3NiT29PTldXbUNNLW1tZw?oc=5>

### Caterpillar’s 34% Slump Over 6 Months: Wall Street Desk Says It Sets Up 90% Gains Within a Year
- Summary: Duplicate of previous forecast, reinforcing potential upside.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOR3RwVnFOZ0M3eWlCbjUybklZQ3BqRDBxVmY0ZE5lb1RKYWY5dW40M0UtV0lMNkM3c1V6VkI3VXhMU1U0TXFRTzZMdWdjek95ZFlGRG1TNVotVDlZRjE5MGV6aVRfQWNrQXFRTHE4T3VUMlRvTi1WQTRQSmRYNDV4V2toRUhzakYxVVJBNFF5QjlGVEtqWDlZ?oc=5>

### “Trades Basically Like an AI Stock”: Caterpillar Just Dropped 22% in a Month. Sell, or Load Up?
- Summary: Caterpillar shares fell 22% in a month, prompting debate over selling or buying.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNTmViZ29WQlB0OWE0SGtrNlhJdTZNU3pNeWxGUXc3SVVXSHJ0VGk2QVM5MHgxdjZPRlh0ZEIzVkhSMFhMbmduSFVzTVB2UTdmQmZEcmI1VThockZRMmszZjBvQ2N6bnVnR3R2RmhURjhHQ3paWXE4RWlNZkdkZnMwMXBCX2N5RndBM1RNUkVYSllubzJreGxlTmRObGh5NlVWVTVzVGFZYWVpeWpPSm5TUEVRRTRtdw?oc=5>

### Morgan Stanley sees Caterpillar rental gains, stays cautious
- Summary: Morgan Stanley forecasts rental revenue growth for Caterpillar but remains cautious about market conditions.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQNlliRkI0Y1l2QlJBWlF3TGFsU0VxS1NRWFhvcHNLT2NYUDdJcW1IYl9CWGxWQ2NOWTVFZWlKaFRtZHF0UlJQME1FcmFGTnJlZnAxWm9xY1NvM0ZWOWpuREZUZXB0TlFMMkl6N2lJVXctck5UaW44Ny1MNEozc3QtWF93SDRmdy1TVEM3OXFEYXEwX3NpM0VFb3JUSkFZdDE2YVBIcQ?oc=5>

### Caterpillar Makes Advanced Safety Technologies Standard on Construction Equipment
- Summary: Company standardizes advanced safety tech, potentially boosting product appeal.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNWVFoNXBMWU1WYk9NU1pTSTJKeXFMY2IyZ3RLSVF3eEJQNEdvcFZqNFp0ZDdGZWp4V1ZaVnJ0UjlPSk1oekJXY1Bad0k4dkhXU0xmV2lSTEFFNUFlVzlxMHZmUjJEMTJ5YnBCZWFDdFZBdjZJRGFQb2loZlA4RHhzMUpiZG8wT0ZULXBCcHVWMm5hUDJINGdURm5kWkh2ZDZ1RWZJWHBNcG5RcTlfMnZNcmtR?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CAT** | **21.93** | **11.45** | **16.75** | **17.30** | **245,897,379,840.00 USD** | **-2.02** |
| DE | 34.74 | 6.02 | 26.30 | 4.90 | 168,486,223,872.00 USD | 33.12 |
| CNH | 52.71 | 1.76 | 35.05 | -1.00 | 17,776,719,872.00 USD | 19.33 |
| CMI | 17.57 | 4.33 | 11.70 | 13.50 | 57,703,030,784.00 USD | -9.70 |

Peers fetched as_of: 2026-11-19; CAT reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 20,682,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 1,141,000,000.00 USD; period 2011-07-01/2011-09-30; fiscal year/reporting period 2011/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/18230/000001823026000057/cat-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMisgFBVV95cUxQbndQdmY0Rld2RzhjdFZEM3dac3l0NHN4OXlWTlRxRzZsT3hZM0VWb2JNMWFpRVk3MmtBS2pMdnZXM1hfS2NSYUw5YjVOcUY1TEV6NTVGVVZJYTN5ZVQxaGdxX0pkRlRrd1A0MWp2cGF0Qi1DaDFSMXhtWE5rNGFJbHlRb05kSFpLUDFWYVdQWHhEV3JYcDVfcHhzR3BBX0IyV2ZwZmFCYUFuR1lNdk9Tbnh3?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxORlhMOXFpWk5hSUNEME9JNE52Y1BONEdMdFVzZ1dtWVR3TkFuSGhDa0NjSGxQalVWWlZVSk1uLVk1TFNhZy1GcTJHSl9VSHVGSUpoeG0xZi1ELUVzR3d6ZURwd2pIZ21SQW9HdFlualc5aHZTUnRzSmlzNFpoSy1pNmhwb2pxODlSR3BrWnMyek9VTUNM?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOaVVvWTg4QlFEZzRGb2gxYjJITE5keFgtblZlWVB5ZGVIUm56Y1FoTTMtVTFwU2Juekl0ODVqZE5xMlk4U2d2bXhpemZfQ1hkcGFvb2lTQ0R4QnlvaEhDNUs5Z05fUWZoMmdqYXhpbFNsMENySDNyREZjdmdpc19vYXFYbnM1ci1OSkxwczVxeFVadFVldFE?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOVXdNRkl0eTd5RkE4STVDVVR5SnJoWDQxa09tQWhVckQtRTN2TDNNZW5iSlBRd2xkRno0SnZFWUtRRFZjMWV1UENEMTYwdUkya3NKZzFNNTFiRFdjUnctX3hKa2ZpSXpvdjB5TEZLX3BaOHJSMnkybzROM3V1T0hqNDlMT2xtVm9IWnN2N1FONWRtX0NwWmg1X1ptMGNoaEE?oc=5
- https://news.google.com/rss/articles/CBMi1wJBVV95cUxQRzlMOWd6Y3BEaDZVeDkyWG9Jd2xuMlltLVFyRnJ1cVhsR2RDcjdSZ0FtRXNnZDloOEF3TlUyTWZpQVk0Q2xaXzBBUEhHN2l1VmVEZk1Ob0FPOE11MFMwc0E0LXpuR3VLYzY2dVBpcDhnRW1iMHlLUkJ2elQxQkc1YmNQTlgtMVJ0RTZnTWZGUkIxd0x2LXhfbklHVnJEZm1taE9vVlJ3SEk4Q3lPRGlZYlRiTzI4bm5KNUxoQ3NGQ0tubmRsRUE4RjF4UGNUQzQ2bk5IdU1qTTZRY1B5UkN3X21qT2k5OHJhc0pyUU1ndUsyXzlOTDJ5QVhpWDRUVWdQZVFLRlBja2lCelV6Tl85aVlPajROUFAtSWpfM1l6N09ncVVIcnhKX1dZMF9oZFh0MDZIQXN0T3VlelNCUmV4ODcyTHdzZUM4el9hdjg4X3JodExGVVdn?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPc2xYTFJOZTF3OEgwMnE4aDRua0FBRjN6R2JKTC1YMk1VMUp4R013WjBMX0dNdXNqN3o2NkpYekliMkpwbm42S3hQNlBaY0oxZGxaLVRHZjFPRlN4N2lBVlpoeWlkSFZ4cEgyTHVxZVMtTFE4aG9CNDRwbkNJQjZ5MnAxeUl0b19YNnc?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQQmd5a2U2TE5CNTVaZmVfTTZ0Y1ZmU3R2WlRMQm44dWJFU2FJN3RMRkZBeTkxS2hqNnBrLUwydHpPdUdoNzFMMDNQY3pZYUlJTmRZd1VlT3piSkluSjVkMXp2a1dXbnVXd29fbzUwaHRDYVdEbDlFV3E1SWIzT3RoM3NpLTNCbG1sMEpZVm9Pa3NiT29PTldXbUNNLW1tZw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOR3RwVnFOZ0M3eWlCbjUybklZQ3BqRDBxVmY0ZE5lb1RKYWY5dW40M0UtV0lMNkM3c1V6VkI3VXhMU1U0TXFRTzZMdWdjek95ZFlGRG1TNVotVDlZRjE5MGV6aVRfQWNrQXFRTHE4T3VUMlRvTi1WQTRQSmRYNDV4V2toRUhzakYxVVJBNFF5QjlGVEtqWDlZ?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxNTmViZ29WQlB0OWE0SGtrNlhJdTZNU3pNeWxGUXc3SVVXSHJ0VGk2QVM5MHgxdjZPRlh0ZEIzVkhSMFhMbmduSFVzTVB2UTdmQmZEcmI1VThockZRMmszZjBvQ2N6bnVnR3R2RmhURjhHQ3paWXE4RWlNZkdkZnMwMXBCX2N5RndBM1RNUkVYSllubzJreGxlTmRObGh5NlVWVTVzVGFZYWVpeWpPSm5TUEVRRTRtdw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQNlliRkI0Y1l2QlJBWlF3TGFsU0VxS1NRWFhvcHNLT2NYUDdJcW1IYl9CWGxWQ2NOWTVFZWlKaFRtZHF0UlJQME1FcmFGTnJlZnAxWm9xY1NvM0ZWOWpuREZUZXB0TlFMMkl6N2lJVXctck5UaW44Ny1MNEozc3QtWF93SDRmdy1TVEM3OXFEYXEwX3NpM0VFb3JUSkFZdDE2YVBIcQ?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNWVFoNXBMWU1WYk9NU1pTSTJKeXFMY2IyZ3RLSVF3eEJQNEdvcFZqNFp0ZDdGZWp4V1ZaVnJ0UjlPSk1oekJXY1Bad0k4dkhXU0xmV2lSTEFFNUFlVzlxMHZmUjJEMTJ5YnBCZWFDdFZBdjZJRGFQb2loZlA4RHhzMUpiZG8wT0ZULXBCcHVWMm5hUDJINGdURm5kWkh2ZDZ1RWZJWHBNcG5RcTlfMnZNcmtR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
