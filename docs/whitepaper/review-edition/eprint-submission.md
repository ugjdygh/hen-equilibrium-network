# Submitting the review edition

Target: **Cryptology ePrint Archive** (eprint.iacr.org). It accepts design documents without code, assigns a permanent report number, and is citable — which is why it is worth doing before any mailing list.

## 1. Fields

| Field | Value |
|---|---|
| Title | `Horizon Equilibrium Network: a coupled design for circulation, ordering and conditionable privacy` |
| Authors | Lee Hyun seok (single author, research byline) |
| Category | `Cryptographic protocols` (fallback: `Applications`) |
| Keywords | `consensus`, `privacy`, `commitments`, `range proofs`, `parameter control`, `ledger design` |
| Comments | `Design document. No implementation, no network, no asset. Whitepaper text frozen at v1.0; hashes and RFC 3161 timestamps recorded in the repository.` |
| Licence | CC-BY if offered; otherwise the most permissive option available, to stay consistent with the repository's MIT |
| PDF | `hen.pdf` (4 pages, two-column, numbered sections, abstract) — built with `tools/build_paper.sh`; the 7-page narrative version stays as `HEN-review-edition.pdf` |

## 2. Abstract (paste as-is)

> This note describes a ledger design that treats four properties as one coupled problem: permissionless ordering whose cost is not purchasable, privacy that is switchable per output rather than absolute, an issuance curve that converges instead of decaying toward fee-only security, and parameter adaptation that is bounded and delay-tolerant. Ordering uses proof of work as a cost anchor together with a verification weight derived from elapsed time and observable behaviour, with three prohibitions: holdings never determine block rights, weight cannot be bought or transferred, and no single entity may hold a de facto veto. Privacy is per-output and visible: transparent, shielded (commitments with range proofs, one-time addresses, mixing at the validating layer), and selective, where the disclosure key is held by the holder rather than by the protocol. Conditional transfers use a minimal script set with default-deny semantics, so a failed condition leaves an output locked instead of spendable. Difficulty control is bounded by static limits, per-step caps and a breaker triggered on cumulated amplitude within a time window; the earlier counting-based rule fails a reproducible step test (target 13.31 against 18.00 required) while the windowed rule converges (18.00, oscillation band 5.56-10.61), and a 42-setting sweep converges in 35. No cryptographic primitive is new. No formal proofs are offered, no implementation exists, and no asset is issued.

## 3. What eprint will and will not settle

- It will **not** certify correctness. A report number means "this document is archived and citable", nothing more.
- It does check for **scope and minimal technical content**; a document that is mostly policy prose can be returned. This edition is organised to survive that check: threat model, construction, claims table, comparison, open problems.
- **Byline**: archives normally require an author name they can correspond with. A pen name has been tolerated in practice but is not guaranteed; if a submission is questioned, the archive may ask for identity verification. This is the same trade-off as everywhere else — a pen name buys distance, not immunity. If verification is requested and refused, expect the submission to be withdrawn, not argued with.

## 4. Order of operations

1. Submit the review edition here. Wait for the report number (days, sometimes longer).
2. Post the mailing-list mail (`docs/outreach/cryptography-list-post.md`) **pointing at the eprint number**, not at GitHub. It reads as research rather than as a repository.
3. Record the report number in `docs/legal/finalization.md` §5 alongside the Zenodo slot, and in `CITATION.cff`.
4. Keep the submitted PDF: hash it and stamp it (`python3 tools/stamp.py <file> --label eprint-submission`). The archive keeps its own copy, but a local dated record settles "what exactly was submitted".

## 3.1 What the live form actually requires (checked 2026-11-24)

Fields on `eprint.iacr.org/submit`, in order:

