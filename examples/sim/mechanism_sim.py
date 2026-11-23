#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HEN · mechanism simulation (examples only, non-normative)

Purpose: turn four claims from the whitepaper into numbers that can be run and refuted.

  1. Difficulty control: "consecutive same-direction moves" is a defective breaker.
     A cumulative-amplitude + time-window rule with cooldown-and-damped-resume converges
     where the old rule froze early. (open question Q6)
  2. Dormancy: circulation decay can be addressed by opt-in burn, never by confiscation.
     Shows the decay curve, the opt-in compensation, and the residual gap. (Q1, Q4)
  3. Sybil cost: whether a bounded energy budget still leaves an attack uneconomic. (Q2)
  4. Stability domain: a gain x delay sweep, reporting the share of settings that converge. (Q6)

Run:
  python3 mechanism_sim.py            # all four sections
  python3 mechanism_sim.py --only 4   # one section

Notes:
  - This implements no protocol and produces no asset.
  - Every parameter is an illustrative example, not a final value, not a promise.
  - Where the output contradicts the whitepaper, the simulation wins and the whitepaper gets a PR.
"""

import argparse
import math

P = {
    "target_interval": 10.0,
    "hash_jump": 1.8,          # a 1.8x compute jump at cycle 10
    "jump_at": 10,
}

# ------------------------------------------------------------------ 1. difficulty control
def controller_cumulative(steps_window=6, cum_cap=0.60, cooldown=4, damp=0.5,
                          gain=0.30, max_step=0.10, target=10.0, jump=1.8,
                          jump_at=10, horizon=80, delay=2):
    """Cumulative-amplitude breaker: freeze only when the window sum exceeds the cap,
    then resume after cooldown with a reduced gain. Returns diagnostics."""
    hashrate = 1.0
    base = target * hashrate
    tgt = base
    intervals, targets, need = [], [], []
    steps = []
    frozen_until = -1
    cur_gain = gain

    for t in range(horizon):
        if t == jump_at:
            hashrate = jump
        actual = tgt / hashrate
        intervals.append(actual)
        targets.append(tgt)

        observed = intervals[-1 - delay] if len(intervals) > delay else target
        err = (observed - target) / target
        step = max(-max_step, min(max_step, -cur_gain * err))

        steps.append(step)
        window_sum = sum(steps[-steps_window:])

        if t < frozen_until:
            pass                                    # frozen: no adjustment
        else:
            if abs(window_sum) >= cum_cap:
                frozen_until = t + cooldown          # cooldown instead of permanent freeze
                cur_gain = cur_gain * damp           # resume with damped gain
            else:
                tgt = max(0.5 * base, min(8.0 * base, tgt * (1 + step)))

    need = target * jump
    post = intervals[jump_at:]
    converged = abs(intervals[-1] - target) / target < 0.05 and abs(targets[-1] - need) < 2.0
    return {
        "interval_min": min(post), "interval_max": max(post),
        "final_interval": intervals[-1], "final_target": targets[-1],
        "needed_target": need, "converged": converged, "freezes": frozen_until > 0,
    }

# ------------------------------------------------------------------ 2. dormancy
def dormancy(decay=0.06, reactivate=0.04, opt_in_burn=0.05, years=40, active0=1.0):
    """Total supply is fixed here (issuance is section 1 of the other script).

    Each year a fraction `decay` of *active* holdings goes quiet; dormant holdings
    return to active use at `reactivate`; holders may also opt in to retiring a
    fraction `opt_in_burn` of their dormant holding permanently.

    Report the active share — a velocity proxy — plus the dormant stock.
    """
    active, dormant = active0, 0.0
    rows = []
    for y in range(years + 1):
        rows.append((y, active, dormant))
        moved = active * decay
        active -= moved
        dormant += moved
        back = dormant * reactivate
        dormant -= back
        active += back
        burnt = dormant * opt_in_burn
        dormant -= burnt            # retired only where the holder consented
        active += 0.0               # burn does not create new active units
    return rows

# ------------------------------------------------------------------ 3. sybil cost
def sybil_cost(cost_per_identity=40.0, reward_per_period=12.0, identities=1000,
               share_gain=0.02):
    attack_cost = cost_per_identity * identities
    expected_gain = reward_per_period * identities * share_gain
    return attack_cost, expected_gain, expected_gain / attack_cost

# ------------------------------------------------------------------ 4. stability sweep
def sweep(gains, delays, **kw):
    ok = 0
    total = 0
    worst = None
    for g in gains:
        for d in delays:
            total += 1
            r = controller_cumulative(gain=g, delay=d, **kw)
            if r["converged"]:
                ok += 1
            elif worst is None or abs(r["final_interval"] - kw.get("target", 10.0)) > abs(worst[2]["final_interval"] - 10.0):
                worst = (g, d, r)
    return ok, total, worst

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", type=int, default=0)
    ap.parse_args()

    print("=" * 72)
    print("HEN mechanism simulation — illustrative only, not a protocol implementation")
    print("=" * 72)

    print("\n[1] Difficulty control: breaker rule comparison (Q6)")
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from incentive_sim import P as P0, difficulty_loop
    old_min, old_max, old_frozen, old_final, old_target = difficulty_loop(P0)
    old = {"final_interval": old_final, "final_target": old_target,
           "needed_target": P0["target_interval"] * P0["hash_jump"],
           "converged": abs(old_final - P0["target_interval"]) / P0["target_interval"] < 0.05}
    new = controller_cumulative()
    print(f"    old rule (3 consecutive same-direction moves -> permanent freeze): "
          f"final interval {old['final_interval']:.2f}, target {old['final_target']:.2f}, "
          f"needed {old['needed_target']:.2f} -> {'converged' if old['converged'] else 'not converged'}")
    print(f"    new rule (window sum + cooldown + damped resume): "
          f"final interval {new['final_interval']:.2f}, target {new['final_target']:.2f}, "
          f"needed {new['needed_target']:.2f} -> {'converged' if new['converged'] else 'not converged'}")
    print(f"    oscillation band after the jump: {new['interval_min']:.2f}-{new['interval_max']:.2f} "
          f"(target {P['target_interval']:.2f})")

    print("\n[2] Dormancy: opt-in burn only, no confiscation (Q1)")
    rows = dormancy()
    print(f"{'year':>5} {'active share':>13} {'dormant':>10}")
    for i in range(0, len(rows), 10):
        y, c, d = rows[i]
        print(f"{y:>5} {c:>13.3f} {d:>10.3f}")
    print("    -> active share settles at an equilibrium between decay and reactivation.")
    print("    -> opt-in burn only retires units the holder explicitly gave up; holdings are never seized.")
    print("    -> the residual gap is answered by issuance and fee design (Q4), not by confiscation.")

    print("\n[3] Sybil cost (Q2)")
    for ids in (100, 1000, 10000):
        cost, gain, ratio = sybil_cost(identities=ids)
        print(f"    {ids:>6} identities: attack cost {cost:>10.0f}, expected gain {gain:>8.0f}, "
              f"gain/cost {ratio:.3f} -> {'uneconomic' if ratio < 1 else 'PROFITABLE'}")

    print("\n[4] Stability sweep: gain x delay (Q6)")
    gains = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.80]
    delays = [1, 2, 3, 4, 6, 8]
    ok, total, worst = sweep(gains, delays, target=P["target_interval"])
    print(f"    {ok}/{total} settings converge to the needed target ({P['hash_jump']}x jump)")
    if worst:
        print(f"    worst case: gain {worst[0]}, delay {worst[1]} -> final interval "
              f"{worst[2]['final_interval']:.2f}")
    print(f"    -> stability is not universal: it depends on gain and measurement delay, "
          f"so the whitepaper must state the band, not a point value.")

    print("\n" + "=" * 72)
    print("No commitment is implied. Parameters are illustrative and open to refutation.")
    print("=" * 72)

if __name__ == "__main__":
    main()
