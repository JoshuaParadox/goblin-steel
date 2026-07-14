#!/usr/bin/env python3
"""
forge.py — the append-only hands of goblin steel.

This tool is the third and fourth forge laws made mechanical: it only ever
APPENDS to the three ledgers, and it has no delete command by design. To
"change" a rule you fork a conditioned variant; to "remove" one you supersede
it. The old lines stay forever, so the lineage — and the reasoning — survives.

Ledgers (JSONL, one event per line) live in --dir (default: current directory),
so the same tool works in any kitchen: a Cowork skill folder, a git repo, a
synced store, or a plain directory on a laptop.

Subcommands:
  seed       create/verify the three ledgers and plant the mother culture
  rule       append a rule (a fork, or a new trunk)
  feedback   log a captured outcome against a rule
  permute    record a deliberate, managed experiment
  show       list rules (optionally filtered)
  lineage    trace a rule's ancestry back to its founding rule
  spoon      export a shareable starter (founding + trunk) to a new directory
  contribute package this kitchen's proven forks to ship to the commons
  graft      merge an incoming contribution as unproven variants (earn trunk locally)

Run `forge.py <subcommand> --help` for arguments.
"""
import argparse
import json
import os
import shutil
import sys
from datetime import datetime, timezone

LEDGERS = {
    "rule": "rule-registry.jsonl",
    "feedback": "feedback-ledger.jsonl",
    "permutation": "permutation-log.jsonl",
}
PREFIX = {"rule": "R", "feedback": "F", "permutation": "P"}
FOUNDING_IDS = {f"R-{i:04d}" for i in range(1, 8)}  # the mother culture ships with every copy

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SEED_ASSET = os.path.join(SCRIPT_DIR, "..", "assets", "rule-registry.seed.jsonl")

# Fallback mother culture, used only if the seed asset is missing (e.g. the
# script was copied on its own). Kept in sync with assets/rule-registry.seed.jsonl.
EMBEDDED_FOUNDING = [
    {"id": "R-0001", "statement": "Treat every rule as a living culture: feed it with captured feedback, grow it by forking, and never throw the mother out.", "why": "The one string of goblin steel.", "when": "*", "status": "trunk", "parent": None, "confidence": "high"},
    {"id": "R-0002", "statement": "Capture every outcome as a recorded signal before you change a rule.", "why": "Feedback is the forge.", "when": "*", "status": "trunk", "parent": None, "confidence": "high"},
    {"id": "R-0003", "statement": "Supersede, never delete. Keep the full lineage so the reasoning behind a change survives it.", "why": "Keep the lineage so the reasoning behind a change survives it.", "when": "*", "status": "trunk", "parent": None, "confidence": "high"},
    {"id": "R-0004", "statement": "Change a rule by forking a conditioned variant, not by overwriting it in place.", "why": "Overwriting is deletion in disguise.", "when": "*", "status": "trunk", "parent": None, "confidence": "high"},
    {"id": "R-0005", "statement": "Stay loosely coupled to the pipe. To fit a kitchen, fork an adapter — never bend the laws to a vendor.", "why": "The pipe is not the point.", "when": "*", "status": "trunk", "parent": None, "confidence": "high"},
    {"id": "R-0006", "statement": "A rule unfed past its horizon is stale — present but untrusted until re-tested.", "why": "Feed, don't finish.", "when": "*", "status": "trunk", "parent": None, "confidence": "high"},
    {"id": "R-0007", "statement": "When you hand out a spoon, include each rule's reason and keep your own mother.", "why": "Propagation ethics.", "when": "propagating to another kitchen or person", "status": "trunk", "parent": None, "confidence": "high"},
]


def now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def path_for(directory, key):
    return os.path.join(directory, LEDGERS[key])


def read_all(path):
    if not os.path.exists(path):
        return []
    out = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def append(path, obj):
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def next_id(path, key):
    n = len(read_all(path)) + 1
    return f"{PREFIX[key]}-{n:04d}"


def ensure_dir(directory):
    os.makedirs(directory, exist_ok=True)


# ---------------------------------------------------------------- subcommands

def cmd_seed(args):
    ensure_dir(args.dir)
    reg = path_for(args.dir, "rule")
    created = []
    # rule registry: plant the mother culture if absent
    if not os.path.exists(reg) or not read_all(reg):
        if os.path.exists(SEED_ASSET):
            shutil.copyfile(SEED_ASSET, reg)
        else:
            with open(reg, "w", encoding="utf-8") as f:
                for r in EMBEDDED_FOUNDING:
                    r = dict(r, ts=now_iso())
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
        created.append(LEDGERS["rule"])
    # feedback + permutation ledgers start empty; feeding fills them
    for key in ("feedback", "permutation"):
        p = path_for(args.dir, key)
        if not os.path.exists(p):
            open(p, "a", encoding="utf-8").close()
            created.append(LEDGERS[key])
    rules = read_all(reg)
    print(f"Starter is alive in: {os.path.abspath(args.dir)}")
    print(f"  carrying {len(rules)} rule(s); "
          f"{sum(1 for r in rules if r.get('status') == 'trunk')} on the trunk.")
    if created:
        print("  created: " + ", ".join(created))
    else:
        print("  ledgers already present — left untouched.")


