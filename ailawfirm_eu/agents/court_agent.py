"""court_agent — EU court information.
PROVENANCE: CITED:01-court-hierarchy.md"""

from ailawfirm_eu.core.ontology import EUCourt

_COURT_INFO: dict[EUCourt, dict] = {
    EUCourt.CJEU: {
        "name": "Court of Justice of the European Union (CJEU)",
        "location": "Luxembourg",
        "tier": "supreme",
        "jurisdiction": "Final interpreter of EU law · preliminary rulings (Art 267 TFEU) · direct actions · appeals",
        "working_language": "French (internal)",
        "research_ref": "01-court-hierarchy.md",
    },
    EUCourt.GENERAL_COURT: {
        "name": "General Court of the EU",
        "location": "Luxembourg",
        "tier": "first_instance",
        "jurisdiction": (
            "Direct actions by individuals/companies against EU institutions · "
            "Member State actions · IP cases"
        ),
        "research_ref": "01-court-hierarchy.md",
    },
    EUCourt.ECHR: {
        "name": "European Court of Human Rights",
        "location": "Strasbourg, France",
        "tier": "international",
        "jurisdiction": "European Convention on Human Rights — Council of Europe body (NOT EU institution)",
        "research_ref": "01-court-hierarchy.md",
    },
    EUCourt.NATIONAL_SUPREME_FRANCE: {
        "name": "Cour de cassation / Conseil d'Etat (France)",
        "location": "Paris",
        "tier": "national_supreme",
        "research_ref": "32-member-state-france.md",
    },
    EUCourt.NATIONAL_SUPREME_GERMANY: {
        "name": "Bundesgerichtshof / Bundesverwaltungsgericht (Germany)",
        "location": "Karlsruhe / Leipzig",
        "tier": "national_supreme",
        "research_ref": "31-member-state-germany.md",
    },
    EUCourt.NATIONAL_SUPREME_ITALY: {
        "name": "Corte suprema di cassazione (Italy)",
        "location": "Rome",
        "tier": "national_supreme",
        "research_ref": "33-member-state-italy.md",
    },
    EUCourt.NATIONAL_SUPREME_SPAIN: {
        "name": "Tribunal Supremo (Spain)",
        "location": "Madrid",
        "tier": "national_supreme",
        "research_ref": "34-member-state-spain.md",
    },
    EUCourt.NATIONAL_SUPREME_NETHERLANDS: {
        "name": "Hoge Raad der Nederlanden",
        "location": "The Hague",
        "tier": "national_supreme",
        "research_ref": "35-member-state-netherlands.md",
    },
}


def _fuzzy_match(query: str) -> EUCourt | None:
    q = query.lower().strip()
    if not q:
        return None
    for court in EUCourt:
        if q in court.value.lower() or q in court.name.lower():
            return court
    return None


def handle(payload: str) -> dict:
    if not isinstance(payload, str):
        return {"found": False, "error": "payload must be a string"}
    matched = _fuzzy_match(payload)
    if matched is None or matched not in _COURT_INFO:
        return {"found": False, "query": payload, "available_courts": list(_COURT_INFO.keys())}
    info = dict(_COURT_INFO[matched])
    info["matched_enum"] = matched.name
    info["found"] = True
    return info
