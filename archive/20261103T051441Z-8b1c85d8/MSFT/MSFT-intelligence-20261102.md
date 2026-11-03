# MSFT Intelligence Report

- ticker: **MSFT**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/MSFT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MSFT/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:16:23.350783+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 6, 'ai': 13, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/MSFT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 45.83%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 507.1200 |
| Return 1D (%) | -2.8338 |
| Return 1W (%) | -4.7841 |
| Return 1M (%) | -2.0115 |
| Return YTD (%) | 5.5244 |
| Return 1Y (%) | -1.2587 |
| Annualized volatility (%) | 32.9773 |
| Beta vs SPY | 1.0027 |
| Max drawdown (%) | -31.3261 |
| Sharpe (rf=0) | 0.1276 |
| Downside deviation (rf=0, %) | 21.3836 |
| Sortino (rf=0) | 0.1968 |
| Historical VaR 95% (1D, %) | 2.7896 |
| Historical ES 95% (1D, %) | 4.0430 |
| Correlation vs SPY | 0.3898 |
| Tracking error vs SPY (%) | 30.3682 |
| P/E (trailing) | 27.24 |
| P/B | 8.00 |
| EV/EBITDA | 18.65 |
| Revenue growth (%) | 18.80 |
| Forward P/E (estimate) | 20.97 |
| Gross margin (%) | 67.66 |
| Operating margin (%) | 49.76 |
| Return on equity (%) | 34.22 |
| Free cash flow yield (%) | 0.08 |
| MA50 | 513.3882 |
| Close vs MA50 (%) | -1.2209 |
| MA200 | 437.1206 |
| Close vs MA200 (%) | 16.0137 |
| RSI (14, Wilder) | 40.1377 |
| MACD (12,26) | 2.7391 |
| MACD signal (9) | 6.1985 |
| MACD histogram | -3.4594 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MSFT': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 507.1200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.8338 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.7841 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -2.0115 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 5.5244 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -1.2587 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 32.9773 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.3836 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1968 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.7896 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.0430 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3898 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.3682 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.0027 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -31.3261 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1276 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.9733 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 67.6570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 49.7570 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 34.2210 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.0795 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.2352 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 40.1377 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.4594 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -1.2209 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 16.0137 -> Clearly above the moving-average trend level.

## TAILWINDS

### Microsoft stock jumps 4% as cloud growth drives earnings and revenue beat
- Summary: Microsoft stock jumps 4% as cloud growth drives earnings and revenue beat
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxNclpVVGdGd3NYYWo4bGNFRTVlYjhQc0VhMzhmZnRsRnlTNkRidVNwaGlQVVdPMktwMHRMYzhUTWpYUXFYaVFfZFRkSkRmbDNGOWxVa29MSWhhUDk4RE9BVElXUTY3SWo2SHRNbGVhRU9vbjd3ZHJnZlpTdHpSbHpDNNIBhgFBVV95cUxNRXA0VC1WZEYxMWVmenJmdVRiRzhDRFVzUVNVNlJXaEJDc011NjZuT2VHdTJLYndYaGV1NDM2UU93Zm12X1J2VWtYMEJNQ3ZkU0Nhb3M0c0dQT3pzVFl3eTlqLWluNHJjRHpVRTJicTdqSXNTSHBVQjdKWlJtYjZjN2tQZkc3dw?oc=5>

### Microsoft Just Revealed a $677 Billion Reason to Buy Its Stock
- Summary: Microsoft announces a $677B rationale for buying its shares, signaling strong confidence in future growth.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPRUJBeDZkZHk3ZlR5WXA2U2JGdS1nYnBfc0UwazNMaTlvWnRhLVY1dG9sVl9tZVBCZjFxbk1maTdaWk1GOG5OdnJBWWxDS3hMdVRzdTdJYUxyeXlWMmYyeGRjQlBVS25XZERVMC1MT3ZQVURXTkpzSmUtc3V1MVdnbWd4MGdDTnN0YXVZY0JoM0F2S2VIS3E1QmFyN1VBaXU5Tmc?oc=5>

