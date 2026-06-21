# Home

This is the home of all engineering documentation. **It lives in the repo** (`/docs`), versioned and PR-reviewed alongside the code it describes — not in ClickUp (that's for tasks/sprints) and not in a separate wiki tool that drifts out of sync. One home.

## Preview

There are **two kinds of doc**, and conflating them is the classic failure that turns a "living wiki" into a pile of lies:

| | **Point-in-time** (ADR, TDD) | **Living** (Architecture, Onboarding) |
|---|---|---|
| Purpose | Record a *decision* and its *context* | Describe *how the system works now* |
| Lifecycle | Written once, dated, **frozen** | Continuously maintained, must match reality |
| If it's stale | Fine — it's history | A bug — fix it like a bug |
| Grows by | Accumulating new records | Being *distilled and rewritten*, not appended |

You do **not** build the living architecture doc by piling up feature TDDs. TDDs go stale the instant the code changes; forty stale TDDs handed to a new hire are worse than nothing because they'll trust wrong information. Instead: TDDs/ADRs are an append-only **historical archive**, and someone periodically distills the current truth into the small `architecture/` set.

## When do I write what?

- **An architecture-level decision** (tooling, branching, data layer, MonoBehaviour↔ECS boundary, save format) → **ADR**. Short, numbered, frozen. You already have two ADRs' worth of decisions made (source control, three-env architecture) — backfill them.
- **A non-trivial feature** that hits the trigger (server-authoritative state, data/save-format change, economy systems, cross-cutting, or > ~3 days) → **TDD**, reviewed *before* coding.
- **A small, local, low-risk feature** → **no doc**. Just a good PR description. Mandating a TDD for everything is how the practice dies; scale rigor to risk.
- **"How does X actually work today?"** → belongs in `architecture/`, and it's someone's job to keep it true.

## Process

1. Author drafts from the template, opens a PR.
2. At least **one reviewer** comments/approves before implementation starts. The review *is the value* — a design doc nobody reads is write-only waste.
3. On merge, the doc is part of the record. After the feature ships, mark the TDD `Shipped` and leave it frozen.
4. Owner (Amera, for now) periodically folds durable truths into `architecture/`.

## Onboarding

New engineers read `onboarding/start-here.md` → `architecture/overview.md` → the standards docs. They do **not** read the TDD archive front to back; they pull from it when they need the *why* behind a specific decision.
