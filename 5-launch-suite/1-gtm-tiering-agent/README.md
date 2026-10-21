# 1. GTM Tiering Agent

Decides how big a launch a roadmap item deserves: scores it against the company's launch rubric and returns a tier, a score and the reasons, for a person to approve.

**Status, 21 Oct 2026: building.** `/tiering-release` and `/tiering-weekly` are built (`../.claude/skills/`), with the handoff contract (`handoff.md`, version 2) and a checker for every file they write (`tools/check_assessment.py`). `/tiering-setup` and `/tiering-calibrate` come next. The process was proven by hand first: a worked example on Rootline (four releases and a weekly list) and two dry runs with a product marketer at every stop (`../examples/`).

## Run it

1. Open Claude Code in the launch suite's folder.
2. Type `/tiering-release RL-401` (any id on your roadmap).
3. It gathers the evidence and seals its own scores, then asks you to score first, in one line. Then it compares, recommends, writes the explainer for your product manager, and waits for your decision.
4. Every Monday, type `/tiering-weekly`. It finds what is new or changed on the roadmap, scores it, and sorts it: small releases onto a routine list you approve in one pass, bigger ones to the full path. Each row carries its ship date.
5. Check any file: `python3 1-gtm-tiering-agent/tools/check_assessment.py launches`.

## What is here

| File | What it is |
|---|---|
| `design.md` | How the agent works: the two paths, what it reads, what it writes, where a person decides |
| `handoff.md` | What every file it writes contains, for people and for the next agent |
| `setup-interview.md` | The questions that produce your rubric |
| `templates/` | The assessment file and the weekly list |
| `tools/check_assessment.py` | Checks a file against the handoff |

