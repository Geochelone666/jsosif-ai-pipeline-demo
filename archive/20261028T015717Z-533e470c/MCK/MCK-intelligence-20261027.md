# MCK Intelligence Report

- ticker: **MCK**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/MCK/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCK/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:00:57.166449+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 6, 'ai': 2, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/MCK** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 7 named publishers; 1 exact duplicates; 12 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 967.0200 |
| Return 1D (%) | -2.6036 |
| Return 1W (%) | -6.1255 |
| Return 1M (%) | 11.5827 |
| Return YTD (%) | 18.2416 |
| Return 1Y (%) | 19.6425 |
| Annualized volatility (%) | 31.0791 |
| Beta vs SPY | -0.2832 |
| Max drawdown (%) | -27.1691 |
| Sharpe (rf=0) | 0.7302 |
| Downside deviation (rf=0, %) | 18.4412 |
| Sortino (rf=0) | 1.2306 |
| Historical VaR 95% (1D, %) | 2.5988 |
| Historical ES 95% (1D, %) | 3.6083 |
| Correlation vs SPY | -0.1157 |
| Tracking error vs SPY (%) | 34.9082 |
| P/E (trailing) | 25.92 |
| P/B | -26.46 |
| EV/EBITDA | 17.30 |
| Revenue growth (%) | 7.70 |
| Forward P/E (estimate) | 19.10 |
| Gross margin (%) | 3.63 |
| Operating margin (%) | 1.35 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 6.03 |
| MA50 | 914.5135 |
| Close vs MA50 (%) | 5.7415 |
| MA200 | 859.0746 |
| Close vs MA200 (%) | 12.5653 |
| RSI (14, Wilder) | 54.0728 |
| MACD (12,26) | 28.3587 |
| MACD signal (9) | 29.2033 |
| MACD histogram | -0.8446 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCK': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 967.0200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.6036 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -6.1255 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 11.5827 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 18.2416 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 19.6425 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.0791 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.4412 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.2306 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5988 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.6083 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1157 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.9082 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.2832 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.1691 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7302 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 19.0994 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 3.6330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 1.3480 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.0324 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.9185 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 54.0728 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.8446 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.7415 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 12.5653 -> Clearly above the moving-average trend level.

## TAILWINDS

### McKesson (MCK) Stock Dips While Market Gains: Key Facts
- Summary: McKesson (MCK) Stock Dips While Market Gains: Key Facts
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOUVo1eHd1dXQ2cEpOZG9ETkhlbXVJWHBpdkRXRG1rQmhSNjcxUDlzVTI3TXRRZ2llR3p1SUtnLWF6cWQ3d0piNmlWdmFRamlqNjNtY25XVDA0c3g4YVNIRW8zSEpzWDA4QWhxc0R3QnJUVXFOdXRBeVlRT1ljc2UtcS1uRlNwcDNQaUExWmdmN1ozOG5GUVFXY29B?oc=5>

### McKesson Stock Rides An 8-Day Winning Streak To An 11% Gain
- Summary: McKesson Stock Rides An 8-Day Winning Streak To An 11% Gain
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOOEJYM2NUQzVENzJvcExVMDBzbFpzaXlDbjFoNlRBd2VvSFNwUTBRM0FVR3BfT2FnTHlmM0gyWExVbkdjX25Md0M1MzNraFVCR0lpZllad0t4ZW11U1FDN0pYOHRUWnlrWGFYU1IwenBvNXNjQUd5dGdMNFlJZjRBTDVLQTRWV0pETGd2OVJLT3hTbUtDbFoxdVV0eTlsNlhuS3FEQldMUFJ6eEVKV0JfVUNaWWcxSFk0WlE?oc=5>

### 9 Green Days In A Row: McKesson Stock Is Up 13%
- Summary: McKesson shares gained 13% over nine consecutive trading days, indicating strong short‑term market momentum.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPS2puSEg0Q2ZwMm4xeXdjdUN6U0VrMDdVQlo1M09QRzBDSFZVbXJ2YTF4Mm1hcjA3NEhsOVpnbzJfeE16aG1jWjdhc2hGN1otMjE3YmVZNXN6R3hqSDYxcV80M1ctUWdrSDNFQXEwWS1UX3lMWGk0RzVDTVBSOExmZFZkcXQ3QVlYSHB5VWJkWHlTczRneWdDRVE4RloyZlJ6RjJLWEJ4LXQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### McKesson's Quarterly Earnings Preview: What You Need to Know
- Summary: McKesson's Quarterly Earnings Preview: What You Need to Know
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNU0NHUGdKaVNGejZBcmZwNFlUMERDS1l2blVqUTFwM05xQmE3bTBaS0hQNFA1X0YtV2JpdGZFeE5QWnpiUkM0bUN5Tl9vcUlSblBCVnROTU54cmc2NjdpeWhmNHNpaDZWbHdBV2dNV2tlMkhEWWxtUHZMLXR1Smx1aUxsdlNFSWs5bXkxUkdSelg3TDdnaXdfaW1wS2c0Smtrb2tjcg?oc=5>

