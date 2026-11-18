# SCHW Intelligence Report

- ticker: **SCHW**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/SCHW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SCHW/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:01:49.386290+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 6, 'rule': 0, 'ai': 6, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/SCHW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 6 unique headlines; 4 named publishers; 0 exact duplicates; 6 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-12

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 91.8400 |
| Return 1D (%) | -1.1836 |
| Return 1W (%) | -0.9335 |
| Return 1M (%) | 0.2192 |
| Return YTD (%) | -6.8410 |
| Return 1Y (%) | 1.2678 |
| Annualized volatility (%) | 25.7176 |
| Beta vs SPY | 0.4157 |
| Max drawdown (%) | -22.5253 |
| Sharpe (rf=0) | 0.1786 |
| Downside deviation (rf=0, %) | 19.4471 |
| Sortino (rf=0) | 0.2362 |
| Historical VaR 95% (1D, %) | 2.5277 |
| Historical ES 95% (1D, %) | 3.9438 |
| Correlation vs SPY | 0.2228 |
| Tracking error vs SPY (%) | 26.3327 |
| P/E (trailing) | 15.89 |
| P/B | 3.50 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 16.90 |
| Forward P/E (estimate) | 11.77 |
| Gross margin (%) | 97.51 |
| Operating margin (%) | 51.11 |
| Return on equity (%) | 21.11 |
| Free cash flow yield (%) | N/A |
| MA50 | 95.8726 |
| Close vs MA50 (%) | -4.2062 |
| MA200 | 96.2459 |
| Close vs MA200 (%) | -4.5778 |
| RSI (14, Wilder) | 46.6205 |
| MACD (12,26) | -0.7587 |
| MACD signal (9) | -1.3903 |
| MACD histogram | 0.6316 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SCHW': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 91.8400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.1836 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.9335 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.2192 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -6.8410 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 1.2678 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.7176 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.4471 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2362 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5277 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9438 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2228 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.3327 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4157 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -22.5253 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1786 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.7671 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.5060 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 51.1070 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 21.1130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.8893 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 46.6205 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6316 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -4.2062 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -4.5778 -> Slightly below the moving-average trend level.

## TAILWINDS

### Analysts’ Top Financial Picks: Corebridge Financial, Inc. (CRBG), Charles Schwab (SCHW)
- Summary: Analysts highlight Schwab as a top pick, signaling confidence in its prospects.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi9gFBVV95cUxNSks0N0dQOVJKeEltWlJYRHlxeU01amNFZVhxUWg5WDVpNDBiSVpHWXlLR0IzNl8xT1VlTXBYREkwdkljVjE1VlhsZzlhRU9zT2xLSDZ2My1pcG5JYnRFdHBSd1dCT2dRMEFENUVmYWRGQk1veVUyQmpLZzZQVzZ6UzBVbVRxZGEwUURWWEdvQnBqcmFJbzhJdHNSYUJNckRZalkwb1QwdGh2R3J4Ry1EbE1CcUxrdEs2UWlMczRaUHBMQWt4a3pjaVltWVplWF9PbWRVMEV0cTNZVGlFVWpPdFRLNjNrZjNhYjZ5RkhSTHRXbDZHeUE?oc=5>

### How Investors May Respond To Schwab (SCHW) Record Client Asset Growth
- Summary: Schwab’s record client asset growth may boost investor confidence and attract more capital, supporting future revenue growth.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxQT2M3QVo2bUhsc3RKeG1hXzlXdHN1UXFlclpNSVpPRWpvMlRYZDV4UnNfYmN6cFEzUDdfOW13aElFQzFfamk5eXRJRm5jejdVcllyX0RmVEJaYmFmREo4OW8zaTkxbTB1R3RzV2ZJWFhDekFwN045WFduODA5RVYyblNWcnFUU1BpV19zNnFwdHd0ekMzSlhOV0hxM1hXTFlZeVFiWDhNdTVhYjVZTXI4T2l3UV8zdHpmdGFnN2VVMHp1QUpZdUw0Vnh1c0JmLWNQd0duMU52Qnl0V2RvUHfSAeMBQVVfeXFMTlU0NVhlLUszakZyN0ptdGNlRWFOaDVFaHM3a2V1UWZrc3dPRWlqQzkwODJxdGVTNkRnQ1gxYkVDZThjZDhJVlQ4dHRKejdiV2RHYkZXMVpVWVF2bTRFeVB4cXloV0hkNWNMaGliRnlfbVVrSUFXU3N6QjZCQUEweXRUUFVmeEdyUFBLclVnOEladEdEWnZWM2dQN1E5eE55UHlMakw2Szktdzdwbzd2WnY2T0JoV0lLYzNnNUFtQWp6MHZVQXpLZG11WDJ6RklobXdMRUhwY29IbTVITS1iMFhIUzg?oc=5>

