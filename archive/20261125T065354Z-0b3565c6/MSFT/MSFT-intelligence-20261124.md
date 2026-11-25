# MSFT Intelligence Report

- ticker: **MSFT**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/MSFT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MSFT/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:16:19.472767+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 2, 'ai': 15, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/MSFT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 16 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 24.0%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 496.1300 |
| Return 1D (%) | 0.7371 |
| Return 1W (%) | -1.8078 |
| Return 1M (%) | -5.2280 |
| Return YTD (%) | 3.4370 |
| Return 1Y (%) | 5.5363 |
| Annualized volatility (%) | 34.0492 |
| Beta vs SPY | 0.9358 |
| Max drawdown (%) | -27.9702 |
| Sharpe (rf=0) | 0.3259 |
| Downside deviation (rf=0, %) | 21.7770 |
| Sortino (rf=0) | 0.5095 |
| Historical VaR 95% (1D, %) | 2.8530 |
| Historical ES 95% (1D, %) | 4.1000 |
| Correlation vs SPY | 0.4110 |
| Tracking error vs SPY (%) | 31.0552 |
| P/E (trailing) | 25.89 |
| P/B | 7.83 |
| EV/EBITDA | 18.25 |
| Revenue growth (%) | 18.80 |
| Forward P/E (estimate) | 20.50 |
| Gross margin (%) | 67.66 |
| Operating margin (%) | 47.10 |
| Return on equity (%) | 34.22 |
| Free cash flow yield (%) | 0.08 |
| MA50 | 518.6329 |
| Close vs MA50 (%) | -4.3389 |
| MA200 | 442.8289 |
| Close vs MA200 (%) | 12.0365 |
| RSI (14, Wilder) | 41.2607 |
| MACD (12,26) | -7.5348 |
| MACD signal (9) | -3.0952 |
| MACD histogram | -4.4397 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MSFT': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 496.1300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.7371 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.8078 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -5.2280 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 3.4370 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 5.5363 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.0492 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.7770 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5095 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8530 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1000 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4110 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.0552 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9358 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.9702 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3259 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.5005 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 67.6570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 47.1040 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 34.2210 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.0813 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.8941 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.2607 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.4397 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -4.3389 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 12.0365 -> Clearly above the moving-average trend level.

## TAILWINDS

### Microsoft (NASDAQ: MSFT) Stock Price Sits 11% Below Record Highs Despite Monday's Nvidia-Driven Tech Rally
- Summary: Microsoft (NASDAQ: MSFT) Stock Price Sits 11% Below Record Highs Despite Monday's Nvidia-Driven Tech Rally
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxQWk9fMnlSS3RJREZlVExGelNuS0JSNm50Y2EzWHNMNDlMWDNRdV80OXdqRnFNMmJUcEJ5X2VRMDk5Ml82VGs1UUVHalpuYXFDU2lTOVBsU0Y3bUNXV0RuTk5nOVRoajlManhuLVV0eUR4eW5Qai1HY3lGRFBKZnhkRGpRSkdYY2Z5UWRXZUlidWhEajU4MnVuU0ExcjlaQjdIekJkcE9vNm16R0ZkUEpPSTJERi1rXzhMaGJtM1J2d3MzVzZFSmxUY0xMVnpPZ2xOcDdpaDFFQWRwVGdRZzZZbEFoYXo?oc=5>

### Is Microsoft Stock Stronger Than It Looks?
- Summary: Analysis questioning stock strength.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPSTN0N1hHMGNON3J1ZFRlaGhhZXA4WnZWWlBRRXU2cG9Sd2J5TmVYMGlWSnJ4TWExU0JJaWN3d3RhM0Rja0RkbmhmQkhLMkhkTlFka3p1TFNUUUhQdTRBNWhJMmhYTmY2QU9PZDJybmtoZWEwVDYzY3BDMWMwRUM3Uy1YQ3Rjck10M1dzaWxzRVNQZ05VQ014V2JiTkJqTWZMSURocA?oc=5>

