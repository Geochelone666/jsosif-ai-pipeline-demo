# CAT Intelligence Report

- ticker: **CAT**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/CAT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CAT/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:35:21.732722+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 10, 'ai': 12, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/CAT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'negative_sentiment_in_tailwinds': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 10 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 56.0%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 613.6200 |
| Return 1D (%) | -1.4661 |
| Return 1W (%) | -11.3432 |
| Return 1M (%) | -27.2457 |
| Return YTD (%) | 8.0242 |
| Return 1Y (%) | 7.2027 |
| Annualized volatility (%) | 40.3154 |
| Beta vs SPY | 1.9029 |
| Max drawdown (%) | -42.1335 |
| Sharpe (rf=0) | 0.4041 |
| Downside deviation (rf=0, %) | 28.4114 |
| Sortino (rf=0) | 0.5734 |
| Historical VaR 95% (1D, %) | 4.0483 |
| Historical ES 95% (1D, %) | 5.5327 |
| Correlation vs SPY | 0.6052 |
| Tracking error vs SPY (%) | 34.1181 |
| P/E (trailing) | 24.08 |
| P/B | 13.11 |
| EV/EBITDA | 18.56 |
| Revenue growth (%) | 17.30 |
| Forward P/E (estimate) | 19.04 |
| Gross margin (%) | 30.21 |
| Operating margin (%) | 20.51 |
| Return on equity (%) | 56.14 |
| Free cash flow yield (%) | 1.46 |
| MA50 | 777.3592 |
| Close vs MA50 (%) | -21.0635 |
| MA200 | 806.4916 |
| Close vs MA200 (%) | -23.9149 |
| RSI (14, Wilder) | 23.0440 |
| MACD (12,26) | -42.6878 |
| MACD signal (9) | -31.6928 |
| MACD histogram | -10.9950 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CAT': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 613.6200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.4661 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -11.3432 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -27.2457 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 8.0242 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 7.2027 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 40.3154 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 28.4114 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5734 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.0483 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.5327 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6052 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.1181 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.9029 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -42.1335 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4041 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 19.0439 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.2110 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 20.5060 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 56.1350 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.4629 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 24.0824 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 23.0440 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -10.9950 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -21.0635 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -23.9149 -> Clearly below the moving-average trend level.

## TAILWINDS

### CAT Q3 Earnings Beat Estimates on Higher Volume and Pricing
- Summary: CAT Q3 Earnings Beat Estimates on Higher Volume and Pricing
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOaU03VHJIZDRSSDE1T2NqZzl3QnF3WGFqc0ZLNzJsMzYyQVJ5aHZBOGR0SzN6ODVhQTlFSi1ZRV95U19HeGdQdjE4X1czT3dWY2diQ3pWV3JaZWFpYkdqam84b0t4TXNMTGkxWlVaeUtFRTk4eVY3Zl9kaWxaQzFBVE90b3o0a3hMTXdJSi13akdxd1dIcVVGbnZZRQ?oc=5>

### Caterpillar (CAT) Q3 Earnings and Revenues Beat Estimates
- Summary: Caterpillar (CAT) Q3 Earnings and Revenues Beat Estimates
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQRnRUZTFxQVcyNTNWM3V0MURNUjIxN0N2b2NnbDZGUU00cW5Cbm1WMWlOVE5DbWxmb2xvb1VSSUV6VTlVSGxseVhzU2NrS0ZRVDYxODBDcWJybTJoSlAyMFc2QUlDTjJFaWV5STNlWEZYOUw0MW1pTDdoLTJ0bF9YSkRJYUpPZTFETjZIT2VLT1lFcUg3a2RaQkVRSjFLTWwzUUxV?oc=5>

### Why is Caterpillar stock sliding today?
- Summary: Stock price decline noted, no company action cited.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNSU95Smtjel92QjROdWFpM0pUTzFaUVhWRExBR1VmaDVlUF9nenFxNnc0RGpUbnF2bzhrQzhOZjNuRzh5M1NsNEZrd1pJRXRkYjBYeWJHWkdMOXA5TEJlVDBEeDNUbGM2Rm9kOU90Z2FKRTNaSV9zRV9MbU9pNC1Gd1JTeUFka3ViRENvVzNXSXRwYjc1MlpVSEhhT2tPUUJJaUE?oc=5>

