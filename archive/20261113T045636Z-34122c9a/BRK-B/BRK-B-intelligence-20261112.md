# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:07:57.538543+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 3, 'ai': 14, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 8 named publishers; 4 exact duplicates; 21 HTTPS source links; largest publisher share 42.86%; oldest publication 2026-11-07

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 589.8300 |
| Return 1D (%) | 0.2703 |
| Return 1W (%) | 3.0577 |
| Return 1M (%) | 13.9548 |
| Return YTD (%) | 17.3441 |
| Return 1Y (%) | 17.4025 |
| Annualized volatility (%) | 15.1640 |
| Beta vs SPY | 0.0576 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 1.1381 |
| Downside deviation (rf=0, %) | 10.0753 |
| Sortino (rf=0) | 1.7129 |
| Historical VaR 95% (1D, %) | 1.4122 |
| Historical ES 95% (1D, %) | 2.0016 |
| Correlation vs SPY | 0.0522 |
| Tracking error vs SPY (%) | 19.9212 |
| P/E (trailing) | 16.51 |
| P/B | 0.00 |
| EV/EBITDA | -2.04 |
| Revenue growth (%) | 11.20 |
| Forward P/E (estimate) | 26.25 |
| Gross margin (%) | 26.60 |
| Operating margin (%) | 26.60 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | 4.19 |
| MA50 | 527.9616 |
| Close vs MA50 (%) | 11.7184 |
| MA200 | 499.8533 |
| Close vs MA200 (%) | 18.0006 |
| RSI (14, Wilder) | 79.9780 |
| MACD (12,26) | 17.2694 |
| MACD signal (9) | 14.3122 |
| MACD histogram | 2.9572 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 589.8300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.2703 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.0577 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 13.9548 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 17.3441 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 17.4025 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 15.1640 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.0753 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7129 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4122 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0016 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0522 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.9212 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0576 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1381 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 26.2497 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.1875 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.5080 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 79.9780 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.9572 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 11.7184 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 18.0006 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire Hathaway (BRK.B) Might Be Buying Back More Stock than Investors Realize. Here’s What’s Happening
- Summary: Berkshire may be conducting larger buybacks than previously known, indicating strong capital allocation strategy.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxQUjJfcy0tSjZBR1djcnBNbDVnVkI5am9lV2V4Mmh5QlJ1N2s4TFRJdWZNUmx6NzdmZVlJYU9vTHBkVDNWNW9NUUdTSFI3UnZCTUt5MHhVYjgtc3pGcnQzZFhaUzI5a3dMLVNlbDhGeWxtV2Y0N0pGbnVwajlnOXN5dXJBa2hqbm1wYUVOb1FDM2p2dzJrM1RXQUtQeU02QUp4RC1DYkRDN3lIY2VsMzBIQlFGaWxTdkYzWUpEamVTMFRjbDBBYU5VWkMwUQ?oc=5>

### Warren Buffett's Rule for Stock Buybacks Is Very Specific. Berkshire Spent a Record $9.6 Billion on Them Last Quarter.
- Summary: Record $9.6B buyback last quarter signals strong capital allocation.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNZ2x4aFRuSTUzYXFaQTc5S3E3N2xiRm9ZU0Npb3Q2RmFYN21JcUxfQld6MUZ0OUQ5ZkNtMzY5MDNXM2FQV0VwSlBWX0NDdi1uemdhdWFzcWVMSF9tUzhmSFA2Yl8xUWVtcUR4X0NrV090V2dTWE9MbjBCZ3VFY1NpOUVpSWNzSTRGTHpZNjVXZ1FqQ1JjU3I1alczTGpBZkswNnc?oc=5>

### Here is What to Know Beyond Why Berkshire Hathaway Inc. (BRK.B) is a Trending Stock
- Summary: Explains factors driving Berkshire's popularity among investors.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxObHJ5bFVHaTJjXzl1RkV0ZVIzYWo5SWJncFdKMzFXUndfcE1Pa1liVE9lamNRNHRqQkNpaER0M2t0Wmd3SzRDMWpBU25NVThNY2dncVVILTAwNW1rcmdaWmJ0VG1jbkpZNFFubHN2WFlxWEFGbVZ6eGZGSkRNVzhzTU9mcjdFVkhmR0w5clU5dXBoV2xuTVM5XzBUbUd6cHkx?oc=5>

