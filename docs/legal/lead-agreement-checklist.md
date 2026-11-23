# Agreement with a technical lead: clause checklist

**This is not a contract and not legal advice.** It lists which clauses must be present when signing a written agreement with the person who will deliver the full implementation, and why. Counsel must draft and review it under the applicable law.

**Precondition**: this file only matters once stage 2 (prototype development) begins. During the documents-only stage, no such agreement is needed or recommended.

---

## Why the CLA cannot carry this

The CLA governs the licensing of contributions. It cannot handle two things:

1. **Ownership of the full implementation** — the CLA is non-exclusive, contributors keep their copyright and may reuse it; ownership of the core implementation needs a separate agreement.
2. **Fork restraint** — anyone can read the whitepaper and rewrite the code from scratch, which **infringes no copyright** (copyright protects no idea). Only a signed counterparty can be restrained, and only with consideration.

---

## Clause list

| # | Clause | Why it must be there |
|---|---|---|
| 1 | **Parties and nature of engagement** | establish employment/contract/consultancy, not partnership, agency or trust; avoid being treated as a joint operator |
| 2 | **Deliverables and acceptance** | itemise the protocol implementation, node software, testnet, documentation; acceptance criteria should be executable tests (the 86 cases in `docs/en/handover/test-cases.md` can be cited directly) |
| 3 | **Ownership of copyright** | who owns the work created in the engagement, including adaptation, translation and compilation rights; if assigned, state scope, territory and whether to register |
| 4 | **Consideration and payment schedule** | milestones tied to acceptance; **fork/non-compete restraints need consideration**, or they will not be enforceable in most jurisdictions |
| 5 | **Fork restraint (core)** | during the engagement and for a stated period after, no competing public chain built directly on this project's conception, and no use of unpublished material for third-party projects; specify term, territory, scope, liquidated damages |
| 6 | **Pre-existing and third-party code** | declare dependencies, prior works and personal projects; confirm licence compatibility (this repository is MIT) |
| 7 | **Interaction with the CLA** | contributions to the community are also governed by `CLA.md`; the agreement must not conflict with rights already granted there (e.g. a ban on sublicensing) |
| 8 | **Confidentiality boundary** | what must be public (research documents), what may stay private (security design, key management); no hiding security defects behind confidentiality |
| 9 | **Security and audit responsibility** | who audits, who signs off pre-deployment; no claim of security without audit |
| 10 | **IP indemnity** | warranty that delivered code infringes no third-party rights, plus handling and indemnity if sued |
| 11 | **Termination and handover** | termination triggers, handover list for source code, keys and credentials, knowledge-transfer period (30 days recommended), acceptance of handover |
| 12 | **Dispute resolution and governing law** | arbitration or forum, governing law; assess enforceability for cross-border engagements |

---

## Three practical cautions

1. **An agreement binds only its parties.** Anyone on the internet who forks or rewrites is unaffected; never suggest to investors, community or yourself that it prevents forking.
2. **Unpaid restrictions usually fail.** Non-compete and fork restraints without payment or compensation are hard to enforce in most jurisdictions; writing them down is not the same as enforcing them.
3. **Copyright is not a moat.** A public chain survives on community, nodes and consensus; with all the copyright in hand, an original network is still marginalised if the community moves to a fork.
