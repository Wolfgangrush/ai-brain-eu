"""Calendar publishers — local ICS file output.
PROVENANCE: ADR-002 D4-D7."""

from pathlib import Path


def default_local_path() -> Path:
    return Path.home() / ".ailawfirm-eu" / "calendar" / "eu_matters.ics"


def publish_local(ics_path: Path) -> dict:
    """Publish ICS file locally. Returns subscribe URL for local file protocol."""
    abs_path = str(ics_path.resolve())
    return {
        "protocol": "file",
        "subscribe_url": f"file://{abs_path}",
        "path": abs_path,
    }
