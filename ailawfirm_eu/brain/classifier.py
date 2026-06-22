"""Rule-based intent detection — EU v0.1."""

from ailawfirm_eu.brain.intents import Intent

_RULES: list[tuple[list[str], Intent]] = [
    (
        ["calendar", "diary", "agenda", "next week", "show today", "what's on"],
        Intent.CALENDAR_QUERY,
    ),
    (["add to calendar", "schedule", "block out", "remind me"], Intent.CALENDAR_ADD),
    (["citation", "ecli", "cjeu", "curia", "cite", "celex"], Intent.CITATION_LOOKUP),
    (
        [
            "court",
            "cjeu",
            "general court",
            "echr",
            "national court",
            "preliminary reference",
            "bundesgerichtshof",
            "cour de cassation",
            "tribunal supremo",
            "hoge raad",
            "curia",
            "luxembourg",
            "strasbourg",
        ],
        Intent.COURT_QUERY,
    ),
    (["draft", "drafting", "pleading", "submission", "skeleton"], Intent.DRAFTING_NEED),
    (
        [
            "deadline",
            "limitation",
            "term",
            "expiry",
            "service deadline",
            "brussels i",
            "rome i",
            "rome ii",
        ],
        Intent.DEADLINE_CHECK,
    ),
    (["client said", "client called", "client wants"], Intent.CLIENT_COMM),
    (
        [
            "gdpr",
            "data protection",
            "data breach",
            "dpa",
            "ccbe",
            "publicity",
            "ai act",
            "high-risk",
            "high risk ai",
            "annex iii",
            "amld",
            "amlr",
            "money laundering",
            "kyc",
            "ubo",
            "personal data",
        ],
        Intent.COMPLIANCE_FLAG,
    ),
    (["matter", "hearing", "filed", "judgment", "order", "service"], Intent.MATTER_UPDATE),
]


def classify(text: str) -> Intent:
    if not isinstance(text, str) or not text.strip():
        return Intent.UNKNOWN
    t = text.lower()
    for keywords, intent in _RULES:
        if any(kw in t for kw in keywords):
            return intent
    return Intent.UNKNOWN
