# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T05:12:32.970147+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 5, 'ai': 10, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/AMZN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 10 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 266.6600 |
| Return 1D (%) | -0.2917 |
| Return 1W (%) | 2.8384 |
| Return 1M (%) | 3.1248 |
| Return YTD (%) | 15.5272 |
| Return 1Y (%) | 12.2401 |
| Annualized volatility (%) | 33.8859 |
| Beta vs SPY | 1.3210 |
| Max drawdown (%) | -19.6419 |
| Sharpe (rf=0) | 0.5077 |
| Downside deviation (rf=0, %) | 20.8312 |
| Sortino (rf=0) | 0.8259 |
| Historical VaR 95% (1D, %) | 2.8374 |
| Historical ES 95% (1D, %) | 4.0742 |
| Correlation vs SPY | 0.5315 |
| Tracking error vs SPY (%) | 29.0356 |
| P/E (trailing) | 21.63 |
| P/B | 4.70 |
| EV/EBITDA | 16.73 |
| Revenue growth (%) | 12.10 |
| Forward P/E (estimate) | 24.42 |
| Gross margin (%) | 51.37 |
| Operating margin (%) | 13.09 |
| Return on equity (%) | 27.42 |
| Free cash flow yield (%) | -1.20 |
| MA50 | 254.8116 |
| Close vs MA50 (%) | 4.6499 |
| MA200 | 244.5955 |
| Close vs MA200 (%) | 9.0208 |
| RSI (14, Wilder) | 57.4345 |
| MACD (12,26) | 3.5019 |
| MACD signal (9) | 1.7996 |
| MACD histogram | 1.7023 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 266.6600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.2917 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.8384 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.1248 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 15.5272 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 12.2401 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.8859 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.8312 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8259 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8374 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.0742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5315 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.0356 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3210 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.6419 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5077 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.4211 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.3740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.0870 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.4160 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -1.2045 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.6269 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.4345 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.7023 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.6499 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.0208 -> Clearly above the moving-average trend level.

## TAILWINDS

### Amazon Stock Climbs: What's Going On?
- Summary: Amazon Stock Climbs: What's Going On?
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQR1FCaUQxM2w1M2hHM2U5STZ0Z2lQV05iVnBma3NFZ2JZVUUyRjJwd3lfN056VUR5X2ZYSlpGTjRiM3J2SllHUFkxRkZ1Qm9aM1diSzJpd2kyeUtrSTVsd3RfTlRIVEhzTWtDU0dSVG1HeGpXVk9NZ3hIRTFlU3RWQWhuU25EOHRaamYxUUZFTG1ncUtjNlRsRGxYcw?oc=5>

### Amazon's Earnings Made Me Bullish But Not A Buyer (NASDAQ:AMZN)
- Summary: Amazon's Earnings Made Me Bullish But Not A Buyer (NASDAQ:AMZN)
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxONWZER29tTDNsRkVSZ2hGNHhTcjBWM2tXS0QyQ2VfeGtLbDh4SHZlSUtEYk80UnZkV280bHF3a21zMldIUEd3WHBTNmNIbXBlSXdDeXpHUG9EQzZrSkp0R0MxNnE2aS14U1lGdElRbEJ4a0JJZW1taG92S0tncnhsVHNQRXFNRHFGc2VWeEFqWEY3TDA?oc=5>

### Amazon: Still Priced Well Below The Promises (NASDAQ:AMZN)
- Summary: Amazon stock appears undervalued relative to expectations.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNdHRhZ296anBFQ2FLWVU5TkVZWkV6OGdSYXNkSWItQUF1WDZoZVNaOWROa0hPZ0pBMUJ5U0VCN2dVVm53eDJIQU1ENTVoNS1Sb3RjU0FQSkoybmIzTXd2bnFRaS1RQ2JXT2ZLZ0xuTDVtU0o5THNfMUtHX3VnLWRCeU5MYUR1bFQ3dXpNNQ?oc=5>

