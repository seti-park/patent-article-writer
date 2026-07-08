# External fact verification

Referenced by editorial-review SKILL.md (Pass 3 sub-pass) and by essay-architect references/context-research.md (Step 1). Cross-skill shared SoT: both skills consult the 5-tier hierarchy below.

## Scope

External factual claims are facts outside the patent's own paragraph attribution. These include:

- Named entity attributes: people's credentials, company history, executive bio claims
- Industry statistics, citation counts, market share figures
- Prior publication references (academic papers, conference talks)
- Competitor or third-party technology claims
- Dates and events (acquisitions, product launches, regulatory actions)

Patent-internal claims (paragraph attribution `[xxxx]`) belong to deterministic-gate CheckID 2, not this sub-pass.

## 5-tier source authority hierarchy

| Tier | Source type | Examples |
|---|---|---|
| Tier 1 | Company official + government primary documents | Press releases, IR pages, SEC filings, official spec sheets, government registries, on-record executive statements |
| Tier 2 | Patents + peer-reviewed papers + standards bodies | Granted patents, published applications, Nature / Science / IEEE / ACM papers, standards body specifications |
| Tier 3 | Mainstream news with editorial process | Reuters, Bloomberg, FT, WSJ, NYT, Nikkei, named-author bylines at established outlets |
| Tier 4 | Industry outlets + reverse-engineered analysis | Electrek, Teslarati, The Information, named-author analyst blogs, tear-down / reverse-engineering reports |
| Tier 5 | Personal blogs, social media, anonymous forums | Twitter / X posts, Reddit threads, anonymous blog posts, unattributed leaks |

## Verification rule per claim type

- **Competitor or third-party technology claim**. Minimum Tier 2 source required. That company's official statement, registered patent, or peer-reviewed paper. Tier 3 news media alone is insufficient.
- **Applicant info or corporate strategy claim**. Tier 1 preferred. Company's own official statement, press release, IR page, or SEC filing.
- **Time-sensitive event claim** (launches, acquisitions, regulatory actions). Tier 1 + Tier 3 cross-check.
- **Technical mechanism claim**. Tier 2 preferred (patent or peer-reviewed paper). Tier 4 reverse-engineered analysis allowed only with explicit hedge language.
- **Personal credentials or bio claim**. Tier 1 (company bio page, official statement) or Tier 2 (academic profile). Tier 5 (LinkedIn self-description) as backup only.
- **Tier 5 sources** as the sole anchor are disqualified for factual claims. They may serve as backup pointers under Tier 1-4 anchors only.

## Verification approach

When Pass 3 reaches a sub-pass 3.5 candidate:

1. **Identify the claim**: extract the specific factual assertion (named entity + attribute, statistic + value, date + event).
2. **Locate the staged fact-base entry**: patent-reader's pool admission stage stores candidate facts. Sub-pass 3.5 re-verifies, not re-discovers.
3. **Identify the source tier** of every source the fact-base entry cites.
4. **Web-search re-verify**: even verified entries get a fresh check at editorial-review stage. Source rot (URL dead, claim retracted, page updated) is the failure pattern this stage catches.
5. **Cross-check across tiers** when the claim is time-sensitive or competitor-related.
6. **Set verification status** (next section).

The motivation for re-verification at editorial-review stage: patent-reader's staged entries may be weeks old. The final trust check belongs at the publication threshold.

## Verification status

| Status | Condition | Action |
|---|---|---|
| verified | Tier 1-2 anchor + recent (within 1 year) | Proceed. |
| partially-verified | Tier 3-4 anchor + recent. OR Tier 1-2 anchor + outdated. | Hedge language required, or re-anchor to Tier 1-2 fresh source. |
| unverifiable | Tier 5 only. OR all sources conflict. OR no fresh source. | Remove claim or downgrade to qualified statement. |
| contradicted | Fresh verify shows essay's claim differs from authoritative source | Fix required before publication. |

## Severity per posture

| Posture | Severity |
|---|---|
| aggressive | medium (forward-looking framing has priority) |
| measured | medium (factual accuracy matters) |
| conservative | critical (factual accuracy absolute priority) |

Exception: Tier 5 only anchor combined with a quantitative claim: high severity across all postures. Quantitative claims (percentages, dollar figures, time durations, counts) anchored only at Tier 5 carry archetype risk regardless of posture.

## Competitor-technology defense

Competitor or third-party technology claims warrant Tier 2 minimum. The specific failure pattern this rule prevents:

- Industry outlet (Tier 4) publishes reverse-engineered analysis of competitor product
- Essay cites the analysis as factual claim about competitor technology
- Source's underlying methodology was inference from packaging photos / leaked images, not the company's own disclosure
- Competitor later releases differing official documentation
- Essay's factual claim about competitor is now contradicted

Defense: require the competitor's own statement, registered patent, or peer-reviewed publication. If only Tier 4 reverse-engineering exists, the prose must explicitly attribute to the outlet's reverse-engineering, not state as factual claim about the competitor.

## Failure case patterns

### Pattern 1: Credential drift

Essay cites person's affiliation as a single block ("15 years at IBM Research"). Web search re-verify reveals the true history splits across two divisions ("IBM EDA Lab 2000-2006, then IBM Research 2007-2015"). The 15-year count is correct but the affiliation specificity is wrong.

Fix: refine the prose to the verified split. Often improves the essay's credibility because the specificity itself is a trust signal.

### Pattern 2: Peripheral source attached as thesis anchor

Essay cites a high-profile academic paper (e.g., Nature 2021) as supporting evidence. Web search re-verify shows the paper covers a related but distinct domain, and the essay's thesis does not actually rest on the paper's conclusions.

Fix: remove the peripheral citation. Thesis must anchor on sources whose claims are directly load-bearing. Peripheral citations dilute trust because they invite reader scrutiny of the connection.

### Pattern 3: Industry blog cited as factual claim

Essay states a competitor's technology specification as fact. The cited source is a Tier 4 industry blog's reverse-engineering. The competitor has not confirmed the specification.

Fix: either find Tier 2 source (competitor's own filing, patent, or paper) or rewrite the prose to attribute the claim to the blog's analysis explicitly ("Electrek's tear-down suggests…" rather than "Company X's system uses…").

## Cross-skill relationship with essay-architect

essay-architect Step 1 (Context research) consults this hierarchy when deciding which external sources to admit to the fact pool. editorial-review Pass 3 sub-pass 3.5 consults the same hierarchy when re-verifying admitted sources at the publication threshold.

This is the intended cross-skill share: single SoT, two consumers at different pipeline stages. essay-architect's context-research.md carries a short summary pointing here; this file holds the full hierarchy + verification logic.
