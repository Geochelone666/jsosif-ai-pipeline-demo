"""Project verified stock archives and allowlisted supplements into shared research views."""
from datetime import date, datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import re

from report_store import read_json, resolve_file, verified_report_files, report_advisory

ROOT = Path(__file__).resolve().parents[1]
FRED_UNITS = {'UNRATE':'percent','FEDFUNDS':'percent','CPIAUCSL':'index (1982–1984=100)','NAPM':'index'}
PEER_UNITS = {'pe':'ratio','pb':'ratio','ev_ebitda':'ratio','revenue_growth':'fraction','ret_1y':'fraction','mktcap':'native currency'}


def numeric(value):
    return value if type(value) in (int,float) and math.isfinite(value) else None


def symbol(value):
    return isinstance(value,str) and bool(re.fullmatch(r'[A-Z0-9][A-Z0-9.-]{0,19}',value))


def source(root,entry,kind):
    relative=(Path(entry['json']).parent/'sources'/kind).as_posix()
    try:
        path=resolve_file(root,relative)
        with path.open('rb') as stream:
            raw=stream.read(2*1024*1024+1)
        if len(raw)>2*1024*1024:raise ValueError('Source exceeds limit')
        value=json.loads(raw)
        if not isinstance(value,dict):raise ValueError('Invalid source object')
        return value,{'sha256':hashlib.sha256(raw).hexdigest(),'integrity':'hash observed at build; no archived expected source hash'}
    except (ValueError,OSError,TypeError):
        return None,None


def source_date(value,as_of):
    try:
        if not isinstance(value,str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}',value):return None
        parsed=date.fromisoformat(value)
        return value if parsed<=date.fromisoformat(as_of) else None
    except ValueError:return None


def peers(root,entry):
    value,provenance=source(root,entry,entry['ticker'].lower()+'-comparables.json')
    missing={'status':'missing','rows':[],'reason':'Peer source missing, malformed or future-dated'}
    if value is None:return missing
    stamp=source_date(value.get('as_of'),entry['as_of'])
    if stamp is None or not isinstance(value.get('peers'),list):return missing
    rows=[]
    for row in value['peers'][:20]:
        if not isinstance(row,dict) or not symbol(row.get('ticker')):continue
        currency=row.get('currency')
        if not isinstance(currency,str) or not re.fullmatch('[A-Z]{3}',currency):currency=None
        metrics=[]
        for name,unit in PEER_UNITS.items():
            number=numeric(row.get(name))
            if name=='mktcap' and currency is None:number=None
            metrics.append({'metric':name,'value':number,'unit':currency if name=='mktcap' else unit,
                            'status':'observed' if number is not None else 'missing'})
        rows.append({'ticker':row['ticker'],'currency':currency,'metrics':metrics})
    usable=any(m['value'] is not None for row in rows for m in row['metrics'])
    return {'status':'observed' if usable else 'missing','as_of':stamp,'provenance':provenance,'rows':rows,
            'reason':None if usable else 'No usable peer metrics in the archived source',
            'limitation':'Provider periods and native currencies can differ; values are not a normalized ranking.'}


def macro(root,entry):
    value,provenance=source(root,entry,'fred.json')
    missing={'status':'missing','observations':[],'reason':'Macro source unavailable or invalid'}
    if value is None or value.get('available') is not True or not isinstance(value.get('indicators'),list):return missing
    observed=[];seen=set()
    for row in value['indicators']:
        if not isinstance(row,dict):continue
        series=row.get('series_id')
        if not isinstance(series,str) or series not in FRED_UNITS or series in seen:continue
        seen.add(series)
        stamp=source_date(row.get('date'),entry['as_of']);number=numeric(row.get('value'))
        if stamp is None:number=None
        observed.append({'series_id':series,'value':number,'observed_on':stamp,'unit':FRED_UNITS[series],
                         'status':'observed' if number is not None else 'missing',
                         'source_url':'https://fred.stlouisfed.org/series/'+series})
    return {'status':'observed' if any(r['status']=='observed' for r in observed) else 'missing',
            'observations':observed,'provenance':provenance,
            'limitation':'Archived observations may be revised or stale; retrieval/publication timestamps are unavailable.'}


def build_dataset(root,index,*,teams_path=None):
    configured=read_json(teams_path or ROOT/'config/research_teams.json')['teams']
    teams=[{**{k:t[k] for k in ('id','name','tickers','kpi_topics','weekly_sections')},
            'benchmark_candidates':[{k:b[k] for k in ('ticker','currency','status')}
                                    for b in t['benchmark_candidates']]} for t in configured]
    latest={}
    for entry in index['reports']:
        key=(entry['as_of'],entry['generated_at'])
        ticker=entry['ticker']
        if ticker not in latest or key>(latest[ticker]['as_of'],latest[ticker]['generated_at']):latest[ticker]=entry
    stocks=[];macro_versions={};inputs=[]
    for ticker,entry in sorted(latest.items()):
        files=verified_report_files(root,entry)
        payload=read_json(files['json']);inputs.append(entry['sha256']['json'])
        peer=peers(root,entry);context=macro(root,entry)
        if 'provenance' in peer:inputs.append(peer['provenance']['sha256'])
        macro_key=None
        if 'provenance' in context:
            macro_key=context['provenance']['sha256']+':'+entry['as_of']
            macro_versions[macro_key]=context;inputs.append(macro_key)
        stocks.append({'ticker':ticker,'report_id':entry['report_id'],'report_date':entry['as_of'],
                       'generated_at':entry['generated_at'],'quality':entry['quality'],
                       'advisory':entry.get('advisory') or report_advisory(root,entry),
                       'snapshot':{'path':entry['json'],'sha256':entry['sha256']['json']},
                       'metrics':[{k:row[k] for k in ('metric','value','availability','reason')} for row in payload['quant']],
                       'source_dates':{k:payload['freshness'][k] for k in ('market_data_as_of','ai_snapshot_as_of')},
                       'peers':peer,'macro_version':macro_key,'macro_status':context['status']})
    inputs.append(hashlib.sha256(json.dumps(teams,sort_keys=True).encode()).hexdigest())
    return {'schema_version':1,'built_at':datetime.now(timezone.utc).isoformat(),
            'inputs_digest':hashlib.sha256('\n'.join(sorted(inputs)).encode()).hexdigest(),
            'teams':teams,'stocks':stocks,'macro_versions':macro_versions,
            'limitations':['Shared archive view; no provider refresh or current-day readiness claim.',
                           'Sector groupings are configurable product defaults, not portfolio weights.',
                           'Candidate benchmark returns and industry KPIs remain unavailable until validated sources exist.']}
