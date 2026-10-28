# ISRG Intelligence Report

- ticker: **ISRG**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/ISRG/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ISRG/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T01:58:33.857949+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 6, 'ai': 8, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261026T005504Z-6368ad31/ISRG** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 11 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 445.8800 |
| Return 1D (%) | -1.2732 |
| Return 1W (%) | 1.7991 |
| Return 1M (%) | 10.0449 |
| Return YTD (%) | -21.2727 |
| Return 1Y (%) | -19.1147 |
| Annualized volatility (%) | 33.9921 |
| Beta vs SPY | 0.8768 |
| Max drawdown (%) | -43.9960 |
| Sharpe (rf=0) | -0.4541 |
| Downside deviation (rf=0, %) | 25.6601 |
| Sortino (rf=0) | -0.6016 |
| Historical VaR 95% (1D, %) | 2.8853 |
| Historical ES 95% (1D, %) | 5.0452 |
| Correlation vs SPY | 0.3276 |
| Tracking error vs SPY (%) | 32.1543 |
| P/E (trailing) | 53.92 |
| P/B | 9.67 |
| EV/EBITDA | 33.70 |
| Revenue growth (%) | 21.70 |
| Forward P/E (estimate) | 35.81 |
| Gross margin (%) | 66.64 |
| Operating margin (%) | 33.29 |
| Return on equity (%) | 17.93 |
| Free cash flow yield (%) | 2.18 |
| MA50 | 398.3118 |
| Close vs MA50 (%) | 11.9425 |
| MA200 | 434.8429 |
| Close vs MA200 (%) | 2.5382 |
| RSI (14, Wilder) | 65.6162 |
| MACD (12,26) | 14.0000 |
| MACD signal (9) | 12.3696 |
| MACD histogram | 1.6304 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ISRG': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 445.8800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.2732 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.7991 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 10.0449 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -21.2727 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -19.1147 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.9921 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.6601 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.6016 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8853 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.0452 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3276 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.1543 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8768 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.9960 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.4541 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 35.8081 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.6420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.2860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.9320 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.1806 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 53.9154 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 65.6162 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.6304 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 11.9425 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 2.5382 -> Slightly above the moving-average trend level.

## TAILWINDS

### Intuitive Surgical (ISRG) Could Be 24% Above Fair Value As Earnings Split The Market
- Summary: Earnings suggest ISRG may be undervalued, indicating potential upside.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNSGxRNkt3UTdSSmFBX2wzamstRjdPamFrWHVmdmtQZ3R1bGRtUVRPWUFDRkJDSHFJQUpENzdzc2x0bUkyek1TWUN1TkNrY0ROdUI1QkdpMDdtWENqWUcxZjR3V2JQM1NqODlOTTkwMXdhSVRxV3NnMkJEYm1DZTF1bTlsci1sZkFuMzJjWjROa1AyZGZLOVVrSGJRd012azA4VWpxWm81cnhRM0g5RU1wblVWa1lMR3pqeXdsd1FYa3FHNGQyYmtiWWRMVlRlZkNKeF9TWjFR0gHbAUFVX3lxTE9kRDlUbzNEbmFlU0REd1E2bkFyQ3YxNzRScjlGbDYtR1NiSnh2TDJEcWdTelFpRXl6bkt6eFlzc0xxT011S2wzM191WU5wTEdfNGF4TnNTSGNxa1dLUlVHSURMNG13b3JZc0RDQzJtNlpLcDlyVUJZRVZ3MzZaQnJtZmEzeWFFd3NYSFluSE4yNXdDdFNMR2xpUTh6VEtDS1Y5YUhlbEpSQXZPZ2gtM0lEdUVCMGRTU1k2MEZyaWUxQk9pdmgyTU5LdEJpU3ZieWJsUkc1RXd2enhNaw?oc=5>

## HEADWINDS

### Intuitive Surgical (NASDAQ:ISRG) Reports Upbeat Q3 2026 But Stock Drops 12.7%
- Summary: Intuitive Surgical (NASDAQ:ISRG) Reports Upbeat Q3 2026 But Stock Drops 12.7%
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPWTRFbm43RUZrNnpvUXBvWW5mZnh1bTBqVHlrMFRQbWdmM1dvYkZGUHR1aHJhUG0xbW05TExUZC1odXVIWUZNMmlNakRsb0J4WkJIN2FQcGVydGdxN3owVGJMNmJwLThiZEVxQ2prYTJvUnRlS1p2QzF4aENVMl9JWGc2d2NNWmY0ekJEYUQxcGhFVWpDUUI5MjFHSE1LWnN6Qm12bWtn?oc=5>

