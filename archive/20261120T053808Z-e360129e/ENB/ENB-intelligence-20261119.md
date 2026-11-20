# ENB Intelligence Report

- ticker: **ENB**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:38:44.324645+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 19, 'rule': 5, 'ai': 12, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/ENB** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 19 unique headlines; 7 named publishers; 0 exact duplicates; 19 HTTPS source links; largest publisher share 21.05%; oldest publication 2026-11-12

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 45.9200 |
| Return 1D (%) | -1.8384 |
| Return 1W (%) | -3.1836 |
| Return 1M (%) | -1.1495 |
| Return YTD (%) | 1.3190 |
| Return 1Y (%) | -0.3273 |
| Annualized volatility (%) | 18.2895 |
| Beta vs SPY | -0.0846 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | 0.0731 |
| Downside deviation (rf=0, %) | 13.0297 |
| Sortino (rf=0) | 0.1027 |
| Historical VaR 95% (1D, %) | 1.8065 |
| Historical ES 95% (1D, %) | 2.5127 |
| Correlation vs SPY | -0.0643 |
| Tracking error vs SPY (%) | 23.6724 |
| P/E (trailing) | 22.51 |
| P/B | 2.37 |
| EV/EBITDA | 12.88 |
| Revenue growth (%) | 44.00 |
| Forward P/E (estimate) | 20.68 |
| Gross margin (%) | 30.20 |
| Operating margin (%) | 12.82 |
| Return on equity (%) | 9.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 46.9900 |
| Close vs MA50 (%) | -2.2772 |
| MA200 | 50.7464 |
| Close vs MA200 (%) | -9.5108 |
| RSI (14, Wilder) | 37.3404 |
| MACD (12,26) | -0.1522 |
| MACD signal (9) | -0.0098 |
| MACD histogram | -0.1424 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 45.9200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.8384 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.1836 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -1.1495 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 1.3190 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -0.3273 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.2895 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.0297 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1027 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8065 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.5127 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0643 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.6724 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0846 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.8462 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0731 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.6757 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.1950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 12.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.8490 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.5098 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 37.3404 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1424 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -2.2772 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -9.5108 -> Clearly below the moving-average trend level.

## TAILWINDS

### Enbridge: A 5.7% Yield With A Growing Cash Flow Engine
- Summary: Enbridge offers a 5.7% yield, backed by growing cash flow, appealing to income-focused investors.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPMS1jMXRwUmtyTHB6ajVMN25ESzBBNkpPb3lTOXhxT2lBXy1Nang5VlFKNXlqamxVZkJLN3FWVkhza25yMnpfRGRKSjNVbEtOVlZWQ0VSRUFYbkVRTzdVcF8tYkZFbzFDRmRjSHNtcGI1c01qcG1OeVlscWdpa0NjOXpYQUFWMkdIMTlhcUgtbGVGeUN3RVFFYXpqdWhPbUlTbWFN?oc=5>

### Enbridge (TSX:ENB) Gets Government Backing For Woodfibre LNG Growth Plans
- Summary: Government backing supports Enbridge’s LNG growth plans, boosting future prospects.
- Date: 2026-11-16 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPZE9OQncyVDhZem5xYUZoOHM2T0t2UGZ5VDhWLUVKUmR1WUxxNV9na25WYWNzVTBsbTUwOGZzUXJDb1NZNXE0MmgxX1RCV0kwYkNLMnFYTVVfc3BCanFZT1NpY3lMb1B6U3lhYWhVSmJMV25YSmx3dGpBSTVQbThrUllHbUUtbThGUkR6dTlMN2VpX2M?oc=5>

## HEADWINDS

### Enbridge shares technical analysis: Trading flat under seller pressure near key support
- Summary: Enbridge shares technical analysis: Trading flat under seller pressure near key support
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPeGxzNTdkZDYwTWc0WUFSQ0pwYzJLS1RMV1lEWGM3eEMtVmFhOTBfTXp4SFpvSl93dUwwZnAyaWpIWXdSYVRUcXhJandYaGtXb1FyWWpDMXktNUJ0dzkzdk83c1dRekctdEFJbk9TRU1VM1lObjZmY2U3bEhPTWp4VTNWeXZ2ZGdjLUJ6Y0RYbnR4aFU?oc=5>

