# What control remains after publication

Written after the paper was licensed CC BY and deposited with a preprint archive. The question it answers: once the text is out and irrevocable, what can the author still control?

## 1. Already given away, permanently

| Act | What it gave | Can it be undone |
|---|---|---|
| MIT on the repository | anyone may use, modify, commercialise, without payment or permission | **no** — irrevocable for everything already published |
| CC BY on the paper (`eprint`) | anyone may reproduce, translate, adapt and sell the paper, with attribution | **no** — the licence is irrevocable once accepted |
| Public git history | the exact text, at a dated commit, forever | **no** — forks and mirrors already hold copies |
| RFC 3161 timestamps | proof of what existed when | not applicable; this is evidence, not a right |

Anyone who tells you these can be clawed back is wrong. Taking the repository private, deleting files, or "revoking" a licence does not affect copies already distributed.

## 2. Still controllable, and worth using

1. **The name as a source identifier** — the only lever with real effect. `docs/legal/name-use-policy.md`: permitted nominative use, prohibited uses (asset naming, "official", "endorsed", continuity claims), and the escalation ladder that ends at public disassociation rather than litigation.
2. **The canonical text and its errata** — only the author issues errata and versions. Implementers must argue against that text, so its author retains interpretive authority even though the words are free to copy.
3. **The refusal to endorse** — the most valuable thing an unregistered name can do. "No implementation is official; silence is not approval" (`GOVERNANCE.md` §7B) removes the legitimacy that implementers most want.
4. **Succession** — authority does not transfer, to a fork, a maintainer, a company or a foundation. Stated in §7B; it forecloses the "we are the continuation" claim.
5. **Future versions** — new, original text can be licensed differently (e.g., a copyleft licence for v2). This does not bind v1.0, and derivatives of v1.0 stay MIT.

## 3. Obtainable only by giving up anonymity

- **A registered trademark** in the full name (classes 9 and 42), in one jurisdiction: the only instrument that converts "disassociate publicly" into an enforceable right. Requires an applicant identity, a filing fee and a class search (see `name-clearance.md`).
- **Ownership of an implementation** — code, keys, infrastructure, contracts. Control over a running network is operational, not documentary; it comes from employing the people who run it.
- **An entity** able to sign, hold and be liable: also identity.

There is no configuration of licences, documents or public statements that produces legal control while the author stays a pen name. Control and anonymity are substitutes, not complements.

## 4. Permanently out of reach

- Preventing a fork, or a commercial product built on the design.
- Preventing a derivative paper, translation or critique (CC BY permits all three).
- Preventing misquotation — the remedy is correction, not prohibition.
- Preventing someone from calling their project "HEN" — the remedy is a dated public statement, and it only works if readers check.

## 5. The trade, stated once

Open publication bought: citability, review, timestamped priority of *text*, and freedom from maintenance obligations. It cost: exclusivity, monetisation, and the ability to say no to a use you dislike.

If the author now wants a different trade, it cannot be made on this text. It has to be made on the next project, before the first commit, with a name registered in advance and a licence chosen for control rather than for reach.
