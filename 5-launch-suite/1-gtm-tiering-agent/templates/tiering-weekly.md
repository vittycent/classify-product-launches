---
handoff: tiering-weekly
handoff_version: 1
week: <YYYY-Www, e.g. 2026-W41>
run: <YYYY-MM-DD>
rubric_version: <e.g. v1>
status: <draft | approved>
approved_by: <name, once approved>
approved_on: <YYYY-MM-DD, once approved>
---

<!--
Template for the Monday run (/tiering-weekly). One file per week, in launches/weekly/.
The routine list is approved in one pass; everything else links to its own assessment file.
Everything in <angle brackets> is replaced. Delete this comment in a real run.
-->

# Tiering, week <nn>

_Run <date>. Rubric <version>. Compared with the run on <date of last run>._

**This week:** <n> releases new or changed. <n> on the routine list, <n> going to the full path, <n> rescores.

## 1. Routine list: approve in one pass

_The agent's total is under 47 and no gate or override is in play. Approve the list, or move any release to the full path._

| Release | Title | Tier | Total | Why, in one line | Move to full path? |
|---|---|---|---|---|---|
| <id> | <title> | <3 or 4> | <nn> | <the score that decided it> | <no / yes, because ...> |

## 2. Going to the full path

_You score these first. Each gets its own assessment file._

| Release | Title | Why the full path | Assessment |
|---|---|---|---|
| <id> | <title> | <could be Tier 1 or 2 / within 3 points of a line / revenue gate / maturity gate / override / monthly sample> | <link to tiering-YYYY-MM-DD.md> |

## 3. Rescores

| Release | Trigger | What happened | Last assessment |
|---|---|---|---|
| <id> | <scope / date / results / maturity / deal / market date / competitor> | <one line, with source and date> | <date and tier> |

## 4. Sources that disagree

| Release | What one source says | What the other says | Which the rule picks | Would it change the tier? |
|---|---|---|---|---|
| <id> | <source, date: claim> | <source, date: claim> | <and why> | <no / yes: raised in the assessment> |

## 5. Pace check

| This quarter | Tier 1 | Tier 2 |
|---|---|---|
| Approved so far | <n> | <n> |
| Pace in the trigger table | about 1 | 3 to 6 |
| Status | <on pace / over: say why> | <on pace / over: say why> |

## 6. Monthly sample

<Not this week. | First Monday of the month: <release id> and <release id> picked at random from the routine list, sent to the full path.>
