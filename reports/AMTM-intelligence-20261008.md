# AMTM Intelligence Demo

- ticker: **AMTM**
- Report as_of: **2026-10-08**
- Market data as_of: **2026-10-07**
- Quant sources: https://finance.yahoo.com/quote/AMTM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMTM/key-statistics/
- AI analysis snapshot as_of: **2026-10-03** (retained; this run refreshes market data only)
- Snapshot note: the report-date daily bar may be intraday until the US market closes; its Close field is provisional. News, peers, earnings, EDGAR and macro sections reuse their existing snapshots.
- Market data fetched_at (UTC): **2026-10-08T04:18:15.883799+00:00**
- AI status: **Available**
- AI model: **gemini-3.5-flash-lite** (25 Google News RSS headlines -> AI extraction and classification; free-tier grounding unavailable, using RSS + AI)

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 18.5100 |
| Return 1D (%) | -1.3852 |
| Return 1W (%) | 2.1523 |
| Return 1M (%) | -7.7268 |
| Return YTD (%) | -36.1724 |
| Return 1Y (%) | -26.6931 |
| Annualized volatility (%) | 46.5791 |
| Beta vs SPY | 1.1723 |
| Max drawdown (%) | -51.7186 |
| Sharpe (rf=0) | -0.4415 |
| P/E (trailing) | 22.57 |
| P/B | 0.96 |
| EV/EBITDA | 8.00 |
| Revenue growth (%) | -2.00 |
| MA50 | 20.5328 |
| Close vs MA50 (%) | -9.8516 |
| MA200 | 25.4081 |
| Close vs MA200 (%) | -27.1492 |
| RSI (14, Wilder) | 40.0233 |
| MACD (12,26) | -0.5763 |
| MACD signal (9) | -0.5717 |
| MACD histogram | -0.0045 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMTM': 255, 'SPY': 255}.

## TAILWINDS

### Amentum Holdings (AMTM) Wins NASA Contract Following A Fair Value Debate
- Summary: Amentum Holdings (AMTM) Wins NASA Contract Following A Fair Value Debate
- Date: 2026-08-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPWDQ4SWVLeGx5bTduODR3VVVYaFpKYXFfSDN4bXdqeWVfRVdLOXNFM3drVzJ4RHREdTBFQjNLenEtS2c5djhYSVFicTF6R1RJaTFqTy1wUFUzdFRpekFrdW1MM0lRTG4zcUtnYWY5b0hBZ1RCRjhJR1FFMmloeTJEeXRhZmJFa0wwbkhnV3lEUFdrLWZLMXdhX21yUXQ?oc=5>

### Amentum Holdings (AMTM) Beats Q3 Earnings Estimates
- Summary: Amentum Holdings (AMTM) Beats Q3 Earnings Estimates
- Date: 2026-08-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOUTFlc3VXTUFObWt2bGlGdnVoSEhGdEFzUXdiSDcyd21PWkRUeDF6QVRUX2RHMEhDRl9iOGpsdHZucGJDM1pzYU1hSW96TjMtVWo1X3pIWUFtOVlyNmJaMEE1SmVjQnF4SWJFM3l5cHdMb3NackNYVENMbG5WV0xxVzNlbDhVN2s0dkI5eGd4bXJwakk1NVFYbmZ5Zw?oc=5>

### Amentum Needs Revenue Growth to Re-rate Higher, Morgan Stanley Says
- Summary: Amentum Needs Revenue Growth to Re-rate Higher, Morgan Stanley Says
- Date: 2026-08-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPNzhPbEhQcmN2N3prVU0zOHdRYWUtcFVHa3Rma2RzWFhJWU5hVlRXSjMwQURZZUdTbXNxWG5yNjk3NEpEVG90TmlVYzlxT1JKRmZ6cFhXMjhSdXVOUVh0MVA1LS00elN5VE0tQUh0VnFpT0N1TkdTQS1KTG4zeEVSMHpvSE83RHAtQ3BTRXF0a1BtQWdlcU4wUHdWbExLak0?oc=5>

