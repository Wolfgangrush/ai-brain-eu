# Začínáme — AI Brain for EU Lawyers · v0.1

**🙏 Vítejte, pane/paní advokáte — vaše AI Brain začíná zde.**

## Co to je?

AI Brain EU je **asistent pro správu advokátní kanceláře** pro nezávislé právníky v EU. Funguje zcela na vašem počítači — žádný cloud, žádný API klíč, žádná telemetrie. Vaše spisy nikdy neopouštějí váš počítač.

## Instalace (30 sekund)

```bash
cd ~/Desktop
git clone https://github.com/Wolfgangrush/ai-law-firm-eu.git
cd ai-law-firm-eu
pip install -e .
```

## Spusťte svou kancelář (2 minuty)

```bash
mkdir ~/ma-eu-kancelar
ailawfirm-eu init ~/ma-eu-kancelar
ailawfirm-eu mine ~/ma-eu-kancelar
ailawfirm-eu search "Brusel I-bis výkon"
```

## 7 specializovaných agentů

| Agent | Funkce |
|---|---|
| `matter_agent` | Sledování případů |
| `citation_agent` | Validace citací ECLI / CELEX |
| `court_agent` | Informace o soudech (SDEU, vnitrostátní) |
| `drafting_agent` | Asistence při psaní podání (vědomá řízení EU) |
| `deadline_agent` | Kontrola promlčecích lhůt |
| `calendar_agent` | Synchronizace kalendáře ICS (časové pásmo Evropa/Brusel) |
| `compliance_agent` | AI Act Příloha III + GDPR + AML/CFT + CCBE |

## ⚠️ Upozornění k AI Act

**Nařízení EU o umělé inteligenci (2024/1689)** klasifikuje systémy AI používané „při výkonu spravedlnosti" jako **VYSOCE RIZIKOVÉ** (Příloha III, bod 8). Tento nástroj je software pro správu kanceláře (Minimální riziko). NEPROVÁDÍ soudní rozhodování ani předpovídání rozsudků.

## Soukromí

Vše je lokální. Navrženo v souladu s GDPR. Žádná data neopouštějí váš počítač.

## Poděkování

the local memory layer od milla-jovovich (MIT) · 35 právních zdrojů EU · wolfgang_rush, 2026 — Licence MIT

---

🙏 Vítejte · Welcome · Willkommen · Bienvenido · Benvenuto · Welkom · Witaj · Välkommen · Bem-vindo · Bienvenue · Καλώς ήρθατε · Bun venit · أهلاً وسهلاً
