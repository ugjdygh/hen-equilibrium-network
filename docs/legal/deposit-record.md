# Deposit record

Evidence that the documents existed at a given time, at zero cost. Registration is a separate, paid step that requires giving up anonymity — see `docs/legal/provenance.md` §3.3.

## Bundles produced

| Date (UTC) | Tag | Size | SHA-256 | Commit | Hold |
|---|---|---|---|---|---|
| 2026-11-23T06:02Z | v0.4.1 worktree | 38,903 B | `5365ad17bcbc6bf952ede164306fb7142aec575315858cb8cb3d3ae94d9aa434` | `4f7e8bf` | maintainer (offline) |

The bundle is **not** committed to git: binaries inflate history, and a hash plus an off-line copy is enough. Reproduce at any time:

```bash
python3 tools/make_deposit.py --tag <version>
```

## What this proves, and what it does not

| Proves | Does not prove |
|---|---|
| The listed files existed with exactly these bytes at that time | That the idea was first conceived by this author |
| The bundle has not been altered since (hash comparison) | Any exclusive right in the mechanism |
| Consistency with the commit recorded inside the bundle | Anything against a third party who rewrote the code independently |

## To strengthen it (optional, in increasing cost)

1. **Independent publication of the hash** — post the SHA-256 on an unrelated platform (a gist, a personal site, a public archive). Cross-verifiable, free.
2. **RFC 3161 timestamp** — submit the hash to a timestamping authority and store the receipt under `docs/legal/stamps/`.
3. **Voluntary copyright registration** — with a real name; incompatible with a byline. Author's decision, not a default.

## Next scheduled deposit

At each release tag. The bundle is generated from the released commit, so the tag inside the bundle always matches the release it belongs to.
