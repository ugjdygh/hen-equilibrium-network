# Glossary / 中英术语表

本文档统一全文用词。凡与白皮书不一致处，以白皮书为准；发现不一致请提 PR 修正。

## 1. 项目与文档

| 中文 | English | 定义 | 不要写作 |
|---|---|---|---|
| 衡远网络 | Horizon Equilibrium Network (HEN) | 本项目英文名 HEN 的标准中文名 | "稳态账本项目" |
| 稳态点对点价值账本 | Steady-State Peer-to-Peer Value Ledger | 技术副题，描述机制目标 | "稳态币" |
| 研究草稿 | research draft | 非规范性、可推翻的文档状态 | "白皮书定稿" |
| 非规范性 | non-normative | 不构成实现或部署要求的描述 | — |

## 2. 机制

| 中文 | English | 定义 |
|---|---|---|
| 稳态 | steady state | 一组可监测指标长期保持有界，不等于价格稳定 |
| 记账单位 | unit of account | 协议内部计量单位，非货币、非证券、非代币 |
| 用户轻节点 | user light node | 仅验证关键区块与自身交易的节点 |
| 验证节点 | validating node | 校验交易、维护交易池、转发候选交易 |
| 共识节点 | consensus node | 打包区块、参与共识、写入账本 |
| 有效最长链 | valid longest chain | 仅在通过完整验证的链之间比较长度 |
| 轻量混合共识 | lightweight hybrid consensus | 工作量证明作成本锚 + 验证履历权重 |
| 验证履历权重 | verification record weight | 由时间与可验证行为累积的参与权重，不可转让或购买 |
| 女巫抵抗 | Sybil resistance | 抑制低成本伪造大量身份的能力 |
| 难度目标 | difficulty target | 出块所需的证明阈值 |
| 熔断 | circuit breaker | 指标异常时冻结自动调节并转入人工评审 |

## 3. 经济

| 中文 | English | 定义 |
|---|---|---|
| 激励收敛 | convergent issuance | 奖励从启动期向长期微量水平收敛，而非衰减至零 |
| 保底奖励 | floor reward | 长期保留的微量激励，用于维持安全预算下限 |
| 手续费分流 | fee split | 手续费按激励/销毁/生态三路分配 |
| 沉睡资产 | dormant asset | 长期无签名活动的输出；默认不改变其所有权 |
| 回流 / 对冲 | reclamation / offset | 默认关闭的实验分支，指沉睡资产进入公共池，须满足 §7.4 全部条件 |
| 本金不可侵犯 | no-seizure default | 所有权不因不活跃而消灭的基线规则 |
| 流通稳态监测 | circulation monitoring | 对活跃度、沉睡率、增量与销毁量的持续公开观测 |

## 4. 隐私

| 中文 | English | 定义 |
|---|---|---|
| 遮蔽 | shielding | 隐藏交易细节关联的技术统称，不等于匿名 |
| 一次性地址 | one-time address | 每笔收款使用不同派生地址 |
| 承诺方案 | commitment scheme | 隐藏明文但可验证的方案（如 Pedersen 承诺） |
| 范围证明 | range proof | 证明隐藏金额落在合法区间而不暴露数值 |
| 选择性披露 | selective disclosure | 持有人主动向特定对象提供可验证信息 |
| 未授权关联 | unauthorized linkage | 未获持有人同意的地址聚类或身份推断 |

## 5. 治理

| 中文 | English | 定义 |
|---|---|---|
| 有界自动微调 | bounded auto-tuning | 在静态上下限与速率限制内自动调整参数 |
| 可逆演进 | reversible evolution | 每次调整留有可复算记录与回滚路径 |
| 向后兼容升级 | backwards-compatible upgrade | 旧节点可继续安全运行的升级方式 |
| 维护者 | maintainer | 负责流程与合并的贡献者，不拥有协议 |
| 决策记录 | decision record | 公开归档的接受/拒绝理由与反对意见摘要 |
| 分叉 | fork | 无法收敛时的独立链，自担责任 |

## 6. 易混词对照

| 不要写 | 应写作 | 原因 |
|---|---|---|
| 匿名币 / 匿名转账 | 遮蔽交易 | 不承诺绝对匿名，避免误导 |
| 挖矿收益 / 币价 | 激励 / 记账单位增量 | 本项目无代币、无价格 |
| 通胀率 | 记账单位年增量 | 避免套用货币框架 |
| 没收沉睡资产 | 默认不回收 | 基线规则是本金不可侵犯 |
| 官方 / 团队 | 贡献者 / 维护者 | 无运营主体，避免暗示组织存在 |
| 匿名池 / 隐私币 | 遮蔽字段 / 隐私方案 | 同第一行 |
| 上线 / 上所 | 不适用 | 本仓库无上线路径，用此词即误导 |

## 7. 状态标签（评审用）

| 标签 | 中文 | 含义 |
|---|---|---|
| `Draft` | 草稿 | 打磨中，未达可评审程度 |
| `Community Review` | 社区评审 | 等待外部反馈 |
| `Awaiting Security Review` | 待安全评审 | 需独立审计评估 |
| `Unmaintained / Archivable` | 待维护 / 可归档 | 无活跃维护者 |
| `Fork / Independent Implementation` | 分叉 / 独立实现 | 独立负责，非本仓库产物 |
| `Superseded` | 已被取代 | 保留原文但不再有效，注明取代者 |

**规则**：状态写在文件头部，与 `ROADMAP.md` 同步；不得把 `Draft` 写成"已通过评审"。

## 8. 角色与资产

| 中文 | English | 定义 |
|---|---|---|
| 创建者 | creator | 搭建仓库骨架、提供初始文档者，不牵头开发与运营 |
| 贡献者 | contributor | 提交文档或代码的人，意见与创建者同权 |
| 维护者 | maintainer | 负责流程与合并，无协议所有权与共识特权 |
| 设计资产 | design assets | 白皮书、规范、字段表、取舍分析、测试用例、风险清单 |
| 实现资产 | implementation assets | 节点、钱包、密码学实现、部署——由独立贡献者承接 |
| 冒用 | impersonation | 以本项目名义募资、发币、宣称官方或审计通过 |

## 9. 项目管理

| 中文 | English | 定义 |
|---|---|---|
| 评审状态 | review status | 见 §7 |
| 决策记录 | decision record (ADR) | 一条决策的背景、选项、决定、理由、代价、重审触发 |
| 兜底规则 | fallback rule | 无评审人时不认定通过；无人维护时归档 |
| 失败信号 | failure signal | 明确写出"该路径不成立"的触发条件（见 `ROADMAP.md`） |
| 条款缺一不可 | all-or-nothing clause | 七项条件须同时满足方可执行（白皮书 §7.4） |

## 10. 新增术语规则

1. 新术语先在本表登记，写清"定义"与"不要写作"。
2. 术语一旦登记，全文统一使用；旧写法在"易混词对照"保留，不直接删除。
3. 中英文名对应关系变更须记入 `CHANGELOG.md`（如"地平线均衡网络"→"衡远网络"）。
