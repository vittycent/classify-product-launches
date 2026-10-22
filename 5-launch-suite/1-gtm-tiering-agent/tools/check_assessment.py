"""Check tiering files against the handoff (../handoff.md).

    python3 check_assessment.py <file or folder> [...]

Checks every tiering-*.md under the paths given: the header has every field, each value is
allowed, and the tier follows from the total, the borderline rule, approved overrides and the
revenue gate. Handoff version 2 adds ship_date and added_from_higher_tier; version 1 files, such
as the published runs, are still checked as version 1. Weekly lists (tiering-YYYY-Www.md) get a
header check, and from version 2 every row: tier, total and ship date on the routine list, a ship
date and an assessment link on the full path, a known trigger on every rescore. Prints one line
per file and exits 1 if any file fails. Standard library only.
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
SHIPS = re.compile(r"^(\d{4}-\d\d-\d\d|not dated)( \(roadmap: [^)]+\))?$")
TRIGGERS = ("scope", "date", "results", "maturity", "deal", "market date", "market_date", "competitor", "evidence")


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
    if h["handoff"] != "tiering-assessment" or h["handoff_version"] not in ("1", "2"):
        errs.append("handoff or version")
    if h["handoff_version"] == "2":
        missing2 = [f for f in ("ship_date", "added_from_higher_tier") if f not in h]
        if missing2:
            return errs + ["missing: " + ", ".join(missing2)]
        if h["ship_date"] != "not dated" and not DATE.match(h["ship_date"]):
            errs.append("ship_date")
        added = h["added_from_higher_tier"]
        if added != "none":
            if not isinstance(added, list) or not added:
                errs.append("added_from_higher_tier")
            else:
                for a in added:
                    ft = a.get("from_tier", "")
                    if not a.get("asset") or not a.get("reason") or not ft.isdigit():
                        errs.append("an added asset needs asset, from_tier and reason")
                    elif h["tier"].isdigit() and not 1 <= int(ft) < int(h["tier"]):
                        errs.append("an added asset must come from a higher tier's row")
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


def table_rows(text, number):
    """The rows of section <number>'s table that start with a release id, as lists of cells."""
    m = re.search(r"^## %d\..*?(?=^## \d+\.|\Z)" % number, text, re.M | re.S)
    if not m:
        return None
    rows = []
    for line in m.group(0).splitlines():
        if re.match(r"^\|\s*RL-\d{3}\s*\|", line):
            rows.append([c.strip().replace("**", "") for c in line.strip().strip("|").split("|")])
    return rows


def check_weekly(h, text=""):
    missing = [f for f in WEEKLY if f not in h]
    if missing:
        return ["missing: " + ", ".join(missing)]
    errs = []
    if h["handoff"] != "tiering-weekly" or h["handoff_version"] not in ("1", "2") or not re.match(r"^\d{4}-W\d\d$", h["week"]) or not DATE.match(h["run"]):
        errs.append("handoff, version, week or run")
    if h["status"] not in ("draft", "approved"):
        errs.append("status")
    if h["status"] == "approved" and not (h["approved_by"] and DATE.match(h["approved_on"])):
        errs.append("approved without approved_by and approved_on")
    if h["handoff_version"] != "2":
        return errs
    routine, full, rescores = table_rows(text, 1), table_rows(text, 2), table_rows(text, 3)
    if routine is None or full is None or rescores is None:
        return errs + ["sections 1 to 3 are not all there"]
    full_ids = {r[0] for r in full}
    for r in routine:
        if len(r) != 7:
            errs.append(f"{r[0]}: the routine row needs 7 cells")
            continue
        rid, _, tier, total, ships, why, move = r
        try:
            t, tot = int(tier), float(total)
        except ValueError:
            errs.append(f"{rid}: tier or total not a number")
            continue
        if not tot < 47 or (tot * 2) != int(tot * 2):
            errs.append(f"{rid}: a routine total must be under 47, in half points")
        want = 4 if tot < 30 or tot <= 33 else 3
        if t != want:
            errs.append(f"{rid}: tier {t} does not follow from total {tot:g} on the routine list")
        if 30 <= tot <= 33 and "borderline" not in why.lower():
            errs.append(f"{rid}: within 3 points above the Tier 3 line, so it must say borderline")
        if not SHIPS.match(ships):
            errs.append(f"{rid}: ship date")
        if move.lower().startswith("yes") and rid not in full_ids:
            errs.append(f"{rid}: moved to the full path but not listed there")
    for r in full:
        if len(r) != 5:
            errs.append(f"{r[0]}: the full path row needs 5 cells")
            continue
        rid, _, ships, _, assessment = r
        if not SHIPS.match(ships):
            errs.append(f"{rid}: ship date")
        if not (re.search(r"\(([^)]*tiering-\d{4}-\d\d-\d\d\.md)\)", assessment) or re.fullmatch(r"to come(, since \d{4}-W\d\d)?", assessment, re.I)):
            errs.append(f"{rid}: the assessment must be a link or 'to come'")
    for r in rescores:
        if len(r) != 5:
            errs.append(f"{r[0]}: the rescore row needs 5 cells")
            continue
        if not any(r[1].lower().startswith(t) for t in TRIGGERS):
            errs.append(f"{r[0]}: unknown trigger")
        if not SHIPS.match(r[3]):
            errs.append(f"{r[0]}: ship date")
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
            text = open(f, encoding="utf-8").read()
            h = header(text)
            errs = check_weekly(h, text) if h.get("handoff") == "tiering-weekly" else check_assessment(h)
        except Exception as e:  # noqa: BLE001, a broken header is a failure, not a crash
            errs = [f"unreadable header: {e}"]
        bad += bool(errs)
        print(("FAIL " if errs else "ok   ") + f + ("" if not errs else "  | " + "; ".join(errs)))
    print(f"{len(files)} files, {bad} fail")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or ["."]))
