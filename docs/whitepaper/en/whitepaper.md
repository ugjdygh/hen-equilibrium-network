# Horizon Equilibrium Network (HEN)

<!-- lang-switch -->
<sub>Full text: **English** · [简体中文](../zh/whitepaper.md) · [繁體中文](../zh-Hant/whitepaper.md)　｜　Entry summaries (not full text): [Русский](../../i18n/ru.md) · [Français](../../i18n/fr.md) · [Español](../../i18n/es.md) · [한국어](../../i18n/ko.md) · [Bahasa Indonesia](../../i18n/id.md) · [Deutsch](../../i18n/de.md) · [Português](../../i18n/pt.md) · [العربية](../../i18n/ar.md)</sub>


## A Steady-State Peer-to-Peer Value Ledger

| Item | Value |
|---|---|
| Project | Horizon Equilibrium Network (HEN) |
| Chinese name | 衡远网络 |
| Document type | Open research whitepaper (research draft, non-normative) |
| Version | v0.4.0 |
| Date | 2026-11-22 |
| Review status | `Draft` (Stage 0 — see `ROADMAP.md`) |
| License | MIT |
| Author | Lee Hyun seok (이 현석), research pen name — see `AUTHORS.md` |
| Nature | No fundraising, no issuance, no investment offer, no launch commitment |

> **Note on editions.** The Chinese edition (`docs/whitepaper/zh/whitepaper.md`) is authoritative. This English edition follows the same structure; where wording differs, the Chinese text governs.

---

## Abstract

Bitcoin demonstrated peer-to-peer value transfer without a trusted third party. Its long-run tensions remain: a fixed supply combined with permanent key loss shrinks circulation; terminal block rewards decay toward fee-only security; unrestricted hash competition pushes energy use upward; transparent transaction graphs are amenable to cluster analysis; parameter changes tend to resolve through hard forks; and native scripting is deliberately limited.

This paper outlines **Horizon Equilibrium Network (HEN)**, a framework for a decentralized ledger that keeps permissionless participation, public verifiability, immutability and peer-to-peer transfer, while adding a layered peer network, a lightweight hybrid consensus with an explicit cost bound, circulation monitoring, a convergent rather than decaying reward curve, native shielding, bounded auto-tuning, and backwards-compatible upgrades.

Its distinguishing constraint is procedural rather than monetary: principal is non-seizable by default, and "equilibrium" is defined as a measurable, explainable, reversible parameter-engineering problem. The aim is not to replicate Bitcoin, and certainly not to issue an asset, but to explore a ledger path that holds a long-run balance across security, energy, privacy, circulation and iteration. This is a non-normative draft. HEN issues no token.

---

## Contents

1. Introduction
2. Design principles
3. Problem statement
4. Network model
5. Transactions and ledger structure
6. Consensus and difficulty adjustment
7. Steady-state economic model
8. Privacy versus auditability
9. Programmable conditional transactions
10. Upgrades and governance
11. Security and risks
12. Compliance stance and boundaries
13. Research route
14. Open questions
15. Key terms
16. Disclaimer
17. References
Appendix A — Naming and revision history

---

## 1. Introduction

Centralized payment systems depend on banks, clearing houses and platform intermediaries, and therefore on admission review, transaction freezing, fees, settlement delay and concentrated data exposure. Bitcoin solved double-spending without an intermediary using a chained ledger, Merkle trees, proof of work and the longest-chain rule.

More than a decade of operation also exposed the edges of that minimal design. A fixed supply lets lost assets leave circulation permanently. Decaying block rewards push long-run security toward fee dependence. Unrestricted hash competition drives energy use. Public addresses and transactions are amenable to clustering. Material parameter changes tend to require hard forks. Native expressiveness is limited.

This paper does not propose a network ready to run. It proposes a framework that can be discussed, simulated and iterated: within a permissionless setting, can circulation, perpetual incentives, bounded privacy, an energy ceiling, smooth upgrades and basic programmable transactions be regulated inside a single ledger model?

Two boundaries must be stated up front. All parameters here are **example ranges awaiting simulation**, not final values and not promises. And everything described concerns a **protocol-internal unit of account**, not money, a security, or a tradable instrument. HEN issues no token and reserves no allocation.

## 2. Design principles

Principles are arbitration rules, not rhetoric. When objectives conflict, priority runs: **security > public verifiability > decentralization > privacy > efficiency**.

