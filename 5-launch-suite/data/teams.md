# Rootline product and engineering, 2026

_Fictional. Who builds Rootline's product, how the work is split, and how much the team can take on in a year. The roadmap's `team` and `owner` fields use these names._

## People

| Name | Role | Team | Notes |
|---|---|---|---|
| Pontus Grahn | Head of Product | Reports to the CEO, Ida Brandt | Owns the interface refresh, reduction planning (exploring) and the look beyond food and beverage. The "head of product" customers hear about: his written answer on abatement planning reached customers in August and September |
| Jonas Wik | Product Manager | Footprint | Corporate footprint, group consolidation, reporting, assurance, loading speed. Already in the Slack export, and the PM the CRO takes customer questions to ("Send it to me in writing and I will take it to Jonas myself", W35 pipeline review) |
| Nadia Rask | Product Manager | Products | Product footprints, recipes, factor library releases, exports and template formats |
| Samir Haddad | Product Manager | Supplier | Supplier engagement, the supplier view and ranking, scenario comparison, supplier portal |

Pontus Grahn, Nadia Rask and Samir Haddad are new to the Rootline data with this file. Jonas Wik, Ida Brandt and everyone in commercial roles already appear in `example-data/`.

## Teams

| Team | PM | Engineers | Owns |
|---|---|---|---|
| Footprint | Jonas Wik | 7 | Core platform: corporate footprint, entities, consolidation, reports, assurance access, performance |
| Products | Nadia Rask | 6 | Rootline PCF: product models, recipes, co products, factor service, exports. Works with the factor data team |
| Supplier | Samir Haddad | 7 | Rootline Supplier: requests, farms, supplier view, rankings, scenario comparison |
| **Total** | 3 PMs | **20** | |

Shared across the three teams: **two product designers** (both on the interface refresh, one moved to scenario comparison from July) and a **factor data team of three climate data specialists**, who prepare the quarterly factor releases. Neither is counted in the 20 engineers.

The teams follow Rootline's three products (Core, PCF, Supplier) even though customers have bought packages (Supply and Group) since November 2025. Work that cuts across packages, like the interface refresh, is led by the head of product.

## How much this team can build in a year

There is no published benchmark for how many features a team ships per quarter. Sources that look for one say to measure your own throughput instead. So the estimate is built from capacity.

| Step | Number | Basis |
|---|---|---|
| Engineers | 20 | Three teams of 6 to 7 |
| Working weeks per engineer | about 42 | Swedish holidays (25 days plus public holidays) and a quiet July |
| Engineer weeks in a year | **about 840** | 20 x 42 |
| Share left for roadmap work | about 55% | Maintenance and technical debt take roughly a fifth to a third of engineering time in developer surveys; planning guides add a 15 to 20% buffer for bugs and unplanned work |
| Engineer weeks for the roadmap | **about 460** | 840 x 0.55 |

**What the 2026 roadmap asks for:** about 516 engineer weeks (the sum of `size_ew_2026` in `roadmap.csv`). 340 go to the six investments, 132 to the 51 smaller updates, 37 to internal work and 7 to discovery. The plan was over full by about 12% from December, which is why four of the six investments slipped a quarter or more.

**Ratio check.** 3 PMs to 20 engineers is 1 to about 7, inside the classic rule of thumb of one PM for 6 to 10 engineers. At small companies product managers are about 13% of research and development headcount (Pave), which matches 3 PMs and 2 designers next to 20 engineers.

## How customer feedback reaches product

- **CSMs and the solutions engineer** raise it after calls; the call notes in `example-data/` show it ("Raising it again", Havsfisk QBR)
- **The `#kundfeedback` Slack channel**, where Jonas Wik answers (`example-data/07-slack-export.md`)
- **The CRO in writing**, from the weekly pipeline review (`example-data/09-internal-calls/`)
- **Release notes** go to customers by email and, from April, in the app (RL-017)

## Sources for the capacity estimate

- Pave, R&D org structure benchmarks: https://pave.com/blog-posts/research-development-org-structure-benchmarks
- Gartner Peer Community poll on PM to engineer ratios: https://www.gartner.com/peer-community/poll/ratio-product-managers-software-engineers-every-1-product-manager-we-have
- Blackblot, on the lack of credible ratio data: https://www.blackblot.com/product-management-to-development-ratio
- Sonar, developers spend 30% of their time on maintenance: https://www.sonarsource.com/de/blog/developers-spend-30-of-their-time-on-code-maintenance-our-latest-survey-results-part-3/
- Stepsize via VentureBeat, about a day a week on technical debt: https://venturebeat.com/dev/stepsize-engineers-waste-1-day-a-week-on-technical-debt
- IdeaPlan, release planning buffer: https://www.ideaplan.io/glossary/release-planning
- Beamer, SaaS release cadence: https://www.getbeamer.com/blog/saas-release-notes-cadence
