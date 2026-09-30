---
status: APPROVED script and assets (2026-09-30); video in production
skill: pixar-ai-video-ads
---

# Brief — „A könyvespolc" · Antal, Book 2, Black Friday · 15 s

## 0. Header

| Field | Value |
|---|---|
| Working title | A könyvespolc (The bookshelf) |
| Slug | `antal-black-friday-15s-2026-09-30` |
| Product / offer | Book 2 (*A tudatalattid határtalan ereje 2*) in the Black Friday offer. Offer details: **TO CONFIRM** (bundle contents, price, dates, landing page) |
| ICP | Core avatar + ICP 1, and warm Book 1 readers who "understand it all, yet nothing changes" |
| Sub-flavour | Founder monologue with a pinned headline card (a founder card in animation, not a story: 15 s is an announcement, not a narrative) |
| Length | 1 segment, 20 s (was 15; the natural-pace Hungarian dialogue runs 16.5 s of speech) |
| Aspect / resolution | 9:16 · 1080p (720p for the test render if credits are tight) |
| Language | Hungarian, every spoken line and every caption |
| Runs from | Lajos Antal's verified page |
| Landing page | TO CONFIRM (Book 2 product page or the Black Friday page) |

**Buyer read-back (Phase 0):**
1. Viewer: 50+, mostly 65+, reading on a phone in the evening; many already own Book 1.
2. Objections: scepticism first, "how exactly does it work" second, and for Book 2 specifically "I read the first one and I'm still stuck."
3. Sophistication: high. They have read the canon. Lead with the plateau, not a promise.
4. Mechanism to dramatise: understanding is not change; the subconscious protects, it doesn't sabotage; the second volume is the how.
5. False belief attacked: "if I understand it, it'll change."
6. Enemy: the pile of books that explained everything and changed nothing. Never the reader.

## 1. Cast sheet

### Antal — the author, speaking to camera

Rendered from a reference photo the team supplies (the black-turtleneck portrait). **Consent: the user requested the founder's likeness on 2026-09-30; the CEO approves paid use.**

- **Age and build:** 60s look (confirm), medium height, solid build, straight posture
- **Face:** from the reference photo; stylised, not caricatured; kind eyes, a calm mouth
- **Hair:** from the reference photo (confirm colour and grey)
- **Clothing (fixed):** black turtleneck, dark charcoal trousers, no jewellery. The brand's event portrait look
- **Signature prop:** Book 2 (blue cover)
- **Personality:** unhurried, dry, a neighbour who has seen it all and isn't selling; talks with one hand, the other holds the book
- **Voice profile (assumption until a sample arrives):** male, low-mid pitch, unhurried, warm and dry, plain eastern-Hungarian register, no radio polish. Example line: „Elolvastad. Megértetted. Mégsem változott semmi."
- **Expressions needed:** the level look at the shelf (a little weary); the small lift when he takes the book down; the half-smile at the close
- **Voice reference:** if a clip of Antal speaking exists in the 2023–2025 founder-video library, 15 to 30 s of him alone becomes `assets/voices/antal.mp3` and is bound as Audio 1

## 2. Locations

### The study

- **What it is:** a home study, one tall wooden bookshelf packed with worn self-help paperbacks (spines only, no readable titles, no real brands), a desk edge, a reading lamp
- **Time of day and light:** late afternoon, warm lamp on, soft window light from the left
- **Three concrete items:** the crowded shelf, a green-shaded desk lamp, a mug on the desk
- **Camera:** eye level, gentle push-ins, no handheld shake
- **Palette:** warm brown, deep blue (the book), gold (lamp light)
- **Continuity:** the shelf never changes; the blue book is the only blue thing in frame

## 3. Props

| Prop | Must match | Reference | Notes |
|---|---|---|---|
| Book 2, blue cover | The real cover exactly: title, layout, colours | **TO SUPPLY** (cover file) | Only the rendering style changes |
| Book 1, red cover | Only if the offer is the bundle | **TO SUPPLY** if needed | |

## 4. Script, shot by shot (one segment, 0:00–0:15)

| Time | Location | In frame | Camera | Action | Dialogue (HU) | Caption (HU) | Headline card |
|---|---|---|---|---|---|---|---|
| 0:00–0:05 | Study | Antal beside the shelf | Medium, slow push in | He taps two worn spines with one finger, looks at camera, calm and kind | „Elolvastad. Megértetted. Mégsem változott semmi." | ELOLVASTAD. MEGÉRTETTED. / MÉGSEM VÁLTOZOTT SEMMI. | „Megjelent a 2. kötet" |
| 0:05–0:10.5 | Study | Antal, the blue book | Medium-close, static | He pulls Book 2 from the shelf, holds it chest-high, cover to camera | „Ezért írtam meg a második kötetet. Onnan indulunk, ahol elakadtál." | EZÉRT ÍRTAM MEG A MÁSODIK KÖTETET. / ONNAN INDULUNK, AHOL ELAKADTÁL. | same |
| 0:10.5–0:18.5 | Study | Book cover, then his face | Close on the cover, then up to his half-smile | Holds, small nod | „Hétfőig huszonöt százalékkal olcsóbb. Kattints a linkre itt lent, és olvass bele." | HÉTFŐ ÉJFÉLIG 25%-KAL OLCSÓBB. / KATTINTS A LINKRE ITT LENT, ÉS OLVASS BELE. | same |

