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
| PDF | `HEN-review-edition.pdf`, 7 pages |

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

## 5. Parallel and fallback options

| Channel | Suits | Hurdle |
|---|---|---|
| eprint | design papers, no code | scope check; author identification may be requested |
| arXiv (cs.CR) | same, with versions | **endorsement by an existing author is required for new submitters in cs.CR** — usually the real obstacle, not the content |
| metzdowd `cryptography` | announcement + discussion | moderated, silent rejections, economics reads as off-topic |
| IACR conferences | full papers with proofs | a design note without proofs will not pass review |

## 6. Rule that applies to all of them

Nothing submitted anywhere may contain: an asset, a sale, a valuation, a launch date, a funding ask, or a claim of security. One sentence of that kind in an abstract is enough to have a cryptography submission read as promotion, and the rejection is silent.
