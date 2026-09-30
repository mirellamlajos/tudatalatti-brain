---
name: pixar-ai-video-ads
description: >
  Builds Pixar-style (3D feature-animation look) AI video story ads end to end for Tudatalatti Kontroll: buyer research, three story concepts, a full ad brief with cast, locations, props and a shot-by-shot script, image prompts for every asset, Seedance 2.5 video prompts per 30-second segment, extension and voice-consistency handling, assembly with captions, compliance and voice lint, and an Andromeda-safe variant plan. Runs on the Higgsfield CLI (GPT Image 2.5, Nano Banana 2, Seedance 2.5). Trigger on any request to make an animated, Pixar-style, 3D-cartoon, "AI animation", or character story video ad, to turn a script into an animated ad, to write Seedance/Higgsfield prompts for one, or to fix voice or character drift in one. Also trigger for "pixel-style ad" (people mean Pixar-style).
---

# Pixar-Style AI Video Ads

You're the whole production line for one format: a short animated story ad in the 3D feature-animation look people call "Pixar-style," made with AI image and video models, for a brand whose buyers are 50+ Hungarians. The format was proven in the market in September 2026 (Jackson Yew, Brook Hiddink, Rise Science, Health Insider; see `Research/Swipe Sources - AI Pixar Story Ads, Jackson Yew Network (2026-09-29).md`). It solves a real constraint for this brand: no founder on camera, no daughters, no real customer's face, and still a person-led story.

The method below comes from a working practitioner's pipeline (the "How I Make Pixar AI Animation Ads" tutorial, Seedance 2.5 + Claude + Higgsfield, 2026) plus everything the brain already knows about scripts, hooks, older audiences, visuals and compliance. Where the tutorial says "Seedance 2.5 is very expensive, dial everything in before you press run," believe it. Every step before the video call exists to make the video call succeed the first time.

One naming note: "Pixar-style" is a look descriptor, not a licence. Every character, location and prop is original. Never render a known animated character, a studio's mascot, or a real public figure. If a generator flags a prompt for intellectual property, drop the studio name and describe the look instead ("3D animated feature-film look, soft subsurface skin, big expressive eyes, rounded stylised proportions, cinematic lighting").

## What good looks like in this format

From the four reference ads on GetHookd board 365487 and the tutorial:

- **Vertical 9:16**, polished 3D animation, one or two recurring characters, burned-in captions at the bottom, a pinned headline card at the top (Brook's habit), 60 seconds to 3 minutes for this brand's audience.
- **A story beat every 10 to 15 seconds.** The scene keeps changing, which is why long runs fine.
- **The product shows up late** (Rise names it at 2:10 of 3:12). Story first, then the reveal, then the offer.
- **Four sub-flavours**: meme-hook monologue with captions; narrated third-person story with a headline card; dialogue mini-movie with no narrator; newsroom anchor "reporting" on a person. For this brand, the **dialogue mini-movie** and the **newsroom device** are the two to lead with. Both let a character tell the story without a first-person "I got better" claim, and the anchor frame borrows the news-format trust that older audiences give (`Advertising to Older Audiences.md`).
- **Made to be enjoyed.** The tutorial's rule: "you're not just making AI slop, you're making things that relate to people, make people laugh." The joke, the warmth, the recognisable Hungarian kitchen: that is the difference between an ad people finish and one they scroll.
- **Sound-off safe.** The visual and the captions carry it. Voices are the bonus.

## Pre-flight

Load, in this order, before writing a word:

1. `Brand/Brand Profile - Tudatalatti Kontroll.md`
2. `Brand/The Method - Mechanism and Beliefs.md` (the mechanism, the false beliefs, the named concepts; the story's "why it works" comes from here)
3. `Brand/Personas - Live Event ICPs.md` (the six ICPs and the Book 2 characters Gábor, Feri, Emese, which are ready-made cast)
4. `Brand/Language Bank - Founder and VOC.md` (write dialogue from these words; [R] lines outrank everything)
5. `Brand/Compliance and Claims Watchlist.md` (the hard floor and the override)
6. `Research/Swipe Sources - AI Pixar Story Ads, Jackson Yew Network (2026-09-29).md` (format references, the newsroom device, "hold the copy, vary the skin")
7. `Knowledge/Tribal Knowledge.md` → "Translation and localization rules" and the CEO rules of thumb (buyers 50+, mostly 65+; AI UGC hasn't worked, so this is a new hypothesis, not a proven lane; launch Wednesdays from Antal's verified page; scale at ROAS 2.5).
8. `Knowledge/Domain Knowledge/Spoken-Script Voice.md` Parts 1 to 3 and `AI Writing Tells.md` "How the check runs." Every spoken line passes both before it goes into a prompt.
9. `Knowledge/Domain Knowledge/Advertising to Older Audiences.md` (slow cuts, big text, age-matched characters, clarity over cleverness).
10. Reference files in this skill's `references/` folder as each phase needs them: `brief-template.md`, `prompt-templates.md`, `pipeline-commands.md`, `failure-log.md`.

Add `Brand/Stories and Proof Assets.md` when the story leans on a founder story, `Creative/Winners - Ad Library.md` when adapting a shipped winner (W-001's spine is the obvious first script), and `Strategy/Angle Map - ICPs to Creative.md` when the user hasn't named an angle.

Also load `Knowledge/Domain Knowledge/Visuals.md` (the "make the invisible visible" move is built for animation) and `Making Iterations.md` (the Andromeda rule governs the variant plan). Both carry a sign-off line; see the end of this file.

**Copy Foundations (mandatory, 2026-09-30).** Every story and every spoken line is built on `Knowledge/Domain Knowledge/Copy Foundations.md`, the five foundation docs it names, and `Strategy/Copy Foundations - Brand Application.md`. Load them here. The Phase 0 read-back gains the Foundation Brief (desire, awareness state, sophistication stage, opening move, the one belief); each Phase 1 concept names its opening pattern and the reader questions it answers; the Phase 2 script passes the four-part audit before any credits are spent. For story craft (scenes over summaries, proof with a "but", landing the mechanism prepared) use `.claude/skills/native-ads-creator/references/story-method.md`. The sign-off line "This copy is built on the Copy Foundations." joins the others at the end.

Then run the tools check in `references/pipeline-commands.md` § Bootstrap. If the Higgsfield CLI isn't authenticated, deliver the brief and every prompt anyway and say the generation step is waiting on `higgsfield auth login`.

## The pipeline

Seven phases. Phases 0 to 2 are thinking and writing; nothing costs credits. Phase 3 is images (cheap; iterate freely). Phases 4 to 5 are video (expensive; measure twice). Phase 6 is post and QA. Each phase ends with the user saying "approve" (any spelling) or giving changes. Never skip a gate on the video phases; the tutorial's author lost "so much money in credits" on regenerations that a tighter prompt would have prevented.

### Phase 0 · Buyer research (silent, then a short read-back)

Input: the product or offer the ad sells (Book 1, Book 2, the bundle with the Guide and Minikurzus, a live event) and, if given, the angle or the winner to adapt.

Work out and write down:

- **Who's watching.** Age band (book buyers are 50+ and mostly 65+), gender skew, which ICP, where they are in TEEP (`Emotional Delivery and Timing.md`). A 62-year-old woman reading on her phone after dinner is the default viewer.
- **Objections**, ranked. Scepticism is #1 for this brand, unanswered "how exactly does it work" is #2 (Tribal Knowledge). Pull the rest from the latest `Research/Review Context - *.md`.
- **Market sophistication.** These viewers have read the self-help canon and tried "a thousand methods" ([R10]). Stage 4 to 5: lead with mechanism and blame removal, not promises.
- **The mechanism the story must dramatise.** From `The Method`: stress writes fear-based programs as images; willpower and positive thinking can't reach them; kódolás clears them; energy returns; then change comes without effort. Pick the one false belief the story attacks.
- **The enemy.** The motivation industry, the "step out of your comfort zone" advice, the pills-and-patents money machine. Never the doctor, never the viewer.

Read it back in six lines. This is what the story has to convert.

### Phase 1 · Three story concepts

Offer three, each in eight to ten lines, each a different sub-flavour or a different ICP. For each: working title, sub-flavour, cast in one line, the setting, the beats in order, the joke or the warmth, where the product appears, the one line of dialogue that is the ad's spine, and the estimated length in 30-second segments.

Rules for the concepts:

- **Relatable before clever.** A Hungarian kitchen at 5 a.m., a bookshelf of failed self-help books, a grown daughter noticing her mother is calmer, a pensioner pair on a Balaton bench. Locations and names from the localizer rules (Marika, Zsófi, Erzsi mama; SZTK, a nyaraló, the postaláda).
- **The character is a [C] composite.** Never a real reader, never "one reader wrote," never a real person's name or face. Frame as fiction ("Képzeld el Marikát…"), as a story a narrator tells, or as news an anchor reports. Never a first-person "I'm cured" testimony.
- **The outcome word is nyugodtabb.** Calmer evenings, switched-off brain, "the worries don't bother me like before" ([W03]). No symptom that disappears, no condition, no "gyógyul."
- **Every concept needs a scene that is the mechanism made visible** (`Visuals.md`): the overflowing stress barrel, the door that shuts when you talk to it, water rolling off a duck's back, the fridge vision board that only makes the character sweat, the child who runs to play without needing willpower.
- **Humour is allowed and wanted**, aimed at the industry and at the shared human mess, never at the viewer. The founder's Mercedes-then-Dacia confession is the tone.
- **Book 2's cast is free to use**: a bajnok Gábor, a halogató Feri, a vállalkozó Emese. They already are the ICPs.
- **Don't render the founder or the daughters** unless the user asks; Mercédesz can approve her own. Antal's face and the book cover are the two anchors that work in statics, so the book cover as a prop is in; a cartoon Antal is a request, not a default.

Unchosen concepts go into `Creative/Idea Bank.md` (one row per idea, hunt lane "pixar-story").

The user says "do 2" or names one. If they don't choose, recommend one and say why in one line.

### Phase 2 · The ad brief

Write the full brief with `references/brief-template.md`. It is the single source of truth for every later prompt, so it has to be complete:

1. **Header**: product, ICP, sub-flavour, length in segments, aspect 9:16, language Hungarian, page it runs from.
2. **Cast sheet**: every character with a name, age, body, face, hair, clothing (specific colours and garments, named once and never changed), one prop they carry, a two-line personality, and a **voice profile** (pitch, pace, accent, texture, an example line). The voice profile is not decoration. Seedance generates the voice from the description, and the first segment's voice becomes the base for every later one.
3. **Locations**: each with time of day, light, three concrete set-dressing items, camera height, colour palette. Hungarian reality: a panel-flat kitchen with a Zepter pot, a Kádár-cube house garden, a Balaton pier, an SZTK corridor.
4. **Props**: the book (Book 1 or Book 2 cover, accurate to the real cover; get the reference image from the site snapshot or ask for the file), plus anything the story needs.
5. **The script**, shot by shot: timestamp, location, who's in frame, camera, action, dialogue in Hungarian (one line per speaker turn), caption text, and the on-screen headline card if the flavour uses one. Segment breaks every 30 seconds at most, placed where a cut is natural, never mid-line.
6. **The spine**: beats to keep in every variant; things that may change for a new Entity ID.
7. **Meta copy**: primary text in the localizer's formatting (one sentence per line, blank line between), headline, CTA, landing page.
8. **Compliance table**: each line that touches the wall, and why it stays on the safe side.
9. **Variant plan** (Phase 6 fills the details).

Script rules that apply on top of `Scriptwriting.md`:

- **Dialogue is spoken Hungarian**, written for the mouth: fragments, contractions, repetition, mess left in, the length jumping around (`Spoken-Script Voice.md` Patterns 1 to 8). Native Hungarian words over Latin or English ones (nemzedék, gond, tünet, módszer; the swap table lives in Tribal Knowledge).
- **The hook is the first line and the first frame together.** For older viewers it's a direct, plain callout or a recognisable moment, not a wink. Good: an anchor saying "Egy 61 éves nő letett ezer módszert. Aztán csinált valamit, ami hét percig tart." Bad: anything ironic, fast, or in English.
- **Sit in the problem.** This audience follows a longer setup. Give the ache 30 to 60 seconds before the reveal.
- **The reveal is kódolás**: the hand positions 1 to 2 centimetres from the face and neck, no touching, set order, a sentence repeated silently, about seven minutes, twice a day. The book is where it's taught. Say it plainly once.
- **The close is a friend's nudge**, not a sales close: "Ott van a könyvben. Link lent." No refunds, no money-back language, no scarcity that isn't true, no reference price that wasn't charged.
- **Every number has a source in the brain or it's cut.** The 90% subconscious figure is "the method teaches," never "science says."
- **Lint before approval.** Run every spoken line and caption through `AI Writing Tells.md` (lint, then judge) and the spoken-register test (read it out loud; where do you breathe?). Fix, then present.

The user approves or edits ("change the daughter to a son," "I don't like the kitchen"). Fold edits into the brief, not into side notes, because the prompts are generated from the brief.

### Phase 3 · Assets: characters, sheets, locations, props

Now the image prompts, one per asset, from `references/prompt-templates.md`. Images are cheap. Generate, look, regenerate, and try more than one model per asset. The tutorial's author made his characters in GPT Image 2 and his character sheets in Nano Banana 2 because GPT's output had a grainy texture that Nano Banana removed and "made it feel more animated." Nothing says every asset has to come from the same model.

Order and rules:

1. **Characters first**, one hero image each, 1:1 or 3:4, neutral pose, full body, plain background, the exact clothing from the brief. Default `gpt_image_2_5`; try `nano_banana_2` on the same prompt; keep the one whose face you'd be happy to see for three minutes. Save under `Creative/Pixar Ads/<slug>/assets/characters/`.
2. **Character sheets**, one per character, from the chosen hero image as the reference: a turnaround (front, three-quarter, side, back), three expressions the script needs (the script tells you which: weary, surprised, the small smile), and one close-up of the face. Default `nano_banana_2` with `--image` set to the hero image. This sheet is what the video model gets, so it must match the hero image exactly. If it drifts, say so in the edit prompt: "keep closer to the reference; same face, same hair, same jacket."
3. **Locations**, one establishing frame each, 9:16, no characters in them, matching the palette in the brief. `gpt_image_2_5` or `nano_banana_2`; the tutorial used Nano Banana Pro for locations and GPT Image for characters in the same film.
4. **Props**, on a plain background. The book cover has to be accurate; the tutorial's supplement bottle came back with a white outline the real bottle didn't have and had to be re-prompted ("make it more accurate to the real bottle, frosted look, no white line"). Pass the real cover as `--image` and say "match the reference cover exactly; only the rendering style changes."
5. **Assign the assets as elements.** In the Higgsfield web app, click "assign element" on each image and label it as a character or location, so the video prompt can name them instead of re-uploading. On the CLI the same thing is done by passing them as `--image-references` on every video call and naming them in the prompt ("Image 1 is Marika's character sheet"). Keep a `assets/manifest.md` listing each asset, its file, its upload id, and its label. Signed URLs and upload ids are the handles the video calls need.

The user reviews the asset board. Edits are cheap here; do them here. Nothing goes to video until the cast, sets and props are the ones the user wants to see on screen.

### Phase 4 · Video: one segment at a time

Now the Seedance 2.5 prompts, one per 30-second segment, from `references/prompt-templates.md` § Video segment. Before each call, read the prompt against the brief line by line. "Sometimes it will have weird little things in it." Find them here, not in a $10 regeneration [Stated, tutorial].

What every video prompt contains, in this order:

1. **The language line, first.** "Every spoken line in this video is in Hungarian. No Mandarin, no English." The tutorial's first renders came out in Mandarin for no visible reason; the line fixes it and stays in every prompt for the project.
2. **Style line.** 3D animated feature-film look, consistent with the reference images, cinematic lighting, no photorealism, no live-action.
3. **Reference bindings.** "Image 1: Marika's character sheet. Image 2: the kitchen. Image 3: the book." Then "Marika always looks exactly like Image 1."
4. **Voice lines**, one per speaking character, copied from the brief's voice profile. "Marika: warm, low, a little tired, Debrecen accent, unhurried. Zsófi: brighter, faster, her daughter."
5. **The shots**, timestamped, three or four per 30-second segment, each with camera, action, and the dialogue verbatim in Hungarian.
6. **What not to render**: no on-screen text, no subtitles, no logos, no watermark (captions are added in post so they can be big and legible).
7. **Audio**: dialogue on, light room tone, no music (music goes in post so it can be swapped across variants).

Call shape (details and flags in `references/pipeline-commands.md`): `seedance_2_5`, `--mode omni_reference`, every character sheet, location and prop for the segment as `--image-references`, `--aspect_ratio 9:16`, `--duration` up to 30, `--resolution 1080p`, audio generation on, `--wait`.

Discipline:

- **Segment 1 is the foundation.** Its voices become the base for every later segment, so if a voice is wrong in segment 1, fix it there. Regenerate segment 1 until faces, clothes, setting and voices all match the brief. Only then move on.
- **If the schema offers a draft render**, run it first and only run full quality on a draft you'd ship. `higgsfield model get seedance_2_5` shows the current `draft` fields.
- **One change per regeneration.** If the face drifts, fix the reference or the binding line; if the voice is wrong, fix the voice line; don't rewrite the whole prompt and lose what worked.
- **Keep every render** in `segments/` with its prompt saved next to it as `.txt`. Rejected takes are still reference material for the voice step.

### Phase 5 · Extend, and keep the voices straight

Seedance 2.5 makes at most 30 seconds per call. Longer stories are chained with the extension mode, which continues from an existing clip and keeps the characters and the scene continuous, which "makes the video flow so much better than regenerating a completely new video."

How:

1. Cut the **last 10 seconds** of the approved previous segment (ffmpeg command in `pipeline-commands.md`).
2. Call `seedance_2_5` with `--mode video_extension`, `--extension_mode forward` (sequel; `backward` is the prequel), that tail as the video reference, the same character sheets and location as image references, and the next segment's prompt. The prompt describes what happens next, not what's already in the tail.
3. Review as in Phase 4, then repeat for the next segment.

**The voice bleed trap.** Extension copies the voices in the tail. If the last speaker in the tail was a different character, the new segment's speaker may come out with that voice: the tutorial's deep-voiced hero got the other alien's "nasally high-pitched" voice this way. Two fixes, use both:

- **Cut the tail so the character who speaks next is the last one heard**, or so nobody speaks in the final second or two.
- **Voice references.** Once a character has spoken cleanly in any approved render, extract up to 30 seconds of only that character speaking, as an audio file (or, in the web app, an MP4 with a blank black screen and only that audio, so the model takes nothing from the picture). Pass it as an `--audio-references` item and bind it in the prompt: "Audio 1 is Marika's voice reference only. Marika speaks with exactly this voice." Build one voice file per speaking character after segment 1 and reuse it on every later segment and every variant. This is the single biggest quality lever after the character sheets.

Keep the voice files in `assets/voices/` and list them in the manifest.

### Phase 6 · Assemble, caption, check, ship

1. **Assemble**: concatenate the segments in order, normalise loudness, add a light music bed if the brief calls for one, export 1080×1920 H.264 with AAC audio. Commands in `pipeline-commands.md`. For subtitle burn-in and trims the `video-use` skill can do the work; keep the captions big, high-contrast, two lines max, one idea per caption, timed to the spoken line.
2. **Headline card** pinned at the top for narrated and newsroom flavours (Brook: "$0 → $2M online. one product"; ours: "61 évesen. Ezer módszer után. Hét perc naponta."). Claims-safe, no number without a source.
3. **The "AI-generated" note.** Lasta, Zeely and Temu carry "Contains AI-generated imagery" on screen; Jackson doesn't. Default to a small caption at the start or the end. It costs nothing with this audience (`Advertising to Older Audiences.md`: they don't penalise obviously AI b-roll) and it removes a labelling risk.
4. **Watch it as the viewer.** Sound off first, then on. Does the first frame plus the first caption tell a 62-year-old what this is and who it's for? Do the cuts hold long enough? Is any character's face, outfit or voice different from segment to segment? Fix before shipping.
5. **Score it** with the Virality Predictor (`brain_activity`) if credits allow; report hook second and sustain as a sanity check, not a verdict.
6. **Compliance pass** against the hard floor (no cure, no guarantee, no doctor-bashing, no fake prices, sourced numbers), the personal-attributes rule (no second-person "szorongsz?"), no condition paired with Gyógyító Kód, [C] never framed as real, consent for any real story, "nyugodtabb" as the outcome. Table it in the brief.
7. **Variant plan, Andromeda-safe.** Brook's engine: **hold the copy, vary the skin.** Three or four cuts of the same script where the **first 3 seconds change visibly**: a different opening shot, a different location for scene 1, a different character delivering the hook, or the newsroom framing versus the kitchen framing. Never a messaging-only variant on the same opening. Each is a new Entity ID; each is a real test. Cheap to make because assets and voices are reused.
8. **Deliver**: final MP4s, the brief with the Meta copy, the asset manifest, and a launch note (from Antal's verified page, Wednesday launch, read on a 4-day average, scale at 2.5).

## Project folder

```
Creative/Pixar Ads/<slug>/
  brief.md                # the approved Phase 2 brief, kept current
  assets/
    characters/  sheets/  locations/  props/  voices/
    manifest.md           # file, upload id, label, model used, notes
  prompts/                # one .txt per generation, same name as the render
  segments/               # every render, kept, with take numbers
  final/                  # assembled variants, named <slug>-v1-<opener>.mp4
```

The slug is the working title in kebab-case plus the date.

## Standing rules

- **Andromeda wins.** Every iteration changes the first 3 seconds visibly. No messaging-only iterations on an existing winner.
- **Source everything.** Claims get Stated / Verified / Inferred / Data-limited. Quotes get [F] [R] [K] [C]. An animated character's lines are [C] by definition and are never shipped as a customer's words.
- **Older-audience defaults hold** unless the account says otherwise: slow cuts, big captions, one thing on screen, age-matched characters, an explicit "this is for you" callout, an authority or news frame where the flavour allows it.
- **Cheap before expensive.** Images and prompts are where the iteration happens. A video call is a decision.
- **The tutorial's reference ad is not a template for claims.** Its product (a mineral supplement) says "energy all day, sleep like a rock, hard to kill." Those are the swipe's claims, not ours. We swipe the structure (cold open joke, the "where did they all go" mystery, the lone hold-out who explains the simple habit, the deadpan close), never the promises.
- **Report cost honestly.** Say how many video calls a plan needs before running them. The tutorial's author quotes roughly $10 per generation [Stated]; check the live price with `higgsfield generate cost` when available.

## Feedback loop

When the user corrects anything (a translation, a character look, a model choice, a prompt line that fixed a drift), do three things: acknowledge it, append the rule to `Knowledge/Tribal Knowledge.md` under a "Pixar AI video ads" heading (create it on first use), and add the failure and fix to this skill's `references/failure-log.md`. Then regenerate only the affected piece.

## Sign-off lines

This skill leans on two docs that carry a required closing line. When a delivery used the visual direction from `Visuals.md` (it always does in Phase 2) and the variant rule from `Making Iterations.md` (Phase 6), end the delivery message with both, verbatim:

"this is based on everything I have learned about visuals in advertising"

"This is based on everything I have learned about making iterations 2.0"
