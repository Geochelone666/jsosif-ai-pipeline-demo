# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:00:52.156380+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 5, 'ai': 9, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 10 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 204.6400 |
| Return 1D (%) | -4.2217 |
| Return 1W (%) | -2.9958 |
| Return 1M (%) | -10.3950 |
| Return YTD (%) | 9.9833 |
| Return 1Y (%) | 1.1042 |
| Annualized volatility (%) | 37.3683 |
| Beta vs SPY | 1.9342 |
| Max drawdown (%) | -20.1527 |
| Sharpe (rf=0) | 0.2150 |
| Downside deviation (rf=0, %) | 25.5783 |
| Sortino (rf=0) | 0.3141 |
| Historical VaR 95% (1D, %) | 3.8869 |
| Historical ES 95% (1D, %) | 4.5913 |
| Correlation vs SPY | 0.6620 |
| Tracking error vs SPY (%) | 30.4504 |
| P/E (trailing) | 25.87 |
| P/B | 21.58 |
| EV/EBITDA | 24.41 |
| Revenue growth (%) | 105.90 |
| Forward P/E (estimate) | 12.86 |
| Gross margin (%) | 74.67 |
| Operating margin (%) | 66.24 |
| Return on equity (%) | 117.21 |
| Free cash flow yield (%) | 0.85 |
| MA50 | 221.6846 |
| Close vs MA50 (%) | -7.6887 |
| MA200 | 204.0922 |
| Close vs MA200 (%) | 0.2684 |
| RSI (14, Wilder) | 35.0660 |
| MACD (12,26) | -3.6439 |
| MACD signal (9) | -2.1615 |
| MACD histogram | -1.4824 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 204.6400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -4.2217 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.9958 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -10.3950 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 9.9833 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 1.1042 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.3683 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.5783 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3141 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.8869 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.5913 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6620 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.4504 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.9342 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.1527 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2150 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.8586 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.2370 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.2110 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.8461 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.8711 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 35.0660 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.4824 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.6887 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 0.2684 -> Slightly above the moving-average trend level.

## TAILWINDS

### Nvidia Reports a Big Win, But Its Stock Stagnates. Wall Street Is Worried About a Potential Plunge to $180.
- Summary: Nvidia Reports a Big Win, But Its Stock Stagnates. Wall Street Is Worried About a Potential Plunge to $180.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOTXZESlFUMlNnVnpVQmw5TUdUZEt0NTRadFFCZW9IYThsRWV4SDJoX3pKQ19HUkNRc0VLdm5LM0JoS0Y4eXVwZlNuc2FPdHNlcnF4SVJpU1pGU0UzNDJ1SnNrMHd2QUt6bDV4OWd6aGV3OUVZbG1YOXJ6Ymh4eEd2ZHFCVXdXVG41MEg2c0ZfU25qcnhNbGh5eg?oc=5>

### Can NVIDIA Stock Jump 50%?
- Summary: Speculative question about future price surge.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxOQXQyVjdJVW4xalMtNHZlclFJN1BOQkxUMElvOFZzZENuX2VCZUplTG1JdVoyZndURXhRaTN2UHZGNEVsM0FwSG41ZWR4TkFUb3VPM2R5cWp2eUw0UktEbzhqbmdiZ0tpSUVGdXA4a3lQMlhUMnlOclRTNXVXQnhZTlcwcDVlb0dDTGRtelV3?oc=5>

### Nvidia: Time To Lock In The Profits (NASDAQ:NVDA)
- Summary: Nvidia signals profit‑locking strategy, hinting at strong earnings outlook.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxOYXFJb1p4X09jV3Y5R3V5bU9XZFpRVXI2c3VyanpBaHVvcHpfbHpyd1VYSzctdU5NSFJFdHk0Tk1kVWpfbGYzeFFibTV3T2hKcC03Rjh1SXJXSEtlZVU2cDkxeHU2emZZUE1KRHpDMWxZbk1PUkxBTDROVzh3OU1KeA?oc=5>

### NVIDIA Corporation (NVDA) is Attracting Investor Attention: Here is What You Should Know
- Summary: General investor interest noted, no specific event announced.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPa0VXRS1ZUVRxVlhOTHhfNTNGazVQZlJ5MEdxMUllUDNmdlZ0dElLbVJCQl9waFJaLUV1azhjc2I5UTJZYjRYT1dQLWRseUlJSjgwTnFaa0t0dnBYSnpOR09SZThsTnRObnhSaHRKZ1JFSnc3VnpJbEUzeTZsSDhkWmR5ZEltVVkyamN2U0VKMkJ0T05xTVZPNlBLTGQ4eGZXVnVTZ2hhX2xwem4t?oc=5>

