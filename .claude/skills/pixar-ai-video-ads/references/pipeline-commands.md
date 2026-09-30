# Pipeline Commands — Higgsfield CLI + ffmpeg

The tutorial runs this pipeline in the Higgsfield web app (generate images, click "assign element" to register characters and locations, prompt Seedance 2.5 with the elements attached, "extend video" with the last 10 seconds, upload a voice reference). Everything below is the same pipeline on the CLI, which this machine has (`/opt/homebrew/bin/higgsfield`) alongside ffmpeg (`/opt/anaconda3/bin/ffmpeg`). Either path is fine; the CLI is scriptable and keeps the prompts on disk.

Schema facts below were read from `higgsfield model get seedance_2_5 --json` on 2026-09-29. Re-check before a big run; models change.

## Bootstrap

```bash
higgsfield account status
```

If it says not authenticated, ask the user to run `higgsfield auth login` in their terminal, and carry on writing prompts until they confirm.

```bash
higgsfield model get seedance_2_5 --json | jq '{params: [.params[] | {name, default, enum}], rules: [.rules[].message]}'
higgsfield model get gpt_image_2_5 --json | jq '{aspect_ratios, params: [.params[].name]}'
higgsfield model get nano_banana_2 --json | jq '{aspect_ratios, params: [.params[].name]}'
```

## Seedance 2.5, what the schema says

| Param | Values | Notes |
|---|---|---|
| `mode` | `t2v` · `omni_reference` · `video_edit` · `video_extension` | `t2v` accepts no media. `omni_reference` needs ≥1 reference. `video_extension` needs ≥1 video reference and `extension_mode`. |
| `extension_mode` | `forward` · `backward` | forward = sequel, backward = prequel. Only allowed with `video_extension`. |
| `image_references` / `video_references` / `audio_references` | arrays | Up to 50 reference items in total across all kinds plus start/end images. |
| `start_image` / `end_image` | one each | Optional first/last frame anchors. |
| `aspect_ratio` | `auto` `21:9` `16:9` `4:3` `1:1` `3:4` `9:16` | Use `9:16`. |
| `duration` | integer, 4–30 | Default 5. Ask for the segment length you scripted. |
| `resolution` | `480p` `720p` `1080p` | Default 720p. Ship at 1080p. |
| `generate_audio` | boolean, default true | This is where the voices come from. |
| `bitrate_mode` | `standard` · `high` | `high` for the final passes. |
| `draft`, `draft_job_id` | boolean, string | A draft path exists in the schema. Test what it does and what it costs before relying on it; if it's a cheap preview, use it before every full-quality call. |

Flags pass through by param name, so `--generate_audio true`, `--extension_mode forward`, `--bitrate_mode high`. The media flags are `--image-references`, `--video-references`, `--audio-references` (repeat the flag per file); `--image`, `--video`, `--audio` are short aliases.

## Phase 3 · images

```bash
# Character hero image (try both models, keep the better face)
higgsfield generate create gpt_image_2_5 --prompt "$(cat prompts/marika-hero.txt)" --aspect_ratio 3:4 --wait
higgsfield generate create nano_banana_2 --prompt "$(cat prompts/marika-hero.txt)" --aspect_ratio 3:4 --wait

# Edit pass on the chosen take
higgsfield generate create nano_banana_2 --prompt "$(cat prompts/marika-hero-fix.txt)" --image assets/characters/marika.png --wait

# Character sheet from the hero image
higgsfield generate create nano_banana_2 --prompt "$(cat prompts/marika-sheet.txt)" --image assets/characters/marika.png --aspect_ratio 16:9 --wait

# Location, in the film's aspect
higgsfield generate create gpt_image_2_5 --prompt "$(cat prompts/kitchen.txt)" --aspect_ratio 9:16 --wait

# Prop: the book, from the real cover
higgsfield generate create gpt_image_2_5 --prompt "$(cat prompts/book.txt)" --image assets/props/book-cover-real.jpg --aspect_ratio 3:4 --wait
```

Download each result into the project folder right away (signed URLs expire), and record file, job id and label in `assets/manifest.md`. A previous job id can be passed as a reference instead of re-uploading the file.

## Phase 4 · first segment

