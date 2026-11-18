# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:07:53.795853+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 3, 'ai': 14, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 503.4100 |
| Return 1D (%) | -0.1725 |
| Return 1W (%) | -2.2903 |
| Return 1M (%) | -4.7924 |
| Return YTD (%) | 135.0626 |
| Return 1Y (%) | 109.3007 |
| Annualized volatility (%) | 73.6028 |
| Beta vs SPY | 3.4254 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.3753 |
| Downside deviation (rf=0, %) | 48.0067 |
| Sortino (rf=0) | 2.1086 |
| Historical VaR 95% (1D, %) | 6.7006 |
| Historical ES 95% (1D, %) | 9.6472 |
| Correlation vs SPY | 0.6413 |
| Tracking error vs SPY (%) | 65.6218 |
| P/E (trailing) | 107.80 |
| P/B | 12.07 |
| EV/EBITDA | 73.50 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 28.54 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 17.82 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 0.88 |
| MA50 | 555.0398 |
| Close vs MA50 (%) | -9.3020 |
| MA200 | 425.7415 |
| Close vs MA200 (%) | 18.2431 |
| RSI (14, Wilder) | 46.6255 |
| MACD (12,26) | -9.7951 |
| MACD signal (9) | -13.6012 |
| MACD histogram | 3.8061 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 503.4100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.1725 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.2903 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -4.7924 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 135.0626 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 109.3007 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 73.6028 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 48.0067 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.1086 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.7006 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.6472 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6413 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 65.6218 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4254 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.3753 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 28.5408 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.8830 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 107.7966 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 46.6255 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 3.8061 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.3020 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 18.2431 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD Stock Up 135% as Nvidia CEO Exit Tests a 100x P/E
- Summary: AMD Stock Up 135% as Nvidia CEO Exit Tests a 100x P/E
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNc1ljR2JaX3VQeTJad2dZS0JWQ18tZXc0S1kxYTFIZHF5WUNIcEd1eFE4MjRnV2RydVZxNDNjX1ppY01LRUQ0X3lIYkZ3NE5FdTRYa2NER1J3Z2Y2ZTM0NlByYmtOZkhrLVFieF9oWnM5cFp0TUg1bzduZGl5UWx2N3ZFTUNubjFvZU00Tm1uNVFtVXM0cGR4dXVWQWEtN1paMXhyRkdR?oc=5>

### Nvidia’s soap opera could be AMD’s big opportunity. Here’s why I’m buying
- Summary: AMD may benefit from Nvidia’s struggles, presenting a buying opportunity for investors.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPVE5KOHVIeDZjZ0k0ZEtSYkk2SUNFOGdZNldnNG1mZDFZZmViVDRyY3loZG8yeDREUmpTelByT3NYeXdTOEV0eEZCaVFPOEMtdklVd2Q0RS1rNERIbl92V2xCVExqaXNkYTNUakMxSDVmTWctb0tyMFRwZy1iaTJ4Ti10ZDBEN1pwZGlN?oc=5>

### Why AMD Stock Was Sliding Today
- Summary: AMD shares fell today, indicating short-term weakness for the company.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNb2ctVEw4Q2ZFLXlpc2ZpeUFwaS0xSDI2Q2tRc2dtMzJmaGJwZjNoakZiTGxZVDhXUUJsWjRwR0dFamttd25sZWk4b0h6bDJZa3llbFE0YV9ub3NfbnItZ0xRejR0MzZoSy02bzh5bXVGWHJBLXVsQjN3ZHhmOXRWQlZJSEtONzQ5cXpsX0dxTGtuZWpnTDBn?oc=5>

### Prediction: These Will Be Nvidia’s and AMD’s Stock Prices by the End of 2027 (Hint: Only 1 Is a Buy).
- Summary: Forecasts for AMD and Nvidia stock prices through 2027, suggesting a potential buy for one.
- Date: 2026-11-17 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNUVBXalR5cmxaQV80T2FxbEUyeklxNTRtT2JSay12LTNCVFZiWmQzZy1BZFVkRENOaFFFallNWDV3ZmZ1Z3RubE1nOWNSU3dncUVHQ2swSThWVFhOd2pScmhtWHZCdTRydEJUMUoyc0FmaHJxcG45MUd6ZkRaLU8ySUR2Y05oQko2VWExMS1vVkRDeHZMV1lwWGctSUNvUFBOMUdPVS10cWhlaFR1ajdONUsyN29DMTd3dmJpSXhLeFJtUjhNWUlpUElGSE5Eek80OFJSbHVR?oc=5>

