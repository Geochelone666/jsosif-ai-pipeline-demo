# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-11-15**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-11-15**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-16T04:56:52.452094+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 0, 'ai': 15, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261115T044154Z-6abfba73/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **13**; {'directional_claim_without_event_type': 7, 'low_uncalibrated_model_confidence': 5, 'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 37.5%; oldest publication 2026-11-11

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 778.3100 |
| Return 1D (%) | -2.5212 |
| Return 1W (%) | 12.7986 |
| Return 1M (%) | -18.3340 |
| Return YTD (%) | 172.8984 |
| Return 1Y (%) | 228.8432 |
| Annualized volatility (%) | 84.2775 |
| Beta vs SPY | 3.4202 |
| Max drawdown (%) | -45.8952 |
| Sharpe (rf=0) | 1.8374 |
| Downside deviation (rf=0, %) | 52.5115 |
| Sortino (rf=0) | 2.9489 |
| Historical VaR 95% (1D, %) | 7.0090 |
| Historical ES 95% (1D, %) | 10.3312 |
| Correlation vs SPY | 0.5533 |
| Tracking error vs SPY (%) | 77.5703 |
| P/E (trailing) | 10.47 |
| P/B | 6.36 |
| EV/EBITDA | 7.74 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 3.75 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 74.59 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 3.31 |
| MA50 | 943.6894 |
| Close vs MA50 (%) | -17.5248 |
| MA200 | 765.4167 |
| Close vs MA200 (%) | 1.6845 |
| RSI (14, Wilder) | 42.4539 |
| MACD (12,26) | -55.0053 |
| MACD signal (9) | -53.5923 |
| MACD histogram | -1.4130 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 778.3100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.5212 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 12.7986 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -18.3340 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 172.8984 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 228.8432 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 84.2775 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 52.5115 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.9489 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.0090 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.3312 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5533 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 77.5703 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4202 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -45.8952 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.8374 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 3.7462 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 74.5860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.3091 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 10.4710 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.4539 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.4130 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -17.5248 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.6845 -> Slightly above the moving-average trend level.

## TAILWINDS

### Micron Technology (MU): Does a Low Earnings Multiple Understate Its AI Opportunity?
- Summary: Analysis questions if low earnings multiple undervalues Micron’s AI prospects.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQRmFxb0NFNGNaVzBRdzExcGJ6a2Jremg4N1JFQk1lRHlQME04V3NnQ2ZocVlBR2RkeVpVWmwzQ3BaVmZSZjhrTFZZTndQSTJNR2hieUtXSzdaNUdraVFlU3ZUNllBRFpNTUtTZUFJeTg3TTdIWGtib0ZKZmROZGk1NHVSeERfLXZoOHNGNmY1TTlqZGpVWjl2Sg?oc=5>

### Micron Is Down 20% in a Month. What Will It Take to Get MU Stock Back to $1,000?
- Summary: Micron's 20% drop and recovery prospects.
- Date: 2026-11-13 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNelVwdm5oMDVMRW1lazFacTZYZXpVTHNKQXNQbjBoREsyUkpBVHVDbnJWM2dHTXdYQTZmVG9hUDR5NjV0c2FoWVFsaExLRXRBUWlGTUhBV0taQkRMbTQtZmpNbzR1TGxaUFNfWHgyM3NyMnU2VWxPTTRpRW0zczEwUm9vMm1Kc2ViMTZBM2MxeVZDQmxTQWR0T0ZRa3pFSmVVS29NczJHQTAzaVZSMUhITTZibjhNamFlQ2pr?oc=5>

### What Is Going on With Micron Stock on Friday?
- Summary: Discussion of Micron stock movement on Friday.
- Date: 2026-11-13 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPV21XaVk3OHBCQXdGdElzYmNzTUI1ek5pQzF2T1Z5SHRZTzd0MENiMEJBQV9ya0N1Wk91LURJTlRDa1lPZ1lvRklEOHY3QVFCU2tCM19aSENsMjRYalFsRnFxcnlZR3E5M0ZHZHVXdll2OWVRYzBtWkg5WnlDUkVHWXpkdDU1T2N2SXdFOWRDeFNndld3NS1vVEZYN2hrQQ?oc=5>

