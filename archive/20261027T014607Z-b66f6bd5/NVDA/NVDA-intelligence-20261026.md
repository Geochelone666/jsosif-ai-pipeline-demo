# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T01:50:05.725516+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 1, 'ai': 10, 'unknown': 0, 'irrelevant': 13})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 37.5%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 216.0000 |
| Return 1D (%) | 2.3891 |
| Return 1W (%) | -0.5021 |
| Return 1M (%) | -4.0299 |
| Return YTD (%) | 16.0887 |
| Return 1Y (%) | 16.2448 |
| Annualized volatility (%) | 37.6575 |
| Beta vs SPY | 1.9342 |
| Max drawdown (%) | -20.2144 |
| Sharpe (rf=0) | 0.5157 |
| Downside deviation (rf=0, %) | 25.3164 |
| Sortino (rf=0) | 0.7671 |
| Historical VaR 95% (1D, %) | 3.7777 |
| Historical ES 95% (1D, %) | 4.5600 |
| Correlation vs SPY | 0.6531 |
| Tracking error vs SPY (%) | 30.8913 |
| P/E (trailing) | 27.31 |
| P/B | 22.78 |
| EV/EBITDA | 25.75 |
| Revenue growth (%) | 105.90 |
| Forward P/E (estimate) | 13.57 |
| Gross margin (%) | 74.67 |
| Operating margin (%) | 66.24 |
| Return on equity (%) | 117.21 |
| Free cash flow yield (%) | 0.80 |
| MA50 | 222.2158 |
| Close vs MA50 (%) | -2.7972 |
| MA200 | 203.5192 |
| Close vs MA200 (%) | 6.1325 |
| RSI (14, Wilder) | 44.1367 |
| MACD (12,26) | -2.7068 |
| MACD signal (9) | -0.9178 |
| MACD histogram | -1.7890 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 216.0000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.3891 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.5021 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -4.0299 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 16.0887 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 16.2448 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.6575 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.3164 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.7671 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7777 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.5600 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6531 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.8913 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.9342 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2144 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5157 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.5724 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.2370 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.2110 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.8016 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.3072 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 44.1367 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.7890 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -2.7972 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.1325 -> Clearly above the moving-average trend level.

## TAILWINDS

### NVDA Stock Ticks Higher Overnight: a16z Data Shows GPU Rental Prices Rising Sharply, Even For Older Chips
- Summary: NVDA Stock Ticks Higher Overnight: a16z Data Shows GPU Rental Prices Rising Sharply, Even For Older Chips
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNVzhIbU14cHlhdjlKTUNmTkpxbXBMTXRHb2U5Wk1rMVg0dEhwX216VVJmUEhfT3l5SUtKZVB0ZU91QklIdERHMDRzSXhmcExnMmJxSUxNMUhJNmpYdEN4bUFMTXlwbjY4WjRENmZyR0JfQWMwTWxramtEVi0teDZWOUVMTUVFRjJSTGg2NjJ6eTVXYmFxWllIT1BQeHFGemM?oc=5>

### Nvidia (NVDA) Surpasses Market Returns: Some Facts Worth Knowing
- Summary: NVDA outperformed market returns, indicating strong performance.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQdnNyZ1g4R2pVdTJTQW1HNE53cGJLSDVBbGFTUWZlOFd0akxCQUJ6SzBwWVVlaDFYZjlLdXA3TktObUZrdnJRX1lCcEFnbDBvZTliYUVCeC1OUDMtVGxhT2pvVWxnYm05UUhEUnRER1NGbFVLZmhWVG8wYVcxQ3hKRHdjdnNkMkRGWFFuRjBFRjdUeE5oU1drR3oxV2tyUUFCcExN?oc=5>

### Nvidia NVDA Stock Rebounds Above $215 on Chip Sentiment Improvement but Data-Centre Risks Remain
- Summary: NVDA shares rise above $215 driven by improved chip sentiment, though data‑centre risks persist.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxOUk5LazdKNWdWMlFzZFVvT2F0QU5oNTdFVXJYMDlJMjdxLUVIZV9ZQmZkWjZBWmsyTnpOZXdidG56aTY4VzFfTTExVkVSQktsQ3BtUWd1cmhrZ3AtRE5aaGhoaTRCMVZ4Q2YtTWRBTkdtWmNZZ2NXNXlXU2hoT1FoQzdDd0x1SVQ3UUtuMWRHR0QtbVlGWG1uc1lPdVQ2Q2hyYTNuc2dJWTVUeXJ6RU5SSC1UQkM2MGVaUTViMDRLYlNyVG9tdG0tMHJyWUdBVnB2MFFwOQ?oc=5>

