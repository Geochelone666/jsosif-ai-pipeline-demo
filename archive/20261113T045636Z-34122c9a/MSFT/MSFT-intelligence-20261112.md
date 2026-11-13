# MSFT Intelligence Report

- ticker: **MSFT**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/MSFT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MSFT/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:16:17.121391+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 8, 'ai': 8, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/MSFT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 15 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 36.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 523.0000 |
| Return 1D (%) | 0.3588 |
| Return 1W (%) | -2.4126 |
| Return 1M (%) | -3.3540 |
| Return YTD (%) | 8.8288 |
| Return 1Y (%) | 3.1622 |
| Annualized volatility (%) | 34.0137 |
| Beta vs SPY | 1.0091 |
| Max drawdown (%) | -30.5348 |
| Sharpe (rf=0) | 0.2587 |
| Downside deviation (rf=0, %) | 21.7502 |
| Sortino (rf=0) | 0.4045 |
| Historical VaR 95% (1D, %) | 2.8530 |
| Historical ES 95% (1D, %) | 4.1000 |
| Correlation vs SPY | 0.4075 |
| Tracking error vs SPY (%) | 31.0618 |
| P/E (trailing) | 27.30 |
| P/B | 8.26 |
| EV/EBITDA | 19.22 |
| Revenue growth (%) | 18.80 |
| Forward P/E (estimate) | 21.62 |
| Gross margin (%) | 67.66 |
| Operating margin (%) | 47.10 |
| Return on equity (%) | 34.22 |
| Free cash flow yield (%) | 0.08 |
| MA50 | 518.7220 |
| Close vs MA50 (%) | 0.8247 |
| MA200 | 440.0262 |
| Close vs MA200 (%) | 18.8566 |
| RSI (14, Wilder) | 48.4457 |
| MACD (12,26) | 2.6933 |
| MACD signal (9) | 4.3129 |
| MACD histogram | -1.6197 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MSFT': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 523.0000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.3588 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.4126 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.3540 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 8.8288 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.1622 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.0137 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.7502 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4045 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8530 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1000 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4075 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.0618 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.0091 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.5348 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2587 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.6154 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 67.6570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 47.1040 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 34.2210 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.0771 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.2965 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.4457 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.6197 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.8247 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 18.8566 -> Clearly above the moving-average trend level.

## TAILWINDS

### Microsoft Stock (MSFT) Climbs Despite a Major Service Outage
- Summary: Microsoft Stock (MSFT) Climbs Despite a Major Service Outage
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPaDFlYVFZNElsTEdDYXN6ZnNjR19Wb2pJMzJBSU9QeGg0bGg4MzlvLU4tUjd6NEE5aG5COUFKNFVoY2YwNkFYc3hZbEltMjR3QkEyMFF5cHl5ekJxdXBpSzZPQndrNHF1bjlZY1dPMUlTc20wWm9JRklUc0dsYU5KZGt1Y2xxY2dCc2lEXzJSTmV1UQ?oc=5>

### Microsoft (MSFT) Stock: $545 Tuesday After a 2.75% Gain, $610 or $505 Next
- Summary: Microsoft (MSFT) Stock: $545 Tuesday After a 2.75% Gain, $610 or $505 Next
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOY1JYc0s5Z20xZnl6RXdiSGdDajFwZ1dWdVp4YlFldTU0TjlZdGsxQkVrdDFvT2d5d0oyVGRjbWJjNjVIMHpzcWZ0UVpKM2EtQ2NxYVI1cFN0anV2RURPcFZEUHBySk1kaV9JSE0wRXpaYnVLcGtZNDZPQ0o3ZmpsMU90R1BWMDdOZW9zYWFiS0duS1FEOGl0VGlacGtILWJ2ZHc?oc=5>

### Microsoft Is Off Its Record High. Next Week Could See the Stock Reignited.
- Summary: Microsoft Is Off Its Record High. Next Week Could See the Stock Reignited.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidkFVX3lxTE83cmJyRlBjMDBWU21ycUZoMzJTZXRiYml1RVpnRHZ6emprSmNFNUVIYk5oYm45VUJXdkJHSm5DVm5lamdUQjZ3QVl2UTcyRzZvc0lsWE9sWGFFeE52VUE2TlBJUExqandxbktlcjNiU01XNGRCbHc?oc=5>

