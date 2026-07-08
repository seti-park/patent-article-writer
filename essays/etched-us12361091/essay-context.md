# Essay context — US 12,361,091 B1 (Etched.ai, "Tensor parallel group")

Framing brief for the patent-essay pipeline. Read by Phase 1 (audience reframe) and carried
through Phase 2/3.

## Audience and deliverable

- **Audience:** default reader-profile (curious retail investor; technical comprehension
  advanced high school – early undergraduate). No override.
- **News moment:** Etched.ai exited stealth in early July 2026 with an X thread that drove
  retail interest in inference-specialized chips. Readers arrive asking whether the
  architecture claims in that thread have patent substance.
- **Question to answer:** Etched claims "Cluster-Scale Memory" (CSM) — a shared low-latency
  memory pool across the whole scale-up domain over a proprietary ultra-low-latency
  interconnect. Does this granted patent substantiate a real, defensible piece of that
  story? Land a clear verdict.
- **Deliverable:** one standalone English analytical article (X Articles long-form). A
  possible part-2 essay on sibling US 12,306,903 B1 (dataflow deep-dive) is reserved: cover
  the siblings as context, do NOT deep-dive their mechanics here.

## News context (company-claimed external facts — source: Etched official X thread, 2026-07)

All of the following are company claims from the stealth-exit thread, not independently
verified; if used, attribute as such ("the company says"):

- Out of stealth after A0 tapeout; first racks built; "$1B+ in customer contracts"; "$800m
  raised"; first racks ship summer 2026.
- Two claimed architecture pillars:
  - **LVI (Low-Voltage Inference):** math blocks at under half the voltage of typical AI
    chips for FLOPs density; "trillion parameter sparse MoEs at 80%+ peak FLOPs without
    thermal throttling".
  - **CSM (Cluster-Scale Memory):** "shared low-latency memory pool across the entire
    scale-up domain"; "proprietary ultra-low-latency, high-bandwidth interconnect"; "each
    memory layer inherently adds latency; thus, the best layer is no layer"; HBM/SRAM
    hybrid design.

## Patent-family facts (verified: WIPS ON bibliographic export, 2026-07-02)

- **This patent:** US 12,361,091 B1, "Tensor parallel group". Filed 2024-10-22
  (US 18/922,976), granted 2025-07-15. Sole inventor Gavin Uberti (Etched co-founder/CEO);
  assignee Etched.ai Inc. 23 claims, 3 independent (per WIPS); 16 figures. Expected expiry
  2044-10-22. Small-entity status on filing.
- **Same-day trio:** filed 2024-10-22 alongside US 12,306,903 B1 ("Performance of tensor
  operations", granted 2025-05-20) and US 12,361,262 B1 ("Tensor operations in AI models",
  granted 2025-07-15) — same sole inventor. Each of the three carries a PCT international
  filing (WO 2026/090208, 090209, 090210) and a US continuation published in 2026
  (US 2026-0111513 / 0111514 / 0111709 A1). The company is paying to extend exactly this
  trio internationally — a commitment signal usable in the essay.
- **Division of labor in the trio:** 903 = how tensor tiles move between chips (method);
  091 (this one) = how the chips are wired (structure/topology); 262 = the model-level
  execution umbrella. One short context paragraph on the siblings is enough.
- Etched's earlier 2023 filings (multi-chip systolic arrays, self-attention circuit,
  compiler applications) exist but are OUT of scope for this essay.

## Scope boundaries (anti-hype guard material)

- The thread's **LVI** claims (voltage, VRMs, power delivery, packaging, cold plates) are
  NOT covered by this patent or its granted siblings. Do not credit LVI to this filing; the
  gap itself is a legitimate observation (later filings may still be unpublished — 18-month
  window).
- The **HBM/SRAM hybrid** from the thread is not claimed in this patent either.
- **Claim-scope discipline (locked / open / pinned):** the verdict rests on what the granted
  independent claims actually require. Note: independent claim 1 requires two sets of
  **four or more** devices each (the abstract's "two or more" is the broader description
  framing; the granted claim is narrower). Never credit optional description embodiments to
  the granted claims.
- External market/financing facts stay fenced as "outside the filing" and sourced.

## Posture and closing discipline

- **Posture: measured.** Full accuracy bar; no relaxation of claim-scope or external-fact
  discipline.
- **closing_posture: firm** (verdict edition default). Lead the verdict with the call, not
  a qualifier; state limits once as boundaries that scope the finding, not as equal
  counterweights; exactly one patent-specific anti-hype guard.
- The steelman must be a THIS-patent objection (grounded in the actual claims/figures or
  prosecution facts), not a generic patent truism.

## Figures available

- `input/figures-raw/` carries the granted patent's drawing sheets (17 PNG sheets;
  D00000 is the front-page representative duplicate — Phase 0 dedupes/renames). The patent
  describes FIG. 1–13 with multi-panel FIGS. 7A–7C and 9A–9B (16 individual figures).