### Migdal Insurance & Financial Holdings Ltd. Buys New Holdings in The Charles Schwab Corporation $SCHW
- Summary: Migdal acquires new holdings in Schwab, potentially boosting shareholder value.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7gFBVV95cUxPZWh2TVVzTHZLRjV1eEd5UHVJRHBNLTVWOXdyOFVPTlJReDlPd1ZFU2hEWDk5eW54bkRnRVlITEkzeEdqUDF2NFFNWDNYZkxPUkdoSERVZWhwWHh2MXBzVFJKWU5NWHVuMzNYYmpfYjQwYkdjSTFkal9IclljdVlibTZJMGhjQW9SdjRPaWR2REE1a09kdThNS2k3bURfM0lCSXJoQmUzdnJ2MW01U1ZjU0g1SGhIdDh1bmxDQkx5RGlUM3JrVjM3STJuY21SZURfZWlnUjVSMlM3b285aHNyal82dl9LUGxsd3NIZlVn?oc=5>

### Why Is Charles Schwab (NYSE:SCHW) Putting Wealth Advice First?
- Summary: Schwab emphasizes wealth advice, signaling strategic focus on advisory services.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPdmJwVnZkVFkwUlRyeUx1NWdHV1Y3UHNZX0lFbHA5ejVxdFh1bmRfOVdJajE1b0R4NFZpTjE2Z1lBNEVOeTV0Uk1SUzNMQlBla3A5S21wMzFqLWpWdHNxdFNWWVNGd1Y1MVNpQldwMFFpRVdFb0lhaFZlaWk1Y0hnV3NYUXlqQU5sWmU2bmhadU5XTjFPeFVuWTJFTmRuOExjbG1tdEtn?oc=5>

## HEADWINDS

### The Charles Schwab Corporation $SCHW Stock Sold by Aberdeen Group plc
- Summary: Aberdeen Group plc sells Schwab shares, possibly indicating a shift in investor sentiment.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxNc1ZyQkk5TWc0SjVNRkFnRGdZcENwYnkyRmd0VlQ1X3l4bGlfTTNETUgwYjhPNksxRXRzMXdaSEtERk5jOHNpQzAtajUwMFpUcG1IbXJ6WWk1S2RnUzBkd2cxUWRXNmY2QTQyMGhaNlJNa3NfdW5Lc2piTERWTW1rRF9XNExYTk8wS3lKU2VLUmN0N01TeTRBbGo3aHU3QzFRdU50eGRsS2dRYUZVTTZjUEFPNjA4RDFadnptWmtCZ04wbEp4NnRYTQ?oc=5>

## CATALYSTS

No items in this run

## RISKS

### Charles Schwab Issues $3 Billion in Senior Notes
- Summary: Schwab issues $3B senior notes, increasing debt obligations.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNYzFCZC1DdDRwdjhidUxhRUhtaGhUQ1JybEwzUEJSMlBacEpNNS1JSk1ib0FMMC1fbjU1YjY1T19zeXlNdjNDbFh3QTBERURuRm8zV1JRNkhNS3dyMXhqUHRfLTJGY1RKSm82dmpzMkNZMS1yYjBKa3J0UTEta3hQQUpJYzBVSUZxNVNUU2h0WmVTS3lKWWlBSWlabHY4SlBrWDlxdEdoV285b0hfd0RhaXk1OXFDcWNPbFJpcjQ2N1J2MHlIcWxlaGw3OE4?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SCHW** | **15.89** | **3.50** | **N/A** | **16.90** | **158,516,543,488.00 USD** | **1.27** |
| IBKR | 29.98 | 5.57 | N/A | 13.50 | 130,275,696,640.00 USD | 21.09 |
| HOOD | 31.88 | 6.23 | N/A | 11.80 | 62,304,993,280.00 USD | -40.34 |
| LPLA | 16.65 | 3.79 | N/A | 17.80 | 21,920,739,328.00 USD | -21.81 |

Peers fetched as_of: 2026-11-17; SCHW reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

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

