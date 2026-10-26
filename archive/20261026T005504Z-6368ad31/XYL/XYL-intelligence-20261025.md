# XYL Intelligence Report

- ticker: **XYL**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/XYL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/XYL/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T00:57:24.192080+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 16, 'rule': 7, 'ai': 6, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 16 unique headlines; 4 named publishers; 0 exact duplicates; 16 HTTPS source links; largest publisher share 75.0%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 108.7400 |
| Return 1D (%) | -0.4759 |
| Return 1W (%) | 4.5074 |
| Return 1M (%) | 0.0920 |
| Return YTD (%) | -19.2588 |
| Return 1Y (%) | -25.3407 |
| Annualized volatility (%) | 25.4315 |
| Beta vs SPY | 0.7416 |
| Max drawdown (%) | -33.1192 |
| Sharpe (rf=0) | -1.0252 |
| Downside deviation (rf=0, %) | 20.0501 |
| Sortino (rf=0) | -1.3003 |
| Historical VaR 95% (1D, %) | 2.7771 |
| Historical ES 95% (1D, %) | 4.0784 |
| Correlation vs SPY | 0.3717 |
| Tracking error vs SPY (%) | 23.8380 |
| P/E (trailing) | 25.89 |
| P/B | 2.44 |
| EV/EBITDA | 13.86 |
| Revenue growth (%) | 1.50 |
| Forward P/E (estimate) | 17.49 |
| Gross margin (%) | 39.24 |
| Operating margin (%) | 17.00 |
| Return on equity (%) | 9.18 |
| Free cash flow yield (%) | 4.66 |
| MA50 | 107.1162 |
| Close vs MA50 (%) | 1.5160 |
| MA200 | 117.7677 |
| Close vs MA200 (%) | -7.6657 |
| RSI (14, Wilder) | 62.6330 |
| MACD (12,26) | 0.0812 |
| MACD signal (9) | -0.9747 |
| MACD histogram | 1.0559 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'XYL': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 108.7400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.4759 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.5074 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.0920 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -19.2588 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -25.3407 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.4315 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.0501 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.3003 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.7771 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.0784 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3717 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.8380 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7416 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -33.1192 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.0252 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.4933 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 39.2400 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.9950 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.1830 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.6624 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.8905 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 62.6330 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.0559 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.5160 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -7.6657 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Xylem (NYSE:XYL) Stock Price Target Lowered at JPMorgan Chase & Co.
- Summary: Xylem (NYSE:XYL) Stock Price Target Lowered at JPMorgan Chase & Co.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNT2pyX2NuUUNySVp2cWRGSURUS3NkenpBd2UxOFB0bXpWNXFSRWZIRHpERFlDcUJyamJoQnYzODdfT1B2SXBMYkRjT1RkZWwtSnoxMFNQbEU4eUJsdVJhVTFJYW15RVE1UUxxRUpPT0hUUDM3a1oyY0xkd1I0U2p3TUZuamQ1ZnpoYTUyb3k5aFNqdHFMUXlMMHRpZ3JfTm5ILXdDV0VVSXVaRG5TcVV0SDlMVVRQWmJKWFhnTkhoVHYxdw?oc=5>

## CATALYSTS

### Xylem (XYL) Reports Next Week: Wall Street Expects Earnings Growth
- Summary: Xylem (XYL) Reports Next Week: Wall Street Expects Earnings Growth
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQSFpqZmFkZlZSTEVNc0hkUjM3QU1yZnNQODdiY0tSUTktTk5MM2NlMmlKQWxER09EQnJlLUFONUhnLWhreG9qTFdUZ3VTTGdJZ3Q0cEpTSlBBbU5Id2w4UGkwUFlueWo3aEEzTDdWOWh2emZMa3g2dUkwM2ViVWl6Wkg5U1pGNm83aWtzb2hDMEF6OTN6cGNj?oc=5>

