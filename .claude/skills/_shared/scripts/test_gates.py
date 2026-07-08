#!/usr/bin/env python3
"""Stdlib unittest suite for the patent-essay validation gates.

Plants violations inline and asserts detection. Run with:

    python test_gates.py

Exits nonzero if any test fails.
"""

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gate_emdash
import gate_anchors
import gate_sources
import gate_banned
import gate_structure
import gate_figure_use
import gate_meta
import gate_stub
import gate_cashtag
import gate_dupe
import gate_typography
import gate_quotes
import gate_hedge
import gate_surface
import run_gates
import strip_publication
import check_run


def _has(result, check_id):
    return any(f["check_id"] == check_id for f in result["findings"])


class TestEmdash(unittest.TestCase):
    def test_emdash_outside_quote_fails(self):
        draft = "The system works well — most of the time.\n"
        r = gate_emdash.check(draft, {})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "EMDASH-001"))

    def test_emdash_inside_quote_passes(self):
        draft = 'The patent states "the system works — reliably" in column 3.\n'
        r = gate_emdash.check(draft, {})
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "EMDASH-001"))

    def test_emdash_in_blockquote_passes(self):
        draft = "> a verbatim quote — with a dash\n"
        r = gate_emdash.check(draft, {})
        self.assertTrue(r["passed"], r["findings"])

    def test_emdash_in_code_fence_ignored(self):
        draft = "```\nx — y\n```\n"
        r = gate_emdash.check(draft, {})
        self.assertTrue(r["passed"], r["findings"])

    def test_endash_connector_warns(self):
        draft = "The result was good – we measured it twice.\n"
        r = gate_emdash.check(draft, {})
        self.assertTrue(r["passed"])  # warn only, no fail
        self.assertTrue(_has(r, "EMDASH-002"))


class TestAnchors(unittest.TestCase):
    def test_unknown_anchor_fails(self):
        draft = "As shown in [9999], the rotor spins.\n"
        ctx = {"invention_summary_text": "Summary mentions [0001] and [0002]."}
        r = gate_anchors.check(draft, ctx)
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "ANCHOR-001"))

    def test_present_anchors_pass(self):
        draft = "See [0001] and [0002] for detail.\n"
        ctx = {"invention_summary_text": "Summary mentions [0001] and [0002]."}
        r = gate_anchors.check(draft, ctx)
        self.assertTrue(r["passed"], r["findings"])

    def test_no_summary_warns_and_passes(self):
        draft = "See [0001].\n"
        r = gate_anchors.check(draft, {})
        self.assertTrue(r["passed"])
        self.assertTrue(_has(r, "ANCHOR-000"))

    def test_figref_not_in_index_fails(self):
        draft = "Figure 7 shows the gear.\n"
        ctx = {"invention_summary_text": "", "figures_index": [1, 2, 3]}
        r = gate_anchors.check(draft, ctx)
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "FIGREF-001"))

    def test_figref_in_index_passes(self):
        draft = "Fig. 2 and Figure 3 are referenced.\n"
        ctx = {"invention_summary_text": "", "figures_index": [1, 2, 3]}
        r = gate_anchors.check(draft, ctx)
        self.assertTrue(r["passed"], r["findings"])

    def test_lettered_figref_not_in_index_fails(self):
        # Panel-suffixed off-index token must no longer escape FIGREF-001.
        draft = "FIG. 7C shows the gear.\n"
        ctx = {"invention_summary_text": "", "figures_index": [1, 2, 3]}
        r = gate_anchors.check(draft, ctx)
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "FIGREF-001"))

    def test_malformed_anchor_fails(self):
        draft = "See [123] and [12345] for detail.\n"
        ctx = {"invention_summary_text": "[0001]"}
        r = gate_anchors.check(draft, ctx)
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "ANCHOR-002"))

    def test_wellformed_anchor_no_format_finding(self):
        draft = "See [0001].\n"
        ctx = {"invention_summary_text": "[0001]"}
        r = gate_anchors.check(draft, ctx)
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "ANCHOR-002"))


class TestSources(unittest.TestCase):
    def test_missing_block_fails(self):
        draft = "# Intro\n\nSome body text with no sources.\n"
        r = gate_sources.check(draft, {})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "SOURCES-001"))

    def test_duplicate_block_fails(self):
        draft = "# Sources\n- a\n\n# Sources\n- b\n"
        r = gate_sources.check(draft, {})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "SOURCES-001"))

    def test_valid_flat_block_passes(self):
        draft = (
            "# Essay\n\nBody.\n\n"
            "# Sources\n"
            "- US1234567B2, Acme, Rotor, priorited 2019-01-01, published 2021-01-01\n"
            "- Smith, John (2020). Title. J. Mech.\n"
        )
        r = gate_sources.check(draft, {})
        self.assertTrue(r["passed"], r["findings"])

    def test_valid_subgrouped_block_passes(self):
        draft = (
            "# Sources\n"
            "## Patents\n"
            "- US1234567B2, Acme, Rotor\n"
            "## Technical specs\n"
            "- Bosch ECU spec sheet\n"
        )
        r = gate_sources.check(draft, {})
        self.assertTrue(r["passed"], r["findings"])

    def test_bad_category_fails(self):
        draft = (
            "# Sources\n"
            "## Industry data\n"
            "- some figure\n"
        )
        r = gate_sources.check(draft, {})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "SOURCES-002"))

    def test_partial_subgrouping_fails(self):
        draft = (
            "# Sources\n"
            "- a bare top-level entry\n"
            "## Patents\n"
            "- US1, Acme, Rotor\n"
        )
        r = gate_sources.check(draft, {})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "SOURCES-003"))

    def test_large_flat_list_warns(self):
        draft = (
            "# Sources\n"
            "- one\n- two\n- three\n- four\n- five\n"
        )
        r = gate_sources.check(draft, {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "SOURCES-004"))


