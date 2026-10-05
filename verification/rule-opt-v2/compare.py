"""Offline, repeatable category comparison; never calls a model or network."""
import importlib.util
import json
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))
import ai_extract as v2
spec = importlib.util.spec_from_file_location('frozen_v1', HERE/'v1_ai_extract.py')
v1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v1)

def evaluate(module):
    counts = dict(unique_headlines=0, rule=0, matched=0, agreed=0)
    details = {}
    for ticker in v1.ALIASES:
        items = json.loads((HERE/'fixtures'/f'{ticker.lower()}-rss-items.json').read_text())
        historical = json.loads((HERE/'fixtures'/f'{ticker.lower()}-ai-intel.json').read_text())
        labels = {i['headline']: k for k in v1.KEYS for i in historical[k]}
        rows = []
        for item in {i['headline']: i for i in items}.values():
            category, result = module.classify_rule(item, ticker)
            rows.append(dict(headline=item['headline'], category=category if result['extraction_method']=='rule' else None,
                             historical=labels.get(item['headline']), event_type=result['event_type'], sentiment=result['sentiment']))
        stats = module.extract(items, ticker)['extraction_stats']
        comparisons = [r for r in rows if r['category'] and r['historical']]
        counts['unique_headlines'] += stats['unique_headlines']
        counts['rule'] += stats['rule']
        counts['matched'] += len(comparisons)
        counts['agreed'] += sum(r['category']==r['historical'] for r in comparisons)
        details[ticker] = dict(stats=stats, rows=rows)
    counts['coverage'] = counts['rule']/counts['unique_headlines']
    counts['agreement'] = counts['agreed']/counts['matched']
    return dict(overall=counts, tickers=details)

if __name__ == '__main__':
    result = {name: evaluate(module) for name, module in [('v1',v1),('v2',v2)]}
    common = []
    for ticker in v1.ALIASES:
        for a,b in zip(result['v1']['tickers'][ticker]['rows'],result['v2']['tickers'][ticker]['rows']):
            if a['category'] and b['category'] and a['historical']:
                common.append((a,b))
    result['common_matched'] = dict(count=len(common), **{name:sum(pair[idx]['category']==pair[idx]['historical'] for pair in common) for idx,name in enumerate(('v1','v2'))})
    (HERE/'comparison.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v['overall'] for k,v in result.items() if k in ('v1','v2')},indent=2))
    print(result['common_matched'])
