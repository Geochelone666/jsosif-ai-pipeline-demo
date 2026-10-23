# Independent delivery with GitHub-only scheduling

Research collection can take hours. Holding the same writer queue for the whole
collection prevented due-member scans from starting. Senders now read an immutable
report checkout and persist only to the independent `delivery-state` branch.
Research and API reservations continue to use `report-data`.

| Work | Concurrency group | Writable branch |
| --- | --- | --- |
| Daily collection | `jsosif-report-data` | `report-data` |
| Weekly and internal email | `jsosif-email-delivery` | `delivery-state` |
| One-time ledger migration | Both groups | Both branches during cutover |

The quarter-hour cron remains configured. A completed, trusted main-branch daily
workflow also triggers a scan, so newly available reports can release deferred
digests without waiting for the next cron. The email switch, member opt-in,
start date, local weekly due time, report eligibility and duplicate guards apply
to every scan. A completion-triggered scan is not an instruction to email everyone.
Fork and non-main workflow runs cannot trigger this privileged delivery path.

GitHub schedule events and runner startup are still best effort. This change
removes the long research lock from normal delivery and adds a recovery trigger;
it does not establish exact-time delivery while GitHub is the only runtime.

## Guarded cutover

Merging the migration files into `main` starts **Initialize independent delivery
ledger**. It can also be dispatched manually from `main`. It sends no email and
does not read the member configuration or Gmail credentials.

1. The migration holds both concurrency groups, then checks that no sender from
   an older source revision is active or queued. If blocked, let those runs finish
   or cancel only the old **Weekly member PDF delivery** and **Internal email
   acceptance** runs, then rerun the migration from current `main`.
2. It validates every legacy reservation and copies the complete ledger into
   `delivery-state`. Accepted, sending and uncertain records are all retained.
   Unexpected private fields, damaged state or missing files stop the cutover.
3. It pushes the independent ledger and a manifest containing the original Git
   commit and hashed seed keys. Only after that push succeeds does it retire the
   legacy state in `report-data`: `state/deliveries.json` becomes JSON `null`, and
   `state/delivery-migration.json` points to the new branch and seed commit.
   The original ledger remains available at that commit and in the new branch.
   Historical report and source files are unchanged.
4. A pre-cutover sender that reads the retired state fails before SMTP. New senders
   also refuse to send unless both stores agree that cutover completed. A missing
   independent ledger never becomes a fresh empty sending history.
5. Run **Weekly member PDF delivery** manually with `confirm=NO`. It validates the
   private configuration, report eligibility and migrated ledger without sending.
   Review the aggregate **Weekly delivery summary** notice. The existing delivery
   switch continues to control normal scheduled and completion-triggered sends.

The migration is idempotent: rerunning it does not reseed an existing ledger or
remove new reservations. If retirement of the legacy branch failed, it can resume
only while the legacy records still match the copied history. A difference stops
the cutover for reconciliation instead of overwriting either history.

Do not rerun pre-cutover sender revisions or roll back only one state branch.
Use current `main` for previews, migration and recovery.

## Duplicate safety and recovery

Before SMTP, the sender pushes a `sending` reservation to `delivery-state`.
Successful SMTP submission becomes `accepted`; an uncertain acknowledgement
becomes `unknown`. Sending and uncertain records block automatic resubmission.
Git rejects a stale writer before its SMTP call; conflicts are not force-pushed
or silently rebased. All production sender workflows share the same short queue.

Back up both state branches. Daily archive backups do not substitute for the
current delivery ledger. Sender artifacts contain only validated
`state/deliveries.json` and `state/migration.json`, retained for 30 days. Member
names, addresses, credentials and message bodies are excluded.

If a ledger or migration marker is damaged, stop and restore reviewed Git state
while preserving every potentially submitted message. Never reset the ledger to
an empty object. Reconcile uncertain records against actual mailbox evidence
before changing their status; SMTP acceptance alone does not prove inbox placement.

## Validation without sending

The regression suite uses local bare Git remotes and a fake SMTP backend. It
checks interleaved research and sender pushes, preservation of migrated weekly
slots, restoration after an uncertain submission, stale-writer rejection before
SMTP, incomplete-cutover refusal, retirement recovery and prevention of private
fields in the public state branch. No live member email is needed for these tests.
