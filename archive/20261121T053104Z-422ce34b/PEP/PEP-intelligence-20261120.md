# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-11-20**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-11-20**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-21T05:37:35.494453+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 7, 'ai': 10, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261120T053808Z-e360129e/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 13 named publishers; 0 exact duplicates; 23 HTTPS source links; largest publisher share 30.43%; oldest publication 2026-11-14

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 140.5400 |
| Return 1D (%) | 1.1079 |
| Return 1W (%) | -3.3691 |
| Return 1M (%) | 4.8649 |
| Return YTD (%) | 0.9045 |
| Return 1Y (%) | 0.0921 |
| Annualized volatility (%) | 21.9597 |
| Beta vs SPY | -0.1639 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | 0.1133 |
| Downside deviation (rf=0, %) | 14.7385 |
| Sortino (rf=0) | 0.1687 |
| Historical VaR 95% (1D, %) | 2.2237 |
| Historical ES 95% (1D, %) | 2.7033 |
| Correlation vs SPY | -0.1067 |
| Tracking error vs SPY (%) | 27.4510 |
| P/E (trailing) | 17.48 |
| P/B | 8.60 |
| EV/EBITDA | 12.12 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 16.35 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.05 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.72 |
| MA50 | 134.1202 |
| Close vs MA50 (%) | 4.7866 |
| MA200 | 143.3335 |
| Close vs MA200 (%) | -1.9490 |
| RSI (14, Wilder) | 53.2382 |
| MACD (12,26) | 2.2359 |
| MACD signal (9) | 2.6974 |
| MACD histogram | -0.4615 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 140.5400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.1079 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.3691 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.8649 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 0.9045 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.0921 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.9597 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.7385 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1687 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.2237 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7033 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1067 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 27.4510 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1639 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1133 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.3535 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.0460 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.7224 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.4801 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.2382 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.4615 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.7866 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.9490 -> Slightly below the moving-average trend level.

## TAILWINDS

### PepsiCo Analysis - Is PEP About to Break Out? - PepsiCo (NASDAQ:PEP)
- Summary: Potential positive price breakout indicated.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNelFianZTb3o2VFNiNVZNaTVWRThFQ2g0dldQSGI4bWM2UUhDb2ZrQ05TSm1ndm9JSHZFYlZLVnBiVDJacHNSTFk2cWFJT3hQZVNmNnptSHhmTWE3QThmbFFSLTBJelZPSnpSVjhxV2d4WWJQVmVhdmRVVkdUcXRyREFUSW9DRW41aDZUT2tVV05LS05idDBjOE14S2E0dkxWblZVZlB2bThOSlpHMlE?oc=5>

## HEADWINDS

### PepsiCo Stock Drops 2.4% in 6 Months: Is More Downside Ahead?
- Summary: PepsiCo Stock Drops 2.4% in 6 Months: Is More Downside Ahead?
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQTGxPZHJlX29nNVVYSmZzUlNmaXBSOVBDd0RyOXZ1ZmMtX040ZzR5VDNDTWp4YWVJaTEyazFkZmsxN2MtOEtMdW9kWVV6UW5vckFxUzlVM3pNVGRxTi1iekVUbnZ0LWVuazY2SmFlZVRPWGF0RVdBak45WlQzLW9lbEx0V0JxY3FKN2ctbFI4TS16QQ?oc=5>

### PepsiCo (NASDAQ:PEP) Shares Down 2% - Here's What Happened
- Summary: PepsiCo (NASDAQ:PEP) Shares Down 2% - Here's What Happened
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQcEFNWVBPdy1VeEF0aGZxckFGOEhIN210Vk44UENtYXZjRm5meFhPejZWWTJlN0hHNGtiWU5fdkJXaFBOcEJadkJZTlZjd3JMM19IVU1JeTlRWjNralR0N1Z2YnlrOVo1Vm1GUE82MndMV3lOcWg2cXdtbzBJT2UxSWFoaExCdjNESUtqS1BBc1k1RE5mNjlOZXphS2RlWG43Qy1SY2lEdlI2MWFJUjBxT3R3?oc=5>