### Microsoft Corp. (MSFT) Surges 37.8% on Record Quarterly Gains
- Summary: MSFT stock jumps 37.8% after reporting record quarterly earnings, boosting investor sentiment.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOQXo2dG9qMTRmU003ZF92OVVZQlpfU2JuS25fczJhUHpGWVFQNm1sQjYwSV9wd0IwNTBzZkZzdjVwNktPRkxNRGtlR3FGUFIya0hEenBBUHhHcy1JeFNWdUhmQjZFRExqcHZndzZzSDl0NXRBNUNwSUFhTi1DRTN5RTU1b0EtMS1YWjQ0NDM2bTd1dzlJVFV6VG5n?oc=5>

### Microsoft: I'm Betting On Azure (NASDAQ:MSFT)
- Summary: Microsoft executive expresses confidence in Azure, highlighting its importance to the company’s strategy.
- Date: 2026-11-02 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiekFVX3lxTE5KOWpoLUVIdjVxNkZUVE1DYWI0WERra3RrNXdyaTJZY3FCR0hmX0JVX1dNZ2g2N2p6Q2tKUFA5MFVyWVFDY3ZLbEhjLXc0bllCVHZqZXlHR3NjaUdyVm9qWkZNNHUtdkNMUWRNNUF2NmlHaDRvQ0NfZzBB?oc=5>

### Microsoft: The AI Race Has A Winner, And The Market Completely Missed It (NASDAQ:MSFT)
- Summary: Microsoft claims AI leadership, suggesting strong future growth.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxOaGtKdHV4UTFNclk5a0RsWk9KNmRIemFYOFB5Wk9lWUY1Um1HTm9zNFVlSTZZdDVHTm5ORDhZSnZEWEl4OXFDRlJJR1JWQzFKNWZLd2tSSlltR08zeUVCZTF6QkRzTndXb0xIZzRfOFhPc2E0cHlxWmRNcXBVdXlDczcwajJhYWJWVU5VeXFWcHNpZTZZM21hN1ZuMXItRkNjbWtpTGFyYS1BbTdRdHVHSg?oc=5>

### Microsoft Corporation (MSFT) Delivers Strong Azure Growth as AI Demand Exceeds Supply
- Summary: Azure revenue surges due to high AI demand.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWVhoYmtlZjVaYkFjNy1oNkJqMDA1d1E0MGRCbjF4Sk5weHRGVDhHTFhubDJkMmpmOEFYTnJLZGp2Nmg0TXpiTDZtVk1hZXdiSEpaVUZUYnpvOFZPUUxLU28ydGpRMzlIeTJKNWFaVlVsbjk2N1YzTWl6bEdCMVNFUWR5U0l1RjgwTXgtenowT0o1dmlVcU8xTDlGS2tPeXpBSVFOdER0S1pfQQ?oc=5>

### Microsoft Corp.’s (MSFT) AI Advantage: Scale, Trust, and Economic Value
- Summary: Microsoft highlights AI strengths in scale and trust.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPR0hrdUNkMEMwbE5ibl80WlQxNHdWWHRxODdNYTBEbWNsOFRSVHpzWF9FdTVHbEtENWx5M2lsTDd6cER2MGlHLVhCUkV5cDhXS05uaHpSSVpHRHd0VDhDZFZWNUkyMnBXRU9JTE9iZUdpUG16dk0xN3ZGcllDUEgzcF9EanZ5X3RHVU1xWnc0OUtnZ2lTME1sUjV4RUo?oc=5>

## HEADWINDS

### Microsoft Stock (NASDAQ:MSFT) Slips as New Scam Emerges
- Summary: Microsoft Stock (NASDAQ:MSFT) Slips as New Scam Emerges
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOQ0QzLVJOaDZOaHlZNUxLczVHYmNpMTNPcERZb0FUQzdYcUYtajFjMkh5Mldvb3czZU16Wlh4a2pvWnRabVpLc1Iwa1h1MVMzRTRDeC1zU19IMDNmOWxoeFl2dk1zN0sxWGJNcGQ3bEVKRFV1cVY2NmdZZW1WRjR6SGFfbEhSWVJuSnc?oc=5>

