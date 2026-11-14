# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T05:05:55.222777+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 2, 'ai': 12, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/T** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 2}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 11 named publishers; 1 exact duplicates; 21 HTTPS source links; largest publisher share 19.05%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 22.1800 |
| Return 1D (%) | 0.0000 |
| Return 1W (%) | 2.5428 |
| Return 1M (%) | -2.9322 |
| Return YTD (%) | -6.4482 |
| Return 1Y (%) | -9.7543 |
| Annualized volatility (%) | 28.6475 |
| Beta vs SPY | -0.3464 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.2150 |
| Downside deviation (rf=0, %) | 21.9829 |
| Sortino (rf=0) | -0.2802 |
| Historical VaR 95% (1D, %) | 2.8546 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1648 |
| Tracking error vs SPY (%) | 33.6943 |
| P/E (trailing) | 11.86 |
| P/B | 1.40 |
| EV/EBITDA | 7.34 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.54 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 22.59 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 8.01 |
| MA50 | 23.4245 |
| Close vs MA50 (%) | -5.3130 |
| MA200 | 24.3934 |
| Close vs MA200 (%) | -9.0736 |
| RSI (14, Wilder) | 48.3811 |
| MACD (12,26) | -0.3374 |
| MACD signal (9) | -0.5327 |
| MACD histogram | 0.1953 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 22.1800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.0000 -> Unchanged adjusted price over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.5428 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -2.9322 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -6.4482 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -9.7543 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.6475 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.9829 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.2802 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8546 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1648 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.6943 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3464 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.2150 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.5446 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 22.5930 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.0057 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.8610 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.3811 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1953 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.3130 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -9.0736 -> Clearly below the moving-average trend level.

## TAILWINDS

### AT&T stock gains satellite handoff milestone as beta nears
- Summary: AT&T stock gains satellite handoff milestone as beta nears
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPZjM0LW8wSEpEWXNNZVMwZHdUZWV3Z3NubEVjQUlydFl0TnFwQU9sQkRVTnF3MnVLZDZXdWhlcThhb19WSHhxaDEtUVAwMTJOR1R6VURoTzJhYjMzT3lTbjhyUy1FQW9nTWszcGRFYzEzUzdKYzJXVGMxUW5YdUV2Q0R1dzVGNnh6Um95U3MyQnpIbzRBbzFmSng3b19QQWdtb1ptYy04cW92TVQzUDhtdXZXWENQcGFjRU10OVlB?oc=5>

### AT&T Inc. (T) Is a Trending Stock: Facts to Know Before Betting on It
- Summary: Provides general information about AT&T’s stock performance and key facts for investors.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOVV9ObmR5eFVxT2JwX1cxbTJWNjJRb2VWUFQ3ZDJRQlhrRlplUTdhNFQ5OVhGbWFkM3NydXVVdUJxdEFFckJHT3V1Vnp3NzhUM3djVkpzMldHNlFlSTEta3ZSdmx0R2poeVl6SkJoVmZCUk8zNVNEZzNkbTh1SVN0dndzXzAxTnZRbkdnbWdoVlE?oc=5>

### AT&T (T) Stock May Be 34% Below Fair Value After Care Reshoring Plan
- Summary: Analysts suggest AT&T may be undervalued due to care reshoring, indicating potential upside.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMic0FVX3lxTE5fSVJiZi0zX1JoRHd2YTJFNENVSVBFQ1pZOTIyT1h1ZFA3TjdNWmt3LTM3am1wSjFNNjBhZTZRamlZckdaQ1hRSUNwNXp3ZnNERkZhc3cyVHJrcDBaY1otN05pRm54VEJYQ2dCMndCWmhXTU0?oc=5>

### Could AT&T Be The Value Stock For Your Portfolio?
- Summary: Explores AT&T as a potential value investment.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNekpYMnFKNG1tQnpzaTk0bmFGRWM2ZldhaGl1OHFxOFBKWVQ4eWFRQUxKQURDTjVweHIzcXZVbVVrR0M5TkxQSnJFY0xOMXhkRmpsamJnaHF1MENkeW1OMjQxUk84enZES0s3dWNYeS1BQmhtcElMVjhiZ0VBS2FjbjdSWklxT1FTQ3pEM0l1MDRBbXhoeTNZZm8xMHRrdHc4U3JvdHpLbi0?oc=5>

