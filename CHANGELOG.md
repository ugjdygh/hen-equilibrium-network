# Changelog

**Horizon Equilibrium Network (HEN)** · Detailed Chinese record: [`CHANGELOG.zh.md`](CHANGELOG.zh.md)

---

## Unreleased — mechanism completion, deposit, trademark plan, X policy

1. **Breaker rule replaced with simulation evidence.** `examples/sim/mechanism_sim.py` (new) computes the old rule's failure from `incentive_sim.py` rather than quoting a hard-coded number: on a 1.8x compute step the "3 consecutive moves" breaker settles at target 13.31 against 18.00 needed, interval 7.39 against 10.00 — not converged. The windowed cumulative rule with cooldown and damped resume converges (target 18.00, interval 10.00, band 5.56–10.61). Gain × delay sweep: 35 of 42 settings converge; worst pair (gain 0.2, delay 8) settles at 7.17, so stability is a region, not a point.
2. **Whitepaper §10.1 amended in both editions** (§10.1.1 added), with the numbers stated as toy-model results that can be refuted.
3. **Dormancy module.** Decay 6% / reactivate 4% / opt-in burn 5%: active share falls from 1.000 to 0.254 over 40 years; burn applies only to holdings the holder explicitly gives up. No confiscation path remains anywhere in the documents.
4. **Sybil cost module.** 1,000 identities at cost 40 and reward 12 per period yields a gain/cost ratio of 0.006 — uneconomic under these assumptions, which are stated so the result can be overturned.
5. **`docs/research/open-questions.md`** gains a simulation update for Q1, Q2, Q4, Q6, marking Q4 as a value judgement that simulation cannot settle.
6. **Copyright deposit.** `tools/make_deposit.py` builds an out-of-tree bundle (whitepaper en/zh, boundary files, byline, licence, ledger, manifest), prints size and SHA-256. First bundle recorded in `docs/legal/deposit-record.md` (38,903 B, `5365ad17…d9aa434`, commit `4f7e8bf`).
7. **Trademark search plan.** `docs/legal/trademark-search-plan.md`: what to protect (full word mark first, not `HEN` alone), classes 9 and 42 only — with an explicit note that filing in class 36 would contradict the no-financial-business stance — search sequence, meaning of a hit, indicative costs, and sequencing before stage 2.
8. **X policy.** `docs/outreach/x-policy.md`: the four statements required in every post, what may and may not be said, account hygiene, three ready-to-post templates, and a correction procedure.
9. **Stage 0 guardrails written into `ROADMAP.md`**: no developer recruitment, no launch or token commitments in public or private, no prototype, no testnet, no funds accepted.
10. **Documentation set completed as requested**: `LICENSE` (MIT, holder "Horizon Equilibrium Network contributors"), `NOTICE.md`, `CLA.md`, `CLA-SIGNATURES.md`, `GOVERNANCE.md` — all present, English, and cross-linked.

## Unreleased — English-only repository surface

- README, DISCLAIMER, NOTICE, AUTHORS, CLA, CLA-SIGNATURES, GOVERNANCE, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, ROADMAP and all `.github` templates rewritten in English only. No mixed-language entry surface remains.
- `CHANGELOG.md` (this file) becomes the English record; the full itemised Chinese history is preserved verbatim at `CHANGELOG.zh.md`.
- Internal links in English documents now point to English editions (`docs/en/...`, `docs/whitepaper/en/...`), so a reader never lands on a Chinese page by following an English document.

## Unreleased — CLA global sign-off

- `.github/workflows/cla-sign.yml`: signing once in the sign-off issue appends a row to `CLA-SIGNATURES.md` (account, UTC time, `CLA.md` fingerprint, comment link), idempotent, with a confirming reply.
- `.github/workflows/cla.yml` now reads the ledger, so anyone who has signed is recognised on every later PR without re-signing.
- `CLA.md` §8 rewritten into three routes (issue sign-off / in-PR sign-off / written sign-off); §9 adds the six validity requirements with their limits.
- `docs/legal/cla-hardcopy.md`: written sign-off template, steps and maintainer checklist; explicitly incompatible with anonymity.
- Verified live: issue signature → ledger row; new PR with no comment → `cla: signed`.

## Unreleased — boundaries, byline, naming, outreach

