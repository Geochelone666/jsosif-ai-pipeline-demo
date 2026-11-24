# MCK Intelligence Report

- ticker: **MCK**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/MCK/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCK/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:39:35.261971+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 10, 'rule': 2, 'ai': 7, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261123T053847Z-45053549/MCK** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 10 unique headlines; 6 named publishers; 0 exact duplicates; 10 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1048.4200 |
| Return 1D (%) | -1.9646 |
| Return 1W (%) | -5.1238 |
| Return 1M (%) | 4.7613 |
| Return YTD (%) | 28.1947 |
| Return 1Y (%) | 21.5371 |
| Annualized volatility (%) | 31.8601 |
| Beta vs SPY | -0.1828 |
| Max drawdown (%) | -27.1691 |
| Sharpe (rf=0) | 0.7564 |
| Downside deviation (rf=0, %) | 18.5498 |
| Sortino (rf=0) | 1.2992 |
| Historical VaR 95% (1D, %) | 2.5993 |
| Historical ES 95% (1D, %) | 3.6083 |
| Correlation vs SPY | -0.0859 |
| Tracking error vs SPY (%) | 36.3499 |
| P/E (trailing) | 27.04 |
| P/B | -30.49 |
| EV/EBITDA | 17.62 |
| Revenue growth (%) | 7.60 |
| Forward P/E (estimate) | 19.99 |
| Gross margin (%) | 3.65 |
| Operating margin (%) | 1.59 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 6.12 |
| MA50 | 977.0726 |
| Close vs MA50 (%) | 7.3022 |
| MA200 | 879.2209 |
| Close vs MA200 (%) | 19.2442 |
| RSI (14, Wilder) | 53.5298 |
| MACD (12,26) | 27.4044 |
| MACD signal (9) | 33.0667 |
| MACD histogram | -5.6623 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCK': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1048.4200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.9646 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.1238 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.7613 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 28.1947 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 21.5371 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.8601 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.5498 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.2992 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5993 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.6083 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0859 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 36.3499 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1828 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.1691 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7564 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 19.9861 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 3.6530 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 1.5900 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.1155 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.0420 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.5298 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -5.6623 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.3022 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 19.2442 -> Clearly above the moving-average trend level.

## TAILWINDS

### McKesson (MCK) Stock Still Sits Below Fair Value On Raised EPS Guidance
- Summary: McKesson (MCK) Stock Still Sits Below Fair Value On Raised EPS Guidance
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQdW1BVTFCeUdGb29fYWRnQnRiQ0Qyd1NramlSQzFBazJmTmhGSXozaUhHcnEzUGRnR0FFYTZMVnkzVnVGZjNKeG8xa1BLY0lRV1BwTmw3YnREeWJiNHhhX2V0Snk5QUlzUng3RzhCX0E5ZEdqeXV1UEwwbGVJYmd0U2NGNVZGRXpIX203N2EzRUMyMzZxSGM3OXJ1cUJaZWYwcGZQc0M4MA?oc=5>

### Two Deals and a Higher Target: UBS’s Call on McKesson (MCK)
- Summary: Discusses UBS's updated target and two new deals involving McKesson.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxQdG1zMDh1d1doZEFIWG9aa281cWdxa1Fhb05zcHlSOHBFNnpFVjRDVG93SWVPSm5XYXlQVEE4bll2UHZrOVB1MjdSdjZtRUpFcVQ2M256Q1BqVjFNZmpkVThtZ3FJMVJhNS1Vbk9fX0s5cnRSR0o1bjk0R0pEQWt0R3ZB?oc=5>

### McKesson (MCK) Q2 Growth Keeps Undervalued Narrative In Focus
- Summary: Q2 earnings exceed expectations, supporting undervalued view.
- Date: 2026-11-18 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQSlAycHpLcmxJN2J0Ul9oOEwzNDZnOWRRYzc0MU5FeUhjMUx2S004OUpSOGJ1TVdJcDRfVjUxUFA1QTdTMzBqZHVJVlBrSUxWZ3g5eFItZ280QzRhc201U3l6RTRfY2dlRi1sYTVjZ3h5RC1IMjBKLWZvX0pWY3pWZDBVWDJneHFxRVo5TDFpb3BkN0JINTJ4eTNrSDJEWVdEQmgwNXhBNUV1QlBNSkJKR0ZCeUVqZDE0ZWJYQTkzM3dQQmvSAcgBQVVfeXFMTjFaMWhtN0NGZlJZRjdNOGd2UUVBX3dfQTVmZnZROThMYUU3bzhxRF9tU19MRm5jT0NqVHcwM2ZyMy1jSW42TjM0ei1NNGdyOG9Ka3czeUFuNGYxazhEVU1aejVLdlZ4TE55eG8zaE10VTJ6c0N0SXdhcGh2MUtqUDlUck90ODRQalE0OHJ0anQwQy1UaHhtVFFOZGdyWnBiMEhlTjJSYzVpVHBPQS1ZcC10bnp4V292VXkwUnFpOWhnVnEyR21wQVU?oc=5>