**P1 No-seizure default.** No valid output is subject to time-based confiscation. Ownership does not lapse through inactivity.

**P2 Public verifiability.** Any node can validate blocks and transactions without trusting anyone; credibility comes from independently recomputable evidence, not institutional assertion.

**P3 Permissionless participation, and power is not purchasable.** No approval is required to join; block production opportunity is not determined by holdings; no seat, membership or voting right is for sale.

**P4 Energy cost explicitly bounded.** Proof of work is retained as a Sybil-resistance cost anchor, but difficulty and total cost carry ceilings and dynamic targets. Energy is a design parameter, not a side effect.

**P5 Minimal disclosure, not regulatory evasion.** The privacy goal is to reduce the effectiveness of *unauthorized* linkage while preserving lawful, auditable disclosure channels. The protocol is not designed to conceal illicit proceeds, obstruct justice or evade sanctions.

**P6 Reversible evolution.** Parameter changes operate within static bounds, rate limits and circuit breakers; changes beyond those bounds go through public proposals and backwards-compatible upgrades rather than routine hard forks.

**P7 No privileged single actor.** No foundation, core company, token governance or paid governance seat. The exit of any individual or team must not halt the network.

## 3. Problem statement

**3.1 Asset loss and shrinking circulation.** Lost keys, destroyed devices and long-dormant addresses remove assets from circulation permanently. With a fixed supply and no offsetting mechanism, circulating quantity contracts over time.

**3.2 Terminal incentive hole.** As block rewards approach zero, validators depend on fees. If fees cannot cover honest participation, security declines with hashrate exit. This is not one date but a thinning security budget over years.

**3.3 Energy and hash concentration.** Unconstrained proof of work becomes an arms race, and large pools weaken smaller participants. Energy and centralization share one root cause: unit reward bound tightly to unit hashpower.

**3.4 Transparency/privacy imbalance.** Public auditability is the basis of trust, but unshielded addresses, amounts and timing enable profiling and linkage.

**3.5 Upgrade friction.** Material changes to parameters, rules or features arrive with long debate and fork risk; there is no smooth, verifiable, reversible adaptive channel.

**3.6 Limited native expressiveness.** Beyond transfers, conditional settlement, time-locked payments, joint control and release conditions rely on external systems or layer 2, moving trust assumptions off-chain.

**3.7 These problems are coupled.** Fixed supply worsens circulation contraction; contraction lowers fee revenue; weak fees worsen the security budget; a weak budget invites higher unit rewards, which raises inflation and energy pressure. Any single fix moves the pressure elsewhere, so they must be observed by one regulator.

## 4. Network model

Three roles, layered by *responsibility*, not by *trust*: every layer's output must be independently recomputable by the layer above.

| Layer | Role | Duties | Example resources |
|---|---|---|---|
| L0 | User light node | Wallet, signing, broadcast, key-block verification | Ordinary device, intermittent online |
| L1 | Validating node | Format and signature checks, spam filtering, mempool, forwarding | Always online, moderate storage |
| L2 | Consensus node | Block assembly, consensus validation, ledger writes | High availability, full ledger |

Rules: transactions are signed and broadcast, pre-processed by validating nodes into the mempool; candidate blocks are validated and competitively confirmed by consensus nodes; the valid-longest-chain rule applies, with invalid and malicious forks excluded; user nodes may upgrade to validating or consensus roles; discovery, propagation and state sync rely on peer protocols; material upgrades land compatibly and incrementally.

The trade-off is sensitivity to propagation delay and the fact that validating nodes can become traffic observation points. The latter is treated as a privacy risk in §8.

## 5. Transactions and ledger structure

Blocks contain a header and a transaction set.

**5.1 Block header.** `version` (uint32, undefined feature bits are invalid), `prev_block_hash`, `merkle_root`, `timestamp` (with a tolerance and median-time rule), `difficulty_target`, `nonce`/`proof`, `extension_flags` (each bit defined before use), and `checksum`.

**5.2 Transaction.** Inputs referencing prior spendable outputs with unlocking evidence; outputs specifying recipient, amount, lock or condition; fee; signatures; optional condition fields (§9); optional shielding fields (§8).

**5.3 Merkle tree.** Transactions form a Merkle tree and only the root enters the block, enabling batch validation and light-client inclusion proofs. Light verification should combine inclusion proofs with exclusion proofs where needed, so that light nodes do not degrade into trusting peers.

