# SCOPE.md — AI Brain · EU · Solo · v0.1

## IN SCOPE (v0.1)

### Core
- [x] EU ontology (MatterType, EUCourt, EUStatute, EUBarRule enums)
- [x] Matter / Citation / CalendarEvent dataclasses
- [x] Europe/Brussels timezone (CEST/CET handling)
- [x] Knowledge provenance ledger (all claims CITED to _research/)

### Brain + 7 Agents
- [x] Rule-based classifier (10 EU-specific keyword sets)
- [x] Brain router dispatching to 7 specialist agents
- [x] compliance_agent with AI Act Annex III HIGH-RISK warning
- [x] GDPR + AML + CCBE keyword firewalls

### 3 MCP Tools
- [x] eu_court_lookup — CJEU + General Court + ECHR + 5 national supreme courts
- [x] eu_citation_validator — ECLI (EU:C, EU:T, national codes) + CELEX
- [x] eu_calendar_sync — ICS writer with Europe/Brussels timezone

### Language Support
- [x] GETTING_STARTED.md (English authoritative, ~250 lines)
- [x] 12 language variants (~120 lines each) with AI-assisted disclaimer
- [x] Arabic (RTL) with Unicode rendering notes
- [x] TRANSLATION_HELP_WANTED.md (community PR call)

### Documentation
- [x] README.md with AI Act warning + language picker + currency table
- [x] SCOPE.md (this file)
- [x] KNOWLEDGE_PROVENANCE.md (claim ledger)
- [x] STATUS.md (build progress tracker)

### Compliance
- [x] AI Act Annex III compliance_agent warning
- [x] GDPR Art 33 breach-notification flag
- [x] 5AMLD + AMLR 2024 currency notes
- [x] CCBE Code publicity / cross-border flags

### Quality
- [x] ruff check + ruff format clean
- [x] 40+ tests passing
- [x] .gitignore sensitive content firewall
- [x] No GitHub push (local build only)

## OUT OF SCOPE (deferred to v0.2+)

### Firm mode
- [ ] Multi-user auth / roles
- [ ] Billing / invoicing
- [ ] Conflict-of-interest checker
- [ ] Matter delegation

### AI-powered features
- [ ] AI legal research / case summarization (High-Risk — needs conformity assessment)
- [ ] Predictive analytics (case outcome prediction)
- [ ] Automated document drafting with AI
- [ ] Natural language → ECLI search

### Integrations
- [ ] e-Curia API (CJEU e-filing)
- [ ] National e-filing system plugins (LexNET, ERV, etc.)
- [ ] Google Calendar / Outlook bidirectional sync
- [ ] CURIA cause-list scraping

### Content
- [ ] Full statute text for all 27 Member States
- [ ] National bar rules for all 27 Member States
- [ ] Case law database
- [ ] Legal forms / templates

### Infrastructure
- [ ] Web UI / Electron app
- [ ] Cloud sync / backup
- [ ] Mobile app
- [ ] Multi-language UI (all 24 EU official languages)

## Version roadmap

| Version | Focus | Target |
|---|---|---|
| v0.1 | Solo practice OS — memory + agents + MCP tools + 13 languages | May 2026 |
| v0.2 | Firm mode — multi-user, billing, conflict-check | TBD |
| v0.3 | AI-powered features (High-Risk compliant) | TBD |
| v1.0 | Full EU solo+firm practice OS | TBD |
