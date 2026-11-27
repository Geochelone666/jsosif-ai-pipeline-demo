"""Build deterministic, retrospective research evidence from verified local archives."""
import argparse
from datetime import date, datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import re
from urllib.parse import parse_qs, urlsplit

from boc_macro import parse as parse_boc
from edgar import CANADIAN_SEC_LISTINGS
from report_store import read_json, verified_report_files
from research_workspace import FRED_UNITS, PEER_UNITS, source, source_date, symbol
from universe import SUPPORTED

ROOT=Path(__file__).resolve().parents[1]
MAX_BYTES=2*1024*1024
STOCK_UNITS={'Close':'price','Return 1D (%)':'percent','Return 1W (%)':'percent',
             'Return 1M (%)':'percent','Return YTD (%)':'percent','Return 1Y (%)':'percent',
             'Annualized volatility (%)':'percent','Beta vs SPY':'ratio'}


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)


def digest(value):return hashlib.sha256(canonical(value).encode()).hexdigest()


def exact_date(value):
    if not isinstance(value,str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}',value):
        raise ValueError('Expected an ISO date')
    return date.fromisoformat(value)


def timestamp(value):
    try:
        parsed=datetime.fromisoformat(value.replace('Z','+00:00'))
        if parsed.utcoffset() is not None:return parsed.astimezone(timezone.utc).isoformat()
    except (ValueError,TypeError,AttributeError):pass
    return None


def number(value,*,text=False):
    if text and isinstance(value,str) and re.fullmatch(r'[+-]?\d+(?:\.\d+)?',value):
        value=float(value)
    try:return value if type(value) in (int,float) and math.isfinite(value) else None
    except OverflowError:return None


def currency(value):
    return value if isinstance(value,str) and re.fullmatch('[A-Z]{3}',value) else None


def label(value):
    return value if isinstance(value,str) and re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9 &(),./+\-]{0,159}',value) else None


def read_bounded(path):
    with Path(path).open('rb') as stream:raw=stream.read(MAX_BYTES+1)
    if len(raw)>MAX_BYTES:raise ValueError('Input exceeds size limit')
    return json.loads(raw)


def teams(path):
    config=read_bounded(path)
    if (not isinstance(config,dict) or type(config.get('schema_version')) is not int or
            config['schema_version']!=1 or config.get('status')!='product_default'):
        raise ValueError('Expected product-default research teams')
    rows=config.get('teams');selected=[];ids=set();tickers=[]
    if not isinstance(rows,list) or len(rows)!=8:raise ValueError('Expected eight configured research teams')
    for row in rows:
        if (not isinstance(row,dict) or not isinstance(row.get('id'),str) or
                not re.fullmatch('[a-z][a-z0-9-]{0,79}',row['id']) or row['id'] in ids or
                not label(row.get('name')) or not isinstance(row.get('tickers'),list) or
                not row['tickers'] or any(not symbol(t) for t in row['tickers'])):
            raise ValueError('Invalid research team identity')
        ids.add(row['id']);tickers.extend(row['tickers'])
        topics=row.get('kpi_topics');benchmarks=row.get('benchmark_candidates')
        if not isinstance(topics,list) or not all(label(t) for t in topics) or not isinstance(benchmarks,list):
            raise ValueError('Invalid research topic or benchmark list')
        candidates=[]
        for b in benchmarks:
            if not isinstance(b,dict) or not symbol(b.get('ticker')) or not currency(b.get('currency')) or b.get('status')!='proposed':
                raise ValueError('Unreviewed benchmark cannot be activated')
            candidates.append({k:b[k] for k in ('ticker','currency','status')})
        selected.append({'id':'sector:'+row['id'],'name':row['name'],'classification':'research_team_product_default',
                         'tickers':sorted(row['tickers']),'kpi_topics':topics,
                         'kpi_status':'not_collected','benchmark_candidates':sorted(candidates,key=lambda b:b['ticker'])})
    if len(tickers)!=len(set(tickers)) or set(tickers)!=set(SUPPORTED):
        raise ValueError('Research teams must cover the supported universe exactly once')
    return sorted(selected,key=lambda r:r['id'])


