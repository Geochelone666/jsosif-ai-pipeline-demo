# DIS Intelligence Report

- ticker: **DIS**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/DIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/DIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:59:09.496232+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 2, 'ai': 11, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/DIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 14 named publishers; 0 exact duplicates; 22 HTTPS source links; largest publisher share 18.18%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 119.6500 |
| Return 1D (%) | 0.3691 |
| Return 1W (%) | 0.5885 |
| Return 1M (%) | 10.7358 |
| Return YTD (%) | 5.9742 |
| Return 1Y (%) | 5.6879 |
| Annualized volatility (%) | 27.2720 |
| Beta vs SPY | 0.6032 |
| Max drawdown (%) | -20.2451 |
| Sharpe (rf=0) | 0.3400 |
| Downside deviation (rf=0, %) | 19.2475 |
| Sortino (rf=0) | 0.4818 |
| Historical VaR 95% (1D, %) | 2.4075 |
| Historical ES 95% (1D, %) | 3.7715 |
| Correlation vs SPY | 0.3037 |
| Tracking error vs SPY (%) | 26.5492 |
| P/E (trailing) | 24.57 |
| P/B | 1.88 |
| EV/EBITDA | 12.13 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 15.97 |
| Gross margin (%) | 37.59 |
| Operating margin (%) | 15.61 |
| Return on equity (%) | 8.01 |
| Free cash flow yield (%) | 2.35 |
| MA50 | 108.7592 |
| Close vs MA50 (%) | 10.0137 |
| MA200 | 103.2667 |
| Close vs MA200 (%) | 15.8650 |
| RSI (14, Wilder) | 71.3045 |
| MACD (12,26) | 3.0468 |
| MACD signal (9) | 2.4154 |
| MACD histogram | 0.6314 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'DIS': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 119.6500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.3691 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.5885 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 10.7358 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 5.9742 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 5.6879 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 27.2720 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.2475 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4818 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4075 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.7715 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3037 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.5492 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6032 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2451 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3400 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.9695 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 37.5950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.6120 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.0100 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.3526 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 24.5688 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 71.3045 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6314 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 10.0137 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 15.8650 -> Clearly above the moving-average trend level.

## TAILWINDS

### Walt Disney (DIS) Stock on Tuesday: Rises 0.08%, RSI Overbought
- Summary: Walt Disney (DIS) Stock on Tuesday: Rises 0.08%, RSI Overbought
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOUWJqRk95ZXNNUGs5eEZiUlJfOTNXM0JMVDE4bXZOTkhxdER0Nmd0WmJYQ0VWalhha1didlRPTU9xRzlZeXZsWHd2WGVDbzRldDI5VVJteXpGc053STZFUGdrbjF1YUlENWF0aEFnUzJLWXc0M3o4c0RSSFJfSDJwa2U2aUJnbUhLY3FEVElhc3N1UFo1MU9CaUhteC0ydw?oc=5>

### Disney (DIS) Stock Looks Fairly Valued As Cash Flow Holds Up
- Summary: Disney’s valuation appears fair with stable cash flow, suggesting a positive outlook.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNUTNPQVVubVlnZVVCd0JScnZIWDFNdTZjRjV0dW1kbnZmYmFNUTFJM3laVWxFNEN4Xy1FT0YtOTFPRGY3X09Ea05JRTVDYk5ScF92anN3cl9zbG1sRWpwcV9nWjhGYl92bU50NDB6R3o4Vkx3TWlrejZDeWtLWU5oZWpkd2NBdGFHWjRnc2pWd1p6bV9TbnJsN2lR?oc=5>

### Disney (DIS) to Launch User-Generated Vertical Videos and Free T
- Summary: Disney announces new vertical video platform and free T‑shirt service, expanding content offerings.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxOa28weGZ1VmRPc3U4Q0poRXhwRHl0NVduaGhtODRWT2VjaW8yUUlsQ1QxZ1E1ZjZ0NHk1VjkwbldUaHV6MDh4R3M0cnJlS2djTk1EM2xXbmxQeC04N1htYlk5bVZoUTF3d1ZBalprd3BleWhfdF84VUhOTW9SZnkzdmRtTFdZWlVRRUp3X2FlR3Z2QnZCVGFpbnBSM1ZEcVRIa2k1Sk1FRG9QVXpRZjR4aS11Q2p2ZnBMQ3VjY253NW0xaGFjdUln?oc=5>

