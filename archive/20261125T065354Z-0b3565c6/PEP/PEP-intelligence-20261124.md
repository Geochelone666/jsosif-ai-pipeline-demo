# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T06:55:27.390587+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 5, 'ai': 13, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261123T053847Z-45053549/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 12 named publishers; 0 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 142.6800 |
| Return 1D (%) | 1.7616 |
| Return 1W (%) | 0.4647 |
| Return 1M (%) | 5.0895 |
| Return YTD (%) | 2.4410 |
| Return 1Y (%) | 2.0353 |
| Annualized volatility (%) | 22.0230 |
| Beta vs SPY | -0.1559 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | 0.2012 |
| Downside deviation (rf=0, %) | 14.7294 |
| Sortino (rf=0) | 0.3008 |
| Historical VaR 95% (1D, %) | 2.2237 |
| Historical ES 95% (1D, %) | 2.7033 |
| Correlation vs SPY | -0.1059 |
| Tracking error vs SPY (%) | 27.8996 |
| P/E (trailing) | 17.95 |
| P/B | 8.73 |
| EV/EBITDA | 12.28 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 16.60 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.05 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.65 |
| MA50 | 134.3412 |
| Close vs MA50 (%) | 6.2072 |
| MA200 | 143.1129 |
| Close vs MA200 (%) | -0.3025 |
| RSI (14, Wilder) | 57.1706 |
| MACD (12,26) | 1.9534 |
| MACD signal (9) | 2.4337 |
| MACD histogram | -0.4804 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 142.6800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.7616 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.4647 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.0895 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 2.4410 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 2.0353 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.0230 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.7294 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3008 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.2237 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7033 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1059 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 27.8996 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1559 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2012 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.6026 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.0460 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.6515 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.9472 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.1706 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.4804 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.2072 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.3025 -> Slightly below the moving-average trend level.

## TAILWINDS

### PepsiCo (PEP) Stock May Be 50% Undervalued Following Partnership Renewal
- Summary: Partnership renewal may signal undervaluation, boosting investor confidence.
- Date: 2026-11-21 | Impact: high | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNQ0V2bUwxb1Y4Y2NrS2ZkNm1LOWx5S19rLUJHSVhyZy1lLWJEZVVsMng0R05OWUV2NlN3S1hVVXVzUndlZnJMV3ppQUNuT3dsMFF3cjE0RlpZTXVXSE90dVJzQ05CWlJtRm1KWFdJMm1HdkNrV2ZQdkhQQ2NzOFNLRkVOWjlUZ3NFdmNSMzJNWHFURG1vOV9SZDFPV3N6SHFXOEN4eVpUU3NleUNSRlZOZWZweHB3S09QcFA1bnBPaTFIcHVCbDhOZVotS0dkVkhqUUR4UNIB2gFBVV95cUxPaU9CUFBiUnptNnFLNVE5MlFhdEEyYlI2MXEtNEhRLVlMS1pDOEdoc0NQbkRvQUc5eDhfV3ZOUW96M3FtbDBweElJdTZrZEl4ZWQ3YjNtUzFnU3BUbG9vdGZtQkVjbXVvbWhHd3lwa3AycnhacGg2MW5pSjZtY0sxZ1pMSFluUEJSRUZEOTFZbzVWTnRUb0g2cEhPWGFhTlZQaS1fQ0lkMU00MXFORjVsUTZySVMydTV6ZUZydER4SC1Rck5jM2Q4dkZWWjRydFhfMDQ1dElKMk8yZw?oc=5>

### PEPSICO INC (NASDAQ:PEP): A Quality Investing Case With High ROIC but Mature Growth
- Summary: High ROIC but mature growth suggests stable returns, supporting a defensive buy.
- Date: 2026-11-21 | Impact: medium | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxNOUplZFJ4dUlHX1FGSHE0dFZ5RlVSVXdBWkduY1BoaTRXYWpsT3NIbllraG1aVTlCRTRuUG05RmNseDZJbDhZSlc0enRBbk5qME5yWUdQbkh6dDNXaVRsQVNuVkJJVThIZVNyYmxsbjRsNjkxNjZjdmRNREZReDQtTWVFSmhUa2tjMERKQkpJMmdJMFdiMzJuZC1sekRDamxQSHN6bXhyVTZLRDNFWmZCaExIcjUycXZRUzdJZldlT0gzSmJlSTU0OE5B?oc=5>

