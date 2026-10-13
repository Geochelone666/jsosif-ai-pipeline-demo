"""Run the 25 holding pipelines in sequence, reusing the FRED snapshot."""
import os
import subprocess
import sys
from config import startup_config
from data_utils import ROOT, SCRIPTS, SUPPORTED


def main():
    config = startup_config()
    # Children receive only normalized settings; report scripts retain their date API.
    env = dict(os.environ)
    env.update({'JSOSIF_' + key.upper(): str(value) for key, value in config.items()})
    env['REPORT_AS_OF'] = config['report_as_of']
    for ticker in SUPPORTED:
        for script in ('quant', 'ai_extract', 'comparables', 'earnings', 'edgar', 'regenerate_report'):
            print(f'RUN {ticker} {script}', flush=True)
            subprocess.run([sys.executable, str(SCRIPTS / f'{script}.py'), '--ticker', ticker],
                           check=True, cwd=ROOT, env=env)


if __name__ == '__main__':
    main()
