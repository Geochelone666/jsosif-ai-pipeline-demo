# SCHW Intelligence Report

- ticker: **SCHW**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/SCHW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SCHW/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:46:39.422245+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 1, 'ai': 10, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261110T055129Z-abd33250/SCHW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 6 named publishers; 0 exact duplicates; 15 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-03

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 93.0300 |
| Return 1D (%) | 0.3235 |
| Return 1W (%) | 4.2003 |
| Return 1M (%) | -3.7952 |
| Return YTD (%) | -5.9631 |
| Return 1Y (%) | -1.4239 |
| Annualized volatility (%) | 25.9242 |
| Beta vs SPY | 0.4553 |
| Max drawdown (%) | -22.5253 |
| Sharpe (rf=0) | 0.0749 |
| Downside deviation (rf=0, %) | 19.7150 |
| Sortino (rf=0) | 0.0985 |
| Historical VaR 95% (1D, %) | 2.5523 |
| Historical ES 95% (1D, %) | 3.9505 |
| Correlation vs SPY | 0.2401 |
| Tracking error vs SPY (%) | 26.2446 |
| P/E (trailing) | 15.90 |
| P/B | 3.55 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 16.90 |
| Forward P/E (estimate) | 11.92 |
| Gross margin (%) | 97.51 |
| Operating margin (%) | 52.80 |
| Return on equity (%) | 21.11 |
| Free cash flow yield (%) | N/A |
| MA50 | 97.8048 |
| Close vs MA50 (%) | -4.8820 |
| MA200 | 96.8400 |
| Close vs MA200 (%) | -3.9343 |
| RSI (14, Wilder) | 49.2263 |
| MACD (12,26) | -1.4924 |
| MACD signal (9) | -2.3093 |
| MACD histogram | 0.8169 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SCHW': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 93.0300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.3235 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.2003 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.7952 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.9631 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -1.4239 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.9242 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.7150 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.0985 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5523 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9505 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2401 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.2446 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4553 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -22.5253 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0749 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.9221 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.5060 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 52.7960 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 21.1130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.9026 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 49.2263 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.8169 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -4.8820 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -3.9343 -> Slightly below the moving-average trend level.

## TAILWINDS

### Eligible Charles Schwab clients can now trade five cryptocurrencies
- Summary: Schwab expands crypto trading to clients.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOOUxpUDlrMFpvVk5xR1daQ0NpWW1ybHZISEhBdHBEQXQ2b3BRc0FMWlFsbDBTWTZVYzhUaU1sdC1WUDkxTjhkdWFfc1dZYS14ZUtMd1hCNFdFNW9FLUFCT3IxaFZLU2FjM3VSWDU3U2UtZkZNZjNpY2Zna09rYzBfT3A5cG16cjVsVDBlY05PNXhpR2dHY2tfYjJma1RzQ2ZpeS1aR2pUTlQxaEJma0pEb3BpcmU2TFUwZFJj?oc=5>

### Charles Schwab Expands Crypto Offerings
- Summary: Schwab broadens crypto services, adding new products for clients.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNZHZ6S0FMbUwyYkh3VUgtR2NGejNBbHozNDUzUmlhcnhsUC1jX1BZWHUyZFFkczZyX19uR1ZETG41RWwxV3F1R2dmeHRxUDFwOE1ndWltRWFFOXl4ZDFhUjlteTJha1pvaDR6eXhnZC1UMVVVeFZYSThXVHlrNE9sY3QxeHhCRkZaZXlNTXJrcUJIRlBWQVF4SmxUa3pzM1IyRVpZUzhfQQ?oc=5>

## HEADWINDS

### Charles Schwab (SCHW) co-chairman sells 11,675 shares; his trust retains 53.3M.
- Summary: Insider sale of shares by co-chairman.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNWnZLUG1QS3A2UTJDVG9DeGJBS0RicHBlbUtlOFIxVTdzVHh5Z21vQzNoeWZPb3lnOHQtZ2VsRnRRdV9zdXlCZWFRbHpRTFV1REFfNEZQT1dPdmVvWjU0S3p2VGpVRWN1RXpPUU5TTklBNkNhRWFfZ1Nqd01LWThwMmc0ODk2NzBrcEo3VG9SRXhXNmhIbFhnWHRVRWd4N05kb2hjS0tmNTZkaHhUQ1FpdWxvQQ?oc=5>

## CATALYSTS

### Charles Schwab Stock: Analyst Estimates & Ratings
- Summary: Charles Schwab Stock: Analyst Estimates & Ratings
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPRm4td3hlLWZLcmNzT3ctaXJMbjhiX3BQX003dm1mQ0F6dXdySGJmZUhZUjVNR3U5VE9MZDFoQUFyYlUzN2cwZmR0NUdIaGh6RDBMeWlTdVFPQllDY19pZERlR0tHQUQ0UzZUTUp2MENqUWZnWGNNLV91TUlodDQzSURaamZtVFZoSGkxZUlGTUJvSWdwNm1aYjJoQTg3bUVIN3JubjZB?oc=5>

