# Languages / 语言

**Primary content language: English (en).**

Everything normative lives in English: `README.md`, `docs/whitepaper/en/whitepaper.md`, `DISCLAIMER.md`, `GOVERNANCE.md`, `docs/handover/`, `docs/review/`, `spec/`. Localized pages are entry summaries so that readers in other languages can understand what this repository is, what it is **not**, and where the authoritative text lives.

## 1. Current coverage

| Locale | Language | Page | Coverage | Status |
|---|---|---|---|---|
| `en` | English | `README.md`, `DISCLAIMER.md` | Full (authoritative) | Published |
| `zh` | 中文（简体） | [`zh.md`](zh.md) + [`docs/whitepaper/zh/whitepaper.md`](../whitepaper/zh/whitepaper.md) | Whitepaper full text + entry summary | Published |
| `zh-Hant` | 中文（繁體） | [`zh-Hant.md`](zh-Hant.md) | Entry summary | Draft |
| `ru` | Русский | [`ru.md`](ru.md) | Entry summary | Draft |
| `fr` | Français | [`fr.md`](fr.md) | Entry summary | Draft |
| `es` | Español | [`es.md`](es.md) | Entry summary | Draft |
| `ar` | العربية | [`ar.md`](ar.md) | Entry summary | Draft |
| `ko` | 한국어 | [`ko.md`](ko.md) | Entry summary | Draft |
| `id` | Bahasa Indonesia | [`id.md`](id.md) | Entry summary | Draft |
| `de` | Deutsch | [`de.md`](de.md) | Entry summary | Draft |
| `pt` | Português | [`pt.md`](pt.md) | Entry summary | Draft |

"Entry summary" means: positioning, explicit non-goals, status, authorship, license, and links. It is **not** a full translation of the whitepaper.

## 2. Rules for localized pages

1. Never weaken these four statements when translating: **no issuance, no fundraising, no operation, no endorsement** (see `DISCLAIMER.md`).
2. Keep the warning that the English version prevails on conflict.
3. Keep the author alias as written (`Lee Hyun seok（이 현석）`); do not localize or transliterate it into a different name.
4. Status must be stated (`Draft` / `Published`) — a machine-translated page must not look finished.
5. Do not translate code spans, file paths, or command names.

## 3. Adding or completing a translation

- Full whitepaper translations go to `docs/whitepaper/<locale>/whitepaper.md` and must be marked with the translator, the source version, and a "may lag behind the English edition" note.
- Entry summaries go to `docs/i18n/<locale>.md`.
- Update the table above in the same PR, otherwise the matrix lies.
- A translation PR is reviewed for **fidelity to the limits**, not for prose style.

## 4. Why this is not a repository setting

GitHub has no repository-level "content language" switch. The languages shown in a repository sidebar are auto-detected by GitHub Linguist from file types and sizes, so they reflect code, not documentation language. Language coverage here is therefore declared in this file and linked from `README.md` instead of being configured in repository settings.

## 5. Known gaps

- No full translations of `docs/handover/`, `docs/review/`, or `spec/` exist in any language.
- `zh-Hant` is written in Traditional characters but has not been proofread by a native editor.
- Arabic page is not RTL-formatted beyond default bidirectional text rendering.

If any of these matter to you, a pull request is the fastest fix.