### Caterpillar Crashed By 25% Over 6 Months But This Global Banking Giant Says 85% Gains Will Come
- Summary: Analyst predicts 85% upside after 25% decline.
- Date: 2026-11-02 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNZkROdDhoUDNnTnpVcjhLWTdMWk91dk94d3o3T1JvbkdzeWphbjNLWTBpZU9GVkwtcTF2TFNTV0dvVnJRU3BVQ3BaNFFCNG56c2s3QUlZWnJKTHF6UDluV3VaaG1iblhCT1ZXVlV1UVZrLWVyeEw5aFlXRGxJZUVGUXVYbnQ2S2VKNmtaVUZCMHNWMHotXzM5eTBn?oc=5>

### Caterpillar Fell Nearly 25% Over 3 Months But These Two Wall Street Firms Say It’s Going to Appreciate by Nearly 80%
- Summary: Wall Street firms forecast 80% upside following 25% drop.
- Date: 2026-10-30 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPbFRuM1NiQ1I0YUhjTll1Yll2TFMtaTdINXVFOVp1WTNTSFNUZmhDTmY5THl2S0s1cGNYdDM3WlFfc05tRGxwNzcxendmZEZRM21OeHdtckdXajhzSHdUVzlnNkFqMHF1NU9saU5sTzYweE0zRUlpcVJTV19Sb2p5VnA4TlI5cHhPeWZnS1k3MDh1dkxQajZSNWhnU0w?oc=5>

## HEADWINDS

### Caterpillar (CAT) Stock Slides As Q3 Results Leave Tariff Questions
- Summary: Caterpillar (CAT) Stock Slides As Q3 Results Leave Tariff Questions
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOMlBwYlpXM2FiMVFzcHJtem9USGJuVU04NGNROUJWM0t6SmkzcFdPUllPSElXYjRuaDAyY0hGcDdkN3Z3RUUtb1VOeWJ3c183X3VLNU5zYlhKcDllZVVXcTE3aVdrekNHVjBrYUpUMlpQWl9uMElVbDFGSTdfdlNocERHZzhVMHZRVklvQ3hHYl9ZM19ZNWl1Nmt6dmg?oc=5>

### Caterpillar’s stock is sinking. Here’s what that means for the Dow.
- Summary: Caterpillar’s stock is sinking. Here’s what that means for the Dow.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNcTFJRWVHOUlkMlFXbFRrZ0xsSEZ1X2V1THprS3B5M2x3dUdnSEltSG5wZE93RDdCM2M4SjBlcDl4SFk5aG1FVjBNN3VFUjd5MG0tbEFIZWtIYzlscUVPaklaZGhIOW9saWYwSzFpNWkyd3o0UDB4LW9Pandpakt3VmlyLXljci1RS1lrcDJFWmliMmI0dWIwNEM4aGNfbHE5b1c1X3ZGRzNOOXI5NmZVNmgzSlVFY3ZJazZXaDB3MHhaUQ?oc=5>

### Caterpillar stock sinks after earnings: here's the case for buying
- Summary: Caterpillar stock sinks after earnings: here's the case for buying
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOZGlQZHBxOU5KU2lhZDZSbTZld29ZU2dfNjJQWnZMWnQ1cEoxTVZrQi1PMGZBUVdud2ZkdXdDYVRqNjdMODctZ1R0YjBHaGk4ZlA4bHZnbTV3UUVIdjdHbDk3QWxsWkdOdlIwWXlwbDVWb3d2d1o1RUtlTHZWVy1FTmVHUGtIQ2ktNmt0OUN2TVIwTEFOS29jNURoaTVXNWFOVjBvVXllQ245MmhtaUk2aEFNRllabE1HUzQ3RDJUQQ?oc=5>

### Caterpillar Revenue Miss, Outlook Dig Hole For Dow Jones Industrial Average
- Summary: Revenue miss signals weaker performance, negatively impacting market outlook.
- Date: 2026-10-29 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNRk54ajQ4MHcydlBCcGgtb21UekZtYnFXdVJGVF91d1ZwSjJqYUsxaXlZUWhoMFJaekV5QjlvU2tlTThoS0w3aUpIRzJqVkRoeDg2VUQzaGRjNmM3dnpzQUZVUE81czY2VUxseEVwZU5KQVJBbURuY3RRUDY3N2ZNaUpsY3kzMGFwcjRlaDBaRTRXOTdXTG9DYk93?oc=5>

