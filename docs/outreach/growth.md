# Organic discoverability

This file explains how real people find the repository, who stars it, and what we will not do. It is not a marketing plan; it is a **reviewable channel-and-metrics checklist**.

---

## 0. Compliance preamble (scope of this file)

**This file covers the dissemination of research documentation and technical tutorials only. It does not cover marketing of any financial product.**

- Permitted content: protocol mechanism discussion, simulation methods and conclusions, document organisation and handover practice, reproduction of design defects.
- Not permitted: price, valuation, supply, allocation, listing, presale, airdrop, returns, partnership solicitation, "early opportunity". None of these are posted, and none are posted "as research".
- Channels excluded: price-calling groups, exchange communities, project Telegram/Discord, paid KOL promotion, airdrop task platforms.
- No paid promotion, no bought traffic, no advertising; no exchange of exposure for "whitelist" or "allocation".
- Every external description must carry three items: **Draft stage / no token, no fundraising, no network / documents only**. Missing any one is a misdescription and must not be published.
- If a venue's rules require appearing as a "project" or "token issuer", the venue is skipped; the positioning is not rewritten to enter it.

Rationale: the entire compliance stance rests on "documents only, no business". Once the framing slides towards "project" or "opportunity", that stance fails at the level of communication, before anyone issues anything. `DISCLAIMER.md` §2–§4 govern behaviour and audience, and bind this file too.

## 0.1 The ceiling

