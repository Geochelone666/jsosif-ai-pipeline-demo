# ISRG Intelligence Report

- ticker: **ISRG**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/ISRG/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ISRG/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:22:34.590917+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 3, 'ai': 4, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/ISRG** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'directional_claim_without_event_type': 4}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 10 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-24

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 430.1800 |
| Return 1D (%) | 0.7023 |
| Return 1W (%) | 7.8010 |
| Return 1M (%) | -3.5211 |
| Return YTD (%) | -24.0448 |
| Return 1Y (%) | -25.0858 |
| Annualized volatility (%) | 36.0934 |
| Beta vs SPY | 0.8810 |
| Max drawdown (%) | -43.9960 |
| Sharpe (rf=0) | -0.6207 |
| Downside deviation (rf=0, %) | 26.6374 |
| Sortino (rf=0) | -0.8411 |
| Historical VaR 95% (1D, %) | 3.3110 |
| Historical ES 95% (1D, %) | 5.1297 |
| Correlation vs SPY | 0.3667 |
| Tracking error vs SPY (%) | 33.6274 |
| P/E (trailing) | 52.02 |
| P/B | 9.33 |
| EV/EBITDA | 32.48 |
| Revenue growth (%) | 21.70 |
| Forward P/E (estimate) | 34.50 |
| Gross margin (%) | 66.64 |
| Operating margin (%) | 31.70 |
| Return on equity (%) | 17.93 |
| Free cash flow yield (%) | 2.30 |
| MA50 | 427.2522 |
| Close vs MA50 (%) | 0.6853 |
| MA200 | 426.3640 |
| Close vs MA200 (%) | 0.8950 |
| RSI (14, Wilder) | 49.6330 |
| MACD (12,26) | -2.4410 |
| MACD signal (9) | 0.2138 |
| MACD histogram | -2.6548 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ISRG': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 430.1800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.7023 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 7.8010 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.5211 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -24.0448 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -25.0858 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.0934 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.6374 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.8411 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.3110 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1297 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3667 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.6274 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8810 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.9960 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.6207 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 34.4985 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.6420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.7020 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.9320 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.3034 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 52.0169 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 49.6330 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.6548 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.6853 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 0.8950 -> Slightly above the moving-average trend level.

## TAILWINDS

### Intuitive Surgical Inc Stock (ISRG) Moved Up by 4.16% on Nov 24: A Full Analysis
- Summary: Intuitive Surgical Inc Stock (ISRG) Moved Up by 4.16% on Nov 24: A Full Analysis
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNeDNVd3Jka29HWFdaai1fN1FQejg3ZDhVS2RYRk1wdUVSa1JFUkduTXpIU3pOSFlCQUVlcklNNlNTSDAyYVMwMGxrenRSZzVMNTVjWmplOTZlYTFfRHdFa1pIN29nN3JLeTlheXEtazQ1NzBhb19uUm5UZXI2X3I1V2l6UUIyWml1aGs0?oc=5>

### Is Intuitive Surgical Stock Worth 33 Times 2027 Profit?
- Summary: Questions valuation relative to projected 2027 profit, implying potential upside if growth expectations are met.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQRzZCdWRpLWg4cmNGTnNoTWllOWIwU2dlOEMzRm5KMDNwMThZQlMySUNUb1Uxa1ROUkZFSVd1RmZEY09WRWRkeGRXR3FtX3JZWGx3cnNwYnhLRld3akxDelItd2h1OGNia3Y1UzE3OFVqVGpkUUhPNVNJRlU0Z1g4b1I4QjhOUjZyaWI4RS1TVTVTVkJ3dEJtR2xBbWZNQ3lCenBHa0RkN08tbXF6ZnV4TkNLbHVQQQ?oc=5>

