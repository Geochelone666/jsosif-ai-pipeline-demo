"""Wrong-issuer history remains intact, visibly annotated and excluded from mail."""
from datetime import datetime, timezone
import json
from pathlib import Path

import pytest

from build_site import build
from check_release import check
import check_site
from deliver_weekly import deliver
from report_store import digest, read_json, report_advisory, write_json
from snapshot_emit import emit_frozen_snapshot


def version(root, run, cik):
    base = Path('archive') / run / 'MG.TO'
    entry = {'ticker': 'MG.TO', 'report_id': run + '/MG.TO', 'quality': 'ready',
             'as_of': '2026-10-19', 'generated_at': '2026-10-19T12:00:00+00:00'}
    snapshot = emit_frozen_snapshot(ticker='MG.TO', as_of=entry['as_of'],
                                   quant_metrics={'Close': 100}, ai={'status': 'Available'},
                                   freshness={}, disclaimer='Not investment advice.')
    snapshot['quality'] = 'ready'
    for kind, body in {'md': '# MG.TO\n', 'pdf': '%PDF-1.4 synthetic', 'json': json.dumps(snapshot)}.items():
        relative = base / ('MG.TO-intelligence-20261019.' + kind)
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body)
        entry[kind] = relative.as_posix()
    entry['sha256'] = {kind: digest(root / entry[kind]) for kind in ('md', 'pdf', 'json')}
    write_json(root / base / 'sources/mg.to-edgar.json', {'cik': cik})
    return entry


@pytest.mark.parametrize('cik,warning', [('1436126', True), ('749098', False), (None, False)])
def test_archived_source_identity_is_checked(tmp_path, cik, warning):
    entry = version(tmp_path, 'old', cik)
    assert bool(report_advisory(tmp_path, entry)) is warning


def test_correction_preserves_history_and_blocks_wrong_issuer_delivery(tmp_path, monkeypatch):
    store = tmp_path / 'store'
    old = version(store, 'old', '1436126')
    index = {'reports': [old], 'last_attempt': {'business_date': '2026-10-19', 'status': 'complete',
             'expected_tickers': ['MG.TO'], 'successful_tickers': ['MG.TO']}}
    write_json(store / 'index.json', index)
    config = {'groups': {}, 'members': [{'id': 'test', 'name': 'Synthetic Test',
        'email': 'test@example.com', 'tickers': ['MG.TO'], 'enabled': True,
        'timezone': 'America/Toronto', 'send_weekday': 0, 'send_time': '09:00'}]}
    now = datetime(2026, 10, 19, 14, tzinfo=timezone.utc)
    assert not check(store, require_ready=True)['ready']
    result = deliver(config, store, now=now)
    assert result['deferred'] == 1 and result['prepared'] == 0
    output = tmp_path / 'site'
    build(store, output)
    assert read_json(output / 'index.json')['reports'][0]['advisory']
    health = read_json(output / 'health.json')
    assert (health['ready'], health['degraded'], health['pending']) == (0, 1, 1)
    assert 'advisory' not in read_json(store / 'index.json')['reports'][0]
    monkeypatch.setattr(check_site, '_fetch', lambda base, relative: (output / relative).read_bytes())
    with pytest.raises(check_site.SiteError, match='incomplete source evidence'):
        check_site.check('https://example.com', business_date='2026-10-19', require_ready=True)

    corrected = version(store, 'corrected', '749098')
    corrected['generated_at'] = '2026-10-19T13:00:00+00:00'
    index['reports'].append(corrected)
    write_json(store / 'index.json', index)
    assert check(store, require_ready=True)['ready']
    assert deliver(config, store, now=now)['prepared'] == 1
    build(store, output)
    published = read_json(output / 'index.json')['reports']
    health = read_json(output / 'health.json')
    assert (health['updated'], health['ready'], health['degraded'], health['pending']) == (1, 1, 0, 0)
    assert published[0]['advisory'] and 'advisory' not in published[1]
    assert check_site.check('https://example.com', business_date='2026-10-19', require_ready=True)['status'] == 'verified'
    assert digest(store / old['pdf']) == old['sha256']['pdf']
    assert not (store / 'state/deliveries.json').exists()
