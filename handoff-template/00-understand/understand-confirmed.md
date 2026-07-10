<!--
  Written ONLY via the Owner checkpoint protocol (patent-essay SKILL.md):
  by the orchestrator AFTER the Owner's explicit affirmative reply, or by
  --yes (by: orchestrator-yes-flag). The understand stage worker must never
  write this file. A file with placeholder or missing values is INVALID
  (the checkpoint counts as unconfirmed).

  comprehension: set by the P1 comprehension check at understand_confirm
  (captured | self-asserted | skipped-unattended). P2 will add demonstrated.
-->

# understand-confirmed

- **status**: pending          # confirmed | pending
- **by**:                      # owner | orchestrator-yes-flag
- **date**:                    # YYYY-MM-DD (real date)
- **patent**:                  # identifier from input/patent.md (e.g. US1234567B2)
- **comprehension**:            # captured | self-asserted | skipped-unattended (P1)
- **notes**:                   # REQUIRED when by: owner — quote the Owner's confirming utterance
