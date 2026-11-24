# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:21:43.157937+00:00**
- AI status: **Partial: 1 headline remains unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 6, 'ai': 10, 'unknown': 1, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261123T053847Z-45053549/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 32.0%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 140.2100 |
| Return 1D (%) | -0.2348 |
| Return 1W (%) | -4.2478 |
| Return 1M (%) | 3.2702 |
| Return YTD (%) | 0.6676 |
| Return 1Y (%) | -0.2998 |
| Annualized volatility (%) | 21.9970 |
| Beta vs SPY | -0.1520 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | 0.1215 |
| Downside deviation (rf=0, %) | 14.7589 |
| Sortino (rf=0) | 0.1811 |
| Historical VaR 95% (1D, %) | 2.2257 |
| Historical ES 95% (1D, %) | 2.7033 |
| Correlation vs SPY | -0.1035 |
| Tracking error vs SPY (%) | 27.8620 |
| P/E (trailing) | 17.64 |
| P/B | 8.58 |
| EV/EBITDA | 12.10 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 16.32 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.05 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.73 |
| MA50 | 134.1976 |
| Close vs MA50 (%) | 4.4803 |
| MA200 | 143.2073 |
| Close vs MA200 (%) | -2.0930 |
| RSI (14, Wilder) | 52.5212 |
| MACD (12,26) | 1.9796 |
| MACD signal (9) | 2.5538 |
| MACD histogram | -0.5742 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 140.2100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.2348 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.2478 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.2702 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 0.6676 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -0.2998 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.9970 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.7589 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1811 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.2257 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7033 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1035 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 27.8620 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1520 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1215 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.3151 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.0460 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.7335 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.6365 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 52.5212 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.5742 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.4803 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -2.0930 -> Slightly below the moving-average trend level.

## TAILWINDS

### PepsiCo (PEP) Stock May Be 50% Undervalued Following Partnership Renewal
- Summary: Partnership renewal may signal undervaluation, boosting investor confidence.
- Date: 2026-11-21 | Impact: high | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNQ0V2bUwxb1Y4Y2NrS2ZkNm1LOWx5S19rLUJHSVhyZy1lLWJEZVVsMng0R05OWUV2NlN3S1hVVXVzUndlZnJMV3ppQUNuT3dsMFF3cjE0RlpZTXVXSE90dVJzQ05CWlJtRm1KWFdJMm1HdkNrV2ZQdkhQQ2NzOFNLRkVOWjlUZ3NFdmNSMzJNWHFURG1vOV9SZDFPV3N6SHFXOEN4eVpUU3NleUNSRlZOZWZweHB3S09QcFA1bnBPaTFIcHVCbDhOZVotS0dkVkhqUUR4UNIB2gFBVV95cUxPaU9CUFBiUnptNnFLNVE5MlFhdEEyYlI2MXEtNEhRLVlMS1pDOEdoc0NQbkRvQUc5eDhfV3ZOUW96M3FtbDBweElJdTZrZEl4ZWQ3YjNtUzFnU3BUbG9vdGZtQkVjbXVvbWhHd3lwa3AycnhacGg2MW5pSjZtY0sxZ1pMSFluUEJSRUZEOTFZbzVWTnRUb0g2cEhPWGFhTlZQaS1fQ0lkMU00MXFORjVsUTZySVMydTV6ZUZydER4SC1Rck5jM2Q4dkZWWjRydFhfMDQ1dElKMk8yZw?oc=5>

### What Keeps PepsiCo (NASDAQ:PEP) Extending Its Multi-Decade Dividend Growth Record?
- Summary: PepsiCo maintains its long-term dividend growth record, signaling stable shareholder returns.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQQ2tWWURnMURwOHZrWFpfNzVUTVVaMjFFLUExSDRtTWRSOEJBTmR3cWFScGI4dXJXZjVBUHhvQ0lSRk16aHA0N2hWc2pNLUFweS0zTmxuTmZBMzItcTFpaDY4amN2YUl4N2pSb2I4ZWZnbmwxVTZvbmhMYVdhbmdYdG11aFVWd2tjZlowLTdZQ3NZRXYzelVocnlTSGFKMjNONDJlRERYc056OHM5dHlxbUhWU1B2OV92TS1MNHNWRQ?oc=5>

## HEADWINDS

