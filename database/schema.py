from pathlib import Path
from .connection import get_connection


def initialise_database(db_path: str = "data/jobs.db") -> None:
    schema = Path(__file__).with_name("schema.sql").read_text(encoding="utf-8")
    with get_connection(db_path) as connection:
        connection.executescript(schema)
        connection.commit()
