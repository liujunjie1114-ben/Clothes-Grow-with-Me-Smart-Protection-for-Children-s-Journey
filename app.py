from pathlib import Path
from uuid import uuid4

from flask import Flask, redirect, render_template, request, url_for

from database import add_uniform_record, get_uniform_records, init_db, update_uniform_status
from wear_detection import detect_wear_level


BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "static" / "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_DIR


def is_allowed_file(filename):
    """Return True when the uploaded file extension is supported."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    """Show the basic user submission page."""
    return render_template("user.html")


@app.route("/submit", methods=["POST"])
def submit_uniform():
    """Handle uniform submission, run initial wear detection, and save a record."""
    image = request.files.get("image")
    if not image or not image.filename or not is_allowed_file(image.filename):
        return "Please upload a valid image file.", 400

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    extension = image.filename.rsplit(".", 1)[1].lower()
    stored_filename = f"{uuid4().hex}.{extension}"
    image_path = UPLOAD_DIR / stored_filename
    image.save(image_path)

    wear_result = detect_wear_level(image_path)
    add_uniform_record(
        child_alias=request.form.get("child_alias", "Anonymous Test User"),
        uniform_type=request.form.get("uniform_type", "Unknown"),
        size=request.form.get("size", "Unknown"),
        image_path=f"static/uploads/{stored_filename}",
        wear_level=wear_result["wear_level"],
        wear_score=wear_result["wear_score"],
        status="pending_review",
        notes=request.form.get("notes", ""),
    )

    return redirect(url_for("index"))


@app.route("/admin")
def admin():
    """Show records for administrator review."""
    status = request.args.get("status")
    records = get_uniform_records(status=status)
    return render_template("admin.html", records=records, selected_status=status)


@app.route("/admin/status/<int:record_id>", methods=["POST"])
def change_status(record_id):
    """Update one uniform record's circulation status."""
    update_uniform_status(record_id, request.form.get("status", "pending_review"))
    return redirect(url_for("admin"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
