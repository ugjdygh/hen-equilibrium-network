# Horizon Equilibrium Network (HEN)

<!-- lang-switch -->
<sub>Full text: **English** · [简体中文](docs/whitepaper/zh/whitepaper.md) · [繁體中文](docs/whitepaper/zh-Hant/whitepaper.md)　｜　Entry summaries (not full text): [Русский](docs/i18n/ru.md) · [Français](docs/i18n/fr.md) · [Español](docs/i18n/es.md) · [한국어](docs/i18n/ko.md) · [Bahasa Indonesia](docs/i18n/id.md) · [Deutsch](docs/i18n/de.md) · [Português](docs/i18n/pt.md) · [العربية](docs/i18n/ar.md)</sub>

**衡远网络 · 稳态点对点价值账本**
*An open research ledger for long-run balance · Draft stage, no token, no offering, no network*

[![Status: Draft](https://img.shields.io/badge/status-draft-lightgrey)](ROADMAP.md) [![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![No token](https://img.shields.io/badge/token-none-critical)](DISCLAIMER.md)

Author: **Lee Hyun seok (이 현석)**, a research pen name · Primary language: **English (en)** · [Other languages](#languages)

---

## Abstract (English)

HEN is a public research notebook for a **layered, steady-state peer-to-peer ledger**. It treats four problems that are usually solved in isolation as one coupled system: how value circulates without unbounded issuance, how peers stay ordered without a single operator, how privacy remains *user-controllable* rather than absolute, and how parameters adapt without quietly destroying the incentives they were meant to protect.

The repository ships working material, not promises: a runnable toy simulation of the incentive curve, an 86-case acceptance test suite for any future implementation, a module map and API sketch, and a handover pack written for whoever takes over the code.

`peer-to-peer ledger` · `steady-state incentives` · `layered consensus` · `accountable privacy` · `parameter adaptation` · `no token`

## What you can actually use today

- **`examples/sim/incentive_sim.py`** — runs offline, no dependencies. Prints the emission curve, the steady-state band, and two design defects it found (one of them is a real conflict between a circuit-breaker rule and the parameter-adjustment budget). `python3 examples/sim/incentive_sim.py`
- **`docs/handover/test-cases.md`** — 86 acceptance cases with stable IDs, written so an implementer can adopt them before any code exists.
- **`docs/handover/api-sketch.md`** — A1–A7, B1–B6, D1–D4, E1–E4 interfaces, enough to start a client without guessing.

If you only read one file, read [`docs/whitepaper/en/whitepaper.md`](docs/whitepaper/en/whitepaper.md).

---

## 这是什么

一个面向区块链底层账本的**开放研究仓库**。它只沉淀四类东西：问题陈述、协议草稿、研究问题、可接手的协作框架。

核心研究方向（均未定稿）：

- 稳态流通与永续激励
- 分层对等节点网络
- 轻量化、低能耗的共识机制
- 账本可审计与用户隐私可控之间的平衡
- 自适应参数调节与平滑升级
- 基础可编程条件交易

**当前阶段只有文档。** 无白皮书定稿、无协议定稿、无代码实现、无发行计划、无运营实体。

## 这明确不是什么

- **不发行、不出售、不推广任何资产。** 文中"资产""金额""供应量"均指假设协议内部的记账单位。
- **不募资。** 无 ICO、无预售、无捐赠地址、无收益分配。
- **不是已运行网络。** 无主网、无测试网、无可信赖的节点软件、无经审计的密码学实现。
- **不承诺。** 不含上线、上币、估值、性能或安全性的任何承诺。

## 创建者边界

仓库创建者只负责：搭建公开仓库骨架、提供初始思路与文档草稿、组织前期打磨与意见收集、维护交接说明。

创建者**不负责**：核心代码开发、长期代码评审与合并把关、安全审计与生产部署、项目运营与社区管理、募资发币与价值承诺、为任何第三方分叉或实现背书。

> 本仓库提供研究、设计、规范与仿真类资产；核心实现由后续贡献者独立承接。仓库创建者不交付、不维护、不担保生产代码。

## 对外统一口径（可直接复用）

| 场景 | 回答 |
|---|---|
| 简介 | This repository lays the groundwork for research, simulation and collaborative design of a layered, steady-state ledger. No launch, token or offering is implied. |
| 白皮书结尾 | This document establishes a research baseline. Subsequent development, simulation, audit and deployment decisions will be determined by the contributing community. |
| 是否上线 | The repository is a research foundation. Any future deployment would require simulation, security review, community consensus and compliance assessment; there is no roadmap to launch. |
| 是否发币 | This project does not issue, sell or promote any asset. If third parties independently build assets, they are not part of this research repository. |
| 第三方实现 | Links to third-party implementations are provided for discoverability only. They are not audited, endorsed, or maintained by this project. Use at your own risk. |

## 如何被发现 / Discoverability

增长路线（渠道、节奏、红线、度量）见 [`docs/outreach/growth.md`](docs/outreach/growth.md)。原则一句话：**只做能被搜索到、能被引用、能被跑起来的事；不买 star、不刷票、不用空投诱饵。**

## 仓库结构

```
hen-equilibrium-network/
├── README.md                      本文件：定位、边界、口径、导航
├── LICENSE                        MIT
├── AUTHORS.md                     作者署名与研究化名说明
├── DISCLAIMER.md                  免责与合规声明（必读）
├── CHANGELOG.md                   版本与逐条修订记录
├── ROADMAP.md                     阶段 0–4 与退出条件
├── CONTRIBUTING.md                参与方式、RFC 入口、标签
├── GOVERNANCE.md                  治理原则与决策权
├── CODE_OF_CONDUCT.md             讨论规范
├── SECURITY.md                    设计层安全问题如何报告
├── CITATION.cff                   引用元数据
├── .github/
│   ├── ISSUE_TEMPLATE/            review / discussion / implementation
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── whitepaper/
│   │   ├── zh/whitepaper.md       中文版（权威版本）
│   │   └── en/whitepaper.md       English edition
│   ├── protocol-draft/            区块头 / 交易 / 消息流 / 验证流（草稿）
│   ├── research/                  术语表、开放问题、参考文献、取舍、对比
│   ├── handover/                  接手引导、模块地图、接口草稿、测试用例、项目工作底稿
│   ├── review/                    评审流程、审核清单、决策记录
│   ├── maintenance/               维护者交接、合并规则
│   ├── ecosystem/implementations.md  第三方实现收录（仅展示）
│   ├── i18n/                      10 个语种的入口摘要页 + 语言覆盖矩阵
│   └── legal/disclaimer.md        声明背后的法务边界说明
├── spec/                          规范沉淀位（当前为空，见 spec/README.md）
├── examples/sim/                  可运行示例（激励曲线仿真）
├── contrib/implementations/       社区实现登记说明
└── assets/diagrams/               架构图（SVG，可编辑）
```

## 从这里开始读

1. **想判断这项目靠不靠谱**：`docs/whitepaper/zh/whitepaper.md` §2（设计原则）、§11（风险）、§12（合规立场）。
2. **想接手写代码**：`docs/handover/onboarding.md` → `docs/handover/module-map.md` → `docs/handover/test-cases.md`。
3. **想评审或提问题**：`docs/review/process.md` + `docs/research/open-questions.md`。
4. **想引用**：`CITATION.cff`。

## 参与

改文档 → 直接提 PR。改机制 → 先开 RFC issue（模板见 `CONTRIBUTING.md`）。首个 PR 需接受许可型 [`CLA.md`](CLA.md)（保留你的著作权，仅授予维护者可再许可的使用权）。

评审入口：[Discussions #1](https://github.com/ugjdygh/hen-equilibrium-network/discussions/1) —— 说明什么算有效意见、什么会被关闭、决策如何做出。价格、代币、拉人、募资类讨论一律关闭。讨论规范见 `CODE_OF_CONDUCT.md`。

## Languages

The switcher above is the only mechanism GitHub offers here: the platform has **no per-repository language setting**, and its automatic "Languages" widget is a file-type statistic, not a language choice. So switching is done by linking between localized pages, not by a site-level control.

The primary content language is **English**. Coverage is declared by what can be read end to end, not by the number of pages:

| Tier | Locales | What exists |
|---|---|---|
| Full text | `en`, `zh`, `zh-Hant` | README, DISCLAIMER, whitepaper (en + zh; zh-Hant is an auto-converted Draft), handover and review docs (en edition) |
| Entry summary only | `ru`, `fr`, `es`, `ar`, `ko`, `id`, `de`, `pt` | positioning, non-goals, status, authorship, license, links — **not** a whitepaper translation |

`zh-Hant` moved left because converting an existing full text from Simplified is a script transform, not a translation — the wording is unproven, the content is complete. It stays marked `Draft`, and the Simplified edition prevails.

The switcher bar reflects exactly this: the left half is full text, the right half is summaries marked "not full text". A language moves left only when its whitepaper translation is complete — page count alone does not promote it.

Coverage rules, translation constraints and known gaps: [`docs/i18n/README.md`](docs/i18n/README.md). Note that GitHub has no repository-level content-language setting — the sidebar "languages" are auto-detected by Linguist, so language coverage is declared here and in the matrix instead.

## 合规与作者角色

作者以固定研究署名 **Lee Hyun seok（이 현석）** 发布文档，不在仓库内披露身份信息；不参与核心开发、不牵头、不运营、不运行节点、不提供兑换或中介服务，仅公开发布文档。该署名不构成身份声明，也不产生匿名保护；**声明的效力仅限本仓库**，同一账号下的其他仓库与本项目无隶属关系。本项目**在任何辖区均不开展**与虚拟货币相关的业务活动（发行、销售、兑换、撮合、定价、做市、托管、中介），不向任何辖区的用户提供上述服务。读者须自行评估所在地法律。详见 [`DISCLAIMER.md`](DISCLAIMER.md)、[`NOTICE.md`](NOTICE.md) 与白皮书 §12。

The author publishes under a research pen name and does not disclose their identity, and takes no part in core development, leadership, operation, node running, exchange, or intermediation. A pen name is not a claim about nationality or identity. This repository is documentation for discussion only.

## License / Citation

MIT，适用于文档与后续代码。Copyright (c) 2026 Horizon Equilibrium Network contributors.

> Horizon Equilibrium Network Contributors. *Horizon Equilibrium Network (HEN): A Steady-State Peer-to-Peer Value Ledger.* Research draft v0.4.0, 2026.
