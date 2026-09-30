# Tribal Knowledge

**Purpose:** What the team knows from experience but hasn't formally documented, such as patterns, instincts, and rules of thumb about customers, creative, and the business.


## From the CEO walkthrough (2026-09-25)

Rules of thumb the team runs on. Source: [[Interview - CEO Brand Walkthrough 2026-09-25 (transcript)]].

- **Monday and Tuesday are the weakest ad days; weekends are the best.** New ads launch from Wednesday so fresh tests are live by the weekend.
- **Read daily, decide on a 4-day average.**
- **Scale at ROAS 2.5; 2.0–2.2 is still fine; break-even is 1.7.** (Corrected by the CEO on 2026-09-26; her first numbers were 3 and 1.8.) ROAS 3–4 is "amazing."
- **The best day ever was 3–4k EUR of spend.** Nothing above that has been tried yet.
- **Customers want to understand it all consciously** before they trust it. The book's whole point is that they don't have to. Expect "how exactly does this work?" questions in comments.
- **Scepticism is the #1 objection.** Unanswered questions are #2.
- **Antal's face and the book cover are the two visual anchors that keep working.** Antal won't go on camera any more.
- **Founder-to-camera video fatigues in a few months.** Plan for re-cuts.
- **AI UGC hasn't worked for this brand** (as of Sept 2026).
- **Book 1 ads keep running even though Book 2 is out.** The two coexist; Q4 sells them as a bundle with the Guide.
- **The product needs a unique angle;** copying competitor strategies doesn't map well because nobody else sells this.
- **Mercédesz is the bottleneck by her own account.** Anything that shortens her decide-and-hand-off loop is worth more than another idea.

## From the autoimmune-ad walkthrough (2026-09-26)

- **Antal's verified Facebook page is the best launch pad.** Ads from it survive longest and scale furthest. His name is the authority. Whitelisted pages work for storytelling but less.
- **Statics with the book in them are the reliable mid/bottom-funnel workhorses**, in many iterations and combinations.
- **Long native storytelling (~1,000+ words, native photo) is the new scaler**, started recently. The CEO uses it for "bottom-of-funnel" targeting.
- **Swipe an English long-form ad → translate → fit the book in → test from Antal's page** is the fastest path from idea to live ad the team has found.
- **The method's name in the team's mouth is *kódolás*.**
- **"Bottom-of-funnel" in the CEO's usage means engagement retargeting:** audiences built from people who engaged with the account's biggest past spenders (mostly the old founder videos). That's where the storytelling ads run.
- **Swipe sources so far: Grounding Well** (grounding sheets, US and the Big Five). Their long native ads and whitelisted-page ads are the template for the storytelling format.
- **One image per storytelling copy is the norm so far.** W-001 ran with a single photo. Image variations are the obvious untested lever (GetHookd clone, Higgsfield).
- **Advertorial landing pages haven't been A/B tested against the product page.** Unknown whether they help.

## Consent log (permanent)

Customer comments and reviews cleared for paid media. A record stays here once cleared; add rows, never delete them. The trimming rule for quotes is [[Compliance and Claims Watchlist]] §3c. Anything not in this table is not cleared, however good the line.

| Date | Record | Source corpus | Cleared for | Cleared by | Notes |
|---|---|---|---|---|---|
| 2026-09-28 | **R10** (B.Zs., ≈2025-12-25) | [[Reviews - Facebook Comments (Book)]] | Paid media: quote, comment overlay, primary text; trims per §3c | Brand clearance and customer consent obtained, stated by Mirella 2026-09-28 | Unlocks H1 in [[Review Context - Book Reviews, FB + Website (2026-09-28)]] |
| 2026-09-28 | **R06** (Z.J., ≈2025-11-27) | [[Reviews - Facebook Comments (Book)]] | Same | Same | Unlocks H3 |
| 2026-09-28 | **W07** (D.D., undated) | [[Reviews - Website (Book)]] | Same | Same | Unlocks H2 |
| 2026-09-28 | **R15** (I.S., ≈2026-03-19) | [[Reviews - Facebook Comments (Book)]] | Paid media, **clause-gated**: the first sentence (the "won't work for everyone" line) and the "well-organised book" clause only, trimmed per §3c. The medication sentence and the "5-10%" clause never | Brand clearance and customer consent obtained, stated by Mirella 2026-09-28; the R15 rule widened the same day in [[Compliance and Claims Watchlist]] §3 | Unlocks H4, built in [[Comment-Response Hooks - Book 1]] |

## From the native-ad localizer run (2026-09-28)

- **GetHookd's clone tool composites the workspace's default product into the variations.** The default was "Cogniva Brain Boost" (product 803), so about half of the first batches came back as Cogniva ads. Fix: pass `product_id=5346` ("Tudatalatti Kontroll – native storytelling, NO product in image") on every `create_clone_ad`. With it, all 8 of 8 variations came back clean.
- **Ask for one scene per output.** Without "ONE single full-frame photo per output, never a grid or collage," Nano Banana Pro returned 2×2 collages for a period-photo brief.
- **Not every ad in the competitor sheet is in GetHookd.** Two of four (Meta IDs 982272944438718 and 2389741744878553) had no match by ID or text; the second exists as a sibling ad (100482568) under the same page with identical copy. Fallback for a missing ad: clone a same-page ad with a similar vibe and steer with a custom prompt.
- **The CSV export of the Google Sheet drops cell colours.** When the team marks rows yellow, ask for the row numbers or Meta Library IDs.
- **Landing page:** only `/pages/faradsag` is a verified URL. The ízület, menopauza and other advertorial pages exist per the sheet but their full URLs aren't in the brain yet.

