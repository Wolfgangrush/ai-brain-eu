"""
Ontology module — AI Brain · EU · Solo · v0.1

EU legal-practice enums. All values traced to _research/ files
per KNOWLEDGE_PROVENANCE.md.

PROVENANCE: CITED:_research/01-court-hierarchy.md for EUCourt
PROVENANCE: CITED:_research/02-court-rules-civil.md for MatterType (Brussels I-bis process names)
PROVENANCE: CITED:_research/04-statute-data-protection.md for GDPR statute refs
PROVENANCE: CITED:_research/10-bar-rule-publicity-solicitation.md for EUBarRule
PROVENANCE: CITED:_research/13-citation-format-primary.md for ECLI/CELEX
PROVENANCE: CITED:_research/23-ai-law-firm-regulatory-stance.md for AI Act
PROVENANCE: CITED:_research/27-anti-money-laundering-obligations.md for AML
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


class MatterType(Enum):
    """EU matter type codes — v0.1 set.
    PROVENANCE: CITED:02-court-rules-civil.md (Brussels I-bis)"""

    DIRECT_ACTION_CJEU = "Direct action before CJEU"
    PRELIMINARY_REFERENCE = "Preliminary reference (Art 267 TFEU)"
    INFRINGEMENT_ACTION = "Infringement action (Art 258 TFEU)"
    NATIONAL_CIVIL = "National civil proceeding (national court)"
    NATIONAL_CRIMINAL = "National criminal proceeding"
    ARBITRATION_ICC = "ICC arbitration"
    GDPR_COMPLAINT = "GDPR complaint to DPA"
    AI_ACT_COMPLAINT = "AI Act complaint to national authority"
    BRUSSELS_I_ENFORCEMENT = "Brussels I-bis cross-border enforcement"
    OTHER = "Other"


class EUCourt(Enum):
    """EU court hierarchy.
    PROVENANCE: CITED:01-court-hierarchy.md"""

    CJEU = "Court of Justice of the European Union (Luxembourg)"
    GENERAL_COURT = "General Court of the EU"
    ECHR = "European Court of Human Rights (Strasbourg — Council of Europe, not EU)"
    NATIONAL_SUPREME_FRANCE = "Cour de cassation / Conseil d'Etat (France)"
    NATIONAL_SUPREME_GERMANY = "Bundesgerichtshof / Bundesverwaltungsgericht (Germany)"
    NATIONAL_SUPREME_ITALY = "Corte suprema di cassazione (Italy)"
    NATIONAL_SUPREME_SPAIN = "Tribunal Supremo (Spain)"
    NATIONAL_SUPREME_NETHERLANDS = "Hoge Raad (Netherlands)"
    NATIONAL_SUPREME_POLAND = "Sad Najwyzszy (Poland)"
    NATIONAL_SUPREME_SWEDEN = "Hogsta domstolen (Sweden)"
    OTHER = "Other"


class EUStatute(Enum):
    """EU statute registry — v0.1 references.
    Real text deferred to v0.2+. PROVENANCE: see KNOWLEDGE_PROVENANCE.md."""

    TFEU = "Treaty on the Functioning of the EU"
    TEU = "Treaty on European Union"
    GDPR = "GDPR — Regulation (EU) 2016/679"
    AI_ACT = "AI Act — Regulation (EU) 2024/1689 (CURRENCY: High-Risk obligations from Aug 2026)"
    BRUSSELS_I_BIS = "Brussels I-bis — Regulation (EU) 1215/2012"
    ROME_I = "Rome I — Regulation (EC) 593/2008"
    ROME_II = "Rome II — Regulation (EC) 864/2007"
    AML_5 = "5th Anti-Money-Laundering Directive (current)"
    AML_6_2024 = "AML Package 2024 — AMLR + 6AMLD (applies July 2027)"
    DIGITAL_SERVICES_ACT = "Digital Services Act — Regulation 2022/2065"
    DIGITAL_MARKETS_ACT = "Digital Markets Act — Regulation 2022/1925"
    DIGITALISATION_REGULATION = "Digitalisation Regulation — 2023/2844 (PHASE-IN)"


class EUBarRule(Enum):
    """CCBE Code of Conduct rule references.
    PROVENANCE: CITED:10-bar-rule-publicity-solicitation.md
                CITED:11-bar-rule-conflict-of-interest.md
                CITED:12-bar-rule-confidentiality.md"""

    CCBE_CODE = "CCBE Code of Conduct for European Lawyers"
    CCBE_PUBLICITY = "CCBE Code 2.6 — publicity (cross-border)"
    CCBE_CONFIDENTIALITY = "CCBE Code 2.3.1 — confidentiality as primary duty"
    CCBE_INDEPENDENCE = "CCBE Code 2.1.1 — lawyer independence"
    CCBE_CONFLICT = "CCBE Code 3.2.1 — conflict of interest"
    CCBE_FEE_SHARING = "CCBE Code 3.6.1 — fee sharing prohibition"
    CCBE_CLIENT_FUNDS = "CCBE Code 3.8.1 — client funds in supervised account"
    CCBE_INSURANCE = "CCBE Code 3.9 — professional indemnity insurance"
    NATIONAL_BAR_RULES = "National bar rules — check per Member State"


@dataclass
class Matter:
    """A single matter (case file) — v0.1 shape only.
    PROVENANCE: STUB — full lifecycle in v0.2+"""

    matter_id: str
    matter_type: MatterType
    court: EUCourt
    short_title: str
    parties_plaintiff: list[str] = field(default_factory=list)
    parties_defendant: list[str] = field(default_factory=list)
    statutes_invoked: list[EUStatute] = field(default_factory=list)
    filed_date: Optional[str] = None  # ISO YYYY-MM-DD
    next_hearing_date: Optional[str] = None  # used by calendar_agent
    next_hearing_location: Optional[str] = None
    status_note: Optional[str] = None


@dataclass
class Citation:
    """A parsed EU legal citation.
    PROVENANCE: CITED:13-citation-format-primary.md"""

    raw: str
    format: str  # 'ECLI' | 'CELEX' | 'UNKNOWN'
    ecli_country: Optional[str] = None  # e.g., 'EU', 'DE', 'FR'
    ecli_court: Optional[str] = None  # e.g., 'C', 'T', 'BGH'
    ecli_year: Optional[int] = None
    ecli_number: Optional[str] = None
    celex_sector: Optional[str] = None  # e.g., '3' for legislation
    celex_year: Optional[int] = None
    celex_type: Optional[str] = None  # e.g., 'R' for Regulation
    celex_number: Optional[str] = None
    valid: bool = False
    parse_notes: Optional[str] = None


@dataclass
class CalendarEvent:
    """A calendar event written to the ICS feed by calendar_agent.
    PROVENANCE: ADR-002 D7 (alias summary discipline)."""

    event_id: str
    matter_id: Optional[str] = None
    summary_alias: str = ""  # lock-screen safe summary
    body_full: str = ""  # full matter detail
    start_iso: str = ""  # YYYY-MM-DDTHH:MM:SS+01:00 / +02:00 (CET/CEST)
    end_iso: str = ""
    location: Optional[str] = None
    event_type: str = "hearing"  # hearing | deadline | reminder | client_meeting
