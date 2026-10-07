# The Commons — goblin steel's public feedback inlet

A spoon of starter goes out; something should be able to come back. The commons is the public culture bank where forked copies of goblin steel ship their improvements to each other — a collective that is, by design, under no single party's control.

This turns propagation from one-way (hand out a spoon) into a loop (hand out a spoon, receive proven forks back). The loop is the whole point: a culture that only ever leaves home never learns from the kitchens it lands in.

> **Status: specified, not yet open.** What follows describes the commons in
> full, as designed. The canonical inlet is not accepting contributions, because
> a pool with no steward is a pool that rots — the reason is in `README.md`.
> The specification is published anyway, so the design can be read, argued with,
> and run inside any fork before the inlet exists. R-0003 applies to the commons
> as much as to a rule: supersede, never delete. Something not yet open is
> marked, not hidden.

## The two-way inlet

Two commands carry the traffic; both obey the forge laws.

**Contribute — ship a fork out.**
```
python scripts/forge.py contribute --out my-forks.json --handle you
```
This packages the rules *your* kitchen forked and proved — never the mother culture, which already ships with every copy — together with the feedback behind them, so the receiver can judge them rather than take them on faith. Your kitchen is untouched; contributing copies.

**Graft — take a fork in.**
```
python scripts/forge.py graft their-forks.json
```
This merges an incoming contribution into your registry as **low-confidence variants**, whatever status they held in their home kitchen. A graft does not arrive as truth. It arrives as a proposal that must earn the trunk *here*, on your feedback. Nothing is overwritten, and the sender's evidence is not laundered in as your own.

## The laws of the pool

The commons is just goblin steel applied to a crowd, so the five forge laws govern it unchanged:

1. **A contribution is another kitchen's attempt, not a fact.** It enters as a variant and earns trust locally.
2. **It carries its reasons and its evidence.** A rule with no *why* and no feedback behind it is a rumour; the pool can hold it, but it stays unproven.
3. **Nothing is deleted.** Weak forks are not removed; they simply never get promoted. The pool grows by accretion.
4. **Forks coexist.** Two contributions can disagree and both live — conditioned on the kitchens they suit — until feedback sorts them.
5. **The pipe is not the point.** The inlet can be a git repository, an issue tracker, a form, a webhook. The bundle format is plain JSON; carry it however you like.

## The pool's immune system

An open inlet invites the obvious worry: won't it fill with noise? The discipline *is* the immunity. Every contribution lands as an unproven variant, so nothing a stranger sends can silently become canon — it has to survive contact with real kitchens and real feedback before it promotes. Claims travel with their evidence, so a confident assertion with nothing behind it stays exactly as trusted as it deserves. And because nothing is ever deleted, there is no destructive act for a bad actor to perform: the worst they can do is add a variant that never earns a promotion. Pollution doesn't accumulate; it just fails to rise.

## Running the inlet on git

Git is the natural home, because git already *is* this discipline for code — fork, branch, never truly delete, merge as reconciliation. Mapped onto the commons:

- **Fork** the canonical repository → your own copy to feed.
- **Contribute** a bundle → open a pull request or an issue against the canonical repo. *(Shut for now.)*
- **Reconcile** → a steward (or an automated pass) grafts accepted bundles as variants; the repo's history keeps every submission, promoted or not.
- **Promote** → the network's feedback, gathered over time, is what moves a variant to trunk in the canonical mother.

No git? The same loop runs over any inlet that can receive a JSON file. The laws don't depend on the pipe.

## The ethic still scales

Keep your mother — contributing and grafting both copy; neither depletes anyone's source. And keep the reasons attached, always: what you ship out, and what you take in, carries its *why* so the next kitchen can disagree with it intelligently. A commons you cannot argue with is not a commons; it is a product with extra contributors.

## License

goblin steel is offered under permissive terms — MIT for the code, CC BY 4.0 for the written methodology — so it can spread as far as it will. Both ask for one thing only: keep the attribution. The names "goblin steel" and "Paradox" are held as trademarks; the license frees the recipe, not the sign over the bakery. See `LICENSE` at the repository root for the full terms.
