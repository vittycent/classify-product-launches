# Rootline customer demand, 2026

_Fictional. What Rootline customers asked the product to do in 2026, and what the roadmap did about it. Every roadmap row in `roadmap.csv` links here through its `demand` field._

**How to read it.** Each demand has an ID, what customers say in their own words, when it first reached product, the evidence inside the Rootline data (August to early October 2026), and the roadmap rows that answer it. Pattern IDs (P-01 and so on) and their counts of independent customer groups come from `2-structured-database/structured-database-w36.md`. Call counts come from the asset usage agent's report on the same calls.

**Before August.** The calls only cover 10 August to 2 October 2026. Earlier requests exist in two forms: what customers say about the past on those calls ("I knew in about March", "flagged it in May"), and the product team's own record of when an item was added, which is the `added` field in `roadmap.csv`. Both are used below.

---

## D-01 What happens after the number

- **In their words:** "You gave us the number and then you stopped." (Aalborg). "I need to know whether to wait for it or plan around its absence." (Nordflor). "On the roadmap means no." (Storhaug)
- **First reached product:** spring 2026. Asked for in April at Lindholm ("I had stopped expecting it"); Aalborg knew it was missing "in about March"; mentioned as being considered at a customer webinar and in a release note
- **Evidence:** P-04, 12 independent groups, confirmed, first seen 2026-W17. P-11 (no internal carbon price), 4 groups. Reduction planning requested on 8 calls in W33 and W34, and the reason 3 of 3 W34 review and exit customers may leave. A lost evaluation (Storhaug, 28 Aug) and a competitor showing a pathway module (W35 pipeline review)
- **Files:** `example-data/06-transcripts-cs/16-bergstrand-group-renewal-decision.md`, `example-data/06-transcripts-cs/17-aalborg-food-group-exit-interview.md`, `example-data/05-transcripts-sales/07-storhaug-meieri-evaluation-review.md`, `example-data/09-internal-calls/02-pipeline-review-w35.md`, `4-asset-usage-agent/transcripts-w37-onward/cs/11-nordkost-holding-product-answer.md`
- **Roadmap:** RL-015 single product what ifs (April), RL-016 supplier comparison (April), RL-500 scenario comparison with early access RL-501 (November), RL-048 hotspots page (December), RL-700 reduction planning, exploring only
- **Status:** partly served. The core ask, a costed pathway to a target year, is not in the next four quarters, and customers have been told so in writing

## D-02 The supplier screen hides the finding

- **In their words:** "still opens sorted alphabetically, which is why I never saw the thing you showed me" (Havsfisk). "I still do not really understand the supplier screen." (Fjordlaks)
- **First reached product:** March 2026, the month the ranking shipped with an alphabetical default ("five months later", Havsfisk, 14 Aug)
- **Evidence:** P-08, 3 groups, new
- **Files:** `example-data/06-transcripts-cs/06-havsfisk-nord-qbr.md`, `example-data/06-transcripts-cs/05-fjordlaks-check-in.md`
- **Roadmap:** RL-008 ranking by emissions (March), RL-032 inline help (September), RL-034 default sort by emissions (October, pulled forward), RL-100 interface refresh
- **Status:** fix in progress

## D-03 Slow loading and consolidation timeouts

- **In their words:** consolidation "times out if I add a fifth" (Sydfood). No sign a year of landings is loading (Fjordlaks)
- **First reached product:** December 2025 (P-07 first seen 2025-W50)
- **Evidence:** P-07, 5 groups, growing. Partly better by August ("The loading speed is better", Havsfisk)
- **Files:** `example-data/06-transcripts-cs/11-sydfood-group-check-in.md`, `4-asset-usage-agent/transcripts-w37-onward/cs/03-sydfood-group-check-in.md`, `example-data/06-transcripts-cs/05-fjordlaks-check-in.md`
- **Roadmap:** RL-200 with steps RL-201 (June), RL-202 (October), RL-203 (December)
- **Status:** in progress, no date given to customers

## D-04 Screens that do not say what they are

