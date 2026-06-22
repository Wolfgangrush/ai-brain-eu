# EU Drafting Data — v0.2 Knowledge Layer

## Purpose

This corpus provides structured drafting-template digests for use by the firm's **Drafting Assistant** specialist. Each file contains the structural skeleton of a supranational EU template — headings, operative sections, recital blocks, signature blocks, and filing metadata — without reproducing the full annotated text. The Drafting Assistant reads these skeletons to scaffold client-ready drafts, validate mandatory clauses, and ensure jurisdiction-appropriate formatting.

## Coverage

| Category | Count | Files |
|---|---|---|
| Foundations & Guides | 1 | 90-drafting-style-guide.md |
| Data Protection & AI Compliance | 8 | 01-dpa · 02-data-breach-notification · 03-dpia · 04-ropa · 05-bcrs · 06-ai-act-conformity · 07-ai-act-fria · 08-privacy-policy |
| Digital Services & Commercial Contracts | 7 | 10-dsa-statement-of-reasons · 11-sccs · 12-employment · 15-choice-of-law · 16-ai-transparency-notice · 17-nis2-incident-notification · 18-cra-declaration-of-conformity |
| Pleading & Motion Templates | 3 | 20-cjeu-application · 25-cjeu-preliminary-reference · 35-dma-challenge |
| Intellectual Property & Competition | 4 | 50-euipo-opposition · 52-euipo-cancellation · 53-competition-complaint · 55-euipo-application |
| Cross-Border & Human Rights | 2 | 51-brussels-ia-certificate · 54-echr-application |
| Statutory Notices | 1 | 80-sar |
| **Total** | **26** | |

**Tier 1 (9/9):** DPA · SCCs · DPIA · ROPA · BCRs · AI Act Conformity · AI Act FRIA · CJEU Application · CJEU Preliminary Reference — every EU solo practitioner's core drafting workload.
**Tier 2 (9/9):** Remaining templates covering DSA, NIS2, CRA, EUIPO, competition, employment, ECHR, and Brussels Ia certificate filings.
**Tier 3 (8 expected):** Additional specialised templates deferred to a future corpus expansion.

## Source-tier discipline

Template authority hierarchy, in descending order:

1. **Commission Implementing Decision** — e.g., SCCs 2021/914, DPA 2021/915
2. **EDPB / EUIPO / CJEU official template or form** — harmonised EU-wide instruments
3. **National DPA published template** — used only where no supranational equivalent exists
4. **Court Rules with attached forms** — CJEU Rules of Procedure, ECHR Rule 47
5. **Academic drafting commentary** — citation only, fair-use only

**Never sourced from:** law-firm marketing pages, SaaS template libraries, or unofficial blog consolidations.

## Copyright firewall

This corpus contains:

- **Permitted:** statute text where the EU instrument grants reuse (EUR-Lex permits reuse with attribution; OJ instruments are public-domain text under EU IP rules) · structural summaries of templates · short fair-use quotes from commentary (under fair-dealing thresholds)
- **NOT contained:** full-text reproduction of copyrighted templates (Practical Law · Halsbury's · LexisNexis annotated commentaries · law-firm proprietary drafts) · full annotated commentary by EDPB beyond paraphrase

If you find any file in this corpus containing such material, please open an issue. We will purge within 24 hours.

Source-tier discipline (template authority hierarchy):
1. Commission Implementing Decision (e.g., SCCs 2021/914)
2. EDPB / EUIPO / CJEU official template or form
3. National DPA published template (where supranational equivalent absent)
4. Court Rules with attached forms
5. Academic drafting commentary (citation only, fair-use only)

## Currency warnings

- **CJEU Preliminary References:** 2024 procedural reform transferred certain jurisdictions to the General Court; verify case type before filing.
- **AI Act Compliance:** Most Tier-1 obligations (Technical Documentation, FRIA, Transparency) have an 2 August 2026 deadline.
- **NIS2 Notification:** The 24-hour Early Warning is a strict compliance trigger — missed deadlines carry significant penalties.

## Provenance

Every file carries `## Source URL` + `## Last Verified` + `## Authority Tier` headers. See [KNOWLEDGE_PROVENANCE.md](../KNOWLEDGE_PROVENANCE.md) for the full source ledger with CELEX links.

## How the firm uses this corpus

| Specialist | Consumption pattern |
|---|---|
| **Drafting Assistant** | Reads template skeletons to scaffold client drafts — pulls statutory obligations from the statute corpus, maps them to template clauses, and ensures mandatory provisions are present before the draft leaves the firm |
| **Citation Clerk** | Cross-references template source URLs against the statute corpus to verify that every cited instrument is current and correctly linked |

## License

MIT — matches the parent repository ([ai-law-firm-eu](https://github.com/Wolfgangrush/ai-law-firm-eu)).

---

*Corpus generated 2026-05-20 · Stage 1b per 00-COMMAND-ROUTING pipeline.*