### Berkshire Hathaway Stock Trades at Record Levels. CEO Greg Abel Clearly Sees More Room to Run.
- Summary: Berkshire stock hits record highs, indicating strong investor confidence.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQRVNpQWloWHRILTZOZlJKU2p0Y3FkNDZzQ0JZVzdHR2JuTmlrc3VEelNqRDNiWXpPWXBFWFlrUmtiQmlWNDBESTRfdVR0b2ZpRjdqNEtoc2dhOE0xT0NIVnlVS1BCUVpxWEs3azdGWDFnUVBSYmJvVW5RalBHeTFfOEREczlhYW5OSUpBei1iaXB6Q2NyT1NqV2VpbkpNM2dmWm5wTzRB?oc=5>

### What Are Wall Street Analysts' Target Price for Berkshire Hathaway Stock?
- Summary: Analysts discuss target price for Berkshire stock, reflecting market expectations.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOa3RnMWFBN1A5QlluSTAybkIzVUU4ZVdYdzdlWnhUOWlNNndQQ3dCVXJDLTd1LTNVT0VEUFM1dTU0Sng5OHprTFdiSDgxT1A3aUcwbHdPd3drZ3REWGVyQjlBWVBqMFR1dXJBLVJpN2dOTU9XQ2ExeGpZUWRERk5EZFBDSGhoQUpZR1dhdUk1eXJsaENCOWREZThvVjBZaGtKT1NiQ0w0WTFpbUZPOGUyUFpOZEpXUQ?oc=5>

### Warren Buffett's Successor, Greg Abel, Just Bought $9.6 Billion of the Oracle of Omaha's Favorite Stock (No, Not Alphabet!)
- Summary: Greg Abel purchased $9.6B of Berkshire stock, signaling confidence in the company.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxOMjdpUU00RXFoSUdqUzhzSEFjcmZMQkhoOVExeXdhUFQ4dzh2M1dpby1MbkcwenQ4YmFHdE4yVUxsdTg5eVBSNVJPTGFvUkNydFRhd0dTeVR5OEdGcVdxWVNzcUwtZWxEZjd3YkNlSDZiRVFvZXhWYkNqUTNGVDhVQUxId0RrcERZTVdWSWstbU1YaGpTVjBQdDRJWlR6WnF4aThBaTQ4UHF5X0ZCVVBabVJtS2t5STlJRjBEWERmNDZlb0t6LUtReklwRE9FZkhyMnBsaDNpQ2xheWs?oc=5>

### Berkshire’s Greg Abel Spent $14.4 Billion on Buffett’s Favorite Stock
- Summary: Greg Abel invested $14.4B in Berkshire stock, reinforcing shareholder value.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQM1QyWS1Rd3JOaU5lZHNhVEs4R2pFNE9rQlVVTmdVQ3E0WWt1XzFTTjFaNzdydS04QzJVc1hfYzNfSF8wcHJNTHh0TXNfSFhHQ3pxWlRtY2RaSE12QVZqenkxNUN4SDNVQmVtZktPbHEyOXpnNm5xbV9CMVQ4ZElqMmk5eElOM0RyTENYSWxtMks5dkVJekVleA?oc=5>

## HEADWINDS

### Berkshire Hathaway Earnings: Cash Levels Retreat Again as Acquisitions and Share Buybacks Pick Up
- Summary: Berkshire Hathaway Earnings: Cash Levels Retreat Again as Acquisitions and Share Buybacks Pick Up
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNU3k5QnhncjJEWEVxWGlGZm9DRnBxTGRBQ29fZHBfV3VrRnVkWEs5bzFSZnZhcURvdzBHVmdiOG5zOGJSdjZRMzVpZGQtY1RKRVBTS0dsa2ZmYWliSEIzUHctdEEtVVo1MHZNU2NsMzFaTHZ5eWxNQ0JWZnp0SWNwQjNIM2IxUmFrX0hvSFBmRzdkOUJ0UFBsUF9HbjlqamcxNDF0T2huUldUSndCQ0I2S2ZQLXdvbU1QTGFNSWZuazdWQQ?oc=5>

### Berkshire Hathaway Stocks Slip 1.01% Despite $9.6 Billion Buyback Surge
- Summary: Stock price fell despite a large buyback, indicating a negative short‑term move.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQWk93cHB4ZzdfR3N6OGQ5Rm04b3EwZTlOVmJEb3FZRElYWDhRTmxkTXRQMkVBLUM4YnRrTV95T25SdXVpbzBncFJGbFVLUk5ITkNVUk5KNE95ZXNNVHBYelgzWFQwTHVjZVRxZHJqdlhvSDd5WFQzQXdzWTFTM19MdjVXWTNYX0ZkNGsxMS1TbERFUVBBVFlLcVZMclBDQQ?oc=5>