### Coca-Cola at $95 or PepsiCo at $140: Which Dividend King Could Turn $1,000 Into More Money by 2036?
- Summary: Dividend comparison highlights PepsiCo’s potential for long-term yield growth.
- Date: 2026-11-24 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAJBVV95cUxPTDlHUUtsS1NhQ1RaeWV0YjQ1eVRLZnNoRnRoR1RXZ3RoSkNqYzNUR2hmZTZGc0stQjZUeTFVOG1YaElSelVPRVo2OU1wY3NqaUhTTzJXNVRka2VMc1ByZzVVaXZxZnVWRktKdDdPNlQ0dnJRUTZaMVZ3LXJoVEd4cUJKOUx3LVZ2bHFTSi1XeE9NajQ4Q2ZkdTJ5X1lCVjFvZW1PRzJOX3QtcF9MeXVpbVFGVS1PM1BWY3dyMzNqV1AyTnFZQlhJNlRVdFRfUGhZYXkxTkJjN1dOclVPNzU2a2F5aWFoc1AxbXlPckJaaHpPYmdFSzY3dFJRaEtaZ3NUSUQtM0toTE5MbXpu?oc=5>

### PepsiCo: A Defensive 'Buy' In A Market Sell-Off (NASDAQ:PEP)
- Summary: Defensive buy recommendation amid market sell-off signals resilience.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPUmtpWWdERFlMcFNZOTJ3eFhBNUFpSEZTVWhPczBpS3p5RUJyZGFZYV9LYUxDb1RtajhzOFRqZDJVQmRYbzA0M3lCVjAwY182NDZEaTlNMndiUEg1dFEzUEpRdXVESVZUWEF6blEtTHdRdlE5RnJIemtWRXQyR2lLNmN6SlVUS2dyRktJb2JB?oc=5>

## HEADWINDS

### PEP Stock Slides As Bernstein Downgrades PepsiCo, Warns Of Earnings Shortfall
- Summary: PEP Stock Slides As Bernstein Downgrades PepsiCo, Warns Of Earnings Shortfall
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxNalNIYng0Ulo0eGVKTF90dldxamJLT1hBVS1XUUs5anEwWk00WV9NMEVaTXlDYnhUM0NkQVRnZ2lmNnJIZURiX1RuM3RacFp1ZWFRM0tld3JvS0xiWmVKMmp3TTVEY1cwak00NWM3RHpWdnRiMm5yQ004bksyQzdGVGNoTlNqLVg1WlViTnBvRTNjVkR1MmxiaGdrQ1BnajN5UlJiZTZVT200X0JuUElEd1V0VnB3QWtNNTFwQkpQaUxmOXJKVVZpNzRfUlVYaDRXOFpRZjB0ZjlhQWx1RkxHX3duaXpMdjB3bEZv?oc=5>

### PepsiCo downgraded by Bernstein with a new price target
- Summary: PepsiCo downgraded by Bernstein with a new price target
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxONnNDY1JCVHh6M0lLSi1wWTQ4WW9Bb0xoeFhwQ0c1UEhvSlRXOW5uTFZQakhyd3NCdUJZRjdUVFQzWk44WXhvRUxaM0hMZ3lmOUNEd2hjZFhoRVBqeTNMSkNaeUdKMVZKQTgtRDd2c29uTlBkV2Y0MG1Db0FrRVpkTG5HU0tfT1ZrMGR3TlFRdXUtOHFxNmhSOEhrMFZObTA?oc=5>

### Bernstein Sees Trouble Ahead for PepsiCo (PEP). Here’s Where.
- Summary: Bernstein research warns of future challenges for PepsiCo.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxOT3ctYUZMSGdjY2o2WFJvcElIdkZWcHlUd2NweGxJRFpHLVhvVzJQaENEMVpXTGlNamhPU28wd1JEMWhSRzRIU0dSdHNGa3JwcFpBTUxlSUw0alVSVEtEc00xYXBTVEl5NkZfOHM2R3ZIeWZxRTVHUi02THNMRk91eTFZR2p6YzRIY2lLWTktUFlMdHNwXzRxZjlac1oyODVFX2NJ?oc=5>

