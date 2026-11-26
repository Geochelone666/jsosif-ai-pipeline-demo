from copy import deepcopy
import json
from pathlib import Path
import stat
import subprocess
import sys

import pytest

from subscription_migration import prepare_plan, review_sql, write_review


@pytest.fixture
def inputs():
    config = {'groups': {'tech': {'name': 'Technology', 'tickers': ['CSCO']}},
              'allow_degraded': False, 'max_report_age_days': 4,
              'members': [{'id': 'legacy-unchanged', 'name': "Analyst's \\ example",
                           'email': 'example@example.com', 'enabled': False,
                           'timezone': 'America/Toronto', 'send_weekday': 1,
                           'send_time': '09:00', 'groups': ['tech'], 'tickers': [],
                           'delivery_start_date': '2026-12-01',
                           'content_preferences': {'sector_brief': False, 'macro_overview': True}}]}
    identities = [{'member_id': 'legacy-unchanged', 'user_id': '00000000-0000-0000-0000-000000000001',
                   'email': 'example@example.com', 'approved': True}]
    return config, identities


def test_preserves_identity_pause_start_and_content_without_mutating_source(inputs):
    config, identities = inputs
    original = deepcopy(inputs)
    plan = prepare_plan(config, identities, 7)
    row = plan['members'][0]
    assert row['member_id'] == 'legacy-unchanged' and row['user_id'] != row['member_id']
    assert row['preferences']['enabled'] is False
    assert row['preferences']['delivery_start_date'] == '2026-12-01'
    assert row['preferences']['content_preferences'] == config['members'][0]['content_preferences']
    assert inputs == original
    sql = review_sql(plan)
    assert sql.endswith('rollback;\n') and '\ncommit;' not in sql.lower()
    assert 'delivery_state' not in sql and 'delivery_ledger' not in sql


@pytest.mark.parametrize('change', [
    lambda c, i: i.clear(),
    lambda c, i: i.append(deepcopy(i[0])),
    lambda c, i: i[0].update(email='other@example.com'),
    lambda c, i: i[0].update(user_id='not-a-uuid'),
    lambda c, i: i[0].update(approved='true'),
    lambda c, i: i[0].update(member_id='renamed-id'),
    lambda c, i: c['members'][0].update(feedback='Must not discard this'),
    lambda c, i: c['members'][0].update(preferred_frequency='monthly'),
    lambda c, i: c['members'][0].update(content_preferences='macro'),
    lambda c, i: c['members'][0].update(content_preferences={'unknown': True}),
    lambda c, i: c['members'][0].update(content_preferences={'sector_brief': 'yes'}),
    lambda c, i: c['members'][0].update(name='x' * 201),
    lambda c, i: c.update(_subscription_authority={}),
])
def test_rejects_ambiguous_or_lossy_mapping(inputs, change):
    config, identities = inputs
    change(config, identities)
    with pytest.raises(ValueError):
        prepare_plan(config, identities, 1)


def test_duplicate_auth_identity_cannot_merge_two_legacy_members(inputs):
    config, identities = inputs
    config['members'].append(dict(config['members'][0], id='other-id', email='other@example.com'))
    identities.append(dict(identities[0], member_id='other-id', email='other@example.com'))
    with pytest.raises(ValueError, match='Duplicate'):
        prepare_plan(config, identities, 1)


@pytest.mark.parametrize('revision', [0, -1, True, '1', 2**63 - 1])
def test_revision_is_explicit_and_bounded(inputs, revision):
    with pytest.raises(ValueError):
        prepare_plan(*inputs, revision)


def test_private_new_file_and_no_overwrite_or_symlink(tmp_path):
    output = tmp_path / 'private.sql'
    write_review(output, 'first')
    assert stat.S_IMODE(output.stat().st_mode) == 0o600
    with pytest.raises(FileExistsError):
        write_review(output, 'overwrite')
    link = tmp_path / 'link.sql'
    link.symlink_to(output)
    with pytest.raises(FileExistsError):
        write_review(link, 'overwrite')
    assert output.read_text() == 'first'


def test_cli_sanitizes_invalid_private_input(tmp_path, inputs):
    config, identities = inputs
    config['members'][0]['groups'] = ['PRIVATE_GROUP_MUST_NOT_LEAK']
    source = tmp_path / 'config.json'; source.write_text(json.dumps(config))
    mapping = tmp_path / 'map.json'; mapping.write_text(json.dumps(identities))
    result = subprocess.run([sys.executable, 'scripts/subscription_migration.py',
                             '--config', str(source), '--identities', str(mapping),
                             '--expected-revision', '1', '--output', str(tmp_path / 'review.sql')],
                            capture_output=True, text=True)
    assert result.returncode != 0
    assert 'PRIVATE_GROUP_MUST_NOT_LEAK' not in result.stderr
    assert 'example@example.com' not in result.stderr
    assert not (tmp_path / 'review.sql').exists()


def test_cli_csv_review_preserves_pause_and_never_changes_sources(tmp_path, inputs):
    config, identities = inputs
    source = tmp_path / 'config.json'; source.write_text(json.dumps(config))
    mapping = tmp_path / 'map.json'; mapping.write_text(json.dumps(identities))
    csv = tmp_path / 'roster.csv'
    csv.write_text('id,name,email,groups,enabled,timezone,send_weekday,send_time\n'
                   'legacy-unchanged,Example,example@example.com,tech,false,America/Toronto,1,09:00\n')
    original = [p.read_bytes() for p in (source, mapping, csv)]
    output = tmp_path / 'review.sql'
    result = subprocess.run([sys.executable, 'scripts/subscription_migration.py',
                             '--config', str(source), '--members-csv', str(csv),
                             '--identities', str(mapping), '--expected-revision', '1',
                             '--output', str(output)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert 'example@example.com' not in result.stdout
    assert '"enabled": false' in output.read_text()
    assert output.read_text().endswith('rollback;\n')
    assert stat.S_IMODE(output.stat().st_mode) == 0o600
    assert [p.read_bytes() for p in (source, mapping, csv)] == original
