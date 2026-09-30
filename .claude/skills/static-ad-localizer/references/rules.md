# Rules learned from feedback

Read this before every run. Newest rules at the bottom of each section. Every rule has a date and a reason so it can be judged later.

**Status:** batch 1 (creatives 1–10 of the Romanian winner set, to English) is generated. Creative #1 was approved on 2026-09-30; 2–10 are waiting for Mirella's review. Thirteen creatives (11–23) are left for batches 2 and 3.

## From the brief (Mirella, 2026-09-30)

- **Precise copy.** The regenerated creative matches the original exactly. Only the language and the product cluster change.
- **Use the supplied product images.** Never let the generator redraw a book. Reason: the supplied images are high quality and already translated.
- **Batches of 10** until she says to do them all. **The first creative of every batch is approved before the rest**, on every batch, for good.
- **She approves the whole process** before the skill counts as built.
- **Any language to any language.** Hungarian sources are the norm; the first batch happened to be Romanian. English first, Spanish next.
- **The offer (from 2026-09-30):** buy Book 1 + Book 2, get the Practical Guide free. Old creatives show Book 1 + the first Guide.
- **Never say "three books for the price of two."** The Guide is a smaller book and it's a gift.
- **No price and no offer title is needed on the ad.** The originals don't show one. "NEW BOOK BUNDLE" from the product-page image is not to be copied over.
- **The product-page bundle image is a style guide, not a template**: two books side by side with their ribbons, a plus sign, the Guide. Arrange it so it looks good in each creative.
- **Brand terms come from the brand's site in that language** (EN: subconsciouscontrol.com). See the glossary.

## Wording (Mirella, 2026-09-30, round 2)

- **Translate from the Hungarian original, never from another translation.** Reason: Romanian → English lost meaning (*tudat* became "mind," *káros képek* became "patterns"). The twins are mapped in `Creative/Static Localization/Hungarian Static Copy Bank.md`.
- **Stick to the original copy as much as possible, headlines above all.** These are vetted ads with good numbers; the new market gets exactly the same ad. This includes the second-person question headline (*„Nem tudsz uralkodni a negatív gondolataidon?"* → "CAN’T CONTROL YOUR NEGATIVE THOUGHTS?"). Don't rewrite it into third person and don't offer a softer version.
- **Natural for the target reader, whole meaning kept.**
- **Testimonial names are localised to the market.** UK English: *K. Mária (47), Debrecen* → "Mary K. (47), Manchester." Pick a name that's at home in the language and a city in the market; keep the age.
- **No full stop at the end of an English headline.** Hungarian headlines sometimes carry one; English ones don't. Question and exclamation marks stay.
- **Winners 1, 2 and 3 take the Hungarian headline:** "THE LAW OF ATTRACTION / DOESN’T WORK", not the Romanian set's "isn't what it seems." Where a translated set and the Hungarian disagree, the Hungarian wins.
- **CTA badge, English:** "GET IT / TODAY AT THE / BEST PRICE!" on three lines, the long line in the middle, so the block sits centred in the circle. She suggested the break herself.

## Layout (Mirella, 2026-09-30, round 2)

- **No empty spaces.** In the originals every part of the frame is used. The three-item cluster has to fill the area the two-item cluster filled.
- **The "NEW OFFER!" label sits close to the products**, lower than in the first test, not floating off-centre. It's a pasted layer now so it can be placed exactly.
- **The plus sign is exactly centred** in whatever it sits between or next to. Use the script's `between` / `center_over`; don't eyeball it.
- **Badge text is centred in its shape**, cut into lines that suit the shape, sized to look like one piece with the badge.
- **She liked the type** Nano Banana Pro produced. Keep that model for plates.
- **The layout she chose (round 3, 2026-09-30):** the Guide stands on its own with the plus between it and Book 2 (the row from option A), and "NEW OFFER!" is big and sits up in the notch above Book 2 and the Guide (where option C had it). She did **not** like the Guide tucked against Book 2, and she did not want the plus in front of the label. Worked numbers: `layouts/01.json` in the first batch (books about 39% of the canvas height, Guide about 24%, label about 28% of the width).
- **The headline must be in exactly the original's typeface** (Mirella, round 4: "attraction" looked wider than the original). She was right: one rerun set the headline wider, heavier and looser. Name the face in the prompt (the statics' headlines are League Spartan Bold; most body copy is Montserrat Bold), say "do not use a wider typeface and do not widen the letter-spacing," and give the line's end point as a share of the image width. Then stack a crop of the new headline under the original's and compare letter shapes and spacing before anything ships.
- **The badge on three lines is approved** ("very good job"). Don't let a rerun change it.

## From the tests (2026-09-30)

