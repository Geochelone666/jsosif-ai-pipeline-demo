# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T02:05:56.320317+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 9, 'ai': 11, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261026T005504Z-6368ad31/JPM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 6 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 68.0%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 334.0400 |
| Return 1D (%) | 0.7419 |
| Return 1W (%) | 0.1529 |
| Return 1M (%) | -2.1435 |
| Return YTD (%) | 5.6649 |
| Return 1Y (%) | 13.3250 |
| Annualized volatility (%) | 22.0393 |
| Beta vs SPY | 0.7291 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.6262 |
| Downside deviation (rf=0, %) | 15.9141 |
| Sortino (rf=0) | 0.8672 |
| Historical VaR 95% (1D, %) | 2.3923 |
| Historical ES 95% (1D, %) | 3.2600 |
| Correlation vs SPY | 0.4207 |
| Tracking error vs SPY (%) | 20.2891 |
| P/E (trailing) | 14.01 |
| P/B | 2.52 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 13.08 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 42.58 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 343.6182 |
| Close vs MA50 (%) | -2.7874 |
| MA200 | 319.7940 |
| Close vs MA200 (%) | 4.4547 |
| RSI (14, Wilder) | 45.9056 |
| MACD (12,26) | -2.1159 |
| MACD signal (9) | -2.8164 |
| MACD histogram | 0.7005 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 334.0400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.7419 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.1529 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -2.1435 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 5.6649 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 13.3250 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.0393 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 15.9141 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8672 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.3923 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.2600 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4207 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.2891 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7291 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6262 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.0836 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 42.5840 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.0117 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 45.9056 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7005 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -2.7874 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 4.4547 -> Slightly above the moving-average trend level.

## TAILWINDS

### JPMorgan (JPM) Stock Could Be 33% Undervalued Following JPM Coin Expansion
- Summary: JPM Coin expansion may boost JPM stock, suggesting undervaluation.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNaU9vbG5tendjbUhPc05YeUpNSjN0MDMyTWswQzFkd1g1NWppUUJxeWlfVEpVQmVlTDF6Z2NsLU52NGxnaVl5bDdNYWRvNVQ0WjZNbnZRZVlQcjRRd2FRU3o0WFpmbHJQR2toVDB4Vm9LLXV1c0Z5NXliRnhSYThKVVF1N25UdmdBT2xlQW9fUGtwMVpUOTdz?oc=5>

### Is JPMorgan Chase (JPM) Undervalued As Bond Issuance And Earnings Strength Meet A Pullback?
- Summary: Bond issuance and earnings strength hint at undervaluation.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQQWdlQWJZZE1LUzdSdVVuRHlmZmJtMVZTdE1ZcTVJRUJrTF9SdGxTWFpxdGNwQkQtenVtNW1JdS1KS0JxSlJpWDNZQ01YMFBBZFlwRXVDR3FyRUc5NkVZV0R5aVZ6dloyMGtwUm1VMHBJLVkxSjJFZnc5elF6VWhqM2F2ZDhJWE9SN01MNUU2TVA4cHFCMmtiWC1SRGVpeTUxczVHRzdqQU9uYnRjYTB0RTdzWlF1U0J4aEs5MElMYXo2cS1PaXfSAcsBQVVfeXFMTk5uY1ZmZmk4bkxka3JUUmw1UlFoWi1FQ3RyUGtDMWxXUGdzR1d3S043R2J2aVA2X3RYTW1VdDh4SzVFS3dETk9YbmwwX20waDg4dnZWREpxQm5iVzNnazZjVFByV0VDOWVaeDFWZEVrcldfblkwdjg0M0xpZE85TXpMUVZTZEhpX0pLOG5Bb1BVeGJvZW1ZNUMydnFuZXY3MVp5MnFPQ1VFR2tVSnpjbG1jOEtFVUZnSlFkVlJLbHpOZVBjVE1GalNMdEE?oc=5>

### Vest Financial LLC Buys 21,084 Shares of JPMorgan Chase & Co. $JPM
- Summary: Institutional purchase may signal confidence.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxNWG1vX01KUUR4d0JhYWtGQ1ZaQnpRUDM4ODRob2c1dzRwMWw2SlFUTndIXzk2aXQzb2dxOFZOZ3VzbXpubE9ERXhicUNzN2ZjS3NCa3hTUV9xclltSEVUVGNSOTZWZDJiWDBFX2xEOGpCT2ZyaWdaUk8xaHAxeUpkaEQxbGY2OENIVEhPRmstVHA3dmhhczJaYkUtRXR1VHFKREFVaWY1ay0wUTlYdFRHTWZRckJXdXFLRVBPVFBVZw?oc=5>

