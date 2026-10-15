#!/usr/bin/env python3
"""Run team report distribution daily at 09:00 America/Toronto."""
import argparse
from datetime import datetime, timedelta, timezone
import fcntl
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import subprocess
import sys
import time
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
TORONTO = ZoneInfo('America/Toronto')
LOGGER = logging.getLogger('jsosif.scheduler')


def next_run(now=None):
    """Return the next strictly future 09:00 in Toronto (aware input required)."""
    now = datetime.now(timezone.utc) if now is None else now
    if now.tzinfo is None or now.utcoffset() is None:
        raise ValueError('now must be timezone-aware')
    local = now.astimezone(TORONTO)
    target = local.replace(hour=9, minute=0, second=0, microsecond=0)
    if target <= local:
        target += timedelta(days=1)
    return target


def seconds_until_next_run(now=None):
    now = datetime.now(timezone.utc) if now is None else now
    # Timestamp subtraction measures elapsed seconds across DST changes.
    return next_run(now).timestamp() - now.timestamp()


def run_once(lock_path):
    """Hold a kernel-managed file lock until the child finishes; never log secrets."""
    try:
        lock_path = Path(lock_path)
        lock_path.parent.mkdir(parents=True, exist_ok=True)
        with lock_path.open('a') as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                LOGGER.warning('Distribution skipped: another run holds the lock')
                return False
            # Keep the lock inode: unlinking it would allow overlapping owners.
            LOGGER.info('Distribution started')
            result = subprocess.run(
                [sys.executable, str(ROOT / 'scripts/distribute_team_reports.py'), '--send'],
                cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                pass_fds=(lock.fileno(),),
            )
            if result.returncode:
                LOGGER.error('Distribution failed (exit code %s)', result.returncode)
                return False
            LOGGER.info('Distribution completed')
            return True
    except Exception as exc:
        LOGGER.error('Distribution failed (%s)', type(exc).__name__)
        return False


def daemon(lock_path):
    while True:
        try:
            now = datetime.now(timezone.utc)
            target = next_run(now)
            LOGGER.info('Next distribution: %s', target.isoformat())
            time.sleep(seconds_until_next_run(now))
            run_once(lock_path)
        except Exception as exc:
            LOGGER.error('Scheduler error (%s); retrying in 60 seconds', type(exc).__name__)
            time.sleep(60)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--once', action='store_true', help='Send once immediately')
    mode.add_argument('--daemon', action='store_true', help='Stay running and send daily')
    mode.add_argument('--dry-run', action='store_true', help='Print next run and delay; do not send')
    parser.add_argument('--lock-file', type=Path, default=ROOT / 'logs/distribution.lock')
    parser.add_argument('--log-file', type=Path, default=ROOT / 'logs/scheduler.log')
    args = parser.parse_args(argv)
    if args.dry_run:
        now = datetime.now(timezone.utc)
        print(f'Next run: {next_run(now).isoformat()} | sleep seconds: {seconds_until_next_run(now):.3f}')
        return 0
    args.log_file.parent.mkdir(parents=True, exist_ok=True)
    handler = RotatingFileHandler(args.log_file, maxBytes=2_000_000, backupCount=3)
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    LOGGER.addHandler(handler)
    LOGGER.setLevel(logging.INFO)
    try:
        if args.once:
            return 0 if run_once(args.lock_file) else 1
        daemon(args.lock_file)
    except KeyboardInterrupt:
        LOGGER.info('Scheduler stopped')
    finally:
        LOGGER.removeHandler(handler)
        handler.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