### Charles Schwab (SCHW) Lowers IPO Minimum Investment Amid Anthropic Buzz
- Summary: Schwab reduces IPO minimum, easing entry for investors.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPQ29zV0V4TTc0S05jU2w2WkNUeHpnRGx1RXJEVmdXLTlQQ3VVaVBhdVNpb0dVcmUxblVlQ1pXZlRTUWFFVlVpSUlEa0lWM3ZvNkViT2g2RkZ3QU1nQ2QtSVR2eHA3ZXllMWg0TEJDbXY4VkswbUV1MnA5STZuVmRRMzM1LU02SjU2ZVpCNGdhdkN0UzNjc2N3aTZPN2ZodHVjZ2JMa0g0TDhfbzNP?oc=5>

### The Charles Schwab Corporation $SCHW Stock: Candriam S.C.A. Trims Position
- Summary: Candriam S.C.A. reduced its Schwab holdings, selling shares.
- Date: 2026-11-08 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxQbkFhVF9kcm5wWEt2aVRtaUVwZy1SZ0Z1OHUxTDBuQWYteUc3TzNwTHYxeDJpRTN0RWZjSzNtcVR0SVRmUkFabTBaMjcxOUJTcXBVX3NqYVBoaldLWERLRWdwdTJpaTU1QUtfOGdoS3RyX1lxM2VWRWR2aHRaVUd5SjF0WVZ3THc5OUR0SUk5V1lXSEdNZ2xVcHoxMk1JZlZRemhmY1dpZDJyOVNfNklrRUVvb3lxaERUY3N6QVhSemN1cVBmSXFlMExn?oc=5>

### Pictet Asset Management Holding SA Sells 81,570 Shares of The Charles Schwab Corporation $SCHW
- Summary: Pictet Asset Management sold 81,570 Schwab shares.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxQTml2WXlsR0NzSFpaUXl1bS15cGNHQjU1bVlxc3FzZk5HT3dkbVJXNG12c3F2TE1STVRmMFdYNmtYcURtSEVacDhZdzFsQUNpVmg4UUZaN0JvSUFCYmNYU0pxVkNKcG5VMU12OFJiU1gtQWc5NVNtNHJsWDlYUFVheTNTMERlUGJ4WnU2eHdkRHBSb3RUZkQ5Vk9aM3p4QnRMMUFpSjlxQmZubHF5V0djLVpHZUFHc1FLWHBnOTRMX3F3M21SS0lEQVFSYmNPNzVCei1VWjZ6YlpDdU9yNUdKNEpMWXd3YVpl?oc=5>

### 11,647 Shares of The Charles Schwab Corporation $SCHW Purchased by Waycross Partners LLC
- Summary: Waycross Partners bought 11,647 Schwab shares.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxOYUlwVzNGbXc2MVJmeVpFa2tJcHVheDF6UmdCRmp6ekhVaGI1UEQzTDAtemtsY0dRWGFwUjdTNVFHUXZLR1BhWFBjVVNFU0I3UVpMZ1MxcnVVc1lxZTNjYmtsckJKMHkwMWhZUEcwcDg5d2hXVEVOVFpoQmNqNHl6NUtkZFpINzM3VmUzZVo3SGh6Q05yVW15Y01sMDctWldKUDEwd0RrdEVpU2ZBU2pBOGRjRlM0MXF4cGZYOGdRajQwN2x0LWNNTF9GaEtTY2gzWmpVUWVpc0JLd2pRcnN3YQ?oc=5>

### The Charles Schwab Corporation $SCHW Stock Holdings Boosted by Kinsale Capital Group Inc.
- Summary: Kinsale Capital Group increased its stake in Schwab, raising its holdings.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxOMjdDd1BjZ0lteGNGcDRUUmYteDBmemNXSjlaUjhDZ05xLXhQU0tyZDZ2ekk0dUVmc01tTUlzaXBFVEJaUHF5ekNBWERqbjFfNzlZYnIwbTdEbmNwTTlMSmE2cWJGY3RtRjV4X3hxZzJsQTB6bnBBclpKT09DNVVsWEZ2ZEFJeXBGLWg2MDMtRnNRX1NJMjdZMWU2cDVhbm5pUHF5Uk5XSFVfOVpTSm5XV3dIZUlsRTQ3UmZvZTdNTUdTQW8weUZSWE9oc05BNldHSTc4QXRuZERMYlJIV0h3TU53?oc=5>

