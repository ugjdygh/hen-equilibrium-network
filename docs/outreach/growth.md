# 自然流量路线 / Organic Discoverability

本文件说明这个仓库如何被真实的人找到、被什么人 star、以及哪些做法我们明确不做。它不是营销方案，是一条**可复盘的渠道与度量清单**。

---

## 0. 先说结论：天花板在哪

- **GitHub Trending 对这个仓库基本不可达。** Trending 按短期 star 速度排序，且高度依赖语言/话题分类；本仓库 66 个文件全是 Markdown 与文本，GitHub 的语言统计返回 `language: null`（Linguist 无法归类），因此进不了任何语言榜。把目标定成"上 trending"会逼着人去刷 star，那是红线。
- **可达的目标是三个，按性价比排序：**
  1. 被 GitHub 站内搜索与 topic 页命中（长尾，稳定）；
  2. 被外部搜索引擎命中（靠 README 的英文摘要与固定术语）；
  3. 被少数开发者真正引用——引用一次（博客、awesome-list、实现仓库的 README 链接）比 100 个 star 有用。
- **star 的真实来源只有一个：仓库里有能跑、能抄、能省时间的东西。** 本站目前有三件：`examples/sim/incentive_sim.py`（零依赖可运行）、86 条验收用例、A1–A7/B1–B6/D1–D4/E1–E4 接口草图。文档型仓库若没有这三件，star 转化率通常在千次访问个位数。

---

## 1. 搜索面：四个入口，各自怎么打分

| 入口 | 排序依据 | 我们能控制的 | 现状 |
|---|---|---|---|
| GitHub 仓库搜索 `github.com/search?q=` | 名称 > description > topics > README 正文 | 仓库名、description、topics、README 首段 | description 已含 `distributed ledger / consensus / privacy / research`；topics 5 个 |
| GitHub Topics 页 `github.com/topics/<topic>` | 该 topic 下的 star 数排序 | 选对 topic、攒真实 star | 0 star 时不曝光，是**长期**资产 |
| 外部搜索引擎（Google/Bing） | 标题、首段、被引用次数 | README 英文摘要、被外链 | 刚建库，尚未被索引 |
| 学术/技术检索（Google Scholar 不收仓库） | 不适用 | — | 若日后成文，投 arXiv 需 endorsement，不列为近期动作 |

**仓库名不要再改。** `hen-equilibrium-network` 已经把 "equilibrium" 这个词占住了，改名的搜索收益远小于链接失效的代价。

### 1.1 关键词矩阵（目标查询 → 命中位置）

| 目标查询（研究者会输入） | 命中位置 | 当前状态 |
|---|---|---|
| `distributed ledger research` | description + topics | ✅ |
| `layered consensus protocol` | README 摘要 + 白皮书标题层 | ✅ |
| `steady state incentive design` | README 摘要 + `docs/research/tradeoffs.md` | ✅ |
| `privacy accountable ledger` | README 摘要 + 术语表 | ✅ |
| `consensus without single operator` | README 摘要 | ✅ |
| `no token distributed ledger` | description 末句 + DISCLAIMER | ✅ |
| `ledger handover documentation` | `docs/handover/` 标题 | ⚠️ 只在文件内，未进 README |

**注意一个反向筛选**：我们要的是"读协议设计的人"，不是"等空投的人"。因此 description 与 README 首屏刻意保留 `no token / no offering / no network`——它降低点击率，但提高 star 质量，也降低后续被仿冒诈骗的风险。这个取舍不要为了数字好看而取消。

---

## 2. 转化面：从"点进来"到"按下 star"

顺序是固定的：**30 秒内看懂这是什么 → 看到能跑的东西 → 决定 star 或离开**。

1. 首屏（README 前 20 行）：英文摘要 + 三条可用资产 + 一行状态徽章。已就位。
2. 第一个可执行动作：`python3 examples/sim/incentive_sim.py`。必须零依赖、5 秒内出结果。
3. 第一个可怀疑点：白皮书里不要有"将会""即将""预计上线"。当前为 0，保持。
4. 第一个可参与点：Discussions #1 与 issue 模板。已就位。

**建议但不强求**：在 `examples/sim/` 里放一张仿真输出的截图（PNG，<200KB）。纯文本仓库首屏没有图，视觉停留时间短。

---

## 3. 渠道清单

