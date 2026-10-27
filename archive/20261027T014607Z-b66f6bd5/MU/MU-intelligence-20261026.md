# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T01:46:14.010372+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 0, 'ai': 17, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 7 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 34.78%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 903.7000 |
| Return 1D (%) | 2.9799 |
| Return 1W (%) | -0.1326 |
| Return 1M (%) | -16.4872 |
| Return YTD (%) | 216.8638 |
| Return 1Y (%) | 313.0793 |
| Annualized volatility (%) | 81.4372 |
| Beta vs SPY | 3.3814 |
| Max drawdown (%) | -39.0954 |
| Sharpe (rf=0) | 2.1542 |
| Downside deviation (rf=0, %) | 48.9986 |
| Sortino (rf=0) | 3.5803 |
| Historical VaR 95% (1D, %) | 7.0066 |
| Historical ES 95% (1D, %) | 9.5345 |
| Correlation vs SPY | 0.5280 |
| Tracking error vs SPY (%) | 75.4996 |
| P/E (trailing) | 12.16 |
| P/B | 7.39 |
| EV/EBITDA | 9.04 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 4.37 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 80.68 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 2.85 |
| MA50 | 981.2390 |
| Close vs MA50 (%) | -7.9022 |
| MA200 | 734.7771 |
| Close vs MA200 (%) | 22.9897 |
| RSI (14, Wilder) | 42.3259 |
| MACD (12,26) | -34.6222 |
| MACD signal (9) | -21.5798 |
| MACD histogram | -13.0424 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 903.7000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.9799 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.1326 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.4872 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 216.8638 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 313.0793 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 81.4372 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 48.9986 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 3.5803 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.0066 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.5345 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5280 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 75.4996 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3814 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -39.0954 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 2.1542 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 4.3679 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 80.6780 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.8500 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 12.1579 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.3259 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -13.0424 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.9022 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 22.9897 -> Clearly above the moving-average trend level.

## TAILWINDS

### Here’s What a $10,000 Investment in Micron Stock Will Be Worth by 2030
- Summary: Projected value of a $10,000 investment in Micron stock by 2030.
- Date: 2026-10-26 | Impact: medium | Horizon: long | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOZjhMZUs2NUJXT3NBUnoxUE9abjQzUW00U2xoUlFhcW1ZbTFIbDNOQ01NWmFZVXp5YlBDSjNRQmZ4VUlmV0NzUzlackxJXzhxa3FsdXNQa0NjVFNmcEc4bGNZNUhvRWZxeHVkSFRtNFpTWk8ySzZPYkZCdVI1VEdUbDBscUxGbDFFUjFDX25URDhRZHpTZkhRSG5HTQ?oc=5>

### Micron (MU) is an Incredible Growth Stock: 3 Reasons Why
- Summary: Analyst highlights Micron’s growth potential, citing strong demand and product pipeline.
- Date: 2026-10-23 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOWVhXbU1jei01bzFkekM5SFZqOXNhVTJnczFONExnSmdyNExGUmFsejRFZ3FZNC1Nb0pkWkRxQkdJcjMySzIyMmoxaUxqek9PZm00VkladHhwOWFMN29ZaGR0Z2xhTWJuVnoyTk16V3BWb1NPMnpaR3lBNFZCeWVQdUwxTU05M0NHWDByTmNRSnFkUmN3SEI2bWpRS2padDg?oc=5>

## HEADWINDS

### Stock-Split Watch: Is Micron Next?
- Summary: Micron may consider a stock split.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxNOHYtZHJvQ0tOM0VDOTlZeWdQTmYwY2JSSGpZS1ROYWRHMi1xQWdxN1d5Tk96dDR3ZFQ2ZnhKTDlUOExWRV9JUW83ZkQwb2RtMHE2U1FXNk9kbjRUeXlaaDZ3R3dZMk1FNDgwUjVMUk02bU9hUzFyQ3NrUFo4cE9sUA?oc=5>