- Nano Banana Pro at 2K kept the original typefaces. GPT Image 2.5 at high quality spelled everything right but swapped the headline face. Both kept the photo intact.
- "Remove the books, the plus sign and the label and continue the background" works in one pass.
- **Without line breaks in the prompt the body copy wraps differently on every run** (one run left "energy." alone on a line). Give every block its lines.
- **Apostrophes came out mixed** (straight in the headline, curved in the body) until the prompt used ’ and said so.
- The bare gold plus from the product page gets lost on a bright background. The gold plus on a dark red disc (`Brand/Product Images/plus-red-gold.png`) reads everywhere and matches the originals.
- A label generated by GPT Image 2.5 on a transparent background from a crop of the rendered label came back clean on the first try: same face, same gradient, real transparency.
- The row layout can't grow: at 2048px, two books at 30% overlap, a plus and a Guide only fit between the left margin and the round badge with books about 800px tall. Bigger books need the plus moved out of the row (layout C).
- If Book 2 isn't dropped far enough, its NEW ribbon covers Book 1's author name.
- The image viewer can make a smooth sky look blotchy. Judge background quality on a zoomed crop, not on the full-frame preview.

## From batch 1, creatives 2–10 (2026-09-30)

- **Plan on about two plates per creative.** Nine creatives took nine first runs plus ten reruns. Budget 4 to 5 credits per creative, not 2.
- **When the English line is shorter than the source line, the model blows the headline up to fill the width.** It happened on 5, 8, 9 and 10. Say the headline is "NOT larger than the original," give the cap height as a share of the image height (these statics: about 4.2 to 4.5%), and give each line's width. Then stack the crop under the original's. The "line 1 ends at about N% of the image width" wording, placed right before the lines, is the one that works most often.
- **Long centred text can come back with a stuttered word** ("withs with," "wasr wasn’t" on the testimonial). Read every line; add "copy these lines character for character, no word repeated" and rerun.
- **A plus sign can survive the removal** (twice on creative 6, left floating on the laptop). Look for it. Patch that spot from another plate of the same creative, or rerun with "erase it entirely, leave no plus sign anywhere."
- **A rerun can undo a colour or a line break that was right the first time** (creative 6 turned "thoughts" gold; creative 10 broke the headline as "REAL CHANGE BEGINS / WITHIN" and used a low „ quote mark). Never assume the parts you didn't touch came back the same; recheck the whole plate.
- **Body copy must clear the photo's subject.** On 6 the longer English line ran into the man's hair; the fix was a narrower column ("no line reaches past 52% of the image width").
- **The books must clear the last line of body copy.** Book 1's ribbon sticks up above the book; leave at least 60px between the last text line and the ribbon (creatives 6 and 7 needed the cluster lowered and shrunk).
- **Originals with no offer label get no label.** Creatives 3, 5, 7 and 8 have none. There the Guide is set 1.2× larger so the notch above it doesn't sit empty (`make_layout.py --label none --guide-scale 1.2`).
- **Label styles follow the original:** dark red text on the light sunset creatives, gold text on the dark ones, the gold ticket on creative 6.
- **Where the original books sit on a person, the new ones do too** (4, 5, 6, 8, 9). Never cover a face; hands, sleeves and a mug are fine, as in the originals.
- **`HTTP 520 … failed to PUT media bytes`** from Higgsfield is an upload hiccup. Run the same command again.

## Open questions (remove each one when answered)

- **Hungarian originals missing** for winners 1, 10, 22 (the "real success and deep contentment" quote), 11 (the "other speakers" card) and 17 ("don't try to reach success through willpower"). Until they turn up, those are translated from the Romanian.
- **Single-book creatives** (12, 18, 19, 22). Show the full bundle there too, or Book 1 plus Book 2, or leave Book 1 alone?
- **#18's market line** (*„Bestseller în România, mii de cititori mulțumiți"*). What's the true line for the UK?

## Failures and fixes

| Date | Creative | What went wrong | Fix |
|---|---|---|---|
| 2026-09-30 | 1 | Body copy re-wrapped with an orphan last line; apostrophes mixed | Line breaks written into the prompt; ’ typed in the prompt plus the "same apostrophe" line |
| 2026-09-30 | 1 | Label placed by the model sat off-centre, far from the products | Label removed from the plate and pasted as a layer |
| 2026-09-30 | 1 | Headline typeface drifted wider and heavier on a rerun (prompt said only "heavy geometric sans-serif") | Named the face (League Spartan Bold), banned wider type and looser spacing, pinned the line's end at 73% of the width; matched on the next run |
| 2026-09-30 | 1 | Rerun for a new headline brought the badge back on four lines and re-wrapped the body, though the prompt was unchanged there | Kept the approved plate and patched in only the headline band from the rerun (feathered seam at y 360–410 of 2048) |