### Skydance Sinks 9% as Warner Bros. Film Slump Overshadows Earnings Beat; Netflix Falls 2%, Disney Dips
- Summary: Disney shares dipped slightly amid Skydance slump, reflecting broader market softness.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxQbGZDSjRSeWtYaV9Yd0VheG1vQ2tIUW5aOV9NTENCZTNIWGNVdGNNVzlBTlBpVUo2eG9LM3ZjTE9UTlhsWm5HNEI4cDFYT1BhVVU2ekpjVmxwUmN1SFN5aFhaUzAyd1VJak9ZcWxRdW10czluQy16QUFwUnE3djNwWWVpS1Z5cnlNR0t2SUpYYlZzMXBOVGdxSXpacWRVQ1hkMDdlY2NhSDZuQ2NENjNsQU9idDRMSVVLY2ZPekdHa0MtTlNYWnNVT1NJVi1HVjF0ZGM0UV9FQQ?oc=5>

### Disney (DIS) Stock Looks Fairly Valued After Its 34% Rise
- Summary: Stock surged 34%, suggesting favorable valuation and investor sentiment.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNMTJCZWR1TUdoN3pVTEJ1MW1XZ1FDR0FtV3hxb2t6U3BQcFI3OGRlWkVSNXF3d1F0WFdoZy1xMUJKY29fQ09OUlh0VW9pOFdHcEdfN240R2F3VVV4ckdhSDlBV0hfcUw5T084TW1Bei1uS0NfV1RiNzYtR0NQdGVrSG9LOVpWdUNSbVhNM05JYlJRbVNjcW05QkFhZ2hLa0hIeEpWTUxJWFpmZVdZMkkxWjFmbHI1Nll6UnfSAb8BQVVfeXFMUF9yRGdYNTNpaElTbEo0NExoX3lwN3M4NFF4ZFNQN2ttbEF5V3NtMFZGQ0toOTBETkwtbS1UYXdCT2hTajRlRkVnN0hiMkF2YkZiZWNXNUt3MVEySkJzRzFIcDRESll5QTJONVNtNk9SV0g2T0tzWW9NQjF1eElxRWk1dVVkS0RNZWVGN1Z3bzI4bXp5R2tRMTBKU2x0OS1UOE5hY2tpb3dBcnoxWVNiSERDQWd2MzB1WmpTeTFja0E?oc=5>

### RSI Overbought, DIS Stock Gains 4.18% on Wednesday
- Summary: Technical indicator shows overbought condition, yet stock rose 4.18% today.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOQkk3dzlhbllDQXR0dzZ4LXoxb3hBakpfS2xIR3dCSXdZT0lEQnptUkU4SE5aMXlNZ05CVGhJcDlabDJWS1dpWGhCS3g5ODJwZTdsZzhLVmRwZmQzZ2ZrcUIyTDlLZjVKSXVVbDBuOTA0WjVVODB5VHBudmpKZExma0I2b3RaUk9oMHpPTkQtaTg?oc=5>

## HEADWINDS

### DIS Stock Layoffs: What to Know as Disney Plans More Layoffs
- Summary: DIS Stock Layoffs: What to Know as Disney Plans More Layoffs
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNQnBnQ2dJT3M2X213aFBVSnpOQ3dWUlN2NWFXdTlCdjZiNERvM2lCSmFyRjJCSHFidkNRRHAtaFlvdjFxeTZTbkhXMl9NNDh3aUFiaUcyejlSby1oV18tZkdmVlU3dURTWGFrZ3N4N3hxSjloaWpyM2c0MWFvV0NYNTRfendCZ3FWYkcyQmJjanhzUE5VdG5FU19xRm4zTzlTSWhGZjdB?oc=5>

### Here's Why Walt Disney (DIS) Gained But Lagged the Market Today
- Summary: Disney’s stock outperformed the market but still fell short of broader gains, indicating weaker relative momentum.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNNlhJRVlqOVREZDZ0SVlEdlNxeUxFWE4wOXQ2cmw5VEtTWlVaeERPcjh6bExDcDgzQUJMTkdpWDZhdmprREJUT0FmU21zVmc1ZFRjMGRxYnk0OXFlSXV6Q0dsS3R5Y2NtZmJmQkMwSmoyeGM4LThhZnV5VU5fRGQ2NzZCUDNxMld0WERRQ19tRnlCaFFV?oc=5>