### The Charles Schwab Corporation $SCHW Stock Sold by Kohmann Bosshard Financial Services LLC
- Summary: Kohmann Bosshard Financial Services sold its Schwab shares, reducing its holdings.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxOWlhqTEk1bnVLTElCYlVxYmVPRlo5d2JNZ2RueVNPTE9GUk5XOFpGYXNhbGN1TzFVZ0VpWExkUjVIMUNyNEZiVXhPR3k3NlVrdDN1ZGs1TGp3OFFsY004VWd4STBCRnNTZXU4RzVndVJLcVZoS2VTcTZyTHBwT2o1RGI0N1VQQ1hvSzNBLU1kc2pQaERZdGxTcjBSMC1XRWhrY19Lb1ZCUUxMZDl1YWZaT3lqSVhYdl8yR2VhU1YxRjF2VE1oYUg2YVJpeXpRNHdUVTRsLUtNeFNwSXppTFo4SnpoY3g?oc=5>

### The Charles Schwab Corporation $SCHW Stock: Allen Investment Management LLC Reduces Stake
- Summary: Allen Investment Management decreased its Schwab holdings.
- Date: 2026-11-08 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxOcTU3Y290Y2xPVXdaeVRBZmlDcEhiQUVwanhMSk1ibGF1QVlKSmtZeTNZMTMxQWZuaDZCWVdSZmF0WnVTZjdFcXgwd1BrYWlIcElYZkxlWDZHZU9UNk9nTXNubXVTSFFMejlvVUhZTE9TV3NJRXJ1SGt3WVN0WDlvWXpCNDFzaDVjNkRVUHFaSlNVV2U0cldHcV9NY2JCbGFKZm4zT29kdW1YUUFGaUJ1SW5qTFJmUWtjdmtUVEtmYlJKQUxmVndVRzZsbHpRQ1d5Zjg0RDFnMFZ0SHhCUVRkZWt3?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SCHW** | **15.90** | **3.55** | **N/A** | **16.90** | **160,570,490,880.00 USD** | **-1.42** |
| IBKR | 29.61 | 5.66 | N/A | 13.50 | 132,201,029,632.00 USD | 9.54 |
| HOOD | 38.36 | 7.33 | N/A | 11.80 | 73,236,955,136.00 USD | -40.15 |
| LPLA | 17.51 | 4.16 | N/A | 17.80 | 24,023,185,408.00 USD | -17.51 |