### PEP Stock Slides As Bernstein Downgrades PepsiCo, Warns Of Earnings Shortfall
- Summary: PEP Stock Slides As Bernstein Downgrades PepsiCo, Warns Of Earnings Shortfall
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8AFBVV95cUxNRVI2RjRxQnBRUGtlcTY3MXZ0UDhYSDBSTnY3OHlGeVJNZG9paFBOQlZvRldnLXhZWlpOcUpJdUYxak9hTHNVMnIyTmNVX05UX1BjQllrQmtHcTlUblVqdllJbDFmN2VmakVFZVF2Y21VRWZmamRya2ZMSF85REZNTWhlQm0xVU1fNU9qX3BpZUl0NTBvRXNkY00wbjJnbjZPRW90NHpFUlNSMU9IYXltSlhlb2JuQWNONDBLaEhBQ0RWOE9FeTIwUWVENEdRVmgydzhOQ2k3THBRRFEwRlN6a1JBMDJyVDM2QlNZYjFGYms?oc=5>

### PepsiCo (PEP) Stock: Drops as Company Secures 10-Year Beverage Deal With Hyatt Across 700+ Hotels in America
- Summary: PepsiCo (PEP) Stock: Drops as Company Secures 10-Year Beverage Deal With Hyatt Across 700+ Hotels in America
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxOd3BCalBHdHFNYWxZdnU1Mi1FSmlTZ1ExeVhNV1VHaGZINVNydFd1SlZaaGhFVWtCS1BSUGdXd1dTSTNaY0RVVGlxWVUzdGdSZC1mOHJ6TVlNRFFxLU9WNW5fbGtzUUJMSV9hWWpNR0FtN1FmZFZ5RkdzTDFYd1czWFc1SklDbjlhNEtxc0ZMeVpabjdyR3k2ejBLZDZkeVd3VEYtSUVTNVJ0aGRqSnp5WmVqTzVxRmZfVUxRZW5semlqMHFmVDI0?oc=5>

### PepsiCo Inc Stock (PEP) Moved Down by 3.26% on Nov 17: A Full Analysis
- Summary: PEP shares fell 3.26% on Nov 17.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQSnFfcTFhcDhibXBiU0xsSGVpUkxBREgzQTkwenllRm9xUUc4SGoxcG9ZV1UyN2xfd093RzZicTc4amxLSlEyWm1HdjcyZG5QOHdsc0hvYW1lWVpkLVFNWG5LcWEzb2JZdmsyS1RhNGNjQVJJajF2bW5TNW56WEoxZkwtQkNUMUZFLUE?oc=5>

### Bernstein Sees Trouble Ahead for PepsiCo (PEP). Here’s Where.
- Summary: Bernstein research warns of future challenges for PepsiCo.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxOT3ctYUZMSGdjY2o2WFJvcElIdkZWcHlUd2NweGxJRFpHLVhvVzJQaENEMVpXTGlNamhPU28wd1JEMWhSRzRIU0dSdHNGa3JwcFpBTUxlSUw0alVSVEtEc00xYXBTVEl5NkZfOHM2R3ZIeWZxRTVHUi02THNMRk91eTFZR2p6YzRIY2lLWTktUFlMdHNwXzRxZjlac1oyODVFX2NJ?oc=5>

### Could PepsiCo Be The Value Stock For Your Portfolio?
- Summary: Opinion piece on PepsiCo as a value investment.
- Date: 2026-11-17 | Impact: low | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNWlJCOW9wd2tPRXh5dHpPLV95R0pCQkdFR1o1cFNYSnFzMlVXWG1kRGxHeGJ0NV9QR2gzM0dqTmJJaUdCQUprTWRNVmxMUmFfNzZvcW1MUVRGU1pZemVVWmxhd0syYTNaU2hjbWVHMDdmaW1mUnhPZWhJQXl6S3dmZ0lDOFlsQXpCMG1NOEpFSmVZaHBfeUlMRzZTS2JIWWd3R0E?oc=5>

### Bernstein cuts PepsiCo to Underperform, the only large-cap downgrade on Tuesday's wire
- Summary: Bernstein downgrades PepsiCo to Underperform.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxPSFF5ZnhMQmRUREhtTUlIZ3pQUS11aGg4RzlpdVdBTW44U2JlcXB5U2s5Slh1b0Fyc3g4UVdiM1d6dHU5VThqZUoycVRPRW5uZlhfeTNqMjd2NGxmT1owU1lzOWliVklVZmpYQ0FJUXczZ3BLWDBONDduVFFEY1JCVUdLdjA4SUFNTHJHc2lFeUFiSklRZzJQcUJsVnRCSXhFaDhKM3A0MkY1MkthaWEtRVpPTUk?oc=5>

