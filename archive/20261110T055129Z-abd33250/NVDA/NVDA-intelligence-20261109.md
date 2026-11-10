# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T06:11:28.554737+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 5, 'ai': 10, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 12 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-07

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 178.6700 |
| Return 1D (%) | -4.2703 |
| Return 1W (%) | -11.5758 |
| Return 1M (%) | -22.0734 |
| Return YTD (%) | -3.9742 |
| Return 1Y (%) | -4.8110 |
| Annualized volatility (%) | 38.2245 |
| Beta vs SPY | 1.7527 |
| Max drawdown (%) | -25.3177 |
| Sharpe (rf=0) | -0.0879 |
| Downside deviation (rf=0, %) | 27.2221 |
| Sortino (rf=0) | -0.1234 |
| Historical VaR 95% (1D, %) | 4.1471 |
| Historical ES 95% (1D, %) | 5.0101 |
| Correlation vs SPY | 0.6278 |
| Tracking error vs SPY (%) | 31.4873 |
| P/E (trailing) | 22.59 |
| P/B | 18.84 |
| EV/EBITDA | 21.28 |
| Revenue growth (%) | 105.90 |
| Forward P/E (estimate) | 11.22 |
| Gross margin (%) | 74.67 |
| Operating margin (%) | 66.24 |
| Return on equity (%) | 117.21 |
| Free cash flow yield (%) | 0.97 |
| MA50 | 219.0005 |
| Close vs MA50 (%) | -18.4157 |
| MA200 | 204.3481 |
| Close vs MA200 (%) | -12.5659 |
| RSI (14, Wilder) | 27.4062 |
| MACD (12,26) | -9.5666 |
| MACD signal (9) | -5.9351 |
| MACD histogram | -3.6315 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 178.6700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -4.2703 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -11.5758 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -22.0734 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -3.9742 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -4.8110 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 38.2245 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.2221 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.1234 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.1471 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.0101 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6278 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.4873 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.7527 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.3177 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0879 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.2173 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.2370 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.2110 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.9691 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.5879 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 27.4062 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.6315 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -18.4157 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -12.5659 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Nvidia stock sinks 5% as chipmaker investigates CEO Jensen Huang's relationship with alleged Chinese spy
- Summary: Nvidia stock sinks 5% as chipmaker investigates CEO Jensen Huang's relationship with alleged Chinese spy
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7gFBVV95cUxObWVFY2cxQURmMnJ2aWFxSlRfeFJzeGJDOEhxbjVqUWVpMU96Mm4wcFNBVG5BaVdBZUIwYnN3WXNsWEZld000V1ZrMl9SR0pVZFB0a21rTUV1U3NJajhTUTN6bjBmVmtIQmhtRWxyV1dyemhvcDFrT1J5TmItcGJyVmt6VGY0VW9nZVBVZ2RIalNEOUhKRGRybVgtdzBPMkpzRTBicXpTaGw3c29vUXhiR21hVmVlWk10NzgySGJwbV9MSWpLeXVpT2hJT1FqU05XTXlZMGQwS285QlhudnBJdkhrMGlRbVJsX0h5alBn?oc=5>

### Nvidia Is Now Down for the Year After a Sharp Selloff. You Can Buy NVDA Stock Gradually, but Don’t Rush In.
- Summary: Nvidia Is Now Down for the Year After a Sharp Selloff. You Can Buy NVDA Stock Gradually, but Don’t Rush In.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxOdEUzQWhaem5BMHNyZnZoVHNDZV9fdXRBNVQ4T210dV9kUHlBVGlGdklmY08xQVlMcjNGblJ0ZDhSM3FDUmpRQm8tcFhVNXR3OUJWWlNjdEhPNW8zd1I5QjZOdHJqSlFHaDJ4LWd6TXR2c0YtSFFMSWZSMGsxbHNIbU9DUGxvTnVaZXEtdm5ZaDFvNlgwQ0gxZnRhaUtwTTM4MmVoZUNqUWxSVzZ0UDNxaWNkMGEtdzl1a3RRcFZSRzk4OHRCR0dRQVBDTnA1UEc0R2ptOHRMZWJIaUMwSUVFeQ?oc=5>

