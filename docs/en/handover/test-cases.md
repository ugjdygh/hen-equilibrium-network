# Test Cases

**Nature:** design-level cases, not executable tests. Each implementation maps these IDs to its own test functions and back-fills pass/fail.

**Principle:** cover the **failure paths** first. Protocols die on "everything normal passes, nothing abnormal was tested".

Format: `ID | scenario | expected | basis`

Source of truth: `docs/handover/test-cases.md` (Chinese).

---

## TC-TX Transactions (12)

| ID | Scenario | Expected | Basis |
|---|---|---|---|
| TX-01 | single input, single output, valid signature | accept | §5.2 |
| TX-02 | references a nonexistent output | reject `INPUT_MISSING` | A1 |
| TX-03 | double-spends the same output | second rejected | A1 |
| TX-04 | signature does not match tx hash | reject `SIG_INVALID` | A2 |
| TX-05 | inputs < outputs + fee | reject `VALUE_MISMATCH` | A3 |
| TX-06 | zero-amount output | decided by rule set; rejected by default with a record | A3 |
| TX-07 | shielded amount with valid range proof | accept | A4 |
| TX-08 | shielded amount, tampered range proof | reject `SHIELD_INVALID` | A4 |
| TX-09 | unknown condition type | reject `UNDEFINED_FIELD` | A6 |
| TX-10 | undefined extension flag | reject `UNDEFINED_FLAG` | A6 |
| TX-11 | script cost above bound | reject `SCRIPT_TOO_COSTLY` | A7 |
| TX-12 | condition unsatisfied (time not reached) | output stays locked; tx may be accepted without changing spendability | A5 |

## TC-BH Block header (6)

| ID | Scenario | Expected |
|---|---|---|
| BH-01 | correct parent hash, correct merkle root, PoW satisfies | accept |
| BH-02 | parent hash not on the known chain | reject `PREV_MISMATCH` |
| BH-03 | tx set replaced, merkle root mismatch | reject `MERKLE_MISMATCH` |
| BH-04 | timestamp beyond tolerance | reject `TIMESTAMP` |
| BH-05 | PoW just below target | reject `PROOF_INVALID` |
| BH-06 | one undefined extension bit set | reject `UNDEFINED_FLAG` |

## TC-MT Merkle (4)

| ID | Scenario | Expected |
|---|---|---|
| MT-01 | inclusion proof for a valid transaction | pass |
| MT-02 | inclusion proof for a tampered transaction | fail |
| MT-03 | exclusion proof for an absent transaction | pass |
| MT-04 | root for a single-transaction block | matches definition |

## TC-MP Mempool (6)

| ID | Scenario | Expected |
|---|---|---|
| MP-01 | valid transaction enters pool | admitted |
| MP-02 | invalid signature | rejected, not pooled |
| MP-03 | same output submitted twice | second rejected |
| MP-04 | fee below floor | rejected with an explicit reason |
| MP-05 | pool full, low-fee transaction | evicted by rule; high-fee never silently dropped |
| MP-06 | backlog metric | matches independent recomputation |

## TC-NW Message flow (5)

| ID | Scenario | Expected |
|---|---|---|
| NW-01 | transaction forwarded L1 → L2 | correct target, no broadcast storm |
| NW-02 | malicious peer rebroadcasts repeatedly | deduplicated; bandwidth not linear in repeats |
| NW-03 | node offline then online | state sync recovers; no requests for pruned data |
| NW-04 | batching / delayed relay enabled | propagation delay increase quantifiable and acceptable |
| NW-05 | unknown message type | ignored, no crash, no state change |

## TC-VF Validation flow (5)

| ID | Scenario | Expected |
|---|---|---|
| VF-01 | validation ordering | cheap before expensive (format → signature → script → state) |
| VF-02 | any stage fails | short-circuit, no later computation |
| VF-03 | a "skip validation" switch | does not exist and is not configurable |
| VF-04 | reproducibility | two nodes produce the same reason code for the same tx |
| VF-05 | malicious oversized field | rejected at parse, never reaching deep validation |

## TC-LV Light node (5)

| ID | Scenario | Expected |
|---|---|---|
| LV-01 | headers-only sync | storage and bandwidth tolerable on mobile (quantify) |
| LV-02 | verify inclusion proof of own transaction | pass |
| LV-03 | two contradictory header chains | flag anomaly; never silently pick one |
| LV-04 | peer asserts "confirmed" without proof | assertion not accepted |
| LV-05 | long offline period, then resume | invalid forks identified and rejected |

