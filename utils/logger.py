# utils/logger.py

import logging
import os

LOG_FILE = "app.log"

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_info(message: str):
    print("ℹ️", message)
    logging.info(message)

def log_warning(message: str):
    print("⚠️", message)
    logging.warning(message)

def log_error(message: str):
    print("❌", message)
    logging.error(message)
