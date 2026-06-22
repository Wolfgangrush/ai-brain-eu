# Komma igång — AI Brain for EU Lawyers · v0.1

**🙏 Välkommen, advokat — din AI Brain börjar här.**

## Vad är det?

AI Brain EU är en **minnesbaserad assistent för byråhantering** för oberoende EU-advokater. Den körs helt på din maskin — inget moln, ingen API-nyckel, ingen telemetri. Dina ärendeakter lämnar aldrig din dator.

## Installation (30 sekunder)

```bash
cd ~/Desktop
git clone https://github.com/Wolfgangrush/ai-law-firm-eu.git
cd ai-law-firm-eu
pip install -e .
```

## Starta din byrå (2 minuter)

```bash
mkdir ~/min-eu-byra
ailawfirm-eu init ~/min-eu-byra
ailawfirm-eu mine ~/min-eu-byra
ailawfirm-eu search "Bryssel I-bis verkställighet"
```

## 7 specialistagenter

| Agent | Funktion |
|---|---|
| `matter_agent` | Ärendeuppföljning |
| `citation_agent` | Validering av ECLI-/CELEX-citat |
| `court_agent` | Domstolsinformation (EU-domstolen, nationella domstolar) |
| `drafting_agent` | Skrivelseassistans (EU-processmedveten) |
| `deadline_agent` | Preskriptionstidskontroll |
| `calendar_agent` | Kalendersynkronisering ICS (tidszon Europa/Bryssel) |
| `compliance_agent` | AI Act Bilaga III + GDPR + Penningtvätt + CCBE |

## ⚠️ AI Act information

**EU:s AI-förordning (2024/1689)** klassificerar AI-system som används « vid rättskipning » som **HÖG RISK** (Bilaga III, punkt 8). Detta verktyg är programvara för byråhantering (Minimal Risk). Det utför INTE rättsligt resonemang eller beslutsförutsägelser.

## Integritet

Allt är lokalt. GDPR-konformt by design. Inga data lämnar din maskin.

## Krediter

the local memory layer av milla-jovovich (MIT) · 35 EU-rättskällor · wolfgang_rush, 2026 — MIT-licens

---

🙏 Välkommen · Welcome · Willkommen · Bienvenido · Benvenuto · Welkom · Witaj · Bienvenue · Bem-vindo · Vítejte · Καλώς ήρθατε · Bun venit · أهلاً وسهلاً
