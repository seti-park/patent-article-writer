# Exemplar notes — which archived essays are patterns, and which are not

Fresh-context workers (compose, review, self-audit) sometimes read an archived
`essays/<id>/` to calibrate. Not every archive is a model to imitate: some predate
current invariants. This note flags the archives that are **historical, not
patterns**, so a worker does not learn a superseded shape from them.

## Pre-double-clean archives (do NOT imitate the acceptance shape)

The `publish` profile requires **double-clean** acceptance (two consecutive clean
rounds from independent reviewers — invariant 2). Archives that terminated on a
single review round predate that rule. Their prose may still be good, but their
**loop shape is not a pattern**.

| Archive | Rounds | Why non-exemplary |
|---------|--------|-------------------|
| `essays/agility-us12560948` | 1 | Single review round — predates double-clean. Read it for voice/scope-precision only, never for the acceptance shape. |

(Round count is the number of `edit-log.round-N.md` / score-history rows. Re-check
with `for e in essays/*/; do ...` if new archives land.)

## Superseded archives

`essays/_superseded/` holds essays replaced by a later edition (e.g. an `-r2`
re-run supersedes its first cut). These are kept for provenance only — always
prefer the current edition. Do not cite or imitate a `_superseded` entry.

## What IS exemplary

Several current archives are model implementations of claim-scope precision (the
system's affirmative-writing target — see `docs/architecture/comprehension-loop.md`
§5.1): `agility-us12560948`'s "Locked, Open, And Pinned" section, and
`intel-us20260191095-backend-hbm`'s explicit claim-vs-inference separation. Imitate
the *scope-precision*, not (for agility) the acceptance shape.
