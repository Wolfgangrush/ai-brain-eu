"""Calendar agent for the ailawfirm_eu package.

This agent manages court, matter, and deadline calendar entries for the
European law-firm workflow. All times are anchored to Europe/Brussels,
which is the canonical jurisdiction-local timezone used across the EU
calendar surfaces (court rosters, client appointments, limitation
deadlines, and statutory filings).

The agent is intentionally thin: it does not own any persistent state
itself. Instead it delegates every operation to the real backend
implemented in :mod:`ailawfirm_eu.mcp_tools.calendar_sync`, which is the
authoritative source of calendar events and ICS generation.
"""

from ailawfirm_eu.mcp_tools.calendar_sync import eu_calendar_sync

__all__ = ["handle"]

_AGENT_NAME = "calendar_agent"
_DEFAULT_TIMEZONE = "Europe/Brussels"


def handle(payload):
    """Dispatch a calendar payload to the real backend.

    Parameters
    ----------
    payload : str
        A command string understood by ``eu_calendar_sync``. Supported
        commands include ``add ...`` (create a calendar event),
        ``sync`` (write the ICS file), ``list`` (return current
        events) and ``clear`` (reset the event store).

    Returns
    -------
    dict
        The result dictionary produced by ``eu_calendar_sync`` with two
        extra keys injected by this agent:

        * ``agent`` -- always set to ``"calendar_agent"`` so callers can
          tell which agent produced the response.
        * ``timezone`` -- defaults to ``"Europe/Brussels"`` when the
          underlying backend does not already specify one.

        If ``payload`` is not a string, a clearly-typed error response
        is returned directly without touching the backend.
    """
    if not isinstance(payload, str):
        return {
            "agent": _AGENT_NAME,
            "ok": False,
            "error": "payload must be a string",
        }

    result = eu_calendar_sync(payload)

    if not isinstance(result, dict):
        return {
            "agent": _AGENT_NAME,
            "ok": False,
            "error": "backend returned a non-dict response",
        }

    result["agent"] = _AGENT_NAME
    result.setdefault("timezone", _DEFAULT_TIMEZONE)
    return result
