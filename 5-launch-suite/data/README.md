# Launch suite data

_Fictional. Shared by every agent in the launch suite._

**Snapshot date: 4 October 2026**, the end of 2026-W40 and the last day of the Rootline calls. Everything released before it happened; everything after it is a plan.

| File | What it is | Used by |
|---|---|---|
| `roadmap.csv` | Rootline's 2026 product roadmap, one row per item, shaped like a Linear export: 6 investments with 6 milestones, 51 smaller updates (one cancelled), plus discovery (two of them added by the CEO in September), declined, internal and later rows (73 in all). Updated when someone remembers | GTM Tiering Agent, brief intake, goal setter, roadmap watch |
| `roadmap.md` | The same roadmap as a readable page: at a glance, how the plan changed, the investments, updates by quarter. Generated from the build script, so edit the script, not the page | People |
| `customer-demand.md` | 23 customer demands (D-01 to D-23): their words, when they reached product, the evidence in the calls, and the roadmap rows that answer them | GTM Tiering Agent (customer value), brief intake |
| `teams.md` | Head of product, three PMs, three teams of 6 to 7 engineers, and the capacity estimate behind the roadmap's size | GTM Tiering Agent, goal setter, planner |
| `rubric.md` | Rootline's launch rubric, version 1.2 (5 Oct 2026; version 1 set up on 4 Oct): tiers, seven scoring questions with anchors, weights, gates, overrides, tier lines, sources, the trigger table, who decides | GTM Tiering Agent; brief intake, goal setter and planner read the trigger table |
| `calibration-log.md` | Every change to the rubric, one per review | GTM Tiering Agent |
| `people.md` | Everyone at Rootline who appears in the data: 29 people, including the marketing team, designers, engineering leads and support | All |
| `accounts.csv` | 120 accounts: the FY25 cohort, every company in the calls, older customers and pipeline prospects, with segment, status, ARR where known, CSM and AE | All |
| `company-goals.md` | Five company goals for 2026 (G1 to G5), each with a measure, target, end of Q3 status and owner | GTM Tiering Agent (strategic signals), goal setter |
| `pipeline.csv`, `pipeline.md` | 43 open opportunities at the snapshot: new business, win back, expansion and Q4 renewals, with the roadmap items deals wait on | GTM Tiering Agent (big deal override), goal setter |
| `market-calendar.md` | Regulation, standard and event dates (real, verified 11 Oct 2026) and Rootline and customer dates (fictional), March 2026 to December 2027 | GTM Tiering Agent (market date override), planner |
| `launch-history.csv`, `launch-history.md` | Every release from June 2025 to the snapshot: what marketing did, hours, email and LinkedIn numbers, adoption, what happened. Rootline has never tiered | GTM Tiering Agent (calibration against results), goal setter |
| `project-updates.md` | Weekly owner updates for the six investments, W33 to W40 | GTM Tiering Agent, roadmap watch |
| `support-tickets.csv`, `support-tickets.md` | 379 support tickets, January to 2 October 2026, tagged by theme, demand and roadmap item | GTM Tiering Agent (validation), brief intake |
| `feedback-portal.csv`, `feedback-portal.md` | 122 feedback portal entries: 42 ideas with votes by account, status and the PM's answer, and 80 merged duplicates | GTM Tiering Agent (customer request, validation), brief intake |
| `slack/produkt.md` | The product team's channel, W33 to W40 | GTM Tiering Agent, roadmap watch |
| `slack/marknad.md` | The marketing team's channel, W33 to W40 | People; the demo's backstory |
| `slack/kundfeedback-w37-w40.md` | The customer feedback channel, W37 to W40 (continues `example-data/07-slack-export.md`) | GTM Tiering Agent, brief intake |
| `transcripts/` | Six internal meetings: the faster loading launch retro (2 Jul), product weekly (7 Sep), support themes (15 Sep), scenario comparison early access review (29 Sep), product leadership on Q4 capacity (30 Sep), marketing weekly on the Q4 launch list (1 Oct) | GTM Tiering Agent, brief intake |
| `emails/` | Nine email threads, W39 to W40, internal and with customers: the CRO's challenge to two product bets, an early access customer questioning its fit, the head of engineering's Q4 capacity proposal, customers asking for something other than what is planned, an expansion put on hold, a date given in writing, the CEO's 2027 memo. Older threads are in `example-data/10-email-threads/` | GTM Tiering Agent, brief intake |

**How the data was made.** Built from what Rootline customers say in the calls and what Rootline's own assets already promise or state, so it contradicts none of them. Tables come from build scripts that are not published; read them as exports. Slack exports and transcripts are written as files. Two checks: `check_roadmap.py` (35 dated facts) and `check_company_data.py` (148 checks: names, accounts, ids, dates, quoted numbers, and every customer quote traced to a call). Both pass on the published data.

**Like a real company, the data is messy on purpose.** A CRM stage that lags a call, a close date nobody moved, a duplicate record, a roadmap date older than the owner's update, automatic call summaries that get things wrong, updates delayed or cancelled in a meeting long before the roadmap tool or the feedback portal catches up, and people inside and outside Rootline who argue against the plan. Read sources against each other.

**Before August.** The calls only cover August to early October. Requests from earlier in the year show up in the `added` and `signal` fields in `roadmap.csv`, the support tickets and the feedback portal (both from January).

**Still to come:** product specs for the investments, a customer facing changelog, channel benchmarks and an adoption funnel. They come with the agents that need them.
