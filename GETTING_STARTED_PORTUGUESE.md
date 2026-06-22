# Começar — AI Brain for EU Lawyers · v0.1

**🙏 Bem-vindo, advogado — a sua AI Brain começa aqui.**

## O que é?

AI Brain EU é um **assistente de gestão de escritório de advocacia** para advogados independentes da UE. Funciona inteiramente na sua máquina — sem nuvem, sem chave de API, sem telemetria. Os seus processos nunca saem do seu computador.

## Instalação (30 segundos)

```bash
cd ~/Desktop
git clone https://github.com/Wolfgangrush/ai-law-firm-eu.git
cd ai-law-firm-eu
pip install -e .
```

## Inicie o seu escritório (2 minutos)

```bash
mkdir ~/meu-escritorio-eu
ailawfirm-eu init ~/meu-escritorio-eu
ailawfirm-eu mine ~/meu-escritorio-eu
ailawfirm-eu search "Bruxelas I-bis execução"
```

## 7 agentes especialistas

| Agent | Função |
|---|---|
| `matter_agent` | Acompanhamento de processos |
| `citation_agent` | Validação de citações ECLI / CELEX |
| `court_agent` | Informação sobre tribunais (TJUE, nacionais) |
| `drafting_agent` | Assistência à redação (ciente do processo UE) |
| `deadline_agent` | Verificação de prazos de prescrição |
| `calendar_agent` | Sincronização de calendário ICS (fuso Europa/Bruxelas) |
| `compliance_agent` | AI Act Anexo III + RGPD + BC/FT + CCBE |

## ⚠️ Aviso sobre a AI Act

O **Regulamento Europeu de IA (2024/1689)** classifica os sistemas de IA utilizados « na administração da justiça » como **ALTO RISCO** (Anexo III, ponto 8). Esta ferramenta é um software de gestão de escritório (Risco Mínimo). NÃO realiza raciocínio judicial nem previsão de decisões.

## Privacidade

Tudo é local. Conforme ao RGPD por conceção. Nenhum dado sai da sua máquina.

## Créditos

the local memory layer por milla-jovovich (MIT) · 35 fontes jurídicas da UE · wolfgang_rush, 2026 — Licença MIT

---

🙏 Bem-vindo · Welcome · Willkommen · Bienvenido · Benvenuto · Welkom · Witaj · Välkommen · Bienvenue · Vítejte · Καλώς ήρθατε · Bun venit · أهلاً وسهلاً