### McKesson (MCK) Expands In Oncology And Multispecialty Care
- Summary: McKesson expands its oncology and multispecialty care services, indicating growth potential.
- Date: 2026-11-21 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPbHhHbkthcWZpaHZCbXlvbkZMMElSZTNlbzQ2VHpnOUVzVjRKUkx3MmNzWnB0bG1vTGZMc3VLeE5ybUNubDUyX2VRcDN1YXg5M3h0dlNhS19Fc2tjRklpcGY1Z2phdmFWdVR3c0tWUWlCNVJxTFdwNVJ3MzhCSWhFTFE0LTRDa1hJOE1TcnZieWxXZ01Jc3ZlU1F3MGd2bmxxcDFwNnZwLUV0MVozNTlWRjBfcU5ESEtqa2ZWYmluY9IBxAFBVV95cUxNWFpiaHQwMUpyb2dBb0lldG9yZHNXdU5OVUZRUVZOVzdvbTJiemxxc1FYdzNpZW1vbHhlZkwtbFdIUFdXUU9mTVg1RG0zbDlBQkJIQ29abnRLQlpINm9JbDJDbFZMNXNYa3V2MlhzbXFpS1VqeEtMSVY2Zk1PbXZiVFhCNVM2MDJ1VUt5b0owU3pNVmpNdVZ4STN6cnVnTUl0cDJPNW4zcWxkNDJOMlA1aXVUbXJVcVJ6Z29DMWRkTm9IaW4z?oc=5>

### Here's Why You Should Add McKesson Stock to Your Portfolio Now
- Summary: Positive recommendation to invest in McKesson stock.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPeTI3T1pQbWZhYUVHa0h1NEZLZXRaLXhId2RDazNxQ1lWTzlxRUs0WlVnczFBR2h5RVFoQ3g4MTlFdXBQQUwyeGhqU1BEWjRhTDQxSTd2c2Nic3FOZFlaZVR0ejlBQklyWWxNU29VS1dnQ3QxVEVFWmlCcGtrVGwwVmZHV2xWQ3FIOTBNanNWelFRem1jemlTZkdtOEE0c25JQlR0SFJWNVMwM1dxdXd6SVozdGw5Vzg5bXc?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### McKesson's (NYSE:MCK) Solid Earnings Are Supported By Other Strong Factors
- Summary: McKesson's (NYSE:MCK) Solid Earnings Are Supported By Other Strong Factors
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPQ0J1Uk0xSFdwcDN1eFNWRlpJUWMwc0Q2czdfTUNtblNCdXhsVGJfQkVDWGtYN0ZFdzhkVW9iWGpFY25CTDF5bFg0a2pqV3NPVjNfLXpnSnRad1hhdHROWEMzbXJKMmZxekNBajdCcFo2RXVITzJDQzNzdm5fWG5UZHM5YjRJbHJxVV9ZU1hqWTZpaEt3NjZaSWUwdW51RXhrWS1JaTNpcGRTMXRuS1FWZFFGdGdtdTJMZXkwSWZtMkFqZ0dX?oc=5>

### McKesson Corporation (MCK) Stock Forecasts
- Summary: Forecasts for McKesson stock performance.
- Date: 2026-11-19 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxOMkRtQkxVZEpQTFA2b2J4cXJPa3V5bjgzX3YyYXNhczhJUU9oY21FZzBEcC0zQW4wejBWbXB0akE2MVByX2NYaThNZDhZU0pqVTlQMzRKSXJkd0hKcXh3Y3ltcXU0b2NqUkEyS3A3QV8zZGdRV2xVaXVQNE8waWxQd3J4dDJRN1JZTUg0eQ?oc=5>

