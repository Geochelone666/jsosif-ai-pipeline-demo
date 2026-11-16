from copy import deepcopy
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import pytest

from report_store import digest,read_json,write_json
from shared_research_pack import build,canonical,coverage_markdown,validate_pack,digest as package_digest,Evidence,add_sec
from snapshot_emit import emit_frozen_snapshot

CAPTURE=Path(__file__).parent/'fixtures/boc_fxusdcad_20261102_20261106.json'


@pytest.fixture
def archive(tmp_path):
    root=tmp_path/'store';rows=[]
    for ticker in ('CSCO','JPM'):
        base=Path('archive/synthetic')/ticker
        entry={'ticker':ticker,'report_id':'synthetic/'+ticker,'as_of':'2026-11-06',
               'generated_at':'2026-11-07T01:00:00+00:00','quality':'ready'}
        snapshot=emit_frozen_snapshot(ticker=ticker,as_of=entry['as_of'],quant_metrics={'Close':100,'Return 1D (%)':0},
            ai={'status':'Available'},freshness={'market_data_as_of':'2026-11-06','market_data_fetched_at':'2026-11-06T22:00:00+00:00'},
            disclaimer='Synthetic research fixture')
        snapshot['quality']='ready'
        for kind in ('json','md','pdf'):
            relative=base/f'{ticker}-intelligence-20261106.{kind}';path=root/relative;path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text({'json':json.dumps(snapshot),'md':'Synthetic report','pdf':'%PDF-1.4 synthetic'}[kind]);entry[kind]=str(relative)
        entry['sha256']={k:digest(root/entry[k]) for k in ('json','md','pdf')}
        sources=root/base/'sources'
        write_json(sources/(ticker.lower()+'-info.json'),{'symbol':ticker,'currency':'USD','industry':'Software',
            'private':'private@example.com','api_key':'synthetic-secret'})
        write_json(sources/'fred.json',{'available':True,'indicators':[{'series_id':'UNRATE','value':0,'date':'2026-10-01'}],
            'api_key':'synthetic-secret','members':['private@example.com']})
        write_json(sources/(ticker.lower()+'-comparables.json'),{'as_of':'2026-11-06','peers':[
            {'ticker':t,'currency':'USD','pe':20,'mktcap':100,'ret_1y':0.2} for t in ('V','MA','AXP')]})
        write_json(sources/(ticker.lower()+'-edgar.json'),{'ticker':ticker,'cik':'123',
            'revenue':{'value':1000,'unit':'USD','period':'2026-07-01/2026-09-30'},
            'net_income':{'value':-5,'unit':'USD','period':'2026-07-01/2026-09-30'},
            'latest_filing':{'filing_date':'2026-11-05','url':'https://evil.invalid/?key=secret'}})
        rows.append(entry)
    write_json(root/'index.json',{'reports':rows,'private':'secret-index-value'})
    return root


def source_path(root,kind,ticker='CSCO'):
    entry=next(e for e in read_json(root/'index.json')['reports'] if e['ticker']==ticker)
    return (root/entry['json']).parent/'sources'/('fred.json' if kind=='fred' else ticker.lower()+'-'+kind+'.json')


def observations(pack,subject,metric):
    return [o for o in pack['observations'] if o['subject']==subject and o['metric']==metric]


def test_entities_units_provenance_and_explicit_missing_are_reusable(archive):
    pack=build(archive,as_of='2026-11-06',boc_capture=CAPTURE)
    assert len(pack['sectors'])==8 and sum(s['coverage']['configured_stocks'] for s in pack['sectors'])==50
    assert len(pack['reports'])==2
    close=observations(pack,'stock:CSCO','stock.Close')[0]
    assert close['value']==100 and close['unit']=='USD' and close['status']=='observed'
    assert close['currency_source_id']!=close['source_id']
    fred=observations(pack,'macro:fred:UNRATE','level')
    assert len(fred)==1 and fred[0]['value']==0 and fred[0]['unit']=='percent'
    assert fred[0]['retrieved_at'] is None and fred[0]['publication_time'] is None
    assert len(observations(pack,'macro:boc:FXUSDCAD','exchange_rate'))==5
    assert all(o['point_in_time_eligible'] is False for o in pack['observations'])
    revenue=observations(pack,'stock:CSCO','sec.quarterly_revenue')[0]
    assert revenue['value']==1000 and revenue['period_start']=='2026-07-01'
    assert revenue['published_on'] is None  # Never substitute the unrelated latest filing date.
    assert observations(pack,'stock:CSCO','sec.quarterly_net_income')[0]['value']==-5
    assert all(s['coverage']['sector_brief_ready'] is False for s in pack['sectors'])
    assert all(s['kpi_status']=='not_collected' for s in pack['sectors'])
    assert 'Retrospective' in coverage_markdown(pack)


