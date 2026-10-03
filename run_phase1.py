"""Run the three ticker pipelines in sequence, reusing the FRED snapshot."""
import subprocess
import sys
from data_utils import ROOT

for ticker in ('NVDA', 'MSFT', 'AAPL'):
    for script in ('quant', 'ai_extract', 'comparables', 'earnings', 'edgar', 'regenerate_report'):
        print(f'RUN {ticker} {script}', flush=True)
        subprocess.run([sys.executable, str(ROOT / f'{script}.py'), '--ticker', ticker], check=True, cwd=ROOT)