### AMD: The Strong AI Contender Keeps Getting Better (NASDAQ:AMD)
- Summary: AMD continues to improve its AI capabilities, strengthening its competitive position.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPMGpqZ2pBdzdCMkhSV0hMX1ExZTRzSll1MHhnLTV5SC1GNXdGaWJxRWdlNjhaUHN5TFpLbUg2dF9LOGJRU0htUHRjX1lzemE4eGg4S2lCOVBxZFlWR29oWmVwVWo3YkJFOFdPSXFVcUZhOGFjbjhjLXR1UTNNMk5HV1YzNWdjNk9LcFVfLUlnWHdyZGM?oc=5>

### Nvidia’s Leadership Crisis Could Be a Major Opportunity for AMD Stock
- Summary: Nvidia leadership issues may create a buying chance for AMD shares.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOVGR3eEEtRnZGcEp4ZjN0Sk1jRkxLSUFEaDViSDU0V1pnQWZjMUNRRU1wcFItS19wWFdyUEVneWo3TFhWQzZ1ci1adGlKZEFKU3BHenJiUFlDM1RWaWpzdTZFOTBOQzMteXgxNVpNOVcwY0dUWG9sS3U1VHpnekdUNW52VTZHTW4yLUo3WGJpM294Z0xUUGw5ZUQ5Sk13TFlmSGtrcmpsMUMwbVRLTElFZXVR?oc=5>

### Why AMD, Micron, and Sandisk Stocks Are Surging After Nvidia Earnings — and Which Has More Upside Ahead
- Summary: AMD shares rise post-Nvidia earnings, indicating positive market sentiment and potential upside.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxNdUlRRnZtUG16MVlKRmx0bG1RSzJfaERvUWg1aFBJUERQbHlwemRkMjVvZFA5RUllOXVqQjVOZW94SVMxQjVLRTBJc3RDRWl4eXVEXzExMTFsZE9oLTM2bmhJRmhJZDFVZVhyYWlGZXduNFJIemVpcWNVZUhEWjZmN1c1VlhVd1N1Qm5Yd2p5Sm1aY1piSGN5eC1RNUVFRWtaZGlsUnBJcDJaVGFvNko3MmdETmZHUFItY1VsbGRBVFVsemVnSUc0ZQ?oc=5>

### Anthropic Just Delivered Great News for AMD Investors and Bad News for Nvidia
- Summary: Anthropic's news boosts AMD investor sentiment.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQbTBKTWc2Y1k4cXU1MGwwTUk3NnBndW9FQ2xTS0lkR21nVnpRRlRSNVZWZE95dUFKTzBBdkx4VVZyOWU2TDB3ejNZYVpzX3NQQno3OVJxNnpFWG8tUjdiNGpVZ1ZNRVVUVkhXTVRzU3FoZVZkcGMxZzQ5QlpLM3BFc2ZwMjI4YWlmNGluY01Hc3RIZEx2RzlVLW5ydzhiR1gy?oc=5>

### Advanced Micro Devices And 2 Other High Growth Stocks
- Summary: AMD highlighted among high growth stocks.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNTUhzLTRyOXRpNzlWd2hJcmhOS3A3MUtUUXdJQU4wOFpsWFktU0M5RHJMM1pHaDhTNEFLSFp6TEN2SzNVeTQtZ3czSXFqWVlldkJsQnJfLXViWWg5anBQMTdsb2JnTEZwcGFaZHQ0aHk3S2ZLM2VmZ0lBanp4Z1FDN3pUVXgyTTFrSVZxcnhTOUh6U0p1U1Q1d2FKRQ?oc=5>

## HEADWINDS

