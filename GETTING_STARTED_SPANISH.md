# Inicio — AI Brain for EU Lawyers · v0.1

**🙏 Bienvenido, abogado — su AI Brain comienza aquí.**

## ¿Qué es?

AI Brain EU es un **asistente de gestión de despacho jurídico** para abogados independientes de la UE. Funciona completamente en su máquina — sin nube, sin clave API, sin telemetría. Sus expedientes nunca salen de su ordenador.

## Instalación (30 segundos)

```bash
cd ~/Desktop
git clone https://github.com/Wolfgangrush/ai-law-firm-eu.git
cd ai-law-firm-eu
pip install -e .
```

## Inicie su despacho (2 minutos)

```bash
mkdir ~/mi-despacho-eu
ailawfirm-eu init ~/mi-despacho-eu
ailawfirm-eu mine ~/mi-despacho-eu
ailawfirm-eu search "Bruselas I-bis ejecución"
```

## 7 agentes especialistas

| Agent | Función |
|---|---|
| `matter_agent` | Seguimiento de asuntos |
| `citation_agent` | Validación de citas ECLI / CELEX |
| `court_agent` | Información de tribunales (TJUE, nacionales) |
| `drafting_agent` | Asistencia a la redacción (consciente del procedimiento UE) |
| `deadline_agent` | Verificación de plazos de prescripción |
| `calendar_agent` | Sincronización de calendario ICS (huso Europa/Bruselas) |
| `compliance_agent` | AI Act Anexo III + RGPD + PBC/FT + CCBE |

## ⚠️ Aviso sobre la AI Act

El **Reglamento Europeo de Inteligencia Artificial (2024/1689)** clasifica los sistemas de IA utilizados « en la administración de justicia » como **ALTO RIESGO** (Anexo III, punto 8). Esta herramienta es un software de gestión de despacho (Riesgo Mínimo). NO realiza razonamiento judicial ni predicción de decisiones.

## Privacidad

Todo es local. Conforme al RGPD por diseño. Ningún dato sale de su máquina.

## Créditos

the local memory layer por milla-jovovich (MIT) · 35 fuentes jurídicas UE · wolfgang_rush, 2026 — Licencia MIT

---

🙏 Bienvenido · Welcome · Willkommen · Bienvenue · Benvenuto · Welkom · Witaj · Välkommen · Bem-vindo · Vítejte · Καλώς ήρθατε · Bun venit · أهلاً وسهلاً
