# utils/pdf_utils.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def export_to_pdf(input_txt_file, output_pdf_file):
    """Convert a TXT file into a PDF."""
    try:
        c = canvas.Canvas(output_pdf_file, pagesize=letter)
        width, height = letter
        y = height - 40  # starting position

        with open(input_txt_file, "r", encoding="utf-8") as f:
            for line in f:
                if y < 40:  # new page if space runs out
                    c.showPage()
                    y = height - 40
                c.drawString(40, y, line.strip())
                y -= 15

        c.save()
        print(f"✅ PDF created: {output_pdf_file}")
        return output_pdf_file
    except Exception as e:
        print(f"❌ Error while creating PDF: {e}")
        return None

# ✅ Alias for backward compatibility
txt_to_pdf = export_to_pdf