### Amentum Holdings (AMTM) Wins Preferred Sellafield Role, Is The Stock Still Undervalued?
- Summary: Amentum Holdings wins a preferred Sellafield role.
- Date: 2026-10-01 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxQNXp1TFE5dnBXaEVINnAwV25rOEhkYW9iekQya2JzSWxLRmxrZEk4bGFRNTJ1aEl2Y2tRazZMZVc4YXBXYjk3VmdtdkNQaGNMTnd1UkI3TUtqV3gzNU5ZY3dnYUd1WGFmblJXcDFlaEw3OUttVzJxaXFVLVdSYl95UUtpMDZxamVwbnVmYkhrT0FZZ1hNcDhwejFKNEt5WVZBUTZOSTBjYk1mN2xhcTRaQTZ0dmdHNkhTVUNVd3Mxekp5OS1ZaXA3ZmdUVlBnM0UwYXZSOWtBLWoyd3PSAeABQVVfeXFMTVF2aDdkZnlrZDNNeEpRaVA4TV83ZExQNEdtb1JFcURmQnE2NjBuRWJUWXVkVXF4Tk5hajZoY2VPZWEtcnBfcDlhcEdkQTJoSHlJUlVXVGZ0d3NYRzM3MXV3ZjdRcXNuOXlzcTVFNGpNYWxKX0ZfLUZvR2JwcF9pVExMQ09ZN0F4cmJldXd6ZVZ1Q3diZmtoVDhfbEJnZnBFN1RURFpmMENTUXZpT3hpVEE5TkNnc1NMTlYtYkY1RmRKb3hVNk9lbEhaamE0NGl4N1ktV3V5aFlaLUc5bTlneFQ?oc=5>

### Amentum (AMTM) Stock May Be A Bargain As Nuclear Shipyard Win Lands
- Summary: Amentum lands a nuclear shipyard win.
- Date: 2026-08-21 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPcGhLVDBiaXdDdzk1LXhKU0NPZ29nY0FIbWR0ZkFNYi1XR1ZjLWNRWnllaDNTLXZhbVhhdWdXbWhuUnJIclUtVGRaV2p4TFdFREZRZEJfX0JCUHFsUHk3SkQ5dTVXWVl5R1Z6WGhyemd5WVBFVWFscnEwZ1NVQUZqcjNnZHcyTkx4cHc5WmZVanlEQkFmZEpRbFljRQ?oc=5>

## HEADWINDS

### Amentum Holdings (AMTM) Is Down 5.5% After Winning Preferred Supplier Role On $2.8 Billion Sellafield Deal
- Summary: Amentum Holdings (AMTM) Is Down 5.5% After Winning Preferred Supplier Role On $2.8 Billion Sellafield Deal
- Date: 2026-10-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOS092VklWX3M1T2E2ZkozZUxtV0ZScWdOWl9JYnJGeHIwQjJRdElUVXpXZVRDRC1KNVB0bHU2OEpUa1JDU2I0MDh0VEk3UXk2bkU2QkloUWl3TEgxOG43NC0tZWozT0pxcEMtQU1FNXhyT25reEtBVXRJVlRVVzUxUHZLVHBEcTJBNTdwWkp4RDh5UVpwNzdTSw?oc=5>

### Amentum (NYSE:AMTM) Misses Q2 CY2026 Revenue Estimates, Stock Drops 15.1%
- Summary: Amentum (NYSE:AMTM) Misses Q2 CY2026 Revenue Estimates, Stock Drops 15.1%
- Date: 2026-08-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNZ3d6Vk10NDF3RUtFRDE1eUJsTlBuT1Rfa00zRjJsN3JLS3Y3LTJJNXd2cTdCMUh1YlJvd3BVVndMM3duQTRDLWdRYWEyYlBKQ0FWYjFWQVJ0b3o1OTBWNURYMHV4empjNzJiYWNZOGxRMnFSbUhzY0pCaUlkcV9UNTBod2tweVpGblFuWGcwT25jSm13UVBJ?oc=5>

### Why Amentum (AMTM) Shares Are Trading Lower Today
- Summary: Why Amentum (AMTM) Shares Are Trading Lower Today
- Date: 2026-08-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQTWZCMGhpbjg5cXh5Y0s1LUNWX21BRWw1MllsUmFXRmJvZF9XSGZ0VnZqSnFZd0lQVzZ2ZjJ2Q05fQ3RUMnRfMVl4Zko0LWtlWjVLTHhPOWV3eVR0QlkyQkJNdjFPLWs1RFJweTV0RW5kMUZ1Y1lPSzVFeHFOUUVNVVdfNXlKRnNiSjNPNC0wY2c3LWZ5LTQwaW1lcXY?oc=5>

