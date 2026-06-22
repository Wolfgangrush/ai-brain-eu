"""
eu_calendar_sync MCP tool — v0.1.

Writes the current matter calendar to an .ics file and publishes it.
Timezone: Europe/Brussels (CET/CEST)
PROVENANCE: ADR-002 D4-D7.
"""

from ailawfirm_eu.core.calendar.ics_writer import write_ics
from ailawfirm_eu.core.calendar.publishers import publish_local, default_local_path
from ailawfirm_eu.core.ontology import CalendarEvent

_EVENT_STORE: list[CalendarEvent] = []


def eu_calendar_sync(payload: str) -> dict:
    """Calendar sync MCP entry point.

    v0.1 commands:
        "sync" / "publish"  -> write all events to .ics + publish
        "add <event_id>::<matter_id>::<summary_alias>::<body>::<start_iso>::<end_iso>[::<location>][::<type>]"
                            -> register an event in the in-memory store
        "list"              -> list events currently in store
        "clear"             -> reset event store (v0.1 dev convenience)
    """
    if not isinstance(payload, str):
        return {"ok": False, "error": "payload must be a string"}

    p = payload.strip().lower()

    if p in ("sync", "publish", ""):
        return _do_sync()
    if p.startswith("add"):
        return _do_add(payload.strip())
    if p == "list":
        return {
            "ok": True,
            "timezone": "Europe/Brussels",
            "events": [
                {"id": e.event_id, "summary": e.summary_alias, "start": e.start_iso}
                for e in _EVENT_STORE
            ],
        }
    if p == "clear":
        _EVENT_STORE.clear()
        return {"ok": True, "note": "event store cleared"}

    return {"ok": False, "error": f"unknown command: {payload[:40]}"}


def _do_sync() -> dict:
    out = default_local_path()
    w = write_ics(_EVENT_STORE, out)
    if not w["ok"]:
        return w
    pub = publish_local(out)
    return {
        "ok": True,
        "timezone": "Europe/Brussels",
        "wrote_path": w["path"],
        "event_count": w["event_count"],
        "publish": pub,
        "subscribe_via": pub["subscribe_url"],
    }


def _do_add(payload: str) -> dict:
    """Parse 'add <event_id>::<matter_id>::<summary>::<body>::<start>::<end>[::<location>][::<type>]'"""
    body = payload[3:].strip()
    parts = body.split("::")
    if len(parts) < 6:
        return {
            "ok": False,
            "error": (
                "add requires at least 6 ::-separated fields: "
                "event_id::matter_id::summary_alias::body_full::start_iso::end_iso"
                "[::location][::type]"
            ),
        }
    e = CalendarEvent(
        event_id=parts[0].strip(),
        matter_id=parts[1].strip() or None,
        summary_alias=parts[2].strip(),
        body_full=parts[3].strip(),
        start_iso=parts[4].strip(),
        end_iso=parts[5].strip(),
        location=parts[6].strip() if len(parts) > 6 else None,
        event_type=parts[7].strip() if len(parts) > 7 else "hearing",
    )
    _EVENT_STORE.append(e)
    return {"ok": True, "added": e.event_id, "store_size": len(_EVENT_STORE)}
