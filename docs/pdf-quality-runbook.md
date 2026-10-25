# PDF research report quality acceptance

Every report is rendered from saved research source snapshots using ReportLab.
Before the version is archived, the pipeline validates the generated PDF
with the pinned pure-Python `pypdf` reader.

The preflight checks:

- The bytes represent an extractable, nonencrypted PDF with A4 portrait pages.
- Every page has extractable body text; total pages stay below a safety cap.
- Core section titles, the correct ticker and report date, all six newer risk
  dimensions and all five fundamental dimensions are present.
- A research/source documentation link is clickable.
- Embedded URI actions permit **HTTPS only**, no credentials in URL and no
  control characters. Untrusted RSS links with unsupported protocols become
  plain text instead of executable or local-file actions.

Any preflight failure aborts the archive step and preserves the previously
known-good report. Existing release and email checksums remain mandatory.

## Run locally

```bash
python scripts/report_pdf.py --ticker AAPL
python scripts/pdf_quality.py --pdf reports/AAPL-intelligence-20261024.pdf \
  --ticker AAPL --as-of 2026-10-24
```

## Evidence limits

This is a **machine-readable structural test**, not a visual pixel/typographic
review. It cannot establish that page breaks, cell padding or cross-page text
flow looks attractive, nor that source articles are true. Review a representative
PDF at 100% scale (dense news, empty news, very long issuer names, 0/25 stories,
French/Canadian listings) before presenting this as final visual QA. Automated
CI includes real synthetic full-pipeline PDF generation and structural checks.
Old archived PDFs remain immutable.