### Amentum (AMTM) Stock Drops Despite Margin Strength And Higher EPS Outlook
- Summary: Amentum stock drops despite margin strength and a higher EPS outlook.
- Date: 2026-08-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxNSjhOcTFZSnRDOEdNOTRrNWlBeTlMLUdkcnJGODM2c3M3UWZhUTNjMU4zSUJ1OWpPMXFUNXBvNnZvMHN3Q29MbmlLdzVnVGw5Z3R2VDBXSXJFYy1oYXlmOE1XbkJ1Nk91bHN6bVlMd3FxWHRURUtSNi1ldDNMTmlIVmZBaW5sX1FEc3B3T0xiTzNlNTJwMzJRUFlwNVV6OVZkcm8xNk9INzhtWk51MGhVS0N6Wm5rbW8zTS1LWkwweWpjTTAzWHdTYmlpejBRUG5ZamdmdG1VRnVaeE3SAeABQVVfeXFMT19BaVBDNFUzcFRZNjlqeFBpNHRzMUFNQURLVFZIWUR6NWdWMzZwYWFySTR4cTQxTWY5ckNhMDlUR1hRT3dveHJhWmdnM251b3RzcXdEZm56MjlpTm5IX0ZRZEpuM0diUjd6UkFtYUVWeTJFZWdDX0djcTVIc3RZV3V6UFhGbF9TZkhZaGxLZFgzSFBINHBUR2Vjbkp4UmxOaTR5Vzg0VjlwNE54ZDR1TEJnMHltaHNoTlVjNGRUX1JWQThJREJRNVBTOEU3cjhVNy11ZlNQS3BfTTYxS0UzT0Y?oc=5>

## CATALYSTS

### Amentum Holdings (AMTM) Reports Next Week: Wall Street Expects Earnings Growth
- Summary: Amentum Holdings (AMTM) Reports Next Week: Wall Street Expects Earnings Growth
- Date: 2026-08-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQMVZZOHhVRDM1clFBalVWZUVfTVk5TVkySkRfU3RWSU94QVVwd1FJR0RBWU54c3dlU21ubjd1dWIyT210alU0Y0tEazlibk55UFNnM2xtbmtGZDNKemRyRXRmNTVrTVdCckhwVk9fa05aNVlIcVhUY2J4S3dNMDhoZWRmbVlKT194ekZxNDBXbndRSlV1MXZlS01yRzZuTDBC?oc=5>

### Amentum Holdings Inc (AMTM) (Q3 2026) Earnings Call Highlights: Record Margins and Strategic ...
- Summary: Amentum Holdings Inc (AMTM) (Q3 2026) Earnings Call Highlights: Record Margins and Strategic ...
- Date: 2026-08-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPbGtmd09nQXp1OEF3ZWFtOFlyOVdPb2V5eERod0VCNVRrVHhDOUhCZzRGVzYwNVJLQTJMY2MwMlFzdU8tWWZEZ0RhZlBPMVJOUFdfQ1NaYmZvX2dOVGt3dllub3pobFNoRUZHalIwaWlxMDdwbmtLWVNVbXhBazBuUERfQ2xlZHRWNUJBeGhQUmhHdDg3N2wtRA?oc=5>

### A Look At Amentum Holdings (AMTM) Valuation After Q2 Results And Record Long Term Contract Backlog
- Summary: A Look At Amentum Holdings (AMTM) Valuation After Q2 Results And Record Long Term Contract Backlog
- Date: 2026-05-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQcWM4VjNtdFNvN2tuVTZ1S0pGeHprdFhxUE1BeElPSEYzeC13YjZoNWFiMmxndlBscWZvbWF5WW5DZ2czRGhpNXlnZWVxbUVpeGNITFZtMmVKTGFSaUh4RE5pWk90UGxlRzhOV0RSTE5aSmNkajdlNGcyTmNUTnA0R3Jfc2NxNWY3VF82cUVmLUJVbEw5aG90U1JyVWpEWDU4eUpR?oc=5>

### Amentum Holdings (AMTM) Appears Attractive With New Contract Awards
- Summary: Amentum Holdings (AMTM) Appears Attractive With New Contract Awards
- Date: 2026-07-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQNUdVWmxfZ2tQZ2VTaEtoaTRpSEVTS2pDVGQyYjc5azh2azFJSjBoRmlMakp4Rk5pUmZsTnpVRks3RjJQT09UVTkwMzNwT2xKaXp5WlMyTVZKUFZVZGMxZW5FLTZ4WGdIRWhEeXJvQVZQUHJ3bEZKVHdldmF6eHIwNFZJS21kM2Vxd203M0lKaVZhRUFIU1drc0lreWN4Z0xLZVRmc1ZlVDM?oc=5>

