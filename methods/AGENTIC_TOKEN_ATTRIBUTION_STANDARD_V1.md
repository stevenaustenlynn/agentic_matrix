# Agentic Token Attribution Standard v1

**Status:** OWNER-REQUIRED

**Effective:** 2026-09-04

**Purpose:** Explain not only how many tokens an agentic run consumes, but which context, phases, responses, tool outputs, rereads, retries, and controller decisions are associated with that consumption so equivalent or better accepted outcomes can be pursued with less token waste.

This standard extends `AGENTIC_LIVE_TELEMETRY_STANDARD_V1.md`. It creates no execution, Git, provider, production, acceptance, release, or causal-claim authority.

## Permanent requirements

```text
TOKEN_ATTRIBUTION_LEDGER=REQUIRED
PROMPT_COMPONENT_MANIFEST=REQUIRED
UPSTREAM_RESPONSE_USAGE=REQUIRED_WHEN_AVAILABLE
TOOL_CONTEXT_EVENT_CAPTURE=REQUIRED
REPEATED_CONTEXT_DETECTION=REQUIRED
UNCHANGED_SOURCE_REREAD_DETECTION=REQUIRED
TOKEN_DRIVER_PARETO=REQUIRED
TOKEN_WASTE_SIGNAL_REPORT=REQUIRED
ATTRIBUTION_CONFIDENCE_LABELS=REQUIRED
PER_PHASE_TOKEN_TOTALS=REQUIRED
PER_RESPONSE_TOKEN_TOTALS=REQUIRED_WHEN_AVAILABLE
ACCEPTED_OUTCOME_TOKEN_BREAKDOWN=REQUIRED
```

## Attribution ceiling

Do not claim token-level causality that the executor does not expose.

The system may know exact native token usage for a response while knowing only which measured context components were introduced before that response. Therefore preserve these evidence classes:

- `NATIVE_EXACT` — token counts/context-window values emitted by the executor/provider protocol.
- `MEASURED_SOURCE` — exact local prompt/file/diff/tool-output component identity, bytes, lines, hash, role, and insertion time.
- `DELTA_ATTRIBUTED` — a native usage delta temporally associated with a measured context change or phase boundary; useful diagnostically but not token-by-token causality.
- `INFERENCE` — bounded interpretation such as likely waste driver or optimization candidate.
- `UNKNOWN` — attribution cannot be supported.

Never convert temporal sequence alone into causal attribution.

## Prompt/context component manifest

Before each model call or native response boundary where practicable, record all known context components with stable identities. Suggested roles:

```text
OWNER_TASK
PROJECT_INSTRUCTIONS
AGENTS
CANONICAL_SOURCE
CURRENT_STATE
TASK_SPEC
CANDIDATE_DIFF
PRIOR_REVIEW
MEMORY_CONTEXT
FILE_READ
TOOL_OUTPUT
TEST_OUTPUT
COMMAND_OUTPUT
PREVIOUS_MODEL_OUTPUT
OTHER_CONTEXT
```

For each component record when available:

- component ID and role;
- source path/URI or synthetic origin;
- content hash;
- bytes and line count;
- insertion/read timestamp;
- whether content changed since prior inclusion;
- prior identical inclusion count;
- whether the component is cache-eligible/observed cached when native evidence supports that distinction;
- phase/call/response association;
- provenance/evidence label.

Do not require a tokenizer estimate when native usage is available. Approximate component-token estimates, if ever used, must be clearly labeled `ESTIMATE` and cannot replace native totals.

## Durable run layout

A compliant run should retain the equivalent of:

```text
<run>/
  token-events.jsonl
  codex-events.jsonl
  live-telemetry.json
  prompt-components.jsonl
  tool-context-events.jsonl
  response-usage.jsonl
  token-attribution.jsonl
  token-driver-pareto.json
  token-waste-signals.json
  call-1-receipt.json
  call-2-receipt.json
  ...
  run-token-summary.json
```

Raw/native events remain authoritative for emitted usage. Summaries and attribution views are derived indexes.

## Required diagnostic views