### Nvidia's stock slides as questions swirl around Jensen Huang's future as CEO
- Summary: Nvidia's stock slides as questions swirl around Jensen Huang's future as CEO
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxOMUZnR09VQTBYd3NTN2NGczJYQU5OOWY0R2wzdW1GQTlmNTk5VTNOc3BZMXRJWG15S1JCYk45by1uNFo5eE5uanhjUkpaclRydk5mUUoxRVJaeGlac1l5b0pEaEdpeGdqU3pBTHdQSmdXOTlONnRDNWRKdXhfRlNmbkFoaFNQdw?oc=5>

### Nvidia stock falls 4% as scrutiny turns to Jensen Huang’s affair with alleged Chinese spy
- Summary: Nvidia stock falls 4% as scrutiny turns to Jensen Huang’s affair with alleged Chinese spy
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPcndzRG1jRHQ5c25nX1RuQVVNeXJUXzNnemotNFRpWGhwUGNCN3hmV2VkMndSVkl4V1hIMmhUMDhjWTJFa1BYckVYM1BkX0ZMMEQ2WmFxRGRhYXFtNzVJQUEtNW9PaUhfekFYM1RWeG0xbldSZlcwVldGZXVXVjNvcDdNN2dReWFqM3c?oc=5>

### Why Nvidia at 13 Times Expected Earnings Still Isn’t Cheap
- Summary: High valuation suggests stock may be overvalued.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPSEhJbGo5Z213RFlZOGstMFRLUW52OVk0NmF1NVl6TlJVbHlzay0tZm4zLVIySnNnSjM2SFduV2psMzk2M1YxVEtSWmpyZ3JCcVQ5MXZFX2ZrdlJkM0t0UDc2a1JvMi03R2xpbVJTeU9PcG5jNTlWVUR3Zi1YVlF6dXhDa2wzM0lOazh5anRyRmlJaTBodFcxUA?oc=5>

### Nvidia stock falls after investigation into CEO, bucking market rally
- Summary: Investigation into CEO causes stock drop, opposing market rally.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE50WjBIUUkwd0ZNMkFYTzZjQjRnOFZoc2lPTFVORzZtU0ZwOV9SNldqdUxPZ0NsUEFLZ3lDdzh3RV9ZTWZ4ek9KaWR4aENKVEFtdFIybjhqUkxvTHRFYWFocVgta1ZKRWJYYTFIZ1JpaE5uTVBfNzMzb3VkUC1iUQ?oc=5>

## CATALYSTS

### Nvidia Stock Is Heavily Discounted. Here’s Why Analysts See 80% Upside.
- Summary: Nvidia Stock Is Heavily Discounted. Here’s Why Analysts See 80% Upside.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQYWVoQTRyTjV4OE5iZ0gyY2NzM1M3STlkWFdhTUJxRE5fZWh2UENxRThXNVltUWpDUFVRMlBLeWxmZTFIRWh1Q2VtaEdQMVBkWVk0VG9RVENkUXRjZTFwUnlUZTBtdDE0Q3pKNVFUUXg0RWU0NXpObWxQT2wtNkd5Sy13ZVJ0bFd3OWhNM1RyQjRRRlc1cDBPS3JXUW1Fck1Pd1E?oc=5>

### Is NVDA stock a buy or sell? Spy alert?
- Summary: Analyst debate on whether to buy or sell NVDA amid spy alert concerns.
- Date: 2026-11-08 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMie0FVX3lxTE9idXM2c01NckxhaUZZUDkzTVg1UTM3VmF1UTQ5anlKblBtVUZienBwR2xicC1EZ2ROaVhVV2k5bkdSR01SZUM4cUU4dEFPbTFwWDRrSTlESXFDR2Q4dG5VeDhKb2Y1TFh0M3k1WkRadXlCYjFiV2hpTFphQQ?oc=5>

### Asian stocks face new pressure as Nvidia spy probe rattles tech sector (NVDA:NASDAQ)
- Summary: Reports of a spy probe into Nvidia create market pressure on tech stocks, including NVDA.
- Date: 2026-11-08 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxOcEFxSEFid1djemktcFlja1EyNW5PZkl5cHd1d1VySUdtWEF1bGFXdk5SSzIyd2x3bTEyX1A0REZ3YXNxNldtNjlLN3VwcHBMbVl2bjNIQ3FBd1RkNlF5a3pRaXllSFA5OWRCb2k1MG40VGh5THo0RGp3WVp5Z0tBMzdEaC1jSzZQTUlsblRnVjdmUHNWdmJwd0NJWmNycndNQjdkNUp3SnItcUV1?oc=5>

