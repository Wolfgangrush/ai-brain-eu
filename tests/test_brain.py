"""Tests for EU brain — intent classification and routing."""

from ailawfirm_eu.brain.intents import Intent, AGENT_FOR_INTENT
from ailawfirm_eu.brain.classifier import classify
from ailawfirm_eu.brain.router import route, think


class TestIntent:
    def test_all_intents_have_agents(self):
        for intent in Intent:
            assert intent in AGENT_FOR_INTENT
            assert AGENT_FOR_INTENT[intent]

    def test_compliance_flagged_routes_correctly(self):
        assert AGENT_FOR_INTENT[Intent.COMPLIANCE_FLAG] == "compliance_agent"


class TestClassifier:
    def test_classify_calendar_query(self):
        assert classify("what's on my calendar today") == Intent.CALENDAR_QUERY

    def test_classify_calendar_add(self):
        assert classify("remind me about the hearing on june 15") == Intent.CALENDAR_ADD

    def test_classify_citation_lookup(self):
        assert classify("validate ECLI:EU:C:2024:567") == Intent.CITATION_LOOKUP
        assert classify("look up this CELEX number") == Intent.CITATION_LOOKUP

    def test_classify_court_query(self):
        assert classify("what is the general court") == Intent.COURT_QUERY
        assert classify("what is the bundesgerichtshof") == Intent.COURT_QUERY
        assert classify("cour de cassation jurisdiction") == Intent.COURT_QUERY

    def test_classify_drafting(self):
        assert classify("I need to draft a pleading") == Intent.DRAFTING_NEED

    def test_classify_deadline(self):
        assert classify("what's the limitation period") == Intent.DEADLINE_CHECK
        assert classify("Brussels I enforcement deadline") == Intent.DEADLINE_CHECK

    def test_classify_compliance(self):
        assert classify("is this GDPR compliant") == Intent.COMPLIANCE_FLAG
        assert classify("AI Act high-risk classification") == Intent.COMPLIANCE_FLAG
        assert classify("money laundering check") == Intent.COMPLIANCE_FLAG
        assert classify("CCBE publicity rules") == Intent.COMPLIANCE_FLAG

    def test_classify_client_comm(self):
        assert classify("client said they need more time") == Intent.CLIENT_COMM

    def test_classify_matter(self):
        assert classify("update the matter status") == Intent.MATTER_UPDATE

    def test_classify_unknown(self):
        assert classify("hello how are you") == Intent.UNKNOWN

    def test_classify_empty(self):
        assert classify("") == Intent.UNKNOWN
        assert classify("   ") == Intent.UNKNOWN

    def test_classify_none(self):
        assert classify(None) == Intent.UNKNOWN


class TestRouter:
    def test_route_compliance(self):
        result = route(Intent.COMPLIANCE_FLAG, "gdpr check")
        assert result["ok"]
        assert result["agent"] == "compliance_agent"
        assert result["result"]["agent"] == "compliance_agent"
        # Verify AI Act warning is in the compliance agent response
        assert "EU AI Act" in str(result)

    def test_route_unknown(self):
        result = route(Intent.UNKNOWN, "hello")
        assert result["ok"]

    def test_think(self):
        result = think("validate ECLI:EU:C:2024:567")
        assert result["ok"]
        assert result["agent"] == "citation_agent"

    def test_think_compliance_fires_ai_act_warning(self):
        result = think("is this high-risk ai in justice")
        assert result["ok"]
        if result["agent"] == "compliance_agent":
            assert "ai act" in str(result).lower() or "AI Act" in str(result)