### Token-driver Pareto

Rank decision-relevant token drivers by observed or bounded contribution, including where measurable:

- cached/replayed context;
- newly introduced prompt/source context;
- candidate diffs;
- file reads;
- tool and command output;
- test logs;
- prior review/reasoning context;
- model output;
- reasoning output;
- retries/repairs;
- controller/infrastructure recovery;
- repeated unchanged context;
- compaction/reconstruction churn;
- unattributed remainder.

Every row must carry its attribution/evidence class.

### Waste signals

Detect and report without automatically changing behavior:

- identical unchanged source included multiple times;
- unchanged file reread multiple times in one bounded task;
- full diff resent when a smaller content-addressed changed-region representation might satisfy the same evidence requirement;
- large test/tool logs passed forward when only bounded failure/success evidence is needed;
- repeated project boilerplate that native caching does not cover effectively;
- low cache reuse across closely related calls;
- repair/review loops caused by controller or evaluator defects rather than candidate defects;
- redundant model calls;
- context-window pressure/compaction associated with repeated context;
- output/reasoning volume disproportionate to accepted-result value, labeled as an optimization hypothesis unless experimentally proven.

## Per-phase and per-response accounting

Record native usage at the finest trustworthy boundary the executor exposes. Aggregate into phases such as:

```text
PREFLIGHT
IMPLEMENTATION
DETERMINISTIC_VERIFICATION
SEMANTIC_REVIEW
BOUNDED_REPAIR
REREVIEW
FINAL_VERIFICATION
HANDOFF
```

Where native per-response usage exists, retain it separately from cumulative thread/run totals.

Controller/instrumentation failures must be attributed to controller/infrastructure recovery rather than to candidate engineering work when the evidence supports that classification.

## Optimization law

Token attribution is diagnostic. It does not authorize automatic prompt/context reduction.

A proposed reduction becomes a workflow change and must preserve:

- accepted quality/correctness;
- authority and scope compliance;
- security/privacy/sovereignty;
- evidence completeness;
- reproducibility;
- operator usability.

When causal attribution matters, test the proposed reduction against the current workflow using Agentic Matrix matched comparison. The objective is not minimum tokens in isolation; it is lower unnecessary token/context burden for the same or better accepted outcome.

## Terminal presentation

The default live monitor may add a compact `TOKEN DRIVERS` region beneath the standard `AGENTIC RUN` panel when useful. Example only:

```text
┌─ TOKEN DRIVERS ───────────────────────────────────────────────────────────┐
│ CACHED / REPLAYED CONTEXT        151.0K   73.9%   NATIVE_EXACT           │
│ NEW PROMPT + SOURCES              21.4K   10.5%   DELTA_ATTRIBUTED       │
│ TOOL / FILE OUTPUT                11.9K    5.8%   DELTA_ATTRIBUTED       │
│ REASONING                           7.2K    3.5%   NATIVE_EXACT           │
│ MODEL RESPONSE                      5.6K    2.7%   NATIVE_EXACT           │
│ OTHER / UNATTRIBUTED                7.3K    3.6%   UNKNOWN                │
│ TOP NEW SOURCE   candidate.diff   13.8K                                  │
│ WASTE SIGNALS    repeated diff ×2 · unchanged source reread ×3           │
└──────────────────────────────────────────────────────────────────────────┘
```

Example values are illustrative, not evidence.

## ATHANOR boundary

Once ATHANOR is integrated and accepted as workflow-measurement owner, ATHANOR should ingest or own the normalized attribution/telemetry analysis while preserving raw evidence identities. LAPIS presents the evidence and references ATHANOR measurements rather than creating a conflicting measurement truth.

## Memory boundary

Memory systems may use distilled stable attribution lessons and pointers to evidence, but must not replace raw run telemetry, current state, or canonical workflow policy. A remembered optimization remains context until current evidence validates its applicability.

## Claim boundary

A token-driver report may support statements about observed usage structure in the recorded run. It does not by itself prove that removing a component will preserve quality or that a workflow is globally more efficient. Such claims require matched evidence.