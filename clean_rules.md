# Clean Rules

Final rules ready for A/B test:
1. `acquisition_uw_score <= 0.838233 & acquisition_uw_score <= 0.689887 & acquisition_uw_score <= 0.597289 & acquisition_uw_score <= 0.516786`
2. `acquisition_uw_score <= 0.838233 & acquisition_uw_score <= 0.689887 & acquisition_uw_score <= 0.597289 & acquisition_uw_score > 0.516786`
3. `acquisition_uw_score <= 0.838233 & acquisition_uw_score > 0.689887 & first_loan_principal > 423.479996 & first_loan_principal > 1001.600006`
4. `acquisition_uw_score <= 0.838233 & acquisition_uw_score <= 0.689887 & acquisition_uw_score > 0.597289 & phone_carrier_te > 0.233899`
5. `acquisition_uw_score <= 0.838233 & acquisition_uw_score <= 0.689887 & acquisition_uw_score > 0.597289 & phone_carrier_te <= 0.233899`
6. `acquisition_uw_score > 0.838233 & acquisition_uw_score <= 0.917851 & limit_utilization > 0.889079 & limit_utilization > 2.473115`