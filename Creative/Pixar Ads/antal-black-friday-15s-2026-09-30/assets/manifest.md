# Asset manifest — antal-black-friday-15s-2026-09-30

Job ids are Higgsfield generation ids; they can be passed as references in place of the file. Signed URLs expire; the files here are the record.

| Label | File | Model | Job id | Status | Notes |
|---|---|---|---|---|---|
| Antal reference photo | `characters/antal-ref-photo.png` | (supplied by Mirella, 2026-09-30) | — | source | Black turtleneck portrait |
| Antal hero, GPT | `characters/antal-hero-gpt.png` | gpt_image_2_5 | da8ba404-6612-44fe-8934-623d6006b0bb | **chosen** | Best likeness; slightly grainy figurine texture |
| Antal hero, Nano Banana | `characters/antal-hero-nb.png` | nano_banana_2 | f1a208e7-d9aa-4c0d-a557-4cd2f6dccdc4 | rejected | Cleaner animation, weaker likeness (greyer, more generic face) |
| **Antal character sheet** | `sheets/antal-sheet.png` | nano_banana_2 from the GPT hero | 46c0a376-6f8e-43d1-92c4-52b8526d5ada | **approved for video** | Front, 3/4, side, back, two face panels; likeness kept, texture smoothed. This is Image 1 in every video prompt |
| Study v1 | `locations/study.png` | gpt_image_2_5 | f4e86857-3b94-4502-98bc-b17161e98c46 | rejected | Photoreal, not the animated look |
| **Study v2** | `locations/study-v2.png` | nano_banana_2 | 8fb7253b-24ee-406a-baed-5f416badf01f | **approved for video** | Animated look, open floor in front of the shelf, spines unreadable, green lamp and mug. Image 2 |
| Book 2 real cover | `props/book2-cover-real.png` | (supplied) | — | source | |
| Book 1 real cover | `props/book1-cover-real.png` | (supplied) | — | source | Not used in v1; for the kitchen-table variant |
| Book 2 prop v1 | `props/book2-prop.png` | gpt_image_2_5 | a805e667-e69d-4c8d-8b61-8eb4e126a934 | alternate | Cover exact |
| **Book 2 prop v2** | `props/book2-prop-v2.png` | nano_banana_2 | 68d68da3-ca6e-49a7-8d4b-8b3130ad8397 | **approved for video** | Cover exact, softer render. Image 3 |
| **Antal voice reference** | `voices/antal.mp3` | ffmpeg from `~/Downloads/2 2.MOV`, 0:11–0:41 | — | approved | 30 s, mono. Assumed to be Antal speaking alone (not listened to; confirm). Audio 1 |
| Voice source preview | `voices/antal-source-preview.mp4` | ffmpeg | — | reference | 360p, silent, same 30 s window, to check who is on screen |
| **Draft take 1** | `../segments/seg1-draft-take1.mp4` | seedance_2_5 draft (480×854, 15.05 s, audio) | 3c999b0a-5e0c-44a4-a8d7-0d2b81e69400 | under review | Prompt `prompts/seg1-take1.txt`; 45 credits; queued 37 min |

Credits used so far: about 54 (images 9, draft 45). Balance: 447.75.
