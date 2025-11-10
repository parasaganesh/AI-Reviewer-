# app.py
import sys
import os
from core.repo_loader import clone_repo
from core.code_parser import analyze_repo
from core.code_reviewer import review_code
from core.doc_generator import generate_docs
from core.test_generator import generate_tests
from core.report_builder import build_report
from utils.file_utils import save_review
from core.agent import CodeReviewAgent
from utils.logger import log_info, log_error
from utils.pdf_utils import export_to_pdf   # ✅ fixed import

if __name__ == "__main__":
    if len(sys.argv) < 2:
        log_error("Usage: python app.py <github_repo_url> [--manual]")
        sys.exit(1)

    repo_url = sys.argv[1]
    manual_mode = "--manual" in sys.argv

    if not manual_mode:
        # 🔹 Agent Mode (automatic full pipeline)
        agent = CodeReviewAgent()
        final_report = agent.run(repo_url)
        log_info(f"🚀 All done! Final report generated at: {final_report}")

    else:
        # 🔹 Manual Mode
        repo_path = clone_repo(repo_url, "data/repos")
        repo_name = repo_url.split("/")[-1]

        log_info(f"🔍 Analyzing repo: {repo_path}")
        results = analyze_repo(repo_path)

        log_info("📊 Code Analysis Results (showing first 10):")
        for r in results[:10]:
            log_info(
                f"File: {r.get('file')} | Lines: {r.get('lines')} | "
                f"Functions: {len(r.get('functions', []))} | Classes: {len(r.get('classes', []))}"
            )

        # ✅ AI Review
        log_info("🤖 AI Code Review:")
        reviews = review_code(results)   # pass whole repo results
        review_file = save_review(repo_name, reviews)
        log_info(f"💾 Review saved at: {review_file}")

        # ✅ Docs (AI-based theory style)
        doc_txt = generate_docs(repo_name, results)   # returns .txt
        doc_pdf = doc_txt.replace(".txt", ".pdf")
        export_to_pdf(doc_txt, doc_pdf)   # ✅ fixed usage
        log_info(f"📄 Documentation saved at: {doc_pdf}")

        # ✅ Tests
        test_file = generate_tests(repo_name, results)
        log_info(f"🧪 Test file generated at: {test_file}")

        # ✅ Final Report
        report_file = build_report(repo_name, results, review_file, doc_pdf, test_file)
        log_info(f"📄 Final Report generated at: {report_file}")