### BRK.B Q3 Earnings Decline Year Over Year, Revenues Top Estimates
- Summary: Q3 earnings down YoY, revenues beat estimates.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPV1MxNnk5dVFqOExmUlBLNWhFS04zU1VQZHAwSWpyckJEQUgxdmFjSWJuQlBYbS1RcnJuSVlZejREcGtuR3ZacFlRSmEwOXFrdWlBTFlXRGRCRkhBRV9oWU5rRV9MOVMyZ0lfRXdyX25lR3ctSWdYVnM0dnIzMnlXVXJkMXVBUktpQW5OOVVWaEZkVDAw?oc=5>

## CATALYSTS

### Berkshire Hathaway more than doubles buybacks in third quarter as earnings decline
- Summary: Berkshire Hathaway more than doubles buybacks in third quarter as earnings decline
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxPTkNjdmJMNHlQMVFUZzMwdUFtSkNCaXAtODVHX2RSVE9OM3hsbzBQdS1INjFZWGFhcFFJTlZFczhzUzVGNnhNRXhQMUZYVk1QOUVWVnZuOExULW9JQXlWcnBfdmFrY3Rqb2lxWUZReEl5bTNLWURIcXdJWDJ3TURaYWtIaWdmS244?oc=5>

### Berkshire Hathaway (BRK.A) Got A 19.3% Q3 Earnings Lift From BNSF
- Summary: Berkshire Hathaway (BRK.A) Got A 19.3% Q3 Earnings Lift From BNSF
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQX2ZKRWdxdVJieVpfZEpsMUgxUWs1VUNHRGp2cEIyNDkzOVVFV2JiQzBRMUUzbDU2U2JnTWU1aHVldGdselpXeEZlMUhmRTE4b3dvM3dkN1NnMnlFNm40NkNGSG1udmJwX2U1c2d5X010czk0akFiZTRRd3Rld0Jrb2dvdVFoOXBhbUlydVpOdEQtckp0S1RfN2JB?oc=5>

### Warren Buffett's Successor, Greg Abel, Just Added Another Tech Stock to Berkshire's Portfolio. Here's What He Sees.
- Summary: New tech investment indicates portfolio diversification and potential growth opportunities.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPOS0tVEUtMkVvMmoydEJNRks4SEcwUUZEQnpmM05sZUpmWVdlcDJzTzREX25GR19HWkczRExwc1FFemNjNllyd3BoaGlTd0czMS1Va1BQdmZOMnR1VU13TFpzUExzOHlvNWdIa0VXUm5ha3VBRFJOUjZoaUl1ZW8xTm9xYlV5bHRTOXpyXzVhaVlsT2tVVFB1dQ?oc=5>

### What You Actually Own When You Buy a Share of Berkshire Hathaway
- Summary: Explains the components of a Berkshire Hathaway share, including its underlying assets and voting rights.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOMVpuMEJ1b0IyTUJPVE1OakZ0NmhqWVNCQTRILXlWaTZPdmkyQzNrb3lXSGVESFZhY0V2eTdMSXdHdFROUW9qT3dlcUN0UkpiMGYtWDhKYVhlOGVmNFpmSDR2WXp6S0VrUWtreEp5ZkxQMlkzWThxMzFZTlZjVkZVMUNCdEQya1ZsOEFWc0czRDBoNHpiX2R0TUhQb3Rrdw?oc=5>

### Warren Buffett’s Successor Is Doubling Down on Berkshire Hathaway Stock. You Probably Shouldn’t
- Summary: Reports that Buffett’s successor increased his Berkshire holdings, suggesting a potential market move.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOZlhDenNoR3FMdmtnWUtUYkpwU2RWS1YzNnZ5UVhsN0FqTi1YWXRnbDhmRlJSNGxxMGNyRzR2ZUVJY3FhZjZMY3RGR2RKSlNJcjBhd1BUcDEwb05NOGM0bmN2NjZoWWxNTEhwczgzQXRsYm5SMk5lU0o0UTV0VUtJdm5UNENhY1hoX3hoMS00NGRRM0ZVVnR1N2hZeUJDaFBQZ1dHM3Vn?oc=5>

