# Contributing to goblin steel

goblin steel grows the way it teaches: by feedback, by forking, never by overwriting. Contributing is the `contribute → graft` loop, run over GitHub.

## The short version

1. **Fork** this repository — your own copy to feed.
2. **Feed** it in your kitchen. As real use forks your rules, `scripts/forge.py` keeps the append-only ledgers.
3. **Package** your proven forks: `python scripts/forge.py contribute --out my-forks.json --handle you`
4. **Open a pull request** using the template, and paste or attach your contribution bundle.

## What makes a good contribution

A rule the pool can actually judge carries four things:

- **The rule** — imperative and concrete.
- **The why** — the reason it exists.
- **The condition** — the kitchen it applies to (`*` if always).
- **The evidence** — the feedback behind it (what you did, what happened). Claims without evidence are welcome, but they stay low-confidence until the network feeds them.

## What happens to your contribution

It is **grafted as an unproven variant**, whatever status it held in your kitchen — it must earn the trunk here, on this pool's feedback. Nothing you send overwrites an existing rule, and nothing is ever deleted. Weak forks aren't rejected; they simply don't get promoted until the evidence lifts them.

See `references/COMMONS.md` for the full protocol and the laws of the pool.

## The one rule of the commons

Keep the reasons attached, always — what you ship out carries its *why*, so the next kitchen can disagree with it intelligently.