### Intuitive Surgical stock drops after Q3 beat (ISRG:NASDAQ)
- Summary: Intuitive Surgical stock drops after Q3 beat (ISRG:NASDAQ)
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxOaHNmbUs4MTcwdVdmcVQ5cTFraThfY0xXTFdpbzkwMVU2R050cTdVRndfR05uSTMwYXltanJHOFhRcXFsLTBweGpGY0txS2l6MDQ3STc4U2xTMzFDN2NXTVlZRExDbldkRnVaa1pUZUp5dlZ2d2UtdkdNMU9Oc3d5dlJ3?oc=5>

### Intuitive Surgical slides 13% as earnings hit by pre-tax charge
- Summary: Intuitive Surgical slides 13% as earnings hit by pre-tax charge
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQcUlHMmEzU1U1eGkwZnk3OXk4b002MkkyTVRwYmI5UU91Zjhkd1VzX3BtNHJLeXNLYlJ0RkJRMW5MMmFWYTZEZ1JudnBwMlptYjcxdXpSdkdRMU9Za1hibDJ2OEtWVGxhbjU5N2pxdlZzNlFFNDRQaUswTUNUODNKTk1oR3BRZndIUW1zR1FhM21kZXZYZW9WNHFmbDloLWlUTkVJTlUta1NiZEFFQ1V1U09zbTg?oc=5>

### ISRG, NFLX, ACN Stocks Slide Before The Bell: Why Intuitive Surgical, Netflix And Accenture Are Heading Lower
- Summary: Pre-market decline signals short-term negative sentiment for ISRG.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPUkZ5UXVsZjJXaGVOT3Z1RkR2TmdDb2xMQ0JNNWJpY2dTX3ZtNFNRVUVVckVReTR2ZGhlUUFtSXl5UElKZE55dnFYdHplX3NkQXVOU1lQcVkySzYyWGo5UFFaaGJadGpjRGRENHVnd0MwVW9KN0dzcm9qdWloZmpVeXAtUXY5ZnJHUE1nX0pyTlptMDZvRFE?oc=5>

### Intuitive Surgical Insider Sold Shares Worth $1,834,124, According to a Recent SEC Filing
- Summary: Insider selling may indicate management concerns about ISRG's prospects.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNWXBYLXU5eHRVeFphS2NhSXpOdXlfc2tldkhQZXRNVlMzTUFSM1VjNGRhU3lRbnJoZ2x6NUg0SVFwaV80cnVpcnlUVW56SGxrT2dQZkJjT1c1ZzNtcl9aVlBSQlJiM1UtQWdiOFBzNlVpSHpycVpfY1NCSlE0N2lsbUJUZGtmNGVSUWs2YzdmeVNLTGQySlliZktyX0NzVThMRTRtTDFFY3NwN25GbEFCdg?oc=5>

### Intuitive Surgical Stock: Margin Hit Masks Strong Q3 Growth Story
- Summary: Margin pressure tempers enthusiasm for ISRG's growth narrative.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQb0YxRUpVLUV3YmkzTENaOURoUUdTbjducXNsdHFzcHNJM3VKT0Vhem1ISUJHZXBFa1FCSzhzcmNtRVhYSEN1MzRjRE5heV9kZ3RWZkVvNnVTck1VSzBaZXNTSXM2d0NUcWp3R0hveHRwVU5QNENNYi15cjRoX1lOcXMySkp6TkJtMFpVWlNQclZ6XzhHWWx1VjU3Z3ViemxXNGV0TEF6VHM4bUg3d3k1dGhXc1FBS1dzbV9VTVdadHBoUQ?oc=5>

## CATALYSTS

