"""Reject stale or inconsistent source evidence before labeling a report ready."""
from copy import deepcopy
import json

import pytest

from freeze_report import freeze


@pytest.fixture
def report(tmp_path):
    path = tmp_path / 'CSCO-intelligence-20261019.md'
    path.write_text('''# CSCO
- ticker: **CSCO**
- Report as_of: **2026-10-19**
- Market data as_of: **2026-10-19**
- AI analysis snapshot as_of: **2026-10-19**
- AI status: **Available**
## QUANTITATIVE
| Metric | Value |
|---|---:|
| Close | 100.0000 |
''')
    path.with_suffix('.json').write_text(json.dumps({'ticker': 'CSCO', 'as_of': '2026-10-19'}))
    quant = {'ticker': 'CSCO', 'as_of': '2026-10-19', 'metrics': {'Close': 100}}
    ai = {'ticker': 'CSCO', 'as_of': '2026-10-19',
          'extraction_stats': {'unique_headlines': 1, 'rule': 1, 'ai': 0, 'unknown': 0}}
    return path, quant, ai


def test_matching_sources_are_ready(report):
    assert freeze(*report)['quality'] == 'ready'


@pytest.mark.parametrize('field,value', [
    ('as_of', '2026-10-20'), ('as_of', '2026-10-14'), ('as_of', 'bad-date'),
    ('as_of', None), ('close', float('nan')), ('close', float('inf')),
    ('close', True), ('close', -1),
])
def test_invalid_market_evidence_is_not_ready(report, field, value):
    path, quant, ai = report
    if field == 'close':
        quant['metrics']['Close'] = value
    else:
        quant[field] = value
    payload = freeze(path, quant, ai)
    assert payload['quality'] == 'degraded'
    assert payload['source_status']['market'] == 'failed'


@pytest.mark.parametrize('changes', [
    {'as_of': '2026-10-03'}, {'as_of': '2026-10-20'}, {'as_of': None},
    {'ticker': 'JPM'}, {'fetch_status': {'status': 'failed'}},
    {'extraction_stats': {'unique_headlines': 2, 'rule': 1, 'ai': 0, 'unknown': 1}},
])
def test_invalid_news_evidence_is_not_ready(report, changes):
    path, quant, ai = report
    ai.update(deepcopy(changes))
    assert freeze(path, quant, ai)['source_status']['news'] == 'degraded'


def test_successful_empty_news_query_is_a_quiet_day_not_an_outage(report):
    path, quant, ai = report
    ai.update(fetch_status={'status': 'ok'}, extraction_stats={'unique_headlines': 0, 'rule': 0, 'ai': 0, 'unknown': 0})
    assert freeze(path, quant, ai)['quality'] == 'ready'
    ai['fetch_status']['status'] = 'failed'
    assert freeze(path, quant, ai)['quality'] == 'degraded'


def test_empty_news_without_successful_fetch_evidence_is_not_ready(report):
    path, quant, ai = report
    ai['extraction_stats'] = {'unique_headlines': 0, 'rule': 0, 'ai': 0, 'unknown': 0}
    assert freeze(path, quant, ai)['quality'] == 'degraded'


def test_partial_ai_classification_cannot_pass_strict_news_gate(report):
    path, quant, ai = report
    ai['extraction_stats'] = {
        'unique_headlines': 3, 'rule': 1, 'ai': 1, 'unknown': 1,
    }
    payload = freeze(path, quant, ai)
    assert payload['quality'] == 'degraded'
    assert payload['source_status']['news'] == 'degraded'
    assert payload['source_evidence']['news']['coverage_pct'] == pytest.approx(66.67)
    assert payload['source_evidence']['news']['count_reconciled']


def test_reconciled_irrelevant_news_counts_as_reviewed(report):
    path, quant, ai = report
    ai['extraction_stats'] = {
        'unique_headlines': 3, 'rule': 1, 'ai': 1, 'irrelevant': 1, 'unknown': 0,
    }
    payload = freeze(path, quant, ai)
    assert payload['quality'] == 'ready'
    assert payload['source_evidence']['news']['coverage_pct'] == 100
    assert payload['source_evidence']['news']['resolved_headlines'] == 3


@pytest.mark.parametrize('stats', [
    {'unique_headlines': 2, 'rule': 1, 'ai': 0, 'unknown': 0},
    {'unique_headlines': 1, 'rule': 1, 'ai': 0, 'unknown': 0, 'irrelevant': 1},
    {'unique_headlines': 1, 'rule': True, 'ai': 0, 'unknown': 0},
    {'unique_headlines': 1, 'rule': -1, 'ai': 1, 'unknown': 1},
    {},
    None,
])
def test_malformed_or_unreconciled_evidence_stays_degraded(report, stats):
    path, quant, ai = report
    ai['extraction_stats'] = stats
    payload = freeze(path, quant, ai)
    assert payload['quality'] == 'degraded'
    assert not payload['source_evidence']['news']['count_reconciled']