- **GitHub Trending is out of reach for this repository.** Trending ranks by short-term star velocity and is heavily segmented by language and topic; all 66 files here are Markdown and text, GitHub's language statistic returns `language: null` (Linguist cannot classify it), so it enters no language board. Targeting trending forces star-buying, which is a red line.
- **Three reachable goals, in order of cost-effectiveness:**
  1. being found by GitHub search and topic pages (long tail, stable);
  2. being found by external search engines, via the English abstract and fixed terminology;
  3. being genuinely cited by a few developers — one citation (a blog post, an awesome-list entry, a link from an implementation's README) is worth more than 100 stars.
- **There is one real source of stars: something that runs, that can be copied, that saves time.** Three such things exist here: `examples/sim/incentive_sim.py` (zero dependencies), the 86 acceptance cases, and the A1–A7 / B1–B6 / D1–D4 / E1–E4 interface sketch. Without those, a documents-only repository converts single-digit stars per thousand visits.

## 1. Search surfaces: four, each scored differently

| Surface | Ranking signal | What we control | Status |
|---|---|---|---|
| GitHub repository search | name > description > topics > README text | name, description, topics, README opening | description carries `distributed ledger / consensus / privacy / research`; 7 topics |
| GitHub topic pages | star count within that topic | right topics, real stars | invisible at 0 stars; a **long-term** asset |
| External search engines | title, opening paragraph, inbound links | English abstract, citations | newly created, not yet indexed |
| Academic search (repositories are not indexed) | not applicable | — | an arXiv paper needs endorsement; not a near-term action |

**Do not rename the repository.** `hen-equilibrium-network` already holds the word "equilibrium"; the search gain from renaming is far smaller than the cost of breaking links.

### 1.1 Keyword matrix (target query → where it hits)

| Query a researcher would type | Where it hits | Status |
|---|---|---|
| `distributed ledger research` | description + topics | ✅ |
| `layered consensus protocol` | README abstract + whitepaper title layer | ✅ |
| `steady state incentive design` | README abstract + `docs/research/tradeoffs.md` | ✅ |
| `privacy accountable ledger` | README abstract + glossary | ✅ |
| `consensus without single operator` | description + README | ✅ |
| `no token distributed ledger` | description closing sentence + DISCLAIMER | ✅ |
| `ledger handover documentation` | `docs/en/handover/` | ⚠️ inside files only, not in README |

**A deliberate filter**: the audience wanted is people who read protocol design, not people waiting for an airdrop. The closing `no token / no offering / no network` in the description lowers click-through and raises star quality, and reduces the risk of impersonation later. Do not remove it to make numbers look better.

## 2. Conversion: from landing to starring

The order is fixed: **understand it in 30 seconds → see something that runs → decide**.

1. First screen (first 20 lines of README): English abstract + three usable assets + status badges. Done.
2. First executable action: `python3 examples/sim/incentive_sim.py` — zero dependencies, results in five seconds.
3. First doubt: no "will", "soon" or "expected launch" anywhere in the whitepaper. Currently zero; keep it.
4. First way to participate: Discussions #1 and the issue templates. Done.

**Recommended, not required**: add a screenshot of the simulation output (PNG, <200 KB) under `examples/sim/`. A text-only repository has no visual anchor, and dwell time is short.

## 3. Channels

| Channel | Post | Do not post | Expectation |
|---|---|---|---|
| GitHub itself | topic maintenance, discussion replies, issues from real feedback | self-generated issues or stars | low volume, high quality |
| Awesome-list PRs | one PR, one description matching their template, honestly marked Draft | several repositories in one PR; editing others' entries | one high-authority backlink, durable |
| dev.to / Medium / personal blog | tutorial: *"I verified an incentive curve with 40 lines of code and found the circuit breaker fighting the adjustment budget"* | project announcements, whitepaper reprints | tutorials are the only tolerated self-mention in developer communities |
| Hacker News (Show HN) | not yet. Needs a usable artefact, or it reads as self-promo | — | negative expected value now |
| Reddit | read each community's self-promotion rules first; most limit frequency | cross-posting the same text | high risk, not necessary |
| Chinese tech communities | one experience post on "how a documents-only protocol repo is organised", linking the repo | airdrops, project prospects | value lies in the **method**, not the project |
| X / Weibo | release notes and concrete conclusions only | riding crypto hashtags | low |

**Priority**: tutorial (external) > awesome-list PR (external) > GitHub upkeep > Chinese-community experience post. The first two are one-off; do not repeat submissions.

## 4. Hard limits (break one and the route is void)

- No buying stars, forks or watchers; no sock-puppet starring; no star-for-star schemes.
- No "follow the repo to get an airdrop / whitelist" bait — it attracts the wrong audience and hands impersonators an opening.
- No posting in communities that prohibit self-promotion; no cross-posting identical text; no multi-account posting.
- No fictional "already live", "already audited", "already funded".
- Do not use `token sale`, `presale`, `airdrop` or `listing` in titles or descriptions — even in negation, recommendation systems misread them.

## 5. Four-week cadence (executable without contacts)

| Week | Action | Output |
|---|---|---|
| 1 | finalise first screen and description; add the simulation screenshot under `assets/`; ensure the three handover documents are linked from the main README | one README commit |
| 2 | write a simulation tutorial (1,000–1,500 words with code and conclusions), publish on dev.to or a blog | one backlink; the starting point for citations |
| 3 | submit one or two awesome-list PRs; open one "open question" discussion drawn from Q1–Q10 in `docs/research/open-questions.md` | one PR; one thread |
| 4 | review GitHub Traffic (views, clones, referrers); adjust the description to the queries people actually used | one description change |

Then stop. **Re-posting the same content is the most common failure**, not a shortage of channels.

## 6. Metrics

GitHub repository Insights (Traffic) reports 14-day views, unique visitors, clones and referring sites; it requires push rights.

Reasonable baselines for a new repository (reference ranges, not promises):

| Metric | First 30 days | Note |
|---|---|---|
| unique visitors / 14 days | 30–300 | below 30 means no external entry; above 300 usually one community mention |
| stars per 1,000 visits | 5–30 | lower for documents-only repos; raised by runnable assets |
| clones per 1,000 visits | 3–15 | the goal is clones above stars — clones may actually use it |
| referring sites | ≥ 1 | without backlinks, traffic comes only from internal search |

**Test**: two consecutive weeks with zero referrers and zero clones means the runnable assets are not doing their job. Fix the first screen and the `examples/sim` notes before adding channels.

---

Related: [`README.md`](../../README.md) · [`docs/research/open-questions.md`](../research/open-questions.md) · [`docs/en/review/process.md`](../en/review/process.md)
