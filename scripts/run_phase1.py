"""Run the 25 holding pipelines in sequence, reusing the FRED snapshot."""
import subprocess
import sys
from data_utils import ROOT, SCRIPTS, SUPPORTED

for ticker in SUPPORTED:
    for script in ('quant', 'ai_extract', 'comparables', 'earnings', 'edgar', 'regenerate_report'):
        print(f'RUN {ticker} {script}', flush=True)
        subprocess.run([sys.executable, str(SCRIPTS / f'{script}.py'), '--ticker', ticker], check=True, cwd=ROOT)