### Intuitive Surgical (ISRG) Stock Faces A Q3 Earnings Valuation Reality Check
- Summary: Intuitive Surgical (ISRG) Stock Faces A Q3 Earnings Valuation Reality Check
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQU0JGbU5VQ1dmVmRnVi1URXY3VWpxT3otdU9LUzRhRm9xZUlzbGlzR3VGSFB6VDI1WHk3SlNsa2x2MjFrbVduQ2R3SVY3bVIwdUg1Z2VyQ3ZxaUVkN0dEMVlTUzhQUlV2TjVfNjVnLXE5WjNvY0FPbnA1MHNqRHNMR2UxSDhnYUM5SXZTdHZwdmhlY3lGSUgwYjZXU0dZdlI4Zmc?oc=5>

### Intuitive Surgical, Inc. 2026 Q3 - Results - Earnings Call Presentation (NASDAQ:ISRG) 2026-10-23
- Summary: Intuitive Surgical, Inc. 2026 Q3 - Results - Earnings Call Presentation (NASDAQ:ISRG) 2026-10-23
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTmpjcE5OT1pBOXJ4aGFzZkhja3VhUi1TcV9tNEI0cUd1TVVUeHF1ZzlNczhHWUplMkZqQXhHNDBELVdXTVZXU24yaHRVRTVPa0JTQW9tZnRadXN1MGNVTWhrQU5zUFcwZ2JaRVZNbFNQcHhNdkpJX0tNRTRhRzNUNUJON2pzY01DQ2ZUMVRlZkVGMmNTdmFMZFRuM1hpelpWVDRzUHdGQjBRZw?oc=5>

### Intuitive Surgical (ISRG) Insider Sale: SVP Chief Human Resource
- Summary: Intuitive Surgical (ISRG) Insider Sale: SVP Chief Human Resource
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxQamx6UHcwVVd0Uno3aVhvcHc4c291YWl0N08wZlViSnFfYTRMTmFPa1VVcnlRd0lpREg4QVd2MXlHeDNNanpqQTF0eEdnTWVia3FoRUEwXzkwWFFFWGpDUFB3UGlWWmFCZC1Zd0FUZjdTcVlCcFRQSTFFdktYTmRMNW81SVhISmZVaHAxSWhSUnJMNUx2Wm5jckFhOGNsM2l4WG9LSXZOOXNXR2ExQnhQLWhrSjB0cEczQzlHYk5OaTRnSjJWcTB6Mzhtb2dKWl82d0hBVW85YTdGNEdrV0VGeVFtZkt0aEJHbDNR?oc=5>

### Intuitive Surgical Q3: The Best Way To Grow May Be To Charge Less (NASDAQ:ISRG)
- Summary: Intuitive Surgical reports Q3 results, suggesting growth strategy may involve pricing adjustments to boost revenue.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNYkxpeXRwTS1ZRVhrQzVyN01NUW56cWk5Sk9IUWkxMkRmRmRtdGp2QjQtZF9NVk1vTWJJMlZtY2Jla3V1Q3B0Ul9WeTRGeWxDVkNoaGVmOFZTZ0RZemxiTk5iR1IxVzRsRmdjeE5EYXlEWVBiSG1JdUJLVk0yMkhOZTVlRmtfTTZxSGZ5Q01pMWRRYkpocHMzcWlsN1daT1I5b0ZBMlBoWWw?oc=5>

### Intuitive Surgical (ISRG) Shares Dip Despite Strong Q3 Results o
- Summary: Shares fell after Q3 earnings, despite strong results, indicating market concerns about future growth.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPVElCY21walNRbE1pRW15Wkx4ZnlZelNFamRpbC04cEdlTVBzejFYdGVqU2V5THhCOUFfSjBmTUk1NGR3RWVQQm80ZGxHb3F2TzYza2swN1RrSDdybllxbE9CSHF2aWtYbnl5czZDTnhmRllQeTllMWo0MVZ3cmVEelJ5ZjJ6dWFiQi1teFJ3aVlFZHJmclpOSEJuSE12cjdLakdWeVphZXV0cWZZZHFQRnowVy1zeDdQ?oc=5>

