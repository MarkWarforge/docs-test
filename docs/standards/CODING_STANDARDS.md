# Coding Standards (C# & Unity)

> **Audience:** Engineers (Unity + backend). Artists do not need this doc — see `ASSET_NAMING_CONVENTIONS.md`.
> **Owner:** Amera (Tech Lead). **Changes:** open a PR against this file; one approver.
> **Last reviewed:** 2026-06 · **Status:** Living
>
> Formatting (whitespace, braces, `var`, naming casing) is **enforced by `.editorconfig` + Roslyn analyzers**, not by this doc. This doc covers only what tooling cannot enforce: intent, architecture, and the judgment calls. If you find yourself documenting something a formatter handles, delete it and put it in `.editorconfig` instead.

## 1. Baseline

We follow **Microsoft's C# coding conventions** by default. This document lists only **Warvest-specific decisions and deviations**. When this doc is silent, assume Microsoft's convention applies. Don't ask for a ruling on whitespace — run cleanup-on-save.

## 2. Naming

Casing rules are enforced by `.editorconfig`. What follows is *intent*, with good/bad examples.

```csharp
// Private serialized fields: _camelCase + [SerializeField]. Never public fields.
[SerializeField] private float _moveSpeed;        // GOOD
public float MoveSpeed;                            // BAD — exposes mutable state

// Interfaces describe a capability, not a thing: I + capability
public interface IDamageable { }                   // GOOD
public interface IEnemyClass { }                   // BAD — that's a base class

// Async methods carry the suffix so call sites read honestly.
public Task<BuildResult> BuildAsync(...) { }       // GOOD
public Task<BuildResult> Build(...) { }            // BAD

// Booleans read as assertions.
bool _isConstructing;   bool _hasGarrison;         // GOOD
bool _construction;     bool _garrison;            // BAD
```

Namespaces mirror folders and assemblies: `Warforge.Warvest.<Module>[.<Sub>]`, e.g. `Warforge.Warvest.Buildings.Construction`. One root namespace per `.asmdef`.

## 3. Unity conventions

**MonoBehaviour discipline.** Cache component references in `Awake`; never call `GetComponent` in `Update`. Use `Awake` for self-setup, `Start` for cross-object wiring (it runs after all `Awake`s). Don't put logic in constructors.

**Public surface.** No public fields. Expose to the inspector with `[SerializeField] private`. Expose to other code with properties. Designers tune via `[SerializeField]` + `[Range]`/`[Tooltip]`, not by editing code.

**ScriptableObjects** are the default for static/config data (building stats, unit definitions, economy curves). They are **not** for runtime mutable state — that's a data layer concern. A 4X game's balance lives in SOs so designers can iterate without recompiles.

**Coroutines vs async.** Default to `async`/`UniTask` for anything that touches IO, the backend, or addressable loads. Reserve coroutines for frame-coupled, view-layer sequencing (animations, simple timers). Don't mix the two for the same workflow.

**Assembly definitions.** One `.asmdef` per module. Dependencies point one direction (features → core → shared; never the reverse). This keeps compile times sane as you scale past a handful of engineers and lets you unit-test modules in isolation. Editor-only code goes in a separate `*.Editor.asmdef`.

**Fake null.** `==`/`?.` against destroyed `UnityEngine.Object`s lies. Don't cache a destroyed object behind `?.`; null-check explicitly where lifetime is uncertain.

## 4. Mobile performance discipline

This is the section that actually matters for a large mobile strategy game. A clean-but-allocating codebase will hitch on mid-tier Android.

- **No per-frame heap allocations.** No `LINQ`, no `foreach` over allocating enumerators, no `string` concatenation, no lambdas that capture, in any code on the per-frame or per-tick path. Profile with the Memory Profiler; the GC alloc column should be flat during steady-state gameplay.
- **Pool everything that spawns repeatedly** — projectiles, VFX, unit instances, UI list items. No `Instantiate`/`Destroy` in gameplay loops. Standardize on one pooling utility; don't let three engineers write three pools.
- **Prefer `struct` for small, short-lived data; avoid boxing.** Watch implicit boxing through `object`, `IEnumerable`, and string formatting.
- **Tick, don't `Update`.** Thousands of `MonoBehaviour.Update()` calls have real overhead. Route updatable systems through a central ticker/manager. (This is also the seam where DOTS/ECS earns its place — see §6.)
- **String discipline.** Cache or `StringBuilder`; never build UI strings every frame. Localization keys are constants, not inline literals.

## 5. Async, threading, logging, errors

- Backend/Jenkins-driven services are async end to end. Surface failures as typed results, not exceptions, on expected paths (network down is expected, not exceptional).
- **Logging:** use the project log wrapper, not raw `Debug.Log`. Wrap verbose logs in `[Conditional("WARVEST_VERBOSE")]` so they compile out of release. Shipping log spam is both a perf and a security leak.
- **Null checks** at module boundaries (public API of an `.asmdef`); trust internal invariants rather than defensively null-checking everything.

## 6. DOTS / ECS (PROVISIONAL — pending the architecture spike)

> Mark anything here provisional until the ECS evaluation lands. Don't let the team adopt ECS naming piecemeal before the decision.

If/when adopted: components are data-only and named for the data (`HealthComponent`, `MovementSpeedComponent`); systems are named for the verb (`MovementSystem`, `GarrisonAssignmentSystem`). Keep ECS code in its own assemblies. Decide the MonoBehaviour↔ECS boundary explicitly and record it as an ADR before anyone writes a system in anger.

## 7. Comments & docs

XML doc comments (`///`) on every public type/member that crosses an `.asmdef` boundary — these are your API. Inline comments explain **why**, never **what** (the code says what). A comment that restates the code is debt.

## 8. Source control & commits

Branching, LFS, and protected branches follow the established GitLab-Flow setup (`develop`/`production`). Commit messages: imperative subject ≤ 72 chars, body explains *why*. Reference the ClickUp task ID. Don't commit generated files, `.meta` orphans, or large binaries outside LFS.

## 9. Code review checklist (paste into the PR template)

- [ ] Cleanup-on-save ran; CI format check is green
- [ ] No new per-frame/tick allocations (profiled if on a hot path)
- [ ] No public fields; inspector exposure via `[SerializeField] private`
- [ ] Async methods suffixed; no fire-and-forget without justification
- [ ] Spawned objects pooled, not Instantiate/Destroy
- [ ] Public cross-assembly members have XML docs
- [ ] No raw `Debug.Log` in shippable paths
