# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T05:08:07.706324+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 3, 'ai': 15, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'directional_claim_without_event_type': 2, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 12 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 54.17%; oldest publication 2026-11-10

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 398.7300 |
| Return 1D (%) | -1.6671 |
| Return 1W (%) | 6.2034 |
| Return 1M (%) | -10.4219 |
| Return YTD (%) | 32.2403 |
| Return 1Y (%) | 42.7888 |
| Annualized volatility (%) | 41.7886 |
| Beta vs SPY | 2.1712 |
| Max drawdown (%) | -27.3158 |
| Sharpe (rf=0) | 1.0652 |
| Downside deviation (rf=0, %) | 28.6450 |
| Sortino (rf=0) | 1.5539 |
| Historical VaR 95% (1D, %) | 4.2423 |
| Historical ES 95% (1D, %) | 5.7594 |
| Correlation vs SPY | 0.7083 |
| Tracking error vs SPY (%) | 33.5416 |
| P/E (trailing) | 26.28 |
| P/B | 76.09 |
| EV/EBITDA | 3.69 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 17.05 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 57.96 |
| Return on equity (%) | 41.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 429.9491 |
| Close vs MA50 (%) | -7.2611 |
| MA200 | 401.6695 |
| Close vs MA200 (%) | -0.7318 |
| RSI (14, Wilder) | 45.2805 |
| MACD (12,26) | -10.5464 |
| MACD signal (9) | -11.1900 |
| MACD histogram | 0.6436 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 398.7300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.6671 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 6.2034 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -10.4219 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 32.2403 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 42.7888 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.7886 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 28.6450 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.5539 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2423 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.7594 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7083 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.5416 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1712 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.3158 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0652 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.0505 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 57.9600 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8550 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 26.2841 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 45.2805 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6436 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.2611 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.7318 -> Slightly below the moving-average trend level.

## TAILWINDS

### TSMC record sales strengthen Wedbush’s bullish outlook
- Summary: TSMC record sales strengthen Wedbush’s bullish outlook
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNYkwtT3FIYWdhdHcyWmJPXzBjLTFuV1AxUGd2amk5ZkFxWEYwMlI4QTRVclUyTmVqTFlhYmdBVlMxVkQ2TjMyZnhVQXNSU3ZBWjVkY1RWTXdYcDgtLXNoMjAzMDNUVVNBQnJ2ZzVKSEdTRHFTeWxEOWtQbjI2bXY4OXZOSzNMLXdLZjhQTVBPYkJ6X2p2RGV6dTl4SHdac3ByeXdv?oc=5>

### Bernstein’s Mark Li Raised His Taiwan Semiconductor Manufacturing (TSM) Target to $600. Here’s What Changed
- Summary: Analyst raises TSM target price to $600, indicating bullish outlook.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQOGpUMzJxTHl5SzNTODh3bFBOVlJzSV95TGNNbTRnWG52S0ptQ0wydXdrTkRQLUZFUHFLdlZLMHRfLTFDbDRhcUYtampvbTEwMWExeDdqdlV4RExiWmVPQnM0Y2ZtYS01TUtqcWVtMTh4UWFwYXNXVDRXeXU4Zk5vZm1ndjZtU3Y4c1lZbzh3Y2JrcG52SldITWxOa04?oc=5>

### What Does Taiwan Semiconductor Manufacturing (TSM) AI Revenue Surge Mean For Investors?
- Summary: TSM's AI revenue surge signals strong product demand, boosting investor confidence.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPdHZ6QnVWUlEtOE5fb0dnOGRMbEttQ1FIM0dTdy1CZzloTk1Tc0RaNm40VTB1YjR1bmpnVmRFelE5RjlyeGJQQl9lY2s5SThnZ1d2QmRHbnM0cHVFTnZCcXh6QzRqZVN0TFoyOGVpSExjYm56czYydkdZLV9YX1RYYWdBY1hMRWlTQVhWR2MxQmp1clVoTW93b2J6NVdTZEdjdGZMc041NldwODR4?oc=5>

