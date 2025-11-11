# core/doc_generator.py
import os
import json
from dotenv import load_dotenv
from config import DOCS_DIR, AI_MODEL, API_KEY, log_error

load_dotenv()

# --- Safe Gemini import ---
try:
    import google.generativeai as genai
    if API_KEY:
        genai.configure(api_key=API_KEY)
        print(f"✅ Gemini configured successfully ({AI_MODEL})")
    else:
        print("⚠️ No GOOGLE_API_KEY found. Using demo fallback mode.")
except Exception as e:
    genai = None
    print(f"⚠️ Gemini module import failed: {e}")


def generate_docs(repo_path, analysis_results):
    """Safely generate repository documentation — never crash."""
    repo_name = os.path.basename(repo_path)
    output_file = os.path.join(DOCS_DIR, f"{repo_name}_docs.json")

    # Collect summary of files analyzed
    files = [
        {
            "file": item.get("path") or item.get("file") or "Unknown_File",
            "lines": item.get("lines", "N/A")
        }
        for item in analysis_results or []
    ]

    doc_text = "⚙️ Generating documentation..."
    success = False

    try:
        # --- Use Gemini only if configured properly ---
        if API_KEY and genai:
            model_name = AI_MODEL if AI_MODEL else "gemini-2.0-flash"
            try:
                model = genai.GenerativeModel(model_name)
                prompt = f"""
                You are an intelligent documentation generator.
                Create a clear technical summary for the repository "{repo_name}".
                Include:
                1️⃣ Overview of the project
                2️⃣ Key modules, files, and functions
                3️⃣ Setup instructions
                4️⃣ Suggestions for improvement
                """

                response = model.generate_content(prompt)
                doc_text = getattr(response, "text", str(response))
                success = True
                print(f"✅ Docs generated for {repo_name}")
            except Exception as inner_error:
                error_msg = f"Gemini model error: {inner_error}"
                log_error(error_msg)
                print(f"⚠️ {error_msg}")
                doc_text = f"⚠️ Failed to generate docs via Gemini: {inner_error}"

        # --- If Gemini missing or API key absent ---
        if not success:
            doc_text = (
                f"⚠️ Gemini not configured or failed.\n"
                f"This is an offline fallback doc for '{repo_name}'.\n"
                f"Files analyzed: {len(files)}\n"
                "Add a valid GOOGLE_API_KEY to enable live AI documentation."
            )

    except Exception as outer_error:
        error_msg = f"Critical doc generation failure: {outer_error}"
        log_error(error_msg)
        print(f"⚠️ {error_msg}")
        doc_text = f"⚠️ Unexpected error during documentation generation: {outer_error}"

    # --- Safely write to file ---
    try:
        os.makedirs(DOCS_DIR, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "repository": repo_name,
                    "model": AI_MODEL,
                    "files_analyzed": files,
                    "generated_doc": doc_text.strip(),
                },
                f,
                indent=4,
                ensure_ascii=False
            )
        print(f"✅ Saved docs to {output_file}")
    except Exception as file_error:
        log_error(f"File write error: {file_error}")
        print(f"⚠️ File save failed: {file_error}")

    return output_file