## CATALYSTS

### Microsoft Delivered a Beat on Both Earnings and Revenue. Here’s How to Think About MSFT Stock Now.
- Summary: Microsoft Delivered a Beat on Both Earnings and Revenue. Here’s How to Think About MSFT Stock Now.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQMklLMEw0WDU1anlpRDg1aHFyekJ6Q1VaRFpQb256emNMSTFGUjFZOUMwcEQwMWMwUkN3U1BiaHJ6R3RGSzZhWERGVmpVNDdrXzhlYnVUdUZsaFl6TXF3NWdXczFpUGRXQ2hTNGNUQVRORzR5VlhkVENqak9qSGFmdzh4MWhqY3I0UkROOEZmdnVmRTF3aXRVOXJPTmZnaFNVa3JVOF9B?oc=5>

### Microsoft (MSFT) Stock Gets Fair Value Bump On Azure And AI Optimism
- Summary: Microsoft (MSFT) Stock Gets Fair Value Bump On Azure And AI Optimism
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOOGFuV1U3LUZsekt0ZU1FV3RlMWN4RDdGUENlVlM3SXhHUFlJSkk3S1AyU2taci1pMGN2ZTE3VDR5UmpqN19rajZQQXNsbmtQaEQyOHY0R1ZRZzZDNXVhTkk5MzBYOEk2WjAtX2JWZ3lWQWU1bmdYZHJLNk9LaW9BWEl2am5PTXo4UHlXaTNJYk5obEZwdl9RSVJfZw?oc=5>

### Microsoft (MSFT) Stock Shrugs Off Q1 Earnings As AI Spending Looms
- Summary: Microsoft (MSFT) Stock Shrugs Off Q1 Earnings As AI Spending Looms
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNcVl0VWhEWUhhTi1wb2pFS2EwdEhvem12dWtCNENMNGRhNjVCbkJ4OHJsLWgtaVRSa2xXcFFoQ1I0RzNLRVdUTmhjYVVkZDJQTmM3SUdZUk5jcWFxZjZfcnJrQnF4Qm5ickpyOU01QmJqMUNsQ2l4UjNmWU9BcDN3Nzk1NUVsTklzTmtUQnM4dTlFLVZEQzRpVkgtUWo?oc=5>

### Microsoft (MSFT) Lands $25 Billion Bond Deal As AI Push Deepens
- Summary: Microsoft (MSFT) Lands $25 Billion Bond Deal As AI Push Deepens
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPbHJpVVFoMThPSnp3Yi1DZFFZMi12UmtEUDR0Q2ZFVFhITFIxRm84UWpSallCak90Z0ZkczVrTzBhRlduclJMbm5GR3VUdTNNN1ZLWGpLUE5EN19oQl9EOGlaYjV0ckYtWC1hUHJKempYak1yaGR5ODF3TU5ELUdjNXlva05OWFl2LWplV1M4bWdDQnVrT251T3lkSQ?oc=5>

### Here’s How Much Microsoft Stock Is Expected to Move After Earnings
- Summary: Anticipated post-earnings stock movement for Microsoft.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNQVNKTWNlM2x1Sm5oa2M2TDd5QUVvdGhWQ0ItRkpQdDluN1lhRkhCOFBpTjNhUlBQRWVaUlFDR3E4b1R2WnNFQlB6TjcxZEE3c3BweW5OY1ZWNzk4aWltVEdibjdrOHNMTGtRNm9QcVh5a0Z1aFpxaTNPTmdDbXNNeGUwalJHUUpxd2NsUFJlcUkzQXhaVmtBTVcxV3ByS3FxQ2VZakxqRFhySV84dTZESGhQNzRYMlRTT0ozZlJrNUNkU0J4NEE?oc=5>

