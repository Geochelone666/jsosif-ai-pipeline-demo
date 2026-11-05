# EW Intelligence Report

- ticker: **EW**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/EW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/EW/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:08:27.603719+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 3, 'ai': 7, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/EW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 7 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 27.27%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 99.3700 |
| Return 1D (%) | 4.3912 |
| Return 1W (%) | 8.2698 |
| Return 1M (%) | 16.6999 |
| Return YTD (%) | 16.5631 |
| Return 1Y (%) | 18.0868 |
| Annualized volatility (%) | 25.4705 |
| Beta vs SPY | 0.6148 |
| Max drawdown (%) | -13.1855 |
| Sharpe (rf=0) | 0.7821 |
| Downside deviation (rf=0, %) | 16.9476 |
| Sortino (rf=0) | 1.1754 |
| Historical VaR 95% (1D, %) | 2.5317 |
| Historical ES 95% (1D, %) | 3.1155 |
| Correlation vs SPY | 0.3099 |
| Tracking error vs SPY (%) | 24.7163 |
| P/E (trailing) | 56.78 |
| P/B | 5.40 |
| EV/EBITDA | 26.96 |
| Revenue growth (%) | 13.60 |
| Forward P/E (estimate) | 29.38 |
| Gross margin (%) | 77.84 |
| Operating margin (%) | 29.84 |
| Return on equity (%) | 9.18 |
| Free cash flow yield (%) | 2.15 |
| MA50 | 88.4760 |
| Close vs MA50 (%) | 12.3129 |
| MA200 | 85.6050 |
| Close vs MA200 (%) | 16.0797 |
| RSI (14, Wilder) | 73.4042 |
| MACD (12,26) | 2.2441 |
| MACD signal (9) | 1.2546 |
| MACD histogram | 0.9895 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'EW': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 99.3700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 4.3912 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 8.2698 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 16.6999 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 16.5631 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 18.0868 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.4705 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.9476 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1754 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5317 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.1155 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3099 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.7163 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6148 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.1855 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7821 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 29.3799 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 77.8390 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 29.8390 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.1750 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.1517 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 56.7829 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 73.4042 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.9895 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 12.3129 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 16.0797 -> Clearly above the moving-average trend level.

## TAILWINDS

### EDWARDS LIFESCIENCES ($EW) Releases Q3 2026 Earnings, Stock Rises
- Summary: EDWARDS LIFESCIENCES ($EW) Releases Q3 2026 Earnings, Stock Rises
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOVXI5ODZCMTdadEFoVEVINmlYZlVQSENUUUlXY2tDTWp3UzVGTHZ3bGZYS2pUaE5ZS3djR21laXBIUmQzaV9qQXRwcnBSSVFxVzNUR08zZDJTdzA4MjJYZm9Ga3B5c0J0Q2pFMWNIWmlXZTdmejNIMTRRZE92WGNSaHlLSktFSkRzYm5sdTdLb2taclFFVk1Wako4T1YtT2RvaHlITHBCOWNoZw?oc=5>

### Edwards Lifesciences' PASCAL System Trial Success Boosts Prospec
- Summary: Positive trial results for PASCAL System, indicating improved patient outcomes.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPLTNNVF91VC1xTndlSFVLRzhuazZJM1d4MnZXVlUyRVZfeGRtUVJ5bml0THNBYnV6ZzRYcm5BcmRCRFVjYnUwSEN5OEVPRUVDWWUwR3dIV0JJU0pUQjdmOHJjNVZRbDR0aFhjcUpRMmwtcEpzOUpNOWx2TTJUbXhYd3FReG83aUtIUWRmR2pjWThZNjJ2UWtEMHJJdklhdXVSaWR6NkNyZzNvS256UTRXX3dKZm44OUoz?oc=5>

### Edwards Lifesciences (EW) Reports Positive CLASP II TR Trial Res
- Summary: CLASP II TR trial shows favorable results for Edwards device.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOb0pDekI2dTZDeXNHOXZMM1lRX0VVQUtLTjEzSEtQMjN1aTdiR3BqcUJCWk4wSFJ2bnB2QUNnNG1CMWRiN1c4QXplRlVrV3dXTjhuTFZjNUhUb00yQWN0TG9GdmdXM2RVaXJYZVFEd1Y3UWZ0eTZVdV9DNTRnQVRlM2NhN0V4QXFOZmhKY2lEWTQzVV8yQjBxOUtoVFhhX0gzcUtSYTdkVUJDSy1OMm81cWNZQmRqa0ZYdGZMLVBrUHQ?oc=5>

