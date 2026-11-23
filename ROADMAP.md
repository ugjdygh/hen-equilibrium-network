# Roadmap

Stages 0–4. Each stage has outputs and exit conditions. **No stage promises entry into the next one.**

The point of the groundwork is not to claim future success, but to leave a research base others can continue: clear problems, clear terminology, clear open questions, clear handover, clear boundaries.

## Stage 0 — convergence and drafting (current)

**What stage 0 explicitly does not do:**

- No recruitment of developers, validators, node operators or an "official team". There is no position to apply for.
- No commitment to launch, no launch date, no token, no allocation, no airdrop, in public or in private.
- No prototype, no testnet, no wallet, no explorer.
- No acceptance of funds in any form, including sponsorships and paid consultation.

Anyone claiming to speak for the project on these points is misrepresenting it.

| # | Item | Status |
|---|---|---|
| 0.1 | English name, abbreviation and slug (Horizon Equilibrium Network / HEN / `hen-equilibrium-network`) | Done |
| 0.2 | Chinese name (衡远网络) | Done (ADR-001) |
| 0.3 | Whitepaper problem statement, glossary, boundary statement | Done (v0.3.0) |
| 0.4 | Terminology fixed (shading/ anonymity, accounting unit/ currency, contributor/ team) | Done (`docs/research/glossary.md`) |
| 0.5 | Open-question list and trade-off analysis | Done (Q1–Q10, `docs/research/tradeoffs.md`) |
| 0.6 | Review log and version record | Done (`CHANGELOG.md`, `docs/en/review/`) |
| 0.7 | Repository skeleton and handover material | Done (`docs/en/handover/`) |
| 0.8 | Public release (repository, push, About panel) | **Done** — v0.4.0 published with release, Discussions and language matrix |

**Exit condition**: items 0.1–0.7 complete, 0.8 released, and 30 days without a reported structural gap (structure and boundaries only, not whether the mechanism is right).

## Stage 1 — research and simulation

- [ ] Literature and comparison review (first cut in place; formal sources for Q2/Q4/Q6 still pending)
- [ ] Economic simulation: circulation, dormancy rate, floor reward, fee routing (`examples/sim/incentive_sim.py` is a starting point only)
- [ ] Difficulty-adjustment simulation: gain × latency grid sweep, producing a stability domain
- [ ] Sybil-resistance cost model (Q2)
- [ ] History-weight gaming simulation (Q3)
- [ ] Privacy feasibility and boundary analysis (Q5)
- [ ] Protocol field drafts: block header, transaction, validation flow, message flow (drafted; to be revised against simulation results)

**Exit condition**: key parameters stable in simulation, every claim backed by a reproducible script (script in repo, parameters in repo, third party can rerun). While a question is open, the mechanism may not be described as "established".

## Stage 2 — prototype validation

- [ ] Transaction parsing and basic signature verification
- [ ] Merkle tree and block header validation
- [ ] Transaction pool and filtering rules
- [ ] Single-node block production and multi-node sync prototype
- [ ] Test-case backfill (`docs/en/handover/test-cases.md`, by ID)
- [ ] Independent security review (including choice of cryptographic primitives)

**Exit condition**: the prototype shows no **design-level failure** under adversarial testing — not "no bugs", but "no failure that overturns a design assumption".

**Explicitly not done at this stage**: no issuance of any asset, no off-exchange trading of any "test coin", no reward pool.

## Stage 3 — community co-creation

- [ ] Open discussion and work claiming
- [ ] Active contributors and maintainer roles (at least two unconnected to the author)
- [ ] Mature proposal and review process
- [ ] At least one independently reproduced simulation report
- [ ] If a testnet is wanted: separate security-audit and compliance assessment first

**Exit condition**: the process runs for three months without the author's involvement.

## Stage 4 — long-term exploration (unspecified)

Whether to pursue a testnet, a layer-2 design, an explorer or a wallet is decided by the community after simulation, audit and compliance assessment.

**This repository presumes no launch path**, and gives no timeline.

## Four things explicitly not done

1. No fundraising (no ICO, no presale, no donation address, no sponsorship).
2. No token issuance (no reserve, no airdrop, no allocation table).
3. No lobbying or endorsement for any exchange listing.
4. No foundation, treasury, or paid membership of any kind.

## Progress record

Version history: `CHANGELOG.md` (English) and `CHANGELOG.zh.md` (完整中文记录). Decisions: `docs/en/review/decisions.md`.