### ETFs Are Buying Microsoft (MSFT) on Nov. 10
- Summary: ETFs increased holdings of MSFT on Nov. 10, indicating institutional support.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQWWxCVUhHQ1NaNThLRkJZVmZJR2RVXzJfNVdTMWNOZTMtd3NjQ2NpLUt4MERvSVV6bXZIZ3YzUXpIZ3Bfdjk2WTRsZXc2dkpiRDJTYk9OMThONTNWMk1CdzlkR0J6RmM0Uk95WC03RExtcENTTWVwQWFxRU14Qy1NM1NXV2htU3RMcTFUdzdYZjl4WkJEOC14bDVrdw?oc=5>

## HEADWINDS

### Microsoft tumbles as Anthropic unveils office tools ahead of IPO (MSFT:NASDAQ)
- Summary: Microsoft tumbles as Anthropic unveils office tools ahead of IPO (MSFT:NASDAQ)
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPNk5XZzZTN001ckRmLXd3cmt5T0dYMXBnYkd5aUs2dmMzcU9kNFlSYU5ZaFY0UVE3U2VVdGxzbnJoZVp4blJkMDMySktmWTFVZFZEU3YyeWRXeW1TSHNpQnFwMmNuaGYyVXRmakRsQ3lNU08xaVhrdGphSGNWdmZTeVlpWER6SW9VaW1PZzU5QWZMOGg1b1M2UDMxamE4MHl2RzFTRg?oc=5>

### Microsoft Stock Falls On Anthropic’s Challenge To Office Software
- Summary: Microsoft Stock Falls On Anthropic’s Challenge To Office Software
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQVU1YdlJPSUlEcmx5OUpyelIxZlBYSnp5QmUzbTJpNE5IcG4xSURIbndrNWlHSXJpMGVacnM2QlpmWGdUbWRtY0xJQ3l1Z3RqN0RCRDM5VXZEOFlQWktpNTBDdHZqTTJDRnhlUkFVS1VOQS1Dakx2VmFhSVU3WXlaTGFicjRpcnBPWjJkbHBtcExZbXQySktYOWRB?oc=5>

### Azure Grew 48%, Yet Griffin Securities Downgraded Microsoft (MSFT). Here’s the Catch
- Summary: Azure Grew 48%, Yet Griffin Securities Downgraded Microsoft (MSFT). Here’s the Catch
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPWTNUbVRXMnF2WU1sMW9vbFRLNFg4VUhFUzNZcTBJUUM3V1ZQT1BfWExkbDF6Z1c5LUdvUUZobko2Ykg1eU5aZUlaS3ZPZFJRdG1fYVpZVU1wYlVNYTNaU25henhkc1I3WHAwMDhZeGtSU3FuUGUtLW94Y2dYSDNLTldXWnRQWHBOUy00Qk9fYVA0Q3ZR?oc=5>

### Microsoft stock sinks as new AI rival targets $27 billion business
- Summary: Microsoft stock sinks as new AI rival targets $27 billion business
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQZzRBWDREUUttRzVpZ2N5Uzk5MmhoVHgxY25iWElyTy14V2E2N0dUY1FNaFpDRmE2eUM5UkVub1dIRG44eHZNQjBqay1jd2RoSURONnhYUGpmbVl5NXh3N0FGOXl2aXpwY3dkQXE2MXM4QlRiRXdBbnlUZGotQjd5ZTdCWHB4YXlfbTFnQmwtRnNrX2pFUURnMlh2dw?oc=5>

### Microsoft stock falls as Anthropic takes aim at Excel and workplace software
- Summary: Microsoft stock falls as Anthropic takes aim at Excel and workplace software
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNRDhIR2N3YWVsRk1wWTZtRmNTTFVwRDdxb1hUVmtqQ3NfTXRRaGJXa211U240YjNxa1hzRUJ0bjJ4RnI0cFlVM3VleXV4XzlqTVp1V0dzQUFtQTR0R09IQzBSeGZzR3RJaHZPS1BMbGpBeWRaM3JkU2o1OF9jQ1ZPV1B2WmxfQU05ZDh2bXVLR0N6YlFza21nOHlVaER1ek4xSTBN?oc=5>

### Microsoft Stocks Move Lower Despite $1 Billion Anthropic Placement Commitment
- Summary: Stock fell despite large Anthropic commitment.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNb0NfSTRNcWhsSkxvQmNiSHhpYzBIVGdSUTl3aXJHV1Z0clVSTkhVUldMS2k3Sm95Wm4zWmt5dkFLYjZZc3p6YWtUOTVXcng3UHN2dkJmaWZ0NWFKNFJGRmQzQjk3c2xTQUt0WmEyWWZpNFBTdm9WTlg5NWd3V3k5ano1ZXBQSzd2d0ZuN2VWM2dudmx4dFE5YUw4SUlMY1hQc2c?oc=5>

