# Examples

What the process produced on Rootline's Monday, 5 October 2026, laid out the way the agent writes into `../launches/`. The agent never reads this folder, so your own run starts fresh.

- **Worked example:** RL-500 (scenario comparison), RL-202 (progress messages), RL-203 (consolidation) and RL-034 (supplier sort), scored by hand with rubric v1, plus the first Monday list in `weekly/`.
- **Two dry runs**, where Victor sat at every stop as the PMM and scored first: RL-401 (grocer scorecard export) and RL-100 (interface refresh). The files say which parts were played.
- **A real run** in `real-run/`: `/tiering-release RL-401` from a fresh copy of this repo on 13 October 2026, with Victor as Frida. Tier 2 at 53. This is the run his blog post walks through. The checker problem it found (a borderline release just below a line could not move up) is fixed.
- **An early calibration** in `calibration/`.

The rubric changed after the worked example and the dry runs (the real run used v1.3, the current version, see `../data/calibration-log.md`), so a run today can score those releases differently. The agent also varies from run to run: a replay of the real run on 18 October, with the same replies, reached the same decision (Tier 2 at 53), but the agent's own total came out at 51 instead of 46.5.
