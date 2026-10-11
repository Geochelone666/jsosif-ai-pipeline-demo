"""Versioned pipeline contracts; missing evidence is never counted as a pass."""
from dataclasses import dataclass
from datetime import date
from pathlib import Path
import re
from typing import Callable

from universe import SUPPORTED

VERSION = 1
PRICE_START = '2025-10-02'
MIN_PRICE_OBSERVATIONS = 1  # Short histories retain Close; other metrics may be N/A.
REQUIRED_ARTIFACTS = ('quant.json', 'info.json', 'ai-intel.json', 'rss-items.json',
                      'comparables.json', 'earnings.json', 'edgar.json', 'fred.json')


@dataclass(frozen=True)
class Assumption:
    id: str
    statement: str
    why: str
    key: str = ''
    predicate: Callable | None = None


def valid_date(value):
    try:
        return (isinstance(value, str) and
                re.fullmatch(r'\d{4}-\d{2}-\d{2}', value) is not None and
                date.fromisoformat(value) <= date.today())
    except ValueError:
        return False


def normalized_index(index):
    return index.tz is None and index.equals(index.normalize())


REGISTRY = (
    Assumption('prices-adjusted-close',
               'Yahoo auto_adjust=True prices are assumed split/dividend-adjusted; post-hoc adjustments may be revised.',
               'Returns depend on provider adjustments; flags cannot verify their correctness.'),
    Assumption('prices-lookback-start',
               f'The nominal one-year lookback starts at fixed {PRICE_START}, not a rolling date.',
               'Earlier report dates or newer runs may lack the intended one-year coverage.',
               'price_start', lambda value: value == PRICE_START),
    Assumption('stooq-us-only',
               'US Stooq fallback is only used for symbols without a dot; a dot denotes an international listing.',
               'A US fallback can otherwise select the wrong listing.',
               'stooq_symbols', lambda symbols: all('.' not in s for s in symbols)),
    Assumption('prices-normalized-index',
               'Price indices are timezone-naive and normalized to midnight.',
               'Date slicing and benchmark alignment require consistent daily labels.',
               'price_index', normalized_index),
    Assumption('prices-trading-calendar',
               'Trading calendar completeness is assumed; missing days are silently absent and gaps are not detected.',
               'Observation counts do not establish continuous trading-day coverage.'),
    Assumption('prices-currency-usd',
               'Prices are assumed USD; yfinance and Stooq rows have no currency check.',
               'International listings may use local currency, affecting USD labels and comparisons.'),
    Assumption('prices-minimum-history',
               f'At least {MIN_PRICE_OBSERVATIONS} usable positive, finite ticker close is required.',
               'Without a usable close the quant snapshot has no price evidence; short histories still produce N/A metrics.',
               'price_count', lambda count: count >= MIN_PRICE_OBSERVATIONS),
    Assumption('phase1-artifacts-exist',
               'Required phase-1 artifacts must exist in data/ before report assembly and validation.',
               'Missing inputs prevent a complete report; existence does not establish schema validity or freshness.',
               'required_paths', lambda paths: all(Path(p).is_file() for p in paths)),
    Assumption('fred-shared-freshness',
               'The shared data/fred.json snapshot is reused across tickers; freshness is assumed acceptable without a staleness bound.',
               'A report date does not imply current macro observations.'),
    Assumption('supported-ticker',
               'Only tickers in universe.SUPPORTED are processable.',
               'Unsupported symbols have no configured pipeline universe entry.',
               'ticker', lambda ticker: ticker in SUPPORTED),
    Assumption('report-as-of-date',
               'REPORT_AS_OF must be a real calendar date in YYYY-MM-DD and not in the future.',
               'Invalid dates make snapshot selection unreliable.',
               'as_of', valid_date),
)


class AssumptionViolation(ValueError):
    """Carries every check result so callers can persist failures before exiting."""

    def __init__(self, results):
        self.results = results
        super().__init__('; '.join(
            f"Assumption {r['id']} violated: {r['statement']} {r['detail']}"
            for r in results if r['status'] == 'violated'))


def check_all(context):
    """Return all results, or raise AssumptionViolation with .results on failure.

    Context keys correspond to registry keys. Omitted keys and predicates without
    evidence are uncheckable. price_count counts cleaned ticker closes (not SPY).
    """
    results = []
    for assumption in REGISTRY:
        status, detail = 'uncheckable', assumption.why
        if assumption.predicate is not None and assumption.key in context:
            value = context[assumption.key]
            status = 'ok' if assumption.predicate(value) else 'violated'
            observed = repr(value)
            if assumption.key == 'required_paths':
                observed = 'missing files: ' + ', '.join(str(p) for p in value if not Path(p).is_file())
                if status == 'ok':
                    observed = 'all required files exist'
            elif assumption.key == 'price_index':
                observed = f'{len(value)} labels; timezone={value.tz}'
            detail = f'Observed {observed}. {assumption.why}'
        results.append(dict(id=assumption.id, statement=assumption.statement,
                            status=status, detail=detail))
    if any(r['status'] == 'violated' for r in results):
        raise AssumptionViolation(results)
    return results


def checked_mapping(results):
    return {r['id']: {'status': r['status'], 'detail': r['detail']} for r in results}


def required_paths(data, ticker):
    return [data / (name if name == 'fred.json' else f'{ticker.lower()}-{name}')
            for name in REQUIRED_ARTIFACTS]