### PEP Stock Slides As Bernstein Downgrades PepsiCo, Warns Of Earnings Shortfall
- Summary: PEP Stock Slides As Bernstein Downgrades PepsiCo, Warns Of Earnings Shortfall
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPRjhZY3hqYUFlSUMyNV9URTM2Z1czQjI1aUl2QTFfOVk2azN1VC1PS1hYN1pqMGExOERjU20zSEp6Y3VKUGZNRFhkbV9TQi1vczJRLWRnY0swZ0x4ZmFsZTkwVXBJZU5TRHR1TWpLdzBRX3h4OVZaVWhINURxYzNSNVBpMHFqYlpzejllaE1QZW1JRHdndVhob1VEa0VpTVB4Y2gxYg?oc=5>

### PepsiCo (NASDAQ:PEP) Shares Down 2% - Here's What Happened
- Summary: PepsiCo (NASDAQ:PEP) Shares Down 2% - Here's What Happened
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQcEFNWVBPdy1VeEF0aGZxckFGOEhIN210Vk44UENtYXZjRm5meFhPejZWWTJlN0hHNGtiWU5fdkJXaFBOcEJadkJZTlZjd3JMM19IVU1JeTlRWjNralR0N1Z2YnlrOVo1Vm1GUE82MndMV3lOcWg2cXdtbzBJT2UxSWFoaExCdjNESUtqS1BBc1k1RE5mNjlOZXphS2RlWG43Qy1SY2lEdlI2MWFJUjBxT3R3?oc=5>

### Bernstein Sees Trouble Ahead for PepsiCo (PEP). Here’s Where.
- Summary: Bernstein research warns of future challenges for PepsiCo.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxOT3ctYUZMSGdjY2o2WFJvcElIdkZWcHlUd2NweGxJRFpHLVhvVzJQaENEMVpXTGlNamhPU28wd1JEMWhSRzRIU0dSdHNGa3JwcFpBTUxlSUw0alVSVEtEc00xYXBTVEl5NkZfOHM2R3ZIeWZxRTVHUi02THNMRk91eTFZR2p6YzRIY2lLWTktUFlMdHNwXzRxZjlac1oyODVFX2NJ?oc=5>

### Could PepsiCo Be The Value Stock For Your Portfolio?
- Summary: Opinion piece on PepsiCo as a value investment.
- Date: 2026-11-17 | Impact: low | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNWlJCOW9wd2tPRXh5dHpPLV95R0pCQkdFR1o1cFNYSnFzMlVXWG1kRGxHeGJ0NV9QR2gzM0dqTmJJaUdCQUprTWRNVmxMUmFfNzZvcW1MUVRGU1pZemVVWmxhd0syYTNaU2hjbWVHMDdmaW1mUnhPZWhJQXl6S3dmZ0lDOFlsQXpCMG1NOEpFSmVZaHBfeUlMRzZTS2JIWWd3R0E?oc=5>

## CATALYSTS

### PepsiCo Declares Quarterly Dividend
- Summary: PepsiCo Declares Quarterly Dividend
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPZlJSVjZEQWNRbmlCdE9hd2c2VzcyY0R6dFBIeTV0TGpVa1paVm9obUdCRXFTZzFTN0k0LTAtbk0xMEdJcFRDQjBDQ1hMN09GTGNGLWVXTzRTWHhEOFZzcHRLZ3NvQzlhUWhrZkdKQkNwTm1ORTBXYjFCTl9Xc1gxWVRoTWNTWjRiWUVEOGVvcWw5RnJFOFFyNFBLM2FVbjRVclE?oc=5>

