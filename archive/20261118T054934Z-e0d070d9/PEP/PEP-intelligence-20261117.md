# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:00:55.491139+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 5, 'ai': 7, 'unknown': 0, 'irrelevant': 12})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 14 named publishers; 0 exact duplicates; 24 HTTPS source links; largest publisher share 16.67%; oldest publication 2026-11-11

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 142.0200 |
| Return 1D (%) | -3.0117 |
| Return 1W (%) | -1.1072 |
| Return 1M (%) | 8.0082 |
| Return YTD (%) | 1.9671 |
| Return 1Y (%) | -0.0375 |
| Annualized volatility (%) | 21.8860 |
| Beta vs SPY | -0.1759 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | 0.1069 |
| Downside deviation (rf=0, %) | 14.6570 |
| Sortino (rf=0) | 0.1597 |
| Historical VaR 95% (1D, %) | 2.2237 |
| Historical ES 95% (1D, %) | 2.7033 |
| Correlation vs SPY | -0.1108 |
| Tracking error vs SPY (%) | 27.1243 |
| P/E (trailing) | 18.42 |
| P/B | 8.69 |
| EV/EBITDA | 12.23 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 16.49 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.05 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.67 |
| MA50 | 133.8852 |
| Close vs MA50 (%) | 6.0760 |
| MA200 | 143.6359 |
| Close vs MA200 (%) | -1.1250 |
| RSI (14, Wilder) | 56.7755 |
| MACD (12,26) | 3.1940 |
| MACD signal (9) | 2.8771 |
| MACD histogram | 0.3168 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 142.0200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.0117 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.1072 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 8.0082 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 1.9671 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -0.0375 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.8860 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.6570 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1597 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.2237 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7033 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1108 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 27.1243 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1759 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1069 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.4866 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.0460 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.6731 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.4202 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.7755 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3168 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.0760 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.1250 -> Slightly below the moving-average trend level.

## TAILWINDS

### PepsiCo (NASDAQ:PEP) Stock Jumps 2.2% - Here's What Happened
- Summary: PepsiCo (NASDAQ:PEP) Stock Jumps 2.2% - Here's What Happened
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPdkNQWXlFTFF4UlZya3BZMUpMdDBhYUVPeHEzd0RGU1hpOEtIcTBMc2t2MHVqU3ZnYmRINkI4Ujh6ZjZUTDRfczZCUEVlQ3d1NGY2TUs4bGdfT2xiSEdqbS1ta0dfSEdtMHZFVHVRVC1oWVhFVmRlMUdXSGF0NHlodzdnbndQbEVqc29oaTg2NXA4T1NvTTM1ZDhrdnZYSEtDT2NzN0Jac1ZoSk05QllDd1Vkaw?oc=5>

### What's Fueling PepsiCo (NASDAQ:PEP) Growth Across Global Markets?
- Summary: PepsiCo's growth driven by global market expansion and product diversification.
- Date: 2026-11-14 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOUVFxdGl2XzVLY1NGejhRUG9nYl80bFM4RjZDUU1GMkxDOGljNzNuVnJkLXVmQVFVckJ1V0kzNFI4MnFGVloxSlh0SkxmSGdaTFkweUFmelJRbUYxU2JXa09UTzR2ZmkwY1FpLW1Ibm01MVhxc3BHMEZGUUtIYkV1T29pbEJnN2FwMmJNOXBLSVl6V0t1YlhtSmVvdk85NWJjSzhXME1nYw?oc=5>

### PepsiCo Analysis - Is PEP About to Break Out? - PepsiCo (NASDAQ:PEP)
- Summary: Potential positive price breakout indicated.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNelFianZTb3o2VFNiNVZNaTVWRThFQ2g0dldQSGI4bWM2UUhDb2ZrQ05TSm1ndm9JSHZFYlZLVnBiVDJacHNSTFk2cWFJT3hQZVNmNnptSHhmTWE3QThmbFFSLTBJelZPSnpSVjhxV2d4WWJQVmVhdmRVVkdUcXRyREFUSW9DRW41aDZUT2tVV05LS05idDBjOE14S2E0dkxWblZVZlB2bThOSlpHMlE?oc=5>

## HEADWINDS

### PepsiCo Stock Drops 2.4% in 6 Months: Is More Downside Ahead?
- Summary: PepsiCo Stock Drops 2.4% in 6 Months: Is More Downside Ahead?
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQTGxPZHJlX29nNVVYSmZzUlNmaXBSOVBDd0RyOXZ1ZmMtX040ZzR5VDNDTWp4YWVJaTEyazFkZmsxN2MtOEtMdW9kWVV6UW5vckFxUzlVM3pNVGRxTi1iekVUbnZ0LWVuazY2SmFlZVRPWGF0RVdBak45WlQzLW9lbEx0V0JxY3FKN2ctbFI4TS16QQ?oc=5>