class TestFigureUse(unittest.TestCase):
    SELECTION = "fig-01 maps to the lead. FIG. 2 anchors the mechanism. Figure 3 closes.\n"

    def test_orphan_selected_figure_fails(self):
        draft = "Figure 1 and Fig. 2 are discussed.\n"  # 3 selected but unused
        r = gate_figure_use.check(draft, {"figure_selection_text": self.SELECTION})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "FIGUSE-001"))

    def test_all_used_passes(self):
        draft = "Figure 1, Fig. 2, and Figure 3 all appear.\n"
        r = gate_figure_use.check(draft, {"figure_selection_text": self.SELECTION})
        self.assertTrue(r["passed"], r["findings"])

    def test_offplan_figure_warns(self):
        draft = "Figure 1, Fig. 2, Figure 3, and Figure 9 appear.\n"
        r = gate_figure_use.check(draft, {"figure_selection_text": self.SELECTION})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "FIGUSE-002"))

    def test_no_selection_skips(self):
        r = gate_figure_use.check("Figure 1.\n", {})
        self.assertTrue(r["passed"])
        self.assertTrue(_has(r, "FIGUSE-000"))

    def test_lettered_panel_token_counts_for_figure(self):
        # "FIG. 3B" must count as a reference to figure 3 (no false orphan).
        draft = "Figure 1, Fig. 2, and FIG. 3B all appear.\n"
        r = gate_figure_use.check(draft, {"figure_selection_text": self.SELECTION})
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "FIGUSE-001"))


class TestBanned(unittest.TestCase):
    def test_banned_hits_fail(self):
        draft = "We delve into the design; it is not just fast, but cheap.\n"
        r = gate_banned.check(draft, {})
        self.assertFalse(r["passed"])
        hits = [f for f in r["findings"] if f["check_id"] == "BANNED-001"]
        # 'delve' literal + 'not just ..., but' regex == 2 hits.
        self.assertEqual(len(hits), 2, hits)

    def test_clean_passes(self):
        draft = "The mechanism rotates a shaft to drive the pump.\n"
        r = gate_banned.check(draft, {})
        self.assertTrue(r["passed"], r["findings"])

    def test_banned_inside_quote_ignored(self):
        draft = 'The inventor said "we delve into novel territory" here.\n'
        r = gate_banned.check(draft, {})
        self.assertTrue(r["passed"], r["findings"])


class TestStructure(unittest.TestCase):
    def test_long_paragraph_warns(self):
        para = " ".join("This is sentence %d." % i for i in range(12))
        r = gate_structure.check(para + "\n", {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "STRUCT-001"))

    def test_eight_sentence_paragraph_warns(self):
        # Boundary aligned to editorial Pass 2C: exactly 8 sentences must warn.
        para = " ".join("This is sentence %d." % i for i in range(8))
        r = gate_structure.check(para + "\n", {})
        self.assertTrue(r["passed"])  # warn only
        hits = [f for f in r["findings"] if f["check_id"] == "STRUCT-001"]
        self.assertEqual(len(hits), 1, r["findings"])

    def test_seven_sentence_paragraph_clean(self):
        para = " ".join("This is sentence %d." % i for i in range(7))
        r = gate_structure.check(para + "\n", {})
        self.assertFalse(_has(r, "STRUCT-001"), r["findings"])

    def test_rule_of_three_warns(self):
        draft = "It was fast, cheap, and simple.\n"
        r = gate_structure.check(draft, {})
        self.assertTrue(_has(r, "STRUCT-004"))

    def test_bullet_overuse_warns(self):
        draft = "Intro line.\n- a\n- b\n- c\n- d\n"
        r = gate_structure.check(draft, {})
        self.assertTrue(_has(r, "STRUCT-003"))


class TestMeta(unittest.TestCase):
    def test_reader_instruction_fails(self):
        r = gate_meta.check("Read it the way an examiner would. The rotor spins.\n", {})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "META-001"))

    def test_self_reference_fails(self):
        r = gate_meta.check("Everything below is the proof; the rest of this essay shows it.\n", {})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "META-001"))

    def test_scope_disclaimer_passes(self):
        # functional self-reference, NOT posturing -> must not fire
        r = gate_meta.check("This essay does not adjudicate them. It only marks where to look.\n", {})
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "META-001"))

    def test_meta_inside_quote_ignored(self):
        r = gate_meta.check('A critic wrote "watch how the patent handles each" last year.\n', {})
        self.assertTrue(r["passed"], r["findings"])

    def test_soft_reader_address_warns(self):
        r = gate_meta.check("You might think the broad claim is the strong move.\n", {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "META-002"))


