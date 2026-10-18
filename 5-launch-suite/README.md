# Launch suite

A group of agents that take a product release from the roadmap to launch: decide how big the launch is, research it, set its goals, plan it and write its first email. Each agent works on its own, and each one reads what the agent before it wrote. Built on Rootline, the fictional software company for food and beverage producers used across the Agent Lab.

Started 11 Oct 2026 by Victor Arellano, a product marketer. The GTM Tiering Agent is the first agent in a series of GTM agents for product marketers (PMMs). The suite is version 2 of a chain Victor first built at his last job; nothing here comes from that employer.

## The agents

| # | Agent | Reads | Writes | Status |
|---|---|---|---|---|
| 1 | [GTM Tiering Agent](1-gtm-tiering-agent/) | A roadmap item, the launch rubric | Tier and score | **Building.** `/tiering-release` built; the other three commands next |
| 2 | [Brief intake](2-brief-intake/) | The tier and score, company context, customer evidence | Launch brief | Planned |
| 3 | [Goal setter](3-goal-setter/) | Tier, brief, company goals, launch history, benchmarks | Goals with baseline, stretch and owner | Planned |
| 4 | [Launch planner](4-launch-planner/) | Goals, brief, people | Week by week plan and asset list | Planned |
| 5 | [Launch email writer](5-launch-email-writer/) | Brief, goals, ICP | Email drafts | Planned |
| 6 | [Roadmap watch](6-roadmap-watch/) | Roadmap, project updates, team chat | Act, Monitor, Watch list that feeds agent 1 | Planned |

## How the folder works

- **`data/`** holds what more than one agent reads: the roadmap, customer demand and teams today; company goals, launch history and people later. An agent never keeps its own copy of shared data.
- **One folder per agent**, numbered in chain order. Each holds that agent's specs and templates.
- **`launches/`** holds what the agents write: one folder per release, one subfolder per agent (`01-tiering`, later `02-brief` and on), and a dated file per run, plus `weekly/` for the Monday lists. It starts empty, so your first run of a release is never a rescore.
- **`examples/`** holds Victor's worked example, dry runs and an early calibration on Rootline, as scored on Monday 5 October 2026, in the same layout. The agents never read it.
- **Rootline context** stays where it already is: `../1-example-company/` for the company, ICP and personas, and `../example-data/` plus `../4-asset-usage-agent/transcripts-w37-onward/` for calls. `data/README.md` describes the suite's data.
- **Answer keys** for testing live in `../answer-keys/` at the top of the repo and are never given to an agent under test.

## Rules every agent follows

1. Runs alone: looks for the earlier agent's file first, and asks the user only for what is missing
2. Writes into one folder per launch, in chain order (`01-tiering`, `02-brief`, `03-goals`, `04-plan`)
3. Uses a fixed handoff format with a version number, readable by people and parseable by the next agent
4. Stops for the user's approval before it writes
5. Questions it asks during setup are about the user's company, never a particular industry
