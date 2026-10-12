---
handoff: tiering-assessment
handoff_version: 1
release_id: <roadmap id, e.g. RL-500>
title: <release title as on the roadmap>
assessed: <YYYY-MM-DD>
rubric_version: <e.g. v1>
path: <full | routine>
tier: <1 | 2 | 3 | 4>
tier_job: <Tell the market | Tell customers and sales | Tell the customers it serves | Log it>
total: <0 to 100>
borderline: <true | false>
provisional: <true | false>
provisional_reason: <e.g. maturity below 5; empty if not provisional>
gates:
  maturity: <0 to 10>
  revenue: <passed | failed>
overrides: <none, or a list: big_deal | market_date, from tier, to tier>
competitor_flag: <true | false>
status: <draft | approved>
decided_by: <name, once approved>
decided_on: <YYYY-MM-DD, once approved>
leadership_signoff: <not needed | pending | given>
previous_assessment: <none | YYYY-MM-DD>
rescore_trigger: <none | scope | date | results | maturity | deal | market_date | competitor>
---

<!--
Template for one tiering assessment. The agent writes a new copy for every assessment, named
tiering-YYYY-MM-DD.md, in launches/<release id>-<short name>/01-tiering/. Nothing is overwritten.
The header above is what the next agent reads; the sections below are for people.
Everything in <angle brackets> is replaced. Delete this comment in a real assessment.
-->

# <Release id>: <title>

_Tiering assessment, <date>. Rubric <version>. <Full path | Routine path>. Status: <draft | approved>._

## 1. Recommendation

**Tier <n>: <tier job>.** Total <nn> of 100.

- **Line:** <nn> points <above | below> the Tier <n> line at <nn>. <Borderline: within 3 points, so it stays in the lower tier unless the reason to move up is clear. | Not borderline.>
- **Maturity gate:** <score>. <Passed: the tier stands. | Below 5: the tier is provisional, and the release is scored again when it is ready to test with customers.>
- **Revenue gate:** <Passed: it opens a new revenue stream or helps win or expand deals. | Failed: Tier 3 at most, whatever the score.>
- **Overrides:** <None. | Big deal: <deal> depends on it, moved from Tier <n> to Tier <n>, approved by <name> on <date>. | Market date: <date and what it is>, moved from Tier <n> to Tier <n>, approved by <name> on <date>.>
- **Competitor:** <None found. | <Competitor> launched the same thing on <date>: the message says catching up, not first; the tier is unchanged.>

## 2. Scores

_Points = settled score × weight. On the routine path, "Your score" stays empty unless you move the release to the full path._

| # | Question | Weight | Your score | Agent score | Gap | Settled | Points | Evidence, strongest first | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | New category | 2 | <0 to 10> | <0 to 10> | <n> | <0 to 10> | <0 to 20> | <one line> | <file, date> |
| 2 | Market need | 2 | | | | | <0 to 20> | | |
| 3 | Validation | 1.5 | | | | | <0 to 15> | | |
| 4 | Strategic signals | 1.5 | | | | | <0 to 15> | | |
| 5 | Customer request | 1 | | | | | <0 to 10> | | |
| 6 | Market expectation | 1 | | | | | <0 to 10> | | |
| 7 | Customer reach | 1 | | | | | <0 to 10> | | |
| | **Total** | **10** | | | | | **<0 to 100>** | | |

| Gate | Answer | Evidence | Source |
|---|---|---|---|
| Development maturity | <0 to 10: scoping, ready to test with customers, ready for customers to use> | <one line> | <file, date> |
| Revenue | <passed | failed> | <new revenue stream, or the deals it helps win or expand> | <file, date> |

**Where sources disagreed:** <None. | <Source A> says <x> (<date>); <source B> says <y> (<date>). The rule picks <A | B> because <newest statement from the owner | newer conversation | a summary never beats its source>. <It would change the tier, so it is raised in section 4.>>

## 3. Explainer for the PM

_What product marketing takes to the product manager. Plain words, no rubric vocabulary._

**<Tier n>: <tier job>.** <One sentence: what this release is and why it gets this kind of launch.>

**Why, in three reasons**

1. **<Question that adds the most points>** (<points> of <max>). <Why this counts, from the weight's reason.> <The evidence, in one line.>
2. **<Second>** (<points> of <max>). <Why it counts.> <The evidence.>
3. **<Third, or a gate or override if it decided the tier>.** <Why it counts.> <The evidence.>

**What would change it**

- <nn> points from the Tier <n> line. <A score of <n> on <question> instead of <n> would move it.>
- <Coming event that would trigger a rescore, with its date: early access opens, a deal closes, a regulation date.>

**Questions for you**

1. <One question per score that rests on thin evidence.>
2. <...>

**If the tier holds:** <lead time>, led by <who>, heard by <who>. The full list is in section 6.

## 4. Where more information would help

| Question | Why the evidence is thin | What would firm it up | Who has it |
|---|---|---|---|
| <question> | <e.g. one customer request, no deal named it> | <e.g. the pipeline export for the quarter> | <name or team> |

## 5. Decision

| | |
|---|---|
| Gaps settled (3 points or more) | <question: kept your score, took the agent's, or left open for the PM. For any score you changed: what changed your mind, or "no reason given". Cause noted for calibration (missing source, anchor read two ways, weight, results after release)> |
| Product manager's input | <name, date, their answers to the explainer's questions; or "not asked: decided without them, because ...". The agent never answers for the PM> |
| Borderline call | <none, or the decision and the written reason> |
| Overrides approved | <none, or which, by whom, when, why> |
| **Decision** | **Tier <n>, by <name>, <date>** |
| Leadership sign off | <not needed, or by whom and when (Tier 1)> |
| For the next calibration review | <causes noted, or none> |

## 6. What this tier sets in motion

_The row for this tier from the trigger table in `data/rubric.md`._

| How often | Lead time | Who leads | Who hears about it | Assets |
|---|---|---|---|---|
| <from the rubric> | <from the rubric> | <from the rubric> | <from the rubric> | <from the rubric> |

**For this release:** <launch date or target>, so work starts by <date>.

## 7. Changes since the last assessment

<None: first assessment. | Compared with <date of previous assessment>:>

| What changed | Trigger | Before | After |
|---|---|---|---|
| <e.g. early access opened> | <maturity> | <tier, total, provisional> | <tier, total, provisional> |
