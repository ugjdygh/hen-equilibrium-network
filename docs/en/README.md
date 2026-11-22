# English Edition / 英文版

<!-- lang-switch -->
<sub>Full text: **English** · [简体中文](../whitepaper/zh/whitepaper.md) · [繁體中文](../whitepaper/zh-Hant/whitepaper.md)　｜　Entry summaries (not full text): [Русский](../i18n/ru.md) · [Français](../i18n/fr.md) · [Español](../i18n/es.md) · [한국어](../i18n/ko.md) · [Bahasa Indonesia](../i18n/id.md) · [Deutsch](../i18n/de.md) · [Português](../i18n/pt.md) · [العربية](../i18n/ar.md)</sub>

**Status: `Draft` (machine-assisted translation, pending human proofread).** The Chinese text remains the source for `docs/handover/` and `docs/review/`; if the two disagree, the Chinese governs.

## 1. Why this folder exists

The repository's working documents were written in Chinese while the entry points (`README.md`, `DISCLAIMER.md`, whitepaper) declare English as the primary content language. This folder closes that gap for the two document sets that outsiders actually need in order to review or take over the work.

## 2. Coverage

| Source (Chinese) | English | Status |
|---|---|---|
| `docs/handover/onboarding.md` | [`handover/onboarding.md`](handover/onboarding.md) | Translated |
| `docs/handover/module-map.md` | [`handover/module-map.md`](handover/module-map.md) | Translated |
| `docs/handover/api-sketch.md` | [`handover/api-sketch.md`](handover/api-sketch.md) | Translated |
| `docs/handover/test-cases.md` | [`handover/test-cases.md`](handover/test-cases.md) | Translated (all 86 case IDs) |
| `docs/review/process.md` | [`review/process.md`](review/process.md) | Translated |
| `docs/review/checklist.md` | [`review/checklist.md`](review/checklist.md) | Translated |
| `docs/review/decisions.md` | [`review/decisions.md`](review/decisions.md) | Translated |
| `docs/handover/project-guide.md` | — | **Not translated** (Chinese-only working draft; see note) |
| `docs/maintenance/*`, `docs/legal/disclaimer.md`, `docs/research/*` | — | Chinese-only at present |

## 3. Notes

- `docs/handover/project-guide.md` is an internal working draft describing why the repository is organized as it is. It is not normative, is kept in Chinese to preserve the original wording, and is not needed to use the repo.
- `docs/research/` pages remain Chinese; `CITATION.cff`, `LICENSE`, `README.md` and the whitepaper are already bilingual.
- Terminology follows [`docs/research/glossary.md`](../research/glossary.md). Fixed renderings: 遮蔽 → shielding; 记账单位 → unit of account; 沉睡资产 → dormant asset; 本金不可侵犯 → no-seizure default; 熔断 → circuit breaker; 验证履历权重 → verification-record weight; 兜底规则 → fallback rule.
- Do not use these translations to restate a rule more loosely than the Chinese. If a rule looks weaker in English, fix the English.
