from copy import deepcopy
from datetime import datetime, timezone

import pytest

from deliver_weekly import due_period
from subscriptions import validate
from universe import SUPPORTED, COMPANIES, PILOT_COMPANIES
from comparables import PEERS


def member():
    return {'id': 'pilot', 'name': 'Pilot', 'email': 'pilot@example.com',
            'enabled': True, 'groups': ['sector'], 'tickers': [],
            'timezone': 'America/Toronto', 'send_weekday': 0,
            'send_time': '09:00', 'delivery_start_date': '2026-10-22'}


def test_new_member_does_not_receive_past_monday_mail_on_activation():
    m = member()
    assert due_period(m, datetime(2026, 10, 22, 14, tzinfo=timezone.utc)) is None
    assert due_period(m, datetime(2026, 10, 26, 12, 59, tzinfo=timezone.utc)) is None
    assert due_period(m, datetime(2026, 10, 26, 13, tzinfo=timezone.utc)) == '2026-10-26'
    # The exact local time stays 09:00 after DST ends.
    assert due_period(m, datetime(2026, 11, 2, 13, 59, tzinfo=timezone.utc)) is None
    assert due_period(m, datetime(2026, 11, 2, 14, tzinfo=timezone.utc)) == '2026-11-02'


def test_thursday_member_is_due_on_first_delivery_date():
    m = member(); m['send_weekday'] = 3
    assert due_period(m, datetime(2026, 10, 22, 12, 59, tzinfo=timezone.utc)) is None
    assert due_period(m, datetime(2026, 10, 22, 13, tzinfo=timezone.utc)) == '2026-10-19'


@pytest.mark.parametrize('bad', ['2026-02-30', 'tomorrow', '2026-1-1', None, 20261022])
def test_invalid_start_date_is_rejected(bad):
    m = member(); m['delivery_start_date'] = bad
    with pytest.raises(ValueError):
        validate({'groups': {'sector': {'tickers': ['CSCO']}}, 'members': [m]})


def test_requested_symbols_have_collection_metadata():
    assert len(SUPPORTED) == len(set(SUPPORTED))
    assert set(PILOT_COMPANIES) <= set(COMPANIES) & set(PEERS)
    assert all(len(PEERS[t]) == 3 for t in PILOT_COMPANIES)


def test_pilot_aliases_preserve_common_news_names():
    from ai_extract import ALIASES
    assert 'google' in ALIASES['GOOGL']
    assert 'azure' in ALIASES['MSFT']
    assert 'tsmc' in ALIASES['TSM']