### JPMorgan Chase (NYSE:JPM) Lifts Interest Income Outlook as Lending Offsets Trading Slowdown
- Summary: Higher interest income outlook offsets trading slowdown.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxNV2c0Q0RkQTlzRWdlYl9PTkZQQXNOMl9wckI2bE9va2dEWmlKUEQ4WExnbTJ6WEdSYUNKYnQxMkdmWjB2bzBKMVZUVUNqSHhIbEd0TkZHcGlZbWZtZEQwc0JiT3JDVkxNTmYyUDZRVkR4VngwT1R4Q1VCQ2RlWGtJbnZidWcwUlFJZHdsR05kZE16RldoUUdFN3JvNFpRODhqaHFRbDJ2dE9rQmEzOG5HbHJsOVhRYl9UYkR0VklZMnVHblJKWWRfU09mVDNVQQ?oc=5>

### 5,154 JPMorgan Chase & Co. $JPM Shares Sold by Commonwealth Financial Services LLC
- Summary: Share sale may indicate portfolio rebalancing.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNd2NmZ09SNzVEQ3VqdEEyZ2JpVmMzZ2RidVh2MVJPOXFPWG1WYTdZd2pEZWh3MUxTbDZOOWdkTGZDRWEteTd3VDBzbjBJcUtzRkh2bVNON0lqNFRYZ1VPZ2JyMUFFMTBub1FxR2I2WURZdk8tY2owa01nazFaczF4anFwdTlJMjA1WE10THI0ZFVNUExGS3N5dUFLRDUxczVDY1NoekNDNlBMb0FvbkRjNVo0aDE2ejEydW8wY3NrQ19NbFBLZmstdWduUHg0RUlSLUctUg?oc=5>

## HEADWINDS

### JPMorgan Chase & Co. (NYSE:JPM) Stock Price Down 1.4% - What's Next?
- Summary: JPMorgan Chase & Co. (NYSE:JPM) Stock Price Down 1.4% - What's Next?
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQb3VYMHhoSXpoQ3BLS2RHZkE3Zks1cnBsMnEtUTJESGJfYnVBLTV1ZWJuREJCRHM2TmJVcmFtZGJzZlZZcDFIQW1NdjV0LWVIMTlMdHd3aVFTWDBxOHVZRFhybFU1RzBpcXpUcTZqMXJ5M2JkbGVHejgtOVhjSkotUEktTWtKcG1VbW1vWmF5T1ZfU3NpMnhnRFpfOTFnc0lUYnd2YWNfTEJ3Wko5a0NQNGtlQjhtWTNn?oc=5>

### JPMorgan Chase & Co. $JPM Stock Holdings Lowered by RWQ Financial Management Services Inc.
- Summary: JPMorgan Chase & Co. $JPM Stock Holdings Lowered by RWQ Financial Management Services Inc.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxPMkNOVWtScWRTSmQ3YktzLWV5emw3QVUzaS1LZWVZNFduTUpGX3NLc01GWW0ySmltQ1FSazdhdGFJMnQ3ZHNzZ3pYZC1JdXlLbnhDM1hqenRZazBPczg2dW1PSGV2UDJ5RmFLWlREbHBCeDZDRG1CMEJoVE5SQ2t1VnRGYWlYMTZiMHFOM0hXdFVvWHNfWUlXem1mVTJPWnNYLVQ4QkRhNVlJSDdONGJqaGt1a3NBaWJOcTE2WTVmcGwxbUoyUDVUNXp4MlFodWFRem5TWjNKYkVwTS1Fem9z?oc=5>

## CATALYSTS

