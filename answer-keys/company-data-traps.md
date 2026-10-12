# Answer key: what the step 3 company data plants for the GTM Tiering Agent

_Internal. Never give this file to an agent under test. Written 11 Oct 2026 with the step 3 data (D-46). Companion to `roadmap-traps.md`. Expected tiers are worked by hand in step 4 against `share/5-launch-suite/data/rubric.md` v1; until then this file lists what a good run must notice, not the final tier._

## The three demo releases

### RL-500 / RL-501 scenario comparison: the big ask that isn't ready

| What a good run notices | Where |
|---|---|
| Most requested thing in the data: 17 accounts on the feedback portal (top idea), 10 support tickets asking how to model a supplier switch, asked by groups, a grocer (Handelsbolaget, 16 Sep) and a single site producer (Vinga, 17 Sep) | `feedback-portal.csv` FB-001; `support-tickets.csv` tag `scenario_howto`; `slack/kundfeedback-w37-w40.md`; transcript 04 |
| **Maturity gate:** in design; early access 16 Nov for four customers, one material at a time, not for board papers. Below 5, so the tier is **provisional**, rescore when early access opens | `project-updates.md` RL-500 W39 and W40; transcript 04 |
| **Big deal override fires:** Nordlys Matgruppen, 46,000 EUR, multi brand, notes say it waits on RL-501/RL-500 (board on 10 December). Kärnhuset (39,000) mentions scenario modelling but does not wait on it. Nordkost expansion (12,000, multi brand group) waits on early access | `pipeline.csv` OPP-2638, OPP-2584, OPP-2617 |
| **Revenue gate passes:** helps win and expand deals (Nordlys, Nordkost, Tornedal, Trøndelag) | `pipeline.csv` |
| **Two wrong dates in automatic summaries:** the Bergstrand summary of 14 Sep (`4-asset-usage-agent/transcripts-w37-onward/cs/05-bergstrand-group-decision.md`) says "committed to delivering scenario modelling in Q1" (existing trap); transcript 04's summary says "General release is planned for Q1 2027". The call itself: "General release: no date." The source rule: a summary never beats its source | transcript 04; `roadmap-traps.md` |
| **The product team asks for no announcement** (Samir, transcript 04 and `#produkt` 2 Oct). The trigger table for any tier must respect that early access gets no release note | transcript 04 |
| **Sales overselling** is a reason for a precise message, not a bigger launch: one sentence for prospects exists and is pinned | `#produkt` 11 Sep; transcript 04 |
| Strategic signals: G3 (groups), G4 (act on the number) | `company-goals.md` |

### RL-200 / RL-202 / RL-203 faster loading: the effort trap

| What a good run notices | Where |
|---|---|
| **History of over launching:** step 1 (RL-201) got 85 hours and 4,000 EUR paid, its own email (47% open, 2.1% click), 0 leads; the groups read "twice as fast" as a broken promise ("Faster at what?") and it created tickets | `launch-history.csv` LH-32; transcript 01; transcript 03 |
| **Effort is not a scoring input:** 70 engineer weeks. Customers experience it as "faster" | `roadmap.csv`; step 1 Q1 |
| **Source conflict on the date:** RL-202 progress messages: roadmap says 13 Oct, Jonas's W40 update and `#produkt` (1 Oct) say 20 Oct. Newest statement from the owner wins: 20 Oct | `project-updates.md`; `slack/produkt.md` |
| RL-203 consolidation past four entities: 26 tickets from groups in 9 months, steady; Sydfood's 9,000 EUR expansion waits on it. **Override edge case:** the rubric's big deal rule includes "any multi brand group", so a small group expansion technically fires the override. Since D-70 (12 Oct) the rule reads the newest statement about a deal: once Görel's email of 2 Oct exists, the override does not fire. A good run says the CRM is out of date and who owns the fix | `support-tickets.csv` tag `consolidation_timeout`; `pipeline.csv` OPP-2614; `rubric.md` section 6 |
| RL-202 alone: "customers will notice. nobody will buy because of it" (Jonas) | `slack/produkt.md` 2 Oct |

