# EU_AI_ACT_COMPLIANCE.md — Regulation 2024/1689 positioning

**This document is the publisher's compliance position on AI Brain — EU under the EU AI Act (Regulation 2024/1689).**

It is a transparency document, not a substitute for the user's own AI Act compliance analysis. Users who deploy AI Brain — EU in their practice must conduct their own conformity assessment if they propose to use it in any way that may attract a higher risk classification than the publisher's intended-use positioning.

---

## Publisher's classification position

The publisher classifies AI Brain — EU as a **LIMITED RISK** AI system under **Article 50** of the EU AI Act (transparency obligations for AI systems intended to interact with natural persons).

### Why LIMITED RISK and not HIGH RISK

**Annex III §8** of the AI Act lists as HIGH RISK: "AI systems intended to be used by a judicial authority, or on their behalf, to assist a judicial authority in researching and interpreting facts and the law and in applying the law to a concrete set of facts."

AI Brain — EU is explicitly **NOT** intended for use by judicial authorities. The Software's:

- **Intended user**: qualified lawyers admitted to practice in EU Member States, in their private capacity as practitioners — NOT judges, court staff, tribunal personnel, or any judicial authority acting in an adjudicative capacity
- **Intended use**: research aid · drafting starter · citation parser · calendar utility · compliance flagging — all subject to mandatory human qualified-counsel review before any client-facing output
- **Mode of operation**: human-in-the-loop mandatory; the Software does not produce final legal conclusions, judgments, or decisions
- **Marketing positioning**: explicitly framed as a "productivity tool for lawyers" — not as an adjudicative or autonomous-reasoning system

Because the Software is intended for use by practising lawyers (not judicial authorities) and because every output requires human qualified-counsel review, the Software falls outside Annex III §8.

### Article 50 transparency obligations — how we satisfy them

Article 50 requires that providers of AI systems intended to interact with natural persons ensure that those persons are informed they are interacting with an AI system.

The Software discharges this obligation via:

1. **README disclosure**: the README explicitly identifies the Software as AI-assisted
2. **DISCLAIMER.md**: detailed disclosure of AI-system status, human-in-the-loop requirement, and output liability allocation
3. **CLI banner**: every CLI invocation displays a banner identifying the Software as AI-assisted
4. **Output captioning**: each AI-generated output is captioned (where the architecture supports it) as "AI-generated draft — human review required"
5. **This document** (EU_AI_ACT_COMPLIANCE.md): explicit Article 50 statement

---

## What this means for the user

### If the user is a practising lawyer

The Software is positioned for the user's use as a productivity aid. The user remains responsible for:
- Reviewing every output before client-facing use
- Maintaining client confidentiality (use local-only mode for confidential work)
- Complying with their Member State bar's guidance on AI tool use
- Article 50 transparency to their clients where relevant (informing clients that AI assistance was used)

### If the user is a judicial authority or court staff

The Software is NOT positioned for adjudicative use. If the user wishes to use AI assistance in an adjudicative capacity, they should:
- NOT use AI Brain — EU for that purpose
- Procure an AI system that is conformity-assessed for HIGH RISK use under Annex III §8
- Comply with the user's institution's AI procurement and ethics policies

If the user nonetheless uses AI Brain — EU in an adjudicative context, the Software's use in that context may bring it within Annex III §8 — and that classification triggers obligations (conformity assessment · CE marking · EU-resident representative · risk management · post-market monitoring) that the publisher has not undertaken. **The user assumes all responsibility for such off-positioning use.**

### If the user is a non-lawyer end consumer

The Software is NOT positioned for consumer use. The user should not use the Software to perform legal acts. Consumer use is excluded by the Disclaimer's "Who may use this Software" section.

---

## Annex III risk-zone watch list

The publisher monitors the following Annex III categories for any boundary-shift that might affect classification:

- **Annex III §8** — Judicial authorities (current position: OUT of scope; software positioned for practising lawyers only)
- **Annex III §6** — Law enforcement (current position: OUT of scope; software not intended for law-enforcement use)
- **Annex III §1** — Biometric identification (current position: OUT of scope; software processes no biometric data)
- **Annex III §3** — Education and vocational training (current position: OUT of scope; software is not for educational outcome assessment)

If any module or feature is added in v0.2+ that may touch any Annex III category, this document will be updated, and a separate Annex III analysis will be conducted before that module ships.

---

## General Purpose AI (GPAI) considerations

The Software integrates with third-party GPAI models (Anthropic Claude · OpenAI · Google Gemini · DeepSeek · Mistral · Qwen · etc.) at the user's election. The publisher is NOT a GPAI provider. Each GPAI provider has its own AI Act obligations under Articles 51-55 (general-purpose AI obligations) and, where applicable, Articles 51a-55a (systemic-risk GPAI).

When the user opts into a cloud GPAI provider, the user is bound by that provider's terms and is responsible for verifying that the GPAI provider's Article 50 transparency disclosures cascade through to the user's clients where applicable.

---

## Post-market monitoring (publisher-side)

While the publisher's LIMITED RISK classification does not legally require post-market monitoring, the publisher will:

- Track Annex III boundary developments via EUR-Lex updates
- Monitor EDPB and national supervisory authority guidance affecting GDPR + AI Act intersection
- Update this document and other compliance docs when material changes occur
- Disclose any incidents that would reclassify the Software in CHANGELOG and on the GitHub repo

---

## What the user should retain in their own AI Act file

If the user deploys AI Brain — EU in their practice, the user should retain:
1. A copy of this EU_AI_ACT_COMPLIANCE.md (or a link to it with the AS-OF date)
2. The DISCLAIMER.md and NO_PII_NO_DATA.md
3. Documentation of the user's own AI Act analysis (how the Software fits in their workflow · what review steps are taken · what transparency is provided to clients)
4. Records of any cloud-mode use including DPA + SCCs + Schrems-II supplementary measures

These records support the user's own AI Act + GDPR accountability obligations.

---

## Enforcement timeline (informational)

- **2 August 2024** — AI Act entered into force
- **2 February 2025** — Prohibited AI practices (Articles 5) begin enforcement
- **2 August 2025** — GPAI obligations (Articles 51-55) begin enforcement
- **2 August 2026** — Annex III HIGH RISK obligations begin enforcement (THIS IS THE KEY DATE for any boundary-shift). *Note: the European Commission proposed a "Digital Omnibus" simplification package in late 2025 that could postpone certain HIGH RISK obligations until December 2027. As of plan revision, that postponement is NOT adopted; treat 2 August 2026 as the binding enforcement date.*
- **2 August 2027** — Article 6(1) HIGH RISK (product-safety-integrated AI) obligations begin enforcement

If the Software's positioning ever drifts toward Annex III HIGH RISK, the publisher's commitment is to either (a) bring the Software into HIGH RISK compliance via conformity assessment, OR (b) explicitly remove the offending functionality. The publisher will not knowingly publish an Annex III HIGH RISK AI system without completing the conformity assessment.

---

## Document version

- v0.1 — 2026-05-18 — initial publisher position; LIMITED RISK classification under Article 50

---

*This document references LEGAL_EXPOSURE_PLAYBOOK §3.V2 (EU AI Act). Playbook v0.1.*
