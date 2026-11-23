# CLA ledger

## Where the record lives

The authoritative record is [`CLA-SIGNATURES.md`](../../CLA-SIGNATURES.md) at the repository root, appended automatically by `.github/workflows/cla-sign.yml` when someone signs in the sign-off issue. One signature is valid repository-wide. Signing inside a PR remains valid as a **secondary** record.

## Why not a central roster

- A roster needs manual syncing, always lags, and gives a false impression that "this person has signed";
- under a byline, a roster only hard-codes "some GitHub account signed", amplifying the unverifiable-party problem in `CLA.md` §9;
- a PR thread is public history that cannot be quietly edited, which is more reliable than a hand-maintained table.

## Export (maintainer rights required)

```bash
# signed PRs and their authors
gh pr list --repo ugjdygh/hen-equilibrium-network --label "cla: signed" \
  --state all --limit 500 --json number,author,createdAt,mergedAt

# pending
gh pr list --repo ugjdygh/hen-equilibrium-network --label "cla: pending" \
  --state all --limit 500 --json number,author,createdAt
```

If a formal roster is needed (prototype stage, or proving the licence chain to a partner), generate a timestamped file from the above and store it under `docs/legal/stamps/`, using the method in `docs/legal/provenance.md` §3.2.

## Verified during setup

| Round | Scenario | Result |
|---|---|---|
| 1 | PR opened, no signature | `cla: pending` automatically, one prompt listing who is missing |
| 1 | Signature posted in the PR | switched to `cla: signed` |
| 2 | Full sentence posted in sign-off issue #4 | ledger row appended (time, first 16 hex of `CLA.md` hash, comment link) with a confirming reply |
| 2 | New PR with **no comment at all** | recognised as `cla: signed` from the ledger |

The first ledger row, `@ugjdygh`, is the maintainer's own signature left in place during verification. The ledger is append-only by design, so the test row stays under the same rule.

## Offline rule simulation (8 cases, all passing)

`tools/cla_sim.py` reduces the workflow's decision rules to reproducible cases; run `python3 tools/cla_sim.py`:

| Case | Result |
|---|---|
| Single-author PR, unsigned | `pending` (author missing) |
| Single-author PR, signed | `signed` |
| Multi-author PR, author signed, other committer not | `pending` (committer missing) |
| Multi-author PR, both signed | `signed` |
| Bot posts the sentence | ignored, still `pending` |
| Bystander (neither author nor committer) signs | not counted, still `pending` |
| Sentence incomplete (missing "to its terms") | not counted, still `pending` |
| Signature edited away afterwards | re-evaluated as `pending` |

**Note**: this is rule-level verification, not an end-to-end test with a second real account. A true third-party test needs an account other than the author to open a PR and comment; this repository has one account, so that test has not been run.

## Known limits

| Limit | Effect |
|---|---|
| Only checks whether the PR author or committer posted the sentence | identity unverified; cannot prove who signed |
| Does not cover email patches or code sent privately | such contributions have no PR record; maintainers must request a signature separately |
| Bot PRs are skipped automatically | the actual rights holder needs separate confirmation |
| Signing creates no employment, partnership or payment relationship | see `CLA.md` §9.4 |
