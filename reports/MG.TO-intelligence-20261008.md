# MG.TO Intelligence Demo

- ticker: **MG.TO**
- Report as_of: **2026-10-08**
- Market data as_of: **2026-10-07**
- Quant sources: https://finance.yahoo.com/quote/MG.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MG.TO/key-statistics/
- AI analysis snapshot as_of: **2026-10-03** (retained; this run refreshes market data only)
- Snapshot note: the report-date daily bar may be intraday until the US market closes; its Close field is provisional. News, peers, earnings, EDGAR and macro sections reuse their existing snapshots.
- Market data fetched_at (UTC): **2026-10-08T04:16:39.365557+00:00**
- AI status: **Available**
- AI model: **gemini-3.5-flash-lite** (25 Google News RSS headlines -> AI extraction and classification; free-tier grounding unavailable, using RSS + AI)

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 92.6200 |
| Return 1D (%) | -0.7288 |
| Return 1W (%) | 2.1619 |
| Return 1M (%) | -2.8631 |
| Return YTD (%) | 29.4844 |
| Return 1Y (%) | 47.2259 |
| Annualized volatility (%) | 37.1690 |
| Beta vs SPY | 1.1659 |
| Max drawdown (%) | -22.7904 |
| Sharpe (rf=0) | 1.2250 |
| P/E (trailing) | 24.63 |
| P/B | 1.53 |
| EV/EBITDA | 7.01 |
| Revenue growth (%) | 3.30 |
| MA50 | 93.3029 |
| Close vs MA50 (%) | -0.7319 |
| MA200 | 84.9219 |
| Close vs MA200 (%) | 9.0649 |
| RSI (14, Wilder) | 53.1326 |
| MACD (12,26) | 0.0605 |
| MACD signal (9) | -0.4223 |
| MACD histogram | 0.4827 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MG.TO': 255, 'SPY': 255}.

## TAILWINDS

### Magna International: Stock To Go Higher On Margin Expansion And Earnings Growth
- Summary: Magna International: Stock To Go Higher On Margin Expansion And Earnings Growth
- Date: 2026-05-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxOVDdvU2ZJRFgwTEZEakg3ckVRanZtZHJXNmluYWRoSHI4T3J1SUpfTUtvTHdHNWpFdmpXMHpXM1JOU09qSWZ5bENWZVpSZEV6UFNuU0FuNXIxVDhJV2VWcUtEUXAzUFdiMmxhWW0xMjVSdkJTdnFRWjAxT3c2emZFZWVkYm96emUxVldncE5SWExXd3pDbHpVc1dDdkhLTHJhNFAyMnFOX2FzalY2aUV4b2pfS05ZWW1qOTIwTVJMclFxaHc?oc=5>

### Magna International (TSX:MG) Stock Jumps On Record Earnings And Margin Repair
- Summary: Magna International (TSX:MG) Stock Jumps On Record Earnings And Margin Repair
- Date: 2026-08-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiWEFVX3lxTE5jVHQyQVFFeTZHVGR5M2pLSXNob3RjSjV2QS1hSVl2c0V5VkVoYTFxYVRVUGwyM2l0Zmk4T3lVaThyVW9GbVpocWdNZ2t1NHd4QW1jQ0lTZzI?oc=5>

### Does Magna International (TSX:MG) Have A Mirror-Integrated Edge In Auto Safety Electronics?
- Summary: Article questions whether Magna has a mirror-integrated edge in auto safety electronics.
- Date: 2026-05-24 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOOVhqVTJJT3NKOUxVS1NUUHI3NVdNUUJKcEdKbEZJSEYyRndFQms5VFNXX3FwY213SmNqR3N1cWJtTGNXTHRqSm9HMmwzUFM0WDVPR2FJUkNZcVVneDZ1NER1aUdqQ3hudFdUa1Y3QWhjSW1kSkJJeERpOUdQQWliUGNtVHVROG1GM2hLa3gxaDZiVGIySHA3Ump5OFY?oc=5>