### Micron Suffers a 99.8% Snub From Its Union, Exposing AI's Human Fault Line
- Summary: Union backlash over AI initiatives may hinder workforce morale and productivity.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOUVpPbmtWRHFDdjBROFF3X00tMG9VcE1TdnRpbWlGcU9zcDRRcUZ5TE5ncGRpNGM2RUpGTUl2c3cydFZZOFRSUlIwZloydnZaRnJOSi1uSHlPQzJfaFhEQURjUXBMMEpkODBkdlVJaHFBSUZ5NVNNZy16X1pzRXpYM21BWXNQZTFCQmZnaVN5TzBrWGFfMDRwMUF3?oc=5>

## CATALYSTS

### Micron Just Delivered a Monster Quarter, but the Stock Is Plummeting. The Reason Is Obvious.
- Summary: Micron reported strong earnings but stock fell.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOdXZaeWxicXpOQ2F0TmtiUWlPVm5IMXpRX2hGM000T3RoVHNySHZmb2tBUl9tV3AyZkJjMlhFOGR3eEczTVZkTlVsaGRueWxJSEJfLVRPNjM2eC1WdDlBSHBSMnNtZXF1ZUY4bEtKTXJhV2RyLUpwRmtBUjRXMXNoMGFBNUswX3VEUkxVd3ZHMGNVelJGeVpoYw?oc=5>

### After Two Spectacular Micron Buy Ratings, I’m Calling It Quits (Downgrade To Sell) (MU)
- Summary: Two analysts downgraded Micron to sell after strong buy ratings, signaling a shift in outlook.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxOSnRNMG1HUzBaZFhtVjE1LU5pMVZ2RExucVN1OWlCX2tmU3I5YW00TDBtSG9jR0E4bG40QzNzV1liM2w0R1JjR3kxZC1fLUNhUmNRSzhYeGlkTTYyU09tVGJnUDd6MVp2TW12Sk40ZHdXUWxNSXJoblZQQkN3UEJHWDVyaFpOV2dnR09JWGxDWGRLdkl3ejV5LWlZWFVmLTVEdkM1RjJqMC1SSzBkUlljUVluTE43eUNpU0l0Xw?oc=5>

### Can Micron Stock Fall 30%?
- Summary: An analyst questions whether Micron’s stock could decline by 30%, indicating potential downside risk.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOQWZtd191SG9peFJsc2duYWMwS004Q3hYa0VpT0F6a21lRVZhcTNOaDZqRWpwdWJScUJRajlZVmZfbnh4QVN5UC1tRjBLUHhrWUFiaExvZVkyaGpEcEZPSzdVdzJEYXdBOF9wZjY2S0t4TDd6ZWU1VDF6QzhqMG9EbTIyeUo3blE1X25N?oc=5>

### If You Invest $1,000 in Micron Today, Here’s What It Could Be Worth by 2030
- Summary: Projected future value of a $1,000 investment in Micron by 2030, based on current performance.
- Date: 2026-10-26 | Impact: low | Horizon: long | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPQmQyNldxZjlIVW9tVzdRaG5hbW43dUtNVjRaY0YyT09aU1NWT3RucDJQTzM1UzFnZzdoR19nRERPdEU1Q3FFSFRBSnlzMklXUFh1YjlZX3NBc2g3X3Y2S0EwUmhkUVhOaEdRRFlROGRUVjBRbDFoLXZ1YjJCNl9GUVRSZWZOaDRDbDVQWUUtSmg4NHM0V0Q2aDA4amNWazhlM2dLQ1NYY1JIT2xGWUFjWGxmT2Z1dw?oc=5>

### $100 Invested In Micron Technology 10 Years Ago Would Be Worth This Much Today
- Summary: Illustrates the growth of a $100 investment in Micron over the past decade.
- Date: 2026-10-26 | Impact: low | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOYWRXUUlUVU9Pd0R0em1tMWpsQUQ1djB2TWxhOWhTWlp2U19yUlRhb040SlJESlBtY1lPc20wTHdXQjc3TDZKSy1XMnhoMW1FZHZEMDJwQmd5cFhzandacVBrd1lWOEZqUVl6NHR2eFN6OE1UbU1XWmhwdi1KUGJiaERLSGs0eDdIVnhFQ0NXYWJBNm9Ia29TdlhyYW1LM1hmRDZNZWs3Q19qbngyT3hKRjJuNGE?oc=5>

