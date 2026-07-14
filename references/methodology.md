# Goblin Steel — the methodology in full

This is the philosophy behind `SKILL.md`. Read it when you want the *why*, not just the *what* — when you are adapting goblin steel to a strange kitchen, deciding whether to fork or promote, or explaining the discipline to someone who just received a spoon of it.

## Table of contents
1. The one string
2. This is not new
3. Two metaphors, one principle
4. Why git is the proof of concept
5. The five forge laws (with reasons)
6. Confidence, promotion, and staleness
7. Reconciling forks
8. Why a *shared* discipline — dyads and quads
9. The ethics of passing on a spoon

## 1. The one string

> A rule is not a fact to be stored. It is a living culture to be fed. You keep it alive with feedback, you grow it by forking, and you never throw the mother out.

## 2. This is not new

Goblin steel is not a clever invention. It is the codification of a discipline that already works wherever people take memory seriously: never delete, never overwrite, keep the revision history, and let feedback — not opinion — decide what survives. Version control already runs exactly this discipline for source code.

Those two instincts — never delete, never get captured by the pipe — are the third, fourth, and fifth forge laws. Goblin steel just gives them a loop, a ledger, and a name so they can travel from code to rules.

## 3. Two metaphors, one principle

**Goblin steel — the material (builder's view).** Goblin-forged metal is made from what is at hand and reforged rather than remelted. You never return it to bare ore; each pass folds the previous one in, so the history is literally *inside* the blade. It is antifragile: stress and use make it better because each stress becomes a fold. When you improve a ruleset this way you never tear it down to nothing and start over — you fold the new lesson in and keep the strength already earned.

**Sourdough starter — the culture (public view).** A starter is alive. You do not finish it; you feed it. Hand a spoon to someone in another city and within a week it has adapted to their flour, their water, their climate — it is now measurably a different culture, yet unmistakably descended from the same mother. This is what a person receives when they download goblin steel: not a frozen product but a live culture that will diverge in their kitchen. Their flour is their domain; their climate is their environment and its delivery pipe; their hands are their judgment. The bread differs everywhere; the lineage is shared everywhere.

The two are the same principle in two materials — one you build with, one you eat. The material view tells you *how to improve without demolition*. The culture view tells you *how it spreads and adapts*. You need both.

## 4. Why git is the proof of concept

Git already runs this discipline, but only for source code:
- **Append-only history** → expansion never deletion.
- **Branches** → fork the rule, don't overwrite it.
- **Nothing truly deleted** (it lingers in history/reflog) → keep the mother.
- **Merge** → reconcile divergent forks.
- **Blame/log** → the lineage that explains *why* the current state is what it is.

Programmers accept this as obviously correct for code and then abandon it the moment they write down a *rule*, a *heuristic*, or a *playbook* — those get overwritten in place, and the reasoning evaporates. Goblin steel's whole move is to take the git discipline that everyone already trusts for code and apply it to rules, while refusing to depend on git specifically (see the fifth law). Where git is present, ride it. Where it is not, carry the same discipline in whatever the kitchen offers.

## 5. The five forge laws (with reasons)

1. **Feedback is the forge.** Improvement is impossible without a closed loop, and a loop you do not *record* is a loop you cannot learn from twice. Memory is not a ledger; people and models both forget and confabulate. So every applied rule must return a captured signal. If you find yourself improving a rule without a recorded outcome behind it, you are guessing, not forging.

2. **Feed, don't finish.** Treating a methodology as "done" is the failure mode that kills starters — you stop feeding it and it goes flat. A rule that has not been exercised against reality lately is not *wrong*, but it is *unfed*: its confidence should decay until fresh feedback restores it. "Finished" is a smell to investigate, not a state to celebrate.

3. **Expand, never delete.** The temptation is to tidy — to remove the rule that stopped working. Resist it. The superseded rule is the record of *why* the current one exists; delete it and the next person (or the next you) re-learns the lesson the hard way. Supersede, mark, and keep. History is the alloy.

4. **Fork the rule, don't overwrite it.** Overwriting is deletion wearing a disguise, and it destroys the variation that feedback needs in order to select. When a rule must change, branch a variant that carries (a) the reason it exists and (b) the condition under which it applies. Variants coexist; the environment picks. This is how one methodology serves many kitchens without shattering into incompatible copies.

5. **The pipe is not the point.** MCP, a Cowork plugin, a GitHub repo, a notebook — these are how the culture is *delivered*, not what it *is*. Coupling the laws to a particular pipe is how you get locked in and how the discipline dies when the vendor changes. When a pipe resists, fork an *adapter* to fit it; never bend the first four laws to suit a tool. Independence from the pipe is precisely what lets the same starter live in every kitchen.

## 6. Confidence, promotion, and staleness

Each rule carries a **status** and a rough **confidence**:
- **trunk** — the current best rule for its kitchen; what `propose` reaches for first.
- **variant** — a fork under test; promising but not yet proven.
- **superseded** — replaced by a better rule, kept as ancestry. Never deleted.
- **stale** — unfed past a threshold; still present, but flagged as untrustworthy until re-exercised.

Movement between them is driven only by captured feedback:
- Repeated positive signals on a **variant** → **promote** to trunk (the old trunk becomes **superseded**, retaining lineage).
- Repeated negative signals on a **trunk** → **demote**; branch a variant to try instead.
- No signal for a long stretch → mark **stale**. Staleness is a prompt to test, not to delete.

Confidence is deliberately coarse (low / medium / high). Precision here is false comfort; what matters is the *direction* the feedback is pushing.

## 7. Reconciling forks

Because variants coexist, kitchens accumulate divergent forks — the point of the system, not a bug. Periodically (the `maintain` mode) reconcile:
- If two forks apply to genuinely different conditions, keep both; sharpen their conditions so it is obvious which fires when.
- If two forks apply to the *same* condition and one clearly out-signals the other, promote the winner and supersede the loser (keeping it).
- If a fork proven in one kitchen looks useful in another, don't copy it silently — propose it there as a variant and let that kitchen's feedback decide. A rule that earned its place in one climate has not yet earned it in another.

Reconciliation never deletes; it re-labels, re-conditions, and promotes.

## 8. Why a *shared* discipline — dyads and quads

A person paired with their AI is a **dyad** — the working unit this is built for. When several dyads run off one shared library, and eventually **quads** form (the AIs coordinating directly for shared work), a shared discipline is what keeps them coherent. If every dyad's rules drift independently, the library fractures: the same question gets ten incompatible answers and no one can tell which lineage to trust.

Goblin steel is the connective tissue. Every dyad feeds the *same* culture by the *same* laws, so their forks stay legible to one another: a variant one dyad proves carries its reason and condition, so the next can adopt it as a proposal rather than a mystery. That is what lets a shared library be *shared* and still *locally adapted* — coherent lineage, divergent leaves. The difference between a library and a pile.

## 9. The ethics of passing on a spoon

The public act is `propagate`: exporting a clean spoon of the culture for someone else. Two obligations come with it.

First, **give a live culture, not a frozen slab.** The spoon should contain the founding rules and genuinely proven trunk — enough to start feeding immediately — not a museum of every dead variant. The recipient inherits a working starter, then makes it theirs.

First-party lineage stays with it: a rule keeps the reason it exists so the recipient can judge it, override it, and fork it in good conscience. You are handing someone the means to disagree with you intelligently. That is the point. A starter you cannot fork is just a product with extra steps.

And **keep your own mother.** Passing on a spoon never depletes the source. You share by copying a portion, never by giving away the only culture you have. Expansion never deletion applies to generosity too.