### Does Magna’s Q1 Earnings Beat and Cash Flow Strength Change The Bull Case For Magna (TSX:MG)?
- Summary: Magna reported a Q1 earnings beat and cash flow strength, prompting questions about the bull case.
- Date: 2026-05-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOVDlwWmhaenJ2RGtPRVVVc1J6SmNYcjBiVllDNDZaVkVFU181aEdMdlBpLU5XbWxlQWlURTQxdVNFR2laX1RTMl9IUHRCbjhKanJyaW5ZaHBJMFF1UG1EZFVjX0pOeFFfeDBBUWVNNzlIbUxfUkk5SXVYRVduUXNWWDRNeHFocTVPc3RrcXhXcDBwM2dXVFJr?oc=5>

## HEADWINDS

### --BMO Capital Downgrades Magna International to Market Perform From Outperform, Adjusts PT to CA$97.90 From CA$105.17
- Summary: --BMO Capital Downgrades Magna International to Market Perform From Outperform, Adjusts PT to CA$97.90 From CA$105.17
- Date: 2026-09-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxQMkRLQnVLRzJxazhobndoLV9yRFdudUFSUFB3R3FReExQSGd4aFVJd0pSRUxxYmNPd2ZVcjVXTDJCdlU4LWN0cW52Z3lyX3NlSzVUOXVIdTYzSHI2UUI3Sm9xdENTSnpBamVwcGxLUjVDVHZMSXhma1R4bWpydVRzQlR5TWxuZFhDVEU4a3BHczlhMWpDMkhEalZzcThSY3hQb1ZXUmJ1YW9KcDA?oc=5>

### Magna Earnings: Guidance Hike Not Enough to Appease a Jittery Market
- Summary: Magna raised its guidance, but it was not enough to appease a jittery market.
- Date: 2026-07-31 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOTHM5ck9jZ2VSN0VmdWZQXzhBQWNUMXFna25sZG4ydDZscVlBbGF6Y2w2TFJxb3BVRFdQX3RSVzZINjhobTU3RDVweGRFQ2tkbGZ3OF85QVJpekotbnRRZDRmWE9DeGZIdjEyVFBoZTFBYzVXUkFudlpFN2c1TVMzNFVaQlZ6NHJ1ZEl6WDNFaFo4WW5IdkJkNGRBMTNUU1NXakkwajhLYTloZw?oc=5>

## CATALYSTS

### Magna International Inc. 2026 Q1 - Results - Earnings Call Presentation (TSX:MG:CA) 2026-05-01
- Summary: Magna International Inc. 2026 Q1 - Results - Earnings Call Presentation (TSX:MG:CA) 2026-05-01
- Date: 2026-05-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPaEhQWFpOWURMR1AxYUpRb005SDY1ZVl4a1lMRmMyS2tPTzVvRXVCZ1JVZzlVNmtHOFNncnRFVi1nQzdlcW5lUUtPZm5VdmU3VnNpM002QnlWVFVtaVVZMjhNTlR4VjBpelhqVk9JR0VITVlqVkJmcmdUY1g2SWZvZDc1M3NKOXMyR2NaZUdqYkxzVktxN0JkeVlndVlVUnJEY3lDeGZXdFh1X0E?oc=5>

### Assessing Magna International (TSX:MG) Valuation After Board Changes Earnings Update And Capital Return Moves
- Summary: Assessing Magna International (TSX:MG) Valuation After Board Changes Earnings Update And Capital Return Moves
- Date: 2026-05-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPRUpzLXVSN01nYUNLNVY0T3c1a0VWdG1qYVgzaUtrbkp6TWRZSm9BNmdyeEJ6MTl0dEthS1pLVHUxNEhhVm9wRFlMSHZEVHU4R2FoUjZybnd4aGVXS1lJdmszdFlOUnVWbHRnUWlGVXFHVWpLMFZsVFJiYWFrZG9VYXp1ZTd0UmRxS2pMTldRc29ha1RNbmNpUDZ3d0gzUUhMcjNz?oc=5>

