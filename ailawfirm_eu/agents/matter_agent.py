import json
import os
from datetime import datetime, timezone
from pathlib import Path

_STORE_PATH = Path(os.path.expanduser("~/.ailawfirm_eu/matters.json"))


def _read_store():
    try:
        with _STORE_PATH.open("r", encoding="utf-8") as stream:
            value = json.load(stream)
        return value if isinstance(value, dict) else {}
    except (OSError, TypeError, ValueError):
        return {}


def _write_store(value):
    try:
        _STORE_PATH.parent.mkdir(parents=True, exist_ok=True)
        temporary = _STORE_PATH.with_suffix(".tmp")
        with temporary.open("w", encoding="utf-8") as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
        temporary.replace(_STORE_PATH)
        return True
    except (OSError, TypeError, ValueError):
        return False


def handle(payload: str) -> dict:
    text = str(payload or "").strip()
    query = text.lower()
    matters = _read_store()

    if query.startswith("add matter "):
        name = text[len("add matter "):].strip()
        action = "added"
    elif query.startswith("new matter "):
        name = text[len("new matter "):].strip()
        action = "added"
    else:
        name = ""
        action = ""

    if name:
        record = {
            "name": name,
            "note": "",
            "updated": datetime.now(timezone.utc).isoformat(),
        }
        matters[name] = record
        saved = _write_store(matters)
        return {
            "agent": "matter_agent",
            "status": "ok" if saved else "error",
            "action": action,
            "matter": record,
        }

    if query in ("list matters", "show matters", "my matters"):
        return {
            "agent": "matter_agent",
            "status": "ok",
            "matters": sorted(matters),
        }

    requested = None
    for prefix in ("status of ", "about ", "matter "):
        if query.startswith(prefix):
            requested = text[len(prefix):].strip()
            break

    if requested is not None:
        record = matters.get(requested)
        return {
            "agent": "matter_agent",
            "status": "ok",
            "matter": record,
            "found": record is not None,
        }

    return {
        "agent": "matter_agent",
        "status": "ok",
        "matters": sorted(matters),
    }
