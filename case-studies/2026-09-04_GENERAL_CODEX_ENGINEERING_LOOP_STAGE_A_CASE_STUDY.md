# Case Study — General Codex Engineering Loop Stage A

**Date:** 2026-09-04  
**Case-study ID:** `AGENTIC_MATRIX_2026_09_04_STAGE_A_001`  
**Experiment:** `GENERAL_CODEX_ENGINEERING_LOOP_V1_1`  
**Cohort:** `GENERAL_CODEX_STAGE_A_001`  
**Classification:** `SOURCE_DERIVED` from frozen preregistration, checkpoint evidence, unit evidence, final artifact identities, and the accepted final project handoff.

## Objective

Determine whether conditional prompt compilation, deep state/skill escalation, or a deterministic host router could materially outperform the owner's actual Codex engineering workflow while preserving quality and authority; separately test whether a read-only review agent could detect defects missed by deterministic validation.

The desired workflow was higher or equal quality with lower token spend, Codex-active time, retries, and owner attention, without adding complexity that did not earn its cost.

## Frozen baseline

P0 was the actual workflow, not a weakened control:

```text
Codex CLI 0.153.1
model=gpt-5.6-sol
reasoning=xhigh
sandbox=workspace-write
approval=on-request
existing hooks/plugins/goals
current global/project AGENTS
```

No OpenAI API workflow was used.

## Policies

- `P0`: exact current runtime baseline.
- `P1`: conditional `codex-prompt-compiler`.
- `P2`: conditional `sss-universal` escalation.
- `P3`: deterministic host-side router.
- `R0`: deterministic validation only.
- `R1`: deterministic validation plus read-only `review-agent`.

Macroscope, remediation/autoloop, and HIGH-vs-XHIGH were deliberately excluded from Stage A.

## Allocation

```text
D1_VECTORIZE_RAW_AMBIGUOUS × P0/P1/P2/P3 = 4
D2_LAPIS_BOUNDED_CONTRACT  × P0/P1/P2/P3 = 4
D3_NEUTRAL_A               × P0/P1/P2/P3 = 4
S1_SENTINEL                × P0/P1/P2/P3 = 4
H1_NEUTRAL_B               × P0/WINNER    = 2
H2_OTHER_HOLDOUT            × P0/WINNER    = 2
RCASE1                      × R0/R1        = 2
RCASE2                      × R0/R1        = 2
TOTAL                                         24
```

The completed cohort used **24/24 experimental units and 22/22 model calls with 0 experimental reruns**.

## Development + sentinel results

| Policy | Quality | Active-time median | Token median | Decision |
|---|---:|---:|---:|---|
| P0 | 4/4 | 45.472 s | 138,667 | retained |
| P1 | 3/4 | 61.407 s | 162,715 | not promoted |
| P2 | 4/4 | 56.013 s | 179,703.5 | not promoted |
| P3 | 4/4 | 63.483 s | 161,076.5 | not promoted |

The only development/sentinel hard quality failure was `S1_SENTINEL` under P1: workspace quality failed even though final-response evaluation passed. P1 was faster and lower-token than P0 on that case, but the quality regression made the efficiency gain non-promotable.

Examples of relative results:

- D1 raw/ambiguous: every P1/P2/P3 route cost more active time than P0; P1 +55.94%, P2 +64.90%, P3 +73.53%.
- D2 bounded contract: P2 was 22.88% faster and 2.76% lower-token than P0 on this case, but this isolated case did not establish a general promotion.
- D3 neutral-A: P3 used 13.87% fewer tokens than P0 but took 36.48% more active time.
- S1 sentinel: P1 used 39.69% fewer tokens and 27.02% less active time than P0 but failed workspace quality; P2 and P3 preserved quality but were slower and higher-token than P0.

Under the preregistered promotion law, no added routing complexity materially beat the simpler baseline. The routing result was:

```text
ROUTING_WINNER=P0_BY_NON_PROMOTION
P1_PROMOTED=NO
P2_PROMOTED=NO
P3_PROMOTED=NO
GENERAL_ROUTER_PROMOTED=NO
```

This is a substantive result: the experiment rejected the assumption that more routing/skill machinery would necessarily improve the engineering loop.

## Holdout

Because P0 won by non-promotion, the `WINNER` holdout arm was also P0. Both P0 and winner arms passed on both holdout classes.

H1 Neutral-B:
- P0: 65.385 s Codex-active, 170,676 total tokens.
- WINNER/P0: 49.075 s, 163,462 tokens.

H2 correct-stop holdout:
- WINNER/P0: 13.918 s, 19,672 tokens.
- P0: 11.126 s, 19,383 tokens.

