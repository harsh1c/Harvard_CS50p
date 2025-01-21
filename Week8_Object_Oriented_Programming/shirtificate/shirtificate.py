from fpdf import FPDF
class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", style="B", size=30)
        # Moving cursor to the right:
        self.cell(55)
        # Printing title:
        self.cell(89, 15, "CS50 Shirtificate", border=1, align="C")
        # Performing a line break:
        self.ln(115)

name = input("Name: ")
pdf = PDF()
pdf.add_page()
my_image = pdf.image("shirtificate.png", x=5, y=60 ,w=200,h=210)
pdf.cell(52)
pdf.set_text_color(255, 255, 255)
pdf.cell(85, 15, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")