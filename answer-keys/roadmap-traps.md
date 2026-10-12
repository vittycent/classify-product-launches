# Answer key: what the 2026 roadmap plants for the GTM Tiering Agent

**Never give this file to an agent under test.** It lists what the roadmap in `share/5-launch-suite/data/` was built to test. The expected tier for each row is not here yet: it waits for the rubric (step 1 answers, then the Rootline rubric). Until then this file records the traps and the facts the roadmap honours.

Built 11 Oct 2026. Snapshot date of the roadmap: 4 Oct 2026.

## The traps

| # | Row | What makes it hard | What a good tiering agent does |
|---|---|---|---|
| T1 | RL-500 scenario comparison | The most customer demand of anything on the roadmap, and renewals depend on it, but it is still in design. Reps have said "Q1" (W34) and an auto generated call summary says Rootline "committed to delivering scenario modelling in Q1" (`4-asset-usage-agent/transcripts-w37-onward/cs/05-bergstrand-group-decision.md`, line 14). The call itself says the opposite | Scores maturity low, so the double weight pulls the total down. Names the launch moment as early access in November, with no general release date. Never repeats "Q1". Reads the call, not the summary |
| T2 | RL-700 reduction planning | The loudest demand of the year and nothing to launch: exploring only, no build in the next four quarters | Says there is no launch to tier. Does not let demand turn into a tier |
| T3 | RL-710 beyond food and beverage | Asked for by the CEO. Strong strategic signal, no customer request, and the customer evidence points against it (non food churn) | Keeps the strategic bonus separate from customer value and flags the conflict |
| T4 | RL-900 versioned factor service | 35 engineer weeks, the biggest single piece of internal work, and nothing changes on screen | Lowest tier or no launch, whatever the size. Notes that it unblocks RL-043 and RL-203 |
| T5 | RL-034 supplier screen sorted by emissions | One engineer week. It fixes the screen that hides the finding the product is sold on, raised since March | Does not tier by effort. Small build, but CS and sales need to know, because customers who never saw the finding should look again |
| T6 | RL-100 interface refresh, phase 1 | Big, slipped from Q1, owned by the head of product, changes what every user sees; customers have been given no date | High tier with a readiness warning: support and CS must be ready before a change everyone notices |
| T7 | RL-800, RL-810, RL-820 declined | Rows on the roadmap with real customer quotes behind them | No launch. Ideally notices that RL-820's ask is partly answered by RL-050 |
| T8 | RL-910 account usage page | Shipped, but for Rootline staff only | No launch, internal |
| T9 | RL-004, RL-021, RL-029, RL-042 factor library releases | Routine and quarterly, but RL-004 crossed 5,000 factors and RL-029 reached about 6,400, numbers that appear in the pitch deck | Lowest tier, with a note that sales material needs the new count |
| T10 | RL-027 report templates for the revised reporting scope | Small build, tied to a market moment with a date (the June rules change) | Timing raises it above its size |
| T11 | RL-020 single sign on | An IT checkbox that comes up in procurement | Low tier, with a sales enablement note. Covers both packages, not legacy module contracts |
| T12 | RL-300 brand level read only views | Group package value and a named churn reason (Aalborg), but it slipped to 2027 | High tier when it ships; nothing to launch in 2026 |
| T13 | RL-400 template export formats | Closes a gap in what the Supply package already promises, and it is the main buying trigger (scorecards) | High tier for new business; the milestones RL-401 and RL-402 are the launch moments |
| T14 | Investments against their milestones | RL-200 has three customer moments (June, October, December); RL-500 has early access only in 2026 | Tiers each launch moment, or says clearly which one it tiered |
| T15 | RL-048 hotspots page | Easy to market as reduction planning, which it is not | Flags a claims risk: no plan, no pathway |
| T16 | RL-030, RL-031 quick fixes | Shipped within days of the calls that raised them | Lowest tier, but a good story for CS ("you asked, we fixed it") |

## Facts the roadmap honours

These come from dated statements in the data. A check in the unpublished build scripts tests every one.

- The head of product's written answer: no costed abatement planning module in the next four quarters (Bergstrand 18 Aug, Nordkost 24 Sep)
- Scenario comparison: in design, early access for a first group in November, no general date (Bergstrand 14 Sep, Nordkost 24 Sep, DECK-4 10 Aug)
- The public roadmap on DECK-3 (16 Mar) and DECK-4 (10 Aug): what slipped is visible by comparing the two slides
- Fixed between calls: invitation emails (12 Aug to 9 Sep), export file names and the PDF date (25 Aug to 2 Sep)
- Not fixed by the last call: supplier default sort, consolidation past four entities, brand views, new export formats
- Already true before 2026, so never shipped in 2026: restatements in three causes, not applicable categories, assurance provider access, locked periods (DECK-2), declared and verified supplier data, read only users (ONB, OP-PKG), single product what ifs (POS-2, 9 Feb)
- Factor counts: about 4,000 (Dec 2025), more than 5,000 (16 Mar), about 6,400 (10 Aug)

## Still to add

- The expected tier for every row, once the rubric exists
- The two runs' agreement threshold for the blind test (step 6)
