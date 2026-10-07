#!/usr/bin/env python3
"""Verify consistency of the public Agentic Matrix Stage-A dataset.

This script does not reproduce the original model executions. It recomputes
published aggregate metrics from the preserved per-unit CSV and checks them
against the aggregate JSON and dated public case study.
"""

from __future__ import annotations

import csv
import json
import math
import re
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "2026-09-04_STAGE_A_UNITS_001_024.csv"
JSON_PATH = ROOT / "data" / "2026-09-04_STAGE_A_METRICS.json"
CASE_STUDY_PATH = ROOT / "case-studies" / "2026-09-04_GENERAL_CODEX_ENGINEERING_LOOP_STAGE_A_CASE_STUDY.md"


def fail(message: str) -> None:
    print(f"STAGE_A_DATA_VALIDATION=FAIL\nERROR={message}", file=sys.stderr)
    raise SystemExit(1)


def as_int(value: str, field: str, unit: str) -> int | None:
    if value == "":
        return None
    try:
        return int(value)
    except ValueError as exc:
        fail(f"unit {unit}: invalid integer for {field}: {value!r}")
        raise AssertionError from exc


def as_float(value: str, field: str, unit: str) -> float | None:
    if value == "":
        return None
    try:
        return float(value)
    except ValueError as exc:
        fail(f"unit {unit}: invalid float for {field}: {value!r}")
        raise AssertionError from exc


def as_bool(value: str, field: str, unit: str) -> bool | None:
    if value == "":
        return None
    if value == "True":
        return True
    if value == "False":
        return False
    fail(f"unit {unit}: invalid boolean for {field}: {value!r}")
    return None


def close(actual: float, expected: float, label: str) -> None:
    if not math.isclose(actual, expected, rel_tol=1e-12, abs_tol=1e-9):
        fail(f"{label}: expected {expected!r}, got {actual!r}")


