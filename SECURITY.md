# SECURITY — AI Brain · EU

## Reporting a vulnerability

If you discover a security vulnerability in AI Brain — EU, please report it via:

1. **GitHub Security Advisories** (preferred): https://github.com/Wolfgangrush/ai-law-firm-eu/security/advisories/new
2. **Private email**: advrushikeshravindramahajan@gmail.com

Please do NOT post vulnerabilities to public GitHub Issues.

Please include:
- A description of the vulnerability
- Steps to reproduce
- Potential impact (severity assessment)
- Any suggested mitigation
- Whether you wish to be publicly credited

We aim to acknowledge reports within 72 hours and provide an initial assessment within 7 days.

## Scope

### Vulnerabilities in scope

- Code-execution vulnerabilities (path traversal · command injection · pickle deserialization · etc.)
- Sensitive-data exposure (config-file world-readable · credentials in logs · etc.)
- Local privilege escalation via tool usage
- Cryptographic weaknesses
- Insecure default configurations

### Out of scope

- Vulnerabilities in upstream dependencies — report to those projects
- Vulnerabilities in cloud AI vendors — report to those vendors
- Social-engineering attacks against users
- Physical access attacks against the user's device

## Disclosure policy

Coordinated disclosure. No public disclosure until fix released or 90 days pass, whichever is sooner. Reporter credited (unless anonymity requested). For confirmed vulnerabilities meeting NIST CVSS criteria, CVE requested via GitHub CNA. No monetary bug bounty at this time.

## Security hygiene practices

- Dependencies pinned in `requirements.txt`
- Quarterly `pip-audit` review
- No `eval` · no `exec` · no unsafe deserialization
- All user input filtered before crossing tool/OS boundary
- File paths normalized to prevent path traversal
- Subprocess calls audited and use explicit argument lists (never `shell=True` with user input)
- Configuration files written with restrictive permissions (file mode 0600)
- No hardcoded credentials, API keys, or secrets in the codebase

## NIS2 Directive alignment (where applicable)

If the user's organization is in scope of the NIS2 Directive (Directive 2022/2555), the user's organization has its own cybersecurity risk-management obligations. The Software's design (local-first · no telemetry · pinned dependencies · no unsafe deserialization) supports the user's NIS2 alignment but does not relieve the user of any specific obligation.

## Past advisories

(None as of v0.1)

---

*This document references LEGAL_EXPOSURE_PLAYBOOK §3.V11 (Security Vulnerability). Playbook version: v0.1.*