```bash
higgsfield generate create seedance_2_5 \
  --mode omni_reference \
  --prompt "$(cat prompts/seg1-take1.txt)" \
  --image-references assets/sheets/marika-sheet.png \
  --image-references assets/sheets/zsofi-sheet.png \
  --image-references assets/locations/kitchen.png \
  --image-references assets/props/book.png \
  --aspect_ratio 9:16 \
  --duration 30 \
  --resolution 1080p \
  --generate_audio true \
  --bitrate_mode high \
  --wait --wait-timeout 30m
```

Pass the references in the same order the prompt names them (Image 1, Image 2…). Save the render as `segments/seg1-take1.mp4` and the prompt beside it.

If the schema's draft path turns out to be a cheap preview, the pattern is: run once with `--draft true`, judge it, then run the full call and pass the draft's job id as `--draft_job_id`. Confirm this against `higgsfield model get seedance_2_5` output before assuming it.

## Phase 5 · extension and voices

```bash
# Last 10 seconds of the approved segment
ffmpeg -sseof -10 -i segments/seg1-take3.mp4 -c copy segments/seg1-tail10.mp4

# Voice reference: up to 30 s of ONE character speaking, audio only
# (start/end from the approved render's timestamps where only Marika speaks)
ffmpeg -ss 00:00:04 -to 00:00:19 -i segments/seg1-take3.mp4 -vn -ac 1 -ar 44100 -b:a 192k assets/voices/marika.mp3

# Web-app variant of the same thing: black picture + that audio, so nothing visual is taken from it
ffmpeg -f lavfi -i color=c=black:s=1080x1920:r=25 -i assets/voices/marika.mp3 -shortest -c:v libx264 -pix_fmt yuv420p -c:a aac assets/voices/marika-blank.mp4

# Segment 2 as a forward extension, with the voice reference bound
higgsfield generate create seedance_2_5 \
  --mode video_extension \
  --extension_mode forward \
  --prompt "$(cat prompts/seg2-take1.txt)" \
  --video-references segments/seg1-tail10.mp4 \
  --image-references assets/sheets/marika-sheet.png \
  --image-references assets/sheets/zsofi-sheet.png \
  --image-references assets/locations/kitchen.png \
  --audio-references assets/voices/marika.mp3 \
  --aspect_ratio 9:16 \
  --duration 30 \
  --resolution 1080p \
  --generate_audio true \
  --bitrate_mode high \
  --wait --wait-timeout 30m
```

For a prequel, `--extension_mode backward` and a tail cut from the **start** of the clip (`ffmpeg -t 10 -i seg1.mp4 -c copy seg1-head10.mp4`).

Voice references also work in `omni_reference` mode, which is how a variant's brand-new opening segment gets the same Marika voice as the base film.

## Phase 6 · assemble

```bash
# Concatenate approved segments in order
printf "file '%s'\n" segments/seg1-take3.mp4 segments/seg2-take2.mp4 segments/seg3-take1.mp4 > final/list.txt
ffmpeg -f concat -safe 0 -i final/list.txt -c copy final/assembled-raw.mp4

# Normalise loudness, optional music bed under dialogue, final encode 1080x1920
ffmpeg -i final/assembled-raw.mp4 -i assets/music/bed.mp3 \
  -filter_complex "[1:a]volume=0.15[m];[0:a][m]amix=inputs=2:duration=first[a];[a]loudnorm=I=-16:TP=-1.5:LRA=11[out]" \
  -map 0:v -map "[out]" -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k \
  final/<slug>-v1-kitchen-open.mp4

# Burn captions from an .ass or .srt file (big, high-contrast; style set in the .ass)
ffmpeg -i final/<slug>-v1-kitchen-open.mp4 -vf "ass=final/captions-v1.ass" -c:a copy final/<slug>-v1-kitchen-open-cc.mp4
```

The `video-use` skill can do the caption timing, the burn-in and trims conversationally if that's faster than hand-writing the `.ass` file.

If a segment came out at 16:9 by mistake, the Higgsfield `reframe` workflow can convert; better to never let it happen (`--aspect_ratio 9:16` on every call).

## Scoring

```bash
higgsfield generate create brain_activity --video final/<slug>-v1-kitchen-open-cc.mp4 --wait
```

Report overall score, peak hook second and sustain, and the report link. It's a sanity check, not a verdict.

## Cost

Before a run, tell the user the number of video calls the plan needs (segments + extensions + variants + a regeneration allowance of about one per segment). If `higgsfield generate cost seedance_2_5 …` exists in the installed CLI version, quote it; if not, say the tutorial's figure of roughly $10 per generation is a [Stated] number from another account.