### Microsoft (MSFT) Stock May Look Reasonable As AI Commitments Draw Scrutiny
- Summary: Analyst suggests MSFT stock appears reasonable amid scrutiny of AI commitments.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNalJYeUVUa3czcERnOXA2LUVJUlJaM0owQlJvZm9Gek1DeHZXV3lwREJFZVM5Nm9KVjdMbC1KRGJmeWg4Rk15M0FZV0ZMNEM0dF9wLXF3dWRpRjhZNVY4Y19fSU9ucUR0QVZKZ1hEQl91eVdnYmlZZ0E4X2RlWmxOWV9KTmpWcEZLZUxBYUJwV3plM3pUOU1MdzF3?oc=5>

### Microsoft (MSFT) and Its Rivals Are Making a Huge AI Bet – Here’s What Investors Should Know
- Summary: Microsoft is investing heavily in AI, positioning itself for future growth.
- Date: 2026-11-20 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQZkJwODVzRnptNlFrc3UtMlA0NUN2bkVNYnNDcGQ3MDBNRzdVbnJPT0Q1c21xNndPMUY5eVA4NzVCUW1fdkx3bGJUMnFUdTV6cjNPUkY4RWpCMXpsNHZjQVp0bHd6RVFmMEpxcGkyNEtNSWJZTklOdVd1Z1RwaWlJX3N1emMxQ0FYUjRaeHlzcXozeFV5bXgzbzZMUERoQQ?oc=5>

### Microsoft Corp Stock (MSFT) Opened Up by 3.39% on Nov 23: A Full Analysis
- Summary: Stock opened higher by 3.39%.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPWUd0X3I1bVJ2SDRzRDBLajlQcXRUTWFMbjg1RS1YR1BhWlR1UVM0dEgtS2VWc2lySFpXYkppSC1XMnFaZkdXa0cxMjBqbjZBRkxYLUd3Y3RhTmdUUVlLTzREdmJEWEhJVWhXTjZucWZoOFYtNXJmdU0tWVJVWXM1S1Y1QkFlY0RVQ0Nz?oc=5>

### Weekly Recap: Azure revenue growth and Maia 300 AI chip unveiling
- Summary: Azure revenue growth and new AI chip unveiled.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPdTJLNGZUM2ZLZEV3d3JWZEM2Z1pqYzRkM0E1bWdpNjJHcVhraEQyTU9vNTZ2T1RzNlF4UWs5aUVCNU9jN3R2NmhQN1ptM2JiQXJtRFl2SmExekh0bG5JZzV0eTVFODJZancxRUxUcF82RDhRRE9mTk5YS3dNZWhsS0F4aWc0MlN3YnFYZDBoNnlLMDg2NktSZ2pPU3gxYXVkajM3bmNqRmY0dTB4ZHJpbDh4dlF1ZVBNRlNpd1p6cV94Z29H?oc=5>

### Microsoft (MSFT) Is One of the Safest Ways to Own AI
- Summary: Positively frames MSFT as a secure AI investment.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOTGFBVVdNRFBFZE9EWTZDR2tLMFNwTXNEbnMycHhqOElxTnRwYzNjdUxRTlRjVGhLR25QRUxvTUdVNlFlOEhWc2JKZFI3Y3JoN3hIS1hHN25CY0s5RFhpeHE3bGN5LWg3c0VVN0ZhUVRBSk5ZbjRBaEtBS2pIVGtHUlV6a0J0Qy1KOFhJS2xCMXJ1elpScUMtcGVn?oc=5>

### Microsoft Stock (MSFT) Rises on Reports That Xbox’s Project Helix Will Be a Normal Gaming Console
- Summary: Xbox Project Helix expected to launch as a standard console, boosting investor confidence.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQbEpreVZCbFQ4SFZpZ2FKUGZ0bkhwNmVuMHdZYUE5RTFsUXBMTFJRTjNoR1ZYSS1IVEpnYzFMMG5GRmxkbjQ4ZHJsMWR2dHFVVVg0UElQdU5tQjZNQWZ1dFRtNmtDNEwxR21idmN3RFhUdE42YURqdEc4Z3o0NXBwWV92RkdhN2dzS1pLSEtNb3BTSEtUNFFLMG5HUW8wQ0xDeGdrZ1gtSVFrVEd6dVBtNlV3Q2xMaFIzbnh3RHdRUExMZw?oc=5>

