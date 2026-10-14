"""Pin the shared snapshot schema so email producers cannot silently drift."""
import importlib
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))


@pytest.fixture
def contract():
    return importlib.import_module('snapshot_contract')


def test_frozen_schema(contract):
    assert contract.CONTRACT_VERSION == '1.0'
    assert contract.REQUIRED_TOP_LEVEL == [
        'contract_version', 'identity', 'quant', 'ai_summary', 'freshness', 'disclaimer']
    assert contract.REQUIRED_IDENTITY == ['ticker', 'as_of', 'report_stamp']
    assert contract.REQUIRED_FRESHNESS == [
        'report_as_of', 'market_data_as_of', 'market_data_fetched_at',
        'ai_snapshot_as_of', 'snapshot_note', 'assumptions_version',
        'assumptions_checked', 'no_refresh_note']