### Enbridge (TSE:ENB) Stock Gets Downgrade from US Capital Advisors
- Summary: Enbridge (TSE:ENB) Stock Gets Downgrade from US Capital Advisors
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPOVJoYW53bkZmYXpUckw3S1RfME9aRmNLZ21OejBXNHRnZ0RfOVA4X2pNbGl0X2d3YkJkSk15cnJ0NVlIUk1TU0N5RGJpMHF0Zzd1MUNLaURGRGZLYS1XWEFXNWkxTHZ2UnlTYlFoMFRnY1ptOG81MGhaWXF2ZWwycm8wYWw3TWluNm9DVl9MVVpxVWY3Q0NxNmRGV3FoVzdFbjByNTA5bDdfRlBhYlo0Z25uZGVEVXp0UGVGdDB5YWkxdw?oc=5>

### Enbridge (TSE:ENB) Share Price Breaks Below Fifty Day Moving Average After Analyst Downgrade
- Summary: Enbridge (TSE:ENB) Share Price Breaks Below Fifty Day Moving Average After Analyst Downgrade
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxOZmYzRUxCYXdVdTlmb1Bnd1BiUFJDUDdEcmVScHp5SnM3OXhYV09hSU5vNjgwek42dGxON1FPZDlyY0FybkpPZHhUUFdIam96MGwtNVJWVjBmelhrelVLdDM4S0E5S1ZIS2dtMUgtYjh5ZkxiZjJSeERfSVN3a08zSzBJYjE5QnhyNjAwY2NDTjh0YWw0Y0JaTWYteHBHMEdERWhqZ0pNYTJ2QUFFcjFxQzZ6RFRIRHpMSzBSdXNNRHFuZTc5OExoR0V4XzFPa1pacllEV0k1cFJJQ2JtNlJENV9IOWQ?oc=5>

### Enbridge: A 32nd Raise Looks Likely, But I Will Wait For A Better Yield (Hold)
- Summary: Potential dividend raise may be delayed, signaling cautious outlook.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPeE0tNzBWUXFDNTloQmhuZkpLbTNLS0hwNFRFV25ZM1pvZk5ocENGTVR0ODZ4bUhmODVWV1o5bUVfUzB5Z0F3c0FXeVlLdjFNTnFYOC1IenN4TXc0bE5RNGxzVWNVZ3UwVHQ4MlRIZzB2ejQwaGdPUko3a01FQkJXRlZTTDFqaHliQnRRYzNBdklIRHJpdkVvU1Y3bWhqVmZlTlBoSHE5MWlrRk5jNHhz?oc=5>

## CATALYSTS

### Enbridge (TSX:ENB) Stock Looks About Right As Acquisition Activity Builds
- Summary: Enbridge (TSX:ENB) Stock Looks About Right As Acquisition Activity Builds
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQSXh0dmJGNGdveTZKcjE3SnljM2ltLUYtaS0wRXZrMEhkSndzVW9jeTNHdjh6OUFOM3RkRzQ2Qk8yajNrQzgzTXV4QUxlQUFCX1dRU0xNM0QyMWphNDFTOXczWVNxdHNKM3VUX3RXUnBBeHBuLXY2anNjem1ic3I0VDFrLVhCVXpUbWFVQUlZNWVRUGc2WFpqYw?oc=5>

### Enbridge Stock: Is It Still a Top Passive Income Pick for Retirees?
- Summary: Enbridge Stock: Is It Still a Top Passive Income Pick for Retirees?
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxNaHJLNGp5dW44UnlHVEhKMmZvazQ0bmJpV2x4bGtlMjM3MURBUHBYSEtpbFJid3hYdkRKZzhiNUJwWnluSWFJLUczNEo2clNxYkx6eEhvSVJzWks4VjU4Q0IydGVVbEZNMlVzWmoyeEdCUFNsbkVKT1JGUlhDQUNVZDdFYUlsUncw?oc=5>

