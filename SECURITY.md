# Security Policy

## Scope

This repository has **no** running network, no node software, no wallet, and no on-chain assets. There is therefore no bug bounty, no loss reimbursement, no incident response team. Anyone claiming to recover losses or offer official compensation is running a scam.

Security here is limited to the **design layer**:

- game-theoretic defects in consensus and difficulty adjustment
- verifiability and failure modes of the privacy scheme
- arbitrage and governance-capture paths in the economic design
- runaway scenarios in upgrades and parameter adjustment
- wording that could lead to misimplementation or misdeployment

## How to report

Open an issue titled `SECURITY:` containing:

1. the affected section or file;
2. the attack scenario (who, under what conditions, at what cost, gaining what);
3. the consequence (security, privacy, economics or consistency);
4. a possible mitigation direction;
5. whether it has been discussed publicly before (to avoid duplicates).

Where a defect could be abused immediately and should not be detailed publicly, **describe only the impact** in the issue, state that details are offered privately, and let the maintainers agree a channel. There is no dedicated security team; no response time is promised.

## Not accepted

- Vulnerabilities in third-party wallets, exchanges or mining pools (report to them).
- Requests for "test assets", "verification addresses" or bounties.
- Promotion, recruitment or fundraising dressed as a security report.

## Disclosure

Once a design defect is confirmed it is recorded publicly as a documentation revision (with reasons and affected sections) in `CHANGELOG.md`; decisions also go into `docs/review/decisions.md`. No fix-then-hide.

## A reminder

This document contains no implementation. If someone ships software based on it, audit that software independently; do not trust code because the documentation looks complete.