### Most Active S&P 500 Stocks: KDP, Ford, AT&T Lead Today's Session
- Summary: Highlights AT&T’s high trading volume in today’s market session.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNM0FxcFNTaEhkcVZlMkotd051bjh1Tl9hTkVyLXdZeWdpNEt6eDJ1S1drRkFYUnk1RnNzME5kVXZxQ1ZuWHJiOFVQUU9OcGF3dFFER0JDZEswX1M1LVg5Z3o2WFFQMmxWUVh6NVh5UjZrTng5TTl4ZERGRGZuUEFhVkVEVU5OSWhNVTFManQta09UaklqWWFMLXQxb2dMVnAtUVhCMVlxLXdkS3c?oc=5>

### AT&T (T) Stock Could Be 35% Undervalued On Customer Care Reshoring
- Summary: Valuation analysis points to significant undervaluation linked to care reshoring strategy.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQQzhTeVNGUjkyM281M1NQTHlScngzUDV2cWNyeWVzT3BQdXRTQ09VX2NYa1VhQW9GVDQ3T09kWGJiZVl0ZnhrMkNFa3E4M2h4SU5NWW5jMmJ5blptQkFxU05NTUtCenZEaXJCRlMtWGczZTAzRklsOTBoVUNHSXB6MUx2RGFTN1psVS1iVG41czg3NGg0TGpxU1NVb3NfVmJPSXp4N2FaMFhKeW5OYk9HWHQySzZ6UDDSAbwBQVVfeXFMTnA5RjlVYmhQQnpVdmlQRzlHZmktblFqa2tyTEM3TkYzLUdYdVVfMlNyNTZUZlNzZjd3T0NkcUZ6ZUJicUlYZXVUYW5kWWdKbkxsTEptbktWRm83bExWaG5zSWQ5V1ZYYmtQcDlHVElveHJoQTVyUjNqb3p2SkwwSnE2R3A4aHVOcXlVR3ZqVTRqbUdDYjVHWmxvNXV6ak1JQkNHV1VEZmFCOXlfZWZLMVJVVFFTTUlvb201Wmw?oc=5>

### Better High-Yield Dividend Stock: AT&T vs. General Mills
- Summary: AT&T offers higher dividend yield than General Mills, attracting income-focused investors.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxOYW14MlFpeDgzenREMk9icVBfWFZiaVNaQXpzMnBsVUxUSnVQZFFVdzk3Z0ttc2xfUXlTdXB2eU1UQl9udXMtbzJpdWZUWTUzNUxjQ2Y3Sl8zdDZPcEZ2VXlqUS1IRDlDdnJkVDduc1pmQ3NxU0pDUVpyQlpjSHFyMnF1RjVEMUU?oc=5>

## HEADWINDS

### AT&T Stock Falls 11.8% in a Year: Should You Buy the Dip?
- Summary: AT&T shares dropped 11.8% over the year, raising concerns about valuation.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNeVJqakhwY213N3laR2tsVk5Zam5UbFBhUWVqNEVILTRjdVlEUFJrQ21qV2RwUHNBVmZwQmNZT25JbHo2eFoxUnBGd01Ob1JpWEQzZzBsejJzcjE2X2F3MmJoM2Rpdm5mZ0l1azhKQnZpVnJaN09SdHJVWHUwbVRIaFMwRjhFNFlLY3hj?oc=5>

### Why AT&T Stock Slumped in October
- Summary: AT&T shares fell sharply in October due to market concerns and earnings expectations.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxNcm8tYWtGY1RKVEpGcGc3THl3dXNvOTRQN0xoTXNBdnJwUmswMVg0d180VjlELTRFeFd2ejhvR1M5cE5QeUF3WDAwLTJpbFZQaFRuRG1NdkVON0drcGpFbjNvVU9uTngxU05FcmdWU2cwbDE0dS01MXRZSUdBZk9rSzJlRXdIRVE?oc=5>

## CATALYSTS

### AT&T Inc. $T Stock Bought by Vestor Capital LLC
- Summary: AT&T Inc. $T Stock Bought by Vestor Capital LLC
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQVGdGNGU4RU5IRWF6VDMtS0ZQeklodGF1VHdUeHV4eC1XVkdZY3NoRmZROFBZVlZrelkydFNYZHNYRlJzRUprT2VGaVFVTXFPWFN0OURNZUd4cnlaSmx6MXI4Tk55REtaeXRrNVF5aWVhbDZKX3lHeDRraVdPOVpvakNCRGtJblROUmw0ZmdidXF6MkFpbV9qSzJXQk1ZaW1lNktPNmJTNmE?oc=5>

