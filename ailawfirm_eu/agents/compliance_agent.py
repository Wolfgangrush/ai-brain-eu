"""compliance_agent — EU AI Act Annex III + GDPR + AML + CCBE keyword firewall.
PROVENANCE: CITED:23-ai-law-firm-regulatory-stance.md (AI Act)
PROVENANCE: CITED:04-statute-data-protection.md (GDPR)
PROVENANCE: CITED:27-anti-money-laundering-obligations.md (AML)
PROVENANCE: CITED:10-bar-rule-publicity-solicitation.md (CCBE)"""

from ailawfirm_eu.core.ontology import EUBarRule


def handle(payload: str) -> dict:
    p = payload.lower()
    flags = []
    if any(k in p for k in ["ai act", "high-risk ai", "annex iii", "ai in justice"]):
        flags.append(
            {
                "rule": "EU AI Act (Reg 2024/1689) — Annex III HIGH-RISK if AI used in administration of justice",
                "concern": (
                    "This tool is matter-management (low risk), NOT a judicial-decision AI. "
                    "But if your query is about deploying ANY AI for substantive judicial reasoning, "
                    "that AI is High-Risk classified — conformity assessment + human oversight + "
                    "risk management mandatory."
                ),
                "research_ref": "23-ai-law-firm-regulatory-stance.md",
            }
        )
    if any(
        k in p for k in ["gdpr", "personal data", "data subject", "data protection", "data breach"]
    ):
        flags.append(
            {
                "rule": "GDPR — Regulation (EU) 2016/679",
                "concern": "72-hour DPA breach notification · DPIA for high-risk processing · Art 35",
                "research_ref": "04-statute-data-protection.md",
            }
        )
    if any(k in p for k in ["aml", "amld", "amlr", "money laundering", "kyc", "ubo"]):
        flags.append(
            {
                "rule": "5AMLD (current) -> AMLR + 6AMLD (applies July 2027)",
                "concern": (
                    "Lawyers are gatekeepers under 5AMLD — KYC + UBO + "
                    "suspicious transaction reporting"
                ),
                "research_ref": "27-anti-money-laundering-obligations.md",
            }
        )
    if any(k in p for k in ["ccbe", "publicity", "solicit", "advertis", "cross-border"]):
        flags.append(
            {
                "rule": EUBarRule.CCBE_PUBLICITY.value,
                "concern": "Check both home-bar and host-bar rules · CCBE 2.6 publicity baseline",
                "research_ref": "10-bar-rule-publicity-solicitation.md",
            }
        )
    return {
        "agent": "compliance_agent",
        "status": "v0.1 — EU AI Act + GDPR + AML firewall",
        "flags": flags,
        "note": "AI Act Annex III compliance module active. HIGH-RISK warning fires on 'ai in justice' / 'high-risk ai' queries.",
    }