def cmd_rule(args):
    reg = path_for(args.dir, "rule")
    if not os.path.exists(reg):
        sys.exit("No registry here yet. Run `forge.py seed` first.")
    status = args.status or ("variant" if args.parent else "trunk")
    confidence = args.confidence or ("low" if args.parent else "medium")
    rule = {
        "id": next_id(reg, "rule"),
        "statement": args.statement,
        "why": args.why,
        "when": args.when,
        "status": status,
        "parent": args.parent,
        "confidence": confidence,
        "ts": now_iso(),
    }
    append(reg, rule)
    kind = f"variant of {args.parent}" if args.parent else "new trunk rule"
    print(f"Forged {rule['id']} ({kind}, {confidence} confidence).")


def cmd_feedback(args):
    reg = path_for(args.dir, "rule")
    fpath = path_for(args.dir, "feedback")
    known = {r["id"] for r in read_all(reg)}
    if args.rule_id not in known:
        sys.exit(f"Unknown rule id {args.rule_id}. Use `forge.py show` to list rules.")
    if args.signal not in ("+", "-", "~"):
        sys.exit("signal must be one of: +  -  ~")
    if args.decision not in ("hold", "fork", "promote", "demote"):
        sys.exit("decision must be one of: hold fork promote demote")
    entry = {
        "id": next_id(fpath, "feedback"),
        "rule_id": args.rule_id,
        "action": args.action,
        "outcome": args.outcome,
        "signal": args.signal,
        "decision": args.decision,
        "ts": now_iso(),
    }
    append(fpath, entry)
    print(f"Fed {entry['id']}: {args.rule_id} {args.signal} -> {args.decision}.")
    if args.decision == "fork":
        print("  Next: forge the variant with `forge.py rule ... --parent "
              f"{args.rule_id}`.")


def cmd_permute(args):
    ppath = path_for(args.dir, "permutation")
    if not os.path.exists(ppath):
        sys.exit("No permutation log here yet. Run `forge.py seed` first.")
    entry = {
        "id": next_id(ppath, "permutation"),
        "hypothesis": args.hypothesis,
        "varied": args.varied,
        "held": args.held,
        "rule_id": args.rule,
        "result": args.result or "",
        "ts": now_iso(),
    }
    append(ppath, entry)
    print(f"Logged experiment {entry['id']} (varied: {args.varied}).")


def cmd_show(args):
    rules = read_all(path_for(args.dir, "rule"))
    if args.status:
        rules = [r for r in rules if r.get("status") == args.status]
    if args.grep:
        g = args.grep.lower()
        rules = [r for r in rules
                 if g in r.get("statement", "").lower() or g in r.get("when", "").lower()]
    if not rules:
        print("No matching rules.")
        return
    for r in rules:
        parent = f"  <-{r['parent']}" if r.get("parent") else ""
        print(f"[{r['id']}] ({r['status']}/{r['confidence']}) "
              f"when={r['when']!r}{parent}")
        print(f"    {r['statement']}")


def cmd_lineage(args):
    rules = {r["id"]: r for r in read_all(path_for(args.dir, "rule"))}
    if args.id not in rules:
        sys.exit(f"Unknown rule id {args.id}.")
    chain = []
    cur = args.id
    seen = set()
    while cur and cur not in seen:
        seen.add(cur)
        r = rules.get(cur)
        if not r:
            break
        chain.append(r)
        cur = r.get("parent")
    print(f"Lineage of {args.id} (newest first):")
    for r in chain:
        print(f"  [{r['id']}] ({r['status']}) {r['statement']}")
        print(f"          why: {r['why']}")


def cmd_spoon(args):
    src = path_for(args.dir, "rule")
    rules = read_all(src)
    if not rules:
        sys.exit("Nothing to share — this kitchen has no rules yet.")
    # A live culture, not a graveyard: founding rules + current trunk, with reasons.
    keep = [r for r in rules if r.get("parent") is None or r.get("status") == "trunk"]
    ensure_dir(args.out)
    out_reg = path_for(args.out, "rule")
    with open(out_reg, "w", encoding="utf-8") as f:
        for r in keep:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    for key in ("feedback", "permutation"):
        open(path_for(args.out, key), "a", encoding="utf-8").close()
    print(f"Spooned {len(keep)} rule(s) into {os.path.abspath(args.out)}.")
    print("  Your mother is untouched. The recipient can feed, fork, and pass on their own spoon.")


def cmd_contribute(args):
    reg = path_for(args.dir, "rule")
    fbp = path_for(args.dir, "feedback")
    if not os.path.exists(reg):
        sys.exit("No registry here yet. Run `forge.py seed` first.")
    local = [r for r in read_all(reg) if r["id"] not in FOUNDING_IDS]
    if not local:
        sys.exit("Nothing to contribute yet — this kitchen carries only the mother culture. "
                 "Feed it and fork a rule first.")
    local_ids = {r["id"] for r in local}
    evidence = [f for f in read_all(fbp) if f.get("rule_id") in local_ids]
    bundle = {
        "goblin_steel_contribution": "1",
        "from": args.handle,
        "rules": local,          # your local forks — never the mother; that ships with every copy
        "evidence": evidence,    # the feedback behind them, so the commons can judge, not just trust
        "ts": now_iso(),
    }
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(bundle, f, ensure_ascii=False, indent=2)
    print(f"Packaged {len(local)} local rule(s) + {len(evidence)} evidence line(s) "
          f"into {os.path.abspath(args.out)}.")
    print("  Ship it to the commons (a pull request, an issue, or the feedback inlet).")
    print("  Your kitchen is untouched — contributing copies, it never depletes the source.")