### Enbridge: The Moat Is Holding, But Growth Is Stalling (Rating Downgrade) (NYSE:ENB)
- Summary: Rating downgrade signals potential earnings pressure.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOU0dUd0NGX3lZQzNDRm5mM01aWWEyYjVob0t2NG1mdml2aUlVQ3ZWUERpZUFnN3NlR29uUk03TFMtWWdNM2dEVzEweWt1S1lWb1Vqdlk0cnZYYkFpY3UtdW85ZFVGOTVZdUJ6aDFpZE8wNUIxc1YtZjEyVW5wdG5tczRDazBnWmlnR3Z6N1JzZ2NPVEY2cDlv?oc=5>

### Enbridge management transition and asset deals: Can ENB regain momentum?
- Summary: Management shift and asset deals may boost growth.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNNy1zNDVUM2VubEdEMHM2d1lSNXBlLVBKOWpqSHRRSkNnbmJVMnRpU2FjR3lLaFEtTW5GTWQ0a2UtaHpQYkR3WWF1Y09XRVdaRDk2dVZHeVdnRHVSM3RXbElYMWx6aTE5dFlGZGFfWWxYdlY2LVFybGtYRG5KT0N6R0hjTzdnRk5EUTVlUEVROUFlWXM?oc=5>

### Enbridge's North Dakota pipeline system shut over contamination concerns - Argus (ENB:NYSE)
- Summary: Pipeline shutdown raises operational risk.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxORTBsOUFTNmxkZWFfSkExdXE3NVNRWFg2TlAtZk9rNld0Q0prSWxIb2FWU3ZDQUhjclgzOENUcWpLSlhZaVFzWlU3RDM0VU9qYldWa3lMSGVMM0hKNjNqMG1kNnZiRmp5VmFHdHZjM01QT0Y2cE12N3U5RnBtNkpXakhORTdRdXI4X3V6SFVGUFZsTTQ5Tzg5a3c2QnpQVHJkVzU1ME1hZ3JNSW9IRi1mMUFRSTVFQQ?oc=5>

### Enbridge stock: company completes US dollar 1.1 billion notes
- Summary: Debt issuance increases financial leverage.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNLTdhNk5sYVE2dWRvZmRsbUx0OFh4emNIUXJhYTdZOFdfVC1PVVhWNWpuQXNhb1RuN1ZmbWdGemVDcVN2Z3c4QlVhRkxpWHk0NWNUTl84WUxVZlNhSFNldnpjeWozZ1Joc1YyblF5eGdrWEJ2UE0xWlQwdzg5Mlh3ZF8wZ1doWmdjOWx4Q05BRjhCUVRaR1lfYmlUc1RHSjA3MW40R25mNG0zU1MxUlYxU1g0a29PMVVHclYxZGZBZGo?oc=5>

### Enbridge stock completes subordinated note offering
- Summary: Enbridge has finished issuing subordinated notes, raising capital to support its operations and future projects.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOMnZra0xCWVlNUm1UeGdXN1JQRVZNTTRJdFZMTWlLcFNaWWVkZ1ZqVXJoZVFsWnkwaHZFSWR2VFpEZWJlQnpBUFRIeFNYTWFzaGpWTy1qaXJKTTl2VlNIX0lBOTBPTGUxZ3IzUlVOQ3o3UHFudlhjdWNkV0ZtcnZWci1YZGh5WFJFV2dSQ3A4SThodUNJemFIMUlCNjZYVTdrYnpseV9ZV1BYUllIZ19rdWtTNmU?oc=5>

### Enbridge: My Verdict Is Buy – Here’s the Dividend $6,000 Would Collect
- Summary: Analyst recommends buying Enbridge, citing attractive dividend potential.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxNVXlpWFk4TDVSdDM5cUJrT0Y1Tm1yZkdlbUhFTDJaSHR6eG91bjNZb0NUeDRpUmJld3V5WDc0bngyN05qQlRacDYyM3Q2UHhPaDdzWEhIOFNwdEJPeUxhQlZnbUtfOU5OYXRHam1ZcF9XQ01ET2F0NHFvbmlnWnJoVFNIQVJwaUxvZGhNRkt6bXpsTzR4VVNHY3lfQ2Y3YlVLQWpfbG9uV3VZX0Y2RkEwUVVvVFpOcUx1QUFGdHE2Vk9ULVZkVXktVnRyQ3NWdGtEeDNtLUpxYlI2bW5XTDI5OURGTGc?oc=5>

