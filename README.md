# Classify product launches: the GTM Tiering Agent

**From Victor Arellano, product marketer.** A Claude Code agent that decides how big a product launch should be, and explains why in words your product manager can use. It is **agent 1 of 4 in a series of GTM agents for product marketers (PMMs).** Built and tested on **fictional data** (a made up company called Rootline), so you can try it today without any of your own company's data.

## What this is, in one minute

Most companies size a launch by how loud the request was or how long the team worked on it. A big build gets a campaign and brings no leads; a small fix that closes deals gets two lines in a release note.

This agent scores each release on the roadmap against your own launch rubric and recommends a tier:

| Tier | Its job |
|---|---|
| 1 | Tell the market |
| 2 | Tell customers and sales |
| 3 | Tell the customers it serves |
| 4 | Log it |

It gathers the evidence from your sources, **asks you to score first** so it doesn't anchor you, compares its scores with yours, and writes a dated assessment with an explainer for your product manager. **You decide every tier.** The agent never approves one on its own, and it never answers for your PM.

What it writes is read by two people and by the agents that come next: the PMM, the product manager, and the next agent in the chain, the Launch Brief ([product-launch-brief](https://github.com/vittycent/product-launch-brief)), which starts the launch brief from it. The format is fixed and checked: see `5-launch-suite/1-gtm-tiering-agent/handoff.md`.

## Try it on Rootline

The agent's part takes about 12 minutes: in Victor's first run, 6 to gather the evidence and seal its own scores, under 1 to compare, about 3.5 to write the draft and 1.5 to record the decision. Add the time you take to read the evidence and score.

1. Install [Claude Code](https://claude.com/claude-code) and clone this repo.
2. Open Claude Code in the suite's folder: `cd classify-product-launches/5-launch-suite` and run `claude`. The suite's `.claude/settings.json` lets it read Rootline's calls in the folders next to it (`example-data/`, `4-asset-usage-agent/`) without asking each time.
3. Type `/tiering-release RL-401` (Rootline's grocer scorecard export). Any id in `data/roadmap.csv` works.
4. Read the evidence it shows you and **score first**, in one line, for example `5 4 7 5 6 8 5 · M6 · pass`.
5. Your files land in `launches/`, which starts empty, so your run is a fresh assessment. After you decide, compare it with Victor's real run in `examples/real-run/RL-401-grocer-scorecard-export/01-tiering/` (Tier 2 at 53), and with what a good run should notice in `answer-keys/`. The agent's scores vary a little from run to run, so yours may not match his exactly.

Tell Claude the date to work on: Rootline's data stops on 4 October 2026, and the worked example runs on **Monday 5 October 2026**.

**Then try the Monday list.** Type `/tiering-weekly. Today is Monday 5 October 2026.` On a first run it reads the whole quarter, scores every release, and sorts each one onto the routine list, which you approve in one pass, or onto the full path, where you score first with `/tiering-release`. It takes about 6 minutes. Compare its list with `examples/weekly/tiering-2026-W41.md`, made by hand on the same data.

## What is in the box

```
classify-product-launches/
  5-launch-suite/                 the suite
    .claude/skills/tiering-release/   the agent: /tiering-release
    .claude/skills/tiering-weekly/    the Monday list: /tiering-weekly
    1-gtm-tiering-agent/          design, handoff, setup interview, templates, a checker
    2-launch-brief/ ... 6-roadmap-watch/   notes on the next agents (the brief itself is in product-launch-brief)
    data/                         Rootline's company data for the suite
    launches/                     where your runs land (starts empty)
    examples/                     the worked example, two dry runs, a real run and an early calibration
  answer-keys/                    what a good run notices (never give these to the agent)
  1-example-company/              Rootline: company, ICP, personas
  2-structured-database/          Rootline's customer evidence database
  4-asset-usage-agent/            Rootline's marketing assets, and calls from weeks 37 to 40
  example-data/                   Rootline's first data set: calls, emails, CRM, surveys, Slack
```

The numbered folders keep the numbers they have in Victor's other repos ([Structured-Database](https://github.com/vittycent/Structured-Database), [message-alignment-agent](https://github.com/vittycent/message-alignment-agent)), so every path inside the data works as it is.

## Rootline: a company to test on

Rootline is a fictional carbon accounting company for food and beverage producers, with about 70 staff and 70 customers. Everything the agent needs is here:

- **The roadmap:** 73 rows shaped like a Linear export, with the Friday project updates from each owner
- **Customers:** 23 customer demands, 120 accounts, 379 support tickets, 122 feedback portal entries, and the calls behind them
- **Deals and goals:** 43 open opportunities, five company goals, a market calendar with real regulation and event dates
- **Conversations:** three Slack channels, six internal meetings, 27 email threads, and more than 80 recorded calls
- **History:** 40 past launches with what marketing did and what came of it
- **A launch rubric** set up by Rootline's PMM, Frida Engström, with its calibration log

**The data is messy on purpose,** the way a real company's is: a roadmap tool that lags the owner's update, a CRM that hasn't caught up with an email, automatic call summaries that get dates wrong, a cancelled update the feedback portal still promises, sales putting a date in writing, a CEO memo about 2027 that no customer has asked for yet. `answer-keys/` lists every planted inconsistency, so you can see what your run caught.

## The worked example and the dry runs

`5-launch-suite/examples/` holds what the process produced on Rootline's Monday, 5 October 2026: six assessments (scenario comparison, progress messages, consolidation, the supplier sort, the grocer scorecard export, the interface refresh), the first weekly list, and an early calibration. Two of them come from dry runs where Victor sat at every stop as the PMM and scored first; the files say which parts were played. `examples/real-run/` holds Victor's first real run of `/tiering-release RL-401` on this repo (13 October 2026). The agent never reads `examples/`, so it can't anchor on Victor's scores or treat your run as a rescore.

## Use it with your own company

1. Answer the setup interview (`5-launch-suite/1-gtm-tiering-agent/setup-interview.md`) with Claude. It produces your rubric: your questions, weights, gates, tier lines and what each tier sets in motion.
2. Save it as `5-launch-suite/data/rubric.md`, and point its source list at your own roadmap, CRM, calls, chat and tickets.
3. Run `/tiering-release` on one release and score first. Check any file with `python3 1-gtm-tiering-agent/tools/check_assessment.py launches`.

## Status

| Part | State |
|---|---|
| `/tiering-release`: tier one release now | Built |
| `/tiering-weekly`: the Monday list | Built |
| `/tiering-setup`: the setup interview as a command | Designed; for now, use the interview file |
| `/tiering-calibrate`: compare tiers with results each quarter | Designed; an early run is in `examples/calibration/` |
| Agent 2: the Launch Brief | Built, in [product-launch-brief](https://github.com/vittycent/product-launch-brief) |
| Agents 3 and 4: goal setter, launch planner | Planned |

Victor will publish updates here as the series grows.

## Provenance and data

- **Everything in this repo was created for this repo,** written by Victor with Claude, on fictional data.
- The idea comes from Victor's own experience: this is version 2 of a chain he first built at his last job. Nothing here comes from that employer, its customers or its data.
- Regulation and event dates in `5-launch-suite/data/market-calendar.md` are real and were checked against their sources; everything about Rootline is invented.

## License

[Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). You may share and adapt it, including commercially, as long as you give credit to Victor Arellano and note any changes.

## Credit

Built by Victor Arellano with Claude. Questions, wins and surprises are welcome. If something did not work for you, that is useful information. Tell Victor.