### Microsoft Stock (NASDAQ:MSFT) Ticks Up with a Return to Cloud PC Plans
- Summary: Reintroduction of Cloud PC plans signals renewed focus on cloud services, lifting stock.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPcm45NHpfT2R3ZUFidXY4LVktaXZWZ3dqMlRIOFZHZzc2WGh2T0dpQ1lFQ1poQlNWeHlwV0FEaVgxWmJqRVN1VDU0SDFHeWYySGtsV2ZzTWw3N0czQlZmWnhOcmRkNU40NjdjV1I5LXVfTHltUzhNQ29XWWVLQnMtMV9Kd3JtbFpPOG50TUFTbVJ5b0ZiSGRWLUhoNlNsZw?oc=5>

### What Microsoft (MSFT)'s Enterprise AI Partnerships Mean For Shareholders
- Summary: New AI partnerships expand enterprise offerings, potentially increasing revenue streams.
- Date: 2026-11-24 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQSVY1c1libERfeFdXazhSbjdCblNEWHZfWGRiVlFPVFdDUWFMLUtjaEFudTU1LTZLOFRTM2Q2TVAyczdOcVZzbUJYTHE4UVBRdUkwOURqbTZtYlE3eVIxRVNPbU9JcWVVNER5UHdlVURGWWFsQnM3eF9vZ2c4VnhpUWlBWm5xZkYwY1UtMFZUdF83OXFGMVQzbmV5cTJkYUlkRDF5SGZ3WkE?oc=5>

## HEADWINDS

### Microsoft Stock Falls 7% in a Month as 24-Hour Outage Triggers "Code Red"
- Summary: Microsoft Stock Falls 7% in a Month as 24-Hour Outage Triggers "Code Red"
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNMmswXzV3QXUxa3JXUFpWUEtGWHZyZzdjdUpsN0pmZzgxM2pqaFMzeXVidDV1ZEY1ZmNJbDIxMHJ5WkVaUF9ValMwdTZzSVQ2Qjdid0RvX3NISXNlLTNiYmx5dTlWdVNvcUVEX2RNNElFeDU5WjlaRTF3a3UzaHBTeXIzZFUxdDFTeDJ1Q1ozdGlJX2FXVmNKSXhaMHV6QVk?oc=5>

### Microsoft engineers faced 'fog of war' during 24-hour outage: report (MSFT:NASDAQ)
- Summary: Reports a 24‑hour outage affecting Microsoft services.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOZXdjMEJSdlpsWVNMV3hya0k1NDRJYXJhZGJoYnZ2VElkUDNxeUh4dF96YVZUak8xaGxfaEVPVm1oOWh6VVFoRzNBLU9ESkxkeDJwQlI1YzhXS3p1dWE3eml2UzdyMTFvbmM4bERmcC1kLWIydm1yS0hRVUZHeTFXNEdETmRuMkwzNjZiRjJBMzBkVm1NSFVLN18xdnNmS203SHRobFRB?oc=5>

### Microsoft Corporation (MSFT) Is Facing AI Spending Fears: Could Its Cloud Growth Change the Narrative?
- Summary: Highlights concerns over AI spending impacting cloud growth.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPSHhZLXZ3QWQ5eFRidGdBVDBfeXYteFljWGQ4Uk9PRUxaOHlNWWVXSzdmOVRyX0pmSm91dWV2SmRZa3pGMHpvQjcxTldsd3hSS1pwVWxtclYxUTNOc1hHZkZYa3ZteFlaakJKNGRwUkJaYVQxdUs0c2V1RjEzOU1yUnA5aWN3a0pFUzhBbHZQVWNvd1FUWXNKV1BNZ3dPMm8zWlZn?oc=5>

## CATALYSTS

### Microsoft Corporation (MSFT) Stock Forecasts
- Summary: Analysts provided stock forecasts for Microsoft.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPQTVtR182YU9iMFIxRHBBTHlWeFRJTWJmMDI4WWwyWUFmem1IWFBPeTYyY3pKQ3o1bkJBZnVwY0xwZ0ZsRHA2UHNzVGFMTjhiRnRMWEtNY2pJLWxnNm1uLTFpZ1cxdUxpZlVaaWl5d2ZtWlJPY2Q5SERuYWNncEQ3UnFlQkxxVTl3MDhOWA?oc=5>

