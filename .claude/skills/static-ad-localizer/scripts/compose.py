#!/usr/bin/env python3
"""Paste the real product images, the plus sign and the offer label onto a generated plate.

Usage:
    python3 compose.py layout.json

layout.json:
{
  "plate":  "../plates/01-nbp.png",       # the Higgsfield render (text translated, products and label removed)
  "out":    "../final/01-en.png",
  "size":   2048,                          # optional; plate is resized to size x size if it differs
  "assets": "../../../../Brand/Product Images/EN",   # folder the item files resolve against
  "items": [                               # pasted in order, so later items sit in front
    {"id": "b1", "file": "book1-bestseller-badge.png", "x": 25,  "y": 960,  "h": 900},
    {"id": "b2", "file": "book2-new-badge.png",        "x": 400, "y": 1100, "h": 900},
    {"id": "g",  "file": "guide.png",                  "x": 950, "y": 1530, "h": 460},
    {"id": "plus",  "file": "../plus-red-gold.png", "h": 84, "between": ["b2", "g"], "cy_of": "g"},
    {"id": "label", "file": "labels/new-offer-darkred.png", "w": 500, "center_over": ["g"], "gap": 30}
  ]
}

Size: give "h" (height of the visible pixels after scaling) or "w".
Position, one of:
  "x", "y"                     top-left corner of the visible pixels (transparent margin is trimmed first)
  "cx", "cy"                   centre point
  "between": [idA, idB]        horizontally centred in the gap between the solid edges of two placed items,
                               measured on the rows this item covers. Needs "cy", "y" or "cy_of": id.
  "center_over": [ids]         horizontally centred on the solid pixels of the listed items and placed
                               "gap" pixels above their top edge. "center_under" works the same, below.
"dx"/"dy" nudge any computed position. All numbers are output pixels. Paths are relative to the layout file.
Solid = alpha above 200, so soft drop shadows don't count when centring.
The script never redraws a product: it only trims, scales (Lanczos) and alpha-pastes.
"""
import json
import os
import sys

from PIL import Image

SOLID = 200


def load_trimmed(path):
    im = Image.open(path).convert("RGBA")
    # ignore near-invisible haze when trimming
    bbox = im.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    return im.crop(bbox) if bbox else im


def solid_bbox(mask):
    return mask.point(lambda v: 255 if v > SOLID else 0).getbbox()


def main(layout_path):
    base = os.path.dirname(os.path.abspath(layout_path))
    with open(layout_path, encoding="utf-8") as f:
        layout = json.load(f)

    def resolve(p, root=base):
        return p if os.path.isabs(p) else os.path.normpath(os.path.join(root, p))

    plate = Image.open(resolve(layout["plate"])).convert("RGBA")
    size = layout.get("size")
    if size and plate.size != (size, size):
        plate = plate.resize((size, size), Image.LANCZOS)
    W, H = plate.size

    assets_root = resolve(layout.get("assets", "."))
    placed = {}  # id -> full-canvas alpha mask of that item
    report = []

    def union_bbox(ids):
        boxes = [solid_bbox(placed[i]) for i in ids]
        return (min(b[0] for b in boxes), min(b[1] for b in boxes),
                max(b[2] for b in boxes), max(b[3] for b in boxes))

    for item in layout["items"]:
        im = load_trimmed(resolve(item["file"], assets_root))
        scale = item["h"] / im.height if "h" in item else item["w"] / im.width
        w, h = round(im.width * scale), round(im.height * scale)
        im = im.resize((w, h), Image.LANCZOS)

        # vertical position first; horizontal rules may depend on it
        if "y" in item:
            y = item["y"]
        elif "cy" in item:
            y = item["cy"] - h / 2
        elif "cy_of" in item:
            b = solid_bbox(placed[item["cy_of"]])
            y = (b[1] + b[3]) / 2 - h / 2
        elif "center_over" in item:
            y = union_bbox(item["center_over"])[1] - item.get("gap", 20) - h
        elif "center_under" in item:
            y = union_bbox(item["center_under"])[3] + item.get("gap", 20)
        else:
            raise SystemExit(f'{item["file"]}: no vertical position given')
        y = round(y + item.get("dy", 0))

        if "x" in item:
            x = item["x"]
        elif "cx" in item:
            x = item["cx"] - w / 2
        elif "between" in item:
            a, b = (placed[i] for i in item["between"])
            rows = range(max(0, y), min(H, y + h))
            rights, lefts = [], []
            for r in rows:
                ra = a.crop((0, r, W, r + 1)).point(lambda v: 255 if v > SOLID else 0).getbbox()
                rb = b.crop((0, r, W, r + 1)).point(lambda v: 255 if v > SOLID else 0).getbbox()
                if ra:
                    rights.append(ra[2])
                if rb:
                    lefts.append(rb[0])
            if not rights or not lefts:
                raise SystemExit(f'{item["file"]}: "between" items do not share these rows')
            rights.sort(), lefts.sort()
            edge_a, edge_b = rights[len(rights) // 2], lefts[len(lefts) // 2]
            x = (edge_a + edge_b) / 2 - w / 2
            report.append(f'  gap between {item["between"][0]} and {item["between"][1]}: {edge_b - edge_a}px, item {w}px')
        elif "center_over" in item or "center_under" in item:
            b = union_bbox(item.get("center_over") or item["center_under"])
            x = (b[0] + b[2]) / 2 - w / 2
        else:
            raise SystemExit(f'{item["file"]}: no horizontal position given')
        x = round(x + item.get("dx", 0))

        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        layer.paste(im, (x, y), im)
        plate = Image.alpha_composite(plate, layer)
        if "id" in item:
            placed[item["id"]] = layer.getchannel("A")

        report.insert(len(report), f'{item.get("id", item["file"])}: x {x}-{x + w}, y {y}-{y + h}, scale {scale:.2f}')
        if scale > 1.0:
            report.append(f'  note: scaled UP ({scale:.2f}x); ask for a larger source image')
        if x < 0 or y < 0 or x + w > W or y + h > H:
            report.append("  WARNING: runs off the canvas")

    out = resolve(layout["out"])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    plate.convert("RGB").save(out, quality=95)
    print(f"saved {out} {plate.size}")
    print("\n".join(report))


if __name__ == "__main__":
    main(sys.argv[1])
