import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from ai_extract import extract, KEYS
root = Path(__file__).resolve().parents[2]
results = {}; total = rules = matched = agreed = 0
for ticker in ('NVDA','MSFT','AAPL','GOOGL','AMZN','TSLA'):
    items = json.loads((root/f'{ticker.lower()}-rss-items.json').read_text())
    historical = json.loads((root/f'{ticker.lower()}-ai-intel.json').read_text())
    baseline = {it['headline']: k for k in KEYS for it in historical[k]}
    data = extract(items, ticker)
    comparisons = [(it['headline'], k, baseline[it['headline']]) for k in KEYS for it in data[k] if it['headline'] in baseline]
    stats = data['extraction_stats'];total += stats['unique_headlines'];rules += stats['rule'];matched += len(comparisons);agreed += sum(k==b for _,k,b in comparisons)
    results[ticker] = dict(stats=stats, historical_category_comparisons=comparisons)
results['overall'] = dict(unique_headlines=total, rule=rules, rule_coverage=rules/total, ai_candidates=total-rules, historical_matched=matched, historical_category_agreement=agreed/matched if matched else None, target_met=rules/total>=.7, limitation='Historical AI is not ground truth and has no event_type/sentiment labels; true accuracy cannot be measured from these fixtures.')
(root/'verification/rule-first/benchmark.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results['overall'],indent=2))
