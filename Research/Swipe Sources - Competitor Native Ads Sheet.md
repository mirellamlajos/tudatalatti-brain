---
summary: "Pointer and read of the team's competitor swipe spreadsheet ('Competitor Scraping - Native ads másolata') — the Savary Tools/Bolthero tabs (native-ad structure reference, ~250 rows), the Grounding Well tab (the health-lane source, 88 rows with Hungarian translations, adapted copy, whitelisted page, landing page and campaign name), and what it tells the brain about how the team adapts ads."
type: research-source
brand: Tudatalatti Kontroll
source_url: https://docs.google.com/spreadsheets/d/1A1OUmbPs8sJ0jp75IFluqEGyxkrwDyzYbz6Mi5RKff8/edit
read_on: 2026-09-26 (via the Drive connector; only the first ~13 rows of each tab were returned, so the counts below are ranges from the sheet, not full reads)
last_updated: 2026-09-26
---

# Swipe Sources — the Competitor Native Ads Sheet

The CEO shared this on 2026-09-26. It's the operating swipe file behind the storytelling format ([[Winners - Ad Library]] W-001). Columns are consistent across tabs: **ID · Brand · Page Name · Meta Library ID · image link · launch date · headline · copy**, and on the Grounding Well tab the team's own working columns.

## Tabs

| Tab | Rows | What it is |
|---|---|---|
| **Grounding Well** | ~88 | The health-lane source. Brand rows: "Grounding Well," "Journal GroundingWell," "GroundingWell." **Page name on every row: "Amber Hayes"**, a whitelisted persona page. Launch dates Jan–Jun 2026 |
| Savary Tools/Bolthero (weekly tabs: June, July, 27.7–2.8, 3.8–11.8) | ~250 | A truck/RV tool brand's native ads. Whitelisted pages: **John Miller, Mike Hartwell, The Home Garage Journal.** Not our niche; it's the **structure library** for first-person, long-form, "the dealer wanted $900" native ads |
| WildBear competitors | ~88 | More Savary rows under the John Miller page |
| Sheet2 | 5 | Scratch budget arithmetic (four ad sets at ≈ €24–28/day, ≈ €749 over 7 days). Low confidence on what it refers to |

## The team's working columns on the Grounding Well tab

`Hungarian translation` → `Image for ads - final` → `Adapted HUN copy` → `Headline` → `FB page` → `URL landing` → `Hirdetéssorozat elnevezése` (campaign-series name). This is the swipe → translate → adapt → assign page → assign landing page → name the series pipeline, written down. Only some rows are adapted; the rest are raw translations waiting.

### Adapted so far (from the rows returned)

| Series name | Source hook (Grounding Well) | Adapted Hungarian opener | FB page | Landing page |
|---|---|---|---|---|
| **Légiutas** | "I've been a flight attendant for 26 years…" | *„26 éve vagyok légiutas-kísérő. Fél évvel…"* | Kiss Ildikó egészség | `/pages/f…` |
| **Menopauza** | "I was diagnosed with menopause at 46…" | *„46 éves voltam, amikor közölték: beállt…"* | Kiss Ildikó egészség | `/pages/m…` |
| **Ízület** | "Forwarded message by Dr. Sarah: for those…" | *„Dr. Kovács továbbított üzenete: Azoknak…"* | Lajos Antal Anthony | `/pages/i…` |
| **Van valakid** | "'Are you seeing someone?' That's what my husband…" | *„»Van valakid?« Ezt kérdezte a férjem múlt…"* | Kiss Ildikó egészség | `/pages/m…` |
| **Kimerültség** | "I'm going to sound crazy, but hear me out…" | *„Tudom, hogy őrültségnek fog hangzani, de…"* | Lajos Antal Anthony | `/pages/f…` (fatigue) |

All five use the headline **„A változás valódi kulcsa"** (the real key to change). W-001 (autoimmune) is a sixth from the same source. GetHookd ids for the sources: Légiutas ← Amber Hayes 101122656 · Menopauza ← 101122687 · Ízület ← 75250657 ("Dr. Sarah") · Kimerültség ← 100366499 · W-001 ← 176156706. Full read of the network: [[Swipe Sources - Grounding Well Network (GetHookd 2026-09-26)]].

