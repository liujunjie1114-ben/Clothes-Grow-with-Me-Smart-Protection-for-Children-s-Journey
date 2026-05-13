from flask import Flask, jsonify, request, send_from_directory

from config import FRONTEND_DIR, MANAGE_DIR
from detect import detect_damage
from utils.tool import allowed_file, create_record, get_records, update_status


app = Flask(__name__)


@app.route("/")
def index():
    """Serve the user-facing upload page."""
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/<path:filename>")
def frontend_assets(filename):
    """Serve frontend CSS and JavaScript assets."""
    return send_from_directory(FRONTEND_DIR, filename)


@app.route("/manage")
def manage_home():
    """Serve the admin entry page."""
    return send_from_directory(MANAGE_DIR, "admin.html")


@app.route("/manage/records")
def manage_records():
    """Serve the record list page."""
    return send_from_directory(MANAGE_DIR, "record_list.html")


@app.route("/api/upload", methods=["POST"])
def upload_record():
    """Receive one uniform image, detect damage, and save the record."""
    image = request.files.get("image")
    if not image or not image.filename or not allowed_file(image.filename):
        return jsonify({"error": "Please upload a valid image file."}), 400

    detection = detect_damage(image)
    record = create_record(request.form, image, detection)
    return jsonify({"record": record}), 201


@app.route("/api/records")
def list_records():
    """Return all stored records as JSON for the management page."""
    return jsonify({"records": get_records()})


@app.route("/api/records/<record_id>/status", methods=["POST"])
def change_record_status(record_id):
    """Update the circulation status of one record."""
    payload = request.get_json(silent=True) or {}
    status = payload.get("status", "pending_review")
    record = update_status(record_id, status)
    if record is None:
        return jsonify({"error": "Record not found."}), 404
    return jsonify({"record": record})


if __name__ == "__main__":
    app.run(debug=True)
