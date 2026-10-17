"""Run the 25 holding pipelines in sequence, reusing the FRED snapshot."""
import os
import subprocess
import sys
from config import startup_config
from data_utils import ROOT, SCRIPTS, SUPPORTED


# No HOME/USERPROFILE, proxy URLs, Python startup controls, or unrelated secrets.
# The absolute interpreter is used below; PATH also supports the Gemini CLI shebang.
RUNTIME_ENV = ('PATH', 'LANG', 'LC_ALL', 'LC_CTYPE', 'TMPDIR', 'TMP', 'TEMP',
               'SYSTEMROOT', 'WINDIR', 'HTTP_PROXY', 'HTTPS_PROXY', 'NO_PROXY',
               'http_proxy', 'https_proxy', 'no_proxy', 'SSL_CERT_FILE',
               'SSL_CERT_DIR', 'REQUESTS_CA_BUNDLE', 'CURL_CA_BUNDLE')
SCRIPT_ENV = {
    'quant': (),
    'ai_extract': ('GEMINI_CLI', 'GEMINI_API_KEY', 'GOOGLE_API_KEY', 'GEMINI_MODEL'),
    'comparables': (),
    'earnings': (),
    'edgar': (),
    'regenerate_report': (),
}


def child_env(script, config):
    """Build a fresh environment, granting Gemini credentials only to extraction."""
    env = {key: os.environ[key] for key in (*RUNTIME_ENV, *SCRIPT_ENV[script])
           if key in os.environ}
    env['REPORT_AS_OF'] = config['report_as_of']
    env['JSOSIF_REPORT_AS_OF'] = config['report_as_of']
    if script == 'ai_extract':
        env.update({'JSOSIF_' + key.upper(): str(config[key])
                    for key in ('rss_count', 'rss_max_attempts', 'rss_timeout')})
    return env


def main():
    config = startup_config()
    for ticker in SUPPORTED:
        for script in ('quant', 'ai_extract', 'comparables', 'earnings', 'edgar', 'regenerate_report'):
            print(f'RUN {ticker} {script}', flush=True)
            subprocess.run([sys.executable, str(SCRIPTS / f'{script}.py'), '--ticker', ticker],
                           check=True, cwd=ROOT, env=child_env(script, config))


if __name__ == '__main__':
    main()

