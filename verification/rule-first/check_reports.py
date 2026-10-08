import hashlib, json, os, shutil, subprocess, sys
from pathlib import Path
root=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(root))
from ai_extract import extract, KEYS, classify_rule
out=root/'verification/report-compat';out.mkdir(exist_ok=True)
for pattern in ('*.py','*.json','*.csv'):
    for p in root.glob(pattern):shutil.copy2(p,out/p.name)
env={**os.environ,'REPORT_AS_OF':'2026-10-05'}
results={}
for ticker in ('NVDA','MSFT','AAPL','GOOGL','AMZN','TSLA'):
    def render():
        subprocess.run([sys.executable,'regenerate_report.py','--ticker',ticker],cwd=out,env=env,check=True,capture_output=True)
        return (out/f'{ticker}-intelligence-20261005.md').read_bytes()
    before=render()
    path=out/f'{ticker.lower()}-ai-intel.json';ai=json.loads(path.read_text());rss=json.loads((out/f'{ticker.lower()}-rss-items.json').read_text());by={i['headline']:i for i in rss}
    for key in KEYS:
        for item in ai[key]:
            extra=classify_rule(by[item['headline']],ticker)[1]
            item.update({k:v for k,v in extra.items() if k not in item})
    path.write_text(json.dumps(ai));after=render();assert before==after
    path.write_text(json.dumps(extract(rss,ticker)));render()
    results[ticker]={'additive_metadata_report_byte_identical':True,'rule_output_report_renders':True}
subprocess.run([sys.executable,'validate_phase1.py'],cwd=out,env=env,check=True,capture_output=True)
(root/'verification/rule-first/report-checks.json').write_text(json.dumps(results,indent=2))
print('Six reports: additive fields byte-identical; rule reports render; existing validate_phase1 passes.')
