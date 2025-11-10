# core/agent.py
from core.repo_loader import clone_repo
from core.code_parser import analyze_repo
from core.code_reviewer import review_code
from core.doc_generator import generate_docs
from core.test_generator import generate_tests
from core.report_builder import build_report
from utils.file_utils import save_review

class CodeReviewAgent:
    def __init__(self, base_dir="data"):
        self.base_dir = base_dir

    def run(self, repo_url: str):
        print(f"🤖 Starting AI Code Review Agent for: {repo_url}")

        # 1. Clone repo
        repo_path = clone_repo(repo_url, f"{self.base_dir}/repos")
        repo_name = repo_url.split("/")[-1]

        # 2. Analyze code
        results = analyze_repo(repo_path)

        # 3. AI review
        reviews = []
        for r in results[:5]:
            reviews.append(review_code(r))
        review_file = save_review(repo_name, reviews)

        # 4. Documentation
        doc_file = generate_docs(repo_name, results)

        # 5. Tests
        test_file = generate_tests(repo_name, results)

        # 6. Report
        report_file = build_report(repo_name, results, review_file, doc_file, test_file)

        print(f"\n✅ AI Agent finished! Final report at: {report_file}")
        return report_file
