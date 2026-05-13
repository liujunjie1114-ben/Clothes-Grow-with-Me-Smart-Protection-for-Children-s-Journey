# System Logic

## User Submission Flow

1. User opens the submission page.
2. User enters anonymized uniform information and uploads an image.
3. Flask receives the form data.
4. The image is saved to `static/uploads/`.
5. OpenCV performs a preliminary wear-level estimate.
6. The record is written to SQLite with status `pending_review`.

## Admin Review Flow

1. Administrator opens the admin page.
2. Flask reads records from SQLite.
3. Administrator reviews wear level, notes, and circulation status.
4. Administrator updates status such as `available`, `reserved`, `recycled`, or `discarded`.

## Future Extension

The current OpenCV rule can be replaced by a trained computer vision model without changing the database contract.
