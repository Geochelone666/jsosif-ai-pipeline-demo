import json
import pytest
import check_integrations as live


def test_one_failed_integration_does_not_hide_other_checks_or_leak_exception_text():
    visited = []
    def bad():
        raise ValueError('synthetic-secret and member@example.com')
    def good():
        visited.append(True)
        return {'source': 'synthetic'}
    result = live.run(site_url='https://example.invalid', business_date='2026-10-19',
                      checks={'ai': bad, 'market': good})
    assert not result['ready_for_roster']
    assert result['checks']['market']['status'] == 'verified' and visited
    assert 'synthetic-secret' not in json.dumps(result)
    assert 'member@example.com' not in json.dumps(result)
    assert result['messages_sent'] == 0


def test_verified_integrations_do_not_require_or_publish_a_roster():
    result = live.run(site_url='https://example.invalid', business_date='2026-10-19',
                      checks={'synthetic': lambda: {'source': 'fixture'}})
    assert result['ready_for_roster'] and result['messages_sent'] == 0


def test_mail_check_authenticates_but_never_submits_a_message(monkeypatch):
    from email_delivery import GmailSmtpBackend
    operations = []
    monkeypatch.setattr(GmailSmtpBackend, 'credentials', lambda _: ('synthetic@example.com', 'synthetic-key'))
    class SMTP:
        def __init__(self, host, port, timeout):
            assert host == 'smtp.gmail.com' and port == 587 and timeout == 60
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass
        def starttls(self, context):
            assert context.verify_mode == live.ssl.CERT_REQUIRED
            operations.append('tls')
        def login(self, address, password):
            assert address == 'synthetic@example.com' and password == 'synthetic-key'
            operations.append('login')
        def send_message(self, *args, **kwargs):
            pytest.fail('The live launch check must not send mail')
    monkeypatch.setattr(live.smtplib, 'SMTP', SMTP)
    assert live.mail()['messages_sent'] == 0
    assert operations == ['tls', 'login']


@pytest.mark.parametrize('roster', ['', '{"groups": {}, "members": []}'])
def test_missing_or_empty_roster_leaves_delivery_idle_without_exposing_data(tmp_path, monkeypatch, roster):
    import prepare_subscriptions
    import sys
    output = tmp_path / 'outputs.txt'
    monkeypatch.setenv('SUBSCRIPTIONS_JSON', roster)
    monkeypatch.delenv('MEMBERS_CSV', raising=False)
    monkeypatch.setenv('GITHUB_OUTPUT', str(output))
    monkeypatch.setattr(sys, 'argv', ['prepare_subscriptions.py', str(tmp_path / 'private.json')])
    prepare_subscriptions.main()
    assert 'email_members=0' in output.read_text()
    assert ('configured=true' if roster else 'configured=false') in output.read_text()


def test_invalid_roster_does_not_enable_delivery(tmp_path, monkeypatch):
    import prepare_subscriptions
    import sys
    output = tmp_path / 'outputs.txt'
    monkeypatch.setenv('SUBSCRIPTIONS_JSON', '{"groups": {}, "members": [{"email": "synthetic@example.com"}]}')
    monkeypatch.delenv('MEMBERS_CSV', raising=False)
    monkeypatch.setenv('GITHUB_OUTPUT', str(output))
    monkeypatch.setattr(sys, 'argv', ['prepare_subscriptions.py', str(tmp_path / 'private.json')])
    with pytest.raises(SystemExit):
        prepare_subscriptions.main()
    assert not output.exists()


@pytest.mark.parametrize('pages,email,ready', [('true', 'true', True), ('true', '', False),
                                              ('false', 'true', False)])
def test_readiness_requires_automation_to_be_armed(pages, email, ready, monkeypatch):
    monkeypatch.setenv('PAGES_DEPLOY_ENABLED', pages)
    monkeypatch.setenv('EMAIL_DELIVERY_ENABLED', email)
    result = live.run(site_url='https://example.invalid', business_date='2026-10-19',
                      checks={'automation': live.automation})
    assert result['ready_for_roster'] is ready
    assert result['messages_sent'] == 0
