"""Offline, network-free acceptance for a gated website subscription sync."""
import copy
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))

from portal_subscription_sync import OFFICIAL_EXPORT, fetch_export, merge, normalize_member

EXISTING = {'groups': {'energy': {'name': 'Energy', 'tickers': ['CNQ.TO']}},
            'members': [{
                'id': 'manual-1', 'name': 'Manual Analyst', 'email': 'manual@example.com',
                'groups': ['energy'], 'tickers': [], 'enabled': True,
                'timezone': 'America/Toronto', 'send_weekday': 0, 'send_time': '09:00'}]}


def portal(**changes):
    p = {'id': 'portal-abc', 'name': 'Portal Test', 'email': 'portal@example.com',
         'tickers': ['AAPL'], 'enabled': True, 'timezone': 'America/Toronto',
         'send_weekday': 1, 'send_time': '08:30'}
    p.update(changes)
    return p


def test_export_endpoint_is_exactly_allowlisted():
    with pytest.raises(ValueError, match='official HTTPS'):
        fetch_export('https://example.com/api/portal/export', 'secret')
    with pytest.raises(ValueError, match='official HTTPS'):
        fetch_export('http://www.jsosif.com/api/portal/export', 'secret')
    with pytest.raises(ValueError, match='official HTTPS'):
        fetch_export(OFFICIAL_EXPORT + '?next=evil', 'secret')


def test_export_has_no_follow_redirect_handler(monkeypatch):
    seen = {}
    class Response:
        status = 200
        def __enter__(self):
            return self
        def __exit__(self, *args):
            return False
        def read(self, n):
            assert n == 2_000_001
            return b'{"members":[]}'
    class Opener:
        def open(self, request, timeout):
            seen['token'] = request.get_header('X-portal-export-token')
            return Response()
    def fake_build_opener(handler):
        seen['handler'] = handler
        return Opener()
    monkeypatch.setattr('portal_subscription_sync.urllib.request.build_opener', fake_build_opener)
    assert fetch_export(OFFICIAL_EXPORT, 'stub-token')['members'] == []
    assert seen['token'] == 'stub-token'
    assert seen['handler'].redirect_request(None, None, 302, 'redirect', {}, 'https://evil.example') is None


def test_exact_origin_does_not_allow_missing_secret():
    with pytest.raises(ValueError, match='missing'):
        fetch_export(OFFICIAL_EXPORT, '')


def test_normalization_rejects_unsafe_and_wrong_types():
    with pytest.raises(ValueError, match='prefixed'):
        normalize_member(portal(id='manual-1'))
    with pytest.raises(ValueError, match='boolean'):
        normalize_member(portal(enabled='false'))
    with pytest.raises(ValueError, match='weekday'):
        normalize_member(portal(send_weekday=True))
    with pytest.raises(ValueError, match='tickers'):
        normalize_member(portal(tickers='AAPL'))


def test_normalization_tracks_unsupported_and_normalizes_case():
    member, count = normalize_member(portal(tickers=['aapl', 'AAPL', 'NOTREAL']), {'AAPL'})
    assert member['tickers'] == ['AAPL']
    assert member['groups'] == []
    assert count == 1


def test_manual_member_and_email_are_preserved():
    before = copy.deepcopy(EXISTING)
    merged, stats = merge(EXISTING, [portal()])
    assert EXISTING == before
    assert len(merged['members']) == 2
    assert merged['members'][0] == EXISTING['members'][0]
    assert stats == {'accepted': 1, 'pending': 0, 'unsupported_tickers': 0}


def test_manual_identity_collision_fails_closed():
    with pytest.raises(ValueError, match='privately managed'):
        merge(EXISTING, [portal(email='manual@example.com')])


def test_portal_can_only_update_its_own_stable_id():
    existing, _ = merge(EXISTING, [portal()])
    updated, _ = merge(existing, [portal(send_time='11:45')])
    assert len(updated['members']) == 2
    assert updated['members'][1]['send_time'] == '11:45'
    with pytest.raises(ValueError, match='identities conflict'):
        merge(existing, [portal(id='portal-other')])
    with pytest.raises(ValueError, match='different email'):
        merge(existing, [portal(email='other@example.com')])


def test_new_unsupported_ticker_waits_outside_active_roster():
    merged, stats = merge(EXISTING, [portal(tickers=['INVALID'])])
    assert merged['members'] == EXISTING['members']
    assert stats == {'accepted': 0, 'pending': 1, 'unsupported_tickers': 1}


def test_existing_portal_cannot_be_silently_left_on_old_ticker():
    existing, _ = merge(EXISTING, [portal()])
    with pytest.raises(ValueError, match='review required'):
        merge(existing, [portal(tickers=['INVALID'])])


def test_rejects_duplicate_portal_emails_and_bad_local_timezone():
    with pytest.raises(ValueError, match='Duplicate email'):
        merge(EXISTING, [portal(), portal(id='portal-other')])
    with pytest.raises(ValueError, match='time zone'):
        merge(EXISTING, [portal(timezone='Not/AZone')])


def test_invalid_export_schema_fails_without_creating_roster(monkeypatch):
    class Response:
        status = 200
        def __enter__(self): return self
        def __exit__(self, *a): return False
        def read(self, n): return b'{"member":[]}'
    class Opener:
        def open(self, request, timeout): return Response()
    monkeypatch.setattr('portal_subscription_sync.urllib.request.build_opener',
                        lambda handler: Opener())
    with pytest.raises(ValueError, match='members list'):
        fetch_export(OFFICIAL_EXPORT, 'stub-token')
