# Changelog

## [0.1.1] — 2026-06-05 · Dual-mode disclosure refinement (with Schrems II + Article 9 cloud-mode clarification)

### Changed
- **README.md** — refined headline tagline, "Why this exists" bullet on Post-Schrems II, "Why this exists" closing line, tier table rows (Local Ollama · DeepSeek · Claude/Gemini), and "Privacy & Data Handling — what stays where" section to honestly disclose the dual-mode architecture (local-default · cloud-optional) and the role of the internalised Pseudonymisation Gateway as the structural privacy primitive when cloud mode is invoked.

  **Schrems II is now explicitly framed dual-mode**:
  - In Local Ollama tier — Schrems II is moot (no cross-border transfer occurs).
  - In cloud mode — Schrems II DOES apply; Gateway sanitisation reduces exposure (structural pseudonymisation supports the TIA technical-measures prong) but does NOT eliminate it; user must independently execute SCCs + Transfer Impact Assessment per EDPB Recommendation 01/2020 + supplementary T&O measures + Article 28 GDPR DPA.

  **GDPR Article 9 special categories** are now flagged with their lawful-basis + cloud-mode requirements; the Compliance Officer agent flags Article 9 keywords automatically.

  **AI Act Article 50 transparency** is now named alongside Article 28 / Chapter V as a residual cloud-mode obligation.

  Prior wording overstated by treating local-only as architectural fact across all tiers; the architecture is in fact **local-default with cloud-optional + Gateway-sanitised cloud transmission**.

### Why this matters
An EU solo lawyer relying on the prior *"Your data stays on your machine"* line who configured a cloud-LLM provider for Article 9 special-category work would have been misled about the residual Chapter V obligations. Gateway sanitisation reduces Schrems II exposure structurally but cloud-mode users retain SCC + TIA + Article 28 obligations the prior wording did not surface. The refinement is honest disclosure; the Gateway as a privacy primitive is materially stronger than what most cloud-AI legal tools offer; the wedge for choosing this tool over commodity cloud AI is preserved.

### Unchanged
- All agents, drafting templates (56 EU templates + 11 statute digests), tests, getting-started guides, and the Pseudonymisation Gateway itself are unchanged. This is a documentation + privacy-disclosure-honesty refinement, not a behavioural change.
