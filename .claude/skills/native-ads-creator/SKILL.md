---
name: native-ads-creator
description: >
  Converts competitor English storytelling ads into culturally localized, compliant Hungarian Meta ads for Tudatalatti Kontroll, swaps the underlying mechanism, generates 4 image variations via GetHookd MCP, and outputs to a new CSV. Trigger: "Run the Native Ad Localizer on [filename.csv]", or any request to localize, translate, or adapt a native/storytelling ad from a CSV into Hungarian.
---

# SKILL: Native Ad Localizer & Iteration Engine

**Description:** Converts competitor English storytelling ads into culturally localized, compliant Hungarian Meta ads for Tudatalatti Kontroll, swaps the underlying mechanism, generates 4 image variations via GetHookd MCP, and outputs to a new CSV.
**Trigger:** "Run the Native Ad Localizer on [filename.csv]"

## PRE-FLIGHT CHECK
1. **Load Brand Context:** Silently read `Brand/The Method - Mechanism and Beliefs.md`, `Brand/Compliance and Claims Watchlist.md`, and `Brand/Brand Profile - Tudatalatti Kontroll.md`.
2. **Load Feedback Memory:** Silently read `Knowledge/Tribal Knowledge.md` to check for any past translation corrections or localization feedback provided by the user. You must apply any active rules found there to this run.

## EXECUTION STEPS

For each row in the provided `.csv` file, execute the following pipeline silently, outputting only the final result:

### Phase 1: Mechanism Swap (English to English)
Read the original English storytelling text. Strip out the competitor's product/method and replace it with the Tudatalatti Kontroll mechanism using the brand context.
* **The "Enemy":** Consistently attribute the root cause of chronic pain, fatigue, and tinnitus to elevated cortisol, trapped stress, and an idegrendszer (nervous system) stuck in survival mode. Never attribute it to personal weakness or "just getting old."
* **Method Consistency:** When describing the physical technique, it must be exact: the fingers must be held 1–2 centimeters away from the skin (without touching) over specific points, in a set sequence, while silently repeating a specific sentence.
* **Compliance:** Ensure no health claims, no condition pairings with the Healing Code, and no second-person attributes ("Are you anxious?").
* **Zero Truncation:** Maintain the complete narrative structure and story arc. Do not cut sections or story beats.

### Phase 2: Hungarian Translation & Localization
Translate the adapted English text into Hungarian, strictly applying these guardrails:
* **Target Tone:** Tailor for Hungarian women aged 50–75. Respectful, grounded, occasionally weary but resilient. Avoid overly Americanized, hyper-enthusiastic sales language.
* **Native Idioms & Cultural Anchors:** Replace literal translations with authentic Hungarian phrases (e.g., "kelengyés láda"). Swap foreign locations for familiar ones (Lake Balaton, Szigliget, Croatia, a rural nyaraló). Use culturally authentic names (Marika, Zsófi, Erzsi mama). Scenarios should match Hungarian reality (SZTK, magánrendelő, postaláda).
* **Conversational Explanations:** Translate complex physiological concepts into relatable, kitchen-table analogies (e.g., comparing nervous system resets to "bikázás" / jump-starting a dead car battery).
* **Syntax & Pro-Drop Mastery:** Eliminate redundant personal pronouns (én, te, ő). Rely on natural verb conjugations and word order. 
* **Authentic Emotional Pacing:** Use natural Hungarian sincerity and stoicism (e.g., "Ott helyben elsírtam magam") instead of melodrama.
* **Formatting (Slip-and-Slide):** Every sentence must be followed by a blank line space for mobile scannability. Exception: Exceptionally short sentences (1–3 words) may share a line with the adjacent sentence for rhythm.
* **No Money-Back Guarantees:** Completely exclude any mention of refunds or "pénzvisszafizetési garancia".
* **Clear CTA:** End with a smooth transition to an emoji-guided directive pointing to the link (e.g., 👇 👉 [link]).

### Phase 3: Image Iteration (GetHookd MCP)
1. Isolate the image URL provided in the spreadsheet row.
2. Call the GetHookd MCP cloning/variant tool using the source image.
3. Generate exactly 4 new iterations. Prompt the MCP to keep the core composition/vibe but alter variables such as the background environment or the demographic appearance of the person in the image.
4. Capture the 4 new image URLs.

### Phase 4: Output & CSV Generation
1. Compile the final localized Hungarian text and the 4 new image URLs.
2. Write this data into a new CSV file named `[Original_Filename]_Localized.csv`. The new CSV should retain the original columns and append new columns for `Translated_Hungarian_Copy`, `Image_Var_1`, `Image_Var_2`, `Image_Var_3`, and `Image_Var_4`.

## THE FEEDBACK LOOP PROTOCOL
If the user provides corrections on the translation, tone, or formatting after the output is generated, you must:
1. Acknowledge the fix.
2. Immediately append the specific correction to `Knowledge/Tribal Knowledge.md` so the mistake is never repeated in future runs.
3. Regenerate the specific ad copy based on the new rule.