### Should Stronger Oncology Earnings Require Action From McKesson (MCK) Investors?
- Summary: Questioning investor response to stronger oncology earnings.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOUlFDTE9CeW1vRGdkSTYtT29CUUdETjRxMkRtTHJuYTVQMlRzeE9zd3BJQWFnWkJ3X0JKbmVJUjBuNHZxYS1UNzk3Z3JUeDBDU3ZXd3BTLTA5Z2d1MUtjRGNITkp0QVpJU08xNEVRazAyTEVTaFFlcG95VDVVZWtYblkwTTdSdjNxZlhOZjB6cU5LVnlhYWUzZlR6WUlmMlpNM28xdXZyMG9naUJGVkRhcnZoZ2hpVFNiZjVjblZLTnlnTDFh0gHKAUFVX3lxTE1iQ3pfRGxFc05ZNGRuaGFIdGxlaHplMW02MjFiQldzRmlELTRnV0I4eTRNblVBZzl6cS1ESUlmcy1pNHpXaXR4emtnX3pHSmhtbjNmS1pUUVYyYkRKTWczYWthZFUxazFETVF6Y0RMTmhqeV9iNXRqWjA2YkNKYkdJSFFjb2NPNDg3NWwxLU1fR25nX1J6bURaZklDc0xyN3Y5c19YcVhYcTIzR1VLUGxTZTNnSExfbllSdkNTREpaSDNqYXl6TXI2RGc?oc=5>

## RISKS

### The Open Question In McKesson’s Two New Deals
- Summary: Uncertainty surrounding two new deals involving McKesson.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPaHZXNjNxNWpfZE5PY1NnVTF4NTVMNm41NE92d0RwcFN4MmlRa2E0eGJvaWlYX0d2R3UxRjhaUFUzX3o1YUs0ZDlnZDg3N0lnbXVXQnhYYUJjN2VJTGV0SGVNb1VBdXFseVdLcUlJNFk5RVpDX0dRNHNfTnJySnVTMV9KcENuZDhzUUFjRWtWNDJGdVNscGtYX2ZtUmJxVW91c1pPZTRTUQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCK** | **27.04** | **-30.49** | **17.62** | **7.60** | **121,047,080,960.00 USD** | **21.54** |
| COR | 18.83 | 17.52 | 12.40 | 5.50 | 64,507,215,872.00 USD | -6.83 |
| CAH | 35.18 | -20.86 | 15.17 | 5.50 | 62,862,237,696.00 USD | 31.06 |
| CNC | 21.76 | 1.41 | 4.99 | 0.20 | 31,347,705,856.00 USD | 73.48 |