def test_deterministic_and_allowlisted_despite_index_order_and_private_fields(archive):
    first=build(archive,as_of='2026-11-06',boc_capture=CAPTURE)
    index=read_json(archive/'index.json');index['reports'].reverse();write_json(archive/'index.json',index)
    second=build(archive,as_of='2026-11-06',boc_capture=CAPTURE)
    assert canonical(first)==canonical(second)
    encoded=canonical(first)
    for private in ('private@example.com','synthetic-secret','secret-index-value','evil.invalid'):
        assert private not in encoded
    assert 'built_at' not in first  # Same inputs must not gain a new wall-clock fingerprint.
    assert all(s['source_url'] is None or '?' not in s['source_url'] for s in first['sources'])


def test_cutoff_excludes_later_reports_without_claiming_historical_vintage(archive):
    early=build(archive,as_of='2026-11-05')
    assert early['reports']==[] and early['observations']==[]
    assert early['temporal_scope']=='retrospective_reconstruction_not_point_in_time'
    # Archive generation may postdate report date: explicitly retrospective, not a fabricated vintage.
    assert len(build(archive,as_of='2026-11-06')['reports'])==2


def test_latest_version_is_selected_deterministically(archive):
    index=read_json(archive/'index.json');new=deepcopy(index['reports'][0])
    new.update(report_id='later/CSCO',generated_at='2026-11-08T01:00:00+00:00')
    index['reports'].append(new);write_json(archive/'index.json',index)
    pack=build(archive,as_of='2026-11-06')
    assert next(r for r in pack['reports'] if r['ticker']=='CSCO')['report_id']=='later/CSCO'


def test_ambiguous_version_id_fails(archive):
    index=read_json(archive/'index.json');index['reports'].append(index['reports'][0]);write_json(archive/'index.json',index)
    with pytest.raises(ValueError,match='Ambiguous'):build(archive,as_of='2026-11-06')


@pytest.mark.parametrize('change',[
    {'symbol':'OTHER'},{'symbol':None},{'currency':None},{'currency':'US$'},
])
def test_unknown_or_mismatched_listing_currency_cannot_be_a_complete_price(archive,change):
    path=source_path(archive,'info');info=read_json(path);info.update(change);write_json(path,info)
    close=observations(build(archive,as_of='2026-11-06'),'stock:CSCO','stock.Close')[0]
    assert close['value']==100 and close['status']=='incomplete' and close['currency'] is None


def test_optional_source_failure_does_not_change_report_quality(archive):
    source_path(archive,'fred').write_text('{broken')
    source_path(archive,'comparables').unlink()
    pack=build(archive,as_of='2026-11-06')
    report=next(r for r in pack['reports'] if r['ticker']=='CSCO')
    assert report['quality']=='ready' and report['peer_ids']==[]
    selected=[o for o in pack['observations'] if o['id'] in report['observation_ids'] and o['subject'].startswith('macro:fred')]
    assert all(o['status']=='missing' for o in selected)


@pytest.mark.parametrize('tampered_kind',('quant','info','ai-intel','rss-items','comparables','earnings','edgar','fred'))
def test_tracked_source_tampering_fails_instead_of_becoming_missing(archive,tampered_kind):
    index=read_json(archive/'index.json');entry=index['reports'][0]
    hashes={}
    for kind in ('quant','info','ai-intel','rss-items','comparables','earnings','edgar','fred'):
        path=source_path(archive,kind)
        if not path.exists():write_json(path,{})
        hashes[kind]=digest(path)
    entry['source_sha256']=hashes;write_json(archive/'index.json',index)
    build(archive,as_of='2026-11-06')
    source_path(archive,tampered_kind).write_text('{"changed":true}')
    with pytest.raises(ValueError,match='source integrity'):build(archive,as_of='2026-11-06')


