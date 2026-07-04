"""Tests for eu_calendar_sync MCP tool."""

from ailawfirm_eu.mcp_tools.calendar_sync import eu_calendar_sync


class TestCalendarSync:
    def test_list_empty(self):
        result = eu_calendar_sync("list")
        assert result["ok"]
        assert result["timezone"] == "Europe/Brussels"
        assert result["events"] == []

    def test_clear(self):
        result = eu_calendar_sync("clear")
        assert result["ok"]

    def test_add_event(self):
        result = eu_calendar_sync(
            "add EVT-001::MAT-001::hearing CJEU::full body::2026-06-15T10:00:00+02:00::2026-06-15T11:00:00+02:00::Luxembourg::hearing"
        )
        assert result["ok"]
        assert result["added"] == "EVT-001"
        assert result["store_size"] == 1

    def test_list_after_add(self):
        eu_calendar_sync("clear")
        eu_calendar_sync(
            "add EVT-002::MAT-002::deadline check::body::2026-06-15T10:00:00+02:00::2026-06-15T11:00:00+02:00"
        )
        result = eu_calendar_sync("list")
        assert result["ok"]
        assert len(result["events"]) == 1

    def test_invalid_payload(self):
        result = eu_calendar_sync(12345)
        assert not result["ok"]

    def test_unknown_command(self):
        result = eu_calendar_sync("fly to the moon")
        assert not result["ok"]
