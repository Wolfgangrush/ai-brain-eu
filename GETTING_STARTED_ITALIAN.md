# Avvio — AI Brain for EU Lawyers · v0.1

**🙏 Benvenuto, avvocato — la sua AI Brain inizia qui.**

## Cos'è?

AI Brain EU è un **assistente di gestione dello studio legale** per avvocati indipendenti dell'UE. Funziona interamente sulla sua macchina — niente cloud, niente chiave API, niente telemetria. I suoi fascicoli non lasciano mai il suo computer.

## Installazione (30 secondi)

```bash
cd ~/Desktop
git clone https://github.com/Wolfgangrush/ai-law-firm-eu.git
cd ai-law-firm-eu
pip install -e .
```

## Avvi il suo studio (2 minuti)

```bash
mkdir ~/mio-studio-eu
ailawfirm-eu init ~/mio-studio-eu
ailawfirm-eu mine ~/mio-studio-eu
ailawfirm-eu search "Bruxelles I-bis esecuzione"
```

## 7 agenti specialistici

| Agent | Funzione |
|---|---|
| `matter_agent` | Gestione dei fascicoli |
| `citation_agent` | Validazione citazioni ECLI / CELEX |
| `court_agent` | Informazioni sui tribunali (CGUE, nazionali) |
| `drafting_agent` | Assistenza alla redazione (consapevole della procedura UE) |
| `deadline_agent` | Verifica termini di prescrizione |
| `calendar_agent` | Sincronizzazione calendario ICS (fuso Europa/Bruxelles) |
| `compliance_agent` | AI Act Allegato III + GDPR + Antiriciclaggio + CCBE |

## ⚠️ Avviso AI Act

Il **Regolamento europeo sull'IA (2024/1689)** classifica i sistemi di IA utilizzati « nell'amministrazione della giustizia » come **ALTO RISCHIO** (Allegato III, punto 8). Questo strumento è un software di gestione dello studio (Rischio Minimo). NON effettua ragionamento giudiziario né previsione di decisioni.

## Privacy

Tutto è locale. Conforme al GDPR per progettazione. Nessun dato lascia la sua macchina.

## Crediti

the local memory layer di milla-jovovich (MIT) · 35 fonti giuridiche UE · wolfgang_rush, 2026 — Licenza MIT

---

🙏 Benvenuto · Welcome · Willkommen · Bienvenido · Bienvenue · Welkom · Witaj · Välkommen · Bem-vindo · Vítejte · Καλώς ήρθατε · Bun venit · أهلاً وسهلاً