class Evidence:
    def __init__(self):
        self.entities={};self.sources={};self.observations={};self.relationships={}

    def entity(self,kind,key,**metadata):
        identity=kind+':'+key
        row={'id':identity,'kind':kind,**metadata}
        prior=self.entities.get(identity)
        if prior is not None and prior!=row:raise ValueError('Conflicting entity identity')
        self.entities[identity]=row
        return identity

    def stock(self,ticker):
        return self.entity('stock',ticker,ticker=ticker,identity_status='provider_symbol_only',exchange_mic=None)

    def provenance(self,kind,provenance,*,url=None,path=None):
        if provenance is None:return None
        row={'kind':kind,'sha256':provenance['sha256'],'integrity':provenance['integrity'],
             'source_url':url,'archive_path':path}
        identity='source:'+digest(row);self.sources[identity]={'id':identity,**row}
        return identity

    def relation(self,subject,predicate,object_,source_id,context_date):
        row={'subject':subject,'predicate':predicate,'object':object_,
             'source_id':source_id,'context_date':context_date}
        self.relationships[digest(row)]=row

    def observation(self,subject,metric,value,unit,observed_on,source_id,context_date,*,
                    currency_=None,currency_source_id=None,period_start=None,retrieved_at=None,limitations=()):
        value=number(value)
        observed_on=source_date(observed_on,context_date)
        status='missing' if value is None else ('observed' if unit and observed_on and source_id else 'incomplete')
        if retrieved_at and observed_on and exact_date(observed_on)>datetime.fromisoformat(retrieved_at).date():
            value=None;status='missing';limitations=(*limitations,'Observation date is after source retrieval')
        row={'subject':subject,'metric':metric,'value':value,'unit':unit,'currency':currency_,
             'currency_source_id':currency_source_id,
             'status':status,'observed_on':observed_on,'period_start':period_start,
             'published_on':None,'publication_time':None,'retrieved_at':retrieved_at,
             'source_id':source_id,'context_date':context_date,
             'point_in_time_eligible':False,'limitations':sorted(set(limitations)),
             'missing_reason':None if status=='observed' else ('value_unavailable_or_rejected' if status=='missing' else 'unit_date_or_source_missing')}
        identity='observation:'+digest(row);self.observations[identity]={'id':identity,**row}
        return identity


def archived_source(root,entry,kind,evidence,url):
    name='fred.json' if kind=='fred' else entry['ticker'].lower()+'-'+kind+'.json'
    value,provenance=source(root,entry,name)
    return value,evidence.provenance(kind,provenance,url=url)


def add_fred(root,entry,evidence):
    raw,source_id=archived_source(root,entry,'fred',evidence,'https://fred.stlouisfed.org/')
    rows={};ambiguous=set()
    if isinstance(raw,dict) and raw.get('available') is True and isinstance(raw.get('indicators'),list):
        for row in raw['indicators']:
            if not isinstance(row,dict) or not isinstance(row.get('series_id'),str) or row['series_id'] not in FRED_UNITS:continue
            key=row['series_id']
            if key in rows:ambiguous.add(key)
            rows[key]=row
    result=[]
    for series,unit in sorted(FRED_UNITS.items()):
        subject=evidence.entity('macro','fred:'+series,provider='FRED',series_id=series)
        row=rows.get(series,{})
        stamp=source_date(row.get('date'),entry['as_of'])
        value=number(row.get('value')) if stamp and series not in ambiguous else None
        result.append(evidence.observation(subject,'level',value,unit,stamp,source_id,entry['as_of'],
                      limitations=('Archive vintage, retrieval and publication time unavailable; revisions may exist',)))
    return result


def add_peers(root,entry,evidence):
    raw,source_id=archived_source(root,entry,'comparables',evidence,'https://finance.yahoo.com/')
    stamp=source_date(raw.get('as_of'),entry['as_of']) if isinstance(raw,dict) else None
    if not stamp or not isinstance(raw.get('peers'),list):return [],[]
    rows=raw['peers']
    if len(rows)>20:return [],[]
    known=set();duplicates=set()
    for row in rows:
        if isinstance(row,dict) and symbol(row.get('ticker')):
            if row['ticker'] in known:duplicates.add(row['ticker'])
            known.add(row['ticker'])
    ids=[];observations=[]
    for row in rows:
        if not isinstance(row,dict) or not symbol(row.get('ticker')) or row['ticker'] in duplicates or row['ticker']==entry['ticker']:continue
        subject=evidence.stock(row['ticker']);ids.append(subject)
        evidence.relation('stock:'+entry['ticker'],'provider_peer_candidate',subject,source_id,entry['as_of'])
        code=currency(row.get('currency'))
        for metric,unit in sorted(PEER_UNITS.items()):
            value=number(row.get(metric))
            if metric=='mktcap':unit=code
            observations.append(evidence.observation(subject,'peer.'+metric,value,unit,stamp,source_id,entry['as_of'],
                currency_=code if metric=='mktcap' else None,currency_source_id=source_id if metric=='mktcap' and code else None,
                limitations=('Provider metric periods and return endpoints are not harmonized',
                             'Native currencies must not be aggregated or ranked without reconciliation')))
    return sorted(ids),observations