### ETFs Are Net Sellers of Microsoft (MSFT) on Nov. 5
- Summary: ETF net selling indicates negative market sentiment.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOajREVXB1X0Fpa25Ha3Y2Q1ZuZTlMNTlpay1oU3pwR01vNVdNWlZaOFRNdFljelFDOUNpaDlkdkUxeFdZY3N2RVVGMFJhSnpuTWlNM3FOajdMWEQwN3pJVWxvWG9tU3k5Qno5LVF0TzRfTl9uVWloLVBBYmE4aXkyOHV4QnVMLVdPY0U4LUFZemZoNVJ3V1JUZlBqWkg?oc=5>

## CATALYSTS

### Microsoft Stocks Decline 2.5% as $1 Billion Anthropic Stake Tests Partner-Rival Balance
- Summary: Microsoft announced a $1B stake in Anthropic, testing its partnership and rivalry balance.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPd2NEVEtyeThmMlBlejQ5YS0xdkVsTnhiczZRSkY2VUlWSFc1ZmhNek0tTVU5THZvZjdGbW5JWF9rSWFkanM3WkxyTlp6NDhWTHJwcGlzWFdGLXlIcXBOcndpVDlOQTZCanZOZ2VsNFdkMUdKOXZhUDlrS1lNUE9OakVMRVZnQVozTkdtYkFEM3Z3SnBQcjlFSw?oc=5>

### Microsoft (MSFT) Expands AI Ties With Ohio State, Is The Stock Fully Priced?
- Summary: MSFT deepened AI partnership with Ohio State, potentially boosting AI capabilities.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxOLTdsc0owQmtKRXJkSGItdm5pcWdySkE1V3hadVNOZkhObEF6ci1hMFV6OUljaDJDeGp1eUJyZGVPV0xzLWJEcm5fZkc2blhHcVZ2SFlpZjlpUU91T0ZSczEtclBVX2tzRmVaNEJULUtVZ09ObnlKaUcyVklmVFZlX3JUZTNmdw?oc=5>

### New Buy Rating for Microsoft (MSFT), the Technology Giant
- Summary: Analyst upgraded MSFT to buy, signaling positive outlook.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxPVi1naEVRRms0UzVDNjUtblhGc0o0ZzRhRExaazBjV1kxQ2lHTVYyTWRoZlRsdFZMbTlKdFAwWHl3T0hHdDJ4bVNDNzlraVZKSU8yUGNFWDBjMVI2S3ZhTm5WTVBqS2t4Y2dMdk00UjV3aEpsU3pVVExsZm9iRDBiQlJIa05pb3R1Z09nUjNQVzNPZ3E4d0prWm02TDJ6RGZvb1owWlY2dllWUTQ4UjI3MEhISzVPa3kzT3AxTmgtRTREdVdSeXBXNXNRMHJENTRWbUMtekVR?oc=5>

## RISKS

### Microsoft Corporation (MSFT) Is Pouring Billions Into AI: Could Massive Spending Weigh on Future Returns?
- Summary: Microsoft’s large AI spend may pressure future returns.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPbEdCNzJNcVA3Rm9nUDNqenBxaENDa1BkT19iWVV0TVhjYzJvOW1WQ3dHQm4xcUNLT1J1bjNXYmlhNjN6RndCcEtPbzFmUGFkeWtHY0ljdzRBZE5SY29KSHJ5Nl9rQlE5dVpyNXBvUGZrQ280WkRwUW9OTV9zN2V6MzNLVG15eFVIUmI2MFdDc25USW12OGRuR1NaRUhkMEVKbkNYeE1JNGFQaEU?oc=5>

### Anthropic’s Office, Microsoft’s Legacy, Filled Moats, And A Potent AI Threat (NASDAQ:MSFT)
- Summary: Commentary highlights AI threat from Anthropic, posing competitive risk to MSFT.
- Date: 2026-11-12 | Impact: high | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxOay04cUhNbjZVcXAzYnNwNGxxRE1NMEt4eWFrUkZuckVzNWY4ZEQzZE5vN0JyU0VpTHJuREFtaDBCbEZpTWdMbzM5Z0E0Ul9VdlFxa0dPMFUwRHhUUC1uU2NrQTNPR1pWbUYxOGFYSG1vM2RnNzJ6Y3BINWdQQ1dBdnJhQWcwMmJqNkN0M3FXQnVxSGZpT0pEUG44UTc2bGQ0M1JxUmpQV25OTm5Y?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MSFT** | **27.30** | **8.26** | **19.22** | **18.80** | **3,883,899,813,888.00 USD** | **3.16** |
| ORCL | 19.92 | 6.22 | 15.15 | 29.60 | 396,291,866,624.00 USD | -43.25 |
| GOOGL | 15.60 | 5.57 | 19.27 | 24.70 | 3,672,217,747,456.00 USD | 4.45 |
| AMZN | 21.62 | 4.71 | 16.78 | 12.10 | 2,891,865,653,248.00 USD | 9.52 |

