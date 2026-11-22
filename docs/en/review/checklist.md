# Review Checklist

Two lists: **before publishing** (every public push of documents) and **mechanism review** (every RFC).

Source of truth: `docs/review/checklist.md` (Chinese).

---

## A. Before publishing

- [ ] Search for legacy names: `Steady Ledger`, `地平线`, `horizon-equilibrium-network` (only the comparison table and revision history may still contain them)
- [ ] Search for "币 / 代币 / token / coin" (only negative statements such as "no token" may remain)
- [ ] No promises, guarantees, "will", or launch timelines anywhere
- [ ] No conversational residue ("shall I also…?", "here is what I generated for you")
- [ ] Every internal path reference resolves
- [ ] Version numbers consistent across `README.md`, the whitepapers, `CITATION.cff`, top of `CHANGELOG.md`
- [ ] `CHANGELOG.md` records this change with its reasoning
- [ ] `DISCLAIMER.md` and whitepaper §12 agree (no issuance, no fundraising, no operation)
- [ ] Author-role wording consistent (no development, no leadership, no operation, no endorsement, identity undisclosed)
- [ ] Every reference is independently verifiable
- [ ] SVG diagrams open in a browser (no garbled text, nothing clipped)
- [ ] Example script runs (`python3 examples/sim/incentive_sim.py`)
- [ ] Status labels match the actual stage (`Draft` / Stage 0)

## B. Mechanism review

- [ ] The proposal states its **cost**, not only its benefit (cross-check `docs/research/tradeoffs.md`)
- [ ] If it overrides a principle, it explains why an exception is justified
- [ ] Does it touch the §12 compliance boundary? (yes → reject outright)
- [ ] Does it introduce purchasable / transferable / inheritable weight or seats?
- [ ] Does it introduce "condition failed → downgrade to spendable"?
- [ ] Does it introduce "undefined flag → ignore"?
- [ ] Is there a rollback path or compatibility window?
- [ ] Is the verification method recomputable (script, parameters, counterexample)?
- [ ] Are `tradeoffs.md` and the matching entry in `open-questions.md` updated?
- [ ] Has one unaffiliated contributor reviewed it?

## C. Handover checklist

- [ ] Module card completed with all six fields (spec / tests / simulation / question / security caveat / acceptance)
- [ ] Known pitfalls written down, not left in code
- [ ] Unimplemented items labelled "not implemented", not "to be optimised"
- [ ] Status correct, including "unaudited"

---

**Usage:** A on every publish, B on every RFC, C on every handover. All three must pass to merge; no exceptions argued.
