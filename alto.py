

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Palo Alto Networks - Attrition Analysis", layout="wide")
st.title("Workforce Attrition Patterns & Risk Hotspot Analysis")
st.caption("Palo Alto Networks | Unified Mentor Data Analyst Internship")

df = pd.read_csv("palo_alto_processed.csv")

# ---------------------------------------------------------------
# Sidebar filters
# ---------------------------------------------------------------
st.sidebar.header("Filters")
dept_filter = st.sidebar.multiselect("Department", sorted(df["Department"].unique()))
role_filter = st.sidebar.multiselect("Job Role", sorted(df["JobRole"].unique()))
tenure_range = st.sidebar.slider(
    "Years At Company", 0, int(df["YearsAtCompany"].max()),
    (0, int(df["YearsAtCompany"].max()))
)
overtime_toggle = st.sidebar.checkbox("OverTime only")
travel_toggle = st.sidebar.multiselect("Business Travel", sorted(df["BusinessTravel"].unique()))

f = df.copy()
if dept_filter:
    f = f[f["Department"].isin(dept_filter)]
if role_filter:
    f = f[f["JobRole"].isin(role_filter)]
f = f[(f["YearsAtCompany"] >= tenure_range[0]) & (f["YearsAtCompany"] <= tenure_range[1])]
if overtime_toggle:
    f = f[f["OverTime"] == "Yes"]
if travel_toggle:
    f = f[f["BusinessTravel"].isin(travel_toggle)]

if f.empty:
    st.warning("No records match the selected filters. Adjust the filters in the sidebar.")
    st.stop()

# ---------------------------------------------------------------
# Module 1: Attrition Overview
# ---------------------------------------------------------------
st.subheader("Module 1 — Attrition Overview")
col1, col2 = st.columns([1, 2])
rate = f["Attrition"].mean() * 100
col1.metric("Attrition Rate", f"{rate:.2f}%", help=f"Based on {len(f):,} filtered records")

fig1 = px.pie(
    f, names=f["Attrition"].map({1: "Exited", 0: "Retained"}),
    title="Retained vs Exited", color_discrete_sequence=["#2E5EAA", "#D97706"]
)
col2.plotly_chart(fig1, use_container_width=True)

# ---------------------------------------------------------------
# Module 2: Department & Role Heatmap
# ---------------------------------------------------------------
st.subheader("Module 2 — Department & Role Heatmap")
heat = f.pivot_table(index="JobRole", columns="Department", values="Attrition", aggfunc="mean") * 100
fig2 = px.imshow(heat, text_auto=".1f", color_continuous_scale="Reds", aspect="auto")
st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------------------
# Module 3: Demographic Attrition Explorer
# ---------------------------------------------------------------
st.subheader("Module 3 — Demographic Attrition Explorer")
demo_options = [c for c in ["AgeGroup", "Gender", "MaritalStatus", "EducationField"] if c in f.columns]
demo_col = st.selectbox("Break down by", demo_options)
demo_summary = f.groupby(demo_col, observed=True)["Attrition"].mean().mul(100).reset_index()
fig3 = px.bar(demo_summary, x=demo_col, y="Attrition", title=f"Attrition % by {demo_col}")
st.plotly_chart(fig3, use_container_width=True)

# ---------------------------------------------------------------
# Module 4: Tenure & Workload Analysis
# ---------------------------------------------------------------
st.subheader("Module 4 — Tenure & Workload Analysis")
c1, c2 = st.columns(2)

tenure_summary = f.groupby("TenureBucket", observed=True)["Attrition"].mean().mul(100).reset_index()
fig4 = px.bar(tenure_summary, x="TenureBucket", y="Attrition", title="Attrition % by Tenure Bucket")
c1.plotly_chart(fig4, use_container_width=True)

workload_summary = f.groupby(["OverTime", "BusinessTravel"])["Attrition"].mean().mul(100).reset_index()
fig5 = px.bar(
    workload_summary, x="BusinessTravel", y="Attrition", color="OverTime", barmode="group",
    title="Attrition % by OverTime x Business Travel"
)
c2.plotly_chart(fig5, use_container_width=True)

st.caption(
    "Note: The OverTime + Frequent Travel combination is the strongest workload-attrition "
    "signal in this dataset — check its rate specifically using the filters above."
)