### PepsiCo (PEP) Shelf Filing Leaves Investors Asking If The Stock Is Already Fairly Valued
- Summary: PepsiCo (PEP) Shelf Filing Leaves Investors Asking If The Stock Is Already Fairly Valued
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxPYnFEbHFZX3FuWkpHeWxoRjJtb0RJX09sbnFVclVHSWJTcmREQmdwVldaUVJvU1JETk1TZk4tVkVoTTRtSDM3TS1NTHZYT3NTazdwTnAtbzNzN2ZrS0Fld25nWUE3cElGZVlvenFJY3lVbFRTWjdOUWdPdGZWLW9xdTJ0ZjEyVXZqSzlxUzgwWUJjaWF0b3o2WTJYVWN6MXltQ1pvRnluSnJ4Z3BLMzJKUG9FRGRhWkxmYVUxTkZnS3RwaVpuOVBaZUFiaW0xaXp1MUlhONIB2gFBVV95cUxPY1RDT3BNamFzeFl5MElfMVFfVnd3UlNzQlM0MGlfWG1SRFhuRDQwQm5NdXpHa2FPNHFHWGtkNDZuMGs1cVlwYW9NTEFEWm9hT0tPOUc2RUttUEtteFhxdzREaEZrZEpIMGJ3R3k0OTJVSmdsMThxR2J3NzAzUUpTUUVYbFpmOEtfelFSY0hFR1BvbnY0MXZ5M0lfS0JfRndmaEhMMGtZVy1SenJnb3EyMTZHVEktT2xrUnUxWE9BUkF3eWZGUG85ZGNYdXpkU3RNMGI0NVkxdDV1Zw?oc=5>

### PepsiCo Has Raised Its Dividend 54 Straight Years. Here's What $10,000 Invested Pays Annually.
- Summary: PepsiCo Has Raised Its Dividend 54 Straight Years. Here's What $10,000 Invested Pays Annually.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxORU9WSnJGbDh4cXZJNVNOX2IyV2FGa0hSU0pQblJvY1E4YjVqRWxmdzF2R1JuY3B2dHM2UFBodEppUWVBLTZtNW9NNmNKdXpYNTM0dlBVOVgtam1kU01LZW1CVjFsZkszZjI4U0R6RUt4REczenhHVXFmMDB0anFzZDRpWUdxSXZPTDdRd0kxNUxUYWJoNUd4Q2tOeVNmVl9EbkJqSkt3aWZlbFlOallkLUkyWVpHTWFwRmJnbkg4Yml3RWI0RHhLU2thRDg?oc=5>

### PepsiCo marks 54 straight years of dividend increases. Its quarterly payment is $1.48 per share.
- Summary: PepsiCo marks 54 straight years of dividend increases. Its quarterly payment is $1.48 per share.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxOOVFaZzg0YzNNODF4UnFpNlBlM210Q0Z6OC12ZXgxYjBjcTh6SEpBN0xwQVFIdXcxVVZsekYyZ1d2X3NHYVl2cEhmdVRvb1dIaEMzaVFWZU50VkFvcGQ3WTlRSGR6Xy1uSS1NWHUzYTlQWlJkandhdE9HbnExUXVTLVlkRnlack0z?oc=5>

### PepsiCo Inc Stock (PEP) Moved Down by 3.26% on Nov 17: A Full Analysis
- Summary: PEP stock fell 3.26% on Nov 17.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQSnFfcTFhcDhibXBiU0xsSGVpUkxBREgzQTkwenllRm9xUUc4SGoxcG9ZV1UyN2xfd093RzZicTc4amxLSlEyWm1HdjcyZG5QOHdsc0hvYW1lWVpkLVFNWG5LcWEzb2JZdmsyS1RhNGNjQVJJajF2bW5TNW56WEoxZkwtQkNUMUZFLUE?oc=5>

### Why Is PepsiCo Stock Falling 1.8% Following Bernstein Analyst Downgrade?
- Summary: PEP stock fell after Bernstein downgrade.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNX19hOEJfa1BFWTFhZTFicjhMNmZ4RzV0M1NlS3ZFMDBlVnp1ZlpaMW5ua1ZWNC1vNENiT2REVWEwYUx0VUJxYzlpX18yUjhla2o2UlNiaXlyU25YMDFZX2xRSlp3M0o4N0pfdUpZdGZrSzJ1eDN0Q3JvNGRKeEJvN2tLUjVCdE5ucnNackVROXhISUdCX01r?oc=5>

### PepsiCo Analysis - Is PEP About to Break Out? - PepsiCo (NASDAQ:PEP)
- Summary: Analyst review of potential breakout.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNelFianZTb3o2VFNiNVZNaTVWRThFQ2g0dldQSGI4bWM2UUhDb2ZrQ05TSm1ndm9JSHZFYlZLVnBiVDJacHNSTFk2cWFJT3hQZVNmNnptSHhmTWE3QThmbFFSLTBJelZPSnpSVjhxV2d4WWJQVmVhdmRVVkdUcXRyREFUSW9DRW41aDZUT2tVV05LS05idDBjOE14S2E0dkxWblZVZlB2bThOSlpHMlE?oc=5>

