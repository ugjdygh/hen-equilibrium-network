---
title: "Horizon Equilibrium Network: a coupled design for circulation, ordering and conditionable privacy"
author: "Lee Hyun seok"
date: "November 2026"
abstract: "This note describes a ledger design that treats four properties as one coupled problem: permissionless ordering whose cost is not purchasable, privacy that is switchable per output rather than absolute, an issuance curve that converges instead of decaying toward fee-only security, and parameter adaptation that is bounded and delay-tolerant. Ordering uses proof of work as a cost anchor together with a verification weight derived from elapsed time and observable behaviour, under three prohibitions: holdings never determine block rights, weight cannot be bought or transferred, and no single entity may hold a de facto veto. Privacy is per-output and visible, in transparent, shielded and selective modes, where the disclosure key is held by the holder rather than by the protocol. Conditional transfers use a minimal script set with default-deny semantics, so a failed condition leaves an output locked instead of spendable. Difficulty control is bounded by static limits, per-step caps and a breaker triggered on cumulated amplitude within a time window; the earlier counting rule fails a reproducible step test (target 13.31 against 18.00 required) while the windowed rule converges (18.00; band 5.56-10.61), and a 42-setting sweep converges in 35. No cryptographic primitive is new, no formal proofs are offered, no implementation exists, and no asset is issued."
---
# Introduction

**Claimed**: one ledger design in which four properties are treated as a single coupled problem — a permissionless ordering mechanism whose cost is not purchasable, a privacy layer that is switchable per transaction rather than absolute, an issuance curve that converges instead of decaying to zero, and parameter adaptation that is bounded, reversible and delay-tolerant.

**Not claimed**: a new cryptographic primitive; a formal security proof; a performance result; an implementation; an asset of any kind. There is no token, no allocation and no sale, and this document is not an offer.

The reason for coupling, in one paragraph: a fixed supply plus permanent key loss removes units from circulation; a contracting circulation weakens fee revenue; a weak fee base pushes long-run security toward risky issuance; more issuance raises inflation and energy pressure; and each of these is normally "fixed" in a subsystem that then exports the problem to the next one. A design that regulates one without observing the others is, in the usual case, a design that moves the failure rather than removing it.


# Threat model

## Assets to protect

- **A1** — Ledger integrity (no double spend, no silent rewrite): the only property everything else rests on
- **A2** — Holder control (no seizure through inactivity, no forced transfer): a seizure default destroys the meaning of ownership
- **A3** — Linkage resistance (transaction graph not trivially clusterable): the practical content of "privacy" here
- **A4** — Participation openness (no purchase of consensus power): otherwise the system is a share register
- **A5** — Continuity of the security budget: a design that cannot pay for its own ordering is temporary


## Adversaries considered

- **D1** — Hashpower coalition: reorder, censor, attempt selfish-mining and long-range reorganisation
- **D2** — Passive chain observer: graph clustering, amount fingerprinting, timing correlation
- **D3** — Active network observer: partial traffic visibility, peer-set inference, eclipse attempts
- **D4** — Weight farmer: long low-intensity presence, then a burst of activity
- **D5** — Key coercer: obtains keys by coercion or theft
- **D6** — Implementation attacker: side channels, faulty randomness, broken assumptions in the privacy layer
- **D7** — Social engineer: fake wallet, fake explorer, fake "official" channel


## Assumptions, stated so they can be attacked

1. Hash and signature primitives are secure against classical adversaries for the design's horizon. No post-quantum claim is made, and a hash break collapses A1.
2. Commitment schemes are binding and hiding, and range proofs are sound and zero-knowledge (Bulletproofs-class constructions are the working assumption).
3. A majority of consensus weight is honest in expectation, with the usual partial-synchrony caveat: messages arrive within a bound most of the time.
4. Peers are not globally observable: no adversary sees all links at all times. **If this fails, A3 degrades first** and the degradation is not detectable from inside the protocol.
5. Time is roughly synchronised within a stated tolerance, and median-time rules bound manipulation.

## Explicit non-goals

Absolute anonymity; resistance to a global passive adversary; censorship resistance against a state-level blocklist enforced at the network edge; confidentiality of metadata already leaked outside the ledger; any claim that unaudited code is trustworthy; any claim that the incentive results are theorems.


# Construction

## Layered roles

Three roles, separated by **responsibility** rather than by trust; each layer's output must be independently recomputable by the layer above.

- **L0** — user light node: sign, broadcast, verify key blocks
- **L1** — validating node: format/signature checks, mempool, forwarding
- **L2** — consensus node: block assembly, full validation, ledger writes


Any participant may ascend a layer. L1 is the honest weak point: validating nodes see transactions before blocks and can act as observation points. This is a design trade, not an oversight, and it is why §3.4 does not promise anonymity.