| 渠道 | 发什么 | 不发什么 | 预期 |
|---|---|---|---|
| GitHub 站内 | topics 维护、Discussions 回帖、给真实反馈开 issue | 给自己的仓库刷 issue/star | 低量、高质量 |
| awesome-list PR（如 `awesome-blockchain`、`awesome-distributed-systems` 一类仓库） | 一次 PR，一段符合对方模板的描述，诚实标注 Draft | 一次 PR 塞多个仓库；改别人条目 | 一个高权重外链，长期有效 |
| dev.to / Medium / 个人博客 | 教程体：*"我用 40 行代码验证一条激励曲线，发现熔断规则和调参预算互相打架"* | 项目宣传稿、白皮书摘要转载 | 教程是唯一在开发者社区被容忍的自我提及形式 |
| Hacker News（Show HN） | 不建议现在发。需有可用产物，否则会被判定为 self-promo | — | 现阶段负期望 |
| Reddit（r/ethereum、r/consensus 等） | 先读各版 self-promotion 规则，多数限制频次 | 跨版复制粘贴 | 高风险，非必要不发 |
| V2EX / 掘金 / 少数派（中文） | 一篇"文档型协议仓库怎么组织的"经验贴，附仓库链接 | 空投、项目前景 | 中文侧主要价值在**方法论**而非项目本身 |
| X / 微博 | 只发版本更新与具体结论 | 蹭币圈话题标签 | 低 |

**优先级**：教程（外部）> awesome-list PR（外部）> GitHub 站内维护 > 中文技术社区经验贴。前两者各做一次就够，不要重复投递。

---

## 4. 红线（任何一条破了，整个路线作废）

- 不购买 star / fork / watcher，不用小号互相点星，不组织"star 换 star"。
- 不做"关注仓库领空投 / 领白名单"类诱饵——这会立即吸引错误受众，并让仿冒者有了可乘之机。
- 不在禁止自我推广的社区发帖，不跨版复制粘贴，不用多个账号发同一内容。
- 不虚构"已上线""已审计""已获投资"。
- 不在标题或描述里使用 `token sale`、`presale`、`airdrop`、`listing` 这类词——即使是否定句，也会被搜索与推荐系统误判。

---

## 5. 四周节奏（可执行，不依赖任何人脉）

| 周 | 动作 | 产出 |
|---|---|---|
| W1 | 首屏与 description 定稿；把 `examples/sim` 的输出截图存入 `assets/`；确认 `docs/handover` 三件在主 README 里被链接 | README 改动 1 次提交 |
| W2 | 写一篇仿真教程（1000–1500 字，含代码片段与结论），发到 dev.to 或自己的博客 | 1 个外链；被引用起点 |
| W3 | 向 1–2 个 awesome-list 提 PR；在仓库内开 1 个"待决问题"discussion（从 `docs/research/open-questions.md` 的 Q1–Q10 取一个） | 1 个 PR；1 条讨论 |
| W4 | 复盘：看 GitHub Traffic（Insights）的 views / clones / referrers；按实际进来的搜索词改 description | 1 次 description 调整 |

四周之后停手。**重复投递同一内容是最常见的失败原因**，不是渠道不够多。

---

## 6. 度量与判据

GitHub 仓库 Insights（Traffic）提供 14 天窗口的 views、unique visitors、clones、referring sites，需要仓库 push 权限，admin 可见。

新仓库的合理基线（参考区间，非承诺）：

| 指标 | 头 30 天合理区间 | 说明 |
|---|---|---|
| unique visitors / 14 天 | 30–300 | 低于 30 说明没有外部入口；高于 300 通常来自单次社区曝光 |
| star / 千次访问 | 5–30 | 文档型仓库偏低；靠可运行资产拉高 |
| clone / 千次访问 | 3–15 | 我们的目标是 clone 高于 star——clone 的人才可能真用 |
| 外链 referrers | ≥ 1 | 没有外链，说明流量只来自站内搜索 |

**判据**：连续两周 referrers 为 0，且 clones 为 0，说明"可运行资产"没有起到作用，优先改首屏与 `examples/sim` 的说明，而不是加渠道。

---

相关文件：[`README.md`](../../README.md) · [`docs/research/open-questions.md`](../research/open-questions.md) · [`docs/review/process.md`](../review/process.md)