### Microsoft beats earnings estimates and lifts dividend: Can MSFT sustain gains?
- Summary: Microsoft reported earnings above estimates and increased its dividend, potentially supporting future growth.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxONWdLNmU3ckxKNHE2MUk5ZFdyZ0p1cmlRcjhsUHI4YktvcWN3S2wtb09nT0pZdElRMnVUa3Ewc3FoMU1FTGkzd2FuSlNIVEN0UVVyREFpejFmdTBBSEg1eDdLY2ZjZDljdGNzeVRqVkc3VmtCUkNLRnd0azlXc1hOaGlKNU1ON0lLOUNJTTdGU01tQjNrOWc?oc=5>

## RISKS

### Microsoft rises as warning on Chinese optical hardware ban fuels AI investment concern
- Summary: Chinese ban warning may dampen AI investment, potentially affecting Microsoft’s growth prospects.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxPRERJcHRpV3FoSUtqN2I0SXk5TGFGYWNjNHZtTGdHaDFuNk9nYklsUlU1WENjMm12OGZzRGZaZ2JoOVQ4cXRiTTA0REdIeWwza0JVSVZ3ZnpKYW5SMFR5X1FuZmNNSnVmUlpSUUM0WHl4c0VKSGVnZ09OeG9KSE5LMFZzSEZQQQ?oc=5>

### Microsoft’s Code Red Exposes a Bigger Cloud Risk for Crypto
- Summary: Security alert highlights increased cloud vulnerability affecting crypto operations.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQd1dwa3Y0b2VQWHZTZUpTc05mczN6bWRkTVp2RmwzNjdOOGp2eDdzNG1sd29CNW12QnVBUGVmRk40NHNjYWd3czZhVFdySTljdjNpU2NBV1pJNFE2MnB3T1pJT2thR1E0R25oekQ2T3RrMlJ5N2RHT1RaSm90QmYzdG1BY2Fwd095cW9pcXU2Y9IBxgFBVV95cUxQalBHcnJRa0FEWUhLdGpZb0JxNUo2SUg2X1VYeWgyalZZRTVTU3RQQTl5clQ5TExDZ0RaX05hYXdVYXY5YVFpM0RNeTVQMHVmZjdpbjFGNUxXeTFkTHJNZmEwcldDXzcteWhzT2dGZUJ3S3pQZ1dzVXVnakR0Um5FYmhTeDFUZDdIMUxXY1FreHBGekpFdXdmc3YtNzNvMXJ3VDdPWUtVMXhWZmFibW41NmZDVVpDajc1eHU3aGd1UlhocERGX2c?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MSFT** | **25.89** | **7.83** | **18.25** | **18.80** | **3,684,357,898,240.00 USD** | **5.54** |
| ORCL | 17.16 | 5.36 | 13.61 | 29.60 | 341,389,017,088.00 USD | -44.60 |
| GOOGL | 14.57 | 5.20 | 17.97 | 24.70 | 3,430,640,517,120.00 USD | -12.18 |
| AMZN | 20.40 | 4.45 | 15.89 | 12.10 | 2,728,046,362,624.00 USD | 11.49 |