### Magna International (MGA) Soars to 4-Year High on Revenue Blowout, Buyback
- Summary: Magna International (MGA) Soars to 4-Year High on Revenue Blowout, Buyback
- Date: 2026-02-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxQNmMzT21zZTFtc18zc2JHTVBNaUpUTU1HLWRKRjVHQjFrR3c5d3plUDlQMzNhOWV1ME5uMTJLZkRvN040WkFNblQyUzhVTE5JeTFXakZQTmxEM1pmb0R2TUx0M3JZaWxhWEtwU2VsU3MyUm01S1pvRWYyUk5Wei1OSzc3TQ?oc=5>

### TD Securities Maintains Buy Rating on Magna International (MGA)
- Summary: TD Securities maintains a buy rating on Magna International.
- Date: 2026-05-14 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQU2N5TUNxQl9UVDBBdFFmb0xQX01tdU5pc0gxNXEyeUJrdmptamRiMS0ybDdWakRXTUcxV1BxRjRNU1BGSWJqMnBEaHJQSHFQekV1cXR1bE54NXZyZWpSNkZUaE9fc1ZZcTBRSjRReTFBa0wyYU82cVl1UTlBd0NUQ1hhaFlLb2VRUERmZVhweDI2UEZmenFUUjhwV1ZScVB6?oc=5>

## RISKS

### With 81% ownership of the shares, Magna International Inc. (TSE:MG) is heavily dominated by institutional owners
- Summary: Magna International Inc. is heavily dominated by institutional owners holding 81% of the shares.
- Date: 2025-07-21 | Impact: low | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxNbXBPSzQ3Y3UwaUFhQ0dLWThQa2FYOFV2Mlo0NjRldFhRUEE0Y2dmb0FtMUZDRm4yS2VCZ3JfM0lSV1ctTzJzbGdvcW1rZE5wRHYyM3J0a01PbVgtWjJfcm1HNHJXanNHV3F3alRGY3NaUTB4aFljanE5Q3p4em5hbEhaQ1hsOGJMVXZPdnFR?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (USD) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MG.TO** | **24.63** | **1.53** | **7.01** | **3.30** | **24,777,689,088.00** | **47.23** |

Peers fetched as_of: 2026-10-08; MG.TO reuses existing data (market data as_of: 2026-10-07); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-31
- Next expected earnings: 2026-10-30 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment Rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index | CPIAUCSL | 334.13 | 2026-08-01 |
| Federal Funds Effective Rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-10
- Revenue (latest available single quarter): 193,132,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 7,581,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1436126/000162828026055351/mg-20260630.htm