### PepsiCo (NASDAQ:PEP) Stock Price Down 1.2% - Here's Why
- Summary: PepsiCo (NASDAQ:PEP) Stock Price Down 1.2% - Here's Why
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQekl6NkVNTlBJZkNyLTNrOXEtV1dCOEo3OVhoc3JfcGYxRjNJTEYzaFlMa0RtLUZ5eXVlOGIwQkZydlpUbERha29QS09pZnpDNU1YZVBkX2c0OTZNMUs4MFgwY0U4T0xZOW1Xa1Vxclh3U1RrcExfckNZWUpJR2ZvUXViLWRjMnZQU3NTbEdFZVQwbDlBMWg2T3dRbk9Kamg3N3lERzNqcGZVOTlR?oc=5>

### PEP Stock Slides As Bernstein Downgrades PepsiCo, Warns Of Earnings Shortfall
- Summary: PEP Stock Slides As Bernstein Downgrades PepsiCo, Warns Of Earnings Shortfall
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8AFBVV95cUxNRVI2RjRxQnBRUGtlcTY3MXZ0UDhYSDBSTnY3OHlGeVJNZG9paFBOQlZvRldnLXhZWlpOcUpJdUYxak9hTHNVMnIyTmNVX05UX1BjQllrQmtHcTlUblVqdllJbDFmN2VmakVFZVF2Y21VRWZmamRya2ZMSF85REZNTWhlQm0xVU1fNU9qX3BpZUl0NTBvRXNkY00wbjJnbjZPRW90NHpFUlNSMU9IYXltSlhlb2JuQWNONDBLaEhBQ0RWOE9FeTIwUWVENEdRVmgydzhOQ2k3THBRRFEwRlN6a1JBMDJyVDM2QlNZYjFGYms?oc=5>

### Will PepsiCo stock avoid deeper losses amid seller dominance and oversold signals?
- Summary: Possible deeper losses due to seller dominance and oversold signals.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOY0RZb0JuMTFtRDk1dnJrb00yYmJwb25BUXc0OGtCOGJ2MEhwX3JJZlAzZlNxaGpfQUJtekdJUW5kZTA4MHU3ZWU2V1htaW9ZczdNOHZ3eURKQUV0bS02aHFPeXlXVHJ2XzI5S2VJVHBVbGgwZWluRzZKMkpCZC0ydFFQcFZ4VGpUUnpIcDE1NGt4RjA?oc=5>

### Which Dates Could Move PepsiCo Stock Most?
- Summary: Specific dates may trigger significant stock movement.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNY0FSbUIzWkFrQjhpOVlXdXNjU2hmb1k0b2pkSDFkb1ZBcks3V0lMZ00xOWJlNFpFWUJLZmNTUlhVTGNxd0ttUHpXNWg4LUtyR3JmeWJUaklrMC1Mb2ZtelF6akpQNE04RWVEMFJiTUtybW5BZmFKRmtuUXNIVHczNHg1T0U3c05nQ3hlckhfMGF1ZjlmSnFQbWNlQ1djUDMxU05J?oc=5>

## CATALYSTS

### PepsiCo Stock And Other Dividend Names Worth Watching As Rate Hike Risks Return
- Summary: PepsiCo Stock And Other Dividend Names Worth Watching As Rate Hike Risks Return
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxPRmhNV2g2eE44SW5VOGc3Zi00NHIxdE4yYW81LVJoM3lzcDY1Rk5zTTJYRXZFVUgzZEtfZXJzYnppeGhnbndNd2RYUmhRSldHNkl1NDdEeFo5Y3A1cTlzN3AtZU9neG12dHNIdEtiZU9hZUx2TkxYRVpxQzRieUJuWXRsRmRsQ015akwxUzZSSTI1ckJfbkxncjM3U1UxUWJTd3kyeTluODFlY1F5aTdSWHlYVGdXendzbHpILWdjNFFxbzFWQXlGeTlQMUUtRzg4NWRtc9IB2gFBVV95cUxPMFpnblNGQzlEa25xWU0xNTNFLWVLVDlOYjVVZ2c3dkNyY1B5QjNaNm1CalpBSXJFU1FMVDFvaEUyNkFDckxfYjh2bHFuT3pYMjkycmx5N0ZXWVNEWC1vWmZRZ1FwMlk1Q0hlRms4MGZvOVpzdk5pTGdEQ0txc0xYVjBuQVQ3d19MWnozcHBKTHBLLUxtYVAza3pqUWdET05PTnlxRUNzTUhrcWt3M29yU2o0bk9CVm9lY1ZpU1QxY1F0Tm05czhkZHo3MUZ1c0g3bjJhd1ZHUlFvZw?oc=5>