Peers fetched as_of: 2026-11-10; SCHW reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-10

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-06
- Revenue (latest available single quarter): 7,171,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,906,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/316709/000031670926000038/schw-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOOUxpUDlrMFpvVk5xR1daQ0NpWW1ybHZISEhBdHBEQXQ2b3BRc0FMWlFsbDBTWTZVYzhUaU1sdC1WUDkxTjhkdWFfc1dZYS14ZUtMd1hCNFdFNW9FLUFCT3IxaFZLU2FjM3VSWDU3U2UtZkZNZjNpY2Zna09rYzBfT3A5cG16cjVsVDBlY05PNXhpR2dHY2tfYjJma1RzQ2ZpeS1aR2pUTlQxaEJma0pEb3BpcmU2TFUwZFJj?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNZHZ6S0FMbUwyYkh3VUgtR2NGejNBbHozNDUzUmlhcnhsUC1jX1BZWHUyZFFkczZyX19uR1ZETG41RWwxV3F1R2dmeHRxUDFwOE1ndWltRWFFOXl4ZDFhUjlteTJha1pvaDR6eXhnZC1UMVVVeFZYSThXVHlrNE9sY3QxeHhCRkZaZXlNTXJrcUJIRlBWQVF4SmxUa3pzM1IyRVpZUzhfQQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxNWnZLUG1QS3A2UTJDVG9DeGJBS0RicHBlbUtlOFIxVTdzVHh5Z21vQzNoeWZPb3lnOHQtZ2VsRnRRdV9zdXlCZWFRbHpRTFV1REFfNEZQT1dPdmVvWjU0S3p2VGpVRWN1RXpPUU5TTklBNkNhRWFfZ1Nqd01LWThwMmc0ODk2NzBrcEo3VG9SRXhXNmhIbFhnWHRVRWd4N05kb2hjS0tmNTZkaHhUQ1FpdWxvQQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPRm4td3hlLWZLcmNzT3ctaXJMbjhiX3BQX003dm1mQ0F6dXdySGJmZUhZUjVNR3U5VE9MZDFoQUFyYlUzN2cwZmR0NUdIaGh6RDBMeWlTdVFPQllDY19pZERlR0tHQUQ0UzZUTUp2MENqUWZnWGNNLV91TUlodDQzSURaamZtVFZoSGkxZUlGTUJvSWdwNm1aYjJoQTg3bUVIN3JubjZB?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPQ29zV0V4TTc0S05jU2w2WkNUeHpnRGx1RXJEVmdXLTlQQ3VVaVBhdVNpb0dVcmUxblVlQ1pXZlRTUWFFVlVpSUlEa0lWM3ZvNkViT2g2RkZ3QU1nQ2QtSVR2eHA3ZXllMWg0TEJDbXY4VkswbUV1MnA5STZuVmRRMzM1LU02SjU2ZVpCNGdhdkN0UzNjc2N3aTZPN2ZodHVjZ2JMa0g0TDhfbzNP?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxQbkFhVF9kcm5wWEt2aVRtaUVwZy1SZ0Z1OHUxTDBuQWYteUc3TzNwTHYxeDJpRTN0RWZjSzNtcVR0SVRmUkFabTBaMjcxOUJTcXBVX3NqYVBoaldLWERLRWdwdTJpaTU1QUtfOGdoS3RyX1lxM2VWRWR2aHRaVUd5SjF0WVZ3THc5OUR0SUk5V1lXSEdNZ2xVcHoxMk1JZlZRemhmY1dpZDJyOVNfNklrRUVvb3lxaERUY3N6QVhSemN1cVBmSXFlMExn?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxQTml2WXlsR0NzSFpaUXl1bS15cGNHQjU1bVlxc3FzZk5HT3dkbVJXNG12c3F2TE1STVRmMFdYNmtYcURtSEVacDhZdzFsQUNpVmg4UUZaN0JvSUFCYmNYU0pxVkNKcG5VMU12OFJiU1gtQWc5NVNtNHJsWDlYUFVheTNTMERlUGJ4WnU2eHdkRHBSb3RUZkQ5Vk9aM3p4QnRMMUFpSjlxQmZubHF5V0djLVpHZUFHc1FLWHBnOTRMX3F3M21SS0lEQVFSYmNPNzVCei1VWjZ6YlpDdU9yNUdKNEpMWXd3YVpl?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxOYUlwVzNGbXc2MVJmeVpFa2tJcHVheDF6UmdCRmp6ekhVaGI1UEQzTDAtemtsY0dRWGFwUjdTNVFHUXZLR1BhWFBjVVNFU0I3UVpMZ1MxcnVVc1lxZTNjYmtsckJKMHkwMWhZUEcwcDg5d2hXVEVOVFpoQmNqNHl6NUtkZFpINzM3VmUzZVo3SGh6Q05yVW15Y01sMDctWldKUDEwd0RrdEVpU2ZBU2pBOGRjRlM0MXF4cGZYOGdRajQwN2x0LWNNTF9GaEtTY2gzWmpVUWVpc0JLd2pRcnN3YQ?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxOMjdDd1BjZ0lteGNGcDRUUmYteDBmemNXSjlaUjhDZ05xLXhQU0tyZDZ2ekk0dUVmc01tTUlzaXBFVEJaUHF5ekNBWERqbjFfNzlZYnIwbTdEbmNwTTlMSmE2cWJGY3RtRjV4X3hxZzJsQTB6bnBBclpKT09DNVVsWEZ2ZEFJeXBGLWg2MDMtRnNRX1NJMjdZMWU2cDVhbm5pUHF5Uk5XSFVfOVpTSm5XV3dIZUlsRTQ3UmZvZTdNTUdTQW8weUZSWE9oc05BNldHSTc4QXRuZERMYlJIV0h3TU53?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxOWlhqTEk1bnVLTElCYlVxYmVPRlo5d2JNZ2RueVNPTE9GUk5XOFpGYXNhbGN1TzFVZ0VpWExkUjVIMUNyNEZiVXhPR3k3NlVrdDN1ZGs1TGp3OFFsY004VWd4STBCRnNTZXU4RzVndVJLcVZoS2VTcTZyTHBwT2o1RGI0N1VQQ1hvSzNBLU1kc2pQaERZdGxTcjBSMC1XRWhrY19Lb1ZCUUxMZDl1YWZaT3lqSVhYdl8yR2VhU1YxRjF2VE1oYUg2YVJpeXpRNHdUVTRsLUtNeFNwSXppTFo4SnpoY3g?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxOcTU3Y290Y2xPVXdaeVRBZmlDcEhiQUVwanhMSk1ibGF1QVlKSmtZeTNZMTMxQWZuaDZCWVdSZmF0WnVTZjdFcXgwd1BrYWlIcElYZkxlWDZHZU9UNk9nTXNubXVTSFFMejlvVUhZTE9TV3NJRXJ1SGt3WVN0WDlvWXpCNDFzaDVjNkRVUHFaSlNVV2U0cldHcV9NY2JCbGFKZm4zT29kdW1YUUFGaUJ1SW5qTFJmUWtjdmtUVEtmYlJKQUxmVndVRzZsbHpRQ1d5Zjg0RDFnMFZ0SHhCUVRkZWt3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
