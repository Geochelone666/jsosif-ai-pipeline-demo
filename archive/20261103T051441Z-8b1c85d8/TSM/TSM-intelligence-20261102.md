# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:27:08.813879+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 1, 'ai': 15, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 398.6300 |
| Return 1D (%) | -1.8467 |
| Return 1W (%) | -6.0655 |
| Return 1M (%) | -15.6838 |
| Return YTD (%) | 32.2072 |
| Return 1Y (%) | 34.0908 |
| Annualized volatility (%) | 39.8122 |
| Beta vs SPY | 2.1874 |
| Max drawdown (%) | -21.5466 |
| Sharpe (rf=0) | 0.9041 |
| Downside deviation (rf=0, %) | 26.8619 |
| Sortino (rf=0) | 1.3400 |
| Historical VaR 95% (1D, %) | 4.2177 |
| Historical ES 95% (1D, %) | 5.2558 |
| Correlation vs SPY | 0.7045 |
| Tracking error vs SPY (%) | 32.0969 |
| P/E (trailing) | 25.83 |
| P/B | 76.08 |
| EV/EBITDA | 3.69 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 17.05 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 58.66 |
| Return on equity (%) | 41.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 434.1505 |
| Close vs MA50 (%) | -8.1816 |
| MA200 | 398.9474 |
| Close vs MA200 (%) | -0.0795 |
| RSI (14, Wilder) | 36.0837 |
| MACD (12,26) | -7.2679 |
| MACD signal (9) | -4.2410 |
| MACD histogram | -3.0269 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 398.6300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.8467 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -6.0655 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -15.6838 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 32.2072 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 34.0908 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 39.8122 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.8619 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3400 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2177 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.2558 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7045 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.0969 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1874 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.5466 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9041 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.0462 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 58.6550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8550 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.8347 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.0837 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.0269 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -8.1816 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.0795 -> Slightly below the moving-average trend level.

## TAILWINDS

### Why Did Taiwan Semiconductor Manufacturing (NYSE:TSM) Shares Drop?
- Summary: Explores reasons behind recent TSM share price decline, analyzing market factors and company performance.
- Date: 2026-11-01 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNUWxQTWdUN0RiZ1RWclVYTGU4T2plYkhPRWFNb1N0aTZGOWF6eVpGSEQxUGVLZEVDNEt3MENjSzcxcGxyRWs3b0NWX1RQSHVIRlRla1RrcG9VTVBCVzdUVXA4ekxydklCMGVTbVNrODRQLWxDUmlwdXlEX2xIdFZSSjVqRm52aEN0d1MzcW9OdWx4TmY4aHNhWVJnRU1zdWVBdDJzUUpaOTZieDQ?oc=5>

### Cathie Wood's weekly recap: loads TER, AVAV after strong results; books gain in AMD, TSM, LLY (ARKK:BATS)
- Summary: Cathie Wood reports book gains in TSM, indicating positive market sentiment.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxOYlBCVThOVlBqMGU5TUZqTkx6WGh0ZVdNTnBncEp3MXExWVppbkw5VndabDFncERwMGVjNFhfTHdtN3AtUjhXeE1QUDRnRlotY290VWtIRjRNaFhSQXZoODgySjFVU1pBMWFtYW9lTTZUZDBBYUhEMVF6MGQtVEtHVnNHNEJoOG5VMmxURHJpeFphZjhRdG5oWE44RVgzOEpLTmNPUGZwTXd6Snh6U3JrSDBhRWx0SkZ2bGlmV3ZmVlFTTUU?oc=5>

### TSMC’s $265B campus drives real estate boom in Phoenix, Bloomberg says
- Summary: TSMC’s new campus fuels Phoenix real estate growth, signaling expansion and investment momentum.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPQVBvc0gwMnRWM0FlMENCRzVndnVGWWRFc3ktOTluS2JJR0tIWHVXclVjNG1ENENQTUtBV2lsenFSbTVWQkxtM2o5ZmZlczBPLURXT2M1d18zSmdQcUJpRS1xUlp0SS12eDQ3SVJlcjFwZ2VWYVNFSG9sbEJJaVJTQTFzTTJqUTlaVi1xTlJKNEJLbG03bDhIQllseVdjZXE4UGpkcFFCRVRUam9oQ0ZTQ2lPZTlSTjR2?oc=5>

