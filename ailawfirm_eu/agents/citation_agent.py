"""citation_agent — EU citation handling (ECLI / CELEX).
PROVENANCE: CITED:13-citation-format-primary.md"""

import re

_ECLI_PATTERN = re.compile(
    r"^ECLI:(?P<country>[A-Z]{2}):(?P<court>[A-Z]+):(?P<year>\d{4}):(?P<num>[A-Za-z0-9]+)$"
)
_CELEX_PATTERN = re.compile(r"^(?P<sector>[1-9])(?P<year>\d{4})(?P<type>[A-Z])(?P<num>\d{4,})$")


def handle(payload: str) -> dict:
    p = payload.strip()
    if not p:
        return {"agent": "citation_agent", "status": "empty query", "citations": []}

    results = []
    m = _ECLI_PATTERN.match(p)
    if m:
        results.append(
            {
                "type": "ECLI",
                "country": m.group("country"),
                "court": m.group("court"),
                "year": int(m.group("year")),
                "number": m.group("num"),
                "valid": True,
            }
        )

    m2 = _CELEX_PATTERN.match(p)
    if m2:
        results.append(
            {
                "type": "CELEX",
                "sector": m2.group("sector"),
                "year": int(m2.group("year")),
                "doc_type": m2.group("type"),
                "number": m2.group("num"),
                "valid": True,
            }
        )

    if not results:
        results.append(
            {
                "type": "UNKNOWN",
                "raw": p,
                "valid": False,
                "note": "No ECLI or CELEX pattern match. ECLI: EU:C:2024:567 | CELEX: 32024R1689",
            }
        )

    return {
        "agent": "citation_agent",
        "status": "v0.1 — ECLI + CELEX parser",
        "citations": results,
    }
