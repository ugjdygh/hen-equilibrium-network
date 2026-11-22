# Horizon Equilibrium Network (HEN)

**衡远网络 · 稳态点对点价值账本**
*An open research ledger for long-run balance.*

状态：`Draft`　｜　阶段：0 · 收敛打磨期　｜　许可：MIT　｜　无代币 / 无发行 / 无网络

作者署名 **Lee Hyun seok（이 현석）**（研究化名）　｜　主内容语言 **English (en)**　｜　[其他语言 / Other languages](#languages)

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

改文档 → 直接提 PR。改机制 → 先开 RFC issue（模板见 `CONTRIBUTING.md`）。价格、代币、拉人、募资类讨论一律关闭。讨论规范见 `CODE_OF_CONDUCT.md`。

## Languages

The primary content language is **English**. Localized pages are entry summaries (positioning, non-goals, status, authorship, license, links) — not full translations. The authoritative text is always the English edition; the Chinese whitepaper is the one full-text exception.

| Locale | Page | Coverage |
|---|---|---|
| en | this file / `DISCLAIMER.md` / whitepaper | authoritative |
| en | [`docs/en/`](docs/en/README.md) | handover + review docs (English edition) |
| zh | [`docs/i18n/zh.md`](docs/i18n/zh.md) · [`docs/whitepaper/zh/whitepaper.md`](docs/whitepaper/zh/whitepaper.md) | full whitepaper + summary |
| zh-Hant | [`docs/i18n/zh-Hant.md`](docs/i18n/zh-Hant.md) | summary |
| ru | [`docs/i18n/ru.md`](docs/i18n/ru.md) | summary |
| fr | [`docs/i18n/fr.md`](docs/i18n/fr.md) | summary |
| es | [`docs/i18n/es.md`](docs/i18n/es.md) | summary |
| ar | [`docs/i18n/ar.md`](docs/i18n/ar.md) | summary |
| ko | [`docs/i18n/ko.md`](docs/i18n/ko.md) | summary |
| id | [`docs/i18n/id.md`](docs/i18n/id.md) | summary |
| de | [`docs/i18n/de.md`](docs/i18n/de.md) | summary |
| pt | [`docs/i18n/pt.md`](docs/i18n/pt.md) | summary |

Coverage rules, translation constraints and known gaps: [`docs/i18n/README.md`](docs/i18n/README.md). Note that GitHub has no repository-level content-language setting — the sidebar "languages" are auto-detected by Linguist, so language coverage is declared here and in the matrix instead.

## 合规与作者角色

作者以研究化名 **Lee Hyun seok（이 현석）** 署名，不公开真实身份；不参与核心开发、不牵头、不运营、不运行节点、不提供兑换或中介服务，仅公开发布文档。本项目**在任何辖区均不开展**与虚拟货币相关的业务活动（发行、销售、兑换、撮合、定价、做市、托管、中介），不向任何辖区的用户提供上述服务。读者须自行评估所在地法律。详见 `DISCLAIMER.md` 与白皮书 §12。

The author publishes under a research pen name and does not disclose their identity, and takes no part in core development, leadership, operation, node running, exchange, or intermediation. A pen name is not a claim about nationality or identity. This repository is documentation for discussion only.

## License / Citation

MIT，适用于文档与后续代码。Copyright (c) 2026 Horizon Equilibrium Network contributors.

> Horizon Equilibrium Network Contributors. *Horizon Equilibrium Network (HEN): A Steady-State Peer-to-Peer Value Ledger.* Research draft v0.4.0, 2026.