def test_shared_fred_bytes_cannot_expose_future_values_to_an_older_report(archive):
    index=read_json(archive/'index.json');entry=index['reports'][0]
    old_date='2026-11-05'
    snapshot=read_json(archive/entry['json']);snapshot['identity']['as_of']=old_date
    snapshot['identity']['report_stamp']='20261105'
    snapshot['freshness']['report_as_of']=old_date
    snapshot['freshness']['market_data_as_of']=old_date
    for kind in ('md','pdf','json'):
        old=archive/entry[kind];new=old.with_name(old.name.replace('20261106','20261105'))
        new.write_bytes(old.read_bytes());entry[kind]=str(new.relative_to(archive))
    write_json(archive/entry['json'],snapshot)
    entry['as_of']=old_date;entry['sha256']={k:digest(archive/entry[k]) for k in ('md','pdf','json')}
    write_json(archive/'index.json',index)
    for ticker in ('CSCO','JPM'):
        write_json(source_path(archive,'fred',ticker),{'available':True,'indicators':[
            {'series_id':'UNRATE','value':4,'date':'2026-11-06'}]})
    pack=build(archive,as_of='2026-11-06')
    for report in pack['reports']:
        fred=[o for o in pack['observations'] if o['id'] in report['observation_ids'] and o['subject']=='macro:fred:UNRATE']
        assert len(fred)==1
        assert fred[0]['value']==(None if report['ticker']=='CSCO' else 4)


def test_fred_duplicates_and_future_dates_cannot_be_claimed_as_observed(archive):
    path=source_path(archive,'fred')
    write_json(path,{'available':True,'indicators':[{'series_id':'UNRATE','value':2,'date':'2026-10-01'},
        {'series_id':'UNRATE','value':3,'date':'2026-10-01'}, {'series_id':'FEDFUNDS','value':4,'date':'2026-11-07'}]})
    pack=build(archive,as_of='2026-11-06');report=next(r for r in pack['reports'] if r['ticker']=='CSCO')
    selected=[o for o in pack['observations'] if o['id'] in report['observation_ids'] and o['subject'].startswith('macro:fred')]
    assert all(o['value'] is None and o['status']=='missing' for o in selected)


@pytest.mark.parametrize('row',[
    {'value':10,'unit':'CAD','period':'2026-07-01/2026-09-30'},
    {'value':True,'unit':'USD','period':'2026-07-01/2026-09-30'},
    {'value':10,'unit':'USD','period':'2026-10-01/2026-12-31'},
    {'value':10,'unit':'USD','period':'2026-01-01/2026-09-30'},
])
def test_invalid_sec_period_or_unit_is_missing(archive,row):
    path=source_path(archive,'edgar');payload=read_json(path);payload['revenue']=row;write_json(path,payload)
    assert observations(build(archive,as_of='2026-11-06'),'stock:CSCO','sec.quarterly_revenue')[0]['value'] is None


def test_wrong_sec_issuer_symbol_is_rejected(archive):
    path=source_path(archive,'edgar');payload=read_json(path);payload['ticker']='OTHER';write_json(path,payload)
    assert observations(build(archive,as_of='2026-11-06'),'stock:CSCO','sec.quarterly_revenue')[0]['status']=='missing'


def test_boc_capture_tampering_and_future_window_fail(archive,tmp_path):
    with pytest.raises(ValueError,match='window'):build(archive,as_of='2026-11-05',boc_capture=CAPTURE)
    capture=read_json(CAPTURE);capture['payload']['observations'][0]['FXUSDCAD']['v']='99'
    path=tmp_path/'bad.json';write_json(path,capture)
    with pytest.raises(ValueError,match='checksum'):build(archive,as_of='2026-11-06',boc_capture=path)


def test_duplicate_peers_are_not_counted_twice_or_arbitrarily_selected(archive):
    path=source_path(archive,'comparables');payload=read_json(path);payload['peers'].append(payload['peers'][0]);write_json(path,payload)
    report=next(r for r in build(archive,as_of='2026-11-06')['reports'] if r['ticker']=='CSCO')
    assert report['peer_ids']==['stock:AXP','stock:MA']


