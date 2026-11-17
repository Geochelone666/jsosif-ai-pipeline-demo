# ISRG Intelligence Report

- ticker: **ISRG**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/ISRG/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ISRG/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:25:28.567862+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 16, 'rule': 3, 'ai': 12, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 16 unique headlines; 9 named publishers; 0 exact duplicates; 16 HTTPS source links; largest publisher share 31.25%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 437.7500 |
| Return 1D (%) | -1.3165 |
| Return 1W (%) | -4.9527 |
| Return 1M (%) | 2.5896 |
| Return YTD (%) | -22.7082 |
| Return 1Y (%) | -20.3381 |
| Annualized volatility (%) | 35.5498 |
| Beta vs SPY | 0.9068 |
| Max drawdown (%) | -43.9960 |
| Sharpe (rf=0) | -0.4507 |
| Downside deviation (rf=0, %) | 26.2631 |
| Sortino (rf=0) | -0.6101 |
| Historical VaR 95% (1D, %) | 3.2284 |
| Historical ES 95% (1D, %) | 5.1297 |
| Correlation vs SPY | 0.3512 |
| Tracking error vs SPY (%) | 33.3104 |
| P/E (trailing) | 52.93 |
| P/B | 9.49 |
| EV/EBITDA | 33.07 |
| Revenue growth (%) | 21.70 |
| Forward P/E (estimate) | 35.11 |
| Gross margin (%) | 66.64 |
| Operating margin (%) | 31.70 |
| Return on equity (%) | 17.93 |
| Free cash flow yield (%) | 2.26 |
| MA50 | 419.0146 |
| Close vs MA50 (%) | 4.4713 |
| MA200 | 429.0483 |
| Close vs MA200 (%) | 2.0281 |
| RSI (14, Wilder) | 49.4784 |
| MACD (12,26) | 7.0009 |
| MACD signal (9) | 10.3657 |
| MACD histogram | -3.3648 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ISRG': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 437.7500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.3165 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.9527 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.5896 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -22.7082 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -20.3381 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.5498 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.2631 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.6101 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2284 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1297 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3512 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.3104 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9068 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.9960 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.4507 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 35.1077 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.6420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.7020 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.9320 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.2636 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 52.9323 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 49.4784 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.3648 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.4713 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 2.0281 -> Slightly above the moving-average trend level.

## TAILWINDS

### Intuitive Surgical price target raised to $500 from $470 at BofA
- Summary: Intuitive Surgical price target raised to $500 from $470 at BofA
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQVHU5UEh1ckhOS3VzSVVZb0czZU1WdXpKa1Nkd2I1NEpFZC1zMkRMQnpESWZ5UUdzb0VkQU9RUVlsRTJkMl9adTIzTzBCbzkwclhnc2UwczAzaTQzaHBXNk85TGZWNF92eU5mY0V3UVhLX2xES1NpckZfTHA2R0szODRiV19xWlVjVGY4NlNmOXdxUXhJMU9Obk1fTnliOFpLWmJ2RUNmVG5QVGhJTFZHSkNn?oc=5>

### Is Intuitive Surgical (ISRG) a Solid Growth Stock? 3 Reasons to Think "Yes"
- Summary: Author argues ISRG is a solid growth stock, citing three supporting reasons.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPQnpLTmE0dklyYmp0MGJRU2hzQmQ2T2luWnppTmJFWl9rSWhXS3djTWNyS29RUTlpYXpXemF0SkdHUGZNOEp3ZXRiTnBlSHl3Nnp0Z01EcWhuekZ1OW0xX0hpdVpIS29PaHc5cG5VTDhLcHQ0d2RYU3ZYd3IzYnJfQ05ac3hlM0pudHY5QlZIU1haUHlYU0ZwWDBvSUk5eF9vckFn?oc=5>

### Brokers Suggest Investing in Intuitive Surgical (ISRG): Read This Before Placing a Bet
- Summary: Brokers recommend buying ISRG shares, highlighting potential upside.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxORTFKZHJ1S19MYjVoemwyQXpjWUY0aTkxcEMwVXRSU2RrVVdhNzJ0Rjd2TUtFd3BheDY4UWdqdnZSNE53azNXQ3Q3Q1pjc1d2SEt5dWNtVk1ERkt5Yi04WC1ONlpIbUIzeVgwNjlVcml3dE9mdUdZTXBIVlNEVi1WNVdyRWU4dXZ4SUFWenFOTS1fYl9KWHFxM0Jfb2FhMGhYcmpNU09BQ2JrOHhleGc?oc=5>

