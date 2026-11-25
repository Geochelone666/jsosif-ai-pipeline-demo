# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:00:23.923002+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 2, 'ai': 15, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 14 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 413.2700 |
| Return 1D (%) | -8.8630 |
| Return 1W (%) | -17.9059 |
| Return 1M (%) | -20.0313 |
| Return YTD (%) | 92.9725 |
| Return 1Y (%) | 92.1739 |
| Annualized volatility (%) | 75.4582 |
| Beta vs SPY | 3.2605 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.2471 |
| Downside deviation (rf=0, %) | 50.2981 |
| Sortino (rf=0) | 1.8710 |
| Historical VaR 95% (1D, %) | 7.1739 |
| Historical ES 95% (1D, %) | 10.2670 |
| Correlation vs SPY | 0.6462 |
| Tracking error vs SPY (%) | 66.7776 |
| P/E (trailing) | 88.31 |
| P/B | 9.91 |
| EV/EBITDA | 60.24 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 23.43 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 17.82 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 1.08 |
| MA50 | 550.4800 |
| Close vs MA50 (%) | -24.9255 |
| MA200 | 431.9976 |
| Close vs MA200 (%) | -4.3351 |
| RSI (14, Wilder) | 38.6840 |
| MACD (12,26) | -23.8474 |
| MACD signal (9) | -15.9923 |
| MACD histogram | -7.8551 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 413.2700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -8.8630 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -17.9059 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -20.0313 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 92.9725 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 92.1739 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 75.4582 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 50.2981 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.8710 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.1739 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.2670 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6462 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 66.7776 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.2605 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2471 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.4303 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0756 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 88.3056 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.6840 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -7.8551 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -24.9255 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -4.3351 -> Slightly below the moving-average trend level.

## TAILWINDS

### Why Is AMD Stock Surging on Monday?
- Summary: AMD shares jump, boosting investor confidence and market perception.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQQnUyRHJUVmlNUWFHdUlKQko5OHl1azVBdU1OVlRqMkpqV0ltVjlHUVA4M3E1YmotSTNzeHp4NmExMkIzcUppQ0lReTdhQ1k1VUJ3Wk5zT0s3VFdOR3hOXzNING5GYlFHeU1ndEVkTFFJcVh2WVJMa0ZfVHBEbmlZMDhVR1JEMDJUTm02ckdiYVVsdlZmRlRkb2h1VWduZw?oc=5>

### Jim Cramer says ‘the time is now’ to put sidelined cash to work
- Summary: Jim Cramer recommends investing AMD cash, signaling positive outlook.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOQktQZTNRUlM1eXJuVnFSVHI0Z0twM3M5MXIyNUVUcHJMYV9SN1JBWVBQY1JsQnlBajRVblEyTUdiX1Y3UWJCeWIxSHllc1YxRWpLZVlYX2JVZ2FvUXJVaWlUN1p0M3VBUG01cUN1SElWaXo1OGlCeU5uQmxqV2hVbmdRTWx4MjRmMnYzQjdPNDZvRUtCWHAyYU45WW5Hb2dvTER4V3hFbElYOXlGMGNhM1B3?oc=5>

### OpenAI and Meta Could Get 320 Million AMD Shares for a Penny Each
- Summary: Potential sale of AMD shares to OpenAI and Meta, indicating partnership opportunity.
- Date: 2026-11-24 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPWm5YRk9KTTJXTGJKeHhFaWtKbS0xamJVR0VHZS1wb2hfR2hjOVR2bW1JY0R5bmxWOFcxVi1tWWFGNkVJVUh1UDBSOS1fUUt3ekdPcTd2c1F3cnFsM0FKOVRHSEJpR0h2UlhNNWRlZ1FqakZUZk1GRktXMTFNdHJ6SUExMTRQVERrMGxFRHZMOVNLWlAtZjlBTEN0bHk4bXJDVmNKRGFSZFFmYnUzQmc?oc=5>

## HEADWINDS

