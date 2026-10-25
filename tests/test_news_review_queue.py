"""Blind stratified review export preserves exact source identities and safety."""
import csv
import json

import pytest

from build_news_review_queue import collect, sample, finalize


def write_snapshots(root, ticker, day, headline, prediction='tailwinds'):
    folder = root / day / ticker / 'sources'
    folder.mkdir(parents=True)
    prefix = ticker.lower() + '-'
    rss = [
        {'headline': headline, 'source': 'Synthetic News',
         'pubDate': 'Sat, 24 Oct 2026 12:00:00 GMT',
         'link': 'https://example.test/article'}
    ]
    ai = {'ticker': ticker, 'as_of': day,
          'tailwinds': [], 'headwinds': [], 'catalysts': [],
          'risks': [], 'unclassified': [], 'irrelevant': []}
    if prediction == 'irrelevant':
        ai['irrelevant'] = [{'headline': headline, 'reason': 'No target event'}]
    elif prediction == 'unclassified':
        ai['unclassified'] = [{'headline': headline, 'extraction_method': 'unknown'}]
    else:
        ai[prediction] = [{'headline': headline, 'extraction_method': 'rule',
                           'confidence': .8, 'event_type': 'market_move'}]
    (folder / (prefix + 'rss-items.json')).write_text(json.dumps(rss))
    (folder / (prefix + 'ai-intel.json')).write_text(json.dumps(ai))


def test_deterministic_blinded_review_queue_and_conversion(tmp_path):
    root = tmp_path / 'archive'
    write_snapshots(root, 'AAPL', '2026-10-24', 'Apple stock jumps')
    write_snapshots(root, 'V', '2026-10-24', 'Will Visa acquire a company?', 'unclassified')
    write_snapshots(root, 'SPGI', '2026-10-24', 'General industry discussion', 'irrelevant')
    # Same observed story on a second report date remains a distinct auditable snapshot.
    write_snapshots(root, 'AAPL', '2026-10-25', 'Apple stock jumps')
    first, second = tmp_path / 'first.csv', tmp_path / 'second.csv'
    assert len(collect(root)) == 4
    assert sample(root, count=4, seed='fixed', out=first) == 4
    assert sample(root, count=4, seed='fixed', out=second) == 4
    assert first.read_bytes() == second.read_bytes()
    with first.open(encoding='utf-8-sig', newline='') as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 4
    assert all(row['label'] == '' for row in rows)
    assert 'prediction' not in rows[0]
    for row in rows:
        row['label'] = 'insufficient_evidence' if '?' in row['headline'] else 'catalysts'
    with first.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    gold = tmp_path / 'gold.json'
    assert finalize(first, gold) == 4
    exported = json.loads(gold.read_text())
    assert len(exported) == 4
    assert sorted(row['as_of'] for row in exported).count('2026-10-24') == 3


def test_csv_formula_safe_and_exact_round_trip(tmp_path):
    root = tmp_path / 'archive'
    write_snapshots(root, 'V', '2026-10-24', '=HYPERLINK("bad")', 'unclassified')
    review = tmp_path / 'review.csv'
    sample(root, count=5, out=review)
    with review.open(encoding='utf-8-sig', newline='') as stream:
        rows = list(csv.DictReader(stream))
    assert rows[0]['headline'].startswith("'=")
    rows[0]['label'] = 'insufficient_evidence'
    with review.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    gold = tmp_path / 'gold.json'
    finalize(review, gold)
    assert json.loads(gold.read_text())[0]['headline'] == '=HYPERLINK("bad")'


def test_partial_review_skips_blank_labels(tmp_path):
    root = tmp_path / 'archive'
    write_snapshots(root, 'V', '2026-10-24', 'Visa stock falls')
    review = tmp_path / 'review.csv'
    sample(root, out=review)
    with pytest.raises(ValueError, match='No labeled rows'):
        finalize(review, tmp_path / 'gold.json')


def test_empty_sources_raise_clear_error(tmp_path):
    with pytest.raises(ValueError, match='No matching saved'):
        sample(tmp_path, out=tmp_path / 'empty.csv')
