# Transaction — draft field table

**Status: non-normative draft.** No wire format, no encoding, no implementation. See whitepaper §5.2 and §9.

## Core fields

| Field | Type | Purpose | Notes |
|---|---|---|---|
| `inputs` | list | References to spendable outputs | Each carries unlocking evidence |
| `outputs` | list | Recipient, amount, lock/condition | Amount may be shielded (§8) |
| `fee` | integer | Resource pricing and incentive | Must be verifiable even when amounts are shielded |
| `signature(s)` | bytes | Proof of control | Scheme choice pending review (BIP-340 class vs others) |
| `condition` | optional | Time lock, multisig threshold, hash/ proof condition | Default-deny semantics |
| `shielding` | optional | Commitment, range proof, nullifier set ref | Must not break third-party verification of validity |

## Condition semantics (default-deny)

| Condition | Satisfied when | Failure behavior |
|---|---|---|
| `time_lock` | Current median time ≥ lock value | Output remains locked, not downgraded |
| `multisig(m-of-n)` | ≥ m distinct valid signatures | Rejected |
| `escrow(proof)` | Supplied proof matches commitment | Rejected |
| `designated(recipient_set)` | Output key in allowed set | Invalid transaction |

Rule: **no condition may degrade to "anyone can spend"** on timeout, error, or missing data. Failures must be inert, not permissive.

## Structural questions still open

1. **Fee visibility under shielding.** If amounts are hidden, how is fee validated without leaking the amount? Candidate: separate fee output with cleartext value, or a proof that fee ≥ minimum. Unresolved.
2. **Nullifier set growth.** Unbounded nullifier storage is a scaling problem; pruning breaks double-spend detection. Unresolved.
3. **Replay across forks.** Transactions must be bound to a chain identifier, otherwise fork coexistence creates double-spend ambiguity (Q7).
4. **Script resource bounds.** Every condition must be statically bounded in size and verification cost; no unbounded loops, no general VM (§9).
5. **UTXO vs account.** All of the above assumes UTXO; an account model changes fee and nullifier handling entirely (Q9).

## Non-negotiables

- No field may reference off-chain state as a validity condition (that imports an external trust anchor into consensus).
- No field may encode an identity claim. Identity data stays out of the ledger (§8.2).
- No field may be added that enables issuance, sale, or redemption of anything (§12).
