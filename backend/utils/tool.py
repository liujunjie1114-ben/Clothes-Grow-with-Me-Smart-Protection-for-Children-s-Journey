import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from config import ALLOWED_EXTENSIONS, DATABASE_FILE, IMAGE_DIR, RECORD_FILE, STATUS_VALUES


def allowed_file(filename):
    """Check whether an uploaded image extension is accepted."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def create_record(form_data, image, detection):
    """Save an uploaded image and store its anonymized record."""
    _ensure_storage()
    extension = image.filename.rsplit(".", 1)[1].lower()
    image_name = f"{uuid4().hex}.{extension}"
    image_path = IMAGE_DIR / image_name
    image.save(image_path)

    record = {
        "id": uuid4().hex,
        "child_alias": form_data.get("child_alias", "Anonymous Test User"),
        "cloth_type": form_data.get("cloth_type", "Unknown"),
        "size": form_data.get("size", "Unknown"),
        "image_path": str(Path("data") / "save_img" / image_name),
        "damage_level": detection["damage_level"],
        "damage_score": detection["damage_score"],
        "status": "pending_review",
        "note": form_data.get("note", ""),
        "created_at": _now(),
        "updated_at": _now(),
    }

    records = get_records()
    records.append(record)
    _write_json_records(records)
    _insert_sqlite_record(record)
    return record


def get_records():
    """Read records from the JSON file used for easy demo inspection."""
    _ensure_storage()
    return json.loads(RECORD_FILE.read_text(encoding="utf-8"))


def update_status(record_id, status):
    """Update one record status in JSON and SQLite."""
    if status not in STATUS_VALUES:
        status = "pending_review"

    records = get_records()
    matched_record = None
    for record in records:
        if record["id"] == record_id:
            record["status"] = status
            record["updated_at"] = _now()
            matched_record = record
            break

    if matched_record is None:
        return None

    _write_json_records(records)
    _update_sqlite_status(record_id, status, matched_record["updated_at"])
    return matched_record


def _ensure_storage():
    """Create local data folders, JSON file, and SQLite table when missing."""
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    DATABASE_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not RECORD_FILE.exists():
        RECORD_FILE.write_text("[]\n", encoding="utf-8")

    with sqlite3.connect(DATABASE_FILE) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS uniform_records (
                id TEXT PRIMARY KEY,
                child_alias TEXT NOT NULL,
                cloth_type TEXT NOT NULL,
                size TEXT NOT NULL,
                image_path TEXT NOT NULL,
                damage_level TEXT NOT NULL,
                damage_score REAL NOT NULL,
                status TEXT NOT NULL,
                note TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """
        )


def _write_json_records(records):
    """Write demo records in a readable JSON format."""
    RECORD_FILE.write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _insert_sqlite_record(record):
    """Mirror a JSON record into SQLite for backend management."""
    with sqlite3.connect(DATABASE_FILE) as connection:
        connection.execute(
            """
            INSERT INTO uniform_records (
                id, child_alias, cloth_type, size, image_path,
                damage_level, damage_score, status, note, created_at, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                record["id"],
                record["child_alias"],
                record["cloth_type"],
                record["size"],
                record["image_path"],
                record["damage_level"],
                record["damage_score"],
                record["status"],
                record["note"],
                record["created_at"],
                record["updated_at"],
            ),
        )


def _update_sqlite_status(record_id, status, updated_at):
    """Keep SQLite status aligned with the JSON record file."""
    with sqlite3.connect(DATABASE_FILE) as connection:
        connection.execute(
            """
            UPDATE uniform_records
            SET status = ?, updated_at = ?
            WHERE id = ?
            """,
            (status, updated_at, record_id),
        )


def _now():
    """Return an ISO timestamp for consistent record keeping."""
    return datetime.now(timezone.utc).isoformat()
