from datetime import date, timedelta
import re

_MONTHS = {
    name.lower(): number
    for number, name in enumerate(
        (
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December",
        ),
        1,
    )
}

_PATTERNS = (
    re.compile(r"\b(\d{1,2})[-/](\d{1,2})[-/](\d{4})\b"),
    re.compile(r"\b(\d{4})-(\d{1,2})-(\d{1,2})\b"),
    re.compile(
        r"\b(\d{1,2})\s+("
        r"January|February|March|April|May|June|July|August|September|"
        r"October|November|December"
        r")\s+(\d{4})\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b("
        r"January|February|March|April|May|June|July|August|September|"
        r"October|November|December"
        r")\s+(\d{1,2})\s+(\d{4})\b",
        re.IGNORECASE,
    ),
)


def _find_date(text):
    for index, pattern in enumerate(_PATTERNS):
        match = pattern.search(text)
        if not match:
            continue

        parts = match.groups()
        try:
            if index == 0:
                return date(int(parts[2]), int(parts[1]), int(parts[0]))
            if index == 1:
                return date(int(parts[0]), int(parts[1]), int(parts[2]))
            if index == 2:
                return date(
                    int(parts[2]),
                    _MONTHS[parts[1].lower()],
                    int(parts[0]),
                )
            return date(
                int(parts[2]),
                _MONTHS[parts[0].lower()],
                int(parts[1]),
            )
        except (KeyError, ValueError):
            continue

    return None


def handle(payload: str) -> dict:
    text = str(payload or "")
    query = text.lower()

    if (
        "data subject access" in query
        or "dsar" in query
        or "subject access" in query
    ):
        category = "GDPR — DSAR response"
        period = "1 month"
        article = (
            "GDPR Art 12(3) "
            "(extendable +2 months for complex requests)"
        )
        years = None
    elif (
        "data breach" in query
        or "breach notification" in query
        or "personal data breach" in query
    ):
        category = "GDPR — breach notification"
        period = "72 hours"
        article = (
            "GDPR Art 33 "
            "(notify supervisory authority within 72 hours where feasible)"
        )
        years = None
    elif any(term in query for term in ("defamation", "libel", "slander")):
        category = "Defamation"
        period = "1 year"
        article = (
            "Statute of Limitations 1957 as amended by Defamation Act 2009 "
            "(extendable to 2 years)"
        )
        years = 1
    elif "personal injury" in query or "accident" in query:
        category = "Personal injury"
        period = "2 years"
        article = (
            "Statute of Limitations (Amendment) Act 1991 s3 "
            "(2 years from date of knowledge)"
        )
        years = 2
    elif any(term in query for term in ("land", "immovable", "possession")):
        category = "Recovery of land"
        period = "12 years"
        article = "Statute of Limitations 1957"
        years = 12
    elif "deed" in query or "specialty" in query:
        category = "Deed"
        period = "12 years"
        article = "Statute of Limitations 1957"
        years = 12
    elif any(term in query for term in ("contract", "breach", "debt", "loan")):
        category = "Contract"
        period = "6 years"
        article = "Statute of Limitations 1957 s 11"
        years = 6
    elif any(
        term in query
        for term in ("tort", "negligence", "nuisance", "trespass", "damage")
    ):
        category = "Tort"
        period = "6 years"
        article = "Statute of Limitations 1957 s 11"
        years = 6
    else:
        category = "General / residuary"
        period = "6 years"
        article = "Statute of Limitations 1957 s 11"
        years = 6

    start = _find_date(text)
    deadline = start + timedelta(days=years * 365) if start and years else None
    days_remaining = (deadline - date.today()).days if deadline else None

    return {
        "agent": "deadline_agent",
        "status": "ok",
        "category": category,
        "period": period,
        "article": article,
        "start_date": start.isoformat() if start else None,
        "deadline": deadline.isoformat() if deadline else None,
        "days_remaining": days_remaining,
        "note": (
            "Ireland is the common-law anchor; GDPR procedural deadlines "
            "included; member-state procedure varies — verify."
        ),
    }