### Xylem Inc. $XYL Stock: Brookmont Capital Management Raises Position
- Summary: Xylem Inc. $XYL Stock: Brookmont Capital Management Raises Position
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNNDZrNHk3NjRqZGV5R0lNQzZMRVhTSjY0Ql9zSENTOHNaVTZoNkpTWDliRm92ZmlwUmFsR00yT2VRUnJfNm43a3hvQzctYnd2UTItbmpWYWo2R2FJZmxTMDFaNHlJdi1reVdXU1pXZjRnOXVBd0trSEZKcUdiamctM25Nd2ZMOUVDS01LelBrNzMzYWhWT3dCc0h1MWdUMnlNbGUxOWdrWGFDd1dFZDhJNmJXUmd0M2VSVFM5ZGd1VUxjTlk?oc=5>

### Xylem Inc. $XYL Shares Sold by Robeco Schweiz AG
- Summary: Xylem Inc. $XYL Shares Sold by Robeco Schweiz AG
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPNmQ0cERxaHY0VE5PUUJvVkVRVVlOdklJRW9NRVk0OVVRdE03WWN0cVpRcWNtdmdyM0VjdUdhZWMtblFTWndzeXIwVnk4b0Z0MWRnd0s0bmt4ajVuNXhRWG5CbFZxaVlPeWFrOVlYVWJqZUQyZTJlanFTRmhQYWpDX3R0YUhiOENBeklzZlU3aEk3aG5ud0E3YWMtSEdwMFdTeGoyZ05zNUFvZnc?oc=5>

### Xylem Inc. $XYL Shares Bought by Pinnacle Associates Ltd.
- Summary: Xylem Inc. $XYL Shares Bought by Pinnacle Associates Ltd.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQOU1XSENBMUxISE5qLTAzbVZDa0Y1cnFjd2NGRS1SdnE5a3FjczdiSGNtR3haVDdscXFwcHZGaHF3dFl5cl9xd0EwNGozTm9reVY4enZzemplSmxSQ1dXb3c1MFdsaUR2NWhqdGZCZnd0UjZEMTN6R29KaTQtTWVsSjFjeUdiZkNDMElHOExtbDdrTFVnZkJER1BVREloY2RKbzVJLXpkb0M5bjJIcmRPYU5Uc05jZw?oc=5>

### Xylem (XYL) Dividend Yield 2026, Date & History $XYL
- Summary: Xylem (XYL) Dividend Yield 2026, Date & History $XYL
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiYkFVX3lxTE5MVzQ1OGIxcjZRQzBoeXFRRmdKTEF1alpmdlBwNS1ZT1FXMU9hX0psUWRFZFRDeDNEd0xhWjk4cDZyZGpDbW5Cb25JbGhLSUw1Y1NMX1pLdG1aMi00bHp6bC1n?oc=5>

### Xylem (XYL) Set to Announce Quarterly Earnings on Tuesday
- Summary: Xylem (XYL) Set to Announce Quarterly Earnings on Tuesday
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNaTZ2YmZJM2R3MUFBcEw1dEdsdnByZmxCREIyZTktRDVZNHV2VGUwTDdINHkzMHVSYkF0Q2hxcXJnaDFWc1RJTDBnMFRxQUtlUVNUNnpHaEgzZG4xa3hWWS1leFM1cUNRNzFDdnQ0UWNXbTViZGZKTDA1Zjd4UVRDOEx0V2VGclFNeU9najRQQkZKWXk1NkpvbW1tY2lpaFJybENMTlBJVnh5NmdBWHNmaFpQMjUzZFJTemc?oc=5>

### Xylem (NYSE:XYL) Stock Forecast & Analyst Predictions
- Summary: Analyst forecasts and price targets for Xylem stock.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidkFVX3lxTE5xa2pia216MXpBQTd6Zzh4bnVLaWRtS213VDRqazJkZWpXWG5vRFhQeGdiazFJaW8ySUdGS2tUSzdSZUNDNHo2WVpYNHUwZHh3OTVXRnJrUk9KdE9qcXNjU1h5ZGQxQ01iUk1XOTNqQ01kVzJhNGc?oc=5>

### Xylem (XYL) Stock Forecast and Price Target 2026 $XYL
- Summary: 2026 price target set for Xylem shares.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiYkFVX3lxTE9GLTFUMWl1cy1VNDhpWS1mdGEySFBFWW5HQVNpazVfYXpDb0VvT1Q1bVAtQUQ3Zm96U2QwaUV3eFdtVXpjWVNKa2ZRRE52OVQ4ZUlGT1l6UnZkVzZPMVlfeWZR?oc=5>

