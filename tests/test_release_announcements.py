from copy import deepcopy
from datetime import datetime, timezone
import json

import pytest

import release_announcements as releases
from prepare_delivery_store import load_ledger

NOW = datetime(2026,10,19,14,tzinfo=timezone.utc)


def record(**changes):
    return dict({'id':'research-v2','version':'2.0','title':'Research update',
        'summary':['Reviewed research improvements.'],'kind':'feature','status':'published',
        'audience':{'groups':[],'tickers':[]},'url':releases.SITE+'whats-new.html',
        'deployed_at':'2026-10-18T10:00:00Z','verified_at':'2026-10-18T11:00:00Z',
        'evidence_url':'https://github.com/Geochelone666/jsosif-ai-pipeline-demo/actions/runs/123'}, **changes)


def catalog(tmp_path, items):
    p=tmp_path/'releases.json'
    p.write_text(json.dumps({'schema_version':1,'releases':items}))
    return p


@pytest.mark.parametrize('change',[
    {'url':'https://evil.example/updates'}, {'url':releases.SITE+'../private'},
    {'evidence_url':'https://example.com/pretend-success'},
    {'verified_at':'2026-10-17T00:00:00Z'}, {'verified_at':'2026-10-18T11:00:00'},
    {'summary':['a','b','c']}, {'audience':{'emails':['one@example.com']}},
])
def test_invalid_release_cannot_be_published(tmp_path, change):
    with pytest.raises(ValueError): releases.load(catalog(tmp_path,[record(**change)]))


def test_duplicate_ids_rejected(tmp_path):
    with pytest.raises(ValueError): releases.load(catalog(tmp_path,[record(),record()]))


def test_draft_withdrawn_and_future_records_stay_unpublished(tmp_path):
    items=[record(id='draft',status='draft'),record(id='withdrawn',status='withdrawn'),
           record(id='future',deployed_at='2026-11-01T00:00:00Z',verified_at='2026-11-01T01:00:00Z')]
    valid=releases.load(catalog(tmp_path,items))
    assert releases.published(valid,NOW)==[]
    assert 'No verified release announcements yet.' in releases.page(valid,NOW)


def test_relevance_and_maximum_two_updates():
    member={'id':'one','groups':['tech']}
    items=[record(id='irrelevant',audience={'groups':['energy'],'tickers':['V']}),
           record(id='minor',kind='maintenance'),record(id='stock',audience={'groups':[],'tickers':['CSCO']}),
           record(id='team',audience={'groups':['tech'],'tickers':[]}),record(id='all')]
    picked=releases.select(items,member,['CSCO'],{},NOW)
    assert {r['id'] for r in picked}=={'team','stock'}


@pytest.mark.parametrize('status',['accepted','sending','unknown'])
def test_accepted_or_uncertain_announcements_are_not_repeated_in_later_weeks(status):
    member={'id':'one','groups':[]}
    ledger={'old-week':{'status':status,'announcements':['research-v2'],
                        'announcement_recipient':releases.recipient_key('one')}}
    assert releases.select([record()],member,['CSCO'],ledger,NOW)==[]
    assert len(releases.select([record()],dict(member,id='two'),['CSCO'],ledger,NOW))==1


def test_page_escapes_content_and_does_not_publish_audience():
    item=record(title='<script>unsafe</script>', audience={'groups':['private-team'],'tickers':[]})
    html=releases.page([item],NOW)
    assert '<script>' not in html and '&lt;script&gt;' in html
    assert 'private-team' not in html


@pytest.mark.parametrize('bad', [False,True])
def test_ledger_validates_optional_announcement_metadata(tmp_path,bad):
    entry={'period':'2026-10-19','status':'accepted','reports':['run/CSCO'],
           'updated_at':NOW.isoformat(),'announcements':['research-v2'],
           'announcement_recipient':releases.recipient_key('one')}
    if bad: entry['announcement_recipient']='one@example.com'
    (tmp_path/'state').mkdir()
    (tmp_path/'state/deliveries.json').write_text(json.dumps({'a'*64:entry}))
    if bad:
        with pytest.raises(ValueError): load_ledger(tmp_path,require_manifest=False)
    else: assert load_ledger(tmp_path,require_manifest=False)['a'*64]==entry
