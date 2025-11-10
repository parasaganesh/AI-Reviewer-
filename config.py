# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(BASE_DIR, "logs")

# Subfolders
REPO_DIR = os.path.join(DATA_DIR, "repos")
REVIEW_DIR = os.path.join(DATA_DIR, "reviews")
DOCS_DIR = os.path.join(DATA_DIR, "docs")
TESTS_DIR = os.path.join(DATA_DIR, "tests")

for folder in [REPO_DIR, REVIEW_DIR, DOCS_DIR, TESTS_DIR, LOG_DIR]:
    os.makedirs(folder, exist_ok=True)

# AI Configuration
AI_MODEL = "gemini-2.1-flash"
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise EnvironmentError("❌ GOOGLE_API_KEY not found! Please add it to your .env file.")

# Logging
LOG_FILE = os.path.join(LOG_DIR, "errors.log")

def log_error(message: str):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[ERROR] {message}\n")