### Here’s What a $10,000 Investment in TSMC Stock Will Be Worth by 2030
- Summary: Projected $10,000 TSMC investment could grow significantly by 2030, indicating strong long‑term potential.
- Date: 2026-10-30 | Impact: high | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOU1hNeUxiYWNYT2JHOHRZVm9JOEx2RmtSU1I3SUV6emRrUmgzUmtvR2k0clBENDlDRTF6SEtIQTRGOVZ4Tm9wTVlDam01bklqRzljU1U0akEzNW5iOGY0cmZVU21QTWJkMlZvTVBHWVpVanhlTVFRQXAteGJ5SzlLcG9ublZqQkw1SlRVZ1BjUjkxWl92dXJvT3VaWWQ2R2lhU29BOVpBUGRXMnNzWGpsakRVRQ?oc=5>

### TSM Soars 33% in the Past Year: Is It a Solid Investment Proposition?
- Summary: TSM's 33% year‑to‑date rise suggests robust performance, supporting its investment appeal.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxQY0M3aGR2aklZX3dfdWVXZVVxR1lIREJEYTFOUWEtbGY0aFJRb3VVMkY0WTJ5b3M4cVNaX29aczM2aWsxSUNpNzNLWmE0cGhJNEtEZGpiRDV5NVZjSjFERGpWcS1STExudUR3WU01djU3bnJTcG5fS0RwWTRQUXV0NmZPMkNsdkE1Y2lod20tU2hIbVdORWNubHZjQk9xTUNfSjBXaVlodTJYdnJYTDZiX1Rwa2RCN3Y3MjR3aTFsSmJPNG9xVWlhZUcxZzVqWGsyMU8tdVNPSzV1WmV4SVNtRlByTlo?oc=5>

### If the AI Bubble Scare Gets Worse, This Is the Chip Stock I'd Still Hold
- Summary: Despite AI bubble concerns, the author maintains confidence in TSM, highlighting resilience.
- Date: 2026-10-30 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNSU1IMGY2WElySS1YWHNuclN0enIybWVCekVJVU82Z2lIdUh5NjFHZXpmZDl6TEV4SFloN0hmUGw0enpNTi1ENE1LV0xMNXJIV1I1eVh3QUZ3eEM5eThjODFLdW9MX1V4b3Ytam80cVpMOExkN2hKYmpFdjZYY3R6MlJLTVJQSFJyVGxBU2tZQkpweEZqZEluag?oc=5>

### Taiwan Semiconductor Manufacturing Company Ltd. (TSM) is Attracting Investor Attention: Here is What You Should Know
- Summary: TSM is drawing investor focus, offering insights into its market position.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPMlBUNlRGNktfa0JOdWxDeTFIZkdoMHhhaEkzSVRVek9acWpFNHpIYkN1dVBaVktiRXloUkcwVGtNSEdRT3AwdFdFMTJnTkNaLXFyT2p3LXF3WEVNaHo1cjdoaEszelBJbWJXbTR3NGIzTzhZSFFBUWN4SGo0aE9OcmFiWnM1R1ZsYzEtNFJFejVlMUlJR01QQU1TU0xwRE9GcklWakU1MUNWZXBBakpUTg?oc=5>

## HEADWINDS

### Taiwan Semiconductor Manufacturing Co Ltd (TSM) Stock Down 6.0% but Still Overvalued -- GF Score: 98/100
- Summary: Taiwan Semiconductor Manufacturing Co Ltd (TSM) Stock Down 6.0% but Still Overvalued -- GF Score: 98/100
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNanJjTkhQMUhmbFpvaGxmRzhsWTdNVDl2T1R2Ml82b0o2NGV3MjRhTy1neFlDSjR5dUlxSlg0c3RWUkhSWEY5UDI3UmFFXzk0cFNHOVRoUXdUUkh1MWNfbEwzMFhVRmpKVHJSbElOMm5JODdVcHhTMDVncURVQnVBT0ZaVlIwemc1ZTZKVDllSGVha3otWjVELVdBbHhzYWt2dTlrbFNIcUVnT19nZHhzbkVucmhPRmhLWkRmdi1GOEZlMUpCWEVuaVo2ZjZWMXc?oc=5>

### TSMC: The Cracks Are Showing (NYSE:TSM)
- Summary: Report indicates operational or financial challenges for TSM, raising concerns.
- Date: 2026-10-29 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMid0FVX3lxTE5NM2ZPNW5mb2NfMHdER3RRX2QyeVkwSDl3anVfdVdWUTQ4UkxyRHBxeGJ0QkFRb0tybEpVNWNXRXZwR0gyWm5UNV9PQUIwOWV5M0xVc1lxZXdKeTV2eFVzTWc1MUF0cEdtYW1NRTMyamVWX0t6V0Y0?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) Stock Looks Pricey Against Cash Flow
- Summary: Valuation concerns relative to cash flow.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxORldEaFpNSnljQTZVWGtRUmV3X0R2QTZQTE9pNm0yWDlremFDNV85cHVhRnlZTy02c2Zkd0dsTTE0Zkx4LWJibjZVR0RHWlhZdy1WcHRVZ2dHQlpHOWxGWEVHUnlJRU5mcFVhU1FnWXk5TzB4ZFdMYjkzRDctYjJ0d0tYeGxfbHlBU1ducHNRZEFOYkwzZy1TTXRGNjRkcDlZZTUwcDNLdlZXSGFsb3c?oc=5>

