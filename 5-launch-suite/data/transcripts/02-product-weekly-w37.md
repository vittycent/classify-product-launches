# Rootline internal: product weekly

**Date:** 2026-09-07
**Week:** 2026-W37
**Duration:** 34 min 12 sec
**Type:** Internal. Not customer speech. Never quotable externally
**Recorded in:** Conversation intelligence tool, auto transcribed, not corrected

**Rootline:** Pontus Grahn (Head of Product), Jonas Wik (Product Manager, Footprint), Nadia Rask (Product Manager, Products), Samir Haddad (Product Manager, Supplier), Viktor Kronqvist (Head of Engineering), Mira Åström (Product Designer), Linnea Hellman (Product Designer), Karin Wallin (Head of Customer Success, left 00:11)

---

**Auto generated summary:** The team agreed to keep the supplier sorting change inside the interface refresh and release both together in November. Engineering capacity is sufficient for Q4. Scenario comparison will be released to all customers in Q1.

---

[00:00:05] **Pontus Grahn:** Morning. Karin's here for the first ten minutes because the first item is hers as much as ours. The supplier screen. Mira, the test.

[00:00:14] **Mira Åström:** Three customers, their own data, the new supplier view. All three found the emissions column faster than in the old one. Two of three still clicked the name column first, out of habit, and then went looking for the ranking.

[00:00:29] **Karin Wallin:** That's Havsfisk in August, word for word. "Still opens sorted alphabetically, which is why I never saw the thing you showed me." Five months after we shipped the ranking.

[00:00:38] **Samir Haddad:** And it's in the support export every month since March. Not many tickets, two or three a month, but always the same question. Where's the ranking.

[00:00:46] **Pontus Grahn:** The plan was that the refresh fixes it in November.

[00:00:49] **Samir Haddad:** The plan was that the refresh fixes everything in November. The default sort is one engineer week in the current interface. Sanna says it can go in this sprint.

[00:00:57] **Viktor Kronqvist:** It can. It's a default. It doesn't touch the refresh code.

[00:01:01] **Pontus Grahn:** [pause] Then why are we making people wait two months for a default?

[00:01:05] **Mira Åström:** Because it was in my design. Which is fine. It can be in both.

[00:01:09] **Pontus Grahn:** Decided. RL-034 comes out of the refresh and goes now. Samir, target?

[00:01:14] **Samir Haddad:** Thirteenth of October, with testing.

[00:01:17] **Karin Wallin:** Can CS tell customers?

[00:01:19] **Samir Haddad:** When it's shipped. Not before.

[00:01:21] **Karin Wallin:** Fine. Havsfisk, Fjordlaks, Nordvik and Rönnbäck will notice the day it happens. That's worth more than a release note.

[00:01:29] **Pontus Grahn:** Karin, anything else before you go?

[00:01:31] **Karin Wallin:** Bergstrand. Petra has the renewal decision call on the fourteenth. They will ask about scenario comparison. What can she put in writing?

[00:01:39] **Samir Haddad:** What Pontus wrote in August, plus the date we now have. Early access for a first group in November, no general date. Bergstrand is in the first group.

[00:01:47] **Karin Wallin:** Thank you. That's all I need.

[00:01:50] **Pontus Grahn:** Next. The refresh. I lost a week to the factor library model change, export screens are at seventy, and Viktor found me an engineer.

[00:02:00] **Viktor Kronqvist:** From Rasmus's team, from today until the end of October. Which means Products is one down for October.

[00:02:06] **Nadia Rask:** Which is the month I have four export fixes and the scorecard build.

[00:02:10] **Viktor Kronqvist:** I know. That's why I'm saying it out loud.

[00:02:13] **Pontus Grahn:** Nadia, what moves if you're one down?

[00:02:16] **Nadia Rask:** Not the scorecard export. Sales asks about it every week, Handelsbolaget most of all. The material names fix and the boundary label can slip a week. Nobody will notice a week.

[00:02:29] **Pontus Grahn:** Fine. Refresh stays at the tenth of November, then. Release candidate second of November.

[00:02:35] **Jonas Wik:** Can I raise the bigger number? We were twelve percent over capacity in December. Four of six investments have slipped. We're not over by less now.