class TestStub(unittest.TestCase):
    def _doc(self, gamma_body):
        return ("## Alpha\n" + ("word " * 120) + "\n\n"
                "## Beta\n" + ("word " * 110) + "\n\n"
                "## Gamma\n" + gamma_body + "\n\n"
                "# Sources\n- x\n")

    def test_stub_section_warns(self):
        r = gate_stub.check(self._doc("a tiny stub."), {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "STUB-001"))

    def test_balanced_sections_pass(self):
        r = gate_stub.check(self._doc("word " * 100), {})
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "STUB-001"))

    def test_sources_subgroups_not_counted(self):
        draft = ("## Alpha\n" + ("word " * 80) + "\n\n"
                 "## Beta\n" + ("word " * 80) + "\n\n"
                 "## Gamma\n" + ("word " * 80) + "\n\n"
                 "# Sources\n## Patents\n- a\n## Papers\n- b\n")
        r = gate_stub.check(draft, {})
        self.assertFalse(_has(r, "STUB-001"))


class TestCashtag(unittest.TestCase):
    def test_bare_ticker_warns(self):
        r = gate_cashtag.check("The firm is trading as AGLT starting Monday.\n", {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "CASH-001"))

    def test_exchange_colon_warns(self):
        r = gate_cashtag.check("It lists on NASDAQ: AGLT this quarter.\n", {})
        self.assertTrue(_has(r, "CASH-001"))

    def test_cashtag_form_passes(self):
        r = gate_cashtag.check("The firm is trading as $AGLT starting Monday.\n", {})
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "CASH-001"))

    def test_acronym_not_flagged(self):
        r = gate_cashtag.check("The deal with GXO and USPTO filings, sold as one stack.\n", {})
        self.assertFalse(_has(r, "CASH-001"))


class TestDupe(unittest.TestCase):
    def test_gross_repeat_warns(self):
        draft = ("The defensible engine is filed elsewhere entirely. "
                 "Months later, the defensible engine is filed elsewhere entirely.\n")
        r = gate_dupe.check(draft, {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "DUPE-001"))

    def test_no_repeat_passes(self):
        r = gate_dupe.check("The rotor turns a shaft which then drives a centrifugal pump cleanly.\n", {})
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "DUPE-001"))

    def test_quoted_repeat_ignored(self):
        draft = ('It says "a deployment mechanism and deployable autonomous delivery robot" once; '
                 'again "a deployment mechanism and deployable autonomous delivery robot" verbatim.\n')
        r = gate_dupe.check(draft, {})
        self.assertFalse(_has(r, "DUPE-001"))


class TestTypography(unittest.TestCase):
    def test_latin_dotted_fails(self):
        r = gate_typography.check("The rotor spins, e.g. at high rpm.\n", {})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "LATIN-001"))

    def test_latin_bare_fails(self):
        r = gate_typography.check("Use a sensor, ie a thermocouple, here.\n", {})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "LATIN-001"))

    def test_latin_inside_quote_passes(self):
        r = gate_typography.check('The patent says "the load, e.g. a motor, varies".\n', {})
        self.assertTrue(r["passed"], r["findings"])

    def test_exclamation_fails(self):
        r = gate_typography.check("This is a huge result!\n", {})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "EXCLAIM-001"))

    def test_markdown_image_not_exclamation(self):
        r = gate_typography.check("![figure one](fig-01.png)\n", {})
        self.assertFalse(_has(r, "EXCLAIM-001"))

    def test_emoji_warns(self):
        r = gate_typography.check("The result is wild \U0001F525.\n", {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "EMOJI-001"))

    def test_sanctioned_thinking_emoji_passes(self):
        r = gate_typography.check("So who really owns the moat? \U0001F914\n", {})
        self.assertFalse(_has(r, "EMOJI-001"))

    def test_caps_run_warns(self):
        r = gate_typography.check("This is THE BIG DEAL today.\n", {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "CAPS-001"))

    def test_single_acronyms_not_flagged(self):
        r = gate_typography.check("The USB link to the LLM is fast.\n", {})
        self.assertFalse(_has(r, "CAPS-001"))

    def test_part_number_not_flagged(self):
        r = gate_typography.check("See US1234567B2 for the rotor.\n", {})
        self.assertFalse(_has(r, "CAPS-001"))

    def test_nondescriptive_link_warns(self):
        r = gate_typography.check("Read the spec [here](http://x.example).\n", {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "LINK-001"))

    def test_long_sentence_warns(self):
        draft = "The rotor " + "and the shaft " * 20 + "spin together.\n"
        r = gate_typography.check(draft, {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "LONGSENT-001"))

    def test_code_fence_exempt(self):
        r = gate_typography.check("```\nx = 1  # e.g. this!\n```\n", {})
        self.assertTrue(r["passed"], r["findings"])

    def test_frontmatter_and_heading_no_longer_merge(self):
        # Before the boundary-merge fix, frontmatter + title + heading text
        # (none of which end in terminal punctuation) glued straight into the
        # first real sentence, inflating it well past the word limit.
        draft = (
            "---\nessay_id: some-long-test-identifier-string\n"
            "mode_used: strict-execution\nposture_used: measured\n---\n"
            "# A Reasonably Short Title For This Test Draft Today\n\n"
            "## Section One Heading Text Goes Here For This Draft\n\n"
            "This is a short clean sentence that stays under the target length.\n"
        )
        r = gate_typography.check(draft, {})
        self.assertFalse(_has(r, "LONGSENT-001"), r["findings"])

    def test_bold_line_boundary_no_longer_merges(self):
        # A standalone **bold** line has no terminal punctuation the old
        # splitter's lookahead recognizes ('*' is not [A-Z0-9"']), so it used
        # to glue onto its neighbor instead of standing as its own boundary.
        draft = (
            "Intro sentence stays reasonably short and quite clean right "
            "here in this test paragraph today, plainly.\n\n"
            "**A standalone bold thesis line that stands entirely alone on "
            "its own separate paragraph here today.**\n\n"
            "Another short clean sentence follows immediately right after "
            "it today, without any further delay at all.\n"
        )
        r = gate_typography.check(draft, {})
        self.assertFalse(_has(r, "LONGSENT-001"), r["findings"])

    def test_genuine_long_sentence_still_warns(self):
        draft = "The rotor " + "and the shaft and the pump and the gear " * 6 + "spin together today.\n"
        r = gate_typography.check(draft, {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "LONGSENT-001"))


