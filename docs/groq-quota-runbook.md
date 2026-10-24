# Groq quota and backup-model operations

The JSOSIF research job defaults to `openai/gpt-oss-20b`. The organization limits
confirmed on 2026-10-24 were **1,000 RPD, 30 RPM, 8,000 TPM, 200,000 TPD**
for both `openai/gpt-oss-20b` and `openai/gpt-oss-120b`. Project-specific
limits may be *lower*. Confirm the project's actual limits in the Groq console
before changing application budgets; never set local caps higher than actual
limits.

## Why daily requests fail below 1,000

The application records both request reservations and token usage for each
model and UTC day in the private `report-data` branch's
`state/api-usage.json`. Either the token or request budget can be exhausted.
The production report on 2026-10-24 shows nearly 200,000 tokens reserved while
fewer than 200 calls were made. Separate preflight headroom is recorded in
`index.json.refresh_plan` and in the daily workflow summary. This local state
is conservative accounting, **not** a live API quota query.

Avoid repeated `force` runs: even failed or degraded attempts may consume
requests, output tokens and time. `resume` reuses only ready and integrity
verified reports; it does **not** reuse degraded AI decisions or refund quota.

## Optional same-provider model fallback

Set GitHub Actions **repository variable**, not secret,
`GROQ_FALLBACK_MODEL=openai/gpt-oss-120b` to enable fallback. Omit or clear it
to disable. Both models use the **same Groq API key** and strict-schema
interface. `qwen/qwen3.8-27b` is also permitted if enabled in the project.

Fallback only happens after a **local application daily request/token budget**
exception on the primary model. HTTP 429, 401, invalid schemas, network
failures or unknown errors **never** trigger fallback. Provider-side limits
still win, and strict release quality gates still block incomplete data.
The model(s) actually used are recorded with each AI source result. Different
models can generate different editorial classifications; test a sample and
review source-grounding before enabling fallback for the member pipeline.

Do not automatically rerun production or send emails while changing this
setting. Verify offline CI first and conduct a deliberately controlled
production recovery with deliverability and duplicate-email checks.

Official references:
- https://console.groq.com/docs/rate-limits
- https://console.groq.com/docs/structured-outputs
- https://console.groq.com/docs/projects