### TSMC Just Dropped 11% in a Month. Is It Time to Sell, or Load Up?
- Summary: TSMC shares fell 11% over a month, raising sell‑side concerns.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNMjFhR2kwWTJrRjYtVDVsdlVEYml2cGpTNUFocFNJaDZHcnE1Snh1dFh2VmVDNi1vM2h1c3NfakpoWVFzclQ4bDY1TnZ0a0lCZjZiMkRvQUF0c3hwVHR2TEc2SnhzTi1FZVVMRXRQdzVNbk0ta0lSRUtRQktyUW9hS3VCVEp4U0ZSbWc5OFFkYnQ?oc=5>

### 8 ETFs Cut Taiwan Semiconductor (TSM) Holdings on Thursday
- Summary: Eight ETFs reduced TSM holdings, signaling potential market caution.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOUkY5cnBtaDA0VDRiSWpibDAzVzktck92aXA0dkR4VENJal9URjhETVo4V05yLVExVGhpaU1JTnllNUxvcGxDdnVvUzFGQmZGQURpVWNhaU5jSGUwejhCY3FKVzFOekNyYnJBeWJwaWYxYkFseWJTV3BUaWoyLTYyVk15b29mdkRoQjdZTndkdWlfa2Q2bXpDdXZGa00?oc=5>

## CATALYSTS

### Beyond NVIDIA: Why TSMC Stock Looks Attractive After Q3 Earnings
- Summary: TSMC’s Q3 earnings boost investor interest, making the stock attractive.
- Date: 2026-10-28 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOTl9Qckw0VV9Ud2FBeDJiSnRJXzdhX2c0VGtNVklNTVZUNlZXaG14Q3VicGQ5SHhnUF9kYWRfZmNXNjJLUW9RMTdBb0d3VXlTejhyQVJsb3JLX3JjTTV0bkJlTnZ0bFEtSlZ6MkNoNDZVSHNwYktuWDF4YlBnNGlObk10WFY2enpwS0RRMk14aGFsTWVGZFdV?oc=5>

### SPCX Stock Jumps Overnight: Musk Reportedly Revives TSMC Terafab Talks — Says Capex Efficiency Is ‘Greatly Underestimated’
- Summary: Musk revives TSMC Terafab talks, citing underestimated capex efficiency.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQS05CMkZQSjAtMlQtWWtUb2xxbUJzTlpLSmREeDBhN1VndVlQZHRVVXJCZTNYeUp6U3VUekxnV3VFOEQ1UkRzV1NLSFFnRnpWaVlxdGdnSkRObmZvZElhRU1yT2xILXBEdWtqQmJjOG9SOFpHQUFpbkZIVWRSZkFqcVVXc0hOZ1dkTTE0SmJZckRvaVBBQk9OcjUyaVo?oc=5>

### Elon Musk 'Softened His Stance' as TSMC Eyes Terafab Role: Report - Tesla (NASDAQ:TSLA)
- Summary: Musk softens stance; TSMC considers Terafab role, signaling potential partnership.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOd1NpcDg1M21Zc2R1Vk9XbC1kZGFZNUtpRThyNWpxLVJXRmNRdFlHS0dpdUlhN2ZtbW40YjB2R2xrTUl2WWRSQWhoc1pYaTc5X2FEdGI0MHJMLVRRT05WQlpkTXpyN2FGM1d6RzNsZFNoNHN2SWwtODR4OG52X0hZTHVhb1pTZHdwYVNSUEhEOEY3LVd1cUVxUEhRcGRZQQ?oc=5>

