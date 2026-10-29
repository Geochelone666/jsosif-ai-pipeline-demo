# GIS Intelligence Report

- ticker: **GIS**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/GIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GIS/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:16:35.567059+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 17, 'rule': 6, 'ai': 9, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/GIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'low_uncalibrated_model_confidence': 2, 'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 17 unique headlines; 8 named publishers; 1 exact duplicates; 17 HTTPS source links; largest publisher share 29.41%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 33.0500 |
| Return 1D (%) | -1.2549 |
| Return 1W (%) | 1.4737 |
| Return 1M (%) | 0.2329 |
| Return YTD (%) | -24.0211 |
| Return 1Y (%) | -26.4720 |
| Annualized volatility (%) | 30.1727 |
| Beta vs SPY | -0.3859 |
| Max drawdown (%) | -33.2524 |
| Sharpe (rf=0) | -0.8729 |
| Downside deviation (rf=0, %) | 21.4973 |
| Sortino (rf=0) | -1.2251 |
| Historical VaR 95% (1D, %) | 3.0349 |
| Historical ES 95% (1D, %) | 3.8909 |
| Correlation vs SPY | -0.1624 |
| Tracking error vs SPY (%) | 34.5871 |
| P/E (trailing) | N/A |
| P/B | 2.37 |
| EV/EBITDA | 9.04 |
| Revenue growth (%) | -2.80 |
| Forward P/E (estimate) | 10.48 |
| Gross margin (%) | 33.73 |
| Operating margin (%) | 15.24 |
| Return on equity (%) | -10.49 |
| Free cash flow yield (%) | 7.37 |
| MA50 | 35.1261 |
| Close vs MA50 (%) | -5.9105 |
| MA200 | 36.3529 |
| Close vs MA200 (%) | -9.0855 |
| RSI (14, Wilder) | 47.4024 |
| MACD (12,26) | -0.1832 |
| MACD signal (9) | -0.4707 |
| MACD histogram | 0.2875 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GIS': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 33.0500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.2549 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.4737 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.2329 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -24.0211 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -26.4720 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.1727 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.4973 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.2251 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0349 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8909 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1624 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.5871 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3859 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -33.2524 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.8729 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.4845 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 33.7280 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.2430 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -10.4950 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.3713 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 47.4024 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2875 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.9105 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -9.0855 -> Clearly below the moving-average trend level.

## TAILWINDS

### General Mills: The 7% Yield Is A Trap, Not A Gift (NYSE:GIS)
- Summary: Dividend yield claim criticized as misleading.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPRk1hRVFaY3FDTlRoYnRjVXc2RmxTUmQ3ZklyejFJX3BsMjYxalhPZnN4bExhYUIyTDRJc2Z0cXZURnd4SnhOaTlfNE5VWF9xMHItd3pfSTJ1UE9vcjNnRXNIZlhwQVFTOF9JS0lxeWsydXB3ZE1tU2hpeF9uTlJWR2NpcDc1aWt6cmFHLWU5LTRJR3M5ejVVY0JCQQ?oc=5>

## HEADWINDS

### General Mills (GIS) Stock Seems About Right On Its 38% Slide
- Summary: General Mills (GIS) Stock Seems About Right On Its 38% Slide
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOSHV0OTVXbmVEVk56cFpiTFMxQkQ5cktwREVEbC04c2hwdGRRNi1qMTJlZzdpaFVDZzJyMnZjMHFuWkZLYzdXVVY0OF9MdkZ0S0dyc1I2NVRBQ2FFSFo3dHFYcnRwNEw0R1EtM3lXVzkyQ0VsRi02MlJKQnVvdWlmdzJOT19XajgtRjVfbUw3SzRHaTNKdWNRSEtR?oc=5>

### General Mills (NYSE:GIS) Shares Down 2.3% - What's Next?
- Summary: General Mills (NYSE:GIS) Shares Down 2.3% - What's Next?
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPYm9PY0NHVnlSQ2Y2TFg2dnIxVjV5VGxoNkhoY0ZibTV5ZFg4bzVrWkplaXZMdy14cUYwdEhBVWk4WTJoVGh6ODNNUTU1WDBtSTJxM1lfUWo4Tmt3U3M3dGZ2VFotVnBSeXFnaHowbEd0RWZmb040YnBPYlc4Uy03azM4QzhrM0JsN1VrYVJDdlRUNHJ3ajZ6SHJBVGRsdGJPUDByY1NBLTMtMThE?oc=5>