### Enbridge (NYSE:ENB) Stock Rating Cut to Hold at US Capital Advisors
- Summary: US Capital Advisors downgrades Enbridge to Hold, reducing bullish outlook.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxONGE1WFp1a1ZlTmFPV2lEYVlFM1I2VXNGYS1PVWlqTmJjX2RJVzZZWi00ZzR1ZWRRaktwVFlFRkNBM3F1dGdUQXpNaDVRTjBPVVVQWmRQLTdRRjRTV0IyVFhSc1U3WVIyaHNMSkFSYWVRcE1OLUh3QldtX29lelpEUHEwQkMtYnFFam9YcGlCcE1UdnpLWWNyUTZzaGpjb3dsbzRQejd2bHl0Z3hLMHdyUWhMbTE5c0tVUnVsdW53ZEE0WXNvZ2c?oc=5>

### Enbridge stock: US Capital Advisors trims FY2028 EPS view
- Summary: US Capital Advisors lowers Enbridge EPS forecast for FY2028.
- Date: 2026-11-19 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQek5XWWZuQncxdHEyaWtZT2t2ekJyUm5lZDE5enE2TFdYdXo0QXgxRHExYXdvcE53dHdEYkYwMDFJdVRXNmlFeUtab1VIQXJmZjBVYkY5dWZJNmVIaktQcUFzbFFzNENmcmp2YnVHLWxyUjU3Q1hrVHozMFRoNUJYVEhqcG53NXdhelVKRXJVRTVqb0RYQXcyaURBanpFWEwyMEgtaGR4czZoQlpKR1ZOWHhDc1BwemdLMDFR?oc=5>

### Enbridge stock cut to Hold by US Capital Advisors
- Summary: Enbridge downgraded to Hold by US Capital Advisors.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQWjhxMzFaWnAyM3hlTzR0WFNEYnRveFVmN3JFeURnNHhlUkJNb0dtM29zTGMwdEZ5cUFJSWNudy1yWVVCNUZndmJpamRBWm1zTVoxdnJZS3ZHV3dWVTJJUHlRVjhBWHZwUS1UaW56b05SNEdzamg3Q1BHZ25Hb1ZYZWhWdWRGUmw2OVNnY3k4bkR1YjFjWGdiQ2dFb0M3Zm9WUVNCbzk0TWdEQ3JnYmlGN0l3?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **22.51** | **2.37** | **12.88** | **44.00** | **102,350,536,704.00 USD** | **-0.33** |
| TRP.TO | 24.29 | 3.67 | 16.53 | 8.80 | 93,873,618,944.00 CAD | 22.17 |
| KMI | 19.31 | 2.19 | 13.41 | 9.30 | 69,259,673,600.00 USD | 20.29 |
| EPD | 11.97 | 2.57 | 10.66 | 49.30 | 77,982,834,688.00 USD | 21.02 |

