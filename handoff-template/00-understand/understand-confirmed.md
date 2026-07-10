<!--
  Written ONLY via the Owner checkpoint protocol (patent-essay SKILL.md):
  by the orchestrator AFTER the Owner's explicit affirmative reply, or by
  --yes (by: orchestrator-yes-flag). The understand stage worker must never
  write this file. A file with placeholder or missing values is INVALID
  (the checkpoint counts as unconfirmed).

  comprehension: P2 value set (IF-1 frozen) —
    demonstrated | self-asserted | skipped-unattended | risk-accepted
  When comprehension: risk-accepted, notes: MUST contain the verbatim string
  "claim-scope risk accepted by owner".
-->

# understand-confirmed

- **status**: pending          # confirmed | pending
- **by**:                      # owner | orchestrator-yes-flag
- **date**:                    # YYYY-MM-DD (real date)
- **patent**:                  # identifier from input/patent.md (e.g. US1234567B2)
- **comprehension**:            # demonstrated | self-asserted | skipped-unattended | risk-accepted
- **notes**:                   # REQUIRED when by: owner — quote the Owner's confirming utterance
                               # when risk-accepted: MUST include "claim-scope risk accepted by owner"
