import sqlite3
import pandas as pd
import streamlit as st

DB = "data/jobs.db"

st.set_page_config(page_title="Job Matching Agent", layout="wide")
st.title("Local Job Matching Agent")

try:
    connection = sqlite3.connect(DB)

    jobs = pd.read_sql_query(
        """
        SELECT
            j.id,
            j.title,
            j.company,
            j.location,
            j.source,
            j.posted_at,
            j.url,
            s.final_score,
            s.recommendation
        FROM jobs j
        LEFT JOIN job_scores s ON s.job_id = j.id
        ORDER BY s.final_score DESC, j.posted_at DESC
        """,
        connection,
    )

    connection.close()

    minimum = st.sidebar.slider(
        "Minimum fit score", 0.0, 10.0, 7.0, 0.5
    )
    limit = st.sidebar.number_input(
        "Maximum results", 1, 100, 10
    )

    filtered = jobs[jobs["final_score"].fillna(0) >= minimum].head(int(limit))

    st.metric("Jobs shown", len(filtered))

    if filtered.empty:
        st.info("No matching jobs are currently available.")
    else:
        st.dataframe(
            filtered,
            column_config={
                "url": st.column_config.LinkColumn("Apply"),
                "final_score": st.column_config.NumberColumn(
                    "Fit Score", format="%.1f"
                ),
            },
            use_container_width=True,
            hide_index=True,
        )

except Exception as exc:
    st.error(f"Dashboard could not load the database: {exc}")
