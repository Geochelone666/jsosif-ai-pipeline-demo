"""Archive selection and safe path handling work without browser dependencies."""
import json
from pathlib import Path
import shutil
import subprocess

import pytest


def test_archive_browser_keeps_newest_version_per_holding_and_handles_missing_values(tmp_path):
    node = shutil.which('node')
    if not node:
        pytest.skip('Node required for archive browser checks')
    root = Path(__file__).resolve().parents[1]
    script = (root / 'docs/index.html').read_text().split('<script>', 1)[1].split('</script>', 1)[0]
    target = tmp_path / 'archive.js'
    target.write_text(script + '''
const archive = JSOSIFArchive;
const reports = [
  {ticker:'CSCO',as_of:'2026-10-18',generated_at:'2026-10-19T08:00:00Z'},
  {ticker:'JPM',as_of:'2026-10-19',generated_at:'2026-10-19T10:00:00Z'},
  {ticker:'CSCO',as_of:'2026-10-19',generated_at:'2026-10-19T09:00:00Z'},
  {ticker:'CSCO',as_of:'2026-10-19',generated_at:'2026-10-19T11:00:00Z'}
];
process.stdout.write(JSON.stringify({
  latest: archive.latestReports(reports),
  inputLength: reports.length,
  metrics: [null, undefined, '', 'N/A', '0', '1,234.50', '-2.00', 'Infinity'].map(archive.metric),
  paths: ['archive/run/CSCO.pdf', '../secret.json', 'archive/../state/secret.json',
          'https://example.com/report.pdf', 'javascript:alert(1)', 'archive/quote".pdf'].map(archive.safePath)
}));
''')
    result = subprocess.run([node, str(target)], capture_output=True, text=True, check=True)
    values = json.loads(result.stdout)
    assert [r['ticker'] for r in values['latest']] == ['CSCO', 'JPM']
    assert values['latest'][0]['generated_at'] == '2026-10-19T11:00:00Z'
    assert values['inputLength'] == 4
    assert values['metrics'] == [None, None, None, None, 0, 1234.5, -2, None]
    assert values['paths'] == [True, False, False, False, False, False]
