# Agentic Matrix

**An evidence-driven evaluation framework for agentic coding workflows.**

Agentic Matrix is a research method and evidence archive for testing whether changes to AI-assisted software-engineering workflows actually improve outcomes.

It evaluates candidate mechanisms such as routing policies, prompt compilers, skills, reviewers, context strategies, memory systems, and reasoning configurations against the current real workflow using matched tasks, frozen decision rules, holdouts, telemetry, and explicit promotion thresholds.

The central rule is simple:

> **New complexity must beat the current real baseline on decision-relevant evidence before it becomes the default.**

## Repository Type

This repository is a **methodology, evaluation, and case-study repository**.

It is not:

- an autonomous agent framework;
- an AI model;
- an installable application;
- a replacement for Codex or another coding agent;
- a claim that one workflow is globally superior;
- a source of repository, deployment, provider, or production authority.

The methodology can be adapted to other agentic engineering workflows. The included September 2026 study is a bounded historical experiment, not a universal benchmark.

## What This Repository Demonstrates

Agentic Matrix focuses on problems that are easy to hide when AI engineering workflows are evaluated informally:

- whether added routing or agent machinery actually improves accepted outcomes;
- whether faster or lower-token execution introduces quality regressions;
- whether failures belong to the candidate, controller, environment, evaluator, or instrumentation;
- whether review agents detect defects beyond deterministic validation;
- whether improvements survive untouched holdout tasks;
- whether token/context reductions preserve correctness and evidence quality;
- whether added workflow complexity has earned its operational cost.

The method deliberately permits a negative result. A candidate that fails to materially beat the baseline is not promoted.

## Current Public Study

The first preserved study is:

**General Codex Engineering Loop — Stage A**  
**Date:** September 4, 2026  
**Experimental units:** 24  
**Model calls:** 22  
**Experimental reruns:** 0

The study compared four workflow policies:

| Policy | Description |
| --- | --- |
| **P0** | Current real human-directed Codex baseline |
| **P1** | Conditional prompt-compiler path |
| **P2** | Conditional deep state/skill-escalation path |
| **P3** | Deterministic host-side router |

A separate review experiment compared:

| Policy | Description |
| --- | --- |
| **R0** | Deterministic validation only |
| **R1** | The same validation plus an independent read-only review agent |

### Result

```text
STAGE_A_STATUS=COMPLETE_ACCEPTED
EXPERIMENTAL_UNITS=24/24
MODEL_CALLS=22/22
EXPERIMENTAL_RERUNS=0

ROUTING_WINNER=P0_BY_NON_PROMOTION
P1_PROMOTED=NO
P2_PROMOTED=NO
P3_PROMOTED=NO
GENERAL_ROUTER_PROMOTED=NO

HOLDOUT_COMPLETE=YES

REVIEW_R0=TP0 FP0 FN2
REVIEW_R1=TP2 FP0 FN0
GLOBAL_REVIEW_SUPERIORITY_CLAIM=NO

STAGE_B_AUTHORIZED=NO
```

No additional routing mechanism materially earned promotion over the simpler P0 baseline under the frozen decision rules.

The read-only reviewer detected both hidden defects in the two-case review experiment while deterministic validation detected neither. Because the review sample was only **N=2**, the result is retained as bounded evidence rather than a global reviewer-superiority claim.

## Measured Stage-A Usage

Across the 22 model-call units represented in the preserved public data:

```text
TOTAL_TOKENS=3,458,207
INPUT_TOKENS=3,347,321
CACHED_INPUT_TOKENS=2,780,288
OUTPUT_TOKENS=70,475
REASONING_TOKENS=40,411
CODEX_ACTIVE_SECONDS=1,628.586
```

These are experiment measurements, not cost-normalized business metrics.

## Repository Structure

```text
agentic_matrix/
├── README.md
├── methods/
│   ├── AGENTIC_MATRIX_METHOD_V1_1.md
│   ├── AGENTIC_LIVE_TELEMETRY_STANDARD_V1.md
│   ├── AGENTIC_TOKEN_ATTRIBUTION_STANDARD_V1.md
│   ├── AGENTIC_CONTROLLER_EXECUTION_STANDARD_V1.md
│   ├── GENERAL_CODEX_ENGINEERING_LOOP_24_RUN_ALLOCATION_V1_1.md
│   └── GENERAL_CODEX_PATHWAY_GAP_ANALYZER_V1_1.md
├── case-studies/
│   └── 2026-09-04_GENERAL_CODEX_ENGINEERING_LOOP_STAGE_A_CASE_STUDY.md
├── data/
│   ├── 2026-09-04_STAGE_A_METRICS.json
│   └── 2026-09-04_STAGE_A_UNITS_001_024.csv
└── scripts/
    └── verify_stage_a.py
```

## Verify the Published Stage-A Data

The public Stage-A summary can be recomputed from the per-unit CSV and checked against the aggregate JSON without calling an AI model or accessing private project data.

```bash
python scripts/verify_stage_a.py
```

A successful verification reports that the preserved unit count, model-call count, token totals, policy summaries, and review results agree with the published aggregate data.

This verifies the consistency of the public dataset. It does **not** reproduce the original model executions.

## Reproducibility Boundary

There are two different levels of reproducibility in this repository.

### Publicly reproducible

The repository provides enough material to:

- inspect the Agentic Matrix methodology;
- inspect the frozen Stage-A allocation;
- inspect per-unit measurements;
- recompute aggregate measurements;
- review the resulting case study;
- adapt the method to a different current workflow.

### Not publicly reproduced

The exact September 4, 2026 model executions depended on historical task fixtures, repository states, private execution evidence, controller state, and project-specific environments that are not published here.

The case study should therefore be interpreted as a preserved, auditable historical experiment rather than a self-contained executable benchmark suite.

## Method

The reusable experimental method is defined in:

[`methods/AGENTIC_MATRIX_METHOD_V1_1.md`](methods/AGENTIC_MATRIX_METHOD_V1_1.md)

Supporting standards cover:

- live native token telemetry;
- token/context attribution;
- long-running controller and executor behavior;
- failure classification;
- evidence identity;
- review and rereview;
- gap analysis;
- holdouts;
- promotion and non-promotion rules.

The current real workflow is always the baseline. Candidate machinery does not receive credit merely because it is more sophisticated.

## Evidence and Claim Discipline

Agentic Matrix separates:

```text
AVAILABLE
≠
ACTIVATED
≠
QUALIFIED
≠
PROMOTED
```

It also distinguishes candidate failures from:

- controller or harness failures;
- environment/toolchain failures;
- evaluator defects;
- infrastructure failures;
- telemetry/instrumentation failures;
- preexisting system failures.

Missing telemetry remains unknown rather than being silently converted to zero.

A successful bounded experiment supports claims only about the tested workflow, task classes, configuration, and evidence. It does not establish universal superiority.

## Future Studies

Each future experiment should:

1. freeze the then-current real workflow as P0;
2. define the candidate treatment before execution;
3. use task classes derived from real engineering history;
4. preregister metrics, decision thresholds, evaluator, holdout, authority, and call budget;
5. preserve native telemetry and durable evidence;
6. apply promotion/non-promotion rules without rewriting negative results;
7. retain untouched holdout evaluation;
8. publish a new dated case study rather than modifying an older one.

Historical case studies remain immutable evidence.

## Public / Private Boundary

This repository intentionally publishes the evaluation methodology, bounded case-study conclusions, and normalized evidence needed to understand the work.

It does not publish unrelated proprietary project source, credentials, private customer data, production authority, or private execution environments.

## License

Apache License 2.0.
