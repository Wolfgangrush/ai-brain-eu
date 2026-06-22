"""Tests for eu_citation_validator MCP tool — ECLI + CELEX."""

from ailawfirm_eu.mcp_tools.citation_validator import eu_citation_validator


class TestECLI:
    def test_ecli_cjeu(self):
        result = eu_citation_validator("ECLI:EU:C:2024:567")
        assert result["valid"]
        assert result["format"] == "ECLI"
        assert result["ecli_country"] == "EU"
        assert result["ecli_court"] == "C"
        assert result["ecli_year"] == 2024
        assert result["ecli_number"] == "567"

    def test_ecli_general_court(self):
        result = eu_citation_validator("ECLI:EU:T:2024:234")
        assert result["valid"]
        assert result["format"] == "ECLI"
        assert result["ecli_court"] == "T"

    def test_ecli_national(self):
        result = eu_citation_validator("ECLI:DE:BGH:2024:abc123")
        assert result["valid"]
        assert result["ecli_country"] == "DE"
        assert result["ecli_court"] == "BGH"

    def test_ecli_invalid_format(self):
        result = eu_citation_validator("ECLI:EU:C:2024")  # missing number
        assert not result["valid"]
        assert result["format"] == "UNKNOWN"


class TestCELEX:
    def test_celex_gdpr(self):
        result = eu_citation_validator("32024R1689")
        assert result["valid"]
        assert result["format"] == "CELEX"
        assert result["celex_sector"] == "3"
        assert result["celex_year"] == 2024
        assert result["celex_type"] == "R"
        assert result["celex_number"] == "1689"

    def test_celex_basic(self):
        result = eu_citation_validator("32016R0679")
        assert result["valid"]
        assert result["format"] == "CELEX"


class TestInvalid:
    def test_garbage_input(self):
        result = eu_citation_validator("not a citation")
        assert not result["valid"]
        assert result["format"] == "UNKNOWN"

    def test_non_string(self):
        result = eu_citation_validator(12345)
        assert not result["valid"]
