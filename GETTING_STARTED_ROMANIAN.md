# Primii pași — AI Brain for EU Lawyers · v0.1

**🙏 Bun venit, avocate — AI Brain a dumneavoastră începe aici.**

## Ce este?

AI Brain EU este un **asistent de gestionare a cabinetului juridic** pentru avocații independenți din UE. Rulează în întregime pe mașina dumneavoastră — fără cloud, fără cheie API, fără telemetrie. Dosarele dumneavoastră nu părăsesc niciodată computerul dumneavoastră.

## Instalare (30 de secunde)

```bash
cd ~/Desktop
git clone https://github.com/Wolfgangrush/ai-law-firm-eu.git
cd ai-law-firm-eu
pip install -e .
```

## Porniți cabinetul dumneavoastră (2 minute)

```bash
mkdir ~/cabinetul-meu-eu
ailawfirm-eu init ~/cabinetul-meu-eu
ailawfirm-eu mine ~/cabinetul-meu-eu
ailawfirm-eu search "Bruxelles I-bis executare"
```

## 7 agenți specialiști

| Agent | Funcție |
|---|---|
| `matter_agent` | Urmărirea cauzelor |
| `citation_agent` | Validarea citărilor ECLI / CELEX |
| `court_agent` | Informații despre instanțe (CJUE, naționale) |
| `drafting_agent` | Asistență la redactare (conștientă de procedura UE) |
| `deadline_agent` | Verificarea termenelor de prescripție |
| `calendar_agent` | Sincronizare calendar ICS (fus orar Europa/Bruxelles) |
| `compliance_agent` | AI Act Anexa III + RGPD + SP/CSB + CCBE |

## ⚠️ Avertisment privind AI Act

**Regulamentul european privind IA (2024/1689)** clasifică sistemele de IA utilizate „în administrarea justiției" ca fiind **CU RISC RIDICAT** (Anexa III, punctul 8). Acest instrument este un software de gestionare a cabinetului (Risc Minim). NU efectuează raționament judiciar sau predicție a deciziilor.

## Confidențialitate

Totul este local. Conform cu RGPD prin proiectare. Niciun date nu părăsesc mașina dumneavoastră.

## Credite

the local memory layer de milla-jovovich (MIT) · 35 de surse juridice UE · wolfgang_rush, 2026 — Licența MIT

---

🙏 Bun venit · Welcome · Willkommen · Bienvenido · Benvenuto · Welkom · Witaj · Välkommen · Bem-vindo · Vítejte · Καλώς ήρθατε · Bienvenue · أهلاً وسهلاً
