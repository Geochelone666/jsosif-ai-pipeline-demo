from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import pytest
from pypdf import PdfReader, PdfWriter

import benchmark_prices as prices
import benchmark_review as benchmarks
import member_attachment_preview as preview
import sector_benchmark as appendix
import sector_briefs as sectors
from report_store import digest as file_digest,write_json
from shared_research_pack import build,digest
from snapshot_emit import emit_frozen_snapshot
from universe import SUPPORTED


@pytest.fixture
def archive(tmp_path):
    root=tmp_path/'archive';entries=[]
    for ticker in ('CSCO','JPM'):
        snapshot=emit_frozen_snapshot(ticker=ticker,as_of='2026-11-06',quant_metrics={'Close':100},
            ai={'status':'Available'},freshness={},disclaimer='Synthetic fixture')
        snapshot['quality']='ready'
        entry=dict(ticker=ticker,report_id='synthetic/'+ticker,as_of='2026-11-06',
                   generated_at='2026-11-06T21:00:00+00:00',quality='ready')
        for kind in ('pdf','json','md'):
            relative='archive/synthetic/'+ticker+'/'+ticker+'-intelligence-20261106.'+kind
            path=root/relative;path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text({'pdf':'%PDF-1.4 synthetic '+ticker,'json':json.dumps(snapshot),'md':'# '+ticker}[kind])
            entry[kind]=relative
        entry['sha256']={k:file_digest(root/entry[k]) for k in ('pdf','json','md')};entries.append(entry)
    write_json(root/'index.json',{'reports':entries})
    return root


@pytest.fixture
def review():
    return benchmarks.build(prices.load_bundle(Path(__file__).parent/'fixtures/benchmark_prices_synthetic'))


def tech(briefs):return next(b for b in briefs if b['sector_id']=='sector:technology')


def test_scoped_projection_has_all_sector_pairs_and_original_capture_lineage(archive,review):
    briefs=sectors.assemble(build(archive,as_of='2026-11-06'),benchmark_review=review)
    assert len(briefs)==8 and sum(len(b['relative_performance']['pairs']) for b in briefs)==59
    for brief in briefs:
        p=appendix.verify(brief,review)
        assert brief['schema_version']==2 and brief['delivery_ready'] is False
        assert p['review_id']==review['review_id'] and p['capture_id']==review['capture']['capture_id']
        assert {r['stock'] for r in p['pairs']}=={s['ticker'] for s in brief['stocks']}
        assert not p['within_review_window'] and 'candidate_window_outside_review' in brief['missing_evidence']
        assert brief['brief_id']==digest({k:v for k,v in brief.items() if k!='brief_id'})
    assert tech(briefs)['relative_performance']['available_pairs']==1
    consumer=next(b for b in briefs if b['sector_id']=='sector:consumer')
    assert len(consumer['relative_performance']['pairs'])==18
    assert {p['benchmark'] for p in consumer['relative_performance']['pairs']}=={'XLP','XLY'}


def test_future_observation_window_rejected_before_output(archive,review,tmp_path):
    with pytest.raises(ValueError,match='cutoff'):
        sectors.write_bundle(build(archive,as_of='2025-10-07'),tmp_path/'out',benchmark_review=review)
    assert not (tmp_path/'out').exists()


def test_within_review_window_is_still_not_approved_or_point_in_time(archive,review):
    capture=deepcopy(review['capture']);capture['start']='2025-10-02'
    for row in capture['series']:row['observations'][0]['observed_on']='2025-10-02'
    capture['capture_id']=digest({k:v for k,v in capture.items() if k!='capture_id'})
    value=benchmarks.build(capture)
    brief=tech(sectors.assemble(build(archive,as_of='2025-10-08'),benchmark_review=value))
    assert brief['relative_performance']['within_review_window']
    assert brief['relative_performance']['point_in_time_eligible'] is False
    assert brief['delivery_ready'] is False
    assert 'approved_sector_benchmarks' in brief['missing_evidence']


