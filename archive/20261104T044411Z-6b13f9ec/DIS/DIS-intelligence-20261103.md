# DIS Intelligence Report

- ticker: **DIS**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/DIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/DIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T04:55:51.391302+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 3, 'ai': 13, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/DIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 12 named publishers; 1 exact duplicates; 22 HTTPS source links; largest publisher share 27.27%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 114.1800 |
| Return 1D (%) | 0.9460 |
| Return 1W (%) | 3.5834 |
| Return 1M (%) | 11.7330 |
| Return YTD (%) | 1.1294 |
| Return 1Y (%) | 3.3119 |
| Annualized volatility (%) | 26.9824 |
| Beta vs SPY | 0.6070 |
| Max drawdown (%) | -20.2451 |
| Sharpe (rf=0) | 0.2562 |
| Downside deviation (rf=0, %) | 19.2130 |
| Sortino (rf=0) | 0.3598 |
| Historical VaR 95% (1D, %) | 2.4075 |
| Historical ES 95% (1D, %) | 3.7715 |
| Correlation vs SPY | 0.2879 |
| Tracking error vs SPY (%) | 26.3247 |
| P/E (trailing) | 23.54 |
| P/B | 1.80 |
| EV/EBITDA | 11.68 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 15.23 |
| Gross margin (%) | 37.59 |
| Operating margin (%) | 19.30 |
| Return on equity (%) | 8.01 |
| Free cash flow yield (%) | 2.47 |
| MA50 | 107.5326 |
| Close vs MA50 (%) | 6.1818 |
| MA200 | 103.0349 |
| Close vs MA200 (%) | 10.8168 |
| RSI (14, Wilder) | 66.3256 |
| MACD (12,26) | 1.6763 |
| MACD signal (9) | 1.5079 |
| MACD histogram | 0.1684 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'DIS': 274, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 114.1800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.9460 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.5834 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 11.7330 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 1.1294 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.3119 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 26.9824 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.2130 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3598 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4075 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.7715 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2879 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.3247 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6070 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2451 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2562 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.2276 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 37.5950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 19.3010 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.0100 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.4653 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 23.5423 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 66.3256 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1684 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.1818 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 10.8168 -> Clearly above the moving-average trend level.

## TAILWINDS

### DIS Stock Ticks Higher Overnight: Disney Reportedly Weighs Thousands Of Job Cuts In Fresh Cost-Cutting Push Under Josh D’Amaro
- Summary: DIS Stock Ticks Higher Overnight: Disney Reportedly Weighs Thousands Of Job Cuts In Fresh Cost-Cutting Push Under Josh D’Amaro
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAJBVV95cUxQaWlHVGdFRHF1VGhjU0doMFhUbjlrbmEtSjhHekdzSUVsYVdJSVlRVV91bGhkbS1yRUtDX3lPanZ2V1ZUanRsUkJvRDdkYThxQ1dZakZWVTg1eXRvOFZGZ0ZCczBUd2JPQXluRlJGYlNCNEd4YlZTQi1kcVhyQlQwMnM5dFZnN2RVaUVlQ2NBZTRWblVtdEU4TjMwdmRnNkpyTm1DLTVoM3NGN2tIMjBaNnJKQ0doWkpaY1ZLbjFCZWVIY2ZqVGJIUHZ0blBuSng1Q3NES01xUTJ0YVNHRnBiSko4NmU3X05GaGtqTGdCdldDbzhGclhnV05YY2dYOXlkOHhqTUtGcjB2SGNicllYYk4wd3h3ZElo?oc=5>

### DIS Stock Analysis: Gains 1.96%, Testing Key Resistance
- Summary: DIS Stock Analysis: Gains 1.96%, Testing Key Resistance
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOYkwxSzlXVTBMLTJDUUtMSWhYRURhNXFsSXhfbkQ5bmotQmh4YjEwNTM1YXlueGQtUXFWMFRCMXN6TVhjTi1sSXMwSnZOWUh4R0I1eDBaeEtFbTFJV1MxZ1BaU2ZQRVhEMEEydTVrc1lidktrZ1VyMFQ1QVk0ZjhBRFdrb1M2QnZQdlpmdElRcDBWVHNTWmc?oc=5>

