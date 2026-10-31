# ISRG Intelligence Report

- ticker: **ISRG**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/ISRG/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ISRG/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:23:11.553092+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 19, 'rule': 3, 'ai': 4, 'unknown': 0, 'irrelevant': 12})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/ISRG** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 19 unique headlines; 9 named publishers; 1 exact duplicates; 19 HTTPS source links; largest publisher share 31.58%; oldest publication 2026-10-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 432.0100 |
| Return 1D (%) | -3.7325 |
| Return 1W (%) | -4.4838 |
| Return 1M (%) | 6.2415 |
| Return YTD (%) | -23.7217 |
| Return 1Y (%) | -18.4918 |
| Annualized volatility (%) | 34.1412 |
| Beta vs SPY | 0.8943 |
| Max drawdown (%) | -43.9960 |
| Sharpe (rf=0) | -0.4281 |
| Downside deviation (rf=0, %) | 25.8340 |
| Sortino (rf=0) | -0.5657 |
| Historical VaR 95% (1D, %) | 2.9944 |
| Historical ES 95% (1D, %) | 5.1080 |
| Correlation vs SPY | 0.3350 |
| Tracking error vs SPY (%) | 32.1970 |
| P/E (trailing) | 52.24 |
| P/B | 9.37 |
| EV/EBITDA | 32.62 |
| Revenue growth (%) | 21.70 |
| Forward P/E (estimate) | 34.69 |
| Gross margin (%) | 66.64 |
| Operating margin (%) | 33.29 |
| Return on equity (%) | 17.93 |
| Free cash flow yield (%) | 2.25 |
| MA50 | 401.5432 |
| Close vs MA50 (%) | 7.5874 |
| MA200 | 433.0610 |
| Close vs MA200 (%) | -0.2427 |
| RSI (14, Wilder) | 54.1544 |
| MACD (12,26) | 12.0282 |
| MACD signal (9) | 12.6570 |
| MACD histogram | -0.6288 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ISRG': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 432.0100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.7325 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.4838 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.2415 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -23.7217 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -18.4918 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.1412 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.8340 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.5657 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9944 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1080 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3350 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.1970 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8943 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.9960 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.4281 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 34.6938 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.6420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.2860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.9320 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.2506 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 52.2382 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 54.1544 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.6288 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.5874 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.2427 -> Slightly below the moving-average trend level.

## TAILWINDS

### Intuitive Surgical (ISRG) Could Be 24% Above Fair Value As Earnings Split The Market
- Summary: Earnings suggest ISRG may be undervalued, indicating potential upside.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNSGxRNkt3UTdSSmFBX2wzamstRjdPamFrWHVmdmtQZ3R1bGRtUVRPWUFDRkJDSHFJQUpENzdzc2x0bUkyek1TWUN1TkNrY0ROdUI1QkdpMDdtWENqWUcxZjR3V2JQM1NqODlOTTkwMXdhSVRxV3NnMkJEYm1DZTF1bTlsci1sZkFuMzJjWjROa1AyZGZLOVVrSGJRd012azA4VWpxWm81cnhRM0g5RU1wblVWa1lMR3pqeXdsd1FYa3FHNGQyYmtiWWRMVlRlZkNKeF9TWjFR0gHbAUFVX3lxTE9kRDlUbzNEbmFlU0REd1E2bkFyQ3YxNzRScjlGbDYtR1NiSnh2TDJEcWdTelFpRXl6bkt6eFlzc0xxT011S2wzM191WU5wTEdfNGF4TnNTSGNxa1dLUlVHSURMNG13b3JZc0RDQzJtNlpLcDlyVUJZRVZ3MzZaQnJtZmEzeWFFd3NYSFluSE4yNXdDdFNMR2xpUTh6VEtDS1Y5YUhlbEpSQXZPZ2gtM0lEdUVCMGRTU1k2MEZyaWUxQk9pdmgyTU5LdEJpU3ZieWJsUkc1RXd2enhNaw?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Intuitive Surgical (ISRG) Insider Sale: EVP & Chief Manufacturin
- Summary: Intuitive Surgical (ISRG) Insider Sale: EVP & Chief Manufacturin
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxPOEVrd2NKanZZVXNSUnJRU3hKT1hpblVOc1hvM3B6SndZalUwTTBlZE1yWi1zOHdSTlBjU1FFZ2lCRUNwYWZEVUpPdzBzRkp3enBGMlpIQnRwcWtZWEQxSHJFOFJQX1hubTFjNW1iT3lkcjZBMVhXWkhTTU1wY2M2dXJLUGZkT0tkUHo2NE9zX2c4dzhvd01NS3dKM3daSXBUQ2RuZmtNSjJQaXI2ejFXQzVNR2VfWG15ZzZKMEx4RXJ1WEtuT01VSU5WLUI1a0x3dVFSeVh2Q09yQ3FuUGJ3WkkwTG1zZGdLMnc?oc=5>

