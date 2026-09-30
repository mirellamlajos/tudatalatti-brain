---
name: static-ad-localizer
description: >
  Takes a folder of the brand's winning static ad creatives (usually Hungarian; any language works), translates the on-image text into a target language from the Hungarian original (English first, then Spanish or whatever is asked), regenerates each creative in Higgsfield so it matches the original exactly, swaps in the current offer, and pastes the brand's real translated product images on top instead of letting the model redraw the books. Works in batches of 10 with an approval on the first creative of every batch, and learns from feedback through a rules file. Trigger on any request to translate, localize, regenerate, recreate or "make English/Spanish versions of" winner creatives, static ads or a creatives folder, to swap the offer or the book images on existing statics, or to run the next batch of a localization job.
---

# Static Ad Localizer

You turn a folder of proven static ads into the same ads in another language, with the current offer and the real product images. The job is a copy, not a redesign: same photo, same layout, same type, same colours, same meaning. These ads are vetted winners, so the copy stays as it ran. Two things change on purpose: the language of the text and the product cluster.

Why it's built in layers: image models redraw everything they touch. A book cover passed in as a reference comes back slightly wrong, and a label the model places lands wherever it likes. So the model does only what it's good at (re-setting the headline and body copy and cleaning the background), and everything that has to be exact or exactly placed (the books, the Guide, the plus sign, the offer label) is pasted on afterwards by a script.

## Inputs

Ask for whatever is missing; don't guess.

1. **The creatives folder or zip.** Still images. Any source language. These decide which ads get made and what they look like.
2. **The Hungarian originals.** Hungarian is the copy of record. If the creatives are already Hungarian, that's them. If they're in another language (the first batch was Romanian), match each one to its Hungarian twin in `Creative/Static Localization/Hungarian Static Copy Bank.md` and translate from the Hungarian. Never translate a translation when the Hungarian exists.
3. **The target language and market.** English for the UK unless told otherwise.
4. **The offer.** What the product cluster has to show now, and anything that must not be said. Current offer (2026-09-30): Book 1 + Book 2, and the Practical Guide comes free with the purchase. Never "three books for the price of two"; the Guide is a smaller book and it's a free gift.
5. **The product images in the target language.** Transparent cutouts, kept in `Brand/Product Images/<LANG>/` (EN is there). If the folder for the target language is empty, stop and ask. Never generate a book.

## Pre-flight

1. Read `references/rules.md`. Every rule in it applies to this run. It's the memory of everything Mirella has corrected.
2. Read `references/glossary-<lang>.md` for the brand's fixed terms in the target language. If it doesn't exist, build it from the brand's site in that language (EN: subconsciouscontrol.com) and the product covers before translating anything.
3. Read `Creative/Static Localization/Hungarian Static Copy Bank.md`.
4. Read `Brand/Compliance and Claims Watchlist.md` and the W-002 entry in `Creative/Winners - Ad Library.md`.
5. `higgsfield account status`. Note the credits. If it isn't logged in, do the specs and translations anyway and say the generation step is waiting on `higgsfield auth login`.

## Batch rules

- **10 creatives per batch** until Mirella says "do them all."
- **Creative #1 of every batch gets approved before the other nine are generated.** This holds for every new batch, even when the skill is running well.
- Number the creatives by their source filename and keep that number through every file.

## The pipeline

### 1 · Set up the batch folder

```
Creative/Static Localization/<date>-<source>-to-<target>/
  source/        the originals, untouched
  translations.md
  prompts/       one .txt per generation, NN-plate.txt
  plates/        raw Higgsfield renders + the job JSON
  layouts/       NN.json for compose.py
  final/         the deliverables, NN-<lang>.png
  review/        side-by-sides and the contact sheet
```

Make 2×2 contact sheets of the sources and look at every creative before writing anything.

### 2 · Match, spec and translate (no credits)

For each creative in the batch:

1. **Find its Hungarian twin** in the copy bank. If the creative is new to the bank, find the twin in the Hungarian files, transcribe it word for word, and add it to the bank. If there's no twin, translate from the creative's own language and say so in the row.
2. Write one block in `translations.md`: every text element in Hungarian (headline, body, labels, badge text, attribution), the line breaks, which words are coloured and in what colour, then the translation element by element with the same words coloured. Note what's in the product cluster.