### General Mills (NYSE:GIS) Stock Falls 2.6% - Here's What Happened
- Summary: General Mills (NYSE:GIS) Stock Falls 2.6% - Here's What Happened
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxOQkFZdjFhZXl2bTYzMXRCZ2p6dlI2ajQ4U0NKS0d4U05JT3R0OURaSU52ZzIydDJhWTRfNl84RDNmTjhYRTEtQkdnWlk1TDdRNEVyY1lCRWtQYjVreFl6ekJiOThSTVI2c2k3VnFlMnhqbVk2Q3JJR1BFMVdGTHZnSXd4OVVtcW9sSE9TZ0ZLXzFOXzRDUEVaTG1BYXhuQlU4aHRLWTdobGVrSHctS0JqZEtzcEplZ2Nt?oc=5>

## CATALYSTS

### General Mills Yields Nearly 7%. Is Its Dividend Safer Than Kraft Heinz or Smucker?
- Summary: General Mills Yields Nearly 7%. Is Its Dividend Safer Than Kraft Heinz or Smucker?
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOLUVNeWVMdXFwU1BoOU5ENnc3SnRPZXZPSXVzQmFsVU9VSi1acTVqYVRxaTgwQjlQMVlQUkFTTkh0ZTlJaFhYMUJVcHAwUzVWYjlfTE5uN1Q5WTBqQWE5NXhTTW1URmxHTklCdXMxMzM0NDJHdG1yTWQ0R1lEM2V4U2ZGX1pWQzlDdGgtMWdBejEzNXNSQWdlaTNUX1d2Tzl1VHRDUDJnLXVkckxjWFZzdy1VNkNhVUZPcG4yVDJoQ3E?oc=5>

### General Mills (GIS) Faces A Valuation Test After EPIC Sticks Launch
- Summary: General Mills (GIS) Faces A Valuation Test After EPIC Sticks Launch
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxNNHZ4dFNFNmd1UXZQWkxfcDE3VVJQZGZWMWNoRkZlazByd2VfM0x2Vnh1c3hzdGd2TEVNM19OcU5hbkF4WmpmVV9PbzRjcmVKQ0pyczlvQmFfRnlJSHk0dXhlR1ZDcXV5WVFFWGxGMmxhOURjLW9YWXd3d3ViUk95OFd1RENFdlpkVWNNZEpPUzJRNjhrWHdMTnFWUGpYLS1DYkl3NjFPUW5YWnI3OTZ3WkJvdTFTYjhocGRGOTBIMjlrV3hYT3ZnMjZPMXZOdk90elZBd1hicXNmUdIB3wFBVV95cUxObVFIenladzhzdUNFc3Q2Xzg0R1NwZUhtT01COVBLdnBROExOd0xwNjBLaVl6OGliS19nN0wzaFVfMnBFM2Q0YjZ2bHMwZjg0RHRNcWQzaHJfWk10aWE0YVNvaC10TnoxbkR3TlplRTYxNGx3SUMwTkpIakhVVFQzLW42TVc3RU9OamlxQmNaYkxwX3FxU00zeU1hd3gyVVdxMXZsaUJzVlJna0otLWVLVmpMTTBsdTlldmJRX2xpeHQzRzdDZS1oS1lGalRKQS1tQ2pDWEI4a3RtR2VxYTNj?oc=5>

### General Mills, Inc. (GIS) - What Are Analysts Saying About This Stock?
- Summary: General Mills, Inc. (GIS) - What Are Analysts Saying About This Stock?
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxPMFVPLXFVcGJ4b3BQb0Z5THJ4Z3hFcllvWjRIY3V6NE4zM2ZGR1dUbXpveTFmdk5JckNwOTVTZEw0b1NGUWM1aHRZRktmLUcxblhoeEhTTHlzUHdGY2NxMzBkajEwOHJKVS0zSjFPZWRUZDMyU2N5UE5aNVJmOWF0aXNpT1cyREJBOGZkY0V1aWRVTDFld3RQY2RsWTJUMlFnSVJnWFViQ3M0eGdxalBkdXpwY1hack9NS0ozNjJRZDZtNVlZOUE?oc=5>