def add_sec(root,entry,evidence):
    raw,source_id=archived_source(root,entry,'edgar',evidence,'https://www.sec.gov/edgar/search/')
    ticker=entry['ticker'];valid=isinstance(raw,dict) and raw.get('ticker')==ticker
    cik=str(raw.get('cik','')) if valid else ''
    valid=valid and bool(re.fullmatch(r'[0-9]{1,10}',cik)) and int(cik)>0
    if ticker.endswith('.TO'):valid=valid and ticker in CANADIAN_SEC_LISTINGS and cik==CANADIAN_SEC_LISTINGS[ticker][1]
    elif '.' in ticker:valid=False  # No suffix stripping or inferred foreign issuer.
    result=[]
    for metric in ('revenue','net_income'):
        row=raw.get(metric) if valid else None
        value=None;start=end=None
        if isinstance(row,dict) and row.get('unit')=='USD':
            try:
                start,end=row['period'].split('/')
                first,last=exact_date(start),exact_date(end)
                if 70<=(last-first).days<=110 and last<=exact_date(entry['as_of']):value=number(row.get('value'))
                else:start=end=None
            except (KeyError,ValueError,TypeError,AttributeError):start=end=None
        result.append(evidence.observation('stock:'+ticker,'sec.quarterly_'+metric,value,'USD',end,source_id,
            entry['as_of'],currency_='USD',currency_source_id=source_id,period_start=start,
            limitations=('Archived fact lacks its own accession and filing/retrieval timestamp',
                         'Latest filing metadata is not evidence of this fact publication date')))
    return result


def add_boc(path,evidence,as_of):
    capture=read_bounded(path)
    if not isinstance(capture,dict):raise ValueError('Invalid BoC capture')
    raw=capture.get('payload');retrieved=timestamp(capture.get('captured_at'))
    url=urlsplit(capture.get('request_url',''));query=parse_qs(url.query,keep_blank_values=True)
    if (url.scheme!='https' or url.netloc!='www.bankofcanada.ca' or url.path!='/valet/observations/FXUSDCAD/json' or
            url.fragment or set(query)!={'start_date','end_date'} or any(len(v)!=1 for v in query.values()) or not retrieved):
        raise ValueError('Invalid BoC capture identity')
    start,end=exact_date(query['start_date'][0]),exact_date(query['end_date'][0])
    if start>end or (end-start).days>3660 or end>exact_date(as_of) or end>datetime.fromisoformat(retrieved).date():
        raise ValueError('BoC window is outside the requested evidence date')
    checksum=hashlib.sha256(json.dumps(raw,sort_keys=True,allow_nan=False).encode()).hexdigest()
    if checksum!=capture.get('canonical_payload_sha256'):raise ValueError('BoC capture checksum mismatch')
    try:parsed=parse_boc(raw,start,end,datetime.fromisoformat(retrieved))
    except (ValueError,TypeError,KeyError,AttributeError,OverflowError):
        raise ValueError('Invalid BoC observation contract') from None
    source_id=evidence.provenance('boc',{'sha256':checksum,'integrity':'capture canonical JSON consistency; not a provider signature'},
                                  url='https://www.bankofcanada.ca/valet/docs')
    subject=evidence.entity('macro','boc:FXUSDCAD',provider='Bank of Canada Valet',series_id='FXUSDCAD')
    ids=[evidence.observation(subject,'exchange_rate',r['value'],'CAD per USD',r['observed_on'],source_id,as_of,
                            currency_='CAD',currency_source_id=source_id,retrieved_at=retrieved,
                            limitations=('Capture can postdate the report cutoff; not a historical vintage',))
         for r in parsed['observations']]
    return ids