def cmd_graft(args):
    reg = path_for(args.dir, "rule")
    if not os.path.exists(reg):
        sys.exit("No registry here yet. Run `forge.py seed` first.")
    try:
        with open(args.bundle, encoding="utf-8") as f:
            bundle = json.load(f)
    except (OSError, ValueError) as e:
        sys.exit(f"Cannot read contribution bundle: {e}")
    incoming = bundle.get("rules", [])
    if not incoming:
        sys.exit("That bundle carries no rules.")
    src = bundle.get("from") or "anonymous"
    n = 0
    for r in incoming:
        entry = {
            "id": next_id(reg, "rule"),
            "statement": r.get("statement", ""),
            "why": r.get("why", ""),
            "when": r.get("when", "*"),
            "status": "variant",                  # a graft must earn the trunk here, on its own merits
            "parent": None,
            "grafted_from": f"{src}:{r.get('id', '?')}",
            "confidence": "low",                  # unproven in this kitchen, whatever it was in theirs
            "ts": now_iso(),
        }
        append(reg, entry)
        n += 1
    print(f"Grafted {n} rule(s) from '{src}' as low-confidence variants.")
    print("  Nothing was overwritten, and their evidence was NOT imported as your own —")
    print("  feed them here and let your kitchen's feedback decide what earns the trunk.")


# --------------------------------------------------------------------- parser

def build_parser():
    p = argparse.ArgumentParser(description="The append-only hands of goblin steel.")
    p.add_argument("--dir", default=".", help="Directory holding the ledgers (default: current).")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("seed", help="Create/verify ledgers and plant the mother culture.").set_defaults(func=cmd_seed)

    r = sub.add_parser("rule", help="Append a rule (fork or new trunk).")
    r.add_argument("statement", help="The rule itself, imperative and concrete.")
    r.add_argument("--why", required=True, help="The reason it exists.")
    r.add_argument("--when", default="*", help="Condition/kitchen it applies to (default: *).")
    r.add_argument("--parent", default=None, help="Rule id this is forked from.")
    r.add_argument("--status", default=None, choices=["trunk", "variant", "superseded", "stale"])
    r.add_argument("--confidence", default=None, choices=["low", "medium", "high"])
    r.set_defaults(func=cmd_rule)

    f = sub.add_parser("feedback", help="Log a captured outcome against a rule.")
    f.add_argument("rule_id", help="The rule this outcome bears on.")
    f.add_argument("--action", required=True, help="What was actually done.")
    f.add_argument("--outcome", required=True, help="What actually happened.")
    f.add_argument("--signal", required=True, help="+ confirmed | - contradicted | ~ mixed")
    f.add_argument("--decision", required=True, help="hold | fork | promote | demote")
    f.set_defaults(func=cmd_feedback)

    pm = sub.add_parser("permute", help="Record a deliberate experiment.")
    pm.add_argument("--hypothesis", required=True, help="What you expect to learn.")
    pm.add_argument("--varied", required=True, help="The single thing you changed.")
    pm.add_argument("--held", required=True, help="What you deliberately kept constant.")
    pm.add_argument("--rule", default=None, help="Rule id being probed (optional).")
    pm.add_argument("--result", default=None, help="What it showed (fill in after).")
    pm.set_defaults(func=cmd_permute)

    s = sub.add_parser("show", help="List rules.")
    s.add_argument("--status", default=None, choices=["trunk", "variant", "superseded", "stale"])
    s.add_argument("--grep", default=None, help="Filter by text in statement/when.")
    s.set_defaults(func=cmd_show)

    lg = sub.add_parser("lineage", help="Trace a rule's ancestry.")
    lg.add_argument("id", help="Rule id, e.g. R-0014.")
    lg.set_defaults(func=cmd_lineage)

    sp = sub.add_parser("spoon", help="Export a shareable starter.")
    sp.add_argument("--out", required=True, help="Directory to write the starter into.")
    sp.set_defaults(func=cmd_spoon)

    ct = sub.add_parser("contribute", help="Package this kitchen's proven forks for the commons.")
    ct.add_argument("--out", required=True, help="File to write the contribution bundle to.")
    ct.add_argument("--handle", default="anonymous", help="Your name/handle, for provenance.")
    ct.set_defaults(func=cmd_contribute)

    gf = sub.add_parser("graft", help="Merge an incoming contribution as unproven variants.")
    gf.add_argument("bundle", help="Path to a contribution bundle produced by `contribute`.")
    gf.set_defaults(func=cmd_graft)

    return p


def main():
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
