---
handoff: tiering-weekly
handoff_version: 1
week: 2026-W41
run: 2026-10-05
rubric_version: v1
status: draft
approved_by:
approved_on:
---

# Tiering, week 41

_Run 5 October 2026. Rubric v1. First run: no earlier run to compare with, so every Q4 release counts as new._

**This week:** the 24 Q4 releases Frida counted on 1 October. 16 scored on the routine path and 12 stay there; 10 go to the full path (6 by the rule, 2 moved by Frida, 2 for the monthly sample); no rescores. 2 are not tiered: RL-047 was cancelled on 1 October, and RL-051 moved to 2027 in a meeting the roadmap tool hasn't heard about. Of the 18 small updates Frida counted, 15 still ship this quarter. Not counted: three discovery items for 2027 (RL-710, and RL-720 and RL-730, added at the CEO's ask on 28 September). They are not releases, so they aren't tiered.

## 1. Routine list: approve in one pass

_The agent's total is under 47 and no gate or override is in play. Approve the list, or move any release to the full path. Every release here fails the revenue gate (no deal names it), which caps it at Tier 3 and changes nothing below 50._

| Release | Title | Tier | Total | Why, in one line | Move to full path? |
|---|---|---|---|---|---|
| RL-034 | Supplier screen opens sorted by emissions | 3 | 45 | Proof from a customer using it (Havsfisk, behind a flag) and two goals; no deal names it | **Yes, by Frida:** the supplier comparison got one hour in April and has closed deals since; she won't under-launch the next small change that matters. [Assessment](../RL-034-supplier-sort/01-tiering/tiering-2026-10-05.md) |
| RL-035 | Exports keep the primary and average data flags | 4 | 29 | 16 tickets and 5 accounts, expected; 1 point under the Tier 3 line, so it stays in Tier 4 | **Yes, monthly sample** |
| RL-036 | Quarterly supplier ranking for purchasing, on one page | 3 | 44 | Purchasing's own page (G4); Havsfisk's purchasing team asked for exactly this on 1 Oct. The release note draft calls it "supplier scorecard", the name sales uses for RL-401 | No |
| RL-037 | Locked features say "not in your package" | 4 | 23.5 | 10 tickets: a product that looks broken | No |
| RL-038 | Product export shows material names | 4 | 25 | 4 tickets, 4 accounts; expected | No |
| RL-039 | Label the boundary on both numbers | 4 | 21.5 | 3 accounts; clarity on a page everyone uses | No |
| RL-040 | Unit conversions visible and editable | 4 | 24.5 | 9 tickets, 4 accounts | No |
| RL-041 | Admin view: who logged in this quarter | 4 | 18.5 | 4 accounts; useful to admins and CSMs | No |
| RL-042 | Factor library 2026.4 | 4 | 24.5 | Expected; every customer recalculates. **23 November, not 9 November** (Nadia, owner, 2 Oct). Three customers' dairy numbers move more than 5%: CS needs to brief them even at Tier 4 | No |
| RL-043 | Factor version and data date on every report line | 4 | 26.5 | 10 tickets; auditors ask. **January, not 16 November** (Jonas, owner, 2 Oct): it leaves Q4 | No |
| RL-044 | Invite a backup user at month three | 4 | 28 | G2, and a pattern at 19 groups; 2 points under the Tier 3 line, so it stays in Tier 4 | No |
| RL-045 | Your name and signature on supplier requests | 4 | 26.5 | 18 tickets, 8 accounts. Samir left it out of his Q4 list on 2 Oct; the tool still says 23 November: confirm it is still on | **Yes, monthly sample** |
| RL-046 | Change by cause on every article line in exports | 4 | 24 | 5 accounts; a grocer clause | No |
| RL-049 | Exports in every unit the product page shows | 4 | 24 | 6 accounts | No |
| RL-050 | Change log export an assurance provider can read | 4 | 17.5 | Group package only; 4 accounts | No |
| RL-202 | Faster data loading, step 2: progress messages | 3 | 33.5 | Expected, wins no deals. **20 October, not 13 October** (Jonas, owner) | **Yes, by Frida:** step 1 of the same investment got a campaign and broke a promise to the groups. [Assessment](../RL-202-progress-messages/01-tiering/tiering-2026-10-05.md) |

## 2. Going to the full path

_You score these first. Each gets its own assessment file._

