# Clean Rules

Final rules ready for A/B test:
1. `acquisition_uw_score <= 0.838233 & acquisition_uw_score <= 0.689887 & acquisition_uw_score <= 0.597289 & acquisition_channel_source_b <= 0.500000 & acquisition_uw_score <= 0.491564`
2. `acquisition_uw_score <= 0.838233 & acquisition_uw_score <= 0.689887 & acquisition_uw_score <= 0.597289 & acquisition_channel_source_b <= 0.500000 & acquisition_uw_score > 0.491564`
3. `acquisition_uw_score <= 0.838233 & acquisition_uw_score > 0.689887 & apps_installed_count_missing > 0.500000 & hotspots_overdue_ratio > 0.184984 & acquisition_uw_score <= 0.782922`
4. `acquisition_uw_score <= 0.838233 & acquisition_uw_score <= 0.689887 & acquisition_uw_score <= 0.597289 & acquisition_channel_source_b > 0.500000`
5. `acquisition_uw_score <= 0.838233 & acquisition_uw_score <= 0.689887 & acquisition_uw_score > 0.597289 & phone_carrier_te > 0.245457`
6. `acquisition_uw_score <= 0.838233 & acquisition_uw_score > 0.689887 & apps_installed_count_missing <= 0.500000 & removed_app_between_first_loan_and_first_due_date > 0.500000`
7. `acquisition_uw_score > 0.838233 & removed_app_between_first_loan_and_first_due_date > 0.500000 & acquisition_uw_score <= 0.909486 & credits_tc_limite_credito > 15215.500000`
8. `acquisition_uw_score <= 0.838233 & acquisition_uw_score <= 0.689887 & acquisition_uw_score > 0.597289 & phone_carrier_te <= 0.245457 & credits_total_credito_maximo <= 75910.000000`
9. `acquisition_uw_score > 0.838233 & removed_app_between_first_loan_and_first_due_date > 0.500000 & acquisition_uw_score <= 0.909486 & credits_tc_limite_credito <= 15215.500000 & bureau_1_credit_lines_past_due > 1.500000`
10. `acquisition_uw_score <= 0.838233 & acquisition_uw_score > 0.689887 & apps_installed_count_missing > 0.500000 & hotspots_overdue_ratio > 0.184984 & acquisition_uw_score > 0.782922`