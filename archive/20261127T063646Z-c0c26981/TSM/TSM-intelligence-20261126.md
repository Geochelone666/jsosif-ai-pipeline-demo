# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:40:57.199506+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 0, 'ai': 13, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **14** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 10 named publishers; 4 exact duplicates; 21 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-11-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 342.3400 |
| Return 1D (%) | -1.9645 |
| Return 1W (%) | -5.5926 |
| Return 1M (%) | -18.2003 |
| Return YTD (%) | 13.5384 |
| Return 1Y (%) | 21.5270 |
| Annualized volatility (%) | 45.8438 |
| Beta vs SPY | 2.3368 |
| Max drawdown (%) | -34.3948 |
| Sharpe (rf=0) | 0.6552 |
| Downside deviation (rf=0, %) | 31.4005 |
| Sortino (rf=0) | 0.9565 |
| Historical VaR 95% (1D, %) | 4.3901 |
| Historical ES 95% (1D, %) | 6.3161 |
| Correlation vs SPY | 0.7611 |
| Tracking error vs SPY (%) | 35.8155 |
| P/E (trailing) | 22.19 |
| P/B | 65.76 |
| EV/EBITDA | 3.14 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 14.66 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 57.96 |
| Return on equity (%) | 41.86 |
| Free cash flow yield (%) | N/A |
| MA50 | 418.2630 |
| Close vs MA50 (%) | -18.1520 |
| MA200 | 402.2330 |
| Close vs MA200 (%) | -14.8901 |
| RSI (14, Wilder) | 38.8712 |
| MACD (12,26) | -20.6778 |
| MACD signal (9) | -17.5711 |
| MACD histogram | -3.1067 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 342.3400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.9645 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.5926 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -18.2003 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 13.5384 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 21.5270 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 45.8438 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 31.4005 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.9565 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.3901 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.3161 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7611 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.8155 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.3368 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -34.3948 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6552 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.6623 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 57.9610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8600 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.1867 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.8712 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.1067 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -18.1520 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -14.8901 -> Clearly below the moving-average trend level.

## TAILWINDS

### TSMC: AI Kingmaker Trading At A Bargain Price (NYSE:TSM)
- Summary: TSMC seen as a bargain AI chipmaker, boosting investor sentiment.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxQYjFERGdLY0xwaVdRX0NkTm94ZGZLY2FvNmdGN0UxWnc3NnUyd0ppSndDSjFUZ3BoeEZHODc0NWthak1sLTBZb3hIbkpRRDlPQkhZRXBlZG5VZUJHVzQ1c0lxV0ZjcVcxLVVCdGJKT1RXdXpDdTB0dDlsdXJjNjhtVDFiWTNEVFRNNU1VOXhB?oc=5>

## HEADWINDS

### Huang Boost Fades Quickly as AI Fears Sink TSMC, SK Hynix Shares
- Summary: AI concerns depress TSMC shares, weakening market outlook.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPSnVQX0EyNnpsTDJhNldDLUZpQWh2am54cXVKTlN1LTVidU50TkZPVFh0UzhZUmpfQno3UHlWaE5qcW9IaFlQaUdXcWFjNjVkVWdCX3VBYXBQMllvY2hoTEFOWVFBQl9qQVhnMXRvNExRTHVzbjIwUVMzNzBpMFlaVmZ0cXNLbW42eXFaVWxmWHlMcVNJeDJfdw?oc=5>

### Taiwan Semiconductor Manufacturing Is Down Nearly 30% From Its High. Is It a Bargain Buy?
- Summary: TSMC shares fell 30% from peak, raising concerns about valuation.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQUG1CLWd6UFFmUUhnN3FheVlWZzFRd05DeFk2TFVsTlBoYzBJbzYzYkdoTlk4RlRUWFc1eFZEdGJJRWJnRUlWcmd1dmU2ekVCeUp0RnNmbFlJMWZMUFdFSVFQNkJoRnB2Z2NoNzlBYzlGcUJLVVVqakVzQ3BHWm9BaDVNaFVPNUNyMHRVUjkzTGZKRG9aNXdnUDhoUERtUFd1X01rWjRJaFpXNjRMSDRNUQ?oc=5>

