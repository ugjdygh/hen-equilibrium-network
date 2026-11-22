# 接口草稿 / API Sketch

**性质**：只定义输入、输出与断言，不写死具体语言实现。**这不是代码，也不保证可编译。**

目的：让不同实现者在不争论语言的前提下，先对"校验必须做什么"达成一致。

---

## 1. 约定

- 所有函数为纯函数式描述：相同输入必须给出相同输出。
- 所有失败都返回**结构化原因**，不允许只返回布尔值（否则无法定位、无法写测试）。
- 所有函数必须声明其**信任边界**：它假设调用方已校验了什么、自己又校验了什么。
- 未定义字段一律视为无效，而非忽略。

## 2. 交易校验

```text
validate_tx(tx, utxo_set, rules)
  -> (valid: bool, errors: list<Reason>, metadata: Metadata)

输入：
  tx        交易（含 inputs, outputs, fee, signatures, conditions, shielding）
  utxo_set  可花费输出集合（或账户状态快照，取决于 Q9 结论）
  rules     规则集（含最大脚本成本、最小手续费、字段合法性表）

断言：
  A1 任一 input 引用不存在或已花费的输出 → valid=false, reason=INPUT_MISSING
  A2 签名覆盖的交易哈希与实际不符 → valid=false, reason=SIG_INVALID
  A3 输入总额 < 输出总额 + 手续费 → valid=false, reason=VALUE_MISMATCH
      （遮蔽场景下改为"范围证明成立"，见 A4）
  A4 遮蔽字段的承诺与范围证明不成立 → valid=false, reason=SHIELD_INVALID
  A5 条件字段未满足 → 输出保持锁定（不是整笔失败，也不是降级为可花费）
  A6 未定义的条件类型或标志位 → valid=false, reason=UNDEFINED_FIELD
  A7 脚本资源用量超过静态上界 → valid=false, reason=SCRIPT_TOO_COSTLY

信任边界：
  本函数不验证 PoW，不验证区块上下文，不知道交易在链上的位置。
```

## 3. 区块校验

```text
validate_block(block, prev_block, difficulty_target, chain_ctx)
  -> (valid: bool, reason: Reason, stats: Stats)

断言：
  B1 prev_block_hash 与已知父块一致 → 否则 reason=PREV_MISMATCH
  B2 merkle_root 可被交易集合复算 → 否则 reason=MERKLE_MISMATCH
  B3 版本位与扩展标志位均在已定义集合内 → 否则 reason=UNDEFINED_FLAG
  B4 时间戳落在容差窗口内且满足中位时间规则 → 否则 reason=TIMESTAMP
  B5 工作量证明满足 difficulty_target → 否则 reason=PROOF_INVALID
  B6 区块内所有交易通过 validate_tx → 否则 reason=TX_INVALID(<tx id>)

信任边界：
  本函数不判断该链是否为"最有效的长链"，链选择由调用方完成。
```

## 4. 难度计算

```text
compute_difficulty(history, node_metrics, bounds)
  -> target: Target

输入：
  history       最近 N 个区块的出块间隔、难度、算力估计
  node_metrics  活跃共识节点数、分布离散度、交易池积压
  bounds        静态上下限、单步幅度上限、连续调整次数上限

断言：
  D1 输出必在 bounds 内 → 越界即钳制，并记录 CLAMPED 事件
  D2 单步变化不超过 bounds.max_step
  D3 连续同向调整达上限即触发熔断 → 返回冻结标记，而非继续调整
  D4 相同输入必得相同输出（禁止使用本地随机源或本地时钟）

信任边界：
  history 与 node_metrics 可能是被攻击者部分影响的数据；
  本函数必须假设输入可被污染，因此需要 D1/D2 的硬钳制。
```

## 5. 激励与手续费

```text
compute_reward(block_stats, params)
  -> (issuance: Amount, fee_split: {incentive, burn, ecosystem}, notes)

断言：
  E1 issuance 不超过 params.annual_growth_cap（按年折算）
  E2 burn 记录可被第三方从交易数据独立复算
  E3 ecosystem 部分不得指向任何个人账户
  E4 fee_split 三部分之和等于总手续费（无遗漏、无凭空生成）
```

## 6. 错误原因枚举（建议）

```text
Reason =
  | INPUT_MISSING | SIG_INVALID | VALUE_MISMATCH | SHIELD_INVALID
  | UNDEFINED_FIELD | UNDEFINED_FLAG | SCRIPT_TOO_COSTLY
  | PREV_MISMATCH | MERKLE_MISMATCH | TIMESTAMP | PROOF_INVALID
  | TX_INVALID(<id>) | CLAMPED | FROZEN
```

新增原因须走 RFC，因为下游实现会用它对用户展示错误信息。

## 7. 明确不做的事

- 不定义网络传输格式（见 `docs/protocol-draft/message-flow.md`）。
- 不定义持久化结构。
- 不定义钱包与 UI 接口。
- 不引入任何"管理员覆盖"参数——没有任何接口可以绕过 A1–A7、B1–B6。
