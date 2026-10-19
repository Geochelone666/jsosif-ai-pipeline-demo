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