### Wedbush Has a Strong Message for TSMC Stock Fans
- Summary: Wedbush analyst endorses TSMC, suggesting positive outlook.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxORk9oU1JVdGlRMFByRzFoVC1yU2d2TjlIMUVmdnVIRXY3am53NkdfaF9LNTloYWtSUUQyS0JvakxRU1lXNTBnbTkyR0I2OE9IUHJsbGFNRl8wX0RGdktPQjdvRlliek05TUVpa0JwTjNJSXpZUDdEY21FNDM4MHl6UWpzeTB1OWluSXpwZmpQVFVLRWZ3RmI4N2VLZDBwenc?oc=5>

### TSMC: Investors Are Well Insulated From Potential Shocks
- Summary: Investors feel protected from potential shocks, indicating market confidence.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOSXJCMlMxbkxDTFB2MFJVcHRickJpUU1lWDVQOGZSYWVxbEEtdnU0RWFZalZoRTdoSnpKTlpraGExVS1xazhvUmtSdGtNYVpLTFVzUEc5b1NYSEtQOWo0WUFHSEsxdlFPaHFET2RVT2J5dlRDUGRaYUlKM196aWY5MWVTakpPTmh1MF9FN2JYTmhqOHdQVjZGQVBvSHg?oc=5>

### TSMC’s Terrific Growth Clearly Shows That the Chip Sell-Off Is Overdone. Here Are the Best Stocks to Buy Hand Over Fist
- Summary: TSMC’s strong growth signals a robust market, suggesting upside potential.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNX1U5OW9ickpsa0Ntb1Z3UGZPUnF1MGtCVHlXQTdNT2lZUnpUcHVkM2prY1h0Yzg0ZTk1bGw1WWZRQ0d2bGdvU1RDNjhUbDg3VWNzbUNqUVhFWjNBTUluZ2VRV3p2ZVZ0cWZNaW40MlJNZWxlU3hmV2E0UWhuSTU1RlZmTS1IdHpseEFEYWoxdUR0Q1R5OGxFM28xbHUybTNy?oc=5>

### AI Sell-Off: Buy ANET, TSM & MU to Make Up for NVIDIA Losses
- Summary: Analyst recommends TSM amid AI sell‑off, boosting bullish sentiment.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPMDJUNUd3WVQwUTlFX1FvN1Q4Q2NSdkpYRnFnenl2b3RSRC1RRGY5RzdjWU5wZU1wTFNEdWNSQy1jbHVDcWtoUm13UGNhcU9kTThIMlZQNlpWb2hES1dDajdyNllKOUZZWWxqVVZMWG9KWnRFN0RPeW5ZQUthS2hXOXRMdGFtZFppMkV0QWgtb3JPbU0yZkxsRjlOamhsLWNXNWJRT3F0WEhXWVVXNy1yTzZB?oc=5>

### TSMC Secures Its Future by Investing in Anthropic and OpenAI
- Summary: TSMC invests up to $1bn in Anthropic and OpenAI, strengthening AI capabilities and future growth.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPV1JfVXFkZmxXMEJSenR3Y29CNTZLV1FIR1BSLXZ3VFlkRmZrUWVFOGpROGFSOVZHV2xyeEtneV9aZHZBYnlwQTRBZEhKSXBJRmVudXRDTDZjNFJDaG1BT0tQRnZYaFFjMV9BUUM2ZWVOTFlsM2hOZUtneUc0dXNzUm4yeEdUY0VqU3FiU0lsLTRZZW9nbWhqZWFyM3VmQ1Q0djA3aUF3?oc=5>

## HEADWINDS

### TSMC Stocks Fall 2.21% as NVIDIA Shake-Up Overshadows Record October Revenue
- Summary: TSMC Stocks Fall 2.21% as NVIDIA Shake-Up Overshadows Record October Revenue
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxORmxpdjhiUlZfRExUZXlUOHRuWmp0cWRuV3htQTdpcTk1VjJKT0ZYYzQ4MzBPeXNraUloRGI0b2JLdC1STHZsZno2eUtRbHRPejhEUzNWak94cWVpQ1g3QnpzRzh6c1I5SGkwWldjUVVUcmdZUDJxZ2U5d1Rkcm90VFRwTHhKTXgxTko2WlZqVQ?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) Stock Could Be 7% Undervalued Despite Fab Expansion Plans
- Summary: Analysts suggest TSMC may be undervalued, indicating potential downside risk.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNclhidVc5Z2VTNE9uZzRCcldGRDUzLXcyc1otalhRaExZNHR2cVRPNk03Z052ekExdUt1QzgxWGkya1NHcElYeWowOXRESHM1UFlsZUx3Yi14bUFHcHp3bVJuTlJPUDlzZFZjYV9URFR6b19NQVRtYUhMdFNobGIwWWFJb1JwODdWM1h6ZjQ4RS1obDRfNUkxdHdGUDdFR0JqbkhnX2ZzVUtRTml2Nmc?oc=5>

