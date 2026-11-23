#!/usr/bin/env python3
"""CLA 判定规则的离线模拟（不联网，不涉及任何真实账号）。

用途：把 `.github/workflows/cla.yml` 的判定规则抽成可复现的用例，覆盖
"谁是应当签署的人""谁的签署会被认""多人 PR 会不会漏"。

这不是对真实第三方账号的测试：真实测试需要在 GitHub 上由一个非作者账号
打开 PR 并评论。此处只验证规则本身。

用法：python3 tools/cla_sim.py
"""
SIGN = "I have read CLA.md and I agree"

def decide(pr_author, commit_authors, comments):
    """返回 (label, missing, signers)。规则与 cla.yml 一致。"""
    required = {pr_author}
    for a in commit_authors:
        if a and not a.endswith("[bot]"):
            required.add(a)
    signers = set()
    for login, body in comments:
        if not login or login.endswith("[bot]"):
            continue
        if body and SIGN in body and login in required:
            signers.add(login)
    missing = sorted(required - signers)
    return ("cla: signed" if not missing else "cla: pending"), missing, sorted(signers)

CASES = [
    ("A1 单人 PR，作者未签", "alice", [], [("bob", SIGN)],
     ("cla: pending", ["alice"], [])),
    ("A2 单人 PR，作者已签", "alice", [], [("alice", SIGN)],
     ("cla: signed", [], ["alice"])),
    ("A3 多人 PR：作者签、另一提交者未签", "alice", ["bob"], [("alice", SIGN)],
     ("cla: pending", ["bob"], ["alice"])),
    ("A4 多人 PR：两人都签", "alice", ["bob"], [("alice", SIGN), ("bob", SIGN)],
     ("cla: signed", [], ["alice", "bob"])),
    ("A5 机器人的签署语句不算", "alice", [], [("dependabot[bot]", SIGN)],
     ("cla: pending", ["alice"], [])),
    ("A6 路人签署不算（非作者、非提交者）", "alice", [], [("mallory", SIGN)],
     ("cla: pending", ["alice"], [])),
    ("A7 语句不完整（缺 to its terms）不算", "alice", [], [("alice", "I have read CLA.md and agree")],
     ("cla: pending", ["alice"], [])),
    ("A8 签署后再编辑掉 → 重新判定为未签", "alice", [], [("alice", "LGTM")],
     ("cla: pending", ["alice"], [])),
]

def main():
    passed = 0
    print(f"{'用例':46} {'结果':14} {'缺失':16} 判定")
    print("-" * 92)
    for name, author, commits, comments, expect in CASES:
        got, missing, signers = decide(author, commits, comments)
        ok = (got, missing, signers) == expect
        passed += ok
        print(f"{name:46} {got:14} {','.join(missing) or '-':16} {'PASS' if ok else 'FAIL'}")
    print("-" * 92)
    print(f"{passed}/{len(CASES)} 通过")
    return 0 if passed == len(CASES) else 1

if __name__ == "__main__":
    raise SystemExit(main())
