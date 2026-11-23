# Finalization record — whitepaper v1.0

Text frozen: **2026-11-23**. From this version on, the whitepaper changes only through numbered errata (see §6), never by silent edits.

This file chains four independent pieces of evidence. Any one of them alone is weak; together they answer "what exactly was published, and when".

| # | Layer | Where | What it fixes |
|---|---|---|---|
| 1 | Git commit + tag | this repository, tag `v1.0` | exact bytes, public history |
| 2 | SHA-256 manifest | `docs/legal/finalization-manifest.sha256` | the four artefacts, byte-exact |
| 3 | RFC 3161 trusted timestamp | `docs/legal/stamps/*.tsr` | existence at a wall-clock time, from a third party |
| 4 | Persistent identifier | Zenodo DOI (pending, §5) | citation, independent of GitHub |

## 1. Frozen artefacts

| Artefact | Bytes | SHA-256 |
|---|---|---|
| `docs/whitepaper/en/whitepaper.md` | 28,132 | `188f32e5e57dc42e3927874de859f8901f9f400c157a5049a5d3e23989895397` |
| `docs/whitepaper/zh/whitepaper.md` | 36,112 | `602107892f2f53e9acffb8c7e27819abd0fbe48cc7aff947b4be05a69b138d18` |
| `HEN-whitepaper-en-v1.0.pdf` | 82,765 | `92523fe3a19ccc3dfa1da2656bf1e9df7a6b4ed57cdb9478dffa372ddee713b1` |
| `HEN-whitepaper-zh-v1.0.pdf` | 332,487 | `11485bf78b98d096953eb15ec66f3af2d5f8cb30dc9f93ae4f4616381f96e907` |

The PDFs are release assets, not repository files: binaries in history make clones slow and diffs unreadable.

## 2. Trusted timestamps (RFC 3161)

Responder: DigiCert public TSA, policy `2.16.840.1.114412.7.1`. No cost, no account, no personal data beyond the request itself.

| Receipt | Stamped (UTC) | Serial |
|---|---|---|
| `stamps/whitepaper-en-v1.0-md.tsr` | 2026-11-23 06:11:37 | `0xCCF44C0045D72DB1F0BF33021B4173BC` |
| `stamps/whitepaper-zh-v1.0-md.tsr` | 2026-11-23 06:11:37 | `0xDBB40A61B81789E39CB871DD5CB34B2C` |
| `stamps/whitepaper-en-v1.0-pdf.tsr` | 2026-11-23 06:11:38 | `0x8FE3730BF3B946E0CBE68812217EE81C` |
| `stamps/whitepaper-zh-v1.0-pdf.tsr` | 2026-11-23 06:11:39 | `0xEB6878A69FAD265FAF0E32AD17C0CE90` |
| `stamps/finalization-manifest.tsr` | 2026-11-23 06:11:46 | `0x7FCA4D99F19B80E08D9527606BA1ECAF` |

Each `.tsq` is kept next to its `.tsr` so the request can be re-submitted to any RFC 3161 responder later without reconstructing it.

Verify locally:

```bash
sha256sum docs/whitepaper/en/whitepaper.md        # must equal §1
openssl ts -reply -in docs/legal/stamps/whitepaper-en-v1.0-md.tsr -text   # imprint + Granted
```

Re-timestamp any file with `python3 tools/stamp.py <file> --label <name>`.

## 3. What this proves

- **Proves**: these exact bytes existed at that time, as certified by a third party that has no relationship with this project; and they have not been altered since (hash mismatch would show).
- **Does not prove**: authorship of the ideas, priority over an earlier unpublished draft, or ownership of the mechanism. A timestamp is evidence about a document, not about a person.

## 4. Escalation for "important" versions only

Not done, and not recommended for every tag — cost and identity exposure without proportionate benefit:

| Step | Cost | Requires | Verdict |
|---|---|---|---|
| Hash posted on an independent platform | free | nothing | **do it** for each major version |
| RFC 3161 timestamp | free | nothing | **done** for v1.0 |
| Notarization of a printed copy | USD 50–300 | physical attendance, real ID | only if a dispute is foreseeable |
| Voluntary copyright registration | USD 45–800 by office | **real name** | conflicts with the pen name; author's call |

Registration and notarization both dissolve the byline. That is a trade-off to make consciously, not a step to automate.

## 5. Zenodo — prepared, not yet deposited

`.zenodo.json` in the repository root carries the metadata (title, description that repeats the "no tradable asset" framing, licence MIT, keywords, creator as the research pen name with an explicit note that no ORCID is given because an ORCID identifies a natural person).

To mint the DOI, either:

1. **GitHub integration** (recommended, no manual upload): Zenodo → Settings → GitHub → switch the repository on; the next release tag produces a DOI automatically. Requires a Zenodo account logged in with GitHub.
2. **Manual upload**: new deposit → upload the two PDFs plus `docs/whitepaper/en/whitepaper.md` → metadata is read from `.zenodo.json`.

Either way the DOI is recorded here and in `CITATION.cff` afterwards. **Until a DOI is recorded in this section, no DOI exists** — do not cite one.

## 6. Errata policy

1. An error is reported as an issue with the label `erratum`.
2. The fix lands as a separate commit titled `errata: <n> — <what>`; the whitepaper keeps a numbered erratum entry under its disclaimer section, with the date and the v1.0 hash it corrects.
3. A new version number is issued only when the substantive text changes; formatting-only commits do not bump it.
4. Old PDFs stay published. Superseded artefacts are never deleted, because deletion is what makes a version history deniable.