The draft field tables are in `docs/protocol-draft/`. The UTXO versus account-model choice is open (Q9) and should be settled by measurement, not preference.

## 6. Consensus and difficulty adjustment

HEN keeps proof of work as the cost anchor for Sybil resistance and anti-tampering, and adds **verification-record weight** derived from time and verifiable behaviour — not from staked assets — to limit pure hashpower dominance.

Three prohibitions: holdings must never determine block rights; weight can never be bought, transferred or inherited; no single entity may hold a de facto veto. Weight accrues only through time and verifiable conduct.

Difficulty responds to multiple signals: deviation from target interval, estimated effective hashrate with confidence bounds, active consensus node count and dispersion, mempool backlog, and concentration warnings. Adjustments carry static bounds, per-step caps and a cap on consecutive moves.

Known limits: selfish mining, long-range reorganization, "weight farming" (long low-intensity participation followed by a burst), and the coupling between Sybil cost and identity cost remain unresolved (Q2, Q3).

## 7. Steady-state economic model

**7.1 A unit of account, not a token.** "Assets", "amounts" and "supply" refer to a protocol-internal unit used to meter resource usage and incentives. It is not legal tender, not a security, not a collective investment scheme, and carries no return expectation.

**7.2 Convergent, not decaying-to-zero, issuance.** Early release bootstraps the network; the middle phase converges to avoid persistent inflation and to prevent early-holder entrenchment; the long run keeps a minimal floor reward so that the security budget does not depend solely on fee volatility. Example parameters for simulation only: annual growth of the unit capped within 0.3%–1.0%; fee share of validator revenue targeted below 50% long-run.

**7.3 Fee split.** Roughly 60% incentive (weighted by verification record), 20% burn (with publicly recomputable records), 20% ecosystem (research, audit, public development, with published accounts and an explicit ban on distributions to individuals). Ratios may move within bounds; material changes require public discussion and a recorded decision.

**7.4 Dormant assets: no reclamation by default.** Baseline rule: **principal is non-seizable**. No output is subject to time-based confiscation, however long it stays dormant. This section exists because circulation contraction cannot be discussed without it, but the conclusion is explicit: this paper neither advocates nor recommends reclamation.

Any study of "reflow" may only exist as a **default-off experimental branch** satisfying all of: a very long dormancy threshold (example 50–100 years, TBD); no signing activity and no public inheritance, custody or recovery registry; supermajority consensus plus an independent governance vote; on-chain notice of at least 12 months; a recovery window in which the holder or lawful successor may claim with verifiable evidence, with return taking priority; immediate freeze on conflict with applicable law or judicial process; and reflowed assets usable only for public research and audit pools, never distributed to any individual, team or early participant.

"No activity" is not "abandonment". No implementation may treat dormancy as a de facto confiscation tool, and no third-party claim against reflowed assets is recognized.

**7.5 Anti-abuse boundary.** Excluded from the project's intent: disguised issuance via "circulation adjustment", insider allocation via "ecosystem pool", confiscation via "reflow", illicit concealment via "privacy", and tyranny of the majority via "governance".

**7.6 Circulation monitoring.** Publicly recomputable indicators: active addresses over a defined window, activity and median fees, dormancy rate, annual unit growth and burn, and expansion or contraction trend. The target is not a fixed money supply but a long-run predictable, explainable, adjustable circulation steady state. Test: a 2× deviation in any indicator triggers a defined, bounded, reversible response.

## 8. Privacy versus auditability

**8.1 Goals.** Auditable blocks and transactions; no direct identification from a chain of addresses alone; disclosure controllable by the holder; and reduced effectiveness of unauthorized clustering, amount fingerprinting, timing correlation and traffic inference.

**8.2 Candidate directions.** One-time or pseudonymous addresses via hierarchical derivation; mixing, batching and shielding fields; commitment schemes with range proofs to preserve verifiability without revealing amounts; separation of publicly verifiable data from identity data, with the latter never entering the ledger; network-layer measures to reduce origin observability, evaluated against propagation cost.

**8.3 Boundaries.** Absolute anonymity is not promised: with enough external information, chain analysis, traffic monitoring or behavioural patterns, deanonymization remains possible. The protocol is not designed to obstruct law enforcement or evade sanctions. And shielding itself is an attack surface: broken cryptographic assumptions, implementation side channels and "marked pool" secondary exposure all belong in the threat model.

## 9. Programmable conditional transactions