### Intuitive Surgical (ISRG) Stock Looks Reasonable After Mixed Q3 Results
- Summary: Mixed Q3 results prompt a reassessment of ISRG’s valuation, suggesting a reasonable price target for investors.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxOdDRpdU9FbjgxbEJxbHVOSy1wTE9UazRNSG1Nc3AwaXRSTUJQR2lISUhyNzltWUZ6MWpFRXlRVWZkMk5uc2xZYnNkSXEzWUFoZUh0MEdiZTVwVVoxU190cmk5WGNUMlRyUTZxLXBIaTNDSUhybG9JRzFmcU5ibDNNenZRc1N0UUJCNmhwMXIwZFV3alpRalFpSmtjTkVfdFYtMUl5YWNFbXZUek5WMWlvZmFkb3ZyenhLMDlxSVkxck1JeDNMXzY3dE9nRWpMd2tGTEN4V0pB0gHbAUFVX3lxTFBEcm1NRjkyem5SRk52RVN6dUdBNHhDRXBXWnZNUzJJU0NadVNZWFFVR3ZMdGwyWVcwVENFd3N3RHB1bVlDV3FNMGRtT28yeUdHSjNzcC1mT0NfV3VEWFowbTE2WVpOUlFValduNnRBT0F4UFgydWNfQXpwVUVLVTZGc2Zvckh6ZDJJc1Yxeng4eUFiVkNiaHZDNlZDUzlKNWhzNmdydlpsc2JUc2lXRDM4bEFMLTNZSkJ6MWdHNHRHZllTN29rLU40T3c4bGNrekNaWG5TLUR2UEMwdw?oc=5>

## RISKS

### Robotics Titan Hammered On Elevated Buy-Side Views
- Summary: Elevated buy-side expectations lead to a sharp decline in ISRG shares, indicating potential downside risk.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPbFQ1cWh6R3FnQ3BUZWJlMHNqazZUeExEN1RkQUMzeDBPcHgyOGxfZHI2eV82RkxQcWVXV2h2MDVOcWZaeGNEOEZDN29GcmdLTDR2S1lMaHpoTDFGQ1VjYTBxS010bkZGbmV1aGxmSW5tcFEyUTFzb3FrQno2aE5WV1JDMHlaU2FndDVRNHZYYkZ1alV3eWQ4RHEyb0ZCWnEtZlJmaDl3?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ISRG** | **53.92** | **9.67** | **33.70** | **21.70** | **157,519,609,856.00 USD** | **-19.11** |
| MDT | 23.08 | 2.39 | 13.46 | 13.70 | 120,175,001,600.00 USD | 3.12 |
| SYK | 31.24 | 4.82 | 17.30 | 9.40 | 115,616,595,968.00 USD | -20.58 |
| BSX | 18.24 | 2.61 | 13.59 | 7.50 | 65,302,286,336.00 USD | -56.01 |

