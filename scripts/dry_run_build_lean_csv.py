#!/usr/bin/env python3
"""Dry-run: load data and rules, attempt to build phone_carrier_te, and write a lean CSV.

This simulates the notebook bottom-cell logic in a standalone script and prints diagnostics.
"""
from pathlib import Path
import re
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "risk_analytics_case_2025.csv"
RULES_FILE = ROOT / "clean_rules.md"
OUT_FILE = ROOT / "outputs" / "fpd_rule_mining" / "lean_rule_features_dryrun.csv"


def extract_rule_strings(md_text: str):
    rules = re.findall(r"^\d+\.\s+`(.+?)`", md_text, flags=re.MULTILINE)
    if rules:
        return rules
    return re.findall(r"`([^`]+)`", md_text)


def extract_columns_from_rule(rule: str):
    cols = set()
    cols.update(re.findall(r"([A-Za-z_][A-Za-z0-9_]*)\s*(?:<=|>=|==|!=|<|>)", rule))
    cols.update(re.findall(r"([A-Za-z_][A-Za-z0-9_]*)\s+in\s+", rule))
    cols.update(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\[['\"]([A-Za-z_][A-Za-z0-9_]*)['\"]\]", rule))
    cols.update(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\.([A-Za-z_][A-Za-z0-9_]*)\b", rule))
    return cols


def frequency_encode(series: pd.Series) -> pd.Series:
    freq = series.fillna("__MISSING__").astype(str).value_counts(normalize=True)
    return series.fillna("__MISSING__").astype(str).map(freq).astype(float)


def cross_fitted_target_encode(series: pd.Series, target: pd.Series, n_splits=5, alpha=200.0, random_state=42):
    # Lightweight implementation similar to notebook's
    from sklearn.model_selection import KFold
    series = pd.Series(series, copy=False).astype(object)
    target = pd.Series(target).astype(float)
    global_mean = target.mean()
    encoded = pd.Series(index=series.index, dtype=float)
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    for train_idx, valid_idx in kf.split(series):
        train_series = series.iloc[train_idx]
        train_target = target.iloc[train_idx]
        stats = train_target.groupby(train_series).agg(["sum", "count"])
        smooth = (stats["sum"] + alpha * global_mean) / (stats["count"] + alpha)
        enc_map = smooth.to_dict()
        encoded.iloc[valid_idx] = series.iloc[valid_idx].map(enc_map).fillna(global_mean)
    return encoded.fillna(global_mean)


def main():
    if not DATA_FILE.exists():
        print(f"ERROR: data file not found: {DATA_FILE}")
        sys.exit(2)
    if not RULES_FILE.exists():
        print(f"WARNING: rules file not found: {RULES_FILE} -- proceeding with minimal columns.")

    df = pd.read_csv(DATA_FILE)
    md_text = RULES_FILE.read_text(encoding="utf-8") if RULES_FILE.exists() else ""
    rule_strs = extract_rule_strings(md_text) if md_text else []

    cols = set()
    for r in rule_strs:
        cols.update(extract_columns_from_rule(r))

    required = {"acquisition_uw_score", "is_fpd"}
    cols.update(required)

    available = set(df.columns)
    present = sorted([c for c in cols if c in available])
    missing = sorted(list(cols - set(present)))

    print("Columns referenced by rules:", sorted(cols))
    print("Available in data:", present)
    print("Missing from data:", missing)

    # Attempt to build phone_carrier_te if missing but referenced
    if "phone_carrier_te" in cols and "phone_carrier_te" not in df.columns:
        print("Attempting to build phone_carrier_te...")
        candidates = ["phone_carrier", "phone_carrier_cat", "phone_carrier_raw"]
        found = next((c for c in candidates if c in df.columns), None)
        if not found:
            print("No raw phone carrier column found among candidates:", candidates)
        else:
            print("Found raw phone carrier column:", found)
            try:
                enc = cross_fitted_target_encode(df[found], df["is_fpd"], n_splits=5, alpha=200.0, random_state=42)
                df["phone_carrier_te"] = enc
                print("Built phone_carrier_te via cross-fold target encoding; adding to present list.")
            except Exception as e:
                print("cross_fitted_target_encode failed:", e)
                print("Falling back to frequency_encode")
                df["phone_carrier_te"] = frequency_encode(df[found]).fillna(0)

    # Recompute present
    present = sorted([c for c in cols if c in df.columns])
    missing = sorted(list(cols - set(present)))
    print("Final present columns to write:", present)
    print("Final missing columns:", missing)

    # Write CSV
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.loc[:, present].to_csv(OUT_FILE, index=False)
    print("Wrote dry-run CSV:", OUT_FILE)


if __name__ == "__main__":
    main()
