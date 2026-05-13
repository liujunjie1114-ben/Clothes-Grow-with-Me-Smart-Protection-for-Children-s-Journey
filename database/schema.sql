CREATE TABLE IF NOT EXISTS uniform_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    child_alias TEXT NOT NULL,
    uniform_type TEXT NOT NULL,
    size TEXT NOT NULL,
    image_path TEXT NOT NULL,
    wear_level TEXT NOT NULL CHECK (wear_level IN ('light', 'moderate', 'heavy', 'unknown')),
    wear_score REAL NOT NULL DEFAULT 0,
    status TEXT NOT NULL DEFAULT 'pending_review'
        CHECK (status IN ('pending_review', 'available', 'reserved', 'recycled', 'discarded')),
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_uniform_records_status
ON uniform_records(status);

CREATE INDEX IF NOT EXISTS idx_uniform_records_uniform_type
ON uniform_records(uniform_type);