### Bernstein Sees 13% Downside in PepsiCo
- Summary: Bernstein projects a 13% downside for PepsiCo.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMidEFVX3lxTE0ydVpHaDRMUXlqMzhlMm9oRkFaY1pwZTBsOHlxOHlGUTNoS0ZHMWpZRE9oUVg4TjdfdUZGUG9lYmozZXBIdHZlUVVOTF96VkVicTZxMWhqTmY1M0hPU0F4ZEFZUHhXUG9uQUg4ZnoySDVCZ0xj?oc=5>

### PepsiCo (PEP) Stock: $142.02, Down 3.01% Nov 17
- Summary: PepsiCo shares fell 3.01% to $142.02 on November 17.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOR0YxUVhzbnI1Y182U2M2MUxYUTB0Um0tb21nYnBVSlF2VDFfTnpMRDdxaHR0WmFFMWdwYklvb3dHQWw4NHNXV2FFSzdrbEpjekdwWjFFYV9Oc3VQQ1I2T3hqbEVVTlBOdzlpTE9VX0ttQ1VpX2tGNlhpOFg5TUF5am9IS1BlQVRtMW5sQWlzWW56WHEzOVZ6ZGw4dG9iazV0bVFjMjVyU1ZEMlJEZ0VGbTlB?oc=5>

## CATALYSTS

### PepsiCo (PEP) Lands Hyatt Deal On A Fair Value Debate
- Summary: PepsiCo (PEP) Lands Hyatt Deal On A Fair Value Debate
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNTVFiVXNnMmNNTlZ4UzA0QlFEZV94WVluckhCT1hsVjJnTXc5NkhiRnVyR0tTQ3phaWNDci0xZWpjQmpoWjA0X2JTU3dzalcyc1djU3gxY0hDV0ZKM0lBZDhINS1LM3VvMHRLUHpTbVhqTVdQb2I1ZU1nbS1BazlCS1pUSWp0TjUtX1NaZDRYVmZzR0VNUDZUeA?oc=5>

### PepsiCo Has Raised Its Dividend 54 Straight Years. Here's What $10,000 Invested Pays Annually.
- Summary: PepsiCo Has Raised Its Dividend 54 Straight Years. Here's What $10,000 Invested Pays Annually.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxORU9WSnJGbDh4cXZJNVNOX2IyV2FGa0hSU0pQblJvY1E4YjVqRWxmdzF2R1JuY3B2dHM2UFBodEppUWVBLTZtNW9NNmNKdXpYNTM0dlBVOVgtam1kU01LZW1CVjFsZkszZjI4U0R6RUt4REczenhHVXFmMDB0anFzZDRpWUdxSXZPTDdRd0kxNUxUYWJoNUd4Q2tOeVNmVl9EbkJqSkt3aWZlbFlOallkLUkyWVpHTWFwRmJnbkg4Yml3RWI0RHhLU2thRDg?oc=5>

### PepsiCo Declares Quarterly Dividend
- Summary: PepsiCo Declares Quarterly Dividend
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPZlJSVjZEQWNRbmlCdE9hd2c2VzcyY0R6dFBIeTV0TGpVa1paVm9obUdCRXFTZzFTN0k0LTAtbk0xMEdJcFRDQjBDQ1hMN09GTGNGLWVXTzRTWHhEOFZzcHRLZ3NvQzlhUWhrZkdKQkNwTm1ORTBXYjFCTl9Xc1gxWVRoTWNTWjRiWUVEOGVvcWw5RnJFOFFyNFBLM2FVbjRVclE?oc=5>

### $400,000 in PepsiCo and Kimberly-Clark Pays $17,845 a Year in Dividends
- Summary: PepsiCo dividend payout of $17,845 per year on $400,000 investment.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNc1VTV3Z4T0ZpZkdWbHI4Q3IxYlMwY3FlMDNrVlZrSFVtYzA4RGJZOHo2Z3AycEVvVnl1QUhmLXQxZDViRjVUM1czRGF5TVFCUkJDWmU4VHJBNEI4Mms2b3FaX1dyRERlcVA3VlhXMDlWZHF6YjFaazlZX1J3cG9CdlhiVkJhWk5RU1F1WXRRb2MxeDhkWFVLLWRUV2ktdzBQSFRuZHpRSGw2c0NMZDRHSg?oc=5>

