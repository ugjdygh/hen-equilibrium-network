# CLA 签署记录 / Ledger

## 记录在哪里

本仓库**不维护集中式的签署名册**。签署记录由两样东西构成：

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

## 已知限制

| 限制 | 影响 |
|---|---|
| 只核对"PR 作者本人是否发过签署语句" | 不核验真实身份；无法证明签约人是谁 |
| 不覆盖 email 补丁、私下发送的代码 | 这类贡献没有 PR 记录，需维护者单独要求签署 |
| 机器人 PR（`[bot]`）自动跳过 | 机器人贡献的实际权利人需另行确认 |
| 签署不产生雇佣、合作或报酬关系 | 见 `CLA.md` §9.4 |