### Xylem (XYL) Stock May Be 34% Undervalued On Cash Flow
- Summary: Analysis suggests Xylem stock undervalued by 34%.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPdGlCMjlZNzhBS08tY2RQUzNJdkZXYWRNMkk1LXQxLUNqUHR1NjBpRWJWaHJ4QnA4R3FPZ3A0VGRXcW11RnM3cEhnVlg1dHEtVGd2NEE3RTNkTXh0ejV5TkZkUHduck54TlJfYjM2eURnMnEyYTF2UVNGUDdFMjJKTlR0Sk1ud0VNV29RaUV1eDJ0T2dzUXJJUlBQU21XTmtjN1VNcGRNMXVaUm9kOF9GNHFla0VmWk3SAbwBQVVfeXFMTzRCbmplNW5UR0V6Mk9KakVCaE1PRlNraVkwS3U3aGJSZnZ3T2VmTXV4MWJHbVFyVE5VQjAyRmdfS1h4N2RQa3RKYlg1OVZzZmJrN3AyeHRHUzQxRGk5SG5KbWd1RlpkNlZPcWQxQXE2dUZzX1NhSF8wcE9udkdJSFhKdGJMemMyNWtLTnd0Qmt6NVZFWExOWnBmTlQyUmNibEt2YVFOYUFZalB0Vm9pTG56eV9WZVlPMzlPMWQ?oc=5>

### Xylem Inc. $XYL Shares Newly Bought by Iridian Asset Management LLC CT
- Summary: Iridian Asset Management purchased Xylem shares.
- Date: 2026-10-25 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxNd24yalZEQUh5NWxfMDVsekU2NUhUZm5Md1ZzVmJ1N21WTWF3MS1rQjQwWUg4UDJHejYyeDZVUFRTdlNOVUUycDRnSks3R0xVRnV0MUxsaEpraFI5WkVBNVZwanRieHdsaWNvZHNhakRNSG9hNW93cndNeHFFWVVaR05PX182YXZJeU43T3VVc1R3VmFpcC00Z210bjlEVWRDZk5HcGxMcEZoVDJBTmNqbEVXaVlnZFdTS1RnUG1VSkJWdk1OcDY2WA?oc=5>

### 18,543 Xylem Inc. $XYL Shares Acquired by Vest Financial LLC
- Summary: Vest Financial acquired 18,543 Xylem shares.
- Date: 2026-10-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNN1pLbVVDUWp0dkNHV0d4SmRsYUxVRzRmT0FOWUl4ay1ablRCV0NVbE55QzN6LXRQU21NN3IxWjhTMFBHY0J0N0ZjM2FlSkRjbndJS3NyNEV3X1laUzgyaGdLUy1aZm93SW1Pb1NsZmpVUU5iMEdmUDNRWVhEM2VCRWl0ZjduNEZkS0dpU21GN19MWFRSdG5XLTdKTGJSbTRLdWZSRkxVUGR5Z2tSNGJTejlsa2R2VkZlcXc?oc=5>

### 12,302 Xylem Inc. $XYL Shares Sold by Robeco Institutional Asset Management B.V.
- Summary: Robeco sold 12,302 Xylem shares, indicating a short‑term market move.
- Date: 2026-10-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxNV3pvQmIxMEdWVURBNHQ3cXRobW9QVXc2Y2M3eXdJQ2JhQjNfa0lNTWhxdWdfZE1wOHlyLVkwdzQxYVpaeTlEZWNkR1dZakttT05FcWRCd2ZBZzdkWjZMVm8zZEtsSGFMTTFTLWFWaTJnQ0ozVWlHUEwyYVNVS1Nva3h4YlZwSHl5UzNoNW04OG9zRXhGNkZ2bVpsNWprRUNZVXBRUzBROFZsWnRhOFdEZWFxR0MyVmhSUkNiWWJFdGU0MHY4LWVteG92bmMyeWxENEE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **XYL** | **25.89** | **2.44** | **13.86** | **1.50** | **25,389,355,008.00 USD** | **-25.34** |
| AOS | 17.17 | 4.55 | 11.32 | -0.70 | 8,378,763,776.00 USD | -8.71 |
| PH | 30.92 | 7.21 | 21.05 | 9.80 | 111,050,809,344.00 USD | 15.88 |
| DOV | 23.24 | 3.47 | 14.32 | 7.50 | 26,828,300,288.00 USD | 11.05 |