### Intuitive Surgical: Why I Remain Bullish Despite Cutting My Price Target (NASDAQ:ISRG)
- Summary: Author stays bullish on ISRG after lowering price target, citing fundamentals.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPazNWaGNyVnM5SXk4aVY5dWpVUy16Z0t6VU85MFhOa01WQVNWRmVPeDZXLTVNYkN1bHQzSmNtdTZFT2VMRFhiU2tfcFNlN3g1ZjZJdVpZc212YlVxa19sY0pnMWV3N1VCWlFqdHljTDZTXzk0LURZVXNITldONmFfSTJUemplYWJwNEZiQlVTeUFvc3FLcGdEVTRfUkJOUWI4OXlPMzVBS29BREhLc1NqQVpn?oc=5>

### Intuitive Surgical (ISRG) Stock Looks In Line With Cash Flow After A 45% Run
- Summary: Stock aligns with strong cash flow, indicating healthy financial performance.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxPLXU0OUM4LWFjWXZGN0hScU9GQkxULVJoT256bEZocFV0WjRpUGlwSnZlbDJDampJM256QVFKcnU4VGVJQ3hXM3lLZXFrYTJjX2o3OUlBbXBLYlV0dHdqV0ZsNFJ5OUhUZFo3SGJIY3VwU2tBbC1sYjg3WWhEVk1oQlY2aGdxVTQxUzB0dDJfVTFtM01PbTY3clZqVk1YM0t5MmZiRW42R29fY194Q2I5cFREMnFra2NTaXpLOUFxRXI0d1VKamFad0YzektQcmtXb0hlZkRn0gHbAUFVX3lxTE5VNTVxX08tUDh3SmNHdl9Ca2tpQ3RoM0g4dGtiMHZrdXkzeXZsZmFwOFE0UWtpY2Y1ZmxhMWJLU09yaWQzdnZxMG13WU9IYWNyY2FtWE9WdVpHVjMxYWxFUzZaUWM4UmRYYUdXYjRyVC1TZ3ZucmFzZEJkdDdqcmFKblJlWnRrSWNZYUdsUXIyU1BPclM5VmpnaUVES3FLZmFpR29ob0RSRHVhWWdvWjNFWDVNTXJUUGJlN1huaE9ILTMtckc3MHJrb2xqRVIxOUdvdWg4VkdpcjB6aw?oc=5>

### Intuitive Surgical (NASDAQ:ISRG): Strong Growth Meets a Constructive Technical Setup
- Summary: Positive growth and favorable technical indicators suggest bullish momentum.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNLVp3elQtUjJkXzRMY1FZbGNSeXFwQXdwZDRCdmJrX2RCUEFZblJpMWE5S3dpc2tzWnYtSG5RZm95VzhKa0MwS0JITnVBWGVhUm5GN0tia2c5aExETTVzOVdBeTZmeTdRb3RDX09ZNVdtVUdiTWE2eUl6U2t6RHkybld0VFRPUHp6cFRndmU4V044UGNudGNLQkR6OEtsRGVJNmdjQ1lkSTNDcEtkSGEyY3hPb2E1S2l0YVlNaU9rTDR0ZjNURlVfajZPZVc?oc=5>

### Intuitive Surgical (ISRG) Sees Rapid Single Port Robot Adoption
- Summary: Rapid adoption of Intuitive's single-port robot boosts product momentum and market share.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNNzJod3JaMUNFVk1IY3dSM1NNN3hrSlNBaDlWM3hQd3Rfa3hOcUVxaFVDZWZIa3VsM0x5U1djZzhvd0QyM2tPcFVmMmN2YTVkT3N2d0o1X1JqUW41NDAtX25KZFRPVzFRbjZua2FWbEFtcmNWM09yMG93ZVlqbmJPcXV6NlN4UGJOd2hYOFl3RVZHVW15RGtqNUk0VlVoOVBYWnVjb19uZFdRRDRDSmVnMlQ4VFNQbU1xNTN1d29Pdno4VEdBWWxJbU9mUkU3VUpJR2RHUGtR0gHbAUFVX3lxTE45cFdMT3h0NFozVHBJOUN2ZnFDZVB3eFl5eDdqLVY1UnRsOTlkcWdLVmFrX3VnTDZ2N2w2am14dTNwVkhyVWtkeXJDQm8xQW1TUjZfTC1jNldLSk1sdHYzTXM3bHM2M2F0STVjR1F4QmNOSFRkdUNxbkU0NFpNS1FNT3ZBckNKcVdGcWhJLTJ3emZ4c2pqS2pNOTliVnpvMU9WTkxTUkNsNVk3cXdGSUlJM3hSWG0zQ1hCenBTbnV0OFNOWTR0Y1M2UHAyRVhhVnI4UF9aS25RZm9mRQ?oc=5>