## TC-CN Consensus node (6)

| ID | Scenario | Expected |
|---|---|---|
| CN-01 | honest node produces a block | accepted |
| CN-02 | one entity holds a dominant share | concentration warning + participation adjustment |
| CN-03 | long-range reorganization attempt | rejected by valid-longest-chain rule |
| CN-04 | selfish mining simulation | revenue not above honest strategy (quantify, Q2) |
| CN-05 | verification-record "farming" strategy | revenue not above sustained honest participation (Q3) |
| CN-06 | special fields for a single entity | no such code path exists |

## TC-DA Difficulty (8)

| ID | Scenario | Expected |
|---|---|---|
| DA-01 | hashrate doubles | difficulty rises, per-step cap respected |
| DA-02 | hashrate falls 70% | difficulty released gradually, no stall |
| DA-03 | persistent mempool backlog | responds within bounds |
| DA-04 | consecutive same-direction moves reach cap | `FROZEN` |
| DA-05 | measurement delay of 2 cycles | no unbounded oscillation (Q6) |
| DA-06 | polluted input (forged hashrate estimate) | clamps hold; damage bounded |
| DA-07 | identical input computed twice | byte-identical output (no local RNG) |
| DA-08 | out-of-range parameter input | `CLAMPED` and logged |

## TC-EC Incentives (6)

| ID | Scenario | Expected |
|---|---|---|
| EC-01 | annual growth computation | does not exceed the cap |
| EC-02 | fee split sum | equals total fees |
| EC-03 | burn record recomputation | third party can reproduce |
| EC-04 | ecosystem share pointing at an individual | rejected at the rule layer |
| EC-05 | volume at historical low | security budget still above target attack cost (Q4, needs simulation) |
| EC-06 | floor-reward parameter change | requires RFC; no silent adjustment |

## TC-DM Dormancy and reflow (5)

| ID | Scenario | Expected |
|---|---|---|
| DM-01 | arbitrarily long dormancy (baseline) | ownership unchanged; no reclamation triggered |
| DM-02 | experimental branch default state | off; no code path exists unless explicitly enabled |
| DM-03 | any one of the seven conditions missing | not executed |
| DM-04 | recovery claim during the notice period | return takes priority |
| DM-05 | conflict with a judicial freeze | immediate freeze |

## TC-PV Privacy (6)

| ID | Scenario | Expected |
|---|---|---|
| PV-01 | consecutive payments to one-time addresses | external observers cannot link them to one holder from addresses alone |
| PV-02 | amounts shielded, validity checked | third party still confirms validity |
| PV-03 | forged commitment | rejected |
| PV-04 | disclosure request from a non-holder | no unilateral disclosure; holder authorisation required |
| PV-05 | disclosure broader than requested | verifiable as out of scope |
| PV-06 | marked privacy-pool transaction re-linked | recorded as a known risk; never counted as "privacy achieved" |

## TC-SC Conditional transactions (8)

| ID | Scenario | Expected |
|---|---|---|
| SC-01 | spend before time lock expires | rejected |
| SC-02 | spend after expiry | accepted |
| SC-03 | 2-of-3 with only one signature | rejected |
| SC-04 | 2-of-3 with two signatures | accepted |
| SC-05 | invalid escrow proof | stays locked |
| SC-06 | escrow timeout | **still locked** (never "anyone may take") |
| SC-07 | designated payment to a non-permitted recipient | transaction invalid |
| SC-08 | condition script hits its resource bound | rejected, not executed |

## TC-UG Upgrade and governance (4)

| ID | Scenario | Expected |
|---|---|---|
| UG-01 | parameter change inside the automatic range | applied automatically with a record |
| UG-02 | parameter outside the automatic range | requires RFC; automatic path refuses |
| UG-03 | backwards-compatible upgrade | old nodes keep running without misjudging new blocks |
| UG-04 | incompatible change | migration window; old nodes can exit safely |

---

## Back-fill format

```
TC-TX-05 | pass | implementer-handle | commit | note
TC-DA-05 | not implemented | — | — | blocked on Q6
```

**Every "pass" must be reproducible by a third party**, otherwise it counts as not passing.