### McKesson Corporation Declares Quarterly Dividend
- Summary: McKesson Corporation Declares Quarterly Dividend
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxQelRDSjlfQkk4MjlGTW1yNkFyZzJVSG04VFNuZjhoYWg1ZmFpbWIwaDhNeVZyWExRbmVqMWF4bnE0Rkw3S3BtaHJjUS1YbzVUYVpWb2gxX080MWpNamQwZXFwMGNvZkZlbk5aMGhWVFplWGdBSnItWEpXZU9OcWdJaldUSnY0UQ?oc=5>

### McKesson Corp (MCK) Maintains Quarterly Dividend Amid Strategic M&A Discussions
- Summary: McKesson Corp (MCK) Maintains Quarterly Dividend Amid Strategic M&A Discussions
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOeGJwOUltMEFVaVh3dUpMU0phLXNPZFdBVk9iaGFlT3dLanNvMG5PbWMzdlJ0UnFPTTF5am1FWFhneGQybnhkLVgyVXY5Um9sQ0k3TzJkbDBtMEF1MlE0cHBkZ0VXUnRUZWZjOXZkNXVwbHUtYUY4bjVoQVZCQVRweENUMkZKY3RzdGYxX2dXRUExMDd6YnVzd0wwbVpCYVg2cDlmcHFGcjJzUExybklwR3VZaG82QQ?oc=5>

### McKesson (MCK) 1% Over Fair Value As Dividend Reaffirmation Keeps Focus On Valuation
- Summary: McKesson (MCK) 1% Over Fair Value As Dividend Reaffirmation Keeps Focus On Valuation
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOMUNuWk5iVlFOendRV2gzN3hIY2J0S0tFUTd4WG1rNDJtN3dmazdVeG9CdUVkX3o2V1FBTWV5emdqWFV4UnNNTnBFWktzQ3NzYmhpMWdwdmt1NEFkbng1emozdTNodUpobFVsOVRvbHhZaUlPaFJhREd1bnRyYWprR1IwaGhRTE0tdEhvelpNc0ZvbkJYNHZLc1FYZjdiUWtjSnlTV1oxTXd6Qndpd1JySGZ6NTVaOUFpQ1diQkE0NWdtMTVO0gHKAUFVX3lxTE9WSGxUOEJ5V2lzVF85UTNvMzZBRHpqak1DTUcydHdlcWxacTh4VTRZZ1lxa0JKTFRUVjBVUERGWDl4MU5aWUgtUFpmWmU2cV9uZnJUamZFVC0xb3NoVjU0bzV6cVZFV0NKTnhkb0VLUGFRUWd0WlN3aDhRYVVTT2N2VVdxZlEyaHMwZUlDV04tSGxOMm5uTXliY2VkdnB1dmV4RjdZeUNpdTBTT0NQcGxLOFhINS1mdjNIdld6SzR3a09MeTVaUkRzMXc?oc=5>

### McKesson: AI And FDA Overhaul Likely To Overtake Regulatory Drag In 2027 (NYSE:MCK)
- Summary: Future AI and FDA changes may boost McKesson's regulatory efficiency.
- Date: 2026-10-22 | Impact: medium | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOUDdqeWI4NzVFNUY4aUNpclZ4MHhfWVQtS3R0a0lOSFI4N0RUV2xwTWhXYk1qM2dTWms0THBKTWtaRk9pamlmaElHa05iSXdUeHgxSUlYZEtyOHIwcUFtNExjTXpZZzdjaDY5cW0xUnV5V3JhYkw0SjlVN0tBcDU2ZGtGQjIyMGZBcjI4M1QwRGR2a0tzWXhNX0w5bU5hWWdBMGxkX1R4WUNxWnZ5ZWxmd193?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCK** | **25.92** | **-26.46** | **17.30** | **7.70** | **112,745,209,856.00 USD** | **19.64** |
| COR | 24.16 | 20.35 | 13.33 | 5.10 | 62,089,433,088.00 USD | -2.44 |
| CAH | 34.09 | -19.92 | 14.76 | 5.80 | 57,067,798,528.00 USD | 51.88 |
| CNC | N/A | 1.69 | 4.94 | 4.60 | 33,942,396,928.00 USD | 107.27 |

