import tempfile

import cv2
import numpy as np


def detect_damage(file_storage):
    """
    Estimate clothing damage from an uploaded image.

    This is a prototype OpenCV rule. It can later be replaced by a trained model
    while keeping the same response fields.
    """
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=True) as temp_file:
        file_storage.save(temp_file.name)
        image = cv2.imread(temp_file.name)
        file_storage.seek(0)

    if image is None:
        return {"damage_level": "unknown", "damage_score": 0.0}

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    brightness = float(np.mean(gray))
    blur_score = float(cv2.Laplacian(gray, cv2.CV_64F).var())
    edges = cv2.Canny(gray, 80, 160)
    edge_density = float(np.count_nonzero(edges)) / edges.size

    score = _calculate_score(brightness, blur_score, edge_density)
    return {"damage_level": _level_from_score(score), "damage_score": round(score, 2)}


def _calculate_score(brightness, blur_score, edge_density):
    """Convert image features into a 0-100 damage score."""
    dim_penalty = max(0.0, (120.0 - brightness) / 120.0) * 35.0
    blur_penalty = max(0.0, (120.0 - min(blur_score, 120.0)) / 120.0) * 35.0
    edge_penalty = min(edge_density * 100.0, 1.0) * 30.0
    return min(100.0, dim_penalty + blur_penalty + edge_penalty)


def _level_from_score(score):
    """Map numeric score to a management-friendly damage level."""
    if score < 30:
        return "light"
    if score < 65:
        return "moderate"
    return "heavy"
