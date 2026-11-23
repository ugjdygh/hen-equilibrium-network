# Horizon Equilibrium Network (HEN)

<!-- lang-switch -->
<sub>Full text: **English** · [简体中文](docs/whitepaper/zh/whitepaper.md) · [繁體中文](docs/whitepaper/zh-Hant/whitepaper.md)　｜　Entry summaries (not full text): [Русский](docs/i18n/ru.md) · [Français](docs/i18n/fr.md) · [Español](docs/i18n/es.md) · [한국어](docs/i18n/ko.md) · [Bahasa Indonesia](docs/i18n/id.md) · [Deutsch](docs/i18n/de.md) · [Português](docs/i18n/pt.md) · [العربية](docs/i18n/ar.md)</sub>

*A layered, steady-state peer-to-peer value ledger — research notebook*

[![Status: Draft](https://img.shields.io/badge/status-draft-lightgrey)](ROADMAP.md) [![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![No token](https://img.shields.io/badge/token-none-critical)](DISCLAIMER.md)

Author: **Lee Hyun seok (이 현석)**, a research pen name · Primary content language: **English (en)**

---

## Abstract

HEN is a public research notebook for a **layered, steady-state peer-to-peer ledger**. It treats four problems that are usually solved in isolation as one coupled system: how value circulates without unbounded issuance, how peers stay ordered without a single operator, how privacy remains *user-controllable* rather than absolute, and how parameters adapt without quietly destroying the incentives they were meant to protect.

The repository ships working material, not promises: a runnable toy simulation of the incentive curve, an 86-case acceptance test suite for any future implementation, a module map and API sketch, and a handover pack written for whoever takes over the code.

`peer-to-peer ledger` · `steady-state incentives` · `layered consensus` · `accountable privacy` · `parameter adaptation` · `no token`

## What you can actually use today

- **`examples/sim/incentive_sim.py`** — runs offline, no dependencies. Prints the emission curve, the steady-state band, and two design defects it found (one is a real conflict between a circuit-breaker rule and the parameter-adjustment budget). Run: `python3 examples/sim/incentive_sim.py`
- **`docs/en/handover/test-cases.md`** — 86 acceptance cases with stable IDs, written so an implementer can adopt them before any code exists.
- **`docs/en/handover/api-sketch.md`** — A1–A7, B1–B6, D1–D4, E1–E4 interfaces, enough to start a client without guessing.

If you read only one file, read [`docs/whitepaper/en/whitepaper.md`](docs/whitepaper/en/whitepaper.md).

## What this is

An open research repository about the base layer of a ledger. It accumulates four kinds of material: problem statements, protocol drafts, open research questions, and a handover framework a successor can pick up.

Research directions (none finalised):

- steady-state circulation and perpetual incentives
- layered peer topology
- lightweight, low-energy consensus
- a balance between ledger auditability and user-controllable privacy
- self-adjusting parameters and reversible upgrades
- basic programmable conditional transactions

**At this stage there are documents only.** No finalised whitepaper, no finalised protocol, no implementation, no issuance plan, no operating entity.

## What this is explicitly not

- **No issuance, no sale, no promotion of any asset.** "Asset", "amount" and "supply" throughout refer to an accounting unit internal to a hypothetical protocol.
- **No fundraising.** No ICO, no presale, no donation address, no revenue share.
- **Not a running network.** No mainnet, no testnet, no trustworthy node software, no audited cryptographic implementation.
- **No promises.** Nothing about launch, listing, valuation, performance or security.

## Boundary of the founder's role

The repository founder is responsible only for: setting up the public repository skeleton, contributing the initial framing and document drafts, organising early review and comment collection, and maintaining the handover notes.

The founder is **not** responsible for: core code development, long-term code review and merge control, security audit and production deployment, project operations or community management, fundraising or issuance, or endorsing any third-party fork or implementation.

> This repository supplies research, design, specification and simulation material. Core implementation is to be taken up independently by later contributors. The founder delivers, maintains and warrants no production code.

## Standard external wording (reusable as-is)

| Situation | Answer |
|---|---|
| One-line summary | This repository lays the groundwork for research, simulation and collaborative design of a layered, steady-state ledger. No launch, token or offering is implied. |
| Whitepaper closing | This document establishes a research baseline. Subsequent development, simulation, audit and deployment decisions will be determined by the contributing community. |
| Is it launching? | The repository is a research foundation. Any future deployment would require simulation, security review, community consensus and compliance assessment; there is no roadmap to launch. |
| Is there a token? | This project does not issue, sell or promote any asset. If third parties independently build assets, they are not part of this research repository. |
| Third-party implementations | Links to third-party implementations are provided for discoverability only. They are not audited, endorsed, or maintained by this project. Use at your own risk. |

## Discoverability

The growth route — channels, cadence, hard limits, metrics — is in [`docs/outreach/growth.md`](docs/outreach/growth.md). One line: **only do what can be searched, cited and run; never buy stars, never brigade, never bait with airdrops.**

## Repository layout

```
hen-equilibrium-network/
├── README.md                      This file: positioning, boundaries, standard wording, navigation
├── LICENSE                        MIT
├── AUTHORS.md                     Byline and pen-name notes
├── DISCLAIMER.md                  Boundaries: what is not done, whom we do not serve (read first)
├── NOTICE.md                      Name, marks and prior-use search disclosure
├── CLA.md                         Permissive contributor licence (not an assignment)
├── CLA-SIGNATURES.md              Signature ledger, appended by automation
├── CHANGELOG.md                   Version and itemised change record
├── ROADMAP.md                     Stages 0–4 and exit conditions
├── CONTRIBUTING.md                How to take part, RFC entry, labels
├── GOVERNANCE.md                  Governance principles and decision rights
├── CODE_OF_CONDUCT.md             Discussion rules
├── SECURITY.md                    How to report design-level security issues
├── CITATION.cff                   Citation metadata
├── .github/                       Issue templates, PR template, CLA workflows
├── docs/
│   ├── whitepaper/
│   │   ├── en/whitepaper.md       English edition (authoritative on conflict)
│   │   ├── zh/whitepaper.md       Chinese edition (normative for Chinese fine print)
│   │   └── zh-Hant/whitepaper.md  Auto-converted draft (script output, not line-edited)
│   ├── en/                        English editions of handover and review docs
│   ├── handover/                  Onboarding, module map, API sketch, 86 test cases, working guide
│   ├── review/                    Review process, checklist, decision records
│   ├── research/                  Glossary, open questions, references, trade-offs, comparison
│   ├── protocol-draft/            Block header / transaction / message flow / validation flow
│   ├── maintenance/               Maintainer handover, merge rules
│   ├── ecosystem/                 Third-party implementations (listing only)
│   ├── outreach/                  Discoverability plan with compliance preamble
│   ├── legal/                     Boundaries, provenance, CLA ledger, lead-agreement checklist
│   └── i18n/                      Entry summaries in 8 locales + coverage matrix
├── spec/                          Specification slot (currently empty, see spec/README.md)
├── examples/sim/                  Runnable example (incentive curve simulation)
├── contrib/implementations/       Community implementation registry notes
└── assets/diagrams/               Architecture diagrams (SVG, editable)
```

## Where to start

1. **Judging whether this is credible** — whitepaper §2 (design principles), §11 (risks), §12 (compliance stance).
2. **Taking over the code** — `docs/en/handover/onboarding.md` → `module-map.md` → `test-cases.md`.
3. **Reviewing or asking questions** — `docs/en/review/process.md` + [`docs/research/open-questions.md`](docs/research/open-questions.md) (Chinese original; English edition pending).
4. **Citing it** — `CITATION.cff`.

## Taking part

Documentation change → open a PR. Mechanism change → open an RFC issue first (template in `CONTRIBUTING.md`). Your first PR needs the permissive [`CLA.md`](CLA.md) accepted: you keep your copyright, the maintainers receive a relicensable licence.

Review entry point: [Discussions #1](https://github.com/ugjdygh/hen-equilibrium-network/discussions/1) — what counts as a valid objection, what gets closed, how decisions are made. Price, token, recruitment and fundraising threads are closed without discussion. Discussion rules: `CODE_OF_CONDUCT.md`.

## Languages

GitHub has **no per-repository content-language setting**; its "Languages" widget is a file-type statistic, not a choice. Switching is therefore done by links between localised pages.

| Tier | Locales | What exists |
|---|---|---|
| Full text | `en`, `zh`, `zh-Hant` | README, DISCLAIMER, whitepaper (en + zh; zh-Hant is an auto-converted Draft), handover and review docs in English |
| Entry summary only | `ru`, `fr`, `es`, `ar`, `ko`, `id`, `de`, `pt` | positioning, non-goals, status, authorship, licence, links — **not** a whitepaper translation |

`zh-Hant` sits in the full-text tier because converting an existing full text from Simplified is a script transform, not a translation: the content is complete, the wording is unproven. It stays marked `Draft`, and the Simplified edition prevails.

Chinese originals of the deeper research, protocol and legal documents live alongside their English editions; where a file is Chinese-only it is listed as such in [`docs/i18n/README.md`](docs/i18n/README.md), never presented as English.

## Compliance and the author's role

The author publishes under a fixed research byline, **Lee Hyun seok (이 현석)**, and does not disclose identity information within this repository. The byline is not a claim about nationality or identity, and it confers no anonymity: it does not change where responsibility lies. **The statements here apply to this repository only**; other repositories under the same account are maintained separately and are not affiliated with this project.

The author takes no part in core development, leadership, operation, node running, exchange or intermediation, and publishes documentation for discussion only. This project does **not** carry out, in **any jurisdiction**, issuance, sale, exchange, matching, pricing, market making, custody or intermediation of virtual currency, and does not offer such services to users anywhere. Readers must assess the law where they are. See [`DISCLAIMER.md`](DISCLAIMER.md), [`NOTICE.md`](NOTICE.md) and whitepaper §12.

## Licence and citation

MIT, covering documentation and any later code. Copyright (c) 2026 Horizon Equilibrium Network contributors.

> Horizon Equilibrium Network Contributors. *Horizon Equilibrium Network (HEN): A Steady-State Peer-to-Peer Value Ledger.* Research draft v0.4.0, 2026.
