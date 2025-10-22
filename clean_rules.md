# Clean Rules

Final rules ready for A/B test:
1. `acquisition_uw_score <= 0.838233 & acquisition_uw_score <= 0.689887 & acquisition_uw_score <= 0.597289 & acquisition_uw_score <= 0.516786`
2. `acquisition_uw_score <= 0.838233 & acquisition_uw_score <= 0.689887 & acquisition_uw_score <= 0.597289 & acquisition_uw_score > 0.516786`
3. `acquisition_uw_score <= 0.838233 & acquisition_uw_score > 0.689887 & apps_installed_count_missing > 0.500000 & acquisition_uw_score <= 0.808913`
4. `acquisition_uw_score <= 0.838233 & acquisition_uw_score <= 0.689887 & acquisition_uw_score > 0.597289 & phone_carrier_te > 0.233899`
5. `acquisition_uw_score <= 0.838233 & acquisition_uw_score <= 0.689887 & acquisition_uw_score > 0.597289 & phone_carrier_te <= 0.233899`
6. `acquisition_uw_score <= 0.838233 & acquisition_uw_score > 0.689887 & apps_installed_count_missing > 0.500000 & acquisition_uw_score > 0.808913`
7. `acquisition_uw_score <= 0.838233 & acquisition_uw_score > 0.689887 & apps_installed_count_missing <= 0.500000 & acquisition_uw_score <= 0.785268`
8. `acquisition_uw_score > 0.838233 & acquisition_uw_score <= 0.917851 & phone_carrier_te > 0.271224 & acquisition_uw_score <= 0.878581`
9. `acquisition_uw_score <= 0.838233 & acquisition_uw_score > 0.689887 & apps_installed_count_missing <= 0.500000 & acquisition_uw_score > 0.785268`