### TSMC Stock (TSM) Dips After Hackers Ransom Employee Data for Bitcoin
- Summary: Security breach caused a dip in TSM shares, raising risk concerns.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQQ3g2UGxvNjBDQXE0bUNmSHhHZUhicnBZU0VSSkJhcjUtajVIck9KYTZsVm42UUFjbVVWcHBTZjVVYk00VE56WWxWRWJ0cmNJUHhuMG5kV1RLSHdBcjk0bERKSlVIQ1Uyckk2djVoRDRfaEpzc3AzQ0UxZFNncFRud2wwVXdaMzgxMXRzZWxkUGlRN3ZIUnRwajcxQ0Q?oc=5>

### ETFs Are Net Sellers of Taiwan Semiconductor (TSM) on Nov. 10
- Summary: ETFs sold TSM shares on Nov. 10, indicating short-term selling pressure.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQU3NOeERERGc3Y2tqYmU3LU1ESnQ2VEVhMHBVOE5XM1djamp5S0VDb0tpVFBRVTVhYk1ReFhLNjAwRlg5QktmWnVnUGFqRnVkOFB5TXNrSXI0ejdUVHJacy1mU3QxNmhnTURRajdNNm84bGVoek9NdnZNekRaS0VEZ2NoTldjbGlOT2tUeVFmWDlkVDBJUTlkWlIwUXkwRXNSZEszMg?oc=5>

## CATALYSTS

### TSM Stock Jumps Premarket After Board Approves $1B Investment In Anthropic And OpenAI, Dividend Raise
- Summary: TSM Stock Jumps Premarket After Board Approves $1B Investment In Anthropic And OpenAI, Dividend Raise
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNcUZzUVF1NFQ5NFVFYVRGSUNtVkhnc0plRGxFazRvVWFheFJOVEdnTnlfNDktZWJmc0Zvb044TGVkVVJiYS1vbmd1SmdLX25qTE9fV3pPckVzdlZqbW9hS19jRDVueWZRRTNMcFRQTGZzTlhnTUtseks2ZUFadmtha09yZG5yckJMbW5XUW9ZS0s0MnBMdFZPZFlqd1I?oc=5>

### TSMC Approves Up to $1 Billion Investment Plan in Anthropic, OpenAI
- Summary: TSMC invests up to $1B in Anthropic and OpenAI, expanding AI partnership.
- Date: 2026-11-11 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNT3ZlYXlWNllKZkZETDl2YUpGcXdKYnBpc01rZ2pMenZYcXJrcmVhbFdlUW5oQnFWeTZ1dlN2S2RwVFFUaVJIUWk0UVJsOHk4R25nSGt4NnlfYTZVNXZvTzlrcXU4V2ZGNUNQQTY1amMwcHZ3bC00aTFBMTRKcFExdThaQlY2Nmp4ek1qSXRDdVVuLUlOSWVPQWMtSHlqT0g3RmlCbQ?oc=5>

### As October Revenue Surges, Wall Street Is Still Bullish on Taiwan Semi Stock
- Summary: Wall Street remains optimistic as TSM's October revenue jumps, signaling strong performance.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOU2RWVW9CTzdRNW1nYlJPWTRHd0N4WlpQRFphaVVUYWZtZDJlS2JybGF3UVptd0p3UFhQZjFCeFE3R2hfZ3VyYzZvZGp3S25IUlFXcVZ4UTBjN1VkUTQ2eHp6MnZDcUZjekN2Wm4xY2tackRRbkFXS3JPc3R3NlZwelhRT0lWQlNvWmt1eERfNGwwS0ZwSHJIc0tFblp2TUphLS1mQ1hJOS1SejdaWHYwWXM5bEI1YkJzeHRz?oc=5>

