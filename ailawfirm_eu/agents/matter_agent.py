"""matter_agent — EU matter/case tracking.
PROVENANCE: CITED:02-court-rules-civil.md (Brussels I-bis process)"""


def handle(payload: str) -> dict:
    return {
        "agent": "matter_agent",
        "status": "v0.1 — EU matter tracking (stub)",
        "payload": payload[:200],
    }
