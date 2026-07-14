# Goblin Steel — the ledgers

Goblin steel keeps three append-only ledgers in **JSONL** (one JSON object per line). JSONL is chosen because it is append-only by nature: you add a line, you never rewrite the file. That shape *is* the third law, enforced by the format rather than by willpower.

To change anything, append a new line. To "delete" a rule, append a superseding line and mark the old one's status — the old line stays forever. `scripts/forge.py` does all of this for you and, by design, has no delete command.

## 1. `rule-registry.jsonl`

One line per rule (including every fork and every superseded version).

| field        | meaning |
|--------------|---------|
| `id`         | stable id, e.g. `R-0007`. Assigned on append; never reused. |
| `statement`  | the rule itself, imperative and concrete. |
| `why`        | the reason it exists — what feedback or reasoning justifies it. |
| `when`       | the condition/kitchen it applies to. `"*"` means always. |
| `status`     | `trunk` \| `variant` \| `superseded` \| `stale`. |
| `parent`     | id this was forked from, or `null` for a founding rule. |
| `confidence` | `low` \| `medium` \| `high` — deliberately coarse. |
| `ts`         | ISO-8601 timestamp of this entry. |

**Example lineage** (three lines, oldest first):
```json
{"id":"R-0007","statement":"Start a task on a higher model to plan, then drop to mid-tier to execute.","why":"Planning is ambiguity-heavy; execution is not. Matching model tier to ambiguity cuts cost without cutting quality.","when":"*","status":"superseded","parent":null,"confidence":"medium","ts":"2026-07-08T09:00:00Z"}
{"id":"R-0014","statement":"Plan on the top tier, execute on mid, review on the top tier again.","why":"Review caught errors that mid-tier execution introduced; the review pass pays for itself.","when":"tasks with a correctness bar","status":"trunk","parent":"R-0007","confidence":"high","ts":"2026-07-08T11:30:00Z"}
{"id":"R-0021","statement":"For throwaway/low-stakes tasks, stay on mid-tier end to end.","why":"The top-tier review pass is wasted when nothing depends on the output.","when":"low-stakes tasks","status":"variant","parent":"R-0014","confidence":"low","ts":"2026-07-08T12:10:00Z"}
```
Note what the lineage tells you: R-0014 beat R-0007 and carries the reason; R-0021 is a fork that narrows R-0014 to a different condition, still under test. Nothing was deleted, so the whole reasoning is legible.

## 2. `feedback-ledger.jsonl`

One line per captured outcome. This is the forge — no line here, no learning.

| field      | meaning |
|------------|---------|
| `id`       | e.g. `F-0003`. |
| `rule_id`  | the rule this outcome bears on. |
| `action`   | what was actually done. |
| `outcome`  | what actually happened — concrete. |
| `signal`   | `+` (confirmed) \| `-` (contradicted) \| `~` (mixed). |
| `decision` | `hold` \| `fork` \| `promote` \| `demote`. |
| `ts`       | ISO-8601 timestamp. |

**Example:**
```json
{"id":"F-0009","rule_id":"R-0014","action":"Executed a client report on mid-tier after top-tier plan; reviewed on top tier.","outcome":"Review caught two mislabeled figures mid-tier had missed.","signal":"+","decision":"promote","ts":"2026-07-08T11:29:00Z"}
```

## 3. `permutation-log.jsonl`

One line per *deliberate* experiment — the fourth law's "managed permutations." This is how you explore on purpose instead of thrashing: vary one thing, hold the rest, watch the signal.

| field        | meaning |
|--------------|---------|
| `id`         | e.g. `P-0002`. |
| `hypothesis` | what you expect to learn. |
| `varied`     | the single thing you changed. |
| `held`       | what you deliberately kept constant. |
| `rule_id`    | the rule being probed, or `null` for open exploration. |
| `result`     | what the experiment showed (filled in after). |
| `ts`         | ISO-8601 timestamp. |

**Example:**
```json
{"id":"P-0002","hypothesis":"Mid-tier end-to-end is fine below some stakes threshold.","varied":"model tier for the review pass","held":"the plan/execute split, the prompt, the input data","rule_id":"R-0014","result":"Held up for low-stakes; produced R-0021 as a conditioned fork.","ts":"2026-07-08T12:10:00Z"}
```

## Reading the ledgers

- **Current position:** the `trunk` rules whose `when` matches your situation.
- **How trustworthy:** confidence plus the density of recent `+` feedback.
- **Why it's here:** walk `parent` back up the chain (`forge.py lineage <id>`).
- **What's shaky:** anything `stale`, or a `trunk` with recent `-` feedback and no fork yet — that is your next experiment.

The ledgers are the memory the laws depend on. Keep them fed, keep them whole.
