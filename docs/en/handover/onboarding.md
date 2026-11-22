# Onboarding

**For:** anyone who wants to read, review, write code for, or maintain this repository.
**Premise:** there is no runnable code here and no network. You may be reading a design that has not been implemented yet.

Source of truth: `docs/handover/onboarding.md` (Chinese).

---

## 0. Decide in ten minutes whether to continue

1. Can you accept that this is a draft that may be overturned? (Whitepaper §16; rejected edits are recorded in `CHANGELOG.md`.)
2. Can you accept that there is no team, no bounty, and nobody assigning you work? (`GOVERNANCE.md` §2)
3. Do you want **a framework that can be argued about**, or **a system that runs**? If the latter, this repository does not offer it today.

If all three are acceptable, continue.

## 1. Shortest path by role

| Role | Read this | Skip |
|---|---|---|
| Just looking | Whitepaper §2, §11, §12 | all handover docs |
| Looking for flaws | `docs/research/tradeoffs.md` + `docs/research/open-questions.md` | handover docs |
| Writing code | this page → `module-map.md` → `test-cases.md` → `api-sketch.md` | whitepaper §7 economics (later) |
| Taking over maintenance | this page → `docs/maintenance/handover.md` → `docs/maintenance/merge-rules.md` | whitepaper §6 consensus detail |
| Citing | whitepaper + `CITATION.cff` | the rest |

## 2. Handover order (follow it literally)

1. **Read the problem statement and goals** (whitepaper §1–§3), and confirm you understand the two hard constraints: *principal is non-seizable* and *power is not purchasable*.
2. **Read the protocol drafts and test cases** (`docs/protocol-draft/`, `docs/handover/test-cases.md`). Note that every field is marked non-normative.
3. **Run the example** (`examples/sim/`). Reaching a printed result is the threshold from "document" to "computable".
4. **Claim the smallest module.** Do not start with a full node. Start with transaction parsing + signature simulation, the first item of Stage 2.
5. **Verify against test cases one by one**, recording which passed and which failed.
6. **Open a design review before touching core consensus, cryptography, or economics.** Do not slip such changes into a PR.
7. **Only then consider a real implementation and security review.** Unaudited implementations must label themselves unaudited.

## 3. Three lines you cannot cross

- **No issuance, no fundraising, no promotion.** Your code must contain no token issuance, redemption, pricing, or fundraising entry point (`DISCLAIMER.md`).
- **No claims of "launched", "audited", or "official".** You are a contributor, not the project (`GOVERNANCE.md` §7).
- **Do not strip the author's attribution or the license.** Keep MIT and `CITATION.cff`.

## 4. A suggested first deliverable

Write `docs/research/q2_cost_model.md`: a minimal Sybil-cost model (cost of forging N consensus identities vs expected gain), plus a runnable script under `examples/sim/`. This decides whether principle P4 (bounded energy) survives, and it is the most valuable open gap right now (Q2).

## 5. Three frustrations you will hit

1. **"All the fields exist but nothing can be implemented."** Normal — the spec is not yet encodable (`spec/README.md` explains why).
2. **"Every mechanism has a counterexample."** Yes; `docs/research/tradeoffs.md` is a list of exactly those. That is honesty, not a defect.
3. **"Nobody answered my issue."** There is no SLA. Silence is not rejection, and the record stays (`docs/review/process.md` §5).

## 6. Pre-submit self-check

- [ ] I read the RFC template in `CONTRIBUTING.md` (for mechanism changes)
- [ ] My change introduces no token, fundraising, or price content
- [ ] I updated `CHANGELOG.md`
- [ ] I labeled the impact area (docs / spec / sim / impl / security)
- [ ] If I overturned part of the whitepaper, I changed the whitepaper too, not only the issue
