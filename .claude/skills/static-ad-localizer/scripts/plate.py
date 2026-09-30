#!/usr/bin/env python3
"""Generate one plate in Higgsfield and download it.

Usage (run from the batch folder):
    python3 plate.py <id> [--tag v1] [--model nano_banana_pro] [--prompt prompts/NN-plate.txt] [--source source/N.png]

Writes plates/NN-<tag>.json (the job record) and plates/NN-<tag>.png.
Defaults: prompt = prompts/NN-plate.txt, source = source/<id>.png, 1:1, 2K.
"""
import argparse
import json
import subprocess
import sys
import urllib.request


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("id", type=int)
    ap.add_argument("--tag", default="v1")
    ap.add_argument("--model", default="nano_banana_pro")
    ap.add_argument("--prompt")
    ap.add_argument("--source")
    ap.add_argument("--aspect", default="1:1")
    args = ap.parse_args()

    nn = f"{args.id:02d}"
    prompt_file = args.prompt or f"prompts/{nn}-plate.txt"
    source = args.source or f"source/{args.id}.png"
    prompt = open(prompt_file, encoding="utf-8").read()

    cmd = ["higgsfield", "generate", "create", args.model, "--prompt", prompt,
           "--image-references", source, "--aspect_ratio", args.aspect, "--resolution", "2k"]
    if args.model.startswith("gpt_image"):
        cmd += ["--quality", "high"]
    cmd += ["--wait", "--wait-timeout", "15m", "--json"]

    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        sys.exit(f"{nn}: higgsfield failed\n{res.stderr[-800:]}")
    out_json = f"plates/{nn}-{args.tag}.json"
    open(out_json, "w", encoding="utf-8").write(res.stdout)
    job = json.loads(res.stdout)[0]
    if job.get("status") != "completed" or not job.get("result_url"):
        sys.exit(f"{nn}: job {job.get('id')} ended as {job.get('status')}")
    out_png = f"plates/{nn}-{args.tag}.png"
    urllib.request.urlretrieve(job["result_url"], out_png)
    print(f"{nn}: {out_png}  job {job['id']}")


if __name__ == "__main__":
    main()