### How to Play DIS Stock as Disney Eyes 20% Cost Cuts and Thousands of Layoffs
- Summary: Disney plans significant cost cuts and layoffs, indicating potential operational challenges.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNUVhqVHpqTlVYeFlSalNiY2t2cTE1R2FNWU5IRFotWjhDVms3dGk0R0o3ZDFWOVFYQ3RhcHpTc0FyTXRXM19ITUM0SjVEemUxSC1fTDdvaG13QmQzeXdOZDdKem5IeTJHU19NalVKRUhmRWZHNzJqNnZ2bWYzSWw0WjFyaktUNTJrUUk2aE1IOTV3U0YzUDFsTFQxTm5BamVVRWxJNG02Q0ticzdUSFBKemFqTHpsS3RmeXc?oc=5>

## CATALYSTS

### Disney steps up generative AI push with expanded Adobe collaboration (DIS:NYSE)
- Summary: Disney expands AI partnership with Adobe, enhancing content creation capabilities.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNMVBZa2NnNXZwbFdEX0lzZ2NCakVidkNTV2pjUVdaQ2dEVkhDZXFoc1IwNmQ0NlhHei1IQ1pVdWVXNGI1b25ReW9wSU5NaUFfeVNkN25WR3lhSW4tR25nTXlLb0tGMFFoV0NfVXBuc1Q1azdVc2plZ01LWU9jblZSbEN3bXpWRGhBTVhEX2JmQ0MyRlBmZVFyYVRxM3p0SmEtd3lOUFlfYw?oc=5>

### Walt Disney Company (The) (DIS) Stock Forecasts
- Summary: Forecasts on Disney’s stock performance.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOeTJOWnNWWS1OV1VMTWJ4ZlFrR2lTX2FuUjNod3Z5cnFCUmMzN0ZnVnR2VHdMdFdiaEdhSWlta1pOUnhPTEVGVjdvLXRtV2pmNEVraDhVaWVjMFp2emkzT1l4ZGlUaFJ5YUpZNXNmYlpIWDY0aUZLcmR2X0V1MUZnZjFoREZEdE1wbFJoOEhDVWw?oc=5>

### Did Adobe AI Partnership Just Shift Disney (DIS) Stock's Investment Narrative?
- Summary: Adobe's AI partnership may influence Disney's investment outlook, potentially affecting its stock narrative.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQS2twRlk2TkNTMm4yZWZHM2xIQTZ5dG4xZ0hCN3AzNzRoUnFpSldTLTd6Qi1tMGlOSzZjaUtkeGxnU196QXdIT1QxOTNyVHkyM19KaTVaMmhkZHluSmRpQmY4Q3FrRXUxc2cyWVVhOWZ6NVNkLURqQWNqem41S0l4d3EzV2dUejg2dmVzR2hNaktuejRjTWVFckxKOEkxWmtsM1dVZTFEemdTaFpfRUY0YndEMFBPNDhUbmZGSEhtNThaZ9IBxwFBVV95cUxON0pSbVQ4ZDdhUjF1RE8xUnNHb0t3cU5qMFJhZ1VicXpnb3l5OEIxV0RBdXY2akdTdUhKb2hmZWdCejZmaEE1N0R0Sk5BOS05WUlmTmJEdE1tVUhUQl95V0dDeFlQemNBNWlxQ3FoYVR4QVNpQUtoMk1zUlVvNEhzS2VKLURMTjNwNGQtMDB1UTB6aHBqcTlsN0ZMNHFqR2tMSk9Ca0tGc3o3Q2pKLWRmUFkxcDVoNnFZcTR6UnNHeERGZWdMZ3Zz?oc=5>

### Disney (DIS) Signs Adobe Deal for Custom AI Models to Speed Up Creative Production
- Summary: Disney partners with Adobe to develop custom AI models, aiming to accelerate creative production workflows.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQbW9Dd2Y2bnIwd1I4VXdibWJXOEh1NktWa3ZPbTNxSENZbExPWUJodEhJVU9fS25rRUpCNHdmOEI1bHkxYXlCNkVtajZSajRZZTh3aGtNenFXTVJlMW9JQUQ5cE15bVFQWXBxZEtadGdBNFJRcmVZY1l0SWxWaFY2LVJoOGoxa1hpbXQyZTNJNEhqOG5TOG9uN0doN1lSQ0RYdGMtVUJjei1kMk1WREZZ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **DIS** | **24.57** | **1.88** | **12.13** | **6.80** | **206,598,078,464.00 USD** | **5.69** |
| NFLX | 18.65 | 9.05 | 17.19 | 11.80 | 265,022,291,968.00 USD | -43.21 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| PSKY | N/A | 0.93 | 7.95 | 0.90 | 10,992,190,464.00 USD | N/A |

