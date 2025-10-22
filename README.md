🧭 Credit Policy Optimization Framework

Private Repository — Internal Use Only

This repository contains a proposed slution for Nelo's Credit Risk business case. Goal is to show the ability to identify, test, and monitor rules that reduce First Payment Default (FPD) while maintaining healthy approval rates.

The framework combines statistical rigor, interpretability, and operational scalability to support data-driven credit-policy adjustments. It was built as a reusable, parameter-free system that can be applied across portfolios, seasons, and product types.

⸻

📌 Purpose

The goal of this project is to enable the systematic discovery and evaluation of credit rules that balance growth and risk.
Rather than running ad-hoc analyses, the framework provides a consistent, repeatable process to:
	•	Detect pockets of elevated default or fraud risk.
	•	Quantify the trade-off between risk reduction and applicant retention.
	•	Translate model outputs into interpretable business rules ready for testing or deployment.

⸻

🔍 Summary of Approach
	1.	Data preparation
	•	Cleans and validates raw application-level data.
	•	Flags missing values (presence or absence as information).
	•	Encodes categorical variables via one-hot or target encoding.
	•	Creates standardized risk bands from the underwriting score to enable peer-group analysis.
	2.	Feature exploration
	•	Computes variable correlation to FPD overall and per risk band.
	•	Identifies high-signal numerical and categorical variables.
	3.	Rule discovery
	•	Trains a shallow Decision Tree Classifier to segment pre-application populations.
	•	Translates each leaf into a plain-language rule (e.g., acquisition_uw_score <= 0.597 & apps_installed_count < 360).
	•	Ranks rules by efficiency (FPD reduction per % of population removed).
	4.	Impact assessment
	•	Applies rules individually and cumulatively.
	•	Measures changes in:
	•	Overall and per-band FPD
	•	Approval rate (kept %)
	•	Good vs. bad volume composition
	•	Produces ready-to-use metrics and visual reports.
	5.	Visualization suite
	•	Trade-off curves — FPD vs. applicants removed.
	•	Single-rule impact — marginal and cumulative effects.
	•	Waterfall charts — absolute and relative volume changes.
	•	Purity analysis — quality of removed population.
	•	FPD by band — distributional stability check.

⸻

📊 Example Outcome

Metric	Baseline	After Rules	Δ
Overall FPD	25.0 %	22.9 %	↓ 2.1 p.p.
Applicants Kept	100 %	93.0 %	↓ 7 p.p.
Bad Accounts	45,615	38,804	-6,811
Good Accounts	136,847	130,913	-5,934

The framework’s six recommended rules target the lowest-score bands and segments showing high utilization or weak carrier profiles, achieving measurable improvement with minimal volume loss.

⸻

🧠 Design Philosophy

This project was built as a sandbox with production intent — balancing exploratory flexibility with engineering discipline:
	•	Fully automated notebook: click-to-run with no hardcoded variables.
	•	Parameterization: adaptable to any dataset following the same schema.
	•	Code readability: each function self-contained for review or audit.
	•	Infrastructure-ready: designed for future deployment in batch or API format.

The approach reflects a long-term view of risk analytics — favoring transparency, reusability, and governance readiness over one-off modeling.

⸻

⚙️ Repository Structure

/fpd_rule_mining.ipynb        → Main analysis notebook  
/data/                         → Raw input and interim CSVs  
/outputs/                      → Leaf summaries, stage metrics, and charts  
clean_rules.md                 → Final rule set (ready for A/B testing)  
metrics.json                   → Global KPIs and performance metrics  


⸻

🧩 How to Reuse
	1.	Update the file path in the configuration cell (FILEPATH = ...).
	2.	Run all cells sequentially in Jupyter.
	3.	Review generated outputs:
	•	leaf_summary.csv for rule details.
	•	single_rule_impact.csv for marginal results.
	•	cumulative_stages.csv for progressive impact.
	•	Exported visuals under /outputs/.
	4.	Use clean_rules.md as the baseline for policy simulation or A/B testing.

⸻

🔒 Access and Governance
	•	Classification: Confidential
  
⸻

🧭 Next Steps
	•	Extend framework to expected-loss (ECL) and profitability analysis.
	•	Add temporal validation and drift detection.
	•	Integrate a lightweight dashboard for ongoing monitoring.
	•	Link directly to the underwriting API for simulation of rule deployment.

⸻

Author: Jaime Laniado Cohen
Owner: Jaime Laniado Cohen
Repository: Private

⸻
