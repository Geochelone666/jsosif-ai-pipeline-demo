import pytest

from finalize_refresh import finalize
from report_store import read_json, write_json


def store(root):
    value = {'reports': [{'report_id': 'preserved'}], 'last_attempt': {
        'workflow_run_id': '123', 'business_date': '2026-10-21', 'status': 'running',
        'expected_tickers': ['CSCO', 'JPM'], 'successful_tickers': ['CSCO']}}
    write_json(root / 'index.json', value)
    return value


@pytest.mark.parametrize('outcome', ['failure', 'cancelled'])
def test_aborted_collector_retains_reports_and_records_interruption(tmp_path, outcome):
    before = store(tmp_path)
    result = finalize(tmp_path, business_date='2026-10-21', workflow_run_id='123', outcome=outcome)
    saved = read_json(tmp_path / 'index.json')
    assert result == {'publish': True, 'status': 'interrupted'}
    assert saved['reports'] == before['reports']
    assert saved['last_attempt']['pending_tickers'] == ['JPM']
    assert saved['last_attempt']['interruption_reason'] == 'collector_' + outcome


def test_a_failed_initialization_cannot_relabel_a_previous_run(tmp_path):
    before = store(tmp_path)
    assert not finalize(tmp_path, business_date='2026-10-21', workflow_run_id='999', outcome='failure')['publish']
    assert read_json(tmp_path / 'index.json') == before


def test_finalize_does_not_overwrite_a_completed_outcome(tmp_path):
    value = store(tmp_path); value['last_attempt']['status'] = 'complete'
    write_json(tmp_path / 'index.json', value)
    assert finalize(tmp_path, business_date='2026-10-21', workflow_run_id='123', outcome='success')['status'] == 'complete'
    assert read_json(tmp_path / 'index.json') == value