### Why Walt Disney (DIS) Outpaced the Stock Market Today
- Summary: Disney's stock outperformed the market, indicating strong investor confidence.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNeVFCRE1aZ21KUEViRGJxdkd6Ni1pY3pOTGV1RnBTRks0dEVGMVN4bWlSWUFLdHZJdzBJZ1ZucFdvTWVvUWgtSGJET2hhUFd1LXhRallxT1NaRlFXS2tCcVFveWNsNXAtU3kyOXVFd1k5Q3hRSG03WEt5ay1JLU5YUUlEanE0dlZjOWh4N25rZS12Wkc0NkUzZw?oc=5>

### Disney Just Gained 9% in a Month: Take Profits, or Buy More?
- Summary: Disney's share price rose 9% over the month, reflecting positive market sentiment.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxOUWJyWmNramVOTllpM1RzVWduX0RWLUZ1dHRSQWViLUtPdzVoMzg4RXg3QTNGbnhpTXZfS0c0ZTNDUVVBWnQ0T3JPMXJhZ0VBZlRkZm1jQWs3U3NyQ1JtWXc5V0FZWmYwb3lUeDhZMWpkMGs2NUVCMjhlQWNMTExoaVFIWQ?oc=5>

## HEADWINDS

### Disney targets up to 20% in cost savings, including job cuts – report (DIS:NYSE)
- Summary: Disney plans cost cuts up to 20%, involving job reductions.
- Date: 2026-11-03 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOM1NkdXQ0aVp1RnYtSlQ4cmswbi11MzJqazIzaDdkeDFIWEM2cGVreTFMRDQ4TkxRZGFpSXBlcjRNbmYzS3NCcW85R0pDS3NMZW9jVzltLTl5NlU2cmFTQmJoMFpsREUzd2JOVk9ONnhyWkh6YTNtTWJ3SGh5MjdvbVM2UVlWbFIxRHNDWFFuZmhOQnh6NXpyNXVmRnJpSjBNeTZZSHh3?oc=5>

### Disney (DIS) Prepares Major Staff Cuts Amid Cost-Cutting Drive
- Summary: Disney plans significant staff reductions to cut costs, impacting operations and employee morale.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOWXpzdlFjOEN1QU9vaDYwNWVmWkJTMWJBVjJCTVlXM0lIMzE0ZGZ2NzFrV3dzTGNDbU5vNkZKRndHWjdtNE5IU0NfYXcxYl9TM0YwMjRkaG1aMzBzNnZBWkFDU3hJY0hUcEdjcUpnLWFrMmp3bF9wX1FfMTJFTDc1aXdIVG9iaHBBMFBJN1ZQT0tmMWY5MWdzZmw3YThBdVU?oc=5>

## CATALYSTS

### Walt Disney Earnings Preview: What to Expect
- Summary: Walt Disney Earnings Preview: What to Expect
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQMldKcDFFX2poOGxTdDBWdGEwSS1tRlI0NUVGaHYtNlVIazlqMFVTempwSlBpbV9uR2sxZDhOTzlKX3cxRFhldjFFa3FNc2d5M0dpdE9YX1hpeFZCWHQ3SGg5NFNpek5fSHBkUDdtWWJLVjUzVGJJWXU5LVZGMEtISmlJbkVoczMzbXl6Yk5wZ0U5dl9RSTlkNGZHVlAyTHliSXc?oc=5>

### How Much Upside Is Left In Disney Stock?
- Summary: Analysis of potential upside in Disney shares, considering current valuation and future prospects.
- Date: 2026-10-27 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQRkwzeUFCNXMtMzV6T2hVRXVmYVhhWVlfbnRUbHJQY1RHcHU4M1Bvd05fQ1hOV1hWVmFhcFV4bkRWY3hDZmdKOHUzWW5mYjZ5RVBkdGtHM1hDejkzc1I5STZBb1RRNjQzd0ZFN1RUa2hEWXdhcHVRTV81azZlVlJYMzRMZ0YzQTdWOW0zV2hPaldXQVlPSnd3OGVUbThvcC1t?oc=5>