def build(root,*,as_of,teams_path=None,boc_capture=None):
    exact_date(as_of);root=Path(root)
    configured=teams(teams_path or ROOT/'config/research_teams.json')
    evidence=Evidence();team_source=evidence.provenance('research_configuration',
        {'sha256':digest(configured),'integrity':'canonical selected configuration; product defaults'})
    for team in configured:
        evidence.entity('sector',team['id'].removeprefix('sector:'),name=team['name'],classification=team['classification'])
        for ticker in team['tickers']:
            evidence.stock(ticker);evidence.relation('stock:'+ticker,'covered_by',team['id'],team_source,as_of)
        for b in team['benchmark_candidates']:
            target=evidence.entity('benchmark',b['ticker'],ticker=b['ticker'],currency=b['currency'],status='proposed')
            evidence.relation(team['id'],'proposed_benchmark',target,team_source,as_of)
    index=read_json(root/'index.json');latest={};identities=set()
    if not isinstance(index,dict) or not isinstance(index.get('reports'),list):raise ValueError('Archive index required')
    for entry in index['reports']:
        if not isinstance(entry,dict) or not symbol(entry.get('ticker')):raise ValueError('Invalid archive identity')
        exact_date(entry['as_of']);generated=timestamp(entry.get('generated_at'))
        if not generated or not isinstance(entry.get('report_id'),str) or entry['report_id'] in identities:
            raise ValueError('Ambiguous archive version identity')
        identities.add(entry['report_id'])
        if entry['as_of']>as_of or entry['ticker'] not in SUPPORTED:continue
        key=(entry['as_of'],generated,entry['report_id'])
        if entry['ticker'] not in latest or key>latest[entry['ticker']][0]:latest[entry['ticker']]=(key,entry)
    reports=[]
    for ticker,(_,entry) in sorted(latest.items()):
        files=verified_report_files(root,entry)
        with files['json'].open('rb') as stream:raw_snapshot=stream.read(MAX_BYTES+1)
        if len(raw_snapshot)>MAX_BYTES or hashlib.sha256(raw_snapshot).hexdigest()!=entry['sha256']['json']:
            raise ValueError('Snapshot changed after archive verification')
        snapshot=json.loads(raw_snapshot)
        source_id=evidence.provenance('verified_snapshot',{'sha256':entry['sha256']['json'],'integrity':'verified against archived expected hash'},path=entry['json'])
        info,info_id=archived_source(root,entry,'info',evidence,'https://finance.yahoo.com/')
        info_matches=isinstance(info,dict) and info.get('symbol')==ticker
        code=currency(info.get('currency')) if info_matches else None
        industry=label(info.get('industry')) if info_matches else None
        industry_id=None
        if industry:
            industry_id=evidence.entity('industry','yahoo:'+digest(industry),name=industry,classification='provider_label')
            evidence.relation('stock:'+ticker,'provider_industry',industry_id,info_id,entry['as_of'])
        quant={r['metric']:r for r in snapshot['quant']};fresh=snapshot['freshness'];obs=[]
        for metric,unit in STOCK_UNITS.items():
            row=quant.get(metric,{})
            value=number(row.get('value'),text=True) if row.get('availability')=='ok' else None
            if metric=='Close' and value is not None and value<=0:value=None
            obs.append(evidence.observation('stock:'+ticker,'stock.'+metric,value,code if unit=='price' else unit,
                fresh.get('market_data_as_of'),source_id,entry['as_of'],currency_=code if unit=='price' else None,
                currency_source_id=info_id if unit=='price' and code else None,
                retrieved_at=timestamp(fresh.get('market_data_fetched_at')),
                limitations=('Saved snapshot value; adjustment basis and exact return endpoints unavailable',)))
        macro_ids=add_fred(root,entry,evidence);peer_ids,peer_obs=add_peers(root,entry,evidence)
        obs+=macro_ids+peer_obs+add_sec(root,entry,evidence)
        reports.append({'ticker':ticker,'report_id':entry['report_id'],'as_of':entry['as_of'],
                        'archive_generated_at':timestamp(entry['generated_at']),'quality':entry['quality'],
                        'snapshot_source_id':source_id,'industry_id':industry_id,
                        'peer_ids':peer_ids,'observation_ids':sorted(set(obs))})
    additional_macro=add_boc(boc_capture,evidence,as_of) if boc_capture else []
    for team in configured:
        selected=[r for r in reports if r['ticker'] in team['tickers']]
        team['coverage']={'configured_stocks':len(team['tickers']),'archived_stocks':len(selected),
                          'missing_reports':sorted(set(team['tickers'])-{r['ticker'] for r in selected}),
                          'with_industry':sum(r['industry_id'] is not None for r in selected),
                          'with_three_to_five_peers':sum(3<=len(r['peer_ids'])<=5 for r in selected),
                          'benchmark_returns':'missing','sector_brief_ready':False}
    payload={'schema_version':1,'as_of':as_of,'temporal_scope':'retrospective_reconstruction_not_point_in_time',
             'sectors':configured,'reports':reports,'additional_macro_observations':sorted(additional_macro),
             'entities':sorted(evidence.entities.values(),key=lambda r:r['id']),
             'sources':sorted(evidence.sources.values(),key=lambda r:r['id']),
             'observations':sorted(evidence.observations.values(),key=lambda r:r['id']),
             'relationships':sorted(evidence.relationships.values(),key=canonical),
             'limitations':['No live refresh, current readiness, investment conclusion or production activation.',
                            'Configured research sectors and provider industry labels are different taxonomies.',
                            'Missing vintage/publication evidence makes this dataset ineligible for point-in-time backtests.',
                            'Benchmark candidates and KPI topics are plans, not collected observations.']}
    pack={'dataset_id':digest(payload),**payload}
    validate_pack(pack)
    return pack


