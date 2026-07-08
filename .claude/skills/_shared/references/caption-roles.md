# Caption Roles (figure planning — Phase 2 only)

> **Status: SCAFFOLD + canon target.** The roles a figure caption can play and the
> figure-locking rule. Loaded **only** by Phase 2 (`essay-en-composer` /
> `voice-canon-lookup`). Phase 3 (Edit) does **not** load this file (fencing). Replace with
> the user's canon; keep the 4-role enum.

## The 4 caption roles (starter — port the canon)

Each selected figure is assigned exactly one `caption_role`:

1. **Evidence** — the figure *is* the proof for a claim.
2. **Mechanism** — the figure shows *how* the disclosed thing works.
3. **Orientation** — the figure situates the reader (context/overview).
4. **Contrast** — the figure marks the gap vs the prior-art baseline.

## figures_locked

Once Phase 2 assigns roles and placements, the set is **locked** for the run: the figure
list, their roles, and their positions don't change during revision unless a Phase-3
finding explicitly calls for it. Record this in `handoff/02-compose/figures-rationale.md`.

<!-- PORT: drop the user's caption-roles canon here. Keep the role names if the gates or
     composer key on them. -->