### Advanced Micro Devices registers millions of shares for resale: AMD remains under pressure
- Summary: Advanced Micro Devices registers millions of shares for resale: AMD remains under pressure
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxOMnAwdERIVnh3eU9hN3pCUkRlSnpXVGE2UjVIR1RSc0hCX1VXVjRmSXI3cEUtVXNyUndJNDZ4SXh6aWVrTWMwbHN4RFRmYlpuWnlmMEh4dlpaOGdYNjlLaWdQdVJqdFRwUUlvTVFHUk1xU1NWa1RCa3A2Z3NydVNDV1BNU3hfV1pKQW45dQ?oc=5>

### Advanced Micro Devices falls 8% amid semiconductor and AI pullback (AMD:NASDAQ)
- Summary: Advanced Micro Devices falls 8% amid semiconductor and AI pullback (AMD:NASDAQ)
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPTUg2QWlJLTRKcVhjVDhsSkEzY3Z1RHpyMHZ6U0dDUy04TkxiejBIYndFQU9xYXR5REU3X21JcWxuNDlMZTJXV0VDazdkWVFUcFFyOUp5aXFoelVhd19MTG5HSVBHc09VMjRxY0Y4THF1eE1TVXMyU3pnMU9DelZISzJheTUyVXRRY2dFb3hNTU1XcU1fQ1gyOEY1NmpaTFRSLURlSjA0VFpabDlzcnpUdQ?oc=5>

### Why Is AMD Stock Falling on Friday?
- Summary: Investors concerned about recent performance and market conditions, leading to a decline in AMD shares.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPakd6RUtYYTBuV2dfQVE4SWpBendrV1B4UmdxOUt4R2djNzVkbWo5VV9qTmZ5YjRHaUJwSXhHb0dZMG5RMTJGQVNhcWZyT1prN3JFdFBWN1JWQ0twS3RDc3ZDVjVWbDltUVZWOURuTHZ6V1MxRkhGN3NCZ1V2N1NRX0FPUnRPamJOVU1EYnVRWkRXR2N2TWZUdnJ4WQ?oc=5>

### AMD Stock Shows the Market Has Stopped Making Sense After Huang’s Dramatic Return
- Summary: Stock volatility following CEO Huang’s return, negative market reaction.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxQZFZiUXAwenUzWFNOTXVsanB4ZEdoeU1nMFozQTF5T0NNRnZGZG1UVnhuWXFwb3Rhc2ZlU1h5dVc1aXUydlcxdEl3ZUZGY2p5MzBQUEZGSzNWb1ZkZ2tDQnh4NTJLX2FJUUtfSmVvQllMY3FESV9uc0g5Z25fTlpBV2FHMjhJY3M?oc=5>

### Advanced Micro Devices falls amid Hunterbrook post on X (update)
- Summary: Share price drop linked to Hunterbrook X post, negative impact.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNOC1TMnJ4ZEFqaXY5ekZzemVYLTh1ekgzYWp2Yk1fMm5HVjdoMUtPMG83UUdZVkdsa3ZET2tyX2ZFRDhteTlDZnp5QVFZTUFReUlIS1hva0YwbVJlM3Q4YUV2YllCeWpodmt1TWRBWVQ1SUZ0WFVReW9raHptNzlVZW5BZllkZ2g2NHEtUzdfSXZMZGMyVWc2NXNqd1FTS2dtQWJmNWFQOEtZWEV0WWh0NnZjOWVtOEF4VUZtMWFwa2Y1aWM?oc=5>

### Why Is AMD Stock Plunging Today Despite Strong Wall Street Buy Ratings?
- Summary: Sharp decline in AMD shares despite positive ratings, negative market move.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxNN1BDblNZcFJ1ZnhVV2drcVlxUEpmNk9KZWhWNU9wZXlaRWxSOGtJUXEzRG5XQ0dzX3NucTZLTE8yYkd5TmNQdTlRaVlycm1PUTYzcUtfcXFLbTBBSkJ2QldYaElpV0ZxQ2xYWFhrLVNWZDl3TXJLcnR3SXVBZm9hYTZqWlZYdGVxYk9Tb0c5THQ4dlNVUXItbnA5MTJkZERQU1cwWXlLN3ZKOWZPbWFZS3pJb1Q2clZFR2xoaVpuRU5fS3ZCc1Jual9DTQ?oc=5>

## CATALYSTS

