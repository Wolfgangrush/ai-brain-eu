"""
eu_citation_validator MCP tool — v0.1.

Validates and parses EU legal citations: ECLI + CELEX.
PROVENANCE: CITED:_research/13-citation-format-primary.md (ECLI + CELEX formats)
"""

import re
from ailawfirm_eu.core.ontology import Citation

_ECLI_PATTERN = re.compile(
    r"^ECLI:(?P<country>[A-Z]{2}):(?P<court>[A-Z]+):(?P<year>\d{4}):(?P<num>[A-Za-z0-9]+)$"
)
# CELEX: sector (1 digit) + year (4 digits) + type (1 letter) + number (4+ digits)
# e.g., 32024R1689 = sector 3 (legislation), year 2024, type R (Regulation), number 1689
_CELEX_PATTERN = re.compile(
    r"^(?P<sector>[1-9])(?P<year>\d{4})(?P<doc_type>[A-Z])(?P<number>\d{4,})$"
)


def eu_citation_validator(citation_string: str) -> dict:
    if not isinstance(citation_string, str):
        return _to_dict(
            Citation(
                raw=str(citation_string),
                format="UNKNOWN",
                parse_notes="input was not a string",
            )
        )

    s = citation_string.strip()

    m = _ECLI_PATTERN.match(s)
    if m:
        return _to_dict(
            Citation(
                raw=s,
                format="ECLI",
                ecli_country=m.group("country"),
                ecli_court=m.group("court"),
                ecli_year=int(m.group("year")),
                ecli_number=m.group("num"),
                valid=True,
            )
        )

    m2 = _CELEX_PATTERN.match(s)
    if m2:
        return _to_dict(
            Citation(
                raw=s,
                format="CELEX",
                celex_sector=m2.group("sector"),
                celex_year=int(m2.group("year")),
                celex_type=m2.group("doc_type"),
                celex_number=m2.group("number"),
                valid=True,
            )
        )

    return _to_dict(
        Citation(
            raw=s,
            format="UNKNOWN",
            valid=False,
            parse_notes=(
                "No ECLI or CELEX pattern match. "
                "ECLI format: ECLI:EU:C:2024:567. "
                "CELEX format: 32024R1689 (GDPR). "
            ),
        )
    )


def _to_dict(c: Citation) -> dict:
    result = {
        "raw": c.raw,
        "format": c.format,
        "valid": c.valid,
        "parse_notes": c.parse_notes,
    }
    if c.format == "ECLI":
        result["ecli_country"] = c.ecli_country
        result["ecli_court"] = c.ecli_court
        result["ecli_year"] = c.ecli_year
        result["ecli_number"] = c.ecli_number
    elif c.format == "CELEX":
        result["celex_sector"] = c.celex_sector
        result["celex_year"] = c.celex_year
        result["celex_type"] = c.celex_type
        result["celex_number"] = c.celex_number
    return result