### Mirae Asset Global Investments Co. Ltd. Buys 343,152 Shares of Edwards Lifesciences Corporation $EW
- Summary: Institutional investor purchases shares, indicating confidence in the company.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxQYUlLdS1adk9MamhRajExQzVTQ0ZPWVVxNGJvM2hhVVlTN2ptS195OHRfOWhoaF9aVGxuTnRJOGQ1U2xxTEI1MHppcXVQTk5TYzVyQ2ZFQjYtOGJycnZEbk44d3pnejhOcm1VN2VaOTF3cm85TTVUMGtrWDM5eVFCNWlrUjRyRlozTUtyWEw3c0o1alVyME1PM3V4S19zR2I5dmVsWk4wTGpyT0xqczZ4b2piRTUtNWh2cVdYMktkR2g2N1BlZ3dsaGdLbVpTeGZPWmNXRERBWUEzT2F0SU9panExV3V3RmxldE5qbw?oc=5>

### Edwards Lifesciences stock hits 52-week high at 98.7 USD By Investing.com
- Summary: Stock price reaches 52‑week peak, indicating strong investor confidence.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOOXV3ejNfRjExbkpIUVNkUkJGUXh1cDBXU1RyUTVDODA4QzB3SDVINE1neHNBNmZmeHBuak5weXpsYkRqa1F2NmFfcENwMVJ4aGhVbjVMaTN3bU1ONkFlQjhjY1dyRkFoSjBhRDNGSmhPdUxMdjMzSnNrNjJvR0x3amlkVHdUVFV4NkI0dUIxVHNYOXJROXEzUXlqUGJuc2xVWWJGUy1nTEoyY0p5eWNaZ0l5V0xSZw?oc=5>

### Edwards Lifesciences (EW) Trial Results Put Earlier TAVR Use In Focus
- Summary: Positive trial outcomes suggest earlier use of TAVR, boosting product prospects.
- Date: 2026-11-04 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQbTJEOW5FTER5Qy1EZjFkUjdaTnpPMEphY0I3SFY0Z3A5R1lfSTZfQVNUQmxhTVVjbExZQTNKX3l0RVhsR2Y5UHpzQXh5SWR4aVhFWm1wVENiVTdEWllkc2VPend3X0dmYlhBUmczSnViWVN1TndzeDJ0ZEsyOF9SRkNVWHYwVEQ0eW9tWnkyOFIyaUF0TzRrQ0RRLVZOMzdUZDY4UlNabW9kbEtmMlp0bDBvRkhYWkdHb3dKLTZpYlVGTmN5b2xhTnQwUU9mSExIMlUw0gHYAUFVX3lxTFBxNnB1N0tqSW4taTFsRW1uSnZHTWREUkMteDM3LThyUm45NVd4bTVKVzdEWGxFRy00YXpaUWwwWHdMTFB3aTVCUk5vMWtrQzdzdkZGeGtyZU5rZmpWdEJvVHJlTW1Fd29RX0VDd05DbGhwbTVEMGpGbE53amxFdUVVOVpKWkluX1R5RnhkZzJVYUh1Q3dNaUFmTFl0Tm5fT2NDUk1UVzB3U2hHMENnNEFhaUh2QVhyNjgzVzBoZ2MxYkJQX1JCV29hYW1iSWhwNElxbDBIZ1BDcA?oc=5>

### Edwards Lifesciences Corporation $EW Stock Position Lifted by AIA Group Ltd
- Summary: AIA Group’s increased stake signals confidence in EW’s future.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxOdEs5M3dOem1rZUwzNFVyakI5UjFIS19nNXZZM3JXZWFUUmM1SzRNSmYyQVlNWU9CQmNSekxMTnRZSm10dkRUXzlPY0ZFMnRRWlRUQS10WTNUbC1kRTV0RkRnb2t5TWlmVklXYm5GeEhfV3k1bjFiQVdwNE11MXltamx4dXhsaFJyb2dfdUZOZGlWa0o1dWdlYkhXdU82YTRyX25IS0NBWm1xVTZ4YXkyc044Q2NLdjNRQ2FialBKYkZTVUZzVHExcHBxMVo4TGR2?oc=5>

