# Aan de slag — AI Brain for EU Lawyers · v0.1

**🙏 Welkom, advocaat — uw AI Brain begint hier.**

## Wat is het?

AI Brain EU is een **geheugengebaseerde assistent voor kantoorbeheer** voor onafhankelijke EU-advocaten. Het draait volledig op uw machine — geen cloud, geen API-sleutel, geen telemetrie. Uw dossiers verlaten nooit uw computer.

## Installatie (30 seconden)

```bash
cd ~/Desktop
git clone https://github.com/Wolfgangrush/ai-law-firm-eu.git
cd ai-law-firm-eu
pip install -e .
```

## Start uw kantoor (2 minuten)

```bash
mkdir ~/mijn-eu-kantoor
ailawfirm-eu init ~/mijn-eu-kantoor
ailawfirm-eu mine ~/mijn-eu-kantoor
ailawfirm-eu search "Brussel I-bis tenuitvoerlegging"
```

## 7 gespecialiseerde agenten

| Agent | Functie |
|---|---|
| `matter_agent` | Dossieropvolging |
| `citation_agent` | Validatie van ECLI-/CELEX-citaten |
| `court_agent` | Rechtbankinformatie (HvJ EU, nationale rechtbanken) |
| `drafting_agent` | Opstelassistentie (EU-procedurebewust) |
| `deadline_agent` | Verjaringstermijncontrole |
| `calendar_agent` | Kalendersynchronisatie ICS (tijdzone Europa/Brussel) |
| `compliance_agent` | AI Act Bijlage III + AVG + Wwft + CCBE |

## ⚠️ AI Act kennisgeving

De **EU AI-verordening (2024/1689)** classificeert AI-systemen die worden gebruikt « in de rechtsbedeling » als **HOOG RISICO** (Bijlage III, punt 8). Deze tool is kantoormanagementsoftware (Minimaal Risico). Het voert GEEN rechterlijke besluitvorming of voorspelling uit.

## Privacy

Alles is lokaal. AVG-conform by design. Geen gegevens verlaten uw machine.

## Credits

the local memory layer door milla-jovovich (MIT) · 35 EU-rechtsbronnen · wolfgang_rush, 2026 — MIT-licentie

---

🙏 Welkom · Welcome · Willkommen · Bienvenido · Benvenuto · Bienvenue · Witaj · Välkommen · Bem-vindo · Vítejte · Καλώς ήρθατε · Bun venit · أهلاً وسهلاً