### Despite Structural Challenges, General Mills' Valuation And 7.1% Yield Stand Out (Upgrade)
- Summary: Analyst upgrade highlights strong valuation and yield.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNdW1xa3dCaEVrVzBscUpYZWRPR3U4QmFmZWtqT3M4ODVLdU43Q3lFWS1NcC0xdWF4ZnE5OU9SbFIway1wd0R0MmNtQ0NURnlraE1sQWRQbUFaVDRtbkhvbFI0OWRxQVRoYUZ3Uk9URnRwMzlQdm10dTVkTHdGSWpEZ0l0Rk9aTy1uTWFVYUVkYWxSTVNNeHEyMkR5T3A4djdCRElGSkFScVNMZWdmbDdMSWZibzZLallzUHRmcmdpY2ZXTVNFUTNN?oc=5>

### General Mills (GIS) Launches EPIC Sticks, Is The Stock Still Cheap?
- Summary: Announces EPIC Sticks launch and questions stock valuation.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQdWVHS2FZd2dTM1U4UkdzdGFmM1AwWVFpNDJwZFA2WmUwN1U4X1d0aTkxN2ZEYU9CMndUY1VpajZVbU5wNjUxM0hkcHdqT1QwSElQLWZfdDUwZTY2aVhmcnc2eEwybWlvaldSMFRLbkpWZkhvSm14VzhTbmk1TVlQX3Z4S3hLMDk4Q05WeTNzZW1zY0tGRFNjUWI5cGQ?oc=5>

### Why General Mills (GIS) Stock Is Up Today
- Summary: Explains factors driving today's rise in GIS stock price.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE9LT3o4SFlxbzZjNzRrRlloQ0Y1SGxpR0dJTTVvdVhMSnV1QmpHRGNwcHVKOVM1Q2gxcGw4T0tYQ0twcWMxcHozeFBUYzE4V3E2eTFQdTlrNmdnWWN0UGFHVFNmc0pSWmRPbG1zZzdNcFZoTXMxMFZNSU5hV3J1eG8?oc=5>

### General Mills (GIS) Stock Looks Reasonably Priced For Now
- Summary: Analyst suggests current price is fair, no immediate upside.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxOaVExbjV1YWNRalAyS2NtY2NTV3NPTzVCUGYwUmFsNWMwRUFMUUxLRkxBRzNQdXk4eFpaWjZPUk1xbzlxWTJ6THhlWlJULTk0Z2VmcHpqcjR0Q3ZJczFYbXZRTXU0UzVPWG9HMm5kUE5VNDc4Q0tFRjNrajV2Y1F4bVJRWHdQc1RUb1A0SU9PcHVsSnFxVDQzUFU2Tl9wRWJPSUFRRkF2MzNkRHZNd251a2JicjN0THQxRTd5VjFKQ24tenpwdDc4Z2dOenpfRVhoNFY40gHYAUFVX3lxTE44clVSWVp3eVlJYlNJcGlwR0I0ZWlqVFV2dGVVUThPb1ltV3JUNGFwaDNqNzRzVldPMHZQYkEzSGl4MDJtQUwybmNyT0p5SWZSUjFpaDkweGFuUUl3MldHTXI1ZVBMa0Y3QWI1bDlid2EtOENuOXl5WUhTdlhHaTBwdUtuLVBkZ0s0b0ZnVU1iWlpNVFVJSEM5TkQtUXBmZ1g3MmhJeElEa3VKU1pyN0V4WWh1SU1iTXJfODRTbV8yeFRUZ3dncVBRUDlyLXhzeWxteENZRThOVQ?oc=5>

### Kraft Heinz vs. General Mills: Which Dividend Can Avoid Campbell’s Fate?
- Summary: Dividend comparison between Kraft Heinz and General Mills, highlighting potential dividend strategies.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOWnFWd3pHOWZWQjlpOV9wR3p3QXVEY1hOZjkzUVkyUnJITTZTMEcxb1FMcnVfQlU4Y192U25rY29RblgwZmdRNzU5dE8yMlFLay1RTFI3Zk0xVGowQWZ4bEUwODNVYXRSZDhycC0zZ3BBM0NnaWluSTdBRWlacHFJdU8tb1dUVHlCcXlraEMxU0ZQUkxJM3NJYw?oc=5>

