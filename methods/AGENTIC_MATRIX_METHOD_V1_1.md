# Agentic Matrix Method v1.1

## Purpose

Evaluate candidate improvements to a real agentic coding workflow using matched tasks, preregistered decision rules, evidence-bound execution, and a complexity burden of proof.

The method is intended for future skills, reviewers, routing policies, memory/context systems, planning layers, model/reasoning configurations, prompt compilers, and other workflow mechanisms.

## Core rule

The current real workflow is always the baseline. A candidate becomes default only when it beats that baseline on decision-relevant outcomes without violating quality, authority, security, sovereignty, or claim validity.

Availability is not activation. Activation is not qualification. Technical success is not owner acceptance.

All future governed agentic runs must also comply with `AGENTIC_LIVE_TELEMETRY_STANDARD_V1.md`. Missing native telemetry remains `UNKNOWN`; it must never be silently converted to zero usage.

## Baseline and candidate arms

- **P0 — current production-style baseline.** Human-directed Codex workflow with the then-current proven controls. No speculative router.
- **P1/P2/P3 — candidate mechanisms.** Each arm must differ from P0 only by the intended treatment where causal attribution matters.
- **R0 — no-review control** for the review-agent subexperiment.
- **R1 — read-only review-agent candidate** for the review-agent subexperiment.

Future runs may rename or add arms, but every treatment must be explicitly defined and frozen before execution.

## Required experiment classes

The 2026-09-04 experiment used real-history task classes including:

1. raw/ambiguous repository engineering work;
2. bounded typed-contract work;
3. debugging/recovery work where a first attempt or surrounding machinery can fail;
4. holdout work not used to tune the candidate path;
5. defective-diff review cases for reviewer evaluation.

Future runs should derive task classes from actual recent engineering history rather than generic benchmark prompts.

## Preregistration requirements

Before spending experimental model calls, freeze:

- experiment ID and date;
- current baseline workflow P0;
- candidate mechanism(s);
- task taxonomy and allocation;
- model and reasoning configuration;
- executor and sandbox controls;
- allowed/prohibited actions;
- run count and retry policy;
- matched-pair or matched-block design;
- evaluator and evaluation criteria;
- primary and secondary metrics;
- minimum practical improvement thresholds (MPIDs);
- promotion/non-promotion rules;
- holdout design;
- repair/failure classification rules;
- artifact/evidence locations;
- stop conditions and authority boundaries;
- live-token telemetry source and retention path;
- context-window source when available;
- terminal-monitor presentation path;
- maximum model-call budget covering the longest authorized causal path, including required repair and rereview calls.

Do not modify these after observing results except through an explicitly labeled posthoc amendment.

## Metrics

Measure outcomes that affect real engineering throughput and quality, not just raw model speed.

At minimum collect:

- final correctness / acceptance result;
- first-pass acceptance;
- final acceptance;
- regression count;
- authority/safety violations;
- scope violations;
- retries and repair calls;
- model-call count;
- input tokens;
- cached input tokens;
- uncached input tokens (`input - cached input`);
- output tokens;
- reasoning tokens when available;
- total token volume;
- cumulative run token volume;
- context-window utilization when available;
- cache-hit percentage when defined;
- native token-usage deltas / rate when available;
- active model seconds;
- end-to-end wall time;
- operator-attention burden where measurable;
- context waste or repeated context where measurable;
- artifact/evidence completeness;
- added workflow complexity.

Quality, correctness, authority, security, sovereignty, and claim validity are hard constraints. A faster arm that violates them does not win.

## Live telemetry requirement

For every future governed agentic run:

```text
LIVE_TOKEN_TELEMETRY=REQUIRED
RAW_TOKEN_EVENT_RETENTION=REQUIRED
PER_CALL_TOKEN_RECEIPT=REQUIRED
CUMULATIVE_RUN_TOKEN_SUMMARY=REQUIRED
CACHED_VS_UNCACHED_INPUT=REQUIRED
CONTEXT_WINDOW_UTILIZATION=REQUIRED_WHEN_AVAILABLE
TERMINAL_MONITOR_DISPLAY=REQUIRED
LAPIS_TUI_PRESENTATION=FUTURE_THIS_TUI_SLICE_OR_NEXT
ATHANOR_MEASUREMENT_EXPORT=REQUIRED_WHEN_ATHANOR_INTEGRATES
```

The normative details are in `AGENTIC_LIVE_TELEMETRY_STANDARD_V1.md`. Native executor usage events are the source of truth where available. The monitor is read-only and must not retry, advance, accept, signal, or mutate the worker.

## Matched comparison

Where causal attribution matters, vary only the intended treatment. Use the same or tightly matched task, repository state, model class, reasoning effort, sandbox, authority envelope, and evaluator.

Never compare one arm on easy tasks and another on harder tasks and call the difference causal.

## Holdout

Reserve a holdout that is not used to tune the candidate mechanism. A candidate that looks good only on development examples does not generalize.

The 2026-09-04 Stage-A run completed its holdout and still did not promote P1/P2/P3.

## Review-agent subexperiment

When evaluating a reviewer, use known defective diffs and a no-review control.

Record at minimum:

- true positives (TP);
- false positives (FP);
- false negatives (FN);
- review latency;
- token cost;
- whether review changed the final decision.

The first run produced R0 = TP0/FP0/FN2 and R1 = TP2/FP0/FN0, but N=2 was too small for a global superiority claim.

## Promotion rule

A candidate is promoted only when all hard constraints pass and the preregistered evidence clears the relevant MPIDs.

If a candidate does not clearly beat P0, **P0 wins by non-promotion**. Do not invent a router merely because multiple variants exist.

## Failure and repair classification

Separate:

- candidate implementation defect;
- controller/harness defect;
- environment/toolchain defect;
- authority failure;
- infrastructure ambiguity;
- test expectation defect;
- telemetry/instrumentation defect;
- genuine task failure.

Do not spend a candidate repair call on a controller, telemetry, or environment failure. Fix the experiment machinery, preserve the candidate budget, and rerun only when justified.

## Evidence

Every run should preserve:

- preregistration;
- allocation table;
- task/unit receipts;
- Codex event streams when available;
- append-only raw token events;
- live telemetry snapshot;
- per-call token receipts;
- cumulative run-token summary;
- wall/active times;
- changed-file and diff identities;
- verification logs;
- evaluator outputs;
- holdout results;
- final machine-readable metrics;
- final case study.

Older case studies are immutable historical evidence.

## Claims

Use bounded claims only. A successful run can support statements about the exact tested workflow, tasks, model configuration, and date. It does not establish global superiority.

## Recommended future-run sequence

1. Freeze current P0.
2. Define one candidate treatment.
3. Pull task classes from recent real engineering history.
4. Preregister allocation, MPIDs, evaluator, holdout, authority, telemetry, and longest-path model-call budget.
5. Initialize durable live-token telemetry and the read-only monitor before the first model call.
6. Run deterministic baseline checks.
7. Execute matched experimental units.
8. Run holdout.
9. Run optional reviewer arm if relevant.
10. Aggregate metrics, including cached/uncached context and context-window utilization where available.
11. Apply promotion/non-promotion rules.
12. Write a dated immutable case study.
13. Keep the winning workflow as the next run's P0.