### JPMorgan Chase & Co. $JPM Stock Sold by Arvest Investments Inc.
- Summary: JPMorgan Chase & Co. $JPM Stock Sold by Arvest Investments Inc.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPMHhtUGxlUnBQcWJhTC1BdnZtaS1TMnJJUVpqZkQ2VkhpWDZ5OUlXWUJQRnpOM0pROXhwZXQ3TlFvZkE0cnhxbTgyc2ROczFZNHROWG5UUU5BTUQ5YWVzSnNyWW11YUt4d1pQTGpqU2diUy1JNmtTU1NrWWI5VVoyd2VZam5OQVhpNnBTRTVidTI5OWdOZU5sOEZFcDJUNGZWLUg3Y0M1aGJvenZCVTgzY09SclRlSEZ3b0Jz?oc=5>

### JPMorgan Chase & Co. $JPM Stock Sold by Hosking Partners LLP
- Summary: JPMorgan Chase & Co. $JPM Stock Sold by Hosking Partners LLP
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPTVBTZmJ3Vk9acUQ5M09uVjA3V3plM0xwOWhkcURiVkl6cE5WY2JMbXUyTmkwTkE1RmltaGM4MkQ2VzVsYl9xdkhBbS03NGh3OTY4UllVSkpzbWVocWpkcElOQTQxQ1hDQUs3cG4xdzlwQThOMjZ5RU1KYVVfZEY1MFFLSWhvMVNoeGJzWHZQcHBESlVfSXc0LThNLWMyd2hjQTBVXzg2VXlFamh4bW5WcW5STm5nMGlt?oc=5>

### JPMorgan Chase & Co. $JPM Stock: Focused Alpha LLC Increases Position
- Summary: JPMorgan Chase & Co. $JPM Stock: Focused Alpha LLC Increases Position
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQNDRjM3pvVV95enBYUUx3LTBLNG05S195UG91VHZRMUsyUXF4X0RFYjdjNGU3ZTBHRnlxbkl5Z1NybmpqTW5EWVliY25uUWY3aGEwUTRBYnB3eFNsOXZuaHVXTDg3N3RtdThmb2VhY09WNFgtUlFzcTc0LTY0eDMzSWtYbFdHcHhiaHFRYVI0R0JFdEZDeUxwdlVfcGVxT204RzdxLXBTZkRuRE95cTl4UnVJb1NDMWg2d01lSkNTZE81Vms?oc=5>

### JPMorgan Chase & Co. $JPM Stock Sold by Grandview Asset Management LLC
- Summary: JPMorgan Chase & Co. $JPM Stock Sold by Grandview Asset Management LLC
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxPenV1WDJlV0Q5VE1pQmkyUWtoa0F2WFVHQnRpU1NoWjdJUFozVU9US1psSUg2M1I3Um1KQXRUYVRhV1VNVHYzMDhGdHZSR1lEV29UUGVOVFdWcWlhRmlCV2daWks4ZzBzMFNLdGZDMWhlcEdWLV9XcTJaMmRYVDN3NXI5RGQ4TzlLV2txSXlKSzkwVVlOZ2VPZHVmNXMtaDc3REh2eUdMZTA5b1E2R3R0NEVPa0tFMjUyS1QwTXhfQUx5c1p5TlE?oc=5>

### JPMorgan Chase & Co. $JPM Shares Sold by Willis Investment Counsel
- Summary: JPMorgan Chase & Co. $JPM Shares Sold by Willis Investment Counsel
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOMG1DLUtQakZKS3pKd3Q4YTJXa2o0Z2JjY0RsMjk1VkRMMHlXdjBwRm5MOG9JZmdON1djMnZKSU0taTR4cDVKcnc0V3ZhcGxfWmd5NzI2V255Mkh5N1FmR0Ftd3JFRHB1eVU2WVp3eWM2aUp0ZTdWSU9Qa21XVkRfSmppRV9SNTBsOXpWY3ZtdzVnMFZlTXFJSXdTeFpfSzBEUzJDZ3B2eFRlQzAzZld4alIzZFJSWmY1TExwa2pIOEY?oc=5>

### JPMorgan Chase & Co. $JPM Stock: BDF Gestion Reduces Holdings
- Summary: JPMorgan Chase & Co. $JPM Stock: BDF Gestion Reduces Holdings
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNWFprSXlPazRSblVDaTI3LWZTNGdoNllMUGhyTGlBVXJmbkt4M2F2UmZIa0FGLTdLVWJaMl80bzZVbExSZEFmVlNUZTVJRm5RVzdwWElBYmJzSXRnVDk1bnAxaDM3Q2p1ODc5N2ZpbEYtQ3hsRmxPRzBZOGJWUmVqTXc0U1dIc2RVVG5YckdwcWNYMUJZMDJUQkJEdnBQdGx4MmdiUklDZkVtVjZ1UkYzSXR0d2syT3Nf?oc=5>

