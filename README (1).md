# Workforce Attrition Patterns & Risk Hotspot Analysis

A data-driven analysis of employee attrition at Palo Alto Networks, built as part of the Unified Mentor Data Analyst Internship. The project identifies where attrition is concentrated across departments, roles, demographics, tenure, and workload factors — and delivers the findings through an interactive Streamlit dashboard.

## Live Dashboard

[Add your deployed Streamlit Cloud link here]

## Project Overview

Employee attrition carries direct costs (recruitment, onboarding) and indirect costs (lost institutional knowledge, team disruption). This project analyzes 1,470 employee records to answer:

- What is the organization's baseline attrition rate?
- Which departments and job roles are attrition hotspots?
- Do age, gender, marital status, or education correlate with attrition?
- Does tenure or time-since-last-promotion predict exit risk?
- How do workload factors (overtime, travel, commute) drive attrition?

## Key Findings

| KPI | Value |
|---|---|
| Overall Attrition Rate | 16.12% |
| Highest Attrition Department | Sales (20.63%) |
| Highest Attrition Role | Sales Representative (39.76%) |
| Early-Tenure Attrition (0–2 yrs) | 29.82% |
| **Workload Attrition Index** (OverTime + Frequent Travel) | **41.86%** |

The strongest single finding: employees who **both work overtime and travel frequently** exit at nearly **3x the organizational baseline** — the highest-risk segment identified in the entire analysis.

## Dataset

- **Source:** Palo Alto Networks employee records (`Palo_Alto_Networks.csv`)
- **Size:** 1,470 rows, 31 original fields
- **Target:** `Attrition` (1 = exited, 0 = retained)
- **Quality:** Zero duplicates, zero missing values

## Methodology

1. **Data Validation & Cleaning** — verified attrition label format, checked for duplicates/nulls, standardized categorical text
2. **Overall Attrition Assessment** — baseline turnover rate
3. **Department & Role Analysis** — group-wise attrition rates, department × role heatmap
4. **Demographic Analysis** — age group, gender, marital status, education level/field
5. **Tenure & Career Stage Analysis** — tenure buckets, promotion-gap buckets
6. **Workload & Mobility Analysis** — overtime, business travel, distance-from-home
7. **KPI Summary** — consolidated headline metrics
8. **Interactive Dashboard** — Streamlit app with live filtering

## Dashboard Modules

The Streamlit app (`app.py`) includes:

1. **Attrition Overview** — overall rate + retained vs. exited breakdown
2. **Department & Role Heatmap** — attrition intensity across the org matrix
3. **Demographic Attrition Explorer** — user-selectable breakdown (age/gender/marital/education field)
4. **Tenure & Workload Analysis** — tenure-bucket trends + overtime × travel comparison

**Filters:** Department, Job Role, Years-at-Company range, OverTime toggle, Business Travel

## Tech Stack

- **Python** — pandas, numpy
- **Visualization** — matplotlib, seaborn (EDA), Plotly (dashboard)
- **Dashboard** — Streamlit
- **Analysis environment** — Jupyter Notebook

## Repository Structure

```
├── app.py                              # Streamlit dashboard
├── requirements.txt                    # Python dependencies
├── Palo_Alto_Networks.csv              # Raw dataset
├── palo_alto_processed.csv             # Cleaned dataset with engineered bucket columns
├── kpi_summary.csv                     # Headline KPI table
├── summary_department_attrition.csv    # Department-level rates
├── summary_role_attrition.csv          # Role-level rates
├── summary_heatmap.csv                 # Role x Department attrition matrix
├── summary_age_attrition.csv
├── summary_tenure_attrition.csv
├── summary_promotion_attrition.csv
├── summary_overtime_attrition.csv
├── summary_travel_attrition.csv
├── summary_distance_attrition.csv
├── notebook/                           # EDA notebook (Palo_Alto.ipynb)
├── Workforce_Attrition_Research_Paper.docx   # Full research paper
└── README.md
```

## Setup & Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Ensure `palo_alto_processed.csv` is present in the same directory before running.

## Recommendations

- **Target the Workload Attrition segment** (OverTime + Frequent Travel, 41.86% exit rate) with workload audits and retention conversations
- **Strengthen early-tenure engagement** — the 0–2 year window drives the second-largest attrition concentration
- **Review Sales Representative role design** — its 39.76% attrition rate is a clear outlier versus every other role
- **Consider flexible travel/overtime policies** for roles that structurally require both

## Author

**Aravinth A**
Data Analyst Intern, Unified Mentor
[LinkedIn](https://www.linkedin.com/in/aravinth-a-341ba9220)