### NVIDIA (NVDA) Sees $682.3 Million in Net ETF Buying on Oct. 28
- Summary: Significant ETF inflow indicates bullish market sentiment.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQVlhEOHRxZkx2cnFrYnpkajdBQjhSYXBTMWhwb2JoLTF2V3Q0XzJpUnlMaFpaX2NlWTVsTk5kUW9mbGNxb21hVDRsVGNlYllsaWMtZllTYVFXMVgtSE9DcFc4U0JjVDE0bnJPaVZ1dW8yOWVHV1pQMTduamJ5cF9jV25KZ1V2LVVnQlFBNWNkclU?oc=5>

## HEADWINDS

### Nvidia Shares Drop Amid Chip Selloff: What's Happening?
- Summary: Nvidia Shares Drop Amid Chip Selloff: What's Happening?
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOOC1GZUJ5QklkTEhTX0FoM3JJc3lIUXFoUUtCcmUxdkljWnpiU0dGUTJ3bW9URFZNTnZ0dEZlSW1WS05SV0NMTnBhUFJ5QkhGSmZUZTd4TEVqR3locUtEVHZ6QnhwRWRFeEpMNkM3YzRMUDZpaThzOU5NZXZTeHZjOGFyejFrOV85YkY1WHA0N0ZoMDJ1T0dEV0QtUWNDZTFwRFhHanBxRXNMdnY4eDJlenlLaw?oc=5>

### Nvidia Stock Has Dropped Nearly 6% in a Month; Now Jim Cramer Is Asking Why ‘Anything Negative in Tech’ Immediately Crushes NVDA
- Summary: Nvidia Stock Has Dropped Nearly 6% in a Month; Now Jim Cramer Is Asking Why ‘Anything Negative in Tech’ Immediately Crushes NVDA
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNcWZmNGZfcHpPQ3V5YWpBOV8yTTZ5OFhVbWV2M0VtLUprRzJwRllPbXVMWDVodmFoUG9wYndHZFlVdFc5Q3RIMkwzMzRGWUVhVmh0M3RURjd1VVJCRVpYbGJiTlc4V1pqTGpuWThGVFpCdXdHVWthTEUycVNybkh1STJYeUtXbFQ2YkhvYVUzdV82RFlGRXcxcGVn?oc=5>

### Nvidia Stock Is Set for Its Worst Month in a Year. Time to Buy the Dip.
- Summary: Nvidia Stock Is Set for Its Worst Month in a Year. Time to Buy the Dip.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTFA5eVhHal84SUVnWXJrMXZ0NGxSNzlkY2VBcnd2M1pjaEhYOTBJcWg1ZFVGeUFyUXhrX0cyZkhMQ0VQRms1VEFXUkFJS2kxd0g4a3ZjbDMteXhJYXVFVFJRVW90VjBaRHE0VUJDc2twdGVFc1c3azhjeQ?oc=5>

## CATALYSTS

### NVIDIA Stock: Analyst Estimates & Ratings
- Summary: NVIDIA Stock: Analyst Estimates & Ratings
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPUmtaX09vY0lvNDRSS196b0l5UFNXbEx0eVp4RmhQT2E0UTVrT2x0MWJQZ1ZLSTMzTk9PbEF1cmNub3laQ1JkaUxnMEJFY0luc0IxUDZvS1V0V21WRnU0RmZpZmtlUDdZUGs0MjdQeVRGMG1kcDkyTmhVOEVtNUlpZ2F6RUFURG5iQkE?oc=5>

### NVDA Stock Drops: Nvidia May Back Data Center Loan Its Own Customer, Analyst Sees Little Impact From Intel’s Weak Report
- Summary: Analyst notes potential data center loan backing; Intel weak report unlikely to affect NVDA stock.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQTGdFWTJ1Wm1ISjFPRjVLdVowSFF0RHpiODd4cldVU1VEX3FUU1VFc3hROVlzM3Nsd0RONGE2emNfZ1hsTm9MUUNUR05IWFFnVTJpeEV4TjMzRTZ5eG1scm0yT1VOTWF1X2F1VmoxeG9NaUJqa1hKX0JlbDhGVmY5dEhZcUc0d2hBMGdNUWo2eDdyMlJ0Y3dZ?oc=5>

### Why Nvidia Stock Took a Dive Today
- Summary: Explains factors behind NVDA stock decline today.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxQZWpnVVNKVXlKQzRrdEl1SmhxZWVWd2ZFZjlEdUxCU1NCal91ZHpWVlo4NnE4WnlvQzVUVkhIVkdpVXRRSWUtcDQ3YThveWU1WnlQQ3VBMDk0aDhmMFRUV2VxcUxOT2pmZlp2WmpZSnpnczQtLVAzXzkyVTNGQXY2X242NA?oc=5>

