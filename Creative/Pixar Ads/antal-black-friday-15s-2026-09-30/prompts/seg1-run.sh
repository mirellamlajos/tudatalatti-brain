#!/bin/zsh
# Usage: ./prompts/seg1-run.sh draft|final <take>
set -e
cd "$(dirname "$0")/.."
MODE=$1; TAKE=${2:-1}
EXTRA=""; [ "$MODE" = "draft" ] && EXTRA="--draft=true"
higgsfield generate create seedance_2_5 \
  --mode omni_reference \
  --prompt "$(cat prompts/seg1-take${PROMPT_TAKE:-3}.txt)" \
  --image-references assets/sheets/antal-sheet.png \
  --image-references assets/locations/study-v2.png \
  --image-references assets/props/book2-prop-v2.png \
  --audio-references assets/voices/antal-dialogue-${VO:-16s}.mp3 \
  --aspect_ratio 9:16 --duration ${DUR:-16} --resolution 1080p \
  --generate_audio true --bitrate_mode high $EXTRA \
  --wait --wait-timeout 30m --json > "segments/seg1-$MODE-take$TAKE.json"
URL=$(jq -r 'if type=="array" then .[0] else . end | .result_url' "segments/seg1-$MODE-take$TAKE.json")
curl -sL "$URL" -o "segments/seg1-$MODE-take$TAKE.mp4"
echo "saved segments/seg1-$MODE-take$TAKE.mp4"