### US Stock Futures Edge Lower After Tech Sell-Off — NVDA Earnings, AMD, SPCX, DIS In Focus
- Summary: Tech sell-off pressures AMD, reflecting negative market sentiment.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxQdzE5aHpjcnRIZTlvSV90VEhaU2o0b2NkSktXUW0ySTRjSG1KMC1IS2FZWUFkUTN3TlBqMjJJNzVZWURFTmlERXZNS2dOQ3J6c3g5SmxGNXo5eU0wbmt6eFJKQWRydFBvVFhCTHhYUlFfakhVOFJCTnVDS1g0UDVWQV9kdnR0cURfUHQ1anpzdmptNklBaUtpVmJZS0luZko0d0R0NHJYR1FNa0NlWDRGZHlMZjAxX1BFVVFFcFBHZVNqTkdGbUhnWFBfTTdhWm9nSllHVWdzV0FzcDZO?oc=5>

### Insider Selling: Advanced Micro Devices (NASDAQ:AMD) EVP Sells 10,000 Shares of Stock
- Summary: EVP sells shares, raising concerns about internal confidence.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxNMlZHckhoZHpyaENqQndvSlBtQWZRUEJTTS1Ob21rdTJmdHBlUHFRSm4xX0doWnFUMUx1ZkJjM3RBQmRSaGFoTHRtSTlxemhndG5UdVJfOHd2dHVRNEs1QTlWOUgtZVRJNnlKLTF3aUdNT3Y2aXhDWjl4Nk9uTFkzTmlMaVhZMGtIVnQtbmhUWFNaaThkaUhFeWhxTE5vMmVhajdtUFRFa2d2U3RJanNwYmpxU0hOTnpwYThWQ0dxWXVNeVFUTTBubTZvTFZTUE1TUW90M1dkaE95S2s?oc=5>

### Is NVIDIA’s Turmoil Advanced Micro Devices’ (AMD) Biggest Opening Yet?
- Summary: Nvidia turmoil may negatively impact AMD’s market performance.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPeE4zN25uZ3h5c01LT2hKdFVrSncwaTlUWXpTUmNKZnpBZnB6b01JQTFIaW9IRms3NFVMS1lTLWZPNWVFajh5Vl90WXdjdEwxX29aTWhjLWtLeExZelZXRkpaZmV3VzVzakN2VzgwRjFkbi1BZkVESTlXZGx5d05LYm1SNnZRdlRhUW9NQ2d6UEh1R05TRFA0Q1MxcmJ6LXFmclRVbg?oc=5>

## CATALYSTS

### AMD Earnings: What Wall Street Missed
- Summary: AMD Earnings: What Wall Street Missed
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxNUU1HTWVkOF9QMnFGbjdXeWIxZmNCVEZaVFg1NjZwRTQtc3pzdEFKLW1KZHZuWE9MM2R0Z3A0ZWhvREs0OS1Nb0ZjSnY5bVdHNE1GRWlYNEVseWpzbUFpQThWbFA2cW5zTUZWTjdaR3RaZXgxZ2N3THhaSHROMDRla3cyeTg4QQ?oc=5>

### AMD Expects Its CPU Revenue to Double in 2027. Is NVIDIA’s Turmoil AMD’s Opening?
- Summary: AMD Expects Its CPU Revenue to Double in 2027. Is NVIDIA’s Turmoil AMD’s Opening?
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQQS1VNjFRWUxReHZERF9KalFEWW5yUVNPTGRfOHVYMWxfS2hZd2NqU0dDYjlwMkdHcUg2NHVmaHl0TGZtLUc0ei1qMldNaU5xSzN1aTJ4Xy1JeGZZTTdvVEJQczh6V2dVUEpFTnpXeWZuWWxQNmQ2OUg0LVZxZWY1cEtScmJvNUZyQ281V2pvMDF0SUNET1BxOXdfbw?oc=5>

