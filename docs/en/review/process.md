# Review Process

**Goal:** every change ends with a traceable conclusion and its reasoning, instead of "whoever merges first wins".

Source of truth: `docs/review/process.md` (Chinese).

---

## 1. Review roles

| Type | Owner | Creator's role |
|---|---|---|
| Draft-stage document review | creator + optional outside readers | may take part, collects comments |
| Design review (protocol change) | review group formed by active contributors | may be consulted; no final say |
| Code review | implementation maintainers and code contributors | does not review core code or gate merges |
| Security / cryptography review | independent auditors or capable community reviewers | does not certify security |
| Launch / deployment review | implementers and community, self-organised | does not participate, does not endorse |

## 2. Flow by change type

**Documents and wording** (terms, translation, layout, errata): open a PR → maintainer handles quickly → record in `CHANGELOG.md`. No design review needed.

**Protocol change**: open an RFC issue (`CONTRIBUTING.md` template) → at least one reviewer unaffiliated with the proposer → discussion converges → conclusion written to `docs/review/decisions.md` if a decision is made → merge.

**Code implementation**: implementation maintainer runs code review and tests; must back-fill `docs/handover/test-cases.md`.

**Security-relevant implementation**: must be labelled "unaudited"; independent audit is expected before any real deployment. Claiming security without audit is a violation.

**No active reviewer**: the change **cannot be considered reviewed**. The project stays at the research stage. This is a rule, not a disclaimer.

## 3. Review statuses

| Status | Meaning | Who sets it |
|---|---|---|
| `Draft` | work in progress | author / maintainer |
| `Community Review` | awaiting feedback | maintainer |
| `Awaiting Security Review` | audit pending | maintainer |
| `Unmaintained / Archivable` | no active maintainer | maintainer or anyone proposing it |
| `Fork / Independent Implementation` | independent fork, self-responsible | the fork's own maintainers |

Status is written in the file header (e.g. `Status: Draft`) and mirrored in `ROADMAP.md`.

## 4. Review criteria (order is not negotiable)

1. Does it violate the priority order in whitepaper §2?
2. Does it touch the compliance boundary in §12 (fundraising, issuance, trading services)? If yes, not accepted.
3. Is the argument independently recomputable (citation, simulation, counterexample)?
4. Is there a rollback path or a compatibility plan?
5. Has at least one unaffiliated contributor checked the argument?

## 5. Fallback rules

- There is no permanent review panel appointed by the creator.
- Design review depends on active contributors; without them, admit "unreviewed".
- Code and security review must be done by people with the corresponding ability.
- The creator carries no long-term review duty.

## 6. Dissent is recorded

Objections are **never deleted**. Format: `## Objection — <date> <handle>`, stating what is objected to, on what grounds, and whether it was accepted. Even when overruled, it stays in `docs/review/decisions.md` or the PR.

A decision history that records only the winners cannot be trusted by anyone who arrives later.

## 7. Closing issues

May be closed: duplicates, off-topic (price/token/fundraising), no specific claim, demands that the author take on development or legal responsibility, violation of the code of conduct.

Every close needs one line of reason and a label. No silent closes.