### AWS Will Keep Amazon Profitable For Years To Come
- Summary: AWS continues to drive Amazon’s profitability into the future.
- Date: 2026-11-12 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQVVNPUTA5NDJDMWlEOTdhaXlNZ3NsTzRWT1RJQkJQQmhEZjRyN0VoV082blR5VEh5dzNEWkFvU2pTTFhrUEk0cG1KWExNaTh4dEE1R1lhZTVGWkVIb1pQMjF0ZjFDRnZ1WTNROTZhYWlaMDhLZzZqQXR1VlFlV1ZMOWs3cWVkVVlwMG9maUhoUTRqbmVZ?oc=5>

## HEADWINDS

### Amazon Stock (AMZN) Slips Despite Updates to Alexa for a Better Shopping Experience
- Summary: Amazon Stock (AMZN) Slips Despite Updates to Alexa for a Better Shopping Experience
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNVi13aUZWMjBmYXlob3AtTFVZRDFPS0o5bzQ0Y1JpcEktM2VnNHhjY19SaENpY0p4QU9OY3JVa2tjMGJ0el9oamR6dFMwYlY1dTBoMDNWakF0Nk41VmpKVGEzR3p2bFRrQXNaSWplTXQ2MUNUclZFY3pmNzRpYUIwdldFbnNmR2o3SFQwZXJWMW1Qb00zQjZPZm5jQ3FYSU5obTRsTEZFWW1xVW5yM240Mw?oc=5>

### Amazon.com, Inc. (AMZN) Sold Off After AWS Growth Accelerated: What Changed?
- Summary: Amazon stock fell after accelerated AWS growth, indicating potential concerns.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNT2w3Um9jU09tYUlBRXFqYXZkZ3NxbG9Mb2k0ZnA0X0lZR2hlNFZONHJqZzg4aGoxbGJ4TUNLOGhPZUVOZzBuek9JTXlGWjVmbFZpLWFuNXFPU0dMd3ZfaGFTaWt0TDNqWF9OQ1FMMFN3U3h5dTlJUUZVVnE2NWUtdkVTSU85WjVmcVA2YktRNDdDdWc?oc=5>

## CATALYSTS

### Amazon Has Quietly Recouped Its Post Q3 Earnings Losses. AMZN Stock Could Hit $300 Next.
- Summary: Amazon Has Quietly Recouped Its Post Q3 Earnings Losses. AMZN Stock Could Hit $300 Next.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxNVDFMMWpzTHFWNVpraFphOVZad0Rza2psdnFrb3UwU2FES3JEZ2VaNHNudE80T2NOejIwTDJUaXJBMFdFSzNQZjFNYXZmc2tucTlPUXFobVpRLUJva2lGb0ItbVR1SkktLWhuaXRaUDA2VVV5SlJpSE5zaldBd19fSE5LNDFRbWZuLUZNT3l4VkRtTVRjRFIwNy15ZzdNWXZSSkg2TVFtUmN6Y2ZwbF9oaFJoby1ORER1UmRXVkNhQjRVaTF6b3dqMg?oc=5>

### Amazon Stock (AMZN) Rises as the Company Prepares for a Leo Satellite Launch Today
- Summary: Amazon Stock (AMZN) Rises as the Company Prepares for a Leo Satellite Launch Today
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPZVJ1RnNYUmF1M3pITzF0clZ0b3NKZzNTWjlxSzFXMWdvN1Y2VjNaVlRFUy1sbXpEX1F6eGF2dV9KVkJKRy15OXNscVVxc3A4eDliN0ZmM19JZTFvM19COVl5ZGExVXhVSm42eEZOUldHandPaXB2M01yejBXNHhLYVg2LWVSYXJwVm1IVGlzaDBYajBWVkIxSDU1QWx0enZNM2RPajc1VV9oOWFtTmdR?oc=5>

### Dear Amazon Stock Fans, Mark Your Calendars for November 19
- Summary: Upcoming event on November 19 likely earnings release.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQMnJtUndPUnpyWXp5MHlQSzF1Tm5reUZubHRqSk5GU3dOY2RQU3FqTUEyWmdOYjNMNjVYMC1neWdkOXRaWHpHZkRiUEJkcno3MDBWYVp2U0xKWXM2d0pMM2xPUnFkZXBzaVUyZHF3aklEWGdCLW9EcktqQU5tSHN0T3pKUThTNUZnakZ2TW11TzBMT0h5UHhFZ1Q2M2RVS2ZFRjdtTg?oc=5>

