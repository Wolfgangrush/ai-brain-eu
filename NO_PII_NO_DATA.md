# NO_PII_NO_DATA — Zero-Collection Architecture (EU)

**This document explains why AI Brain — EU collects no personal data from the user, and what that means under GDPR.**

---

## TL;DR

The publisher (wolfgang_rush) operates **zero infrastructure** that touches user data. There is no server. There is no telemetry. There is no analytics. The Software runs entirely on the user's device.

---

## The architectural guarantee

AI Brain — EU is **local-first** software. Specifically:

**(1) The codebase contains zero telemetry.** Verify with:
```bash
grep -rE "telemetry|analytics|tracking|posthog|mixpanel|segment|amplitude|google-analytics|datadog|sentry" ailawfirm_eu/
```
Should return only legitimate cloud-AI calls (user-initiated, routed direct to user's chosen vendor).

**(2) The publisher operates no server.** No AI Brain EU API. No cloud service. No database. The publisher's only infrastructure is the public GitHub repository.

**(3) Storage is on the user's device.** All persistent state lives under `~/.ailawfirm-eu/`. The publisher has no access to this folder.

**(4) Network calls are limited to:**
- Package installation (PyPI)
- User-initiated AI cloud calls (only if user opts into cloud mode — direct to vendor)
- Optional update checks (v0.2+ if added — opt-in only)

---

## Cloud-mode (when the user opts in)

If the user chooses to use cloud AI processing, queries route **directly from the user's device to the AI vendor**. The publisher is not in the data path.

For client-confidential work covered by professional secrecy and GDPR Article 9 special categories, do NOT use cloud mode without an Article 28 GDPR-compliant processor contract with the vendor. Use local-only mode.

---

## GDPR analysis — Publisher's status

**The publisher is NOT a Controller.** GDPR Article 4(7) defines "controller" as the entity that determines the purposes and means of processing. The publisher determines neither.

**The publisher is NOT a Processor.** GDPR Article 4(8) defines "processor" as an entity processing personal data on behalf of a controller. The publisher processes no data on anyone's behalf.

**The publisher is NOT a Joint Controller.** GDPR Article 26 joint-controller status requires determining purposes and means together with another party. The publisher does neither.

**The publisher is a software publisher.** Publishing open-source software is not "processing of personal data" under GDPR Article 4(2). It is publication activity governed by EU Copyright Directive (2019/790) and Member State copyright law, not GDPR.

---

## Your status as Controller when using this Software

If the user uses this Software to process personal data of EU data subjects, **the user** is the Controller.

GDPR obligations (non-exhaustive):
- Article 5 — Principles (lawfulness · fairness · transparency · purpose limitation · data minimisation · accuracy · storage limitation · integrity & confidentiality · accountability)
- Article 6 — Lawful basis (consent · contract · legal obligation · vital interests · public task · legitimate interests)
- Article 9 — Special categories (health · biometric · political · religious · sexual orientation · trade union · genetic) — explicit consent or specific derogations
- Articles 12-14 — Transparency / information at collection
- Articles 15-22 — Data subject rights (access · rectification · erasure · restriction · portability · objection · automated decision-making)
- Article 25 — Data protection by design and by default
- Article 28 — Processor contracts (apply if you use cloud AI vendors)
- Article 30 — Records of processing activities
- Article 32 — Security of processing
- Article 33 — Breach notification to supervisory authority within 72 hours
- Article 34 — Breach communication to data subjects without undue delay
- Article 35 — DPIA for high-risk processing
- Article 37 — DPO appointment where required
- Article 44+ — International transfers (Chapter V)

---

## International transfers (GDPR Chapter V)

If the user opts into cloud mode and the cloud vendor processes data outside the EU/EEA, GDPR Chapter V applies to that transfer:

- **Article 45** — Adequacy decisions (limited list: Andorra · Argentina · Canada (commercial) · Faroe Islands · Guernsey · Isle of Man · Israel · Japan · Jersey · New Zealand · Republic of Korea · Switzerland · United Kingdom · Uruguay · USA (under EU-US Data Privacy Framework, subject to recurring challenges))
- **Article 46** — Appropriate safeguards (Standard Contractual Clauses · Binding Corporate Rules · approved Codes of Conduct · approved Certification mechanisms)
- **Article 47** — Binding Corporate Rules
- **Article 49** — Derogations (narrow — explicit consent · contract necessity · public interest · legal claims · vital interests · public register · compelling legitimate interests)
- **Schrems II case-law** — supplementary measures required for transfers to jurisdictions with surveillance laws (notably USA)

Many cloud AI vendors are US-based. If you opt into US-vendor cloud mode for EU client data, you must verify:
1. The vendor has an Article 28 DPA
2. The transfer relies on a valid mechanism (DPF · SCCs + supplementary measures · BCRs · etc.)
3. The DPIA addresses the transfer risk

The publisher transfers no data anywhere — these obligations are entirely the user's.

---

## ePrivacy / cookie / IoT considerations

The Software does not use cookies (no browser surface). The Software does not place tags or trackers. The Software does not integrate with telematics or IoT devices in v0.1.

---

## Verification path

The user can independently verify zero-collection:

1. `grep -rE "telemetry|analytics|posthog|mixpanel|segment|amplitude|google-analytics|datadog|sentry" ailawfirm_eu/`
2. `cat requirements.txt`
3. Run offline test (cloud-AI calls fail visibly; local features work)
4. Network inspection with `nettop` / `nethogs` / Resource Monitor

---

## If this changes

Future telemetry additions will be announced in CHANGELOG · default OFF · opt-in only · documented here. Code is the truth.

---

*This document references LEGAL_EXPOSURE_PLAYBOOK §2(b) (Zero Data Collection pillar), §3.V4 (Data Protection — GDPR + ePrivacy + Schrems II). Playbook version: v0.1.*
