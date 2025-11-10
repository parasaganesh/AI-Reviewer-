import os
from dotenv import load_dotenv

# ✅ Load environment variables from .env (optional for local)
load_dotenv()

# ✅ Define BASE_DIR first (must be before using it!)
BASE_DIR = "/tmp" if os.getenv("VERCEL_ENV") else os.path.dirname(os.path.abspath(__file__))

# ✅ Define all important directories
DOCS_DIR = os.path.join(BASE_DIR, "docs")
TESTS_DIR = os.path.join(BASE_DIR, "tests")
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(BASE_DIR, "logs")

# ✅ Ensure required folders exist (Render & Vercel safe)
for folder in [DATA_DIR, LOG_DIR, DOCS_DIR, TESTS_DIR]:
    os.makedirs(folder, exist_ok=True)

# ✅ Model and API setup
AI_MODEL = "gemini-2.1-flash"
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise EnvironmentError("❌ GOOGLE_API_KEY not found. Please set it in Render Environment Variables.")

# ✅ Logging setup
LOG_FILE = os.path.join(LOG_DIR, "errors.log")

def log_error(message: str):
    """Simple file-based logger"""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[ERROR] {message}\n")