### Intuitive Surgical (ISRG) Insider Sale: SVP Chief Human Resource
- Summary: Intuitive Surgical (ISRG) Insider Sale: SVP Chief Human Resource
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxQamx6UHcwVVd0Uno3aVhvcHc4c291YWl0N08wZlViSnFfYTRMTmFPa1VVcnlRd0lpREg4QVd2MXlHeDNNanpqQTF0eEdnTWVia3FoRUEwXzkwWFFFWGpDUFB3UGlWWmFCZC1Zd0FUZjdTcVlCcFRQSTFFdktYTmRMNW81SVhISmZVaHAxSWhSUnJMNUx2Wm5jckFhOGNsM2l4WG9LSXZOOXNXR2ExQnhQLWhrSjB0cEczQzlHYk5OaTRnSjJWcTB6Mzhtb2dKWl82d0hBVW85YTdGNEdrV0VGeVFtZkt0aEJHbDNR?oc=5>

### Intuitive Surgical, Inc. 2026 Q3 - Results - Earnings Call Presentation (NASDAQ:ISRG) 2026-10-23
- Summary: Intuitive Surgical, Inc. 2026 Q3 - Results - Earnings Call Presentation (NASDAQ:ISRG) 2026-10-23
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTmpjcE5OT1pBOXJ4aGFzZkhja3VhUi1TcV9tNEI0cUd1TVVUeHF1ZzlNczhHWUplMkZqQXhHNDBELVdXTVZXU24yaHRVRTVPa0JTQW9tZnRadXN1MGNVTWhrQU5zUFcwZ2JaRVZNbFNQcHhNdkpJX0tNRTRhRzNUNUJON2pzY01DQ2ZUMVRlZkVGMmNTdmFMZFRuM1hpelpWVDRzUHdGQjBRZw?oc=5>

### Intuitive Surgical Insider Sold Shares Worth $1,834,124, According to a Recent SEC Filing
- Summary: Insider sold shares worth $1.8M, reflecting ownership change.
- Date: 2026-10-26 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNWXBYLXU5eHRVeFphS2NhSXpOdXlfc2tldkhQZXRNVlMzTUFSM1VjNGRhU3lRbnJoZ2x6NUg0SVFwaV80cnVpcnlUVW56SGxrT2dQZkJjT1c1ZzNtcl9aVlBSQlJiM1UtQWdiOFBzNlVpSHpycVpfY1NCSlE0N2lsbUJUZGtmNGVSUWs2YzdmeVNLTGQySlliZktyX0NzVThMRTRtTDFFY3NwN25GbEFCdg?oc=5>

### An EVP sold 61 shares per sale under a trading plan at Intuitive Surgical (ISRG).
- Summary: EVP sold 61 shares under a trading plan, indicating insider activity.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNN2ZfRVV6SE1yX3g4WGw4a1kxdmZMTmZuWlAxRnd0ak5kd0k5TnQtWGlCU0E0UW1Hb2JtWTY3Slk3UmVzTGFoZVNwVEF3V1N5OUdLOWxwY0p3VWlyTkYxVWZUWnBOdXpneERzRXg0VHM5dUllZEFKZ3VjemVBRnl5T3JoZmJnQmtTRnpiTEN6eFZCc3N0WDYwV05TRkgzd3A4R3YwR1NfWnlhZ0wzZTNXQUhfck9lNVk?oc=5>

### After selling 20,095 shares, Intuitive Surgical (ISRG) director Gary S. Guthart's trust holds 1,204,530.
- Summary: Director sold 20,095 shares; trust retains 1.2M shares, showing insider ownership shift.
- Date: 2026-10-26 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPYkxQbk01d3gxbjRyR1F1aVpZODJ5Z1F3NFNPRUhFbnBjeWZ3Q3lONHctSXY1bE5hWGhlV0c5MEVoTXpMR01xRENuMHp4SHdnQlZJd0s5TTItaFh2R1F4TndKRjNPd1RjdVRVRzM5bHBfUkNvU2RCV1laS0lhUzRKSjFLbjRhQnpaOWpmVFpzWVVIbDNEaTEtM3pYUlFOeG9LY0hmV2hmTXl1X052MTRsOGhQWGpycWs?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ISRG** | **52.24** | **9.37** | **32.62** | **21.70** | **152,619,646,976.00 USD** | **-18.49** |
| MDT | 23.72 | 2.46 | 13.78 | 13.70 | 123,487,977,472.00 USD | 9.64 |
| SYK | 30.24 | 4.98 | 17.84 | 9.40 | 111,949,627,392.00 USD | -20.02 |
| BSX | 17.71 | 2.44 | 12.85 | 1.40 | 60,838,658,048.00 USD | -58.26 |

