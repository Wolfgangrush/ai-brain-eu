"""Tests for EU ontology module."""

from ailawfirm_eu.core.ontology import (
    MatterType,
    EUCourt,
    EUStatute,
    EUBarRule,
    Matter,
    Citation,
    CalendarEvent,
)


class TestMatterType:
    def test_all_matter_types_exist(self):
        assert len(list(MatterType)) >= 9
        assert MatterType.DIRECT_ACTION_CJEU.value == "Direct action before CJEU"
        assert MatterType.PRELIMINARY_REFERENCE.value == "Preliminary reference (Art 267 TFEU)"
        assert MatterType.GDPR_COMPLAINT.value == "GDPR complaint to DPA"
        assert MatterType.BRUSSELS_I_ENFORCEMENT.value == "Brussels I-bis cross-border enforcement"

    def test_matter_type_unique_values(self):
        vals = [m.value for m in MatterType]
        assert len(vals) == len(set(vals))


class TestEUCourt:
    def test_all_courts_exist(self):
        courts = list(EUCourt)
        assert len(courts) >= 10
        assert EUCourt.CJEU.value == "Court of Justice of the European Union (Luxembourg)"
        assert EUCourt.GENERAL_COURT.value == "General Court of the EU"

    def test_echr_not_eu(self):
        assert "Council of Europe" in EUCourt.ECHR.value
        assert "not EU" in EUCourt.ECHR.value

    def test_national_courts_present(self):
        national_courts = [
            EUCourt.NATIONAL_SUPREME_FRANCE,
            EUCourt.NATIONAL_SUPREME_GERMANY,
            EUCourt.NATIONAL_SUPREME_ITALY,
            EUCourt.NATIONAL_SUPREME_SPAIN,
            EUCourt.NATIONAL_SUPREME_NETHERLANDS,
        ]
        for court in national_courts:
            assert court.value


class TestEUStatute:
    def test_key_statutes_exist(self):
        assert EUStatute.GDPR.value
        assert EUStatute.AI_ACT.value
        assert EUStatute.BRUSSELS_I_BIS.value
        assert EUStatute.ROME_I.value
        assert EUStatute.ROME_II.value
        assert EUStatute.AML_5.value
        assert EUStatute.AML_6_2024.value

    def test_ai_act_has_currency_warning(self):
        assert "CURRENCY" in EUStatute.AI_ACT.value
        assert "Aug 2026" in EUStatute.AI_ACT.value

    def test_aml_6_has_currency_warning(self):
        assert "applies July 2027" in EUStatute.AML_6_2024.value


class TestEUBarRule:
    def test_key_rules_exist(self):
        assert EUBarRule.CCBE_CODE.value
        assert EUBarRule.CCBE_PUBLICITY.value
        assert EUBarRule.CCBE_CONFIDENTIALITY.value
        assert EUBarRule.CCBE_CONFLICT.value

    def test_ccbe_publicity_mentions_rule_number(self):
        assert "2.6" in EUBarRule.CCBE_PUBLICITY.value


class TestMatter:
    def test_create_matter(self):
        m = Matter(
            matter_id="MAT-2026-001",
            matter_type=MatterType.PRELIMINARY_REFERENCE,
            court=EUCourt.CJEU,
            short_title="Test Case",
        )
        assert m.matter_id == "MAT-2026-001"
        assert m.matter_type == MatterType.PRELIMINARY_REFERENCE
        assert m.court == EUCourt.CJEU
        assert m.parties_plaintiff == []
        assert m.statutes_invoked == []
        assert m.filed_date is None


class TestCitation:
    def test_create_ecli_citation(self):
        c = Citation(
            raw="ECLI:EU:C:2024:567",
            format="ECLI",
            ecli_country="EU",
            ecli_court="C",
            ecli_year=2024,
            ecli_number="567",
            valid=True,
        )
        assert c.valid
        assert c.ecli_country == "EU"

    def test_create_celex_citation(self):
        c = Citation(
            raw="32024R1689",
            format="CELEX",
            celex_sector="3",
            celex_year=2024,
            celex_type="R",
            celex_number="1689",
            valid=True,
        )
        assert c.valid
        assert c.celex_type == "R"


class TestCalendarEvent:
    def test_create_event(self):
        e = CalendarEvent(
            event_id="EVT-001",
            matter_id="MAT-001",
            summary_alias="hearing | CJEU | C-403/03",
            start_iso="2026-06-15T10:00:00+02:00",
            end_iso="2026-06-15T11:00:00+02:00",
            location="Luxembourg",
            event_type="hearing",
        )
        assert e.event_id == "EVT-001"
        assert e.event_type == "hearing"
        assert "+02:00" in e.start_iso  # CEST