### Musk may soften Terafab control stance in fresh TSMC talks
- Summary: Potential shift in Terafab control could open new partnership opportunities for TSMC.
- Date: 2026-11-02 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPNWFrSy1PcGw2ODU0OHVRdmtoMDd5b2pTM3VfaDdVNVg5N24zNXZ2OGNveWpSN01wbUhJT1VJSERldjRlS0NVSkh6NTg4WmtjLVBPbklxM19EY09xWWZrLTdVR1JxSnd6cC1ORWJTejBBbV9EU290bkMybWFNNGRZdjNRYVFuZXNBM3ktWlhLbUF0Z1pLb0ZZ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **25.83** | **76.08** | **3.69** | **50.90** | **2,067,484,114,944.00 USD** | **34.09** |
| UMC | 15.46 | 2.83 | -0.26 | 25.60 | 41,102,741,504.00 USD | 116.32 |
| GFS | 32.67 | 1.94 | 11.27 | 5.80 | 23,311,247,360.00 USD | 17.94 |
| INTC | N/A | 2.77 | 17.32 | 20.90 | 318,740,529,152.00 USD | 49.96 |

Peers fetched as_of: 2026-11-02; TSM reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNUWxQTWdUN0RiZ1RWclVYTGU4T2plYkhPRWFNb1N0aTZGOWF6eVpGSEQxUGVLZEVDNEt3MENjSzcxcGxyRWs3b0NWX1RQSHVIRlRla1RrcG9VTVBCVzdUVXA4ekxydklCMGVTbVNrODRQLWxDUmlwdXlEX2xIdFZSSjVqRm52aEN0d1MzcW9OdWx4TmY4aHNhWVJnRU1zdWVBdDJzUUpaOTZieDQ?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxOYlBCVThOVlBqMGU5TUZqTkx6WGh0ZVdNTnBncEp3MXExWVppbkw5VndabDFncERwMGVjNFhfTHdtN3AtUjhXeE1QUDRnRlotY290VWtIRjRNaFhSQXZoODgySjFVU1pBMWFtYW9lTTZUZDBBYUhEMVF6MGQtVEtHVnNHNEJoOG5VMmxURHJpeFphZjhRdG5oWE44RVgzOEpLTmNPUGZwTXd6Snh6U3JrSDBhRWx0SkZ2bGlmV3ZmVlFTTUU?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPQVBvc0gwMnRWM0FlMENCRzVndnVGWWRFc3ktOTluS2JJR0tIWHVXclVjNG1ENENQTUtBV2lsenFSbTVWQkxtM2o5ZmZlczBPLURXT2M1d18zSmdQcUJpRS1xUlp0SS12eDQ3SVJlcjFwZ2VWYVNFSG9sbEJJaVJTQTFzTTJqUTlaVi1xTlJKNEJLbG03bDhIQllseVdjZXE4UGpkcFFCRVRUam9oQ0ZTQ2lPZTlSTjR2?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOU1hNeUxiYWNYT2JHOHRZVm9JOEx2RmtSU1I3SUV6emRrUmgzUmtvR2k0clBENDlDRTF6SEtIQTRGOVZ4Tm9wTVlDam01bklqRzljU1U0akEzNW5iOGY0cmZVU21QTWJkMlZvTVBHWVpVanhlTVFRQXAteGJ5SzlLcG9ublZqQkw1SlRVZ1BjUjkxWl92dXJvT3VaWWQ2R2lhU29BOVpBUGRXMnNzWGpsakRVRQ?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxQY0M3aGR2aklZX3dfdWVXZVVxR1lIREJEYTFOUWEtbGY0aFJRb3VVMkY0WTJ5b3M4cVNaX29aczM2aWsxSUNpNzNLWmE0cGhJNEtEZGpiRDV5NVZjSjFERGpWcS1STExudUR3WU01djU3bnJTcG5fS0RwWTRQUXV0NmZPMkNsdkE1Y2lod20tU2hIbVdORWNubHZjQk9xTUNfSjBXaVlodTJYdnJYTDZiX1Rwa2RCN3Y3MjR3aTFsSmJPNG9xVWlhZUcxZzVqWGsyMU8tdVNPSzV1WmV4SVNtRlByTlo?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNSU1IMGY2WElySS1YWHNuclN0enIybWVCekVJVU82Z2lIdUh5NjFHZXpmZDl6TEV4SFloN0hmUGw0enpNTi1ENE1LV0xMNXJIV1I1eVh3QUZ3eEM5eThjODFLdW9MX1V4b3Ytam80cVpMOExkN2hKYmpFdjZYY3R6MlJLTVJQSFJyVGxBU2tZQkpweEZqZEluag?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPMlBUNlRGNktfa0JOdWxDeTFIZkdoMHhhaEkzSVRVek9acWpFNHpIYkN1dVBaVktiRXloUkcwVGtNSEdRT3AwdFdFMTJnTkNaLXFyT2p3LXF3WEVNaHo1cjdoaEszelBJbWJXbTR3NGIzTzhZSFFBUWN4SGo0aE9OcmFiWnM1R1ZsYzEtNFJFejVlMUlJR01QQU1TU0xwRE9GcklWakU1MUNWZXBBakpUTg?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxNanJjTkhQMUhmbFpvaGxmRzhsWTdNVDl2T1R2Ml82b0o2NGV3MjRhTy1neFlDSjR5dUlxSlg0c3RWUkhSWEY5UDI3UmFFXzk0cFNHOVRoUXdUUkh1MWNfbEwzMFhVRmpKVHJSbElOMm5JODdVcHhTMDVncURVQnVBT0ZaVlIwemc1ZTZKVDllSGVha3otWjVELVdBbHhzYWt2dTlrbFNIcUVnT19nZHhzbkVucmhPRmhLWkRmdi1GOEZlMUpCWEVuaVo2ZjZWMXc?oc=5
- https://news.google.com/rss/articles/CBMid0FVX3lxTE5NM2ZPNW5mb2NfMHdER3RRX2QyeVkwSDl3anVfdVdWUTQ4UkxyRHBxeGJ0QkFRb0tybEpVNWNXRXZwR0gyWm5UNV9PQUIwOWV5M0xVc1lxZXdKeTV2eFVzTWc1MUF0cEdtYW1NRTMyamVWX0t6V0Y0?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxORldEaFpNSnljQTZVWGtRUmV3X0R2QTZQTE9pNm0yWDlremFDNV85cHVhRnlZTy02c2Zkd0dsTTE0Zkx4LWJibjZVR0RHWlhZdy1WcHRVZ2dHQlpHOWxGWEVHUnlJRU5mcFVhU1FnWXk5TzB4ZFdMYjkzRDctYjJ0d0tYeGxfbHlBU1ducHNRZEFOYkwzZy1TTXRGNjRkcDlZZTUwcDNLdlZXSGFsb3c?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNMjFhR2kwWTJrRjYtVDVsdlVEYml2cGpTNUFocFNJaDZHcnE1Snh1dFh2VmVDNi1vM2h1c3NfakpoWVFzclQ4bDY1TnZ0a0lCZjZiMkRvQUF0c3hwVHR2TEc2SnhzTi1FZVVMRXRQdzVNbk0ta0lSRUtRQktyUW9hS3VCVEp4U0ZSbWc5OFFkYnQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOUkY5cnBtaDA0VDRiSWpibDAzVzktck92aXA0dkR4VENJal9URjhETVo4V05yLVExVGhpaU1JTnllNUxvcGxDdnVvUzFGQmZGQURpVWNhaU5jSGUwejhCY3FKVzFOekNyYnJBeWJwaWYxYkFseWJTV3BUaWoyLTYyVk15b29mdkRoQjdZTndkdWlfa2Q2bXpDdXZGa00?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOTl9Qckw0VV9Ud2FBeDJiSnRJXzdhX2c0VGtNVklNTVZUNlZXaG14Q3VicGQ5SHhnUF9kYWRfZmNXNjJLUW9RMTdBb0d3VXlTejhyQVJsb3JLX3JjTTV0bkJlTnZ0bFEtSlZ6MkNoNDZVSHNwYktuWDF4YlBnNGlObk10WFY2enpwS0RRMk14aGFsTWVGZFdV?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQS05CMkZQSjAtMlQtWWtUb2xxbUJzTlpLSmREeDBhN1VndVlQZHRVVXJCZTNYeUp6U3VUekxnV3VFOEQ1UkRzV1NLSFFnRnpWaVlxdGdnSkRObmZvZElhRU1yT2xILXBEdWtqQmJjOG9SOFpHQUFpbkZIVWRSZkFqcVVXc0hOZ1dkTTE0SmJZckRvaVBBQk9OcjUyaVo?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOd1NpcDg1M21Zc2R1Vk9XbC1kZGFZNUtpRThyNWpxLVJXRmNRdFlHS0dpdUlhN2ZtbW40YjB2R2xrTUl2WWRSQWhoc1pYaTc5X2FEdGI0MHJMLVRRT05WQlpkTXpyN2FGM1d6RzNsZFNoNHN2SWwtODR4OG52X0hZTHVhb1pTZHdwYVNSUEhEOEY3LVd1cUVxUEhRcGRZQQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPNWFrSy1PcGw2ODU0OHVRdmtoMDd5b2pTM3VfaDdVNVg5N24zNXZ2OGNveWpSN01wbUhJT1VJSERldjRlS0NVSkh6NTg4WmtjLVBPbklxM19EY09xWWZrLTdVR1JxSnd6cC1ORWJTejBBbV9EU290bkMybWFNNGRZdjNRYVFuZXNBM3ktWlhLbUF0Z1pLb0ZZ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
