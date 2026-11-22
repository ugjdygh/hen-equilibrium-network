# Changelog / 修订记录

---

## Unreleased — 语言切换 / 发现性 / 首屏

### 语言切换（本次）

- 切换栏按**真实覆盖**分两段：左段 `Full text` 只列有全文的 `en`、`zh`；右段 `Entry summaries (not full text)` 列其余 9 个语种。摘要页不得进入左段。
- 覆盖声明同步改写：`docs/i18n/README.md` 拆为 Tier A（全文 2）与 Tier B（摘要 9），并新增"晋级规则"——只有 `docs/whitepaper/<locale>/whitepaper.md` 完成全译、且切换栏与矩阵在同一提交内更新，才算晋级；仅新增摘要页不构成晋级。
- 根 `README.md` 的语言覆盖表改为两行式（Full text / Entry summary only），不再逐语种罗列后暗示同级。
- 覆盖到 `docs/en/README.md`、`docs/i18n/` 10 页、中英白皮书顶部；相对路径逐条校验，0 处断链。
- 白皮书为**双语全文切换**（中文全文 ↔ English full text）；其余 8 个语种仍为入口摘要页——这是内容覆盖的真实状态，未做全文翻译的地方不标注为全文。
- 事实记录：GitHub 无仓库级"内容语言"设置，侧栏 Languages 是 Linguist 按文件类型统计（本仓库全为 Markdown，返回 `language: null`），因此切换只能靠页间链接实现，无法做成站点级控件。

### 发现性与首屏

- README 首屏改为英文优先：新增 Abstract（English）与 "What you can actually use today"，把可运行的仿真脚本、86 条验收用例、接口草图提到第一屏；增加 status / license / no-token 三个徽章。
- 新增 `docs/outreach/growth.md`：四个搜索入口的排序依据、关键词矩阵、渠道清单（含各渠道"不发什么"）、红线、四周节奏、度量基线与判据。
- `description` 重写为可搜索句式（`consensus without a single operator` / `conditionable privacy` / `convergent incentives` / `parameter adaptation` / `86 acceptance cases`）；topics 增至 7 个（新增 `protocol-design`、`distributed-systems`）。
- 事实记录：GitHub 仓库搜索对 `consensus without a single operator` 的返回结果唯一命中本仓库，说明 description 关键词已进入索引；Trending 不可达的原因（全 Markdown、`language: null`）已写入 growth.md。

---

## v0.4.0 — 2026-11-22（匿名化 / 英文版 / 发布）

### 一、匿名化（本次最重要的改动）

| 项 | 原 | 现 |
|---|---|---|
| 作者身份 | 以单一籍属身份作为署名依据，并据此推论业务范围 | 以研究化名 `Lee Hyun seok（이 현석）` 署名，**不公开真实身份与国籍**（ADR-007） |
| 白皮书 §12.3 | 单一辖区合规环境 | "监管环境的差异"：以中国内地、欧盟 MiCA、美国证券框架为**示例**，辖区中立 |
| 合规承诺 | 仅在单一辖区不开展 | **在任何辖区均不开展**发行、销售、兑换、撮合、定价、做市、托管、中介 |

理由：合规范畴取决于项目做什么，不取决于作者在哪。把承诺从"某地不做"升级为"到处都不做"，反而更强；同时不再暴露任何可推断国籍或居所的信息（相关词已从正文、声明与元数据中清除；修订记录中亦不再复述具体国籍）。

代价：化名会引来"到底是谁"的猜测；`AUTHORS.md` 与 ADR-007 明确写明"化名不构成国籍、民族或身份声明"。**禁止**借化名暗示任何具体国籍，翻译亦不得本地化该姓名。

### 二、英文版补齐（原"主语言 English"承诺的兑现）

此前 README 声明主语言为英文，但 `docs/handover/` 与 `docs/review/` 实际为中文——这是不一致，本版修掉：

