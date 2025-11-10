
from flask import Flask, render_template, request, redirect, url_for, send_file, abort
from core.repo_loader import clone_repo
from core.code_parser import analyze_repo
from core.code_reviewer import review_code
from core.doc_generator import generate_docs
from core.test_generator import generate_tests
from core.report_builder import build_report
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    repo_url = request.form.get("repo_url", "").strip()
    if not repo_url:
        return redirect(url_for("home"))

    # 1) Clone / reuse repo
    repo_path = clone_repo(repo_url)

    # 2) Analyze
    analysis_results = analyze_repo(repo_path)

    # 3) Review / Docs / Tests
    review_file = review_code(analysis_results)
    docs_file   = generate_docs(repo_path, analysis_results)
    tests_file  = generate_tests(repo_path, analysis_results)

    # 4) Final short report
    repo_name = repo_url.rstrip("/").split("/")[-1]
    report_file = build_report(repo_name, analysis_results, review_file, docs_file, tests_file)

    # 5) 4–5 line summary
    summary = (
        f"✅ Repo analyzed: {repo_name}\n"
        f"📂 Files scanned: {len(analysis_results)}\n"
        f"🤖 AI code review generated\n"
        f"📚 Docs + 🧪 Tests ready to download"
    )

    return render_template(
        "result.html",
        summary=summary,
        repo_url=repo_url,
        review_file=review_file,
        docs_file=docs_file,
        tests_file=tests_file,
        report_file=report_file
    )

@app.route("/download")
def download():
    """Serve a file from the data directory safely"""
    path = request.args.get("path")
    if not path:
        abort(404)

    abs_path = os.path.abspath(path)
    data_root = os.path.abspath(DATA_DIR)

    # prevent path traversal; only allow files under /data
    if not abs_path.startswith(data_root):
        abort(403)

    if not os.path.exists(abs_path) or not os.path.isfile(abs_path):
        abort(404)

    return send_file(abs_path, as_attachment=True)

@app.route("/back", methods=["GET"])
def back():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