### How Investors Are Reacting To AT&T (T) Satellite Phone Handoff
- Summary: Investors react to AT&T's satellite phone handoff, indicating market sentiment on the transition.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPMndVTWxGVVhEX19hREV1aDRrb2RHS3ZxMzFIa2ZNeXBOcjkxbUVOZm9qRUlKaDZHeXMtSEdFZ3B2QTlGXzVtdXRhaGNTSndNOUxDaTZNdGxXWDI3cXRNVmhCcEl2WS1WbTZOckgzYkhETzNCSmxUTnhhYldrWTJHRkh0LVdtdXVRZzJrcWJtaTRlVll1cEU0RWtNNEpGTGgxYjVtUEZDeFFHZ1F4T1FwaEF1YXhDUdIBuwFBVV95cUxNbGVjdUJJcXVDU01lN1NpOUVST1RjZVI3OHRrWDh0UDZvWFYwa3hoSUVvMlBlWWdSUEcyRkc3dnNFU1I0S2h3eGR0R0hadXBVTnJONm5SeEdqTFZGM0JoOVVlSV82eGYwU2xzMzBIaHExNmVhZk9hM3Q4RkplM2cxbExNS3YxbXlJVFREaVhLTVU4N3ViTTloQmxYX1hUN3BBMC1ISURNNXA1d3FYWWczSUJhUzBzM1JIODRZ?oc=5>

### AT&T stock advances as satellite handoff clears beta-testing hurdle
- Summary: AT&T stock rises after satellite handoff passes beta test.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPRGxRZDFLSG1GNmhmWFFKQThEWC1aSmJNYXpZZ01mZnBzVF9idjhqRC1oX3BmYnI4ZEVhcXZibG4zams2QUtmZWFrcFZqc05sZWFoSVRPTUM4MDQ3Skwzci1RYk5WT3NHRzZWMF8yWDdCUEpQcVdDbk5qb2tza2pVczNfbmVuSWJwd0d0dWE2UHVDeW1hdzlYLWNhQlNCcU1Sd1NxVVM0bExDcjliUmgwX2VWdERIbkRNLWQ0VUdqUUl2VmFVNFFCazBn?oc=5>

### AT&T stock: Satellite handoff moves toward beta testing
- Summary: AT&T stock noted as satellite handoff moves toward beta testing.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxObVpTcjN4dTg2QlpzVTdUazBIdUpFNk9wX1pHZENGZnlCa3pfVnBtMjNqbjVKRnlVbEFraW05NC02LTJqcFRhUVY3ZFEwSDdrS3ZkaWxhREFFaHNPRnVCamUzMElyX0dUS2k1U3RTb2dyTjM5aS1RUENITmplNzM3T2JEWE15QkhSOERVem94ZmdpQm5nUHNSX0V2RkUtUXRwNW5PQU1CcngxY3htS2FGUmxoeDM4TFNs?oc=5>

### Verizon, AT&T and T-Mobile shut out Elon Musk’s phone service. Now the FCC is reviewing SpaceX’s plan to build its own
- Summary: AT&T participates in blocking Elon Musk’s service, prompting FCC review of SpaceX’s infrastructure plans.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQVzJFZFlzQmplRmxxcEtrRmlSUjk4anJsbUlBVlhjYURlZUQ2WmVmZm12dmgyd0lEdHVSakItcHZwM2pYQ3AtTTkxSER0cWRndEg5b3VBOUM2WXRyYWpVR0UwMGxBeWZwenRidWVrby15cFVfVGg2RVBQcjJrSHRWVk9jM2J5V0xzRDdGSw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **11.86** | **1.40** | **7.34** | **5.30** | **149,414,985,728.00 USD** | **-9.75** |
| VZ | 11.89 | 1.81 | 7.38 | 1.50 | 192,143,572,992.00 USD | 20.28 |
| TMUS | 16.50 | 3.21 | 8.30 | 7.40 | 180,023,377,920.00 USD | -19.12 |
| BCE | 11.52 | 1.34 | 7.36 | 2.20 | 19,984,029,696.00 USD | -2.30 |

