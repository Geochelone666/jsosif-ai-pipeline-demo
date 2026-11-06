# ISRG Intelligence Report

- ticker: **ISRG**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/ISRG/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ISRG/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:21:46.570580+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 1, 'ai': 4, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/ISRG** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 8 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 27.27%; oldest publication 2026-11-01

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 468.5200 |
| Return 1D (%) | -2.8168 |
| Return 1W (%) | 4.4032 |
| Return 1M (%) | 15.2627 |
| Return YTD (%) | -17.2752 |
| Return 1Y (%) | -14.5894 |
| Annualized volatility (%) | 35.4471 |
| Beta vs SPY | 0.9273 |
| Max drawdown (%) | -43.9960 |
| Sharpe (rf=0) | -0.2678 |
| Downside deviation (rf=0, %) | 25.9688 |
| Sortino (rf=0) | -0.3656 |
| Historical VaR 95% (1D, %) | 2.9944 |
| Historical ES 95% (1D, %) | 5.1080 |
| Correlation vs SPY | 0.3556 |
| Tracking error vs SPY (%) | 33.1449 |
| P/E (trailing) | 58.27 |
| P/B | 10.16 |
| EV/EBITDA | 35.45 |
| Revenue growth (%) | 21.70 |
| Forward P/E (estimate) | 37.58 |
| Gross margin (%) | 66.64 |
| Operating margin (%) | 33.29 |
| Return on equity (%) | 17.93 |
| Free cash flow yield (%) | 2.08 |
| MA50 | 408.2152 |
| Close vs MA50 (%) | 14.7728 |
| MA200 | 431.5648 |
| Close vs MA200 (%) | 8.5631 |
| RSI (14, Wilder) | 64.8151 |
| MACD (12,26) | 14.1396 |
| MACD signal (9) | 12.6067 |
| MACD histogram | 1.5330 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ISRG': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 468.5200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.8168 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.4032 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 15.2627 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -17.2752 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -14.5894 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.4471 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.9688 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.3656 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9944 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1080 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3556 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.1449 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9273 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.9960 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.2678 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 37.5755 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.6420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.2860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.9320 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.0752 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 58.2736 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 64.8151 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.5330 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 14.7728 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 8.5631 -> Clearly above the moving-average trend level.

## TAILWINDS

### Intuitive Surgical Inc. (NASDAQ:ISRG) Stock Analysis — Sharp Gain, Valuation and Momentum Review
- Summary: Intuitive Surgical Inc. (NASDAQ:ISRG) Stock Analysis — Sharp Gain, Valuation and Momentum Review
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxQNXdmQTdVbHVYck4xWE9wMElucXViSUxWMzhJcTRka194a0pYLURJTDVEUUpkLWhHVDJzN2FSWnRMVFFPeGRqSzgtOVM5ajJ4aXhTSU02RTJVcVQ5WTUwVUhHeWlJYzFoYkZMOFVVT3Fid0NSakFMSmw5Y21MOUtET1RXejBRa2xwbmlZOTJpZi1rZGV4cDR4NFplMmx4UE5tYUM2bWU1UWdMSXdWdTMxTjZtdjFEWXhkd2p2NDZfMUlfc2Z2UmFMRmhYZllRYTQ5RWxFaUpsVEc?oc=5>

### Intuitive Surgical Surges 5.4%, Adding ~$9 Billion in One Session
- Summary: Stock price jumps 5.4%, adding ~$9B in one session.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOYVkwRnFNQk9ZV2VhaHJnMnBIbklPVEd3cHc4elB3VldOSVRwS0RvRm9yQWdWNjR6LThPVlU5ZTNjSzY5N3RqV3hPUkotZWE5VnEyTi1iMDNNengzZ2R5Q1lYWmpOVnI0MWZwLVU0MEFWOUtzT0JNT081dEdwOW5pN3VGNmF1OTMyd3VRVGh1OWNZNEhZ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Intuitive Surgical Stock Just Fell Despite a 22% Revenue Jump. Here's What Investors Are Missing.
- Summary: Stock decline amid strong revenue, indicating market skepticism.
- Date: 2026-11-01 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOVzVGQXhQVHBIdmRpcGgweEFJNVhUWFpEZVdYYk1CelFJMmVpM29pOV8zREhFWWJSU2Y5QXNSX3JIM1FOS2poUjFaSTFCdm05YlJFbVltV1A4Q0gzNml3bUYwOUFZWWdTNFNLbktxLS04WVJQOEtfZDQ1MmdiVnppbU50VWhYa01yb2VvU3ZvVllzeG92VUZzOA?oc=5>