### A massive trade in Nvidia just went off – here are the details
- Summary: Details of a large Nvidia trade that just executed.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOcTZiNlRvdFdDOEZEcWtaQV9NZU94U1A0RU9qZXVXV3MtbDZtcmxlQ01oS1ZhVEpZQmVvcGx5N212aFIxM215UEZiRjBzeGpQUkc2aThiSVY4M0J1NE5ra0NIcDBxY3JieTlfdUVhZlJnSC03Z1huWmF0ZUdlUjhGQmVDYk1lTjduMkJNVjZzd0EzdzRzbWdzYmpocThuZw?oc=5>

## RISKS

### Nvidia (NVDA) Stock: Near $180 Monday as the Board Opens an Independent Probe, Bull $194, Bear $172
- Summary: Board initiates independent probe into Nvidia, potentially impacting investor confidence and stock valuation.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQV0dOa2t0SEpQc2tqM2pXOXBkeWZTUHBiT1lEVk5jQmpRWVlKeVpPMHA2TVFqRDFJWkNUb3NBempZZnFJZ2FwZ0FGMTducDBTZ2h3MmJZVXQ5WTloSmtySkJiRXZXWTA2eXhZNVVFUUszUk9CNmJjOFFLTjB0cXhmcW52LU5LV2Y2RjRTUFpRZW5GR2JBNmk5NGlNU2JpdkZTUmN6NWs5ZTJyQUhiTmJWQXNyM0FhRldTbXB1VE9FaXQzOHJFQ1Bv?oc=5>

### Nvidia Stock (NVDA) Falls on Probe into CEO’s Affair; Here’s Why Baird Stays Bullish
- Summary: A probe into CEO’s affair has caused NVDA shares to drop, raising concerns about governance and potential legal ramifications, though some analysts remain bullish.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNWUFVU2lWYVlHMUFDTVF5aEtzTlh3clZ6ZEwtNzVKSU4yQ3JzRlIzZmVoUk5IdnBNaVJpVlQxUHlKcXotTnhycjV4Rm55TmV0RXNTcF85bnh4aXV1Z2thcUFTVThRV2kxX0VOWW9NbEx2NWM2MV85MUYtUDZRNWlzTF8tR2JtRjJ0SFZWV0hkWGo3elVHUWdZaHZucDhabnVvbFdfOUNFV0s4dlpfdWc?oc=5>

### Why Ousting Nvidia’s CEO May Be Worse Than the Scandal Itself
- Summary: CEO ousting could destabilize Nvidia, worsening scandal.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE1HRXFMT2pzMTR2MGUybjNiVm5aYUhrX0VPZGxUVmMteGIzNmFNZHgzNDRRMHFfb1pNSmxLT1d2a1dPSHlaTGpFdG84c0x4N2FMY2NtYk92M1hZLV9jQi1kQVJIM29rM0pOeFRwUTJCelpHNGpSck55UkZMUld2QQ?oc=5>

### Jensen Huang affair puts Nvidia's future at risk, with no clear successor to the renowned CEO
- Summary: Jensen Huang's affair threatens Nvidia's future, no successor.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE5EcnlNdzFRY2RtTFNiaVYxeFhDSnJIck5qckxaeE4wLVRVYWFFSkZoc2tJNjRmLWxXSGxQMXFuYi1YeHpYbGNjOW5CMy1rNHNTaDlCWEpfUEpvYkprUEVkZjBJTTl6SmZRLWtNd1B3czh3ckl2ejlYcHFUN1FUODQ?oc=5>

### Nvidia CEO Jensen Huang's affair with a reported Chinese spy damages this key investing factor
- Summary: CEO's alleged affair with a Chinese spy raises security concerns, potentially harming investor confidence and NVIDIA's reputation.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxPNHlSbFpNZW04Q2dTTTZOdFlHcmxmdk1BTDN3c1d3SWtaVTlldnI4Rllab0dlYW5xT25JVEI0WkYxN0FOU2doV3VuTEh3d1JaZVVIZUw5ZGNYbVAtRDRYck1YQWhKVGRGbXk3ZDZaNXJRQXdtaVZBUktpbEtDUDltRy1HZWU4aVRfaGota2pCMTBUd1lURVYyQVlfWDE4LWx4bTFWdTFEaVJpcXo2U2pGXzFVOEM2WVlmWGZJRXE5SEl2bl93SVpsMWprUEdZM3h0ZlJVd2t0RUtSbTBfeEpjaEJnNWViUVNG?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **22.59** | **18.84** | **21.28** | **105.90** | **4,314,344,194,048.00 USD** | **-4.81** |
| AMD | 108.67 | 12.20 | 74.27 | 44.70 | 834,115,600,384.00 USD | 117.77 |
| AVGO | 40.80 | 15.30 | 29.86 | 85.50 | 1,525,079,343,104.00 USD | -7.89 |
| INTC | N/A | 2.74 | 17.16 | 20.90 | 315,551,547,392.00 USD | 55.70 |