## CATALYSTS

### Caterpillar, the Dow's best stock of 2026, is unraveling — and an earnings beat couldn't stop it
- Summary: Caterpillar, the Dow's best stock of 2026, is unraveling — and an earnings beat couldn't stop it
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxPQk5icEllSDRCZkxZWk9JRDNoLWtacDBFWVh6QjZxcUpIa1VIbXBxa3pSbV9lc2JzejN3aEQ3THloSWp2TzQzeGJZcDAtZFU4WXlQWjhrNS1OVFU2ZkZBT0QyMG5JRHVaTjdJbmxoakpFWUNqbGNKRkxPbEMxUVF6LXgyelNZVlN4YUJHTUd3cTVSSVVjVE9ZTkpPSlNCdkNYX1VjSkdSenNxYmtSekx4eFVqU3Z5QU9SekNDUmpSZXdWelFOektIQlljclZWUlhOdmpkajJpRkFhOUh2TWVBc0ln?oc=5>

### Caterpillar's 10.80% earnings gap down is biggest since 2002
- Summary: Caterpillar's 10.80% earnings gap down is biggest since 2002
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQXzEzSEZPTDhkTWdUMEpQcmNycEJ3NU1GN0g1bmNRcVVjUFd4M3lZMnRUNmN5UmtWUDhYMDJIbUtzQU5Ec0g3NDhmZjl5SVVHeGxnLXJZa1lkc0JqV0lITzdtU1NLT29IN1NnY1RUQ1ZseHFjRlREX3F5eVRqYUJPX2JMNURlMzVjTnlmUF91QQ?oc=5>

### Caterpillar Inc. Acquires Fabick Cat Dealership
- Summary: Caterpillar Inc. Acquires Fabick Cat Dealership
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNdWhHeHNNemRFWjlvaERmMFhnVDNDanZvZGdlU282QzRoSkJvLVJqakQ1XzNBYnQyR0ozdXhYRlZVVjY4c2JaUGlMYWZRMmNFazZfUEdZQU84WWVKRzlndjhDbkJuZFNuakpvQjZQZ2NXTHpZb3o2b2Q3cVlpZzczcW5OT1RMWEt6YnZKNGVDejlIODNSVFd0ZDBJR3ptQThTV0E?oc=5>

### Caterpillar earnings: what to look for from CAT
- Summary: Caterpillar earnings: what to look for from CAT
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPemNZNTRhaF82ZzBVWlItSDA2VnhjUVdIblNFa3BCVGZlbVR0QUhMZzlFN21YaGdNNUY1WVRrUE9uSF9iYVN1Z2tVMzBLV1J5a0tjci0zNmhvb19fd0p3LU1Neno2XzlSWVhaTUFtbGE1bWxUbk9fN1hBeGJYZnJlZ2NtUWZvdlY2ckRzRm9SRWd6UEFqS1FQY0xn?oc=5>

### Caterpillar (CAT) Q3 Earnings: How Key Metrics Compare to Wall Street Estimates
- Summary: Caterpillar (CAT) Q3 Earnings: How Key Metrics Compare to Wall Street Estimates
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNTlFvcnJ2OFNOdGFRcGw5SG1IZVIycHJMd2hxMkFVZUQtcHJCeW5sYmxXNEtCNVN2b3habXFlbGVSUXdkZFZYOUJLLVN1bk0zWUZTeWZsRUo4MU5zeFh2UFJwNUxTOEtFMlZrY3pkZFliTGh5eS1QR3VFWmdHa3BPWUJ1NXEzLUN5YzFGZFpoSUhMelhxU2V6Z3gxY3E?oc=5>

### Caterpillar (CAT) Stock May Be 20% Undervalued Following Backlog Questions
- Summary: Analysis suggests potential undervaluation due to backlog concerns.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNamg4bGJCNnJ2bkNBa0JFTGZfZFVrU0JsbEN0RE5vUXBQcGZOYU1lV1I2TzBkTDF1VDhWM2lOTkRfb0xNY21mT0FaSHFuWEpqTTBtM3JCbHRaMmJHZ0ZoWGlLVjViS0VTTWJvc1AyS3NkLUxibHBQMUVOaF9kUlgzWDVvOFllMWVJT1RSb003QXRrWUxUaWRPSg?oc=5>

