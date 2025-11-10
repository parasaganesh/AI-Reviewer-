# core/doc_generator.py
import os, json
import google.generativeai as genai
from dotenv import load_dotenv
from config import DOCS_DIR, AI_MODEL, API_KEY, log_error

load_dotenv()

# Configure Gemini with API key
genai.configure(api_key=API_KEY)

def generate_docs(repo_path, analysis_results):
    """Generate repository documentation using Gemini Flash 2.1 and save as JSON."""
    repo_name = os.path.basename(repo_path)
    output_file = os.path.join(DOCS_DIR, f"{repo_name}_docs.json")

    # Prepare file summary
    files = [
        {
            "file": item.get("path") or item.get("file") or "Unknown_File",
            "lines": item.get("lines", "N/A"),
        }
        for item in analysis_results
    ]

    # Prompt for Gemini
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

    try:
        model = genai.GenerativeModel(AI_MODEL or "gemini-2.0-flash")
        response = model.generate_content(prompt)
        doc_text = getattr(response, "text", str(response))
    except Exception as e:
        doc_text = f"⚠️ Error generating docs: {e}"
        log_error(doc_text)

    # Save as JSON
    data = {
        "repository": repo_name,
        "model": AI_MODEL,
        "files_analyzed": files,
        "generated_doc": doc_text.strip(),
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return output_file