### Is Intuitive Surgical (ISRG) Fairly Valued After Fresh Optimism Around Procedure Growth?
- Summary: Highlights optimism about procedure growth, suggesting a favorable valuation outlook for ISRG.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNQURfMWtza01GbndkMFdCTFRSb1I0ZjJHVVNVLURBWG5zVk5wODgxckxpWkRBUDRYQ2JWSjFOMEtYSVB6dTN1c1Y4M2VraGJoTEprME9zWlh0X0x3aUd5Y2dtQTZHbFQ4SDZOREdfcC03RjFIdzlNR2NGQkNaazJiXzJGWG1uek9Bd2U4WXFQZmF4RWw2WExVQU5aYnNWdTdoLW5Ddg?oc=5>

### Here's How Much $100 Invested In Intuitive Surgical 10 Years Ago Would Be Worth Today
- Summary: Shows historical investment performance, reinforcing positive long-term returns for ISRG shareholders.
- Date: 2026-11-25 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOV0p6UGU5MXhWNUY3TFU4QWhBSHRjTEg3VGhMM0NyN2hOeGthTHk1dERfelF5cXdYdGF3NFZhVk9SX3FoVnMwVUFwTTBiRFhaZndMOHBmZ3VLcUJOaFNOY0tPWUZqdGhja0h1WlRBMGhHdmQwR2k0YlF5N1lITmMycUFzM3BuNDdoeGV3MF9aSnc3N3FBb0tvMDFoOGE0Xzk2WC1raVd1WDJ0ZFdsams1d01HaXEwZ0NiZXdka3hmb0VaeWFO?oc=5>

### Procedure Growth Is Altering The Investment Case For Intuitive Surgical Stock
- Summary: Indicates that rising procedure volumes are reshaping the investment thesis, likely improving valuation prospects.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPVHhLZHdCWjdKYzZmN1E2N21yRjRieUViNXRYb050bzJ3RFB1djdLMkZnT01PTl9ESEMzckgteldCQW5aaUJLdXNqNW9GNTZLblFqRDVtZmpCOElJMU94TGVyaDc0UnFhNDNhQWZ4YlV4Vk45THh1UEdWdkJoSHVBYjhaSTdmYWE0Yjg2RkFZcmFCeG9IckdUWTByNTVwQWVuY1dVWGJacmthQQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Intuitive Surgical completes record share buyback: ISRG gains momentum
- Summary: Intuitive Surgical completes record share buyback: ISRG gains momentum
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPMm5nOVNQZml2RnJNbU5SR0E4dzdaMldZcTFKQ0NydnhOb1NuRTIzZ3pEbFhSbGJNcUhSamM3a0lmZ09vLV9QSzlXR01QX01CTElYaGFTWkE0djdzMDh3LUdkeFo2UUhVRGU1NVJiUFF6WXhSdzlHcjRXc0FBSlc0ZmRRT1Q5Ri1lTUdLUTUybG1pbktPQW1IUw?oc=5>

### Intuitive Surgical rises as investors appear to lean on upbeat analyst commentary and durable procedure growth
- Summary: Intuitive Surgical rises as investors appear to lean on upbeat analyst commentary and durable procedure growth
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxQVDhaRlBvZXRMT1ZOUHluMGNvaVFKczBRVWl3MkdKeWdSOEJNQlBhN3MxdW9Jd2xTREJEdi1YbTNMSE90UjNBU2RTMXo3bjNiMVFvZ1NlT0xMUXRFVDlUejZkMWRHRW5WMk8tSnZrWGVFeTczY0FtbUxRQzFUSXZqYXhZNU9hbGRLbHZkV2tPWUFtT0htNlFLdTlnMGs5OURQbGxoVDZZNmZuTU9nNjUxTThrb3FxbU13MU1UYVhDNXdZNW9PRmMtTkdjbzljaVpzM0ZNYkhLRWNZazA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ISRG** | **52.02** | **9.33** | **32.48** | **21.70** | **149,119,188,992.00 USD** | **-25.09** |
| MDT | 23.44 | 2.43 | 13.36 | 4.50 | 122,042,556,416.00 USD | -6.14 |
| SYK | 35.60 | 5.42 | 18.56 | 7.60 | 127,253,577,728.00 USD | -9.22 |
| BSX | 19.09 | 2.56 | 13.86 | 1.40 | 65,588,666,368.00 USD | -55.18 |

