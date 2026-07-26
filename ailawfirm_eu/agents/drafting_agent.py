"""Drafting router for the EU (GDPR + Ireland common-law) brain.

Pure stdlib. No network. Classifies a payload into a document type and points
at the shared `draft-with-docx` skill (no local template files).
"""

from __future__ import annotations

from typing import Any

SUGGESTED_SKILL = "draft-with-docx"

NEXT_STEP = (
    "Invoke draft-with-docx with the case folder; "
    "for GDPR instruments verify the current EDPB guidance; "
    "for pleadings verify the relevant member-state procedure."
)

NOTE = (
    "EU brain covers GDPR instruments and the Ireland common-law litigation "
    "default. Member-state procedure varies \u2014 confirm the governing forum."
)

# Order matters: first match wins.
_RULES: tuple[tuple[tuple[str, ...], str], ...] = (
    (
        ("dsar", "data subject access"),
        "DSAR Response (GDPR Art 15)",
    ),
    (
        ("dpia", "data protection impact", "impact assessment"),
        "DPIA (GDPR Art 35)",
    ),
    (
        ("records of processing", "ropa", "article 30"),
        "Records of Processing (GDPR Art 30)",
    ),
    (
        ("breach notification", "data breach"),
        "Personal Data Breach Notification (GDPR Art 33/34)",
    ),
    (
        ("standard contractual clauses", "scc"),
        "Standard Contractual Clauses",
    ),
    (
        ("plenary summons", "statement of claim"),
        "Statement of Claim / Plenary Summons (Ireland)",
    ),
    (
        ("defence",),
        "Defence (Ireland)",
    ),
    (
        ("cjeu", "preliminary reference"),
        "CJEU Preliminary Reference",
    ),
    (
        ("legal opinion", "advice", "memorandum"),
        "Legal Opinion / Advice",
    ),
)

DEFAULT_DOC_TYPE = "General document (confirm doc type)"


def _classify(payload: str) -> str:
    text = (payload or "").lower()
    for keywords, doc_type in _RULES:
        for keyword in keywords:
            if keyword in text:
                return doc_type
    return DEFAULT_DOC_TYPE


def handle(payload: str) -> dict[str, Any]:
    """Classify the payload and return a routing suggestion."""
    return {
        "agent": "drafting_agent",
        "status": "classified",
        "doc_type": _classify(payload),
        "suggested_skill": SUGGESTED_SKILL,
        "next_step": NEXT_STEP,
        "note": NOTE,
    }