## CATALYSTS

### Trump Warns of “Paying 200 Percent on Chips” in Two Years. That Pushes TSMC Toward a $22.6 Billion Texas Plant
- Summary: Potential U.S. plant expansion could boost TSMC’s production capacity.
- Date: 2026-11-24 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxNeVNuU2V1WFJMVG1qWmkwNUZqQjh5WWk3eFEtcC10ZWhGQU1GNC14bWw3NllTSjZpOVpEVFlybFVsTmd6ZDVaSzlFU3lTdEhfWG5nMklCVXhrOHhKN1ZyRF82NmJkYUVWbHo3Z1N2X0RldDJ4WTZXN3pTd1Iwb2dUZTNzN1hqV0NVVkREZmNhOEpPd1VYemtKOG9xSFhzbzN5YVluZVFKeUtQeUVYQWlQUUEzRmh2bWQzMk5CbTVFMWF4Z0ZURXItWm0taU9nSjYweHE2S2phU0JLbFd6V1E?oc=5>

### Down On TSMC Stock? Your Buy Price Decides It
- Summary: TSM stock performance depends on buy price, indicating market sensitivity.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOLWc4NXFYcWoxVVljOGZaR2kzVHF2QnY5X2l0eEY4Ri1BWGNhTzlMWWhiM1BLdWtXWnN2QWhabzliQzBSYjI1UFBMV3gxYUlqMnBfTjhqWTBDb0Z0SUFCeTBxdVRvTjBNVEF2ZFVmeWFXSXQyZ0RNbTZpb0dlYmhLT2Yzc2hzam5ENVVzZzJOSC1kWWN3cjI5WTh0Nm1xVWlGSlVsR2NIWQ?oc=5>

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Stock May Be Reasonable After New Export Curbs
- Summary: TSM stock may be reasonable following new export curbs, suggesting potential upside.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPa1JvdC0wSGFvVjBwYUYzVlhoX2FHMkdLMUdUUUtibHZhUmJzWkxoT24wQlBjeGZfWGxydF92YnAxN3BDRl9VdkFtTVRiY0tyc1ZjS1RYWE16NUN1X2ZDLW1SRW9vYmdxSmhFMzU5UmdJSV81RE9XOGNIWEYwZFJCMm1OWTFzWS1hckRybm9MVXZLUV9HVTRNZmZRNVdMNDlhVkprUC1DYTBKOHdv?oc=5>

### Tech rally sparks 14% rise in Taiwan Semiconductor Manufacturing (TSM:NYSE)
- Summary: 14% rise due to tech rally, no specific company event.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNRTRBZ2lSU1RSRkx2U2U5eDRld2g4V0dfZlY5QjFhX1JPeVlrM2g3WFIxMnhodldqNFlJZHN5VGNFWWRXX0ZyZVBLdDJVWkVseTNyc3hFYjFLR3dBOS1rVVlQaVdzSkxoMEh4NGJwQVNjdGJaV3lvbjd3aUFhVzFKNFBkd2VDdFl6bGhwSWxGb292WWEzQnkxU3dtOHhjQlJNS2xz?oc=5>

### History Says TSMC Stock Falls Before Its Sales
- Summary: Stock fell before sales announcement, no event specified.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPUFFsQTg2cVZWZjh5R3RsUk1QbkdWTC1VazlPT25ONmVqZ3EyY3o2LU9Sa1BFN1VJZjRiOGF1bXJIZlNKYjYxX3lZdm5RTjE3aHRJUWMzcHg0UWJSYkxLaWJSTHo5VkllWGN1ZjRwX1NpWlhiOVBqNk9BdDFNWXNhRmU4UDZBQUtJckFHYlBPM3ZWOC1vNjVScVl0QUE2bG5RckpvT1E4Wm0xQQ?oc=5>