def exact(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        fail(f"{label}: expected {expected!r}, got {actual!r}")


def main() -> None:
    for path in (CSV_PATH, JSON_PATH, CASE_STUDY_PATH):
        if not path.is_file():
            fail(f"missing required file: {path.relative_to(ROOT)}")

    aggregate = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    case_study = CASE_STUDY_PATH.read_text(encoding="utf-8")

    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    exact(len(rows), aggregate["experimental_units"], "experimental_units")
    exact(len(rows), 24, "public Stage-A row count")

    units = [row["unit"] for row in rows]
    exact(units, [str(i) for i in range(1, 25)], "unit sequence")

    parsed = []
    for row in rows:
        unit = row["unit"]
        parsed.append(
            {
                **row,
                "model_calls_n": as_int(row["model_calls"], "model_calls", unit) or 0,
                "quality_pass_b": as_bool(row["quality_pass"], "quality_pass", unit),
                "active_seconds_n": as_float(row["active_seconds"], "active_seconds", unit),
                "wall_seconds_n": as_float(row["wall_seconds"], "wall_seconds", unit),
                "input_tokens_n": as_int(row["input_tokens"], "input_tokens", unit),
                "cached_input_tokens_n": as_int(row["cached_input_tokens"], "cached_input_tokens", unit),
                "output_tokens_n": as_int(row["output_tokens"], "output_tokens", unit),
                "reasoning_tokens_n": as_int(row["reasoning_tokens"], "reasoning_tokens", unit),
                "total_tokens_n": as_int(row["total_tokens"], "total_tokens", unit),
            }
        )

    model_calls = sum(row["model_calls_n"] for row in parsed)
    exact(model_calls, aggregate["model_calls"], "model_calls")
    exact(model_calls, aggregate["aggregate_model_usage"]["model_calls"], "aggregate model_calls")

    token_fields = (
        ("input_tokens_n", "input_tokens"),
        ("cached_input_tokens_n", "cached_input_tokens"),
        ("output_tokens_n", "output_tokens"),
        ("reasoning_tokens_n", "reasoning_tokens"),
        ("total_tokens_n", "total_tokens"),
    )
    usage = aggregate["aggregate_model_usage"]
    for parsed_name, json_name in token_fields:
        value = sum(row[parsed_name] or 0 for row in parsed)
        exact(value, usage[json_name], json_name)

    active_seconds = sum(row["active_seconds_n"] or 0.0 for row in parsed)
    wall_seconds = sum(row["wall_seconds_n"] or 0.0 for row in parsed)
    close(active_seconds, usage["codex_active_seconds"], "codex_active_seconds")
    close(wall_seconds, usage["wall_seconds"], "wall_seconds")

    dev_blocks = {
        "D1_VECTORIZE_RAW_AMBIGUOUS",
        "D2_LAPIS_BOUNDED_CONTRACT",
        "D3_NEUTRAL_A",
        "S1_SENTINEL",
    }
    dev = [row for row in parsed if row["block"] in dev_blocks]
    exact(len(dev), 16, "development_and_sentinel row count")

    for policy in ("P0", "P1", "P2", "P3"):
        policy_rows = [row for row in dev if row["arm"] == policy]
        expected = aggregate["development_and_sentinel"][policy]
        exact(len(policy_rows), expected["units"], f"{policy}.units")
        exact(
            sum(row["quality_pass_b"] is True for row in policy_rows),
            expected["quality_pass"],
            f"{policy}.quality_pass",
        )

        active = [row["active_seconds_n"] for row in policy_rows]
        tokens = [row["total_tokens_n"] for row in policy_rows]
        if any(v is None for v in active + tokens):
            fail(f"{policy}: missing active_seconds or total_tokens")
        active_f = [float(v) for v in active if v is not None]
        tokens_i = [int(v) for v in tokens if v is not None]

        close(
            statistics.median(active_f),
            expected["active_seconds_median"],
            f"{policy}.active_seconds_median",
        )
        close(min(active_f), expected["active_seconds_min"], f"{policy}.active_seconds_min")
        close(max(active_f), expected["active_seconds_max"], f"{policy}.active_seconds_max")
        close(
            float(statistics.median(tokens_i)),
            float(expected["total_tokens_median"]),
            f"{policy}.total_tokens_median",
        )
        exact(min(tokens_i), expected["total_tokens_min"], f"{policy}.total_tokens_min")
        exact(max(tokens_i), expected["total_tokens_max"], f"{policy}.total_tokens_max")

    p1_failures = [
        row["block"]
        for row in dev
        if row["arm"] == "P1" and row["quality_pass_b"] is False
    ]
    exact(
        p1_failures,
        [aggregate["development_and_sentinel"]["P1"]["hard_quality_failure"]],
        "P1 hard-quality failure",
    )

    holdout_rows = [
        row
        for row in parsed
        if row["block"] in {"H1_NEUTRAL_B", "H2_OTHER_HOLDOUT"}
    ]
    exact(len(holdout_rows), 4, "holdout row count")
    for row in holdout_rows:
        key = (
            "WINNER_P0"
            if row["arm"] == "WINNER" and row["policy"] == "P0"
            else row["arm"]
        )
        expected = aggregate["holdout"][row["block"]][key]
        close(
            float(row["active_seconds_n"]),
            expected["active_seconds"],
            f"{row['block']}.{key}.active_seconds",
        )
        exact(
            row["total_tokens_n"],
            expected["total_tokens"],
            f"{row['block']}.{key}.total_tokens",
        )
        exact(
            row["quality_pass_b"],
            expected["quality_pass"],
            f"{row['block']}.{key}.quality_pass",
        )

    review_rows = [
        row for row in parsed if row["unit_kind"] in {"review-r0", "review-r1"}
    ]
    exact(len(review_rows), 4, "review row count")
    exact(sum(row["arm"] == "R0" for row in review_rows), 2, "R0 case count")
    exact(sum(row["arm"] == "R1" for row in review_rows), 2, "R1 case count")
    exact(
        sum(row["model_calls_n"] for row in review_rows if row["arm"] == "R0"),
        0,
        "R0 model calls",
    )
    exact(
        sum(row["model_calls_n"] for row in review_rows if row["arm"] == "R1"),
        2,
        "R1 model calls",
    )

    review_pattern = re.compile(
        r"REVIEW_R(?P<arm>[01])=TP(?P<tp>\d+) FP(?P<fp>\d+) FN(?P<fn>\d+)"
    )
    case_review = {
        f"R{match.group('arm')}": {
            "true_positives": int(match.group("tp")),
            "false_positives": int(match.group("fp")),
            "false_negatives": int(match.group("fn")),
        }
        for match in review_pattern.finditer(case_study)
    }
    for arm in ("R0", "R1"):
        if arm not in case_review:
            fail(f"case study missing {arm} review adjudication")
        exact(
            case_review[arm],
            aggregate["review_detection"][arm],
            f"{arm} review adjudication",
        )

    superiority_match = re.search(
        r"GLOBAL_REVIEW_SUPERIORITY_CLAIM=(YES|NO)", case_study
    )
    if superiority_match is None:
        fail("case study missing GLOBAL_REVIEW_SUPERIORITY_CLAIM")
    exact(
        superiority_match.group(1) == "YES",
        aggregate["review_detection"]["global_review_superiority_claim"],
        "global review superiority claim",
    )

    for row in review_rows:
        if row["arm"] != "R1":
            continue
        expected = aggregate["review_detection"]["R1_cases"][row["block"]]
        close(
            float(row["active_seconds_n"]),
            expected["active_seconds"],
            f"{row['block']}.active_seconds",
        )
        exact(
            row["total_tokens_n"],
            expected["total_tokens"],
            f"{row['block']}.total_tokens",
        )

    routing = aggregate["routing_result"]
    exact(routing["winner"], "P0_BY_NON_PROMOTION", "routing winner")
    exact(routing["P1_promoted"], False, "P1 promoted")
    exact(routing["P2_promoted"], False, "P2 promoted")
    exact(routing["P3_promoted"], False, "P3 promoted")
    exact(routing["general_router_promoted"], False, "general router promoted")
    exact(routing["holdout_complete"], True, "holdout complete")
    exact(routing["stage_b_authorized"], False, "stage B authorized")

    print("STAGE_A_DATA_VALIDATION=PASS")
    print(f"UNITS={len(rows)}")
    print(f"MODEL_CALLS={model_calls}")
    print("AGGREGATES_MATCH=YES")
    print("POLICY_SUMMARIES_MATCH=YES")
    print("HOLDOUT_MATCH=YES")
    print("REVIEW_COUNTS_MATCH=YES")
    print("CASE_STUDY_REVIEW_ADJUDICATION_MATCH=YES")


if __name__ == "__main__":
    main()
