# Clean Rules

Final rules ready for A/B test:
1. `acquisition_uw_score <= 0.838233 & acquisition_uw_score <= 0.689887 & acquisition_uw_score <= 0.597289 & acquisition_uw_score <= 0.516786`
2. `acquisition_uw_score <= 0.838233 & acquisition_uw_score <= 0.689887 & acquisition_uw_score <= 0.597289 & acquisition_uw_score > 0.516786`
3. `acquisition_uw_score <= 0.838233 & acquisition_uw_score > 0.689887 & apps_installed_count_missing > 0.500000 & hotspots_overdue_ratio > 0.190947 & acquisition_uw_score <= 0.810201`
4. `acquisition_uw_score <= 0.838233 & acquisition_uw_score <= 0.689887 & acquisition_uw_score > 0.597289 & phone_carrier_te > 0.233899`
5. `acquisition_uw_score <= 0.838233 & acquisition_uw_score <= 0.689887 & acquisition_uw_score > 0.597289 & phone_carrier_te <= 0.233899`
6. `acquisition_uw_score <= 0.838233 & acquisition_uw_score > 0.689887 & apps_installed_count_missing > 0.500000 & hotspots_overdue_ratio > 0.190947 & acquisition_uw_score > 0.810201`