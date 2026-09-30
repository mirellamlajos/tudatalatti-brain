---
name: native-ads-creator
description: >
  Converts competitor English storytelling ads into culturally localized, compliant Hungarian Meta ads for Tudatalatti Kontroll: maps the source story, swaps the underlying mechanism, rebuilds the story on the brain's Copy Foundations (one belief, the twelve story beats, scenes, proof with a "but", a prepared mechanism), runs a hard story audit, generates 4 image variations via GetHookd MCP, and outputs to a new CSV with a story-audit file. Trigger: "Run the Native Ad Localizer on [filename.csv]", or any request to localize, translate, adapt, rewrite or improve a native/storytelling ad from a CSV into Hungarian.
---

# SKILL: Native Ad Localizer & Iteration Engine

**Description:** Converts competitor English storytelling ads into culturally localized, compliant Hungarian Meta ads for Tudatalatti Kontroll, swaps the underlying mechanism, rebuilds the story so it holds up on its own, generates 4 image variations via GetHookd MCP, and outputs to a new CSV.
**Trigger:** "Run the Native Ad Localizer on [filename.csv]"

## THE RULE THIS SKILL RUNS ON

> **A native ad is a story first and a translation second.** Swapping the product inside someone else's story and translating it is not enough. The source's mechanism explanation and its proof were built for the source's product; once the product changes, both have to be rebuilt. Every ad this skill ships is built on the brain's Copy Foundations and passes the Story Audit in Phase 3. **Copy that isn't built on the Foundations isn't good, and copy that fails the audit doesn't ship.** (Mirella, 2026-09-30.)

## PRE-FLIGHT CHECK

Once per run (not once per row), silently. None of it is optional.

1. **Load Brand Context:** Silently read the brand context in the `CLAUDE.md` order: `Brand/Brand Profile - Tudatalatti Kontroll.md`, `Brand/The Method - Mechanism and Beliefs.md`, `Brand/Personas - Live Event ICPs.md`, `Brand/Language Bank - Founder and VOC.md`, and `Brand/Compliance and Claims Watchlist.md`.
2. **Load Feedback Memory:** Silently read `Knowledge/Tribal Knowledge.md` to check for any past translation corrections or localization feedback provided by the user. You must apply any active rules found there to this run.
3. **Load the Copy Foundations.** Read `Knowledge/Domain Knowledge/Copy Foundations.md` and all five foundation docs it names:
   - `Market Awareness and Sophistication.md` (the opening)
   - `One Belief and the Ten Questions.md` (the spine)
   - `Belief Building in Long Copy.md` (the body)
   - `Persuasion Principles and Copy Checklist.md` (the craft check)
   - `Testing Doctrine and Specificity.md` (the specificity pass)
4. **Load the brand's answers:** `Strategy/Copy Foundations - Brand Application.md`. It holds the pre-filled Foundation Brief for a cold native ad, the one-belief sentence per offer, and the brand material for each opening pattern.
5. **Load the story method:** `references/story-method.md` in this skill folder. It holds the four acts and twelve beats, the opening patterns, scene craft, proof craft and how to land the mechanism.
6. **Load the benchmark:** the W-001 entry in `Creative/Winners - Ad Library.md` (full copy and anatomy). Every new ad should be at least that good a story.
7. **Load the lint:** `Knowledge/Domain Knowledge/AI Writing Tells.md` (the sign families; Phase 3 applies them by hand to the Hungarian).

## EXECUTION STEPS

For each row in the provided `.csv` file, execute the following pipeline silently. The only things delivered are the output CSV, the story-audit file, and a short run message (Phase 5).

### Phase 0: Story Diagnosis (before a word is changed)

1. **Fill the Foundation Brief for this row.** Start from the pre-filled brief in `Strategy/Copy Foundations - Brand Application.md` and change what this source ad changes: the desire that leads, the narrator, the offer. All ten lines. It goes in the audit file.
2. **Write the one belief.** One sentence: a new opportunity is the key to what this reader wants, reachable only through the brand's mechanism. If the first slot can't be filled with something this reader hasn't heard a hundred times, find a better angle before going on.
3. **Map the source ad** (`references/story-method.md` §10): list its beats in order, tag each with its twelve-beat number and the reader question it answers, and name why the ad worked (its opening pattern, its turn, what its proof rests on, the line people would repeat).
4. **Mark what the swap will break** (always the mechanism explanation and the proof) **and which of the twelve beats are missing.** Those get rebuilt or added in Phase 1.
5. **Decide the narrator.** Keep the source's narrator (sex, job, situation) when that narrator is why the ad worked: an unlikely messenger, an authority with no reason to sell. Move the age toward the reader where it stays believable. Recast only when the narrator has no pull for a 50–75-year-old Hungarian reader. Either way, **the reader has to see her own world within the first third**: a spouse, a kitchen, a garden, a doctor's waiting room. Look at the row's source image before settling the narrator's age and sex, because Phase 4 clones that image: the person in the copy and the person in the picture have to match. If the image can't be opened, set the narrator from the source text and flag it in the audit.