### Could PepsiCo Be The Value Stock For Your Portfolio?
- Summary: Opinion piece on PepsiCo as a value investment.
- Date: 2026-11-17 | Impact: low | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNWlJCOW9wd2tPRXh5dHpPLV95R0pCQkdFR1o1cFNYSnFzMlVXWG1kRGxHeGJ0NV9QR2gzM0dqTmJJaUdCQUprTWRNVmxMUmFfNzZvcW1MUVRGU1pZemVVWmxhd0syYTNaU2hjbWVHMDdmaW1mUnhPZWhJQXl6S3dmZ0lDOFlsQXpCMG1NOEpFSmVZaHBfeUlMRzZTS2JIWWd3R0E?oc=5>

### PepsiCo (PEP) Stock May Be 49% Undervalued Following Margin Concerns
- Summary: Margin concerns suggest potential downside, questioning valuation.
- Date: 2026-11-23 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQVUdmVlJzZ1hCcW1ubUtSVU5sUnpPTkNmUklJOHhRRG1DVV92MkZKVWd6YkVaU0lLTml2dmJ0b1pyZkpLSFVJYnpXcXE5T1hJSkVoQWlhQWxzWWlCS3AtOTNLdnkyaGNYVG5MMVBiSVZXWmYweXJubkFQcEhadDZOUGxmdGRXdm1vWHJOQU9JcXdydGs?oc=5>

### PepsiCo: Still Not Refreshing, Remains A Sell (NASDAQ:PEP)
- Summary: Negative outlook, recommending a sell due to lack of growth.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPRGlRbFpjUVZkM1B0Rk4wZVVLRlhuaVN6ZHZkY2tCT3ZiU3p1XzVBRG1KbWFiVEFHR19GSkpyOGlRYXF2blRfUEZ2QkZ2TXBPb1ZMZnFzOFFqUjVyaFRydks0QzRWbjI1MEhWbUpJakd1UFJ1Vi1GNnRBMjRmNG5RTFZJV0lRcnQ5LVlwUA?oc=5>

## CATALYSTS

### PepsiCo (PEP) Lands Hyatt Deal On A Fair Value Debate
- Summary: PepsiCo (PEP) Lands Hyatt Deal On A Fair Value Debate
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNTVFiVXNnMmNNTlZ4UzA0QlFEZV94WVluckhCT1hsVjJnTXc5NkhiRnVyR0tTQ3phaWNDci0xZWpjQmpoWjA0X2JTU3dzalcyc1djU3gxY0hDV0ZKM0lBZDhINS1LM3VvMHRLUHpTbVhqTVdQb2I1ZU1nbS1BazlCS1pUSWp0TjUtX1NaZDRYVmZzR0VNUDZUeA?oc=5>

### PepsiCo Stock: A Dividend King With Little Room For Error (NASDAQ:PEP)
- Summary: PepsiCo Stock: A Dividend King With Little Room For Error (NASDAQ:PEP)
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNd0k0OXppUmNGUDRQbW5KakdGX1lDZkVWdVgzTEZyWVRkTjcwWHI1V3FZb18wNTNhMlZZRUcyajFudllRT0RIU0JaT2JBU1VROGRnSGFEUnRYNjdhbnF2aWYtU0pYaDVJemJfRXpFRkRsVVRwcFNiekdZOGdjbjlXZHNuYjA0ek44S05mYWF3OERtNHVCZmNPT3I3dmJyMld5U3k4azYydUpXd2FrdV96VThaOEhYbmM?oc=5>

