"""Live launch checks using repository credentials; never submit an email message."""
import argparse
from datetime import datetime, timedelta
import json
import os
import re
from pathlib import Path
import smtplib
import ssl
from tempfile import TemporaryDirectory
from zoneinfo import ZoneInfo


def ai():
    from probe_ai import probe
    return probe()


def market():
    from price_fetch import fetch_symbol_prices
    today = datetime.now(ZoneInfo('America/Toronto')).date()
    with TemporaryDirectory() as directory:
        prices, statuses = fetch_symbol_prices('CSCO', (today - timedelta(days=30)).isoformat(),
                                                today.isoformat(), (today + timedelta(days=1)).isoformat(),
                                                Path(directory), max_attempts=1)
    if prices is None or len(prices) < 3:
        raise ValueError('Market source has insufficient price history')
    return {'provider': statuses[-1]['source'], 'observations': len(prices),
            'market_as_of': prices.index[-1].date().isoformat()}


def news():
    from ai_extract import fetch_rss
    items, status = fetch_rss('Cisco', n=5, max_attempts=1, window_days=7,
                             as_of=datetime.now(ZoneInfo('America/Toronto')).date().isoformat())
    if status['status'] != 'ok':
        raise ValueError('News source is unavailable')
    return {'source': 'Google News RSS', 'headlines': len(items)}


def sec():
    from edgar import fetch
    records = fetch('https://www.sec.gov/files/company_tickers.json')
    if not isinstance(records, dict) or not any(row.get('ticker') == 'CSCO' for row in records.values()):
        raise ValueError('SEC response did not contain the expected company')
    return {'source': 'SEC company ticker directory'}


def mail():
    from email_delivery import GmailSmtpBackend
    address, password = GmailSmtpBackend().credentials()
    # Login verifies STARTTLS and authentication; there is intentionally no MAIL,
    # RCPT, DATA or send_message call in this check.
    with smtplib.SMTP('smtp.gmail.com', 587, timeout=60) as smtp:
        smtp.starttls(context=ssl.create_default_context())
        smtp.login(address, password)
    return {'transport': 'Gmail STARTTLS', 'authentication': 'verified', 'messages_sent': 0}


def automation():
    if any(os.environ.get(name, '').lower() != 'true'
           for name in ('PAGES_DEPLOY_ENABLED', 'EMAIL_DELIVERY_ENABLED')):
        raise ValueError('The production automation switches are not enabled')
    return {'daily_publication': 'enabled', 'weekly_delivery': 'enabled'}


def expected_business_date(now=None):
    local = (now or datetime.now(ZoneInfo('America/Toronto'))).astimezone(ZoneInfo('America/Toronto'))
    return (local.date() - timedelta(days=local.hour < 19)).isoformat()


def run(*, site_url, business_date, checks=None, allow_newer_site=False):
    from check_site import check
    checks = checks if checks is not None else {
        'ai': ai, 'market': market, 'news': news, 'sec': sec, 'mail_authentication': mail,
        'automation': automation,
        'deployed_site': lambda: check(site_url, business_date=business_date, require_ready=True,
                                      allow_newer=allow_newer_site)}
    results = {}
    hints = {'ai': 'Check the Groq Secret, model access and account quotas.',
             'market': 'Check Yahoo/Stooq access and price availability.',
             'news': 'Check Google News RSS access.',
             'sec': 'Check SEC_USER_AGENT and SEC endpoint access.',
             'mail_authentication': 'Check Gmail credentials, App Password and SMTP access.',
             'automation': 'Review existing roster and test results, then enable PAGES_DEPLOY_ENABLED and EMAIL_DELIVERY_ENABLED.',
             'deployed_site': 'Run the daily pipeline with Pages enabled and verify the expected date.'}
    for name, function in checks.items():
        try:
            details = function()
            results[name] = {'status': 'verified', 'details': details}
        except Exception as exc:
            # Provider/SMTP exception strings can contain credentials or addresses.
            results[name] = {'status': 'blocked', 'category': type(exc).__name__}
            code = getattr(exc, 'smtp_code', getattr(exc, 'code', None))
            if type(code) is int:
                results[name]['service_status'] = code
            # Extract only the numeric status from the client's fixed safe error.
            if name == 'ai':
                from groq_provider import GroqError
                if isinstance(exc, GroqError):
                    if exc.provider_code:
                        results[name]['provider_code'] = exc.provider_code
                    if exc.provider_code == 'model_not_found':
                        from groq_provider import available_models
                        try:
                            results[name]['available_models'] = available_models()
                        except Exception:
                            results[name]['model_discovery'] = 'unavailable'
                    match = re.fullmatch(r'Groq HTTP (\d{3}); check account limits and retry guidance', str(exc))
                    if match:
                        results[name]['service_status'] = int(match.group(1))
                    elif str(exc) == 'Groq API key is not configured':
                        results[name]['reason'] = 'missing_credentials'
            if name == 'automation':
                results[name]['switches'] = {key: os.environ.get(key, '').lower() == 'true'
                                            for key in ('PAGES_DEPLOY_ENABLED', 'EMAIL_DELIVERY_ENABLED')}
            if name in hints:
                results[name]['hint'] = hints[name]
    return {'ready_for_roster': bool(results) and all(r['status'] == 'verified' for r in results.values()),
            'business_date': business_date, 'checks': results, 'member_roster': 'not required for these checks',
            'messages_sent': 0}


def publish_ci_results(report):
    """Expose sanitized check states without requiring access to zipped run logs."""
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        return
    rows = ['# Live launch acceptance', '', '| Check | Result |', '| --- | --- |']
    for name, result in report['checks'].items():
        # Details may contain provider text; only status diagnostics enter annotations.
        safe = {key: result[key] for key in ('status', 'category', 'service_status', 'provider_code', 'available_models', 'model_discovery', 'reason', 'switches', 'hint')
                if key in result}
        message = json.dumps({'check': name, **safe}, sort_keys=True)
        escaped = message.replace('%', '%25').replace('\r', '%0D').replace('\n', '%0A')
        print('::notice title=Live acceptance::' + escaped)
        rows.append('| ' + name.replace('|', '\\|').replace('\n', ' ') + ' | ' + result['status'] + ' |')
    rows += ['', 'Messages sent: 0', '']
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as stream:
            stream.write('\n'.join(rows))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site-url', required=True)
    parser.add_argument('--business-date', help='Exact report date; defaults to the latest expected evening publication')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = run(site_url=args.site_url, business_date=args.business_date or expected_business_date(),
                 allow_newer_site=args.business_date is None)
    text = json.dumps(report, indent=2)
    print(text)
    publish_ci_results(report)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + '\n', encoding='utf-8')
    if not report['ready_for_roster']:
        raise SystemExit('Live acceptance has blocked checks; inspect credential, source and deployment configuration')


if __name__ == '__main__':
    main()
