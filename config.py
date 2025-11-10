import os
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Define BASE_DIR FIRST (this fixes the NameError)
BASE_DIR = "/tmp" if os.getenv("VERCEL_ENV") else os.path.dirname(os.path.abspath(__file__))

# ✅ Define directories AFTER BASE_DIR is known
DOCS_DIR = os.path.join(BASE_DIR, "docs")
TESTS_DIR = os.path.join(BASE_DIR, "tests")
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(BASE_DIR, "logs")

# ✅ Create folders safely (Render, Vercel, or local)
for folder in [DATA_DIR, LOG_DIR, DOCS_DIR, TESTS_DIR]:
    os.makedirs(folder, exist_ok=True)

# ✅ Model and API
AI_MODEL = "gemini-2.1-flash"
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise EnvironmentError("❌ GOOGLE_API_KEY not found. Please set it in Render Environment Variables.")

# ✅ Logging
LOG_FILE = os.path.join(LOG_DIR, "errors.log")

def log_error(message: str):
    """Simple file-based logger"""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[ERROR] {message}\n")
