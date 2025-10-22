<!-- Copilot instructions for JLaniado/nelo -->
# Copilot instructions

This repository is a small risk-analytics / rule-mining analysis project built primarily as Jupyter notebooks (Python). The guidance below is focused on making AI coding agents productive quickly when editing notebooks, adding small scripts, or improving analysis reproducibility.

Quick facts
- Primary artifacts: `Streamlined_analysis.ipynb`, `fpd_rule_mining.ipynb`, `clean_rules.md`.
- Kernel / language: Python (notebooks import pandas, numpy, matplotlib, seaborn). Expect standard data-science workflows (CSV inputs, plotting, model/tree-based rule extraction).

What to edit
- Small, focused Python helpers (IO, config constants, rule-export) are preferred over large notebook rewrites. If you add new modules, place them in a top-level `src/` or `nelo/` package and keep notebook cells minimal by importing from those modules.

Useful patterns in this repo (do and follow)
- Config is defined as module-level constants in notebooks. When refactoring to scripts, preserve names: `FILEPATH`, `ID_COL`, `TARGET_COL`, `UW_SCORE_COL`, `DROP_POST_APP_COLS`, `RANDOM_SEED`, etc. Example: `fpd_rule_mining.ipynb` defines `FILEPATH = "risk_analytics_case_2025.csv"` and `ID_COL = "user_uuid"`.
- Rule export: notebook outputs human-readable leaf rules (see `Streamlined_analysis.ipynb` and `clean_rules.md`). Keep rule output format as readable boolean expressions (e.g., `acquisition_uw_score <= 0.838233 & ...`) to match downstream A/B testing steps.
- Missingness and banding: notebooks create missing-flag columns and quantile bands (`_band` suffix). When generating features, follow the same naming convention (original name + `_band` or `_missing`).

Workflows & commands
- This repo is notebook-first. Recommended local workflow:

```bash
# open the notebook in VS Code (recommended) or Colab
code .
# or
# Upload to Google Colab via the badge link in the top of each notebook
```

- If you convert portions to scripts, run them with the system Python (create a virtualenv) and install common data-science packages: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`.

Project-specific conventions
- Keep analysis reproducible by preserving the notebook-level config constants and seeding (`RANDOM_SEED = 42`).
- Filenames referenced by notebooks are relative paths (e.g., `risk_analytics_case_2025.csv`). Do not assume a specific data directory; add configurable `DATA_DIR` if creating scripts.
- Visualization style: notebooks set `PLOT_STYLE = "whitegrid"`. When creating plots programmatically, set the same style for consistency.

Integration points and assumptions
- No external CI or build scripts were found. Notebooks assume local CSV availability; if adding automated data-loading, document expected CSV column names (see variable names used in notebooks: `is_fpd`, `acquisition_uw_score`, `user_uuid`).

What not to change without author guidance
- Avoid renaming the top-level notebooks or `clean_rules.md` without discussion — they are the primary deliverables.
- Avoid changing the human-readable rule syntax format; downstream reading and A/B testing expects simple boolean expressions.

Examples to reference
- `fpd_rule_mining.ipynb` — configuration constants and pipeline parameters (MAX_DEPTH, MIN_SAMPLES_LEAF_FRAC, TEST_SIZE).
- `Streamlined_analysis.ipynb` — stepwise EDA and rule export examples; follow its data cleaning and banding steps.

If you need clarification
- Ask the repository owner which CSV(s) to use and whether they want refactors into a `src/` package and a `requirements.txt` or `environment.yml` for reproducibility.

Short checklist for edits
- Preserve notebook config constants and seeds.
- Keep rule output as boolean-expression strings.
- Add any new scripts under `src/` and expose the same configuration variable names.

If this file is out-of-date or you want a different level of guidance, reply with specific goals (e.g., "convert notebooks to scripts", "add requirements.txt", "add tests").