### Greg Abel Has Plowed $14.4 Billion Into Warren Buffett's Favorite Stock This Year, and It's Not Apple
- Summary: Highlights Greg Abel’s significant investment in Berkshire Hathaway, indicating strong confidence in the company.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPNTkxOVJNbDlUV05ZbG93M1hvTFNOdG1uN1ZZaGQ0RDlSdWRlTTl1M21sd3Z1c2xUSEl1cVhXYUEtMmFHLTBGYlpBcFBjMl9wMzg1MFFDTUF2T2l6eXhMM0p4RzVQYWQtVDlURnhUckFndS0wV2M2cGtITFVoM0Fqb3BWOV9oZUJqaDJNdnh2SXBXaWd2RGFn?oc=5>

### Greg Abel's Berkshire Hathaway Owns 37% of This Company. Here's Why the Stock Is Also a Buy for Retail Investors.
- Summary: Details Berkshire’s 37% stake in another firm, suggesting a strategic investment opportunity.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOM1hXc0JSeWtxeFVyeWZPdWhwOVM4ZTNleEZzTFN6QVlRbHA0S0FnMmJQWGN5Tll0bkJTT0dlYzZ5angzSmpFYjVWNkZwWUNDa2FnV1dPTUZQM3RjUHFoQ1QwYzE0cTY5RDdsekNMRWNudlc4YnB0YlFvaWh5NWsxS180UHlwZTA0YWpHeFFTMEV3Zw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **16.51** | **0.00** | **-2.04** | **11.20** | **1,253,105,205,248.00 USD** | **17.40** |
| MKL | 13.96 | 1.30 | 8.03 | -11.20 | 23,994,992,640.00 USD | -6.21 |
| FFH.TO | 10.16 | 1.45 | 8.87 | 1.90 | 57,089,724,416.00 CAD | 23.15 |
| L | 15.47 | 1.24 | 8.76 | 1.90 | 22,614,847,488.00 USD | 7.73 |

