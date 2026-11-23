# Decision Records

ADR format: one decision = context, options, decision, reasoning, cost, review trigger. IDs are never reused; superseded entries are kept and marked `Superseded`.

Source of truth: `docs/review/decisions.md` (Chinese).

---

## ADR-001 Naming and slug

**Status:** Accepted (2026-11-22), amended (2026-11-23)

**Context.** The project needed a searchable, identifiable name that can't be mistaken for an asset offering; the Chinese name was undecided.

**Options**

| Option | Pro | Con |
|---|---|---|
| A. Steady Ledger (working name) | literal | generic word pair, drowns in search, sounds like a product |
| B. Horizon Equilibrium Network (HEN) | maps the semantics; memorable acronym; points at no asset | three words long; `HEN` means something else in English |
| C. 衡续网络 | emphasises perpetuity | weaker mapping to "Horizon" |
| D. 衡远网络 | 衡 = equilibrium, 远 = horizon/long-run; closest match; two characters | needs one sentence of explanation |

**Decision.** English `Horizon Equilibrium Network (HEN)`; Chinese `衡远网络`; subtitle "steady-state P2P value ledger" retained; slug `hen-equilibrium-network`.

**Costs to be aware of.**
1. `hen` is an everyday English word; English readers may find it odd. `hen-network` would fix it but requires a global rename.
2. Three-letter acronyms collide; check GitHub org and npm/PyPI before publishing.
3. 衡远 is opaque without explanation — English name must appear at first mention.

**Review trigger.** Trademark conflict, name already taken on GitHub, or community consensus on ambiguity.

---

## ADR-002 Dormant assets: no reclamation by default

**Status:** Accepted (2026-11-22); the experimental branch remains `Open`

**Context.** The first draft's "dormant-asset reflow" read as "the protocol may confiscate inactive funds" — the most dangerous phrasing in a public repository.

**Options**

| Option | Outcome |
|---|---|
| A. keep reclamation in the baseline | rejected: treats inactivity as abandonment; easily implemented as confiscation |
| B. delete the topic entirely | rejected: circulation contraction is a main driver; §7 would lose its counterpart |
| C. no-reclamation default + default-off experimental branch (seven conditions) | **adopted** |
| D. voluntary burn entry point | kept as Q1 candidate, not baseline |

**Decision.** Baseline states P1 "principal is non-seizable"; any reflow research exists only as a default-off experimental branch satisfying all seven conditions (whitepaper §7.4).

**Cost.** The clause is long; readers may think "much said, nothing done". That is intentional — the document only needs to be honest.

**Review trigger.** A jurisdiction explicitly prohibits any dormant-asset handling; or Q1 produces a non-compulsory alternative.

---

## ADR-003 No token, no fundraising, no operation

**Status:** Accepted (2026-11-22)

**Context.** The author publishes under a fixed byline and takes no part in development or operation; being read as "pre-ICO" would be both a risk and a misunderstanding.

**Decision.** No asset issuance, no reserved allocation, no foundation or treasury, no donations, no exchange or intermediation. The five standard answers in `README.md` are the fixed external line.

**Cost.** No economic incentive makes long-term contributors harder to attract; the repository must earn attention through documentation quality and takeover-friendliness (hence `docs/handover/`).

**Risk response.** If a third party "borrows" the name to issue something, cut with the README wording and `DISCLAIMER.md`, and remove its link from `docs/ecosystem/implementations.md`.

---

## ADR-004 Design assets separated from implementation assets

**Status:** Accepted (2026-11-22)

**Context.** The creator writes no core code, yet the repo must be takeable.

**Decision.** Design assets (whitepaper, spec, field tables, trade-offs, simulation plan, test cases, risk list) stay here; implementations live in separate repositories or clearly-labelled directories. The main repo endorses no implementation.

**Cost.** The repository will never "run", and may look abandoned. Stated in the README opening and `ROADMAP.md`.

---

## ADR-005 Status labels made mandatory

**Status:** Accepted (2026-11-22)

**Context.** The usual failure of research repos is looking complete while nothing has been verified.

**Decision.** Every artifact carries a status (`Draft` / `Community Review` / `Awaiting Security Review` / `Unmaintained` / `Fork`), in the file header and mirrored in `ROADMAP.md`.

**Cost.** One extra line per file, ongoing maintenance.

**Review trigger.** When status labels start being used as a synonym for "approved".

---

## ADR-006 Adopt the `PROJECT-GUIDE` directory structure

**Status:** Accepted (2026-11-22)

**Decision.** Restructure per `docs/handover/project-guide.md` §10: `docs/{whitepaper,protocol-draft,research,handover,review,maintenance,ecosystem,legal}` plus `spec/`, `examples/sim/`, `contrib/implementations/`, `assets/diagrams/`.

**Reason.** Readers can enter through four paths — read / review / take over / maintain — instead of scrolling a single large file.

**Cost.** More files and more cross-references, so `docs/review/checklist.md` A makes link-checking mandatory.

**Deviation.** The guide does not list root-level `CONTRIBUTING.md` / `GOVERNANCE.md` / `SECURITY.md` / `CODE_OF_CONDUCT.md`. They are platform conventions and their content remains valid, so they stay at the root, with operational detail pushed into `docs/maintenance/` to avoid two competing rule sets.

---

## ADR-007 The byline and the limits of disclosure

**Status:** Accepted (2026-11-22)

**Context.** The author wishes to publish research without disclosing identity or nationality.

**Amendment (2026-11-23).** The original decision called this "anonymous publication". That framing was both inaccurate and gave a false expectation of protection: a byline is not anonymity and does not isolate liability. Public wording is now "does not disclose identity information within this repository", and `DISCLAIMER.md` §5 and `AUTHORS.md` state that the byline confers no anonymity.

**Decision.** Publish under the pen name `Lee Hyun seok（이 현석）`; remove all statements about nationality from README, DISCLAIMER, whitepaper §12, legal notes and ADRs; rewrite §12.3 from "Mainland China" to a jurisdiction-neutral patchwork of regimes (mainland China, EU MiCA, US securities framework as illustrative examples).

**Reason.** Anonymity is a legitimate publishing choice, and the compliance boundary does not depend on the author's location — it depends on what the project does, which is nothing commercial.

**Cost.** A pen name invites speculation about who is behind it. Mitigation: `AUTHORS.md` states plainly that the name is a pen name and not a claim of nationality, ethnicity or identity. Anonymity does not reduce anyone's obligations.

**What must not happen.** Nobody may use the pen name to imply a different nationality. If a translator localises the name, that is a violation (`docs/i18n/README.md` §2.3).