| Field | Requirement | What to enter |
|---|---|---|
| Title | required, no HTML | the title from §1 |
| Authors | one block per author, ordered as in the paper; ORCID optional | `Lee Hyun seok`; leave ORCID empty (an ORCID identifies a natural person) |
| Abstract | required, plain text, MathJax allowed; no HTML | paste §2, no markdown, no repo links |
| Published elsewhere? | one of three radios | **"This is the only paper; not published elsewhere"** |
| PDF | **required, A4 or US letter, and the author's email address must appear in the file** | `hen.pdf` (see below) |
| Supplement | public | leave empty, or the repository URL with a one-line description |
| Comments to editor | editor-only, never public | one line: `Design document; single-authored; pen name used consistently; no implementation exists.` |
| Licence | **required dropdown**; must grant IACR a non-exclusive, irrevocable licence | choose the most permissive option offered (CC-BY if present); this does not conflict with MIT |
| Confirmation | checkbox accepting standards, licence, republication and withdrawal rules | tick after reading |

**The two things our first PDF failed on**, both fixed in `paper.md` and `tools/build_paper.sh`:

1. **Paper size** — was US letter by LaTeX default; now built with `papersize=a4`, verified 595.28 x 841.89 pt.
2. **Email inside the PDF** — now printed under the author line as `Lee Hyun seok (contact: <address>)`. The address must be a mailbox you will keep; it becomes permanently public in the paper.

## 4.1 Click path (about 15 minutes, one-time)

1. **Account**: `https://eprint.iacr.org/` -> `Register`. Email + password. No endorsement, no institutional affiliation, no fee. Use a mailbox you will still control in two years; the account is the only way to submit revisions.
2. **New submission**: `https://eprint.iacr.org/submit` -> fill the fields from §1.
3. **Upload** `hen.pdf`. The archive does not require a house template; a clean two-column paper is fine. Do not upload a bundle or a source archive.
4. **Checks before pressing submit**:
   - abstract is plain text, no markdown, no citations to the repository;
   - no mention of a token, sale, funding or launch (a single such sentence is enough to be read as promotion);
   - author email is the same as the account, otherwise correspondence is lost.
5. **Moderation**: typically days. The report number (`2026/NNN`) appears on the metadata page once accepted; until then the submission is not public.
6. **If returned**: the usual reasons are scope ("not cryptography enough"), insufficient technical content, or self-promotion. Fix by expanding §2 and §3 and cutting economics, then resubmit — the account keeps the draft.

### What eprint does not give you

No DOI, no peer review, no permanence guarantee beyond the archive's own policy. Its value is a **stable, citable report number** and a metadata page that is independent of GitHub. The DOI question stays with Zenodo (§5 of `docs/legal/finalization.md`).

## 5. Backfill after the number is assigned

Four places, one commit:

| File | What to change |
|---|---|
| `docs/outreach/metzdowd-post.txt` | replace `<report-number>` with `2026/NNN` and drop the "preferred once assigned" note |
| `docs/whitepaper/review-edition/eprint-submission.md` | add a line at the top: `Report number: 2026/NNN, assigned <date>` |
| `docs/legal/finalization.md` §5 | add an `ePrint` row next to the Zenodo slot, with the number and the date |
| `CITATION.cff` | add the report number under `identifiers:` (or in `notes:` if the schema rejects it) |

Then: `git commit -m "docs: eprint report number 2026/NNN"` and push. Hash and stamp the accepted PDF once (`python3 tools/stamp.py <pdf> --label eprint-2026-NNN`) so the submitted version is dated locally as well.

## 6. Parallel and fallback options

| Channel | Suits | Hurdle |
|---|---|---|
| eprint | design papers, no code | scope check; author identification may be requested |
| arXiv (cs.CR) | same, with versions | **endorsement by an existing author is required for new submitters in cs.CR** — usually the real obstacle, not the content |
| metzdowd `cryptography` | announcement + discussion | moderated, silent rejections, economics reads as off-topic |
| IACR conferences | full papers with proofs | a design note without proofs will not pass review |

## 7. Rule that applies to all of them

Nothing submitted anywhere may contain: an asset, a sale, a valuation, a launch date, a funding ask, or a claim of security. One sentence of that kind in an abstract is enough to have a cryptography submission read as promotion, and the rejection is silent.