Peers fetched as_of: 2026-10-27; ISRG reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNSGxRNkt3UTdSSmFBX2wzamstRjdPamFrWHVmdmtQZ3R1bGRtUVRPWUFDRkJDSHFJQUpENzdzc2x0bUkyek1TWUN1TkNrY0ROdUI1QkdpMDdtWENqWUcxZjR3V2JQM1NqODlOTTkwMXdhSVRxV3NnMkJEYm1DZTF1bTlsci1sZkFuMzJjWjROa1AyZGZLOVVrSGJRd012azA4VWpxWm81cnhRM0g5RU1wblVWa1lMR3pqeXdsd1FYa3FHNGQyYmtiWWRMVlRlZkNKeF9TWjFR0gHbAUFVX3lxTE9kRDlUbzNEbmFlU0REd1E2bkFyQ3YxNzRScjlGbDYtR1NiSnh2TDJEcWdTelFpRXl6bkt6eFlzc0xxT011S2wzM191WU5wTEdfNGF4TnNTSGNxa1dLUlVHSURMNG13b3JZc0RDQzJtNlpLcDlyVUJZRVZ3MzZaQnJtZmEzeWFFd3NYSFluSE4yNXdDdFNMR2xpUTh6VEtDS1Y5YUhlbEpSQXZPZ2gtM0lEdUVCMGRTU1k2MEZyaWUxQk9pdmgyTU5LdEJpU3ZieWJsUkc1RXd2enhNaw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPWTRFbm43RUZrNnpvUXBvWW5mZnh1bTBqVHlrMFRQbWdmM1dvYkZGUHR1aHJhUG0xbW05TExUZC1odXVIWUZNMmlNakRsb0J4WkJIN2FQcGVydGdxN3owVGJMNmJwLThiZEVxQ2prYTJvUnRlS1p2QzF4aENVMl9JWGc2d2NNWmY0ekJEYUQxcGhFVWpDUUI5MjFHSE1LWnN6Qm12bWtn?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxOaHNmbUs4MTcwdVdmcVQ5cTFraThfY0xXTFdpbzkwMVU2R050cTdVRndfR05uSTMwYXltanJHOFhRcXFsLTBweGpGY0txS2l6MDQ3STc4U2xTMzFDN2NXTVlZRExDbldkRnVaa1pUZUp5dlZ2d2UtdkdNMU9Oc3d5dlJ3?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQcUlHMmEzU1U1eGkwZnk3OXk4b002MkkyTVRwYmI5UU91Zjhkd1VzX3BtNHJLeXNLYlJ0RkJRMW5MMmFWYTZEZ1JudnBwMlptYjcxdXpSdkdRMU9Za1hibDJ2OEtWVGxhbjU5N2pxdlZzNlFFNDRQaUswTUNUODNKTk1oR3BRZndIUW1zR1FhM21kZXZYZW9WNHFmbDloLWlUTkVJTlUta1NiZEFFQ1V1U09zbTg?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPUkZ5UXVsZjJXaGVOT3Z1RkR2TmdDb2xMQ0JNNWJpY2dTX3ZtNFNRVUVVckVReTR2ZGhlUUFtSXl5UElKZE55dnFYdHplX3NkQXVOU1lQcVkySzYyWGo5UFFaaGJadGpjRGRENHVnd0MwVW9KN0dzcm9qdWloZmpVeXAtUXY5ZnJHUE1nX0pyTlptMDZvRFE?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNWXBYLXU5eHRVeFphS2NhSXpOdXlfc2tldkhQZXRNVlMzTUFSM1VjNGRhU3lRbnJoZ2x6NUg0SVFwaV80cnVpcnlUVW56SGxrT2dQZkJjT1c1ZzNtcl9aVlBSQlJiM1UtQWdiOFBzNlVpSHpycVpfY1NCSlE0N2lsbUJUZGtmNGVSUWs2YzdmeVNLTGQySlliZktyX0NzVThMRTRtTDFFY3NwN25GbEFCdg?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQb0YxRUpVLUV3YmkzTENaOURoUUdTbjducXNsdHFzcHNJM3VKT0Vhem1ISUJHZXBFa1FCSzhzcmNtRVhYSEN1MzRjRE5heV9kZ3RWZkVvNnVTck1VSzBaZXNTSXM2d0NUcWp3R0hveHRwVU5QNENNYi15cjRoX1lOcXMySkp6TkJtMFpVWlNQclZ6XzhHWWx1VjU3Z3ViemxXNGV0TEF6VHM4bUg3d3k1dGhXc1FBS1dzbV9VTVdadHBoUQ?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxQTGFHWDBOTUw5azNzSmpLUlVpeEg0U1FsaUZqY2p6by1wUllXZi1lNHZjOVZsOWdyN2VIQlltV1Z3amxYckFxMGlVTlQzeWxaRVVNZzA5RkMxZm1hUm95MDJSOWxjZUFxaHQ2QmRYMHhMc1ZUQnFQWThCMEZZUHl4US1EaksybTZfZTFQNFRtNUFyMjJmTHN1d3ZIdTduQndXRGdSZFdPS3doMjVYM0RRVmhQczBTMkZlTGpWSm5PdFhWaGJ2UFNydVN6dC0yRXVBZ0tHaW41bWRWOGRaS2dxYmRjRGE?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQU0JGbU5VQ1dmVmRnVi1URXY3VWpxT3otdU9LUzRhRm9xZUlzbGlzR3VGSFB6VDI1WHk3SlNsa2x2MjFrbVduQ2R3SVY3bVIwdUg1Z2VyQ3ZxaUVkN0dEMVlTUzhQUlV2TjVfNjVnLXE5WjNvY0FPbnA1MHNqRHNMR2UxSDhnYUM5SXZTdHZwdmhlY3lGSUgwYjZXU0dZdlI4Zmc?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTmpjcE5OT1pBOXJ4aGFzZkhja3VhUi1TcV9tNEI0cUd1TVVUeHF1ZzlNczhHWUplMkZqQXhHNDBELVdXTVZXU24yaHRVRTVPa0JTQW9tZnRadXN1MGNVTWhrQU5zUFcwZ2JaRVZNbFNQcHhNdkpJX0tNRTRhRzNUNUJON2pzY01DQ2ZUMVRlZkVGMmNTdmFMZFRuM1hpelpWVDRzUHdGQjBRZw?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxQamx6UHcwVVd0Uno3aVhvcHc4c291YWl0N08wZlViSnFfYTRMTmFPa1VVcnlRd0lpREg4QVd2MXlHeDNNanpqQTF0eEdnTWVia3FoRUEwXzkwWFFFWGpDUFB3UGlWWmFCZC1Zd0FUZjdTcVlCcFRQSTFFdktYTmRMNW81SVhISmZVaHAxSWhSUnJMNUx2Wm5jckFhOGNsM2l4WG9LSXZOOXNXR2ExQnhQLWhrSjB0cEczQzlHYk5OaTRnSjJWcTB6Mzhtb2dKWl82d0hBVW85YTdGNEdrV0VGeVFtZkt0aEJHbDNR?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNYkxpeXRwTS1ZRVhrQzVyN01NUW56cWk5Sk9IUWkxMkRmRmRtdGp2QjQtZF9NVk1vTWJJMlZtY2Jla3V1Q3B0Ul9WeTRGeWxDVkNoaGVmOFZTZ0RZemxiTk5iR1IxVzRsRmdjeE5EYXlEWVBiSG1JdUJLVk0yMkhOZTVlRmtfTTZxSGZ5Q01pMWRRYkpocHMzcWlsN1daT1I5b0ZBMlBoWWw?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPVElCY21walNRbE1pRW15Wkx4ZnlZelNFamRpbC04cEdlTVBzejFYdGVqU2V5THhCOUFfSjBmTUk1NGR3RWVQQm80ZGxHb3F2TzYza2swN1RrSDdybllxbE9CSHF2aWtYbnl5czZDTnhmRllQeTllMWo0MVZ3cmVEelJ5ZjJ6dWFiQi1teFJ3aVlFZHJmclpOSEJuSE12cjdLakdWeVphZXV0cWZZZHFQRnowVy1zeDdQ?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxOdDRpdU9FbjgxbEJxbHVOSy1wTE9UazRNSG1Nc3AwaXRSTUJQR2lISUhyNzltWUZ6MWpFRXlRVWZkMk5uc2xZYnNkSXEzWUFoZUh0MEdiZTVwVVoxU190cmk5WGNUMlRyUTZxLXBIaTNDSUhybG9JRzFmcU5ibDNNenZRc1N0UUJCNmhwMXIwZFV3alpRalFpSmtjTkVfdFYtMUl5YWNFbXZUek5WMWlvZmFkb3ZyenhLMDlxSVkxck1JeDNMXzY3dE9nRWpMd2tGTEN4V0pB0gHbAUFVX3lxTFBEcm1NRjkyem5SRk52RVN6dUdBNHhDRXBXWnZNUzJJU0NadVNZWFFVR3ZMdGwyWVcwVENFd3N3RHB1bVlDV3FNMGRtT28yeUdHSjNzcC1mT0NfV3VEWFowbTE2WVpOUlFValduNnRBT0F4UFgydWNfQXpwVUVLVTZGc2Zvckh6ZDJJc1Yxeng4eUFiVkNiaHZDNlZDUzlKNWhzNmdydlpsc2JUc2lXRDM4bEFMLTNZSkJ6MWdHNHRHZllTN29rLU40T3c4bGNrekNaWG5TLUR2UEMwdw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPbFQ1cWh6R3FnQ3BUZWJlMHNqazZUeExEN1RkQUMzeDBPcHgyOGxfZHI2eV82RkxQcWVXV2h2MDVOcWZaeGNEOEZDN29GcmdLTDR2S1lMaHpoTDFGQ1VjYTBxS010bkZGbmV1aGxmSW5tcFEyUTFzb3FrQno2aE5WV1JDMHlaU2FndDVRNHZYYkZ1alV3eWQ4RHEyb0ZCWnEtZlJmaDl3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
