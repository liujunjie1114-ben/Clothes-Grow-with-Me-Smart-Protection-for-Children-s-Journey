# API Document

This prototype uses server-rendered Flask routes.

## GET /

Shows the user submission page.

## POST /submit

Submits one uniform record.

Form fields:

- `child_alias`: anonymized test label
- `uniform_type`: uniform category
- `size`: uniform size
- `image`: uploaded image file
- `notes`: optional notes

Result:

- Saves the image under `static/uploads/`
- Runs preliminary OpenCV wear detection
- Inserts the record into SQLite
- Redirects to `/`

## GET /admin

Shows administrator records.

Optional query:

- `status`: filter by circulation status

## POST /admin/status/<record_id>

Updates one record status.

Form fields:

- `status`: one of `pending_review`, `available`, `reserved`, `recycled`, `discarded`
