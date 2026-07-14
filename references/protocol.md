# Goblin Steel — the operating protocol

Concrete steps for each mode. `SKILL.md` names the modes; this file tells you how to run them. You will rarely run one in isolation — a typical session is `seed` once, then loops of `propose → iterate`, with `maintain` and `propagate` as periodic housekeeping.

All writes go through `scripts/forge.py`, which only ever appends. Never hand-edit a ledger to "fix" it; append a superseding entry instead. Editing in place is deletion in disguise and breaks the fourth law.

## Mode: SEED (first contact with a kitchen)

Run this the first time goblin steel meets a new environment, host library, or repo.

1. **Sense the kitchen.** Identify the delivery pipe (see `references/adapters.md` for detection): Cowork/Claude skill, an MCP-backed store, a GitHub repo, or a bare notebook. Identify the host — what skill library, ruleset, or playbook you are being asked to keep alive.
2. **Choose the adapter.** The adapter decides *where the three ledgers physically live* in this kitchen. Fork a new adapter if none fits; do not bend the laws to an existing one.
3. **Create or verify the ledgers.** Run `python scripts/forge.py seed`. This creates `rule-registry.jsonl`, `feedback-ledger.jsonl`, and `permutation-log.jsonl` if absent and writes the founding rules (goblin steel's own meta-rules — it is self-hosting). If they already exist, it leaves them untouched and reports what it found.
4. **Bootstrap host rules, carefully.** If the host library already encodes rules, enter them as **trunk** with a note that they are inherited and unproven-here (medium confidence at most). Do not launder inherited assumptions into certainty.
5. **Announce.** Tell the user the starter is alive in this kitchen, which pipe/adapter it is using, and how many rules it is carrying.

## Mode: PROPOSE (give a base rule fast)

The point is a fast, honest starting point — not a final answer.

1. **Retrieve.** Pull the relevant **trunk** rules from the registry (`forge.py show --status trunk`, filtered to the task). Prefer rules whose condition matches this kitchen.
2. **Present as a starting fork.** State the rule, its rough confidence, and its lineage in one breath: "Current trunk (high confidence, forked twice from R-0007): …". The lineage is not decoration — it tells the user how battle-tested this is.
3. **Flag staleness.** If the best matching rule is **stale**, say so and treat the proposal as a hypothesis to be re-tested, not relied upon.
4. **Hand off to iterate.** A proposal is the *start* of the loop. Do not stop here unless the user only wanted the current position.

## Mode: ITERATE (run the loop against reality)

This is Propose → Act → Sense → Fork → Feed, turned as many times as the task needs.

1. **Act.** Apply the proposed rule in the real environment, within what this kitchen actually permits (its tools, its permissions). Adapt the *execution* to the pipe; keep the *rule* intact.
2. **Sense.** Capture the outcome as a signal: positive (`+`), negative (`-`), or mixed (`~`). Be specific about what actually happened — the signal is only as useful as it is concrete.
3. **Decide.** Based on the signal:
   - Confirms the rule → `hold` (and, over repeats, `promote`).
   - Contradicts it, but the rule is close → `fork` a variant carrying the reason and the new condition.
   - Contradicts it broadly → `demote` the trunk and fork an alternative to try.
4. **Feed.** Record it: `forge.py feedback <rule-id> --action "…" --outcome "…" --signal + --decision fork`. If you forked, create the variant: `forge.py rule "…" --why "…" --when "…" --parent <rule-id>`.
5. **Loop or stop.** Continue until the signal stabilizes or the task is done. Every turn leaves the ledger richer than it found it.

## Mode: MAINTAIN (curate the culture)

Periodic housekeeping. Run when the registry has grown noisy, before a propagation, or on a cadence.

1. **Promote the proven.** Variants with repeated positive signals become trunk; the trunk they replace becomes superseded (kept).
2. **Flag the unfed.** Rules with no recent feedback get marked stale. Do not delete them — staleness is a to-do, not a verdict.
3. **Reconcile forks** per `references/methodology.md` §7: sharpen conditions on forks that serve different cases; promote-and-supersede among forks that compete for the same case.
4. **Never delete.** Every housekeeping action is a re-label, a re-condition, or a promotion, each of which appends a new registry entry. The old lines stay.

## Mode: PROPAGATE (hand out a spoon)

The public act — exporting a shareable starter for another kitchen or person.

1. **Export a live culture.** Run `python scripts/forge.py spoon --out <path>`. This writes a fresh starter containing the founding rules plus proven trunk — enough to start feeding immediately, without the graveyard of dead variants.
2. **Keep the reasons.** The spoon carries each rule's *why*, so the recipient can judge, override, and fork it honestly. A starter you cannot argue with is not a starter.
3. **Keep your mother.** Propagation copies; it never moves. Your source ledger is untouched.
4. **Tell them how to feed it.** Point the recipient at `STARTER.md` — the kitchen-agnostic instructions for keeping their new culture alive and, eventually, passing on their own spoon.

## A note on adapting proposals to the environment

A guiding instruction: the pipe manufacturer should not get in the way of the skill, even if you have to fork out and offer differentiation. In practice that means: when a kitchen constrains you (a connector is read-only, a model tier is cheaper, a permission needs human approval), fork a *variant* of the rule conditioned on that constraint — not a workaround that quietly abandons the rule. The constraint becomes part of the rule's condition, captured and inheritable, rather than a lost piece of tribal knowledge.
