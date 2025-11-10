# core/code_reviewer.py
import os
import json
from datetime import datetime

def review_code(analysis_results: list[dict], output_dir: str = "data/reviews") -> str:
    """
    Accepts the list produced by analyze_repo() and returns the saved JSON path.
    """
    os.makedirs(output_dir, exist_ok=True)

    issues = []
    for fa in analysis_results:
        msgs = []

        # Extract values safely
        functions = fa.get("functions", [])
        classes = fa.get("classes", [])
        lines = fa.get("lines", 0)

        if lines > 300:
            msgs.append("⚠️ File is large, consider splitting into smaller modules.")
        if len(functions) == 0 and len(classes) == 0:
            msgs.append("ℹ️ No functions or classes; might be a script/config.")
        if len(functions) > 30:
            msgs.append("📌 Too many functions; refactor into modules/classes.")


        if msgs:
            issues.append({"file": fa.get("path", "Unknown_File"), "review": msgs})

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = os.path.join(output_dir, f"review_{ts}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(issues, f, indent=4, ensure_ascii=False)

    return out_path