### Disney Stock Forecast: DIS Guidance, Valuation and Risks
- Summary: Analysts discuss Disney’s future guidance, valuation metrics, and potential risks affecting the stock.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMidkFVX3lxTE41dUpLLXdRYk5Sel80Nll3NDdzZS1YZElydlhZbHd5ZUlSQVFxZVZtdE9RUGtMajg5X2pBUWNaZzFQZ3VFQlhja2lJR2l5bUJQT1pBbnB4WWx3aXJaU0tURVo0VzY1SjdJZzFHNjhJUEhwSnJIWEE?oc=5>

### Disney (DIS) and WWE Launch John Cena Classic Event at ESPN Comp
- Summary: Disney partners with WWE for a new event featuring John Cena.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQZkNOWmdYM0xPeFNhQ1FaVURLcGwzUFhOcmN1alFHdDFTNVNNWU1kV21wazYzTFk3SEVrZ3p0cnVwajVOZzJJZl8tRk5wcnN0OFY0VWZtTzRzSng0ZTFmczhneGFFbHE3TlJxUVpja0F5Z3N6VmM3TzFSZzFtbXNSTHk5Y0tsd09QRy1SaUZYZmE1SXd3RmRZdFNkOFd5NWhOU1MtSEZJSQ?oc=5>

### A new Disney-WWE mashup has John Cena and the new Avengers movie working in tandem (DIS:NYSE)
- Summary: Disney collaborates with WWE and Avengers for a joint promotion featuring John Cena.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNQzhET2J5Qm5WbjlETllEMzBudlFiYVNoUnF2SUl6YzlLbW9YQlBwNndLLTMxalE2bmxQeENPNkVEUUNncjB1WGtaM3NiQ082UnJoSXRpM2Ntc1ZpUWZPb3JhTEVHeW1NTms4amE0ZWtuSElPN1RPaTFUeWQwWlVUWG1oMEtLeEJib2VSN0d6d1Vjakw0NWNJQ1FmQWZmcThKOXNXMGxidVhSNlFRTHM1M1JuMDNwLV9MMnJFQQ?oc=5>

### Walt Disney (DIS) Bids For Character.AI, Is The 13% Discount Enough?
- Summary: Disney bids to acquire Character.AI at a 13% discount.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPQ3gxelZ2T29IdUFpdHVkZ0pMdGFWX0ZpRnlUcWJKczduQXl6N2JwQTM1M2wtc3VlQ3BaNVRZZjRHUmQ4dll6V0FBVlU2ZG5VYWdNNkxQa01BU2w0TVJpNDRobjZCN1VpQ3lMOUpuXzRub0Y5OFpTMEZJd0pCYUNDdnFHZGNzck9TM3d4UEJ4WXF3VWozR1JUZWtHOA?oc=5>

### Is Wall Street Bullish or Bearish on Walt Disney Stock?
- Summary: Market sentiment toward Disney stock is questioned.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPOGY5TVhmTGFlbzZYUXZpXzdpSTNmSXVhdFpid2dUbnMyV3JSQjh4cmtFbV9SdFBlOTAtVzZtWS1sdlV4dWNtUXZsUFNrMkNhdmFJU2dpakRua0xBZEN4emt0Yy0zN3FObnRTVW9xUlhOV3lDaW1ENWduc3dOMWpfajd6Q28tSUE3M0dLVTI5blhrazlZeDVGVVNhWnp3dw?oc=5>