SEC requests use the demo placeholder contact email contact@example.com. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiwwFBVV95cUxOVDdvU2ZJRFgwTEZEakg3ckVRanZtZHJXNmluYWRoSHI4T3J1SUpfTUtvTHdHNWpFdmpXMHpXM1JOU09qSWZ5bENWZVpSZEV6UFNuU0FuNXIxVDhJV2VWcUtEUXAzUFdiMmxhWW0xMjVSdkJTdnFRWjAxT3c2emZFZWVkYm96emUxVldncE5SWExXd3pDbHpVc1dDdkhLTHJhNFAyMnFOX2FzalY2aUV4b2pfS05ZWW1qOTIwTVJMclFxaHc?oc=5
- https://news.google.com/rss/articles/CBMiWEFVX3lxTE5jVHQyQVFFeTZHVGR5M2pLSXNob3RjSjV2QS1hSVl2c0V5VkVoYTFxYVRVUGwyM2l0Zmk4T3lVaThyVW9GbVpocWdNZ2t1NHd4QW1jQ0lTZzI?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOOVhqVTJJT3NKOUxVS1NUUHI3NVdNUUJKcEdKbEZJSEYyRndFQms5VFNXX3FwY213SmNqR3N1cWJtTGNXTHRqSm9HMmwzUFM0WDVPR2FJUkNZcVVneDZ1NER1aUdqQ3hudFdUa1Y3QWhjSW1kSkJJeERpOUdQQWliUGNtVHVROG1GM2hLa3gxaDZiVGIySHA3Ump5OFY?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOVDlwWmhaenJ2RGtPRVVVc1J6SmNYcjBiVllDNDZaVkVFU181aEdMdlBpLU5XbWxlQWlURTQxdVNFR2laX1RTMl9IUHRCbjhKanJyaW5ZaHBJMFF1UG1EZFVjX0pOeFFfeDBBUWVNNzlIbUxfUkk5SXVYRVduUXNWWDRNeHFocTVPc3RrcXhXcDBwM2dXVFJr?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxQMkRLQnVLRzJxazhobndoLV9yRFdudUFSUFB3R3FReExQSGd4aFVJd0pSRUxxYmNPd2ZVcjVXTDJCdlU4LWN0cW52Z3lyX3NlSzVUOXVIdTYzSHI2UUI3Sm9xdENTSnpBamVwcGxLUjVDVHZMSXhma1R4bWpydVRzQlR5TWxuZFhDVEU4a3BHczlhMWpDMkhEalZzcThSY3hQb1ZXUmJ1YW9KcDA?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOTHM5ck9jZ2VSN0VmdWZQXzhBQWNUMXFna25sZG4ydDZscVlBbGF6Y2w2TFJxb3BVRFdQX3RSVzZINjhobTU3RDVweGRFQ2tkbGZ3OF85QVJpekotbnRRZDRmWE9DeGZIdjEyVFBoZTFBYzVXUkFudlpFN2c1TVMzNFVaQlZ6NHJ1ZEl6WDNFaFo4WW5IdkJkNGRBMTNUU1NXakkwajhLYTloZw?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPaEhQWFpOWURMR1AxYUpRb005SDY1ZVl4a1lMRmMyS2tPTzVvRXVCZ1JVZzlVNmtHOFNncnRFVi1nQzdlcW5lUUtPZm5VdmU3VnNpM002QnlWVFVtaVVZMjhNTlR4VjBpelhqVk9JR0VITVlqVkJmcmdUY1g2SWZvZDc1M3NKOXMyR2NaZUdqYkxzVktxN0JkeVlndVlVUnJEY3lDeGZXdFh1X0E?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPRUpzLXVSN01nYUNLNVY0T3c1a0VWdG1qYVgzaUtrbkp6TWRZSm9BNmdyeEJ6MTl0dEthS1pLVHUxNEhhVm9wRFlMSHZEVHU4R2FoUjZybnd4aGVXS1lJdmszdFlOUnVWbHRnUWlGVXFHVWpLMFZsVFJiYWFrZG9VYXp1ZTd0UmRxS2pMTldRc29ha1RNbmNpUDZ3d0gzUUhMcjNz?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxQNmMzT21zZTFtc18zc2JHTVBNaUpUTU1HLWRKRjVHQjFrR3c5d3plUDlQMzNhOWV1ME5uMTJLZkRvN040WkFNblQyUzhVTE5JeTFXakZQTmxEM1pmb0R2TUx0M3JZaWxhWEtwU2VsU3MyUm01S1pvRWYyUk5Wei1OSzc3TQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQU2N5TUNxQl9UVDBBdFFmb0xQX01tdU5pc0gxNXEyeUJrdmptamRiMS0ybDdWakRXTUcxV1BxRjRNU1BGSWJqMnBEaHJQSHFQekV1cXR1bE54NXZyZWpSNkZUaE9fc1ZZcTBRSjRReTFBa0wyYU82cVl1UTlBd0NUQ1hhaFlLb2VRUERmZVhweDI2UEZmenFUUjhwV1ZScVB6?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxNbXBPSzQ3Y3UwaUFhQ0dLWThQa2FYOFV2Mlo0NjRldFhRUEE0Y2dmb0FtMUZDRm4yS2VCZ3JfM0lSV1ctTzJzbGdvcW1rZE5wRHYyM3J0a01PbVgtWjJfcm1HNHJXanNHV3F3alRGY3NaUTB4aFljanE5Q3p4em5hbEhaQ1hsOGJMVXZPdnFR?oc=5

## Demo notes and limitations

- Multi-ticker local demo; AI items require human spot checks; RSS coverage is not guaranteed.
- Free-tier Gemini grounding (google_search tool) returned 429; the demo uses Google News RSS + plain-text AI extraction.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
