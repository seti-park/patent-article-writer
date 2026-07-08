# Cold read — casual X scroller, round 1

Blind protocol observed: read `handoff/03-edit/essay-final.md` once, top to bottom, at
reading speed, looking at the embedded figures (fig-05 header; figs 1, 2, 3, 6, 7 in the
body) from `input/figures/`. Nothing else opened. No checklist — this is what actually
happened in my head.

## 1. Where I stopped or skimmed

I read the whole thing — the argument I'd seen online kept me going — but I skimmed twice
and genuinely dragged once.

First skim: the long legal quote in the memory section. I bailed about fifteen words into
"Another embodiment in this disclosure is a package that includes an IC comprising a
systolic array of data processing units (DPUs) and a separate memory device comprising a
plurality of channels..." — my eyes jumped down to the bolded line after it, which told me
what the quote meant anyway.

The real attention drop: "Computing attention queries means the data 'passes through the
systolic array three times' [0055]." That paragraph and the one around it (batches, Time B,
layer normalization, 98%) is where I stopped reading sentence-by-sentence and started
sliding. The "This one budgeted its idle cycles" line at the end pulled me back in.

Small glaze: the parentheticals with "reel/frame 067204/0877" — I skipped the numbers both
times, though I kept reading the sentences around them.

The little [0016]-style bracket numbers everywhere: I stopped seeing them after the second
section. Not a stop — just noise I learned to filter.

## 2. What I felt, section by section

- **Title + header picture:** curious. The picture is a dry black-and-white line drawing,
  but the caption's "pitched on stage in July 2026... The drawing is dated May 2023" is the
  whole reason I kept going.
- **The Pitch Has a Paper Trail:** hooked — "the patent office still hasn't said yes to it"
  told me both sides of the fight I'd seen were about to get dealt with. The third
  paragraph ("the verdict in miniature... prices exactly that") felt chewy and abstract; I
  pushed through it.
- **One Giant Array, Stitched From Identical Chips:** mildly smart — lots of identical
  small chips pretending to be one big one is easy to picture, like tiles. The aside about
  a "companion analysis" of another patent felt like inside baseball for people who read a
  previous article I haven't.
- **The Memory Claims Delete the Switch:** smartest I felt all article, and here is the one
  moment: the trade — each column can only read its own memory lane, and that's fine
  because the weights parked there never change, so nothing ever needs to switch. I got WHY
  you can delete the layer, not just that they say they did. The bolded "It is claim
  language, dated May 2023" is the mic-drop. (Skimmed the legal blockquote, see item 1.)
- **Math That Forgets, a Sidecar That Remembers:** liked it — the sidecar with its own
  private memory, walled off from the big array, stuck with me. Then bored in the
  scheduling part; won back by "budgeted its idle cycles."
- **Etched Keeps Paying to Own It:** most gripped. "Final rejection" jolted me — I clicked
  half-expecting a receipts victory lap and instead got told the examiner already said no
  once and the company paid to keep arguing. The loan bit where the second lien lands three
  days after two patents granted — "The dates are facts. Any motive read into them is
  inference." — felt like being let in on gossip without the article actually gossiping.
  Pleasantly suspicious, aimed at the company, not the writer.
- **An Asset in Formation:** satisfied. "On stage the layer is already gone. At the patent
  office, Etched is still paying to own the deletion" is the closer I'll remember.

## 3. What I'd repeat to a friend tomorrow

"You know that Etched chip everyone's fighting about? Their whole 'no memory layers' pitch
is literally written into their first patent from May 2023, before they had anything to
sell — so the idea really is theirs. But the patent office has already rejected it once,
they're still paying to fight for it, and they've borrowed money against those patents.
Real receipts, not yet real property."

## 4. Would I have tapped from the feed?

Yes — but only because I'd seen the argument. "Put Its No-Switch Memory Idea in Writing in
May 2023" promises receipts, which is exactly what the fight was about, and a patent
drawing as the first image looks like evidence, which fits the promise. Cold, with no
argument context, "No-Switch Memory Idea" plus a gray line drawing probably scrolls past.
