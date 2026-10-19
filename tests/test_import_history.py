"""Saved reports retain original contents and can never masquerade as fresh mail."""
from datetime import datetime, timezone

from build_site import build
from deliver_weekly import deliver
from import_history import import_history
from report_store import digest, read_json


def saved_report(tmp_path):
    reports = tmp_path / 'old-reports'
    reports.mkdir()
    source = reports / 'ACN-intelligence-20261008.md'
    source.write_text('''# ACN Intelligence Demo
- Report as_of: **2026-10-08**
- Market data as_of: **2026-10-07**
- AI analysis snapshot as_of: **2026-10-03** (retained)
- AI status: **Available**
## QUANTITATIVE
| Metric | Value |
|---|---:|
| Close | 12.3400 |
## TAILWINDS
Original saved headline.
Not investment advice.
''', encoding='utf-8')
    return reports, source


def test_existing_history_import_preserves_bytes_and_is_idempotent(tmp_path):
    reports, source = saved_report(tmp_path)
    store = tmp_path / 'store'
    now = datetime(2026, 10, 19, 14, tzinfo=timezone.utc)
    assert import_history(reports, store, now=now)['imported'] == 1
    assert import_history(reports, store, now=now)['already_archived'] == 1
    entry = read_json(store / 'index.json')['reports'][0]
    assert entry['as_of'] == '2026-10-08' and entry['quality'] == 'historical'
    assert (store / entry['md']).read_bytes() == source.read_bytes()
    assert digest(store / entry['md']) == entry['sha256']['md']
    assert (store / entry['pdf']).read_bytes().startswith(b'%PDF-')
    payload = read_json(store / entry['json'])
    assert payload['quant'][0]['value'] == '12.3400'
    assert payload['identity']['as_of'] == '2026-10-08'
    assert entry['imported_at'] == now.isoformat()
    build(store, tmp_path / 'site')
    assert (tmp_path / 'site' / entry['pdf']).is_file()
    assert (tmp_path / 'site/members.html').is_file()


def test_historical_import_is_never_a_weekly_delivery_even_when_degraded_is_allowed(tmp_path):
    reports, _ = saved_report(tmp_path)
    store = tmp_path / 'store'
    now = datetime(2026, 10, 19, 14, tzinfo=timezone.utc)
    import_history(reports, store, now=now)
    config = {'allow_degraded': True, 'max_report_age_days': 30,
              'groups': {'history': {'tickers': ['ACN']}},
              'members': [{'id': 'one', 'name': 'Example', 'email': 'example@example.com',
                           'enabled': True, 'groups': ['history'], 'timezone': 'America/Detroit',
                           'send_weekday': 0, 'send_time': '09:00'}]}
    sent = []
    assert deliver(config, store, now=now, really_send=True, backend=sent.append)['deferred'] == 1
    assert not sent
