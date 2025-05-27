from fpdf import FPDF
import json

def generate_pdf():
    with open("data/results.json") as f:
        results = json.load(f)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Assignment Marks", ln=True, align='C')
    pdf.ln(10)

    for roll, mark in results.items():
        pdf.cell(200, 10, txt=f"Roll No: {roll} — Marks: {mark}", ln=True)

    pdf_path = "results/report.pdf"
    pdf.output(pdf_path)
    return pdf_path
