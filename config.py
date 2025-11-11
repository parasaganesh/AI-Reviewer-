import os
from dotenv import load_dotenv

load_dotenv()

# ✅ Base directory for Render
BASE_DIR = "/tmp" if os.getenv("RENDER") else os.path.dirname(os.path.abspath(__file__))

# ✅ Directories
DOCS_DIR = os.path.join(BASE_DIR, "docs")
TESTS_DIR = os.path.join(BASE_DIR, "tests")
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(BASE_DIR, "logs")

for folder in [DOCS_DIR, TESTS_DIR, DATA_DIR, LOG_DIR]:
    os.makedirs(folder, exist_ok=True)

# ✅ Model setup (public-friendly)
AI_MODEL = "gemini-2.0-flash"

# ✅ Safe API Key setup
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    print("⚠️ Warning: GOOGLE_API_KEY missing. Public mode enabled — limited AI features.")

# ✅ Logging
LOG_FILE = os.path.join(LOG_DIR, "errors.log")

def log_error(message: str):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[ERROR] {message}\n")
