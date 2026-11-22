#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HEN · 激励与调节的最小示例仿真 (examples only, non-normative)

目的：让白皮书里的三个参数主张变成可以跑、可以反驳的数字。
   1) 收敛式发行 vs 减半：稳态期年增量是否落在 0.3%–1.0% 区间；
   2) 手续费三路分流：三部分是否恒等于总手续费；
   3) 延迟闭环下的难度调节：算力跃升后是否收敛，还是自激振荡（开放问题 Q6）。

运行：
   python3 incentive_sim.py              # 默认 40 年
   python3 incentive_sim.py --years 60

注意：
   - 本脚本不实现任何协议，不产生任何资产。
   - 所有参数都是"示例参数"，用于讨论，不是最终取值，也不是承诺。
   - 结论若与白皮书冲突，以仿真结果为准，并提 PR 修改白皮书。
"""

import argparse
import math

# ---------------------------------------------------------------- 参数（示例）
P = {
    "years": 40,
    "g0": 0.08,            # 启动期年增量 8%（仅示例，不是比特币参数）
    "g_floor": 0.005,      # 长期保底年增量 0.5%
    "tau": 8.0,            # 收敛时间常数（年）
    "supply0": 1.0,        # 归一化初始供应，仅观察相对变化
    "steady_from": 25,     # "稳态期"起点（约 3×tau，年增量降到 1% 以下）
    "fee_split": (0.60, 0.20, 0.20),
    "target_interval": 10.0,
    "delay": 2,            # 测量延迟（调节周期数）
    "gain": 0.30,          # 调节增益
    "max_step": 0.10,      # 单步幅度上限 ±10%
    "consecutive_cap": 3,  # 连续同向调整上限 → 熔断
    "hash_jump_at": 10,    # 第 10 周期算力跃升
    "hash_jump": 1.8,
}


def growth_rate(year, p):
    """收敛式年增量：从 g0 指数收敛到 g_floor。"""
    return p["g_floor"] + (p["g0"] - p["g_floor"]) * math.exp(-year / p["tau"])


def issuance_curve(p):
    supply, rows = p["supply0"], []
    for y in range(p["years"] + 1):
        g = growth_rate(y, p)
        rows.append((y, g, supply))
        supply *= (1 + g)
    return rows


def halving_curve(p, era_years=4.0, initial_rate=0.08):
    """对照模型：每 4 年发行速率减半（形状对照，非真实参数）。"""
    supply, rows = p["supply0"], []
    for y in range(p["years"] + 1):
        g = initial_rate / (2 ** int(y // era_years))
        rows.append((y, g, supply))
        supply *= (1 + g)
    return rows


def fee_split(fee_total, p):
    inc, burn, eco = p["fee_split"]
    parts = (fee_total * inc, fee_total * burn, fee_total * eco)
    assert abs(sum(parts) - fee_total) < 1e-9, "分流之和必须等于总手续费"
    return parts


def difficulty_loop(p):
    """第 10 周期算力跳升 1.8 倍；控制器只能看到延迟 delay 个周期的间隔。"""
    hashrate = 1.0
    target0 = p["target_interval"] * hashrate
    target = target0
    intervals, targets = [], []
    last_sign, consecutive, frozen = 0, 0, False

    for t in range(80):
        if t == p["hash_jump_at"]:
            hashrate = p["hash_jump"]
        actual = target / hashrate
        intervals.append(actual)
        targets.append(target)

        if len(intervals) > p["delay"]:
            observed = intervals[-1 - p["delay"]]
            err = (observed - p["target_interval"]) / p["target_interval"]
        else:
            err = 0.0

        step = max(-p["max_step"], min(p["max_step"], -p["gain"] * err))
        sign = 0 if abs(step) < 1e-12 else (1 if step > 0 else -1)
        if sign != 0:
            consecutive = consecutive + 1 if sign == last_sign else 0
            last_sign = sign
        if consecutive >= p["consecutive_cap"]:
            frozen = True
        if not frozen:
            target = max(0.5 * target0, min(8.0 * target0, target * (1 + step)))

    post = intervals[p["hash_jump_at"]:]
    return min(post), max(post), frozen, intervals[-1], targets[-1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--years", type=int, default=P["years"])
    args = ap.parse_args()
    p = dict(P)
    p["years"] = args.years

    print("=" * 68)
    print("HEN 激励与调节示例仿真 —— 非协议实现，仅用于讨论")
    print("=" * 68)

    print("\n[1] 收敛式发行 vs 减半（相对供应，归一化起点 = 1.0）")
    print(f"{'年':>4} {'收敛式年增量':>13} {'收敛式供应':>12} {'减半式年增量':>13} {'减半式供应':>12}")
    conv, half = issuance_curve(p), halving_curve(p)
    for i in range(0, len(conv), max(1, len(conv) // 10)):
        y, g, s = conv[i]
        _, gh, sh = half[i]
        print(f"{y:>4} {g*100:>12.2f}% {s:>12.4f} {gh*100:>12.2f}% {sh:>12.4f}")

    steady = [g for y, g, _ in conv if y >= p["steady_from"]]
    ok = all(0.003 - 1e-12 <= g <= 0.010 + 1e-12 for g in steady)
    print(f"    → 稳态期（第 {p['steady_from']} 年起）年增量是否全在 0.3%–1.0%：{'是' if ok else '否'}")
    print(f"    → 启动期年增量最高 {conv[0][1]*100:.2f}%；这段属'适度释放以启动网络'，不计入稳态区间。")
    print("    → 保底年增量意味着总量无上限；是否可接受由 Q4 回答，本脚本不替你下结论。")

    print("\n[2] 手续费分流（示例：年手续费总量 = 1.00）")
    inc, burn, eco = fee_split(1.0, p)
    print(f"    激励 {inc:.2f} | 销毁 {burn:.2f} | 生态 {eco:.2f} | 合计 {inc+burn+eco:.2f}")
    print("    → 断言：三部分之和恒等于总手续费（无遗漏、无凭空生成）")

    print("\n[3] 延迟闭环下的难度调节（开放问题 Q6）")
    lo, hi, frozen, final_interval, final_target = difficulty_loop(p)
    ratio = hi / lo if lo > 0 else float("inf")
    print(f"    测量延迟 {p['delay']} 周期 | 增益 {p['gain']} | 单步上限 ±{p['max_step']*100:.0f}% "
          f"| 连续上限 {p['consecutive_cap']} 次")
    print(f"    算力跃升 {p['hash_jump']}× 后的出块间隔：{lo:.2f} – {hi:.2f}（目标 {p['target_interval']:.2f}）")
    print(f"    最大/最小比 {ratio:.2f} | 熔断触发 {'是' if frozen else '否'}")
    need_target = p["target_interval"] * p["hash_jump"]
    converged = abs(final_interval - p["target_interval"]) / p["target_interval"] < 0.05
    print(f"    末态出块间隔 {final_interval:.2f} | 末态目标 {final_target:.2f} | 需要目标 {need_target:.2f} "
          f"→ {'已收敛' if converged else '未收敛'}")
    if frozen and not converged:
        print("    → 关键发现：以'连续同向次数'作为熔断条件，会在算力阶跃时过早冻结，")
        print("      阻止了必要的一轮累计调整（本例需要 +80%）。")
        print("      改进方向：熔断改用'累计幅度 + 时间窗'，或熔断后仅暂停并降增益，而非永久冻结。")
    if ratio > 1.5:
        print("    → 该组参数下出现明显振荡。Q6 不是修辞，是必须解决的问题。")
        print("      可试：降低增益、缩短延迟、改用积分型调节并加阻尼。")
    else:
        print(f"    → 振荡幅度受控（最大/最小 {ratio:.2f}），但收敛结论见上一条；单点结果不等于鲁棒，需扫描增益与延迟网格。")

    print("\n" + "=" * 68)
    print("本输出不构成任何承诺；参数为示例，可被任意反驳。")
    print("=" * 68)


if __name__ == "__main__":
    main()