### Disney Targets Thousands of Jobs in Fresh Cost-Cutting Blitz: Report
- Summary: Disney plans massive layoffs to cut costs, targeting thousands of jobs across the company.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQalFuV2FLS0xzQ3pQdjVtNE1qWXo4UUh6QUx5MkdqaDZXTjNaajN5ZC14WDRyOFFwVHZjSC1uSUhoODNiajRYeFItTGVzc2Q4UkliVTJHSkU2dEFMeENhZzNyMnRkdlNfWlVFVU00dzdJWjRvY0xJdDVSZl85ZHRIaGI5aVVhU0FocGIyb1gxMWtkclYtdG1LUjEwRVBUcmFSdXVXRl94RFl0QmJtdTl0TkZkWVRCQ1FnU1h3RWRXUVh0S0U?oc=5>

### Disney Eyes Thousands of Layoffs, With Managers Asked to Cut 20%
- Summary: Disney seeks to reduce workforce by thousands, asking managers to cut 20% of staff.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxONy1ueVhiMS1RaHJGNUlaZGpPaFlxR3lhd0xBN0o5SFctdk1sVFpQZmN6dnVoa3ZlamhnM0RHbzBaQi0xZ0dIZTdidTZQS0Z5ZFpHN0xlRGJMdlJEQllFV2ZoSmFSVzg4a1NQNjE4ZVN2STF2UzZacWJxeTluN3ZDaUJpZHVBaE15MFhyWTE1SWxvakZvSXNuLVJyVU80ejR4anRsUXpyZnNLdw?oc=5>

## RISKS

### Walt Disney (DIS) Stock Drops Despite Market Gains: Important Facts to Note
- Summary: Disney shares fell amid broader market gains, indicating investor concern over recent performance.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOYlBMWmx5TjRucnVzN1dpOVN4dG9wRFJFdEF0NHRkX1FhMnpLVmpiai1oTXI4VUtTSXdrdmF1N2gzQjZDX3l6UjJKb2U5M3V4NDcxNEJFdVVYTF8ySkJxZkY1ZEtrNmdoQXBhVXlLTDFIY2dMcmdoN19XVE5UVHBsbUN3N3NKLTJOdGF5ZWxJOGVoYWVldVI4?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **DIS** | **23.54** | **1.80** | **11.68** | **6.80** | **197,153,112,064.00 USD** | **3.31** |
| NFLX | 18.02 | 8.89 | 16.90 | 11.80 | 264,077,033,472.00 USD | -42.35 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| PSKY | N/A | 0.93 | 7.95 | 0.90 | 10,992,190,464.00 USD | N/A |