### Andy Jassy Just Delivered Great News for Amazon Stock Investors
- Summary: Positive announcement from CEO likely to lift investor sentiment.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPMld0cG1LWndtWHQ5bm1YaGUwenhpYUtNUG5DTjA2TzU2bC1VMkg2cnc2X3FISFR6TUotcHAxOUljbThGc3NRUGtzbHd1czY3UUNTNEg2cGpIUG5PdU1TblRtaHhiWG9qSS03eTd6bENkdG1RcEF0UVdwaExGdDlZQlh5MWw5MU5sOFA1YTNKTHEyM25CNnM1TjhySVc?oc=5>

### ETFs Bought $259.9 Million of Amazon (AMZN) on Tuesday
- Summary: ETFs purchased $259.9M of Amazon shares, indicating institutional confidence.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNREd4ZGhCclU0RUZUaGRReG05VGQyV0NrY0d4R1JpUWRHSFNSVEZDMEZUdV9QZF8tTTBIYll1RVVMMkdzM1JaTktQTUxYc0NIb0Uyel9iNE4wQ2xjZzN2dGI1TFdEYzdVRDBfRzFXeXVlWUh4SmxMQlFFYkZ3ejlsZC0xOWxhYldXSUc0a256TGkzWXhY?oc=5>

### Amazon Is “the Cheapest It’s Been” in Years. Its P/E Fell From 34 to 21
- Summary: Amazon’s P/E ratio dropped from 34 to 21, indicating a cheaper valuation for investors.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOWDBOTm13THhibmtfRG1EOS1sSlRjY25uRTdxbUlCbS03OExaa2s0Z2JHR3BndzZfVWo1Z3BIWWN5ZEQ3cm5mUlJvWXlrZWRRS2pVM0pUSW85NU8yeDNVMUpQTUJfNDFOVjVnSnVXcE10ZVc0blRHWEJ1OTRPU0EtMU1aSmxjdmZoRHhsb3d3NkhUOHhr?oc=5>

### A Major Catalyst Could Send Amazon Stock to New Highs
- Summary: Speculation that a significant event could lift Amazon shares to record levels.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOY0VmM0xVNFNSMnJQVjd6UUhRdXVnY25PNzNfclFRUU1UWG03S1IwRkJlNUV0QlhnVkdpYndpVmdXODNJcFhlY003UzlIY1k0c2tPN2VxbjJtNFBUcE9yTTBLMnNKalF1QWg4NWVqWGlNd3V3U1IxMjBCOG1FaUFjd1hTNlhhVG9aeXIxQXR2S2F0WXFvNXBoaExPRjlqZw?oc=5>

### META, AMZN Stocks Jump As JPMorgan Picks Pair Over Alphabet — Sees Stronger AI Returns, Cloud Growth
- Summary: JPMorgan’s bullish outlook on Amazon and Meta drives their stock prices up, reflecting confidence in AI and cloud growth.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPUlRYcGF5YmpQQkx5NWI4RHdxbjNNNk16RldoUnduOG5hTzJYSUVxSFprTmNKXzVJZlAybzVUMzNzX3JPYTNObDE5enVrckpoOEtCWjZQNjVrOHJyMUY5OEFXa1p5OGdxLUFIWGhGM0Jxak5EeURaNHlxY0R6RUFuenFOVmI1SEVHSVBXY1dneFYwSGhlaXVtYk1Vcw?oc=5>

## RISKS

