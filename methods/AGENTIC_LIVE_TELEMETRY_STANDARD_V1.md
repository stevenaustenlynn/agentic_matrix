# Agentic Live Telemetry Standard v1

**Status:** OWNER-REQUIRED

**Effective:** 2026-09-04

**Scope:** All future governed agentic coding loops unless a controlling project source explicitly requires a stricter standard. This standard does not create execution, Git, provider, production, acceptance, or release authority.

## Required capabilities

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

## Evidence model

Each agentic run must retain, under its durable run-evidence root, the equivalent of:

```text
<run>/
  token-events.jsonl
  live-telemetry.json
  call-1-receipt.json
  call-2-receipt.json
  ...
  run-token-summary.json
```

`token-events.jsonl` is append-only raw usage evidence. `live-telemetry.json` is a small current snapshot for presentation. Per-call receipts are immutable call summaries after completion. `run-token-summary.json` aggregates the run without replacing raw evidence.

When the executor exposes native token-usage events, those events are the source of truth. Do not estimate token counts from text length, process CPU, output bytes, or wall time. If a field is genuinely unavailable, record `UNKNOWN`/null rather than inventing a value.

## Required telemetry fields

Record when available:

- run ID;
- task ID;
- phase;
- model;
- reasoning effort;
- call index and preregistered call ceiling;
- elapsed call time;
- elapsed run time;
- input tokens;
- cached input tokens;
- uncached input tokens;
- output tokens;
- reasoning-output tokens;
- total tokens;
- cumulative run tokens;
- context-window tokens;
- context tokens currently used;
- context utilization percentage;
- cache-hit percentage;
- token delta since the previous native usage snapshot;
- token rate derived only from real usage-snapshot deltas;
- timestamp/source identity for each usage update.

Derived values:

```text
UNCACHED_INPUT = INPUT - CACHED_INPUT
CACHE_PERCENT = CACHED_INPUT / INPUT * 100   # when INPUT > 0
CONTEXT_PERCENT = CONTEXT_USED / CONTEXT_WINDOW * 100
RATE = TOKEN_DELTA / ELAPSED_TIME_BETWEEN_REAL_USAGE_SNAPSHOTS
```

Do not treat cached tokens and uncached tokens as equivalent when analyzing context efficiency.

## Terminal monitor presentation

The default operator-facing monitor should preserve this compact structure, adapting widths to the terminal without dropping required information:

```text
┌─ AGENTIC RUN ─────────────────────────────────────────────────────────────┐
│ PHASE     ASTRA_IMPLEMENTATION                    ELAPSED  08:42          │
│ MODEL     GPT-6 ASTRA / XHIGH                     CALL     1 / 4          │
│                                                                          │
│ INPUT       184,320     CACHED      151,040       CACHE      82.0%       │
│ OUTPUT       12,846     REASONING     7,231       TOTAL     204,397      │
│                                                                          │
│ CONTEXT   204k / 512k   ████████░░░░░░░░░░░ 40%                         │
│ RATE      +18.4k tokens since last update                               │
│                                                                          │
│ RUN TOTAL    204,397 tokens       MODEL CALLS  1                         │
└──────────────────────────────────────────────────────────────────────────┘
```

Presentation rules:

- update only when a real usage event, phase transition, call transition, or meaningful elapsed-time boundary occurs;
- avoid rapid redraw that distracts the operator or wastes CPU;
- show `—` or `UNKNOWN` for unavailable values;
- preserve the distinction between current-call and cumulative-run usage;
- show context utilization only when the model context window and current usage are known;
- keep monitoring read-only; it must not retry, signal, advance, accept, or mutate the worker;
- live-monitor failure must not corrupt the underlying run or raw token evidence.

## Controller requirements

A compliant long-running controller must:

1. initialize the telemetry evidence files before the first candidate model call;
2. capture native usage events as they become available;
3. atomically refresh `live-telemetry.json` from raw evidence;
4. emit a per-call receipt after each model call;
5. emit a cumulative summary at every completed call and final stop;
6. expose the live snapshot to a separate read-only terminal monitor;
7. preserve raw events even if the presentation layer crashes;
8. keep controller/model transport reliability independent from the monitor implementation;
9. classify missing telemetry as missing evidence, not zero usage;
10. distinguish controller/instrumentation failure from candidate implementation failure.

Model-call ceilings must cover the longest authorized causal path, including required repair and rereview calls. Unused reserve capacity is not a failure.

## LAPIS presentation

LAPIS should eventually surface a compact subset of the same evidence in the command bar, for example:

```text
ASTRA ◆ XHIGH    TOK 204K    CTX 40%    CACHE 82%
```

The TUI is presentation only. Raw token events and durable receipts remain the evidence source.

## ATHANOR boundary

When ATHANOR integrates, export the same normalized telemetry rather than creating a second conflicting measurement truth. ATHANOR may analyze tokens, cache efficiency, context waste, model calls, retries, wall time, repair rate, first-pass/final acceptance, operator intervention, and quality outcomes. LAPIS presents and references this evidence; Agentic Matrix uses it for matched experiments.

## Claim boundary

Live telemetry improves observability; it does not by itself establish workflow superiority, quality, or causal benefit. Any efficiency claim still requires the Agentic Matrix comparison standard or another qualified matched evaluation.
