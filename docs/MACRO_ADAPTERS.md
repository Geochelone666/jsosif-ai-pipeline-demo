# Shared macro adapters and source integrity

## Bank of Canada candidate

boc_macro.py implements the public Valet FXUSDCAD observation envelope and a
bounded shared cache. FXUSDCAD is quoted CAD per USD; observation dates are not
publication times. Output includes the requested window, retrieval time, public
source reference, raw response digest and explicit missing cells. It does not
forward-fill holidays, invent missing quotes or infer a publication timestamp.

```bash
python scripts/boc_macro.py --start 2026-11-02 --end 2026-11-06 \
  --cache /private/local/cache/boc --output /private/local/boc-usd-cad.json
```

One provider request is made for a cache miss; there are no automatic HTTP retries.
An exclusive process lock merges identical concurrent windows. Successful payloads
are reparsed from cached raw content and reused for one hour. Failed requests
receive at least 60 seconds of backoff, extended by a valid Retry-After value.
Cache keys bind schema/series/window. Malformed caches are refetched. Cache hashes
check local consistency, not provider signatures or independent truth. Invalid
responses and transport failures produce sanitized categories without raw errors.
No API key is required by this public adapter. TLS and redirect verification stay
in force. Cache files are local performance state, not immutable report history.

The former cloud environment could not reach the official API. On 2026-11-14,
the local CLI successfully fetched the requested 2026-11-02 through 2026-11-06
window, containing five observed business-day values. The captured provider
metadata identifies USD/CAD as Canadian dollars per US dollar, business daily.
The same cached payload replayed without a second network call. A public captured
fixture now joins the synthetic failure fixtures, with capture time, exact URL
and canonical JSON SHA-256. `raw_sha256` is the digest of the canonical parsed
payload, not a claim to hash the original HTTP bytes or authenticate the provider.
Explicit contradictory series units, date dimension or frequency now fail closed.

This is acceptance of one series/window and the local cache contract, not broad
coverage or a long-running availability assessment. This CLI is not
enabled in scheduled production, does not feed automatic FX conversion, and does
not claim Bank of Canada observation coverage on the public site. Validate the
actual endpoint and reviewed series semantics before activation. Source failure
is represented independently and must not block stock collection when integrated.

## Archive-source integrity correction

The newer stock archive already records source_sha256 for eight source files.
The site builder previously projected the public index before verifying entries,
which dropped those expected hashes. A regression proved that a modified FRED
file could reach the optional research projection. The builder now verifies the
original archive entry before publication and passes original expected hashes to
the shared dataset. The dataset hashes the same bounded bytes that it parses and
checks available expected hashes. Corruption aborts site replacement. Public index
metadata remains allowlisted; expected source metadata need not be exposed there.

Legacy archives without expected source hashes remain readable, with provenance
explicitly labelled build-observed. New verified sources receive the distinct
verified-against-expected label. Optional absence remains missing; a tracked
integrity mismatch is not downgraded into a recoverable optional-source gap.
No historical report was changed or expected checksum weakened by this fix.

## Remaining work

FRED continues through the existing collector. Canonical cache/history integration,
additional BoC series/window validation, approved series catalogues, aligned currency conversion,
sector benchmark collectors, industry KPI observations and Sector Weekly Brief
assembly remain distinct delivery items. No current macro/sector readiness claim
is justified merely by a passing parser test.