- 新增 `docs/en/`：`handover/{onboarding,module-map,api-sketch,test-cases}` + `review/{process,checklist,decisions}` 全量英译，**测试用例 86 条 ID 全部保留**（TC-TX-01 … TC-UG-04）。
- 新增 `docs/en/README.md`：覆盖矩阵、术语固定译法、以及"英文不得比中文更宽松"的规则。
- `docs/handover/project-guide.md` 明确**不翻译**（内部工作底稿，保留原文）。
- `docs/i18n/README.md` 与 README 语言表同步更新；已知缺口改为 `maintenance/`、`legal/`、`research/`、`spec/` 仅中文。

### 三、发布与协作入口

- 发布 `v0.4.0`，资产含中/英文白皮书 PDF（xelatex + Noto CJK，中文 12 页 / 英文 9 页）与 Markdown 源。
- 启用 GitHub Discussions，分类沿用平台默认（Announcements / General / Ideas / Polls / Q&A / Show and tell），并在 Q&A 创建与 `docs/review/process.md` 对齐的评审入口帖 [#1](https://github.com/ugjdygh/hen-equilibrium-network/discussions/1)（置顶需在网页端手动操作）。

### 四、待确认项

- 英文版为机助翻译，**尚未母语校对**；发现译文比中文宽松时，以中文为准并修英文。
- `docs/maintenance/`、`docs/legal/`、`docs/research/`、`spec/` 仍仅中文。
- zh-Hant 与 ar 入口页待母语校对。

---

## v0.3.1 — 2026-11-22（公开发布版）

本次为**仓库上线版本**：内容机制未改动（白皮书仍为 v0.3.0），仅新增署名、语言覆盖与发布信息。

### 新增

1. **研究化名署名**：作者以 `Lee Hyun seok（이 현석）` 公开署名，写入 `AUTHORS.md`、`README.md`、`CITATION.cff`、`DISCLAIMER.md`、中英文白皮书元信息表。
2. **语言覆盖**：`docs/i18n/` 下新增 10 个语种入口摘要页（zh、zh-Hant、ru、fr、es、ar、ko、id、de、pt）+ 语言矩阵 `docs/i18n/README.md`，主内容语言声明为 **English (en)**。
3. **公开发布**：仓库 `ugjdygh/hen-equilibrium-network` 上线，Description 仅英文。

### 说明（必须记录）

- **GitHub 没有仓库级"内容语言"设置。** 侧栏语言由 GitHub Linguist 按文件类型自动统计，反映的是代码而非文档语言。因此语言覆盖改为"文档内声明 + 入口页"实现，而非仓库设置项。
- 本地化页均为**摘要**，不含白皮书全文；中文是唯一有全文正文章节的例外（`docs/whitepaper/zh/whitepaper.md`）。
- 化名仅用于署名，不代表国籍或身份声明；合规立场（不开发、不运营、不背书）未变。

### 待确认项

- 是否把 `docs/handover/`、`docs/review/`、`spec/` 也做全文翻译（成本较高，当前无）。
- `zh-Hant` 与 `ar` 需要母语校对。

---

所有实质修改记入本文件，附理由。反对意见保留，不删除。

版本规则：文档类修订 Y 递增（v0.3.0 → v0.4.0）；纯勘误/路径修正 Z 递增。

---

## v0.3.0 — 2026-11-22（结构定稿版，可公开）

本次变更依据 `docs/handover/project-guide.md`（项目内部工作底稿）执行：把仓库从"一个大文档 + 几个附属文件"重组为「定位 / 规范 / 研究 / 接手 / 评审 / 维护 / 生态 / 法务」八段结构，并补齐交接材料。

### 一、命名定稿

| 项 | 原 | 现 |
|---|---|---|
| 英文名 | Steady Ledger（v0.1）→ Horizon Equilibrium Network（v0.2） | **Horizon Equilibrium Network（HEN）** |
| 中文名 | 待定（候选：衡续网络 / 衡远网络） | **衡远网络**（ADR-001；此前工作名"地平线均衡网络"已废弃） |
| 技术副题 | 稳态点对点价值账本 | 保留（承担解释功能） |
| GitHub slug | `hen-equilibrium-network`（依 GUIDE §2.1） | 不变 |
| 一句话定位 | — | An open research ledger for long-run balance. |

理由：中文名与英文语义对位（衡 = Equilibrium，远 = Horizon），二字可记；副题保留以免读者丢失内容定位。**代价**：`hen` 在英语中另有语义，英文读者可能觉得怪；若在意可换 `hen-network`，但需一次全局替换（ADR-001）。

### 二、结构重组（按 GUIDE §10）

| 原位置 | 现位置 |
|---|---|
| `docs/whitepaper.md` | `docs/whitepaper/zh/whitepaper.md`（权威）+ `docs/whitepaper/en/whitepaper.md`（英文版） |
| `docs/protocol/*` | `docs/protocol-draft/*`（并新增 `docs/protocol-draft/message-flow.md`、`validation-flow.md`） |
| `docs/glossary.md`、`docs/open-questions.md` | `docs/research/`（并新增 `docs/research/tradeoffs.md`、`comparison.md`、`references.md`） |
| `docs/roadmap.md` | `ROADMAP.md`（根目录） |
| `docs/review/CHANGELOG.md` | `CHANGELOG.md`（根目录） |
| — | 新增 `docs/handover/`（onboarding / module-map / api-sketch / test-cases） |
| — | 新增 `docs/review/`（process / checklist / decisions） |
| — | 新增 `docs/maintenance/`（handover / merge-rules） |
| — | 新增 `docs/ecosystem/implementations.md`、`docs/legal/disclaimer.md` |
| — | 新增 `spec/`、`examples/sim/`、`contrib/implementations/`、`assets/diagrams/`、`.github/` |

偏差：GUIDE §10 未列根目录的 `CONTRIBUTING.md` / `GOVERNANCE.md` / `SECURITY.md` / `CODE_OF_CONDUCT.md`。这些是平台惯例且原内容有效，保留于根目录，操作细节下沉到 `docs/maintenance/`，避免两处各自定义规则（ADR-006）。

### 三、新增内容（有实际价值的，不只是搬家）

1. **`docs/handover/onboarding.md`**：按角色分路径 + 接手七步 + 三条不能越的线 + 第一个可交付小任务（Q2 成本模型）。
2. **`docs/handover/module-map.md`**：14 个模块的规范/测试/仿真/开放问题/安全注意/验收六列对照 + 依赖图 + "最容易被做错的三处"。
3. **`docs/handover/api-sketch.md`**：`validate_tx` / `validate_block` / `compute_difficulty` / `compute_reward` 的输入输出与断言 A1–A7、B1–B6、D1–D4、E1–E4；含错误码枚举；明确"没有任何接口可以绕过校验"。
4. **`docs/handover/test-cases.md`**：86 条设计级用例，按 TX/BH/MT/MP/NW/VF/LV/CN/DA/EC/DM/PV/SC/UG 分类，优先覆盖失败路径。
5. **`docs/review/`**：评审角色与流程、状态标签、评审判据顺序、兜底规则、发布前清单、6 条 ADR。
6. **`docs/research/tradeoffs.md`**：15 项机制的三栏对照（收益/代价/边界），每条都写代价；标出"三个必须优先回答的取舍"。
7. **`docs/research/comparison.md`**：与 Bitcoin / Ethereum / Zcash / Monero / Tezos 的八维对比，含"最可能的失败模式"排序。
8. **`examples/sim/incentive_sim.py`**：可运行的示例仿真（纯标准库），产出三个可反驳的结论（见下）。
9. **`assets/diagrams/`**：两张手写 SVG（分层网络、问题闭环），离线可读。
10. **`.github/` 三种 issue 模板 + PR 模板**：强制"位置—问题—理由—建议"与合规自检。

### 四、仿真带来的两个结论（已回写 Q4 / Q6）

1. `g(t) = 0.5% + 7.5%·exp(-t/8)` 在第 25 年后全部低于 1%，**稳态期年增量可被压在 0.3%–1.0%**；代价是前 10 年明显偏高，且总量无上限。
2. **"连续同向 3 次即熔断"与幅度需求冲突**：算力跃升 1.8× 需累计 +80% 调整，但连续 3 次上调即冻结，末态目标 13.3 / 18.0，**未收敛**。初步结论：熔断条件应改为"累计幅度 + 时间窗"，或冻结后仅暂停并降增益。

这两条是玩具模型结论，已写入 `docs/research/open-questions.md` Q4 / Q6 的"当前结论"。

### 五、被拒绝的修改（记录理由）

- **中文名用"衡续"而非"衡远"**：拒绝。英文名的主词是 Horizon，"衡远"对位更紧；"衡续"更适合强调永续激励的单点卖点，但会让中英文名各自指向不同重点。备选保留，若后续改名需全局替换。
- **把 `spec/` 填成占位规范**：拒绝。账本模型（Q9）与难度闭环（Q6）未定，此时写规范等于固化未验证内容（见 `spec/README.md`）。
- **保留 `docs/roadmap.md` 与根 `ROADMAP.md` 两份**：拒绝。两处写同一件事必然不一致，只留根目录一份。
- **给示例脚本加代币分配/价格模型**：拒绝，属白皮书 §12 禁止范围。
- **加"官方实现"目录**：拒绝。主仓库只留说明，不复制代码（ADR-004）。

### 六、待确认项

- GitHub slug 是否已被占用（发布前检索）；`hen` 的语义歧义是否接受。
- 阶段 1 的仿真脚本清单（Q2 / Q3 / Q6 三个脚本待认领）。
- 是否需要第三语言版本（当前仅中/英）。

---

## v0.2.0 — 2026-11-22（首次公开准备版）

### 必须修改（不改则不可公开）

1. **删除会话残留语句。** 原文末尾"需要我把这一版再压缩成「一页纸摘要 + 完整正文」两套可直接导出的 Markdown 文件吗？"属对话产物，已删除。
2. **拆出内嵌的 README 与"使用建议"。** 原文把仓库入口与使用建议写在正文之后，已拆为独立文件与目录结构。
3. **补全 License 主体。** 原文只在署名行写 `License：MIT`，现补齐 `LICENSE` 全文，版权主体为"Horizon Equilibrium Network contributors"。
4. **沉睡资产改为"默认不回收"。** 原文整体读作默认可没收，且无门槛、无恢复路径、无法律冲突处理。现为基线本金不可侵犯 + 默认关闭的实验分支（七项条件，缺一不可）。
5. **新增合规立场章。** 原文只有一句"监管风险"。现明确不发行、不募资、不运营、不提供兑换中介，并陈述代表性辖区的监管事实（非法律意见）。
6. **隐私章加"非规避监管"边界。** "抗去匿名化"改为"降低未授权关联"，明确不设计隐藏非法所得或逃避司法的功能。
7. **显式声明"不发行代币"。** 界定"资产/金额/供应量"为协议内部记账单位，无预留、无私售、无金库。
8. **参考文献补为可核验条目。** 原文 4 条为概括描述，现为 12 条含作者与出处。

### 结构性优化

9. 新增 §2 设计原则（七条 + 显式优先级）。
10. 新增 §3.7 问题耦合关系。
11. 新增 §14 开放问题、§15 关键术语、附录 A 命名沿革。
12. §6 增三条设计禁令（不得持币定权、不得购买权重、不得单一实体否决）。
13. §10 治理从描述改为可执行规则。
14. §13 研究路线加退出条件。
15. §11 补社会工程风险。
16. 术语统一：遮蔽（非匿名）、记账单位（非货币）、贡献者/维护者（非"团队/官方"）。

### 被拒绝的修改

- 彻底删除沉睡议题：拒绝，会让 §7 论证失去对手方。
- 给参数填具体最终值：拒绝，无仿真支撑的定值会被读作承诺。
- 按章节拆成 13 个独立文件：拒绝，单文件更利于引用与版本比对。
- 加代币经济分配表：拒绝，属禁止范围。

---

## v0.1.0 — 2026-11（初稿，未公开）

以 "Steady Ledger / 稳态点对点价值账本" 为工作名建立初稿，13 章，末尾附 README 草稿与使用建议。

已知缺陷：命名待定、缺合规立场、缺设计原则、沉睡机制表述过强、参考文献不可核验、含会话残留语句。

---

## 记录格式

```
## vX.Y.Z — YYYY-MM-DD

### 变更
- （文件/章节）：（改了什么）

### 理由
（为什么必须改；不改会怎样）

### 反对意见
（若有，摘要保留）

### 待确认项
（仍未解决的问题）
```