## Translation and localization rules (team feedback relayed by Mirella, 2026-09-28)

Active rules for every Hungarian native ad. The localizer skill reads this section at pre-flight.

**Formatting (Meta primary text):**
- One sentence per line, and a blank line after every line. Short paragraphs, short sentences.
- Exception: very short sentences (roughly four words or fewer, e.g. *„51 éves vagyok. Ezt csinálom. Azt próbáltam."*) may share a line for rhythm, at most a handful in a row.

**Sentence style:**
- Aim for a spoken style, as if someone were telling the story across the kitchen table. Hungarian allows longer sentences than English, so a longer sentence is fine when it sounds more natural, but never so long that the general public trips on it. No overly complicated words.

**Word choice: prefer the originally Hungarian word over the Latin, Greek or English-origin one.** The list the team gave:

| Avoid | Use |
|---|---|
| aktuális | jelenlegi, időszerű |
| affektál | kényeskedik, tettet |
| banalitás | közhely, elcsépeltség |
| definiál | meghatároz |
| dilemma | kétes választás, kényszerhelyzet |
| frusztrált | csalódott, feszült |
| generáció | nemzedék |
| illúzió | ábránd, tévhit |
| kommunikáció | tájékoztatás, kapcsolattartás, beszélgetés |
| konkrét | kézzelfogható, pontos |
| kvalitás | minőség, képesség |
| metódus | módszer |
| negatív / pozitív | rossz, tagadó / jó, állító |
| probléma | gond, nehézség |
| reális | valószerű, észszerű |
| szelektál | válogat, elkülönít |
| tolerál | eltűr, elfogad |
| adminisztráció | ügyintézés, papírmunka |
| fluktuáció | munkaerő-vándorlás, hullámzás |
| információ | adat, felvilágosítás, hír |
| kompetens | hozzáértő, illetékes |
| kontextus | szövegkörnyezet, összefüggés |
| koordinál | összehangol |
| korrekció | javítás, helyesbítés |
| prezentáció | bemutató, előadás |
| prioritás | elsőbbség |
| produktív | termelékeny, hasznos |
| szekció | részleg, osztály |
| abszurd | képtelen, képtelenség |
| analizál | elemez |
| deficit | hiány |
| divergens | széttartó |
| ekvivalens | egyenértékű |
| fikció | kitaláció |
| funkció | szerep, feladat |
| globális | világméretű, átfogó |
| indikátor | mutatószám, jelző |
| konstrukció | építmény, szerkezet |
| kvantitás | mennyiség |
| maximális / minimális | legnagyobb / legkisebb |
| statisztikus | állandó, mozdulatlan (or: kimutatással foglalkozó) |
| szimptóma | tünet |

Same spirit beyond the list: *placebo* → *beképzelés*, *generáció* → *nemzedék*, *stressz* stays (no native word carries it).

**Image variations (GetHookd clones, Higgsfield, any generator):**
- **Never reproduce a split image or any frame that features the competitor's product** (the grounding sheet, a mat, a plug). If the source is "pilot on the left, bed or sheet on the right," generate the pilot alone.
- **Vary the shot, not just the setting.** Same concept, very different visual: one wide shot (two men walking with canes on a street), one closer (a selfie-style shot of one man with his cane), one close-up (a hand holding the cane). Four variations of the same framing in different streets and outfits are not four tests.
- **Full resolution, no pixelation.** Never ship an upscaled crop from a collage output. If the generator returns a grid, regenerate with "one single full-frame photo per output."
- Reason (the CEO's): the goal is to test as many genuinely different creatives as possible; near-duplicates waste the test.


## Pixar AI video ads (first run, 2026-09-30)

- **Seedance 2.5 cannot speak Hungarian.** With a voice reference it gets the founder's timbre right and the words wrong (fluent-sounding gibberish). Generate the Hungarian dialogue first with Seed Audio 1.0 cloning the voice from a 30 s clip, verify with whisper, then have Seedance lip-sync to that track. Never ask Seedance to invent Hungarian speech.
- **Write numbers out in words** in any spoken-line prompt („huszonöt százalékkal", never "25%").
- **Draft mode** (`--draft=true`) renders at 480×854 for a quarter of the price and Mirella judged that resolution good enough for a first test. Queue time was 37 minutes for 15 s.
- **The founder's voice sample on file:** `Creative/Pixar Ads/antal-black-friday-15s-2026-09-30/assets/voices/antal.mp3` (30 s of Antal alone, cut from a 2025 talk clip). Reuse it for any cloned-voice line.
- **Antal's animated likeness** is approved by the team for this format: character sheet at `…/assets/sheets/antal-sheet.png`. Reuse it; don't regenerate him per ad.