### AMD Will Capture More Market Share Than Broadcom to End November as Nvidia's Leadership Vacuum Persists
- Summary: Forecast that AMD will overtake Broadcom in market share by end of November.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxNUEtFa05wLWJTVmlmb3NGOWhSem8wTEZzaS1SYThoRGJSU0I5azhlVndSQkx0MnZueEM0NnF5UjIya09zckRrNzVvUHpNM2hwS2J6ZjVXTUZBX19LaWEzcDRFOWVDbkNkRFdGSklueUQ3ckxYNHJRSTQ1YUVkZjRWaHhldlpBemd5VXdkUFpzMk1mZUJmeUhYRFUyR1BaTkRMQ3dZZjJ3Z2dnZjFEOW1TTVhwY1k0ck5ZblRyTU85aC1FM1pqYXBJaklxb0hLSGR6QmtHa0l4aXNvdHBJSUFB?oc=5>

### Advanced Micro Devices vs. Broadcom: One Stock Has a $27 Billion Advantage Investors Shouldn't Ignore
- Summary: AMD outperforms Broadcom with a $27B advantage.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxNRzNNRXMtVjVTc3RiVHcyaTAxcDZjOUlLbFp0X205cUZqajRQV2c5X3NqNkwxS1dZck11VndPRi1SZllZVk5oLVpTNEc3NDV5cnd4WmpsUWM4Z1ZoTWVMbVdKTFJETlJLZUhUZEhvck9uRUM4LW8xOEh2OGNMaEtZYzZnWHJia2tETDNFR09Qd29kOERTVW5rSXJqTm5PS2ZNdFp4aXAzUFV4S0djSktTVEV2d0Y1UE52YnZGREZUaUtnakliMEpuTVJHYmc4Z3pCbVpSSlFFVGNLUDI0c2hBc1F5NUh3c3NDaEE?oc=5>

### Why Advanced Micro Devices Stock Surged This Week
- Summary: AMD stock surged this week.
- Date: 2026-11-14 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNY2ZFMjdSWTFDS3UtR1c0NWJneU1QdGZLZEFBRzY1SC05U2hyXzE3QlNMa193bk1USTFfMHRNVGY0LUxGT0ZPNHZ6RXFTMk1keGYzdnhSRTdvQ1hicDF6SXVmQzlhamJvczJfMk1VVGN2dWZsUjFSdGRoQmgyZ0l2R2Y2QkExbHByZGpmVWFyVkI1ZVFyVnNiUEt3R3lndHlYVkFzME9JNDE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **107.80** | **12.07** | **73.50** | **44.70** | **833,176,600,576.00 USD** | **109.30** |
| NVDA | 19.65 | 16.39 | 18.50 | 105.90 | 3,753,892,642,816.00 USD | -16.49 |
| INTC | N/A | 2.55 | 15.99 | 20.90 | 293,228,544,000.00 USD | 58.95 |
| AVGO | 43.63 | 16.36 | 31.88 | 85.50 | 1,630,671,994,880.00 USD | 0.43 |