Peers fetched as_of: 2026-11-12; MSFT reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

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
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 19,953,000,000.00 USD; period 2010-10-01/2010-12-31; fiscal year/reporting period 2011/Q2
- Net income (latest available single quarter): 36,629,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikgFBVV95cUxPaDFlYVFZNElsTEdDYXN6ZnNjR19Wb2pJMzJBSU9QeGg0bGg4MzlvLU4tUjd6NEE5aG5COUFKNFVoY2YwNkFYc3hZbEltMjR3QkEyMFF5cHl5ekJxdXBpSzZPQndrNHF1bjlZY1dPMUlTc20wWm9JRklUc0dsYU5KZGt1Y2xxY2dCc2lEXzJSTmV1UQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOY1JYc0s5Z20xZnl6RXdiSGdDajFwZ1dWdVp4YlFldTU0TjlZdGsxQkVrdDFvT2d5d0oyVGRjbWJjNjVIMHpzcWZ0UVpKM2EtQ2NxYVI1cFN0anV2RURPcFZEUHBySk1kaV9JSE0wRXpaYnVLcGtZNDZPQ0o3ZmpsMU90R1BWMDdOZW9zYWFiS0duS1FEOGl0VGlacGtILWJ2ZHc?oc=5
- https://news.google.com/rss/articles/CBMidkFVX3lxTE83cmJyRlBjMDBWU21ycUZoMzJTZXRiYml1RVpnRHZ6emprSmNFNUVIYk5oYm45VUJXdkJHSm5DVm5lamdUQjZ3QVl2UTcyRzZvc0lsWE9sWGFFeE52VUE2TlBJUExqandxbktlcjNiU01XNGRCbHc?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQWWxCVUhHQ1NaNThLRkJZVmZJR2RVXzJfNVdTMWNOZTMtd3NjQ2NpLUt4MERvSVV6bXZIZ3YzUXpIZ3Bfdjk2WTRsZXc2dkpiRDJTYk9OMThONTNWMk1CdzlkR0J6RmM0Uk95WC03RExtcENTTWVwQWFxRU14Qy1NM1NXV2htU3RMcTFUdzdYZjl4WkJEOC14bDVrdw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPNk5XZzZTN001ckRmLXd3cmt5T0dYMXBnYkd5aUs2dmMzcU9kNFlSYU5ZaFY0UVE3U2VVdGxzbnJoZVp4blJkMDMySktmWTFVZFZEU3YyeWRXeW1TSHNpQnFwMmNuaGYyVXRmakRsQ3lNU08xaVhrdGphSGNWdmZTeVlpWER6SW9VaW1PZzU5QWZMOGg1b1M2UDMxamE4MHl2RzFTRg?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQVU1YdlJPSUlEcmx5OUpyelIxZlBYSnp5QmUzbTJpNE5IcG4xSURIbndrNWlHSXJpMGVacnM2QlpmWGdUbWRtY0xJQ3l1Z3RqN0RCRDM5VXZEOFlQWktpNTBDdHZqTTJDRnhlUkFVS1VOQS1Dakx2VmFhSVU3WXlaTGFicjRpcnBPWjJkbHBtcExZbXQySktYOWRB?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPWTNUbVRXMnF2WU1sMW9vbFRLNFg4VUhFUzNZcTBJUUM3V1ZQT1BfWExkbDF6Z1c5LUdvUUZobko2Ykg1eU5aZUlaS3ZPZFJRdG1fYVpZVU1wYlVNYTNaU25henhkc1I3WHAwMDhZeGtSU3FuUGUtLW94Y2dYSDNLTldXWnRQWHBOUy00Qk9fYVA0Q3ZR?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQZzRBWDREUUttRzVpZ2N5Uzk5MmhoVHgxY25iWElyTy14V2E2N0dUY1FNaFpDRmE2eUM5UkVub1dIRG44eHZNQjBqay1jd2RoSURONnhYUGpmbVl5NXh3N0FGOXl2aXpwY3dkQXE2MXM4QlRiRXdBbnlUZGotQjd5ZTdCWHB4YXlfbTFnQmwtRnNrX2pFUURnMlh2dw?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNRDhIR2N3YWVsRk1wWTZtRmNTTFVwRDdxb1hUVmtqQ3NfTXRRaGJXa211U240YjNxa1hzRUJ0bjJ4RnI0cFlVM3VleXV4XzlqTVp1V0dzQUFtQTR0R09IQzBSeGZzR3RJaHZPS1BMbGpBeWRaM3JkU2o1OF9jQ1ZPV1B2WmxfQU05ZDh2bXVLR0N6YlFza21nOHlVaER1ek4xSTBN?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNb0NfSTRNcWhsSkxvQmNiSHhpYzBIVGdSUTl3aXJHV1Z0clVSTkhVUldMS2k3Sm95Wm4zWmt5dkFLYjZZc3p6YWtUOTVXcng3UHN2dkJmaWZ0NWFKNFJGRmQzQjk3c2xTQUt0WmEyWWZpNFBTdm9WTlg5NWd3V3k5ano1ZXBQSzd2d0ZuN2VWM2dudmx4dFE5YUw4SUlMY1hQc2c?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOajREVXB1X0Fpa25Ha3Y2Q1ZuZTlMNTlpay1oU3pwR01vNVdNWlZaOFRNdFljelFDOUNpaDlkdkUxeFdZY3N2RVVGMFJhSnpuTWlNM3FOajdMWEQwN3pJVWxvWG9tU3k5Qno5LVF0TzRfTl9uVWloLVBBYmE4aXkyOHV4QnVMLVdPY0U4LUFZemZoNVJ3V1JUZlBqWkg?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPd2NEVEtyeThmMlBlejQ5YS0xdkVsTnhiczZRSkY2VUlWSFc1ZmhNek0tTVU5THZvZjdGbW5JWF9rSWFkanM3WkxyTlp6NDhWTHJwcGlzWFdGLXlIcXBOcndpVDlOQTZCanZOZ2VsNFdkMUdKOXZhUDlrS1lNUE9OakVMRVZnQVozTkdtYkFEM3Z3SnBQcjlFSw?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxOLTdsc0owQmtKRXJkSGItdm5pcWdySkE1V3hadVNOZkhObEF6ci1hMFV6OUljaDJDeGp1eUJyZGVPV0xzLWJEcm5fZkc2blhHcVZ2SFlpZjlpUU91T0ZSczEtclBVX2tzRmVaNEJULUtVZ09ObnlKaUcyVklmVFZlX3JUZTNmdw?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxPVi1naEVRRms0UzVDNjUtblhGc0o0ZzRhRExaazBjV1kxQ2lHTVYyTWRoZlRsdFZMbTlKdFAwWHl3T0hHdDJ4bVNDNzlraVZKSU8yUGNFWDBjMVI2S3ZhTm5WTVBqS2t4Y2dMdk00UjV3aEpsU3pVVExsZm9iRDBiQlJIa05pb3R1Z09nUjNQVzNPZ3E4d0prWm02TDJ6RGZvb1owWlY2dllWUTQ4UjI3MEhISzVPa3kzT3AxTmgtRTREdVdSeXBXNXNRMHJENTRWbUMtekVR?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPbEdCNzJNcVA3Rm9nUDNqenBxaENDa1BkT19iWVV0TVhjYzJvOW1WQ3dHQm4xcUNLT1J1bjNXYmlhNjN6RndCcEtPbzFmUGFkeWtHY0ljdzRBZE5SY29KSHJ5Nl9rQlE5dVpyNXBvUGZrQ280WkRwUW9OTV9zN2V6MzNLVG15eFVIUmI2MFdDc25USW12OGRuR1NaRUhkMEVKbkNYeE1JNGFQaEU?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxOay04cUhNbjZVcXAzYnNwNGxxRE1NMEt4eWFrUkZuckVzNWY4ZEQzZE5vN0JyU0VpTHJuREFtaDBCbEZpTWdMbzM5Z0E0Ul9VdlFxa0dPMFUwRHhUUC1uU2NrQTNPR1pWbUYxOGFYSG1vM2RnNzJ6Y3BINWdQQ1dBdnJhQWcwMmJqNkN0M3FXQnVxSGZpT0pEUG44UTc2bGQ0M1JxUmpQV25OTm5Y?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