### JPMorgan Chase & Co. $JPM Stock: Birch Hill Investment Advisors LLC Lowers Holdings
- Summary: JPMorgan Chase & Co. $JPM Stock: Birch Hill Investment Advisors LLC Lowers Holdings
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQY1ZJeFRzMlBPdmxlSVZiV3ZxS19sallCZEtBOW1zLTdibGpFU09raENBdlJ6UW1kX2xZZmxreE5LLU1yT21RVUVpSnlUaHJTT0ZvOHZ0bmxJeWdQUTk1VXhaRXNGY3c0b1N4c1N2TEl3UHl1U3hIeVFQZnFBWU1IWGJKTXZwd0lhbVJ6cVF4OExKSEtPU2t4QXFJTGs3dlVBUldPTTd3c3dqVDVaX3RnREtpbVpQTnBUMW1NUlBTVmVtSUlYTk1yc3J0WmdDVHFvWm9yeldB?oc=5>

### JPMorgan Chase & Co. $JPM Stock Holdings Cut by Pinnacle Associates Ltd.
- Summary: Pinnacle Associates reduced its JPM holdings, indicating a potential shift in analyst sentiment.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxPTkM2bmlrQjZwX2ZHNko4eEhUZGZvTm9CUDNXaWVLdUJOVVRfa1huZVZxRUdmcGRjZzl3ZGtSc0x2Q05zczI5TUpWMGcydVJMbTJYUWR0R2ZtT1hVbHctNlExNlRPVnpFOVZ2RTZHbXhEUTVSUUlWWXI5aHlLXzNEOWpfMkNyX0hTSW9qdVo3clRIZVBBMGFhTnNnY05tQW1qOTUyS0VtSnNxSXRkVzl0WU04QVRla01idlpHLWZ2c1JUQWZNeFVv?oc=5>

### JPMorgan Chase & Co. $JPM Stock: Carnegie Investment Counsel Trims Holdings
- Summary: Carnegie Investment Counsel decreased its JPM holdings, reflecting a change in analyst view.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxOeWRoUlFSZEtLTnhOSVNTM214TDlNSVV1ZXdQdFdYb3BJU0lJSnlhMGdtNHdSS3Q1UXpwRmdPREhvWExQZ1Y5QkQweDM0VF81TVduS29IbXZvNnlrekZueWV6UTc0YTlYX0Vtdk9Yam83VmdBc2dwVFdjdTgzR0N5MkM1WHRNdFFjcTdSQ0pCMklhQUV2ZWkyNGNibjhCeTkyVFJ1eldTS2Y3TUhLc1V5bWRVTl9pVm9pYnZTNzA2UjcwSGU0c1R6aDhIaw?oc=5>

### JPMorgan Chase & Co. $JPM Stock: SteelPeak Wealth LLC Boosts Holdings
- Summary: SteelPeak Wealth LLC increased its JPM holdings, indicating confidence in the bank's prospects.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQQzY3X29lNl95NmF4Nkw1TjBFWU9HaU5KcWlJQ0RZUlpqNnF3clFCQ3VBWWVkb0Nfa1FSS0ZkeklycmhtQlNQalJBV0I5X0dfYWN1bXhaZEVDN2dyRHdWWm95Y0REOVJsWnREWXhwMUtjZlZZWU0xdGZJOVR0d2lja19QUEk3eGdHRlBjSERNSkQ0S2VHN3VPUVRRdkdmMHFrb1dEOUlLRklYcUpIbXJzVzJ6U1lYdzF5aXFkTG5vT1V4aWc?oc=5>

### James Hambro & Partners LLP Sells 7,733 Shares of JPMorgan Chase & Co. $JPM
- Summary: James Hambro & Partners LLP sold 7,733 JPM shares, a divestment move.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxQc200aVhqdFJCQlJRVDdwMERia0ZCM3JoRWgzdDBMclE5RnJWSHU5eHowa1Bxc25rVzV1SVhSdm8wNVp3bE5qa3JyMzVPR29GX0tEbjVRb1pnUmdMazl5THd3azk1VlZJZ0lMNWtIODJtUTBKU0xaaF9WWnc0VnRTMTIzNnE1ckFUdE96d21IVWhDS25QSkNudjJMNHZkd3hrT0pqWXdFLW1ZaUJjLVEyb3o2NXhjYThBRzZES2xjQ2duemNfSUI0WQ?oc=5>