## HEADWINDS

### What Has The Market Missed In Intuitive Surgical Stock’s Drop?
- Summary: Article discusses factors behind ISRG stock decline, suggesting missed risks.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPcnNNYlRENUEzZlozRzA1dVNKUXFzZTJHNFU5UV84YmhDWGdDY0NTSjluaHMtMURpWldGVTFEcUJrcW80QWs0dzVDa0FlN2IxM3FUMHRfeWNSRm9WWnUyelBUbkZNTkFaMmJ2OFlORTJ3dnZucG1mTW1Pc2JIRDRuMWJYSHFsRms0QWRkY2RodEF4eEFLZnlyMzRCZTNEazZpVHFIMVV0WDdpQWpWV0J2LUJNYnEzS0x1X3loNzl3?oc=5>

### ISRG Agrees to $450M Settlement: What Does It Mean for Investors?
- Summary: ISRG settles for $450M, raising concerns for investors.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOR0NfWVNLdlR1cW5URWJBNHlzenR4ZHhQY2E2TU5qdHk2QTZNekJMakstNjFQM21FVFAzLU9zSmM2V0pTaGY4UHpQaUp5bUtDVTJWN09YV0xSdDRGZUNRY3k4OThTOVFmOGxqQjc5OUkxdnZCODA3RER0bGRWYkV5ZDV5bzhsODB1M1BfZFBLV1p4NFBQcnJQMQ?oc=5>

### Intuitive Surgical Inc Stock (ISRG) Moved Down by 3.35% on Nov 10: Drivers Behind the Movement
- Summary: Stock decline driven by negative market factors.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOUXdvN1pkV0dSakVkc2ZWekJ3WUVjUXJEZGV3TkpyWWl1dEViMW5GZl9EN1NJY2l4TVU3aEJoa00tWUtoMXRrSzBYY1MxQ3ZhOV9ZOWJPN2l5WDd0QUIwRGRiNm0xd0Uyd1l5S0FuUjBLbzF5RWd3bDNkWEh3RnVjWFB5WW9ZUENxbVRV?oc=5>

### Is Intuitive Surgical Stock Paying You Enough For The Swings?
- Summary: Questioning returns suggests potential investor concern.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxNbmc0eUNQSGJkem1MQ2FNaVY2WklEVEFzZEYzbGNCMnc1MHpza3lTOVBaOFYwMDhBRTNOUDQ5RlN6MGl3RzRlaGJKSk1ELUF5MEpsZm96d1lLNUZETlljb3ZqWWNtMXBoVVlCaEJGdUpSVXhkeV91bFp2bTJJQmRCS0otRm5VanBkdmV1RnhWMDNtMENYQ1ZsTmZkTHJubHFwVHh5TDFvTHAwcnBVZmVhUWFiQTc0bVpvQ2pMN2lB?oc=5>

## CATALYSTS

### Intuitive Surgical (ISRG) Stock Fair Value Edges Higher After Mixed Q3 Analyst Revisions
- Summary: Intuitive Surgical (ISRG) Stock Fair Value Edges Higher After Mixed Q3 Analyst Revisions
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPQW1hV1lMNFBYRmJWdW9OTDVTTDV6QktCT3hhMGFteTFYdGJ5dGxSci1TNk1pdkVBUUhuRlJJamNodjcya3o1NXh5aVZTUWU3b1NNekM5YWdyd2IxU00xZ3hRRXdWdG96YmRRZXhIWUF0aGZfR2FfNC0zR21JZ05KSzNhckdBQlBFcFctbDVRV0o5cUplWXpuMjhSaTNSVFlR?oc=5>