### Amazon: AI Bet Getting Riskier (NASDAQ:AMZN)
- Summary: Amazon is increasing its AI investment, raising potential risks to its operations and financials.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiekFVX3lxTE1COEZ0M0p2RHl5US1uaEtOckxaRlRXUXRMc1hlR01pNE4yV0NGTHJIb0Vma3FzZUtKX3RCbVg3ZmpUNHpnaHJZeTBjVFV0YmdFWDc0R2N5RFRObTY0bllEUU15N0J0aGFkUWdNdF9HOHg0WWtMSDJpdTl3?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **21.63** | **4.70** | **16.73** | **12.10** | **2,883,431,432,192.00 USD** | **12.24** |
| WMT | 45.75 | 10.36 | 24.65 | 5.90 | 1,019,350,286,336.00 USD | 25.97 |
| MSFT | 27.30 | 8.27 | 19.25 | 18.80 | 3,890,434,801,664.00 USD | 4.95 |
| GOOGL | 15.60 | 5.51 | 19.08 | 24.70 | 3,636,196,016,128.00 USD | 6.45 |

Peers fetched as_of: 2026-11-13; AMZN reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-30
- Revenue (latest available single quarter): 201,944,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 20,685,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxQR1FCaUQxM2w1M2hHM2U5STZ0Z2lQV05iVnBma3NFZ2JZVUUyRjJwd3lfN056VUR5X2ZYSlpGTjRiM3J2SllHUFkxRkZ1Qm9aM1diSzJpd2kyeUtrSTVsd3RfTlRIVEhzTWtDU0dSVG1HeGpXVk9NZ3hIRTFlU3RWQWhuU25EOHRaamYxUUZFTG1ncUtjNlRsRGxYcw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxONWZER29tTDNsRkVSZ2hGNHhTcjBWM2tXS0QyQ2VfeGtLbDh4SHZlSUtEYk80UnZkV280bHF3a21zMldIUEd3WHBTNmNIbXBlSXdDeXpHUG9EQzZrSkp0R0MxNnE2aS14U1lGdElRbEJ4a0JJZW1taG92S0tncnhsVHNQRXFNRHFGc2VWeEFqWEY3TDA?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNdHRhZ296anBFQ2FLWVU5TkVZWkV6OGdSYXNkSWItQUF1WDZoZVNaOWROa0hPZ0pBMUJ5U0VCN2dVVm53eDJIQU1ENTVoNS1Sb3RjU0FQSkoybmIzTXd2bnFRaS1RQ2JXT2ZLZ0xuTDVtU0o5THNfMUtHX3VnLWRCeU5MYUR1bFQ3dXpNNQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQVVNPUTA5NDJDMWlEOTdhaXlNZ3NsTzRWT1RJQkJQQmhEZjRyN0VoV082blR5VEh5dzNEWkFvU2pTTFhrUEk0cG1KWExNaTh4dEE1R1lhZTVGWkVIb1pQMjF0ZjFDRnZ1WTNROTZhYWlaMDhLZzZqQXR1VlFlV1ZMOWs3cWVkVVlwMG9maUhoUTRqbmVZ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNVi13aUZWMjBmYXlob3AtTFVZRDFPS0o5bzQ0Y1JpcEktM2VnNHhjY19SaENpY0p4QU9OY3JVa2tjMGJ0el9oamR6dFMwYlY1dTBoMDNWakF0Nk41VmpKVGEzR3p2bFRrQXNaSWplTXQ2MUNUclZFY3pmNzRpYUIwdldFbnNmR2o3SFQwZXJWMW1Qb00zQjZPZm5jQ3FYSU5obTRsTEZFWW1xVW5yM240Mw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNT2w3Um9jU09tYUlBRXFqYXZkZ3NxbG9Mb2k0ZnA0X0lZR2hlNFZONHJqZzg4aGoxbGJ4TUNLOGhPZUVOZzBuek9JTXlGWjVmbFZpLWFuNXFPU0dMd3ZfaGFTaWt0TDNqWF9OQ1FMMFN3U3h5dTlJUUZVVnE2NWUtdkVTSU85WjVmcVA2YktRNDdDdWc?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxNVDFMMWpzTHFWNVpraFphOVZad0Rza2psdnFrb3UwU2FES3JEZ2VaNHNudE80T2NOejIwTDJUaXJBMFdFSzNQZjFNYXZmc2tucTlPUXFobVpRLUJva2lGb0ItbVR1SkktLWhuaXRaUDA2VVV5SlJpSE5zaldBd19fSE5LNDFRbWZuLUZNT3l4VkRtTVRjRFIwNy15ZzdNWXZSSkg2TVFtUmN6Y2ZwbF9oaFJoby1ORER1UmRXVkNhQjRVaTF6b3dqMg?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPZVJ1RnNYUmF1M3pITzF0clZ0b3NKZzNTWjlxSzFXMWdvN1Y2VjNaVlRFUy1sbXpEX1F6eGF2dV9KVkJKRy15OXNscVVxc3A4eDliN0ZmM19JZTFvM19COVl5ZGExVXhVSm42eEZOUldHandPaXB2M01yejBXNHhLYVg2LWVSYXJwVm1IVGlzaDBYajBWVkIxSDU1QWx0enZNM2RPajc1VV9oOWFtTmdR?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQMnJtUndPUnpyWXp5MHlQSzF1Tm5reUZubHRqSk5GU3dOY2RQU3FqTUEyWmdOYjNMNjVYMC1neWdkOXRaWHpHZkRiUEJkcno3MDBWYVp2U0xKWXM2d0pMM2xPUnFkZXBzaVUyZHF3aklEWGdCLW9EcktqQU5tSHN0T3pKUThTNUZnakZ2TW11TzBMT0h5UHhFZ1Q2M2RVS2ZFRjdtTg?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPMld0cG1LWndtWHQ5bm1YaGUwenhpYUtNUG5DTjA2TzU2bC1VMkg2cnc2X3FISFR6TUotcHAxOUljbThGc3NRUGtzbHd1czY3UUNTNEg2cGpIUG5PdU1TblRtaHhiWG9qSS03eTd6bENkdG1RcEF0UVdwaExGdDlZQlh5MWw5MU5sOFA1YTNKTHEyM25CNnM1TjhySVc?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNREd4ZGhCclU0RUZUaGRReG05VGQyV0NrY0d4R1JpUWRHSFNSVEZDMEZUdV9QZF8tTTBIYll1RVVMMkdzM1JaTktQTUxYc0NIb0Uyel9iNE4wQ2xjZzN2dGI1TFdEYzdVRDBfRzFXeXVlWUh4SmxMQlFFYkZ3ejlsZC0xOWxhYldXSUc0a256TGkzWXhY?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOWDBOTm13THhibmtfRG1EOS1sSlRjY25uRTdxbUlCbS03OExaa2s0Z2JHR3BndzZfVWo1Z3BIWWN5ZEQ3cm5mUlJvWXlrZWRRS2pVM0pUSW85NU8yeDNVMUpQTUJfNDFOVjVnSnVXcE10ZVc0blRHWEJ1OTRPU0EtMU1aSmxjdmZoRHhsb3d3NkhUOHhr?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOY0VmM0xVNFNSMnJQVjd6UUhRdXVnY25PNzNfclFRUU1UWG03S1IwRkJlNUV0QlhnVkdpYndpVmdXODNJcFhlY003UzlIY1k0c2tPN2VxbjJtNFBUcE9yTTBLMnNKalF1QWg4NWVqWGlNd3V3U1IxMjBCOG1FaUFjd1hTNlhhVG9aeXIxQXR2S2F0WXFvNXBoaExPRjlqZw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPUlRYcGF5YmpQQkx5NWI4RHdxbjNNNk16RldoUnduOG5hTzJYSUVxSFprTmNKXzVJZlAybzVUMzNzX3JPYTNObDE5enVrckpoOEtCWjZQNjVrOHJyMUY5OEFXa1p5OGdxLUFIWGhGM0Jxak5EeURaNHlxY0R6RUFuenFOVmI1SEVHSVBXY1dneFYwSGhlaXVtYk1Vcw?oc=5
- https://news.google.com/rss/articles/CBMiekFVX3lxTE1COEZ0M0p2RHl5US1uaEtOckxaRlRXUXRMc1hlR01pNE4yV0NGTHJIb0Vma3FzZUtKX3RCbVg3ZmpUNHpnaHJZeTBjVFV0YmdFWDc0R2N5RFRObTY0bllEUU15N0J0aGFkUWdNdF9HOHg0WWtMSDJpdTl3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
