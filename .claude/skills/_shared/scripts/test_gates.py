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

    def test_dropped_figures_in_reviewed_section_not_orphaned(self):
        # Figures named only in "Reviewed but NOT selected" / "Figure relationships"
        # are NOT selected and must not false-orphan when absent from the draft.
        selection = (
            "# Figure Selection\n\n"
            "## Selected figures\n"
            "| FIG. 1 | fig-01.png | header |\n"
            "| FIG. 4 | fig-04.png | body |\n"
            "| FIG. 5 | fig-05.png | body |\n\n"
            "## Reviewed but NOT selected (with reason)\n"
            "| FIG. 2 | fig-02.png | redundant with FIG. 1 |\n"
            "| FIG. 3 | fig-03.png | covered by FIG. 5 + prose |\n"
        )
        draft = "FIG. 1 anchors it. FIG. 4 shows the legs. FIG. 5 the deployment.\n"
        r = gate_figure_use.check(draft, {"figure_selection_text": selection})
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "FIGUSE-001"))

    def test_orphan_still_fails_within_selected_section(self):
        # A genuine orphan inside "## Selected figures" must still FAIL.
        selection = (
            "## Selected figures\n"
            "| FIG. 1 | header |\n| FIG. 4 | body |\n| FIG. 5 | body |\n\n"
            "## Reviewed but NOT selected\n| FIG. 2 | dropped |\n"
        )
        draft = "Only FIG. 1 and FIG. 4 appear.\n"   # FIG. 5 is a true orphan
        r = gate_figure_use.check(draft, {"figure_selection_text": selection})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "FIGUSE-001"))

    def test_acknowledged_pair_section_not_selected(self):
        # Intel-style: selected {1,5,7,8,11}; acknowledged pairs name 9/10/2...
        selection = (
            "## Selected figures\n"
            "| FIG. 1 | | |\n| FIG. 5A/5B | | |\n| FIG. 7 | | |\n"
            "| FIG. 8 | | |\n| FIG. 11 | | |\n\n"
            "## Paired-figure relationships (acknowledged)\n"
            "FIG. 9, FIG. 10, FIG. 2, FIG. 3, FIG. 4, FIG. 6, "
            "FIG. 12, FIG. 13, FIG. 14, FIG. 15\n"
        )
        draft = "FIG. 1, FIG. 5, FIG. 7, FIG. 8, and FIG. 11 appear.\n"
        r = gate_figure_use.check(draft, {"figure_selection_text": selection})
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "FIGUSE-001"))
        selected = gate_figure_use._figure_numbers(
            gate_figure_use._selected_region(selection))
        self.assertEqual(selected, {1, 5, 7, 8, 11})


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
        # Without a patent the gate cannot verify verbatim matches: warn-only
        # QUOTE-000 and pass (vacuous zero-anchor FAIL requires patent available).
        r = gate_quotes.check("", {"invention_summary_text": self.SUMMARY})
        self.assertTrue(r["passed"])
        self.assertTrue(_has(r, "QUOTE-000"))
        self.assertFalse(_has(r, "QUOTE-002"))

    def test_summary_without_quotes_fails_when_patent_available(self):
        # GATE-05 / HARNESS-02: zero extractable anchors + patent present → FAIL
        # (essay mode / invention-summary requires anchors).
        r = gate_quotes.check("", {"invention_summary_text": "## Metadata\nnothing here\n",
                                   "patent_text": self.PATENT,
                                   "mode": "essay"})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "QUOTE-002"))

    def test_summary_without_quotes_warns_in_wire_mode(self):
        r = gate_quotes.check("", {"invention_summary_text": "## Metadata\nnothing here\n",
                                   "patent_text": self.PATENT,
                                   "mode": "wire"})
        self.assertTrue(r["passed"])  # wire: anchors optional → warn only
        self.assertTrue(_has(r, "QUOTE-002"))

    def test_fabricated_quote_with_trailing_gloss_fails(self):
        # H5: trailing gloss after closing quote must not skip the line.
        summary = (
            "**Quotable spans:**\n"
            '- `[0016]`: "this fabricated span is not in the patent at all" (gloss)\n'
        )
        r = gate_quotes.check("", {"invention_summary_text": summary,
                                   "patent_text": self.PATENT})
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "QUOTE-001"))

    def test_verbatim_quote_with_trailing_gloss_passes(self):
        summary = (
            "**Quotable spans:**\n"
            '- `[0016]`: "The vision sensor provides pre-impact prediction to the '
            'airbag controller" (owner note)\n'
        )
        r = gate_quotes.check("", {"invention_summary_text": summary,
                                   "patent_text": self.PATENT})
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "QUOTE-001"))

    def test_span_line_without_closing_quote_not_extracted(self):
        # Boundary: malformed line with no closing quote is not a quote to check.
        summary = (
            "**Quotable spans:**\n"
            '- `[0016]`: "unterminated span without close\n'
        )
        r = gate_quotes.check("", {"invention_summary_text": summary,
                                   "patent_text": self.PATENT,
                                   "mode": "essay"})
        # No extractable quote → QUOTE-002 (zero anchors), not a silent pass of fabrications.
        self.assertFalse(r["passed"])
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
    # Self-declared pass while medium+ findings remain (RUN-014).
    DIRTY_PASS_LOG = (
        "overall_assessment: pass\n\nfindings:\n"
        "  - finding_id: r1-F1\n    pass: pass-3-fact-paraphrase\n"
        "    location: s3\n    severity: high\n    finding: \"still broken\"\n"
    )
    GATE_PASS = '{"passed": true, "gates": []}'
    GATE_FAIL = '{"passed": false, "gates": [{"findings": [{"check_id": "BANNED-001", "severity": "fail"}]}]}'
    # Minimal essay-final that passes run_gates with empty/optional context
    # (RUN-015 recheck default-on must not invent failures on compliant fixtures).
    CLEAN_ESSAY = (
        "# Title\n\n"
        "Body text here about the rotor mechanism under load.\n\n"
        "# Sources\n"
        "- US9999999B2, Fixture Co.\n"
    )
    # Fails BANNED-001 (delve) so a lying gate-result.round-K.json is catchable.
    DIRTY_ESSAY = (
        "# Title\n\n"
        "We delve into the rotor mechanism under load carefully.\n\n"
        "# Sources\n"
        "- US9999999B2, Fixture Co.\n"
    )
    PATENT_ID = "US9999999B2"

    def setUp(self):
        # Production layout: <run_root>/{input,handoff,essays}/
        # check_run resolves run_root as parent of --handoff.
        self.run_root = tempfile.mkdtemp()
        self.root = os.path.join(self.run_root, "handoff")  # handoff_dir
        self.edit = os.path.join(self.root, "03-edit")
        self.compose = os.path.join(self.root, "02-compose")
        os.makedirs(self.edit)
        os.makedirs(self.compose)
        os.makedirs(os.path.join(self.run_root, "input"), exist_ok=True)
        patent_path = os.path.join(self.run_root, "input", "patent.md")
        with open(patent_path, "w", encoding="utf-8") as fh:
            fh.write("# %s — Fixture Patent\n\n[0001] sample verbatim line for fixture\n"
                     % self.PATENT_ID)
        # Real runs always carry a run-manifest (bootstrap writes it). A
        # design-or-beyond run under owner-confirm cannot skip the patent lock
        # by omitting it (RUN-012), so the compliant baseline includes one; the
        # absent-manifest tests remove it explicitly.
        self._write_manifest()

    def _write_manifest(self):
        import hashlib
        patent_path = os.path.join(self.run_root, "input", "patent.md")
        h = hashlib.sha256(open(patent_path, "rb").read()).hexdigest()
        self._w("run-manifest.md",
                "# run-manifest\n\n"
                "- **run_id**: fixture-run\n"
                "- **patent**: %s\n"
                "- **patent_sha256**: %s\n"
                "- **profile**: publish\n"
                "- **started**: 2026-07-10\n" % (self.PATENT_ID, h))

    def _w(self, rel, text):
        path = os.path.join(self.root, rel)
        parent = os.path.dirname(path)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)

    def _legacy(self, **kwargs):
        """check() with RUN-010/011/015 off — isolates pre-existing rules."""
        opts = dict(owner_confirm="off", require_understand=False,
                    recheck_gates=False)
        opts.update(kwargs)
        return check_run.check(self.root, **opts)

    def _write_cap_confirmed(self, round_n, by="owner", status="confirmed",
                             date="2026-07-10", notes='"ship at cap"'):
        self._w("03-edit/cap-confirmed.md",
                "# cap-confirmed\n\n"
                "- **status**: %s\n"
                "- **by**: %s\n"
                "- **date**: %s\n"
                "- **round**: %s\n"
                "- **notes**: %s\n"
                % (status, by, date, round_n, notes))

    def _write_owner_briefing(self, text=None):
        os.makedirs(os.path.join(self.root, "01-design"), exist_ok=True)
        self._w("01-design/owner-briefing.md", text if text is not None else (
            "## 이 특허가 다루는 문제\n\n"
            "기존 기술은 성능과 비용 사이의 절충으로 어려움을 겪었다.\n\n"
            "**근거 (verbatim):**\n"
            '- `[0001]`: "sample verbatim line for fixture"\n'
        ))
        inv = os.path.join(self.root, "01-design", "invention-summary.md")
        if not os.path.exists(inv):
            self._w("01-design/invention-summary.md",
                    "# Invention Summary\n\n## Metadata\n- **Patent ID**: %s\n\n"
                    "## Layer 1\nFixture mechanism for check_run tests.\n\n"
                    "## Quotable spans\n"
                    '- `[0001]`: "sample verbatim line for fixture"\n'
                    % self.PATENT_ID)

    def _write_understand_complete(self, confirmed=True, by="owner",
                                   status="confirmed", date="2026-07-10",
                                   patent=None, notes='"owner confirmed triad"'):
        os.makedirs(os.path.join(self.root, "00-understand"), exist_ok=True)
        self._w("00-understand/invention-summary.md",
                "# Invention Summary\n\n## Metadata\n- **Patent ID**: %s\n\n"
                "## Layer 1\nFixture mechanism.\n\n"
                "## Quotable spans\n"
                '- `[0001]`: "sample verbatim line for fixture"\n'
                % self.PATENT_ID)
        self._w("00-understand/owner-study-pack.md",
                "# Owner Study Pack\n\n## 1. Problem\n\n"
                '**근거 (verbatim):**\n- `[0001]`: "sample verbatim line for fixture"\n')
        self._w("00-understand/owner-briefing.md",
                "## 이 특허가 다루는 문제\n\n"
                "기존 기술은 성능과 비용 사이의 절충으로 어려움을 겪었다.\n")
        self._w("00-understand/figure-primer.md", "# Figure primer\n\nFIG. 1 overview.\n")
        self._w("00-understand/open-questions.md", "# Open questions\n\n- none\n")
        if confirmed:
            self._w("00-understand/understand-confirmed.md",
                    "# understand-confirmed\n\n"
                    "- **status**: %s\n"
                    "- **by**: %s\n"
                    "- **date**: %s\n"
                    "- **patent**: %s\n"
                    "- **notes**: %s\n"
                    % (status, by, date, patent or self.PATENT_ID, notes))

    def _accepted_double_clean(self, with_briefing=True, with_understand=True):
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
        self._w("03-edit/essay-final.md", self.CLEAN_ESSAY)
        self._w("03-edit/revision-notes.md", "## delta\n- self-audit fix\n")
        if with_briefing:
            self._write_owner_briefing()
        if with_understand:
            self._write_understand_complete()

    def test_double_clean_acceptance_passes(self):
        self._accepted_double_clean()
        r = check_run.check(self.root)  # defaults: double-clean + required confirm
        self.assertTrue(r["passed"], r["findings"])

    def test_single_pass_promotion_fails_double_clean(self):
        self._w("03-edit/edit-log.round-1.md", self.CLEAN_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("03-edit/essay-final.md", self.CLEAN_ESSAY)
        self._w("03-edit/revision-notes.md", "self-audit: no unresolved findings\n")
        self._write_owner_briefing()
        self._write_understand_complete()
        r = check_run.check(self.root, acceptance="double-clean")
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-005"))

    def test_single_clean_acceptance_passes_k1(self):
        self._w("03-edit/edit-log.round-1.md", self.CLEAN_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("03-edit/essay-final.md", self.CLEAN_ESSAY)
        self._w("03-edit/revision-notes.md", "self-audit: no unresolved findings\n")
        self._write_owner_briefing()
        self._write_understand_complete()
        r = check_run.check(self.root, acceptance="single-clean")
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "RUN-005"))

    def test_single_clean_rejects_dirty_round(self):
        self._w("03-edit/edit-log.round-1.md", self.FAIL_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("03-edit/essay-final.md", self.CLEAN_ESSAY)
        self._w("03-edit/revision-notes.md", "self-audit: no unresolved findings\n")
        self._write_owner_briefing()
        self._write_understand_complete()
        r = check_run.check(self.root, acceptance="single-clean")
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-005"))

    def test_single_clean_rejects_failed_gates(self):
        self._w("03-edit/edit-log.round-1.md", self.CLEAN_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_FAIL)
        self._w("03-edit/essay-final.md", self.CLEAN_ESSAY)
        self._w("03-edit/revision-notes.md", "self-audit: no unresolved findings\n")
        self._write_owner_briefing()
        self._write_understand_complete()
        r = check_run.check(self.root, acceptance="single-clean")
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-005"))

    def test_missing_disposition_fails(self):
        self._w("03-edit/edit-log.round-1.md", self.FAIL_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("02-compose/revision-response.round-1.md", "# Revision response\n(empty)\n")
        self._w("03-edit/edit-log.round-2.md", self.CLEAN_LOG.replace("pass\n", "pass\nr1-F1 ruled: fixed\n", 1))
        self._w("03-edit/gate-result.round-2.json", self.GATE_PASS)
        r = self._legacy()
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-003"))

    def test_dropped_carried_id_fails(self):
        self._w("03-edit/edit-log.round-1.md", self.FAIL_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("02-compose/revision-response.round-1.md", "## r1-F1\n- disposition: applied\n")
        self._w("03-edit/edit-log.round-2.md", self.CLEAN_LOG)  # never mentions r1-F1
        self._w("03-edit/gate-result.round-2.json", self.GATE_PASS)
        r = self._legacy()
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-004"))

    def test_cap_hit_promotion_warns_but_passes(self):
        # Authorized CAP HIT: score-history + valid cap-confirmed for K=2.
        # (Prior version encoded the broken no-authorizer path; RUN-013 now fires.)
        self._w("03-edit/edit-log.round-1.md", self.FAIL_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("02-compose/revision-response.round-1.md", "## r1-F1\n- disposition: applied\n")
        self._w("03-edit/edit-log.round-2.md",
                "overall_assessment: revise-required\n\nfindings:\n"
                "  - finding_id: r2-F1\n    pass: pass-3\n    severity: high\n"
                "    finding: \"r1-F1 persists\"\n")
        self._w("03-edit/gate-result.round-2.json", self.GATE_PASS)
        self._w("03-edit/essay-final.md", self.CLEAN_ESSAY)
        self._w("03-edit/score-history.md", "| 2 | ... |\nCAP HIT at max-iter; best round shipped.\n")
        self._w("03-edit/revision-notes.md", "self-audit: no unresolved findings\n")
        self._write_cap_confirmed(2)
        self._write_owner_briefing()
        self._write_understand_complete()
        r = check_run.check(self.root)
        self.assertTrue(r["passed"], r["findings"])
        self.assertTrue(_has(r, "RUN-006"))
        self.assertFalse(_has(r, "RUN-013"))

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
        self._accepted_double_clean(with_briefing=False, with_understand=False)
        # No briefing in design or understand → RUN-008
        r = self._legacy()
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-008"))

    def test_owner_briefing_whitespace_only_fails(self):
        self._accepted_double_clean(with_briefing=False, with_understand=False)
        self._write_owner_briefing(text="   \n\t\n  \n")
        r = self._legacy()
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
        self._w("03-edit/essay-final.md", self.CLEAN_ESSAY)
        self._w("03-edit/revision-notes.md", "self-audit: no unresolved findings\n")
        self._write_owner_briefing()
        self._write_understand_complete()
        r = check_run.check(self.root)
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "RUN-001"))
        self.assertFalse(_has(r, "RUN-003"))
        self.assertTrue(_has(r, "RUN-000"))  # informational confirmation-skip note

    def test_confirmation_veto_when_revision_response_exists(self):
        # VETO: revision-response.round-1.md present + confirmation wording on
        # round 2 → treat as REAL revision; RUN-003 must still run.
        self._w("03-edit/edit-log.round-1.md", self.FAIL_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("02-compose/revision-response.round-1.md",
                "# Revision response\n\n## r1-F1\n- disposition: applied\n")
        self._w("03-edit/edit-log.round-2.md",
                "# Edit Log - Round 2\n\n"
                "First clean → confirmation trigger next, NOT acceptance.\n\n"
                "overall_assessment: pass\n\n"
                "findings:\n  - pass: carried\n    finding: \"r1-F1 verified fixed\"\n")
        self._w("03-edit/gate-result.round-2.json", self.GATE_PASS)
        self._w("03-edit/score-history.md",
                "| round | round_type | assessment | gates | clean | notes |\n"
                "| 1 | revision | revise-required | pass | no | |\n"
                "| 2 | revision | pass | pass | yes | First clean → confirmation |\n")
        r = self._legacy()
        self.assertTrue(r["passed"], r["findings"])
        # Veto warn present; not a pure confirmation skip without response
        self.assertTrue(_has(r, "RUN-000"))
        veto_msgs = [f["message"] for f in r["findings"]
                     if f["check_id"] == "RUN-000" and "dispositive" in f["message"]]
        self.assertTrue(veto_msgs, r["findings"])

    def test_confirmation_veto_surfaces_missing_disposition(self):
        # Same shape as veto pass, but r1-F1 disposition missing → RUN-003 FAIL
        # (the gap the old heuristic would have masked).
        self._w("03-edit/edit-log.round-1.md", self.FAIL_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("02-compose/revision-response.round-1.md",
                "# Revision response\n(empty — no dispositions recorded)\n")
        self._w("03-edit/edit-log.round-2.md",
                "# confirmation round wording that would over-fire\n\n"
                "overall_assessment: pass\n\nr1-F1 ruled: ignored\n")
        self._w("03-edit/gate-result.round-2.json", self.GATE_PASS)
        r = self._legacy()
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-003"))

    def test_understand_study_pack_required_when_00_present(self):
        self._accepted_double_clean(with_understand=False)
        self._write_owner_briefing()
        os.makedirs(os.path.join(self.root, "00-understand"), exist_ok=True)
        self._w("00-understand/invention-summary.md", "# Invention Summary\n\nlayer\n")
        # study pack missing → RUN-009 (and RUN-011 if require_understand)
        r = self._legacy()
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-009"))
        self._w("00-understand/owner-study-pack.md",
                "# Owner Study Pack\n\n## 1. Problem\n\n"
                '**근거 (verbatim):**\n- `[0001]`: "sample verbatim line for fixture"\n')
        r2 = self._legacy()
        self.assertTrue(r2["passed"], r2["findings"])
        self.assertFalse(_has(r2, "RUN-009"))

    def test_prior_severity_notation_excluded_from_run003_and_run004(self):
        self._w("03-edit/edit-log.round-1.md", self.FAIL_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("02-compose/revision-response.round-1.md",
                "# Revision response\n\n## r1-F1\n\n- disposition: applied\n")
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
        self._w("03-edit/edit-log.round-3.md", self.CLEAN_LOG)
        self._w("03-edit/gate-result.round-3.json", self.GATE_PASS)
        r = self._legacy()
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "RUN-003"))
        self.assertFalse(_has(r, "RUN-004"))

    def test_genuinely_dropped_medium_still_fails(self):
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
        self._w("03-edit/edit-log.round-2.md",
                "overall_assessment: pass\n\ncarried_finding_rulings:\n\n"
                "  - finding_id: r1-F1\n"
                "    prior_severity: high\n"
                "    ruling: verified-landed\n"
                "    evidence: |\n"
                "      present in the current draft\n\n"
                "findings:\n  - pass: pass-1\n    finding: \"no further findings\"\n")
        self._w("03-edit/gate-result.round-2.json", self.GATE_PASS)
        r = self._legacy()
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-004"))

    # --- RUN-002 + threshold (previously untested) -------------------------

    def test_run002_missing_overall_assessment(self):
        self._w("03-edit/edit-log.round-1.md",
                "findings:\n  - pass: pass-1\n    finding: \"no assessment field\"\n")
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        r = self._legacy()
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-002"))

    def test_run002_unreadable_gate_json(self):
        self._w("03-edit/edit-log.round-1.md", self.CLEAN_LOG)
        self._w("03-edit/gate-result.round-1.json", "{not valid json!!!")
        r = self._legacy()
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-002"))

    def test_threshold_revise_recommended_accepts_that_assessment(self):
        self._w("03-edit/edit-log.round-1.md",
                "overall_assessment: revise-recommended\n\nfindings:\n"
                "  - pass: pass-1\n    finding: \"soft pass\"\n")
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("02-compose/revision-response.round-1.md",
                "# Revision response\n(no medium+ findings)\n")
        self._w("03-edit/edit-log.round-2.md",
                "overall_assessment: revise-recommended\n\nfindings:\n"
                "  - pass: carried\n    finding: \"still soft\"\n")
        self._w("03-edit/gate-result.round-2.json", self.GATE_PASS)
        self._w("03-edit/essay-final.md", self.CLEAN_ESSAY)
        self._w("03-edit/revision-notes.md", "self-audit: no unresolved findings\n")
        self._write_owner_briefing()
        self._write_understand_complete()
        r_strict = check_run.check(self.root, threshold="pass")
        self.assertFalse(r_strict["passed"])
        self.assertTrue(_has(r_strict, "RUN-005"))
        r_soft = check_run.check(self.root, threshold="revise-recommended")
        self.assertTrue(r_soft["passed"], r_soft["findings"])

    # --- RUN-010 owner confirm ---------------------------------------------

    def test_run010_valid_confirm_passes(self):
        self._accepted_double_clean()
        r = check_run.check(self.root, owner_confirm="required")
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "RUN-010"))

    def test_run010_missing_confirm_fails(self):
        self._accepted_double_clean(with_understand=True)
        os.unlink(os.path.join(self.root, "00-understand", "understand-confirmed.md"))
        r = check_run.check(self.root, owner_confirm="required")
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-010"))

    def test_run010_placeholder_date_fails(self):
        self._accepted_double_clean(with_understand=False)
        self._write_understand_complete(date="<YYYY-MM-DD>")
        r = check_run.check(self.root, owner_confirm="required")
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-010"))

    def test_run010_status_pending_fails(self):
        self._accepted_double_clean(with_understand=False)
        self._write_understand_complete(status="pending")
        r = check_run.check(self.root, owner_confirm="required")
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-010"))

    def test_run010_patent_mismatch_fails(self):
        self._accepted_double_clean(with_understand=False)
        self._write_understand_complete(patent="US0000000A1")
        r = check_run.check(self.root, owner_confirm="required")
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-010"))

    def test_run010_off_skips(self):
        self._accepted_double_clean(with_understand=False)
        # five files for RUN-011 off path; no confirm file. Invention-summary
        # must still carry a Quotable span so RUN-015 recheck does not invent
        # QUOTE-002 noise on this RUN-010-focused fixture.
        os.makedirs(os.path.join(self.root, "00-understand"), exist_ok=True)
        for name in ("owner-study-pack.md", "owner-briefing.md",
                     "figure-primer.md", "open-questions.md"):
            self._w("00-understand/" + name, "# ok\nbody\n")
        self._w("00-understand/invention-summary.md",
                "# Invention Summary\n\n## Quotable spans\n"
                '- `[0001]`: "sample verbatim line for fixture"\n')
        self._write_owner_briefing()
        r = check_run.check(self.root, owner_confirm="off", require_understand=False)
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "RUN-010"))

    def test_run010_yes_flag_requires_orchestrator(self):
        self._accepted_double_clean(with_understand=False)
        self._write_understand_complete(by="owner")
        r = check_run.check(self.root, owner_confirm="yes-flag")
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-010"))
        self._write_understand_complete(by="orchestrator-yes-flag",
                                        notes='"--yes unattended"')
        r2 = check_run.check(self.root, owner_confirm="yes-flag")
        self.assertTrue(r2["passed"], r2["findings"])

    def test_run010_confirm_patent_unverifiable_warns(self):
        """Confirm patent set but no run-side id derivable → no RUN-010 fail;
        RUN-000 warn. The manifest stays hash-consistent with input/patent.md
        (so RUN-012 is satisfied), but neither the manifest nor the patent text
        yields a patent number, so the patent-match clause cannot run."""
        import hashlib
        self._accepted_double_clean(with_understand=False)
        # Rewrite input/patent.md to id-less text and a manifest with no
        # `patent:` field, kept hash-consistent so RUN-012 passes.
        patent_path = os.path.join(self.run_root, "input", "patent.md")
        with open(patent_path, "w", encoding="utf-8") as fh:
            fh.write("# Fixture Patent\n\nno recognizable publication number here\n")
        h = hashlib.sha256(open(patent_path, "rb").read()).hexdigest()
        self._w("run-manifest.md",
                "# run-manifest\n\n- **run_id**: fixture-run\n"
                "- **patent_sha256**: %s\n- **profile**: publish\n"
                "- **started**: 2026-07-10\n" % h)
        self._write_understand_complete(patent="US1234567B2")
        r = check_run.check(self.root, owner_confirm="required",
                            recheck_gates=False)  # isolate RUN-010 softening
        self.assertFalse(_has(r, "RUN-010"), r["findings"])
        self.assertFalse(_has(r, "RUN-012"), r["findings"])
        self.assertTrue(r["passed"], r["findings"])
        msgs = [f["message"] for f in r["findings"] if f["check_id"] == "RUN-000"]
        self.assertTrue(
            any("US1234567B2" in m and "unverifiable" in m for m in msgs),
            msgs,
        )

    def test_run010_empty_patent_fails(self):
        """Empty patent: field is mandatory — RUN-010 fail regardless of derivability."""
        self._accepted_double_clean(with_understand=False)
        self._write_understand_complete(confirmed=False)
        self._w("00-understand/understand-confirmed.md",
                "# understand-confirmed\n\n"
                "- **status**: confirmed\n"
                "- **by**: owner\n"
                "- **date**: 2026-07-10\n"
                "- **patent**: \n"
                "- **notes**: \"owner confirmed triad\"\n")
        r = check_run.check(self.root, owner_confirm="required")
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-010"))
        msgs = [f["message"] for f in r["findings"] if f["check_id"] == "RUN-010"]
        self.assertTrue(any("patent" in m.lower() for m in msgs), msgs)

    # --- newline-swallowing field parsers (WS-B follow-up 2) ---------------

    def _confirm_text(self, **fields):
        """Build a confirm-file body; omit a key or pass '' for empty value."""
        defaults = {
            "status": "confirmed",
            "by": "owner",
            "date": "2026-07-10",
            "patent": "US9999999B2",
            "notes": '"ok"',
        }
        defaults.update(fields)
        lines = ["# understand-confirmed", ""]
        for key in ("status", "by", "date", "patent", "notes"):
            lines.append("- **%s**: %s" % (key, defaults[key]))
        return "\n".join(lines) + "\n"

    def test_validate_empty_patent_no_ids_fails(self):
        """Exploit path: empty patent: + patent_ids=[] must fail closed."""
        text = self._confirm_text(patent="")
        ok, msg, _warn = check_run._validate_understand_confirmed(
            text, [], "required")
        self.assertFalse(ok, msg)
        self.assertIn("patent", msg.lower())

    def test_validate_whitespace_only_patent_fails(self):
        text = self._confirm_text(patent="   ")
        ok, msg, _warn = check_run._validate_understand_confirmed(
            text, [], "required")
        self.assertFalse(ok, msg)
        self.assertIn("patent", msg.lower())

    def test_validate_empty_date_fails(self):
        text = self._confirm_text(date="")
        ok, msg, _warn = check_run._validate_understand_confirmed(
            text, ["US9999999B2"], "required")
        self.assertFalse(ok, msg)
        self.assertIn("date", msg.lower())
        # Must not have swallowed the next line's leading "-" as the value.
        self.assertNotIn("'-'", msg)
        self.assertNotIn('"-"', msg)

    def test_validate_empty_by_fails(self):
        text = self._confirm_text(by="")
        ok, msg, _warn = check_run._validate_understand_confirmed(
            text, ["US9999999B2"], "required")
        self.assertFalse(ok, msg)
        self.assertIn("by", msg.lower())
        self.assertNotIn("'-'", msg)
        self.assertNotIn('"-"', msg)

    def test_validate_empty_status_fails(self):
        text = self._confirm_text(status="")
        ok, msg, _warn = check_run._validate_understand_confirmed(
            text, ["US9999999B2"], "required")
        self.assertFalse(ok, msg)
        self.assertIn("status", msg.lower())
        self.assertNotIn("'-'", msg)
        self.assertNotIn('"-"', msg)

    def test_run010_empty_patent_no_run_side_id_fails(self):
        """E2E: empty patent: with no input/patent.md must surface RUN-010 fail."""
        self._accepted_double_clean(with_understand=False)
        patent_path = os.path.join(self.run_root, "input", "patent.md")
        os.unlink(patent_path)
        self._write_understand_complete(confirmed=False)
        self._w("00-understand/understand-confirmed.md",
                "# understand-confirmed\n\n"
                "- **status**: confirmed\n"
                "- **by**: owner\n"
                "- **date**: 2026-07-10\n"
                "- **patent**:\n"
                "- **notes**: \"owner confirmed triad\"\n")
        r = check_run.check(self.root, owner_confirm="required")
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-010"), r["findings"])
        msgs = [f["message"] for f in r["findings"] if f["check_id"] == "RUN-010"]
        self.assertTrue(any("patent" in m.lower() for m in msgs), msgs)

    def test_shipped_template_confirm_fails_validation(self):
        """Shipped template (all values empty / status pending) must fail closed."""
        template_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "..", "..",
            "handoff-template", "00-understand", "understand-confirmed.md",
        )
        template_path = os.path.normpath(template_path)
        if os.path.isfile(template_path):
            text = open(template_path, encoding="utf-8").read()
        else:
            text = (
                "# understand-confirmed\n\n"
                "- **status**: pending          # confirmed | pending\n"
                "- **by**:                      # owner | orchestrator-yes-flag\n"
                "- **date**:                    # YYYY-MM-DD (real date)\n"
                "- **patent**:                  # identifier from input/patent.md\n"
                "- **notes**:                   # REQUIRED when by: owner\n"
            )
        ok, msg, _warn = check_run._validate_understand_confirmed(
            text, [], "required")
        self.assertFalse(ok, msg)

    def test_patent_ids_match_rejects_truncated_prefix(self):
        self.assertFalse(
            check_run._patent_ids_match("US999", "US9999999B2"))

    def test_patent_ids_match_kind_code_core(self):
        self.assertTrue(
            check_run._patent_ids_match("US9999999", "US9999999B2"))

    def test_patent_ids_match_slash_form(self):
        self.assertTrue(
            check_run._patent_ids_match(
                "US 2025/0266395 A1", "US20250266395A1"))

    # --- RUN-011 require understand ----------------------------------------

    def test_run011_missing_five_fails_when_required(self):
        self._accepted_double_clean(with_understand=False)
        self._write_owner_briefing()
        r = check_run.check(self.root, owner_confirm="off", require_understand=True)
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-011"))

    def test_run011_complete_passes(self):
        self._accepted_double_clean()
        r = check_run.check(self.root, require_understand=True)
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "RUN-011"))

    def test_run011_off_allows_legacy(self):
        self._accepted_double_clean(with_understand=False)
        self._write_owner_briefing()
        r = check_run.check(self.root, owner_confirm="off", require_understand=False)
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "RUN-011"))
        self.assertTrue(_has(r, "RUN-000"))  # legacy layout warn

    # --- RUN-012 patent hash -----------------------------------------------

    def test_run012_absent_manifest_fails_when_owner_confirm_on(self):
        # A design-or-beyond run under owner-confirm cannot silence the patent
        # lock by deleting run-manifest.md: absent manifest is a hard fail.
        self._accepted_double_clean()
        os.remove(os.path.join(self.root, "run-manifest.md"))
        r = check_run.check(self.root)  # default owner_confirm="required"
        self.assertFalse(r["passed"], r["findings"])
        self.assertTrue(_has(r, "RUN-012"))

    def test_run012_absent_manifest_warns_on_legacy_reverify(self):
        # Legacy archive re-verification (owner_confirm off) keeps the warn path.
        self._accepted_double_clean()
        os.remove(os.path.join(self.root, "run-manifest.md"))
        r = check_run.check(self.root, owner_confirm="off")
        msgs = [f["message"] for f in r["findings"] if f["check_id"] == "RUN-000"]
        self.assertTrue(any("run-manifest" in m for m in msgs), msgs)

    def test_run012_match_passes(self):
        # setUp already wrote a matching manifest; a compliant tree passes clean.
        self._accepted_double_clean()
        r = check_run.check(self.root)
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "RUN-012"))

    def test_run012_mismatch_fails(self):
        self._accepted_double_clean()
        self._w("run-manifest.md",
                "# run-manifest\n\n- **run_id**: fixture-run\n"
                "- **patent**: %s\n- **patent_sha256**: %s\n"
                "- **profile**: publish\n- **started**: 2026-07-10\n"
                % (self.PATENT_ID, "0" * 64))
        r = check_run.check(self.root)
        self.assertFalse(r["passed"], r["findings"])
        self.assertTrue(_has(r, "RUN-012"))

    def test_run012_mismatch_fails(self):
        self._accepted_double_clean()
        self._w("run-manifest.md",
                "# run-manifest\n\n"
                "- **run_id**: fixture-run\n"
                "- **patent**: %s\n"
                "- **patent_sha256**: %s\n"
                "- **profile**: publish\n"
                "- **started**: 2026-07-10\n"
                % (self.PATENT_ID, "0" * 64))
        r = check_run.check(self.root)
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-012"))

    # --- RUN-013 CAP HIT authorizer ----------------------------------------

    def _cap_hit_tree(self, with_cap_confirm=False, cap_round=2):
        self._w("03-edit/edit-log.round-1.md", self.FAIL_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        self._w("02-compose/revision-response.round-1.md",
                "## r1-F1\n- disposition: applied\n")
        self._w("03-edit/edit-log.round-2.md",
                "overall_assessment: revise-required\n\nfindings:\n"
                "  - finding_id: r2-F1\n    pass: pass-3\n    severity: high\n"
                "    finding: \"r1-F1 persists\"\n")
        self._w("03-edit/gate-result.round-2.json", self.GATE_PASS)
        self._w("03-edit/essay-final.md", self.CLEAN_ESSAY)
        self._w("03-edit/score-history.md",
                "| 2 | ... |\nCAP HIT at max-iter; best round shipped.\n")
        self._w("03-edit/revision-notes.md",
                "self-audit: no unresolved findings\n")
        self._write_owner_briefing()
        self._write_understand_complete()
        if with_cap_confirm:
            self._write_cap_confirmed(cap_round)

    def test_run013_unauthorized_cap_hit_fails(self):
        self._cap_hit_tree(with_cap_confirm=False)
        r = check_run.check(self.root, owner_confirm="required")
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-013"), r["findings"])

    def test_run013_authorized_cap_hit_no_run013(self):
        self._cap_hit_tree(with_cap_confirm=True, cap_round=2)
        r = check_run.check(self.root, owner_confirm="required")
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "RUN-013"))
        self.assertTrue(_has(r, "RUN-006"))

    def test_run013_wrong_round_fails(self):
        self._cap_hit_tree(with_cap_confirm=True, cap_round=1)  # K=2
        r = check_run.check(self.root, owner_confirm="required")
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-013"), r["findings"])
        msgs = [f["message"] for f in r["findings"] if f["check_id"] == "RUN-013"]
        self.assertTrue(any("round" in m.lower() for m in msgs), msgs)

    def test_run013_owner_confirm_off_skips(self):
        self._cap_hit_tree(with_cap_confirm=False)
        r = check_run.check(self.root, owner_confirm="off",
                           require_understand=False)
        self.assertFalse(_has(r, "RUN-013"), r["findings"])

    def test_run013_owner_notes_required(self):
        self._cap_hit_tree(with_cap_confirm=False)
        self._w("03-edit/cap-confirmed.md",
                "# cap-confirmed\n\n"
                "- **status**: confirmed\n"
                "- **by**: owner\n"
                "- **date**: 2026-07-10\n"
                "- **round**: 2\n"
                "- **notes**:\n")
        r = check_run.check(self.root, owner_confirm="required")
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-013"))
        msgs = [f["message"] for f in r["findings"] if f["check_id"] == "RUN-013"]
        self.assertTrue(any("notes" in m.lower() for m in msgs), msgs)

    # --- RUN-014 self-declared clean with findings -------------------------

    def test_run014_dirty_pass_fails(self):
        self._w("03-edit/edit-log.round-1.md", self.DIRTY_PASS_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        r = self._legacy()
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-014"), r["findings"])

    def test_run014_clean_pass_no_finding(self):
        self._w("03-edit/edit-log.round-1.md", self.CLEAN_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        r = self._legacy()
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "RUN-014"))

    def test_run014_revise_with_findings_no_run014(self):
        # Honest dirty assessment is not RUN-014 (that is RUN-005 territory
        # when promoted).
        self._w("03-edit/edit-log.round-1.md", self.FAIL_LOG)
        self._w("03-edit/gate-result.round-1.json", self.GATE_PASS)
        r = self._legacy()
        self.assertFalse(_has(r, "RUN-014"), r["findings"])

    # --- RUN-015 gate recheck on accepted essay ----------------------------

    def test_run015_lying_gate_json_fails(self):
        self._accepted_double_clean()
        self._w("03-edit/essay-final.md", self.DIRTY_ESSAY)  # BANNED-001
        # Last round JSON still claims passed=true
        self._w("03-edit/gate-result.round-3.json", self.GATE_PASS)
        r = check_run.check(self.root, recheck_gates=True)
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "RUN-015"), r["findings"])

    def test_run015_consistent_tree_no_finding(self):
        self._accepted_double_clean()
        r = check_run.check(self.root, recheck_gates=True)
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "RUN-015"))

    def test_run015_no_recheck_flag_skips(self):
        self._accepted_double_clean()
        self._w("03-edit/essay-final.md", self.DIRTY_ESSAY)
        self._w("03-edit/gate-result.round-3.json", self.GATE_PASS)
        r = check_run.check(self.root, recheck_gates=False)
        self.assertFalse(_has(r, "RUN-015"), r["findings"])
        # Still may fail other rules? DIRTY essay alone isn't a RUN-00x fail.
        # Without recheck, lying JSON is invisible → pass on that dimension.
        self.assertTrue(r["passed"], r["findings"])