[00:02:43] **Viktor Kronqvist:** We're over by about the same. Roughly five hundred and sixteen engineer weeks planned against four hundred and sixty available, and the year is three quarters gone.

[00:02:52] **Pontus Grahn:** What goes, if something has to?

[00:02:55] **Jonas Wik:** Not step three of loading. The groups have waited a year.

[00:02:58] **Samir Haddad:** Not early access.

[00:03:00] **Nadia Rask:** Not the scorecard.

[00:03:02] **Pontus Grahn:** [laughter] Good. Then nothing goes and we watch it. Brand level views was always 2027. Supplier portal is discovery. Those absorb the slips.

[00:03:11] **Jonas Wik:** Brand views has three customers asking. Lindholm, Sjöland, and Nordflor now they've signed.

[00:03:17] **Pontus Grahn:** And it was always 2027, and they've been told 2027. Samir, scenario comparison.

[00:03:23] **Samir Haddad:** Second prototype round with Nordkost last week. They want to swap more than one material at a time. Linnea?

[00:03:30] **Linnea Hellman:** Their sustainability lead tried to swap the palm oil and the rapeseed together. The prototype only does one. She said "this is the question my COO will ask". So it's real.

[00:03:41] **Samir Haddad:** But not for early access. Sanna says several materials at once is another six to eight weeks.

[00:03:47] **Pontus Grahn:** Early access is one material at a time. Write it down so nobody promises otherwise.

[00:03:52] **Samir Haddad:** And I need help on that, honestly. Sales described it as available on two calls last month. Tobias corrected both.

[00:03:59] **Pontus Grahn:** I'll talk to Henrik. Again.

[00:04:02] **Linnea Hellman:** One design question for early access. Data quality under every number. Some of the supplier data is a certificate, some is an average. If we show a swap from an average to a certificate, the number moves partly because the data got better, not because the supplier is better.

[00:04:18] **Samir Haddad:** That's the most important thing in the whole feature.

[00:04:21] **Linnea Hellman:** So I'd like to show it. Every number says what it's made of.

[00:04:25] **Pontus Grahn:** Agreed. That's what makes it ours and not a spreadsheet.

[00:04:29] **Nadia Rask:** Scorecard export, quickly. Build started today. Sixteenth of November. I've decided to leave packaging and transport blank with a note rather than estimate, because two grocers ask for them and we don't collect them for every product.

[00:04:41] **Jonas Wik:** Sales will hate the blanks.

[00:04:43] **Nadia Rask:** Sales will hate an estimate more when the grocer asks where it came from.

[00:04:47] **Pontus Grahn:** Right. Last thing. Marketing.

[00:04:50] **Jonas Wik:** Ebba asked in the channel what needs more than the release note.

[00:04:54] **Pontus Grahn:** Everything we ship in Q4 ships before they plan Q4. That's the honest answer. Their planning is the third of November.

[00:05:01] **Samir Haddad:** I'd like early access not to be announced at all. Four customers. One material at a time.

[00:05:06] **Pontus Grahn:** And I'd like the refresh to be announced properly. A year of work and every customer will see it. I'll tell Frida.

[00:05:12] **Jonas Wik:** Who decides how big a launch is? Honestly, I've never known.

[00:05:16] **Pontus Grahn:** [pause] Marketing, I suppose. After we tell them.

[00:05:20] **Mira Åström:** Then we should tell them better.

[00:05:23] **Pontus Grahn:** Fair. Okay. Thanks, everyone.

[00:05:26] [Recording ended 00:34:12. The remaining items, sprint planning per team, are not transcribed.]

---

**Note added by Pontus Grahn after the call, 2026-09-07:**

Decided: RL-034, supplier screen opens sorted by emissions, comes out of the interface refresh and ships now in the current interface. Samir's team, one engineer week, target 13 October. Added to the roadmap today.

Interface refresh: one engineer from Products until end of October. Target 10 November holds. Products absorbs a week of slip on RL-038 and RL-039 if needed.

Scenario comparison early access: one material at a time, data quality under every number. Several materials at once comes after early access. Bergstrand can be told in writing: early access in November, no general date.

Capacity: still about 12% over. Nothing comes out this quarter; brand level views (2027) and the supplier portal (discovery) absorb slips.

Open: who decides how big a launch is. Nobody in the room knew.