### Advanced Micro Devices, Inc. (AMD) is Attracting Investor Attention: Here is What You Should Know
- Summary: Investor attention highlighted, no specific event disclosed.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOZkZxQzNLc04tWGhod0c2ZmRjeW9pNHdhekQyOENwZ3A5YjhocURDeFpjUFZSNHNnUzRWQktUcGhZUnlmTGZBdTJVcVBxTFM0bC1DRWJidVlKemJlUktpYTQxTGtsUk1xSUZTRmdFRVhEbDdDakFyWl9YSHZ0NkRnaEszRGpZQ3VXM0JyQUxZUlFjS0ZvUGRkbVM4bw?oc=5>

### How to Play AMD Stock as Hunterbrook Slams the Company With a New Short Report
- Summary: Short report issued, negative analyst stance.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOUGtQQXd2TllZXzYtaEJrSkM0c3V1RGRLVlhycU5BNUFKekVfSWVnamYzQ0ZYOUZxeXlyeFNqNmtyYkVxUXE4OEtWNm1VTUIyT0JPdkRSMEctMnJFb0lCUmV5ck16N1g2d2NiaU4zLXg5NGY4alpDRXBCUnpJSTBrY2QwaldESVktbjdXcVNCOE9KR2V1ZTFYMm40VHZjY0dlZGxvdWMyWmVIR1hSSF9JbDhSMzRoOXlyODU1TEc0UQ?oc=5>

### AMD (Advanced Micro Devices) : Bernstein reiterates its Buy rating
- Summary: Buy rating reaffirmed by Bernstein.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOdUEtNDd5TDhvOUhPaGRmSzI2NjhNR0o1ZHNQb1B2Ul9KM0dUZ1lJbXJ4MHJzYkpmdUctREk1OHFFZF9FTUJMajRNZThVVDhRdjZ3WXppVFhTZUlSZjB5bEpGeEZ0Z1JldmRyWHIxaGJYUVBJZTJBV09lUHRHNVBLYTVQbUltT0JwbkRSblo0YnA5NmRjOFBCQnVqTW9fWngzWHNRTUtPWFdCZzIwb3FtWnVNbHV0Zw?oc=5>

### Stock Market Today, Nov. 23: Advanced Micro Devices Climbs on AI-Chip Rebound After Nvidia Reinstates Jensen Huang as CEO
- Summary: AMD shares rose on AI-chip rebound, linked to Nvidia CEO change.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwJBVV95cUxQeWlXazZSREdHVFpCWDBzdG1YTHQwU2JmZXc5Y0dqamhsaTV0YWo5UzFqbUk2aVM0Q0p6TWtxb3kzdUQtdVVySWg0V3lNRm1SSlNuMmx3V09SVGhvZUh6bS1hNmFHR05ENGdHSjRDR1o1SmxnTXJMYmQ0ZWdTRmhBbk0xTjBENHdoRUQ3RG1waTZNYkNodEFMdHZrQjRkRmJUUkxPWkxLR3dkUXdyaTNGcmwxdlp5SlFtRmxpMENLRTBoWDV3aE45cktrVU94Rnk2cXdlXzg1d3hQZ2g3NWgxbmxjc2trcEtvN1o1S3VHNThuS2dnTmZSVU15aUF2ZWFaaTdwU0ZKOWsyTnc?oc=5>

### AMD After The Selloff: A 26x P/E With A Server Business Set To Double (NASDAQ:AMD)
- Summary: Highlights a 26x P/E and projected doubling of server business, indicating positive growth prospects.
- Date: 2026-11-24 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNU00zTjg0NklSdWdOQkE4R0NNVUtrMmRVS2hRX0FUdm1mMEpPWDhkc1l1X084YkZTblBnZUdkbGJKcGhEaG5lUEpvV2VLN09pWEVFaVBtZTdESGdqTEthVUkySlc2ZGtrRTZFR2w2NndWN2xjeVZHZnUzbk9ucVNlMFRlY0pkWmVzZXp3dG5YeUI1MHlsUWFGSlhQQ0RJc0JORldENU44OEYzdmVMTFE?oc=5>

## RISKS