### Should You Buy And Hold Microsoft Stock?
- Summary: An investment advisory piece discussing the merits of holding Microsoft shares, offering a neutral stance on future performance.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQcHRINTdUZlVPQnFtbHd5b3lONVpTemJCdnNndXh4NS13d3FYTGVldGdNVTZsS0NkVHNlTW0zWUlhM1JjZHRxbmdyT3phdXgyckczbjlBSzF3dUpNTGZxZm1TOGVOSVJiM0FRR2h2R1k1d21NZi1jdzJRMEs3YlkwLXpYMkh3VDFjUU9IOVBYWTNDSm94UC1ESVEzMWk1QzNlbWc?oc=5>

### Microsoft Stock Has One Thing Left To Prove
- Summary: Commentary on Microsoft’s stock performance, suggesting a single remaining factor to validate its valuation.
- Date: 2026-11-01 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxORFdZTE1zVmY5a2dfaFdTcTN0aWZaS3FmcllCSHRQbVpfSFFtM1hYMUdDcTVscThEZmZfaE56RDQxaWNIaV9vYjN1VWZCdXFmV0kwRS1vSmpQNjNyNUNmeUZOQVp1c0JrcFdoNTlNZkQ3NnlZN2VvRi1ZcGZ3TXhRZ1FGaHkycEM2R01NMEJsSHZpWVZsdFRTM3V4dERmWTE3aG11ZU4wRQ?oc=5>

### What Could Surprise Microsoft Stock Investors On The Upside?
- Summary: Speculation about potential upside factors for MSFT investors, suggesting upcoming positive developments.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNY3E2YmVpd2JPblRCUFhZeWFLcDJsUTRDWXJtNnNCVFVoQnNsNEpfT2xLQi1rWnp3WUxVYV9mVC1BZS1fc2VzN1ExRnRGT0xTMHFiVkpYekZhZi11eEJUQjVlWkRGZmdkM0pBQW1MTWQwaDB5LUFUNE5SOXRCaWpWNU1RTkpzek95VllIXy1HVGdxM0pBRzJJdHQ4UXRndWdrWFlHbFRaQml6aTdyZnF1MjQ4M1VCS3dEUkw3RA?oc=5>

### Microsoft Beat Again. Its Stock Is Still Lower Than a Year Ago
- Summary: Microsoft reported earnings that beat expectations, though its stock remains below last year's level.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNb3RPR1ZNU25VcS1ad09XX1FlZnJrWENqMXcyNThFc3JkZVVfQmRGOWZ5QVNxMTNjdU9QOS0yQ0QtT2ZHMEloR0NUQmpuUGtCTENYTi1JaURIWjBjVWNhdGFtbUJRb0stRW5obEJ5aXpYN3ZadTlzM1hORGpta1hKeTJSRk9wcXo0X2IxeUlrMzRJMEUtWER2cTZsUGVvcE1TZE90aE9xb0U?oc=5>

## RISKS

### AI Bond Funding Might Change The Case For Investing In Microsoft (MSFT)
- Summary: AI bond funding could alter MSFT investment outlook.
- Date: 2026-11-02 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxORnhOQUtrTXZjTkcyUElCQ2VNeTQ3VzZ0SHhaRzRKOUdTTThnLUlwVGhxckVBUm5zdDBkTUdKNlFnaGZ1WXpqdUhQM2dxYjRWQUFqZEh0NEp2UEp4b19OZ1pJNXE1ay1GZTJ4NWc5N0o3RzRheFJKd016RXhxY1J0azdxUkxMZHdpLWFmUVBxblMyWlRoUUFXRA?oc=5>

