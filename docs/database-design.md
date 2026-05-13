# Database Design

## Table: uniform_records

| Field | Type | Description |
| --- | --- | --- |
| id | INTEGER | Primary key |
| child_alias | TEXT | Anonymized child label for testing and review |
| uniform_type | TEXT | Uniform category |
| size | TEXT | Uniform size |
| image_path | TEXT | Local upload path |
| wear_level | TEXT | `light`, `moderate`, `heavy`, or `unknown` |
| wear_score | REAL | Prototype OpenCV score from 0 to 100 |
| status | TEXT | Circulation status |
| notes | TEXT | Optional review notes |
| created_at | TEXT | Creation timestamp |
| updated_at | TEXT | Last update timestamp |

## Status Values

- `pending_review`: submitted and awaiting review
- `available`: can be reused
- `reserved`: reserved for future circulation
- `recycled`: entered recycling process
- `discarded`: not suitable for reuse or recycling display
