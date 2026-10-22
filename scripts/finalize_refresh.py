"""Checkpoint an interrupted collection and determine publication from durable state."""
import argparse
from datetime import datetime, timezone
import os
from pathlib import Path

from report_store import read_json, write_json, persist


def finalize(root, *, business_date, workflow_run_id, outcome, git=False):
    root = Path(root)
    index = read_json(root / 'index.json', {})
    attempt = index.get('last_attempt', {})
    owned = bool(workflow_run_id and attempt.get('workflow_run_id') == workflow_run_id
                 and attempt.get('business_date') == business_date)
    if owned and attempt.get('status') == 'running':
        attempt['status'] = 'interrupted'
        attempt['interruption_reason'] = 'collector_' + outcome
        attempt['finished_at'] = datetime.now(timezone.utc).isoformat()
        attempt['pending_tickers'] = sorted(set(attempt.get('expected_tickers', [])) -
                                            set(attempt.get('successful_tickers', [])) |
                                            set(attempt.get('degraded_tickers', [])))
        write_json(root / 'index.json', index)
    # Never label a previous run as interrupted if this collector failed before
    # initialization or deliberately skipped its date through idempotency.
    persist(root, git=git)
    return {'publish': bool(owned and index.get('reports')), 'status': attempt.get('status', 'not_collected')}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--store', type=Path, required=True)
    parser.add_argument('--business-date', required=True)
    parser.add_argument('--workflow-run-id', default=os.environ.get('GITHUB_RUN_ID'))
    parser.add_argument('--outcome', required=True)
    parser.add_argument('--persist-git', action='store_true')
    args = parser.parse_args()
    result = finalize(args.store, business_date=args.business_date, workflow_run_id=args.workflow_run_id,
                      outcome=args.outcome, git=args.persist_git)
    print('publish=' + str(result['publish']).lower())
    print('status=' + result['status'])


if __name__ == '__main__':
    main()
