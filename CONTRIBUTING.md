# Contributing to goblin steel

goblin steel grows the way it teaches: by feedback, by forking, never by overwriting. Contributing is the `contribute → graft` loop, run over GitHub.

> **The inlet is shut for now. Please don't open issues or pull requests.**
>
> Everything below describes how contribution works when the commons is open.
> It is not open. I am not ready to administer a commons with the care and
> attention it deserves, and I would rather say that plainly than run an inlet
> that quietly ignores what people send it.
>
> None of the discipline is blocked by this. Fork, feed, and pass on a spoon all
> work today, in your own kitchen, with no inlet at all. The only step waiting
> is the one where your proven forks come back here.
>
> If you have forks worth contributing, keep the bundle. `python
> scripts/forge.py contribute --out my-forks.json --handle you` produces it, and
> it stays valid — the format will not change out from under you. When the
> inlet opens, this file will say so.

## The short version

1. **Fork** this repository — your own copy to feed.
2. **Feed** it in your kitchen. As real use forks your rules, `scripts/forge.py` keeps the append-only ledgers.
3. **Package** your proven forks: `python scripts/forge.py contribute --out my-forks.json --handle you`
4. **Keep the bundle.** This is the step that is shut. When the inlet opens, this is where you open a pull request using the template and paste or attach it. Until then, hold what you have packaged — nothing is lost by waiting.

## What makes a good contribution

A rule the pool can actually judge carries four things:

- **The rule** — imperative and concrete.
- **The why** — the reason it exists.
- **The condition** — the kitchen it applies to (`*` if always).
- **The evidence** — the feedback behind it (what you did, what happened). Claims without evidence are welcome, but they stay low-confidence until the network feeds them.

## What happens to your contribution (once the inlet is open)

It is **grafted as an unproven variant**, whatever status it held in your kitchen — it must earn the trunk here, on this pool's feedback. Nothing you send overwrites an existing rule, and nothing is ever deleted. Weak forks aren't rejected; they simply don't get promoted until the evidence lifts them.

See `references/COMMONS.md` for the full protocol and the laws of the pool.

## The one rule of the commons

Keep the reasons attached, always — what you ship out carries its *why*, so the next kitchen can disagree with it intelligently.
