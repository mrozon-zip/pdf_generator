from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf.set_font(family='Helvetica', style="B", size=12)
pdf.cell(w=0, h=24, txt='Welcome!', align='C', ln=1, border=1)
pdf.set_font(family='Helvetica', style="", size=10)
pdf.cell(w=0, h=24, txt="What's up?", align='L', ln=1, border=1)

pdf.output('my_document.pdf')