### This Edwards Lifesciences Analyst Turns Bullish; Here Are Top 5 Upgrades For Wednesday
- Summary: Analyst upgrades indicate bullish outlook for EW shares.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxNaGJ0VWNzX1RFUTZPUk5oU0RvNWxVMFRKWkxfMFIxSmh2VmxsZEdwYXpET1hVcXdUemh6RTdLMlc2b2pla2tSMlhpY09LcnoxeVZGNlFVZE1SdDFJYkNXaDlDLVZaMUdNRGRMWG12T1VlcmYwbG5jSE1HSmhnZjNrUlVacUJFQkVGTW5lTy1vZ2Jibm9URDFWRmRjd2JmbXd3TFpLVEJJUG1FUkMwYVRMdmxITzZqNWxtZEszZkJmbmR6TTJtUlVCTXIwQkMxdVBKSTZVSEVZN0N2QmVIWlBGWHY5eWlSVUl0T1dYNg?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Edwards Lifesciences Q3 2026 Earnings Call Transcript
- Summary: Edwards Lifesciences Q3 2026 Earnings Call Transcript
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPX1F6OFo3WGZ5T2ZXdVVabEsyTmZHMGRudkdGZk84V1lxdVNvYl9LM2tzNHpleXc5REptVVB2MWczb19ua0xLejctT3RGUXBNLWJ4eE9ZOUVtMlU0VFZqQWk2MFVOREd4UDdWekF5YjF3OTRWQVdOc2pzNldHUl9nRlM2RzBTWEw4UWRZWHBkZkNuTTcwVEw0ZTM4WGJYLXc?oc=5>

### Edwards Lifesciences Corporation $EW Stock Sold by Sumitomo Mitsui Trust Group Inc.
- Summary: Edwards Lifesciences Corporation $EW Stock Sold by Sumitomo Mitsui Trust Group Inc.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxQS1A3NGE0RHNKSUc2c05xaTVYS04wMVl2TEQtX0xIc0dqaHppYnNZU0tTT1huNFROQUhLYU5lNkRwb0lSUXFSZEVwWDZWenVCOG95QjVaaFVYbnp3R1RIMU5qeHJYMXA0TVNsMGxUaTNBcEFqUWQxd1Vkb3FXbEV4YWlKQVpXcGI5WTh4YkV2aVVQb281VU5kNFh4cHljUkIyamdBQ09YMkNSRXVjWUptZWtLbzNOWVFtMHdXYjZ0bGFHSFJscE9ZV2tuNUVhOG80WWhiTnp3RzFOQQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **EW** | **56.78** | **5.40** | **26.96** | **13.60** | **57,276,870,656.00 USD** | **18.09** |
| MDT | 24.30 | 2.67 | 14.82 | 13.70 | 134,258,311,168.00 USD | 19.93 |
| BSX | 18.33 | 2.59 | 14.00 | 1.40 | 66,414,866,432.00 USD | -53.64 |
| ABT | 42.94 | 3.91 | 19.04 | 14.50 | 199,876,591,616.00 USD | -5.90 |

