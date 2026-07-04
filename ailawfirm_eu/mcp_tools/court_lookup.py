"""
eu_court_lookup MCP tool — v0.1.

Resolves EU court name (fuzzy) to structured court info.
PROVENANCE: CITED:_research/01-court-hierarchy.md
PROVENANCE: CITED:_research/31-38-member-state-*.md (national courts)
"""

from typing import Optional
from ailawfirm_eu.core.ontology import EUCourt


_COURT_INFO: dict[EUCourt, dict] = {
    EUCourt.CJEU: {
        "name": "Court of Justice of the European Union (CJEU)",
        "location": "Luxembourg",
        "tier": "supreme",
        "jurisdiction_class": (
            "Final interpreter of EU law. Preliminary rulings (Art 267 TFEU), "
            "direct actions (Art 263 TFEU), infringement proceedings (Art 258 TFEU), appeals."
        ),
        "working_language": "French (internal). Proceedings in any of 24 official EU languages.",
        "judges": "27 Judges + 11 Advocates General",
        "research_ref": "01-court-hierarchy.md",
    },
    EUCourt.GENERAL_COURT: {
        "name": "General Court of the EU",
        "location": "Luxembourg",
        "tier": "first_instance",
        "jurisdiction_class": (
            "Direct actions brought by individuals and companies against EU institutions. "
            "Member State actions against Commission/Council. IP, competition, State aid cases."
        ),
        "judges": "54 Judges (two per Member State as of 2019)",
        "research_ref": "01-court-hierarchy.md",
    },
    EUCourt.ECHR: {
        "name": "European Court of Human Rights",
        "location": "Strasbourg, France",
        "tier": "international",
        "jurisdiction_class": (
            "European Convention on Human Rights (ECHR). "
            "NOTE: Council of Europe body — NOT an EU institution. "
            "Individual applications after exhaustion of domestic remedies."
        ),
        "research_ref": "01-court-hierarchy.md",
    },
    EUCourt.NATIONAL_SUPREME_FRANCE: {
        "name": "Cour de cassation (civil/criminal) / Conseil d'Etat (administrative)",
        "location": "Paris, France",
        "tier": "national_supreme",
        "jurisdiction_class": "Final appellate court for French law. Can refer to CJEU under Art 267 TFEU.",
        "research_ref": "32-member-state-france.md",
    },
    EUCourt.NATIONAL_SUPREME_GERMANY: {
        "name": "Bundesgerichtshof (civil/criminal) / Bundesverwaltungsgericht (administrative)",
        "location": "Karlsruhe / Leipzig, Germany",
        "tier": "national_supreme",
        "jurisdiction_class": "Final appellate court for German law. Bundesverfassungsgericht (constitutional) separate.",
        "research_ref": "31-member-state-germany.md",
    },
    EUCourt.NATIONAL_SUPREME_ITALY: {
        "name": "Corte suprema di cassazione",
        "location": "Rome, Italy",
        "tier": "national_supreme",
        "jurisdiction_class": "Final appellate court for Italian law. Corte Costituzionale for constitutional matters.",
        "research_ref": "33-member-state-italy.md",
    },
    EUCourt.NATIONAL_SUPREME_SPAIN: {
        "name": "Tribunal Supremo",
        "location": "Madrid, Spain",
        "tier": "national_supreme",
        "jurisdiction_class": "Final appellate court for Spanish law. Tribunal Constitucional separate.",
        "research_ref": "34-member-state-spain.md",
    },
    EUCourt.NATIONAL_SUPREME_NETHERLANDS: {
        "name": "Hoge Raad der Nederlanden",
        "location": "The Hague, Netherlands",
        "tier": "national_supreme",
        "jurisdiction_class": "Final appellate court for Dutch law (civil/criminal/tax). Raad van State for administrative.",
        "research_ref": "35-member-state-netherlands.md",
    },
}


def _fuzzy_match(query: str) -> Optional[EUCourt]:
    q = query.lower().strip()
    if not q:
        return None
    for court in EUCourt:
        if q in court.value.lower() or q in court.name.lower():
            return court
    return None


def eu_court_lookup(court_name: str) -> dict:
    if not isinstance(court_name, str):
        return {"found": False, "error": "court_name must be a string"}
    matched = _fuzzy_match(court_name)
    if matched is None or matched not in _COURT_INFO:
        return {
            "found": False,
            "query": court_name,
            "available_courts": sorted([c.name for c in _COURT_INFO if c in _COURT_INFO]),
        }
    info = dict(_COURT_INFO[matched])
    info["matched_enum"] = matched.name
    info["found"] = True
    return info