| Release | Title | Why the full path | Assessment |
|---|---|---|---|
| RL-500 | Scenario comparison (early access, RL-501, 16 Nov) | Could be Tier 1 or 2; maturity gate; big deal override | [Tier 2, 60, provisional; override proposed](../RL-500-scenario-comparison/01-tiering/tiering-2026-10-05.md) |
| RL-203 | Faster data loading, step 3: consolidation past four entities | Within 3 points of the Tier 2 line; maturity gate. The big deal override would fire on the CRM note, but the newest statement says the deal is on hold, so it doesn't | [Tier 3, 49.5, provisional, borderline](../RL-203-consolidation/01-tiering/tiering-2026-10-05.md) |
| RL-202 | Progress messages on long loads | Moved by Frida | [Tier 4, 32, borderline](../RL-202-progress-messages/01-tiering/tiering-2026-10-05.md) |
| RL-034 | Supplier screen opens sorted by emissions | Moved by Frida | [Tier 3, 52.5, capped by the revenue gate](../RL-034-supplier-sort/01-tiering/tiering-2026-10-05.md) |
| RL-048 | Hotspots page | Within 3 points of the Tier 2 line (47.5); the revenue gate caps it at Tier 3. "Might be more, it's the first 'what next' thing we ship" (Jonas, 2 Oct) | To come |
| RL-100 | Interface refresh, phase 1 (10 Nov) | Could be Tier 1 or 2: every customer sees it. **Launch work is already committed:** a webinar slot is booked for 12 November, invite held until this score (`#marknad`, 1 Oct) | To come |
| RL-401 | Export format: grocer supplier scorecard (16 Nov) | Could be Tier 1 or 2: three open deals name it. Market date override possible: Gotlandskött's grocer deadline, 1 December. **The CEO calls it "the start of 2027, not a fix"** and wants to talk before it is sized (`emails/09`, 2 Oct). The score stays honest; a decision against it is Frida's, logged with who asked (rubric, section 11) | To come |
| RL-402 | Export format: importer documentation (14 Dec) | Maturity gate: still in design | To come |
| RL-035 | Exports keep the data flags | Monthly sample | To come |
| RL-045 | Your name and signature on supplier requests | Monthly sample | To come |

## 3. Rescores

None: first run.

**Coming:** RL-500 if Tre Kronor steps back from early access (call on 6 October) and when early access opens (16 November); RL-203 after the week 42 decision on a pause, and when it is ready to test with customers.

## 4. Sources that disagree

| Release | What one source says | What the other says | Which the rule picks | Would it change the tier? |
|---|---|---|---|---|
| RL-202 | `roadmap.csv`: 13 Oct. Ebba's release note draft (`#marknad`, 1 Oct, 11:20): 13 Oct | Jonas, the owner (`#produkt`, 1 Oct, 17:30; Friday update, 2 Oct): 20 Oct | 20 Oct: the owner's newest statement | No |
| RL-042 | `roadmap.csv` and `market-calendar.md`: 9 Nov | Agnes Mortensen (`#produkt`, 2 Oct, 16:40): 23 Nov, confirmed by Nadia Rask, the owner, at 16:58 | 23 Nov: the owner confirmed it. Agnes's message alone would not have been enough | No |
| RL-043 | `roadmap.csv`: 16 Nov | Jonas, the owner (`#produkt`, 2 Oct, 17:12): January, because it needs the 2026.4 version ids | January: the owner's newest statement. It leaves Q4 | No |
| RL-051 | `roadmap.csv`: planned, 14 Dec. Feedback portal FB-024: "Planned for December" | Transcript 06 and Pontus's note (30 Sep): moves to 2027 Q1 | 2027 Q1: a newer conversation beats the roadmap tool. Not tiered this quarter | Not tiered |
| RL-047 | Feedback portal FB-014 (5 Aug): "Planned for November" | `roadmap.csv`: cancelled on 1 Oct, after transcript 06 | Cancelled: the newer statement. Bergstrand asked for it and nothing shows it has been told | Not tiered |
| RL-203 | Transcript 06's automatic summary: "moved to Q1 2027" | The call and Pontus's note: decision in week 42; 7 Dec until then | The call: a summary never beats its source | No; in the assessment |
| RL-203 | `pipeline.csv` OPP-2614 (9 Sep): Sydfood's expansion waits on the fix, closes 18 Dec | Görel Wass (`emails/07`, 2 Oct): on hold until the March budget | On hold: the newest statement, so the big deal override doesn't fire | No; on the CRM alone it would have. In the assessment |
| RL-203 | Roadmap title: five or more entities | Olle Berglöf (`#produkt`, 1 Oct): a large entity times out at four; Nordkost isn't covered on 7 Dec | Olle: the newest statement about what the release does | Customer reach; in the assessment |
| RL-034 | `roadmap.csv`: in progress, 13 Oct | `#produkt` (30 Sep): on for Havsfisk behind a flag | Both: the tool doesn't track flags. General release 13 Oct | No |
| RL-036 | Ebba's draft: "supplier scorecard for purchasing" | The roadmap: quarterly supplier ranking. "Scorecard" is RL-401, the grocer export | Names aren't ids; Frida caught it, the draft isn't fixed yet | No |
| All | Frida (transcript 05, 1 Oct): eighteen small updates in Q4 | The roadmap and the conversations: one cancelled, two moved out of Q4 | Fifteen | No |

## 5. Pace check

| This quarter | Tier 1 | Tier 2 |
|---|---|---|
| Approved so far | 0 | 0 |
| Pace in the trigger table | about 1 | 3 to 6 |
| Status | On pace. RL-500 becomes this quarter's Tier 1 only if its override is approved; the agent suggests deciding that on 16 November | On pace. RL-500 (provisional) so far; RL-401 and RL-100 to come |

## 6. Monthly sample

First Monday of the month: **RL-035** and **RL-045**, picked at random from the routine list (seeded with the week, 2026-W41) and sent to the full path. Assessments to come.
