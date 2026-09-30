# Plate prompt template

One prompt per creative. Fill the brackets from the creative's block in `translations.md`. Describe each text element by where it is and what it looks like, then give the exact new text line by line. Keep the wording below; it's the version that produced a clean plate (creative #1, third run, 2026-09-30; saved as `prompts/01-plate-v3.txt` in the first batch).

```
Edit the attached image. It is a [square 1:1] Facebook ad for a book. Reproduce it EXACTLY: the same background photo ([two or three things that identify the photo]), the same colours, the same layout, the same typefaces, the same text sizes and positions. Make only the two changes below.

CHANGE 1: Replace the [Romanian] text with the [English] text given here. Each [English] text sits in the same place, in the same typeface, weight, colour and size as the text it replaces. Spell every word exactly as written, nothing added, nothing left out.

- Headline, [position], [type description: e.g. heavy black geometric sans-serif, all caps], [N] lines, no full stop at the end:
  line 1: [TEXT]
  line 2: [TEXT]
  [Colour note if any: The words "[X]" are red (the same red as in the original). Every other word is black.]

- Body paragraph [position], [type description], [alignment], same left margin as the headline, exactly [N] lines broken like this:
  line 1: [TEXT]
  line 2: [TEXT]
  ...
  [Colour note]

- [Round badge / seal description], same size and position as the original. [Type description] on exactly three lines, each line centred horizontally, and the three-line block centred vertically in the shape with equal space above and below and equal space left and right:
  line 1: [TEXT]
  line 2: [TEXT]
  line 3: [TEXT]

[One bullet per remaining text element. Elements already in the target language: "Keep the [gold BEST SELLER seal] exactly as it is."]

CHANGE 2: Remove these things completely: [the two red books], [the small round red-and-gold plus sign between them], and [the dark red label "OFERTĂ NOUĂ!" above the smaller book]. Fill the area where they were with the natural continuation of the background ([what the background is there]). Leave that whole [lower-left and lower-middle] area empty: no books, no objects, no shadows, no text.

Every apostrophe in the image is the same curved typographic apostrophe (’).

Do not add anything else: no new elements, no logos, no watermark, no border. No [Romanian] words may remain anywhere in the image.
```

## Notes

- Line breaks for every block. Break the body so the lines are even and nothing is left alone on the last line. Keep the block as wide as the original's.
- Type ’ in the prompt text itself, not '.
- The offer label ("NEW OFFER!") is never in the plate. It's pasted as a layer.
- If a person's face is in the ad, add: "The person's face, hair, expression and clothing stay exactly as in the original. Do not retouch or regenerate the person."
- If a book overlaps a person or a hand in the original, say what the removed area should show ("her green jumper continues where the book was").

# Label asset prompt

For a new label style. Reference image: a tight crop of that label from the source creative or from a plate.

```
Reproduce the text in the attached image exactly: the words [NEW OFFER!] in the same tall condensed bold all-caps display typeface, the same letter shapes and spacing, the same [dark red colour with the same subtle gradient to a darker red-brown at the bottom of the letters]. Output ONLY the text on a fully transparent background. No background colour, no sky, no shadow, no glow, no outline, no frame, no other elements. The text is one line, centred, and fills about 85% of the image width. Crisp, sharp edges.
```

```bash
higgsfield generate create gpt_image_2_5 --prompt "$(cat prompts/label-<style>.txt)" \
  --image-references <crop>.png --aspect_ratio 21:9 --quality high --resolution 1k \
  --background transparent --wait --json > <out>.json
```

Check it on a light and a dark fill, trim to the solid pixels, save to `Brand/Product Images/<LANG>/labels/<text>-<style>.png`.
