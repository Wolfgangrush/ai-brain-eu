"""
Acceptance tests (TDD) — EU calendar_agent must delegate to the real backend.

The 'add' branch was a stub note. The real create/store logic already exists in
ailawfirm_eu.mcp_tools.calendar_sync.eu_calendar_sync — the agent must delegate to it
so an add actually creates+stores an event. NO 'stub' language anywhere.
"""

from ailawfirm_eu.agents import calendar_agent

_ADD = "add E1::M1::Directions hearing::Full matter body::2026-08-12T10:00:00+02:00::2026-08-12T11:00:00+02:00"


def test_add_creates_a_real_event():
    calendar_agent.handle("clear")
    r = calendar_agent.handle(_ADD)
    assert r.get("ok") is True
    # the event is actually stored — sync/list reflects it
    synced = calendar_agent.handle("sync")
    assert synced.get("ok") is True


def test_no_stub_language_anywhere():
    for q in [_ADD, "sync", "list", "clear"]:
        out = str(calendar_agent.handle(q)).lower()
        assert "stub" not in out, q


def test_agent_key_present():
    assert calendar_agent.handle("list").get("agent") == "calendar_agent"


def test_unknown_command_is_graceful():
    r = calendar_agent.handle("fly to the moon")
    assert r.get("agent") == "calendar_agent"
    assert r.get("ok") is False