Peers fetched as_of: 2026-11-19; ENB reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-06
- Next expected earnings: 2027-02-12 (yfinance; expected dates may change)

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
- Filing date: 2026-11-06
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/895728/000119312526450714/enb-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiowFBVV95cUxPMS1jMXRwUmtyTHB6ajVMN25ESzBBNkpPb3lTOXhxT2lBXy1Nang5VlFKNXlqamxVZkJLN3FWVkhza25yMnpfRGRKSjNVbEtOVlZWQ0VSRUFYbkVRTzdVcF8tYkZFbzFDRmRjSHNtcGI1c01qcG1OeVlscWdpa0NjOXpYQUFWMkdIMTlhcUgtbGVGeUN3RVFFYXpqdWhPbUlTbWFN?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPZE9OQncyVDhZem5xYUZoOHM2T0t2UGZ5VDhWLUVKUmR1WUxxNV9na25WYWNzVTBsbTUwOGZzUXJDb1NZNXE0MmgxX1RCV0kwYkNLMnFYTVVfc3BCanFZT1NpY3lMb1B6U3lhYWhVSmJMV25YSmx3dGpBSTVQbThrUllHbUUtbThGUkR6dTlMN2VpX2M?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPeGxzNTdkZDYwTWc0WUFSQ0pwYzJLS1RMV1lEWGM3eEMtVmFhOTBfTXp4SFpvSl93dUwwZnAyaWpIWXdSYVRUcXhJandYaGtXb1FyWWpDMXktNUJ0dzkzdk83c1dRekctdEFJbk9TRU1VM1lObjZmY2U3bEhPTWp4VTNWeXZ2ZGdjLUJ6Y0RYbnR4aFU?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPOVJoYW53bkZmYXpUckw3S1RfME9aRmNLZ21OejBXNHRnZ0RfOVA4X2pNbGl0X2d3YkJkSk15cnJ0NVlIUk1TU0N5RGJpMHF0Zzd1MUNLaURGRGZLYS1XWEFXNWkxTHZ2UnlTYlFoMFRnY1ptOG81MGhaWXF2ZWwycm8wYWw3TWluNm9DVl9MVVpxVWY3Q0NxNmRGV3FoVzdFbjByNTA5bDdfRlBhYlo0Z25uZGVEVXp0UGVGdDB5YWkxdw?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxOZmYzRUxCYXdVdTlmb1Bnd1BiUFJDUDdEcmVScHp5SnM3OXhYV09hSU5vNjgwek42dGxON1FPZDlyY0FybkpPZHhUUFdIam96MGwtNVJWVjBmelhrelVLdDM4S0E5S1ZIS2dtMUgtYjh5ZkxiZjJSeERfSVN3a08zSzBJYjE5QnhyNjAwY2NDTjh0YWw0Y0JaTWYteHBHMEdERWhqZ0pNYTJ2QUFFcjFxQzZ6RFRIRHpMSzBSdXNNRHFuZTc5OExoR0V4XzFPa1pacllEV0k1cFJJQ2JtNlJENV9IOWQ?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPeE0tNzBWUXFDNTloQmhuZkpLbTNLS0hwNFRFV25ZM1pvZk5ocENGTVR0ODZ4bUhmODVWV1o5bUVfUzB5Z0F3c0FXeVlLdjFNTnFYOC1IenN4TXc0bE5RNGxzVWNVZ3UwVHQ4MlRIZzB2ejQwaGdPUko3a01FQkJXRlZTTDFqaHliQnRRYzNBdklIRHJpdkVvU1Y3bWhqVmZlTlBoSHE5MWlrRk5jNHhz?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQSXh0dmJGNGdveTZKcjE3SnljM2ltLUYtaS0wRXZrMEhkSndzVW9jeTNHdjh6OUFOM3RkRzQ2Qk8yajNrQzgzTXV4QUxlQUFCX1dRU0xNM0QyMWphNDFTOXczWVNxdHNKM3VUX3RXUnBBeHBuLXY2anNjem1ic3I0VDFrLVhCVXpUbWFVQUlZNWVRUGc2WFpqYw?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxNaHJLNGp5dW44UnlHVEhKMmZvazQ0bmJpV2x4bGtlMjM3MURBUHBYSEtpbFJid3hYdkRKZzhiNUJwWnluSWFJLUczNEo2clNxYkx6eEhvSVJzWks4VjU4Q0IydGVVbEZNMlVzWmoyeEdCUFNsbkVKT1JGUlhDQUNVZDdFYUlsUncw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOU0dUd0NGX3lZQzNDRm5mM01aWWEyYjVob0t2NG1mdml2aUlVQ3ZWUERpZUFnN3NlR29uUk03TFMtWWdNM2dEVzEweWt1S1lWb1Vqdlk0cnZYYkFpY3UtdW85ZFVGOTVZdUJ6aDFpZE8wNUIxc1YtZjEyVW5wdG5tczRDazBnWmlnR3Z6N1JzZ2NPVEY2cDlv?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNNy1zNDVUM2VubEdEMHM2d1lSNXBlLVBKOWpqSHRRSkNnbmJVMnRpU2FjR3lLaFEtTW5GTWQ0a2UtaHpQYkR3WWF1Y09XRVdaRDk2dVZHeVdnRHVSM3RXbElYMWx6aTE5dFlGZGFfWWxYdlY2LVFybGtYRG5KT0N6R0hjTzdnRk5EUTVlUEVROUFlWXM?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxORTBsOUFTNmxkZWFfSkExdXE3NVNRWFg2TlAtZk9rNld0Q0prSWxIb2FWU3ZDQUhjclgzOENUcWpLSlhZaVFzWlU3RDM0VU9qYldWa3lMSGVMM0hKNjNqMG1kNnZiRmp5VmFHdHZjM01QT0Y2cE12N3U5RnBtNkpXakhORTdRdXI4X3V6SFVGUFZsTTQ5Tzg5a3c2QnpQVHJkVzU1ME1hZ3JNSW9IRi1mMUFRSTVFQQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNLTdhNk5sYVE2dWRvZmRsbUx0OFh4emNIUXJhYTdZOFdfVC1PVVhWNWpuQXNhb1RuN1ZmbWdGemVDcVN2Z3c4QlVhRkxpWHk0NWNUTl84WUxVZlNhSFNldnpjeWozZ1Joc1YyblF5eGdrWEJ2UE0xWlQwdzg5Mlh3ZF8wZ1doWmdjOWx4Q05BRjhCUVRaR1lfYmlUc1RHSjA3MW40R25mNG0zU1MxUlYxU1g0a29PMVVHclYxZGZBZGo?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOMnZra0xCWVlNUm1UeGdXN1JQRVZNTTRJdFZMTWlLcFNaWWVkZ1ZqVXJoZVFsWnkwaHZFSWR2VFpEZWJlQnpBUFRIeFNYTWFzaGpWTy1qaXJKTTl2VlNIX0lBOTBPTGUxZ3IzUlVOQ3o3UHFudlhjdWNkV0ZtcnZWci1YZGh5WFJFV2dSQ3A4SThodUNJemFIMUlCNjZYVTdrYnpseV9ZV1BYUllIZ19rdWtTNmU?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxNVXlpWFk4TDVSdDM5cUJrT0Y1Tm1yZkdlbUhFTDJaSHR6eG91bjNZb0NUeDRpUmJld3V5WDc0bngyN05qQlRacDYyM3Q2UHhPaDdzWEhIOFNwdEJPeUxhQlZnbUtfOU5OYXRHam1ZcF9XQ01ET2F0NHFvbmlnWnJoVFNIQVJwaUxvZGhNRkt6bXpsTzR4VVNHY3lfQ2Y3YlVLQWpfbG9uV3VZX0Y2RkEwUVVvVFpOcUx1QUFGdHE2Vk9ULVZkVXktVnRyQ3NWdGtEeDNtLUpxYlI2bW5XTDI5OURGTGc?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxONGE1WFp1a1ZlTmFPV2lEYVlFM1I2VXNGYS1PVWlqTmJjX2RJVzZZWi00ZzR1ZWRRaktwVFlFRkNBM3F1dGdUQXpNaDVRTjBPVVVQWmRQLTdRRjRTV0IyVFhSc1U3WVIyaHNMSkFSYWVRcE1OLUh3QldtX29lelpEUHEwQkMtYnFFam9YcGlCcE1UdnpLWWNyUTZzaGpjb3dsbzRQejd2bHl0Z3hLMHdyUWhMbTE5c0tVUnVsdW53ZEE0WXNvZ2c?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQek5XWWZuQncxdHEyaWtZT2t2ekJyUm5lZDE5enE2TFdYdXo0QXgxRHExYXdvcE53dHdEYkYwMDFJdVRXNmlFeUtab1VIQXJmZjBVYkY5dWZJNmVIaktQcUFzbFFzNENmcmp2YnVHLWxyUjU3Q1hrVHozMFRoNUJYVEhqcG53NXdhelVKRXJVRTVqb0RYQXcyaURBanpFWEwyMEgtaGR4czZoQlpKR1ZOWHhDc1BwemdLMDFR?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQWjhxMzFaWnAyM3hlTzR0WFNEYnRveFVmN3JFeURnNHhlUkJNb0dtM29zTGMwdEZ5cUFJSWNudy1yWVVCNUZndmJpamRBWm1zTVoxdnJZS3ZHV3dWVTJJUHlRVjhBWHZwUS1UaW56b05SNEdzamg3Q1BHZ25Hb1ZYZWhWdWRGUmw2OVNnY3k4bkR1YjFjWGdiQ2dFb0M3Zm9WUVNCbzk0TWdEQ3JnYmlGN0l3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
