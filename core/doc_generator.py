# core/doc_generator.py
import os
import json
from dotenv import load_dotenv
from config import DOCS_DIR, AI_MODEL, API_KEY, log_error

# Load environment
load_dotenv()

# Try to import Gemini only if available
try:
    import google.generativeai as genai
    if API_KEY:
        genai.configure(api_key=API_KEY)
    else:
        print("⚠️ GOOGLE_API_KEY not found — running in safe public mode.")
except Exception as e:
    print(f"⚠️ Gemini module import/config failed: {e}")
    genai = None


def generate_docs(repo_path, analysis_results):
    """
    Generate repository documentation using Gemini Flash 2.0 (server-side)
    or safe fallback text in public/demo mode.
    """
    repo_name = os.path.basename(repo_path)
    output_file = os.path.join(DOCS_DIR, f"{repo_name}_docs.json")

    # Prepare summary of analyzed files
    files = [
        {
            "file": item.get("path") or item.get("file") or "Unknown_File",
            "lines": item.get("lines", "N/A"),
        }
        for item in analysis_results
    ]

    # Default doc text
    doc_text = ""

    # --- Step 1: Generate with Gemini if available ---
    if API_KEY and genai:
        try:
            model = genai.GenerativeModel(AI_MODEL or "gemini-2.0-flash")
            prompt = f"""
            You are a professional software documentation assistant.
            Analyze this repository: {repo_name}.

            Provide detailed technical documentation including:
            1️⃣ Project overview
            2️⃣ Key modules and features
            3️⃣ Class/function purposes
            4️⃣ Setup and usage guide
            5️⃣ Recommendations for improvement
            """

            response = model.generate_content(prompt)
            doc_text = getattr(response, "text", str(response))

        except Exception as e:
            log_error(f"Error generating docs with Gemini: {e}")
            doc_text = f"⚠️ Error generating docs: {e}"

    # --- Step 2: Public fallback mode ---
    else:
        doc_text = (
            "⚠️ Gemini API key missing or not configured.\n"
            "Running in public demo mode.\n\n"
            "This document provides a summary of the repository structure "
            "and placeholder analysis for demonstration purposes."
        )

    # --- Step 3: Save JSON output ---
    data = {
        "repository": repo_name,
        "model": AI_MODEL,
        "files_analyzed": files,
        "generated_doc": doc_text.strip(),
    }

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        log_error(f"Error saving doc file: {e}")

    return output_file
