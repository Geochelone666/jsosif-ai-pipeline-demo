(() => {
'use strict';const $=id=>document.getElementById(id);let data;
const cell=value=>{const td=document.createElement('td');td.textContent=value??'Unavailable';return td;};
const row=(body,values)=>{const tr=document.createElement('tr');for(const v of values)tr.append(cell(v));body.append(tr);return tr;};
function linkCell(tr,stock){const td=document.createElement('td'),a=document.createElement('a');a.textContent='JSON · '+stock.snapshot.sha256.slice(0,12);const path=stock.snapshot.path;
 if(typeof path==='string'&&/^archive\/[A-Za-z0-9._/-]+\.json$/.test(path)&&!path.split('/').includes('..')){a.href='./'+path;td.append(a);}else td.textContent='Invalid snapshot path';tr.append(td);}
function stock(id){return data.stocks.find(s=>s.ticker===$(id).value);}
function sector(){const team=data.teams.find(t=>t.id===$('team').value);if(!team)return;
 const present=data.stocks.filter(s=>team.tickers.includes(s.ticker));$('coverage').textContent=present.length+'/'+team.tickers.length+' configured holdings have archived reports. '+present.filter(s=>s.quality==='ready'&&!s.advisory).length+' carry a Ready label; read the dates.';
 $('benchmark').textContent='Candidate benchmarks: '+team.benchmark_candidates.map(b=>b.ticker+' ('+b.currency+', '+b.status+')').join(', ')+'. Relative performance unavailable until validated aligned observations exist.';
 $('topics').replaceChildren();for(const topic of team.kpi_topics){const li=document.createElement('li');li.textContent=topic;$('topics').append(li);}
 $('sector-rows').replaceChildren();for(const s of present){const tr=row($('sector-rows'),[s.ticker,s.report_date,s.quality+(s.advisory?' · '+s.advisory:''),s.source_dates.market_data_as_of+' / '+s.source_dates.ai_snapshot_as_of]);linkCell(tr,s);}
}
function compare(){
 $('comparison').replaceChildren();for(const s of [stock('stock-a'),stock('stock-b')]){if(!s)continue;const metric=s.metrics.find(m=>m.metric===$('metric').value);const tr=row($('comparison'),[s.ticker,metric?.value,metric?.availability==='ok'?'Observed':metric?.reason||'Metric unavailable',s.report_date]);linkCell(tr,s);}
 const s=stock('stock-a');$('peers').replaceChildren();$('macro-rows').replaceChildren();if(!s)return;
 $('peer-status').textContent=s.peers.status==='observed'?'Archived provider data · '+s.peers.limitation+' Source hash observed at build: '+s.peers.provenance.sha256:s.peers.reason;
 for(const p of s.peers.rows){const value=key=>{const m=p.metrics.find(v=>v.metric===key);if(m?.value==null)return 'Unavailable';return m.unit==='fraction'?(m.value*100).toFixed(2)+'%':m.value+' '+(m.unit||'');};row($('peers'),[p.ticker+' ('+(p.currency||'currency unavailable')+')',value('pe'),value('revenue_growth'),value('ret_1y'),value('mktcap'),s.peers.as_of]);}
 const macro=data.macro_versions[s.macro_version];$('macro-status').textContent=macro?'Source context: '+s.ticker+' report '+s.report_date+'. '+macro.limitation+' Build-observed hash: '+macro.provenance.sha256:'No usable macro source is archived for the selected report.';
 for(const m of macro?.observations||[]){const tr=row($('macro-rows'),[m.series_id,m.value==null?'Unavailable':m.value+' '+m.unit,m.observed_on,m.status]);const td=document.createElement('td'),a=document.createElement('a');a.textContent='FRED series';if(/^https:\/\/fred\.stlouisfed\.org\/series\/[A-Z0-9]+$/.test(m.source_url)){a.href=m.source_url;td.append(a);}tr.append(td);}
}
(async()=>{try{const response=await fetch('./research-data.json',{cache:'no-store',credentials:'omit',redirect:'error'});if(!response.ok)throw Error('Unavailable');data=await response.json();if(data.schema_version!==1||!Array.isArray(data.stocks)||!Array.isArray(data.teams))throw Error('Invalid research view');
 for(const t of data.teams)$('team').append(new Option(t.name,t.id));for(const s of data.stocks)for(const id of ['stock-a','stock-b'])$(id).append(new Option(s.ticker,s.ticker));if(data.stocks.length>1)$('stock-b').selectedIndex=1;
 for(const metric of [...new Set(data.stocks.flatMap(s=>s.metrics.map(m=>m.metric)))].sort())$('metric').append(new Option(metric,metric));
 $('team').addEventListener('change',sector);for(const id of ['stock-a','stock-b','metric'])$(id).addEventListener('change',compare);sector();compare();$('status').textContent=data.stocks.length+' latest archived stock snapshots · View built '+data.built_at+'. No sources refreshed.';
}catch(error){$('status').textContent='The shared research view is unavailable. Return to the research library for saved reports.';}})();
})();
