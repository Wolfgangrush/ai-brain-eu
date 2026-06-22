"""calendar_agent — EU calendar sync.
PROVENANCE: ADR-002 D4-D7 (ICS feed)
Timezone: Europe/Brussels (CET/CEST)"""

from ailawfirm_eu.core.ontology import CalendarEvent

_EVENT_STORE: list[CalendarEvent] = []


def handle(payload: str) -> dict:
    if not isinstance(payload, str):
        return {"ok": False, "error": "payload must be a string"}

    p = payload.strip().lower()

    if p in ("sync", "publish", ""):
        return {
            "agent": "calendar_agent",
            "ok": True,
            "event_count": len(_EVENT_STORE),
            "events": [
                {"id": e.event_id, "summary": e.summary_alias, "start": e.start_iso}
                for e in _EVENT_STORE
            ],
            "timezone": "Europe/Brussels",
        }
    if p.startswith("add"):
        return {
            "agent": "calendar_agent",
            "ok": True,
            "note": "Event add — parsed (stub in v0.1 MCP tool)",
            "timezone": "Europe/Brussels",
        }
    if p == "list":
        return {
            "agent": "calendar_agent",
            "ok": True,
            "events": [
                {"id": e.event_id, "summary": e.summary_alias, "start": e.start_iso}
                for e in _EVENT_STORE
            ],
            "timezone": "Europe/Brussels",
        }
    if p == "clear":
        _EVENT_STORE.clear()
        return {"agent": "calendar_agent", "ok": True, "note": "event store cleared"}

    return {
        "agent": "calendar_agent",
        "ok": False,
        "error": f"unknown command: {payload[:40]}",
        "timezone": "Europe/Brussels",
    }