Peers fetched as_of: 2026-11-17; AMD reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,428,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipgFBVV95cUxNc1ljR2JaX3VQeTJad2dZS0JWQ18tZXc0S1kxYTFIZHF5WUNIcEd1eFE4MjRnV2RydVZxNDNjX1ppY01LRUQ0X3lIYkZ3NE5FdTRYa2NER1J3Z2Y2ZTM0NlByYmtOZkhrLVFieF9oWnM5cFp0TUg1bzduZGl5UWx2N3ZFTUNubjFvZU00Tm1uNVFtVXM0cGR4dXVWQWEtN1paMXhyRkdR?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPVE5KOHVIeDZjZ0k0ZEtSYkk2SUNFOGdZNldnNG1mZDFZZmViVDRyY3loZG8yeDREUmpTelByT3NYeXdTOEV0eEZCaVFPOEMtdklVd2Q0RS1rNERIbl92V2xCVExqaXNkYTNUakMxSDVmTWctb0tyMFRwZy1iaTJ4Ti10ZDBEN1pwZGlN?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNb2ctVEw4Q2ZFLXlpc2ZpeUFwaS0xSDI2Q2tRc2dtMzJmaGJwZjNoakZiTGxZVDhXUUJsWjRwR0dFamttd25sZWk4b0h6bDJZa3llbFE0YV9ub3NfbnItZ0xRejR0MzZoSy02bzh5bXVGWHJBLXVsQjN3ZHhmOXRWQlZJSEtONzQ5cXpsX0dxTGtuZWpnTDBn?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNUVBXalR5cmxaQV80T2FxbEUyeklxNTRtT2JSay12LTNCVFZiWmQzZy1BZFVkRENOaFFFallNWDV3ZmZ1Z3RubE1nOWNSU3dncUVHQ2swSThWVFhOd2pScmhtWHZCdTRydEJUMUoyc0FmaHJxcG45MUd6ZkRaLU8ySUR2Y05oQko2VWExMS1vVkRDeHZMV1lwWGctSUNvUFBOMUdPVS10cWhlaFR1ajdONUsyN29DMTd3dmJpSXhLeFJtUjhNWUlpUElGSE5Eek80OFJSbHVR?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPMGpqZ2pBdzdCMkhSV0hMX1ExZTRzSll1MHhnLTV5SC1GNXdGaWJxRWdlNjhaUHN5TFpLbUg2dF9LOGJRU0htUHRjX1lzemE4eGg4S2lCOVBxZFlWR29oWmVwVWo3YkJFOFdPSXFVcUZhOGFjbjhjLXR1UTNNMk5HV1YzNWdjNk9LcFVfLUlnWHdyZGM?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxOVGR3eEEtRnZGcEp4ZjN0Sk1jRkxLSUFEaDViSDU0V1pnQWZjMUNRRU1wcFItS19wWFdyUEVneWo3TFhWQzZ1ci1adGlKZEFKU3BHenJiUFlDM1RWaWpzdTZFOTBOQzMteXgxNVpNOVcwY0dUWG9sS3U1VHpnekdUNW52VTZHTW4yLUo3WGJpM294Z0xUUGw5ZUQ5Sk13TFlmSGtrcmpsMUMwbVRLTElFZXVR?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxNdUlRRnZtUG16MVlKRmx0bG1RSzJfaERvUWg1aFBJUERQbHlwemRkMjVvZFA5RUllOXVqQjVOZW94SVMxQjVLRTBJc3RDRWl4eXVEXzExMTFsZE9oLTM2bmhJRmhJZDFVZVhyYWlGZXduNFJIemVpcWNVZUhEWjZmN1c1VlhVd1N1Qm5Yd2p5Sm1aY1piSGN5eC1RNUVFRWtaZGlsUnBJcDJaVGFvNko3MmdETmZHUFItY1VsbGRBVFVsemVnSUc0ZQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQbTBKTWc2Y1k4cXU1MGwwTUk3NnBndW9FQ2xTS0lkR21nVnpRRlRSNVZWZE95dUFKTzBBdkx4VVZyOWU2TDB3ejNZYVpzX3NQQno3OVJxNnpFWG8tUjdiNGpVZ1ZNRVVUVkhXTVRzU3FoZVZkcGMxZzQ5QlpLM3BFc2ZwMjI4YWlmNGluY01Hc3RIZEx2RzlVLW5ydzhiR1gy?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNTUhzLTRyOXRpNzlWd2hJcmhOS3A3MUtUUXdJQU4wOFpsWFktU0M5RHJMM1pHaDhTNEFLSFp6TEN2SzNVeTQtZ3czSXFqWVlldkJsQnJfLXViWWg5anBQMTdsb2JnTEZwcGFaZHQ0aHk3S2ZLM2VmZ0lBanp4Z1FDN3pUVXgyTTFrSVZxcnhTOUh6U0p1U1Q1d2FKRQ?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxQdzE5aHpjcnRIZTlvSV90VEhaU2o0b2NkSktXUW0ySTRjSG1KMC1IS2FZWUFkUTN3TlBqMjJJNzVZWURFTmlERXZNS2dOQ3J6c3g5SmxGNXo5eU0wbmt6eFJKQWRydFBvVFhCTHhYUlFfakhVOFJCTnVDS1g0UDVWQV9kdnR0cURfUHQ1anpzdmptNklBaUtpVmJZS0luZko0d0R0NHJYR1FNa0NlWDRGZHlMZjAxX1BFVVFFcFBHZVNqTkdGbUhnWFBfTTdhWm9nSllHVWdzV0FzcDZO?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxNMlZHckhoZHpyaENqQndvSlBtQWZRUEJTTS1Ob21rdTJmdHBlUHFRSm4xX0doWnFUMUx1ZkJjM3RBQmRSaGFoTHRtSTlxemhndG5UdVJfOHd2dHVRNEs1QTlWOUgtZVRJNnlKLTF3aUdNT3Y2aXhDWjl4Nk9uTFkzTmlMaVhZMGtIVnQtbmhUWFNaaThkaUhFeWhxTE5vMmVhajdtUFRFa2d2U3RJanNwYmpxU0hOTnpwYThWQ0dxWXVNeVFUTTBubTZvTFZTUE1TUW90M1dkaE95S2s?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPeE4zN25uZ3h5c01LT2hKdFVrSncwaTlUWXpTUmNKZnpBZnB6b01JQTFIaW9IRms3NFVMS1lTLWZPNWVFajh5Vl90WXdjdEwxX29aTWhjLWtLeExZelZXRkpaZmV3VzVzakN2VzgwRjFkbi1BZkVESTlXZGx5d05LYm1SNnZRdlRhUW9NQ2d6UEh1R05TRFA0Q1MxcmJ6LXFmclRVbg?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxNUU1HTWVkOF9QMnFGbjdXeWIxZmNCVEZaVFg1NjZwRTQtc3pzdEFKLW1KZHZuWE9MM2R0Z3A0ZWhvREs0OS1Nb0ZjSnY5bVdHNE1GRWlYNEVseWpzbUFpQThWbFA2cW5zTUZWTjdaR3RaZXgxZ2N3THhaSHROMDRla3cyeTg4QQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQQS1VNjFRWUxReHZERF9KalFEWW5yUVNPTGRfOHVYMWxfS2hZd2NqU0dDYjlwMkdHcUg2NHVmaHl0TGZtLUc0ei1qMldNaU5xSzN1aTJ4Xy1JeGZZTTdvVEJQczh6V2dVUEpFTnpXeWZuWWxQNmQ2OUg0LVZxZWY1cEtScmJvNUZyQ281V2pvMDF0SUNET1BxOXdfbw?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxNUEtFa05wLWJTVmlmb3NGOWhSem8wTEZzaS1SYThoRGJSU0I5azhlVndSQkx0MnZueEM0NnF5UjIya09zckRrNzVvUHpNM2hwS2J6ZjVXTUZBX19LaWEzcDRFOWVDbkNkRFdGSklueUQ3ckxYNHJRSTQ1YUVkZjRWaHhldlpBemd5VXdkUFpzMk1mZUJmeUhYRFUyR1BaTkRMQ3dZZjJ3Z2dnZjFEOW1TTVhwY1k0ck5ZblRyTU85aC1FM1pqYXBJaklxb0hLSGR6QmtHa0l4aXNvdHBJSUFB?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxNRzNNRXMtVjVTc3RiVHcyaTAxcDZjOUlLbFp0X205cUZqajRQV2c5X3NqNkwxS1dZck11VndPRi1SZllZVk5oLVpTNEc3NDV5cnd4WmpsUWM4Z1ZoTWVMbVdKTFJETlJLZUhUZEhvck9uRUM4LW8xOEh2OGNMaEtZYzZnWHJia2tETDNFR09Qd29kOERTVW5rSXJqTm5PS2ZNdFp4aXAzUFV4S0djSktTVEV2d0Y1UE52YnZGREZUaUtnakliMEpuTVJHYmc4Z3pCbVpSSlFFVGNLUDI0c2hBc1F5NUh3c3NDaEE?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNY2ZFMjdSWTFDS3UtR1c0NWJneU1QdGZLZEFBRzY1SC05U2hyXzE3QlNMa193bk1USTFfMHRNVGY0LUxGT0ZPNHZ6RXFTMk1keGYzdnhSRTdvQ1hicDF6SXVmQzlhamJvczJfMk1VVGN2dWZsUjFSdGRoQmgyZ0l2R2Y2QkExbHByZGpmVWFyVkI1ZVFyVnNiUEt3R3lndHlYVkFzME9JNDE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