### Can You Make Money Off NVIDIA Stock Now?
- Summary: Discusses current NVDA stock valuation and potential returns.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQd3NKR0JBQldHLU45bXdMd1g3ZFBDby0tMURjdVNBelJOUW9OcXJfUmJ6cFN4NkdXUHo5Zkk3Z1pyeHRTMTdfTWNVY3prZmptVEJ2NHdGUmJrVEVGQ2xQUGIxZUs1dTk5Q09rWlRsRGt3UHM0YmdoaERWblc1dzF2RlJURHRyRnZCSi1WekRiazFaVDhEc0VMdFR3Q3V0MjJBaVE?oc=5>

### NVDA Stock Alert: What to Know as Nvidia Invests $3 Billion in Meta
- Summary: Highlights NVDA's $3B Meta investment and its market implications.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPWnl5Qi1MY0NrMUF0ODAzM3hvbUxLMkpLRnBrMlp2RExVQkx5eEhtZW0zdVdac1pPNGowX1JBUkYzX3BHYWtVRnZtOGFZbzdoYV9oY3hpenJXcnltOE5IUEtKc21zRktPb0Q3cTRGX2VXc2FaUzFGZVRjWkZrc29veEdoX1pIazh6Wm5Rdy1CYkRFUUhQS0NNb01DSVE4SThlRkFiNWZmdkdQUF9qcVE?oc=5>

### Why Nvidia shares are down over 4% on Friday?
- Summary: Analyzes reasons for NVDA shares falling 4% on Friday.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxNcVM1bDh2VTFiSk80QXE1STh2azE2TDlXQWtkX1ppS3BaaUctdGItZTNpNmo1WFJwaGVleGszWVVoaEk4Q1V6eEN2YmdBYk85RXVUOUNtSmN4OWFqTWZBSjJUNjVZYVRJSHVmZnpmanRqbkZvMVEtUzZpRnI5XzBfdV9TbHZzUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **25.87** | **21.58** | **24.41** | **105.90** | **4,941,441,662,976.00 USD** | **1.10** |
| AMD | 128.78 | 12.26 | 85.26 | 50.10 | 824,073,388,032.00 USD | 98.09 |
| AVGO | 41.64 | 15.62 | 30.46 | 85.50 | 1,556,585,250,816.00 USD | -12.74 |
| INTC | N/A | 2.87 | 29.74 | 25.40 | 349,185,605,632.00 USD | 63.75 |