### Nvidia vs. TSMC: With Jensen Huang Back, Which AI Stock Is the Better Buy for 2027?
- Summary: Analyst comparison of TSMC vs Nvidia for 2027, offering investment guidance.
- Date: 2026-11-23 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNdWhCeTlBalBJa1lLUlZlX0xlOWFaWUZQS2VTRVFUUEJwbWVrcU85OTVwQXRKRG9ZUldYZjNaZHk0QWN2dWtPblkwdXluTjB5cDFnZjMzMVEyaVZSZG9QVTdvVUFGSFV1Yk1vd09tQ3Y3NTN1RzNpMHBNQUtsZzBOZFpBdDhjeXRQaWw3MTNFX2Y1ZUdkbjZhZFBmYzNuZ1pUSFlhb3laRG50X0IzQm8wM1p2bUtwOHdSSUMxejNSR1FLZlVnbTZQMzVkR0o?oc=5>

### Is Trending Stock Taiwan Semiconductor Manufacturing Company Ltd. (TSM) a Buy Now?
- Summary: Analyst question about TSMC’s current buyability.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOVnFQVHNkWVBBYzM1bTVkQXBrMHdVbC0xOHdmLXk2Z0Ztb2NmSjRnX1lndE40bTdfNGR6dUx6Y1VGeEkxeTQ1cVRlVm12RWVCUGZUZEFYWEJrMHRkMDBLMzdZYnJLaFdVcXdHMW5TWElSalRwZS1JLWdtdm1BMFZ1cl9BN0tzblJuUDE2U3Jwa2l5ZDNGQTV3aHNhT3Y5QVhDTmY3NzB2YlIzUVVCeGh4eEJRMDI?oc=5>

### Why TSMC Stock Soared Today
- Summary: TSMC shares surged today, reflecting positive market sentiment.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOMEdpVWJwSTh1cU9tb25IQWwwR3VjdlNfYWZUYXI5b3lrZzRTb3c3SHBqVy00endjamt2M3RvMFZLcGZRTmRLcTZTOE92ejJqM09vejF6Y29zRy02XzRQeGJ2a2ZKaTVDNE5DeU1YbjJUc3NOM3plT3NJOWZWZ1ZoTm9YZ0JZZkZGMXZwUkNxQ3NnSVhDWDVn?oc=5>

### TSMC Stock Just Had Its Best Day Since 2008
- Summary: TSMC shares surged, marking the strongest performance since 2008, reflecting investor optimism and strong market demand.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQeVFFYS1CVFNpYzJZQ2VUM3hMOGFJb2ZnRV9vMzZpYnlXUEZEOTlTZVFwdkg3SGZHekhoRnNKRXlrNU5UeXROQzZHdE5qd2dDcG5pVTFfYnVVa0tPVUkwRUNWQ242R292azd3ckM1dTQwVUF4MlJPNUNNaTRfSG9OQmE2MjUtTmJ5ZWUxVEhYWGw?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) May Make Its $22.6 Billion Texas Plant Conditional
- Summary: TSM may condition its $22.6B Texas plant on regulatory approvals, potentially delaying construction.
- Date: 2026-11-26 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQY0Vwa0dtbVZjbmlKcW1zeXlsNlZRNFc2YkJTNURRbnJnTWI4aVZTbHZQMWY3UWpJb0FKRjJQOFJSMDFWU0NlVGUtM3NYd2FQTVNycno0U1hDNmp4Tml1OXllS0hVenotUzlDVkxsUThzd3VXUFpyek9uMC1EbjFlOURDZERyZkVEUm40ZGV2RGUzeExVcDN1d1hqMXpfTDUzZ3RyZHNR?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **22.19** | **65.76** | **3.14** | **50.90** | **1,775,537,094,656.00 USD** | **21.53** |
| UMC | 12.44 | 2.28 | -0.33 | 25.60 | 33,077,800,960.00 USD | 84.62 |
| GFS | 103.43 | 1.69 | 9.69 | 12.50 | 20,179,646,464.00 USD | 5.04 |
| INTC | N/A | 2.52 | 15.80 | 20.90 | 289,508,032,512.00 USD | 52.02 |

Peers fetched as_of: 2026-11-26; TSM reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-26

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

