# Offline snapshot email (v1 / P0-1)

The delivery module reads existing reports only. It never refreshes data, invokes AI,
loads provider credentials, or sends mail. Real recipients are still pending.
`recipients.json` deliberately starts empty and fails validation until configured.
Use the reserved example address in `recipients.example.json` for offline previews.
Recipients must be a nonempty list of unique bare ASCII email addresses; display
names, header injection, and malformed addresses are rejected.

```bash
python3 scripts/email_delivery.py reports/ACN-intelligence-20261008.md \
  --recipients recipients.example.json --dry-run --output /tmp/acn-preview.eml
```

Omit `--output` to print the full MIME message to stdout. `--dry-run` is the default.
Pass multiple report paths to combine holdings into one email. Each path must use
`TICKER-intelligence-YYYYMMDD.md` or `.json`. Matching Markdown and JSON sidecars
are read together, and supplying both paths does not duplicate the holding.
Different snapshot dates remain explicit in the subject and each holding heading.
Missing sections render as N/A; conflicting report identities fail closed.

The frozen email order is date/holding, quant table, AI summary (status, tailwinds,
headwinds, catalysts, risks), assumptions/data freshness, and investment disclaimer.
HTML uses escaped text and an actual quant table. Plain text and HTML are carried
as `multipart/alternative`. No sender is invented: these are review artifacts,
not configured transport messages. Snapshot dates are retained, never replaced
with today's date. Missing assumption evidence is never represented as a pass.

`--send` immediately raises `NotImplementedError("发送需 Lucas 明确批准")`.
`DeliveryBackend.deliver(message)` is the pluggable backend contract;
`DryRunBackend` is the sole implemented backend. No automatic pipeline hook or
Gmail transport is enabled. Sending requires a later implementation and Lucas's
explicit approval of each message.

## Existing report chain

`run_phase1.py` runs quant, AI extraction, comparables, earnings, EDGAR and
`regenerate_report.py` for each holding, reusing FRED data. The report generator
writes a JSON sidecar containing ticker, as_of, assumptions_version and
assumptions_checked **before** preflight failure can stop Markdown generation.
JSON alone therefore does not contain quant or AI content or prove report success.
The email displays its checks and N/A for missing Markdown evidence.

Markdown sections are QUANTITATIVE, HOW TO READ THE QUANTITATIVE SECTION (when
metrics are available), TAILWINDS, HEADWINDS, CATALYSTS, RISKS, PEER COMPARABLES,
EARNINGS CALENDAR, MACRO (FRED), LATEST FILING (EDGAR), SOURCES, and Demo notes and
limitations. The header carries report, market and retained AI dates, market fetch
time, and AI availability. Email keeps the requested compact quant/AI view and
preserves those freshness caveats; it does not reclassify investment signals.

## Validation and teaching note

Tests were written first, observed failing without the module, then implemented.
The full offline suite includes archived verification tests; use the established
importlib mode to avoid duplicate archived module names:

```bash
PYTHONPATH=scripts .venv/bin/python -m pytest --import-mode=importlib -q
```

Separating report rendering from delivery makes the artifact reviewable before
any transport is added. Separate recipient configuration also means previews do
not need to read the pipeline configuration or any provider credentials.
