# Ad Brief Template — Pixar-style AI video ad

Copy this whole structure into `Creative/Pixar Ads/<slug>/brief.md`. Fill every field. Empty fields become guesswork in the prompts, and guesswork in the prompts becomes paid regenerations.

---

## 0. Header

| Field | Value |
|---|---|
| Working title | |
| Slug | `<kebab-title>-<YYYY-MM-DD>` |
| Product / offer | Book 1 · Book 2 · Bundle (Book + Guide + Minikurzus) · Event |
| ICP | (from `Personas - Live Event ICPs.md`) |
| Sub-flavour | meme-hook monologue · narrated story + headline card · dialogue mini-movie · newsroom anchor |
| Length | N segments × ≤30 s = ~M:SS |
| Aspect / resolution | 9:16 · 1080p |
| Language | Hungarian, every spoken line and every caption |
| Runs from | Lajos Antal's verified page (default) · whitelisted page |
| Landing page | (verified URL only; `/pages/faradsag` is the one on file) |
| Buyer read-back (Phase 0) | six lines: viewer, objections, sophistication, mechanism, false belief attacked, enemy |

## 1. Cast sheet

One block per character. Names are Hungarian and fictional; never a real customer's or family member's name.

### <Name> — <role in the story>

- **Age and build:** e.g. 61, short, soft round shoulders, a little stooped
- **Face:** shape, eyes, brows, nose, mouth, skin tone, distinguishing mark (reading glasses on a chain, a mole)
- **Hair:** colour, length, style, grey pattern
- **Clothing (fixed for the whole film):** every garment with its colour: e.g. burgundy cardigan over a cream blouse, dark grey slacks, house slippers
- **Signature prop:** what they always hold or wear
- **Personality in two lines:** how they move, what they do with their hands, their default expression
- **Voice profile (goes verbatim into every video prompt):**
  - Pitch: low / mid / high
  - Pace: unhurried / brisk
  - Texture: warm, dry, tired, bright, gravelly
  - Accent / register: e.g. Debrecen, plain, no city polish
  - Example line, in Hungarian, in this voice: „…"
- **Expressions the script needs:** list three (e.g. weary at the sink; startled; the small smile at the end)
- **Model used / hero image file / sheet file / upload ids:** filled in Phase 3

## 2. Locations

One block per location.

### <Location name>

- **What it is:** e.g. a Budapest panel-flat kitchen, 1980s cabinets repainted white
- **Time of day and light:** 5 a.m., one warm bulb over the table, blue dawn in the window
- **Three concrete set-dressing items:** a Zepter pot on the stove, a wall calendar from the pharmacy, a radio on the fridge
- **Camera height and default lens feel:** eye level, slightly wide, soft depth
- **Palette:** three colours
- **Continuity notes:** what must never change between shots
- **Model used / file / upload id:** Phase 3

## 3. Props

| Prop | Must match | Reference image | Notes |
|---|---|---|---|
| The book (Book 1 / Book 2) | The real cover exactly: title, colours, typography | `Research/Website - Snapshot…` or a file from the team | Style changes, cover doesn't |
| … | | | |

## 4. Script, shot by shot

Segment breaks at ≤30 s, on a natural cut, never mid-line. Three or four shots per segment.

### Segment 1 (0:00–0:30)

| Time | Location | In frame | Camera | Action | Dialogue (HU, verbatim) | Caption (HU) | Headline card |
|---|---|---|---|---|---|---|---|
| 0:00–0:07 | | | | | | | |
| 0:07–0:15 | | | | | | | |
| … | | | | | | | |

**Last speaker in this segment:** <name> (matters for extension; see SKILL.md Phase 5)

### Segment 2 (0:30–1:00)

…

## 5. The spine

- **Keep in every variant:** (beats, lines, the reveal wording, the close)
- **May change for a new Entity ID:** (opening shot, location of scene 1, who delivers the hook, framing device)

## 6. Meta copy

**Primary text** (one sentence per line, blank line between; native Hungarian words; no refunds, no fake prices):

…

**Headline:** …
**CTA:** … 👇 👉 [link]
**Landing page:** …

## 7. Compliance table

| Line or scene | Rule it touches | Why it stays safe |
|---|---|---|
| | no cure / no guarantee / no doctor-bashing / no fake price / sourced numbers / personal attributes / condition pairing / [C] framing / consent / "nyugodtabb" | |

## 8. Variant plan (Andromeda)

| Variant | What changes in the first 3 s | Reused assets | New calls needed |
|---|---|---|---|
| v1 | (the base) | | |
| v2 | different opening shot / location | all | 1 segment |
| v3 | different character delivers the hook | all | 1 segment |
| v4 | newsroom framing vs kitchen framing | all + anchor sheet | 1–2 segments |

## 9. Cost and call count

| Step | Calls | Model | Notes |
|---|---|---|---|
| Characters | | gpt_image_2_5 / nano_banana_2 | cheap, iterate |
| Sheets | | nano_banana_2 | cheap |
| Locations | | | cheap |
| Props | | | cheap |
| Video segments | N (+ regenerations) | seedance_2_5 | expensive; see SKILL.md Phase 4 |
| Extensions | N−1 | seedance_2_5 video_extension | expensive |
| Variants | | seedance_2_5 | 1–2 calls each |
