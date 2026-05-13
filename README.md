# AI Kindergarten Uniform Recycling System

中文项目名称：衣随我长·智护童行——可生长型AI赋能幼儿环保园服系统

## Project Introduction

This project is a Flask + SQLite + OpenCV based prototype for kindergarten uniform recycling management. The user side allows families or staff to submit uniform information with an uploaded image. The system uses OpenCV to make an initial wear-level estimate and stores the result in SQLite. The admin side reads from the database to review records, filter data, and update circulation status.

The repository is prepared for GitHub version control, team collaboration, and university innovation and entrepreneurship competition demonstrations.

Important privacy rule: do not commit real children's information, real photos, or production databases.

## Tech Stack

- Backend: Python, Flask
- Database: SQLite
- Image analysis: OpenCV
- Frontend foundation: HTML, CSS, JavaScript
- Testing: pytest

## Local Setup

1. Create and activate a virtual environment.

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Initialize the database.

```bash
python database.py
```

4. Run the Flask app.

```bash
python app.py
```

5. Open the app in a browser.

```text
http://127.0.0.1:5000
```

## Project Structure

```text
ai-uniform-recycling-system/
├── README.md
├── requirements.txt
├── .gitignore
├── app.py
├── database.py
├── wear_detection.py
├── docs/
│   ├── project-overview.md
│   ├── system-logic.md
│   ├── database-design.md
│   └── api-document.md
├── database/
│   ├── schema.sql
│   └── sample_data.sql
├── static/
│   ├── css/
│   │   ├── user.css
│   │   └── admin.css
│   ├── js/
│   │   ├── user.js
│   │   └── admin.js
│   └── uploads/
├── templates/
│   ├── user.html
│   ├── admin.html
│   └── login.html
└── tests/
    └── test_database.py
```

## Collaboration Notes

- Keep feature work on branches and open pull requests for review.
- Keep database schema changes in `database/schema.sql`.
- Keep sample-only, anonymized test data in `database/sample_data.sql`.
- Do not commit files under `static/uploads/` except `.gitkeep`.
- Do not commit local SQLite databases, cache folders, or virtual environments.

## Competition Display Direction

The project can be presented as an AI-assisted circular uniform management system with three core values:

- Environmental protection through uniform reuse.
- Lightweight AI-assisted wear assessment.
- Traceable circulation status management for schools.