class TestRunGatesEndToEnd(unittest.TestCase):
    CLEAN = (
        "# Essay\n\n"
        "The rotor turns a shaft. The shaft drives a pump. This is described "
        "plainly. See [0001] for the mechanism and Figure 1 for the layout.\n\n"
        "# Sources\n"
        "- US1234567B2, Acme, Rotor, priorited 2019-01-01, published 2021-01-01\n"
        "- Smith, John (2020). Title. J. Mech.\n"
    )
    DIRTY = (
        "# Essay\n\n"
        "We delve into the rotor — it is fast. See [9999] and Figure 9.\n"
        # no Sources block
    )

    def _write(self, text):
        fh = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
        fh.write(text)
        fh.close()
        return fh.name

    def test_clean_passes(self):
        ctx = {"invention_summary_text": "[0001]", "figures_index": [1]}
        overall, results = run_gates.run_all(self.CLEAN, ctx)
        self.assertTrue(overall, [r for r in results if not r["passed"]])

    def test_dirty_fails(self):
        ctx = {"invention_summary_text": "[0001]", "figures_index": [1]}
        overall, results = run_gates.run_all(self.DIRTY, ctx)
        self.assertFalse(overall)

    def test_main_exit_codes(self):
        clean_path = self._write(self.CLEAN)
        dirty_path = self._write(self.DIRTY)
        summary = self._write("[0001]")
        figs = self._write("1")
        try:
            rc_clean = run_gates.main(
                ["--draft", clean_path, "--invention-summary", summary, "--figures", figs])
            rc_dirty = run_gates.main(
                ["--draft", dirty_path, "--invention-summary", summary, "--figures", figs])
            self.assertEqual(rc_clean, 0)
            self.assertEqual(rc_dirty, 1)
        finally:
            for p in (clean_path, dirty_path, summary, figs):
                os.unlink(p)


class TestQuotes(unittest.TestCase):
    PATENT = (
        "# US 9,999,999 B2\n\n"
        "[0016] The vision sensor provides **pre-impact prediction** to the\n"
        "airbag controller before contact occurs.\n\n"
        "[0024] The deployment decision is made approximately 70 milliseconds\n"
        "before traditional systems would respond.\n"
    )
    SUMMARY = (
        "**Quotable spans:**\n"
        '- `[0016]`: "The vision sensor provides pre-impact prediction to the airbag controller"\n'
        "\n"
        "## Quote anchor table\n\n"
        "| Quote ID | Paragraph | Verbatim text | Significance |\n"
        "|---|---|---|---|\n"
        '| q-0024-1 | `[0024]` | "approximately 70 milliseconds" | quantitative |\n'
    )

    def test_verbatim_quotes_pass(self):
        # Span 0016 crosses a bold marker + a hard wrap in the patent text:
        # the allowed normalizations must bridge both.
        r = gate_quotes.check("", {"invention_summary_text": self.SUMMARY,
                                   "patent_text": self.PATENT})
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "QUOTE-001"))

    def test_fabricated_span_fails(self):
        summary = self.SUMMARY.replace("pre-impact prediction", "post-impact correction")
        r = gate_quotes.check("", {"invention_summary_text": summary,
                                   "patent_text": self.PATENT})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "QUOTE-001"))

    def test_mutated_table_quote_fails(self):
        summary = self.SUMMARY.replace("approximately 70 milliseconds",
                                       "approximately 90 milliseconds")
        r = gate_quotes.check("", {"invention_summary_text": summary,
                                   "patent_text": self.PATENT})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "QUOTE-001"))

    def test_no_patent_skips(self):
        r = gate_quotes.check("", {"invention_summary_text": self.SUMMARY})
        self.assertTrue(r["passed"])
        self.assertTrue(_has(r, "QUOTE-000"))

    def test_summary_without_quotes_warns(self):
        r = gate_quotes.check("", {"invention_summary_text": "## Metadata\nnothing here\n",
                                   "patent_text": self.PATENT})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "QUOTE-002"))