### PepsiCo (PEP) Cuts 1,000 Jobs, Is The Stock A Bargain?
- Summary: Job cuts could signal cost-cutting but may impact morale.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxOd1NlejQ3S3lTcnUyN2JrUm5YcUJxNldEZjQ4RHZFb0tZa1dPY1JwSU8wZzc1Zi0wRVFuSjNlS2NxTWE2b0hQUXVlcy1fNTdENWZPaDJYTTR2QWVFQnQ2eEpTRzJtbm9SV21SSUE1N0VCeFY5QzRmX1o5Mm0yQ1l5RjR4ZWh1d250R1RCMUhPdFp6TGFHcUhNbUIzMTV3MkRWcW1fUnlGME9GUmFTY2xfVzcyaHBuTUswSGdhX3J1Nk8tMGI2ZHfSAcsBQVVfeXFMT01IRERycWtBX1FPYW5mLXIzZVd5aHpPWjQyR2t0Zko5czBfbjFXVVNvMFdYS2hWTERtSWN0NVJyM2NDTDhIRnRLYWRxTzFWMXhwODlTNUUya1k2NGVtVXVlQU1paXo4Tzd4VTl4SVh0UE5mb0VNSjdiVDlBa3htM2xJbTBxX0FBUll6ZkJ2ZklmZHppTXMxSEZOTUpRMHZrSFRqeTVZa3QyMlFzcm51Y3BIQlBwWGJOeEVCQ1FFM0NSdVJLSmhSQ0ptRFk?oc=5>

### PepsiCo (PEP) Stock Could Be Below Fair Value On Cash Flow
- Summary: Stock may be undervalued based on cash flow analysis.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxQa1FBd3lLTDU1OE1vQzByRlphSWJZY05HS1ptZGpfZEgyMVJMQlVTMUt3LUVvWjRTYXpIbWUzMEdSN3BqUjJVdjBOb0J4X1ByMHpaZWxrX041NVFRalVPMnNvUXFoOG1qV1k2NXVPc1BubFRLcElDUGROTUdreldNSm5OOHd4anhIaGZKSmU3ZWZGUkc5TmZtWkpad3psdmZLMWRua3pFYTBnUzV0Uy0wUGo4Y2pEcGk0TzBmaWI5am53NENacFJHaGYtdFd3ZE3SAdQBQVVfeXFMT1BUY2dJbXFWeXBrbWIxV3Rlb0o2SWFtRkhYRGx2Y21rc2tGU3l2S1ZmVEpfaW0tb0QyLXdpSFdfdkpKWnU3UjlEMTZ3TkFiT2NRM19CVHlCa2dMRmlrQ2JMQ0tGbVVvYkRiaUpLZDh0UWxpWVlnblhhdTBfeEV4NXdPc1FHQUxZV2dtXzVURWpOcjJIY01jQkxHRUpmZmw0QzlWdk8xb2Z0bkFma3lNOWZySnFzZ2sxMEhhWkxRUlRZV2ZnZHVFeVh4UWx2VnE5el9qOEY?oc=5>

## RISKS

### Can PepsiCo's Asia Pacific Foods Business Maintain Volume Growth?
- Summary: Uncertainty over maintaining volume growth in Asia Pacific Foods.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxQaENDLVpqUV8waHZFRWd3eEVLUzBFd3ZncGxSYVBVeldGSkdLUGhmcjdJSGFOS09lX0xsUEM4bHRkR1p0em9XMXFoYmxzWGdZbDNteHphWmNTNzZwX0hQOXFDZ3VBdUxQRG5xcWtlQTJndnpuTDJvWF94Y3Byd243T2xPMlk1VHUyUkswS2RSUG9OcExmM2tKY19IcmJoVTc0Z3FFWm9STVl1MzExdVA2amZHbmpXRnZ0MEJIQQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **18.42** | **8.69** | **12.23** | **5.60** | **193,536,491,520.00 USD** | **-0.04** |
| KO | 29.14 | 11.37 | 25.97 | 7.40 | 424,984,936,448.00 USD | 43.49 |
| MNST | 40.40 | 8.84 | 27.99 | 16.70 | 86,991,831,040.00 USD | 23.72 |
| KDP | 31.34 | 1.86 | 16.24 | 70.60 | 47,347,392,512.00 USD | 33.15 |