### Dear Caterpillar Stock Fans, Mark Your Calendars for October 29
- Summary: Upcoming event on October 29, likely earnings or guidance.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQc1ZHR1lneTJYUC1xZkdaOHdKMVdIT3gzNlctZEliZHJmWGh2bVJ0UVlQbW41d3M4NThYRjNOV0V2VEFIal90SndCT3dZZExJUjdLS1RxX2tMQ3V3bE9MZHdOQVRBSjVpUVJCR1JiSm5ZY3FoMXF5OV9sV3lOZ1JvSmsyX0Q4VjJ6dzJLNW4tdDF2UkR3aVNvUGtvVDAtVUxXbFNuZldubThVUQ?oc=5>

### Caterpillar: Q3 Earnings Snapshot
- Summary: Snapshot of Caterpillar’s Q3 earnings results.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQUnlROWdTSTFOYmlFelh1TUtXaGg1YnI2dF9ta2RwQV83REcwQjZOMU5PMlhjM1dRcGg2RERKMWc4YzhURU9hTGtLOFpvajdodlJIVUJjdEVrc2tsbVZ1TkZNVm44cml4SmJSaklxb21fa1RKQzR2MFcyMEFJV19zVWgzTWJvbUtPOGFtRFJicHdJY3Nvd25UYmdpSDF5UQ?oc=5>

### What Could Caterpillar (CAT) Gain From This Dealer Acquisition?
- Summary: Potential dealer acquisition could boost CAT's market reach.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOMjZvcW9FcFFlNFJTUXVNVEswUjUzNmZCYVlCVlNBUThjLUVXOFR5RHpMQm5jLWZmdF9BQnJmdU5DeWhaRkYzQTJxU3VCNEozaExWRGFQblJUTXJiNTU3ZEFNTHdncjRNQ3ZMMmtIckxkd0NmUGxOUlBFUDVpSW5RVlpqZHpiT2hpMTZMV09Rd2NyRC1YMlIzRUNEMkdxcFE?oc=5>

### Caterpillar Inc. stock underperforms Monday when compared to competitors
- Summary: Caterpillar shares fell, lagging competitors on Monday.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxPdldraWlzY3JlMUd1MlpWVmFTNVdRZDc1NlQyTGVNX2N1dzhkQVF1cFBHWjEtY2hKenltZ2NiQzBhNEJ1Yi1XX2xCZkx1amY3Nm9adDBLbGJVYXZzamhNVC1LdElnbml5Sm9xZ2p4TUttWmtDNW9IUmREX01QTFVzTFJZOGhRd2FsVVZVYlNnQm5zYXJqYzM4TkRyN0VQYzcwdGhQYmRmWjhqbmdDWnJMR2J1Tzg2eDJjbk94c2w0a1JyTWduNWZ3N2NYYW1QMTQ2SGZlUERlcjZzUGxraE0za2pTcw?oc=5>

### Caterpillar Stocks Move Lower With Target Cut Putting Its Margin Premium on Trial
- Summary: Caterpillar shares dropped after a target cut, testing margin premium.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPQ2tBSV9ER1FJOG42QXE3U25MT1lDMFQxQVpPSklsODFnejNESFFUenpBNXJRZmJkODF6Sl9RTHdhWk02cUNvbDJaNUpVS1h5YV84S3ZCRU1wdjk2YjVJelJGaHpUQTFQVG9Zem4xcE1SQ0JFUkE4Q29tLVhscjVnSE04dFRvOFQ2bDlrY3hlMk9FOXlwQlpWR0c0a3F0T3UzY3dkSEczdFNoTHJoS3FXYm5OOTNQTGVBWGJ3Zg?oc=5>

## RISKS

### Why Caterpillar (CAT) shares are falling today
- Summary: Short‑term share price decline indicates market uncertainty and potential downside risk.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPMEVrQWc4M293b0pxWUxDYVRtb05YOHAyWFZqcDZCOGd5R3hzVGZuRjBPYmFndDBYenFFc0N3bl9URVlPYVdnMTdxR3A2YzJhTVJBckFyd3RIVEY1SFNsUDdyaVdZTTB4bjdtMFdVYnJjcGJCSU44dXV3QkJkUWRwYUdsR2t4dzhDZFk5T2NBUTdMT3dBeGtpSW5ESHlGR1V5?oc=5>

