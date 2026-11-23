# Contributing

Thanks for reading. The goal here is to make **technical arguments checkable**, not to gather supporters.

## What you can do

- Point out an error, omission or contradiction in an argument.
- Offer a counterexample: a concrete situation in which a design fails.
- Supply simulations, references, or comparisons with existing work.
- Fix terminology, translations, formatting and citation style.
- Propose an alternative design and show how it satisfies the principle priority in `docs/whitepaper/en/whitepaper.md` §2.

## Contributor licence (CLA)

Any contribution — code, documentation, translation, test cases — requires accepting [`CLA.md`](CLA.md) first. It is a **permissive** CLA: you keep the copyright in your work, and grant the maintainers a perpetual, worldwide, sublicensable, relicensable licence.

Easiest route: sign once in the sign-off issue (label `cla-signoff`) with

```
I have read CLA.md and I agree to its terms for my contributions to this repository.
```

`.github/workflows/cla-sign.yml` records it in `CLA-SIGNATURES.md`, and from then on any PR you open is recognised as signed. Signing inside a PR thread also works; where a PR has several contributors, each must reply.

**This is not a judgement on the quality of your contribution** — it is a necessary link in the licence chain. Records and export: [`docs/legal/cla-ledger.md`](docs/legal/cla-ledger.md).

If a contribution contains generative-AI output, declare it in the PR description (see `CLA.md` §6).

## Out of scope (closed without discussion)

- Price, market capitalisation, listing, trading strategy, "when token".
- Fundraising, recruitment, group invites, presales, airdrop plans.
- Any commercial partnership, endorsement or promotion under this name.
- Personal attacks, regional or ethnic attacks, political mobilisation, religious proselytising.
- Requests that the author assume development, operational or legal responsibility.

## How to file an issue

Make the title itself a claim; include four things:

1. **Location** — section number or file path.
2. **Problem** — which sentence fails, under what conditions.
3. **Reason** — citation, derivation, counterexample or simulation result.
4. **Proposed handling** — delete, rewrite, mark as an open question, or add conditions.

"I think this is wrong" or "HEN will fail" cannot be processed.

## How to file an RFC

Open an issue titled `RFC:` and use this structure:

```
## Problem
(the specific defect, with section location)

## Proposal
(what changes, and how)

## Alternatives
(at least one, and why it was not chosen)

## Impact
- security:
- privacy:
- economics:
- compatibility:
- compliance (does it touch the §12 boundary?):

## Rollout and rollback
(how many steps, and how to revert)
```

Review turns on whether the technical argument holds, not on headcount, holdings or votes. Outcomes and reasons go into `CHANGELOG.md`; decisions also go into `docs/review/decisions.md`. Full process and status vocabulary: `docs/en/review/process.md`.

## Labels

| Label | Used for |
|---|---|
| `docs` | documentation revisions |
| `translation` | translations |
| `spec` | protocol specification |
| `simulation` | simulation changes |
| `security` | security notes |
| `implementation` | community implementations |
| `archived` | archived / paused |
| `out-of-scope` | price, token, fundraising, recruitment |
| `needs-repro` | no reproducible basis |
| `needs-review` | awaiting an unaffiliated reviewer |
| `cla: pending` / `cla: signed` | CLA status (automated) |

## Commit conventions

- One concern per PR; prose fixes can go straight to a PR, mechanism proposals need an RFC issue first.
- Commit messages in the imperative, saying what changed rather than what you think.
- Documentation and code share the licence (MIT). Submitting means you agree to release your contribution under it.
- Do not introduce unverifiable or unattributed references; citations must be independently findable.
- Tick the self-checks in `.github/PULL_REQUEST_TEMPLATE.md`; mechanism changes also pass part B of `docs/review/checklist.md`.

## Discussion rules

See `CODE_OF_CONDUCT.md`. The core rule: attack the argument, not the person.

## What maintainers do

See `GOVERNANCE.md`. Maintainers run the process and merge; they do not own the protocol and do not guarantee the conclusions are right.
