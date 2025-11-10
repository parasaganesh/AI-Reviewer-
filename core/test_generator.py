# core/test_generator.py
import os, json
import google.generativeai as genai
from dotenv import load_dotenv
from config import TESTS_DIR, AI_MODEL, API_KEY, log_error

load_dotenv()

# Configure Gemini
genai.configure(api_key=API_KEY)

def _class_name_from_path(path: str) -> str:
    """Extract class-like name from a file path."""
    if not path:
        return "UnknownClass"
    base = os.path.basename(path)
    name, _ = os.path.splitext(base)
    return name.capitalize() + "Test"

def generate_tests(repo_path, analysis_results):
    """Generate Python unit tests using Gemini Flash 2.1 and save as JSON."""
    repo_name = os.path.basename(repo_path)
    output_file = os.path.join(TESTS_DIR, f"{repo_name}_tests.json")

    files = [
        {
            "file": fa.get("path") or fa.get("file") or "Unknown_File",
            "lines": fa.get("lines", "N/A"),
            "test_class": _class_name_from_path(fa.get("path") or fa.get("file")),
        }
        for fa in analysis_results
    ]

    prompt = f"""
    You are an expert in Python testing.
    Repository: {repo_name}.
    Generate structured and runnable test cases using unittest or pytest.
    Each module/class should have:
    - A test class
    - At least 2–3 test methods
    - Edge and normal case tests
    """

    try:
        model = genai.GenerativeModel(AI_MODEL or "gemini-2.0-flash")
        response = model.generate_content(prompt)
        test_text = getattr(response, "text", str(response))
    except Exception as e:
        test_text = f"⚠️ Error generating tests: {e}"
        log_error(test_text)

    data = {
        "repository": repo_name,
        "model": AI_MODEL,
        "files_analyzed": files,
        "generated_tests": test_text.strip(),
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return output_file