Peers fetched as_of: 2026-11-11; DIS reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-05
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 25,248,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,638,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1744489/000174448926000057/dis-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMingFBVV95cUxOUWJqRk95ZXNNUGs5eEZiUlJfOTNXM0JMVDE4bXZOTkhxdER0Nmd0WmJYQ0VWalhha1didlRPTU9xRzlZeXZsWHd2WGVDbzRldDI5VVJteXpGc053STZFUGdrbjF1YUlENWF0aEFnUzJLWXc0M3o4c0RSSFJfSDJwa2U2aUJnbUhLY3FEVElhc3N1UFo1MU9CaUhteC0ydw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNUTNPQVVubVlnZVVCd0JScnZIWDFNdTZjRjV0dW1kbnZmYmFNUTFJM3laVWxFNEN4Xy1FT0YtOTFPRGY3X09Ea05JRTVDYk5ScF92anN3cl9zbG1sRWpwcV9nWjhGYl92bU50NDB6R3o4Vkx3TWlrejZDeWtLWU5oZWpkd2NBdGFHWjRnc2pWd1p6bV9TbnJsN2lR?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxOa28weGZ1VmRPc3U4Q0poRXhwRHl0NVduaGhtODRWT2VjaW8yUUlsQ1QxZ1E1ZjZ0NHk1VjkwbldUaHV6MDh4R3M0cnJlS2djTk1EM2xXbmxQeC04N1htYlk5bVZoUTF3d1ZBalprd3BleWhfdF84VUhOTW9SZnkzdmRtTFdZWlVRRUp3X2FlR3Z2QnZCVGFpbnBSM1ZEcVRIa2k1Sk1FRG9QVXpRZjR4aS11Q2p2ZnBMQ3VjY253NW0xaGFjdUln?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxQbGZDSjRSeWtYaV9Yd0VheG1vQ2tIUW5aOV9NTENCZTNIWGNVdGNNVzlBTlBpVUo2eG9LM3ZjTE9UTlhsWm5HNEI4cDFYT1BhVVU2ekpjVmxwUmN1SFN5aFhaUzAyd1VJak9ZcWxRdW10czluQy16QUFwUnE3djNwWWVpS1Z5cnlNR0t2SUpYYlZzMXBOVGdxSXpacWRVQ1hkMDdlY2NhSDZuQ2NENjNsQU9idDRMSVVLY2ZPekdHa0MtTlNYWnNVT1NJVi1HVjF0ZGM0UV9FQQ?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNMTJCZWR1TUdoN3pVTEJ1MW1XZ1FDR0FtV3hxb2t6U3BQcFI3OGRlWkVSNXF3d1F0WFdoZy1xMUJKY29fQ09OUlh0VW9pOFdHcEdfN240R2F3VVV4ckdhSDlBV0hfcUw5T084TW1Bei1uS0NfV1RiNzYtR0NQdGVrSG9LOVpWdUNSbVhNM05JYlJRbVNjcW05QkFhZ2hLa0hIeEpWTUxJWFpmZVdZMkkxWjFmbHI1Nll6UnfSAb8BQVVfeXFMUF9yRGdYNTNpaElTbEo0NExoX3lwN3M4NFF4ZFNQN2ttbEF5V3NtMFZGQ0toOTBETkwtbS1UYXdCT2hTajRlRkVnN0hiMkF2YkZiZWNXNUt3MVEySkJzRzFIcDRESll5QTJONVNtNk9SV0g2T0tzWW9NQjF1eElxRWk1dVVkS0RNZWVGN1Z3bzI4bXp5R2tRMTBKU2x0OS1UOE5hY2tpb3dBcnoxWVNiSERDQWd2MzB1WmpTeTFja0E?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOQkk3dzlhbllDQXR0dzZ4LXoxb3hBakpfS2xIR3dCSXdZT0lEQnptUkU4SE5aMXlNZ05CVGhJcDlabDJWS1dpWGhCS3g5ODJwZTdsZzhLVmRwZmQzZ2ZrcUIyTDlLZjVKSXVVbDBuOTA0WjVVODB5VHBudmpKZExma0I2b3RaUk9oMHpPTkQtaTg?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNQnBnQ2dJT3M2X213aFBVSnpOQ3dWUlN2NWFXdTlCdjZiNERvM2lCSmFyRjJCSHFidkNRRHAtaFlvdjFxeTZTbkhXMl9NNDh3aUFiaUcyejlSby1oV18tZkdmVlU3dURTWGFrZ3N4N3hxSjloaWpyM2c0MWFvV0NYNTRfendCZ3FWYkcyQmJjanhzUE5VdG5FU19xRm4zTzlTSWhGZjdB?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNNlhJRVlqOVREZDZ0SVlEdlNxeUxFWE4wOXQ2cmw5VEtTWlVaeERPcjh6bExDcDgzQUJMTkdpWDZhdmprREJUT0FmU21zVmc1ZFRjMGRxYnk0OXFlSXV6Q0dsS3R5Y2NtZmJmQkMwSmoyeGM4LThhZnV5VU5fRGQ2NzZCUDNxMld0WERRQ19tRnlCaFFV?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNUVhqVHpqTlVYeFlSalNiY2t2cTE1R2FNWU5IRFotWjhDVms3dGk0R0o3ZDFWOVFYQ3RhcHpTc0FyTXRXM19ITUM0SjVEemUxSC1fTDdvaG13QmQzeXdOZDdKem5IeTJHU19NalVKRUhmRWZHNzJqNnZ2bWYzSWw0WjFyaktUNTJrUUk2aE1IOTV3U0YzUDFsTFQxTm5BamVVRWxJNG02Q0ticzdUSFBKemFqTHpsS3RmeXc?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNMVBZa2NnNXZwbFdEX0lzZ2NCakVidkNTV2pjUVdaQ2dEVkhDZXFoc1IwNmQ0NlhHei1IQ1pVdWVXNGI1b25ReW9wSU5NaUFfeVNkN25WR3lhSW4tR25nTXlLb0tGMFFoV0NfVXBuc1Q1azdVc2plZ01LWU9jblZSbEN3bXpWRGhBTVhEX2JmQ0MyRlBmZVFyYVRxM3p0SmEtd3lOUFlfYw?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOeTJOWnNWWS1OV1VMTWJ4ZlFrR2lTX2FuUjNod3Z5cnFCUmMzN0ZnVnR2VHdMdFdiaEdhSWlta1pOUnhPTEVGVjdvLXRtV2pmNEVraDhVaWVjMFp2emkzT1l4ZGlUaFJ5YUpZNXNmYlpIWDY0aUZLcmR2X0V1MUZnZjFoREZEdE1wbFJoOEhDVWw?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQS2twRlk2TkNTMm4yZWZHM2xIQTZ5dG4xZ0hCN3AzNzRoUnFpSldTLTd6Qi1tMGlOSzZjaUtkeGxnU196QXdIT1QxOTNyVHkyM19KaTVaMmhkZHluSmRpQmY4Q3FrRXUxc2cyWVVhOWZ6NVNkLURqQWNqem41S0l4d3EzV2dUejg2dmVzR2hNaktuejRjTWVFckxKOEkxWmtsM1dVZTFEemdTaFpfRUY0YndEMFBPNDhUbmZGSEhtNThaZ9IBxwFBVV95cUxON0pSbVQ4ZDdhUjF1RE8xUnNHb0t3cU5qMFJhZ1VicXpnb3l5OEIxV0RBdXY2akdTdUhKb2hmZWdCejZmaEE1N0R0Sk5BOS05WUlmTmJEdE1tVUhUQl95V0dDeFlQemNBNWlxQ3FoYVR4QVNpQUtoMk1zUlVvNEhzS2VKLURMTjNwNGQtMDB1UTB6aHBqcTlsN0ZMNHFqR2tMSk9Ca0tGc3o3Q2pKLWRmUFkxcDVoNnFZcTR6UnNHeERGZWdMZ3Zz?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQbW9Dd2Y2bnIwd1I4VXdibWJXOEh1NktWa3ZPbTNxSENZbExPWUJodEhJVU9fS25rRUpCNHdmOEI1bHkxYXlCNkVtajZSajRZZTh3aGtNenFXTVJlMW9JQUQ5cE15bVFQWXBxZEtadGdBNFJRcmVZY1l0SWxWaFY2LVJoOGoxa1hpbXQyZTNJNEhqOG5TOG9uN0doN1lSQ0RYdGMtVUJjei1kMk1WREZZ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
