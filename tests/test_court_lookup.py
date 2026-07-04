"""Tests for eu_court_lookup MCP tool."""

from ailawfirm_eu.mcp_tools.court_lookup import eu_court_lookup


class TestEUCourtLookup:
    def test_cjeu_lookup(self):
        result = eu_court_lookup("CJEU")
        assert result["found"]
        assert "Luxembourg" in result["location"]
        assert result["tier"] == "supreme"

    def test_general_court_lookup(self):
        result = eu_court_lookup("General Court")
        assert result["found"]
        assert result["tier"] == "first_instance"

    def test_echr_lookup(self):
        result = eu_court_lookup("ECHR")
        assert result["found"]
        assert "Strasbourg" in result["location"]

    def test_french_court_lookup(self):
        result = eu_court_lookup("cour de cassation")
        assert result["found"]
        assert "France" in result.get("location", "")

    def test_german_court_lookup(self):
        result = eu_court_lookup("bundesgerichtshof")
        assert result["found"]
        assert "Germany" in result["location"]

    def test_unknown_court(self):
        result = eu_court_lookup("supreme court of mars")
        assert not result["found"]

    def test_invalid_input(self):
        result = eu_court_lookup(12345)
        assert not result["found"]
        assert "error" in result
