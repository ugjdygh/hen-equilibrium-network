# Web archive record

Purpose: snapshot the **public web surface** of the project, so that what a reader saw on a given day can be shown later even if the repository is renamed, made private or deleted.

This is **supplementary**. The authoritative evidence is the git tag plus hashes plus RFC 3161 receipts in [`finalization.md`](finalization.md) — those do not expire and do not depend on any archive service. A page snapshot proves a rendering, not the bytes behind it.

## 1. Batch

- Machine list: [`web-archive-urls.txt`](web-archive-urls.txt) — 23 URLs, priority `P0` (8) / `P1` (10) / `P2` (5), tab-separated.
- Upload form: [`web-archive-batch.csv`](web-archive-batch.csv) — same list as `priority,url,label`, for services that accept a CSV.
- Submit: `python3 tools/archive_batch.py` (appends this file), or `--limit 5` for a partial run, or `--dry-run` to just print the batch.

`P0` is the minimum that must exist: repository root, `VERIFY.md`, `finalization.md`, the hash manifest, release `v1.0`, both whitepaper editions, name clearance. If only five snapshots are affordable, take those.

## 2. Choosing a service — the one-year problem

Free tiers differ mainly in **how long a snapshot is kept**, which is the only property that matters here.

| Service | Cost | Retention | Login | Notes |
|---|---|---|---|---|
| Internet Archive (Save Page Now) | free | no stated expiry; snapshots are kept indefinitely in practice | none | slow, rate-limited, sometimes returns 503; no SLA and no guarantee — treat as best-effort |
| archive.today | free | no stated expiry | none | CAPTCHA per submission; poor for scripted batches |
| Domestic "web evidence" / notary platforms, free tier | free | **typically 12 months**, paid to extend | usually phone + real name | the 1-year limit you mentioned; the certificate is the product, not the snapshot |
| Paid archive/notary plans | USD 50–500/yr | 3–10 years or permanent | real name | only worth it if a dispute is foreseeable |

**Recommendation**: use Internet Archive as the primary (free, no expiry, no identity), and if a domestic platform is used for its certificate, treat its 12-month window as a **renewal obligation**, not a one-off task. Do not let a 1-year free tier be the only copy of anything.

Note on anonymity: platforms that need a phone number and real name for the certificate will link the deposit to a natural person, which undoes the pen name. Internet Archive needs neither.

## 3. Network limitation, stated

Attempted from this environment on 2026-11-23: `https://web.archive.org/save/...` returned **HTTP 503** for every URL (the sandbox has no route to the archive endpoints), so **no snapshot was actually created here**. The batch and the script are ready; the submission has to run from a normal network:

```bash
python3 tools/archive_batch.py --limit 5     # first the P0 set
python3 tools/archive_batch.py               # then the rest
```

Manual fallback, no script: paste a URL into `https://web.archive.org/save/`, one at a time, five P0 pages first.

## 4. Snapshot log

| Date | Priority | Page | Snapshot | Status |
|---|---|---|---|---|
| 2026-11-23 | P0 | repository root | — | attempted, 503, not created |
| 2026-11-23 | P0 | `VERIFY.md` | — | attempted, 503, not created |

Rows are appended by the script as snapshots succeed. An empty table means "not yet done", not "done".

## 5. Renewal

- **Once a year, in November**, re-archive the eight `P0` URLs, plus the current release page, so the record is continuous rather than a single point.
- Re-archive immediately after any of: a rename, a release, a change to `CLA.md` or `DISCLAIMER.md`, or the first real external citation.
- Keep every previous snapshot URL in this table. Deleting old rows is what makes a record contestable.