class TestHedge(unittest.TestCase):
    def _draft(self, verdict, firm=False, limits=""):
        fm = "---\nessay_id: t\nclosing_posture: firm\n---\n" if firm else ""
        return (
            fm + "# T\n\n## Lead\n\nBody paragraph one.\n\n" + limits +
            "## The Investor Read\n\n" + verdict + "\n\n# Sources\n\n- US1, Acme\n"
        )

    def test_boilerplate_fails_when_firm(self):
        d = self._draft("The verdict is yes. But a patent does not guarantee production.",
                        firm=True)
        r = gate_hedge.check(d, {})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "HEDGE-001"))

    def test_boilerplate_warns_without_firm_posture(self):
        d = self._draft("A patent does not guarantee production.")
        r = gate_hedge.check(d, {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "HEDGE-001"))

    def test_qualifier_led_verdict_fails_when_firm(self):
        d = self._draft("The verdict is a qualified yes, with real limits.", firm=True)
        r = gate_hedge.check(d, {})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "HEDGE-002"))

    def test_firm_clean_verdict_passes(self):
        d = self._draft(
            "The verdict is yes. The claim sits on the physics of the problem. "
            "The boundaries scope the moat rather than cancel it. "
            "Watch the continuation filings over the next year.", firm=True)
        r = gate_hedge.check(d, {})
        self.assertTrue(r["passed"], r["findings"])

    def test_quoted_boilerplate_exempt(self):
        d = self._draft('The CEO said "a patent does not guarantee success" on stage. '
                        "The verdict is yes.", firm=True)
        r = gate_hedge.check(d, {})
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "HEDGE-001"))

    def test_limits_section_not_scanned(self):
        limits = ("## What This Patent Does Not Do\n\n"
                  "A patent is not a product, and it does not guarantee production.\n\n")
        d = self._draft("The verdict is yes. The moat is real and it gates the revenue.",
                        firm=True, limits=limits)
        r = gate_hedge.check(d, {})
        self.assertTrue(r["passed"], r["findings"])

    def test_hedge_density_warns(self):
        d = self._draft(
            "The claim might hold. Competitors could route around it. "
            "The market may not care. Perhaps the family grows.")
        r = gate_hedge.check(d, {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "HEDGE-003"))