Peers fetched as_of: 2026-11-27; ISRG reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNeDNVd3Jka29HWFdaai1fN1FQejg3ZDhVS2RYRk1wdUVSa1JFUkduTXpIU3pOSFlCQUVlcklNNlNTSDAyYVMwMGxrenRSZzVMNTVjWmplOTZlYTFfRHdFa1pIN29nN3JLeTlheXEtazQ1NzBhb19uUm5UZXI2X3I1V2l6UUIyWml1aGs0?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQRzZCdWRpLWg4cmNGTnNoTWllOWIwU2dlOEMzRm5KMDNwMThZQlMySUNUb1Uxa1ROUkZFSVd1RmZEY09WRWRkeGRXR3FtX3JZWGx3cnNwYnhLRld3akxDelItd2h1OGNia3Y1UzE3OFVqVGpkUUhPNVNJRlU0Z1g4b1I4QjhOUjZyaWI4RS1TVTVTVkJ3dEJtR2xBbWZNQ3lCenBHa0RkN08tbXF6ZnV4TkNLbHVQQQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNQURfMWtza01GbndkMFdCTFRSb1I0ZjJHVVNVLURBWG5zVk5wODgxckxpWkRBUDRYQ2JWSjFOMEtYSVB6dTN1c1Y4M2VraGJoTEprME9zWlh0X0x3aUd5Y2dtQTZHbFQ4SDZOREdfcC03RjFIdzlNR2NGQkNaazJiXzJGWG1uek9Bd2U4WXFQZmF4RWw2WExVQU5aYnNWdTdoLW5Ddg?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOV0p6UGU5MXhWNUY3TFU4QWhBSHRjTEg3VGhMM0NyN2hOeGthTHk1dERfelF5cXdYdGF3NFZhVk9SX3FoVnMwVUFwTTBiRFhaZndMOHBmZ3VLcUJOaFNOY0tPWUZqdGhja0h1WlRBMGhHdmQwR2k0YlF5N1lITmMycUFzM3BuNDdoeGV3MF9aSnc3N3FBb0tvMDFoOGE0Xzk2WC1raVd1WDJ0ZFdsams1d01HaXEwZ0NiZXdka3hmb0VaeWFO?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPVHhLZHdCWjdKYzZmN1E2N21yRjRieUViNXRYb050bzJ3RFB1djdLMkZnT01PTl9ESEMzckgteldCQW5aaUJLdXNqNW9GNTZLblFqRDVtZmpCOElJMU94TGVyaDc0UnFhNDNhQWZ4YlV4Vk45THh1UEdWdkJoSHVBYjhaSTdmYWE0Yjg2RkFZcmFCeG9IckdUWTByNTVwQWVuY1dVWGJacmthQQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPMm5nOVNQZml2RnJNbU5SR0E4dzdaMldZcTFKQ0NydnhOb1NuRTIzZ3pEbFhSbGJNcUhSamM3a0lmZ09vLV9QSzlXR01QX01CTElYaGFTWkE0djdzMDh3LUdkeFo2UUhVRGU1NVJiUFF6WXhSdzlHcjRXc0FBSlc0ZmRRT1Q5Ri1lTUdLUTUybG1pbktPQW1IUw?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxQVDhaRlBvZXRMT1ZOUHluMGNvaVFKczBRVWl3MkdKeWdSOEJNQlBhN3MxdW9Jd2xTREJEdi1YbTNMSE90UjNBU2RTMXo3bjNiMVFvZ1NlT0xMUXRFVDlUejZkMWRHRW5WMk8tSnZrWGVFeTczY0FtbUxRQzFUSXZqYXhZNU9hbGRLbHZkV2tPWUFtT0htNlFLdTlnMGs5OURQbGxoVDZZNmZuTU9nNjUxTThrb3FxbU13MU1UYVhDNXdZNW9PRmMtTkdjbzljaVpzM0ZNYkhLRWNZazA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
