# Title-Lead Candidates

**reader_sentence** (`input/essay-context.md` absent; drafted here for the orchestrator to confirm):
> A year before OpenAI announced its own chip, someone at OpenAI had already written the math engine down to the individual memory cell, and filed it.

All five pairs ride the locked spine's facts (claim-1 triad; priority 2024-11-22 vs announcement 2025-10-13; latch-level depth). Register changes delivery order and polarity only. Titles are ≤ 70 characters; no verdict-insurance fact precedes the beat in any lead.

## discovery

- **title**: OpenAI's Chip Patent Does Floating-Point Math on Integer Adders
- **lead**: There is a published OpenAI patent that designs an AI chip down to the individual memory cell: the math runs inside the memory array itself, and the expensive part, summing thousands of floating-point products, is done by plain integer adders after one clever shift. The paperwork carries a priority date of November 22, 2024, eleven months before OpenAI and Broadcom announced their "OpenAI-designed" accelerators. It is a pending application, not a granted patent, and that prices what follows without changing it.
- **rationale**: Hands the reader the reader_sentence's unknown fact directly (the document exists, it is this deep, and it is this early); the mechanism rides in the same breath.

## tension

- **title**: OpenAI Announced Its Chip in 2025. The Filing Says November 2024
- **lead**: On October 13, 2025, OpenAI announced it would design its own AI accelerators with Broadcom. The patent record says the design work is older: a compute-in-memory engine, specified down to latch circuits and clock margins, carrying an OpenAI-assigned priority date of November 22, 2024. Both dates are real, and the gap between them is the story of how literal "OpenAI-designed" has become.
- **rationale**: Collides two checkable dates; the reader_sentence is the resolution of the collision.

## contrarian

- **title**: OpenAI Isn't Just Buying Chips. The Patent Record Shows Design
- **lead**: The consensus read is that OpenAI is the world's biggest chip customer, and that "designs its own accelerators" is press-release garnish on a Broadcom contract. The published patent record argues back: a compute-in-memory macro that multiplies in floating point and accumulates on integer adders, written at the level of individual bitcells, scan chains, and setup times. That is not garnish. That is circuit design, on file since November 2024.
- **rationale**: States the citable consensus in one sentence, then inverts it with the document; the reader leaves able to correct the crowd with the reader_sentence.

## insider

- **title**: Inside OpenAI's First Silicon Patent, Down to the Memory Cell
- **lead**: Almost everyone has an opinion on OpenAI's chip ambitions; almost nobody has read the one primary document OpenAI has published about them. US 2026/0147536 A1 is that document, and it goes further than any announcement: individual memory cells that store a weight and multiply by it in place, a one-shot alignment trick that lets integer adders finish floating-point math, and test circuitry for silicon someone intends to manufacture. Here is what it commits to, element by element.
- **rationale**: Access is the value; the reader_sentence becomes something the reader saw over the essayist's shoulder.

## stakes

- **title**: Ten Gigawatts of Custom AI Compute Start With One Skipped Step
- **lead**: OpenAI has committed to deploying ten gigawatts of its own accelerators, and at that scale the enemy is any circuit that does the same work twice. Its published chip patent attacks exactly that: every needless conversion between number formats costs area, power, and latency, so the design converts once, sums everything as integers inside the memory array, and converts back once at the end. The ten-gigawatt bet and the one-conversion arithmetic are the same idea at two scales.
- **rationale**: The 10 GW figure carries ¶1 and prices why the mechanism matters; the reader_sentence supplies the who-and-when.

---

recommended: discovery
why: The document's existence, depth, and early date are genuinely unknown to the target reader and deliver the reader_sentence in one beat, with the mechanism payload in ¶1 (reader-payload-first); tension is the fallback if the orchestrator wants the date collision foregrounded.