### Micron: I Was Bearish Before, But This Call May Be Even More Controversial (Upgrade) (MU)
- Summary: An analyst upgrades Micron after previously being bearish, suggesting a potential turnaround.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQeFpfX0t3eUhHMzBHdEtWY0tFdzY1NGxZUFJVZkhiOGNTeGhESGdkLWJrWUVrLUVLbG5POHdPcnlITzMxdFQzem5zUVJUOS0zY0FIdjg2WkdFUXFSWTVFcnowWGlrZjE0ekpzdmN6VVFjdHpSZXA4R1hScmVZMGFMR2VYUEpsWkdWLTFMVnZVMDNWSWN3c1hkc0s1b3RNSThfOTVxamt4ZE5sMVdMTFFzeVctWkxHZWUwM1hjcFV3?oc=5>

### Micron Just Revealed a New Business Strategy. That Change Makes It a Screaming Buy.
- Summary: Micron unveiled a new strategy, signaling growth potential.
- Date: 2026-10-25 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxONzJEanVQYlFGY2pNd3VnRC1zZllfbG1LLVRsVWwtbGtMNVNsVWZ4Y3k5M09OZTBNdWdTUEVScUVMeXY5N0I2UElNVFdkNUh6R2IxUnlWMkFJQXA4Nm5rZ3VUNGlIOXVqSnEteHRQekhOS2I4YUs5RmtlQ1RxUi1tTmpSUFJjQXlpa1pnc2steERfdGRMaGFtby11cWdzTXZEcTV5alhR?oc=5>

### Micron: The New SCA Contracts Are Not As Great As You Think (NASDAQ:MU)
- Summary: New SCA contracts may underperform expectations.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPNkxBTXZQVDNJRkNvdmVZbVdTY2RUZUZSY3dFUjl6STBCbzF1T3ZrWUY2SXZ1ZzFHWkk0LWpfQjBQLUltTzE5dUd0UXBsaGFSY0ctZE5DTzJQX0dkTE5pUVhEeDRTT3hNQkdyOUFKR1RvYlpEU2xoN1A4Z1N6ZEYtWk5sRC10Zlh2NlhDVkxobUNTaG9lamc?oc=5>

### Why Micron Stock Dropped on Thursday
- Summary: Stock fell due to recent market factors.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPNUJTTHZMRXZtaXhGU3pzdjhvek43SkFTb3VGVjhfMVhpV3ZXdDdkZTZ0LUFnUWRXQXRlYTNEb1RNSlc2R2ozNmw5ZkZoWGt4bkNwSldmTlg5R0NHVl9faWlPTkFCYklrTDh4WHpPQnRJOHlCQkNXczN1R2Z2ejNLRmstTWVZbWlTbU10RHlwelcwZW9RNUxmUDZ3cFJCNEE?oc=5>

### “Durability and Predictability”: Micron Is Up 200% in 2026. Take Profits, or Buy More?
- Summary: Micron's stock surged, prompting buy/hold debate.
- Date: 2026-10-26 | Impact: high | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNeVJqX0Z5T2dHeTN6M0pFN2pJU01oTmpnN0h1T1RFVmNBb3IxMzBNZzBieDV1RlExRUY2Q2FkRkZJYV9QMGc4N2pYR3NTdjBCQ0Z6OU5SXzRSeHVldmNfR1kwS1Nob2VOUklvV2hwZWw1blJibkMwTXhMNkFjQlRta1FNT1A1VllGdmZZWWpQSjNoMlFXcUl0MUcxR3J1SGhnUTRuYkU2cmJEZw?oc=5>