def test_cli_refuses_archive_output_and_preserves_existing_file(archive,tmp_path):
    command=[sys.executable,'scripts/shared_research_pack.py','--store',str(archive),'--as-of','2026-11-06','--output']
    existing=tmp_path/'existing.json';existing.write_text('user file')
    assert subprocess.run(command+[str(existing)],capture_output=True).returncode!=0
    assert existing.read_text()=='user file'
    assert subprocess.run(command+[str(archive/'new.json')],capture_output=True).returncode!=0
    assert not (archive/'new.json').exists()


def rehash(pack):
    pack['dataset_id']=package_digest({k:v for k,v in pack.items() if k!='dataset_id'})


def test_consumer_checks_fingerprint_and_dangling_evidence_links(archive):
    pack=build(archive,as_of='2026-11-06')
    assert validate_pack(pack) is pack
    altered=deepcopy(pack);altered['as_of']='2026-11-07'
    with pytest.raises(ValueError,match='fingerprint'):validate_pack(altered)
    altered=deepcopy(pack);altered['reports'][0]['observation_ids'].append('observation:missing');rehash(altered)
    with pytest.raises(ValueError,match='reference'):validate_pack(altered)
    altered=deepcopy(pack);altered['entities'].append(altered['entities'][0]);rehash(altered)
    with pytest.raises(ValueError,match='Duplicate'):validate_pack(altered)


@pytest.mark.parametrize('cik,expected',[('749098',100),('1436126',None)])
def test_canadian_issuer_mapping_is_checked_without_stripping_suffix(tmp_path,cik,expected):
    entry={'ticker':'MG.TO','as_of':'2026-11-06','json':'archive/synthetic/MG.TO/report.json'}
    write_json(tmp_path/'archive/synthetic/MG.TO/sources/mg.to-edgar.json',
        {'ticker':'MG.TO','cik':cik,'revenue':{'value':100,'unit':'USD','period':'2026-07-01/2026-09-30'}})
    evidence=Evidence();evidence.stock('MG.TO');ids=add_sec(tmp_path,entry,evidence)
    assert evidence.observations[ids[0]]['value']==expected


def test_group_mapping_duplicates_fail_before_evidence_build(archive,tmp_path):
    config=read_json(Path(__file__).parents[1]/'config/research_teams.json')
    config['teams'][0]['tickers'].append('CSCO');path=tmp_path/'teams.json';write_json(path,config)
    with pytest.raises(ValueError,match='exactly once'):build(archive,as_of='2026-11-06',teams_path=path)


def test_malformed_optional_cells_are_isolated_without_losing_other_stocks(archive):
    write_json(source_path(archive,'fred'),{'available':True,'indicators':[
        {'series_id':['UNRATE'],'value':5,'date':'2026-10-01'},
        {'series_id':'UNRATE','value':10**500,'date':'2026-10-01'}]})
    pack=build(archive,as_of='2026-11-06')
    assert len(pack['reports'])==2
    report=next(r for r in pack['reports'] if r['ticker']=='CSCO')
    fred=[o for o in pack['observations'] if o['id'] in report['observation_ids'] and o['subject']=='macro:fred:UNRATE']
    assert fred[0]['value'] is None


@pytest.mark.parametrize('price',[0,-1])
def test_nonpositive_close_is_not_a_price_observation(archive,price):
    index=read_json(archive/'index.json');entry=index['reports'][0];path=archive/entry['json']
    snapshot=read_json(path);next(r for r in snapshot['quant'] if r['metric']=='Close')['value']=str(price)
    write_json(path,snapshot);entry['sha256']['json']=digest(path);write_json(archive/'index.json',index)
    assert observations(build(archive,as_of='2026-11-06'),'stock:CSCO','stock.Close')[0]['status']=='missing'


def test_cli_markdown_reports_coverage_without_claiming_ready_briefs(archive,tmp_path):
    output=tmp_path/'coverage.md'
    result=subprocess.run([sys.executable,'scripts/shared_research_pack.py','--store',str(archive),
        '--as-of','2026-11-06','--format','markdown','--output',str(output)],capture_output=True,text=True)
    assert result.returncode==0,result.stderr
    assert 'Industry KPIs, benchmark returns and completed sector briefs remain unavailable.' in output.read_text()