class TestSurface(unittest.TestCase):
    def test_title_too_long_warns(self):
        draft = (
            "# " + ("A" * 75) + ".\n\n"
            "## Section\n\n"
            "The rotor spins fast today. It drives the pump reliably.\n"
        )
        r = gate_surface.check(draft, {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "SURF-001"))

    def test_qualifier_led_first_sentence_warns(self):
        draft = (
            "# A Short Clean Title\n\n"
            "## Section\n\n"
            "The verdict here is a qualified yes, with real limits attached. "
            "The rest of the paragraph explains why.\n"
        )
        r = gate_surface.check(draft, {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "SURF-002"))

    def test_clean_draft_passes(self):
        draft = (
            "# A Short Clean Title\n\n"
            "## Section\n\n"
            "The rotor spins fast today. It drives the pump reliably.\n"
        )
        r = gate_surface.check(draft, {})
        self.assertTrue(r["passed"], r["findings"])
        self.assertEqual(r["findings"], [])

    def test_defensive_open_lexicon_warns(self):
        draft = (
            "# A Short Clean Title\n\n"
            "## Section\n\n"
            "This is a pending application from a small startup. "
            "It is not a patent yet.\n"
        )
        r = gate_surface.check(draft, {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "SURF-004"))

    def test_numeral_dense_cover_caption_warns(self):
        draft = (
            "# A Short Clean Title\n\n"
            "![alt](fig-01.png)\n\n"
            "*FIG. 1: parts 100, 200, 300, 400, 500, 600, and 700 shown.*\n\n"
            "## Section\n\n"
            "The rotor spins fast today. It drives the pump reliably.\n"
        )
        r = gate_surface.check(draft, {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "SURF-003"))

    def test_lead_procedure_narration_warns(self):
        draft = (
            "# A Short Clean Title\n\n"
            "## The Lead\n\n"
            "The rotor spins fast today. The examiner rejected the first claim set. "
            "The company keeps paying to argue the case, and the last RCE was filed "
            "in April. It drives the pump reliably regardless.\n\n"
            "## Section Two\n\n"
            "Nothing procedural happens here at all.\n"
        )
        r = gate_surface.check(draft, {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "SURF-005"))

    def test_lead_single_procedure_sentence_does_not_warn(self):
        draft = (
            "# A Short Clean Title\n\n"
            "## The Lead\n\n"
            "The rotor spins fast today. The examiner rejected the first claim set. "
            "It drives the pump reliably regardless.\n\n"
            "## Section Two\n\n"
            "Nothing procedural happens here at all.\n"
        )
        r = gate_surface.check(draft, {})
        self.assertTrue(r["passed"])
        self.assertFalse(_has(r, "SURF-005"))

    def test_lead_procedure_terms_in_quotes_and_blockquotes_exempt(self):
        draft = (
            "# A Short Clean Title\n\n"
            "## The Lead\n\n"
            'The filing says "the examiner rejected the claim after the RCE fee '
            'was paid." The rotor spins fast today.\n\n'
            "> The examiner rejected it and the fee was paid during examination.\n\n"
            "It drives the pump reliably regardless.\n\n"
            "## Section Two\n\n"
            "Nothing procedural happens here at all.\n"
        )
        r = gate_surface.check(draft, {})
        self.assertTrue(r["passed"])
        self.assertFalse(_has(r, "SURF-005"))

    def test_lead_status_language_alone_does_not_warn(self):
        draft = (
            "# A Short Clean Title\n\n"
            "## The Lead\n\n"
            "The rotor spins fast today. This application is still pending, and the "
            "patent office has not said yes. It drives the pump reliably regardless.\n\n"
            "## Section Two\n\n"
            "Nothing procedural happens here at all.\n"
        )
        r = gate_surface.check(draft, {})
        self.assertTrue(r["passed"])
        self.assertFalse(_has(r, "SURF-005"))

    def test_spend_motif_warns_above_threshold(self):
        # 5 lexicon hits: paid, fee, paid, fee, paying.
        draft = (
            "# A Short Clean Title\n\n"
            "## Section\n\n"
            "The company paid the first fee. It paid a second fee too. "
            "Then it kept paying a third time.\n"
        )
        r = gate_surface.check(draft, {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "SURF-006"))

    def test_spend_motif_at_threshold_does_not_warn(self):
        # 4 lexicon hits: paid, fee, paid, fee -- at the max, should not fire.
        draft = (
            "# A Short Clean Title\n\n"
            "## Section\n\n"
            "The company paid the first fee. It paid a second fee too.\n"
        )
        r = gate_surface.check(draft, {})
        self.assertTrue(r["passed"])
        self.assertFalse(_has(r, "SURF-006"))

    def test_spend_motif_quoted_spans_exempt(self):
        draft = (
            "# A Short Clean Title\n\n"
            "## Section\n\n"
            'The filing states "the fee was paid, the payment was made, the company '
            'kept paying and spending on the fee." The rotor spins fast today.\n'
        )
        r = gate_surface.check(draft, {})
        self.assertTrue(r["passed"])
        self.assertFalse(_has(r, "SURF-006"))

    def test_steelman_overweight_warns(self):
        # The non-lead 'The Objection, Read Cold' section carries 2+
        # CONCESSION_MARKER hits ("concedes", "strongest objection", "read
        # cold", "no single claim") and a spend-motif hit ("fee", "spend") --
        # the steelman-overweight shape SURF-007 targets.
        draft = (
            "# A Short Clean Title\n\n"
            "## The Lead\n\n"
            "The rotor spins fast today. It drives the pump reliably.\n\n"
            "## The Objection, Read Cold\n\n"
            "This section concedes the strongest objection directly: no single "
            "claim here has issued yet. Read cold, the filing's overseas "
            "counterparts are fee money a company does not usually spend on "
            "ideas it considers dead.\n\n"
            "## The Core Holds Anyway\n\n"
            "Nothing above touches the core sequence directly.\n"
        )
        r = gate_surface.check(draft, {})
        self.assertTrue(r["passed"])  # warn only
        self.assertTrue(_has(r, "SURF-007"))

    def test_compact_concession_without_spend_motif_does_not_warn(self):
        # Same concede beat, still >= SURF007_MIN_MARKERS, but compact and
        # carrying no spend/procedure motif -- a lean, specific steelman is
        # not what SURF-007 targets.
        draft = (
            "# A Short Clean Title\n\n"
            "## The Lead\n\n"
            "The rotor spins fast today. It drives the pump reliably.\n\n"
            "## The Objection, Read Cold\n\n"
            "This section concedes the strongest objection directly: no single "
            "claim here has issued yet. Nothing else in the record changes "
            "that.\n\n"
            "## The Core Holds Anyway\n\n"
            "Nothing above touches the core sequence directly.\n"
        )
        r = gate_surface.check(draft, {})
        self.assertTrue(r["passed"])
        self.assertFalse(_has(r, "SURF-007"))


