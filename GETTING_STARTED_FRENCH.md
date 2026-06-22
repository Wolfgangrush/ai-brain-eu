# Démarrage — AI Brain for EU Lawyers · v0.1

**🙏 Bienvenue, Maître — votre AI Brain commence ici.**

## Qu'est-ce que c'est ?

AI Brain EU est un **assistant de gestion de cabinet juridique** pour les avocats indépendants de l'UE. Il fonctionne entièrement sur votre machine — pas de cloud, pas de clé API, pas de télémétrie. Vos dossiers ne quittent jamais votre ordinateur.

## Installation (30 secondes)

```bash
cd ~/Desktop
git clone https://github.com/Wolfgangrush/ai-law-firm-eu.git
cd ai-law-firm-eu
pip install -e .
```

## Démarrez votre cabinet (2 minutes)

```bash
mkdir ~/mon-cabinet-eu
ailawfirm-eu init ~/mon-cabinet-eu
ailawfirm-eu mine ~/mon-cabinet-eu
ailawfirm-eu search "Bruxelles I-bis exécution"
```

## 7 agents spécialistes

| Agent | Fonction |
|---|---|
| `matter_agent` | Suivi des dossiers |
| `citation_agent` | Validation des citations ECLI / CELEX |
| `court_agent` | Recherche des juridictions (CJUE, nationales) |
| `drafting_agent` | Assistance à la rédaction (consciente de la procédure UE) |
| `deadline_agent` | Vérification des délais de prescription |
| `calendar_agent` | Synchronisation calendrier ICS (fuseau Europe/Bruxelles) |
| `compliance_agent` | AI Act Annexe III + RGPD + LCB-FT + CCBE |

## ⚠️ Avertissement AI Act

Le **Règlement européen sur l'IA (2024/1689)** classe les systèmes d'IA utilisés « dans l'administration de la justice » comme **HAUT RISQUE** (Annexe III, point 8). Cet outil est un logiciel de gestion de cabinet (Risque Minimal). Il n'effectue PAS de raisonnement judiciaire ni de prédiction de décisions.

## Confidentialité

Tout est local. Conforme RGPD par conception. Aucune donnée ne quitte votre machine.

## Crédits

the local memory layer par milla-jovovich (MIT) · 35 sources juridiques UE · wolfgang_rush, 2026 — Licence MIT

---

🙏 Bienvenue · Welcome · Willkommen · Bienvenido · Benvenuto · Welkom · Witaj · Välkommen · Bem-vindo · Vítejte · Καλώς ήρθατε · Bun venit · أهلاً وسهلاً