### ETFs Are Buying NVIDIA (NVDA) on Thursday
- Summary: ETFs are purchasing NVDA shares, indicating increased institutional demand.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQRDhlSHItazZid1JpaGpGOVJSb0tMUENleERVZEVyX3pMaklPcXJwRDBqQlFVcTRBTzZ5ZXM4ZEMzRWdHS2oyaV8yNUFBeFFqU0l2UDZCd0s2THhnMUJkMGRfeWpNb2tJVjZaLXNmblNDdWlaczJPTjQwYkVsTzRaeVN0MlgzcG5ob3U5V05raGowQ2hGRVEzMjJQNTVnUQ?oc=5>

## HEADWINDS

### Nvidia Stock (NVDA) Gets Rare Sell Rating. Here’s Why
- Summary: Analyst downgrades NVDA, citing valuation concerns and potential slowdown in demand.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxOMmthY0ZjT3BHV1dsSWZmZHh4bWZud1ljRHRSOEhOLTJUUTI1TXFDR0VBWUgwWnk5c2RGYTVqc2VaM2pyRFlTbUV6bUVSQlYyVUktRE9lZlktMmctWWF0ZW1tckJ4c2lSOXhCT1ZLNmxrNHJiVE1DamdYdTgxcEZnQkplMkF3dw?oc=5>

### Elon Musk Just Delivered a Sweeping Blow to Nvidia Investors
- Summary: Negative impact on NVDA investors due to Musk's actions.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQdFlrYjBrclR0Z1h0LTZJejNtYXRkbWRQb3NkSENTdVlicWxDTWFzRXp4V0pfYWhLX0xQVzc1NVZkUThPOFkzLXBQOXdVV193ZkpPVk9LNXAwQnV3N0VPNE81Zk5wM3YxLVYwRGNQbjFLRzF4N21GdzhTSVFPTUktMDM1cG5RdDBxUEJSOGtOall0UkRNMnBKTg?oc=5>

## CATALYSTS

### Prediction: This Could Trigger NVDA’s Next Breakout by 2027
- Summary: Analysts predict a potential breakout for NVDA by 2027.
- Date: 2026-10-26 | Impact: medium | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQREZTS1hMYzJXdnNuUEt5QjdCQUZLSmpqU09sRDhLd05XX3Q1blhTMURVbDI2dUZnNFpsYjRobmZxMEEwdGZWVWJTS0pDM05rZFpVX1BOZnJLSF9fSU1PVUZaS1BIa3dMbkRqUEtWN1F3Yk9qZXBUVTlYdmFVWFZoR1Nld2Qwbzdyd1U3ckQ4amxqcTY0OG5BaEstUnkzNVlJUERF?oc=5>

### Elon Musk and SpaceX Just Delivered Incredible News to Nvidia That Could Help the Stock Double in the Next Year
- Summary: Musk and SpaceX announced news that may boost NVDA’s stock performance.
- Date: 2026-10-26 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQV3FvU0kxSnA1Q09RekNwSXJuelU4V3dhajNkRUxtT2lWa1lvekh0ZDNfN1NwT1NKSkY5ZDFzWlplY0ZMZWROVjM3MmpfcFdkSWo4MkZaWllGYjN5eWI1bGR4eTVhYW44VDBwXzlCVW5ndzVrRXV4WjBHLW9WeUxubkFSU1lhcnhxRTJhUzFkUkZUSjBtWjBGSA?oc=5>

