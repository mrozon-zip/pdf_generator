from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv', delimiter=',')
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
page = 0

for index, row in df.iterrows():
    # Set the header
    pdf.add_page()
    page += 1
    pdf.set_font(family='Helvetica', style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=24, txt=row['Topic'], align='C', ln=1)
    pdf.line(x1=10, x2=200, y1=28, y2=28)

    # Set the lines
    for j in range(28,288, 10):
        pdf.line(x1=20, x2=200, y1=j, y2=j)

    # Set the footer
    pdf.ln(250)
    pdf.set_font(family='Helvetica', style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=str(page), align='R')

    for i in range(row['Pages']-1):
        pdf.add_page()
        page += 1

        # Set the lines
        for j in range(20, 288, 10):
            pdf.line(x1=20, x2=200, y1=j, y2=j)

        # Set the footer
        pdf.ln(274)
        pdf.set_font(family='Helvetica', style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        if page % 2 == 0:
            pdf.cell(w=0, h=10, txt=str(page), align='L')
        else:
            pdf.cell(w=0, h=10, txt=str(page), align='R')

pdf.output('my_document.pdf')