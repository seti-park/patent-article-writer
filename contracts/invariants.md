# Hard invariants

Load-bearing rules. Each cites the failure it prevents. Changing one requires a
fixture or explicit Owner decision recorded in `meta/CHANGELOG.md`.

1. **Physical isolation of compose vs review**  
   Failure: round-1 rubber-stamp (same context graded its own draft).  
   Mechanism: `context: fork` + fresh `editorial-reviewer` every round.

2. **Double-clean acceptance on `publish`**  
   Failure: single self-graded pass shipped.  
   Mechanism: two consecutive clean rounds from independent reviewers; `check_run` RUN-005.

3. **Composer never reads raw patent**  
   Failure: paraphrase drift / unanchored invention.  
   Mechanism: only Quotable spans + design handoff; patent access fenced to understand/review/verifier.

4. **Understand before design**  
   Failure: Owner re-studies the patent under deadline; angle pollutes comprehension.  
   Mechanism: `handoff/00-understand/` triad complete + gates; Owner confirm (unless `--yes`).

5. **Triad fidelity: Problem · Solution · Benefits**  
   Failure: essay invents pain, mechanism, or upside not licensed by the document.  
   Mechanism: `owner-study-pack.md` + `gate_quotes` on summary/briefing.

6. **Grounding fix priority: anchor → narrow → label → cut**  
   Failure: hedge ratchet under critic pressure.  
   Mechanism: jurisdiction fence in editorial-review; never “add a disclaimer to the verdict.”

7. **Verdict symmetry (overreach and over-hedge)**  
   Failure: safe-harbor boilerplate conclusions.  
   Mechanism: `closing_posture`, pass-6 6G, `gate_hedge`.

8. **Meta-loop propose-only**  
   Failure: self-editing skills into instability.  
   Mechanism: `pipeline-retro` writes proposals; human applies after `meta/regression.py`.

9. **check_run before archive**  
   Failure: incomplete loops archived as success.  
   Mechanism: RUN-001…; never edit artifacts to satisfy the checker.

10. **Promo safe-claims**  
    Failure: promo reintroduces scrubbed facts or over-hedges.  
    Mechanism: every factual phrase traces to essay-final/publication or owner-briefing.
