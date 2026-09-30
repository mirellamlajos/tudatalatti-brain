#!/bin/zsh
# Usage: assets/voices/build-vo.sh <line1.mp3> <line2.mp3> <line3.mp3> <out.wav>
# Timeline (20 s): L1 at 0.4 s, L2 at 5.2 s, L3 at 10.8 s, total 20.0 s, mono 44.1 kHz, peak-normalised
set -e
L1=$1; L2=$2; L3=$3; OUT=$4
ffmpeg -y -loglevel error \
  -i "$L1" -i "$L2" -i "$L3" \
  -filter_complex "\
[0:a]aformat=sample_rates=44100:channel_layouts=mono,adelay=400|400[a0];\
[1:a]aformat=sample_rates=44100:channel_layouts=mono,adelay=5200|5200[a1];\
[2:a]aformat=sample_rates=44100:channel_layouts=mono,adelay=10800|10800[a2];\
[a0][a1][a2]amix=inputs=3:normalize=0,apad=whole_dur=20,atrim=0:20,loudnorm=I=-18:TP=-1.5:LRA=9[out]" \
  -map "[out]" -ar 44100 -ac 1 "$OUT"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
