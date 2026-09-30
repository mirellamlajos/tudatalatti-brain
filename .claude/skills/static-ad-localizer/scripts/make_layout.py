#!/usr/bin/env python3
"""Write layouts/NN.json for the approved Book 1 + Book 2 + Guide cluster.

Usage (run from the batch folder):
    python3 make_layout.py <id> --plate plates/NN-v1.png --x0 25 --y0 990 --k 1.0 [--label darkred|gold|ticket-gold|none]
                           [--lang EN] [--label-w 570] [--label-dx 0] [--label-dy 0] [--out-lang en]

The cluster is the one Mirella approved on creative #1 (2026-09-30), on a 2048px canvas:
    Book 1 at (x0, y0), 810k tall.
    Book 2 in front, 318k right and 192k down, 815k tall.
    Guide on its own, 919k right and 517k down, 486k tall.
    Plus centred in the gap between Book 2 and the Guide, level with the Guide's middle.
    Offer label in the notch right of Book 1's top: 618k right, 110k down, 570k wide.
k scales the whole cluster. At k = 1 it is 1187px wide and 1007px tall.
Creatives whose original has no offer label get --label none and --guide-scale 1.2, so the Guide fills the notch.
Pick x0, y0 and k so the cluster fills the space the original cluster filled and clears the badge and any face.
"""
import argparse
import json
import os

ap = argparse.ArgumentParser()
ap.add_argument("id", type=int)
ap.add_argument("--plate", required=True)
ap.add_argument("--x0", type=float, required=True)
ap.add_argument("--y0", type=float, required=True)
ap.add_argument("--k", type=float, default=1.0)
ap.add_argument("--label", default="darkred")
ap.add_argument("--label-w", type=float)
ap.add_argument("--label-dx", type=float, default=0)
ap.add_argument("--label-dy", type=float, default=0)
ap.add_argument("--guide-scale", type=float, default=1.0, help="grow the Guide (keeps its baseline); use about 1.2 when there is no label, to fill the notch")
ap.add_argument("--lang", default="EN")
ap.add_argument("--assets", default="../../../../Brand/Product Images")
a = ap.parse_args()

k, x0, y0 = a.k, a.x0, a.y0
r = round
items = [
    {"id": "b1", "file": "book1-bestseller-badge.png", "x": r(x0), "y": r(y0), "h": r(810 * k)},
    {"id": "b2", "file": "book2-new-badge.png", "x": r(x0 + 318 * k), "y": r(y0 + 192 * k), "h": r(815 * k)},
    {"id": "g", "file": "guide.png", "x": r(x0 + 919 * k), "y": r(y0 + (517 + 486 * (1 - a.guide_scale)) * k), "h": r(486 * k * a.guide_scale)},
    {"id": "plus", "file": "../plus-red-gold.png", "h": r(74 * k), "between": ["b2", "g"], "cy_of": "g"},
]
if a.label != "none":
    items.append({"id": "label", "file": f"labels/new-offer-{a.label}.png",
                  "w": r(a.label_w or 570 * k),
                  "x": r(x0 + 618 * k + a.label_dx), "y": r(y0 + 110 * k + a.label_dy)})

nn = f"{a.id:02d}"
layout = {"plate": "../" + a.plate, "out": f"../final/{nn}-{a.lang.lower()}.png", "size": 2048,
          "assets": f"{a.assets}/{a.lang}", "items": items}
os.makedirs("layouts", exist_ok=True)
with open(f"layouts/{nn}.json", "w", encoding="utf-8") as f:
    json.dump(layout, f, indent=2)
print(f"layouts/{nn}.json  cluster x {r(x0)}-{r(x0 + 1187 * k)}, y {r(y0)}-{r(y0 + 1007 * k)}")