`HOLDOUT_COMPLETE=YES`. The holdout supports the non-promotion decision; it is not evidence that P0 is universally superior.

## Review detection arm

Two frozen defective diffs were tested with no remediation:

```text
R0 = deterministic validation only
R1 = deterministic validation + read-only review-agent
```

Aggregate adjudication:

```text
REVIEW_R0=TP0 FP0 FN2
REVIEW_R1=TP2 FP0 FN0
```

R1 model costs:
- RCASE1: 32.674 s, 81,952 total tokens.
- RCASE2: 34.382 s, 83,102 total tokens.

The review-agent detected both hidden defects in this N=2 study while deterministic validation detected neither. This is **bounded promise**, not a global promotion:

```text
GLOBAL_REVIEW_SUPERIORITY_CLAIM=NO
```

A later study should expand defect classes and quantify operator/review cost before making review mandatory.

## Aggregate measured model usage

Across the 22 model-call units represented in preserved unit evidence:

```text
TOTAL_TOKENS=3,458,207
INPUT_TOKENS=3,347,321
CACHED_INPUT_TOKENS=2,780,288
OUTPUT_TOKENS=70,475
REASONING_TOKENS=40,411
CODEX_ACTIVE_SECONDS=1628.586
```

These totals describe the experiment evidence; they are not a cost-normalized business metric.

## Infrastructure incident and recovery

After units 17–24 had durably completed, the postcheckpoint worker exited with:

```text
NON_CONFIG_GATE0_FAILURE:candidate_identity
```

The failure occurred during post-execution admission/finalization, not during any experimental unit. Durable evidence showed all units 17–24 complete and no rerun was performed. This was classified as infrastructure rather than candidate failure. Stage-A completion artifacts were subsequently finalized without rerunning experimental units.

This incident is important to preserve because it demonstrated the value of:
- host-owned durable checkpoints;
- infrastructure-vs-candidate failure classification;
- no hidden reruns;
- content-addressed finalization.

## Final accepted outcome

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

## Durable final artifact identities

```text
stage-a-complete.json
sha256=9e5b901587c12a23b3053bbf325c11ed6cbd49b3fe05c3df8110e9fc7456c6f2

stage-a-final-report.json
sha256=aaca39eb939ddf1f6dd5a00a5c44a399196eefefb6ca03857d17349decaafa25

stage-a-final-report.md
sha256=bc4699188bbfd882c7845019dbd14c18e09fa239c0c2491a7aa584af066773c2

stage-a-finalization-manifest.json
sha256=5c69a4f9adab81c6e9d98f3af3a9c0ce15c7a91751c9b8482f59ec41d1ab0f1a
```

Original local evidence root:

`~/.local/share/lapis/experiments/general-codex-engineering-loop/v1.1/runtime/stage-a-001/`

## What changed in the real engineering workflow

The experiment did not promote a general router, compiler, or SSS layer. Instead it validated a simpler operating rule:

1. use the P0 Codex baseline by default;
2. do not load a general router merely because it exists;
3. require optional complexity to earn promotion through matched evidence;
4. use a deterministic host controller for long machine work;
5. preserve durable receipts/checkpoints and separate infrastructure failures from candidate failures;
6. use independent read-only review selectively on consequential diffs as a bounded optional control, not a globally mandatory layer.

This simpler workflow was then used successfully for later LAPIS agentic implementation work in the same project.

## Relationship to ATHANOR

This experiment produced capabilities that overlap the intended ATHANOR domain:

- workflow telemetry;
- token/context accounting;
- Codex-active and wall-time measurement;
- routing-policy comparison;
- gap classification;
- host-controller receipts/checkpoints;
- evidence-bounded improvement hypotheses;
- policy promotion/non-promotion.

That overlap should be treated as seed evidence and reusable measurement design for ATHANOR, not as a reason for LAPIS to duplicate ATHANOR. Once ATHANOR is integrated, ATHANOR should own workflow observation/measurement and policy-learning evidence; LAPIS should reference ATHANOR run/evaluation identities.

The `agentic_matrix` repository remains the reusable experimental protocol and case-study archive.

## Limitations

- Small corpus.
- Routing policies were tested on four development/sentinel classes, not broad software engineering.
- Review result N=2.
- No HIGH-vs-XHIGH comparison.
- No Macroscope matched comparator.
- No Stage B.
- Operator-active-time telemetry was not complete enough to support a strong operator-burden claim.
- The study supports bounded workflow decisions, not global superiority.

## Reuse

For a future candidate skill, do not simply rerun the old policy labels. Freeze the current real workflow as a fresh P0, classify the new mechanism, construct matched arms, preserve a holdout, and use the smallest study capable of changing the decision. Store each future study as a new dated case study rather than rewriting this one.
