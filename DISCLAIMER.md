# DISCLAIMER — AI Brain for EU Lawyers

**Read this in full before installation or use.**

---

## What this Software IS and IS NOT

AI Brain — EU · Solo is **open-source developer software** published by wolfgang_rush under the MIT License. The Software is a **productivity utility for qualified legal professionals**.

The Software is **NOT**:
- A legal service
- A law firm
- A legal-advice channel
- A substitute for the judgement of a qualified lawyer admitted to practice in any EU Member State
- An autonomous legal-reasoning system
- An AI system intended for use by judicial authorities in adjudicating cases (see EU AI Act positioning below)
- A service operated by the publisher
- A lawyer-client communication channel

Every output produced by the Software must be reviewed by a lawyer admitted to practice in the relevant EU Member State before any client-facing use.

The publisher does NOT provide legal services to any user of the Software. Installation, use, or distribution of the Software does NOT create any lawyer-client relationship. No professional privilege attaches to interactions with the Software or its publisher.

---

## Who may use this Software

The Software is intended exclusively for:

- **Lawyers** admitted to practice in any EU Member State under the relevant national bar regulation (Avocat · Advocaat · Rechtsanwalt · Abogado · Avvocato · Advokat · Adwokat · Δικηγόρος · Advokát · etc.)
- **Lawyers** registered for cross-border practice under Directive 98/5/EC (Establishment Directive)
- **In-house counsel** employed by EU entities and working on EU-law matters
- **Trainee lawyers / stagiaires** working under the supervision of a fully admitted lawyer
- **Paralegals** working under the direct supervision of an admitted lawyer

**If you are not a qualified legal professional, do not use this Software to produce client-facing legal work.**

---

## Publisher's jurisdiction

The publisher (wolfgang_rush — **Rushikesh R. Mahajan**) is an Indian advocate enrolled with the Bar Council of Maharashtra & Goa under the Indian Advocates Act 1961, currently practising at the High Courts of India, India.

The publisher is NOT admitted to practice law in any EU Member State. The publisher does NOT offer legal services in any EU Member State. The publisher offers this tool as **open-source software**, published from India under the MIT License, for use by EU-admitted lawyers in their own practice.

---

## 🇪🇺 EU AI Act (Regulation 2024/1689) — LIMITED RISK classification

**The Software is classified by the publisher as a LIMITED RISK AI system under Article 50 of the EU AI Act.** The user is informed (via this Disclaimer, the README, and the CLI banner) that they interact with an AI-assisted system. This satisfies the Article 50 transparency obligation.

**The Software is NOT classified as a HIGH RISK AI system under Annex III §8.** Annex III §8 covers AI systems "intended to be used by a judicial authority, or on their behalf, to assist a judicial authority in researching and interpreting facts and the law and in applying the law to a concrete set of facts."

The Software is **explicitly NOT** intended for use by judicial authorities in adjudicating cases. Its design, marketing, and intended-use positioning are:
- **For qualified lawyers practicing privately** — not for judges, court staff, or any tribunal personnel acting in an adjudicative capacity
- **Productivity-aid only** — every output requires human qualified-counsel review; the Software does not produce final legal conclusions or decisions
- **Human-in-the-loop mandatory** — the Software's outputs are explicitly framed as drafts, suggestions, and research aids requiring human review

If the user is a judicial authority or court staff member acting in an adjudicative capacity, the user must NOT use this Software for that adjudicative work. The Software's use in such a context may bring it within Annex III §8 high-risk classification, which would impose conformity-assessment, CE-marking, EU-resident-representative, and post-market-monitoring obligations that the publisher has not undertaken.

See [EU_AI_ACT_COMPLIANCE.md](EU_AI_ACT_COMPLIANCE.md) for the full compliance documentation.

---

## Bar conduct rules (your obligations)

EU lawyer professional conduct is regulated per-Member-State (with some harmonization via the CCBE Code of Conduct for European Lawyers). Common obligations affecting Software use include:

- **Client confidentiality / professional secrecy** — the Software's local-only default mode supports this; cloud-mode use requires careful confidentiality analysis
- **Conflict-of-interest checks** — the Software does NOT perform these; you must
- **Technological competence** — multiple bars have issued guidance on AI tool use; consult your jurisdiction's current position
- **Advertising and solicitation restrictions** — vary by Member State

The user must verify compliance with their Member-State bar before any client-facing use of Software outputs.

---

## GDPR + ePrivacy compliance

The publisher is **neither a Controller nor a Processor** under GDPR (Regulation 2016/679) with respect to the user's tool usage. The publisher operates no server processing user input. See [NO_PII_NO_DATA.md](NO_PII_NO_DATA.md) for the complete zero-collection architecture documentation.