def validate_pack(pack):
    """Verify the versioned package fingerprint, identities and evidence links.

    This is an integrity/contract check, not provider authentication or a sanitizer
    for arbitrary third-party content. Only build() performs the public projection.
    """
    keys={'dataset_id','schema_version','as_of','temporal_scope','sectors','reports','additional_macro_observations',
          'entities','sources','observations','relationships','limitations'}
    if (not isinstance(pack,dict) or set(pack)!=keys or type(pack['schema_version']) is not int or
            pack['schema_version']!=1 or pack['temporal_scope']!='retrospective_reconstruction_not_point_in_time' or
            pack['dataset_id']!=digest({k:v for k,v in pack.items() if k!='dataset_id'})):
        raise ValueError('Invalid shared research package fingerprint or schema')
    cutoff=exact_date(pack['as_of'])
    def registry(rows):
        if not isinstance(rows,list) or any(not isinstance(r,dict) or not isinstance(r.get('id'),str) for r in rows):
            raise ValueError('Invalid evidence registry')
        result={r['id']:r for r in rows}
        if len(result)!=len(rows):raise ValueError('Duplicate evidence identity')
        return result
    entities=registry(pack['entities']);sources=registry(pack['sources']);observations=registry(pack['observations'])
    for identity,row in entities.items():
        if row.get('kind') not in ('stock','sector','industry','benchmark','macro') or not identity.startswith(row['kind']+':'):
            raise ValueError('Invalid entity namespace')
    for identity,row in sources.items():
        if (identity!='source:'+digest({k:v for k,v in row.items() if k!='id'}) or
                not isinstance(row.get('sha256'),str) or not re.fullmatch('[0-9a-f]{64}',row['sha256'])):
            raise ValueError('Invalid source fingerprint')
        if row.get('source_url'):
            url=urlsplit(row['source_url'])
            if url.scheme!='https' or not url.hostname or url.username or url.password or url.query or url.fragment:
                raise ValueError('Source reference must not contain credentials or query strings')
    for identity,row in observations.items():
        if (identity!='observation:'+digest({k:v for k,v in row.items() if k!='id'}) or row.get('subject') not in entities or
                row.get('source_id') is not None and row['source_id'] not in sources or
                row.get('currency_source_id') is not None and row['currency_source_id'] not in sources or
                row.get('status') not in ('observed','incomplete','missing') or row.get('point_in_time_eligible') is not False):
            raise ValueError('Invalid observation identity or reference')
        context=exact_date(row['context_date'])
        if context>cutoff or row.get('observed_on') and exact_date(row['observed_on'])>context:
            raise ValueError('Observation is outside its evidence context')
        if row.get('period_start') and (not row.get('observed_on') or exact_date(row['period_start'])>exact_date(row['observed_on'])):
            raise ValueError('Invalid observation period')
        if row['retrieved_at'] is not None and timestamp(row['retrieved_at']) is None:
            raise ValueError('Invalid retrieval timestamp')
        if row['publication_time'] is not None or row['published_on'] is not None:
            raise ValueError('This schema does not establish historical publication evidence')
        if row['status']=='missing':
            if row['value'] is not None:raise ValueError('Missing evidence cannot carry a numeric assertion')
        elif number(row['value']) is None:raise ValueError('Nonfinite or nonnumeric observation')
        if row['status']=='observed' and not (row['unit'] and row['observed_on'] and row['source_id']):
            raise ValueError('Observed evidence requires unit, date and source')
    for relation in pack['relationships']:
        if relation['subject'] not in entities or relation['object'] not in entities or relation['source_id'] not in sources:
            raise ValueError('Broken research relationship')
        if exact_date(relation['context_date'])>cutoff:raise ValueError('Future relationship context')
    for report in pack['reports']:
        if ('stock:'+report['ticker'] not in entities or report['snapshot_source_id'] not in sources or
                not set(report['observation_ids'])<=observations.keys() or
                not set(report['peer_ids'])<=entities.keys() or
                report['industry_id'] is not None and report['industry_id'] not in entities or
                exact_date(report['as_of'])>cutoff):
            raise ValueError('Broken archive evidence reference')
    if not set(pack['additional_macro_observations'])<=observations.keys():raise ValueError('Broken macro evidence reference')
    return pack