### Amentum Q3 Earnings Call Highlights
- Summary: Amentum Q3 Earnings Call Highlights
- Date: 2026-08-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPMmZ2Sk96akVIZjRudGdISnZjbENmNkEzT2dSMXE3QVpKS0VvYXlQUERrNTc5eWJTOWc1ZHRVWkpaU2d2azlMcFdQVHNEQ2ctWWprWnpOYlNRYzFPazNiNlVCZzBLdXFKWURYbng1bjRkVy1EZVVEa2F6UXQtblVlWDhtUjBNaW8wV1JFNXdaa0R6aEZIU0Jna09XdDVRYzN0bEE?oc=5>

### Amentum Holdings Stock: Multiple Re-Rating Incoming (NYSE:AMTM)
- Summary: Amentum Holdings stock has a multiple re-rating incoming.
- Date: 2026-06-22 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxPRDZDdktvQk03TFkxVHVUWlAwSGVmdXlPRDZYdVBjWmc1UUlIUFdFWTNPZzB2cW43VU5ySUlGT2ZubnRFTVJZaEo5R010eVhRSklyQkFwX2JBbG81a09ha01ENTA4X25uX0N6dmVBVWJSV09scDdfbHZCZm03cDRQbzZn?oc=5>

## RISKS

### A $625K base salary is set for Amentum (AMTM)'s executive chair as severance terms change.
- Summary: A $625K base salary is set for Amentum's executive chair as severance terms change.
- Date: 2026-10-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNMWo3bzEzZFpCcXZaNlhBUUloaHVTdDAtN3lEeXBFSGJtNExXemtKNFBkUFFMLWFzWThDbzd4eGFrd3lfWVRuUi0xRnh0ZnlQQUhBOE9TUWRKVkxaVVl0bGZqTWV1c2ZOS0pXaDdNYTQ4U2NmQ0tuRlNiTmxoRzBiSmJyZ0hFVzNEbFJ3YzFSeVQ3TEE0aktPdHBPcWRZYVdNcngtWVlrRWV1S0hyYnc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (USD) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMTM** | **22.57** | **0.96** | **8.00** | **-2.00** | **4,525,813,760.00** | **-26.69** |

Peers fetched as_of: 2026-10-08; AMTM reuses existing data (market data as_of: 2026-10-07); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-10
- Next expected earnings: 2026-12-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment Rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index | CPIAUCSL | 334.13 | 2026-08-01 |
| Federal Funds Effective Rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-11
- Revenue (latest available single quarter): 3,490,000,000.00 USD; period 2026-04-04/2026-07-03; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 66,000,000.00 USD; period 2026-04-04/2026-07-03; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2011286/000162828026055727/amtm-20260703.htm

