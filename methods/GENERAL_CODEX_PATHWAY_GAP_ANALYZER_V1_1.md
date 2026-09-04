# General Codex Pathway / Gap Analyzer V1.1

**Role:** observational and advisory  
**Authority:** none

## Pathway

```text
OBJECTIVE
→ PROJECT/WORKTREE IDENTITY
→ AUTHORITY
→ TASK INPUT CLASS
→ CONTEXT
→ ROUTING
→ SKILL LOAD
→ CODEX REASONING
→ IMPLEMENTATION OR NO-OP
→ HOST CONTROLLER
→ VALIDATION
→ REVIEW
→ ACCEPTANCE
→ RECEIPT
```

## Minimum telemetry

```text
RUN_ID
COHORT_ID
REPOSITORY_ID
TASK_ID
TASK_CLASS
INITIAL_STATE_SHA
WORKTREE_OR_SNAPSHOT_SHA
MODEL_AND_VERSION
REASONING_EFFORT
CONFIG_SHA
HOOKS_SHA
AGENTS_SHA_SET
ROUTER_ID_AND_SHA
ROUTING_POLICY_AND_DECISION
SELECTED_SKILLS_AND_HASHES
AUTHORITY_MODE
CODEX_ACTIVE_SECONDS
HOST_COMPUTE_SECONDS
WALL_SECONDS
QUEUE_DELAY_SECONDS
INPUT_TOKENS
CACHED_INPUT_TOKENS
OUTPUT_TOKENS
REASONING_TOKENS
COMMAND_EVENTS
FILE_CHANGE_EVENTS
RETRIES
OPERATOR_ACTIVE_SECONDS
OPERATOR_INTERRUPTION_TYPES
TEST_RESULTS
REVIEW_RESULTS
HARD_VIOLATIONS
ACCEPTANCE_STATE
ARTIFACT_MANIFEST_SHA
```

Missing telemetry is `UNKNOWN`.

## Primary cause classes

```text
PROJECT_IDENTITY_OR_WORKTREE
ENVIRONMENT_MODULE_ENTRYPOINT
FIXTURE_OR_RUNTIME_CONTROL
INSTRUMENT_OR_HARNESS
CAUSAL_STAGE_OR_VERDICT_SCOPE
SEMANTIC_VS_AUDIT_IDENTITY
CASE_BOUND_VS_GENERICITY
REPAIR_PROPAGATION
PREEXISTING_BASELINE
SOURCE_OR_EVIDENCE_DRIFT
HUMAN_JUDGMENT_REQUIRED
DETERMINISTIC_SCRIPT
HOST_CONTROLLER
AGENTS_OR_CONFIG
CONTEXT_ROUTING
EXISTING_SKILL
MISSING_SKILL
TEST_OR_EVALUATOR
PROMPT_OR_TASK_COMPILE
MODEL_REASONING_MODE
REVIEW_POLICY
SUBAGENT_POLICY
AUTHORITY_CONTRACT
UNKNOWN
```

## Deterministic signals

Immediate:
- authority/security violation;
- wrong repo/worktree/snapshot;
- invalid fixture/control/instrument/evaluator;
- long work left in a Codex-owned wait/poll;
- holdout contamination.

Efficiency:
- unchanged rereads;
- blind retries without new evidence;
- repeated polling;
- unnecessary skill/context load;
- SSS invoked when escalation gate is false;
- compiler invoked on bounded contract;
- duplicate validation/review without predicted unique value.

Quality:
- upstream causal failure blamed on downstream mechanism;
- diagnostic repair not propagated to executed artifact;
- audit metadata variance mistaken for semantic variance;
- case-bound code given generic credit;
- preexisting failure attributed to candidate patch;
- deterministic checks used where human judgment is required.

## Gap status

```text
SINGLE_OBSERVATION
REPEATED_GAP_HYPOTHESIS
GENERALIZATION_CANDIDATE
PREREGISTERED_IMPROVEMENT_HYPOTHESIS
CONFIRMED_BOUNDED_IMPROVEMENT
REJECTED_HYPOTHESIS
INCONCLUSIVE
```

## Remedy hierarchy

```text
1. project/worktree/source identity
2. fixture/runtime control
3. instrument/harness/evaluator
4. repair propagation
5. deterministic script/check
6. host controller
7. repository-native validation
8. AGENTS/config/rule
9. context/routing correction
10. existing skill
11. prompt/task compiler
12. review/subagent policy
13. model reasoning mode
14. MISSING_SKILL
15. broader architecture
```

Internet skill search is forbidden until `MISSING_SKILL` is justified.

## Gap record

```text
GAP_ID
EVIDENCE_IDS
REPOSITORIES
TASK_CLASSES
FREQUENCY
PRIMARY_CAUSE_CLASS
SECONDARY_CAUSE_CLASSES
QUALITY_IMPACT
AUTHORITY_SECURITY_IMPACT
TOKEN_IMPACT
CODEX_ACTIVE_TIME_IMPACT
WALL_TIME_IMPACT
OPERATOR_ATTENTION_IMPACT
LOWEST_COMPLEXITY_REMEDY
EXPECTED_MECHANISM
TESTABLE_PREDICTION
MPID
OVERFITTING_RISK
SEARCH_REQUIRED
STATUS
```

Do not create a large gap record for every trivial single anomaly.

## Missing-skill ladder

```text
1. frozen runtime-visible skills
2. trusted installed local capabilities
3. official OpenAI plugin/skill sources
4. primary vendor repositories
5. trusted GitHub targeted search
6. broader targeted web search
7. create local candidate only if necessary
8. provenance/security/license/script review
9. structural validation
10. matched targeted comparison
11. holdout/cross-repository confirmation
12. PROMOTE | REJECT | INCONCLUSIVE
```

## Skill-miner boundary

`skill-miner-workflow-compiler` is secondary hypothesis generation after repeated deterministic gap evidence. It cannot install, create, or promote by itself.

## Anti-self-acceptance

The analyzer may not:
- expand authority;
- alter evaluator or holdout membership mid-cohort;
- install skills;
- mutate production;
- promote its own recommendation;
- hide negative evidence;
- reclassify harness failure as candidate failure for convenience.