### AMD Gained From Nvidia’s China Scandal. Now a Short Seller Says AMD Has a China Problem Too.
- Summary: Short seller alleges AMD faces China issues after Nvidia scandal.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNM2UyYnM1anhCMjQ0bTNQYXVwLWRhMHVoOFRWZU5kUXRvbksxQUM2UW5vYTBkX0U4RXZZVUlySTZ6UEV3SEp0OTM4UmVudnk0dUFtZm1aTTR2b001MnJmdnJZVFBzaTFmOU1hcTljTDktZm5OampyVklMUmJkYzliWVJHSXhoM3MxYmFtN3l0RzU4X1kydWNCQkhhc2g?oc=5>

### AMD Shares Plunge 8% as Ties to Multiple US Entity List Firms Draw Scrutiny, Export Controls May Curb Overseas Sales
- Summary: Export controls linked to US entity list firms may limit AMD's overseas sales, causing a sharp share price drop.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxPbkRmNld6T2M5OHpTemtNMlh0OEpkSl9iNFJSb05tdGdQclRXM2lfZHdlX1hyOVVybU82NDlyUUlYbnBuSjlUem5say1ZU2NZTTlnV3NPREtiUTBrNVAwVHZXeHdaS0p4RmNyYndXdjYxd1lGY0I1T29kOTBINVJObDZWTTQ4TjNuMFNxQm8wU2J2a2lCSnV4Ynh1c3IwWDYxRGVsRzFiRldCQXBjUGRWNjJRUV9vc3NBdEFQd2Rhc0p3UFN6VGN3ZjdRRHdqb2t5TlBlOWx3?oc=5>

### Own AMD Stock? Watch Its Pile Of Unsold Chips
- Summary: Notes unsold chip inventory, signaling potential supply risk for AMD.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNSlptN0ZHOG51cTZwcldTekpsUmhwNzBfakxoR2M2X2h4VnpQWWNvbWY1RXN6TGEtR0pEbF80Y0lVN1FwVFlGNmxSaDF6dlVvTXlqZFJ5dWsxY0h2NFhTcHRFX0NYUjgwM2pkZ3ozSzRyWGxPbWwtMEpKNVBtS2ZIXzdYazlYNGV3ZFY1YjBKeVdTVEk?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **88.31** | **9.91** | **60.24** | **44.70** | **683,988,942,848.00 USD** | **92.17** |
| NVDA | 16.69 | 14.05 | 15.15 | 103.20 | 3,751,960,903,680.00 USD | -14.68 |
| INTC | N/A | 2.53 | 15.89 | 20.90 | 291,261,972,480.00 USD | 53.12 |
| AVGO | 38.45 | 14.42 | 28.18 | 85.50 | 1,437,244,456,960.00 USD | -19.75 |

