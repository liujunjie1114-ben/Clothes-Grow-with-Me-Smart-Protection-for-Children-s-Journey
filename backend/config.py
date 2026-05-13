from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
FRONTEND_DIR = ROOT_DIR / "frontend"
MANAGE_DIR = ROOT_DIR / "manage"
DATA_DIR = ROOT_DIR / "data"
IMAGE_DIR = DATA_DIR / "save_img"
DATABASE_DIR = DATA_DIR / "database"
RECORD_FILE = DATA_DIR / "record.json"
DATABASE_FILE = DATABASE_DIR / "uniform_records.db"

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
STATUS_VALUES = {"pending_review", "available", "reserved", "recycled", "discarded"}