### $400,000 in PepsiCo and Kimberly-Clark Pays $17,845 a Year in Dividends
- Summary: PepsiCo dividend payout of $17,845 per year on $400,000 investment.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNc1VTV3Z4T0ZpZkdWbHI4Q3IxYlMwY3FlMDNrVlZrSFVtYzA4RGJZOHo2Z3AycEVvVnl1QUhmLXQxZDViRjVUM1czRGF5TVFCUkJDWmU4VHJBNEI4Mms2b3FaX1dyRERlcVA3VlhXMDlWZHF6YjFaazlZX1J3cG9CdlhiVkJhWk5RU1F1WXRRb2MxeDhkWFVLLWRUV2ktdzBQSFRuZHpRSGw2c0NMZDRHSg?oc=5>

### PepsiCo vs. Starbucks: Which Consumer Goods Stock Is a Better Buy for 2027?
- Summary: Analyst comparison of PepsiCo and Starbucks for 2027 investment prospects.
- Date: 2026-11-22 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPNVpCWUpueGFzYmNJVHptd3ZWTXQ4QWJ6Zk5VUGxreFJQOGlmbHI4X3RJTXRIdG1ZLXNVS2hZU3RvQWtpNlJBbk5USzFidXRLYzZOLXh6aWNvZWc3aThKb0hJc3RnYVRuQ0p0WnZ5YXpVVnlidFIzMVRpaW02WjVhRy1DUzNJYXV3S2JMZzFob21acVlYYVNZRTRySS03QjJHQWc?oc=5>

### PepsiCo (PEP) Stock May Be 49% Undervalued Following Margin Concerns
- Summary: Margin concerns may be driving a 49% undervaluation of PepsiCo stock, indicating potential downside risk for investors.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQVUdmVlJzZ1hCcW1ubUtSVU5sUnpPTkNmUklJOHhRRG1DVV92MkZKVWd6YkVaU0lLTml2dmJ0b1pyZkpLSFVJYnpXcXE5T1hJSkVoQWlhQWxzWWlCS3AtOTNLdnkyaGNYVG5MMVBiSVZXWmYweXJubkFQcEhadDZOUGxmdGRXdm1vWHJOQU9JcXdydGs?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **17.64** | **8.58** | **12.10** | **5.60** | **191,069,945,856.00 USD** | **-0.30** |
| KO | 28.28 | 11.04 | 25.25 | 7.40 | 412,466,380,800.00 USD | 34.93 |
| MNST | 38.57 | 8.44 | 26.67 | 16.70 | 83,057,229,824.00 USD | 17.80 |
| KDP | 31.92 | 1.90 | 16.40 | 70.60 | 50,580,398,080.00 USD | 31.79 |

