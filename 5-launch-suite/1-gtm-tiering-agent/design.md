# GTM Tiering Agent: design

_Draft 0.1, 11 Oct 2026, approved. Nothing here is built yet. Examples use Rootline, the fictional company in this kit._

**What it does.** For each release on the roadmap, the agent recommends a launch tier, explains it in words a product manager can use, and keeps a dated record of every assessment and decision. Product marketing decides. It is the first agent in the launch suite: brief intake, the goal setter and the launch planner come next and read what it writes.

**What it is built on.** The rubric your setup interview produces (`setup-interview.md`): seven scored questions with weights, two gates, overrides, tier lines, the evidence order, the sources and the rule for conflicts, the trigger table, and who decides.

---

## 1. How you run it

The kit has no interface. The agent is a set of Claude Code commands, skills in `.claude/skills/` at the top of the suite, and every spec, template and rubric is a plain file you can read and change. Open Claude Code in the suite's folder and type the command.

| Command | When | What it does |
|---|---|---|
| `/tiering-setup` | Once, and again when the business changes | Walks you through the setup interview and writes your rubric, `data/rubric.md` |
| `/tiering-release <id>` | Whenever you need a tier now | Tiers one release on the full path (section 2) |
| `/tiering-weekly` | Every Monday | Finds releases that are new or changed since the last run, checks the rescore triggers, and tiers them as one batch |
| `/tiering-calibrate` | Once a quarter | Compares tiers with how the launches did, and proposes at most one change to the rubric |

## 2. Two paths: routine and full

Two things from the setup have to work together: product marketing scores before seeing the agent's score, and the agent runs small launches without taking product marketing's time. So every release takes one of two paths.