@pytest.mark.parametrize('field,value',[('name','Other'),('tickers',['CSCO']),('benchmark_candidates',[])])
def test_rehashed_taxonomy_mismatch_rejected(archive,review,field,value):
    pack=build(archive,as_of='2026-11-06');sector=next(s for s in pack['sectors'] if s['id']=='sector:technology')
    sector[field]=value;pack['dataset_id']=digest({k:v for k,v in pack.items() if k!='dataset_id'})
    with pytest.raises(ValueError):sectors.assemble(pack,benchmark_review=review)


@pytest.mark.parametrize('mutation',[
    lambda b:b['relative_performance'].update(within_review_window=True),
    lambda b:b['relative_performance'].update(available_pairs=12),
    lambda b:b['relative_performance'].update(capture_id='0'*64),
    lambda b:b['relative_performance'].update(retrieved_at='2026-11-06T00:00:00+00:00'),
    lambda b:b['relative_performance'].update(point_in_time_eligible=True),
    lambda b:b['relative_performance']['pairs'].pop(),
    lambda b:b['relative_performance']['pairs'][0]['result'].update(relative_return_pp=100),
    lambda b:b.update(delivery_ready=True),
])
def test_rehashed_projection_cannot_change_results_or_labels(archive,review,mutation):
    brief=deepcopy(tech(sectors.assemble(build(archive,as_of='2026-11-06'),benchmark_review=review)))
    mutation(brief);brief['brief_id']=digest({k:v for k,v in brief.items() if k!='brief_id'})
    with pytest.raises(ValueError):appendix.verify(brief,review)


def test_full_five_page_bundle_is_reproducible_and_member_loader_accepts_it(archive,review,tmp_path):
    pack=build(archive,as_of='2026-11-06')
    a,b=tmp_path/'a',tmp_path/'b'
    first=sectors.write_bundle(pack,a,benchmark_review=review)
    second=sectors.write_bundle(pack,b,benchmark_review=review)
    assert first==second and len(list(a.iterdir()))==18
    assert first['schema_version']==2 and first['benchmark_review']['review_id']==review['review_id']
    assert {p.name:p.read_bytes() for p in a.iterdir()}=={p.name:p.read_bytes() for p in b.iterdir()}
    loaded=preview.load_briefs(a)
    for entry in first['briefs']:
        reader=PdfReader(a/entry['pdf']);assert len(reader.pages)==5
        text=reader.pages[-1].extract_text()
        assert 'OUTSIDE archive review window' in text and 'SYNTHETIC FIXTURE' in text and '5 / 5' in text
        assert entry['validation']['pages']==5 and loaded[entry['sector_id']]['bytes']==(a/entry['pdf']).read_bytes()
    tech_pdf=PdfReader(a/'technology-2026-11-06.pdf')
    links=[str(a.get_object().get('/A',{}).get('/URI','')) for a in tech_pdf.pages[4].get('/Annots',[])]
    assert prices.source_url('CSCO') in links and prices.source_url('XLK') in links


@pytest.mark.parametrize('mutation',['evidence','projection','downgrade','filename'])
def test_member_loader_rejects_tampering_even_with_updated_file_hashes(archive,review,tmp_path,mutation):
    out=tmp_path/'bundle';manifest=sectors.write_bundle(build(archive,as_of='2026-11-06'),out,benchmark_review=review)
    if mutation=='evidence':
        path=out/'benchmark-review.json';value=json.loads(path.read_text());value['coverage']['available_pairs']=59
        value['review_id']=digest({k:v for k,v in value.items() if k!='review_id'});path.write_text(json.dumps(value))
        manifest['benchmark_review'].update(review_id=value['review_id'],sha256=file_digest(path))
    elif mutation=='projection':
        entry=next(e for e in manifest['briefs'] if e['sector_id']=='sector:technology')
        path=out/entry['json'];value=json.loads(path.read_text());value['relative_performance']['within_review_window']=True
        value['brief_id']=digest({k:v for k,v in value.items() if k!='brief_id'});path.write_text(json.dumps(value))
        entry['brief_id']=value['brief_id'];entry['sha256']['json']=file_digest(path)
    elif mutation=='downgrade':manifest['schema_version']=1
    else:manifest['benchmark_review']['json']='../benchmark-review.json'
    write_json(out/'manifest.json',manifest)
    with pytest.raises(ValueError):preview.load_briefs(out)


