# Calibration check, early: two past launches against the rubric

_Monday 5 October 2026. Rubric v1. An early run of `/tiering-calibrate`, before the first quarter of tiers exists, at Frida's ask: "Also score the supplier comparison (shipped April) as if it shipped today: it may deserve more than the release note it got" (transcript 05, 1 Oct). Approved by Frida on 5 October: rubric v1.1. Dry run: Frida is Victor._

**Why these two.** They are the two numbers behind the rubric (section 1): the speed launch got 85 hours and 4,000 EUR and brought no leads; the supplier comparison got one hour and has closed or turned four accounts since August. Rootline has never tiered, so neither has a tier to compare with. The agent scores each twice: with what was known when it shipped, and with what is known today.

## The two releases

| | RL-201 faster imports, step 1 | RL-016 supplier comparison |
|---|---|---|
| Shipped | 15 June | 13 April |
| What marketing did | A campaign: its own email to every user, the What's new panel, four paid LinkedIn posts, a video, a sales slide. 85 hours, 4,000 EUR | Two lines in the April release note. 1 hour |
| What that treatment was, in today's tiers | About Tier 1 | Tier 4 |
| What happened | No leads, no opportunities. Customers noticed the speed. The groups read "twice as fast" as a promise not kept ("Faster at what?") | 17% of Supply and Group customers opened it in a month by September, nearly all after a CSM or Tobias showed it. Closed or turned Vretstorp, Klarälven, Tre Kronor's renewal and Nordkost's COO (W40 pipeline review). Tre Kronor wrote a supplier tiebreak into its purchasing policy (28 Sep) |
| Sources | `launch-history.csv` LH-32; transcripts 01 and 03 | `launch-history.csv` LH-20; W40 pipeline review; transcript 04 |

## Scored with what was known when it shipped

| # | Question | Weight | RL-201, June | RL-016, April |
|---|---|---|---|---|
| 1 | New category | 2 | 0: speed for the product customers have | 3: a supplier decision on one screen; nobody knew yet that purchasing would use it |
| 2 | Market need | 2 | 1 | 2: group customers asking which of two suppliers to favour |
| 3 | Validation | 1.5 | 5: 34 slow import tickets, requests | 3: a few groups asking; no test |
| 4 | Strategic signals | 1.5 | 5: G2, keep the customers we win | 5: G4 counts it from April |
| 5 | Customer request | 1 | 5: 8 accounts | 4: 4 accounts |
| 6 | Market expectation | 1 | 9: expected | 4: not expected |
| 7 | Customer reach | 1 | 8 | 5: Supply and Group |
| | **Total** | | **39: Tier 3** | **35: Tier 3** |
| | Revenue gate | | Failed: no deal named it | Failed: no deal named it yet |

## Scored with what is known today

RL-201: no change; nothing in the results raises a score, and the groups' reaction lowers nothing the rubric asks. **Still Tier 3.**

| # | Question | Weight | RL-016 today | What changed |
|---|---|---|---|---|
| 1 | New category | 2 | 5 | Purchasing uses it: Tre Kronor's policy, Klarälven's purchasing manager, Nordkost's COO |
| 2 | Market need | 2 | 6 | It wins prospects Rootline didn't serve: Vretstorp, Klarälven |
| 3 | Validation | 1.5 | 9 | Results from customers using it, and deals closed or turned |
| 4 | Strategic signals | 1.5 | 9 | G4 directly; G1 through new deals; G2 through Tre Kronor's renewal |
| 5 | Customer request | 1 | 4 | Still not driven by requests |
| 6 | Market expectation | 1 | 5 | Customers who see it are pleased; nobody expects it |
| 7 | Customer reach | 1 | 5 | Unchanged |
| | **Total** | | **63: Tier 2** | Revenue gate now passed |

## What the comparison says

- **RL-201: the rubric would have prevented the mistake.** Tier 3 in June: a release note, an email to the customers it serves, a CS briefing, support writing to everyone who raised slow imports. Not a campaign. And a precise message would have said what it didn't fix, which is what the groups needed to hear.
- **RL-016: the rubric would have done better, but not well enough.** Tier 3 in April instead of two lines: an email to the customers it serves and a CS briefing, which is how it later spread anyway. But its value only showed after customers used it, from August. The rubric scores a release once, before it ships, and nothing scores it again afterwards. Today it is a Tier 2 release that got a Tier 4 launch, and nothing in the process would have noticed.

## The one change proposed

**At every quarterly calibration, score again every release shipped in the last two quarters, with its results. A release that moves up a tier gets the launch it missed, as a second launch moment.**

- For RL-016 today: Tier 2, so it gets a Tier 2 moment now: the page Karin and Henrik asked for (`#marknad`, 28 Sep), a sales one pager and briefing, an email to the customers it serves.
- Where it goes: `rubric.md` section 10 (when to look again) and `design.md` section 8 (calibration).
- Cause: none of the three in the calibration log fits. It isn't a gap between Frida and the agent; it is results the rubric couldn't see at launch. Proposed fourth cause: **results after release**.

**Pace check.** This quarter so far: no Tier 1; RL-401 approved at Tier 3. RL-016's second launch moment, at Tier 2, is the quarter's first Tier 2.

**Decision, 5 October.** The change is approved (`calibration-log.md` v1.1). RL-016 gets its Tier 2 moment now: led by Frida with Samir, heard by existing customers and the current pipeline.
