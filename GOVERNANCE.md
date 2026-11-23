# Governance

**Horizon Equilibrium Network (HEN)**

The repository has one governance goal: let technical disagreement be settled by a traceable process, not by volume.

Principles live here; operational rules — merge thresholds, labels, PR checks, conflict handling — are in `docs/maintenance/merge-rules.md` (Chinese original; English edition pending) (this file prevails on conflict).

## 1. Three layers

| Layer | Content | How it is decided |
|---|---|---|
| Parameter | difficulty, fee bands, circulation adjustment | automatic within the protocol, bounded by limits, rate limits and circuit breakers (whitepaper §10.1) |
| Mechanism | semantics of consensus, privacy, incentives, scripting | RFC issue + public review + backward-compatible upgrade |
| Direction | whether to enter the next research stage | public discussion among active contributors, no forced conclusion (see `ROADMAP.md`) |

## 2. What is deliberately absent

- **No foundation, no treasury, no reserved allocation.**
- **No token governance.** There is no "one token one vote".
- **No paid seats.** Influence cannot be bought, transferred or inherited.
- **No technical veto.** Nobody — maintainer or author — holds a veto over a technical proposal. Reserved matters exist (§3.1) and are limited to project identity and assets, never technical judgement.

## 3. Maintainer powers and limits

Maintainers emerge from sustained contribution. Their duties are limited to:

- merging changes that passed review (thresholds in `docs/maintenance/merge-rules.md`);
- keeping releases and documents consistent;
- enforcing discussion rules (`CODE_OF_CONDUCT.md`);
- recording decisions (`docs/en/review/decisions.md`) and changes (`CHANGELOG.md`).

Maintainers **may not**: claim to speak for the community, change the protocol to serve a particular party, use the repository for fundraising or promotion, or endorse any commercial entity under the project's name.

### 3.1 Reserved matters (identity and assets only)

The following are not decided by technical review and are not subject to "majority of active contributors". They are decided by the repository owner, with reasons recorded publicly in `docs/en/review/decisions.md`:

1. **Name and marks** — name, abbreviation, logo, domain, and whether to register;
2. **Licence** — any change to `LICENSE`, including to stricter terms;
3. **Ownership and hosting** — which account holds the repository, migration, archiving or deletion;
4. **External voice** — who may speak for the project (currently: documentation maintainers issuing release notes only).

**Hard boundary.** Reserved matters **may not** be used to:
- override the review criteria in §4;
- veto a mechanism change already accepted in review;
- turn the repository into fundraising, issuance or commercial operation;
- alter the compliance boundary in whitepaper §12 or the principle order in §2.

In short: the owner decides what the project is *called*, *who holds it* and *under which licence*; review decides *how the technology changes*. The split exists so identity and assets have an accountable owner, not so that technical authority is centralised.

## 4. Review criteria

A change is accepted only if, in order:

1. it does not violate the principle priority in whitepaper §2;
2. it does not touch the compliance boundary in §12 (proposals involving fundraising, issuance or trading services are not accepted at all);
3. its argument can be independently recomputed (citation, simulation, counterexample);
4. it has a rollback path or a compatibility plan;
5. at least one contributor unconnected to the proposer has reviewed the argument.

## 5. Decision records

Every substantive decision — accepted, rejected, deferred — is recorded in `CHANGELOG.md` with date, change, reasons and a summary of dissent. Dissent is not deleted: keeping disagreement is part of what makes these documents trustworthy.

## 6. Forks

Where disagreement cannot converge, forking is allowed. A fork must:

- use a different name and repository, avoiding confusion;
- carry its own security, economic and legal responsibility;
- not raise funds, issue assets or promote itself as "official HEN".

The original repository endorses no fork.

## 7. The author's role

The author created the documents but does **not** lead, operate or take part in core development.

- On **technical** matters the author's opinion carries the same weight as any contributor's, no more (whitepaper P7);
- On the **reserved matters** of §3.1 — name and marks, licence, ownership, external voice — the author, as repository owner, has the final say, with reasons recorded publicly;
- The author's departure does not end the repository; ownership does not transfer with maintainer changes.

## 7A. No allocation, no address, no keys

The author holds no genesis allocation, no founder share, no vesting position and no advisory grant in any implementation of this design, and will not accept one.

- **No wallet address.** No address is published, assigned, pre-generated or "reserved" for the author. Any address circulating as "the founder's" is not the author's.
- **No keys.** The author will not receive, custody or sign with keys or seed phrases supplied by a third party, and will not accept an "allocation claim" link, airdrop form or multisig seat offered on the basis that this repository proposed the design.
- **No compulsion to accept.** A fork, an implementation or a community may adopt this design freely (MIT). Adoption creates no obligation toward the author, and confers no authority on the author.
- **If something is sent anyway**, it is refused in writing, not used, not moved and not counted as endorsement; the refusal is recorded publicly with a date. Unclaimed value sent to an address the author does not control is not the author's property and creates no relationship.

Reason, stated once: accepting a genesis allocation would make the author an issuer or an insider, contradict every boundary in `DISCLAIMER.md`, and convert the repository's written commitments into evidence of knowing conduct. A byline plus an on-chain allocation also ends anonymity permanently, because the two become linkable the moment the allocation moves.

Reply template and handling steps: `docs/outreach/decline-allocation.md`.

## 7B. No succession, no official implementation, no endorsement by silence

There is no "official" implementation of this design, and there will not be one under this repository's name.

- **No succession.** Authority does not transfer — not to a fork, not to a maintainer, not to a company, not to a foundation. If this repository goes dormant, dormancy is the end of it; nobody inherits the right to speak for it.
- **No endorsement.** No implementation, product or person is endorsed, approved or audited by this repository. A link, a mention or a favourable review is a technical opinion about a document, not an endorsement of a deployment.
- **Silence is not consent.** Only a dated statement in this repository counts as approval; the absence of objection counts as nothing. See `docs/legal/name-use-policy.md` §5.
- **The one durable lever.** What the owner controls is: the name as a source identifier, the canonical text and its errata, and the decision to disassociate publicly. That is all — and it is enough to keep a reader able to tell documents from products.

**What is not controllable, stated plainly**: the MIT licence is irrevocable for everything already published, so any implementation may be built, modified and commercialised without permission, credit or payment. Control over code was traded for adoption at the first commit; it cannot be bought back by accepting an allocation, only by starting a different project under a different licence.

## 8. Termination

If maintenance goes dormant, the repository is archived and stays readable and citable. Archiving does not authorise anyone to raise funds or issue assets under its name.
