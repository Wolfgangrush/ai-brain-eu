# Getting Started — AI Brain for EU Lawyers · v0.1

**🙏 Welcome, Maître / Herr Anwalt / Señor Abogado — your AI Brain begins here.**

This guide takes you from zero to running your own AI-powered EU practice OS in about 30 minutes.

---

## What this is

AI Brain EU is a **memory-first practice management assistant** for EU solo lawyers. It runs entirely on your machine — no cloud, no API keys, no telemetry. Your case files never leave your computer.

Built on the local memory layer (MIT), it remembers your matters, checks deadlines, validates ECLI/CELEX citations, looks up EU courts, syncs your practice calendar to ICS, and flags compliance risks before they become disciplinary problems.

**It does NOT:** perform judicial reasoning, predict case outcomes, or draft substantive legal arguments. See the AI Act disclaimer below.

---

## Before you start

You need:
- macOS, Linux, or WSL2 on Windows
- Python 3.9 or later
- Terminal (Terminal.app, iTerm2, GNOME Terminal, etc.)
- 5 minutes of focus

---

## Install (30 seconds)

```bash
# Clone the repo
cd ~/Desktop
git clone https://github.com/Wolfgangrush/ai-law-firm-eu.git
cd ai-law-firm-eu

# Install in development mode
pip install -e .
```

Verified: the CLI is now available as `ailawfirm-eu`. Test it:

```bash
ailawfirm-eu --help
```

---

## Initialize your practice (2 minutes)

```bash
# Create a practice directory (anywhere you like)
mkdir ~/my-eu-practice

# Initialize it as an AI Brain palace
ailawfirm-eu init ~/my-eu-practice
```

This scans your directory and creates the memory palace structure at `~/.ailawfirm-eu/`. If you have existing case files, it auto-detects them.

---

## Your first search (30 seconds)

```bash
# Mine your practice files into memory
ailawfirm-eu mine ~/my-eu-practice

# Search for anything
ailawfirm-eu search "Brussels I-bis enforcement"
```

---

## 7 specialist agents — what they do

| Agent | Trigger keywords | What you get |
|---|---|---|
| `matter_agent` | matter, hearing, filed, judgment | Case tracking + matter updates |
| `citation_agent` | ecli, celex, citation, cjeu | ECLI/CELEX citation validation |
| `court_agent` | cjeu, general court, bundesgerichtshof, cour de cassation | Court hierarchy + jurisdiction info |
| `drafting_agent` | draft, pleadings, submission | EU procedure-aware drafting assistance (stub v0.1) |
| `deadline_agent` | deadline, limitation, brussels i | Limitation + filing deadline checks |
| `calendar_agent` | calendar, schedule, diary | ICS calendar sync (Europe/Brussels tz) |
| `compliance_agent` | gdpr, ai act, high-risk, aml, ccbe | AI Act + GDPR + AML + CCBE firewall |

---

## 3 MCP tools — for Claude Code / AI assistants

Register these with your AI assistant for richer EU law support:

```bash
# eu_court_lookup — find any EU court
# eu_citation_validator — validate ECLI & CELEX citations
# eu_calendar_sync — manage your practice calendar
```

---

## Privacy + Data Location

Everything is local. The palace lives at `~/.ailawfirm-eu/palace` (ChromaDB). The calendar ICS file at `~/.ailawfirm-eu/calendar/eu_matters.ics`. No telemetry. No cloud sync. Your practice is yours.

Under GDPR: you are the data controller of your own practice data. The tool processes nothing externally.

---

## ⚠️ AI Act Disclaimer (mandatory read)

**The EU AI Act (Regulation 2024/1689) classifies AI systems used "in administration of justice" as HIGH-RISK (Annex III point 8).**

This tool is **matter-management software** (Minimal Risk category). It does NOT:
- Perform legal reasoning or judicial decision-making
- Predict case outcomes
- Draft substantive legal arguments autonomously
- Replace a lawyer's professional judgment

If you deploy ANY AI for substantive judicial reasoning, that AI is High-Risk classified and requires: conformity assessment, human oversight mechanisms, risk management system, and transparency documentation. The `compliance_agent` in this tool fires an explicit warning whenever your query enters AI-in-justice territory. Do not bypass it.

---

## Currency watch

| Regulation | Current | Next |
|---|---|---|
| AI Act — Prohibitions | Active since Feb 2025 | — |
| AI Act — High-Risk obligations | Phased | From Aug 2026 |
| AML | 5AMLD (current) | AMLR + 6AMLD from Jul 2027 |
| Digitalisation | Phasing in | Mandatory digital cross-border |

---

## Troubleshooting

**"No palace found"** → Run `ailawfirm-eu init ~/my-eu-practice` first.

**"Module not found"** → You're in the wrong directory. `cd ~/Desktop/ai-law-firm-eu` and `pip install -e .`

**ChromaDB issues on macOS** → `brew install chromadb` or `pip install chromadb --upgrade`

---

## Next steps

- Read `MODEL_SETUP.md` to configure Claude Code / ChatGPT with MCP tools
- Read `SCOPE.md` to understand what's in/out for v0.1
- Read `KNOWLEDGE_PROVENANCE.md` for the full legal source ledger
- Read `DISCLAIMER.md` for full legal disclaimers
- Join the translation effort: `TRANSLATION_HELP_WANTED.md`

---

## Credits

- local memory architecture by milla-jovovich (MIT)
- 35 authoritative EU legal research sources in `_research/`
- wolfgang_rush, 2026 — MIT License

---

🙏 Welcome · Bienvenue · Willkommen · Bienvenido · Benvenuto · Welkom · Witaj · Välkommen · Bem-vindo · Vítejte · Καλώς ήρθατε · Bun venit · أهلاً وسهلاً