class TestPatentLeak(unittest.TestCase):
    """LEAK-001: draft must not paste raw patent outside Quotable spans."""

    PATENT = (
        "The present invention provides a novel rotor assembly that includes a "
        "plurality of blades arranged in a circumferential pattern around a "
        "central hub structure for improved airflow management under high load.\n"
    )
    SPAN = (
        "a novel rotor assembly that includes a plurality of blades arranged "
        "in a circumferential pattern around a central hub"
    )

    def test_leak_raw_paragraph_fails(self):
        import gate_patent_leak
        draft = (
            "# Title\n\n"
            + self.PATENT
            + "\n# Sources\n- US1\n"
        )
        summary = "# Invention Summary\n\nNo quotable spans listed.\n"
        r = gate_patent_leak.check(draft, {
            "patent_text": self.PATENT,
            "invention_summary_text": summary,
        })
        self.assertFalse(r["passed"])
        self.assertTrue(_has(r, "LEAK-001"), r["findings"])

    def test_covered_span_quote_passes(self):
        import gate_patent_leak
        draft = (
            "# Title\n\n"
            'As recorded in the summary, "%s".\n\n'
            "# Sources\n- US1\n"
        ) % self.SPAN
        summary = (
            "# Invention Summary\n\n"
            '- `[0001]`: "%s"\n'
        ) % self.SPAN
        r = gate_patent_leak.check(draft, {
            "patent_text": self.PATENT,
            "invention_summary_text": summary,
        })
        self.assertTrue(r["passed"], r["findings"])
        self.assertFalse(_has(r, "LEAK-001"))

    def test_missing_context_warn_skip(self):
        import gate_patent_leak
        draft = "# Title\n\n" + self.PATENT + "\n# Sources\n- US1\n"
        r = gate_patent_leak.check(draft, {})
        self.assertTrue(r["passed"])  # warn-skip, not vacuous fail
        self.assertTrue(_has(r, "LEAK-000"))
        self.assertFalse(_has(r, "LEAK-001"))

    def test_registered_in_run_gates(self):
        names = [m.GATE_ID if hasattr(m, "GATE_ID") else m.__name__
                 for m in run_gates.GATES]
        self.assertIn("patent_leak", names)

    def test_run_gates_only_runs_leak_with_both_context(self):
        """Absent patent/summary → LEAK-000 warn, no LEAK-001; both present → can fire."""
        draft = (
            "# Title\n\n"
            + self.PATENT
            + "\n# Sources\n- US1\n"
        )
        overall, results = run_gates.run_all(draft, {"mode": "essay"})
        leak = next(r for r in results if r["gate"] == "patent_leak")
        self.assertTrue(any(f["check_id"] == "LEAK-000" for f in leak["findings"]))
        self.assertFalse(any(f["check_id"] == "LEAK-001" for f in leak["findings"]))

        summary = "# Invention Summary\n\nNo quotable spans.\n"
        overall2, results2 = run_gates.run_all(draft, {
            "mode": "essay",
            "patent_text": self.PATENT,
            "invention_summary_text": summary,
        })
        leak2 = next(r for r in results2 if r["gate"] == "patent_leak")
        self.assertFalse(leak2["passed"])
        self.assertTrue(any(f["check_id"] == "LEAK-001" for f in leak2["findings"]))
        self.assertFalse(overall2)


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
