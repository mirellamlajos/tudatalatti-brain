# Prompt Templates — Pixar-style AI video ads

Every prompt is generated from the approved brief. Fill the brackets from the brief; don't improvise details the brief doesn't have, because a detail invented in one prompt is a continuity break in the next.

Style words to use everywhere: **"3D animated feature-film look, stylised rounded proportions, big expressive eyes, soft subsurface skin, clean smooth surfaces, cinematic three-point lighting, shallow depth of field, warm colour grade."** These say "Pixar-style" without naming a studio, which keeps the generator's IP filter quiet and keeps the characters original. Never name a known animated character or a real person.

Keep image prompts under about 150 words and video prompts under about 300. Long prompts distort. Put the must-haves first.

---

## 1. Character hero image

Model: `gpt_image_2_5` first; also try `nano_banana_2` on the same prompt. Aspect 3:4 or 1:1.

```
One original animated character, full body, standing, neutral relaxed pose, facing camera, plain light-grey studio background, even soft lighting.
3D animated feature-film look, stylised rounded proportions, big expressive eyes, soft subsurface skin, clean smooth surfaces.
[Name]: [age] years old, [build], [face: shape, eyes, brows, nose, mouth, skin tone, mark]. Hair: [colour, length, style, grey pattern].
Clothing: [every garment with colour, exactly as the brief]. Holding: [signature prop].
Expression: [default expression from the brief].
Single character only, no text, no logo, no watermark.
```

Edit prompt when the result drifts (pass the best take as `--image`):

```
Same character, same face, same hair, same clothing as the reference. Change only: [one thing]. Keep the 3D animated feature-film look. No text.
```

The tutorial's fixes, word for word in spirit: "keep it closer to the reference," "make this more [animation style]," "the real one doesn't have a white line, match it."

## 2. Character sheet

Model: `nano_banana_2` with `--image <hero image>`. Aspect 16:9.

```
Character reference sheet of the character in the reference image, identical face, hair and clothing in every panel.
Panels on one white sheet: front view full body, three-quarter view, side profile, back view; then three head-and-shoulders expressions: [expression 1], [expression 2], [expression 3]; then one close-up of the face, neutral.
3D animated feature-film look, consistent lighting, plain white background, panels evenly spaced, no labels, no text, no watermark.
```

Check the sheet against the hero image before saving it: same eye shape, same hairline, same garment colours. If one panel drifts, regenerate the sheet; don't ship a sheet with a stranger in panel four.

## 3. Location

Model: `gpt_image_2_5` or `nano_banana_2`. Aspect 9:16 (the film's aspect), so the framing is the one the video will use.

```
Empty location, no people, no text.
[What it is, from the brief]. [Time of day and light]. Set dressing: [three concrete items]. Camera at [height], [lens feel].
Palette: [three colours].
3D animated feature-film look, stylised but grounded, soft global illumination, clean surfaces, cinematic depth. Hungarian everyday realism in the details.
```

## 4. Prop (the book)

Model: `gpt_image_2_5` with `--image <real cover file>`.

```
The book from the reference image, cover matched exactly: same title text, same colours, same layout. Render it as a prop in a 3D animated feature-film look: slightly softened edges, subtle paper texture, standing upright on a plain neutral background, soft studio light. No extra text, no changes to the cover art, no white outline, no glow.
```

## 5. Video segment (Seedance 2.5, `omni_reference`)

One prompt per ≤30 s segment. Bind every reference by its position in the `--image-references` list (Image 1, Image 2…), in the same order you pass them on the command line.

```
LANGUAGE: every spoken line in this video is in Hungarian. No Mandarin, no English, no other language.

STYLE: 3D animated feature-film look, exactly matching the reference images. Stylised rounded characters, cinematic lighting, shallow depth of field, warm grade. Not photorealistic, not live action. Vertical 9:16.

REFERENCES:
Image 1: [Name A] character sheet. [Name A] looks exactly like Image 1 in every shot: same face, same hair, same [garment colours].
Image 2: [Name B] character sheet. Same rule.
Image 3: [Location] establishing frame. The scene is this room, this light.
Image 4: the book prop. The cover stays exactly as in Image 4.

VOICES:
[Name A]: [pitch], [pace], [texture], [accent/register]. 
[Name B]: [pitch], [pace], [texture], [accent/register].
Each character keeps one consistent voice for the whole clip.

SHOTS:
0:00–0:07 — [camera]. [Action]. [Name A]: „[line]"
0:07–0:15 — [camera]. [Action]. [Name B]: „[line]"
0:15–0:23 — [camera]. [Action]. [Name A]: „[line]"
0:23–0:30 — [camera]. [Action, ending on a natural pause]. [Last speaker or silence, per the brief]

DO NOT RENDER: on-screen text, subtitles, captions, logos, watermarks, extra characters, wardrobe changes.

AUDIO: dialogue as written, natural room tone, no music.
```

Notes:
- Three or four shots per segment. More than that and the model rushes or merges them.
- Camera words that work: slow push in, static wide, over-the-shoulder, close-up on hands, gentle pan. Older audience: hold shots, few cuts.
- Dialogue verbatim from the brief, in quotation marks, already linted for the spoken register.
- If the previous take had one specific fault, add one line at the top naming the fix ("[Name A] never removes her cardigan"), don't rewrite the rest.

## 6. Video extension (Seedance 2.5, `video_extension`, `extension_mode forward`)

Video 1 is the last 10 seconds of the approved previous segment. Same image references as before. The prompt describes only what happens next.

```
LANGUAGE: every spoken line is in Hungarian. No Mandarin, no English.

Continue the scene from Video 1 without a cut. Same characters, same room, same light, same clothes.

REFERENCES: Image 1: [Name A] sheet. Image 2: [Name B] sheet. Image 3: [Location]. [Audio 1: [Name A]'s voice reference only, if attached.]

VOICES: [Name A] speaks with [voice profile] [and exactly the voice in Audio 1]. [Name B]: [voice profile]. Do not swap voices between characters.

NEXT SHOTS:
0:00–0:08 — [camera]. [Action]. [Name]: „[line]"
0:08–0:18 — …
0:18–0:28 — …
0:28–0:30 — [settle on a natural pause; last speaker: [name] / silence]

DO NOT RENDER: on-screen text, subtitles, logos. AUDIO: dialogue, room tone, no music.
```

`extension_mode backward` is the prequel: the same shape, but "what happens just before Video 1."

## 7. Voice-reference binding (any mode)

Add to the REFERENCES block, one line per attached voice file, in the order passed as `--audio-references`:

```
Audio 1: voice reference for [Name A] only. [Name A] speaks with exactly this voice, this pitch and this pace. Audio 1 is not a soundtrack and contains no other character.
Audio 2: voice reference for [Name B] only. …
```

Make the voice file from an approved render: up to 30 seconds of only that character speaking, exported as audio (mp3/wav). In the web app, use an MP4 with a blank black picture and only that audio, so the model takes nothing from the frame.

## 8. Caption and headline-card copy (post, not a generation prompt)

- Captions: the spoken line, trimmed to two lines max, one idea per caption, timed to the line. Big sans-serif, white with a dark outline or a dark box, bottom third, safe from the Meta UI overlays.
- Headline card (narrated and newsroom flavours): one pinned line at the top for the whole film, claims-safe, sourced if it has a number: e.g. „61 évesen. Ezer módszer után. Hét perc naponta."
- AI note: a small „AI-val készült animáció" at the start or the end.