Peers fetched as_of: 2026-11-23; MCK reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 29,980,000,000.00 USD; period 2011-04-01/2011-06-30; fiscal year/reporting period 2011/Q1
- Net income (latest available single quarter): 1,218,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/927653/000092765326000281/mck-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipwFBVV95cUxQdW1BVTFCeUdGb29fYWRnQnRiQ0Qyd1NramlSQzFBazJmTmhGSXozaUhHcnEzUGRnR0FFYTZMVnkzVnVGZjNKeG8xa1BLY0lRV1BwTmw3YnREeWJiNHhhX2V0Snk5QUlzUng3RzhCX0E5ZEdqeXV1UEwwbGVJYmd0U2NGNVZGRXpIX203N2EzRUMyMzZxSGM3OXJ1cUJaZWYwcGZQc0M4MA?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxQdG1zMDh1d1doZEFIWG9aa281cWdxa1Fhb05zcHlSOHBFNnpFVjRDVG93SWVPSm5XYXlQVEE4bll2UHZrOVB1MjdSdjZtRUpFcVQ2M256Q1BqVjFNZmpkVThtZ3FJMVJhNS1Vbk9fX0s5cnRSR0o1bjk0R0pEQWt0R3ZB?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQSlAycHpLcmxJN2J0Ul9oOEwzNDZnOWRRYzc0MU5FeUhjMUx2S004OUpSOGJ1TVdJcDRfVjUxUFA1QTdTMzBqZHVJVlBrSUxWZ3g5eFItZ280QzRhc201U3l6RTRfY2dlRi1sYTVjZ3h5RC1IMjBKLWZvX0pWY3pWZDBVWDJneHFxRVo5TDFpb3BkN0JINTJ4eTNrSDJEWVdEQmgwNXhBNUV1QlBNSkJKR0ZCeUVqZDE0ZWJYQTkzM3dQQmvSAcgBQVVfeXFMTjFaMWhtN0NGZlJZRjdNOGd2UUVBX3dfQTVmZnZROThMYUU3bzhxRF9tU19MRm5jT0NqVHcwM2ZyMy1jSW42TjM0ei1NNGdyOG9Ka3czeUFuNGYxazhEVU1aejVLdlZ4TE55eG8zaE10VTJ6c0N0SXdhcGh2MUtqUDlUck90ODRQalE0OHJ0anQwQy1UaHhtVFFOZGdyWnBiMEhlTjJSYzVpVHBPQS1ZcC10bnp4V292VXkwUnFpOWhnVnEyR21wQVU?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPbHhHbkthcWZpaHZCbXlvbkZMMElSZTNlbzQ2VHpnOUVzVjRKUkx3MmNzWnB0bG1vTGZMc3VLeE5ybUNubDUyX2VRcDN1YXg5M3h0dlNhS19Fc2tjRklpcGY1Z2phdmFWdVR3c0tWUWlCNVJxTFdwNVJ3MzhCSWhFTFE0LTRDa1hJOE1TcnZieWxXZ01Jc3ZlU1F3MGd2bmxxcDFwNnZwLUV0MVozNTlWRjBfcU5ESEtqa2ZWYmluY9IBxAFBVV95cUxNWFpiaHQwMUpyb2dBb0lldG9yZHNXdU5OVUZRUVZOVzdvbTJiemxxc1FYdzNpZW1vbHhlZkwtbFdIUFdXUU9mTVg1RG0zbDlBQkJIQ29abnRLQlpINm9JbDJDbFZMNXNYa3V2MlhzbXFpS1VqeEtMSVY2Zk1PbXZiVFhCNVM2MDJ1VUt5b0owU3pNVmpNdVZ4STN6cnVnTUl0cDJPNW4zcWxkNDJOMlA1aXVUbXJVcVJ6Z29DMWRkTm9IaW4z?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPeTI3T1pQbWZhYUVHa0h1NEZLZXRaLXhId2RDazNxQ1lWTzlxRUs0WlVnczFBR2h5RVFoQ3g4MTlFdXBQQUwyeGhqU1BEWjRhTDQxSTd2c2Nic3FOZFlaZVR0ejlBQklyWWxNU29VS1dnQ3QxVEVFWmlCcGtrVGwwVmZHV2xWQ3FIOTBNanNWelFRem1jemlTZkdtOEE0c25JQlR0SFJWNVMwM1dxdXd6SVozdGw5Vzg5bXc?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPQ0J1Uk0xSFdwcDN1eFNWRlpJUWMwc0Q2czdfTUNtblNCdXhsVGJfQkVDWGtYN0ZFdzhkVW9iWGpFY25CTDF5bFg0a2pqV3NPVjNfLXpnSnRad1hhdHROWEMzbXJKMmZxekNBajdCcFo2RXVITzJDQzNzdm5fWG5UZHM5YjRJbHJxVV9ZU1hqWTZpaEt3NjZaSWUwdW51RXhrWS1JaTNpcGRTMXRuS1FWZFFGdGdtdTJMZXkwSWZtMkFqZ0dX?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxOMkRtQkxVZEpQTFA2b2J4cXJPa3V5bjgzX3YyYXNhczhJUU9oY21FZzBEcC0zQW4wejBWbXB0akE2MVByX2NYaThNZDhZU0pqVTlQMzRKSXJkd0hKcXh3Y3ltcXU0b2NqUkEyS3A3QV8zZGdRV2xVaXVQNE8waWxQd3J4dDJRN1JZTUg0eQ?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOUlFDTE9CeW1vRGdkSTYtT29CUUdETjRxMkRtTHJuYTVQMlRzeE9zd3BJQWFnWkJ3X0JKbmVJUjBuNHZxYS1UNzk3Z3JUeDBDU3ZXd3BTLTA5Z2d1MUtjRGNITkp0QVpJU08xNEVRazAyTEVTaFFlcG95VDVVZWtYblkwTTdSdjNxZlhOZjB6cU5LVnlhYWUzZlR6WUlmMlpNM28xdXZyMG9naUJGVkRhcnZoZ2hpVFNiZjVjblZLTnlnTDFh0gHKAUFVX3lxTE1iQ3pfRGxFc05ZNGRuaGFIdGxlaHplMW02MjFiQldzRmlELTRnV0I4eTRNblVBZzl6cS1ESUlmcy1pNHpXaXR4emtnX3pHSmhtbjNmS1pUUVYyYkRKTWczYWthZFUxazFETVF6Y0RMTmhqeV9iNXRqWjA2YkNKYkdJSFFjb2NPNDg3NWwxLU1fR25nX1J6bURaZklDc0xyN3Y5c19YcVhYcTIzR1VLUGxTZTNnSExfbllSdkNTREpaSDNqYXl6TXI2RGc?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPaHZXNjNxNWpfZE5PY1NnVTF4NTVMNm41NE92d0RwcFN4MmlRa2E0eGJvaWlYX0d2R3UxRjhaUFUzX3o1YUs0ZDlnZDg3N0lnbXVXQnhYYUJjN2VJTGV0SGVNb1VBdXFseVdLcUlJNFk5RVpDX0dRNHNfTnJySnVTMV9KcENuZDhzUUFjRWtWNDJGdVNscGtYX2ZtUmJxVW91c1pPZTRTUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