- **In their words:** an export that drops the data flags, a unit conversion nobody can find, two numbers on one page with the boundary in small print, a PDF without the date of its data, a locked module that looks broken
- **First reached product:** the PDF and file name complaints in the summer; the rest in late August and September
- **Evidence:** P-13, 4 groups, new (W35 and W36). The PDF date and file names were fixed within a week of being raised (Fjordmelk 25 Aug; Nordvik confirms 2 Sep)
- **Files:** `example-data/06-transcripts-cs/02-fjordmelk-check-in.md`, `example-data/06-transcripts-cs/03-nordvik-dairy-qbr.md`
- **Roadmap:** RL-030 (released), RL-035, RL-037, RL-039, RL-040, RL-043, RL-202, RL-100
- **Status:** mostly planned for Q4

## D-05 Access for one brand or entity, and knowing who uses the seats

- **In their words:** "there is no way to give a person read access to one entity without giving them the navigation for all of it." "the fourteen brand managers who actually make the decisions that change the number never once opened it." (Aalborg)
- **First reached product:** spring 2026; a purchasing manager has had his own read only login since April (Tre Kronor)
- **Evidence:** the Aalborg exit (20 Aug); a buyer asking for his own login unprompted (Lindholm, 14 Aug); 25 read only seats per Group customer (Nordflor kickoff, 7 Sep; Bergstrand, 14 Sep). Related: P-06, the brand has its own number, 6 groups
- **Files:** `example-data/06-transcripts-cs/17-aalborg-food-group-exit-interview.md`, `example-data/06-transcripts-cs/14-lindholm-brands-check-in.md`, `example-data/06-transcripts-cs/15-tre-kronor-renewal-review.md`, `4-asset-usage-agent/transcripts-w37-onward/cs/05-bergstrand-group-decision.md`
- **Roadmap:** RL-012 group overview (March), RL-041 who logged in (November), RL-300 brand level read only views (2027)
- **Status:** slipped from Q2; design under way

## D-06 Customer and importer formats

- **In their words:** export markets each want "documentation in its own format" (Vinga). "Product export shows material codes" (Sydfood)
- **First reached product:** before 2026; the Supply package already promised exports in every standard template format (November 2025)
- **Evidence:** P-10, 3 groups, new. Three common formats are covered today (Vretstorp, 31 Aug)
- **Files:** `example-data/05-transcripts-sales/03-vinga-sjomat-discovery.md`, `4-asset-usage-agent/transcripts-w37-onward/cs/03-sydfood-group-check-in.md`, `example-data/05-transcripts-sales/02-vretstorp-konserv-technical-deep-dive.md`
- **Roadmap:** RL-038 (October), RL-400 with RL-401 and RL-402 (November and December), RL-046 and RL-049 (more in every export)
- **Status:** slipped from Q2; build started in September

## D-07 Answer the customer's scorecard from one model

- **In their words:** "three weeks that would have taken me four months" (NPS). Bought for one customer request, then little reason to open the system
- **First reached product:** the reason most customers buy (use case 1)
- **Evidence:** P-05, 15 groups, confirmed
- **Files:** `2-structured-database/structured-database-w36.md`, `4-asset-usage-agent/assets/BLOG-4-first-retailer-scorecard.md`
- **Roadmap:** RL-001 article numbers and pack sizes, RL-010 English method notes, RL-401 grocer scorecard format
- **Status:** served; the formats work continues

## D-08 Supplier requests spend goodwill

- **In their words:** "Every form I send those farms costs me something. Not money. Goodwill." (Mjölkringen)
- **First reached product:** Q4 2025 CS feedback (farms giving up at the login screen); all year since
- **Evidence:** P-02, 13 groups, confirmed. The signature, not the template, decides whether a supplier answers
- **Files:** `2-structured-database/structured-database-w36.md`, `4-asset-usage-agent/transcripts-w37-onward/cs/02-nordflor-brands-kickoff.md`
- **Roadmap:** RL-003, RL-006, RL-013, RL-022, RL-026, RL-028, RL-033 (released); RL-045 (November); RL-600 supplier portal v2 (2027)
- **Status:** steady small fixes; the rebuild moved to 2027

## D-09 The data sits with somebody else

- **In their words:** "two of my eleven send data in a format that has to be rebuilt by hand every quarter, and that has been true for four quarters" (Bergstrand)
- **First reached product:** onboarding feedback all year
- **Evidence:** P-09, 10 groups, growing
- **Files:** `example-data/06-transcripts-cs/16-bergstrand-group-renewal-decision.md`, `example-data/06-transcripts-cs/01-vanerns-mejeri-onboarding.md`
- **Roadmap:** RL-007, RL-014, RL-018 (released); RL-047, RL-051 (Q4); RL-600 (2027)
- **Status:** partly served