Peers fetched as_of: 2026-11-09; NVDA reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-26
- Revenue (latest available single quarter): 96,221,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- Net income (latest available single quarter): 59,688,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi7gFBVV95cUxObWVFY2cxQURmMnJ2aWFxSlRfeFJzeGJDOEhxbjVqUWVpMU96Mm4wcFNBVG5BaVdBZUIwYnN3WXNsWEZld000V1ZrMl9SR0pVZFB0a21rTUV1U3NJajhTUTN6bjBmVmtIQmhtRWxyV1dyemhvcDFrT1J5TmItcGJyVmt6VGY0VW9nZVBVZ2RIalNEOUhKRGRybVgtdzBPMkpzRTBicXpTaGw3c29vUXhiR21hVmVlWk10NzgySGJwbV9MSWpLeXVpT2hJT1FqU05XTXlZMGQwS285QlhudnBJdkhrMGlRbVJsX0h5alBn?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxOdEUzQWhaem5BMHNyZnZoVHNDZV9fdXRBNVQ4T210dV9kUHlBVGlGdklmY08xQVlMcjNGblJ0ZDhSM3FDUmpRQm8tcFhVNXR3OUJWWlNjdEhPNW8zd1I5QjZOdHJqSlFHaDJ4LWd6TXR2c0YtSFFMSWZSMGsxbHNIbU9DUGxvTnVaZXEtdm5ZaDFvNlgwQ0gxZnRhaUtwTTM4MmVoZUNqUWxSVzZ0UDNxaWNkMGEtdzl1a3RRcFZSRzk4OHRCR0dRQVBDTnA1UEc0R2ptOHRMZWJIaUMwSUVFeQ?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxOMUZnR09VQTBYd3NTN2NGczJYQU5OOWY0R2wzdW1GQTlmNTk5VTNOc3BZMXRJWG15S1JCYk45by1uNFo5eE5uanhjUkpaclRydk5mUUoxRVJaeGlac1l5b0pEaEdpeGdqU3pBTHdQSmdXOTlONnRDNWRKdXhfRlNmbkFoaFNQdw?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPcndzRG1jRHQ5c25nX1RuQVVNeXJUXzNnemotNFRpWGhwUGNCN3hmV2VkMndSVkl4V1hIMmhUMDhjWTJFa1BYckVYM1BkX0ZMMEQ2WmFxRGRhYXFtNzVJQUEtNW9PaUhfekFYM1RWeG0xbldSZlcwVldGZXVXVjNvcDdNN2dReWFqM3c?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPSEhJbGo5Z213RFlZOGstMFRLUW52OVk0NmF1NVl6TlJVbHlzay0tZm4zLVIySnNnSjM2SFduV2psMzk2M1YxVEtSWmpyZ3JCcVQ5MXZFX2ZrdlJkM0t0UDc2a1JvMi03R2xpbVJTeU9PcG5jNTlWVUR3Zi1YVlF6dXhDa2wzM0lOazh5anRyRmlJaTBodFcxUA?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE50WjBIUUkwd0ZNMkFYTzZjQjRnOFZoc2lPTFVORzZtU0ZwOV9SNldqdUxPZ0NsUEFLZ3lDdzh3RV9ZTWZ4ek9KaWR4aENKVEFtdFIybjhqUkxvTHRFYWFocVgta1ZKRWJYYTFIZ1JpaE5uTVBfNzMzb3VkUC1iUQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQYWVoQTRyTjV4OE5iZ0gyY2NzM1M3STlkWFdhTUJxRE5fZWh2UENxRThXNVltUWpDUFVRMlBLeWxmZTFIRWh1Q2VtaEdQMVBkWVk0VG9RVENkUXRjZTFwUnlUZTBtdDE0Q3pKNVFUUXg0RWU0NXpObWxQT2wtNkd5Sy13ZVJ0bFd3OWhNM1RyQjRRRlc1cDBPS3JXUW1Fck1Pd1E?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTE9idXM2c01NckxhaUZZUDkzTVg1UTM3VmF1UTQ5anlKblBtVUZienBwR2xicC1EZ2ROaVhVV2k5bkdSR01SZUM4cUU4dEFPbTFwWDRrSTlESXFDR2Q4dG5VeDhKb2Y1TFh0M3k1WkRadXlCYjFiV2hpTFphQQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxOcEFxSEFid1djemktcFlja1EyNW5PZkl5cHd1d1VySUdtWEF1bGFXdk5SSzIyd2x3bTEyX1A0REZ3YXNxNldtNjlLN3VwcHBMbVl2bjNIQ3FBd1RkNlF5a3pRaXllSFA5OWRCb2k1MG40VGh5THo0RGp3WVp5Z0tBMzdEaC1jSzZQTUlsblRnVjdmUHNWdmJwd0NJWmNycndNQjdkNUp3SnItcUV1?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOcTZiNlRvdFdDOEZEcWtaQV9NZU94U1A0RU9qZXVXV3MtbDZtcmxlQ01oS1ZhVEpZQmVvcGx5N212aFIxM215UEZiRjBzeGpQUkc2aThiSVY4M0J1NE5ra0NIcDBxY3JieTlfdUVhZlJnSC03Z1huWmF0ZUdlUjhGQmVDYk1lTjduMkJNVjZzd0EzdzRzbWdzYmpocThuZw?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQV0dOa2t0SEpQc2tqM2pXOXBkeWZTUHBiT1lEVk5jQmpRWVlKeVpPMHA2TVFqRDFJWkNUb3NBempZZnFJZ2FwZ0FGMTducDBTZ2h3MmJZVXQ5WTloSmtySkJiRXZXWTA2eXhZNVVFUUszUk9CNmJjOFFLTjB0cXhmcW52LU5LV2Y2RjRTUFpRZW5GR2JBNmk5NGlNU2JpdkZTUmN6NWs5ZTJyQUhiTmJWQXNyM0FhRldTbXB1VE9FaXQzOHJFQ1Bv?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNWUFVU2lWYVlHMUFDTVF5aEtzTlh3clZ6ZEwtNzVKSU4yQ3JzRlIzZmVoUk5IdnBNaVJpVlQxUHlKcXotTnhycjV4Rm55TmV0RXNTcF85bnh4aXV1Z2thcUFTVThRV2kxX0VOWW9NbEx2NWM2MV85MUYtUDZRNWlzTF8tR2JtRjJ0SFZWV0hkWGo3elVHUWdZaHZucDhabnVvbFdfOUNFV0s4dlpfdWc?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE1HRXFMT2pzMTR2MGUybjNiVm5aYUhrX0VPZGxUVmMteGIzNmFNZHgzNDRRMHFfb1pNSmxLT1d2a1dPSHlaTGpFdG84c0x4N2FMY2NtYk92M1hZLV9jQi1kQVJIM29rM0pOeFRwUTJCelpHNGpSck55UkZMUld2QQ?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE5EcnlNdzFRY2RtTFNiaVYxeFhDSnJIck5qckxaeE4wLVRVYWFFSkZoc2tJNjRmLWxXSGxQMXFuYi1YeHpYbGNjOW5CMy1rNHNTaDlCWEpfUEpvYkprUEVkZjBJTTl6SmZRLWtNd1B3czh3ckl2ejlYcHFUN1FUODQ?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxPNHlSbFpNZW04Q2dTTTZOdFlHcmxmdk1BTDN3c1d3SWtaVTlldnI4Rllab0dlYW5xT25JVEI0WkYxN0FOU2doV3VuTEh3d1JaZVVIZUw5ZGNYbVAtRDRYck1YQWhKVGRGbXk3ZDZaNXJRQXdtaVZBUktpbEtDUDltRy1HZWU4aVRfaGota2pCMTBUd1lURVYyQVlfWDE4LWx4bTFWdTFEaVJpcXo2U2pGXzFVOEM2WVlmWGZJRXE5SEl2bl93SVpsMWprUEdZM3h0ZlJVd2t0RUtSbTBfeEpjaEJnNWViUVNG?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
