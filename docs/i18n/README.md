# Languages / 语言

<!-- lang-switch -->
<sub>Full text: [English](../../README.md) · [简体中文](zh.md)　｜　Entry summaries (not full text): **语言总览** · [繁體中文](zh-Hant.md) · [Русский](ru.md) · [Français](fr.md) · [Español](es.md) · [한국어](ko.md) · [Bahasa Indonesia](id.md) · [Deutsch](de.md) · [Português](pt.md) · [العربية](ar.md)</sub>

Each page below carries the same switcher bar at the top, so any reader can move between locales without going back to the root. GitHub has no repository-level language setting; switching is done by these links.

**Primary content language: English (en).**

Everything normative lives in English: `README.md`, `docs/whitepaper/en/whitepaper.md`, `DISCLAIMER.md`, `GOVERNANCE.md`, `docs/handover/`, `docs/review/`, `spec/`. Localized pages are entry summaries so that readers in other languages can understand what this repository is, what it is **not**, and where the authoritative text lives.

## 1. Real coverage: two tiers

Coverage is declared by what a reader can actually read end to end, not by how many pages exist. **Full text exists in two locales only.** Everything else is a summary and is labelled as such everywhere it appears.

### Tier A — full text (2)

| Locale | Language | Page | Status |
|---|---|---|---|
| `en` | English | [`README.md`](../../README.md), [`DISCLAIMER.md`](../../DISCLAIMER.md), [`whitepaper/en`](../whitepaper/en/whitepaper.md), [`docs/en/`](../en/README.md) | Published (authoritative on conflict) |
| `zh` | 中文（简体） | [`whitepaper/zh`](../whitepaper/zh/whitepaper.md) + [`zh.md`](zh.md) | Published (authoritative for Chinese technical detail) |

These two appear in the "Full text" half of the switcher bar.

### Tier B — entry summaries (9)

| Locale | Language | Page | Status |
|---|---|---|---|
| `zh-Hant` | 中文（繁體） | [`zh-Hant.md`](zh-Hant.md) | Draft |
| `ru` | Русский | [`ru.md`](ru.md) | Draft |
| `fr` | Français | [`fr.md`](fr.md) | Draft |
| `es` | Español | [`es.md`](es.md) | Draft |
| `ar` | العربية | [`ar.md`](ar.md) | Draft |
| `ko` | 한국어 | [`ko.md`](ko.md) | Draft |
| `id` | Bahasa Indonesia | [`id.md`](id.md) | Draft |
| `de` | Deutsch | [`de.md`](de.md) | Draft |
| `pt` | Português | [`pt.md`](pt.md) | Draft |

"Entry summary" means: positioning, explicit non-goals, status, authorship, license, and links. It is **not** a full translation of the whitepaper, and it must never be presented as one.

### Promotion rule

A locale moves from Tier B to Tier A only when a complete whitepaper translation exists at `docs/whitepaper/<locale>/whitepaper.md`, the switcher bar is updated in the same commit, and the matrix above is updated in the same commit. Until then it stays in the right-hand half of the bar, marked "not full text". Adding a page to Tier B does not promote it.

## 2. Rules for localized pages

1. Never weaken these four statements when translating: **no issuance, no fundraising, no operation, no endorsement** (see `DISCLAIMER.md`).
2. Keep the warning that the English version prevails on conflict.
3. Keep the author alias as written (`Lee Hyun seok（이 현석）`); do not localize or transliterate it into a different name.
4. Status must be stated (`Draft` / `Published`) — a machine-translated page must not look finished.
6. The author name is a pen name: never localise it into a different name (see `AUTHORS.md`).
5. Do not translate code spans, file paths, or command names.

## 3. Adding or completing a translation

- Full whitepaper translations go to `docs/whitepaper/<locale>/whitepaper.md` and must be marked with the translator, the source version, and a "may lag behind the English edition" note.
- Entry summaries go to `docs/i18n/<locale>.md`.
- Update the table above in the same PR, otherwise the matrix lies.
- A translation PR is reviewed for **fidelity to the limits**, not for prose style.

## 4. Why this is not a repository setting

GitHub has no repository-level "content language" switch. The languages shown in a repository sidebar are auto-detected by GitHub Linguist from file types and sizes, so they reflect code, not documentation language. Language coverage here is therefore declared in this file and linked from `README.md` instead of being configured in repository settings.

## 5. Known gaps

- `docs/maintenance/`, `docs/legal/`, `docs/research/` and `spec/` are Chinese-only; only `docs/handover/` and `docs/review/` have English editions (see `docs/en/README.md`).
- `docs/handover/project-guide.md` is deliberately untranslated (internal working draft).
- `zh-Hant` is written in Traditional characters but has not been proofread by a native editor.
- Arabic page is not RTL-formatted beyond default bidirectional text rendering.

If any of these matter to you, a pull request is the fastest fix.
