"""Refresh both dashboards from the active holdings and available local snapshots."""
import json
import re
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'scripts'))
from universe import SUPPORTED
path = ROOT / 'docs/index.html'
html = path.read_text()
match = re.search(r'const DATA=(.*?);\n', html)
data = json.loads(match[1])
for ticker in SUPPORTED:
    for key, name in [('quant', 'quant'), ('ai', 'ai-intel'), ('peers', 'comparables'), ('earnings', 'earnings'), ('filing', 'edgar')]:
        snapshot = ROOT / 'data' / f'{ticker.lower()}-{name}.json'
        if snapshot.exists():
            data[ticker][key] = json.loads(snapshot.read_text())
macro = ROOT / 'data/fred.json'
if macro.exists():
    data['macro'] = json.loads(macro.read_text())
html = html[:match.start(1)] + json.dumps(data) + html[match.end(1):]
for name in ('index.html', 'intelligence-mockup.html'):
    (ROOT / 'docs' / name).write_text(html)
