import pandas as pd
import numpy as np
import streamlit as st

# -------------------------------
# App Title
# -------------------------------
st.title(" Student Performance Analysis")

# -------------------------------
# File Upload
# -------------------------------
uploaded_file = st.file_uploader("students.csv", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df)

    # -------------------------------
    # Sidebar Filters
    # -------------------------------
    st.sidebar.header("Filter Options")

    # Filter by Name
    if "Name" in df.columns:
        selected_student = st.sidebar.multiselect("Student Name", df["Name"].unique())
        if selected_student:
            df = df[df["Name"].isin(selected_student)]

    # Filter by City
    if "City" in df.columns:
        selected_city = st.sidebar.multiselect("City", df["City"].unique())
        if selected_city:
            df = df[df["City"].isin(selected_city)]

    # Filter by Nationality
    if "Nationality" in df.columns:
        selected_nationality = st.sidebar.multiselect("Nationality", df["Nationality"].unique())
        if selected_nationality:
            df = df[df["Nationality"].isin(selected_nationality)]

    # -------------------------------
    # Show Filtered Data
    # -------------------------------
    st.subheader("Filtered Data")
    st.dataframe(df)

    # -------------------------------
    # Statistics Summary
    # -------------------------------
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    if numeric_cols:
        st.subheader("Statistics Summary")
        stats_df = pd.DataFrame({
            "Mean": df[numeric_cols].mean(),
            "Median": df[numeric_cols].median(),
            "Min": df[numeric_cols].min(),
            "Max": df[numeric_cols].max()
        })
        st.dataframe(stats_df)

        # -------------------------------
        # Visualizations
        # -------------------------------
        st.subheader("Grade Visualizations")
        for col in numeric_cols:
            st.write(f" {col} Grades")
            st.bar_chart(df[[col]])

else:
    st.info("Upload a CSV file to get started!")