### Micron’s Taiwan Unit Reached a Deal With the Taichung Union. Here’s What to Know.
- Summary: Partnership with Taichung Union could expand local manufacturing capacity.
- Date: 2026-10-24 | Impact: medium | Horizon: medium | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNNVd3V3FmWXh1R28xWTN4T21iT1JUWGRCaG1UT1lzZHYtM3FBejhyd0ZPMmVZQzVZQ2x1eUJNR0h2Q2RiMk1qQ3ZlbFM4VGxlNDltWkp5a1I5YmYtMlpST0I3Ums3RndmemowSndyd2pBaVZBX3NIZURZdmRFamU2TW9EWHFxUUlZSFNaWk93TTlJMmc0QXhQVU5ZSnM?oc=5>

### Sell Micron: Don't Wait For Memory Boom To End (NASDAQ:MU)
- Summary: Analysts advise selling Micron shares, citing potential memory market slowdown.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPeFAtWHBZMGdZT1dtTnRWUWIyenV2djVSN3JjOVJuV1pIQjNId1NPS3h1X2FQeDB3cUxEamNaVUl6TUNDLWdwNURyMVZpRjVhXzYxU0duVE9uX0Q5Si15dGdQS1ZwaExSM2RhQUpsdEROVFhuc3RTVHlqR3VPUnFTMWlnNzVObTRhcUtKRm1R?oc=5>

## RISKS

### What Could Micron Technology (MU) Strike Risk And Supply Moves Mean For Investors?
- Summary: Potential risks and supply chain moves affecting Micron.
- Date: 2026-10-23 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQc1NSLUxySzlsNnBqd2dQNjhQeHliel8wRHFXNmR2WFpIbFhRbnVobnFaQXBtOXAwTGh1R2hLajFKcHVJcXU2cEx5d19UWXhFNDQ1aVlHYWxBT25DSGVrSzQ1UTN5R2pIVXFOZlBsSnJzSHZqTnhqUXVDUUZucWpoUnJSWXBvWjhOcXBxcEVQbWRuX2JGMHZyV2ZUS216dGM?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **12.16** | **7.39** | **9.04** | **379.30** | **1,022,467,178,496.00 USD** | **313.08** |
| WDC | 12.53 | 14.25 | 21.06 | 55.50 | 133,307,744,256.00 USD | 175.67 |
| STX | 46.35 | 67.42 | 32.92 | 48.50 | 146,488,852,480.00 USD | 176.78 |
| NXPI | 20.99 | 5.44 | 13.83 | 19.50 | 61,989,519,360.00 USD | 14.15 |

