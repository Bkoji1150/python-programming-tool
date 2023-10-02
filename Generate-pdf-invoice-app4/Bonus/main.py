import glob
from fpdf import FPDF
from pathlib import Path

pdf = FPDF(orientation="P", unit="mm",format="A4")

filepaths = glob.glob("TextFiles/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    name = filename.title()
    pdf.set_font(family="Times", size=16,style="B")
    pdf.cell(w=50, h=8, txt=name)

    # with open(filepath) as file:
    #     content = file.read()
    #     pdf.cell(w=0, h=5.0, txt=content, ln=0, align="L", border=0)
    pdf.output("PDFs/out.pdf")