## Ordering: cost-anchored, not holding-anchored

Ordering uses proof of work as a **cost anchor** for Sybil resistance, plus a **verification weight** derived from elapsed time and observable participation behaviour. Three prohibitions define the mechanism:

- holdings never determine block rights;
- weight can never be bought, transferred or inherited;
- no single entity may accumulate a de facto veto.

The intent is to keep D1 expensive while preventing the usual drift into a proof-of-stake register where consensus power is purchasable (A4). The known weaknesses are D4 (farming weight by long low-intensity presence) and the coupling between Sybil cost and identity cost, which is unresolved (see §6, Q2, Q3). This mechanism is the least mature part of the design and the most likely to be replaced.

## Parameter control: amplitude, not counting

Difficulty responds to several signals: deviation from the target interval, estimated effective hashrate with confidence bounds, active consensus node count and dispersion, mempool backlog, and concentration warnings. Responses are bounded by static limits, per-step caps and a breaker.

The breaker rule matters, and it changed because the first version failed a test anyone can rerun:

- **freeze after 3 consecutive same-direction moves** — final target 13.31 against 18.00 required; interval 7.39 against 10.00: **does not converge**
- **trigger on cumulated amplitude in a time window, then cooldown, then resume at `gain x 0.5`** — final target 18.00; interval 10.00; oscillation band after the step 5.56-10.61: converges


A sweep over gain against measurement delay (7 gains x 6 delays, illustrative parameters) converges in 35 of 42 settings; the worst pair (gain 0.2, delay 8) settles at 7.17 against 10.00. The correct statement is therefore **"a stable region exists", not "the operating point is stable"**. Both scripts are in `examples/sim/` and run with plain Python 3; readers are invited to break them.

## Privacy: switchable, not absolute

Three modes, chosen per output, with the mode itself visible on chain:

- **transparent** — sender, recipient, amount: nothing
- **shielded** — that a valid transfer occurred: sender, recipient, amount
- **selective** — as shielded, plus a disclosure key: amounts to third parties only


Primitives, and why each is there:

- **one-time addresses** via hierarchical derivation — removes address reuse as the cheapest clustering signal;
- **commitments with range proofs** — amounts stay verifiable as non-negative and conserved without being revealed; this is the load-bearing assumption of the whole privacy layer, and it is an assumption (D6);
- **mixing and batching at the validating layer** — raises the cost of timing correlation, at a propagation cost that must be measured, not assumed;
- **identity data kept outside the ledger** — the ledger never holds the join key;
- **network-layer measures against origin observability**, evaluated against their propagation cost.

**Leak analysis, stated plainly.** Shielding hides values, not existence. A shielded transfer still reveals: that two parties transacted, at a time, with a fee, and with a size class if the range proof's granularity is coarse. Repeated interaction between the same counterparties remains linkable by timing even when addresses are one-time; a "marked pool" (an adversary depositing into a shielded set to trace withdrawals) defeats naive shielding; and the naive "anonymity set" argument fails whenever the pool is small relative to the adversary's view. Selective disclosure is the honest response to lawful requests, but it is also the point at which the design becomes censorable — a trade to be made deliberately, in the open, not discovered later.

## Conditional transfers with default-deny semantics

Supported: time-locked transfers (median-time gated), m-of-n multisig, conditional escrow, proof-based fulfilment, designated payments restricted to recipient or purpose.

Constraints: minimal script set with statically bounded cost; no general-purpose VM; complex contracts belong to layer 2 with **declared** trust assumptions; and every condition is **default-deny** — a failed condition leaves the output locked, never degrading into a freely spendable output. That single semantic choice removes a whole class of failure (the "condition expired, so the money is anyone's" pattern) and is the main reason the script set can stay small.

D5 (key coercion) is partly addressed here: a transfer can be made conditional on a delay or a co-signature held elsewhere, which turns a coerced key into a delayed, revocable event rather than an immediate loss. It is not a solution to coercion.

## Circulation and issuance (summary)

The unit is a protocol-internal counter, not money. Issuance converges rather than decays: early release bootstraps, the middle phase targets bounded annual growth (example band 0.3%-1.0%), and the long run keeps a minimal floor so that the security budget does not rest on fee volatility alone. Fees split roughly 60% incentive / 20% burn with publicly recomputable records / 20% ecosystem with published accounts and a ban on individual distributions.

Dormant outputs are **never** reclaimed: principal is non-seizable, and no output is subject to time-based confiscation. A reflow mechanism may only exist as a default-off experimental branch satisfying seven conjunctive conditions (long threshold, no signing or inheritance record, supermajority plus independent vote, twelve-month notice, recovery window with priority, freeze on legal conflict, use limited to public research and audit pools). Under illustrative parameters (decay 6%, reactivation 4%, opt-in burn 5%), active share falls from 1.000 to 0.254 over forty years — the point being that contraction is *measurable* and must be answered by issuance and fee design (Q4), not by seizure.


