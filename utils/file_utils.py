# utils/file_utils.py
import os
import json
from datetime import datetime

def save_review(repo_name, reviews, output_dir="data/reviews"):
    """
    Save review results into a JSON file with timestamp.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    filename = f"{repo_name}_review_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=4)

    return filepath
