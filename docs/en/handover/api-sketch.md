# API Sketch

**Nature:** inputs, outputs and assertions only. No language, no implementation, nothing compilable.

**Purpose:** let independent implementers agree on *what validation must do* before arguing about languages.

Source of truth: `docs/handover/api-sketch.md` (Chinese).

---

## 1. Conventions

- Every function is described functionally: identical input must yield identical output.
- Every failure returns a **structured reason**. Boolean-only returns are not allowed — they make failures undiagnosable and untestable.
- Every function declares its **trust boundary**: what the caller has already checked, and what the function checks itself.
- Undefined fields are invalid, never ignored.

## 2. Transaction validation

```text
validate_tx(tx, utxo_set, rules)
  -> (valid: bool, errors: list<Reason>, metadata: Metadata)

Inputs:
  tx        transaction (inputs, outputs, fee, signatures, conditions, shielding)
  utxo_set  spendable outputs (or account snapshot, depending on Q9)
  rules     rule set (max script cost, minimum fee, field legality table)

Assertions:
  A1 an input references a missing or already-spent output -> valid=false, INPUT_MISSING
  A2 signature does not cover the actual tx hash            -> valid=false, SIG_INVALID
  A3 inputs < outputs + fee                                 -> valid=false, VALUE_MISMATCH
     (with shielding, replaced by "range proof holds", see A4)
  A4 commitment / range proof invalid                       -> valid=false, SHIELD_INVALID
  A5 condition unsatisfied                                  -> output stays locked
     (not a whole-tx failure, and not a downgrade to spendable)
  A6 undefined condition type or flag                        -> valid=false, UNDEFINED_FIELD
  A7 script cost exceeds static bound                        -> valid=false, SCRIPT_TOO_COSTLY

Trust boundary:
  Does not check PoW, does not check block context, does not know chain position.
```

## 3. Block validation

```text
validate_block(block, prev_block, difficulty_target, chain_ctx)
  -> (valid: bool, reason: Reason, stats: Stats)

Assertions:
  B1 prev_block_hash matches a known parent      -> else PREV_MISMATCH
  B2 merkle_root recomputable from tx set        -> else MERKLE_MISMATCH
  B3 version bits and extension flags all defined -> else UNDEFINED_FLAG
  B4 timestamp inside tolerance + median-time rule -> else TIMESTAMP
  B5 work proof meets difficulty_target          -> else PROOF_INVALID
  B6 every transaction passes validate_tx        -> else TX_INVALID(<id>)

Trust boundary:
  Does not decide whether this chain is "the valid longest"; chain selection is the caller's job.
```

## 4. Difficulty computation

```text
compute_difficulty(history, node_metrics, bounds) -> target: Target

Inputs:
  history       last N intervals, difficulties, hashrate estimates
  node_metrics  active consensus nodes, dispersion, mempool backlog
  bounds        static min/max, per-step cap, consecutive-move cap

Assertions:
  D1 output always inside bounds       -> else clamp and emit CLAMPED
  D2 per-step change <= bounds.max_step
  D3 consecutive same-direction moves at cap -> emit freeze flag, stop adjusting
  D4 identical input yields identical output (no local RNG, no local clock)

Trust boundary:
  history and node_metrics may be partially attacker-influenced;
  the function must assume pollution, which is why D1/D2 are hard clamps.
```

## 5. Incentives and fees

```text
compute_reward(block_stats, params)
  -> (issuance: Amount, fee_split: {incentive, burn, ecosystem}, notes)

Assertions:
  E1 issuance <= params.annual_growth_cap (annualized)
  E2 burn records independently recomputable from transaction data
  E3 ecosystem share never addresses an individual account
  E4 three shares sum exactly to total fees (nothing created, nothing lost)
```

## 6. Reason enum (proposed)

```text
Reason =
  | INPUT_MISSING | SIG_INVALID | VALUE_MISMATCH | SHIELD_INVALID
  | UNDEFINED_FIELD | UNDEFINED_FLAG | SCRIPT_TOO_COSTLY
  | PREV_MISMATCH | MERKLE_MISMATCH | TIMESTAMP | PROOF_INVALID
  | TX_INVALID(<id>) | CLAMPED | FROZEN
```

Adding a reason requires an RFC, because downstream implementations surface it to users.

## 7. Explicit non-goals

- No wire format (see `docs/protocol-draft/message-flow.md`).
- No persistence layout.
- No wallet or UI interface.
- **No administrative override parameter.** No interface can bypass A1–A7 or B1–B6.