### Meta Launches $35B Stock Offering, Plans Another $60B Program In 2027: Nvidia, AMD, Broadcom Eye Up To $5B Investment
- Summary: NVDA may invest in Meta’s upcoming stock offerings.
- Date: 2026-10-26 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPRUZTaHN0QlFyYk9uM1pRZWtkcWV4T19femtzQ3FwWXpGQnhDZDh0WFdQUU1EREtESlhjeUVKRUpfTkxfUjVhVGFFNFFnSUJ6NEc4RWNoUkJqZ19WdlNUNDZMb3U3N3RKUzZKa24zaTd0dkM0R0VLdThfUThyM1lIU2NOdlRXSHJTVXJyeUxfS1AtUnZqaVotNElVakI2QQ?oc=5>

### Why Did Nvidia (NASDAQ:NVDA) Stock Jump 3%? Anthropic IPO and Morgan Stanley Spark AI Rally
- Summary: Nvidia shares rose 3% after Anthropic IPO and Morgan Stanley’s AI rally, boosting investor sentiment.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMie0FVX3lxTE5oby1RYnBMY0d5UnpHN2pfZG82SmlXMDRUOWs4d05vZVc3ZmlfVjdMZF9Qc0swYS1CYUJxZlpkOTBJZUJMaW1HMkQ5aW52Z3A3NjdGM2tmUkNodnc4MUJhVkEtMHlMWTdUeWtkSlAwbXFBYVluUzBxcHVZUQ?oc=5>

## RISKS

### Nvidia (NVDA) Has Lost Its China AI Accelerator Market
- Summary: Nvidia lost its China AI accelerator market, indicating a decline in regional market share.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNZXBrdnEtYnZLWk95RmJjZlRTeFR2ZjZDaGM5dDR4VW9KNWdDZjRjTmJidlY0eWExNVJVYUZ2NGJlNlo3NXZYMzFTZkhYeUU4ZC1RSGUzMXhLYkdkRUZXMEt5bVJRY1E0LW52Z0QzaWFYRTE3bDh1SVBMWnRNZUs0dndHVXBXdmZkYjBoRWFsX0p6RG8?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **27.31** | **22.78** | **25.75** | **105.90** | **5,215,751,766,016.00 USD** | **16.24** |
| AMD | 135.53 | 12.90 | 89.78 | 50.10 | 867,301,392,384.00 USD | 110.06 |
| AVGO | 42.04 | 15.76 | 30.75 | 85.50 | 1,571,335,831,552.00 USD | -6.36 |
| INTC | N/A | 5.21 | 29.26 | 25.40 | 478,233,919,488.00 USD | 136.34 |