def test_all_configured_pairs_with_large_values_fit_five_pages(archive,tmp_path):
    def fetch(symbol,start,end):
        return dict(symbol=symbol,currency='USD',exchange_timezone='America/New_York',exchange_name='SYNTHETIC',
                    instrument_type='EQUITY' if symbol in SUPPORTED else 'ETF',provider_version='synthetic-test',
                    observations=[dict(observed_on=start,value=1),dict(observed_on=end,value=1e100 if symbol in SUPPORTED else 2)])
    capture=prices.capture(sorted(prices.allowed_symbols()),start='2025-10-01',end='2025-10-08',fetcher=fetch,
                           clock=lambda:datetime(2025,10,10,tzinfo=timezone.utc))
    value=benchmarks.build(capture)
    result=sectors.write_bundle(build(archive,as_of='2026-11-06'),tmp_path/'all',benchmark_review=value)
    assert value['coverage']['available_pairs']==59 and all(e['validation']['pages']==5 for e in result['briefs'])


def test_private_preview_keeps_explicit_draft_gate_and_deduplicates_groups(archive,review,tmp_path):
    out=tmp_path/'bundle';sectors.write_bundle(build(archive,as_of='2026-11-06'),out,benchmark_review=review)
    config={'groups':{'one':{'tickers':['CSCO','JPM']},'two':{'tickers':['CSCO']}},'members':[
        dict(id='synthetic',name='Fixture',email='fixture@example.com',enabled=True,timezone='UTC',send_weekday=4,
             send_time='09:00',groups=['one','two'],content_preferences={'sector_brief':True})]}
    now=datetime(2026,11,6,22,tzinfo=timezone.utc)
    off,_=preview.prepare(config,archive,now=now,sector_bundle=out)
    on,messages=preview.prepare(config,archive,now=now,sector_bundle=out,include_sector_drafts=True)
    assert not any(a['kind']=='sector_draft' for a in off['members'][0]['attachments'])
    attachments=[a for a in on['members'][0]['attachments'] if a['kind']=='sector_draft']
    assert len(attachments)==2 and len(messages)==1
    assert on['members'][0]['encoded_bytes']<preview.MAX_MESSAGE_BYTES


def test_cli_cannot_write_into_benchmark_input(archive,review,tmp_path):
    root=tmp_path/'review';benchmarks.write_bundle(review,root)
    result=subprocess.run([sys.executable,'scripts/sector_briefs.py','--store',str(archive),'--as-of','2026-11-06',
                           '--benchmark-review',str(root),'--output',str(root/'nested')],capture_output=True)
    assert result.returncode==2 and not (root/'nested').exists()


def test_rehashed_pdf_cannot_swap_in_another_sectors_appendix(archive,review,tmp_path):
    out=tmp_path/'bundle';manifest=sectors.write_bundle(build(archive,as_of='2026-11-06'),out,benchmark_review=review)
    entry=next(e for e in manifest['briefs'] if e['sector_id']=='sector:technology')
    original=PdfReader(out/entry['pdf']);other=PdfReader(out/'financial-services-2026-11-06.pdf')
    writer=PdfWriter()
    for page in original.pages[:4]:writer.add_page(page)
    writer.add_page(other.pages[4]);writer.write(out/entry['pdf'])
    entry['sha256']['pdf']=file_digest(out/entry['pdf']);write_json(out/'manifest.json',manifest)
    with pytest.raises(ValueError,match='comparison'):preview.load_briefs(out)


def test_shared_evidence_cannot_escape_bundle_through_symlink(archive,review,tmp_path):
    out=tmp_path/'bundle';sectors.write_bundle(build(archive,as_of='2026-11-06'),out,benchmark_review=review)
    path=out/'benchmark-review.json';path.rename(tmp_path/'outside.json');path.symlink_to(tmp_path/'outside.json')
    with pytest.raises(ValueError):preview.load_briefs(out)
