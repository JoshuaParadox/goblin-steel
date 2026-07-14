# goblin steel™

*A small, open discipline for keeping a body of rules — yours, or your team's — alive and improving through feedback. Fork it, feed it, pass it on.*

**Home:** https://viableparadox.com

---

## What it is

> A rule is not a fact to be stored. It's a living culture to be fed. You keep it alive with feedback, you grow it by forking, and you never throw the mother out.

Most of us treat our rules of thumb like carvings in stone — we set them, quietly overwrite them when they stop working, and lose the reasoning. goblin steel treats a rule like a sourdough starter instead: alive, fed, never thrown out. When a rule changes you keep the old one and branch a new one beside it. Nothing is lost, so nothing has to be re-learned the hard way.

It is version control, applied to the rules in your head — and it rides whatever pipe you already use (a Claude skill, a git repo, an MCP-backed store, or a notebook).

## What's in here

```
SKILL.md              the core — the one string, the five laws, the loop, the modes
STARTER.md            start here if you just downloaded a spoon
LICENSE               MIT (code) · CC BY 4.0 (words) · trademark on the name
CONTRIBUTING.md       how to contribute a fork back to the commons
references/
  methodology.md      the why in full
  protocol.md         the operating protocol, mode by mode
  adapters.md         carrying it across pipes
  ledgers.md          the three append-only ledgers
  COMMONS.md          the public two-way feedback inlet
scripts/forge.py      the append-only ledger tool (no delete command, by design)
assets/rule-registry.seed.jsonl   the mother culture (seven founding rules)
```

## Quick start

```
python scripts/forge.py seed        # plant the culture in this kitchen
python scripts/forge.py show        # see the rules you've been handed
python scripts/forge.py rule "Do X when Y" --why "..." --when "Y" --parent R-0002
python scripts/forge.py feedback R-0002 --action "tried X" --outcome "worked" --signal + --decision promote
python scripts/forge.py lineage R-0004   # trace why a rule exists
```

Read `STARTER.md` for the friendly version, or `SKILL.md` for the full discipline.

## The commons

goblin steel is meant to be shared and improved. Fork it, feed it in your own kitchen, and ship your proven forks back — see `CONTRIBUTING.md` and `references/COMMONS.md`. Contributions arrive as unproven variants and earn their place on real feedback; nothing is ever overwritten or deleted.

## License

Code under MIT, written methodology under CC BY 4.0 — both need only attribution. "goblin steel" and "Viable Paradox" are trademarks of Paradox Group Pty Ltd. See `LICENSE`.