Supported types: time-locked transfers (locked until the median time passes), m-of-n multisig, conditional escrow, proof-based fulfilment, and designated payments restricted to a recipient or purpose.

Design constraints: scripts stay minimal and statically bounded in resource cost; no general-purpose VM; complex contracts and general computation live on layer 2 or outside the protocol; every condition uses **default-deny** semantics — a failed condition leaves the output locked rather than degrading into a freely spendable one; and layer-2 trust assumptions must be declared rather than masked by the word "main-chain security".

## 10. Upgrades and governance

**10.1 Bounded auto-tuning.** Static bounds; rate limits per step and per unit time; a circuit breaker that freezes adjustment after N consecutive same-direction moves or threshold deterioration; and full recomputable records permitting rollback to the last stable state.

**10.2 Proposals.** Changes beyond the automatic range follow a public RFC: problem, proposal, alternatives, impact analysis across security/privacy/economics/compatibility, implementation and rollback plan, and a review conclusion. Review turns on whether the technical argument holds, not on headcount or holdings.

**10.3 Compatible upgrades.** Prefer backwards-compatible (soft) upgrades with a migration window and coexistence period, so that old nodes can exit safely rather than being instantly isolated.

**10.4 Maintainers.** Formed naturally by long-active contributors. Their remit is technical arbitration and process execution: merging reviewed changes, maintaining releases, keeping decision records public. They own neither the protocol nor a paid seat, and gain no consensus-layer privilege.

**10.5 Forks.** Forks are permitted when consensus fails. A fork chain bears its own security, economic and legal responsibility; this repository endorses none of them; a fork may not fundraise or claim official status under this project's name.

The goal is to reduce fracture, not to enforce unanimity — and not to silence dissent through process.

## 11. Security and risks

Unresolved and merely identified: cryptographic risk (hash, signature, commitment and shielding schemes may fail in theory or implementation; unaudited code is untrustworthy); consensus attacks (hash concentration, double spending, selfish mining, long-range reorg, weight farming); privacy risk (shielding is not anonymity); economic risk (inflation expectations, incentive misalignment, floor-reward arbitrage, fee-split capture); parameter drift; implementation risk (a prototype is far from a production node; this repository contains none); compliance risk (divergent and sometimes conflicting rules across jurisdictions); and social engineering (fake wallets, fake explorers and fake airdrops cause most real losses and are outside protocol design but decisive for users).

Treat this as a research framework, not a product. Any claim that "HEN has launched" or "HEN tokens are for sale" is unrelated to this project and should be treated as fraud.

## 12. Compliance stance and boundaries

**12.1 Nature.** Public technical documentation only. No token, no asset issuance, no public offering, sale, exchange, matching, pricing, market making, custody or asset management. No investment advice, return promise, price forecast or valuation opinion. No foundation, treasury, reserved allocation, donation address or paid membership.

**12.2 Author's role.** The author publishes under the research pen name **Lee Hyun seok (이 현석)** and does not disclose their identity. The author takes no part in core development, leadership, operation, node running, exchange or intermediation, and publishes documentation for discussion and review only. The author accepts no responsibility for, and endorses no, subsequent deployments, forks or derivative projects. A pen name is not a claim about nationality, residence or identity, and anonymity does not remove anyone's legal obligations.

**12.3 A patchwork of regimes.** Rules differ sharply across jurisdictions. The following examples are illustrative, not an exhaustive survey:

- Mainland China: the seven-authority *Announcement on Preventing Risks from Token Offering Financing* (4 September 2017) treats token offerings as unapproved illegal public financing; the ten-authority *Notice on Further Preventing and Handling the Risks of Cryptocurrency Trading and Speculation* (September 2021) classifies cryptocurrency-related business activity as illegal financial activity.
- European Union: Regulation (EU) 2023/1114 (MiCA) imposes authorisation and disclosure duties on crypto-asset issuance and service provision.
- United States: securities analysis follows the framework of *SEC v. W.J. Howey Co.* (1946), with separate state money-transmission rules.

Accordingly, this project conducts no cryptocurrency-related business activity in any jurisdiction — issuance, sale, exchange, matching, pricing, market making, custody or intermediation — offers no such service to users anywhere, and does not encourage anyone to undertake it. Publication serves academic and technical discussion only.

