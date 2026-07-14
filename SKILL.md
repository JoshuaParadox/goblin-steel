---
name: goblin-steel
description: >-
  A portable, pipe-agnostic feedback-forging
  discipline for keeping a body of rules, heuristics, or skills alive and
  improving through feedback. Hand it to any shared skill library and it
  maintains that library like a sourdough starter you feed: propose a base
  rule, act, capture the signal, fork the rule to fit the local kitchen, and
  never throw the mother out. Use goblin steel WHENEVER you build, maintain,
  evolve, port, or seed a skill library, ruleset, playbook, or methodology;
  when a skill or agent must adapt itself to a new environment (a Cowork
  plugin, an MCP-backed store, a GitHub repo, or a human's notebook);
  when a decision-rule must keep improving as conditions change; or when
  someone says 'use goblin steel', 'feed the starter', 'fork this rule', or
  'propose then iterate'. Reach for it even when 'goblin steel' is unspoken
  but the task is really a living, self-improving ruleset that must survive
  changing conditions and different delivery pipes.
---

# Goblin Steel

Goblin steel is a focused feedback-forging discipline, wrapped in a skill so it can run anywhere. It does one thing — keep a body of rules alive and improving through feedback — and it is built to be genuinely useful on its own.

## The one string

> A rule is not a fact to be stored. It is a living culture to be fed. You keep it alive with feedback, you grow it by forking, and you never throw the mother out.

Everything below is a consequence of that sentence. If you only remember one thing, remember that a rule is a culture, not a carving.

## Two metaphors, one principle

**Goblin steel (the material).** Forged from what is at hand, reforged rather than remelted, stronger by accretion, antifragile. This is the *builder's* view — how you improve a system without ever tearing it down to bare metal.

**Sourdough starter (the culture).** Alive, fed rather than finished, it adapts to your kitchen and is passed on by the spoonful. This is the *public* view — what a person receives when they download this skill. The moment it lands in a new kitchen it begins to diverge: adapting to your flour (your domain), your climate (your environment and its delivery pipe), and your hands (your judgment). Your job is to feed it, keep the mother, and pass a spoon on. Every kitchen's bread tastes different; the culture is shared.

They are the same principle in two materials — one you build with, one you eat. Hold both.

**Why this already works elsewhere.** Git runs half of this discipline for source code: append-only history, branches, nothing truly lost, merge as reconciliation. Goblin steel generalizes that discipline from *code* to *rules and heuristics*, and makes it substrate-agnostic so it can ride whatever storage a given environment offers instead of requiring one.

## The five forge laws

1. **Feedback is the forge.** Nothing improves without a closed loop. Every rule you apply must return a signal, and the signal must be *captured*, not merely felt. An uncaptured outcome never happened. This is why the skill keeps a ledger rather than trusting memory.

2. **Feed, don't finish.** Like a starter, the methodology is never "done." A rule you stop feeding goes stale — not wrong, just unfed, and untrustworthy until fed again. Treat "finished" as a smell, not a state.

3. **Expand, never delete.** When a rule stops earning its place, you supersede it; you do not remove it. The lineage is the asset: it lets you backtrack, compare, and resurrect. History is the alloy that makes the current rule strong.

4. **Fork the rule, don't overwrite it.** A change is a new branch carrying a reason and a condition ("in kitchen X, use variant B"). The trunk stays; variants coexist; the environment selects which applies. Overwriting destroys the very variation that feedback needs to select from.

5. **The pipe is not the point.** The methodology is portable. MCP, a Cowork plugin, a GitHub repo, a human's notebook — these are delivery pipes, kitchens, not the culture itself. When a pipe gets in the way, you fork an *adapter* to fit it; you never bend the four laws above to suit a vendor. Independence from the pipe is what lets the same discipline run everywhere.

## The loop

Every use of goblin steel is one or more turns of the same wheel:

**Propose → Act → Sense → Fork → Feed → (repeat)**

- **Propose** the current best rule (the trunk) as a *starting fork*, never as gospel.
- **Act** — apply it in the real environment.
- **Sense** — capture the outcome as a signal (positive, negative, mixed). If you did not capture it, go back.
- **Fork** — if the signal says the rule should change, branch a variant with a reason and a condition. If it confirms, raise confidence or promote.
- **Feed** — append everything to the ledger. Expansion never deletion.

## What to do when you are invoked

Pick the mode(s) that fit. Full step-by-step lives in `references/protocol.md`.

- **Seed** — first contact with a new kitchen. Detect the environment and its pipe, choose the right adapter (`references/adapters.md`), create or verify the three ledgers, and bootstrap the founding rules if none exist. Announce that the starter is alive here.
- **Propose** — given a task, surface the relevant trunk rule fast, labeled with its confidence and lineage, explicitly as a starting fork.
- **Iterate** — run the loop against the real environment, adapting the proposal to what the kitchen actually allows (its tools, its constraints), capturing feedback each turn.
- **Maintain** — curate the registry: promote proven variants to trunk, flag stale rules, reconcile divergent forks, keep all ancestry. Never delete; supersede.
- **Propagate** — export a clean spoon of the current culture (founding rules plus proven trunk) as a shareable starter for another kitchen or person. This is the public, hand-it-out act.
- **Contribute / Graft** — the two-way commons. `contribute` ships this kitchen's proven forks back to a public feedback inlet; `graft` receives another kitchen's and enters it as an unproven variant that must earn the trunk locally. This is how forked copies improve each other as a collective — see `references/COMMONS.md`.

## The artifacts you maintain

Goblin steel keeps three append-only ledgers (JSONL — one event per line, you only ever append):

- **`rule-registry`** — the rules themselves, with lineage and status.
- **`feedback-ledger`** — action → outcome → signal → decision.
- **`permutation-log`** — deliberate experiments (what varied, what was held, the result).

These are plain files, so they live anywhere. Where they physically sit is the adapter's job. To read the schemas see `references/ledgers.md`. To write to them without breaking append-only discipline, use the helper — it is the discipline made mechanical (there is no delete command by design):

```
python scripts/forge.py seed            # create/verify the ledgers + founding rules in this kitchen
python scripts/forge.py rule    ...     # append a new rule (a fork)
python scripts/forge.py feedback ...    # log an outcome against a rule
python scripts/forge.py permute ...     # record a managed experiment
python scripts/forge.py show     ...    # list current rules
python scripts/forge.py lineage  <id>   # trace a rule's ancestry
python scripts/forge.py spoon    ...    # export a shareable starter
python scripts/forge.py contribute ...  # package your proven forks for the commons
python scripts/forge.py graft   <file>  # receive another's fork as a variant to test
```

Run `python scripts/forge.py --help` for exact arguments.

## Adapting to the kitchen

The same three ledgers, carried by whatever the pipe offers. Detect the pipe, then fork the matching adapter (details in `references/adapters.md`):

- **Cowork / Claude skill** — ledgers as files in the skill folder or the attached project.
- **MCP-backed store / your own "brain"** — ledgers in the backing store, read/written through MCP tools.
- **GitHub** — ledgers as versioned files; forking rides branches, feedback rides commits/issues, reconciliation rides merges.
- **Human notebook** — ledgers as a markdown file or literal paper. Lowest-tech fallback; the laws still hold.

If a kitchen needs behaviour none of these cover, fork a new adapter. That is the fifth law in action, not an exception to it.

## Deeper references

- `references/methodology.md` — the philosophy in full: the string, the two metaphors, the git lineage, confidence and staleness, reconciliation, and the ethics of passing on a spoon.
- `references/protocol.md` — the operating protocol, mode by mode, as concrete steps.
- `references/adapters.md` — how to detect the pipe and carry the ledgers across each one.
- `references/ledgers.md` — the exact JSONL schemas with worked examples.
- `references/COMMONS.md` — the public commons: how forked copies ship improvements back to each other, and the laws that keep the pool clean.