Peers fetched as_of: 2026-11-24; AMD reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,428,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMingFBVV95cUxQQnUyRHJUVmlNUWFHdUlKQko5OHl1azVBdU1OVlRqMkpqV0ltVjlHUVA4M3E1YmotSTNzeHp4NmExMkIzcUppQ0lReTdhQ1k1VUJ3Wk5zT0s3VFdOR3hOXzNING5GYlFHeU1ndEVkTFFJcVh2WVJMa0ZfVHBEbmlZMDhVR1JEMDJUTm02ckdiYVVsdlZmRlRkb2h1VWduZw?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxOQktQZTNRUlM1eXJuVnFSVHI0Z0twM3M5MXIyNUVUcHJMYV9SN1JBWVBQY1JsQnlBajRVblEyTUdiX1Y3UWJCeWIxSHllc1YxRWpLZVlYX2JVZ2FvUXJVaWlUN1p0M3VBUG01cUN1SElWaXo1OGlCeU5uQmxqV2hVbmdRTWx4MjRmMnYzQjdPNDZvRUtCWHAyYU45WW5Hb2dvTER4V3hFbElYOXlGMGNhM1B3?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPWm5YRk9KTTJXTGJKeHhFaWtKbS0xamJVR0VHZS1wb2hfR2hjOVR2bW1JY0R5bmxWOFcxVi1tWWFGNkVJVUh1UDBSOS1fUUt3ekdPcTd2c1F3cnFsM0FKOVRHSEJpR0h2UlhNNWRlZ1FqakZUZk1GRktXMTFNdHJ6SUExMTRQVERrMGxFRHZMOVNLWlAtZjlBTEN0bHk4bXJDVmNKRGFSZFFmYnUzQmc?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxOMnAwdERIVnh3eU9hN3pCUkRlSnpXVGE2UjVIR1RSc0hCX1VXVjRmSXI3cEUtVXNyUndJNDZ4SXh6aWVrTWMwbHN4RFRmYlpuWnlmMEh4dlpaOGdYNjlLaWdQdVJqdFRwUUlvTVFHUk1xU1NWa1RCa3A2Z3NydVNDV1BNU3hfV1pKQW45dQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPTUg2QWlJLTRKcVhjVDhsSkEzY3Z1RHpyMHZ6U0dDUy04TkxiejBIYndFQU9xYXR5REU3X21JcWxuNDlMZTJXV0VDazdkWVFUcFFyOUp5aXFoelVhd19MTG5HSVBHc09VMjRxY0Y4THF1eE1TVXMyU3pnMU9DelZISzJheTUyVXRRY2dFb3hNTU1XcU1fQ1gyOEY1NmpaTFRSLURlSjA0VFpabDlzcnpUdQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPakd6RUtYYTBuV2dfQVE4SWpBendrV1B4UmdxOUt4R2djNzVkbWo5VV9qTmZ5YjRHaUJwSXhHb0dZMG5RMTJGQVNhcWZyT1prN3JFdFBWN1JWQ0twS3RDc3ZDVjVWbDltUVZWOURuTHZ6V1MxRkhGN3NCZ1V2N1NRX0FPUnRPamJOVU1EYnVRWkRXR2N2TWZUdnJ4WQ?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxQZFZiUXAwenUzWFNOTXVsanB4ZEdoeU1nMFozQTF5T0NNRnZGZG1UVnhuWXFwb3Rhc2ZlU1h5dVc1aXUydlcxdEl3ZUZGY2p5MzBQUEZGSzNWb1ZkZ2tDQnh4NTJLX2FJUUtfSmVvQllMY3FESV9uc0g5Z25fTlpBV2FHMjhJY3M?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNOC1TMnJ4ZEFqaXY5ekZzemVYLTh1ekgzYWp2Yk1fMm5HVjdoMUtPMG83UUdZVkdsa3ZET2tyX2ZFRDhteTlDZnp5QVFZTUFReUlIS1hva0YwbVJlM3Q4YUV2YllCeWpodmt1TWRBWVQ1SUZ0WFVReW9raHptNzlVZW5BZllkZ2g2NHEtUzdfSXZMZGMyVWc2NXNqd1FTS2dtQWJmNWFQOEtZWEV0WWh0NnZjOWVtOEF4VUZtMWFwa2Y1aWM?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxNN1BDblNZcFJ1ZnhVV2drcVlxUEpmNk9KZWhWNU9wZXlaRWxSOGtJUXEzRG5XQ0dzX3NucTZLTE8yYkd5TmNQdTlRaVlycm1PUTYzcUtfcXFLbTBBSkJ2QldYaElpV0ZxQ2xYWFhrLVNWZDl3TXJLcnR3SXVBZm9hYTZqWlZYdGVxYk9Tb0c5THQ4dlNVUXItbnA5MTJkZERQU1cwWXlLN3ZKOWZPbWFZS3pJb1Q2clZFR2xoaVpuRU5fS3ZCc1Jual9DTQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOZkZxQzNLc04tWGhod0c2ZmRjeW9pNHdhekQyOENwZ3A5YjhocURDeFpjUFZSNHNnUzRWQktUcGhZUnlmTGZBdTJVcVBxTFM0bC1DRWJidVlKemJlUktpYTQxTGtsUk1xSUZTRmdFRVhEbDdDakFyWl9YSHZ0NkRnaEszRGpZQ3VXM0JyQUxZUlFjS0ZvUGRkbVM4bw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOUGtQQXd2TllZXzYtaEJrSkM0c3V1RGRLVlhycU5BNUFKekVfSWVnamYzQ0ZYOUZxeXlyeFNqNmtyYkVxUXE4OEtWNm1VTUIyT0JPdkRSMEctMnJFb0lCUmV5ck16N1g2d2NiaU4zLXg5NGY4alpDRXBCUnpJSTBrY2QwaldESVktbjdXcVNCOE9KR2V1ZTFYMm40VHZjY0dlZGxvdWMyWmVIR1hSSF9JbDhSMzRoOXlyODU1TEc0UQ?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOdUEtNDd5TDhvOUhPaGRmSzI2NjhNR0o1ZHNQb1B2Ul9KM0dUZ1lJbXJ4MHJzYkpmdUctREk1OHFFZF9FTUJMajRNZThVVDhRdjZ3WXppVFhTZUlSZjB5bEpGeEZ0Z1JldmRyWHIxaGJYUVBJZTJBV09lUHRHNVBLYTVQbUltT0JwbkRSblo0YnA5NmRjOFBCQnVqTW9fWngzWHNRTUtPWFdCZzIwb3FtWnVNbHV0Zw?oc=5
- https://news.google.com/rss/articles/CBMiiwJBVV95cUxQeWlXazZSREdHVFpCWDBzdG1YTHQwU2JmZXc5Y0dqamhsaTV0YWo5UzFqbUk2aVM0Q0p6TWtxb3kzdUQtdVVySWg0V3lNRm1SSlNuMmx3V09SVGhvZUh6bS1hNmFHR05ENGdHSjRDR1o1SmxnTXJMYmQ0ZWdTRmhBbk0xTjBENHdoRUQ3RG1waTZNYkNodEFMdHZrQjRkRmJUUkxPWkxLR3dkUXdyaTNGcmwxdlp5SlFtRmxpMENLRTBoWDV3aE45cktrVU94Rnk2cXdlXzg1d3hQZ2g3NWgxbmxjc2trcEtvN1o1S3VHNThuS2dnTmZSVU15aUF2ZWFaaTdwU0ZKOWsyTnc?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNU00zTjg0NklSdWdOQkE4R0NNVUtrMmRVS2hRX0FUdm1mMEpPWDhkc1l1X084YkZTblBnZUdkbGJKcGhEaG5lUEpvV2VLN09pWEVFaVBtZTdESGdqTEthVUkySlc2ZGtrRTZFR2w2NndWN2xjeVZHZnUzbk9ucVNlMFRlY0pkWmVzZXp3dG5YeUI1MHlsUWFGSlhQQ0RJc0JORldENU44OEYzdmVMTFE?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNM2UyYnM1anhCMjQ0bTNQYXVwLWRhMHVoOFRWZU5kUXRvbksxQUM2UW5vYTBkX0U4RXZZVUlySTZ6UEV3SEp0OTM4UmVudnk0dUFtZm1aTTR2b001MnJmdnJZVFBzaTFmOU1hcTljTDktZm5OampyVklMUmJkYzliWVJHSXhoM3MxYmFtN3l0RzU4X1kydWNCQkhhc2g?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxPbkRmNld6T2M5OHpTemtNMlh0OEpkSl9iNFJSb05tdGdQclRXM2lfZHdlX1hyOVVybU82NDlyUUlYbnBuSjlUem5say1ZU2NZTTlnV3NPREtiUTBrNVAwVHZXeHdaS0p4RmNyYndXdjYxd1lGY0I1T29kOTBINVJObDZWTTQ4TjNuMFNxQm8wU2J2a2lCSnV4Ynh1c3IwWDYxRGVsRzFiRldCQXBjUGRWNjJRUV9vc3NBdEFQd2Rhc0p3UFN6VGN3ZjdRRHdqb2t5TlBlOWx3?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNSlptN0ZHOG51cTZwcldTekpsUmhwNzBfakxoR2M2X2h4VnpQWWNvbWY1RXN6TGEtR0pEbF80Y0lVN1FwVFlGNmxSaDF6dlVvTXlqZFJ5dWsxY0h2NFhTcHRFX0NYUjgwM2pkZ3ozSzRyWGxPbWwtMEpKNVBtS2ZIXzdYazlYNGV3ZFY1YjBKeVdTVEk?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
