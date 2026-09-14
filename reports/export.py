import sqlite3
from pathlib import Path
import pandas as pd


def export_shortlist(
    db_path="data/jobs.db",
    output_path="data/exports/shortlist.csv",
    minimum_score=7.0,
):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(db_path)

    query = """
        SELECT
            j.title AS role,
            j.company,
            j.location,
            j.posted_at,
            j.source,
            s.final_score AS fit_score,
            s.recommendation,
            j.url AS apply_link
        FROM jobs j
        JOIN job_scores s ON s.job_id = j.id
        WHERE s.final_score >= ?
        ORDER BY s.final_score DESC, j.posted_at DESC
    """

    dataframe = pd.read_sql_query(query, connection, params=(minimum_score,))
    connection.close()
    dataframe.to_csv(output_path, index=False)