Peers fetched as_of: 2026-11-17; PEP reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

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

- https://news.google.com/rss/articles/CBMiswFBVV95cUxPdkNQWXlFTFF4UlZya3BZMUpMdDBhYUVPeHEzd0RGU1hpOEtIcTBMc2t2MHVqU3ZnYmRINkI4Ujh6ZjZUTDRfczZCUEVlQ3d1NGY2TUs4bGdfT2xiSEdqbS1ta0dfSEdtMHZFVHVRVC1oWVhFVmRlMUdXSGF0NHlodzdnbndQbEVqc29oaTg2NXA4T1NvTTM1ZDhrdnZYSEtDT2NzN0Jac1ZoSk05QllDd1Vkaw?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOUVFxdGl2XzVLY1NGejhRUG9nYl80bFM4RjZDUU1GMkxDOGljNzNuVnJkLXVmQVFVckJ1V0kzNFI4MnFGVloxSlh0SkxmSGdaTFkweUFmelJRbUYxU2JXa09UTzR2ZmkwY1FpLW1Ibm01MVhxc3BHMEZGUUtIYkV1T29pbEJnN2FwMmJNOXBLSVl6V0t1YlhtSmVvdk85NWJjSzhXME1nYw?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNelFianZTb3o2VFNiNVZNaTVWRThFQ2g0dldQSGI4bWM2UUhDb2ZrQ05TSm1ndm9JSHZFYlZLVnBiVDJacHNSTFk2cWFJT3hQZVNmNnptSHhmTWE3QThmbFFSLTBJelZPSnpSVjhxV2d4WWJQVmVhdmRVVkdUcXRyREFUSW9DRW41aDZUT2tVV05LS05idDBjOE14S2E0dkxWblZVZlB2bThOSlpHMlE?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQTGxPZHJlX29nNVVYSmZzUlNmaXBSOVBDd0RyOXZ1ZmMtX040ZzR5VDNDTWp4YWVJaTEyazFkZmsxN2MtOEtMdW9kWVV6UW5vckFxUzlVM3pNVGRxTi1iekVUbnZ0LWVuazY2SmFlZVRPWGF0RVdBak45WlQzLW9lbEx0V0JxY3FKN2ctbFI4TS16QQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQekl6NkVNTlBJZkNyLTNrOXEtV1dCOEo3OVhoc3JfcGYxRjNJTEYzaFlMa0RtLUZ5eXVlOGIwQkZydlpUbERha29QS09pZnpDNU1YZVBkX2c0OTZNMUs4MFgwY0U4T0xZOW1Xa1Vxclh3U1RrcExfckNZWUpJR2ZvUXViLWRjMnZQU3NTbEdFZVQwbDlBMWg2T3dRbk9Kamg3N3lERzNqcGZVOTlR?oc=5
- https://news.google.com/rss/articles/CBMi8AFBVV95cUxNRVI2RjRxQnBRUGtlcTY3MXZ0UDhYSDBSTnY3OHlGeVJNZG9paFBOQlZvRldnLXhZWlpOcUpJdUYxak9hTHNVMnIyTmNVX05UX1BjQllrQmtHcTlUblVqdllJbDFmN2VmakVFZVF2Y21VRWZmamRya2ZMSF85REZNTWhlQm0xVU1fNU9qX3BpZUl0NTBvRXNkY00wbjJnbjZPRW90NHpFUlNSMU9IYXltSlhlb2JuQWNONDBLaEhBQ0RWOE9FeTIwUWVENEdRVmgydzhOQ2k3THBRRFEwRlN6a1JBMDJyVDM2QlNZYjFGYms?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOY0RZb0JuMTFtRDk1dnJrb00yYmJwb25BUXc0OGtCOGJ2MEhwX3JJZlAzZlNxaGpfQUJtekdJUW5kZTA4MHU3ZWU2V1htaW9ZczdNOHZ3eURKQUV0bS02aHFPeXlXVHJ2XzI5S2VJVHBVbGgwZWluRzZKMkpCZC0ydFFQcFZ4VGpUUnpIcDE1NGt4RjA?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNY0FSbUIzWkFrQjhpOVlXdXNjU2hmb1k0b2pkSDFkb1ZBcks3V0lMZ00xOWJlNFpFWUJLZmNTUlhVTGNxd0ttUHpXNWg4LUtyR3JmeWJUaklrMC1Mb2ZtelF6akpQNE04RWVEMFJiTUtybW5BZmFKRmtuUXNIVHczNHg1T0U3c05nQ3hlckhfMGF1ZjlmSnFQbWNlQ1djUDMxU05J?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxPRmhNV2g2eE44SW5VOGc3Zi00NHIxdE4yYW81LVJoM3lzcDY1Rk5zTTJYRXZFVUgzZEtfZXJzYnppeGhnbndNd2RYUmhRSldHNkl1NDdEeFo5Y3A1cTlzN3AtZU9neG12dHNIdEtiZU9hZUx2TkxYRVpxQzRieUJuWXRsRmRsQ015akwxUzZSSTI1ckJfbkxncjM3U1UxUWJTd3kyeTluODFlY1F5aTdSWHlYVGdXendzbHpILWdjNFFxbzFWQXlGeTlQMUUtRzg4NWRtc9IB2gFBVV95cUxPMFpnblNGQzlEa25xWU0xNTNFLWVLVDlOYjVVZ2c3dkNyY1B5QjNaNm1CalpBSXJFU1FMVDFvaEUyNkFDckxfYjh2bHFuT3pYMjkycmx5N0ZXWVNEWC1vWmZRZ1FwMlk1Q0hlRms4MGZvOVpzdk5pTGdEQ0txc0xYVjBuQVQ3d19MWnozcHBKTHBLLUxtYVAza3pqUWdET05PTnlxRUNzTUhrcWt3M29yU2o0bk9CVm9lY1ZpU1QxY1F0Tm05czhkZHo3MUZ1c0g3bjJhd1ZHUlFvZw?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOd1NlejQ3S3lTcnUyN2JrUm5YcUJxNldEZjQ4RHZFb0tZa1dPY1JwSU8wZzc1Zi0wRVFuSjNlS2NxTWE2b0hQUXVlcy1fNTdENWZPaDJYTTR2QWVFQnQ2eEpTRzJtbm9SV21SSUE1N0VCeFY5QzRmX1o5Mm0yQ1l5RjR4ZWh1d250R1RCMUhPdFp6TGFHcUhNbUIzMTV3MkRWcW1fUnlGME9GUmFTY2xfVzcyaHBuTUswSGdhX3J1Nk8tMGI2ZHfSAcsBQVVfeXFMT01IRERycWtBX1FPYW5mLXIzZVd5aHpPWjQyR2t0Zko5czBfbjFXVVNvMFdYS2hWTERtSWN0NVJyM2NDTDhIRnRLYWRxTzFWMXhwODlTNUUya1k2NGVtVXVlQU1paXo4Tzd4VTl4SVh0UE5mb0VNSjdiVDlBa3htM2xJbTBxX0FBUll6ZkJ2ZklmZHppTXMxSEZOTUpRMHZrSFRqeTVZa3QyMlFzcm51Y3BIQlBwWGJOeEVCQ1FFM0NSdVJLSmhSQ0ptRFk?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxQa1FBd3lLTDU1OE1vQzByRlphSWJZY05HS1ptZGpfZEgyMVJMQlVTMUt3LUVvWjRTYXpIbWUzMEdSN3BqUjJVdjBOb0J4X1ByMHpaZWxrX041NVFRalVPMnNvUXFoOG1qV1k2NXVPc1BubFRLcElDUGROTUdreldNSm5OOHd4anhIaGZKSmU3ZWZGUkc5TmZtWkpad3psdmZLMWRua3pFYTBnUzV0Uy0wUGo4Y2pEcGk0TzBmaWI5am53NENacFJHaGYtdFd3ZE3SAdQBQVVfeXFMT1BUY2dJbXFWeXBrbWIxV3Rlb0o2SWFtRkhYRGx2Y21rc2tGU3l2S1ZmVEpfaW0tb0QyLXdpSFdfdkpKWnU3UjlEMTZ3TkFiT2NRM19CVHlCa2dMRmlrQ2JMQ0tGbVVvYkRiaUpLZDh0UWxpWVlnblhhdTBfeEV4NXdPc1FHQUxZV2dtXzVURWpOcjJIY01jQkxHRUpmZmw0QzlWdk8xb2Z0bkFma3lNOWZySnFzZ2sxMEhhWkxRUlRZV2ZnZHVFeVh4UWx2VnE5el9qOEY?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxQaENDLVpqUV8waHZFRWd3eEVLUzBFd3ZncGxSYVBVeldGSkdLUGhmcjdJSGFOS09lX0xsUEM4bHRkR1p0em9XMXFoYmxzWGdZbDNteHphWmNTNzZwX0hQOXFDZ3VBdUxQRG5xcWtlQTJndnpuTDJvWF94Y3Byd243T2xPMlk1VHUyUkswS2RSUG9OcExmM2tKY19IcmJoVTc0Z3FFWm9STVl1MzExdVA2amZHbmpXRnZ0MEJIQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
