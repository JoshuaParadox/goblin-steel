# You've been handed a spoon of starter

This is goblin steel™. What you just downloaded is not a finished product — it's a **living culture**, the same way a sourdough starter is. You keep it by feeding it, it adapts to your kitchen, and one day you pass a spoon of it on to someone else.

It's a small, self-contained discipline — you already have everything you need to start baking.

You and the AI you run this with are a *dyad* — a human paired with their assistant. That's the unit goblin steel is built to feed: the two of you learning together, leaving a trail neither of you has to hold in memory alone. (When the assistants start coordinating directly, dyads become *quads*.)

## The one thing to understand

> A rule is not a fact to be stored. It is a living culture to be fed. You keep it alive with feedback, you grow it by forking, and you never throw the mother out.

Most of us treat our rules of thumb like carvings in stone — we set them, then quietly overwrite them when they stop working, and the reasoning behind the change evaporates. Goblin steel treats a rule like dough instead: alive, fed, and never thrown out. When a rule changes, you keep the old one as history and branch a new one beside it. Nothing is lost, so nothing has to be re-learned the hard way.

## The five laws (plain version)

1. **Feedback is the forge.** Write down what actually happened before you change a rule. An outcome you didn't record didn't happen.
2. **Feed, don't finish.** A rule you haven't tested lately isn't wrong — it's just stale, and you shouldn't fully trust it until you've fed it again.
3. **Expand, never delete.** When a rule stops working, retire it *beside* the new one; don't erase it. The old rule explains why the new one exists.
4. **Fork, don't overwrite.** A change is a new branch with a reason and a condition attached — "in this situation, do this instead" — not a silent edit.
5. **The pipe is not the point.** However you store this — a folder, a repo, a notes app, a notebook — is just plumbing. The discipline is the same everywhere. Never bend the laws to fit a tool.

## Feeding your starter

Goblin steel keeps three simple logs (plain text, one line per entry, you only ever add lines):

- a **rule registry** — your rules, each with its reason, its condition, and its history;
- a **feedback ledger** — what you tried, what happened, and what you decided;
- a **permutation log** — experiments you ran on purpose.

The little tool `scripts/forge.py` feeds them for you, and by design it has *no delete button* — that's the discipline built into the tool instead of relying on willpower.

Get started in your own kitchen:

```bash
python scripts/forge.py seed          # plant the culture here
python scripts/forge.py show          # see the rules you've been handed
python scripts/forge.py rule "Do X when Y" --why "..." --when "Y" --parent R-0002
python scripts/forge.py feedback R-0002 --action "tried X" --outcome "worked" --signal + --decision promote
python scripts/forge.py lineage R-0004 # trace why a rule exists
```

Prefer paper? The laws still hold. Keep the three logs by hand, always add, never erase, and write down the *reason* and the *condition* every time. That's goblin steel too — the tool is a convenience, not the point.

## It will become yours

The spoon you got carries a handful of founding rules — goblin steel's own laws, so the culture is alive from the first minute. As you feed it in your kitchen, it will drift: rules will fork to fit your flour, your climate, your hands. Within a while your starter will bake differently from everyone else's, yet still trace back to the same mother. That divergence is the feature.

## Passing it on

When you want to hand a spoon to someone else:

```bash
python scripts/forge.py spoon --out ../starter-for-a-friend
```

That exports a clean, live starter — the founding rules plus whatever you've proven — **with the reasons intact**, so the person you give it to can question it, adapt it, and fork it honestly. And it never touches your own culture: you share by copying a portion, never by giving away your only jar.

Keep your mother. Feed it. Pass on a spoon.
