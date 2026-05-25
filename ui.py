import streamlit as st
import pandas as pd

from src.services.storage_service import load_reviews

st.set_page_config(
    page_title="AI Code Review Dashboard",
    layout="wide"
)

st.title("AI-Powered Code Review Assistant")

reviews = load_reviews()

if not reviews:

    st.warning("No reviews found.")

    st.stop()

# Convert to DataFrame
df = pd.DataFrame(reviews)

# Metrics
total_reviews = len(df)

total_issues = df["total_issues"].sum()

average_risk = df["risk_score"].mean()

# Top Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Reviewed PRs", total_reviews)

col2.metric("Total Issues", total_issues)

col3.metric("Average Risk Score", round(average_risk, 2))

st.divider()

# Reviews Table
st.subheader("Pull Request Reviews")

st.dataframe(
    df[[
        "repository",
        "pr_number",
        "risk_score",
        "total_issues"
    ]]
)

st.divider()

# Detailed Issues
st.subheader("Detailed Findings")

for review in reviews:

    st.markdown(
        f"## {review['repository']} - PR #{review['pr_number']}"
    )

    st.markdown(
        f"Risk Score: {review['risk_score']}"
    )

    for issue in review["issues"]:

        st.error(
            f"""
Severity: {issue['severity']}

Issue: {issue['issue']}

Suggestion: {issue['suggestion']}
"""
        )