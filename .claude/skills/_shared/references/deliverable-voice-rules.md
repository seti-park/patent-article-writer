# Deliverable Voice Rules (checkable — Phase 2 author, Phase 3 judge)

> **Base: the govuk-style plain-English standard, adapted for patent essays.** The *checkable*
> composition rules for the published essay's voice. Loaded by Phase 2 (to write) and Phase 3
> (to judge — this is the voice file the editor is allowed to see, since it is rules, not
> persona). Many rules here are also enforced mechanically by `_shared/scripts/` so they survive
> every revision; the gate `check_id` is noted on each. The author's distinctive *persona*
> (openings, closings, aphoristic landings) lives in `voice-canon-lookup/`, not here —
> govuk-style is the hygiene layer, the voice canon is the personality, and they stack.

## Hard rules (gate-enforced — a hit fails the loop round)

- **No em-dash** (`—`) in body or title outside verbatim quotes. *(gate: `EMDASH-001`)*
- **No Latin abbreviations** — write "for example" / "that is" / "and so on", not eg / ie / etc.
  *(gate: `LATIN-001`)*
- **No exclamation marks** in body prose. *(gate: `EXCLAIM-001`)*
- **No banned AI-tell terms/constructions** outside quotes (the govuk-base govspeak/cliché list
  + the SETI canon live in `anti-ai-writing.md` → `scripts/banned_terms.txt`). *(gate: `BANNED-001`)*
- **No reader-instruction / essay-self-reference posturing** — "read it the way…", "the rest of
  this essay…". Insight, not stage directions. *(gate: `META-001`; functional scope disclaimers
  like "this essay does not adjudicate X" are exempt.)*
- **Citations resolve + well-formed:** every `[dddd]` anchor is 4-digit zero-padded and exists in
  the Phase-1 hand-off; every figure ref resolves. *(gates: `ANCHOR-001/002`, `FIGREF-001`)*
- **No orphan figures:** every figure Phase 1 selected is actually used. *(gate: `FIGUSE-001`)*
- **Sources block** present exactly once as `# Sources` (h1), 5-label enum, all-or-nothing `##`
  subgrouping. *(gates: `SOURCES-001/002/003`)*

## Composition base (govuk-style) — soft rules + warn-gates + Phase-3 judgment

- **Front-load everything.** The single most important point first — in the section, the
  paragraph, and the sentence. At the piece level the front-loaded thing is the lead's HOOK
  beat, not the insurance: ¶1 delivers the chosen energy register's beat (never a deferred
  question, never a disclaimer stack), and the full two-sided call lands by the lead
  section's end — see `reader-energy.md`. *(editorial pass-6 6A/6H + pass-7 hook check.)*
- **One idea per sentence; active voice; everyday words.** Say who does what. Prefer the plain
  word (use not utilise, help not facilitate, start not commence) — see the plain-word swaps in
  `anti-ai-writing.md`.
- **Keep sentences short — pressure, not a cap.** Target ~15–25 words; a necessary causal or
  claim clause may run longer. Egregious run-ons warn. *(gate: `LONGSENT-001` warn, threshold 35.)*
- **Restrained bold.** At most one load-bearing thesis anchor per essay; otherwise bold only to
  name a literal interface element. No bold/bullet overuse, no reflexive rule-of-three.
  *(gate warns: `STRUCT-002/003/004`; the single-anchor persona pattern is in voice-canon.)*
- **No emoji** (the single sanctioned closing 🤔 excepted); **no ALL-CAPS emphasis** (acronyms and
  part numbers are fine). *(gates: `EMOJI-001`, `CAPS-001` — both warn.)*
- **Descriptive link text** — say where it goes, key words first; never "click here".
  *(gate: `LINK-001` warn.)*
- **Numbers and dates (editorial, not gated):** spell out "one", numerals from 2 up; dates like
  "4 June 2026"; ranges with "to". *Deliberately not gated* — patent part numbers and claim ranges
  use hyphens legitimately, so this stays editorial judgment.
- **Jargon as signposts, not deep-dives:** keep the short term-of-art the target reader scans for
  ("Section 101", "Alice"); cut the doctrinal explanation only a specialist needs. *(pass-5.)*
- **Headings.** Body section headers are claims (a header-only skim = the argument); follow the X
  Articles format in `essay-en-composer/references/x-articles-format-en.md`. **Capitalization:
  Title Case** — the X Articles house style. (govuk-style prefers sentence case, but heading
  format is the pipeline's decision and govuk defers to it; never mix cases in one piece.)
  *(editorial pass-6/7; not gated.)*
- **No stub sections; no gross verbatim repetition; tickers as `$`-cashtags.**
  *(gate warns: `STUB-001`, `DUPE-001`, `CASH-001`.)*

## Reading level — readability, not depth (govuk)

The "9-year-old reading age" target is about reading *difficulty*, not content *depth*.

- **Keep** the precise technical term (`die-attach`, `sintering`, a part number). Specialist
  vocabulary is not jargon; removing it makes the writing worse for the expert reader who is the
  point.
- **Lower** the difficulty of the connective tissue around those terms: shorter sentences, active
  voice, common verbs. Precision stays; reading speed goes up.

## Patent-domain exceptions

These override the plain-English rules where the patent's own language is at stake:

- **Verbatim patent / specification quotes, claim language, terms of art, and part numbers keep
  their exact wording.** Plain-word swaps and the reading-age target apply ONLY to the connective
  prose, never to quoted or claim material. (Every gate already exempts double-quoted spans,
  blockquotes, and fenced code, so quoted patent text is safe.)
- A subordinate clause the claim logic needs ("if X then Y, unless Z") may exceed the
  sentence-length target — keep the clause, trim the fat around it.
- Em-dashes inside a verbatim quote are allowed (`gate_emdash` already exempts them).

<!-- PORT: when the Tier-1 banned list changes, mirror it to scripts/banned_terms.txt and keep
     the check_ids above aligned with the gate scripts. -->