## D-10 Assurance and audit

- **In their words:** "Our auditors will ask." (Lindholm, on the factor version). "Two years of assurance history coming with me." (Bergstrand). The value side: "Our auditor accepted it with three questions" (Aalborg)
- **First reached product:** groups preparing their first assured reports (BLOG-2, November 2025)
- **Evidence:** assurance is the value customers report most often in review calls (W34)
- **Files:** `example-data/06-transcripts-cs/14-lindholm-brands-check-in.md`, `example-data/06-transcripts-cs/16-bergstrand-group-renewal-decision.md`, `4-asset-usage-agent/assets/BLOG-2-group-first-csrd-report.md`
- **Roadmap:** RL-009, RL-023, RL-024 (released); RL-043, RL-050 (Q4)
- **Status:** a strength; two gaps planned for Q4

## D-11 There is no second person

- **In their words:** "if I get hit by a bus, right now, Vänerns has nothing." "I am the sustainability department. It is me and a folder." (Hedlunds)
- **First reached product:** visible all year in who logs in
- **Evidence:** P-01, 19 groups, the most independent groups of any pattern
- **Files:** `example-data/06-transcripts-cs/01-vanerns-mejeri-onboarding.md`, `2-structured-database/structured-database-w36.md`
- **Roadmap:** RL-910 internal usage page (March), RL-041 (November), RL-044 backup user prompt (November)
- **Status:** planned for Q4

## D-12 Built for the people who decide

- **In their words:** "nobody here has changed a single decision because of it" (Havsfisk). "It is a bit political, going to purchasing with a chart about their suppliers." (Fjordlaks)
- **First reached product:** Q4 2025 reviews (where do we start with suppliers?)
- **Evidence:** P-03, 10 groups. Champions without material for purchasing on 7 calls across W33, W34 and W37
- **Files:** `example-data/06-transcripts-cs/06-havsfisk-nord-qbr.md`, `example-data/06-transcripts-cs/05-fjordlaks-check-in.md`, `example-data/06-transcripts-cs/11-sydfood-group-check-in.md`
- **Roadmap:** RL-005, RL-008, RL-016 (released); RL-036 (October); RL-100, RL-300
- **Status:** partly served

## D-13 Units and weights

- **In their words:** "A crude oil intake that was about four times what it should have been." (Nordolie, a unit mismatch flagged in May)
- **First reached product:** May 2026 (Nordolie)
- **Evidence:** one implementation stall; per can figures redone by hand because the export only gives per litre (Bryggeri Kvarnen, 14 Sep); fishing customers count fuel per kilo landed (Vinga, 17 Aug)
- **Files:** `example-data/06-transcripts-cs/19-nordolie-implementation-stall.md`, `4-asset-usage-agent/transcripts-w37-onward/cs/06-bryggeri-kvarnen-check-in.md`, `example-data/05-transcripts-sales/16-vinga-sjomat-qualification.md`
- **Roadmap:** RL-040, RL-049, RL-051 (Q4); RL-600
- **Status:** planned for Q4

## D-14 Explain the change on every article

- **In their words:** a grocer clause asks for each article's change from last year to be "explained". "It doesn't say. It says explained." (Tre Kronor's sustainability lead). The CSM: "Then give them the split. Factor updates, your own data, method. You have it for the group already. For the articles it's the same logic one level down."
- **First reached product:** September 2026 (Tre Kronor, 7 Sep). The split by cause itself is old: restatements have been split into three causes since 2025, and solutions engineers show it per product in demos ("three of the four is our factor update", Vinga, 1 Sep; Nordflor, 18 Aug)
- **Files:** `4-asset-usage-agent/transcripts-w37-onward/cs/01-tre-kronor-renewal-cfo.md`, `example-data/05-transcripts-sales/05-vinga-sjomat-evaluation-call.md`, `example-data/05-transcripts-sales/09-nordflor-brands-demo.md`
- **Roadmap:** RL-046, the split on every article line in exports (November)
- **Status:** served on screen; planned for exports

## D-15 Invitations land in junk

