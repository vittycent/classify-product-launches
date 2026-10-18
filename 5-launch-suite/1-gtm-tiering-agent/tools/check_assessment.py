"""Check tiering files against the handoff (../handoff.md).

    python3 check_assessment.py <file or folder> [...]

Checks every tiering-*.md under the paths given: the header has every field, each value is
allowed, and the tier follows from the total, the borderline rule, approved overrides and the
revenue gate. Weekly lists (tiering-YYYY-Www.md) get a header check. Prints one line per file
and exits 1 if any file fails. Standard library only.
"""
import os
import re
import sys

JOBS = {1: "Tell the market", 2: "Tell customers and sales", 3: "Tell the customers it serves", 4: "Log it"}
FIELDS = ["handoff", "handoff_version", "release_id", "title", "assessed", "rubric_version", "path", "tier",
          "tier_job", "total", "borderline", "provisional", "provisional_reason", "gates", "overrides",
          "competitor_flag", "status", "decided_by", "decided_on", "leadership_signoff",
          "previous_assessment", "rescore_trigger"]
WEEKLY = ["handoff", "handoff_version", "week", "run", "rubric_version", "status", "approved_by", "approved_on"]
DATE = re.compile(r"^\d{4}-\d\d-\d\d$")


def scalar(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def header(text):
    """Parse the small YAML subset the handoff uses: scalars, one nested map, one list of maps."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        raise ValueError("no header")
    end = lines.index("---", 1)
    out, key, item = {}, None, None
    for line in lines[1:end]:
        if not line.strip():
            continue
        if not line.startswith(" "):
            k, _, v = line.partition(":")
            key, item = k.strip(), None
            out[key] = scalar(v) if v.strip() else {}
        elif line.strip().startswith("- "):
            item = {}
            if not isinstance(out[key], list):
                out[key] = []
            out[key].append(item)
            k, _, v = line.strip()[2:].partition(":")
            item[k.strip()] = scalar(v)
        else:
            k, _, v = line.strip().partition(":")
            (item if item is not None else out[key])[k.strip()] = scalar(v)
    return out


def tier_from(total, borderline, overrides, revenue):
    """The tiers the header allows: the line's tier; when borderline, either tier on that line
    (one lower just above a line, one higher just below it, with the reason written down, as
    rubric section 7 says); one higher per approved override; never above Tier 3 when the
    revenue gate failed."""
    line = 1 if total >= 70 else 2 if total >= 50 else 3 if total >= 30 else 4
    allowed = {line}
    if borderline and any(0 <= total - l <= 3 for l in (30, 50, 70)):
        allowed.add(min(line + 1, 4))
    if borderline and any(0 < l - total <= 3 for l in (30, 50, 70)):
        allowed.add(max(line - 1, 1))
    ups = sum(1 for o in overrides if o.get("status") == "approved")
    allowed = {max(1, t - ups) for t in allowed}
    if revenue == "failed":
        allowed = {max(3, t) for t in allowed}
    return allowed


def check_assessment(h):
    errs = []
    missing = [f for f in FIELDS if f not in h]
    if missing:
        return ["missing: " + ", ".join(missing)]
    if h["handoff"] != "tiering-assessment" or h["handoff_version"] != "1":
        errs.append("handoff or version")
    if not re.match(r"^RL-\d{3}$", h["release_id"]):
        errs.append("release_id")
    if not DATE.match(h["assessed"]):
        errs.append("assessed")
    if not re.match(r"^v\d+(\.\d+)?$", h["rubric_version"]):
        errs.append("rubric_version")
    if h["path"] not in ("full", "routine"):
        errs.append("path")
    try:
        tier, total = int(h["tier"]), float(h["total"])
    except ValueError:
        return errs + ["tier or total not a number"]
    if tier not in JOBS or h["tier_job"] != JOBS[tier]:
        errs.append("tier_job does not match tier")
    if not 0 <= total <= 100 or (total * 2) != int(total * 2):
        errs.append("total")
    for f in ("borderline", "provisional", "competitor_flag"):
        if h[f] not in ("true", "false"):
            errs.append(f)
    if h["provisional"] == "true" and not h["provisional_reason"]:
        errs.append("provisional without a reason")
    g = h["gates"] if isinstance(h["gates"], dict) else {}
    if g.get("revenue") not in ("passed", "failed") or not g.get("maturity", "").isdigit() or not 0 <= int(g.get("maturity", "0")) <= 10:
        errs.append("gates")
    elif (int(g["maturity"]) < 5) != (h["provisional"] == "true"):
        errs.append("provisional does not match maturity")
    ov = h["overrides"]
    if ov == "none":
        ov = []
    if not isinstance(ov, list):
        errs.append("overrides")
        ov = []
    for o in ov:
        if o.get("type") not in ("big_deal", "market_date") or o.get("status") not in ("proposed", "approved", "not approved", "does not fire"):
            errs.append("an override's type or status")
    if h["status"] not in ("draft", "approved"):
        errs.append("status")
    if h["status"] == "approved" and not (h["decided_by"] and DATE.match(h["decided_on"])):
        errs.append("approved without decided_by and decided_on")
    if h["leadership_signoff"] not in ("not needed", "pending", "given"):
        errs.append("leadership_signoff")
    if h["status"] == "approved" and tier == 1 and h["leadership_signoff"] != "given":
        errs.append("approved Tier 1 without leadership sign off")
    if h["previous_assessment"] != "none" and not DATE.match(h["previous_assessment"]):
        errs.append("previous_assessment")
    if h["rescore_trigger"] not in ("none", "scope", "date", "results", "maturity", "deal", "market_date", "competitor"):
        errs.append("rescore_trigger")
    if not errs and tier not in tier_from(total, h["borderline"] == "true", ov, g["revenue"]):
        errs.append(f"tier {tier} does not follow from total {total:g}, the borderline rule, approved overrides and the revenue gate")
    return errs


def check_weekly(h):
    missing = [f for f in WEEKLY if f not in h]
    if missing:
        return ["missing: " + ", ".join(missing)]
    errs = []
    if h["handoff"] != "tiering-weekly" or not re.match(r"^\d{4}-W\d\d$", h["week"]) or not DATE.match(h["run"]):
        errs.append("handoff, week or run")
    if h["status"] not in ("draft", "approved"):
        errs.append("status")
    return errs


def main(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            for root, _, names in os.walk(p):
                files += [os.path.join(root, n) for n in names if n.startswith("tiering-") and n.endswith(".md")]
        else:
            files.append(p)
    bad = 0
    for f in sorted(files):
        try:
            h = header(open(f, encoding="utf-8").read())
            errs = check_weekly(h) if h.get("handoff") == "tiering-weekly" else check_assessment(h)
        except Exception as e:  # noqa: BLE001, a broken header is a failure, not a crash
            errs = [f"unreadable header: {e}"]
        bad += bool(errs)
        print(("FAIL " if errs else "ok   ") + f + ("" if not errs else "  | " + "; ".join(errs)))
    print(f"{len(files)} files, {bad} fail")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or ["."]))