- https://news.google.com/rss/articles/CBMijgFBVV95cUxQYjFERGdLY0xwaVdRX0NkTm94ZGZLY2FvNmdGN0UxWnc3NnUyd0ppSndDSjFUZ3BoeEZHODc0NWthak1sLTBZb3hIbkpRRDlPQkhZRXBlZG5VZUJHVzQ1c0lxV0ZjcVcxLVVCdGJKT1RXdXpDdTB0dDlsdXJjNjhtVDFiWTNEVFRNNU1VOXhB?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPSnVQX0EyNnpsTDJhNldDLUZpQWh2am54cXVKTlN1LTVidU50TkZPVFh0UzhZUmpfQno3UHlWaE5qcW9IaFlQaUdXcWFjNjVkVWdCX3VBYXBQMllvY2hoTEFOWVFBQl9qQVhnMXRvNExRTHVzbjIwUVMzNzBpMFlaVmZ0cXNLbW42eXFaVWxmWHlMcVNJeDJfdw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQUG1CLWd6UFFmUUhnN3FheVlWZzFRd05DeFk2TFVsTlBoYzBJbzYzYkdoTlk4RlRUWFc1eFZEdGJJRWJnRUlWcmd1dmU2ekVCeUp0RnNmbFlJMWZMUFdFSVFQNkJoRnB2Z2NoNzlBYzlGcUJLVVVqakVzQ3BHWm9BaDVNaFVPNUNyMHRVUjkzTGZKRG9aNXdnUDhoUERtUFd1X01rWjRJaFpXNjRMSDRNUQ?oc=5
- https://news.google.com/rss/articles/CBMigwJBVV95cUxPMWh0QWV4VHZWMnlJSDdLZzJKcmNFWUtGc0U3djZYMF9Wa0ZoQU9PVl9FUFU5bWl2UTN4V05fbDkyN0FmeGo5OVdGbk1MUW0zR3d3VG1iTjE2M0RDNTNKeGV1NXpmbkdXT24zVmp1dm1OcGE4ZEFrdnhNZEpnMVMyc1VDaG91S3JxYVJZVFBvMTFiN2l6VHJjUFMySGFWNVVHc055eU9WZDA0Q2I3SzQ5YnFTUm5HaklPODMyeTU0azVOWEFZbnR5Q3M3b2xLdkdFd1FqRFg0eUFha2JVQmtLMDl4WWlqOHh1cVdzblhGSnJRU2poNEwtMFIyZWNYN1Z5cVg4?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxNeVNuU2V1WFJMVG1qWmkwNUZqQjh5WWk3eFEtcC10ZWhGQU1GNC14bWw3NllTSjZpOVpEVFlybFVsTmd6ZDVaSzlFU3lTdEhfWG5nMklCVXhrOHhKN1ZyRF82NmJkYUVWbHo3Z1N2X0RldDJ4WTZXN3pTd1Iwb2dUZTNzN1hqV0NVVkREZmNhOEpPd1VYemtKOG9xSFhzbzN5YVluZVFKeUtQeUVYQWlQUUEzRmh2bWQzMk5CbTVFMWF4Z0ZURXItWm0taU9nSjYweHE2S2phU0JLbFd6V1E?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOLWc4NXFYcWoxVVljOGZaR2kzVHF2QnY5X2l0eEY4Ri1BWGNhTzlMWWhiM1BLdWtXWnN2QWhabzliQzBSYjI1UFBMV3gxYUlqMnBfTjhqWTBDb0Z0SUFCeTBxdVRvTjBNVEF2ZFVmeWFXSXQyZ0RNbTZpb0dlYmhLT2Yzc2hzam5ENVVzZzJOSC1kWWN3cjI5WTh0Nm1xVWlGSlVsR2NIWQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPa1JvdC0wSGFvVjBwYUYzVlhoX2FHMkdLMUdUUUtibHZhUmJzWkxoT24wQlBjeGZfWGxydF92YnAxN3BDRl9VdkFtTVRiY0tyc1ZjS1RYWE16NUN1X2ZDLW1SRW9vYmdxSmhFMzU5UmdJSV81RE9XOGNIWEYwZFJCMm1OWTFzWS1hckRybm9MVXZLUV9HVTRNZmZRNVdMNDlhVkprUC1DYTBKOHdv?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNRTRBZ2lSU1RSRkx2U2U5eDRld2g4V0dfZlY5QjFhX1JPeVlrM2g3WFIxMnhodldqNFlJZHN5VGNFWWRXX0ZyZVBLdDJVWkVseTNyc3hFYjFLR3dBOS1rVVlQaVdzSkxoMEh4NGJwQVNjdGJaV3lvbjd3aUFhVzFKNFBkd2VDdFl6bGhwSWxGb292WWEzQnkxU3dtOHhjQlJNS2xz?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPUFFsQTg2cVZWZjh5R3RsUk1QbkdWTC1VazlPT25ONmVqZ3EyY3o2LU9Sa1BFN1VJZjRiOGF1bXJIZlNKYjYxX3lZdm5RTjE3aHRJUWMzcHg0UWJSYkxLaWJSTHo5VkllWGN1ZjRwX1NpWlhiOVBqNk9BdDFNWXNhRmU4UDZBQUtJckFHYlBPM3ZWOC1vNjVScVl0QUE2bG5RckpvT1E4Wm0xQQ?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNdWhCeTlBalBJa1lLUlZlX0xlOWFaWUZQS2VTRVFUUEJwbWVrcU85OTVwQXRKRG9ZUldYZjNaZHk0QWN2dWtPblkwdXluTjB5cDFnZjMzMVEyaVZSZG9QVTdvVUFGSFV1Yk1vd09tQ3Y3NTN1RzNpMHBNQUtsZzBOZFpBdDhjeXRQaWw3MTNFX2Y1ZUdkbjZhZFBmYzNuZ1pUSFlhb3laRG50X0IzQm8wM1p2bUtwOHdSSUMxejNSR1FLZlVnbTZQMzVkR0o?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOVnFQVHNkWVBBYzM1bTVkQXBrMHdVbC0xOHdmLXk2Z0Ztb2NmSjRnX1lndE40bTdfNGR6dUx6Y1VGeEkxeTQ1cVRlVm12RWVCUGZUZEFYWEJrMHRkMDBLMzdZYnJLaFdVcXdHMW5TWElSalRwZS1JLWdtdm1BMFZ1cl9BN0tzblJuUDE2U3Jwa2l5ZDNGQTV3aHNhT3Y5QVhDTmY3NzB2YlIzUVVCeGh4eEJRMDI?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOMEdpVWJwSTh1cU9tb25IQWwwR3VjdlNfYWZUYXI5b3lrZzRTb3c3SHBqVy00endjamt2M3RvMFZLcGZRTmRLcTZTOE92ejJqM09vejF6Y29zRy02XzRQeGJ2a2ZKaTVDNE5DeU1YbjJUc3NOM3plT3NJOWZWZ1ZoTm9YZ0JZZkZGMXZwUkNxQ3NnSVhDWDVn?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQeVFFYS1CVFNpYzJZQ2VUM3hMOGFJb2ZnRV9vMzZpYnlXUEZEOTlTZVFwdkg3SGZHekhoRnNKRXlrNU5UeXROQzZHdE5qd2dDcG5pVTFfYnVVa0tPVUkwRUNWQ242R292azd3ckM1dTQwVUF4MlJPNUNNaTRfSG9OQmE2MjUtTmJ5ZWUxVEhYWGw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPN002UnhrTzlCU1BJUk1kd2xHVmhXcXk4Y0hwcHE2ZEk2TkVYT3ZmX2k3OWNFQlJMV2RIR2t1QXc0ek9zMzRwVWU2ZEljQ1ZTZ1VWSnRYM0xxVE40eDVTeUpTRklBSFpzSjhUUDZlWFY1Q0NQcXlvcmZENTBSeWotRGJGM2pOWEZXX2pTaXlhZ3cwT0U?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQY0Vwa0dtbVZjbmlKcW1zeXlsNlZRNFc2YkJTNURRbnJnTWI4aVZTbHZQMWY3UWpJb0FKRjJQOFJSMDFWU0NlVGUtM3NYd2FQTVNycno0U1hDNmp4Tml1OXllS0hVenotUzlDVkxsUThzd3VXUFpyek9uMC1EbjFlOURDZERyZkVEUm40ZGV2RGUzeExVcDN1d1hqMXpfTDUzZ3RyZHNR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
