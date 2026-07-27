"""
Acceptance tests (TDD) — EU deadline_agent + matter_agent (both were stub-in-disguise).

deadline_agent: Ireland Statute of Limitations 1957 (the EU brain's common-law anchor)
for litigation limitation, PLUS the two GDPR procedural clocks a practitioner needs
(DSAR response 1 month Art 12(3); personal-data-breach notification 72 hours Art 33).
matter_agent: local store under ~/.ailawfirm_eu. NO foreign residue.
"""

import inspect
import re


from ailawfirm_eu.agents import deadline_agent, matter_agent

FOREIGN_RESIDUE = re.compile(
    r"\b1963\b|CrPC|BNSS|\bSLP\b|\b482\b|\bwrit\b|indian-|ailawfirm[-_]india|"
    r"Limitation Act 1959|Limitation Act 1980|ROC 2021|\bSGHC\b|ailawfirm[_-]singapore|"
    r"\bFRCP\b|\bUCC\b|ailawfirm[_-]usa|ailawfirm[_-]uk|\bDIFC\b|ailawfirm[_-]dubai",
    re.I,
)


def _flat(d: dict) -> str:
    return " ".join(str(v) for v in d.values())


class TestDeadlineEU:
    def test_contract_six_years_1957(self):
        b = _flat(deadline_agent.handle("limitation for a breach of contract claim"))
        assert "6 year" in b.lower()
        assert "Statute of Limitations 1957" in b

    def test_tort_six_years(self):
        b = _flat(deadline_agent.handle("tort negligence property damage claim")).lower()
        assert "6 year" in b

    def test_personal_injury_two_years(self):
        b = _flat(deadline_agent.handle("personal injury claim after an accident")).lower()
        assert "2 year" in b

    def test_defamation_one_year(self):
        b = _flat(deadline_agent.handle("defamation libel claim")).lower()
        assert "1 year" in b or "one year" in b

    def test_recovery_of_land_twelve_years(self):
        b = _flat(deadline_agent.handle("action to recover land")).lower()
        assert "12 year" in b

    def test_gdpr_dsar_one_month(self):
        b = _flat(deadline_agent.handle("deadline to respond to a data subject access request DSAR")).lower()
        assert "1 month" in b or "one month" in b

    def test_gdpr_breach_72_hours(self):
        b = _flat(deadline_agent.handle("personal data breach notification deadline")).lower()
        assert "72" in b

    def test_shape_keys(self):
        r = deadline_agent.handle("contract claim")
        for k in ("agent", "category", "period"):
            assert k in r

    def test_no_foreign_residue(self):
        for q in ["contract claim", "personal injury", "data breach", "recover land"]:
            assert not FOREIGN_RESIDUE.search(_flat(deadline_agent.handle(q))), q


class TestMatterEU:
    def test_store_path_is_eu(self):
        src = inspect.getsource(matter_agent)
        assert ".ailawfirm_eu" in src
        assert ".ailawfirm-india" not in src and ".ailawfirm_singapore" not in src

    def test_add_then_list_roundtrip(self, tmp_path, monkeypatch):
        store = tmp_path / "matters.json"
        monkeypatch.setattr(matter_agent, "_STORE_PATH", store, raising=False)
        matter_agent.handle("add matter Data Protection Commission v Meta")
        assert "Meta" in _flat(matter_agent.handle("list matters"))

    def test_shape_keys(self):
        assert matter_agent.handle("list matters").get("agent") == "matter_agent"

    def test_not_a_stub(self):
        out = _flat(matter_agent.handle("list matters")).lower()
        assert "stub" not in out and "v0.2" not in out and "v0.1 —" not in out

    def test_no_foreign_residue(self):
        for q in ["add matter ABC", "list matters", "status of XYZ"]:
            assert not FOREIGN_RESIDUE.search(_flat(matter_agent.handle(q))), q