- **In their words:** "the email they get is from a noreply address and looks like spam" (Sydfood, 12 Aug)
- **Files:** `example-data/06-transcripts-cs/11-sydfood-group-check-in.md`, `4-asset-usage-agent/transcripts-w37-onward/cs/03-sydfood-group-check-in.md`
- **Roadmap:** RL-031, released 1 Sep, confirmed fixed on 9 Sep
- **Status:** served

## D-16 Leaving without losing the data

- **In their words:** "How much would it cost to keep it in a, what do you call it, a frozen state?" (Kallvatten)
- **Evidence:** P-15, 2 groups, new: the best informed buyers negotiate the exit, not the price
- **Files:** `example-data/06-transcripts-cs/09-kallvatten-renewal-review.md`, `example-data/06-transcripts-cs/16-bergstrand-group-renewal-decision.md`
- **Roadmap:** RL-050 change log export (December); RL-820 frozen archive, declined
- **Status:** partly served, partly declined

## D-17 Requests from outside food and beverage

- **In their words:** "We are not a food company and the tool knows that better than the salesperson did" (NPS)
- **Evidence:** two non food accounts churned or will not renew; the CRO approved a second packaging account against the AE's objection. Leadership wants a path out of food and beverage
- **Files:** `example-data/05-transcripts-sales/15-nordisk-emballage-qualification-call.md`, `example-data/09-internal-calls/03-pipeline-review-w36.md`, `1-example-company/example-context-company.md`
- **Roadmap:** RL-810 declined (PFAS); RL-710 market exploration, asked for by the CEO, not by customers
- **Status:** a leadership question, not a customer request

## D-18 A number on pack for consumers

- **In their words:** two shelf competitors put a carbon figure on the can (Falkenberg)
- **Files:** `example-data/05-transcripts-sales/06-falkenberg-bryggeri-discovery-and-demo.md`
- **Roadmap:** RL-800, declined in April
- **Status:** declined

## D-19 The reporting rules changed

- **What happened:** the reporting scope changed in June 2026. Customers asked what it meant at the June webinar; their customers' scorecards did not change (CSF)
- **Files:** `4-asset-usage-agent/assets/WEB-scope-change-customer-webinar.md`, `4-asset-usage-agent/assets/CSF-customer-scorecard-framing.md`
- **Roadmap:** RL-027, released 22 June
- **Status:** served. A market moment, not a customer request

## D-20 Food specific modelling

- **What it covers:** co products, seasonal sourcing, recipe versions, farms behind cooperatives, and the factor library. Rootline's claimed strength ("We know how the industry works")
- **First reached product:** onboarding feedback, all year
- **Files:** `1-example-company/example-context-company.md`, `example-data/05-transcripts-sales/18-hedlunds-bageri-discovery.md`, `example-data/05-transcripts-sales/04-smakbolaget-demo-and-pricing.md`
- **Roadmap:** RL-004, RL-007, RL-011, RL-019, RL-021, RL-022, RL-025, RL-029 (released); RL-042 (November)
- **Status:** served, quarterly

## D-21 What the November 2025 packages promised

- **What it is:** not a customer request. The new packages (Supply and Group) promised allowances the product had to count and support
- **Files:** `4-asset-usage-agent/assets/OP-PKG-packaging-old-vs-new.md`
- **Roadmap:** RL-001, RL-002 (January)
- **Status:** served

## D-22 Customers do not hear what changed

- **In their words:** "I kept hoping something would appear in a release note." "Nobody from product ever asked me a single question." (Aalborg)
- **Files:** `example-data/06-transcripts-cs/17-aalborg-food-group-exit-interview.md`
- **Roadmap:** RL-017 what's new panel (April)
- **Status:** partly served: the panel shipped, the asking did not

## D-23 IT and security reviews

- **What it is:** security questionnaires and data terms in procurement; data security and exit terms came up on 7 calls across W33, W34 and W37
- **Files:** `example-data/10-email-threads/05-nordflor-brands-security-questionnaire.md`
- **Roadmap:** RL-020 single sign on on both packages (May)
- **Status:** served. Customers on the old module contracts get it when they move to a package

---

## Asked for, not on the roadmap

| Request | Evidence | Why not |
|---|---|---|
| Do the first year for us | Three lost or churned accounts chose a consultant or wished someone had done it for them (Vanilj och Co, Ödeshög, Hedlunds; the asked for, not served table in the structured database) | A services question, not a product one |
| Water and biodiversity alongside carbon | Never raised in the calls | No demand found |