**What it tiers.** What customers get as one launch, not the roadmap row. An investment that ships in pieces is assessed per piece still to ship (Rootline's faster loading becomes progress messages in October and consolidation in December); a stage such as early access is not a launch of its own. The agent works this out from the roadmap and the project updates.

**Which path.** The agent scores every release from the evidence first, and keeps its score to itself. A release goes on the **routine path** if the agent's total is under 47 (more than 3 points below the Tier 2 line) and no gate or override is in play. Everything else goes on the **full path**: anything that could be Tier 1 or 2, anything close to the Tier 2 line, anything where the revenue gate, the maturity gate or an override applies.

**Two details the first run settled.** A gate is in play when it changes the outcome: a failed revenue gate caps at Tier 3, so it is in play only from a total of 50 up; below that it changes nothing, and most small updates fail it. On the routine list, a total within 3 points of the Tier 3 line is shown in the lower tier and marked borderline; you can move it to the full path like any other.

**The full path**

1. **Evidence.** The agent gathers the evidence for each scoring question from your sources, ranked by the evidence order, and writes it up without scores. It seals its own scores before you see anything. For validation it lists the kinds of proof it found, strongest first; how many customers asked goes under customer request only. It also says what of the release's promise has already reached customers through other releases, because a big release can arrive with its most visible parts already shipped.
2. **You score first.** You give each of the seven questions a 0 to 10 and answer the two gates, before you see the agent's scores.
3. **Compare.** The agent shows its scores. Only gaps of 3 or more points are discussed. For each one you keep your score, take the agent's, or note the cause for calibration. A gap can stay open until you have talked to the product manager; your score stands meanwhile, and the file shows what settling it the agent's way would do. If you change a score, say what changed your mind: the file records it, and a change without a reason is recorded as one.
4. **Recommend.** The agent applies the weights, the tier lines, the revenue gate, any overrides and the maturity gate, then writes the recommendation and the explainer (section 5).
5. **Ask the PM.** You take the explainer's questions to the product manager, a person, and record their answers. The agent prepares the questions and never answers them itself. The file stays a draft until the PM has answered, or until you decide without them and say why.
6. **Decide.** You decide. The file is marked approved, with the trigger table row for that tier attached, and the next agent can pick it up. Tier 1 also needs leadership sign off. You can add an asset from a higher tier's row (a messaging update, a session) without changing the tier; the file records it with its reason.

**The routine path**

1. The agent gathers the evidence and scores the release.
2. It goes on the weekly list with its tier, total and a one line reason.
3. You approve the list in one pass, or move any release to the full path.

**Keeping calibration honest.** Routine releases never get a score from you, so calibration would only ever see the big ones. Each month, two routine releases picked at random go through the full path as well.

## 3. What it reads

| Input | What the agent uses it for | Rootline file |
|---|---|---|
| Roadmap | What is planned: every release, its stage, dates, size and owner | `data/roadmap.csv` |
| Rubric | Questions, anchors, weights, gates, overrides, lines, trigger table | `data/rubric.md` (step 3) |
| Customer evidence | Requests, lost deals, workarounds, test results | `data/customer-demand.md`, `data/emails/`, the calls and emails in `../example-data/` and `../4-asset-usage-agent/transcripts-w37-onward/` |
| Project updates and the product team's chat | What is really happening, against the roadmap | Step 3 |
| Pipeline export, with the emails and calls about each deal | Deals that depend on a release (the big deal override). The newest statement about a deal wins, wherever it is | Step 3 |
| Company goals | Strategic signals | Step 3 |
| Market calendar | Dates customers must meet (the market date override) | Step 3 |
| Launch history with results | Past tiers to compare against; the quarterly results check | Step 3 |
| Teams | Owners named in the explainer | `data/teams.md` |

When two sources disagree, the agent follows the rule in the rubric: the newest dated statement from the owner wins, a newer conversation beats the roadmap tool, an automatic summary never beats its source, and a disagreement that would change the tier is raised, never settled quietly.

**How the agent reads the gates and overrides.** Four rules the dry runs needed, for any rubric:

- **A deal waits on a release** only if the newest dated statement about the deal says so: the CRM notes, an email or a call, whichever is newest. A CRM field that lists the release is not enough.
- **The revenue gate** passes when the release opens a new revenue stream, or an open deal waits on it by that rule. "It could help us win" is a reason in the explainer, not a pass.
- **A market date** counts for the override only when a current customer must meet it. A prospect's date is written into the file and the explainer, and counts once they sign.
- **A gate is in play** only when it changes the outcome (section 2).

## 4. What it writes

**One folder per release, one file per assessment.**

```
launches/
  RL-500-scenario-comparison/
    01-tiering/
      evidence-2026-10-05.md     (step 1: the evidence, no scores)
      agent-scores-2026-10-05.md (the agent's scores, sealed before you score)
      tiering-2026-10-05.md      (the assessment)
      tiering-2026-11-16.md      (rescored when early access opened)
  weekly/
    tiering-2026-W41.md          (the routine list for that week)
  calibration/
    calibration-2026-10-05.md    (a calibration review)
```

Each assessment is a new dated file. Nothing is overwritten; the newest approved file is the current tier. Later agents write into the same release folder (`02-brief/`, `03-goals/`, `04-plan/`).

**Each file has a short header** the next agent can read, then sections for people:

| Header field | Example |
|---|---|
| release, title | RL-500, Scenario comparison |
| date, rubric version | 2026-10-05, rubric v1 |
| path | full |
| tier, total | 2, 58 |
| provisional | yes (maturity below 5) |
| gates, overrides | revenue passed; none |
| status | draft or approved |
| previous assessment | none, or the date of the last one |

_The values above show the format only; Rootline's real scores come in step 4._

| Section | What it holds |
|---|---|
| 1. Recommendation | Tier, total, provisional or not, which gates and overrides applied |
| 2. Scores | Per question: weight, your score, the agent's score, the gap, the points, and the evidence with its source |
| 3. Explainer for the PM | Section 5 below |
| 4. Where more information would help | Scores resting on thin evidence, and what would firm them up |
| 5. Decision | The PM's input, your decision, the date, and the reason for any borderline call or override |
| 6. What this tier sets in motion | The trigger table row: lead time, who leads, who hears about it, assets |
| 7. Changes since the last assessment | For a rescore: what changed and which trigger fired |

The template is `templates/tiering-assessment.md`; the weekly list is `templates/tiering-weekly.md`.

## 5. The explainer

The part you take to the product manager. Plain words, no rubric vocabulary.

1. **The tier in one sentence,** with its job: "Tier 2: tell customers and sales."
2. **The three reasons that weigh most,** taken from the questions that add the most points, each with the reason behind its weight. A tie goes to the question closest to its maximum, then to the one asked first.
3. **What would change the tier:** how far it is from the nearest line, which score would move it, and any coming event that would trigger a rescore.
4. **Questions for the PM:** one for each score that rests on thin evidence.

## 6. When it runs, and when it looks again

- **Every Monday,** `/tiering-weekly`. Until the roadmap watch agent exists, it compares the roadmap and project updates with its own last run.
- **On demand,** `/tiering-release <id>`.
- **A release is scored again** when scope is added or cut, the date moves into another quarter, results come in from customers testing it, it becomes ready to test with customers, a big deal or market date appears or falls away, or a competitor launches the same thing.
- **And after it ships:** at every quarterly calibration, for two quarters, with its results.

## 7. Where a person decides

| Moment | Who |
|---|---|
| Setup, and any change to the rubric | Product marketing |
| Scores on the full path, and settling gaps | Product marketing |
| A release close to a line | Product marketing; it stays in the lower tier unless the reason to move up is clear |
| An override | Product marketing approves; logged with its reason |
| The routine weekly list | Product marketing, in one pass |
| The tier | Product marketing, after the product manager's input |
| A Tier 1 launch | Leadership signs off |

**Version 1 never approves a tier on its own.** Product marketing approves every tier, Tier 3 and 4 included. Until then each assessment stays a draft, to be discussed. Letting the agent approve Tier 3 and 4 is for a later version, once calibration shows it can be trusted.

## 8. The rubric and calibration

- **`data/rubric.md`** carries a version number. Version 1 is what the setup interview produced.
- **`data/calibration-log.md`** records every change: the date, the new version, the cause (a missing source, an anchor read two ways, or a weight), what changed, and the evidence.
- **One change per review.**
- **Releases are scored again after they ship.** At each quarterly calibration, every release from the last two quarters is scored with its results; one that moves up a tier gets the launch it missed, as a second launch moment. The cause for such a change is **results after release**, the fourth cause next to a missing source, an anchor read two ways and a weight.
- **Once a quarter,** `/tiering-calibrate` compares each tier with how the launch did, and counts Tier 1 and 2 launches against the trigger table's pace: about one Tier 1 a quarter, one or two Tier 2 a month.

## 9. Tiers

Tier 1 to 4, with 1 the biggest.

## 10. What the next agent gets

Brief intake reads the newest approved tiering file for a release: the header, the explainer and the evidence links. The exact handoff is set when brief intake is built, using what the tiering agent teaches.