Peers fetched as_of: 2026-10-27; MCK reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-05
- Next expected earnings: 2026-11-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 29,980,000,000.00 USD; period 2011-04-01/2011-06-30; fiscal year/reporting period 2011/Q1
- Net income (latest available single quarter): 614,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/927653/000092765326000234/mck-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxOUVo1eHd1dXQ2cEpOZG9ETkhlbXVJWHBpdkRXRG1rQmhSNjcxUDlzVTI3TXRRZ2llR3p1SUtnLWF6cWQ3d0piNmlWdmFRamlqNjNtY25XVDA0c3g4YVNIRW8zSEpzWDA4QWhxc0R3QnJUVXFOdXRBeVlRT1ljc2UtcS1uRlNwcDNQaUExWmdmN1ozOG5GUVFXY29B?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNc1VSQkdGQXhLT0piYTVfRXhNbWI3ODlZci1nMnRXMW9CT0xBc1RBemxrOGdkXzRwZHoyQ0FlSGYyQy1OWUw3cWJwZ29KQWpmUTRDV2tjeTlxaTNObUhuNm5mLWZXZ1Jnb2JYak1MTnAzTGsweV9ZeUo5dkFvUGQzZDk2WVcyTS0xWTJDUENjYnpMMmtTWDNFMEp3?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOOEJYM2NUQzVENzJvcExVMDBzbFpzaXlDbjFoNlRBd2VvSFNwUTBRM0FVR3BfT2FnTHlmM0gyWExVbkdjX25Md0M1MzNraFVCR0lpZllad0t4ZW11U1FDN0pYOHRUWnlrWGFYU1IwenBvNXNjQUd5dGdMNFlJZjRBTDVLQTRWV0pETGd2OVJLT3hTbUtDbFoxdVV0eTlsNlhuS3FEQldMUFJ6eEVKV0JfVUNaWWcxSFk0WlE?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPS2puSEg0Q2ZwMm4xeXdjdUN6U0VrMDdVQlo1M09QRzBDSFZVbXJ2YTF4Mm1hcjA3NEhsOVpnbzJfeE16aG1jWjdhc2hGN1otMjE3YmVZNXN6R3hqSDYxcV80M1ctUWdrSDNFQXEwWS1UX3lMWGk0RzVDTVBSOExmZFZkcXQ3QVlYSHB5VWJkWHlTczRneWdDRVE4RloyZlJ6RjJLWEJ4LXQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNU0NHUGdKaVNGejZBcmZwNFlUMERDS1l2blVqUTFwM05xQmE3bTBaS0hQNFA1X0YtV2JpdGZFeE5QWnpiUkM0bUN5Tl9vcUlSblBCVnROTU54cmc2NjdpeWhmNHNpaDZWbHdBV2dNV2tlMkhEWWxtUHZMLXR1Smx1aUxsdlNFSWs5bXkxUkdSelg3TDdnaXdfaW1wS2c0Smtrb2tjcg?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxQelRDSjlfQkk4MjlGTW1yNkFyZzJVSG04VFNuZjhoYWg1ZmFpbWIwaDhNeVZyWExRbmVqMWF4bnE0Rkw3S3BtaHJjUS1YbzVUYVpWb2gxX080MWpNamQwZXFwMGNvZkZlbk5aMGhWVFplWGdBSnItWEpXZU9OcWdJaldUSnY0UQ?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOeGJwOUltMEFVaVh3dUpMU0phLXNPZFdBVk9iaGFlT3dLanNvMG5PbWMzdlJ0UnFPTTF5am1FWFhneGQybnhkLVgyVXY5Um9sQ0k3TzJkbDBtMEF1MlE0cHBkZ0VXUnRUZWZjOXZkNXVwbHUtYUY4bjVoQVZCQVRweENUMkZKY3RzdGYxX2dXRUExMDd6YnVzd0wwbVpCYVg2cDlmcHFGcjJzUExybklwR3VZaG82QQ?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOMUNuWk5iVlFOendRV2gzN3hIY2J0S0tFUTd4WG1rNDJtN3dmazdVeG9CdUVkX3o2V1FBTWV5emdqWFV4UnNNTnBFWktzQ3NzYmhpMWdwdmt1NEFkbng1emozdTNodUpobFVsOVRvbHhZaUlPaFJhREd1bnRyYWprR1IwaGhRTE0tdEhvelpNc0ZvbkJYNHZLc1FYZjdiUWtjSnlTV1oxTXd6Qndpd1JySGZ6NTVaOUFpQ1diQkE0NWdtMTVO0gHKAUFVX3lxTE9WSGxUOEJ5V2lzVF85UTNvMzZBRHpqak1DTUcydHdlcWxacTh4VTRZZ1lxa0JKTFRUVjBVUERGWDl4MU5aWUgtUFpmWmU2cV9uZnJUamZFVC0xb3NoVjU0bzV6cVZFV0NKTnhkb0VLUGFRUWd0WlN3aDhRYVVTT2N2VVdxZlEyaHMwZUlDV04tSGxOMm5uTXliY2VkdnB1dmV4RjdZeUNpdTBTT0NQcGxLOFhINS1mdjNIdld6SzR3a09MeTVaUkRzMXc?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxOUDdqeWI4NzVFNUY4aUNpclZ4MHhfWVQtS3R0a0lOSFI4N0RUV2xwTWhXYk1qM2dTWms0THBKTWtaRk9pamlmaElHa05iSXdUeHgxSUlYZEtyOHIwcUFtNExjTXpZZzdjaDY5cW0xUnV5V3JhYkw0SjlVN0tBcDU2ZGtGQjIyMGZBcjI4M1QwRGR2a0tzWXhNX0w5bU5hWWdBMGxkX1R4WUNxWnZ5ZWxmd193?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