### JPMorgan Chase (JPM) Puts JPM Coin on Ethereum for Institutional Payments
- Summary: JPM launched JPM Coin on Ethereum to facilitate institutional payments.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNNzVNbW9MWnd2YV9qRU9pR2NTYzRxMTdzSVJ5Y0Nsc0VmNzVFSXVRYnNIYUVrT3NWa1hDSjZKXzh0TkxtMnlsTFV2VVY4UlZhYnk1aGx1NTE0SWJBRXRCTnNIMXJXUGVGWXRyOG9ZY2R5VTNlUTczVEtVZWFHY0JHUHlHSWRwM2E1SzN1dGtFdkVoRGN5Y2RJU1Q4OTJQS096cVg1T0VYMjR2OVpyV0J1U1kxcUJ0OXRRZEpObWlYMDdIcU5PVEHSAcsBQVVfeXFMUE9WdEFHRlVvQU9qX1VkYndfLUNmM0ViRnh2VzdpU0pCeGhGbmZacFpMT29mUk1sazBOeUc3dHdfc1NQNFlLLVdUX1V1MVVlb1pLY1BwM2FQUEF2OGx1UDgxWmJrenVCTGVrT2NBVXpaelBFbjVJVnk3MVpJT1FfMWJGZzluVFpoVnlxOU5sU3ZRSDktaXZpbVdfNEZfRlJvNTJSb1drTjNqSGVIQ2VkdnhTN2xDdFlLZXdvOUkxZmRXLV9PMkJ2Xy12cDg?oc=5>

## RISKS

### Jamie Dimon Just Listed 5 Market Risks Hiding 'Under the Surface.' JPMorgan Is Already Feeling The Heat.
- Summary: Jamie Dimon identifies five hidden market risks affecting JPMorgan.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOU3g4a0pTeGFlLUk3c3JNcDRiaDE4OVJJdkNWUkNYSmZTWllIb2QxcGQ3RXBIQkZlSUktYWdVc1drVTZpUnRoVmJDa1QzT3hkaG5BQXFvaE1fR0d3aENVYmpvNTRDQS1hUVZQRGlHaS1mM19NUDFnYXpCZkZXUkxrXzNFc1dWYy1HcWRMWnhEZm56SmlM?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **14.01** | **2.52** | **N/A** | **10.20** | **887,076,683,776.00 USD** | **13.32** |
| BAC | 12.06 | 1.29 | N/A | 7.10 | 349,734,567,936.00 USD | -1.85 |
| C | 11.80 | 1.05 | N/A | 8.00 | 200,345,403,392.00 USD | 25.13 |
| WFC | 11.66 | 1.56 | N/A | 0.40 | 248,085,463,040.00 USD | -2.27 |