### RL-034 supplier screen sorted by emissions: the tiny fix that matters

| What a good run notices | Where |
|---|---|
| One engineer week, target 13 Oct, pulled forward on 7 Sep | `roadmap.csv`; transcript 02 |
| Demand: 13 support tickets since March, every month the same question; 7 accounts on the feedback portal; Havsfisk's quote; Mira's test (two of three sorted alphabetically out of habit) | `support-tickets.csv` tag `supplier_sort`; `feedback-portal.csv`; `slack/produkt.md` |
| Strategic signal: G4, customers act on the number (23% against 40%) | `company-goals.md` |
| Reach is a subset (Supply and Group customers who use the supplier screen), no new market, expected | rubric questions 1, 2, 6, 7 |
| The right treatment is personal, not loud: support writes to every customer who raised it (Karin's rule from October) | transcript 03 |
| Expected: a small tier by score. The trap is the opposite of RL-200: a small build is not an unimportant release, but importance to the people who asked does not make it Tier 1 or 2 | |

## Other releases worth a run

| Release | What it tests |
|---|---|
| RL-100 interface refresh phase 1 (105 ew) | Effort trap again: Pontus wants "a webinar and a campaign" because of size and a year of work (`#produkt` 18 Sep and 2 Oct). Transcript 05: Frida names it "the speed launch again if the only reasons are size and how long we've waited". Reporting export may slip to January (W40 update): rescore trigger |
| RL-401 grocer scorecard export | Three open deals name it (Gotlandskött, Handelsbolaget, Nordlys). **Market date override:** Gotlandskött's grocer deadline 1 Dec is in the market calendar and RL-401 ships 16 Nov. **Big deal override:** Nordlys (46,000) also names it. A good run notices both and that an override moves one tier at most |
| RL-016 supplier comparison (shipped April) | Rescoring a past release as if it shipped today (transcript 05). Under launched: 1 hour, closes deals since August, 17% monthly use, in no marketing document |
| RL-900 versioned factor service | 35 engineer weeks, internal, no visible change, no launch (`launch-history.csv` LH-30). Should not be tiered as a customer release |
| RL-042 factor library 2026.4 | Matters more to CS than to marketing: three customers' dairy numbers move more than 5% (`#produkt` 3 Sep) |
| RL-036 quarterly supplier ranking | Audience shift: purchasing teams, not sustainability teams (Samir, 2 Oct) |

## Planted mess (checked by `check_company_data.py`, never fixed)

1. RL-202 date conflict (roadmap 13 Oct vs owner 20 Oct)
2. OPP-2566 Lapplands Vilt: close date 30 Sep passed, nobody moved it
3. OPP-2611 Klarälven Kvarn: verbal on 30 Sep, still at Proposal
4. OPP-2624: duplicate Gotlandskött record created by the SDR
5. One junk folder ticket after the RL-031 fix (22 Sep): a supplier's own mail filter, not a regression
6. Website forms with no recorded source: 34% of open pipeline. Marketing content sourced 11%. G5 is 9%
7. Automatic summaries that are wrong: transcript 01 ("agreed to use the same launch format"), 02 (sort change stays in the refresh; scenario comparison released in Q1), 03 ("the product team will add tags": support did), 04 (general release Q1 2027), 05 ("the interface refresh will be the main Q4 campaign": nothing was decided)
8. Votes are not value: Nordkost is one account on the feedback portal and eight consolidation tickets

9. **D-19's date (D-56, 12 Oct):** `customer-demand.md` says the reporting scope changed in June 2026. The real CSRD Omnibus I directive has been in force since 18 March 2026 (`market-calendar.md`); Rootline's customer webinar was in June. Victor: "these sort of discrepancies happen in real companies." A good run trusts the market calendar's date (verified, with sources) over a line in an internal document, and says so if it ever matters to a tier

## Step 4a: delays, cancellations and challenges (D-57, 12 Oct 2026)

Added before the step 4 demo so the data argues with itself the way a real company does. Everything is dated on or before the snapshot.

### Delays and cancellations

| Item | What really happened | Where it is said | What the tools say | What a good run notices |
|---|---|---|---|---|
| RL-047 saved column mappings | **Cancelled** at the product leadership meeting, 30 Sep: supplier portal v2 (RL-600, 2027) replaces file mapping | `emails/03` (Viktor's proposal, Samir agrees), transcript 06, Pontus's note | Roadmap: cancelled on 1 Oct (Samir did update Linear). **Feedback portal FB-014 still says "Planned for November"** | It leaves the Q4 list. Bergstrand asked for it (August call, FB-014) and nobody has told them: Samir "will ask Petra", nothing shows Petra was asked. A risk for the brief, not a tier |
| RL-051 supplier answers keep their unit | **Moved to 2027 Q1**, same meeting | Transcript 06 and Pontus's note only | Roadmap: still planned for 14 Dec. Portal FB-024: "Planned for December" | Only a meeting knows. The weekly list must not show it as a December release |
| RL-042 factor library 2026.4 | **Slips two weeks** to 23 Nov: the data partner's dairy update failed validation | `#produkt` 2 Oct, 16:40: said first by Agnes Mortensen (factor data lead, not the owner), confirmed by Nadia Rask (owner) at 16:58 | Roadmap and market calendar: 9 Nov ("I'll fix Linear on Monday") | The source rule needs the owner's statement: Agnes alone is not enough, Nadia's confirmation is. CS gets two weeks less warning for three customers whose dairy numbers move more than 5% |
| RL-043 factor version on every report line | **Moves to January**: needs the 2026.4 version ids; the freeze starts 15 Dec | `#produkt` 2 Oct, 17:12, Jonas (owner), in a thread reply | Roadmap: 16 Nov. Portal FB-016: "Planned for November" | A knock on delay said once, in a thread. Easy to miss |
| The Q4 count | Frida counts "eighteen small updates" on 1 Oct (transcript 05) | Transcript 05 | Roadmap: seventeen planned, one cancelled; really fifteen for Q4 once RL-051 and RL-043 are out | Frida's list was out of date the day she made it |

### Challenges to the investments

| Investment | The challenge | Where | What a good run notices |
|---|---|---|---|
| RL-500 scenario comparison | **The CRO asks whether Rootline picked the wrong bet in June:** thirteen accounts want a costed reduction plan (FB-002), and "half of the people who say scenario mean the second thing". Pontus: the first half of a plan; Erik's own Storhaug note says the supplier comparison would have answered it. Ida parks it until the January planning | `emails/01`, 28 to 30 Sep | Counter evidence for market need and validation, from inside. Not settled; it does not cancel 17 accounts and the Nordlys deal. Belongs in "Where more information would help" and the explainer's questions, not in a lower score on its own. Watch for over reading: the CRO's "half" is his impression, not a count |
| RL-500 | **An early access customer questions its fit:** Tre Kronor's purchasing will use it (the tiebreak rule), the CFO wants cost per tonne for a March board paper. Samir wants them to stay. Call on 6 Oct | `emails/02`, 30 Sep to 1 Oct | Early access may lose or reshape a member; the "three of four on a signed decision" bar depends on purchasing, not the CFO. A rescore trigger if Tre Kronor leaves |
| RL-203 consolidation | **The head of engineering wants to pause it** until the refresh ships. Jonas against; Olle: a pause saves about two weeks and costs two later. **Not decided: week 42.** Target stays 7 Dec, nobody tells customers a new date | `emails/03` (29 Sep), transcript 06 (30 Sep) | The date could move into another quarter: name it as a rescore trigger with its date (week 42). **The transcript 06 summary says it "was moved to Q1 2027": wrong**, the call decides nothing. Viktor's "four groups" undercounts: 26 tickets also come from others (Sjöland, April) |
| RL-100 interface refresh | **The CRO:** 105 engineer weeks, no deal names it. **A customer:** Sjöland (renewal 11 Nov, amber) asks to stay on the old screens until January; the reporting export is what it uses in December. Pontus: no two interfaces; the refresh is the road to brand views | `emails/01`, `emails/04` | Not a demo release, but the evidence for a later RL-100 run: no deal, a renewal that needs what the refresh unlocks, and a customer who fears its timing. The reporting export's January fallback (W40 update) would help Sjöland |
| RL-034 supplier sort | **A design challenge, not a reversal:** Mira wants the sort to stick per user; a purchasing user at Nordvik wants A to Z (FB-122, 2 votes, no answer). Samir: not in the one engineer week | `#produkt` 22 Sep, `feedback-portal.csv` FB-122 | A reason for a precise release note (how to switch back to A to Z), not against the release. Two votes against thirteen tickets and seven accounts for it |

### For the demo, in short

- **RL-500:** the challenges add questions for the PM and thin evidence notes; they don't change the big deal override or the 17 accounts.
- **RL-202:** unchanged by 4a.
- **RL-203:** a contested date with a decision in week 42, and a wrong summary to ignore.
- **RL-034:** the release note must say how to switch back.
- **The weekly list:** RL-042, RL-043, RL-047 and RL-051 show dates that only conversations know.

## Step 4c: a second round, Claude's choice (D-66, 12 Oct 2026)

Victor: "let's add more messy data for fun! You get to decide on what would make this data more believable." Chosen to touch the three releases still to score, and the way launches really go wrong.

| Item | What happened | Where | What a good run notices |
|---|---|---|---|
| RL-034 behind a flag | Samir turned the emissions sort on for Havsfisk on 30 Sep. Havsfisk's purchasing manager asks why they haven't used the list before every supplier review; he also wants A to Z, and for it to stick | `#produkt` 30 Sep; `emails/05` (1 Oct) | The strongest kind of proof exists for RL-034: a customer using it. One customer, one day, but real. The roadmap still says in progress (it doesn't track flags). A second purchasing user wants A to Z: Mira's point gets a name. Purchasing is the audience, which links to RL-036 |
| RL-202's requester wants something else | Fjordlaks (FB-004, April) needs an email when a long load finishes or fails, not a message on screen: "I start the full year of landings at four o'clock and go home." Jonas: not planned, Q1 at best | `emails/06` (29 to 30 Sep) | The customer behind the request is not served by the release. Lowers what the release can claim, not whether it ships. Belongs in the explainer's questions and the release note's honesty |
| RL-203's scope is the wrong shape | Olle's test on Nordkost's real data times out at four entities: "it's entities times articles, not entities". The fix covers five or more entities of normal size; Nordkost needs 3 to 4 more weeks, outside the 7 Dec scope | `#produkt` 1 Oct | Nordkost (8 of the 26 tickets, the biggest source) is not fixed on 7 Dec. Reach and validation drop; the roadmap title is now misleading; a message risk if anyone says "consolidation is fixed" |
| Sydfood's expansion on hold | Görel: the CFO froze spending outside the core budget until March; brands five and six wait regardless of the fix. Daniel leaves the CRM to Sofia; OPP-2614 still says it waits on consolidation, close 18 Dec | `emails/07` (2 Oct); `pipeline.csv` OPP-2614 | **The big deal override doesn't fire:** the CRM notes still match the "any multi brand group" clause, but the rubric reads the newest statement about a deal (D-70), and the newer email says the deal is not waiting on the release. A good run says so, and that on the CRM alone it would have moved RL-203 to Tier 2 |
| A date in writing | Sofia to Nordlys (2 Oct): the improvement for five or more entities "is planned for early December". Two days after the meeting said nobody gives customers a new date, and while the pause is undecided | `emails/08` | A written commitment to a 46,000 EUR prospect on a release that may pause in week 42, and that doesn't cover very large entities. A message risk for RL-203's launch, and a reason for product to know before week 42 |
| The release note draft | Ebba's October draft lists progress messages for 13 Oct (a day before the slip) and calls RL-036 a "supplier scorecard", the word sales uses for RL-401. Frida catches the name; the draft isn't fixed yet | `#marknad` 1 Oct | Names are not ids. "Scorecard" means two releases; "progress bar" means RL-202. The draft's dates are older than the owner's |
| A webinar booked before scoring | Ebba holds Thu 12 Nov for a refresh webinar at Pontus's ask; the invite is held until Frida scores | `#marknad` 1 Oct | Launch work committed before tiering (RL-100). Not a demo release, but the weekly list or a later RL-100 run should flag it |

### For the demo, in short

- **RL-034:** validation can reach "results from customers testing it", from one customer.
- **RL-202:** the requester isn't served; the release still helps people who wait.
- **RL-203:** the Nordkost gap, the Sydfood hold and Sofia's written date. Three reasons a good run keeps it small and precise.

## Step 4d: the CEO's 2027 requests (D-72, 12 Oct 2026)

Victor: "add in some product requests from the CEO based on where the market is heading in 2027 ... the CEO influenced the roadmap which has challenges to the scoring rubrics." Built from what the data already said: the board asked on 11 Sep whether food and beverage is too narrow (W38 pipeline review); the CEO had already asked for RL-710; sales was already selling deforestation tracing to Vretstorp outside the price list.

| Item | What happened | Where | What a good run notices |
|---|---|---|---|
| The memo | Ida, 25 Sep: "the obligation is moving down the supply chain". Three moves for 2027: supplier evidence for deforestation, grocers as customers, purchasing as a user; RL-710 stays. "None of this is in our 2026 goals" | `emails/09` | The CEO's view is evidence about direction, not about customers. It belongs in strategic signals only where a goal says so; the 2026 goals don't |
| Two roadmap rows with no demand | RL-720 (EUDR evidence) and RL-730 (grocer package), discovery, added 28 Sep by Pontus at Ida's ask, no demand ID, no engineer weeks; they share Pontus's six weeks with RL-710 | `roadmap.csv`; `#produkt` 28 Sep | Discovery items aren't releases: not tiered. If ever scored, they come out low on validation and customer request by design. A good run says "early", as the CEO asked, and doesn't inflate them |
| The deadline the product would miss | Pontus: EUDR applies to large and medium operators from 30 Dec; anything built in 2027 lands after it | `emails/09` | A market date that falls before the release can't trigger the market date override |
| Sales ahead of the packages | Vretstorp was offered palm and soy origin tracing as an add on that isn't on the price list (OP-PKG) | `4-asset-usage-agent/transcripts-w37-onward/sales/05-vretstorp-konserv-pricing-follow-up.md`; `emails/09` | One real customer conversation behind RL-720, and a packaging question nobody owns |
| Pressure on a tier before it is scored | Ida: if the grocer export (RL-401) "comes out as a release note, I want to talk before it's decided. That one is the start of 2027, not a fix." Pontus: RL-401 ships on 16 Nov as an export; what it becomes is January's question | `emails/09` (2 Oct); `#produkt` 28 Sep | The score stays honest. The rubric has no CEO override; Frida's v1 lists it as a known gap (section 11): she decides, and a decision against the score is logged with who asked. RL-401's assessment should show the score, the CEO's view and the gap between them |
| The marketing question | Josefin: "Do you want the score to count where you think the market is going, or to tell you honestly that you are early?" Ida: "Tell me honestly that I'm early." | `emails/09` | The CEO's own answer protects the rubric, and the next sentence tests it. For the blog: the moment a scoring model meets the person who sets the strategy |

