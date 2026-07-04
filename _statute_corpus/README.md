# EU Statute Corpus — v0.2 Knowledge Layer

## Purpose

This corpus provides structured statute-text digests of the EU regulatory framework for use by the firm's **Citation Clerk**, **Drafting Assistant**, and **Compliance Officer** specialists. Each digest distils the operative provisions of its parent instrument — scope, definitions, obligations, enforcement, and penalties — into a machine-readable structural skeleton. The corpus is the firm's primary statutory reference layer: every citation, compliance check, and drafting recommendation at v0.2+ draws its statutory authority from these files.

## Coverage

| # | Statute | Tier | Authority | Type |
|---|---|---|---|---|
| s01 | GDPR — General Data Protection Regulation (2016/679) | 1 | EUR-Lex | Regulation |
| s02 | EU AI Act (2024/1689) | 1 | EUR-Lex | Regulation |
| s03 | Digital Services Act (2022/2065) | 1 | EUR-Lex | Regulation |
| s04 | Digital Markets Act (2022/1925) | 1 | EUR-Lex | Regulation |
| s05 | Data Act (2023/2854) | 1 | EUR-Lex | Regulation |
| s06 | NIS2 Directive (2022/2555) | 1 | EUR-Lex | Directive |
| s07 | ePrivacy Directive (2002/58/EC) | 1 | EUR-Lex | Directive |
| s08 | Cyber Resilience Act (2024/2847) | 1 | EUR-Lex | Regulation |
| s09 | MiCA — Markets in Crypto-Assets Regulation (2023/1114) | 2 | EUR-Lex | Regulation |
| s10 | DORA — Digital Operational Resilience Act (2022/2554) | 2 | EUR-Lex | Regulation |
| s11 | Brussels Ia (1215/2012) | 2 | EUR-Lex | Regulation |

**Tier 1 (8/8):** Core EU digital-regulatory stack — every EU solo practitioner advising on data, AI, platforms, or cybersecurity needs these instruments at hand.
**Tier 2 (3/8):** Specialised and procedural instruments — operative-core coverage only; full section-level digestion deferred to a future corpus expansion.

## Source-tier discipline

- **Primary:** EUR-Lex (Official Journal of the EU) — every section digest links to its source CELEX number
- **Secondary:** EDPB guidelines, Commission Q&A, and OEM guidance — used only for interpretive triangulation, never as substitute for the legislative text
- **Rejected:** Law-firm blogs, SaaS commentary sites, unofficial consolidations (GDPR.eu used only for comparison)

## Currency warnings

- **AI Act:** Phased application (2025-2027). Each section tagged with its effective date.
- **Cyber Resilience Act:** Entered into force November 2024; full application November 2027.
- **NIS2:** Required national transposition by October 2024 — check your Member State's implementing legislation.
- **ePrivacy:** Directive 2002/58/EC is in force; the proposed ePrivacy Regulation replacement is still pending.

## AI Act phased-application note

The AI Act applies in four tranches. Every s02 section carries its applicable date:

| Date | Milestone |
|---|---|
| 2 February 2025 | Prohibited practices (Art 5) — in effect |
| 2 August 2025 | GPAI model obligations (Art 52-55) — in effect |
| 2 August 2026 | High-risk system obligations (Annex III, including Annex III §8 administration of justice) |
| 2 August 2027 | Technical annexes and remaining obligations |

> ⚠️ A proposed Digital Omnibus delay to December 2027 for high-risk obligations has NOT been adopted as of this corpus date. Treat 2 August 2026 as the binding compliance deadline.

## Known gaps

- **AI Act:** Some technical annexes summarised rather than verbatim due to length; CEN/CENELEC standards still under development.
- **DORA / MiCA:** Tier-2 level coverage only (operative core); full section-level digestion deferred.
- **Procedural statutes:** Rome I, Rome II, and Brussels Ia have limited section coverage.
- **~20 sections** across the corpus are marked NOT VERIFIED and require human follow-up on specific annexes or recitals.

## Provenance

Every section carries a `**STATUS:** VERIFIED | PARTIAL | NOT VERIFIED` marker. See [KNOWLEDGE_PROVENANCE.md](../KNOWLEDGE_PROVENANCE.md) for the full follow-up list and source ledger.

## How the firm uses this corpus

| Specialist | Consumption pattern |
|---|---|
| **Citation Clerk** | Reads statute files to validate ECLI/CELEX citations, resolve cross-references, and confirm operative-text currency before surfacing any statutory authority |
| **Drafting Assistant** | Pulls statutory obligations from the corpus to populate drafting templates — e.g., GDPR Art 28 obligations → DPA template; AI Act Annex IV → Technical Documentation template |
| **Compliance Officer** | Runs the corpus against published material — flags GDPR data-handling gaps, AI Act Article 50 transparency obligations, NIS2 cybersecurity baselines, and cross-border transfer issues under GDPR Chapter V |

## License

MIT — matches the parent repository ([ai-law-firm-eu](https://github.com/Wolfgangrush/ai-law-firm-eu)).

---

*Corpus generated 2026-05-20 · Stage 1c per 00-COMMAND-ROUTING pipeline.*
