# Posting to the metzdowd `cryptography` list

Plain-text mail to a moderated list. Everything below is ASCII-only, carries no product or asset language, and points at a versioned PDF.

## 0. Scope check, before sending

That list is about **cryptography**, not about ledger economics. Honest positioning of this repository against that bar:

| The list expects | What this repository actually has | Verdict |
|---|---|---|
| A threat model | `whitepaper.md` §11 names the adversary set: hash concentration, selfish mining, long-range reorg, weight farming, broken commitments, traffic correlation, implementation side channels | adequate, though coarse |
| Cryptographic primitives, and why chosen | §8: hierarchical one-time addresses, commitments with range proofs, mixing/batching, separated identity data; §9: hash-timelocks, m-of-n multisig, default-deny conditions | adequate as a design, **no new primitive** |
| Comparison with prior work | §3 and §17 contrast with Bitcoin's supply/key-loss/fee-only/transparency/fork problems and with existing e-cash | thin on the privacy literature |
| Stated limits | §11, §14 (Q1–Q10) state what is unproven | strong, and unusual for a submission — use it |

The design's novelty is **system-level coupling** (circulation, ordering, privacy and parameter adaptation treated as one problem), not a new construction. Say that in the mail. A submission that oversells a primitive gets rejected; one that says "here is a coupled design and here is exactly where its cryptography is weakest" is on-topic.

**Order of operations that costs nothing**: post to the list *and* deposit the same PDF at eprint.iacr.org. The list has no archive of its own worth citing; a preprint does.

## 1. The mail, ready to paste

To: `cryptography@metzdowd.com`
Subject: `[Cryptography] Design whitepaper: Horizon Equilibrium Network — layered consensus with conditionable privacy`

```
Summary of a design-stage whitepaper, posted for cryptographic review.
There is no implementation: no node, no network, no client, and no
asset. The document is the whole submission.

Problem. Bitcoin fixed three things that are now load-bearing: a fixed
supply with permanent key loss, a security budget that decays toward
fees alone, and a globally transparent transaction graph. Fixing any
one of them in isolation moves the problem into another subsystem,
which is why these are usually debated separately and adjusted
separately. This design treats circulation, ordering, privacy and
parameter adaptation as one coupled problem, and states the coupling
explicitly rather than claiming each part is solved.

Threat model (whitepaper section 11). Adversaries considered: a
hashpower coalition able to reorder or reorg; a passive observer doing
graph clustering and timing correlation; a participant farming
verification weight through long low-intensity presence; a party
holding keys it obtained by coercion; and an implementer whose side
channels or broken assumptions defeat the shielding layer. Explicit
non-goals: absolute anonymity, resistance to a global passive
adversary, and any claim that unaudited code is trustworthy.

Construction. Ordering is proof-of-work for cost, plus a verification
weight derived from time and observable behaviour (never from holdings,
never transferable). Privacy is conditionable rather than absolute:
hierarchical one-time addresses, commitments with range proofs so
amounts stay verifiable without being revealed, and identity data kept
outside the ledger. Conditional transfers use a deliberately minimal
script set with default-deny semantics, so a failed condition leaves an
output locked instead of degrading into a spendable one. Difficulty
responds to several signals under static bounds, per-step caps and a
breaker triggered by cumulated amplitude in a time window.

What is weak, stated plainly. The Sybil cost is tied to identity cost,
and that coupling is unresolved (Q2). Shielding is an attack surface,
not a guarantee. There are no formal proofs of the incentive claims;
they rest on a toy simulation with illustrative parameters, which
readers can rerun and contradict. The breaker rule was changed
precisely because the earlier version failed a step test.

Differences from prior work. Against Bitcoin: the issuance curve
converges instead of decaying, weight is not purchasable, and privacy
is user-controlled rather than absent. Against existing e-cash and
privacy protocols: no trusted issuer, and the privacy layer is
switchable per transaction rather than all-or-nothing. The contribution
claimed is the coupling and its stated failure modes, not a primitive.

Version: v1.0, text frozen 2026-11-23. SHA-256 of the PDF and an
RFC 3161 timestamp are recorded in the repository, so a later revision
cannot quietly claim to have said something else.

https://github.com/ugjdygh/hen-equilibrium-network/releases/tag/v1.0

Criticism of the threat model, the commitment scheme assumptions, and
the places where the design is silent would be most useful. I am not
seeking adoption, funding or collaborators; the document is public
research and nothing here is an offer of any asset.

Lee Hyun seok
```

Notes on the text: no non-ASCII characters; no links except the one versioned release page; no reference to any token, sale, community or contact channel; "no asset" stated once, factually, not as a disclaimer wall.

## 2. Before pressing send

1. `metzdowd.com/mailman/listinfo/cryptography` → subscribe with the sending address → confirm the activation mail → wait until list traffic arrives. Mail from an unsubscribed address is discarded.
2. Check the body is still plain text (no HTML part), one link per line, no attachment.
3. Read three recent threads in `pipermail/cryptography/` and match their length and tone; if the current traffic is dominated by a specific topic, wait for a quieter week.
4. Keep the sent copy. Hash it and stamp it — a dated record of what was submitted costs nothing and settles later disputes about wording.

## 3. If it is rejected

Rejections are silent and unargued; absence from the archive is the signal. Do not resend.

- Most likely cause here: the mail reads as a ledger/economics proposal with privacy attached, rather than a cryptographic one. Fix by cutting the economics to two sentences and expanding the commitment/range-proof and threat-model paragraphs.
- Second cause: length. Cut to 20 lines.
- Third: it duplicates a design already discussed. Search the archive for "accountable privacy", "range proof", "weight".
- Parallel channel that always works: **Cryptology ePrint Archive** accepts design documents without code, assigns a permanent report number, and is citable. Submit there first, then post the list mail pointing at the eprint number instead of GitHub — it reads as research, not as a repository.

## 4. What not to do

- No follow-up "any feedback?" bump. One post, then reply only inside existing threads.
- No cross-posting the same text to five lists on the same day; it reads as promotion.
- No claims of security, no "unbreakable", no comparisons that imply a product.
- No identity details beyond the byline: nationality, residence, employer and time zone are all absent from the mail, deliberately.