### PepsiCo (PEP) Shelf Filing Leaves Investors Asking If The Stock Is Already Fairly Valued
- Summary: PepsiCo (PEP) Shelf Filing Leaves Investors Asking If The Stock Is Already Fairly Valued
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxPY1RDT3BNamFzeFl5MElfMVFfVnd3UlNzQlM0MGlfWG1SRFhuRDQwQm5NdXpHa2FPNHFHWGtkNDZuMGs1cVlwYW9NTEFEWm9hT0tPOUc2RUttUEtteFhxdzREaEZrZEpIMGJ3R3k0OTJVSmdsMThxR2J3NzAzUUpTUUVYbFpmOEtfelFSY0hFR1BvbnY0MXZ5M0lfS0JfRndmaEhMMGtZVy1SenJnb3EyMTZHVEktT2xrUnUxWE9BUkF3eWZGUG85ZGNYdXpkU3RNMGI0NVkxdDV1Z9IB2gFBVV95cUxPY1RDT3BNamFzeFl5MElfMVFfVnd3UlNzQlM0MGlfWG1SRFhuRDQwQm5NdXpHa2FPNHFHWGtkNDZuMGs1cVlwYW9NTEFEWm9hT0tPOUc2RUttUEtteFhxdzREaEZrZEpIMGJ3R3k0OTJVSmdsMThxR2J3NzAzUUpTUUVYbFpmOEtfelFSY0hFR1BvbnY0MXZ5M0lfS0JfRndmaEhMMGtZVy1SenJnb3EyMTZHVEktT2xrUnUxWE9BUkF3eWZGUG85ZGNYdXpkU3RNMGI0NVkxdDV1Zw?oc=5>

### PepsiCo Analysis - Is PEP About to Break Out? - PepsiCo (NASDAQ:PEP)
- Summary: Analyst review of potential breakout.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNelFianZTb3o2VFNiNVZNaTVWRThFQ2g0dldQSGI4bWM2UUhDb2ZrQ05TSm1ndm9JSHZFYlZLVnBiVDJacHNSTFk2cWFJT3hQZVNmNnptSHhmTWE3QThmbFFSLTBJelZPSnpSVjhxV2d4WWJQVmVhdmRVVkdUcXRyREFUSW9DRW41aDZUT2tVV05LS05idDBjOE14S2E0dkxWblZVZlB2bThOSlpHMlE?oc=5>

### PepsiCo: 4.2% Dividend Yield Looks More Attractive As Volatility Returns (NASDAQ:PEP)
- Summary: PepsiCo’s dividend yield rises to 4.2%, making the stock more appealing amid market volatility.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOdTh0WnU2YnM4N2xBM2E0aUJfbVltaGVEWmV0Z2M0aWpRQy1jVHZ6TDJLOFo0anVScHRtYUZUM2NqN1dEcGtfbS1NcXJVN2wyVW9jdjgyODlzRkdfWWJrd3FXNDZBbW80WU9wOGlLQlpmelF4SzU2MVp2M3V2V2UzZkQ1UzZPYWY2MWxVWE5wUFVKV2Z1YkZsbEdmQlpiTjlXX3JIT3dfZi0zdmY1Y21NUUpjM2tuYnZ5WFZZ?oc=5>

### PepsiCo: Staples Ugly Duckling (Rating Downgrade) (NASDAQ:PEP)
- Summary: Analysts downgrade PepsiCo’s rating, citing concerns over its staples segment performance.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxQUzhlU2RhMjJZcHpGWHd0VjJMaGdOdmZxN092LTZiMkRmc2k1V3prUk1xdFViRkRoblNUXy1VUTFneWgyeXIxR3hCNnZOb0dKQ3RYNUVtZW1wQ3hxd09ESFBOc1dELUR1VXFrZ2daU1dXbnVZSVVqZWRtcnhGT1VLcTNpRkZQRjg?oc=5>

### PepsiCo: Cheap, With A Record Dividend, But The Downtrend Channel Still Rules (NASDAQ:PEP)
- Summary: PepsiCo trades cheaply with a record dividend, yet remains in a downtrend channel.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNbVQ3MXA0WFQ2dXNJbU1pV2V5MUE3dWF0Wnpva0prR1ZaZXlxamRNYWJNTXB4eHRQY0tqajU2TVp0eGZGWWRjMllvdDNRZkJhbkFXRWJxZnVwT05hVTdSWS1fcVZQaVlrXzlwMmlIekpyQ2NtaFZzY1R4V2k4aXlqeTN4Q21SUGh2bDlsRkhKUWEzN1RHOFBIYjdnTERzR0RZOC1UaDR0cmtWME1GMDBqUmpjQjMyUQ?oc=5>

