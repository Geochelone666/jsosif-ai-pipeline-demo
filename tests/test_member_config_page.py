"""Keep browser-exported private configuration compatible with the Python importer."""
from copy import deepcopy
import json
from pathlib import Path
import shutil
import subprocess

import pytest

from subscriptions import validate


def test_browser_validator_matches_subscription_schema(tmp_path):
    node = shutil.which('node')
    if not node:
        pytest.skip('Node is required for the standalone browser validator contract')
    root = Path(__file__).resolve().parents[1]
    html = (root / 'docs/members.html').read_text()
    script = html.split('<script>', 1)[1].split('</script>', 1)[0]
    fixture = json.loads((root / 'config/subscriptions.example.json').read_text())
    values = [deepcopy(fixture)]
    for field, value in [('enabled', 'false'), ('timezone', 'not/a/zone'),
                         ('send_time', '24:00'), ('send_weekday', True),
                         ('groups', ['missing']), ('email', 'a..b@example.com'),
                         ('email', 'Name <a@example.com>'), ('name', '')]:
        changed = deepcopy(fixture)
        changed['members'][0][field] = value
        values.append(changed)
    changed = deepcopy(fixture)
    changed['groups']['energy']['tickers'] = ['UNKNOWN']
    values.append(changed)
    changed = deepcopy(fixture)
    changed['members'].append(dict(changed['members'][0], id='different-id'))
    values.append(changed)
    expected = []
    for config in values:
        try:
            validate(config)
        except ValueError:
            expected.append(False)
        else:
            expected.append(True)
    target = tmp_path / 'config-validator.js'
    target.write_text(script + '''
const fs = require('node:fs');
const values = JSON.parse(fs.readFileSync(0, 'utf8'));
const outcomes = values.map(value => {try {JSOSIFConfig.validateConfig(value); return true} catch {return false}});
process.stdout.write(JSON.stringify(outcomes));
''')
    result = subprocess.run([node, str(target)], input=json.dumps(values), capture_output=True,
                            text=True, check=True)
    assert json.loads(result.stdout) == expected
