#!/usr/bin/env python3
"""Create a blinded, stratified human news-label queue from saved RSS/AI snapshots.

No network, subscriptions, mail, inference, or automatic truth labels.
Predictions are used only to balance sampling; reviewers do not see them.
"""
import argparse
from collections import defaultdict
import csv
import hashlib
import json
from pathlib import Path

from eval_news_classification import GOLD_LABELS, load_gold

COLUMNS = ('ticker', 'headline', 'pubDate', 'source', 'link', 'as_of', 'label')


def _protect_csv(value):
    """Prevent a scraped headline or publisher being evaluated as a spreadsheet formula."""
    text = str(value or '')
    return "'" + text if text.lstrip().startswith(('=', '+', '-', '@')) else text


def _unprotect_csv(value):
    return value[1:] if value.startswith("'") and value[1:].lstrip().startswith(('=', '+', '-', '@')) else value


def collect(root):
    """Collect an intact mapping between exact RSS titles and saved class decisions."""
    output, seen = [], set()
    for ai_path in sorted(Path(root).rglob('*-ai-intel.json')):
        ai = json.loads(ai_path.read_text(encoding='utf-8'))
        ticker, as_of = ai.get('ticker'), ai.get('as_of')
        stem = ai_path.name[:-len('ai-intel.json')]
        rss_path = ai_path.with_name(stem + 'rss-items.json')
        if not isinstance(ticker, str) or not isinstance(as_of, str) or not rss_path.is_file():
            continue
        rss = json.loads(rss_path.read_text(encoding='utf-8'))
        if not isinstance(rss, list):
            continue
        classes = {}
        for category in ('tailwinds', 'headwinds', 'catalysts', 'risks', 'unclassified'):
            for item in ai.get(category, []):
                if not isinstance(item, dict) or not isinstance(item.get('headline'), str):
                    continue
                method = item.get('extraction_method') or category
                classes[item['headline']] = str(method) + ':' + category
        for item in ai.get('irrelevant', []):
            if isinstance(item, dict) and isinstance(item.get('headline'), str):
                classes[item['headline']] = 'irrelevant'
        for item in rss:
            if not isinstance(item, dict):
                continue
            headline = item.get('headline')
            published = item.get('pubDate')
            if not isinstance(headline, str) or not headline.strip():
                continue
            if not isinstance(published, str) or not published.strip():
                continue
            identity = (ticker, as_of, headline, published)
            if identity in seen:
                continue
            seen.add(identity)
            row = {key: item.get(key, '') for key in ('headline', 'pubDate', 'source', 'link')}
            row.update(ticker=ticker, as_of=as_of, label='')
            output.append((classes.get(headline, 'missing_prediction'), row))
    return output


def sample(root, *, count=300, seed='2026', out):
    if type(count) is not int or count < 1:
        raise ValueError('count must be a positive integer')
    buckets = defaultdict(list)
    for prediction, row in collect(root):
        buckets[(prediction.split(':', 1)[0], row['ticker'])].append(row)
    if not buckets:
        raise ValueError('No matching saved RSS/AI headline pairs found')
    for key, rows in buckets.items():
        rows.sort(key=lambda row: hashlib.sha256(
            (seed + '\x1f' + row['ticker'] + '\x1f' + row['headline'] + '\x1f' +
             row['pubDate']).encode('utf-8')).hexdigest())
    result = []
    groups = sorted(buckets)
    # One item from each ticker/prediction class per round: no long single-ticker run.
    while len(result) < count:
        progressed = False
        for group in groups:
            if buckets[group]:
                result.append(buckets[group].pop(0))
                progressed = True
                if len(result) == count:
                    break
        if not progressed:
            break
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('w', newline='', encoding='utf-8-sig') as stream:
        writer = csv.DictWriter(stream, fieldnames=COLUMNS)
        writer.writeheader()
        for row in result:
            writer.writerow({k: _protect_csv(row.get(k, '')) for k in COLUMNS})
    return len(result)


def finalize(review_csv, gold_json):
    """Convert independent human labels to evaluation input; blanks stay unreviewed."""
    with Path(review_csv).open(newline='', encoding='utf-8-sig') as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or not set(COLUMNS).issubset(reader.fieldnames):
            raise ValueError('Review CSV lacks required columns')
        rows = []
        for n, row in enumerate(reader, 2):
            label = (row.get('label') or '').strip()
            if not label:
                continue  # Human review may proceed incrementally.
            if label not in GOLD_LABELS:
                raise ValueError(f'Row {n}: invalid human label {label!r}')
            rows.append({key: _unprotect_csv(row.get(key) or '')
                         for key in COLUMNS})
    if not rows:
        raise ValueError('No labeled rows are ready for evaluation')
    out = Path(gold_json)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(load_gold_from_rows(rows), ensure_ascii=False,
                              indent=2) + '\n', encoding='utf-8')
    return len(rows)


def load_gold_from_rows(rows):
    """Validate the same invariants as load_gold without temporary files."""
    used = set()
    for row in rows:
        if row['label'] not in GOLD_LABELS:
            raise ValueError('Invalid human label')
        if not all(row.get(key) and isinstance(row[key], str)
                   for key in ('ticker', 'headline', 'pubDate')):
            raise ValueError('Incomplete headline identity')
        ident = (row['ticker'], row['headline'], row['pubDate'])
        if ident in used:
            raise ValueError('Duplicate reviewed headline identity')
        used.add(ident)
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='command', required=True)
    s = sub.add_parser('sample')
    s.add_argument('--root', required=True, type=Path)
    s.add_argument('--count', type=int, default=300)
    s.add_argument('--seed', default='2026')
    s.add_argument('--out', required=True, type=Path)
    f = sub.add_parser('finalize')
    f.add_argument('--review-csv', required=True, type=Path)
    f.add_argument('--gold-json', required=True, type=Path)
    args = parser.parse_args(argv)
    if args.command == 'sample':
        print(json.dumps({'review_rows': sample(args.root, count=args.count,
                                                seed=args.seed, out=args.out)}))
    else:
        print(json.dumps({'gold_rows': finalize(args.review_csv, args.gold_json)}))


if __name__ == '__main__':
    main()