def coverage_markdown(pack):
    lines=['# Shared research evidence coverage','',
           'Cutoff: '+pack['as_of']+' · Retrospective archive reconstruction; not point-in-time backtest data.',
           '', 'Dataset SHA-256: `'+pack['dataset_id']+'`','',
           '| Research group | Archived / configured | Industry labels | 3–5 peer candidates |',
           '|---|---:|---:|---:|']
    for team in pack['sectors']:
        c=team['coverage'];lines.append(f"| {team['name']} | {c['archived_stocks']} / {c['configured_stocks']} | {c['with_industry']} | {c['with_three_to_five_peers']} |")
    observed=sum(o['status']=='observed' for o in pack['observations'])
    incomplete=sum(o['status']=='incomplete' for o in pack['observations'])
    lines+=['',f"Unique observations: {observed} observed, {incomplete} incomplete, {len(pack['observations'])-observed-incomplete} missing.",
            '', 'Industry KPIs, benchmark returns and completed sector briefs remain unavailable.',
            'Peer counts describe provider candidates, not comparable fiscal periods or valuations.','']
    lines+=['## Macro observation dates','','| Series | Available observations | First date | Last date |',
            '|---|---:|---|---|']
    for entity in pack['entities']:
        if entity['kind']!='macro':continue
        dates=sorted({o['observed_on'] for o in pack['observations']
                      if o['subject']==entity['id'] and o['status']=='observed'})
        lines.append(f"| {entity['id']} | {len(dates)} | {dates[0] if dates else 'missing'} | {dates[-1] if dates else 'missing'} |")
    lines+=['','Observation dates can precede the cutoff; this build does not refresh providers.','']
    for team in pack['sectors']:
        lines+=['## '+team['name'],'','Missing reports: '+(', '.join(team['coverage']['missing_reports']) or 'none')+'.','']
    return '\n'.join(lines)


def write_new(path,value):
    fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o644)
    with os.fdopen(fd,'w',encoding='utf-8') as stream:stream.write(value)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--store',type=Path,required=True);parser.add_argument('--as-of',required=True)
    parser.add_argument('--boc-capture',type=Path);parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--format',choices=('json','markdown'),default='json')
    args=parser.parse_args()
    try:
        if args.output.resolve().is_relative_to(args.store.resolve()):raise ValueError('Output must not alter archive')
        pack=build(args.store,as_of=args.as_of,boc_capture=args.boc_capture)
        content=coverage_markdown(pack) if args.format=='markdown' else json.dumps(pack,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
        write_new(args.output,content)
    except (OSError,ValueError,KeyError,TypeError,AttributeError):
        parser.error('Evidence build failed; verify archive integrity, input contracts and a new output path')
    print(f"Shared evidence built: {len(pack['reports'])} stock reports, {len(pack['sectors'])} research groups; retrospective only")


if __name__=='__main__':main()
