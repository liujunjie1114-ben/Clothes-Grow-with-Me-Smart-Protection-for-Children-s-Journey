import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "database" / "uniform_recycling.db"
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"


def get_connection(db_path=DATABASE_PATH):
    """Create a SQLite connection with dictionary-like row access."""
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection


def init_db(db_path=DATABASE_PATH):
    """Initialize database tables from the schema file."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with get_connection(db_path) as connection:
        connection.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    return db_path


def add_uniform_record(
    child_alias,
    uniform_type,
    size,
    image_path,
    wear_level,
    wear_score,
    status,
    notes="",
    db_path=DATABASE_PATH,
):
    """Insert one anonymized uniform recycling record."""
    with get_connection(db_path) as connection:
        cursor = connection.execute(
            """
            INSERT INTO uniform_records (
                child_alias, uniform_type, size, image_path,
                wear_level, wear_score, status, notes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                child_alias,
                uniform_type,
                size,
                image_path,
                wear_level,
                wear_score,
                status,
                notes,
            ),
        )
        return cursor.lastrowid


def get_uniform_records(status=None, db_path=DATABASE_PATH):
    """Read uniform records, optionally filtered by circulation status."""
    with get_connection(db_path) as connection:
        if status:
            rows = connection.execute(
                "SELECT * FROM uniform_records WHERE status = ? ORDER BY created_at DESC",
                (status,),
            ).fetchall()
        else:
            rows = connection.execute(
                "SELECT * FROM uniform_records ORDER BY created_at DESC"
            ).fetchall()
    return [dict(row) for row in rows]


def update_uniform_status(record_id, status, db_path=DATABASE_PATH):
    """Update the circulation status of a uniform record."""
    with get_connection(db_path) as connection:
        connection.execute(
            """
            UPDATE uniform_records
            SET status = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (status, record_id),
        )


if __name__ == "__main__":
    created_path = init_db()
    print(f"Database initialized at: {created_path}")