Peers fetched as_of: 2026-11-12; BRK-B reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-07
- Next expected earnings: 2027-03-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-09
- Revenue (latest available single quarter): 105,647,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 22,112,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1067983/000119312526452412/brka-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiywFBVV95cUxQUjJfcy0tSjZBR1djcnBNbDVnVkI5am9lV2V4Mmh5QlJ1N2s4TFRJdWZNUmx6NzdmZVlJYU9vTHBkVDNWNW9NUUdTSFI3UnZCTUt5MHhVYjgtc3pGcnQzZFhaUzI5a3dMLVNlbDhGeWxtV2Y0N0pGbnVwajlnOXN5dXJBa2hqbm1wYUVOb1FDM2p2dzJrM1RXQUtQeU02QUp4RC1DYkRDN3lIY2VsMzBIQlFGaWxTdkYzWUpEamVTMFRjbDBBYU5VWkMwUQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNZ2x4aFRuSTUzYXFaQTc5S3E3N2xiRm9ZU0Npb3Q2RmFYN21JcUxfQld6MUZ0OUQ5ZkNtMzY5MDNXM2FQV0VwSlBWX0NDdi1uemdhdWFzcWVMSF9tUzhmSFA2Yl8xUWVtcUR4X0NrV090V2dTWE9MbjBCZ3VFY1NpOUVpSWNzSTRGTHpZNjVXZ1FqQ1JjU3I1alczTGpBZkswNnc?oc=5
- https://news.google.com/rss/articles/CBMi8wFBVV95cUxQMkZDbzkwLTA3amltUTd6N041ZWVwZVo4bmtpVF9nZTRMZEExTXRBaXRvT2xIdGowdHRwd1BpUG1IdzU4MTRKTnJiSnJNNkZ1a2VOSUlXQTNsY2o2Y1VUaEl2N0wxRlZkRDRfTkJBakZxbkthbVllOG1yaHJZeW80Y19sdUR6TnlxYnZ3aWZOcTg5THFtbEY5cjU5M1ZJUUltR25vZzhNZkFUQm1UNGxjR291YUgxV0FlcllVSTNiWmh4ZGNRa3JtdURvbWNfNGxJbU12c0hidll4RmxDbFFjTHBwZXBobmNBeS00WjdFVUdIblU?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxObHJ5bFVHaTJjXzl1RkV0ZVIzYWo5SWJncFdKMzFXUndfcE1Pa1liVE9lamNRNHRqQkNpaER0M2t0Wmd3SzRDMWpBU25NVThNY2dncVVILTAwNW1rcmdaWmJ0VG1jbkpZNFFubHN2WFlxWEFGbVZ6eGZGSkRNVzhzTU9mcjdFVkhmR0w5clU5dXBoV2xuTVM5XzBUbUd6cHkx?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQRVNpQWloWHRILTZOZlJKU2p0Y3FkNDZzQ0JZVzdHR2JuTmlrc3VEelNqRDNiWXpPWXBFWFlrUmtiQmlWNDBESTRfdVR0b2ZpRjdqNEtoc2dhOE0xT0NIVnlVS1BCUVpxWEs3azdGWDFnUVBSYmJvVW5RalBHeTFfOEREczlhYW5OSUpBei1iaXB6Q2NyT1NqV2VpbkpNM2dmWm5wTzRB?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxPdWxNZHVCTnhVUE84a1R5MGtQdVZ6WkxDb0tfMTN6aUR3WklyM2RROC1wTU5EYS1xR0FfanBuYkFncmdPQlNKcXNkM0ZZRklzWERSTkVqMWt1RUdqUHBYRE5IQ2tPdXY4VktzNUFQbnNVWHBNbUVGdG9fb3FrVExnY252bkk1MjBmVTlvek5nSjVSX0dadi1sQnJ5c2ctaXdpaVd6WnFjX1k2dnRJM0lZSjR1bG5ZWHRUY1c5Z0F2R1hnS3FjU0ZUUDNaVHExMEE3?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOa3RnMWFBN1A5QlluSTAybkIzVUU4ZVdYdzdlWnhUOWlNNndQQ3dCVXJDLTd1LTNVT0VEUFM1dTU0Sng5OHprTFdiSDgxT1A3aUcwbHdPd3drZ3REWGVyQjlBWVBqMFR1dXJBLVJpN2dOTU9XQ2ExeGpZUWRERk5EZFBDSGhoQUpZR1dhdUk1eXJsaENCOWREZThvVjBZaGtKT1NiQ0w0WTFpbUZPOGUyUFpOZEpXUQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQUWlIQkEtV3A5SE9taWtKbUNiU0Zudnp1X3plYmpRY3YyRXNYdFYzVFlOYUFQLUdmY2xodjQ5eDE3T2dnd25jSmcwZGtlZ0JxeV8ydk0zQjBTbHczWlF3THRpVkQ1bVhxdWpvLXBJd0piaUplUHBpcmJZVkVHU0FmY1ZGYWZndFJxMUFoWjYwdHZBSzJKcEZLbm92azJKLTg?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxOMjdpUU00RXFoSUdqUzhzSEFjcmZMQkhoOVExeXdhUFQ4dzh2M1dpby1MbkcwenQ4YmFHdE4yVUxsdTg5eVBSNVJPTGFvUkNydFRhd0dTeVR5OEdGcVdxWVNzcUwtZWxEZjd3YkNlSDZiRVFvZXhWYkNqUTNGVDhVQUxId0RrcERZTVdWSWstbU1YaGpTVjBQdDRJWlR6WnF4aThBaTQ4UHF5X0ZCVVBabVJtS2t5STlJRjBEWERmNDZlb0t6LUtReklwRE9FZkhyMnBsaDNpQ2xheWs?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQM1QyWS1Rd3JOaU5lZHNhVEs4R2pFNE9rQlVVTmdVQ3E0WWt1XzFTTjFaNzdydS04QzJVc1hfYzNfSF8wcHJNTHh0TXNfSFhHQ3pxWlRtY2RaSE12QVZqenkxNUN4SDNVQmVtZktPbHEyOXpnNm5xbV9CMVQ4ZElqMmk5eElOM0RyTENYSWxtMks5dkVJekVleA?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPVkxDV3ZJUzVsVWxvNXJvdk1oUDU0YjVtbHBrempqdXprRGluZFhIWDN0bF9SNXZzRXRwY3FZZTgxWWdRXzVpLTlGT1ZRUEpIRWV2cU9hOTVibGgtTm9XUFVxOUd0ZTdhenZEYS1XS1lIbDBSLVZEVWRJZFFOMlhzVk9hQ2o5VEt2enUwMzM0a25vel8wUEp2T1hMMnZremJIQlVWNWk3WHNUdWtCWUww?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNU3k5QnhncjJEWEVxWGlGZm9DRnBxTGRBQ29fZHBfV3VrRnVkWEs5bzFSZnZhcURvdzBHVmdiOG5zOGJSdjZRMzVpZGQtY1RKRVBTS0dsa2ZmYWliSEIzUHctdEEtVVo1MHZNU2NsMzFaTHZ5eWxNQ0JWZnp0SWNwQjNIM2IxUmFrX0hvSFBmRzdkOUJ0UFBsUF9HbjlqamcxNDF0T2huUldUSndCQ0I2S2ZQLXdvbU1QTGFNSWZuazdWQQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQWk93cHB4ZzdfR3N6OGQ5Rm04b3EwZTlOVmJEb3FZRElYWDhRTmxkTXRQMkVBLUM4YnRrTV95T25SdXVpbzBncFJGbFVLUk5ITkNVUk5KNE95ZXNNVHBYelgzWFQwTHVjZVRxZHJqdlhvSDd5WFQzQXdzWTFTM19MdjVXWTNYX0ZkNGsxMS1TbERFUVBBVFlLcVZMclBDQQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPV1MxNnk5dVFqOExmUlBLNWhFS04zU1VQZHAwSWpyckJEQUgxdmFjSWJuQlBYbS1RcnJuSVlZejREcGtuR3ZacFlRSmEwOXFrdWlBTFlXRGRCRkhBRV9oWU5rRV9MOVMyZ0lfRXdyX25lR3ctSWdYVnM0dnIzMnlXVXJkMXVBUktpQW5OOVVWaEZkVDAw?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxPTkNjdmJMNHlQMVFUZzMwdUFtSkNCaXAtODVHX2RSVE9OM3hsbzBQdS1INjFZWGFhcFFJTlZFczhzUzVGNnhNRXhQMUZYVk1QOUVWVnZuOExULW9JQXlWcnBfdmFrY3Rqb2lxWUZReEl5bTNLWURIcXdJWDJ3TURaYWtIaWdmS244?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQX2ZKRWdxdVJieVpfZEpsMUgxUWs1VUNHRGp2cEIyNDkzOVVFV2JiQzBRMUUzbDU2U2JnTWU1aHVldGdselpXeEZlMUhmRTE4b3dvM3dkN1NnMnlFNm40NkNGSG1udmJwX2U1c2d5X010czk0akFiZTRRd3Rld0Jrb2dvdVFoOXBhbUlydVpOdEQtckp0S1RfN2JB?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPOS0tVEUtMkVvMmoydEJNRks4SEcwUUZEQnpmM05sZUpmWVdlcDJzTzREX25GR19HWkczRExwc1FFemNjNllyd3BoaGlTd0czMS1Va1BQdmZOMnR1VU13TFpzUExzOHlvNWdIa0VXUm5ha3VBRFJOUjZoaUl1ZW8xTm9xYlV5bHRTOXpyXzVhaVlsT2tVVFB1dQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOMVpuMEJ1b0IyTUJPVE1OakZ0NmhqWVNCQTRILXlWaTZPdmkyQzNrb3lXSGVESFZhY0V2eTdMSXdHdFROUW9qT3dlcUN0UkpiMGYtWDhKYVhlOGVmNFpmSDR2WXp6S0VrUWtreEp5ZkxQMlkzWThxMzFZTlZjVkZVMUNCdEQya1ZsOEFWc0czRDBoNHpiX2R0TUhQb3Rrdw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOZlhDenNoR3FMdmtnWUtUYkpwU2RWS1YzNnZ5UVhsN0FqTi1YWXRnbDhmRlJSNGxxMGNyRzR2ZUVJY3FhZjZMY3RGR2RKSlNJcjBhd1BUcDEwb05NOGM0bmN2NjZoWWxNTEhwczgzQXRsYm5SMk5lU0o0UTV0VUtJdm5UNENhY1hoX3hoMS00NGRRM0ZVVnR1N2hZeUJDaFBQZ1dHM3Vn?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPNTkxOVJNbDlUV05ZbG93M1hvTFNOdG1uN1ZZaGQ0RDlSdWRlTTl1M21sd3Z1c2xUSEl1cVhXYUEtMmFHLTBGYlpBcFBjMl9wMzg1MFFDTUF2T2l6eXhMM0p4RzVQYWQtVDlURnhUckFndS0wV2M2cGtITFVoM0Fqb3BWOV9oZUJqaDJNdnh2SXBXaWd2RGFn?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOM1hXc0JSeWtxeFVyeWZPdWhwOVM4ZTNleEZzTFN6QVlRbHA0S0FnMmJQWGN5Tll0bkJTT0dlYzZ5angzSmpFYjVWNkZwWUNDa2FnV1dPTUZQM3RjUHFoQ1QwYzE0cTY5RDdsekNMRWNudlc4YnB0YlFvaWh5NWsxS180UHlwZTA0YWpHeFFTMEV3Zw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
