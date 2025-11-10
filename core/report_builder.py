# core/report_builder.py
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from utils.logger import log_info, log_error


def build_report(repo_name, results, review_file, doc_file, test_file):
    """Builds a final combined report in both .md and .pdf formats."""

    # ======================
    # 1) Build Markdown Report
    # ======================
    report_md = f"data/reports/{repo_name}_report.md"
    os.makedirs("data/reports", exist_ok=True)

    try:
        with open(report_md, "w", encoding="utf-8") as f:
            f.write(f"# 📊 Final Report for {repo_name}\n\n")

            f.write("## 🔍 Code Analysis Summary\n")
            for r in results[:10]:
                f.write(
                    f"- **File:** {r['file']} | "
                    f"Lines: {r['lines']} | "
                    f"Functions: {len(r['functions'])} | "
                    f"Classes: {len(r['classes'])}\n"
                )

            f.write("\n## 🤖 AI Code Review\n")
            f.write(f"See detailed review in: `{review_file}`\n\n")

            f.write("## 📄 Documentation\n")
            f.write(f"Generated docs: `{doc_file}`\n\n")

            f.write("## 🧪 Test Cases\n")
            f.write(f"Generated tests: `{test_file}`\n\n")

        log_info(f"✅ Markdown report saved at {report_md}")

    except Exception as e:
        log_error(f"⚠️ Error generating Markdown report: {e}")
        return None

    # ======================
    # 2) Build PDF Report
    # ======================
    report_pdf = report_md.replace(".md", ".pdf")
    try:
        doc = SimpleDocTemplate(report_pdf)
        styles = getSampleStyleSheet()
        flow = []

        flow.append(Paragraph(f"📊 Final Report for {repo_name}", styles["Title"]))
        flow.append(Spacer(1, 12))

        flow.append(Paragraph("🔍 Code Analysis Summary", styles["Heading2"]))
        for r in results[:10]:
            flow.append(Paragraph(
                f"File: {r['file']} | Lines: {r['lines']} | "
                f"Functions: {len(r['functions'])} | Classes: {len(r['classes'])}",
                styles["Normal"]
            ))

        flow.append(Spacer(1, 12))
        flow.append(Paragraph("🤖 AI Code Review", styles["Heading2"]))
        flow.append(Paragraph(f"See detailed review in: {review_file}", styles["Normal"]))

        flow.append(Spacer(1, 12))
        flow.append(Paragraph("📄 Documentation", styles["Heading2"]))
        flow.append(Paragraph(f"Generated docs: {doc_file}", styles["Normal"]))

        flow.append(Spacer(1, 12))
        flow.append(Paragraph("🧪 Test Cases", styles["Heading2"]))
        flow.append(Paragraph(f"Generated tests: {test_file}", styles["Normal"]))

        doc.build(flow)
        log_info(f"✅ PDF report saved at {report_pdf}")

    except Exception as e:
        log_error(f"⚠️ Error generating PDF report: {e}")
        return report_md  # fallback only md

    return report_pdf
