# News classifier quality: an offline, human-grounded evaluation protocol

The pipeline's fixed rule confidence (0.8) and Groq-returned confidence (0–1)
are **not calibrated correctness probabilities**. Neither CI fixture pass rate
nor the fraction of headlines processed proves classification accuracy.

## Collect ground truth

1. Stratify at least 200–400 headlines across tickers, publication dates,
   sectors, event types, publisher types, rule-accepted cases, Groq-accepted
   cases, irrelevant headlines and unresolved headlines. Sample from *raw
   archived RSS items* before looking at model results, not just PDF sections.
2. Two independent reviewers inspect the original dated article when accessible
   and label each case as `tailwinds`, `headwinds`, `catalysts`, `risks`,
   `irrelevant`, or `insufficient_evidence`. A speculative headline without
   a verified factual event must **not** be forced into a positive or negative
   bucket. Review disagreements and keep the adjudicated label separately.
3. Keep sampling dates and listing identity. Do not mark a competitor event as
   a target-company event. For an ongoing lawsuit/acquisition, label the
   reported event separately from its current unresolved status.
4. Keep real member contact details out of gold files, CLI output and public
   repositories. Use offline local files for human labels.
5. Hold out at least one chronological future sample and freeze the label
   definitions *before* tuning regexes or model prompts. Avoid measuring on
   the same manually constructed regression cases that were used to fix rules.

## Build a blinded review set from an archived report run

In a **local clone of the report-data branch**, the archived source files
appear under `archive/<run-id>/<ticker>/sources/*-ai-intel.json` and
`*-rss-items.json`. They must not be regenerated or classified again.

```bash
python scripts/build_news_review_queue.py sample \
    --root /path/to/report-data/archive/<run-id> \
    --count 300 --seed 20261025 \
    --out /private/news-review.csv
```

The sampled queue is stratified across tickers and observed rule/AI/unknown/
irrelevant decisions, but the CSV **does not reveal the predictions**. Open
and label the `label` column independently using the accepted values above,
after checking the article. The exporter neutralizes spreadsheet formula
prefixes and restores original headline text during conversion.

```bash
python scripts/build_news_review_queue.py finalize \
    --review-csv /private/news-review.csv \
    --gold-json /private/news-gold.json
python scripts/eval_news_classification.py --gold /private/news-gold.json
```

Unlabeled rows remain pending; the converter includes only manually labeled
cases. Use fresh blind review and a chronological holdout to estimate actual
accuracy, rather than treating the curated CI regression fixtures as a valid
random sample. Keep review CSV and gold JSON in **private storage**.

## Run

```bash
python scripts/eval_news_classification.py --gold local-private-gold.json
python scripts/eval_news_classification.py --gold local-private-gold.json \
    --snapshots saved-acn-ai-intel.json saved-v-ai-intel.json
```

Gold file format: a nonempty JSON array, with one object per observed headline:

```json
[
  {
    "ticker": "SPGI",
    "headline": "SPGI Gears Up to Report Q3 Earnings",
    "pubDate": "Fri, 23 Oct 2026 12:00:00 GMT",
    "source": "Sample publication",
    "link": "https://example.org/sample",
    "as_of": "2026-10-24",
    "label": "catalysts"
  }
]
```

Gold labels must be **independent human judgments**, not re-used rule or
AI predictions. The listed example is a structural illustration, *not* a
validated gold set.

Outputs distinguish:

- **Selective precision** = correct *classified* / all classified. Incorrect
  company event claims on truly irrelevant or insufficient-evidence headlines
  reduce precision.
- **Coverage on labelable cases** = classified / human-labelable items.
- **Correct abstentions** = withholding conclusions on material that independent
  reviewers say is insufficient to classify.
- **False company events on irrelevant items** = clearly unrelated headlines
  incorrectly promoted into company-specific research.
- **Observed pipeline** = recorded rule+AI decisions on the matched dated
  snapshot; **AI candidate subset** = only the items the current rule classifier
  abstains on. It is *not* a randomized direct head-to-head model comparison.

Do not target 100% coverage by forcing all stories into a bucket. After a
representative holdout exists, compare versions on selective precision,
coverage, irrelevant false positives and token/cost budget together. The
initial goal of >=95% rule precision is a **proposed acceptance threshold**, not
a historical measurement. Consider 95% confidence intervals and per-ticker
worst cases rather than one pooled rate; abstention is permitted.