Peers fetched as_of: 2026-11-03; DIS reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-05
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMimAJBVV95cUxQaWlHVGdFRHF1VGhjU0doMFhUbjlrbmEtSjhHekdzSUVsYVdJSVlRVV91bGhkbS1yRUtDX3lPanZ2V1ZUanRsUkJvRDdkYThxQ1dZakZWVTg1eXRvOFZGZ0ZCczBUd2JPQXluRlJGYlNCNEd4YlZTQi1kcVhyQlQwMnM5dFZnN2RVaUVlQ2NBZTRWblVtdEU4TjMwdmRnNkpyTm1DLTVoM3NGN2tIMjBaNnJKQ0doWkpaY1ZLbjFCZWVIY2ZqVGJIUHZ0blBuSng1Q3NES01xUTJ0YVNHRnBiSko4NmU3X05GaGtqTGdCdldDbzhGclhnV05YY2dYOXlkOHhqTUtGcjB2SGNicllYYk4wd3h3ZElo?oc=5
- https://news.google.com/rss/articles/CBMilAJBVV95cUxPaWY3UnlMcVRlWlRhQWxtdDhBTkg1RExvSkE4R0Z1T2xWVFVCWGlYamxKVnhWa0FVVUdua2RLWVdLbkRadjBWa3pOcXozNzdMUWhsTFprVHdDODBFaGY0OVlFNHVkdGtMT0xFQXlucENTeEw0LUQ0S3dVRTVsdzliV21aeTY2OXVoOGlIYWtLLVFzdy1JcHl1OG9VVDZReE9QZm00WjJ0MC1menJpaDNDVGM4djBYRlc5MnZMdDBBbENqNDctZ2xRT2lrOTNpd0ZYNFZNR2ZXbDRxY1BScm10X0RUb05FaF81VnhqTENGTjBxR1JTM3Vrc0RSRnBZeEVtdVlnRjZJZ05jMUthcGI1U3c4YTA?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOYkwxSzlXVTBMLTJDUUtMSWhYRURhNXFsSXhfbkQ5bmotQmh4YjEwNTM1YXlueGQtUXFWMFRCMXN6TVhjTi1sSXMwSnZOWUh4R0I1eDBaeEtFbTFJV1MxZ1BaU2ZQRVhEMEEydTVrc1lidktrZ1VyMFQ1QVk0ZjhBRFdrb1M2QnZQdlpmdElRcDBWVHNTWmc?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNeVFCRE1aZ21KUEViRGJxdkd6Ni1pY3pOTGV1RnBTRks0dEVGMVN4bWlSWUFLdHZJdzBJZ1ZucFdvTWVvUWgtSGJET2hhUFd1LXhRallxT1NaRlFXS2tCcVFveWNsNXAtU3kyOXVFd1k5Q3hRSG03WEt5ay1JLU5YUUlEanE0dlZjOWh4N25rZS12Wkc0NkUzZw?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxOUWJyWmNramVOTllpM1RzVWduX0RWLUZ1dHRSQWViLUtPdzVoMzg4RXg3QTNGbnhpTXZfS0c0ZTNDUVVBWnQ0T3JPMXJhZ0VBZlRkZm1jQWs3U3NyQ1JtWXc5V0FZWmYwb3lUeDhZMWpkMGs2NUVCMjhlQWNMTExoaVFIWQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOM1NkdXQ0aVp1RnYtSlQ4cmswbi11MzJqazIzaDdkeDFIWEM2cGVreTFMRDQ4TkxRZGFpSXBlcjRNbmYzS3NCcW85R0pDS3NMZW9jVzltLTl5NlU2cmFTQmJoMFpsREUzd2JOVk9ONnhyWkh6YTNtTWJ3SGh5MjdvbVM2UVlWbFIxRHNDWFFuZmhOQnh6NXpyNXVmRnJpSjBNeTZZSHh3?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOWXpzdlFjOEN1QU9vaDYwNWVmWkJTMWJBVjJCTVlXM0lIMzE0ZGZ2NzFrV3dzTGNDbU5vNkZKRndHWjdtNE5IU0NfYXcxYl9TM0YwMjRkaG1aMzBzNnZBWkFDU3hJY0hUcEdjcUpnLWFrMmp3bF9wX1FfMTJFTDc1aXdIVG9iaHBBMFBJN1ZQT0tmMWY5MWdzZmw3YThBdVU?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQMldKcDFFX2poOGxTdDBWdGEwSS1tRlI0NUVGaHYtNlVIazlqMFVTempwSlBpbV9uR2sxZDhOTzlKX3cxRFhldjFFa3FNc2d5M0dpdE9YX1hpeFZCWHQ3SGg5NFNpek5fSHBkUDdtWWJLVjUzVGJJWXU5LVZGMEtISmlJbkVoczMzbXl6Yk5wZ0U5dl9RSTlkNGZHVlAyTHliSXc?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQRkwzeUFCNXMtMzV6T2hVRXVmYVhhWVlfbnRUbHJQY1RHcHU4M1Bvd05fQ1hOV1hWVmFhcFV4bkRWY3hDZmdKOHUzWW5mYjZ5RVBkdGtHM1hDejkzc1I5STZBb1RRNjQzd0ZFN1RUa2hEWXdhcHVRTV81azZlVlJYMzRMZ0YzQTdWOW0zV2hPaldXQVlPSnd3OGVUbThvcC1t?oc=5
- https://news.google.com/rss/articles/CBMidkFVX3lxTE41dUpLLXdRYk5Sel80Nll3NDdzZS1YZElydlhZbHd5ZUlSQVFxZVZtdE9RUGtMajg5X2pBUWNaZzFQZ3VFQlhja2lJR2l5bUJQT1pBbnB4WWx3aXJaU0tURVo0VzY1SjdJZzFHNjhJUEhwSnJIWEE?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQZkNOWmdYM0xPeFNhQ1FaVURLcGwzUFhOcmN1alFHdDFTNVNNWU1kV21wazYzTFk3SEVrZ3p0cnVwajVOZzJJZl8tRk5wcnN0OFY0VWZtTzRzSng0ZTFmczhneGFFbHE3TlJxUVpja0F5Z3N6VmM3TzFSZzFtbXNSTHk5Y0tsd09QRy1SaUZYZmE1SXd3RmRZdFNkOFd5NWhOU1MtSEZJSQ?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNQzhET2J5Qm5WbjlETllEMzBudlFiYVNoUnF2SUl6YzlLbW9YQlBwNndLLTMxalE2bmxQeENPNkVEUUNncjB1WGtaM3NiQ082UnJoSXRpM2Ntc1ZpUWZPb3JhTEVHeW1NTms4amE0ZWtuSElPN1RPaTFUeWQwWlVUWG1oMEtLeEJib2VSN0d6d1Vjakw0NWNJQ1FmQWZmcThKOXNXMGxidVhSNlFRTHM1M1JuMDNwLV9MMnJFQQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPQ3gxelZ2T29IdUFpdHVkZ0pMdGFWX0ZpRnlUcWJKczduQXl6N2JwQTM1M2wtc3VlQ3BaNVRZZjRHUmQ4dll6V0FBVlU2ZG5VYWdNNkxQa01BU2w0TVJpNDRobjZCN1VpQ3lMOUpuXzRub0Y5OFpTMEZJd0pCYUNDdnFHZGNzck9TM3d4UEJ4WXF3VWozR1JUZWtHOA?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPOGY5TVhmTGFlbzZYUXZpXzdpSTNmSXVhdFpid2dUbnMyV3JSQjh4cmtFbV9SdFBlOTAtVzZtWS1sdlV4dWNtUXZsUFNrMkNhdmFJU2dpakRua0xBZEN4emt0Yy0zN3FObnRTVW9xUlhOV3lDaW1ENWduc3dOMWpfajd6Q28tSUE3M0dLVTI5blhrazlZeDVGVVNhWnp3dw?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQalFuV2FLS0xzQ3pQdjVtNE1qWXo4UUh6QUx5MkdqaDZXTjNaajN5ZC14WDRyOFFwVHZjSC1uSUhoODNiajRYeFItTGVzc2Q4UkliVTJHSkU2dEFMeENhZzNyMnRkdlNfWlVFVU00dzdJWjRvY0xJdDVSZl85ZHRIaGI5aVVhU0FocGIyb1gxMWtkclYtdG1LUjEwRVBUcmFSdXVXRl94RFl0QmJtdTl0TkZkWVRCQ1FnU1h3RWRXUVh0S0U?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxONy1ueVhiMS1RaHJGNUlaZGpPaFlxR3lhd0xBN0o5SFctdk1sVFpQZmN6dnVoa3ZlamhnM0RHbzBaQi0xZ0dIZTdidTZQS0Z5ZFpHN0xlRGJMdlJEQllFV2ZoSmFSVzg4a1NQNjE4ZVN2STF2UzZacWJxeTluN3ZDaUJpZHVBaE15MFhyWTE1SWxvakZvSXNuLVJyVU80ejR4anRsUXpyZnNLdw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOYlBMWmx5TjRucnVzN1dpOVN4dG9wRFJFdEF0NHRkX1FhMnpLVmpiai1oTXI4VUtTSXdrdmF1N2gzQjZDX3l6UjJKb2U5M3V4NDcxNEJFdVVYTF8ySkJxZkY1ZEtrNmdoQXBhVXlLTDFIY2dMcmdoN19XVE5UVHBsbUN3N3NKLTJOdGF5ZWxJOGVoYWVldVI4?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