- https://news.google.com/rss/articles/CBMi9gFBVV95cUxNSks0N0dQOVJKeEltWlJYRHlxeU01amNFZVhxUWg5WDVpNDBiSVpHWXlLR0IzNl8xT1VlTXBYREkwdkljVjE1VlhsZzlhRU9zT2xLSDZ2My1pcG5JYnRFdHBSd1dCT2dRMEFENUVmYWRGQk1veVUyQmpLZzZQVzZ6UzBVbVRxZGEwUURWWEdvQnBqcmFJbzhJdHNSYUJNckRZalkwb1QwdGh2R3J4Ry1EbE1CcUxrdEs2UWlMczRaUHBMQWt4a3pjaVltWVplWF9PbWRVMEV0cTNZVGlFVWpPdFRLNjNrZjNhYjZ5RkhSTHRXbDZHeUE?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxQT2M3QVo2bUhsc3RKeG1hXzlXdHN1UXFlclpNSVpPRWpvMlRYZDV4UnNfYmN6cFEzUDdfOW13aElFQzFfamk5eXRJRm5jejdVcllyX0RmVEJaYmFmREo4OW8zaTkxbTB1R3RzV2ZJWFhDekFwN045WFduODA5RVYyblNWcnFUU1BpV19zNnFwdHd0ekMzSlhOV0hxM1hXTFlZeVFiWDhNdTVhYjVZTXI4T2l3UV8zdHpmdGFnN2VVMHp1QUpZdUw0Vnh1c0JmLWNQd0duMU52Qnl0V2RvUHfSAeMBQVVfeXFMTlU0NVhlLUszakZyN0ptdGNlRWFOaDVFaHM3a2V1UWZrc3dPRWlqQzkwODJxdGVTNkRnQ1gxYkVDZThjZDhJVlQ4dHRKejdiV2RHYkZXMVpVWVF2bTRFeVB4cXloV0hkNWNMaGliRnlfbVVrSUFXU3N6QjZCQUEweXRUUFVmeEdyUFBLclVnOEladEdEWnZWM2dQN1E5eE55UHlMakw2Szktdzdwbzd2WnY2T0JoV0lLYzNnNUFtQWp6MHZVQXpLZG11WDJ6RklobXdMRUhwY29IbTVITS1iMFhIUzg?oc=5
- https://news.google.com/rss/articles/CBMi7gFBVV95cUxPZWh2TVVzTHZLRjV1eEd5UHVJRHBNLTVWOXdyOFVPTlJReDlPd1ZFU2hEWDk5eW54bkRnRVlITEkzeEdqUDF2NFFNWDNYZkxPUkdoSERVZWhwWHh2MXBzVFJKWU5NWHVuMzNYYmpfYjQwYkdjSTFkal9IclljdVlibTZJMGhjQW9SdjRPaWR2REE1a09kdThNS2k3bURfM0lCSXJoQmUzdnJ2MW01U1ZjU0g1SGhIdDh1bmxDQkx5RGlUM3JrVjM3STJuY21SZURfZWlnUjVSMlM3b285aHNyal82dl9LUGxsd3NIZlVn?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPdmJwVnZkVFkwUlRyeUx1NWdHV1Y3UHNZX0lFbHA5ejVxdFh1bmRfOVdJajE1b0R4NFZpTjE2Z1lBNEVOeTV0Uk1SUzNMQlBla3A5S21wMzFqLWpWdHNxdFNWWVNGd1Y1MVNpQldwMFFpRVdFb0lhaFZlaWk1Y0hnV3NYUXlqQU5sWmU2bmhadU5XTjFPeFVuWTJFTmRuOExjbG1tdEtn?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxNc1ZyQkk5TWc0SjVNRkFnRGdZcENwYnkyRmd0VlQ1X3l4bGlfTTNETUgwYjhPNksxRXRzMXdaSEtERk5jOHNpQzAtajUwMFpUcG1IbXJ6WWk1S2RnUzBkd2cxUWRXNmY2QTQyMGhaNlJNa3NfdW5Lc2piTERWTW1rRF9XNExYTk8wS3lKU2VLUmN0N01TeTRBbGo3aHU3QzFRdU50eGRsS2dRYUZVTTZjUEFPNjA4RDFadnptWmtCZ04wbEp4NnRYTQ?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNYzFCZC1DdDRwdjhidUxhRUhtaGhUQ1JybEwzUEJSMlBacEpNNS1JSk1ib0FMMC1fbjU1YjY1T19zeXlNdjNDbFh3QTBERURuRm8zV1JRNkhNS3dyMXhqUHRfLTJGY1RKSm82dmpzMkNZMS1yYjBKa3J0UTEta3hQQUpJYzBVSUZxNVNUU2h0WmVTS3lKWWlBSWlabHY4SlBrWDlxdEdoV285b0hfd0RhaXk1OXFDcWNPbFJpcjQ2N1J2MHlIcWxlaGw3OE4?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
