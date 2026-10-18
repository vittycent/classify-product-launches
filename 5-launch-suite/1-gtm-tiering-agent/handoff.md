# GTM Tiering Agent: the handoff

_Version 1, 12 Oct 2026. What the agent writes, and what people and the next agents can rely on. The checker `tools/check_assessment.py` tests every file against this page._

## Who reads it

| Reader | Reads | For |
|---|---|---|
| Product marketing | The whole file, sections 1 to 7 | Deciding the tier, taking the explainer to the PM, starting the launch work |
| The product manager | Section 3, the explainer | Answering the questions; knowing what the tier sets in motion |
| Brief intake (agent 2) | The header, section 1, section 2's evidence and sources, section 3 | Starting the launch brief from what the evidence says, not from scratch |
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
    02-brief/                      written by brief intake
  weekly/tiering-YYYY-Www.md       the Monday list
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
| `handoff_version` | `1` | Changes only when a field is added, removed or redefined |
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

`handoff: tiering-weekly`, `handoff_version: 1`, `week` (`YYYY-Www`), `run` (a date), `rubric_version`, `status` (`draft` or `approved`), `approved_by`, `approved_on`. Its sections are in `templates/tiering-weekly.md`. A release on an approved routine list is approved at the tier the list gives it.