Translation rules:

- **Stick to the original copy.** These are vetted ads with good numbers. Same meaning, same claim, same person and tense. Headlines most of all: a question stays a question, "you" stays "you."
- **Natural to a native reader.** Not word for word, but nothing added and nothing softened.
- **Use the glossary terms exactly.** Book titles are spelled as printed on the supplied covers. *Tudat* is "the conscious mind," not "the mind."
- **No full stop at the end of a headline** in English. Question marks and exclamation marks stay.
- **Keep the emphasis.** If a phrase is red or gold in the source, the matching phrase is red or gold in the translation.
- **Testimonial names get localised** to the target market: a first name that's at home in the language, the same initial style, the same age, a city in the market (EN/UK: "Mary K. (47), Manchester" for *K. Mária (47), Debrecen*).
- **Mind the length.** Tighten the wording before you shrink the type.
- Text already in the target language (a "BEST SELLER" seal, "BLACK FRIDAY") stays as it is.
- Tag unverified claims `[Stated]` in the notes and move on.

Mirella sees the translations for the batch before generation. For creative #1 of a batch the translation and the render can be shown together.

### 3 · Generate the plate in Higgsfield

The plate is the ad with the headline, body and any fixed badges translated, and with the old products, the plus sign and the offer label removed. Build the prompt from `references/prompt-template.md`, save it as `prompts/NN-plate.txt`, then:

```bash
# from the batch folder; writes plates/NN-v1.json and plates/NN-v1.png
python3 ../../../.claude/skills/static-ad-localizer/scripts/plate.py <id> --tag v1
```

(`plate.py` wraps `higgsfield generate create nano_banana_pro … --resolution 2k --wait --json` and downloads the result. `--model gpt_image_2_5` switches model, `--aspect` sets the ratio.)

- Use the source's own aspect ratio.
- **Name the typefaces.** Headlines in these statics are League Spartan Bold; most body copy is Montserrat Bold. Say "do not use a wider typeface and do not widen the letter-spacing," and where you can, say where line 1 ends as a share of the image width. "Heavy geometric sans-serif" alone lets the face drift.
- **Give the line breaks for every text block**, headline and body, line by line. Left to itself the model wraps differently on every run.
- **Type the curved apostrophe (’) in the prompt** and say every apostrophe is the same one.
- **Round CTA badges stay in the plate** (same place, same size). Give their text as lines so it sits centred in the shape, longest line in the middle.
- Download `result_url` from the JSON right away; the links expire.
- **Default model: Nano Banana Pro** (2 credits at 2K). It holds the original typefaces. GPT Image 2.5 (`gpt_image_2_5 --quality high --resolution 2k`, 2.75 credits) is the fallback when a plate fails twice.
- Run the nine after approval in parallel, three at a time. In zsh, don't loop over a quoted list of ids (`for n in "2 3 4"` passes one string); launch each id explicitly with `&` and `wait`.

### 4 · Check the plate

Open it and check, in this order:

1. **The headline typeface.** Stack a crop of the new headline under the original's headline and compare letter shapes, weight and spacing. Same face or it fails.
1. **Every word, letter by letter, against `translations.md`.** Apostrophes, quote marks, capitals, no full stop on the headline. One wrong character fails the plate.
2. **The line breaks are the ones you asked for.**
3. **No source-language text left anywhere.**
4. **The coloured words are the right words.**
5. **The photo is the same photo.** Faces most of all: the founder's face is a brand anchor and must not drift. Compare a crop against the source side by side.
6. **The old products, the plus sign and the label are gone** and the background under them is clean.
7. **Nothing was added.**

If it fails, fix the one line of the prompt that caused it and rerun. Two fails on the same creative: switch model. Log what fixed it in `references/rules.md`.

**Patch, don't reroll, once part of a plate is approved.** A rerun redraws everything, so an approved badge or body block can come back different. When only one block has to change, generate the new plate, then copy just that band from it onto the approved plate with a soft (about 50px) feathered seam through a text-free strip. Two plates of the same source line up to within a pixel or two, so the seam doesn't show. Save the result as `plates/NN-...-patched.png` and look at the seam on a zoomed crop.

### 5 · Paste the layers

Layers, all from `Brand/Product Images/`: the books and the Guide (`<LANG>/`), the plus sign (`plus-red-gold.png`), and the offer label (`<LANG>/labels/`). Write `layouts/NN.json` with the approved cluster:

```bash
# from the batch folder. x0, y0 = top-left of Book 1; k = size of the whole cluster (1.0 = 1187 x 1007 px on a 2048 canvas)
python3 ../../../.claude/skills/static-ad-localizer/scripts/make_layout.py <id> --plate plates/NN-v1.png \
  --x0 60 --y0 980 --k 1.0 --label darkred        # or gold | ticket-gold | none (+ --guide-scale 1.2)
```

Pick `x0`, `y0`, `k` from the original: the cluster goes where the old one was, starts at least 60px under the last line of body copy, ends about 60px above the bottom edge, and stops short of the badge and of any face. Then run:

```bash
python3 .claude/skills/static-ad-localizer/scripts/compose.py "<batch>/layouts/NN.json"
```

The script trims each cutout, scales it and alpha-pastes it. It can centre one item between two others or over another (`between`, `center_over`; see the header of the script), so centring is measured, not eyeballed. It prints where everything landed and warns if something runs off the canvas or was scaled up.

**Offer labels are assets, not plate text.** One file per style per language, made once and reused: `labels/new-offer-darkred.png` exists. `labels/new-offer-gold.png` (gold text for dark creatives; the dark red file recoloured locally, so the letters are identical) and `labels/new-offer-ticket-gold.png` (the gold ticket) exist too. When a creative needs a style that isn't there yet, first try recolouring an existing label; otherwise make it with GPT Image 2.5 on a transparent background from a crop of the label as the reference (`--background transparent --aspect_ratio 21:9 --quality high`), check it on a light and a dark background, trim it, and save it next to the others.

Layout rules for the current offer:

- **Fill the space the old cluster filled.** The originals leave no empty pockets. Start the books right under the body copy and run them to the bottom margin.
- **Order, left to right:** Book 1 (BEST SELLER ribbon), Book 2 (NEW ribbon) overlapping it, the Practical Guide.
- **Book 2 sits in front of Book 1, lower and to the right**: start it at about 70% of Book 1's width and drop it by about 24% of the book's height, so the NEW ribbon lands in the clear band between Book 1's author name and its title. Book 1's author name and most of its title stay readable.
- **The Guide is smaller than the books** (about 65 to 70% of a book's height) and shares Book 2's baseline.
- **The plus sign sits between Book 2 and the Guide**, centred in the gap by the script (`between`) and level with the Guide's middle. The Guide stands on its own, not tucked against Book 2.
- **The offer label is big and sits in the notch**: to the right of Book 1's top, above Book 2 and the Guide, its right edge lined up with the Guide's right edge. About 28% of the canvas width on a square creative. Close to the products, never floating on its own.
- **Nothing touches**: keep clear of the round badge, the body copy, and any face or hand in the photo.
- Use the ribbon versions of the books unless the original already has its own bestseller mark right next to the book and the two would collide.
- Single-book originals: see `references/rules.md`.

Worked example: `Creative/Static Localization/2026-09-30-ro-winners-to-en/layouts/01.json`.

### 6 · Check the final and show it

Look at the composed image at full size and at a zoomed crop of the cluster. Covers crisp, nothing overlapping text, nothing off the canvas, no empty pockets. Then build the side-by-side in `review/` (original left, new right).

- **Creative #1 of the batch:** send the side-by-side and stop for approval.
- **After approval:** run the rest, then send one contact sheet of the batch with the list of anything flagged.

### 7 · Feedback

When Mirella corrects anything (a word, a layout, a colour, a model choice, the process):

1. Say what you understood in one line.
2. Add it to `references/rules.md` as a dated rule with the reason. If it's a term, add it to the glossary. If it changes a step of the pipeline, edit this file too.
3. Redo only the affected creatives.

The rules file is what makes the next batch better than this one. Every correction lands there, even the small ones.

## Standing rules

- **Never redraw a product.** Products only ever come from `Brand/Product Images/<LANG>/` through `compose.py`.
- **Never invent text.** Nothing appears on the ad that isn't in the original or in the approved translation. No prices unless the original shows one and a real charged price is supplied for the new market.
- **Translate from Hungarian.** A translated set is a layout reference, not a copy source.
- **Report credits.** Say what a batch will cost before running it and what it did cost after.
