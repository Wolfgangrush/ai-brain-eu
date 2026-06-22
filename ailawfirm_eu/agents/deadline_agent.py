"""deadline_agent — EU limitation / filing deadline checks.
PROVENANCE: CITED:09-statute-limitation-act.md
PROVENANCE: CITED:02-court-rules-civil.md (Brussels I-bis deadlines)"""


def handle(payload: str) -> dict:
    p = payload.lower()
    flags = []
    if any(k in p for k in ["limitation", "prescription", "time bar"]):
        flags.append(
            {
                "type": "limitation_period",
                "note": "EU limitation periods vary by Member State and cause of action. "
                "Rome II Art 15 governs applicable limitation law in cross-border torts.",
                "research_ref": "09-statute-limitation-act.md",
            }
        )
    if any(k in p for k in ["service", "brussels", "enforcement"]):
        flags.append(
            {
                "type": "brussels_i_bis_deadline",
                "note": "Brussels I-bis enforcement certificate (Annex I). "
                "Lis pendens — first-seized court rule (Art 29).",
                "research_ref": "02-court-rules-civil.md",
            }
        )
    return {
        "agent": "deadline_agent",
        "status": "v0.1 — EU deadline awareness",
        "flags": flags,
    }
