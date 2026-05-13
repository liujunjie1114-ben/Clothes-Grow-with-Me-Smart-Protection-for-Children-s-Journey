from pathlib import Path

import cv2
import numpy as np


def detect_wear_level(image_path):
    """
    Estimate uniform wear level using image brightness, blur, and edge density.

    This is a lightweight prototype rule, not a final AI model. Future versions can
    replace it with a trained classifier while keeping the same return structure.
    """
    path = Path(image_path)
    image = cv2.imread(str(path))
    if image is None:
        return {"wear_level": "unknown", "wear_score": 0.0}

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    brightness = float(np.mean(gray))
    blur_score = float(cv2.Laplacian(gray, cv2.CV_64F).var())
    edges = cv2.Canny(gray, 80, 160)
    edge_density = float(np.count_nonzero(edges)) / edges.size

    wear_score = _calculate_wear_score(brightness, blur_score, edge_density)
    return {
        "wear_level": _score_to_level(wear_score),
        "wear_score": round(wear_score, 2),
    }


def _calculate_wear_score(brightness, blur_score, edge_density):
    """Convert simple image features into a 0-100 prototype wear score."""
    dim_penalty = max(0.0, (120.0 - brightness) / 120.0) * 35.0
    blur_penalty = max(0.0, (120.0 - min(blur_score, 120.0)) / 120.0) * 35.0
    edge_penalty = min(edge_density * 100.0, 1.0) * 30.0
    return min(100.0, dim_penalty + blur_penalty + edge_penalty)


def _score_to_level(score):
    """Map a numeric score to a readable wear level."""
    if score < 30:
        return "light"
    if score < 65:
        return "moderate"
    return "heavy"
