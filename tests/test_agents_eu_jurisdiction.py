"""
Acceptance test (TDD) — EU drafting_agent (the only stub; matter+deadline work).

EU brain is regulatory + Ireland-common-law: the drafting router classifies GDPR
instruments (DSAR response, DPIA Art 35, RoPA Art 30, breach notification Art 33/34,
SCCs), Irish pleadings (plenary summons, statement of claim, defence), and CJEU
references, all pointing at draft-with-docx. NO Indian/SG/US/UK-specific residue.
"""

import re


from ailawfirm_eu.agents import drafting_agent

FOREIGN_RESIDUE = re.compile(
    r"\b1963\b|CrPC|BNSS|\bSLP\b|\b482\b|\bwrit\b|anticipatory\s+bail|indian-|"
    r"ailawfirm[-_]india|ROC 2021|\bSGHC\b|ailawfirm[_-]singapore|\bFRCP\b|"
    r"ailawfirm[_-]usa|ailawfirm[_-]uk",
    re.I,
)


def _flat(d: dict) -> str:
    return " ".join(str(v) for v in d.values())


class TestDraftingEU:
    def test_dsar_recognised(self):
        r = drafting_agent.handle("draft a DSAR response to a data subject access request")
        b = _flat(r).lower()
        assert "dsar" in b or "data subject access" in b

    def test_dpia_recognised(self):
        r = drafting_agent.handle("draft a data protection impact assessment")
        b = r.get("doc_type", "").lower()
        assert "dpia" in b or "impact assessment" in b

    def test_breach_notification_recognised(self):
        r = drafting_agent.handle("draft a personal data breach notification to the supervisory authority")
        assert "breach" in r.get("doc_type", "").lower()

    def test_irish_pleading_recognised(self):
        r = drafting_agent.handle("draft a statement of claim / plenary summons")
        b = r.get("doc_type", "").lower()
        assert "statement of claim" in b or "plenary summons" in b

    def test_shape_keys(self):
        r = drafting_agent.handle("draft a legal opinion")
        assert "doc_type" in r and "suggested_skill" in r

    def test_points_at_draft_with_docx(self):
        assert "draft-with-docx" in _flat(drafting_agent.handle("draft a DPIA")).lower()

    def test_no_foreign_residue(self):
        for q in ["draft a DSAR", "draft a writ petition", "draft an SLP", "draft a complaint under FRCP"]:
            assert not FOREIGN_RESIDUE.search(_flat(drafting_agent.handle(q))), q
