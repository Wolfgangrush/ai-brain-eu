# 🇪🇺 AI Brain for EU Lawyers

> **Free practice OS for every EU solo lawyer (avocat · Anwalt · advocaat · abogado · avvocato · advokát · δικηγόρος · advokat · adwokat · ügyvéd · advogado · etc.). Terminal-native. Local-first by default (Ollama + Qwen3 / Mistral — nothing leaves your laptop). Cloud-LLM optional with the [Pseudonymisation Gateway](https://github.com/Wolfgangrush/pseudonymisation-gateway) sanitising PII before any prompt leaves the machine; Chapter V Article 46 supplementary safeguards remain YOUR responsibility for US-routed cloud transmission.**

**For qualified legal professionals only.** Intended for lawyers admitted to practice in any EU Member State under the relevant national bar regulation, lawyers registered for cross-border practice under Directive 98/5/EC (Establishment Directive), in-house counsel of EU entities, trainee lawyers / stagiaires under supervision, and paralegals working under supervision. **If you are not a qualified legal professional, do not use this tool to produce client-facing legal work.** Read [DISCLAIMER.md](DISCLAIMER.md) before installation.

**Version:** 0.1.1 · **License:** MIT · **Publisher:** [wolfgang_rush](https://github.com/Wolfgangrush) — an Indian advocate (High Courts of India, India). NOT admitted in any EU Member State. This is a software publication for EU-admitted lawyers. · **Engine:** Built on a local memory architecture

> ⚖️ **EU AI Act positioning:** This Software is classified as **LIMITED RISK under Article 50** (transparency obligation only). It is NOT classified as HIGH RISK under Annex III §8 — it is positioned exclusively for qualified lawyers in their private capacity, NOT for judicial authorities in adjudicative use. See [EU_AI_ACT_COMPLIANCE.md](EU_AI_ACT_COMPLIANCE.md).

> ⚠️ **AI can make mistakes. Always verify the output.**
>
> This software generates assistive drafts and suggestions only. Every legal claim, citation, statute reference, procedural step, deadline calculation, and ground of relief must be independently verified by a qualified human practitioner before filing, advising a client, or relying on the output. The publisher accepts no liability for outputs used without verification.

> 🛡️ **Privacy primitive: PII pseudonymisation** via [pseudonymisation-gateway](https://github.com/Wolfgangrush/pseudonymisation-gateway) (wolfgang_rush · MIT). This firm uses the `eu` jurisdiction module + Indian-diaspora overlay for cross-jurisdiction PII coverage. Open-source · zero runtime deps · session-scoped · in-memory only · never writes PII to disk.


> 🛡️ **Pseudonymisation coverage (v0.1.1):** The privacy gateway pseudonymises PII before any cloud-API call; any residue the scanner can't fully resolve is surfaced to you and audit-logged — you retain the final call (v0.3 honest-disclosure). Covers EU-native identifiers (IBAN across 27 member states · EU VAT · EORI · German Steuer-ID · French INSEE · Italian Codice Fiscale · CJEU case numbers · EUR amounts) and Indian-diaspora identifiers (Aadhaar · PAN · GSTIN · IFSC · Indian phone — Europe has substantial South Asian diaspora). Generic patterns (email · names with honorifics · dates) work cross-jurisdiction. Per-member-state national-ID variants (27 countries) will expand in v0.2.

> **🧠 AI Brain that LEARNS.** Every session makes the next one smarter. Two built-in Claude Code skills power this: `/retrospective` saves what the firm learned at session end — every jurisdiction, statute, argument pattern, and procedural rule you touched is logged so the firm's knowledge compounds. `/wake` loads that accumulated context the next time you start, so you never begin from zero. The firm is your second brain, and it gets sharper with every case.

---

## 🌐 Choose your language

13 EU language guides shipped (English authoritative, others AI-assisted with native-PR welcome):

| Script | Language | Member States | Guide |
|---|---|---|---|
| 🇬🇧 | **English** | Ireland · Malta · cross-border default | [GETTING_STARTED.md](GETTING_STARTED.md) |
| 🇩🇪 | **Deutsch (German)** | DE · AT · LU · BE-East | [GETTING_STARTED_GERMAN.md](GETTING_STARTED_GERMAN.md) |
| 🇫🇷 | **Français (French)** | FR · BE-West · LU · cross-border | [GETTING_STARTED_FRENCH.md](GETTING_STARTED_FRENCH.md) |
| 🇪🇸 | **Español (Spanish)** | ES · cross-border | [GETTING_STARTED_SPANISH.md](GETTING_STARTED_SPANISH.md) |
| 🇮🇹 | **Italiano (Italian)** | IT · SM · cross-border | [GETTING_STARTED_ITALIAN.md](GETTING_STARTED_ITALIAN.md) |
| 🇵🇹 | **Português (Portuguese)** | PT · cross-border | [GETTING_STARTED_PORTUGUESE.md](GETTING_STARTED_PORTUGUESE.md) |
| 🇳🇱 | **Nederlands (Dutch)** | NL · BE-Flanders · cross-border | [GETTING_STARTED_DUTCH.md](GETTING_STARTED_DUTCH.md) |
| 🇵🇱 | **Polski (Polish)** | PL · cross-border | [GETTING_STARTED_POLISH.md](GETTING_STARTED_POLISH.md) |
| 🇨🇿 | **Čeština (Czech)** | CZ · cross-border | [GETTING_STARTED_CZECH.md](GETTING_STARTED_CZECH.md) |
| 🇸🇪 | **Svenska (Swedish)** | SE · FI-Swedish · cross-border | [GETTING_STARTED_SWEDISH.md](GETTING_STARTED_SWEDISH.md) |
| 🇬🇷 | **Ελληνικά (Greek)** | GR · CY · cross-border | [GETTING_STARTED_GREEK.md](GETTING_STARTED_GREEK.md) |
| 🇷🇴 | **Română (Romanian)** | RO · cross-border | [GETTING_STARTED_ROMANIAN.md](GETTING_STARTED_ROMANIAN.md) |
| 🌍 | **العربية (Arabic)** | Cross-border (Gulf-EU bridges) | [GETTING_STARTED_ARABIC.md](GETTING_STARTED_ARABIC.md) — RTL |

> 🙏 **Honest note:** 12 of these guides were AI-assisted. **Native-speaker PRs warmly welcome** via [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md).

---

## 💛 Why this exists

> The EU solo legal market faces structural pressures unique to the bloc:
> - **EU AI Act Annex III HIGH RISK enforcement begins 2 August 2026** — cascades onto any AI tool used in justice administration (a proposed Digital Omnibus delay to Dec 2027 is NOT adopted as of plan date · treat 2 Aug 2026 as binding)
> - **Post-Schrems II** — every US-routed data transfer requires supplementary safeguards under GDPR Chapter V; cloud AI for client matters is a compliance landmine UNLESS you (a) use the Local Ollama tier — no cross-border transfer occurs, Schrems II is moot — OR (b) rely on the Pseudonymisation Gateway to sanitise PII before transmission AND independently execute Chapter V Article 46 supplementary safeguards with your cloud vendor
> - **CCBE Code of Conduct + 27 national bar codes** — multi-jurisdictional practitioners must navigate cross-border conflict-of-interest, confidentiality, and advertising rules
> - **Volatile regulatory stack** — Data Act 2025 · NIS2 transposition · eIDAS 2.0 · MiCA · ongoing DSA/DMA enforcement
> - **Solo + small-firm practitioners dominate** the EU market by headcount but have least access to legal-tech infrastructure

The Big Four professional services firms have AI procurement teams. Solo lawyers don't. We built this so an EU solo practitioner — whether avocate in Paris or advokat in Stockholm — can have a second brain that costs **€0 forever**, runs locally by default (Ollama + Qwen3 / Mistral), and supports GDPR Article 5(1)(f) integrity-and-confidentiality + the AI Act at the architecture layer — either by absence of transmission (local mode) or by Pseudonymisation Gateway sanitisation (cloud mode, with Chapter V Article 46 supplementary safeguards remaining YOUR responsibility).

---

## 🧠 What's inside — specialists who live in your terminal

| # | Specialist | What they do for you |
|---|---|---|
| 🧠 | **The Receptionist (brain)** | Listens to what you say. Figures out who you need. Calls the right specialist. You never memorize commands. |
| 📂 | **The Matter Manager** | Holds every active matter — parties, prayers, hearings, orders, draft state. Walk into court · context comes back instantly. |
| 📜 | **The Citation Clerk** | Parses EU citations — ECLI format (`ECLI:EU:C:2024:101`) · CJEU C-cases (`C-123/22`) · national court formats per Member State. |
| 🏛️ | **The Court Registrar** | Knows the EU court hierarchy: CJEU (Court of Justice + General Court) · ECtHR (Strasbourg) · plus national supreme courts and constitutional courts per Member State. |
| ✍️ | **The Drafting Assistant** | Ships with **56 EU drafting templates** (in [`_drafting_data/`](_drafting_data/)) covering: EU regulatory compliance (GDPR · AI Act · Data Act · DSA · DMA · NIS2 · ePrivacy · CRA · MiCA · DORA) · CJEU / General Court litigation (annulment Art 263 · failure-to-act Art 265 · appeal Art 256 · intervention · interim measures Art 279 · EAPO Reg 655/2014 · defence + reply · evidence + Damages Directive disclosure) · cross-border enforcement (Brussels Ia · EEO Reg 805/2004 · EOP Reg 1896/2006 · Small Claims Reg 861/2007) · skeleton arguments (CJEU + ECHR) · cross-border counsel instructions (CCBE Code) · ADR (Mediation Directive 2008/52/EC + Singapore Convention) · EU insolvency (Reg 2015/848 main + secondary) · EUIPO Boards of Appeal · commercial backbone (Commercial Agents Directive 86/653 · VBER 2022/720 franchise + distribution · TTBER 316/2014 · Public Procurement Directive 2014/24 · DGA 2022/868). Optionally connects to the wolfgang_rush drafting plugin family (separate, MIT) for additional drafting flows. |
| 🛡️ | **The Compliance Officer** | Watches your published material for **CCBE Code of Conduct** + per-Member-State bar advertising firewall risks. Flags **GDPR** data-handling gaps · **Chapter V international transfer** issues · **AI Act Article 50** transparency obligations · **NIS2** cybersecurity baselines. |
| 📅 | **The Calendar Sync** | ICS feed sync to iPhone Calendar / Google Calendar / Outlook — no third-party API, no data processor. code-aliased summary line (lock-screen safe) · full matter detail in event body. Timezone Europe/Brussels default (configurable per Member State, DST-aware). |

---

## 🚀 Install in 30 minutes

### Step 1 — Pick your operating system

| OS | Guide |
|---|---|
| 🍎 **Mac** | Standard Python install (Terminal) |
| 🪟 **Windows** | PowerShell · standard pip install |
| 🐧 **Linux** | Same commands as Mac |

### Step 2 — Install Python (one-time) + the tool

```bash
pip install git+https://github.com/Wolfgangrush/ai-law-firm-eu.git
```

### Step 3 — Connect an AI brain (ONE COMMAND)

```bash
ailawfirm-eu connect-local
```

This single command:
1. Detects if Ollama is installed; if not, prints platform-specific install instructions
2. Detects your laptop's RAM
3. Recommends and downloads the right Qwen3 model (14b for 16GB+ · 7b for 8GB · 1.7b for older laptops · Mistral 7b also available as European-developed alternative)
4. Writes config so all subsequent calls route to local Ollama
5. Runs a smoke test to confirm local connectivity

After this, **no queries leave your laptop**.

Three honest model options — see [MODEL_SETUP.md](MODEL_SETUP.md):

| Choice | Cost | Privacy | Best for |
|---|---|---|---|
| 🥇 **Local Ollama + Qwen3 / Mistral** | €0 forever | 🟢 Perfect — nothing leaves your laptop · Schrems II moot (no cross-border transfer occurs) | **Client matters · GDPR Article 9 special categories · professional secrecy · Schrems-II-sensitive data · use this tier when zero cross-border data flow is required** |
| 🥈 **DeepSeek API** | ~€2-5/mo | ⚠️ Pseudonymisation Gateway sanitises EU national-ID/IBAN/case-references + names before transmission, BUT China is NOT on EU Commission adequacy list (Art 45 GDPR); Chapter V Article 46 supplementary safeguards still needed for the pseudonymised transmission | Non-client work · public-law research · templates |
| 🥉 **Claude / Gemini API** | ~€25-70/mo | 🟢 Strong (enterprise privacy default-ON) — Gateway sanitises before transmission | Heavy daily users with executed Article 28 DPA + Schrems-II supplementary measures (SCCs + TIA + technical/organisational measures per EDPB Recommendation 01/2020) + EDPB guidance compliance. Gateway sanitisation supports your Transfer Impact Assessment but does NOT discharge it. |

### Step 4 — Run

```bash
ailawfirm-eu
```

Sample commands:

```
> tell me about the CJEU preliminary reference procedure (Article 267 TFEU)
> validate ECLI:EU:C:2024:101
> check this advert: "Top GDPR specialist in Frankfurt"
> what's the limitation under the German BGB §195?
> add CJEU hearing C-456/24 Luxembourg 2026-06-09 10:00 CEST
> sync calendar
```

---

## 🔒 Privacy & Data Handling — what stays where

**Architecture — three pieces decide your privacy posture:**

**(1) Local-only state.** Your matters, drafts, audit logs, calendar entries, and configuration live in `~/.ailawfirm_eu/`. Never uploaded by the tool. Never synced to a third-party cloud by the tool. No telemetry. No "anonymous usage statistics." The publisher operates zero infrastructure and cannot access this folder. Verifiable via `grep -ri "telemetry\|analytics\|requests.post\|urlopen" ailawfirm_eu/` — should return only user-initiated cloud-LLM calls.

**(2) LLM backend — you choose.** The default `connect-local` command configures Ollama + Qwen3 (or Mistral as European-developed alternative) to run the language model on your laptop (truly nothing leaves; Schrems II is moot in this configuration because no cross-border transfer occurs). If you opt into a cloud-LLM tier (DeepSeek / Claude / Gemini) for quality reasons, see the tier table above for cost + privacy trade-offs.

**(3) Pseudonymisation Gateway — always-on for cloud mode.** When you configure a cloud-LLM provider in `~/.ailawfirm_eu/config.json`, the internalised `PseudonymisationGateway` (source: `ailawfirm_eu/pseudonymisation.py`) automatically substitutes real names, government IDs (IBAN across 27 Member States · EU VAT · EORI · German Steuer-ID · French INSEE · Italian Codice Fiscale · Aadhaar for Indian-diaspora matters), contact identifiers (phone · email), and case references (CJEU C-numbers · ECLI · national court formats) with deterministic placeholders BEFORE the prompt leaves your machine. The placeholder ↔ original map lives in memory only (never written to disk; destroyed when the gateway goes out of scope). Cloud vendors see only the abstract structure of the matter; the user sees real values restored in the response.

**⚠️ Schrems II in cloud mode.** US-based cloud providers (Anthropic · OpenAI · Google) trigger GDPR Chapter V Article 44 + 46. Gateway sanitisation **reduces** Schrems II exposure (because what crosses the border is structurally pseudonymised — supports your Transfer Impact Assessment) but does **not eliminate** it. You must independently execute:
- Standard Contractual Clauses (Module 2 for controller-to-processor transfers)
- Transfer Impact Assessment per EDPB Recommendation 01/2020
- Supplementary technical and organisational measures (Gateway sanitisation counts toward the "technical" prong but the assessment is yours)
- Article 28 GDPR Data Processing Agreement with the vendor
- AI Act Article 50 transparency obligation if the AI output is used for client-facing decisions

**GDPR Article 9 special categories** (health data · biometric data · data revealing racial/ethnic origin · political opinions · religious beliefs · trade-union membership · genetic data · data concerning sex life or sexual orientation · criminal convictions/offences) require either (a) the Local Ollama tier OR (b) cloud mode with explicit Article 9(2) lawful basis + Gateway sanitisation + executed Article 28 DPA + Chapter V safeguards. The Compliance Officer agent flags Article 9 keywords automatically.

The wedge: every other cloud-AI legal tool sends raw client PII to the LLM by default. wolfgang_rush AI Brain — EU ships Ollama-first AND ships the Gateway as the privacy primitive that closes the gap when you choose cloud mode — while remaining honest that Schrems II / Article 28 / Article 9 obligations remain yours to execute.

### What goes to the API provider during each query

Each time the firm reasons about a matter, the following are sent to your chosen API provider:
- Your prompt (the question or instruction)
- Relevant context the firm pulls from your local matter folder (current draft state, recent orders, citations being verified)

Your full matter history, audit logs, and unrelated cases are NOT sent. The firm sends the minimum context needed to answer the current question.

### What API providers contractually guarantee

| Provider | Trains on your data? | Retention | Source |
|---|---|---|---|
| **Claude API** (Anthropic) | ❌ No — Commercial Services data is not used for training | ~30 days for safety/abuse review (Zero Data Retention available on enterprise contract) | [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy) · [Commercial Terms](https://www.anthropic.com/legal/commercial-terms) |
| **OpenAI API** (GPT-4) | ❌ No — API data not used for training since March 2023 | ~30 days for abuse review (ZDR available) | [OpenAI API Data Usage Policies](https://openai.com/policies/api-data-usage-policies) |
| **Gemini API (paid via Vertex AI)** | ❌ No — paid-tier API data not used for training | Per Google Cloud contract | [Vertex AI data governance](https://cloud.google.com/vertex-ai/docs/general/data-governance) |
| **Gemini Free Tier** | ⚠️ **YES — Google AI uses free-tier prompts to improve products** | — | [Google AI Studio terms](https://ai.google.dev/gemini-api/terms) — **DO NOT use free-tier Gemini for confidential client matters.** |
| **DeepSeek V4 Pro API** | ❌ No — per DeepSeek API terms, inputs/outputs not used for model training | Retention policy less documented than OpenAI/Anthropic; verify for matter sensitivity | [DeepSeek API ToS](https://platform.deepseek.com/api-docs/legal) · **Note:** provider is China-based; consider jurisdictional data-residency requirements |

### What that does NOT mean — solicitor's residual risk

Even though API data is not used for training:

1. **Data IS in transit** during each query — it passes through the provider's infrastructure
2. **Brief logging retention** (typically 30 days) means the provider holds the data for that window
3. **Lawful access requests** — a subpoena, lawful intercept warrant, GDPR data-subject access request, or provider security incident could expose data during the retention window
4. **Provider-side breach risk** — however small, it exists

This is fundamentally different from local-LLM mode (where no data leaves your machine, ever, period). The `connect-local` command already configures Ollama + Qwen3 as the v0.1 default — lawyers handling confidential, privileged, or special-category data should stay in local-LLM mode for that work. The cloud-LLM tier exists for non-confidential research, public-law analysis, and template scaffolding where contractual no-training is a sufficient safeguard.

### Solicitor's decision

If your matter is:
- **General commercial / corporate / contract drafting** → Claude / OpenAI / paid Gemini API are appropriate. Contractual no-training protections are strong. Audit logs are local.
- **Legal-privileged client communication / privileged litigation strategy** → Evaluate against your jurisdiction's professional conduct rules. Most regulators permit reasoned use of cloud-AI with disclosure to the client. (See Member-state Bars per EU avocat rules guidance.) Document the choice in your audit log.
- **GDPR special-category data / health / criminal record / political opinion** → Stay in `connect-local` (Ollama + Qwen3) mode. Do not opt into any cloud-LLM tier for these matters; do not use free-tier Gemini.
- **State secrets / classified material / under-seal court orders** → Stay in `connect-local` (Ollama + Qwen3) mode. For physically air-gapped networks where the pip-install / model-download / auto-update paths are also prohibited, await the v0.3+ signed offline-install bundle below.

The firm's audit log captures every API call (timestamp, agent, prompt-summary, output-summary) at `~/.ailawfirm_eu/audit_logs/`. Logs never leave your machine. They are your professional-conduct compliance trail.

### v0.3+ roadmap

> What v0.1 already ships: (a) local-LLM default via `connect-local` (Ollama + Qwen3 — nothing leaves your laptop in local mode), (b) configurable cloud-LLM tier covering Claude / OpenAI / paid Gemini / DeepSeek, (c) Pseudonymisation Gateway sanitising PII before any cloud-LLM call, and (d) no first-party telemetry. The items below extend the floor — they are not a future replacement for what is already shipped.

- **Signed offline-install bundle** — the `pip install` path currently touches PyPI and the Ollama model registry; v0.3+ ships a signed offline-installable archive with the Qwen3 model pre-bundled, removing the last network-touch point even at install time. For lawyers on physically air-gapped networks (sealed-court matter rooms, defence-and-security mandates).
- **In-firm LLM tenant adapter** — drop-in config for Azure OpenAI / private Vertex / on-prem vLLM endpoints. Distinct from the today-shipped public-API cloud-LLM tier; targets lawyers whose firm already provisions LLM infrastructure under its own GDPR Art 28 DPA.
- **Expanded local-model surface** — Llama 3.3 70B / Qwen 2.5 72B / DeepSeek V4 Pro (open-weights via Ollama), for lawyers with larger laptops who want better-than-Qwen3-14b local reasoning.

Tracked at: [drafting-agents-core issues](https://github.com/Wolfgangrush/drafting-agents-core/issues).

---

**No agenda · no telemetry · no cloud-default · MIT licensed · €0 forever.**

**Member-state Bars per EU avocat rules compliance built into the tool's audit + transparency-gate architecture.** Solicitor remains professionally responsible for every output. The firm is a force-multiplier, not a substitute for judgment.

---

## 📁 Where your data lives

```
~/.ailawfirm-eu/                     ← Mac/Linux
C:\Users\YourName\.ailawfirm-eu\     ← Windows
├── palace/                          ← all matter/client/citation memory (ChromaDB)
├── config.json                      ← your settings (AI provider · Member State · timezone · prefs)
├── calendars/                       ← generated .ics feeds for iPhone/Outlook subscribe
└── people_map.json                  ← optional client alias system (lock-screen safety)
```

Copy this folder to a USB drive · OneDrive · iCloud Drive · Dropbox = complete backup of your practice in 5 seconds.

---

## 🔄 How to update your firm

When a new version of AI Brain — EU is published, you pull it in with **one command**. Your matter data + your project-root `CLAUDE.md` are **never touched** — only the firm's installed code, skills, and prompts refresh.

### Path 1 — Plain terminal

```
ailawfirm-eu update
```

Under the hood this runs `pip install --upgrade git+https://github.com/Wolfgangrush/ai-law-firm-eu.git`. After it finishes, restart any open `ailawfirm-eu` session so the new skills + prompts load.

### Path 2 — Inside Claude Code

Type:

```
/update
```

Claude runs the same command for you and reports the result.

### Path 3 — Inside Gemini CLI

Type:

```
/update
```

Same outcome — Gemini calls `ailawfirm-eu update` for you.

### When to update

- **The publisher tells you** a new version is out → update.
- **Monthly hygiene** → update once a month so you stay current on skills + bug fixes.
- **After hitting a bug** → first thing to try is updating, in case it is already fixed upstream.

### What does NOT update (by design)

- Your matter folders (`~/Desktop/<your-firm>/<matter>/...`)
- Your project-root `CLAUDE.md` (your customisations always win)
- Your `~/.ailawfirm-eu/` config + palace data
- Your chosen AI model setup (Ollama · DeepSeek · Claude · Gemini)

Only the firm's installed Python code, skills, and template files refresh. Your practice is unaffected.

### One catch — existing users + new template rules

If a new version updates the template `CLAUDE.md` (the firm's standing rules), your project-root `CLAUDE.md` is preserved because your customisations always win. To see what changed in the template after an update:

```
diff CLAUDE.md "$(python3 -c 'import ailawfirm_eu, os; print(os.path.join(os.path.dirname(ailawfirm_eu.__file__), "templates/CLAUDE.md"))')"
```

Review the diff and merge what you want into your own `CLAUDE.md`.

---

## 🛤️ Roadmap (honest)

> 🙏 **Honest note on timelines:** Solo-author OSS · ships as time permits · v0.2 / v0.3 / v0.4+ targets are indicative, not committed dates. Open an issue if a specific feature on a specific timeline matters to your work.



- **v0.1.0** *(shipped)* — bootstrap: architecture, brain layer, 7 specialist agents (4 live · 3 stubs), 3 working MCP tools (court · citation · calendar), 13-language onboarding, connect-local one-command CLI, EU AI Act Article 50 LIMITED RISK positioning, LEGAL_EXPOSURE_PLAYBOOK v0.1 compliance
- **v0.2 — knowledge layer** *(shipped 2026-05-28)* — Statute corpus: 11 Tier-1 EU instruments (GDPR Regulation 2016/679 · AI Act Regulation 2024/1689 · DSA · DMA · Data Act Regulation 2023/2854 · NIS2 Directive · ePrivacy Directive 2002/58/EC · CRA · MiCA · DORA · Brussels Ia Recast). Drafting corpus: **56 templates** covering (a) EU regulatory compliance — 10 templates (GDPR DPA · DPIA · ROPA · BCRs · AI Act conformity + FRIA · DSA SoR · NIS2 incident · CRA conformity · privacy policy · SCCs); (b) CJEU / General Court litigation — 10 templates (Art 263 annulment · Art 265 failure-to-act · Art 256 appeal · intervention · interim measures · EAPO · defence + reply · measures of inquiry · Damages Directive disclosure · preliminary reference · DMA challenge); (c) cross-border enforcement — 5 instruments (Brussels Ia certificate + Arts 39-44 · EEO Reg 805/2004 · EOP Reg 1896/2006 · Small Claims Reg 861/2007); (d) skeletons + counsel briefing — 3 templates (CJEU direct action · ECHR · CCBE cross-border instructions); (e) ADR — 3 templates (Mediation Directive 2008/52/EC position statement + settlement enforceability + consumer ADR/post-ODR framework); (f) EU insolvency — 2 templates (main + secondary proceedings under Reg 2015/848); (g) EUIPO Boards of Appeal practice; (h) EU commercial backbone — 9 templates (Commercial Agents 86/653 · Franchise VBER · Distribution VBER · TTBER 316/2014 · Data Act SaaS · DGA data sharing · Public Procurement 2014/24 · MiCA CASP · DORA ICT provider); (i) IP + competition forms (EUIPO opposition/cancellation/application · competition complaint · ECHR Art 34 application · SAR statutory notice). Pseudonymisation Gateway for safe cloud-mode shipped at v0.1.1.
- **v0.2 — frontend / UX layer** *(in progress)* — CJEU citation deep-parse · matter dashboard · per-Member-State limitation periods · expanded per-Member-State national-ID variants
- **v0.3** *(following milestone)* — **firm mode** for multi-lawyer EU practices (Establishment Directive cross-border practice support) · role/permission · matter assignment · conflict-check across Member States · CCBE Code compliance dashboard
- **v0.4+** — EUR-Lex / CJEU Court website cross-reference · per-Member-State bar codes (top 10 by practitioner count) · Apple EventKit native · CalDAV bidirectional sync · ECtHR cross-reference for human-rights matters · ECB Administrative Board of Review + EPO Boards of Appeal templates · sector Data Spaces (Health · Mobility · Financial) once Regulations finalised · AI Act technical Annexes once CEN/CENELEC standards adopted · anti-suit / anti-arbitration injunction specialist note

Six sister jurisdictions on the same architecture: 🇮🇳 India · 🇸🇬 Singapore · 🇬🇧 UK · 🇦🇺 Australia · 🇦🇪 Dubai-DIFC · 🇺🇸 USA — each as its own MIT-licensed repo.

---

## 🌐 Family Status (honest · cross-firm)

The wolfgang_rush AI Brain family ships across 7 jurisdictions. Honest status of the v0.2 legal-knowledge layer (statute corpus + drafting data) per firm:

| Firm | Statute corpus | Drafting corpus | Shared agents | GitHub |
|------|---|---|---|---|
| 🇮🇳 **India** | Native knowledge base · maintainer-curated | wolfgang_rush plugins (14 Indian-litigation plugins · separate stack) | Not applicable — Indian-specific | ✅ LIVE |
| 🇪🇺 **EU** | ✅ 11 statutes · 8/8 Tier-1 | ✅ **56 templates** · litigation + commercial complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇦🇺 **Australia** | ✅ 13 Tier-1 statute digests + 39 research files | ✅ **79 templates** · litigation + commercial + tribunal complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇦🇪 **Dubai-DIFC** | ✅ 24 statute digests · dual-track (15 DIFC + 9 Mainland UAE Federal) · v0.2 closed 2026-05-29 | ✅ **81 templates** · dual-track DIFC + Mainland · litigation + commercial + tribunal complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇸🇬 **Singapore** | ✅ 17 statute digests Tier-1 | ✅ **55 templates + 6 scaffolds** · litigation + commercial + regulatory complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇬🇧 **UK** | ✅ 10 statute digests Tier-1 | ✅ **107 templates** · litigation + commercial + Tier-3 specialist + procedural anchors complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇺🇸 **USA** | ✅ 23 federal-first Tier-1 statute digests | ✅ **89 templates** · all 13 litigation categories + commercial + corporate complete (v0.2 closed 2026-05-29) | ✅ Migrated | ✅ LIVE |

**Plus:**
- **AI Startup Firm — India v0.1** (legal-ops brain for founders)
- **GC In-House Brain** (multi-jurisdictional, 8 modules — 3 live · 5 shipping v0.2+)

Both share the same `drafting-agents-core` architecture pattern.

All firms migrated to the central [drafting-agents-core](https://github.com/Wolfgangrush/drafting-agents-core) agent library on 2026-05-20 (Path B-Lite) — single source of truth for the agent layer; jurisdictional knowledge stays per-firm.

---

## 📚 Documentation

| File | What it covers |
|---|---|
| [GETTING_STARTED.md](GETTING_STARTED.md) + 12 language variants | Layman-friendly 30-minute tour |
| [DISCLAIMER.md](DISCLAIMER.md) | Full legal disclaimer · CCBE + per-Member-State bar conduct positioning · GDPR · EU AI Act Article 50 · cross-border |
| [NO_PII_NO_DATA.md](NO_PII_NO_DATA.md) | Zero-collection architecture · GDPR controller/processor analysis · Chapter V Schrems-II considerations |
| [EU_AI_ACT_COMPLIANCE.md](EU_AI_ACT_COMPLIANCE.md) | Article 50 LIMITED RISK classification · Annex III §8 exclusion · enforcement timeline · GPAI provider considerations |
| [SECURITY.md](SECURITY.md) | Vulnerability reporting · coordinated disclosure · NIS2 alignment notes |
| [MODEL_SETUP.md](MODEL_SETUP.md) | Honest privacy table · local vs cloud · Schrems-II analysis · third-party CLI tool warning |
| [SCOPE.md](SCOPE.md) | What's in v0.1, what's not |
| [KNOWLEDGE_PROVENANCE.md](KNOWLEDGE_PROVENANCE.md) | Every domain claim's source (CITED:<research-file>) |
| [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) | Community call for native-speaker translation PRs (12 EU languages welcomed) |

---

## 🙏 Credits

- **Engine — all architectural credit:** a local memory architecture — the highest-scoring open-source AI memory system ever benchmarked. MIT licensed. We are a downstream fork specialized for EU solo practice.
- **Publisher:** [wolfgang_rush](https://github.com/Wolfgangrush) — an Indian advocate (High Courts of India, India). MIT-licensed legal-tech publisher.
- **Inspired by:** every EU solo lawyer who's worked Sunday night on a CJEU preliminary reference or a national-court filing the Monday before vacation.

---

## ⚠️ Disclaimer

This tool helps you organize your practice. It does **NOT** give legal advice. It does **NOT** replace your professional judgment. It does **NOT** solicit work on your behalf. CCBE Code + per-Member-State bar advertising firewalls are built in but **YOU** remain responsible for compliance with all national bar conduct rules, GDPR, AI Act, sectoral regulations, and any CCBE / EDPB guidance.

The publisher is not admitted in any EU Member State. The publisher does not offer legal services in the EU. This is a software publication under the MIT License.

Ships AS-IS without warranty. See [LICENSE](LICENSE).

---

## 📞 Support

- **Issues / bugs:** https://github.com/Wolfgangrush/ai-law-firm-eu/issues
- **Translation help:** [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) (12 EU languages welcomed)
- **Member-State-specific feature?** Open an issue with `[ms-DE]` / `[ms-FR]` / etc. label
- **CJEU / cross-border feature?** Open an issue with `[cross-border]` label

---

`Let's begin. Fangen wir an. Commençons. Empecemos. Cominciamo. Vamos começar. Laten we beginnen. Zacznijmy. Začněme. Låt oss börja. Ας ξεκινήσουμε. Să începem. لنبدأ.` 🙏
