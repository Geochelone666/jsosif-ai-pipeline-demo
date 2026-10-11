# JSOSIF 25-Report Module Completeness Matrix

**As of:** 2026-10-08
**Reports:** `*-intelligence-20261008.md` (25 files)

## Completeness Matrix

| Ticker | QUANT | AI | PEERS | EARNINGS | EDGAR | NEWS | Score |
|--------|-------|----|-------|----------|-------|------|-------|
| ACN | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | 4/6 |
| AMTM | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | 5/6 |
| ATD.TO | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | 5/6 |
| BMO.TO | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | 4/6 |
| CNQ.TO | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | 4/6 |
| COST | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | 5/6 |
| CP.TO | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | 5/6 |
| CSCO | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | 5/6 |
| DIS | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | 5/6 |
| ENB | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | 4/6 |
| GIS | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | 4/6 |
| J | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | 4/6 |
| JPM | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | 5/6 |
| JWEL.TO | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | 5/6 |
| MC.PA | ✓ | ✓ | ✗ | ✗ | ✓ | ✓ | 4/6 |
| MG.TO | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | 5/6 |
| NTR.TO | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | 4/6 |
| NVO | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | 5/6 |
| OTEX.TO | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | 5/6 |
| PEP | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | 5/6 |
| PFE | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | 5/6 |
| SCHW | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | 5/6 |
| V | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | 4/6 |
| VRTX | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | 4/6 |
| XYL | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | 5/6 |

## Module Success Rates

| Module | Success | Rate | Notes |
|--------|---------|------|-------|
| QUANT | 24/25 | 96% | GIS missing P/E (N/A) |
| AI | 17/25 | 68% | 8 failures (code fixed, reports still have old snapshots) |
| PEERS | 0/25 | 0% | **All reports show only self, zero peer companies** |
| EARNINGS | 24/25 | 96% | MC.PA missing (N/A) |
| EDGAR | 25/25 | 100% | All have Form, filing date, revenue |
| NEWS | 25/25 | 100% | All have headlines (1-17 per report) |

## Key Findings

### Most Complete Tickers (5/6)
15 tickers achieve 5/6: AMTM, ATD.TO, COST, CP.TO, CSCO, DIS, JPM, JWEL.TO, MG.TO, NVO, OTEX.TO, PEP, PFE, SCHW, XYL

**No ticker achieves 6/6** due to the PEERS module being 0% across the board.

### Least Complete Tickers (4/6)
10 tickers at 4/6:
- ACN, BMO.TO, CNQ.TO, ENB, J, NTR.TO, V, VRTX (AI failure)
- GIS (AI ok, but QUANT missing P/E)
- MC.PA (AI ok, but EARNINGS missing)

### Critical Gap: PEERS Module (0%)
The PEER COMPARABLES section in all 25 reports contains only the ticker itself — **zero actual peer companies**. The comparables pipeline returned 0 rows. This is the biggest completeness gap.

### AI Module (68%)
8 reports have `AI unavailable` status. The code bugs were fixed (commit `abb5d77`) but the reports still carry the old failed snapshots. Re-running the pipeline would fix these.

### Data Quality Notes
- **GIS**: P/E is N/A (yfinance didn't return it)
- **MC.PA**: Earnings dates N/A (European ticker, yfinance calendar gaps)
- **NEWS**: Headline counts vary widely (ENB: 1, PEP: 17) — reflects RSS availability per ticker
