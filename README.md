# AI Kindergarten Uniform Recycling System

中文项目名称：衣随我长·智护童行——可生长型AI赋能幼儿环保园服系统

## Project Introduction

This project is a Flask + SQLite + OpenCV + HTML/CSS/JavaScript prototype for kindergarten uniform recycling management. Users can upload a uniform image and submit basic clothing information. The backend uses OpenCV to make an initial wear-level estimate, stores the result, and provides management pages for viewing and updating record status.

Important privacy rule: this repository must not contain real children's information, real photos, or production databases.

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- Image analysis: OpenCV
- Data storage: JSON record file and local SQLite database

## Project Structure

```text
ai-uniform-recycling-system/
├─ frontend/
│  ├─ index.html
│  ├─ style.css
│  ├─ js/
│  │  └─ main.js
│  └─ static/
│     └─ images/
│
├─ backend/
│  ├─ app.py
│  ├─ detect.py
│  ├─ config.py
│  └─ utils/
│     └─ tool.py
│
├─ data/
│  ├─ record.json
│  ├─ database/
│  └─ save_img/
│
├─ manage/
│  ├─ admin.html
│  └─ record_list.html
│
├─ run.bat
├─ requirements.txt
├─ .gitignore
├─ LICENSE
└─ README.md
```

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

3. Run the project.

```bash
run.bat
```

Or run Flask directly:

```bash
python backend/app.py
```

4. Open the local site.

```text
http://127.0.0.1:5000
```

## Main Features

- Upload uniform image and basic clothing information.
- Use OpenCV for preliminary wear-level judgment.
- Save submitted records into `data/record.json` and local SQLite storage.
- Provide management pages for record viewing and status updates.

## Collaboration Notes

- Use branches and pull requests for team development.
- Keep frontend code under `frontend/`.
- Keep backend routes and detection logic under `backend/`.
- Keep only virtual demo data in `data/record.json`.
- Do not commit real uploaded photos, local database files, cache files, or virtual environments.