### How EPIC Sticks Launch At General Mills (GIS) Has Changed Its Investment Story
- Summary: Launch of EPIC Sticks product line, influencing investment perception.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPanpYVHhXaXhLRHRUX3lEOEZkcVNFX3JmeW4tQklHOXpORjFqYmxXRHpDQTZnZUdkTFRLV3A3bFFUTkxnaGVLenRORFdkSXdNRlNzejlYa2JMcDZFVkJ1UXN6VEJVRm5ucG5XaWxkbDJ5dmd1UDBiR3gwWkNiX1BLWlZ6V1dJd0wzbzlGak5BSzFaUGdtV2Q4TUEyU3BvUQ?oc=5>

### General Mills (GIS) Up 1% Since Last Earnings Report: Can It Continue?
- Summary: Stock price movement post-earnings, questioning future performance.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQTWd6MzJHZzVDOWQwcHhGc1RnY2RlMW1Pa0JlRDBTMGdQa3BIemZyalU1WUxmWndKOGc5cC1Jckt2MGYtVlEyMWJ0WFdLVWNXVktOalg1elVqUERrVEZfOGtBZzZLaFd2WVVOVU0zdENmMlBnT3MtSjF2TjdJZDUxdW1fTzNZWDJhaWlRb1ZrbTV2b09N?oc=5>

### What Does the Latest General Mills (NYSE:GIS) Filing Reveal?
- Summary: Analysis of recent filing, details unclear.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQSTVVY3NtRHR0S3AtRmRhR3BiQ0gtdl81V1lWMmhZQV9BZmlvREZ0MFA2Z18tZ2ZFU2VJeVlkOGtFR1M3aU44bE9ldmRsQVZLbDdfOHd5Q0hqOU1pcXNndk8taDNBLVB3eF9WU251aGRibHZzeVRLUERqWDlxbk4tY1ZOX0xGSWZHUjM1dWxUZmg1ZFdSZFVSTlFzQS1QWWNwS0E?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GIS** | **N/A** | **2.37** | **9.04** | **-2.80** | **17,671,409,664.00 USD** | **-26.47** |
| KHC | N/A | 0.79 | 8.14 | -1.40 | 28,293,754,880.00 USD | -0.10 |
| CPB | 15.84 | 1.59 | 8.34 | -7.90 | 6,140,652,032.00 USD | -29.20 |
| SJM | 58.63 | 2.33 | 8.97 | 5.00 | 13,402,036,224.00 USD | 24.60 |

