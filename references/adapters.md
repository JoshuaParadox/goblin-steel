# Goblin Steel — deployment adapters

The fifth forge law: *the pipe is not the point.* The same three ledgers ride whatever a kitchen offers. An adapter answers one question — **where do the ledgers physically live here, and how do I read and write them?** — without touching the four core laws.

If a kitchen fits none of these, fork a new adapter. That is the law working, not an exception to it.

## Detecting the pipe

Work top-down; stop at the first match:

1. **GitHub / a git repo present** (a `.git` directory, or git MCP/API tools available) → **GitHub adapter**. Prefer this when it exists; git already embodies half the discipline.
2. **An MCP "brain" with a backing store** (e.g. a database/Supabase MCP, or a notes store exposed over MCP) → **MCP-brain adapter**.
3. **A Cowork/Claude skill or an attached project** (you are running as an installed skill, or a project is attached) → **Cowork adapter**.
4. **None of the above** → **Notebook adapter** (plain files or literal paper). Always available as a fallback.

When two could apply, choose by *where the host library's memory already lives* — put the ledgers next to the thing they describe, so lineage and rules travel together.

## GitHub adapter (preferred where present)

- **Where the ledgers live:** committed files in the repo (e.g. `goblin/rule-registry.jsonl`).
- **Fork the rule → branch.** A variant under test can literally be a branch; a proven variant merges to the trunk branch. Even without branching, `forge.py rule --parent …` records lineage in-file.
- **Feedback → commits and issues.** Each `forge.py feedback` is a commit; substantive outcomes can open issues for discussion (this is why GitHub was chosen over flat storage — line-level comments and version control).
- **Reconcile → merge / PR.** Competing forks reconcile through review, the discipline programmers already trust.
- **Keep the mother:** history is inherent; nothing is ever truly lost.

## MCP-brain adapter

- **Where the ledgers live:** the backing store behind the MCP, one row/record per ledger line. Read and write only through the MCP's tools — never assume direct DB access.
- **Append-only in a mutable store:** enforce it in behaviour. Insert new records; never `UPDATE`/`DELETE` a rule to change it — insert a superseding record and mark the old one's status. If the store lacks an append helper, `forge.py` can still manage local JSONL and sync up through the MCP.
- **Where this leads:** the shared library as a brain that every dyad and quad reads from and feeds. The adapter is what makes the same starter that runs in a Cowork folder also run in the brain, unchanged in principle.

## Cowork / Claude skill adapter

- **Where the ledgers live:** files in the skill's own folder for a personal culture, or in the attached project (via project docs) for a shared one so teammates see the same lineage.
- **Fork/feed/reconcile:** all through `forge.py` against those files; surface `maintain` results to the user in chat.
- **Good for:** an individual's dyad, a single project's playbook, and the moment someone first downloads the starter.

## Notebook adapter (lowest-tech fallback)

- **Where the ledgers live:** a single markdown file, or paper, following the same three-section structure.
- **Why it still counts:** the laws are about *discipline*, not tooling. A human feeding a rule-log by hand — append a fork, never erase, note the reason and the condition — is running goblin steel correctly. This is the proof that the pipe is not the point.

## The rule for all adapters

Adapt the *carrying*, never the *culture*. If you find yourself weakening "never delete" or "fork don't overwrite" to fit a pipe, stop — you are bending the culture to the pipe, which is the exact failure the fifth law exists to prevent. Fork the adapter harder instead.