Peers fetched as_of: 2026-11-23; PEP reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-08
- Revenue (latest available single quarter): 25,274,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,048,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/77476/000007747626000048/pep-20260905.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNQ0V2bUwxb1Y4Y2NrS2ZkNm1LOWx5S19rLUJHSVhyZy1lLWJEZVVsMng0R05OWUV2NlN3S1hVVXVzUndlZnJMV3ppQUNuT3dsMFF3cjE0RlpZTXVXSE90dVJzQ05CWlJtRm1KWFdJMm1HdkNrV2ZQdkhQQ2NzOFNLRkVOWjlUZ3NFdmNSMzJNWHFURG1vOV9SZDFPV3N6SHFXOEN4eVpUU3NleUNSRlZOZWZweHB3S09QcFA1bnBPaTFIcHVCbDhOZVotS0dkVkhqUUR4UNIB2gFBVV95cUxPaU9CUFBiUnptNnFLNVE5MlFhdEEyYlI2MXEtNEhRLVlMS1pDOEdoc0NQbkRvQUc5eDhfV3ZOUW96M3FtbDBweElJdTZrZEl4ZWQ3YjNtUzFnU3BUbG9vdGZtQkVjbXVvbWhHd3lwa3AycnhacGg2MW5pSjZtY0sxZ1pMSFluUEJSRUZEOTFZbzVWTnRUb0g2cEhPWGFhTlZQaS1fQ0lkMU00MXFORjVsUTZySVMydTV6ZUZydER4SC1Rck5jM2Q4dkZWWjRydFhfMDQ1dElKMk8yZw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQQ2tWWURnMURwOHZrWFpfNzVUTVVaMjFFLUExSDRtTWRSOEJBTmR3cWFScGI4dXJXZjVBUHhvQ0lSRk16aHA0N2hWc2pNLUFweS0zTmxuTmZBMzItcTFpaDY4amN2YUl4N2pSb2I4ZWZnbmwxVTZvbmhMYVdhbmdYdG11aFVWd2tjZlowLTdZQ3NZRXYzelVocnlTSGFKMjNONDJlRERYc056OHM5dHlxbUhWU1B2OV92TS1MNHNWRQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPRjhZY3hqYUFlSUMyNV9URTM2Z1czQjI1aUl2QTFfOVk2azN1VC1PS1hYN1pqMGExOERjU20zSEp6Y3VKUGZNRFhkbV9TQi1vczJRLWRnY0swZ0x4ZmFsZTkwVXBJZU5TRHR1TWpLdzBRX3h4OVZaVWhINURxYzNSNVBpMHFqYlpzejllaE1QZW1JRHdndVhob1VEa0VpTVB4Y2gxYg?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQcEFNWVBPdy1VeEF0aGZxckFGOEhIN210Vk44UENtYXZjRm5meFhPejZWWTJlN0hHNGtiWU5fdkJXaFBOcEJadkJZTlZjd3JMM19IVU1JeTlRWjNralR0N1Z2YnlrOVo1Vm1GUE82MndMV3lOcWg2cXdtbzBJT2UxSWFoaExCdjNESUtqS1BBc1k1RE5mNjlOZXphS2RlWG43Qy1SY2lEdlI2MWFJUjBxT3R3?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxOT3ctYUZMSGdjY2o2WFJvcElIdkZWcHlUd2NweGxJRFpHLVhvVzJQaENEMVpXTGlNamhPU28wd1JEMWhSRzRIU0dSdHNGa3JwcFpBTUxlSUw0alVSVEtEc00xYXBTVEl5NkZfOHM2R3ZIeWZxRTVHUi02THNMRk91eTFZR2p6YzRIY2lLWTktUFlMdHNwXzRxZjlac1oyODVFX2NJ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNWlJCOW9wd2tPRXh5dHpPLV95R0pCQkdFR1o1cFNYSnFzMlVXWG1kRGxHeGJ0NV9QR2gzM0dqTmJJaUdCQUprTWRNVmxMUmFfNzZvcW1MUVRGU1pZemVVWmxhd0syYTNaU2hjbWVHMDdmaW1mUnhPZWhJQXl6S3dmZ0lDOFlsQXpCMG1NOEpFSmVZaHBfeUlMRzZTS2JIWWd3R0E?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPZlJSVjZEQWNRbmlCdE9hd2c2VzcyY0R6dFBIeTV0TGpVa1paVm9obUdCRXFTZzFTN0k0LTAtbk0xMEdJcFRDQjBDQ1hMN09GTGNGLWVXTzRTWHhEOFZzcHRLZ3NvQzlhUWhrZkdKQkNwTm1ORTBXYjFCTl9Xc1gxWVRoTWNTWjRiWUVEOGVvcWw5RnJFOFFyNFBLM2FVbjRVclE?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxPYnFEbHFZX3FuWkpHeWxoRjJtb0RJX09sbnFVclVHSWJTcmREQmdwVldaUVJvU1JETk1TZk4tVkVoTTRtSDM3TS1NTHZYT3NTazdwTnAtbzNzN2ZrS0Fld25nWUE3cElGZVlvenFJY3lVbFRTWjdOUWdPdGZWLW9xdTJ0ZjEyVXZqSzlxUzgwWUJjaWF0b3o2WTJYVWN6MXltQ1pvRnluSnJ4Z3BLMzJKUG9FRGRhWkxmYVUxTkZnS3RwaVpuOVBaZUFiaW0xaXp1MUlhONIB2gFBVV95cUxPY1RDT3BNamFzeFl5MElfMVFfVnd3UlNzQlM0MGlfWG1SRFhuRDQwQm5NdXpHa2FPNHFHWGtkNDZuMGs1cVlwYW9NTEFEWm9hT0tPOUc2RUttUEtteFhxdzREaEZrZEpIMGJ3R3k0OTJVSmdsMThxR2J3NzAzUUpTUUVYbFpmOEtfelFSY0hFR1BvbnY0MXZ5M0lfS0JfRndmaEhMMGtZVy1SenJnb3EyMTZHVEktT2xrUnUxWE9BUkF3eWZGUG85ZGNYdXpkU3RNMGI0NVkxdDV1Zw?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxORU9WSnJGbDh4cXZJNVNOX2IyV2FGa0hSU0pQblJvY1E4YjVqRWxmdzF2R1JuY3B2dHM2UFBodEppUWVBLTZtNW9NNmNKdXpYNTM0dlBVOVgtam1kU01LZW1CVjFsZkszZjI4U0R6RUt4REczenhHVXFmMDB0anFzZDRpWUdxSXZPTDdRd0kxNUxUYWJoNUd4Q2tOeVNmVl9EbkJqSkt3aWZlbFlOallkLUkyWVpHTWFwRmJnbkg4Yml3RWI0RHhLU2thRDg?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxOOVFaZzg0YzNNODF4UnFpNlBlM210Q0Z6OC12ZXgxYjBjcTh6SEpBN0xwQVFIdXcxVVZsekYyZ1d2X3NHYVl2cEhmdVRvb1dIaEMzaVFWZU50VkFvcGQ3WTlRSGR6Xy1uSS1NWHUzYTlQWlJkandhdE9HbnExUXVTLVlkRnlack0z?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQSnFfcTFhcDhibXBiU0xsSGVpUkxBREgzQTkwenllRm9xUUc4SGoxcG9ZV1UyN2xfd093RzZicTc4amxLSlEyWm1HdjcyZG5QOHdsc0hvYW1lWVpkLVFNWG5LcWEzb2JZdmsyS1RhNGNjQVJJajF2bW5TNW56WEoxZkwtQkNUMUZFLUE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNX19hOEJfa1BFWTFhZTFicjhMNmZ4RzV0M1NlS3ZFMDBlVnp1ZlpaMW5ua1ZWNC1vNENiT2REVWEwYUx0VUJxYzlpX18yUjhla2o2UlNiaXlyU25YMDFZX2xRSlp3M0o4N0pfdUpZdGZrSzJ1eDN0Q3JvNGRKeEJvN2tLUjVCdE5ucnNackVROXhISUdCX01r?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNelFianZTb3o2VFNiNVZNaTVWRThFQ2g0dldQSGI4bWM2UUhDb2ZrQ05TSm1ndm9JSHZFYlZLVnBiVDJacHNSTFk2cWFJT3hQZVNmNnptSHhmTWE3QThmbFFSLTBJelZPSnpSVjhxV2d4WWJQVmVhdmRVVkdUcXRyREFUSW9DRW41aDZUT2tVV05LS05idDBjOE14S2E0dkxWblZVZlB2bThOSlpHMlE?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNc1VTV3Z4T0ZpZkdWbHI4Q3IxYlMwY3FlMDNrVlZrSFVtYzA4RGJZOHo2Z3AycEVvVnl1QUhmLXQxZDViRjVUM1czRGF5TVFCUkJDWmU4VHJBNEI4Mms2b3FaX1dyRERlcVA3VlhXMDlWZHF6YjFaazlZX1J3cG9CdlhiVkJhWk5RU1F1WXRRb2MxeDhkWFVLLWRUV2ktdzBQSFRuZHpRSGw2c0NMZDRHSg?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPNVpCWUpueGFzYmNJVHptd3ZWTXQ4QWJ6Zk5VUGxreFJQOGlmbHI4X3RJTXRIdG1ZLXNVS2hZU3RvQWtpNlJBbk5USzFidXRLYzZOLXh6aWNvZWc3aThKb0hJc3RnYVRuQ0p0WnZ5YXpVVnlidFIzMVRpaW02WjVhRy1DUzNJYXV3S2JMZzFob21acVlYYVNZRTRySS03QjJHQWc?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQVUdmVlJzZ1hCcW1ubUtSVU5sUnpPTkNmUklJOHhRRG1DVV92MkZKVWd6YkVaU0lLTml2dmJ0b1pyZkpLSFVJYnpXcXE5T1hJSkVoQWlhQWxzWWlCS3AtOTNLdnkyaGNYVG5MMVBiSVZXWmYweXJubkFQcEhadDZOUGxmdGRXdm1vWHJOQU9JcXdydGs?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