Peers fetched as_of: 2026-11-13; T reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

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
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 32,322,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 891,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/732717/000073271726000372/t-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMivgFBVV95cUxPZjM0LW8wSEpEWXNNZVMwZHdUZWV3Z3NubEVjQUlydFl0TnFwQU9sQkRVTnF3MnVLZDZXdWhlcThhb19WSHhxaDEtUVAwMTJOR1R6VURoTzJhYjMzT3lTbjhyUy1FQW9nTWszcGRFYzEzUzdKYzJXVGMxUW5YdUV2Q0R1dzVGNnh6Um95U3MyQnpIbzRBbzFmSng3b19QQWdtb1ptYy04cW92TVQzUDhtdXZXWENQcGFjRU10OVlB?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOVV9ObmR5eFVxT2JwX1cxbTJWNjJRb2VWUFQ3ZDJRQlhrRlplUTdhNFQ5OVhGbWFkM3NydXVVdUJxdEFFckJHT3V1Vnp3NzhUM3djVkpzMldHNlFlSTEta3ZSdmx0R2poeVl6SkJoVmZCUk8zNVNEZzNkbTh1SVN0dndzXzAxTnZRbkdnbWdoVlE?oc=5
- https://news.google.com/rss/articles/CBMic0FVX3lxTE5fSVJiZi0zX1JoRHd2YTJFNENVSVBFQ1pZOTIyT1h1ZFA3TjdNWmt3LTM3am1wSjFNNjBhZTZRamlZckdaQ1hRSUNwNXp3ZnNERkZhc3cyVHJrcDBaY1otN05pRm54VEJYQ2dCMndCWmhXTU0?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNekpYMnFKNG1tQnpzaTk0bmFGRWM2ZldhaGl1OHFxOFBKWVQ4eWFRQUxKQURDTjVweHIzcXZVbVVrR0M5TkxQSnJFY0xOMXhkRmpsamJnaHF1MENkeW1OMjQxUk84enZES0s3dWNYeS1BQmhtcElMVjhiZ0VBS2FjbjdSWklxT1FTQ3pEM0l1MDRBbXhoeTNZZm8xMHRrdHc4U3JvdHpLbi0?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNM0FxcFNTaEhkcVZlMkotd051bjh1Tl9hTkVyLXdZeWdpNEt6eDJ1S1drRkFYUnk1RnNzME5kVXZxQ1ZuWHJiOFVQUU9OcGF3dFFER0JDZEswX1M1LVg5Z3o2WFFQMmxWUVh6NVh5UjZrTng5TTl4ZERGRGZuUEFhVkVEVU5OSWhNVTFManQta09UaklqWWFMLXQxb2dMVnAtUVhCMVlxLXdkS3c?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxQQzhTeVNGUjkyM281M1NQTHlScngzUDV2cWNyeWVzT3BQdXRTQ09VX2NYa1VhQW9GVDQ3T09kWGJiZVl0ZnhrMkNFa3E4M2h4SU5NWW5jMmJ5blptQkFxU05NTUtCenZEaXJCRlMtWGczZTAzRklsOTBoVUNHSXB6MUx2RGFTN1psVS1iVG41czg3NGg0TGpxU1NVb3NfVmJPSXp4N2FaMFhKeW5OYk9HWHQySzZ6UDDSAbwBQVVfeXFMTnA5RjlVYmhQQnpVdmlQRzlHZmktblFqa2tyTEM3TkYzLUdYdVVfMlNyNTZUZlNzZjd3T0NkcUZ6ZUJicUlYZXVUYW5kWWdKbkxsTEptbktWRm83bExWaG5zSWQ5V1ZYYmtQcDlHVElveHJoQTVyUjNqb3p2SkwwSnE2R3A4aHVOcXlVR3ZqVTRqbUdDYjVHWmxvNXV6ak1JQkNHV1VEZmFCOXlfZWZLMVJVVFFTTUlvb201Wmw?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxOYW14MlFpeDgzenREMk9icVBfWFZiaVNaQXpzMnBsVUxUSnVQZFFVdzk3Z0ttc2xfUXlTdXB2eU1UQl9udXMtbzJpdWZUWTUzNUxjQ2Y3Sl8zdDZPcEZ2VXlqUS1IRDlDdnJkVDduc1pmQ3NxU0pDUVpyQlpjSHFyMnF1RjVEMUU?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNeVJqakhwY213N3laR2tsVk5Zam5UbFBhUWVqNEVILTRjdVlEUFJrQ21qV2RwUHNBVmZwQmNZT25JbHo2eFoxUnBGd01Ob1JpWEQzZzBsejJzcjE2X2F3MmJoM2Rpdm5mZ0l1azhKQnZpVnJaN09SdHJVWHUwbVRIaFMwRjhFNFlLY3hj?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxNcm8tYWtGY1RKVEpGcGc3THl3dXNvOTRQN0xoTXNBdnJwUmswMVg0d180VjlELTRFeFd2ejhvR1M5cE5QeUF3WDAwLTJpbFZQaFRuRG1NdkVON0drcGpFbjNvVU9uTngxU05FcmdWU2cwbDE0dS01MXRZSUdBZk9rSzJlRXdIRVE?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQVGdGNGU4RU5IRWF6VDMtS0ZQeklodGF1VHdUeHV4eC1XVkdZY3NoRmZROFBZVlZrelkydFNYZHNYRlJzRUprT2VGaVFVTXFPWFN0OURNZUd4cnlaSmx6MXI4Tk55REtaeXRrNVF5aWVhbDZKX3lHeDRraVdPOVpvakNCRGtJblROUmw0ZmdidXF6MkFpbV9qSzJXQk1ZaW1lNktPNmJTNmE?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPMndVTWxGVVhEX19hREV1aDRrb2RHS3ZxMzFIa2ZNeXBOcjkxbUVOZm9qRUlKaDZHeXMtSEdFZ3B2QTlGXzVtdXRhaGNTSndNOUxDaTZNdGxXWDI3cXRNVmhCcEl2WS1WbTZOckgzYkhETzNCSmxUTnhhYldrWTJHRkh0LVdtdXVRZzJrcWJtaTRlVll1cEU0RWtNNEpGTGgxYjVtUEZDeFFHZ1F4T1FwaEF1YXhDUdIBuwFBVV95cUxNbGVjdUJJcXVDU01lN1NpOUVST1RjZVI3OHRrWDh0UDZvWFYwa3hoSUVvMlBlWWdSUEcyRkc3dnNFU1I0S2h3eGR0R0hadXBVTnJONm5SeEdqTFZGM0JoOVVlSV82eGYwU2xzMzBIaHExNmVhZk9hM3Q4RkplM2cxbExNS3YxbXlJVFREaVhLTVU4N3ViTTloQmxYX1hUN3BBMC1ISURNNXA1d3FYWWczSUJhUzBzM1JIODRZ?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPRGxRZDFLSG1GNmhmWFFKQThEWC1aSmJNYXpZZ01mZnBzVF9idjhqRC1oX3BmYnI4ZEVhcXZibG4zams2QUtmZWFrcFZqc05sZWFoSVRPTUM4MDQ3Skwzci1RYk5WT3NHRzZWMF8yWDdCUEpQcVdDbk5qb2tza2pVczNfbmVuSWJwd0d0dWE2UHVDeW1hdzlYLWNhQlNCcU1Sd1NxVVM0bExDcjliUmgwX2VWdERIbkRNLWQ0VUdqUUl2VmFVNFFCazBn?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxObVpTcjN4dTg2QlpzVTdUazBIdUpFNk9wX1pHZENGZnlCa3pfVnBtMjNqbjVKRnlVbEFraW05NC02LTJqcFRhUVY3ZFEwSDdrS3ZkaWxhREFFaHNPRnVCamUzMElyX0dUS2k1U3RTb2dyTjM5aS1RUENITmplNzM3T2JEWE15QkhSOERVem94ZmdpQm5nUHNSX0V2RkUtUXRwNW5PQU1CcngxY3htS2FGUmxoeDM4TFNs?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQVzJFZFlzQmplRmxxcEtrRmlSUjk4anJsbUlBVlhjYURlZUQ2WmVmZm12dmgyd0lEdHVSakItcHZwM2pYQ3AtTTkxSER0cWRndEg5b3VBOUM2WXRyYWpVR0UwMGxBeWZwenRidWVrby15cFVfVGg2RVBQcjJrSHRWVk9jM2J5V0xzRDdGSw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