### Intuitive Surgical (ISRG) Just Grew Revenue 22%. Why Is the Stock Still Down This Year?
- Summary: Intuitive Surgical (ISRG) Just Grew Revenue 22%. Why Is the Stock Still Down This Year?
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOV1JDa3pWOXNYTDdmclZzOG0yMVlIUElneWlQU05HbzZKQWdTdHZrVlZaaVhtMFcwT1RoUjMzaVdQY2tYeThqXzEtNWxNZGxZNUFDbEhCOU5WeFptd3ltY2lmTTVBR3NnLXlnS2RwUFNpUkJPVXBTQ1d2Zk5jWFJfLVYxelNTcFV1ajA0RDh6cjhLbm5ISkRsLWxQN29xb3M?oc=5>

### How Investors Are Reacting To Intuitive Surgical (ISRG) Board Appointment
- Summary: Board appointment may influence investor sentiment and strategy.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNclo2dTVKQXo1ZTVJaVhZQjJnM25sT2Q2WlFrRzNEMmhfTkxhcnJWMTdmblRuQXFfbEpVd3k2MGh0SWtxQS1fTWF4WDY1cWZweFZMZ3EtRXozbGJUMjRtZTJNZEh0TjVQQ0FsZmgydUNmU1plX0ZsWHMxcXYydXhrS2FJWGZ6Y0c0bWdFNmVZTjFmUDlSSmN1UXZCdFAxZFA1Y05jV1IwdG1vSE80THFPRHFocHZwNWlNR19xem40dFBzcTBRSUVkUnRQNU1FRU1IdDhIbQ?oc=5>

### Can Intuitive Surgical (NASDAQ:ISRG) Keep Robotic Surgery Growing?
- Summary: Questioning future growth prospects for Intuitive's robotic surgery platform.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNOE5fYnBpbkxVWVF6Z2JOTmZIYVZTYXNfLUZUTHV6VklKRm1EZXJJNk43Nkhtamg3aXpxVFo3SHdiZVRsalVlLWpVUGdnRkRkV3lobDBBVzYzVzlBZjdEVmVfZTlKN05wSFhQZlpFTjVWTVlnN2xwXzZkWHZIdmw2T3Njd0RsSUlxVndleGtZZ2xHX0hjZWxRYUFQQks4WHVlODFRcVNNdGFNR3JC?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ISRG** | **52.93** | **9.49** | **33.07** | **21.70** | **151,743,283,200.00 USD** | **-20.34** |
| MDT | 25.28 | 2.62 | 14.58 | 13.70 | 131,597,705,216.00 USD | 10.87 |
| SYK | 33.09 | 5.04 | 17.37 | 7.60 | 118,288,310,272.00 USD | -13.27 |
| BSX | 18.43 | 2.47 | 13.45 | 1.40 | 63,327,485,952.00 USD | -57.45 |