Peers fetched as_of: 2026-10-26; NVDA reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMinwFBVV95cUxNVzhIbU14cHlhdjlKTUNmTkpxbXBMTXRHb2U5Wk1rMVg0dEhwX216VVJmUEhfT3l5SUtKZVB0ZU91QklIdERHMDRzSXhmcExnMmJxSUxNMUhJNmpYdEN4bUFMTXlwbjY4WjRENmZyR0JfQWMwTWxramtEVi0teDZWOUVMTUVFRjJSTGg2NjJ6eTVXYmFxWllIT1BQeHFGemM?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQdnNyZ1g4R2pVdTJTQW1HNE53cGJLSDVBbGFTUWZlOFd0akxCQUJ6SzBwWVVlaDFYZjlLdXA3TktObUZrdnJRX1lCcEFnbDBvZTliYUVCeC1OUDMtVGxhT2pvVWxnYm05UUhEUnRER1NGbFVLZmhWVG8wYVcxQ3hKRHdjdnNkMkRGWFFuRjBFRjdUeE5oU1drR3oxV2tyUUFCcExN?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxOUk5LazdKNWdWMlFzZFVvT2F0QU5oNTdFVXJYMDlJMjdxLUVIZV9ZQmZkWjZBWmsyTnpOZXdidG56aTY4VzFfTTExVkVSQktsQ3BtUWd1cmhrZ3AtRE5aaGhoaTRCMVZ4Q2YtTWRBTkdtWmNZZ2NXNXlXU2hoT1FoQzdDd0x1SVQ3UUtuMWRHR0QtbVlGWG1uc1lPdVQ2Q2hyYTNuc2dJWTVUeXJ6RU5SSC1UQkM2MGVaUTViMDRLYlNyVG9tdG0tMHJyWUdBVnB2MFFwOQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQRDhlSHItazZid1JpaGpGOVJSb0tMUENleERVZEVyX3pMaklPcXJwRDBqQlFVcTRBTzZ5ZXM4ZEMzRWdHS2oyaV8yNUFBeFFqU0l2UDZCd0s2THhnMUJkMGRfeWpNb2tJVjZaLXNmblNDdWlaczJPTjQwYkVsTzRaeVN0MlgzcG5ob3U5V05raGowQ2hGRVEzMjJQNTVnUQ?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxOMmthY0ZjT3BHV1dsSWZmZHh4bWZud1ljRHRSOEhOLTJUUTI1TXFDR0VBWUgwWnk5c2RGYTVqc2VaM2pyRFlTbUV6bUVSQlYyVUktRE9lZlktMmctWWF0ZW1tckJ4c2lSOXhCT1ZLNmxrNHJiVE1DamdYdTgxcEZnQkplMkF3dw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQdFlrYjBrclR0Z1h0LTZJejNtYXRkbWRQb3NkSENTdVlicWxDTWFzRXp4V0pfYWhLX0xQVzc1NVZkUThPOFkzLXBQOXdVV193ZkpPVk9LNXAwQnV3N0VPNE81Zk5wM3YxLVYwRGNQbjFLRzF4N21GdzhTSVFPTUktMDM1cG5RdDBxUEJSOGtOall0UkRNMnBKTg?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQREZTS1hMYzJXdnNuUEt5QjdCQUZLSmpqU09sRDhLd05XX3Q1blhTMURVbDI2dUZnNFpsYjRobmZxMEEwdGZWVWJTS0pDM05rZFpVX1BOZnJLSF9fSU1PVUZaS1BIa3dMbkRqUEtWN1F3Yk9qZXBUVTlYdmFVWFZoR1Nld2Qwbzdyd1U3ckQ4amxqcTY0OG5BaEstUnkzNVlJUERF?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQRlVNeGxTREFDYlY2bEwtNjZKSGlma1FMWWNsNmtpWHhScHlCQXZQYzZrdlVtbjFvSFEyY2pPVURJZzNtSWl1T1dqYXdkcFF6Q1lBcjVZQ1R4b1ZseEdfeVRmODBQQ0lVaUFvSWpfd1VLRDBlQmVURVVFTEVxWEJMa1Jfb2lSNnhYRm1GcFJ4VW9oTk1hdWZYRkZTXzlueWpW?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQV3FvU0kxSnA1Q09RekNwSXJuelU4V3dhajNkRUxtT2lWa1lvekh0ZDNfN1NwT1NKSkY5ZDFzWlplY0ZMZWROVjM3MmpfcFdkSWo4MkZaWllGYjN5eWI1bGR4eTVhYW44VDBwXzlCVW5ndzVrRXV4WjBHLW9WeUxubkFSU1lhcnhxRTJhUzFkUkZUSjBtWjBGSA?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPRUZTaHN0QlFyYk9uM1pRZWtkcWV4T19femtzQ3FwWXpGQnhDZDh0WFdQUU1EREtESlhjeUVKRUpfTkxfUjVhVGFFNFFnSUJ6NEc4RWNoUkJqZ19WdlNUNDZMb3U3N3RKUzZKa24zaTd0dkM0R0VLdThfUThyM1lIU2NOdlRXSHJTVXJyeUxfS1AtUnZqaVotNElVakI2QQ?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTE5oby1RYnBMY0d5UnpHN2pfZG82SmlXMDRUOWs4d05vZVc3ZmlfVjdMZF9Qc0swYS1CYUJxZlpkOTBJZUJMaW1HMkQ5aW52Z3A3NjdGM2tmUkNodnc4MUJhVkEtMHlMWTdUeWtkSlAwbXFBYVluUzBxcHVZUQ?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNZXBrdnEtYnZLWk95RmJjZlRTeFR2ZjZDaGM5dDR4VW9KNWdDZjRjTmJidlY0eWExNVJVYUZ2NGJlNlo3NXZYMzFTZkhYeUU4ZC1RSGUzMXhLYkdkRUZXMEt5bVJRY1E0LW52Z0QzaWFYRTE3bDh1SVBMWnRNZUs0dndHVXBXdmZkYjBoRWFsX0p6RG8?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
