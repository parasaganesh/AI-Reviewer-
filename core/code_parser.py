import os

def analyze_repo(repo_path):
    analysis_results = []
    
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):  # Only Python files for now
                file_path = os.path.join(root, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                line_count = len(lines)
                functions = [l for l in lines if l.strip().startswith("def ")]
                classes   = [l for l in lines if l.strip().startswith("class ")]

                analysis_results.append({
                    "file": file_path,
                    "lines": line_count,
                    "functions": functions,
                    "classes": classes
                })
    
    return analysis_results
