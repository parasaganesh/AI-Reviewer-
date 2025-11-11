# core/doc_generator.py
import os, json
from dotenv import load_dotenv
from config import DOCS_DIR, AI_MODEL, API_KEY, log_error

load_dotenv()

def generate_docs(repo_path, analysis_results):
    """Always return a docs file — never crash."""
    repo_name = os.path.basename(repo_path)
    output_file = os.path.join(DOCS_DIR, f"{repo_name}_docs.json")

    # fallback content
    doc_text = (
        f"📘 Documentation for '{repo_name}'\n\n"
        f"Files analyzed: {len(analysis_results)}\n"
        "Gemini API skipped for this build.\n"
        "Everything runs locally and safely."
    )

    data = {
        "repository": repo_name,
        "model": AI_MODEL,
        "files_analyzed": [
            {"file": f.get('path', f.get('file', 'unknown'))} for f in analysis_results
        ],
        "generated_doc": doc_text,
    }

    os.makedirs(DOCS_DIR, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return output_file