### Here’s Why Bernstein’s Mark Li Is Raising His Price Target on TSMC (TSM) to $600
- Summary: Analyst Mark Li lifts TSM price target to $600, reflecting bullish outlook.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQTTlUdnBEMndLSFFyVEV0bVNDVWlRRW0zZXdNSTJxeEY5VjVOOHluSVA2TEJldkJWTl91a1Z0bWJ4QTBhLVdpSWlVeUZTcF91Q0txMGZyaXpyUEN2TTNsRUdLT2ZGSzJha3kzeU91T2RGVElDTmd0clBWMFRmUkx2MkY2SkdSSFhZRGQteWhJalVMcWlVS2Z1R3hR?oc=5>

### Something happened in October that changes the TSMC stock debate
- Summary: An October event altered the TSMC stock debate, potentially impacting investor sentiment.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxQUWZrV3ludGRQVklLOFN1cmN1eU9MVjhaS0xIWVNmOG83U2ZxckNJb2FqMUN4c29rUng3a1ZJNWpiUTNvZGcwOG1CcTA5Y3phZTRUZzVZSENRaTJfeFFpajZRS1psVDVzbTdETTNtSldZMm5DM2tBaE9FTG9VNnkySQ?oc=5>

### TSMC plans up to $1bn investment in Anthropic, OpenAI
- Summary: TSMC will invest up to $1bn in AI firms Anthropic and OpenAI, signaling a strategic push into artificial intelligence technologies.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOZklnSkwxMVFPYnVQNUpzdVAtaXg0LXU0R1dBeTBDUGhScllSemQ4bWlBOW1mdmNHdzRuQV83RFdZWENqNXlDWFBqbkxtYU1jNWVuSHRoMVB3Qmtyd2hGMFl1Rk9PTXZkc2xQMUZhRjh2T3hiNEdoMlBmUFhndmFLWTFEQlpqaFFfRlFwT2NuT1paR2EwdHNBOGN3YlBYamRX?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **26.28** | **76.09** | **3.69** | **50.90** | **2,068,002,373,632.00 USD** | **42.79** |
| UMC | 14.81 | 2.66 | -0.28 | 25.60 | 38,620,024,832.00 USD | 120.41 |
| GFS | 121.97 | 1.94 | 11.13 | 12.50 | 23,117,402,112.00 USD | 27.24 |
| INTC | N/A | 2.76 | 17.24 | 20.90 | 317,092,888,576.00 USD | 66.14 |

