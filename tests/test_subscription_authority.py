"""Authoritative subscriptions fail closed without falling back to stale secrets."""
from copy import deepcopy
from datetime import datetime, timezone
import io
import json

import pytest

import subscription_authority as authority
import prepare_subscriptions
from report_store import read_json

NOW = datetime(2026, 11, 3, 15, tzinfo=timezone.utc)


@pytest.fixture
def envelope(monkeypatch):
    monkeypatch.setenv('SUBSCRIPTIONS_SUPABASE_URL', 'https://team-example.supabase.co')
    monkeypatch.setenv('SUBSCRIPTIONS_SERVICE_KEY', 'synthetic-server-key')
    return {'schema_version': 1, 'revision': '9', 'generated_at': NOW.isoformat(),
            'config': {'groups': {}, 'members': [{'id': 'legacy-member', 'name': 'Example',
                'email': 'one@example.com', 'enabled': True, 'timezone': 'America/Toronto',
                'send_weekday': 1, 'send_time': '09:00', 'groups': [], 'tickers': ['CSCO']}]}}


def fetch(envelope):
    def opener(request, timeout):
        assert request.full_url == 'https://team-example.supabase.co/rest/v1/rpc/subscription_snapshot'
        assert request.get_header('Authorization') == 'Bearer synthetic-server-key'
        assert request.get_method() == 'POST' and timeout == 20
        return io.BytesIO(json.dumps(envelope).encode())
    return authority.fetch_snapshot(opener=opener, now=NOW)


def test_snapshot_preserves_delivery_identity_and_private_file(envelope, monkeypatch, tmp_path):
    config = fetch(envelope)
    monkeypatch.setenv('SUBSCRIPTIONS_BACKEND', 'supabase')
    monkeypatch.setenv('SUBSCRIPTIONS_JSON', 'stale invalid legacy config')
    monkeypatch.setenv('MEMBERS_CSV', 'also ignored')
    monkeypatch.setattr(authority, 'fetch_snapshot', lambda: config)
    target = tmp_path / 'subscriptions.json'
    assert prepare_subscriptions.prepare(target)
    assert read_json(target)['members'][0]['id'] == 'legacy-member'
    assert target.stat().st_mode & 0o777 == 0o600
    assert 'synthetic-server-key' not in target.read_text()


@pytest.mark.parametrize('change', ['stale','future','naive','bad_revision','unknown_schema','bad_member'])
def test_reject_invalid_or_stale_snapshot(envelope, change):
    if change == 'stale': envelope['generated_at'] = '2026-11-02T15:00:00+00:00'
    elif change == 'future': envelope['generated_at'] = '2026-11-04T15:00:00+00:00'
    elif change == 'naive': envelope['generated_at'] = '2026-11-03T15:00:00'
    elif change == 'bad_revision': envelope['revision'] = 9
    elif change == 'unknown_schema': envelope['schema_version'] = 2
    else: envelope['config']['members'][0]['email'] = 'invalid'
    with pytest.raises(ValueError, match='snapshot invalid'):
        fetch(envelope)


def test_remote_failure_never_falls_back_to_valid_legacy(envelope, monkeypatch, tmp_path):
    monkeypatch.setenv('SUBSCRIPTIONS_BACKEND','supabase')
    monkeypatch.setenv('SUBSCRIPTIONS_JSON',json.dumps(envelope['config']))
    def fail(): raise ValueError('Authority unavailable')
    monkeypatch.setattr(authority,'fetch_snapshot',fail)
    target = tmp_path / 'subscriptions.json'
    with pytest.raises(ValueError): prepare_subscriptions.prepare(target)
    assert not target.exists()


@pytest.mark.parametrize('change',['pause','email','revision','local_edit'])
def test_sender_blocks_changed_configuration(envelope, monkeypatch, change):
    frozen = fetch(envelope)
    next_value = deepcopy(envelope)
    if change == 'pause': next_value['config']['members'][0]['enabled'] = False
    elif change == 'email': next_value['config']['members'][0]['email'] = 'verified-new@example.com'
    elif change == 'revision': next_value['revision'] = '10'
    else: frozen['members'][0]['enabled'] = False
    current = fetch(next_value)
    monkeypatch.setattr(authority,'fetch_snapshot',lambda: current)
    with pytest.raises(ValueError): authority.assert_current(frozen)


def test_unchanged_snapshot_allows_reservation(envelope,monkeypatch):
    config = fetch(envelope)
    monkeypatch.setattr(authority,'fetch_snapshot',lambda: config)
    authority.assert_current(config)


def test_server_errors_are_sanitized(envelope):
    def fail(*args,**kwargs): raise OSError('synthetic-server-key one@example.com')
    with pytest.raises(ValueError) as error: authority.fetch_snapshot(opener=fail, now=NOW)
    assert 'synthetic-server-key' not in str(error.value) and 'one@example.com' not in str(error.value)


def test_supabase_mode_refuses_unversioned_config(monkeypatch):
    monkeypatch.setenv('SUBSCRIPTIONS_BACKEND','supabase')
    with pytest.raises(ValueError,match='authoritative'): authority.assert_current({})
