"""Offline contracts and report preflight regression coverage."""
from pathlib import Path
import json
import runpy
import sys

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import data_utils
from assumptions import REGISTRY, AssumptionViolation, check_all


IDS = {'prices-adjusted-close', 'prices-lookback-start', 'stooq-us-only',
       'prices-normalized-index', 'prices-trading-calendar', 'prices-currency-usd',
       'prices-minimum-history', 'phase1-artifacts-exist', 'fred-shared-freshness',
       'supported-ticker', 'report-as-of-date'}


def test_registry_and_missing_evidence():
    assert {a.id for a in REGISTRY} == IDS
    assert len(REGISTRY) == len(IDS)
    assert all(a.statement and a.why for a in REGISTRY)
    assert all(r['status'] == 'uncheckable' for r in check_all({}))


def test_pass_recorded():
    results = check_all({'ticker': 'CSCO', 'price_count': 1,
                         'price_index': pd.date_range('2020-01-01', periods=1)})
    assert {r['id']: r['status'] for r in results}['prices-minimum-history'] == 'ok'


@pytest.mark.parametrize('context, assumption, observation', [
    ({'price_count': 0}, 'prices-minimum-history', '0'),
    ({'ticker': 'UNKNOWN'}, 'supported-ticker', 'UNKNOWN'),
    ({'as_of': '2026-02-30'}, 'report-as-of-date', '2026-02-30'),
    ({'as_of': '9999-01-01'}, 'report-as-of-date', '9999-01-01'),
    ({'stooq_symbols': ['CNQ.TO']}, 'stooq-us-only', 'CNQ.TO'),
    ({'price_index': pd.date_range('2020-01-01', periods=1, tz='UTC')},
     'prices-normalized-index', 'UTC'),
])
def test_violation_is_actionable(context, assumption, observation):
    with pytest.raises(AssumptionViolation) as caught:
        check_all(context)
    message = str(caught.value)
    assert assumption in message and observation in message
    row = next(r for r in caught.value.results if r['id'] == assumption)
    assert row['status'] == 'violated'
    assert next(a.why for a in REGISTRY if a.id == assumption) in message


@pytest.mark.parametrize('missing', [False, True])
def test_report_preflight(monkeypatch, tmp_path, capsys, missing):
    monkeypatch.setattr(data_utils, 'DATA', tmp_path)
    monkeypatch.setattr(data_utils, 'REPORTS', tmp_path)
    monkeypatch.setattr(data_utils, 'ticker_arg', lambda: 'CSCO')
    monkeypatch.setenv('REPORT_AS_OF', '2020-01-01')
    fixtures = {
        'quant.json': {'metrics': {}}, 'info.json': {}, 'rss-items.json': [],
        'ai-intel.json': {k: [] for k in ('tailwinds', 'headwinds', 'catalysts', 'risks')},
        'comparables.json': {'peers': [], 'as_of': '2020-01-01'},
        'earnings.json': {'last_earnings': None, 'next_earnings': None},
        'edgar.json': {'latest_filing': None, 'revenue': None, 'net_income': None},
        'fred.json': {'available': False},
    }
    for name, content in fixtures.items():
        path = tmp_path / (name if name == 'fred.json' else 'csco-' + name)
        path.write_text(json.dumps(content))
    if missing:
        (tmp_path / 'fred.json').unlink()
    script = Path(data_utils.__file__).with_name('regenerate_report.py')
    if missing:
        with pytest.raises(SystemExit) as caught:
            runpy.run_path(str(script), run_name='__main__')
        assert caught.value.code == 2
        assert 'fred.json' in capsys.readouterr().err
        assert not (tmp_path / 'CSCO-intelligence-20200101.md').exists()
    else:
        runpy.run_path(str(script), run_name='__main__')
        assert (tmp_path / 'CSCO-intelligence-20200101.md').exists()
    metadata = json.loads((tmp_path / 'CSCO-intelligence-20200101.json').read_text())
    assert metadata['assumptions_version'] == 1
    assert metadata['assumptions_checked']['phase1-artifacts-exist']['status'] == (
        'violated' if missing else 'ok')
