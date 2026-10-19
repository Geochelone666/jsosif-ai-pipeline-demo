#!/usr/bin/env python3
"""Run extraction, report packaging, and an offline email preview in order."""
import argparse
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--recipients', type=Path, default=ROOT / 'recipients.json',
                        help='Recipient JSON file (default: repository recipients.json)')
    parser.add_argument('--really-send', action='store_true',
                        help='Reserved guard; real delivery is disabled in v1')
    args = parser.parse_args(argv)
    if args.really_send:
        parser.error('Real email delivery is disabled; this pipeline is dry-run only')
    recipients = args.recipients.resolve()
    original_cwd = Path.cwd()
    # Support both direct execution and importing scripts.run_all.
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    stage, name = 1, 'Quant + AI extract'
    try:
        print(f'STAGE {stage} START: {name}', flush=True)
        subprocess.run([sys.executable, 'scripts/run_phase1.py'], check=True, cwd=ROOT)
        print(f'STAGE {stage} DONE: {name}', flush=True)

        stage, name = 2, 'Report packaging'
        print(f'STAGE {stage} START: {name}', flush=True)
        from scripts.bundle_reports import bundle_reports

        os.chdir(ROOT)
        bundle_dir = Path(bundle_reports(reports_dir='reports', bundle_root='bundle'))
        if not bundle_dir.is_dir():
            raise ValueError('bundle_reports did not return an existing bundle directory')
        print(f'STAGE {stage} DONE: {name}', flush=True)

        stage, name = 3, 'Dry-run email rendering'
        print(f'STAGE {stage} START: {name}', flush=True)
        from scripts.email_delivery import DryRunBackend, build_email, load_recipients

        snapshots = sorted(path for path in bundle_dir.rglob('*')
                           if path.is_file() and re.fullmatch(
                               r'[A-Z0-9][A-Z0-9.-]*-intelligence-\d{8}\.(md|json)',
                               path.name))
        # build_email deduplicates Markdown/JSON pairs; no preview files accumulate.
        message = build_email(snapshots, load_recipients(recipients))
        print('DRY-RUN: Would send the following email (no mail is sent):', flush=True)
        DryRunBackend().deliver(message)
        print(f'\nSTAGE {stage} DONE: {name}', flush=True)
    except Exception as exc:
        print(f'STAGE {stage} FAILED ({name}): {exc}', file=sys.stderr)
        return 1
    finally:
        os.chdir(original_cwd)
    return 0


if __name__ == '__main__':
    sys.exit(main())