### Phase 1: Mechanism Swap and Story Rebuild (English to English)

Read the original English storytelling text. Strip out the competitor's product/method and replace it with the Tudatalatti Kontroll mechanism using the brand context. Then rebuild the story until it carries all twelve beats.

**Swap rules:**
* **The "Enemy":** Consistently attribute the root cause of chronic pain, fatigue, and tinnitus to elevated cortisol, trapped stress, and an idegrendszer (nervous system) stuck in survival mode. Never attribute it to personal weakness or "just getting old." (Cortisol and the nervous-system account are cleared for this long-form native format by the CEO's 2026-09-26 ruling in the Compliance doc. Attribute them to the book or the method, and list them under the audit's flags.)
* **Method Consistency:** When describing the physical technique, it must be exact: the fingers must be held 1–2 centimeters away from the skin (without touching) over specific points, in a set sequence, while silently repeating a specific sentence.
* **Compliance:** Ensure no health claims, no condition pairings with the Healing Code, and no second-person attributes ("Are you anxious?").
* **Zero Truncation:** Maintain the complete narrative structure and story arc. Do not cut sections or story beats. "Kept" means the beat's job is kept, not its length:
  * Two source beats doing the same job (a recap that repeats the timeline, a second spec block) may be merged into one.
  * Blocks may be reordered to hold momentum, as long as the two fixed points below hold.
  * A beat that breaks the wall is replaced with its compliant version, never simply deleted:

  | Source beat | Compliant version |
  |---|---|
  | A money-back guarantee | The honest part: what it isn't, how long it takes, that it isn't the same for everyone |
  | A false deadline, "selling out," limited stock | The authenticity warning (incomplete versions online), or nothing |
  | A discount or price line | Only a discount verified as live today and a price actually charged; otherwise where the official material is |
  | A cure or "gone for good" line | A change in daily experience, noticed sideways, told as the narrator's own |
  | A second-person symptom timeline ("by week two you'll…") | The narrator's own first-person timeline |
  | Product specs and compatibility | How little the practice asks: no equipment, no appointment, done alone, a missed session is fine |
  | A third party's medical recovery | Someone who says only that they're *nyugodtabb* |
  | The competitor's coined terms and study claims | The brand's own named concepts, attributed to the book |