class TestCheckRun(unittest.TestCase):
    CLEAN_LOG = "overall_assessment: pass\n\nfindings:\n  - pass: pass-1\n    finding: \"no findings\"\n"
    FAIL_LOG = (
        "overall_assessment: revise-required\n\nfindings:\n"
        "  - finding_id: r1-F1\n    pass: pass-3-fact-paraphrase\n"
        "    location: s3\n    severity: high\n    finding: \"drift\"\n"
    )
    GATE_PASS = '{"passed": true, "gates": []}'

    def setUp(self):
        self.root = tempfile.mkdtemp()
        self.edit = os.path.join(self.root, "03-edit")
        self.compose = os.path.join(self.root, "02-compose")
        os.makedirs(self.edit)
        os.makedirs(self.compose)

    def _w(self, rel, text):
        path = os.path.join(self.root, rel)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)

    def _write_owner_briefing(self, text=None):
        os.makedirs(os.path.join(self.root, "01-design"), exist_ok=True)
        self._w("01-design/owner-briefing.md", text if text is not None else (
            "## 이 특허가 다루는 문제\n\n"
            "기존 기술은 성능과 비용 사이의 절충으로 어려움을 겪었다.\n\n"
            "**근거 (verbatim):**\n"
            '- `[0001]`: "sample verbatim line for fixture"\n'
        ))

    def _accepted_double_clean(self, with_briefing=True):
        self._w("03-edit/edit-log.round-1.md", self.FAIL_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("02-compose/revision-response.round-1.md",
                "# Revision response\n\n## r1-F1\n\n- disposition: applied\n")
        self._w("03-edit/edit-log.round-2.md",
                "overall_assessment: pass\n\nfindings:\n"
                "  - pass: carried\n    finding: \"r1-F1 verified fixed\"\n")
        self._w("03-edit/gate-result.round-2.json", self.GATE_PASS)
        self._w("03-edit/edit-log.round-3.md", self.CLEAN_LOG)
        self._w("03-edit/gate-result.round-3.json", self.GATE_PASS)
        self._w("02-compose/revision-response.round-2.md", "# Revision response\n(no medium+ findings)\n")
        self._w("03-edit/essay-final.md", "# Final\n")
        self._w("03-edit/revision-notes.md", "## delta\n- self-audit fix\n")
        if with_briefing:
            self._write_owner_briefing()

    def test_double_clean_acceptance_passes(self):
        self._accepted_double_clean()
        r = check_run.check(self.root)
        self.assertTrue(r["passed"], r["findings"])

    def test_single_pass_promotion_fails(self):
        self._w("03-edit/edit-log.round-1.md", self.CLEAN_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("03-edit/essay-final.md", "# Final\n")
        self._w("03-edit/revision-notes.md", "self-audit: no unresolved findings\n")
        r = check_run.check(self.root)
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-005"))

    def test_missing_disposition_fails(self):
        self._w("03-edit/edit-log.round-1.md", self.FAIL_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("02-compose/revision-response.round-1.md", "# Revision response\n(empty)\n")
        self._w("03-edit/edit-log.round-2.md", self.CLEAN_LOG.replace("pass\n", "pass\nr1-F1 ruled: fixed\n", 1))
        self._w("03-edit/gate-result.round-2.json", self.GATE_PASS)
        r = check_run.check(self.root)
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-003"))

    def test_dropped_carried_id_fails(self):
        self._w("03-edit/edit-log.round-1.md", self.FAIL_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("02-compose/revision-response.round-1.md", "## r1-F1\n- disposition: applied\n")
        self._w("03-edit/edit-log.round-2.md", self.CLEAN_LOG)  # never mentions r1-F1
        self._w("03-edit/gate-result.round-2.json", self.GATE_PASS)
        r = check_run.check(self.root)
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-004"))

    def test_cap_hit_promotion_warns_but_passes(self):
        self._w("03-edit/edit-log.round-1.md", self.FAIL_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("02-compose/revision-response.round-1.md", "## r1-F1\n- disposition: applied\n")
        self._w("03-edit/edit-log.round-2.md",
                "overall_assessment: revise-required\n\nfindings:\n"
                "  - finding_id: r2-F1\n    pass: pass-3\n    severity: high\n"
                "    finding: \"r1-F1 persists\"\n")
        self._w("03-edit/gate-result.round-2.json", self.GATE_PASS)
        self._w("03-edit/essay-final.md", "# Final\n")
        self._w("03-edit/score-history.md", "| 2 | ... |\nCAP HIT at max-iter; best round shipped.\n")
        self._w("03-edit/revision-notes.md", "self-audit: no unresolved findings\n")
        self._write_owner_briefing()
        r = check_run.check(self.root)
        self.assertTrue(r["passed"], r["findings"])
        self.assertTrue(_has(r, "RUN-006"))

    def test_missing_self_audit_fails(self):
        self._accepted_double_clean()
        os.unlink(os.path.join(self.edit, "revision-notes.md"))
        r = check_run.check(self.root)
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-007"))

    def test_owner_briefing_present_and_nonempty_no_finding(self):
        self._accepted_double_clean()
        r = check_run.check(self.root)
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "RUN-008"))

    def test_owner_briefing_missing_fails(self):
        self._accepted_double_clean(with_briefing=False)
        r = check_run.check(self.root)
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-008"))

    def test_owner_briefing_whitespace_only_fails(self):
        self._accepted_double_clean(with_briefing=False)
        self._write_owner_briefing(text="   \n\t\n  \n")
        r = check_run.check(self.root)
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-008"))

    def test_confirmation_transition_without_response_passes(self):
        # Round 1 clean; round 2 is a confirmation round (round_type marker)
        # reviewing the SAME draft with no revision in between -- per spec
        # there is nothing to disposition or trace, so no
        # revision-response.round-1.md should be required at all.
        self._w("03-edit/edit-log.round-1.md", self.CLEAN_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("03-edit/edit-log.round-2.md",
                "# Edit Log - Round 2 (confirmation round: no revision since round 1)\n\n"
                "```yaml\noverall_assessment: pass\nround_type: confirmation\n\n"
                "findings:\n  - pass: carried\n    finding: \"no findings\"\n```\n")
        self._w("03-edit/gate-result.round-2.json", self.GATE_PASS)
        self._w("03-edit/essay-final.md", "# Final\n")
        self._w("03-edit/revision-notes.md", "self-audit: no unresolved findings\n")
        self._write_owner_briefing()
        r = check_run.check(self.root)
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "RUN-001"))
        self.assertFalse(_has(r, "RUN-003"))
        self.assertTrue(_has(r, "RUN-000"))  # informational confirmation-skip note

    def test_prior_severity_notation_excluded_from_run003_and_run004(self):
        # Round 1: fresh high finding r1-F1, dispositioned normally.
        self._w("03-edit/edit-log.round-1.md", self.FAIL_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("02-compose/revision-response.round-1.md",
                "# Revision response\n\n## r1-F1\n\n- disposition: applied\n")
        # Round 2 RULES on r1-F1 using prior_severity: notation only (a
        # carried verification block) and raises nothing new of its own --
        # this must NOT be treated as a new round-2 finding.
        self._w("03-edit/edit-log.round-2.md",
                "overall_assessment: pass\n\ncarried_finding_rulings:\n\n"
                "  - finding_id: r1-F1\n"
                "    prior_severity: high\n"
                "    disposition_claimed: applied\n"
                "    ruling: verified-landed\n"
                "    evidence: |\n"
                "      the fix is present in the current draft text\n\n"
                "findings:\n"
                "  - pass: pass-1\n    finding: \"no further findings\"\n")
        self._w("03-edit/gate-result.round-2.json", self.GATE_PASS)
        self._w("02-compose/revision-response.round-2.md",
                "# Revision response\n(no new medium+ findings this round)\n")
        # Round 3: a normal fresh clean round (no confirmation marker), so
        # this test exercises the prior_severity fix on its own, independent
        # of the confirmation-transition detection.
        self._w("03-edit/edit-log.round-3.md", self.CLEAN_LOG)
        self._w("03-edit/gate-result.round-3.json", self.GATE_PASS)
        r = check_run.check(self.root)
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "RUN-003"))
        self.assertFalse(_has(r, "RUN-004"))

    def test_genuinely_dropped_medium_still_fails(self):
        # Regression guard: prior_severity exclusion must not become a
        # blanket exemption. Round 1 declares two medium+ findings.
        self._w("03-edit/edit-log.round-1.md",
                "overall_assessment: revise-required\n\nfindings:\n"
                "  - finding_id: r1-F1\n    pass: pass-3\n    severity: high\n"
                "    finding: \"drift one\"\n"
                "  - finding_id: r1-F2\n    pass: pass-4\n    severity: medium\n"
                "    finding: \"drift two\"\n")
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("02-compose/revision-response.round-1.md",
                "# Revision response\n\n## r1-F1\n- disposition: applied\n\n"
                "## r1-F2\n- disposition: applied\n")
        # Round 2 properly carries/rules r1-F1 (prior_severity notation) but
        # never mentions r1-F2 anywhere -- a genuine silent drop.
        self._w("03-edit/edit-log.round-2.md",
                "overall_assessment: pass\n\ncarried_finding_rulings:\n\n"
                "  - finding_id: r1-F1\n"
                "    prior_severity: high\n"
                "    ruling: verified-landed\n"
                "    evidence: |\n"
                "      present in the current draft\n\n"
                "findings:\n  - pass: pass-1\n    finding: \"no further findings\"\n")
        self._w("03-edit/gate-result.round-2.json", self.GATE_PASS)
        r = check_run.check(self.root)
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-004"))


class TestStripPublication(unittest.TestCase):
    DRAFT = (
        "---\n"
        "essay_id: 044-test\n"
        "mode_used: walkthrough\n"
        "---\n"
        "# Title\n"
        "\n"
        "First line of a paragraph that was\n"
        "hard-wrapped at a narrow column [^f-one]\n"
        "and continues here.\n"
        "\n"
        "> a verbatim quote line\n"
        "> attribution line\n"
        "\n"
        "*FIG. 1, [0042]: caption stays on its own line.*\n"
        "\n"
        "# Sources\n"
        "- US1234567B2, Acme, Rotor\n"
        "\n"
        "# Footnotes\n"
        "[^f-one]: fact-base entry\n"
    )

    def test_frontmatter_stripped(self):
        out = strip_publication.strip_publication(self.DRAFT)
        self.assertNotIn("essay_id", out)
        self.assertTrue(out.startswith("# Title"))

    def test_footnotes_cut_sources_kept(self):
        out = strip_publication.strip_publication(self.DRAFT)
        self.assertNotIn("# Footnotes", out)
        self.assertNotIn("fact-base entry", out)
        self.assertIn("# Sources", out)

    def test_markers_stripped_no_space_artifact(self):
        out = strip_publication.strip_publication(self.DRAFT)
        self.assertNotIn("[^f-one]", out)
        self.assertNotIn("  ", out)  # marker removal must not leave a double space
        self.assertIn("hard-wrapped at a narrow column and continues here.", out)

    def test_paragraph_rejoined_to_one_line(self):
        out = strip_publication.strip_publication(self.DRAFT)
        self.assertIn(
            "First line of a paragraph that was hard-wrapped at a narrow column "
            "and continues here.", out.splitlines())

    def test_structural_lines_not_joined(self):
        out = strip_publication.strip_publication(self.DRAFT)
        lines = out.splitlines()
        self.assertIn("> a verbatim quote line", lines)
        self.assertIn("> attribution line", lines)
        self.assertIn("*FIG. 1, [0042]: caption stays on its own line.*", lines)

    def test_code_fence_untouched(self):
        draft = "Body text.\n\n```\nx = 1\ny = 2\n```\n"
        out = strip_publication.strip_publication(draft)
        self.assertIn("x = 1\ny = 2", out)


def _run():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    total = result.testsRun
    failed = len(result.failures) + len(result.errors)
    print("\n%s" % ("=" * 50))
    print("SUMMARY: %d run, %d passed, %d failed" % (total, total - failed, failed))
    print("%s" % ("=" * 50))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(_run())
