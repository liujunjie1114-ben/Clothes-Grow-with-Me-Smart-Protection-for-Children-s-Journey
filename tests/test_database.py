import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from database import add_uniform_record, get_uniform_records, init_db, update_uniform_status


def test_uniform_record_lifecycle(tmp_path):
    """Verify that records can be inserted, read, and updated."""
    db_path = tmp_path / "test_uniform_recycling.db"
    init_db(db_path)

    record_id = add_uniform_record(
        child_alias="Test Child",
        uniform_type="Summer T-shirt",
        size="110",
        image_path="static/uploads/test.jpg",
        wear_level="light",
        wear_score=12.5,
        status="pending_review",
        notes="Virtual test data only.",
        db_path=db_path,
    )

    records = get_uniform_records(db_path=db_path)
    assert len(records) == 1
    assert records[0]["id"] == record_id
    assert records[0]["status"] == "pending_review"

    update_uniform_status(record_id, "available", db_path=db_path)
    updated_records = get_uniform_records(status="available", db_path=db_path)
    assert len(updated_records) == 1
    assert updated_records[0]["status"] == "available"