### PepsiCo (PEP) Cuts 1,000 Jobs, Is The Stock A Bargain?
- Summary: Job cuts could signal cost-cutting but may impact morale.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxOd1NlejQ3S3lTcnUyN2JrUm5YcUJxNldEZjQ4RHZFb0tZa1dPY1JwSU8wZzc1Zi0wRVFuSjNlS2NxTWE2b0hQUXVlcy1fNTdENWZPaDJYTTR2QWVFQnQ2eEpTRzJtbm9SV21SSUE1N0VCeFY5QzRmX1o5Mm0yQ1l5RjR4ZWh1d250R1RCMUhPdFp6TGFHcUhNbUIzMTV3MkRWcW1fUnlGME9GUmFTY2xfVzcyaHBuTUswSGdhX3J1Nk8tMGI2ZHfSAcsBQVVfeXFMT01IRERycWtBX1FPYW5mLXIzZVd5aHpPWjQyR2t0Zko5czBfbjFXVVNvMFdYS2hWTERtSWN0NVJyM2NDTDhIRnRLYWRxTzFWMXhwODlTNUUya1k2NGVtVXVlQU1paXo4Tzd4VTl4SVh0UE5mb0VNSjdiVDlBa3htM2xJbTBxX0FBUll6ZkJ2ZklmZHppTXMxSEZOTUpRMHZrSFRqeTVZa3QyMlFzcm51Y3BIQlBwWGJOeEVCQ1FFM0NSdVJLSmhSQ0ptRFk?oc=5>

### Why Is PepsiCo Stock Falling 1.8% Following Bernstein Analyst Downgrade?
- Summary: Bernstein downgraded PepsiCo, causing a 1.8% drop in its stock price.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNX19hOEJfa1BFWTFhZTFicjhMNmZ4RzV0M1NlS3ZFMDBlVnp1ZlpaMW5ua1ZWNC1vNENiT2REVWEwYUx0VUJxYzlpX18yUjhla2o2UlNiaXlyU25YMDFZX2xRSlp3M0o4N0pfdUpZdGZrSzJ1eDN0Q3JvNGRKeEJvN2tLUjVCdE5ucnNackVROXhISUdCX01r?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **17.48** | **8.60** | **12.12** | **5.60** | **191,519,621,120.00 USD** | **0.09** |
| KO | 28.61 | 11.16 | 25.53 | 7.40 | 417,241,497,600.00 USD | 39.82 |
| MNST | 39.72 | 8.69 | 27.50 | 16.70 | 85,523,693,568.00 USD | 20.99 |
| KDP | 31.11 | 1.86 | 16.25 | 70.60 | 49,738,104,832.00 USD | 32.12 |

Peers fetched as_of: 2026-11-20; PEP reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-20

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

