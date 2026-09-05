# Agentic Controller Execution Standard v1

**Status:** OWNER-REQUIRED

**Effective:** 2026-09-04

**Purpose:** Preserve the durable controller/executor lessons established during LAPIS agentic engineering so future runs do not rediscover avoidable transport, budgeting, evidence-binding, monitoring, or failure-classification defects.

This is a workflow method. It creates no project, Git, provider, production, acceptance, release, or TRINITY authority.

## Long-running execution shape

Prefer this pattern for long machine work:

```text
LONG_MACHINE_WORK
→ normal WSL host
→ deterministic local controller
→ durable summaries / receipts / checkpoints
→ separate read-only live monitor
→ Codex does not own or poll the long-lived orchestration loop
```

The worker and monitor are separate failure domains. Monitor failure must not terminate, retry, accept, advance, or corrupt the worker.

## Codex model policy

Owner-selected current default for high-value agentic coding work:

```text
MODEL=gpt-6-astra
REASONING=xhigh
```

This is an owner workflow selection, not an Agentic Matrix superiority claim. Future matched evidence may change the default.

## Proven GPT-6 Astra transport profile

On Codex CLI 0.153.1, LAPIS isolated probe `LAPIS_ASTRA_ISOLATED_MODEL_PATH_PROBE_071` established that `gpt-6-astra` works through an isolated Codex configuration. The reliable execution family used by the successful successor was:

```text
codex exec
--ignore-user-config
--ignore-rules
--ephemeral
-C <repository-root>
--sandbox <mode>
--model gpt-6-astra
-c model_reasoning_effort="xhigh"
--output-last-message <file>
--color never
<PROMPT-AS-POSITIONAL-ARGUMENT>
```

For detached/local controllers, stdin may be `DEVNULL`; do not depend on a TTY unless a probe has established that exact controller environment.

The successful transport intentionally avoided using JSON/stdin as the only result channel after prior no-op behavior. Raw/event-stream instrumentation may be added for telemetry only if it is proven not to destabilize the execution transport.

## Result-channel law

- Prompts should use an explicitly tested transport.
- Final model output must have a deterministic durable result channel, such as `--output-last-message`.
- Shell functions used inside command substitution must not contaminate stdout with receipts, diagnostics, or JSON that callers expect to be a path/value only.
- Controller diagnostics belong in explicit files or stderr, not overloaded return channels.

## Model-call budget law

Freeze a call budget that covers the **longest authorized causal path**, not the expected happy path.

For a standard implementation/review loop, reserve at least:

```text
IMPLEMENTATION
SEMANTIC_REVIEW
OPTIONAL_BOUNDED_REPAIR
MANDATORY_REREVIEW_AFTER_REPAIR
```

If a second repair is authorized, reserve the corresponding final rereview as well. Unused reserve capacity is not a failure and does not count as consumed model spend.

Do not consume candidate model budget for controller, evaluator, environment, transport, or instrumentation failures.

## Failure-classification law

Separate at minimum:

- candidate implementation defect;
- semantic-review finding;
- controller/harness defect;
- evaluator/test-expectation defect;
- model-transport/infrastructure defect;
- environment/toolchain defect;
- authority/gate failure;
- evidence-contract defect;
- instrumentation/telemetry defect;
- genuine task failure.

A controller or evaluator defect does not establish a candidate defect.

## Evidence-identity law

Evidence bindings must identify both **artifact role and content identity**. Do not substitute the hash of one artifact class for another merely because they were produced in the same run.

Historical LAPIS example: a corrected evaluator log SHA was mistakenly used as the expected SHA for the evaluator Python source. The controller correctly blocked, but the defect was the controller's evidence-role binding, not the candidate.

Before consequential execution, validate required evidence files by:

- expected path/role;
- type/schema where applicable;
- content hash;
- source/run identity;
- required fields.

## Reconciliation-record law

Validate reconciliation/acceptance records against the repository-native contract **before** spending model calls or mutating candidate code.

Required structured fields must be present. Historical LAPIS example: a preview reconciliation record omitted required `evidence_identities`, and `lapis-ops reconcile --dry-run` correctly failed closed before model spend.

Always:

```text
construct record
→ contract/schema validation where available
→ lapis-ops reconcile --dry-run
→ inspect expected after-state
→ apply only when authority permits
```

Generated Sources 00/02/13 remain generated views; never repair reconciliation by manually rewriting them.

## Admission law

Before candidate model spend establish the minimum sufficient facts:

- repository/project identity;
- controlling instructions/AGENTS;
- current canonical phase/gate;
- expected HEAD/worktree state;
- environment/toolchain;
- authority/prohibitions;
- frozen donor/baseline identities where applicable;
- controller/evaluator identities;
- model-call budget;
- stop boundary;
- telemetry evidence path.

A deterministic Gate-0 self-test should verify the controller itself can represent the authorized path.

## Scope law

After each writable model call, independently verify:

- branch/HEAD/ref invariants when Git mutation is prohibited;
- no staging unless authorized;
- allowed writable paths only;
- frozen donor/reference integrity;
- generated-state boundary;
- original external/reference repositories remain untouched;
- prohibited project/provider/network/secret/production/Trinity actions remain absent.

## Verification law

Use deterministic verification before semantic review when feasible. A model reviewer complements deterministic checks; it does not replace them.

After bounded repair:

```text
scope check
→ deterministic verification
→ independent semantic rereview
```

Do not treat repair completion as review acceptance.

## Telemetry integration

All new governed controllers must implement `AGENTIC_LIVE_TELEMETRY_STANDARD_V1.md` and `AGENTIC_TOKEN_ATTRIBUTION_STANDARD_V1.md` before the first candidate model call unless a controlling project source explicitly defers them.

The controller must preserve:

- raw token events when available;
- live telemetry snapshot;
- prompt/context component manifest;
- per-call receipts;
- cumulative summary;
- token attribution/waste signals;
- separate read-only terminal monitor.

Missing telemetry is missing evidence, not zero usage.

## Operator monitor

The default terminal monitor should use the owner-approved compact `AGENTIC RUN` panel from the live telemetry standard, with an optional `TOKEN DRIVERS` panel from the token-attribution standard.

The monitor should make long calls visibly alive through elapsed time and native usage updates without streaming noisy model prose into the operator terminal.

## Stop law

Stop when:

- authority is absent;
- current source/gate identity conflicts;
- controller cannot represent the authorized causal path;
- required evidence identity is unresolved;
- deterministic verification fails without an authorized bounded repair;
- semantic rereview remains non-PASS after the authorized repair budget;
- security/privacy/licensing/sovereignty boundaries would be crossed;
- an owner visual/irreversible decision checkpoint is reached.

Never manufacture work merely because reserve call capacity remains.