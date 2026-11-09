#!/usr/bin/env python3
"""Claude Code hook for the reel test gate.

PostToolUse Bash: after a reel render, remind Claude to run reel-test.
PreToolUse SendUserFile: deny sending a video that has no .score.json next to it.
"""
import json, os, re, sys

VIDEO = re.compile(r"[^\s'\"]+\.(mp4|mov)\b", re.I)


def main():
    try:
        d = json.load(sys.stdin)
    except Exception:
        return 0
    ev = d.get("hook_event_name")
    tool = d.get("tool_name")
    inp = d.get("tool_input") or {}
    cwd = d.get("cwd") or os.getcwd()

    if ev == "PostToolUse" and tool == "Bash":
        cmd = inp.get("command", "")
        if not re.search(r"(^|[;&|(]\s*|\bnpx\s+|\bbunx\s+)remotion\s+render\s+\S", cmd, re.M) or "<<" in cmd:
            return 0
        outs = [m.group(0) for m in VIDEO.finditer(cmd)]
        msg = ("Reel rendered%s. Before delivering it to Jack, run the reel-test skill "
               "(Higgsfield Virality Predictor, pass mark 60 overall / 50 hook, one rework round if below)."
               % ((": " + ", ".join(outs)) if outs else ""))
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse",
                                                 "additionalContext": msg}}))
        return 0

    if ev == "PreToolUse" and tool == "SendUserFile":
        missing = []
        for f in inp.get("files") or []:
            if not re.search(r"\.(mp4|mov)$", f, re.I):
                continue
            p = f if os.path.isabs(f) else os.path.join(cwd, f)
            if not os.path.exists(p + ".score.json"):
                missing.append(f)
        if missing:
            reason = ("Reel test gate: no virality score for %s. Run the reel-test skill first "
                      "(or score.py --skip \"reason\" if Higgsfield is down, and tell Jack)."
                      % ", ".join(missing))
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                                     "permissionDecision": "deny",
                                                     "permissionDecisionReason": reason}}))
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
