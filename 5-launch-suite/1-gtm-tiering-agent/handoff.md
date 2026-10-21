# GTM Tiering Agent: the handoff

_Version 2, 21 Oct 2026: adds `ship_date` and `added_from_higher_tier` to the assessment's header, and the weekly list's rows. Version 1 files stay valid. What the agent writes, and what people and the next agents can rely on. The checker `tools/check_assessment.py` tests every file against this page._

## Who reads it

| Reader | Reads | For |
|---|---|---|
| Product marketing | The whole file, sections 1 to 7 | Deciding the tier, taking the explainer to the PM, starting the launch work |
| The product manager | Section 3, the explainer | Answering the questions; knowing what the tier sets in motion |
| Launch Brief (agent 2) | The header (above all `tier`, `status`, `provisional`, `competitor_flag`, `ship_date`, `added_from_higher_tier`), section 2's evidence and sources, section 3 | Starting the launch brief: the tier sets how much it covers, and an added asset becomes its own section |
| The Launch Brief, for any tier | Every approved weekly list that mentions the release | The history before and after the tier was decided |
| The Launch Brief's monthly note | Approved weekly lists: the routine rows at Tier 4, with their ship dates. Approved full path assessments at Tier 4, with their `ship_date` | One note a month for the month's Tier 4 releases |
| Goal setter (agent 3) | The header (tier, total, gates) | Setting goals that fit the size of the launch |
| Launch planner (agent 4) | The header and section 6, the trigger table row | Lead time, who leads, who hears, which assets |

## Where the files are

```
launches/
  <release id>-<short name>/
    01-tiering/
      evidence-YYYY-MM-DD.md       step 1, no scores; for the PMM to score from
      agent-scores-YYYY-MM-DD.md   the agent's scores, sealed before the PMM scores
      tiering-YYYY-MM-DD.md        the assessment: the handoff file
    02-brief/                      written by the Launch Brief agent
  weekly/tiering-YYYY-Www.md       the Monday list
  weekly/scores-YYYY-Www.md        the agent's scores for that week's releases
  calibration/calibration-YYYY-MM-DD.md
```

## Which file is current

- **The newest `tiering-*.md` with `status: approved` is the current tier.** Nothing is overwritten; a rescore is a new dated file whose `previous_assessment` names the one before.
- **A draft is never handed on.** If the newest file is a draft, the next agent says so ("a tiering draft from 5 October is waiting for product marketing") and uses the newest approved one, if there is one, or stops.
- **A provisional tier is handed on, marked.** The next agent repeats the provisional reason and plans to the rescore date, not past it.

## The header

YAML between the first two `---` lines. Every field is required; an empty value is written as nothing after the colon.

| Field | Values | Meaning |
|---|---|---|
| `handoff` | `tiering-assessment` | What kind of file this is |
| `handoff_version` | `1` or `2` | Changes only when a field is added, removed or redefined. Version 2 adds the last two fields below |
| `release_id` | The roadmap id, for example `RL-401` | What was tiered: what customers get as one launch |
| `title` | Text | The release's title on the roadmap |
| `assessed` | `YYYY-MM-DD` | The day of the assessment |
| `rubric_version` | `v1`, `v1.2` and so on | The rubric it was scored with (`data/calibration-log.md`) |
| `path` | `full` or `routine` | Which path it took |
| `tier` | `1`, `2`, `3` or `4` | The recommended tier; once approved, the decided tier |
| `tier_job` | `Tell the market`, `Tell customers and sales`, `Tell the customers it serves`, `Log it` | Must match the tier |
| `total` | 0 to 100, in half points | The settled score |
| `borderline` | `true` or `false` | Within 3 points of a tier line |
| `provisional` | `true` or `false` | Maturity below 5 |
| `provisional_reason` | Text, or empty | Required when provisional |
| `gates` | `maturity:` 0 to 10; `revenue:` `passed` or `failed` | The two gates |
| `overrides` | `none`, or a list of `type` (`big_deal`, `market_date`), `from_tier`, `to_tier`, `status` (`proposed`, `approved`, `not approved`, `does not fire`) | Only an `approved` override changes the tier |
| `competitor_flag` | `true` or `false` | A competitor launched the same thing; changes the message, not the tier |
| `status` | `draft` or `approved` | Only approved files are handed on |
| `decided_by`, `decided_on` | A name and a date, or empty | Required when approved |
| `leadership_signoff` | `not needed`, `pending` or `given` | `given` is required for an approved Tier 1 |
| `previous_assessment` | `none` or `YYYY-MM-DD` | The file this one rescores |
| `rescore_trigger` | `none`, `scope`, `date`, `results`, `maturity`, `deal`, `market_date`, `competitor` | Why it was scored again |
| `ship_date` | `YYYY-MM-DD` or `not dated` | From version 2. The owner's newest dated statement, as the assessment found it |
| `added_from_higher_tier` | `none`, or a list of `asset`, `from_tier` (a higher tier than this one) and `reason` | From version 2. Set when the PMM adds an asset from a higher tier's row; the same is written in section 6 |

**How the tier follows from the header** (the checker tests it): the total sets the tier by the lines (70, 50, 30); a borderline release may take either tier on its line (one lower within 3 points above a line, one higher within 3 points below it, with the reason written in section 5); an approved override moves it up one tier; a failed revenue gate caps it at Tier 3.

## The sections people read

1. **Recommendation:** the tier, the line, the gates, the overrides, the decision once made
2. **Scores:** per question, the PMM's score, the agent's, the gap, the settled score, the evidence with its source
3. **Explainer for the PM:** plain words, three reasons, what would change it, questions for the PM
4. **Where more information would help**
5. **Decision:** gaps and what changed the PMM's mind, the PM's answers, the borderline call, overrides, who asked for a different tier
6. **What this tier sets in motion:** the trigger table row and any asset added from a higher tier, with its reason
7. **Changes since the last assessment**

## The weekly list

Written by `/tiering-weekly` every Monday. Header: `handoff: tiering-weekly`, `handoff_version` (`2` from 21 Oct 2026), `week` (`YYYY-Www`), `run` (a date), `rubric_version`, `status` (`draft` or `approved`), `approved_by`, `approved_on`. Its sections are in `templates/tiering-weekly.md`.

- **Approval:** product marketing approves the routine list in one pass, and the list's header records who and when. A release on an approved routine list is approved at the tier the list gives it. A draft list is never handed on.
- **The routine list** has a row per release: release, title, tier, total, ships, why, and whether it moves to the full path. Totals are under 47. A total within 3 points above the Tier 3 line shows as Tier 4, marked borderline.
- **Ships** on every row: the owner's newest dated statement as `YYYY-MM-DD`, with the roadmap's date in brackets when they differ, or `not dated`. The monthly note sorts Tier 4 releases by it.
- **The full path** rows show no total and no tier, because product marketing scores them first. Each links to its assessment, or says "to come".
- **Rescores** name the trigger and its source, including a trigger from an approved Launch Brief.
- **The agent's scores** for the week are in `scores-YYYY-Www.md` beside the list.
- **The record:** every week is a new file, and approved lists are never changed or deleted. A release waiting for its assessment says since which week (`to come, since 2026-W41`). The Launch Brief reads every approved list that mentions a release: its ship date week by week, what changed, the disagreements settled, the rescores, and who asked for what.