If the user uses the Software to process personal data of EU data subjects, the **user** is the Controller for that processing. The user's GDPR obligations apply:
- Article 5 — Lawfulness, fairness, transparency · purpose limitation · data minimisation · accuracy · storage limitation · integrity & confidentiality · accountability
- Article 6 — Lawful basis (and Article 9 for special categories)
- Articles 12-22 — Data subject rights (information · access · rectification · erasure · restriction · portability · objection · automated decision-making)
- Article 28 — Processor contracts (with cloud AI vendors if used)
- Article 32 — Security of processing
- Articles 33-34 — Breach notification (72 hours to supervisory authority; without undue delay to data subjects)
- Article 35 — DPIA for high-risk processing
- Article 37 — DPO appointment where required
- Chapter V (Articles 44-50) — International transfers (adequacy · SCCs · BCRs · derogations)

For client-confidential work, use the **local-only mode** (Ollama + Qwen3 or equivalent). See [MODEL_SETUP.md](MODEL_SETUP.md).

---

## Cloud-mode and third-party AI tools — user assumes all risk

If the user chooses to integrate the Software with any third-party AI service or CLI tool — including but not limited to: **Anthropic Claude API**, **Claude CLI**, **Claude Code**, **OpenAI API**, **Codex CLI**, **Google Gemini API**, **Gemini CLI**, **DeepSeek API**, **OpenCode**, **Cursor**, **Mistral API**, **Cohere API**, **HuggingFace inference**, **Groq API**, or any other model provider, CLI, IDE, or AI-assisted tool — the user does so **at their own risk** and under the terms of service of that third-party tool.

The publisher:
- Does NOT recommend any specific third-party tool
- Does NOT receive any compensation or referral fee from any third-party tool's adoption
- Does NOT verify any third-party tool's GDPR compliance, AI Act compliance, or other regulatory posture
- Accepts NO responsibility for the user's choice of third-party tooling
- Accepts NO responsibility for any data leakage, confidentiality breach, professional-conduct violation, or regulatory non-compliance resulting from such third-party tool use
- Makes NO warranty that any third-party tool is suitable for EU legal-professional use

The user is **solely responsible** for verifying GDPR compliance, Article 28 processor contracts, Chapter V international transfer mechanisms, and bar conduct compliance for any third-party tool used alongside the Software.

---

## Output liability

The Software is provided **AS-IS** under the MIT License, without warranty of any kind, express or implied. The publisher is **NOT liable** for any output produced by the Software or any decision the user makes based on Software output.

**The user is the responsible operator.** Every output must be reviewed by the user before any client-facing use.

---

## Statutory currency

EU law evolves continuously. The Software's encoded knowledge has an AS-OF date documented in [KNOWLEDGE_PROVENANCE.md](KNOWLEDGE_PROVENANCE.md). Always verify against EUR-Lex, the relevant Member State's official gazette, and the relevant regulator's guidance before client work.

Particularly volatile areas as of 2026:
- **EU AI Act** (Regulation 2024/1689) — Annex III high-risk obligations begin enforcement August 2026
- **Digital Services Act** (Regulation 2022/2065) — full enforcement ongoing
- **Digital Markets Act** (Regulation 2022/1925) — designated gatekeeper proceedings ongoing
- **Data Act** (Regulation 2023/2854) — applies from September 2025
- **NIS2 Directive** (Directive 2022/2555) — Member State transposition ongoing
- **eIDAS 2.0** (Regulation 2024/1183) — EUDI wallet rollout
- **Regulation on Markets in Crypto-Assets** (MiCA — Regulation 2023/1114) — fully applicable

---

## Cross-border practice

The publisher does not offer cross-border legal services. The act of publishing software from India for use in the EU does NOT constitute the practice of law in any EU Member State by the publisher.

---

## Foreign judgment / enforcement

The publisher operates entirely from Indian soil with no assets in any EU Member State. Any claim against the publisher must comply with Indian law on enforcement of foreign judgments (Section 13, Code of Civil Procedure 1908) and the relevant EU-India treaty arrangements (very limited).

---

## Contact

For questions about this Disclaimer or Software functionality: **GitHub Issues** at the repository URL. The publisher does NOT accept legal-services engagement through this Software or its repository.

For security vulnerabilities only: see [SECURITY.md](SECURITY.md).

---

*This Disclaimer references LEGAL_EXPOSURE_PLAYBOOK §3.V1 (Copyright), §3.V2 (EU AI Act), §3.V3 (UPL — per-Member-State bar rules), §3.V4 (Data Protection — GDPR), §3.V6 (Advertising), §3.V8 (Cross-border), §5 (Jurisdictional Positioning EU), §6.D1-D12 (Discipline Rules), §8 (Personal-Jurisdiction Shield). Playbook version: v0.1.*