- `DISCLAIMER.md` rewritten as *Boundaries*: what is not done, whom it does not serve, which uses are prohibited; the stacked "at your own risk" language removed because over-disclaiming reads as prior knowledge of risk. Adds §2.1: the statement **ceases to apply** once a deployable contract, prototype, token scheme, funding intake or operating entity appears.
- Byline wording corrected across `AUTHORS.md`, `DISCLAIMER.md` §5 and whitepaper §12.2: a fixed research byline, not a claim of identity, and **not** anonymity; no liability limit is asserted on the strength of a pen name.
- `NOTICE.md` added: unregistered marks, no exclusive rights claimed, disclosure of the searches performed and those not performed, rename-on-conflict policy, abbreviation risk.
- `docs/outreach/growth.md` gains a compliance preamble: what may and may not be promoted, channels excluded, no paid promotion, three mandatory descriptors, and a rule to skip any venue that requires a "project" identity.

## Unreleased — permissive CLA, reserved matters, provenance

- `CLA.md` v1.0: permissive licence, not an assignment — perpetual, worldwide, non-exclusive, sublicensable, relicensable; limited patent grant; AI-output declaration; no warranty.
- `GOVERNANCE.md` §3.1 reserved matters: name and marks, licence, ownership and hosting, external voice — owner-decided with public reasons, and barred from overriding technical review.
- ADR-008 records the change, its tension with "no veto", and the cost of an unverifiable owner under a byline.
- `docs/legal/provenance.md`: layer-by-layer account of conception / AI-assisted drafting / human review; what can and cannot be claimed (ideas are not protected by copyright); three deposit routes with costs; copyright registration and anonymity are mutually exclusive.
- `tools/provenance_manifest.py` + `docs/legal/provenance.sha256`: SHA-256 manifest of every tracked file.
- `docs/legal/lead-agreement-checklist.md`: twelve clauses for a future technical lead, plus three cautions — agreements bind only their parties, unpaid restrictions usually fail, and copyright is not a moat.

## Unreleased — language coverage, discoverability

- Language switcher split by real coverage: full text `en`, `zh`, `zh-Hant`; entry summaries for the other eight locales, always labelled "not full text". A locale moves left only when a complete whitepaper translation exists.
- `docs/whitepaper/zh-Hant/whitepaper.md` added: mechanical OpenCC conversion of the Simplified full text, marked Draft, Simplified edition prevails.
- README first screen rewritten English-first with an abstract and three usable assets; repository description made searchable; topics raised to seven.
- `docs/outreach/growth.md`: four search surfaces, keyword matrix, channel table, hard limits, four-week cadence, metric baselines.

## v0.4.0 — 2026-11-22 (anonymisation, English editions, release)

- Byline standardised; compliance stance rewritten as jurisdiction-neutral illustrative examples (mainland China, MiCA, the Howey framework).
- Commitment upgraded from "not in one jurisdiction" to "in no jurisdiction": no issuance, sale, exchange, matching, pricing, market making, custody or intermediation.
- `docs/en/` added: English editions of the four handover documents and the three review documents, all 86 test-case IDs preserved; policy that an English text may never be laxer than its Chinese counterpart.
- Whitepaper zh/en PDFs (12 and 9 pages) attached to the release; Markdown sources attached separately with distinct names.
- Release `v0.4.0`, Discussions enabled, review entry discussion posted.

## v0.3.1 / v0.3.0 — repository scaffolding

- Reorganised into `docs/{whitepaper,protocol-draft,research,handover,review,maintenance,ecosystem,legal}` plus `spec/`, `examples/sim/`, `contrib/implementations/`, `assets/diagrams/`, `.github/`.
- Chinese name fixed at 衡远网络 (ADR-001, with 衡续 rejected for weak correspondence with "Horizon").
- Handover pack: onboarding, module map, API sketch (A1–A7, B1–B6, D1–D4, E1–E4), 86 acceptance cases.
- Two runnable conclusions from the simulation: a decaying issuance curve that holds the steady-state band below 1% after year 25 at the cost of up to 8% in the first decade; and a genuine conflict between the "three same-direction moves triggers a halt" rule and the 1.8× compute-jump adjustment budget, where the target band was never reached (13.31 against 18.0).

## v0.2.0 — publication review

- Eight blocking issues fixed before publication; three mattered most: a conversational leftover at the end of the whitepaper, a licence line with no rights holder (LICENSE added, holder set to "Horizon Equilibrium Network contributors"), and a dormancy mechanism that read as "the protocol may confiscate inactive assets", rewritten as principal-inviolable with a default-off experimental branch requiring seven conditions.
- Added compliance section, explicit "no token issuance", twelve verifiable references, design-principle priority (security > verifiability > decentralisation > privacy > efficiency), problem coupling, open questions Q1–Q10, glossary.

## v0.1 — first draft

- Baseline whitepaper draft from the original working document.
