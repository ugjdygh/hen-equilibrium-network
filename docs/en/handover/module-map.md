# Module Map

**Purpose:** break "what must be built" into claimable units. Each module lists spec location, test cases, simulation, open question, security caveat, and acceptance criteria.

**Status:** everything is `Draft` or `Open`. There is no implementation.

Source of truth: `docs/handover/module-map.md` (Chinese).

---

## 1. Master table

| Module | Spec | Tests | Simulation | Open Q | Acceptance | Status |
|---|---|---|---|---|---|---|
| Transaction structure | `docs/protocol-draft/transaction.md` | TC-TX-01..12 | — | Q9 | serializable, verifiable, invalid inputs rejected | `Draft` |
| Block header | `docs/protocol-draft/block-header.md` | TC-BH-01..06 | — | Q6 | integrity verifiable; undefined flags invalid | `Draft` |
| Merkle tree / inclusion proofs | whitepaper §5.3 | TC-MT-01..04 | — | — | light node verifies inclusion/exclusion independently | `Draft` |
| Mempool | whitepaper §4 | TC-MP-01..06 | backlog curve | Q6 | rejects invalid transactions; backlog recomputable | `Draft` |
| Message flow | `docs/protocol-draft/message-flow.md` | TC-NW-01..05 | propagation delay | — | layered forwarding loses nothing, amplifies nothing | `Draft` |
| Validation flow | `docs/protocol-draft/validation-flow.md` | TC-VF-01..05 | — | — | ordering and short-circuit rules fixed; no skip path | `Draft` |
| Light validating node | whitepaper §4 | TC-LV-01..05 | — | — | passes base cases; never degrades into trusting peers | `Draft` |
| Consensus node | whitepaper §6.1 | TC-CN-01..06 | block rate | Q2 / Q3 | passes sim + tests; no privileged branch | `Draft` |
| Difficulty adjustment | whitepaper §6.2 | TC-DA-01..08 | `examples/sim/` | Q6 / Q8 | reproducible output; bounds never exceeded | `Open` |
| Steady-state incentives | whitepaper §7.2 / §7.3 | TC-EC-01..06 | `examples/sim/incentive_sim.py` | Q4 | reproducible; annual growth respects cap | `Draft` |
| Dormancy / reflow (experimental) | whitepaper §7.4 | TC-DM-01..05 | to build | Q1 | off by default; all seven conditions; freeze on legal conflict | `Open` |
| Shielding | whitepaper §8.2 | TC-PV-01..06 | boundary analysis | Q5 | passes boundary tests; no anonymity promise | `Draft` |
| Conditional transactions | whitepaper §9 | TC-SC-01..08 | — | — | fail-closed; no downgrade path | `Draft` |
| Upgrade & governance | whitepaper §10 | TC-UG-01..04 | — | — | distinguishes auto-tuning from material change | `Draft` |

## 2. Module card (copy and fill when claiming)

```
### Module: <name>
Status: Draft | Community Review | Aw awaiting Security Review | Unmaintained
Spec: <file + section>
Tests: <case IDs>
Simulation: <script path> (or "none")
Open question: <Q number>
Security caveat: <the one thing most likely to be implemented wrong>
Acceptance: <objective pass/fail condition>
Claimant: <GitHub handle>   (claiming is not owning — see GOVERNANCE.md)
```

## 3. Dependencies

```
Transaction structure ─┬─> Merkle tree ─> Block header ─> Consensus node
                      ├─> Mempool ─> Light validating node
                      ├─> Conditional transactions
                      └─> Shielding (depends on crypto selection, Q5)
Difficulty adjustment ──> Consensus node ──> Steady-state incentives (needs block stats)
Message flow ──> Validation flow ──> Mempool
```

**Suggested build order:** transaction → Merkle → block header → mempool → validation flow → difficulty → consensus → incentives → conditions → shielding. Shielding comes last because it changes encoding assumptions for everything before it.

## 4. Three things most often implemented wrong

1. **Condition failure downgrade.** The tempting shortcut is "after timeout anyone may spend". This is the single largest source of fund loss. Must be fail-closed.
2. **Undefined flags.** The tempting shortcut is "ignore unknown bits". That turns a compatibility mechanism into a bypass. Must be treated as invalid.
3. **Difficulty measurement delay.** Implementations often assume delay = 0, so it looks stable in simulation and oscillates on a real network (Q6).

## 5. What must accompany a handover

Spec location, test cases, simulation script, known unresolved issues, and the pitfalls you personally hit — written down, not left in code.