Peers fetched as_of: 2026-10-26; JPM reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-06
- Revenue (latest available single quarter): 24,246,000,000.00 USD; period 2014-07-01/2014-09-30; fiscal year/reporting period 2014/Q3
- Net income (latest available single quarter): 21,155,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/19617/000162828026054343/jpm-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilwFBVV95cUxNaU9vbG5tendjbUhPc05YeUpNSjN0MDMyTWswQzFkd1g1NWppUUJxeWlfVEpVQmVlTDF6Z2NsLU52NGxnaVl5bDdNYWRvNVQ0WjZNbnZRZVlQcjRRd2FRU3o0WFpmbHJQR2toVDB4Vm9LLXV1c0Z5NXliRnhSYThKVVF1N25UdmdBT2xlQW9fUGtwMVpUOTdz?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQQWdlQWJZZE1LUzdSdVVuRHlmZmJtMVZTdE1ZcTVJRUJrTF9SdGxTWFpxdGNwQkQtenVtNW1JdS1KS0JxSlJpWDNZQ01YMFBBZFlwRXVDR3FyRUc5NkVZV0R5aVZ6dloyMGtwUm1VMHBJLVkxSjJFZnc5elF6VWhqM2F2ZDhJWE9SN01MNUU2TVA4cHFCMmtiWC1SRGVpeTUxczVHRzdqQU9uYnRjYTB0RTdzWlF1U0J4aEs5MElMYXo2cS1PaXfSAcsBQVVfeXFMTk5uY1ZmZmk4bkxka3JUUmw1UlFoWi1FQ3RyUGtDMWxXUGdzR1d3S043R2J2aVA2X3RYTW1VdDh4SzVFS3dETk9YbmwwX20waDg4dnZWREpxQm5iVzNnazZjVFByV0VDOWVaeDFWZEVrcldfblkwdjg0M0xpZE85TXpMUVZTZEhpX0pLOG5Bb1BVeGJvZW1ZNUMydnFuZXY3MVp5MnFPQ1VFR2tVSnpjbG1jOEtFVUZnSlFkVlJLbHpOZVBjVE1GalNMdEE?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxNWG1vX01KUUR4d0JhYWtGQ1ZaQnpRUDM4ODRob2c1dzRwMWw2SlFUTndIXzk2aXQzb2dxOFZOZ3VzbXpubE9ERXhicUNzN2ZjS3NCa3hTUV9xclltSEVUVGNSOTZWZDJiWDBFX2xEOGpCT2ZyaWdaUk8xaHAxeUpkaEQxbGY2OENIVEhPRmstVHA3dmhhczJaYkUtRXR1VHFKREFVaWY1ay0wUTlYdFRHTWZRckJXdXFLRVBPVFBVZw?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxNV2c0Q0RkQTlzRWdlYl9PTkZQQXNOMl9wckI2bE9va2dEWmlKUEQ4WExnbTJ6WEdSYUNKYnQxMkdmWjB2bzBKMVZUVUNqSHhIbEd0TkZHcGlZbWZtZEQwc0JiT3JDVkxNTmYyUDZRVkR4VngwT1R4Q1VCQ2RlWGtJbnZidWcwUlFJZHdsR05kZE16RldoUUdFN3JvNFpRODhqaHFRbDJ2dE9rQmEzOG5HbHJsOVhRYl9UYkR0VklZMnVHblJKWWRfU09mVDNVQQ?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNd2NmZ09SNzVEQ3VqdEEyZ2JpVmMzZ2RidVh2MVJPOXFPWG1WYTdZd2pEZWh3MUxTbDZOOWdkTGZDRWEteTd3VDBzbjBJcUtzRkh2bVNON0lqNFRYZ1VPZ2JyMUFFMTBub1FxR2I2WURZdk8tY2owa01nazFaczF4anFwdTlJMjA1WE10THI0ZFVNUExGS3N5dUFLRDUxczVDY1NoekNDNlBMb0FvbkRjNVo0aDE2ejEydW8wY3NrQ19NbFBLZmstdWduUHg0RUlSLUctUg?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQb3VYMHhoSXpoQ3BLS2RHZkE3Zks1cnBsMnEtUTJESGJfYnVBLTV1ZWJuREJCRHM2TmJVcmFtZGJzZlZZcDFIQW1NdjV0LWVIMTlMdHd3aVFTWDBxOHVZRFhybFU1RzBpcXpUcTZqMXJ5M2JkbGVHejgtOVhjSkotUEktTWtKcG1VbW1vWmF5T1ZfU3NpMnhnRFpfOTFnc0lUYnd2YWNfTEJ3Wko5a0NQNGtlQjhtWTNn?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxPMkNOVWtScWRTSmQ3YktzLWV5emw3QVUzaS1LZWVZNFduTUpGX3NLc01GWW0ySmltQ1FSazdhdGFJMnQ3ZHNzZ3pYZC1JdXlLbnhDM1hqenRZazBPczg2dW1PSGV2UDJ5RmFLWlREbHBCeDZDRG1CMEJoVE5SQ2t1VnRGYWlYMTZiMHFOM0hXdFVvWHNfWUlXem1mVTJPWnNYLVQ4QkRhNVlJSDdONGJqaGt1a3NBaWJOcTE2WTVmcGwxbUoyUDVUNXp4MlFodWFRem5TWjNKYkVwTS1Fem9z?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPMHhtUGxlUnBQcWJhTC1BdnZtaS1TMnJJUVpqZkQ2VkhpWDZ5OUlXWUJQRnpOM0pROXhwZXQ3TlFvZkE0cnhxbTgyc2ROczFZNHROWG5UUU5BTUQ5YWVzSnNyWW11YUt4d1pQTGpqU2diUy1JNmtTU1NrWWI5VVoyd2VZam5OQVhpNnBTRTVidTI5OWdOZU5sOEZFcDJUNGZWLUg3Y0M1aGJvenZCVTgzY09SclRlSEZ3b0Jz?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPTVBTZmJ3Vk9acUQ5M09uVjA3V3plM0xwOWhkcURiVkl6cE5WY2JMbXUyTmkwTkE1RmltaGM4MkQ2VzVsYl9xdkhBbS03NGh3OTY4UllVSkpzbWVocWpkcElOQTQxQ1hDQUs3cG4xdzlwQThOMjZ5RU1KYVVfZEY1MFFLSWhvMVNoeGJzWHZQcHBESlVfSXc0LThNLWMyd2hjQTBVXzg2VXlFamh4bW5WcW5STm5nMGlt?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQNDRjM3pvVV95enBYUUx3LTBLNG05S195UG91VHZRMUsyUXF4X0RFYjdjNGU3ZTBHRnlxbkl5Z1NybmpqTW5EWVliY25uUWY3aGEwUTRBYnB3eFNsOXZuaHVXTDg3N3RtdThmb2VhY09WNFgtUlFzcTc0LTY0eDMzSWtYbFdHcHhiaHFRYVI0R0JFdEZDeUxwdlVfcGVxT204RzdxLXBTZkRuRE95cTl4UnVJb1NDMWg2d01lSkNTZE81Vms?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxPenV1WDJlV0Q5VE1pQmkyUWtoa0F2WFVHQnRpU1NoWjdJUFozVU9US1psSUg2M1I3Um1KQXRUYVRhV1VNVHYzMDhGdHZSR1lEV29UUGVOVFdWcWlhRmlCV2daWks4ZzBzMFNLdGZDMWhlcEdWLV9XcTJaMmRYVDN3NXI5RGQ4TzlLV2txSXlKSzkwVVlOZ2VPZHVmNXMtaDc3REh2eUdMZTA5b1E2R3R0NEVPa0tFMjUyS1QwTXhfQUx5c1p5TlE?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOMG1DLUtQakZKS3pKd3Q4YTJXa2o0Z2JjY0RsMjk1VkRMMHlXdjBwRm5MOG9JZmdON1djMnZKSU0taTR4cDVKcnc0V3ZhcGxfWmd5NzI2V255Mkh5N1FmR0Ftd3JFRHB1eVU2WVp3eWM2aUp0ZTdWSU9Qa21XVkRfSmppRV9SNTBsOXpWY3ZtdzVnMFZlTXFJSXdTeFpfSzBEUzJDZ3B2eFRlQzAzZld4alIzZFJSWmY1TExwa2pIOEY?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNWFprSXlPazRSblVDaTI3LWZTNGdoNllMUGhyTGlBVXJmbkt4M2F2UmZIa0FGLTdLVWJaMl80bzZVbExSZEFmVlNUZTVJRm5RVzdwWElBYmJzSXRnVDk1bnAxaDM3Q2p1ODc5N2ZpbEYtQ3hsRmxPRzBZOGJWUmVqTXc0U1dIc2RVVG5YckdwcWNYMUJZMDJUQkJEdnBQdGx4MmdiUklDZkVtVjZ1UkYzSXR0d2syT3Nf?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQY1ZJeFRzMlBPdmxlSVZiV3ZxS19sallCZEtBOW1zLTdibGpFU09raENBdlJ6UW1kX2xZZmxreE5LLU1yT21RVUVpSnlUaHJTT0ZvOHZ0bmxJeWdQUTk1VXhaRXNGY3c0b1N4c1N2TEl3UHl1U3hIeVFQZnFBWU1IWGJKTXZwd0lhbVJ6cVF4OExKSEtPU2t4QXFJTGs3dlVBUldPTTd3c3dqVDVaX3RnREtpbVpQTnBUMW1NUlBTVmVtSUlYTk1yc3J0WmdDVHFvWm9yeldB?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPTkM2bmlrQjZwX2ZHNko4eEhUZGZvTm9CUDNXaWVLdUJOVVRfa1huZVZxRUdmcGRjZzl3ZGtSc0x2Q05zczI5TUpWMGcydVJMbTJYUWR0R2ZtT1hVbHctNlExNlRPVnpFOVZ2RTZHbXhEUTVSUUlWWXI5aHlLXzNEOWpfMkNyX0hTSW9qdVo3clRIZVBBMGFhTnNnY05tQW1qOTUyS0VtSnNxSXRkVzl0WU04QVRla01idlpHLWZ2c1JUQWZNeFVv?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxOeWRoUlFSZEtLTnhOSVNTM214TDlNSVV1ZXdQdFdYb3BJU0lJSnlhMGdtNHdSS3Q1UXpwRmdPREhvWExQZ1Y5QkQweDM0VF81TVduS29IbXZvNnlrekZueWV6UTc0YTlYX0Vtdk9Yam83VmdBc2dwVFdjdTgzR0N5MkM1WHRNdFFjcTdSQ0pCMklhQUV2ZWkyNGNibjhCeTkyVFJ1eldTS2Y3TUhLc1V5bWRVTl9pVm9pYnZTNzA2UjcwSGU0c1R6aDhIaw?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQQzY3X29lNl95NmF4Nkw1TjBFWU9HaU5KcWlJQ0RZUlpqNnF3clFCQ3VBWWVkb0Nfa1FSS0ZkeklycmhtQlNQalJBV0I5X0dfYWN1bXhaZEVDN2dyRHdWWm95Y0REOVJsWnREWXhwMUtjZlZZWU0xdGZJOVR0d2lja19QUEk3eGdHRlBjSERNSkQ0S2VHN3VPUVRRdkdmMHFrb1dEOUlLRklYcUpIbXJzVzJ6U1lYdzF5aXFkTG5vT1V4aWc?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxQc200aVhqdFJCQlJRVDdwMERia0ZCM3JoRWgzdDBMclE5RnJWSHU5eHowa1Bxc25rVzV1SVhSdm8wNVp3bE5qa3JyMzVPR29GX0tEbjVRb1pnUmdMazl5THd3azk1VlZJZ0lMNWtIODJtUTBKU0xaaF9WWnc0VnRTMTIzNnE1ckFUdE96d21IVWhDS25QSkNudjJMNHZkd3hrT0pqWXdFLW1ZaUJjLVEyb3o2NXhjYThBRzZES2xjQ2duemNfSUI0WQ?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNNzVNbW9MWnd2YV9qRU9pR2NTYzRxMTdzSVJ5Y0Nsc0VmNzVFSXVRYnNIYUVrT3NWa1hDSjZKXzh0TkxtMnlsTFV2VVY4UlZhYnk1aGx1NTE0SWJBRXRCTnNIMXJXUGVGWXRyOG9ZY2R5VTNlUTczVEtVZWFHY0JHUHlHSWRwM2E1SzN1dGtFdkVoRGN5Y2RJU1Q4OTJQS096cVg1T0VYMjR2OVpyV0J1U1kxcUJ0OXRRZEpObWlYMDdIcU5PVEHSAcsBQVVfeXFMUE9WdEFHRlVvQU9qX1VkYndfLUNmM0ViRnh2VzdpU0pCeGhGbmZacFpMT29mUk1sazBOeUc3dHdfc1NQNFlLLVdUX1V1MVVlb1pLY1BwM2FQUEF2OGx1UDgxWmJrenVCTGVrT2NBVXpaelBFbjVJVnk3MVpJT1FfMWJGZzluVFpoVnlxOU5sU3ZRSDktaXZpbVdfNEZfRlJvNTJSb1drTjNqSGVIQ2VkdnhTN2xDdFlLZXdvOUkxZmRXLV9PMkJ2Xy12cDg?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOU3g4a0pTeGFlLUk3c3JNcDRiaDE4OVJJdkNWUkNYSmZTWllIb2QxcGQ3RXBIQkZlSUktYWdVc1drVTZpUnRoVmJDa1QzT3hkaG5BQXFvaE1fR0d3aENVYmpvNTRDQS1hUVZQRGlHaS1mM19NUDFnYXpCZkZXUkxrXzNFc1dWYy1HcWRMWnhEZm56SmlM?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
