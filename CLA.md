# Contributor License Agreement

**Horizon Equilibrium Network (HEN) · CLA v1.0 · 2026-11**

This is a **permissive CLA**, not a copyright assignment. You keep the copyright in what you contribute, and grant the maintainers a licence broad enough to keep the repository workable. One signature covers all your future contributions to this repository until withdrawn in writing, and withdrawal does not affect licences already granted.

**Why it exists.** If every contributor kept all rights with no licence, any future change of licence, archiving or repurposing would require individual permission from dozens or hundreds of people. For an open repository whose contributor count is expected to grow, that path does not work. The CLA solves that. It does not take your copyright.

---

## 1. Definitions

- **"You"** — the natural or legal person submitting a contribution.
- **"Contribution"** — anything you submit to this repository: code, documentation, diagrams, test cases, translations, patches, or code fragments in issues.
- **"Project"** — this repository, its documents, specifications, simulations and later derivative works.
- **"Maintainer"** — a party holding merge rights on this repository (see `GOVERNANCE.md`).

## 2. Copyright

You **retain** copyright in your contribution. This agreement assigns and transfers no ownership.

## 3. Licence you grant

For your contribution you grant the maintainers a **perpetual, worldwide, non-exclusive, royalty-free, irrevocable** licence to:

1. reproduce, modify, adapt, translate, compile, publicly display and distribute your contribution;
2. **sublicense** the above, including to later users under the repository's licence at that time;
3. **change the licence** — relicensing the repository in whole or in part, including to stricter terms where necessary;
4. use the contribution commercially (paid distribution, hosted services, commercial integration);
5. exercise these rights while keeping the attribution convention described in `AUTHORS.md`.

No fee is payable, and no claim for payment arises from a contribution being merged, except under a separate written agreement.

## 4. Patent licence (limited)

You grant the maintainers and users of this repository a non-exclusive, worldwide, royalty-free patent licence covering only those claims necessarily practised by your contribution alone or in combination with the project.

**Termination.** If you or an affiliate bring a patent action against the project or its users alleging infringement of a patent your contribution touches, the licence granted to you under this section terminates as of the filing date.

## 5. Representations and warranties

You represent and warrant that:

1. you hold all rights needed to submit and license the contribution, or have the rights holder's permission;
2. the contribution contains nothing you know to infringe third-party copyright, patents, trademarks or trade secrets;
3. where the contribution includes third-party material, you have identified its source and licence in the submission, and that licence permits distribution under the project's licence;
4. where the contribution was made within the scope of employment, you have your employer's consent or the employer has waived its claim.

## 6. Contributions containing generative-AI output

If your contribution includes content produced by a generative model (code, prose, diagrams, translations), you must declare it in the pull request and warrant that:

1. it contains no third-party material you are not entitled to license;
2. you accept the same warranties for the submitted result as for any other contribution;
3. you understand that copyright in purely AI-generated material is unsettled in some jurisdictions, and therefore do not rely on it to assert exclusive rights.

The provenance layers of this project's own documents are described in `docs/legal/provenance.md`.

## 7. No warranty

Contributions are provided "as is", without any express or implied warranty, including merchantability, fitness for a particular purpose and non-infringement. You waive, to the maximum extent permitted by law, claims arising from the quality of a contribution.

## 8. How to sign (three routes, choose one)

### Route A — sign once in the sign-off issue (recommended; valid repository-wide)

Reply in the issue whose title contains `CLA sign-off` with the **complete** sentence:

```
I have read CLA.md and I agree to its terms for my contributions to this repository.
```

The automation (`.github/workflows/cla-sign.yml`) checks that the sentence is complete, that the comment was posted by your own account, and that you are not already listed; it then appends a row to [`CLA-SIGNATURES.md`](CLA-SIGNATURES.md) and confirms in the thread. After that, every pull request you open is recognised as signed (`.github/workflows/cla.yml` reads the ledger).

### Route B — sign inside your pull request

The **PR author, or any commit author on that PR**, replies with the same sentence in the PR thread. Rules:

- where a PR has several contributors (co-authors, commits from multiple accounts), **each must reply separately**;
- comments from bystanders (neither author nor commit author) are not counted;
- bot accounts (`[bot]`) are always ignored;
- editing the comment away afterwards makes the PR unsigned again at the next check.

### Route C — written signature (when enforceability matters)

See §9.3. Used where a stronger form is required, or where the signatory's identity must be verifiable.

## 9. Requirements for validity

Whether this agreement is recognised as a valid licence depends on six elements. The project controls what it can and states plainly what it cannot.

| # | Element | How it is handled here | Limit |
|---|---|---|---|
| 1 | **Clear assent** | Only the complete sentence counts; missing words or rephrasings do not; the automation confirms in-thread | Coercion or misunderstanding cannot be excluded |
| 2 | **Version binding** | The ledger records the first 16 hex characters of the SHA-256 of `CLA.md` at signing time | After a revision, earlier signatures bind to the earlier text (§13) |
| 3 | **Written form** | A text record; in some jurisdictions a data message counts as writing (e.g. PRC Civil Code art. 469) | **Not guaranteed to satisfy written-form rules in every jurisdiction** |
| 4 | **Retention and traceability** | The ledger lives in git history with comment links; every check re-reads it | If the ledger is tampered with, only git history can establish what happened |
| 5 | **Identifiable party** | The GitHub account is the default identifier; Route C where verifiability is required | An anonymous account cannot be verified |
| 6 | **Governing law and forum** | Deliberately left open in §11 | That openness is itself uncertainty |

**One admission**: under a pen name, "certain to be enforceable" cannot reach 100%. The reason is not imprecise drafting but that enforcement requires identifying the counterparty, which a byline declines to do. The only action that materially improves certainty is §9.3.

### 9.3 Route C — written sign-off

Where a signed, producible, enforceable record is needed, prepare a written confirmation using the template in [`docs/legal/cla-hardcopy.md`](docs/legal/cla-hardcopy.md), sign and scan it to PDF, then open an issue in the sign-off thread labelled `cla-hardcopy` and attach it. The ledger entry is appended and marked `hardcopy`.

That route requires the signatory to supply verifiable identity information, and is therefore **mutually exclusive with anonymity**. The signatory decides.

## 10. Relationship to the repository licence

Documentation is released under **MIT** (see `LICENSE`). The CLA grants the maintainers **additional** rights — notably sublicensing and relicensing — and does not alter rights any user already holds under MIT.

## 11. Governing law and disputes

The governing law and forum are **not specified in this document**. The parties may agree them in a separate written instrument; absent agreement, the law and courts of the maintainer's principal place of business at the time of contribution apply. Cross-border contributors should assess enforceability themselves.

*This clause is deliberately blank: naming a forum under a byline raises the question of who the party is. It must be completed by counsel before the agreement is relied on in a commercial setting.*

## 12. General

1. **Entire agreement** — this agreement, together with `LICENSE` and `CONTRIBUTING.md`, forms the complete set of contribution conditions; where a separate written agreement conflicts, that written agreement prevails as to the conflict.
2. **Severability** — if any clause is held invalid or unenforceable, the remaining clauses stand.
3. **No assignment** — you may not assign your obligations; the maintainers may transfer the rights under this agreement to a successor if repository ownership changes (see `GOVERNANCE.md` §3.1).
4. **Notices** — notices under this agreement may be given through repository issues, pull request comments, or the channels listed in `NOTICE.md`.
5. **No waiver** — a failure to exercise a right is not a waiver of it.

## 13. Versions and changes

Version changes are announced in `CHANGELOG.md`. **The version you signed remains effective for your earlier contributions**; a new version applies only to contributions made after it takes effect. You may stop contributing at any time; licences already granted are not revoked. Version archives are in `docs/legal/cla-versions/`.

---

*This is a licence grant, not a copyright assignment. You keep your copyright; the maintainers receive a broad, irrevocable licence to use, relicense and sublicense your contribution. Signing is recorded in the ledger or the pull request thread; the automated check verifies only that the account posted the sentence, not who the person is. Contributions containing generative-AI output must be declared. This document is not legal advice.*