Peers fetched as_of: 2026-10-26; MU reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMimwFBVV95cUxOZjhMZUs2NUJXT3NBUnoxUE9abjQzUW00U2xoUlFhcW1ZbTFIbDNOQ01NWmFZVXp5YlBDSjNRQmZ4VUlmV0NzUzlackxJXzhxa3FsdXNQa0NjVFNmcEc4bGNZNUhvRWZxeHVkSFRtNFpTWk8ySzZPYkZCdVI1VEdUbDBscUxGbDFFUjFDX25URDhRZHpTZkhRSG5HTQ?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQSkN2MjJhU0NQUkpOaTRMQ3cxTXgwRExnRmtIWHN1MTlHNWJGczFPOWNKZXpEUm40MC1UTENYTVl2YmRBR0EwVFlTSHpDaVNWTm82RlpYalNFSWZHNFhRcndkcERTcld4WDZHdE5Ic1JsTWstY1VuS0RXZzdLWjhlX3VLRmxEYVhsYjdhVnJ2ckFRSFF2d2ZaS1ZQVWJSWTh3VGM5MUhnMFZDcm5oMDZsb3UwLW5Kdw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOWVhXbU1jei01bzFkekM5SFZqOXNhVTJnczFONExnSmdyNExGUmFsejRFZ3FZNC1Nb0pkWkRxQkdJcjMySzIyMmoxaUxqek9PZm00VkladHhwOWFMN29ZaGR0Z2xhTWJuVnoyTk16V3BWb1NPMnpaR3lBNFZCeWVQdUwxTU05M0NHWDByTmNRSnFkUmN3SEI2bWpRS2padDg?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxNOHYtZHJvQ0tOM0VDOTlZeWdQTmYwY2JSSGpZS1ROYWRHMi1xQWdxN1d5Tk96dDR3ZFQ2ZnhKTDlUOExWRV9JUW83ZkQwb2RtMHE2U1FXNk9kbjRUeXlaaDZ3R3dZMk1FNDgwUjVMUk02bU9hUzFyQ3NrUFo4cE9sUA?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQTVo0czRwU1JlaEpkQnBEM2lZSUFmdGthc0hRS2ZLbWdfREpJY0I3RjI4Z3FENGVEZmY4TmVsc29xTk9lQnM4dkRhamlpSTVDc2s3VXNuanN3WVFIb0Rmc2daRkdMRG9hZDBzRTZ1cmdNYlRFVklRVVJqand4SXdSUnhmUWdFQV94dHVXazB3eUxmb3ZWbGNudnhn?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOUVpPbmtWRHFDdjBROFF3X00tMG9VcE1TdnRpbWlGcU9zcDRRcUZ5TE5ncGRpNGM2RUpGTUl2c3cydFZZOFRSUlIwZloydnZaRnJOSi1uSHlPQzJfaFhEQURjUXBMMEpkODBkdlVJaHFBSUZ5NVNNZy16X1pzRXpYM21BWXNQZTFCQmZnaVN5TzBrWGFfMDRwMUF3?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOdXZaeWxicXpOQ2F0TmtiUWlPVm5IMXpRX2hGM000T3RoVHNySHZmb2tBUl9tV3AyZkJjMlhFOGR3eEczTVZkTlVsaGRueWxJSEJfLVRPNjM2eC1WdDlBSHBSMnNtZXF1ZUY4bEtKTXJhV2RyLUpwRmtBUjRXMXNoMGFBNUswX3VEUkxVd3ZHMGNVelJGeVpoYw?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxOSnRNMG1HUzBaZFhtVjE1LU5pMVZ2RExucVN1OWlCX2tmU3I5YW00TDBtSG9jR0E4bG40QzNzV1liM2w0R1JjR3kxZC1fLUNhUmNRSzhYeGlkTTYyU09tVGJnUDd6MVp2TW12Sk40ZHdXUWxNSXJoblZQQkN3UEJHWDVyaFpOV2dnR09JWGxDWGRLdkl3ejV5LWlZWFVmLTVEdkM1RjJqMC1SSzBkUlljUVluTE43eUNpU0l0Xw?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOQWZtd191SG9peFJsc2duYWMwS004Q3hYa0VpT0F6a21lRVZhcTNOaDZqRWpwdWJScUJRajlZVmZfbnh4QVN5UC1tRjBLUHhrWUFiaExvZVkyaGpEcEZPSzdVdzJEYXdBOF9wZjY2S0t4TDd6ZWU1VDF6QzhqMG9EbTIyeUo3blE1X25N?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPQmQyNldxZjlIVW9tVzdRaG5hbW43dUtNVjRaY0YyT09aU1NWT3RucDJQTzM1UzFnZzdoR19nRERPdEU1Q3FFSFRBSnlzMklXUFh1YjlZX3NBc2g3X3Y2S0EwUmhkUVhOaEdRRFlROGRUVjBRbDFoLXZ1YjJCNl9GUVRSZWZOaDRDbDVQWUUtSmg4NHM0V0Q2aDA4amNWazhlM2dLQ1NYY1JIT2xGWUFjWGxmT2Z1dw?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOYWRXUUlUVU9Pd0R0em1tMWpsQUQ1djB2TWxhOWhTWlp2U19yUlRhb040SlJESlBtY1lPc20wTHdXQjc3TDZKSy1XMnhoMW1FZHZEMDJwQmd5cFhzandacVBrd1lWOEZqUVl6NHR2eFN6OE1UbU1XWmhwdi1KUGJiaERLSGs0eDdIVnhFQ0NXYWJBNm9Ia29TdlhyYW1LM1hmRDZNZWs3Q19qbngyT3hKRjJuNGE?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQeFpfX0t3eUhHMzBHdEtWY0tFdzY1NGxZUFJVZkhiOGNTeGhESGdkLWJrWUVrLUVLbG5POHdPcnlITzMxdFQzem5zUVJUOS0zY0FIdjg2WkdFUXFSWTVFcnowWGlrZjE0ekpzdmN6VVFjdHpSZXA4R1hScmVZMGFMR2VYUEpsWkdWLTFMVnZVMDNWSWN3c1hkc0s1b3RNSThfOTVxamt4ZE5sMVdMTFFzeVctWkxHZWUwM1hjcFV3?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxONzJEanVQYlFGY2pNd3VnRC1zZllfbG1LLVRsVWwtbGtMNVNsVWZ4Y3k5M09OZTBNdWdTUEVScUVMeXY5N0I2UElNVFdkNUh6R2IxUnlWMkFJQXA4Nm5rZ3VUNGlIOXVqSnEteHRQekhOS2I4YUs5RmtlQ1RxUi1tTmpSUFJjQXlpa1pnc2steERfdGRMaGFtby11cWdzTXZEcTV5alhR?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPNkxBTXZQVDNJRkNvdmVZbVdTY2RUZUZSY3dFUjl6STBCbzF1T3ZrWUY2SXZ1ZzFHWkk0LWpfQjBQLUltTzE5dUd0UXBsaGFSY0ctZE5DTzJQX0dkTE5pUVhEeDRTT3hNQkdyOUFKR1RvYlpEU2xoN1A4Z1N6ZEYtWk5sRC10Zlh2NlhDVkxobUNTaG9lamc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPNUJTTHZMRXZtaXhGU3pzdjhvek43SkFTb3VGVjhfMVhpV3ZXdDdkZTZ0LUFnUWRXQXRlYTNEb1RNSlc2R2ozNmw5ZkZoWGt4bkNwSldmTlg5R0NHVl9faWlPTkFCYklrTDh4WHpPQnRJOHlCQkNXczN1R2Z2ejNLRmstTWVZbWlTbU10RHlwelcwZW9RNUxmUDZ3cFJCNEE?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNeVJqX0Z5T2dHeTN6M0pFN2pJU01oTmpnN0h1T1RFVmNBb3IxMzBNZzBieDV1RlExRUY2Q2FkRkZJYV9QMGc4N2pYR3NTdjBCQ0Z6OU5SXzRSeHVldmNfR1kwS1Nob2VOUklvV2hwZWw1blJibkMwTXhMNkFjQlRta1FNT1A1VllGdmZZWWpQSjNoMlFXcUl0MUcxR3J1SGhnUTRuYkU2cmJEZw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNNVd3V3FmWXh1R28xWTN4T21iT1JUWGRCaG1UT1lzZHYtM3FBejhyd0ZPMmVZQzVZQ2x1eUJNR0h2Q2RiMk1qQ3ZlbFM4VGxlNDltWkp5a1I5YmYtMlpST0I3Ums3RndmemowSndyd2pBaVZBX3NIZURZdmRFamU2TW9EWHFxUUlZSFNaWk93TTlJMmc0QXhQVU5ZSnM?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPeFAtWHBZMGdZT1dtTnRWUWIyenV2djVSN3JjOVJuV1pIQjNId1NPS3h1X2FQeDB3cUxEamNaVUl6TUNDLWdwNURyMVZpRjVhXzYxU0duVE9uX0Q5Si15dGdQS1ZwaExSM2RhQUpsdEROVFhuc3RTVHlqR3VPUnFTMWlnNzVObTRhcUtKRm1R?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQc1NSLUxySzlsNnBqd2dQNjhQeHliel8wRHFXNmR2WFpIbFhRbnVobnFaQXBtOXAwTGh1R2hLajFKcHVJcXU2cEx5d19UWXhFNDQ1aVlHYWxBT25DSGVrSzQ1UTN5R2pIVXFOZlBsSnJzSHZqTnhqUXVDUUZucWpoUnJSWXBvWjhOcXBxcEVQbWRuX2JGMHZyV2ZUS216dGM?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