### Micron Stock (MU) Forecast – Why Are Analysts Bullish Despite Ongoing Volatility?
- Summary: Analysts remain optimistic about Micron’s future, citing strong demand and potential upside despite market volatility.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNV1J2alhFSlhSeFc5cG9KRWZ3R0hGd013SC1hc3lFcjRNVE8tdnpyc2lnS0FSUDJ6Qzc1SWhtUk5QZ2pkX3V0U0R1U3h3WWNOMENqUjJYdlkxSmdOYlVfcEluQ3phV1NUNjVCS3pHNkN1QWx0Nnp3ZFBVbXZmcmp0dEYxT1F5YXEtMlNmZmhzVWZxSmhYa010dUx3SHFPSVZxOEFma2xDa0JxZzdNeG9KVnljSW4?oc=5>

### What Bernstein Sees in Micron (MU) After the Memory Selloff
- Summary: Bernstein analysis following Micron’s recent selloff, discussing potential recovery and valuation.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPdUdkNlU1SG9TdmdNNU9IQW1tZl9lLVBFR1QzNUdUQVl4TzVxY3NfY3VLQW1BWmhpWDNlTjlTUC1rUTlXbEFXYUdmS0dMWHJkOUR0NTR1RXc0X3pGb1VPY0FJSjc5ZU5XbFRTMEJQQXFHaFpPMHZ3a2t0Vmo5c2w1a0FDc2JXZ3RqZlVid1pELVJ3T09OVERoOUhJUnQ?oc=5>

### Micron Technology (MU) Has More Than 75% Of 2027 Output Committed
- Summary: Micron secured over 75% of 2027 output, indicating strong demand.
- Date: 2026-11-14 | Impact: high | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNU1J4THBrTkV3M19WbEtScExWeGVyeUtlOGdEZHB5WE95NVo1dlBrMlp1b1JFXzBnQnd0Q3ZSaXFlNGdYWGJKYjhlaGMtS3NtOHEySFBqWVBSaVZFV0dRaG1qY19pZDgtc2N0R3pGd0R0VG1GdnlyX1RRajFrU1dpdTRNajE4amplYk5ubkF2WWV5WWc?oc=5>

### Micron, Amazon, and IBM: My 3 Favorite Stocks to Buy and Hold Through 2030
- Summary: Analyst recommends holding MU, Amazon, IBM until 2030.
- Date: 2026-11-15 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQUE96UGhWZTA3MG1KVjNmaHBYZjVuRHNHVXBnMzlHQ1NRajBRRS11WTVhYmNGSGFNYkFjU281Q3phU1lpVkI5RmhOdGtOUXVDbHhMSFNNaVhjVjQ0SnZ4YzlZWWthYWVTazdCb3A0LU5mVHVkNzh0clgxNU5qQUZBcENoYjBzbnQ4dURlWDk4aTNEZ3ZYQ0xqRg?oc=5>

### Why Micron Stock Was Sliding Today
- Summary: Analysis of recent Micron stock decline, citing market factors and investor sentiment.
- Date: 2026-11-13 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxQWm51RHk0MnZpTDZrTWFTR0l5RDJyTVBFWFBEQTNoVHZmQUNxLS1lMTlyNzJKajJkd1RHOW1LRVBPaFR5djF1aUJEV0ZxamlhTTZOUUhBSXVEenMzRVN1S05qZ282V3ZYa0xIa0FJVE52c1NNN08xbEUxaFQ2VXZldkN5cw?oc=5>

### Micron Technology (MU) Could Be 42% Undervalued Despite Board Retirement News
- Summary: Valuation assessment suggesting Micron undervalued, despite board changes.
- Date: 2026-11-11 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQd0FwdWhPal9UUHpiMk44MFFyUlpwbzBaZFl5VEFLTm5uZjRuTndoRkFZYmZtMm41M0x2SEVaNVdMcVpHdHBndVByeFpDTk1xOTVGcGkzY2Q2UXozRWtiWVZpY3pDNlVBd3p2aHR4VHVoSzF5ZlkzVWlDQ0FKNXFpMWk0eUJVMDRFa1FGQXAwaDAwMDhSYUJwejBR?oc=5>

### Is It Too Late to Buy Micron Stock?
- Summary: Questioning optimal timing for Micron investment.
- Date: 2026-11-14 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxOTE1UT2VEX281LUxZd1BjS1ZTYU9wQmpvdnVqQjUyRk1MUjVXTm1tRjhkRFI3MDVjT3c5dFBYNDl2MU5zQnd0X0RqODdXbEJSNnA3NnpFdGFKRWVEcTBwMmcxOE4wREU1ajdGRHUwSjg2RFhFTVU2Z19XUTBTYlVGd3RuUQ?oc=5>