### Pepsi Has Drawn My Interest (NASDAQ:PEP)
- Summary: The author expresses interest in PepsiCo, indicating potential positive outlook.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE9rZkZremh6dVBzNE1ETGNoVEplbXFuMUVndzlva042T2pKUnViWk5YMUF3cGN5RFNOLTgwamhna0h5TnNuaUtpWnk4eWwwWk1qUXpzU0dqcmV2NVYtYU1LbEt0UkRvWm9BM0RueVNsRWo4UW9VRGNCM044THRmUjg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **17.95** | **8.73** | **12.28** | **5.60** | **194,435,891,200.00 USD** | **2.04** |
| KO | 28.80 | 11.24 | 25.68 | 7.40 | 419,951,706,112.00 USD | 38.06 |
| MNST | 38.34 | 8.39 | 26.50 | 16.70 | 82,548,277,248.00 USD | 15.16 |
| KDP | 32.25 | 1.92 | 16.49 | 70.60 | 51,108,614,144.00 USD | 35.02 |

Peers fetched as_of: 2026-11-24; PEP reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-08
- Revenue (latest available single quarter): 25,274,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,048,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/77476/000007747626000048/pep-20260905.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNQ0V2bUwxb1Y4Y2NrS2ZkNm1LOWx5S19rLUJHSVhyZy1lLWJEZVVsMng0R05OWUV2NlN3S1hVVXVzUndlZnJMV3ppQUNuT3dsMFF3cjE0RlpZTXVXSE90dVJzQ05CWlJtRm1KWFdJMm1HdkNrV2ZQdkhQQ2NzOFNLRkVOWjlUZ3NFdmNSMzJNWHFURG1vOV9SZDFPV3N6SHFXOEN4eVpUU3NleUNSRlZOZWZweHB3S09QcFA1bnBPaTFIcHVCbDhOZVotS0dkVkhqUUR4UNIB2gFBVV95cUxPaU9CUFBiUnptNnFLNVE5MlFhdEEyYlI2MXEtNEhRLVlMS1pDOEdoc0NQbkRvQUc5eDhfV3ZOUW96M3FtbDBweElJdTZrZEl4ZWQ3YjNtUzFnU3BUbG9vdGZtQkVjbXVvbWhHd3lwa3AycnhacGg2MW5pSjZtY0sxZ1pMSFluUEJSRUZEOTFZbzVWTnRUb0g2cEhPWGFhTlZQaS1fQ0lkMU00MXFORjVsUTZySVMydTV6ZUZydER4SC1Rck5jM2Q4dkZWWjRydFhfMDQ1dElKMk8yZw?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxNOUplZFJ4dUlHX1FGSHE0dFZ5RlVSVXdBWkduY1BoaTRXYWpsT3NIbllraG1aVTlCRTRuUG05RmNseDZJbDhZSlc0enRBbk5qME5yWUdQbkh6dDNXaVRsQVNuVkJJVThIZVNyYmxsbjRsNjkxNjZjdmRNREZReDQtTWVFSmhUa2tjMERKQkpJMmdJMFdiMzJuZC1sekRDamxQSHN6bXhyVTZLRDNFWmZCaExIcjUycXZRUzdJZldlT0gzSmJlSTU0OE5B?oc=5
- https://news.google.com/rss/articles/CBMijAJBVV95cUxPTDlHUUtsS1NhQ1RaeWV0YjQ1eVRLZnNoRnRoR1RXZ3RoSkNqYzNUR2hmZTZGc0stQjZUeTFVOG1YaElSelVPRVo2OU1wY3NqaUhTTzJXNVRka2VMc1ByZzVVaXZxZnVWRktKdDdPNlQ0dnJRUTZaMVZ3LXJoVEd4cUJKOUx3LVZ2bHFTSi1XeE9NajQ4Q2ZkdTJ5X1lCVjFvZW1PRzJOX3QtcF9MeXVpbVFGVS1PM1BWY3dyMzNqV1AyTnFZQlhJNlRVdFRfUGhZYXkxTkJjN1dOclVPNzU2a2F5aWFoc1AxbXlPckJaaHpPYmdFSzY3dFJRaEtaZ3NUSUQtM0toTE5MbXpu?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPUmtpWWdERFlMcFNZOTJ3eFhBNUFpSEZTVWhPczBpS3p5RUJyZGFZYV9LYUxDb1RtajhzOFRqZDJVQmRYbzA0M3lCVjAwY182NDZEaTlNMndiUEg1dFEzUEpRdXVESVZUWEF6blEtTHdRdlE5RnJIemtWRXQyR2lLNmN6SlVUS2dyRktJb2JB?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxNalNIYng0Ulo0eGVKTF90dldxamJLT1hBVS1XUUs5anEwWk00WV9NMEVaTXlDYnhUM0NkQVRnZ2lmNnJIZURiX1RuM3RacFp1ZWFRM0tld3JvS0xiWmVKMmp3TTVEY1cwak00NWM3RHpWdnRiMm5yQ004bksyQzdGVGNoTlNqLVg1WlViTnBvRTNjVkR1MmxiaGdrQ1BnajN5UlJiZTZVT200X0JuUElEd1V0VnB3QWtNNTFwQkpQaUxmOXJKVVZpNzRfUlVYaDRXOFpRZjB0ZjlhQWx1RkxHX3duaXpMdjB3bEZv?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxONnNDY1JCVHh6M0lLSi1wWTQ4WW9Bb0xoeFhwQ0c1UEhvSlRXOW5uTFZQakhyd3NCdUJZRjdUVFQzWk44WXhvRUxaM0hMZ3lmOUNEd2hjZFhoRVBqeTNMSkNaeUdKMVZKQTgtRDd2c29uTlBkV2Y0MG1Db0FrRVpkTG5HU0tfT1ZrMGR3TlFRdXUtOHFxNmhSOEhrMFZObTA?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxOT3ctYUZMSGdjY2o2WFJvcElIdkZWcHlUd2NweGxJRFpHLVhvVzJQaENEMVpXTGlNamhPU28wd1JEMWhSRzRIU0dSdHNGa3JwcFpBTUxlSUw0alVSVEtEc00xYXBTVEl5NkZfOHM2R3ZIeWZxRTVHUi02THNMRk91eTFZR2p6YzRIY2lLWTktUFlMdHNwXzRxZjlac1oyODVFX2NJ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNWlJCOW9wd2tPRXh5dHpPLV95R0pCQkdFR1o1cFNYSnFzMlVXWG1kRGxHeGJ0NV9QR2gzM0dqTmJJaUdCQUprTWRNVmxMUmFfNzZvcW1MUVRGU1pZemVVWmxhd0syYTNaU2hjbWVHMDdmaW1mUnhPZWhJQXl6S3dmZ0lDOFlsQXpCMG1NOEpFSmVZaHBfeUlMRzZTS2JIWWd3R0E?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQVUdmVlJzZ1hCcW1ubUtSVU5sUnpPTkNmUklJOHhRRG1DVV92MkZKVWd6YkVaU0lLTml2dmJ0b1pyZkpLSFVJYnpXcXE5T1hJSkVoQWlhQWxzWWlCS3AtOTNLdnkyaGNYVG5MMVBiSVZXWmYweXJubkFQcEhadDZOUGxmdGRXdm1vWHJOQU9JcXdydGs?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPRGlRbFpjUVZkM1B0Rk4wZVVLRlhuaVN6ZHZkY2tCT3ZiU3p1XzVBRG1KbWFiVEFHR19GSkpyOGlRYXF2blRfUEZ2QkZ2TXBPb1ZMZnFzOFFqUjVyaFRydks0QzRWbjI1MEhWbUpJakd1UFJ1Vi1GNnRBMjRmNG5RTFZJV0lRcnQ5LVlwUA?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNTVFiVXNnMmNNTlZ4UzA0QlFEZV94WVluckhCT1hsVjJnTXc5NkhiRnVyR0tTQ3phaWNDci0xZWpjQmpoWjA0X2JTU3dzalcyc1djU3gxY0hDV0ZKM0lBZDhINS1LM3VvMHRLUHpTbVhqTVdQb2I1ZU1nbS1BazlCS1pUSWp0TjUtX1NaZDRYVmZzR0VNUDZUeA?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNd0k0OXppUmNGUDRQbW5KakdGX1lDZkVWdVgzTEZyWVRkTjcwWHI1V3FZb18wNTNhMlZZRUcyajFudllRT0RIU0JaT2JBU1VROGRnSGFEUnRYNjdhbnF2aWYtU0pYaDVJemJfRXpFRkRsVVRwcFNiekdZOGdjbjlXZHNuYjA0ek44S05mYWF3OERtNHVCZmNPT3I3dmJyMld5U3k4azYydUpXd2FrdV96VThaOEhYbmM?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxPY1RDT3BNamFzeFl5MElfMVFfVnd3UlNzQlM0MGlfWG1SRFhuRDQwQm5NdXpHa2FPNHFHWGtkNDZuMGs1cVlwYW9NTEFEWm9hT0tPOUc2RUttUEtteFhxdzREaEZrZEpIMGJ3R3k0OTJVSmdsMThxR2J3NzAzUUpTUUVYbFpmOEtfelFSY0hFR1BvbnY0MXZ5M0lfS0JfRndmaEhMMGtZVy1SenJnb3EyMTZHVEktT2xrUnUxWE9BUkF3eWZGUG85ZGNYdXpkU3RNMGI0NVkxdDV1Z9IB2gFBVV95cUxPY1RDT3BNamFzeFl5MElfMVFfVnd3UlNzQlM0MGlfWG1SRFhuRDQwQm5NdXpHa2FPNHFHWGtkNDZuMGs1cVlwYW9NTEFEWm9hT0tPOUc2RUttUEtteFhxdzREaEZrZEpIMGJ3R3k0OTJVSmdsMThxR2J3NzAzUUpTUUVYbFpmOEtfelFSY0hFR1BvbnY0MXZ5M0lfS0JfRndmaEhMMGtZVy1SenJnb3EyMTZHVEktT2xrUnUxWE9BUkF3eWZGUG85ZGNYdXpkU3RNMGI0NVkxdDV1Zw?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNelFianZTb3o2VFNiNVZNaTVWRThFQ2g0dldQSGI4bWM2UUhDb2ZrQ05TSm1ndm9JSHZFYlZLVnBiVDJacHNSTFk2cWFJT3hQZVNmNnptSHhmTWE3QThmbFFSLTBJelZPSnpSVjhxV2d4WWJQVmVhdmRVVkdUcXRyREFUSW9DRW41aDZUT2tVV05LS05idDBjOE14S2E0dkxWblZVZlB2bThOSlpHMlE?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOdTh0WnU2YnM4N2xBM2E0aUJfbVltaGVEWmV0Z2M0aWpRQy1jVHZ6TDJLOFo0anVScHRtYUZUM2NqN1dEcGtfbS1NcXJVN2wyVW9jdjgyODlzRkdfWWJrd3FXNDZBbW80WU9wOGlLQlpmelF4SzU2MVp2M3V2V2UzZkQ1UzZPYWY2MWxVWE5wUFVKV2Z1YkZsbEdmQlpiTjlXX3JIT3dfZi0zdmY1Y21NUUpjM2tuYnZ5WFZZ?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxQUzhlU2RhMjJZcHpGWHd0VjJMaGdOdmZxN092LTZiMkRmc2k1V3prUk1xdFViRkRoblNUXy1VUTFneWgyeXIxR3hCNnZOb0dKQ3RYNUVtZW1wQ3hxd09ESFBOc1dELUR1VXFrZ2daU1dXbnVZSVVqZWRtcnhGT1VLcTNpRkZQRjg?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxNbVQ3MXA0WFQ2dXNJbU1pV2V5MUE3dWF0Wnpva0prR1ZaZXlxamRNYWJNTXB4eHRQY0tqajU2TVp0eGZGWWRjMllvdDNRZkJhbkFXRWJxZnVwT05hVTdSWS1fcVZQaVlrXzlwMmlIekpyQ2NtaFZzY1R4V2k4aXlqeTN4Q21SUGh2bDlsRkhKUWEzN1RHOFBIYjdnTERzR0RZOC1UaDR0cmtWME1GMDBqUmpjQjMyUQ?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE9rZkZremh6dVBzNE1ETGNoVEplbXFuMUVndzlva042T2pKUnViWk5YMUF3cGN5RFNOLTgwamhna0h5TnNuaUtpWnk4eWwwWk1qUXpzU0dqcmV2NVYtYU1LbEt0UkRvWm9BM0RueVNsRWo4UW9VRGNCM044THRmUjg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