**Story rules (mandatory; detail in `references/story-method.md`):**
* **Four acts, twelve beats.** Act 1, the opening (beats 1–3): identification opening · what's at stake · early proof. Act 2, the struggle (4–7): the narrator arrives · everything tried · the real problem · what's to blame. Act 3, the turn (8–9): how it was found · how it works. Act 4, the proof and the close (10–12): proof over time · the honest part · the close. The rebuilt story carries all twelve. Keep the source's order where it's better, with two fixed points: the identification opening comes first, and the practice is never *explained* before the real problem and what's to blame have landed.
* **A glimpse is allowed; an explanation isn't.** Someone can be *seen* doing something odd early on, unexplained. That's curiosity, and it's often the source's best asset. What the practice is, and why it works, waits for Act 3.
* **Length follows the source.** Count the finished Hungarian against the English source, and never run longer than it. For a long source (1,000+ words) aim for 1,000 to 1,300 Hungarian words: that's where W-001 sits (about 1,100), and the first test of this skill read better at 1,108 than at 1,667. For a short source (under about 600 words) stay near its length: a beat can be a single line, and beats 3, 5 and 11 can each ride inside a neighbouring beat. A rebuilt story is never padded to look thorough.
* **The opening identifies; it doesn't sell.** No product, no price, no promise in the opening. Name which of the eight patterns it uses. A curiosity loop ("something I can't stop thinking about") is a device that rides on top of a pattern, not a pattern itself: keep the source's loop, and name the pattern underneath it.
* **Scenes, not summaries.** Every act gets at least one scene: a place or time of day, an object, a small action, and a line of speech where someone else is present. Don't name a feeling after showing it.
* **Proof has a "but."** Night one: nothing, and the narrator says so. Then small changes stretched over weeks, each noticed sideways, and a doubting witness who remarks on it unprompted. One small proof beat goes in the first third.
* **The real problem is the flip.** Whatever makes this way different, everything tried before was missing exactly that. Lift the blame off the narrator in the narrator's own words.
* **Blame a thing.** The way we live now, stress that never gets cleared, the advice to push harder. Never a doctor, never medicine, never the reader. When a doctor appears, the doctor is right.
* **Land the mechanism prepared.** Problem mechanism first in kitchen-table words, then the flip, then the practice (exact), next to a familiar picture, simplified with the counted facts on file (about seven minutes, morning and evening, alone at home), in the same plain voice as everything before it.
* **Show the promise in four or more settings:** in action, the first evening, stretched over time, through someone else's eyes, old mornings against new ones, how little it asks, a homely comparison.
* **The honest part.** One or two lines on what it isn't, how long it took, that it isn't the same for everyone. It sits close after the long proof, not four blocks later.
* **No ad voice.** Understatement. No "amazing," "secret," "breakthrough." Emotional words stay out of sight.
* **Specificity pass.** Swap every vague line for a real detail. Two kinds of number:
  * **Claims and statistics** (study results, percentages, device readings, sales counts, "X% of people," prices, discounts): traced to a source in the brain, or cut. A scene replaces a number that can't be sourced. Never invent one.
  * **Story-world details** (the narrator's age, years in the job, the hour of the night, how many nights away): the narrator's own. Keep them plausible and consistent.
* **The close hands the choice back** and ends on one line worth keeping.

### Phase 2: Hungarian Translation & Localization
Write the story in Hungarian from the Phase 1 English rebuild. This is a retelling in Hungarian, not a line-by-line translation: the beats and facts are fixed, the sentences are new. Strictly apply these guardrails:
* **Target Tone:** Tailor for Hungarian women aged 50–75. Respectful, grounded, occasionally weary but resilient. Avoid overly Americanized, hyper-enthusiastic sales language. (This is the *reader*. The narrator may be someone else; see Phase 0 step 5.)
* **Native Idioms & Cultural Anchors:** Replace literal translations with authentic Hungarian phrases (e.g., "kelengyés láda"). Swap foreign locations for familiar ones (Lake Balaton, Szigliget, Croatia, a rural nyaraló). Use culturally authentic names (Marika, Zsófi, Erzsi mama). Scenarios should match Hungarian reality (SZTK, magánrendelő, postaláda). Where the story needs foreign places (a pilot, a lorry driver, someone working abroad), keep them and put the narrator's home, family and everyday objects in Hungary.
* **Conversational Explanations:** Translate complex physiological concepts into relatable, kitchen-table analogies (e.g., comparing nervous system resets to "bikázás" / jump-starting a dead car battery).
* **Syntax & Pro-Drop Mastery:** Eliminate redundant personal pronouns (én, te, ő). Rely on natural verb conjugations and word order. 
* **Authentic Emotional Pacing:** Use natural Hungarian sincerity and stoicism (e.g., "Ott helyben elsírtam magam") instead of melodrama.
* **Formatting (Slip-and-Slide):** One sentence per line, and a blank line after every line. Short sentences, short paragraphs. Exception: very short sentences (about four words or fewer) may share a line for rhythm. A line of quoted speech stays on one line even when it holds two short sentences.
* **Spoken style and word choice:** Write as if telling the story across a kitchen table. A longer sentence is fine where Hungarian sounds more natural that way, but never one the general public trips on. Prefer originally Hungarian words over Latin, Greek or English-origin ones (nemzedék not generáció, gond not probléma, tünet not szimptóma). The full swap list lives in `Knowledge/Tribal Knowledge.md` → Translation and localization rules.
* **No Money-Back Guarantees:** Completely exclude any mention of refunds or "pénzvisszafizetési garancia".
* **Clear CTA:** End with a smooth transition to an emoji-guided directive pointing to the link (e.g., 👇 👉 [link]). Use the row's landing URL if the sheet gives one; otherwise `https://atudatalattikontroll.com/pages/faradsag` (the one verified URL), flagged in the audit.
* **The story survives the retelling.** Every scene, every "but," the witness's line and the line worth keeping must land in Hungarian as well as they did in English. The scenes use Hungarian objects and rooms. The last line should sound like something a Hungarian reader would repeat.
* **Words from the Language Bank.** Where the narrator's feelings match what real readers wrote, use their vocabulary (*nyugodtabb*, *ezer féle módszer*, *valami visszatart*) and the founder's own labels (*stresszhordó*, *kódolás*). Reader quotes themselves ship only under the consent log.

### Phase 3: Story Audit (hard gate)

Run this on the finished Hungarian copy. Use `references/story-audit-template.md`.

1. **Hard checks H1–H16. All must pass.** They cover: the opening, the second-person rule, the one belief, the questions answered, the early proof, the prepared and exact mechanism, the "but" and the witness, a scene per act, the specificity pass and sourced numbers, the hard floor (no cure, no guarantee, no doctor-bashing, no fake price, no refund talk, no invented deadline), the honest part, the close, zero truncation, the localization rules, and the AI-tells lint.
2. **The AI-tells lint is done by hand on the Hungarian.** Read the draft against the sign families in `AI Writing Tells.md` and their Hungarian forms: *„nem csak X, hanem Y"* and "not X, not Y, but Z" frames, matched triads, manufactured-intimacy openers (*„Megmondom őszintén…"*, *„Az igazság az, hogy…"*), dash cadence, brochure adjectives, a tidy moral at the end of every paragraph. (The doc's lint script isn't in this repo; don't wait on it.)
3. **Craft score.** Seven lines, 0–2 each. Under 10 of 14 is a rewrite. A momentum score of 1 or lower means merge or reorder the blocks between the witness and the close, then re-score.
4. **On any fail: rewrite the failing part, then run the whole audit again.** A row does not go to Phase 4 until it passes. After three failed passes on the same check, stop on that row and report which check fails and why, instead of shipping a weak ad.
5. **Write two alternative openings** in Hungarian, each from a different opening pattern than the one used, with a note on where each joins the body and which body lines to cut so nothing gets told twice. At least one should reach the reader's own world faster than the main opening does. New opening, same body: that's a new test for the team and a new first line for Meta.
6. **Compare with W-001.** Say in the audit's flags where this story is stronger and where it's weaker than the benchmark.

### Phase 4: Image Iteration (GetHookd MCP)
1. Isolate the image URL provided in the spreadsheet row.
2. Call the GetHookd MCP cloning/variant tool using the source image.
3. Generate exactly 4 new iterations. Same concept, very different visuals: vary the shot distance and framing (one wide shot, one closer or selfie-style, one close-up detail, one alternative angle), not just the setting, outfit or face. Four versions of the same framing in different streets are not four tests.
   * **Never reproduce a split image or any frame that shows the competitor's product** (sheet, mat, plug, packaging). If the source is "person on the left, product or bed on the right," generate the person alone.
   * Always pass `product_id=5346` (the brand's product-free native record) and open the prompt with "ONE single full-frame photo per output, never a grid or collage," plus an explicit no-product, no-text line. Never ship an upscaled crop from a collage; regenerate instead.
   * Deliver full resolution (1080×1080 or larger), nothing pixelated.
   * **The image is the first beat of the story.** It has to fit the opening pattern and the narrator as rewritten: state the narrator's age and sex in the clone prompt so the person in the picture matches the copy: a person and a place this reader sees as her own or one step up, nothing that looks like an ad.
4. Capture the 4 new image URLs.

### Phase 5: Output & CSV Generation
1. Compile the final localized Hungarian text and the 4 new image URLs.
2. Write this data into a new CSV file named `[Original_Filename]_Localized.csv`. The new CSV should retain the original columns and append new columns for `Translated_Hungarian_Copy`, `Image_Var_1`, `Image_Var_2`, `Image_Var_3`, and `Image_Var_4`. Leave the sheet's existing columns exactly as they came in.
3. Write `[Original_Filename]_Story_Audit.md` next to it: one block per row from the audit template, with the Foundation Brief, the source map, the hard checks, the craft score, the two alternative openings and the flags for the team. The Foundation Brief lives here, not in the chat.
4. The run message is short: the two file paths, then one line per row (opening pattern, passes needed, craft score, anything the team must decide), and it ends with: "This copy is built on the Copy Foundations."

## THE FEEDBACK LOOP PROTOCOL
If the user provides corrections on the translation, tone, or formatting after the output is generated, you must:
1. Acknowledge the fix.
2. Immediately append the specific correction to `Knowledge/Tribal Knowledge.md` so the mistake is never repeated in future runs.
3. Regenerate the specific ad copy based on the new rule.

Corrections about the **story** (a flat scene, a proof nobody would believe, a mechanism that lands badly, a weak opening) are logged the same way, under a "Native ad storytelling rules" heading in `Knowledge/Tribal Knowledge.md`, and the regenerated ad goes through Phase 3 again.