Peers fetched as_of: 2026-11-13; TSM reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiowFBVV95cUxNYkwtT3FIYWdhdHcyWmJPXzBjLTFuV1AxUGd2amk5ZkFxWEYwMlI4QTRVclUyTmVqTFlhYmdBVlMxVkQ2TjMyZnhVQXNSU3ZBWjVkY1RWTXdYcDgtLXNoMjAzMDNUVVNBQnJ2ZzVKSEdTRHFTeWxEOWtQbjI2bXY4OXZOSzNMLXdLZjhQTVBPYkJ6X2p2RGV6dTl4SHdac3ByeXdv?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQOGpUMzJxTHl5SzNTODh3bFBOVlJzSV95TGNNbTRnWG52S0ptQ0wydXdrTkRQLUZFUHFLdlZLMHRfLTFDbDRhcUYtampvbTEwMWExeDdqdlV4RExiWmVPQnM0Y2ZtYS01TUtqcWVtMTh4UWFwYXNXVDRXeXU4Zk5vZm1ndjZtU3Y4c1lZbzh3Y2JrcG52SldITWxOa04?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPdHZ6QnVWUlEtOE5fb0dnOGRMbEttQ1FIM0dTdy1CZzloTk1Tc0RaNm40VTB1YjR1bmpnVmRFelE5RjlyeGJQQl9lY2s5SThnZ1d2QmRHbnM0cHVFTnZCcXh6QzRqZVN0TFoyOGVpSExjYm56czYydkdZLV9YX1RYYWdBY1hMRWlTQVhWR2MxQmp1clVoTW93b2J6NVdTZEdjdGZMc041NldwODR4?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxORk9oU1JVdGlRMFByRzFoVC1yU2d2TjlIMUVmdnVIRXY3am53NkdfaF9LNTloYWtSUUQyS0JvakxRU1lXNTBnbTkyR0I2OE9IUHJsbGFNRl8wX0RGdktPQjdvRlliek05TUVpa0JwTjNJSXpZUDdEY21FNDM4MHl6UWpzeTB1OWluSXpwZmpQVFVLRWZ3RmI4N2VLZDBwenc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOSXJCMlMxbkxDTFB2MFJVcHRickJpUU1lWDVQOGZSYWVxbEEtdnU0RWFZalZoRTdoSnpKTlpraGExVS1xazhvUmtSdGtNYVpLTFVzUEc5b1NYSEtQOWo0WUFHSEsxdlFPaHFET2RVT2J5dlRDUGRaYUlKM196aWY5MWVTakpPTmh1MF9FN2JYTmhqOHdQVjZGQVBvSHg?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNX1U5OW9ickpsa0Ntb1Z3UGZPUnF1MGtCVHlXQTdNT2lZUnpUcHVkM2prY1h0Yzg0ZTk1bGw1WWZRQ0d2bGdvU1RDNjhUbDg3VWNzbUNqUVhFWjNBTUluZ2VRV3p2ZVZ0cWZNaW40MlJNZWxlU3hmV2E0UWhuSTU1RlZmTS1IdHpseEFEYWoxdUR0Q1R5OGxFM28xbHUybTNy?oc=5
- https://news.google.com/rss/articles/CBMi8wFBVV95cUxONTZ5MzJING1za2tPVFRORnpBd0lTbHlGN1pmaFJhMmw2R1lKeWZXNXFtRFNfVkItVTE5MjZIaG4wa01lTmF4TmNsR3ducHhCMTA2bGhKUmVDOVRJUmE4QUU1OE0xRkliR3pFOENxT2haZ1RlX3VMTm5Sdkl4Rk5XQ2dicjBTa3dQMFlva2JWLTdYMzdscWxOOTJsV013RXY1VDlkQ3lwc2pEVlZTeUZ3UHFZZVJqT2RpY3lWSWFyNUNqTmtjRUwxQW9TSlhIdUFaVE1RLXd1UThKV3ZCNjRYcjhaWVFLY2F5YjNtcXhiNDg4bW8?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPMDJUNUd3WVQwUTlFX1FvN1Q4Q2NSdkpYRnFnenl2b3RSRC1RRGY5RzdjWU5wZU1wTFNEdWNSQy1jbHVDcWtoUm13UGNhcU9kTThIMlZQNlpWb2hES1dDajdyNllKOUZZWWxqVVZMWG9KWnRFN0RPeW5ZQUthS2hXOXRMdGFtZFppMkV0QWgtb3JPbU0yZkxsRjlOamhsLWNXNWJRT3F0WEhXWVVXNy1yTzZB?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPV1JfVXFkZmxXMEJSenR3Y29CNTZLV1FIR1BSLXZ3VFlkRmZrUWVFOGpROGFSOVZHV2xyeEtneV9aZHZBYnlwQTRBZEhKSXBJRmVudXRDTDZjNFJDaG1BT0tQRnZYaFFjMV9BUUM2ZWVOTFlsM2hOZUtneUc0dXNzUm4yeEdUY0VqU3FiU0lsLTRZZW9nbWhqZWFyM3VmQ1Q0djA3aUF3?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxORmxpdjhiUlZfRExUZXlUOHRuWmp0cWRuV3htQTdpcTk1VjJKT0ZYYzQ4MzBPeXNraUloRGI0b2JLdC1STHZsZno2eUtRbHRPejhEUzNWak94cWVpQ1g3QnpzRzh6c1I5SGkwWldjUVVUcmdZUDJxZ2U5d1Rkcm90VFRwTHhKTXgxTko2WlZqVQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNclhidVc5Z2VTNE9uZzRCcldGRDUzLXcyc1otalhRaExZNHR2cVRPNk03Z052ekExdUt1QzgxWGkya1NHcElYeWowOXRESHM1UFlsZUx3Yi14bUFHcHp3bVJuTlJPUDlzZFZjYV9URFR6b19NQVRtYUhMdFNobGIwWWFJb1JwODdWM1h6ZjQ4RS1obDRfNUkxdHdGUDdFR0JqbkhnX2ZzVUtRTml2Nmc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQQ3g2UGxvNjBDQXE0bUNmSHhHZUhicnBZU0VSSkJhcjUtajVIck9KYTZsVm42UUFjbVVWcHBTZjVVYk00VE56WWxWRWJ0cmNJUHhuMG5kV1RLSHdBcjk0bERKSlVIQ1Uyckk2djVoRDRfaEpzc3AzQ0UxZFNncFRud2wwVXdaMzgxMXRzZWxkUGlRN3ZIUnRwajcxQ0Q?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQU3NOeERERGc3Y2tqYmU3LU1ESnQ2VEVhMHBVOE5XM1djamp5S0VDb0tpVFBRVTVhYk1ReFhLNjAwRlg5QktmWnVnUGFqRnVkOFB5TXNrSXI0ejdUVHJacy1mU3QxNmhnTURRajdNNm84bGVoek9NdnZNekRaS0VEZ2NoTldjbGlOT2tUeVFmWDlkVDBJUTlkWlIwUXkwRXNSZEszMg?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNcUZzUVF1NFQ5NFVFYVRGSUNtVkhnc0plRGxFazRvVWFheFJOVEdnTnlfNDktZWJmc0Zvb044TGVkVVJiYS1vbmd1SmdLX25qTE9fV3pPckVzdlZqbW9hS19jRDVueWZRRTNMcFRQTGZzTlhnTUtseks2ZUFadmtha09yZG5yckJMbW5XUW9ZS0s0MnBMdFZPZFlqd1I?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNT3ZlYXlWNllKZkZETDl2YUpGcXdKYnBpc01rZ2pMenZYcXJrcmVhbFdlUW5oQnFWeTZ1dlN2S2RwVFFUaVJIUWk0UVJsOHk4R25nSGt4NnlfYTZVNXZvTzlrcXU4V2ZGNUNQQTY1amMwcHZ3bC00aTFBMTRKcFExdThaQlY2Nmp4ek1qSXRDdVVuLUlOSWVPQWMtSHlqT0g3RmlCbQ?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOU2RWVW9CTzdRNW1nYlJPWTRHd0N4WlpQRFphaVVUYWZtZDJlS2JybGF3UVptd0p3UFhQZjFCeFE3R2hfZ3VyYzZvZGp3S25IUlFXcVZ4UTBjN1VkUTQ2eHp6MnZDcUZjekN2Wm4xY2tackRRbkFXS3JPc3R3NlZwelhRT0lWQlNvWmt1eERfNGwwS0ZwSHJIc0tFblp2TUphLS1mQ1hJOS1SejdaWHYwWXM5bEI1YkJzeHRz?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQTTlUdnBEMndLSFFyVEV0bVNDVWlRRW0zZXdNSTJxeEY5VjVOOHluSVA2TEJldkJWTl91a1Z0bWJ4QTBhLVdpSWlVeUZTcF91Q0txMGZyaXpyUEN2TTNsRUdLT2ZGSzJha3kzeU91T2RGVElDTmd0clBWMFRmUkx2MkY2SkdSSFhZRGQteWhJalVMcWlVS2Z1R3hR?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxQUWZrV3ludGRQVklLOFN1cmN1eU9MVjhaS0xIWVNmOG83U2ZxckNJb2FqMUN4c29rUng3a1ZJNWpiUTNvZGcwOG1CcTA5Y3phZTRUZzVZSENRaTJfeFFpajZRS1psVDVzbTdETTNtSldZMm5DM2tBaE9FTG9VNnkySQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOZklnSkwxMVFPYnVQNUpzdVAtaXg0LXU0R1dBeTBDUGhScllSemQ4bWlBOW1mdmNHdzRuQV83RFdZWENqNXlDWFBqbkxtYU1jNWVuSHRoMVB3Qmtyd2hGMFl1Rk9PTXZkc2xQMUZhRjh2T3hiNEdoMlBmUFhndmFLWTFEQlpqaFFfRlFwT2NuT1paR2EwdHNBOGN3YlBYamRX?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
