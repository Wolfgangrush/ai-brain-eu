# Erste Schritte — AI Brain for EU Lawyers · v0.1

**🙏 Willkommen, Frau/Herr Rechtsanwältin/Rechtsanwalt — Ihre AI Brain beginnt hier.**

## Was ist das?

AI Brain EU ist ein **gedächtnisbasierter Kanzleimanagement-Assistent** für EU-Einzelanwälte. Alles läuft lokal auf Ihrem Rechner — keine Cloud, kein API-Key, keine Telemetrie. Ihre Mandantenakten verlassen niemals Ihren Computer.

## Installation (30 Sekunden)

```bash
cd ~/Desktop
git clone https://github.com/Wolfgangrush/ai-law-firm-eu.git
cd ai-law-firm-eu
pip install -e .
```

## Richten Sie Ihre Kanzlei ein (2 Minuten)

```bash
mkdir ~/meine-eu-kanzlei
ailawfirm-eu init ~/meine-eu-kanzlei
ailawfirm-eu mine ~/meine-eu-kanzlei
ailawfirm-eu search "Brüssel I-bis Vollstreckung"
```

## 7 Fachagenten

| Agent | Funktion |
|---|---|
| `matter_agent` | Aktenverfolgung |
| `citation_agent` | ECLI-/CELEX-Zitierprüfung |
| `court_agent` | Gerichtsinformationen (CJEU, BGH, nationale Gerichte) |
| `drafting_agent` | Schriftsatzassistenz (EU-Verfahren) |
| `deadline_agent` | Fristen- und Verjährungsprüfung |
| `calendar_agent` | Kalender-Sync (ICS, Zeitzone Europa/Brüssel) |
| `compliance_agent` | KI-Verordnung Anhang III + DSGVO + Geldwäsche + CCBE |

## ⚠️ KI-Verordnung Hinweis

Die **EU-KI-Verordnung (2024/1689)** stuft KI-Systeme in der „Rechtspflege" als **HOCHRISIKO** ein (Anhang III, Nr. 8). Dieses Tool ist Kanzleimanagement-Software (Minimales Risiko). Es führt KEINE richterliche Entscheidungsfindung durch.

## Datenschutz

Alles lokal. DSGVO-konform by design. Keine Daten verlassen Ihren Rechner.

## Credits

the local memory layer von milla-jovovich (MIT) · 35 EU-Rechtsquellen · wolfgang_rush, 2026 — MIT-Lizenz

---

🙏 Willkommen · Welcome · Bienvenue · Bienvenido · Benvenuto · Welkom · Witaj · Välkommen · Bem-vindo · Vítejte · Καλώς ήρθατε · Bun venit · أهلاً وسهلاً