### Caterpillar Stock Tumbles Despite Q3 Earnings Beat As Revenue Falls Short Of Estimates
- Summary: Q3 earnings beat but revenue miss signals weaker growth, raising concerns about future performance.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOQlhocGZIRndSYzQ1dTJlZUYzVmpZdVRXYlF6QzZnc095NU5DNkY1WWJpMlkxZUx6dkM3U1lhYWIzSTBPTHNnUThaTTZKRGJ0S0g5QU9IYkF2Z2kwa3FvdG1HUnA1YlZHdzFPZjZXODVFQWFfbFkxaHFRVDZQX2xpbEFmRkFkYWZ4NGd3UnJodDhNZzVUUkxBdDJVelFUTDRZ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CAT** | **24.08** | **13.11** | **18.56** | **17.30** | **282,065,698,816.00 USD** | **7.20** |
| DE | 37.11 | 6.43 | 27.64 | 4.90 | 180,001,914,880.00 USD | 46.27 |
| CNH | 47.24 | 1.88 | 37.58 | 2.00 | 18,992,355,328.00 USD | 13.67 |
| CMI | 25.58 | 5.36 | 14.81 | 9.40 | 68,914,839,552.00 USD | 16.05 |

Peers fetched as_of: 2026-11-02; CAT reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 20,543,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 1,141,000,000.00 USD; period 2011-07-01/2011-09-30; fiscal year/reporting period 2011/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/18230/000001823026000046/cat-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxOaU03VHJIZDRSSDE1T2NqZzl3QnF3WGFqc0ZLNzJsMzYyQVJ5aHZBOGR0SzN6ODVhQTlFSi1ZRV95U19HeGdQdjE4X1czT3dWY2diQ3pWV3JaZWFpYkdqam84b0t4TXNMTGkxWlVaeUtFRTk4eVY3Zl9kaWxaQzFBVE90b3o0a3hMTXdJSi13akdxd1dIcVVGbnZZRQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQRnRUZTFxQVcyNTNWM3V0MURNUjIxN0N2b2NnbDZGUU00cW5Cbm1WMWlOVE5DbWxmb2xvb1VSSUV6VTlVSGxseVhzU2NrS0ZRVDYxODBDcWJybTJoSlAyMFc2QUlDTjJFaWV5STNlWEZYOUw0MW1pTDdoLTJ0bF9YSkRJYUpPZTFETjZIT2VLT1lFcUg3a2RaQkVRSjFLTWwzUUxV?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNSU95Smtjel92QjROdWFpM0pUTzFaUVhWRExBR1VmaDVlUF9nenFxNnc0RGpUbnF2bzhrQzhOZjNuRzh5M1NsNEZrd1pJRXRkYjBYeWJHWkdMOXA5TEJlVDBEeDNUbGM2Rm9kOU90Z2FKRTNaSV9zRV9MbU9pNC1Gd1JTeUFka3ViRENvVzNXSXRwYjc1MlpVSEhhT2tPUUJJaUE?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNZkROdDhoUDNnTnpVcjhLWTdMWk91dk94d3o3T1JvbkdzeWphbjNLWTBpZU9GVkwtcTF2TFNTV0dvVnJRU3BVQ3BaNFFCNG56c2s3QUlZWnJKTHF6UDluV3VaaG1iblhCT1ZXVlV1UVZrLWVyeEw5aFlXRGxJZUVGUXVYbnQ2S2VKNmtaVUZCMHNWMHotXzM5eTBn?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPbFRuM1NiQ1I0YUhjTll1Yll2TFMtaTdINXVFOVp1WTNTSFNUZmhDTmY5THl2S0s1cGNYdDM3WlFfc05tRGxwNzcxendmZEZRM21OeHdtckdXajhzSHdUVzlnNkFqMHF1NU9saU5sTzYweE0zRUlpcVJTV19Sb2p5VnA4TlI5cHhPeWZnS1k3MDh1dkxQajZSNWhnU0w?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOMlBwYlpXM2FiMVFzcHJtem9USGJuVU04NGNROUJWM0t6SmkzcFdPUllPSElXYjRuaDAyY0hGcDdkN3Z3RUUtb1VOeWJ3c183X3VLNU5zYlhKcDllZVVXcTE3aVdrekNHVjBrYUpUMlpQWl9uMElVbDFGSTdfdlNocERHZzhVMHZRVklvQ3hHYl9ZM19ZNWl1Nmt6dmg?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNcTFJRWVHOUlkMlFXbFRrZ0xsSEZ1X2V1THprS3B5M2x3dUdnSEltSG5wZE93RDdCM2M4SjBlcDl4SFk5aG1FVjBNN3VFUjd5MG0tbEFIZWtIYzlscUVPaklaZGhIOW9saWYwSzFpNWkyd3o0UDB4LW9Pandpakt3VmlyLXljci1RS1lrcDJFWmliMmI0dWIwNEM4aGNfbHE5b1c1X3ZGRzNOOXI5NmZVNmgzSlVFY3ZJazZXaDB3MHhaUQ?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOZGlQZHBxOU5KU2lhZDZSbTZld29ZU2dfNjJQWnZMWnQ1cEoxTVZrQi1PMGZBUVdud2ZkdXdDYVRqNjdMODctZ1R0YjBHaGk4ZlA4bHZnbTV3UUVIdjdHbDk3QWxsWkdOdlIwWXlwbDVWb3d2d1o1RUtlTHZWVy1FTmVHUGtIQ2ktNmt0OUN2TVIwTEFOS29jNURoaTVXNWFOVjBvVXllQ245MmhtaUk2aEFNRllabE1HUzQ3RDJUQQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNRk54ajQ4MHcydlBCcGgtb21UekZtYnFXdVJGVF91d1ZwSjJqYUsxaXlZUWhoMFJaekV5QjlvU2tlTThoS0w3aUpIRzJqVkRoeDg2VUQzaGRjNmM3dnpzQUZVUE81czY2VUxseEVwZU5KQVJBbURuY3RRUDY3N2ZNaUpsY3kzMGFwcjRlaDBaRTRXOTdXTG9DYk93?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxPQk5icEllSDRCZkxZWk9JRDNoLWtacDBFWVh6QjZxcUpIa1VIbXBxa3pSbV9lc2JzejN3aEQ3THloSWp2TzQzeGJZcDAtZFU4WXlQWjhrNS1OVFU2ZkZBT0QyMG5JRHVaTjdJbmxoakpFWUNqbGNKRkxPbEMxUVF6LXgyelNZVlN4YUJHTUd3cTVSSVVjVE9ZTkpPSlNCdkNYX1VjSkdSenNxYmtSekx4eFVqU3Z5QU9SekNDUmpSZXdWelFOektIQlljclZWUlhOdmpkajJpRkFhOUh2TWVBc0ln?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQXzEzSEZPTDhkTWdUMEpQcmNycEJ3NU1GN0g1bmNRcVVjUFd4M3lZMnRUNmN5UmtWUDhYMDJIbUtzQU5Ec0g3NDhmZjl5SVVHeGxnLXJZa1lkc0JqV0lITzdtU1NLT29IN1NnY1RUQ1ZseHFjRlREX3F5eVRqYUJPX2JMNURlMzVjTnlmUF91QQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNdWhHeHNNemRFWjlvaERmMFhnVDNDanZvZGdlU282QzRoSkJvLVJqakQ1XzNBYnQyR0ozdXhYRlZVVjY4c2JaUGlMYWZRMmNFazZfUEdZQU84WWVKRzlndjhDbkJuZFNuakpvQjZQZ2NXTHpZb3o2b2Q3cVlpZzczcW5OT1RMWEt6YnZKNGVDejlIODNSVFd0ZDBJR3ptQThTV0E?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPemNZNTRhaF82ZzBVWlItSDA2VnhjUVdIblNFa3BCVGZlbVR0QUhMZzlFN21YaGdNNUY1WVRrUE9uSF9iYVN1Z2tVMzBLV1J5a0tjci0zNmhvb19fd0p3LU1Neno2XzlSWVhaTUFtbGE1bWxUbk9fN1hBeGJYZnJlZ2NtUWZvdlY2ckRzRm9SRWd6UEFqS1FQY0xn?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNTlFvcnJ2OFNOdGFRcGw5SG1IZVIycHJMd2hxMkFVZUQtcHJCeW5sYmxXNEtCNVN2b3habXFlbGVSUXdkZFZYOUJLLVN1bk0zWUZTeWZsRUo4MU5zeFh2UFJwNUxTOEtFMlZrY3pkZFliTGh5eS1QR3VFWmdHa3BPWUJ1NXEzLUN5YzFGZFpoSUhMelhxU2V6Z3gxY3E?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNamg4bGJCNnJ2bkNBa0JFTGZfZFVrU0JsbEN0RE5vUXBQcGZOYU1lV1I2TzBkTDF1VDhWM2lOTkRfb0xNY21mT0FaSHFuWEpqTTBtM3JCbHRaMmJHZ0ZoWGlLVjViS0VTTWJvc1AyS3NkLUxibHBQMUVOaF9kUlgzWDVvOFllMWVJT1RSb003QXRrWUxUaWRPSg?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQc1ZHR1lneTJYUC1xZkdaOHdKMVdIT3gzNlctZEliZHJmWGh2bVJ0UVlQbW41d3M4NThYRjNOV0V2VEFIal90SndCT3dZZExJUjdLS1RxX2tMQ3V3bE9MZHdOQVRBSjVpUVJCR1JiSm5ZY3FoMXF5OV9sV3lOZ1JvSmsyX0Q4VjJ6dzJLNW4tdDF2UkR3aVNvUGtvVDAtVUxXbFNuZldubThVUQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQUnlROWdTSTFOYmlFelh1TUtXaGg1YnI2dF9ta2RwQV83REcwQjZOMU5PMlhjM1dRcGg2RERKMWc4YzhURU9hTGtLOFpvajdodlJIVUJjdEVrc2tsbVZ1TkZNVm44cml4SmJSaklxb21fa1RKQzR2MFcyMEFJV19zVWgzTWJvbUtPOGFtRFJicHdJY3Nvd25UYmdpSDF5UQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOMjZvcW9FcFFlNFJTUXVNVEswUjUzNmZCYVlCVlNBUThjLUVXOFR5RHpMQm5jLWZmdF9BQnJmdU5DeWhaRkYzQTJxU3VCNEozaExWRGFQblJUTXJiNTU3ZEFNTHdncjRNQ3ZMMmtIckxkd0NmUGxOUlBFUDVpSW5RVlpqZHpiT2hpMTZMV09Rd2NyRC1YMlIzRUNEMkdxcFE?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxPdldraWlzY3JlMUd1MlpWVmFTNVdRZDc1NlQyTGVNX2N1dzhkQVF1cFBHWjEtY2hKenltZ2NiQzBhNEJ1Yi1XX2xCZkx1amY3Nm9adDBLbGJVYXZzamhNVC1LdElnbml5Sm9xZ2p4TUttWmtDNW9IUmREX01QTFVzTFJZOGhRd2FsVVZVYlNnQm5zYXJqYzM4TkRyN0VQYzcwdGhQYmRmWjhqbmdDWnJMR2J1Tzg2eDJjbk94c2w0a1JyTWduNWZ3N2NYYW1QMTQ2SGZlUERlcjZzUGxraE0za2pTcw?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPQ2tBSV9ER1FJOG42QXE3U25MT1lDMFQxQVpPSklsODFnejNESFFUenpBNXJRZmJkODF6Sl9RTHdhWk02cUNvbDJaNUpVS1h5YV84S3ZCRU1wdjk2YjVJelJGaHpUQTFQVG9Zem4xcE1SQ0JFUkE4Q29tLVhscjVnSE04dFRvOFQ2bDlrY3hlMk9FOXlwQlpWR0c0a3F0T3UzY3dkSEczdFNoTHJoS3FXYm5OOTNQTGVBWGJ3Zg?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPMEVrQWc4M293b0pxWUxDYVRtb05YOHAyWFZqcDZCOGd5R3hzVGZuRjBPYmFndDBYenFFc0N3bl9URVlPYVdnMTdxR3A2YzJhTVJBckFyd3RIVEY1SFNsUDdyaVdZTTB4bjdtMFdVYnJjcGJCSU44dXV3QkJkUWRwYUdsR2t4dzhDZFk5T2NBUTdMT3dBeGtpSW5ESHlGR1V5?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOQlhocGZIRndSYzQ1dTJlZUYzVmpZdVRXYlF6QzZnc095NU5DNkY1WWJpMlkxZUx6dkM3U1lhYWIzSTBPTHNnUThaTTZKRGJ0S0g5QU9IYkF2Z2kwa3FvdG1HUnA1YlZHdzFPZjZXODVFQWFfbFkxaHFRVDZQX2xpbEFmRkFkYWZ4NGd3UnJodDhNZzVUUkxBdDJVelFUTDRZ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