### Why You Should Think About Micron Differently Now
- Summary: Recommending a new perspective on Micron investment.
- Date: 2026-11-12 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPcFNnQTlwa05zX0NIRktFcVBSaF9RMTFkVXJUbERZNFlVTzdqM2FGdDkwQVFtdGpnQUhtU2hqSklFb1VLOWkwT1RsWEE2Mzg4cmsycFE1VndieDBjZzJDU0dVeWpwU3VXdlhMNXBtWlRoYVd1YnNIQmEtY2JBVFBpdldSVlFiT2RLeVVYT3dHTGp6bTM5LXFfRVhVYnJPMVNUaC1GaVh2VlZVQTBx?oc=5>

### DRAM Just Got More Expensive Than AI Memory. Here’s Why Micron Could Soar in 2027
- Summary: Forecasting Micron growth due to rising DRAM costs versus AI memory.
- Date: 2026-11-15 | Impact: high | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPUEk0MzFlS3ZUbzdJbjg3OHlCamtpbjBCYVZmWGNLWXZaZVNnRXlXNXl3aVJ5eFV4SW45UWFKaWY2MnFRTFVUVEItd01xdXk3V1lWZGNEZXNiMXdTc1FfZnRUQWZXdlRyV2x2U1loS3ZGYzRZU0JuTDhUNFV2NW0zTGZjRU5OcnRsYlNzeHl2NTI1U0V1U2N6WmJpRER4cXM1TFdkdlJzYnRpaEZvbUpCV2JCMGU0REptd01HemFoTUU?oc=5>

## HEADWINDS

### Micron Technology (MU) Faces Fresh Regulatory Pressure In AI Memory
- Summary: New regulatory scrutiny targets Micron’s AI memory segment, potentially impacting growth and operations.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxOM2p6T05vX25BSVZwY2wybTdXWk9xckdjb2lHcWo2TFlDN2Z0MEZJSm5hczdzUjNFOTlfSVlzUDFUbWU1SzFkOTBDazVGY09JeGIzSDdDMVVDYk83YjJfWmNLUEJkVlBSNy01dXRtNE5ELV9paDJnZGRsMXNjb1d3TXRHMzBxT2FDYkpxUVJobWhZZlpSVVBpb3RQSTJpZ2RWcFNzODc5WmR2aWhVa29MZmtmTzhDb1hfQTd0WlY1eldESkdqS3pIWHVCOVZYOTRBalo3STBTSdIB3AFBVV95cUxOd1hlNGtaRV91b1BLSU9pTVpKSG5sTkRreENZOW1zMWluTldoYzhhVlY5MC0zb3JacTFYbjJmRnFEQWtYSTBWc3ZQRjRab1R2eE1neDJwLVdBcXRkN0h3eVk0dmloOENQRUtJWWplUEdSYjlCVDFBYnYtLXVPZG9iU3RZcGpIaDR3cU40Q01WQTFMM01ESXBCY3AtQlRZdVI1VDE0Qi15eFkxWnFlMnljcG9TYmJleEJVWnZtWGNzSkRGejZ6Z05EUXJiVlc1d21QZ0V0RlpqWUR4VVY0?oc=5>

### Why Micron Stock Dropped on Thursday
- Summary: MU shares fell Thursday due to market concerns.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOV0U3WERRLXdqM09NRmo1QVZkMGpRN2xncG5iZkJJTzBrcFhLa0ExNW94UjY0MmlKWUFHMEFmV0xReFNhNThEcTRFbC1VYU5XWVYzWE5RVGljWklmX1VGOEcwWndhd3FZalBCamZGR3lnQjM0cW5oRUVNRnRSazFTcTA3Qmc3UDdBVEpUUU9CZUJfVy13SExFUFAySUptYUE?oc=5>

## CATALYSTS

### Micron Technology (MU) Commits $1 Billion To Landmark AI Infrastructure IPO
- Summary: MU invests $1B in AI infrastructure IPO.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxORC1PS1FreEtDdjc3c0lRUTVvazRVVzBFVkNXYzNMMDBXRGV0R2Nfc1V5cjFlcnh6cHRhanE0a0dUbjByaGNBWExfcmpibDlYc1NoU3VYcjd2SzYzQ0hlcnh6WER0eXZUbHJQRUZ5WG5LS0NTRWxtTG1jcnJnMlVuOFJqaU1TbHg1dTFLLXdJQ21acXZ0MG5IMFZR?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **10.47** | **6.36** | **7.74** | **379.30** | **880,597,991,424.00 USD** | **228.84** |
| WDC | 10.40 | 11.83 | 17.47 | 55.50 | 110,668,668,928.00 USD | 88.47 |
| STX | 27.70 | 35.14 | 20.91 | 61.00 | 121,274,826,752.00 USD | 102.39 |
| NXPI | 20.86 | 5.53 | 13.78 | 19.30 | 66,816,724,992.00 USD | 34.07 |

