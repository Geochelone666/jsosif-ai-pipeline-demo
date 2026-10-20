from datetime import datetime, timezone
import pytest

import internal_email_check as internal


def test_internal_acceptance_uses_only_the_sender_and_five_approved_holdings():
    config = internal.self_config('synthetic@example.com', datetime(2026,10,20,14,tzinfo=timezone.utc))
    assert len(config['members']) == 1
    member = config['members'][0]
    assert member['email'] == 'synthetic@example.com' and member['id'] == 'internal-email-acceptance'
    assert member['tickers'] == ['CNQ.TO','CSCO','JPM','BMO.TO','COST']


def test_internal_test_cannot_send_without_its_explicit_confirmation(monkeypatch, tmp_path):
    monkeypatch.setenv('GMAIL_USER', 'synthetic@example.com')
    monkeypatch.delenv('INTERNAL_EMAIL_CONFIRM', raising=False)
    monkeypatch.setattr(internal, 'deliver', lambda *a, **kw: pytest.fail('No delivery without confirmation'))
    with pytest.raises(ValueError, match='SEND_ONE_TO_SELF'):
        internal.check(tmp_path / 'store', tmp_path / 'preview', send=True)


def test_preview_mode_cannot_turn_into_delivery_when_confirmation_is_present(monkeypatch, tmp_path):
    monkeypatch.setenv('GMAIL_USER', 'synthetic@example.com')
    monkeypatch.setenv('INTERNAL_EMAIL_CONFIRM', 'SEND_ONE_TO_SELF')
    calls = []
    def preview(*args, **kwargs):
        calls.append(kwargs)
        assert 'really_send' not in kwargs and kwargs['preview_all']
        return {'prepared':0,'deferred':0,'unknown':0,'skipped':1,'sent':0}
    monkeypatch.setattr(internal, 'deliver', preview)
    internal.check(tmp_path / 'store', tmp_path / 'preview')
    assert len(calls) == 1


def test_fallback_credentials_cannot_redirect_the_self_test_to_another_mailbox(monkeypatch, tmp_path):
    monkeypatch.setenv('GMAIL_USER', 'synthetic@example.com')
    monkeypatch.setenv('INTERNAL_EMAIL_CONFIRM', 'SEND_ONE_TO_SELF')
    monkeypatch.setattr(internal.GmailSmtpBackend, 'credentials', lambda _: ('different@example.com', 'synthetic'))
    monkeypatch.setattr(internal, 'deliver', lambda *a, **kw: pytest.fail('Sender mismatch must prevent delivery'))
    with pytest.raises(ValueError, match='configured sender itself'):
        internal.check(tmp_path / 'store', tmp_path / 'preview', send=True)