### ETFs Are Net Sellers of Microsoft (MSFT) on Thursday
- Summary: Exchange-traded funds sold Microsoft shares, indicating a short-term sell pressure.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPVXlBRDVRWWpFT1JuRUkzSnlzSVZmUWpZUU9GWEVURGRZR3RxSnJsb196TlQzUkFFNEwxRFZlZThxNzRRR0VYejlqMzFyQmFfTGF5QWhNMkgtdUg2b0RxUTQ3amlMaDY0WEk3NXA1MFZiQzVrejAyREpjXzVvSkUzbjY4LUs0TGg1TkxfbWhvWVFOUUJrWEc0MEdaNDE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MSFT** | **27.24** | **8.00** | **18.65** | **18.80** | **3,765,971,714,048.00 USD** | **-1.26** |
| ORCL | 20.48 | 5.83 | 14.46 | 29.60 | 361,415,573,504.00 USD | -53.99 |
| GOOGL | 14.57 | 5.20 | 17.97 | 24.70 | 3,429,902,843,904.00 USD | -0.52 |
| AMZN | 19.86 | 4.33 | 15.49 | 12.10 | 2,656,031,211,520.00 USD | 0.58 |

Peers fetched as_of: 2026-11-02; MSFT reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMigAFBVV95cUxNclpVVGdGd3NYYWo4bGNFRTVlYjhQc0VhMzhmZnRsRnlTNkRidVNwaGlQVVdPMktwMHRMYzhUTWpYUXFYaVFfZFRkSkRmbDNGOWxVa29MSWhhUDk4RE9BVElXUTY3SWo2SHRNbGVhRU9vbjd3ZHJnZlpTdHpSbHpDNNIBhgFBVV95cUxNRXA0VC1WZEYxMWVmenJmdVRiRzhDRFVzUVNVNlJXaEJDc011NjZuT2VHdTJLYndYaGV1NDM2UU93Zm12X1J2VWtYMEJNQ3ZkU0Nhb3M0c0dQT3pzVFl3eTlqLWluNHJjRHpVRTJicTdqSXNTSHBVQjdKWlJtYjZjN2tQZkc3dw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPRUJBeDZkZHk3ZlR5WXA2U2JGdS1nYnBfc0UwazNMaTlvWnRhLVY1dG9sVl9tZVBCZjFxbk1maTdaWk1GOG5OdnJBWWxDS3hMdVRzdTdJYUxyeXlWMmYyeGRjQlBVS25XZERVMC1MT3ZQVURXTkpzSmUtc3V1MVdnbWd4MGdDTnN0YXVZY0JoM0F2S2VIS3E1QmFyN1VBaXU5Tmc?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOQXo2dG9qMTRmU003ZF92OVVZQlpfU2JuS25fczJhUHpGWVFQNm1sQjYwSV9wd0IwNTBzZkZzdjVwNktPRkxNRGtlR3FGUFIya0hEenBBUHhHcy1JeFNWdUhmQjZFRExqcHZndzZzSDl0NXRBNUNwSUFhTi1DRTN5RTU1b0EtMS1YWjQ0NDM2bTd1dzlJVFV6VG5n?oc=5
- https://news.google.com/rss/articles/CBMiekFVX3lxTE5KOWpoLUVIdjVxNkZUVE1DYWI0WERra3RrNXdyaTJZY3FCR0hmX0JVX1dNZ2g2N2p6Q2tKUFA5MFVyWVFDY3ZLbEhjLXc0bllCVHZqZXlHR3NjaUdyVm9qWkZNNHUtdkNMUWRNNUF2NmlHaDRvQ0NfZzBB?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxOaGtKdHV4UTFNclk5a0RsWk9KNmRIemFYOFB5Wk9lWUY1Um1HTm9zNFVlSTZZdDVHTm5ORDhZSnZEWEl4OXFDRlJJR1JWQzFKNWZLd2tSSlltR08zeUVCZTF6QkRzTndXb0xIZzRfOFhPc2E0cHlxWmRNcXBVdXlDczcwajJhYWJWVU5VeXFWcHNpZTZZM21hN1ZuMXItRkNjbWtpTGFyYS1BbTdRdHVHSg?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWVhoYmtlZjVaYkFjNy1oNkJqMDA1d1E0MGRCbjF4Sk5weHRGVDhHTFhubDJkMmpmOEFYTnJLZGp2Nmg0TXpiTDZtVk1hZXdiSEpaVUZUYnpvOFZPUUxLU28ydGpRMzlIeTJKNWFaVlVsbjk2N1YzTWl6bEdCMVNFUWR5U0l1RjgwTXgtenowT0o1dmlVcU8xTDlGS2tPeXpBSVFOdER0S1pfQQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPR0hrdUNkMEMwbE5ibl80WlQxNHdWWHRxODdNYTBEbWNsOFRSVHpzWF9FdTVHbEtENWx5M2lsTDd6cER2MGlHLVhCUkV5cDhXS05uaHpSSVpHRHd0VDhDZFZWNUkyMnBXRU9JTE9iZUdpUG16dk0xN3ZGcllDUEgzcF9EanZ5X3RHVU1xWnc0OUtnZ2lTME1sUjV4RUo?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOQ0QzLVJOaDZOaHlZNUxLczVHYmNpMTNPcERZb0FUQzdYcUYtajFjMkh5Mldvb3czZU16Wlh4a2pvWnRabVpLc1Iwa1h1MVMzRTRDeC1zU19IMDNmOWxoeFl2dk1zN0sxWGJNcGQ3bEVKRFV1cVY2NmdZZW1WRjR6SGFfbEhSWVJuSnc?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQMklLMEw0WDU1anlpRDg1aHFyekJ6Q1VaRFpQb256emNMSTFGUjFZOUMwcEQwMWMwUkN3U1BiaHJ6R3RGSzZhWERGVmpVNDdrXzhlYnVUdUZsaFl6TXF3NWdXczFpUGRXQ2hTNGNUQVRORzR5VlhkVENqak9qSGFmdzh4MWhqY3I0UkROOEZmdnVmRTF3aXRVOXJPTmZnaFNVa3JVOF9B?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQT1lkOTk4d0ZMa1ZYOTRrOHhNV0ZmNVJhZ0lOTGVnVTk5S2tYYkw0Y0wyX1lkRWtnVjREZ1pGVmM4bGRjZ292dGNjdzlYNEtEcVBzUGU5X2l2WFF3N2JEZFItZzdxVW9Bc0sycDcyY2swcHVkZ1M1cTBac2R6Nm5LdFpMUXFQYW5KQTduM1NMYkkyLW8yaUwwWWpKT3JUM21DZjYyZUh4X28xWjJCak1EdmJqMFFEQ0dzN2ZDN3hWZTZ3aXF0YmVBRjc2dmZTUVNEa3hiWlN3?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOOGFuV1U3LUZsekt0ZU1FV3RlMWN4RDdGUENlVlM3SXhHUFlJSkk3S1AyU2taci1pMGN2ZTE3VDR5UmpqN19rajZQQXNsbmtQaEQyOHY0R1ZRZzZDNXVhTkk5MzBYOEk2WjAtX2JWZ3lWQWU1bmdYZHJLNk9LaW9BWEl2am5PTXo4UHlXaTNJYk5obEZwdl9RSVJfZw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNcVl0VWhEWUhhTi1wb2pFS2EwdEhvem12dWtCNENMNGRhNjVCbkJ4OHJsLWgtaVRSa2xXcFFoQ1I0RzNLRVdUTmhjYVVkZDJQTmM3SUdZUk5jcWFxZjZfcnJrQnF4Qm5ickpyOU01QmJqMUNsQ2l4UjNmWU9BcDN3Nzk1NUVsTklzTmtUQnM4dTlFLVZEQzRpVkgtUWo?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPbHJpVVFoMThPSnp3Yi1DZFFZMi12UmtEUDR0Q2ZFVFhITFIxRm84UWpSallCak90Z0ZkczVrTzBhRlduclJMbm5GR3VUdTNNN1ZLWGpLUE5EN19oQl9EOGlaYjV0ckYtWC1hUHJKempYak1yaGR5ODF3TU5ELUdjNXlva05OWFl2LWplV1M4bWdDQnVrT251T3lkSQ?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNQVNKTWNlM2x1Sm5oa2M2TDd5QUVvdGhWQ0ItRkpQdDluN1lhRkhCOFBpTjNhUlBQRWVaUlFDR3E4b1R2WnNFQlB6TjcxZEE3c3BweW5OY1ZWNzk4aWltVEdibjdrOHNMTGtRNm9QcVh5a0Z1aFpxaTNPTmdDbXNNeGUwalJHUUpxd2NsUFJlcUkzQXhaVmtBTVcxV3ByS3FxQ2VZakxqRFhySV84dTZESGhQNzRYMlRTT0ozZlJrNUNkU0J4NEE?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQcHRINTdUZlVPQnFtbHd5b3lONVpTemJCdnNndXh4NS13d3FYTGVldGdNVTZsS0NkVHNlTW0zWUlhM1JjZHRxbmdyT3phdXgyckczbjlBSzF3dUpNTGZxZm1TOGVOSVJiM0FRR2h2R1k1d21NZi1jdzJRMEs3YlkwLXpYMkh3VDFjUU9IOVBYWTNDSm94UC1ESVEzMWk1QzNlbWc?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxORFdZTE1zVmY5a2dfaFdTcTN0aWZaS3FmcllCSHRQbVpfSFFtM1hYMUdDcTVscThEZmZfaE56RDQxaWNIaV9vYjN1VWZCdXFmV0kwRS1vSmpQNjNyNUNmeUZOQVp1c0JrcFdoNTlNZkQ3NnlZN2VvRi1ZcGZ3TXhRZ1FGaHkycEM2R01NMEJsSHZpWVZsdFRTM3V4dERmWTE3aG11ZU4wRQ?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNY3E2YmVpd2JPblRCUFhZeWFLcDJsUTRDWXJtNnNCVFVoQnNsNEpfT2xLQi1rWnp3WUxVYV9mVC1BZS1fc2VzN1ExRnRGT0xTMHFiVkpYekZhZi11eEJUQjVlWkRGZmdkM0pBQW1MTWQwaDB5LUFUNE5SOXRCaWpWNU1RTkpzek95VllIXy1HVGdxM0pBRzJJdHQ4UXRndWdrWFlHbFRaQml6aTdyZnF1MjQ4M1VCS3dEUkw3RA?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNb3RPR1ZNU25VcS1ad09XX1FlZnJrWENqMXcyNThFc3JkZVVfQmRGOWZ5QVNxMTNjdU9QOS0yQ0QtT2ZHMEloR0NUQmpuUGtCTENYTi1JaURIWjBjVWNhdGFtbUJRb0stRW5obEJ5aXpYN3ZadTlzM1hORGpta1hKeTJSRk9wcXo0X2IxeUlrMzRJMEUtWER2cTZsUGVvcE1TZE90aE9xb0U?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxORnhOQUtrTXZjTkcyUElCQ2VNeTQ3VzZ0SHhaRzRKOUdTTThnLUlwVGhxckVBUm5zdDBkTUdKNlFnaGZ1WXpqdUhQM2dxYjRWQUFqZEh0NEp2UEp4b19OZ1pJNXE1ay1GZTJ4NWc5N0o3RzRheFJKd016RXhxY1J0azdxUkxMZHdpLWFmUVBxblMyWlRoUUFXRA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPVXlBRDVRWWpFT1JuRUkzSnlzSVZmUWpZUU9GWEVURGRZR3RxSnJsb196TlQzUkFFNEwxRFZlZThxNzRRR0VYejlqMzFyQmFfTGF5QWhNMkgtdUg2b0RxUTQ3amlMaDY0WEk3NXA1MFZiQzVrejAyREpjXzVvSkUzbjY4LUs0TGg1TkxfbWhvWVFOUUJrWEc0MEdaNDE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
