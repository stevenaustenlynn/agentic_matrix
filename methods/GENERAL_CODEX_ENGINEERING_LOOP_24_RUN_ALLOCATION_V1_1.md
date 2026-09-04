# Exact Stage-A 24-Run Allocation V1.1

**Execution authority:** `NOT_GRANTED`

## Arithmetic

```text
ROUTING_SCREEN=12
SENTINEL_REPLICATION=4
HOLDOUT_CONFIRMATION=4
REVIEW_DETECTION=4
TOTAL=24
```

## Runs 1–12: routing screen

Three frozen development cases:

```text
D1_VECTORIZE_RAW_AMBIGUOUS × P0/P1/P2/P3 = 4
D2_LAPIS_BOUNDED_CONTRACT × P0/P1/P2/P3  = 4
D3_NEUTRAL_A_ENGINEERING × P0/P1/P2/P3   = 4
TOTAL=12
```

D1 must be a positive compiler class.  
D2 must be a compiler negative-control class.  
D3 must exercise ordinary engineering without assuming Steven-style governance.

## Runs 13–16: sentinel

```text
S1_DECISION_SENSITIVE_SENTINEL × P0/P1/P2/P3 = 4
```

Then mandatory owner checkpoint.

## Runs 17–20: holdout

```text
H1_NEUTRAL_B × P0/WINNER = 2
H2_UNTOUCHED_OTHER_CLASS × P0/WINNER = 2
TOTAL=4
```

No holdout reuse after outcome-driven changes.

## Runs 21–24: review detection

```text
RCASE1_FROZEN_DIFF × R0/R1 = 2
RCASE2_FROZEN_DIFF × R0/R1 = 2
TOTAL=4
```

R0 = deterministic validation only.  
R1 = same validation + read-only review-agent.  
No fixes in either arm.

## Winner selection after run 16

1. eliminate hard-constraint failures not caused by invalid infrastructure;
2. prefer higher accepted quality;
3. reject routes dominated by simpler routes;
4. require MPID-sized efficiency improvement before promoting added complexity;
5. if tied/inconclusive, prefer simpler route;
6. if nothing beats P0 materially, P0 becomes the holdout comparator/winner.

## Randomization

Freeze one seed before run 1 and randomize policy order within each task block. Record cache and queue conditions separately.

## Stage-B boundary

No automatic run 25. Runs 25–36 require a new owner-approved preregistration.