Peers fetched as_of: 2026-10-25; XYL reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-28
- Next expected earnings: 2026-10-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-28
- Revenue (latest available single quarter): 2,336,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 263,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1524472/000152447226000110/xyl-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNT2pyX2NuUUNySVp2cWRGSURUS3NkenpBd2UxOFB0bXpWNXFSRWZIRHpERFlDcUJyamJoQnYzODdfT1B2SXBMYkRjT1RkZWwtSnoxMFNQbEU4eUJsdVJhVTFJYW15RVE1UUxxRUpPT0hUUDM3a1oyY0xkd1I0U2p3TUZuamQ1ZnpoYTUyb3k5aFNqdHFMUXlMMHRpZ3JfTm5ILXdDV0VVSXVaRG5TcVV0SDlMVVRQWmJKWFhnTkhoVHYxdw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQSFpqZmFkZlZSTEVNc0hkUjM3QU1yZnNQODdiY0tSUTktTk5MM2NlMmlKQWxER09EQnJlLUFONUhnLWhreG9qTFdUZ3VTTGdJZ3Q0cEpTSlBBbU5Id2w4UGkwUFlueWo3aEEzTDdWOWh2emZMa3g2dUkwM2ViVWl6Wkg5U1pGNm83aWtzb2hDMEF6OTN6cGNj?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNNDZrNHk3NjRqZGV5R0lNQzZMRVhTSjY0Ql9zSENTOHNaVTZoNkpTWDliRm92ZmlwUmFsR00yT2VRUnJfNm43a3hvQzctYnd2UTItbmpWYWo2R2FJZmxTMDFaNHlJdi1reVdXU1pXZjRnOXVBd0trSEZKcUdiamctM25Nd2ZMOUVDS01LelBrNzMzYWhWT3dCc0h1MWdUMnlNbGUxOWdrWGFDd1dFZDhJNmJXUmd0M2VSVFM5ZGd1VUxjTlk?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPNmQ0cERxaHY0VE5PUUJvVkVRVVlOdklJRW9NRVk0OVVRdE03WWN0cVpRcWNtdmdyM0VjdUdhZWMtblFTWndzeXIwVnk4b0Z0MWRnd0s0bmt4ajVuNXhRWG5CbFZxaVlPeWFrOVlYVWJqZUQyZTJlanFTRmhQYWpDX3R0YUhiOENBeklzZlU3aEk3aG5ud0E3YWMtSEdwMFdTeGoyZ05zNUFvZnc?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQOU1XSENBMUxISE5qLTAzbVZDa0Y1cnFjd2NGRS1SdnE5a3FjczdiSGNtR3haVDdscXFwcHZGaHF3dFl5cl9xd0EwNGozTm9reVY4enZzemplSmxSQ1dXb3c1MFdsaUR2NWhqdGZCZnd0UjZEMTN6R29KaTQtTWVsSjFjeUdiZkNDMElHOExtbDdrTFVnZkJER1BVREloY2RKbzVJLXpkb0M5bjJIcmRPYU5Uc05jZw?oc=5
- https://news.google.com/rss/articles/CBMiYkFVX3lxTE5MVzQ1OGIxcjZRQzBoeXFRRmdKTEF1alpmdlBwNS1ZT1FXMU9hX0psUWRFZFRDeDNEd0xhWjk4cDZyZGpDbW5Cb25JbGhLSUw1Y1NMX1pLdG1aMi00bHp6bC1n?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNaTZ2YmZJM2R3MUFBcEw1dEdsdnByZmxCREIyZTktRDVZNHV2VGUwTDdINHkzMHVSYkF0Q2hxcXJnaDFWc1RJTDBnMFRxQUtlUVNUNnpHaEgzZG4xa3hWWS1leFM1cUNRNzFDdnQ0UWNXbTViZGZKTDA1Zjd4UVRDOEx0V2VGclFNeU9najRQQkZKWXk1NkpvbW1tY2lpaFJybENMTlBJVnh5NmdBWHNmaFpQMjUzZFJTemc?oc=5
- https://news.google.com/rss/articles/CBMidkFVX3lxTE5xa2pia216MXpBQTd6Zzh4bnVLaWRtS213VDRqazJkZWpXWG5vRFhQeGdiazFJaW8ySUdGS2tUSzdSZUNDNHo2WVpYNHUwZHh3OTVXRnJrUk9KdE9qcXNjU1h5ZGQxQ01iUk1XOTNqQ01kVzJhNGc?oc=5
- https://news.google.com/rss/articles/CBMiYkFVX3lxTE9GLTFUMWl1cy1VNDhpWS1mdGEySFBFWW5HQVNpazVfYXpDb0VvT1Q1bVAtQUQ3Zm96U2QwaUV3eFdtVXpjWVNKa2ZRRE52OVQ4ZUlGT1l6UnZkVzZPMVlfeWZR?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPdGlCMjlZNzhBS08tY2RQUzNJdkZXYWRNMkk1LXQxLUNqUHR1NjBpRWJWaHJ4QnA4R3FPZ3A0VGRXcW11RnM3cEhnVlg1dHEtVGd2NEE3RTNkTXh0ejV5TkZkUHduck54TlJfYjM2eURnMnEyYTF2UVNGUDdFMjJKTlR0Sk1ud0VNV29RaUV1eDJ0T2dzUXJJUlBQU21XTmtjN1VNcGRNMXVaUm9kOF9GNHFla0VmWk3SAbwBQVVfeXFMTzRCbmplNW5UR0V6Mk9KakVCaE1PRlNraVkwS3U3aGJSZnZ3T2VmTXV4MWJHbVFyVE5VQjAyRmdfS1h4N2RQa3RKYlg1OVZzZmJrN3AyeHRHUzQxRGk5SG5KbWd1RlpkNlZPcWQxQXE2dUZzX1NhSF8wcE9udkdJSFhKdGJMemMyNWtLTnd0Qmt6NVZFWExOWnBmTlQyUmNibEt2YVFOYUFZalB0Vm9pTG56eV9WZVlPMzlPMWQ?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxNd24yalZEQUh5NWxfMDVsekU2NUhUZm5Md1ZzVmJ1N21WTWF3MS1rQjQwWUg4UDJHejYyeDZVUFRTdlNOVUUycDRnSks3R0xVRnV0MUxsaEpraFI5WkVBNVZwanRieHdsaWNvZHNhakRNSG9hNW93cndNeHFFWVVaR05PX182YXZJeU43T3VVc1R3VmFpcC00Z210bjlEVWRDZk5HcGxMcEZoVDJBTmNqbEVXaVlnZFdTS1RnUG1VSkJWdk1OcDY2WA?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNN1pLbVVDUWp0dkNHV0d4SmRsYUxVRzRmT0FOWUl4ay1ablRCV0NVbE55QzN6LXRQU21NN3IxWjhTMFBHY0J0N0ZjM2FlSkRjbndJS3NyNEV3X1laUzgyaGdLUy1aZm93SW1Pb1NsZmpVUU5iMEdmUDNRWVhEM2VCRWl0ZjduNEZkS0dpU21GN19MWFRSdG5XLTdKTGJSbTRLdWZSRkxVUGR5Z2tSNGJTejlsa2R2VkZlcXc?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxNV3pvQmIxMEdWVURBNHQ3cXRobW9QVXc2Y2M3eXdJQ2JhQjNfa0lNTWhxdWdfZE1wOHlyLVkwdzQxYVpaeTlEZWNkR1dZakttT05FcWRCd2ZBZzdkWjZMVm8zZEtsSGFMTTFTLWFWaTJnQ0ozVWlHUEwyYVNVS1Nva3h4YlZwSHl5UzNoNW04OG9zRXhGNkZ2bVpsNWprRUNZVXBRUzBROFZsWnRhOFdEZWFxR0MyVmhSUkNiWWJFdGU0MHY4LWVteG92bmMyeWxENEE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