- https://news.google.com/rss/articles/CBMirgFBVV95cUxNelFianZTb3o2VFNiNVZNaTVWRThFQ2g0dldQSGI4bWM2UUhDb2ZrQ05TSm1ndm9JSHZFYlZLVnBiVDJacHNSTFk2cWFJT3hQZVNmNnptSHhmTWE3QThmbFFSLTBJelZPSnpSVjhxV2d4WWJQVmVhdmRVVkdUcXRyREFUSW9DRW41aDZUT2tVV05LS05idDBjOE14S2E0dkxWblZVZlB2bThOSlpHMlE?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQTGxPZHJlX29nNVVYSmZzUlNmaXBSOVBDd0RyOXZ1ZmMtX040ZzR5VDNDTWp4YWVJaTEyazFkZmsxN2MtOEtMdW9kWVV6UW5vckFxUzlVM3pNVGRxTi1iekVUbnZ0LWVuazY2SmFlZVRPWGF0RVdBak45WlQzLW9lbEx0V0JxY3FKN2ctbFI4TS16QQ?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQcEFNWVBPdy1VeEF0aGZxckFGOEhIN210Vk44UENtYXZjRm5meFhPejZWWTJlN0hHNGtiWU5fdkJXaFBOcEJadkJZTlZjd3JMM19IVU1JeTlRWjNralR0N1Z2YnlrOVo1Vm1GUE82MndMV3lOcWg2cXdtbzBJT2UxSWFoaExCdjNESUtqS1BBc1k1RE5mNjlOZXphS2RlWG43Qy1SY2lEdlI2MWFJUjBxT3R3?oc=5
- https://news.google.com/rss/articles/CBMi8AFBVV95cUxNRVI2RjRxQnBRUGtlcTY3MXZ0UDhYSDBSTnY3OHlGeVJNZG9paFBOQlZvRldnLXhZWlpOcUpJdUYxak9hTHNVMnIyTmNVX05UX1BjQllrQmtHcTlUblVqdllJbDFmN2VmakVFZVF2Y21VRWZmamRya2ZMSF85REZNTWhlQm0xVU1fNU9qX3BpZUl0NTBvRXNkY00wbjJnbjZPRW90NHpFUlNSMU9IYXltSlhlb2JuQWNONDBLaEhBQ0RWOE9FeTIwUWVENEdRVmgydzhOQ2k3THBRRFEwRlN6a1JBMDJyVDM2QlNZYjFGYms?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxOd3BCalBHdHFNYWxZdnU1Mi1FSmlTZ1ExeVhNV1VHaGZINVNydFd1SlZaaGhFVWtCS1BSUGdXd1dTSTNaY0RVVGlxWVUzdGdSZC1mOHJ6TVlNRFFxLU9WNW5fbGtzUUJMSV9hWWpNR0FtN1FmZFZ5RkdzTDFYd1czWFc1SklDbjlhNEtxc0ZMeVpabjdyR3k2ejBLZDZkeVd3VEYtSUVTNVJ0aGRqSnp5WmVqTzVxRmZfVUxRZW5semlqMHFmVDI0?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQSnFfcTFhcDhibXBiU0xsSGVpUkxBREgzQTkwenllRm9xUUc4SGoxcG9ZV1UyN2xfd093RzZicTc4amxLSlEyWm1HdjcyZG5QOHdsc0hvYW1lWVpkLVFNWG5LcWEzb2JZdmsyS1RhNGNjQVJJajF2bW5TNW56WEoxZkwtQkNUMUZFLUE?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxOT3ctYUZMSGdjY2o2WFJvcElIdkZWcHlUd2NweGxJRFpHLVhvVzJQaENEMVpXTGlNamhPU28wd1JEMWhSRzRIU0dSdHNGa3JwcFpBTUxlSUw0alVSVEtEc00xYXBTVEl5NkZfOHM2R3ZIeWZxRTVHUi02THNMRk91eTFZR2p6YzRIY2lLWTktUFlMdHNwXzRxZjlac1oyODVFX2NJ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNWlJCOW9wd2tPRXh5dHpPLV95R0pCQkdFR1o1cFNYSnFzMlVXWG1kRGxHeGJ0NV9QR2gzM0dqTmJJaUdCQUprTWRNVmxMUmFfNzZvcW1MUVRGU1pZemVVWmxhd0syYTNaU2hjbWVHMDdmaW1mUnhPZWhJQXl6S3dmZ0lDOFlsQXpCMG1NOEpFSmVZaHBfeUlMRzZTS2JIWWd3R0E?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxPSFF5ZnhMQmRUREhtTUlIZ3pQUS11aGg4RzlpdVdBTW44U2JlcXB5U2s5Slh1b0Fyc3g4UVdiM1d6dHU5VThqZUoycVRPRW5uZlhfeTNqMjd2NGxmT1owU1lzOWliVklVZmpYQ0FJUXczZ3BLWDBONDduVFFEY1JCVUdLdjA4SUFNTHJHc2lFeUFiSklRZzJQcUJsVnRCSXhFaDhKM3A0MkY1MkthaWEtRVpPTUk?oc=5
- https://news.google.com/rss/articles/CBMidEFVX3lxTE0ydVpHaDRMUXlqMzhlMm9oRkFaY1pwZTBsOHlxOHlGUTNoS0ZHMWpZRE9oUVg4TjdfdUZGUG9lYmozZXBIdHZlUVVOTF96VkVicTZxMWhqTmY1M0hPU0F4ZEFZUHhXUG9uQUg4ZnoySDVCZ0xj?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxOR0YxUVhzbnI1Y182U2M2MUxYUTB0Um0tb21nYnBVSlF2VDFfTnpMRDdxaHR0WmFFMWdwYklvb3dHQWw4NHNXV2FFSzdrbEpjekdwWjFFYV9Oc3VQQ1I2T3hqbEVVTlBOdzlpTE9VX0ttQ1VpX2tGNlhpOFg5TUF5am9IS1BlQVRtMW5sQWlzWW56WHEzOVZ6ZGw4dG9iazV0bVFjMjVyU1ZEMlJEZ0VGbTlB?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNTVFiVXNnMmNNTlZ4UzA0QlFEZV94WVluckhCT1hsVjJnTXc5NkhiRnVyR0tTQ3phaWNDci0xZWpjQmpoWjA0X2JTU3dzalcyc1djU3gxY0hDV0ZKM0lBZDhINS1LM3VvMHRLUHpTbVhqTVdQb2I1ZU1nbS1BazlCS1pUSWp0TjUtX1NaZDRYVmZzR0VNUDZUeA?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxORU9WSnJGbDh4cXZJNVNOX2IyV2FGa0hSU0pQblJvY1E4YjVqRWxmdzF2R1JuY3B2dHM2UFBodEppUWVBLTZtNW9NNmNKdXpYNTM0dlBVOVgtam1kU01LZW1CVjFsZkszZjI4U0R6RUt4REczenhHVXFmMDB0anFzZDRpWUdxSXZPTDdRd0kxNUxUYWJoNUd4Q2tOeVNmVl9EbkJqSkt3aWZlbFlOallkLUkyWVpHTWFwRmJnbkg4Yml3RWI0RHhLU2thRDg?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPZlJSVjZEQWNRbmlCdE9hd2c2VzcyY0R6dFBIeTV0TGpVa1paVm9obUdCRXFTZzFTN0k0LTAtbk0xMEdJcFRDQjBDQ1hMN09GTGNGLWVXTzRTWHhEOFZzcHRLZ3NvQzlhUWhrZkdKQkNwTm1ORTBXYjFCTl9Xc1gxWVRoTWNTWjRiWUVEOGVvcWw5RnJFOFFyNFBLM2FVbjRVclE?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNc1VTV3Z4T0ZpZkdWbHI4Q3IxYlMwY3FlMDNrVlZrSFVtYzA4RGJZOHo2Z3AycEVvVnl1QUhmLXQxZDViRjVUM1czRGF5TVFCUkJDWmU4VHJBNEI4Mms2b3FaX1dyRERlcVA3VlhXMDlWZHF6YjFaazlZX1J3cG9CdlhiVkJhWk5RU1F1WXRRb2MxeDhkWFVLLWRUV2ktdzBQSFRuZHpRSGw2c0NMZDRHSg?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOd1NlejQ3S3lTcnUyN2JrUm5YcUJxNldEZjQ4RHZFb0tZa1dPY1JwSU8wZzc1Zi0wRVFuSjNlS2NxTWE2b0hQUXVlcy1fNTdENWZPaDJYTTR2QWVFQnQ2eEpTRzJtbm9SV21SSUE1N0VCeFY5QzRmX1o5Mm0yQ1l5RjR4ZWh1d250R1RCMUhPdFp6TGFHcUhNbUIzMTV3MkRWcW1fUnlGME9GUmFTY2xfVzcyaHBuTUswSGdhX3J1Nk8tMGI2ZHfSAcsBQVVfeXFMT01IRERycWtBX1FPYW5mLXIzZVd5aHpPWjQyR2t0Zko5czBfbjFXVVNvMFdYS2hWTERtSWN0NVJyM2NDTDhIRnRLYWRxTzFWMXhwODlTNUUya1k2NGVtVXVlQU1paXo4Tzd4VTl4SVh0UE5mb0VNSjdiVDlBa3htM2xJbTBxX0FBUll6ZkJ2ZklmZHppTXMxSEZOTUpRMHZrSFRqeTVZa3QyMlFzcm51Y3BIQlBwWGJOeEVCQ1FFM0NSdVJLSmhSQ0ptRFk?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNX19hOEJfa1BFWTFhZTFicjhMNmZ4RzV0M1NlS3ZFMDBlVnp1ZlpaMW5ua1ZWNC1vNENiT2REVWEwYUx0VUJxYzlpX18yUjhla2o2UlNiaXlyU25YMDFZX2xRSlp3M0o4N0pfdUpZdGZrSzJ1eDN0Q3JvNGRKeEJvN2tLUjVCdE5ucnNackVROXhISUdCX01r?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