# Analysis: claims and their basis

- **C1** — Coupling these four problems is necessary rather than decorative: argument in §1, §3.6
- **C2** — Weighted ordering resists D4: three prohibitions; no measurement of farming cost
- **C3** — Windowed-amplitude control converges where counting does not: two toy simulations, 42-setting sweep
- **C4** — Shielding preserves verifiability without revealing amounts: standard commitment/range-proof argument, assumed
- **C5** — Selectivity is not a backdoor: design: disclosure key is holder-held, not protocol-held
- **C6** — No seizure path exists anywhere: textual: P1, §3.6, default-off branch
- **C7** — Convergence of the issuance curve to a bounded band: arithmetic + simulation
- **C8** — The design is safe: nothing here supports that claim


Rows C2 and C8 are the ones a reviewer should attack first. C3 is the row most likely to be misread as stronger than it is.


# Comparison with prior work

- **Bitcoin** — PoW, purchasable by renting hash: none by default, transparent graph
- **Zcash / Zerocash-class** — PoW: strong shielding (zk-SNARK)
- **Monero** — PoW: ring signatures + stealth addresses, always on
- **Mimblewimble / Grin** — PoW: confidential amounts, no addresses
- **Chaumian e-cash** — trusted issuer: issuer-blind signatures


Not claimed as better in any row. The differing claim is structural: none of these regulates ordering cost, privacy granularity, issuance and parameter adaptation inside one feedback loop, and none publishes its own failure modes as acceptance criteria for reviewers.


# Open problems

- **Q2** — Does a cost anchor survive an energy ceiling?: a model relating energy cap, cost floor, and attacker budget, with measured numbers
- **Q3** — Can verification weight avoid farming and newcomer exclusion?: an adversarial simulation with a farming strategy and a cost accounting
- **Q5** — Selective disclosure that answers lawful requests without a backdoor: a formal indistinguishability statement under disclosure-key absence
- **Q6** — Control-theoretic stability with delay: a proper stability analysis of the multi-indicator loop, not a toy sweep
- **Q7** — Fork coexistence without dual-spend legitimacy: a legitimacy criterion that does not require trusting an operator
- **Q8** — A verifiable, not declared, energy bound: attestation design, or an economic argument that bounds hash spend
- **Q9** — UTXO versus account model: measurement on the conditional-transfer workload


Q1 (dormancy alternatives) and Q4 (floor level) are stated in the whitepaper as value judgements rather than technical questions, and are not claimed to be solvable by simulation.


# How to attack this design

1. Re-run `examples/sim/mechanism_sim.py` and try to make the breaker unstable with defensible parameters.
2. Attack C2: construct a farming strategy that accumulates weight cheaper than honest participation, and see whether the three prohibitions actually exclude it.
3. Attack the leak analysis in §3.4: find a linkage that survives one-time addresses and batching in a pool with realistic size.
4. Check whether default-deny semantics has a path where a locked output becomes spendable through a reorganisation.

Negative results on any of these are more valuable to this project than agreement, and will be recorded as errata or as revisions of the design.


# References

1. Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System.*
2. Merkle, R. C. (1979). *A Certified Digital Signature.* CRYPTO '89.
3. Garay, J., Kiayias, A., & Leonardos, N. (2015). *The Bitcoin Backbone Protocol.* EUROCRYPT 2015.
4. Eyal, I., & Sirer, E. G. (2014). *Majority is not Enough: Bitcoin Mining is Vulnerable.* Financial Cryptography 2014.
5. Poon, J., & Dryja, T. (2016). *The Bitcoin Lightning Network.*
6. Bünz, B., Bootle, J., Boneh, D., Poelstra, A., Wuille, P., & Maxwell, G. (2018). *Bulletproofs.* IEEE S&P 2018.
7. Maxwell, G. (2013). *CoinJoin: Bitcoin Privacy for the Real World.*
8. de Vries, A. (2018). *Bitcoin's Growing Energy Problem.* Joule, 2(5).
9. Narayanan, A., Bonneau, J., Felten, E., Miller, A., & Goldfeder, S. (2016). *Bitcoin and Cryptocurrency Technologies.* Princeton University Press.
10. De Filippi, P., & Wright, A. (2018). *Blockchain and the Law.* Harvard University Press.
11. BIP-8, BIP-9, BIP-141, BIP-340.
12. Foundational literature on hash and signature primitives, consensus lower bounds, and monetary velocity.

These mark the public knowledge this design relies on; they do not imply endorsement by their authors.


*Design document. No token, no allocation, no sale, no network, no implementation. Any claim that this project has launched, or that anything is for sale under its name, is false and unrelated to this repository.*