**Raw-translated, not yet adapted (from the sample):** "Don't waste your money on grounding sheets…", "Mom, I need you to sit down", "I'm shaking as I type this", "Three days before my grandmother died", "Mom, don't freak out", "Stop tinnitus today", "Gabapentin is one of the most prescribed…". Several of these are condition-specific (tinnitus, nerve pain); each needs the hard-floor check before adaptation ([[Compliance and Claims Watchlist]] override).

## What this tells the brain

1. **The brand runs two kinds of pages:** Antal's own ("Lajos Antal Anthony") and a **whitelisted health persona page, "Kiss Ildikó egészség."** So the CEO's "whitelisted pages also work" has a name. Grounding Well's "Amber Hayes" is the model.
2. **One advertorial landing page per theme** (fatigue, menopause, joints…), not one per ad. The theme is the unit: series name = landing page = audience problem.
3. **Dr. Sarah became Dr. Kovács.** An invented doctor endorsing the book is one step past a composite narrator. Under the hard floor ("no doctor-bashing" cuts both ways: no fake doctors either) this one needs the CEO's eyes before it runs again.
4. **The Savary library is the better structure teacher.** Its hooks are price-anchored ("$275/hr tech vs $89 tool. Same bolt.") and identity-anchored ("If your hands are older than your Cummins…"). For a 50+ reader, those translate to "the therapist wanted 25,000 Ft an hour; the book is 6,000" and "if you've been tired longer than your grandkids have been alive."

## Still needed from the sheet

- The full Grounding Well tab (only 13 of ~88 rows came through; the Drive connector's read and metadata calls both stop short of that tab, and the CSV export URL needs a signed-in session). **Ask the team to download the tab as CSV and drop it into `Research/`,** or share it as a plain Google Doc.
- The English original of W-001 (the CEO said it's attached; it hasn't arrived).
- Which of the five adapted series ran, and their numbers.

## The Grounding Well whitelist network in GetHookd (read 2026-09-26)

A landing-page-domain search across `groundingwell.com`, `journal.groundingwell.com`, `article.groundingwell.com` and `es.groundingwell.com` finds **≈3,000 ads, ≈1,270 active**, spread over the main page and a set of persona and "community" pages. This is the "whitelisted accounts" the CEO asked the swipe file to include. GetHookd brand ids in brackets (use as `brand_id` in `search_ads`).

| Page | GetHookd id | Active ads (2026-09-26) | What it runs |
|---|---|---|---|
| **GroundingWell** (main) | 697 | 801 | Product-page videos ("Get Grounded Today"), sale statics, a long menopause copy ("Wake Up Feeling Normal Again") |
| **Amber Hayes** | 306559 | 37 | The page in the team's sheet. Persona advertorials: "The 'weird sheet'…", "The only grounding brand that isn't a scam" |
| **Wellness Today** | 689 | 153 | "Fix Yourself at the Cellular Level", "Feel Like Yourself Again" |
| **Grounding Health Benefits** | 698 | 152 | Advertorial and listicle pages (`/pages/fm01`, sleep-aid listicle) |
| **Charlotte Miller** | 2741196 | 53 | "Get Grounded While You Sleep!" persona |
| **Shelly L. Gayton** | 7011100 | 12 | "Why diuretics never touched the swelling" (edema angle) |
| **Jennifer Lauren** | 4307446 | 8 | "The 'Weird Sheet' At Our Women's Retreat" |
| **Laura Ashworth** | 7011070 | 4 | "The truth about tinnitus", "Natural Relief in Weeks" |
| **Nerve Support Community** | 11289280 | 5 | Neuropathy listicle; "The Mat That Helps Relieve Neuropathy" |
| **Lymphatic Support Community** | 11316235 | 3 | Lymphedema listicle |

**Pattern worth copying:** one persona page per *angle* (a named woman for the story ads, a "community" page for the condition listicles), each with its own advertorial or listicle page. The brand already does the first half ("Kiss Ildikó egészség"); the "community" page idea is untested here.

**GetHookd spend estimates** on these rows are third-party estimates ("0 – $500", "$501 – $2,000") and are not used to rank anything ([[Analyzing Public Ad Accounts]]).