Peers fetched as_of: 2026-10-28; GIS reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-23
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

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
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOSHV0OTVXbmVEVk56cFpiTFMxQkQ5cktwREVEbC04c2hwdGRRNi1qMTJlZzdpaFVDZzJyMnZjMHFuWkZLYzdXVVY0OF9MdkZ0S0dyc1I2NVRBQ2FFSFo3dHFYcnRwNEw0R1EtM3lXVzkyQ0VsRi02MlJKQnVvdWlmdzJOT19XajgtRjVfbUw3SzRHaTNKdWNRSEtR?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPYm9PY0NHVnlSQ2Y2TFg2dnIxVjV5VGxoNkhoY0ZibTV5ZFg4bzVrWkplaXZMdy14cUYwdEhBVWk4WTJoVGh6ODNNUTU1WDBtSTJxM1lfUWo4Tmt3U3M3dGZ2VFotVnBSeXFnaHowbEd0RWZmb040YnBPYlc4Uy03azM4QzhrM0JsN1VrYVJDdlRUNHJ3ajZ6SHJBVGRsdGJPUDByY1NBLTMtMThE?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxOQkFZdjFhZXl2bTYzMXRCZ2p6dlI2ajQ4U0NKS0d4U05JT3R0OURaSU52ZzIydDJhWTRfNl84RDNmTjhYRTEtQkdnWlk1TDdRNEVyY1lCRWtQYjVreFl6ekJiOThSTVI2c2k3VnFlMnhqbVk2Q3JJR1BFMVdGTHZnSXd4OVVtcW9sSE9TZ0ZLXzFOXzRDUEVaTG1BYXhuQlU4aHRLWTdobGVrSHctS0JqZEtzcEplZ2Nt?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOLUVNeWVMdXFwU1BoOU5ENnc3SnRPZXZPSXVzQmFsVU9VSi1acTVqYVRxaTgwQjlQMVlQUkFTTkh0ZTlJaFhYMUJVcHAwUzVWYjlfTE5uN1Q5WTBqQWE5NXhTTW1URmxHTklCdXMxMzM0NDJHdG1yTWQ0R1lEM2V4U2ZGX1pWQzlDdGgtMWdBejEzNXNSQWdlaTNUX1d2Tzl1VHRDUDJnLXVkckxjWFZzdy1VNkNhVUZPcG4yVDJoQ3E?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxNNHZ4dFNFNmd1UXZQWkxfcDE3VVJQZGZWMWNoRkZlazByd2VfM0x2Vnh1c3hzdGd2TEVNM19OcU5hbkF4WmpmVV9PbzRjcmVKQ0pyczlvQmFfRnlJSHk0dXhlR1ZDcXV5WVFFWGxGMmxhOURjLW9YWXd3d3ViUk95OFd1RENFdlpkVWNNZEpPUzJRNjhrWHdMTnFWUGpYLS1DYkl3NjFPUW5YWnI3OTZ3WkJvdTFTYjhocGRGOTBIMjlrV3hYT3ZnMjZPMXZOdk90elZBd1hicXNmUdIB3wFBVV95cUxObVFIenladzhzdUNFc3Q2Xzg0R1NwZUhtT01COVBLdnBROExOd0xwNjBLaVl6OGliS19nN0wzaFVfMnBFM2Q0YjZ2bHMwZjg0RHRNcWQzaHJfWk10aWE0YVNvaC10TnoxbkR3TlplRTYxNGx3SUMwTkpIakhVVFQzLW42TVc3RU9OamlxQmNaYkxwX3FxU00zeU1hd3gyVVdxMXZsaUJzVlJna0otLWVLVmpMTTBsdTlldmJRX2xpeHQzRzdDZS1oS1lGalRKQS1tQ2pDWEI4a3RtR2VxYTNj?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxPMFVPLXFVcGJ4b3BQb0Z5THJ4Z3hFcllvWjRIY3V6NE4zM2ZGR1dUbXpveTFmdk5JckNwOTVTZEw0b1NGUWM1aHRZRktmLUcxblhoeEhTTHlzUHdGY2NxMzBkajEwOHJKVS0zSjFPZWRUZDMyU2N5UE5aNVJmOWF0aXNpT1cyREJBOGZkY0V1aWRVTDFld3RQY2RsWTJUMlFnSVJnWFViQ3M0eGdxalBkdXpwY1hack9NS0ozNjJRZDZtNVlZOUE?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNdW1xa3dCaEVrVzBscUpYZWRPR3U4QmFmZWtqT3M4ODVLdU43Q3lFWS1NcC0xdWF4ZnE5OU9SbFIway1wd0R0MmNtQ0NURnlraE1sQWRQbUFaVDRtbkhvbFI0OWRxQVRoYUZ3Uk9URnRwMzlQdm10dTVkTHdGSWpEZ0l0Rk9aTy1uTWFVYUVkYWxSTVNNeHEyMkR5T3A4djdCRElGSkFScVNMZWdmbDdMSWZibzZLallzUHRmcmdpY2ZXTVNFUTNN?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQdWVHS2FZd2dTM1U4UkdzdGFmM1AwWVFpNDJwZFA2WmUwN1U4X1d0aTkxN2ZEYU9CMndUY1VpajZVbU5wNjUxM0hkcHdqT1QwSElQLWZfdDUwZTY2aVhmcnc2eEwybWlvaldSMFRLbkpWZkhvSm14VzhTbmk1TVlQX3Z4S3hLMDk4Q05WeTNzZW1zY0tGRFNjUWI5cGQ?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE9LT3o4SFlxbzZjNzRrRlloQ0Y1SGxpR0dJTTVvdVhMSnV1QmpHRGNwcHVKOVM1Q2gxcGw4T0tYQ0twcWMxcHozeFBUYzE4V3E2eTFQdTlrNmdnWWN0UGFHVFNmc0pSWmRPbG1zZzdNcFZoTXMxMFZNSU5hV3J1eG8?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOaVExbjV1YWNRalAyS2NtY2NTV3NPTzVCUGYwUmFsNWMwRUFMUUxLRkxBRzNQdXk4eFpaWjZPUk1xbzlxWTJ6THhlWlJULTk0Z2VmcHpqcjR0Q3ZJczFYbXZRTXU0UzVPWG9HMm5kUE5VNDc4Q0tFRjNrajV2Y1F4bVJRWHdQc1RUb1A0SU9PcHVsSnFxVDQzUFU2Tl9wRWJPSUFRRkF2MzNkRHZNd251a2JicjN0THQxRTd5VjFKQ24tenpwdDc4Z2dOenpfRVhoNFY40gHYAUFVX3lxTE44clVSWVp3eVlJYlNJcGlwR0I0ZWlqVFV2dGVVUThPb1ltV3JUNGFwaDNqNzRzVldPMHZQYkEzSGl4MDJtQUwybmNyT0p5SWZSUjFpaDkweGFuUUl3MldHTXI1ZVBMa0Y3QWI1bDlid2EtOENuOXl5WUhTdlhHaTBwdUtuLVBkZ0s0b0ZnVU1iWlpNVFVJSEM5TkQtUXBmZ1g3MmhJeElEa3VKU1pyN0V4WWh1SU1iTXJfODRTbV8yeFRUZ3dncVBRUDlyLXhzeWxteENZRThOVQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOWnFWd3pHOWZWQjlpOV9wR3p3QXVEY1hOZjkzUVkyUnJITTZTMEcxb1FMcnVfQlU4Y192U25rY29RblgwZmdRNzU5dE8yMlFLay1RTFI3Zk0xVGowQWZ4bEUwODNVYXRSZDhycC0zZ3BBM0NnaWluSTdBRWlacHFJdU8tb1dUVHlCcXlraEMxU0ZQUkxJM3NJYw?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPcnFKa1BEV2dOUHl0LVZUYXNIZi1ySDlvcGZlemhwRndLSHl0U0VLQmZXMkhFZ0dZZTBkLUJlVzljbGFYMmU4QklMUkZWbGo5enZXYnp2ZVBfWnZIWHhQaTdYYWhpRm1LLTJKalFLeDVZSVBRYUZrZUxYWUhlWEczU2x3UWZXUVlVaVVYSGpId2xJcWRWRVA5RWVadGJGdTU1N0hIS2lUMlRBTTNHNkhOdGZR?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPanpYVHhXaXhLRHRUX3lEOEZkcVNFX3JmeW4tQklHOXpORjFqYmxXRHpDQTZnZUdkTFRLV3A3bFFUTkxnaGVLenRORFdkSXdNRlNzejlYa2JMcDZFVkJ1UXN6VEJVRm5ucG5XaWxkbDJ5dmd1UDBiR3gwWkNiX1BLWlZ6V1dJd0wzbzlGak5BSzFaUGdtV2Q4TUEyU3BvUQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQTWd6MzJHZzVDOWQwcHhGc1RnY2RlMW1Pa0JlRDBTMGdQa3BIemZyalU1WUxmWndKOGc5cC1Jckt2MGYtVlEyMWJ0WFdLVWNXVktOalg1elVqUERrVEZfOGtBZzZLaFd2WVVOVU0zdENmMlBnT3MtSjF2TjdJZDUxdW1fTzNZWDJhaWlRb1ZrbTV2b09N?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQSTVVY3NtRHR0S3AtRmRhR3BiQ0gtdl81V1lWMmhZQV9BZmlvREZ0MFA2Z18tZ2ZFU2VJeVlkOGtFR1M3aU44bE9ldmRsQVZLbDdfOHd5Q0hqOU1pcXNndk8taDNBLVB3eF9WU251aGRibHZzeVRLUERqWDlxbk4tY1ZOX0xGSWZHUjM1dWxUZmg1ZFdSZFVSTlFzQS1QWWNwS0E?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
