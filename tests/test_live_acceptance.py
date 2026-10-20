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


def test_provider_status_diagnostics_do_not_include_private_error_bodies():
    from groq_provider import GroqError
    def rejected():
        raise GroqError('Groq HTTP 401; check account limits and retry guidance')
    result = live.run(site_url='https://example.invalid', business_date='2026-10-19', checks={'ai': rejected})
    assert result['checks']['ai']['service_status'] == 401


def test_ci_annotations_are_sanitized_and_available_without_artifact_download(monkeypatch, tmp_path, capsys):
    summary = tmp_path / 'summary.md'
    monkeypatch.setenv('GITHUB_ACTIONS', 'true')
    monkeypatch.setenv('GITHUB_STEP_SUMMARY', str(summary))
    report = {'checks': {'ai': {'status': 'verified', 'details': 'synthetic-secret'},
                         'sec': {'status': 'blocked', 'service_status': 403, 'category': 'HTTPError'}}}
    live.publish_ci_results(report)
    output = capsys.readouterr().out
    assert output.count('::notice title=Live acceptance::') == 2
    assert '403' in output and 'synthetic-secret' not in output
    assert '| ai | verified |' in summary.read_text()
    assert 'synthetic-secret' not in summary.read_text()


def test_sec_contact_can_reuse_a_validated_sender_without_a_placeholder(monkeypatch):
    import edgar
    monkeypatch.delenv('SEC_USER_AGENT', raising=False)
    monkeypatch.setenv('GMAIL_USER', 'synthetic@example.com')
    assert edgar.request_identity() == 'JSOSIF Research contact synthetic@example.com'
    monkeypatch.setenv('GMAIL_USER', 'not an address')
    with pytest.raises(ValueError):
        edgar.request_identity()


@pytest.mark.parametrize('instant,expected', [('2026-10-20T14:00:00+00:00','2026-10-19'),
                                              ('2026-10-20T23:00:00+00:00','2026-10-20'),
                                              ('2026-12-03T00:00:00+00:00','2026-12-02')])
def test_morning_acceptance_checks_the_last_expected_toronto_publication(instant, expected):
    from datetime import datetime
    assert live.expected_business_date(datetime.fromisoformat(instant)) == expected