Peers fetched as_of: 2026-11-15; MU reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-15

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-09
- Revenue (latest available single quarter): 8,440,000,000.00 USD; period 2018-06-01/2018-08-30; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 28,243,000,000.00 USD; period 2026-02-27/2026-05-28; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxQRmFxb0NFNGNaVzBRdzExcGJ6a2Jremg4N1JFQk1lRHlQME04V3NnQ2ZocVlBR2RkeVpVWmwzQ3BaVmZSZjhrTFZZTndQSTJNR2hieUtXSzdaNUdraVFlU3ZUNllBRFpNTUtTZUFJeTg3TTdIWGtib0ZKZmROZGk1NHVSeERfLXZoOHNGNmY1TTlqZGpVWjl2Sg?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNelVwdm5oMDVMRW1lazFacTZYZXpVTHNKQXNQbjBoREsyUkpBVHVDbnJWM2dHTXdYQTZmVG9hUDR5NjV0c2FoWVFsaExLRXRBUWlGTUhBV0taQkRMbTQtZmpNbzR1TGxaUFNfWHgyM3NyMnU2VWxPTTRpRW0zczEwUm9vMm1Kc2ViMTZBM2MxeVZDQmxTQWR0T0ZRa3pFSmVVS29NczJHQTAzaVZSMUhITTZibjhNamFlQ2pr?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQRG90Z3ZXaHhwb050bTI2cmlubU9XTVk0YUlrZ0lBLUxMUDQ5SlZ0UXBUVml4VGhLN21veURwaThVSzRZT2pibGVXMkNuVWxPTkV5VmNuQXB0WVJKVm9oSzg4RlJqRGFDejA1R1FHTlhYVF9zVVd2eXpjUGFyM01STFVKY0JwajdBRW1yc0YzLUpnQQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPV21XaVk3OHBCQXdGdElzYmNzTUI1ek5pQzF2T1Z5SHRZTzd0MENiMEJBQV9ya0N1Wk91LURJTlRDa1lPZ1lvRklEOHY3QVFCU2tCM19aSENsMjRYalFsRnFxcnlZR3E5M0ZHZHVXdll2OWVRYzBtWkg5WnlDUkVHWXpkdDU1T2N2SXdFOWRDeFNndld3NS1vVEZYN2hrQQ?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNV1J2alhFSlhSeFc5cG9KRWZ3R0hGd013SC1hc3lFcjRNVE8tdnpyc2lnS0FSUDJ6Qzc1SWhtUk5QZ2pkX3V0U0R1U3h3WWNOMENqUjJYdlkxSmdOYlVfcEluQ3phV1NUNjVCS3pHNkN1QWx0Nnp3ZFBVbXZmcmp0dEYxT1F5YXEtMlNmZmhzVWZxSmhYa010dUx3SHFPSVZxOEFma2xDa0JxZzdNeG9KVnljSW4?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPdUdkNlU1SG9TdmdNNU9IQW1tZl9lLVBFR1QzNUdUQVl4TzVxY3NfY3VLQW1BWmhpWDNlTjlTUC1rUTlXbEFXYUdmS0dMWHJkOUR0NTR1RXc0X3pGb1VPY0FJSjc5ZU5XbFRTMEJQQXFHaFpPMHZ3a2t0Vmo5c2w1a0FDc2JXZ3RqZlVid1pELVJ3T09OVERoOUhJUnQ?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNU1J4THBrTkV3M19WbEtScExWeGVyeUtlOGdEZHB5WE95NVo1dlBrMlp1b1JFXzBnQnd0Q3ZSaXFlNGdYWGJKYjhlaGMtS3NtOHEySFBqWVBSaVZFV0dRaG1qY19pZDgtc2N0R3pGd0R0VG1GdnlyX1RRajFrU1dpdTRNajE4amplYk5ubkF2WWV5WWc?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQUE96UGhWZTA3MG1KVjNmaHBYZjVuRHNHVXBnMzlHQ1NRajBRRS11WTVhYmNGSGFNYkFjU281Q3phU1lpVkI5RmhOdGtOUXVDbHhMSFNNaVhjVjQ0SnZ4YzlZWWthYWVTazdCb3A0LU5mVHVkNzh0clgxNU5qQUZBcENoYjBzbnQ4dURlWDk4aTNEZ3ZYQ0xqRg?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxQWm51RHk0MnZpTDZrTWFTR0l5RDJyTVBFWFBEQTNoVHZmQUNxLS1lMTlyNzJKajJkd1RHOW1LRVBPaFR5djF1aUJEV0ZxamlhTTZOUUhBSXVEenMzRVN1S05qZ282V3ZYa0xIa0FJVE52c1NNN08xbEUxaFQ2VXZldkN5cw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQd0FwdWhPal9UUHpiMk44MFFyUlpwbzBaZFl5VEFLTm5uZjRuTndoRkFZYmZtMm41M0x2SEVaNVdMcVpHdHBndVByeFpDTk1xOTVGcGkzY2Q2UXozRWtiWVZpY3pDNlVBd3p2aHR4VHVoSzF5ZlkzVWlDQ0FKNXFpMWk0eUJVMDRFa1FGQXAwaDAwMDhSYUJwejBR?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxOTE1UT2VEX281LUxZd1BjS1ZTYU9wQmpvdnVqQjUyRk1MUjVXTm1tRjhkRFI3MDVjT3c5dFBYNDl2MU5zQnd0X0RqODdXbEJSNnA3NnpFdGFKRWVEcTBwMmcxOE4wREU1ajdGRHUwSjg2RFhFTVU2Z19XUTBTYlVGd3RuUQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPcFNnQTlwa05zX0NIRktFcVBSaF9RMTFkVXJUbERZNFlVTzdqM2FGdDkwQVFtdGpnQUhtU2hqSklFb1VLOWkwT1RsWEE2Mzg4cmsycFE1VndieDBjZzJDU0dVeWpwU3VXdlhMNXBtWlRoYVd1YnNIQmEtY2JBVFBpdldSVlFiT2RLeVVYT3dHTGp6bTM5LXFfRVhVYnJPMVNUaC1GaVh2VlZVQTBx?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPUEk0MzFlS3ZUbzdJbjg3OHlCamtpbjBCYVZmWGNLWXZaZVNnRXlXNXl3aVJ5eFV4SW45UWFKaWY2MnFRTFVUVEItd01xdXk3V1lWZGNEZXNiMXdTc1FfZnRUQWZXdlRyV2x2U1loS3ZGYzRZU0JuTDhUNFV2NW0zTGZjRU5OcnRsYlNzeHl2NTI1U0V1U2N6WmJpRER4cXM1TFdkdlJzYnRpaEZvbUpCV2JCMGU0REptd01HemFoTUU?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxOM2p6T05vX25BSVZwY2wybTdXWk9xckdjb2lHcWo2TFlDN2Z0MEZJSm5hczdzUjNFOTlfSVlzUDFUbWU1SzFkOTBDazVGY09JeGIzSDdDMVVDYk83YjJfWmNLUEJkVlBSNy01dXRtNE5ELV9paDJnZGRsMXNjb1d3TXRHMzBxT2FDYkpxUVJobWhZZlpSVVBpb3RQSTJpZ2RWcFNzODc5WmR2aWhVa29MZmtmTzhDb1hfQTd0WlY1eldESkdqS3pIWHVCOVZYOTRBalo3STBTSdIB3AFBVV95cUxOd1hlNGtaRV91b1BLSU9pTVpKSG5sTkRreENZOW1zMWluTldoYzhhVlY5MC0zb3JacTFYbjJmRnFEQWtYSTBWc3ZQRjRab1R2eE1neDJwLVdBcXRkN0h3eVk0dmloOENQRUtJWWplUEdSYjlCVDFBYnYtLXVPZG9iU3RZcGpIaDR3cU40Q01WQTFMM01ESXBCY3AtQlRZdVI1VDE0Qi15eFkxWnFlMnljcG9TYmJleEJVWnZtWGNzSkRGejZ6Z05EUXJiVlc1d21QZ0V0RlpqWUR4VVY0?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOV0U3WERRLXdqM09NRmo1QVZkMGpRN2xncG5iZkJJTzBrcFhLa0ExNW94UjY0MmlKWUFHMEFmV0xReFNhNThEcTRFbC1VYU5XWVYzWE5RVGljWklmX1VGOEcwWndhd3FZalBCamZGR3lnQjM0cW5oRUVNRnRSazFTcTA3Qmc3UDdBVEpUUU9CZUJfVy13SExFUFAySUptYUE?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxORC1PS1FreEtDdjc3c0lRUTVvazRVVzBFVkNXYzNMMDBXRGV0R2Nfc1V5cjFlcnh6cHRhanE0a0dUbjByaGNBWExfcmpibDlYc1NoU3VYcjd2SzYzQ0hlcnh6WER0eXZUbHJQRUZ5WG5LS0NTRWxtTG1jcnJnMlVuOFJqaU1TbHg1dTFLLXdJQ21acXZ0MG5IMFZR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