### A former Amazon healthcare executive will join Intuitive's board in January
- Summary: New board member from Amazon healthcare joins ISRG.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOZ2gydkJGa3BFbjV3dGltcWFqQU10S283QnZWbEtpOW5ZclF4UlQwcXZzZ3lsTEN4Q0tFYXZtcDlqTFVpUjltZndmbWd2bHN6VTVkNHl4YmpGdTRQY0Rtd0V6QmRMVXlGNUszaFF6REhuWENPdkNNcXRnaktkV0Y5a2ZtNEdNbU9BV0ZKSUZwWlN6d1lyZFhqSC0ySENBUFptQlYtaA?oc=5>

## RISKS

### Is This Number The Biggest Risk To Intuitive Surgical Stock?
- Summary: Questioning a key risk factor for ISRG, potentially affecting investor confidence.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPM3g0TU1KTFdMLXpCSmJXTjVybXNkdlNDcW1UY2RvdmxnSksya3JxME0wVGxqaDFKTU51UUV2QUVlbm1QTThsRUI0YTUyNTFSMnIzNlU3N0R3cW4yLWZ4aUdWd1N2OGR2NEZiMnVRaUlBNXAyMUlsM3dNVi1pdmV3Nmd4T1A5Z3ZGTVFVYlNubTQ4Ym5uOVNwVnhFYVdRUDdrNlFjV21HZS12OE9VUFVSZkJ2Y25EWlBOdm5CLQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ISRG** | **58.27** | **10.16** | **35.45** | **21.70** | **165,517,819,904.00 USD** | **-14.59** |
| MDT | 25.76 | 2.67 | 14.80 | 13.70 | 134,104,817,664.00 USD | 19.82 |
| SYK | 36.19 | 5.44 | 18.61 | 7.60 | 127,561,940,992.00 USD | -5.28 |
| BSX | 18.84 | 2.52 | 13.70 | 1.40 | 64,704,487,424.00 USD | -54.86 |

Peers fetched as_of: 2026-11-05; ISRG reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMi2AFBVV95cUxQNXdmQTdVbHVYck4xWE9wMElucXViSUxWMzhJcTRka194a0pYLURJTDVEUUpkLWhHVDJzN2FSWnRMVFFPeGRqSzgtOVM5ajJ4aXhTSU02RTJVcVQ5WTUwVUhHeWlJYzFoYkZMOFVVT3Fid0NSakFMSmw5Y21MOUtET1RXejBRa2xwbmlZOTJpZi1rZGV4cDR4NFplMmx4UE5tYUM2bWU1UWdMSXdWdTMxTjZtdjFEWXhkd2p2NDZfMUlfc2Z2UmFMRmhYZllRYTQ5RWxFaUpsVEc?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOYVkwRnFNQk9ZV2VhaHJnMnBIbklPVEd3cHc4elB3VldOSVRwS0RvRm9yQWdWNjR6LThPVlU5ZTNjSzY5N3RqV3hPUkotZWE5VnEyTi1iMDNNengzZ2R5Q1lYWmpOVnI0MWZwLVU0MEFWOUtzT0JNT081dEdwOW5pN3VGNmF1OTMyd3VRVGh1OWNZNEhZ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOVzVGQXhQVHBIdmRpcGgweEFJNVhUWFpEZVdYYk1CelFJMmVpM29pOV8zREhFWWJSU2Y5QXNSX3JIM1FOS2poUjFaSTFCdm05YlJFbVltV1A4Q0gzNml3bUYwOUFZWWdTNFNLbktxLS04WVJQOEtfZDQ1MmdiVnppbU50VWhYa01yb2VvU3ZvVllzeG92VUZzOA?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOZ2gydkJGa3BFbjV3dGltcWFqQU10S283QnZWbEtpOW5ZclF4UlQwcXZzZ3lsTEN4Q0tFYXZtcDlqTFVpUjltZndmbWd2bHN6VTVkNHl4YmpGdTRQY0Rtd0V6QmRMVXlGNUszaFF6REhuWENPdkNNcXRnaktkV0Y5a2ZtNEdNbU9BV0ZKSUZwWlN6d1lyZFhqSC0ySENBUFptQlYtaA?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPM3g0TU1KTFdMLXpCSmJXTjVybXNkdlNDcW1UY2RvdmxnSksya3JxME0wVGxqaDFKTU51UUV2QUVlbm1QTThsRUI0YTUyNTFSMnIzNlU3N0R3cW4yLWZ4aUdWd1N2OGR2NEZiMnVRaUlBNXAyMUlsM3dNVi1pdmV3Nmd4T1A5Z3ZGTVFVYlNubTQ4Ym5uOVNwVnhFYVdRUDdrNlFjV21HZS12OE9VUFVSZkJ2Y25EWlBOdm5CLQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
