#!/usr/bin/env python3
"""Score a reel from a Higgsfield Virality Predictor report.

Usage:
  score.py REPORT.html VIDEO.mp4 --brand "Chef Burger" --name "Sad takeaway" [--version v2]
  score.py --skip "reason" VIDEO.mp4 --brand ... --name ...   (test could not run)

Writes VIDEO.mp4.score.json next to the reel (the delivery hook looks for it),
appends one row to the reel score log in the vault, prints a verdict.
Exit 0 = pass, 2 = below the pass mark, 1 = error.
"""
import argparse, datetime, json, os, re, sys

PASS_OVERALL = 60
PASS_HOOK = 50
VAULT = os.path.expanduser("~/Documents/Obsidian Vault/50 Stack/Reel scores.md")
COAL_VAULT = os.path.expanduser("~/repos/coalandco-vault/Reel scores.md")
COAL_BRANDS = ("coal & co", "coal and co", "castle inn", "tollgate", "bull", "berwick",
               "tea room", "farm shop", "taste of dreams", "coal")
COAL_EXCEPT = ("coal retreats",)

HEADER = """# Reel scores

Every reel made in the stack is tested on Higgsfield's Virality Predictor before delivery.
Pass mark: overall {o}+ and hook {h}+. Scores are a predictive proxy, not a promise.
Add real Instagram numbers (views, follows after 48h) in the last two columns to check the predictor.
Process: [[SOP - Reel test]]

| Date | Brand | Reel | Ver | Overall | Hook | Viral | Sustain | Verdict | File | IG views | IG follows |
|---|---|---|---|---|---|---|---|---|---|---|---|
""".format(o=PASS_OVERALL, h=PASS_HOOK)


def grab(html, key):
    m = re.search(r'"%s"\s*:\s*([-0-9.]+)' % key, html)
    return float(m.group(1)) if m else None


def log_path(brand):
    b = brand.lower()
    if any(x in b for x in COAL_EXCEPT):
        return VAULT
    return COAL_VAULT if any(x in b for x in COAL_BRANDS) else VAULT


def append_row(path, row):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        open(path, "w").write(HEADER)
    with open(path, "a") as f:
        f.write(row + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--brand", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--version", default="v1")
    ap.add_argument("--skip", help="reason the test could not run")
    a = ap.parse_args()

    today = datetime.date.today().isoformat()
    if a.skip:
        video = os.path.abspath(a.paths[-1])
        res = {"skipped": a.skip, "date": today, "brand": a.brand, "name": a.name, "version": a.version}
        json.dump(res, open(video + ".score.json", "w"), indent=2)
        append_row(log_path(a.brand), "| %s | %s | %s | %s | - | - | - | - | SKIPPED: %s | %s | | |"
                   % (today, a.brand, a.name, a.version, a.skip, os.path.basename(video)))
        print("SKIPPED (logged): %s" % a.skip)
        return 0

    if len(a.paths) != 2:
        ap.error("need REPORT.html and VIDEO.mp4")
    report, video = a.paths[0], os.path.abspath(a.paths[1])
    html = open(report, errors="ignore").read()
    s = {k: grab(html, k) for k in ("overall_score", "hook_score", "viral_potential",
                                    "brain_engagement", "sustain", "peak_second")}
    if s["overall_score"] is None or s["hook_score"] is None:
        print("ERROR: no overall_score/hook_score in report %s" % report)
        return 1

    frames = []
    m = re.search(r'"global_scores_by_frame"\s*:\s*\[([^\]]*)\]', html)
    if m:
        frames = [float(x) for x in m.group(1).split(",") if x.strip()]
    weakest = sorted(range(len(frames)), key=lambda i: frames[i])[:3] if frames else []
    # drop-off: first second after the hook window where attention falls >10% below the hook average
    drop = None
    if len(frames) > 3:
        base = sum(frames[:3]) / 3
        drop = next((i for i in range(3, len(frames)) if frames[i] < base * 0.9), None)

    passed = s["overall_score"] >= PASS_OVERALL and s["hook_score"] >= PASS_HOOK
    verdict = "PASS" if passed else "BELOW"
    res = {"date": today, "brand": a.brand, "name": a.name, "version": a.version,
           "verdict": verdict, "pass_mark": {"overall": PASS_OVERALL, "hook": PASS_HOOK},
           "scores": s, "weakest_seconds": weakest, "dropoff_second": drop,
           "frames": frames, "report": os.path.abspath(report)}
    json.dump(res, open(video + ".score.json", "w"), indent=2)

    n = lambda v: "-" if v is None else str(int(round(v)))
    append_row(log_path(a.brand), "| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | | |" % (
        today, a.brand, a.name, a.version, n(s["overall_score"]), n(s["hook_score"]),
        n(s["viral_potential"]), n(s["sustain"]), verdict, os.path.basename(video)))

    print("%s  overall %s/%d  hook %s/%d  viral %s  sustain %s  peak %ss" % (
        verdict, n(s["overall_score"]), PASS_OVERALL, n(s["hook_score"]), PASS_HOOK,
        n(s["viral_potential"]), n(s["sustain"]), n(s["peak_second"])))
    if weakest:
        print("weakest seconds: %s" % ", ".join("%ds" % i for i in sorted(weakest)))
    if drop is not None:
        print("attention drops from %ds" % drop)
    print("logged to %s" % log_path(a.brand))
    return 0 if passed else 2


if __name__ == "__main__":
    sys.exit(main())
