# 🤖 AI Model Setup — EU · Honest Privacy Guide

The Software stores everything on the user's device. The AI model the user connects determines privacy.

> **For client matters, GDPR Article 9 special categories, professional-secrecy material: use local-only mode (Option A).**

---

## 🎯 The honest privacy table

| Option | Where it runs | Who can see your queries | Cost (EUR/month) | Best for |
|---|---|---|---|---|
| 🥇 **Ollama + Qwen3 (local)** | Your device | ONLY you | €0 forever | **Client matters · GDPR Article 9 · professional secrecy · Schrems-II-sensitive data** |
| 🥈 **DeepSeek API** | DeepSeek servers (China) | DeepSeek (opt-out available) | €2-5 moderate use | NON-client work · public-law research · templates |
| 🥉 **Claude API (Anthropic)** | Anthropic servers (USA) | Anthropic (per policy) | €25-70 | Heavy users with verified Article 28 DPA |
| 🥉 **Gemini API (Google)** | Google servers (globally) | Google | €8-25 | Long-PDF synthesis · with Workspace-tier terms |

---

## 🥇 Option A — Ollama + Qwen3 (local · RECOMMENDED · DEFAULT)

### Why local is the right choice for EU practice

- Model runs ON THE USER'S DEVICE. Queries never leave.
- No GDPR Chapter V international transfer concern.
- No Schrems-II supplementary-measures analysis required.
- No Article 28 processor contract negotiation needed.
- Supports professional-secrecy obligations across EU Member States.
- Compatible with EU AI Act Article 50 transparency (the Software discloses AI use to the user).

### Manual install (v0.1 — one-command bridge ships in v0.2)

**Mac:** `brew install ollama` (or download from https://ollama.com/download/Mac)
**Windows:** Download installer from https://ollama.com/download
**Linux:** `curl -fsSL https://ollama.com/install.sh | sh`

```
ollama pull qwen3:14b
```

Alternative models:
- `ollama pull qwen3:7b` — 4 GB · faster, slightly lower quality
- `ollama pull mistral:7b` — 4 GB · European-developed model (in line with EU AI sovereignty preferences)
- `ollama pull llama3.3:8b` — 5 GB

Edit `~/.ailawfirm-eu/config.json`:

```json
{
  "ai_provider": "ollama",
  "ollama_model": "qwen3:14b",
  "ollama_host": "http://localhost:11434"
}
```

### Hardware reality check

- MacBook Air M1/M2 8GB: works with `qwen3:7b` or `mistral:7b`
- MacBook Air M2/M3/M4 16GB+: smooth with `qwen3:14b`
- Windows / Linux 16GB + dGPU: smooth with `qwen3:14b`
- Older laptops 4-8GB no GPU: `qwen3:7b` or smaller

---

## 🥈 Option B — DeepSeek API (cheap cloud · NOT for client work)

### MANDATORY privacy setup

DeepSeek's default ToS permits use of API inputs for training. **Opt-out required.**

1. https://platform.deepseek.com → Settings → Privacy
2. Toggle OFF "Improve the model for everyone"

Even after opt-out, DeepSeek servers (in China) process queries in transit. China is NOT on the EU Commission's adequacy list under GDPR Article 45. **For client matter data with EU data subjects, do NOT use DeepSeek even with opt-out** — the cross-border transfer would require Article 46 safeguards that are not practical to set up for individual cloud-API use.

---

## 🥉 Option C — Claude API (Anthropic, USA)

Top-tier reasoning. Anthropic does not use API inputs for training (per public policy). USA is on the EU-US Data Privacy Framework adequacy list — but the DPF has been challenged and may be invalidated; verify current status with EUR-Lex / EDPB.

If you use Claude API for EU client data, you must:
- Execute a GDPR Article 28 Data Processing Agreement with Anthropic (Anthropic provides one)
- Consider Schrems-II supplementary measures (encryption · access controls · sub-processor flow-down)
- Document the lawful basis and transfer mechanism in your records of processing
- Update your privacy notice

---

## 🥉 Option D — Gemini API (Google, globally)

Long-PDF synthesis strength. Google's terms vary by tier (paid Workspace tier has better data-isolation than free tier).

If you use Gemini API for EU client data:
- Verify the tier (free vs Workspace vs Vertex AI)
- Execute Google's DPA + ensure SCCs are in place
- Same Schrems-II analysis applies

---

## ⚠️ Third-party CLI tools and IDEs — user assumes all risk

If you integrate the Software with **Claude Code · Claude CLI · Codex CLI · Gemini CLI · OpenCode · Cursor · GitHub Copilot · JetBrains AI · any other AI-assisted IDE or CLI** — you do so **at your own risk** and under the terms of service of that tool.

The publisher:
- Does NOT recommend any specific third-party tool
- Does NOT verify any third-party tool's GDPR / AI Act compliance
- Accepts NO responsibility for the user's choice of third-party tooling
- Accepts NO responsibility for any data leakage, GDPR violation, or professional-conduct violation resulting from such use

The user is solely responsible for GDPR · Article 28 · Chapter V · bar conduct compliance for any third-party AI tool used alongside the Software.

---

## Cloud-mode consent (v0.2 will enforce; principle now)

```
⚠️  CLOUD MODE WARNING

Your queries will leave your device and be processed on [VENDOR]'s servers.

DO NOT use cloud mode for:
  ❌ Confidential client matter data covered by professional secrecy
  ❌ GDPR Article 9 special categories (health · biometric · political · etc.)
  ❌ Cross-border transfers without verified Article 46 safeguards
  ❌ Anything subject to professional privilege

The publisher (wolfgang_rush) is NOT in this data path. You contract directly
with [VENDOR]. You must execute Article 28 DPA. You must address Chapter V.
```

For client matters: stay on Option A (local-only).

---

*References LEGAL_EXPOSURE_PLAYBOOK §2(a) (Local-AI-Only Default pillar), §3.V4 (Data Protection — GDPR + Schrems II). Playbook v0.1.*
