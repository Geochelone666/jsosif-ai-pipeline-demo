"""Select one daily Toronto evening run across standard/daylight saving time."""
import argparse
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo


def decision(event, now=None, cron=None):
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        raise ValueError('Scheduled time must be timezone-aware')
    selected = now
    if event == 'schedule' and cron is not None:
        if cron not in ('0 23 * * *', '0 0 * * *'):
            raise ValueError('Unknown daily schedule')
        # Use the trigger instant, not the worker start hour: Actions can queue.
        selected = now.astimezone(timezone.utc).replace(
            hour=int(cron.split()[1]), minute=0, second=0, microsecond=0)
        if selected > now:
            selected -= timedelta(days=1)
    local = selected.astimezone(ZoneInfo('America/Toronto'))
    return {'run': event != 'schedule' or local.hour == 19,
            'business_date': local.date().isoformat()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--event', choices=('schedule', 'workflow_dispatch'), required=True)
    parser.add_argument('--cron')
    args = parser.parse_args()
    result = decision(args.event, cron=args.cron or None)
    print('run=' + str(result['run']).lower())
    print('business_date=' + result['business_date'])


if __name__ == '__main__':
    main()