**Last speaker:** Antal. **Word count:** 25. Runs 20 s at a natural pace with a silent 1.5 s hold at the end.

**Dialogue production (2026-09-30):** Seedance cannot speak Hungarian (draft take 1 was fluent gibberish), so the dialogue is generated line by line with Seed Audio 1.0 cloning Antal's voice from `assets/voices/antal.mp3`, verified by whisper, assembled by `assets/voices/build-vo.sh` into `assets/voices/antal-dialogue-20s.mp3`, and Seedance lip-syncs to it (prompt `prompts/seg1-take2.txt`). Line 3 says „Hétfőig" instead of „Hétfő éjfélig" because the cloned voice stumbles on „éjfélig"; the midnight detail lives in the caption and the primary text. Known soft spot: the clone clips the end of „Megértetted" in every take.

**Tone revision (Mirella, 2026-09-30):** kinder and more inviting. Final lines approved by Mirella 2026-09-30: the short three-beat open stays; he walks with the reader („onnan indulunk"), and the close is an invitation that names the link. Alternative warmer close on file: „A linket itt lent találod, kattints rá, és olvass bele. Várlak." (needs 18 s).

**Offer (confirmed by Mirella, 2026-09-30):** Book 2 at 25% off, live from Black Friday until Cyber Monday at midnight. No price is shown; "olcsóbb" (cheaper) is the plain word. The 25% is off the 6,950 Ft price the book has been sold at since September, so the reference price is real. Headline card: „Black Friday · 25% kedvezmény a 2. kötetre".

Spoken-register check: three fragments open it, one longer line in the middle, a short close. Read aloud, the breaths fall unevenly. No triplet-for-rhythm, no signpost transitions, no "de itt a lényeg." Native words throughout (kötet, kedvezmény, elakadtál).

## 5. The spine

- **Keep:** the "read it, understood it, nothing changed" open; "onnan indulunk, ahol elakadtál"; the book shown cover-to-camera; the invitation close that names the link.
- **May change for a new Entity ID:** the opening frame (shelf vs kitchen table vs the newsroom anchor), the first prop he touches, the room.

## 6. Meta copy (draft; offer line to confirm)

Megjelent a második kötet.

Az első könyv megmutatta, hol a megoldás.

Ez a kötet megmutatja, hogyan férsz hozzá.

Ott kezdődik, ahol a legtöbben elakadnak: már mindent értesz, mégsem változik semmi.

Black Friday-ig kedvezménnyel. [ajánlat + ár, ha megerősítve]

👇 👉 [link]

**Headline:** Amikor már mindent értesz, mégsem változik semmi
**CTA:** Megnézem 👉
**Landing page:** TO CONFIRM

## 7. Compliance table

| Line or scene | Rule it touches | Why it stays safe |
|---|---|---|
| „Elolvastad. Megértetted. Mégsem változott semmi." | Personal attributes | It's about reading, not a health, mental-health, weight or money attribute; and it's the brand's own title line |
| „Onnan indulunk, ahol elakadtál." | Health claims | No outcome promised; the brand's published positioning |
| „Hétfő éjfélig 25 százalékkal olcsóbb." | No fake prices | Fine once the pre-discount price is one that was charged. Never strike through 11,750 Ft for Book 2 (it was never sold at that price). If a price appears on screen: „6 950 Ft + ajándék Útmutató" framing, or the confirmed bundle price |
| A cartoon of the founder | Likeness, consent | Requested by the team; the founder is the brand's public face; keep him dignified and recognisable, never caricatured |
| The shelf of worn self-help books | Comparative advertising | No readable titles or real brands on the spines |
| No guarantee, no cure, no doctor, no numbers | Hard floor | None used |

## 8. Variant plan (Andromeda, for after the first test)

| Variant | What changes in the first 3 s | Reused assets | New calls |
|---|---|---|---|
| v1 | Shelf open (this brief) | | 1 |
| v2 | Kitchen-table open: coffee mug, Book 1 red on the table, he slides Book 2 next to it | Antal sheet, book props | 1 |
| v3 | Newsroom anchor open: „Megjelent a második kötet", cut to Antal for lines 2 and 3 | Antal sheet + a new anchor sheet | 1 |
| v4 | Close-up open on the worn spines, then reveal Antal | all | 1 |

## 9. Cost and call count (checked 2026-09-30, this account)

| Step | Calls | Model | Credits |
|---|---|---|---|
| Antal hero image, 2 models | 2 | gpt_image_2_5 (0.25) / nano_banana_2 (2) | ~2.5 |
| Antal character sheet | 1–2 | nano_banana_2 | ~4 |
| Study location | 1–2 | gpt_image_2_5 | ~0.5 |
| Book 2 prop | 1–2 | gpt_image_2_5 | ~0.5 |
| Video, 15 s, 1080p | 1 (+1 allowance) | seedance_2_5 | **180 each** |
| Account balance | | | 501.5 |

A 1080p render is 180 credits, so the plan allows two full-quality attempts and not three. Cheaper checks on the same 15 s: 720p = 105, 480p = 45, `--draft true` at 1080p = 45. Plan: one draft (45) to catch language, voice and likeness problems, then one 1080p final (180). Total ≈ 235 credits, leaving one more full render in reserve.