SEC requests use the demo placeholder contact email contact@example.com. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinAFBVV95cUxPWDQ4SWVLeGx5bTduODR3VVVYaFpKYXFfSDN4bXdqeWVfRVdLOXNFM3drVzJ4RHREdTBFQjNLenEtS2c5djhYSVFicTF6R1RJaTFqTy1wUFUzdFRpekFrdW1MM0lRTG4zcUtnYWY5b0hBZ1RCRjhJR1FFMmloeTJEeXRhZmJFa0wwbkhnV3lEUFdrLWZLMXdhX21yUXQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOUTFlc3VXTUFObWt2bGlGdnVoSEhGdEFzUXdiSDcyd21PWkRUeDF6QVRUX2RHMEhDRl9iOGpsdHZucGJDM1pzYU1hSW96TjMtVWo1X3pIWUFtOVlyNmJaMEE1SmVjQnF4SWJFM3l5cHdMb3NackNYVENMbG5WV0xxVzNlbDhVN2s0dkI5eGd4bXJwakk1NVFYbmZ5Zw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPNzhPbEhQcmN2N3prVU0zOHdRYWUtcFVHa3Rma2RzWFhJWU5hVlRXSjMwQURZZUdTbXNxWG5yNjk3NEpEVG90TmlVYzlxT1JKRmZ6cFhXMjhSdXVOUVh0MVA1LS00elN5VE0tQUh0VnFpT0N1TkdTQS1KTG4zeEVSMHpvSE83RHAtQ3BTRXF0a1BtQWdlcU4wUHdWbExLak0?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxQNXp1TFE5dnBXaEVINnAwV25rOEhkYW9iekQya2JzSWxLRmxrZEk4bGFRNTJ1aEl2Y2tRazZMZVc4YXBXYjk3VmdtdkNQaGNMTnd1UkI3TUtqV3gzNU5ZY3dnYUd1WGFmblJXcDFlaEw3OUttVzJxaXFVLVdSYl95UUtpMDZxamVwbnVmYkhrT0FZZ1hNcDhwejFKNEt5WVZBUTZOSTBjYk1mN2xhcTRaQTZ0dmdHNkhTVUNVd3Mxekp5OS1ZaXA3ZmdUVlBnM0UwYXZSOWtBLWoyd3PSAeABQVVfeXFMTVF2aDdkZnlrZDNNeEpRaVA4TV83ZExQNEdtb1JFcURmQnE2NjBuRWJUWXVkVXF4Tk5hajZoY2VPZWEtcnBfcDlhcEdkQTJoSHlJUlVXVGZ0d3NYRzM3MXV3ZjdRcXNuOXlzcTVFNGpNYWxKX0ZfLUZvR2JwcF9pVExMQ09ZN0F4cmJldXd6ZVZ1Q3diZmtoVDhfbEJnZnBFN1RURFpmMENTUXZpT3hpVEE5TkNnc1NMTlYtYkY1RmRKb3hVNk9lbEhaamE0NGl4N1ktV3V5aFlaLUc5bTlneFQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPcGhLVDBiaXdDdzk1LXhKU0NPZ29nY0FIbWR0ZkFNYi1XR1ZjLWNRWnllaDNTLXZhbVhhdWdXbWhuUnJIclUtVGRaV2p4TFdFREZRZEJfX0JCUHFsUHk3SkQ5dTVXWVl5R1Z6WGhyemd5WVBFVWFscnEwZ1NVQUZqcjNnZHcyTkx4cHc5WmZVanlEQkFmZEpRbFljRQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOS092VklWX3M1T2E2ZkozZUxtV0ZScWdOWl9JYnJGeHIwQjJRdElUVXpXZVRDRC1KNVB0bHU2OEpUa1JDU2I0MDh0VEk3UXk2bkU2QkloUWl3TEgxOG43NC0tZWozT0pxcEMtQU1FNXhyT25reEtBVXRJVlRVVzUxUHZLVHBEcTJBNTdwWkp4RDh5UVpwNzdTSw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNZ3d6Vk10NDF3RUtFRDE1eUJsTlBuT1Rfa00zRjJsN3JLS3Y3LTJJNXd2cTdCMUh1YlJvd3BVVndMM3duQTRDLWdRYWEyYlBKQ0FWYjFWQVJ0b3o1OTBWNURYMHV4empjNzJiYWNZOGxRMnFSbUhzY0pCaUlkcV9UNTBod2tweVpGblFuWGcwT25jSm13UVBJ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQTWZCMGhpbjg5cXh5Y0s1LUNWX21BRWw1MllsUmFXRmJvZF9XSGZ0VnZqSnFZd0lQVzZ2ZjJ2Q05fQ3RUMnRfMVl4Zko0LWtlWjVLTHhPOWV3eVR0QlkyQkJNdjFPLWs1RFJweTV0RW5kMUZ1Y1lPSzVFeHFOUUVNVVdfNXlKRnNiSjNPNC0wY2c3LWZ5LTQwaW1lcXY?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxNSjhOcTFZSnRDOEdNOTRrNWlBeTlMLUdkcnJGODM2c3M3UWZhUTNjMU4zSUJ1OWpPMXFUNXBvNnZvMHN3Q29MbmlLdzVnVGw5Z3R2VDBXSXJFYy1oYXlmOE1XbkJ1Nk91bHN6bVlMd3FxWHRURUtSNi1ldDNMTmlIVmZBaW5sX1FEc3B3T0xiTzNlNTJwMzJRUFlwNVV6OVZkcm8xNk9INzhtWk51MGhVS0N6Wm5rbW8zTS1LWkwweWpjTTAzWHdTYmlpejBRUG5ZamdmdG1VRnVaeE3SAeABQVVfeXFMT19BaVBDNFUzcFRZNjlqeFBpNHRzMUFNQURLVFZIWUR6NWdWMzZwYWFySTR4cTQxTWY5ckNhMDlUR1hRT3dveHJhWmdnM251b3RzcXdEZm56MjlpTm5IX0ZRZEpuM0diUjd6UkFtYUVWeTJFZWdDX0djcTVIc3RZV3V6UFhGbF9TZkhZaGxLZFgzSFBINHBUR2Vjbkp4UmxOaTR5Vzg0VjlwNE54ZDR1TEJnMHltaHNoTlVjNGRUX1JWQThJREJRNVBTOEU3cjhVNy11ZlNQS3BfTTYxS0UzT0Y?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQMVZZOHhVRDM1clFBalVWZUVfTVk5TVkySkRfU3RWSU94QVVwd1FJR0RBWU54c3dlU21ubjd1dWIyT210alU0Y0tEazlibk55UFNnM2xtbmtGZDNKemRyRXRmNTVrTVdCckhwVk9fa05aNVlIcVhUY2J4S3dNMDhoZWRmbVlKT194ekZxNDBXbndRSlV1MXZlS01yRzZuTDBC?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPbGtmd09nQXp1OEF3ZWFtOFlyOVdPb2V5eERod0VCNVRrVHhDOUhCZzRGVzYwNVJLQTJMY2MwMlFzdU8tWWZEZ0RhZlBPMVJOUFdfQ1NaYmZvX2dOVGt3dllub3pobFNoRUZHalIwaWlxMDdwbmtLWVNVbXhBazBuUERfQ2xlZHRWNUJBeGhQUmhHdDg3N2wtRA?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQcWM4VjNtdFNvN2tuVTZ1S0pGeHprdFhxUE1BeElPSEYzeC13YjZoNWFiMmxndlBscWZvbWF5WW5DZ2czRGhpNXlnZWVxbUVpeGNITFZtMmVKTGFSaUh4RE5pWk90UGxlRzhOV0RSTE5aSmNkajdlNGcyTmNUTnA0R3Jfc2NxNWY3VF82cUVmLUJVbEw5aG90U1JyVWpEWDU4eUpR?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQNUdVWmxfZ2tQZ2VTaEtoaTRpSEVTS2pDVGQyYjc5azh2azFJSjBoRmlMakp4Rk5pUmZsTnpVRks3RjJQT09UVTkwMzNwT2xKaXp5WlMyTVZKUFZVZGMxZW5FLTZ4WGdIRWhEeXJvQVZQUHJ3bEZKVHdldmF6eHIwNFZJS21kM2Vxd203M0lKaVZhRUFIU1drc0lreWN4Z0xLZVRmc1ZlVDM?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPMmZ2Sk96akVIZjRudGdISnZjbENmNkEzT2dSMXE3QVpKS0VvYXlQUERrNTc5eWJTOWc1ZHRVWkpaU2d2azlMcFdQVHNEQ2ctWWprWnpOYlNRYzFPazNiNlVCZzBLdXFKWURYbng1bjRkVy1EZVVEa2F6UXQtblVlWDhtUjBNaW8wV1JFNXdaa0R6aEZIU0Jna09XdDVRYzN0bEE?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxPRDZDdktvQk03TFkxVHVUWlAwSGVmdXlPRDZYdVBjWmc1UUlIUFdFWTNPZzB2cW43VU5ySUlGT2ZubnRFTVJZaEo5R010eVhRSklyQkFwX2JBbG81a09ha01ENTA4X25uX0N6dmVBVWJSV09scDdfbHZCZm03cDRQbzZn?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNMWo3bzEzZFpCcXZaNlhBUUloaHVTdDAtN3lEeXBFSGJtNExXemtKNFBkUFFMLWFzWThDbzd4eGFrd3lfWVRuUi0xRnh0ZnlQQUhBOE9TUWRKVkxaVVl0bGZqTWV1c2ZOS0pXaDdNYTQ4U2NmQ0tuRlNiTmxoRzBiSmJyZ0hFVzNEbFJ3YzFSeVQ3TEE0aktPdHBPcWRZYVdNcngtWVlrRWV1S0hyYnc?oc=5

## Demo notes and limitations

- Multi-ticker local demo; AI items require human spot checks; RSS coverage is not guaranteed.
- Free-tier Gemini grounding (google_search tool) returned 429; the demo uses Google News RSS + plain-text AI extraction.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
