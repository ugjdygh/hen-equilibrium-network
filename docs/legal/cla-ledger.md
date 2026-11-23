# CLA 签署记录 / Ledger

## 记录在哪里

**权威记录是仓库根目录的 [`CLA-SIGNATURES.md`](../../CLA-SIGNATURES.md)**，由 `.github/workflows/cla-sign.yml` 在签署 issue 下自动追加（一次签署，全仓库有效）。PR 里的签署仍有效，作为**辅助记录**存在：

1. **PR 会话本身**：贡献者在本人的 PR 中回复签署语句，该评论随仓库公开历史永久留存，不会被删除（删除也会留在 GitHub 的编辑历史里）。
2. **标签**：`cla: signed` 表示该 PR 的作者已在会话中签署；`cla: pending` 表示尚未签署。

状态迁移由 `.github/workflows/cla.yml` 自动完成，规则见 `CLA.md` §8。

## 为什么不做成一份签到表

- 名册需要人工同步，一定会滞后，且容易给出"这个人签过了"的错误印象；
- 匿名署名下，名册只会把"某个 GitHub 账号签过"写死，反而放大 §9.3 的主体不可核验问题；
- PR 会话是不可篡改的公开历史，比维护者手工维护的表格更可靠。

## 导出（需要维护者权限）

```bash
# 已签署的 PR 及其作者
gh pr list --repo ugjdygh/hen-equilibrium-network --label "cla: signed" \
  --state all --limit 500 --json number,author,createdAt,mergedAt

# 待签署
gh pr list --repo ugjdygh/hen-equilibrium-network --label "cla: pending" \
  --state all --limit 500 --json number,author,createdAt
```

需要正式名册时（例如进入原型阶段、或需要向合作方证明许可证链条完整），按上述输出生成一份带时间戳的文件，存 `docs/legal/stamps/`，方法同 `docs/legal/provenance.md` §3.2。

## 启用前的实测记录

用一次临时 PR 验证了两个状态（两条工作流运行均为 `success`）：

| 场景 | 观察到的结果 |
|---|---|
| 未签署的 PR（作者未回复） | 自动打 `cla: pending`；机器人只发一次提示，不重复刷屏 |
| 作者本人回复签署语句后 | 自动切换为 `cla: signed`，`cla: pending` 被移除 |

测试 PR 已关闭且未合并，分支已删除，`main` 无残留文件。

## 规则级模拟（8 个用例，全通过）

`tools/cla_sim.py` 把工作流的判定规则抽成离线用例，`python3 tools/cla_sim.py` 可复现：

| 用例 | 结果 |
|---|---|
| 单人 PR、作者未签 | `pending`（缺作者） |
| 单人 PR、作者已签 | `signed` |
| 多人 PR，作者签了但另一提交者未签 | `pending`（缺该提交者） |
| 多人 PR，两人都签 | `signed` |
| 机器人发签署语句 | 忽略，仍 `pending` |
| 路人（非作者非提交者）签署 | 不计入，仍 `pending` |
| 语句不完整（漏 "to its terms"） | 不计入，仍 `pending` |
| 签署后把评论编辑掉 | 重新判定为 `pending` |

**注意**：这是规则级验证，不是"另一个真实账号"的端到端验证。真实第三方测试需要在 GitHub 上由一个非作者账号开 PR 并评论，本仓库目前只有一个账号，未做该项测试。

## 已知限制

| 限制 | 影响 |
|---|---|
| 只核对"PR 作者本人是否发过签署语句" | 不核验真实身份；无法证明签约人是谁 |
| 不覆盖 email 补丁、私下发送的代码 | 这类贡献没有 PR 记录，需维护者单独要求签署 |
| 机器人 PR（`[bot]`）自动跳过 | 机器人贡献的实际权利人需另行确认 |
| 签署不产生雇佣、合作或报酬关系 | 见 `CLA.md` §9.4 |
