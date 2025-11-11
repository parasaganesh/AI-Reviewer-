import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = "/tmp" if os.getenv("RENDER") else os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, "docs")
TESTS_DIR = os.path.join(BASE_DIR, "tests")
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(BASE_DIR, "logs")

for folder in [DATA_DIR, LOG_DIR, DOCS_DIR, TESTS_DIR]:
    os.makedirs(folder, exist_ok=True)

AI_MODEL = "gemini-2.0-flash"
API_KEY = os.getenv("GOOGLE_API_KEY")

LOG_FILE = os.path.join(LOG_DIR, "errors.log")

def log_error(message: str):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[ERROR] {message}\n")
