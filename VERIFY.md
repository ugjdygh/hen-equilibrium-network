# Verify this document

Three things can be checked independently, by anyone, without trusting this repository.

## 1. Where the records live

| What | Where on GitHub |
|---|---|
| Frozen hashes (4 artefacts, byte-exact) | [`docs/legal/finalization-manifest.sha256`](docs/legal/finalization-manifest.sha256) |
| Trusted timestamp receipts (RFC 3161) | [`docs/legal/stamps/`](docs/legal/stamps/) — 5 `.tsr` files, each with its `.tsq` request |
| Human-readable evidence chain | [`docs/legal/finalization.md`](docs/legal/finalization.md) |
| Published PDFs | [release `v1.0`](https://github.com/ugjdygh/hen-equilibrium-network/releases/tag/v1.0) |
| Git state at freeze | tag `v1.0`, commit `7fd5393` |
| Everything else, hashed | [`docs/legal/provenance.sha256`](docs/legal/provenance.sha256) |

Direct raw links (no page rendering needed):

```
https://raw.githubusercontent.com/ugjdygh/hen-equilibrium-network/main/docs/legal/finalization-manifest.sha256
https://raw.githubusercontent.com/ugjdygh/hen-equilibrium-network/main/docs/whitepaper/en/whitepaper.md
https://raw.githubusercontent.com/ugjdygh/hen-equilibrium-network/main/docs/legal/stamps/whitepaper-en-v1.0-md.tsr
```

## 2. How to check the hash

```bash
curl -sL https://raw.githubusercontent.com/ugjdygh/hen-equilibrium-network/main/docs/whitepaper/en/whitepaper.md | sha256sum
# expected: 188f32e5e57dc42e3927874de859f8901f9f400c157a5049a5d3e23989895397
```

## 3. How to check the timestamp

```bash
curl -sLO https://raw.githubusercontent.com/ugjdygh/hen-equilibrium-network/main/docs/legal/stamps/whitepaper-en-v1.0-md.tsr
openssl ts -reply -in whitepaper-en-v1.0-md.tsr -text
```

Read three lines in the output:

- `Status: Granted` — the authority actually issued it;
- `Message data` — must start `18 8f 32 e5 …`, i.e. the same bytes as the file's SHA-256;
- `Time stamp: Nov 23 06:11:37 2026 GMT` — the certified wall-clock time.

The responder is DigiCert's public RFC 3161 service, policy `2.16.840.1.114412.7.1`. It has no relationship with this project beyond issuing the receipt.

## 4. What the evidence does and does not say

- **Says**: these exact bytes existed at that time, certified by a third party; they have not changed since.
- **Does not say**: who wrote them, or that the ideas were first. A timestamp is evidence about a document, not about a person.

## 5. Zenodo DOI — where it will appear

Not minted yet. When it exists it will be recorded in `docs/legal/finalization.md` §5 and in `CITATION.cff`. **Until then, no DOI exists; do not cite one.**

To mint it, either switch on the GitHub integration in Zenodo (Settings → GitHub → this repository; the next release produces a DOI automatically), or upload the pre-built bundle `HEN-v1.0-zenodo-bundle.zip` attached to release `v1.0` — it already contains both PDFs, both markdown sources and `.zenodo.json` with the metadata. Neither path needs anything typed by hand beyond logging in.
