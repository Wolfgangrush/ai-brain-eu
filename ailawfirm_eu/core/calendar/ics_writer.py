"""ICS writer — EU calendar sync.
Timezone: Europe/Brussels (CET/CEST)
PROVENANCE: ADR-002 D4-D7."""

from pathlib import Path
from ailawfirm_eu.core.ontology import CalendarEvent


def write_ics(events: list[CalendarEvent], output_path: Path) -> dict:
    """Write CalendarEvent list to .ics file."""
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//AI Brain EU v0.1//EN",
        "X-WR-TIMEZONE:Europe/Brussels",
    ]
    for e in events:
        lines.extend(
            [
                "BEGIN:VEVENT",
                f"UID:{e.event_id}@ailawfirm_eu",
                f"SUMMARY:{e.summary_alias}",
                f"DESCRIPTION:{e.body_full}",
                f"DTSTART:{_format_dt(e.start_iso)}",
                f"DTEND:{_format_dt(e.end_iso)}",
            ]
        )
        if e.location:
            lines.append(f"LOCATION:{e.location}")
        lines.append("END:VEVENT")
    lines.append("END:VCALENDAR")

    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            f.write("\r\n".join(lines) + "\r\n")
        return {"ok": True, "path": str(output_path), "event_count": len(events)}
    except OSError as exc:
        return {"ok": False, "error": str(exc)}


def _format_dt(iso_str: str) -> str:
    """Convert ISO datetime to ICS format: 20260518T140000Z or 20260518T140000."""
    if not iso_str:
        return ""
    s = iso_str.replace("-", "").replace(":", "")
    if "T" not in s:
        return s + "T000000"
    return s[:15]
