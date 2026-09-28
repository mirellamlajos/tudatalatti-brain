---
summary: "The weekly and daily loop the CEO asked the brain to run — Monday GetHookd swipe-file report and ad-comment analysis, Monday ideation, Mon–Tue build, Wednesday-onward launches so the weekend has fresh tests, a daily Slack finance report, and ongoing ad-account gap analysis — plus the 50-creatives-a-day target and the setup each workflow still needs. Operating rules for the AI are pending."
type: operating-cadence
brand: Tudatalatti Kontroll
status: requested 2026-09-25; not yet running
sources:
  - Research/Sources/Interview - CEO Brand Walkthrough 2026-09-25 (transcript).md
last_updated: 2026-09-25
---

# Operating Cadence and AI Workflows

What Mercédesz asked the brain to do on a schedule, and what each piece needs before it can run. Day-of-week logic comes from the brand's own data: **Monday and Tuesday are the weakest days, weekends the strongest.**

## The weekly loop

| Day | What happens | Method docs |
|---|---|---|
| **Monday** | **Report 1: GetHookd swipe file.** Best-performing ads from the best-performing brands, saved to the swipe file, with ad ideas the brand can use. | [[Analyzing Public Ad Accounts]] (its caveats on public-library "winners" apply), the GetHookd table in `CLAUDE.md` |
| **Monday** | **Report 2: ad-comment analysis.** Read the comments on the brand's Facebook and Instagram ads. Pull out questions, fears, hesitations, objections. | [[Customer Review Mining Method]], [[Hooks]] #1 comment-response |
| **Monday** | **Ideation session** with Mercédesz: the brain's recommendations, concepts picked. | [[Ideation and Brainstorming]], [[Choosing Which Ads to Iterate On]] |
| **Mon–Tue** | **Build.** Chosen concepts are produced (Mirella generates, Mercédesz approves). Finish by Tuesday. | [[Making Iterations]], [[Static Ad Recreation]], [[Visuals]] |
| **Wednesday →** | **Launch new ads.** No launches on Mon–Tue. | |
| **By the weekend** | Enough new ads live so testing runs through Sat–Sun, the best days. | [[Meta Creative Diversity (Andromeda v2)]] |

**Volume target:** launch tests every day, **at least 50 creatives a day.** Under the Andromeda rule in `CLAUDE.md`, 50 only counts as 50 if each one is visibly different in the first 3 seconds. Fifty near-duplicates get collapsed into a handful of entities.

## The daily loop

| Cadence | What | Needs |
|---|---|---|
| **Daily** | **Finance report to Slack.** | Which numbers (spend, revenue, ROAS, orders by product?), the data source (Meta API, Shopify, or the tracking sheet), the Slack channel, and a scheduled task |
| **Daily / ongoing** | **Ad-account analysis:** where the account is lagging, where the gaps are. From the Meta account directly, or from a Google Sheet export. | Account access or the sheet link. Method: [[Analyzing Ad Account Data]]. Decisions use the 4-day average ([[Team and Operations]]) |

## Setup checklist (nothing above runs until these are done)

- [ ] **GetHookd:** the workspace ("Mercedesz's Workspace", Team plan, ≈650 credits on 2026-09-26) has a **stale profile**: it says the customer sells a "public speaking / presentation confidence course" into US, GB, CA, AU, NZ, and has a saved product and brand profile for "Cogniva Brain Boost." None of that is this brand. The survey is pending. Fix: confirm with Mercédesz, then run the survey so niche and market are right (HU now; UK and ES soon). Until then, brand-scoped searches (Grounding Well, named competitors) work fine; niche-wide searches will point at the wrong market.
- [ ] **Swipe sources on file:** the team's sheet ([[Swipe Sources - Competitor Native Ads Sheet]]): Grounding Well (health lane, page "Amber Hayes") and Savary Tools/Bolthero (structure lane, pages John Miller, Mike Hartwell, The Home Garage Journal). The "best-performing brands" list starts there; add Hungarian self-development advertisers and the international subconscious / Healing Code / Silva / mindset advertisers.
- [ ] **Swipe file and boards:** the existing swipe file (71 ads on 2026-09-26) is mostly the other business's research (public speaking, language apps, a drinks brand) plus a handful of health natives (Julia's Blog, Relief Starts Today, Neuropathy Corner, Modern Health Journal, Brenda Burke). Boards: a Default Board (55), an "ads" board under "Language" (59), and five under "Public Speaking." **New boards for this brand start with the Grounding Well network board (2026-09-26).** Then one board per creative universe ([[Angle Map - ICPs to Creative]]) so Monday's picks land in the right lane.
- [ ] **Ad comments:** access to the brand's Meta Page and ad comments (Meta API, or exports pasted into `Research/`).
- [ ] **Slack:** the channel for the daily finance report and the Monday reports.
- [ ] **Data:** Meta ad account access, or the Google Sheet the team tracks in.
- [ ] **Scheduling:** set up the Monday and daily runs as scheduled tasks once the inputs exist.

## Operating rules for the AI

**Pending.** Mercédesz said she'd detail the operating rules later. When they arrive, they go here (or in `CLAUDE.md` if she wants them enforced on every session). Until then the brain runs on `CLAUDE.md` plus the Brand docs.