Peers fetched as_of: 2026-11-16; ISRG reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 3,048,700,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 522,800,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1035267/000103526726000071/isrg-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMisgFBVV95cUxQVHU5UEh1ckhOS3VzSVVZb0czZU1WdXpKa1Nkd2I1NEpFZC1zMkRMQnpESWZ5UUdzb0VkQU9RUVlsRTJkMl9adTIzTzBCbzkwclhnc2UwczAzaTQzaHBXNk85TGZWNF92eU5mY0V3UVhLX2xES1NpckZfTHA2R0szODRiV19xWlVjVGY4NlNmOXdxUXhJMU9Obk1fTnliOFpLWmJ2RUNmVG5QVGhJTFZHSkNn?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPQnpLTmE0dklyYmp0MGJRU2hzQmQ2T2luWnppTmJFWl9rSWhXS3djTWNyS29RUTlpYXpXemF0SkdHUGZNOEp3ZXRiTnBlSHl3Nnp0Z01EcWhuekZ1OW0xX0hpdVpIS29PaHc5cG5VTDhLcHQ0d2RYU3ZYd3IzYnJfQ05ac3hlM0pudHY5QlZIU1haUHlYU0ZwWDBvSUk5eF9vckFn?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxORTFKZHJ1S19MYjVoemwyQXpjWUY0aTkxcEMwVXRSU2RrVVdhNzJ0Rjd2TUtFd3BheDY4UWdqdnZSNE53azNXQ3Q3Q1pjc1d2SEt5dWNtVk1ERkt5Yi04WC1ONlpIbUIzeVgwNjlVcml3dE9mdUdZTXBIVlNEVi1WNVdyRWU4dXZ4SUFWenFOTS1fYl9KWHFxM0Jfb2FhMGhYcmpNU09BQ2JrOHhleGc?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPazNWaGNyVnM5SXk4aVY5dWpVUy16Z0t6VU85MFhOa01WQVNWRmVPeDZXLTVNYkN1bHQzSmNtdTZFT2VMRFhiU2tfcFNlN3g1ZjZJdVpZc212YlVxa19sY0pnMWV3N1VCWlFqdHljTDZTXzk0LURZVXNITldONmFfSTJUemplYWJwNEZiQlVTeUFvc3FLcGdEVTRfUkJOUWI4OXlPMzVBS29BREhLc1NqQVpn?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxPLXU0OUM4LWFjWXZGN0hScU9GQkxULVJoT256bEZocFV0WjRpUGlwSnZlbDJDampJM256QVFKcnU4VGVJQ3hXM3lLZXFrYTJjX2o3OUlBbXBLYlV0dHdqV0ZsNFJ5OUhUZFo3SGJIY3VwU2tBbC1sYjg3WWhEVk1oQlY2aGdxVTQxUzB0dDJfVTFtM01PbTY3clZqVk1YM0t5MmZiRW42R29fY194Q2I5cFREMnFra2NTaXpLOUFxRXI0d1VKamFad0YzektQcmtXb0hlZkRn0gHbAUFVX3lxTE5VNTVxX08tUDh3SmNHdl9Ca2tpQ3RoM0g4dGtiMHZrdXkzeXZsZmFwOFE0UWtpY2Y1ZmxhMWJLU09yaWQzdnZxMG13WU9IYWNyY2FtWE9WdVpHVjMxYWxFUzZaUWM4UmRYYUdXYjRyVC1TZ3ZucmFzZEJkdDdqcmFKblJlWnRrSWNZYUdsUXIyU1BPclM5VmpnaUVES3FLZmFpR29ob0RSRHVhWWdvWjNFWDVNTXJUUGJlN1huaE9ILTMtckc3MHJrb2xqRVIxOUdvdWg4VkdpcjB6aw?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNLVp3elQtUjJkXzRMY1FZbGNSeXFwQXdwZDRCdmJrX2RCUEFZblJpMWE5S3dpc2tzWnYtSG5RZm95VzhKa0MwS0JITnVBWGVhUm5GN0tia2c5aExETTVzOVdBeTZmeTdRb3RDX09ZNVdtVUdiTWE2eUl6U2t6RHkybld0VFRPUHp6cFRndmU4V044UGNudGNLQkR6OEtsRGVJNmdjQ1lkSTNDcEtkSGEyY3hPb2E1S2l0YVlNaU9rTDR0ZjNURlVfajZPZVc?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNNzJod3JaMUNFVk1IY3dSM1NNN3hrSlNBaDlWM3hQd3Rfa3hOcUVxaFVDZWZIa3VsM0x5U1djZzhvd0QyM2tPcFVmMmN2YTVkT3N2d0o1X1JqUW41NDAtX25KZFRPVzFRbjZua2FWbEFtcmNWM09yMG93ZVlqbmJPcXV6NlN4UGJOd2hYOFl3RVZHVW15RGtqNUk0VlVoOVBYWnVjb19uZFdRRDRDSmVnMlQ4VFNQbU1xNTN1d29Pdno4VEdBWWxJbU9mUkU3VUpJR2RHUGtR0gHbAUFVX3lxTE45cFdMT3h0NFozVHBJOUN2ZnFDZVB3eFl5eDdqLVY1UnRsOTlkcWdLVmFrX3VnTDZ2N2w2am14dTNwVkhyVWtkeXJDQm8xQW1TUjZfTC1jNldLSk1sdHYzTXM3bHM2M2F0STVjR1F4QmNOSFRkdUNxbkU0NFpNS1FNT3ZBckNKcVdGcWhJLTJ3emZ4c2pqS2pNOTliVnpvMU9WTkxTUkNsNVk3cXdGSUlJM3hSWG0zQ1hCenBTbnV0OFNOWTR0Y1M2UHAyRVhhVnI4UF9aS25RZm9mRQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPcnNNYlRENUEzZlozRzA1dVNKUXFzZTJHNFU5UV84YmhDWGdDY0NTSjluaHMtMURpWldGVTFEcUJrcW80QWs0dzVDa0FlN2IxM3FUMHRfeWNSRm9WWnUyelBUbkZNTkFaMmJ2OFlORTJ3dnZucG1mTW1Pc2JIRDRuMWJYSHFsRms0QWRkY2RodEF4eEFLZnlyMzRCZTNEazZpVHFIMVV0WDdpQWpWV0J2LUJNYnEzS0x1X3loNzl3?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOR0NfWVNLdlR1cW5URWJBNHlzenR4ZHhQY2E2TU5qdHk2QTZNekJMakstNjFQM21FVFAzLU9zSmM2V0pTaGY4UHpQaUp5bUtDVTJWN09YV0xSdDRGZUNRY3k4OThTOVFmOGxqQjc5OUkxdnZCODA3RER0bGRWYkV5ZDV5bzhsODB1M1BfZFBLV1p4NFBQcnJQMQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOUXdvN1pkV0dSakVkc2ZWekJ3WUVjUXJEZGV3TkpyWWl1dEViMW5GZl9EN1NJY2l4TVU3aEJoa00tWUtoMXRrSzBYY1MxQ3ZhOV9ZOWJPN2l5WDd0QUIwRGRiNm0xd0Uyd1l5S0FuUjBLbzF5RWd3bDNkWEh3RnVjWFB5WW9ZUENxbVRV?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxNbmc0eUNQSGJkem1MQ2FNaVY2WklEVEFzZEYzbGNCMnc1MHpza3lTOVBaOFYwMDhBRTNOUDQ5RlN6MGl3RzRlaGJKSk1ELUF5MEpsZm96d1lLNUZETlljb3ZqWWNtMXBoVVlCaEJGdUpSVXhkeV91bFp2bTJJQmRCS0otRm5VanBkdmV1RnhWMDNtMENYQ1ZsTmZkTHJubHFwVHh5TDFvTHAwcnBVZmVhUWFiQTc0bVpvQ2pMN2lB?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPQW1hV1lMNFBYRmJWdW9OTDVTTDV6QktCT3hhMGFteTFYdGJ5dGxSci1TNk1pdkVBUUhuRlJJamNodjcya3o1NXh5aVZTUWU3b1NNekM5YWdyd2IxU00xZ3hRRXdWdG96YmRRZXhIWUF0aGZfR2FfNC0zR21JZ05KSzNhckdBQlBFcFctbDVRV0o5cUplWXpuMjhSaTNSVFlR?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOV1JDa3pWOXNYTDdmclZzOG0yMVlIUElneWlQU05HbzZKQWdTdHZrVlZaaVhtMFcwT1RoUjMzaVdQY2tYeThqXzEtNWxNZGxZNUFDbEhCOU5WeFptd3ltY2lmTTVBR3NnLXlnS2RwUFNpUkJPVXBTQ1d2Zk5jWFJfLVYxelNTcFV1ajA0RDh6cjhLbm5ISkRsLWxQN29xb3M?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNclo2dTVKQXo1ZTVJaVhZQjJnM25sT2Q2WlFrRzNEMmhfTkxhcnJWMTdmblRuQXFfbEpVd3k2MGh0SWtxQS1fTWF4WDY1cWZweFZMZ3EtRXozbGJUMjRtZTJNZEh0TjVQQ0FsZmgydUNmU1plX0ZsWHMxcXYydXhrS2FJWGZ6Y0c0bWdFNmVZTjFmUDlSSmN1UXZCdFAxZFA1Y05jV1IwdG1vSE80THFPRHFocHZwNWlNR19xem40dFBzcTBRSUVkUnRQNU1FRU1IdDhIbQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNOE5fYnBpbkxVWVF6Z2JOTmZIYVZTYXNfLUZUTHV6VklKRm1EZXJJNk43Nkhtamg3aXpxVFo3SHdiZVRsalVlLWpVUGdnRkRkV3lobDBBVzYzVzlBZjdEVmVfZTlKN05wSFhQZlpFTjVWTVlnN2xwXzZkWHZIdmw2T3Njd0RsSUlxVndleGtZZ2xHX0hjZWxRYUFQQks4WHVlODFRcVNNdGFNR3JC?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