Peers fetched as_of: 2026-11-24; MSFT reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 19,953,000,000.00 USD; period 2010-10-01/2010-12-31; fiscal year/reporting period 2011/Q2
- Net income (latest available single quarter): 36,629,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi5AFBVV95cUxQWk9fMnlSS3RJREZlVExGelNuS0JSNm50Y2EzWHNMNDlMWDNRdV80OXdqRnFNMmJUcEJ5X2VRMDk5Ml82VGs1UUVHalpuYXFDU2lTOVBsU0Y3bUNXV0RuTk5nOVRoajlManhuLVV0eUR4eW5Qai1HY3lGRFBKZnhkRGpRSkdYY2Z5UWRXZUlidWhEajU4MnVuU0ExcjlaQjdIekJkcE9vNm16R0ZkUEpPSTJERi1rXzhMaGJtM1J2d3MzVzZFSmxUY0xMVnpPZ2xOcDdpaDFFQWRwVGdRZzZZbEFoYXo?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPSTN0N1hHMGNON3J1ZFRlaGhhZXA4WnZWWlBRRXU2cG9Sd2J5TmVYMGlWSnJ4TWExU0JJaWN3d3RhM0Rja0RkbmhmQkhLMkhkTlFka3p1TFNUUUhQdTRBNWhJMmhYTmY2QU9PZDJybmtoZWEwVDYzY3BDMWMwRUM3Uy1YQ3Rjck10M1dzaWxzRVNQZ05VQ014V2JiTkJqTWZMSURocA?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNalJYeUVUa3czcERnOXA2LUVJUlJaM0owQlJvZm9Gek1DeHZXV3lwREJFZVM5Nm9KVjdMbC1KRGJmeWg4Rk15M0FZV0ZMNEM0dF9wLXF3dWRpRjhZNVY4Y19fSU9ucUR0QVZKZ1hEQl91eVdnYmlZZ0E4X2RlWmxOWV9KTmpWcEZLZUxBYUJwV3plM3pUOU1MdzF3?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQZkJwODVzRnptNlFrc3UtMlA0NUN2bkVNYnNDcGQ3MDBNRzdVbnJPT0Q1c21xNndPMUY5eVA4NzVCUW1fdkx3bGJUMnFUdTV6cjNPUkY4RWpCMXpsNHZjQVp0bHd6RVFmMEpxcGkyNEtNSWJZTklOdVd1Z1RwaWlJX3N1emMxQ0FYUjRaeHlzcXozeFV5bXgzbzZMUERoQQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPWUd0X3I1bVJ2SDRzRDBLajlQcXRUTWFMbjg1RS1YR1BhWlR1UVM0dEgtS2VWc2lySFpXYkppSC1XMnFaZkdXa0cxMjBqbjZBRkxYLUd3Y3RhTmdUUVlLTzREdmJEWEhJVWhXTjZucWZoOFYtNXJmdU0tWVJVWXM1S1Y1QkFlY0RVQ0Nz?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPdTJLNGZUM2ZLZEV3d3JWZEM2Z1pqYzRkM0E1bWdpNjJHcVhraEQyTU9vNTZ2T1RzNlF4UWs5aUVCNU9jN3R2NmhQN1ptM2JiQXJtRFl2SmExekh0bG5JZzV0eTVFODJZancxRUxUcF82RDhRRE9mTk5YS3dNZWhsS0F4aWc0MlN3YnFYZDBoNnlLMDg2NktSZ2pPU3gxYXVkajM3bmNqRmY0dTB4ZHJpbDh4dlF1ZVBNRlNpd1p6cV94Z29H?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOTGFBVVdNRFBFZE9EWTZDR2tLMFNwTXNEbnMycHhqOElxTnRwYzNjdUxRTlRjVGhLR25QRUxvTUdVNlFlOEhWc2JKZFI3Y3JoN3hIS1hHN25CY0s5RFhpeHE3bGN5LWg3c0VVN0ZhUVRBSk5ZbjRBaEtBS2pIVGtHUlV6a0J0Qy1KOFhJS2xCMXJ1elpScUMtcGVn?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQbEpreVZCbFQ4SFZpZ2FKUGZ0bkhwNmVuMHdZYUE5RTFsUXBMTFJRTjNoR1ZYSS1IVEpnYzFMMG5GRmxkbjQ4ZHJsMWR2dHFVVVg0UElQdU5tQjZNQWZ1dFRtNmtDNEwxR21idmN3RFhUdE42YURqdEc4Z3o0NXBwWV92RkdhN2dzS1pLSEtNb3BTSEtUNFFLMG5HUW8wQ0xDeGdrZ1gtSVFrVEd6dVBtNlV3Q2xMaFIzbnh3RHdRUExMZw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPcm45NHpfT2R3ZUFidXY4LVktaXZWZ3dqMlRIOFZHZzc2WGh2T0dpQ1lFQ1poQlNWeHlwV0FEaVgxWmJqRVN1VDU0SDFHeWYySGtsV2ZzTWw3N0czQlZmWnhOcmRkNU40NjdjV1I5LXVfTHltUzhNQ29XWWVLQnMtMV9Kd3JtbFpPOG50TUFTbVJ5b0ZiSGRWLUhoNlNsZw?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQSVY1c1libERfeFdXazhSbjdCblNEWHZfWGRiVlFPVFdDUWFMLUtjaEFudTU1LTZLOFRTM2Q2TVAyczdOcVZzbUJYTHE4UVBRdUkwOURqbTZtYlE3eVIxRVNPbU9JcWVVNER5UHdlVURGWWFsQnM3eF9vZ2c4VnhpUWlBWm5xZkYwY1UtMFZUdF83OXFGMVQzbmV5cTJkYUlkRDF5SGZ3WkE?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNMmswXzV3QXUxa3JXUFpWUEtGWHZyZzdjdUpsN0pmZzgxM2pqaFMzeXVidDV1ZEY1ZmNJbDIxMHJ5WkVaUF9ValMwdTZzSVQ2Qjdid0RvX3NISXNlLTNiYmx5dTlWdVNvcUVEX2RNNElFeDU5WjlaRTF3a3UzaHBTeXIzZFUxdDFTeDJ1Q1ozdGlJX2FXVmNKSXhaMHV6QVk?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOZXdjMEJSdlpsWVNMV3hya0k1NDRJYXJhZGJoYnZ2VElkUDNxeUh4dF96YVZUak8xaGxfaEVPVm1oOWh6VVFoRzNBLU9ESkxkeDJwQlI1YzhXS3p1dWE3eml2UzdyMTFvbmM4bERmcC1kLWIydm1yS0hRVUZHeTFXNEdETmRuMkwzNjZiRjJBMzBkVm1NSFVLN18xdnNmS203SHRobFRB?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPSHhZLXZ3QWQ5eFRidGdBVDBfeXYteFljWGQ4Uk9PRUxaOHlNWWVXSzdmOVRyX0pmSm91dWV2SmRZa3pGMHpvQjcxTldsd3hSS1pwVWxtclYxUTNOc1hHZkZYa3ZteFlaakJKNGRwUkJaYVQxdUs0c2V1RjEzOU1yUnA5aWN3a0pFUzhBbHZQVWNvd1FUWXNKV1BNZ3dPMm8zWlZn?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPQTVtR182YU9iMFIxRHBBTHlWeFRJTWJmMDI4WWwyWUFmem1IWFBPeTYyY3pKQ3o1bkJBZnVwY0xwZ0ZsRHA2UHNzVGFMTjhiRnRMWEtNY2pJLWxnNm1uLTFpZ1cxdUxpZlVaaWl5d2ZtWlJPY2Q5SERuYWNncEQ3UnFlQkxxVTl3MDhOWA?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxONWdLNmU3ckxKNHE2MUk5ZFdyZ0p1cmlRcjhsUHI4YktvcWN3S2wtb09nT0pZdElRMnVUa3Ewc3FoMU1FTGkzd2FuSlNIVEN0UVVyREFpejFmdTBBSEg1eDdLY2ZjZDljdGNzeVRqVkc3VmtCUkNLRnd0azlXc1hOaGlKNU1ON0lLOUNJTTdGU01tQjNrOWc?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxPRERJcHRpV3FoSUtqN2I0SXk5TGFGYWNjNHZtTGdHaDFuNk9nYklsUlU1WENjMm12OGZzRGZaZ2JoOVQ4cXRiTTA0REdIeWwza0JVSVZ3ZnpKYW5SMFR5X1FuZmNNSnVmUlpSUUM0WHl4c0VKSGVnZ09OeG9KSE5LMFZzSEZQQQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQd1dwa3Y0b2VQWHZTZUpTc05mczN6bWRkTVp2RmwzNjdOOGp2eDdzNG1sd29CNW12QnVBUGVmRk40NHNjYWd3czZhVFdySTljdjNpU2NBV1pJNFE2MnB3T1pJT2thR1E0R25oekQ2T3RrMlJ5N2RHT1RaSm90QmYzdG1BY2Fwd095cW9pcXU2Y9IBxgFBVV95cUxQalBHcnJRa0FEWUhLdGpZb0JxNUo2SUg2X1VYeWgyalZZRTVTU3RQQTl5clQ5TExDZ0RaX05hYXdVYXY5YVFpM0RNeTVQMHVmZjdpbjFGNUxXeTFkTHJNZmEwcldDXzcteWhzT2dGZUJ3S3pQZ1dzVXVnakR0Um5FYmhTeDFUZDdIMUxXY1FreHBGekpFdXdmc3YtNzNvMXJ3VDdPWUtVMXhWZmFibW41NmZDVVpDajc1eHU3aGd1UlhocERGX2c?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
