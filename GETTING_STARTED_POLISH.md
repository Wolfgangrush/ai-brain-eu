# Pierwsze kroki — AI Brain for EU Lawyers · v0.1

**🙏 Witaj, mecenasie — Twoja AI Brain zaczyna się tutaj.**

## Co to jest?

AI Brain EU to **asystent zarządzania kancelarią prawną** dla niezależnych prawników w UE. Działa w całości na Twoim komputerze — żadnej chmury, żadnego klucza API, żadnej telemetrii. Twoje akta nigdy nie opuszczają Twojego komputera.

## Instalacja (30 sekund)

```bash
cd ~/Desktop
git clone https://github.com/Wolfgangrush/ai-law-firm-eu.git
cd ai-law-firm-eu
pip install -e .
```

## Uruchom swoją kancelarię (2 minuty)

```bash
mkdir ~/moja-kancelaria-eu
ailawfirm-eu init ~/moja-kancelaria-eu
ailawfirm-eu mine ~/moja-kancelaria-eu
ailawfirm-eu search "Bruksela I-bis egzekucja"
```

## 7 agentów specjalistycznych

| Agent | Funkcja |
|---|---|
| `matter_agent` | Śledzenie spraw |
| `citation_agent` | Weryfikacja cytowań ECLI / CELEX |
| `court_agent` | Informacje o sądach (TSUE, krajowe) |
| `drafting_agent` | Pomoc w redagowaniu pism (świadoma procedury UE) |
| `deadline_agent` | Sprawdzanie terminów przedawnienia |
| `calendar_agent` | Synchronizacja kalendarza ICS (strefa Europa/Bruksela) |
| `compliance_agent` | AI Act Załącznik III + RODO + AML/CFT + CCBE |

## ⚠️ Informacja o AI Act

**Rozporządzenie UE w sprawie AI (2024/1689)** klasyfikuje systemy AI używane „w wymiarze sprawiedliwości" jako **WYSOKIEGO RYZYKA** (Załącznik III, pkt 8). To narzędzie jest oprogramowaniem do zarządzania kancelarią (Minimalne Ryzyko). NIE wykonuje rozumowania sądowego ani przewidywania orzeczeń.

## Prywatność

Wszystko lokalnie. Zgodne z RODO z założenia. Żadne dane nie opuszczają Twojego komputera.

## Kredyty

the local memory layer autorstwa milla-jovovich (MIT) · 35 źródeł prawnych UE · wolfgang_rush, 2026 — Licencja MIT

---

🙏 Witaj · Welcome · Willkommen · Bienvenido · Benvenuto · Welkom · Bienvenue · Välkommen · Bem-vindo · Vítejte · Καλώς ήρθατε · Bun venit · أهلاً وسهلاً
