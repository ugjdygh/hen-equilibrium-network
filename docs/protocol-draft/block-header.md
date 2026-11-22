# Block Header — draft field table

**Status: non-normative draft.** This file does not define a wire format, does not specify encoding, and does not describe an implementation. It exists so that reviewers can argue about fields instead of prose.

See whitepaper §5.1.

| Field | Type | Purpose | Notes |
|---|---|---|---|
| `version` | uint32 | Protocol version and feature bits | Undefined bits MUST be treated as invalid |
| `prev_block_hash` | 32 bytes | Links to parent block | Genesis has all-zero value |
| `merkle_root` | 32 bytes | Root of transaction set | Inclusion proofs must be verifiable by light nodes |
| `timestamp` | int64 | Block time | Must define tolerance window and median-time rule |
| `difficulty_target` | uint256 | Proof threshold | Derived from §6.2 multi-metric adjustment, bounded |
| `nonce` / `proof` | bytes | Work proof | Format TBD by Q2/Q8 evaluation |
| `extension_flags` | bitfield | Backwards-compatible upgrade markers | Each bit must be defined in a spec before use |
| `checksum` | 32 bytes | Ledger integrity check | Redundant by design; used to detect truncation/corruption |

## Open items in this file

1. Encoding is unspecified. Fixed-width little-endian vs canonical serialization must be decided before any implementation.
2. `timestamp` tolerance is not fixed. Too tight → honest nodes rejected; too loose → difficulty manipulation. This interacts with Q6.
3. `extension_flags` bit allocation needs a registry with an expiry rule, otherwise it becomes a permanent bypass surface.
4. `checksum` duplicates existing hashes; justify it or remove it. Current rationale is defense against truncation in storage/transport, not consensus.

## Rules that hold regardless of encoding

- Every field must be independently recomputable by any node from the ledger alone.
- No field may grant special validation status to a specific entity (whitepaper §6.1).
- Adding a field requires a backwards-compatible path; removing one requires a deprecation window.