Peers fetched as_of: 2026-10-30; ISRG reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 3,048,700,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 522,800,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1035267/000103526726000071/isrg-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNSGxRNkt3UTdSSmFBX2wzamstRjdPamFrWHVmdmtQZ3R1bGRtUVRPWUFDRkJDSHFJQUpENzdzc2x0bUkyek1TWUN1TkNrY0ROdUI1QkdpMDdtWENqWUcxZjR3V2JQM1NqODlOTTkwMXdhSVRxV3NnMkJEYm1DZTF1bTlsci1sZkFuMzJjWjROa1AyZGZLOVVrSGJRd012azA4VWpxWm81cnhRM0g5RU1wblVWa1lMR3pqeXdsd1FYa3FHNGQyYmtiWWRMVlRlZkNKeF9TWjFR0gHbAUFVX3lxTE9kRDlUbzNEbmFlU0REd1E2bkFyQ3YxNzRScjlGbDYtR1NiSnh2TDJEcWdTelFpRXl6bkt6eFlzc0xxT011S2wzM191WU5wTEdfNGF4TnNTSGNxa1dLUlVHSURMNG13b3JZc0RDQzJtNlpLcDlyVUJZRVZ3MzZaQnJtZmEzeWFFd3NYSFluSE4yNXdDdFNMR2xpUTh6VEtDS1Y5YUhlbEpSQXZPZ2gtM0lEdUVCMGRTU1k2MEZyaWUxQk9pdmgyTU5LdEJpU3ZieWJsUkc1RXd2enhNaw?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxPOEVrd2NKanZZVXNSUnJRU3hKT1hpblVOc1hvM3B6SndZalUwTTBlZE1yWi1zOHdSTlBjU1FFZ2lCRUNwYWZEVUpPdzBzRkp3enBGMlpIQnRwcWtZWEQxSHJFOFJQX1hubTFjNW1iT3lkcjZBMVhXWkhTTU1wY2M2dXJLUGZkT0tkUHo2NE9zX2c4dzhvd01NS3dKM3daSXBUQ2RuZmtNSjJQaXI2ejFXQzVNR2VfWG15ZzZKMEx4RXJ1WEtuT01VSU5WLUI1a0x3dVFSeVh2Q09yQ3FuUGJ3WkkwTG1zZGdLMnc?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxQamx6UHcwVVd0Uno3aVhvcHc4c291YWl0N08wZlViSnFfYTRMTmFPa1VVcnlRd0lpREg4QVd2MXlHeDNNanpqQTF0eEdnTWVia3FoRUEwXzkwWFFFWGpDUFB3UGlWWmFCZC1Zd0FUZjdTcVlCcFRQSTFFdktYTmRMNW81SVhISmZVaHAxSWhSUnJMNUx2Wm5jckFhOGNsM2l4WG9LSXZOOXNXR2ExQnhQLWhrSjB0cEczQzlHYk5OaTRnSjJWcTB6Mzhtb2dKWl82d0hBVW85YTdGNEdrV0VGeVFtZkt0aEJHbDNR?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTmpjcE5OT1pBOXJ4aGFzZkhja3VhUi1TcV9tNEI0cUd1TVVUeHF1ZzlNczhHWUplMkZqQXhHNDBELVdXTVZXU24yaHRVRTVPa0JTQW9tZnRadXN1MGNVTWhrQU5zUFcwZ2JaRVZNbFNQcHhNdkpJX0tNRTRhRzNUNUJON2pzY01DQ2ZUMVRlZkVGMmNTdmFMZFRuM1hpelpWVDRzUHdGQjBRZw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNWXBYLXU5eHRVeFphS2NhSXpOdXlfc2tldkhQZXRNVlMzTUFSM1VjNGRhU3lRbnJoZ2x6NUg0SVFwaV80cnVpcnlUVW56SGxrT2dQZkJjT1c1ZzNtcl9aVlBSQlJiM1UtQWdiOFBzNlVpSHpycVpfY1NCSlE0N2lsbUJUZGtmNGVSUWs2YzdmeVNLTGQySlliZktyX0NzVThMRTRtTDFFY3NwN25GbEFCdg?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNN2ZfRVV6SE1yX3g4WGw4a1kxdmZMTmZuWlAxRnd0ak5kd0k5TnQtWGlCU0E0UW1Hb2JtWTY3Slk3UmVzTGFoZVNwVEF3V1N5OUdLOWxwY0p3VWlyTkYxVWZUWnBOdXpneERzRXg0VHM5dUllZEFKZ3VjemVBRnl5T3JoZmJnQmtTRnpiTEN6eFZCc3N0WDYwV05TRkgzd3A4R3YwR1NfWnlhZ0wzZTNXQUhfck9lNVk?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPYkxQbk01d3gxbjRyR1F1aVpZODJ5Z1F3NFNPRUhFbnBjeWZ3Q3lONHctSXY1bE5hWGhlV0c5MEVoTXpMR01xRENuMHp4SHdnQlZJd0s5TTItaFh2R1F4TndKRjNPd1RjdVRVRzM5bHBfUkNvU2RCV1laS0lhUzRKSjFLbjRhQnpaOWpmVFpzWVVIbDNEaTEtM3pYUlFOeG9LY0hmV2hmTXl1X052MTRsOGhQWGpycWs?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