Peers fetched as_of: 2026-10-30; NVDA reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-26
- Revenue (latest available single quarter): 96,221,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- Net income (latest available single quarter): 59,688,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxOTXZESlFUMlNnVnpVQmw5TUdUZEt0NTRadFFCZW9IYThsRWV4SDJoX3pKQ19HUkNRc0VLdm5LM0JoS0Y4eXVwZlNuc2FPdHNlcnF4SVJpU1pGU0UzNDJ1SnNrMHd2QUt6bDV4OWd6aGV3OUVZbG1YOXJ6Ymh4eEd2ZHFCVXdXVG41MEg2c0ZfU25qcnhNbGh5eg?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxOQXQyVjdJVW4xalMtNHZlclFJN1BOQkxUMElvOFZzZENuX2VCZUplTG1JdVoyZndURXhRaTN2UHZGNEVsM0FwSG41ZWR4TkFUb3VPM2R5cWp2eUw0UktEbzhqbmdiZ0tpSUVGdXA4a3lQMlhUMnlOclRTNXVXQnhZTlcwcDVlb0dDTGRtelV3?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxOYXFJb1p4X09jV3Y5R3V5bU9XZFpRVXI2c3VyanpBaHVvcHpfbHpyd1VYSzctdU5NSFJFdHk0Tk1kVWpfbGYzeFFibTV3T2hKcC03Rjh1SXJXSEtlZVU2cDkxeHU2emZZUE1KRHpDMWxZbk1PUkxBTDROVzh3OU1KeA?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPa0VXRS1ZUVRxVlhOTHhfNTNGazVQZlJ5MEdxMUllUDNmdlZ0dElLbVJCQl9waFJaLUV1azhjc2I5UTJZYjRYT1dQLWRseUlJSjgwTnFaa0t0dnBYSnpOR09SZThsTnRObnhSaHRKZ1JFSnc3VnpJbEUzeTZsSDhkWmR5ZEltVVkyamN2U0VKMkJ0T05xTVZPNlBLTGQ4eGZXVnVTZ2hhX2xwem4t?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQVlhEOHRxZkx2cnFrYnpkajdBQjhSYXBTMWhwb2JoLTF2V3Q0XzJpUnlMaFpaX2NlWTVsTk5kUW9mbGNxb21hVDRsVGNlYllsaWMtZllTYVFXMVgtSE9DcFc4U0JjVDE0bnJPaVZ1dW8yOWVHV1pQMTduamJ5cF9jV25KZ1V2LVVnQlFBNWNkclU?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOOC1GZUJ5QklkTEhTX0FoM3JJc3lIUXFoUUtCcmUxdkljWnpiU0dGUTJ3bW9URFZNTnZ0dEZlSW1WS05SV0NMTnBhUFJ5QkhGSmZUZTd4TEVqR3locUtEVHZ6QnhwRWRFeEpMNkM3YzRMUDZpaThzOU5NZXZTeHZjOGFyejFrOV85YkY1WHA0N0ZoMDJ1T0dEV0QtUWNDZTFwRFhHanBxRXNMdnY4eDJlenlLaw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNcWZmNGZfcHpPQ3V5YWpBOV8yTTZ5OFhVbWV2M0VtLUprRzJwRllPbXVMWDVodmFoUG9wYndHZFlVdFc5Q3RIMkwzMzRGWUVhVmh0M3RURjd1VVJCRVpYbGJiTlc4V1pqTGpuWThGVFpCdXdHVWthTEUycVNybkh1STJYeUtXbFQ2YkhvYVUzdV82RFlGRXcxcGVn?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTFA5eVhHal84SUVnWXJrMXZ0NGxSNzlkY2VBcnd2M1pjaEhYOTBJcWg1ZFVGeUFyUXhrX0cyZkhMQ0VQRms1VEFXUkFJS2kxd0g4a3ZjbDMteXhJYXVFVFJRVW90VjBaRHE0VUJDc2twdGVFc1c3azhjeQ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPUmtaX09vY0lvNDRSS196b0l5UFNXbEx0eVp4RmhQT2E0UTVrT2x0MWJQZ1ZLSTMzTk9PbEF1cmNub3laQ1JkaUxnMEJFY0luc0IxUDZvS1V0V21WRnU0RmZpZmtlUDdZUGs0MjdQeVRGMG1kcDkyTmhVOEVtNUlpZ2F6RUFURG5iQkE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQTGdFWTJ1Wm1ISjFPRjVLdVowSFF0RHpiODd4cldVU1VEX3FUU1VFc3hROVlzM3Nsd0RONGE2emNfZ1hsTm9MUUNUR05IWFFnVTJpeEV4TjMzRTZ5eG1scm0yT1VOTWF1X2F1VmoxeG9NaUJqa1hKX0JlbDhGVmY5dEhZcUc0d2hBMGdNUWo2eDdyMlJ0Y3dZ?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxQZWpnVVNKVXlKQzRrdEl1SmhxZWVWd2ZFZjlEdUxCU1NCal91ZHpWVlo4NnE4WnlvQzVUVkhIVkdpVXRRSWUtcDQ3YThveWU1WnlQQ3VBMDk0aDhmMFRUV2VxcUxOT2pmZlp2WmpZSnpnczQtLVAzXzkyVTNGQXY2X242NA?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQd3NKR0JBQldHLU45bXdMd1g3ZFBDby0tMURjdVNBelJOUW9OcXJfUmJ6cFN4NkdXUHo5Zkk3Z1pyeHRTMTdfTWNVY3prZmptVEJ2NHdGUmJrVEVGQ2xQUGIxZUs1dTk5Q09rWlRsRGt3UHM0YmdoaERWblc1dzF2RlJURHRyRnZCSi1WekRiazFaVDhEc0VMdFR3Q3V0MjJBaVE?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPWnl5Qi1MY0NrMUF0ODAzM3hvbUxLMkpLRnBrMlp2RExVQkx5eEhtZW0zdVdac1pPNGowX1JBUkYzX3BHYWtVRnZtOGFZbzdoYV9oY3hpenJXcnltOE5IUEtKc21zRktPb0Q3cTRGX2VXc2FaUzFGZVRjWkZrc29veEdoX1pIazh6Wm5Rdy1CYkRFUUhQS0NNb01DSVE4SThlRkFiNWZmdkdQUF9qcVE?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxNcVM1bDh2VTFiSk80QXE1STh2azE2TDlXQWtkX1ppS3BaaUctdGItZTNpNmo1WFJwaGVleGszWVVoaEk4Q1V6eEN2YmdBYk85RXVUOUNtSmN4OWFqTWZBSjJUNjVZYVRJSHVmZnpmanRqbkZvMVEtUzZpRnI5XzBfdV9TbHZzUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