**12.4 The reader's own obligations.** Readers must assess local law themselves (securities, AML, tax, sanctions, consumer protection). Any deployment or experiment requires the necessary permissions and is undertaken at the reader's own risk. Nothing here is a compliance opinion for any jurisdiction.

**12.5 Code is not law.** A protocol can describe mechanisms; it cannot create legality. Where on-chain rules conflict with applicable law, law prevails — which is why §7.4 includes an immediate-freeze clause.

## 13. Research route

Stage 1 *refinement and simulation*: protocol field draft, economic and difficulty simulations, legality assessment of dormancy handling, privacy boundary report, terminology unification. Exit: key parameters stable in simulation, every claim backed by a reproducible script.

Stage 2 *prototype validation*: light node and mempool prototype, consensus and difficulty measurements, explorer and wallet prototypes, independent security review. Exit: no design-level failure under adversarial testing.

Stage 3 *open community*: public discussion, contributor-led maintenance, archived decision records. Exit: at least two maintainers unaffiliated with the author, and a process that runs independently for three months.

Stage 4 *long-term exploration*: layer 2, payment channels, asset proofs and compliance tooling, only if the community decides. No timeline is set.

Not done at any stage: fundraising, token issuance, or exchange-listing advocacy. Details and checklists are in `ROADMAP.md`.

## 14. Open questions

Q1 dormant-asset alternatives that do not touch principal; Q2 whether a cost anchor survives an energy ceiling; Q3 how verification-record weight avoids farming and structural exclusion of newcomers; Q4 at what floor level a reward still sustains a security budget without becoming inflationary; Q5 selective disclosure that responds to lawful requests without becoming a backdoor; Q6 control-theoretic stability of a multi-indicator loop with delay; Q7 fork coexistence without dual-spend legitimacy; Q8 a verifiable, not merely declared, energy bound; Q9 UTXO versus account model; Q10 measurable criteria for judging, in five years, whether this framework holds.

Full statements, evaluation methods and acceptance criteria: `docs/research/open-questions.md`.

## 15. Key terms

*Steady state* — long-run boundedness of monitored indicators, not price stability. *Unit of account* — the protocol's internal counter, not money. *Shielding* — techniques hiding linkage without breaking verifiability, not anonymity. *Dormant asset* — an output without signing activity, whose ownership is not changed by dormancy. *Valid longest chain* — the longest among fully validated chains. *Reversible evolution* — adjustments bounded and rollback-capable. Bilingual glossary: `docs/research/glossary.md`.

## 16. Disclaimer

This is an open technical research draft under continuous revision and may be overturned, replaced or abandoned. It is not investment, issuance, fundraising, trading, legal, tax or compliance advice, and contains no launch commitment. No security, stability, absence of defects or value is guaranteed; it contains no implementation and has not been independently audited. The repository creator does not lead, operate or guarantee further development and accepts no liability arising from use of this document. If a community proceeds, all risk lies with participants, who must verify compliance with local law. Commercial hype, pyramid schemes, fraud, illegal fundraising, token issuance and misleading endorsement under this project's name are prohibited. Any fundraising, sale, airdrop or promotion claiming to be "official HEN" is unrelated to this project.

## 17. References

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
11. Bitcoin Improvement Proposals (BIP-8, BIP-9, BIP-141, BIP-340) on version-bit activation, segregated witness and Schnorr signatures.
12. Foundational literature on hash and signature primitives, consensus lower bounds, and monetary velocity and seigniorage.

These entries mark the public knowledge this framework relies on; they do not imply that their authors endorse this paper.

---

## Appendix A — Naming and revision history

| Version | Date | Change |
|---|---|---|
| v0.1.0 | 2026-11 | Initial draft under the working name "Steady Ledger" |
| v0.2.0 | 2026-11-22 | English name fixed as Horizon Equilibrium Network (HEN); design principles, compliance stance, open questions and glossary added; dormant-asset mechanism changed to no-reclamation-by-default; non-evasion boundary added to privacy; references verified; conversational residue removed |
| v0.3.0 | 2026-11-22 | Chinese name fixed as 衡远网络; repository restructured per `PROJECT-GUIDE`; handover and review materials added; **mechanisms unchanged**, only naming, paths and status labels |
| v0.4.0 | 2026-11-22 | §12.2 rewritten for anonymous authorship (pen name Lee Hyun seok / 이 현석); §12.3 generalised from "mainland China" to an illustrative patchwork of regimes; mechanisms unchanged |

See `CHANGELOG.md` for the itemized record.
