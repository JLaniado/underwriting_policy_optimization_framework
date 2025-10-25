#!/usr/bin/env python3
"""Create a lean CSV containing only the columns needed to evaluate the rules.

Assumptions:
- Source data file: `risk_analytics_case_2025.csv` at repo root.
- Rules live in `clean_rules.md` and contain rule expressions in backticks, e.g. `1. `col <= 5 & other > 3``.

This script extracts column identifiers referenced in the rules, ensures `acquisition_uw_score`
and `is_fpd` are included, reads the source CSV, keeps all rows but only the needed columns,
and writes the result to `outputs/fpd_rule_mining/lean_rule_features.csv`.
"""
from pathlib import Path
import re
import pandas as pd
import sys

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "risk_analytics_case_2025.csv"
RULES_FILE = ROOT / "clean_rules.md"
OUT_FILE = ROOT / "sanity_check" / "lean_rule_features.csv"


def extract_rule_strings(md_text: str):
    # Prefer numbered rule format: lines like '1. `rule here`'
    rules = re.findall(r"^\d+\.\s+`(.+?)`", md_text, flags=re.MULTILINE)
    if rules:
        return rules
    # Fallback: any backtick-enclosed snippet
    return re.findall(r"`([^`]+)`", md_text)


def extract_columns_from_rule(rule: str):
    cols = set()
    # Match comparisons like col <= 5, col > 3, col == 1
    cols.update(re.findall(r"([A-Za-z_][A-Za-z0-9_]*)\s*(?:<=|>=|==|!=|<|>)", rule))
    # Match `col in [..]` or `col not in [...]`
    cols.update(re.findall(r"([A-Za-z_][A-Za-z0-9_]*)\s+in\s+", rule))
    # Match bracketed/existence patterns like df['col'] or df.col (very simple)
    cols.update(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\[['\"]([A-Za-z_][A-Za-z0-9_]*)['\"]\]", rule))
    cols.update(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\.([A-Za-z_][A-Za-z0-9_]*)\b", rule))
    return cols


def main():
    if not DATA_FILE.exists():
        print(f"ERROR: Data file not found: {DATA_FILE}")
        sys.exit(2)
    if not RULES_FILE.exists():
        print(f"ERROR: Rules file not found: {RULES_FILE}")
        sys.exit(2)

    md = RULES_FILE.read_text(encoding="utf-8")
    rule_strs = extract_rule_strings(md)
    if not rule_strs:
        print("Warning: no rule strings found in clean_rules.md. No columns will be extracted.")

    cols = set()
    for r in rule_strs:
        cols.update(extract_columns_from_rule(r))

    # Always keep these
    required = {"acquisition_uw_score", "is_fpd"}
    cols.update(required)

    # Read data and keep intersection with actual columns
    df = pd.read_csv(DATA_FILE)
    available = set(df.columns)
    keep = [c for c in cols if c in available]
    missing = sorted(list(cols - set(keep)))

    if not keep:
        print("No matching columns found in data. Exiting without writing.")
        sys.exit(3)

    # Ensure output directory exists
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Save subset (keep original row order)
    df.loc[:, keep].to_csv(OUT_FILE, index=False)

    print("Wrote lean CSV:", OUT_FILE)
    print(f"Columns kept ({len(keep)}): {sorted(keep)}")
    if missing:
        print(f"Columns referenced in rules but missing from data ({len(missing)}): {missing}")


if __name__ == "__main__":
    main()
