# Trademark search plan

**Not legal advice.** This is a working plan for the search that must happen before any application is filed. Costs below are indicative and change; confirm with a local agent.

## 1. What is being protected

| Element | Form | Notes |
|---|---|---|
| Word mark | `HORIZON EQUILIBRIUM NETWORK` | the primary asset; long, distinctive, low collision risk |
| Abbreviation | `HEN` | short, high collision risk — see `NOTICE.md` §6; likely unregistrable alone |
| Chinese | `衡远网络` | only if a Chinese-market filing is intended |

Protect the full word mark first. Do not spend the budget on `HEN` alone.

## 2. Where, and in which classes

Nice classification matters more than the jurisdiction list. Likely classes:

| Class | Covers | Why relevant here |
|---|---|---|
| 9 | software, downloadable publications | documentation, client software, research publications |
| 42 | computer services, hosting, technical research | protocol research, technical consulting, hosting |
| 35 | advertising, business services | **no** — this project sells nothing, and 中船衡远 already holds class 35 |
| 36 | financial services | **avoid** while the project does no financial business — filing here creates the appearance of financial intent |

**Recommendation (revised 2026-11-23, after screening)**: classes **9 and 42 only**. Class 35 is excluded: it would declare a commercial service that does not exist and it duplicates a class already held by another 衡远 user. Class 36 stays excluded for the same reason as before. Screening results and the decision are in `docs/legal/name-clearance.md`.

## 3. Search sequence

1. **Exact and near-exact word search** in the target registers (CNIPA, EUIPO, USPTO, WIPO Global Brand Database) for `HORIZON EQUILIBRIUM`, `EQUILIBRIUM NETWORK`, `HEN` within classes 9/42.
2. **Phonetic and translation search**: Chinese transliterations of "Horizon" and "Equilibrium" (地平线, 均衡, 衡远, 衡续); note that 衡续 was already rejected as a name (ADR-001).
3. **Common-law / unregistered use**: GitHub, npm, PyPI, app stores, domain WHOIS for `horizon-equilibrium`, `hen-ledger`.
4. **Company-name registers** in the home jurisdiction for the same combination.
5. **Record the result** in an issue labelled `trademark`, with dates, registers searched, and hits.

## 4. What a hit means

| Result | Action |
|---|---|
| Identical mark in class 9 or 42, same goods/services | Change the name before filing; record in `CHANGELOG.md` |
| Similar mark, different goods | Assess likelihood of confusion with an agent; usually fileable |
| Identical mark, unrelated class | Usually no bar, but check for dilution in some jurisdictions |
| No hits | Proceed to filing, but note that registers are not exhaustive |

## 5. Indicative costs (confirm locally)

| Item | Rough range |
|---|---|
| Official filing fee, one class, one jurisdiction | USD 250–400 (CNIPA is cheaper; USPTO and EUIPO higher) |
| Agent / attorney fee per class | USD 300–800 |
| Search report from an agent | USD 100–400 |
| Madrid international extension | additional per-country fees |

Budget for **two classes in one jurisdiction** before considering international extension: filing everywhere at once is the usual way small projects waste money.

## 6. Sequence relative to the roadmap

1. Search now (stage 0), because a rename later costs the repository, the release tags and every citation.
2. File **before** stage 2 (prototype), because that is when outside developers and a public identity start to matter.
3. Do not file in class 36 at any point while the project conducts no financial business.

## 7. What registration does and does not buy

It buys the right to stop others using the name for those goods and services. It does **not** stop anyone from building a chain on the same idea, and it does not make the code yours. See `docs/legal/provenance.md` §2.