Peers fetched as_of: 2026-11-04; EW reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: N/A (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,715,500,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 307,500,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1099800/000109980026000054/ew-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOVXI5ODZCMTdadEFoVEVINmlYZlVQSENUUUlXY2tDTWp3UzVGTHZ3bGZYS2pUaE5ZS3djR21laXBIUmQzaV9qQXRwcnBSSVFxVzNUR08zZDJTdzA4MjJYZm9Ga3B5c0J0Q2pFMWNIWmlXZTdmejNIMTRRZE92WGNSaHlLSktFSkRzYm5sdTdLb2taclFFVk1Wako4T1YtT2RvaHlITHBCOWNoZw?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPLTNNVF91VC1xTndlSFVLRzhuazZJM1d4MnZXVlUyRVZfeGRtUVJ5bml0THNBYnV6ZzRYcm5BcmRCRFVjYnUwSEN5OEVPRUVDWWUwR3dIV0JJU0pUQjdmOHJjNVZRbDR0aFhjcUpRMmwtcEpzOUpNOWx2TTJUbXhYd3FReG83aUtIUWRmR2pjWThZNjJ2UWtEMHJJdklhdXVSaWR6NkNyZzNvS256UTRXX3dKZm44OUoz?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOb0pDekI2dTZDeXNHOXZMM1lRX0VVQUtLTjEzSEtQMjN1aTdiR3BqcUJCWk4wSFJ2bnB2QUNnNG1CMWRiN1c4QXplRlVrV3dXTjhuTFZjNUhUb00yQWN0TG9GdmdXM2RVaXJYZVFEd1Y3UWZ0eTZVdV9DNTRnQVRlM2NhN0V4QXFOZmhKY2lEWTQzVV8yQjBxOUtoVFhhX0gzcUtSYTdkVUJDSy1OMm81cWNZQmRqa0ZYdGZMLVBrUHQ?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxQYUlLdS1adk9MamhRajExQzVTQ0ZPWVVxNGJvM2hhVVlTN2ptS195OHRfOWhoaF9aVGxuTnRJOGQ1U2xxTEI1MHppcXVQTk5TYzVyQ2ZFQjYtOGJycnZEbk44d3pnejhOcm1VN2VaOTF3cm85TTVUMGtrWDM5eVFCNWlrUjRyRlozTUtyWEw3c0o1alVyME1PM3V4S19zR2I5dmVsWk4wTGpyT0xqczZ4b2piRTUtNWh2cVdYMktkR2g2N1BlZ3dsaGdLbVpTeGZPWmNXRERBWUEzT2F0SU9panExV3V3RmxldE5qbw?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOOXV3ejNfRjExbkpIUVNkUkJGUXh1cDBXU1RyUTVDODA4QzB3SDVINE1neHNBNmZmeHBuak5weXpsYkRqa1F2NmFfcENwMVJ4aGhVbjVMaTN3bU1ONkFlQjhjY1dyRkFoSjBhRDNGSmhPdUxMdjMzSnNrNjJvR0x3amlkVHdUVFV4NkI0dUIxVHNYOXJROXEzUXlqUGJuc2xVWWJGUy1nTEoyY0p5eWNaZ0l5V0xSZw?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQbTJEOW5FTER5Qy1EZjFkUjdaTnpPMEphY0I3SFY0Z3A5R1lfSTZfQVNUQmxhTVVjbExZQTNKX3l0RVhsR2Y5UHpzQXh5SWR4aVhFWm1wVENiVTdEWllkc2VPend3X0dmYlhBUmczSnViWVN1TndzeDJ0ZEsyOF9SRkNVWHYwVEQ0eW9tWnkyOFIyaUF0TzRrQ0RRLVZOMzdUZDY4UlNabW9kbEtmMlp0bDBvRkhYWkdHb3dKLTZpYlVGTmN5b2xhTnQwUU9mSExIMlUw0gHYAUFVX3lxTFBxNnB1N0tqSW4taTFsRW1uSnZHTWREUkMteDM3LThyUm45NVd4bTVKVzdEWGxFRy00YXpaUWwwWHdMTFB3aTVCUk5vMWtrQzdzdkZGeGtyZU5rZmpWdEJvVHJlTW1Fd29RX0VDd05DbGhwbTVEMGpGbE53amxFdUVVOVpKWkluX1R5RnhkZzJVYUh1Q3dNaUFmTFl0Tm5fT2NDUk1UVzB3U2hHMENnNEFhaUh2QVhyNjgzVzBoZ2MxYkJQX1JCV29hYW1iSWhwNElxbDBIZ1BDcA?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxOdEs5M3dOem1rZUwzNFVyakI5UjFIS19nNXZZM3JXZWFUUmM1SzRNSmYyQVlNWU9CQmNSekxMTnRZSm10dkRUXzlPY0ZFMnRRWlRUQS10WTNUbC1kRTV0RkRnb2t5TWlmVklXYm5GeEhfV3k1bjFiQVdwNE11MXltamx4dXhsaFJyb2dfdUZOZGlWa0o1dWdlYkhXdU82YTRyX25IS0NBWm1xVTZ4YXkyc044Q2NLdjNRQ2FialBKYkZTVUZzVHExcHBxMVo4TGR2?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxNaGJ0VWNzX1RFUTZPUk5oU0RvNWxVMFRKWkxfMFIxSmh2VmxsZEdwYXpET1hVcXdUemh6RTdLMlc2b2pla2tSMlhpY09LcnoxeVZGNlFVZE1SdDFJYkNXaDlDLVZaMUdNRGRMWG12T1VlcmYwbG5jSE1HSmhnZjNrUlVacUJFQkVGTW5lTy1vZ2Jibm9URDFWRmRjd2JmbXd3TFpLVEJJUG1FUkMwYVRMdmxITzZqNWxtZEszZkJmbmR6TTJtUlVCTXIwQkMxdVBKSTZVSEVZN0N2QmVIWlBGWHY5eWlSVUl0T1dYNg?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPX1F6OFo3WGZ5T2ZXdVVabEsyTmZHMGRudkdGZk84V1lxdVNvYl9LM2tzNHpleXc5REptVVB2MWczb19ua0xLejctT3RGUXBNLWJ4eE9ZOUVtMlU0VFZqQWk2MFVOREd4UDdWekF5YjF3OTRWQVdOc2pzNldHUl9nRlM2RzBTWEw4UWRZWHBkZkNuTTcwVEw0ZTM4WGJYLXc?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxQS1A3NGE0RHNKSUc2c05xaTVYS04wMVl2TEQtX0xIc0dqaHppYnNZU0tTT1huNFROQUhLYU5lNkRwb0lSUXFSZEVwWDZWenVCOG95QjVaaFVYbnp3R1RIMU5qeHJYMXA0TVNsMGxUaTNBcEFqUWQxd1Vkb3FXbEV4YWlKQVpXcGI5WTh4YkV2aVVQb281VU5kNFh4cHljUkIyamdBQ09YMkNSRXVjWUptZWtLbzNOWVFtMHdXYjZ0bGFHSFJscE9ZV2tuNUVhOG80WWhiTnp3RzFOQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
